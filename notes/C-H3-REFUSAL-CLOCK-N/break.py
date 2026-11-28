"""NON-CANONICAL #2135 result-exposed alternate five-cycle arithmetic."""
from fractions import Fraction as Q
from itertools import product,combinations
from functools import lru_cache,cache
from collections import Counter

def red(a):
    a=tuple(a);return tuple(x-a[4] for x in a[:4])
def j(k):return red(int(i==k%5) for i in range(5))
P=tuple(j(k) for k in range(5));O=P[0];Z=(0,0,0,0);R=P[2]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sc(k,a):return tuple(k*x for x in a)
def sub(a,b):return add(a,sc(-1,b))
def neg(a):return sc(-1,a)
def rs(xs):
    a=Z
    for z in xs:a=add(a,z)
    return a
@cache
def mul(a,b):
    v=[0]*5
    for i,x in enumerate(a):
        for k,y in enumerate(b):v[(i+k)%5]+=x*y
    return red(v)
@cache
def h(a):return mul(a,rs(sc(v,P[-k%5]) for k,v in enumerate(a)))
def q(a):return 2*h(a)[0]-h(a)[2]
def even(a):return not any(v%2 for v in a)
J=add(O,R);JI=neg(add(P[1],P[2]));L=sub(O,R);T=h(J);T2=mul(T,T)
alpha=sc(Q(1,2),J);beta=sc(Q(1,2),L)
BI=sc(Q(2,5),rs((sc(4,O),sc(3,R),sc(2,P[4]),P[1])))
assert mul(beta,BI)==O and mul(J,JI)==O
def scale(a):return mul(L,a)
def ints(a):
    assert all(Q(v).denominator==1 for v in a)
    return tuple(map(int,a))
