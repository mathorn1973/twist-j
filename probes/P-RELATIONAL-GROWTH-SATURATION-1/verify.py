#!/usr/bin/env python3
"""Exact finite audit of the separately written, result-exposed proof.

Python >= 3.10, standard library only. No external inputs or file reads.
Finite checks audit universal proofs; they do not supply their quantifiers.
"""

from fractions import Fraction
from itertools import product
from math import comb, factorial


COUNTS = {}
NAME = "P-RELATIONAL-GROWTH-SATURATION-1"
STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))
FIBER_STEPS = ((3, 0), (2, 0), (3, 3), (2, 2), (1, 3), (4, 2))
T1 = (0, 0, 0, 0, -2, 0)
T2 = (-5, -5, -5, -5, -2, -2)
T3 = (-5, -5, -5, -5, -4, -2)
LETTERS = ("a", "b", "c", "d", "e")
PAIR_TRANSLATIONS = (("d", "e", T1), ("b", "d", T2), ("b", "e", T3))


def check(condition, section, case):
    if not condition:
        raise AssertionError((section, case))
    COUNTS[section] = COUNTS.get(section, 0) + 1


def binom(n, r):
    return comb(n, r) if n >= r else 0


def falling(n, r):
    value = 1
    for j in range(r):
        value *= n - j
    return value


def differences(values):
    return [b - a for a, b in zip(values, values[1:])]


