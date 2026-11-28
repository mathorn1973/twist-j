"""NON-CANONICAL #2135 A/B. Native refusal clock census."""
from pathlib import Path
import sys,hashlib,importlib.util
from itertools import product
from collections import Counter
from functools import lru_cache,cache
from fractions import Fraction as Q
source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()=='4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H;spec.loader.exec_module(H)
Z,O,R,J,JI,P=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV,H.J_POWERS
add,sub,mul,sc,h=H.add,H.sub,H.mul,H.scale,H.h
neg=lambda x:sc(-1,x)
L=sub(O,R);BI=H.inverse(sc(Q(1,2),L))
def scale(z):return mul(L,z)
D=scale((12,0,6,6));D2=scale((0,6,0,0))
r=scale((-2,-2,9,-5));c=scale((7,-8,12,-2))
def need(r,D,t):
    f=mul(D,H.inverse(sub(O,JI if t==1 else J)))
    z=add(r,sc(2,f));assert all(Q(v).denominator==1 for v in z);return tuple(map(int,z))
G1=tuple(need(r,D,t) for t in (1,2));G2=tuple(need(c,D2,t) for t in (1,2))
def q(z):return H.scalar_account(h(z))
# Independent inverse checks on every distinct pair used in the census.
@lru_cache(maxsize=300000)
def contact(a,b):
    refused=not H.even(sub(a,b));u,v=H.transport_pair(a,b,False)
    assert H.transport_pair(u,v,True)==(a,b)
    assert add(a,b)==add(u,v) and add(h(a),h(b))==add(h(u),h(v))
    return u,v,refused
def vert(v,bit):
    n=len(v);out=list(v);mask=0
    for i,y in enumerate(range(bit,n,2)):
        k=(y+1)%n;out[y],out[k],ref=contact(v[y],v[k]);mask|=int(ref)<<i
    return tuple(out),mask
def subeven(v,D):return tuple(sub(z,D) if y%2==0 else z for y,z in enumerate(v))
def mean(v,bit):return sc(Q(2,len(v)),H.ring_sum(v[bit::2]))
def ready(v,gs):return sum(z in gs for z in v[::2])
pairs=tuple(product(range(2),repeat=2))
OD=[]
for a,b in pairs:
    x=sub(G1[a],D);y=G2[b]
    assert x!=y
    odd=add(x,mul(BI,sub(y,x)))
    assert all(Q(v).denominator==1 for v in odd)
    odd=tuple(map(int,odd))
    assert H.even(sub(x,odd)) and H.transport_pair(x,odd,False)[0]==y
    assert H.even(sub(G1[a],odd))
    OD.append(odd)
    print('A PARTNER',a+1,b+1,'READY113',G1[a],'ODD',odd,'POST_B113',x,'READY114',y,'REFUSAL_IMPOSSIBLE',1)
def start(word):
    n=2*len(word);v=[Z]*n
    for i,k in enumerate(word):v[2*i]=G1[pairs[k][0]];v[(2*i-1)%n]=OD[k]
    return tuple(v)
# Cache each complete orbit segment, with actual refusal masks. No quotient
# of the enumeration is made. Repeated state+matching bit may be replayed.
@lru_cache(maxsize=40000)
def trace(v,first_bit,length):
    masks=[];seen={};states=[];t=0
    while t<length:
        key=(v,(first_bit+t)%2)
        if key in seen:
            s=seen[key];period=t-s
            # State at index j is the state before layer j+1.
            left=length-t;cycles,rem=divmod(left,period)
            masks.extend(masks[s:t]*cycles+masks[s:s+rem])
            v=states[s+rem][0]
            break
        seen[key]=t;states.append(key)
        v,mask=vert(v,(first_bit+t)%2);masks.append(mask);t+=1
    assert len(masks)==length
    return v,tuple(masks)
def evaluate(word):
    v=start(word);n=len(v)
    # Negative-first free evolution and positive-first two literal CLK debits.
    vn,mn=trace(v,1,114)
    vp0,mask=vert(subeven(v,D),1)
    assert mask==0 and tuple(vp0[::2])==tuple(G2[pairs[k][1]] for k in word)
    vp,mp=trace(subeven(vp0,D2),0,113);mp=(mask,)+mp
    return v,vn,vp,mn,mp
