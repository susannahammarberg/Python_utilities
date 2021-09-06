# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:37:26 2018

@author: Sanna
"""


# its not so good its a bit wired
# input here is 4d matrix with [nbr_diffpatterns][nbr_rotations][nbr_pixels_x][nbr_pixels_y]
def COM_voxels_reciproc(data, vect1, vect2, vect3):
    # define a vector with length of the length of roi on the detector
    #roix = np.linspace(1, data.shape[2], data.shape[2])
    ## define a vector with length of the height of roi on the detector
    #roiy = np.linspace(1,data.shape[3],data.shape[3])
    #roiz = np.linspace(1,nbr_rot,nbr_rot)    
    # meshgrids for center of mass calculations
    #Z, X, Y = np.meshgrid(roix,roiz,roiy)
    
    # meshgrids for center of mass calculations in reciprocal space
    #TODO why in this order?
    Qx,Qz,Qy = np.meshgrid(vect1,vect3,vect2)
    
    
#    COM_hor = np.zeros((nbr_rows,nbr_cols))
#    COM_ver = np.zeros((nbr_rows,nbr_cols))
#    COM_rot = np.zeros((nbr_rows,nbr_cols))
#    COM_mag = np.zeros((nbr_rows,nbr_cols))
#    COM_ang = np.zeros((nbr_rows,nbr_cols))
#    index = 0
#    for row in range(0,nbr_rows):
#        for col in range(0,nbr_cols):
#            threshold = 3000   #dont know how to set this threshold. but should be when the data it is summung is just some single photon ocunts on each image
#            if sum(sum(sum(data[index]))) > threshold:
    
    COM_x = sum(sum(sum(data* Qx)))/sum(sum(sum(data)))
    COM_y = sum(sum(sum(data* Qy)))/sum(sum(sum(data)))
    COM_z = sum(sum(sum(data* Qz)))/sum(sum(sum(data)))
#            else:
#                COM_hor[row,col] = 13.616534672254996      # == np.mean(COM_hor) without the if-sats
#                COM_ver[row,col] = 64.117565383940558
#                COM_rot[row,col] = 61.397211314625821             
#                print 'peeeeep'
#
#            if row == 0 and col == 0:
#                bkg_hor = 152.4#65.1#152#COM_hor[row,col] #152.4#
#                bkg_ver = 101.8#64.6#101#COM_ver[row,col]  #101.8#
#                bkg_rot = 0
#            # DPC in polar coordinates. r then phi: . although does not make much sence
#            COM_mag[row, col] = np.sqrt( (COM_hor[row,col]-bkg_hor)**2 + (COM_ver[row,col]-bkg_ver)**2 + (COM_rot[row,col]-bkg_rot)**2) 
#            COM_ang[row, col] = np.arctan( (COM_hor[row,col]) / (COM_ver[row,col]))
#    
            #index += 1
    print 'coordinates in reciprocal space:'
    print COM_x, COM_y, COM_z
    return COM_x, COM_y, COM_z
