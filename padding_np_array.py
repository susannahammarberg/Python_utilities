# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:01:02 2018

@author: Sanna
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import fft
import numpy as np

#f = open('C:/Users/Sanna/Documents/python_utilities/fft2_images/img.PNG')
#load() 
im = mpimg.imread('C:/Users/Sanna/Documents/kurser/modernXrayPhysics_vt2019/laser_lab/2019_02_22/IMG_0015.jpg')
padding = 5000
arim=np.pad(np.rot90(np.array(np.sum(im, axis=2))), ((padding,padding),(padding,padding)), 'constant', constant_values=(14, 14))
#((3, 2), (2, 3))


fftim= fft.fftshift(fft.fft2(arim))

plt.figure()
plt.subplot(121)
plt.imshow(arim, cmap='jet' )
plt.colorbar()
plt.show()
plt.subplot(122)
plt.imshow(np.log10(abs(fftim)), cmap='jet')
plt.colorbar()

#f = open('photo.jpg', 'r+')
#jpgdata = f.read()
#f.close()

