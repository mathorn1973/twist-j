"""NON-CANONICAL #2125 D/E, declared after A and before these diagnostics."""
from pathlib import Path
import runpy,hashlib
from itertools import product,combinations
from collections import Counter
from fractions import Fraction as Q
root=Path(__file__).resolve().parent
assert hashlib.sha256((root/'predecessor.py').read_bytes()).hexdigest()=='ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95'
V=runpy.run_path(str(root/'predecessor.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
hist,step,seed,account,ix=map(V.get,('hist','step','seed','account','ix'))
src,worker,archive,reader=map(V.get,('sourcepart','worker','archive','reader'))
N=(0,2,3,4); K=range(5); ARCH=(1,2,3,4,5,7)
keys=tuple(product(range(2),K)); reps=tuple(product(range(2),range(2)))
bits=lambda k:(k[0],int(k[1]==1))
D=((8,7,1,13),(6,5,-1,11)); G=(34,10,21,31)
g=(6,-2,12,1); mark=(5,-3,11,1)
def setup(F,d,g0):
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
def parts(F,part,keyfn=bits):
    out={}
    for k,f in F.items():out.setdefault(keyfn(k),set()).add(part(f))
    return out
def disj(part):
    return all(a.isdisjoint(b) for a,b in combinations(part.values(),2))
def clean(part):
    return disj(part) and all(len(x)==1 for x in part.values())
def counts(part):return tuple(len(part[k]) for k in sorted(part))
def digest(F):
    return hashlib.sha256(';'.join(','.join(map(str,z)) for z in F).encode()).hexdigest()
def col(F,x):return F[8*x:8*x+8]
def readset():
    for x,y,r in product(ARCH,range(2),(2,3)):
        yield (0,x,y,r),lambda F,x=x,y=y,r=r:F[ix(x,y,r)]
    for x,y in product(ARCH,range(2)):
        for r,s in combinations(range(4),2):
            yield (1,x,y,r,s),lambda F,x=x,y=y,r=r,s=s:sub(F[ix(x,y,r)],F[ix(x,y,s)])
    for x,r in product(ARCH,range(4)):
        yield (2,x,r),lambda F,x=x,r=r:sub(F[ix(x,0,r)],F[ix(x,1,r)])
def read_class(F):
    reads=list(readset())
    independent=[[v for v in reads if clean(parts(F,v[1],lambda k,b=b:bits(k)[b]))] for b in range(2)]
    four=[v for v in reads if clean(parts(F,v[1]))]
    if all(independent):pick=[v[0] for v in independent]
    else:
        pair=next(((a,b) for a,b in combinations(reads,2) if clean(parts(F,lambda f,a=a,b=b:(a[1](f),b[1](f))))),None)
        pick=list(pair) if pair else []
    print('READ_CLASS','INDEPENDENT',tuple(map(len,independent)),'FOUR_SINGLE',len(four),'FIRST_FOUR',four[0][0] if four else None,
          'PICK',tuple(v[0] for v in pick))
    if not pick and four:pick=[four[0]]
    return pick
def class_read_values(F,pick):
    f=lambda ff:tuple(v[1](ff) for v in pick)
    assert clean(parts(F,f))
    vals={bits(k):f(ff) for k,ff in F.items()}
    return f,vals
def audit_cols(F):
    for x in ARCH:
        p=parts(F,lambda f,x=x:col(f,x))
        only=tuple(int(clean(parts(F,lambda f,x=x:col(f,x),lambda k,b=b:bits(k)[b]))) for b in range(2))
        print('COLUMN',x,'DISTINCT',len({col(f,x) for f in F.values()}),'COUNTS',counts(p),'BIT_ONLY',only)
I=[setup(seed(k,'static'),D,G) for k in K]
basehist=[hist(f,244,True) for f in I]
assert len({w[3] for w in basehist})==1
def D_gate(T):
    base=[w[0][T] for w in basehist]
    F={(a,q):replace(base[a],a,q) for a,q in keys}
    ac={k:account(f) for k,f in F.items()}
    hh={k:hist(f,256,True) for k,f in F.items()}
    old_classes={k:k[0] for k in keys};first_hist=None
    for t in range(1,257):
        for st in (1,0):
            cuts={k:w[st][t] for k,w in hh.items()}
            mp={}
            for k in keys:
                z=old_classes[k],reader(cuts[k])
                if z not in mp:mp[z]=len(mp)
                old_classes[k]=mp[z]
            if first_hist is None and clean(parts(old_classes,lambda x:x)):first_hist=(t,st)
    print('D START',T,'FIRST_FOUR_HISTORIES',first_hist)
    for k in reps:
        w=hh[k];c=w[1][6][48:52]
        d=sc(Q(1,2),sub(c[0],c[1]));f=sc(Q(1,2),sub(c[2],c[3]))
        print('D PRE6',T,k,'CELL',c,'H_D',tuple(map(str,h(d))),'H_F',tuple(map(str,h(f))),
              'PARITY',int(H.even(sub(c[0],c[1]))),int(H.even(sub(c[2],c[3]))),'TAG',w[2][6][12])
    print('D POS_CORR_DIFF',T,sub(hh[1,1][1][6][ix(6,0,3)],hh[0,1][1][6][ix(6,0,3)]))
    F={k:w[0][114] for k,w in hh.items()}
    assert clean(parts(F,archive))
    print('D RESET114',T,tuple(sum((1 if k[0] else 4) for k,f in F.items() if bits(k)==b and src(f)==src(I[k[1]]) and worker(f)==worker(I[k[1]])) for b in reps))
    for k in reps:print('D ARCH114',T,k,'SHA',digest(archive(F[k])),'SOURCE_READY',int(src(F[k])==src(I[k[1]])),'WORKER_READY',int(worker(F[k])==worker(I[k[1]])))
    audit_cols(F)
    pick=read_class(F)
    if pick:
        fn,vals=class_read_values(F,pick)
        print('D READ',T,tuple(v[0] for v in pick),'VALUES',tuple(sorted(vals.items())))
        exactloss=seploss=None
        for t in range(115,257):
            for st in (1,0):
                ff={k:w[st][t] for k,w in hh.items()}
                if exactloss is None and any(fn(v)!=vals[bits(k)] for k,v in ff.items()):exactloss=(t,st)
                if seploss is None and not clean(parts(ff,fn)):seploss=(t,st)
        print('D READ_LOSS',T,exactloss,seploss)

def rot(pair,n,back=False):
    for _ in range(n%5):pair=H.transport_pair(*pair,back)
    return pair
def E_gate():
    I0=[seed(k,'static') for k in K]
    old=[hist(f,114,True) for f in I0]
    delta=(12,0,6,6);rp=(-2,-2,9,-5);t=113
    ws=(Z,)+tuple(sc(n*s,P[k]) for n,s,k in product((1,3,5),(1,-1),range(5)))
    stats=Counter();first_ready=None
    for tag in (1,2):
        f=mul(delta,H.inverse(sub(O,JI if tag==1 else J)))
        assert all(Q(v).denominator==1 for v in f)
        f=tuple(map(int,f));g0=add(rp,sc(2,f));b=mul(JI if tag==1 else J,f)
        local=Counter()
        for sign,k,w in product((1,-1),K,ws):
            d0=mul(b,sc(sign,P[k]));d=rot((d0,add(d0,sc(2,w))),t,True)
            stats['tried']+=1;local['tried']+=1;cur=d;ok=True
            for u in range(1,t+1):
                cur=rot(cur,1)
                if any(H.collision((cur[y],neg(cur[y]),g0,old[k0][1][u][ix(5,y,3)]))[1]!=(tag if u==t and k0==1 and y==0 else 0)
                       for k0,y in product(K,range(2))):
                    ok=False;break
            if not ok:
                stats['guard_reject']+=1;local['guard_reject']+=1;continue
            assert cur==(d0,add(d0,sc(2,w)))
            stats['admitted']+=1;local['admitted']+=1
            base=[];prep=[]
            for k0 in K:
                F0=setup(I0[k0],d,g0);ac=account(F0);prep.append(F0)
                F112=setup(old[k0][0][112],rot(d,112),g0)
                assert account(F112)==ac
                _,F113,tt=step(F112,0,ac,True)
                assert tt[10:12]==(tag if k0==1 else 0,0)
                assert F113[ix(5,0,3)]==add(old[k0][0][113][ix(5,0,3)],delta if k0==1 else Z)
                _,F114,tt=step(F113,1,ac,True)
                assert src(F114)==src(F0) and worker(F114)==worker(F0) and account(archive(F114))==account(archive(F0))
                base.append(F114)
            assert len({archive(base[k0]) for k0 in N})==1 and archive(base[0])!=archive(base[1])
            F={k0:replace(base[k0[0]],k0[0],k0[1]) for k0 in reps}
            ac={k0:account(ff) for k0,ff in F.items()}
            for u in range(1,7):
                md={};cut={};ts={}
                for k0,ff in F.items():md[k0],cut[k0],ts[k0]=step(ff,(u-1)%2,ac[k0],True)
                F=cut
            pattern=tuple(int(F[k0][ix(6,0,2)]==(mark if k0[1]==1 else g) and F[k0][ix(6,1,2)]==g) for k0 in reps)
            local['screen_'+''.join(map(str,pattern))]+=1
            stats['screen_'+''.join(map(str,pattern))]+=1
            if not all(pattern):
                continue
            if first_ready is None:
                first_ready=tag,sign,k,w,d,g0
                print('E FIRST_READY',first_ready,'PRE6',tuple(md[k0][48:52] for k0 in reps))
            # all ten distinct second input states; preserve full exact read and reset target.
            F={k0:replace(base[k0[0]],k0[0],k0[1]) for k0 in keys}
            ac={k0:account(ff) for k0,ff in F.items()}
            held=True
            for u in range(1,513):
                md={};cut={}
                for k0,ff in F.items():md[k0],cut[k0],_=step(ff,(u-1)%2,ac[k0],True)
                held &= all(disj(parts(ff,archive,lambda kk:kk[0])) for ff in (md,cut))
                F=cut
                if u==6 and not all(F[k0][ix(6,0,2)]==(mark if k0[1]==1 else g) and F[k0][ix(6,1,2)]==g for k0 in keys):break
                if u<6 or u%2 or not held:continue
                if all(src(ff)==src(prep[k0[1]]) and worker(ff)==worker(prep[k0[1]]) for k0,ff in F.items()) and clean(parts(F,archive)):
                    stats['success']+=1;local['success']+=1
                    print('E SELECT',tag,sign,k,w,d,g0,'T',u,'Q',H.scalar_account(ac[0,0][2]))
                    # Literal first histories and all 25 exchanges, no compressed positive evidence.
                    hh=[hist(ff,114,True) for ff in prep]
                    assert [z[0][114] for z in hh]==base
                    literal={(p,q):hist(replace(base[p],p,q),u,True) for p,q in product(K,repeat=2)}
                    for (p,q),z in literal.items():
                        assert z[0][u]==F[int(p==1),q]
                        assert z[0][6][ix(6,0,2)]==(mark if q==1 else g) and z[0][6][ix(6,1,2)]==g
                    pick=read_class(F)
                    if pick:
                        fn,vals=class_read_values(F,pick)
                        print('E READ',tuple(v[0] for v in pick),tuple(sorted(vals.items())))
                    audit_cols(F)
                    print('E LOCAL',tag,sorted(local.items()))
                    print('E COUNTS',sorted(stats.items()))
                    return
            stats['no_endpoint']+=1;local['no_endpoint']+=1
        print('E LOCAL',tag,sorted(local.items()))
    print('E COUNTS',sorted(stats.items()),'FIRST_READY',first_ready)
    print('E NO QUALIFYING SECOND READ')
if __name__=='__main__':
    for T in (114,198,244):D_gate(T)
    E_gate()
    print('DONE D/E exact diagnostic and bounded family')
