#
#
#
#
# https://brilliant.org/wiki/identical-objects-into-distinct-bins/
#
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

    return size

# Simple function to calculate factorial
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i

    return f
