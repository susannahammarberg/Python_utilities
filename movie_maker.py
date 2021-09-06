# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:02:15 2017

@author: Sanna
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def movie_maker(data, name):
    #figure for animation
    fig = plt.figure()
    #make image movie
    # Initialize vector for animation data
    ims = []  
    for i in range(0,len(data)):
        im = plt.imshow((data[i]), animated=True, cmap = 'jet', interpolation = 'none', origin='lower')
                       #y  x
        txt = plt.text(30,30,'i = : ' + str(i) , color = 'red', fontsize=11)  
        ims.append([im,txt])
        
    ani = animation.ArtistAnimation(fig, ims, interval=5000, blit=True,repeat_delay=0)  
    plt.axis('off')
    plt.show()
    # save animation:
    ani.save(name +'.mp4', writer="mencoder")   
