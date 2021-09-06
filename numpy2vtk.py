# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:55:50 2018

@author: zhe ren
"""

def numpy2vtk(a,filename,dx=1.0,dy=1.0,dz=1.0,x0=0.0,y0=0.0,z0=0.0):
   # http://www.vtk.org/pdf/file-formats.pdf
   f=open(filename,'w')
   nx,ny,nz=a.shape
   f.write("# vtk DataFile Version 2.0\n")
   f.write("Test data\n")
   f.write("ASCII\n")
   f.write("DATASET STRUCTURED_POINTS\n")
   f.write("DIMENSIONS %u %u %u\n"%(nz,ny,nx))
   f.write("SPACING %f %f %f\n"%(dx,dy,dz))
   f.write("ORIGIN %f %f %f\n"%(x0,y0,z0))
   f.write("POINT_DATA %u\n"%len(a.flat))
   f.write("SCALARS volume_scalars float 1\n")
   f.write("LOOKUP_TABLE default\n")
   for i in a.flat:
     f.write("%f "%i)
   f.close()
   print 'function was called'
   return ()