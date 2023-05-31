#monic polynomial of degree 2 whose constant term is zeta_6
#roots have modulus less than N
import numpy as np
N=1.3
z=1j
w=1/2+np.sqrt(3)*z/2
M1=int(np.floor(3*N))
M2=int(np.floor(3*N**2))
a=float(-M1-1)
b=float(-M1-1)
c=float(-M2-1)
d=float(-M2-1)
D=3
while a<M1+1:
    while b<M1+1:
        while c<M2+1:
            while d<M2+1:
                if a**2+b**2*D<9*N**2 and c**2+d**2*D<9*N**4:
                    s=a+b
                    t=c+d
                    if s.is_integer() and t.is_integer():
                        p = np.poly1d([1, a+b*z*np.sqrt(D) ,c+d*z*np.sqrt(D), w])
                        root=p.roots
                        r1=root[0]
                        r2=root[1]
                        r3=root[2]
                        m=max(abs(r1), abs(r2), abs(r3))
                        if m<N:
                            print(p)
                            print(m)
                d=d+1/2
            d=float(-M2-1)
            c=c+1/2
        c=float(-M2-1)
        b=b+1/2
    b=float(-M1-1)
    a=a+1/2
