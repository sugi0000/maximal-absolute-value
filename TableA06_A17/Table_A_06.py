#monic polynomial of degree 3
#roots are all real and in (-N,N)
#at least one root is larger than 2
import numpy as np
N=2.25
M1=int(np.floor(3*N))
M2=int(np.floor(3*N**2))
M3=int(np.floor(N**3))
for a in range(-M1,M1+1):
    for b in range(-M2,M2+1):
        for c in range(-M3,M3+1):
            p = np.poly1d([1, a, b, c])
            if p(2)!=0 and p(1)!=0 and p(0)!=0 and p(-1)!=0 and p(-2)!=0:
                root=p.roots
                r1=np.real_if_close(root[0])
                r2=np.real_if_close(root[1])
                r3=np.real_if_close(root[2])
                if np.isrealobj([r1, r2, r3]) and -N<r1<N and -N<r2<N and -N<r3<N:
                    m=max([r1,r2,r3])
                    if m>2:
                        print(p)
                        print(m)
