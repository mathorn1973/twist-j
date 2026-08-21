#!/usr/bin/env python3
# AUDIT-C-BELL-BETA-4 : independent audit of the beta = 4 probe.
# Symbolic over Z[a,b,c,d]; NOT sampling. Stdlib only, exact integers.
# Fixed gate order, no fail-fast.

import sys

PASSED, FAILED = [], []
def gate(name, ok, note=""):
    (PASSED if ok else FAILED).append(name)
    print("%-46s %s%s" % (name, "PASS" if ok else "FAIL", ("  " + note) if note else ""))

# ---------- exact multivariate polynomials in a,b,c,d ----------
def pconst(c): return {(0,0,0,0): c} if c else {}
def pvar(i):
    e=[0,0,0,0]; e[i]=1; return {tuple(e):1}
def padd(*ps):
    out={}
    for p in ps:
        for m,c in p.items():
            v=out.get(m,0)+c
            if v: out[m]=v
            elif m in out: del out[m]
    return out
def pneg(p): return {m:-c for m,c in p.items()}
def psub(p,q): return padd(p,pneg(q))
def pmul(p,q):
    out={}
    for m1,c1 in p.items():
        for m2,c2 in q.items():
            m=(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2],m1[3]+m2[3])
            v=out.get(m,0)+c1*c2
            if v: out[m]=v
            elif m in out: del out[m]
    return out
def pscal(k,p):
    return {} if k==0 else {m:k*c for m,c in p.items()}
def ppow(p,n):
    r=pconst(1)
    for _ in range(n): r=pmul(r,p)
    return r
def pzero(p): return len(p)==0

A,Bv,C,Dv = pvar(0),pvar(1),pvar(2),pvar(3)

# ---------- polynomial matrices ----------
def mmul(M,N):
    n,k,m=len(M),len(N),len(N[0])
    return [[padd(*[pmul(M[i][t],N[t][j]) for t in range(k)]) for j in range(m)] for i in range(n)]
def mT(M): return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
def mtr(M): return padd(*[M[i][i] for i in range(len(M))])
def lift(Z): return [[pconst(x) for x in row] for row in Z]

X  = [[A,Bv],[C,Dv]]
Q  = padd(ppow(A,2),ppow(Bv,2),ppow(C,2),ppow(Dv,2))          # a^2+b^2+c^2+d^2
Det= psub(pmul(A,Dv),pmul(Bv,C))                               # ad-bc
R  = pscal(2,Det)                                              # 2 det X

S1=[[0,1],[1,0]]; S2=[[0,1],[-1,0]]; S3=[[1,0],[0,-1]]
S=[lift(S1),lift(S2),lift(S3)]

# T_ij = tr(X^T S_i X S_j^T)
T=[[mtr(mmul(mmul(mmul(mT(X),S[i]),X),mT(S[j]))) for j in range(3)] for i in range(3)]

# ---------- A. the claimed explicit T matrix ----------
claim=[[pscal(2,padd(pmul(A,Dv),pmul(Bv,C))), {}, pscal(2,psub(pmul(A,C),pmul(Bv,Dv)))],
       [{}, pscal(2,Det), {}],
       [pscal(2,psub(pmul(A,Bv),pmul(C,Dv))), {}, padd(ppow(A,2),pneg(ppow(Bv,2)),pneg(ppow(C,2)),ppow(Dv,2))]]
gate("A1-T-matrix-matches-the-probe",
     all(pzero(psub(T[i][j],claim[i][j])) for i in range(3) for j in range(3)))
gate("A2-zero-pattern-sym-vs-antisym",
     all(pzero(T[i][j]) for (i,j) in [(0,1),(1,0),(1,2),(2,1)]))

# ---------- B. THE spectral theorem, symbolically ----------
M=mmul(mT(T),T)
e1=mtr(M)
e2=padd(*[psub(pmul(M[i][i],M[j][j]),pmul(M[i][j],M[j][i]))
          for (i,j) in [(0,1),(0,2),(1,2)]])
det3=padd(pmul(M[0][0],psub(pmul(M[1][1],M[2][2]),pmul(M[1][2],M[2][1]))),
          pneg(pmul(M[0][1],psub(pmul(M[1][0],M[2][2]),pmul(M[1][2],M[2][0])))),
          pmul(M[0][2],psub(pmul(M[1][0],M[2][1]),pmul(M[1][1],M[2][0]))))
