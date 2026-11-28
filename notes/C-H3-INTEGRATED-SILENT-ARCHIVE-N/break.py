"""NON-CANONICAL #2131. Result-exposed independent cyclic arithmetic/update.
Recomputes the frozen local censuses and the two selected complete replays.
Does not import the primary verifier or pinned H3 source.
"""
from functools import cache
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter

def red(a):
    a=tuple(a);return tuple(x-a[4] for x in a[:4])
def root(k):return red(int(i==k%5) for i in range(5))
P=tuple(root(k) for k in range(5));O=P[0];Z=(0,0,0,0);R=P[2]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sc(k,a):return tuple(k*x for x in a)
def sub(a,b):return add(a,sc(-1,b))
def neg(a):return sc(-1,a)
def rs(xs):
    a=Z
    for z in xs:a=add(a,z)
    return a
@cache
def mul(a,b):
    v=[0]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[(i+j)%5]+=x*y
    return red(v)
@cache
def h(a):
    return mul(a,rs(sc(v,P[-k%5]) for k,v in enumerate(a)))
def even(a):return not any(v%2 for v in a)
def half(a):
    assert even(a);return tuple(v//2 for v in a)
J=add(O,R);JI=neg(add(P[1],P[2]));T=h(J);L=sub(O,R)
BI=sc(Q(2,5),rs((sc(4,O),sc(3,R),sc(2,P[4]),P[1])))
assert mul(J,JI)==O and mul(sc(Q(1,2),L),BI)==O and not even(L)
def integral(a):
    assert all(Q(v).denominator==1 for v in a);return tuple(map(int,a))
def scale(a):return integral(mul(L,a))
def f_for(delta,tag):
    a=mul(delta,mul(J,P[3]) if tag==1 else neg(P[3]))
    assert mul(sub(O,JI if tag==1 else J),a)==delta
    return a
def d_for(f,tag):return mul(JI if tag==1 else J,f)
@cache
def C(a,b,back=False):
    dif=sub(a,b)
    if not even(dif):return a,b
    u=mul(P[3] if back else R,dif)
    return half(add(add(a,b),u)),half(sub(add(a,b),u))
def cell(d,g,c):return d,neg(d),g,c
@cache
def B(cell):
    a,b,u,v=cell
    if not even(sub(a,b)) or not even(sub(u,v)):return cell,0
    d,f=half(sub(a,b)),half(sub(u,v));cm,cr=half(add(a,b)),half(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        dn,fn,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        dn,fn,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(cm,dn),sub(cm,dn),add(cr,fn),sub(cr,fn)),k
def vert(v,bit,back=False):
    n=len(v);out=list(v)
    for y in range(bit,n,2):
        j=(y+1)%n;out[y],out[j]=C(v[y],v[j],back)
    return tuple(out)
def rev(v,n):
    for i in reversed(range(n)):v=vert(v,i%2,True)
    return v
def ix(n,x,y):return n*x+y
def transport(F,n,bit,back=False):
    out=[list(c) for c in F]
    for x in range(8):
        for q in range(3):
            values=vert(tuple(F[ix(n,x,y)][q] for y in range(n)),bit,back)
            for y,v in enumerate(values):out[ix(n,x,y)][q]=v
    for y in range(n):
        values=vert(tuple(F[ix(n,x,y)][3] for x in range(8)),bit,back)
        for x,v in enumerate(values):out[ix(n,x,y)][3]=v
    return tuple(tuple(c) for c in out)
def account(F):
    return rs(z for c in F for z in c[:2]),rs(z for c in F for z in c[2:]),rs(h(z) for c in F for z in c)
def scalar(H):
    n=4*H[0]-sum(H[1:]);assert n%2==0;return n//2
def step(F,n,bit,ac):
    G=transport(F,n,bit);ct=tuple(B(c) for c in G)
    N=tuple(c for c,k in ct)
    E=tuple((x,y,ct[ix(n,x,y)][1]) for x,y in product(range(8),range(n)) if ct[ix(n,x,y)][1])
    back=tuple(B(c)[0] for c in N)
    assert back==G and transport(back,n,bit,True)==F and account(G)==account(N)==ac
    return G,N,E
def hist(F,n,nt):
    ac=account(F);cut=[F];mid=[None];tags=[None]
    for t in range(nt):
        G,F,E=step(F,n,t%2,ac);cut.append(F);mid.append(G);tags.append(E)
    return cut,mid,tags,ac
K=range(5);N=(0,2,3,4);ARCH=(1,2,3,4,5,7)
roots=tuple(sc(s,P[k]) for s,k in product((1,-1),K));WS=(Z,)+roots
m=sub(sc(2,O),R);gs=sc(2,mul(J,m));a=sc(-3,L)
b=add(add(mul(m,R),mul(J,a)),sc(12,J))
stock=(Z,Z,Z,b,b,b,add(mul(m,R),sc(2,a)))
gw=(6,-2,12,1);mark=(5,-3,11,1)
def base(p,old=False):
    out=[]
    for x,y in product(range(8),range(2)):
        d=(P[p] if y==0 else sc(3,P[1])) if x==0 else JI if x==6 else Z
        g=gs if x==0 else gw if x==6 else Z
        c=(Z if x==0 else stock[x-1]) if y==0 else gs
        if old and x==5:d=((8,7,1,13),(6,5,-1,11))[y];g=(34,10,21,31)
        out.append(cell(d,g,c))
    return tuple(out)
def col(F,n,x):return F[n*x:n*(x+1)]
def arch(F,n):return tuple(c for x in ARCH for c in col(F,n,x))
def read(F,n):return F[n:]
def corr(F):return tuple(c[3] for c in F)
def material(F,n,x):return tuple(c[0] for c in col(F,n,x))
def mem(F,n,x):return material(F,n,x),tuple(c[2] for c in col(F,n,x))
def negsame(F,part):return len({part(F[p]) for p in N})==1
def two(F,part):return negsame(F,part) and part(F[1])!=part(F[0])
Rhist=[hist(base(p),2,512) for p in K]
Ohist=[hist(base(p,True),2,114) for p in K]
assert scalar(Rhist[0][3][2])==2630 and len({w[3] for w in Rhist})==1
assert scalar(Ohist[0][3][2])==7752 and len({w[3] for w in Ohist})==1
for hs,n in ((Rhist,512),(Ohist,114)):
    for t in range(n+1):
        for st in ((0,) if t==0 else (1,0)):
            assert negsame([w[st][t] for w in hs],lambda f:read(f,2))
def inc(hs,x,t,p,y):return scale(hs[p][1][t][ix(2,x,y%2)][3])
def words(hs,x,t,y):return tuple(dict.fromkeys(inc(hs,x,t,p,y) for p in K))
def table(hs,x,last):return {t:tuple(words(hs,x,t,y) for y in range(2)) for t in range(1,last+1)}
A5=table(Rhist,5,112);A7=table(Ohist,7,113)
future={x:table(Rhist,x,512) for x in (5,7)}
delta=(12,0,6,6);delta5=(0,6,0,0);delta7=(-12,-6,-6,-6)
r=(-2,-2,9,-5);c=(7,-8,12,-2);c7=(7,7,15,7)
assert inc(Rhist,5,113,1,0)==scale(r)
assert inc(Ohist,5,114,1,0)==scale(c) and inc(Ohist,7,114,1,0)==scale(c7)
def advance_pair(d,g,bit):return vert(d,bit),vert(g,bit)
def noB(d,g,w):
    return all(B(cell(d[y],g[y],v))[1]==0 for y in range(len(d)) for v in w[y%2])
def at_write(d,g,hs,x,t,tag,p,correction,final=False):
    out=[];ny=len(d)
    for y in range(ny):
        c0=inc(hs,x,t,p,y);z,b=B(cell(d[y],g[y],c0));target=tag if p==1 and y%2==0 else 0
        if b!=target:return None
        assert z[3]==(scale(base(p)[ix(2,x,y%2)][3]) if final else add(c0,scale(correction) if b else Z))
        out.append(z)
    return tuple(z[0] for z in out),tuple(z[2] for z in out)
def check5(ny,a,b,s,t,e):
    f1,f2=f_for(delta,a),f_for(delta5,b)
    g1=add(r,sc(2,f1));post=sub(g1,delta);target=add(c,sc(2,f2))
    other=add(post,mul(BI,sub(target,post)))
    D=[None]*ny;G=[None]*ny
    for y in range(0,ny,2):
        d1=mul(d_for(f1,a),s if y==0 else O)
        d2=mul(d_for(f2,b),t if y==e else O)
        dp=mul(J if a==1 else JI,d1)
        D[y]=d1;D[(y-1)%ny]=add(dp,mul(BI,sub(d2,dp)))
        G[y]=g1;G[(y-1)%ny]=other
    ready=tuple(map(scale,D)),tuple(map(scale,G))
    ini=rev(ready[0],113),rev(ready[1],113)
    d,g=ini
    for u in range(1,114):
        d,g=advance_pair(d,g,(u-1)%2)
        if u<113 and not noB(d,g,A5[u]):return None,('first',u)
    assert (d,g)==ready
    post=[]
    for p in K:
        pair=at_write(d,g,Rhist,5,113,a,p,delta)
        if pair is None:return None,('write113',p)
        d2,g2=advance_pair(*pair,1)
        pair=at_write(d2,g2,Ohist,5,114,b,p,delta5,True)
        if pair is None:return None,('write114',p)
        post.append(pair)
    assert negsame(post,lambda z:z)
    return (ini,(post[0],post[1])),None
def check7(ny,tag,k,u,v):
    f=f_for(delta7,tag);d0=d_for(f,tag);g0=scale(add(c7,sc(2,f)))
    ready=tuple(scale((mul(d0,P[k]) if y==0 else d0) if y%2==0 else add(d0,sc(2,v if y==1 else u))) for y in range(ny))
    ini=rev(ready,114),tuple(g0 for y in range(ny))
    d,g=ini
    for t in range(1,115):
        d=vert(d,(t-1)%2)
        if t<114 and not noB(d,g,A7[t]):return None,('first',t)
    assert d==ready
    post=[]
    for p in K:
        pair=at_write(d,g,Ohist,7,114,tag,p,delta7,True)
        if pair is None:return None,('write114',p)
        post.append(pair)
    assert negsame(post,lambda z:z)
    return (ini,(post[0],post[1])),None
def hold(x,post):
    now=post
    if now[0][0]==now[1][0]:return -1,('no_material_record',)
    for t in range(1,513):
        now=tuple(advance_pair(d,g,(t-1)%2) for d,g in now)
        assert now[0][0]!=now[1][0]
        for a,(d,g) in enumerate(now):
            for y in range(len(d)):
                if not all(B(cell(d[y],g[y],v))[1]==0 for v in future[x][t][y%2]):
                    q,tag=next((q,B(cell(d[y],g[y],inc(Rhist,x,t,q,y)))[1]) for q in K if B(cell(d[y],g[y],inc(Rhist,x,t,q,y)))[1])
                    return t-1,(t,a,q,y,tag)
    return 512,None
def report(label,rr,reject):
    histo=Counter(z['hold'] for z in rr)
    best=max(rr,key=lambda z:z['hold']) if rr else None
    print('CENSUS',label,'ADMITTED',len(rr),'REJECT',sorted(reject.items()),'HOLD',sorted(histo.items()),
          'GE114',sum(n for h,n in histo.items() if h>=114),'GE228',sum(n for h,n in histo.items() if h>=228),'FULL512',histo[512])
    if best:print('BEST',label,best['id'],best['hold'],best['fail'])
def result(id,x,res):
    ini,post=res;v,fail=hold(x,post)
    return dict(id=id,ini=ini,post=post,hold=v,fail=fail)
def census5(n,ext):
    rr=[];reject=Counter()
    for a,b,si,ti,e in product((1,2),(1,2),range(10),range(10),(0,2) if ext else (0,)):
        res,err=check5(n,a,b,roots[si],roots[ti],e)
        if err:reject[err]+=1
        else:rr.append(result((n,a,b,si,ti,e),5,res))
    report(('B5' if ext else 'A5',n),rr,reject)
    assert len(rr)+sum(reject.values())==(800 if ext else 400)
    return rr
def census7(n):
    rr=[]
    for tag in (1,2):
        rr0=[];reject=Counter()
        for k,ui,vi in product(K,range(11),range(11)):
            res,err=check7(n,tag,k,WS[ui],WS[vi])
            if err:reject[err]+=1
            else:rr0.append(result((n,tag,k,ui,vi),7,res))
        report(('A7',n,tag),rr0,reject)
        assert len(rr0)+sum(reject.values())==605
        rr+=rr0
    return rr
def choose(l5,l7):
    out=[]
    for ny in (6,8):
        if not l5[ny] or not l7[ny]:continue
        score=min(max(z['hold'] for z in l5[ny]),max(z['hold'] for z in l7[ny]))
        a=next(z for z in l5[ny] if z['hold']>=score);b=next(z for z in l7[ny] if z['hold']>=score)
        out.append((score,ny,a,b))
    return max(out,key=lambda z:z[0])
def make(p,n,a,b):
    out=[]
    for x,y in product(range(8),range(n)):
        z=tuple(scale(v) for v in base(p)[ix(2,x,y%2)])
        if x in (5,7):
            d,g=(a if x==5 else b)['ini'];z=cell(d[y%len(d)],g[y%len(g)],z[3])
        out.append(z)
    return tuple(out)
def parts(F,part,keyfn):
    d={}
    for k,f in F.items():d.setdefault(keyfn(k),set()).add(part(f))
    return d
def disj(d):return all(a.isdisjoint(b) for a,b in combinations(d.values(),2))
def clean(d):return disj(d) and all(len(v)==1 for v in d.values())
def run(label,best):
    horizon,ny,a,b=best
    I=[make(p,ny,a,b) for p in K]
    hh=[hist(f,ny,114) for f in I];F=[w[0][114] for w in hh]
    ac=hh[0][3];assert all(w[3]==ac for w in hh)
    for p,w in enumerate(hh):
        assert all(col(F[p],ny,x)==col(I[p],ny,x) for x in (0,6))
        assert corr(F[p])==corr(I[p]) and account(arch(F[p],ny))==account(arch(I[p],ny))
        for t in range(1,115):
            expected=[]
            if p==1:
                if t==113:expected=[(5,y,a['id'][1]) for y in range(0,ny,2)]
                if t==114:expected=[(5,y,a['id'][2]) for y in range(0,ny,2)]+[(7,y,b['id'][1]) for y in range(0,ny,2)]
            assert tuple(e for e in w[2][t] if e[0] in ARCH)==tuple(expected)
        for x,z in ((5,a),(7,b)):
            d,g=z['post'][int(p==1)]
            assert mem(F[p],ny,x)==(tuple(d[y%len(d)] for y in range(ny)),tuple(g[y%len(g)] for y in range(ny)))
    assert two(F,lambda f:arch(f,ny))
    assert all(negsame([w[s][t] for w in hh],lambda f:read(f,ny)) for t in range(115) for s in ((0,) if t==0 else (1,0)))
    print('FIRST_RETURN',label,'Q',scalar(ac[2]),'H',ac[2],'CORR',len(corr(F[0])),'MEMORY_MATERIAL',tuple((x,material(F[0],ny,x),material(F[1],ny,x)) for x in (5,7)))
    def exchange(p,q):
        f=list(F[p]);u=[];v=[]
        for y in range(0,ny,2):
            i=ix(ny,0,y);assert f[i][:2]==(scale(P[p]),scale(neg(P[p])))
            v.append(cell(scale(P[p]),Z,Z));u.append(cell(scale(P[q]),Z,Z))
            f[i]=cell(scale(P[q]),f[i][2],f[i][3])
        f=tuple(f);assert account(f)==account(F[p]) and account(F[p]+tuple(u))==account(f+tuple(v))
        return f
    keys=tuple(product(range(2),K));all25={(p,q):exchange(p,q) for p,q in product(K,repeat=2)}
    ini={k:all25[k] for k in keys}
    assert len(set(all25.values()))==10 and all(f==ini[int(p==1),q] for (p,q),f in all25.items())
    hs={k:hist(f,ny,512) for k,f in ini.items()}
    materialpart=lambda f:tuple(material(f,ny,x) for x in (5,7))
    verticalpart=lambda f:tuple(mem(f,ny,x) for x in (5,7))
    archivepart=lambda f:arch(f,ny)
    bitfn=lambda k:k[0];pairfn=lambda k:(k[0],int(k[1]==1))
    firstB=firstOutside=firstLoss=split=firsthist=None
    current4=[];resets=[];heldresets=[];hids={k:k[0] for k in keys}
    for t in range(513):
        if t and firstB is None:
            hit=next(((k,ev) for k,w in hs.items() if (ev:=tuple(e for e in w[2][t] if e[0] in ARCH))),None)
            if hit:firstB=(t,hit)
        for st in ((0,) if t==0 else (1,0)):
            G={k:w[st][t] for k,w in hs.items()}
            if firstOutside is None and any((corr(G[0,q]),col(G[0,q],ny,0),col(G[0,q],ny,6))!=(corr(G[1,q]),col(G[1,q],ny,0),col(G[1,q],ny,6)) for q in K):firstOutside=t,st
            if firstLoss is None and not disj(parts(G,archivepart,bitfn)):firstLoss=t,st
            if t<=horizon:
                if t:assert not any(e[0] in ARCH for w in hs.values() for e in w[2][t])
                assert clean(parts(G,materialpart,bitfn)) and clean(parts(G,verticalpart,bitfn)) and disj(parts(G,archivepart,bitfn))
                for k,f in G.items():
                    ref=Rhist[k[1]][st][t]
                    for x in (0,6):
                        exp=tuple(tuple(scale(v) for v in ref[ix(2,x,y%2)]) for y in range(ny))
                        assert col(f,ny,x)==exp
                    assert corr(f)==tuple(scale(ref[ix(2,x,y%2)][3]) for x,y in product(range(8),range(ny)))
            vals={k:(hids[k],read(f,ny)) for k,f in G.items()}
            hp=parts(vals,lambda x:x,pairfn)
            if firsthist is None and clean(hp):firsthist=t,st
            if split is None and any(len(v)>1 for v in hp.values()):split=t,st
            ids={v:i for i,v in enumerate(dict.fromkeys(vals.values()))};hids={k:ids[v] for k,v in vals.items()}
            if st==0 and t>=2 and t%2==0:
                if clean(parts(G,archivepart,pairfn)):current4.append(t)
                if all(all(col(f,ny,x)==col(I[k[1]],ny,x) for x in (0,6)) for k,f in G.items()):
                    resets.append(t)
                    if t<=horizon:heldresets.append(t)
    if horizon<512:assert firstB[0]==horizon+1
    else:assert firstB is None
    write=sr=wr=rr=0
    for (p,q),w in hs.items():
        weight=1 if p else 4
        f=w[0][6];ok=all(f[ix(ny,6,y)][2]==scale(mark if q==1 and y%2==0 else gw) for y in range(ny))
        write+=weight*ok
        f=w[0][114];s0=col(f,ny,0)==col(I[q],ny,0);w0=col(f,ny,6)==col(I[q],ny,6)
        sr+=weight*s0;wr+=weight*w0;rr+=weight*(s0 and w0)
    print('SECOND',label,'WRITE6',write,'FIRST_B',firstB,'FIRST_OUTSIDE',firstOutside,'FIRST_LOSS',firstLoss,
          'SOURCE114',sr,'WORKER114',wr,'BOTH114',rr,'COMMON_RESETS',resets,'HELD_RESETS',heldresets,
          'CURRENT4_COUNT',len(current4),'CURRENT4_FIRST',current4[0] if current4 else None,'HISTORY4',firsthist,'HISTORY_SPLIT',split)
    print('SILENT_CONTRACT',label,'GE114',int(horizon>=114),'GE228',int(horizon>=228),'HOLD',horizon)
    if label=='B':
        pos={w[1][112][ix(ny,4,y)][3] for (a0,q),w in hs.items() for y in range(0,ny,2) if q==1}
        negative={w[1][112][ix(ny,4,y)][3] for (a0,q),w in hs.items() for y in range(0,ny,2) if q!=1}
        d4=sc(2,delta);assert mul(sc(Q(1,2),L),d4)==scale(delta)
        assert pos==negative=={(21,10,17,12)}
        print('D TARGET226','POS',sorted(pos),'NEG',sorted(negative),'DELTA4',d4)
        print('D STOP target radiation unavailable')
def main():
    a5=census5(2,False);a7={n:census7(n) for n in (6,8)}
    A=choose({6:a5,8:a5},a7)
    b5={n:census5(n,True) for n in (6,8)};B0=choose(b5,a7)
    print('COMBINED_A',A[0],A[1],A[2]['id'],A[3]['id'])
    print('COMBINED_B',B0[0],B0[1],B0[2]['id'],B0[3]['id'])
    assert A[0:2]==(4,6) and B0[0:2]==(126,6)
    run('A',A);run('B',B0)
    print('PASS alternate independent ring, full local censuses and complete selected trajectories')
if __name__=='__main__':main()
