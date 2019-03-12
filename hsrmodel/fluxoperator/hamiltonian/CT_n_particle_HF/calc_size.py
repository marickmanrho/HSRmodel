def calc_size_frenkel(parms):
    import numpy as np

    N = parms['N']
    MaxVib = parms['MaxVib']
    incl_nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']

    size = np.zeros((incl_nps,))
    for n in range(incl_nps):
        q = 2*nps_truncation
        prefactor = N*factorial(q)/(factorial(q-n)*factorial(n)) #factorial(n+q-1)/(factorial(q-1)*factorial(n))
        # if MaxVib-(n) == 0:
        #     size[n] = size[n] + N
        # elif MaxVib-(n) < 0 :
        #     size[n] = size[n]
        # else:
        for v in range(0,MaxVib+1-n):
            fac = factorial(v+n+1-1)/(factorial(n+1-1)*factorial(v))
            size[n] = size[n] + prefactor*fac

    return size

def calc_size_ct(parms):
    import numpy as np

    N = parms['N']
    MaxVib = parms['MaxVib']
    incl_nps = parms['incl_nps']
    nps_truncation = parms['nps_truncation']
    ct_truncation = parms['ct_truncation']

    size = np.zeros((incl_nps,))

    for n in range(incl_nps):
        if n < 1:
            size[n] = 0
        else:
            for s in range(ct_truncation):
                q = min(s+2*nps_truncation,4*nps_truncation)

                p = n-1

                prefactor = 2*N*factorial(q)/(factorial(q-p)*factorial(p))

                for v in range(MaxVib+1-p):
                    size[n] = size[n] + prefactor * factorial(v+n+1-1)/(factorial(n+1-1)*factorial(v))

    return(size)

# Simple function to calculate factorial
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i

    return f
