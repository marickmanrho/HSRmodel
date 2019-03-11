def solve_H(H,parms):

    import numpy as np
    import scipy.linalg.lapack as lapack    # for diagonalization of Hamiltonian
    from utils.saveJson import save_eigen

    Lw = lapack.flapack.zgeev(np.asfortranarray(H,dtype='cfloat'))
    w = Lw[0]
    v = Lw[2]

    save_eigen(w,v,parms['PathDataFolder'],'solved_hamiltonian')

    return(w,v)
