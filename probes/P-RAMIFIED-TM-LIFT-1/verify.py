#!/usr/bin/env python3
"""Exact audit for P-RAMIFIED-TM-LIFT-1.

The all-n result is proof-first.  This frozen verifier audits its finite-field
algebra, the public M_J matrix, exhaustive readout eigendata over F_5, and
large independent prefixes of the digit recursion and carry cocycle.
"""

from itertools import permutations, product


checks = []


def check(name, condition):
    checks.append((name, bool(condition)))


def quotient_bit(value):
    value %= 5
    assert value in (1, 2, 3, 4)
    return 0 if value in (1, 4) else 1


def step(vector):
    """Multiplication by J = 1 + zeta_5^2 in the power basis."""
    a, b, c, d = vector
    return (a - c + d, b - c, a, b - c + d)


def tr4(vector):
    return sum(vector)


def polynomial_add(left, right):
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return out


def polynomial_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


# Gate 01: the ramified residue and its four phases.
J_LAMBDA = (1 + 1**2) % 5
orbit = [pow(J_LAMBDA, exponent, 5) for exponent in range(4)]
check(
    "01 J_lambda = [1+zeta_5^2]_(1-zeta_5) = 2 has orbit 1,2,4,3 and order 4",
    J_LAMBDA == 2
    and orbit == [1, 2, 4, 3]
    and pow(J_LAMBDA, 2, 5) == 4
    and pow(J_LAMBDA, 4, 5) == 1,
)


# Gates 02-04: construct the C4 lift and the binary word independently by
# their digit recursions, then compare with popcount and the carry law.
LIMIT = 1 << 20
theta = bytearray(LIMIT + 1)
tm = bytearray(LIMIT + 1)
theta[0] = 1
for n in range(1, LIMIT + 1):
    parent = n >> 1
    theta[n] = (theta[parent] * (J_LAMBDA if n & 1 else 1)) % 5
    tm[n] = tm[parent] ^ (n & 1)

ok = True
for n in range(LIMIT + 1):
    pop = n.bit_count()
    ok &= theta[n] == pow(J_LAMBDA, pop, 5)
    ok &= tm[n] == (pop & 1)
    ok &= quotient_bit(theta[n]) == tm[n]
    ok &= pow(theta[n], 2, 5) == (1 if tm[n] == 0 else 4)
check(
    "02 digit automata: Theta_n=J_lambda^s2(n), q(Theta_n)=t_n, Theta_n^2=(-1)^t_n, n<=2^20",
    ok and set(theta[:8]) == {1, 2, 3, 4},
)

ok = True
for n in range(1 << 19):
    ok &= theta[2 * n] == theta[n]
    ok &= theta[2 * n + 1] == (J_LAMBDA * theta[n]) % 5
    ok &= tm[2 * n] == tm[n]
    ok &= tm[2 * n + 1] == (tm[n] ^ 1)
check(
    "03 dyadic recursion: T_0(u)=u and T_1(u)=J_lambda*u descend to Thue-Morse, n<2^19",
    ok,
)

ok = True
for n in range(LIMIT):
    carry_length = ((n + 1) & -(n + 1)).bit_length() - 1
    ok &= (n + 1).bit_count() == n.bit_count() + 1 - carry_length
    ok &= theta[n + 1] == (
        theta[n] * pow(J_LAMBDA, (1 - carry_length) % 4, 5)
    ) % 5
    ok &= tm[n + 1] == (tm[n] ^ 1 ^ (carry_length & 1))
check(
    "04 carry cocycle: s2, Theta and t increment identities hold for n<2^20",
    ok,
)


# Gates 05-07: import and independently audit the exact public CODEC-TR4
# premise.  The basis calculation proves the integer identity for all Z^4.
BASIS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
SAMPLES = BASIS + [
    (3, -2, 7, 5),
    (-4, 11, 0, -9),
    (123, -456, 789, -1011),
    (2, 1, 4, 4),
]
MATRIX = [[0] * 4 for _ in range(4)]
for column, basis_vector in enumerate(BASIS):
    image = step(basis_vector)
    for row in range(4):
        MATRIX[row][column] = image[row]

