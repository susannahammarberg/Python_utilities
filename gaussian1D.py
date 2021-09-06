# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:24:12 2018

@author: Sanna
"""

def fit_gauss1d(x,y):
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    import numpy as np

    n = len(x)                      
    mean = sum(x*y)/sum(y)              
    sigma = np.sqrt(sum(y*(x-mean)**2)*1. /n)
    def gaus(x,a,x0,sigma):
        return a*np.exp(-(x-x0)**2/(2*sigma**2))
    
    popt,pcov = curve_fit(gaus,x,y,p0=[max(y),mean,sigma])
    print 'popt should be = a, x0, sigma'
    print popt
    plt.figure()
    plt.plot(x,y,'b+:',label='data')
    plt.plot(x,gaus(x,*popt),'ro:',label='fit')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
from scipy import asarray as ar
    
x = ar(range(10))
y = ar([0,1,2,3,4,5,4,3,2,1])
fit_gauss1d(x,y)