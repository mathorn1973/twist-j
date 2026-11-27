"""NON-CANONICAL #2127, result-exposed independent cyclic-five-coefficient audit.
Replays A/B, local C1/C2 enumerations, selected C3 and D. Uses no primary code.
"""
from pathlib import Path
import runpy,hashlib
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
root=Path(__file__).resolve().parent
engine=root/'alternate_predecessor.py'
assert hashlib.sha256(engine.read_bytes()).hexdigest()=='48262b6e7bb600c069952412015385721c894210eec50da11314df792c2ac27e'
E=runpy.run_path(str(engine))
O,Z,R,J,JI,P=map(E.get,('O','Z','R','J','JI','P'))
add,sub,mul,sc,h,even=map(E.get,('add','sub','mul','sc','h','even'))
raw,flat,cell,ix,rs=map(E.get,('raw','flat','cell','ix','rs'))
C,B,trans,hist,acc,scalar=map(E.get,('C','B','trans','hist','acc','scalar'))
seed,src,worker,archive,reader,ret,two=map(E.get,('seed','source','worker','archive','reader','ret','two'))
K=range(5);N=(0,2,3,4);ARCH=(1,2,3,4,5,7)
neg=lambda x:sc(-1,x)
eta=sub(O,R)
bi=sc(Q(2,5),rs((sc(4,O),sc(3,R),sc(2,P[4]),P[1])))
assert mul(sc(Q(1,2),eta),bi)==O
def scale(z):
    v=mul(eta,z);assert all(Q(a).denominator==1 for a in v)
    return tuple(map(int,v))
def Cq(a,b,back=False):
    dif=sub(a,b);assert all(Q(v).denominator%2 for v in dif)
    if any(Q(v).numerator%2 for v in dif):return a,b
    u=mul(P[3] if back else R,dif)
    ans=sc(Q(1,2),add(add(a,b),u)),sc(Q(1,2),sub(add(a,b),u))
    assert all(Q(v).denominator%2 for z in ans for v in z)
    return ans
def rot(pair,n,back=False):
    for _ in range(n%5):pair=Cq(*pair,back)
    return pair
def f_for(delta,tag):
    f=mul(delta,mul(J,P[3]) if tag==1 else neg(P[3]))
    assert mul(sub(O,JI if tag==1 else J),f)==delta
    return f
def dm(f,tag):return mul(JI if tag==1 else J,f)
def ex(tag):return J if tag==1 else JI
def mk(z):return tuple(z)+(0,)
def corr(F):return tuple(c[3] for c in F)
def setup(F,x,d,g):
    f=list(F)
    for y in range(2):f[ix(x,y)]=cell(d[y],g[y],f[ix(x,y)][3])
    return tuple(f)
D=tuple(map(mk,((8,7,1,13),(6,5,-1,11))));G=mk((34,10,21,31))
g=mk((6,-2,12,1));mark=mk((5,-3,11,1))
I=[setup(seed(k,'static'),5,D,(G,G)) for k in K]
old=[hist(f,370) for f in I]
assert len({w[3] for w in old})==1 and scalar(old[0][3][2])==7752
old0=[hist(seed(k,'static'),114) for k in K]
def exchange(F,p,q):
    assert F[0][:2]==(P[p],neg(P[p]))
    out=(cell(P[q],F[0][2],F[0][3]),)+F[1:]
    assert acc(F)==acc(out)
    assert acc(F+(cell(P[q],Z,Z),))==acc(out+(cell(P[p],Z,Z),))
    return out
