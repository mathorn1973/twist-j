#!/usr/bin/env python3
"""Exact local audit. NON-CANONICAL L1; not an independent confirmation."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parent
PIN = 'd83fd63b3f3518b247dc4a97378f708a09fb169d90d2af871b08627ffd54b885'
assert hashlib.sha256((ROOT/'PREREG.md').read_bytes()).hexdigest() == PIN
x=s.Symbol('x'); p=41
f=s.Poly(x**4-3*x**3+4*x**2-2*x+1,x)
g=s.Poly(x**4-4*x**3+8*x**2-4*x+1,x); h=f*g
phi5=s.Poly(x**4+x**3+x**2+x+1,x); phi8=s.Poly(x**4+1,x)

def coeff(a: s.Poly, n: int) -> s.Matrix:
    return s.Matrix([a.nth(i) for i in range(n)])

def companion(a: s.Poly) -> s.Matrix:
    n=a.degree()
    return s.Matrix.hstack(*(coeff(s.rem(s.Poly(x**(i+1),x),a),n) for i in range(n)))

def mpow(A: s.Matrix, n: int, mod: int = p) -> s.Matrix:
    A=A.applyfunc(lambda z:int(z)%mod); out=s.eye(A.rows)
    while n:
        if n&1: out=(out*A).applyfunc(lambda z:int(z)%mod)
        A=(A*A).applyfunc(lambda z:int(z)%mod); n//=2
    return out

def mrank(A: s.Matrix, mod: int = p) -> int:
    a=[[int(z)%mod for z in row] for row in A.tolist()]; r=0
    for c in range(A.cols):
        pivot=next((k for k in range(r,A.rows) if a[k][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]; inv=pow(a[r][c],-1,mod)
        a[r]=[(t*inv)%mod for t in a[r]]
        for k in range(A.rows):
            if k!=r:
                z=a[k][c]; a[k]=[(u-z*v)%mod for u,v in zip(a[k],a[r])]
        r+=1
        if r==A.rows: break
    return r

Cf,Cg,H=map(companion,(f,g,h)); D=s.diag(Cf,Cg)
C=s.Matrix.hstack(*(coeff(s.rem(s.Poly(x**i,x),f),4).col_join(
                   coeff(s.rem(s.Poly(x**i,x),g),4)) for i in range(8)))
assert C.det()==41 and D*C==C*H
assert [abs(t) for t in smith_normal_form(C,domain=s.ZZ).diagonal()]==[1]*7+[41]

def power_basis(element: s.Poly, modulus: s.Poly) -> s.Matrix:
    powers=[s.Poly(1,x)]
    for _ in range(3): powers.append(s.rem(powers[-1]*element,modulus))
    return s.Matrix.hstack(*(coeff(t,4) for t in powers))

BJ=power_basis(s.Poly(1+x*x,x),phi5)
BM=power_basis(s.Poly(1+x+x*x,x),phi8)
G5=5*s.eye(4)-s.ones(4); G8=4*s.eye(4)
GS=s.diag(BJ.T*G5*BJ, BM.T*G8*BM)
GR=C.T*GS*C
assert GS.det()==288000 and GR.det()==484128000
assert GR.det()==41**2*GS.det()
assert all(GR[:i,:i].det()>0 for i in range(1,9))
assert all(GS[:i,:i].det()>0 for i in range(1,9))
GSinv=GS.inv(); GRinv=GR.inv()
print('C-JM-ORIENTED-QUADRATIC-READING-N exact audit')
print('predecessor C determinant = 41; intertwining and Smith = PASS')
print('trace Gram determinants S/R =',GS.det(),GR.det())
print('trace Gram ranks modulo 41 S/R =',mrank(GS),mrank(GR))
print('trace Gram leading minors R =',list(GR[:i,:i].det() for i in range(1,9)))

# Direct kernels, positivity and normalizations audited on fixed sample.
basis=[s.eye(8)[:,i] for i in range(8)]
sample=basis+[basis[i]+basis[j] for i in range(8) for j in range(i+1,8)]
sample += [s.Matrix([1,-2,3,-1,2,0,-3,1]),s.ones(8,1)]
for z in sample:
    Q=z*z.T; q=(z.T*GR*z)[0]; K=Q*GR; rho=K/q
    assert q>0 and K*K==q*K
    assert GRinv*K.T*GR==K and rho*rho==rho and s.trace(rho)==1
    assert q*rho*GRinv==Q
    znew=H*z; qnew=(znew.T*GR*znew)[0]
    Hsharp=GRinv*H.T*GR
    t=s.trace(H*rho*Hsharp)
    assert q*t==qnew
    assert H*rho*Hsharp/t==znew*znew.T*GR/qnew
    for w in sample:
        qw=(w.T*GR*w)[0]; b=(w.T*GR*z)[0]
        assert 0 <= b*b <= q*qw
        assert s.trace(rho*(w*w.T*GR/qw))==b*b/(q*qw)
print('rank-one normalization, update and Cauchy audit = PASS sample',len(sample))

# Compatible-seam test, simultaneous sign, and multiplication loss.
U=s.Matrix([[1,19,19**2,19**3,0,0,0,0],
            [0,0,0,0,1,19,19**2,19**3]])
ell=U[0,:]-U[1,:]
assert (ell*C).applyfunc(lambda z:int(z)%41)==s.zeros(1,8)
splus=s.Matrix([1,0,0,0,1,0,0,0]); sminus=s.Matrix([1,0,0,0,-1,0,0,0])
assert (ell*splus)[0]%41==0 and (ell*sminus)[0]%41!=0
assert (splus.T*GS*splus)[0] == (sminus.T*GS*sminus)[0] == 8
assert splus*splus.T != sminus*sminus.T
assert (C.inv()*(41*sminus)).applyfunc(lambda z:z.q)==s.ones(8,1)
assert (C.inv()*sminus).applyfunc(lambda z:z.q)!=s.ones(8,1)
rho_minus=sminus*sminus.T*GS/8
assert (41*sminus)*(41*sminus).T*GS/(8*41**2)==rho_minus
buckets={}
for a in range(41):
    for b in range(41):
        W=(a*a%41,a*b%41,b*b%41)
        assert ((W[0]-2*W[1]+W[2])%41==0)==(a==b)
        buckets.setdefault(W,[]).append((a,b))
assert len(buckets)==(41**2+1)//2
assert all(len(v)==(1 if v==[(0,0)] else 2) for v in buckets.values())
assert len({a*a%41 for a in range(41)})==21
print('residue pairs exhausted = 1681; square fibers = 841; seam sign classes = 21')
print('membership via ell Q ell^T; scalar norm loss; scale-erasure witness = PASS')
print('q(1,-1), q(41,-41) =',8,8*41**2)

# Tensor-module embedding: use Smith normal form of C. Symmetric kernels
# are the star-fixed tensor lattice, not a silently rescaled Sym^2 quotient.
diag=[1]*7+[41]
tensor=sorted(a*b for a in diag for b in diag)
symdiag=sorted(diag[i]*diag[j] for i in range(8) for j in range(i,8))
assert tensor==[1]*49+[41]*14+[41**2]
assert symdiag==[1]*28+[41]*7+[41**2]
pairs=[(i,j) for i in range(8) for j in range(i,8)]

def sym_action(A: s.Matrix) -> s.Matrix:
    cols=[]
    for i,j in pairs:
        F=A[:,i]*A[:,j].T
        if i!=j:F+=A[:,j]*A[:,i].T
        cols.append(s.Matrix([F[a,b] for a,b in pairs]))
    return s.Matrix.hstack(*cols)
CS=sym_action(C)
assert sorted(abs(int(t)) for t in smith_normal_form(CS,domain=s.ZZ).diagonal())==symdiag
assert CS.det()==41**9
print('tensor Smith = 1^49,41^14,1681; index = 41^16')
print('symmetric-kernel Smith = 1^28,41^7,1681; index = 41^9')

# Intrinsic nilpotent direction survives its OUTER square, not multiplication.
kpoly,remainder=s.div(h,s.Poly(x-19,x)); assert remainder.nth(0)%41==0
k=coeff(kpoly,8).applyfunc(lambda z:int(z)%41)
assert k[7]==1 and (C*k).applyfunc(lambda z:int(z)%41)==s.zeros(8,1)
assert s.rem(kpoly*kpoly,h).all_coeffs() and all(int(z)%41==0 for z in s.rem(kpoly*kpoly,h).all_coeffs())
Qk=k*k.T
assert Qk[7,7]==1
assert (C*Qk*C.T).applyfunc(lambda z:int(z)%41)==s.zeros(8)
qk=(k.T*GR*k)[0]
assert qk%41**2==0
print('nilpotent intrinsic vector =',list(k))
print('nilpotent square: ring multiplication zero, tensor nonzero, split reduction zero = PASS')
print('nilpotent q divisible by 41^2 = PASS')

# Exact order after diagonal quadratic read.
negI=(-s.eye(8)).applyfunc(lambda z:int(z)%41)
assert mpow(D,20)==negI and mpow(H,820)==negI
QD=sym_action(D); QH=sym_action(H)
for A,n in [(QD,20),(QH,820)]:
    assert mpow(A,n)==s.eye(36)
    for prime in s.factorint(n): assert mpow(A,n//int(prime))!=s.eye(36)
assert mrank(QD)==36 and mrank(QH)==36
print('exact quadratic mod41 orders split/glued = 20/820')
print('rank(quadratic_glued^20-I) mod41 =',mrank(mpow(QH,20)-s.eye(36)))

# Reference-lift alternative is explicitly on Z direct sum R, not R alone.
Ghat=s.diag(s.ones(1),GR)
for z in sample:
    zh=s.ones(1,1).col_join(z); qh=(zh.T*Ghat*zh)[0]
    rh=zh*zh.T*Ghat/qh
    assert s.trace(rh)==1 and rh*rh==rh
    assert rh[1:,0]/rh[0,0]==z
    assert 1/rh[0,0]-1 == (z.T*GR*z)[0]
print('explicit added-reference normalized reconstruction = PASS')
print('ALL EXACT LOCAL CHECKS PASS; candidate-C audit only')
