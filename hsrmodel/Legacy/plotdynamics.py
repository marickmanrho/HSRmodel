#
#                           plotdynamics.py
#
# A function to make a ordered plot of all populations.
#
#-------------------------------------------------------------------------------

def plotdynamics(N,dt,maxtime,pop):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    # Create time scale for plotting
    timeaxis = np.linspace(0,dt*(maxtime-1),maxtime)

    # Plot all populations
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for n in range(N):
        x = np.zeros((maxtime,1))
        y = np.zeros((maxtime,1))
        z = np.zeros((maxtime,1))
        for m in range(maxtime):
            x[m] = timeaxis[m]
            y[m] = pop[m,N-n-1]
        ax.plot(x,y,N-n-1,zdir='y')
    ax.set_xlabel('Time (fs)')
    ax.set_ylabel('Site')
    ax.set_zlabel('Probability')
    ax.set_zticks([0,0.2,0.4,0.6,0.8,1])

    ax.set_yticks(np.linspace(0,N-1,N))
    plt.show()
