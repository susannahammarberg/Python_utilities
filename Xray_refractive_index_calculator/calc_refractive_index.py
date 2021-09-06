# -*- coding: utf-8 -*-
"""
Created on Wed May 02 09:59:41 2018

@author: Sanna

Refractive index calculator

About refractive index: http://gisaxs.com/index.php/Atomic_scattering_factors

f2 describes how strongly the material absorbs the radiation
while f1 describes the non-absorptive interaction (which leads to refraction). 
☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ☻☻☻☻
"""
import numpy as np
"""
Insert inputs here: 
"""



material = 'au'


file_name = 'C:/Users/Sanna/Documents/Python Scripts/Xray_refractive_index_calculator/atomic_scattering_factors/%s.nff'%material
print file_name
data = open(file_name).readlines()

#  plt.title('Scan_nbr_%d'%(first_scan_nbr+i))
  
f = [ 10075.9,	73.3671, 5.35422]

energy = f[0]*1e-3   #keV   
wavelength = (1.23984E-9)/energy    #m


r_e = 2.8179403E-15 # m classical electron radius (described how stsrongly a electron sccatters) 

rho = 19.30  # g/cm3   (/density)
MM = 196.97  #g/ mol (molar mass)
A_tal = 6.02214129e23    # unit 1/mol
n_a = rho * A_tal / MM # unit 1/cm3
n_a = n_a*1e6 # unit 1/m

delta = n_a * r_e * wavelength**2 * f[1] /( 2 * np.pi)
beta =  n_a * r_e * wavelength**2 * f[2] /( 2 * np.pi)

print 'Energy:', energy, 'keV'
print 'delta:', delta, 'beta:', beta

n = 1 - delta + 1j*beta