def A():
    expected={114:((5,0,(0,-6,0,0)),(7,0,(12,6,6,6))),
              198:((5,0,(0,-6,0,0)),(7,0,(12,6,6,6))),
              244:((4,0,(-3,-6,-3,-3)),(5,0,(3,0,3,3)),(7,0,(12,6,6,6)))}
    for t in (114,198,244):
        F=[w[0][t] for w in old]
        assert ret(F,I,src) and ret(F,I,worker) and two(F,archive)
        assert all(acc(archive(f))==acc(archive(I[k])) for k,f in enumerate(F))
        ds=tuple((x,y,raw(sub(F[1][ix(x,y)][3],F[0][ix(x,y)][3]))) for x,y in product(range(8),range(2)) if F[1][ix(x,y)][3]!=F[0][ix(x,y)][3])
        assert ds==expected[t]
        aliases=[]
        for x,y,d in ds:
            delta=neg(mk(d));rp=old[1][1][t][ix(x,y)][3];cn=F[0][ix(x,y)][3]
            assert add(rp,delta)==cn and all(not w[2][t][ix(x,y)] for w in old)
            alias=next(((s,k) for s,k in product(range(1,t),K) if (t-s)%5==0 and old[k][1][s][ix(x,y)][3]==rp),None)
            aliases.append((x,y,alias))
            for tag in (1,2):
                f=f_for(delta,tag);clk=add(rp,sc(2,f));d0=dm(f,tag)
                pos,pt=B(cell(d0,clk,rp));nn,nt=B(cell(d0,clk,old[0][1][t][ix(x,y)][3]))
                assert pt==tag and pos[3]==cn and nt==0
        print('ALT A',t,'DIFF',ds,'ALIASES',aliases)
        for q in K:
            hh=[hist(exchange(F[p],p,q),114) for p in (0,1)]
            first=next(((u,s) for u in range(1,115) for s in (1,0) if (src(hh[0][s][u]),worker(hh[0][s][u]))!=(src(hh[1][s][u]),worker(hh[1][s][u]))),None)
            assert first==((2,1) if q==1 or t==244 else (10,1))
            print('ALT A INTERFACE',t,q,first)
def passive(q,k,u):
    F=list(exchange(old[0][0][114],0,q))
    for x,y in product(ARCH,range(2)):
        i=ix(x,y);F[i]=cell(Z,Z,F[i][3])
    g0=add(F[ix(5,0)][3],u)
    for y,d in enumerate((P[k],neg(P[k]))):
        i=ix(5,y);F[i]=cell(d,g0,F[i][3])
    return tuple(F)
def passive_tests():
    wins=[]
    for s,l in product((1,-1),K):
        u=sc(s,P[l]);first=None;write=reset=0
        for q in K:
            hh=[hist(passive(q,k,u),160) for k in K]
            assert len({w[3] for w in hh})==1
            for t in range(161):
                for st in ((0,) if t==0 else (1,0)):
                    FF=[w[st][t] for w in hh]
                    same=len({(src(f),worker(f),corr(f)) for f in FF})==1
                    separate=len({archive(f) for f in FF})==5
                    idle=t==0 or all(not any(w[2][t][ix(x,y)] for x,y in product(ARCH,range(2))) for w in hh)
                    if first is None and not(same and separate and idle):first=q,t,st,int(same),int(separate),int(idle)
            write+=sum(w[0][6][ix(6,0)][2]==(mark if q==1 else g) and w[0][6][ix(6,1)][2]==g for w in hh)
            reset+=sum(src(w[0][114])==src(w[0][0]) and worker(w[0][114])==worker(w[0][0]) for w in hh)
        assert (write,reset)==(25,20)
        if first is None:wins.append((s,l))
        print('ALT B',s,l,first,write,reset)
    assert wins==[(1,0),(1,1),(1,2),(1,3),(-1,0),(-1,1),(-1,2)]
    print('ALT B WINS',wins)
