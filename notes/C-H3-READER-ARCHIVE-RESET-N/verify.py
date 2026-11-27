"""NON-CANONICAL #2121, source/worker recovery and separate archive."""
from pathlib import Path
import hashlib,sys,importlib.util
from itertools import product
from functools import cache
from collections import Counter
source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H;spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,R,J,JI,P=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV,H.J_POWERS
add,sub,mul,sc,h=H.add,H.sub,cache(H.mul),H.scale,H.h
neg=lambda x:sc(-1,x)
L=sub(O,R);m=sub(sc(2,O),R);gs=sc(2,mul(J,m));a=sc(-3,L)
b=add(add(mul(m,R),mul(J,a)),sc(12,J))
stock=(Z,Z,Z,b,b,b,add(mul(m,R),sc(2,a)))
g=(6,-2,12,1);mark=(5,-3,11,1)
N=(0,2,3,4)
CASES=tuple(range(5))
VARIANTS=('static','rotating')
ARCH=(1,2,3,4,5,7)
ix=lambda x,y,q:H.index(2,x,y,q)
def cols(d,g,c):return d,neg(d),g,c
def rs(xs):return tuple(map(sum,zip(*xs)))
def account(F):
    return rs(z for i,z in enumerate(F) if i%4<2),rs(z for i,z in enumerate(F) if i%4>=2),rs(h(z) for z in F)
def seed(k,variant):
    d0=(JI,JI) if variant=='static' else ((1,-1,-1,-1),(1,-1,-1,1))
    F=[]
    for x,y in product(range(8),range(2)):
        d=(P[k] if y==0 else sc(3,P[1])) if x==0 else d0[y] if x==6 else Z
        clk=gs if x==0 else g if x==6 else Z
        c=(Z if x==0 else stock[x-1]) if y==0 else gs
        F.extend(cols(d,clk,c))
    return tuple(F)
def sourcepart(F):return F[:8]
def worker(F):return F[48:56]
def store(F):return tuple(F[ix(6,y,q)] for y,q in product(range(2),range(3)))
def archive(F):return tuple(F[ix(x,y,q)] for x,y,q in product(ARCH,range(2),range(4)))
def reader(F):return F[8:]
edges=[]
for bit in range(2):
    es=[(ix(x,bit,q),ix(x,1-bit,q)) for x,q in product(range(8),range(3))]
    es += [(ix(x,y,3),ix((x+1)%8,y,3)) for x,y in product(range(bit,8,2),range(2))]
    edges.append(tuple(es))
def trans(F,bit,back=False):
    G=list(F)
    for i,k in edges[bit]:G[i],G[k]=H.transport_pair(F[i],F[k],back)
    return tuple(G)
def collide(F):
    G=[];ts=[]
    for i in range(0,len(F),4):
        c,t=H.collision(F[i:i+4]);G.extend(c);ts.append(t)
    return tuple(G),tuple(ts)
def step(F,bit,ac,literal=False):
    G=trans(F,bit);V,ts=collide(G)
    assert account(G)==account(V)==ac
    back,_=collide(V)
    assert back==G and trans(back,bit,True)==F
    if literal:
        assert H.transport(F,2,bit)==G
        V0,ev=H.collide(G,2)
        assert V0==V
        assert H.transport(back,2,bit,backward=True)==F
        assert ts==tuple(dict(((x,y),t) for x,y,t in ev).get((x,y),0) for x,y in product(range(8),range(2)))
    return G,V,ts
def hist(F,n,literal=False):
    ac=account(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac,literal);cuts.append(F);mids.append(G);tags.append(E)
    return cuts,mids,tags,ac
def two(states,part=reader):
    return len({part(states[k]) for k in N})==1 and part(states[1])!=part(states[0])
def partition_history(hh,t):
    # Entire negative history identical and positive history differs.
    ne=True;po=False
    for u in range(t+1):
        for s in ((0,) if u==0 else (1,0)):
            arr=[reader(hh[k][s][u]) for k in CASES]
            ne &= all(arr[k]==arr[0] for k in N)
            po |= arr[1]!=arr[0]
    return ne,po
