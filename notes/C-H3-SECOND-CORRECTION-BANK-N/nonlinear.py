"""NON-CANONICAL #2133 D. Bounded actual changed-guard route diagnostic."""
import runpy
from pathlib import Path
from itertools import product
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'prior.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
ix,cols,account,step,hist,scale=map(V.get,('ix','cols','account','step','hist','scale'))
col,arch,read,corr,material,mem,vert,back=map(V.get,('col','arch','read','corr','material','mem','vert','back'))
parts,disj,clean,ratio,dm=map(V.get,('parts','disj','clean','ratio','dm'))
K=range(5);N=(0,2,3,4);keys=tuple(product(range(2),K));ny=6
old=V['Rhist'][1];target=(6,3,0,6);delta=V['delta']
def powr(a,e):
    if e<0:
        assert a==J
        a,e=JI,-e
    z=O
    for _ in range(e):z=mul(z,a)
    return z
units=tuple(sc(s,mul(P[k],powr(J,e))) for s,k,e in product((1,-1),K,range(-3,4)))
zs=[]
for N0,u,d in product((1,2,3,4,6,8,12,16),units,(target,delta)):
    zs.append(sc(N0,mul(u,d)))
for h0,ell,u,d in product(range(4),(1,2),units,(target,delta)):
    zs.append(sc(2**h0,mul(mul(powr(V['L'],ell),u),d)))
zs=tuple(dict.fromkeys(zs))
assert all(z!=Z and all(type(v)==int for v in z) for z in zs)
print('D AMPLITUDES',len(zs),'EVENTS',12,'TOTAL',12*len(zs),flush=True)
def patch(f,n,x,y,r,z):
    out=list(f);i=ix(n,x,y,r);out[i]=add(out[i],z);return tuple(out)
def direct(f,n,t):
    g=H.transport(f,n,(t-1)%2);return H.collide(g,n)
wins=[];counts=Counter()
for t in range(91,103):
    local=Counter()
    for z in zs:
        f=patch(old[0][t],2,4,0,3,z)
        changed=False
        for u in range(t+1,115):
            f,ev=direct(f,2,u)
            changed |= ev!=old[2][u]
        a=col(f,2,0)==col(old[0][0],2,0);b=col(f,2,6)==col(old[0][0],2,6)
        c=f[ix(2,6,0,3)]==old[0][0][ix(2,6,0,3)]
        local[(int(a),int(b),int(c),int(changed))]+=1
        if a and b:wins.append((t,z))
    counts.update(local)
    print('D BARE',t,sorted(local.items()),'CUM_WINS',len(wins),flush=True)
print('D COUNTS',sorted(counts.items()),'WINS',len(wins),flush=True)
for t,z in wins:print('D BARE_WIN',t,z)
if not wins:
    print('D NO HYPOTHETICAL ROUTE; no stock synthesis')
    raise SystemExit(0)
a,err=V['c5test'](6,1,1,V['ROOTS'][8],V['ROOTS'][5],0);assert err is None
a=dict(id=(6,1,1,8,5,0),ini=a[0],post=a[1],hold=154)
b,err=V['c7test'](6,1,1,7,3);assert err is None
b=dict(id=(6,1,1,7,3),ini=b[0],post=b[1],hold=126)
I=[V['make'](p,ny,a,b) for p in K]
hh=[hist(f,ny,114) for f in I]
base=[w[0][114] for w in hh]
def load(f,p,q):
    f=list(f);reserve=[];outgoing=[]
    for y in range(0,ny,2):
        i=ix(ny,0,y,0);assert f[i:i+2]==[scale(P[p]),scale(neg(P[p]))]
        outgoing.extend(f[i:i+2]+[Z,Z])
        f[i:i+2]=[scale(P[q]),scale(neg(P[q]))]
        reserve.extend(f[i:i+2]+[Z,Z])
    return tuple(f),tuple(reserve),tuple(outgoing)
all25={}
for p,q in product(K,repeat=2):
    f,r,u=load(base[p],p,q)
    assert account(f)==account(base[p]) and account(base[p]+r)==account(f+u)
    all25[p,q]=f
loaded={k:all25[k] for k in keys}
assert len(set(all25.values()))==10 and all(f==loaded[int(p==1),q] for (p,q),f in all25.items())
reference={k:hist(f,ny,114) for k,f in loaded.items()}
qual=[]
for t,z in wins:
    okay=True;report=[]
    for k in keys:
        f=reference[k][0][t];new=scale(z)
        if k[1]==1:
            for y in range(0,ny,2):f=patch(f,ny,4,y,3,new)
        first=None;changed=0
        for u in range(t+1,115):
            f,ev=direct(f,ny,u)
            changed+=ev!=reference[k][2][u]
            if first is None and any(x in (5,7) for x,y,b0 in ev):first=(u,ev)
        ready=all(col(f,ny,x)==col(I[k[1]],ny,x) for x in (0,6))
        okay &= ready and first is None
        report.append((k,int(ready),first,changed))
    print('D INTEGRATED_HYPOTHETICAL',t,z,'PASS',int(okay),'DETAIL',report)
    if okay:qual.append((t,z))
