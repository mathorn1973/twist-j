#!/usr/bin/env python3
"""Exact audit for P-QDD-AFFINE-PURE-RECORD-BRIDGE-1."""

from fractions import Fraction as F
from itertools import product

BASE = "2a5601a9ec5cd5c8e24e80f3da78ca6838608fb4"
ISSUE = 497
CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


def matrix(rows):
    return tuple(tuple(x if isinstance(x, F) else F(x) for x in row) for row in rows)


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def zeros(n, m=None):
    if m is None:
        m = n
    return matrix([[0 for _ in range(m)] for _ in range(n)])


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def add(a, b):
    return matrix([[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))])


def scale(c, a):
    c = F(c)
    return matrix([[c * x for x in row] for row in a])


def subtract(a, b):
    return add(a, scale(-1, b))


def multiply(a, b):
    bt = transpose(b)
    return matrix([[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a])


def matvec(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), F(0)) for row in a)


def outer(v, w):
    return matrix([[x * y for y in w] for x in v])


def power(a, n):
    result = identity(len(a))
    base = a
    while n:
        if n & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        n //= 2
    return result


def inverse(a):
    n = len(a)
    work = [list(a[i]) + [F(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if work[row][col])
        work[col], work[pivot] = work[pivot], work[col]
        divisor = work[col][col]
        work[col] = [x / divisor for x in work[col]]
        for row in range(n):
            if row != col and work[row][col]:
                factor = work[row][col]
                work[row] = [work[row][j] - factor * work[col][j] for j in range(2 * n)]
    return tuple(tuple(work[i][n:]) for i in range(n))


def rank(a):
    work = [list(row) for row in a]
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((row for row in range(pivot_row, rows) if work[row][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][col]
        work[pivot_row] = [x / divisor for x in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][col]:
                factor = work[row][col]
                work[row] = [work[row][j] - factor * work[pivot_row][j] for j in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def determinant(a):
    work = [list(row) for row in a]
    n = len(work)
    value = F(1)
    sign = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign = -sign
        divisor = work[col][col]
        value *= divisor
        for row in range(col + 1, n):
            if work[row][col]:
                factor = work[row][col] / divisor
                for j in range(col, n):
                    work[row][j] -= factor * work[col][j]
    return sign * value


def dot_metric(v, gram, w):
    return sum((v[i] * sum((gram[i][j] * w[j] for j in range(len(w))), F(0))
                for i in range(len(v))), F(0))


# Q(zeta_5) in the basis 1,z,z^2,z^3.
POWERS = (
    (F(1), F(0), F(0), F(0)),
    (F(0), F(1), F(0), F(0)),
    (F(0), F(0), F(1), F(0)),
    (F(0), F(0), F(0), F(1)),
    (F(-1), F(-1), F(-1), F(-1)),
)


def k_scale(c, x):
    return tuple(F(c) * y for y in x)


def k_multiply(x, y):
    out = [F(0), F(0), F(0), F(0)]
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            basis_power = POWERS[(i + j) % 5]
            for k in range(4):
                out[k] += xi * yj * basis_power[k]
    return tuple(out)


def k_conjugate(x):
    out = [F(0), F(0), F(0), F(0)]
    for i, xi in enumerate(x):
        basis_power = POWERS[(-i) % 5]
        for k in range(4):
            out[k] += xi * basis_power[k]
    return tuple(out)


def k_trace(x):
    return 4 * x[0] - x[1] - x[2] - x[3]


def trace_pair(x, y):
    return k_trace(k_multiply(x, k_conjugate(y))) / 5


def rank_one_operator(v):
    columns = []
    for basis_vector in POWERS[:4]:
        columns.append(k_scale(trace_pair(basis_vector, v), v))
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))


I4 = identity(4)
ONE4 = matrix([[1, 1, 1, 1] for _ in range(4)])
G = subtract(I4, scale(F(1, 5), ONE4))
G_INV = add(I4, ONE4)
M_J = matrix(((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1)))
D_J = subtract(M_J, I4)
E0 = (F(1), F(0), F(0), F(0))
U2 = matvec(power(D_J, 2), E0)
P = scale(F(1, 4), outer(U2, U2))
Q = subtract(I4, P)


def gram_adjoint(a, gram, gram_inverse):
    return multiply(gram_inverse, multiply(transpose(a), gram))


def total_weight(v):
    return dot_metric(v, G, v)


def density(v):
    m = total_weight(v)
    if not m:
        return None
    return scale(1 / m, multiply(outer(v, v), G))


def pure_record(v):
    m = total_weight(v)
    if not m:
        return ("ZERO",)
    return (m, density(v))


W_BASIS = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, -1, -1)))
W_LEFT = matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)))
H = multiply(transpose(W_BASIS), multiply(G, W_BASIS))
H_INV = inverse(H)
A = multiply(W_LEFT, multiply(Q, multiply(D_J, W_BASIS)))
A_SHARP = gram_adjoint(A, H, H_INV)
S = multiply(A_SHARP, A)
O_STAR = matrix(((-1, -1, -1), (0, 1, 0), (0, 0, 1)))
XI_STAR = subtract(multiply(O_STAR, A), multiply(A, O_STAR))
K_FORM = multiply(transpose(A), multiply(H, A))