roots=tuple(sc(s,P[k]) for s,k in product((1,-1),K))
delta=mk((12,0,6,6));delta5=mk((0,6,0,0));delta7=mk((-12,-6,-6,-6))
r=mk((-2,-2,9,-5));c=mk((7,-8,12,-2));c7=mk((7,7,15,7))
def C1():
    first=None
    for a,b in product((1,2),repeat=2):
        f1,f2=f_for(delta,a),f_for(delta5,b)
        g1=add(r,sc(2,f1));post=sub(g1,delta);target=add(c,sc(2,f2))
        gr=add(post,mul(bi,sub(target,post)))
        gs=tuple(map(scale,rot((g1,gr),113,True)))
        count=0
        for s,t in product(roots,repeat=2):
            d1=mul(dm(f1,a),s);dp=mul(ex(a),d1);target=mul(dm(f2,b),t)
            dr=add(dp,mul(bi,sub(target,dp)))
            ds=tuple(map(scale,rot((d1,dr),113,True)))
            dd,gg=ds,gs;ok=True
            for u in range(1,114):
                dd=C(*dd);gg=C(*gg)
                if any(B(cell(dd[y],gg[y],scale(old0[k][1][u][ix(5,y)][3])))[1]!=(a if u==113 and k==1 and y==0 else 0) for k,y in product(K,range(2))):
                    ok=False;break
            if not ok:continue
            for k in K:
                e=tuple(B(cell(dd[y],gg[y],scale(old0[k][1][113][ix(5,y)][3])))[0] for y in range(2))
                dr2=C(e[0][0],e[1][0]);gr2=C(e[0][2],e[1][2])
                zz=tuple(B(cell(dr2[y],gr2[y],scale(old[k][1][114][ix(5,y)][3]))) for y in range(2))
                if tuple(z[1] for z in zz)!=(b if k==1 else 0,0) or zz[0][0][3]!=scale(old[0][0][114][ix(5,0)][3]):
                    ok=False;break
            if ok:
                count+=1
                if first is None:first=ds,gs
        assert count==100
        print('ALT C1',a,b,count)
    ds,gs=first
    assert tuple(map(raw,ds))==((-33,-9,-18,-30),(-15,3,-18,6))
    assert tuple(map(raw,gs))==((-21,-8,5,-36),(3,28,-19,30))
    II=[setup(tuple(tuple(scale(z) for z in c0) for c0 in seed(k,'static')),5,ds,gs) for k in K]
    hh=[hist(f,114) for f in II];F=[w[0][114] for w in hh]
    assert ret(F,II,src) and ret(F,II,worker) and two(F,archive) and scalar(hh[0][3][2])==18202
    assert [(x,y) for x,y in product(range(8),range(2)) if F[0][ix(x,y)][3]!=F[1][ix(x,y)][3]]==[(7,0)]
    assert all(acc(archive(f))==acc(archive(II[k])) for k,f in enumerate(F))
    print('ALT C1 SELECT',tuple(map(raw,ds)),tuple(map(raw,gs)),18202)
    return ds,gs
def vert(ds,bit,back=False):
    out=list(ds);n=len(ds)
    for y in range(bit,n,2):
        z=(y+1)%n;out[y],out[z]=C(ds[y],ds[z],back)
    return tuple(out)
def backvertical(ds,t):
    for u in range(t,0,-1):ds=vert(ds,(u-1)%2,True)
    return ds
def C2():
    first=None;ws=(Z,)+roots
    want={(6,1):240,(6,2):282,(8,1):121,(8,2):134}
    for ny,tag in product((6,8),(1,2)):
        f=f_for(delta7,tag);g0=add(c7,sc(2,f));d=dm(f,tag);stats=Counter()
        for k,u,v in product(K,ws,ws):
            goal=tuple((mul(d,P[k]) if y==0 else d) if y%2==0 else add(d,sc(2,v if y==1 else u)) for y in range(ny))
            init=backvertical(goal,114);ds=init;ok=True
            for t in range(1,115):
                ds=vert(ds,(t-1)%2)
                if any(B(cell(ds[y],g0,old[p][1][t][ix(7,y%2)][3]))[1]!=(tag if t==114 and p==1 and y%2==0 else 0) for p,y in product(K,range(ny))):
                    stats['guard_first_'+str(t)]+=1;ok=False;break
            if ok:
                assert ds==goal
                stats['pass']+=1
                if first is None:first=ny,tag,init,g0
        assert stats['pass']==want[ny,tag] and sum(stats.values())==605
        print('ALT C2',ny,tag,sorted(stats.items()))
    assert first[0:2]==(6,1)
    assert tuple(map(raw,first[2]))==((1,0,6,-7),(2,0,6,-6),(1,2,7,-5),(-1,0,5,-7),(0,0,6,-6),(1,0,6,-5))
    assert raw(first[3])==(-17,-5,15,-17)
    return first
