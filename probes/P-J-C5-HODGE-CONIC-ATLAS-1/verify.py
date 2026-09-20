#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

P=5

class Q5:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=a if isinstance(a,F) else F(a)
        self.b=b if isinstance(b,F) else F(b)
    def __add__(self,o):
        o=q5(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q5(o))
    def __rsub__(self,o): return q5(o)-self
    def __mul__(self,o):
        o=q5(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-5*self.b*self.b
        if not d: raise ZeroDivisionError
        return Q5(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q5(o).inv()
    def __eq__(self,o):
        o=q5(o); return self.a==o.a and self.b==o.b
    def __bool__(self): return bool(self.a or self.b)
    def __repr__(self): return f"Q5({self.a},{self.b})"

def q5(x): return x if isinstance(x,Q5) else Q5(x)
S=Q5(0,1)

pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def eye(n,field=F): return [[field(int(i==j)) for j in range(n)] for i in range(n)]
def zeros(r,c,field=F): return [[field(0) for _ in range(c)] for __ in range(r)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c): return [[c*x for x in row] for row in A]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),start=0) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum((A[i][k]*v[k] for k in range(len(v))),start=0) for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def power(A,n):
    field=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    R=eye(len(A),field); B=A
    while n:
        if n&1:R=mm(R,B)
        B=mm(B,B); n//=2
    return R
