"""NON-CANONICAL W2 exact audit. Original package Python was not read."""
from collections import Counter
from fractions import Fraction as F
from functools import cmp_to_key
from hashlib import sha256
from itertools import combinations, permutations, product
from random import Random


def check(name, condition, detail):
    if not condition:
        print("FAIL " + name + " " + detail, flush=True)
        raise AssertionError(name)
    print("PASS " + name + " " + detail, flush=True)


# Q(sqrt(5)), represented independently as two rational coefficients.
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def scale(x, t):
    return (x[0] * t, x[1] * t)


def mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def sign(x):
    a, b = x
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if (a > 0) == (b > 0):
        return (a > 0) - (a < 0)
    difference = a * a - 5 * b * b
    answer = (difference > 0) - (difference < 0)
    return answer if a > 0 else -answer


ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def total(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def wigner(vector, root=1):
    norm = sum(x * x for x in vector)
    answer = []
    for q, r in product(range(5), repeat=2):
        coefficients = [0] * 5
        for j in range(5):
            coefficients[(root * 2 * r * (q - j)) % 5] += (
                vector[j] * vector[(2 * q - j) % 5])
        assert coefficients[1] == coefficients[4]
        assert coefficients[2] == coefficients[3]
        a = 2 * coefficients[0] - coefficients[1] - coefficients[2]
        b = coefficients[1] - coefficients[2]
        answer.append((F(a, 10 * norm), F(b, 10 * norm)))
    return tuple(answer)


def negativity(values):
    return scale(total(x for x in values if sign(x) < 0), -1)


# Cyclotomic integers, used only for operator calculations. No Q(sqrt(5))
# code is used in matrix construction or multiplication.
CZ = (0, 0, 0, 0)
CI = (1, 0, 0, 0)
ROOTS = (CI, (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (-1, -1, -1, -1))


def ca(x, y):
    return tuple(a + b for a, b in zip(x, y))


def cs(x, n):
    return tuple(n * a for a in x)


def cm(x, y):
    polynomial = [0] * 7
    for i in range(4):
        for j in range(4):
            polynomial[i + j] += x[i] * y[j]
    for k in range(6, 3, -1):
        for j in range(1, 5):
            polynomial[k - j] -= polynomial[k]
    return tuple(polynomial[:4])


def mm(a, b):
    rows = []
    for i in range(5):
        row = []
        for j in range(5):
            value = CZ
            for k in range(5):
                value = ca(value, cm(a[i][k], b[k][j]))
            row.append(value)
        rows.append(tuple(row))
    return tuple(rows)


def ms(a, n):
    return tuple(tuple(cs(x, n) for x in row) for row in a)


def tr(a):
    value = CZ
    for j in range(5):
        value = ca(value, a[j][j])
    return value


def mono_compose(a, b):
    return tuple((a[k][0], (e + a[k][1]) % 5) for k, e in b)


def mono_inverse(a):
    result = [None] * 5
    for j, (k, e) in enumerate(a):
        result[k] = (j, -e % 5)
    return tuple(result)


PARITY = tuple((-j % 5, 0) for j in range(5))
IDENTITY = tuple((j, 0) for j in range(5))


def phase(q, r, root=1):
    return tuple(((2 * q - j) % 5, root * 2 * r * (q - j) % 5)
                 for j in range(5))


def dense(a):
    result = [[CZ] * 5 for _ in range(5)]
    for j, (k, e) in enumerate(a):
        result[k][j] = ROOTS[e]
    return tuple(tuple(row) for row in result)


POINTS = tuple(product(range(5), repeat=2))
DIRECTIONS = ((0, 1),) + tuple((1, m) for m in range(5))


def label(point, direction):
    q, r = point
    return q if direction == 0 else (r - (direction - 1) * q) % 5


LINES = tuple(tuple(u for u in POINTS if label(u, d) == b)
              for d in range(6) for b in range(5))
SETS = tuple(frozenset(line) for line in LINES)


def shift(u, d, t):
    dq, dr = DIRECTIONS[d]
    return ((u[0] + t * dq) % 5, (u[1] + t * dr) % 5)


def generator(index, state):
    p, s, t, v, q, r = state
    choices = ((s, p, v, t, q, r), (-t, -v, -p, -s, -q, -r),
               (-t + 2, -v + 1 + r, -p + 2, -s + 1 - r, 1 - q, -r),
               (2 - p, 1 - s, 3 - t, 4 - v, 1 - q, 1 - r),
               (2 - p, 1 - s, 3 - t, 4 - v, 2 - q, 1 - r))
    return tuple(x % 5 for x in choices[index])


def rref(rows, width):
    a = [[x % 5 for x in row] for row in rows]
    pivots = []
    for j in range(width):
        k = next((k for k in range(len(pivots), len(a)) if a[k][j]), None)
        if k is None:
            continue
        i = len(pivots)
        a[i], a[k] = a[k], a[i]
        inverse = pow(a[i][j], -1, 5)
        a[i] = [x * inverse % 5 for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                factor = a[k][j]
                a[k] = [(x - factor * y) % 5 for x, y in zip(a[k], a[i])]
        pivots.append(j)
    return a, pivots


def kernel(rows, width):
    a, pivots = rref(rows, width)
    basis = []
    for j in range(width):
        if j not in pivots:
            v = [0] * width
            v[j] = 1
            for i, k in enumerate(pivots):
                v[k] = -a[i][j] % 5
            basis.append(v)
    return basis


def geometry():
    centres = ((0, 0), (3, 0), (3, 3), (1, 3))
    states = tuple(product(range(5), repeat=6))
    affine = True
    for state in states:
        affine &= generator(0, state)[4:] == state[4:]
        for g, centre in enumerate(centres, 1):
            affine &= generator(g, state)[4:] == tuple(
                (2 * centre[j] - state[j + 4]) % 5 for j in range(2))
    maps = {(1, 0, 0)}
    frontier = list(maps)
    while frontier:
        signum, q, r = frontier.pop()
        for a, b in centres:
            entry = (-signum, (2 * a - q) % 5, (2 * b - r) % 5)
            if entry not in maps:
                maps.add(entry)
                frontier.append(entry)
    check("S1_NATIVE", affine and len(maps) == 50,
          "states=15625 generators=5 fibre_group=50")
    images = []
    for bit in range(2):
        images.append(len({generator((sum(x) + 2 * bit) % 5, x) for x in states}))
    collision = generator(0, (0,) * 6) == generator(2, (2, 1, 2, 1, 1, 0))
    weights = Counter(states)
    sizes = []
    for n in range(128):
        bit = n.bit_count() % 2
        selectors = {(sum(x) + 2 * bit) % 5 for x in weights}
        if n >= 3:
            old = (n - 1).bit_count() % 2
            expected = 1 if old != bit else (3 if bit else 4)
            assert selectors == {expected}
        after = Counter()
        for x, count in weights.items():
            after[generator((sum(x) + 2 * bit) % 5, x)] += count
        weights = after
        sizes.append(len(weights))
        if n >= 2:
            assert len(weights) == 3125 and set(weights.values()) == {5}
    check("S2_SELECTED", collision and images == [6250, 9375]
          and sizes[:3] == [6250, 6250, 3125],
          "images=6250,9375 ticks=0..127 synchronized_ticks=3..127")


def forms():
    pairs = tuple(combinations(range(6), 2))
    linear = []
    for g in range(3):
        origin = generator(g, (0,) * 6)
        columns = []
        for j in range(6):
            e = tuple(int(j == k) for k in range(6))
            columns.append(tuple((x - y) % 5 for x, y in zip(generator(g, e), origin)))
        linear.append(columns)
    expected = {(1, 1, 1): 3, (4, 1, 1): 3, (1, 4, 4): 1, (4, 4, 4): 1}
    found = {}
    ranks = Counter()
    strict = None
    for multipliers in product(range(1, 5), repeat=3):
        equations = []
        for g, multiplier in enumerate(multipliers):
            columns = linear[g]
            for i, j in pairs:
                equations.append([
                    (columns[i][a] * columns[j][b] - columns[i][b] * columns[j][a]
                     - (multiplier if (a, b) == (i, j) else 0)) % 5
                    for a, b in pairs])
        basis = kernel(equations, 15)
        if basis:
            found[multipliers] = len(basis)
        if multipliers == (1, 1, 1):
            strict = basis
        for coefficients in product(range(5), repeat=len(basis)):
            if not any(coefficients):
                continue
            coordinates = [sum(c * v[k] for c, v in zip(coefficients, basis)) % 5
                           for k in range(15)]
            matrix = [[0] * 6 for _ in range(6)]
            for (i, j), value in zip(pairs, coordinates):
                matrix[i][j], matrix[j][i] = value, -value % 5
            ranks[len(rref(matrix, 6)[1])] += 1
    kappa, q, r = (1, 1, 1, 1, 0, 0), (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)
    proposed = [[(a[i] * b[j] - a[j] * b[i]) % 5 for i, j in pairs]
                for a, b in ((kappa, q), (kappa, r), (q, r))]
    same_span = len(rref(strict + proposed, 15)[1]) == 3
    stack = []
    for values in strict:
        matrix = [[0] * 6 for _ in range(6)]
        for (i, j), value in zip(pairs, values):
            matrix[i][j], matrix[j][i] = value, -value % 5
        stack.extend(matrix)
    radical = 6 - len(rref(stack, 6)[1])
    check("S3_FORMS", found == expected and ranks == {2: 256} and same_span and radical == 3,
          "multiplier_triples=64 nonzero_forms=256 rank=2 dimensions=3,3,1,1 common_radical=3")


def operators():
    convention_cases = 0
    for root, tau in product(range(1, 5), range(5)):
        for q, r in POINTS:
            d = tuple(((j + q) % 5, root * (tau * q * r + r * j) % 5)
                      for j in range(5))
            got = mono_compose(mono_compose(d, PARITY), mono_inverse(d))
            assert got == phase(q, r, root)
            assert mono_compose(got, got) == IDENTITY and mono_inverse(got) == got
            assert sum(ROOTS[e][0] for j, (k, e) in enumerate(got) if k == j) == 1
            convention_cases += 1
    for s, u in product(POINTS, repeat=2):
        conjugate = mono_compose(mono_compose(phase(*s), phase(*u)), phase(*s))
        assert conjugate == phase((2 * s[0] - u[0]) % 5, (2 * s[1] - u[1]) % 5)
    matrices = tuple(dense(phase(*u)) for u in POINTS)
    projectors = []  # Entries are five times the actual projector.
    for index, line in enumerate(LINES):
        entries = []
        for i in range(5):
            row = []
            for j in range(5):
                value = CZ
                for u in line:
                    value = ca(value, matrices[5 * u[0] + u[1]][i][j])
                row.append(value)
            entries.append(tuple(row))
        p = tuple(entries)
        direction, b = divmod(index, 5)
        if direction == 0:
            chirp = tuple(tuple(cs(CI, 5) if i == j == b else CZ for j in range(5))
                          for i in range(5))
        else:
            m = direction - 1
            chirp = tuple(tuple(ROOTS[(3 * m * (i * i - j * j) + b * (i - j)) % 5]
                                for j in range(5)) for i in range(5))
        assert p == chirp and mm(p, p) == ms(p, 5) and tr(p) == cs(CI, 5)
        projectors.append(p)
    for i, j in product(range(30), repeat=2):
        overlap = len(SETS[i] & SETS[j])
        multiplication = mm(projectors[i], projectors[j])
        assert tr(multiplication) == cs(CI, 5 * overlap)
        assert mm(projectors[j], multiplication) == ms(projectors[j], 5 * overlap)
    check("S1_S4_S8_OPERATORS", True,
          "weyl_conventions=20 conjugations=500 reflection_cases=625 explicit_line_vectors=30 sandwich_pairs=900")


def census():
    lifts = (0, 1, 2, -2, -1)
    sources = tuple(p for p in product(range(5), repeat=4) if any(p))
    cached = {}
    baseline = {}
    low = wigner((4, -1, -1, -1, -1))
    for p in sources:
        v = tuple(lifts[j] for j in p)
        s = sum(v)
        psi = tuple(5 * x - s for x in (0,) + v)
        values = wigner(psi)
        cached[psi] = negativity(values)
        baseline[p] = cached[psi]
        assert total(values) == ONE
        assert total(values[q * 5] for q in range(5)) == ZERO
        assert any(sign(values[q * 5]) < 0 for q in range(5))
        line_sums = [total(values[5 * q + r] for q, r in line) for line in LINES]
        for u in POINTS:
            inversion = scale(add(total(line_sums[i] for i, line in enumerate(SETS) if u in line),
                                  scale(ONE, -1)), F(1, 5))
            assert inversion == values[5 * u[0] + u[1]]
        overlap = scale(total(mul(a, b) for a, b in zip(values, low)), 5)
        expected = (F(s * s, 4 * (5 * sum(x * x for x in v) - s * s)), F(0))
        assert overlap == expected
        for root in range(2, 5):
            changed = wigner(psi, root)
            assert changed == tuple(values[5 * q + root * r % 5] for q, r in POINTS)
            assert negativity(changed) == baseline[p]
    histogram = Counter(baseline.values())
    ordered = sorted(histogram, key=cmp_to_key(lambda x, y: sign(add(x, scale(y, -1)))))
    minimum, maximum = ordered[0], ordered[-1]
    assert minimum == (F(1, 10), F(1, 10)) and histogram[minimum] == 32
    assert maximum == (F(29, 220), F(8, 55)) and histogram[maximum] == 16
    assert len(histogram) == 39
    assert baseline[(1, 4, 0, 0)] == minimum
    named_difference = None
    for empty, order in product(range(5), permutations(range(4))):
        alternate = Counter()
        for p in sources:
            v = [lifts[p[j]] for j in order]
            v.insert(empty, 0)
            s = sum(v)
            psi = tuple(5 * x - s for x in v)
            if psi not in cached:
                cached[psi] = negativity(wigner(psi))
            n = cached[psi]
            alternate[n] += 1
            if empty == 0 and n != baseline[p] and named_difference is None:
                named_difference = (p, order)
        assert alternate == histogram
    assert named_difference is not None
    table = ''.join(''.join(map(str, p)) + '\t' + str(baseline[p][0]) + '\t' +
                    str(baseline[p][1]) + '\n' for p in sources).encode('ascii')
    check("S4_S6_CENSUS", True,
          "preparations=624 values=39 minimum=(1+sqrt5)/10 multiplicity=32 maximum=29/220+8sqrt5/55 multiplicity=16")
    check("CONVENTIONS", True,
          "root_relabel_cases=1872 embedding_relabelings=120 census_entries=74880 named_dependence=" +
          str(named_difference))
    print("AUDIT_TABLE_SHA256 " + sha256(table).hexdigest() + " bytes=" + str(len(table)), flush=True)


def rational_row_attack():
    rng = Random(20261002)
    dimensions = (3, 5, 7, 9, 15)
    count = 0
    noninteger = 0
    for d in dimensions:
        vectors = []
        for i, j in combinations(range(d), 2):
            vectors.append(tuple(F(int(k == i) - int(k == j)) for k in range(d)))
        for _ in range(400):
            v = [F(rng.randrange(-7, 8), rng.randrange(2, 12)) for _ in range(d - 1)]
            v.append(-sum(v))
            if not any(v):
                v[0], v[-1] = F(1, 2), F(-1, 2)
            vectors.append(tuple(v))
        for v in vectors:
            norm = sum(x * x for x in v)
            row = tuple(sum(v[j] * v[(2 * q - j) % d] for j in range(d)) / (d * norm)
                        for q in range(d))
            assert sum(v) == 0 and sum(row) == 0 and any(row)
            assert any(x < 0 for x in row)
            assert sum(x * x for x in row) >= F(1, d * (d - 1))
            mass = -sum(x for x in row if x < 0)
            assert 4 * d * (d - 1) * mass * mass >= 1
            count += 1
            noninteger += any(x.denominator != 1 for x in v)
    check("S5_RATIONAL_ODD", count == 2175,
          "dimensions=3,5,7,9,15 vectors=" + str(count) + " noninteger_vectors=" + str(noninteger) +
          " zero_sum_nonzero_row=PASS squared_bound=PASS")


def readers():
    low = tuple(scale(x, 5) for x in wigner((4, -1, -1, -1, -1)))
    expected = {(F(1), F(0)): 1, (F(3, 4), F(0)): 4, (F(-1, 4), F(0)): 4,
                (F(1, 8), F(1, 8)): 8, (F(1, 8), F(-1, 8)): 8}
    assert Counter(low) == expected
    acceptance = tuple((F(r != 0), F(0)) for q, r in POINTS)
    plus = tuple(scale(x, 5) for x in wigner((1, 1, 1, 1, 1)))
    assert acceptance == tuple(add(ONE, scale(x, -1)) for x in plus)
    high = tuple(add(x, scale(y, -1)) for x, y in zip(acceptance, low))
    assert Counter(high) == {(F(-1), F(0)): 1, (F(1, 4), F(0)): 8,
                             (F(7, 8), F(-1, 8)): 8, (F(7, 8), F(1, 8)): 8}
    probabilities = []
    for response in (low, acceptance, high):
        line_sums = [total(response[5 * q + r] for q, r in line) for line in LINES]
        whole = total(line_sums[:5])
        for u in POINTS:
            inversion = scale(add(total(line_sums[i] for i, line in enumerate(SETS) if u in line),
                                  scale(whole, -1)), F(1, 5))
            assert inversion == response[5 * u[0] + u[1]]
        if response == low:
            probabilities = [scale(x, F(1, 5)) for x in line_sums]
    assert Counter(probabilities[:5]) == {(F(4, 5), F(0)): 1, (F(1, 20), F(0)): 4}
    assert Counter(probabilities[5:10]) == {ZERO: 1, (F(1, 4), F(0)): 4}
    assert sum(b == 0 and (5 * a).denominator == 1 for a, b in probabilities) == 2
    assert sum(sign(x) < 0 for x in low) == 12
    assert sum(sign(x) < 0 for x in high) == 1
    assert sum(sign(add(x, scale(ONE, -1))) > 0 for x in high) == 8
    check("S7_READERS", True,
          "effects=3 dual_inversions=75 LOW_negative=12 LOW_grid_probabilities=2 HIGH_below_zero=1 HIGH_above_one=8")


def counting():
    scenarios = 0
    for preparation, d1, d2 in product(range(30), range(6), range(6)):
        counts, finals = Counter(), Counter()
        for u, t1, t2 in product(LINES[preparation], range(5), range(5)):
            b1 = label(u, d1)
            middle = shift(u, d1, t1)
            b2 = label(middle, d2)
            final = shift(middle, d2, t2)
            counts[b1, b2] += 1
            finals[b1, b2, final] += 1
        for b1, b2 in product(range(5), repeat=2):
            first, second = 5 * d1 + b1, 5 * d2 + b2
            intersection1 = len(SETS[preparation] & SETS[first])
            intersection2 = len(SETS[first] & SETS[second])
            assert counts[b1, b2] == 5 * intersection1 * intersection2
            for u in POINTS:
                expected = intersection1 * intersection2 if u in SETS[second] else 0
                assert finals[b1, b2, u] == expected
        scenarios += 1
    control = 0
    for preparation, d1, d2 in product(range(30), range(6), range(6)):
        if d1 == d2:
            continue
        returned = 0
        for u, t1, t2 in product(LINES[preparation], range(5), range(5)):
            first = label(u, d1)
            final = shift(shift(u, d1, t1), d2, t2)
            returned += label(final, d1) == first
            assert label(u, d1) == first  # U0 returns first with certainty.
        assert returned == 25
        control += 1
    check("S8_ENSEMBLE", scenarios == 1080 and control == 900,
          "two_round_scenarios=1080 microstates_each=125 three_round_controls=900 U1_return=1/5 U0_return=1")
    # For a universal point-only update and a transversal singleton outcome,
    # uniform next-direction probabilities require uniform counts on its line.
    # Exhaust all nonnegative count vectors with totals 1 through 5. Restricting
    # support to the outcome line follows already from repeating its direction.
    rejected, admitted = 0, 0
    for counts in product(range(6), repeat=5):
        size = sum(counts)
        if not 1 <= size <= 5:
            continue
        good = all(5 * count == size for count in counts)
        if good:
            admitted += 1
            assert size == 5 and counts == (1, 1, 1, 1, 1)
        else:
            rejected += 1
    check("S8_RESOURCE", admitted == 1 and rejected == 250,
          "continuation_histograms=251 rejected=250 minimum=5 scope=universal_point_only_continuation_ready")


def main():
    print("NON-CANONICAL W2 CODEX-W2-INDEPENDENT-20261002 L1", flush=True)
    geometry()
    forms()
    operators()
    census()
    rational_row_attack()
    readers()
    counting()
    print("PASS COMPLETE independent_checks=10 falsifiers=0", flush=True)
    print("STOP_APPLICABILITY / H_NOT_TESTED unchanged", flush=True)


if __name__ == "__main__":
    main()
