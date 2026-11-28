"""NON-CANONICAL #2131. Integrated native absorbing archive; exact local census."""
import sys,hashlib,importlib.util
from pathlib import Path
from itertools import product,combinations
from functools import cache
from fractions import Fraction as Q
from collections import Counter
source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H;spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,R,J,JI,P=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV,H.J_POWERS
add,sub,mul,sc,h=H.add,H.sub,cache(H.mul),H.scale,H.h
neg=lambda x:sc(-1,x)
L=sub(O,R);BI=H.inverse(sc(Q(1,2),L))
assert mul(BI,sc(Q(1,2),L))==O and not H.even(L)
K=range(5);N=(0,2,3,4);BITS=range(2);ARCH=(1,2,3,4,5,7)
ROOTS=tuple(sc(s,P[k]) for s,k in product((1,-1),K));WS=(Z,)+ROOTS
ix=lambda ny,x,y,r:H.index(ny,x,y,r)
def cols(d,g,c):return d,neg(d),g,c
def account(F):
    return H.ring_sum(z for i,z in enumerate(F) if i%4<2),H.ring_sum(z for i,z in enumerate(F) if i%4>=2),H.ring_sum(h(z) for z in F)
def step(F,ny,bit,ac):
    G=H.transport(F,ny,bit);V,ev=H.collide(G,ny)
    back,_=H.collide(V,ny)
    assert back==G and H.transport(back,ny,bit,True)==F and account(G)==account(V)==ac
    return G,V,ev
def hist(F,ny,n):
    ac=account(F);cut=[F];mid=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,ny,t%2,ac);cut.append(F);mid.append(G);tags.append(E)
    return cut,mid,tags,ac
def ints(z):
    assert all(Q(v).denominator==1 for v in z)
    return tuple(map(int,z))
def scale(z):return ints(mul(L,z))
def col(F,ny,x):return F[4*ny*x:4*ny*(x+1)]
def arch(F,ny):return tuple(z for x in ARCH for z in col(F,ny,x))
def read(F,ny):return F[4*ny:]
def corr(F):return F[3::4]
def material(F,ny,x):return tuple(F[ix(ny,x,y,0)] for y in range(ny))
def clk(F,ny,x):return tuple(F[ix(ny,x,y,2)] for y in range(ny))
def mem(F,ny,x):return material(F,ny,x),clk(F,ny,x)
def same_neg(F,part):return len({part(F[k]) for k in N})==1
def two(F,part):return same_neg(F,part) and part(F[1])!=part(F[0])
def vert(v,bit,back=False):
    a=list(v);ny=len(v)
    for y in range(bit,ny,2):
        k=(y+1)%ny;a[y],a[k]=H.transport_pair(v[y],v[k],back)
    return tuple(a)
def back(v,n):
    for t in range(n,0,-1):v=vert(v,(t-1)%2,True)
    return v
def ratio(d,tag):return ints(mul(d,H.inverse(sub(O,JI if tag==1 else J))))
def dm(f,tag):return mul(JI if tag==1 else J,f)
def ex(tag):return J if tag==1 else JI
m=sub(sc(2,O),R);gs=sc(2,mul(J,m));a=sc(-3,L)
b=add(add(mul(m,R),mul(J,a)),sc(12,J))
stock=(Z,Z,Z,b,b,b,add(mul(m,R),sc(2,a)))
gworker=(6,-2,12,1);mark=(5,-3,11,1)
def base(p,old=False):
    F=[]
    for x,y in product(range(8),range(2)):
        d=(P[p] if y==0 else sc(3,P[1])) if x==0 else JI if x==6 else Z
        g=gs if x==0 else gworker if x==6 else Z
        c=(Z if x==0 else stock[x-1]) if y==0 else gs
        if old and x==5:d=((8,7,1,13),(6,5,-1,11))[y];g=(34,10,21,31)
        F.extend(cols(d,g,c))
    return tuple(F)
Rhist=[hist(base(p),2,512) for p in K]
Ohist=[hist(base(p,True),2,114) for p in K]
assert len({w[3] for w in Rhist})==1 and H.scalar_account(Rhist[0][3][2])==2630
assert len({w[3] for w in Ohist})==1 and H.scalar_account(Ohist[0][3][2])==7752
for t in range(513):
    for stage in ((0,) if t==0 else (1,0)):
        assert len({read(Rhist[p][stage][t],2) for p in N})==1
