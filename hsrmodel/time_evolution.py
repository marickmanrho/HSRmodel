#
# Calc Density function time evolution
#
def td_densitymatrix(N,p,E,J,gamma):
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
                L[idx1][idx2] = L[idx1][idx2] +1j*J[abs(n-q)]
                idx2 = fidx(n,q,N)
                L[idx1][idx2] = L[idx1][idx2] -1j*J[abs(q-m)]

    # Then the Incoherent part of L

    return L

def fidx(n,m,N):
    import numpy as np

    index = n*N+m

    return index
