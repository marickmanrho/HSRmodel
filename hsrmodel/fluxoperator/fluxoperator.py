#
#                           fluxoperator.py
#
#   This function serves as a wrapper for the fluxoperator model.
#
def fluxoperator(parms):
    import numpy as np

    from utils.loadJson import input_c_np_array, input_eigen
    from utils.saveJson import save_dict
    from fluxoperator.hamiltonian.frenkel_HF import frenkel_HF
    from fluxoperator.solve_H import solve_H
    from fluxoperator.calc_diffusion import calc_diffusion

    Nsamples = parms['Nsamples']

    try:
        # Find out if Gamma range is specified
        Gamma_min = parms['Gamma_min']
        Gamma_max = parms['Gamma_max']
        Gamma_delta = parms['Gamma_delta']

        print('Gamma range specified')

        # Setup vector containing all values of Gamma
        n_Gamma_points = np.int(np.round((Gamma_max-Gamma_min)/Gamma_delta))+1
        Gamma = np.linspace(Gamma_min,Gamma_max,n_Gamma_points)
    except:
        n_Gamma_points = 1
        Gamma = parms['Gamma']

    # Initialize diffusion variable
    Diff = np.zeros((n_Gamma_points,))

    for n in range(Nsamples):
        try: # Importing Hamiltonian and Flux operator
            try:    # Either import existing Hamiltonian, or Solved_Hamiltonian
                H = input_c_np_array('hamiltonian',parms)
                F = input_c_np_array('fluxoperator',parms)
            except:
                w,v = input_eigen('solved_hamiltonian',parms)
        except: # We generate a new Hamiltonian and Flux operator and solve it.
            if parms['hamiltonian'] == 'frenkel':
                H,F = frenkel_HF(parms)
                w,v = solve_H(H,parms)
            else:
                raise ImportError("Hamiltonian type: \'%s\' does not yet excist." %parms['hamiltonian'])

        # Calculate diffusion
        try:
            # Initialize D
            D = np.zeros((n_Gamma_points,))

            # Loop over all Gamma and calculate the Diffusion constant
            for n in range(n_Gamma_points):
                parms["Gamma"] = Gamma[n,]
                D[n] = calc_diffusion(w,v,F,parms)
        except:
            D = calc_diffusion(w,v,F,parms)

        Diff = Diff + D

    Diff = Diff/Nsamples
    Diff_dict = {}
    Diff_dict['diffusion'] = Diff.tolist()
    Diff_dict['gamma'] = Gamma.tolist()
    save_dict(Diff_dict,parms['PathDataFolder'],'diffusion')
