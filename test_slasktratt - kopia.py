# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:25:16 2017

@author: Sanna
"""



#from scipy.sparse import csc_matrix
#import mayavi
#import matplotlib.pyplot as plt
from scipy import sparse
import numpy as np
from sys import getsizeof   #se hur mkt minne variabler tar upp  
#from mayavi import mlab
import h5py

#scan = h5py.File( 'D:/PetraIII_run65_20170917/LCBP18_IJ_ptycho1/eiger/LCBP18_IJ_ptycho1_00001_data_000001.h5') # read-only
data_pil = scan.get('/entry_0000/measurement/Pilatus/data' )
#LCBP18_IJ_ptycho1_metadata
#textfile = np.load('D:/PetraIII_run65_20170917/LCBP18_IJ_ptycho1/LCBP18_IJ_ptycho1_metadata.txt')
#'D:/PetraIII_run65_20170917/LCBP18_IJ_ptycho1/LCBP18_IJ_ptycho1_metadata.txt'
n = np.loadtxt("D:/PetraIII_run65_20170917/LCBP18_IJ_ptycho1/LCBP18_IJ_ptycho1_metadata.txt")#,dtype='int'
#data = np.load('C:\Users\Sanna\Desktop\NanoMAX062017\merlin_mask(1).npy')
#
##
#x, y, z, value = np.random.random((4, 40))
#mlab.points3d(x, y, z, value)
#
#test = np.zeros((4,4))
#test[ 0,0 ] =1
#test[ 1,3 ] =1
#print getsizeof(test)
#
#sparse_matrix= sparse.csc_matrix((4,4))
#print getsizeof(sparse_matrix)
#
#sparse_matrix[:,:] = test
#print getsizeof(sparse_matrix)
#
#B =sparse.lil_matrix(test)
#
#A = sparse.coo_matrix(test,shape=(4,4))
#print getsizeof(A)
#
#list_A = [ A, A]
#
#print getsizeof(list_A)
#
#tuple_A = ((A,A) , (A,A))     #tuples takes less space than lists
#
#
##gather data with tuple_A[0][0]
#i= tuple_A[0][0]
#print getsizeof(tuple_A)
#
#
#
#
## from sparse to array
#array = A.toarray()
#
#print array
#
#li = [ [], [], [], [], [] ]            #make lists inside a list li
#
#for i in range(0,3):
#    li[0].append((A))   # put A in the first
#    
#    
#print li
#    
#x = [ [[5,7],[6,6]] , [[6,6],[7,8]] , [[7,2],[2,5]] ]
#print x[1][1][1]
## list for all 4  positions in one row
#pos  = [  A , A , A ,A ]
#print pos
#
## Du vill kopo'iera den listan så många gånger som du har rader, alltså säg 3. 
## en list där varje list är en list med 
## All 4 position for all 3 rows:
#rows = [ [A,A,A, A], [A,A,A,A] , [A,A,A,A]  ]
## all 2 rotaions for all 3 rows and all 4 positions
#rot = [    [ [A,A,A, A], [A,A,A,A] , [A,A,A,A]  ]      ,      [ [A,A,A, A], [A,A,A,A] , [A,A,A,A]  ]        ]
#
#N=8
## spare to list and onwards to array that works
#M=[A for i in xrange(N)]
#H=[M[0].toarray()]
#J=[m.toarray() for m in M]
