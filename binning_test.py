# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:49:53 2018

@author: Sanna
"""

import ptypy.utils
import numpy as np


a = np.arange(16).reshape(4,4)

# for 2x2 binning, b will be half the size of a 
b = np.zeros((a.shape))



b=ptypy.utils.rebin(a,2,2)
b2=ptypy.utils.rebin_2d(a,2)

#  sum all pairs of pixels in all the rows




# the start summing in every paris of columns 




#Code in ptypy:
#def rebin(a, *args,**kwargs):
#    """
#    Rebin ndarray data into a smaller ndarray of the same rank whose dimensions
#    are factors of the original dimensions.
#
#    .. note::
#        eg. An array with 6 columns and 4 rows
#        can be reduced to have 6,3,2 or 1 columns and 4,2 or 1 rows.
#
#    Parameters
#    ----------
#    a : ndarray
#        Input array.
#
#    axis : int, Default=-1, optional
#        The laplacian is computed along the provided axis or list of axes,
#        or all axes if None
#
#    Returns
#    -------
#    out : ndarray
#        Rebined array.
#
#    Examples
#    --------
#    >>> import ptypy
#    >>> import numpy as np
#    >>> a=np.random.rand(6,4)
#    >>> b=ptypy.utils.rebin(a,3,2)
#    a.reshape(args[0],factor[0],args[1],factor[1],).sum(1).sum(2)*( 1./factor[0]/factor[1])
#    >>> a2=np.random.rand(6)
#    >>> b2=ptypy.utils.rebin(a2,2)
#    a.reshape(args[0],factor[0],).sum(1)*( 1./factor[0])
#    """
#    shape = a.shape
#    lenShape = a.ndim
#    factor = np.asarray(shape)/np.asarray(args)
#    evList = ['a.reshape('] + \
#             ['args[%d],factor[%d],'%(i,i) for i in range(lenShape)] + \
#             [')'] + ['.sum(%d)'%(i+1) for i in range(lenShape)] + \
#             ['*( 1.'] + ['/factor[%d]'%i for i in range(lenShape)] + [')']
#    if kwargs.get('verbose',False):
#        print ''.join(evList)
#    return eval(''.join(evList))

    