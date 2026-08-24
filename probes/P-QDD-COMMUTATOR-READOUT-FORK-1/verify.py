#!/usr/bin/env python3
"""Exact audit for P-QDD-COMMUTATOR-READOUT-FORK-1."""
from fractions import Fraction as F
from itertools import product
BASE="9d06e5386d2481890eedcb13b0fe02ba1386da0b"; ISSUE=492; C=[]
def ck(s,x): C.append((s,bool(x)))
def M(r): return tuple(tuple(F(x) for x in q) for q in r)
def I(n): return M([[i==j for j in range(n)] for i in range(n)])
def Z(n): return M([[0]*n for _ in range(n)])
def T(A): return tuple(zip(*A))
def add(A,B): return M([[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))])
def sc(x,A): return M([[F(x)*y for y in r] for r in A])
def sub(A,B): return add(A,sc(-1,B))
def mul(A,B):
 BT=T(B); return M([[sum(x*y for x,y in zip(r,c)) for c in BT] for r in A])
def mv(A,v): return tuple(sum(x*y for x,y in zip(r,v)) for r in A)
def pw(A,n):
 R=I(len(A))
 for _ in range(n): R=mul(R,A)
 return R
def rk(A):
 a=[list(r) for r in A]; m=len(a); n=len(a[0]); k=0
 for j in range(n):
  p=next((i for i in range(k,m) if a[i][j]),None)
  if p is None: continue
  a[k],a[p]=a[p],a[k]; d=a[k][j]; a[k]=[x/d for x in a[k]]
  for i in range(m):
   if i!=k and a[i][j]: d=a[i][j]; a[i]=[a[i][q]-d*a[k][q] for q in range(n)]
  k+=1
 return k
def inv(A):
 n=len(A); a=[list(A[i])+[F(i==j) for j in range(n)] for i in range(n)]
 for j in range(n):
  p=next(i for i in range(j,n) if a[i][j]); a[j],a[p]=a[p],a[j]; d=a[j][j]; a[j]=[x/d for x in a[j]]
  for i in range(n):
   if i!=j and a[i][j]: d=a[i][j]; a[i]=[a[i][q]-d*a[j][q] for q in range(2*n)]
 return tuple(tuple(a[i][n:]) for i in range(n))
def det(A):
 a=[list(r) for r in A]; z=F(1); s=1
 for j in range(len(A)):
  p=next((i for i in range(j,len(A)) if a[i][j]),None)
  if p is None:return F(0)
  if p!=j:a[j],a[p]=a[p],a[j];s=-s
  d=a[j][j];z*=d
  for i in range(j+1,len(A)):
   if a[i][j]:q=a[i][j]/d;a[i]=[a[i][h]-q*a[j][h] for h in range(len(A))]
 return s*z
def out(v): return M([[x*y for y in v] for x in v])
I4=I(4); one=M([[1]*4]*4); G=sub(I4,sc(F(1,5),one)); Gi=add(I4,one)
MJ=M([[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]]); D=sub(MJ,I4); e=(F(1),0,0,0);u=mv(pw(D,2),e)
P=sc(F(1,4),out(u));Q=sub(I4,P); sharp=lambda A:mul(Gi,mul(T(A),G))
cols=((1,0,0,-1),(0,1,0,-1),(0,0,1,-1));B=T(cols); Bi=mul(inv(mul(T(B),B)),T(B));H=mul(T(B),mul(G,B));A=mul(Bi,mul(Q,mul(D,B)))
ck('C1 authority',BASE.startswith('9d06e538') and ISSUE==492)
ck('C2 motor metric',pw(D,5)==I4 and mul(T(D),mul(G,D))==G and mul(G,Gi)==I4)
ck('C3 projectors',u==(F(-1),)*4 and mul(P,P)==P and sharp(P)==P and rk(P)==1 and mul(Q,Q)==Q and sharp(Q)==Q and rk(Q)==3)
ck('C4 compressed motor',H==M([[2,1,1],[1,2,1],[1,1,2]]) and A==M([[-1,-1,F(-3,4)],[0,0,F(1,4)],[1,0,F(1,4)]]) and det(A)==F(-1,4) and sum(A[i][i] for i in range(3))==F(-3,4))
def X(a,b,c):return M([[c-5*a/4,-a-b/4,-3*a/4+b/4],[-b/4,c-a/4-b/2,a/4-b/4],[a,b,c]])
def E(a,b,c):return sub(mul(T(X(a,b,c)),mul(H,X(a,b,c))),H)
ck('C5 centralizer formula',all(mul(X(a,b,c),A)==mul(A,X(a,b,c)) for a,b,c in product((-2,-1,0,1,2),repeat=3)))
ck('C6 first elimination',all(E(a,b,c)[1][1]-E(a,b,c)[0][0]==F(5,4)*b*b for a,b,c in product((-2,-1,0,1,2),repeat=3)))
ck('C7 second elimination',all(E(a,0,c)[0][0]-E(a,0,c)[2][2]==a*(7*a-8*c)/4 and E(a,0,c)[0][1]-E(a,0,c)[0][2]==a*(a-4*c)/2 for a,c in product(range(-3,4),repeat=2)))
ck('C8 final elimination',all(E(0,0,c)[0][0]==2*(c*c-1) for c in range(-4,5)))
ck('C9 signs centralize',all(mul(T(X(0,0,c)),mul(H,X(0,0,c)))==H for c in (-1,1)))
grid=[v for v in product(range(-2,3),repeat=3) if any(v)]
ck('D1 quadratic sign fibres',all((out(v)==out(w))==(w==v or w==tuple(-x for x in v)) for v in grid for w in grid))
r=(F(1),0,0);hr=mv(H,r);O=sub(I(3),sc(F(2)/sum(r[i]*hr[i] for i in range(3)),M([[r[i]*hr[j] for j in range(3)] for i in range(3)])))
OA=mul(O,A);AO=mul(A,O);Xi=sub(OA,AO);W=((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1))
ck('D2 reflection noncentral',mul(T(O),mul(H,O))==H and Xi!=Z(3))
ck('D3 event blind',all(any(mv(OA,v)) and any(mv(AO,v)) for v in W))
ck('D4 quadratic detects',any(out(mv(OA,v))!=out(mv(AO,v)) for v in W))
Elo=sc(F(1,4),one);ck('T1 target last',P==Elo and Q==sub(I4,Elo))
f=0
for s,x in C:print(('PASS 'if x else'FAIL ')+s);f+=not x
print('CENTRALIZER signs_only')
print('EVENT_READOUT complete_for_event_partition blind_to_internal_commutators')
print('QUADRATIC_READOUT sign_complete faithful_to_nonzero_internal_commutators')
print('PUBLIC_BOUNDARY common_ordered_composition_domain_not_supplied')
print('DECISION EQUALITY-FORK')
print('SAMPLING NOT PROVIDED')
print('RESULT %d/%d PASS'%(len(C)-f,len(C)))
raise SystemExit(1 if f else 0)