for t in range(115):
    for stage in ((0,) if t==0 else (1,0)):
        assert len({read(Ohist[p][stage][t],2) for p in N})==1
delta=(12,0,6,6);delta5=(0,6,0,0);delta7=(-12,-6,-6,-6)
r=(-2,-2,9,-5);c=(7,-8,12,-2);c7=(7,7,15,7)
assert Rhist[1][1][113][ix(2,5,0,3)]==r
assert Ohist[1][1][114][ix(2,5,0,3)]==c and Ohist[1][1][114][ix(2,7,0,3)]==c7
for p in K:
    for x in (0,6):assert col(Ohist[p][0][114],2,x)==col(base(p),2,x)
    assert Ohist[p][0][114][ix(2,5,0,3)]==add(base(p)[ix(2,5,0,3)],neg(delta5) if p==1 else Z)
    assert Ohist[p][0][114][ix(2,7,0,3)]==add(base(p)[ix(2,7,0,3)],neg(delta7) if p==1 else Z)
def incoming(hs,x,t,p,y):return scale(hs[p][1][t][ix(2,x,y%2,3)])
# Unique radiation values, with the first raw-input representative. The
# negative classes are verified equal above; retain explicit q in failures.
def uniq(hs,x,t,y):
    return tuple(dict.fromkeys(incoming(hs,x,t,p,y) for p in K))
FIRST5={t:tuple(uniq(Rhist,5,t,y) for y in range(2)) for t in range(1,113)}
FIRST7={t:tuple(uniq(Ohist,7,t,y) for y in range(2)) for t in range(1,114)}
FUTURE={x:{t:tuple(uniq(Rhist,x,t,y) for y in range(2)) for t in range(1,513)} for x in (5,7)}
def local(d,g,c):return H.collision(cols(d,g,c))
def quiet(d,g,cs):
    return all(local(d,g,z)[1]==0 for z in cs)
def firstquiet(d,g,cs):
    return all(quiet(d[y],g[y],cs[y%2]) for y in range(len(d)))
def c5prep(ny,a,b,s,t,e):
    f1,f2=ratio(delta,a),ratio(delta5,b)
    g1=add(r,sc(2,f1));postg=sub(g1,delta);g2=add(c,sc(2,f2))
    gr=add(postg,mul(BI,sub(g2,postg)))
    dd=[None]*ny;gg=[None]*ny
    for y in range(0,ny,2):
        d1=mul(dm(f1,a),s if y==0 else O)
        d2=mul(dm(f2,b),t if y==e else O)
        dp=mul(ex(a),d1)
        dd[y]=d1;dd[(y-1)%ny]=add(dp,mul(BI,sub(d2,dp)))
        gg[y]=g1;gg[(y-1)%ny]=gr
    ready=tuple(map(scale,dd)),tuple(map(scale,gg))
    return (back(ready[0],113),back(ready[1],113)),ready
def c5test(ny,a,b,s,t,e):
    ini,ready=c5prep(ny,a,b,s,t,e)
    d,g=ini
    for u in range(1,114):
        d,g=vert(d,(u-1)%2),vert(g,(u-1)%2)
        if u<113 and not firstquiet(d,g,FIRST5[u]):return None,('first',u)
    assert (d,g)==ready
    post=[]
    for p in K:
        c1=tuple(local(d[y],g[y],incoming(Rhist,5,113,p,y)) for y in range(ny))
        if tuple(z[1] for z in c1)!=tuple(a if p==1 and y%2==0 else 0 for y in range(ny)):return None,('write113',p)
        for y,(z,tag) in enumerate(c1):
            old=incoming(Rhist,5,113,p,y)
            assert z[3]==add(old,scale(delta) if tag else Z)
        d2=vert(tuple(z[0][0] for z in c1),1);g2=vert(tuple(z[0][2] for z in c1),1)
        c2=tuple(local(d2[y],g2[y],incoming(Ohist,5,114,p,y)) for y in range(ny))
        if tuple(z[1] for z in c2)!=tuple(b if p==1 and y%2==0 else 0 for y in range(ny)):return None,('write114',p)
        assert all(z[0][3]==scale(base(p)[ix(2,5,y%2,3)]) for y,z in enumerate(c2))
        post.append((tuple(z[0][0] for z in c2),tuple(z[0][2] for z in c2)))
    assert same_neg(post,lambda z:z)
    return (ini,(post[0],post[1])),None
