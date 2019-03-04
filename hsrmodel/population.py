#
#                               population.py
#
# Simpel function to take the absolute value of the diagonal of the
# densitymatrix at time t.
#
#-------------------------------------------------------------------------------

def get_population(rho):
    import numpy as np

    # Determine size
    srho = np.shape(rho)

    # Initialize
    pop = np.zeros((srho[0],))

    # Determine absolute value of diagonal
    for n in range(srho[0]):
        pop[n] = np.abs(np.sqrt(rho[n,n]*np.conj(rho[n,n])))

    return(pop)
