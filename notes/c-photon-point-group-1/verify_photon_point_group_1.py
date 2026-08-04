#!/usr/bin/env python3
# verify_photon_point_group_1.py
# C-PHOTON-POINT-GROUP-1, incubation lane. CANDIDATE verifier, no authority.
# Frozen by PREREG-C-PHOTON-POINT-GROUP-1_2026-08-04.md (sha256 01988776...).
# Python 3 stdlib only. Exact arithmetic (int, Fraction). No float anywhere.
# stdout is deterministic and environment-free (byte-identical across
# architectures is the requirement).

import sys
from fractions import Fraction
from itertools import permutations, product

# ---------------------------------------------------------------- helpers

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))

def mat_mul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n))
                       for j in range(n)) for i in range(n))

def mat_vec(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A)))

def mat_id(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))

def mat_det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

def mat_order(M, cap):
    P = M
    for k in range(1, cap + 1):
        if P == mat_id(len(M)):
            return k
        P = mat_mul(P, M)
    return None

def mat_mul_mod(A, B, m):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) % m
                       for j in range(n)) for i in range(n))

def mat_order_mod(M, m, cap):
    I = mat_id(len(M))
    P = M
    for k in range(1, cap + 1):
        if P == I:
            return k
        P = mat_mul_mod(P, M, m)
    return None

def gauss_rank(rows):
    rows = [list(r) for r in rows]
    nrows, ncols = len(rows), len(rows[0])
    rank, pr = 0, 0
    for c in range(ncols):
        piv = None
        for r in range(pr, nrows):
            if rows[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        rows[pr], rows[piv] = rows[piv], rows[pr]
        pv = rows[pr][c]
        rows[pr] = [x / pv for x in rows[pr]]
        for r in range(nrows):
            if r != pr and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[pr])]
        pr += 1
        rank += 1
    return rank

results = []
def gate(name, ok, data):
    results.append(ok)
    print(("%s %s %s") % (name, "PASS" if ok else "FAIL", data))

demos = []
def demo(name, fired, data):
    demos.append(fired)
    print(("%s %s %s") % (name, "FIRED" if fired else "NOT-FIRED", data))

# ---------------------------------------------------------------- objects

CART = ((2, -1, 0), (-1, 2, -1), (0, -1, 2))

# A_3 side: L = sum-zero vectors of Z^4, basis b1=e1-e2, b2=e2-e3, b3=e3-e4.
def e4(i):
    return tuple(1 if k == i else 0 for k in range(4))

def sub4(u, v):
    return tuple(a - b for a, b in zip(u, v))

B4 = (sub4(e4(0), e4(1)), sub4(e4(1), e4(2)), sub4(e4(2), e4(3)))

def to_basis(x):
    # x in Z^4, sum zero -> coordinates in basis B4
    return (x[0], x[0] + x[1], x[0] + x[1] + x[2])

ROOTS4 = sorted(sub4(e4(i), e4(j)) for i in range(4) for j in range(4) if i != j)
ROOTS_B = sorted(to_basis(r) for r in ROOTS4)

# sanity of the frozen basis Gram (prints as data inside G1)
BASIS_GRAM_OK = all(dot(B4[i], B4[j]) == CART[i][j] for i in range(3) for j in range(3))

# ------------------------------------------------------------------- G1

def gram_of_triple(t):
    return tuple(tuple(dot(t[i], t[j]) for j in range(3)) for i in range(3))

aut = []
for t in product(ROOTS4, repeat=3):
    if gram_of_triple(t) == CART:
        M = tuple(tuple(to_basis(t[c])[r] for c in range(3)) for r in range(3))
        aut.append(M)
aut = sorted(set(aut))

# every element maps the root set bijectively onto itself
roots_closed = all(sorted(mat_vec(M, r) for r in ROOTS_B) == ROOTS_B for M in aut)
dets = sorted(set(mat_det3(M) for M in aut))

# the 48 candidates eps * P_sigma, expressed in basis coordinates
signed_perm4 = []
for eps in (1, -1):
    for sig in permutations(range(4)):
        imgs = []
        for (i, j) in ((0, 1), (1, 2), (2, 3)):
            v = sub4(e4(sig[i]), e4(sig[j]))
            imgs.append(to_basis(tuple(eps * c for c in v)))
        M = tuple(tuple(imgs[c][r] for c in range(3)) for r in range(3))
        signed_perm4.append(M)
