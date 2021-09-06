# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:41:58 2018

@author: Sanna

Calculate the overlap for a ptycho measurement

"""
import numpy as np
import matplotlib.pyplot as plt
# probe diameter
diam = 5
r = diam/2.  
# stepsize: distance between circles # distance between centers?
d = 1* diam/ 4.
# en med en fjärdedel är man säker på att få 60 %
   

Atot = np.pi*r**2

A_overlap = (2*r**2) * np.arccos(d/(2.*r)) - (d/2.)*np.sqrt((4*r**2) - d**2)
np.disp(A_overlap)
overlap = 100*A_overlap/Atot
np.disp( '\n % ' +'Overlap: %f'  %overlap)

