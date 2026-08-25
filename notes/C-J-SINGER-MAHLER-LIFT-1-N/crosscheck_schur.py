#!/usr/bin/env python3
"""Exact verifier for C-J-SINGER-MAHLER-LIFT-1-N.

Standard-library only.  There is no floating-point arithmetic here.

For f(X)=X^4+aX^3+bX^2+cX+1, the eigenvalues of the second
exterior power of a companion matrix are the six pair-products of
the roots of f.  If f has exactly two roots outside the unit circle,
its Mahler measure is the spectral radius of that exterior power.

We compare that radius with tau=phi^2 in Z[tau], tau^2=3*tau-1,
using the strict Schur transform.  Equality is checked by removing a
factor Z-1 or Z+1 after scaling the compound polynomial by tau.
"""

from itertools import combinations


class K(tuple):
    """u+v*tau in Z[tau], where tau^2=3*tau-1."""

    __slots__ = ()

    def __new__(cls, u=0, v=0):
        return tuple.__new__(cls, (int(u), int(v)))

    def __add__(self, other):
        other = other if isinstance(other, K) else K(other)
        return K(self[0] + other[0], self[1] + other[1])

    __radd__ = __add__

    def __neg__(self):
        return K(-self[0], -self[1])

    def __sub__(self, other):
        return self + (-(other if isinstance(other, K) else K(other)))

    def __mul__(self, other):
        other = other if isinstance(other, K) else K(other)
        u, v = self
        x, y = other
        return K(u * x - v * y, u * y + v * x + 3 * v * y)

    __rmul__ = __mul__


ZERO = K()
ONE = K(1)
TAU = K(0, 1)


def sign_k(value):
    """Exact sign in the real embedding tau=(3+sqrt(5))/2."""

    # 2*(u+v*tau) = A+B*sqrt(5).
    a = 2 * value[0] + 3 * value[1]
    b = value[1]
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0:
        if b >= 0:
            return 1
        return 1 if a * a > 5 * b * b else -1
    if b <= 0:
        return -1
    return 1 if 5 * b * b > a * a else -1


