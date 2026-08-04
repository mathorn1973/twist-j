#!/usr/bin/env python3
# break_photon_point_group_1.py
# C-PHOTON-POINT-GROUP-1, incubation self-break pass. CANDIDATE, no authority.
# Independent code paths; nothing imported from, and no code shared with, the
# verifier. Attempts to refute G1 to G7 of the frozen preregistration:
#   B1  axes-forced completeness proof for the D_3 point group (kills any
#       hypothetical 49th element, including non-integer-matrix ones, which
#       the verifier's basis-image enumeration could conceivably miss)
#   B2  the literature order formula |O_3(q)| = 2 q (q^2 - 1) against an
#       independent ROW-condition enumeration of O(F_5^3, A mod 5)
#   B3  Molien / power-sum route to the degree-4 invariant dimension
#   B4  the harmonic identity a(S) = (5 M_xxxx - |S| N^2) / 2 against the
#       direct definition, plus invariance premises
#   B5  second enumeration of the D_3 point group from a different frozen
#       basis, with standard-coordinate matrices recovered exactly
# Exact arithmetic only. Deterministic environment-free stdout.

import sys
from fractions import Fraction
from itertools import permutations, product

res, dem = [], []

def gate(name, ok, data):
    res.append(ok)
    print("%s %s %s" % (name, "PASS" if ok else "FAIL", data))

def demo(name, fired, data):
    dem.append(fired)
    print("%s %s %s" % (name, "FIRED" if fired else "NOT-FIRED", data))

def dotv(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]

def sperm_all():
    out = []
    for p in permutations(range(3)):
        for s in product((1, -1), repeat=3):
            out.append(tuple(tuple(s[i] if p[i] == j else 0 for j in range(3))
                             for i in range(3)))
    return sorted(set(out))

def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
                 for i in range(3))

def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

# ---------------------------------------------------------------- B1
# Premise P1: the norm-4 shell of D_3 is exactly {+-2 e_i}.
# Premise P2: {2 e_1, 2 e_2, 2 e_3} spans Q^3.
# Deduction: an isometry g of (D_3, dot) permutes the norm-4 shell, so
# g(2 e_i) = +-2 e_pi(i); by Q-linearity g(e_i) = +-e_pi(i); a linear map
# fixed on a spanning set by these values IS a signed permutation matrix.
# Hence Aut(D_3) is contained in the 48 signed permutations. Lower bound:
# every signed permutation is orthogonal and preserves the parity of the
# coordinate sum, hence preserves D_3. Together |Aut(D_3)| = 48 exactly.

shell4 = sorted(v for v in product(range(-2, 3), repeat=3)
                if sum(x * x for x in v) == 4 and sum(v) % 2 == 0)
axes = sorted(t for i in range(3) for t in
              (tuple(2 * (j == i) for j in range(3)),
               tuple(-2 * (j == i) for j in range(3))))
p1 = shell4 == axes
span = det3(((2, 0, 0), (0, 2, 0), (0, 0, 2)))
p2 = span != 0

SP = sperm_all()
orth = all(mmul(tuple(zip(*M)), M) == ((1, 0, 0), (0, 1, 0), (0, 0, 1)) for M in SP)
d3basis = ((1, 1, 0), (1, -1, 0), (0, 1, 1))
closed = all(all(sum(sum(M[i][k] * b[k] for k in range(3)) for i in range(3)) % 2 == 0
                 for b in d3basis) for M in SP)
b1 = p1 and p2 and len(SP) == 48 and orth and closed
gate("B1", b1, "shell4=axes:%s span_det=%d signed_perms=%d orthogonal=%s preserve_D3=%s"
     % (p1, span, len(SP), orth, closed))
print("B1 deduction: isometry permutes the norm-4 shell => g(e_i) = +-e_pi(i)"
      " on a spanning set => g is a signed permutation; ceiling 48 meets floor 48.")

# ---------------------------------------------------------------- B2

q = 5
A5 = ((2, 4, 0), (4, 2, 4), (0, 4, 2))
formula = 2 * q * (q * q - 1)

vecs = sorted(product(range(q), repeat=3))
def bilr(u, v):
    return sum(u[i] * A5[i][j] * v[j] for i in range(3) for j in range(3)) % q

# ROW condition: M A5 M^T = A5, rows enumerated
r1s = [v for v in vecs if bilr(v, v) == A5[0][0]]
cnt = 0
order5 = 0
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
def mmul5(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) % q for j in range(3))
                 for i in range(3))
for r1 in r1s:
    r2s = [v for v in vecs if bilr(v, v) == A5[1][1] and bilr(r1, v) == A5[0][1]]
    for r2 in r2s:
        for r3 in vecs:
            if (bilr(r3, r3) == A5[2][2] and bilr(r1, r3) == A5[0][2]
                    and bilr(r2, r3) == A5[1][2]):
                M = (r1, r2, r3)
                cnt += 1
                P2 = mmul5(M, M)
                P4 = mmul5(P2, P2)
                if mmul5(P4, M) == I3 and M != I3:
                    order5 += 1
b2 = (cnt == formula == 240 and order5 == 24)
gate("B2", b2, "row_count=%d formula=%d order5(g^5=I,g!=I)=%d" % (cnt, formula, order5))

# ---------------------------------------------------------------- B3
# Molien by power sums: dim Inv_4 = (1/|G|) sum_g h4, with p_k = tr(g^k),
# h4 = (p1^4 + 6 p1^2 p2 + 3 p2^2 + 8 p1 p3 + 6 p4) / 24.

