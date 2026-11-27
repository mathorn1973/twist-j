"""NON-CANONICAL result-exposed alternate exact ring/update audit, #2109.
Five cyclic coefficients; fraction-free rank tests on scaled integer matrices.
No import of the public verifier or first audit.
"""
from functools import cache
from itertools import product
from collections import Counter

def red(a):
    a=tuple(a)
    return tuple(x-a[4] for x in a[:4])+(0,)
def p(n):
    return red(int(k==n%5) for k in range(5))
def add(a,b):
    return red(x+y for x,y in zip(a,b))
def sc(k,a):
    return red(k*x for x in a)
def sub(a,b):
    return add(a,sc(-1,b))
@cache
def mul(a,b):
    return red(sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5))
Z=sc(0,p(0)); O=p(0); R=p(2); RI=p(3)
J=add(O,R); JI=sc(-1,add(p(1),p(2)))
JP={-1:JI,0:O,1:J}
def sig(a,k):
    return red(sum(a[i] for i in range(5) if i*k%5==j) for j in range(5))
@cache
def h(a):
    return mul(a,sig(a,4))
T=h(J)
def rsum(seq):
    return tuple(map(sum,zip(*seq)))
def scalar(H):
    n=4*H[0]-sum(H[1:])
    assert n%2==0
    return n//2

# Independent residue audit by determinant of a diagonal minus a cyclic shift.
hist=Counter()
for u in product(range(1,5),repeat=4):
    det=u[0]*u[1]*u[2]*u[3]-1
    # every consecutive 3-column minor contains an endpoint triangular minor
    for start in range(4):
        rows=[(start+i)%4 for i in range(3)]
        M=[[((u[j] if i==j else 0)-(1 if i==(j+1)%4 else 0))%5
            for j in rows] for i in rows]
        assert all(M[i][j]==0 for i in range(3) for j in range(i+1,3))
        assert all(M[i][i] for i in range(3))
    hist[4 if det%5 else 3]+=1
for es in product((-1,0,1),repeat=4):
    assert all(pow(2,e,5) in (1,2,3,4) for e in es)
print('A LOCAL_RESIDUE=PASS branch_assignments=81 accumulated_units=256 ranks='+str(sorted(hist.items())))

def eye(n,k=1):
    return tuple(tuple(sc(k,O) if i==j else Z for j in range(n)) for i in range(n))
def mm(A,B):
    return tuple(tuple(rsum(mul(x,y) for x,y in zip(row,col)) for col in zip(*B)) for row in A)
def minus(A,B):
    return tuple(tuple(sub(a,b) for a,b in zip(u,v)) for u,v in zip(A,B))
def diag(a):
    return tuple(tuple(v if i==j else Z for j in range(len(a))) for i,v in enumerate(a))
def rd(a,b):
    return tuple(sub(u,v) for u,v in zip(a,b))
@cache
def rank(A):
    A=[list(row) for row in A]
    n=len(A[0]); r=0
    for j in range(n):
        pos=next((i for i in range(r,len(A)) if A[i][j]!=Z),None)
        if pos is None:continue
        A[pos],A[r]=A[r],A[pos]
        v=A[r][j]
        for i in range(r+1,len(A)):
            u=A[i][j]
            if u!=Z:A[i]=[sub(mul(v,a),mul(u,b)) for a,b in zip(A[i],A[r])]
        r+=1
        if r==len(A):break
    return r
def nz(M,row,r):
    return rank(M+(row,))>r
# All single-step maps below are multiplied by two. They are integral.
aa=add(O,R); bb=sub(O,R); two=sc(2,O)
MC=((aa,bb),(bb,aa))
RC=((aa,Z,bb,Z),(Z,two,Z,Z),(bb,Z,aa,Z),(Z,Z,Z,two))
def RB(e):
    v=JP[-e];a=add(O,v);b=sub(O,v)
    return ((a,b),(b,a))
