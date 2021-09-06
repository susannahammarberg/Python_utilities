# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:51:10 2018

@author: Sanna

Load a bunch of COM-analysis images from the STXM images of a ptycho set
(One image for each theta in the ptycho set, with nbr_pixels = nbr_rowsxnbr_cols
on the 2d scanning grid in the ptycho set)


Dataset 192 etc

# find center of mass in image    
import scipy.ndimage.measurements
"""

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.measurements
from scipy.signal import convolve2d as conv2
scans = range(192, 200+1)+range(205, 222+1)


#import pdb (or ipdb)
#pdb.set_trace() 
    
   
#def step_function(x, thresh_value, low, high):
#    fun = np.zeros(len(x))
#    for ii in x:
#        if ii<thresh_value:
#            fun[ii] = high
#        else:
#            fun[ii] = low
#    return fun
              
def step_function(x,a,b,c): 
    return a * (np.sign(x-b) - c) # Heaviside fitting function

def heaviside(x, limit, low, high):
    return np.where(x <= limit, 0.0, low) + np.where(x > limit, 0.0, high)


hor_edge = []
# save the vertical center of NW for each scan in a list
vert_center = []
for ii in range(0,len(scans)):
    
    loaded_array = np.load('C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d_pilatus_orig\scan%d_COM_ang.npy'%scans[ii]) #put in ii
    # define background
    bkg = np.median(loaded_array) #198.2      # find most common pixel value
    

    # remove the background
    # take the absolute square
    # then do COM analysis
    row_com, col_com = map(int, scipy.ndimage.measurements.center_of_mass(abs(loaded_array-bkg)))
    vert_center.append(row_com)
    
    
    # the row_col is good, that I can use but the col_com does not give me the edge
    
    plt.figure()
    plt.subplot(211)
    plt.imshow(loaded_array)
    plt.title('Bkg is set to median:%f'%bkg)
    plt.colorbar()
    plt.subplot(212)
    plt.imshow(abs(loaded_array-bkg))
    plt.title('With subtracted bkg')
    plt.colorbar()
    plt.tight_layout()
    plt.subplots_adjust(left=-0.75, bottom=None, right=None, top=None, wspace=None, hspace=None)    
    plt.suptitle('row_com:%d and col_com%d:'%(row_com,col_com))

    # to find the edge of the NW:
    col_line = np.sum(abs(loaded_array-bkg),axis=0)
    # method 1
    # find the point with the highest derivative (one-liner!)
    # this is not good the derivative is highest just after the peak
    edge_col1 = np.argmax(col_line[:-1] - col_line[1:])
    plt.figure()
    plt.plot(col_line)
    #make a line where you found the edge of the column
    plt.plot(edge_col1, col_line[edge_col1],'yo')
    plt.title('Edge_col1:%d:'%(edge_col1))
    
    # method 2:
    # find where the max-min/2 is on the line
    halfMax = (max(col_line) - min(col_line)) / 2 
    # check the first value which is below the half max
    edge_col2 = np.where(col_line < halfMax)[0][0]
    plt.figure()
    plt.plot(col_line,'b.')
    plt.plot(col_line,'b-')
    #make a line where you found the edge of the column
    plt.plot(edge_col2, col_line[edge_col2],'mD')
    plt.title('Edge identified at col: %d:'%(edge_col2))
    
    # add the column of the right edge for all scans
    hor_edge.append(edge_col2)
    
    # Method 3
    # TODO it is not working, its not fitting! it just sets the edge to 12 (for any of the step functions )
    # fit a step function to the lineplot (sum over all rows)    
    xx = np.arange(len(col_line))
    popt, pcov = curve_fit( heaviside, xx, col_line, [12,min(col_line), max(col_line)])
    # fitted function is
    fit_fun = heaviside(xx,*popt)  #what does star mean?
    # find where the max-min/2 is on the line
    halfMax3 = (max(fit_fun) - min(fit_fun)) / 2  + min(fit_fun)
    # check the first value which is below the half max
    edge_col3 = np.where(fit_fun < halfMax3)[0][0]
    #np.disp(popt)
    plt.figure()
    plt.plot(col_line,'b.')
    plt.plot(col_line,'b-')
    plt.plot(xx,fit_fun)   
    plt.plot(edge_col3, col_line[edge_col3], 'mD')
    #method 3: fit a step function to the data, then do method 2
    #plt.savefig('C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d\summed_rows_lineplots\\vers_3_scan%d'%((scans[ii])), bbox_inches='tight')

# save the vertical center of NW in a list
# use the lowest or highest lying NW as reference, does not matter
vertical_shift_vector = np.array(vert_center) -min(vert_center)    
# corresponding to scan
scans[np.argmax(hor_edge)] 
#np.save('vertical_shift_vector', vertical_shift_vector)        

# find the NW vertically most to the left
#max_vert_edge = np.argmax(vert_edge)   
ref_edge = min(hor_edge)   
# corresponding to scan_nbr
scans[np.argmax(hor_edge)] 
# the NW with edge furthest to the left, ref_edge, is the reference
#the other ones should be -   and the nbr of steps from the reference
horizontal_shift_vector = ( hor_edge - ref_edge)
#np.save('horizontal_shift_vector', horizontal_shift_vector)

# test if the shifting vector is correct
interval=1
for ii in range(0,len(scans), interval):
    loaded_array = np.load('C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d_pilatus_orig\scan%d_COM_ang.npy'%scans[ii]) #put in ii

    hor_shift_array = np.roll(loaded_array, -horizontal_shift_vector[ii],axis=1)
    
#    plt.figure()

#    plt.imshow(hor_shift_array)
#    plt.title('Horizontally shifted')
#    plt.colorbar()
#    plt.tight_layout()
    
#    plt.figure()
#    plt.imshow(np.roll(loaded_array, vertical_shift_vector[ii], axis=0))
#    plt.title('vert shifted')
#    plt.colorbar()
#    plt.tight_layout()
    
    
    plt.figure()
    plt.subplot(211)
    plt.imshow(loaded_array,cmap='cool')
    plt.title('original')
    plt.colorbar()
    plt.subplot(212)
    plt.imshow(np.roll(hor_shift_array, -vertical_shift_vector[ii], axis=0),cmap='gray')
    plt.title('shifted')
    plt.colorbar()
    plt.tight_layout()
    plt.subplots_adjust(left=-0.75, bottom=None, right=None, top=None, wspace=None, hspace=None)    
    plt.suptitle('Horizontally and vertically aligned COM maps')
   # plt.savefig('C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d_pilatus_aligned\\scan%d'%((scans[ii])), bbox_inches='tight')















# try to find the right NW edge using convolutions with filters on the image
#  mark horizontal edges
f1 = np.array([[0,1],
                [0,-1]])

# find edge with filter
# filter to mark vertical edges
f3 = np.array([[1,-1],
                [0,0]])


# this sort of works (find NW horizontally )
conv_array = conv2((loaded_array-bkg), f1)
# find NW verticall edge
conv_array_vert = conv2(abs(loaded_array-bkg),f3)

plt.figure()
plt.imshow(conv_array)
plt.figure()
plt.imshow(conv_array_vert)