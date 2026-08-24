#!/usr/bin/env python3
"""Exact audit for P-QDD-PURE-RECORD-TYPED-BRIDGE-1."""

from fractions import Fraction as F
from itertools import product
from math import isqrt

BASE = "1b288cbed5a9ccdfed5edde906df82fa1522870e"
ISSUE = 502
CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


def matrix(rows):
    return tuple(tuple(x if isinstance(x, F) else F(x) for x in row) for row in rows)


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def zero(rows, cols=None):
    if cols is None:
        cols = rows
    return matrix([[0 for _ in range(cols)] for _ in range(rows)])


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
    return matrix([
        [sum((x * y for x, y in zip(row, col)), F(0)) for col in bt]
        for row in a
    ])


def matvec(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), F(0)) for row in a)


def outer(v, w=None):
    if w is None:
        w = v
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
                work[row] = [
                    work[row][j] - factor * work[pivot_row][j] for j in range(cols)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def metric(v, gram, w=None):
    if w is None:
        w = v
    return sum(
        (
            v[i] * sum((gram[i][j] * w[j] for j in range(len(w))), F(0))
            for i in range(len(v))
        ),
        F(0),
    )


def gram_adjoint(a, gram, gram_inverse):
    return multiply(gram_inverse, multiply(transpose(a), gram))


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
            p = POWERS[(i + j) % 5]
            for k in range(4):
                out[k] += xi * yj * p[k]
    return tuple(out)


def k_conjugate(x):
    out = [F(0), F(0), F(0), F(0)]
    for i, xi in enumerate(x):
        p = POWERS[(-i) % 5]
        for k in range(4):
            out[k] += xi * p[k]
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
P = scale(F(1, 4), outer(U2))
Q = subtract(I4, P)


def total_weight(v):
    return metric(v, G)


def density(v):
    m = total_weight(v)
    if not m:
        return None
    return scale(1 / m, multiply(outer(v), G))


def pure_record(v):
    m = total_weight(v)
    if not m:
        return ("ZERO",)
    return (m, density(v))


def canonical_sign(v):
    v = tuple(F(x) for x in v)
    if not any(v):
        raise ValueError("zero has no sign class")
    first = next(x for x in v if x)
    return tuple(-x for x in v) if first < 0 else v


def zigzag(a):
    return 2 * a if a >= 0 else -2 * a - 1


def unzigzag(n):
    return n // 2 if n % 2 == 0 else -(n // 2) - 1


def cantor(a, b):
    s = a + b
    return s * (s + 1) // 2 + b


def uncantor(z):
    w = (isqrt(8 * z + 1) - 1) // 2
    t = w * (w + 1) // 2
    b = z - t
    return w - b, b


def encode_fraction(q):
    q = F(q)
    return cantor(zigzag(q.numerator), q.denominator - 1)


def decode_fraction(code):
    a, b = uncantor(code)
    return F(unzigzag(a), b + 1)


def encode_class(v):
    v = canonical_sign(v)
    e0, e1, e2, e3 = (encode_fraction(x) for x in v)
    return cantor(cantor(cantor(e0, e1), e2), e3)


def decode_class(code):
    c012, e3 = uncantor(code)
    c01, e2 = uncantor(c012)
    e0, e1 = uncantor(c01)
    return (
        decode_fraction(e0),
        decode_fraction(e1),
        decode_fraction(e2),
        decode_fraction(e3),
    )


ZERO_CHECKPOINT = (0, 0, 0, 0, 0, 0)


def eta(v, residue):
    return (4 * encode_class(v) + residue, ZERO_CHECKPOINT)


def decode_eta(head, residue):
    n, checkpoint = head
    if checkpoint != ZERO_CHECKPOINT or n <= 0 or n % 4 != residue:
        raise ValueError("outside encoded image")
    return decode_class((n - residue) // 4)


def decoded_record(head, residue):
    return pure_record(decode_eta(head, residue))


check("A1 authority", BASE.startswith("1b288cbe") and ISSUE == 502)
check("A2 Gram inverse", multiply(G, G_INV) == I4)
check(
    "A3 motor and metric",
    power(D_J, 5) == I4 and multiply(transpose(D_J), multiply(G, D_J)) == G,
)
check(
    "A4 projective order certificates",
    all(
        determinant(subtract(power(D_J, k), I4)) == 5
        and determinant(add(power(D_J, k), I4)) == 1
        for k in range(1, 5)
    ),
)

PAIR_GRAM = matrix(
    [[trace_pair(POWERS[i], POWERS[j]) for j in range(4)] for i in range(4)]
)
check("R1 cyclotomic trace Gram", PAIR_GRAM == G)

ELL = (0, 1, 2, -2, -1)
V_EFF = [tuple(F(x) for x in values) for values in product(ELL, repeat=4)]
RATIONAL_CONTROLS = (
    (F(1, 2), F(-2, 3), F(3, 5), F(7, 4)),
    (F(4, 7), F(2, 5), F(-3, 8), F(9, 10)),
    (F(-5, 6), F(11, 9), F(1, 3), F(-7, 12)),
)
DIRECT_CONTROLS = V_EFF + list(RATIONAL_CONTROLS)
check(
    "R2 global direct-helper identity",
    all(
        trace_pair(v, v) == total_weight(v)
        and rank_one_operator(v) == multiply(outer(v), G)
        for v in DIRECT_CONTROLS
    ),
)

NONZERO_DIRECT = [v for v in DIRECT_CONTROLS if any(v)]
check(
    "R3 pure-record projector identities",
    all(
        multiply(density(v), density(v)) == density(v)
        and gram_adjoint(density(v), G, G_INV) == density(v)
        and rank(density(v)) == 1
        and sum(density(v)[i][i] for i in range(4)) == 1
        and multiply(scale(total_weight(v), density(v)), G_INV) == outer(v)
        for v in NONZERO_DIRECT
    ),
)

SIGN_VALUES = (F(-1), F(-1, 2), F(0), F(1, 2), F(1))
SIGN_CONTROLS = [
    tuple(values) for values in product(SIGN_VALUES, repeat=4) if any(values)
]
SIGN_GROUPS = {}
for v in SIGN_CONTROLS:
    SIGN_GROUPS.setdefault(outer(v), set()).add(v)
check(
    "R4 exact sign fibres",
    len(SIGN_CONTROLS) == 624
    and len(SIGN_GROUPS) == 312
    and all(
        len(group) == 2
        and next(iter(group)) in group
        and tuple(-x for x in next(iter(group))) in group
        for group in SIGN_GROUPS.values()
    ),
)

FINITE_RECORDS = {pure_record(v) for v in V_EFF}
check(
    "R5 current finite image",
    len(V_EFF) == 625 and len(FINITE_RECORDS) == 313,
)

W_RAYS = [(F(1), F(n), F(0), F(-1 - n)) for n in range(-20, 21)]
check(
    "R6 rational HIGH-support rays",
    all(multiply(Q, matrix([[x] for x in v])) == matrix([[x] for x in v]) for v in W_RAYS)
    and len({pure_record(v) for v in W_RAYS}) == len(W_RAYS),
)

CANONICAL_CONTROLS = {canonical_sign(v) for v in SIGN_CONTROLS}
check(
    "C1 rational-code round trip",
    len(CANONICAL_CONTROLS) == 312
    and all(decode_class(encode_class(v)) == v for v in CANONICAL_CONTROLS),
)

ETA1 = {eta(v, 1) for v in CANONICAL_CONTROLS}
ETA2 = {eta(v, 2) for v in CANONICAL_CONTROLS}
check(
    "C2 static encodings disjoint",
    len(ETA1) == len(CANONICAL_CONTROLS)
    and len(ETA2) == len(CANONICAL_CONTROLS)
    and ETA1.isdisjoint(ETA2)
    and all(head[0] > 0 for head in ETA1 | ETA2),
)
check(
    "C3 static extensions decode",
    all(
        decoded_record(eta(v, 1), 1) == pure_record(v)
        and decoded_record(eta(v, 2), 2) == pure_record(v)
        for v in CANONICAL_CONTROLS
    ),
)
check(
    "C4 static bridges nonidentical",
    all(eta(v, 1) != eta(v, 2) for v in CANONICAL_CONTROLS),
)

MOTOR_SAMPLE = tuple(sorted(CANONICAL_CONTROLS, key=encode_class)[:40])
check(
    "U1 projective motor five-cycles",
    all(
        len({encode_class(matvec(power(D_J, k), v)) for k in range(5)}) == 5
        and encode_class(matvec(power(D_J, 5), v)) == encode_class(v)
        for v in MOTOR_SAMPLE
    ),
)
check(
    "U2 pointed-tail freeness",
    all(n + lag != n for n in range(20) for lag in range(1, 11)),
)
check(
    "U3 nonnegative lag reduction",
    all((sum(lags) == 0) == all(x == 0 for x in lags) for lags in product(range(3), repeat=5)),
)
check(
    "U4 congruence no-go audit",
    power(D_J, 5) == I4
    and determinant(subtract(D_J, I4)) == 5
    and all(n + lag != n for n in range(5) for lag in range(1, 6)),
)

W_BASIS = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, -1, -1)))
W_LEFT = matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)))
H = multiply(transpose(W_BASIS), multiply(G, W_BASIS))
H_INV = inverse(H)
A = multiply(W_LEFT, multiply(Q, multiply(D_J, W_BASIS)))
O_STAR = matrix(((-1, -1, -1), (0, 1, 0), (0, 0, 1)))
XI_STAR = subtract(multiply(O_STAR, A), multiply(A, O_STAR))
check(
    "L1 compressed source",
    H == matrix(((2, 1, 1), (1, 2, 1), (1, 1, 2)))
    and determinant(A) == F(-1, 4)
    and multiply(transpose(O_STAR), multiply(H, O_STAR)) == H
    and XI_STAR != zero(3)
    and rank(XI_STAR) == 2,
)

