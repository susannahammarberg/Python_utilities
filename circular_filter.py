# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:38:03 2018

@author: Sanna ( but also stolen from link below)
"""
import numpy as np

#test_circular probe function taken from https://mail.scipy.org/pipermail/numpy-discussion/2011-January/054470.html
# used for dark field filter and also possible for initial probe definition
# Not very round...
# exempel = circular_filter(50,50,4,0)     to make a single circle and
# exempel = circular_filter(50,50,4,0)     to make a circular filter (dark field filter)
def circular_filter(ySize, xSize, outer_radius, inner_radius):
    inner_circle = np.zeros((ySize, xSize)).astype('uint8')
    outer_circle = np.zeros((ySize, xSize)).astype('uint8')
    cx, cy = int(xSize/2), int(ySize/2) # The center of circle
    
    #construct outer circle
    y_outer, x_outer = np.ogrid[-outer_radius: outer_radius, -outer_radius: outer_radius]
    index_outer = x_outer**2 + y_outer**2 <= outer_radius**2
    
    outer_circle[cy-outer_radius:cy+outer_radius, cx-outer_radius:cx+outer_radius][index_outer] = 1

#    #construct inner circle
    y_inner, x_inner = np.ogrid[-inner_radius: inner_radius, -inner_radius: inner_radius]
    index_inner = x_inner**2 + y_inner**2 <= inner_radius**2
    inner_circle[cy-inner_radius:cy + inner_radius, cx- inner_radius:cx+ inner_radius][index_inner] = 1
    
    return outer_circle -inner_circle