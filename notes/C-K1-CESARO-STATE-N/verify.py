#!/usr/bin/env python3
"""Exact K1 spectral calculation. NON-CANONICAL; Python standard library only."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import json

@dataclass(frozen=True)
class K5:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))
    @staticmethod
    def cast(x):
        return x if isinstance(x, K5) else K5(F(x))
    def __add__(self, x):
        x=self.cast(x); return K5(self.a+x.a, self.b+x.b)
    __radd__=__add__
    def __neg__(self): return K5(-self.a,-self.b)
    def __sub__(self,x): return self + (-self.cast(x))
    def __rsub__(self,x): return self.cast(x)-self
    def __mul__(self,x):
        x=self.cast(x)
        return K5(self.a*x.a+5*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cast(x); n=x.a*x.a-5*x.b*x.b
        if not n: raise ZeroDivisionError('zero K5 divisor')
        return self*K5(x.a/n,-x.b/n)
    def __rtruediv__(self,x): return self.cast(x)/self
    def __pow__(self,n):
        if n<0: return (1/self)**(-n)
        out=K5(1); base=self
        while n:
            if n&1: out=out*base
            base=base*base; n//=2
        return out
    def conj(self): return K5(self.a,-self.b)
    def rational(self):
        assert self.b==0, self
        return self.a
    def __str__(self): return f'({self.a})+({self.b})*sqrt(5)'

def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a): return list(map(list,zip(*a)))
def add(a,b): return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def scale(a,c): return [[c*x for x in row] for row in a]
def mul(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def outer(a,b): return [[x*y for y in b] for x in a]
def mv(a,v): return [sum((x*y for x,y in zip(row,v)),F(0)) for row in a]
def vs(a,b): return [x-y for x,y in zip(a,b)]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def zmat(a): return all(K5.cast(x)==K5() for row in a for x in row)
def det(a):
    a=[r[:] for r in a]; ans=F(1); n=len(a)
    for k in range(n):
        pivot=next((r for r in range(k,n) if a[r][k]),None)
        if pivot is None: return F(0)
        if pivot!=k: a[pivot],a[k]=a[k],a[pivot]; ans=-ans
        p=a[k][k]; ans*=p
        for r in range(k+1,n):
            f=a[r][k]/p
            for j in range(k+1,n): a[r][j]-=f*a[k][j]
    return ans

W=('0010','0011','0100','0101','0110','1001','1010','1011','1100','1101')
nu={w:F(1,6 if w in ('0110','1001') else 12) for w in W}
L=[[F(188 if i==j else (-29 if (j-i)%5 in (1,4) else -65),324) for j in range(5)] for i in range(5)]
I=eye(5); P0=[[F(1,5) for j in range(5)] for i in range(5)]
def init(w,t):
    u=int(w[t+2])-int(w[t])
    return [F(int(r==u%5)+int(r==(u+1)%5),2) for r in range(5)]
def energy(a,b):
    p=vs(b,a)
    return (dot(p,p)+dot(b,mv(L,a)))/2

assert sum(nu.values())==1
assert zmat(add(L,scale(tr(L),-1))) and mv(L,[F(1)]*5)==[0]*5
A=[[F(0)]*5 for _ in range(5)]; B=[[F(0)]*5 for _ in range(5)]
energy_law={}; energies={}; finite_checks=0
for w in W:
    a,b=init(w,0),init(w,1)
    A=add(A,scale(outer(a,a),nu[w])); B=add(B,scale(outer(a,b),nu[w]))
    e=energy(a,b); energies[w]=e
    energy_law[e]=energy_law.get(e,F(0))+nu[w]
    for n in range(32):
        nxt=vs(mv(add(scale(I,2),scale(L,-1)),b),a)
        assert energy(b,nxt)==e and sum(nxt)==1
        a,b=b,nxt; finite_checks+=1
assert B==tr(B)
# Universal rational quadratic-form identity, rather than a finite-time proof.
T=[[(2*I[i][j]-L[i][j]) if j<5 else -I[i][j-5] for j in range(10)] for i in range(5)]
T += [[I[i][j] if j<5 else F(0) for j in range(10)] for i in range(5)]
Q=[[F(0)]*10 for _ in range(10)]
for i in range(5):
    for j in range(5):
        Q[i][j]=Q[i+5][j+5]=I[i][j]/2
        Q[i][j+5]=Q[i+5][j]=(L[i][j]-2*I[i][j])/4
assert mul(mul(tr(T),Q),T)==Q
assert energy_law=={F(53,432):F(1,3),F(713,2592):F(1,3),F(67,162):F(1,3)}
E=sum(nu[w]*energies[w] for w in W); assert E==F(701,2592)

lam=[K5(F(235,324),F(1,18)),K5(F(235,324),F(-1,18))]
c=[1-x/2 for x in lam]; d=[1-x*x for x in c]
assert (d[0]*d[1]).rational()==F(60257434105,176319369216)
num=(d[0]*d[1]).rational().numerator
assert num%11==0 and num%121!=0
assert (2*c[0]+2*c[1]).rational()==F(413,162)
assert F(413,162).denominator!=1
# Proof in PROOF.md converts these certificates to all-order nonresonance.
P1=scale(add(L,scale(add(I,scale(P0,-1)),-lam[1])),1/(lam[0]-lam[1]))
P2=add(add(I,scale(P0,-1)),scale(P1,-1)); Ps=[P1,P2]
for p,l in zip(Ps,lam):
    assert zmat(add(mul(p,p),scale(p,-1)))
    assert zmat(add(mul(L,p),scale(p,-l)))
    assert sum(p[i][i] for i in range(5))==K5(2)
assert zmat(mul(P1,P2))
Cs=[]; powers=[]
for k in range(2):
    ck=scale(mul(mul(Ps[k],add(A,scale(B,-c[k]))),Ps[k]),1/d[k])
    Cs.append(ck)
    expected=K5(F(3,40),F(1 if k==0 else -1,40))*(10+lam[k])/(3*lam[k]*(4-lam[k]))
    assert sum(ck[i][i] for i in range(5))/2==expected
    powers.append(expected)
C0=[[K5.cast(x).rational() for x in r] for r in add(*Cs)]
Ctau1=[[K5.cast(x).rational() for x in r] for r in add(scale(Cs[0],c[0]),scale(Cs[1],c[1]))]
assert mv(C0,[F(1)]*5)==[0]*5
# All principal minors are an exact PSD certificate, not an eigenvalue tolerance.
for size in range(1,6):
    for ix in combinations(range(5),size):
        assert det([[C0[i][j] for j in ix] for i in ix])>=0
K=[C0[i]+Ctau1[i] for i in range(5)]+[Ctau1[i]+C0[i] for i in range(5)]
assert mul(mul(T,K),tr(T))==K
mean_variance=sum(C0[i][i] for i in range(5))/5
assert mean_variance==F(25297675542,301287170525)
# An actual finite counterexample to stationarity of the original nu packet law.
mean0=[sum(nu[w]*init(w,0)[r] for w in W) for r in range(5)]
mean2=vs(mv(add(scale(I,2),scale(L,-1)),mean0),mean0)
assert mean2!=mean0
out={
 'status':'candidate-T / NON-CANONICAL, conditional on the frozen K1 inputs',
 'energy_law':{str(e):str(p) for e,p in sorted(energy_law.items())},
 'mean_energy':str(E),
 'radicand_norm':str((d[0]*d[1]).rational()),
 'radicand_norm_11_valuation':1,
 'trace_twocos':str((2*c[0]+2*c[1]).rational()),
 'power_k1_k4':str(powers[0]),'power_k2_k3':str(powers[1]),
 'mean_site_variance':str(mean_variance),
 'stationary_covariance':[[str(x) for x in row] for row in C0],
 'lag1_covariance':[[str(x) for x in row] for row in Ctau1],
 'original_packet_law_stationary':False,
 'finite_recurrence_checks':finite_checks,
 'universal_energy_matrix_identity':True,
 'stationary_pair_matrix_identity':True,
 'all_31_covariance_principal_minors_nonnegative':True,
 'physical_energy_or_tensor_ratio':None,
}
print(json.dumps(out,sort_keys=True,indent=2))
