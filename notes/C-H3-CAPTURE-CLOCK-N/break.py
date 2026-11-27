"""NON-CANONICAL result-exposed alternate #2119.
Five cyclic coefficients, independent local update, direct complete fields.
Checks A census, selected B witness, C failure and D/E controls.
Does not repeat the primary B enumeration or import its code.
"""
from functools import cache
from itertools import product
from collections import Counter
from pathlib import Path
import ast,re,hashlib
root=Path(__file__).resolve().parent
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
O=p(0);Z=sc(0,O);R=p(2);RI=p(3);J=add(O,R);JI=sc(-1,add(p(1),p(2)))
L=sub(O,R);T=h(J);P=tuple(p(k) for k in range(5))
assert mul(J,JI)==O
def raw(a):return a[:4]
def pairraw(a):return tuple(map(raw,a))
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
def reader(F):return F[2:]
def matter(F):return F[12][0],F[13][0]
def port(F):return F[12][2]
def ref(F):return F[13][2]
def corr(F):return F[12][3]
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
def acraw(ac):return tuple(map(raw,ac))
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
def words(hh,t):
    cut,mid,_,_=hh
    return tuple(reader(F) for u in range(t+1) for F in ((cut[u],) if u==0 else (mid[u],cut[u])))
m=sub(sc(2,O),R);gs=sc(2,mul(J,m));mR=mul(m,R)
V=(Z,)+tuple(sc(s,P[k]) for s in (1,-1) for k in range(5))
def stock(n,l,vi):
    u=sc(n,P[l]);a=mul(L,u);v=V[vi];z=mul(L,v)
    b=sub(add(mR,mul(J,a)),sc(4,mul(J,u)))
    c2=add(mR,mul(L,a))
    assert not even(b) and (z==Z or (not even(z) and not even(sub(z,c2))))
    return Z,sc(2,v),sc(2,v),b,b,b,add(mR,sc(2,a))
def seed(p0,st,d=None,g=None):
    F=[]
    for x,y in product(range(8),range(2)):
        mat=(p0 if y==0 else sc(3,P[1])) if x==0 else Z
        clk=gs if x==0 else Z
        c=(Z if x==0 else st[x-1]) if y==0 else gs
        if d is not None and x==6:mat=d[y];clk=g
        F.append(cell(mat,clk,c))
    return tuple(F)
def A():
    prev=(root/'B_PREV.txt').read_bytes()
    assert hashlib.sha256(prev).hexdigest()=='83a3879a57fa20e6975f2dad47294f357854ff0d7caf673081e14d55dc2c3488'
    counts=Counter();first=Counter();nstock=nt=0
    for line in prev.decode().splitlines():
        ma=re.match(r'^B STOCK (-?\d+) (\d+) (\d+) .* MATCHES (\[.*?\]) NEGATIVE_SPLIT ',line)
        if not ma:continue
        n,l,vi=map(int,ma.groups()[:3]);tt=ast.literal_eval(ma[4])
        if not tt:continue
        hh=[hist(seed(p0,stock(n,l,vi)),max(tt)) for p0 in P];nstock+=1
        assert len({w[3] for w in hh})==1
        for k,t in enumerate(tt):
            assert all(source(w[0][t])==source(w[0][0]) for w in hh)
            assert len({words(w,t) for w in hh})==2
            assert len({words(hh[i],t) for i in (0,2,3,4)})==1
            r=corr(hh[1][1][t])
            assert corr(hh[1][0][t])==r and all(corr(hh[i][0][t])!=r for i in (0,2,3,4))
            same=[(u,i) for u,i in product(range(1,t),range(5)) if corr(hh[i][1][u])==r]
            mod=[(u,i) for u,i in same if (t-u)%5==0]
            key=bool(same),bool(mod);counts[key]+=1;nt+=1
            if k==0:first[key]+=1
            print('A WITNESS',n,l,vi,t,'EARLIEST',same[0] if same else None,'SAME_MOD5',mod[0] if mod else None)
    assert (nstock,nt)==(143,202)
    print('A ALL',nt,sorted(counts.items()))
    print('A FIRST',nstock,sorted(first.items()))
def rot(pair,n,back=False):
    for _ in range(n):pair=C(*pair,back)
    return pair
