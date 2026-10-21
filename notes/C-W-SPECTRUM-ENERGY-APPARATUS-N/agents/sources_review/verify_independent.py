#!/usr/bin/env python3
"""Independent exact input audit. Newton identities, no root code imported.

Authored after PREREG and certificate schema were frozen. This source is
not to be executed until its SHA256 and the root source are both frozen.
No numerical spectrum, numerical phase grid, or finite-volume walk occurs.
"""

from fractions import Fraction as Q
import json
from pathlib import Path
import sys


def coefficient_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def coefficient_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def polynomial_constant(real=0, imag=0):
    value = (Q(real), Q(imag))
    return {(0, 0): value} if value != (0, 0) else {}


def polynomial_add(a, b):
    result = dict(a)
    for exponent, value in b.items():
        value = coefficient_add(result.get(exponent, (Q(0), Q(0))), value)
        if value == (0, 0):
            result.pop(exponent, None)
        else:
            result[exponent] = value
    return result


def polynomial_scale(a, scalar):
    scalar = Q(scalar)
    if not scalar:
        return {}
    return {e: (v[0] * scalar, v[1] * scalar) for e, v in a.items()}


def polynomial_mul(a, b):
    result = {}
    for (az, aw), av in a.items():
        for (bz, bw), bv in b.items():
            exponent = (az + bz, aw + bw)
            value = coefficient_add(result.get(exponent, (Q(0), Q(0))),
                                    coefficient_mul(av, bv))
            if value == (0, 0):
                result.pop(exponent, None)
            else:
                result[exponent] = value
    return result


def polynomial_conjugate(a):
    return {(-z, -w): (value[0], -value[1])
            for (z, w), value in a.items()}


def polynomial_shift(a, z, w):
    return {(az + z, aw + w): value for (az, aw), value in a.items()}


def polynomial_sum(polynomials):
    result = {}
    for p in polynomials:
        result = polynomial_add(result, p)
    return result


def matrix_identity(n):
    return [[polynomial_constant(int(i == j)) for j in range(n)]
            for i in range(n)]


