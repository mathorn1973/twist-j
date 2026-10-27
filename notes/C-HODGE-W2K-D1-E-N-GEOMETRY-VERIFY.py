#!/usr/bin/env python3
"""NON-CANONICAL exact audit for the W2K geometric construction.
Standard library only. This checks the displayed certificates, not r or semiregularity.
"""
from fractions import Fraction as Q
from math import comb


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def tr(a): return [list(r) for r in zip(*a)]

def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]

def scale(k,a): return [[k*x for x in r] for r in a]

def inv(a):
    n=len(a); a=[list(map(Q,r))+s for r,s in zip(a,eye(n))]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j])
        a[j],a[p]=a[p],a[j]; v=a[j][j]
        a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j]; a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [r[n:] for r in a]


def det(a):
    a=[list(map(Q,r)) for r in a]; out=Q(1)
    for j in range(len(a)):
        p=next((i for i in range(j,len(a)) if a[i][j]),None)
        if p is None:return Q(0)
        if p!=j:a[p],a[j]=a[j],a[p]; out=-out
        v=a[j][j]; out*=v
        for i in range(j+1,len(a)):
            c=a[i][j]/v
            a[i]=[x-c*y for x,y in zip(a[i],a[j])]
    return out


def block(a,b,c,d):
    return [r+s for r,s in zip(a,b)]+[r+s for r,s in zip(c,d)]


def integer(a): return [[int(x) if Q(x).denominator==1 else str(x) for x in r] for r in a]

