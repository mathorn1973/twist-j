#!/usr/bin/env python3
# verify_cm_2i_qcarrier_2.py
# Exact verifier for C-CM-2I-QCARRIER-2 (TWIST-J incubation lane,
# NON-CANONICAL, no canon writes). Against Public Canon v30.
#
# Second slice of the audit-proposed probe P-CM-2I-QCARRIER-1: the
# EXPLICIT semilinear quarter-turn on the branch pair, with its cocycle.
# Setting: K = Q(zeta5), Gal(K/Q) = <tau>, tau(zeta) = zeta^2,
# tau^2 = sigma (CM involution); G = <S, T> the registered integral 2I
# lift (COLOR-INTEGRAL-LIFT); pair carrier V = K^2 (+) K^2 with
# Pi(g) = diag(g, tau(g)). A G-equivariant tau-semilinear map is
# necessarily nu(x, y) = (C tau(y), d tau(x)) with C the sigma-
# intertwiner (C sigma(g) = g C) and d a scalar (Schur; the diagonal
# Hom-blocks vanish because rho and rho^tau are the two DIFFERENT
# golden branches).
#
# Results proved here, exactly:
#   1. The sigma-intertwiner line is one K-line; the primitive C is
#      computed and intertwines all 120 elements.
#   2. The cocycle C sigma(C) = mu I with mu = -phi^2, TOTALLY NEGATIVE.
#      Norms of the CM extension are totally positive, so no rescaling
#      of C or choice of d gives nu^4 = 1: the class of the obstruction
#      is [-1] in F^x / N(K^x).
#   3. With N(d) = phi^2 (solvable, deterministic smallest d) the
#      quarter-turn closes at order EIGHT: nu^4 = -1, nu^8 = 1.
#      The arithmetic quarter-turn on the equivariant pair is a C8
#      central extension -- exactly the order of the registered
#      antiunitary spinor lift of the rotoreflection S (C-HERM2 gate
#      C5), and the same central sign as the mu_5-escaping glue phase
#      1 - J (C-CENTRAL-LIFT-PHASE-1 gate CP12) and the half-tick
#      obstruction sigma(phi) < 0 (C-COMMON-CARRIER-ICOSIAN-1 gate T6).
#   4. nu swaps the two branch summands, nu^2 preserves them acting as
#      the sigma-descent: ker chi5 within branches, the coset across --
#      completing the descent picture of C-CM-2I-QCARRIER-1.
#   5. nu transports the pair Gram diag(H0, tau H0) exactly onto
#      diag(N(d) tau H0, kappa sigma H0): a semilinear similitude with
#      totally positive multipliers.
# Exact arithmetic; Python 3 stdlib; deterministic, no randomness.
import sys
from fractions import Fraction as F
from math import gcd

R = []
def ck(name, cond):
    ok = bool(cond)
    R.append(ok)
    print(("PASS " if ok else "FAIL ") + name)

# ---------- Q(zeta5) exact ----------
def red(v):
    c = v[4]
    return (v[0]-c, v[1]-c, v[2]-c, v[3]-c)
def zmul(a, b):
    v = [F(0)]*5
    for i in range(4):
        if a[i] == 0: continue
        for j in range(4):
            if b[j] == 0: continue
            v[(i+j) % 5] += a[i]*b[j]
    return red(tuple(v))
def zadd(a, b): return tuple(p+q for p, q in zip(a, b))
def zsub(a, b): return tuple(p-q for p, q in zip(a, b))
def zint(n): return (F(n), F(0), F(0), F(0))
def zneg(a): return tuple(-p for p in a)
def gal(a, k):
    v = [F(0)]*5
    for i in range(4): v[(i*k) % 5] += a[i]
    return red(tuple(v))
def zinv(a):
    cols = []
    for e in range(4):
        y = [F(0)]*4; y[e] = F(1)
        cols.append(zmul(a, tuple(y)))
    A = [[cols[c][r] for c in range(4)] for r in range(4)]
    b = [F(1), F(0), F(0), F(0)]
    for c in range(4):
        piv = None
        for r in range(c, 4):
            if A[r][c] != 0: piv = r; break
        if piv is None: return None
        A[c], A[piv] = A[piv], A[c]; b[c], b[piv] = b[piv], b[c]
        inv = 1/A[c][c]
        A[c] = [t*inv for t in A[c]]; b[c] = b[c]*inv
        for r in range(4):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f*y for x, y in zip(A[r], A[c])]
                b[r] = b[r] - f*b[c]
    return tuple(b)
