#!/usr/bin/env python3
"""Exact audit for P-O5-GOLDEN-PROFILE-TRANSFER-1."""

from __future__ import annotations

import ast
from bisect import bisect_left
from fractions import Fraction
from pathlib import Path


LUCAS_COUNT = 60
PRODUCT_LIMIT = 512
THRESHOLD_MAX_K = 30
FOUR_DIAGONAL_MAX_K = 12

Y_VALUES = (
    0, 1, 2, 5, 6, 10, 11, 17, 18, 45, 46, 47, 121, 122, 123,
    320, 321, 322, 360, 361, 841, 842, 843, 1680, 1681,
)


def check(label, condition, detail=""):
    if not condition:
        raise AssertionError(f"{label} failed: {detail}")


# Elements a+b*alpha in Q(alpha), alpha^2=3*alpha-1.  Both coordinates are
# Fraction, so this representation is exact for every threshold below.
QZERO = (Fraction(0), Fraction(0))
QONE = (Fraction(1), Fraction(0))
ALPHA = (Fraction(0), Fraction(1))
ALPHA_INV = (Fraction(3), Fraction(-1))


def q(value=0, alpha_coefficient=0):
    return Fraction(value), Fraction(alpha_coefficient)


def qadd(left, right):
    return left[0] + right[0], left[1] + right[1]


def qneg(value):
    return -value[0], -value[1]


def qsub(left, right):
    return qadd(left, qneg(right))


def qmul(left, right):
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c + 3 * b * d


def qscale(value, scalar):
    scalar = Fraction(scalar)
    return scalar * value[0], scalar * value[1]


def alpha_power(exponent):
    exponent = int(exponent)
    base = ALPHA
    if exponent < 0:
        base = ALPHA_INV
        exponent = -exponent
    out = QONE
    while exponent:
        if exponent & 1:
            out = qmul(out, base)
        base = qmul(base, base)
        exponent //= 2
    return out


def rational_sign(value):
    return (value > 0) - (value < 0)


def qsign(value):
    # a+b*alpha = ((2a+3b)+b*sqrt(5))/2.  Compare opposite-sign
    # rational terms by squaring their nonnegative magnitudes.
    a, b = value
    rational = 2 * a + 3 * b
    radical = b
    if radical == 0:
        return rational_sign(rational)
    if rational >= 0 and radical > 0:
        return 1
    if rational <= 0 and radical < 0:
        return -1
    if rational > 0 and radical < 0:
        comparison = rational * rational - 5 * radical * radical
        check("quadratic sign nondegenerate", comparison != 0, value)
        return rational_sign(comparison)
    check("quadratic sign branch", rational < 0 and radical > 0, value)
    comparison = 5 * radical * radical - rational * rational
    check("quadratic sign nondegenerate", comparison != 0, value)
    return rational_sign(comparison)


def qle(left, right):
    return qsign(qsub(right, left)) >= 0


def qlt(left, right):
    return qsign(qsub(right, left)) > 0


def lucas_even(count):
    values = [2, 3]
    while len(values) < count:
        values.append(3 * values[-1] - values[-2])
    return tuple(values[:count])


