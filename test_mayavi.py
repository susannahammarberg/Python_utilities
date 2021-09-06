# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 10:24:47 2018

@author: stolen from https://pyscience.wordpress.com/2014/09/06/numpy-to-vtk-converting-your-numpy-arrays-to-vtk-arrays-and-files/

"""
import numpy as np
from vtk.util import numpy_support
import vtk
help(numpy_support.numpy_to_vtk)


NumPy_data = np.random.random((10,10,10))

# convert  (u need to reshape from 3d to a 1df representation of the data)
NumPy_data_shape = NumPy_data.shape
VTK_data = numpy_support.numpy_to_vtk(num_array=NumPy_data.ravel(), deep=True, array_type=vtk.VTK_FLOAT)





file=open("guru.vtk", "a+")

