# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:33:05 2018

@author: Sanna
"""

def plot_motorpositions(samx, samy, scan_name_string):
    import matplotlib.pyplot as plt
    plt.figure()
    plt.xlabel(' [$\mu m$]')
    plt.ylabel(' [$\mu m$]')
    plt.scatter(samx,samy)
    plt.title('Motorpositions samx samy scan%s'%scan_name_string) #'/entry%s' %scan_name_string  
    #plt.scatter(motorpositionx_AdLink,motorpositiony)
    