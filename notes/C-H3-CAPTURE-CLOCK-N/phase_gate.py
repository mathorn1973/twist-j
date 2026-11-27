"""NON-CANONICAL E: constant-input native phase gate, #2119 comment 7221916857."""
from pathlib import Path
import runpy
from itertools import product
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=V['Z'],V['O'],V['R'],V['J'],V['JI'],V['P']
add,sub,mul,sc,h,neg=V['add'],V['sub'],V['mul'],V['sc'],V['h'],V['neg']
hist,matter,cols,ix=V['hist'],V['matter'],V['cols'],V['ix']
phi=neg(add(P[2],P[3]));w=add(sc(2,O),P[1])
D=add(w,P[1]);f=mul(J,D);g=sc(2,f)
assert D==add(w,P[6%5])
mark=add(g,mul(sub(JI,O),f))
norms=tuple(h(add(w,p)) for p in P)
assert norms==tuple(add(sc(a,O),sc(b,phi)) for a,b in ((7,3),(4,4),(3,1),(4,-1),(2,3)))
assert len(set(norms))==5 and all(x!=mul(mul(H.T,H.T),h(D)) for x in norms)
print('E NORMS',norms,'D',D,'F',f,'G',g,'MARK',mark)
base=None
for q in range(6):
    label=str(q) if q<5 else 'static'
    d=(add(w,P[(2*q)%5]),sub(w,P[(2*q)%5])) if q<5 else (D,D)
    F=tuple(z for x,y in product(range(8),range(2)) for z in cols(d[y] if x==6 else Z,g if x==6 else Z,Z if y==0 else g))
    cut,mid,tags,ac=hist(F,12,True)
    if q==0:base=ac
    if q<5:assert ac==base
    t0=next(t for t in range(1,13) if any(tags[t]))
    goal=(3-q-1)%5+1 if q<5 else 1
    assert t0==goal
    for t in range(1,goal+1):
        assert matter(mid[t],6)==((add(w,P[2*(q+t)%5]),sub(w,P[2*(q+t)%5])) if q<5 else (D,D))
        assert mid[t][ix(6,0,2)]==g and mid[t][ix(6,0,3)]==Z
        assert mid[t][ix(6,1,2)]==mid[t][ix(6,1,3)]==g
        assert tags[t]==tuple(int(t==goal and i==12) for i in range(16))
    assert cut[goal][ix(6,0,2)]==mark and cut[goal][ix(6,1,2)]==g
    change=next(((t,s) for t in range(goal+1,13) for s,F1 in ((1,mid[t]),(0,cut[t])) if F1[ix(6,0,2)]!=mark or F1[ix(6,1,2)]!=g),None)
    print('E CASE',label,'D_INIT',d,'ACCOUNT',ac,'Q',H.scalar_account(ac[2]),'FIRST',t0,'OUTPUT',cut[t0][ix(6,0,2)],'FIRST_CHANGE',change)
    for t in range(1,13):
        print('E TICK',label,t,'PRE',matter(mid[t],6),'TAGS',tags[t],'CLK',cut[t][ix(6,0,2)],'REF',cut[t][ix(6,1,2)])
print('E PASS five initial clock phases select five different first-write ticks; static ready t1')
