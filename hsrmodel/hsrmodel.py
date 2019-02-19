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
    dt = 0.001

    J = np.zeros((N,1),dtype=complex)
    J[0] = 0
    J[1] = 1j

    gamma = np.zeros((1,1),dtype=complex)
    gamma[0][0] = 1

    maxtime = 10000
    Data = np.zeros((maxtime,2), dtype=complex)
    # Create initial density matrix
    # Create Frenkel at n=1

    p = np.zeros((N**2,1),dtype = complex)
    p[0] = 1
    #print(p)
    # Loop over time

    L = td_densitymatrix(N,p,E,J,gamma)
    v,w = np.linalg.eig(L)
    alpha = np.zeros((N**2,1),dtype=complex)

    for n in range(N**2):
        alpha[n] = w[n][0]

    Data = np.zeros((maxtime,N**2),dtype=complex)
    p1 = np.zeros((maxtime,1),dtype=complex)
    p2 = p1
    for n in range(maxtime):
        for m in range(N**2):
            Data[n][:] = Data[n][:] + np.multiply(alpha[m],np.transpose(np.exp(-1j*v[m]*dt*n)*w[:][m]))
            p1[n] = Data[n][0]
            p2[n] = Data[n][3]

    #plt.plot(abs(p1))
    plt.plot(abs(p2))
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
