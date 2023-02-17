#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image
import sys

''' ./imcon.py <dir path> '''

#takes input in the CLI for the path of images
input = sys.argv[1]
#creates the path using Path module
dir = Path(input)

#makes a list of all the image files
images = os.listdir(dir)
#moves inside the directory to interact with the files
os.chdir(dir)

for file in images:
    #skip all the hidden files that start with "."
    if file[0] == '.':
        continue
    else:
        im = Image.open(file)
        #need to convert to RGB prior to changing the format
        new_im = im.rotate(90).resize((128,128)).convert('RGB').save("/opt/icons/{}".format(file), format='jpeg')
