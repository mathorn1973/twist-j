"""NON-CANONICAL #2129, exact finite writable silent memory and clock obstruction."""
import hashlib,sys,importlib.util
from pathlib import Path
from itertools import product
from functools import cache
from fractions import Fraction as Q
from collections import Counter
source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H;spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,R,J,JI,P=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV,H.J_POWERS
add,sub,mul,sc,h=H.add,H.sub,cache(H.mul),H.scale,H.h
neg=lambda x:sc(-1,x)
L=sub(O,R);delta=sub(O,JI)
g=add(sc(2,O),P[3]);gp=sub(g,delta)
assert add(P[3],delta)==neg(P[4])
ix=lambda x,y,r:H.index(2,x,y,r)
MEM=(2,3)
NS=(0,1,-1,3,-3,5,-5)
WS=(Z,)+tuple(sc(s,P[k]) for s,k in product((1,-1),range(5)))
def cols(d,g,c):return d,neg(d),g,c
def account(F):
    return (H.ring_sum(z for i,z in enumerate(F) if i%4<2),
            H.ring_sum(z for i,z in enumerate(F) if i%4>=2),
            H.ring_sum(h(z) for z in F))
def step(F,bit,ac):
    G=H.transport(F,2,bit);V,ev=H.collide(G,2)
    back,_=H.collide(V,2)
    assert back==G and H.transport(back,2,bit,True)==F
    assert account(G)==account(V)==ac
    return G,V,ev
def radiation(a,b,c):
    a,b,c=(sc(n,P[4]) for n in (a,b,c))
    return (b,a,neg(P[4]),P[4],neg(a),neg(b),neg(c),c)
def rstep(row,bit,back=False):
    G=list(row)
    for x in range(bit,8,2):
        y=(x+1)%8
        G[x],G[y]=H.transport_pair(row[x],row[y],back)
    return tuple(G)
def seed(n,w,bit):
    post=radiation(*n);rr=list(rstep(post,0,True))
    # The input pair is the only bit-dependent part of the preparation.
    u=P[1] if bit else neg(R)
    rr[2],rr[3]=u,neg(u)
    v=add(neg(P[4]),sc(2,w))
    F=[]
    for x,y in product(range(8),range(2)):
        if x in MEM:
            s=1 if x==2 else -1
            d=sc(s,JI) if y==0 else Z
            clk=sc(s,g if y==0 else v)
        else:d=clk=Z
        F.extend(cols(d,clk,rr[x] if y==0 else Z))
    return tuple(F)
def corr(F):return F[3::4]
def outside(F):return tuple(F[ix(x,y,r)] for x,y,r in product(range(8),range(2),range(4)) if x not in MEM)
def mat(F):return tuple(F[ix(x,y,0)] for x,y in product(MEM,range(2)))
def write(n,w):
    I=[seed(n,w,b) for b in (0,1)];ac=account(I[0]);assert ac==account(I[1])
    assert all(I[0][i]==I[1][i] for i in range(len(I[0])) if i not in (ix(2,0,3),ix(3,0,3)))
    V=[]
    for b,f in enumerate(I):
        G,X,ev=step(f,0,ac)
        assert G[ix(2,0,3)]==(P[3] if b else neg(P[4]))
        assert ev==(((2,0,1),(3,0,1)) if b else ())
        assert tuple(X[ix(x,0,3)] for x in range(8))==radiation(*n)
        assert all(X[ix(x,1,3)]==Z for x in range(8))
        assert mat(X)==((O if b else JI),Z,neg(O if b else JI),Z)
        assert X[ix(2,0,2)]==(gp if b else g)
        V.append(X)
    assert corr(V[0])==corr(V[1]) and outside(V[0])==outside(V[1])
    return I,ac,V
def free_clk(w,b):
    v=add(neg(P[4]),sc(2,w));pair=(gp if b else g,v)
    out=[pair]
    for _ in range(5):out.append(H.transport_pair(*out[-1],False))
    assert out[-1]==out[0]
    return tuple(out[:-1])
def test(n,w,rows):
    # At full1 all CORR common. While no B, vertical C is independent of
    # incoming CORR; d is stationary because the other row is zero and
    # its own parity is nonzero. Reflection negates x2 and x3.
    clocks=tuple(free_clk(w,b) for b in (0,1))
    for k,row in enumerate(rows,1):
        for b in (0,1):
            d=O if b else JI
            clk=clocks[b][k%5][0]
            for x,s in ((2,1),(3,-1)):
                _,tag=H.collision(cols(sc(s,d),sc(s,clk),row[x]))
                if tag:return k-1,(k+1,b,x,tag)
        # row1 d=0 and all other d=0, so no collision.
    return len(rows),None