@lru_cache(maxsize=300000)
def C(a,b,inv=False):
    dif=sub(a,b)
    if not even(dif):return a,b,1
    u=mul(P[3] if inv else R,dif)
    z,w=add(add(a,b),u),sub(add(a,b),u)
    assert even(z) and even(w)
    return tuple(x//2 for x in z),tuple(x//2 for x in w),0
@cache
def B(cell):
    a,b,u,v=cell
    if not even(sub(a,b)) or not even(sub(u,v)):return cell,0
    d,f=tuple(x//2 for x in sub(a,b)),tuple(x//2 for x in sub(u,v))
    m,c=tuple(x//2 for x in add(a,b)),tuple(x//2 for x in add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):D,F,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):D,F,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(m,D),sub(m,D),add(c,F),sub(c,F)),k
def vert(v,bit,inv=False):
    n=len(v);out=list(v);mask=0
    for i,y in enumerate(range(bit,n,2)):
        z=(y+1)%n;out[y],out[z],r=C(v[y],v[z],inv);mask|=r<<i
    return tuple(out),mask
def transport(F,n,bit,inv=False):
    out=[list(c) for c in F]
    for x in range(8):
        for rail in range(3):
            v=vert(tuple(F[n*x+y][rail] for y in range(n)),bit,inv)[0]
            for y,z in enumerate(v):out[n*x+y][rail]=z
    for y in range(n):
        v=vert(tuple(F[n*x+y][3] for x in range(8)),bit,inv)[0]
        for x,z in enumerate(v):out[n*x+y][3]=z
    return tuple(tuple(c) for c in out)
def acct(F):
    return rs(z for c in F for z in c[:2]),rs(z for c in F for z in c[2:]),rs(h(z) for c in F for z in c)
def scalar(H):return 2*H[0]-H[2]
def step(F,n,bit,ac):
    G=transport(F,n,bit);r=tuple(B(c) for c in G)
    N=tuple(z[0] for z in r);ev=tuple((x,y,r[n*x+y][1]) for x,y in product(range(8),range(n)) if r[n*x+y][1])
    assert tuple(B(c)[0] for c in N)==G and transport(G,n,bit,True)==F and acct(G)==acct(N)==ac
    return G,N,ev
# A: direct native exact enumeration of all row tag vectors.
D=scale((12,0,6,6));D2=scale((0,6,0,0))
r=scale((-2,-2,9,-5));c=scale((7,-8,12,-2))
def need(r,D,k):
    f=mul(D,mul(J,P[3]) if k==1 else neg(P[3]))
    assert mul(sub(O,JI if k==1 else J),f)==D
    return add(r,sc(2,f))
G1=tuple(need(r,D,k) for k in (1,2));G2=tuple(need(c,D2,k) for k in (1,2))
pairs=tuple(product(range(2),repeat=2))
OD=[]
for a,b in pairs:
    x=sub(G1[a],D);y=G2[b]
    assert x!=y
    odd=ints(add(x,mul(BI,sub(y,x))))
    assert C(x,odd)[0]==y and C(x,odd)[2]==0 and C(G1[a],odd)[2]==0
    OD.append(odd)
def seedA(w):
    n=2*len(w);v=[Z]*n
    for i,k in enumerate(w):v[2*i]=G1[pairs[k][0]];v[(2*i-1)%n]=OD[k]
    return tuple(v)
def debit(v,d):return tuple(sub(z,d) if i%2==0 else z for i,z in enumerate(v))
def walk(v,bit,num):
    seen={};masks=[];t=0
    while t<num:
        key=(v,(bit+t)%2)
        if key in seen:
            period=t-seen[key];cnt=(num-t)//period
            if cnt:
                a=seen[key];masks.extend(masks[a:t]*cnt);t+=period*cnt
                if t==num:break
        else:seen[key]=t
        v,mask=vert(v,(bit+t)%2);masks.append(mask);t+=1
    return v,tuple(masks)
want={2:{(0,0):4},4:{(0,0):16},6:{(0,0):64},8:{(0,0):224,(1,0):32},
      10:{(0,0):899,(1,0):125},12:{(0,0):3736,(0,1):12,(1,0):348},
      14:{(0,0):12443,(0,1):7,(1,0):2765,(2,0):889,(3,0):280}}
for n in (2,4,6,8,10,12,14):
    hist=Counter();rmin=[10**9,10**9];rmax=[0,0]
    for w in product(range(4),repeat=n//2):
        v=seedA(w);neg0,mn=walk(v,1,114)
        p0,m0=vert(debit(v,D),1);assert m0==0
        assert p0[::2]==tuple(G2[pairs[k][1]] for k in w)
        pos0,mp=walk(debit(p0,D2),0,113)
        hist[sum(z in G1 for z in neg0[::2]),sum(z in G1 for z in pos0[::2])]+=1
        for i,mask in enumerate((mn,mp)):
            k=sum(m.bit_count() for m in mask)
            rmin[i]=min(rmin[i],k);rmax[i]=max(rmax[i],k)
    assert hist==want[n]
    print('ALT A',n,sorted(hist.items()),'MIN',rmin,'MAX',rmax,flush=True)
# B: independently check the full periods and event words.
def familyB(n):
    for seed in [None]+list(product(range(2,n,2),range(5),(1,2))):
        v=[Z]*n;v[0]=O;v[1]=neg(O)
        if seed:
            y,k,m=seed;v[y]=sc(m,P[k])
        yield seed,tuple(v)
def trace(v,lim,stop=False):
    n=len(v);I=v;cut=[v];words=[[] for _ in v]
    for t in range(1,lim+1):
        bit=(t-1)%2;nxt,mask=vert(v,bit)
        for y in range(n):
            z=(y+1)%n if y%2==bit else (y-1)%n
            words[y].append('R' if not even(sub(v[y],v[z])) else 'C' if nxt[y]!=v[y] else '=')
        v=nxt;cut.append(v)
        if stop and t%2==0 and v==I:break
    return cut,words
clocks=[];best=None;ct=Counter()
for n in (4,6,8,10,12):
    loc=Counter()
    for seed,v in familyB(n):
        cut,word=trace(v,4096,True);p=len(cut)-1
        assert p%2==0 and cut[-1]==v and 'R' in word[0] and 'C' in word[0]
        loc['tried']+=1
        if p>10:
            loc['qualified']+=1;clocks.append((n,seed,cut,word))
            if best is None or p>best[0]:best=(p,n,seed,v)
            first=next((i+1 for i,c in enumerate(word[0]) if c=='C' and cut[i+1][0]==O),None)
            assert first!=114
    ct.update(loc);print('ALT B',n,sorted(loc.items()))
assert best==(90,6,(4,0,2),(O,neg(O),Z,Z,sc(2,O),Z))
assert ct=={'tried':155,'qualified':75}
p,n,seed,v=best
I=tuple((v[y],neg(v[y]),Z,Z) if x==0 else (Z,Z,Z,Z) for x,y in product(range(8),range(n)));F=I;ac=acct(I)
for t in range(1,p+1):
    _,F,ev=step(F,n,(t-1)%2,ac);assert not ev
    assert (F==I and t%2==0)==(t==p)
assert scalar(ac[2])==24
print('ALT B BEST',best,'Q',24)
# D: earliest hits computed from complete per-reference bitmaps.
st=Counter()
for n,seed,cut,words in clocks:
    p=len(cut)-1
    hits={}
    for s in range(0,p,2):
        seen=set()
        for t,k in product(range(1,p+1),(1,2)):
            d=cut[(s+t)%p][0]
            if d==Z:continue
            f=mul(J if k==1 else JI,d)
            if (f,k) in seen:continue
            seen.add((f,k));st['tested']+=1
            if f not in hits:hits[f]=tuple(B((v[0],neg(v[0]),sc(2,f),Z))[1] for v in cut[:-1])
            tag=hits[f];a=next(i for i in range(1,p+1) if tag[(s+i)%p])
            if (a,tag[(s+a)%p])!=(t,k):st['earlier_or_other_tag']+=1;continue
            w=''.join(words[0][(s+i)%p] for i in range(t))
            assert 'R' not in w[:-1] or 'C' not in w
            st['no_refusal_before']+=1
assert st=={'tested':24750,'earlier_or_other_tag':19800,'no_refusal_before':4950}
print('ALT D',sorted(st.items()))
# F: use the actual single-row clock and its fixed second material rail.
roots=tuple(sc(s,P[k]) for s,k in product((1,-1),range(5)))
ct=Counter();hs=Counter();best=None
for n,seed,cut,words in clocks:
    p=len(cut)-1
    for y in range(n):
        vals=tuple(dict.fromkeys(v[y] for v in cut[1:]))
        for d,w,k in product(vals,roots,(1,2)):
            ref=add(d,sc(2,w));f=mul(J if k==1 else JI,neg(w))
            hits=[(i,B((v[y],ref,sc(2,f),Z))[1]) for i,v in enumerate(cut[:-1])]
            hits=[(i,t) for i,t in hits if t]
            for s in range(0,p,2):
                ct['tried']+=1
                t,tag=min((((i-s)%p or p),t) for i,t in hits)
                if tag!=k or cut[(s+t)%p][y]!=d:ct['other_ready_or_tag']+=1;continue
                ww=''.join(words[y][(s+i)%p] for i in range(t))
                if 'R' not in ww[:-1] or 'C' not in ww:ct['no_prior_refusal_or_change']+=1;continue
                ct['qualified']+=1;hs[t]+=1
                if best is None or t>best[0]:best=(t,n,seed,p,y,d,w,k,s,ref,f,cut[s])
assert ct=={'tried':1440000,'qualified':943500,'no_prior_refusal_or_change':496500}
assert best[:9]==(17,4,(2,0,1),18,0,R,O,1,2)
print('ALT F',sorted(ct.items()),'HIST',sorted(hs.items()),'BEST',best[:9])
def replay(n,y,u,v,f,t):
    g=sc(2,f)
    I=tuple((u[k] if x==0 else Z,v[k] if x==0 else Z,g if x==0 else Z,Z if k==y else g) for x,k in product(range(8),range(n)))
    ac=acct(I);F=I;mark=None;hold=0;active=True
    for a in range(1,t+33):
        G,F,ev=step(F,n,(a-1)%2,ac)
        if a<t:assert not ev
        if a<=t:assert all(c[2:]==i[2:] for c,i in zip(G,I))
        if a==t:
            assert ev==((0,y,1),)
            print('ALT WRITE',t,G[y],F[y],'Q',scalar(ac[2]))
            mark=F[y][2];assert mark!=g
        if a>t and active:
            if G[y][2]==F[y][2]==mark:hold+=1
            else:active=False
    assert hold==0
    return scalar(ac[2])
t,n,seed,p,y,d,w,k,s,ref,f,u=best
assert replay(n,y,u,(ref,)*n,f,t)==374
# G/H: generate all new wheels once and use explicit equality time sets.
def familyG(n):
    for (y,z),(a,b) in product(combinations(range(2,n,2),2),product((-3,-2,-1,1,2,3),repeat=2)):
        v=[Z]*n;v[0]=O;v[1]=neg(O);v[y]=sc(a,O);v[z]=sc(b,O)
        yield ('G',y,z,a,b),tuple(v)
targets=(114,90,89)
chosen={};tot={t:Counter() for t in targets};g_count=0;g_vectors=0
for n in (6,8,10,12,14):
    masks={(t,y):{} for t,y in product(targets,range(n))};cnt=Counter()
    for name,I in list(familyG(n))+([(('B',s),v) for s,v in familyB(n)] if n<14 else []):
        cut,words=trace(I,146)
        if name[0]=='G':g_vectors+=1
        for y in range(n):
            byval={}
            for i,v in enumerate(cut):byval.setdefault(v[y],[]).append(i)
            for s in range(0,33,2):
                if name[0]=='G':
                    assert any(s<i<s+114 for i in byval[cut[s+114][y]])
                    g_count+=1
                for t in targets:
                    if 'R' not in words[y][s:s+t-1] or 'C' not in words[y][s:s+t]:continue
                    a=frozenset(i-s for i in byval[cut[s+t][y]] if s<i<s+t)
                    masks[t,y].setdefault(a,(name,I,s));cnt[t]+=1
    for t in targets:
        tot[t]['wheels']+=cnt[t]
        for y in range(n):
            d=masks[t,y];tot[t]['masks']+=len(d)
            for i,a in enumerate(d):
                for b in list(d)[i:]:
                    if not a.isdisjoint(b):continue
                    tot[t]['disjoint_pairs']+=1
                    if t not in chosen:chosen[t]=(n,y,a,b,d[a],d[b])
assert (g_vectors,g_count)==(1260,257040)
print('ALT G',g_vectors,g_count,'ALL_REPEATED')
assert {t:tuple(tot[t][k] for k in ('wheels','masks','disjoint_pairs')) for t in targets}=={114:(94656,1700,903),90:(94656,1540,1409),89:(94656,1540,850)}
for t in targets:
    n,y,a,b,(nu,Iu,su),(nv,Iv,sv)=chosen[t]
    assert not a&b
    u,wu=trace(Iu,146);v,wv=trace(Iv,146)
    U=tuple(z[y] for z in u[su:su+t+1]);V=tuple(z[y] for z in v[sv:sv+t+1])
    assert a==frozenset(i for i in range(1,t) if U[i]==U[t])
    assert b==frozenset(i for i in range(1,t) if V[i]==V[t])
    assert q(mul(J,J))!=q(O)
    def bal(d,w):return h(d) in (h(w),mul(T2,h(w)))
    for N in range(1,4*(t-1)+2):
        w=sc(N,O)
        if all(not bal(sub(sc(Q(1,2),sub(U[i],U[t])),w),w) for i in b):break
    else:raise AssertionError
    for M in range(1,2*(4*(t-1)+1),2):
        if all(not bal(sub(sc(Q(1,2),sub(sub(U[i],U[t]),sc(M,sub(V[i],V[t])))),w),w) for i in range(1,t) if i not in b):break
    else:raise AssertionError
    c=add(sub(U[t],sc(M,V[t])),sc(2,w));f=neg(mul(J,w))
    assert all(not bal(sc(Q(1,2),sub(U[i],add(sc(M,V[i]),c))),w) for i in range(1,t))
    print('ALT H',t,sorted(tot[t].items()),'SEEDS',nu,su,nv,sv,'ROW',y,'PRIOR',sorted(a),sorted(b),'N M',N,M,'SHIFT',c)
    assert replay(n,y,u[su],tuple(add(sc(M,z),c) for z in v[sv]),f,t)=={114:1414,90:1504,89:2690}[t]
print('PASS alternate independent ring, all A/B/D/F/G/H principal results and selected writes')
