"""NON-CANONICAL #2125. Two independent input reads, supplied exchange boundary."""
from pathlib import Path
import runpy,hashlib,sys
from itertools import product,combinations
from collections import Counter
root=Path(__file__).resolve().parent
assert hashlib.sha256((root/'predecessor.py').read_bytes()).hexdigest()=='ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95'
V=runpy.run_path(str(root/'predecessor.py'))
H=V['H'];Z,P=V['Z'],V['P']
add,sub,neg=V['add'],V['sub'],V['neg']
hist,step,seed,account,ix=V['hist'],V['step'],V['seed'],V['account'],V['ix']
src,worker,archive,reader=V['sourcepart'],V['worker'],V['archive'],V['reader']
N=(0,2,3,4); K=range(5)
ARCH=(1,2,3,4,5,7)
keys=tuple(product(range(2),K))
bits=lambda k:(k[0],int(k[1]==1))
D=((8,7,1,13),(6,5,-1,11)); G=(34,10,21,31)
g=(6,-2,12,1); mark=(5,-3,11,1)
def initial(k):
    F=list(seed(k,'static'))
    for y in range(2):
        i=ix(5,y,0); F[i:i+3]=(D[y],neg(D[y]),G)
    return tuple(F)
def replace(F,p,q):
    assert F[0:2]==(P[p],neg(P[p]))
    out=(P[q],neg(P[q]))+F[2:]
    assert account(F)==account(out)
    # Formal external exchange with a reserve that supplies q and retains p.
    assert account(F+(P[q],neg(P[q])))==account(out+(P[p],neg(P[p])))
    return out
def parts(F,part,keyfn=bits):
    result={}
    for k in keys:result.setdefault(keyfn(k),set()).add(part(F[k]))
    return result
def separated(part):
    a=list(part.values())
    return all(x.isdisjoint(y) for x,y in combinations(a,2))
def clean(part):
    return separated(part) and all(len(x)==1 for x in part.values())
def counts(part):
    return tuple(len(part[k]) for k in sorted(part))
def eqout(F,bit):
    return all(F[k][ix(6,0,2)]==(mark if bit(k) else g) and F[k][ix(6,1,2)]==g for k in keys)
def fact(F):
    left=[];right=[];common=[];other=[]
    for x in ARCH:
        def col(ff):return ff[8*x:8*x+8]
        if len({col(ff) for ff in F.values()})==1:common.append(x)
        elif clean(parts(F,col,lambda k:bits(k)[0])):left.append(x)
        elif clean(parts(F,col,lambda k:bits(k)[1])):right.append(x)
        else:other.append(x)
    return (tuple(left),tuple(right),tuple(common),tuple(other))
def local_reads():
    # Order: kind, column, row, rail(s). Fixed order independent of results.
    for x,y,r in product(ARCH,range(2),(2,3)):
        yield (0,x,y,r),lambda F,x=x,y=y,r=r:F[ix(x,y,r)]
    for x,y in product(ARCH,range(2)):
        for r,s in combinations(range(4),2):
            yield (1,x,y,r,s),lambda F,x=x,y=y,r=r,s=s:sub(F[ix(x,y,r)],F[ix(x,y,s)])
    for x,r in product(ARCH,range(4)):
        yield (2,x,r),lambda F,x=x,r=r:sub(F[ix(x,0,r)],F[ix(x,1,r)])
def digest(F):
    import hashlib
    return hashlib.sha256(';'.join(','.join(map(str,z)) for z in F).encode()).hexdigest()
I=[initial(k) for k in K]
old=[hist(f,244,True) for f in I]
assert len({w[3] for w in old})==1 and H.scalar_account(old[0][3][2])==7752
for t in range(245):
    for stage in ((0,) if t==0 else (1,0)):
        assert len({reader(old[k][stage][t]) for k in N})==1
