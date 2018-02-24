#!/usr/bin/python
from PIL import Image

img = Image.open("wire.png")

pix = img.load()
new_pix = pix
