def gen_h(f_count,f_idx,f_vibs,ct_count,ct_idx,ct_vibs,parms):
    import numpy as np

    # Import parameters
    N = parms['N']
    incl_nps = parms['incl_nps']
    E = parms['E']
    Esig = parms['Esig']
    wvib = parms['wvib']

    # We generate the Hamiltonian in three blocks.
    #   A | B
    #   B'| C

    # init H
    Nstates = np.int(np.sum(np.sum(f_count))+np.sum(np.sum(ct_count)))
    H = np.zeros((Nstates,Nstates),dtype=complex)

    # Block A, Frenkel - Frenkel
    #--------------------------------------------------------------------------#
    # Use the fact that a 1p state only couples to 2p states.
    # determine ranges
    ran = np.zeros((incl_nps,2),dtype=int)
    for n in range(incl_nps):
        if n == 0:
            ran[n,0] = 0
            ran[n,1] = f_count[n]
        else:
            ran[n,0] = f_count[n-1]
            ran[n,1] = f_count[n]

    for nps_a in range(incl_nps):
        # determine coupling range
        incl_nps_b = np.array([[nps_a-1],[nps_a],[nps_a+1]])
        incl_nps_b = incl_nps_b[(incl_nps_b >= 0) & (incl_nps_b < incl_nps)]

        for nps_b in incl_nps_b:

            for n in range(ran[nps_a,0],ran[nps_a,1]):
                for m in range(ran[nps_b,0],ran[nps_b,1]):
                    n_idx = f_idx[n,:]
                    m_idx = f_idx[m,:]
                    n_vibs = f_vibs[n,:]
                    m_vibs = f_vibs[m,:]
                    # Diagonal
                    if np.all(n_idx==m_idx) & np.all(n_vibs == m_vibs):
                        H[n,m] = H[n,m] + np.random.normal(E,Esig) + np.sum(f_vibs[n,:])*wvib

                    # Off-diagonal

                    # Check if Frenkel is compatible


    # Block B, Frenkel - CT
    #--------------------------------------------------------------------------#

    # Block C, CT - CT
    #--------------------------------------------------------------------------#
    F = np.zeros((2,2))
    return(H,F)

def iscompat_f(n_idx,n_vibs,m_idx,m_vibs):
    import numpy as np

    ln = np.shape(n_idx)
    lm = np.shape(m_idx)

    # First check if Frenkel in n is occupied in m
    if n_idx[0] != m_idx[0]:
        if n_idx[0] in m_idx:
            # Find where it matches
            n_f_in_m = np.array(np.where(m_idx==n_idx[0]))

        elif True:  # n_f falls outsize m, thus m_f must be in n
            if m_idx[0] in n_idx:
                m_f_in_n = np.array(np.where(m_idx[0]==n_idx))
                # Also, all vibrations other then on n_f and m_f must be equal
                n_idx_temp = np.delete(n_idx,[m_f_in_n],0)
                m_idx_temp = np.delete(m_idx,[0],0)
            else:
                return False
        else:
            return False
    else:
        return False

    return True # replace by the indeces of the frenkel positions


import numpy as np
n_idx = np.array([[0],[2],[1]])
n_vibs = np.array([[1],[1],[0]])

m_idx = np.array([[1],[2]])
m_vibs = np.array([[1],[1]])

print(iscompat_f(n_idx,n_vibs,m_idx,m_vibs))
