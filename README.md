# HSRmodel
A study of the Haken, Strobl, Reineker model.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Usage
Main function is `hsrmodel()` as found in `hsrmodel.py`.

## Time evolution
First we create the coherent part based on ![equation](https://latex.codecogs.com/gif.latex?L_0%20%3D%20H_0%5Ex).

![equation](https://latex.codecogs.com/gif.latex?-i%5BH_0%2Cp%5D_%7Bnm%7D%20%3D%20-i%5Cleft%3Cn%5Cright%7C%5BH_0%2Cp%5D%5Cleft%7Cm%5Cright%3E) $-i[H_0,p]_{nm} = -i\left<n\right|[H_0,p]\left|m\right>$

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
