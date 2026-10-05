"""Supplemental exact audit of independently proved inline L1 theorems.

Calculations originated as exploratory candidate-C work, not a formal probe.
No preregistration, retrospective preregistration, or native realization.
Standard library only; deterministic LF stdout; no writes or network access.
"""

from collections import Counter
from itertools import product
import sys

P = 5
POINTS = tuple(product(range(P), repeat=3))
ZERO = (0, 0, 0)
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
L5_W = ((3, 3, 2), (3, 4, 2), (3, 2, 0))
B_W_FROM_GRAM = ((1, 4, 2), (4, 0, 1), (3, 4, 4))
M_GRAM = ((0, 3, 0), (4, 4, 4), (0, 3, 3))
LAMBDA_W = ((1, 1, 2),)
CLASSES = ("Z", "R1+", "R1-", "R2+", "R2-")
EXPECTED_COUNTS = {
    (1, 1): (1, 2, 0, 0, 0),
    (1, 2): (1, 0, 2, 0, 0),
    (2, 1): (49, 4, 4, 8, 0),
    (2, 2): (1, 6, 6, 0, 12),
    (3, 1): (145, 270, 20, 120, 120),
    (3, 2): (145, 20, 270, 120, 120),
    (4, 1): (6625, 3000, 3000, 3600, 2400),
    (4, 2): (625, 3250, 3250, 2600, 3900),
    (5, 1): (78625, 94250, 63000, 78000, 78000),
    (5, 2): (78625, 63000, 94250, 78000, 78000),
    (6, 1): (2340625, 1937500, 1937500, 2015000, 1860000),
    (6, 2): (1590625, 1968750, 1968750, 1890000, 2047500),
}
EXPECTED_REACHABLE = {
    (3, 1): 353515625, (3, 2): 353515625,
    (4, 1): 281640625, (4, 2): 284765625,
    (5, 1): 264140625, (5, 2): 264140625,
    (6, 1): 251890625, (6, 2): 252015625,
}
EXPECTED_ORBITS = {
    (0, 0, 0): (1, (1, 0, 0, 0, 0)),
    (1, 3, 4): (2, (0, 2, 0, 0, 0)),
    (2, 1, 3): (2, (0, 0, 2, 0, 0)),
    **{g: (10, (0, 0, 0, 10, 0)) for g in ((0, 1, 1), (0, 2, 2))},
    **{g: (10, (0, 2, 0, 4, 4)) for g in
       ((0, 0, 1), (0, 1, 0), (0, 2, 1), (1, 1, 1), (1, 3, 0))},
    **{g: (10, (0, 0, 2, 4, 4)) for g in
       ((0, 0, 2), (0, 1, 3), (0, 1, 4), (1, 1, 0), (1, 1, 4))},
}


def mm(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) % P
                       for col in zip(*b)) for row in a)


def mv(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) % P for row in a)


