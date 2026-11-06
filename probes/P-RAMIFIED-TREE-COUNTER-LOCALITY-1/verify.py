#!/usr/bin/env python3
"""Exact finite audit for P-RAMIFIED-TREE-COUNTER-LOCALITY-1.

Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.
Depths 1..6; no floating point, external input, or simulation of native U.
Universal assertions and transport hypotheses are proved in PROOF.md.
Scientific mismatches print their first exact witness and exit zero;
unexpected implementation errors remain nonzero STOP conditions.
"""

from collections import Counter, deque
from fractions import Fraction


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ROOT = (0, 1, 0, 0)
J = (1, 0, 1, 0)
J_INV = (0, -1, -1, 0)
BETA = (1, -1, 0, 0)
MAX_DEPTH = 6
BASIS = tuple(tuple(int(i == r) for i in range(4)) for r in range(4))
IDENTITY = tuple(tuple(int(i == r) for r in range(4)) for i in range(4))


class Falsified(Exception):
    """A deterministic scientific counterexample, not a runtime failure."""


def check(condition, label, witness):
    if not condition:
        raise Falsified(f"{label}: {witness!r}")


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(c, x):
    return tuple(c * a for a in x)


def mul(x, y):
    """Independent polynomial convolution modulo 1+j+j^2+j^3+j^4."""
    z = [0] * 7
    for i, a in enumerate(x):
        for r, b in enumerate(y):
            z[i + r] += a * b
    for degree in range(6, 3, -1):
        coefficient = z[degree]
        for r in range(4):
            z[degree - 4 + r] -= coefficient
        z[degree] = 0
    return tuple(z[:4])


def power(x, exponent):
    result = ONE
    for _ in range(exponent):
        result = mul(result, x)
    return result


def mat_mul(a, b):
    return tuple(tuple(sum(a[i][t] * b[t][r] for t in range(4))
                       for r in range(4)) for i in range(4))


def mat_vec(a, x):
    return tuple(sum(a[i][r] * x[r] for r in range(4)) for i in range(4))


def inverse_and_det(matrix):
    """Rational Gaussian elimination; independent of digit division."""
    rows = [[Fraction(x) for x in matrix[i] + IDENTITY[i]] for i in range(4)]
    determinant = Fraction(1)
    for column in range(4):
        pivot = next(i for i in range(column, 4) if rows[i][column])
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            determinant = -determinant
        value = rows[column][column]
        determinant *= value
        rows[column] = [x / value for x in rows[column]]
        for i in range(4):
            if i != column:
                factor = rows[i][column]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[column])]
    return tuple(tuple(row[4:]) for row in rows), determinant


def divide_beta(x):
    """Exact quotient after a residue digit has been removed."""
    a, b, c, d = x
    check(sum(x) % 5 == 0, "division-domain", x)
    t = (a + b + c + d) // 5
    return (a - t, a + b - 2 * t, a + b + c - 3 * t, t)


def residue_id(x, depth):
    """Low beta digits as an integer ID, not as a ring element."""
    result, place = 0, 1
    for _ in range(depth):
        digit = sum(x) % 5
        result += digit * place
        place *= 5
        x = divide_beta(sub(x, scale(digit, ONE)))
    return result


def prefix_depth(left, right, depth):
    common = 0
    while common < depth and left % 5 == right % 5:
        common += 1
        left //= 5
        right //= 5
    return common


def cycle_lengths(permutation):
    seen, lengths = set(), []
    for start in range(len(permutation)):
        if start in seen:
            continue
        current, length = start, 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        check(current == start, "cycle-closing", (start, current))
        lengths.append(length)
    return lengths