@cache
def B_rad(e):
    A,D=RB(e[0]),RB(e[1])
    return ((A[0][0],A[0][1],Z,Z),(A[1][0],A[1][1],Z,Z),
            (Z,Z,D[0][0],D[0][1]),(Z,Z,D[1][0],D[1][1]))
@cache
def sector(word,rad):
    c1,c2,e1,e2=word
    n=4 if rad else 2
    Id=eye(n)
    C1=(RC if rad else MC) if c1 else eye(n,2)
    C2=(RC if rad else MC) if c2 else eye(n,2)
    B1=B_rad(e1) if rad else diag(tuple(sc(2,JP[e]) for e in e1))
    B2=B_rad(e2) if rad else diag(tuple(sc(2,JP[e]) for e in e2))
    F1=mm(B1,C1); F2=mm(B2,C2)
    M=minus(mm(F2,F1),eye(n,16))
    r=rank(M); pre2=mm(C2,F1)
    if rad:
        active=all(nz(M,rd(P0[2*i],P0[2*i+1]),r)
                   for P0,e in ((C1,e1),(pre2,e2)) for i in range(2) if e[i])
        change=(c1 and nz(M,rd(Id[0],Id[2]),r)) or (c2 and nz(M,rd(F1[0],F1[2]),r))
    else:
        active=all(nz(M,P0[i],r) for P0,e in ((C1,e1),(pre2,e2))
                   for i in range(2) if e[i])
        change=(c1 and nz(M,rd(Id[0],Id[1]),r)) or (c2 and nz(M,rd(F1[0],F1[1]),r))
    return active,bool(change),n-r
es=tuple(product((-1,0,1),repeat=2));hist=Counter();survivors=[]
for m1,m2,g1,g2,e1,e2 in product((0,1),(0,1),(0,1),(0,1),es,es):
    ma,mc,md=sector((m1,m2,e1,e2),False)
    ra,rc,rdim=sector((g1,g2,e1,e2),True)
    if not ma:hist['zero_pre_d']+=1
    elif not ra:hist['zero_pre_f']+=1
    elif not (mc or rc):hist['C_idle']+=1
    else:
        hist['survivors']+=1
        survivors.append((m1,m2,g1,g2,e1,e2,md,rdim,mc,rc))
assert sum(hist.values())==1296
print('B WORDS',sorted(hist.items()))
print('B SURVIVORS',len(survivors))
for w in survivors:print('B WORD',w)

# Independent native full-field implementation in cell-major five-power basis.
def even(a):
    return not any(x%2 for x in a)