def accumulation():
    section = "ACCUMULATION"
    for n in range(65):
        for r in range(9):
            check(
                sum(binom(k, r) for k in range(n)) == binom(n, r + 1),
                section, ("hockey-stick", n, r),
            )
            check(
                binom(n + 1, r + 1) - binom(n, r + 1) == binom(n, r),
                section, ("antidifference", n, r),
            )
            if r:
                check(
                    sum(falling(k, r) for k in range(1, n + 1))
                    == factorial(r) * binom(n + 1, r + 1),
                    section, ("falling-factorial", n, r),
                )
    for a, b in product(range(8), repeat=2):
        layers = [
            sum(a if i == j else b for i in range(k) for j in range(k))
            for k in range(65)
        ]
        total = 0
        volumes = []
        for n, layer in enumerate(layers):
            check(layer == a * n + b * n * (n - 1), section, ("layer", a, b, n))
            total += layer
            numerator = 3 * a * n * (n + 1) + 2 * b * n * (n + 1) * (n - 1)
            check(numerator % 6 == 0, section, ("integrality", a, b, n))
            check(total == numerator // 6, section, ("pair-volume", a, b, n))
            volumes.append(total)
            if a == b == 1:
                check(
                    6 * total == n * (n + 1) * (2 * n + 1),
                    section, ("squares", n),
                )
        first = differences(volumes)
        second = differences(first)
        third = differences(second)
        fourth = differences(third)
        check(all(value == 2 * b for value in third), section, ("cubic-leading", a, b))
        check(all(value == 0 for value in fourth), section, ("degree-bound", a, b))
        if b == 0:
            check(all(value == a for value in second), section, ("quadratic-leading", a))
        if a == b == 0:
            check(all(value == 0 for value in volumes), section, "zero-family")


def local_ratio_counterexample():
    section = "LOCAL_RATIO"
    previous = 0
    for n in range(1, 257):
        volume = n ** 3 + (-1) ** n * n ** 2 + n
        shell = volume - previous
        expected_shell = n * n - n + 1 if n % 2 else 5 * n * n - 5 * n + 3
        check(volume > 0 and shell > 0, section, ("positive-increasing", n))
        check(shell == expected_shell, section, ("shell", n))
        check(
            Fraction(volume, n ** 3) == 1 + Fraction((-1) ** n, n) + Fraction(1, n * n),
            section, ("relative-error", n),
        )
        ratio = Fraction(n * shell, volume)
        if n % 2:
            check(ratio == 1, section, ("odd-ratio", n))
        else:
            error = Fraction(10 * n + 2, n * n + n + 1)
            check(ratio == 5 - error, section, ("even-ratio", n))
            check(0 < error <= Fraction(12, n), section, ("even-error-bound", n))
        previous = volume


def hex_norm(point):
    x, y = point
    return max(abs(x), abs(y), abs(x - y))


def fiber_image(point):
    x, y = point
    return ((3 * x + 3 * y) % 5, (3 * y) % 5)


def lattice_image(a, b):
    return tuple(a * x + b * y for x, y in zip(T1, T2))


def balls(steps, maximum, modulus=None):
    reached = {(0, 0)}
    result = [set(reached)]
    for _ in range(maximum):
        extended = set(reached)
        for x, y in reached:
            for dx, dy in steps:
                point = (x + dx, y + dy)
                if modulus is not None:
                    point = tuple(value % modulus for value in point)
                extended.add(point)
        reached = extended
        result.append(set(reached))
    return result


def hexagons_and_reduction():
    section = "HEX_BALLS"
    infinite = balls(STEPS, 16)
    finite = balls(FIBER_STEPS, 16, 5)
    total_infinite = 0
    total_finite = 0
    for n, (cover, quotient) in enumerate(zip(infinite, finite)):
        norm_ball = {
            (x, y) for x in range(-n, n + 1) for y in range(-n, n + 1)
            if hex_norm((x, y)) <= n
        }
        check(cover == norm_ball, section, ("BFS-versus-norm", n))
        check(len(cover) == 3 * n * (n + 1) + 1, section, ("hex-cardinality", n))
        check(
            len(cover) == sum(2 * n + 1 - abs(x) for x in range(-n, n + 1)),
            section, ("row-count", n),
        )
        check(
            len(cover) == (2 * n + 1) ** 2 - n * (n + 1),
            section, ("deleted-triangles", n),
        )
        if n:
            check(len(cover - infinite[n - 1]) == 6 * n, section, ("hex-shell", n))
        expected_finite = (1, 7, 19)[n] if n < 3 else 25
        check(len(quotient) == expected_finite, section, ("quotient-size", n))
        check({fiber_image(point) for point in cover} == quotient, section, ("ball-image", n))
        if n <= 2:
            check(len(cover) == len(quotient), section, ("pre-wrap-injective", n))
        if n >= 3:
            check(quotient == set(product(range(5), repeat=2)), section, ("saturation", n))
        total_infinite += len(cover)
        total_finite += len(quotient)
        check(total_infinite == (n + 1) ** 3, section, ("cubic-accumulation", n))
        if n >= 2:
            check(total_finite == 25 * n - 23, section, ("linear-accumulation", n))
        if n >= 4:
            check(len(quotient) - len(finite[n - 1]) == 0, section, ("zero-late-shell", n))
    check(tuple(len(finite[n] - finite[n - 1]) for n in range(1, 4)) == (6, 12, 6),
          section, "finite-distance-histogram")
    check(sum(map(len, finite[:3])) == 27, section, "apparent-cubic-prefix")
    check(sum(map(len, finite[:4])) == 52 != 64, section, "first-cubic-break")

    section = "LIFT_REDUCTION"
    check(3 * 3 - 0 * 3 == 9 and 9 % 5 == 4, section, "finite-basis-determinant")
    check(T3 == tuple(x + y for x, y in zip(T1, T2)), section, "third-commutator-sum")
    check(T1[4] * T2[5] - T1[5] * T2[4] == 4, section, "integer-rank-minor")
    check(len({fiber_image(point) for point in product(range(5), repeat=2)}) == 25,
          section, "basis-surjectivity")
    for a, b in product(range(-8, 9), repeat=2):
        image = fiber_image((a, b))
        recovered = ((2 * image[0] - 2 * image[1]) % 5, (2 * image[1]) % 5)
        check(recovered == (a % 5, b % 5), section, ("finite-inverse", a, b))
        integer = lattice_image(a, b)
        check(integer[4] == -2 * (a + b) and integer[5] == -2 * b,
              section, ("integer-coefficients", a, b))
        check(tuple(value % 5 for value in integer[:4]) == (0, 0, 0, 0),
              section, ("piston-kernel", a, b))
        check(tuple(value % 5 for value in integer[4:]) == image,
              section, ("literal-lift-reduction", a, b))
        check(all(value % 5 == 0 for value in integer) == (a % 5 == b % 5 == 0),
              section, ("kernel-5L", a, b))


def native(letter, point, modulus=None):
    p1, p4, p1p, p4p, q, r = point
    if letter == "a":
        result = (p4, p1, p4p, p1p, q, r)
    elif letter == "b":
        result = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif letter == "c":
        result = (-p1p + 2, -p4p + 1 + r, -p1 + 2, -p4 + 1 - r, 1 - q, -r)
    elif letter == "d":
        result = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    elif letter == "e":
        result = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    else:
        raise ValueError(letter)
    if modulus is not None:
        return tuple(value % modulus for value in result)
    return result


def commutator(g, h, point, modulus=None):
    # [g,h]=g o h o g^-1 o h^-1, with involutive generators.
    for letter in (h, g, h, g):
        point = native(letter, point, modulus)
    return point


def translated(point, vector):
    return tuple(x + y for x, y in zip(point, vector))


def silent_displacement(r):
    return (-1 - r, 1 + r, -1 + r, 1 - r, 0, 0)


def native_and_integer_maps():
    section = "NATIVE_AFFINE"
    for point in product(range(5), repeat=6):
        for letter in LETTERS:
            for modulus in (None, 5):
                check(native(letter, native(letter, point, modulus), modulus) == point,
                      section, ("involution", letter, modulus, point))
        for g, h, vector in PAIR_TRANSLATIONS:
            integer_expected = translated(point, vector)
            check(commutator(g, h, point) == integer_expected,
                  section, ("integer-fired", g, h, point))
            check(commutator(g, h, point, 5) == tuple(x % 5 for x in integer_expected),
                  section, ("finite-fired", g, h, point))
        silent_expected = translated(point, silent_displacement(point[5]))
        check(commutator("a", "c", point) == silent_expected,
              section, ("integer-silent", point))
        check(commutator("a", "c", point, 5) == tuple(x % 5 for x in silent_expected),
              section, ("finite-silent", point))

    section = "NORMAL_LATTICE"
    affine_basis = [(0,) * 6] + [tuple(int(i == j) for i in range(6)) for j in range(6)]
    for a, b in product(range(-8, 9), repeat=2):
        vector = lattice_image(a, b)
        negative = tuple(-value for value in vector)
        for letter in ("b", "d", "e"):
            for point in affine_basis:
                conjugated = native(letter, translated(native(letter, point), vector))
                check(conjugated == translated(point, negative),
                      section, ("conjugation-negates", a, b, letter, point))


def silent_orbits():
    section = "SILENT_ORBITS"
    for r in range(-3, 4):
        start = (0, 0, 0, 0, 0, r)
        displacement = silent_displacement(r)
        check(any(displacement), section, ("nonzero-integer", r))
        check(any(value % 5 for value in displacement), section, ("nonzero-mod5", r))
        integer_state = start
        finite_state = tuple(value % 5 for value in start)
        integer_ball = {start}
        finite_ball = {finite_state}
        total_integer = 0
        total_finite = 0
        for n in range(9):
            expected_iterate = translated(start, tuple(n * value for value in displacement))
            check(integer_state == expected_iterate, section, ("integer-iterate", r, n))
            check(finite_state == tuple(value % 5 for value in expected_iterate),
                  section, ("finite-iterate", r, n))
            expected_ball = {
                translated(start, tuple(j * value for value in displacement))
                for j in range(-n, n + 1)
            }
            check(integer_ball == expected_ball, section, ("integer-orbit-ball", r, n))
            check(finite_ball == {tuple(value % 5 for value in point) for point in expected_ball},
                  section, ("finite-orbit-ball", r, n))
            check(len(integer_ball) == 2 * n + 1, section, ("linear-orbit", r, n))
            check(len(finite_ball) == min(2 * n + 1, 5), section, ("finite-orbit", r, n))
            total_integer += len(integer_ball)
            total_finite += len(finite_ball)
            check(total_integer == (n + 1) ** 2, section, ("quadratic-accumulation", r, n))
            check(total_finite == (1 if n == 0 else 5 * n - 1),
                  section, ("linear-finite-accumulation", r, n))
            if n < 8:
                integer_state = commutator("a", "c", integer_state)
                finite_state = commutator("a", "c", finite_state, 5)
                integer_ball |= {
                    commutator(g, h, point)
                    for point in integer_ball for g, h in (("a", "c"), ("c", "a"))
                }
                finite_ball |= {
                    commutator(g, h, point, 5)
                    for point in finite_ball for g, h in (("a", "c"), ("c", "a"))
                }


def main():
    accumulation()
    local_ratio_counterexample()
    hexagons_and_reduction()
    native_and_integer_maps()
    silent_orbits()
    print(NAME)
    for section, count in COUNTS.items():
        print("PASS {} checks={}".format(section, count))
    print("PASS ALL checks={}".format(sum(COUNTS.values())))
    print("SCOPE L1 exact finite audit of written proofs; physical dimension not selected")


if __name__ == "__main__":
    main()
