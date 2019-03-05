def diffusion(N,E,J,gamma,gammabar,timesteps,dt):
    import numpy as np

    from hamiltonian import get_hamiltonian
    from densitymatrix import get_densitymatrix
    from meansquareddiffusion import get_msd
    from liouville import get_liouvilleoperator

    # Setup Hamiltonian and Initial conditions
    H = get_hamiltonian(N,E,J)
    rho = get_densitymatrix(N)

    # Init population
    D = np.zeros((timesteps,))

    # Run in time
    for t in range(timesteps):
        # Calculate Diffusion constant
        msd = get_msd(rho)
        D[t] = np.abs(msd)/2/(t+1)
        # Calculate rho_dot and update rho
        rho_dot = get_liouvilleoperator(H,rho,gamma,gammabar)
        rho = rho + rho_dot*dt

    return(D)
