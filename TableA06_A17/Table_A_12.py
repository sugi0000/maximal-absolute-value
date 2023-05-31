#monic polynomial of degree 2
#one root in E_3 and the another in E_4
import numpy as np
N=1.28
m1=N-1/N
m2=N+1/N
A=np.sqrt(2+np.sqrt(2))/2
B=np.sqrt(2-np.sqrt(2))/2
z=1j
v=B+A*z
w=A+B*z
C=np.sqrt(2)/2
V=C+C*z
W=-C+C*z
M1=int(np.floor(2*m2))
M2=int(np.floor(m2**2))
for a in range(-M1,1):
    for b in range(-M1,M1+1):
        for c in range(-M2,M2+1):
            for d in range(-M2,M2+1):
                Z1=a+b*np.sqrt(2)*z
                Z2=c+d*np.sqrt(2)*z
                Z3=a-b*np.sqrt(2)*z
                Z4=c-d*np.sqrt(2)*z
                p = np.poly1d([1, Z1, Z2])
                if -4*m2**2<a**2+2*b**2<4*m2**2 and -m2**4<c**2+2*d**2<m2**4:
                    root=p.roots
                    r1=root[0]
                    r2=root[1]
                    r10=r1*v
                    r20=r2*w
                    r11=r10.real
                    r12=r10.imag
                    r21=r20.real
                    r22=r20.imag
                    s_1=r11**2*m2**2+r12**2*m1**2
                    s_2=r21**2*m2**2+r22**2*m1**2
                    r1=root[0]
                    r2=root[1]
                    r10=r1*w
                    r20=r2*v
                    r11=r10.real
                    r12=r10.imag
                    r21=r20.real
                    r22=r20.imag
                    t_1=r11**2*m2**2+r12**2*m1**2
                    t_2=r21**2*m2**2+r22**2*m1**2
                    if s_1<m1**2*m2**2 and s_2<m1**2*m2**2:
                        print(p)
                        print(root)
                        q1=np.poly1d([1, r1, V])
                        q2=np.poly1d([1, r2, W])
                        q=q1*q2
                        print(q)
                        root1=q.roots
                        print(max(abs(root1[0]),abs(root1[1]),abs(root1[2]),abs(root1[3])))
                    if t_1<m1**2*m2**2 and t_2<m1**2*m2**2:
                        print(p)
                        print(root)
                        q1=np.poly1d([1, r1, W])
                        q2=np.poly1d([1, r2, V])
                        q=q1*q2
                        print(q)
                        root1=q.roots
                        print(max(abs(root1[0]),abs(root1[1]),abs(root1[2]),abs(root1[3])))
