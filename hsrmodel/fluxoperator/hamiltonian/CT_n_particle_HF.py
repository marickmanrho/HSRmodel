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

    # Check if calculated and generated sizes agree
    if not (f_count==nparticle_count).all():
        print('Error:')
        print('Calculated size: %s' %np.array2string(nparticle_count))
        print('Actual size:\t %s' %np.array2string(count))
        raise AssertionError('calc_size and index_h_frenkel produce different counts.')

    nparticle_ct_count = calc_size_ct(parms)
    print(nparticle_ct_count)
    Nstates = np.int(np.sum(nparticle_ct_count))
    ct_idx,ct_vibs,ct_count = index_h_ct(Nstates,parms)
    print(ct_count)



    # Build Hamiltonian


parms = {"N": 3, "MaxVib": 1, "incl_nps":2, "nps_truncation": 1, "ct_truncation": 1}
CT_n_particle_HF(parms)
