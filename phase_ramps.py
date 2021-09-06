# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:57:27 2018

@author: Sanna
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#from create2Dgaussian2 import create2Dgaussian2  #import all functions
from scipy import misc
from math import ceil
import matplotlib.animation as animation

def data():
#    data = np.genfromtxt("diffractionPattern.txt", dtype='float')
    #image = misc.imread('P.png',flatten=True)
    #p = misc.imread('star.bmp',flatten=True)
    #absF = abs(np.fft.fftshift(np.fft.fft2(p)))
    ########### Test att använda fft av kristall som inputi shrinkwrap
    crystal = np.zeros((201,201), dtype= np.int32)
    
    dx=1
    for row in range(60,140,dx):
        for col in range(60,140,dx):
            crystal[row,col] = 1
    
    crystal_fourier = np.fft.fftshift(np.fft.fft2(crystal))
    absF = abs(crystal_fourier)**2
    return (absF,crystal)
#absF, crystal = data()

#############Test att använda bild som är skjuvad coord
#image = misc.imread('amp.bmp')[:,:,0]
#image2 = misc.imread('sljus.bmp')[:,:,0]
frog = misc.imread('C:/Users/Sanna/Documents/CDI_2017/CXI/Shrinkwrap/frog.jpg')[:,:,0]
horse = misc.imread('C:/Users/Sanna/Documents/Kurser/Paganin_course/lecture_CDI/horse.png')[:,:,0]


#frog = horse
plt.figure()
plt.imshow(frog)

plt.figure()
plt.imshow(np.log10(abs(np.fft.fftshift(np.fft.fft2((frog))))))

# testing the numpy 'roll' function for shifting an array by x nbr of columns
def test_roll(array):
    plt.figure()
    plt.imshow(array)
    array = np.roll(array, 1)
    plt.figure()
    plt.imshow(array)
#test_roll(np.array([[1,2,3],[1,2,3]]))
    
# a phses ramp is introduced for example when the diffraction pattern is 
# shifted by one column
    # does not work if you use fftshift

plt.figure()
plt.imshow(abs(np.log10(np.roll(np.fft.fft2(frog), 1))))

plt.figure()
plt.imshow(np.log10(abs(np.fft.fft2(np.roll(np.fft.fft2(frog), 1)))))


