"""Result-exposed G diagnostic, pinned comment 7219617099 of #2109.
Exact autonomous two-phase transport; not raw Galois or single-marker motor.
"""
import verify as V
from itertools import product
from functools import cache
import hashlib
H=V.H
Z,O,J,P=V.Z,V.O,V.J,V.P
add,sub,h,scale,neg=V.add,V.sub,V.h,V.scale,V.neg
H.transport_pair=cache(H.transport_pair)
H.collision=cache(H.collision)
NY=8
def seed(b,k,l):
    F=[]
    for x,y in product(range(8),range(NY)):
        d=scale((-1)**y,O)
        if x==0 and y==0:d=P[k]
        if x==0 and y==4:d=P[l]
        F.extend((d,neg(d),Z,scale(2*(-1)**(x+b*y),J)))
    return tuple(F)
def shift(F,a):
    return tuple(F[H.index(NY,x,(y-a)%NY,r)]
                 for x,y,r in product(range(8),range(NY),range(4)))
def rsum(seq):return tuple(map(sum,zip(*seq)))
def account(F):
    return (rsum(v for n,v in enumerate(F) if n%4<2),
            rsum(v for n,v in enumerate(F) if n%4>=2),
            rsum(h(v) for v in F))
def step(F,bit,ac):
    G=H.transport(F,NY,bit)
    N,_=H.collide(G,NY)
    back,_=H.collide(N,NY)
    assert back==G and H.transport(back,NY,bit,backward=True)==F
    assert account(G)==account(N)==ac
    return N,bit^1
def digest(F,bit):
    t=str(bit)+';'+';'.join(','.join(map(str,z)) for z in F)
    return hashlib.sha256(t.encode()).hexdigest()
def values(F):
    out=[]
    for y in (0,2,4,6):
        i=H.index(NY,0,y,0)
        d=F[i]
        assert F[i+1]==neg(d)
        out.append(P.index(d))
    return tuple(out)
wins=0
for b,s,a in ((0,120,2),(1,40,-2)):
    hist={2:0,4:0}; periods={}; bg=seed(b,0,0)
    for k,l in product(range(1,5),repeat=2):
        F0=seed(b,k,l); F=F0; bit=0; ac=account(F)
        assert H.scalar_account(ac[2])==1024
        states=[F0]; vals=[values(F0)]; ds=[digest(F0,bit)]; first=0
        for t in range(1,4*s+1):
            F,bit=step(F,bit,ac)
            if not first and F==F0 and bit==0:first=t
            if t%s==0:
                r=t//s
                assert F==shift(F0,r*a) and bit==0
                expected=list(bg)
                for y,p in ((r*a%8,k),((4+r*a)%8,l)):
                    i=H.index(NY,0,y,0)
                    expected[i]=P[p];expected[i+1]=neg(P[p])
                assert F==tuple(expected)
                states.append(F);vals.append(values(F));ds.append(digest(F,bit))
        assert F==F0 and bit==0 and states[-1]==states[0]
        n=len(set(states[:-1]))
        assert n==(2 if k==l else 4)
        assert all(states[i]!=F0 for i in range(1,n))
        assert states[n]==F0
        hist[n]+=1;periods[first]=periods.get(first,0)+1
        wins+=1
        print('G CASE',b,k,l,'STRIDE',s,'SHIFT',a,'PERIOD',first,'STROBE_ORDER',n,'Q',1024)
        print('G PORTS',b,k,l,*vals)
        print('G DIGESTS',b,k,l,*ds)
    assert hist=={2:4,4:12}
    print('G GROUP',b,'STROBE_ORDERS',sorted(hist.items()),'PERIODS',sorted(periods.items()))
assert wins==32
print('G PASS 32/32 pairs; 24 exact order-four orbits, 8 exact order-two controls')
print('DONE exact two-phase four-stroke native transport')
