"""NON-CANONICAL C: equal-account echo capture, frozen comment 7220694517."""
from pathlib import Path
import runpy,ast,re
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from collections import Counter
root=Path(__file__).resolve().parent
captured=StringIO()
with redirect_stdout(captured):
    V=runpy.run_path(str(root/'verify.py'))
assert captured.getvalue()==(root/'A.txt').read_text()
H=V['H'];Z,O,R,J,JI,P=V['Z'],V['O'],V['R'],V['J'],V['JI'],V['P']
L,T=V['L'],V['T']
add,sub,mul,sc,h,neg=V['add'],V['sub'],V['mul'],V['sc'],V['h'],V['neg']
idx,cell,src,reader,acc,hist,word=V['idx'],V['cell'],V['src'],V['reader'],V['acc'],V['hist'],V['word']
m=sub(sc(2,O),R);gsource=sc(2,mul(J,m));mR=mul(m,R)
values=(Z,)+tuple(sc(s,P[k]) for s in (1,-1) for k in range(5))
stocks=[]
for line in (root/'B.txt').read_text().splitlines():
    mat=re.match(r'^B STOCK (-?\d+) (\d+) (\d+) .* MATCHES (\[.*?\]) NEGATIVE_SPLIT ',line)
    if mat:
        n,l,vi=map(int,mat.groups()[:3]);ts=ast.literal_eval(mat[4])
        if ts:stocks.append((n,l,vi,ts[0]))
assert len(stocks)==143 and stocks[0]==(-3,0,0,24)
def base(n,l,vi,p):
    u=sc(n,P[l]);a=mul(L,u);v=values[vi]
    b=sub(add(mR,mul(J,a)),sc(4,mul(J,u)))
    stock=(Z,sc(2,v),sc(2,v),b,b,b,add(mR,sc(2,a)))
    F=[]
    for x,y in product(range(8),range(2)):
        d=(p if y==0 else sc(3,P[1])) if x==0 else Z
        clk=gsource if x==0 else Z
        c=(Z if x==0 else stock[x-1]) if y==0 else gsource
        F.extend((d,neg(d),clk,c))
    return tuple(F)
def setup(F,a,g):
    N=list(F);d=mul(JI,a)
    assert not H.even(d)
    for y in range(2):N[idx(6,y,2)]=g
    N[idx(6,0,0)]=d;N[idx(6,0,1)]=neg(d)
    return tuple(N)
port=idx(6,0,2);ref=idx(6,1,2);corr=idx(6,0,3)
negks=(0,2,3,4)
def continuation(hs,old,T,g,mark):
    acs=set()
    for k,hh in hs.items():
        cuts,mids,tags,ac=hh;acs.add(ac[2])
        for t in range(T+1):
            assert src(cuts[t])==src(old[k][0][t])
            for i in range(3,len(cuts[t]),4):
                if i==corr and t==T:continue
                assert cuts[t][i]==old[k][0][t][i]
        assert cuts[T][port]==(mark if k==1 else g)
        assert cuts[T][ref]==g
        assert src(cuts[T])==src(cuts[0])
        assert tags[T].get((6,0),0)==int(k==1)
        assert not any((6,0) in tags[t] for t in range(1,T))
    assert len(acs)==1
    assert len({word(hh,T) for hh in hs.values()})==2
    assert len({word(hs[k],T) for k in negks})==1
    n=0
    for t in range(T+1,T+9):
        for stage in (1,0):
            if not all(hh[stage][t][port]==(mark if k==1 else g) and hh[stage][t][ref]==g for k,hh in hs.items()):return n
            n+=1
    return n
for n,l,vi,Tcut in stocks:
    old={k:hist(base(n,l,vi,p),Tcut) for k,p in enumerate(P)}
    Rpos=old[1][0][Tcut][corr];Rneg=old[0][0][Tcut][corr]
    assert Rpos!=Rneg and all(old[k][0][Tcut][corr]==Rneg for k in negks)
    assert all(hh[0][Tcut][corr]==hh[1][Tcut][corr] for hh in old.values())
    print('C STOCK',n,l,vi,Tcut,'POS',Rpos,'NEG',Rneg)
    wins=[];reject=Counter();hold_hist=Counter()
    for v,mult in product(tuple(x for x in product(range(2),repeat=4) if any(x)),range(1,16,2)):
        a=sc(mult,v);g=add(Rpos,sc(2,a));d=mul(JI,a)
        early=[]
        for t in range(1,Tcut):
            for k,hh in old.items():
                tag=H.collision((d,neg(d),g,hh[1][t][corr]))[1]
                if tag:early.append((t,k,tag))
        if early:
            reject['early']+=1
            print('C CANDIDATE',a,'REJECT_EARLY',early[0]);continue
        tags=tuple(H.collision((d,neg(d),g,old[k][1][Tcut][corr]))[1] for k in range(5))
        if tags!=(0,1,0,0,0):
            reject['target']+=1
            print('C CANDIDATE',a,'REJECT_TARGET',tags);continue
        mark=add(g,mul(sub(JI,O),a));assert mark!=g
        hs={k:hist(setup(hh[0][0],a,g),Tcut+8) for k,hh in old.items()}
        for k,hh in hs.items():assert reader(hh[0][0])==reader(hs[0][0][0])
        hold=continuation(hs,old,Tcut,g,mark)
        hold_hist[hold]+=1;wins.append((hold,a,g,mark))
        print('C CANDIDATE',a,'HOLD',hold,'Q',H.scalar_account(hs[0][3][2]))
    print('C CENSUS',n,l,vi,'REJECT',sorted(reject.items()),'HOLD_HIST',sorted(hold_hist.items()))
    if wins:
        hold,a,g,mark=max(wins,key=lambda x:x[0])
        hs={k:hist(setup(hh[0][0],a,g),Tcut+8) for k,hh in old.items()}
        assert continuation(hs,old,Tcut,g,mark)==hold
        Q=H.scalar_account(hs[0][3][2])
        print('C SELECT',n,l,vi,Tcut,'A',a,'G',g,'MARK',mark,'DELTA',sub(mark,g),'HOLD',hold,'Q',Q,'H',hs[0][3][2])
        for k,hh in hs.items():
            cut,mid,tags,ac=hh
            print('C WITNESS',k,'SOURCE',src(cut[Tcut]),'PORT',cut[Tcut][port],'REFERENCE',cut[Tcut][ref],'Q',H.scalar_account(ac[2]))
        for t in range(Tcut+9):
            print('C PREFIX',t,'CLASSES',len({word(hh,t) for hh in hs.values()}),'SOURCE_MATCH',sum(src(hh[0][t])==src(hh[0][0]) for hh in hs.values()))
        print('C PASS 5/5 native CLK record and literal source return')
        break
else:print('C NO CAPTURE')
print('DONE exact equal-account source echo capture')
