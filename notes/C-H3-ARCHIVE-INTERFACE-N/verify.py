"""NON-CANONICAL #2127 A/B, exact interface diagnosis and passive archive tests."""
from pathlib import Path
import runpy,hashlib
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
root=Path(__file__).resolve().parent
assert hashlib.sha256((root/'predecessor.py').read_bytes()).hexdigest()=='ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95'
V=runpy.run_path(str(root/'predecessor.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
seed,cols,hist,step,account,ix=map(V.get,('seed','cols','hist','step','account','ix'))
src,worker,archive,reader=map(V.get,('sourcepart','worker','archive','reader'))
ARCH=V['ARCH'];K=range(5);N=(0,2,3,4)
D=((8,7,1,13),(6,5,-1,11)); G=(34,10,21,31)
g=(6,-2,12,1); mark=(5,-3,11,1)
def setup(F,d=D,g0=G):
    F=list(F)
    for y in range(2):
        i=ix(5,y,0);F[i:i+3]=(d[y],neg(d[y]),g0)
    return tuple(F)
def replace(F,p,q):
    assert F[:2]==(P[p],neg(P[p]))
    out=(P[q],neg(P[q]))+F[2:]
    assert account(F)==account(out)
    assert account(F+(P[q],neg(P[q])))==account(out+(P[p],neg(P[p])))
    return out
def cor(F):return F[3::4]
def cell(F,x,y):return F[ix(x,y,0):ix(x,y,0)+4]
def res(z):return tuple(v%2 for v in z)
def rsum(xs):return H.ring_sum(xs)
def railaccount(F,r):
    vv=F[r::4]
    return rsum(vv),rsum(h(z) for z in vv)
def ready(F,I):return src(F)==src(I) and worker(F)==worker(I)
def I(k):return setup(seed(k,'static'))
initial=[I(k) for k in K]
old=[hist(f,370,True) for f in initial]
assert len({hh[3] for hh in old})==1 and H.scalar_account(old[0][3][2])==7752
def A():
    for T in (114,198,244):
        F=[w[0][T] for w in old]
        assert all(ready(f,initial[k]) and account(archive(f))==account(archive(initial[k])) for k,f in enumerate(F))
        assert len({archive(F[k]) for k in N})==1 and archive(F[1])!=archive(F[0])
        print('A CUT',T,'DIFFERING_CORR',sum(x!=y for x,y in zip(cor(F[0]),cor(F[1]))),'SLOTS',sum(x!=y for x,y in zip(F[0],F[1])))
        for x,y,r in product(range(8),range(2),range(4)):
            i=ix(x,y,r);d=sub(F[1][i],F[0][i])
            if d!=Z:print('A DIFF',T,x,y,r,'NEG',F[0][i],'POS',F[1][i],'DELTA',d,'MOD2',res(d))
        for r in range(4):print('A RAIL_ACCOUNT',T,r,'NEG',railaccount(F[0],r),'POS',railaccount(F[1],r))
        for x,y in product(ARCH,range(2)):
            i=ix(x,y,3)
            print('A PORT',T,x,y,'NEG',tuple(old[0][s][u][i] for s,u in ((0,T-1),(1,T),(0,T))),
                  'POS',tuple(old[1][s][u][i] for s,u in ((0,T-1),(1,T),(0,T))))
            if F[0][i]==F[1][i]:continue
            cp=old[1][1][T][i];cn=F[0][i];d=sub(cn,cp)
            tags=old[0][2][T][2*x+y],old[1][2][T][2*x+y]
            aliases=[(u,k) for u,k in product(range(1,T),K) if (T-u)%5==0 and old[k][1][u][i]==cp]
            for tag in (1,2):
                f=mul(d,H.inverse(sub(O,JI if tag==1 else J)))
                integ=all(Q(z).denominator==1 for z in f)
                print('A CORRECTION',T,x,y,tag,'DELTA',d,'F',tuple(map(str,f)),'INTEGER',int(integ),'OLD_TAGS',tags,'ALIAS',aliases[0] if aliases else None)
                if integ and d!=Z:
                    f=tuple(map(int,f));clk=add(cp,sc(2,f));mat=mul(JI if tag==1 else J,f)
                    pp,pt=H.collision(cols(mat,clk,cp))
                    nn,nt=H.collision(cols(mat,clk,old[0][1][T][i]))
                    assert pt==tag and pp[3]==cn
                    print('A HYPOTHETICAL',T,x,y,tag,'CLK',clk,'D',mat,'POS_TAG',pt,'NEG_TAG',nt,'NEG_CORR',nn[3])
        # Exact future interface, comparing first-bit classes at each fixed new q.
        for q in K:
            hh=[hist(replace(F[p],p,q),114,True) for p in (0,1)]
            first={}
            for t in range(1,115):
                for stage in (1,0):
                    n,p=hh[0][stage][t],hh[1][stage][t]
                    for name,part in (('source',src),('worker',worker),('all_corr',cor)):
                        if name not in first and part(n)!=part(p):first[name]=(t,stage)
                    for x,y in product((0,6),range(2)):
                        i=ix(x,y,3);name='port_'+str(x)+'_'+str(y)
                        if stage==1 and name not in first and n[i]!=p[i]:first[name]=(t,stage,n[i],p[i])
            print('A INTERFACE',T,q,'FIRST',sorted(first.items()),'MATCH6',int(all(k not in first or first[k][0]>6 for k in ('source','worker','port_0_0','port_0_1','port_6_0','port_6_1'))),'MATCH114',int(all(k not in first for k in ('source','worker','port_0_0','port_0_1','port_6_0','port_6_1'))))
def passive(q,k,u):
    F=list(replace(old[0][0][114],0,q))
    # A separate supplied memory preparation, not a trajectory from old[0].
    for x,y in product(ARCH,range(2)):
        i=ix(x,y,0);F[i:i+3]=(Z,Z,Z)
    d=P[k];clk=add(F[ix(5,0,3)],u)
    for y,z in enumerate((d,neg(d))):
        i=ix(5,y,0);F[i:i+3]=(z,neg(z),clk)
    return tuple(F)
def B():
    wins=[]
    for s,l in product((1,-1),K):
        u=sc(s,P[l]);first=None;write=reset=0;good=0
        for q in K:
            hh=[hist(passive(q,k,u),160,True) for k in K]
            assert len({w[3] for w in hh})==1
            q0=H.scalar_account(hh[0][3][2])
            for t in range(161):
                for stage in ((0,) if t==0 else (1,0)):
                    FF=[w[stage][t] for w in hh]
                    same=len({(src(f),worker(f),cor(f)) for f in FF})==1
                    separate=len({archive(f) for f in FF})==5
                    idle=t==0 or all(not any(w[2][t][2*x+y] for x,y in product(ARCH,range(2))) for w in hh)
                    if first is None and not (same and separate and idle):first=(q,t,stage,int(same),int(separate),int(idle))
                    if t==160 and stage==0:good+=int(same and separate and idle)
            ww=sum(w[0][6][ix(6,0,2)]==(mark if q==1 else g) and w[0][6][ix(6,1,2)]==g for w in hh)
            rr=sum(ready(w[0][114],w[0][0]) for w in hh)
            write+=ww;reset+=rr
            print('B QCASE',s,l,q,'Q',q0,'WRITE6',ww,'RESET114',rr)
        if first is None:wins.append((s,l))
        print('B STOCK',s,l,'U',u,'FIRST_FAILURE',first,'FINAL_GROUPS_PASS',good,'WRITE6',write,'RESET114',reset)
    print('B WINS',wins)
if __name__=='__main__':
    A();B()
    print('DONE A/B exact interface and supplied passive records')
