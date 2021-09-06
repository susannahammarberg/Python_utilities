# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:39:15 2019

@author: Sanna



# where do i import the libraries I depend on?


"""

import numpy as np


# Find the indices of a np array
#Var ska jag importera np??    
def max_indices_np(np_array):
   
    # this gives you the index of the flattened array
    # but thats all you ever need
    return np.argmax(np_array)    

def set_max_zero_array(np_array):
    # save shape of array
    shape = np_array.shape
    # find max indic (of flattened array)
    max_pos = np.argmax(np_array)
    # flatten the array
    flat_array = np_array.flatten()
    # remove that largest element
    flat_array[max_pos] = 0     
    # reshape the array to original shape 
    np_array = flat_array.reshape(shape)  
    # return the array
    return np_array

# simpler way?
def mask_matrix(a): 

    # set the largest element in the matrix to 0
    a[ a== a.max()] = 0
    return a 

    # thats all

# calculate backwords from theta to d
def theta2a(theta_i,energy=9.49,crystal_key='cubic' ):
    wavelength = 1.23984E-9 / energy
    q_abs_i = 4 * np.pi * np.sin(np.deg2rad(theta_i)) / wavelength
    d_calc = 2*np.pi/q_abs_i
    a_calc = d_calc * np.sqrt(3)  
    return (d_calc,a_calc,q_abs_i)


def test_or_something():
    
    theta2a(11.9)
    theta2a(10.99)
    
    # homogenous wires:
    #dx_InP_homo = 
    # how much the detector is rotatad (towards sample)
    det_rot = 11
    # pixels away from center of detec tor
    dx_InP = -66       #center of roi for INP analysis is -66
    dx_GaInP = 74      #center of roi for GaInP analysis is 74
    
    det2sample_opt =  1.065
     # distance from detector to optical axis
    det2opt = 0.43
    # the cener att the detector is at angle: (2theta/2)
    theta_middle = np.rad2deg(np.arctan(det2opt  /det2sample_opt))/2
    # the InP peak is dx_InP pixels away, thus at the angle:
    theta_InP = np.rad2deg(np.arctan((det2opt  +(np.cos(np.deg2rad(det_rot))*(dx_InP*55E-6))) /det2sample_opt)) / 2 
    theta_GaInP = np.rad2deg(np.arctan((det2opt  +(np.cos(np.deg2rad(det_rot))*(dx_GaInP*55E-6))) /det2sample_opt)) / 2 
    print theta_InP
    print theta_GaInP
    d_InP,a_InP,q_abs_InP = theta2a(theta_InP)
    d_GaInP,a_GaInP,q_abs_GaInP = theta2a(theta_GaInP )


def calc_lattice_mismatch(a1,a2):
    return ((a1-a2)/a2)


# calculate backwords from |q| to d
def qabs2latticeplaned(q_abs_i):
    d_calc = 2*np.pi/q_abs_i
    return d_calc

# TODO fix qubix or WZ ZB..
def absq2a(absq,crystal_key='cubic' ):
    d_calc = 2*np.pi/absq
    # lattice constant for a cubic crystal
    a_calc = d_calc * np.sqrt(3)  
    return a_calc

def absq2d(absq):
    return 2*np.pi/absq

def Vigards_law(x_ga):
    a_inp = 5.8687 #[Å]
    a_gap =  	5.4505 #A [ioffe])
    a_gainp = (1-x_ga)*a_inp + x_ga*a_gap
    #a_gainp = a_inp - x_ga*(a_inp-a_gap)
    return a_gainp    
    
def Vigards_law_back(a_GaInP, a_InP=5.8687, a_GaP=5.4505):
    xGa= (a_GaInP-a_InP)/(-a_InP+a_GaP)
    return xGa

def calc_dq3(dtheta=0.02,wavelength=1E-10,theta_rad=1):
    # AB calculations dq3= np.deg2rad(self.psize[0]) * 4 * np.pi / self.lam * self.sintheta 
    dq3= np.deg2rad(dtheta) * 4 * np.pi / wavelength* np.sin(theta_rad) 
    return dq3
    
def sintheta(self):
   return np.sin(np.deg2rad(self.theta_bragg))
#    return dq

if __name__== '__main__':
    
    # import here?
    
    # test some functions
    
    arr = np.arange(6).reshape(2,3)
    print 'Array:' ; print  arr
    print '\n'
    # returns the max position of the flattened array
    max_value = max_indices_np(arr)
    
    # check, and set the max value to 0 in a np array
    arr = set_max_zero_array(arr)    
    print arr; print '\n'
    
    a = np.random.randn(3,2)
    print a 
    a = mask_matrix(a)
    print a  
    
    calc_lattice_mismatch(a_InP,a_GaInP)#,a_GaInP)
    
    