check("A1 authority", BASE.startswith("2a5601a9") and ISSUE == 497)
check("A2 Gram inverse", multiply(G, G_INV) == I4)
check("A3 motor", power(D_J, 5) == I4 and multiply(transpose(D_J), multiply(G, D_J)) == G)
check("A4 target-independent projectors",
      U2 == (F(-1), F(-1), F(-1), F(-1))
      and multiply(P, P) == P and rank(P) == 1
      and multiply(Q, Q) == Q and rank(Q) == 3
      and add(P, Q) == I4)

PAIR_GRAM = matrix([[trace_pair(POWERS[i], POWERS[j]) for j in range(4)] for i in range(4)])
check("R1 cyclotomic trace Gram", PAIR_GRAM == G)

ELL = (0, 1, 2, -2, -1)
V_EFF = [tuple(F(x) for x in values) for values in product(ELL, repeat=4)]
RATIONAL_CONTROLS = (
    (F(1, 2), F(-2, 3), F(3, 5), F(7, 4)),
    (F(4, 7), F(2, 5), F(-3, 8), F(9, 10)),
    (F(-5, 6), F(11, 9), F(1, 3), F(-7, 12)),
)
ALL_CONTROLS = V_EFF + list(RATIONAL_CONTROLS)

check("R2 global rank-one operator identity",
      all(trace_pair(v, v) == total_weight(v)
          and rank_one_operator(v) == multiply(outer(v, v), G)
          for v in ALL_CONTROLS))

nonzero_controls = [v for v in ALL_CONTROLS if any(v)]
check("R3 density projector identities",
      all(multiply(density(v), density(v)) == density(v)
          and gram_adjoint(density(v), G, G_INV) == density(v)
          and rank(density(v)) == 1
          and sum(density(v)[i][i] for i in range(4)) == 1
          for v in nonzero_controls))

check("R4 pure-record reconstruction",
      all(multiply(scale(total_weight(v), density(v)), G_INV) == outer(v, v)
          for v in nonzero_controls))

outer_fibres = {outer(v, v) for v in V_EFF}
record_fibres = {pure_record(v) for v in V_EFF}
check("R5 finite fibre census",
      len(V_EFF) == 625 and len(outer_fibres) == 313 and len(record_fibres) == 313)

check("C1 compressed carrier",
      H == matrix(((2, 1, 1), (1, 2, 1), (1, 1, 2)))
      and A == matrix(((-1, -1, F(-3, 4)), (0, 0, F(1, 4)), (1, 0, F(1, 4))))
      and determinant(A) == F(-1, 4)
      and sum(A[i][i] for i in range(3)) == F(-3, 4))

check("S1 scalar-blind reflection",
      multiply(transpose(O_STAR), multiply(H, O_STAR)) == H
      and multiply(O_STAR, S) == multiply(S, O_STAR)
      and XI_STAR != zeros(3)
      and rank(XI_STAR) == 2
      and multiply(transpose(O_STAR), multiply(K_FORM, O_STAR)) == K_FORM)

