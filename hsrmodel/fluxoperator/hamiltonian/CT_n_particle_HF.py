#
#                              CT_n_particle_HF
#
#   This function serves as a wrapper for the n-particle Hamiltonian builder
#   including CT states. It outputs the Hamiltonian and Flux matrix

def CT_n_particle_HF(parms):
    import numpy as np
    from CT_n_particle_HF.calc_size import calc_size
    from CT_n_particle_HF.index_h_frenkel import index_h_frenkel

    # Index states
    nparticle_count = calc_size(parms)
    Nstates = np.int(np.sum(nparticle_count))
    f_idx,f_vibs,count = index_h_frenkel(Nstates,parms)

    # Check if calculated and generated sizes agree
    if not (count==nparticle_count).all():
        print('Error:')
        print('Calculated size: %s' %np.array2string(nparticle_count))
        print('Actual size:\t %s' %np.array2string(count))
        raise AssertionError('calc_size and index_h_frenkel produce different counts.')

    # Build Hamiltonian


parms = {"N": 3, "MaxVib": 2, "incl_nps": 3, "nps_truncation": 1}
CT_n_particle_HF(parms)