def tr(M):
    return M[0][0] + M[1][1] + M[2][2]

tot = Fraction(0)
for g in SP:
    g2 = mmul(g, g)
    g3 = mmul(g2, g)
    g4 = mmul(g3, g)
    p1, p2m, p3m, p4m = tr(g), tr(g2), tr(g3), tr(g4)
    h4 = Fraction(p1 ** 4 + 6 * p1 ** 2 * p2m + 3 * p2m ** 2 + 8 * p1 * p3m
                  + 6 * p4m, 24)
    tot += h4
molien = tot / len(SP)
b3 = molien == 2
gate("B3", b3, "molien_dim_deg4=%s" % molien)

# ---------------------------------------------------------------- B4

FROZEN_A = (-4, 32, -72, -64)
box = [v for v in product(range(-3, 4), repeat=3)
       if 0 < sum(x * x for x in v) <= 8 and sum(v) % 2 == 0]
vals = []
inv_prem = True
ident_ok = True
for idx, N in enumerate((2, 4, 6, 8)):
    S = sorted(v for v in box if sum(x * x for x in v) == N)
    orbit_closed = all(tuple(sum(M[i][k] * v[k] for k in range(3)) for i in range(3))
                       in set(S) for v in S for M in SP)
    if not orbit_closed:
        inv_prem = False
    mxxxx = sum(v[0] ** 4 for v in S)
    mxxyy = sum(v[0] ** 2 * v[1] ** 2 for v in S)
    direct = mxxxx - 3 * mxxyy
    ident = Fraction(5 * mxxxx - len(S) * N * N, 2)
    if ident != direct:
        ident_ok = False
    vals.append(direct)
b4 = tuple(vals) == FROZEN_A and inv_prem and ident_ok
gate("B4", b4, "a=%s orbit_closed=%s identity=%s" % (tuple(vals), inv_prem, ident_ok))

# ---------------------------------------------------------------- B5

G2B = ((1, 1, 0), (1, -1, 0), (0, 1, 1))          # frozen second basis
GRAM2 = tuple(tuple(dotv(G2B[i], G2B[j]) for j in range(3)) for i in range(3))
minvecs = sorted(v for v in box if sum(x * x for x in v) == 2)
Bcols = tuple(tuple(G2B[j][i] for j in range(3)) for i in range(3))   # columns g_i
dB = det3(Bcols)

def inv_frac(M):
    d = Fraction(det3(M))
    return tuple(tuple(
        Fraction((M[(j + 1) % 3][(i + 1) % 3] * M[(j + 2) % 3][(i + 2) % 3]
                  - M[(j + 1) % 3][(i + 2) % 3] * M[(j + 2) % 3][(i + 1) % 3])) / d
        for j in range(3)) for i in range(3))

Binv = inv_frac(Bcols)
found = set()
std_all_sperm = True
for t in product(minvecs, repeat=3):
    ok = True
    for i in range(3):
        for j in range(3):
            if dotv(t[i], t[j]) != GRAM2[i][j]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        continue
    V = tuple(tuple(t[j][i] for j in range(3)) for i in range(3))     # columns v_i
    Mstd = mmul(tuple(tuple(Fraction(x) for x in r) for r in V), Binv)
    ints = all(x.denominator == 1 for r in Mstd for x in r)
    if not ints:
        std_all_sperm = False
        continue
    Mi = tuple(tuple(int(x) for x in r) for r in Mstd)
    if Mi not in set(SP):
        std_all_sperm = False
    found.add(Mi)
b5 = len(found) == 48 and std_all_sperm and sorted(found) == SP
gate("B5", b5, "second_basis_count=%d all_signed_perms=%s |detB|=%d"
     % (len(found), std_all_sperm and sorted(found) == SP, abs(dB)))

# ------------------------------------------------- breaker's own demos

print("-- breaker expected-fail demonstrations --")
demo("BD1", det3(((2, 0, 0), (0, 2, 0), (0, 0, 0))) == 0,
     "rank-2 axis set fails the spanning premise")
demo("BD2", 239 != formula, "a miscount 239 is caught by the formula")
rotC4 = ((0, 1, 0), (-1, 0, 0), (0, 0, 1))
gg, tot4 = I3, Fraction(0)
for _ in range(4):
    gg = mmul(gg, rotC4)
    h2 = mmul(gg, gg)
    h3 = mmul(h2, gg)
    h4m = mmul(h3, gg)
    a, b, c, d = tr(gg), tr(h2), tr(h3), tr(h4m)
    tot4 += Fraction(a ** 4 + 6 * a * a * b + 3 * b * b + 8 * a * c + 6 * d, 24)
demo("BD3", tot4 / 4 != 2, "Molien on C4 gives %s, not 2" % (tot4 / 4))
sx = [(1, 0, 0)]
demo("BD4", Fraction(5 * 1 - 1 * 1, 2) != (1 - 0),
     "harmonic identity fails on a non-invariant set")
demo("BD5", dotv((1, 1, 0), (1, 1, 0)) != GRAM2[0][1],
     "a repeated-vector triple is rejected by the Gram filter")

ok = all(res) and all(dem)
print("BREAK GATES %d/%d PASS, DEMOS %d/%d FIRED, VERDICT %s"
      % (sum(res), len(res), sum(dem), len(dem),
         "NO BREAK FOUND" if ok else "BREAK OR DEFECT"))
sys.exit(0 if ok else 1)
