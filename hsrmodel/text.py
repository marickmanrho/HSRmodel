import scipy.linalg.lapack as la

# http://www.nag.com/lapack-ex/node22.html
import numpy as np
A = np.array([[-1.65 + 2.26j, -2.05 - 0.85j,  0.97 - 2.84j,  0.0         ],
              [6.30j,         -1.48 - 1.75j, -3.99 + 4.01j,  0.59 - 0.48j],
              [0.0,           -0.77 + 2.83j, -1.06 + 1.94j,  3.33 - 1.04j],
              [0.0,            0.0,           4.48 - 1.09j, -0.46 - 1.72j]])

# construction of Ab is tricky.  Fortran indexing starts at 1, not
# 0. This code is based on the definition of Ab at
# http://linux.die.net/man/l/zgbsv. First, we create the Fortran
# indices based on the loops, and then subtract one from them to index
# the numpy arrays.
Ab = np.zeros((5,4),dtype=np.complex)
n, kl, ku = 4, 1, 2

for j in range(1, n + 1):
    for i in range(max(1, j - ku), min(n, j + kl) + 1):
        Ab[kl + ku + 1 + i - j - 1, j - 1] = A[i-1, j-1]

b = np.array([[-1.06  + 21.50j],
              [-22.72 - 53.90j],
              [28.24 - 38.60j],
              [-34.56 + 16.73j]])

v,w = la.flapack.sgeev(Ab)

print(v)

lub, piv, x, info = la.flapack.zgbsv(kl, ku, Ab, b)

# compare to results at http://www.nag.com/lapack-ex/examples/results/zgbsv-ex.r
print('x = ',x)
print('info = ',info)

# check solution
print('solved: ',np.all(np.dot(A,x) - b < 1e-12))

# here is the easy way!!!
print('\n\nbuilt-in solver')
print(np.linalg.solve(A,b))
