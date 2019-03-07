# HSRmodel
A study of the Haken, Strobl, Reineker model.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Usage
Main function is `hsrmodel()` as found in `hsrmodel.py`.

## Time evolution
First we create the coherent part based on ![equation](https://latex.codecogs.com/gif.latex?L_0%20%3D%20H_0%5Ex).

![equation](https://latex.codecogs.com/gif.latex?-i%5BH_0%2Cp%5D_%7Bnm%7D%20%3D%20-i%5Cleft%3Cn%5Cright%7C%5BH_0%2Cp%5D%5Cleft%7Cm%5Cright%3E)
<!-- ( $-i[H_0,p]_{nm} = -i\left<n\right|[H_0,p]\left|m\right>$ ) -->

![equation](https://latex.codecogs.com/gif.latex?%5Cqquad%20%5Cqquad%20%5Cquad%3D%20-i%5Cleft%3Cn%5Cright%7C%5Cleft%5B%5Cleft%28%5Csum_%7Bn%27%7D%20%5Cepsilon%20%5Cleft%7Cn%27%5Cright%3E%5Cleft%3Cn%27%5Cright%7C&plus;%5Csum_%7Bn%27%5Cneq%20m%27%7D%20J_%7Bn%27m%27%7D%5Cleft%7Cn%27%5Cright%3E%5Cleft%3Cm%27%5Cright%7C%5Cright%29%5Csum_%7Br%2Cq%7D%20p_%7Brq%7D%20%5Cleft%7Cr%5Cright%3E%5Cleft%3Cq%5Cright%7C%5Cright.)
<!--$\qquad \qquad \quad= -i\left<n\right|\left[\left(\sum_{n'} \epsilon \left|n'\right>\left<n'\right|+\sum_{n'\neq m'} J_{n'm'}\left|n'\right>\left<m'\right|\right)\sum_{r,q} p_{rq} \left|r\right>\left<q\right|\right.$-->

![equation](https://latex.codecogs.com/gif.latex?%5Cqquad%20%5Cqquad%20%5Cqquad%20-%20%5Cleft.%5Csum_%7Brq%7D%20p_%7Brq%7D%5Cleft%7Cr%5Cright%3E%5Cleft%3Cq%5Cright%7C%5Cleft%28%5Csum_%7Bn%27%7D%20%5Cepsilon%20%5Cleft%7Cn%27%5Cright%3E%5Cleft%3Cn%27%5Cright%7C%20&plus;%20%5Csum_%7Bn%27%5Cneq%20m%27%7D%20J_%7Bn%27m%27%7D%5Cleft%7Cn%27%5Cright%3E%5Cleft%3Cm%27%5Cright%7C%5Cright%29%5Cright%5D%5Cleft%7Cm%5Cright%3E)
<!--$\qquad \qquad \qquad - \left.\sum_{rq} p_{rq}\left|r\right>\left<q\right|\left(\sum_{n'} \epsilon \left|n'\right>\left<n'\right| + \sum_{n'\neq m'} J_{n'm'}\left|n'\right>\left<m'\right|\right)\right]\left|m\right>$ -->

![equation](https://latex.codecogs.com/gif.latex?%5Cqquad%20%5Cqquad%20%5Cquad%20%3D%20-i%5Csum_%7Bq%7DJ_%7Bnq%7Dp_%7Bqm%7D%20&plus;i%20%5Csum_q%20p_%7Bnq%7DJ_%7Bqm%7D)
<!--$\qquad \qquad \quad = -i\sum_{q}J_{nq}p_{qm} +i \sum_q p_{nq}J_{qm}$-->

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