def ixn(ny,x,y):return ny*x+y
def col(ny,F,x):return F[ny*x:ny*(x+1)]
def arch(ny,F):return tuple(c0 for x in ARCH for c0 in col(ny,F,x))
def read(ny,F):return F[ny:]
def ttrans(F,ny,bit,back=False):
    out=[list(c0) for c0 in F]
    for x,y in product(range(8),range(bit,ny,2)):
        i,z=ixn(ny,x,y),ixn(ny,x,(y+1)%ny)
        for r in range(3):out[i][r],out[z][r]=C(F[i][r],F[z][r],back)
    for x,y in product(range(bit,8,2),range(ny)):
        i,z=ixn(ny,x,y),ixn(ny,(x+1)%8,y)
        out[i][3],out[z][3]=C(F[i][3],F[z][3],back)
    return tuple(tuple(c0) for c0 in out)
def thist(F,ny,n):
    ac=acc(F);cut=[F];mid=[None];tags=[None]
    for t in range(1,n+1):
        G0=ttrans(F,ny,(t-1)%2)
        b0=tuple(B(c0) for c0 in G0);N0=tuple(v[0] for v in b0);tt=tuple(v[1] for v in b0)
        back=tuple(B(c0)[0] for c0 in N0)
        assert back==G0 and ttrans(back,ny,(t-1)%2,True)==F and acc(G0)==acc(N0)==ac
        cut.append(N0);mid.append(G0);tags.append(tt);F=N0
    return cut,mid,tags,ac
def make_tall(p,ny,d7,g7,c1=None):
    F=[]
    for x,y in product(range(8),range(ny)):
        c0=I[p][ix(x,y%2)] if c1 is None else tuple(scale(z) for z in seed(p,'static')[ix(x,y%2)])
        if x==5 and c1 is not None:c0=cell(c1[0][y%2],c1[1][y%2],c0[3])
        if x==7:c0=cell(d7[y],g7,c0[3]) if c1 is None else cell(scale(d7[y]),scale(g7),c0[3])
        F.append(c0)
    return tuple(F)
keys=tuple(product(range(2),K));reps=tuple(product(range(2),range(2)))
def parts(F,part,keyfn=lambda k:(k[0],int(k[1]==1))):
    out={}
    for k,f in F.items():out.setdefault(keyfn(k),set()).add(part(f))
    return out
