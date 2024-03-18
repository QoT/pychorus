# Pychorus

Pychorus is an open source library to find choruses or interesting sections in pieces of music. The algorithm is largely based on [a paper](https://pdfs.semanticscholar.org/f120/3fb2efe2f251ea7c221c9eaca95cc163594b.pdf) by Masataka Goto with some simplifications and modifications. There is room for improvement so feel free to contribute to the project.

Check out blog post: https://towardsdatascience.com/finding-choruses-in-songs-with-python-a925165f94a8 for a full explanation on how the library works

## Getting Started

You can install the codebase easily with

```
git clone https://github.com/QoT/pychorus

If using Conda, you may use this install procedure:

conda create --name pychorus
conda activate pychorus
conda install python
pip install librosa
pip install moviepy

```

### Sample execution

The most straightforward way to use the module is as follows for m3u file:


```
python detect.py -m3u "/Users/nickburrett/Downloads/Input Files/playlist.m3u"

or for individual file:

python detect.py -m3u "/Users/nickburrett/Downloads/Input Files/50 Cent - In Da Club (Clean Single).mp4"

```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
