#!/usr/bin/env python3
"""Exact audit for P-FCC-WEIGHTED-SHELL-SYMBOL-1.

Standard library only.  The theorem source is the finite written proof in
PREREG.md; this program independently audits its integer identities.
"""

from __future__ import annotations

import sys
from collections import defaultdict
from itertools import permutations, product
from math import factorial


SHELL_NORMS = (2, 4, 8, 10, 16)
SHELL_REPS = {
    2: (1, 1, 0),
    4: (2, 0, 0),
    8: (2, 2, 0),
    10: (3, 1, 0),
    16: (4, 0, 0),
}
SHELL_SIZES = (12, 6, 12, 24, 6)
WEIGHTS = (6, 1, 15, 1, 1)


class GateError(Exception):
    """A deterministic integrity or audit gate stopped the run."""


def require(condition: bool, label: str) -> None:
    if not condition:
        raise GateError(label)


def shell(norm: int) -> tuple[tuple[int, int, int], ...]:
    points = []
    for x, y, z in product(range(-4, 5), repeat=3):
        if x * x + y * y + z * z == norm:
            points.append((x, y, z))
    return tuple(sorted(points))


def group_elements() -> tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]:
    elements = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            elements.append((perm, signs))
    return tuple(elements)


def act(
    element: tuple[tuple[int, int, int], tuple[int, int, int]],
    vector: tuple[int, int, int],
) -> tuple[int, int, int]:
    perm, signs = element
    return tuple(signs[i] * vector[perm[i]] for i in range(3))


def orbit(
    vector: tuple[int, int, int],
    group: tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...],
) -> frozenset[tuple[int, int, int]]:
    return frozenset(act(element, vector) for element in group)


def multinomial(degree: int, exponents: tuple[int, int, int]) -> int:
    value = factorial(degree)
    for exponent in exponents:
        value //= factorial(exponent)
    return value


def exponent_triples(degree: int):
    for a in range(degree + 1):
        for b in range(degree - a + 1):
            yield (a, b, degree - a - b)


def moment(
    degree: int,
    shells: dict[int, tuple[tuple[int, int, int], ...]],
    weights: tuple[int, int, int, int, int],
) -> dict[tuple[int, int, int], int]:
    coefficients: defaultdict[tuple[int, int, int], int] = defaultdict(int)
    for norm, weight in zip(SHELL_NORMS, weights):
        for vector in shells[norm]:
            for exponents in exponent_triples(degree):
                coefficient = multinomial(degree, exponents)
                for coordinate, exponent in zip(vector, exponents):
                    coefficient *= coordinate**exponent
                coefficients[exponents] += weight * coefficient
    return {key: value for key, value in sorted(coefficients.items()) if value != 0}


def expected_m2() -> dict[tuple[int, int, int], int]:
    return {(0, 0, 2): 648, (0, 2, 0): 648, (2, 0, 0): 648}


def expected_m4() -> dict[tuple[int, int, int], int]:
    result = {}
    for axis in range(3):
        exponents = [0, 0, 0]
        exponents[axis] = 4
        result[tuple(exponents)] = 3168
    for first in range(3):
        for second in range(first + 1, 3):
            exponents = [0, 0, 0]
            exponents[first] = 2
            exponents[second] = 2
            result[tuple(exponents)] = 6336
    return dict(sorted(result.items()))


def expected_m6() -> dict[tuple[int, int, int], int]:
    result = {}
    for axis in range(3):
        exponents = [0, 0, 0]
        exponents[axis] = 6
        result[tuple(exponents)] = 21888
    for fourth_axis in range(3):
        for square_axis in range(3):
            if fourth_axis == square_axis:
                continue
            exponents = [0, 0, 0]
            exponents[fourth_axis] = 4
            exponents[square_axis] = 2
            result[tuple(exponents)] = 63360
    return dict(sorted(result.items()))


def cone_value(weights: tuple[int, int, int, int, int]) -> int:
    coefficients = (-4, 32, -64, 440, 512)
    return sum(coefficient * weight for coefficient, weight in zip(coefficients, weights))


def bounded_positive_solutions(max_total: int):
    for total in range(5, max_total + 1):
        for a in range(1, total - 3):
            for b in range(1, total - a - 2):
                for c in range(1, total - a - b - 1):
                    for d in range(1, total - a - b - c):
                        e = total - a - b - c - d
                        candidate = (a, b, c, d, e)
                        if cone_value(candidate) == 0:
                            yield candidate


def elimination_solutions(max_total: int):
    solutions = []
    for w4, w8, w10, w16 in product(range(1, max_total), repeat=4):
        w2 = 8 * w4 - 16 * w8 + 110 * w10 + 128 * w16
        candidate = (w2, w4, w8, w10, w16)
        if w2 >= 1 and sum(candidate) <= max_total:
            solutions.append(candidate)
    return tuple(sorted(set(solutions), key=lambda item: (sum(item), item)))


def weighted_multiset(
    shells: dict[int, tuple[tuple[int, int, int], ...]],
    weights: tuple[int, int, int, int, int],
) -> dict[tuple[int, int, int], int]:
    result = {}
    for norm, weight in zip(SHELL_NORMS, weights):
        for vector in shells[norm]:
            require(vector not in result, "OVERLAPPING_SHELLS")
            result[vector] = weight
    return result


