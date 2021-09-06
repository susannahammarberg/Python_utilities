# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:33:15 2021

@author: Sanna
"""

import matplotlib.pyplot as plt
import numpy as np

vect = [ [ 1, 2, 3], [4,5,6], [7,8,9]]



plt.figure()
plt.imshow(vect,cmap='jet')



# load and display an image with Matplotlib

from matplotlib import image

from matplotlib import pyplot
import numpy as np
# load image as pixel array

imag = image.imread('lone2.jpg')

# summarize shape of the pixel array

print(imag.dtype)

print(imag.shape)

# display the array of pixels as an image
imag = imag[:,:,0]

pyplot.imshow(imag)

pyplot.xlabel('q1')
pyplot.show()


im_tr = imag[::-1]
pyplot.figure()
pyplot.imshow(im_tr)
pyplot.ylabel('q1')

