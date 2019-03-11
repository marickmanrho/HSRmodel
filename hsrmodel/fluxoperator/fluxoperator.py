#
#                           fluxoperator.py
#
#   This function serves as a wrapper for the fluxoperator model.
#
def fluxoperator(parms):

    from utils.loadJson import input_c_np_array, input_eigen
    from fluxoperator.hamiltonian.frenkel_HF import frenkel_HF
    from fluxoperator.solve_H import solve_H
    from fluxoperator.calc_diffusion import calc_diffusion


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
    D = calc_diffusion(w,v,F,parms)
    
