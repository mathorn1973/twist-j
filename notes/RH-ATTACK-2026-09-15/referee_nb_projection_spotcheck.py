#!/usr/bin/env python3
"""Referee (evidence lens) independent spot-check of a few lane-A numbers.
Own code: binary sum by brute-force cycle detection on 2^j mod L (no v_2/ord bookkeeping),
own Mobius, own p_h, own 2x2 / 3x3 Gaussian elimination. int + Fraction only."""
from fractions import Fraction as Fr
from math import gcd
def lcm(a,b): return a*b//gcd(a,b)
def bsum(q):
    L=len(q); P=[Fr(0)]
    for v in q: P.append(P[-1]+v)
    S=P[L]
    def A(M): return (M//L)*S + P[M%L]
    seen={}; j=0; b=1%L; blocks=[]
    while b not in seen:
        seen[b]=j
        blocks.append(A(2**(j+1))-A(2**j) - Fr(2**j)*S/L)   # eta part only
        b=(2*b)%L; j+=1
    h=seen[b]; t=j-h
    tot=Fr(2)*S/L
    for i in range(h): tot+=blocks[i]/4**i
    cyc=sum(blocks[h+a]/4**a for a in range(t))
    tot+=cyc/(4**h)/(1-Fr(1,4**t))
    return tot
def mob(N):
    mu=[1]*(N+1); mu[0]=0
    for p in range(2,N+1):
        if all(p%d for d in range(2,int(p**0.5)+1)):
            for q in range(p,N+1,p): mu[q]=-mu[q]
            for q in range(p*p,N+1,p*p): mu[q]=0
    return mu
N=200; MU=mob(N)
def A(Q,n): return 1 if n>=1 and n%(2*Q)==Q else 0
def tQ(Q):
    dA=[0]+[A(Q,m)-A(Q,m-1) for m in range(1,N+1)]
    return [0]+[sum(MU[d]*dA[k//d] for d in range(1,k+1) if k%d==0) for k in range(1,N+1)]
ok=True
t=tQ(2)
T=[Fr(0)]*(N+1); s=[0]*(N+1)
for k in range(1,N+1): T[k]=T[k-1]+Fr(t[k],k); s[k]=s[k-1]+t[k]
g8=T[7]-Fr(s[7],8); print("gamma_{2,8} =",g8, g8==Fr(11,168)); ok&= g8==Fr(11,168)
g16=T[15]-Fr(s[15],16); print("gamma_{2,16} =",g16, g16==Fr(89,2772)); ok&= g16==Fr(89,2772)
# p_0 for Q=2 (K=8) and ||A_2 - p_0||^2 over period 840
K=8; c={k:-Fr(t[k],k) for k in range(2,K)}; c[K]=T[K-1]
Lp=840
e=[Fr(A(2,n))-sum(ck*(n%k) for k,ck in c.items()) for n in range(Lp)]
v=bsum([x*x for x in e]); print("||A_2-p_0||^2 =",v, v==Fr(217759,3210480)); ok&= v==Fr(217759,3210480)
print("p_0 == A_2 below cut:", all(e[n]==0 for n in range(0,K)))
# D and Y for (2,1)
D=[e[(2*m+1)%Lp]-e[(2*m)%Lp] for m in range(Lp)]; Y=[(e[(2*m)%Lp]+e[(2*m+1)%Lp])/2 for m in range(Lp)]
nD=bsum([x*x for x in D]); nY=bsum([x*x for x in Y])
print("||D||^2 =",nD, nD==Fr(167,546)); ok&= nD==Fr(167,546)
print("||Y||^2 =",nY, nY==Fr(47507,802620)); ok&= nY==Fr(47507,802620)
print("identity (1) J=1:", v==nY/2+nD/8); ok&= v==nY/2+nD/8
# d_3(A_2)^2 via 2x2 normal equations, own Gram
def rk(k,L): return [n%k for n in range(L)]
G={}
for k in (2,3):
    for l in (2,3):
        L=lcm(k,l); G[(k,l)]=bsum([Fr(a*b) for a,b in zip(rk(k,L),rk(l,L))])
print("G22,G23,G33 =",G[(2,2)],G[(2,3)],G[(3,3)])
nA2=bsum([Fr(A(2,n)) for n in range(4)])
b={k:bsum([Fr(A(2,n)*(n%k)) for n in range(lcm(4,k))]) for k in (2,3)}
det=G[(2,2)]*G[(3,3)]-G[(2,3)]**2
c2=(b[2]*G[(3,3)]-b[3]*G[(2,3)])/det; c3=(G[(2,2)]*b[3]-G[(2,3)]*b[2])/det
d3=nA2-b[2]*c2-b[3]*c3
print("d_3(A_2)^2 =",d3, d3==Fr(1425,8032), " <A_2,r_2> =",b[2]); ok&= d3==Fr(1425,8032) and b[2]==0
b1={k:bsum([Fr(n%k) for n in range(k)]) for k in (2,3)}
c2=(b1[2]*G[(3,3)]-b1[3]*G[(2,3)])/det; c3=(G[(2,2)]*b1[3]-G[(2,3)]*b1[2])/det
print("target 1: c2,c3 =",c2,c3, (c2,c3)==(Fr(160,251),Fr(105,251)), " d_3^2 =",2-b1[2]*c2-b1[3]*c3); ok&=(c2,c3)==(Fr(160,251),Fr(105,251))
# forward convention: t^fwd_2(1) and gamma^fwd at K=2,3
dAf=[0]+[A(2,m+1)-A(2,m) for m in range(1,N+1)]
tf=[0]+[sum(MU[d]*dAf[k//d] for d in range(1,k+1) if k%d==0) for k in range(1,N+1)]
Tf=[Fr(0)]*(N+1); sf=[0]*(N+1)
for k in range(1,N+1): Tf[k]=Tf[k-1]+Fr(tf[k],k); sf[k]=sf[k-1]+tf[k]
print("t^fwd_2(1) =",tf[1]," gamma^fwd_{2,2},{2,3} =",Tf[1]-Fr(sf[1],2),Tf[2]-Fr(sf[2],3))
# Mobius note eq. (23)-(24) source pairs: Delta A_Q backward gives +1 at Qu, -1 at Qu+1 (u odd)
print("backward Delta A_2 at n=2,3,6,7:",[A(2,n)-A(2,n-1) for n in (2,3,6,7)], " forward at n=1,2,5,6:",[A(2,n+1)-A(2,n) for n in (1,2,5,6)])
print("ALL SPOT CHECKS:", "PASS" if ok else "FAIL")
