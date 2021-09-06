# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:17:52 2019

@author: Sanna
"""

import numpy as np

a = 42
b = 31

print 'a', a,  id(a)
print 'b', b, id(b), '\n'

a=b

print 'a', a,  id(a)
print 'b', b, id(b), '\n'

b=12

print 'a', a, id(a)
print 'b', b, id(b), '\n'

b_copy = np.copy(b)

print 'b', b, id(b)
print 'b_copy', b_copy, id(b_copy), '\n'

b = 677

print 'b', b, id(b)
print 'b_copy', b_copy, id(b_copy), '\n'

print ' So neither an assignemnet or an np copy points ', '\n'




# the opposite to append is remove
#listname.remove() 

# stacking (what is that??)
values = []
values.append(8*4)
values.append('apa' *3)
values.append(65)
values.append(999)

# removes the last values
values.pop()

gd = []
gd.append(55)
gd.append(484)
gd.append(2763)
print '\n', gd
for i in range(3):
    print values[i], gd[i]
# clear the list
#values.clear()

