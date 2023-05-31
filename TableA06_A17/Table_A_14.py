#irreducible monic polynomial of degree 3 whose constant term is 1
#roots have modulus less than N
import numpy as np
N=1.3
z=1j
M1=int(np.floor(3*N))
M2=int(np.floor(3*N**2))
for a in range(-M1,M1+1):
    for c in range(-M2,M2+1):
        p = np.poly1d([1, a, c, 1])
        root=p.roots
        r1=root[0]
        r2=root[1]
        r3=root[2]
        m=max(abs(r1), abs(r2), abs(r3))
        if  m<N:
            print(p)
            print(m)
