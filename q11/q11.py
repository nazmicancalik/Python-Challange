#!/usr/bin/python

from PIL import Image

img=Image.open("cave.jpg")

size = list(img.size)

#For even odd pixel division
size[0] /= 2
size[1] /= 2

downsized = img.resize(size, Image.NEAREST) # NEAREST drops the lines
downsized.save("answer.png")