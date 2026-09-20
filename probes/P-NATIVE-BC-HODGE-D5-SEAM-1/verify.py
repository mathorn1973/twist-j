#!/usr/bin/env python3
from itertools import product

P = 5
PAIRS = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def mod(x): return x % P
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def zeros(r,c): return [[0]*c for _ in range(r)]
def add(A,B): return [[(A[i][j]+B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[(A[i][j]-B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(r) for r in zip(*A)]
def power(A,n):
    R=eye(len(A))
    while n:
        if n&1: R=mm(R,A)
        A=mm(A,A); n//=2
    return R
def rank(A):
    A=[[x%P for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]%P),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        u=pow(A[r][c],-1,P); A[r]=[(u*x)%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%P:
                u=A[i][c]%P
                A[i]=[(A[i][j]-u*A[r][j])%P for j in range(n)]
        r+=1
        if r==m: break
    return r
def rref(A):
    A=[[x%P for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0; piv=[]
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]%P),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        u=pow(A[r][c],-1,P); A[r]=[(u*x)%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%P:
                u=A[i][c]%P
                A[i]=[(A[i][j]-u*A[r][j])%P for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    return A,piv
def nullspace(A):
    R,piv=rref(A); n=len(A[0]); free=[j for j in range(n) if j not in piv]
    out=[]
    for f in free:
        v=[0]*n; v[f]=1
        for i,c in enumerate(piv): v[c]=(-R[i][f])%P
        out.append(v)
    return out
def inverse(A):
    n=len(A); M=[[(A[i][j]%P) for j in range(n)]+eye(n)[i] for i in range(n)]
    R,piv=rref(M)
    if piv[:n] != list(range(n)): raise AssertionError("singular inverse")
    return [row[n:] for row in R]
def det_nonzero(A): return rank(A)==len(A)
def c2(A):
    out=zeros(6,6)
    for col,(i,j) in enumerate(PAIRS):
        for row,(k,l) in enumerate(PAIRS):
            out[row][col]=(A[k][i]*A[l][j]-A[k][j]*A[l][i])%P
    return out
def perm_A4(p):
    A=zeros(4,4)
    for col,j in enumerate(range(1,5)):
        if p[j]: A[p[j]-1][col]=(A[p[j]-1][col]+1)%P
        if p[0]: A[p[0]-1][col]=(A[p[0]-1][col]-1)%P
    return A
def flatten(A): return [x%P for row in A for x in row]
def matrix(v,n=6): return [v[i*n:(i+1)*n] for i in range(n)]
def pkey(A):
    v=flatten(A); k=next((i for i,x in enumerate(v) if x),None)
    if k is None: return tuple(v)
    u=pow(v[k],-1,P)
    return tuple((u*x)%P for x in v)
def projective_coeffs(d):
    for lead in range(d):
        for tail in product(range(P), repeat=d-lead-1):
            yield [0]*lead+[1]+list(tail)
def lincomb(basis,coeff):
    v=[0]*len(basis[0])
    for c,b in zip(coeff,basis):
        if c:
            v=[(x+c*y)%P for x,y in zip(v,b)]
    return matrix(v)
def order(A,limit=100):
    R=eye(len(A))
    for n in range(1,limit+1):
        R=mm(R,A)
        if R==eye(len(A)): return n
    return None
def intertwiner_basis(Bn,Cn,Tb,Tc):
    eq=[]
    for N,T in ((Bn,Tb),(Cn,Tc)):
        for i in range(6):
            for j in range(6):
                row=[0]*36
                for k in range(6):
                    row[i*6+k]=(row[i*6+k]+N[k][j])%P
                    row[k*6+j]=(row[k*6+j]-T[i][k])%P
                eq.append(row)
    return nullspace(eq)
def symmetric_form_space(gens):
    pairs=[(i,j) for i in range(6) for j in range(i,6)]
    basis=[]
    for a,b in pairs:
        Q=zeros(6,6); Q[a][b]=1; Q[b][a]=1
        if a==b: Q[a][b]=1
        basis.append(Q)
    eq=[]
    for G in gens:
        for i in range(6):
            for j in range(6):
                row=[]
                for Q in basis:
                    D=sub(mm(mm(tr(G),Q),G),Q)
                    row.append(D[i][j])
                eq.append(row)
    return nullspace(eq)
def jordan_ranks(U):
    N=sub(U,eye(6)); out=[]; X=eye(6)
    for k in range(1,6):
        X=mm(X,N); out.append(rank(X))
    return tuple(out)
def similitude_preserves(G,Q):
    H=mm(mm(tr(G),Q),G)
    return pkey(H)==pkey(Q)
def line_normalizes(G,N):
    H=mm(mm(G,N),inverse(G))
    return pkey(H)==pkey(N)

Bn=[
[0,0,4,0,0,0],
[0,0,0,4,0,0],
[4,0,0,0,0,0],
[0,4,0,0,0,0],
[0,0,0,0,4,0],
[0,0,0,0,0,4],
]
Cn=[
[0,0,4,0,0,0],
[0,0,0,4,0,1],
[4,0,0,0,0,0],
[0,4,0,0,0,4],
[0,0,0,0,4,0],
[0,0,0,0,0,4],
]
An=[
[0,1,0,0,0,0],
[1,0,0,0,0,0],
[0,0,0,1,0,0],
[0,0,1,0,0,0],
[0,0,0,0,1,0],
[0,0,0,0,0,1],
]
Dn=[[4*int(i==j)%P for j in range(6)] for i in range(6)]
En=[row[:] for row in Dn]
Pn=mm(Bn,Cn)

C4=[[4,4,4,4],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
sperm=(0,4,3,2,1)
R4=perm_A4(sperm)
Ah=c2(C4); Sh=c2(R4)

H4=[[2 if i==j else 1 for j in range(4)] for i in range(4)]
G2=c2(H4)
Beta=zeros(6,6)
for a,p in enumerate(PAIRS):
    for b,q in enumerate(PAIRS):
        inds=p+q
        if len(set(inds))==4:
            inv=sum(inds[i]>inds[j] for i in range(4) for j in range(i+1,4))
            Beta[a][b]=(-1 if inv%2 else 1)%P
Kbar=mm(Beta,G2)

assert power(Bn,2)==eye(6) and power(Cn,2)==eye(6)
assert order(Pn,10)==5
assert power(Sh,2)==eye(6) and order(Ah,10)==5
assert mm(mm(Sh,Ah),Sh)==inverse(Ah)
assert rank(Kbar)==3 and mm(Kbar,Kbar)==zeros(6,6)
assert rank(Beta)==6

native_jordan=jordan_ranks(Pn)
hodge_jordan=jordan_ranks(Ah)

orientations={}
all_K=set(); all_Q=set(); total_proj_inv=0
for eps in (1,-1):
    Ae=Ah if eps==1 else inverse(Ah)
    Tb=Sh; Tc=mm(Sh,Ae)
    assert power(Tc,2)==eye(6) and mm(Tb,Tc)==Ae
    basis=intertwiner_basis(Bn,Cn,Tb,Tc)
    inv_reps=[]
    for coeff in projective_coeffs(len(basis)):
        X=lincomb(basis,coeff)
        if det_nonzero(X): inv_reps.append(X)
    orientations[eps]=(len(basis),len(inv_reps))
    total_proj_inv += len(inv_reps)
    for X in inv_reps:
        Xi=inverse(X)
        N=mm(mm(Xi,Kbar),X)
        assert rank(N)==3 and mm(N,N)==zeros(6,6)
        Q=mm(mm(tr(X),Beta),X)
        assert rank(Q)==6
        all_K.add(pkey(N)); all_Q.add(pkey(Q))

form_dim=len(symmetric_form_space((Bn,Cn)))

K_unique=(len(all_K)==1)
Q_unique=(len(all_Q)==1)
K_ext=None; Q_ext=None
if K_unique:
    N=matrix(list(next(iter(all_K))))
    K_ext=all(line_normalizes(G,N) for G in (An,Dn,En))
if Q_unique:
    Qm=matrix(list(next(iter(all_Q))))
    Q_ext=all(similitude_preserves(G,Qm) for G in (An,Dn,En))

seam=total_proj_inv>0
print("P-NATIVE-BC-HODGE-D5-SEAM-1")
print("native product order / target cycle order: %d %d" % (order(Pn,10),order(Ah,10)))
print("Jordan ranks native: "+" ".join(map(str,native_jordan)))
print("Jordan ranks Hodge: "+" ".join(map(str,hodge_jordan)))
for eps in (1,-1):
    d,n=orientations[eps]
    print("orientation %+d intertwiner_dim / projective_invertible: %d %d" % (eps,d,n))
print("D5 seam verdict: "+("SEAM" if seam else "DIFFER"))
print("transported K projective lines: %d" % len(all_K))
print("transported beta projective lines: %d" % len(all_Q))
print("native D5 invariant symmetric-form dimension: %d" % form_dim)
print("K-line canonical: "+("YES" if K_unique else "NO"))
print("beta-line canonical: "+("YES" if Q_unique else "NO"))
print("remaining generators normalize K-line: "+("YES" if K_ext is True else "NO" if K_ext is False else "NA"))
print("remaining generators preserve beta-line as similitudes: "+("YES" if Q_ext is True else "NO" if Q_ext is False else "NA"))
if seam:
    if K_unique and Q_unique and K_ext and Q_ext:
        print("linear extension verdict: FULL-LINEAR-SEAM")
    elif K_unique and Q_unique:
        print("linear extension verdict: D5-ONLY")
    else:
        print("linear extension verdict: NONCANONICAL-D5-SEAM")
else:
    print("linear extension verdict: DIFFER")
print("FIRED-COMMUTATOR-NOGO boundary: unchanged")
print("VERDICT: COMPLETE")
