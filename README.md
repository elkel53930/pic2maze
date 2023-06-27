# pic2maze

This script converts the image data of mazes from past Micromouse competitions published on the [NFT web page](https://www.ntf.or.jp/mouse/history/index.html) into text.


## Notice

The image data published on the NFT web page has the starting point in the lower left corner.
However, for the convenience of me, the output text has the starting point in the upper left corner.
In other words, the maze is rotated 90 degrees clockwise.

## Constraint

Currently only classic maze is supported.

## Python version

This script is developed with Python 3.10.

## Dependencies

```
pip install opencv-python
```

## Usage

To process single file.
```
./pic2maze.py {bmp_file} > {output_text_file}
```

To process all files under the directory:.
```
./run.sh {directory_name}
```
