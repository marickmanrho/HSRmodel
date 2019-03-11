#
#                           liouville.py
#
# This function will return the Liouville operator acting on the density matrix.
# i.e. $\dot{\rho}=-i L\rho$
#
#-------------------------------------------------------------------------------

def get_liouvilleoperator(H,rho,gamma,gammabar):
    import numpy as np

    # Determine size
    sH = np.shape(H)

    # Initialize
    rho_dot = np.zeros((sH[0],sH[0]),dtype=complex)

    # Construct $L\rho = [H,\rho]$
    rho_dot = -1j*(np.dot(H,rho)-np.dot(rho,H))

    # Introduce HSR model dephasing on all off-diagonal elements
    for n in range(sH[0]):
        for m in range(sH[0]):
            if (n==m):
                continue
            rho_dot[n,m] = rho_dot[n,m] - 2*gamma[0]

    return rho_dot
