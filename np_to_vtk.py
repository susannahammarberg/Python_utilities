# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:58:29 2018

@author: Sanna


Function for saving np arrays in vtk format. 
Made it to be able to export to Mayavi. But now Mayavi works, plotting from python script
"""
import numpy as np

def numpy2vtk(data,filename,dx=1.0,dy=1.0,dz=1.0,x0=0.0,y0=0.0,z0=0.0):
   # http://www.vtk.org/pdf/file-formats.pdf
   f=open(filename,'w')
   nx,ny,nz=data.shape
   f.write("# vtk DataFile Version 2.0\n")
   f.write("Test data\n")
   f.write("ASCII\n")
   f.write("DATASET STRUCTURED_POINTS\n")
   f.write("DIMENSIONS %u %u %u\n"%(nz,ny,nx))
   f.write("SPACING %f %f %f\n"%(dx,dy,dz))
   f.write("ORIGIN %f %f %f\n"%(x0,y0,z0))
   f.write("POINT_DATA %u\n"%len(data.flat))
   f.write("SCALARS volume_scalars float 1\n")
   f.write("LOOKUP_TABLE default\n")
   for i in data.flat:
     f.write("%f "%i)
   f.close()
   return ()
# save vtk file     
KO = np.random.randint(1,12,size=(13,8,8))
vtk_out = numpy2vtk(KO,'KOtest.vtk')

#vtk_out = numpy2vtk(np.log10(a[623,:,140:180,170:240]),'single_braggpeak_log.vtk')
