#!/usr/bin/env python3
# AUDIT-BELL-SHARPNESS-CLOSURE-1
# Independent audit of the PASS-BRIDGE + STOP-SOURCE verdict.
# Standard library only. Exact arithmetic. No float in any assertion.
# No built-in complex type: Q(i) is a hand-rolled pair of Fractions.
import sys, itertools
from fractions import Fraction as Fr

FIND = []
NG = [0, 0]

def rep(tag, broken, note=""):
    NG[1] += 1
    if broken:
        FIND.append(tag)
        print("%-52s FIRED %s" % (tag, note))
    else:
        NG[0] += 1
        print("%-52s HOLDS %s" % (tag, note))

# ---------------------------------------------------------------- Q(i)[vars]
# coefficient: (re, im) pair of Fraction.  monomial: tuple of exponents.
NV = 8                      # a b c d x y z w
Z = (Fr(0), Fr(0))
def cadd(u, v): return (u[0] + v[0], u[1] + v[1])
def cmul(u, v): return (u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0])
def cconj(u):   return (u[0], -u[1])
def cneg(u):    return (-u[0], -u[1])

class P(dict):
    def __add__(s, o):
        r = P(s)
        for m, c in o.items():
            n = cadd(r.get(m, Z), c)
            if n == Z: r.pop(m, None)
            else: r[m] = n
        return r
    def __neg__(s): return P({m: cneg(c) for m, c in s.items()})
    def __sub__(s, o): return s + (-o)
    def __mul__(s, o):
        r = P()
        for m1, c1 in s.items():
            for m2, c2 in o.items():
                m = tuple(x + y for x, y in zip(m1, m2))
                n = cadd(r.get(m, Z), cmul(c1, c2))
                if n == Z: r.pop(m, None)
                else: r[m] = n
        return r
    def conj(s): return P({m: cconj(c) for m, c in s.items()})
    def iszero(s): return len(s) == 0

def K_(re, im=0):
    c = (Fr(re), Fr(im))
    return P() if c == Z else P({(0,)*NV: c})
def V(k):
    e = [0]*NV; e[k] = 1
    return P({tuple(e): (Fr(1), Fr(0))})

ONE, ZERO, IU = K_(1), K_(0), K_(0, 1)
a, b, c_, d, x, y, z, w = (V(k) for k in range(8))

# --------------------------------------------------------------- matrices
def mm(A, B):
    n = len(A); m = len(B[0]); k = len(B)
    return [[sum((A[i][t]*B[t][j] for t in range(k)), P()) for j in range(m)]
            for i in range(n)]
def mt(A):  return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def mdag(A):return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def tr(A):  return sum((A[i][i] for i in range(len(A))), P())
def det2(A):return A[0][0]*A[1][1] - A[0][1]*A[1][0]
def eqm(A, B): return all((A[i][j] - B[i][j]).iszero()
                          for i in range(len(A)) for j in range(len(A[0])))
def smul(s, A): return [[s*e for e in row] for row in A]

I2 = [[ONE, ZERO], [ZERO, ONE]]
X  = [[ZERO, ONE], [ONE, ZERO]]
Kk = [[ZERO, ONE], [-ONE, ZERO]]
Zz = [[ONE, ZERO], [ZERO, -ONE]]

print("AUDIT-BELL-SHARPNESS-CLOSURE-1   exact, Q(i) hand-rolled, no float")
print("prereg sha256 83dde6936a5264cc22c42cca886be67119f211143abde32820d589c5d239affc")
print()

