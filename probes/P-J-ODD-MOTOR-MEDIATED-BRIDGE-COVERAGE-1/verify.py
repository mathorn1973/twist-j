#!/usr/bin/env python3
"""Full exact evidence coverage for J-ODD-MOTOR-MEDIATED-BRIDGE [T].

Standard library only. Exact rational and Q(sqrt(5)) arithmetic. This verifier
covers the frozen Public Canon v61 theorem scope without extending it. The
later 624-channel-box uniqueness result is intentionally excluded.
"""

from fractions import Fraction as Q
from itertools import permutations, product


def zero(n=4):
    return tuple(tuple(Q(0) for _ in range(n)) for _ in range(n))


def identity(n=4):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def madd(x, y):
    return tuple(tuple(a + b for a, b in zip(rx, ry)) for rx, ry in zip(x, y))


def msub(x, y):
    return tuple(tuple(a - b for a, b in zip(rx, ry)) for rx, ry in zip(x, y))


def mscale(c, x):
    return tuple(tuple(Q(c) * a for a in row) for row in x)


def transpose(x):
    return tuple(tuple(c) for c in zip(*x))


def mmul(x, y):
    yt = transpose(y)
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in yt) for row in x)


def mpow(x, n):
    out = identity(len(x))
    base = x
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def minv(x):
    n = len(x)
    aug = [list(x[i]) + list(identity(n)[i]) for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v / scale for v in aug[col]]
        for row in range(n):
            if row != col and aug[row][col]:
                factor = aug[row][col]
                aug[row] = [a - factor * b for a, b in zip(aug[row], aug[col])]
    return tuple(tuple(row[n:]) for row in aug)


def rank(x):
    a = [list(row) for row in x]
    pivot_row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [v / scale for v in a[pivot_row]]
        for row in range(len(a)):
            if row != pivot_row and a[row][col]:
                factor = a[row][col]
                a[row] = [u - factor * v for u, v in zip(a[row], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def trace(x):
    return sum(x[i][i] for i in range(len(x)))


def columns(vectors):
    return tuple(tuple(vectors[j][i] for j in range(len(vectors))) for i in range(len(vectors[0])))


def matvec(x, v):
    return tuple(sum(a * b for a, b in zip(row, v)) for row in x)


def sum_matrices(items):
    out = zero()
    for item in items:
        out = madd(out, item)
    return out


I4 = identity()
Z4 = zero()
ONES = tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))
M_J = (
    (Q(1), Q(0), Q(-1), Q(1)),
    (Q(0), Q(1), Q(-1), Q(0)),
    (Q(1), Q(0), Q(0), Q(0)),
    (Q(0), Q(1), Q(-1), Q(1)),
)
D = msub(M_J, I4)
D1, D2, D3, D4 = (mpow(D, k) for k in range(1, 5))
A1 = msub(D1, D4)
EVEN = madd(D1, D4)
G = msub(I4, mscale(Q(1, 5), ONES))
G_INV = minv(G)


def sharp(x):
    return mmul(mmul(G_INV, transpose(x)), G)


def hs(x):
    return trace(mmul(sharp(x), x))


# Frozen affine simplex and multiplier-stabilizer sectors.
e0 = (Q(1), Q(0), Q(0), Q(0))
vertices = tuple(matvec(mpow(D, k), e0) for k in range(5))
basis = columns(vertices[:4])
basis_inv = minv(basis)


def rho(a, b):
    return mmul(columns(tuple(vertices[(a * x + b) % 5] for x in range(4))), basis_inv)


AFFINE = {(a, b): rho(a, b) for a in (1, 2, 3, 4) for b in range(5)}
P_SECTOR = {}
R_SECTOR = {}
C_SECTOR = {}
G_TOKEN = {}
for token in range(5):
    stabilizer = {a: AFFINE[(a, token * (1 - a) % 5)] for a in (1, 2, 3, 4)}
    g = stabilizer[2]
    G_TOKEN[token] = g
    p = mscale(Q(1, 4), sum_matrices(stabilizer.values()))
    r = mscale(Q(1, 4), madd(msub(madd(I4, mpow(g, 2)), g), mscale(-1, mpow(g, 3))))
    c = msub(msub(I4, p), r)
    P_SECTOR[token] = p
    R_SECTOR[token] = r
    C_SECTOR[token] = c


