def gen_h(parms):
    import numpy as np

    from hamiltonian.calc_size import calc_size
    from hamiltonian.index_h import index_h

    print(calc_size(parms))

    # Index states
    idx = index_h(parms)

    # Gen hamiltonian

    H = np.zeros((2,2))

    return H
