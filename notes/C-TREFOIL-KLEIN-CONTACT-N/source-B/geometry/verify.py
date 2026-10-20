#!/usr/bin/env python3
"""Exact author verifier for frozen geometry targets F0--F6.

NON-CANONICAL auxiliary verification. The accepted group H has order 120;
this program checks the prescribed word certificates, not a group search.
No floating point, external packages, network access, or input files are used.
The program emits deterministic JSON. Execution is reserved for the root
after all three implementations have been pinned in IMPLEMENTATIONS.json.
"""

import json
import sys


PREREG_SHA256 = "5061341dd53c3814ef87293b4a5d361600b123f53ac1892bd25005bb46b5640f"


class Cyclotomic:
    """An element of Z[j], represented in the basis 1,j,j^2,j^3."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0):
        if isinstance(value, Cyclotomic):
            coefficients = value.coefficients
        elif isinstance(value, int):
            coefficients = (value, 0, 0, 0)
        else:
            coefficients = tuple(value)
            if len(coefficients) != 4 or any(type(x) is not int for x in coefficients):
                raise TypeError("Expected four integer cyclotomic coefficients")
        self.coefficients = coefficients

    def __add__(self, other):
        other = Cyclotomic(other)
        return Cyclotomic(tuple(x + y for x, y in zip(self.coefficients, other.coefficients)))

    __radd__ = __add__

    def __neg__(self):
        return Cyclotomic(tuple(-x for x in self.coefficients))

    def __sub__(self, other):
        return self + (-Cyclotomic(other))

    def __rsub__(self, other):
        return Cyclotomic(other) + (-self)

    def __mul__(self, other):
        other = Cyclotomic(other)
        product = [0] * 7
        for r, x in enumerate(self.coefficients):
            for t, y in enumerate(other.coefficients):
                product[r + t] += x * y
        # j^4 = -(1+j+j^2+j^3), applied from the highest degree downward.
        for degree in range(6, 3, -1):
            coefficient = product[degree]
            for shift in range(4):
                product[degree - 4 + shift] -= coefficient
            product[degree] = 0
        return Cyclotomic(tuple(product[:4]))

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if type(exponent) is not int or exponent < 0:
            raise ValueError("Only nonnegative integer powers are required")
        result = Cyclotomic(1)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def __eq__(self, other):
        if isinstance(other, int):
            other = Cyclotomic(other)
        if not isinstance(other, Cyclotomic):
            return False
        return self.coefficients == other.coefficients

    def __bool__(self):
        return any(self.coefficients)

    def __repr__(self):
        return "Cyclotomic" + repr(self.coefficients)


ZERO = Cyclotomic(0)
ONE = Cyclotomic(1)
J = Cyclotomic((0, 1, 0, 0))


def matrix(a, b, c, d):
    """Row-major 2 by 2 matrix, acting on a column from the left."""
    return tuple(Cyclotomic(x) for x in (a, b, c, d))


IDENTITY = matrix(1, 0, 0, 1)


def matrix_multiply(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def matrix_power(value, exponent):
    if type(exponent) is not int or exponent < 0:
        raise ValueError("Only nonnegative matrix powers are required")
    result = IDENTITY
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, value)
        value = matrix_multiply(value, value)
        exponent //= 2
    return result


def matrix_scale(value, scalar):
    return tuple(Cyclotomic(scalar) * entry for entry in value)


def matrix_add(left, right):
    return tuple(x + y for x, y in zip(left, right))


def matrix_subtract(left, right):
    return tuple(x - y for x, y in zip(left, right))


def matrix_trace(value):
    return value[0] + value[3]


def matrix_determinant(value):
    return value[0] * value[3] - value[1] * value[2]


def characteristic_polynomial(value):
    # Descending coefficients of X^2 - tr(value) X + det(value).
    return (ONE, -matrix_trace(value), matrix_determinant(value))


def sigma3(value):
    return sum((coefficient * J ** (3 * degree)
                for degree, coefficient in enumerate(value.coefficients)), ZERO)


def matrix_sigma3(value):
    return tuple(sigma3(entry) for entry in value)


def polynomial_add(left, right):
    result = dict(left)
    for exponents, coefficient in right.items():
        new_value = result.get(exponents, ZERO) + coefficient
        if new_value:
            result[exponents] = new_value
        elif exponents in result:
            del result[exponents]
    return result


def polynomial_scale(value, scalar):
    scalar = Cyclotomic(scalar)
    if not scalar:
        return {}
    return {powers: scalar * coefficient for powers, coefficient in value.items()
            if scalar * coefficient}


def polynomial_multiply(left, right):
    result = {}
    for (u1, v1), coefficient1 in left.items():
        for (u2, v2), coefficient2 in right.items():
            powers = (u1 + u2, v1 + v2)
            new_value = result.get(powers, ZERO) + coefficient1 * coefficient2
            if new_value:
                result[powers] = new_value
            elif powers in result:
                del result[powers]
    return result


def polynomial_power(value, exponent):
    result = {(0, 0): ONE}
    while exponent:
        if exponent & 1:
            result = polynomial_multiply(result, value)
        value = polynomial_multiply(value, value)
        exponent //= 2
    return result


def linear_polynomial(u_coefficient, v_coefficient):
    result = {}
    u_coefficient = Cyclotomic(u_coefficient)
    v_coefficient = Cyclotomic(v_coefficient)
    if u_coefficient:
        result[(1, 0)] = u_coefficient
    if v_coefficient:
        result[(0, 1)] = v_coefficient
    return result


def klein_f_of(x, y):
    # f0(x,y) = x*y*(x^10 + 11*x^5*y^5 - y^10).
    middle = polynomial_add(
        polynomial_power(x, 10),
        polynomial_scale(polynomial_multiply(polynomial_power(x, 5), polynomial_power(y, 5)), 11),
    )
    middle = polynomial_add(middle, polynomial_scale(polynomial_power(y, 10), -1))
    return polynomial_multiply(polynomial_multiply(x, y), middle)


def polynomial_substitute(value, transformation):
    x = linear_polynomial(transformation[0], transformation[1])
    y = linear_polynomial(transformation[2], transformation[3])
    maximum_u = max((powers[0] for powers in value), default=0)
    maximum_v = max((powers[1] for powers in value), default=0)
    xpowers = [{(0, 0): ONE}]
    ypowers = [{(0, 0): ONE}]
    for _ in range(maximum_u):
        xpowers.append(polynomial_multiply(xpowers[-1], x))
    for _ in range(maximum_v):
        ypowers.append(polynomial_multiply(ypowers[-1], y))
    result = {}
    for (u_degree, v_degree), coefficient in value.items():
        term = polynomial_multiply(xpowers[u_degree], ypowers[v_degree])
        result = polynomial_add(result, polynomial_scale(term, coefficient))
    return result


def residue(value):
    # O/(1-j) -> F5, not an identification O/(5) = F5.
    return sum(value.coefficients) % 5


def matrix_residue(value):
    return tuple(residue(entry) for entry in value)


def mod_matrix_multiply(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return ((a * e + b * g) % 5, (a * f + b * h) % 5,
            (c * e + d * g) % 5, (c * f + d * h) % 5)


def mod_matrix_power(value, exponent):
    result = (1, 0, 0, 1)
    while exponent:
        if exponent & 1:
            result = mod_matrix_multiply(result, value)
        value = mod_matrix_multiply(value, value)
        exponent //= 2
    return result


def encoded(value):
    if isinstance(value, Cyclotomic):
        return list(value.coefficients)
    if isinstance(value, dict):
        return [
            {"powers": list(powers), "coefficient": encoded(coefficient)}
            for powers, coefficient in sorted(value.items())
        ]
    if isinstance(value, (tuple, list)):
        return [encoded(entry) for entry in value]
    return value


class CheckFailure(Exception):
    pass


class Report:
    def __init__(self):
        self.checks = []
        self.certificates = {}

    def equal(self, check_id, actual, expected):
        result = {"id": check_id, "status": "PASS" if actual == expected else "FAIL"}
        if actual != expected:
            result["actual"] = encoded(actual)
            result["expected"] = encoded(expected)
        self.checks.append(result)
        if actual != expected:
            raise CheckFailure(check_id)

    def nonzero(self, check_id, value):
        self.equal(check_id, bool(value), True)

    def finish(self, error=None):
        groups = {}
        for check in self.checks:
            group = check["id"].split(".", 1)[0]
            if group not in groups:
                groups[group] = {"passed": 0, "failed": 0}
            groups[group]["passed" if check["status"] == "PASS" else "failed"] += 1
        passed = sum(check["status"] == "PASS" for check in self.checks)
        failed = sum(check["status"] == "FAIL" for check in self.checks)
        complete = error is None and all("F" + str(index) in groups for index in range(7))
        result = {
            "kind": "NON-CANONICAL exact geometry author verification",
            "prereg_sha256": PREREG_SHA256,
            "status": "PASS" if complete and failed == 0 else "FAIL",
            "arithmetic": "Z[j], j^4+j^3+j^2+j+1=0; coefficient equality",
            "matrix_convention": "left action on column vectors",
            "complex_embedding": "j=exp(2*pi*i/5); local positive endpoint j*z",
            "passed": passed,
            "failed": failed,
            "groups": groups,
            "checks": self.checks,
            "certificates": self.certificates,
            "group_enumeration_performed": False,
            "scope": {
                "H_order_120": "accepted earlier result; generation checked by C^3=A and D^2=B",
                "G_order_600": "proof from accepted H and scalar intersection; generation word certificates checked",
                "geometric_path_existence": "analytic proof with primary sources, not finite path enumeration",
                "native_or_physical_admission": "not tested or asserted",
            },
        }
        if error is not None:
            result["error"] = error
        return result


def verify(report):
    a = J + J ** 4
    s = J ** 2 - J ** 3
    S = matrix(0, -1, 1, 0)
    S_inverse = matrix(0, 1, -1, 0)
    A = matrix(J, 1, 0, J ** 4)
    B = matrix_multiply(matrix_multiply(S, A), S_inverse)
    C = matrix_power(A, 2)
    D = matrix_power(B, 3)
    Q = matrix(a, 0, -s, 1)
    Q_inverse = matrix(a + 1, 0, s * (a + 1), 1)
    R1 = matrix_scale(C, J ** 3)
    R2 = matrix_scale(D, J ** 3)

    report.equal("F0.a_quadratic", a ** 2 + a, ONE)
    report.equal("F0.s_square", s ** 2, a - 2)
    report.equal("F0.a_unit", a * (a + 1), ONE)
    report.equal("F0.other_real_trace", J ** 2 + J ** 3, -a - 1)
    report.equal("F0.B_explicit", B, matrix(J ** 4, 0, -1, J))

    original_obstruction = matrix_determinant(matrix_subtract(matrix_scale(A, J ** 3), IDENTITY))
    report.equal("F1.original_obstruction_value", original_obstruction, 2 + 2 * J + J ** 3)
    report.nonzero("F1.original_obstruction_nonzero", original_obstruction)
    report.equal("F1.original_trace", matrix_trace(A), a)
    report.equal("F1.corrected_trace", matrix_trace(C), -a - 1)
    report.equal("F1.traces_differ", matrix_trace(A) == matrix_trace(C), False)
    report.equal("F1.jA_characteristic", characteristic_polynomial(matrix_scale(A, J)),
                 (ONE, -(ONE + J ** 2), J ** 2))
    report.equal("F1.jA_determinant", matrix_determinant(matrix_scale(A, J)), J ** 2)

    report.equal("F2.C_explicit", C, matrix(J ** 2, a, 0, J ** 3))
    report.equal("F2.D_explicit", D, matrix(J ** 2, 0, a, J ** 3))
    CD = matrix_multiply(C, D)
    DC = matrix_multiply(D, C)
    report.equal("F2.braid", matrix_multiply(CD, C), matrix_multiply(DC, D))
    report.equal("F2.distinct", C == D, False)
    report.equal("F2.C_fifth", matrix_power(C, 5), IDENTITY)
    report.equal("F2.D_fifth", matrix_power(D, 5), IDENTITY)
    report.equal("F2.C_determinant", matrix_determinant(C), ONE)
    report.equal("F2.D_determinant", matrix_determinant(D), ONE)
    report.equal("F2.CD_trace", matrix_trace(CD), ONE)
    report.equal("F2.CD_characteristic_identity",
                 matrix_add(matrix_subtract(matrix_power(CD, 2), CD), IDENTITY),
                 matrix(0, 0, 0, 0))
    report.equal("F2.CD_center", matrix_power(CD, 3), matrix_scale(IDENTITY, -1))
    report.equal("F2.recover_A", matrix_power(C, 3), A)
    report.equal("F2.recover_B", matrix_power(D, 2), B)
    commutator_difference = matrix_subtract(CD, DC)
    report.equal("F2.commutator_difference", commutator_difference,
                 matrix(a ** 2, -a * s, -a * s, -(a ** 2)))
    report.equal("F2.irreducibility_determinant", matrix_determinant(commutator_difference), a ** 2)
    report.nonzero("F2.irreducibility_nonzero", matrix_determinant(commutator_difference))

    report.equal("F3.R1_explicit", R1, matrix(1, J ** 3 * a, 0, J))
    report.equal("F3.R2_explicit", R2, matrix(1, 0, J ** 3 * a, J))
    for name, reflection in (("R1", R1), ("R2", R2)):
        report.equal("F3." + name + "_characteristic", characteristic_polynomial(reflection),
                     (ONE, -(ONE + J), J))
        report.equal("F3." + name + "_nonidentity", reflection == IDENTITY, False)
        report.equal("F3." + name + "_fixed_line", matrix_determinant(matrix_subtract(reflection, IDENTITY)), ZERO)
        report.equal("F3." + name + "_determinant", matrix_determinant(reflection), J)
        report.equal("F3." + name + "_fifth", matrix_power(reflection, 5), IDENTITY)
    R12 = matrix_multiply(R1, R2)
    R21 = matrix_multiply(R2, R1)
    report.equal("F3.braid", matrix_multiply(R12, R1), matrix_multiply(R21, R2))
    report.equal("F3.center", matrix_power(R12, 3), matrix_scale(IDENTITY, -(J ** 3)))
    report.equal("F3.recover_scalar_j", matrix_power(R12, 6), matrix_scale(IDENTITY, J))
    report.equal("F3.recover_C", matrix_scale(R1, J ** 2), C)
    report.equal("F3.recover_D", matrix_scale(R2, J ** 2), D)

    report.equal("F4.Q_left_inverse", matrix_multiply(Q, Q_inverse), IDENTITY)
    report.equal("F4.Q_right_inverse", matrix_multiply(Q_inverse, Q), IDENTITY)
    report.equal("F4.Q_determinant", matrix_determinant(Q), a)
    report.equal("F4.Q_integral", all(type(c) is int for x in Q for c in x.coefficients), True)
    report.equal("F4.Q_inverse_integral", all(type(c) is int for x in Q_inverse for c in x.coefficients), True)
    report.equal("F4.sigma3_generator", sigma3(J), J ** 3)
    for degree in range(4):
        value = J ** degree
        transformed = value
        for _ in range(4):
            transformed = sigma3(transformed)
        report.equal("F4.sigma3_fourth_basis_" + str(degree), transformed, value)
    for name, old, expected in (("A", A, C), ("B", B, D),
                                ("jA", matrix_scale(A, J), R1),
                                ("jB", matrix_scale(B, J), R2)):
        transformed = matrix_multiply(matrix_multiply(Q, matrix_sigma3(old)), Q_inverse)
        report.equal("F4.conjugate_" + name, transformed, expected)

    f = klein_f_of(linear_polynomial(s, a), linear_polynomial(0, 1))
    report.nonzero("F5.f_nonzero", f)
    report.equal("F5.f_homogeneous_12", sorted(set(u + v for u, v in f)), [12])
    for name, transformation, weight in (("C", C, ONE), ("D", D, ONE),
                                         ("R1", R1, J), ("R2", R2, J),
                                         ("jA", matrix_scale(A, J), J ** 2)):
        report.equal("F5.f_character_" + name, polynomial_substitute(f, transformation), polynomial_scale(f, weight))
    report.equal("F5.weight_degree_20", (J ** 3) ** 20, ONE)
    report.equal("F5.weight_degree_30", (J ** 3) ** 30, ONE)
    report.equal("F5.weight_degree_12", (J ** 3) ** 12, J)

    A0 = (1, 1, 0, 1)
    B0 = (1, 0, 4, 1)
    K0 = (2, 0, 0, 1)
    K0_inverse = (3, 0, 0, 1)
    C0 = (1, 2, 0, 1)
    D0 = (1, 0, 2, 1)
    report.equal("F6.a_residue", residue(a), 2)
    report.equal("F6.s_residue", residue(s), 0)
    report.equal("F6.Q_residue", matrix_residue(Q), K0)
    report.equal("F6.Q_inverse_residue", matrix_residue(Q_inverse), K0_inverse)
    report.equal("F6.C_residue", matrix_residue(C), C0)
    report.equal("F6.R1_residue", matrix_residue(R1), C0)
    report.equal("F6.A0_square", mod_matrix_power(A0, 2), C0)
    report.equal("F6.conjugate_A0", mod_matrix_multiply(mod_matrix_multiply(K0, A0), K0_inverse), C0)
    report.equal("F6.D_residue", matrix_residue(D), D0)
    report.equal("F6.R2_residue", matrix_residue(R2), D0)
    report.equal("F6.B0_cube", mod_matrix_power(B0, 3), D0)
    report.equal("F6.conjugate_B0", mod_matrix_multiply(mod_matrix_multiply(K0, B0), K0_inverse), D0)
    report.equal("F6.braid", mod_matrix_multiply(mod_matrix_multiply(C0, D0), C0),
                 mod_matrix_multiply(mod_matrix_multiply(D0, C0), D0))
    report.equal("F6.center", mod_matrix_power(mod_matrix_multiply(C0, D0), 3), (4, 0, 0, 4))

    report.certificates = {
        "original_local_obstruction": encoded(original_obstruction),
        "C": encoded(C),
        "D": encoded(D),
        "R1": encoded(R1),
        "R2": encoded(R2),
        "Q": encoded(Q),
        "Q_inverse": encoded(Q_inverse),
        "irreducibility_determinant": encoded(matrix_determinant(commutator_difference)),
        "f_coefficients": encoded(f),
        "f_nonzero_coefficient_count": len(f),
        "reduced_C": list(C0),
        "reduced_D": list(D0),
        "reduced_Q": list(K0),
    }


def main():
    report = Report()
    error = None
    try:
        verify(report)
    except CheckFailure as exc:
        error = {"kind": "frozen_target_failed", "check": str(exc)}
    except Exception as exc:
        error = {"kind": "implementation_error", "type": type(exc).__name__, "message": str(exc)}
    output = report.finish(error)
    print(json.dumps(output, ensure_ascii=True, indent=2, sort_keys=True))
    return 0 if output["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
