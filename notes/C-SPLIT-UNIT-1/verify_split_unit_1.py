#!/usr/bin/env python3
# verify_split_unit_1.py
# Candidate C-SPLIT-UNIT-1, TWIST-J incubation lane. NON-CANONICAL, no authority.
# Basis: Public Canon v30 (tag canon-v30, content commit 857223fc..24ee0).
# Exact integer and Fraction arithmetic only. No float anywhere in this file.
# Run: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
#      python3 verify_split_unit_1.py
import sys
from fractions import Fraction as F
from itertools import product as iproduct

PASS = 0
FAIL = 0


def gate(gid, text, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("PASS %s %s" % (gid, text))
    else:
        FAIL += 1
        print("FAIL %s %s" % (gid, text))


# ---- Z[zeta_5], basis (1, z, z^2, z^3), z^4 = -(1+z+z^2+z^3) --------------
def red(c):
    c = list(c) + [0] * (8 - len(c))
    c[0] += c[5]
    c[1] += c[6]
    c[2] += c[7]
    q = c[4]
    return (c[0] - q, c[1] - q, c[2] - q, c[3] - q)


def zmul(a, b):
    c = [0] * 8
    for i in range(4):
        ai = a[i]
        if ai:
            for j in range(4):
                c[i + j] += ai * b[j]
    return red(c)


def zadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def zneg(a):
    return tuple(-x for x in a)


ONE = (1, 0, 0, 0)
ZERO = (0, 0, 0, 0)


def zpow5(k):
    k %= 5
    if k < 4:
        t = [0, 0, 0, 0]
        t[k] = 1
        return tuple(t)
    return (-1, -1, -1, -1)


def sigma(a, x):
    acc = ZERO
    for k in range(4):
        if x[k]:
            acc = zadd(acc, tuple(x[k] * t for t in zpow5(a * k)))
    return acc


def norm(x):
    p = ONE
    for a in (1, 2, 3, 4):
        p = zmul(p, sigma(a, x))
    if p[1] != 0 or p[2] != 0 or p[3] != 0:
        return None
    return p[0]


# ---- Z[phi] pairs a + b phi, phi^2 = 1 + phi ------------------------------
def qmul(p, q):
    a, b = p
    c, d = q
    return (a * c + b * d, a * d + b * c + b * d)


def qpow(n):
    r = (1, 0)
    step = (0, 1) if n >= 0 else (-1, 1)  # phi, or phi^-1 = phi - 1
    for _ in range(abs(n)):
        r = qmul(r, step)
    return r


def embed(p):
    a, b = p
    return (a, 0, -b, -b)  # a + b phi with phi = -z^2 - z^3


J = (1, 0, 1, 0)          # 1 + zeta^2
PHI = (0, 0, -1, -1)      # -zeta^2 - zeta^3
CHI5 = {1: 1, 2: -1, 3: -1, 4: 1}

print("C-SPLIT-UNIT-1 exact verifier. Basis Public Canon v30.")

# ---- A. ring sanity -------------------------------------------------------
gate("A1", "zeta^a zeta^(5-a) = 1 for a = 1, 2",
     zmul(zpow5(1), zpow5(4)) == ONE and zmul(zpow5(2), zpow5(3)) == ONE)
s = ZERO
for k in range(5):
    s = zadd(s, zpow5(k))
gate("A2", "Phi_5(zeta) = 0: 1 + zeta + ... + zeta^4 = 0", s == ZERO)
gate("A3", "phi^2 = 1 + phi transported through the embedding",
     zmul(PHI, PHI) == embed((1, 1)) and PHI == embed((0, 1)))

# ---- B. axiom anchors (failing input: replace J by 1 + zeta) --------------
gate("B1", "N(J) = 1", norm(J) == 1)
t = ZERO
for a in (1, 2, 3, 4):
    t = zadd(t, sigma(a, J))
gate("B2", "Tr(J) = 3", t == (3, 0, 0, 0))
gate("B3", "J phi = zeta (Canon anchor J . phi = j)", zmul(J, PHI) == zpow5(1))
jm1 = (0, 0, 1, 0)
gate("B4", "(J - 1)^3 = zeta", zmul(zmul(jm1, jm1), jm1) == zpow5(1))
j5 = ONE
for _ in range(5):
    j5 = zmul(j5, J)
gate("B5", "J^5 = phi^-5", j5 == embed(qpow(-5)))
gate("B6", "the failing input 1 + zeta does not satisfy the anchor J phi = j",
     zmul((1, 1, 0, 0), PHI) != zpow5(1))

# ---- C. size character: |sigma_a(J)|^2 = phi^(-2 chi5(a)) exactly ---------
for a in (1, 2, 3, 4):
    lhs = zmul(sigma(a, J), sigma(5 - a, J))
    rhs = embed(qpow(-2 * CHI5[a]))
    gate("C%d" % a, "sigma_%d(J) sigma_%d(J) = phi^(%d) exactly"
         % (a, 5 - a, -2 * CHI5[a]), lhs == rhs)
gate("C5", "the size partition is {1,4} vs {2,3}, not {1,2} vs {3,4}",
     zmul(sigma(1, J), sigma(4, J)) != zmul(sigma(2, J), sigma(3, J))
     and embed(qpow(-2)) != embed(qpow(2)))

# ---- D. Gauss sum of chi5 -------------------------------------------------
g = ZERO
for a in (1, 2, 3, 4):
    term = zpow5(a)
    if CHI5[a] < 0:
        term = zneg(term)
    g = zadd(g, term)
gate("D1", "sum chi5(a) zeta^a = 2 phi - 1", g == embed((-1, 2)))
gate("D2", "(2 phi - 1)^2 = 5", zmul(g, g) == (5, 0, 0, 0))
tw_ok = True
for b in (1, 2, 3, 4):
    gb = ZERO
    for a in (1, 2, 3, 4):
        term = zpow5(a * b)
        if CHI5[a] < 0:
            term = zneg(term)
        gb = zadd(gb, term)
    want = g if CHI5[b] > 0 else zneg(g)
    tw_ok = tw_ok and gb == want
gate("D3", "twist: sum chi5(a) zeta^(ab) = chi5(b) (2 phi - 1) for all b", tw_ok)

# ---- E. orbit forcing: units of the form 1 + torsion ----------------------
torsion = []
for k in range(5):
    torsion.append(zpow5(k))
    torsion.append(zneg(zpow5(k)))
found = []
norms = {}
for w in torsion:
    x = zadd(ONE, w)
    if x == ZERO:
        norms[w] = 0
        continue
    n = norm(x)
    norms[w] = n
    if n in (1, -1):
        found.append(w)
orbit = {zpow5(1), zpow5(2), zpow5(3), zpow5(4)}
gate("E1", "units among 1 + mu_10 are exactly the four 1 + zeta^k",
     set(found) == orbit and len(found) == 4)
gate("E2", "the six failures fail with norms 16 (w=1), 5 (w=-zeta^k), 0 (w=-1)",
     norms[ONE] == 16
     and all(norms[zneg(zpow5(k))] == 5 for k in range(1, 5))
     and norms[zneg(ONE)] == 0)
gate("E3", "the four are one Galois orbit: sigma_a(J) = 1 + zeta^(2a)",
     all(sigma(a, J) == zadd(ONE, zpow5(2 * a)) for a in (1, 2, 3, 4))
     and {sigma(a, J) for a in (1, 2, 3, 4)}
     == {zadd(ONE, w) for w in orbit})

# ---- F. bit uniqueness ----------------------------------------------------
Gset = (1, 2, 3, 4)
subs = []
from itertools import combinations
for size in (0, 1, 2, 3):
    for c in combinations((2, 3, 4), size):
        cand = {1} | set(c)
        if all((x * y) % 5 in cand for x in cand for y in cand):
            subs.append(frozenset(cand))
gate("F1", "subgroups of (Z/5)^x are {1}, {1,4}, G: one subgroup of index 2",
     set(subs) == {frozenset({1}), frozenset({1, 4}), frozenset({1, 2, 3, 4})}
     and [s for s in subs if len(s) == 2] == [frozenset({1, 4})])
gate("F2", "{1,4} = squares mod 5 = {+-1} mod 5",
     {(a * a) % 5 for a in Gset} == {1, 4} == {1 % 5, (-1) % 5})
# characters: chi(2) in {1, i, -1, -i} as Gaussian pairs (re, im)
ORD2 = {1: 0, 2: 1, 4: 2, 3: 3}  # discrete log base 2 in (Z/5)^x
def gmulc(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])
chars = []
for t in range(4):  # chi(2) = i^t, chi(a) = (i^t)^(log_2 a)
    chi = {}
    for a in Gset:
        e = (t * ORD2[a]) % 4
        chi[a] = [(1, 0), (0, 1), (-1, 0), (0, -1)][e]
    if all(chi[(x * y) % 5] == gmulc(chi[x], chi[y]) for x in Gset for y in Gset):
        chars.append(chi)
