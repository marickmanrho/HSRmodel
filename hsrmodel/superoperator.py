#
#                           superoperator.py
#
# The superoperator is a way of calculating the Liouville equation. In the
# superoperator approach we map the densitymatrix on a vector such that we no
# longer need to construct a ani-commutator for our Liouville operator. The
# Liouville operator now is a matrix of size N^2 which can be diagonalized
# independently of the densitymatrix itself.
# We use the eigenvectors and eigenenergies to calculate the time dynamics.
#
#-------------------------------------------------------------------------------

def get_superoperator(N,E,J,gamma,gammabar):
    import numpy as np

    # gamma is a vector in general, Gamma is the sum over its components
    # Also we assume gamma is symmetric, gamma(n)=gamma(-n). So we only concern
    # ourselves with positive gamma. We make sure gamma has shape (Nx1)

    a = np.shape(gamma)
    gc = gamma
    gamma = np.zeros((N,1),dtype = complex)
    Gamma = 0
    for i in range(a[0]):
        Gamma = Gamma + gc[i]
        gamma[i] = gc[i]
    # Init Super Matrix
    L = np.zeros((N**2,N**2), dtype=complex)

    # Populate Coherent part of L
    for n in range(N):
        for m in range(N):
            idx1 = fidx(n,m,N)
            for q in range(N):
                idx2 = fidx(q,m,N)
                L[idx1,idx2] = L[idx1,idx2] - 1j*J[abs(n-q)]
                idx2 = fidx(n,q,N)
                L[idx1,idx2] = L[idx1,idx2] - 1j*J[abs(q-m)]

    # Then the Incoherent part of L
    # Diagonal part
    # This can be neglected if gamma(0) >> gamma(1)
    for n in range(N):
        idx1 = fidx(n,n,N)
        for m in range(N):
            idx2 = fidx(m,m,N)
            L[idx1,idx1] = L[idx1,idx1] - 2*gamma[abs(n-m)]
            L[idx1,idx2] = L[idx1,idx2] + 2*gamma[abs(n-m)]

    # Off-diagonal part
    for n in range(N):
        for m in range(N):
            if (n!=m):
                idx1 = fidx(n,m,N)
                idx2 = fidx(m,n,N)

                L[idx1,idx1] = L[idx1,idx1] - 2*Gamma
                L[idx1,idx2] = L[idx1,idx2] + 2*np.conj(gammabar[abs(n-m)])

    # Little test to make sure L is symmetric and not Hermitian!
    if np.allclose(L, L.T, atol=0.01) == False:
        exit('L is not symmetric!')
    return L
