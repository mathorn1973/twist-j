"""Result-exposed F diagnostic declared in issue #2109 comment 7219598326.
Complete-stock equality, fixed two-row translation; no postselected reader.
"""
import verify as V
from itertools import product
from functools import cache
H=V.H
Z,O,J,P=V.Z,V.O,V.J,V.P
add,sub,h,scale,neg=V.add,V.sub,V.h,V.scale,V.neg
# Transparent memoization of the pinned, pure local primitives.
H.transport_pair=cache(H.transport_pair)
H.collision=cache(H.collision)
def seed(ny,b,k,l=0):
    F=[]
    for x,y in product(range(8),range(ny)):
        d=scale((-1)**y,O)
        if x==0 and y==0:d=P[k]
        if x==0 and y==4 and ny==8:d=P[l]
        F.extend((d,neg(d),Z,scale(2*(-1)**(x+b*y),J)))
    return tuple(F)
def shift(F,ny,a):
    return tuple(F[H.index(ny,x,(y-a)%ny,r)]
                 for x,y,r in product(range(8),range(ny),range(4)))
def rsum(seq):return tuple(map(sum,zip(*seq)))
def account(F):
    return (rsum(v for n,v in enumerate(F) if n%4<2),
            rsum(v for n,v in enumerate(F) if n%4>=2),
            rsum(h(v) for v in F))
def step(F,ny,bit,ac):
    G=H.transport(F,ny,bit)
    N,_=H.collide(G,ny)
    back,_=H.collide(N,ny)
    assert back==G and H.transport(back,ny,bit,backward=True)==F
    assert account(G)==account(N)==ac
    return N,bit^1
def evolve(F,ny,n):
    ac=account(F);bit=0
    for _ in range(n):F,bit=step(F,ny,bit,ac)
    return F,bit
def four_strokes(ny,b,k,l,s,a):
    F0=seed(ny,b,k,l);F=F0;bit=0;ac=account(F)
    states=[F0]
    for t in range(1,4*s+1):
        F,bit=step(F,ny,bit,ac)
        if t%s==0:
            assert bit==0 and F==shift(F0,ny,(t//s)*a)
            states.append(F)
    assert F==F0 and bit==0
    return len(set(states[:-1]))

for b,s in ((0,120),(1,40)):
    result=[]
    for k in range(5):
        F0=seed(4,b,k)
        F,bit=evolve(F0,4,s)
        result.append(int(bit==0 and F==shift(F0,4,2)))
    print('F SHUTTLE',b,s,'COMPLETE_TRANSLATION',result)

wins=[]
for b,s0 in ((0,120),(1,40)):
    common=None
    for k in range(5):
        F0=seed(8,b,k);F=F0;bit=0;ac=account(F)
        targets={a:shift(F0,8,a) for a in (2,-2)}
        matches=[];period=0;seen=[]
        for t in range(1,257):
            F,bit=step(F,8,bit,ac)
            if bit==0:
                for a,target in targets.items():
                    if F==target:matches.append((t,a))
                if not period and F==F0:period=t
        print('F HEIGHT8',b,k,'PERIOD',period,'MATCHES',matches)
        common=set(matches) if common is None else common.intersection(matches)
    common=sorted(common)
    print('F COMMON',b,common)
    for s,a in common:
        counts=[four_strokes(8,b,k,0,s,a) for k in range(5)]
        assert counts==[1,4,4,4,4]
        wins.append((b,s,a))
        print('F FOUR_STROKES',b,s,a,counts)
    # Both orientations, declared stride and any common single-marker witness.
    strides=sorted({s0}|{s for s,a in common})
    for s in strides:
        fam={a:[] for a in (2,-2)}
        for k,l in product(range(5),repeat=2):
            F0=seed(8,b,k,l);F,bit=evolve(F0,8,s)
            for a in fam:
                if bit==0 and F==shift(F0,8,a):fam[a].append((k,l))
        for a,match in fam.items():
            print('F TWO_PHASE',b,s,a,'MATCHES',match)
            if len(match)==25:
                counts=[four_strokes(8,b,k,l,s,a) for k,l in product(range(5),repeat=2)]
                assert all(n in (1,2,4) for n in counts)
                print('F TWO_PHASE_FOUR',b,s,a,'ORBIT_SIZES',counts)
print('F WINS',wins)
print('DONE exact height-8 prolongation')
