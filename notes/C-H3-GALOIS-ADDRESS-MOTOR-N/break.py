"""Result-exposed alternate five-power ring and rowwise full-state audit."""
from itertools import product
import hashlib
# Store five cyclic coefficients modulo the common vector (1,1,1,1,1).
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
def mul(a,b):
    return red(sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5))
def sig(a,k):
    return red(sum(a[i] for i in range(5) if i*k%5==j) for j in range(5))
def h(a):
    return mul(a,sig(a,4))
def q(a):
    b=h(a)
    return (4*b[0]-sum(b[1:]))//2
def m2(a):
    return tuple(x%2 for x in a[:4])
def div2(a):
    assert not any(x%2 for x in a)
    return red(x//2 for x in a)
Z=sc(0,p(0)); O=p(0)
R=p(2); J=add(O,R); JI=sc(-1,add(p(1),p(2)))
T=h(J); v=add(p(2),p(3)); phi=sc(-1,v)
w=add(sc(2,O),p(1)); c=add(O,p(1)); ci=sc(-1,mul(J,p(1)))
assert mul(c,ci)==O and mul(J,JI)==O
S=(Z,)+tuple(sc(s,p(k)) for s in (1,-1) for k in range(5))
A=tuple((sc(s,p(b)),sc(s,p(3*b))) for s in (1,-1) for b in range(5))
expect=((1,1),(4,0),(5,3),(4,5),(6,1),(7,3),(4,4),(3,1),(4,-1),(2,3))
assert tuple(h(sub(x,w)) for x in S[1:])==tuple(add(sc(a,O),sc(b,phi)) for a,b in expect)
assert h(w)==add(sc(3,O),sc(2,phi))
assert [x for x in S if h(sub(x,w))==h(c)]==[O]
assert not any(h(sub(x,w))==T for x in S)
assert m2(mul(add(O,p(4)),p(4))) not in {m2(p(i)) for i in range(5)}
def B(cell):
    a,b,u,v=cell
    if any(m2(sub(a,b))) or any(m2(sub(u,v))):
        return cell,0
    d,f=div2(sub(a,b)),div2(sub(u,v))
    m,n=div2(add(a,b)),div2(add(u,v))
    if d!=Z and h(f)==mul(T,h(d)):
        d,f,t=mul(J,d),mul(JI,f),1
    elif f!=Z and h(d)==mul(T,h(f)):
        d,f,t=mul(JI,d),mul(J,f),2
    else:
        return cell,0
    return (add(m,d),sub(m,d),add(n,f),sub(n,f)),t
def C(a,b,back=False):
    d=sub(a,b)
    if any(m2(d)):
        return a,b
    u=mul(p(3) if back else p(2),d)
    return div2(add(add(a,b),u)),div2(sub(add(a,b),u))
def cell(x,m,i):
    z,r=A[i]
    d=mul(m,mul(ci,sub(x,mul(r,w))))
    f=sc(-1,mul(J,mul(p(3),mul(m,z))))
    return d,sc(-1,d),Z,sc(-2,f)
def residues(m,i):
    vals={m2(B(cell(x,m,i))[0][0]) for x in S}
    assert len(vals)<=7
    return vals
def g(m1,i,m2_,j):
    banned=residues(m1,i)|residues(m2_,j)
    assert len(banned)<=14
    return next(tuple(a)+(0,) for a in product(range(2),repeat=4) if a not in banned)
g1=g(v,9,p(4),0)
g2=g(p(4),9,v,0)
def block(x,m):
    return tuple(cell(x,m,i) for i in range(10) for t in range(2))
def pad(g):
    return ((g,sc(-1,g),Z,Z),)*2
def rsum(a):
    t=Z
    for x in a:t=add(t,x)
    return t
def acct(rows):
    return (rsum(z for c in rows for z in c[:2]),rsum(z for c in rows for z in c[2:]),
            rsum(h(z) for c in rows for z in c),sum(q(z) for c in rows for z in c))
def idle(rows,bit,back=False):
    # All columns are identical, so horizontal CORR pair is equal.
    for i in range(bit,len(rows),2):
        j=(i+1)%len(rows)
        for k in range(3):
            assert C(rows[i][k],rows[j][k],back)==(rows[i][k],rows[j][k])
    for c in rows:
        assert C(c[3],c[3],back)==(c[3],c[3])
def audit(rows,blocks,Q):
    ac=acct(rows)
    assert ac[:2]==(Z,Z) and ac[3]*8==Q
    idle(rows,0)
    hit={start+2*i+r for start,x,m in blocks if x!=Z
         for i,(_,ref) in enumerate(A) if x==ref for r in range(2)}
    cells=tuple(B(c) for c in rows)
    N=tuple(c for c,t in cells)
    assert {i for i,(c,t) in enumerate(cells) if t==1}==hit
    assert all(t in (0,1) for c,t in cells)
    assert {i for i,c in enumerate(N) if c[2]!=Z}==hit
    assert acct(N)==ac
    out=[]
    for start,x,m in blocks:
        occupied=[(i,N[start+2*i][2]) for i in range(10) if N[start+2*i][2]!=Z]
        if x==Z:
            assert not occupied
            out.append((-1,Z))
        else:
            assert len(occupied)==1
            i,z=occupied[0]
            sign,k=divmod(S.index(x)-1,5)
            assert i==sign*5+2*k%5 and z==mul(m,sig(x,2))
            out.append((i,z))
    idle(N,1)
    back=tuple(B(c) for c in N)
    NN=tuple(c for c,t in back)
    assert NN==rows and {i for i,(c,t) in enumerate(back) if t==2}==hit
    assert all(t in (0,2) for c,t in back) and acct(NN)==ac
    idle(rows,0,True); idle(N,1,True)
    # Exact same canonical ordering as full field (column-major).
    F=tuple(z for a in range(8) for c in rows for z in c)
    F1=tuple(z for a in range(8) for c in N for z in c)
    F2=tuple(z for a in range(8) for c in NN for z in c)
    text=';'.join(','.join(map(str,z[:4])) for z in F+F1+F2)
    return tuple(out),8*len(hit),hashlib.sha256(text.encode()).hexdigest()
def line(label,ix,iy,outs,n,Q,digest):
    print(label,ix,iy,';'.join(str(a)+':'+','.join(map(str,z[:4])) for a,z in outs),
          n,Q,digest)
print('NORMS 11/11; B1 unique; B2 excluded; residue root set 5')
print('GUARDS',','.join(map(str,g1[:4])),','.join(map(str,g2[:4])),'Q',32*(q(g1)+q(g2)))
for ix,x in enumerate(S):
    Q=4160 if x==Z else 5120
    out,n,digest=audit(block(x,O),((0,x,O),),Q)
    line('A',ix,-1,out,n,Q,digest)
for (ix,x),(iy,y) in product(enumerate(S),repeat=2):
    Q=(3840 if x==Z else 4480)+(4160 if y==Z else 5120)+32*(q(g1)+q(g2))
    out,n,digest=audit(block(x,v)+pad(g1)+block(y,p(4))+pad(g2),
                       ((0,x,v),(22,y,p(4))),Q)
    assert mul(out[0][1],out[1][1])[3]==mul(x,y)[3]
    line('B',ix,iy,out,n,Q,digest)
print('PASS A=11/11 B=121/121 return=132/132 pairing=121/121')
