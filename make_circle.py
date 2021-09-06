# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:57:05 2020

@author: Susanna


Make a circle
"""

import numpy as np
import matplotlib.pyplot as plt



r = 10
xdim = 5
ydim = 128
A = np.zeros((ydim,xdim))
S = np.ones((ydim,xdim))

ycen = int(ydim/2)
xcen = int(xdim/2)
for x in range(xdim):
    for y in range(ydim):
        if (xcen-x)**2 + (ycen-y)**2 \
           <= r**2:
            A[y,x] = 1


#make a circular filter from a x and y grid
x = np.linspace(-5,5,xdim)
y = np.linspace(-6,6,ydim)
xv, yv = np.meshgrid(x,y)
mask = np.sqrt(xv**2 + yv**2)
import matplotlib.pyplot as plt
plt.figure(); plt.imshow(mask); plt.show()
plt.figure(); plt.imshow(S); plt.colorbar(); plt.show()
slow = -3
shigh = 3
S[(mask > shigh) | (mask < slow)] *= 0
plt.figure(); plt.imshow(S); plt.show()
import pdb; pdb.set_trace()

S[(s > shigh) | (s < slow)] *= 0
        
plt.figure(); plt.imshow(A); plt.show()