GRID = [tuple(F(x) for x in values)
        for values in product(range(-2, 3), repeat=3)
        if any(values)]
check("S2 scalar equality control",
      all(dot_metric(matvec(multiply(O_STAR, A), v), H, matvec(multiply(O_STAR, A), v))
          == dot_metric(matvec(multiply(A, O_STAR), v), H, matvec(multiply(A, O_STAR), v))
          for v in GRID))

check("F1 quadratic sign fibres",
      all((outer(v, v) == outer(w, w))
          == (w == v or w == tuple(-x for x in v))
          for v in GRID for w in GRID))


def centralizer_matrix(a, b, c):
    return matrix((
        (c - F(5, 4) * a, -a - F(1, 4) * b, -F(3, 4) * a + F(1, 4) * b),
        (-F(1, 4) * b, c - F(1, 4) * a - F(1, 2) * b, F(1, 4) * a - F(1, 4) * b),
        (a, b, c),
    ))


def orthogonal_error(a, b, c):
    x = centralizer_matrix(a, b, c)
    return subtract(multiply(transpose(x), multiply(H, x)), H)


COEFF = (-2, -1, 0, 1, 2)
check("F2 centralizer formula",
      all(multiply(centralizer_matrix(F(a), F(b), F(c)), A)
          == multiply(A, centralizer_matrix(F(a), F(b), F(c)))
          for a, b, c in product(COEFF, repeat=3)))

check("F3 orthogonal eliminations",
      all(orthogonal_error(F(a), F(b), F(c))[1][1]
          - orthogonal_error(F(a), F(b), F(c))[0][0]
          == F(5, 4) * b * b
          for a, b, c in product(COEFF, repeat=3))
      and all(orthogonal_error(F(a), F(0), F(c))[0][0]
              - orthogonal_error(F(a), F(0), F(c))[2][2]
              == F(a) * (7 * F(a) - 8 * F(c)) / 4
              and orthogonal_error(F(a), F(0), F(c))[0][1]
              - orthogonal_error(F(a), F(0), F(c))[0][2]
              == F(a) * (F(a) - 4 * F(c)) / 2
              for a, c in product(range(-3, 4), repeat=2))
      and all(orthogonal_error(F(0), F(0), F(c))[0][0]
              == 2 * (F(c) * F(c) - 1)
              for c in range(-4, 5)))

WITNESS = (F(1), F(0), F(0))
LEFT = matvec(multiply(O_STAR, A), WITNESS)
RIGHT = matvec(multiply(A, O_STAR), WITNESS)
check("F4 complete record separates",
      dot_metric(LEFT, H, LEFT) == dot_metric(RIGHT, H, RIGHT)
      and outer(LEFT, LEFT) != outer(RIGHT, RIGHT))

RAYS = [(F(1), F(n), F(0), F(-1 - n)) for n in range(-20, 21)]
check("D1 rational support rays",
      all(sum(v) == 0 for v in RAYS)
      and len({pure_record(v) for v in RAYS}) == len(RAYS)
      and len(RAYS) > 313 // 10)

E_LOW = scale(F(1, 4), ONE4)
check("T1 target comparison last", P == E_LOW and Q == subtract(I4, E_LOW))

failures = 0
for label, passed in CHECKS:
    print(("PASS " if passed else "FAIL ") + label)
    failures += int(not passed)

print("SCALAR_CHANNEL blind_witness_rank=2")
print("PURE_RECORD finite_fibres=313 reconstruction=exact")
print("GLOBAL_HELPER R_cyc_o_iota_B0 projectively_faithful")
print("PUBLIC_BOUNDARY finite_D_matter_domain_not_full_W")
print("BRIDGE_GATE GATE-L4-L1-QDD-PURE-RECORD UNADOPTED")
print("DECISION PURE-RECORD-BRIDGE-BOUNDARY")
print("SAMPLING NOT PROVIDED")
print("RESULT %d/%d PASS" % (len(CHECKS) - failures, len(CHECKS)))

raise SystemExit(1 if failures else 0)