def B():
    census=Counter();firstfails=Counter();best=None;matches114=0
    for n in product(NS,repeat=3):
        row=radiation(*n);rows=[]
        for k in range(1,513):
            row=rstep(row,k%2);rows.append(row)
        for wi,w in enumerate(WS):
            # Literal first write on every candidate, followed by exact
            # reduced no-B continuation until the first failing guard.
            I,ac,V=write(n,w)
            hold,fail=test(n,w,rows)
            census[hold]+=1;firstfails[fail[1:]+(fail[0],) if fail else None]+=1
            matches114+=hold>=114
            if best is None or hold>best[0]:best=hold,n,wi,w,fail
    assert sum(census.values())==3773
    print('B CENSUS','TRIED',3773,'HIST',sorted(census.items()),'GE114',matches114,'FULL512',census[512])
    print('B SELECT',best)
    hold,n,wi,w,fail=best
    I,ac,V=write(n,w)
    print('B ACCOUNT',ac,'Q',H.scalar_account(ac[2]))
    for b in (0,1):
        print('B INITIAL',b,I[b])
        print('B WRITE',b,V[b])
    F=I[:];first=[None,None];returns=[None,None];common_loss=None;record_loss=None;Bafter=[]
    for t in range(1,4097):
        G=[];V0=[];ee=[]
        for b in (0,1):
            m,f,ev=step(F[b],(t-1)%2,ac);G.append(m);V0.append(f);ee.append(ev)
            if t>1 and first[b] is None and ev:
                first[b]=(t,ev)
                Bafter.append((b,t,ev))
            if t%2==0 and returns[b] is None and f==I[b]:returns[b]=t
        if t>=2:
            for stage,ff in ((1,G),(0,V0)):
                if common_loss is None and (corr(ff[0])!=corr(ff[1]) or outside(ff[0])!=outside(ff[1])):common_loss=t,stage
                if record_loss is None and any(mat(ff[b])!=((O if b else JI),Z,neg(O if b else JI),Z) for b in (0,1)):record_loss=t,stage
        F=V0
        if t==hold+1:
            assert corr(F[0])==corr(F[1]) and outside(F[0])==outside(F[1])
            assert all(mat(F[b])==((O if b else JI),Z,neg(O if b else JI),Z) for b in (0,1))
            for b in (0,1):print('B HELD_ENDPOINT',b,t,F[b])
        if t>=513 and all(v is not None for v in first) and all(v is not None for v in returns):break
    assert min((x[0] for x in first if x),default=4097)==hold+2 if hold<512 else min((x[0] for x in first if x),default=4097)>=514
    print('B FUTURE','THROUGH',t,'FIRST_B',first,'FIRST_RETURN',returns,'CORR_OR_OUTSIDE_LOSS',common_loss,'MATERIAL_LOSS',record_loss)
    print('B PASS native conversion and exact finite silent interval')
def C():
    # Entire four CLK-pair choices, independent of signed-root material.
    eta=L;beta=sc(Q(1,2),eta);bi=H.inverse(beta)
    assert mul(beta,bi)==O
    r=(-2,-2,9,-5);c=(7,-8,12,-2)
    d1=(12,0,6,6);d2=(0,6,0,0)
    def f_for(d,tag):return mul(d,H.inverse(sub(O,JI if tag==1 else J)))
    def scale(z):
        p=mul(eta,z);assert all(Q(v).denominator==1 for v in p);return tuple(map(int,p))
    def rot(p,n,back=False):
        for _ in range(n%5):p=H.transport_pair(*p,back)
        return p
    allowed=tuple(scale(add(r,sc(2,f_for(d1,tag)))) for tag in (1,2))
    match=0
    for a,b in product((1,2),repeat=2):
        f1=f_for(d1,a);f2=f_for(d2,b)
        g1=add(r,sc(2,f1));g1p=sub(g1,d1);g2=add(c,sc(2,f2))
        gr=add(g1p,mul(bi,sub(g2,g1p)))
        ready=tuple(map(scale,(g1,gr)));ini=rot(ready,113,True)
        assert rot(ini,113)==ready and H.even(sub(*ready))
        g_second=rot(ready,114)[0]
        tags=tuple(int(g_second==g0) for g0 in allowed);match+=sum(tags)
        # Literal C-only initial to second pre-B cuts; the negative first
        # input has B idle, so this is the required clock prehistory.
        v=ini
        for t in range(1,228):
            v=H.transport_pair(*v,False)
            if t==113:assert v==ready
            if t==227:assert v[0]==g_second
        print('C CLOCK',a,b,'INITIAL',ini,'READY113',ready,'SECOND227',g_second,'ALLOWED',allowed,'MATCH',tags)
    print('C MATCHING_TAG_PAIRS',match,'OF',4,'MATERIAL_CHOICES_PER_PAIR',100)
if __name__=='__main__':
    B();C()
    print('DONE exact writable memory and conditional repeat-clock test')