def invariant_under_group(
    weighted: dict[tuple[int, int, int], int],
    group: tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...],
) -> bool:
    for element in group:
        transformed = {act(element, vector): weight for vector, weight in weighted.items()}
        if transformed != weighted:
            return False
    return True


def evaluate() -> tuple[str, ...]:
    lines = []
    shells = {norm: shell(norm) for norm in SHELL_NORMS}
    group = group_elements()

    require(tuple(len(shells[norm]) for norm in SHELL_NORMS) == SHELL_SIZES, "G01_SHELL_SIZES")
    lines.append("G01 shell sizes 12,6,12,24,6 PASS")

    require(all(sum(vector) % 2 == 0 for values in shells.values() for vector in values), "G02_FCC_PARITY")
    lines.append("G02 FCC even-coordinate-sum carrier PASS")

    require(len(group) == 48 and len(set(group)) == 48, "G03_GROUP_ORDER")
    require(all(orbit(SHELL_REPS[norm], group) == frozenset(shells[norm]) for norm in SHELL_NORMS), "G03_SINGLE_ORBITS")
    lines.append("G03 48 signed permutations and five single orbits PASS")

    require(all(weight >= 1 for weight in WEIGHTS) and cone_value(WEIGHTS) == 0, "G04_WEIGHT_ADMISSIBILITY")
    lines.append("G04 Wstar positive and cone value zero PASS")

    route_one = tuple(bounded_positive_solutions(24))
    route_two = elimination_solutions(24)
    require(route_one == (WEIGHTS,), "G05_MINIMUM_ENUMERATION")
    require(route_two == (WEIGHTS,), "G05_MINIMUM_ELIMINATION")
    require(cone_value((230, 1, 1, 1, 1)) == 0, "G05_OUTSIDE_CONTROL")
    lines.append("G05 Wstar unique minimum total 24 by two routes PASS")

    m2 = moment(2, shells, WEIGHTS)
    m4 = moment(4, shells, WEIGHTS)
    m6 = moment(6, shells, WEIGHTS)
    require(m2 == expected_m2(), "G06_M2")
    lines.append("G06 M2 equals 648 times norm-square PASS")
    require(m4 == expected_m4(), "G07_M4")
    lines.append("G07 M4 equals 3168 times norm-fourth PASS")
    require(m6 == expected_m6(), "G08_M6")
    lines.append("G08 M6 coefficient block 21888,63360,0 PASS")

    require(m6.get((4, 2, 0)) != 3 * m6[(6, 0, 0)], "G09_SIXTH_ORDER_MIXED")
    require(m6.get((2, 2, 2), 0) != 6 * m6[(6, 0, 0)], "G09_SIXTH_ORDER_TRIPLE")
    lines.append("G09 sixth-order isotropy refuted exactly PASS")

    weighted = weighted_multiset(shells, WEIGHTS)
    require(len(weighted) == 60 and sum(weighted.values()) == 288, "G10_WEIGHTED_MASS")
    require(invariant_under_group(weighted, group), "G10_GROUP_INVARIANCE")
    lines.append("G10 weighted mass 288 and full group invariance PASS")

    require(m2[(2, 0, 0)] // 2 == 324, "G11_TAYLOR_SECOND")
    require(m4[(4, 0, 0)] // 24 == 132, "G11_TAYLOR_FOURTH")
    lines.append("G11 Taylor coefficients -324 and 132 PASS")

    shell_nine = frozenset(shell(9))
    remaining = set(shell_nine)
    orbit_sizes = []
    while remaining:
        seed = min(remaining)
        current = orbit(seed, group)
        orbit_sizes.append(len(current))
        remaining.difference_update(current)
    require(sorted(orbit_sizes) == [6, 24], "S01_NORM9_SPLIT")
    lines.append("S01 norm-nine split-orbit control 6,24 PASS")

    require(cone_value((1, 1, 1, 1, 1)) == 916, "S02_UNIFORM_CONE")
    mutated_m2 = moment(2, shells, (7, 1, 15, 1, 1))
    require(mutated_m2[(2, 0, 0)] == 656 and mutated_m2 != expected_m2(), "S02_WEIGHT_MUTATION")
    lines.append("S02 uniform and weight-mutation controls PASS")

    dropped = dict(weighted)
    dropped.pop(min(shells[2]))
    require(not invariant_under_group(dropped, group), "S03_DROPPED_VECTOR")
    lines.append("S03 dropped-vector symmetry breaker PASS")

    return tuple(lines)


def render(lines: tuple[str, ...]) -> bytes:
    header = (
        "P-FCC-WEIGHTED-SHELL-SYMBOL-1\n",
        "ARITHMETIC exact-integer\n",
    )
    body = tuple(line + "\n" for line in lines)
    footer = (
        "S04 fresh-state deterministic replay PASS\n",
        "OUTCOME SYMBOL-PROVED\n",
        "RESULT 15/15 ALL PASS\n",
    )
    return "".join(header + body + footer).encode("ascii")


def main() -> int:
    if len(sys.argv) != 1:
        sys.stderr.write("usage: verify.py\n")
        return 2
    try:
        first = evaluate()
        second = evaluate()
        require(first == second, "S04_NONDETERMINISTIC")
        transcript = render(first)
        require(transcript == render(second), "S04_RENDER_NONDETERMINISTIC")
    except GateError as exc:
        sys.stderr.write("STOP " + str(exc) + "\n")
        return 1
    sys.stdout.buffer.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
