#!/usr/bin/env python3
"""Exact audit for P-J-ODD-MOTOR-BRIDGE-HARDENING-1.

Standard library only. Rational and Q(sqrt(5)) arithmetic only. No float,
tolerance, randomness, file input, environment input, network, or third-party
package. The probe hardens two clauses of the public odd-motor theorem and
classifies a frozen 624-element channel box at L1 only.
"""

from fractions import Fraction as Q
from itertools import product
from typing import Dict, Iterable, List, Sequence, Tuple

Rat = Q
Matrix = Tuple[Tuple[Rat, ...], ...]
Vector = Tuple[Rat, ...]
Monomial = Tuple[int, int]  # (power of z, power of t), z powers may be negative
FormalMatrix = Dict[Monomial, Matrix]
Q5 = Tuple[Rat, Rat]  # a + b sqrt(5)
Q5Poly = Tuple[Q5, ...]  # low degree first
Q5Matrix = Tuple[Tuple[Q5, ...], ...]


def zero(n: int = 4) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(n)) for _ in range(n))


def identity(n: int = 4) -> Matrix:
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def madd(x: Matrix, y: Matrix) -> Matrix:
    return tuple(tuple(a + b for a, b in zip(rx, ry)) for rx, ry in zip(x, y))


def msub(x: Matrix, y: Matrix) -> Matrix:
    return tuple(tuple(a - b for a, b in zip(rx, ry)) for rx, ry in zip(x, y))


def mscale(c: Rat, x: Matrix) -> Matrix:
    return tuple(tuple(c * a for a in row) for row in x)


def transpose(x: Matrix) -> Matrix:
    return tuple(tuple(c) for c in zip(*x))


def mmul(x: Matrix, y: Matrix) -> Matrix:
    yt = transpose(y)
    return tuple(
        tuple(sum(a * b for a, b in zip(row, col)) for col in yt)
        for row in x
    )


def mpow(x: Matrix, n: int) -> Matrix:
    out = identity(len(x))
    base = x
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def minv(x: Matrix) -> Matrix:
    n = len(x)
    aug = [list(x[i]) + list(identity(n)[i]) for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v / scale for v in aug[col]]
        for row in range(n):
            if row != col and aug[row][col] != 0:
                factor = aug[row][col]
                aug[row] = [a - factor * b for a, b in zip(aug[row], aug[col])]
    return tuple(tuple(row[n:]) for row in aug)


