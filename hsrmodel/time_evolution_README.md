## Readme for time_evolution

First we create the coherent part based on $L_0 = H_0^x$.

$-i[H_0,p]_{nm} = -i\left<n\right|[H_0,p]\left|m\right>$

$\qquad \qquad \quad= -i\left<n\right|\left[\left(\sum_{n'} \epsilon \left|n'\right>\left<n'\right|+\sum_{n'\neq m'} J_{n'm'}\left|n'\right>\left<m'\right|\right)\sum_{r,q} p_{rq} \left|r\right>\left<q\right|\right.$

$\qquad \qquad \qquad - \left.\sum_{rq} p_{rq}\left|r\right>\left<q\right|\left(\sum_{n'} \epsilon \left|n'\right>\left<n'\right| + \sum_{n'\neq m'} J_{n'm'}\left|n'\right>\left<m'\right|\right)\right]\left|m\right>$

$\qquad \qquad \quad = -i\sum_{q}J_{nq}p_{qm} +i \sum_q p_{nq}J_{qm}$

Which results to:
```python
for n in range(N):
    for m in range(N):
        idx1 = fidx(n,m,N)
        for q in range(N):
            idx2 = fidx(q,m,N)
            L[idx1][idx2] = L[idx1][idx2] -1j*J[abs(n-q)]
            idx2 = fidx(n,q,N)
            L[idx1][idx2] = L[idx1][idx2] +1j*J[abs(q-m)]
```