def half(a):
    assert even(a)
    return tuple(x//2 for x in a)
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
    d,f=half(sub(a,b)),half(sub(u,v))
    m,n=half(add(a,b)),half(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        D,F,k=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        D,F,k=mul(JI,d),mul(J,f),2
    else:return cell,0
    return (add(m,D),sub(m,D),add(n,F),sub(n,F)),k
NX,NY=8,4
ix=lambda x,y:x*NY+y
def transport(F,bit,back=False):
    G=[list(c) for c in F]; mv=[0,0]
    for x,y in product(range(NX),range(bit,NY,2)):
        i,k=ix(x,y),ix(x,(y+1)%NY)
        for r in range(3):
            u,v=C(F[i][r],F[k][r],back)
            G[i][r],G[k][r]=u,v
            mv[0]+=(u!=F[i][r] or v!=F[k][r])
    for x,y in product(range(bit,NX,2),range(NY)):
        i,k=ix(x,y),ix((x+1)%NX,y)
        u,v=C(F[i][3],F[k][3],back)
        G[i][3],G[k][3]=u,v
        mv[1]+=(u!=F[i][3] or v!=F[k][3])
    return tuple(tuple(c) for c in G),tuple(mv)
def collide(F):
    coll=tuple(B(c) for c in F)
    return tuple(c for c,t in coll),tuple(sum(t==k for c,t in coll) for k in (1,2))
def account(F):
    m=rsum(z for c in F for z in c[:2])
    f=rsum(z for c in F for z in c[2:])
    H=rsum(h(z) for c in F for z in c)
    return m,f,H,scalar(H)
def seed(b,kind,delta):
    F=[]
    for x,y in product(range(NX),range(NY)):
        d=sc((-1)**y,O);f=sc(2*(-1)**(x+b*y),J);g=Z
        if x==y==0:
            if kind==0:d=add(d,delta)
            else:g=delta;f=sub(f,delta)
        F.append((d,sc(-1,d),g,f))
    return tuple(F)
def shift(F,a):
    return tuple(F[ix((x-a)%NX,y)] for x,y in product(range(NX),range(NY)))
def step(F,bit,ac):
    G,mv=transport(F,bit)
    N,ts=collide(G)
    assert account(G)==account(N)==ac
    rev,_=collide(N)
    assert rev==G and transport(rev,bit,True)[0]==F
    return N,mv,ts
def check_witness(F0,b,kind,delta,s,a):
    F=F0;bit=0;ac=account(F)
    q=next(i for i,v in enumerate(delta) if v)
    bg=seed(b,kind,Z)
    for t in range(1,4*s+1):
        F,_,_=step(F,bit,ac);bit^=1
        if t%s==0:
            k=t//s
            assert F==shift(F0,k*a) and bit==0
            read=[F[ix(a*r%NX,0)][0 if kind==0 else 2][q]-bg[ix(a*r%NX,0)][0 if kind==0 else 2][q] for r in range(4)]
            assert read==[delta[q] if r==k%4 else 0 for r in range(4)]
    assert F==F0 and bit==0
deltas=sorted({sc(sign*m,mul(mul(p(l),JP[e]),sub(O,p(k))))
               for sign,m,l,e,k in product((-1,1),(1,2),range(5),(-1,0,1),range(1,5))}-{Z})
assert len(deltas)==80
print('C DELTAS',len(deltas),'PREPARATIONS',4*len(deltas),'STRIDES',128)
periods=Counter();wins=[];ticks=0;active_both=0
for b,kind in product(range(2),repeat=2):
    cat=Counter();cboth=0;cticks=0;cwins=0
    for i,delta in enumerate(deltas):
        F0=seed(b,kind,delta);F=F0;bit=0;ac=account(F)
        assert sum(delta)%5==0
        bg=seed(b,kind,Z)
        assert all(add(u[0],u[1])==add(v[0],v[1]) and add(u[2],u[3])==add(v[2],v[3]) for u,v in zip(F0,bg))
        assert len({shift(F0,2*k) for k in range(4)})==4
        targets={a:shift(F0,a) for a in (2,6)}
        moves=[0,0];tags=[0,0];period=0;matches=[]
        for t in range(1,257):
            F,c,ts=step(F,bit,ac);bit^=1;cticks+=1
            for k in range(2):moves[k]+=c[k];tags[k]+=ts[k]
            if bit==0:
                for a,target in targets.items():
                    if F==target:matches.append((t,a))
                if F==F0:period=t;break
        for t,a in matches:
            for s in (range(t,257,period) if period else (t,)):
                check_witness(F0,b,kind,delta,s,a)
                wins.append((b,kind,i,s,a));cwins+=1
        cat[period]+=1
        cboth+=int(all(moves))
        print('C CASE',b,kind,i,period,moves[0],moves[1],tags[0],tags[1],len(matches),ac[3])
    periods.update(cat);ticks+=cticks;active_both+=cboth
    print('C GROUP',b,kind,'PERIODS',sorted(cat.items()),'BOTH_AXES',cboth,'TICKS',cticks,'WINS',cwins)
print('C PERIODS',sorted(periods.items()))
print('C TICKS',ticks,'BOTH_AXES',active_both,'WINS',len(wins))
for w in wins:print('C WIN',w)
print('DONE exact native 2D census; period 0 means no return by 256')
