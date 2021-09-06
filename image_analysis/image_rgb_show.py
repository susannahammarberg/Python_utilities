# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:04:29 2019

@author: Sanna
"""
import matplotlib.pyplot as plt
import os
# fetching a random png image from my home directory, which has size 258 x 384
img_file = os.path.expanduser("dog.png")

from scipy import misc
# read this image in as a NumPy array, using imread from scipy.misc
M = misc.imread(img_file)

plt.figure()
plt.imshow(M)
    #displayList=numpy.array(image).T
    #im1 = Image.fromarray(displayList)
    #im1.show()