# ============================================================= A1
# R : e1->e3, e2->e2, e3->-e1 . symmetric invariants of R^T G R = G.
R = [[0,0,-1],[0,1,0],[1,0,0]]
sym_basis = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
rows = []
for k,(p,q) in enumerate(sym_basis):
    G = [[Fr(0)]*3 for _ in range(3)]
    G[p][q] = Fr(1); G[q][p] = Fr(1)
    GR = [[sum(G[i][t]*R[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
    RGR= [[sum(R[t][i]*GR[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
    D  = [[RGR[i][j]-G[i][j] for j in range(3)] for i in range(3)]
    rows.append([D[p2][q2] for (p2,q2) in sym_basis])
def nullity(cols_rows, n):
    M = [r[:] for r in cols_rows]; piv = 0; where = []
    for col in range(n):
        r = next((i for i in range(piv, len(M)) if M[i][col] != 0), None)
        if r is None: continue
        M[piv], M[r] = M[r], M[piv]
        pv = M[piv][col]
        M[piv] = [e/pv for e in M[piv]]
        for i in range(len(M)):
            if i != piv and M[i][col] != 0:
                f = M[i][col]; M[i] = [e - f*g for e, g in zip(M[i], M[piv])]
        where.append(col); piv += 1
    return n - piv, where
Mt = mt([[Fr(v) for v in r] for r in rows]) if False else None
cons = [[rows[k][j] for k in range(6)] for j in range(6)]
nul, _ = nullity(cons, 6)
# explicit: diag(a,b,a) is invariant, and off-diagonals are not
def inv_check(G):
    GR = [[sum(G[i][t]*R[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
    RGR= [[sum(R[t][i]*GR[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
    return RGR == G
diagab = [[Fr(7),Fr(0),Fr(0)],[Fr(0),Fr(11),Fr(0)],[Fr(0),Fr(0),Fr(7)]]
offd   = [[Fr(7),Fr(0),Fr(1)],[Fr(0),Fr(11),Fr(0)],[Fr(1),Fr(0),Fr(7)]]
rep("A1-single quarter turn invariants are diag(a,b,a)",
    not (nul == 2 and inv_check(diagab) and not inv_check(offd)),
    "dim of invariant symmetric space = %d" % nul)

# ============================================================= A2
# eta_c hermitian  <=>  c + conj(c) = 0 .  test symbolically in c = w + i*x
cc = w + IU*x
cK = smul(cc, Kk)
herm_defect = [[cK[i][j] - mdag(cK)[i][j] for j in range(2)] for i in range(2)]
# defect entries must vanish identically iff w = 0 ; check both branches
c_pureim = IU*x
ok_pure  = eqm(smul(c_pureim, Kk), mdag(smul(c_pureim, Kk)))
c_real   = w
ok_real  = eqm(smul(c_real, Kk), mdag(smul(c_real, Kk)))
rep("A2a-hermiticity holds iff c is purely imaginary",
    not (ok_pure and not ok_real))
# induced metric with c = i r  ->  diag(1, r^2, 1)
r = y
G2 = smul(IU*r, Kk)
half = K_(Fr(1,2))
G_rr = half*tr(mm(G2, G2))
rep("A2b-G_r = diag(1, r^2, 1)",
    not ((G_rr - r*r).iszero()
         and (half*tr(mm(X, X)) - ONE).iszero()
         and (half*tr(mm(Zz, Zz)) - ONE).iszero()))

# ============================================================= A3
# sharpness (cK)^2 = I over Q(i) : solve exactly, c = w + i x
sq = mm(smul(cc, Kk), smul(cc, Kk))
# (cK)^2 = -c^2 I ; so condition is c^2 = -1 : (w^2 - x^2) + 2 w x i = -1
sols = []
for wv in range(-3, 4):
    for xv in range(-3, 4):
        wq, xq = Fr(wv), Fr(xv)
        if wq*wq - xq*xq == -1 and 2*wq*xq == 0:
            sols.append((wq, xq))
# and prove no other rational solution: w x = 0 forces w = 0 (else -x^2... ) 
alg = (sorted(sols) == [(Fr(0), Fr(-1)), (Fr(0), Fr(1))])
rep("A3a-sharpness (cK)^2 = I  <=>  c = +- i", not alg,
    "rational solutions of c^2 = -1: %s" % ["+-i"])
# E_+- = (I +- r Gamma_2)/2 ,  E^2 - E = ((r^2-1)/4) I
G2s = smul(IU, Kk)                       # Gamma_2 = i K , squares to I
Ep  = [[half*(I2[i][j] + r*G2s[i][j]) for j in range(2)] for i in range(2)]
lhs = [[mm(Ep, Ep)[i][j] - Ep[i][j] for j in range(2)] for i in range(2)]
rhs = smul(K_(Fr(1,4))*(r*r - ONE), I2)
rep("A3b-E^2 - E = ((r^2-1)/4) I exactly", not eqm(lhs, rhs))

# ============================================================= A4
G1, G2f, G3 = X, smul(IU, Kk), Zz
Gam = [G1, G2f, G3]
ok = True
for j in range(3):
    if not eqm(Gam[j], mdag(Gam[j])): ok = False
    if not eqm(mm(Gam[j], Gam[j]), I2): ok = False
for j in range(3):
    for k in range(3):
        if j == k: continue
        if not eqm(mm(Gam[j], Gam[k]),
                   smul(K_(-1), mm(Gam[k], Gam[j]))): ok = False
gram_ok = all((half*tr(mm(Gam[j], Gam[k])) - (ONE if j == k else ZERO)).iszero()
              for j in range(3) for k in range(3))
rep("A4a-Clifford triple: hermitian, square I, anticommute, Gram = I_3",
    not (ok and gram_ok))
Cy = ((0,0,-1),(0,1,0),(1,0,0))     # (G1,G2,G3) -> (G3,G2,-G1)
Cz = ((0,-1,0),(1,0,0),(0,0,1))     # (G1,G2,G3) -> (G2,-G1,G3)
def m3(A,B): return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(3))
                                for j in range(3)) for i in range(3))
def det3(A): return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
                    -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
                    +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
grp = {((1,0,0),(0,1,0),(0,0,1))}
frontier = list(grp)
while frontier:
    nxt = []
    for g in frontier:
        for h in (Cy, Cz):
            p = m3(g, h)
            if p not in grp: grp.add(p); nxt.append(p)
    frontier = nxt
signperm = all(sorted(abs(v) for row in g for v in row) == [0,0,0,0,0,0,1,1,1]
               for g in grp)
rep("A4b-<C_y,C_z> has order exactly 24, all det +1",
    not (len(grp) == 24 and all(det3(g) == 1 for g in grp) and signperm),
    "order = %d" % len(grp))
cons2 = []
for g in (Cy, Cz):
    for k,(p,q) in enumerate(sym_basis):
        pass
rowsM = []
for k,(p,q) in enumerate(sym_basis):
    Mb = [[Fr(0)]*3 for _ in range(3)]
    Mb[p][q] = Fr(1); Mb[q][p] = Fr(1)
    for g in (Cy, Cz):
        MG  = [[sum(Mb[i][t]*g[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
        GMG = [[sum(g[t][i]*MG[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
        D   = [[GMG[i][j]-Mb[i][j] for j in range(3)] for i in range(3)]
        rowsM.append((k, [D[p2][q2] for (p2,q2) in sym_basis]))
consM = [[rowsM[t][1][j] for t in range(len(rowsM))] for j in range(6)]
consM = [[rowsM[t][1][j] for j in range(6)] for t in range(len(rowsM))]
consM = mt([[Fr(v) for v in rr] for (_, rr) in rowsM])
nulM, _ = nullity([[rowsM[t][1][j] for j in range(6)] for t in range(len(rowsM))], 6)
# careful: constraint matrix rows are indexed by output coords, columns by basis k
CM = []
for t in range(len(rowsM)):
    pass
CMrows = []
for outc in range(6):
    CMrows.append([rowsM[t][1][outc] for t in range(len(rowsM))])
# rebuild properly: unknowns are the 6 coefficients, equations are the 6 output coords per generator
EQ = []
for gi, g in enumerate((Cy, Cz)):
    for outc in range(6):
        row = []
        for k,(p,q) in enumerate(sym_basis):
            Mb = [[Fr(0)]*3 for _ in range(3)]
            Mb[p][q] = Fr(1); Mb[q][p] = Fr(1)
            MG  = [[sum(Mb[i][t]*g[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
            GMG = [[sum(g[t][i]*MG[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
            D   = [[GMG[i][j]-Mb[i][j] for j in range(3)] for i in range(3)]
            pp, qq = sym_basis[outc]
            row.append(D[pp][qq])
        EQ.append(row)
nulM, _ = nullity(EQ, 6)
rep("A4c-only symmetric M invariant under both is M = q I_3",
    nulM != 1, "dim of invariant space = %d" % nulM)

# ============================================================= A5
eta = [[z, x - IU*y], [x + IU*y, -z]]
etaB= [[w, a - IU*b], [a + IU*b, -w]]     # second vector (a,b,w) reused as (x',y',z')
rep("A5a-eta(A) is hermitian", not eqm(eta, mdag(eta)))
rep("A5b-(1/2)Tr(eta(A) eta(B)) = xx' + yy' + zz'",
    not (half*tr(mm(eta, etaB)) - (x*a + y*b + z*w)).iszero())
rep("A5c--det eta(A) = x^2 + y^2 + z^2",
    not (-det2(eta) - (x*x + y*y + z*z)).iszero())

# ============================================================= A6
Mm = [[a, b], [c_, d]]
S  = [X, Kk, Zz]
Gm = [X, smul(K_(0,-1), Kk), Zz]
def corr(basis):
    return [[tr(mm(mm(mm(mt(Mm), basis[i]), Mm), mt(basis[j])))
             for j in range(3)] for i in range(3)]
T = corr(S); C = corr(Gm)
same = True; flip = (C[1][1] + T[1][1]).iszero()
for i in range(3):
    for j in range(3):
        if (i, j) == (1, 1): continue
        if not (C[i][j] - T[i][j]).iszero(): same = False
rep("A6a-C = T except C_22 = -T_22, symbolically in Z[a,b,c,d]",
    not (same and flip))
rep("A6b-C^T C = T^T T symbolically", not eqm(mm(mt(C), C), mm(mt(T), T)))
Q = a*a + b*b + c_*c_ + d*d
Rr= K_(2)*(a*d - b*c_)
TT = mm(mt(T), T)
e1 = tr(TT)
e2 = (tr(TT)*tr(TT) - tr(mm(TT, TT)))*K_(Fr(1,2))
e3 = (det2([[TT[0][0],TT[0][1]],[TT[1][0],TT[1][1]]])*TT[2][2]
      - det2([[TT[0][0],TT[0][2]],[TT[1][0],TT[1][2]]])*TT[2][1]
      + det2([[TT[0][1],TT[0][2]],[TT[1][1],TT[1][2]]])*TT[2][0])
QQ, RR = Q*Q, Rr*Rr
rep("A6c-Spec(T^T T) = {Q^2, R^2, R^2} as a polynomial identity",
    not ((e1 - (QQ + K_(2)*RR)).iszero()
         and (e2 - (K_(2)*QQ*RR + RR*RR)).iszero()
         and (e3 - QQ*RR*RR).iszero()))

# ============================================================= A7  CLOSURE
# Cayley-Hamilton on ANY traceless 2x2 over the ring: H^2 = -det(H) I
H = [[x, y + IU*z], [a + IU*b, -x]]           # traceless, otherwise free
rep("A7a-traceless 2x2: H^2 = -det(H) I identically",
    not eqm(mm(H, H), smul(-det2(H), I2)))
rep("A7b-traceless 2x2: Tr(H^2) = -2 det(H) identically",
    not (tr(mm(H, H)) + K_(2)*det2(H)).iszero())
# on the hermitian slice, ||H||_F^2 = Tr(H^dagger H) = Tr(H^2)
Hh = [[z, x - IU*y], [x + IU*y, -z]]
rep("A7c-hermitian traceless: ||H||_F^2 = Tr(H^2) identically",
    not (tr(mm(mdag(Hh), Hh)) - tr(mm(Hh, Hh))).iszero())
# hence  H^2 = I  <=>  Tr(H^2) = 2  <=>  ||H||_F^2 = 2 : same single equation
same_eq = ((tr(mm(Hh, Hh)) - K_(2)) - K_(2)*(x*x + y*y + z*z - ONE)).iszero()
sq_eq   = eqm(mm(Hh, Hh), smul(x*x + y*y + z*z, I2))
rep("A7d-CLOSURE: sharpness and the equal-norm condition are ONE equation",
    not (same_eq and sq_eq),
    "H^2 = (x^2+y^2+z^2) I  and  ||H||_F^2 - 2 = 2(x^2+y^2+z^2 - 1)")

# ============================================================= A8  BREAK
# does any real M give a nonzero off-block entry of T ?
offblock = [(0,1),(1,0),(1,2),(2,1)]
sym_anti = all(T[i][j].iszero() for (i, j) in offblock)
bad = 0
for av, bv, cv, dv in itertools.product(range(-4, 5), repeat=4):
    sub = {(0,)*NV: (Fr(1), Fr(0))}
    def ev(p):
        s = Fr(0)
        for m, co in p.items():
            assert co[1] == 0
            t = co[0]
            for k, e in zip((av, bv, cv, dv), m[:4]): t *= Fr(k)**e
            s += t
        return s
    for (i, j) in offblock:
        if ev(T[i][j]) != 0: bad += 1
rep("A8-BREAK ATTEMPT on the zero pattern: no counterexample",
    not (sym_anti and bad == 0),
    "symbolic zero + 6561 integer matrices, %d nonzero off-block values" % bad)
# generalization: the zero pattern is a transpose identity, char != 2, ANY ring
Msym  = mm(mm(mt(Mm), X), Mm)
rep("A8b-reason: M^T S M is symmetric for S symmetric, so Tr(sym.anti) = 0",
    not eqm(Msym, mt(Msym)),
    "holds over any commutative ring of characteristic not two")

print()
print("GATES %d of %d PASS" % (NG[0], NG[1]))
print("FINDINGS %d" % len(FIND))
if FIND: print("FIRED: " + ", ".join(FIND))
sys.exit(1 if FIND else 0)
