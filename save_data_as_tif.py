# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:54:24 2020

@author: Sanna
"""

import numpy as np
import PIL.Image as im

data = np.random.randint(0, 255, (10,10))#.astype(np.uint8)
im = im.fromarray(data)
im.save('test.tif')