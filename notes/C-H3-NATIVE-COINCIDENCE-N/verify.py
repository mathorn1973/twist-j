"""NON-CANONICAL native coincidence audit, frozen issue #2113."""
import hashlib,sys,importlib.util
from pathlib import Path
from itertools import product
from functools import cache
from fractions import Fraction
from collections import Counter

source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
spec=importlib.util.spec_from_file_location('h3_source',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H
spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,R,J,JI=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV
P=H.J_POWERS
add,sub,mul,sc,h=H.add,H.sub,cache(H.mul),H.scale,H.h
neg=lambda x:sc(-1,x)
m=8
A=sc(Fraction(1,2),J)
B=sc(Fraction(1,2),sub(O,R))
Rwrite=sc(m,sub(mul(R,R),R))
other=sc(-m,R)
idx=lambda x,y,q: H.index(8,x,y,q)
def rsum(a):return tuple(map(sum,zip(*a)))
def acc(F):
    return rsum(z for i,z in enumerate(F) if i%4<2),rsum(z for i,z in enumerate(F) if i%4>=2),rsum(h(z) for z in F)
def seed(r,u,k=1,l=2,v=3,w=4):
    marks={(0,-2*r%8):P[k],(0,(4-2*r)%8):P[l],
           (7,-2*u%8):P[v],(7,(4-2*u)%8):P[w]}
    G=[]
    for x,y in product(range(8),repeat=2):
        d=marks.get((x,y),sc((-1)**y,O))
        clk=Z;corr=sc(2*(-1)**(x+y),J)
        if y%2==0:
            if x==0:d=add(sc(m,O),sub(d,P[1]))
            if x==7:d=add(sc(m,O),sub(d,P[3]));clk=sc(4*m,O)
            if x in (0,1):corr=sc(-2*m,J)
            if x in (6,7):corr=sc(m,sub(sc(4,O),sc(2,J)))
        else:
            if x in (0,7):d=O;clk=O
            if x in (0,1,6,7):corr=Z
        G.extend((d,neg(d),clk,corr))
    return tuple(G)
def cell(F,x,y):
    i=idx(x,y,0);return F[i:i+4]
def step(F,bit,ac):
    G=H.transport(F,8,bit)
    N,events=H.collide(G,8)
    back,_=H.collide(N,8)
    assert back==G and H.transport(back,8,bit,backward=True)==F
    assert acc(G)==acc(N)==ac
    return G,N,{(x,y):t for x,y,t in events}
def actual_half(c):
    return H.half(sub(c[2],c[3]))
def raw(c):
    return ';'.join(','.join(map(str,z)) for z in c)
def mask(F):return tuple(int(F[idx(0,y,2)]==Rwrite) for y in range(0,8,2))
def run(F,n):
    ac=acc(F);cut=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac)
        cut.append(F);mids.append(G);tags.append(E)
    return cut,mids,tags,ac
def bits_at(r,u,y):
    return int(y==-2*r%8),int(y==-2*u%8)
def local_type(r,u,y):
    p=P[1] if y==-2*r%8 else P[2] if y==(4-2*r)%8 else O
    q=P[3] if y==-2*u%8 else P[4] if y==(4-2*u)%8 else O
    return p,q
assert Rwrite!=Z and Rwrite!=other and other!=Z
# Prove the exact norm tests on all local input types.
for p,q in product((O,P[1],P[2]),(O,P[3],P[4])):
    a=int(p==P[1]);b=int(q==P[3])
    dA=add(sc(m,O),sub(p,P[1]))
    dB=add(sc(m,O),sub(q,P[3]))
    assert (h(dA)==sc(m*m,O))==bool(a)
    assert (h(dB)==sc(m*m,O))==bool(b)
    assert h(dA)!=sc(m*m,mul(H.T,H.T))
    assert h(dB)!=sc(m*m,mul(H.T,H.T))
    d=mul(J,dA) if a else dA
    F=sc(m,mul(R,add(O,add(sc(Fraction(1-a,2),add(O,A)),sc(Fraction(1-b,2),B)))))
    assert all(t.denominator==1 if isinstance(t,Fraction) else True for t in F)
    assert h(F)!=mul(H.T,h(d))
    assert (h(d)==mul(H.T,h(F)))==bool(a and b)
    print('A NORMS',P.index(p),P.index(q),'MATTER',raw((h(d),)),'RAD',raw((h(F),)),'TAG',2*int(a and b))
