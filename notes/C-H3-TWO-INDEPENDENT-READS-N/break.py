"""NON-CANONICAL #2125 result-exposed alternate.
Pinned independent five-coefficient ring and native-update engine.
Does not import the primary code or public H3 source.
"""
from pathlib import Path
import runpy,hashlib
from itertools import product,combinations
from collections import Counter
from fractions import Fraction as Q
root=Path(__file__).resolve().parent
engine=root/'alternate_predecessor.py'
assert hashlib.sha256(engine.read_bytes()).hexdigest()=='48262b6e7bb600c069952412015385721c894210eec50da11314df792c2ac27e'
E=runpy.run_path(str(engine))
O,Z,R,J,JI,P=map(E.get,('O','Z','R','J','JI','P'))
add,sub,mul,sc,h,even=map(E.get,('add','sub','mul','sc','h','even'))
raw,flat,cell,ix=map(E.get,('raw','flat','cell','ix'))
C,B,hist,step,acc,scalar=map(E.get,('C','B','hist','step','acc','scalar'))
seed,src,worker,archive,reader=map(E.get,('seed','source','worker','archive','reader'))
neg=lambda z:sc(-1,z)
K=range(5);N=(0,2,3,4);ARCH=(1,2,3,4,5,7)
keys=tuple(product(range(2),K));reps=tuple(product(range(2),range(2)))
bits=lambda k:(k[0],int(k[1]==1))
D=((8,7,1,13,0),(6,5,-1,11,0));G=(34,10,21,31,0)
g=(6,-2,12,1,0);mark=(5,-3,11,1,0)
def setup(F,d,g0):
    F=list(F)
    for y in range(2):
        i=ix(5,y);F[i]=cell(d[y],g0,F[i][3])
    return tuple(F)
def replace(F,p,q):
    assert F[0][:2]==(P[p],neg(P[p]))
    out=(cell(P[q],F[0][2],F[0][3]),)+F[1:]
    assert acc(F)==acc(out)
    assert acc(F+(cell(P[q],Z,Z),))==acc(out+(cell(P[p],Z,Z),))
    return out
def groups(F,part,keyfn=bits):
    groups={}
    for k,f in F.items():groups.setdefault(keyfn(k),set()).add(part(f))
    return groups
def disj(gs):return all(a.isdisjoint(b) for a,b in combinations(gs.values(),2))
def clean(gs):return disj(gs) and all(len(v)==1 for v in gs.values())
def counts(gs):return tuple(len(gs[k]) for k in sorted(gs))
def digest(F):
    return hashlib.sha256(';'.join(','.join(map(str,z)) for z in flat(F)).encode()).hexdigest()
def ready(F,k,I):return src(F)==src(I[k[1]]) and worker(F)==worker(I[k[1]])
def checkwrite(F,k):return F[ix(6,0)][2]==(mark if k[1]==1 else g) and F[ix(6,1)][2]==g
I=[setup(seed(k,'static'),D,G) for k in K]
old=[hist(f,244) for f in I]
assert len({hh[3] for hh in old})==1 and scalar(old[0][3][2])==7752
for t in range(245):
    for st in ((0,) if t==0 else (1,0)):
        assert len({reader(old[k][st][t]) for k in N})==1
def load(T):
    base=[hh[0][T] for hh in old]
    assert all(src(f)==src(I[k]) and worker(f)==worker(I[k]) and acc(archive(f))==acc(archive(I[k])) for k,f in enumerate(base))
    assert len({archive(base[k]) for k in N})==1 and archive(base[0])!=archive(base[1])
    all25={(p,q):replace(base[p],p,q) for p,q in product(K,repeat=2)}
    F={k:all25[k] for k in keys}
    assert len(set(all25.values()))==len(set(F.values()))==10
    assert all(v==F[int(p==1),q] for (p,q),v in all25.items())
    return F
