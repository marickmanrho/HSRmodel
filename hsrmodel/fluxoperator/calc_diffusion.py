#
#
#

def calc_diffusion(w,v,F,parms):
    import numpy as np

    # Import parameters
    N = parms['N']
    Gamma = parms['Gamma']

    if Gamma == 0:
        Gamma = 10^(-10)    # Gamma may not be zero to prevent division by zero
                            # error later on when calculating diffusion constant

    # rotate flux matrix using eigenvectors and take square of values
    F = np.transpose(v)*F*v
    F = F*np.conj(F)

    # Add Hagen-Strobl model
    D = 0
    for n in range(N):
        for m in range(N):
            dE = w[n]-w[m]
            dEs = dE*np.conj(dE)
            D = D + (Gamma/(Gamma**2+np.real(dEs)))*np.real(F[n,m])/N
            
    return(D)
