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

                    H[n,m] = H[n,m] + get_matrix_element(n_idx,n_vibs,m_idx,m_vibs)
                    # Diagonal

                    #if np.all(n_idx==m_idx) & np.all(n_vibs == m_vibs):
                    #    H[n,m] = H[n,m] + np.random.normal(E,Esig) + np.sum(f_vibs[n,:])*wvib

                    # Off-diagonal

                    # Check if Frenkel is compatible


    # Block B, Frenkel - CT
    #--------------------------------------------------------------------------#

    # Block C, CT - CT
    #--------------------------------------------------------------------------#
    F = np.zeros((2,2))
    return(H,F)

def get_matrix_element(n_idx,n_vibs,m_idx,m_vibs,parms):
    import numpy as np

    ln = np.shape(n_idx)
    lm = np.shape(m_idx)

    # Three posibilities, either ln < lm, ln = lm, or ln > lm
    # We treat each seperately.

    if ln[0] == lm[0]:
        h = get_matrix_element_equal(n_idx,n_vibs,m_idx,m_vibs,parms)
        return h
    elif ln[0] < lm[0]:
        pass
    elif ln[0] > lm[0]:
        pass
    else:
        raise ValueError('n_idx and m_idx are not proper numpy vectors.')
    # # First check if Frenkel in n is occupied in m
    # if n_idx[0] != m_idx[0]:
    #     if n_idx[0] in m_idx:
    #         # Find where it matches
    #         n_f_in_m = np.array(np.where(m_idx==n_idx[0]))
    #
    #     elif True:  # n_f falls outsize m, thus m_f must be in n
    #         if m_idx[0] in n_idx:
    #             m_f_in_n = np.array(np.where(m_idx[0]==n_idx))
    #             # Also, all vibrations other then on n_f and m_f must be equal
    #             n_idx_temp = np.delete(n_idx,[m_f_in_n],0)
    #             m_idx_temp = np.delete(m_idx,[0],0)
    #         else:
    #             return False
    #     else:
    #         return False
    # else:
    #     return False

    return True # replace by matrix element

def find_distance(n,m,N):
    import numpy as np

    d_a = np.abs(n-m)
    d_b = np.abs(N-m+n)
    d_c = np.abs(N-n+m)
    d = min(d_a,d_b,d_c)
    return d

def get_matrix_element_equal(n_idx,n_vibs,m_idx,m_vibs,parms):
    from fcf import fcf
    # Import parameters
    N = parms['N']
    incl_nps = parms['incl_nps']
    E = parms['E']
    Esig = parms['Esig']
    wvib = parms['wvib']
    S = parms['S']
    J =  np.array(parms['J'])

    # Determine sizes
    ln = np.size(n_idx)
    lm = np.size(m_idx)

    # set default
    h = 0

    # Frenkel must have moved, or the states must be the same
    # Check the latter
    if np.all(n_idx==m_idx) & np.all(n_vibs == m_vibs):
        h = np.random.normal(E,Esig) + np.sum(m_vibs[:])*wvib
    else: # Check the former
        # Two options:
        #   - Frenkel took all of its vibrations and moved to a new molecule
        #   - Frenkel exchanged with existing vibration

        # asses the first option:
        if (n_idx[0] not in m_idx):
            # Make sure all vibrational states have stayed the same
            # remove first index from n_idx and m_idx
            n_idx_temp = n_idx[1:]
            n_vib_temp = n_vibs[1:]
            m_idx_temp = m_idx[1:]
            m_vib_temp = m_vibs[1:]

            if (np.all(n_idx_temp==m_idx_temp) & np.all(n_vib_temp==m_vib_temp)):
                d = find_distance(n_idx[0,0],m_idx[0,0],N)
                h = fcf(0,n_vibs[0,0],S)*fcf(0,m_vibs[0,0],S)*J[d,0]

        # Asses second option:
        if ((n_idx[0] in m_idx) & (m_idx[0] in n_idx)):
            # Find which positions have exchanged
            fn_in_m = np.array(np.where(m_idx==n_idx[0]))
            fm_in_n = np.array(np.where(n_idx==m_idx[0]))

            d = find_distance(n_idx[0,0],m_idx[0,0],N)
            h = fcf(m_vibs[fn_in_m,0],n_vibs[0,0])*fcf(n_vibs[fm_in_n,0],m_vibs[0,0])*J[d,0]

    return h # return default h=0

import numpy as np
n_idx = np.array([[0],[2],[1]])
n_vibs = np.array([[2],[1],[0]])

m_idx = np.array([[3],[2],[1]])
m_vibs = np.array([[0],[1],[0]])

parms = {"N": 4, "MaxVib": 1, "incl_nps": 1, "nps_truncation": 1, "ct_truncation": 1, "E":0, "Esig":0.1, "wvib":2, "S":1, "J":[[0],[1],[2],[3]]}

print(get_matrix_element(n_idx,n_vibs,m_idx,m_vibs,parms))
