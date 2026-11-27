"""NON-CANONICAL raw equal-account source echo census, frozen #2117 B."""
from pathlib import Path
import runpy
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from collections import Counter

root=Path(__file__).resolve().parent
captured=StringIO()
with redirect_stdout(captured):
    V=runpy.run_path(str(root/'verify.py'))
assert captured.getvalue()==(root/'A.txt').read_text()
H=V['H'];Z,O,R,J,JI,P=V['Z'],V['O'],V['R'],V['J'],V['JI'],V['P']
L,T=V['L'],V['T']
add,sub,mul,sc,h,neg=V['add'],V['sub'],V['mul'],V['sc'],V['h'],V['neg']
idx,cell,src,reader,acc=V['idx'],V['cell'],V['src'],V['reader'],V['acc']
m=sub(sc(2,O),R);g=sc(2,mul(J,m))
mR=mul(m,R)
assert h(m)!=O and mul(mul(T,T),h(m))!=O
# Precomputed matching edges; call only the unchanged pinned native
# local primitives. Literal full-field replay checks any selected witness.
edges=[]
for bit in range(2):
    e=[]
    for x in range(8):
        for q in range(3):e.append((idx(x,bit,q),idx(x,1-bit,q)))
    for x,y in product(range(bit,8,2),range(2)):
        e.append((idx(x,y,3),idx((x+1)%8,y,3)))
    edges.append(tuple(e))
def transport(F,bit,back=False):
    G=list(F)
    for i,k in edges[bit]:G[i],G[k]=H.transport_pair(F[i],F[k],back)
    return tuple(G)
def collide(F):
    G=[];tags=[]
    for i in range(0,len(F),4):
        c,t=H.collision(F[i:i+4]);G.extend(c);tags.append(t)
    return tuple(G),tuple(tags)
def step(F,bit,ac):
    G=transport(F,bit);N,tags=collide(G)
    assert acc(G)==acc(N)==ac
    back,_=collide(N)
    assert back==G and transport(back,bit,True)==F
    return G,N,tags
def setup(p,stock):
    F=[]
    for x,y in product(range(8),range(2)):
        d=(p if y==0 else sc(3,P[1])) if x==0 else Z
        clk=g if x==0 else Z
        c=(Z if x==0 else stock[x-1]) if y==0 else g
        F.extend((d,neg(d),clk,c))
    return tuple(F)
def init_stock(n,l,v):
    u=sc(n,P[l]);a=mul(L,u);z=mul(L,v)
    b=sub(add(mR,mul(J,a)),sc(4,mul(J,u)))
    c2=add(mR,mul(L,a))
    if H.even(b) or (z!=Z and (H.even(z) or H.even(sub(z,c2)))):return None
    stock=(Z,sc(2,v),sc(2,v),b,b,b,add(mR,sc(2,a)))
    return a,z,b,stock
values=(Z,)+tuple(sc(s,P[k]) for s in (1,-1) for k in range(5))
stocks=[];wins=[];count=0;returns_hist=Counter();match_hist=Counter()
total=0
for n,l,vi in product((-3,-1,1,3),range(5),range(len(values))):
    total+=1
    v=values[vi];params=init_stock(n,l,v)
    if params is None:
        print('B FILTER',n,l,vi,'REJECT')
        continue
    a,z,b,stock=params
    F0=[setup(p,stock) for p in P];F=F0[:]
    accounts=[acc(x) for x in F]
    assert len(set(accounts))==1
    ac=accounts[0]
    Q=H.scalar_account(ac[2]);count+=1
    first_material=[tuple(transport(ff,0)[i] for i in (0,1,4,5)) for ff in F0]
    histneg=True;histpos=False;ret=[];match=[];prefix_split=None
    port=idx(6,0,3)
    for t in range(1,161):
        mids=[];nxt=[];tt=[]
        for ff in F:
            mid,nf,tags=step(ff,(t-1)%2,ac)
            mids.append(mid);nxt.append(nf);tt.append(tags)
        for stage in (mids,nxt):
            negsame=len({reader(stage[k]) for k in (0,2,3,4)})==1
            if histneg and not negsame:prefix_split=t
            histneg &= negsame
            histpos |= reader(stage[1])!=reader(stage[0])
        F=nxt
        if t<=4:
            for k,ff in enumerate(F):
                pos=k==1
                expected=[0]*16
                if pos and t in (1,4):expected[0]=1 if t==1 else 2
                assert tt[k]==tuple(expected),(n,l,vi,k,t,tt[k])
                if t==1:
                    assert (mids[k][0],mids[k][1],mids[k][4],mids[k][5])==first_material[k]
                    if pos:
                        assert mids[k][0]==mul(m,P[1]) and mids[k][4]==mul(add(sc(2,O),R),P[1])
                    else:assert mids[k][0]==P[k] and mids[k][4]==sc(3,P[1])
                if t in (2,3,4):
                    assert tuple(mids[k][i] for i in (0,1,4,5))==tuple((mul(J,first_material[k][i]) if pos and i<2 else first_material[k][i]) for i in range(4))
                if t==4:
                    assert tuple(ff[i] for i in (0,1,4,5))==first_material[k]
                    assert tuple(ff[i] for i in (2,3,6,7))==tuple(F0[k][i] for i in (2,3,6,7))
        if t>=6 and t%2==0 and all(src(ff)==src(init) for ff,init in zip(F,F0)):
            ret.append(t)
            nv={F[k][port] for k in (0,2,3,4)}
            if histneg and histpos and len(nv)==1 and F[1][port]!=next(iter(nv)):
                match.append(t)
    returns_hist[len(ret)]+=1;match_hist[len(match)]+=1
    print('B STOCK',n,l,vi,'A',a,'Z',z,'Q',Q,'RETURNS',ret,'MATCHES',match,'NEGATIVE_SPLIT',prefix_split)
    if match:wins.append((n,l,vi,match[0],stock))
assert total==220
print('B CENSUS',total,'ADMITTED',count,'RETURN_HIST',sorted(returns_hist.items()),'MATCH_HIST',sorted(match_hist.items()))
print('B WIN_COUNT',len(wins))
if wins:
    n,l,vi,t,stock=wins[0]
    print('B SELECT',n,l,vi,t)
    hh=[V['hist'](setup(p,stock),160) for p in P]
    assert all(src(w[0][t])==src(w[0][0]) for w in hh)
    vals=[w[0][t][idx(6,0,3)] for w in hh]
    assert len(set(vals))==2 and all(vals[k]==vals[0] for k in (0,2,3,4)) and vals[1]!=vals[0]
    assert len({V['word'](w,t) for w in hh})==2
    for k,w in enumerate(hh):
        print('B WITNESS',k,'SOURCE',src(w[0][t]),'REMOTE',vals[k],'Q',H.scalar_account(w[3][2]))
    for stage,name in ((1,'POST_C'),(0,'FULL')):
        loss=next((v for v in range(t+1,161) if any(w[stage][v][idx(6,0,3)]!=vals[k] for k,w in enumerate(hh))),None)
        print('B HOLD_FIRST_LOSS',name,loss)
else:
    print('B NO RAW ECHO IN FROZEN CENSUS')
print('DONE exact raw equal-account echo census')
