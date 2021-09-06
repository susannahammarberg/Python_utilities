# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:54:37 2018

@author: Sanna
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft as fft

T = 2                      # time distance between pulses
Fs = 1000                  # sampling frequency, used for discretizing the system
t = np.arange(-6, 6, 1./Fs) # time range to consider
comb = np.zeros_like(t)
comb[::int(Fs*T)] = T     # Comb becomes T every T*Fs samples

plt.figure()
plt.plot(t, comb)


plt.figure()
plt.plot(fft.fft(comb))