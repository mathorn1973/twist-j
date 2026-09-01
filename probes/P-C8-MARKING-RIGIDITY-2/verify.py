#!/usr/bin/env python3
"""Exact audit for P-C8-MARKING-RIGIDITY-2.

Standard library only. Exact integer and rational arithmetic throughout.
No floating point, complex builtin arithmetic, files, subprocesses, network,
random choice, dynamic imports, eval, exec, or external packages.
"""

from fractions import Fraction
from math import isqrt

FAILURES = []


def gate(name, ok, message):
    if not ok:
        FAILURES.append(name)
    print("%s %s: %s" % (name, "PASS" if ok else "FAIL", message))


# ---------------------------------------------------------------------------
# F_25 = F_5[t]/(t^2 - 2)


def f25_mul(x, y):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % 5, (a * d + b * c) % 5)


def f25_pow(x, n):
    out = (1, 0)
    base = x
    while n:
        if n & 1:
            out = f25_mul(out, base)
        base = f25_mul(base, base)
        n >>= 1
    return out


def f25_order(x):
    if x == (0, 0):
        return 0
    for n in range(1, 25):
        if f25_pow(x, n) == (1, 0):
            return n
    return 0


def order_mod(a, p):
    a %= p
    if a == 0:
        return 0
    value = 1
    for n in range(1, p):
        value = (value * a) % p
        if value == 1:
            return n
    return 0


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n)
    d = 3
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True


# ---------------------------------------------------------------------------
# Q(zeta_8) = Q[z]/(z^4 + 1), exact Fraction coordinates

Q = Fraction
ZERO = (Q(0), Q(0), Q(0), Q(0))
ONE = (Q(1), Q(0), Q(0), Q(0))


def q_add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def q_scale(c, x):
    c = Q(c)
    return tuple(c * a for a in x)


def q_mul(x, y):
    raw = [Q(0) for _ in range(7)]
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            raw[i + j] += a * b
    for degree in range(6, 3, -1):
        raw[degree - 4] -= raw[degree]
    return tuple(raw[:4])


def zeta8(k):
    k %= 8
    sign = 1
    if k >= 4:
        k -= 4
        sign = -1
    out = [Q(0), Q(0), Q(0), Q(0)]
    out[k] = Q(sign)
    return tuple(out)


def q_conj(x):
    out = ZERO
    for power, coeff in enumerate(x):
        out = q_add(out, q_scale(coeff, zeta8(-power)))
    return out


def q_is_rational(x):
    return x[1] == 0 and x[2] == 0 and x[3] == 0


INV_SQRT2 = q_scale(Q(1, 2), q_add(zeta8(1), q_scale(-1, zeta8(3))))

I2 = ((ONE, ZERO), (ZERO, ONE))
X = ((ZERO, ONE), (ONE, ZERO))
Y = ((ZERO, q_scale(-1, zeta8(2))), (zeta8(2), ZERO))
Z = ((ONE, ZERO), (ZERO, q_scale(-1, ONE)))
PAULI = (("I", I2), ("X", X), ("Y", Y), ("Z", Z))


def phase_gate(k):
    return ((ONE, ZERO), (ZERO, zeta8(k)))


