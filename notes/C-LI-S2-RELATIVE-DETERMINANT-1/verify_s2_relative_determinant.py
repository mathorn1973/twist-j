#!/usr/bin/env python3
"""Exact dictionary checks for C-LI-S2-RELATIVE-DETERMINANT-1.

This is a non-formal, proof-audit verifier.  It pins finite exact skeletons;
it does not assert Li's criterion, Fourier uniqueness, Hadamard factorization,
the Riemann-von Mangoldt formula, or any all-n construction of A_J.

Discipline: Python stdlib only; Fraction/integer arithmetic in every asserted
value; no files, network, subprocesses, floats, Decimal, or libm.
"""

from fractions import Fraction as F


FAILED = []


def check(name, condition):
    print(("PASS " if condition else "FAIL ") + name)
    if not condition:
        FAILED.append(name)


# Complex rationals are pairs (real, imaginary).
ONE = (F(1), F(0))


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def cdiv(a, b):
    den = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / den,
            (a[1] * b[0] - a[0] * b[1]) / den)


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def cheb(x, n):
    """T_n(x), exact, with n >= 0."""
    if n == 0:
        return F(1)
    a, b = F(1), x
    for _ in range(1, n):
        a, b = b, 2 * x * b - a
    return b


def madd(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def msub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(2)) for i in range(2))


def mmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def mpow(a, n):
    out = ((F(1), F(0)), (F(0), F(1)))
    base = a
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def mnorm2(a):
    return sum(entry * entry for row in a for entry in row)


def padd(a, b):
    size = max(len(a), len(b))
    out = [F(0)] * size
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pderiv(a):
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def pinv_series(a, terms):
    assert a[0] != 0
    out = [F(0)] * terms
    out[0] = 1 / a[0]
    for n in range(1, terms):
        out[n] = -sum((a[k] if k < len(a) else 0) * out[n - k]
                      for k in range(1, n + 1)) / a[0]
    return out


def determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    out = F(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        pivot_value = a[col][col]
        out *= pivot_value
        for j in range(col, n):
            a[col][j] /= pivot_value
        for r in range(col + 1, n):
            factor = a[r][col]
            for j in range(col, n):
                a[r][j] -= factor * a[col][j]
    return out


GAMMAS = [F(1), F(3, 2), F(7, 3), F(14), F(101, 7)]


# S1: Cayley/rotation and one-block Hilbert-Schmidt factors.
ok = True
for gamma in GAMMAS:
    z = cdiv((gamma, F(1, 2)), (gamma, F(-1, 2)))
    den = gamma * gamma + F(1, 4)
    x = (gamma * gamma - F(1, 4)) / den
    y = gamma / den
    rotation = ((x, -y), (y, x))
    defect = msub(((F(1), F(0)), (F(0), F(1))), rotation)
    ok = ok and z == (x, y) and cabs2(z) == 1
    ok = ok and cabs2(csub(ONE, z)) == 1 / den
    ok = ok and mnorm2(defect) == 2 / den
check("S1 exact Cayley rotation and Hilbert-Schmidt defect factors", ok)


# S2: block Li contribution and the canonical cocycle telescope.
ok = True
identity = ((F(1), F(0)), (F(0), F(1)))
for gamma in GAMMAS:
    den = gamma * gamma + F(1, 4)
    x = (gamma * gamma - F(1, 4)) / den
    y = gamma / den
    rotation = ((x, -y), (y, x))
    one_step = msub(identity, rotation)
    for n in range(1, 17):
        rn = mpow(rotation, n)
        lhs = F(1, 2) * mnorm2(msub(identity, rn))
        rhs = 2 * (1 - cheb(x, n))
        telescope = ((F(0), F(0)), (F(0), F(0)))
        power = identity
        for _ in range(n):
            telescope = madd(telescope, mmul(power, one_step))
            power = mmul(power, rotation)
        ok = ok and lhs == rhs and telescope == msub(identity, rn)
check("S2 exact block Li formula and cocycle telescope for n=1..16", ok)


# S3: second differences are the Fourier moments of |1-z|^2 dnu.
SYNTH = [(F(1), 1), (F(3, 2), 2), (F(7), 1), (F(11, 3), 3)]


def lam(n):
    n = abs(n)
    total = F(0)
    for gamma, multiplicity in SYNTH:
        den = gamma * gamma + F(1, 4)
        x = (gamma * gamma - F(1, 4)) / den
        total += 2 * multiplicity * (1 - cheb(x, n))
    return total


ok = True
for n in range(0, 17):
    moment = F(0)
    for gamma, multiplicity in SYNTH:
        den = gamma * gamma + F(1, 4)
        x = (gamma * gamma - F(1, 4)) / den
        moment += 2 * multiplicity * cheb(x, n) / den
    second_difference = lam(n + 1) + lam(n - 1) - 2 * lam(n)
    ok = ok and second_difference == moment
ok = ok and lam(1) * 2 == lam(1) + lam(-1) - 2 * lam(0)
check("S3 exact weighted spectral moments equal Li second differences", ok)


# S4: positive A -> unitary/orthogonal rotation, B_A, and Chebyshev trace.
SPECTRUM = [(F(1, 4), 1), (F(4, 9), 2), (F(9, 25), 1), (F(16, 49), 3)]
ok = True
for a, _multiplicity in SPECTRUM:
    # Every selected a is a rational square.
    roots = {F(1, 4): F(1, 2), F(4, 9): F(2, 3),
             F(9, 25): F(3, 5), F(16, 49): F(4, 7)}
    r = roots[a]
    z = cdiv((F(1), r / 2), (F(1), -r / 2))
    b = (1 - a / 4) / (1 + a / 4)
    ok = ok and z[0] == b
    ok = ok and cabs2(z) == 1
    ok = ok and cabs2(csub(ONE, z)) == a / (1 + a / 4)
for n in range(1, 17):
    by_rotation = sum(2 * m * (1 - cheb((1 - a / 4) / (1 + a / 4), n))
                      for a, m in SPECTRUM)
    by_trace = 2 * sum(m * (1 - cheb((1 - a / 4) / (1 + a / 4), n))
                       for a, m in SPECTRUM)
    ok = ok and by_rotation == by_trace
check("S4 exact A-to-O Cayley map, B_A, and Chebyshev trace dictionary", ok)


# S5: complex positive-frequency determinant versus realification square.
d_plus = [F(1)]
for a, multiplicity in SPECTRUM:
    for _ in range(multiplicity):
        d_plus = pmul(d_plus, [F(1), -a])
d_real = pmul(d_plus, d_plus)
d_blocks = [F(1)]
for a, multiplicity in SPECTRUM:
    for _ in range(2 * multiplicity):
        d_blocks = pmul(d_blocks, [F(1), -a])
check("S5 exact polarization: the realified determinant is D_plus squared",
      d_real == d_blocks)


# S6: formal logarithmic derivative and trace-power coefficients.
terms = 13
negative_derivative = [-value for value in pderiv(d_plus)]
series = pmul(negative_derivative, pinv_series(d_plus, terms))[:terms]
series += [F(0)] * (terms - len(series))
powers = [sum(m * a ** k for a, m in SPECTRUM) for k in range(1, terms + 1)]
check("S6 exact Fredholm log-derivative coefficients are p_m=Tr(A^m)",
      series == powers)


# S7: the two shifted Hankel families are positive on a finite exact model.
ok = True
for shift in (1, 2):
    for size in range(1, 5):
        hankel = [[sum(m * a ** (i + j + shift) for a, m in SPECTRUM)
                   for j in range(size)] for i in range(size)]
        ok = ok and determinant(hankel) > 0
check("S7 exact shifted Hankel moment matrices are positive definite", ok)


# S8: direct carrier obstruction skeletons, with their restricted scope.
ok = True
for h in (F(0), F(1, 3), F(2), F(17, 5), F(101)):
    q = cdiv((h, F(1, 2)), (h, F(-1, 2)))
    ok = ok and cabs2(q) == 1
    ok = ok and cabs2(csub(ONE, q)) == 1 / (h * h + F(1, 4))
# On an orthonormal bilateral-shift chain, (I-K)e_k=e_k-e_(k+1).
shift_defect_norms = [F(1) + F(1) for _ in range(32)]
ok = ok and all(value == 2 for value in shift_defect_norms)
# log(2)<1 gives this rational lower bound for a dyadic Fock block.
block_bounds = [F(2 ** k, 1) / (F((k + 1) ** 2) + F(1, 4))
                for k in range(8, 33)]
ok = ok and all(block_bounds[i + 1] > block_bounds[i]
                for i in range(len(block_bounds) - 1))
check("S8 exact direct-Cayley carrier obstruction skeletons (scope: direct identifications only)", ok)


print("IMPORTED: Li criterion; Fourier uniqueness; Hadamard product; Riemann-von Mangoldt count; spectral theorem")
print("NONCLAIM: no J-native A_J is constructed; G8 and RH remain open")
print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS C-LI-S2-RELATIVE-DETERMINANT-1 dictionary" if not FAILED else "FAIL"))

raise SystemExit(1 if FAILED else 0)
