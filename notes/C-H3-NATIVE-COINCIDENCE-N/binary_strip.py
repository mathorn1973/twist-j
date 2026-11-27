"""NON-CANONICAL result-exposed successor D, frozen #2113 comment 7220227085."""
import runpy
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from collections import Counter

root=Path(__file__).resolve().parent
captured=StringIO()
with redirect_stdout(captured):
    V=runpy.run_path(str(root/'verify.py'))
assert captured.getvalue()==(root/'EXPECTED.txt').read_text()
H=V['H'];Z,O,R,J=V['Z'],V['O'],V['R'],V['J']
P=V['P'];m=V['m'];A,B=V['A'],V['B']
add,sub,mul,sc,h=V['add'],V['sub'],V['mul'],V['sc'],V['h']
neg=V['neg'];seed0=V['seed'];cell=V['cell'];idx=V['idx'];run=V['run']
raw=V['raw'];mask=V['mask'];bits_at=V['bits_at'];actual_half=V['actual_half']
Rwrite=V['Rwrite'];other=V['other']
Hstar=sc(m,sub(sub(sc(-4,O),sc(2,R)),mul(R,B)))
assert all(int(z)==z for z in Hstar)
Hstar=tuple(int(z) for z in Hstar)
left=sc(-2*m,J)
start=H.transport_pair(left,Hstar,True)
assert H.transport_pair(*start,False)==(left,Hstar)
print('D STOCK',Hstar,'INVERSE_PAIR',start)
def seed(r,u,k=1,l=2,v=3,w=4):
    F=list(seed0(r,u,k,l,v,w))
    for x,y in product(range(8),repeat=2):
        if x in (1,2,3):
            F[idx(x,y,0)]=F[idx(x,y,1)]=Z
        if x in (0,1,2,3):
            F[idx(x,y,3)]=(start[x] if x<2 else Hstar) if y%2==0 else Z
    return tuple(F)
def strip(F):
    return tuple(F[idx(0,y,2)] for y in range(0,8,2))
def predicted(r,u):
    return tuple(Rwrite if r==u and y==-2*r%8 else Z for y in range(0,8,2))
cases=tuple(product(range(4),repeat=2))
hs={};qvals=set();local_types={}
for r,u in cases:
    hist=run(seed(r,u),160);cuts,mids,tags,ac=hist;hs[r,u]=hist
    Q=H.scalar_account(ac[2]);qvals.add(Q)
    original=run(seed0(r,u),2)
    for t in (1,2):
        for x,y in product((0,7),range(8)):
            assert cell(mids[t],x,y)==cell(original[1][t],x,y)
            assert cell(cuts[t],x,y)==cell(original[0][t],x,y)
        assert not any(x in (1,2,3) for x,y in tags[t])
    for y in range(0,8,2):
        a,b=bits_at(r,u,y)
        assert cell(cuts[2],1,y)[3]==Hstar
        assert cell(mids[3],0,y)[:3]==cell(cuts[2],0,y)[:3]
        assert H.even(sub(cell(cuts[2],0,y)[3],Hstar))
        expect=H.transport_pair(cell(cuts[2],0,y)[3],Hstar,False)
        assert (cell(mids[3],0,y)[3],cell(mids[3],1,y)[3])==expect
        assert expect[0]!=cell(cuts[2],0,y)[3]
        if a and not b:
            assert actual_half(cell(mids[3],0,y))==sc(m,O)
        assert tags[3].get((0,y),0)==2*(a and not b)
        p,q=V['local_type'](r,u,y)
        key=P.index(p),P.index(q)
        val=(cell(cuts[2],0,y),cell(mids[3],0,y),cell(cuts[3],0,y),tags[3].get((0,y),0))
        assert key not in local_types or local_types[key]==val
        local_types[key]=val
    assert strip(cuts[3])==predicted(r,u)
    print('D CASE',r,u,'STRIP',strip(cuts[3]),'Q',Q,'H',ac[2])
assert len(qvals)==1 and len(local_types)==9
for key,(before,mid,after,tag) in sorted(local_types.items()):
    print('D LOCAL',*key,'FULL2',raw(before),'PRE3',raw(mid),'FULL3',raw(after),'TAG',tag)
print('D PASS',len(hs),'POSITIVE',sum(sum(mask(hs[p][0][3])) for p in cases),'Q',next(iter(qvals)))
for t in range(4,13):
    mid=sum(strip(hs[r,u][1][t])==predicted(r,u) for r,u in cases)
    full=sum(strip(hs[r,u][0][t])==predicted(r,u) for r,u in cases)
    print('D HOLD',t,'POST_C',mid,'FULL',full)
for r,u in cases:
    cuts,mids,tags,ac=hs[r,u]
    n=0;ok=True
    for t in range(4,13):
        for F in (mids[t],cuts[t]):
            if strip(F)!=predicted(r,u):ok=False;break
            n+=1
        if not ok:break
    print('D HOLD_PREFIX_SUBSTEPS',r,u,n)
for n in range(1,5):
    t=n*40
    print('D STROKE',t,'COMPLETE_MATCHES',sum(hs[r,u][0][t]==seed((r+n)%4,(u+n)%4) for r,u in cases))
records=[]
for t,x,y in product(range(3,161),range(8),range(8)):
    pos={hs[r,u][0][t][idx(x,y,2)] for r,u in cases if r==u}
    negs={hs[r,u][0][t][idx(x,y,2)] for r,u in cases if r!=u}
    if len(pos)==len(negs)==1 and pos!=negs:
        records.append((t,x,y,next(iter(pos)),next(iter(negs))))
print('D FIXED_BINARY_RECORDS',len(records))
if records:print('D FIRST',records[0])
controls=((0,0,3,4),(1,1,3,4),(2,2,3,4),(1,2,0,0),(1,2,3,3),(1,2,4,4))
for k,l,v,w in controls:
    out=Counter();binary=0
    for r,u in cases:
        cut=run(seed(r,u,k,l,v,w),3)[0]
        out[sum(mask(cut[3]))]+=1
        binary+=all(z in (Z,Rwrite) for z in strip(cut[3]))
    print('D CONTROL',k,l,v,w,'R_COUNTS',sorted(out.items()),'BINARY',binary)
print('D EMPTY',strip(run(seed(0,0,0,0,0,0),3)[0][3]))
print('DONE exact binary-strip successor')
