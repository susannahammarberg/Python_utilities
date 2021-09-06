
# TODO: remove single photon count, if the COM is calculated for very small values like pixels with 1 photon counts, 
#then the result will be missleading. Set a threshold that keeps the resulting pixel on a mean value, like if sum(sum(sum(diffPattern)))< threshold. sum(sum(sum()))==bkg_value

# input here is 4d matrix with [nbr_diffpatterns][nbr_rotations][nbr_pixels_x][nbr_pixels_y]
def COM_voxels(data,nbr_cols,nbr_rows):
    # define a vector with length of the length of roi on the detector
    roix = np.linspace(1, shape, shape )
    ## define a vector with length of the height of roi on the detector
    roiy = np.linspace(1,shape, shape)
    roiz = np.linspace(1,nbr_rot,nbr_rot)    
    # meshgrids for center of mass calculations
    Z, X, Y = np.meshgrid(roix,roiz,roiy)
    
    COM_hor = np.zeros((nbr_rows,nbr_cols))
    COM_ver = np.zeros((nbr_rows,nbr_cols))
    COM_rot = np.zeros((nbr_rows,nbr_cols))
    COM_mag = np.zeros((nbr_rows,nbr_cols))
    COM_ang = np.zeros((nbr_rows,nbr_cols))
    index = 0
    for row in range(0,nbr_rows):
        for col in range(0,nbr_cols):
            threshold = 3000   #dont know how to set this threshold. but should be when the data it is summung is just some single photon ocunts on each image
            if sum(sum(sum(data[index]))) > threshold:
                COM_hor[row,col] = sum(sum(sum(data[index]*X)))/sum(sum(sum(data[index])))
                COM_ver[row,col] = sum(sum(sum(data[index,:]*Y)))/sum(sum(sum(data[index])))
                COM_rot[row,col] = sum(sum(sum(data[index,:]*Z)))/sum(sum(sum(data[index])))
            else:
                COM_hor[row,col] = 13.616534672254996      # == np.mean(COM_hor) without the if-sats
                COM_ver[row,col] = 64.117565383940558
                COM_rot[row,col] = 61.397211314625821             
                
            if row == 0 and col == 0:
                bkg_hor = 152.4#65.1#152#COM_hor[row,col] #152.4#
                bkg_ver = 101.8#64.6#101#COM_ver[row,col]  #101.8#
                bkg_rot = 0
            # DPC in polar coordinates. r then phi: . although does not make much sence
            COM_mag[row, col] = np.sqrt( (COM_hor[row,col]-bkg_hor)**2 + (COM_ver[row,col]-bkg_ver)**2 + (COM_rot[row,col]-bkg_rot)**2) 
            COM_ang[row, col] = np.arctan( (COM_hor[row,col]) / (COM_ver[row,col]))
    
            index += 1
    return COM_hor, COM_ver, COM_rot, COM_mag, COM_ang

COM_hor,COM_ver,COM_rot,COM_mag,not_corr_ang = COM_voxels(diff_data,nbr_cols,nbr_rows)

def plot_COM():
    plt.figure()
    plt.suptitle('Center of masss analysis')
    plt.subplot(411)
    plt.imshow(COM_hor, cmap='jet',interpolation='none',extent=extent_motorpos) 
    plt.title('COM hor')
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    plt.subplot(412)
    plt.imshow(COM_ver, cmap='jet',interpolation='none',extent=extent_motorpos)
    plt.title('COM ver')
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    plt.subplot(413)
    plt.imshow(COM_rot, cmap='jet',interpolation='none',extent=extent_motorpos) 
    plt.title('COM rot')
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    plt.subplot(414)
    plt.title('Bright field (sum of all rotations)')
    plt.imshow(sum(brightfield), cmap='jet', interpolation='none',extent=extent_motorpos)
    plt.xlabel('x [$\mu m$]') 
    plt.ylabel('y [$\mu m$]')
    plt.colorbar()
    #plt.savefig("C:\Users\Sanna\Documents\Beamtime\NanoMAX062017\Analysis_ptypy\scan461_\COM_3d") 
    
plot_COM()
