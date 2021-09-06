# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:52:33 2018

@author: Sanna


Copied from XRF_usingptypy...nanomax
just the Section where i try out different mayavi ways to plot 3d volumees (Bragg peaks)
"""
import numpy as np
import matplotlib.pyplot as plt


#------------------------------------------------------------------------------
# Make a test object. FFT3 of a cube
#------------------------------------------------------------------------------
# make a cube
N = 101       # if N is even, the first column ion the fft will be very close to 0
cube_side = 21
cube = np.zeros((N,N,N))
cube[N/2 - cube_side/2 : N/2 + cube_side/2 ,N/2 - cube_side/2:N/2 + cube_side/2,N/2 - cube_side/2:N/2 + cube_side/2 ]  = 1

plt.figure()
plt.imshow(cube[N/2])

fft_cube = np.fft.fftshift(np.fft.fftn(cube))

#plot data
data = (np.angle(( (fft_cube))))

plt.figure()
plt.imshow(data[N/2],cmap='jet')
plt.show()


from mayavi import mlab   #if you can do this instde function it is ood because it changes to QT fram

###############################################################################
# Testing a few Mayavi plotting functions
###############################################################################    


# a working slice plot
#def slice_plot():
mlab.figure()
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                            plane_orientation='x_axes',
                            slice_index=N/2,
                            colormap = 'jet'
                        )
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                            plane_orientation='y_axes',
                            slice_index=N/2,
                            colormap = 'jet'
                        )
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                            plane_orientation='z_axes',
                            slice_index=N/2,
                            colormap = 'jet'
                            )
mlab.outline()
##
##def plot3dvolume(): #  this looks very good, but almost never works 
##    x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
##    s = np.sin(x*y*z)/(x*y*z)
##    mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
##    # pipeline.scalar_filed makes data on a regular grid
##    #mlab.pipeline.volume(data[max_pos], vmin=0, vmax=0.8)
##
###def contour3d():   #iso surface
##mlab.figure()
###xmin=q3_orth[0]*1E0; xmax = q3_orth[-1]*1E0; ymin=q2_orth[0]*1E0; ymax=q2_orth[-1]*1E0; zmin=q1_orth[0]*1E0; zmax=q1_orth[-1]*1E0
##obj = mlab.contour3d( data, contours=10, opacity=0.5, transparent=False, extent=[ q1_orth[0], q1_orth[-1],q2_orth[0], q2_orth[-1] , q3_orth[0], q3_orth[-1] ])  #  , vmin=0, vmax=0.8)
##mlab.axes(ranges=[xmin, xmax, ymin, ymax, zmin, zmax])
##mlab.xlabel('$Q_z$ [$\AA^{-1}$]'); mlab.ylabel('$Q_y$ [$\AA^{-1}$]'); mlab.zlabel('$Q_z$ [$\AA^{-1}$]')
###C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\scan461_\bragg_peak_stacking\InP\
###mlab.savefig('pos_'+ str(pos) +'.jpg')
##
##
### Another way to maka an iso surface. Can also be combined with cut planes
##def iso_pipeline_plot():
##    src = mlab.pipeline.scalar_field(plot_data)  # this creates a regular space data
##    mlab.pipeline.iso_surface(src, contours=[diff_data[position].min()+0.1*diff_data[position].ptp(), ], opacity=0.5)
##    mlab.show()    
##iso_pipeline_plot()