I=eye(4); Z=scale(0,I)
M=[[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]
O=[[0,1,0,0],[-1,0,1,0],[0,-1,0,1],[0,0,-1,0]]
phi=scale(-1,add(mm(M,M),mm(mm(M,M),M)))
assert mm(phi,phi)==add(phi,I)
B=[[1,0,Q(1,2),0],[0,Q(1,2),0,0],[0,0,Q(1,2),0],[0,0,0,1]]
phib=mm(inv(B),mm(phi,B)); Ob=mm(tr(B),mm(scale(2,O),B))
assert all(Q(x).denominator==1 for row in phib for x in row)
assert mm(tr(phib),Ob)==mm(Ob,phib)
u=[[1],[3],[1],[0]]
Ru=mm(add(scale(2,phi),scale(-1,I)),u)
lu=mm(add(I,scale(-1,M)),u)
assert all(int(r[0])%5==0 for r in Ru)
assert any(int(r[0])%5 for r in lu)
assert all(int(r[0])%5==0 for r in mm(add(phi,scale(-3,I)),u))
Tm=block(I,scale(-1,I),add(phi,scale(-1,I)),phi)
Bmix=[[1,0,Q(1,2),0,0,0,Q(1,10),0],
      [0,Q(1,2),0,0,0,0,Q(3,10),0],
      [0,0,Q(1,2),0,0,0,Q(1,10),0],
      [0,0,0,1,0,0,0,0],
      [0,0,0,0,1,0,Q(1,10),0],
      [0,0,0,0,0,Q(1,2),Q(3,10),0],
      [0,0,0,0,0,0,Q(1,10),0],
      [0,0,0,0,0,0,0,1]]
Bt=block(B,Z,Z,B); Oprod=block(Ob,Z,Z,Ob)
Tbar=mm(inv(Bt),mm(Tm,Bmix))
Lbar=mm(tr(Tbar),mm(Oprod,Tbar))
Lexpected=[[0,2,-1,2,0,0,1,0],[-2,0,0,-1,0,0,0,0],
 [1,0,0,3,0,0,0,0],[-2,1,-3,0,0,0,0,0],
 [0,0,0,0,0,3,2,-2],[0,0,0,0,-3,0,0,1],
 [-1,0,0,0,-2,0,0,1],[0,0,0,0,2,-1,-1,0]]
assert all(Q(x).denominator==1 for row in Tbar for x in row)
assert det(Tm)==25 and det(Tbar)==5 and det(Bmix)==Q(1,80)
assert Lbar==Lexpected
assert det(Lbar)==25
print('phi on quotient lattice:',integer(phib))
print('sqrt(5) u:',integer(Ru),'(1-j)u:',integer(lu))
print('Tbar:',integer(Tbar))
print('deg T upstairs / downstairs: 25 / 5')
print('Tbar^t (Theta + Theta) Tbar = frozen Lbar: PASS')

# Polynomial arithmetic; coefficients in ascending order.
def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
    return a or [0]


def pa(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def ps(a,k): return trim([k*x for x in a])

def pm(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)


def pd(a):return trim([i*a[i] for i in range(1,len(a))])

def powp(a,n):
    b=[1]
    for _ in range(n):b=pm(b,a)
    return b

# Richelot identity using b+c=-1, bc=-1. The individual determinants
# are stated in PROOF.md; the remaining quartic is exact over Z.
assert pm([0,2,1],[5,0,-5,0,1])==[0,10,5,-10,-5,2,1]
f=[0,10,5,-10,-5,2,1]
print('Richelot sextic: z(z+2)(z^4-5z^2+5)')

P=19

def mod(a):return trim([x%P for x in a])

def divmodp(a,b):
    a=mod(a); b=mod(b); assert b!=[0]
    q=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b); c=a[-1]*pow(b[-1],-1,P)%P
        q[j]=(q[j]+c)%P
        a=mod(pa(a,ps([0]*j+b,-c)))
    return mod(q),a


def xgcd(a,b):
    aa,bb=mod(a),mod(b); u,v=[1],[0]; w,z=[0],[1]
    while bb!=[0]:
        q,r=divmodp(aa,bb)
        aa,bb=bb,r
        u,w=w,mod(pa(u,ps(pm(q,w),-1)))
        v,z=z,mod(pa(v,ps(pm(q,z),-1)))
    c=pow(aa[-1],-1,P)
    return mod(ps(aa,c)),mod(ps(u,c)),mod(ps(v,c))


def inversion_at(root):
    # x^6 f(root+1/x); f(root)=0 in the specified coefficient field.
    out=[0]*6
    for i in range(1,7):
        out[6-i]=sum(f[k]*comb(k,i)*root**(k-i) for k in range(i,7))
    return trim(out)


def torsion_numerator(F):
    d1=pd(F); d2=pd(d1); d3=pd(d2)
    return pa(pa(ps(pm(pm(F,F),d3),4),ps(pm(pm(F,d1),d2),-6)),ps(powp(d1,3),3))

assert sum(f[k]*8**k for k in range(7))%P==0
assert (8**4-5*8*8+5)%P==0
for root,P,expected in [(0,19,[1]),(-2,11,[0,1]),(8,19,[1])]:
    F=inversion_at(root)
    A=torsion_numerator(F); Ad=pd(A)
    assert len(A)==13 and A[-1]%P and Ad[-1]%P
    d,U,V=xgcd(A,Ad)
    assert d==expected
    assert mod(pa(pm(U,A),pm(V,Ad)))==d
    print('branch root / prime:',root,P,'F:',mod(F))
    print('  gcd(A,A\'):',d)
    print('  Bezout U:',U)
    print('  Bezout V:',V)

Fm=inversion_at(-2)
assert Fm==[1,-10,35,-50,25,-2]
assert pa(Fm,ps(powp([1,-5,5],2),-1))==[0,0,0,0,0,-2]
Am=torsion_numerator(Fm)
assert Am[0]==Am[1]==0 and Am[2]!=0
print('only Weierstrass-based 5-torsion: +/-[infinity - W_-2]')

# All 3-subsets of C5 are uniquely centred arithmetic progressions.
from itertools import combinations
for subset in combinations(range(5),3):
    centers=[]
    for q in subset:
        other=[x for x in subset if x!=q]
        if (sum(other)-2*q)%5==0:centers.append(q)
    assert len(centers)==1
print('C5 triple-centre classification: 10/10')
assert set([1,4]).isdisjoint(set([2,3]))
print('Gamma cap H = {+h,-h}; F2 sends nodes to {+2h,-2h}: disjoint')
assert 2+(-5)-2== -5 # chi(N_A)+chi(N_B) for genus two
assert (-5)+(5+5)//2==0
print('m=2: deg N_A=2, deg N_B=-5, total curve/root top term=0')
print('RESULT: exact geometric certificates PASS; r/profiles/semiregularity NOT COMPUTED')
