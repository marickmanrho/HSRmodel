
def get_FME(n_idx,n_vibs,m_idx,m_vibs,parms):
    import numpy as np

    n_negs = np.nonzero(n_idx==-1)
    m_negs = np.nonzero(m_idx==-1)

    # remove NaN positions
    n_idx = np.delete(n_idx,n_negs)
    n_vibs = np.delete(n_vibs,n_negs)
    m_idx = np.delete(m_idx,m_negs)
    m_idx = np.delete(m_vibs,m_negs)
    ln = np.shape(n_idx)
    lm = np.shape(m_idx)

    # Three posibilities, either ln < lm, ln = lm, or ln > lm
    # We treat each seperately.

    if ln[0] == lm[0]:
        h,f = get_FME_equal(n_idx,n_vibs,m_idx,m_vibs,parms)
        return h,f
    elif ln[0] < lm[0]:
        h,f = get_FME_less(n_idx,n_vibs,m_idx,m_vibs,parms)
        return h,f
    elif ln[0] > lm[0]:
        h = 0
        f = 0
        return h,f
    else:
        raise ValueError('n_idx and m_idx are not proper numpy vectors.')

    return False # replace by matrix element

def get_FME_equal(n_idx,n_vibs,m_idx,m_vibs,parms):
    import numpy as np
    from CT_n_particle_HF.fcf import fcf
    # Import parameters
    N = parms['N']
    incl_nps = parms['incl_nps']
    E = parms['E']
    Esig = parms['Esig']
    wvib = parms['wvib']
    S = parms['S']
    J =  np.array(parms['J'])

    # Determine sizes
    ln = np.size(n_idx)
    lm = np.size(m_idx)

    # set default
    h = 0
    f = 0
    # Frenkel must have moved, or the states must be the same
    # Check the latter
    if np.all(n_idx==m_idx) & np.all(n_vibs == m_vibs):
        h = np.random.normal(E,Esig) + np.sum(m_vibs)*wvib
    else: # Check the former
        # Two options:
        #   - Frenkel took all of its vibrations and moved to a new molecule
        #   - Frenkel exchanged with existing vibration

        # asses the first option:
        if (n_idx[0] not in m_idx):
            # Make sure all vibrational states have stayed the same
            # remove first index from n_idx and m_idx
            n_idx_temp = n_idx[1:]
            n_vib_temp = n_vibs[1:]
            m_idx_temp = m_idx[1:]
            m_vib_temp = m_vibs[1:]

            if (np.all(n_idx_temp==m_idx_temp) & np.all(n_vib_temp==m_vib_temp)):
                dabs,d = find_distance(n_idx[0],m_idx[0],N)
                h = fcf(0,np.int(n_vibs[0]),S)*fcf(0,np.int(m_vibs[0]),S)*J[dabs]
                f = h*d

        # Asses second option:
        elif ((n_idx[0] in m_idx) & (m_idx[0] in n_idx)):
            # Find which positions have exchanged
            fn_in_m, = np.nonzero(np.array(m_idx)==n_idx[0])
            fm_in_n, = np.nonzero(np.array(n_idx)==m_idx[0])
            dabs,d = find_distance(n_idx[0],m_idx[0],N)

            h = fcf(m_vibs[fn_in_m[0]],np.int(n_vibs[0]),S)*fcf(n_vibs[fm_in_n[0]],np.int(m_vibs[0]),S)*J[dabs]
            f = h*d

    return h,f

def get_FME_less(n_idx,n_vibs,m_idx,m_vibs,parms):
    import numpy as np
    from CT_n_particle_HF.fcf import fcf

    # Import parameters
    N = parms['N']
    incl_nps = parms['incl_nps']
    E = parms['E']
    Esig = parms['Esig']
    wvib = parms['wvib']
    S = parms['S']
    J =  np.array(parms['J'])

    # Determine sizes
    ln = np.size(n_idx)
    lm = np.size(m_idx)

    # set default
    h = 0
    f = 0

    # This only happens when the Frenkel in m recombines with a vibration in m
    if n_idx[0] in m_idx[1:]:
        # find its index
        fn_in_m, = np.nonzero(np.array(m_idx)==n_idx[0])
        # check if the other vibrations remain the same
        n_idx_temp = n_idx[1:]
        n_vibs_temp = n_vibs[1:]
        m_idx_temp = np.delete(m_idx,[0,fn_in_m[0]],0)
        m_vibs_temp = np.delete(m_vibs,[0,fn_in_m[0]],0)

        if np.all(n_idx_temp==m_idx_temp) & np.all(n_vibs_temp==m_vibs_temp):
            dabs,d = find_distance(n_idx[0],m_idx[0],N)
            h = fcf(0,m_vibs[0],S)*fcf(m_vibs[fn_in_m[0]],n_vibs[0],S)*J[dabs]
            f = h*d

    return h,f

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

# import numpy as np
# n_idx = np.array([2])
# n_vibs = np.array([0])
# m_idx = np.array([1,2])
# m_vibs = np.array([0,1])
#
# parms = {"N": 3, "MaxVib": 2, "incl_nps": 2, "nps_truncation": 1, "ct_truncation": 1, "E":0, "Esig":0.1, "wvib":1, "S":1, "J":[0,1,1,1]}
#
# print(get_FME_less(n_idx,n_vibs,m_idx,m_vibs,parms))