print('D INTEGRATED_WINS',len(qual))
if not qual:
    print('D NO INTEGRATED ROUTE; no stock synthesis')
    raise SystemExit(0)
t,z=qual[0]
print('D FIRST_ROUTE',t,z,flush=True)
# First route only. Native bank common stock, no changed target.
r=old[1][t][ix(2,4,0,3)];T=114+t
inputs={}
for u in range(1,T):
    hs=hh if u<=114 else reference.values()
    inputs[u]=tuple(tuple(dict.fromkeys(w[1][u if u<=114 else u-114][ix(ny,4,y,3)] for w in hs)) for y in range(ny))
def prep(tag,k,ui,vi):
    f=ratio(z,tag);d0=dm(f,tag);g0=scale(add(r,sc(2,f)))
    u,v=V['WS'][ui],V['WS'][vi]
    goal=tuple(scale((mul(d0,P[k]) if y==0 else d0) if y%2==0 else add(d0,sc(2,v if y==1 else u))) for y in range(ny))
    ini=back(goal,T);d=ini;g=tuple(g0 for _ in range(ny))
    for u0 in range(1,T+1):
        d=vert(d,(u0-1)%2)
        if u0==T:break
        for y in range(ny):
            if any(H.collision(cols(d[y],g0,c0))[1] for c0 in inputs[u0][y]):return 'EARLY_'+str(u0),None
    assert d==goal
    for k0,w in reference.items():
        for y in range(ny):
            c=w[1][t][ix(ny,4,y,3)];f0,b0=H.collision(cols(d[y],g0,c))
            expected=tag if k0[1]==1 and y%2==0 else 0
            if b0!=expected:return 'TARGET',None
            assert f0[3]==add(c,scale(z) if expected else Z)
    return 'ADMIT',(ini,g)
def patchbank(F,d,g):
    f=list(F)
    for y in range(ny):
        i=ix(ny,4,y,0);f[i:i+3]=(d[y],neg(d[y]),g[y])
    return tuple(f)
def native(tag,d,g):
    II=[patchbank(f,d,g) for f in I];hh0=[hist(f,ny,114) for f in II]
    assert len({w[3] for w in hh0})==1
    for p,w in enumerate(hh0):
        for u in range(1,115):assert not any(e[0]==4 for e in w[2][u])
        f=w[0][114]
        assert all(col(f,ny,x)==col(II[p],ny,x) for x in (0,6)) and corr(f)==corr(II[p])
        assert account(arch(f,ny))==account(arch(II[p],ny))
    A={}
    for p,q in product(K,repeat=2):
        f0=hh0[p][0][114];f1,u,v=load(f0,p,q)
        assert account(f0)==account(f1) and account(f0+u)==account(f1+v)
        A[p,q]=f1
    assert len(set(A.values()))==10 and all(f==A[int(p==1),q] for (p,q),f in A.items())
    hs={k:hist(A[k],ny,114) for k in keys}
    F={k:w[0][114] for k,w in hs.items()}
    for k,w in hs.items():
        for u in range(1,115):
            ev=tuple(e for e in w[2][u] if e[0] in V['ARCH'])
            want=tuple((4,y,tag) for y in range(0,ny,2)) if k[1]==1 and u==t else ()
            if ev!=want:return 'LATER_OR_EARLY_B',None
        if not all(col(F[k],ny,x)==col(II[k[1]],ny,x) for x in (0,6)):return 'RESET',None
        assert account(arch(F[k],ny))==account(arch(II[k[1]],ny))
    if not clean(parts(F,lambda f:tuple(material(f,ny,x) for x in (5,7)),lambda k:k[0])):return 'OLD_RECORD',None
    if not clean(parts(F,lambda f:material(f,ny,4),lambda k:int(k[1]==1))):return 'NEW_RECORD',None
    return 'PASS',(II,hh0,hs,F)
stats=Counter()
for tag,k,ui,vi in product((1,2),K,range(11),range(11)):
    status,zz=prep(tag,k,ui,vi);stats[status]+=1
    if zz is None:continue
    status,ans=native(tag,*zz);stats[status]+=1
    if ans:
        II,hh0,hs,F=ans
        print('D NATIVE_SELECT',tag,k,ui,vi,'INITIAL_BANK',zz,'Q',H.scalar_account(hh0[0][3][2]),'COUNTS',sorted(stats.items()))
        print('D NATIVE_PASS',25,'MATERIAL4',len({tuple(material(f,ny,x) for x in (4,5,7)) for f in F.values()}))
        for k in ((0,0),(0,1),(1,0),(1,1)):print('D MATERIAL',k,tuple(material(F[k],ny,x) for x in (4,5,7)))
        break
else:
    print('D NATIVE_NO',sorted(stats.items()))
