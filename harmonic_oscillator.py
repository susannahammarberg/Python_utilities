# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:29:18 2020

@author: Sanna
"""


import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use( 'Qt5agg' )

k = 1
x = np.linspace(-1,1,20)
n = np.linspace(1,5)
m = 15

omega = np.sqrt(k/m)


U = 0.5*k*x**2          # the curvatrure will depend on k, not m.
U = 0.5*m*omega**2*x**2  

E =  omega*(n+0.5)

plt.figure()
plt.plot(x,U)
#plt.plot(E[0]*len(x))
plt.show()
