"""NON-CANONICAL result-exposed successor D, frozen #2115 comment 7220474250."""
from pathlib import Path
import runpy
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from collections import Counter

root=Path(__file__).resolve().parent
captured=StringIO()
with redirect_stdout(captured):
    V=runpy.run_path(str(root/'verify.py'))
assert captured.getvalue()==(root/'EXPECTED.txt').read_text()
H=V['H']
O,Z,J,JI=V['O'],V['Z'],V['J'],V['JI']
add,sub,mul,sc,neg=V['add'],V['sub'],V['mul'],V['sc'],V['neg']
idx,cell,hist,account=V['idx'],V['cell'],V['hist'],V['account']
src,reader,prepare=V['src'],V['reader'],V['prepare']
H0,R0=V['H0'],V['R0']
pos,negative=V['pos'],V['negative']
scale_eta=V['scale_eta']
def setup(a,l,r):
    F=list(prepare(l,r))
    g=add(pos,sc(2,a));d=mul(JI,a)
    assert not H.even(d)
    for y in range(8):
        F[idx(1,y,2)]=g
    y=(-2*l)%8
    F[idx(1,y,0)]=d;F[idx(1,y,1)]=neg(d)
    return tuple(F)
def gvals(a):
    g=add(pos,sc(2,a));delta=mul(sub(JI,O),a)
    assert delta!=Z
    return g,add(g,delta)
def initial_idle(a):
    g,_=gvals(a);d=mul(JI,a)
    tags=tuple(H.collision((d,neg(d),g,H0[0][1][t][idx(1,0,3)]))[1] for t in range(1,5))
    return tags
def capture_ok(hs,a,l=0):
    y=(-2*l)%8;g,mark=gvals(a)
    for r,hh in hs.items():
        cuts,mids,tags,ac=hh
        if l==0:
            assert all(src(cuts[t])==src(H0[r][0][t]) for t in range(6))
        assert not any((1,y0) in tags[t] for y0 in range(8) for t in range(1,5))
        positive=(r-l)%4==2
        assert mids[5][idx(1,y,3)]==(pos if positive else negative)
        assert tags[5].get((1,y),0)==int(positive)
        assert cuts[5][idx(1,y,2)]==(mark if positive else g)
        assert cuts[5][idx(1,(y+1)%8,2)]==g
    assert len({H.scalar_account(hh[3][2]) for hh in hs.values()})==1
def hold(hs,a,l=0):
    y=(-2*l)%8;g,mark=gvals(a)
    n=0
    for t in range(6,13):
        for stage in (1,0):
            if not all(hh[stage][t][idx(1,y,2)]==(mark if (r-l)%4==2 else g)
                       and hh[stage][t][idx(1,(y+1)%8,2)]==g for r,hh in hs.items()):
                return n
            n+=1
    return n
records=[];idle_count=0;counts=Counter()
for v,n in product(tuple(x for x in product(range(2),repeat=4) if any(x)),range(1,16,2)):
    a=sc(n,v);tags=initial_idle(a)
    if any(tags):
        print('D CANDIDATE',a,'EARLY_TAGS',tags,'REJECT')
        continue
    idle_count+=1
    hs={r:hist(setup(a,0,r),12) for r in range(4)}
    capture_ok(hs,a)
    n_hold=hold(hs,a);counts[n_hold]+=1
    Q=H.scalar_account(hs[0][3][2])
    records.append((n_hold,a,Q))
    print('D CANDIDATE',a,'EARLY_TAGS',tags,'HOLD',n_hold,'Q',Q)
assert len(records)==idle_count
print('D CENSUS',120,'IDLE',idle_count,'HOLD_HIST',sorted(counts.items()))
if records:
    best=max(records,key=lambda q:q[0])
    length,a,Q=best;g,mark=gvals(a)
    print('D SELECT',a,'HOLD',length,'Q',Q,'G',g,'MARK',mark,'DELTA',sub(mark,g))
    hs={r:hist(setup(a,0,r),160) for r in range(4)}
    capture_ok(hs,a)
    assert hold(hs,a)==length
    for t in range(1,13):
        histories=tuple(tuple(reader(F) for u in range(t+1)
                          for F in ((hh[0][u],) if u==0 else (hh[1][u],hh[0][u])))
                        for hh in hs.values())
        print('D PREFIX',t,'READER_CLASSES',len(set(histories)),'FULL_READER_CLASSES',len({reader(hh[0][t]) for hh in hs.values()}))
    for r,hh in hs.items():
        cut,mid,tags,ac=hh
        print('D RECORD',r,'POST_C5',cell(mid[5],1,0),'FULL5',cell(cut[5],1,0))
        for t in range(1,13):
            print('D LOCAL',r,t,'TAG',tags[t].get((1,0),0),'CLK',cut[t][idx(1,0,2)],'REF',cut[t][idx(1,1,2)])
    for name,mat,initial in (('material_ref',True,False),('full_ref',False,False),('material_initial',True,True)):
        vals=[]
        for t in range(1,161):
            vals.append(sum(src(hs[r][0][t],mat)==tuple(scale_eta(z) for z in src(R0[r][0][0 if initial else t],mat)) for r in range(4)))
        print('D RECOVERY',name,'COMMON',[t for t,n in enumerate(vals,1) if n==4],'HIST',sorted(Counter(vals).items()),
              'CUTS',[(t,vals[t-1]) for t in (5,40,80,120,160)])
    for l in range(4):
        hhs={r:hist(setup(a,l,r),12) for r in range(4)}
        capture_ok(hhs,a,l)
        assert hold(hhs,a,l)==length
        for r,hh in hhs.items():
            yy=(-2*l)%8
            print('D TRANSLATED',l,r,'CLK5',hh[0][5][idx(1,yy,2)],'HOLD',length)
    print('D PASS',16,'FIXED_NATIVE_PORT',1,0,'COMMON_HOLD_SUBSTEPS',length)
else:
    print('D NO CAPTURE')
print('DONE exact separate reader capture')
