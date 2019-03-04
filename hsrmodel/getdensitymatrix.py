def getdensitymatrix(N):
    import numpy as np

    rho = np.zeros((N,N))

    rho[0][0] = 1

    return rho
