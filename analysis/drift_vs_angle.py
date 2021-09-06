# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:44:15 2019

@author: Sanna
"""
import matplotlib.pyplot as plt
import numpy as np
sample = 'JWX29A_NW1'; scans = [458,459,460,461,462,463,464,465,466,467,468,469,470,471,518,473,474,475,476,477,478,479,480,481,482,483,484,485,486,519,488, 496,497,498, 499, 500, 501, 502, 503, 504, 505, 506,507, 508, 509, 510, 511, 512, 513, 514, 515]

# 458 theta = 13.01 459 13.08        515: theta = 12.10
angle = np.linspace(13.10, 12.10, 51)   #stepsize 0.02

# shifting list
vertical_shift =  [-1,-1,0,0,0,  0,0,2,1,0,  1,1,1,0,-1,  -1,-1,-1,-1,0,  -1,-1,0,0,1,  1,-1,0,1,0,   2,0,0,1,1,  1,0,0,1,1,  1,2,2,2,4,  3,3,3,3,3,   3]
horizontal_shift =  [3,2,0,1,2,  3,4,3,4,5,  5,6,6,5,6,  5,4,7,8,8,  8,8,10,11,12,  11,12,12,11,12,  12,11,12,13,13,  14,15,14,14,14,  13,15,16,15,14,  17,19,18,18,17,   17]

#if __name__ == 'main':
plt.figure()
plt.plot(angle, horizontal_shift, 'g-', label='Horizontal shift')
plt.plot(angle, vertical_shift, 'b-', label = 'Vertical shift') 
plt.xlabel('Theta angle [$\deg$]')
plt.ylabel('Compensation for drift in pixels')
plt.legend()

# size of these pixels are the stepsizes of the measuring grid , rigth. so 40 or 30 nm. 

plt.figure()
plt.plot(angle, [40 * index for index in horizontal_shift], 'g-', label='Horizontal shift')
plt.plot(angle, [30* index for index in vertical_shift], 'b-', label = 'Vertical shift') 
plt.xlabel('Theta angle [$\deg$]')
plt.ylabel('Compensation for drift [nm]')
plt.legend()