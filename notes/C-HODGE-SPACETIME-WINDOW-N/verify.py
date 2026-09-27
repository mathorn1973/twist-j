#!/usr/bin/env python3
"""Exact audit of the preregistered windowed spacetime construction."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from math import factorial, gcd, lcm
from pathlib import Path
from collections import Counter
import contextlib
import hashlib
import io
import runpy

ROOT=Path(__file__).resolve().parents[2]
ANCHOR='probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py'
HASH='02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9'
PHOTON='probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/verify.py'
PHASH='3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e'

def main():
    for p,h in [(ANCHOR,HASH),(PHOTON,PHASH)]:
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:
            raise RuntimeError('STOP: inherited source hash mismatch')
    with contextlib.redirect_stdout(io.StringIO()):
        m=runpy.run_path(str(ROOT/ANCHOR))
    Q5=m['Q5']; Z=Q5(0); O=Q5(1)
    mm,tr,mv,add,sub,scale,rank,solve,cb=(m[k] for k in
        ('mm','tr','mv','add','sub','scale','rank','solve','colbasis'))
    eye=lambda n:m['eye'](n,Q5)
    mat=lambda a:[[Q5(x) for x in row] for row in a]
    inv=lambda a:tr([solve(a,v) for v in tr(eye(len(a)))])
    def sig(x):return Q5(x.a,-x.b)
    def sgn(x):
        if not isinstance(x,Q5):return (x>0)-(x<0)
        a,b=x.a,x.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if a*b>0:return (a>0)-(a<0)
        d=a*a-5*b*b
        assert d!=0
        r=a if d>0 else b
        return (r>0)-(r<0)
    def ab(x):return x if sgn(x)>=0 else -x
    def maxq(a):
        it=iter(a); out=next(it)
        for x in it:
            if sgn(x-out)>0:out=x
        return out
    def floorq(x):
        a,b=x.a,x.b
        base=a.numerator//a.denominator
        bb=(abs(b.numerator)+b.denominator-1)//b.denominator
        lo,hi=base-3*bb-2,base+3*bb+2
        while hi-lo>1:
            mid=(lo+hi)//2
            if sgn(x-Q5(mid))>=0:lo=mid
            else:hi=mid
        return lo
    def vadd(a,b):return [x+y for x,y in zip(a,b)]
    def vsub(a,b):return [x-y for x,y in zip(a,b)]
    def vmul(a,c):return [c*x for x in a]
    def inner(a,b):return sum((x*y for x,y in zip(a,mv(beta,b))),Z)
    E,g,L,beta,K=(m[k] for k in ('E','B','LQ','WQ','KQ'))
    Pi=mm(mm(mm(E,inv(g)),tr(E)),beta)
    N=sub(eye(6),Pi)
    Q=mat(m['compound2'](m['C']))
    assert rank(Pi)==4 and rank(N)==2 and mm(Pi,Pi)==Pi
    assert mm(Pi,L)==mm(L,Pi) and mm(Pi,Q)==mm(Q,Pi)
    assert mm(mm(tr(L),beta),L)==beta
    assert mm(mm(tr(Q),beta),Q)==beta
    Nbar=[[sig(x) for x in row] for row in N]
    assert rank(tr(cb(N))+[])==2
    assert rank(tr(cb(N)+cb(Nbar)))==4
    rational_rows=[[x.a for x in row] for row in Pi]+[[x.b for x in row] for row in Pi]
    assert rank(rational_rows)==6
    assert mm(mm(tr(L),mm(mm(tr(N),beta),N)),L)==mm(mm(tr(N),beta),N)
    t=tr(E)[3]; tt=inner(t,t); ct=-tt
    assert sgn(ct)>0
    tau=lambda x:inner(t,x)/tt
    spatial=lambda x:vsub(x,vmul(t,tau(x)))
    sp2=lambda x:inner(spatial(x),spatial(x))/ct
    win=lambda w:-inner(mv(N,w),mv(N,w))
    vertices=[[Q5(F(e,2)) for e in es] for es in product((-1,1),repeat=6)]
    c0=maxq(win(e) for e in vertices)
    Rs2=maxq(sp2(mv(Pi,e)) for e in vertices)
    Rt=sum((ab(tau(col)) for col in tr(Pi)),Z)/2
    R=Rt+Rs2+1
    assert sgn(c0)>0 and sgn(Rs2)>=0 and sgn(R-Rt)>=0
    assert sgn(R*R-Rs2)>=0
    assert inner(t,mv(L,t))/tt==Q5(F(3,2))
    tests=0
    for cs in product((-1,0,1),repeat=4):
        x=mv(E,[Q5(F(c,2)) for c in cs])
        for h in (1,2,5,10):
            w=[Q5(floorq(h*v+Q5(F(1,2)))) for v in x]
            assert sgn(win(w)-c0)<=0
            error=vsub(vmul(mv(Pi,w),Q5(F(1,h))),x)
            assert sgn(ab(tau(error))-R/h)<=0
            assert sgn(sp2(error)-R*R/(h*h))<=0
            assert win(mv(L,w))==win(w) and win(mv(Q,w))==win(w)
            tests+=1
    # Rational primary projector and a fully specified primitive integral seed.
    Pibar=[[sig(x) for x in row] for row in Pi]
    PT=mm(Pi,Pibar)
    assert all(x.b==0 for row in PT for x in row)
    basis=cb(PT); assert len(basis)==2
    a,b=basis; aa,bb,ab0=inner(a,a),inner(b,b),inner(a,b)
    assert sgn(aa*bb-ab0*ab0)<0
    if sgn(aa)<0:u=a
    elif sgn(aa)>0:u=vsub(vmul(b,aa),vmul(a,ab0))
    else:
        assert ab0
        u=vadd(b,vmul(a,-(bb+1)/(2*ab0)))
    assert sgn(inner(u,u))<0 and all(x.b==0 for x in u)
    den=lcm(*(x.a.denominator for x in u))
    nums=[int(x.a*den) for x in u]
    common=0
    for x in nums:common=gcd(common,abs(x))
    u=[Q5(x//common) for x in nums]
    if sgn(tau(u))<0:u=vmul(u,Q5(-1))
    ell2=-inner(u,u); assert sgn(ell2)>0 and ell2.b==0 and ell2.a.denominator==1
    assert mv(PT,u)==u and mv(N,u)==[Z]*6
    Lu=mv(L,u)
    assert inner(vsub(Lu,u),vsub(Lu,u))==ell2
    assert sgn(tau(u))>0 and sgn(tau(Lu))>0
    w=[Z]*6; v=u[:]; an0,an1=2,3
    for n in range(1,41):
        w=vadd(w,v); v=mv(L,v)
        assert all(x.b==0 and x.a.denominator==1 for x in w+v)
        assert win(w)==Z and inner(v,v)==-ell2 and sgn(tau(v))>0
        assert -inner(w,w)==ell2*(an1-2)
        assert sgn(tau(w))>0
        an0,an1=an1,3*an1-an0
    # Independent shell-moment reconstruction, no floating point.
    weighted=[]
    for ns,we in zip((2,4,8,10,16),(6,1,15,1,1)):
        shell=[v for v in product(range(-4,5),repeat=3) if sum(x*x for x in v)==ns]
        assert len(shell)=={2:12,4:6,8:12,10:24,16:6}[ns]
        weighted.extend((v,we) for v in shell)
    assert sum(w for v,w in weighted)==288
    for i in range(3):
        for j in range(3):
            assert sum(w*v[i]*v[j] for v,w in weighted)==(648 if i==j else 0)
    assert sum(w*v[0]**4 for v,w in weighted)==3168
    assert sum(w*v[0]**2*v[1]**2 for v,w in weighted)==1056
    assert F(3168,24*324)==F(11,27)
    def cos_interval(x):
        degree=32
        value=sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(degree+1)),F(0))
        error=abs(x)**(2*degree+2)/factorial(2*degree+2)
        return value-error,value+error
    def symbol_interval(k):
        args=Counter()
        for v,w in weighted:
            a=sum((k[i]*v[i] for i in range(3)),F(0)); args[abs(a)]+=w
        lo=hi=F(0)
        for a,w in args.items():
            cl,ch=cos_interval(a); lo+=w*(1-ch); hi+=w*(1-cl)
        return lo/324,hi/324
    photon_tests=0
    for direction in [(F(1),F(0),F(0)),(F(3,5),F(4,5),F(0)),(F(1,3),F(2,3),F(2,3))]:
        assert sum(x*x for x in direction)==1
        for r in (F(1,2),F(1)):
            k=tuple(r*x for x in direction)
            for ep in (F(1,8),F(1,4),F(1,2),F(1)):
                assert ep*r<=1
                slo,shi=symbol_interval(tuple(ep*x for x in k))
                low=r-F(11,27)*ep*ep*r**3
                high=r+F(1,12)*ep*ep*r**3
                assert 0<=ep*low<=ep*high<2
                cl,ch=cos_interval(ep*low)
                assert 2*(1-cl)<=slo
                cl,ch=cos_interval(ep*high)
                assert shi<=2*(1-ch)
                photon_tests+=1
    print('PASS G1: real projector rank 4; rational-source rank 6, so no integer label is erased')
    print('PASS G2: 64-vertex window and covering constants; exact rounding fixtures='+str(tests))
    print('WINDOW_C0',c0)
    print('COVER_R',R)
    print('PASS G3: inherited cone, future-preserving J/C5 action; geometric/order limit rests on written proof')
    print('PASS G4: direct J step has a spacelike displacement at an admitted timelike integer point')
    print('CLOCK_SEED',','.join(str(x.a) for x in u))
    print('CLOCK_STEP_LENGTH_SQUARED',ell2.a)
    print('PASS G5: 40 exact integral cumulative-clock prefixes and chord identities')
    print('PASS G6: exact photon shell moments; rigorous rational null-sheet brackets='+str(photon_tests))
    print('NON-CANONICAL: selected flat event geometry, not native physical spacetime or a massless phase')

if __name__=='__main__':main()
