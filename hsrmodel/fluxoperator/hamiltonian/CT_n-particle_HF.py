def CT_n_particle_HF(parms):
    import numpy as np

    N = parms['N']

    # Index states
    nparticle_count = calc_size(parms)
    Nstates = np.int(np.sum(nparticle_count))
    index_h(Nstates,parms)
    # Build Hamiltonian

def index_h(Nstates,parms):
    import numpy as np
    import itertools

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

    idx = np.zeros((Nstates,incl_nps))
    vib = np.zeros((Nstates,incl_nps))

    for nps in range(incl_nps):

        # Find the permutations possible for a `nps` particle state.
        # First list all possible positions with respect to a Frenkel
        # -trun, - trun+1, .... , -1, 1, .... ,trun
        loc_string = np.linspace(-1,-nps_truncation,nps_truncation)
        loc_string = np.concatenate((loc_string,-loc_string),axis=0)
        # Create a list of all possible combinations of positions with length nps
        loc_perms = np.array(list(itertools.permutations(loc_string,nps)))
        # Determine how many permutations we end up with
        nr_perms = np.shape(loc_perms)

        # For all possible number of vibrations (which are left over to
        # distribute)
        v = max(0,MaxVib-nps)

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

        # Determine the Frenkel position
        for n in range(N):

            # For all possible permutations of vibrational excited states
            # excluding the Frenkel
            for m in range(nr_perms[0]):
                loc = np.zeros((incl_nps,))-1
                loc[0] = n
                # translate position of vibrational excited states to positions
                # around the Frenkel exciton
                loc[1:nps+1] = n+loc_perms[m,:]
                for qq in range(nps):
                    # Fix edges
                    if loc[qq+1] >= N:
                        loc[qq+1] = loc[qq+1]-N
                    if loc[qq+1] < 0:
                        loc[qq+1] = N + loc[qq+1]

                # For all possible permutations of the extra vibrational quanta
                for k in range(nr_vib_perms[0]):
                    # save location of each excitation
                    idx[kount,:] = loc[:]

                    # save nr. of vibrations on each excitation
                    vib_temp = np.zeros((incl_nps,))-1
                    vib_temp[1:nps+1] = vib_perms[k,1:nps+1]+1
                    vib_temp[0] = vib_perms[k,0]
                    vib[kount,:] = vib_temp

                    # Increase count
                    count[nps] = count[nps] + 1
                    kount = kount + 1

def calc_size(parms):
    import numpy as np

    N = parms['N']
    MaxVib = parms['MaxVib']
    nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']

    size = np.zeros((nps,))
    for n in range(nps):
        q = max(0,MaxVib+1-n)
        prefactor = N*factorial(2*nps_truncation)/factorial(2*nps_truncation-n)
        for m in range(0,q):
            size[n] = size[n] + prefactor*factorial(m+n)/(factorial(n)*factorial(m))

    print(size)
    return(size)

# Simple function to calculate factorial
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i

    return f


parms = {"N": 3, "MaxVib": 2, "incl_nps": 3, "nps_truncation": 1}

CT_n_particle_HF(parms)
