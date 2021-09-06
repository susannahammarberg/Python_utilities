# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:43:55 2019

@author: Sanna


Save as sannas_analysis

"""
import numpy as np
# function for calculating bright field of data
# input is the data as a 3D array with dimension data[scans_y * scans_x][yPixels][xPixels]
def bright_field(data,x,y, index_arr=None):
    index = 0
    photons = np.zeros((y,x))     
    for row in range(0,y):
        for col in range(0,x):
            # dependet on how the scan was done
            if index == None:
                photons[row,col] = sum(sum(data[index])) 
            elif index != None:
                photons[row,col] = sum(sum(data[index_arr[index]])) #/ max_intensity
            
            index += 1            
    return photons



# input is 4d matrix with [nbr_diffpatterns][nbr_rotations][nbr_pixels_x][nbr_pixels_y]
def COM_voxels_reciproc(data, vect_Qx, vect_Qz, vect_Qy ):

    # meshgrids for center of mass calculations in reciprocal space
    COM_qx = np.sum(data* vect_Qx)/np.sum(data)
    COM_qz = np.sum(data* vect_Qz)/np.sum(data)
    COM_qy = np.sum(data* vect_Qy)/np.sum(data)

   # print 'coordinates in reciprocal space:'
   # print COM_qx, COM_qz, COM_qy
    return COM_qx, COM_qz, COM_qy




if '__name__'== '__main__':
    
    #test function
    print 'TODO implement test functions'
    
    