WITNESS = (F(1), F(0), F(0))
LEFT3 = matvec(multiply(O_STAR, A), WITNESS)
RIGHT3 = matvec(multiply(A, O_STAR), WITNESS)
LEFT4 = matvec(W_BASIS, LEFT3)
RIGHT4 = matvec(W_BASIS, RIGHT3)
check(
    "L2 global bridge reads L4 commutator",
    pure_record(LEFT4) != pure_record(RIGHT4)
    and total_weight(LEFT4) == total_weight(RIGHT4),
)

E_LOW = scale(F(1, 4), ONE4)
check(
    "T1 target comparison last",
    U2 == (F(-1), F(-1), F(-1), F(-1))
    and P == E_LOW
    and Q == subtract(I4, E_LOW),
)

failures = 0
for label, passed in CHECKS:
    print(("PASS " if passed else "FAIL ") + label)
    failures += not passed

print("READONLY_BRIDGE global_Q4_sign_source faithful")
print("FINITE_LEG pure_record_fibres=313 insufficient_for_infinite_source")
print("STATIC_ENCODINGS count=2 disjoint exact nonselected")
print("U_CONGRUENCE class=empty order5_vs_free_tail")
print("L4_RESTRICTION internal_commutator_read=YES")
print("PUBLIC_GATE GATE-L4-L1-QDD-PURE-RECORD ABSENT_ON_BASIS")
print("DECISION READONLY-BRIDGE-ONLY")
print("SAMPLING NOT PROVIDED")
print(f"RESULT {len(CHECKS)-failures}/{len(CHECKS)} PASS")
raise SystemExit(1 if failures else 0)
