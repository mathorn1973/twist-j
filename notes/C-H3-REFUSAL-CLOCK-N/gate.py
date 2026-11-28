"""NON-CANONICAL #2135 D: actual B timed by a refusal clock."""
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
    ini=tuple(v);v=ini;cuts=[v];word=[]
    for t in range(1,4097):
        bit=(t-1)%2;j=1 if bit==0 else n-1;a,b=v[0],v[j]
        v,m=vert(v,bit)
        word.append('R' if not H.even(sub(a,b)) else 'C' if v[0]!=a else '=')
        cuts.append(v)
        if t%2==0 and v==ini:return cuts,word
    return cuts,word
def first_write(orbit,s,f):
    p=len(orbit)-1
    for t in range(1,p+1):
        d=orbit[(s+t)%p][0]
        cell=(d,neg(d),sc(2,f),Z);_,tag=H.collision(cell)
        if tag:return t,tag
    return None
stats=Counter();histogram=Counter();best=None;qualified=0
for n in (4,6,8,10,12):
    for seed in [None]+list(product(range(2,n,2),range(5),(1,2))):
        cuts,word=orbit(n,seed);p=len(word)
        if not (p%2==0 and cuts[-1]==cuts[0] and p>10 and 'R' in word and 'C' in word):continue
        qualified+=1
        for s in range(0,p,2):
            seen=set()
            for t,tag in product(range(1,p+1),(1,2)):
                d=cuts[(s+t)%p][0]
                if d==Z:continue
                f=mul(J if tag==1 else JI,d)
                key=f,tag
                if key in seen:continue
                seen.add(key);stats['tested']+=1
                first=first_write(cuts,s,f)
                assert first is not None
                if first!=(t,tag):stats['earlier_or_other_tag']+=1;continue
                w=''.join(word[(s+i)%p] for i in range(t))
                if 'R' not in w[:-1] or 'C' not in w:stats['no_refusal_before']+=1;continue
                stats['qualified']+=1;histogram[t]+=1
                if best is None or t>best[0]:best=(t,n,seed,p,s,tag,f,cuts[s],d,w)
assert qualified==75
print('D CENSUS','CLOCKS',qualified,'COUNTS',sorted(stats.items()),'HIST',sorted(histogram.items()),'GT5',sum(v for k,v in histogram.items() if k>5),'GE10',sum(v for k,v in histogram.items() if k>=10),'GE114',sum(v for k,v in histogram.items() if k>=114))
if best is None:
    print('D NO QUALIFIED WRITE');raise SystemExit(0)
t,n,seed,p,s,tag,f,init,dstar,w=best
print('D SELECT','DELAY',t,'HEIGHT',n,'SEED',seed,'PERIOD',p,'PHASE',s,'TAG',tag,'F',f,'INIT',init,'READY',dstar,'WORD',w)
def account(F):
    return H.ring_sum(z for i,z in enumerate(F) if i%4<2),H.ring_sum(z for i,z in enumerate(F) if i%4>=2),H.ring_sum(h(z) for z in F)
F=[]
for x,y in product(range(8),range(n)):
    d=init[y] if x==0 else Z
    F.extend((d,neg(d),sc(2,f) if x==0 else Z,Z if y==0 else sc(2,f)))
F0=F=tuple(F);ac=account(F);actual=None;hold=0;mark=None;ref=sc(2,f);hold_active=True
for u in range(1,t+33):
    G=H.transport(F,n,(u-1)%2);N,ev=H.collide(G,n)
    assert H.collide(N,n)[0]==G and H.transport(G,n,(u-1)%2,True)==F and account(G)==account(N)==ac
    if u<t:assert not ev
    if u==t:
        assert ev==((0,0,tag),) and G[0]==dstar and G[2:4]==(ref,Z)
        actual=N[:4];mark=N[2];assert mark!=ref
        print('D WRITE','PRE',G[:4],'POST',actual,'ACCOUNT',ac,'Q',H.scalar_account(ac[2]))
    if u>t and hold_active:
        if G[2]==N[2]==mark:hold+=1
        else:hold_active=False
    if u<=t or ev:print('D NATIVE',u,'D',N[0],'CLK',N[2],'TAGS',ev)
    F=N
print('D HOLD','SUBSEQUENT',hold,'OF',32)
# Counterfactual all-admitted rational C, never a native field.
def lin(a,b):
    s=sc(Q(1,2),add(a,b));d=sc(Q(1,2),mul(R,sub(a,b)))
    return add(s,d),sub(s,d)
v=init;first=None
for u in range(1,t+1):
    out=list(v);bit=(u-1)%2
    for y in range(bit,n,2):
        j=(y+1)%n;out[y],out[j]=lin(v[y],v[j])
    v=tuple(out);d=v[0]
    tag0=1 if d!=Z and h(f)==mul(H.T,h(d)) else 2 if f!=Z and h(d)==mul(H.T,h(f)) else 0
    if first is None and tag0:first=(u,tag0)
print('D FORCED_LINEAR','FIRST_BALANCE',first,'TARGET_D',v[0],'SAME_READY',int(v[0]==dstar))
print('PASS actual refusal-timed native B')
