import numpy as np

N = 5
E = 0
diag = [1]*(N-1)
print(diag)

J = np.diag(diag,k=1)+np.diag(diag,k=-1)

print(J)
