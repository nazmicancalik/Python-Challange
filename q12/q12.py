#!/usr/bin/python
data = open("evil2.gfx","rb").read()

#This next line is not useful.
#print (data)

#We divide the data (gfx file) into 5 chunks making each one of them an image.
#Save the images and concat the findings.
for i in range(5):
	open('%d.png' % i, 'wb').write(data[i::5])

#Open images with GNU Emacs GUI to see the images properly.