def matrix_mul(a, b):
    return [[polynomial_sum(polynomial_mul(a[i][k], b[k][j])
                            for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def matrix_adjoint(a):
    return [[polynomial_conjugate(a[j][i]) for j in range(len(a))]
            for i in range(len(a[0]))]


def matrix_trace(a):
    return polynomial_sum(a[i][i] for i in range(len(a)))


def matrix_vector(a, vector):
    return [polynomial_sum(polynomial_mul(a[i][j], vector[j])
                           for j in range(len(vector)))
            for i in range(len(a))]


def characteristic_by_newton(a):
    """Return [1,c1,...,cn] using traces and Newton's identities."""
    n = len(a)
    traces = [None]
    power = matrix_identity(n)
    for j in range(1, n + 1):
        power = matrix_mul(power, a)
        traces.append(matrix_trace(power))
    coefficients = [polynomial_constant(1)]
    for k in range(1, n + 1):
        numerator = polynomial_sum(
            polynomial_mul(coefficients[k - j], traces[j])
            for j in range(1, k + 1))
        coefficients.append(polynomial_scale(numerator, Q(-1, k)))
    return coefficients


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def main(output_path):
    # Tensor product is formed from the specified 2 by 2 factor.
    factor = [[polynomial_constant(1), polynomial_constant(0, 2)],
              [polynomial_constant(0, 2), polynomial_constant(1)]]
    coin = [[polynomial_scale(
                polynomial_mul(factor[i // 2][j // 2],
                               factor[i % 2][j % 2]), Q(1, 5))
             for j in range(4)] for i in range(4)]
    identity = matrix_identity(4)
    require(matrix_mul(matrix_adjoint(coin), coin) == identity,
            "whole coin adjoint product is not identity")
    coin_characteristic = characteristic_by_newton(coin)
    require(coin_characteristic[-1] == polynomial_constant(1),
            "coin determinant is not one")

    shifts = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    free = [[polynomial_shift(coin[i][j], *shifts[i])
             for j in range(4)] for i in range(4)]
    require(matrix_mul(matrix_adjoint(free), free) == identity,
            "whole Laurent symbol is not unitary")
    actual = characteristic_by_newton(free)

    trace_expected = {(1, 0): (Q(1, 5), Q(0)),
                      (-1, 0): (Q(1, 5), Q(0)),
                      (0, 1): (Q(1, 5), Q(0)),
                      (0, -1): (Q(1, 5), Q(0))}
    middle_expected = {(1, 1): (Q(1, 5), Q(0)),
                       (1, -1): (Q(1, 5), Q(0)),
                       (-1, 1): (Q(1, 5), Q(0)),
                       (-1, -1): (Q(1, 5), Q(0)),
                       (0, 0): (Q(-6, 5), Q(0))}
    expected = [polynomial_constant(1),
                polynomial_scale(trace_expected, -1),
                middle_expected,
                polynomial_scale(trace_expected, -1),
                polynomial_constant(1)]
    require(actual == expected, "entire free characteristic polynomial mismatch")

    antisymmetric = [polynomial_constant(x) for x in (1, 0, 0, -1)]
    symmetric = [polynomial_constant(x) for x in (1, 0, 0, 1)]
    require(matrix_vector(coin, antisymmetric) == antisymmetric,
            "compact antisymmetric coin vector not fixed")
    coin_symmetric = matrix_vector(coin, symmetric)
    expectation = polynomial_scale(
        polynomial_sum(polynomial_mul(polynomial_conjugate(symmetric[j]),
                                      coin_symmetric[j])
                       for j in range(4)), Q(1, 2))
    require(expectation == polynomial_constant(Q(-3, 5)),
            "symmetric-vector coin expectation mismatch")

    half_angle = Q(1, 2)
    cos_b = (1 - half_angle ** 2) / (1 + half_angle ** 2)
    sin_b = 2 * half_angle / (1 + half_angle ** 2)
    cos_delta = sin_b ** 2 - cos_b ** 2
    threshold = 1 + 4 * cos_delta
    margin = Q(5) - threshold ** 2
    require((cos_b, sin_b, cos_delta) == (Q(3, 5), Q(4, 5), Q(7, 25)),
            "half-angle gap coefficients mismatch")
    require(threshold == Q(53, 25) and margin == Q(316, 625) and margin > 0,
            "strict global-gap sign certificate failed")

    # Q(sqrt(5)) represented here by its rational and sqrt(5) parts.
    cos_pi_over_five = (Q(1, 4), Q(1, 4))
    beta = tuple(Q(3, 20) * coefficient for coefficient in cos_pi_over_five)
    require(beta == (Q(3, 80), Q(3, 80)),
            "algebraic beta-lower conversion failed")

    characteristic_rows = []
    for k, coefficient_polynomial in enumerate(actual):
        for (z_power, w_power), (real, imag) in coefficient_polynomial.items():
            characteristic_rows.append([4 - k, z_power, w_power,
                                        str(real), str(imag)])
    characteristic_rows.sort(key=lambda row: tuple(row[:3]))

    certificate = {
        "schema": "w-spectrum-exact-v1",
        "coin_unitary": True,
        "coin_determinant": "1",
        "free_symbol_unitary": True,
        "compact_rest_eigenvector": True,
        "s_coin_expectation": "-3/5",
        "characteristic": characteristic_rows,
        "gap": {
            "cos_b": str(cos_b),
            "sin_b": str(sin_b),
            "cos_delta": str(cos_delta),
            "sqrt5_threshold": str(threshold),
            "squared_margin": str(margin),
            "strictly_positive": True,
        },
        "beta_lower": {
            "rational_part": str(beta[0]),
            "sqrt5_part": str(beta[1]),
        },
    }
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(certificate, sort_keys=True,
                                      separators=(",", ":")) + "\n",
                           encoding="utf-8")
    print("PASS independent exact Newton-identity audit; certificate written")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_independent.py OUTPUT_CERTIFICATE.json")
    main(sys.argv[1])
