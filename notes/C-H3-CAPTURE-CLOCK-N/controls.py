"""NON-CANONICAL D: clock phase controls, preregistered #2119 comment 7221902605."""
from pathlib import Path
import runpy
from collections import Counter
root=Path(__file__).resolve().parent
V=runpy.run_path(str(root/'verify.py'))
H=V['H'];P,O,JI=V['P'],V['O'],V['JI']
st=V['stock'](-3,0,0)
assert st is not None
initial,ready=V['make_clock'](O,O,6)
g=(6,-2,12,1);mark=(5,-3,11,1)
port,ref=V['port'],V['ref']
src,reader,setup,seed,hist,word=V['sourcepart'],V['reader'],V['setup'],V['seed'],V['hist'],V['word']
N=(0,2,3,4)
base_ac=None
for q in range(6):
    label=str(q) if q<5 else 'static'
    d=V['Cpow'](initial,q) if q<5 else (JI,JI)
    hh=[hist(setup(seed(p,st),d,g),160,True) for p in P]
    ac=hh[0][3]
    assert all(w[3]==ac for w in hh)
    if q==0:base_ac=ac
    if q<5:assert ac==base_ac
    print('D CONTROL',label,'D_INIT',d,'ACCOUNT',ac,'Q',H.scalar_account(ac[2]))
    for k,w in enumerate(hh):
        cuts,mids,tags,_=w
        hit=next(((t,y,tags[t][12+y],cuts[t][port],cuts[t][ref]) for t in range(1,161) for y in range(2) if tags[t][12+y]),None)
        print('D FIRST',label,k,hit)
    def correct(F,k):return F[port]==(mark if k==1 else g) and F[ref]==g
    active=all(correct(w[0][6],k) for k,w in enumerate(hh))
    print('D TARGET6',label,int(active))
    loss=None if active else (6,0)
    returns=[];held=[]
    firstsplit=None
    for t in range(1,161):
        if firstsplit is None and len({word(hh[k],t) for k in N})!=1:firstsplit=t
        if t>6 and active:
            for stage in (1,0):
                if not all(correct(w[stage][t],k) for k,w in enumerate(hh)):
                    active=False;loss=(t,stage);break
        if t%2==0 and all(src(w[0][t])==src(w[0][0]) for w in hh):
            returns.append(t)
            if t>=6 and active and len({word(w,t) for w in hh})==2 and len({word(hh[k],t) for k in N})==1:
                held.append(t)
    print('D ENDPOINTS',label,'SOURCE_RETURNS',returns,'HELD_RETURNS',held,'FIRST_HOLD_LOSS',loss,'FIRST_NEGATIVE_SPLIT',firstsplit)
    for t in (6,16,30,100,110,111,160):
        print('D PARTITION',label,t,sorted(Counter(word(w,t) for w in hh).values()),'PORTS',tuple(w[0][t][port] for w in hh),'REFS',tuple(w[0][t][ref] for w in hh))
    if q==0:assert held==[16,30,44,58,72,86,100] and loss==(111,0)
print('DONE exact clock phase controls')