def c7test(ny,tag,k,ui,vi):
    f=ratio(delta7,tag);d0=dm(f,tag);g0=add(c7,sc(2,f));u,v=WS[ui],WS[vi]
    goal=tuple((mul(d0,P[k]) if y==0 else d0) if y%2==0 else add(d0,sc(2,v if y==1 else u)) for y in range(ny))
    goal=tuple(map(scale,goal));g=tuple(scale(g0) for _ in range(ny));ini=(back(goal,114),g);d=ini[0]
    for t in range(1,115):
        d=vert(d,(t-1)%2)
        if t<114 and not firstquiet(d,g,FIRST7[t]):return None,('first',t)
    assert d==goal
    post=[]
    for p in K:
        cc=tuple(local(d[y],g[y],incoming(Ohist,7,114,p,y)) for y in range(ny))
        if tuple(z[1] for z in cc)!=tuple(tag if p==1 and y%2==0 else 0 for y in range(ny)):return None,('write114',p)
        assert all(z[0][3]==scale(base(p)[ix(2,7,y%2,3)]) for y,z in enumerate(cc))
        post.append((tuple(z[0][0] for z in cc),tuple(z[0][2] for z in cc)))
    assert same_neg(post,lambda z:z)
    return (ini,(post[0],post[1])),None
def hold(x,post):
    if post[0][0]==post[1][0]:return -1,('no_material_record',)
    now=post
    for t in range(1,513):
        now=tuple((vert(d,(t-1)%2),vert(g,(t-1)%2)) for d,g in now)
        assert now[0][0]!=now[1][0]
        cs=FUTURE[x][t]
        for a,(d,g) in enumerate(now):
            for y in range(len(d)):
                if not quiet(d[y],g[y],cs[y%2]):
                    q,tag=next((q,local(d[y],g[y],incoming(Rhist,x,t,q,y))[1]) for q in K if local(d[y],g[y],incoming(Rhist,x,t,q,y))[1])
                    return t-1,(t,a,q,y,tag)
    return 512,None
def report(label,rr,reject):
    histo=Counter(r['hold'] for r in rr)
    best=max(rr,key=lambda r:r['hold']) if rr else None
    print('CENSUS',label,'ADMITTED',len(rr),'REJECT',sorted(reject.items()),'HOLD',sorted(histo.items()),
          'GE114',sum(n for h,n in histo.items() if h>=114),'GE228',sum(n for h,n in histo.items() if h>=228),'FULL512',histo[512])
    if best:print('BEST',label,best['id'],best['hold'],best['fail'])
def census5(ny,ext):
    rr=[];reject=Counter()
    for a,b,si,ti,e in product((1,2),(1,2),range(10),range(10),(0,2) if ext else (0,)):
        res,err=c5test(ny,a,b,ROOTS[si],ROOTS[ti],e)
        if err:reject[err]+=1;continue
        ini,post=res;v,fail=hold(5,post)
        rr.append(dict(id=(ny,a,b,si,ti,e),ini=ini,post=post,hold=v,fail=fail))
    report(('B5' if ext else 'A5',ny),rr,reject)
    assert len(rr)+sum(reject.values())==(800 if ext else 400)
    if not ext:assert len(rr)==400
    return rr
def census7(ny):
    rr=[]
    for tag in (1,2):
        rec=[];reject=Counter()
        for k,ui,vi in product(K,range(11),range(11)):
            res,err=c7test(ny,tag,k,ui,vi)
            if err:reject[err]+=1;continue
            ini,post=res;v,fail=hold(7,post)
            rec.append(dict(id=(ny,tag,k,ui,vi),ini=ini,post=post,hold=v,fail=fail))
        assert len(rec)+sum(reject.values())==605
        assert len(rec)=={(6,1):240,(6,2):282,(8,1):121,(8,2):134}[ny,tag]
        report(('A7',ny,tag),rec,reject);rr+=rec
    return rr