signed_perm4 = sorted(set(signed_perm4))

g1 = (len(aut) == 48 and aut == signed_perm4 and roots_closed
      and dets == [-1, 1] and BASIS_GRAM_OK)
gate("G1", g1, "|Aut|=%d eq_pmPsigma=%s roots_closed=%s dets=%s basis_gram=%s"
     % (len(aut), aut == signed_perm4, roots_closed, dets, BASIS_GRAM_OK))

# ------------------------------------------------------------------- G2

order_count = {}
for M in aut:
    o = mat_order(M, 60)
    order_count[o] = order_count.get(o, 0) + 1
FROZEN_ORDERS = {1: 1, 2: 19, 3: 8, 4: 12, 6: 8}
g2 = order_count == FROZEN_ORDERS
gate("G2", g2, "orders=%s frozen=%s" % (sorted(order_count.items()),
                                        sorted(FROZEN_ORDERS.items())))

# ------------------------------------------------------------------- G3

T = ((1, 0, -1), (-1, 1, -1), (0, -1, 0))   # columns f1=(1,-1,0), f2=(0,1,-1), f3=(-1,-1,0)
detT = mat_det3(T)

def mat_inv3_frac(M):
    d = Fraction(mat_det3(M))
    c = [[Fraction((M[(j+1)%3][(i+1)%3] * M[(j+2)%3][(i+2)%3]
                    - M[(j+1)%3][(i+2)%3] * M[(j+2)%3][(i+1)%3])) / d
          for j in range(3)] for i in range(3)]
    return tuple(tuple(row) for row in c)

Tinv = mat_inv3_frac(T)

def is_signed_perm(M):
    for row in M:
        if sorted(abs(x) for x in row) != [0, 0, 1]:
            return False
    for j in range(3):
        col = [M[i][j] for i in range(3)]
        if sorted(abs(x) for x in col) != [0, 0, 1]:
            return False
    return True

def d3_box(norm_max):
    out = []
    for v in product(range(-3, 4), repeat=3):
        n = dot(v, v)
        if 0 < n <= norm_max and sum(v) % 2 == 0:
            out.append(v)
    return sorted(out)

shell4 = sorted(v for v in d3_box(4) if dot(v, v) == 4)
axes = sorted([tuple(2 * (1 if k == i else 0) for k in range(3)) for i in range(3)]
              + [tuple(-2 * (1 if k == i else 0) for k in range(3)) for i in range(3)])

transported = []
ok_int = True
for M in aut:
    X = mat_mul(T, M)              # integer
    Y = mat_mul(tuple(tuple(Fraction(x) for x in row) for row in X), Tinv)
    Z = []
    for row in Y:
        r = []
        for x in row:
            if x.denominator != 1:
                ok_int = False
            r.append(int(x))
        Z.append(tuple(r))
    transported.append(tuple(Z))
transported_set = sorted(set(transported))

all_signed_perms3 = []
for sig in permutations(range(3)):
    for signs in product((1, -1), repeat=3):
        all_signed_perms3.append(tuple(tuple(signs[i] * (1 if sig[i] == j else 0)
                                             for j in range(3)) for i in range(3)))
all_signed_perms3 = sorted(set(all_signed_perms3))

# frozen isometry also matches root shell to the D_3 minimal shell
shell2 = sorted(v for v in d3_box(2) if dot(v, v) == 2)
t_roots = sorted(tuple(int(x) for x in mat_vec(T, r)) for r in ROOTS_B)

g3 = (shell4 == axes and ok_int and transported_set == all_signed_perms3
      and len(transported_set) == 48 and t_roots == shell2 and detT in (-2, 2))
gate("G3", g3, "shell4_eq_axes=%s transported_eq_signedperms=%s roots_to_minvecs=%s |detT|=%d"
     % (shell4 == axes, transported_set == all_signed_perms3, t_roots == shell2, abs(detT)))

# ------------------------------------------------------------------- G4

P = 5
A5 = tuple(tuple(x % P for x in row) for row in CART)
vecs = sorted(product(range(P), repeat=3))

def bil(u, v):
    return sum(u[i] * A5[i][j] * v[j] for i in range(3) for j in range(3)) % P