def disj(pp):return all(a.isdisjoint(b) for a,b in combinations(pp.values(),2))
def clean(pp):return disj(pp) and all(len(v)==1 for v in pp.values())
def tall(c1,c2):
    ny,tag,d7,g7=c2
    II=[make_tall(p,ny,d7,g7) for p in K]
    hh=[thist(f,ny,114) for f in II]
    F=[w[0][114] for w in hh]
    assert all(col(ny,f,0)==col(ny,II[p],0) and col(ny,f,6)==col(ny,II[p],6) and acc(arch(ny,f))==acc(arch(ny,II[p])) for p,f in enumerate(F))
    assert [(x,y) for x,y in product(range(8),range(ny)) if F[0][ixn(ny,x,y)][3]!=F[1][ixn(ny,x,y)][3]]==[(5,y) for y in range(0,ny,2)]
    assert scalar(hh[0][3][2])==36156
    print('ALT C2 FULL',36156)
    II=[make_tall(p,ny,d7,g7,c1) for p in K]
    hh=[thist(f,ny,114) for f in II]
    F=[w[0][114] for w in hh]
    source=lambda f:col(ny,f,0);worker=lambda f:col(ny,f,6);archive=lambda f:arch(ny,f)
    assert all(source(f)==source(II[p]) and worker(f)==worker(II[p]) and acc(archive(f))==acc(archive(II[p])) for p,f in enumerate(F))
    assert len({corr(f) for f in F})==1 and all(corr(f)==corr(II[0]) for f in F)
    assert len({archive(F[p]) for p in N})==1 and archive(F[0])!=archive(F[1])
    assert len({w[3] for w in hh})==1 and scalar(hh[0][3][2])==80436
    print('ALT C3 FIRST',80436,len(corr(F[0])))
    def load(p,q):
        f=list(F[p])
        for y in range(0,ny,2):
            i=ixn(ny,0,y);assert f[i][:2]==(scale(P[p]),scale(neg(P[p])))
            f[i]=cell(scale(P[q]),f[i][2],f[i][3])
        assert acc(f)==acc(F[p]);return tuple(f)
    all25={(p,q):load(p,q) for p,q in product(K,repeat=2)}
    ff={k:all25[k] for k in keys}
    assert len(set(ff.values()))==10 and all(f==ff[int(p==1),q] for (p,q),f in all25.items())
    hs={k:thist(f,ny,512) for k,f in ff.items()}
    for k,w in hs.items():
        assert all(w[0][6][ixn(ny,6,y)][2]==scale(mark if k[1]==1 and y%2==0 else g) for y in range(ny))
    first_hist=split=loss=None;four=[];resets=[];hids={k:k[0] for k in keys}
    for t in range(513):
        for st in ((0,) if t==0 else (1,0)):
            FF={k:w[st][t] for k,w in hs.items()}
            if loss is None and not disj(parts(FF,archive,lambda k:k[0])):loss=t,st
            vals={k:(hids[k],read(ny,f)) for k,f in FF.items()}
            pp=parts(vals,lambda x:x)
            if first_hist is None and clean(pp):first_hist=t,st
            if split is None and any(len(v)>1 for v in pp.values()):split=t,st
            ids={v:i for i,v in enumerate(dict.fromkeys(vals.values()))}
            hids={k:ids[v] for k,v in vals.items()}
            if st==0 and t>=2 and t%2==0:
                if clean(parts(FF,archive)):four.append(t)
                if all(source(f)==source(II[k[1]]) and worker(f)==worker(II[k[1]]) for k,f in FF.items()):resets.append(t)
    assert first_hist==(2,1) and split is None and loss is None and len(four)==256 and not resets
    print('ALT C3 SECOND','WRITE',25,'FOUR',len(four),'HIST',first_hist,'SPLIT',split,'LOSS',loss,'RESETS',resets)
    for q in K:
        first=next(((t,s) for t in range(1,513) for s in (1,0) if (source(hs[0,q][s][t]),worker(hs[0,q][s][t]))!=(source(hs[1,q][s][t]),worker(hs[1,q][s][t]))),None)
        assert first==((116,1) if q==1 else (6,1))
        print('ALT D INTERFACE',q,first)
    values=[]
    for k in reps:
        f=hs[k][0][114];i=II[k[1]]
        assert source(f)==source(i)
        assert (worker(f)==worker(i))==(k==(0,0))
        values.append(raw(f[ixn(ny,7,2)][2]))
        print('ALT D END',k,tuple(tuple(raw(sub(a,b)) for a,b in zip(acc(part(f)),acc(part(i)))) for part in (source,worker,archive)))
    assert values==[(15,10,47,3),(24,16,53,12),(18,19,50,3),(15,13,41,6)]
    print('ALT D READ',values)
def alltime_passive():
    q=lambda z:scalar(h(z))
    assert q(J)==q(JI)==3 and q(sc(64,O))==8192>2*2630+24
    for q0 in K:
        F=list(passive(q0,0,O))
        for x,y in product(ARCH,range(2)):
            i=ix(x,y);F[i]=cell(Z,Z,F[i][3])
        F=tuple(F);assert scalar(acc(F)[2])==2630
        bh=hist(F,160);ph=[]
        for k in K:
            z=setup(F,5,(P[k],neg(P[k])),(sc(64,O),sc(64,O)))
            ph.append(hist(z,160))
        assert len({w[3] for w in ph})==1 and scalar(ph[0][3][2])==19022
        for t in range(161):
            for st in ((0,) if t==0 else (1,0)):
                ref=bh[st][t]
                ff=[w[st][t] for w in ph]
                assert all((src(f),worker(f),corr(f))==(src(ref),worker(ref),corr(ref)) for f in ff)
                assert len({archive(f) for f in ff})==5
                assert all(f[ix(5,0)][0]==P[(k+2*t)%5] and f[ix(5,1)][0]==neg(P[(k+2*t)%5]) for k,f in enumerate(ff))
        print('ALT D PASSIVE',q0,19022)
if __name__=='__main__':
    A();passive_tests();c1=C1();c2=C2();tall(c1,c2);alltime_passive()
    print('PASS alternate independent ring A/B/C and selected D')
