#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

class Q5:
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0):
        self.a = a if isinstance(a,F) else F(a)
        self.b = b if isinstance(b,F) else F(b)
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
        if d==0: raise ZeroDivisionError
        return Q5(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q5(o).inv()
    def __eq__(self,o):
        o=q5(o); return self.a==o.a and self.b==o.b
    def __bool__(self): return bool(self.a or self.b)
    def __repr__(self): return f'Q5({self.a},{self.b})'

def q5(x): return x if isinstance(x,Q5) else Q5(x)
S=Q5(0,1)

pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def eye(n,field=F):
    return [[field(int(i==j)) for j in range(n)] for i in range(n)]
def zeros(r,c,field=F): return [[field(0) for _ in range(c)] for __ in range(r)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c): return [[c*x for x in row] for row in A]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), start=0) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum((A[i][k]*v[k] for k in range(len(v))),start=0) for i in range(len(A))]
def transpose(A): return [list(x) for x in zip(*A)]
def power(A,n):
    R=eye(len(A), type(A[0][0]) if type(A[0][0]) in (F,Q5) else F)
    # normalize identity field for int matrices
    if isinstance(A[0][0],int): R=eye(len(A),int)
    B=A
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
        inv = A[r][c].inv() if isinstance(A[r][c],Q5) else 1/A[r][c]
        A[r]=[inv*x for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def stack(ms):
    out=[]
    for M in ms: out.extend(M)
    return out

def compound2(A):
    out=zeros(6,6,type(A[0][0]) if type(A[0][0]) in (F,Q5) else int)
    for col,(i,j) in enumerate(pairs):
        for row,(k,l) in enumerate(pairs):
            out[row][col]=A[k][i]*A[l][j]-A[l][i]*A[k][j]
    return out

def det4(A):
    import itertools
    s=0
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=1
        for i in range(4): term*=A[i][p[i]]
        s += (-1 if inv%2 else 1)*term
    return s

def plucker(v): return v[0]*v[5]-v[1]*v[4]+v[2]*v[3]

def perm_comp(p,q): return tuple(p[q[i]] for i in range(5))
def perm_A4(p):
    A=[[0]*4 for _ in range(4)]
    for col,j in enumerate(range(1,5)):
        if p[j]: A[p[j]-1][col]+=1
        if p[0]: A[p[0]-1][col]-=1
    return A

def group_closure(gens):
    ident=tuple(range(5)); G={ident}; todo=[ident]
    while todo:
        g=todo.pop()
        for h in gens:
            for z in (perm_comp(g,h),perm_comp(h,g)):
                if z not in G: G.add(z); todo.append(z)
    return G

# Marked A4 root carrier.
H=[[F(2 if i==j else 1) for j in range(4)] for i in range(4)]
C=[[-1,-1,-1,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
I4=eye(4,int)
assert power(C,5)==I4
assert mm(mm(transpose(C),H),C)==H
M=add(I4,power(C,2))
assert det4(M)==1

# Explicit integral conjugacy to the public J-step in the ideal (1-j)O_K basis.
U=[[-1,-1,-1,-1],[0,-1,-1,-1],[0,0,-1,-1],[0,0,0,-1]]
MJ=[[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]]
assert det4(U)==1
assert mm(U,M)==mm(MJ,U)

# Wedge metric and scaled Hodge K=sqrt(5)*.
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
K=mm(W,G2)  # W^-1=W in this marked basis.
assert mm(K,K)==scale(eye(6,F),F(5))
L=compound2(M)

# Q(sqrt5) Hodge projectors.
IQ=eye(6,Q5)
KQ=[[Q5(x) for x in row] for row in K]
LQ=[[Q5(x) for x in row] for row in L]
Pp=add(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
Pm=sub(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
assert rank(Pp)==rank(Pm)==3
assert mm(Pp,Pp)==Pp and mm(Pm,Pm)==Pm and mm(Pp,Pm)==zeros(6,6,Q5)

# One scalar crosses each Hodge direction at one J-step.
r_pm=rank(mm(mm(Pp,LQ),Pm)); r_mp=rank(mm(mm(Pm,LQ),Pp))
assert (r_pm,r_mp)==(1,1)

# Fixed-J observability saturates at rank four.
obs_plus=stack([mm(Pp,power(LQ,n)) for n in range(6)])
obs_minus=stack([mm(Pm,power(LQ,n)) for n in range(6)])
assert rank(obs_plus)==rank(obs_minus)==4

# The L-invariant hull of either Hodge triple has dimension four.
def colspace_basis(A):
    cols=[[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    B=[]
    for c in cols:
        if rank(list(map(list,zip(*(B+[c])))))>len(B): B.append(c)
    return B
bp=colspace_basis(Pp); bm=colspace_basis(Pm)
hp=[]; hm=[]
for n in range(6):
    Ln=power(LQ,n)
    hp.extend(mv(Ln,v) for v in bp)
    hm.extend(mv(Ln,v) for v in bm)
assert rank(list(map(list,zip(*hp))))==4
assert rank(list(map(list,zip(*hm))))==4

# A5 is generated by the marked 5-cycle and 3-cycle; both preserve the Hodge split.
pC=(1,2,3,4,0); pR=(1,2,0,3,4)
A5=group_closure((pC,pR)); assert len(A5)==60
GC=compound2(perm_A4(pC)); GR=compound2(perm_A4(pR))
GCQ=[[Q5(x) for x in row] for row in GC]; GRQ=[[Q5(x) for x in row] for row in GR]
assert mm(KQ,GCQ)==mm(GCQ,KQ) and mm(KQ,GRQ)==mm(GRQ,KQ)

# Arbitrary interleaved A5/J future words have zero common invisible space.
gens=(LQ,GCQ,GRQ)
ops=[IQ]
rank_by_depth=[]
for depth in range(4):
    rr=rank(stack([mm(Pp,A) for A in ops])); rank_by_depth.append(rr)
    if depth<3:
        candidates=ops+[mm(g,A) for A in ops for g in gens]
        uniq=[]; seen=set()
        for A in candidates:
            key=tuple((x.a,x.b) for row in A for x in row)
            if key not in seen: seen.add(key); uniq.append(A)
        ops=uniq
assert rank_by_depth==[3,4,5,6]

# Decomposable witness: x=e12 and y=*x have the same present plus output but different next output.
x=[Q5(1),Q5(0),Q5(0),Q5(0),Q5(0),Q5(0)]
y=mv(scale(KQ,Q5(0,F(1,5))),x) # (sqrt5/5)Kx = *x
assert plucker(x)==0 and plucker(y)==0
assert mv(Pp,x)==mv(Pp,y)
assert mv(Pp,mv(LQ,x))!=mv(Pp,mv(LQ,y))

print('P-J-HODGE-PREDICTIVE-CLOSURE-1 dry verifier')
print('A4/J integral conjugacy: PASS')
print('Hodge dimensions: 3 + 3')
print('cross ranks: 1 1')
print('fixed-J observable ranks: 4 4')
print('A5/J word observable ranks depth 0..3: 3 4 5 6')
print('decomposable current-output collision: PASS')
print('ALL EXACT CHECKS PASS')
