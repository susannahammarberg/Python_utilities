# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 14:02:38 2018

@author: Sanna
"""

import h5py
import numpy as np
import matplotlib.pyplot as plt
data = 'D:/exp20170628_Wallentin_nanomax/exp20170628_Wallentin/JWX33_NW2/scan_0282_merlin_0006.hdf5'

hf =  h5py.File(data, 'r')
lista= []
    
title = lista.append(hf.get('entry_0000/title'))
data = np.array(hf.get('entry_0000/measurement/Merlin/data'))#[0]

plt.figure()
plt.imshow(np.log(data[20]))

#    psize = np.array(hf.get('content/probe/S00G00/_psize'))[0]
#    energy = np.array(hf.get('content/probe/S00G00/_energy'))
#    origin = np.array(hf.get('content/probe/S00G00/_origin'))