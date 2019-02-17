#
# Calc Density function time evolution
#
def pd(N,E,J,gamma):
    import numpy as np

    # gamma is a vector in general.
    # Gamma is the sum over its components
    a = np.shape(gamma)
    for i in range(a[0]):
        Gamma = Gamma + gamma(i)

    # Init Density matrix time derivative
    pd = np.zeros((N,N))

    # Populate Coherent part of Desity matrix time derivative
    for i in range(N):
        pd[i][i] = E # Diagonal

        if i < N:
            pd[i][i+1] = -1j*J # Off diagonal
            pd[i+1][i] = -1j*J # Symmetric

    # Populate Incoherent part of Density matrix time derivative
    # Diagonal part
    for i in range(N):
        for j in range(N):
            pd[i][i] = pd[i][i] - 2*gamma[abs(i-j)]*(p[i][i]-p[j][j])

    # Off diagonal part
    for i in range(N):
        for j in range(N):
            pd[i][j] = pd[i][j] - 2*(Gamma*p[i][j]-gamma[abs(i-j)]p[j][i])
