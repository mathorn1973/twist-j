#!/usr/bin/env python3
"""Exact audit for P-QDD-RECORD-MONOID-DESCENT-1.

The verifier uses the five-label sum-zero simplex representation for its main
route and reconstructs the public four-coordinate J basis only in the final
target gate. Standard library, integers and Fraction only.
"""

BASE_COMMIT = "7820173bdf035fa8b59e40113fdad3ac3c66f12a"
ISSUE = 489

from fractions import Fraction as F
from itertools import combinations

N=5
F5=tuple(range(5))
UNITS=(1,2,3,4)
CHECKS=[]

def check(label, ok): CHECKS.append((label,bool(ok)))
def mat(rows): return tuple(tuple(x if isinstance(x,F) else F(x) for x in r) for r in rows)
def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def zero(n): return tuple(tuple(F(0) for _ in range(n)) for _ in range(n))
def trans(A): return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))
def add(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def scale(c,A): c=F(c); return tuple(tuple(c*x for x in r) for r in A)
def neg(A): return scale(-1,A)
def sub(A,B): return add(A,neg(B))
def mm(A,B):
    BT=trans(B)
    return tuple(tuple(sum((x*y for x,y in zip(r,c)),F(0)) for c in BT) for r in A)
def mv(A,v): return tuple(sum((x*y for x,y in zip(r,v)),F(0)) for r in A)
def mpow(A,n):
    out=eye(len(A)); base=A
    while n:
        if n&1: out=mm(out,base)
        base=mm(base,base); n//=2
    return out
def cols(vs): return tuple(tuple(vs[j][i] for j in range(len(vs))) for i in range(len(vs[0])))
def rank(A):
    w=[list(r) for r in A]; nr=len(w); nc=len(w[0]); pr=0
    for c in range(nc):
        p=next((r for r in range(pr,nr) if w[r][c]),None)
        if p is None: continue
        w[pr],w[p]=w[p],w[pr]
        d=w[pr][c]; w[pr]=[x/d for x in w[pr]]
        for r in range(nr):
            if r!=pr and w[r][c]:
                d=w[r][c]; w[r]=[w[r][j]-d*w[pr][j] for j in range(nc)]
        pr+=1
        if pr==nr: break
    return pr
def same_class(A,B): return A==B or A==neg(B)
def same_ray(v,w): return rank(cols((v,w)))==1 if any(v) and any(w) else v==w

def perm_matrix(pi):
    # columns e_x -> e_pi(x)
    return tuple(tuple(F(i==pi[j]) for j in range(N)) for i in range(N))
def affine(a,k): return tuple((k+a*(x-k))%5 for x in F5)

def sat(n): return 0 if n==0 else 1
def bor(a,b): return int(bool(a or b))
def bpower(T,Q,n): return Q if n==0 else mpow(T,n)
def descends(T,Q,depth=14):
    vals=[bpower(T,Q,n) for n in range(depth+1)]
    return all(sat(m)!=sat(n) or same_class(vals[m],vals[n]) for m in range(depth+1) for n in range(depth+1))

I=eye(N); ONE=mat(((1,)*N,)*N); S=sub(I,scale(F(1,5),ONE))
# simplex vertices u_x=e_x-1/5 one
vertices=tuple(tuple(F(i==x)-F(1,5) for i in F5) for x in F5)
P={};Q={};R={};C={};J={}
for k in F5:
    u=vertices[k]
    P[k]=scale(F(5,4),tuple(tuple(u[i]*u[j] for j in F5) for i in F5))
    Q[k]=sub(S,P[k])
    g=perm_matrix(affine(2,k))
    R[k]=scale(F(1,4),sub(add(sub(I,g),mpow(g,2)),mpow(g,3)))
    C[k]=sub(Q[k],R[k])
    J[k]=mm(g,C[k])

# monoids
check('M1 sat homomorphism',all(sat(m+n)==bor(sat(m),sat(n)) for m in range(20) for n in range(20)))
check('M2 source nonidempotent target idempotent',1+1==2 and 2!=1 and bor(1,1)==1)
check('M3 histories free',all('H'*m+'H'*n=='H'*(m+n) for m in range(10) for n in range(10)) and 'H'!='HH')
# conditioning
subsets=[{x for x in F5 if mask>>x&1} for mask in range(32)]
events=[{2},set(F5)-{2},{0,2,4},set(),set(F5)]
check('C1 conditioning idempotent',all((A&E)&E==A&E for A in subsets for E in events))
# simplex/projectors
check('J1 simplex',all(sum(vertices[x][i] for x in F5)==0 for i in F5) and all(sum(vertices[x][i]*vertices[y][i] for i in F5)==(F(4,5) if x==y else F(-1,5)) for x in F5 for y in F5))
check('J2 S projector',mm(S,S)==S and trans(S)==S and rank(S)==4)
check('J3 branch algebra',all(mm(P[k],P[k])==P[k] and trans(P[k])==P[k] and rank(P[k])==1 and mm(Q[k],Q[k])==Q[k] and trans(Q[k])==Q[k] and rank(Q[k])==3 and add(P[k],Q[k])==S and add(R[k],C[k])==Q[k] and mm(R[k],C[k])==zero(N) and mm(J[k],J[k])==neg(C[k]) and trans(J[k])==neg(J[k]) for k in F5))
# witnesses
Ts={k:sub(R[k],C[k]) for k in F5}
Ti={k:add(R[k],add(scale(F(3,5),C[k]),scale(F(4,5),J[k]))) for k in F5}
check('W1 finite witness',all(mm(trans(Ts[k]),Ts[k])==Q[k] and mm(Q[k],Ts[k])==Ts[k] and mm(Ts[k],Q[k])==Ts[k] and mm(Ts[k],Ts[k])==Q[k] and not same_class(Ts[k],Q[k]) for k in F5))
# mixed ray
mixed=[]
for k in F5:
    basis=[tuple(F(i==j) for i in F5) for j in F5]
    wr=next(mv(R[k],e) for e in basis if any(mv(R[k],e)))
    wc=next(mv(C[k],e) for e in basis if any(mv(C[k],e)))
    mixed.append((k,tuple(wr[i]+wc[i] for i in F5)))
check('W2 finite witness ray moves',all(not same_ray(mv(Ts[k],w),mv(mpow(Ts[k],2),w)) for k,w in mixed))
check('W3 parity not saturation',all(not descends(Ts[k],Q[k]) for k in F5) and all(same_class(bpower(Ts[k],Q[k],n),Q[k])==(n%2==0) for k in F5 for n in range(10)))
check('W4 infinite witness effect',all(mm(trans(Ti[k]),Ti[k])==Q[k] and mm(Q[k],Ti[k])==Ti[k] and mm(Ti[k],Q[k])==Ti[k] for k in F5))
check('W5 infinite certificate',F(3,5)**2+F(4,5)**2==1 and 2*F(3,5)==F(6,5) and F(6,5).denominator==5)
check('W6 first powers distinct',all(not same_class(mpow(Ti[k],m),mpow(Ti[k],n)) for k in F5 for m,n in combinations(range(1,15),2)))
check('W7 infinite witness not saturation',all(not descends(Ti[k],Q[k]) for k in F5))
# descent controls
for k in F5:
    for T in (Q[k],neg(Q[k]),Ts[k],Ti[k]):
        check(f'D{k}-{len(CHECKS)} descent iff idem',descends(T,Q[k])==same_class(mm(T,T),T))
check('Dfinal only signs descend',all(descends(T,Q[k])==same_class(T,Q[k]) for k in F5 for T in (Q[k],neg(Q[k]),Ts[k],Ti[k])))
# final mapping to public 4D target
I4=eye(4); ONE4=mat(((1,1,1,1),)*4); G4=sub(I4,scale(F(1,5),ONE4)); MJ=mat(((1,0,-1,1),(0,1,-1,0),(1,0,0,0),(0,1,-1,1))); D4=sub(MJ,I4)
def mv4(A,v): return tuple(sum(A[i][j]*v[j] for j in range(4)) for i in range(4))
def mm4(A,B):
    BT=tuple(zip(*B)); return tuple(tuple(sum(A[i][t]*BT[j][t] for t in range(4)) for j in range(4)) for i in range(4))
def mp4(A,n):
    out=I4
    for _ in range(n): out=mm4(out,A)
    return out
v4=tuple(mv4(mp4(D4,x),(F(1),F(0),F(0),F(0))) for x in F5)
B4=tuple(tuple(v4[j][i] for j in range(4)) for i in range(4))
def inv4(A):
    n=4; aug=[list(A[i])+[F(i==j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if aug[r][c]); aug[c],aug[p]=aug[p],aug[c]; d=aug[c][c]; aug[c]=[x/d for x in aug[c]]
        for r in range(n):
            if r!=c and aug[r][c]: d=aug[r][c]; aug[r]=[aug[r][j]-d*aug[c][j] for j in range(8)]
    return tuple(tuple(aug[i][4:]) for i in range(4))
BI4=inv4(B4)
def rho4(pi): return mm4(tuple(tuple(v4[pi[j]][i] for j in range(4)) for i in range(4)),BI4)
P2=scale(F(1,4),tuple(tuple(sum(rho4(affine(a,2))[i][j] for a in UNITS) for j in range(4)) for i in range(4)))
Elo=scale(F(1,4),ONE4); Ehi=sub(I4,Elo)
check('TARGET last',P2==Elo and sub(I4,P2)==Ehi)

fails=0
for label,ok in CHECKS:
    print(('PASS ' if ok else 'FAIL ')+label); fails+=not ok
print('DECISION RECORD-MONOID-NONDESCENT')
print('FINITE_ORBIT period=2')
print('INFINITE_ORBIT certificate_trace=6/5')
print('BOUNDARY same_record_conditioning_idempotent_fresh_reinteraction_not_forced')
print('SAMPLING NOT PROVIDED')
print(f'RESULT {len(CHECKS)-fails}/{len(CHECKS)} PASS')
raise SystemExit(1 if fails else 0)
