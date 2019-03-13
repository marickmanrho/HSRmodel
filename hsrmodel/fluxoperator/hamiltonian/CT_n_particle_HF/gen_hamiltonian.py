def gen_hamiltonian(f_count,f_idx,f_vibs,ct_count,ct_idx,ct_vibs,parms):
    import numpy as np
    from CT_n_particle_HF.fcf import fcf

    # Import parameters
    incl_nps = parms['incl_nps']
    N = parms['N']
    E = parms['E']
    Esig = parms['Esig']
    J = np.array(parms['J'])
    wvib = parms['wvib']
    S = parms['S']

    np_range = np.zeros((incl_nps,2),dtype=int)
    for n in range(incl_nps):
        if n == 0:
            np_range[n,0] = 0
            np_range[n,1] = f_count[n]
        else:
            np_range[n,0] = np_range[n-1,1]
            np_range[n,1] = np_range[n,0] + f_count[n]

    print(np_range)

    Nstates = np.sum(f_count)
    H = np.zeros((Nstates,Nstates),dtype=complex)
    F = np.zeros((Nstates,Nstates),dtype=complex)

    # We calculate all couplings between particles which we now denote as
    # particle a and b.
    for np_a in range(incl_nps):
        # Particle a can only couple to np_a, np_a +/- 1 particle states
        range_np_b = np.array([np_a-1,np_a,np_a+1])
        range_np_b = range_np_b[(range_np_b>=0)&(range_np_b<incl_nps)]
        range_np_b = np.array(range_np_b,dtype=int)

        for np_b in range_np_b:

            for a in range(np_range[np_a,0],np_range[np_a,1]):
                for b in range(np_range[np_b,0],np_range[np_b,1]):

                    # See if we have diagonal
                    if (np.all(f_idx[a,:]==f_idx[b,:]) & np.all(f_vibs[a,:]==f_vibs[b,:])):
                        H[a,b] = H[a,b] + np.random.normal(E,Esig) + np.sum(f_vibs[a,:])*wvib

                    # Exchange
                    elif (f_idx[a,0] in f_idx[b,1:]) & (f_idx[b,0] in f_idx[a,1:]):
                        # test if other vibrations remain equal
                        fa_in_b = np.nonzero(f_idx[a,0]==f_idx[b,:])[0][0]
                        fb_in_a = np.nonzero(f_idx[b,0]==f_idx[a,:])[0][0]

                        if np.all(np.delete(f_idx[a,:],[0,fa_in_b])==np.delete(f_idx[b,:],[0,fb_in_a])):
                            if np.all(np.delete(f_vibs[a,:],[0,fa_in_b])==np.delete(f_vibs[b,:],[0,fb_in_a])):
                                dabs, d = find_distance(f_idx[a,0],f_idx[b,0],N)
                                H[a,b] = H[a,b] + fcf(f_vibs[a,fa_in_b],f_vibs[a,0],S)*fcf(f_vibs[b,fb_in_a],f_vibs[b,0],S)*J[dabs]
                                F[a,b] = -1j*H[a,b]*d
                    # n to n+1 particle state
                    elif (f_idx[a,0] in f_idx[b,:]) & (f_idx[b,0] not in f_idx[a,:]):
                        # test if other vibrations remain equal
                        fa_in_b = np.nonzero(f_idx[a,0]==f_idx[b,:])[0][0]

                        if np.all(np.delete(f_idx[b,:],[0,fa_in_b])==f_idx[a,1:]):
                            if np.all(np.delete(f_vibs[b,:],[0,fa_in_b])==f_idx[a,1:]):
                                dabs,d = find_distance(f_idx[a,0],f_idx[b,0],N)
                                H[a,b] = H[a,b] + fcf(0,f_vibs[b,0],S)*fcf(f_vibs[b,fa_in_b],f_vibs[a,0],S)*J[dabs]
                                F[a,b] = -1j*H[a,b]*d

                    # n+1 to n particle state
                    elif (f_idx[a,0] not in f_idx[b,:]) & (f_idx[b,0] in f_idx[a,:]):
                        # test if other vibrations remain equal
                        fb_in_a = np.nonzero(f_idx[b,0]==f_idx[a,:])[0][0]

                        if np.all(np.delete(f_idx[a,:],[0,fb_in_a])==f_idx[b,1:]):
                            if np.all(np.delete(f_vibs[a,:],[0,fb_in_a])==f_idx[b,1:]):
                                dabs,d = find_distance(f_idx[a,0],f_idx[b,0],N)
                                H[a,b] = H[a,b] + fcf(0,f_vibs[a,0],S)*fcf(f_vibs[a,fb_in_a],f_vibs[b,0],S)*J[dabs]
                                F[a,b] = -1j*H[a,b]*d

                    # Edge case, Frenkel moves completely
                    elif (f_idx[a,0] is not f_idx[b,0]) & (np.all(f_idx[a,1:]==f_idx[b,1:])):
                        if np.all(f_vibs[a,1:]==f_vibs[b,1:]):
                            dabs,d = find_distance(f_idx[a,0],f_idx[b,0],N)
                            H[a,b] = H[a,b] + fcf(0,f_vibs[a,0],S)*fcf(0,f_vibs[b,0],S)*J[dabs]
                            F[a,b] = -1j*H[a,b]*d
    
    return H,F

def find_distance(n,m,N):
    import numpy as np

    d_a = n-m
    d_b = N-m+n
    d_c = N-n+m

    dabs = np.int(min(np.abs(d_a),np.abs(d_b),np.abs(d_c)))
    if dabs == np.int(np.abs(d_a)):
        d = dabs*np.sign(d_a)
    elif dabs == np.int(np.abs(d_b)):
        d = dabs*np.sign(d_b)
    else:
        d = dabs*np.sign(d_c)

    return dabs,d
