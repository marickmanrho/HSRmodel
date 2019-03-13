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
    from CT_n_particle_HF.gen_h import gen_h

    # Index states
    nparticle_count = calc_size_frenkel(parms)
    Nstates = np.int(np.sum(nparticle_count))
    f_idx,f_vibs,f_count = index_h_frenkel(Nstates,parms)

    #Check if calculated and generated sizes agree
    if not (f_count==nparticle_count).all():
       print('Error:')
       print('Calculated size: %s' %np.array2string(nparticle_count))
       print('Actual size:\t %s' %np.array2string(f_count))
       raise AssertionError('calc_size and index_h_frenkel produce different counts.')

    nparticle_ct_count = calc_size_ct(parms)
    Nstates = np.int(np.sum(nparticle_ct_count))
    ct_idx,ct_vibs,ct_count = index_h_ct(Nstates,parms)

    #Check if calculated and generated sizes agree
    if not (f_count==nparticle_count).all():
       print('Error:')
       print('Calculated size: %s' %np.array2string(nparticle_ct_count))
       print('Actual size:\t %s' %np.array2string(ct_count))
       raise AssertionError('calc_size and index_h_ct produce different counts.')

    # print number of states
    print('Nr Frenkel states:\t', f_count)
    print('Nr CT states:\t\t',ct_count)
    # Save site basis
    #basis_dict = {}
    #basis_dict['f_count'] = f_count
    #basis_dict['f_idx'] = f_idx
    #basis_dict['f_vibs'] = f_vibs
    #basis_dict['ct_count'] = ct_count
    #basis_dict['ct_idx'] = ct_idx
    #basis_dict['ct_vibs'] = ct_vibs

    #from utils.saveJson import save_dict
    #save_dict(basis_dict,parms['PathToDataFolder'],'basis')

    # Build Hamiltonian
    H,F = gen_h(f_count,f_idx,f_vibs,ct_count,ct_idx,ct_vibs,parms)
    n1p = np.int(f_count[0])
    n2p = np.int(f_count[0]+f_count[1])
    print(np.array2string(H[0:n1p,n1p:n2p], precision=3))
    print(np.array2string(H[n1p:n2p,0:n1p], precision=3))

parms = {"N": 3, "MaxVib": 1, "incl_nps": 2, "nps_truncation": 1, "ct_truncation": 1, "E":0, "Esig":0.1, "wvib":1, "S":1, "J":[0,1,1,1]}
CT_n_particle_HF(parms)
