"""NON-CANONICAL source echo; frozen issue #2117, gate A."""
import sys,hashlib,importlib.util
from pathlib import Path
from itertools import product
from functools import cache
from collections import Counter
source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H
spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,R,J,JI,P=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV,H.J_POWERS
add,sub,mul,sc,h=H.add,H.sub,cache(H.mul),H.scale,H.h
neg=lambda x:sc(-1,x)
L=sub(O,R); T=H.T
idx=lambda x,y,q:H.index(2,x,y,q)
def rs(seq):return tuple(map(sum,zip(*seq)))
def acc(F):
    return rs(z for i,z in enumerate(F) if i%4<2),rs(z for i,z in enumerate(F) if i%4>=2),rs(h(z) for z in F)
def step(F,bit,account):
    G=H.transport(F,2,bit)
    N,ev=H.collide(G,2)
    back,_=H.collide(N,2)
    assert back==G and H.transport(back,2,bit,backward=True)==F
    assert acc(G)==acc(N)==account
    return G,N,{(x,y):t for x,y,t in ev}
def hist(F,n):
    ac=acc(F);cut=[F];mid=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac);cut.append(F);mid.append(G);tags.append(E)
    return cut,mid,tags,ac
def cell(F,x,y):
    i=idx(x,y,0);return F[i:i+4]
def src(F):return F[:8]
def reader(F):return F[8:]
def word(hh,t):
    cut,mid,_,_=hh
    return tuple(reader(F) for u in range(t+1) for F in ((cut[u],) if u==0 else (mid[u],cut[u])))
def cols(d,g,c):
    return d,neg(d),g,c
def powr(a,n):
    t=O
    for _ in range(n):t=mul(t,a)
    return t
m=sc(3,O);a=L;b=sub(add(mul(m,R),mul(J,a)),sc(4,J))
f=sc(2,O);g=add(add(b,sc(2,mul(J,a))),sc(2,f))
delta=mul(sub(JI,O),f)
gp=add(g,delta)
assert gp!=g
source_g=sc(2,mul(J,m))
stock=(Z,sc(2,O),sc(2,O),b,b,b,add(mul(m,R),sc(2,a)))
def seed(p):
    F=[]
    for x,y in product(range(8),range(2)):
        if x==0:F.extend(cols(add(m,sub(p,P[1])),source_g,Z))
        else:F.extend(cols(mul(JI,f) if x==6 else Z,g if x==6 else Z,stock[x-1]))
    return tuple(F)
def halfdiff(c):
    assert H.even(sub(c[2],c[3]))
    return H.half(sub(c[2],c[3]))
print('A STOCK',stock,'CLK',g,'MARK',gp,'DELTA',delta)
assert h(add(f,mul(J,a)))!=h(f)
assert h(mul(JI,f))!=mul(T,h(add(f,mul(J,a))))
hs={}
for k,p in enumerate(P):
    pos=k==1;d=add(m,sub(p,P[1]));hp=h(d)
    assert (hp==h(m))==pos
    assert hp!=mul(h(m),mul(T,T))
    F0=seed(p);hh=hist(F0,160);cuts,mids,tags,ac=hh;hs[k]=hh
    assert reader(F0)==reader(seed(P[0]))
    assert tags[1]==({(0,y):1 for y in range(2)} if pos else {})
    assert tags[2]=={}
    assert tags[3]==({(6,y):1 for y in range(2)} if pos else {})
    assert tags[4]==({(0,y):2 for y in range(2)} if pos else {})
    for y in range(2):
        assert cell(mids[1],0,y)==cell(F0,0,y)
        assert cell(cuts[1],0,y)[3]==(mul(m,R) if pos else Z)
        assert cell(mids[2],0,y)[3]==(add(mul(m,R),mul(L,a)) if pos else Z)
        assert cell(cuts[2],7,y)[3]==(add(mul(m,R),mul(J,a)) if pos else stock[-1])
        assert (not H.even(sub(cell(mids[2],0,y)[2],cell(mids[2],0,y)[3])))==pos
        assert cell(mids[3],0,y)==cell(cuts[2],0,y)
        assert cell(mids[3],7,y)[3]==(sub(mul(m,R),mul(J,a)) if pos else stock[-1])
        assert cell(mids[3],6,y)[3]==(add(b,sc(2,mul(J,a))) if pos else b)
        assert cell(mids[4],0,y)[3]==(mul(m,R) if pos else Z)
        if pos:assert halfdiff(cell(mids[4],0,y))==m
        assert cell(cuts[3],6,y)[2]==cell(cuts[4],6,y)[2]==(gp if pos else g)
    assert src(cuts[4])==src(F0)
    assert (src(cuts[1])!=src(F0))==pos
    assert all(src(cuts[t])==src(F0) for t in range(1,5))== (not pos)
    print('A CASE',k,'H_D',hp,'H',ac[2],'Q',H.scalar_account(ac[2]),'SOURCE_RETURN4',int(src(cuts[4])==src(F0)),'CLK4',cuts[4][idx(6,0,2)])
    for t in range(1,5):
        print('A LOCAL',k,t,'SOURCE',cell(cuts[t],0,0),'READER6',cell(cuts[t],6,0),'CORR7',cell(cuts[t],7,0)[3],'TAGS',sorted(tags[t].items()))
for t in range(5):
    n=len({word(hh,t) for hh in hs.values()})
    assert n==(1 if t<2 else 2)
    assert len({word(hs[k],t) for k in (0,2,3,4)})==1
    print('A PREFIX',t,n)
for k,hh in hs.items():
    times=[t for t in range(1,161) if src(hh[0][t])==src(hh[0][0])]
    print('A RETURN',k,times)
print('A COMMON_RETURN',[t for t in range(1,161) if all(src(hh[0][t])==src(hh[0][0]) for hh in hs.values())])
for stage,name in ((1,'POST_C'),(0,'FULL')):
    loss=next((t for t in range(5,161) if not all(hh[stage][t][idx(6,0,2)]==(gp if k==1 else g) for k,hh in hs.items())),None)
    print('A OUTPUT_FIRST_LOSS',name,loss)
# Full reader-history comparison through all tested ticks.
loss=next((t for t in range(5,161) if len({word(hh,t) for hh in hs.values()})!=2),None)
print('A READER_FIRST_EXTRA_CLASS',loss)
for name,p in (('zero',Z),('minus_j',neg(P[1]))):
    F=seed(p);cut,mid,tags,ac=hist(F,4)
    print('A CONTROL',name,'RETURN4',int(src(cut[4])==src(F)),'CLK4',cut[4][idx(6,0,2)],'Q',H.scalar_account(ac[2]))
print('A PASS 5/5 complete source columns restored, bit=0, remote record')
