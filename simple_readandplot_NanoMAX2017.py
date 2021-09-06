# -*- coding: utf-8 -*-
"""
Created on Thursday June 29 11:40 2017


Reading of the NanoMAX 2017 data, Merlin detector. 

FLYSCANS saves all images in the fast axis in one file.

Ex: flyscan 192 with 17 rows (slow axis) and 21 cols (fast axis)
    will have 17 hdf5 files called 'scan_0192_merlin_0000' to 'scan_0192_merlin_0016'
    with 21 images in each file

For MESH SCANS the files are saved one file for each image: 
    scan_0192_merlin_0000' - 'scan_0192_merlin_xxxx', xxxx=numbr_of_points



Masking and choosing roi of data. plot single diffraction images.  


@author: Susanna Hammarberg

"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import h5py
import matplotlib.animation as animation


# choose scan nbr:
scan_name_int = 192#354#192
scan_name_string = '%d' %scan_name_int   

directory = 'D:/exp20170628_Wallentin_nanomax/exp20170628_Wallentin/JWX33_NW2/scan_0%d_merlin_'%scan_name_int
directory_pil100K = 'D:/exp20170628_Wallentin_nanomax/exp20170628_Wallentin/JWX33_NW2/scan_0%d_pil100K_'%scan_name_int 
metadata_directory = 'D:/exp20170628_Wallentin_nanomax/exp20170628_Wallentin/JWX33_NW2/JWX33_NW2.h5' 


# choose which row (slow axis) to load
row = 8
# load hdf5-file (all fast axis data in single file)
scan = h5py.File( directory  + str('{0:04}'.format(row)) + '.hdf5','r') # read-only
# load and store in np array
data_Merlin =  np.flipud(np.array((scan.get('/entry_0000/measurement/Merlin/data')), dtype=np.int32))

# plot a single image col
col = 0
fig = plt.figure()
plt.title('Raw single Merlin image')
plt.imshow(np.log10(abs((data_Merlin[col]))), cmap = 'jet', interpolation = 'none')
plt.colorbar()

# plot sum of all images
fig = plt.figure()
plt.title('sum of all raw single Merlin images on one row')
plt.imshow(np.log10(abs(sum(data_Merlin))), cmap = 'jet', interpolation = 'none')
plt.colorbar()

def create_mask_Merlin():
    # Alex mask:
    data = np.load('C:/Users/Sanna/Documents/Beamtime/NanoMAX062017/merlin_mask(1).npy')
    return data

mask_Merlin = create_mask_Merlin()

# apply mask to Merlin data
data_Merlin = data_Merlin*(1-mask_Merlin)

fig = plt.figure()
plt.title('Masked Merlin image')
plt.imshow(np.log10(abs((data_Merlin[0]))), cmap = 'jet', interpolation = 'none')
plt.colorbar()

def choose_roi(roix_start,roix_end,roiy_start,roiy_end):
    a = data_Merlin[:, roiy_start:roiy_end, roix_start:roix_end]
    return a

# choose a roi for Merlin data
data_Merlin = choose_roi(roix_start = 100,roix_end = 350,roiy_start = 200,roiy_end = 500)

fig = plt.figure()
plt.title('Masked Merlin image')
plt.imshow(np.log10(abs((data_Merlin[0]))), cmap = 'jet', interpolation = 'none')
plt.colorbar()
        
fig = plt.figure()
plt.title('sum of all Masked Merlin image on one row')
plt.imshow(np.log10(abs(sum(data_Merlin))), cmap = 'jet', interpolation = 'none')
plt.colorbar()
        