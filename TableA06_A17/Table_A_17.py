#monic polynomial of degree 5
#roots are all real and in (-N,N)
#at least one root is larger than 2
import numpy as np
N=2.1
M1=int(np.floor(5*N))
M2=int(np.floor(10*N**2))
for a in range(-M1,M1+1):
    for b in range(-M2,M2+1):
        s = np.poly1d([60, 24*a, 6*b])
        root2=np.real_if_close(s.roots)
        if np.isrealobj(root2) and -N<root2[0]<N and -N<root2[1]<N:
            root2=sorted(root2)
            r = np.poly1d([20, 12*a, 6*b, 0])
            m1=min([r(N), r(root2[0])])
            m2=max([r(root2[1]),r(-N)])
            n1=int(np.ceil(-m1/2))
            n2=int(np.ceil(-m2/2))
            if n1<n2:
                for c in range(n1,n2):
                    r = np.poly1d([20, 12*a, 6*b, 2*c])
                    if r(N)>0 and r(-N)<0:
                        root3=np.real_if_close(r.roots)
                        if np.isrealobj(root3):
                            root3=sorted(root3)
                            q = np.poly1d([5, 4*a, 3*b, 2*c, 0])
                            m1=min([q(N), q(root3[1]), q(-N)])
                            m2=max([q(root3[0]),q(root3[2])])
                            n1=int(np.ceil(-m1))
                            n2=int(np.ceil(-m2))
                            if n1<n2:
                                for d in range(n1,n2):
                                    q = np.poly1d([5, 4*a, 3*b, 2*c, d])
                                    if q(N)>0 and q(-N)>0:
                                        root4=np.real_if_close(q.roots)
                                        if np.isrealobj(root4):
                                            root4=sorted(root4)
                                            p = np.poly1d([1, a, b, c, d, 0])
                                            m1=min([p(N), p(root4[0]), p(root4[2])])
                                            m2=max([p(root4[1]),p(root4[3]),p(-N)])
                                            n1=int(np.ceil(-m1))
                                            n2=int(np.ceil(-m2))
                                            if n1<n2:
                                                for e in range(n1,n2):
                                                    p = np.poly1d([1, a, b, c, d, e])
                                                    if p(2)!=0 and p(1)!=0 and p(0)!=0 and p(-1)!=0 and p(-2)!=0 and p(N)>0 and p(-N)<0:
                                                        root=np.real_if_close(p.roots)
                                                        r1=root[0]
                                                        r2=root[1]
                                                        r3=root[2]
                                                        r4=root[3]
                                                        r5=root[4]
                                                        if np.isrealobj([r1, r2, r3, r4, r5]) and -N<r1<N and -N<r2<N and -N<r3<N and -N<r4<N and -N<r5<N:
                                                            m=max([r1, r2, r3, r4])
                                                            if m>2:
                                                                print(p)
                                                                print(m)
