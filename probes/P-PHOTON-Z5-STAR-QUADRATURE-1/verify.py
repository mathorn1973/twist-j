#!/usr/bin/env python3
"""Exact finite audit: P-PHOTON-Z5-STAR-QUADRATURE-1.

Exact finite L4 classification only; not a probability/phase verifier.
No input files, environment, network, randomness, floating point or writes.
Scientific classifications FAIL_HALF / FAIL_UNIT are successful classified
outputs (exit zero); only internal certificate failures exit nonzero.
"""

from fractions import Fraction
from math import comb
import sys


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def mul(x, y):
    coefficients = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            coefficients[i + j] += a * b
    for degree in range(6, 3, -1):
        value = coefficients[degree]
        coefficients[degree] = 0
        for shift in range(1, 5):
            coefficients[degree - shift] -= value
    return tuple(coefficients[:4])


def power(x, exponent):
    answer = ONE
    for _ in range(exponent):
        answer = mul(answer, x)
    return answer


ROOTS = tuple(power(ZETA, exponent) for exponent in range(5))


def conjugate(x):
    answer = ZERO
    for exponent, coefficient in enumerate(x):
        answer = add(answer, tuple(coefficient * a for a in ROOTS[(-exponent) % 5]))
    return answer


def norm_square(x):
    return mul(x, conjugate(x))


def real_pair(x):
    # zeta^2 + zeta^3 = -(1+sqrt(5))/2.
    require(x[1] == 0 and x[2] == x[3], "REAL_SUBFIELD")
    return (Fraction(2 * x[0] - x[2], 2), Fraction(-x[2], 2))


