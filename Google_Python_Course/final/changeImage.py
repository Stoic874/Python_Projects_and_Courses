#!/usr/bin/env python3

import os
from PIL import Image
import sys

# Change image resolution from 3000x2000 to 600x400
# Convert to RGB to change the format
# Change image format from .TIFF to .JPEG
# Save the images in ~/supplier-data/images

dir = sys.argv[1]
files = os.listdir(dir)
for f in files:
    path = os.path.join(dir, f)
    print("Converting: {}".format(path))
    if f[0] != ('0'):
        print("Skipping...")
    else:
        im = Image.open(path)
        new_im = im.resize((600, 400)).convert('RGB').save("supplier-data/images/{}.jpeg".format(f[:-5], format='jpeg'))