# Q(sqrt(5)) arithmetic for the native two-sector clause.
def q5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q5_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q5_neg(x):
    return (-x[0], -x[1])


def q5_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5_inv(x):
    den = x[0] * x[0] - 5 * x[1] * x[1]
    if den == 0:
        raise ZeroDivisionError("zero in Q(sqrt5)")
    return (x[0] / den, -x[1] / den)


def q5_div(x, y):
    return q5_mul(x, q5_inv(y))


def q5_zero(x):
    return x == (Q(0), Q(0))


def q5_sign(x, embedding):
    a, b = x[0], Q(embedding) * x[1]
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return 1 if a > 0 else -1
    left = a * a
    right = 5 * b * b
    if left == right:
        return 0
    if a > 0 and b < 0:
        return 1 if left > right else -1
    return 1 if right > left else -1


def ptrim(p):
    out = list(p)
    while len(out) > 1 and q5_zero(out[-1]):
        out.pop()
    return tuple(out)


def padd(p, q):
    out = []
    for i in range(max(len(p), len(q))):
        a = p[i] if i < len(p) else (Q(0), Q(0))
        b = q[i] if i < len(q) else (Q(0), Q(0))
        out.append(q5_add(a, b))
    return ptrim(out)


def pneg(p):
    return tuple(q5_neg(x) for x in p)


def psub(p, q):
    return padd(p, pneg(q))