def rank(a):
    a = [list(row) for row in a]
    pivot = 0
    for col in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][col] % P), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        scale = pow(a[pivot][col] % P, -1, P)
        a[pivot] = [(x * scale) % P for x in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                scale = a[i][col]
                a[i] = [(x - scale * y) % P for x, y in zip(a[i], a[pivot])]
        pivot += 1
    return pivot


def chi(t):
    return 0 if t % P == 0 else (1 if t % P in (1, 4) else -1)


def gram_type(g):
    a, b, c = g
    det = (a * c - b * b) % P
    if det:
        return "R2+" if chi(det) == 1 else "R2-"
    if g == ZERO:
        return "Z"
    return "R1+" if chi(a or c) == 1 else "R1-"


def norm_count(s, t, epsilon):
    assert s >= 0
    if s == 0:
        return int(t % P == 0)
    if s % 2:
        return P ** (s - 1) + epsilon * chi(t) * P ** ((s - 1) // 2)
    return P ** (s - 1) + epsilon * (4 if t % P == 0 else -1) * P ** (s // 2 - 1)


def closed_count(r, delta, g):
    a, b, c = g
    epsilon = chi(delta)
    if g == ZERO:
        n0 = norm_count(r, 0, epsilon)
        return n0 if n0 == 1 else n0 + (n0 - 1) * P * norm_count(r - 2, 0, epsilon)
    det = (a * c - b * b) % P
    if det == 0:
        t = a or c
        return norm_count(r, t, epsilon) * norm_count(r - 1, 0, epsilon * chi(t))
    return 0 if r == 1 else norm_count(r, 1, epsilon) * norm_count(r - 1, det, epsilon)


def convolution(r, delta):
    counts = Counter({ZERO: 1})
    for coefficient in [1] * (r - 1) + [delta]:
        one = Counter(((coefficient * x * x) % P,
                       (coefficient * x * y) % P,
                       (coefficient * y * y) % P)
                      for x, y in product(range(P), repeat=2))
        following = Counter()
        for u, nu in counts.items():
            for v, nv in one.items():
                following[tuple((x + y) % P for x, y in zip(u, v))] += nu * nv
        counts = following
    return counts


def orbits():
    seen, result = set(), []
    for start in POINTS:
        if start in seen:
            continue
        orbit, g = [], start
        while g not in seen:
            seen.add(g)
            orbit.append(g)
            g = mv(M_GRAM, g)
        assert g == start
        result.append(orbit)
    return result


def required_memory(pairs):
    result = 1
    for source, target in pairs:
        if source and not target:
            return None
        if target:
            result = max(result, (source + target - 1) // target)
    return result


def verify_covariant_class():
    """Compare all coefficients; do not assume the symmetric-C ansatz."""
    monomials = tuple((i, j) for i in range(12) for j in range(i, 12))
    index = {m: i for i, m in enumerate(monomials)}
    width = len(monomials)
    assert width == 78
    source_generators = (((1, 1), (0, 1)), ((1, 0), (1, 1)))
    sl2_basis = (((1, 0), (0, 4)), ((0, 1), (0, 0)), ((0, 0), (1, 0)))
    equations = []
    for generator in source_generators:
        a, b = generator[0]
        c, d = generator[1]
        inverse = ((d, -b % P), (-c % P, a))
        target_columns = [mm(mm(generator, basis), inverse) for basis in sl2_basis]
        target = tuple(tuple(image[i][j] for image in target_columns)
                       for i, j in ((0, 0), (0, 1), (1, 0)))
        substitutions = [{6 * slot + coordinate: generator[row][slot] for slot in range(2)}
                         for row in range(2) for coordinate in range(6)]
        transformed = []
        for i, j in monomials:
            coefficients = [0] * width
            for u, cu in substitutions[i].items():
                for v, cv in substitutions[j].items():
                    k = index[tuple(sorted((u, v)))]
                    coefficients[k] = (coefficients[k] + cu * cv) % P
            transformed.append(coefficients)
        for component in range(3):
            for monomial in range(width):
                row = [0] * (3 * width)
                for source in range(width):
                    row[component * width + source] = transformed[source][monomial]
                for target_component in range(3):
                    k = target_component * width + monomial
                    row[k] = (row[k] - target[component][target_component]) % P
                equations.append(row)
    explicit_basis = []
    for first in range(6):
        for second in range(first, 6):
            vector = [0] * (3 * width)
            for i, j in {(first, second), (second, first)}:
                vector[index[(i, 6 + j)]] -= 1
                vector[width + index[tuple(sorted((i, j)))]] += 1
                vector[2 * width + index[tuple(sorted((6 + i, 6 + j)))]] -= 1
            explicit_basis.append(tuple(value % P for value in vector))
    assert rank(equations) == 213
    assert rank(explicit_basis) == 21
    assert all(sum(x * y for x, y in zip(row, vector)) % P == 0
               for row in equations for vector in explicit_basis)


def main():
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    print("Supplemental exact audit: quadratic polynomial class and fixed L5 memory")
    print("Evidence: inline exact proofs; exploratory calculations, no formal probe")
    print(f"L5_W={L5_W}")
    print(f"B_W_FROM_GRAM={B_W_FROM_GRAM}")
    print(f"M_GRAM={M_GRAM}")
    verify_covariant_class()
    print("PASS: 234 quadratic coefficients, equation rank 213, explicit covariant dimension 21")
    assert rank(B_W_FROM_GRAM) == rank(M_GRAM) == 3
    assert mm(B_W_FROM_GRAM, M_GRAM) == mm(L5_W, B_W_FROM_GRAM)
    assert mm(LAMBDA_W, B_W_FROM_GRAM) == ((1, 2, 1),)
    assert mm(mm(LAMBDA_W, L5_W), B_W_FROM_GRAM) == ((3, 4, 1),)
    power = IDENTITY
    for _ in range(5):
        power = mm(power, M_GRAM)
    assert power == tuple(tuple(-x % P for x in row) for row in IDENTITY)
    nil = tuple(tuple((M_GRAM[i][j] + IDENTITY[i][j]) % P for j in range(3)) for i in range(3))
    assert rank(mm(nil, nil)) == 1 and rank(mm(mm(nil, nil), nil)) == 0
    for a, b, c in POINTS:
        u, v, w = mv(M_GRAM, (a, b, c))
        assert (u + v - w) % P == -(a + b - c) % P
        assert (u * w - v * v) % P == (a * c - b * b - (a + b - c) ** 2) % P
    print("PASS: marked conjugacy, scalar certificate, tau/Delta laws, M^5=-I")
    obs = orbits()
    found = {}
    for orbit in obs:
        histogram = Counter(map(gram_type, orbit))
        found[min(orbit)] = (len(orbit), tuple(histogram[k] for k in CLASSES))
    assert found == EXPECTED_ORBITS
    assert Counter(map(gram_type, POINTS)) == dict(zip(CLASSES, (1, 12, 12, 60, 40)))
    print("Orbit histogram order: Z R1+ R1- R2+ R2-")
    for representative, (length, histogram) in sorted(found.items()):
        print(f"orbit={representative} length={length} types={histogram}")
    for r in range(1, 7):
        for delta in (1, 2):
            counts = convolution(r, delta)
            assert all(counts[g] == closed_count(r, delta, g) for g in POINTS)
            assert sum(counts.values()) == P ** (2 * r)
            by_type = {}
            for g in POINTS:
                category = gram_type(g)
                assert by_type.setdefault(category, counts[g]) == counts[g]
            row = tuple(by_type[k] for k in CLASSES)
            assert row == EXPECTED_COUNTS[r, delta]
            diagonal = [1] * (r - 1) + [delta] + [0] * (6 - r)
            cmat = tuple(tuple(diagonal[i] if i == j else 0 for j in range(6)) for i in range(6))
            for small, expected_rank in ((((1, 1), (1, 1)), r), (((3, 2), (2, 1)), 2 * r)):
                tensor = tuple(tuple(small[i // 6][j // 6] * cmat[i % 6][j % 6] % P
                                     for j in range(12)) for i in range(12))
                assert rank(tensor) == expected_rank
            single = required_memory((counts[g], counts[mv(M_GRAM, g)]) for g in POINTS)
            forever = required_memory((max(counts[g] for g in o), min(counts[g] for g in o)) for o in obs)
            expected = None if r <= 2 else (6 if r == 3 else 2)
            assert single == forever == expected
            factor = P ** (12 - 2 * r)
            reachable = None if forever is None else factor * sum(len(o) * max(counts[g] for g in o) for o in obs)
            assert reachable == EXPECTED_REACHABLE.get((r, delta))
            if r == 3:
                source = (0, 4, 1) if delta == 1 else (0, 2, 3)
                target = (2, 0, 0) if delta == 1 else (1, 0, 0)
                assert mv(M_GRAM, source) == target and counts[source] == 6 * counts[target]
            cap = "infinite" if forever is None else str(forever)
            print(f"r={r} delta={delta} reduced={row} factor={factor} support={sum(bool(counts[g]) for g in POINTS)}")
            print(f"  memory_one_step={cap} memory_forever={cap} reachable_min={reachable}")
    print("PASS: all 1500 Gram fibers match independent convolution and formulas")
    print("PASS: all 12 rank/discriminant classes and exact capacities verified")
    print("PASS: all exact checks completed.")


if __name__ == "__main__":
    main()
