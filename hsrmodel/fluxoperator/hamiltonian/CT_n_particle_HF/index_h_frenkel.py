def index_h_frenkel(Nstates,parms):
    import numpy as np
    import itertools

    from CT_n_particle_HF.bring_into_range import bring_into_range_vec

    # Import parameters
    N = parms['N']
    MaxVib = parms['MaxVib']
    incl_nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']

    # First determine Frenkel position
    # Then calculate all possible itterations of neighbourhing particles
    # Distribute vibrations

    # For each number of vibrational particles (excluding Frenkel excitons)
    count = np.zeros(incl_nps,)
    kount = 0

    f_idx = np.zeros((3+Nstates,incl_nps))
    f_vib = np.zeros((3+Nstates,incl_nps))

    for nps in range(incl_nps):
        # For all possible number of vibrations (which are left over to
        # distribute)
        v = MaxVib-nps

        # We can have 0,1,2,3 .. v vibrations on a molecule
        vib_string = np.linspace(0,v,v+1)
        vib_string = np.unique(vib_string)
        # Calculate all possible permutations of these with
        #   len = nps+1
        vib_perms = list(itertools.product(vib_string,repeat=nps+1))
        # Select only those permutations with the correct sum of
        # vibrations
        vib_sum = np.sum(vib_perms,axis=1)
        vib_perms = list(itertools.compress(vib_perms,vib_sum<=v))
        vib_perms = np.array(vib_perms)
        nr_vib_perms = np.shape(vib_perms)

        # Determine the Frenkel position
        for n in range(N):
            # Find the permutations possible for a `nps` particle state.
            # First list all possible positions with respect to a Frenkel
            # -trun, - trun+1, .... , -1, 1, .... ,trun
            range_a = np.linspace(n-1,n-nps_truncation,nps_truncation)
            range_b = np.linspace(n+1,n+nps_truncation,nps_truncation)
            loc_string = np.concatenate((range_a,range_b),axis=0)
            loc_string = bring_into_range_vec(N,loc_string)
            loc_string = loc_string[np.all(loc_string != n)]
            loc_string = np.unique(loc_string)
            # Create a list of all possible combinations of positions with length nps
            loc_perms = np.array(list(itertools.combinations(loc_string,nps)))
            # Determine how many permutations we end up with
            nr_perms = np.shape(loc_perms)

            # For all possible permutations of vibrational excited states
            # excluding the Frenkel
            for m in range(nr_perms[0]):
                loc = np.zeros((incl_nps,))-1
                loc[0] = n
                # translate position of vibrational excited states to positions
                # around the Frenkel exciton
                loc[1:nps+1] = loc_perms[m,:]

                # For all possible permutations of the extra vibrational quanta
                for k in range(nr_vib_perms[0]):
                    # save location of each excitation
                    f_idx[kount,:] = loc[:]

                    # save nr. of vibrations on each molecule
                    vib_temp = np.zeros((incl_nps,))
                    vib_temp[1:nps+1] = vib_perms[k,1:nps+1]+1
                    vib_temp[0] = vib_perms[k,0]
                    f_vib[kount,:] = vib_temp

                    # Increase count
                    count[nps] = count[nps] + 1
                    kount = kount + 1

    return(f_idx,f_vib,count)
