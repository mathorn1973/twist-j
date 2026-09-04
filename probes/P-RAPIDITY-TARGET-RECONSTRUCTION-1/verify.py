#!/usr/bin/env python3
"""Exact finite audit for P-RAPIDITY-TARGET-RECONSTRUCTION-1.

All scientific arithmetic uses integers, Fraction, or the exact real field
Q(sqrt(5)).  The fixed audit range is m = 1,...,16.  This program reads no
files, accepts no data input, and performs no writes or external operations.
The finite audit does not establish any unbounded claim by computation.
"""

from fractions import Fraction


class Q5:
    """The exact real number a + b*sqrt(5), with rational a and b."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        if not isinstance(a, (int, Fraction)) or not isinstance(b, (int, Fraction)):
            raise TypeError("Q5 coefficients must be exact rationals")
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def coerce(value):
        if isinstance(value, Q5):
            return value
        if isinstance(value, (int, Fraction)):
            return Q5(value)
        raise TypeError("Q5 arithmetic requires exact operands")

    def __add__(self, other):
        other = self.coerce(other)
        return Q5(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Q5(
            self.a * other.a + 5 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        norm = other.a * other.a - 5 * other.b * other.b
        if norm == 0:
            raise ZeroDivisionError("zero Q5 divisor")
        return self * Q5(other.a / norm, -other.b / norm)

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("Q5 exponent must be an integer")
        if exponent < 0:
            return (Q5(1) / self) ** (-exponent)
        result = Q5(1)
        factor = self
        while exponent:
            if exponent % 2:
                result = result * factor
            factor = factor * factor
            exponent //= 2
        return result

    def sign(self):
        """Exact ordering: only rational signs and squared comparisons."""
        if self.b == 0:
            return (self.a > 0) - (self.a < 0)
        if self.a == 0:
            return (self.b > 0) - (self.b < 0)
        if self.a > 0 and self.b > 0:
            return 1
        if self.a < 0 and self.b < 0:
            return -1
        delta = self.a * self.a - 5 * self.b * self.b
        comparison = (delta > 0) - (delta < 0)
        return comparison if self.a > 0 else -comparison

    def __abs__(self):
        return -self if self.sign() < 0 else self

    def __eq__(self, other):
        if not isinstance(other, (Q5, int, Fraction)):
            return False
        other = self.coerce(other)
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return (self - other).sign() < 0

    def __le__(self, other):
        return (self - other).sign() <= 0

    def __gt__(self, other):
        return (self - other).sign() > 0

    def __ge__(self, other):
        return (self - other).sign() >= 0


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def rational_sign(value):
    return (value > 0) - (value < 0)


def admissible_nodes(nodes, target):
    if not nodes:
        raise ValueError("empty node set")
    if not isinstance(target, (int, Fraction)):
        raise TypeError("target must be exact")
    if any(not isinstance(node, (int, Fraction)) for node in nodes):
        raise TypeError("nodes must be exact")
    if len(set(nodes)) != len(nodes):
        raise ValueError("repeated node")
    if target in nodes:
        raise ValueError("target is an interpolation node")


def lucas_nodes(m):
    if not isinstance(m, int) or m < 1:
        raise ValueError("m must be a positive integer")
    lucas = [2, 1]
    for _ in range(2, 2 * m + 1):
        lucas.append(lucas[-1] + lucas[-2])
    return tuple(1 - lucas[2 * k] for k in range(1, m + 1))


def lagrange_weights(nodes, target):
    """Direct rational product; no Q5 or q-product formula is used."""
    admissible_nodes(nodes, target)
    weights = []
    for k, node in enumerate(nodes):
        weight = Fraction(1)
        for ell, other in enumerate(nodes):
            if ell != k:
                weight *= Fraction(target - other, node - other)
        weights.append(weight)
    return tuple(weights)


def q_weights(m, q):
    """Independent exact field formula via P_r = product(1-q**j)."""
    products = [Q5(1)]
    for j in range(1, 2 * m + 1):
        products.append(products[-1] * (1 - q ** j))
    return tuple(
        ((-1) ** (k - 1))
        * q ** (k * (k - 1) // 2)
        * (1 + q ** k)
        * products[m] ** 2
        / (products[m - k] * products[m + k])
        for k in range(1, m + 1)
    )


def linear_system_weights(nodes, target):
    """Independent dense rational solve of the monomial equations."""
    admissible_nodes(nodes, target)
    m = len(nodes)
    matrix = [
        [Fraction(node) ** j for node in nodes] + [Fraction(target) ** j]
        for j in range(m)
    ]
    for column in range(m):
        pivot = next(
            (row for row in range(column, m) if matrix[row][column] != 0),
            None,
        )
        if pivot is None:
            raise ValueError("singular interpolation system")
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [entry / divisor for entry in matrix[column]]
        for row in range(m):
            if row != column:
                factor = matrix[row][column]
                matrix[row] = [
                    matrix[row][j] - factor * matrix[column][j]
                    for j in range(m + 1)
                ]
    return tuple(matrix[row][-1] for row in range(m))


def weighted_sum(weights, values):
    if len(weights) != len(values):
        raise ValueError("weight/value length mismatch")
    return sum((weight * value for weight, value in zip(weights, values)), Fraction(0))


def reconstructs_monomial(nodes, weights, target, degree):
    return weighted_sum(weights, tuple(node ** degree for node in nodes)) == target ** degree


def absolute_amplification(weights):
    return sum((abs(weight) for weight in weights), Fraction(0))


def relative_amplification(nodes, weights, degree):
    return weighted_sum(
        tuple(abs(weight) for weight in weights),
        tuple(abs(node) ** degree for node in nodes),
    )


def envelope(k, q):
    return q ** (k * (k - 1) // 2) * (1 + q ** k)


def tail_bound(k, q):
    return q ** (k * (k + 1) // 2) * (
        1 + 2 * q ** (k + 1) / (1 - q ** (k + 2))
    )


def gate_1(context):
    rows = {}
    for m in range(1, 17):
        nodes = lucas_nodes(m)
        admissible_nodes(nodes, -1)
        require(all(node < -1 for node in nodes), "node target separation")
        require(all(nodes[k] > nodes[k + 1] for k in range(m - 1)), "node order")
        rows[m] = (nodes, lagrange_weights(nodes, -1))
    require(rows[1] == ((-2,), (Fraction(1),)), "m=1 reference")
    require(rows[2][0] == (-2, -6), "m=2 node reference")
    require(rows[3][0] == (-2, -6, -17), "m=3 node reference")
    require(rows[2][1] == (Fraction(5, 4), Fraction(-1, 4)), "m=2 weights")
    require(rows[3][1] == (Fraction(4, 3), Fraction(-4, 11), Fraction(1, 33)), "m=3 weights")
    context["rows"] = rows


def gate_2(context):
    q = Q5(Fraction(3, 2), Fraction(-1, 2))
    require(0 < q < 1, "q interval")
    require(q * q - 3 * q + 1 == 0, "q polynomial")
    for m, (_, weights) in context["rows"].items():
        field_weights = q_weights(m, q)
        for rational, algebraic in zip(weights, field_weights):
            require(algebraic.b == 0 and algebraic.a == rational, "independent q formula")
    context["q"] = q


def gate_3(context):
    for m, (nodes, weights) in context["rows"].items():
        for degree in range(m):
            require(reconstructs_monomial(nodes, weights, -1, degree), "monomial identity")
        if m <= 6:
            require(linear_system_weights(nodes, -1) == weights, "independent dense solve")


def gate_4(context):
    q = context["q"]
    for m, (_, weights) in context["rows"].items():
        require(sum(weights, Fraction(0)) == 1, "partition of unity")
        for k, weight in enumerate(weights, 1):
            require(rational_sign(weight) == (-1) ** (k - 1), "alternating signs")
            require(Q5(abs(weight)) < envelope(k, q), "individual strict envelope")
            for j in range(k):
                factor = (1 - q ** (m - j)) / (1 - q ** (m + j + 1))
                require(0 < factor < 1, "positive product factor below one")


def gate_5(context):
    previous = None
    for m, (_, weights) in context["rows"].items():
        value = absolute_amplification(weights)
        require(value < Fraction(19, 10), "absolute amplification upper bound")
        if previous is not None:
            require(previous < value, "strict increase in m")
        previous = value
        if m == 2:
            require(value == Fraction(3, 2), "Lambda_2 reference")
        if m == 3:
            require(value == Fraction(19, 11), "Lambda_3 reference")


def gate_6(context):
    q = context["q"]
    require(tail_bound(1, q) == Fraction(1, 2), "K=1 exact tail bound")
    for m, (_, weights) in context["rows"].items():
        for k in range(m + 1):
            tail = absolute_amplification(weights[k:])
            require(Q5(tail) < tail_bound(k, q), "strict finite tail bound")
        require(absolute_amplification(weights[1:]) < Fraction(1, 2), "tail beyond first node")


def gate_7(context):
    q = context["q"]
    for m, (nodes, weights) in context["rows"].items():
        degree = m - 1
        if degree == 0:
            continue
        s = degree * (degree + 1) // 2
        kappa = relative_amplification(nodes, weights, degree)
        require(q ** (2 - s) < Q5(kappa), "relative amplification lower bound")
        require(Q5(kappa) < 6 * q ** (-s), "relative amplification upper bound")
        if m == 2:
            require(kappa == 4, "kappa_1 reference")
        if m == 3:
            require(kappa == Fraction(299, 11), "kappa_2 reference")


def gate_8(context):
    epsilon = Fraction(1, 7)
    for m, (nodes, weights) in context["rows"].items():
        degree = m - 1
        samples = tuple(node ** degree for node in nodes)
        target_value = (-1) ** degree
        lam = absolute_amplification(weights)
        kappa = relative_amplification(nodes, weights, degree)
        for orientation in (-1, 1):
            absolute_errors = tuple(orientation * epsilon * rational_sign(weight) for weight in weights)
            require(all(abs(error) == epsilon for error in absolute_errors), "absolute error budget")
            perturbed = tuple(value + error for value, error in zip(samples, absolute_errors))
            require(
                weighted_sum(weights, perturbed) - target_value == orientation * epsilon * lam,
                "exact absolute extremizer",
            )
            relative_factors = tuple(
                orientation * epsilon * rational_sign(weight) * rational_sign(value)
                for weight, value in zip(weights, samples)
            )
            require(all(abs(factor) == epsilon for factor in relative_factors), "relative error budget")
            perturbed = tuple(value * (1 + factor) for value, factor in zip(samples, relative_factors))
            require(
                weighted_sum(weights, perturbed) - target_value == orientation * epsilon * kappa,
                "exact relative extremizer",
            )


def expect_value_error(action):
    try:
        action()
    except ValueError:
        return True
    return False


def breaker_1(context):
    nodes, _ = context["rows"][2]
    wrong_weights = lagrange_weights(nodes, 0)
    require(reconstructs_monomial(nodes, wrong_weights, 0, 1), "wrong-target control")
    require(not reconstructs_monomial(nodes, wrong_weights, -1, 1), "wrong target must be detected")


def breaker_2(context):
    nodes, weights = context["rows"][2]
    altered_weights = tuple(abs(weight) for weight in weights)
    require(not reconstructs_monomial(nodes, altered_weights, -1, 0), "lost signs must be detected")


def breaker_3(context):
    require(expect_value_error(lambda: lagrange_weights((-2, -2), -1)), "repeated node must be rejected")


def breaker_4(context):
    require(expect_value_error(lambda: admissible_nodes((-1, -2), -1)), "target node must be rejected")


def breaker_5(context):
    nodes, weights = context["rows"][2]
    kappa = relative_amplification(nodes, weights, 1)
    require(kappa == 4 and kappa > Fraction(19, 10), "false relative cap must be refuted")


def main():
    context = {}
    gates = (
        ("G1", "nodes and rational reference weights", gate_1),
        ("G2", "independent exact Qsqrt5 q-product formula", gate_2),
        ("G3", "all monomials and independent dense rational solve", gate_3),
        ("G4", "alternating signs, sum one, individual envelopes", gate_4),
        ("G5", "absolute amplification increasing and below 19/10", gate_5),
        ("G6", "all finite tail bounds and tail beyond one below 1/2", gate_6),
        ("G7", "relative monomial bounds and exact reference values", gate_7),
        ("G8", "exact absolute and relative error extremizers", gate_8),
    )
    breakers = (
        ("B1", "wrong target zero rejected by monomial reconstruction", breaker_1),
        ("B2", "absolute-valued weights rejected by constant reconstruction", breaker_2),
        ("B3", "repeated node rejected", breaker_3),
        ("B4", "target included as node rejected", breaker_4),
        ("B5", "relative cap 19/10 refuted by kappa_1=4", breaker_5),
    )
    print("P-RAPIDITY-TARGET-RECONSTRUCTION-1 EXACT AUDIT m=1..16")
    for label, description, action in gates:
        try:
            action(context)
        except Exception as error:
            print(label + " FAIL: " + type(error).__name__ + ": " + str(error))
            print("VERIFY RESULT FAIL")
            return 1
        print(label + " PASS: " + description)
    print("BREAKER BLOCK")
    for label, description, action in breakers:
        try:
            action(context)
        except Exception as error:
            print(label + " FAIL: " + type(error).__name__ + ": " + str(error))
            print("BREAKER RESULT FAIL")
            return 1
        print(label + " PASS: " + description)
    print("BREAKER RESULT 5/5 ALL PASS")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