def main():
    print("P-RAMIFIED-TREE-COUNTER-LOCALITY-1 exact audit")
    print("route: polynomial ring; beta digits; independent rational lattice inverse")
    check(mul(J, J_INV) == ONE, "J inverse", mul(J, J_INV))
    check(power(BETA, 4) == scale(5, power(J, 2)), "ramification", power(BETA, 4))
    check(power(sub(J, ONE), 3) == ROOT, "Z[J]=O generator", power(sub(J, ONE), 3))
    columns = tuple(mul(BETA, e) for e in BASIS)
    matrix = tuple(tuple(columns[r][i] for r in range(4)) for i in range(4))
    inverse, determinant = inverse_and_det(matrix)
    check(determinant == 5, "beta determinant", determinant)
    check(all((5 * x).denominator == 1 for row in inverse for x in row),
          "integral adjugate", inverse)
    adjugate = tuple(tuple(int(5 * x) for x in row) for row in inverse)
    check(mat_mul(matrix, adjugate) == tuple(tuple(5 * x for x in row)
                                           for row in IDENTITY), "adjugate", adjugate)
    adj_powers = [IDENTITY]
    for _ in range(MAX_DEPTH):
        adj_powers.append(mat_mul(adj_powers[-1], adjugate))

    def in_ideal(x, depth):
        return all(c % (5 ** depth) == 0 for c in mat_vec(adj_powers[depth], x))

    def valuation(x, depth):
        return next((r - 1 for r in range(1, depth + 1) if not in_ideal(x, r)), depth)

    print("identities: J*Jinv=1; beta^4=5*J^2; (J-1)^3=j; det(beta)=5 PASS")
    print("depth nodes counter_orbit counter_cycles affine_orbit A_distance")
    previous_maps = {name: [0] for name in ("A", "Ai", "M", "Mi")}
    representatives = [ZERO]
    beta_power = ONE
    cut_rows = []
    for depth in range(1, MAX_DEPTH + 1):
        parents = len(representatives)
        representatives = [add(x, scale(d, beta_power))
                           for d in range(5) for x in representatives]
        beta_power = mul(beta_power, BETA)
        size = 5 ** depth
        check(len(set(representatives)) == size, "distinct representatives", depth)
        check(Counter(i % parents for i in range(size)) ==
              Counter({i: 5 for i in range(parents)}), "five children", depth)
        maps = {name: [] for name in previous_maps}
        for index, x in enumerate(representatives):
            check(residue_id(x, depth) == index, "digit round trip", (depth, index, x))
            check(valuation(x, depth) == prefix_depth(index, 0, depth),
                  "valuation-prefix", (depth, index, x))
            transformed = {"A": add(x, ONE), "Ai": sub(x, ONE),
                           "M": mul(J, x), "Mi": mul(J_INV, x)}
            for name, y in transformed.items():
                target = residue_id(y, depth)
                maps[name].append(target)
                check(in_ideal(sub(y, representatives[target]), depth),
                      "independent lattice congruence", (depth, name, index, target, y))
                check(target % parents == previous_maps[name][index % parents],
                      "parent coherence", (depth, name, index, target))
                if name in ("A", "M"):
                    difference = sub(representatives[target], x)
                    common = prefix_depth(index, target, depth)
                    check(common == valuation(difference, depth),
                          "independent metric", (depth, name, index, target))
                    expected = 0 if name == "A" else valuation(x, depth)
                    check(common == expected, "displacement", (depth, name, index, common))
        for name, permutation in maps.items():
            check(len(set(permutation)) == size, "permutation", (depth, name))
        for forward, backward in (("A", "Ai"), ("M", "Mi")):
            check(all(maps[backward][maps[forward][i]] == i for i in range(size)),
                  "inverse permutations", (depth, forward, backward))
        length = 5 ** ((depth + 3) // 4)
        lengths = cycle_lengths(maps["A"])
        check(Counter(lengths) == Counter({length: size // length}),
              "counter cycle census", (depth, Counter(lengths)))
        natural = {residue_id(scale(n, ONE), depth) for n in range(length)}
        orbit, current = set(), 0
        for _ in range(length):
            orbit.add(current)
            current = maps["A"][current]
        check(current == 0 and orbit == natural and len(natural) == length,
              "natural counter orbit", (depth, current, len(orbit), len(natural)))
        check(size == len(natural) * 5 ** ((3 * depth) // 4),
              "natural orbit fraction", (depth, size, len(natural)))
        check(all(in_ideal(scale(n, ONE), depth) == (n % length == 0)
                  for n in range(length + 1)), "integer ideal intersection", depth)
        reached, queue = {0}, deque([0])
        while queue:
            source = queue.popleft()
            for name in ("A", "Ai", "M", "Mi"):
                target = maps[name][source]
                if target not in reached:
                    reached.add(target)
                    queue.append(target)
        check(len(reached) == size, "affine transitivity", (depth, len(reached)))
        leaves = 5 ** (depth - 1)
        for digit in range(5):
            outgoing = sum(i % 5 == digit and maps["A"][i] % 5 != digit
                           for i in range(size))
            check(outgoing == leaves, "A cut demand", (depth, digit, outgoing))
        outgoing_j = sum(i % 5 == 1 and maps["M"][i] % 5 != 1 for i in range(size))
        check(outgoing_j == leaves, "J cut demand", (depth, outgoing_j))
        for radius in range(1, min(3, depth) + 1):
            boundary = [(level, i) for level in range(1, radius + 1)
                        for i in range(5 ** level) if i % 5 == 0]
            bound = (5 ** radius - 1) // 4
            check(len(boundary) == bound, "inside cut boundary", (depth, radius, boundary))
            latency = (leaves + bound - 1) // bound
            check(bound * latency >= leaves > bound * (latency - 1),
                  "q=Q=5 cut lower bound", (depth, radius, leaves, bound, latency))
            cut_rows.append((depth, radius, leaves, bound, latency))
        print(depth, size, length, len(lengths), len(reached), 2 * depth)
        previous_maps = maps
    print("cut audit: q=Q=5; all A first-digit cuts and J first-digit-1 cut PASS")
    print("depth radius outgoing_leaves inside_boundary latency_lower_bound")
    for row in cut_rows:
        print(*row)
    print("scope: finite audit only; all-depth locality and information bounds use PROOF.md")
    print("scope: fixed tree, independent payload, bounded total cell alphabet; no native-U realization")
    print("ROUTE RAMIFIED-TREE-TRANSPORT-BOUNDARY (finite audit; independent proof review required)")
    print("VERDICT PASS")


if __name__ == "__main__":
    try:
        main()
    except Falsified as error:
        print(f"FALSIFIER {error}")
        print("ROUTE FALSIFIED")
        print("VERDICT FALSIFIED")
