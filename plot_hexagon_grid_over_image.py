# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:47:05 2020

@author: Sanna
"""
import numpy as np
import matplotlib.pyplot as plt

R=2
N=20
a = np.random.rand(N-2,N)
center = N/2


            
            
plt.figure()
plt.imshow(a,cmap='hot')
plt.plot(np.arange(N))
plt.plot(-np.arange(N)+N-1)
plt.plot(5*np.ones(N))
plt.plot(np.arange(N),9*np.ones(N-2).T)