real = [c for c in chars if all(v[1] == 0 for v in c.values())]
nontrivial_real = [c for c in real if any(v != (1, 0) for v in c.values())]
gate("F3", "exactly 4 characters, exactly 2 real, one nontrivial real = chi5",
     len(chars) == 4 and len(real) == 2 and len(nontrivial_real) == 1
     and all(nontrivial_real[0][a] == (CHI5[a], 0) for a in Gset))
gate("F4", "sector census: doublet count (p-3)/2 over p in {3,5,7,13} is "
     "(0,1,2,5); exactly one doublet only at p = 5",
     [(p - 3) // 2 for p in (3, 5, 7, 13)] == [0, 1, 2, 5]
     and [(p - 1) // 2 == 2 for p in (3, 5, 7, 13)] == [False, True, False, False])

# ---- G. argument sector (principal branch, exact rationals times pi) ------
r = {}
for a in (1, 2, 3, 4):
    k = (2 * a) % 5
    r[a] = F(k, 5) if k in (1, 2) else F(k - 5, 5)
gate("G1", "r = (2, -1, 1, -2)/5",
     [r[a] for a in (1, 2, 3, 4)] == [F(2, 5), F(-1, 5), F(1, 5), F(-2, 5)])
gate("G2", "trivial component of the argument vector is 0: sum r_a = 0",
     sum(r.values()) == 0)
gate("G3", "chi5 component of the argument vector is 0: sum chi5(a) r_a = 0",
     sum(CHI5[a] * r[a] for a in Gset) == 0)
gate("G4", "conjugation-odd: r_a = -r_(5-a)",
     all(r[a] == -r[5 - a] for a in Gset))
chi_i = {}
for a in Gset:
    e = ORD2[a] % 4
    chi_i[a] = [(1, 0), (0, 1), (-1, 0), (0, -1)][e]  # chi(2) = i
gate("G5", "5 r_a = Re[(2 + i) chi(a)] with chi(2) = i",
     all(5 * r[a] == 2 * chi_i[a][0] - chi_i[a][1] for a in Gset))
gate("G6", "ratio identity sigma_a(J) = zeta^(2a) sigma_(5-a)(J)",
     all(sigma(a, J) == zmul(zpow5(2 * a), sigma(5 - a, J)) for a in Gset))
gate("G7", "half-plane bookkeeping: r_a > 0 iff 2a mod 5 in {1,2}",
     all((r[a] > 0) == ((2 * a) % 5 in (1, 2)) for a in Gset))

# ---- H. unit scan, coefficient box [-4,4]^4 -------------------------------
POW = {}
for m in range(-60, 61):
    POW[qpow(m)] = m
count = 0
bad = 0
seenJ = False
for co in iproduct(range(-4, 5), repeat=4):
    if co == ZERO:
        continue
    n = norm(co)
    if n not in (1, -1):
        continue
    count += 1
    if co == J:
        seenJ = True
    x = zmul(co, sigma(4, co))
    if x[1] != 0 or x[2] != x[3]:
        bad += 1
        continue
    m = POW.get((x[0], -x[2]))
    if m is None or m % 2 != 0:
        bad += 1
        continue
    y = zmul(sigma(2, co), sigma(3, co))
    if y[1] != 0 or y[2] != y[3] or POW.get((y[0], -y[2])) != -m:
        bad += 1
gate("H1", "every unit in the box lies on the chi5 size line, quantized in "
     "even phi powers, with the inverse pair product", bad == 0)
gate("H2", "witness counts: units found even, at least 10, J present "
     "(count = %d)" % count, count % 2 == 0 and count >= 10 and seenJ)
u0 = (1, -1, 0, 0)  # 1 - zeta, the constructed non-unit
x0 = zmul(u0, sigma(4, u0))
gate("H3", "constructed failing input: 1 - zeta has norm 5 and size datum "
     "3 - phi, which is not a phi power",
     norm(u0) == 5 and x0 == (3, 0, 1, 1)
     and POW.get((3, -1)) is None)
gate("H4", "J sits at quantum m = -1: J conj(J) = phi^-2 and |m| = 1 is the "
     "least nonzero even half",
     zmul(J, sigma(4, J)) == embed(qpow(-2)) and POW[qpow(-2)] == -2)

# ---- I. the zero-outward skeleton ----------------------------------------
gate("I1", "sum of the nontrivial character over the whole group is 0",
     sum(CHI5[a] for a in Gset) == 0)
P = ((F(1), F(0)), (F(0), F(0)))
Q = ((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)))
def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))
def msub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(2)) for i in range(2))
C = msub(mmul(P, Q), mmul(Q, P))
gate("I2", "projectors with [P,Q] != 0 and Tr[P,Q] = 0 exactly",
     mmul(Q, Q) == Q and any(any(v != 0 for v in row) for row in C)
     and C[0][0] + C[1][1] == 0)
