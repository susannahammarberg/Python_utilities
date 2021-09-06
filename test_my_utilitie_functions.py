# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:36:59 2018

@author: Sanna
"""


import sys   #to collect system path ( to collect function from another directory)
sys.path.insert(0, 'C:/Users/Sanna/Documents/python_utilities/analysis') #can I collect all functions in this folder?
 
from plot_motorpositions import plot_motorpositions


yes = plot_motorpositions([ 1, 2, 3, 1,1,1],[ 2, 2, 5, 2,2,5],'testar bara')