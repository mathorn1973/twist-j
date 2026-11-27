"""NON-CANONICAL result-exposed alternate #2115 audit.
Independent five-power arithmetic, local maps and inverse synthesis.
Does not import the pinned H3 source or either primary audit.
Usage: python3 break.py ABC or D.
"""
from functools import cache
from itertools import product
from fractions import Fraction as Q
from collections import Counter
import sys

def reduce(v):
    v=tuple(v);return tuple(x-v[4] for x in v[:4])+(0,)
def p(n):return reduce(int(k==n%5) for k in range(5))
def add(a,b):return reduce(x+y for x,y in zip(a,b))
def sc(k,a):return reduce(k*x for x in a)
def sub(a,b):return add(a,sc(-1,b))
@cache
def mul(a,b):return reduce(sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5))
def conj(a):return reduce(a[(4*k)%5] for k in range(5))
@cache
def h(a):return mul(a,conj(a))
Z=sc(0,p(0));O=p(0);R=p(2);RI=p(3);J=add(O,R);JI=sc(-1,add(p(1),p(2)))
T=h(J);P=tuple(p(k) for k in range(5))
def neg(z):return sc(-1,z)
def even(z):return all(x%2==0 for x in z)
def half(z):
    assert even(z);return tuple(x//2 for x in z)
def rs(seq):return tuple(map(sum,zip(*seq)))
def scalar(z):
    t=4*z[0]-sum(z[1:]);assert t%2==0;return t//2
@cache
def C(a,b,back=False):
    d=sub(a,b)
    if not even(d):return a,b
    u=mul(RI if back else R,d)
    return half(add(add(a,b),u)),half(sub(add(a,b),u))
@cache
def B(cell):
    a,b,u,v=cell
    if not even(sub(a,b)) or not even(sub(u,v)):return cell,0
    d,f=half(sub(a,b)),half(sub(u,v));c,g=half(add(a,b)),half(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        D,F,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        D,F,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(c,D),sub(c,D),add(g,F),sub(g,F)),k
def ix(x,y):return x*8+y
def transport(F,bit,back=False):
    G=[list(c) for c in F]
    for x,y in product(range(8),range(bit,8,2)):
        i,k=ix(x,y),ix(x,(y+1)%8)
        for q in range(3):G[i][q],G[k][q]=C(F[i][q],F[k][q],back)
    for x,y in product(range(bit,8,2),range(8)):
        i,k=ix(x,y),ix((x+1)%8,y)
        G[i][3],G[k][3]=C(F[i][3],F[k][3],back)
    return tuple(tuple(c) for c in G)
def acc(F):
    return rs(z for c in F for z in c[:2]),rs(z for c in F for z in c[2:]),rs(h(z) for c in F for z in c)
def step(F,bit,account):
    G=transport(F,bit)
    coll=tuple(B(c) for c in G)
    N=tuple(c for c,t in coll)
    assert acc(G)==acc(N)==account
    rev=tuple(B(c)[0] for c in N)
    assert rev==G and transport(rev,bit,True)==F
    return G,N,tuple(t for c,t in coll)
def hist(F,n):
    ac=acc(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac);cuts.append(F);mids.append(G);tags.append(E)
    return cuts,mids,tags,ac
def val(F,x,y):return F[ix(x,y)]
def raw(z):return z[:4]
def rawcell(c):return tuple(map(raw,c))
def powr(a,n):
    t=O
    for _ in range(n):t=mul(t,a)
    return t
def ref(r,u=None):
    marks={(0,-2*r%8):P[1],(0,(4-2*r)%8):P[2]}
    if u is not None:marks.update({(1,-2*u%8):P[3],(1,(4-2*u)%8):P[4]})
    F=[]
    for x,y in product(range(8),repeat=2):
        d=marks.get((x,y),sc((-1)**y,O));F.append((d,neg(d),Z,sc(2*(-1)**(x+y),J)))
    return tuple(F)
def src(F,mat=False):return tuple(z for c in F[:8] for z in (c[:2] if mat else c))
def reader(F):return F[8:]
def rad(F):return tuple(z for c in F for z in c[2:])
def radword(hh,n):
    cut,mid,tags,ac=hh
    return tuple(rad(F) for t in range(n+1) for F in ((cut[t],) if t==0 else (mid[t],cut[t])))
def tagword(hh,n):return tuple(hh[2][1:n+1])
def reader_words(hh,n):
    cut,mid,_,_=hh
    return tuple(reader(F) for t in range(n+1) for F in ((cut[t],) if t==0 else (mid[t],cut[t])))
def A_gate():
    single={r:hist(ref(r),160) for r in range(4)}
    for name,inputs in (('single',[(r,None) for r in range(4)]),('paired',list(product(range(4),repeat=2)))):
        hs=[single[r] if u is None else hist(ref(r,u),160) for r,u in inputs]
        assert all(hh[0][160]==hh[0][0] and scalar(hh[3][2])==1024 for hh in hs)
        rr=len({radword(hh,160) for hh in hs});tt=len({tagword(hh,160) for hh in hs})
        assert rr==tt==1
        print('A REFERENCE',name,'INPUTS',len(hs),'RAD_CLASSES',rr,'B_CLASSES',tt,'RETURN',len(hs),'Q',1024)
    return single

# Inverse neighbor coefficient from 5=(1-rho)(4+3rho+2rho^2+rho^3).
beta=sc(Q(1,2),sub(O,R))
beta_inv=sc(Q(2,5),rs((sc(4,O),sc(3,R),sc(2,powr(R,2)),powr(R,3))))
assert mul(beta,beta_inv)==O
eta=powr(sub(O,R),4)
def oddden(z):return all(Q(t).denominator%2 for t in z)
def evloc(z):
    assert oddden(z)
    return all(Q(t).numerator%2==0 for t in z)
def rationalC(a,b,back=False):
    dif=sub(a,b)
    if not evloc(dif):return a,b
    u=mul(RI if back else R,dif)
    v=(sc(Q(1,2),add(add(a,b),u)),sc(Q(1,2),sub(add(a,b),u)))
    assert all(oddden(z) for z in v)
    return v
def partner(a,w):
    b=add(a,mul(beta_inv,sub(w,a)))
    assert evloc(sub(a,b)) and rationalC(a,b)[0]==w
    return b
def ints(z):
    assert all(Q(v).denominator==1 for v in z)
    return tuple(map(int,z))
def scale_eta(z):return ints(mul(eta,z))
assert not even(eta)
f={1:tuple(sc(-(-1)**y,mul(J,R)) for y in range(8)),
   2:tuple(powr(J,2) if y==0 else sc(-(-1)**y,O) for y in range(8)),
   3:tuple(powr(J,3) if y==0 else Z for y in range(8)),
   4:tuple(powr(J,2) if y==0 else Z for y in range(8))}
g={1:tuple(sc((-1)**y,powr(R,2)) for y in range(8))}
c={1:tuple(sc((-1)**y,mul(add(J,O),R)) for y in range(8))}
pre={}
for t in range(2,5):
    gg=list(g[t-1])
    for y in range((t-1)%2,8,2):
        k=(y+1)%8;gg[y],gg[k]=C(gg[y],gg[k])
    pre[t]=tuple(sub(gg[y],sc(2,f[t][y])) for y in range(8))
    if t<4:
        # The independent ring uses explicit reciprocal branches.
        w=[JI if y==0 else J if t==2 else O for y in range(8)]
        ds=[mul(sub(w[y],O),f[t][y]) for y in range(8)]
        g[t]=tuple(add(a,b) for a,b in zip(gg,ds));c[t]=tuple(sub(a,b) for a,b in zip(pre[t],ds))
cp=tuple(sub(pre[4][y],mul(R,f[4][y])) for y in range(8))
target=tuple(add(z,sc(2,O)) for z in cp)
# Solve the same boundary constraints by a table of time-indexed reader cells.
stock={}
for y in range(8):
    S={(1,1):sc(-2*(-1)**y,mul(J,R))}
    def put(x,t,z):
        S[x,t]=z
    def get(x,t):
        return S[x,t]
    put(7,1,partner(c[1][y],pre[2][y]));put(6,1,get(7,1))
    put(7,2,sub(add(c[1][y],get(7,1)),pre[2][y]))
    put(1,2,partner(c[2][y],pre[3][y]))
    put(2,1,partner(get(1,1),get(1,2)));put(3,1,get(2,1))
    put(2,2,sub(add(get(1,1),get(2,1)),get(1,2)))
    put(1,3,sub(add(c[2][y],get(1,2)),pre[3][y]))
    put(7,3,partner(c[3][y],pre[4][y]))
    put(6,2,partner(get(7,2),get(7,3)))
    put(5,1,partner(get(6,1),get(6,2)))
    put(2,3,partner(get(1,3),target[y]))
    put(3,2,partner(get(2,2),get(2,3)))
    put(4,1,partner(get(3,1),get(3,2)))
    a,b=rationalC(get(4,1),get(5,1),True)
    assert rationalC(a,b)==(get(4,1),get(5,1))
    initial=(sc(-2*(-1)**y,J),get(2,1),get(3,1),a,b,get(6,1),get(7,1))
    for x,z in enumerate(initial,1):
        assert oddden(z)
        stock[x,y]=scale_eta(z)
pos=scale_eta(add(target[0],sub(R,O)));negative=scale_eta(target[0])
assert pos!=negative
def prepare(l,r):
    F=[]
    for x,y in product(range(8),repeat=2):
        if x==0:F.append(tuple(scale_eta(z) for z in val(ref(r),0,y)))
        else:F.append((Z,Z,Z,stock[x,(y+2*l)%8]))
    return tuple(F)
def bcheck(l,r,hh):
    cuts,mids,tags,ac=hh
    positive=(r-l)%4==2
    for t in range(1,5):
        for y in range(8):
            yy=(y+2*l)%8
            c0=val(mids[t],0,y)
            assert half(sub(c0[2],c0[3]))==scale_eta(f[t][yy])
            tag=1 if t==1 else (1 if yy==0 else 2) if t==2 else (1 if yy==0 else 0) if t==3 else (2 if yy==0 and positive else 0)
            assert tags[t][ix(0,y)]==tag
        assert not any(tags[t][8:])
    y=(-2*l)%8
    dv=sub(val(cuts[3],0,(y-1)%8)[0],val(cuts[3],0,y)[0])
    assert even(dv)==(not positive)
    assert (val(mids[4],0,y)[0]!=val(cuts[3],0,y)[0])==(not positive)
    assert val(cuts[4],1,y)[3]==negative
    assert val(cuts[5],1,y)[3]==(pos if positive else negative)
    assert (val(cuts[5],1,y)[3]!=val(cuts[4],1,y)[3])==positive
    assert not any(any(tags[t][8:]) for t in range(1,len(cuts)))
def recovery(hh,R0):
    out=[]
    for name,mat,initial in (('material_ref',True,False),('full_ref',False,False),('material_initial',True,True)):
        counts=[sum(src(hh[r][0][t],mat)==tuple(scale_eta(z) for z in src(R0[r][0][0 if initial else t],mat)) for r in range(4)) for t in range(1,161)]
        out.append((name,[t for t,n in enumerate(counts,1) if n==4],sorted(Counter(counts).items()),[(t,counts[t-1]) for t in (5,40,80,120,160)]))
    return out
def BC_gate(R0):
    for y in range(8):print('B STOCK',y,*[raw(stock[x,y]) for x in range(1,8)])
    print('B ETA',raw(eta),'Q_ETA',scalar(h(eta)))
    qvals=set();H0={}
    for l,r in product(range(4),repeat=2):
        F0=prepare(l,r)
        assert src(F0)==tuple(scale_eta(z) for z in src(ref(r)))
        assert reader(F0)==reader(prepare(l,0))
        hh=hist(F0,160 if l==0 else 12)
        bcheck(l,r,hh)
        if l==0:H0[r]=hh
        cuts,mids,tags,ac=hh
        qvals.add(scalar(ac[2]))
        positive=(r-l)%4==2;y=(-2*l)%8
        print('B CASE',l,r,'T4_C_ADMIT',int(not positive),'T4_TAG',2*int(positive),'REMOTE5',raw(val(cuts[5],1,y)[3]))
        print('B SOURCE4',l,r,'PRE_D',raw(val(mids[4],0,y)[0]),'POST_D',raw(val(cuts[4],0,y)[0]))
    assert len(qvals)==1
    print('B PASS',16,'POSITIVE',4,'Q',next(iter(qvals)),'R_POS',raw(pos),'R_NEG',raw(negative))
    for t in range(1,13):
        print('B READER_PREFIX',t,len({reader_words(H0[r],t) for r in range(4)}))
    for t in range(5,13):
        out=[pos if r==2 else negative for r in range(4)]
        print('B HOLD',t,'POST_C',sum(val(H0[r][1][t],1,0)[3]==out[r] for r in range(4)),
              'FULL',sum(val(H0[r][0][t],1,0)[3]==out[r] for r in range(4)))
    for name,times,counts,cuts in recovery(H0,R0):
        print('C COMMON',name,times);print('C HIST',name,counts);print('C CUTS',name,cuts)
    print('DONE exact separated-source active interrogation and recovery boundary')
    return H0

def setup(a,l,r):
    F=list(prepare(l,r));g=add(pos,sc(2,a));d=mul(JI,a)
    assert not even(d)
    for y in range(8):
        u,v,_,c0=val(F,1,y)
        if y==-2*l%8:u,v=d,neg(d)
        F[ix(1,y)]=(u,v,g,c0)
    return tuple(F)
def gvals(a):
    g=add(pos,sc(2,a));return g,add(g,mul(sub(JI,O),a))
def capture_ok(hs,a,H0,l=0):
    y=(-2*l)%8;g,mark=gvals(a)
    for r,hh in hs.items():
        cuts,mids,tags,ac=hh
        if l==0:assert all(src(cuts[t])==src(H0[r][0][t]) for t in range(6))
        assert not any(tags[t][ix(1,q)] for q in range(8) for t in range(1,5))
        positive=(r-l)%4==2
        assert val(mids[5],1,y)[3]==(pos if positive else negative)
        assert tags[5][ix(1,y)]==int(positive)
        assert val(cuts[5],1,y)[2]==(mark if positive else g)
        assert val(cuts[5],1,(y+1)%8)[2]==g
    assert len({scalar(hh[3][2]) for hh in hs.values()})==1
def hold(hs,a,l=0):
    y=(-2*l)%8;g,mark=gvals(a);n=0
    for t in range(6,13):
        for stage in (1,0):
            if not all(val(hh[stage][t],1,y)[2]==(mark if (r-l)%4==2 else g)
                        and val(hh[stage][t],1,(y+1)%8)[2]==g for r,hh in hs.items()):
                return n
            n+=1
    return n
def D_gate():
    R0={r:hist(ref(r),160) for r in range(4)}
    H0={r:hist(prepare(0,r),12) for r in range(4)}
    records=[];idle_count=0;counts=Counter()
    for v,n in product(tuple(x for x in product(range(2),repeat=4) if any(x)),range(1,16,2)):
        a=sc(n,v+(0,));g,_=gvals(a);d=mul(JI,a)
        tags=tuple(B((d,neg(d),g,val(H0[0][1][t],1,0)[3]))[1] for t in range(1,5))
        if any(tags):
            print('D CANDIDATE',raw(a),'EARLY_TAGS',tags,'REJECT');continue
        idle_count+=1
        hs={r:hist(setup(a,0,r),12) for r in range(4)}
        capture_ok(hs,a,H0)
        n_hold=hold(hs,a);counts[n_hold]+=1
        Q0=scalar(hs[0][3][2]);records.append((n_hold,a,Q0))
        print('D CANDIDATE',raw(a),'EARLY_TAGS',tags,'HOLD',n_hold,'Q',Q0)
    print('D CENSUS',120,'IDLE',idle_count,'HOLD_HIST',sorted(counts.items()))
    if records:
        length,a,Q0=max(records,key=lambda q:q[0]);g,mark=gvals(a)
        print('D SELECT',raw(a),'HOLD',length,'Q',Q0,'G',raw(g),'MARK',raw(mark),'DELTA',raw(sub(mark,g)))
        hs={r:hist(setup(a,0,r),160) for r in range(4)}
        capture_ok(hs,a,H0);assert hold(hs,a)==length
        for t in range(1,13):
            print('D PREFIX',t,'READER_CLASSES',len({reader_words(hh,t) for hh in hs.values()}),
                  'FULL_READER_CLASSES',len({reader(hh[0][t]) for hh in hs.values()}))
        for r,hh in hs.items():
            cut,mid,tags,ac=hh
            print('D RECORD',r,'POST_C5',rawcell(val(mid[5],1,0)),'FULL5',rawcell(val(cut[5],1,0)))
            for t in range(1,13):
                print('D LOCAL',r,t,'TAG',tags[t][ix(1,0)],'CLK',raw(val(cut[t],1,0)[2]),'REF',raw(val(cut[t],1,1)[2]))
        for name,times,counts,cuts in recovery(hs,R0):
            print('D RECOVERY',name,'COMMON',times,'HIST',counts,'CUTS',cuts)
        for l in range(4):
            hhs={r:hist(setup(a,l,r),12) for r in range(4)}
            capture_ok(hhs,a,H0,l);assert hold(hhs,a,l)==length
            for r,hh in hhs.items():
                print('D TRANSLATED',l,r,'CLK5',raw(val(hh[0][5],1,(-2*l)%8)[2]),'HOLD',length)
        print('D PASS',16,'FIXED_NATIVE_PORT',1,0,'COMMON_HOLD_SUBSTEPS',length)
    else:print('D NO CAPTURE')
    print('DONE exact separate reader capture')
if sys.argv[1]=='ABC':BC_gate(A_gate())
elif sys.argv[1]=='D':D_gate()
else:raise SystemExit('use ABC or D')
