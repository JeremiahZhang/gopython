# -*- coding: utf-8 -*-
import os
import glob
from PIL import Image

size = 460, 284

i = 0
# print size

for infile in glob.glob("*.jpg"):
    i += 1
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.resize(size, Image.ANTIALIAS)
    im.save(file + ext)
    print i

print "Resize {0} images successfully.".format(i)

    
"""
Resize my jpg image to size(460x284)
"""
