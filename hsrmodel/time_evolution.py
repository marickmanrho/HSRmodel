#
# Calc Density function time evolution
#
def pd(p,E,J,gamma):
    import numpy as np

    # Find size of density matrix p
    b = np.shape(p)
    N = b[0]

    # gamma is a vector in general, Gamma is the sum over its components
    # Also we assume gamma is symmetric, gamma(n)=gamma(-n). So we only concern
    # ourselves with positive gamma. We make sure gamma has shape (Nx1)

    a = np.shape(gamma)
    gc = gamma
    gamma = np.zeros((N,1))
    for i in range(a[0]):
        Gamma = Gamma + gc[i]
        gamma[i] = gc[i]

    # Init Density matrix time derivative
    pd = np.zeros((N,N))

    # Populate Coherent part of Desity matrix time derivative
    for i in range(N):
        pd[i][i] = E # Diagonal

        if i < N:
            pd[i][i+1] = -1j*J*(p[j][j]-p[i][i]) # Off diagonal
            pd[i+1][i] = 1j*J*(p[j][j]-p[i][i]) # Symmetric

    # Populate Incoherent part of Density matrix time derivative
    # Diagonal part
    for i in range(N):
        for j in range(N):
            pd[i][i] = pd[i][i] - 2*gamma[abs(i-j)]*(p[i][i]-p[j][j])

    # Off diagonal part
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            g = gamma[abs(i-j)]
            pd[i][j] = pd[i][j] - 2*(Gamma*p[i][j]-g.conj()]p[j][i])
