import numpy as np
import scipy.linalg.lapack as lapack

N = 2
r = np.array([[1,3],[2,5]])
print(r[0,0])
x = np.asfortranarray(r)
print(x[0,0])

w = lapack.flapack.sgeev(x)
print(w[0])
print(w[1])
print(w[3])

q,p = np.linalg.eig(r)

print(q)
print(p)
