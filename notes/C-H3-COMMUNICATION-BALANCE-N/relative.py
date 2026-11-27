"""NON-CANONICAL #2123 D, result-exposed relative archive successor."""
from pathlib import Path
import runpy
from itertools import product
from collections import Counter
from fractions import Fraction
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=V['Z'],V['O'],V['R'],V['J'],V['JI'],V['P']
add,sub,mul,sc,h,neg=V['add'],V['sub'],V['mul'],V['sc'],V['h'],V['neg']
seed,cols,hist,account,ix=V['seed'],V['cols'],V['hist'],V['account'],V['ix']
src,worker,archive,reader=V['src'],V['worker'],V['archive'],V['reader']
N,K=V['N'],V['K']
equal,two,neg_equal,rot=V['equal'],V['two'],V['neg_equal'],V['rot']
initial_add=V['initial_add'];ints=V['ints']
T=114;t=113
old=[hist(seed(k,'static'),T,True) for k in K]
u=old[1][0][0][ix(6,0,3)];x=old[1][0][t][ix(6,0,3)]
rp=old[1][0][t][ix(5,0,3)]
ystar=ints(add(x,mul(V['BI'],sub(u,x))))
delta=sub(ystar,rp)
alpha=sc(Fraction(1,2),J);beta=V['beta']
assert H.even(delta) and delta!=Z
assert H.transport_pair(g0:=Z,neg(delta),False)==(neg(mul(beta,delta)),neg(mul(alpha,delta)))
# The written pair is (g-delta,g); the two outputs shift by -alpha*delta,-beta*delta.
port,ref=ix(5,0,2),ix(5,1,2)
def rawpair(F):return F[port],F[ref]
def relation(F):return sub(F[port],F[ref])
def local_end(k,d0,d1,g,tag):
    a0,e0=H.collision(cols(d0,g,old[k][1][t][ix(5,0,3)]))
    a1,e1=H.collision(cols(d1,g,old[k][1][t][ix(5,1,3)]))
    assert (e0,e1)==(tag if k==1 else 0,0)
    if k==1:assert a0[3]==ystar and a0[2]==sub(g,delta)
    ds=H.transport_pair(a0[0],a1[0],False)
    gs=H.transport_pair(a0[2],a1[2],False)
    cs=(H.transport_pair(ystar,x,False)[0] if k==1 else old[k][1][T][ix(5,0,3)],old[k][1][T][ix(5,1,3)])
    r0,e0=H.collision(cols(ds[0],gs[0],cs[0]))
    r1,e1=H.collision(cols(ds[1],gs[1],cs[1]))
    return (r0,r1),(e0,e1)
selected=None;total=Counter()
for tag in (1,2):
    f=ints(mul(delta,H.inverse(sub(O,JI if tag==1 else J))))
    g=add(rp,sc(2,f));base=mul(JI if tag==1 else J,f);stats=Counter()
    ws=(Z,)+tuple(sc(n*s,P[k]) for n,s,k in product((1,3,5),(1,-1),range(5)))
    goal=(ints(sub(g,mul(alpha,delta))),ints(sub(g,mul(beta,delta))))
    for sign,k,w in product((1,-1),range(5),ws):
        d0=mul(base,sc(sign,P[k]));d1=add(d0,sc(2,w));d=rot((d0,d1),t,True)
        stats['tried']+=1
        if not V['pretest'](old,t,d,g,tag):stats['guard_reject']+=1;continue
        r=[local_end(k0,d0,d1,g,tag) for k0 in K]
        pairs=[(a[0][2],a[1][2]) for a,e in r]
        assert all(pairs[k0]==pairs[0] for k0 in N)
        distinct=pairs[1][0]!=pairs[0][0]
        common_ref=all(q[1]==g for q in pairs)
        stats['reference_moved']+=not common_ref
        stats['port_distinct']+=distinct
        stats['port_failed']+=not (distinct and common_ref)
        ok=all(pairs[k0]==(goal if k0==1 else (g,g)) and r[k0][1]==(0,0) for k0 in K)
        stats['relative_target']+=ok
        if ok and tag==1 and selected is None:selected=f,g,d,sign,k,w,goal
    total.update(stats)
    print('D LOCAL_CENSUS',tag,sorted(stats.items()))