def rank(x: Matrix) -> int:
    a = [list(row) for row in x]
    rows = len(a)
    cols = len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col] != 0), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [v / scale for v in a[pivot_row]]
        for row in range(rows):
            if row != pivot_row and a[row][col] != 0:
                factor = a[row][col]
                a[row] = [u - factor * v for u, v in zip(a[row], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def trace(x: Matrix) -> Rat:
    return sum(x[i][i] for i in range(len(x)))


def columns(vectors: Sequence[Vector]) -> Matrix:
    return tuple(tuple(vectors[j][i] for j in range(len(vectors))) for i in range(len(vectors[0])))


def matvec(x: Matrix, v: Vector) -> Vector:
    return tuple(sum(a * b for a, b in zip(row, v)) for row in x)


def sum_matrices(items: Iterable[Matrix]) -> Matrix:
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
D_POWERS = tuple(mpow(D, k) for k in range(1, 5))
A1 = msub(D_POWERS[0], D_POWERS[3])
A2 = msub(D_POWERS[1], D_POWERS[2])
G = msub(I4, mscale(Q(1, 5), ONES))
G_INV = minv(G)


def sharp(x: Matrix) -> Matrix:
    return mmul(mmul(G_INV, transpose(x)), G)


# Frozen affine simplex and projectors.
e0 = (Q(1), Q(0), Q(0), Q(0))
vertices = tuple(matvec(mpow(D, k), e0) for k in range(5))
basis = columns(vertices[:4])
basis_inv = minv(basis)


def rho(a: int, b: int) -> Matrix:
    return mmul(columns(tuple(vertices[(a * x + b) % 5] for x in range(4))), basis_inv)


AFFINE = {(a, b): rho(a, b) for a in (1, 2, 3, 4) for b in range(5)}
P_SECTOR: Dict[int, Matrix] = {}
R_SECTOR: Dict[int, Matrix] = {}
C_SECTOR: Dict[int, Matrix] = {}
G_TOKEN: Dict[int, Matrix] = {}
for token in range(5):
    stabilizer = {a: AFFINE[(a, token * (1 - a) % 5)] for a in (1, 2, 3, 4)}
    g = stabilizer[2]
    G_TOKEN[token] = g
    p = mscale(Q(1, 4), sum_matrices(stabilizer.values()))
    r = mscale(Q(1, 4), madd(msub(madd(I4, mpow(g, 2)), g), mscale(Q(-1), mpow(g, 3))))
    c = msub(msub(I4, p), r)
    P_SECTOR[token] = p
    R_SECTOR[token] = r
    C_SECTOR[token] = c


# Q(sqrt(5)) arithmetic.
def q5_add(x: Q5, y: Q5) -> Q5:
    return (x[0] + y[0], x[1] + y[1])


def q5_sub(x: Q5, y: Q5) -> Q5:
    return (x[0] - y[0], x[1] - y[1])


def q5_neg(x: Q5) -> Q5:
    return (-x[0], -x[1])


def q5_mul(x: Q5, y: Q5) -> Q5:
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5_inv(x: Q5) -> Q5:
    den = x[0] * x[0] - 5 * x[1] * x[1]
    if den == 0:
        raise ZeroDivisionError("zero divisor in Q(sqrt(5)) field arithmetic")
    return (x[0] / den, -x[1] / den)


def q5_div(x: Q5, y: Q5) -> Q5:
    return q5_mul(x, q5_inv(y))


def q5_is_zero(x: Q5) -> bool:
    return x == (Q(0), Q(0))


def q5_sign(x: Q5, embedding: int) -> int:
    """Exact sign of a + embedding*b*sqrt(5), embedding in {+1,-1}."""
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


def poly_trim(p: Sequence[Q5]) -> Q5Poly:
    out = list(p)
    while len(out) > 1 and q5_is_zero(out[-1]):
        out.pop()
    return tuple(out)


def poly_add(p: Q5Poly, q: Q5Poly) -> Q5Poly:
    n = max(len(p), len(q))
    out = []
    for i in range(n):
        a = p[i] if i < len(p) else (Q(0), Q(0))
        b = q[i] if i < len(q) else (Q(0), Q(0))
        out.append(q5_add(a, b))
    return poly_trim(out)


def poly_neg(p: Q5Poly) -> Q5Poly:
    return tuple(q5_neg(x) for x in p)


def poly_sub(p: Q5Poly, q: Q5Poly) -> Q5Poly:
    return poly_add(p, poly_neg(q))


def poly_mul(p: Q5Poly, q: Q5Poly) -> Q5Poly:
    out = [(Q(0), Q(0)) for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = q5_add(out[i + j], q5_mul(a, b))
    return poly_trim(out)


def poly_scale(c: Q5, p: Q5Poly) -> Q5Poly:
    return poly_trim(tuple(q5_mul(c, x) for x in p))


def poly_divmod(p: Q5Poly, q: Q5Poly) -> Tuple[Q5Poly, Q5Poly]:
    if len(q) == 1 and q5_is_zero(q[0]):
        raise ZeroDivisionError("zero polynomial")
    rem = list(poly_trim(p))
    quo = [(Q(0), Q(0)) for _ in range(max(1, len(rem) - len(q) + 1))]
    while len(rem) >= len(q) and not (len(rem) == 1 and q5_is_zero(rem[0])):
        degree = len(rem) - len(q)
        lead = q5_div(rem[-1], q[-1])
        quo[degree] = q5_add(quo[degree], lead)
        for i in range(len(q)):
            rem[degree + i] = q5_sub(rem[degree + i], q5_mul(lead, q[i]))
        rem = list(poly_trim(rem))
    return (poly_trim(quo), poly_trim(rem))


def poly_xgcd(a: Q5Poly, b: Q5Poly) -> Tuple[Q5Poly, Q5Poly, Q5Poly]:
    old_r, r = a, b
    old_s, s = ((Q(1), Q(0)),), ((Q(0), Q(0)),)
    old_t, t = ((Q(0), Q(0)),), ((Q(1), Q(0)),)
    while not (len(r) == 1 and q5_is_zero(r[0])):
        quotient, new_r = poly_divmod(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, poly_sub(old_s, poly_mul(quotient, s))
        old_t, t = t, poly_sub(old_t, poly_mul(quotient, t))
    lead_inv = q5_inv(old_r[-1])
    return (poly_scale(lead_inv, old_r), poly_scale(lead_inv, old_s), poly_scale(lead_inv, old_t))


def q5_matrix_zero(n: int = 4) -> Q5Matrix:
    return tuple(tuple((Q(0), Q(0)) for _ in range(n)) for _ in range(n))


def q5_matrix_identity(n: int = 4) -> Q5Matrix:
    return tuple(tuple((Q(i == j), Q(0)) for j in range(n)) for i in range(n))


def q5_matrix_add(x: Q5Matrix, y: Q5Matrix) -> Q5Matrix:
    return tuple(tuple(q5_add(a, b) for a, b in zip(rx, ry)) for rx, ry in zip(x, y))


def q5_matrix_mul(x: Q5Matrix, y: Q5Matrix) -> Q5Matrix:
    yt = tuple(tuple(c) for c in zip(*y))
    return tuple(
        tuple(
            sum_q5(q5_mul(a, b) for a, b in zip(row, col))
            for col in yt
        )
        for row in x
    )


def sum_q5(items: Iterable[Q5]) -> Q5:
    out = (Q(0), Q(0))
    for item in items:
        out = q5_add(out, item)
    return out


def q5_matrix_scale(c: Q5, x: Q5Matrix) -> Q5Matrix:
    return tuple(tuple(q5_mul(c, a) for a in row) for row in x)


def q5_matrix_rank(x: Q5Matrix) -> int:
    a = [list(row) for row in x]
    rows = len(a)
    cols = len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if not q5_is_zero(a[i][col])), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv_pivot = q5_inv(a[pivot_row][col])
        a[pivot_row] = [q5_mul(inv_pivot, v) for v in a[pivot_row]]
        for row in range(rows):
            if row != pivot_row and not q5_is_zero(a[row][col]):
                factor = a[row][col]
                a[row] = [q5_sub(u, q5_mul(factor, v)) for u, v in zip(a[row], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def rational_to_q5_matrix(x: Matrix) -> Q5Matrix:
    return tuple(tuple((a, Q(0)) for a in row) for row in x)


def eval_poly_matrix(p: Q5Poly, x: Q5Matrix) -> Q5Matrix:
    out = q5_matrix_zero(len(x))
    power = q5_matrix_identity(len(x))
    for coefficient in p:
        out = q5_matrix_add(out, q5_matrix_scale(coefficient, power))
        power = q5_matrix_mul(power, x)
    return out


# Formal Laurent matrix arithmetic.
def formal_clean(x: FormalMatrix) -> FormalMatrix:
    return {m: a for m, a in x.items() if a != Z4}


def formal_add(x: FormalMatrix, y: FormalMatrix) -> FormalMatrix:
    out = dict(x)
    for monomial, coefficient in y.items():
        out[monomial] = madd(out.get(monomial, Z4), coefficient)
    return formal_clean(out)


def formal_neg(x: FormalMatrix) -> FormalMatrix:
    return {m: mscale(Q(-1), a) for m, a in x.items()}


def formal_sub(x: FormalMatrix, y: FormalMatrix) -> FormalMatrix:
    return formal_add(x, formal_neg(y))


def formal_mul(x: FormalMatrix, y: FormalMatrix) -> FormalMatrix:
    out: FormalMatrix = {}
    for (zx, tx), a in x.items():
        for (zy, ty), b in y.items():
            monomial = (zx + zy, tx + ty)
            out[monomial] = madd(out.get(monomial, Z4), mmul(a, b))
    return formal_clean(out)


def formal_block(left: Matrix, x: FormalMatrix, right: Matrix) -> FormalMatrix:
    return formal_clean({m: mmul(mmul(left, a), right) for m, a in x.items()})


def formal_sharp(x: FormalMatrix) -> FormalMatrix:
    return formal_clean({m: sharp(a) for m, a in x.items()})


# Integrity of the frozen carrier.
carrier_integrity = (
    mpow(D, 5) == I4
    and mmul(G, G_INV) == I4
    and all(
        (rank(P_SECTOR[k]), rank(R_SECTOR[k]), rank(C_SECTOR[k])) == (1, 1, 2)
        and madd(madd(P_SECTOR[k], R_SECTOR[k]), C_SECTOR[k]) == I4
        and all(
            mmul(x, y) == Z4
            for x, y in (
                (P_SECTOR[k], R_SECTOR[k]),
                (R_SECTOR[k], P_SECTOR[k]),
                (P_SECTOR[k], C_SECTOR[k]),
                (C_SECTOR[k], P_SECTOR[k]),
                (R_SECTOR[k], C_SECTOR[k]),
                (C_SECTOR[k], R_SECTOR[k]),
            )
        )
        for k in range(5)
    )
)


# H1: factorization, exact embedding signs, explicit CRT idempotents and ranks.
one_q5 = (Q(1), Q(0))
zero_q5 = (Q(0), Q(0))
alpha_u = (Q(3, 2), Q(1, 2))
alpha_s = (Q(3, 2), Q(-1, 2))
f_u: Q5Poly = (alpha_u, q5_neg(alpha_u), one_q5)
f_s: Q5Poly = (alpha_s, q5_neg(alpha_s), one_q5)
product_poly = poly_mul(f_u, f_s)
target_poly: Q5Poly = tuple((Q(c), Q(0)) for c in (1, -2, 4, -3, 1))
delta_u = q5_sub(q5_mul(alpha_u, alpha_u), q5_mul((Q(4), Q(0)), alpha_u))
delta_s = q5_sub(q5_mul(alpha_s, alpha_s), q5_mul((Q(4), Q(0)), alpha_s))
embedding_signs = (
    q5_sign(delta_u, 1),
    q5_sign(delta_u, -1),
    q5_sign(delta_s, 1),
    q5_sign(delta_s, -1),
)
gcd_poly, bezout_u, bezout_s = poly_xgcd(f_u, f_s)
J_q5 = rational_to_q5_matrix(M_J)
e_u_poly = poly_mul(bezout_s, f_s)
e_s_poly = poly_mul(bezout_u, f_u)
e_u = eval_poly_matrix(e_u_poly, J_q5)
e_s = eval_poly_matrix(e_s_poly, J_q5)
q5_i4 = q5_matrix_identity()
q5_z4 = q5_matrix_zero()
idempotents_ok = (
    gcd_poly == (one_q5,)
    and q5_matrix_mul(e_u, e_u) == e_u
    and q5_matrix_mul(e_s, e_s) == e_s
    and q5_matrix_mul(e_u, e_s) == q5_z4
    and q5_matrix_add(e_u, e_s) == q5_i4
    and (q5_matrix_rank(e_u), q5_matrix_rank(e_s)) == (2, 2)
)
h1_ok = (
    product_poly == target_poly
    and delta_u == (Q(-5, 2), Q(-1, 2))
    and delta_s == (Q(-5, 2), Q(1, 2))
    and embedding_signs == (-1, -1, -1, -1)
    and alpha_u != alpha_s
    and idempotents_ok
)


# H2: explicit formal Schur complement on every token.
schur_tokens: List[bool] = []
for token in range(5):
    p = P_SECTOR[token]
    r = R_SECTOR[token]
    c = C_SECTOR[token]
    h = madd(G_TOKEN[token], mpow(G_TOKEN[token], 3))
    l_formal: FormalMatrix = {
        (1, 0): I4,
        (0, 0): mscale(Q(-1), h),
        (0, 1): mscale(Q(-1), A1),
    }
    clc = formal_block(c, l_formal, c)
    clc_inv: FormalMatrix = {(-1, 0): c}
    plr = formal_block(p, l_formal, r)
    plc = formal_block(p, l_formal, c)
    clr = formal_block(c, l_formal, r)
    schur = formal_sub(plr, formal_mul(formal_mul(plc, clc_inv), clr))
    b = mmul(mmul(mmul(mmul(p, A1), c), A1), r)
    expected_schur: FormalMatrix = {(-1, 2): mscale(Q(-1), b)}
    expected_right: FormalMatrix = {(-2, 4): mscale(Q(5, 4), r)}
    expected_left: FormalMatrix = {(-2, 4): mscale(Q(5, 4), p)}
    token_ok = (
        clc == {(1, 0): c}
        and formal_mul(clc, clc_inv) == {(0, 0): c}
        and plr == {}
        and plc == {(0, 1): mscale(Q(-1), mmul(mmul(p, A1), c))}
        and clr == {(0, 1): mscale(Q(-1), mmul(mmul(c, A1), r))}
        and schur == expected_schur
        and formal_mul(formal_sharp(schur), schur) == expected_right
        and formal_mul(schur, formal_sharp(schur)) == expected_left
    )
    schur_tokens.append(token_ok)
h2_ok = all(schur_tokens)


def channel(coefficients: Tuple[int, int, int, int]) -> Matrix:
    return sum_matrices(mscale(Q(c), power) for c, power in zip(coefficients, D_POWERS))


def active_line_projector(u: Matrix, source: Matrix, mediator: Matrix) -> Tuple[bool, Matrix]:
    active = mmul(mmul(mediator, u), source)
    gram_line = mmul(active, sharp(active))
    scalar = trace(gram_line)
    if rank(active) != 1 or scalar <= 0 or mmul(gram_line, gram_line) != mscale(scalar, gram_line):
        return (False, Z4)
    projector = mscale(Q(1, 1) / scalar, gram_line)
    return (mmul(projector, projector) == projector, projector)


def battery(u: Matrix) -> bool:
    if sharp(u) != mscale(Q(-1), u):
        return False
    for token in range(5):
        p = P_SECTOR[token]
        r = R_SECTOR[token]
        c = C_SECTOR[token]
        if any(mmul(mmul(x, u), x) != Z4 for x in (p, r, c)):
            return False
        if mmul(mmul(p, u), r) != Z4 or mmul(mmul(r, u), p) != Z4:
            return False
        if any(
            rank(mmul(mmul(x, u), y)) != 1
            for x, y in ((p, c), (c, p), (r, c), (c, r))
        ):
            return False
        b = mmul(mmul(mmul(mmul(p, u), c), u), r)
        if (
            rank(b) != 1
            or mmul(sharp(b), b) != mscale(Q(5, 4), r)
            or mmul(b, sharp(b)) != mscale(Q(5, 4), p)
        ):
            return False
        ok_p, line_p = active_line_projector(u, p, c)
        ok_r, line_r = active_line_projector(u, r, c)
        if not ok_p or not ok_r or trace(mmul(line_p, line_r)) != Q(1, 5):
            return False
    return True


box = tuple(product(range(-2, 3), repeat=4))
nonzero_box = tuple(c for c in box if c != (0, 0, 0, 0))
survivors = tuple(c for c in nonzero_box if battery(channel(c)))
target_survivors = (
    (-1, 0, 0, 1),
    (0, -1, 1, 0),
    (0, 1, -1, 0),
    (1, 0, 0, -1),
)
conjugator = AFFINE[(2, 0)]
conjugacy_ok = mmul(mmul(conjugator, A1), minv(conjugator)) == A2
h3_ok = len(nonzero_box) == 624 and survivors == target_survivors and conjugacy_ok

all_ok = carrier_integrity and h1_ok and h2_ok and h3_ok

print("P-J-ODD-MOTOR-BRIDGE-HARDENING-1")
print("LAYER L1 EXACT ARITHMETIC AND LINEAR ALGEBRA ONLY")
print("AUTHORITY BASIS PUBLIC CANON v61")
print("CARRIER INTEGRITY", "PASS" if carrier_integrity else "FAIL")
print("H1 FACTORIZATION", "PASS" if product_poly == target_poly else "FAIL")
print("H1 DISCRIMINANTS", "delta_u=(-5-sqrt5)/2", "delta_s=(-5+sqrt5)/2")
print("H1 EMBEDDING SIGNS", *embedding_signs)
print("H1 CRT IDEMPOTENT RANKS", q5_matrix_rank(e_u), q5_matrix_rank(e_s))
print("H1 NATIVE TWO-SECTOR HARDENING", "PASS" if h1_ok else "FAIL")
print("H2 EXPLICIT SCHUR TOKENS", sum(schur_tokens), "/5")
print("H2 SCHUR P-R TERM -(t^2/z)PACAR", "PASS" if h2_ok else "FAIL")
print("H2 SQUARED MAGNITUDE (5/4)t^4/z^2", "PASS" if h2_ok else "FAIL")
print("H3 FROZEN BOX", len(nonzero_box))
print("H3 SURVIVOR COUNT", len(survivors))
print("H3 SURVIVORS", ";".join(",".join(str(v) for v in c) for c in survivors))
print("H3 AFFINE CONJUGACY rho(2,0) A1 rho(2,0)^-1=A2", "PASS" if conjugacy_ok else "FAIL")
print("H3 UNIQUE UP TO SIGN AND AFFINE CONJUGACY IN BOX", "PASS" if h3_ok else "FAIL")
print("PHYSICAL FREQUENCY MATERIAL BORN DECODER APPARATUS NOT CLAIMED")
print("DECISION", "HARDENING-CERTIFIED" if all_ok else "ROUTE-FALSIFIED")
