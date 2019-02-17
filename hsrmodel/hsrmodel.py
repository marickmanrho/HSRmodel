#
# Haken Strobl Reineker Model
#
def hsrmodel():
    import numpy as np
    from time_evolution import td_densitymatrix

    # Variables
    N = 5
    E = 0
    J = 1
    gamma = np.zeros((1,1),dtype=complex)
    gamma[0][0] = 1j

    maxtime = 1

    # Create initial density matrix
    # Create Frenkel at n=1

    p = np.zeros((N,N),dtype = complex)
    p[0][0] = 1

    # Loop over time

    for i in range(maxtime):
        pd = td_densitymatrix(p,E,J,gamma)
        p = p + pd

    #print(p)

hsrmodel()
