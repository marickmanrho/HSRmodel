#
# Haken Strobl Reineker Model
#
def hsrmodel():
    import numpy as np
    from time_evolution import td_densitymatrix
    import matplotlib.pyplot as plt

    # Variables
    N = 2
    E = 0
    dt = 0.1

    J = np.zeros((N,1),dtype=complex)
    J[0] = 0
    J[1] = 0.5

    gamma = np.zeros((1,1),dtype=complex)
    gamma[0][0] = 0

    maxtime = 100

    Data = np.zeros((maxtime,2), dtype=complex)
    # Create initial density matrix
    # Create Frenkel at n=1

    p = np.zeros((N**2,1),dtype = complex)
    p[0] = 1
    #print(p)
    # Loop over time

    L = td_densitymatrix(N,E,J,gamma)
    print('------------------------------')
    print(L)
    print('------------------------------')
    v,w = np.linalg.eigh(L)
    alpha = np.zeros((N**2,1),dtype=complex)

    for n in range(N**2):
        alpha[n] = w[n][0]

    Data = np.zeros((maxtime,N**2),dtype=complex)
    p1 = np.zeros((maxtime,1))
    p2 = np.zeros((maxtime,1))

    for t in range(maxtime):
        for m in range(N**2):
            Data[t][:] = Data[t][:] + np.multiply(alpha[m],np.transpose(np.multiply(np.exp(-1j*v[m]*dt*t),w[:][m])))

    timeaxis = np.linspace(0,dt*(maxtime-1),maxtime)

    plt.plot(timeaxis,Data[:,0])
    plt.plot(timeaxis,Data[:,3])
    plt.show()

def timestep(N,p,pd):
    import numpy as np
    dt = 1
    count = 0
    for n in range(N):
        for m in range(N):
            p[count] = p[count] + dt*pd[n][m]
            count = count + 1

    return p

hsrmodel()
