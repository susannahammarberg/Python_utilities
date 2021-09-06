# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:25:00 2018

@author: Sanna
"""

import scipy
import numpy as np 

scipy.io.savemat('exampel_probe.mat',{"probe":probe})  

# u need to store as a dictionary with a name


# for np arrays in np format
np.save('filename', nparray)

#open this file
loaded_array = np.load('C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d\scan222_COM_ang.npy')
