from PIL import Image
import numpy as np
img = Image.open('wire.png')
pdata = np.asarray(img)
w, h = img.size
deimg = [ [0 for i in range(100)] for j in range(100)]
for i in range(100):
    deimg[i] = pdata[0][100*i: 100*i+100]
Image.fromarray(np.array(deimg)).show() # bit.html says "you took the wrong curve."

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
deimg_spiral = [ [0 for i in range(100)] for j in range(100)]
pos = 0
x, y = 0, 0
for i in range(100, -1, -2):
    for d in range(4):
        for j in range(i-1):
            deimg_spiral[x][y] = pdata[0][pos]
            pos += 1
            x += direct[d][0]
            y += direct[d][1]
    x += 1
    y += 1
Image.fromarray(np.array(deimg_spiral)).save('out.png')