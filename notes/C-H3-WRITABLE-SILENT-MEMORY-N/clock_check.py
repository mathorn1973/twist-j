"""NON-CANONICAL #2129 C sample audit of the actual first correction histories."""
from pathlib import Path
import runpy
from itertools import product
from fractions import Fraction as Q
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
step,account,ix,cols=map(V.get,('step','account','ix','cols'))
eta=sub(O,R);bi=H.inverse(sc(Q(1,2),eta))
def scale(z):
    p=mul(eta,z);assert all(Q(v).denominator==1 for v in p);return tuple(map(int,p))
def rot(pair,n,back=False):
    for _ in range(n%5):pair=H.transport_pair(*pair,back)
    return pair
def rq(a,b,back=False):
    dif=sub(a,b)
    assert all(Q(v).denominator%2 for v in dif)
    if any(Q(v).numerator%2 for v in dif):return a,b
    u=mul(P[3] if back else R,dif)
    return sc(Q(1,2),add(add(a,b),u)),sc(Q(1,2),sub(add(a,b),u))
def rrot(pair,n,back=False):
    for _ in range(n%5):pair=rq(*pair,back)
    return pair
def f_for(d,tag):return mul(d,H.inverse(sub(O,JI if tag==1 else J)))
def dm(f,tag):return mul(JI if tag==1 else J,f)
def ex(tag):return J if tag==1 else JI
m=sub(sc(2,O),R);gs=sc(2,mul(J,m));a=sc(-3,eta)
b=add(add(mul(m,R),mul(J,a)),sc(12,J))
stock=(Z,Z,Z,b,b,b,add(mul(m,R),sc(2,a)))
def base(p):
    F=[]
    for x,y in product(range(8),range(2)):
        d=(P[p] if y==0 else sc(3,P[1])) if x==0 else JI if x==6 else Z
        g=gs if x==0 else (6,-2,12,1) if x==6 else Z
        c=(Z if x==0 else stock[x-1]) if y==0 else gs
        F.extend(cols(d,g,c))
    return tuple(F)
r=(-2,-2,9,-5);c=(7,-8,12,-2);delta=(12,0,6,6);delta5=(0,6,0,0)
allowed=tuple(scale(add(r,sc(2,f_for(delta,tag)))) for tag in (1,2))
for a,b in product((1,2),repeat=2):
    f1,f2=f_for(delta,a),f_for(delta5,b)
    d1,d2=dm(f1,a),dm(f2,b);d1p=mul(ex(a),d1)
    g1=add(r,sc(2,f1));g1p=sub(g1,delta);g2=add(c,sc(2,f2))
    dr=add(d1p,mul(bi,sub(d2,d1p)));gr=add(g1p,mul(bi,sub(g2,g1p)))
    dd=tuple(map(scale,rrot((d1,dr),113,True)))
    gg=tuple(map(scale,rrot((g1,gr),113,True)))
    ready=tuple(map(scale,(g1,gr)))
    assert rot(gg,113)==ready
    out=[]
    for p in range(5):
        F=list(map(scale,base(p)))
        for y in range(2):
            i=ix(5,y,0);F[i:i+3]=(dd[y],neg(dd[y]),gg[y])
        F0=F=tuple(F);ac=account(F)
        for t in range(1,115):
            G,F,ev=step(F,(t-1)%2,ac)
            expected=(((5,0,a),) if p==1 and t==113 else ((5,0,b),) if p==1 and t==114 else ())
            assert tuple(e for e in ev if e[0]==5)==expected
            if t==113:assert (G[ix(5,0,2)],G[ix(5,1,2)])==ready
            if t==114 and p==1:
                assert G[ix(5,0,2)]==scale(g2)
        assert F[:8]==F0[:8] and F[48:56]==F0[48:56]
        assert F[ix(5,0,3)]==F0[ix(5,0,3)]
        if p==0:
            neg_cut=(F[ix(5,0,2)],F[ix(5,1,2)])
            assert neg_cut==rot(gg,114)
            second=rot(neg_cut,113)[0]
            assert second==rot(ready,114)[0] and second not in allowed
        out.append(F)
    assert len({tuple(F[ix(x,y,3)] for x,y in product(range(7),range(2))) for F in out})==1
    print('CLOCK_SAMPLE',a,b,'FIRST_TRAJECTORIES',5,'Q',H.scalar_account(ac[2]),'NEG114_CLK',neg_cut,'CONDITIONAL_SECOND227_CLK',second,'MATCH',(0,0))
print('PASS literal four tag-pair first-write samples and conditional second readiness')
