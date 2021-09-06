# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 15:11:28 2019

# first part ok
# not working just cut out the essential for fitting from other code
@author: Sanna
"""

# make linear fit


from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def line_fun(x,k,m):
    return k*x + m

# random data
x = np.linspace(0,10,100)
y = 3. * x + 2. + np.random.normal(0., 10., 100)

#fit
popt, pcov = curve_fit( line_fun, x, y)
# fitted function is
fit_fun = line_fun(x,*popt) 

plt.figure()
plt.plot(x,y, '.')
plt.plot(x,fit_fun)