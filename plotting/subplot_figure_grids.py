# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:05:49 2020

@author: Sanna
"""

import matplotlib.pyplot as plt
import numpy as np

def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


im1 = np.ones((9,9))
im2 = 2*np.ones((9,4))
im3 = 3*np.ones((15,4))

fig = plt.figure()
ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((2, 3), (1, 0), colspan=1)
ax3 = plt.subplot2grid((2, 3), (1, 1), colspan=1)
ax4 = plt.subplot2grid((2, 3), (1, 2))
#ax5 = plt.subplot2grid((3, 3), (2, 1))

ax1 = plt.imshow(im1)
ax2 = plt.imshow(im2)
ax3 = plt.imshow(im3)
plt.show()


fig = plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

#annotate_axes(fig)

plt.show()
