"""Non-canonical proof-led audit, issue #2102. Standard library only."""
from itertools import product
from collections import Counter

def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mm(A, B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def sub(A,B):
    return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]

def tr(A):
    return list(map(list,zip(*A)))

def mat(cols):
    return tr(cols)

def smith(A):
    A=[row[:] for row in A]
    m,n=len(A),len(A[0])
    out=[]
    for k in range(min(m,n)):
        pos=next(((i,j) for i in range(k,m) for j in range(k,n) if A[i][j]),None)
        if pos is None:
            break
        i,j=pos
        A[i],A[k]=A[k],A[i]
        for row in A:
            row[j],row[k]=row[k],row[j]
        while True:
            i=next((i for i in range(k+1,m) if A[i][k]),None)
            if i is not None:
                q=A[i][k]//A[k][k]
                A[i]=[x-q*y for x,y in zip(A[i],A[k])]
                if A[i][k]:
                    A[i],A[k]=A[k],A[i]
                continue
            j=next((j for j in range(k+1,n) if A[k][j]),None)
            if j is not None:
                q=A[k][j]//A[k][k]
                for row in A:
                    row[j]-=q*row[k]
                if A[k][j]:
                    for row in A:
                        row[j],row[k]=row[k],row[j]
                continue
            pos=next(((i,j) for i in range(k+1,m) for j in range(k+1,n) if A[i][j]%A[k][k]),None)
            if pos is None:
                break
            i,j=pos
            A[k]=[x+y for x,y in zip(A[k],A[i])]
        if A[k][k]<0:
            A[k]=[-x for x in A[k]]
        out.append(A[k][k])
    assert all(A[i][j]==(out[i] if i==j and i<len(out) else 0) for i in range(m) for j in range(n))
    assert all(b%a==0 for a,b in zip(out,out[1:]))
    return tuple(out)

def rank_mod(A,p):
    A=[[x%p for x in row] for row in A]
    r=0
    for j in range(len(A[0])):
        i=next((i for i in range(r,len(A)) if A[i][j]),None)
        if i is None:
            continue
        A[i],A[r]=A[r],A[i]
        u=pow(A[r][j],-1,p)
        A[r]=[u*x%p for x in A[r]]
        for k in range(r+1,len(A)):
            u=A[k][j]
            A[k]=[(x-u*y)%p for x,y in zip(A[k],A[r])]
        r+=1
    return r

G=[[5*int(i==j)-1 for j in range(4)] for i in range(4)]
assert smith(G)==(1,5,5,5)
assert rank_mod(G,5)==1
N=[[int(i==j)+1 for j in range(4)] for i in range(4)]
assert mm(G,N)==mm(N,G)==[[5*x for x in row] for row in eye(4)]
print("GRAM smith=1,5,5,5 rank_mod5=1")

basis=[b for b in range(16) if b.bit_count()==2]
idx={b:i for i,b in enumerate(basis)}
def sign(i,b):
    return (-1)**((b&((1<<i)-1)).bit_count())
def create(i,b):
    if not b&(1<<i):
        yield b|(1<<i),sign(i,b)
def annihilate(i,b,H):
    for k in range(4):
        if b&(1<<k) and H[i][k]:
            yield b^(1<<k),sign(k,b)*H[i][k]

def crossing(H):
    plus=[[0]*24 for _ in range(24)]
    minus=[[0]*24 for _ in range(24)]
    target=[[0]*24 for _ in range(24)]
    for i,j,b in product(range(4),range(4),basis):
        beta=idx[b]
        for mid,u in create(j,b):
            for a,v in annihilate(i,mid,H):
                plus[6*i+idx[a]][6*j+beta]+=u*v
        for mid,u in annihilate(i,b,H):
            for a,v in create(j,mid):
                minus[6*j+idx[a]][6*i+beta]+=u*v
        for alpha in range(6):
            expected=H[i][j]*int(alpha==beta)
            target[6*i+alpha][6*j+beta]=expected
            assert plus[6*i+alpha][6*j+beta]+minus[6*j+alpha][6*i+beta]==expected
    return plus,minus,target

