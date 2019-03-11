def gen_h(parms):
    import numpy as np

    #from hamiltonian.calc_size import calc_size
    #from hamiltonian.index_h import index_h
    from hamiltonian.Tenzin.H_and_Flux import H_and_Flux

    #print(calc_size(parms))

    # Index states
    #idx = index_h(parms)

    H, F = H_and_Flux(parms)

    return(H,F)
