# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 12:04:14 2018

@author: Sanna
"""

def COM2d(data,nbr_cols,nbr_rows):
    
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
    
    for row in range(0,nbr_rows):
        for col in range(0,nbr_cols):
            COM_hor[row,col] = sum(sum(data[row][col]*X))/sum(sum(data[row][col]))
            COM_ver[row,col] = sum(sum(data[row][col]*Y))/sum(sum(data[row][col]))
            if row == 0 and col == 0:
                bkg_hor = 152.4#COM_hor[row,col] 
                bkg_ver = 101.8#COM_ver[row,col] 
                        # DPC in polar coordinates. r then phi:
            COM_mag[row, col] = np.sqrt( (COM_hor[row,col]-bkg_hor)**2 + (COM_ver[row,col]-bkg_ver)**2) 
     #       COM_ver(row_ROI(1):row_idx, col_ROI(1):col_ROI(end),scan_idx)-mean(mean(COM_ver(row_ROI(1):row_idx,col_ROI(1):col_ROI(end),scan_idx))))
    #[COM_angle(row_ROI(1):row_idx, col_ROI(1):col_ROI(end),scan_idx), COM_magnitude(row_ROI(1):row_idx,col_ROI(1):col_ROI(end),scan_idx)] = cart2pol(COM_hor(row_ROI(1):row_idx,nbr:cols,scan_idx)-mean(mean(COM_hor(row_ROI(1):row_idx,col_ROI(1):col_ROI(end),scan_idx))), grej        
            COM_ang[row, col] = np.arctan( COM_hor[row,col] / COM_ver[row,col])
       #     COM_hor_tmp(col) = sum(sum(image_dat(roiy,roix).*X))/sum(sum(image_dat(roiy,roix)));
       #     COM_ver_tmp(col) = sum(sum(image_dat(roiy,roix).*Y))/sum(sum(image_dat(roiy,roix)));
       return COM_ang