def A():
    for n in (2,4,6,8,10,12,14):
        k=n//2;counts=Counter();hist=Counter();refh=Counter();early=[set() for _ in range(10)];earlyp=[set() for _ in range(10)]
        first_ref=None;first_nontrivial=None;full=[];max_ready=(0,0);maxr=None
        for word in product(range(4),repeat=k):
            v,vn,vp,mn,mp=evaluate(word)
            rn,rp=ready(vn,G1),ready(vp,G1);hist[rn,rp]+=1
            if rn==k:counts['negative_full']+=1
            if rp==k:counts['positive_full']+=1
            if rn==rp==k:
                counts['joint227']+=1
                nn,m0=vert(subeven(vn,D),1);pp,m1=vert(subeven(vp,D),1)
                ok=ready(nn,G2)==ready(pp,G2)==k
                counts['joint228']+=ok
                full.append((word,vn,vp,nn,pp,m0,m1,int(ok)))
            if (rn or rp) and first_nontrivial is None:first_nontrivial=(word,rn,rp,vn,vp)
            if first_ref is None or min((i for i,m in enumerate(mn) if m),default=114)<first_ref[0]:
                first_ref=(min((i for i,m in enumerate(mn) if m),default=114),word,mn[:10],mp[:10])
            score=rn+rp
            if maxr is None or score>maxr[0]:maxr=(score,word,rn,rp)
            max_ready=max(max_ready[0],rn),max(max_ready[1],rp)
            refh[(sum(m.bit_count() for m in mn),sum(m.bit_count() for m in mp))]+=1
            for i in range(10):early[i].add(mn[i]);earlyp[i].add(mp[i])
            counts['tried']+=1
        assert counts['tried']==4**k
        print('A CENSUS',n,sorted(counts.items()),'READY_HIST',sorted(hist.items()),'MAX',max_ready,'BEST',maxr,flush=True)
        print('A REFUSAL',n,'DISTINCT_COUNT_PAIRS',len(refh),'MINMAX_N',min(a for a,b in refh),max(a for a,b in refh),'MINMAX_P',min(b for a,b in refh),max(b for a,b in refh),'FIRST',first_ref)
        print('A EARLY_MASK_COUNTS',n,tuple(map(len,early)),tuple(map(len,earlyp)),'ALL_UNIFORM_N',tuple(all(m in (0,(1<<k)-1) for m in mm) for mm in early),'ALL_UNIFORM_P',tuple(all(m in (0,(1<<k)-1) for m in mm) for mm in earlyp))
        print('A FIRST_READY',n,first_nontrivial)
        for rec in full:print('A JOINT_PATTERN',n,rec)
        # Exact selected literal trace and inverse/sector account at each step.
        v,vn,vp,mn,mp=evaluate(maxr[1]);cur=v
        for i in range(114):
            nxt,mask=vert(cur,(1+i)%2);assert mask==mn[i]
            assert H.ring_sum(cur)==H.ring_sum(nxt) and H.ring_sum(h(z) for z in cur)==H.ring_sum(h(z) for z in nxt)
            cur=nxt
        assert cur==vn
        trace.cache_clear()
        print('A DONE_HEIGHT',n,flush=True)
def B():
    best=None;passes=[];counts=Counter()
    for n in (4,6,8,10,12):
        seeds=[None]+list(product(range(2,n,2),range(5),(1,2)));local=Counter()
        for seed in seeds:
            v=[Z]*n;v[0]=O;v[1]=neg(O)
            if seed:
                y,k,m=seed;v[y]=sc(m,P[k])
            ini=v=tuple(v);word=[];first=None;period=None
            for t in range(1,4097):
                bit=(t-1)%2;neighbor=1 if bit==0 else n-1
                a,b=v[0],v[neighbor]
                v,mask=vert(v,bit)
                ref=not H.even(sub(a,b))
                event='R' if ref else 'C' if v[0]!=a else '='
                word.append(event)
                if first is None and event=='C' and v[0]==O:first=t
                if t%2==0 and v==ini:period=t;break
            mixed='R' in word and 'C' in word
            local['tried']+=1;local['mixed']+=mixed;local['returned']+=period is not None
            if mixed and period and period>10:
                local['period_gt10']+=1
                if best is None or period>best[0]:best=(period,n,seed,ini,''.join(word),first)
                if first==114:passes.append((n,seed,period));local['first114']+=1
            print('B CASE',n,seed,'PERIOD',period,'MIXED',int(mixed),'FIRST_READY',first,'EVENTS',dict(sorted(Counter(word).items())))
        counts.update(local);print('B CENSUS',n,sorted(local.items()),flush=True)
    print('B TOTAL',sorted(counts.items()),'FIRST114',passes)
    if best is None:print('B NO QUALIFIED CLOCK');return
    period,n,seed,ini,word,first=best
    print('B SELECT','PERIOD',period,'HEIGHT',n,'SEED',seed,'INITIAL',ini,'FIRST_READY',first,'EVENT_WORD',word)
    F=[]
    for x,y in product(range(8),range(n)):
        z=ini[y] if x==0 else Z;F.extend((z,neg(z),Z,Z))
    F0=F=tuple(F);total=H.ring_sum(h(z) for z in F)
    assert H.ring_sum(F)==Z
    for t in range(1,period+1):
        bit=(t-1)%2;G=H.transport(F,n,bit);V,ev=H.collide(G,n)
        assert not ev and G==V and H.transport(G,n,bit,True)==F
        assert H.ring_sum(V)==Z and H.ring_sum(h(z) for z in V)==total
        a=F[H.index(n,0,0,0)];b=F[H.index(n,0,1 if bit==0 else n-1,0)];z=V[H.index(n,0,0,0)]
        assert word[t-1]==('R' if not H.even(sub(a,b)) else 'C' if z!=a else '=')
        assert (V==F0 and t%2==0)==(t==period)
        F=V
    print('B FULL_REPLAY',period,'Q',H.scalar_account(total),'H',total,'PASS')
if __name__=='__main__':
    A();B()
    print('DONE exact native refusal clocks')
