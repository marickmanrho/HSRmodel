#
#                               time_evolution.py
#
# This file contains two main functions td_superoperator and td_hamiltonian.
# These functions correspond to two different ways of calculating the time
# dynamics of the system.
# See README.md in the main project folder for more details.
#
#-------------------------------------------------------------------------------

def td_superoperator(N,E,J,gamma,gammabar,maxtime,dt):
    import numpy as np
    import scipy.linalg.lapack as lapack
    import scipy.linalg as la
    from superoperator import get_superoperator
    from verbose import verbose

    # Generate super density matrix time evolution operator
    L = get_superoperator(N,E,J,gamma,gammabar)

    # Diagonalize L
    Lw = lapack.flapack.zgeev(np.asfortranarray(L,dtype='cfloat'))
    w = Lw[0]
    v = Lw[2]
    #w,v = la.eig(L)
    #w = -1j*w
    # Make sure v is normalized
    # norm = np.zeros((N**2,1))
    # for n in range(N**2):
    #     for m in range(N**2):
    #         norm[n] = norm[n] + np.abs(v[m,n]*np.conj(v[m,n]))
    #     v[:,n] = v[:,n]/np.sqrt(norm[n])

    # Find weights based on initial condition p(t=0) = |1>
    alpha = np.sqrt(np.multiply(v[0,:],np.conj(v[0,:])))
    alpha = np.zeros((N**2,1))
    alpha[:,0] = np.divide(1,v[0,:])
    alpha[:,0] = np.divide(alpha[:,0],np.sum(np.multiply(alpha[0,:],np.conj(alpha[0,:]))))
    # Check initial condition
    Init = np.zeros((N**2,1),dtype=complex)

    for n in range(N**2):
        Init[:,0] = Init[:,0] + alpha[n]*v[:,n]

    # Write info if N<3
    verbose(N,L,w,v,alpha,Init)

    # Setup super density matrix
    p = np.zeros((maxtime,N**2),dtype=complex)
    pe = np.zeros((maxtime,N**2)) # Stores expectation value

    # Calculate dynamics based on eigenvalues and vectors
    for t in range(maxtime):
        for m in range(N**2):
            fact = alpha[m]*np.exp(w[m]*dt*t)
            p[t,:] = p[t,:] + np.transpose(np.multiply(fact,v[:,m]))
        for m in range(N**2):
            pe[t,m] = np.sqrt(p[t,m].real**2 + p[t,m].imag**2)

    # Take trace
    pop = np.zeros((maxtime,N))
    for n in range(N):
        pop[:,n] = pe[:,n*N+n]

    return(pop)

def td_hamiltonian(N,E,J,gamma,gammabar,timesteps,dt):
    import numpy as np
    from hamiltonian import get_hamiltonian
    from densitymatrix import get_densitymatrix
    from population import get_population
    from liouville import get_liouvilleoperator

    # Setup Hamiltonian and Initial conditions
    H = get_hamiltonian(N,E,J)
    rho = get_densitymatrix(N)

    # Init population
    pop = np.zeros((timesteps,N))

    # Run in time
    for t in range(timesteps):
        # Calculate population first and normalize
        pop[t,:] = get_population(rho)
        norm = np.sum(pop[t,:])
        rho = rho/norm

        # Calculate rho_dot and update rho
        rho_dot = get_liouvilleoperator(H,rho,gamma,gammabar)
        rho = rho + rho_dot*dt

    return(pop)