def run(T):
    base=[w[0][T] for w in old]
    assert all(src(f)==src(I[k]) and worker(f)==worker(I[k]) and account(archive(f))==account(archive(I[k])) for k,f in enumerate(base))
    assert len({archive(base[k]) for k in N})==1 and archive(base[1])!=archive(base[0])
    all25={(p,q):replace(base[p],p,q) for p,q in product(K,repeat=2)}
    F={(a,q):all25[a,q] for a,q in keys} # representative p=0 or p=1
    assert len(set(all25.values()))==len(set(F.values()))==10
    assert all(v==F[int(p==1),q] for (p,q),v in all25.items())
    ac={k:account(v) for k,v in F.items()}
    assert len(set(ac.values()))==1
    print('START',T,'LOADED',len(set(F.values())),'Q',H.scalar_account(next(iter(ac.values()))[2]))
    first_loss=None;history_split=None;first_extra=None
    # Histories prior to load: exactly two first-bit classes, no q-dependence.
    first_seen=separated(parts(F,archive,lambda k:k[0]))
    assert first_seen
    successes=[];resets=[];disjoint=[];exact=[];factor=[];success114=False
    single_resets=Counter();first_single={}
    firstread=None;fixed_loss=None
    all_reader_history={k:k[0] for k in keys}
    hist_id=2
    for t in range(1,4097):
        mids={};nxt={};tags={}
        for k,f in F.items():
            G0,N0,E=step(f,(t-1)%2,ac[k],True)
            mids[k]=G0;nxt[k]=N0;tags[k]=E
        for stage,ff in ((1,mids),(0,nxt)):
            if first_loss is None and not separated(parts(ff,archive,lambda k:k[0])):
                first_loss=(t,stage)
            # Refine the partition of complete reader histories, never just current states.
            mp={}
            for k in keys:
                z=all_reader_history[k],reader(ff[k])
                if z not in mp:mp[z]=len(mp)
                all_reader_history[k]=mp[z]
            hpart=parts(all_reader_history,lambda x:x)
            if history_split is None and any(len(x)>1 for x in hpart.values()):
                history_split=(t,stage,counts(hpart),len(mp))
            if firstread and fixed_loss is None:
                for desc,func,b,vals in firstread:
                    if any(func(ff[k])!=vals[bits(k)[b]] for k in keys):
                        fixed_loss=(t,stage);break
        F=nxt
        if t==6:
            print('WRITE6',T,'CORRECT',sum((F[k][ix(6,0,2)]==(mark if k[1]==1 else g) and F[k][ix(6,1,2)]==g)*(1 if k[0] else 4) for k in keys))
            for k in keys:
                print('WRITE_CASE',T,k,'CLK',F[k][ix(6,0,2)],F[k][ix(6,1,2)],'TAGS',tags[k][12:14])
        if t%2:continue
        ready={k:src(F[k])==src(I[k[1]]) and worker(F[k])==worker(I[k[1]]) for k in keys}
        for k in keys:
            if ready[k]:
                single_resets[k]+=1
                first_single.setdefault(k,t)
        if t==114:
            pp=parts(F,archive)
            print('STRIDE114',T,'READY',sum(ready[k]*(1 if k[0] else 4) for k in keys),'ARCHIVE_COUNTS',counts(pp),'DISJOINT',int(separated(pp)),'FIRST_LOSS',first_loss)
        if not all(ready.values()):continue
        resets.append(t)
        pp=parts(F,archive);clean4=clean(pp);disj=separated(pp)
        if disj:disjoint.append(t)
        if clean4:exact.append(t)
        # Exact restoration makes archive accounts equal their initial post-first-measurement values.
        for k in keys:assert account(archive(F[k]))==account(archive(base[k[0]]))
        fac=fact(F)
        factor_ok=bool(fac[0] and fac[1] and not fac[3])
        if factor_ok:factor.append(t)
        yes=clean4 and first_loss is None
        print('RESET',T,t,'STATES',len({archive(f) for f in F.values()}),'COUNTS',counts(pp),'DISJOINT',int(disj),'FIRST_HELD',int(first_loss is None),'FACTOR',fac)
        if not yes:continue
        successes.append(t)
        if t==114:success114=True
        if len(successes)!=1:continue
        candidates=[[],[]]
        for desc,func in local_reads():
            for b0 in range(2):
                pt=parts(F,func,lambda k:bits(k)[b0])
                if clean(pt):
                    vals=tuple(next(iter(pt[b])) for b in range(2))
                    candidates[b0].append((desc,func,b0,vals))
        print('READS',T,t,'COUNTS',tuple(map(len,candidates)))
        if all(candidates):
            firstread=[v[0] for v in candidates]
            print('READ_PAIR',T,t,tuple((d,b,v) for d,_,b,v in firstread))
        for k in keys:
            print('WITNESS',T,t,k,'BITS',bits(k),'FIELD_SHA',digest(F[k]),'ARCH_ACCOUNT',account(archive(F[k])))
    for p,q in product(K,repeat=2):
        k=(int(p==1),q)
        print('CASE',T,p,q,'BITS',bits(k),'FIRST_RESET',first_single.get(k),'RESET_COUNT',single_resets[k],'FINAL_SHA',digest(F[k]))
    print('SUMMARY',T,'RESETS',resets,'DISJOINT',disjoint,'EXACT4',exact,'SUCCESS',successes,'SUCCESS114',int(success114),'FACTORED',factor,'FIRST_LOSS',first_loss,'HISTORY_SPLIT',history_split,'READ_LOSS',fixed_loss)
for T in (114,198,244):run(T)
print('DONE exact supplied second-input continuation, not a native input loader')
