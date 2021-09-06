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
im = mpimg.imread(r'C:\Users\Sanna\Documents\Figures\circle_256.png')
#load() 
#im = mpimg.imread('C:/Users/Sanna/Documents/python_utilities/fft2_images/cali.jpeg')#single.png')#L.png circle_insquare.png')

arim = np.array(np.sum(im, axis=2))
np.save('circle_256',arim)
# complex
#arim = 1j*np.array(np.sum(im, axis=2))

padding = 0
arim=np.pad(arim, ((padding,padding),(padding,padding)), 'constant', constant_values=(0, 0))

# choose a smaller part of the image
choose_roi = 0
if choose_roi == 1:
    size= 20
    dx=25
    ceny = arim.shape[0]/2; cenx = arim.shape[0]/2 + dx
    #arim = arim[ ceny-size : ceny+size, cenx -size : cenx+size ]
    arim = arim[105:160,210:260]



fftim= fft.fftshift(fft.fft2(arim))

plt.figure()
plt.subplot(121)
plt.imshow(abs(arim),cmap='bone'); plt.title('Cali'); plt.axis('off') #;plt.colorbar()
plt.subplot(122); plt.title('log10 FFT2 Cali'); plt.axis('off')
plt.imshow(np.log10(abs(fftim)),cmap='jet')#winter')
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