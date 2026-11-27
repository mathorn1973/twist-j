"""NON-CANONICAL #2121 D, declared after A/B, before execution."""
from pathlib import Path
import runpy
from itertools import product
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=V['Z'],V['O'],V['R'],V['J'],V['JI'],V['P']
add,sub,mul,sc,h,neg=V['add'],V['sub'],V['mul'],V['sc'],V['h'],V['neg']
seed,cols,hist,step,account,ix=V['seed'],V['cols'],V['hist'],V['step'],V['account'],V['ix']
src,worker,store,archive,reader=V['sourcepart'],V['worker'],V['store'],V['archive'],V['reader']
N=(0,2,3,4); K=range(5)
def two(F,part):
    return len({part(F[k]) for k in N})==1 and part(F[1])!=part(F[0])
def returns(F,initial,part):
    return all(part(F[k])==part(initial[k]) for k in K)
def ports(F):
    return [(x,y,q) for x,y,q in product(V['ARCH'],range(2),(2,3))
               if all(F[k][ix(x,y,q)]==F[0][ix(x,y,q)] for k in N)
               and F[1][ix(x,y,q)]!=F[0][ix(x,y,q)]]
def D1():
    out=None
    for variant in V['VARIANTS']:
        hh=[hist(seed(k,variant),4096,True) for k in K]
        ini=[w[0][0] for w in hh]
        if variant=='static':
            joint=[(t%2,tuple(w[0][t] for w in hh)) for t in range(929)]
            assert joint[-1]==joint[0] and len(set(joint[:-1]))==928
            print('D PERIOD static',928,'DISTINCT',len(set(joint[:-1])))
        ne=True;po=False;common=[];qual=[]
        for t in range(1,4097):
            for s in (1,0):
                arr=[reader(w[s][t]) for w in hh]
                ne &= all(arr[k]==arr[0] for k in N);po |= arr[1]!=arr[0]
            F=[w[0][t] for w in hh]
            if t<6 or t%2 or not (returns(F,ini,src) and returns(F,ini,store)):continue
            same=len({worker(f) for f in F})==1
            arc=two(F,archive) and ne and po
            ps=ports(F) if arc else []
            print('D CONTEXT',variant,t,'COMMON_WORKER',int(same),'TWO_ARCHIVE',int(arc),'PORTS',len(ps),'FIRST',ps[0] if ps else None)
            if same and arc and ps:common.append(t)
            if arc and ps and t<928:qual.append(t)
        print('D CONTEXT_SUMMARY',variant,'TIMES',common)
        if variant=='static':out=hh,qual
    assert out is not None
    return out
def rot(pair,n,back=False):
    for _ in range(n%5):pair=H.transport_pair(*pair,back)
    return pair
def prepare(F,x,d,G):
    G0=list(F)
    for y in range(2):
        G0[ix(x,y,0):ix(x,y,0)+3]=(d[y],neg(d[y]),G)
    return tuple(G0)
def pretest(old,x,t,f,w,G):
    ready=mul(JI,f),add(mul(JI,f),sc(2,w));d=rot(ready,t,True)
    cur=d
    for u in range(1,t+1):
        cur=rot(cur,1)
        for k,y in product(K,range(2)):
            if H.collision(cols(cur[y],G,old[k][1][u][ix(x,y,3)]))[1]!=int(u==t and k==1 and y==0):return None
    assert cur==ready
    return d
