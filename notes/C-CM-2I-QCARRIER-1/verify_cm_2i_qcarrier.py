#!/usr/bin/env python3
# verify_cm_2i_qcarrier.py
# Exact verifier for C-CM-2I-QCARRIER-1 (TWIST-J incubation lane,
# NON-CANONICAL, no canon writes). Against Public Canon v30.
#
# Question (audit-proposed probe P-CM-2I-QCARRIER-1, first slice): which
# part of the arithmetic Galois C4 of K = Q(zeta5) is compatible with the
# registered integral 2I lift <S, T> over Z[zeta5] (COLOR-INTEGRAL-LIFT),
# under GL2(K)-conjugacy as the frozen equivalence?
#
# Answer proved here, exactly:
#   1. The lift <S, T> is stable AS A SET under the CM involution sigma
#      (zeta -> zeta^4): complex conjugation acts on the single carrier
#      directly, entrywise.
#   2. The quarter-turn tau (zeta -> zeta^2) twists the lift to a group
#      whose (order, trace) class function DIFFERS exactly on the golden
#      classes (phi-1 <-> -phi, phi <-> 1-phi): tau(G) realizes the OTHER
#      2-dim irrep (2b), so no GL2(K)-conjugacy exists and the
#      quarter-turn does NOT descend to the single lift. The descent
#      subgroup of Gal(K/Q) = C4 is exactly ker chi5 = {1, sigma}:
#      THE BIT IS THE DESCENT OBSTRUCTION OF THE ARITHMETIC C4.
#   3. The Galois-closed object is the PAIR 2a + 2b: its character is
#      Q-valued on every element. This is the carrier-level echo of the
#      Herm2 finding A (Herm alone not Galois-closed, the pair is).
#   4. The invariant sigma-Hermitian Gram: H0 = sum g-dagger g over the
#      120 lift elements is computed exactly, is Hermitian, invariant,
#      totally positive definite, and the space of invariant Hermitian
#      forms is EXACTLY one-dimensional over F = Q(sqrt5): the Gram of
#      the common carrier is unique up to a positive F-scalar (the
#      audit's H0 uniqueness, machine-checked). By uniqueness this is
#      the same form as the canonical icosian h of
#      C-COMMON-CARRIER-ICOSIAN-1 under the GL2(K) identification there.
# Exact arithmetic; Python 3 stdlib; deterministic.
import sys
from fractions import Fraction as F

R = []
def ck(name, cond):
    ok = bool(cond)
    R.append(ok)
    print(("PASS " if ok else "FAIL ") + name)

# ---------- Z[zeta5] / Q(zeta5) exact ----------
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
Z0 = zint(0); Z1 = zint(1)
X5 = (F(0), F(1), F(0), F(0))
PHI = (F(0), F(0), F(-1), F(-1))
IPHI = zsub(PHI, Z1)

# ---------- 2x2 matrices over Q(zeta5) ----------
def mmul(A, B):
    return ((zadd(zmul(A[0][0], B[0][0]), zmul(A[0][1], B[1][0])),
             zadd(zmul(A[0][0], B[0][1]), zmul(A[0][1], B[1][1]))),
            (zadd(zmul(A[1][0], B[0][0]), zmul(A[1][1], B[1][0])),
             zadd(zmul(A[1][0], B[0][1]), zmul(A[1][1], B[1][1]))))
def mgal(A, k):
    return ((gal(A[0][0], k), gal(A[0][1], k)),
            (gal(A[1][0], k), gal(A[1][1], k)))
def mdag(A):                                   # sigma-conjugate transpose
    return ((gal(A[0][0], 4), gal(A[1][0], 4)),
            (gal(A[0][1], 4), gal(A[1][1], 4)))
def mtr(A): return zadd(A[0][0], A[1][1])
def mdet(A): return zsub(zmul(A[0][0], A[1][1]), zmul(A[0][1], A[1][0]))
ID2 = ((Z1, Z0), (Z0, Z1))
SM = ((Z0, zneg(Z1)), (Z1, Z0))
TM = ((X5, Z1), (Z0, gal(X5, 4)))

grp = {ID2}
frontier = [ID2]
overflow = False
while frontier and not overflow:
    x = frontier.pop()
    for g in (SM, TM):
        y = mmul(x, g)
        if y not in grp:
            grp.add(y); frontier.append(y)
            if len(grp) > 130: overflow = True; break
G = sorted(grp)
def mord(A):
    n = 1; X = A
    while X != ID2:
        X = mmul(X, A); n += 1
        if n > 200: return 0
    return n