def pair_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def pair_sign(x):
    a, b = x
    if a == 0:
        return (b > 0) - (b < 0)
    if b == 0:
        return (a > 0) - (a < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    difference = a * a - 5 * b * b
    require(difference != 0, "IRRATIONAL_SIGN_SEPARATION")
    difference_sign = (difference > 0) - (difference < 0)
    return difference_sign if a > 0 else -difference_sign


def pair_divide(x, y):
    a, b = x
    c, d = y
    denominator = c * c - 5 * d * d
    require(denominator != 0, "NONZERO_FIELD_DENOMINATOR")
    return ((a * c - 5 * b * d) / denominator,
            (b * c - a * d) / denominator)


def pair_abs(x):
    return tuple(-value for value in x) if pair_sign(x) < 0 else x


def compare(x, y):
    return pair_sign(pair_sub(x, y))


def rational_text(value):
    return str(value.numerator) + "/" + str(value.denominator)


def pair_text(value):
    return "(" + rational_text(value[0]) + "," + rational_text(value[1]) + ")"


def count_text(counts):
    return "(" + ",".join(str(value) for value in counts) + ")"


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest


def polynomial(counts):
    coefficients = [ONE]
    for phase, multiplicity in enumerate(counts):
        for _ in range(multiplicity):
            updated = [ZERO] * (len(coefficients) + 1)
            for degree, value in enumerate(coefficients):
                updated[degree] = add(updated[degree], value)
                updated[degree + 1] = add(updated[degree + 1], mul(ROOTS[phase], value))
            coefficients = updated
    return coefficients


def evaluate(coefficients, argument):
    answer = ZERO
    for value in reversed(coefficients):
        answer = add(mul(answer, argument), value)
    return answer


def calculate(counts):
    coefficients = polynomial(counts)
    require(len(coefficients) == sum(counts) + 1, "POLYNOMIAL_DEGREE")
    c0 = ZERO
    for coefficient in coefficients:
        c0 = add(c0, norm_square(coefficient))
    padded = coefficients + [ZERO] * (7 - len(coefficients))
    c5 = add(mul(padded[5], conjugate(padded[0])),
             mul(padded[6], conjugate(padded[1])))
    signed_f = add(c5, conjugate(c5))
    denominator = add(c0, signed_f)

    # Independent discrete quadrature, not reconstructed from c0 or c5.
    quadrature_sum = ZERO
    for root in ROOTS:
        quadrature_sum = add(quadrature_sum, norm_square(evaluate(coefficients, root)))
    require(all(value % 5 == 0 for value in quadrature_sum), "QUADRATURE_DIVISIBILITY")
    quadrature = tuple(value // 5 for value in quadrature_sum)
    require(quadrature == denominator, "QUADRATURE_EQUALS_C0_PLUS_F")

    real_c0 = real_pair(c0)
    real_f = real_pair(signed_f)
    real_d = real_pair(denominator)
    require(pair_sign(real_c0) > 0, "POSITIVE_C0")
    require(pair_sign(real_d) > 0, "POSITIVE_DISCRETE_DENOMINATOR")
    require(compare(real_f, real_c0) <= 0, "GENERIC_UPPER_F")
    require(pair_sign((real_f[0] + real_c0[0], real_f[1] + real_c0[1])) >= 0,
            "GENERIC_LOWER_F")
    ratio = pair_divide(pair_abs(real_f), real_d)
    require(pair_sign(ratio) >= 0, "NONNEGATIVE_RATIO")
    return (c0, signed_f, denominator, ratio)


def shifted(counts, shift):
    answer = [0] * 5
    for phase, multiplicity in enumerate(counts):
        answer[(phase + shift) % 5] += multiplicity
    return tuple(answer)


def reflected(counts):
    return tuple(counts[(-phase) % 5] for phase in range(5))


def extremal_report(label, keys, results):
    best = None
    witnesses = []
    half = (Fraction(1, 2), Fraction(0))
    unit = (Fraction(1), Fraction(0))
    violating_half = []
    violating_unit = []
    for counts in sorted(keys):
        ratio = results[counts][3]
        relation = 1 if best is None else compare(ratio, best)
        if relation > 0:
            best = ratio
            witnesses = [counts]
        elif relation == 0:
            witnesses.append(counts)
        if compare(ratio, half) > 0:
            violating_half.append(counts)
        if compare(ratio, unit) >= 0:
            violating_unit.append(counts)
    require(best is not None and witnesses, "NONEMPTY_EXTREMAL_CLASS")
    lines = [label + " COUNT=" + str(len(keys))
             + " MAX_RATIO=" + pair_text(best)
             + " LEX_WITNESS=" + count_text(witnesses[0])
             + " MULTIPLICITY=" + str(len(witnesses))
             + " VIOLATE_HALF=" + str(len(violating_half))
             + " VIOLATE_STRICT_UNIT=" + str(len(violating_unit))]
    for witness in witnesses:
        c0, signed_f, denominator, _ = results[witness]
        lines.append(label + " EXTREMUM=" + count_text(witness)
                     + " C0=" + pair_text(real_pair(c0))
                     + " F=" + pair_text(real_pair(signed_f))
                     + " D=" + pair_text(real_pair(denominator)))
    return lines, violating_half, violating_unit


def main():
    require(power(ZETA, 5) == ONE, "ZETA_ORDER_FIVE")
    root_sum = ZERO
    for root in ROOTS:
        root_sum = add(root_sum, root)
    require(root_sum == ZERO, "CYCLOTOMIC_SUM")
    for root in ROOTS:
        require(norm_square(root) == ONE, "ROOT_UNIT_NORM")
        require(conjugate(conjugate(root)) == root, "CONJUGATION_INVOLUTION")
    require(pair_sign((Fraction(2), Fraction(-1))) == -1, "SIGN_CONTROL_MINUS")
    require(pair_sign((Fraction(-2), Fraction(1))) == 1, "SIGN_CONTROL_PLUS")

    by_degree = {}
    results = {}
    for degree in range(7):
        keys = list(compositions(degree, 5))
        require(len(keys) == comb(degree + 4, 4), "DEGREE_COVERAGE")
        require(len(set(keys)) == len(keys), "UNIQUE_DEGREE_COVERAGE")
        by_degree[degree] = keys
        for counts in keys:
            require(counts not in results, "UNIQUE_GLOBAL_COVERAGE")
            require(sum(counts) == degree and min(counts) >= 0, "COUNT_DOMAIN")
            results[counts] = calculate(counts)
    require(len(results) == 462 and len(results) == comb(11, 5), "GLOBAL_COVERAGE_462")

    for counts, result in results.items():
        require(results[reflected(counts)] == result, "PHASE_REFLECTION")
        for shift in range(5):
            require(results[shifted(counts, shift)] == result, "GLOBAL_PHASE_SHIFT")

    known = results[(2, 1, 1, 1, 1)]
    require(known[1] == known[0], "KNOWN_POSITIVE_F_SATURATION")
    require(known[3] == (Fraction(1, 2), Fraction(0)), "KNOWN_HALF_RATIO")

    lines = ["P-PHOTON-Z5-STAR-QUADRATURE-1",
             "SCOPE=L4_FINITE_FACTOR_QUADRATURE",
             "PAIR_ENCODING=(a,b)_MEANS_a+b*sqrt(5)",
             "COVERAGE=462 DEGREES=0..6 INTERNAL_CERTIFICATES=PASS"]
    for degree in range(7):
        report, _, _ = extremal_report("DEGREE=" + str(degree), by_degree[degree], results)
        lines.extend(report)
    report, violating_half, violating_unit = extremal_report("GLOBAL", list(results), results)
    lines.extend(report)
    lines.append("CLASSIFICATION_HALF=" + ("FAIL_HALF" if violating_half else "PASS_HALF"))
    lines.append("CLASSIFICATION_STRICT_UNIT=" + ("FAIL_UNIT" if violating_unit else "PASS_UNIT"))
    for counts in violating_half:
        lines.append("HALF_COUNTEREXAMPLE=" + count_text(counts)
                     + " RATIO=" + pair_text(results[counts][3]))
    for counts in violating_unit:
        lines.append("STRICT_UNIT_COUNTEREXAMPLE=" + count_text(counts)
                     + " RATIO=" + pair_text(results[counts][3]))
    lines.append("END=CLASSIFIED_NO_PROBABILITY_OR_PHASE_CLAIM")
    output = "\n".join(lines) + "\n"
    require(output.isascii(), "ASCII_OUTPUT")
    return output


if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.stderr.write("STOP unexpected arguments\n")
        raise SystemExit(2)
    try:
        buffered_output = main()
    except Exception:
        sys.stdout.write("P-PHOTON-Z5-STAR-QUADRATURE-1 INTERNAL_ERROR\n")
        raise SystemExit(2)
    sys.stdout.write(buffered_output)
