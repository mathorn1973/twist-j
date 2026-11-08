#!/usr/bin/env python3
"""Exact finite audit of the explicitly selected seam-readout comparison."""
from fractions import Fraction as F
from itertools import combinations

N = 9
G = [[F(0) for _ in range(N)] for _ in range(N)]
G[0][0] = F(1)
for i in range(1,5):
    for j in range(1,5):
        G[i][j] = F(5*(i == j)-1)
for i in range(5,9):
    G[i][i] = F(4)

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))
def mv(A,x):
    return [dot(row,x) for row in A]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return sum((A[i][i] for i in range(len(A))),F(0))
def transpose(A):
    return [list(r) for r in zip(*A)]
def basis(i):
    return [F(int(i==j)) for j in range(N)]
def norm(y):
    return dot(y,mv(G,y))
def pure(y):
    gy=mv(G,y); q=norm(y)
    assert q>0
    return [[y[i]*gy[j]/q for j in range(N)] for i in range(N)]
def lincomb(A,B,t):
    return [[t*A[i][j]+(1-t)*B[i][j] for j in range(N)] for i in range(N)]

vectors = [basis(i) for i in range(N)]
labels = [(i,) for i in range(N)]
for i,j in combinations(range(N),2):
    vectors.append([F(int(k in (i,j))) for k in range(N)])
    labels.append((i,j))
assert len(vectors)==45
projectors=[]
for v in vectors:
    P=pure(v)
    assert mm(P,P)==P and transpose(mm(G,P))==mm(G,P) and tr(P)==1
    assert norm(v) in (1,4,5,6,8)
    projectors.append(P)

def response(z):
    y=[F(1)]+list(map(F,z)); gy=mv(G,y); a=norm(y)
    return [dot(v,gy)**2/(norm(v)*a) for v in vectors]
def reconstruct(p):
    p0=p[0]
    dual=[]
    for i in range(1,9):
        pij=p[labels.index((0,i))]
        dual.append(((1+G[i][i])*pij-p0-G[i][i]*p[i])/(2*p0))
    sg=sum(dual[:4],F(0))
    return [(x+sg)/5 for x in dual[:4]]+[x/4 for x in dual[4:]]
def q(z):
    return norm([F(0)]+list(map(F,z)))
def in_S(z):
    return (z[5]-z[6]-z[7])%3==0
ELL=(1,10,18,16,-1,-27,-32,-3)
def in_R(z):
    return in_S(z) and sum(a*b for a,b in zip(ELL,z))%41==0

BM=((1,1,0,-5),(0,1,2,0),(0,1,3,5),(0,0,2,7))
def source_from_power(z):
    a=z[:4]; b=z[4:]
    return tuple(a)+tuple(sum(BM[i][j]*b[j] for j in range(4)) for i in range(4))
controls=set()
for i in range(8):
    for sign in (-1,1):
        p=[0]*8; p[i]=sign; controls.add(source_from_power(p))
for i,j in combinations(range(8),2):
    for si in (-1,1):
        for sj in (-1,1):
            p=[0]*8; p[i]=si; p[j]=sj; controls.add(source_from_power(p))
V=(1,0,0,0,-1,0,0,0)
assert q(V)==8 and not in_R(V)
for t in (40,41,42,-40,-41,-42):
    controls.add(tuple(t*a for a in V))
controls=sorted(controls)
profiles=[]
for z in controls:
    assert in_S(z)
    assert q(z)>=sum(x*x for x in z)>0
    p=response(z)
    assert all(F(0)<=x<=F(1) for x in p)
    assert reconstruct(p)==list(map(F,z))
    assert F(1)/p[0]-1==q(z)
    profiles.append(p)
checks=0
for i,j in combinations(range(len(controls)),2):
    z,w=controls[i],controls[j]
    delta=max(abs(a-b) for a,b in zip(profiles[i],profiles[j]))
    Q=max(q(z),q(w))
    assert delta>=F(1,72*(Q+1))
    yz=[F(1)]+list(map(F,z)); yw=[F(1)]+list(map(F,w))
    A=norm(yz); B=norm(yw); c=dot(yz,mv(G,yw))
    D2=1-c*c/(A*B)
    assert D2>=F(1,(Q+1)**2)
    assert delta*delta<=D2
    checks+=1

def sigma(t):
    z=tuple(t*x for x in V)
    return lincomb(pure([F(1)]+list(map(F,z))),pure([F(1)]+[-F(x) for x in z]),F(1,2))
f40=F(1,1+8*40**2); f41=F(1,1+8*41**2); f42=F(1,1+8*42**2)
lam=(f41-f42)/(f40-f42)
assert lam==F(354161,735212) and F(0)<lam<F(1)
assert sigma(41)==lincomb(sigma(40),sigma(42),lam)
assert in_R(tuple(41*x for x in V))
assert all(not in_R(tuple(t*x for x in V)) for t in (40,-40,42,-42))
assert q(tuple(42*x for x in V))==14112
for n in range(1,26):
    a=41*n; b=a+1; Q=8*b*b
    r=tuple(a*x for x in V); s=tuple(b*x for x in V)
    assert in_R(r) and not in_R(s)
    D2=F(8,(1+8*a*a)*(1+8*b*b))
    assert D2<F(9,Q*Q)
    delta=max(abs(u-v) for u,v in zip(response(r),response(s)))
    assert F(1,72*(Q+1))<=delta and delta*delta<=D2
    assert 8*(41*(n+1)+1)**2<4*Q

print('C-JM-SEAM-READOUT-COST-N exact finite audit')
print('STATUS NON-CANONICAL L1 candidate-C; universal claims require PROOF.md')
print('EFFECTS 45 binary projectors; denominator set 1,4,5,6,8')
print('SOURCE_CONTROLS',len(controls))
print('PAIR_CONTROLS',checks)
print('EXACT_RECONSTRUCTION PASS')
print('PAIR_LOWER_BOUND 1/[72(Q+1)] PASS on declared finite controls')
print('ALL_EFFECT_UPPER_CONTROL 25 adjacent-multiple pairs PASS')
print('MIXTURE_LAMBDA',str(lam))
print('MIXTURE_OTHER_WEIGHT',str(1-lam))
print('MIXTURE_IDENTICAL_DENSITY PASS; Q=14112')
print('PHYSICAL_PREPARATION OCCURRENCE NATIVE_CONTACT NOT_PROVIDED')
print('PASS')
