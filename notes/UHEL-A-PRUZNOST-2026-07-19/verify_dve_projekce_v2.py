#!/usr/bin/env python3
"""Exact non-canonical audit for the two projections overview, version 2.

The script uses Z[zeta_5] in the power basis (1, j, j^2, j^3), exact
integers only, and the Python standard library only.  It audits algebraic
identities and finite prefixes.  Physical identifications are out of scope.

Any failed check produces a nonzero exit code.
"""

ONE = (1, 0, 0, 0)
JGEN = (0, 1, 0, 0)          # j
J = (1, 0, 1, 0)             # J = 1 + j^2
PHI = (0, 0, -1, -1)         # phi = -j^2 - j^3
LAM = (1, -1, 0, 0)          # lambda = 1 - j
TWO = (2, 0, 0, 0)
J4 = (-1, -1, -1, -1)        # j^4


def mul(x, y):
    """Multiply exactly in Z[j]/(1+j+j^2+j^3+j^4)."""
    coefficients = [0] * 5
    for i in range(4):
        if x[i] == 0:
            continue
        for k in range(4):
            coefficients[(i + k) % 5] += x[i] * y[k]
    return tuple(coefficients[i] - coefficients[4] for i in range(4))


def sigma(x, k):
    """Apply the Galois embedding j -> j^k for k in {1,2,3,4}."""
    coefficients = [0] * 5
    for i in range(4):
        coefficients[(i * k) % 5] += x[i]
    return tuple(coefficients[i] - coefficients[4] for i in range(4))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def power(x, exponent):
    result = ONE
    for _ in range(exponent):
        result = mul(result, x)
    return result


def step(a, b, c, d):
    return (a - c + d, b - c, a, b - c + d)


def quotient_bit(value):
    value %= 5
    if value not in (1, 2, 3, 4):
        raise ValueError("the sign quotient is defined on F_5^x")
    return 0 if value in (1, 4) else 1


def binary_digit_sum(number):
    """Return s_2(number) without requiring int.bit_count (Python 3.8+)."""
    total = 0
    while number:
        total += number & 1
        number >>= 1
    return total


checks = []


def check(label, condition):
    checks.append((label, bool(condition)))


# Principal-embedding polar algebra.  The logarithmic branch statement is
# kept in the note; the exact algebraic skeleton is audited here.
check("J*phi = j", mul(J, PHI) == JGEN)
check("phi^2 = phi + 1", mul(PHI, PHI) == add(PHI, ONE))
J_BAR = sigma(J, 4)
MODULUS_SQUARED = mul(J, J_BAR)
check("J*Jbar = 2 - phi", MODULUS_SQUARED == sub(TWO, PHI))
check("(2 - phi)*phi^2 = 1", mul(MODULUS_SQUARED, power(PHI, 2)) == ONE)
check("Jbar*phi = j^4", mul(J_BAR, PHI) == J4)
check("J^5*phi^5 = 1", mul(power(J, 5), power(PHI, 5)) == ONE)


# Galois scale balance.
S1, S2, S3, S4 = (sigma(J, k) for k in (1, 2, 3, 4))
check("N(J) = 1", mul(mul(S1, S2), mul(S3, S4)) == ONE)
check(
    "Galois modulus pairs are phi^-2 and phi^2",
    mul(S1, S4) == sub(TWO, PHI)
    and mul(S2, S3) == add(PHI, ONE),
)
check("Tr(J) = 3", add(add(S1, S2), add(S3, S4)) == (3, 0, 0, 0))
check("(J - 1)^3 = j", power(sub(J, ONE), 3) == JGEN)


# The canonical integral step.
step_ok = True
for a in range(-2, 3):
    for b in range(-2, 3):
        for c in range(-2, 3):
            for d in range(-2, 3):
                step_ok &= step(a, b, c, d) == mul((a, b, c, d), J)
check("the canonical step equals multiplication by J on 625 states", step_ok)