def select(l5,l7):
    out=[]
    for ny in (6,8):
        if not l5[ny] or not l7[ny]:continue
        best=min(max(z['hold'] for z in l5[ny]),max(z['hold'] for z in l7[ny]))
        a=next(z for z in l5[ny] if z['hold']>=best)
        b=next(z for z in l7[ny] if z['hold']>=best)
        out.append((best,ny,a,b))
    return max(out,key=lambda z:z[0]) if out else None
def make(p,ny,a,b):
    F=[]
    for x,y in product(range(8),range(ny)):
        i=ix(2,x,y%2,0);c=tuple(map(scale,base(p)[i:i+4]))
        if x in (5,7):
            z=a if x==5 else b
            d,g=z['ini'];c=cols(d[y%len(d)],g[y%len(g)],c[3])
        F.extend(c)
    return tuple(F)
def parts(F,part,keyfn):
    out={}
    for k,f in F.items():out.setdefault(keyfn(k),set()).add(part(f))
    return out
def disj(gs):return all(a.isdisjoint(b) for a,b in combinations(gs.values(),2))
def clean(gs):return disj(gs) and all(len(v)==1 for v in gs.values())
def run(label,best):
    horizon,ny,a,b=best
    print('SELECT',label,'HEIGHT',ny,'HOLD',horizon,'C5',a,'C7',b)
    I=[make(p,ny,a,b) for p in K]
    hh=[hist(f,ny,114) for f in I]
    ac=hh[0][3];assert all(w[3]==ac for w in hh)
    F=[w[0][114] for w in hh]
    for p,w in enumerate(hh):
        assert all(col(F[p],ny,x)==col(I[p],ny,x) for x in (0,6))
        assert corr(F[p])==corr(I[p])
        assert account(arch(F[p],ny))==account(arch(I[p],ny))
        for t in range(1,115):
            ev=[(x,y,k) for x,y,k in w[2][t] if x in ARCH]
            expected=[]
            if p==1:
                if t==113:expected=[(5,y,a['id'][1]) for y in range(0,ny,2)]
                if t==114:expected=[(5,y,a['id'][2]) for y in range(0,ny,2)]+[(7,y,b['id'][1]) for y in range(0,ny,2)]
            assert ev==expected
        for x,z in ((5,a),(7,b)):
            d,g=z['post'][int(p==1)]
            assert mem(F[p],ny,x)==(tuple(d[y%len(d)] for y in range(ny)),tuple(g[y%len(g)] for y in range(ny)))
    assert two(F,lambda f:arch(f,ny))
    assert all(same_neg([w[s][t] for w in hh],lambda f:read(f,ny)) for t in range(115) for s in ((0,) if t==0 else (1,0)))
    print('FIRST_RETURN',label,'Q',H.scalar_account(ac[2]),'H',ac[2],'CORR',len(corr(F[0])),'MEMORY_MATERIAL',tuple((x,material(F[0],ny,x),material(F[1],ny,x)) for x in (5,7)))
    def exchange(p,q):
        f=list(F[p]);reserve=[];outgoing=[]
        for y in range(0,ny,2):
            i=ix(ny,0,y,0)
            assert f[i:i+2]==[scale(P[p]),scale(neg(P[p]))]
            outgoing.extend(f[i:i+2]+[Z,Z])
            new=[scale(P[q]),scale(neg(P[q]))];reserve.extend(new+[Z,Z]);f[i:i+2]=new
        f=tuple(f)
        assert account(f)==account(F[p])
        assert account(F[p]+tuple(reserve))==account(f+tuple(outgoing))
        return f
    keys=tuple(product(BITS,K));all25={(p,q):exchange(p,q) for p,q in product(K,repeat=2)}
    ini={k:all25[k] for k in keys}
    assert len(set(all25.values()))==10 and all(f==ini[int(p==1),q] for (p,q),f in all25.items())
    hs={k:hist(f,ny,512) for k,f in ini.items()}
    materialpart=lambda f:tuple(material(f,ny,x) for x in (5,7))
    verticalpart=lambda f:tuple(mem(f,ny,x) for x in (5,7))
    archivepart=lambda f:arch(f,ny)
    bitfn=lambda k:k[0]
    pairfn=lambda k:(k[0],int(k[1]==1))
    firstB=firstOutside=firstLoss=split=firsthist=None
    current4=[];resets=[];heldresets=[];hids={k:k[0] for k in keys}
    for t in range(513):
        if t and firstB is None:
            hit=next(((k,ev) for k,w in hs.items() if (ev:=tuple(e for e in w[2][t] if e[0] in ARCH))),None)
            if hit:firstB=(t,hit)
        for stage in ((0,) if t==0 else (1,0)):
            G={k:w[stage][t] for k,w in hs.items()}
            if firstOutside is None and any((corr(G[0,q]),col(G[0,q],ny,0),col(G[0,q],ny,6))!=(corr(G[1,q]),col(G[1,q],ny,0),col(G[1,q],ny,6)) for q in K):firstOutside=t,stage
            if firstLoss is None and not disj(parts(G,archivepart,bitfn)):firstLoss=t,stage
            if t<=horizon:
                if t:assert not any(e[0] in ARCH for w in hs.values() for e in w[2][t])
                assert clean(parts(G,materialpart,bitfn)) and clean(parts(G,verticalpart,bitfn)) and disj(parts(G,archivepart,bitfn))
                for k,f in G.items():
                    ref=Rhist[k[1]][stage][t]
                    for x in (0,6):
                        exp=tuple(scale(ref[ix(2,x,y%2,r)]) for y,r in product(range(ny),range(4)))
                        assert col(f,ny,x)==exp
                    assert corr(f)==tuple(scale(ref[ix(2,x,y%2,3)]) for x,y in product(range(8),range(ny)))
            vals={k:(hids[k],read(f,ny)) for k,f in G.items()}
            hp=parts(vals,lambda x:x,pairfn)
            if firsthist is None and clean(hp):firsthist=t,stage
            if split is None and any(len(v)>1 for v in hp.values()):split=t,stage
            ids={v:i for i,v in enumerate(dict.fromkeys(vals.values()))};hids={k:ids[v] for k,v in vals.items()}
            if stage==0 and t>=2 and t%2==0:
                if clean(parts(G,archivepart,pairfn)):current4.append(t)
                if all(all(col(f,ny,x)==col(I[k[1]],ny,x) for x in (0,6)) for k,f in G.items()):
                    resets.append(t)
                    if t<=horizon:heldresets.append(t)
    if horizon<512:assert firstB[0]==horizon+1
    else:assert firstB is None
    write=0;sr=wr=rr=0
    for k,w in hs.items():
        p,q=k;weight=1 if p else 4
        f=w[0][6];ok=all(f[ix(ny,6,y,2)]==scale(mark if q==1 and y%2==0 else gworker) for y in range(ny))
        write+=weight*ok
        f=w[0][114];s0=col(f,ny,0)==col(I[q],ny,0);w0=col(f,ny,6)==col(I[q],ny,6)
        sr+=weight*s0;wr+=weight*w0;rr+=weight*(s0 and w0)
    print('SECOND',label,'WRITE6',write,'FIRST_B',firstB,'FIRST_OUTSIDE',firstOutside,'FIRST_LOSS',firstLoss,
          'SOURCE114',sr,'WORKER114',wr,'BOTH114',rr,'COMMON_RESETS',resets,'HELD_RESETS',heldresets,
          'CURRENT4_COUNT',len(current4),'CURRENT4_FIRST',current4[0] if current4 else None,'HISTORY4',firsthist,'HISTORY_SPLIT',split)
    print('SILENT_CONTRACT',label,'GE114',int(horizon>=114),'GE228',int(horizon>=228),'HOLD',horizon)
def main():
    a5=census5(2,False)
    a7={ny:census7(ny) for ny in (6,8)}
    bestA=select({6:a5,8:a5},a7)
    b5={ny:census5(ny,True) for ny in (6,8)}
    bestB=select(b5,a7)
    print('COMBINED_A',bestA[0],bestA[1],bestA[2]['id'],bestA[3]['id'])
    print('COMBINED_B',bestB[0],bestB[1],bestB[2]['id'],bestB[3]['id'])
    run('A',bestA)
    if bestB[0]>bestA[0]:run('B',bestB)
    else:print('B NO IMPROVEMENT; selected A replay only')
    print('DONE exact integrated absorbing archive')
if __name__=='__main__':main()