def matmul(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def charpoly_ascending(matrix):
    """det(ZI-A), ascending coefficients, by Newton identities."""

    n = len(matrix)
    power = [row[:] for row in matrix]
    traces = [0]
    descending = [1]
    for k in range(1, n + 1):
        traces.append(sum(power[i][i] for i in range(n)))
        numerator = traces[k] + sum(
            descending[i] * traces[k - i] for i in range(1, k)
        )
        assert numerator % k == 0
        descending.append(-numerator // k)
        if k < n:
            power = matmul(power, matrix)
    return list(reversed(descending))


PAIRS = tuple(combinations(range(4), 2))


def compound_polynomial(a, b, c):
    """Characteristic polynomial of exterior_square(C_f)."""

    companion = [
        [0, 0, 0, -1],
        [1, 0, 0, -c],
        [0, 1, 0, -b],
        [0, 0, 1, -a],
    ]
    compound = [
        [
            companion[k][i] * companion[l][j]
            - companion[k][j] * companion[l][i]
            for i, j in PAIRS
        ]
        for k, l in PAIRS
    ]
    return charpoly_ascending(compound)


def scale_by_tau(polynomial):
    """Return P(tau*Z), with coefficients in ascending order."""

    power = ONE
    scaled = []
    for coefficient in polynomial:
        scaled.append(coefficient * power)
        power = power * TAU
    return scaled


def evaluate(polynomial, point):
    value = ZERO
    for coefficient in reversed(polynomial):
        value = value * point + coefficient
    return value


def schur_strict(polynomial):
    """True exactly when every zero lies in |Z|<1."""

    current = list(polynomial)
    while len(current) > 1:
        constant = current[0]
        leading = current[-1]
        if sign_k(leading * leading - constant * constant) <= 0:
            return False
        degree = len(current) - 1
        current = [
            leading * current[k] - constant * current[degree - k]
            for k in range(1, degree + 1)
        ]
    return sign_k(current[0]) != 0


def divide_linear(polynomial, root):
    """Exact division by Z-root; ascending coefficients."""

    degree = len(polynomial) - 1
    quotient = [ZERO for _ in range(degree)]
    quotient[-1] = polynomial[-1]
    for k in range(degree - 1, 0, -1):
        quotient[k - 1] = polynomial[k] + root * quotient[k]
    assert polynomial[0] + root * quotient[0] == ZERO
    return quotient


def radius_lt_tau(a, b, c):
    return schur_strict(scale_by_tau(compound_polynomial(a, b, c)))


def radius_eq_tau(a, b, c):
    """Exact test for compound spectral radius equal to tau.

    For an admissible 2-out/2-in quartic the unique maximal compound
    root is the product of the two outside roots, hence is real.  Thus
    after scaling it is +1 or -1.  Removing all such linear factors and
    applying strict Schur certifies that every remaining root is smaller.
    """

    current = scale_by_tau(compound_polynomial(a, b, c))
    removed = 0
    for root in (ONE, -ONE):
        while evaluate(current, root) == ZERO:
            current = divide_linear(current, root)
            removed += 1
    return removed > 0 and schur_strict(current)


def parity_class(a, b, c):
    parity = (a & 1, b & 1, c & 1)
    if parity == (0, 0, 1):
        return "p_L"
    if parity == (1, 0, 0):
        return "p_R"
    return None


def f_at_one(a, b, c):
    return 2 + a + b + c


def f_at_minus_one(a, b, c):
    return 2 - a + b - c


def outside_count(a, b, c):
    """Exact Routh count after s=(z-1)/(z+1).

    In the frozen parity classes a-c is odd, so it is nonzero.  For all
    candidates reaching this routine the displayed Routh first column is
    nondegenerate.  Its sign changes count |z|>1 roots.
    """

    e = f_at_one(a, b, c)
    aa = f_at_minus_one(a, b, c)
    d = 2 * (a - c)
    cc = 12 - 2 * b
    ff = aa + cc
    first_column_sign_equivalents = [
        aa,
        -d,
        ff,
        d * (ff + e) * ff,
        e,
    ]
    assert all(first_column_sign_equivalents)
    signs = [value > 0 for value in first_column_sign_equivalents]
    return sum(signs[k] != signs[k - 1] for k in range(1, len(signs)))


def admissible(a, b, c):
    if parity_class(a, b, c) is None:
        return False
    # On |z|=1, Im(f(z)/z^2)=(a-c)sin(theta).  Opposite parity makes
    # a!=c, so only z=+/-1 need checking.
    if f_at_one(a, b, c) == 0 or f_at_minus_one(a, b, c) == 0:
        return False
    return outside_count(a, b, c) == 2


def in_class(level, triple):
    a, b, c = triple
    side = parity_class(a, b, c)
    if level == 0:
        return side is not None
    if side != "p_R":
        return False
    if level == 1:
        return True
    if a != -3:
        return False
    if level == 2:
        return True
    return f_at_one(a, b, c) == 1


def main():
    window = [
        (a, b, c)
        for a in range(-10, 11)
        for b in range(-15, 16)
        for c in range(-10, 11)
        if parity_class(a, b, c) is not None
    ]
    assert len(window) == 3300

    lower_radius = [triple for triple in window if radius_lt_tau(*triple)]
    equal_radius = [triple for triple in window if radius_eq_tau(*triple)]

    expected_a2_lower_candidates = [
        (-3, -2, 0),
        (-3, 0, 0),
        (-3, 2, -2),
        (-3, 4, -4),
    ]
    observed_a2_lower_candidates = [
        triple for triple in lower_radius if in_class(2, triple)
    ]
    assert observed_a2_lower_candidates == expected_a2_lower_candidates
    observed_counts = [outside_count(*triple) for triple in observed_a2_lower_candidates]
    assert observed_counts == [1, 1, 1, 3]
    assert [triple for triple in equal_radius if in_class(2, triple)] == [
        (-3, 4, -2)
    ]

    f_j = (-3, 4, -2)
    assert admissible(*f_j)
    assert f_at_one(*f_j) == 1

    witness = (-1, 0, 0)
    assert admissible(*witness)
    assert in_class(1, witness)
    assert radius_lt_tau(*witness)

    for level in range(4):
        strict_admissible = [
            triple
            for triple in lower_radius
            if in_class(level, triple) and admissible(*triple)
        ]
        equal_admissible = [
            triple
            for triple in equal_radius
            if in_class(level, triple) and admissible(*triple)
        ]
        print(
            f"A{level}: lower={strict_admissible}; equal={equal_admissible}"
        )

    print("A0=FALSE (F-LOWER and F-TIE)")
    print("A1=FALSE (F-LOWER and F-TIE)")
    print("A2=TRUE (unique equality f_J)")
    print("A3=TRUE (unique equality f_J)")


if __name__ == "__main__":
    main()
