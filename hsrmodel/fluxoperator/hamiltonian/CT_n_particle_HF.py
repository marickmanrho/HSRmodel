#
#                              CT_n_particle_HF
#
#   This function serves as a wrapper for the n-particle Hamiltonian builder
#   including CT states. It outputs the Hamiltonian and Flux matrix

def CT_n_particle_HF(parms):
    import numpy as np
    from CT_n_particle_HF.calc_size import calc_size_frenkel
    from CT_n_particle_HF.calc_size import calc_size_ct
    from CT_n_particle_HF.index_h_frenkel import index_h_frenkel
    from CT_n_particle_HF.index_h_ct import index_h_ct

    # Index states
    nparticle_count = calc_size_frenkel(parms)
    Nstates = np.int(np.sum(nparticle_count))
    f_idx,f_vibs,f_count = index_h_frenkel(Nstates,parms)

    print('Frenkel')
    print('calc:\t', nparticle_count)
    print('gen:\t', f_count)

    # Check if calculated and generated sizes agree
    #if not (f_count==nparticle_count).all():
    #    print('Error:')
    #    print('Calculated size: %s' %np.array2string(nparticle_count))
    #    print('Actual size:\t %s' %np.array2string(f_count))
    #    raise AssertionError('calc_size and index_h_frenkel produce different counts.')

    nparticle_ct_count = calc_size_ct(parms)
    Nstates = np.int(np.sum(nparticle_ct_count))
    ct_idx,ct_vibs,ct_count = index_h_ct(Nstates,parms)

    print('CT')
    print('calc:\t', nparticle_ct_count)
    print('gen:\t', ct_count)

    # print('----------')
    # np.set_printoptions(threshold=np.inf)
    # print('locs')
    # print(ct_idx[36:])
    # print('vibs')
    # print(ct_vibs[36:])

    # Build Hamiltonian


parms = {"N": 7, "MaxVib": 10, "incl_nps": 3, "nps_truncation": 1, "ct_truncation": 1}
CT_n_particle_HF(parms)
