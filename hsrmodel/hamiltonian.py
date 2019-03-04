def get_hamiltonian(N,E,J):
    import numpy as np

    # Make sure E and J are vectors of length N
    Etemp = E
    Jtemp = J
    sE = np.shape(E)
    sJ = np.shape(J)

    if (sE[0]<N):
        E = np.zeros((N,))
        for n in range(sE[0]):
            E[n] = Etemp[n]

    if (sJ[0]<N):
        J = np.zeros((N,))
        for n in range(sJ[0]):
            J[n] = Jtemp[n]

    # Initialize Hamiltonian
    H = np.zeros((N,N),dtype=complex)

    # Set energy on the diagonal of the Hamiltonian
    H = np.diag(E)

    # Include coulomb coupling J on off diagonal
    for n in range(N):
        Jn = np.zeros((N-n,))+J[n]
        H = H + np.diag(Jn,n) + np.diag(Jn,-n)

    print('Hamiltonian')
    print('-----------')
    print(H)
    return H

# test case
# hamiltonian(2,[1,1],[0,2])
