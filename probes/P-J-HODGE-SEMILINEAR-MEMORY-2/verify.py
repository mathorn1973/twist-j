#!/usr/bin/env python3
from fractions import Fraction as F

class Q5:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        if isinstance(a,Q5): self.a,self.b=a.a,a.b; return
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
    def sigma(self): return Q5(self.a,-self.b)

def q5(x): return x if isinstance(x,Q5) else Q5(x)
S=Q5(0,1)
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def eye(n,field=F): return [[field(int(i==j)) for j in range(n)] for i in range(n)]
def zeros(r,c,field=F): return [[field(0) for _ in range(c)] for __ in range(r)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c): return [[c*x for x in row] for row in A]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),start=0)
             for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v):
    return [sum((A[i][k]*v[k] for k in range(len(v))),start=0) for i in range(len(A))]
def transpose(A): return [list(x) for x in zip(*A)]
def power(A,n):
    field=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    R=eye(len(A),field)
    while n:
        if n&1:R=mm(R,A)
        A=mm(A,A); n//=2
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
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        r+=1
    return r
def rref(A):
    A=[row[:] for row in A]; m=len(A); n=len(A[0]) if m else 0; r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]; iz=z.inv() if isinstance(z,Q5) else 1/z
        A[r]=[iz*x for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        piv.append(c); r+=1
    return A,piv
def solve(A,b):
    Aug=[list(row)+[b[i]] for i,row in enumerate(A)]
    R,piv=rref(Aug); n=len(A[0])
    for row in R:
        if all(not x for x in row[:n]) and row[n]: raise AssertionError("inconsistent")
    zero=Q5(0) if isinstance(A[0][0],Q5) else F(0)
    x=[zero for _ in range(n)]
    rr=0
    for c in piv:
        if c<n:
            x[c]=R[rr][n]; rr+=1
    return x
def inverse(A):
    n=len(A); cols=[]
    field=Q5 if isinstance(A[0][0],Q5) else F
    for j in range(n):
        e=[field(int(i==j)) for i in range(n)]
        cols.append(solve(A,e))
    return transpose(cols)
def colbasis(A):
    out=[]
    for j in range(len(A[0])):
        c=[A[i][j] for i in range(len(A))]
        T=transpose(out+[c])
        if rank(T)>len(out): out.append(c)
    return out
def compound2(A):
    field=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    R=zeros(6,6,field)
    for col,(i,j) in enumerate(PAIRS):
        for row,(k,l) in enumerate(PAIRS):
            R[row][col]=A[k][i]*A[l][j]-A[l][i]*A[k][j]
    return R
def sigma_matrix(A): return [[x.sigma() if isinstance(x,Q5) else x for x in row] for row in A]
def sigma_vec(v): return [x.sigma() if isinstance(x,Q5) else x for x in v]
def mat_from_cols(cs): return transpose(cs)
def sum_matrices(ms):
    out=zeros(len(ms[0]),len(ms[0][0]),F)
    for A in ms: out=add(out,A)
    return out
def row_times(row,A): return mm([row],A)[0]
def stack_rows(*As):
    out=[]
    for A in As: out.extend(A)
    return out
def coords(B,v): return solve(B,v)
def coord_matrix(B,Op,C):
    cols=[]
    for j in range(len(C[0])):
        v=[C[i][j] for i in range(len(C))]
        cols.append(coords(B,mv(Op,v)))
    return mat_from_cols(cols)
def apply_semilinear(A,B,x): return [u+v for u,v in zip(mv(A,x),mv(B,sigma_vec(x)))]

H=[[F(2 if i==j else 1) for j in range(4)] for i in range(4)]
C=[[-1,-1,-1,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
M=add(eye(4,int),power(C,2))
Acycle=compound2(C); L=compound2(M); G=compound2(H)
Wedge=zeros(6,6,F)
for a,p in enumerate(PAIRS):
    for b,q in enumerate(PAIRS):
        u=p+q
        if len(set(u))==4:
            inv=sum(u[i]>u[j] for i in range(4) for j in range(i+1,4))
            Wedge[a][b]=F(-1 if inv%2 else 1)
K=mm(Wedge,G)
assert mm(K,K)==scale(eye(6,F),F(5))
Kinv=scale(K,F(1,5)); Linv=inverse([[F(x) for x in r] for r in L])
T=scale(sum_matrices([power(Acycle,j) for j in range(5)]),F(1,5)); R=sub(eye(6,F),T)
assert mm(mm(mm(K,L),Kinv),T)==mm(Linv,T)
assert mm(sub(mm(K,L),mm(L,K)),R)==zeros(6,6,F)

IQ=eye(6,Q5); KQ=[[Q5(x) for x in row] for row in K]; LQ=[[Q5(x) for x in row] for row in L]
TQ=[[Q5(x) for x in row] for row in T]
Pp=add(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
Pm=sub(scale(IQ,Q5(F(1,2))),scale(KQ,Q5(0,F(1,10))))
assert sigma_matrix(Pp)==Pm
bp=colbasis(Pp); BP=mat_from_cols(bp); BM=sigma_matrix(BP)
assert rank(BP)==rank(BM)==3
assert rank([a+b for a,b in zip(BM,Pm)])==3
Aplus=coord_matrix(BP,mm(Pp,LQ),BP)
Bplus=coord_matrix(BP,mm(Pp,LQ),BM)
assert rank(Bplus)==1

qcols=[]; qbasis=[]
for j in range(3):
    e=[Q5(0) for _ in range(3)]; e[j]=Q5(1); qbasis.append(e)
    f=[Q5(0) for _ in range(3)]; f[j]=S; qbasis.append(f)
for x in qbasis:
    w=[u+v for u,v in zip(mv(BP,x),mv(BM,sigma_vec(x)))]
    assert all(z.b==0 for z in w)
    qcols.append([z.a for z in w])
    assert coords(BP,mv(Pp,w))==x
    assert coords(BP,mv(Pp,mv(LQ,w)))==apply_semilinear(Aplus,Bplus,x)
assert rank(mat_from_cols(qcols))==6

j=next(j for j in range(3) if any(Bplus[i][j] for i in range(3)))
e=[Q5(0) for _ in range(3)]; e[j]=Q5(1); se=[S*x for x in e]
assert apply_semilinear(Aplus,Bplus,se)!=[S*x for x in apply_semilinear(Aplus,Bplus,e)]

cross=mm(mm(Pm,LQ),Pp)
t=next(v for v in ([cross[i][j] for i in range(6)] for j in range(6)) if any(v))
E=mat_from_cols(bp+[t]); assert rank(E)==4
C4=coord_matrix(E,LQ,E); assert mm(E,C4)==mm(LQ,E)
O=[[Q5(int(i==j)) for j in range(4)] for i in range(3)]
assert rank(stack_rows(O,mm(O,C4)))==4

Tplus=coord_matrix(BP,TQ,BP); assert rank(Tplus)==1 and mm(Tplus,Tplus)==Tplus
qrow=next(row[:] for row in Tplus if any(row))
yrow=row_times(qrow,O)
poly=add(sub(power(C4,2),scale(C4,Q5(3))),eye(4,Q5))
assert row_times(yrow,poly)==[Q5(0) for _ in range(4)]
prev=row_times(yrow,inverse(C4))
assert rank(O+[prev])==4

v0=next([T[i][j] for i in range(6)] for j in range(6) if any(T[i][j] for i in range(6)))
hp=mv(Pp,[Q5(x) for x in v0]); hm=mv(Pm,[Q5(x) for x in v0])
H2=mat_from_cols([hp,hm]); assert rank(H2)==2
Boost=coord_matrix(H2,LQ,H2)
assert Boost[0][0]==Boost[1][1]==Q5(F(3,2))
b=Boost[0][1]; c=Boost[1][0]
assert b and c and b*c==Q5(F(5,4))
target=Q5(0,F(-1,2))
r=target/b
D=[[Q5(1),Q5(0)],[Q5(0),r]]
Dinv=inverse(D)
BoostN=mm(mm(Dinv,Boost),D)
assert BoostN==[[Q5(F(3,2)),target],[target,Q5(F(3,2))]]

print("P-J-HODGE-SEMILINEAR-MEMORY-2")
print("G1 Hodge twist / periodic commute: PASS")
print("G2 plus update: x' = A x + B sigma(x), rank(B)=1")
print("G3 update is Q-linear semilinear and not Q(sqrt5)-linear: PASS")
print("G4 fixed-J linear predictive dimensions: 3 -> 4")
print("G5 axial recurrence: y[n+2] = 3 y[n+1] - y[n]")
print("G6 present triple + one previous axial scalar rank: 4")
print("G7 boost diagonal / conjugate coupling: 3/2 ; sqrt5/2 magnitude")
print("G8 P_minus = sigma(P_plus): PASS")
print("G9 full A5/J minimum 6: inherited accepted boundary")
print("G10 native-U / physical-time claim: NONE")
print("VERDICT: PASS")
