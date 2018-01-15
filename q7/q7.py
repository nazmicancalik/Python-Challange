#!/usr/bin/python

from PIL import Image
import re

img = Image.open("oxygen.png",'r')

row = [img.getpixel((x,img.height/2)) for x in range(img.width)]

# 7 repeat
row = row[::7]
ords = [r for r, g, b, a in row if r == g == b]
#map ascii to values
text = "".join(map(chr, ords))
print (text)

#This list contains strings. Map them to ints before use
next_level_nums = re.findall("\d+", text)
print(next_level_nums)

next_level = "".join(map(chr, map(int, next_level_nums)))
print (next_level)
