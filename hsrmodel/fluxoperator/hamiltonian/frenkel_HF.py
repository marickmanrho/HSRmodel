def frenkel_HF(parms):

    import numpy as np

    from utils.saveJson import save_c_np_array

    # Import variables
    N = parms['N']
    Jt = np.array(parms['J'])
    sJ = np.shape(Jt)
    J = np.zeros((N,))
    J[0:sJ[0]] = Jt[:,0]

    E = parms['E']
    Esig = parms['Esig']

    # Init H and F
    H = np.zeros((N,N),dtype=complex)
    F = np.zeros((N,N),dtype=complex)

    # Calc Hamiltonian and Flux operator
    for n in range(N):
        for m in range(N):
            nd = abs(n-m)
            d = n-m
            if n==m:    # Diagonal
                H[n,m] = H[n,m] + np.random.normal(E,Esig)
            else:       # Off-diagonal
                H[n,m] = H[n,m] + -J[nd]

            # Flux operator
            F[n,m] = F[n,m] - 1j*d*H[n,m]

    # Save to file
    save_c_np_array(H,parms["PathDataFolder"],'hamiltonian')
    save_c_np_array(F,parms["PathDataFolder"],'fluxoperator')

    return(H,F)
