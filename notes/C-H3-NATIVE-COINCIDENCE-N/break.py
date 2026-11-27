"""NON-CANONICAL result-exposed alternate #2113 audit.
Independent five-power cyclic arithmetic, no primary or H3 source import.
Usage: python3 break.py A or D.
"""
from functools import cache
from itertools import product
from collections import Counter
import sys

def reduce(v):
    v=tuple(v);return tuple(x-v[4] for x in v[:4])+(0,)
def p(n):return reduce(int(k==n%5) for k in range(5))
def add(a,b):return reduce(x+y for x,y in zip(a,b))
def sc(k,a):return reduce(k*x for x in a)
def sub(a,b):return add(a,sc(-1,b))
@cache
def mul(a,b):return reduce(sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5))
def conj(a):return reduce(a[(4*k)%5] for k in range(5))
@cache
def h(a):return mul(a,conj(a))
Z=sc(0,p(0));O=p(0);R=p(2);RI=p(3);J=add(O,R);JI=sc(-1,add(p(1),p(2)))
T=h(J);P=tuple(p(k) for k in range(5));m=8
def neg(z):return sc(-1,z)
def even(z):return all(x%2==0 for x in z)
def half(z):
    assert even(z);return tuple(x//2 for x in z)
def rs(seq):return tuple(map(sum,zip(*seq)))
def scalar(z):
    t=4*z[0]-sum(z[1:]);assert t%2==0;return t//2
@cache
def C(a,b,back=False):
    d=sub(a,b)
    if not even(d):return a,b
    u=mul(RI if back else R,d)
    return half(add(add(a,b),u)),half(sub(add(a,b),u))
@cache
def B(cell):
    a,b,u,v=cell
    if not even(sub(a,b)) or not even(sub(u,v)):return cell,0
    d,f=half(sub(a,b)),half(sub(u,v));c,g=half(add(a,b)),half(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        D,F,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        D,F,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(c,D),sub(c,D),add(g,F),sub(g,F)),k
def ix(x,y):return x*8+y
def transport(F,bit,back=False):
    G=[list(c) for c in F]
    for x,y in product(range(8),range(bit,8,2)):
        i,k=ix(x,y),ix(x,(y+1)%8)
        for q in range(3):G[i][q],G[k][q]=C(F[i][q],F[k][q],back)
    for x,y in product(range(bit,8,2),range(8)):
        i,k=ix(x,y),ix((x+1)%8,y)
        G[i][3],G[k][3]=C(F[i][3],F[k][3],back)
    return tuple(tuple(c) for c in G)
def acc(F):
    return rs(z for c in F for z in c[:2]),rs(z for c in F for z in c[2:]),rs(h(z) for c in F for z in c)
def step(F,bit,account):
    G=transport(F,bit)
    coll=tuple(B(c) for c in G)
    N=tuple(c for c,t in coll)
    assert acc(G)==acc(N)==account
    rev=tuple(B(c)[0] for c in N)
    assert rev==G and transport(rev,bit,True)==F
    return G,N,tuple(t for c,t in coll)
def run(F,n):
    ac=acc(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac);cuts.append(F);mids.append(G);tags.append(E)
    return cuts,mids,tags,ac
Rwrite=sc(m,sub(mul(R,R),R));other=sc(-m,R)
Hstar=add(sc(-4*m,O),add(sc(-5*m//2,R),sc(m//2,mul(R,R))))
left=sc(-2*m,J);start=C(left,Hstar,True)
assert C(*start)==(left,Hstar)
def seed(r,u,k=1,l=2,v=3,w=4,mode='A'):
    marks={(0,-2*r%8):P[k],(0,(4-2*r)%8):P[l],
           (7,-2*u%8):P[v],(7,(4-2*u)%8):P[w]}
    F=[]
    for x,y in product(range(8),repeat=2):
        d=marks.get((x,y),sc((-1)**y,O));g=Z;f=sc(2*(-1)**(x+y),J)
        if y%2==0:
            if x==0:d=add(sc(m,O),sub(d,P[1]))
            if x==7:d=add(sc(m,O),sub(d,P[3]));g=sc(4*m,O)
            if x in (0,1):f=left
            if x in (6,7):f=sc(m,sub(sc(4,O),sc(2,J)))
        else:
            if x in (0,7):d=O;g=O
            if x in (0,1,6,7):f=Z
        if mode=='D':
            if x in (1,2,3):d=Z
            if x in (0,1,2,3):f=(start[x] if x<2 else Hstar) if y%2==0 else Z
        F.append((d,neg(d),g,f))
    return tuple(F)
def val(F,x,y):return F[ix(x,y)]
def halfdiff(c):return half(sub(c[2],c[3]))
def raw(c):return ';'.join(','.join(map(str,z[:4])) for z in c)
def tup(z):return z[:4]
def strip(F):return tuple(val(F,0,y)[2] for y in range(0,8,2))
def mask(F):return tuple(int(z==Rwrite) for z in strip(F))
def expected(r,u):
    return tuple(int(r==u and y==-2*r%8) for y in range(0,8,2))
def binary(r,u):return tuple(Rwrite if f else Z for f in expected(r,u))
def firstbits(r,u,y):return int(y==-2*r%8),int(y==-2*u%8)
def localtype(r,u,y):
    p=1 if y==-2*r%8 else 2 if y==(4-2*r)%8 else 0
    q=3 if y==-2*u%8 else 4 if y==(4-2*u)%8 else 0
    return p,q
def F2(a,b):
    # Independent expansion with integral coefficients, no fractions.
    return mul(R,add(sc(m+(1-a)*m//2,O),
                  add(sc((1-a)*m//4,J),sc((1-b)*m//4,sub(O,R)))))
def records(hs,start_t):
    out=[]
    for t,x,y in product(range(start_t,161),range(8),range(8)):
        pos={val(hs[r,u][0][t],x,y)[2] for r,u in cases if r==u}
        negs={val(hs[r,u][0][t],x,y)[2] for r,u in cases if r!=u}
        if len(pos)==len(negs)==1 and pos!=negs:
            out.append((t,x,y,tup(next(iter(pos))),tup(next(iter(negs)))))
    return out
cases=tuple(product(range(4),repeat=2))
controls=((0,0,3,4),(1,1,3,4),(2,2,3,4),(1,2,0,0),(1,2,3,3),(1,2,4,4))

def A():
    for k,l in product((0,1,2),(0,3,4)):
        p,q=P[k],P[l];a,b=int(k==1),int(l==3)
        da=add(sc(m,O),sub(p,P[1]));db=add(sc(m,O),sub(q,P[3]))
        assert (h(da)==sc(m*m,O))==bool(a)
        assert (h(db)==sc(m*m,O))==bool(b)
        assert h(da)!=sc(m*m,mul(T,T)) and h(db)!=sc(m*m,mul(T,T))
        d=mul(J,da) if a else da;f=F2(a,b)
        assert h(f)!=mul(T,h(d)) and (h(d)==mul(T,h(f)))==bool(a*b)
        print('A NORMS',k,l,'MATTER',raw((h(d),)),'RAD',raw((h(f),)),'TAG',2*a*b)
    hs={};qvals=set()
    for r,u in cases:
        F0=seed(r,u);hh=run(F0,160);cuts,mids,tags,ac=hh;hs[r,u]=hh
        Q=scalar(ac[2]);qvals.add(Q)
        for y in range(0,8,2):
            a,b=firstbits(r,u,y)
            for x,e in ((0,a),(7,b)):
                assert val(mids[1],x,y)==val(F0,x,y)
                assert tags[1][ix(x,y)]==e
                assert halfdiff(val(cuts[1],x,y))==sc(m,add(O,sc(1-e,R)))
                assert val(mids[2],x,y)[:3]==val(cuts[1],x,y)[:3]
                assert val(cuts[1],x,y+1)==val(cuts[2],x,y+1)==(O,neg(O),O,Z)
            assert even(sub(val(cuts[1],0,y)[3],val(cuts[1],7,y)[3]))
            assert halfdiff(val(mids[2],0,y))==F2(a,b)
            assert tags[2][ix(0,y)]==2*a*b
            assert val(cuts[2],0,y)[2]==(Rwrite if a*b else other if a else Z)
            print('A WORD',r,u,y,a,b,'PRE1',raw(val(mids[1],0,y)),raw(val(mids[1],7,y)),
                  'FULL1',raw(val(cuts[1],0,y)),raw(val(cuts[1],7,y)),
                  'PRE2',raw(val(mids[2],0,y)),'FULL2',raw(val(cuts[2],0,y)))
        assert mask(cuts[2])==expected(r,u)
        print('A CASE',r,u,'MASK',mask(cuts[2]),'Q',Q,'H',tup(ac[2]))
    assert len(qvals)==1
    print('A PASS',len(hs),'POSITIVE',sum(sum(mask(hs[p][0][2])) for p in cases),'Q',next(iter(qvals)),'R',tup(Rwrite),'OTHER',tup(other))
    for n in range(1,5):
        t=n*40
        print('B STROKE',t,'COMPLETE_MATCHES',sum(hs[r,u][0][t]==seed((r+n)%4,(u+n)%4) for r,u in cases))
        if n<4:
            print('B REPEAT',t+2,'MASK_MATCHES',sum(mask(hs[r,u][0][t+2])==expected((r+n)%4,(u+n)%4) for r,u in cases))
    rr=records(hs,2);print('B FIXED_BINARY_RECORDS',len(rr))
    if rr:
        t,x,y,v,w=rr[0];print('B FIRST',t,x,y,'POS',v,'NEG',w)
        if t<160:
            print('B FIRST_HOLD_NEXT',*(int(all(tup(val(hs[r,u][i][t+1],x,y)[2])==(v if r==u else w) for r,u in cases)) for i in (1,0)))
    for k,l,v,w in controls:
        c=Counter(sum(mask(run(seed(r,u,k,l,v,w),2)[0][2])) for r,u in cases)
        print('C CONTROL',k,l,v,w,'R_COUNTS',sorted(c.items()))
    print('C EMPTY',mask(run(seed(0,0,0,0,0,0),2)[0][2]))
    print('DONE exact native two-tick coincidence and recurrence boundary')

def D():
    print('D STOCK',tup(Hstar),'INVERSE_PAIR',tuple(map(tup,start)))
    hs={};qvals=set();local={}
    for r,u in cases:
        hist=run(seed(r,u,mode='D'),160);cuts,mids,tags,ac=hist;hs[r,u]=hist
        Q=scalar(ac[2]);qvals.add(Q)
        old=run(seed(r,u),2)
        for t in (1,2):
            for x,y in product((0,7),range(8)):
                assert val(mids[t],x,y)==val(old[1][t],x,y)
                assert val(cuts[t],x,y)==val(old[0][t],x,y)
            assert not any(tags[t][ix(x,y)] for x,y in product((1,2,3),range(8)))
        for y in range(0,8,2):
            a,b=firstbits(r,u,y)
            assert val(cuts[2],1,y)[3]==Hstar
            assert val(mids[3],0,y)[:3]==val(cuts[2],0,y)[:3]
            assert even(sub(val(cuts[2],0,y)[3],Hstar))
            exp=C(val(cuts[2],0,y)[3],Hstar)
            assert exp==(val(mids[3],0,y)[3],val(mids[3],1,y)[3])
            assert exp[0]!=val(cuts[2],0,y)[3]
            if a and not b:assert halfdiff(val(mids[3],0,y))==sc(m,O)
            assert tags[3][ix(0,y)]==2*int(a and not b)
            key=localtype(r,u,y)
            v=(val(cuts[2],0,y),val(mids[3],0,y),val(cuts[3],0,y),tags[3][ix(0,y)])
            assert key not in local or local[key]==v;local[key]=v
        assert strip(cuts[3])==binary(r,u)
        print('D CASE',r,u,'STRIP',tuple(map(tup,strip(cuts[3]))),'Q',Q,'H',tup(ac[2]))
    assert len(qvals)==1 and len(local)==9
    for key,(a,b,c,t) in sorted(local.items()):
        print('D LOCAL',*key,'FULL2',raw(a),'PRE3',raw(b),'FULL3',raw(c),'TAG',t)
    print('D PASS',len(hs),'POSITIVE',sum(sum(mask(hs[p][0][3])) for p in cases),'Q',next(iter(qvals)))
    for t in range(4,13):
        print('D HOLD',t,'POST_C',sum(strip(hs[r,u][1][t])==binary(r,u) for r,u in cases),
              'FULL',sum(strip(hs[r,u][0][t])==binary(r,u) for r,u in cases))
    for r,u in cases:
        cuts,mids,tags,ac=hs[r,u];n=0;ok=True
        for t in range(4,13):
            for F in (mids[t],cuts[t]):
                if strip(F)!=binary(r,u):ok=False;break
                n+=1
            if not ok:break
        print('D HOLD_PREFIX_SUBSTEPS',r,u,n)
    for n in range(1,5):
        t=n*40
        print('D STROKE',t,'COMPLETE_MATCHES',sum(hs[r,u][0][t]==seed((r+n)%4,(u+n)%4,mode='D') for r,u in cases))
    rr=records(hs,3);print('D FIXED_BINARY_RECORDS',len(rr))
    if rr:print('D FIRST',rr[0])
    for k,l,v,w in controls:
        c=Counter();n=0
        for r,u in cases:
            F=run(seed(r,u,k,l,v,w,mode='D'),3)[0][3]
            c[sum(mask(F))]+=1;n+=all(z in (Z,Rwrite) for z in strip(F))
        print('D CONTROL',k,l,v,w,'R_COUNTS',sorted(c.items()),'BINARY',n)
    print('D EMPTY',tuple(map(tup,strip(run(seed(0,0,0,0,0,0,mode='D'),3)[0][3]))))
    print('DONE exact binary-strip successor')

if sys.argv[1]=='A':A()
elif sys.argv[1]=='D':D()
else:raise SystemExit('use A or D')