def A(T):
    F=load(T);ac={k:acc(f) for k,f in F.items()}
    assert len(set(ac.values()))==1
    print('START',T,'LOADED',len(set(F.values())),'Q',scalar(ac[0,0][2]))
    first_loss=None;history_split=None;ret=[];sret=Counter();fst={}
    ids={k:k[0] for k in keys}
    assert disj(groups(F,archive,lambda k:k[0]))
    for t in range(1,4097):
        mids={};nxt={};tags={}
        for k,f in F.items():mids[k],nxt[k],tags[k]=step(f,(t-1)%2,ac[k])
        for stage,ff in ((1,mids),(0,nxt)):
            if first_loss is None and not disj(groups(ff,archive,lambda k:k[0])):first_loss=(t,stage)
            vals={k:(ids[k],reader(ff[k])) for k in keys}
            if history_split is None and any(len(v)>1 for v in groups(vals,lambda x:x).values()):
                history_split=(t,stage,counts(groups(vals,lambda x:x)),len(set(vals.values())))
            # Distinct exact prefix equivalence classes.
            uniq={v:i for i,v in enumerate(dict.fromkeys(vals.values()))}
            ids={k:uniq[v] for k,v in vals.items()}
        F=nxt
        if t==6:
            print('WRITE6',T,'CORRECT',sum(int(checkwrite(f,k))*(1 if k[0] else 4) for k,f in F.items()))
            for k,f in F.items():print('WRITE_CASE',T,k,'CLK',raw(f[ix(6,0)][2]),raw(f[ix(6,1)][2]),'TAGS',tags[k][12:14])
        if t%2:continue
        ok={k:ready(f,k,I) for k,f in F.items()}
        for k in keys:
            if ok[k]:sret[k]+=1;fst.setdefault(k,t)
        if t==114:
            pp=groups(F,archive)
            print('STRIDE114',T,'READY',sum(ok[k]*(1 if k[0] else 4) for k in keys),'ARCHIVE_COUNTS',counts(pp),'DISJOINT',int(disj(pp)),'FIRST_LOSS',first_loss)
        if all(ok.values()):ret.append(t)
    assert not ret and history_split is None
    for p,q in product(K,repeat=2):
        k=int(p==1),q
        print('CASE',T,p,q,'BITS',bits(k),'FIRST_RESET',fst.get(k),'RESET_COUNT',sret[k],'FINAL_SHA',digest(F[k]))
    print('SUMMARY',T,'RESETS',ret,'DISJOINT',[],'EXACT4',[],'SUCCESS',[],'SUCCESS114',0,'FACTORED',[],'FIRST_LOSS',first_loss,'HISTORY_SPLIT',history_split,'READ_LOSS',None)

def readset():
    for x,y,r in product(ARCH,range(2),(2,3)):
        yield (0,x,y,r),lambda F,x=x,y=y,r=r:F[ix(x,y)][r]
    for x,y in product(ARCH,range(2)):
        for r,s in combinations(range(4),2):
            yield (1,x,y,r,s),lambda F,x=x,y=y,r=r,s=s:sub(F[ix(x,y)][r],F[ix(x,y)][s])
    for x,r in product(ARCH,range(4)):
        yield (2,x,r),lambda F,x=x,r=r:sub(F[ix(x,0)][r],F[ix(x,1)][r])
def D_gate(T):
    hs={k:hist(f,256) for k,f in load(T).items()}
    ids={k:k[0] for k in keys};first_hist=None
    for t in range(1,257):
        for st in (1,0):
            vals={k:(ids[k],reader(hs[k][st][t])) for k in keys}
            if first_hist is None and clean(groups(vals,lambda x:x)):first_hist=t,st
            uniq={v:i for i,v in enumerate(dict.fromkeys(vals.values()))}
            ids={k:uniq[v] for k,v in vals.items()}
    assert first_hist==(2,1)
    print('D START',T,'FIRST_FOUR_HISTORIES',first_hist)
    for k in reps:
        w=hs[k];c=w[1][6][ix(6,0)]
        d=sc(Q(1,2),sub(c[0],c[1]));f=sc(Q(1,2),sub(c[2],c[3]))
        print('D PRE6',T,k,'CELL',tuple(map(raw,c)),'H_D',tuple(map(str,raw(h(d)))),'H_F',tuple(map(str,raw(h(f)))),
              'PARITY',int(even(sub(c[0],c[1]))),int(even(sub(c[2],c[3]))),'TAG',w[2][6][12])
    print('D POS_CORR_DIFF',T,raw(sub(hs[1,1][1][6][ix(6,0)][3],hs[0,1][1][6][ix(6,0)][3])))
    F={k:w[0][114] for k,w in hs.items()}
    assert clean(groups(F,archive))
    print('D RESET114',T,tuple(sum((1 if k[0] else 4) for k,f in F.items() if bits(k)==b and ready(f,k,I)) for b in reps))
    for k in reps:print('D ARCH114',T,k,'SHA',digest(archive(F[k])),'SOURCE_READY',int(src(F[k])==src(I[k[1]])),'WORKER_READY',int(worker(F[k])==worker(I[k[1]])))
    for x in ARCH:
        col=lambda f,x=x:f[2*x:2*x+2]
        print('COLUMN',x,'DISTINCT',len({col(f) for f in F.values()}),'COUNTS',counts(groups(F,col)),
              'BIT_ONLY',tuple(int(clean(groups(F,col,lambda k,b=b:bits(k)[b]))) for b in range(2)))
    reads=list(readset())
    indep=[[v for v in reads if clean(groups(F,v[1],lambda k,b=b:bits(k)[b]))] for b in range(2)]
    four=[v for v in reads if clean(groups(F,v[1]))]
    assert not any(indep)
    pick=next((v for v in combinations(reads,2) if clean(groups(F,lambda f,v=v:tuple(w[1](f) for w in v)))),None)
    assert pick is not None
    print('READ_CLASS','INDEPENDENT',tuple(map(len,indep)),'FOUR_SINGLE',len(four),'FIRST_FOUR',four[0][0] if four else None,'PICK',tuple(v[0] for v in pick))
    fn=lambda f:tuple(v[1](f) for v in pick)
    vals={bits(k):fn(f) for k,f in F.items()}
    print('D READ',T,tuple(v[0] for v in pick),'VALUES',tuple((k,tuple(map(raw,v))) for k,v in sorted(vals.items())))
    el=sl=None
    for t in range(115,257):
        for st in (1,0):
            ff={k:w[st][t] for k,w in hs.items()}
            if el is None and any(fn(v)!=vals[bits(k)] for k,v in ff.items()):el=t,st
            if sl is None and not clean(groups(ff,fn)):sl=t,st
    print('D READ_LOSS',T,el,sl)
