# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 11:40:48 2018

@author: Sanna
"""

# function for calculating bright field of data
# input is the data as a 3D array with dimension data[scans_y * scans_x][yPixels][xPixels]
def bright_field(data,x,y):
    import numpy as np
    index = 0
    photons = np.zeros((y,x)) 
    for row in range(0,y):
        for col in range(0,x):
            photons[row,col] = sum(sum(data[index])) #/ max_intensity
            index = index+1
            
    return photons