def pmul(p, q):
    out = [(Q(0), Q(0)) for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = q5_add(out[i + j], q5_mul(a, b))
    return ptrim(out)


def pscale(c, p):
    return ptrim(tuple(q5_mul(c, x) for x in p))


def pdivmod(p, q):
    rem = list(ptrim(p))
    quo = [(Q(0), Q(0)) for _ in range(max(1, len(rem) - len(q) + 1))]
    while len(rem) >= len(q) and not (len(rem) == 1 and q5_zero(rem[0])):
        degree = len(rem) - len(q)
        lead = q5_div(rem[-1], q[-1])
        quo[degree] = q5_add(quo[degree], lead)
        for i in range(len(q)):
            rem[degree + i] = q5_sub(rem[degree + i], q5_mul(lead, q[i]))
        rem = list(ptrim(rem))
    return ptrim(quo), ptrim(rem)


def pxgcd(a, b):
    old_r, r = a, b
    old_s, s = (((Q(1), Q(0)),), ((Q(0), Q(0)),))
    old_t, t = (((Q(0), Q(0)),), ((Q(1), Q(0)),))
    while not (len(r) == 1 and q5_zero(r[0])):
        quotient, new_r = pdivmod(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, psub(old_s, pmul(quotient, s))
        old_t, t = t, psub(old_t, pmul(quotient, t))
    inv_lead = q5_inv(old_r[-1])
    return pscale(inv_lead, old_r), pscale(inv_lead, old_s), pscale(inv_lead, old_t)


def q5m_zero(n=4):
    return tuple(tuple((Q(0), Q(0)) for _ in range(n)) for _ in range(n))


def q5m_identity(n=4):
    return tuple(tuple((Q(i == j), Q(0)) for j in range(n)) for i in range(n))


def q5m_add(x, y):
    return tuple(tuple(q5_add(a, b) for a, b in zip(rx, ry)) for rx, ry in zip(x, y))


def q5_sum(items):
    out = (Q(0), Q(0))
    for item in items:
        out = q5_add(out, item)
    return out


def q5m_mul(x, y):
    yt = tuple(tuple(c) for c in zip(*y))
    return tuple(tuple(q5_sum(q5_mul(a, b) for a, b in zip(row, col)) for col in yt) for row in x)


def q5m_scale(c, x):
    return tuple(tuple(q5_mul(c, a) for a in row) for row in x)


def q5m_rank(x):
    a = [list(row) for row in x]
    pivot_row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if not q5_zero(a[i][col])), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv_p = q5_inv(a[pivot_row][col])
        a[pivot_row] = [q5_mul(inv_p, v) for v in a[pivot_row]]
        for row in range(len(a)):
            if row != pivot_row and not q5_zero(a[row][col]):
                factor = a[row][col]
                a[row] = [q5_sub(u, q5_mul(factor, v)) for u, v in zip(a[row], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def q5m_rational(x):
    return tuple(tuple((a, Q(0)) for a in row) for row in x)


def eval_poly_matrix(p, x):
    out = q5m_zero(len(x))
    power = q5m_identity(len(x))
    for coefficient in p:
        out = q5m_add(out, q5m_scale(coefficient, power))
        power = q5m_mul(power, x)
    return out


one_q5 = (Q(1), Q(0))
alpha_u = (Q(3, 2), Q(1, 2))
alpha_s = (Q(3, 2), Q(-1, 2))
f_u = (alpha_u, q5_neg(alpha_u), one_q5)
f_s = (alpha_s, q5_neg(alpha_s), one_q5)
target_poly = tuple((Q(c), Q(0)) for c in (1, -2, 4, -3, 1))
delta_u = q5_sub(q5_mul(alpha_u, alpha_u), q5_mul((Q(4), Q(0)), alpha_u))
delta_s = q5_sub(q5_mul(alpha_s, alpha_s), q5_mul((Q(4), Q(0)), alpha_s))
embedding_signs = (
    q5_sign(delta_u, 1), q5_sign(delta_u, -1),
    q5_sign(delta_s, 1), q5_sign(delta_s, -1),
)
gcd_poly, bezout_u, bezout_s = pxgcd(f_u, f_s)
J_q5 = q5m_rational(M_J)
e_u = eval_poly_matrix(pmul(bezout_s, f_s), J_q5)
e_s = eval_poly_matrix(pmul(bezout_u, f_u), J_q5)
q5_i4 = q5m_identity()
q5_z4 = q5m_zero()
native = (
    pmul(f_u, f_s) == target_poly
    and delta_u == (Q(-5, 2), Q(-1, 2))
    and delta_s == (Q(-5, 2), Q(1, 2))
    and embedding_signs == (-1, -1, -1, -1)
    and gcd_poly == (one_q5,)
    and q5m_mul(e_u, e_u) == e_u
    and q5m_mul(e_s, e_s) == e_s
    and q5m_mul(e_u, e_s) == q5_z4
    and q5m_add(e_u, e_s) == q5_i4
    and (q5m_rank(e_u), q5m_rank(e_s)) == (2, 2)
)


# Full P/C/R block and bridge audit on all five tokens.
token_checks = []
for token in range(5):
    p = P_SECTOR[token]
    r = R_SECTOR[token]
    c = C_SECTOR[token]
    integrity = (
        (rank(p), rank(r), rank(c)) == (1, 1, 2)
        and madd(madd(p, r), c) == I4
        and all(mmul(x, y) == Z4 for x, y in ((p, r), (r, p), (p, c), (c, p), (r, c), (c, r)i)
        and sharp(A1) == mscale(-1, A1)
     )
    diagonal_zero = all(mmul(mmul(x, A1), x) == Z4 for x in (p, r, c))
    direct_zero = mmul(mmul(p, A1), r) == Z4 and mmul(mmul(r, A1), p) == Z4
    cross = all(
        rank(mmul(mmul(x, A1), y)) == 1 and hs(mmul(mmul(x, A1), y)) == Q(5, 2)
        for x, y in ((p, c), (c, p), (r, c), (c, r)i
    )
    b = mmul(mmul(mmul(mmul(p, A1), c), A1), r)
    bridge = (
        rank(b) == 1
        and hs(b) == Q(5, 4)
        and mmul(sharp(b), b) == mscale(Q(5, 4), r)
        and mmul(b, sharp(b)) == mscale(Q(5, 4), p)
    )
    up = mmul(mmul(c, A1), p)
    ur = mmul(mmul(c, A1), r)
    line_p = mscale(Q(2, 5), mmul(up, sharp(up)))
    line_r = mscale(Q(2, 5), mmul(ur, sharp(ur)))
    overlap = trace(mmul(line_p, line_r)) == Q(1, 5)
    h = madd(G_TOKEN[token], mpow(G_TOKEN[token], 3))
    spectrum = mmul(h, p) == mscale(2, p) and mmul(h, r) == mscale(-2, r) and mmul(h, c) == Z4
    token_checks.append(integrity and diagonal_zero and direct_zero and cross and bridge and overlap and spectrum)
bridge_ok = all(token_checks)


# Frozen controls do not exhibit the same mediated-zero pattern.
controls_ok = True
for u in (D1,D2,D3,D4,EVEN):
    for token in range(5):
        sectors = {"P": P_SECTOR[token], "R": R_SECTOR[token], "C": C_SECTOR[token]}
        for x, y in permutations(sectors, 2):
            z = ({"P", "R", "C"} - {x, y}).pop()
            direct = mmul(mmul(sectors[x], u), sectors[y])
            mediated = mmul(mmul(mmul(mmul(sectors[x], u), sectors[z]), u), sectors[y])
            if direct == Z4 and mediated != Z4:
                controls_ok = False


# Explicit formal Laurent Schur complement on every token.
def formal_clean(x):
    return {m: a for m, a in x.items() if a != Z4}


def formal_add(x, y):
    out = dict(x)
    for monomial, coefficient in y.items():
        out[monomial] = madd(out.get(monomial, Z4), coefficient)
    return formal_clean(out)


def formal_neg(x):
    return {m: mscale(-1, a) for m, a in x.items()}


def formal_sub(x, y):
    return formal_add(x, formal_neg(y))


def formal_mul(x, y):
    out = {}
    for (zx, tx), a in x.items():
        for (zy, ty), b in y.items():
            monomial = (zx + zy, tx + ty)
            out[monomial] = madd(out.get(monomial, Z4), mmul(a, b))
    return formal_clean(out)


def formal_block(left, x, right):
    return formal_clean({m: mmul(mmul(left, a), right) for m, a in x.items()})


def formal_sharp(x):
    return formal_clean({m: sharp(a) for m, a in x.items()})


schur_tokens = []
for token in range(5):
    p = P_SECTOR[token]
    r = R_SECTOR[token]
    c = C_SECTOR[token]
    h = madd(G_TOKEN[token], mpow(G_TOKEN[token], 3))
    l_formal = {(1, 0): I4, (0, 0): mscale(-1, h), (0, 1): mscale(-1, A1)}
    clc = formal_block(c, l_formal, c)
    clc_inv = {(-1, 0): c}
    plr = formal_block(p, l_formal, r)
    plc = formal_block(p, l_formal, c)
    clr = formal_block(c, l_formal, r)
    schur = formal_sub(plr, formal_mul(formal_mul(plc, clc_inv), clr))
    b = mmul(mmul(mmul(mmul(p, A1), c), A1), r)
    expected = {(-1, 2): mscale(-1, b)}
    schur_tokens.append(
        clc == {(1, 0): c}
        and formal_mul(clc, clc_inv) == {(0, 0): c}
        and plr == {}
        and schur == expected
        and formal_mul(formal_sharp(schur), schur) == {(-2, 4): mscale(Q(5, 4), r))
        and formal_mul(schur, formal_sharp(schur)) == {(-2, 4): mscale(Q(5, 4), p)}
    )
schur_ok = all(schur_tokens)


# Exact determinant polynomial in z,t at token 2.
def add_poly(a, b):
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, Q(0)) + coefficient
    return {m: c for m, c in out.items() if c}


def mul_poly(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            out[(i + k, j + l)] = out.get((i + k, j + l), Q(0)) + x * y
    return {m: c for m, c in out.items() if c}


def perm_sign(p):
    return -1 if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 else 1


H2_TOKEN = madd(G_TOKEN[2], mpow(G_TOKEN[2], 3))
formal_matrix = []
for i in range(4):
    row = []
    for j in range(4):
        entry = {}
        if i == j:
            entry[(1, 0)] = Q(1)
        if H2_TOKEN[i][j]:
            entry[(0, 0)] = entry.get((0, 0), Q(0)) - H2_TOKEN[i][j]
        if A1[i][j]:
            entry[(0, 1)] = entry.get((0, 1), Q(0)) - A1[i][j]
        row.append(entry)
    formal_matrix.append(row)
determinant = {}
for perm in permutations(range(4)):
    term = {(0, 0): Q(perm_sign(perm))}
    for i, j in enumerate(perm):
        term = mul_poly(term, formal_matrix[i][j])
    determinant = add_poly(determinant, term)
determinant_ok = determinant == {
    (4, 0): Q(1),
    (2, 2): Q(5),
    (2, 0): Q(-4),
    (0, 4): Q(5),
}


# Frozen Sym^2 character decomposition, covariance and trilinear census.
group = tuple((a, b) for a in (1, 2, 3, 4) for b in range(5))


def fixed_points(g):
    a, b = g
    return sum((a * x + b) % 5 == x for x in range(5))


def group_mul(g, h):
    a, b = g
    c, d = h
    return (a * c % 5, (b + a * d) % 5)


def epsilon(g):
    return Q(1 if g[0] in (1, 4) else -1)


chi_v = {g: Q(fixed_points(g) - 1) for g in group}
chi_1 = {g: Q(1) for g in group}
chi_e = {g: epsilon(g) for g in group}
chi_sym2 = {g: Q(1, 2) * (chi_v[g] ** 2 + chi_v[group_mul(g, g)]) for g in group}


def inner(a, b):
    return Q(1, 20) * sum(a[g] * b[g] for g in group)


decomposition_ok = (
    inner(chi_1, chi_sym2), inner(chi_e, chi_sym2), inner(chi_v, chi_sym2), inner(chi_sym2, chi_sym2)
) == (1, 1, 2, 6) and inner(chi_1, chi_e) == inner(chi_1, chi_v) == inner(chi_e, chi_v) == 0

q_minus = (
    (Q(0), Q(1), Q(-1), Q(-1)),
    (Q(1), Q(0), Q(1), Q(-1)),
    (Q(-1), Q(1), Q(0), Q(1)),
    (Q(-1), Q(-1), Q(1), Q(0)),
)
q_plus = mscale(Q(5, 2), G)
covariance_ok = True
for g, x in AFFINE.items():
    covariance_ok &= mmul(mmul(transpose(x), q_plus), x) == q_plus
    covariance_ok &= mmul(mmul(transpose(x), q_minus), x) == mscale(epsilon(g), q_minus)

characters = {"1": chi_1, "e": chi_e, "V": chi_v}
trilinear = {}
for a, b, c in product(characters, repeat=3):
    dim = Q(1, 20) * sum(characters[a][g] * characters[b][g] * characters[c][g] for g in group)
    if dim:
        trilinear[(a, b, c)] = dim
trilinear_target = {
    ("1", "1", "1"): Q(1),
    ("1", "e", "e"): Q(1),
    ("e", "1", "e"): Q(1),
    ("e", "e", "1"): Q(1),
    ("1", "V", "V"): Q(1),
    ("V", "1", "V"): Q(1),
    ("V", "V", "1"): Q(1),
    ("e", "V", "V"): Q(1),
    ("V", "e", "V"): Q(1),
    ("V", "V", "e"): Q(1),
    ("V", "V", "V"): Q(3),
}
trilinear_ok = trilinear == trilinear_target

all_ok = all((native, bridge_ok, controls_ok, schur_ok, determinant_ok, decomposition_ok, covariance_ok, trilinear_ok))

print("P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-1")
print("LAYER L1 EXACT ARITHMETIC ONLY")
print("AUTHORITY BASIS PUBLIC CANON v61")
print("NATIVE DISCRIMINANTS", "PASS" if native else "FAIL")
print("NATIVE CRT RANKS", q5m_rank(e_u), q5m_rank(e_s))
print("AFFINE TOKEN COVERAGE", sum(token_checks), "/5")
print("P-C-R BRIDGE 5/4 OVERLAP 1/5", "PASS" if bridge_ok else "FAIL")
print("RAW POWER AND EVEN CONTROLS", "PASS" if controls_ok else "FAIL")
print("EXPLICIT SCHUR TOKENS", sum(schur_tokens), "/5")
print("SCHUR TERM -(t^2/z)PACAR", "PASS" if schur_ok else "FAIL")
print("SCHUR SQUARED MAGNITUDE (5/4)t^4/z^2", "PASS" if schur_ok else "FAIL")
print("FULL DET z^4+(5t^2-4)z^2+5t^4", "PASS" if determinant_ok else "FAIL")
print("SYM2 1+epsilon+2V END_DIM 6", "PASS" if decomposition_ok else "FAIL")
print("QPLUS INVARIANT QMINUS EPSILON", "PASS" if covariance_ok else "FAIL")
print("PAIRWISE HOM VANISHING", "PASS" if decomposition_ok else "FAIL")
print("TRILINEAR CENSUS", "PASS" if trilinear_ok else "FAIL")
print("REPEATED 2V NONSELECTION BOUNDARY RETAINED")
print("624 CHANNEL BOX UNIQUENESS EXCLUDED")
print("PHYSICAL FREQUENCY MATERIAL BORN DECODER APPARATUS NOT CLAIMED")
print("DECISION", "COVERAGE-CERTIFIED" if all_ok else "ROUTE-FALSIFIED")