# conjugation permutation on the four embeddings: a <-> 5 - a
perm = {0: 3, 1: 2, 2: 1, 3: 0}
Pm = tuple(tuple(F(1) if perm[i] == j else F(0) for j in range(4))
           for i in range(4))
Iden = tuple(tuple(F(1) if i == j else F(0) for j in range(4))
             for i in range(4))
def m4(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))
def mhalf(A, B, sgn):
    return tuple(tuple((A[i][j] + sgn * B[i][j]) / 2 for j in range(4))
                 for i in range(4))
ep = mhalf(Iden, Pm, 1)
em = mhalf(Iden, Pm, -1)
zero4 = tuple(tuple(F(0) for _ in range(4)) for _ in range(4))
eps = tuple(tuple(ep[i][j] - em[i][j] for j in range(4)) for i in range(4))
gate("I3", "e+- = (1 +- c)/2 idempotent, orthogonal, sum 1; (e+ - e-)^2 = 1",
     m4(ep, ep) == ep and m4(em, em) == em and m4(ep, em) == zero4
     and tuple(tuple(ep[i][j] + em[i][j] for j in range(4))
               for i in range(4)) == Iden
     and m4(eps, eps) == Iden)

print("GATES %d PASS %d FAIL %d" % (PASS + FAIL, PASS, FAIL))
print("RESULT: %s" % ("ALL PASS" if FAIL == 0 else "FAILURES PRESENT"))
sys.exit(0 if FAIL == 0 else 1)
