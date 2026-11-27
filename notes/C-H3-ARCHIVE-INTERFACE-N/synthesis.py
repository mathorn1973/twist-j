"""NON-CANONICAL #2127 C1/C2: inverse-synthesized two-column corrections."""
from pathlib import Path
import runpy
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
seed,cols,hist,step,account,ix=map(V.get,('seed','cols','hist','step','account','ix'))
src,worker,archive,reader,cor=map(V.get,('src','worker','archive','reader','cor'))
K=range(5);N=(0,2,3,4);ARCH=V['ARCH']
eta=sub(O,R);BI=H.inverse(sc(Q(1,2),eta))
def ints(z):
    assert all(Q(v).denominator==1 for v in z),z
    return tuple(map(int,z))
def scale(z):return ints(mul(eta,z))
assert not H.even(eta) and H.mul(eta,H.inverse(eta))==O
def rational_even(z):
    assert all(Q(v).denominator%2 for v in z)
    return all(Q(v).numerator%2==0 for v in z)
def rational_C(a,b,back=False):
    dif=sub(a,b)
    if not rational_even(dif):return a,b
    u=mul(H.RHO_INV if back else R,dif)
    ans=(sc(Q(1,2),add(add(a,b),u)),sc(Q(1,2),sub(add(a,b),u)))
    assert all(Q(v).denominator%2 for z in ans for v in z)
    return ans
def rot(pair,n,back=False):
    for _ in range(n%5):pair=rational_C(*pair,back)
    return pair
def ratio(delta,tag):
    return ints(mul(delta,H.inverse(sub(O,JI if tag==1 else J))))
def dm(f,tag):return mul(JI if tag==1 else J,f)
def ex(tag):return J if tag==1 else JI
def tags_expected(k,tag):return (tag if k==1 else 0,0)
def same_neg(F,part):return len({part(F[k]) for k in N})==1
def two(F,part):return same_neg(F,part) and part(F[1])!=part(F[0])
old0=[hist(seed(k,'static'),114,True) for k in K]
old=V['old'];oldcuts=[w[0][114] for w in old]
delta=(12,0,6,6);delta5=(0,6,0,0);delta7=(-12,-6,-6,-6)
r=(-2,-2,9,-5);c=(7,-8,12,-2);c7=(7,7,15,7)
assert old[1][1][114][ix(5,0,3)]==c and old[1][1][114][ix(7,0,3)]==c7
roots=tuple(sc(s,P[k]) for s,k in product((1,-1),K))
def prep5(F,d,g):
    F=list(F)
    for y in range(2):
        i=ix(5,y,0);F[i:i+3]=(d[y],neg(d[y]),g[y])
    return tuple(F)
def C1():
    stats=Counter();first=None
    for a,b in product((1,2),repeat=2):
        f1,f2=ratio(delta,a),ratio(delta5,b)
        g1=add(r,sc(2,f1));g1p=sub(g1,delta);g2=add(c,sc(2,f2))
        gother=add(g1p,mul(BI,sub(g2,g1p)))
        gs=tuple(map(scale,rot((g1,gother),113,True)))
        local=Counter()
        for si,ti in product(range(10),repeat=2):
            d1=mul(dm(f1,a),roots[si]);d1p=mul(ex(a),d1);d2=mul(dm(f2,b),roots[ti])
            dother=add(d1p,mul(BI,sub(d2,d1p)))
            ds=tuple(map(scale,rot((d1,dother),113,True)))
            local['tried']+=1;dd=ds;gg=gs;ok=True
            for t in range(1,114):
                dd=H.transport_pair(*dd,False);gg=H.transport_pair(*gg,False)
                for k,y in product(K,range(2)):
                    z=scale(old0[k][1][t][ix(5,y,3)])
                    tag=H.collision(cols(dd[y],gg[y],z))[1]
                    if tag!=(a if t==113 and k==1 and y==0 else 0):
                        ok=False;break
                if not ok:
                    local['guard_first_'+str(t)]+=1;break
            if not ok:continue
            assert dd==tuple(map(scale,(d1,dother))) and gg==tuple(map(scale,(g1,gother)))
            # The first compensating write yields exactly the old #2124 CORR at114.
            for k in K:
                e=tuple(H.collision(cols(dd[y],gg[y],scale(old0[k][1][113][ix(5,y,3)])))[0] for y in range(2))
                dd2=H.transport_pair(e[0][0],e[1][0],False)
                gg2=H.transport_pair(e[0][2],e[1][2],False)
                b2=tuple(H.collision(cols(dd2[y],gg2[y],scale(old[k][1][114][ix(5,y,3)]))) for y in range(2))
                if tuple(z[1] for z in b2)!=tags_expected(k,b) or b2[0][0][3]!=scale(old[0][0][114][ix(5,0,3)]):
                    ok=False;break
            if not ok:
                local['guard_second']+=1;continue
            local['pass']+=1
            if first is None:first=(a,b,si,ti,ds,gs)
        stats.update(local)
        print('C1 TAGS',a,b,sorted(local.items()))
    print('C1 COUNTS',sorted(stats.items()))
    if first is None:
        print('C1 NO WITNESS');return None
    a,b,si,ti,d,g=first
    print('C1 SELECT',first)
    I=[prep5(tuple(map(scale,seed(k,'static'))),d,g) for k in K]
    hh=[hist(f,114,True) for f in I]
    assert len({w[3] for w in hh})==1
    F=[w[0][114] for w in hh]
    for k,w in enumerate(hh):
        assert src(F[k])==src(I[k]) and worker(F[k])==worker(I[k])
        for t in range(1,113):
            assert tuple(map(scale,old0[k][0][t][3::4]))==w[0][t][3::4]
        assert w[2][113][10:12]==tags_expected(k,a)
        assert w[2][114][10:12]==tags_expected(k,b)
        assert F[k][ix(5,0,3)]==scale(old[0][0][114][ix(5,0,3)])
        assert account(archive(F[k]))==account(archive(I[k]))
    assert [i for i in range(len(F[0])) if i%4==3 and F[0][i]!=F[1][i]]==[ix(7,0,3)]
    assert two(F,archive)
    assert all(same_neg([w[s][t] for w in hh],reader) for t in range(115) for s in ((0,) if t==0 else (1,0)))
    print('C1 PASS','Q',H.scalar_account(hh[0][3][2]),'CORR_DIFFS',[(7,0,sub(F[1][ix(7,0,3)],F[0][ix(7,0,3)]))])
    return first
