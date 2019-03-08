def index_h(parms):
    import numpy as np
    import itertools

    N = parms['N']
    MaxVib = parms['MaxVib']
    incl_nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']

    # First determine Frenkel position
    # Then calculate all possible itterations of neighbourhing particles
    # Distribute vibrations

    # For all vibrational states (excluding the Frenkel)
    count = np.zeros(incl_nps,)
    for nps in range(incl_nps):

        # Find the permutations possible for a `nps` particle state.
        # First list all possible positions
        loc_string = np.linspace(1,2*nps_truncation,2*nps_truncation)
        # Create a list of all possible combinations of positions with length nps
        loc_perms = np.array(list(itertools.permutations(loc_string,nps)))
        # Determine how many permutations we end up with
        nr_perms = np.shape(loc_perms)

        # For all possible number of vibrations (which are left over to
        # distribute)
        q = max(0,MaxVib-nps)

        # We can have 0,1,2,3 .. v vibrations on a molecule
        vib_string = np.linspace(0,q,q+1)
        # Calculate all possible permutations of these with len =
        #   nps+1
        vib_perms = list(itertools.product(vib_string,repeat=nps+1))
        # Select only those permutations with the correct sum of
        # vibrations
        vib_sum = np.sum(vib_perms,axis=1)
        vib_perms = list(itertools.compress(vib_perms,vib_sum<=q))
        nr_vib_perms = np.shape(vib_perms)

        idx = []
        vib = []

        # Determine the Frenkel position
        for n in range(N):

            # For all possible permutations of vibrational states
            for m in range(nr_perms[0]):
                locs = np.zeros(incl_nps,)
                locs[0] = n
                locs[1:nps] = loc_perms[m,:]

                # For all possible permutations of the extra vibrations
                for k in range(nr_vib_perms[0]):
                    #vibs = np.zeros(incl_nps,)
                    #vibs[1:nps] = np.zeros(nps,)+1
                    #vibs[0:nps] = vibs[0:nps] + vib_perms[k,:]

                    #idx.append(locs)
                    #vib.append(vibs)
                    count[nps] = count[nps] + 1

    print(count)

parms = {"N": 50, "MaxVib": 5, "incl_nps": 2, "nps_truncation": 25}
index_h(parms)