def rot(d,n,back=False):
    for _ in range(n%5):d=C(*d,back)
    return d
def E_gate():
    I0=[seed(k,'static') for k in K]
    hh=[hist(f,114) for f in I0]
    delta=(12,0,6,6,0);rp=(-2,-2,9,-5,0)
    ws=(Z,)+tuple(sc(n*s,P[k]) for n,s,k in product((1,3,5),(1,-1),K))
    stats=Counter()
    for tag in (1,2):
        f=mul(delta,mul(J,P[3]) if tag==1 else neg(P[3]))
        assert mul(sub(O,JI if tag==1 else J),f)==delta
        g0=add(rp,sc(2,f));b=mul(JI if tag==1 else J,f);local=Counter()
        for sign,k,w in product((1,-1),K,ws):
            d0=mul(b,sc(sign,P[k]));d=rot((d0,add(d0,sc(2,w))),113,True)
            cur=d;ok=True;local['tried']+=1
            for t in range(1,114):
                cur=C(*cur)
                if any(B(cell(cur[y],g0,hh[i][1][t][ix(5,y)][3]))[1]!=(tag if t==113 and i==1 and y==0 else 0) for i,y in product(K,range(2))):
                    ok=False;break
            if not ok:local['guard_reject']+=1;continue
            local['admitted']+=1
            assert cur==(d0,add(d0,sc(2,w)))
            base=[]
            for i in K:
                F0=setup(I0[i],d,g0);ac=acc(F0)
                F112=setup(hh[i][0][112],rot(d,112),g0)
                assert acc(F112)==ac
                _,F113,tt=step(F112,0,ac)
                assert tt[10:12]==(tag if i==1 else 0,0)
                assert F113[ix(5,0)][3]==add(hh[i][0][113][ix(5,0)][3],delta if i==1 else Z)
                _,F114,_=step(F113,1,ac)
                assert src(F114)==src(F0) and worker(F114)==worker(F0) and acc(archive(F114))==acc(archive(F0))
                base.append(F114)
            assert len({archive(base[i]) for i in N})==1 and archive(base[0])!=archive(base[1])
            F={k:hist(replace(base[k[0]],*k),6)[0][6] for k in reps}
            pat=''.join(str(int(checkwrite(F[k],k))) for k in reps)
            local['screen_'+pat]+=1
            assert pat=='1110'
        assert local=={'tried':310,'guard_reject':10,'admitted':300,'screen_1110':300}
        stats.update(local)
        print('E LOCAL',tag,sorted(local.items()))
    print('E COUNTS',sorted(stats.items()),'FIRST_READY',None)
    print('E NO QUALIFYING SECOND READ')
import sys
if sys.argv[1]=='A':
    for T in (114,198,244):A(T)
    print('DONE exact supplied second-input continuation, not a native input loader')
elif sys.argv[1]=='DE':
    for T in (114,198,244):D_gate(T)
    E_gate()
    print('DONE D/E exact diagnostic and bounded family')
else:raise SystemExit('use A or DE')
