# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 15:11:28 2019

# first part ok
# not working just cut out the essential for fitting from other code
@author: Sanna
"""

# define box and step function and plot them. Working


from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.measurements
from scipy.signal import convolve2d as conv2


def box_function(x,limit1,limit2,low,high): 
    func = high*np.ones((len(x)))
    func[np.where(x <= limit1)] = low
    func[np.where(x > limit2)] = low 
    return func

def step_function(x, limit, low, high):
    return np.where(x <= limit , 0.0, low) + np.where(x > limit, 0.0, high)


x = np.linspace(0,10,100)

stepfunction = step_function(x,2,6,7)
boxfunc = box_function(x,2,5,6,7)

plt.figure()
plt.plot(x,stepfunction)


#%%



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