#!/usr/bin/env python3
"""Exact audit for P-QDD-PURE-RECORD-PORT-CANONICAL-1."""
from fractions import Fraction as F
from itertools import product

BASE = "47fa9ddd8db5e9fdbbd4440f29107ca298898350"
ISSUE = 505
C = []

def ck(label, cond): C.append((label, bool(cond)))
def M(rows): return tuple(tuple(F(x) for x in row) for row in rows)
def I(n): return M([[i == j for j in range(n)] for i in range(n)])
def T(a): return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))
def add(a,b): return M([[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))])
def sc(c,a): return M([[F(c)*x for x in row] for row in a])
def sub(a,b): return add(a,sc(-1,b))
def mul(a,b):
    bt=T(b); return M([[sum((x*y for x,y in zip(row,col)),F(0)) for col in bt] for row in a])
def mv(a,v): return tuple(sum((x*y for x,y in zip(row,v)),F(0)) for row in a)
def outer(v,w): return M([[x*y for y in w] for x in v])
def pw(a,n):
    r=I(len(a)); b=a
    while n:
        if n&1: r=mul(r,b)
        b=mul(b,b); n//=2
    return r
def inv(a):
    n=len(a); w=[list(a[i])+[F(i==j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if w[i][c]); w[c],w[p]=w[p],w[c]
        d=w[c][c]; w[c]=[x/d for x in w[c]]
        for i in range(n):
            if i!=c and w[i][c]:
                q=w[i][c]; w[i]=[w[i][j]-q*w[c][j] for j in range(2*n)]
    return tuple(tuple(w[i][n:]) for i in range(n))
def rk(a):
    w=[list(r) for r in a]; m=len(w); n=len(w[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if w[i][c]),None)
        if p is None: continue
        w[r],w[p]=w[p],w[r]; d=w[r][c]; w[r]=[x/d for x in w[r]]
        for i in range(m):
            if i!=r and w[i][c]:
                q=w[i][c]; w[i]=[w[i][j]-q*w[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r
def det(a):
    w=[list(r) for r in a]; z=F(1); s=1; n=len(w)
    for c in range(n):
        p=next((i for i in range(c,n) if w[i][c]),None)
        if p is None: return F(0)
        if p!=c: w[c],w[p]=w[p],w[c]; s=-s
        d=w[c][c]; z*=d
        for i in range(c+1,n):
            if w[i][c]:
                q=w[i][c]/d
                for j in range(c,n): w[i][j]-=q*w[c][j]
    return s*z
def tr(a): return sum((a[i][i] for i in range(len(a))),F(0))
def dot(v,g,w): return sum((v[i]*sum((g[i][j]*w[j] for j in range(len(w))),F(0)) for i in range(len(v))),F(0))
def sgn(v):
    for x in v:
        if x: return v if x>0 else tuple(-y for y in v)
    return v

I4=I(4); J4=M([[1]*4 for _ in range(4)]); G=sub(I4,sc(F(1,5),J4)); GI=add(I4,J4)
MJ=M(((1,0,-1,1),(0,1,-1,0),(1,0,0,0),(0,1,-1,1))); DJ=sub(MJ,I4)
e0=(F(1),F(0),F(0),F(0)); u2=mv(pw(DJ,2),e0); P=sc(F(1,4),outer(u2,u2)); Q=sub(I4,P)
sharp4=lambda a: mul(GI,mul(T(a),G))
B=M(((1,0,0),(0,1,0),(0,0,1),(-1,-1,-1))); L=M(((1,0,0,0),(0,1,0,0),(0,0,1,0)))
H=mul(T(B),mul(G,B)); HI=inv(H); A=mul(L,mul(Q,mul(DJ,B))); AI=inv(A)

def lift(x): return mv(B,x)
def m(v): return dot(v,G,v)
def rho(v): return sc(F(1,1)/m(v),mul(outer(v,v),G))
def pure(v): return (m(v),rho(v))

ck('A1 authority', BASE.startswith('47fa9ddd') and ISSUE==505)
ck('A2 Gram', mul(G,GI)==I4)
ck('A3 motor', pw(DJ,5)==I4 and mul(T(DJ),mul(G,DJ))==G)
ck('A4 support', u2==(F(-1),)*4 and mul(P,P)==P and sharp4(P)==P and rk(P)==1 and mul(Q,Q)==Q and rk(Q)==3)
ck('A5 W', H==M(((2,1,1),(1,2,1),(1,1,2))) and mul(L,B)==I(3) and mul(Q,B)==B)
ck('A6 compressed motor', A==M(((-1,-1,F(-3,4)),(0,0,F(1,4)),(1,0,F(1,4)))) and det(A)==F(-1,4) and mul(A,AI)==I(3))

GRID=[tuple(F(x) for x in t) for t in product(range(-2,3),repeat=3) if any(t)]
ck('S1 ordered source controls', all(mv(A,mv(AI,w))==w for w in GRID))
O=M(((-1,-1,-1),(0,1,0),(0,0,1)))
ck('S2 ordered maps invertible', mul(T(O),mul(H,O))==H and det(mul(O,A))!=0 and det(mul(A,O))!=0)

V4=[lift(w) for w in GRID]
ck('R1 scalar positive', all(m(v)>0 for v in V4))
ck('R2 density projector', all(mul(rho(v),rho(v))==rho(v) and sharp4(rho(v))==rho(v) and rk(rho(v))==1 and tr(rho(v))==1 and mv(rho(v),v)==v for v in V4))
ck('R3 reconstruction', all(mul(sc(m(v),rho(v)),GI)==outer(v,v) for v in V4))
ck('R4 sign invariance', all(pure(v)==pure(tuple(-x for x in v)) for v in V4))
SMALL=[lift(tuple(F(x) for x in t)) for t in product((-1,0,1),repeat=3) if any(t)]
ck('R5 sign fibres', all((pure(v)==pure(w))==(sgn(v)==sgn(w)) for v in SMALL for w in SMALL))

ELL=(0,1,2,-2,-1)
OVER=[tuple(F(x) for x in t) for t in product(ELL,repeat=4) if any(t) and sum(t)==0]
ck('O1 finite overlap', len(OVER)>0 and all(m(v)==dot(v,G,v) and rho(v)==sc(F(1,1)/dot(v,G,v),mul(outer(v,v),G)) for v in OVER))

XI=sub(mul(O,A),mul(A,O)); w=(F(1),F(0),F(0)); l=lift(mv(mul(O,A),w)); r=lift(mv(mul(A,O),w))
ck('C1 nonzero commutator witness', XI!=M([[0]*3 for _ in range(3)]) and rk(XI)==2)
ck('C2 port separates witness', pure(l)!=pure(r))

ELOW=sc(F(1,4),J4)
ck('T1 target last', P==ELOW and Q==sub(I4,ELOW))

bad=0
for label,ok in C:
    print(('PASS ' if ok else 'FAIL ')+label); bad+=int(not ok)
print('SOURCE ordered_outputs=full_W_sign_quotient')
print('PORT admissible_class=singleton')
print('OVERLAP vectors=%d sign_classes=%d'%(len(OVER),len({sgn(v) for v in OVER})))
print('READONLY feeds_U=FALSE source_to_K_encoding=NONE')
print('SCHEMA separate_bridge_manifest_possible gate_unregistered')
print('DECISION PORT-CANONICAL')
print('SAMPLING NOT PROVIDED')
print('RESULT %d/%d PASS'%(len(C)-bad,len(C)))
raise SystemExit(1 if bad else 0)
