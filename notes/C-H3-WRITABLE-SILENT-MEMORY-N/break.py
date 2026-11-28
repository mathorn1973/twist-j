"""NON-CANONICAL #2129, result-exposed alternate exact ring/update audit.
No import of the primary or public H3 source. Recomputes the entire
finite memory census, selected full trajectories and conditional clocks.
"""
from functools import cache
from itertools import product
from collections import Counter
from fractions import Fraction as Q

def red(a):
    a=tuple(a)
    return tuple(x-a[4] for x in a[:4])+(0,)
def p(n):return red(int(k==n%5) for k in range(5))
def add(a,b):return red(x+y for x,y in zip(a,b))
def sc(k,a):return red(k*x for x in a)
def sub(a,b):return add(a,sc(-1,b))
@cache
def mul(a,b):return red(sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5))
def conj(a):return red(a[(4*k)%5] for k in range(5))
@cache
def h(a):return mul(a,conj(a))
O=p(0);Z=sc(0,O);R=p(2);J=add(O,R);JI=sc(-1,add(p(1),p(2)))
T=h(J);P=tuple(p(k) for k in range(5));L=sub(O,R);delta=sub(O,JI)
assert mul(J,JI)==O
def raw(a):return a[:4]
def flat(F):return tuple(raw(z) for c in F for z in c)
def neg(a):return sc(-1,a)
def even(a):return all(x%2==0 for x in a)
def half(a):
    assert even(a)
    return tuple(x//2 for x in a)
def rs(xs):
    a=Z
    for z in xs:a=add(a,z)
    return a
def scalar(a):
    n=4*a[0]-sum(a[1:]);assert n%2==0;return n//2
@cache
def C(a,b,back=False):
    dif=sub(a,b)
    if not even(dif):return a,b
    u=mul(P[3] if back else R,dif)
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
def cell(d,g,c):return d,neg(d),g,c
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
    N=tuple(c for c,k in ct)
    ev=tuple((x,y,ct[ix(x,y)][1]) for x,y in product(range(8),range(2)) if ct[ix(x,y)][1])
    assert acc(G)==acc(N)==a
    back=tuple(B(c)[0] for c in N)
    assert back==G and trans(back,bit,True)==F
    return G,N,ev
g=add(sc(2,O),P[3]);gp=sub(g,delta)
NS=(0,1,-1,3,-3,5,-5)
WS=(Z,)+tuple(sc(s,P[k]) for s,k in product((1,-1),range(5)))
def radiation(n):
    a,b,c=(sc(k,P[4]) for k in n)
    return b,a,neg(P[4]),P[4],neg(a),neg(b),neg(c),c
def rstep(row,bit,back=False):
    out=list(row)
    for x in range(bit,8,2):
        k=(x+1)%8;out[x],out[k]=C(row[x],row[k],back)
    return tuple(out)
def seed(n,w,b):
    rr=list(rstep(radiation(n),0,True))
    u=P[1] if b else neg(R);rr[2:4]=[u,neg(u)]
    v=add(neg(P[4]),sc(2,w));F=[]
    for x,y in product(range(8),range(2)):
        s=1 if x==2 else -1
        d=sc(s,JI) if x in (2,3) and y==0 else Z
        clk=sc(s,g if y==0 else v) if x in (2,3) else Z
        F.append(cell(d,clk,rr[x] if y==0 else Z))
    return tuple(F)
def corr(F):return tuple(c[3] for c in F)
def outside(F):return tuple(c for i,c in enumerate(F) if i//2 not in (2,3))
def mat(F):return tuple(F[ix(x,y)][0] for x,y in product((2,3),range(2)))
def wanted(b):return (O if b else JI),Z,neg(O if b else JI),Z
def write(n,w):
    I=[seed(n,w,b) for b in (0,1)];a=acc(I[0]);assert a==acc(I[1])
    assert all(I[0][i]==I[1][i] for i in range(16) if i not in (4,6))
    assert all(I[0][i][:3]==I[1][i][:3] for i in (4,6))
    F=[]
    for b,f in enumerate(I):
        G,X,ev=step(f,0,a)
        assert G[ix(2,0)][3]==(P[3] if b else neg(P[4]))
        assert ev==(((2,0,1),(3,0,1)) if b else ())
        assert tuple(X[ix(x,0)][3] for x in range(8))==radiation(n)
        assert all(X[ix(x,1)][3]==Z for x in range(8))
        assert mat(X)==wanted(b)
        F.append(X)
    assert corr(F[0])==corr(F[1]) and outside(F[0])==outside(F[1])
    return I,a,F
def B_gate():
    census=Counter();best=None
    for n in product(NS,repeat=3):
        row=radiation(n);rows=[]
        for k in range(1,513):
            row=rstep(row,k%2);rows.append(row)
        for wi,w in enumerate(WS):
            I,a,F=write(n,w)
            # Advance the actual two vertical CLK pairs by C, rather than
            # evaluating a period-indexed formula for the local record.
            clk=[(F[b][4][2],F[b][5][2]) for b in (0,1)]
            hold=512;fail=None
            for k,row in enumerate(rows,1):
                clk=[C(*pair) for pair in clk]
                ev=[(b,x,B(cell(sc(s,O if b else JI),sc(s,clk[b][0]),row[x]))[1])
                    for b in (0,1) for x,s in ((2,1),(3,-1))]
                hit=next(((b,x,t) for b,x,t in ev if t),None)
                if hit:
                    hold=k-1;fail=(k+1,*hit);break
            census[hold]+=1
            if best is None or hold>best[0]:best=hold,n,wi,w,fail
    assert sum(census.values())==3773
    print('B CENSUS','TRIED',3773,'HIST',sorted(census.items()),'GE114',sum(n for h,n in census.items() if h>=114),'FULL512',census[512])
    hold,n,wi,w,fail=best
    print('B SELECT',(hold,n,wi,raw(w),fail))
    I,a,F=write(n,w)
    print('B ACCOUNT',tuple(map(raw,a)),'Q',scalar(a[2]))
    for b in (0,1):
        print('B INITIAL',b,flat(I[b]))
        print('B WRITE',b,flat(F[b]))
    F=I[:];first=[None,None];returns=[None,None];loss=recordloss=None
    for t in range(1,4097):
        G=[];N=[]
        for b in (0,1):
            m,f,ev=step(F[b],(t-1)%2,a);G.append(m);N.append(f)
            if t>1 and first[b] is None and ev:first[b]=t,ev
            if t%2==0 and returns[b] is None and f==I[b]:returns[b]=t
        if t>=2:
            for stage,ff in ((1,G),(0,N)):
                if loss is None and (corr(ff[0])!=corr(ff[1]) or outside(ff[0])!=outside(ff[1])):loss=t,stage
                if recordloss is None and any(mat(ff[b])!=wanted(b) for b in (0,1)):recordloss=t,stage
        F=N
        if t==hold+1:
            assert corr(F[0])==corr(F[1]) and outside(F[0])==outside(F[1])
            assert all(mat(F[b])==wanted(b) for b in (0,1))
            for b in (0,1):print('B HELD_ENDPOINT',b,t,flat(F[b]))
        if t>=513 and all(v is not None for v in first) and all(v is not None for v in returns):break
    print('B FUTURE','THROUGH',t,'FIRST_B',first,'FIRST_RETURN',returns,'CORR_OR_OUTSIDE_LOSS',loss,'MATERIAL_LOSS',recordloss)
    print('B PASS native conversion and exact finite silent interval')
def C_gate():
    bi=sc(Q(2,5),rs((sc(4,O),sc(3,R),sc(2,P[4]),P[1])))
    assert mul(sc(Q(1,2),L),bi)==O
    r=(-2,-2,9,-5,0);c=(7,-8,12,-2,0);d1=(12,0,6,6,0);d2=(0,6,0,0,0)
    def f(d,tag):return mul(d,mul(J,P[3]) if tag==1 else neg(P[3]))
    def scale(z):
        v=mul(L,z);assert all(Q(a).denominator==1 for a in v)
        return tuple(map(int,v))
    def rot(p,n,back=False):
        for _ in range(n%5):p=C(*p,back)
        return p
    allowed=tuple(scale(add(r,sc(2,f(d1,a)))) for a in (1,2));match=0
    for a,b in product((1,2),repeat=2):
        f1,f2=f(d1,a),f(d2,b);g1=add(r,sc(2,f1));post=sub(g1,d1);g2=add(c,sc(2,f2))
        gr=add(post,mul(bi,sub(g2,post)))
        ready=tuple(map(scale,(g1,gr)));ini=rot(ready,113,True)
        assert rot(ini,113)==ready and even(sub(*ready))
        g_second=rot(ready,114)[0];tags=tuple(int(g_second==g0) for g0 in allowed);match+=sum(tags)
        v=ini
        for t in range(1,228):
            v=C(*v)
            if t==113:assert v==ready
            if t==227:assert v[0]==g_second
        print('C CLOCK',a,b,'INITIAL',tuple(map(raw,ini)),'READY113',tuple(map(raw,ready)),'SECOND227',raw(g_second),'ALLOWED',tuple(map(raw,allowed)),'MATCH',tags)
    print('C MATCHING_TAG_PAIRS',match,'OF',4,'MATERIAL_CHOICES_PER_PAIR',100)
if __name__=='__main__':
    B_gate();C_gate()
    print('DONE exact writable memory and conditional repeat-clock test')
