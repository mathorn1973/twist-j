"""Result-exposed D diagnostic preregistered in issue #2109 comment 7219555522.
Exact full-preparation comparisons; no postselected reader or stride.
"""
import verify as V
from itertools import product
H=V.H
Z,O,J=V.Z,V.O,V.J
P=V.P
add,sub,h,scale,neg=V.add,V.sub,V.h,V.scale,V.neg
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
wins=[]
for b,period in ((0,240),(1,80)):
    E={k:seed(b,k) for k in range(1,5)}
    results={}
    for k in range(1,5):
        F=E[k];bit=0;ac=account(F);hits=[(0,k)];quarter=[F[0]]
        for t in range(1,period+1):
            C=H.transport(F,4,bit)
            N,_=H.collide(C,4)
            back,_=H.collide(N,4)
            assert H.transport(back,4,bit,backward=True)==F
            assert account(C)==account(N)==ac
            F=N;bit^=1
            if bit==0:
                for l,E0 in E.items():
                    if F==E0:hits.append((t,l))
            assert all(F[i]==neg(F[i+1]) for i in range(0,len(F),4))
            if t%(period//4)==0:
                quarter.append(F[0])
        assert F==E[k] and bit==0
        results[k]=hits
        print('D CASE',b,k,'PERIOD',period,'HITS',hits)
        print('D PORT',b,k,quarter)
    for s in (period//4,3*period//4):
        ok=all((s,2*k%5) in results[k] for k in range(1,5))
        if ok:wins.append((b,s))
        print('D STRIDE',b,s,'MATCHES',sum((s,2*k%5) in results[k] for k in range(1,5)),'WIN',int(ok))
print('D WINS',wins)
print('DONE exact fixed-port phase diagnostic')
