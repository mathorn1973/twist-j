"""NON-CANONICAL #2135 F: refusal clock with fixed second material rail."""
from pathlib import Path
import runpy
from itertools import product
from fractions import Fraction as Q
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
vert=V['vert']
def orbit(n,seed):
    v=[Z]*n;v[0]=O;v[1]=neg(O)
    if seed:
        y,k,m=seed;v[y]=sc(m,P[k])
    ini=tuple(v);v=ini;cuts=[v];words=[[] for y in range(n)]
    for t in range(1,4097):
        bit=(t-1)%2;nxt,mask=vert(v,bit)
        for y in range(n):
            j=(y+1)%n if y%2==bit else (y-1)%n
            words[y].append('R' if not H.even(sub(v[y],v[j])) else 'C' if nxt[y]!=v[y] else '=')
        v=nxt;cuts.append(v)
        if t%2==0 and v==ini:return cuts,words
    return cuts,words
roots=tuple(sc(s,P[k]) for s,k in product((1,-1),range(5)))
stats=Counter();histogram=Counter();best=None;qualified=0
for n in (4,6,8,10,12):
    for seed in [None]+list(product(range(2,n,2),range(5),(1,2))):
        cuts,words=orbit(n,seed);p=len(cuts)-1
        if not (p%2==0 and cuts[-1]==cuts[0] and p>10 and 'R' in words[0] and 'C' in words[0]):continue
        qualified+=1
        for y in range(n):
            values=tuple(dict.fromkeys(v[y] for v in cuts[1:]))
            for dstar,w,tag in product(values,roots,(1,2)):
                v=add(dstar,sc(2,w));f=mul(J if tag==1 else JI,neg(w))
                tags=tuple(H.collision((a[y],v,sc(2,f),Z))[1] for a in cuts)
                assert any(tags)
                for s in range(0,p,2):
                    stats['tried']+=1
                    first=next(t for t in range(1,p+1) if tags[(s+t)%p])
                    if tags[(s+first)%p]!=tag or cuts[(s+first)%p][y]!=dstar:
                        stats['other_ready_or_tag']+=1;continue
                    word=''.join(words[y][(s+i)%p] for i in range(first))
                    if 'R' not in word[:-1] or 'C' not in word:
                        stats['no_prior_refusal_or_change']+=1;continue
                    stats['qualified']+=1;histogram[first]+=1
                    if best is None or first>best[0]:
                        best=(first,n,seed,p,y,dstar,w,tag,s,v,f,cuts[s],word)
assert qualified==75
print('F CENSUS','CLOCKS',qualified,'COUNTS',sorted(stats.items()),'HIST',sorted(histogram.items()),'GT5',sum(v for k,v in histogram.items() if k>5),'GE10',sum(v for k,v in histogram.items() if k>=10),'GE114',sum(v for k,v in histogram.items() if k>=114))
if best is None:
    print('F NO QUALIFIED WRITE');raise SystemExit(0)
t,n,seed,p,y,dstar,w,tag,s,v,f,init,word=best
print('F SELECT','DELAY',t,'HEIGHT',n,'SEED',seed,'PERIOD',p,'ROW',y,'READY',dstar,'W',w,'TAG',tag,'PHASE',s,'REFERENCE',v,'F',f,'INIT',init,'WORD',word)
def account(F):
    return H.ring_sum(z for i,z in enumerate(F) if i%4<2),H.ring_sum(z for i,z in enumerate(F) if i%4>=2),H.ring_sum(h(z) for z in F)
def seedfield(init):
    F=[]
    for x,k in product(range(8),range(n)):
        F.extend((init[k] if x==0 else Z,v if x==0 else Z,sc(2,f) if x==0 else Z,Z if k==y else sc(2,f)))
    return tuple(F)
F0=F=seedfield(init);ac=account(F);i=H.index(n,0,y,0);actual=None;hold=0;mark=None;ref=sc(2,f);hold_active=True
for u in range(1,t+33):
    G=H.transport(F,n,(u-1)%2);N,ev=H.collide(G,n)
    assert H.collide(N,n)[0]==G and H.transport(G,n,(u-1)%2,True)==F and account(G)==account(N)==ac
    if u<t:assert not ev
    if u<=t:
        assert all(G[H.index(n,0,k,0)]==orbit(n,seed)[0][(s+u)%p][k] for k in range(n))
        assert G[i+1:i+4]==(v,ref,Z)
    if u==t:
        assert ev==((0,y,tag),) and G[i]==dstar
        actual=N[i:i+4];mark=actual[2];assert mark!=ref
        print('F WRITE','PRE',G[i:i+4],'POST',actual,'ACCOUNT',ac,'Q',H.scalar_account(ac[2]))
    if u>t and hold_active:
        if G[i+2]==N[i+2]==mark:hold+=1
        else:hold_active=False
    if u<=t or ev:print('F NATIVE',u,'R0',N[i],'R2',N[i+1],'CLK',N[i+2],'TAGS',ev)
    F=N
print('F HOLD','SUBSEQUENT',hold,'OF',32)
# Compare all even starting phases at fixed v/f using the actual local
# pre-write clock and the complete initial account.
cuts,words=orbit(n,seed);phase_results=[]
for s0 in range(0,p,2):
    assert account(seedfield(cuts[s0]))==ac
    hit=next((u,H.collision((cuts[(s0+u)%p][y],v,ref,Z))[1],cuts[(s0+u)%p][y]) for u in range(1,p+1) if H.collision((cuts[(s0+u)%p][y],v,ref,Z))[1])
    phase_results.append((s0,*hit))
assert len({u for s0,u,t0,d in phase_results})>1
print('F PHASES',phase_results)
# Counterfactual all-admitted rational C, not a native trajectory.
def lin(a,b):
    s=sc(Q(1,2),add(a,b));d=sc(Q(1,2),mul(R,sub(a,b)))
    return add(s,d),sub(s,d)
r0=init;first=None
for u in range(1,t+1):
    out=list(r0);bit=(u-1)%2
    for k in range(bit,n,2):
        j=(k+1)%n;out[k],out[j]=lin(r0[k],r0[j])
    r0=tuple(out);d=sc(Q(1,2),sub(r0[y],v))
    tag0=1 if d!=Z and h(f)==mul(H.T,h(d)) else 2 if f!=Z and h(d)==mul(H.T,h(f)) else 0
    if first is None and tag0:first=(u,tag0)
print('F FORCED_LINEAR','FIRST_BALANCE',first,'TARGET_R0',r0[y],'SAME_READY',int(r0[y]==dstar))
print('PASS actual reference-gated refusal-clock write')