def kron(A, B):
    return tuple(
        tuple(q_mul(A[i // 2][j // 2], B[i % 2][j % 2]) for j in range(4))
        for i in range(4)
    )


def mat_vec(A, v):
    out = []
    for i in range(4):
        total = ZERO
        for j in range(4):
            total = q_add(total, q_mul(A[i][j], v[j]))
        out.append(total)
    return tuple(out)


def inner(u, v):
    total = ZERO
    for a, b in zip(u, v):
        total = q_add(total, q_mul(q_conj(a), b))
    return total


# ---------------------------------------------------------------------------
# G1

tau = (0, 1)
squares = sorted({(x * x) % 5 for x in range(1, 5)})
nonsquares = sorted(x for x in range(1, 5) if x not in squares)

g1 = (
    f25_pow(tau, 2) == (2, 0)
    and f25_pow(tau, 4) == (4, 0)
    and f25_order(tau) == 8
    and order_mod(2, 5) == 4
    and nonsquares == [2, 3]
)
gate("G1", g1, "marked datum exact: tau^2=2, tau^4=-1, ord(tau)=8, ord_5(2)=4, nonsquares {2,3}")


# ---------------------------------------------------------------------------
# G2, theorem audit plus exact integer finite scan

divisor_primes = [p for p in range(2, 16) if 15 % p == 0 and is_prime(p)]
survivors = [p for p in divisor_primes if 3 % p != 0]
scan = [p for p in range(3, 20000, 2) if is_prime(p) and order_mod(2, p) == 4]

g2 = divisor_primes == [3, 5] and survivors == [5] and order_mod(2, 3) == 2 and scan == [5]
gate("G2", g2, "rigidity: ord_p(2)=4 forces p|15 and p not|3, hence p=5; integer isqrt scan below 20000 returns [5]")


# ---------------------------------------------------------------------------
# G3

roots = {}
orders = {}
for m in range(1, 5):
    roots[m] = [
        (a, b)
        for a in range(5)
        for b in range(5)
        if f25_mul((a, b), (a, b)) == (m, 0)
    ]
    orders[m] = sorted({f25_order(r) for r in roots[m]})

g3 = (
    all(len(roots[m]) == 2 for m in range(1, 5))
    and orders[2] == [8]
    and orders[3] == [8]
    and 8 not in orders[1]
    and 8 not in orders[4]
)
gate("G3", g3, "over F_5 every nonsquare marking gives order-8 roots and square markings give none")


# ---------------------------------------------------------------------------
# G4

g4 = (
    (2 * 3) % 5 == 1
    and nonsquares == [2, 3]
    and f25_pow(tau, 6) == (3, 0)
    and f25_pow(tau, 14) == (3, 0)
    and f25_pow(tau, 10) == (2, 0)
)
gate("G4", g4, "source orientation is 2 versus 2^-1=3; tau^3 and tau^7 square to 3 while tau^5 squares to 2")


# ---------------------------------------------------------------------------
# G5

units8 = [1, 3, 5, 7]
frob = 5
conj = 7
involutions = (frob * frob) % 8 == 1 and (conj * conj) % 8 == 1
commute = (frob * conj) % 8 == (conj * frob) % 8
generated = sorted({(pow(frob, a, 8) * pow(conj, b, 8)) % 8 for a in (0, 1) for b in (0, 1)})
orbits = [
    sorted({(u * pow(frob, a, 8) * pow(conj, b, 8)) % 8 for a in (0, 1) for b in (0, 1)})
    for u in units8
]
g5 = frob != conj and involutions and commute and generated == units8 and all(o == units8 for o in orbits)
gate("G5", g5, "Frobenius exponent 5 and conjugation exponent 7 are commuting involutions generating a free transitive action on {1,3,5,7}")


# ---------------------------------------------------------------------------
# G6

bell = (INV_SQRT2, ZERO, ZERO, INV_SQRT2)
psi1 = mat_vec(kron(phase_gate(1), phase_gate(1)), bell)
psi7 = mat_vec(kron(phase_gate(7), phase_gate(7)), bell)
conjugate_pair = psi7 == tuple(q_conj(a) for a in psi1)

separating = []
rational_separating = []
values_rational = True
rational_basis_count = 0

for name_a, A in PAULI:
    for name_b, B in PAULI:
        observable = kron(A, B)
        rational_entries = all(q_is_rational(entry) for row in observable for entry in row)
        if rational_entries:
            rational_basis_count += 1
        e1 = inner(psi1, mat_vec(observable, psi1))
        e7 = inner(psi7, mat_vec(observable, psi7))
        if not (q_is_rational(e1) and q_is_rational(e7)):
            values_rational = False
        if e1 != e7:
            label = name_a + name_b
            separating.append(label)
            if rational_entries:
                rational_separating.append(label)

separating.sort()
rational_separating.sort()
xy1 = inner(psi1, mat_vec(kron(X, Y), psi1))
xy7 = inner(psi7, mat_vec(kron(X, Y), psi7))
yx1 = inner(psi1, mat_vec(kron(Y, X), psi1))
yx7 = inner(psi7, mat_vec(kron(Y, X), psi7))

g6 = (
    conjugate_pair
    and values_rational
    and rational_basis_count == 10
    and rational_separating == []
    and separating == ["XY", "YX"]
    and xy1 == ONE
    and xy7 == q_scale(-1, ONE)
    and yx1 == ONE
    and yx7 == q_scale(-1, ONE)
)
gate("G6", g6, "relative no-go: 10 rational-entry Pauli products do not separate conjugate orientations; separating set is XY,YX with signs +1,-1")


TOTAL = 6
passed = TOTAL - len(FAILURES)
print("RESULT %d/%d %s: exact integer repair audit; no physical bridge; marking remains a dictionary input" % (
    passed,
    TOTAL,
    "ALL PASS" if not FAILURES else "FAIL " + ",".join(FAILURES),
))
raise SystemExit(1 if FAILURES else 0)