def continuation(old,x,t,d,G,M):
    hh=[hist(prepare(old[k][0][0],x,d,G),t+256,True) for k in K]
    ini=[w[0][0] for w in hh]
    assert len({w[3] for w in hh})==1
    assert len({reader(f) for f in ini})==1
    port,ref=ix(x,0,2),ix(x,1,2)
    for u in range(1,t):
        for k,w in enumerate(hh):
            if src(w[0][u])!=src(old[k][0][u]) or worker(w[0][u])!=worker(old[k][0][u]) or any(w[0][u][i]!=old[k][0][u][i] for i in range(3,len(ini[k]),4)) or any(w[2][u][2*x:2*x+2]):
                return 'EARLY',None
    F=[w[0][t] for w in hh]
    for k,w in enumerate(hh):
        if w[2][t][2*x:2*x+2]!=(int(k==1),0) or w[1][t][ix(x,0,3)]!=old[k][1][t][ix(x,0,3)] or F[k][port]!=(M if k==1 else G) or F[k][ref]!=G:
            return 'CAPTURE',None
    if not (returns(F,ini,src) and returns(F,ini,store) and two(F,archive)):return 'RESET',None
    ne=True;po=False;active=True;loss=None;weak=[];common=[];full=[]
    for u in range(t+257):
        for s in ((0,) if u==0 else (1,0)):
            arr=[reader(w[s][u]) for w in hh]
            ne &= all(arr[k]==arr[0] for k in N);po |= arr[1]!=arr[0]
            if u>t and active and any(w[s][u][port]!=(M if k==1 else G) or w[s][u][ref]!=G for k,w in enumerate(hh)):
                active=False;loss=(u,s)
        if u==t and not (ne and po):return 'PARTITION',None
        if u<t or u%2 or not (active and ne and po):continue
        F=[w[0][u] for w in hh]
        if not (returns(F,ini,src) and returns(F,ini,store) and two(F,archive)):continue
        weak.append(u)
        if len({worker(f) for f in F})==1:common.append(u)
        if returns(F,ini,worker):full.append(u)
    assert t in weak
    return 'PASS',(hh,weak,common,full,loss)
def D2(old,ts):
    print('D DELAYED_TIMES',ts)
    stats=Counter()
    for t,x in product(ts,(5,7,4,3,2,1)):
        Rp=old[1][1][t][ix(x,0,3)];nv={old[k][1][t][ix(x,0,3)] for k in N}
        if len(nv)!=1 or Rp in nv:stats['cut_reject']+=1;continue
        same=next(((u,k) for u,k in product(range(1,t),K) if (t-u)%5==0 and old[k][1][u][ix(x,0,3)]==Rp),None)
        if same:
            stats['clock_alias']+=1
            print('D LATE_ALIAS',t,x,same)
            continue
        print('D LATE_ELIGIBLE',t,x,'RP',Rp)
        for v,n,w in product(tuple(x for x in product(range(2),repeat=4) if any(x)),(1,3,5),tuple(sc(s,P[k]) for s in (1,-1) for k in range(5))):
            f=sc(n,v);G=add(Rp,sc(2,f));M=add(G,mul(sub(JI,O),f));stats['tried']+=1
            d=pretest(old,x,t,f,w,G)
            if d is None:stats['guard_reject']+=1;continue
            stats['pretest_pass']+=1
            status,info=continuation(old,x,t,d,G,M)
            stats[status]+=1
            if status!='PASS':continue
            hh,weak,common,full,loss=info
            print('D LATE_SELECT',t,x,'F',f,'W',w,'INIT',d,'G',G,'MARK',M,'Q',H.scalar_account(hh[0][3][2]),'WEAK',weak,'COMMON',common,'FULL',full,'LOSS',loss)
            for k in (0,1):
                F=hh[k][0][t];Fi=hh[k][0][0]
                print('D LATE_WITNESS',k,'SOURCE',src(F),'WORKER',worker(F),'ARCHIVE_CELL',F[ix(x,0,0):ix(x,0,0)+8])
                print('D LATE_SECTORS',k,*(tuple(sub(a,b) for a,b in zip(account(part(F)),account(part(Fi)))) for part in (src,worker,archive)))
            print('D LATE_COUNTS',sorted(stats.items()))
            return
    print('D LATE_COUNTS',sorted(stats.items()))
    print('D NO LATE CAPTURE')
if __name__=='__main__':
    old,ts=D1();D2(old,ts)
    print('DONE D exact common-context and delayed archive checks')
