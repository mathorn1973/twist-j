#!/usr/bin/env python3
# verify_r3_w4_minimal_point.py
# Support computation for OWNER RULING R3 (2026-08-05): the frozen W4
# working point of the photon transfer data. RULING SUPPORT GRADE:
# exact integer arithmetic throughout (Fraction only for the two
# displayed Taylor coefficients), deterministic, stdlib only, single
# file. No candidate id, no probe, no authority. ONE AMBIENT: Z^3. No
# finite-field object appears anywhere in this script.
#
# Ruled objects (displayed):
#   SHELL FAMILY  the full norm shells of Z^3 for norms {2,4,8,10,16},
#                 the symmetric completion of the machine's deposited
#                 alphabet. Equality of the completion with these full
#                 shells is the moment recon's N4, cited not
#                 recomputed; sizes and single-orbit structure ARE
#                 recomputed here from scratch.
#   CRITERION     admissible weight vectors w = (w2,w4,w8,w10,w16) are
#                 integer, every entry >= 1 (every deposited shell
#                 participates), and satisfy the N6 cone
#                   -4 w2 + 32 w4 - 64 w8 + 440 w10 + 512 w16 = 0.
#                 Selected is the admissible point of minimal total
#                 sum(w); ties broken lexicographically in the order
#                 (w2, w4, w8, w10, w16).
#   CLAIM         the selected point is unique: W* = (6, 1, 15, 1, 1),
#                 total 24, tie-break displayed and unused.
import sys
from fractions import Fraction
from itertools import product, permutations
from math import comb, gcd

OK = []
def chk(name, ok, data):
    OK.append(ok)
    print("%s %s %s" % (name, "PASS" if ok else "FAIL", data))
def note(name, data):
    print("%s NOTE %s" % (name, data))

NORMS = (2, 4, 8, 10, 16)
A_DISPLAY = (-4, 32, -64, 440, 512)
WSTAR = (6, 1, 15, 1, 1)

# X1: rebuild the shells by direct box enumeration. Any coordinate
# with absolute value >= 5 forces norm >= 25 > 16, so the box -4..4
# is provably sufficient.
BOX = list(range(-4, 5))
shells = {n: [] for n in NORMS}
for v in product(BOX, repeat=3):
    n = v[0] * v[0] + v[1] * v[1] + v[2] * v[2]
    if n in shells:
        shells[n].append(v)
for n in NORMS:
    shells[n] = sorted(shells[n])
sizes = tuple(len(shells[n]) for n in NORMS)
chk("X1", sizes == (12, 6, 12, 24, 6),
    "shell sizes on norms %s: %s" % (NORMS, sizes))

# X2: every vector of the family has even coordinate sum. FCC (D_3)
# membership is a verified property here, not an input.
allv = [v for n in NORMS for v in shells[n]]
chk("X2", all(sum(v) % 2 == 0 for v in allv),
    "all %d vectors have even coordinate sum" % len(allv))

# X3: each shell is ONE orbit of the 48 signed permutations, with its
# representative displayed. The named failing input for this gate
# shape is the norm-9 shell of Z^3, which splits (X3f).
def sperm_all():
    out = []
    for p in permutations(range(3)):
        for s in product((1, -1), repeat=3):
            out.append(tuple(tuple(s[i] if p[i] == j else 0
                                   for j in range(3)) for i in range(3)))
    return out
SP = sperm_all()
def act(M, v):
    return tuple(sum(M[i][k] * v[k] for k in range(3)) for i in range(3))
def orbit_of(v):
    return set(act(M, v) for M in SP)
one_orbit = all(orbit_of(shells[n][0]) == set(shells[n]) for n in NORMS)
reps = {}
for n in NORMS:
    r = set(tuple(sorted((abs(x) for x in v), reverse=True))
            for v in shells[n])
    reps[n] = sorted(r)
rep_ok = all(len(reps[n]) == 1 for n in NORMS)
chk("X3", one_orbit and rep_ok,
    "each shell is a single 48-orbit; representatives %s"
    % sorted((n, reps[n][0]) for n in NORMS))
n9 = sorted(v for v in product(BOX, repeat=3)
            if v[0] * v[0] + v[1] * v[1] + v[2] * v[2] == 9)
seen = set()
orbs9 = []
for v in n9:
    if v not in seen:
        o = orbit_of(v)
        seen |= o
        orbs9.append(len(o))
chk("X3f", len(n9) == 30 and sorted(orbs9) == [6, 24],
    "named failing input: the norm-9 shell (30 vectors) splits into "
    "orbits of sizes %s and would FAIL the one-orbit gate"
    % sorted(orbs9))

# M1: per-shell fourth-order data, coordinate-balanced, and the
# deficit vector a_n = A_n - 3 B_n, matching the display of N6.
def msum(vs, exps, w=1):
    t = 0
    for v in vs:
        r = w
        for x, e in zip(v, exps):
            r *= x ** e
        t += r
    return t
A4, B22 = [], []
balanced = True
for n in NORMS:
    ac = [msum(shells[n], e) for e in ((4, 0, 0), (0, 4, 0), (0, 0, 4))]
    bp = [msum(shells[n], e) for e in ((2, 2, 0), (2, 0, 2), (0, 2, 2))]
    if len(set(ac)) != 1 or len(set(bp)) != 1:
        balanced = False
    A4.append(ac[0])
    B22.append(bp[0])
a_vec = tuple(A - 3 * B for A, B in zip(A4, B22))
chk("M1", balanced and a_vec == A_DISPLAY,
    "per-shell (A, B) = %s, deficit vector a = %s matches the display"
    % (list(zip(A4, B22)), a_vec))
chk("M2", sum(a_vec) == 916,
    "uniform weights miss the cone by exactly 916, reproducing N5")

