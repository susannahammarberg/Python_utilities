# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 15:11:28 2019

# first part ok
# not working just cut out the essential for fitting from other code
@author: Sanna
"""

# define box and step function and plot them. Working


from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.measurements
from scipy.signal import convolve2d as conv2

def line_fun(x,k,m):
    return k*x + m

def box_function(x,limit1,limit2,low,high): 
    func = high*np.ones((len(x)))
    func[np.where(x <= limit1)] = low
    func[np.where(x > limit2)] = low 
    return func

def step_function(x, limit, low, high):
    return np.where(x <= limit , 0.0, low) + np.where(x > limit, 0.0, high)

#%%
# linear fit
# random data
x = np.linspace(0,10,100)
y = 3. * x + 2. + np.random.normal(0., 5., 100)

#fit
popt, pcov = curve_fit( line_fun, x, y)
print('a is: ', popt[0])
# fitted function is
print('and b is ', popt[1])
print('The error is in pcov')
fit_fun = line_fun(x,*popt) 

plt.figure()
plt.plot(x,y, '.')
plt.plot(x,fit_fun)

#%%##
# plot eamples of functions
x = np.linspace(0,100,100)

boxfunc = box_function(x,2,5,6,7)
stepfunc = step_function(x,2,6,7)


plt.figure()
plt.plot(x,boxfunc)
plt.plot(x,stepfunc)


#%%
#test step fun fit
x = np.linspace(0,100,100)
y = [1]*50 +[3]*50 
#fit p0 are initial guesses
popt, pcov = curve_fit( step_function, x, y , p0=[49,1,3])
# fitted function is
fit_fun = step_function(x,*popt) 
print('Estimated paramters are ', popt)

plt.figure()
plt.plot(x,y)
plt.plot(x,fit_fun,'o')
print('It can find the max and min but not the place of the junction')
#%%
#test box fit
y = [1]*50 +[3]*20 + [1]*30# + np.array((8,8,8,8,8))

# with curve fitfit
popt, pcov = curve_fit( box_function, x, y)

print('gradient based algorithm doesnt work so well with finding edges like this. try stochastic method:')

#x,limit1,limit2,low,high
res = differential_evolution(lambda p: np.sum((box_function(x, *p) - y)**2),  # quadratic cost function
                             [[45, 60], [0, 100], [0.1, 5], [0.1, 5]])  # parameter bounds (ranges))

plt.figure()
plt.plot(x,y,'.')
plt.plot(x,box_function(x,*popt))
plt.plot(x,box_function(x,*res.x))    #*res = #res.x[0],res.x[1],res.x[2],res.x[3]))
print('better')
print('but why is it one pixel wrong?')
