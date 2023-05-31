#monic polynomial of degree 2 whose constant term is 1
#roots have modulus less than N
import numpy as np
N=1.3
z=1j
M1=int(np.floor(3*N))
M2=int(np.floor(3*N**2))
M3=int(np.floor(4*9*N**4))
a=float(-M1-1)
b=float(-M1-1)
c=float(-M2-1)
d=float(-M2-1)
D=1
while a<M1+1:
    while b<M1+1:
        while c<M2+1:
            while d<M2+1:
                while D<M3+1:
                    if a**2+b**2*D<9*N**2 and c**2+d**2*D<9*N**4:
                        s=a+b
                        t=c+d
                        if (D%4==3 and s.is_integer() and t.is_integer()) or (a.is_integer() and b.is_integer() and c.is_integer() and d.is_integer()):
                            if b!=0 or d!=0:
                                p = np.poly1d([1, a+b*z*np.sqrt(D) ,c+d*z*np.sqrt(D), 1])
                                root=p.roots
                                r1=root[0]
                                r2=root[1]
                                r3=root[2]
                                m=max(abs(r1), abs(r2), abs(r3))
                                if m<N:
                                    print(p)
                                    print(m)
                    D=D+1
                D=1
                d=d+1/2
            d=float(-M2-1)
            c=c+1/2
        c=float(-M2-1)
        b=b+1/2
    b=float(-M1-1)
    a=a+1/2
