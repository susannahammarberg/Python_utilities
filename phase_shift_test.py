# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:10:20 2018

@author: Sanna
"""

import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-4*np.pi,4*np.pi,100)
a = np.sin(x)
b = np.sin(x+1)
plt.figure()
plt.plot(x/np.pi,a,'red')
plt.plot(x/np.pi,b,'blue')


#complex form

ac = 1./(2*1j) * ( np.exp(1j*x) - np.exp(-1j*x) )
lam = 6.3
k = 2*np.pi/lam
bc = ac * np.exp(-1j*k*0.5)
plt.figure()
plt.plot(x,ac)
plt.plot(x,bc,'green')