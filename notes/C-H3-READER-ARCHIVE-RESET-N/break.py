"""NON-CANONICAL #2121 alternate exact audit.
Result-exposed; independent cyclic five-coefficient ring and update.
Replays A, D1 and selected D2; does not repeat the B search.
"""
from functools import cache
from itertools import product
from collections import Counter

def red(z):
    z=tuple(z)
    return tuple(x-z[4] for x in z[:4])+(0,)
def p(n):return red(int(k==n%5) for k in range(5))
def add(a,b):return red(x+y for x,y in zip(a,b))
def sc(k,a):return red(k*x for x in a)
def sub(a,b):return add(a,sc(-1,b))
@cache
def mul(a,b):return red(sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5))
def conj(a):return red(a[(4*k)%5] for k in range(5))
@cache
def h(a):return mul(a,conj(a))
O=p(0);Z=sc(0,O);R=p(2);RI=p(3);J=add(O,R);JI=sc(-1,add(p(1),p(2)))
L=sub(O,R);T=h(J);P=tuple(p(k) for k in range(5))
assert mul(J,JI)==O
def raw(a):return a[:4]
def flat(F):return tuple(raw(z) for c in F for z in c)
def even(a):return all(x%2==0 for x in a)
def half(a):
    assert even(a)
    return tuple(x//2 for x in a)
def rs(xs):return tuple(map(sum,zip(*xs)))
def scalar(a):
    n=4*a[0]-sum(a[1:]);assert n%2==0
    return n//2
@cache
def C(a,b,back=False):
    dif=sub(a,b)
    if not even(dif):return a,b
    u=mul(RI if back else R,dif)
    return half(add(add(a,b),u)),half(sub(add(a,b),u))
@cache
def B(cell):
    a,b,u,v=cell
    if not even(sub(a,b)) or not even(sub(u,v)):return cell,0
    d,f=half(sub(a,b)),half(sub(u,v));cm,cr=half(add(a,b)),half(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        dn,fn,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        dn,fn,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(cm,dn),sub(cm,dn),add(cr,fn),sub(cr,fn)),k
def ix(x,y):return 2*x+y
def cell(d,g,c):return d,sc(-1,d),g,c
def source(F):return F[:2]
def worker(F):return F[12:14]
def store(F):return tuple(z for c in F[12:14] for z in c[:3])
ARCH=(1,2,3,4,5,7)
def archive(F):return tuple(F[ix(x,y)] for x,y in product(ARCH,range(2)))
def reader(F):return F[2:]
def trans(F,bit,back=False):
    G=[list(c) for c in F]
    for x in range(8):
        i,k=ix(x,bit),ix(x,1-bit)
        for q in range(3):G[i][q],G[k][q]=C(F[i][q],F[k][q],back)
    for x,y in product(range(bit,8,2),range(2)):
        i,k=ix(x,y),ix((x+1)%8,y)
        G[i][3],G[k][3]=C(F[i][3],F[k][3],back)
    return tuple(tuple(c) for c in G)
def acc(F):
    return rs(z for c in F for z in c[:2]),rs(z for c in F for z in c[2:]),rs(h(z) for c in F for z in c)
def step(F,bit,a):
    G=trans(F,bit);ct=tuple(B(c) for c in G)
    N=tuple(c for c,k in ct);tags=tuple(k for c,k in ct)
    assert acc(G)==acc(N)==a
    back=tuple(B(c)[0] for c in N)
    assert back==G and trans(back,bit,True)==F
    return G,N,tags
def hist(F,n):
    ac=acc(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac);cuts.append(F);mids.append(G);tags.append(E)
    return cuts,mids,tags,ac
m=sub(sc(2,O),R);gs=sc(2,mul(J,m));a=sc(-3,L)
b=add(add(mul(m,R),mul(J,a)),sc(12,J))
stock=(Z,Z,Z,b,b,b,add(mul(m,R),sc(2,a)))
g=(6,-2,12,1,0);mark=(5,-3,11,1,0)
K=range(5);N=(0,2,3,4)
def seed(k,variant):
    d0=(JI,JI) if variant=='static' else ((1,-1,-1,-1,0),(1,-1,-1,1,0))
    return tuple(cell((P[k] if y==0 else sc(3,P[1])) if x==0 else d0[y] if x==6 else Z,
                      gs if x==0 else g if x==6 else Z,
                      (Z if x==0 else stock[x-1]) if y==0 else gs) for x,y in product(range(8),range(2)))
def ret(F,I,part):return all(part(F[k])==part(I[k]) for k in K)
def two(F,part):
    return len({part(F[k]) for k in N})==1 and part(F[1])!=part(F[0])
def sectors(F,I):
    return tuple(tuple(raw(sub(a,b)) for a,b in zip(acc(part(F)),acc(part(I)))) for part in (source,worker,archive))
def all_ports(F):
    return [(x,y,q) for x,y,q in product(ARCH,range(2),(2,3))
               if all(F[k][ix(x,y)][q]==F[0][ix(x,y)][q] for k in N)
               and F[1][ix(x,y)][q]!=F[0][ix(x,y)][q]]
def audit_A(variant):
    hh=[hist(seed(k,variant),4096) for k in K];I=[w[0][0] for w in hh]
    assert len({w[3] for w in hh})==1
    Q=scalar(hh[0][3][2]);assert Q==(2630 if variant=='static' else 2654)
    if variant=='static':
        joint=[(t%2,tuple(w[0][t] for w in hh)) for t in range(929)]
        assert joint[-1]==joint[0] and len(set(joint[:-1]))==928
    for k,w in enumerate(hh):
        assert w[0][6][12][2]==(mark if k==1 else g) and w[0][6][13][2]==g
        assert w[2][6][12:14]==(int(k==1),0)
    loss=next((t,s) for t in range(7,161) for s in (1,0)
              if any(w[s][t][12][2]!=(mark if k==1 else g) or w[s][t][13][2]!=g for k,w in enumerate(hh)))
    assert loss==(111,0)
    neg=True;pos=False;work=[];both=[];full=[];field=[];R0=[];nweak=nfull=0;qual=[];common=[]
    first=None
    for t in range(1,4097):
        for s in (1,0):
            arr=[reader(w[s][t]) for w in hh]
            neg &= all(arr[k]==arr[0] for k in N);pos |= arr[1]!=arr[0]
        F=[w[0][t] for w in hh]
        S,W,U=ret(F,I,source),ret(F,I,store),ret(F,I,worker)
        if W and t>=6:work.append(t)
        if t<6 or t%2:continue
        if S:R0.append(t)
        if F==I:field.append(t)
        if not (S and W):continue
        both.append(t)
        if U:full.append(t)
        ok=two(F,archive) and neg and pos
        ports=all_ports(F) if ok else []
        if ok and ports:
            nweak+=1;nfull+=U
            if len({worker(f) for f in F})==1:common.append(t)
            if t<928:qual.append(t)
            if first is None:
                x,y,q=ports[0];i=ix(x,y)
                a,b=F[0][i][q],F[1][i][q]
                loss=next(((u,s) for u in range(t+1,4097) for s in (1,0)
                           if any(w[s][u][i][q]!=(b if k==1 else a) for k,w in enumerate(hh))),None)
                first=(t,x,y,q,raw(a),raw(b),loss)
                print('ALT A FIRST_SECTORS',variant,t,0,sectors(F[0],I[0]))
                print('ALT A FIRST_SECTORS',variant,t,1,sectors(F[1],I[1]))
    assert [t for t in R0 if 6<=t<=110]==[16,30,44,58,72,86,100]
    if variant=='static':
        assert work[0]==111 and both==[114,384,758,928,1042,1312,1686,1856,1970,2240,2614,2784,2898,3168,3542,3712,3826,4096]
        assert full==field==[928,1856,2784,3712]
        assert (nweak,nfull)==(14,0) and common==[] and qual==[114,384,758]
        assert first==(114,5,0,3,(7,-2,12,-2),(1,-5,6,-2),(116,1))
    else:
        assert work[0]==115 and not both and not full and not field and not common and nweak==nfull==0
    assert neg
    print('ALT A',variant,'Q',Q,'FIRST_STORE',work[0],'SOURCE_RETURNS',R0,'BOTH',both,'FULL',full,'FIELD',field,'WEAK_RECORDS',nweak,'FULL_RECORDS',nfull,'FIRST',first,'COMMON_CONTEXT',common)
    return hh
def rot(pair,n,back=False):
    for _ in range(n%5):pair=C(*pair,back)
    return pair
def D(old):
    t,x=114,5;f=P[3];w=O
    Rp=old[1][1][t][ix(x,0)][3]
    assert raw(Rp)==(1,-5,6,-2)
    assert len({old[k][1][t][ix(x,0)][3] for k in N})==1 and Rp!=old[0][1][t][ix(x,0)][3]
    assert all(old[k][1][u][ix(x,0)][3]!=Rp for u,k in product(range(1,t),K) if (t-u)%5==0)
    ready=mul(JI,f),add(mul(JI,f),sc(2,w));d=rot(ready,t,True)
    G=add(Rp,sc(2,f));M=add(G,mul(sub(JI,O),f))
    assert tuple(map(raw,d))==((1,1,0,1),(1,1,2,1))
    assert raw(G)==(1,-5,6,0) and raw(M)==(1,-4,7,0)
    cur=d
    for u in range(1,t+1):
        cur=rot(cur,1)
        for k,y in product(K,range(2)):
            assert B(cell(cur[y],G,old[k][1][u][ix(x,y)][3]))[1]==int(u==t and k==1 and y==0)
    assert cur==ready
    def setup(k):
        F=list(old[k][0][0])
        for y in range(2):F[ix(x,y)]=cell(d[y],G,F[ix(x,y)][3])
        return tuple(F)
    hh=[hist(setup(k),t+256) for k in K];I=[w[0][0] for w in hh]
    assert len({w[3] for w in hh})==1 and scalar(hh[0][3][2])==2952
    for k,w0 in enumerate(hh):
        for u in range(1,t):
            assert source(w0[0][u])==source(old[k][0][u]) and worker(w0[0][u])==worker(old[k][0][u])
            assert tuple(c[3] for c in w0[0][u])==tuple(c[3] for c in old[k][0][u])
            assert w0[2][u][2*x:2*x+2]==(0,0)
        assert w0[2][t][2*x:2*x+2]==(int(k==1),0)
        assert w0[1][t][ix(x,0)][3]==old[k][1][t][ix(x,0)][3]
        assert w0[0][t][ix(x,0)][2]==(M if k==1 else G) and w0[0][t][ix(x,1)][2]==G
    neg=True;pos=False;active=True;loss=None;weak=[];common=[];full=[]
    for u in range(t+257):
        for s in ((0,) if u==0 else (1,0)):
            arr=[reader(w0[s][u]) for w0 in hh]
            neg &= all(arr[k]==arr[0] for k in N);pos |= arr[1]!=arr[0]
            if u>t and active and any(w0[s][u][ix(x,0)][2]!=(M if k==1 else G) or w0[s][u][ix(x,1)][2]!=G for k,w0 in enumerate(hh)):
                active=False;loss=u,s
        if u==t:assert neg and pos
        if u<t or u%2 or not (active and neg and pos):continue
        F=[w0[0][u] for w0 in hh]
        if ret(F,I,source) and ret(F,I,store) and two(F,archive):
            weak.append(u)
            if len({worker(ff) for ff in F})==1:common.append(u)
            if ret(F,I,worker):full.append(u)
    assert weak==[114] and not common and not full and loss==(115,0)
    print('ALT D',t,x,'INIT',tuple(map(raw,d)),'G',raw(G),'MARK',raw(M),'Q',scalar(hh[0][3][2]),'WEAK',weak,'COMMON',common,'FULL',full,'LOSS',loss)
    for k in (0,1):
        F=hh[k][0][t]
        print('ALT D WITNESS',k,'SOURCE',flat(source(F)),'WORKER',flat(worker(F)),'ARCHIVE',flat(F[2*x:2*x+2]))
        print('ALT D SECTORS',k,sectors(F,I[k]))
if __name__=='__main__':
    old=audit_A('static')
    audit_A('rotating');D(old)
    print('PASS alternate exact A/D1 and selected D2')