# Ramified residue and a scope guard separating its order four from the
# archimedean phase root of order five.
N_LAMBDA = mul(
    mul(sigma(LAM, 1), sigma(LAM, 2)),
    mul(sigma(LAM, 3), sigma(LAM, 4)),
)
check(
    "J - 2 = -(1+j)*lambda and N(lambda) = 5",
    sub(J, TWO) == neg(mul((1, 1, 0, 0), LAM))
    and N_LAMBDA == (5, 0, 0, 0),
)
check(
    "order guard: j has order 5 while J_lambda=2 has order 4",
    power(JGEN, 5) == ONE
    and all(power(JGEN, k) != ONE for k in range(1, 5))
    and pow(2, 4, 5) == 1
    and all(pow(2, k, 5) != 1 for k in range(1, 4)),
)


# Binary addition.  The finite sweep audits the implementation.  The note
# supplies the all-N place-value proof and the one-case uniqueness proof.
binary_ok = all(
    x + y == (x ^ y) + 2 * (x & y)
    for x in range(256)
    for y in range(256)
)
check("binary adder identity on all 65536 pairs in [0,255]^2", binary_ok)
check(
    "the integer carry coefficient is uniquely forced to 2 by x=y=1",
    [
        coefficient
        for coefficient in range(-8, 9)
        if 1 + 1 == (1 ^ 1) + coefficient * (1 & 1)
    ] == [2],
)


# Ramified four-phase lift and its chronological carry cocycle.  These are
# finite audits only; the all-N proof belongs to P-RAMIFIED-TM-LIFT-1.
LIMIT = 1 << 18
theta = bytearray(LIMIT + 1)
thue_morse = bytearray(LIMIT + 1)
theta[0] = 1
for n in range(1, LIMIT + 1):
    parent = n >> 1
    theta[n] = theta[parent] * (2 if n & 1 else 1) % 5
    thue_morse[n] = thue_morse[parent] ^ (n & 1)

lift_ok = True
for n in range(LIMIT + 1):
    digit_sum = binary_digit_sum(n)
    lift_ok &= theta[n] == pow(2, digit_sum, 5)
    lift_ok &= quotient_bit(theta[n]) == (digit_sum & 1) == thue_morse[n]
    lift_ok &= pow(theta[n], 2, 5) == (1 if thue_morse[n] == 0 else 4)
check("ramified C4 -> C2 Thue-Morse lift through n=2^18", lift_ok)

carry_ok = True
for n in range(LIMIT):
    carry_length = ((n + 1) & -(n + 1)).bit_length() - 1
    carry_ok &= (
        binary_digit_sum(n + 1)
        == binary_digit_sum(n) + 1 - carry_length
    )
    carry_ok &= theta[n + 1] == theta[n] * pow(2, (1 - carry_length) % 4, 5) % 5
    carry_ok &= thue_morse[n + 1] == (
        thue_morse[n] ^ 1 ^ (carry_length & 1)
    )
check("chronological carry cocycle through n<2^18", carry_ok)


# Base-five digit/carry audit.
def digits_base_five(number):
    digits = []
    while number:
        digits.append(number % 5)
        number //= 5
    return digits or [0]


base_five_ok = True
for a in range(625):
    for b in range(625):
        digits_a = digits_base_five(a)
        digits_b = digits_base_five(b)
        length = max(len(digits_a), len(digits_b))
        digits_a += [0] * (length - len(digits_a))
        digits_b += [0] * (length - len(digits_b))
        digit_sum = sum(
            ((digits_a[i] + digits_b[i]) % 5) * 5**i
            for i in range(length)
        )
        carry = sum(
            ((digits_a[i] + digits_b[i]) // 5) * 5**i
            for i in range(length)
        )
        base_five_ok &= a + b == digit_sum + 5 * carry

wheel_ok = True
for digit in range(5):
    value = digit
    carries = 0
    for _ in range(5):
        value += 1
        if value == 5:
            value = 0
            carries += 1
    wheel_ok &= value == digit and carries == 1

check(
    "base-five digit/carry identity on 625^2 pairs and the five-step wheel",
    base_five_ok and wheel_ok,
)


passed = sum(result for _, result in checks)
for index, (label, result) in enumerate(checks, 1):
    print(("PASS" if result else "FAIL"), f"{index:2d}:", label)

if passed == len(checks):
    print(f"{passed}/{len(checks)} ALL PASS")
    raise SystemExit(0)

print(f"{passed}/{len(checks)} SOME FAIL")
raise SystemExit(1)
