#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Independent preregistered audit; NON-CANONICAL / L1.

Written from PREREG.md and its cited public mathematical premises without
reading verify.py. No implementation or generated data are imported from it.
Integer states use Z^5 / Z(1,1,1,1,1), normalized by subtracting the minimum.
Products use cyclic convolution; conjugation reverses the cyclic indices.
The final determinant uses rational field Gaussian elimination, with scalar
inverses computed by polynomial extended Euclid, not a permutation sum.
G0's finite enumeration is deliberately outside this checker's scope.
"""

from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json


CHECKS = 0


def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def z(values):
    values = tuple(values)
    if len(values) != 5 or any(type(a) is not int for a in values):
        raise TypeError("expected five integer cyclic coefficients")
    low = min(values)
    return tuple(a - low for a in values)


ZERO = z((0, 0, 0, 0, 0))
ONE = z((1, 0, 0, 0, 0))
JROOT = z((0, 1, 0, 0, 0))
RHO = z((0, 0, 1, 0, 0))


def za(a, b):
    return z(tuple(x + y for x, y in zip(a, b)))


def zn(a):
    return z(tuple(-x for x in a))


def zs(a, b):
    return za(a, zn(b))


def zi(n):
    return z((n, 0, 0, 0, 0))


def zm(a, b):
    out = [0] * 5
    for i, ai in enumerate(a):
        for k, bk in enumerate(b):
            out[(i + k) % 5] += ai * bk
    return z(tuple(out))


def zc(a):
    return z(tuple(a[(-i) % 5] for i in range(5)))


def divisible(a, n):
    return all(v % n == 0 for v in a)


def half(a):
    if not divisible(a, 2):
        raise ArithmeticError("nonintegral half in the cyclic quotient")
    return z(tuple(v // 2 for v in a))


def q(a):
    numerator = 5 * sum(v * v for v in a) - sum(a) ** 2
    if numerator % 2:
        raise ArithmeticError("half-trace not integral")
    return numerator // 2


def four(a):
    return [a[k] - a[4] for k in range(4)]


def residue(a):
    return sum(a) % 5


def sumz(values):
    total = ZERO
    for value in values:
        total = za(total, value)
    return total


def h_coordinates(a):
    coeff = four(a)
    require(coeff[1] == 0 and coeff[2] == coeff[3], "real-subring coordinates")
    return [coeff[0], -coeff[2]]


def contact(state, pair):
    i, k = pair
    a, b = state[i], state[k]
    difference = zs(a, b)
    if not divisible(difference, 2):
        return False, False, ZERO
    center, relative = half(za(a, b)), half(difference)
    rotated = zm(RHO, relative)
    state[i], state[k] = za(center, rotated), zs(center, rotated)
    return True, relative != ZERO, relative


def parse_word(text):
    return [(int(item[0]) - 1, int(item[1]) - 1) for item in text.split()]


P27 = parse_word(
    "12 12 12 12 35 36 16 16 16 16 46 46 46 46 24 "
    "36 36 36 36 16 12 12 46 45 45 45 45"
) + [(0, 2)] * 8
P35 = [(0, 1)] * 5 + ([(2, 4)] + [(2, 5)] * 5 + [(2, 4)] * 4) * 3
WORDS = {"P27": P27, "P35": P35}
B = zs(ONE, RHO)
U = zs(ONE, JROOT)
X = za(za(ONE, JROOT), zn(z((0, 0, 0, 2, 0))))
INITIAL = [B, zn(B), U, U, X, zi(2)]
T = 2 ** 35
EDGES = list(combinations(range(6), 2))


def inverse_word(word):
    return [pair for pair in reversed(word) for _ in range(4)]


def divergence(field):
    out = [ZERO] * 6
    for (a, b), value in zip(EDGES, field):
        out[a] = zs(out[a], value)
        out[b] = za(out[b], value)
    return out


def source_and_continuity(name, word):
    state = INITIAL.copy()
    field = [INITIAL[b] if a == 0 else ZERO for a, b in EDGES]
    first_field = field.copy()
    background = [zn(sumz(INITIAL))] + [ZERO] * 5
    source_residues = [residue(value) for value in state]
    source_sum = sumz(state)
    initial_diagnostic = sum(map(q, state)) + sum(map(q, field))
    counts = {"admitted": 0, "changed": 0, "diagonal": 0, "refused": 0}
    area = ZERO

    def check_cut():
        require(divergence(field) == [za(a, b) for a, b in zip(state, background)],
                "G1 exact Gauss at primitive cut")
        require(sum(map(q, state)) == 43, "source Q at primitive cut")
        require(sumz(state) == source_sum, "source sum at primitive cut")
        require([residue(value) for value in state] == source_residues,
                "source individual residues at primitive cut")

    check_cut()
    for pair in word:
        before = state[pair[0]]
        admitted, changed, relative = contact(state, pair)
        if admitted:
            counts["admitted"] += 1
            counts["changed" if changed else "diagonal"] += 1
            area = za(area, zm(relative, zc(relative)))
        else:
            counts["refused"] += 1
        current = zs(before, state[pair[0]])
        edge = EDGES.index(pair)
        field[edge] = za(field[edge], current)
        check_cut()

    require(state == INITIAL, "source return")
    require(h_coordinates(area) == [55, 20], "base path area")
    require(q_path(area) == 130, "base path half-trace")
    expected_admitted = 27 if name == "P27" else 35
    require(counts == {"admitted": expected_admitted, "changed": expected_admitted,
                       "diagonal": 0, "refused": 35 - expected_admitted},
            "source event counts")
    delta = [zs(a, b) for a, b in zip(field, first_field)]
    require(divergence(delta) == [ZERO] * 6, "closed-source current is divergence-free")
    if name == "P27":
        require(delta[EDGES.index((2, 4))] == zn(X), "P27 edge35 current obstruction")
        require(field != first_field, "P27 field nonreturn")
    else:
        require(field == first_field, "P35 field return")
    result = {
        "attempts": len(word), "Q_initial": 43, "path_H": h_coordinates(area),
        "path_Q": q_path(area), **counts,
        "delta_E": [four(value) for value in delta],
        "field_return": field == first_field,
        "diagnostic_initial": initial_diagnostic,
        "diagnostic_final": sum(map(q, state)) + sum(map(q, field)),
    }
    for pair in inverse_word(word):
        before = state[pair[0]]
        contact(state, pair)
        edge = EDGES.index(pair)
        field[edge] = za(field[edge], zs(before, state[pair[0]]))
        check_cut()
    require(state == INITIAL and field == first_field, "G1 complete literal inverse")
    result["inverse_attempts"] = 4 * len(word)
    return result


def q_path(area):
    a, b = h_coordinates(area)
    return 2 * a + b


# A separate rational field representation is used only for matrix auditing.
FZERO = (Fraction(0),) * 4
FONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
FRHO = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))


def fa(a, b):
    return tuple(x + y for x, y in zip(a, b))


def fn(a):
    return tuple(-x for x in a)


def fs(a, b):
    return fa(a, fn(b))


def fscale(a, scalar):
    return tuple(scalar * value for value in a)


def fm(a, b):
    coefficients = [Fraction(0)] * 7
    for i in range(4):
        for k in range(4):
            coefficients[i + k] += a[i] * b[k]
    for degree in range(6, 3, -1):
        lead = coefficients[degree]
        for shift in range(1, 5):
            coefficients[degree - shift] -= lead
        coefficients[degree] = Fraction(0)
    return tuple(coefficients[:4])


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_sub(a, b):
    return trim([(a[i] if i < len(a) else Fraction(0)) -
                 (b[i] if i < len(b) else Fraction(0))
                 for i in range(max(len(a), len(b)))])


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for k, bk in enumerate(b):
            out[i + k] += ai * bk
    return trim(out)


def poly_divmod(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError("zero polynomial")
    quotient = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        degree = len(a) - len(b)
        factor = a[-1] / b[-1]
        quotient[degree] += factor
        a = poly_sub(a, [Fraction(0)] * degree + [factor * v for v in b])
    return trim(quotient), a


def fi(a):
    if a == FZERO:
        raise ZeroDivisionError("zero field element")
    phi5 = [Fraction(1)] * 5
    old_r, r = phi5, trim(a)
    old_s, s = [Fraction(0)], [Fraction(1)]
    while r != [0]:
        quotient, remainder = poly_divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, poly_sub(old_s, poly_mul(quotient, s))
    require(len(old_r) == 1 and old_r[0] != 0, "field inverse gcd")
    candidate = [coefficient / old_r[0] for coefficient in old_s]
    _, candidate = poly_divmod(candidate, phi5)
    candidate += [Fraction(0)] * (4 - len(candidate))
    inverse = tuple(candidate)
    require(fm(a, inverse) == FONE, "polynomial inverse identity")
    return inverse


def as_field(a):
    return tuple(Fraction(value) for value in four(a))


def field_four(a):
    require(all(value.denominator == 1 for value in a), "integral field output")
    return [value.numerator for value in a]


def determinant(matrix):
    matrix = [row.copy() for row in matrix]
    answer = FONE
    for column in range(len(matrix)):
        pivot = next((row for row in range(column, len(matrix))
                      if matrix[row][column] != FZERO), None)
        if pivot is None:
            return FZERO
        if pivot != column:
            matrix[pivot], matrix[column] = matrix[column], matrix[pivot]
            answer = fn(answer)
        value = matrix[column][column]
        answer = fm(answer, value)
        reciprocal = fi(value)
        for row in range(column + 1, len(matrix)):
            factor = fm(matrix[row][column], reciprocal)
            for k in range(column + 1, len(matrix)):
                matrix[row][k] = fs(matrix[row][k], fm(factor, matrix[column][k]))
            matrix[row][column] = FZERO
    return answer


def witness_banks(name, word):
    banks = [INITIAL.copy() for _ in range(7)]
    for k in range(6):
        banks[k + 1][k] = za(banks[k + 1][k], zi(T))
    initial_banks = [bank.copy() for bank in banks]
    initial_residues = [[residue(value) for value in bank] for bank in banks]
    budget = 12 * T * T + 23 * T + 301
    initial_sum = sumz(value for bank in banks for value in bank)
    matrix = [[FONE if row == column else FZERO for column in range(6)]
              for row in range(6)]
    area = ZERO
    primitive_attempts = 0

    def check_cut():
        require(sum(q(value) for bank in banks for value in bank) == budget,
                "42-slot Q at primitive cut")
        require(sumz(value for bank in banks for value in bank) == initial_sum,
                "42-slot sum at primitive cut")
        require([[residue(value) for value in bank] for bank in banks] == initial_residues,
                "42-slot residues at primitive cut")

    check_cut()
    for index, pair in enumerate(word):
        for witness in banks[1:]:
            require(all(divisible(zs(a, b), 2 ** (35 - index))
                        for a, b in zip(witness, banks[0])), "pre-attempt dyadic agreement")
        flags = []
        for bank in banks:
            admitted, _, relative = contact(bank, pair)
            primitive_attempts += 1
            flags.append(admitted)
            if admitted:
                area = za(area, zm(relative, zc(relative)))
            check_cut()
        require(all(flag == flags[0] for flag in flags), "seven-bank admission agreement")
        if flags[0]:
            a, b = pair
            first, second = matrix[a].copy(), matrix[b].copy()
            for column in range(6):
                center = fscale(fa(first[column], second[column]), Fraction(1, 2))
                relative = fscale(fs(first[column], second[column]), Fraction(1, 2))
                rotated = fm(FRHO, relative)
                matrix[a][column], matrix[b][column] = fa(center, rotated), fs(center, rotated)
        for row in range(6):
            for column in range(6):
                actual = as_field(zs(banks[column + 1][row], banks[0][row]))
                require(actual == fscale(matrix[row][column], T), "actual difference equals T M")
    require(banks[0] == INITIAL, "witness source return")
    expected_phase = as_field(z((0, 0, 0, 0, 1))) if name == "P27" else FONE
    differences = [[as_field(zs(banks[column + 1][row], banks[0][row]))
                    for column in range(6)] for row in range(6)]
    actual_det = determinant(differences)
    require(actual_det == fscale(expected_phase, T ** 6), "actual determinant value")
    normalized = fscale(actual_det, Fraction(1, T ** 6))
    admitted_count = 27 if name == "P27" else 35
    expected_area = [385 + (T * T // 2) * admitted_count, 140]
    require(h_coordinates(area) == expected_area, "complete extended path area formula")
    if name == "P35":
        require(banks == initial_banks, "P35 all banks return")
    else:
        require(banks != initial_banks, "P27 retained witness")
    final_states = [[four(value) for value in bank] for bank in banks]
    fingerprint = sha256(json.dumps(final_states, separators=(",", ":")).encode()).hexdigest()
    result = {
        "attempts": primitive_attempts, "Q_initial": budget,
        "determinant": field_four(actual_det),
        "det_normalized": field_four(normalized),
        "extended_H": h_coordinates(area), "extended_path_Q": q_path(area),
        "state_sha256": fingerprint, "all_banks_return": banks == initial_banks,
    }
    inverse_attempts = 0
    for pair in reversed(word):
        for bank in reversed(banks):
            for _ in range(4):
                contact(bank, pair)
                inverse_attempts += 1
                check_cut()
    require(banks == initial_banks, "complete seven-bank literal inverse")
    require(primitive_attempts == 245 and inverse_attempts == 980, "complete attempt counts")
    result["inverse_attempts"] = inverse_attempts
    return result


def receiver_controls():
    root = ONE
    outputs = []
    word = [(0, 2), (0, 1)] * 5
    stock = z((3, 4, 2, 0, 0))
    for index in range(5):
        state = [root, zn(root), stock]
        initial = state.copy()
        residues = [residue(value) for value in state]
        for pair in word:
            contact(state, pair)
            require(sum(map(q, state)) == 36, "receiver total account")
            require([residue(value) for value in state] == residues, "receiver residues")
        outputs.append(q(state[2]))
        for pair in inverse_word(word):
            contact(state, pair)
            require(sum(map(q, state)) == 36, "receiver inverse account")
        require(state == initial, "receiver inverse")
        root = zm(root, JROOT)
    require(outputs == [32, 17, 2, 7, 27], "five receiver responses")
    return outputs


def main():
    require(all(len(word) == 35 for word in WORDS.values()), "equal attempt horizons")
    require(sum(map(q, INITIAL)) == 43, "initial source budget")
    diagonal, refused = [ZERO, ZERO], [ZERO, ONE]
    first = contact(diagonal, (0, 1))
    second = contact(refused, (0, 1))
    require(first == (True, False, ZERO), "admitted zero-current diagonal")
    require(second == (False, False, ZERO), "refused zero-current event")
    results = {
        "implementation": "independent cyclic-five integer quotient; Euclid field elimination",
        "scope": "source, G1, M, zero-current and receiver; G0 enumeration omitted",
        "T": T,
        "source_and_G1": {name: source_and_continuity(name, word) for name, word in WORDS.items()},
        "matrix": {name: witness_banks(name, word) for name, word in WORDS.items()},
        "receiver": receiver_controls(),
    }
    require(results["matrix"]["P35"]["extended_H"][0] -
            results["matrix"]["P27"]["extended_H"][0] == 4 * T * T,
            "extended area difference")
    results["checks"] = CHECKS
    print(json.dumps(results, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
