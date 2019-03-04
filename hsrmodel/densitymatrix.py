#
#                               densitymatrix.py
#
# This function quite simply creates an initial condition of the density matrix.
# In general you want either a particular diagonal value to be non-zero, or
# have the complete diagonal corresponding to a specific delocalized Frenkel
# exciton state.
#
#-------------------------------------------------------------------------------

def get_densitymatrix(N):
    import numpy as np

    # initialize
    rho = np.zeros((N,N))

    # set |1><1|= 1, so we start with a Frenkel exciton fully localized at
    # molecule n=1.
    rho[0][0] = 1

    return rho
