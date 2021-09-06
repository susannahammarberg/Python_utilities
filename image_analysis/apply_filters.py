# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:15:35 2017

@author: Sanna
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.signal import convolve2d as conv2
shapes = misc.imread('shapes.jpg',flatten=True)

#shape = np.zeros((shapes.shape))

#image = misc.imread('P.png')

# create filters
###############################################

#  mark horizontal edges
f1 = np.array([[0,-1],
                [0,1]])

#  mark horizontal edges but opposite signs
f2 = np.array([[1,0],
                [-1,0]])

# filter to mark vertical edges
f3 = np.array([[1,-1],
                [0,0]])

f6 = np.array([[0, 1],
               [-1,0]])

g=conv2(shapes,f3)
plt.figure()
plt.imshow(shapes,cmap='gray')
plt.title('Original')
plt.colorbar()
#plt.figure()
plt.imshow(g,cmap='gray')
plt.title('convolution')