def hold(hh,t,port,negval,posval,last):
    for u in range(t+1,last+1):
        for s in (1,0):
            if any(hh[k][s][u][port]!=(posval if k==1 else negval) for k in CASES):return u,s
    return None
def scan_A(variant,horizon=4096):
    hh=[hist(seed(k,variant),horizon,True) for k in CASES]
    assert len({w[3] for w in hh})==1
    assert H.scalar_account(hh[0][3][2])==(2630 if variant=='static' else 2654)
    for k,w in enumerate(hh):
        assert w[0][6][ix(6,0,2)]==(mark if k==1 else g)
        assert w[0][6][ix(6,1,2)]==g
        assert w[2][6][12:14]==(int(k==1),0)
    loss=next(( (t,s) for t in range(7,161) for s in (1,0) if any(hh[k][s][t][ix(6,0,2)]!=(mark if k==1 else g) or hh[k][s][t][ix(6,1,2)]!=g for k in CASES)),None)
    assert loss==(111,0)
    initial=[w[0][0] for w in hh];R0=[];W0=[];both=[];full=[];fullfield=[]
    ne=True;po=False;firstweak=None;firstfull=None;counts=Counter()
    for t in range(1,horizon+1):
        for s in (1,0):
            arr=[reader(w[s][t]) for w in hh]
            ne &= all(arr[k]==arr[0] for k in N)
            po |= arr[1]!=arr[0]
        F=[w[0][t] for w in hh]
        S=all(sourcepart(F[k])==sourcepart(initial[k]) for k in CASES)
        W=all(store(F[k])==store(initial[k]) for k in CASES)
        U=all(worker(F[k])==worker(initial[k]) for k in CASES)
        if W and t>=6:W0.append(t)
        if t%2 or t<6:continue
        if S:R0.append(t)
        if all(F[k]==initial[k] for k in CASES):fullfield.append(t)
        if not (S and W):continue
        both.append(t)
        if U:full.append(t)
        ok=two(F,archive) and ne and po
        ports=[(x,y,q) for x,y,q in product(ARCH,range(2),(2,3))
               if all(F[k][ix(x,y,q)]==F[0][ix(x,y,q)] for k in N) and F[1][ix(x,y,q)]!=F[0][ix(x,y,q)]]
        counts['weak_record']+=bool(ok and ports)
        counts['full_record']+=bool(U and ok and ports)
        print('A CUT',variant,t,'FULL_WORKER',int(U),'TWO_ARCHIVE',int(ok),'PORTS',len(ports))
        if ok and ports:
            x,y,q=ports[0];port=ix(x,y,q);info=(t,x,y,q,F[0][port],F[1][port],hold(hh,t,port,F[0][port],F[1][port],horizon))
            if firstweak is None:firstweak=info
            if U and firstfull is None:firstfull=info
    assert [t for t in R0 if 6<=t<=110]==[16,30,44,58,72,86,100]
    print('A SUMMARY',variant,'Q',H.scalar_account(hh[0][3][2]),'WORKER_STORE_FIRST',W0[0] if W0 else None,'SOURCE_RETURNS',R0,'STORE_AND_SOURCE',both,'FULL_WORKER_AND_SOURCE',full,'FULL_FIELD',fullfield)
    print('A RECORDS',variant,sorted(counts.items()),'FIRST_WEAK',firstweak,'FIRST_FULL',firstfull,'NEG_HISTORY_EQUAL',int(ne))
    # On a selected endpoint compare full exact sector accounts.
    if firstweak:
        t=firstweak[0]
        for k in (0,1):
            F=hh[k][0][t];Fi=initial[k]
            print('A SECTORS',variant,t,k,'SOURCE_DELTA',tuple(sub(x,y) for x,y in zip(account(sourcepart(F)),account(sourcepart(Fi)))),'WORKER_DELTA',tuple(sub(x,y) for x,y in zip(account(worker(F)),account(worker(Fi)))),'ARCH_DELTA',tuple(sub(x,y) for x,y in zip(account(archive(F)),account(archive(Fi)))))
    return hh
if __name__=='__main__':
    for variant in VARIANTS:scan_A(variant)
    print('DONE A exact worker/record recurrence census')
