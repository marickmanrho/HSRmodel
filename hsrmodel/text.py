import numpy as np
N=4
j = 0.1
dJ = [j]*(N-1)
print(dJ)
J = np.diag(dJ,1)+np.diag(dJ,-1)
J[0,N-1] = j
J[N-1,0] = j
print(J)
