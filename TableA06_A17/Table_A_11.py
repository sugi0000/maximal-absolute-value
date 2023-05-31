#monic polynomial of degree 2
#roots are all in E_2
import numpy as np
N=1.28
m1=N-1/N
m2=N+1/N
A=np.sqrt(2)/2
z=1j
w=A+A*z
M1=int(np.floor(2*m2))
M2=int(np.floor(m2**2))
for a in range(-M1,1):
    for b in range(-M1,M1+1):
        for c in range(-M2,M2+1):
            for d in range(-M2,M2+1):
                Z1=a+b*z
                Z2=c+d*z
                p = np.poly1d([1, Z1, Z2])
                if -4*m1**2<a**2+b**2<4*m2**2 and -m2**4<c**2+d**2<m2**4:
                    root=p.roots
                    r1=root[0]
                    r2=root[1]
                    r10=r1*w
                    r20=r2*w
                    r11=r10.real
                    r12=r10.imag
                    r21=r20.real
                    r22=r20.imag
                    s_1=r11**2*m2**2+r12**2*m1**2
                    s_2=r21**2*m2**2+r22**2*m1**2
                    t_1=r11**2*m1**2+r12**2*m2**2
                    t_2=r21**2*m1**2+r22**2*m2**2
                    if  s_1<m1**2*m2**2 and s_2<m1**2*m2**2:
                        q = np.poly1d([1, 0])
                        r=(q**2+z)**2++Z1*q*(q**2+z)+Z2*q**2
                        root=r.roots
                        m=max([abs(root[0]),abs(root[1]),abs(root[2]),abs(root[3])])
                        print(p)
                        print(r)
                        print(m)
