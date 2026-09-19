#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def I(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum((A[i][k]*v[k] for k in range(len(v))),F(0)) for i in range(len(A))]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def pw(A,n):
 R=I(len(A))
 while n:
  if n&1:R=mm(R,A)
  A=mm(A,A);n//=2
 return R
def rk(A):
 A=[r[:] for r in A];m=len(A);n=len(A[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];q=A[r][c];A[r]=[x/q for x in A[r]]
  for i in range(m):
   if i!=r and A[i][c]:
    q=A[i][c];A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
  r+=1
 return r
def c2(A):
 R=[[F(0) for _ in range(6)] for _ in range(6)]
 for b,(i,j) in enumerate(pairs):
  for a,(k,l) in enumerate(pairs):R[a][b]=A[k][i]*A[l][j]-A[l][i]*A[k][j]
 return R
def stack(X): return [r for A in X for r in A]
H=[[F(2 if i==j else 1) for j in range(4)] for i in range(4)]
C=[[F(x) for x in r] for r in [[-1,-1,-1,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]]
M=add(I(4),pw(C,2));L=c2(M)
G=[[F(0) for _ in range(6)] for _ in range(6)]
E=[[F(0) for _ in range(6)] for _ in range(6)]
for a,(i,j) in enumerate(pairs):
 for b,(k,l) in enumerate(pairs):
  G[a][b]=H[i][k]*H[j][l]-H[i][l]*H[j][k]
  z=(i,j,k,l)
  if len(set(z))==4:E[a][b]=F(-1 if sum(z[x]>z[y] for x in range(4) for y in range(x+1,4))%2 else 1)
K=mm(E,G);assert mm(K,K)==[[F(5*(i==j)) for j in range(6)] for i in range(6)]
# Work without sqrt(5): rows of 2P+ are sqrt5*I+K. Represent a+b sqrt5 as pairs.
def qadd(x,y):return(x[0]+y[0],x[1]+y[1])
def qmul(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qinv(x):
 d=x[0]*x[0]-5*x[1]*x[1];return(x[0]/d,-x[1]/d)
def qmm(A,B):return [[sum((qmul(A[i][k],B[k][j]) for k in range(len(B))), (F(0),F(0))) for j in range(len(B[0]))] for i in range(len(A))]
def qrk(A):
 A=[r[:] for r in A];m=len(A);n=len(A[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m) if A[i][c]!=(0,0)),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];u=qinv(A[r][c]);A[r]=[qmul(u,x) for x in A[r]]
  for i in range(m):
   if i!=r and A[i][c]!=(0,0):
    u=A[i][c];A[i]=[qadd(A[i][j],(-qmul(u,A[r][j])[0],-qmul(u,A[r][j])[1])) for j in range(n)]
  r+=1
 return r
QK=[[(x,F(i==j)) for j,x in enumerate(row)] for i,row in enumerate(K)]
QL=[[(x,F(0)) for x in row] for row in L]
def qpow(A,n):
 R=[[(F(i==j),F(0)) for j in range(len(A))] for i in range(len(A))]
 while n:
  if n&1:R=qmm(R,A)
  A=qmm(A,A);n//=2
 return R
assert qrk(QK)==3
obs=stack([qmm(QK,qpow(QL,n)) for n in range(6)])
assert qrk(obs)==4
# Cross rank is rank(P+ L P-) =1; use (sI+K)L(sI-K), scalar factors irrelevant.
QKm=[[(x[0],-x[1]) for x in row] for row in QK]
assert qrk(qmm(qmm(QK,QL),QKm))==1
print("P-J-HODGE-PREDICTIVE-CLOSURE-1")
print("Hodge rank: 3")
print("fixed-J observable rank: 4")
print("directed cross rank: 1")
print("ALL EXACT CHECKS PASS")
