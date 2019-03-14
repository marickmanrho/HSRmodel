def gen_h(f_count,f_idx,f_vibs,ct_count,ct_idx,ct_vibs,parms):
    import numpy as np
    from fluxoperator.hamiltonian.np_frenkel_ct.get_FME import get_FME

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
    Nstates = np.int(np.sum(np.sum(f_count)))#+np.sum(np.sum(ct_count)))
    H = np.zeros((Nstates,Nstates),dtype=complex)
    F = np.zeros((Nstates,Nstates),dtype=complex)

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
            ran[n,0] = ran[n-1,1]
            ran[n,1] = ran[n-1,1] + f_count[n]
    print('Range Frenkels: \n',ran)
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

                    h,f = get_FME(n_idx,n_vibs,m_idx,m_vibs,parms)
                    H[n,m] = H[n,m] + h
                    F[n,m] = F[n,m] + f


    # Block B, Frenkel - CT
    #--------------------------------------------------------------------------#

    # Block C, CT - CT
    #--------------------------------------------------------------------------#
    F = np.zeros((2,2))
    return(H,F)
