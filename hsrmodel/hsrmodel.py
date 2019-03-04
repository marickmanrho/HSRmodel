#
# Haken Strobl Reineker Model
#
def hsrmodel():
    import numpy as np
    from hamiltonian import hamiltonian
    from getdensitymatrix import getdensitymatrix
    from getpopulation import getpopulation
    from louivile import louivile

    from densitymatrix import densitymatrix
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

    # H = hamiltonian(N,E,J)
    # rho = getdensitymatrix(N)
    #
    # pop = np.zeros((timesteps,N))
    # for t in range(timesteps):
    #     pop[t,:] = getpopulation(rho)
    #     norm = np.sum(pop[t,:])
    #     rho = rho/norm
    #     L = louivile(H,rho,gamma,gammabar)
    #     rho = rho + L*dt

    pop = densitymatrix(N,E,J,gamma,gammabar,maxtime,dt)

    plotdynamics(N,dt,timesteps,pop)

hsrmodel()
