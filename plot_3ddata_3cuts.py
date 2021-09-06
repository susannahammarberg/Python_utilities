# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:50:28 2018

@author: Sanna
"""

# general function for plotting central cuts of 3d data
def plot3ddata(data):
    plt.figure()
    plt.suptitle('Single position Bragg peak')
    plt.subplot(221)
    #plt.title('-axis')
    plt.imshow((abs((data[data.shape[0]/2,:,:]))), cmap='jet', interpolation='none') 
    plt.colorbar()
    plt.subplot(222)
    #plt.title('-axis')
    plt.imshow(abs(data[:,data.shape[1]/2,:]), cmap='jet', interpolation='none') 
    plt.colorbar()
    plt.subplot(223)
    #plt.title('-axis')
    plt.imshow((abs(data[:,:,data.shape[2]/2])), cmap='jet', interpolation='none') 
    plt.colorbar()
    
plot3ddata(input_data)