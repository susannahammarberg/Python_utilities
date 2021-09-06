# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:50:18 2018

@author: Sanna

Does this function make sense?
"""

def bright_field_voxels(data,x,y):
    index = 0
    photons = np.zeros((y,x)) 
    for row in range(0,y):
        for col in range(0,x):
            #instead of saving data (0,0), save up all diffpatterns for that position, that is, every 
            photons[row,col] = sum(sum(sum(data[index,:])))#/ max_intensity
            index += 1
            
    return photons
brightfield_voxel = bright_field_voxels(diff_data,nbr_cols,nbr_rows)
