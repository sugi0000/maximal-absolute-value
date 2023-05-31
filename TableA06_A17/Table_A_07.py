#monic polynomial of degree 7 whose constant term is 1 or -1
#roots are all real and in (0,N+2)
#at least one root is larger than 4
import numpy as np
N=2.04
M1=int(np.floor(7*N))
M2=int(np.floor(21*N**2))
M3=int(np.floor(N**7))
for a in range(-M1,M1+1):
    for b in range(-M2,M2+1):
        s = np.poly1d([2520, 720*a, 120*b])
        root2=np.real_if_close(s.roots)
        if np.isrealobj(root2) and -2<root2[0]<N and -2<root2[1]<N:
            root2=sorted(root2)
            r = np.poly1d([840, 360*a, 120*b, 0])
            m1=min([r(N), r(root2[0])])
            m2=max([r(root2[1]),r(-2)])
            n1=int(np.ceil(-m1/24))
            n2=int(np.ceil(-m2/24))
            if n1<n2:
                for c in range(n1,n2):
                    r = np.poly1d([840, 360*a, 120*b, 24*c])
                    if r(N)>0 and r(-2)<0:
                        r_root=r.roots
                        root3=np.real_if_close(r_root)
                        if np.isrealobj(root3):
                            root3=sorted(root3)
                            q = np.poly1d([210, 120*a, 60*b, 24*c, 0])
                            m1=min([q(N), q(root3[1]), q(-2)])
                            m2=max([q(root3[0]),q(root3[2])])
                            n1=int(np.ceil(-m1/6))
                            n2=int(np.ceil(-m2/6))
                            if n1<n2:
                                for d in range(n1,n2):
                                    q = np.poly1d([210, 120*a, 60*b, 24*c, 6*d])
                                    root4=np.real_if_close(q.roots)
                                    if np.isrealobj(root4):
                                        root4=sorted(root4)
                                        p = np.poly1d([42, 30*a, 20*b, 12*c, 6*d, 0])
                                        m1=min([p(N), p(root4[0]), p(root4[2])])
                                        m2=max([p(root4[1]),p(root4[3]),p(-2)])
                                        n1=int(np.ceil(-m1/2))
                                        n2=int(np.ceil(-m2/2))
                                        if n1<n2:
                                            for e in range(n1,n2):
                                                p = np.poly1d([42, 30*a, 20*b, 12*c, 6*d, 2*e])
                                                root5=np.real_if_close(p.roots)
                                                if np.isrealobj(root5):
                                                    root5=sorted(root5)
                                                    p1 = np.poly1d([7, 6*a, 5*b, 4*c, 3*d, 2*e, 0])
                                                    m1=min([p1(N), p1(root5[1]), p1(root5[3]),p1(-2)])
                                                    m2=max([p1(root5[0]),p1(root5[2]),p1(root5[4])])
                                                    n1=int(np.ceil(-m1))
                                                    n2=int(np.ceil(-m2))
                                                    if n1<n2:
                                                        for f in range(n1,n2):
                                                            p1 = np.poly1d([7, 6*a, 5*b, 4*c, 3*d, 2*e, f])
                                                            if p1(N)>0 and p1(-2)>0 and p1(root5[0])<0 and p1(root5[1])>0 and p1(root5[2])<0 and p1(root5[3])>0 and p1(root5[4])<0:
                                                                g=1+128-64*a+32*b-16*c+8*d-4*e+2*f
                                                                if -M3-1<g<M3+1:
                                                                    p2 = np.poly1d([1, a, b, c, d, e ,f, g])
                                                                    if p2(2)!=0 and p2(1)!=0 and p2(0)!=0 and p2(-1)!=0 and p2(-2)!=0 and p2(N)>0 and p2(-2)<0:
                                                                        v=np.poly1d([1,-2])
                                                                        p2=p2(v)
                                                                        root=np.real_if_close(p2.roots)
                                                                        if np.isrealobj([root[0], root[1], root[2], root[3], root[4], root[5], root[6]]) and [0,0,0,0,0,0,0]<[root[0], root[1], root[2], root[3], root[4], root[5], root[6]]<[N+2,N+2,N+2,N+2,N+2,N+2,N+2]:
                                                                            m=max([root[0], root[1], root[2], root[3], root[4], root[5], root[6]])
                                                                            if m>4:
                                                                                print(p2)
                                                                                print(m)
                                                                g=-1+128-64*a+32*b-16*c+8*d-4*e+2*f
                                                                if -M3-1<g<M3+1:
                                                                    p2 = np.poly1d([1, a, b, c, d, e ,f, g])
                                                                    if p2(2)!=0 and p2(1)!=0 and p2(0)!=0 and p2(-1)!=0 and p2(-2)!=0 and p2(N)>0 and p2(-2)<0:
                                                                        v=np.poly1d([1,-2])
                                                                        p2=p2(v)
                                                                        root=np.real_if_close(p2.roots)
                                                                        if np.isrealobj([root[0], root[1], root[2], root[3], root[4], root[5], root[6]]) and [0,0,0,0,0,0,0]<[root[0], root[1], root[2], root[3], root[4], root[5], root[6]]<[N+2,N+2,N+2,N+2,N+2,N+2,N+2]:
                                                                            m=max([root[0], root[1], root[2], root[3], root[4], root[5], root[6]])
                                                                            if m>4:
                                                                                print(p2)
                                                                                print(m)