expected_matrix = [
    [1, 0, -1, 1],
    [0, 1, -1, 0],
    [1, 0, 0, 0],
    [0, 1, -1, 1],
]
check(
    "05 CODEC-TR4 premise: M_J is exact and Tr4(M_J*x)=2*Tr4(x)-5*x_zeta2",
    MATRIX == expected_matrix
    and all(tr4(step(x)) == 2 * tr4(x) - 5 * x[2] for x in SAMPLES),
)

polynomial_matrix = [
    [([-MATRIX[row][column], 1] if row == column else [-MATRIX[row][column]])
     for column in range(4)]
    for row in range(4)
]
characteristic = [0]
for permutation in permutations(range(4)):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(4)
        for j in range(i + 1, 4)
    )
    term = [-1 if inversions & 1 else 1]
    for row in range(4):
        term = polynomial_mul(term, polynomial_matrix[row][permutation[row]])
    characteristic = polynomial_add(characteristic, term)
while len(characteristic) < 5:
    characteristic.append(0)

x_minus_2_fourth = [16, -32, 24, -8, 1]
check(
    "06 char(M_J)=x^4-3x^3+4x^2-2x+1=(x-2)^4 mod 5",
    characteristic == [1, -2, 4, -3, 1]
    and [value % 5 for value in characteristic]
    == [value % 5 for value in x_minus_2_fourth],
)

left_eigenpairs = set()
for covector in product(range(5), repeat=4):
    if covector == (0, 0, 0, 0):
        continue
    image = tuple(
        sum(covector[row] * MATRIX[row][column] for row in range(4)) % 5
        for column in range(4)
    )
    for multiplier in range(5):
        if image == tuple((multiplier * value) % 5 for value in covector):
            left_eigenpairs.add((multiplier, covector))

expected_eigenpairs = {
    (2, (scalar, scalar, scalar, scalar)) for scalar in range(1, 5)
}
check(
    "07 exhaustive F5 readouts: nonzero scalar covectors form only the Tr4 line, multiplier 2",
    left_eigenpairs == expected_eigenpairs,
)


# Gate 08: all 125 residue seeds with Tr4=1.  The all-k statement itself is
# the one-line induction frozen in PREREG.md; this is a finite audit of it.
seeds = [
    vector for vector in product(range(5), repeat=4) if tr4(vector) % 5 == 1
]
ok = len(seeds) == 125
for seed in seeds:
    vector = seed
    for exponent in range(17):
        ok &= tr4(vector) % 5 == pow(J_LAMBDA, exponent, 5)
        vector = tuple(value % 5 for value in step(vector))
check(
    "08 trace lift: all 125 Tr4=1 residue seeds read J_lambda^k for 0<=k<=16",
    ok,
)


# Gates 09-10: scope guards and recovered consequences.
inverse_blind = all(
    quotient_bit(pow(3, n.bit_count(), 5)) == tm[n] for n in range(1 << 18)
)
carry_coefficients = [
    coefficient
    for coefficient in range(-4, 9)
    if all(
        x + y == (x ^ y) + coefficient * (x & y)
        for x in range(64)
        for y in range(64)
    )
]
check(
    "09 guards: inverse quotient n<2^18; carry audit -4<=mu<=8, x,y<64 selects 2",
    inverse_blind and carry_coefficients == [2],
)

ok = True
for n in range(1, LIMIT + 1):
    signed = 1 if pow(theta[n], 2, 5) == 1 else -1
    parent_signed = 1 if pow(theta[n >> 1], 2, 5) == 1 else -1
    ok &= signed == (-1 if n & 1 else 1) * parent_signed
check(
    "10 recovered breath: (-1)^t(n)=(-1)^n*(-1)^t(floor(n/2)), 1<=n<=2^20",
    ok,
)


passed = sum(result for _, result in checks)
for name, result in checks:
    print(("PASS " if result else "FAIL ") + name)
print(f"RESULT {passed}/{len(checks)} ALL PASS" if passed == len(checks) else f"RESULT {passed}/{len(checks)}")
raise SystemExit(0 if passed == len(checks) else 1)
