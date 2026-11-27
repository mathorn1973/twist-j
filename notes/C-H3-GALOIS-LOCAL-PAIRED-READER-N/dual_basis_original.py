"""NON-CANONICAL E diagnostic, frozen issue #2111 comment 7219949923."""
import verify as V
from itertools import product
from collections import Counter
H=V.H
Z,O,J,P=V.Z,V.O,V.J,V.P
K,W,mul,add,sub,scale=V.K,V.W,V.mul,V.add,V.sub,V.scale
rsum,idx=V.rsum,V.idx
a=-2
def fields(r,u,k=1,l=2,m=3,n=4):
    return V.seed(1,{(0,a*r%8):P[k],(0,(4+a*r)%8):P[l],
                   (1,a*u%8):P[m],(1,(4+a*u)%8):P[n]})
X=[P[2]];Y=[V.neg(P[2])]
for _ in range(4):X.append(K(X[-1]));Y.append(W(Y[-1]))
assert X[4]==X[0] and Y[4]==Y[0]
X,Y=tuple(X[:4]),tuple(Y[:4])
assert all(K(K(K(K(x))))==x and W(W(W(W(x))))==x for x in P)
assert all(mul(K(x),W(y))[3]==mul(x,y)[3] for x,y in product(P[:4],repeat=2))
dets=tuple(V.det(tuple(zip(*tar))) for tar in (X,Y))
assert all(abs(d)==1 for d in dets)
pairing=tuple(tuple(mul(x,y)[3] for y in Y) for x in X)
assert pairing==tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
print('E1 X',X,'DET',dets[0])
print('E1 Y',Y,'DET',dets[1])
print('E1 PAIRING',pairing)
def fast(track,z,w):
    if track==0:
        q0=z[1]-z[0];q2=-z[0];q1=q0-w[1];q3=z[2]+q2-q1
    else:
        q0=z[3]-z[0];q2=z[1]-z[0];q1=q0-w[0];q3=-z[0]-q1
    return q0,q1,q2,q3
def slow(track,z,w):
    if track==0:return z[1],w[2],z[2],w[1]
    aa=lambda z:z[3]-z[1];bb=lambda z:-z[1]
    return aa(z),bb(w),bb(z),aa(w)
def onehot(k):return tuple(int(i==k) for i in range(4))
def read_fast(track,cuts,t):
    off=2+2*track
    return fast(track,cuts[t+off][idx(track,0,0)],cuts[t+off+1][idx(track,0,0)])
def read_slow(track,F):
    return slow(track,F[idx(track,0,0)],F[idx(track,2,0)])
def accepted(v):return v in tuple(onehot(k) for k in range(4))
def decode(v,basis):return rsum(scale(q,z) for q,z in zip(v,basis))
def coincide(F):
    return sum(int(F[idx(0,y,0)]==P[1])*int(F[idx(1,y,0)]==P[3]) for y in (0,2,4,6))
cases=tuple(product(range(4),repeat=2))
hs={};invariants=Counter();count=0;first=set()
for r,u in cases:
    Hs=V.history(fields(r,u),165)
    hs[r,u]=Hs
    cuts,mids,tags,ac=Hs
    assert H.scalar_account(ac[2])==1024
    prev=None
    for n in range(5):
        t=n*40
        F=cuts[t]
        rr,uu=(r+n)%4,(u+n)%4
        assert F==fields(rr,uu)
        a,b=read_fast(0,cuts,t),read_fast(1,cuts,t)
        assert a==onehot(rr)==read_slow(0,F)
        assert b==onehot(uu)==read_slow(1,F)
        xx,yy=decode(a,X),decode(b,Y)
        p=mul(xx,yy)[3]
        assert p==int(rr==uu)==coincide(F)
        assert xx==X[rr] and yy==Y[uu]
        if n==0:
            invariants[p]+=1;first.add((xx,yy))
        else:
            assert xx==K(prev[0]) and yy==W(prev[1]) and p==prev[2]
        prev=xx,yy,p;count+=1
    assert cuts[160]==cuts[0]
    assert cuts[161:166]==cuts[1:6]
    print('E2 CASE',r,u,'ELL',prev[2],'Q',1024)
assert len(first)==16 and invariants=={0:12,1:4} and count==80
print('E2 PAIRS',len(first),'WINDOWS',count,'ELL_HISTOGRAM',sorted(invariants.items()))
controls=((0,0,3,4),(1,1,3,4),(2,2,3,4),(1,2,0,0),(1,2,3,3),(1,2,4,4))
for k,l,m,n in controls:
    nfast=nslow=0
    for r,u in cases:
        cuts=V.history(fields(r,u,k,l,m,n),5)[0]
        nfast+=all(accepted(read_fast(t,cuts,0)) for t in (0,1))
        nslow+=all(accepted(read_slow(t,cuts[0])) for t in (0,1))
    print('E2 CONTROL',k,l,m,n,'FAST_ACCEPTED',nfast,'SLOW_ACCEPTED',nslow)
def flagword(hist,track,y,t,L):
    cuts,mids,tags,ac=hist
    i=idx(track,y,0)
    return tuple(int(cuts[v-1][i]!=mids[v][i]) for v in range(t,t+L))
ctrl=V.history(fields(0,0,0,0,0,0),40)
for track in range(2):
    hist=Counter();first=None
    for L in range(1,9):
        for t,y in product(range(1,42-L),range(8)):
            vals=[]
            for q in range(4):
                words={flagword(hs[(q,z) if track==0 else (z,q)],track,y,t,L) for z in range(4)}
                if len(words)!=1:break
                vals.append(next(iter(words)))
            if len(vals)!=4 or len(set(vals))!=4:continue
            hist[L]+=1
            if first is None:first=L,t,y,tuple(vals),flagword(ctrl,track,y,t,L)
    print('E3 COUNTS',track,[(i,hist[i]) for i in range(1,9)])
    print('E3 FIRST',track,first)
print('PASS E dual integral bases, local fast read, exact coincidence invariant')
