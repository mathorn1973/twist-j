"""NON-CANONICAL alternate exact audit of #2117.
Five cyclic coefficients; separately implemented native pair and site maps.
Does not import the pinned H3 source or any primary verifier.
Usage: python3 break.py A or B or C.
"""
from functools import cache
from itertools import product
from collections import Counter
import sys,re,ast
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
def conj(a):return red(a[(4*k)%5] for k in range(5))
@cache
def h(a):return mul(a,conj(a))
Z=sc(0,p(0));O=p(0);R=p(2);RI=p(3);J=add(O,R);JI=sc(-1,add(p(1),p(2)))
L=sub(O,R);T=h(J);P=tuple(p(k) for k in range(5))
def neg(z):return sc(-1,z)
def even(z):return all(x%2==0 for x in z)
def half(z):
    assert even(z);return tuple(x//2 for x in z)
def rs(seq):return tuple(map(sum,zip(*seq)))
def scalar(z):
    t=4*z[0]-sum(z[1:]);assert t%2==0;return t//2
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
    d,f=half(sub(a,b)),half(sub(u,v));c,g=half(add(a,b)),half(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        D,F,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        D,F,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(c,D),sub(c,D),add(g,F),sub(g,F)),k
def ix(x,y):return x*2+y
def val(F,x,y):return F[ix(x,y)]
def src(F):return F[:2]
def reader(F):return F[2:]
def raw(z):return z[:4]
def rc(c):return tuple(map(raw,c))
def rsrc(F):return tuple(raw(z) for c in src(F) for z in c)
def transport(F,bit,back=False):
    G=[list(c) for c in F]
    for x in range(8):
        i,k=ix(x,bit),ix(x,1-bit)
        for q in range(3):G[i][q],G[k][q]=C(F[i][q],F[k][q],back)
    for x,y in product(range(bit,8,2),range(2)):
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
def hist(F,n):
    ac=acc(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac);cuts.append(F);mids.append(G);tags.append(E)
    return cuts,mids,tags,ac
def word(hh,t):
    cut,mid,_,_=hh
    return tuple(reader(F) for u in range(t+1) for F in ((cut[u],) if u==0 else (mid[u],cut[u])))
def cols(d,g,c):return d,neg(d),g,c
def tagdict(t):return {divmod(i,2):k for i,k in enumerate(t) if k}
def A_gate():
    m=sc(3,O);a=L;b=sub(add(mul(m,R),mul(J,a)),sc(4,J))
    f=sc(2,O);g=add(add(b,sc(2,mul(J,a))),sc(2,f))
    delta=mul(sub(JI,O),f);gp=add(g,delta);gs=sc(2,mul(J,m))
    stock=(Z,sc(2,O),sc(2,O),b,b,b,add(mul(m,R),sc(2,a)))
    def seed(p):
        return tuple(cols(add(m,sub(p,P[1])),gs,Z) if x==0 else
            cols(mul(JI,f) if x==6 else Z,g if x==6 else Z,stock[x-1])
            for x,y in product(range(8),range(2)))
    print('A STOCK',tuple(map(raw,stock)),'CLK',raw(g),'MARK',raw(gp),'DELTA',raw(delta))
    assert h(add(f,mul(J,a)))!=h(f)
    assert h(mul(JI,f))!=mul(T,h(add(f,mul(J,a))))
    hs={}
    for k,p in enumerate(P):
        pos=k==1;d=add(m,sub(p,P[1]));hp=h(d)
        assert (hp==h(m))==pos and hp!=mul(h(m),mul(T,T))
        F0=seed(p);hh=hist(F0,160);cuts,mids,tags,ac=hh;hs[k]=hh
        assert reader(F0)==reader(seed(P[0]))
        expected=[{(0,y):1 for y in range(2)}, {},{(6,y):1 for y in range(2)},{(0,y):2 for y in range(2)}]
        assert all(tagdict(tags[t])==(expected[t-1] if pos else {}) for t in range(1,5))
        for y in range(2):
            assert val(mids[1],0,y)==val(F0,0,y)
            assert val(cuts[1],0,y)[3]==(mul(m,R) if pos else Z)
            assert val(mids[2],0,y)[3]==(add(mul(m,R),mul(L,a)) if pos else Z)
            assert val(cuts[2],7,y)[3]==(add(mul(m,R),mul(J,a)) if pos else stock[-1])
            assert (not even(sub(val(mids[2],0,y)[2],val(mids[2],0,y)[3])))==pos
            assert val(mids[3],0,y)==val(cuts[2],0,y)
            assert val(mids[3],7,y)[3]==(sub(mul(m,R),mul(J,a)) if pos else stock[-1])
            assert val(mids[3],6,y)[3]==(add(b,sc(2,mul(J,a))) if pos else b)
            assert val(mids[4],0,y)[3]==(mul(m,R) if pos else Z)
            if pos:assert half(sub(val(mids[4],0,y)[2],val(mids[4],0,y)[3]))==m
            assert val(cuts[3],6,y)[2]==val(cuts[4],6,y)[2]==(gp if pos else g)
        assert src(cuts[4])==src(F0)
        assert (src(cuts[1])!=src(F0))==pos
        assert all(src(cuts[t])==src(F0) for t in range(1,5))==(not pos)
        print('A CASE',k,'H_D',raw(hp),'H',raw(ac[2]),'Q',scalar(ac[2]),'SOURCE_RETURN4',1,'CLK4',raw(val(cuts[4],6,0)[2]))
        for t in range(1,5):
            print('A LOCAL',k,t,'SOURCE',rc(val(cuts[t],0,0)),'READER6',rc(val(cuts[t],6,0)),'CORR7',raw(val(cuts[t],7,0)[3]),'TAGS',sorted(tagdict(tags[t]).items()))
    for t in range(5):
        n=len({word(hh,t) for hh in hs.values()})
        assert n==(1 if t<2 else 2) and len({word(hs[k],t) for k in (0,2,3,4)})==1
        print('A PREFIX',t,n)
    for k,hh in hs.items():print('A RETURN',k,[t for t in range(1,161) if src(hh[0][t])==src(hh[0][0])])
    print('A COMMON_RETURN',[t for t in range(1,161) if all(src(hh[0][t])==src(hh[0][0]) for hh in hs.values())])
    for stage,name in ((1,'POST_C'),(0,'FULL')):
        loss=next((t for t in range(5,161) if not all(val(hh[stage][t],6,0)[2]==(gp if k==1 else g) for k,hh in hs.items())),None)
        print('A OUTPUT_FIRST_LOSS',name,loss)
    loss=next((t for t in range(5,161) if len({word(hh,t) for hh in hs.values()})!=2),None)
    print('A READER_FIRST_EXTRA_CLASS',loss)
    for name,p in (('zero',Z),('minus_j',neg(P[1]))):
        F=seed(p);cut,mid,tags,ac=hist(F,4)
        print('A CONTROL',name,'RETURN4',int(src(cut[4])==src(F)),'CLK4',raw(val(cut[4],6,0)[2]),'Q',scalar(ac[2]))
    print('A PASS 5/5 complete source columns restored, bit=0, remote record')

m=sub(sc(2,O),R);gs=sc(2,mul(J,m));mR=mul(m,R)
assert h(m)!=O and mul(mul(T,T),h(m))!=O
values=(Z,)+tuple(sc(s,P[k]) for s in (1,-1) for k in range(5))
def stock_for(n,l,vi):
    u=sc(n,P[l]);a=mul(L,u);v=values[vi];z=mul(L,v)
    b=sub(add(mR,mul(J,a)),sc(4,mul(J,u)))
    c2=add(mR,mul(L,a))
    if even(b) or (z!=Z and (even(z) or even(sub(z,c2)))):return None
    return a,z,b,(Z,sc(2,v),sc(2,v),b,b,b,add(mR,sc(2,a)))
def setup(p,stock):
    F=[]
    for x,y in product(range(8),range(2)):
        d=(p if y==0 else sc(3,P[1])) if x==0 else Z
        g=gs if x==0 else Z
        c=(Z if x==0 else stock[x-1]) if y==0 else gs
        F.append(cols(d,g,c))
    return tuple(F)
def B_gate():
    wins=[];count=total=0;returns_hist=Counter();match_hist=Counter()
    for n,l,vi in product((-3,-1,1,3),range(5),range(len(values))):
        total+=1
        params=stock_for(n,l,vi)
        if params is None:
            print('B FILTER',n,l,vi,'REJECT');continue
        a,z,b,stock=params
        F0=[setup(p,stock) for p in P];F=F0[:]
        accounts=[acc(x) for x in F]
        assert len(set(accounts))==1
        ac=accounts[0];Q=scalar(ac[2]);count+=1
        firstmat=[tuple(v for c in src(transport(ff,0)) for v in c[:2]) for ff in F0]
        histneg=True;histpos=False;ret=[];match=[];split=None
        for t in range(1,161):
            mids=[];nxt=[];tt=[]
            for ff in F:
                mid,nf,tags=step(ff,(t-1)%2,ac)
                mids.append(mid);nxt.append(nf);tt.append(tags)
            for stage in (mids,nxt):
                negsame=len({reader(stage[k]) for k in (0,2,3,4)})==1
                if histneg and not negsame:split=t
                histneg &= negsame
                histpos |= reader(stage[1])!=reader(stage[0])
            F=nxt
            if t<=4:
                for k,ff in enumerate(F):
                    pos=k==1;expected=[0]*16
                    if pos and t in (1,4):expected[0]=1 if t==1 else 2
                    assert tt[k]==tuple(expected)
                    if t==1:
                        assert tuple(z for c in src(mids[k]) for z in c[:2])==firstmat[k]
                        assert val(mids[k],0,0)[0]==(mul(m,P[1]) if pos else P[k])
                        assert val(mids[k],0,1)[0]==(mul(add(sc(2,O),R),P[1]) if pos else sc(3,P[1]))
                    if t in (2,3,4):
                        assert tuple(z for c in src(mids[k]) for z in c[:2])==tuple(mul(J,z) if pos and i<2 else z for i,z in enumerate(firstmat[k]))
                    if t==4:
                        assert tuple(z for c in src(ff) for z in c[:2])==firstmat[k]
                        assert tuple(z for c in src(ff) for z in c[2:])==tuple(z for c in src(F0[k]) for z in c[2:])
            if t>=6 and t%2==0 and all(src(ff)==src(init) for ff,init in zip(F,F0)):
                ret.append(t);nv={val(F[k],6,0)[3] for k in (0,2,3,4)}
                if histneg and histpos and len(nv)==1 and val(F[1],6,0)[3]!=next(iter(nv)):match.append(t)
        returns_hist[len(ret)]+=1;match_hist[len(match)]+=1
        print('B STOCK',n,l,vi,'A',raw(a),'Z',raw(z),'Q',Q,'RETURNS',ret,'MATCHES',match,'NEGATIVE_SPLIT',split)
        if match:wins.append((n,l,vi,match[0],stock))
    assert total==220
    print('B CENSUS',total,'ADMITTED',count,'RETURN_HIST',sorted(returns_hist.items()),'MATCH_HIST',sorted(match_hist.items()))
    print('B WIN_COUNT',len(wins))
    if wins:
        n,l,vi,t,stock=wins[0];print('B SELECT',n,l,vi,t)
        hh=[hist(setup(p,stock),160) for p in P]
        assert all(src(w[0][t])==src(w[0][0]) for w in hh)
        vals=[val(w[0][t],6,0)[3] for w in hh]
        assert len(set(vals))==2 and all(vals[k]==vals[0] for k in (0,2,3,4)) and vals[1]!=vals[0]
        assert len({word(w,t) for w in hh})==2
        for k,w in enumerate(hh):print('B WITNESS',k,'SOURCE',rsrc(w[0][t]),'REMOTE',raw(vals[k]),'Q',scalar(w[3][2]))
        for stage,name in ((1,'POST_C'),(0,'FULL')):
            loss=next((v for v in range(t+1,161) if any(val(w[stage][v],6,0)[3]!=vals[k] for k,w in enumerate(hh))),None)
            print('B HOLD_FIRST_LOSS',name,loss)
    else:print('B NO RAW ECHO IN FROZEN CENSUS')
    print('DONE exact raw equal-account echo census')

def C_gate():
    root=Path(__file__).resolve().parent
    stocks=[]
    for line in (root/'B.txt').read_text().splitlines():
        mat=re.match(r'^B STOCK (-?\d+) (\d+) (\d+) .* MATCHES (\[.*?\]) NEGATIVE_SPLIT ',line)
        if mat:
            n,l,vi=map(int,mat.groups()[:3]);ts=ast.literal_eval(mat[4])
            if ts:stocks.append((n,l,vi,ts[0]))
    assert len(stocks)==143 and stocks[0]==(-3,0,0,24)
    for n,l,vi,Tcut in stocks:
        st=stock_for(n,l,vi)[3]
        old={k:hist(setup(p,st),Tcut) for k,p in enumerate(P)}
        pos=val(old[1][0][Tcut],6,0)[3];neg0=val(old[0][0][Tcut],6,0)[3]
        assert pos!=neg0 and all(val(old[k][0][Tcut],6,0)[3]==neg0 for k in (0,2,3,4))
        assert all(val(hh[0][Tcut],6,0)[3]==val(hh[1][Tcut],6,0)[3] for hh in old.values())
        print('C STOCK',n,l,vi,Tcut,'POS',raw(pos),'NEG',raw(neg0))
        rejects=Counter()
        for v,mult in product(tuple(x for x in product(range(2),repeat=4) if any(x)),range(1,16,2)):
            a=sc(mult,v+(0,));g=add(pos,sc(2,a));d=mul(JI,a)
            early=None
            for t,k in product(range(1,Tcut),range(5)):
                tag=B((d,neg(d),g,val(old[k][1][t],6,0)[3]))[1]
                if tag:early=t,k,tag;break
            # All the frozen candidates are excluded by earlier writes.
            # A contradiction fails rather than falling through to a new search.
            assert early is not None
            rejects['early']+=1
            print('C CANDIDATE',raw(a),'REJECT_EARLY',early)
        print('C CENSUS',n,l,vi,'REJECT',sorted(rejects.items()),'HOLD_HIST',[])
    print('C NO CAPTURE')
    print('DONE exact equal-account source echo capture')
if sys.argv[1]=='A':A_gate()
elif sys.argv[1]=='B':B_gate()
elif sys.argv[1]=='C':C_gate()
else:raise SystemExit('use A, B or C')
