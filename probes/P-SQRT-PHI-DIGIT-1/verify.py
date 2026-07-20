#!/usr/bin/env python3
"""Exact audit for P-SQRT-PHI-DIGIT-1.

The all-n result is proof-first. This frozen verifier exhausts the F_25
field and the restricted C8 norm sequence, then audits both digit branches
and the chronological carry law on a fixed finite prefix.
"""


P = 5
ZERO = (0, 0)
ONE = (1, 0)
MINUS_ONE = (4, 0)
J = (2, 0)
PHI = (3, 0)
TAU = (0, 1)
N_MAX = 1 << 18

checks = []


def check(name, condition):
    checks.append((name, bool(condition)))


def neg(value):
    return ((-value[0]) % P, (-value[1]) % P)


def mul(left, right):
    """Multiply pairs in F_5[tau]/(tau^2 - 2)."""
    a, b = left
    c, d = right
    return ((a * c + 2 * b * d) % P, (a * d + b * c) % P)


def power(value, exponent):
    if exponent < 0:
        raise ValueError("power expects a nonnegative exponent")
    out = ONE
    base = value
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent >>= 1
    return out


def inverse(value):
    if value == ZERO:
        raise ZeroDivisionError("zero has no multiplicative inverse")
    return power(value, 23)


def norm(value):
    return mul(value, power(value, 5))


def norm_formula(value):
    a, b = value
    return ((a * a - 2 * b * b) % P, 0)


def order(value):
    if value == ZERO:
        raise ValueError("zero has no multiplicative order")
    for exponent in range(1, 25):
        if power(value, exponent) == ONE:
            return exponent
    raise ArithmeticError("unit order does not divide 24")


def encode(value):
    return 5 * value[0] + value[1]


def decode(code):
    return divmod(code, 5)


def quotient_bit(value):
    if value[1] != 0 or value[0] not in (1, 2, 3, 4):
        raise ValueError("quotient expects an embedded F_5 unit")
    return 0 if value[0] in (1, 4) else 1


def valuation_two_positive(value):
    if value <= 0:
        raise ValueError("valuation expects a positive integer")
    return (value & -value).bit_length() - 1


def build_digit_branch(root):
    sequence = bytearray(N_MAX + 1)
    sequence[0] = encode(ONE)
    for n in range(1, N_MAX + 1):
        parent = decode(sequence[n >> 1])
        value = parent if not (n & 1) else mul(root, parent)
        sequence[n] = encode(value)
    return sequence


elements = [(a, b) for a in range(P) for b in range(P)]
units = [value for value in elements if value != ZERO]
ETA = power(TAU, 3)
NEG_ETA = neg(ETA)


# Gate 01: audit the field model before using it downstream.
scalar_squares = {(value * value) % P for value in range(P)}
no_zero_divisors = all(mul(left, right) != ZERO for left in units for right in units)
all_inverses = all(mul(value, inverse(value)) == ONE for value in units)
all_norms = all(norm(value) == norm_formula(value) for value in elements)
check(
    "01 FIELD        F_25 pair model exact; tau^2=J, tau^5=-tau; eta=tau^3 has eta^2=phi, eta^4=-1, order 8, norm J",
    scalar_squares == {0, 1, 4}
    and no_zero_divisors
    and all_inverses
    and all_norms
    and ETA == (0, 2)
    and NEG_ETA == (0, 3)
    and power(TAU, 2) == J
    and power(TAU, 5) == neg(TAU)
    and power(ETA, 2) == PHI
    and power(ETA, 4) == MINUS_ONE
    and order(ETA) == 8
    and norm(ETA) == J,
)


# Gate 02: exhaust the full field for square roots of phi.
phi_roots = {value for value in elements if mul(value, value) == PHI}
check(
    "02 ROOTS        r^2=phi has exactly {eta,-eta}; both roots have order 8 and norm J",
    phi_roots == {ETA, NEG_ETA}
    and all(order(root) == 8 for root in phi_roots)
    and all(norm(root) == J for root in phi_roots),
)


