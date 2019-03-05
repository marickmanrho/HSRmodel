def get_msd(rho):
    import numpy as np

    # Determine size
    srho = np.shape(rho)

    # Init D
    msd = 0
    for n in range(srho[0]):
        msd = msd + rho[n,n]*n**2

    return(msd)