for name,H,pred in (("SELF",G,(1,1,1,5)),("DUAL",eye(4),(1,1,1,1))):
    A,B,T=crossing(H)
    assert smith(A)==smith(B)==pred
    rank=sum(x%5!=0 for x in pred)
    assert rank_mod(A,5)==rank_mod(B,5)==rank
    assert smith(T)==((1,)*6+(5,)*18 if name=="SELF" else (1,)*24)
    assert rank_mod(T,5)==(6 if name=="SELF" else 24)
    print(name,"identity=576/576", "cut_smith="+",".join(map(str,pred)), "cut_rank_mod5="+str(rank), "target_rank_mod5="+str(rank_mod(T,5)))

def mv(A,x):
    return tuple(sum(a*b for a,b in zip(row,x)) for row in A)

fibres=Counter()
records=set()
for x in product(range(5),repeat=4):
    b=mv(G,x)
    low=tuple(t%5 for t in b)
    assert low==((-sum(x))%5,)*4
    fibres[low]+=1
    diffs=[]
    for i in range(3):
        q,r=divmod(b[i]-b[3],5)
        assert r==0
        diffs.append(q%5)
    x4=((-low[0]-sum(diffs))*4)%5
    recovered=tuple((d+x4)%5 for d in diffs)+(x4,)
    assert recovered==x
    records.add((low,tuple(diffs)))
    assert tuple((t//5)%5 for t in mv(N,tuple(t%25 for t in b)))==x
assert len(fibres)==5 and set(fibres.values())=={125} and len(records)==625
assert 5**2<125==5**3
print("READER fibres=5x125 reconstructed=625/625 added_digits_min=3")

# Ring in the marked basis (j,j^2,j^3,j^4), with 1=-j-j^2-j^3-j^4.
def canon(c):
    return tuple(c[k]-c[0] for k in range(1,5))
def jp(k):
    c=[0]*5
    c[k%5]=1
    return canon(c)
def add(x,y):
    return tuple(a+b for a,b in zip(x,y))
def neg(x):
    return tuple(-a for a in x)
def mul(x,y):
    c=[0]*5
    for i,a in enumerate(x,1):
        for j,b in enumerate(y,1):
            c[(i+j)%5]+=a*b
    return canon(c)
def gal(x,a):
    c=[0]*5
    for i,v in enumerate(x,1):
        c[(i*a)%5]+=v
    return canon(c)
one=jp(0)
J=add(one,jp(2))
u=add(jp(2),jp(3))
ui=neg(add(jp(1),jp(4)))
assert mul(u,ui)==one and gal(u,4)==u
Dcols=[]
for k in range(1,5):
    d=(0,)*4
    for t in range(k):
        d=add(d,neg(jp(k+t)))
    assert mul(add(one,neg(jp(1))),d)==add(jp(2*k),neg(jp(k)))
    Dcols.append(d)
D=mat(Dcols)
M=mat([mul(J,jp(k)) for k in range(1,5)])
K=sub(mm(M,D),mm(D,M))
assert K==mat([mul(u,jp(2*k)) for k in range(1,5)])
assert smith(K)==(1,)*4 and smith(D)==(1,1,1)
K2=mm(K,K)
assert K2==mat([neg(jp(4*k)) for k in range(1,5)])
assert mm(K2,K2)==eye(4)
Kv=mat([mul(ui,jp(2*k)) for k in range(1,5)])
assert smith(Kv)==(1,)*4 and mm(mm(tr(K),G),Kv)==G
def norm(x):
    return sum(a*b for a,b in zip(x,mv(G,x)))
assert norm(one)==4 and norm(mv(K,one))==6
print("COMMUTATOR D_rank=3 K_unimodular=YES K2=-conjugation K4=I paired_covariance=YES norms=4,6")
print("PASS: non-canonical L1 audit; no native readout or asymptotic claim")
