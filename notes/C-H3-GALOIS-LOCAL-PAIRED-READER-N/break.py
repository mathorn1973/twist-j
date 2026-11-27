"""NON-CANONICAL alternate exact five-cyclic-coefficient audit of #2111.
Result-exposed; does not import the first verifier or public H3 source.
"""
from functools import cache
from itertools import product, permutations
from collections import Counter
from pathlib import Path

def red(z):
    z=tuple(z)
    return tuple(x-z[4] for x in z[:4])+(0,)
def p(n):return red(int(k==n%5) for k in range(5))
def add(a,b):return red(x+y for x,y in zip(a,b))
def sc(k,a):return red(k*x for x in a)
def sub(a,b):return add(a,sc(-1,b))
@cache
def mul(a,b):return red(sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5))
def sig(a,k):return red(sum(a[i] for i in range(5) if i*k%5==j) for j in range(5))
@cache
def h(a):return mul(a,sig(a,4))
Z=sc(0,p(0));O=p(0);R=p(2);RI=p(3);J=add(O,R);JI=sc(-1,add(p(1),p(2)))
T=h(J);P=tuple(p(k) for k in range(5))
v=add(P[2],P[3]); K=lambda z:mul(v,sig(z,2));W=lambda z:mul(P[4],sig(z,2))
def rsum(seq):return tuple(map(sum,zip(*seq)))
def scalar(H):
    n=4*H[0]-sum(H[1:]);assert n%2==0;return n//2
