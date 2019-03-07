def plotdiffusion(N,dt,maxtime,D):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    # Create time scale for plotting
    timeaxis = np.linspace(0,dt*(maxtime-1),maxtime)

    # Plot all populations
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(timeaxis,D)
    ax2.set_xlabel('Time (fs)')
    ax2.set_ylabel('RMS')
    #ax.set_zticks([0,0.2,0.4,0.6,0.8,1])

    #ax.set_yticks(np.linspace(0,N-1,N))
    plt.show()