LUCAS_EVEN = lucas_even(LUCAS_COUNT)
X = tuple(value - 1 for value in LUCAS_EVEN)
M = tuple(value // 11 for value in X)
R = tuple(value % 11 for value in X)
RESIDUE_PATTERN = (1, 2, 6, 6, 2)
FORCING_PATTERN = (0, 1, 1, 0, 0)


def shell_index(n):
    check("positive integer carrier", type(n) is int and n >= 1, n)
    if n == 1:
        return -1
    index = bisect_left(X, n) - 1
    check("shell table coverage", 0 <= index < len(X) - 1, n)
    return index


def shell_bounds(k):
    if k == -1:
        return 1, 1
    check("shell bound index", 0 <= k < len(X) - 1, k)
    return X[k] + 1, X[k + 1]


def z_value(n):
    return qscale(alpha_power(-shell_index(n)), n)


def canonical_sequence(raw):
    out = {}
    for n, value in raw.items():
        check("sequence positive key", type(n) is int and n >= 1, n)
        check("sequence integer value", type(value) is int, (n, value))
        if value:
            out[n] = value
    return out


def profile(sequence, k):
    out = {}
    for n, value in sequence.items():
        if shell_index(n) != k:
            continue
        key = z_value(n)
        check("profile key collision", key not in out, (k, n, key))
        out[key] = value
    return out


def decode_profile(shell_profile, k):
    out = {}
    scale = alpha_power(k)
    for reduced_mantissa, value in shell_profile.items():
        integer = qmul(reduced_mantissa, scale)
        check("profile decode alpha coefficient", integer[1] == 0, (k, integer))
        check(
            "profile decode integer",
            integer[0].denominator == 1 and integer[0] >= 1,
            (k, integer),
        )
        n = integer[0].numerator
        check("profile decode shell", shell_index(n) == k, (k, n))
        check("profile decode collision", n not in out, (k, n))
        out[n] = value
    return out


def max_shell(sequence):
    return max((shell_index(n) for n in sequence), default=-1)


def shell_mass(sequence, k):
    return sum(value for n, value in sequence.items() if shell_index(n) == k)


def shell_mass_state(sequence):
    state = {}
    for n, value in sequence.items():
        k = shell_index(n)
        state[k] = state.get(k, 0) + value
    return {k: value for k, value in state.items() if value}


def complete_diagonal_state(sequence):
    masses = shell_mass_state(sequence)
    state = {}
    for i, left in masses.items():
        for j, right in masses.items():
            s = i + j
            state[s] = state.get(s, 0) + left * right
    return {s: value for s, value in state.items() if value}


def integer_pair(sequence, i, j, cutoff):
    total = 0
    for a, left in sequence.items():
        if shell_index(a) != i:
            continue
        for b, right in sequence.items():
            if shell_index(b) == j and a * b <= cutoff:
                total += left * right
    return total


def profile_pair(sequence, i, j, cutoff):
    threshold = qscale(alpha_power(-(i + j)), cutoff)
    total = 0
    for x, left in profile(sequence, i).items():
        for y, right in profile(sequence, j).items():
            if qle(qmul(x, y), threshold):
                total += left * right
    return total


def direct_h(sequence, cutoff):
    return sum(
        left * right
        for a, left in sequence.items()
        for b, right in sequence.items()
        if a * b <= cutoff
    )


def direct_q(sequence, cutoff):
    lower = cutoff // 11
    return sum(
        left * right
        for a, left in sequence.items()
        for b, right in sequence.items()
        if lower < a * b <= cutoff
    )


def profile_h(sequence, cutoff):
    top = max_shell(sequence)
    return sum(
        profile_pair(sequence, i, j, cutoff)
        for i in range(-1, top + 1)
        for j in range(-1, top + 1)
    )


def diagonal_pair(sequence, s, cutoff):
    top = max_shell(sequence)
    return sum(
        profile_pair(sequence, i, s - i, cutoff)
        for i in range(-1, top + 1)
        if -1 <= s - i <= top
    )


def complete_diagonal(sequence, s):
    top = max_shell(sequence)
    return sum(
        shell_mass(sequence, i) * shell_mass(sequence, s - i)
        for i in range(-1, top + 1)
        if -1 <= s - i <= top
    )


def lucas_four_diagonal(sequence, k):
    n = X[k]
    lower = n // 11
    return (
        complete_diagonal(sequence, k - 4) - diagonal_pair(sequence, k - 4, lower)
        + complete_diagonal(sequence, k - 3) - diagonal_pair(sequence, k - 3, lower)
        + complete_diagonal(sequence, k - 2)
        + diagonal_pair(sequence, k - 1, n)
    )


F_EMPTY = {}
F_BOUNDARY = {
    1: 2, 2: -3, 3: 5, 6: -7, 7: 11, 17: -13, 18: 17,
    46: -19, 47: 23, 122: -29, 123: 31, 321: -37, 322: 41,
    842: -43,
}
F_MIXED = {
    3: 0, 19: -1, 29: 2, 31: -3, 41: 4, 59: -5, 61: 6,
    360: 0, 361: -7, 500: 8, 841: -9, 842: 10, 843: -11,
    1681: 12,
}
PROFILE_FIXTURES = (F_EMPTY, F_BOUNDARY, F_MIXED)


def factorization(n):
    check("factorization domain", type(n) is int and n >= 1, n)
    out = []
    remainder = n
    p = 2
    while p * p <= remainder:
        if remainder % p:
            p += 1
            continue
        exponent = 0
        while remainder % p == 0:
            remainder //= p
            exponent += 1
        out.append((p, exponent))
        p += 1
    if remainder > 1:
        out.append((remainder, 1))
    return tuple(out)


def chi5(n):
    residue = n % 5
    if residue == 0:
        return 0
    return 1 if residue in (1, 4) else -1


def actual_nu(n):
    if n == 1:
        return 1
    factors = factorization(n)
    sign = 1
    for prime, exponent in factors:
        if exponent != 1 or prime <= 11 or chi5(prime) != 1:
            return 0
        sign = -sign
    return sign


def in_f_nu(sequence):
    return all(value == actual_nu(n) for n, value in sequence.items())


def cutoff_forcing(k):
    check("forcing index", 1 <= k < len(R) - 1, k)
    numerator = 3 * R[k] - R[k - 1] + 1 - R[k + 1]
    check("forcing divisibility", numerator % 11 == 0, (k, numerator))
    return numerator // 11


def gate_01():
    check("Lucas starts", LUCAS_EVEN[:8] == (2, 3, 7, 18, 47, 123, 322, 843))
    check("cutoff starts", X[:8] == (1, 2, 6, 17, 46, 122, 321, 842))
    for k in range(1, 50):
        check("Lucas recurrence", LUCAS_EVEN[k + 1] == 3 * LUCAS_EVEN[k] - LUCAS_EVEN[k - 1], k)
        check("cutoff recurrence", X[k + 1] == 3 * X[k] - X[k - 1] + 1, k)
    for k in range(0, 51):
        check("residue five-cycle", R[k] == RESIDUE_PATTERN[k % 5], k)
    check("residue state return", R[5:7] == R[0:2])
    for period in range(1, 5):
        check(
            "residue period minimal",
            any(R[k] != R[k + period] for k in range(0, 20 - period)),
            period,
        )


def gate_02():
    check("lower cutoff starts", M[:8] == (0, 0, 0, 1, 4, 11, 29, 76))
    for k in range(0, 51):
        check("cutoff quotient and residue", X[k] == 11 * M[k] + R[k], k)
        check("least residue range", 0 <= R[k] <= 10, (k, R[k]))
    for k in range(1, 50):
        forcing = cutoff_forcing(k)
        check("forcing pattern", forcing == FORCING_PATTERN[(k - 1) % 5], k)
        check(
            "lower cutoff recurrence",
            M[k + 1] - 3 * M[k] + M[k - 1] == forcing,
            k,
        )
    for k in range(0, 44):
        value = (
            M[k + 7] - 3 * M[k + 6] + M[k + 5]
            - M[k + 2] + 3 * M[k + 1] - M[k]
        )
        check("order seven recurrence", value == 0, (k, value))


def gate_03():
    check("alpha inverse", qmul(ALPHA, ALPHA_INV) == QONE)
    check("alpha above one", qlt(QONE, ALPHA))
    indices = [None] + [shell_index(n) for n in range(1, PRODUCT_LIMIT + 1)]
    mantissas = [None] + [z_value(n) for n in range(1, PRODUCT_LIMIT + 1)]
    for n in range(1, PRODUCT_LIMIT + 1):
        check("mantissa lower", qlt(QONE, mantissas[n]), n)
        check("mantissa upper", qle(mantissas[n], ALPHA), n)
    for a in range(1, PRODUCT_LIMIT + 1):
        i = indices[a]
        x = mantissas[a]
        for b in range(1, PRODUCT_LIMIT + 1):
            j = indices[b]
            y = mantissas[b]
            xy = qmul(x, y)
            epsilon = 0 if qle(xy, ALPHA) else 1
            check(
                "skew product shell",
                shell_index(a * b) == i + j + epsilon,
                (a, b, i, j, epsilon, shell_index(a * b)),
            )
            expected_z = qmul(xy, alpha_power(-epsilon))
            check("skew product mantissa", z_value(a * b) == expected_z, (a, b))


def gate_04():
    for raw in PROFILE_FIXTURES:
        sequence = canonical_sequence(raw)
        top = max_shell(sequence)
        for k in range(-1, top + 1):
            expected = {
                n: value for n, value in sequence.items() if shell_index(n) == k
            }
            encoded = profile(sequence, k)
            check("profile cardinality", len(encoded) == len(expected), (k, raw))
            check("profile decode", decode_profile(encoded, k) == expected, (k, raw))
        for cutoff in Y_VALUES:
            for i in range(-1, top + 1):
                for j in range(-1, top + 1):
                    check(
                        "profile kernel pair",
                        profile_pair(sequence, i, j, cutoff)
                        == integer_pair(sequence, i, j, cutoff),
                        (raw, cutoff, i, j),
                    )
            check("profile H reconstruction", profile_h(sequence, cutoff) == direct_h(sequence, cutoff), (raw, cutoff))
            check(
                "profile Q reconstruction",
                profile_h(sequence, cutoff) - profile_h(sequence, cutoff // 11)
                == direct_q(sequence, cutoff),
                (raw, cutoff),
            )
        for k in range(4, FOUR_DIAGONAL_MAX_K + 1):
            check(
                "Lucas four diagonal arbitrary profile",
                lucas_four_diagonal(sequence, k) == direct_q(sequence, X[k]),
                (raw, k, lucas_four_diagonal(sequence, k), direct_q(sequence, X[k])),
            )

    alpha_three_over_eleven = qscale(alpha_power(3), Fraction(1, 11))
    alpha_four_over_eleven = qscale(alpha_power(4), Fraction(1, 11))
    for k in range(4, THRESHOLD_MAX_K + 1):
        n = X[k]
        lower = M[k]
        residue = R[k]

        upper_lhs = qscale(alpha_power(-(k - 1)), n)
        upper_rhs = qadd(
            qsub(ALPHA, alpha_power(1 - k)),
            alpha_power(1 - 2 * k),
        )
        check("upper threshold formula", upper_lhs == upper_rhs, k)

        lower_three_lhs = qscale(alpha_power(-(k - 3)), lower)
        lower_three_rhs = qscale(
            qsub(
                qadd(alpha_power(3), alpha_power(3 - 2 * k)),
                qscale(alpha_power(3 - k), 1 + residue),
            ),
            Fraction(1, 11),
        )
        check("lower three threshold formula", lower_three_lhs == lower_three_rhs, k)

        lower_four_lhs = qscale(alpha_power(-(k - 4)), lower)
        lower_four_rhs = qmul(ALPHA, lower_three_rhs)
        check("lower four threshold formula", lower_four_lhs == lower_four_rhs, k)

        check("upper threshold tends from below", qlt(upper_lhs, ALPHA), k)
        check("lower three tends from below", qlt(lower_three_lhs, alpha_three_over_eleven), k)
        check("lower four tends from below", qlt(lower_four_lhs, alpha_four_over_eleven), k)


def gate_05():
    f = canonical_sequence({19: -1})
    g = canonical_sequence({41: -1})
    check("f belongs to F_nu", in_f_nu(f))
    check("g belongs to F_nu", in_f_nu(g))
    check("no-go source shells", shell_index(19) == shell_index(41) == 3)
    check("complete shell mass state f", shell_mass_state(f) == {3: -1})
    check("complete shell mass state g", shell_mass_state(g) == {3: -1})
    check("equal complete shell mass states", shell_mass_state(f) == shell_mass_state(g))
    check("complete diagonal state f", complete_diagonal_state(f) == {6: 1})
    check("complete diagonal state g", complete_diagonal_state(g) == {6: 1})
    check("equal complete diagonal states", complete_diagonal_state(f) == complete_diagonal_state(g))
    check("profiles differ", profile(f, 3) != profile(g, 3))
    check("no-go f annulus", direct_q(f, 842) == 1)
    check("no-go g annulus", direct_q(g, 842) == 0)


def gate_06():
    expected_primes = (
        19, 29, 31, 41, 59, 61, 71, 79, 89, 101, 109, 131, 139,
        149, 151, 179, 181, 191, 199, 211, 229, 239, 241, 251, 269,
        271, 281, 311,
    )
    actual = canonical_sequence({n: actual_nu(n) for n in range(1, X[6] + 1)})
    check("actual nu support", tuple(actual) == (1,) + expected_primes, tuple(actual))
    check("actual nu unit", actual_nu(1) == 1)
    check("actual nu selected primes", all(actual_nu(p) == -1 for p in (19, 29, 31, 41)))
    check("actual nu exclusions", actual_nu(2) == actual_nu(5) == actual_nu(11) == actual_nu(361) == 0)
    check("actual nu product", actual_nu(19 * 29) == 1)
    values = tuple(direct_q(actual, X[k]) for k in (4, 5, 6))
    check("actual Q values", values == (-8, -22, -52), values)
    prediction = 3 * values[1] - values[0]
    check("naive recurrence prediction", prediction == -58, prediction)
    check("actual recurrence failure", values[2] != prediction, (values[2], prediction))
    check("cutoff forcing c5", cutoff_forcing(5) == 0)


# Production-path mutations.  G07 must call these functions, not merely restate
# the correct witnesses checked by G01--G06.
def mutation_b1_next_cutoff(previous, current):
    return 3 * current - previous


def mutation_b2_zero_carry_product_shell(a, b):
    return shell_index(a) + shell_index(b)


def mutation_b3_complete_mass_pair(sequence, i, j):
    return shell_mass(sequence, i) * shell_mass(sequence, j)


def mutation_b4_period_four_residue(k):
    return RESIDUE_PATTERN[k % 4]


def mutation_b5_naive_q_next(previous, current, forcing):
    return 3 * current - previous + forcing


def gate_07():
    first_b1 = None
    for k in range(1, 20):
        mutated = mutation_b1_next_cutoff(X[k - 1], X[k])
        if mutated != X[k + 1]:
            first_b1 = (k, mutated, X[k + 1])
            break
    check("B1 first witness", first_b1 == (1, 5, 6), first_b1)

    b2_mutated = mutation_b2_zero_carry_product_shell(41, 41)
    b2_actual = shell_index(41 * 41)
    check("B2 witness", (b2_mutated, b2_actual) == (6, 7), (b2_mutated, b2_actual))

    f = canonical_sequence({19: -1})
    g = canonical_sequence({41: -1})
    b3_f = mutation_b3_complete_mass_pair(f, 3, 3)
    b3_g = mutation_b3_complete_mass_pair(g, 3, 3)
    check("B3 mass mutation same", b3_f == b3_g == 1, (b3_f, b3_g))
    check("B3 kernel witness f", integer_pair(f, 3, 3, 842) == 1)
    check("B3 kernel witness g", integer_pair(g, 3, 3, 842) == 0)

    first_b4 = None
    for k in range(20):
        mutated = mutation_b4_period_four_residue(k)
        if mutated != R[k]:
            first_b4 = (k, mutated, R[k])
            break
    check("B4 first witness", first_b4 == (4, 1, 2), first_b4)

    b5_mutated = mutation_b5_naive_q_next(-8, -22, cutoff_forcing(5))
    check("B5 witness", (cutoff_forcing(5), b5_mutated, -52) == (0, -58, -52))


def imported_roots(node):
    if isinstance(node, ast.Import):
        return tuple(alias.name.split(".")[0] for alias in node.names)
    if isinstance(node, ast.ImportFrom):
        return ((node.module or "").split(".")[0],)
    return ()


def gate_08():
    raw = Path(__file__).read_bytes()
    check("final LF", raw.endswith(b"\n"))
    check("LF only", b"\r" not in raw)
    tree = ast.parse(raw.decode("utf-8"), filename=__file__)
    allowed_imports = {"__future__", "ast", "bisect", "fractions", "pathlib"}
    forbidden_names = {
        "__builtins__", "__import__", "compile", "complex", "eval", "exec",
        "float", "getattr", "globals", "input", "locals", "open", "round",
        "setattr", "vars",
    }
    forbidden_attributes = {"from_float", "fromhex"}
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.extend(imported_roots(node))
        if isinstance(node, ast.Constant):
            check(
                "no float or complex literal",
                type(node.value).__name__ not in {"float", "complex"},
            )
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            check("forbidden dynamic or inexact name", node.id not in forbidden_names, node.id)
        if isinstance(node, ast.Attribute):
            check("forbidden inexact attribute", node.attr not in forbidden_attributes, node.attr)
        if isinstance(node, ast.BinOp):
            check("no true division", not isinstance(node.op, ast.Div))
            check("no exponent operator", not isinstance(node.op, ast.Pow))
    check("exact import allowlist", set(imports) <= allowed_imports, imports)


def main():
    gate_01()
    print("G01 PASS Lucas cutoff recurrence and residue 5-cycle")
    gate_02()
    print("G02 PASS lower cutoff forcing and order-seven transfer")
    gate_03()
    print("G03 PASS exact golden skew-product multiplication")
    gate_04()
    print("G04 PASS arbitrary-profile kernels and Lucas thresholds")
    gate_05()
    print("G05 PASS scalar shell-mass closure no-go")
    gate_06()
    print("G06 PASS actual nu Q values and recurrence failure")
    gate_07()
    print("G07 PASS breakers B1-B5 frozen witnesses")
    gate_08()
    print("G08 PASS exact-quadratic stdlib AST firewall")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
