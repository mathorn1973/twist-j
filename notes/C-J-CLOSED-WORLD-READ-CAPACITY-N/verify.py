#!/usr/bin/env python3
"""Exact audit of periodic cyclotomic quotient readers.

Standard library only. No floating point, random input, network, or package
imports. This file must not be executed before its public preregistration pin.
The finite reconnaissance and analytical controls named in PREREG are exposed.
"""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import json


SIZE = 4
IDENTITY = tuple(tuple(int(i == j) for j in range(SIZE)) for i in range(SIZE))
ZETA = ((0, 0, 0, -1), (1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1))


def mat_add(a, b, factor=1):
    return tuple(tuple(a[i][j] + factor * b[i][j] for j in range(SIZE))
                 for i in range(SIZE))


def mat_scale(a, factor):
    return tuple(tuple(factor * v for v in row) for row in a)


def mat_mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(SIZE))
                       for j in range(SIZE)) for i in range(SIZE))


def mat_pow(a, exponent):
    result = IDENTITY
    while exponent:
        if exponent & 1:
            result = mat_mul(result, a)
        a = mat_mul(a, a)
        exponent //= 2
    return result


def determinant(matrix):
    """Fraction-free Bareiss determinant, including row pivoting."""
    a = [list(row) for row in matrix]
    size = len(a)
    previous = 1
    sign = 1
    for k in range(size - 1):
        if not a[k][k]:
            pivot = next((i for i in range(k + 1, size) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def mobius(n):
    answer = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            answer = -answer
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        answer = -answer
    return answer


def primitive(total, n):
    return sum(mobius(n // d) * total(d) for d in divisors(n))


J = mat_add(IDENTITY, mat_pow(ZETA, 2))
PHI_INVERSE = mat_scale(mat_add(mat_add(IDENTITY, mat_pow(ZETA, 2)),
                              mat_pow(ZETA, 3)), -1)
UNITS = {"J": J, "phi_inverse": PHI_INVERSE,
         "zeta": ZETA, "J_squared": mat_mul(J, J)}


@lru_cache(maxsize=None)
def norm_count(name, n):
    return abs(determinant(mat_add(mat_pow(UNITS[name], n), IDENTITY, -1)))


def source_cycles(name, n):
    counts = {}
    for d in divisors(n):
        points = primitive(lambda e: norm_count(name, e), d)
        assert points >= 0 and points % d == 0
        counts[d] = points // d
    assert sum(d * c for d, c in counts.items()) == norm_count(name, n)
    return counts


def target_necklaces(m, n):
    counts = {}
    for d in divisors(n):
        words = primitive(lambda e: m ** e, d)
        assert words >= 0 and words % d == 0
        counts[d] = words // d
    assert sum(d * c for d, c in counts.items()) == m ** n
    return counts


def extended_gcd(a, b):
    """Return g>0 and s,t with s*a+t*b=g, for nonzero pair."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    assert old_s * a + old_t * b == old_r and old_r > 0
    return old_r, old_s, old_t


def column_hermite(matrix):
    """Triangular column lattice basis, with its unimodular certificate.

    Integer column Bezout operations produce H=B*Q. No determinant-value
    result is used to choose representatives. The resulting upper triangular
    H has positive diagonal and 0<=H[i,j]<H[i,i] for i<j.
    """
    h = [list(row) for row in matrix]
    qmat = [list(row) for row in IDENTITY]
    for row in range(SIZE - 1, -1, -1):
        pivot = next((j for j in range(row + 1) if h[row][j]), None)
        assert pivot is not None
        for a in (h, qmat):
            for r in range(SIZE):
                a[r][pivot], a[r][row] = a[r][row], a[r][pivot]
        for col in range(row):
            if not h[row][col]:
                continue
            a, b = h[row][row], h[row][col]
            g, s, t = extended_gcd(a, b)
            for matrix_work in (h, qmat):
                old_pivot = [matrix_work[r][row] for r in range(SIZE)]
                old_col = [matrix_work[r][col] for r in range(SIZE)]
                for r in range(SIZE):
                    matrix_work[r][row] = s * old_pivot[r] + t * old_col[r]
                    matrix_work[r][col] = -(b // g) * old_pivot[r] + (a // g) * old_col[r]
        if h[row][row] < 0:
            for a in (h, qmat):
                for r in range(SIZE):
                    a[r][row] = -a[r][row]
    for col in range(SIZE):
        for row in range(col - 1, -1, -1):
            quotient = h[row][col] // h[row][row]
            for a in (h, qmat):
                for r in range(SIZE):
                    a[r][col] -= quotient * a[r][row]
    h, qmat = tuple(map(tuple, h)), tuple(map(tuple, qmat))
    assert mat_mul(matrix, qmat) == h
    assert abs(determinant(qmat)) == 1
    for i in range(SIZE):
        assert h[i][i] > 0
        for j in range(i):
            assert h[i][j] == 0
        for j in range(i + 1, SIZE):
            assert 0 <= h[i][j] < h[i][i]
    return h


def quotient_orbits(name, n):
    """Enumerate every HNF representative; never infer orbit counts by Mobius."""
    unit = UNITS[name]
    basis = mat_add(mat_pow(unit, n), IDENTITY, -1)
    h = column_hermite(basis)
    diag = tuple(h[i][i] for i in range(SIZE))
    total = 1
    strides = []
    for d in diag:
        strides.append(total)
        total *= d
    active = tuple(i for i, d in enumerate(diag) if d > 1)

    def reduce_vector(values):
        values = list(values)
        for i in range(SIZE - 1, -1, -1):
            quotient, residue = divmod(values[i], diag[i])
            values[i] = residue
            for j in range(i):
                values[j] -= quotient * h[j][i]
        return tuple(values)

    columns = tuple(reduce_vector(tuple(unit[i][j] for i in range(SIZE)))
                    for j in range(SIZE))
    if not active:
        def advance(index):
            assert index == 0
            return 0
    elif len(active) == 1:
        coordinate = active[0]
        multiplier = columns[coordinate][coordinate]
        modulus = diag[coordinate]

        def advance(index):
            return (multiplier * index) % modulus
    else:
        def advance(index):
            coordinates = tuple((index // strides[j]) % diag[j] for j in range(SIZE))
            image = reduce_vector(tuple(sum(columns[j][i] * coordinates[j] for j in active)
                                        for i in range(SIZE)))
            return sum(image[i] * strides[i] for i in active)

    seen = bytearray(total)
    cycles = Counter()
    for start in range(total):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = 1
            current = advance(current)
            length += 1
            assert length <= n
        assert current == start and n % length == 0
        cycles[length] += 1
    assert sum(seen) == total
    assert sum(length * count for length, count in cycles.items()) == total
    return total, {d: cycles.get(d, 0) for d in divisors(n)}, h


@lru_cache(maxsize=None)
def necklace_patterns(lengths, d, c):
    """All exact integer patterns for one target d-necklace."""
    eligible = tuple((i, e // d) for i, e in enumerate(lengths)
                     if e % d == 0 and e // d <= c)
    result = []
    work = [0] * len(lengths)

    def visit(index, remaining):
        if index == len(eligible):
            if remaining == 0:
                result.append(tuple(work))
            return
        i, weight = eligible[index]
        for count in range(remaining // weight, -1, -1):
            work[i] = count
            visit(index + 1, remaining - count * weight)
        work[i] = 0

    visit(0, c)
    return tuple(result)


def complete_assignment(lengths, available, necklaces, c):
    """Complete grouped integer assignment; no fractional-flow relaxation.

    Each recursive pattern multiplicity is bounded by both the number of
    necklaces and every source-cycle capacity. Failed integer states are
    memoized. All assignments are finite, so a negative return is exhaustive.
    """
    groups = tuple((d, necklaces[d]) for d in reversed(lengths) if necklaces[d])

    @lru_cache(maxsize=None)
    def solve(group_index, capacities):
        if group_index == len(groups):
            return ()
        d, number = groups[group_index]
        patterns = tuple(p for p in necklace_patterns(lengths, d, c)
                         if all(x <= limit for x, limit in zip(p, capacities)))
        if not patterns:
            return None
        failed = set()

        def allocate(pattern_index, remaining, caps, record):
            if remaining == 0:
                tail = solve(group_index + 1, caps)
                if tail is not None:
                    return ((d, tuple(record)),) + tail
                return None
            key = (pattern_index, remaining, caps)
            if key in failed or pattern_index == len(patterns):
                return None
            remaining_patterns = patterns[pattern_index:]
            if any(remaining * min(p[i] for p in remaining_patterns) > caps[i]
                   for i in range(len(lengths))):
                failed.add(key)
                return None
            pattern = patterns[pattern_index]
            upper = min([remaining] + [caps[i] // use for i, use in enumerate(pattern) if use])
            lower = remaining if pattern_index + 1 == len(patterns) else 0
            for multiplicity in range(upper, lower - 1, -1):
                new_caps = tuple(limit - multiplicity * use for limit, use in zip(caps, pattern))
                new_record = record + (((pattern, multiplicity),) if multiplicity else ())
                answer = allocate(pattern_index + 1, remaining - multiplicity, new_caps, new_record)
                if answer is not None:
                    return answer
            failed.add(key)
            return None

        return allocate(0, number, capacities, ())

    return solve(0, available)


def audit_certificate(cycles, necklaces, c, assignment):
    lengths = tuple(sorted(cycles))
    used = Counter()
    assert dict((d, sum(count for pattern, count in group)) for d, group in assignment) == necklaces
    for d, group in assignment:
        for pattern, count in group:
            assert count > 0 and len(pattern) == len(lengths)
            assert all(use >= 0 and (not use or e % d == 0)
                       for e, use in zip(lengths, pattern))
            assert sum((e // d) * use for e, use in zip(lengths, pattern)) == c
            for e, use in zip(lengths, pattern):
                used[e] += use * count
    assert all(used[e] <= cycles[e] for e in lengths)


def reader(cycles, m, n):
    lengths = tuple(sorted(cycles))
    necklaces = target_necklaces(m, n)
    states = sum(d * cycles[d] for d in lengths)
    if m ** n > states:
        return False, {"reason": "cardinality"}
    if all(cycles[d] >= necklaces[d] for d in lengths):
        return True, {"mode": "exact-period", "c": 1}
    if cycles[n] >= m ** n:
        return True, {"mode": "full-period", "c": n}
    # Every primitive target necklace requires c separate n-cycles.
    max_c = min(states // (m ** n), cycles[n] // necklaces[n])
    for c in range(1, max_c + 1):
        assignment = complete_assignment(lengths, tuple(cycles[d] for d in lengths), necklaces, c)
        if assignment is not None:
            audit_certificate(cycles, necklaces, c, assignment)
            encoded = json.dumps(assignment, separators=(",", ":"))
            return True, {"mode": "integer-assignment", "c": c,
                          "assignment_sha256": sha256(encoded.encode()).hexdigest(),
                          "assignment": assignment}
    return False, {"reason": "exhaustive-cycle-assignment", "max_c": max_c}


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def ceiling_ratio(a, b):
    assert a >= 0 and b > 0
    return (a + b - 1) // b


def sufficient_onset(k, m):
    ell = lucas(2 * k)
    q = 2 * ell - 1
    assert 2 <= m <= ell - 1
    n0 = max(2, ceiling_ratio(2 * m, q - 2 * m),
             ceiling_ratio(12 * ell, q * q - 4 * ell))

    def inequalities(n):
        return (q ** n >= 32 * n * (2 * m) ** n and
                q ** (2 * n) >= 512 ** 2 * n ** 2 * (4 * ell) ** n)

    n = n0
    while not inequalities(n):
        n += 1
    assert inequalities(n)
    assert n == n0 or not inequalities(n - 1)
    assert q * n >= 2 * m * (n + 1)
    assert q * q * n * n >= 4 * ell * (n + 1) ** 2
    # The frozen lower n0 establishes monotonicity for all larger n,
    # independently of the subsequent finite arithmetic audit.
    assert (q - 2 * m) * n0 >= 2 * m
    assert (q * q - 4 * ell) * n0 >= 12 * ell
    return n0, n


def emit(label, value):
    print(label + " " + json.dumps(value, sort_keys=True, separators=(",", ":")))


def main():
    assert mat_pow(ZETA, 5) == IDENTITY
    assert mat_mul(J, mat_add(PHI_INVERSE, IDENTITY)) == ZETA
    assert all(determinant(u) == 1 for u in UNITS.values())
    assert [norm_count("J", n) for n in range(1, 6)] == [1, 11, 31, 55, 121]
    assert [primitive(lambda d: norm_count("J", d), n) for n in range(1, 6)] == [1, 10, 30, 44, 120]
    census = []
    decisions = {}
    for name in UNITS:
        for n in range(1, 13):
            total = norm_count(name, n)
            if total == 0:
                assert name == "zeta" and n % 5 == 0
                row = {"u": name, "n": n, "status": "INFINITE_QUOTIENT"}
                census.append(row)
                emit("CENSUS", row)
                continue
            cycles = source_cycles(name, n)
            feasible = []
            for m in range(2, 8):
                answer, certificate = reader(cycles, m, n)
                feasible.append([m, answer])
                decisions[name, n, m] = answer
                if answer:
                    emit("CERT", {"u": name, "n": n, "m": m, **certificate})
            row = {"u": name, "n": n, "states": total,
                   "cycles": [[d, cycles[d]] for d in sorted(cycles)], "readers": feasible}
            census.append(row)
            emit("CENSUS", row)
            if n <= 8:
                enumerated_total, enumerated_cycles, h = quotient_orbits(name, n)
                assert enumerated_total == total and enumerated_cycles == cycles
                emit("ENUM", {"u": name, "n": n, "states": enumerated_total,
                              "cycles": [[d, enumerated_cycles[d]] for d in sorted(cycles)],
                              "hermite": h})
    assert not decisions["J", 1, 2]
    assert decisions["J", 2, 2] and decisions["J", 3, 2]
    assert not decisions["J", 5, 2]
    assert all(not decisions["J", n, 3] for n in range(1, 6))
    assert all(not decisions["J", n, 5] for n in range(1, 6))
    assert all(decisions["zeta", 1, m] == (m <= 5) for m in range(2, 8))
    assert all(not value for (name, n, m), value in decisions.items()
               if name == "zeta" and n >= 2)
    assert norm_count("J", 2) != norm_count("phi_inverse", 2)
    assert norm_count("J", 2) % (2 ** 2) != 0

    onsets = []
    for k in (1, 2):
        for m in range(2, lucas(2 * k)):
            n0, onset = sufficient_onset(k, m)
            names = ("J", "phi_inverse") if k == 1 else ("J_squared",)
            for name in names:
                for n in range(onset, onset + 13):
                    assert primitive(lambda d: norm_count(name, d), n) >= n * m ** n
            row = {"k": k, "m": m, "n0": n0, "sufficient_onset": onset,
                   "audited_units": names, "audit_end": onset + 12}
            onsets.append(row)
            emit("ONSET", row)
    strides = []
    for denominator in (2, 5, 16, 256):
        k = 1
        while denominator >= lucas(2 * k):
            k += 1
        assert denominator < lucas(2 * k)
        assert k == 1 or denominator >= lucas(2 * (k - 1))
        strides.append([denominator, k])
    assert strides == [[2, 1], [5, 2], [16, 3], [256, 6]]
    emit("STRIDES", strides)

    # A rotation can supply a shorter independent window. It cannot supply
    # independent outputs throughout its own complete period.
    rotation = (0, 0, 1, 1)
    pairs = Counter((rotation[i], rotation[(i + 1) % 4]) for i in range(4))
    assert len(pairs) == 4 and set(pairs.values()) == {1}
    assert 4 < 2 ** 4
    emit("ROTATION_CONTROL", {"cycle_length": 4, "fair_binary_window": 2,
                              "fair_full_period": False})
    emit("CENSUS_SHA256", sha256(json.dumps(census, sort_keys=True, separators=(",", ":")).encode()).hexdigest())
    emit("ONSET_SHA256", sha256(json.dumps(onsets, sort_keys=True, separators=(",", ":")).encode()).hexdigest())
    print("ALL PASS")


if __name__ == "__main__":
    main()
