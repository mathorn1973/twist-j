#!/usr/bin/env python3
P=5
pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v):return [sum(A[i][k]*v[k] for k in range(len(v))) for i in range(len(A))]
def mod(A):return [[x%P for x in r] for r in A]
def rk(A):
 A=mod(A);m=len(A);n=len(A[0]);r=0
 for c in range(n):
  q=next((i for i in range(r,m) if A[i][c]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];u=pow(A[r][c],-1,P);A[r]=[(u*x)%P for x in A[r]]
  for i in range(m):
   if i!=r and A[i][c]:
    u=A[i][c];A[i]=[(A[i][j]-u*A[r][j])%P for j in range(n)]
  r+=1
 return r
def wedge(a,b):return [(a[i]*b[j]-a[j]*b[i])%P for i,j in pairs]
H=[[2 if i==j else 1 for j in range(4)] for i in range(4)]
G=[[0]*6 for _ in range(6)]
E=[[0]*6 for _ in range(6)]
for a,(i,j) in enumerate(pairs):
 for b,(k,l) in enumerate(pairs):
  G[a][b]=H[i][k]*H[j][l]-H[i][l]*H[j][k]
  z=(i,j,k,l)
  if len(set(z))==4:E[a][b]=-1 if sum(z[x]>z[y] for x in range(4) for y in range(x+1,4))%2 else 1
K=mm(E,G)
assert mm(K,K)==[[5*int(i==j) for j in range(6)] for i in range(6)]
Kb=mod(K);assert mod(mm(Kb,Kb))==[[0]*6 for _ in range(6)] and rk(Kb)==3
ell=[1,1,1,1]
S=[wedge(ell,[int(i==j) for i in range(4)]) for j in range(4)]
S=[list(x) for x in zip(*S)]
assert rk(S)==3 and mod(mm(Kb,S))==[[0]*4 for _ in range(6)]
assert rk([S[i]+Kb[i] for i in range(6)])==3
Hb=mod(H)
assert rk(Hb)==3 and [x%P for x in mv(Hb,ell)]==[0]*4
assert all(sum(Hb[i][j] for i in range(4))%P==0 for j in range(4))
assert mod(mm(Hb,Hb))==Hb
B=[[1,0,0],[4,1,0],[0,4,1],[0,0,4]]
Bt=[list(x) for x in zip(*B)]
Bpub=mod(mm(Bt,B))
assert Bpub==[[2,4,0],[4,2,4],[0,4,2]]
print("P-A4-RAMIFIED-HODGE-TRACEKERNEL-1")
print("K^2 = 5 I_6: PASS")
print("Kbar^2 = 0, rank Kbar = 3: PASS")
print("im Kbar = ker Kbar = ell wedge Vbar: PASS")
print("Hbar quotient to W5 carrier: PASS")
print("public residual Gram reconstructed: PASS")
print("ALL EXACT CHECKS PASS")
