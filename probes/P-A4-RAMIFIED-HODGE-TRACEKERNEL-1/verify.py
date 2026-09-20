#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

P=5
pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def zeros(r,c): return [[0]*c for _ in range(r)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum(A[i][k]*v[k] for k in range(len(v))) for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def modA(A): return [[x%P for x in row] for row in A]
def modv(v): return [x%P for x in v]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))%P

def invp(a): return pow(a%P,-1,P)
def rankp(A):
    A=[[(x%P) for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        u=invp(A[r][c]); A[r]=[(u*x)%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[(A[i][j]-f*A[r][j])%P for j in range(n)]
        r+=1
        if r==m: break
    return r

def solvep(A,b):
    M=[[(x%P) for x in row]+[b[i]%P] for i,row in enumerate(A)]
    m=len(M); n=len(A[0]); r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        u=invp(M[r][c]); M[r]=[(u*x)%P for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]:
                f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%P for j in range(n+1)]
        piv.append(c); r+=1
    for row in M:
        if all(x%P==0 for x in row[:n]) and row[n]%P: raise AssertionError('inconsistent')
    x=[0]*n
    for i,c in enumerate(piv): x[c]=M[i][n]%P
    return x

def inv3(A):
    cols=[]
    for j in range(3):
        e=[int(i==j) for i in range(3)]
        cols.append(solvep(A,e))
    return [list(x) for x in zip(*cols)]

def compound2(A):
    out=zeros(6,6)
    for col,(i,j) in enumerate(pairs):
        for row,(k,l) in enumerate(pairs):
            out[row][col]=A[k][i]*A[l][j]-A[l][i]*A[k][j]
    return out

def wedge(a,b): return [(a[i]*b[j]-a[j]*b[i])%P for i,j in pairs]
def cross(a,b): return [
    (a[1]*b[2]-a[2]*b[1])%P,
    (a[2]*b[0]-a[0]*b[2])%P,
    (a[0]*b[1]-a[1]*b[0])%P]

def perm_comp(p,q): return tuple(p[q[i]] for i in range(5))
def group_closure(gens):
    ident=tuple(range(5)); G={ident}; todo=[ident]
    while todo:
        g=todo.pop()
        for h in gens:
            for z in (perm_comp(g,h),perm_comp(h,g)):
                if z not in G: G.add(z); todo.append(z)
    return G

def perm_A4(p):
    A=zeros(4,4)
    for col,j in enumerate(range(1,5)):
        if p[j]: A[p[j]-1][col]+=1
        if p[0]: A[p[0]-1][col]-=1
    return A

def qcoords(v):
    # quotient Vbar/<ell>, using e0,e1,e2 and killing the e3 coefficient.
    return [(v[i]-v[3])%P for i in range(3)]

def qaction(A):
    cols=[]
    for j in range(3):
        e=[0]*4; e[j]=1
        cols.append(qcoords(modv(mv(A,e))))
    return [list(x) for x in zip(*cols)]

def lincomb(cols,c):
    return [sum(cols[j][i]*c[j] for j in range(len(c)))%P for i in range(len(cols[0]))]

# Root Gram and integral scaled Hodge operator.
H=[[2 if i==j else 1 for j in range(4)] for i in range(4)]
G2=zeros(6,6)
for a,(i,j) in enumerate(pairs):
    for b,(k,l) in enumerate(pairs):
        G2[a][b]=H[i][k]*H[j][l]-H[i][l]*H[j][k]
W=zeros(6,6)
for a,pair1 in enumerate(pairs):
    for b,pair2 in enumerate(pairs):
        inds=pair1+pair2
        if len(set(inds))<4: continue
        inv=sum(inds[i]>inds[j] for i in range(4) for j in range(i+1,4))
        W[a][b]=-1 if inv%2 else 1
K=mm(W,G2)
assert mm(K,K)==[[5*int(i==j) for j in range(6)] for i in range(6)]
assert all(isinstance(x,int) for row in K for x in row)

# Ramified Hodge operator.
Kb=modA(K)
assert modA(mm(Kb,Kb))==zeros(6,6)
assert rankp(Kb)==3
ell=[1,1,1,1]
E=[wedge(ell,[int(i==j) for i in range(4)]) for j in range(4)]
E=[list(x) for x in zip(*E)]
assert rankp(E)==3
assert modA(mm(Kb,E))==zeros(6,4)
# im(E)=ker(Kb), and im(Kb)=ker(Kb) by rank and nilpotence.
assert rankp([row[:] for row in E])==6-rankp(Kb)
assert rankp([E[i]+Kb[i] for i in range(6)])==3

# Root Gram reduction gives the public trace-kernel carrier.
Hb=modA(H)
assert rankp(Hb)==3 and modv(mv(Hb,ell))==[0,0,0,0]
assert all(sum(Hb[i][j] for i in range(4))%P==0 for j in range(4))
# marked W5 difference basis and public residual Gram
Bmat=[[1,0,0],[4,1,0],[0,4,1],[0,0,4]]
Bpub=modA(mm(tr(Bmat),Bmat))
assert Bpub==[[2,4,0],[4,2,4],[0,4,2]]
Binv=inv3(Bpub)
assert Binv==[[2,3,4],[3,1,3],[4,3,2]]

# quotient basis q=(e0,e1,e2); Hbar maps it isomorphically to W5.
Q=[[1,0,0],[0,1,0],[0,0,1],[0,0,0]]
Tcols=[]
for j in range(3):
    y=modv(mv(Hb,[Q[i][j] for i in range(4)]))
    Tcols.append(solvep(Bmat,y))
T=[list(x) for x in zip(*Tcols)]
assert det3(T)!=0
Gq=modA(mm(mm(tr(Q),Hb),Q))
assert modA(mm(mm(tr(T),Bpub),T))==Gq
# Direct isometry identity H^2=H mod 5.
assert modA(mm(Hb,Hb))==Hb

# Kbar descends Lambda^2(Vbar/<ell>) -> Vbar/<ell>.
q_basis=[[1,0,0],[0,1,0],[0,0,1]]
std4=[[1,0,0,0],[0,1,0,0],[0,0,1,0]]
def bracket_q(x,y):
    vx=[x[0],x[1],x[2],0]; vy=[y[0],y[1],y[2],0]
    kw=modv(mv(Kb,wedge(vx,vy)))
    v=solvep(E,kw)
    return qcoords(v)

def beta_pub(x,y): return modv(mv(Binv,cross(x,y)))

def tmap(x): return modv(mv(T,x))

# Freeze orientation scalar: transported K-bracket = - public metric-volume bracket.
scalar=4
for a,b in ((1,2),(2,0),(0,1)):
    left=tmap(bracket_q(q_basis[a],q_basis[b]))
    right=[scalar*z%P for z in beta_pub(tmap(q_basis[a]),tmap(q_basis[b]))]
    assert left==right

# A5 equivariance on the marked quotient and transported W5 carrier.
pC=(1,2,3,4,0); pR=(1,2,0,3,4)
assert len(group_closure((pC,pR)))==60
for p in (pC,pR):
    A=modA(perm_A4(p)); Aq=qaction(A)
    # quotient bracket equivariance
    for i,j in ((0,1),(0,2),(1,2)):
        lhs=bracket_q(mv(Aq,q_basis[i]),mv(Aq,q_basis[j]))
        rhs=modv(mv(Aq,bracket_q(q_basis[i],q_basis[j])))
        assert lhs==rhs
    # transported action preserves public residual metric and has determinant 1
    Aw=modA(mm(mm(T,Aq),inv3(T)))
    assert modA(mm(mm(tr(Aw),Bpub),Aw))==Bpub
    assert det3(Aw)==1
    for i,j in ((0,1),(0,2),(1,2)):
        xi=tmap(q_basis[i]); xj=tmap(q_basis[j])
        lhs=beta_pub(mv(Aw,xi),mv(Aw,xj))
        rhs=modv(mv(Aw,beta_pub(xi,xj)))
        assert lhs==rhs

print('P-A4-RAMIFIED-HODGE-TRACEKERNEL-1 dry verifier')
print('integral scaled Hodge: K^2 = 5 I_6')
print('ramified Kbar: square zero, rank 3')
print('im Kbar = ker Kbar = ell wedge Vbar: PASS')
print('Vbar/<ell> -> W5 residual isometry: PASS')
print('transported bracket scalar versus public beta: -1')
print('A5 equivariance on generators: PASS')
print('ALL EXACT CHECKS PASS')
