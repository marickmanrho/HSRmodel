def densitymatrix(N,E,J,gamma,gammabar,maxtime,dt):
    import numpy as np
    import scipy.linalg.lapack as lapack
    import scipy.linalg as la
    from time_evolution import td_densitymatrix
    from verbose import verbose

    # Generate super density matrix time evolution operator
    L = td_densitymatrix(N,E,J,gamma,gammabar)

    # Diagonalize L
    #Lw = lapack.flapack.zgeev(np.asfortranarray(L,dtype='cfloat'))
    #w = Lw[0]
    #v = Lw[2]
    w,v = la.eig(L)
    #w = -1j*w
    # Make sure v is normalized
    norm = np.zeros((N**2,1))
    for n in range(N**2):
        for m in range(N**2):
            norm[n] = norm[n] + np.abs(v[m,n]*np.conj(v[m,n]))
        v[:,n] = v[:,n]/np.sqrt(norm[n])

    # Find weights based on initial condition p(t=0) = |1>
    alpha = v[0,:]

    # Check initial condition
    Init = np.zeros((N**2,1),dtype=complex)

    for n in range(N**2):
        Init[:,0] = Init[:,0] + alpha[n]*v[:,n]

    # Write if N<3
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
