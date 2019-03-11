#
#                       Haken Strobl Reineker Model
#
# This is the main engine of the software. Calling the hsrmodel() function will
# create the variable input and call either the td_hamiltonian() or
# td_superoperator() routines.
# See README.md in the main project folder for more details.
#
#-------------------------------------------------------------------------------

def hsrmodel(parms):
    import numpy as np

    # Import the functions
    from hamiltonian.get_hamiltonian import get_hamiltonian

    from time_evolution import td_superoperator
    from time_evolution import td_hamiltonian
    from diffusion import diffusion
    import scipy.linalg.lapack as lapack

    # Custom plotting function
    from plotdynamics import plotdynamics
    from plotdiffusion import plotdiffusion

    # create Hamiltonian
    H,F = get_hamiltonian(parms)

    # Diagnoalize Hamiltonian
    Lw = lapack.flapack.zgeev(np.asfortranarray(H,dtype='cfloat'))
    w = Lw[0]
    v = Lw[2]

    # Calculate diffusion
    

    # Choose which version of the code you want to use:
    #   First option is to create a Hamiltonian and compute the Liouville -
    #   operator. The timeseries is determined in an itterative way.
    #pop = td_hamiltonian(N,E,J,gamma,gammabar,timesteps,dt)


    #   Second option is to compute the superoperator of the Liouville operator
    #   and compute the timeseries using the eigenvectors and eigenvalues of the
    #   superoperator.
    #pop = td_superoperator(N,E,J,gamma,gammabar,timesteps,dt)

    #   Calculate diffusion
    #D = diffusion(N,E,J,gamma,gammabar,timesteps,dt)

    # fancier plotting
    #plotdynamics(N,dt,timesteps,pop)
    #plotdiffusion(N,dt,timesteps,D)

# #Test script
parms = {"N": 3, "E": 0, "Esig": 1, "J": [[0],[1]], "save_hamiltonian": False}
hsrmodel(parms)