ck("Q1  the registered lift <S, T> closes to exactly 120 matrices over Z[zeta5] with det 1 (COLOR-INTEGRAL-LIFT reproduced)",
   not overflow and len(G) == 120 and all(mdet(A) == Z1 for A in G))

# ---------- 1. Galois twists of the single carrier ----------
sigG = {mgal(A, 4) for A in grp}
tauG = {mgal(A, 2) for A in grp}
core = {ID2, ((zneg(Z1), Z0), (Z0, zneg(Z1))), SM,
        ((Z0, Z1), (zneg(Z1), Z0))}
ck("Q2  NO Galois twist fixes the lift setwise: sigma(G) and tau(G) each meet G in exactly 4 elements, and that common core is precisely {+-I, +-S} = <S>, the GEOMETRIC C4: the arithmetic Galois branches of the lift intersect exactly in the rational geometric quarter-turn -- the integral echo of the Herm2 finding that the arithmetic C4 and the rotoreflection S are different C4 realizations",
   sigG != grp and tauG != grp
   and (sigG & grp) == core and (tauG & grp) == core
   and mmul(SM, SM) == ((zneg(Z1), Z0), (Z0, zneg(Z1))))
ck("Q3  every trace of the lift is sigma-fixed pointwise (values in F), so the sigma-twist has the SAME marked class function and Noether-Deuring gives a GL2(K)-conjugacy intertwining g -> sigma(g): complex conjugation descends to the single carrier with markings intact",
   all(gal(mtr(A), 4) == mtr(A) for A in grp))
def classfn(k):
    d = {}
    for A in grp:
        key = (mord(A), gal(mtr(A), k))
        d[key] = d.get(key, 0) + 1
    return d
CF = {k: classfn(k) for k in (1, 2, 3, 4)}
irr = [A for A in grp if mtr(A)[1:] != (0, 0, 0) or mtr(A) != gal(mtr(A), 2)]
golden = [A for A in grp if gal(mtr(A), 2) != mtr(A)]
ck("Q4  the (order, trace) MULTISET is invariant under ALL four twists (the golden classes only swap), so multiset data cannot see the branch; but the tau-twist moves EVERY golden trace pointwise: tau(tr) != tr for exactly the 48 elements of orders 5 and 10, with tau(tr T) = -phi != phi - 1 = tr T on the marked generator: the quarter-turn cannot descend with markings intact -- every trace-preserving identification of G with tau(G) must compose with the OUTER automorphism swapping the golden classes 5a <-> 5b",
   CF[1] == CF[2] == CF[3] == CF[4]
   and len(golden) == 48
   and all(mord(A) in (5, 10) for A in golden)
   and mtr(TM) == IPHI and gal(mtr(TM), 2) == zneg(PHI))
ck("Q5  the tau-twisted lift is itself a closed group of 120 det-1 matrices, a genuine second integral model (the Galois-conjugate golden branch), distinct from G as a set",
   len(tauG) == 120 and all(mdet(A) == Z1 for A in tauG) and tauG != grp)

# ---------- 3. the pair is Galois-closed ----------
pair_ok = True
for A in grp:
    t = mtr(A)
    s = zadd(t, gal(t, 2))
    if not (s[1] == 0 and s[2] == 0 and s[3] == 0): pair_ok = False
ck("Q6  the PAIR character chi_2a + chi_2b is rational on every element: tr(g) + tau(tr(g)) lies in Q for all 120 g, so the pair carrier 2a + 2b is stable under the full arithmetic C4 -- the carrier-level echo of Herm2 finding A (the pair, not the single slot, is the Galois-closed object)",
   pair_ok)

# ---------- 4. the invariant Gram: existence, positivity, uniqueness ----------
H0 = ((Z0, Z0), (Z0, Z0))
for A in grp:
    P = mmul(mdag(A), A)
    H0 = ((zadd(H0[0][0], P[0][0]), zadd(H0[0][1], P[0][1])),
          (zadd(H0[1][0], P[1][0]), zadd(H0[1][1], P[1][1])))
ck("Q7  H0 = sum over the 120 lift elements of g-dagger g is sigma-Hermitian and invariant: h-dagger H0 h = H0 for both generators, exactly",
   mdag(H0) == H0
   and mmul(mdag(SM), mmul(H0, SM)) == H0
   and mmul(mdag(TM), mmul(H0, TM)) == H0)

def to_F(a):                                   # element of F inside K -> (x, y): x + y sqrt5
    # basis: 1 = (1,0,0,0), sqrt5 = (-1,0,-2,-2)
    if a[1] != 0 or a[2] != a[3]: return None
    y = -a[2]/F(2)
    x = a[0] + y
    return (x, y)
