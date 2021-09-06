# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:21:14 2017

@author: Sanna
"""
#from IPython import get_ipython
#get_ipython().magic('reset -sf')
import h5py
import numpy as np
import matplotlib.pyplot as plt


path = r'C:\Users\Sanna\Documents\Beamtime\Diamond_I13_20180925\probe'
file = r'\191646_20180928-152025.hdf'

#data_key = 

print('will try to open file:' , path+file)
with h5py.File(path + file) as fp:
    print('the 1:st key in the file are: ' , fp.keys())
    a = (fp.get('entry_1/process_1/output_1/probe')[()])
    
    
probe = np.squeeze(a)

# for np arrays in np format
np.save(r'C:\Users\Sanna\Documents\Beamtime\Diamond_I13_20180925\probe\probe_ndarray', probe)


#open this file
loaded_array = np.load(r'C:\Users\Sanna\Documents\Beamtime\Diamond_I13_20180925\probe\probe_ndarray.npy') #C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\ptycho_192_222\COM2d\scan222_COM_ang.npy')

    
plt.figure()
plt.subplot(121)
plt.suptitle('probe: amplitude and phase', fontsize=20)
plt.imshow(((abs(probe))), cmap= 'RdBu_r', interpolation='none') 
plt.colorbar()
plt.subplot(122)
plt.imshow(np.angle(probe), cmap= 'RdBu_r', interpolation='none') 
plt.colorbar()

print( type(probe))
    #data = np.array(fp.get('entry%d'%scannr + '/measurement/gonphi').value))

loaded_array = np.load(r'C:\Users\Sanna\Documents\temp\sample_mask.png')

  