cases=tuple(product(range(4),repeat=2));hs={};qvals=set()
for r,u in cases:
    F0=seed(r,u);hist=run(F0,160);cuts,mids,tags,ac=hist;hs[r,u]=hist
    Q=H.scalar_account(ac[2]);qvals.add(Q)
    for y in range(0,8,2):
        a,b=bits_at(r,u,y)
        for x,e in ((0,a),(7,b)):
            assert cell(mids[1],x,y)==cell(F0,x,y)
            assert tags[1].get((x,y),0)==e
            assert actual_half(cell(cuts[1],x,y))==sc(m,add(O,sc(1-e,R)))
            assert cell(mids[2],x,y)[:3]==cell(cuts[1],x,y)[:3]
        for x in (0,7):
            assert H.even(sub(cell(cuts[1],0,y)[3],cell(cuts[1],7,y)[3]))
            for yy in (y+1,):
                assert cell(cuts[1],x,yy)==cell(cuts[2],x,yy)==(O,neg(O),O,Z)
        F=sc(m,mul(R,add(O,add(sc(Fraction(1-a,2),add(O,A)),sc(Fraction(1-b,2),B)))))
        assert actual_half(cell(mids[2],0,y))==F
        assert tags[2].get((0,y),0)==2*(a*b)
        assert cuts[2][idx(0,y,2)]==(Rwrite if a*b else other if a else Z)
        print('A WORD',r,u,y,a,b,'PRE1',raw(cell(mids[1],0,y)),raw(cell(mids[1],7,y)),
              'FULL1',raw(cell(cuts[1],0,y)),raw(cell(cuts[1],7,y)),
              'PRE2',raw(cell(mids[2],0,y)),'FULL2',raw(cell(cuts[2],0,y)))
    actual=mask(cuts[2])
    expected=tuple(int(r==u and y==-2*r%8) for y in range(0,8,2))
    assert actual==expected
    print('A CASE',r,u,'MASK',actual,'Q',Q,'H',ac[2])
assert len(qvals)==1
print('A PASS',len(hs),'POSITIVE',sum(sum(mask(hs[p][0][2])) for p in cases),'Q',next(iter(qvals)),'R',Rwrite,'OTHER',other)
# The stronger recurrence and repetition tests are independent of gate A.
for n in range(1,5):
    t=40*n
    whole=sum(hs[r,u][0][t]==seed((r+n)%4,(u+n)%4) for r,u in cases)
    print('B STROKE',t,'COMPLETE_MATCHES',whole)
    if n<4:
        ok=sum(mask(hs[r,u][0][t+2])==tuple(int(r==u and y==-2*(r+n)%8) for y in range(0,8,2)) for r,u in cases)
        print('B REPEAT',t+2,'MASK_MATCHES',ok)
records=[]
for t,x,y in product(range(2,161),range(8),range(8)):
    pos={hs[r,u][0][t][idx(x,y,2)] for r,u in cases if r==u}
    negs={hs[r,u][0][t][idx(x,y,2)] for r,u in cases if r!=u}
    if len(pos)==len(negs)==1 and pos!=negs:
        records.append((t,x,y,next(iter(pos)),next(iter(negs))))
print('B FIXED_BINARY_RECORDS',len(records))
if records:
    t,x,y,v,w=records[0]
    print('B FIRST',t,x,y,'POS',v,'NEG',w)
    if t<160:
        mid_hold=all(hs[r,u][1][t+1][idx(x,y,2)]==(v if r==u else w) for r,u in cases)
        full_hold=all(hs[r,u][0][t+1][idx(x,y,2)]==(v if r==u else w) for r,u in cases)
        print('B FIRST_HOLD_NEXT',int(mid_hold),int(full_hold))
controls=((0,0,3,4),(1,1,3,4),(2,2,3,4),(1,2,0,0),(1,2,3,3),(1,2,4,4))
for k,l,v,w in controls:
    out=Counter()
    for r,u in cases:
        cut=run(seed(r,u,k,l,v,w),2)[0]
        out[sum(mask(cut[2]))]+=1
    print('C CONTROL',k,l,v,w,'R_COUNTS',sorted(out.items()))
F=run(seed(0,0,0,0,0,0),2)[0][2]
print('C EMPTY',mask(F))
print('DONE exact native two-tick coincidence and recurrence boundary')
