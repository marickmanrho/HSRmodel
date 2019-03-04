#
# Haken Strobl Reineker Model
#
def hsrmodel():
    import numpy as np

    from time_evolution import td_superoperator
    from time_evolution import td_hamiltonian

    from plotdynamics import plotdynamics


    # Variables
    # --------------------
    N = 5               # Number of molecules
    E = [0]               # Energy of Frenkel exciton
    timesteps = 1000        #
    maxtime = 1000        # Number of timesteps
    dt = maxtime/timesteps  # Time interval
    # Coulomb coupling
    J = np.zeros((N+1,1),dtype=complex)
    J[0] = 0
    J[1] = -0.01

    # Gamma
    gamma = np.zeros((N,1),dtype=complex)
    gamma[0] = 0.01
    gamma[1] = 0.0
    gammabar = np.zeros((N,1),dtype=complex)
    # --------------------

    # Choose which version of the code you want to use:
    #   First option is to create a Hamiltonian and compute the Liouville -
    #   operator. The timeseries is determined in an itterative way.
    pop = td_hamiltonian(N,E,J,gamma,gammabar,timesteps,dt)
    
    #   Second option is to compute the superoperator of the Liouville operator
    #   and compute the timeseries using the eigenvectors and eigenvalues of the
    #   superoperator.
    #pop = td_superoperator(N,E,J,gamma,gammabar,maxtime,dt)

    plotdynamics(N,dt,timesteps,pop)

hsrmodel()
