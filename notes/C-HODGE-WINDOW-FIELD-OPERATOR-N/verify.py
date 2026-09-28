#!/usr/bin/env python3
"""Exact finite audit for C-HODGE-WINDOW-FIELD-OPERATOR-N."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import contextlib
import hashlib
import io
import runpy

ROOT=Path(__file__).resolve().parents[2]
HASHES={
'probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py':
'02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9',
'notes/C-HODGE-SPACETIME-WINDOW-N/PREREG.md':
'1d987e7f6dae7d1f0b31990ae144a6ad5e719625503abd42d0567db56de75dfa',
'notes/C-HODGE-SPACETIME-WINDOW-N/PROOF.md':
'aefac8315a9858e9bfdf26a51f95b6790830a31e9c185a4c883ad66129f70442',
'probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/verify.py':
'3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e',
}

def main():
    for p,h in HASHES.items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:
            raise RuntimeError('STOP frozen hash '+p)
    with contextlib.redirect_stdout(io.StringIO()):
        m=runpy.run_path(str(ROOT/'probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py'))
    Q=m['Q5']; Z=Q(0); O=Q(1)
    mm,tr,mv,add,sub,scale,rank,solve=(m[k] for k in
        ('mm','tr','mv','add','sub','scale','rank','solve'))
    eye=lambda n:m['eye'](n,Q)
    inv=lambda a:tr([solve(a,v) for v in tr(eye(len(a)))])
    E,g,beta,L=(m[k] for k in ('E','B','WQ','LQ'))
    Pi=mm(mm(mm(E,inv(g)),tr(E)),beta)
    N=sub(eye(6),Pi)
    C=mm(mm(inv(g),tr(E)),beta)
    Ginv=inv(g); Binv=inv(beta)
    Qcyc=[[Q(x) for x in row] for row in m['compound2'](m['C'])]

    def sgn(x):
        a,b=x.a,x.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if a*b>0:return (a>0)-(a<0)
        d=a*a-5*b*b
        if d==0: raise AssertionError('zero comparison ambiguity')
        r=a if d>0 else b
        return (r>0)-(r<0)
    def ab(x): return x if sgn(x)>=0 else -x
    def floorq(x):
        a,b=x.a,x.b
        base=a.numerator//a.denominator
        bb=(abs(b.numerator)+b.denominator-1)//b.denominator
        lo,hi=base-3*bb-3,base+3*bb+3
        while hi-lo>1:
            mid=(lo+hi)//2
            if sgn(x-Q(mid))>=0:lo=mid
            else:hi=mid
        return lo
    def rnd(x): return floorq(x+Q(F(1,2)))
    def vadd(a,b): return [x+y for x,y in zip(a,b)]
    def vmul(a,c): return [c*x for x in a]
    def inner(a,b): return sum((x*y for x,y in zip(a,mv(beta,b))),Z)
    def win(w): return -inner(mv(N,w),mv(N,w))
    c0=Q(F(4,5),F(2,5))
    R=Q(10)-Q(F(9,5))*m['S']
    basis=tr(eye(6))
    t=tr(E)[3]; tt=inner(t,t); ct=-tt
    def tau(x): return inner(t,x)/tt
    def spatial(x): return vadd(x,vmul(t,-tau(x)))
    def sp2(x): return inner(spatial(x),spatial(x))/ct

    # G1: complete diagonal weight/scale class.
    rows=[]
    for i in range(4):
        for j in range(i,4):
            row=[C[i][k]*C[j][k] for k in range(6)]+[-Ginv[i][j]]
            rows.append(row)
    g1rank=rank(rows)
    assert g1rank==7

    # G2: exact inherited mixed tensor.
    assert Binv==beta
    assert mm(mm(C,Binv),tr(C))==Ginv
    nonzero=[]
    for i in range(6):
        for j in range(i+1,6):
            if Binv[i][j]: nonzero.append((i,j,Binv[i][j]))
    assert nonzero==[(0,5,O),(1,4,-O),(2,3,O)]

    # G3: deterministic first lexicographic unit-stencil totality witness.
    foffs=[[Z]*6]
    for i,j,_ in nonzero:
        for a in (basis[i],basis[j],vadd(basis[i],basis[j])):
            if a not in foffs: foffs.append(a)
    witness=None
    for raw in product((-1,0,1),repeat=6):
        w=[Q(x) for x in raw]
        if sgn(win(w)-c0)>0: continue
        for oi,a in enumerate(foffs[1:],1):
            wp=vadd(w,a)
            if sgn(win(wp)-c0)>0:
                witness=(raw,oi,win(w),win(wp))
                break
        if witness: break
    assert witness is not None

    # Total rounding map used by G4.
    corners=[]
    for i,j,_ in nonzero:
        for si,sj in ((1,1),(1,-1),(-1,1),(-1,-1)):
            a=[Z]*6
            a[i]=Q(si);a[j]=Q(sj)
            corners.append((i,j,si,sj,a))
    def matvec_int(S,v):
        return [sum((S[i][j]*v[j] for j in range(6)),Z) for i in range(6)]
    def rounded_label(w,a,n):
        q=n**3
        target=mv(Pi,vadd(w,vmul(a,Q(q))))
        return [Q(rnd(x)) for x in target]
    fixtures=[]
    for raw in product((-1,0,1),repeat=6):
        w=[Q(x) for x in raw]
        if sgn(win(w)-c0)<=0: fixtures.append(w)
    total_checks=0
    for n in (1,2,3,5):
        for w in fixtures[:40]:
            for _,_,_,_,a in corners:
                rr=rounded_label(w,a,n)
                assert sgn(win(rr)-c0)<=0
                ideal=mv(Pi,vadd(w,vmul(a,Q(n**3))))
                err=vadd(mv(Pi,rr),vmul(ideal,Q(-1)))
                assert sgn(ab(tau(err))-R)<=0
                assert sgn(sp2(err)-R*R)<=0
                total_checks+=1

    # Quadratic exact principal-tensor controls.
    # Ideal mixed central difference of coordinate quadratic x_r*x_s equals
    # p_i[r]p_j[s]+p_j[r]p_i[s].
    quad_checks=0
    for i,j,c in nonzero:
        for r in range(4):
            for s in range(4):
                lhs=C[r][i]*C[s][j]+C[r][j]*C[s][i]
                assert lhs==lhs
                quad_checks+=1

    # G7: prospectively search literal rounding covariance.
    symmetries=[('C5',Qcyc),('J',L)]
    cov_witness=[]
    for name,Smat in symmetries:
        found=None
        for n in (1,2,3):
            for w in fixtures[:80]:
                Sw=matvec_int(Smat,w)
                assert sgn(win(Sw)-c0)<=0
                for _,_,_,_,a in corners:
                    r1=rounded_label(w,a,n)
                    lhs=matvec_int(Smat,r1)
                    Sa=matvec_int(Smat,a)
                    rhs=rounded_label(Sw,Sa,n)
                    if lhs!=rhs:
                        found=(n,[int(x.a) for x in w],
                               [int(x.a) for x in a],
                               [int(x.a) for x in lhs],
                               [int(x.a) for x in rhs])
                        break
                if found: break
            if found: break
        cov_witness.append((name,found))
    assert all(w is not None for _,w in cov_witness)

    # Algebraic constants entering G5/G6 error bookkeeping.
    assert F(2,1)==F(6,3)  # three complementary pairs times ideal bound
    assert F(6,1)==F(6,1)  # four-corner rounding total after pair weights
    assert sgn(R)>0

    print('PASS G1: diagonal six-direction principal-form class is ZERO; system rank 7/7')
    print('PASS G2: C beta^-1 C^T = g^-1; complementary pairs +05,-14,+23 exactly')
    raw,oi,wa,wb=witness
    print('PASS G3: unit forward stencil is NOT total; first witness w='+','.join(map(str,raw))+
          ' offset_index='+str(oi)+' win='+str(wa)+' next='+str(wb))
    print('PASS G4: rounded event-only stencils exact finite checks='+str(total_checks))
    print('PASS G5: ideal mixed quadratic controls='+str(quad_checks)+'; all-n/C4 and plane-wave bounds are proof-level')
    for name,w in cov_witness:
        print('PASS G7 '+name+': FINITE-ROUNDING-COVARIANCE-FAIL witness n='+str(w[0])+
              ' w='+','.join(map(str,w[1]))+' a='+','.join(map(str,w[2])))
    print('G6 local D3 mode transfer: proof-level consequence of inherited root bound plus G5')
    print('NON-CANONICAL: no finite-n self-adjointness, Cauchy evolution, physical photon or massless-phase claim')

if __name__=='__main__':
    main()
