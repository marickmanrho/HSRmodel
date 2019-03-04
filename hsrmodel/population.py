def get_population(rho):
    import numpy as np

    srho = np.shape(rho)

    pop = np.zeros((srho[0],))
    for n in range(srho[0]):
        pop[n] = np.abs(np.sqrt(rho[n,n]*np.conj(rho[n,n])))

    return(pop)
