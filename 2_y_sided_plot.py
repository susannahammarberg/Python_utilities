

#a_InGaP_ref = 5.8060E-10
# plot 3 values compared to a table reference 
def two_sided_plot():

 
    import numpy as np
    import matplotlib.pyplot as plt
    
    x = np.arange(50)
    data = np.random.randint(0, 8, 50)
    data2 = np.random.randint(0,33,50)
            
    fig,ax1 = plt.subplots()
    color = 'tab:blue'
    ax1.plot(x,data,marker='.', color = color,linestyle = 'None')

    plt.title('$\\beta$ (mrad)', loc='left', pad =-12)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylabel('Lattice constant $a_{GaInP}$ [$\AA$]',color=color)
    ax1.set_xlabel('$x$ [$\mathrm{\mu m}$]') 
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Ga content  [$\%$]', color='g')
    ax2.tick_params(axis='y', labelcolor='g')
    ax2.plot(x,data2,'g.')#',marker='*')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    
two_sided_plot()

