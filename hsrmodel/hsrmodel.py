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
    from time_evolution import td_superoperator
    from time_evolution import td_hamiltonian
    from diffusion import diffusion

    # Custom plotting function
    from plotdynamics import plotdynamics
    from plotdiffusion import plotdiffusion

    # Variables
    # --------------------------------------------------------------------------
    N = 20                # Number of molecules
    E = [0]               # Energy of Frenkel exciton
    timesteps = 40000        #
    maxtime = 4000        # Number of timesteps
    dt = maxtime/timesteps  # Time interval
    # Coulomb coupling
    J = np.zeros((N+1,1),dtype=complex)
    J[0] = 0
    J[1] = -0.01

    # Gamma
    gamma = np.zeros((N,1),dtype=complex)
    gamma[0] = 0.001
    gamma[1] = 0.0
    gammabar = np.zeros((N,1),dtype=complex)
    # --------------------------------------------------------------------------

    # Choose which version of the code you want to use:
    #   First option is to create a Hamiltonian and compute the Liouville -
    #   operator. The timeseries is determined in an itterative way.
    pop = td_hamiltonian(N,E,J,gamma,gammabar,timesteps,dt)


    #   Second option is to compute the superoperator of the Liouville operator
    #   and compute the timeseries using the eigenvectors and eigenvalues of the
    #   superoperator.
    #pop = td_superoperator(N,E,J,gamma,gammabar,timesteps,dt)

    #   Calculate diffusion
    D = diffusion(N,E,J,gamma,gammabar,timesteps,dt)

    # fancier plotting
    plotdynamics(N,dt,timesteps,pop)
    plotdiffusion(N,dt,timesteps,D)

hsrmodel()