# Gate 03: exactness and nonsplitting of the restricted C8 -> C4 norm.
c8 = {power(ETA, exponent) for exponent in range(8)}
c4 = {(pow(2, exponent, P), 0) for exponent in range(4)}
image = {norm(value) for value in c8}
kernel = {value for value in c8 if norm(value) == ONE}
preimage_j = {value for value in c8 if norm(value) == J}
homomorphism = all(
    norm(mul(left, right)) == mul(norm(left), norm(right))
    for left in c8
    for right in c8
)
check(
    "03 EXACT-SEQ    1->{+/-1}-><eta>--N--><J>->1 is exact and nonsplit",
    len(c8) == 8
    and len(c4) == 4
    and image == c4
    and kernel == {ONE, MINUS_ONE}
    and preimage_j == {ETA, NEG_ETA}
    and homomorphism
    and all(order(value) == 8 for value in preimage_j),
)


# Gate 04: construct both branches by recursion, independently of popcount.
y_plus = build_digit_branch(ETA)
y_minus = build_digit_branch(NEG_ETA)
digit_ok = True
for root, sequence in ((ETA, y_plus), (NEG_ETA, y_minus)):
    expected_states = {encode(power(root, exponent)) for exponent in range(8)}
    digit_ok &= set(sequence) == expected_states
    for n in range(N_MAX + 1):
        digit_ok &= decode(sequence[n]) == power(root, n.bit_count())
check(
    "04 DIGIT        both digit recursions equal r_epsilon^s2(n) for 0<=n<=2^18 and visit all 8 states",
    digit_ok,
)


# Gate 05: compare with independently calculated C4 and C2 projections.
tower_ok = True
for n in range(N_MAX + 1):
    popcount = n.bit_count()
    theta = popcount & 1
    theta_lift = (pow(2, popcount, P), 0)
    theta_inverse = (pow(3, popcount, P), 0)
    sign = ONE if theta == 0 else MINUS_ONE
    plus = decode(y_plus[n])
    minus = decode(y_minus[n])
    for value in (plus, minus):
        square = mul(value, value)
        fourth = mul(square, square)
        tower_ok &= norm(value) == theta_lift
        tower_ok &= quotient_bit(norm(value)) == theta
        tower_ok &= square == theta_inverse
        tower_ok &= fourth == sign
    tower_ok &= minus == (plus if theta == 0 else neg(plus))
check(
    "05 TOWER        N(Y)=Theta, q(N(Y))=theta, Y^2=Theta^-1, Y^4=(-1)^theta, Y^-=(-1)^theta Y^+ for 0<=n<=2^18",
    tower_ok,
)


# Gate 06: chronological carry law and the nonconstant-multiplier witness.
chronology_ok = True
carry_values = set()
for root, sequence in ((ETA, y_plus), (NEG_ETA, y_minus)):
    for n in range(N_MAX):
        carry = valuation_two_positive(n + 1)
        carry_values.add(carry)
        chronology_ok &= (n + 1).bit_count() == n.bit_count() + 1 - carry
        expected = mul(decode(sequence[n]), power(root, (1 - carry) % 8))
        chronology_ok &= decode(sequence[n + 1]) == expected
    ratio_zero = mul(decode(sequence[1]), inverse(decode(sequence[0])))
    ratio_one = mul(decode(sequence[2]), inverse(decode(sequence[1])))
    chronology_ok &= ratio_zero == root
    chronology_ok &= ratio_one == ONE
    chronology_ok &= root != ONE
check(
    "06 CHRONOLOGY   Y(n+1)=Y(n)r^(1-nu2(n+1)) for 0<=n<2^18; multipliers at n=0,1 are r and 1",
    chronology_ok and carry_values == set(range(19)),
)


passed = sum(result for _, result in checks)
for name, result in checks:
    print(("PASS " if result else "FAIL ") + name)
if passed == len(checks):
    print(f"RESULT {passed}/{len(checks)} ALL PASS")
else:
    print(f"RESULT {passed}/{len(checks)} FAILURES PRESENT")
raise SystemExit(0 if passed == len(checks) else 1)
