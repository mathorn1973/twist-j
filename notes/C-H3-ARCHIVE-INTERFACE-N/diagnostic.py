"""NON-CANONICAL #2127 D: selected combined trajectory and passive storage."""
from pathlib import Path
import runpy
from itertools import product,combinations
from collections import Counter
S=runpy.run_path(str(Path(__file__).resolve().parent/'synthesis.py'))
V=S['V'];H=S['H'];Z,O,R,J,JI,P=map(S.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(S.get,('add','sub','mul','sc','h','neg'))
seed,cols,hist,account,ix,scale=map(S.get,('seed','cols','hist','account','ix','scale'))
col,ar,rd,th,index=map(S.get,('col','ar','rd','tall_hist','index'))
K=range(5);N=(0,2,3,4);ARCH=S['ARCH'];ny=6
d5=((-33,-9,-18,-30),(-15,3,-18,6))
g5=((-21,-8,5,-36),(3,28,-19,30))
d7=((1,0,6,-7),(2,0,6,-6),(1,2,7,-5),(-1,0,5,-7),(0,0,6,-6),(1,0,6,-5))
g7=(-17,-5,15,-17)
def I(p):
    F=[]
    for x,y in product(range(8),range(ny)):
        i=ix(x,y%2,0);c=tuple(map(scale,seed(p,'static')[i:i+4]))
        if x==5:c=cols(d5[y%2],g5[y%2],c[3])
        if x==7:c=cols(scale(d7[y]),scale(g7),c[3])
        F.extend(c)
    return tuple(F)
def ixn(x,y,r):return index(ny,x,y,r)
def source(f):return col(ny,f,0)
def worker(f):return col(ny,f,6)
def archive(f):return ar(ny,f)
def reader(f):return rd(ny,f)
def corr(f):return f[3::4]
def parts(F,part,keyfn=lambda k:(k[0],int(k[1]==1))):
    pp={}
    for k,f in F.items():pp.setdefault(keyfn(k),set()).add(part(f))
    return pp
def disj(pp):return all(a.isdisjoint(b) for a,b in combinations(pp.values(),2))
def clean(pp):return disj(pp) and all(len(v)==1 for v in pp.values())
def counts(pp):return tuple(len(pp[k]) for k in sorted(pp))
def delta(f,i):return tuple(sub(a,b) for a,b in zip(account(f),account(i)))
def ready(f,i):return source(f)==source(i) and worker(f)==worker(i)
def readset():
    for x,y,r in product(ARCH,range(ny),(2,3)):
        yield (0,x,y,r),lambda f,x=x,y=y,r=r:f[ixn(x,y,r)]
    for x,y in product(ARCH,range(ny)):
        for r,s in combinations(range(4),2):
            yield (1,x,y,r,s),lambda f,x=x,y=y,r=r,s=s:sub(f[ixn(x,y,r)],f[ixn(x,y,s)])
    for x,r in product(ARCH,range(4)):
        for y,z in combinations(range(ny),2):
            yield (2,x,r,y,z),lambda f,x=x,r=r,y=y,z=z:sub(f[ixn(x,y,r)],f[ixn(x,z,r)])
ini=[I(p) for p in K];old=[th(f,ny,114) for f in ini];base=[w[0][114] for w in old]
assert all(ready(f,ini[p]) and account(archive(f))==account(archive(ini[p])) for p,f in enumerate(base))
assert len({corr(f) for f in base})==1 and len({archive(base[p]) for p in N})==1 and archive(base[0])!=archive(base[1])
print('D FIRST','Q',H.scalar_account(old[0][3][2]),'CORR_EQUAL_ACROSS_INPUTS',len({corr(f) for f in base}),'CORR_INITIAL_MATCH',sum(a==b for a,b in zip(corr(base[0]),corr(ini[0]))),'OF',8*ny)
for x,y,r in product(range(8),range(ny),range(4)):
    i=ixn(x,y,r)
    if r==3 and base[0][i]!=ini[0][i]:
        print('D FIRST_CORR_CHANGE',x,y,ini[0][i],base[0][i])
    if x in ARCH and r!=3 and base[0][i]!=base[1][i]:
        print('D FIRST_ARCH_DIFF',x,y,r,base[0][i],base[1][i])
def exchange(p,q):
    f=list(base[p])
    for y in range(0,ny,2):
        i=ixn(0,y,0);assert f[i:i+2]==[scale(P[p]),scale(neg(P[p]))]
        f[i:i+2]=[scale(P[q]),scale(neg(P[q]))]
    assert account(f)==account(base[p])
    return tuple(f)
keys=tuple(product(range(2),K));reps=tuple(product(range(2),range(2)))
loaded={(p,q):exchange(p,q) for p,q in product(K,repeat=2)}
F={k:loaded[k] for k in keys}
assert len(set(loaded.values()))==10 and all(f==F[int(p==1),q] for (p,q),f in loaded.items())
hs={k:th(f,ny,512) for k,f in F.items()}
for q in K:
    fd=None;pc=None;sw6=True
    for t in range(1,513):
        for s in (1,0):
            a,b=hs[0,q][s][t],hs[1,q][s][t]
            if fd is None and (source(a),worker(a))!=(source(b),worker(b)):fd=t,s
            if s==1 and pc is None and any(a[ixn(x,y,3)]!=b[ixn(x,y,3)] for x,y in product((0,6),range(ny))):pc=t,s
            if t<=6:sw6 &= (source(a),worker(a))==(source(b),worker(b))
    print('D INTERFACE',q,'FIRST_SW',fd,'FIRST_INCOMING_CORR',pc,'SW_MATCH6',int(sw6))
for k in reps:
    w=hs[k]
    hit=next(((t,tuple(sorted((x,y,tag) for (x,y),tag in w[2][t].items() if x in ARCH))) for t in range(1,513) if any(x in ARCH for x,y in w[2][t])),None)
    print('D FIRST_ARCHIVE_B',k,hit)
hids={k:k[0] for k in keys};first_hist=split=loss=None;four=[];first_sep=None;individual={k:[] for k in keys}
for t in range(513):
    for stage in ((0,) if t==0 else (1,0)):
        FF={k:w[stage][t] for k,w in hs.items()}
        if loss is None and not disj(parts(FF,archive,lambda k:k[0])):loss=t,stage
        vals={k:(hids[k],reader(f)) for k,f in FF.items()}
        hp=parts(vals,lambda x:x)
        if split is None and any(len(v)>1 for v in hp.values()):split=t,stage,counts(hp)
        if first_hist is None and clean(hp):first_hist=t,stage
        ids={v:i for i,v in enumerate(dict.fromkeys(vals.values()))}
        hids={k:ids[v] for k,v in vals.items()}
        if stage==0 and t>=2 and t%2==0:
            if clean(parts(FF,archive)):four.append(t)
            for k,f in FF.items():
                if ready(f,ini[k[1]]):individual[k].append(t)
F114={k:w[0][114] for k,w in hs.items()}
print('D PARTITIONS','FIRST_HIST4',first_hist,'HIST_SPLIT',split,'FIRST_BIT_LOSS',loss,'CURRENT4_FIRST',four[0] if four else None,'CURRENT4_COUNT',len(four),'CURRENT114',counts(parts(F114,archive)),'DISJOINT114',int(disj(parts(F114,archive))))
for k in reps:
    f=F114[k];i=ini[k[1]]
    print('D END114',k,'SOURCE',int(source(f)==source(i)),'WORKER',int(worker(f)==worker(i)),'SOURCE_DIFFS',sum(a!=b for a,b in zip(source(f),source(i))),'WORKER_DIFFS',sum(a!=b for a,b in zip(worker(f),worker(i))),
          'DELTAS',tuple(delta(p(f),p(i)) for p in (source,worker,archive)),'FIRST_READY',individual[k][0] if individual[k] else None,'READY_COUNT',len(individual[k]))
    for x in (0,6):
        diff=next(((y,r,i[ixn(x,y,r)],f[ixn(x,y,r)]) for y,r in product(range(ny),range(4)) if i[ixn(x,y,r)]!=f[ixn(x,y,r)]),None)
        print('D FIRST_SLOT114',k,x,diff)
for x in ARCH:
    part=lambda f,x=x:col(ny,f,x)
    print('D COLUMN114',x,'DISTINCT',len({part(f) for f in F114.values()}),'COUNTS',counts(parts(F114,part)),'BIT_ONLY',tuple(int(clean(parts(F114,part,lambda k,b=b:(k[0],int(k[1]==1))[b]))) for b in range(2)))
reads=[(desc,fun) for desc,fun in readset() if clean(parts(F114,fun))]
print('D READ114','COUNT',len(reads),'FIRST',reads[0][0] if reads else None)
if reads:print('D READ_VALUES114',tuple((k,reads[0][1](F114[k])) for k in reps))
# Independent supplied passive memory with all-time no-B bound.
qscalar=lambda z:H.scalar_account(h(z))
assert qscalar(J)==qscalar(JI)==3 and qscalar(sc(64,O))==8192
print('D PASSIVE_BOUND',8192,2*2630+24)
for q in K:
    bare=list(V['passive'](q,0,O))
    for x,y in product(ARCH,range(2)):
        i=ix(x,y,0);bare[i:i+3]=(Z,Z,Z)
    bare=tuple(bare)
    assert H.scalar_account(account(bare)[2])==2630
    bh=hist(bare,160,True)
    fields=[]
    for k in K:
        f=list(bare)
        for y,d in enumerate((P[k],neg(P[k]))):
            i=ix(5,y,0);f[i:i+3]=(d,neg(d),sc(64,O))
        fields.append(tuple(f))
    ph=[hist(f,160,True) for f in fields]
    assert len({w[3] for w in ph})==1
    for t in range(161):
        for s in ((0,) if t==0 else (1,0)):
            ref=bh[s][t]
            ff=[w[s][t] for w in ph]
            assert all((V['src'](f),V['worker'](f),V['cor'](f))==(V['src'](ref),V['worker'](ref),V['cor'](ref)) for f in ff)
            assert len({V['archive'](f) for f in ff})==5
            assert all(f[ix(5,0,0)]==P[(k+2*t)%5] and f[ix(5,1,0)]==neg(P[(k+2*t)%5]) for k,f in enumerate(ff))
        if t:assert all(not any(w[2][t][2*x+y] for x,y in product(ARCH,range(2))) for w in ph)
    print('D PASSIVE',q,'BASE_Q',2630,'Q',H.scalar_account(ph[0][3][2]),'PHASES',5,'HORIZON',160)
print('DONE D selected combined and all-time passive bound audit')
