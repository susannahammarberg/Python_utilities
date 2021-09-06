# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:09:18 2019

Plotting lattice vectors and the corresponding reciprocal lattice vector
using plt.quiver!

@author: Sanna

help:
https://stackoverflow.com/questions/43723224/how-does-matplotlibs-quiver-work
"""
import matplotlib.pyplot as plt
import numpy as np

a1 = [0,1]
a2 = [0,2]

#b1 = 2*np.pi/a1    #magnitude
#b1 = 

origo = [0,0]

plt.figure()
plt.subplot(121)
plt.quiver([0,1],[0],a1,a2,color=['r','g'], scale =100, label='jj')
plt.subplot(122)
plt.quiver([0],[0],a1,a2,color=['r','g'], scale = 10, label='jj')
#plt.legend(['a1'])