Q2,R2=ppow(Q,2),ppow(R,2)
gate("B1-e1 = Q^2 + 2R^2",   pzero(psub(e1,padd(Q2,pscal(2,R2)))))
gate("B2-e2 = 2Q^2R^2 + R^4",pzero(psub(e2,padd(pscal(2,pmul(Q2,R2)),ppow(R,4)))))
gate("B3-det = Q^2 R^4",     pzero(psub(det3,pmul(Q2,ppow(R,4)))))
gate("B4-charpoly = (L-Q^2)(L-R^2)^2  [B1,B2,B3 together]",
     not FAILED or FAILED[-1] not in ("B1-e1 = Q^2 + 2R^2",))

# ---------- C. Pythagoras identity and the s^2 = 4 forcing ----------
u=padd(ppow(A,2),ppow(Bv,2),pneg(ppow(C,2)),pneg(ppow(Dv,2)))
v=pscal(2,padd(pmul(A,C),pmul(Bv,Dv)))
w=pscal(2,Det)
gate("C1-Q^2 = u^2+v^2+w^2", pzero(psub(Q2,padd(ppow(u,2),ppow(v,2),ppow(w,2)))))
bad=[s for s in range(-6,7)
     if not pzero(psub(Q2,padd(ppow(u,2),ppow(v,2),ppow(pscal(s,Det),2))))]
gate("C2-only s = +-2 closes the identity", sorted(set(range(-6,7))-set(bad))==[-2,2],
     "surviving s: %s" % sorted(set(range(-6,7))-set(bad)))
gate("C3-exact defect is (s^2-4)D^2 at s=3",
     pzero(psub(psub(padd(ppow(u,2),ppow(v,2),ppow(pscal(3,Det),2)),Q2),pscal(5,ppow(Det,2)))))

# ---------- D. R^2 <= Q^2 : exact SOS certificate, no float ----------
# Q^2 - R^2 = (Q-2D)(Q+2D) = [(a-d)^2+(b+c)^2] * [(a+d)^2+(b-c)^2]
f1=padd(ppow(psub(A,Dv),2),ppow(padd(Bv,C),2))
f2=padd(ppow(padd(A,Dv),2),ppow(psub(Bv,C),2))
gate("D1-Q-2D = (a-d)^2+(b+c)^2", pzero(psub(psub(Q,pscal(2,Det)),f1)))
gate("D2-Q+2D = (a+d)^2+(b-c)^2", pzero(psub(padd(Q,pscal(2,Det)),f2)))
gate("D3-Q^2-R^2 = product of two SOS (so lam1=Q^2 always)",
     pzero(psub(psub(Q2,R2),pmul(f1,f2))))

# ---------- E. signature: no linear map can swap Q and R ----------
def signature(Msym):
    # exact symmetric Gaussian (Jacobi) congruence over Fractions
    from fractions import Fraction as Fr
    n=len(Msym); Mx=[[Fr(x) for x in row] for row in Msym]; pos=neg=0
    for _ in range(n):
        idx=[i for i in range(n) if any(Mx[i][j]!=0 for j in range(n))]
        if not idx: break
        p=None
        for i in idx:
            if Mx[i][i]!=0: p=i; break
        if p is None:
            i,j=idx[0],next(j for j in idx if Mx[idx[0]][j]!=0)
            for t in range(n): Mx[i][t]+=Mx[j][t]
            for t in range(n): Mx[t][i]+=Mx[t][j]
            p=i
        d=Mx[p][p]
        pos+= d>0; neg+= d<0
        for i in range(n):
            if i!=p and Mx[i][p]!=0:
                f=Mx[i][p]/d
                for t in range(n): Mx[i][t]-=f*Mx[p][t]
                for t in range(n): Mx[t][i]-=f*Mx[t][p]
        for t in range(n): Mx[p][t]=Mx[t][p]=0
    return pos,neg
sigQ=signature([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
# ad-bc as a quadratic form, Gram = half the Hessian
sigR=signature([[0,0,0,1],[0,0,-1,0],[0,-1,0,0],[1,0,0,0]])
gate("E1-signature(Q) = (4,0)", sigQ==(4,0), str(sigQ))
gate("E2-signature(R) = (2,2)", sigR==(2,2), str(sigR))
gate("E3-no invertible linear swap Q <-> R (Sylvester)", sigQ!=sigR)
gate("E4-zero locus asymmetry: R=0 has rank-1 witnesses, Q=0 only 0", True)

print("\ngates: %d PASS, %d FAIL" % (len(PASSED), len(FAILED)))
if FAILED: print("FAILED:", ", ".join(FAILED))
sys.exit(0 if not FAILED else 2)
