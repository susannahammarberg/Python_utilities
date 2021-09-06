# -*- coding: utf-8 -*-

from numpy import np

a = np.random.randn(4,5)

# set the largest element in the matrix to 0
a[ a== a.max()] = 0

# thats all
