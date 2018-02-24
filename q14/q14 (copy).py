#!/usr/bin/python
from PIL import Image

img=Image.open("wire.png")

'''
size = list(img.size)
size[0] /= 2
size[1] /= 2
downsized = img.resize(size, Image.NEAREST) # NEAREST drops the lines
downsized.save("answer.png")
'''

pix = img.load()
new_pix = img.load()

t = 100
isRow = True
start = 0
stop = 100
rowNumberUp = 99
rowNumberDown = 0
rowNumber = rowNumberDown

colNumberUp = 99
colNumberDown = 0
colNumber = colNumberUp
for i in range(start,stop):
	if isRow:
		new_pix[rowNumber,i] = pix[rowNumber,i]
		if (stop == i):
			isRow = False
			if rowNumber > rowNumberDown:
				rowNumberUp = rowNumberUp - 2
			else:
				rowNumberDown = rowNumberDown + 2
	else:
		new_pix[i,colNumber] = pix[i,colNumber]
		if (stop == i):
			isRow = True
			if colNumber > colNumberDown:
				colNumberUp = colNumberUp - 2
			else:
				colNumberDown = colNumberDown + 2
print('Width of the image is: ' + str(img.width))