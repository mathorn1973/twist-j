"""Result-exposed E diagnostic, pinned comment 7219574359 of #2109.
Half-period phase retention in actual full fields; no chosen time/reader.
"""
import verify as V
from itertools import product
H=V.H
Z,O,J,P=V.Z,V.O,V.J,V.P
add,sub,mul,h,scale,neg=V.add,V.sub,V.mul,V.h,V.scale,V.neg
def seed(b,k):
    F=[]
    for x,y in product(range(8),range(4)):
        d=P[k] if x==y==0 else scale((-1)**y,O)
        F.extend((d,neg(d),Z,scale(2*(-1)**(x+b*y),J)))
    return tuple(F)
def account(F):
    return (H.ring_sum(v for n,v in enumerate(F) if n%4<2),
            H.ring_sum(v for n,v in enumerate(F) if n%4>=2),
            H.ring_sum(h(v) for v in F))
def half(z):
    assert H.even(z)
    return H.half(z)
def pair(F,i):
    a,b=F[i:i+2]
    # Avoid pretending arbitrary local pair half-differences are integral.
    # Report doubled center/difference in O, then use exact comparison.
    return add(a,b),sub(a,b)
for b,t in ((0,120),(1,40)):
    Fs=[]
    for k in range(5):
        F=seed(b,k);bit=0;ac=account(F)
        for n in range(t):
            G=H.transport(F,4,bit)
            N,_=H.collide(G,4)
            back,_=H.collide(N,4)
            assert H.transport(back,4,bit,backward=True)==F
            assert account(G)==account(N)==ac
            F=N;bit^=1
        Fs.append(F)
    assert len(set(Fs))==5
    source=[F[:2] for F in Fs]
    print('E SOURCE',b,t,source)
    varying=[i for i in range(len(Fs[0])) if len({F[i] for F in Fs})>1]
    sites=sorted({i//4 for i in varying})
    vpairs=sorted({i//2 for i in varying})
    injective=[divmod(c,4) for c in range(32) if len({F[4*c:4*c+4] for F in Fs})==5]
    print('E SUPPORT',b,'SLOTS',len(varying),'SITES',len(sites),'PAIRS',len(vpairs),'LOCAL_INJECTIVE',injective)
    matches=[]
    for c,role in product(range(32),range(2)):
        i=4*c+2*role
        values=[pair(F,i) for F in Fs]
        if len(set(values))==1:continue
        centers=[u for u,v in values]
        diffs=[v for u,v in values]
        print('E PAIR',b,divmod(c,4),role,'CENTERS',centers,'DIFFS',diffs,'INJECTIVE',int(len(set(values))==5))
        if len(set(centers))==1 and diffs[0]!=Z:
            for e in range(1,5):
                if all(diffs[k]==mul(diffs[0],P[e*k%5]) for k in range(5)):
                    matches.append((c,role,e,diffs[0]))
    strong=[m for m in matches if m[0]!=0 and vpairs==[2*m[0]+m[1]] and all(v==(O,neg(O)) for v in source)]
    print('E LOCAL_PHASE_RECORDS',b,[(divmod(c,4),r,e,d) for c,r,e,d in matches])
    print('E STRONG_RELOCATION',b,[(divmod(c,4),r,e,d) for c,r,e,d in strong])
print('DONE exact five-input half-period record diagnostic')