c1s = [v for v in vecs if bil(v, v) == A5[0][0]]
O5 = []
for c1 in c1s:
    c2s = [v for v in vecs if bil(v, v) == A5[1][1] and bil(c1, v) == A5[0][1]]
    for c2 in c2s:
        for c3 in vecs:
            if (bil(c3, c3) == A5[2][2] and bil(c1, c3) == A5[0][2]
                    and bil(c2, c3) == A5[1][2]):
                M = tuple(tuple((c1, c2, c3)[j][i] for j in range(3)) for i in range(3))
                O5.append(M)
O5 = sorted(set(O5))

o5_orders = {}
for M in O5:
    o = mat_order_mod(M, P, 240)
    o5_orders[o] = o5_orders.get(o, 0) + 1
n_order5 = o5_orders.get(5, 0)

red = [tuple(tuple(x % P for x in row) for row in M) for M in aut]
red_set = sorted(set(red))
red_in_O5 = all(M in set(O5) for M in red_set)
red_order5 = any(mat_order_mod(M, P, 240) == 5 for M in red_set)

g4 = (len(O5) == 240 and n_order5 == 24 and len(red_set) == 48
      and red_in_O5 and not red_order5 and 240 // 48 == 5)
gate("G4", g4, "|O5|=%d order5=%d red_distinct=%d red_in_O5=%s order5_in_image=%s index=%d"
     % (len(O5), n_order5, len(red_set), red_in_O5, red_order5,
        (len(O5) // len(red_set)) if red_set else 0))

# ------------------------------------------------------------------- G5

MONS = sorted([(i, j, 4 - i - j) for i in range(5) for j in range(5 - i)])
MIDX = {m: k for k, m in enumerate(MONS)}

def act_on_monomial(g, mon):
    # variables x_i -> sum_j g[j][i]? For signed permutation matrices the
    # substitution x -> g^{-1} x sends monomial to monomial. Use: new var
    # k gets old var image: x_i -> s * x_{p(i)} read from columns of g.
    # g column i has single nonzero s at row p(i): x_i |-> s * x_{p(i)}.
    out_exp = [0, 0, 0]
    sign = 1
    for i in range(3):
        col = [g[r][i] for r in range(3)]
        for r in range(3):
            if col[r] != 0:
                out_exp[r] += mon[i]
                if col[r] < 0 and mon[i] % 2 == 1:
                    sign = -sign
    return tuple(out_exp), sign

REY = [[Fraction(0)] * 15 for _ in range(15)]
for g in transported_set:
    for m in MONS:
        im, s = act_on_monomial(g, m)
        REY[MIDX[im]][MIDX[m]] += Fraction(s, 48)
rk = gauss_rank([tuple(row) for row in REY])
tr = sum(REY[i][i] for i in range(15))

r4 = [Fraction(0)] * 15
for m in MONS:
    (i, j, k) = m
    # (x^2+y^2+z^2)^2 coefficients: multinomial over squared terms
    if i % 2 == 0 and j % 2 == 0 and k % 2 == 0:
        a, b, c = i // 2, j // 2, k // 2
        from math import factorial
        r4[MIDX[m]] = Fraction(factorial(2) // (factorial(a) * factorial(b) * factorial(c)))
m4 = [Fraction(0)] * 15
for m in ((4, 0, 0), (0, 4, 0), (0, 0, 4)):
    m4[MIDX[m]] = Fraction(1)

def apply_rey(v):
    return [sum(REY[i][j] * v[j] for j in range(15)) for i in range(15)]

fix_r4 = apply_rey(r4) == r4
fix_m4 = apply_rey(m4) == m4
indep = gauss_rank([tuple(r4), tuple(m4)]) == 2

g5 = (rk == 2 and tr == 2 and fix_r4 and fix_m4 and indep)
gate("G5", g5, "rank=%d trace=%s fix_r4=%s fix_m4=%s indep=%s"
     % (rk, tr, fix_r4, fix_m4, indep))

# ------------------------------------------------------------------- G6

FROZEN_SIZES = (12, 6, 24, 12)
FROZEN_A = (-4, 32, -72, -64)
allv = d3_box(8)
shells = {N: sorted(v for v in allv if dot(v, v) == N) for N in (2, 4, 6, 8)}

def moments(S):
    m4c = [sum(v[c] ** 4 for v in S) for c in range(3)]
    m22 = [sum(v[a] ** 2 * v[b] ** 2 for v in S) for (a, b) in ((0, 1), (0, 2), (1, 2))]
    return m4c, m22

sizes, avals, iso_ok = [], [], True
for N in (2, 4, 6, 8):
    S = shells[N]
    m4c, m22 = moments(S)
    if len(set(m4c)) != 1 or len(set(m22)) != 1:
        iso_ok = False
    sizes.append(len(S))
    avals.append(m4c[0] - 3 * m22[0])
g6 = (tuple(sizes) == FROZEN_SIZES and tuple(avals) == FROZEN_A and iso_ok
      and all(a != 0 for a in avals))
gate("G6", g6, "sizes=%s a=%s coord_indep=%s" % (tuple(sizes), tuple(avals), iso_ok))

# ------------------------------------------------------------------- G7

a3 = avals[:3]
def cone(w):
    return sum(a3[i] * w[i] for i in range(3))

wit = (cone((8, 1, 0)) == 0, cone((0, 9, 4)) == 0, cone((6, 3, 1)) == 0)
no_13 = True
for w1 in range(1, 41):
    for w3 in range(1, 41):
        if a3[0] * w1 + a3[2] * w3 == 0:
            no_13 = False
g7 = all(wit) and no_13
gate("G7", g7, "witness_810=%s witness_094=%s witness_631=%s no_positive_shells13=%s cone=%s"
     % (wit[0], wit[1], wit[2], no_13, tuple(a3)))

# ------------------------------------------------- EXPECTED-FAIL demos

print("-- expected-fail demonstrations (a NOT-FIRED line is a failure) --")

# D1: wrong-Gram triple must be rejected by the G1 filter
t_bad = (sub4(e4(0), e4(1)), sub4(e4(1), e4(2)), sub4(e4(0), e4(2)))
demo("D1", gram_of_triple(t_bad) != CART, "wrong-Gram triple rejected by filter")

# D2: multiset check on Aut plus one injected foreign element
g5elt = None
for M in O5:
    if mat_order_mod(M, P, 240) == 5:
        g5elt = M
        break
fake = sorted(set(aut) | {g5elt})
oc = {}
for M in fake:
    o = mat_order(M, 60) or 0
    oc[o] = oc.get(o, 0) + 1
demo("D2", oc != FROZEN_ORDERS, "multiset breaks on injected 49th element")

# D3: axes check on Shell(2)
demo("D3", sorted(shell2) != axes, "Shell(2) is not the axes set")

# D4: no-order-5 check on the full finite orthogonal group
demo("D4", any(mat_order_mod(M, P, 240) == 5 for M in O5),
     "full O(F_5^3) contains order-5 elements")

# D5: invariant dimension for a single fourfold rotation subgroup
rot4 = ((0, 1, 0), (-1, 0, 0), (0, 0, 1))
C4 = []
Mm = mat_id(3)
for _ in range(4):
    Mm = mat_mul(Mm, rot4)
    C4.append(Mm)
REY4 = [[Fraction(0)] * 15 for _ in range(15)]
for g in C4:
    for m in MONS:
        im, s = act_on_monomial(g, m)
        REY4[MIDX[im]][MIDX[m]] += Fraction(s, 4)
rk4 = gauss_rank([tuple(row) for row in REY4])
demo("D5", rk4 != 2, "C4 invariant dimension is %d, not 2" % rk4)

# D6: wrong anisotropy table; and coordinate independence on a bad set
demo("D6a", (0, 32, -72, -64) != tuple(avals), "wrong table detected")
bad_m4c, bad_m22 = moments([(1, 0, 0)])
demo("D6b", len(set(bad_m4c)) != 1, "non-invariant set breaks coordinate independence")

# D7: cone membership on (1,1,1)
demo("D7", cone((1, 1, 1)) != 0, "weights (1,1,1) are off the cone, value %d"
     % cone((1, 1, 1)))

# ------------------------------------------------------------- summary

ok = all(results) and all(demos)
print("GATES %d/%d PASS, DEMOS %d/%d FIRED, VERDICT %s"
      % (sum(results), len(results), sum(demos), len(demos),
         "ALL PASS" if ok else "FAIL"))
sys.exit(0 if ok else 1)
