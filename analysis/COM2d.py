# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 12:04:14 2018

@author: Sanna
"""

import matplotlib.pyplot as plt
import numpy as np
def COM2d(data,nbr_cols,nbr_rows):

    nbr_rows=17
    nbr_cols=21
    # define a vector with length of the length of roi on the detector
    roix = np.linspace(1, data.shape[1], data.shape[1])
    ## define a vector with length of the height of roi on the detector
    roiy = np.linspace(1,data.shape[2],data.shape[2])     #shape 1 or 2 ?
    # meshgrids for center of mass calculations
    X, Y = np.meshgrid(roix,roiy)
    
    COM_hor = np.zeros((nbr_rows,nbr_cols))
    COM_ver = np.zeros((nbr_rows,nbr_cols))
    COM_mag = np.zeros((nbr_rows,nbr_cols))
    COM_ang = np.zeros((nbr_rows,nbr_cols))
    index = 0
    for row in range(0,nbr_rows):
        for col in range(0,nbr_cols):
            COM_hor[row,col] = sum(sum(data[index]*X))/sum(sum(data[index]))
            COM_ver[row,col] = sum(sum(data[index]*Y))/sum(sum(data[index]))
            if row == 0 and col == 0:
                bkg_hor = 65.1#152#COM_hor[row,col] #152.4#
                bkg_ver = 64.6#101#COM_ver[row,col]  #101.8#
            # DPC in polar coordinates. r then phi:
            COM_mag[row, col] = np.sqrt( (COM_hor[row,col]-bkg_hor)**2 + (COM_ver[row,col]-bkg_ver)**2) 
            COM_ang[row, col] = np.arctan( (COM_hor[row,col]) / (COM_ver[row,col]))
    
            index += 1
        #return COM_ang
        
    plt.figure()
    plt.imshow(COM_hor, cmap='jet')
    plt.colorbar()
    plt.figure()
    plt.imshow(COM_ver, cmap='jet')
    plt.colorbar()
    plt.figure()
    plt.imshow(COM_mag, cmap='jet')
    plt.colorbar()
    plt.figure()
    plt.imshow(COM_ang, cmap='jet')
    plt.colorbar()
    
    return 0