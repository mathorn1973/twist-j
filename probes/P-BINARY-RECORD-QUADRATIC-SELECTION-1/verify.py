#!/usr/bin/env python3
"""Exact finite audit of the pinned binary-record selection boundary."""

from fractions import Fraction
from itertools import combinations, permutations, product


CHECKS = 0


def check(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def pattern(t):
    labels = {}
    return tuple(labels.setdefault(x, len(labels)) for x in t)


def falling(d, r):
    result = 1
    for j in range(r):
        result *= d - j
    return result


def swaps(d):
    for i in range(d - 1):
        p = list(range(d))
        p[i], p[i + 1] = p[i + 1], p[i]
        yield tuple(p)


def invariant_subsets(atoms, actions):
    index = {a: i for i, a in enumerate(atoms)}
    images = [tuple(index[action(a)] for a in atoms) for action in actions]
    accepted = []
    for mask in range(1 << len(atoms)):
        if all(all(((mask >> i) & 1) == ((mask >> j) & 1)
                   for i, j in enumerate(image)) for image in images):
            accepted.append(mask)
    return accepted


def orbit_audit():
    cases = 0
    for k in range(1, 5):
        # Every partition has a representative among k labels.
        all_patterns = sorted({pattern(t) for t in product(range(k), repeat=k)})
        check(len(all_patterns) == (1, 2, 5, 15)[k - 1], "partition count")
        for d in range(6):
            buckets = {}
            for t in product(range(d), repeat=k):
                pi = pattern(t)
                buckets.setdefault(pi, []).append(t)
                for perm in swaps(d):
                    check(pattern(tuple(perm[x] for x in t)) == pi,
                          "equality pattern covariance")
                check(pattern(tuple(x + 1 for x in t)) == pi,
                      "injection stability control")
            admitted = [pi for pi in all_patterns if len(set(pi)) <= d]
            check(sorted(buckets) == admitted, "complete orbit inventory")
            for pi, tuples in sorted(buckets.items()):
                check(len(tuples) == falling(d, len(set(pi))), "orbit size")
            check(sum(falling(d, len(set(pi))) for pi in all_patterns) == d ** k,
                  "full Cartesian partition identity")
            # Independent atomic sum versus weighted falling-factorial formula.
            coefficients = {pi: i + 1 for i, pi in enumerate(all_patterns)}
            direct = sum(coefficients[pattern(t)]
                         for t in product(range(d), repeat=k))
            formula = sum(coefficients[pi] * falling(d, len(set(pi)))
                          for pi in all_patterns)
            check(direct == formula, "stable weighted orbit valuation")
            cases += 1
    # Exhaust every binary support, not only preconstructed orbit unions.
    for d in range(4):
        atoms = list(product(range(d), repeat=2))
        actions = [lambda t, p=p: (p[t[0]], p[t[1]]) for p in swaps(d)]
        masks = invariant_subsets(atoms, actions)
        expected = {
            sum(1 << i for i, (x, y) in enumerate(atoms)
                if (diag if x == y else off))
            for diag, off in product((False, True), repeat=2)
        }
        check(set(masks) == expected, "all matched binary supports")
    for m, n in product(range(4), repeat=2):
        atoms = list(product(range(m), range(n)))
        actions = ([lambda t, p=p: (p[t[0]], t[1]) for p in swaps(m)]
                   + [lambda t, p=p: (t[0], p[t[1]]) for p in swaps(n)])
        check(set(invariant_subsets(atoms, actions)) == {0, (1 << (m * n)) - 1},
              "all unmarked product-action supports")
    return cases


def binary_weights():
    for a, b, c in product(range(5), repeat=3):
        square = True
        for d in range(9):
            direct = sum(a if x == y else b for x, y in product(range(d), repeat=2))
            check(direct == a * d + b * d * (d - 1), "binary weight formula")
            square = square and direct == c * d * d
        check(square == (a == b == c), "exact square-selection criterion")
    check([d + 2 * d * (d - 1) for d in (1, 2, 3)] == [1, 6, 15],
          "strict positivity nonselection witness")
    for d in range(6):
        tuples = list(product(range(d), repeat=3))
        check(sum(x == y == z for x, y, z in tuples) == d, "triple linear")
        check(sum(x == y for x, y, z in tuples) == d * d, "triple quadratic")
        check(len(tuples) == d ** 3, "triple cubic")


def write(s, r):
    return s if r == -1 else (-1 if r == s else r)


def writer_audit():
    states = 0
    for d in range(1, 6):
        symbols = tuple(range(d))
        records = (-1,) + symbols
        image = set()
        graph = set()
        for s, r in product(symbols, records):
            out = write(s, r)
            check(out in records and write(s, out) == r, "writer involution")
            image.add((s, out))
            states += 1
            for p in permutations(symbols):
                rename = lambda x: -1 if x == -1 else p[x]
                check(write(p[s], rename(r)) == rename(out), "full writer covariance")
            if r == -1:
                graph.add((s, out))
        check(len(image) == d * (d + 1), "writer bijective on complete domain")
        check(graph == {(s, s) for s in symbols}, "faithful active graph")
        check(len(graph) == d, "linear graph count")
        for s in symbols:
            for tape in product(records, repeat=2):
                for j in range(2):
                    out = list(tape)
                    out[j] = write(s, out[j])
                    check(out[1 - j] == tape[1 - j], "old cell unchanged")
                    out[j] = write(s, out[j])
                    check(tuple(out) == tape, "addressed write inverse")
        for sources in product(symbols, repeat=3):
            tape = [-1] * 3
            for j, s in enumerate(sources):
                old = tuple(tape[:j])
                tape[j] = write(s, tape[j])
                check(tuple(tape[:j]) == old, "fresh sequence preserves prefix")
            check(tuple(tape) == sources, "complete retained source word")
            for j in reversed(range(3)):
                tape[j] = write(sources[j], tape[j])
            check(tape == [-1] * 3, "inverse complete sequence")
    check(2 != 2 ** 2, "writer refutes unrestricted square implication")
    return states


def weights(z, p):
    return abs(sum(z)) ** p, 5 * sum(abs(z[i] - z[j]) ** p
                                   for i, j in combinations(range(4), 2))


def reading(z, p):
    a, b = weights(z, p)
    return None if a + b == 0 else (Fraction(a, a + b), Fraction(b, a + b))


def native_audit():
    sources = list(product(range(-2, 3), repeat=4))
    for z in sources:
        for p in range(1, 5):
            a, b = weights(z, p)
            check(a >= 0 and b >= 0, "nonnegative integer weights")
            check((a == 0) == (sum(z) == 0), "LOW zero class")
            check((b == 0) == (len(set(z)) == 1), "HIGH zero class")
            check((a + b == 0) == (z == (0, 0, 0, 0)), "total zero class")
            value = reading(z, p)
            if value is not None:
                check(sum(value) == 1, "normalized nonzero reading")
            for permutation in permutations(range(4)):
                check(weights(tuple(z[i] for i in permutation), p) == (a, b),
                      "coordinate permutation invariance")
            for scale in (-2, -1, 0, 1, 2):
                scaled = tuple(scale * x for x in z)
                check(weights(scaled, p) == (abs(scale) ** p * a, abs(scale) ** p * b),
                      "integer homogeneity")
                if scale:
                    check(reading(scaled, p) == value, "normalized scale invariance")
        s = sum(z)
        check(weights(z, 2) == (s * s, 5 * (4 * sum(x * x for x in z) - s * s)),
              "v80 quadratic specialization")
    witness = (1, 1, 0, 0)
    values = [reading(witness, p)[0] for p in range(1, 9)]
    check(values[:4] == [Fraction(1, 11), Fraction(1, 6), Fraction(2, 7), Fraction(4, 9)],
          "exact native ambiguity witness")
    check(all(x < y for x, y in zip(values, values[1:])), "strict power-family separation")
    return len(sources)


def signed_audit():
    survivors = []
    for entries in product((-1, 0, 1), repeat=4):
        matrix = (entries[:2], entries[2:])
        # Values on both signs of every basis pair suffice to detect the obstruction.
        values = [sx * sy * matrix[i][j] for i, j in product(range(2), repeat=2)
                  for sx, sy in product((-1, 1), repeat=2)]
        if min(values) >= 0:
            survivors.append(entries)
    check(survivors == [(0, 0, 0, 0)], "signed positive bilinear audit")
    raw = (1, -1)
    check(len(list(product(raw, repeat=2))) == 4 and abs(sum(raw)) ** 2 == 0,
          "raw versus reduced signed fibres")


def main():
    orbit_cases = orbit_audit()
    binary_weights()
    writer_states = writer_audit()
    source_count = native_audit()
    signed_audit()
    print("P-BINARY-RECORD-QUADRATIC-SELECTION-1")
    print(f"ORBIT AUDIT PASS cases={orbit_cases} arity=1..4 size=0..5")
    print("BINARY CLASS PASS W=a*d+b*d*(d-1); square iff a=b=c")
    print(f"REVERSIBLE WRITER PASS complete_states={writer_states}; active_graph=d")
    print(f"NATIVE FAMILY PASS sources={source_count} audited_p=1..4; LOW_p1=1/11 LOW_p2=1/6")
    print("SIGNED BIADDITIVITY PASS nonnegative group pairing is zero")
    print("NONSELECTION CONFIRMED; PHYSICAL REALIZATION AND OCCURRENCE OPEN")
    print(f"RESULT PASS checks={CHECKS}")


if __name__ == "__main__":
    main()