def rank(A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        piv=A[r][c]; inv=piv.inv() if isinstance(piv,Q5) else 1/piv
        A[r]=[inv*x for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        r+=1
    return r
def rref(A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0; pivs=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        piv=A[r][c]; inv=piv.inv() if isinstance(piv,Q5) else 1/piv
        A[r]=[inv*x for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        pivs.append(c); r+=1
    return A,pivs
def nullspace(A):
    R,pivs=rref(A); n=len(A[0]); free=[j for j in range(n) if j not in pivs]
    out=[]
    zero=Q5(0) if isinstance(A[0][0],Q5) else F(0)
    one=Q5(1) if isinstance(A[0][0],Q5) else F(1)
    for f in free:
        v=[zero for _ in range(n)]; v[f]=one
        for i,p in enumerate(pivs): v[p]=-R[i][f]
        out.append(v)
    return out
def solve(A,b):
    Aug=[list(row)+[b[i]] for i,row in enumerate(A)]
    R,pivs=rref(Aug)
    n=len(A[0])
    for row in R:
        if all(not x for x in row[:n]) and row[n]: raise AssertionError("inconsistent")
    zero=Q5(0) if isinstance(A[0][0],Q5) else F(0)
    x=[zero for _ in range(n)]
    for i,p in enumerate([p for p in pivs if p<n]): x[p]=R[i][n]
    return x
def colbasis(A):
    cols=[[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    out=[]
    for c in cols:
        if rank([list(x) for x in zip(*(out+[c]))])>len(out): out.append(c)
    return out
def compound2(A):
    field=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    out=zeros(6,6,field)
    for col,(i,j) in enumerate(pairs):
        for row,(k,l) in enumerate(pairs):
            out[row][col]=A[k][i]*A[l][j]-A[l][i]*A[k][j]
    return out

def perm_comp(p,q): return tuple(p[q[i]] for i in range(5))
def perm_inv(p):
    q=[0]*5
    for i,x in enumerate(p): q[x]=i
    return tuple(q)
def perm_pow(p,n):
    r=tuple(range(5))
    for _ in range(n): r=perm_comp(p,r)
    return r
def perm_order(p):
    r=tuple(range(5))
    for n in range(1,61):
        r=perm_comp(p,r)
        if r==tuple(range(5)): return n
    raise AssertionError
def group_closure(gens):
    ident=tuple(range(5)); G={ident}; todo=[ident]
    while todo:
        g=todo.pop()
        for h in gens:
            for z in (perm_comp(g,h),perm_comp(h,g)):
                if z not in G: G.add(z); todo.append(z)
    return G
def perm_A4(p):
    A=[[0]*4 for _ in range(4)]
    for col,j in enumerate(range(1,5)):
        if p[j]: A[p[j]-1][col]+=1
        if p[0]: A[p[0]-1][col]-=1
    return A

H=[[F(2 if i==j else 1) for j in range(4)] for i in range(4)]
G2=zeros(6,6,F)
for a,(i,j) in enumerate(pairs):
    for b,(k,l) in enumerate(pairs):
        G2[a][b]=H[i][k]*H[j][l]-H[i][l]*H[j][k]
W=zeros(6,6,F)
for a,p in enumerate(pairs):
    for b,q in enumerate(pairs):
        inds=p+q
        if len(set(inds))<4: continue
        inv=sum(inds[i]>inds[j] for i in range(4) for j in range(i+1,4))
        W[a][b]=F(-1 if inv%2 else 1)
K=mm(W,G2)
IQ=eye(6,Q5); KQ=[[Q5(x) for x in row] for row in K]
Pp=add(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
Pm=sub(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
bp=colbasis(Pp); bm=colbasis(Pm)
Bm=[list(x) for x in zip(*bm)]
WQ=[[Q5(x) for x in row] for row in W]
Gminus=scale(mm(mm(tr(Bm),WQ),Bm),Q5(-1))
targetG=[[Q5(0,F(3,10) if i==j else F(1,10)) for j in range(3)] for i in range(3)]
assert Gminus==targetG

def restrict(B,Op):
    cols=[]
    for j in range(len(B[0])):
        v=[B[i][j] for i in range(len(B))]
        cols.append(solve(B,mv(Op,v)))
    return [list(x) for x in zip(*cols)]

pC=(1,2,3,4,0); pR=(1,2,0,3,4)
A5=group_closure((pC,pR)); assert len(A5)==60
order5=sorted(p for p in A5 if perm_order(p)==5)
assert len(order5)==24
subgroups={}
for p in order5:
    E=frozenset(perm_pow(p,k) for k in range(5))
    subgroups.setdefault(E,sorted(x for x in E if x!=tuple(range(5)))[0])
assert len(subgroups)==6
subs=sorted(subgroups.items(),key=lambda kv:sorted(kv[0]))

real_lines={}
for E,gen in subs:
    R=restrict(Bm,[[Q5(x) for x in row] for row in compound2(perm_A4(gen))])
    ns=nullspace(sub(R,eye(3,Q5)))
    assert len(ns)==1
    real_lines[E]=ns[0]

for p in order5:
    E=frozenset(perm_pow(p,k) for k in range(5))
    A=perm_A4(p)
    Mc=add(eye(4,int),power(A,2))
    Lc=[[Q5(x) for x in row] for row in compound2(Mc)]
    cross=mm(mm(Pm,Lc),Pp)
    assert rank(cross)==1
    c=next(col for col in [[cross[i][j] for i in range(6)] for j in range(6)] if any(col))
    cc=solve(Bm,c)
    assert rank([real_lines[E],cc])==1

def dotG(u,v): return sum((u[i]*mv(Gminus,v)[i] for i in range(3)),start=Q5(0))
lines=[real_lines[E] for E,_ in subs]
for i in range(6):
    assert dotG(lines[i],lines[i])
    for j in range(i+1,6):
        x=dotG(lines[i],lines[j])
        assert x*x == Q5(F(1,5))*dotG(lines[i],lines[i])*dotG(lines[j],lines[j])
Sum=zeros(3,3,Q5)
for v in lines:
    gv=mv(Gminus,v); den=dotG(v,v)
    Pi=[[v[i]*gv[j]/den for j in range(3)] for i in range(3)]
    Sum=add(Sum,Pi)
assert Sum==scale(eye(3,Q5),Q5(2))

def conjugate(g,p): return perm_comp(perm_comp(g,p),perm_inv(g))
for E,_ in subs:
    N=[g for g in A5 if frozenset(conjugate(g,x) for x in E)==E]
    assert len(N)==10
baseE=subs[0][0]
orbit={frozenset(conjugate(g,x) for x in baseE) for g in A5}
assert orbit==set(E for E,_ in subs)

def invp(x): return pow(x%P,-1,P)
def mm5(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P for j in range(len(B[0]))] for i in range(len(A))]
def mv5(A,v): return [sum(A[i][k]*v[k] for k in range(len(v)))%P for i in range(len(A))]
def inv3mod(A):
    cols=[]
    for j in range(3):
        b=[int(i==j) for i in range(3)]
        M=[[(A[i][k]%P) for k in range(3)]+[b[i]] for i in range(3)]
        r=0
        for c in range(3):
            p=next(i for i in range(r,3) if M[i][c]%P)
            M[r],M[p]=M[p],M[r]
            u=invp(M[r][c]); M[r]=[(u*x)%P for x in M[r]]
            for i in range(3):
                if i!=r and M[i][c]%P:
                    f=M[i][c]%P; M[i]=[(M[i][k]-f*M[r][k])%P for k in range(4)]
            r+=1
        cols.append([M[i][3]%P for i in range(3)])
    return [list(x) for x in zip(*cols)]

Hb=[[int(H[i][j])%P for j in range(4)] for i in range(4)]
Bmat=[[1,0,0],[4,1,0],[0,4,1],[0,0,4]]
Bpub=mm5([list(x) for x in zip(*Bmat)],Bmat)
Btop=[row[:] for row in Bmat[:3]]
BtopInv=inv3mod(Btop)
Q=[[1,0,0],[0,1,0],[0,0,1],[0,0,0]]
T=mm5(BtopInv,mm5(Hb,Q)[:3])
Tinv=inv3mod(T)

def qcoords(v): return [(v[i]-v[3])%P for i in range(3)]
def qaction(A):
    cols=[]
    for j in range(3):
        e=[0,0,0,0]; e[j]=1
        cols.append(qcoords(mv5(A,e)))
    return [list(x) for x in zip(*cols)]
def line_norm(v):
    k=next(i for i,x in enumerate(v) if x%P)
    u=invp(v[k])
    return tuple((u*x)%P for x in v)
projective=sorted({line_norm(v) for v in product(range(P),repeat=3) if any(v)})
assert len(projective)==31
isotropic={v for v in projective if sum(v[i]*Bpub[i][j]*v[j] for i in range(3) for j in range(3))%P==0}
assert len(isotropic)==6

finite_lines={}
for E,gen in subs:
    A4=[[x%P for x in row] for row in perm_A4(gen)]
    Aq=qaction(A4)
    Aw=mm5(mm5(T,Aq),Tinv)
    fixed=[v for v in projective if mv5(Aw,list(v))==list(v)]
    assert len(fixed)==1
    finite_lines[E]=fixed[0]
assert len(set(finite_lines.values()))==6
assert set(finite_lines.values())==isotropic

print("P-J-C5-HODGE-CONIC-ATLAS-1 verifier")
print("Sylow-5 subgroups / real lines / finite lines: 6 6 6")
print("cross-image identity over all order-5 elements: 24/24")
print("real six-line squared angle: 1/5")
print("real tight-frame sum: 2 I_3")
print("normalizer order: 10")
print("finite fixed lines = complete W5 isotropic conic: PASS")
print("ALL EXACT CHECKS PASS")