def even(a):return not any(x%2 for x in a)
def half(a):
    assert even(a)
    return tuple(x//2 for x in a)
@cache
def C(a,b,back=False):
    dif=sub(a,b)
    if not even(dif):return a,b
    u=mul(RI if back else R,dif)
    return half(add(add(a,b),u)),half(sub(add(a,b),u))
@cache
def B(cell):
    a,b,u,v=cell
    if not even(sub(a,b)) or not even(sub(u,v)):return cell,0
    d,f=half(sub(a,b)),half(sub(u,v));m,n=half(add(a,b)),half(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        D,F,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        D,F,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(m,D),sub(m,D),add(n,F),sub(n,F)),k
def ix(x,y):return x*8+y
def transport(F,bit,back=False):
    G=[list(c) for c in F]
    for x,y in product(range(8),range(bit,8,2)):
        i,k=ix(x,y),ix(x,(y+1)%8)
        for r in range(3):G[i][r],G[k][r]=C(F[i][r],F[k][r],back)
    for x,y in product(range(bit,8,2),range(8)):
        i,k=ix(x,y),ix((x+1)%8,y)
        G[i][3],G[k][3]=C(F[i][3],F[k][3],back)
    return tuple(tuple(c) for c in G)
def account(F):
    return rsum(z for c in F for z in c[:2]),rsum(z for c in F for z in c[2:]),rsum(h(z) for c in F for z in c)
def step(F,bit,ac):
    G=transport(F,bit)
    coll=tuple(B(c) for c in G)
    N=tuple(c for c,t in coll)
    assert account(G)==account(N)==ac
    back=tuple(B(c)[0] for c in N)
    assert back==G and transport(back,bit,True)==F
    return G,N,tuple(t for c,t in coll)
def hist(F,n):
    ac=account(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac)
        cuts.append(F);mids.append(G);tags.append(E)
    return cuts,mids,tags,ac
def seed(b,marks):
    F=[]
    for x,y in product(range(8),range(8)):
        d=marks.get((x,y),sc((-1)**y,O))
        F.append((d,sc(-1,d),Z,sc(2*(-1)**(x+b*y),J)))
    return tuple(F)
def shift(F,a):return tuple(F[ix(x,(y-a)%8)] for x,y in product(range(8),range(8)))
def single(b,k=1,l=2,r=0):
    a=2 if b==0 else -2
    return seed(b,{(0,a*r%8):P[k],(0,(4+a*r)%8):P[l]})
def double(b,c,r,u,k=1,l=2,m=3,n=4):
    a=2 if b==0 else -2
    return seed(b,{(0,a*r%8):P[k],(0,(4+a*r)%8):P[l],
                   (c,a*u%8):P[m],(c,(4+a*u)%8):P[n]})
def raw(z):return z[:4]
def ddet(A):
    if len(A)==1:return A[0][0]
    return sum((-1)**i*v*ddet([r[:i]+r[i+1:] for r in A[1:]]) for i,v in enumerate(A[0]))
def coldet(V):return ddet([list(r) for r in zip(*[raw(x) for x in V])])
def one(k):return tuple(int(i==k) for i in range(4))

# A: independent census on complete translated full fields.
for b,s,a in ((0,120,2),(1,40,-2)):
    F0=single(b);cuts,mids,tags,ac=hist(F0,4*s)
    assert all(cuts[r*s]==shift(F0,r*a) for r in range(5))
    count=0;maxdist=0
    for t,x,y in product(range(1,s+1),range(8),range(8)):
        n=len({cuts[t][ix(x,(y-a*r)%8)][2] for r in range(4)})
        count+=n==4;maxdist=max(n,maxdist)
    assert count==0
    print('ALT A',b,'FOUR_DISTINCT_CLK',count,'MAX_DISTINCT',maxdist)

# B: actual replay of all four strokes in all layouts.
total=0
for b,s,a in ((0,120,2),(1,40,-2)):
    for c in range(1,8):
        good=0
        for r,u in product(range(4),repeat=2):
            F=double(b,c,r,u);F0=F;ac=account(F)
            assert scalar(ac[2])==1024
            for t in range(1,4*s+1):
                _,F,_=step(F,(t-1)%2,ac)
                if t%s==0:assert F==double(b,c,(r+t//s)%4,(u+t//s)%4)
            assert F==F0
            good+=1;total+=1
        print('ALT B',b,c,'FOUR_STROKES',good)
assert total==224
print('ALT B PASS',total)

def orbit(f,x):
    out=[x]
    for _ in range(4):out.append(f(out[-1]))
    assert out[-1]==out[0]
    return tuple(out[:4])
# C: independent port temporal code.
tagpairs=((1,2),(1,3),(1,4),(2,3))
xs,fs=orbit(K,P[1]),orbit(W,P[2])
words={};ells={};pairset=set();states=set()
for d,(k,l) in enumerate(tagpairs):
    F=single(1,k,l);cut=hist(F,160)[0]
    assert all(cut[40*n]==shift(F,-2*n) for n in range(5))
    for r in range(4):
        E=single(1,k,l,r);assert E not in states;states.add(E)
        word=tuple(P.index(cut[40*((n+r)%4)][0][0]) for n in range(4))
        tags=tuple(sorted(q for q in word if q))
        rr=(-word.index(tags[0]))%4
        assert (tagpairs.index(tags),rr)==(d,r)
        x,f=xs[rr],fs[(rr+d)%4]
        assert (x,f) not in pairset;pairset.add((x,f));words[(d,r)]=word
        val=mul(x,f)[3];assert mul(K(x),W(f))[3]==val
        ells.setdefault(d,val);assert ells[d]==val
print('ALT C PREFIX',[len({w[:k] for w in words.values()}) for k in range(1,5)],'ELL',sorted(ells.items()))

# D: full radiation and B tag comparison, local cut counts.
cases=tuple(product(range(4),repeat=2))
hs={p0:hist(double(1,1,*p0),165) for p0 in cases}
control=hist(double(1,1,0,0,0,0,0,0),41)
def radword(hh):
    cuts,mids,tags,ac=hh
    return tuple(tuple(z for c in F for z in c[2:]) for t in range(41)
        for F in ((cuts[t],) if t==0 else (mids[t],cuts[t])))
def tagword(hh):return tuple(hh[2][1:41])
def masks(hh):
    cuts=hh[0]
    return tuple(tuple(even(sub(cuts[t-1][ix(x,y)][0],cuts[t-1][ix(x,(y+1)%8)][0]))
        for x,y in product(range(8),range((t-1)%2,8,2))) for t in range(1,41))
for name,fun in (('radiation',radword),('Btags',tagword),('matter_C_masks',masks)):
    arr=[fun(hs[p]) for p in cases]
    print('ALT D1',name,len(set(arr)),sum(z==fun(control) for z in arr))
for track in range(2):
    counts=Counter();first=None
    for t,y in product(range(40),range(8)):
        for n in (1,2):
            vals=[]
            for q in range(4):
                z={tuple(hs[(q,k) if track==0 else (k,q)][0][t+i][ix(track,y)][0] for i in range(n)) for k in range(4)}
                if len(z)!=1:break
                vals.append(next(iter(z)))
            if len(vals)!=4:continue
            counts[n,'independent']+=1
            if len(set(vals))==4:
                counts[n,'distinct']+=1
                if n==2 and first is None:first=t,y,tuple(tuple(raw(z) for z in v) for v in vals)
    print('ALT D2',track,sorted(counts.items()),'FIRST',first)

# E: dual bases, independent direct full-field read and event census.
X,Y=orbit(K,P[2]),orbit(W,sc(-1,P[2]))
assert all(abs(coldet(V))==1 for V in (X,Y))
pairing=tuple(tuple(mul(x,y)[3] for y in Y) for x in X)
assert pairing==tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
print('E1 X',tuple(map(raw,X)),'DET',coldet(X))
print('E1 Y',tuple(map(raw,Y)),'DET',coldet(Y))
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
def rf(track,cuts,t):
    off=2+2*track
    return fast(track,cuts[t+off][ix(track,0)][0],cuts[t+off+1][ix(track,0)][0])
def rs(track,F):return slow(track,F[ix(track,0)][0],F[ix(track,2)][0])
def accepted(v):return v in tuple(one(k) for k in range(4))
def decode(v,basis):return rsum(sc(q,z) for q,z in zip(v,basis))
invs=Counter();count=0;pairset=set()
for r,u in cases:
    cuts,mids,tags,ac=hs[r,u];prev=None
    assert scalar(ac[2])==1024
    for n in range(5):
        t=n*40;F=cuts[t];rr,uu=(r+n)%4,(u+n)%4
        assert F==double(1,1,rr,uu)
        a,b=rf(0,cuts,t),rf(1,cuts,t)
        assert a==one(rr)==rs(0,F);assert b==one(uu)==rs(1,F)
        x,y=decode(a,X),decode(b,Y)
        p0=mul(x,y)[3]
        coinc=sum(int(F[ix(0,j)][0]==P[1] and F[ix(1,j)][0]==P[3]) for j in (0,2,4,6))
        assert p0==coinc==int(rr==uu)
        if n==0:invs[p0]+=1;pairset.add((x,y))
        else:assert x==K(prev[0]) and y==W(prev[1]) and p0==prev[2]
        prev=x,y,p0;count+=1
    assert cuts[160:166]==cuts[:6]
    print('E2 CASE',r,u,'ELL',prev[2],'Q',1024)
assert len(pairset)==16 and count==80 and invs=={0:12,1:4}
print('E2 PAIRS',len(pairset),'WINDOWS',count,'ELL_HISTOGRAM',sorted(invs.items()))
controls=((0,0,3,4),(1,1,3,4),(2,2,3,4),(1,2,0,0),(1,2,3,3),(1,2,4,4))
for k,l,m,n in controls:
    nfast=nslow=0
    for r,u in cases:
        cut=hist(double(1,1,r,u,k,l,m,n),5)[0]
        nfast+=all(accepted(rf(t,cut,0)) for t in (0,1))
        nslow+=all(accepted(rs(t,cut[0])) for t in (0,1))
    print('E2 CONTROL',k,l,m,n,'FAST_ACCEPTED',nfast,'SLOW_ACCEPTED',nslow)
def flags(hh,x,y,t,L):
    cut,mid,_,_=hh;i=ix(x,y)
    return tuple(int(cut[v-1][i][0]!=mid[v][i][0]) for v in range(t,t+L))
for track in range(2):
    counts=Counter();first=None
    for L in range(1,9):
        for t,y in product(range(1,42-L),range(8)):
            vals=[]
            for q in range(4):
                words={flags(hs[(q,k) if track==0 else (k,q)],track,y,t,L) for k in range(4)}
                if len(words)!=1:break
                vals.append(next(iter(words)))
            if len(vals)!=4 or len(set(vals))!=4:continue
            counts[L]+=1
            if first is None:first=L,t,y,tuple(vals),flags(control,track,y,t,L)
    print('E3 COUNTS',track,[(i,counts[i]) for i in range(1,9)])
    print('E3 FIRST',track,first)
print('PASS E dual integral bases, local fast read, exact coincidence invariant')
