# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 18:11:16 2017

@author: Sanna
"""
import matplotlib as plt
# Using vmax and vmin
matrix = [[1, 6 ,4] ,[1,2,7]]
plt.figure()
plt.imshow(matrix)
plt.colorbar()
plt.figure()
plt.imshow(matrix, vmin=1, vmax=6)
plt.colorbar()