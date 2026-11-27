"""Reproduction of the eight result-exposed closed periods in frozen gate C.
Not a new target or a new decoder. Use complete pinned H3 source.
"""
import verify as V
from itertools import product
import hashlib

H=V.H
Z,O,J,JI=V.Z,V.O,V.J,V.JI
P=V.P
add,sub,mul,h,scale,neg=V.add,V.sub,V.mul,V.h,V.scale,V.neg
deltas=sorted({scale(sign*m,mul(mul(P[l],{-1:JI,0:O,1:J}[e]),sub(O,P[k])))
               for sign,m,l,e,k in product((-1,1),(1,2),range(5),(-1,0,1),range(1,5))}-{Z})
def seed(b,delta):
    F=[]
    for x,y in product(range(8),range(4)):
        d=scale((-1)**y,O)
        if x==y==0:d=add(d,delta)
        F.extend((d,neg(d),Z,scale(2*(-1)**(x+b*y),J)))
    return tuple(F)
def account(F):
    return (H.ring_sum(v for n,v in enumerate(F) if n%4<2),
            H.ring_sum(v for n,v in enumerate(F) if n%4>=2),
            H.ring_sum(h(v) for v in F))
def sha(F,bit):
    t=str(bit)+';'+';'.join(','.join(map(str,z)) for z in F)
    return hashlib.sha256(t.encode()).hexdigest()
for b,period in ((0,240),(1,80)):
    for i in (12,26,27,29):
        delta=deltas[i]; F0=seed(b,delta);F=F0;bit=0;ac=account(F)
        assert H.scalar_account(ac[2])==512
        cuts=[sha(F,bit)]
        for t in range(1,period+1):
            C=H.transport(F,4,bit)
            N,_=H.collide(C,4)
            back,_=H.collide(N,4)
            assert H.transport(back,4,bit,backward=True)==F
            assert account(C)==account(N)==ac
            F=N;bit^=1
            if t<period:assert (F,bit)!=(F0,0)
            if t%(period//4)==0:cuts.append(sha(F,bit))
        assert F==F0 and bit==0 and cuts[-1]==cuts[0]
        assert len(set(cuts[:-1]))==4
        print('CLOSED',b,i,delta,'PERIOD',period,'STRIDE',period//4,'Q',512,'H',ac[2])
        print('QUARTER_DIGESTS',*cuts)
print('PASS 8 complete native minimal periods, 4 distinct quarter cuts each')
