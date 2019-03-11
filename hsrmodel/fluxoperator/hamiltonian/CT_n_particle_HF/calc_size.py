def calc_size_frenkel(parms):
    import numpy as np

    N = parms['N']
    MaxVib = parms['MaxVib']
    incl_nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']

    size = np.zeros((incl_nps,))
    for n in range(incl_nps):
        q = max(0,MaxVib+1-n)
        prefactor = N*factorial(2*nps_truncation)/factorial(2*nps_truncation-n)
        for m in range(0,q):
            size[n] = size[n] + prefactor*factorial(m+n)/(factorial(n)*factorial(m))
    return(size)

def calc_size_ct(parms):
    import numpy as np

    N = parms['N']
    MaxVib = parms['MaxVib']
    incl_nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']
    ct_truncation = parms['ct_truncation']

    size = np.zeros((incl_nps,))
    for n in range(1,incl_nps):
        if n < 1:
            size[n] = 0
        else:
            for s in range(1,ct_truncation+1): # actual range also spans
                                             # -ct_truncation, this is
                                             # compensated later on.
                # truncated range of vibrational states
                q = min(s-1+2*nps_truncation,4*nps_truncation)

                p = n+1-2   # the number of purely vibrational states

                # prefactor including factor 2 due to ct_truncation
                prefactor = 2*N*factorial(p+q-1)/(factorial(q-1)*factorial(p))

                # for all vibrational configurations
                for v in range(MaxVib-p):
                    size[n] = size[n] + prefactor*factorial(v+n+1-1)/(factorial(n+1-1)*factorial(v))

    return(size)

# Simple function to calculate factorial
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i

    return f