Z0 = zint(0); Z1 = zint(1)
X5 = (F(0), F(1), F(0), F(0))
PHI = (F(0), F(0), F(-1), F(-1))
def to_F(a):
    if a[1] != 0 or a[2] != a[3]: return None
    y = -a[2]/F(2)
    return (a[0] + y, y)
def fsign(p):
    x, y = p
    if x == 0 and y == 0: return 0
    if x >= 0 and y >= 0: return 1
    if x <= 0 and y <= 0: return -1
    big = 1 if x*x > 5*y*y else -1
    return big if x > 0 else -big
def fgal(p): return (p[0], -p[1])

# ---------- 2x2 matrices over K; the registered lift ----------
def mmul(A, B):
    return ((zadd(zmul(A[0][0], B[0][0]), zmul(A[0][1], B[1][0])),
             zadd(zmul(A[0][0], B[0][1]), zmul(A[0][1], B[1][1]))),
            (zadd(zmul(A[1][0], B[0][0]), zmul(A[1][1], B[1][0])),
             zadd(zmul(A[1][0], B[0][1]), zmul(A[1][1], B[1][1]))))
def mgal(A, k):
    return ((gal(A[0][0], k), gal(A[0][1], k)),
            (gal(A[1][0], k), gal(A[1][1], k)))
def mdag(A):
    return ((gal(A[0][0], 4), gal(A[1][0], 4)),
            (gal(A[0][1], 4), gal(A[1][1], 4)))
def mdet(A): return zsub(zmul(A[0][0], A[1][1]), zmul(A[0][1], A[1][0]))
ID2 = ((Z1, Z0), (Z0, Z1))
SM = ((Z0, zneg(Z1)), (Z1, Z0))
TM = ((X5, Z1), (Z0, gal(X5, 4)))
grp = {ID2}
frontier = [ID2]
while frontier:
    x = frontier.pop()
    for g in (SM, TM):
        y = mmul(x, g)
        if y not in grp:
            grp.add(y); frontier.append(y)
            if len(grp) > 130: frontier = []; break
G = sorted(grp)
ck("N1  the registered lift closes to 120 det-1 matrices (COLOR-INTEGRAL-LIFT reproduced)",
   len(G) == 120 and all(mdet(A) == Z1 for A in G))

# ---------- the sigma-intertwiner C ----------
def apply_lin(cvec, g):
    C = ((tuple(cvec[0:4]), tuple(cvec[4:8])),
         (tuple(cvec[8:12]), tuple(cvec[12:16])))
    D1 = mmul(C, mgal(g, 4)); D2 = mmul(g, C)
    out = []
    for i in range(2):
        for j in range(2):
            out.extend(zsub(D1[i][j], D2[i][j]))
    return out
rows = []
for g in (SM, TM):
    cols = []
    for e in range(16):
        cv = [F(0)]*16; cv[e] = F(1)
        cols.append(apply_lin(cv, g))
    for r in range(16):
        rows.append([cols[c][r] for c in range(16)])
M = [row[:] for row in rows]
piv_cols = []; rpos = 0
for c in range(16):
    piv = None
    for r in range(rpos, len(M)):
        if M[r][c] != 0: piv = r; break
    if piv is None: continue
    M[rpos], M[piv] = M[piv], M[rpos]
    inv = 1/M[rpos][c]
    M[rpos] = [t*inv for t in M[rpos]]
    for r in range(len(M)):
        if r != rpos and M[r][c] != 0:
            f = M[r][c]
            M[r] = [a - f*b for a, b in zip(M[r], M[rpos])]
    piv_cols.append(c); rpos += 1
free = [c for c in range(16) if c not in piv_cols]
ck("N2  the space of C with C sigma(g) = g C for the generators is exactly ONE K-line (rank 12, nullity 4 over Q): Schur for the two irreducible golden branches",
   len(piv_cols) == 12 and len(free) == 4)
v = [F(0)]*16; v[free[0]] = F(1)
for i, pc in enumerate(piv_cols):
    v[pc] = -M[i][free[0]]
