def H_and_Flux(parms):

    import numpy as np

    # import variables
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
                H[n,m] = H[n,m] + J[nd]

            # Flux operator
            F[n,m] = F[n,m] - 1j*d*H[n,m]

    return(H,F)

# #Test script
# parms = {"N": 3, "E": 0, "Esig": 1, "J": [[0],[1]]}
# H_and_Flux(parms)