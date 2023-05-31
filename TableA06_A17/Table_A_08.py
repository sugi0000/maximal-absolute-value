#monic polynomial of degree 4
#roots are all real and in (-N,N)
#at least one root is larger than 2
import numpy as np
N=2.1
M1=int(np.floor(4*N))
M2=int(np.floor(6*N**2))
M3=int(np.floor(4*N**3))
M4=int(np.floor(N**4))
for a in range(-M1,M1+1):
    for b in range(-M2,M2+1):
        for c in range(-M3,M3+1):
            q = np.poly1d([4, 3*a, 2*b, c])
            if -128*b**3-432*c**2+36*a**2*b**2+432*a*b*c-108*c>0:
                root_3=np.real_if_close(q.roots)
                r1_3=root_3[0]
                r2_3=root_3[1]
                r3_3=root_3[2]
                if np.isrealobj([r1_3, r2_3, r3_3]) and -N<r1_3<N and -N<r2_3<N and -N<r3_3<N:
                    for d in range(-M4,M4+1):
                        p = np.poly1d([1, a, b, c, d])
                        if p(2)!=0 and p(1)!=0 and p(0)!=0 and p(-1)!=0 and p(-2)!=0 and p(N)>0 and p(-N)>0:
                            root=np.real_if_close(p.roots)
                            r1=root[0]
                            r2=root[1]
                            r3=root[2]
                            r4=root[3]
                            if np.isrealobj([r1, r2, r3, r4]) and -N<r1<N and -N<r2<N and -N<r3<N and -N<r4<N:
                                m=max([r1, r2, r3, r4])
                                if m>2:
                                    print(p)
                                    print(m)