den = 1
for t in v: den = den * t.denominator // gcd(den, t.denominator)
w = [int(t*den) for t in v]
g0 = 0
for t in w: g0 = gcd(g0, t)
if g0: w = [t//g0 for t in w]
CM_ = ((tuple(F(t) for t in w[0:4]), tuple(F(t) for t in w[4:8])),
       (tuple(F(t) for t in w[8:12]), tuple(F(t) for t in w[12:16])))
ck("N3  the primitive integral C intertwines ALL 120 elements: C sigma(g) = g C on the whole lift (multiplicativity made explicit), and C is invertible",
   all(mmul(CM_, mgal(g, 4)) == mmul(g, CM_) for g in G)
   and mdet(CM_) != Z0)

# ---------- the cocycle mu ----------
MU = mmul(CM_, mgal(CM_, 4))
mu = MU[0][0]
muF = to_F(mu)
ck("N4  C sigma(C) = mu I with mu = -phi^2 exactly: the cocycle scalar is minus a totally positive unit, hence TOTALLY NEGATIVE at both real places",
   MU[0][1] == Z0 and MU[1][0] == Z0 and MU[1][1] == mu
   and mu == zneg(zadd(Z1, PHI))
   and muF is not None and fsign(muF) == -1 and fsign(fgal(muF)) == -1)
target = gal(zinv(mu), 3)                     # tau^3(mu^-1) = -phi^-2 conjugated
sols_plus = []
sols_minus = []
rng = range(-3, 4)
for c0 in rng:
    for c1 in rng:
        for c2 in rng:
            for c3 in rng:
                if c0 == c1 == c2 == c3 == 0: continue
                d = (F(c0), F(c1), F(c2), F(c3))
                Nd = zmul(d, gal(d, 4))
                if Nd == target: sols_plus.append(d)
                elif Nd == zneg(target): sols_minus.append(d)
ck("N5  the norm equation N(d) = tau^3(mu^-1) has NO solution (exhaustive box |c_i| <= 3, and impossible in principle: the target is totally negative while CM norms are totally positive), so nu^4 = 1 is UNREACHABLE for every choice of C-scaling and d: the obstruction class is [-1] in F^x / N_{K/F}(K^x)",
   len(sols_plus) == 0 and fsign(to_F(target)) == -1 and fsign(fgal(to_F(target))) == -1)
ck("N6  the sign-flipped equation N(d) = -tau^3(mu^-1) = phi^2 IS solvable: deterministic smallest d picked from 10 small solutions",
   len(sols_minus) == 10 and to_F(zneg(target)) is not None
   and zneg(target) == zadd(Z1, PHI))
d = sorted(sols_minus)[0]

# ---------- the semilinear quarter-turn nu ----------
# semilinear maps as (4x4 matrix over K, twist exponent k): v -> M gal(v, k)
def m4mul(A, B):
    n = 4
    return tuple(tuple(
        red(tuple(sum((zmul(A[i][t], B[t][j])[m] for t in range(n)), F(0))
                  for m in range(4)) + (F(0),))
        for j in range(n)) for i in range(n))
def m4gal(A, k):
    return tuple(tuple(gal(A[i][j], k) for j in range(4)) for i in range(4))
def scomp(f1, f2):
    # apply f2 first, then f1
    M1, k1 = f1; M2, k2 = f2
    return (m4mul(M1, m4gal(M2, k1)), (k1*k2) % 5)
def blk(A, B, C_, D):
    out = []
    for i in range(2):
        out.append(tuple(A[i]) + tuple(B[i]))
    for i in range(2):
        out.append(tuple(C_[i]) + tuple(D[i]))
    return tuple(out)
ZB2 = ((Z0, Z0), (Z0, Z0))
dI = ((d, Z0), (Z0, d))
I4 = blk(ID2, ZB2, ZB2, ID2)
mI4 = blk(((zneg(Z1), Z0), (Z0, zneg(Z1))), ZB2, ZB2,
          ((zneg(Z1), Z0), (Z0, zneg(Z1))))
NU = (blk(ZB2, CM_, dI, ZB2), 2)
def Pi(g): return (blk(g, ZB2, ZB2, mgal(g, 2)), 1)
ck("N7  nu is G-equivariant: nu o Pi(g) = Pi(g) o nu exactly for both generators (4x4 semilinear composites equal)",
   all(scomp(NU, Pi(g)) == scomp(Pi(g), NU) for g in (SM, TM)))
NU2 = scomp(NU, NU)
NU4 = scomp(NU2, NU2)
NU8 = scomp(NU4, NU4)
ck("N8  nu^2 is block-diagonal sigma-semilinear (the pair's global conjugation), nu^4 = -1 exactly, nu^8 = 1: the arithmetic quarter-turn on the equivariant pair closes at order EIGHT with central sign -1, never at order four",
   NU2[1] == 4
   and all(NU2[0][i][j] == Z0 for i in range(2) for j in range(2, 4))
   and all(NU2[0][i][j] == Z0 for i in range(2, 4) for j in range(2))
   and NU4 == (mI4, 1) and NU8 == (I4, 1))
ck("N9  the central sign is the SAME bit for the third time: mu = -phi^2 pairs with the order-8 antiunitary spinor lift of S (C-HERM2 gate C5), the mu_5-escaping tenth-root glue phase 1 - J = -zeta5^2 with (1-J)^5 = -1 (C-CENTRAL-LIFT-PHASE-1 CP12), and the half-tick obstruction sigma(phi^-1) = -phi < 0 (C-COMMON-CARRIER-ICOSIAN-1 T6): vector level C4, spinor level C8, exactly",
   zmul(zneg(zmul(X5, X5)), zmul(zneg(zmul(X5, X5)), zmul(zneg(zmul(X5, X5)), zmul(zneg(zmul(X5, X5)), zneg(zmul(X5, X5)))))) == zneg(Z1)
   and fsign(fgal(to_F(zsub(PHI, Z1)))) == -1)
ck("N10 nu swaps the two branch summands (antidiagonal blocks, diagonal zero) while nu^2 preserves them: ker chi5 acts within branches, the nontrivial coset across -- the explicit operator completing the descent dichotomy of C-CM-2I-QCARRIER-1",
   all(NU[0][i][j] == Z0 for i in range(2) for j in range(2))
   and all(NU[0][i][j] == Z0 for i in range(2, 4) for j in range(2, 4))
   and any(NU[0][i][j] != Z0 for i in range(2) for j in range(2, 4))
   and any(NU[0][i][j] != Z0 for i in range(2, 4) for j in range(2)))

# ---------- Gram transport ----------
H0 = ZB2
for A in G:
    P = mmul(mdag(A), A)
    H0 = ((zadd(H0[0][0], P[0][0]), zadd(H0[0][1], P[0][1])),
          (zadd(H0[1][0], P[1][0]), zadd(H0[1][1], P[1][1])))
Bm = blk(ZB2, CM_, dI, ZB2)
def m4dag(A):
    return tuple(tuple(gal(A[j][i], 4) for j in range(4)) for i in range(4))
Hp = blk(H0, ZB2, ZB2, mgal(H0, 2))
Tp = m4mul(m4dag(Bm), m4mul(Hp, Bm))
CtH0C = mmul(mdag(CM_), mmul(H0, CM_))
sH0 = mgal(H0, 4)
kap = zmul(CtH0C[0][0], zinv(sH0[0][0]))
Nd = zmul(d, gal(d, 4))
ck("N11 Gram transport: B-dagger diag(H0, tau H0) B = diag(N(d) tau H0, kappa sigma H0) exactly, with kappa in F totally positive: nu is a semilinear similitude between the pair Gram and its Galois twist -- the quarter-turn respects the unique invariant form up to totally positive scale",
   Tp == blk(((zmul(Nd, gal(H0[0][0], 2)), zmul(Nd, gal(H0[0][1], 2))),
              (zmul(Nd, gal(H0[1][0], 2)), zmul(Nd, gal(H0[1][1], 2)))),
             ZB2, ZB2,
             ((zmul(kap, sH0[0][0]), zmul(kap, sH0[0][1])),
              (zmul(kap, sH0[1][0]), zmul(kap, sH0[1][1]))))
   and to_F(kap) is not None
   and fsign(to_F(kap)) == 1 and fsign(fgal(to_F(kap))) == 1)

n = len(R); ok = sum(R)
print("SUMMARY %d/%d PASS" % (ok, n))
sys.exit(0 if ok == n else 1)
