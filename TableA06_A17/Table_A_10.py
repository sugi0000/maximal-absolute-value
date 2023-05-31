#irreducible monic polynomial of degree 4
#roots are all in E_1
import numpy as np
N=1.28
m1=N-1/N
m2=N+1/N
M1=int(np.floor(4*m2))
M2=int(np.floor(6*m2**2))
M3=int(np.floor(4*m2**3))
M4=int(np.floor(m2**4))
for a in range(-M1,1):
    for b in range(-M2,M2+1):
        for c in range(-M3,M3+1):
            for d in range(-M4,M4+1):
                p = np.poly1d([1, a, b, c, d])
                if p(0)!=0:
                    root=p.roots
                    r1=root[0]
                    r2=root[1]
                    r3=root[2]
                    r4=root[3]
                    r11=r1.real
                    r12=r1.imag
                    r21=r2.real
                    r22=r2.imag
                    r31=r3.real
                    r32=r3.imag
                    r41=r4.real
                    r42=r4.imag
                    s_1=r11**2*m2**2+r12**2*m1**2
                    s_2=r21**2*m2**2+r22**2*m1**2
                    s_3=r31**2*m2**2+r32**2*m1**2
                    s_4=r41**2*m2**2+r42**2*m1**2
                    if  s_1<m1**2*m2**2 and s_2<m1**2*m2**2 and s_3<m1**2*m2**2 and s_4<m1**2*m2**2:
                        q = np.poly1d([1, 0])
                        r=(q**2-1)**4+a*q*(q**2-1)**3+b*q**2*(q**2-1)**2++c*q**3*(q**2-1)+d*q**4
                        root=r.roots
                        m=max([abs(root[0]),abs(root[1]),abs(root[2]),abs(root[3]),abs(root[4]),abs(root[5]),abs(root[6]),abs(root[7])])
                        print(p)
                        print(r)
                        print(m)