def D():
    st=stock(-3,0,0);ready=JI,add(JI,sc(2,O))
    initial=rot(ready,6,True)
    assert rot(initial,5)==initial and all(rot(initial,n)!=initial for n in range(1,5))
    g=(6,-2,12,1,0);mark=(5,-3,11,1,0)
    assert mark==add(g,sub(JI,O))
    old=[hist(seed(p0,st),6) for p0 in P]
    assert g==add(corr(old[1][1][6]),sc(2,O))
    base=None
    for q in range(6):
        label=str(q) if q<5 else 'static'
        d=rot(initial,q) if q<5 else (JI,JI)
        hh=[hist(seed(p0,st,d,g),160) for p0 in P]
        ac=hh[0][3];assert all(w[3]==ac for w in hh)
        if q==0:base=ac
        if q<5:assert ac==base
        print('D CONTROL',label,'D_INIT',pairraw(d),'ACCOUNT',acraw(ac),'Q',scalar(ac[2]))
        for k,w in enumerate(hh):
            cut,mid,tags,_=w
            hit=next(((t,y,tags[t][12+y],raw(port(cut[t])),raw(ref(cut[t]))) for t in range(1,161) for y in range(2) if tags[t][12+y]),None)
            print('D FIRST',label,k,hit)
        if q==0:
            for k,w in enumerate(hh):
                for t in range(1,6):
                    assert source(w[0][t])==source(old[k][0][t])
                    assert tuple(c[3] for c in w[0][t])==tuple(c[3] for c in old[k][0][t])
                    assert w[2][t][12:14]==(0,0)
                assert matter(w[1][6])==ready and corr(w[1][6])==corr(old[k][1][6])
                assert w[2][6][12:14]==(int(k==1),0)
        def correct(F,k):return port(F)==(mark if k==1 else g) and ref(F)==g
        active=all(correct(w[0][6],k) for k,w in enumerate(hh))
        print('D TARGET6',label,int(active))
        loss=None if active else (6,0)
        returns=[];held=[];split=None
        for t in range(1,161):
            negsame=len({words(hh[k],t) for k in (0,2,3,4)})==1
            if split is None and not negsame:split=t
            if t>6 and active:
                for s in (1,0):
                    if not all(correct(w[s][t],k) for k,w in enumerate(hh)):
                        active=False;loss=t,s;break
            if t%2==0 and all(source(w[0][t])==source(w[0][0]) for w in hh):
                returns.append(t)
                if t>=6 and active and len({words(w,t) for w in hh})==2 and negsame:held.append(t)
        print('D ENDPOINTS',label,'SOURCE_RETURNS',returns,'HELD_RETURNS',held,'FIRST_HOLD_LOSS',loss,'FIRST_NEGATIVE_SPLIT',split)
        for t in (6,16,30,100,110,111,160):
            print('D PARTITION',label,t,sorted(Counter(words(w,t) for w in hh).values()),'PORTS',tuple(raw(port(w[0][t])) for w in hh),'REFS',tuple(raw(ref(w[0][t])) for w in hh))
        if q==0:assert held==[16,30,44,58,72,86,100] and loss==(111,0) and scalar(ac[2])==2654
    print('DONE exact clock phase controls')
def C_failed():
    d=rot((JI,add(JI,sc(2,P[1]))),3,True)
    F=tuple(cell(d[y] if x==6 else Z,sc(2,O) if x==6 else Z,Z if y==0 else sc(2,O)) for x,y in product(range(8),range(2)))
    cut,mid,tags,ac=hist(F,12)
    first=next(t for t in range(1,13) if any(tags[t]))
    assert first==2
    print('C CLOCK_INITIAL',pairraw(d),'READY',pairraw(rot(d,3)),'FREE_PERIOD',5,'Q',scalar(ac[2]))
    print('C FIRST',first)
    for t in range(1,13):
        print('C TICK',t,'PRE',pairraw(matter(mid[t])),'POST',pairraw(matter(cut[t])),'TAGS',tags[t][12:14],'CLK',raw(port(cut[t])),'REF',raw(ref(cut[t])))
    print('C RESULT',0)
def E():
    phi=sc(-1,add(P[2],P[3]));w=add(sc(2,O),P[1]);D=add(w,P[1]);f=mul(J,D);g=sc(2,f)
    mark=add(g,mul(sub(JI,O),f))
    norms=tuple(h(add(w,p0)) for p0 in P)
    assert norms==tuple(add(sc(a,O),sc(b,phi)) for a,b in ((7,3),(4,4),(3,1),(4,-1),(2,3)))
    assert len(set(norms))==5 and all(v!=mul(mul(T,T),h(D)) for v in norms)
    print('E NORMS',pairraw(norms),'D',raw(D),'F',raw(f),'G',raw(g),'MARK',raw(mark))
    base=None
    for q in range(6):
        label=str(q) if q<5 else 'static'
        d=(add(w,P[2*q%5]),sub(w,P[2*q%5])) if q<5 else (D,D)
        F=tuple(cell(d[y] if x==6 else Z,g if x==6 else Z,Z if y==0 else g) for x,y in product(range(8),range(2)))
        cut,mid,tags,ac=hist(F,12)
        if q==0:base=ac
        if q<5:assert base==ac
        t0=next(t for t in range(1,13) if any(tags[t]))
        goal=(3-q-1)%5+1 if q<5 else 1
        assert t0==goal
        for t in range(1,goal+1):
            assert matter(mid[t])==((add(w,P[2*(q+t)%5]),sub(w,P[2*(q+t)%5])) if q<5 else (D,D))
            assert port(mid[t])==g and corr(mid[t])==Z and ref(mid[t])==mid[t][13][3]==g
            assert tags[t]==tuple(int(t==goal and i==12) for i in range(16))
        assert port(cut[goal])==mark and ref(cut[goal])==g
        change=next(((t,s) for t in range(goal+1,13) for s,F1 in ((1,mid[t]),(0,cut[t])) if port(F1)!=mark or ref(F1)!=g),None)
        print('E CASE',label,'D_INIT',pairraw(d),'ACCOUNT',acraw(ac),'Q',scalar(ac[2]),'FIRST',t0,'OUTPUT',raw(port(cut[t0])),'FIRST_CHANGE',change)
        for t in range(1,13):
            print('E TICK',label,t,'PRE',pairraw(matter(mid[t])),'TAGS',tags[t],'CLK',raw(port(cut[t])),'REF',raw(ref(cut[t])))
    print('E PASS five initial clock phases select five different first-write ticks; static ready t1')
if __name__=='__main__':
    A();C_failed();D();E()