# C1: the candidate point is admissible.
def cone(w):
    return sum(a * x for a, x in zip(A_DISPLAY, w))
chk("C1", cone(WSTAR) == 0 and min(WSTAR) >= 1,
    "W* = %s is admissible: all entries >= 1, cone value 0" % (WSTAR,))

# C2: enumeration path A, the proof leg. ALL positive integer
# 5-tuples with total <= 24 (the candidate's total) are enumerated in
# lexicographic order; any admissible point of total <= 24 appears.
sols = []
for w2 in range(1, 21):
    for w4 in range(1, 22 - w2):
        for w8 in range(1, 23 - w2 - w4):
            for w10 in range(1, 24 - w2 - w4 - w8):
                for w16 in range(1, 25 - w2 - w4 - w8 - w10):
                    w = (w2, w4, w8, w10, w16)
                    if cone(w) == 0:
                        sols.append(w)
chk("C2", sols == [WSTAR],
    "exhaustive over all positive 5-tuples with total <= 24: "
    "admissible points found %s; W* is the unique minimizer at total "
    "24 and the lexicographic tie-break is unused" % (sols,))

# C3: enumeration path B, independent structure. Eliminate w2 through
# the equivalent integer identity (the cone divided by -4)
#   w2 = 8 w4 - 16 w8 + 110 w10 + 128 w16,
# scan the reduced variables on a wide box, verify the identity on
# the whole box, minimize the reconstructed total.
best = None
ident_ok = True
for w4 in range(1, 8):
    for w8 in range(1, 61):
        for w10 in range(1, 8):
            for w16 in range(1, 8):
                w2 = 8 * w4 - 16 * w8 + 110 * w10 + 128 * w16
                if cone((w2, w4, w8, w10, w16)) != 0:
                    ident_ok = False
                if w2 >= 1:
                    t = w2 + w4 + w8 + w10 + w16
                    cand = (t, (w2, w4, w8, w10, w16))
                    if best is None or cand < best:
                        best = cand
chk("C3", ident_ok and best == (24, WSTAR),
    "independent elimination scan agrees: minimum total 24 at %s"
    % (best[1],))

# C4: the named failing inputs of the two gates above, constructed.
UNIF = (1, 1, 1, 1, 1)
CONTRAST = (230, 1, 1, 1, 1)
chk("C4", cone(UNIF) == 916 and cone(CONTRAST) == 0
        and sum(CONTRAST) == 234,
    "uniform %s misses the cone by 916 (fails admissibility); "
    "%s lies on the cone with total 234 > 24 (fails minimality)"
    % (UNIF, CONTRAST))

# W-block: exact witnesses at W*.
WMAP = dict(zip(NORMS, WSTAR))
mass = sum(WMAP[n] * len(shells[n]) for n in NORMS)
chk("W1", mass == 288, "total mass sum w_n |S_n| = %d" % mass)

def poly_dict(m):
    # coefficient dict of sum_v w(v) <k,v>^m as a polynomial in
    # (k_x, k_y, k_z): key = exponent triple, value = integer coeff
    d = {}
    for i in range(m + 1):
        for j in range(m + 1 - i):
            l = m - i - j
            c = comb(m, i) * comb(m - i, j)
            s = 0
            for n in NORMS:
                s += WMAP[n] * msum(shells[n], (i, j, l))
            if c * s != 0:
                d[(i, j, l)] = c * s
    return d
def iso_dict(m):
    # coefficient dict of |k|^m for even m
    h = m // 2
    d = {}
    for i in range(h + 1):
        for j in range(h + 1 - i):
            l = h - i - j
            d[(2 * i, 2 * j, 2 * l)] = comb(h, i) * comb(h - i, j)
    return d
def scale(d, c):
    return dict((k, c * v) for k, v in d.items())

d2 = poly_dict(2)
chk("W2", d2 == scale(iso_dict(2), 648),
    "sum w <k,v>^2 = 648 |k|^2 exactly (M2 = 648 I); coefficients %s"
    % sorted(d2.items()))
d4 = poly_dict(4)
chk("W3", d4 == scale(iso_dict(4), 3168),
    "sum w <k,v>^4 = 3168 |k|^4 exactly; pure quartic 3168 = 3 x "
    "1056 = three times the square-pair moment")
c2 = Fraction(648, 2)
c4 = Fraction(3168, 24)
chk("W4", c2 == 324 and c4 == 132,
    "symbol S(k) = sum w (cos<k,v> - 1) = -324 |k|^2 + 132 |k|^4 + "
    "R6 with exact Taylor coefficients 648/2 and 3168/24; isotropic "
    "through fourth order")
d6 = poly_dict(6)
iso6 = scale(iso_dict(6), d6[(6, 0, 0)])
chk("W5", d6[(6, 0, 0)] == 21888 and d6[(4, 2, 0)] == 63360
        and (2, 2, 2) not in d6 and d6 != iso6,
    "sixth order ANISOTROPIC, exact display: k^6-type 21888, "
    "k^4k^2-type 63360 where isotropy would need 65664, k^2k^2k^2 "
    "absent where isotropy would need 131328; every vector of the "
    "family has a zero coordinate, so the triple-product moment "
    "vanishes identically")
chk("W6", gcd(*WSTAR) == 1,
    "W* is primitive (gcd 1); the overall scale of W is a cone "
    "direction not fixed by isotropy, fixed here by integrality and "
    "minimality; its physical pairing with the time leg is K3 "
    "material, named and not ruled")

ok = all(OK)
print("R3 W4 MINIMAL POINT: %d/%d checks PASS, VERDICT %s"
      % (sum(OK), len(OK), "COMPLETE" if ok else "DEFECT"))
sys.exit(0 if ok else 1)
