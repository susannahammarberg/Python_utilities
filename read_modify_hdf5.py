# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:21:14 2017

@author: Sanna
"""
#from IPython import get_ipython
#get_ipython().magic('reset -sf')
import h5py
import numpy as np

new_data = np.ones((1,128,128),dtype=np.complex)

f1 = h5py.File('test_hdf5_file.ptyr', 'r+')     # open the file
data = f1['/content/probe/S00G00/data'].value     # load the data
#probe = np.array(f1.get('content/probe/S00G00/data'))[0]
#probe = np.array(f1.get('content/probe/S00G00/data'))[0]
data[...] = new_data                      # assign new values to data
f1.close()                          # close the file
#
#
##To confirm the changes were properly made and saved:
#
f1 = h5py.File('test_hdf5_file.ptyr', 'r')
np.allclose(f1['/content/probe/S00G00/data'].value, new_data)
##True
OLLE = np.array(f1.get('content/probe/S00G00/data'))[0]