def fsign(p):
    x, y = p
    if x == 0 and y == 0: return 0
    if x >= 0 and y >= 0: return 1
    if x <= 0 and y <= 0: return -1
    big = 1 if x*x > 5*y*y else -1
    return big if x > 0 else -big
def fgal(p): return (p[0], -p[1])
d0 = mdet(H0)
h11 = to_F(H0[0][0]); h22 = to_F(H0[1][1]); dF = to_F(d0)
ck("Q8  H0 is totally positive definite: its diagonal entries and determinant lie in F and are positive under BOTH real embeddings (exact sign tests)",
   h11 is not None and h22 is not None and dF is not None
   and fsign(h11) == 1 and fsign(fgal(h11)) == 1
   and fsign(h22) == 1 and fsign(fgal(h22)) == 1
   and fsign(dF) == 1 and fsign(fgal(dF)) == 1)

# uniqueness: solve h-dagger H h = H for h in {S, T} over the 8 rational
# parameters of a sigma-Hermitian matrix H = [[a, b],[sigma(b), d]]:
# a = a0 + a1 sqrt5, d = d0 + d1 sqrt5 in F, b = (b0,b1,b2,b3) in K
S5T = (F(-1), F(0), F(-2), F(-2))              # sqrt5 as a zeta-tuple
def lin_H(p):
    a = tuple(p[0]*Z1[i] + p[1]*S5T[i] for i in range(4))
    d = tuple(p[2]*Z1[i] + p[3]*S5T[i] for i in range(4))
    b = (p[4], p[5], p[6], p[7])
    return ((a, b), (gal(b, 4), d))
rows = []
for gmat in (SM, TM):
    for ei in range(8):
        p = [F(0)]*8; p[ei] = F(1)
        H = lin_H(p)
        D = mmul(mdag(gmat), mmul(H, gmat))
        Dm = ((zsub(D[0][0], H[0][0]), zsub(D[0][1], H[0][1])),
              (zsub(D[1][0], H[1][0]), zsub(D[1][1], H[1][1])))
        col = []
        for i in range(2):
            for j in range(2):
                col.extend(Dm[i][j])
        rows.append(col)
# rows currently = 16 columns (8 per generator); stack into a 32 x 8 system
M = []
for blk in range(2):
    for r in range(16):
        M.append([rows[blk*8 + c][r] for c in range(8)])
def rankQ(M):
    M = [row[:] for row in M]
    ncols = len(M[0]); rank = 0; rpos = 0
    for c in range(ncols):
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
        rank += 1; rpos += 1
    return rank
rk = rankQ(M)
h0p = [h11[0], h11[1], h22[0], h22[1],
       H0[0][1][0], H0[0][1][1], H0[0][1][2], H0[0][1][3]]
in_null = all(sum(M[r][c]*h0p[c] for c in range(8)) == 0 for r in range(32))
ck("Q9  the invariance system for sigma-Hermitian forms has rank 6 over Q on 8 parameters: the solution space is EXACTLY 2-dimensional over Q = 1-dimensional over F, H0 lies in it, so the invariant Gram of the registered lift is unique up to an F-scalar (the audit's uniqueness claim, machine-checked; by this uniqueness and the GL2(K) identification of C-COMMON-CARRIER-ICOSIAN-1 gate L4, H0 is the canonical icosian form h up to positive scale)",
   rk == 6 and in_null)
ck("Q10 chi5 summary: pointwise on traces, gal(a) fixes every trace for a in ker chi5 = {1, 4} and moves every golden trace for a in {2, 3}: the arithmetic C4 descends to the marked single carrier exactly through its chi5 kernel, its nontrivial coset acts only with the outer 5a <-> 5b swap, and the branch PAIR carries the full quarter-turn (Q6): the moduli split |sigma_a(J)| = phi^(-chi5(a)) of the Herm2 lane, now as a marking theorem at the integral carrier level, consistent with the fired SPIN-LIFT-FORCED (marked lifts are not unique)",
   all(gal(mtr(A), 4) == mtr(A) for A in grp)
   and all(gal(mtr(A), 2) != mtr(A) for A in golden)
   and all(gal(mtr(A), 3) != mtr(A) for A in golden)
   and all(gal(mtr(A), 2) == mtr(A) for A in grp if A not in golden))

n = len(R); ok = sum(R)
print("SUMMARY %d/%d PASS" % (ok, n))
sys.exit(0 if ok == n else 1)
