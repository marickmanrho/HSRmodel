def fcf(n,m,S):
    import numpy as np

    n = np.int(n)
    m = np.int(m)

    fc = 0
    facn = factorial(n)
    facm = factorial(m)

    for t in range(m+1):
        if (n-m+t < 0 ):
            continue

        facmt = factorial(m-t)
        facnmt = factorial(n-m+t)
        fact = factorial(t)

        facin = 1/(fact*facmt*facnmt)

        fc = fc + facin*S**(t*0.5)*S**(0.5*(n-m+t))*(-1)**(n-m+t)

    fc = fc*np.sqrt(facm*facn)*np.exp(-S/2)
    return fc

def factorial(n):
    f = 1
    for q in range(1,n):
        f = f*q

    return f
