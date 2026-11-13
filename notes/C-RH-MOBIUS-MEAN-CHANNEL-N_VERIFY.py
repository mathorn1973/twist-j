#!/usr/bin/env python3
"""NON-CANONICAL reproduction audit for C-RH-MOBIUS-MEAN-CHANNEL-N.

Checks finite exact identities and rigorous real-zeta interval enclosures used at the current endpoint.
It does not prove the missing uniform-in-N bound, RH, or fixed-epsilon L2 membership."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt
from pathlib import Path
ROOT=Path(__file__).resolve().parent
GRID_BITS=256
ROOT_BITS=288
COUNTS={}
def check(p: bool,g: str) -> None:
    COUNTS[g]=COUNTS.get(g,0)+1
    if not p: raise AssertionError(g)
@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        lo,hi=F(self.lo),F(self.hi)
        if lo>hi: raise ValueError('reversed interval')
        d=1<<GRID_BITS
        object.__setattr__(self,'lo',F((lo.numerator*d)//lo.denominator,d))
        object.__setattr__(self,'hi',F(-((-hi.numerator*d)//hi.denominator),d))
    def __add__(self,other):
        o=iv(other);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-iv(other)
    def __rsub__(self,other):return iv(other)+-self
    def __mul__(self,other):
        o=iv(other);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('interval includes zero')
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,other):return self*iv(other).inv()
    def square(self):
        if self.lo>=0:return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return I(self.hi*self.hi,self.lo*self.lo)
        return I(F(0),max(self.lo*self.lo,self.hi*self.hi))
def iv(a):return a if isinstance(a,I) else I(F(a),F(a))
def nthroot(n:int,q:int)->int:
    if n<0 or q<1:raise ValueError('root domain')
    if n<2 or q==1:return n
    if q==2:return isqrt(n)
    x=1<<((n.bit_length()+q-1)//q)
    while True:
        y=((q-1)*x+n//(x**(q-1)))//q
        if y>=x:break
        x=y
    while x**q>n:x-=1
    while (x+1)**q<=n:x+=1
    return x
@lru_cache(None)
def root_interval(n:int,q:int)->I:
    d=1<<ROOT_BITS;v=n<<(ROOT_BITS*q);r=nthroot(v,q)
    check(r**q<=v<(r+1)**q,'integer root enclosures')
    return I(F(r,d),F(r if r**q==v else r+1,d))
@lru_cache(None)
def reciprocal_power(n:int,s:F)->I:
    # All requested s have fractional part +/-1/q.
    a=s.numerator//s.denominator;r=s-a;q=s.denominator
    if r==0:return iv(F(1,n**a))
    if r==F(1,q):return root_interval(n,q).inv()*F(1,n**a)
    if r==1-F(1,q):return root_interval(n,q)*F(1,n**(a+1))
    raise ValueError('unpreregistered exponent')
def bernoulli(n:int):
    b=[F(1)]
    for m in range(1,n+1):
        b.append(-sum(F(comb(m+1,k))*b[k] for k in range(m))/(m+1))
    return b
B=bernoulli(48)
@lru_cache(None)
def zeta_interval(s:F)->I:
    if s<=1:raise ValueError('only absolutely convergent real zeta values')
    N=128;p=24
    a=reciprocal_power(N,s)
    val=sum((reciprocal_power(n,s) for n in range(1,N)),iv(0))
    val+=a*(F(N)/(s-1)+F(1,2))
    rising=F(1)
    for k in range(1,2*p):
        rising*=s+k-1
        if k%2==1:
            j=(k+1)//2
            val+=a*(B[2*j]*rising/F(factorial(2*j)*N**k))
    # |B_48({x})| <= the sum of absolute polynomial coefficients on [0,1].
    sup=sum(F(comb(2*p,k))*abs(B[k]) for k in range(2*p+1))
    err=a.hi*sup*rising/F(factorial(2*p)*N**(2*p-1))
    out=I(val.lo-err,val.hi+err)
    check(out.lo>0,'positive real zeta intervals')
    check(out.hi-out.lo < F(1,10**40),'real zeta enclosure width')
    return out

def R(n:int):
    return [(-1)**(n-k)*comb(n,k)*comb(n+k+2,k+2) for k in range(n+1)]
def integral_product(a,b,weight:int=0):
    return sum((F(x*y,i+j+weight+1) for i,x in enumerate(a) for j,y in enumerate(b)),F(0))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def export(i:I):return {'lower':str(i.lo),'upper':str(i.hi)}
def coarse(i:I,d:int=10**12):
    return {'denominator':d,'lower_numerator':(i.lo.numerator*d)//i.lo.denominator,
            'upper_numerator':-((-i.hi.numerator*d)//i.hi.denominator)}


def addpoly(a,b):
    z=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):z[i]+=x
    for i,x in enumerate(b):z[i]+=x
    return z

def scalepoly(a,c):return [c*x for x in a]
def mulpoly(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def deriv(a):return [i*a[i] for i in range(1,len(a))] or [F(0)]
def trim(a):
    z=list(a)
    while len(z)>1 and z[-1]==0:z.pop()
    return z

def ev(a,t):
    z=F(0)
    for c in reversed(a):z=z*t+c
    return z

def legendre_shifted(degree):
    p=[[F(1)],[F(-1),F(2)]]
    for k in range(1,degree):
        z=addpoly(scalepoly(mulpoly([-1,2],p[-1]),2*k+1),scalepoly(p[-2],-k))
        p.append(scalepoly(z,F(1,k+1)))
    return p[:degree+1]

def fracpart(x):return x-x.numerator//x.denominator

def hyperbola_audit():
    arrays=[[F(1),-F(1,2),0,F(3,4),-F(2,3)],
            [F((-1)**d,d+1) for d in range(1,13)],
            [F(0),F(3),F(-5),F(0),F(2),F(-1)]]
    for aa in arrays:
        coeff={d:a for d,a in enumerate(aa,1)}
        def M(y):return sum((a for d,a in coeff.items() if d<=y),F(0))
        for k in range(2,65):
            x=F(k,2)
            exact=sum((a*fracpart(x/d) for d,a in coeff.items()),F(0))
            for D in range(1,x.numerator//x.denominator+1):
                inner=sum((a/F(max(D,d)) for d,a in coeff.items()),F(0))
                short=sum((a*fracpart(x/d) for d,a in coeff.items() if d<=D),F(0))
                q=(x/D).numerator//(x/D).denominator
                joined=short+x*inner-sum((M(x/l) for l in range(1,q+1)),F(0))-fracpart(x/D)*M(D)
                check(exact==joined,'finite signed hyperbola identity')

def polynomial_audit():
    ps=legendre_shifted(12)
    for n,p in enumerate(ps):
        for m,q in enumerate(ps):
            check(integral_product(p,q)==(F(1,2*n+1) if m==n else 0),'Legendre exact orthogonality')
        rhs=[F(0)]
        for k in range(n-1,-1,-2):rhs=addpoly(rhs,scalepoly(ps[k],2*(2*k+1)))
        check(trim(deriv(p))==trim(rhs),'Legendre exact derivative expansion')
        for i in range(17):
            t=F(i,16)
            check(abs(ev(p,t))<=1,'finite Legendre value checks')
            check(abs(ev(deriv(p),t))<=n*(n+1),'finite Legendre derivative checks')
    jac=[R(n) for n in range(13)]
    for n,p in enumerate(jac):
        for m,q in enumerate(jac):
            check(integral_product(p,q,2)==(F(1,2*n+3) if m==n else 0),'Jacobi exact orthogonality')
    # Exact finite dual-norm identity on polynomial test functions.
    for degree in range(1,13):
        p=[F(0)]+[F((-1)**k,k+1) for k in range(degree)]
        coeff=[]
        E=F(0)
        for n in range(degree):
            a=integral_product(p,[0]+jac[n])
            coeff.append(a)
            E+=(2*n+3)*a*a
        check(E==integral_product(p,p),'finite dual joint norm identity')
        A=degree+1
        for i in range(17):
            t=F(i,16);v=ev(p,t)
            check(v*v<=A*A*E,'finite polynomial sup estimate')
            check(v*v<=A**6*t*t*E,'finite polynomial endpoint estimate')
    for n in range(33):
        for e in [F(1,4),F(1,16)]:
            delta=e/2;alpha=1-delta
            got=sum((F(R(n)[k])/(F(k+2)-alpha) for k in range(n+1)),F(0))
            prod=F(1,1+delta)
            for k in range(n):prod*=F(k+2-delta,k+2+delta)
            check(got==(-1)**n*prod,'exact power-model Jacobi coefficient')
    for M in range(1,100):
        A=M+1
        check(sum(2*k+1 for k in range(M+1))==A*A,'Legendre kernel exact square sum')
        check(sum((2*k+1)*k*k*(k+1)*(k+1) for k in range(M+1))<=A**6,'global derivative constant check')
    check(F(8,3)*F(600,599)<3,'complete exponential-integral constant')
    check(F(1,4)+1+F(1,3)<2,'elementary arithmetic constant')
    check(48+F(1,4)*F(76,3)<64,'signed arithmetic constant')
    check(9*64**2 < 2**16,'joint upper constant')
    check(F(81,4)<25,'elementary joint upper constant')
    check(F(64,3)<25,'endpoint square inequality')

def actual_moment_audit():
    out=[]
    for e in [F(1,4),F(1,16)]:
        delta=e/2;c=zeta_interval(1+e).inv()
        moments=[]
        for k in range(33):
            sm=F(k+2)-delta;sp=F(k+2)+delta
            moments.append(c/(F(k+1)-delta)-zeta_interval(sm)/(sm*zeta_interval(sp)))
        E=iv(0);partial=[];coeff=[]
        for n in range(33):
            bn=sum((moments[k]*v for k,v in enumerate(R(n))),iv(0))
            coeff.append(export(bn));E+=(2*n+3)*bn.square()
            check(E.lo>=0,'nonnegative actual partial moment energy')
            check(E.hi-E.lo<F(1,10**12),'actual finite energy enclosure precision')
            A=n+2
            # Exact rational enclosure of A^(2-2epsilon).
            scale=reciprocal_power(A,2*e)*(A*A)
            upper=scale*(25/(e*e))
            check(E.hi<=upper.lo,'new elementary upper bound versus actual energy')
            if n in [0,4,8,16,32]:
                val=c.square()/(1+e)+E
                partial.append({'degree':n,'L_N':export(val),'readable':coarse(val),
                                'proved_finite_N_upper':export(c.square()/(1+e)+upper)})
                z=coarse(val)
                print(f'epsilon={e}; N={n}; L_N in [{z["lower_numerator"]},{z["upper_numerator"]}]/{z["denominator"]}',flush=True)
        out.append({'epsilon':str(e),'moments':[export(i) for i in moments],
                    'coefficients':coeff,'partial_energies':partial})
    return out

def main():
    polynomial_audit();hyperbola_audit()
    results=actual_moment_audit()
    print('PASS: '+str(sum(COUNTS.values()))+' exact/rigorous-enclosure checks; '+str(len(COUNTS))+' groups')
    print('An all-N growing upper bound is proved; no uniform finite bound for the full norm.')
    print('All finite moment enclosures have rigorously bounded real-zeta tails. Degree tail remains open.')
    print('No independent analytic review or second architecture; external Mertens input not reverified.')
if __name__=='__main__':main()
