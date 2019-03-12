def index_h_ct(Nstates,parms):
    import numpy as np
    import itertools

    from CT_n_particle_HF.bring_into_range import bring_into_range_vec

    # Import parameters
    N = parms['N']
    MaxVib = parms['MaxVib']
    incl_nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']
    ct_truncation = parms['ct_truncation']

    # First determine hole position
    # then electron position
    # find different vibrational state locations
    # distribute remaining vibrations

    # For each number of vibrational particles (excluding Frenkel excitons)
    count = np.zeros(incl_nps,)
    kount = 0

    ct_idx = np.zeros((Nstates,incl_nps))
    ct_vib = np.zeros((Nstates,incl_nps))

    for nps in range(incl_nps):
        if nps < 1:
            continue

        for n in range(N): # pos hole
            loc_hole = n

            # find locations electron
            range_e_a = np.linspace(n-1,n-ct_truncation,ct_truncation)
            range_e_b = np.linspace(n+1,n+ct_truncation,ct_truncation)
            loc_e_string = np.concatenate((range_e_a,range_e_b),axis=0)
            loc_e_string = bring_into_range_vec(N,loc_e_string)
            loc_e_string = loc_e_string[(loc_e_string != loc_hole)]
            loc_e_string = np.unique(loc_e_string)
            # Create a list of all possible combinations of positions with length 1
            loc_e_perms = np.array(list(itertools.permutations(loc_e_string,1)))
            # Determine how many permutations we end up with
            nr_e_perms = np.shape(loc_e_perms)

            for m in range(nr_e_perms[0]): # pos electron
                loc_electron = loc_e_perms[m,0]

                # determine how many purely vibrational states are left
                p = nps+1-2

                # There are four different ranges (+/- from the hole and electron)
                range_a = np.linspace(loc_hole-1,loc_hole-nps_truncation,nps_truncation)
                range_b = np.linspace(loc_hole+1,loc_hole+nps_truncation,nps_truncation)
                range_c = np.linspace(loc_electron-1,loc_electron-nps_truncation,nps_truncation)
                range_d = np.linspace(loc_electron+1,loc_electron+nps_truncation,nps_truncation)

                # We combine the ranges
                loc_string = np.concatenate((range_a,range_b,range_c,range_d),axis=0)

                # Fix the edges
                loc_string = bring_into_range_vec(N,loc_string)
                
                # Remove accidental electron and hole locations
                loc_string = loc_string[(loc_string != loc_hole) & (loc_string != loc_electron)]
                loc_string = np.unique(loc_string)

                # determine the permutations on these locations
                loc_perms = np.array(list(itertools.permutations(loc_string,p)))

                # Determine how many permutations we end up with
                nr_perms = np.shape(loc_perms)

                for q in range(nr_perms[0]):
                    loc_temp = np.zeros((incl_nps,))-1
                    loc_temp[0] = loc_hole
                    loc_temp[1] = loc_electron
                    loc_temp[2:2+p] = loc_perms[q,:]

                    v = MaxVib-p
                    # We can have 0,1,2,3 .. v vibrations on a molecule
                    vib_string = np.linspace(0,v,v+1)
                    # Calculate all possible permutations of these with
                    #   len = nps+1
                    vib_perms = list(itertools.product(vib_string,repeat=nps+1))
                    # Select only those permutations with the correct sum of
                    # vibrations
                    vib_sum = np.sum(vib_perms,axis=1)
                    vib_perms = list(itertools.compress(vib_perms,vib_sum<=v))
                    vib_perms = np.array(vib_perms)
                    nr_vib_perms = np.shape(vib_perms)

                    for q in range(nr_vib_perms[0]):
                        ct_idx[kount,:] = loc_temp

                        # save nr. of vibrations on each excitation
                        vib_temp = np.zeros((incl_nps,))-1
                        vib_temp[2:nps+1] = vib_perms[q,2:nps+1]+1
                        vib_temp[0] = vib_perms[q,0]
                        vib_temp[1] = vib_perms[q,1]
                        ct_vib[kount,:] = vib_temp

                        # increase counters
                        count[nps] = count[nps] + 1
                        kount = kount + 1
    return(ct_idx,ct_vib,count)