def vertical(ds,bit,back=False):
    out=list(ds);n=len(ds)
    for y in range(bit,n,2):
        k=(y+1)%n;out[y],out[k]=H.transport_pair(ds[y],ds[k],back)
    return tuple(out)
def backvertical(ds,n):
    for t in range(n,0,-1):ds=vertical(ds,(t-1)%2,True)
    return ds
def index(ny,x,y,r):return H.index(ny,x,y,r)
def initial_tall(k,ny,d7,g7):
    f=V['I'](k);F=[]
    for x,y in product(range(8),range(ny)):
        i=ix(x,y%2,0);c=f[i:i+4]
        if x==7:c=cols(d7[y],g7,c[3])
        F.extend(c)
    return tuple(F)
def col(ny,F,x):
    i=index(ny,x,0,0);return F[i:i+4*ny]
def ar(ny,F):
    return tuple(z for x in ARCH for z in col(ny,F,x))
def rd(ny,F):return F[4*ny:]
def tall_hist(F,ny,n):
    ac=account(F);cut=[F];mid=[None];tags=[None]
    for t in range(n):
        G=H.transport(F,ny,t%2);N0,ev=H.collide(G,ny)
        back,_=H.collide(N0,ny)
        assert back==G and H.transport(back,ny,t%2,True)==F and account(G)==account(N0)==ac
        cut.append(N0);mid.append(G);tags.append(dict(((x,y),tag) for x,y,tag in ev));F=N0
    return cut,mid,tags,ac
def C2():
    stats=Counter();first=None;ws=(Z,)+roots
    # Incoming radiation through the cut is independent of the new clock
    # provided every earlier local B is idle.
    for ny,tag in product((6,8),(1,2)):
        f=ratio(delta7,tag);g=add(c7,sc(2,f));d=dm(f,tag)
        local=Counter()
        for k,ui,vi in product(K,range(11),range(11)):
            u,v=ws[ui],ws[vi]
            goal=tuple((mul(d,P[k]) if y==0 else d) if y%2==0 else add(d,sc(2,v if y==1 else u)) for y in range(ny))
            init=backvertical(goal,114);ds=init;ok=True
            local['tried']+=1
            for t in range(1,115):
                ds=vertical(ds,(t-1)%2)
                for p,y in product(K,range(ny)):
                    z=old[p][1][t][ix(7,y%2,3)]
                    tt=H.collision(cols(ds[y],g,z))[1]
                    if tt!=(tag if t==114 and p==1 and y%2==0 else 0):
                        ok=False;break
                if not ok:local['guard_first_'+str(t)]+=1;break
            if ok:
                assert ds==goal
                local['pass']+=1
                if first is None:first=(ny,tag,k,ui,vi,init,g)
        stats.update(local)
        print('C2 GROUP',ny,tag,sorted(local.items()))
    print('C2 COUNTS',sorted(stats.items()))
    if first is None:
        print('C2 NO WITNESS');return None
    ny,tag,k,ui,vi,d,g=first
    print('C2 SELECT',first)
    I=[initial_tall(p,ny,d,g) for p in K]
    hh=[tall_hist(f,ny,114) for f in I]
    F=[w[0][114] for w in hh]
    assert len({w[3] for w in hh})==1
    for p,w in enumerate(hh):
        assert col(ny,F[p],0)==col(ny,I[p],0) and col(ny,F[p],6)==col(ny,I[p],6)
        for t in range(1,114):
            assert not any(x==7 for x,y in w[2][t])
        assert all(w[2][114].get((7,y),0)==(tag if p==1 and y%2==0 else 0) for y in range(ny))
        assert account(ar(ny,F[p]))==account(ar(ny,I[p]))
    diff=[(x,y) for x,y in product(range(8),range(ny)) if F[0][index(ny,x,y,3)]!=F[1][index(ny,x,y,3)]]
    assert diff==[(5,y) for y in range(0,ny,2)]
    assert two(F,lambda f:ar(ny,f))
    assert all(same_neg([w[s][t] for w in hh],lambda f:rd(ny,f)) for t in range(115) for s in ((0,) if t==0 else (1,0)))
    print('C2 PASS','Q',H.scalar_account(hh[0][3][2]),'CORR_DIFFS',diff)
    return first
