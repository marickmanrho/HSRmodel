def louivile(H,rho,gamma,gammabar):
    import numpy as np

    sH = np.shape(H)

    L = np.zeros((sH[0],sH[0]),dtype=complex)

    L = -1j*(np.dot(H,rho)-np.dot(rho,H))

    for n in range(sH[0]):
        for m in range(sH[0]):
            if (n==m):
                continue

            L[n,m] = L[n,m] - 2*gamma[0]
            
    return L
