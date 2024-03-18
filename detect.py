from __future__ import division

# conda create --name pychorus_my
# conda activate pychorus_my
# conda install python
# pip install librosa
# pip install moviepy

import os
import argparse
from pychorus import helpers
from pychorus.helpers import find_and_output_chorus

def rename_file(name, chorus):
    filename = os.path.splitext(name)

    if not chorus is None:
        val1, val2 = chorus
        
        # format the input values as strings with two decimal places
        formatted_val1 = "{:.3f}".format(val1).replace(".","")
        formatted_val2 = "{:.3f}".format(val2).replace(".","")
        
        # define the new file names
        new_filename = f"{filename[0]}_{formatted_val1}_{formatted_val2}_true.mp4"

        # rename the file using the os module
        os.rename(name, new_filename)
    else:
        new_filename = f"{filename[0]}_false.mp4"

        # rename the file using the os module
        os.rename(name, new_filename)

def enumerate_files(args):
    if not args.m3u is None:
        with open(args.m3u, "r") as m3u_file:
            lines = m3u_file.readlines()

        files = []

        for line in lines:
            # skip comment lines
            if line.startswith("#"):
                continue
            # add file name to list
            files.append(line.strip())
    else:
        files = [args.input_file]
        
    return files

def main(args):
    files = enumerate_files(args)
    
    for file in files:
    
        basename = os.path.basename(file)
        
        if not os.path.exists(file):
            print(basename, 'Not found (already processed?)')
        elif basename.endswith('true') or basename.endswith('false'):
            print(basename, 'Already processed')
        else:
            chroma, song_wav_data, sr, song_length_sec = helpers.create_chroma(file)
            chorus = helpers.find_chorus(chroma, sr, song_length_sec, args.min_clip_length)
            
            if not chorus is None:
                print(basename, 'chorus found at', str(int(chorus[0])),'->', str(int(chorus[1])))
            else:
                print(basename, 'No chorus found')

            rename_file(file, chorus)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse all audio files from M3U file or single file")
    parser.add_argument("input_file", nargs="?", help="Path to input audio file")
    parser.add_argument("-m3u", nargs="?", help="Path to input M3U file")
    parser.add_argument(
        "--min_clip_length",
        default=15,
        help="Minimum length (in seconds) to be considered a chorus")

    main(parser.parse_args())

