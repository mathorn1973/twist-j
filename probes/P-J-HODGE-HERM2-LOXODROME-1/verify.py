#!/usr/bin/env python3
from fractions import Fraction as F

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
phi=Q5(F(1,2),F(1,2))

class Z5:
    __slots__=("c",)
    def __init__(self,c=(0,0,0,0)):
        if isinstance(c,(int,F)): c=(c,0,0,0)
        self.c=tuple(x if isinstance(x,F) else F(x) for x in c)
    def __add__(self,o):
        o=z5(o); return Z5(tuple(self.c[i]+o.c[i] for i in range(4)))
    __radd__=__add__
    def __neg__(self): return Z5(tuple(-x for x in self.c))
    def __sub__(self,o): return self+(-z5(o))
    def __rsub__(self,o): return z5(o)-self
    def __mul__(self,o):
        o=z5(o); a=[F(0)]*7
        for i,x in enumerate(self.c):
            for j,y in enumerate(o.c): a[i+j]+=x*y
        for k in range(6,3,-1):
            t=a[k]
            if t:
                for d in range(1,5): a[k-d]-=t
                a[k]=0
        return Z5(tuple(a[:4]))
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0: return self.inv()**(-n)
        r=Z5(1); b=self
        while n:
            if n&1: r=r*b
            b=b*b; n//=2
        return r
    def conj(self):
        j=Z5((0,1,0,0))
        return eval_poly(self.c,j**4)
    def inv(self):
        basis=[Z5((1,0,0,0)),Z5((0,1,0,0)),Z5((0,0,1,0)),Z5((0,0,0,1))]
        cols=[(self*e).c for e in basis]
        A=[list(row) for row in zip(*cols)]
        return Z5(tuple(solve(A,[F(1),F(0),F(0),F(0)])))
    def __truediv__(self,o): return self*z5(o).inv()
    def __eq__(self,o): return self.c==z5(o).c
    def __bool__(self): return any(self.c)

def z5(x): return x if isinstance(x,Z5) else Z5(x)
def eval_poly(cs,x):
    r=Z5(0)
    for c in reversed(cs): r=r*x+c
    return r

pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def eye(n,field=F): return [[field(int(i==j)) for j in range(n)] for i in range(n)]
def zeros(r,c,field=F): return [[field(0) for _ in range(c)] for __ in range(r)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c): return [[c*x for x in row] for row in A]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),start=0)
             for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v):
    return [sum((A[i][k]*v[k] for k in range(len(v))),start=0)
            for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def power(A,n):
    field=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    R=eye(len(A),field); B=A
    while n:
        if n&1: R=mm(R,B)
        B=mm(B,B); n//=2
    return R
def rank(A):
    A=[row[:] for row in A]; m=len(A); n=len(A[0]) if m else 0; r=0
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
def solve(A,b):
    A=[list(row)+[b[i]] for i,row in enumerate(A)]
    m=len(A); n=len(A[0])-1; r=0; pivs=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        piv=A[r][c]; inv=piv.inv() if hasattr(piv,"inv") else 1/piv
        A[r]=[inv*x for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n+1)]
        pivs.append(c); r+=1
    for row in A:
        if all(not x for x in row[:n]) and row[n]:
            raise AssertionError("inconsistent")
    z=Q5(0) if isinstance(A[0][0],Q5) else F(0)
    x=[z for _ in range(n)]
    for i,c in enumerate(pivs): x[c]=A[i][n]
    return x
def colbasis(A):
    cols=[[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    out=[]
    for c in cols:
        T=[list(x) for x in zip(*(out+[c]))]
        if rank(T)>len(out): out.append(c)
    return out
def compound2(A):
    field=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    out=zeros(6,6,field)
    for col,(i,j) in enumerate(pairs):
        for row,(k,l) in enumerate(pairs):
            out[row][col]=A[k][i]*A[l][j]-A[l][i]*A[k][j]
    return out

H=[[F(2 if i==j else 1) for j in range(4)] for i in range(4)]
C=[[-1,-1,-1,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
M=add(eye(4,int),power(C,2))
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
L=compound2(M)
IQ=eye(6,Q5)
KQ=[[Q5(x) for x in row] for row in K]
LQ=[[Q5(x) for x in row] for row in L]
WQ=[[Q5(x) for x in row] for row in W]
Pp=add(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
Pm=sub(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
bp=colbasis(Pp)
cross=mm(mm(Pm,LQ),Pp)
cross_cols=[[cross[i][j] for i in range(6)] for j in range(6)]
t=next(c for c in cross_cols if any(c))
Ecols=bp+[t]
E=[list(x) for x in zip(*Ecols)]
assert rank(E)==4

Acols=[]
for v in Ecols:
    Acols.append(solve(E,mv(LQ,v)))
A=[list(x) for x in zip(*Acols)]
assert mm(E,A)==mm(LQ,E)

B=mm(mm(tr(E),WQ),E)
Bp=mm(mm(tr([list(x) for x in zip(*bp)]),WQ),
      [list(x) for x in zip(*bp)])
targetBp=[[Q5(0,F(3,10) if i==j else F(1,10))
           for j in range(3)] for i in range(3)]
assert Bp==targetBp
assert all(B[i][3]==Q5(0) and B[3][i]==Q5(0) for i in range(3))
assert B[3][3]==Q5(F(-1,4),F(-1,8))
assert mm(mm(tr(A),B),A)==B

I=eye(4,Q5)
pboost=add(sub(power(A,2),scale(A,Q5(3))),I)
prot=add(sub(power(A,2),scale(A,phi)),I)
assert mm(pboost,prot)==zeros(4,4,Q5)
assert rank(pboost)==2 and rank(prot)==2
assert phi*phi+(Q5(1)/phi)*(Q5(1)/phi)==Q5(3)

j=Z5((0,1,0,0))
Phi=-(j**2+j**3)
J=Z5(1)+j**2
z10=-(j**3)
aH=-(J**-2)
assert Phi*Phi-Phi-Z5(1)==Z5(0)
assert z10**10==Z5(1) and z10**5==Z5(-1)
assert z10+z10**-1==Phi
assert aH==(Phi**2)*z10
assert aH*aH.conj()==Phi**4
assert Phi**2+Phi**-2==Z5(3)

print("P-J-HODGE-HERM2-LOXODROME-1 verifier")
print("predictive carrier dimension: 4")
print("beta restriction signature certificate: 3 + 1")
print("L preserves beta on E_J: PASS")
print("characteristic factors: X^2-3X+1 ; X^2-phi X+1")
print("a_H = -J^-2 = phi^2 zeta_10: PASS")
print("Herm2 modulus/phase factors match: PASS")
print("ALL EXACT CHECKS PASS")
