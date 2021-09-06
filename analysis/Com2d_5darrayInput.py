# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:14:10 2018

@author: Sanna
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import io
scans = range(192, 200+1)+range(205, 222+1)

def COM2d(data,nbr_cols,nbr_rows):
    for rot in range(0, len(scans)):
        # define a vector with length of detector-roi width
        roix = np.linspace(0, data.shape[4], data.shape[4])
        # define a vector with height of detector-roi width
        roiy = np.linspace(0,data.shape[3],data.shape[3])     
        # meshgrids for center of mass calculations
        X, Y = np.meshgrid(roix,roiy)
        
        COM_hor = np.zeros((nbr_rows,nbr_cols))
        COM_ver = np.zeros((nbr_rows,nbr_cols))
        COM_mag = np.zeros((nbr_rows,nbr_cols))
        COM_ang = np.zeros((nbr_rows,nbr_cols))
             
        for row in range(0,nbr_rows):
            for col in range(0,nbr_cols):
                COM_hor[row,col] = sum(sum(data[rot,row,col]*X))/sum(sum(data[rot,row,col]))
                COM_ver[row,col] = sum(sum(data[rot,row,col]*Y))/sum(sum(data[rot,row,col]))
                if row == 0 and col == 0:
                    bkg_hor = 98.9#65.1#152#COM_hor[row,col] #152.4#
                    bkg_ver = 239.1#64.6#101#COM_ver[row,col]  #101.8#
                # DPC in polar coordinates. r then phi:
                COM_mag[row, col] = np.sqrt( (COM_hor[row,col]-bkg_hor)**2 + (COM_ver[row,col]-bkg_ver)**2) 
                COM_ang[row, col] = np.arctan( (COM_hor[row,col]-bkg_hor) / (COM_ver[row,col]-bkg_ver))
        
        io.savemat('scan%d_COM_ang.mat'%((scans[rot])),{"COM2d_mag":COM_mag})  
           
        np.disp(rot)
    return COM_ang, COM_mag, COM_hor, COM_ver
COM_ang, COM_mag, COM_hor, COM_ver = COM2d(diffSet_Pil100K, nbr_cols, nbr_rows)

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

plt.figure()
plt.imshow(COM_ang, cmap='gray', interpolation='none')#, extent=[motorpositionx[0], motorpositionx[-1], motorpositiony[0], motorpositiony[-1] ])
plt.title('Scan %d: COM_ang on %s'%((scans[rot]),analyse_detector_name_string))
plt.xlabel('Nominal motorpositions [um]')
plt.colorbar()
plt.savefig('C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d\scan%d_COM_ang'%((scans[rot])), bbox_inches='tight')


plt.figure()    
plt.imshow(COM_mag, cmap = 'gray', interpolation='none')#, extent=[motorpositionx[0], motorpositionx[-1], motorpositiony[0], motorpositiony[-1] ])
plt.title('Scan %d: COM mag %s'%((scans[rot]),analyse_detector_name_string))
#plt.xlabel('Nominal motorpositions [um]')
#plt.ylabel('Nominal motorpositions [um]')
plt.colorbar()  
plt.savefig('C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d\scan%d_COM_mag'%((scans[rot])), bbox_inches='tight')
