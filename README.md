# Image Resizer

Script to resize image.

# How to install

You should install packages from requirements.txt

```bash

pip install requirements.txt

```

# Quick Start

```bash
usage: re_size.py [-h] --input_path INPUT_PATH [--height HEIGHT]
                  [--width WIDTH] [--scale SCALE] [--output_path OUTPUT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH
                        path to the image
  --height HEIGHT       height of the result image
  --width WIDTH         width of the result image
  --scale SCALE         scale of the result image
  --output_path OUTPUT_PATH
                        path, where we should save image
 ```
 
 Example of using on Mac OS. Input file has size: 830x222:
 ```bash
 python re_size.py --input_path image.png --scale 2
 ```
 Result: image__1660x444.png

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
