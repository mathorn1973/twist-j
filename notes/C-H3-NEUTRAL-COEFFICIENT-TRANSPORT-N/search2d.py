"""NON-CANONICAL exact 2D neutral-defect census, frozen issue #2109."""
import verify as V
from itertools import product
from collections import Counter
import hashlib

H=V.H
Z,O,J,JI=V.Z,V.O,V.J,V.JI
P=V.P
add,sub,mul,h,scale,neg=V.add,V.sub,V.mul,V.h,V.scale,V.neg
C,B=V.C,V.B
NX,NY=8,4
N=NX*NY
MAX=256
idx=lambda x,y,r:4*(x*NY+y)+r
edges={}
for bit in (0,1):
    for axis in (0,1):
        a=[]
        rails=(3,) if axis==1 else (0,1,2)
        for rail in rails:
            size,breadth=(NX,NY) if rail==3 else (NY,NX)
            for u,v in product(range(bit,size,2),range(breadth)):
                w=(u+1)%size
                a.append((idx(u,v,rail),idx(w,v,rail)) if axis==1 else
                         (idx(v,u,rail),idx(v,w,rail)))
        edges[bit,axis]=tuple(a)
def transport(F,bit,back=False):
    G=list(F); moves=[0,0]
    for axis in (0,1):
        for i,k in edges[bit,axis]:
            a,b=C(F[i],F[k],back)
            G[i],G[k]=a,b
            moves[axis]+=(a!=F[i] or b!=F[k])
    return tuple(G),tuple(moves)
def collision(F):
    G=[]; tags=[0,0]
    for i in range(0,len(F),4):
        out,t=B(F[i:i+4])
        G.extend(out)
        if t:tags[t-1]+=1
    return tuple(G),tuple(tags)
def rsum(seq):
    return tuple(map(sum,zip(*seq)))
def account(F):
    m=rsum(z for i,z in enumerate(F) if i%4<2)
    f=rsum(z for i,z in enumerate(F) if i%4>=2)
    H0=rsum(h(z) for z in F)
    return m,f,H0,H.scalar_account(H0)
def seed(b,kind,delta):
    G=[]
    for x,y in product(range(NX),range(NY)):
        d=scale((-1)**y,O)
        f=scale(2*(-1)**(x+b*y),J)
        if (x,y)==(0,0):
            if kind==0:d=add(d,delta); g=Z
            else:g=delta; f=sub(f,delta)
        else:g=Z
        G.extend((d,neg(d),g,f))
    return tuple(G)
def shift(F,a):
    return tuple(F[idx((x-a)%NX,y,r)] for x,y,r in product(range(NX),range(NY),range(4)))
def full_witness(initial,b,kind,delta,s,a):
    F=initial; bit=0; fixed=account(F)
    q=next(i for i,v in enumerate(delta) if v)
    bg=seed(b,kind,Z)
    for t in range(1,4*s+1):
        G=H.transport(F,NY,bit)
        N0,ev=H.collide(G,NY)
        rev,_=H.collide(N0,NY)
        assert H.transport(rev,NY,bit,backward=True)==F
        assert account(N0)==account(G)==fixed
        F=N0; bit^=1
        if t%s==0:
            k=t//s
            assert F==shift(initial,k*a) and bit==0
            read=[F[idx(a*r%NX,0,0 if kind==0 else 2)][q]-bg[idx(a*r%NX,0,0 if kind==0 else 2)][q] for r in range(4)]
            assert read==[delta[q] if r==k%4 else 0 for r in range(4)]
    assert F==initial and bit==0
deltas=sorted({scale(sign*m,mul(mul(P[l],{-1:JI,0:O,1:J}[e]),sub(O,P[k])))
               for sign,m,l,e,k in product((-1,1),(1,2),range(5),(-1,0,1),range(1,5))}-{Z})
assert len(deltas)==80
print('C DELTAS',len(deltas),'PREPARATIONS',4*len(deltas),'STRIDES',MAX//2)
periods=Counter();category=Counter();wins=[];ticks=0;active_both=0
for b,kind in product(range(2),repeat=2):
    cat=Counter();cboth=0;cticks=0;cwins=0
    for i,delta in enumerate(deltas):
        F0=seed(b,kind,delta); F=F0; bit=0
        acc0=account(F)
        assert sum(delta)%5==0
        # The local pair sums are unchanged by this neutral perturbation.
        assert all(add(F0[i],F0[i+1])==add(seed(b,kind,Z)[i],seed(b,kind,Z)[i+1])
                   for i in range(0,len(F0),2))
        assert len({shift(F0,2*k) for k in range(4)})==4
        targets={a:shift(F0,a) for a in (2,6)}
        moves=[0,0];tags=[0,0];period=0;matches=[]
        for t in range(1,MAX+1):
            G,c=transport(F,bit)
            if t==1:assert G==H.transport(F,NY,bit)
            N0,Btags=collision(G)
            if t==1:
                lit,ev=H.collide(G,NY)
                assert lit==N0 and tuple(sum(tag==k for x,y,tag in ev) for k in (1,2))==Btags
            assert account(G)==account(N0)==acc0
            rev,_=collision(N0)
            assert rev==G and transport(rev,bit,True)[0]==F
            F=N0;bit^=1
            cticks+=1
            for k in range(2):moves[k]+=c[k];tags[k]+=Btags[k]
            if bit==0:
                for a,target in targets.items():
                    if F==target:matches.append((t,a))
                if F==F0:
                    period=t;break
        for t,a in matches:
            strides=range(t,MAX+1,period) if period else (t,)
            for s in strides:
                full_witness(F0,b,kind,delta,s,a)
                wins.append((b,kind,i,s,a))
                cwins+=1
        cat[period]+=1
        both=int(all(moves)); cboth+=both
        print('C CASE',b,kind,i,period,moves[0],moves[1],tags[0],tags[1],len(matches),acc0[3])
    periods.update(cat);ticks+=cticks;active_both+=cboth
    print('C GROUP',b,kind,'PERIODS',sorted(cat.items()),'BOTH_AXES',cboth,'TICKS',cticks,'WINS',cwins)
print('C PERIODS',sorted(periods.items()))
print('C TICKS',ticks,'BOTH_AXES',active_both,'WINS',len(wins))
for w in wins:print('C WIN',w)
print('DONE exact native 2D census; period 0 means no return by 256')
