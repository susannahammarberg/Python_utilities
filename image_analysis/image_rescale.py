# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:01:02 2018

@author: Sanna
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#from scipy.misc import imresize # deprecated
from skimage.transform import resize
from skimage.transform import rescale
import numpy as np

#f = open('C:/Users/Sanna/Documents/python_utilities/fft2_images/img.PNG')
#load() 
im = mpimg.imread('dog.png')#L.png circle_insquare.png')
im = mpimg.imread('C:/Users/Sanna/Documents/python_utilities/fft2_images/cali.jpeg')#L.png circle_insquare.png')

arim=np.array(np.sum(im, axis=2), dtype=np.uint8)
# complex
#arim = 1j*np.array(np.sum(im, axis=2))

padding = 0
arim=np.pad(arim, ((padding,padding),(padding,padding)), 'constant', constant_values=(0, 0))

#scale image by a certain factor
scale = 5
im2 = rescale(arim, scale=scale, order=1, mode='reflect', cval=0, clip=True, preserve_range=True, multichannel=False, anti_aliasing=False, anti_aliasing_sigma=None)
# resize image to match a certain size
#im2 = resize(arim,output_shape = (256,256), order = 1, anti_aliasing = False)

plt.figure()
plt.subplot(121)
plt.imshow(abs(arim)); plt.title('Array')#; plt.axis('off') #;plt.colorbar()
plt.subplot(122); plt.title('rescaled factor %f'%scale)#; plt.axis('off')
plt.imshow(abs(im2))#winter')
plt.tight_layout()
#plt.colorbar()

#f = open('photo.jpg', 'r+')
#jpgdata = f.read()
#f.close()

# if complex
#-----------------

#plt.figure()
#plt.subplot(121)
#plt.imshow(abs(arim)); plt.title('Array'); plt.axis('off') #;plt.colorbar()
#plt.subplot(122); plt.title('phase'); plt.axis('off')
#plt.imshow(np.angle(arim),cmap='winter')
#plt.tight_layout()