print('D TOTAL',sorted(total.items()))
assert total['port_failed']==600
if selected is None:
    print('D NO RELATIVE WITNESS')
    raise SystemExit(0)
f,g,d,sg,k,w,goal=selected
print('D SELECT',f,g,d,sg,k,w,'DELTA',delta,'PAIR_POS',goal,'REL_POS',sub(*goal))
hh=[hist(initial_add(v[0][0],d,g),T+256,True) for v in old]
I=[v[0][0] for v in hh]
assert len({v[3] for v in hh})==1 and len({reader(ff) for ff in I})==1
for k0,v in enumerate(hh):
    for s in range(1,t):
        F=v[0][s]
        assert src(F)==src(old[k0][0][s]) and worker(F)==worker(old[k0][0][s])
        assert all(F[i]==old[k0][0][s][i] for i in range(3,len(F),4)) and v[2][s][10:12]==(0,0)
    assert v[2][t][10:12]==(int(k0==1),0)
    assert v[0][t][ix(5,0,3)]==(ystar if k0==1 else old[k0][0][t][ix(5,0,3)])
    assert v[0][t][port]==(sub(g,delta) if k0==1 else g)
    assert v[2][T][10:12]==(0,0)
    F=v[0][T]
    assert src(F)==src(I[k0]) and worker(F)==worker(I[k0])
    assert rawpair(F)==(goal if k0==1 else (g,g))
    assert relation(F)==(neg(mul(R,delta)) if k0==1 else Z)
    assert account(archive(F))==account(archive(I[k0]))
    print('D WITNESS',k0,'SRC',src(F),'WORKER',worker(F),'ARCHIVE5',F[40:48],'SECTORS',V['delta_accounts'](F,I[k0]))
F=[v[0][T] for v in hh]
assert two(F,archive)
pair_loss=rel_loss=predicate_loss=None
negsame=True;pos_seen=False;first_split=None;resets=[];records=[];pairresets=[];relresets=[];joint=[]
for s in range(T+257):
    for a0 in ((0,) if s==0 else (1,0)):
        FF=[v[a0][s] for v in hh]
        negsame &= neg_equal(FF,reader);pos_seen |= reader(FF[1])!=reader(FF[0])
        if not negsame and first_split is None:first_split=(s,a0)
        if s==T and a0==0:assert negsame and pos_seen
        if s>T:
            if pair_loss is None and any(rawpair(FF[k])!=(goal if k==1 else (g,g)) for k in K):pair_loss=(s,a0)
            if rel_loss is None and any(relation(FF[k])!=(sub(*goal) if k==1 else Z) for k in K):rel_loss=(s,a0)
            if predicate_loss is None and any((relation(FF[k])!=Z)!=(k==1) for k in K):predicate_loss=(s,a0)
        if a0==0 and s>=T and s%2==0 and equal(FF,I,src) and equal(FF,I,worker):
            resets.append(s)
            if two(FF,archive) and negsame and pos_seen:records.append(s)
            if all(rawpair(FF[k])==(goal if k==1 else (g,g)) for k in K):pairresets.append(s)
            if all(relation(FF[k])==(sub(*goal) if k==1 else Z) for k in K):relresets.append(s)
        if a0==0 and s>0 and s%2==0 and FF==I:joint.append(s)
print('D SUMMARY','Q',H.scalar_account(hh[0][3][2]),'H',hh[0][3][2],
      'PAIR_LOSS',pair_loss,'REL_LOSS',rel_loss,'PREDICATE_LOSS_DIAGNOSTIC',predicate_loss,'NEG_SPLIT',first_split,
      'RESETS',resets,'ARCHIVE_RESETS',records,'PAIR_RESETS',pairresets,'REL_RESETS',relresets,'JOINT_RETURNS',joint)
print('D PASS exact complete source and worker restoration with compensated relative archive')