def C3(first,second):
    if first is None or second is None:
        print('C3 NOT RUN: missing component');return
    a,b,si,ti,d5,g5=first
    ny,tag,k,ui,vi,d7,g7=second
    I=[]
    for p in K:
        F=[]
        for x,y in product(range(8),range(ny)):
            i=ix(x,y%2,0);c=tuple(map(scale,seed(p,'static')[i:i+4]))
            if x==5:c=cols(d5[y%2],g5[y%2],c[3])
            if x==7:c=cols(scale(d7[y]),scale(g7),c[3])
            F.extend(c)
        I.append(tuple(F))
    hh=[tall_hist(f,ny,114) for f in I];F=[w[0][114] for w in hh]
    assert len({w[3] for w in hh})==1
    for p,w in enumerate(hh):
        assert col(ny,F[p],0)==col(ny,I[p],0) and col(ny,F[p],6)==col(ny,I[p],6)
        assert account(ar(ny,F[p]))==account(ar(ny,I[p]))
    assert len({cor(f) for f in F})==1
    assert two(F,lambda f:ar(ny,f))
    assert all(same_neg([w[s][t] for w in hh],lambda f:rd(ny,f)) for t in range(115) for s in ((0,) if t==0 else (1,0)))
    print('C3 FIRST PASS','NY',ny,'Q',H.scalar_account(hh[0][3][2]))
    def exchange(p,q):
        f=list(F[p])
        for y in range(0,ny,2):
            i=index(ny,0,y,0);assert f[i:i+2]==[scale(P[p]),scale(neg(P[p]))]
            f[i:i+2]=[scale(P[q]),scale(neg(P[q]))]
        assert account(f)==account(F[p])
        return tuple(f)
    keys=tuple(product(range(2),K))
    all25={(p,q):exchange(p,q) for p,q in product(K,repeat=2)}
    ff={k:all25[k] for k in keys}
    assert len(set(ff.values()))==10 and all(f==ff[int(p==1),q] for (p,q),f in all25.items())
    hs={k:tall_hist(f,ny,512) for k,f in ff.items()}
    def parts(F,part,keyfn):
        pp={}
        for k,f in F.items():pp.setdefault(keyfn(k),set()).add(part(f))
        return pp
    def disj(pp):return all(a.isdisjoint(b) for a,b in combinations(pp.values(),2))
    held=True;firstloss=None;wins=[];resets=[]
    count=0
    for k,w in hs.items():
        a0,q=k;v=w[0][6]
        count+=(1 if a0 else 4)*int(all(v[index(ny,6,y,2)]==scale(V['mark'] if q==1 and y%2==0 else V['g']) for y in range(ny)))
    print('C3 WRITE6',count)
    for t in range(513):
        for s in ((0,) if t==0 else (1,0)):
            A={k:w[s][t] for k,w in hs.items()}
            if held and not disj(parts(A,lambda f:ar(ny,f),lambda k:k[0])):held=False;firstloss=(t,s)
        if t<2 or t%2:continue
        if not all(col(ny,w[0][t],0)==col(ny,I[k[1]],0) and col(ny,w[0][t],6)==col(ny,I[k[1]],6) for k,w in hs.items()):continue
        resets.append(t)
        A={k:w[0][t] for k,w in hs.items()}
        pp=parts(A,lambda f:ar(ny,f),lambda k:(k[0],int(k[1]==1)))
        if held and disj(pp) and all(len(v)==1 for v in pp.values()):wins.append(t)
    print('C3 SUMMARY','RESETS',resets,'WINS',wins,'FIRST_LOSS',firstloss)
if __name__=='__main__':
    first=C1();second=C2();C3(first,second)
    print('DONE C exact inverse synthesis')
