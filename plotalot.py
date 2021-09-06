# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:34:32 2019

@author: Sanna


Collection of plotting functions

"""
import matplotlib.pyplot as plt
import time
import numpy as np
date_str = time.strftime("%Y%m%d") # -%H%M%S")


# This functions plot all brightfield maps in an array
# aswell as the average vale and sum of all
# Scans is an array of scan numbers
def plot_BF(data, interval=1,save=True,scans=np.arange(1000),extent = None , savepath = 'C:/Users/Sanna/Documents/temp/' ): #,
    
    #plot every something 2d bright fields
    for ii in range(0,data.shape[0],interval):
        plt.figure()
        plt.imshow(data[ii], cmap='jet', interpolation='none',extent=extent) 
        plt.title('Bright field #S %d'%scans[ii])  
        plt.xlabel('x [$\mu m$]') 
        plt.ylabel('y [$\mu m$]')
        if save==True:
            plt.savefig(savepath +date_str+ '_BF_scan%d'%((scans[ii])), bbox_inches='tight')
#            #plt.savefig("BF/scan%d"%scans_gonphi[ii])   
    # plot average bright field image (average over rotation)
    plt.figure()
    plt.imshow(np.mean(data, axis=0), cmap='jet', interpolation='none',extent=extent)
    plt.title('Average image from bright field') 
    plt.xlabel('$x$ [$\mu m$]') 
    plt.ylabel('$y$ [$\mu m$]')
    if save==True:
        plt.savefig(savepath + date_str +'_average_brightfield')     
    
    plt.figure()
    plt.imshow(sum(data), cmap='jet', interpolation='none',extent=extent)
    plt.title('Bright field summed over all positions') 
    plt.xlabel('$x$ [$\mu m$]') 
    plt.ylabel('$y$ [$\mu m$]')


def plot_XRD_xyz(XRD_qx, XRD_qy, XRD_qz, brightfield, factor, extent):
    # plot reciprocal space map x y z 
    plt.figure()
    plt.subplot(411)
    plt.imshow(factor*XRD_qx, cmap='jet',interpolation='none',extent=extent)
    plt.title('Reciprocal space map, $q_x$ $ (\AA ^{-1}$) ')
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    plt.subplot(412)
    plt.imshow(factor*XRD_qy, cmap='jet',interpolation='none',extent=extent) 
    plt.title('Reciprocal space map, $q_y$ $ (\AA ^{-1}$) ')
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    plt.subplot(413)
    plt.imshow(factor*XRD_qz, cmap='jet',interpolation='none',extent=extent)
    plt.title('Reciprocal space map, $q_z$ $(\AA ^{-1}$) ')
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    plt.subplot(414)
    plt.title('Bright field (sum of all rotations)')
    plt.imshow(sum(brightfield)/sum(brightfield).max(), cmap='jet', interpolation='none',extent=extent)
    plt.xlabel('x [$\mu m$]') 
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    


if __name__ == '__main__':
    
    print 'this'
    fake_data = np.arange(3*4*5).reshape(3,4,5)
    plot_BF(data=fake_data)
