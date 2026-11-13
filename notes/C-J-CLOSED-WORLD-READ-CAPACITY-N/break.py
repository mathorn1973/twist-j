#!/usr/bin/env python3
"""Frozen independent exact audit; stdlib only; no builder imports.

Read BREAK_CONTRACT.md before execution.  All scientific work is under main.
"""

import itertools
import json
from functools import lru_cache


ONE = (1, 0, 0, 0)
ZERO = (0, 0, 0, 0)
Z = (0, 1, 0, 0)
J = (1, 0, 1, 0)
PHI_INV = (-1, 0, -1, -1)


def emit(kind, **data):
    print(json.dumps(dict(type=kind, **data), sort_keys=True,
                     separators=(",", ":")), flush=True)


def multiply(a, b):
    """Coefficient convolution, then x^4 = -1-x-x^2-x^3."""
    raw = [0] * 7
    for i in range(4):
        for j in range(4):
            raw[i + j] += a[i] * b[j]
    for degree in range(6, 3, -1):
        leading = raw[degree]
        raw[degree] = 0
        for offset in range(1, 5):
            raw[degree - offset] -= leading
    return tuple(raw[:4])


def power(a, n):
    assert n >= 0
    answer = ONE
    while n:
        if n & 1:
            answer = multiply(answer, a)
        a = multiply(a, a)
        n //= 2
    return answer


@lru_cache(None)
def signed_permutations(size):
    result = []
    for p in itertools.permutations(range(size)):
        inversions = sum(p[i] > p[j] for i in range(size)
                         for j in range(i + 1, size))
        result.append((p, -1 if inversions & 1 else 1))
    return tuple(result)


def determinant_by_permutations(rows):
    size = len(rows)
    assert all(len(row) == size for row in rows)
    answer = 0
    for permutation, sign in signed_permutations(size):
        term = sign
        for i, j in enumerate(permutation):
            term *= rows[i][j]
            if term == 0:
                break
        answer += term
    return answer


def norm(a):
    """Res(x^4+x^3+x^2+x+1, a), using the Sylvester determinant.

    This does not form a multiplication matrix.  The monic first polynomial
    makes the resultant exactly the product of a over its four embeddings.
    """
    if a == ZERO:
        return 0
    degree = max(i for i, coefficient in enumerate(a) if coefficient)
    if degree == 0:
        return a[0] ** 4
    first = (1, 1, 1, 1, 1)  # Descending coefficients.
    second = tuple(reversed(a[:degree + 1]))
    size = 4 + degree
    rows = []
    for shift in range(degree):
        rows.append([0] * shift + list(first)
                    + [0] * (size - shift - len(first)))
    for shift in range(4):
        rows.append([0] * shift + list(second)
                    + [0] * (size - shift - len(second)))
    return determinant_by_permutations(rows)


@lru_cache(None)
def divisors(n):
    assert n >= 1
    return tuple(d for d in range(1, n + 1) if n % d == 0)


@lru_cache(None)
def fixed_count(unit, n):
    a = list(power(unit, n))
    a[0] -= 1
    a = tuple(a)
    if a == ZERO:
        return None  # O/(0) is infinite; no finite law is assigned.
    result = abs(norm(a))
    assert result > 0
    return result


@lru_cache(None)
def primitive_count(unit, n):
    total = fixed_count(unit, n)
    assert total is not None
    exact = total - sum(primitive_count(unit, d)
                        for d in divisors(n) if d != n)
    assert exact >= 0 and exact % n == 0
    return exact


@lru_cache(None)
def primitive_words(m, n):
    exact = m ** n - sum(primitive_words(m, d)
                         for d in divisors(n) if d != n)
    assert exact >= 0 and exact % n == 0
    return exact


def necklace_counts(m, n):
    return {d: primitive_words(m, d) // d for d in divisors(n)}


def allocation_patterns(lengths, d, c, available):
    """Every integer vector whose weighted contribution to one necklace is c."""
    candidates = [(i, e // d) for i, e in enumerate(lengths)
                  if e % d == 0 and e // d <= c and available[i] > 0]
    vector = [0] * len(lengths)
    result = []

    def visit(at, remaining):
        if at == len(candidates):
            if remaining == 0:
                result.append(tuple(vector))
            return
        i, weight = candidates[at]
        for amount in range(min(remaining // weight, available[i]) + 1):
            vector[i] = amount
            visit(at + 1, remaining - amount * weight)
        vector[i] = 0

    visit(0, c)
    # Preserve scarce shorter cycles first.  This ordering affects speed only.
    return tuple(sorted(result))


def validate_witness(cycles, n, m, c, witness):
    lengths = divisors(n)
    targets = necklace_counts(m, n)
    total = sum(e * cycles.get(e, 0) for e in lengths)
    assert c >= 1 and c * m ** n <= total
    if witness["kind"] == "only_n_cycles":
        assert c == n and cycles.get(n, 0) >= m ** n
        assert sum(d * targets[d] for d in lengths) == m ** n
        return
    assert witness["kind"] == "integer_patterns"
    covered = {d: 0 for d in lengths}
    consumed = {e: 0 for e in lengths}
    for item in witness["patterns"]:
        d, count = item["period"], item["necklaces"]
        assert d in covered and isinstance(count, int) and count > 0
        allocation = {int(e): amount for e, amount in item["cycles"].items()}
        assert all(e in consumed and e % d == 0
                   and isinstance(amount, int) and amount > 0
                   for e, amount in allocation.items())
        assert sum((e // d) * amount for e, amount in allocation.items()) == c
        covered[d] += count
        for e, amount in allocation.items():
            consumed[e] += count * amount
    assert covered == targets
    assert all(consumed[e] <= cycles.get(e, 0) for e in lengths)
    assert sum(e * consumed[e] for e in lengths) == c * m ** n


def solve_fixed_c(cycles, n, m, c):
    """Complete integer allocation search at the given replication count.

    A pattern describes ONE necklace.  Nonnegative multiplicities of every
    pattern are enumerated with their sum exactly B_d.  These are equivalent
    to assigning the individually distinguishable necklaces, since necklaces
    of a given period have identical constraints.  No fractional relaxation.
    """
    lengths = divisors(n)
    available = tuple(cycles.get(e, 0) for e in lengths)
    targets = necklace_counts(m, n)
    total = sum(e * count for e, count in zip(lengths, available))
    if c < 1 or c * m ** n > total:
        return None
    if c * targets[n] > cycles.get(n, 0):
        return None
    periods = tuple(d for d in reversed(lengths) if targets[d])
    patterns = tuple(allocation_patterns(lengths, d, c, available)
                     for d in periods)
    if any(not options for options in patterns):
        return None
    suffix_minima = []
    for options in patterns:
        table = [None] * len(options)
        lower = list(options[-1])
        for p in range(len(options) - 1, -1, -1):
            lower = [min(a, b) for a, b in zip(lower, options[p])]
            table[p] = tuple(lower)
        suffix_minima.append(tuple(table))

    @lru_cache(None)
    def search(g, p, remaining, capacities):
        if g == len(periods):
            return ()
        if remaining == 0:
            next_remaining = targets[periods[g + 1]] if g + 1 < len(periods) else 0
            return search(g + 1, 0, next_remaining, capacities)
        options = patterns[g]
        if p == len(options):
            return None
        minimum = suffix_minima[g][p]
        if any(remaining * amount > supply
               for amount, supply in zip(minimum, capacities)):
            return None
        pattern = options[p]
        maximum = min([remaining] + [supply // amount
                                     for supply, amount in zip(capacities, pattern)
                                     if amount])
        amounts = (remaining,) if p + 1 == len(options) else range(maximum, -1, -1)
        for count in amounts:
            if count > maximum:
                continue
            rest = tuple(supply - count * amount
                         for supply, amount in zip(capacities, pattern))
            tail = search(g, p + 1, remaining - count, rest)
            if tail is not None:
                return (((periods[g], count, pattern),) + tail) if count else tail
        return None

    solution = search(0, 0, targets[periods[0]], available)
    if solution is None:
        return None
    witness = {"kind": "integer_patterns", "patterns": [
        {"period": d, "necklaces": count,
         "cycles": {str(e): amount for e, amount in zip(lengths, pattern) if amount}}
        for d, count, pattern in solution]}
    validate_witness(cycles, n, m, c, witness)
    return witness


def decide(cycles, n, m):
    total = sum(e * count for e, count in cycles.items())
    cardinal_cap = total // m ** n
    primitive_cap = cycles.get(n, 0) // necklace_counts(m, n)[n]
    cap = min(cardinal_cap, primitive_cap)
    if cap == 0:
        return False, None, None, {"cardinality_cap": cardinal_cap,
                                   "primitive_cap": primitive_cap, "tested_c": []}
    if cycles.get(n, 0) >= m ** n:
        witness = {"kind": "only_n_cycles", "cycles_used": m ** n,
                   "necklaces_of_period_d_receive": "d cycles of length n"}
        validate_witness(cycles, n, m, n, witness)
        return True, n, witness, {"method": "proved_c_equals_n_construction"}
    for c in range(1, cap + 1):
        witness = solve_fixed_c(cycles, n, m, c)
        if witness is not None:
            return True, c, witness, {"method": "complete_integer_search"}
    return False, None, None, {"cardinality_cap": cardinal_cap,
                               "primitive_cap": primitive_cap,
                               "tested_c": list(range(1, cap + 1))}


def lucas(index):
    a, b = 2, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def ceiling_ratio(a, b):
    assert a >= 0 and b > 0
    return (a + b - 1) // b


def sufficient_onset(k, m):
    L = lucas(2 * abs(k))
    Q = 2 * L - 1
    assert 2 <= m <= L - 1
    n0 = max(2, ceiling_ratio(2 * m, Q - 2 * m),
             ceiling_ratio(12 * L, Q * Q - 4 * L))

    def conditions(n):
        return (Q ** n >= 32 * n * (2 * m) ** n,
                Q ** (2 * n) >= 512 ** 2 * n ** 2 * (4 * L) ** n)

    n = n0
    while not all(conditions(n)):
        n += 1
    assert n == n0 or not all(conditions(n - 1))
    assert n0 * (Q - 2 * m) >= 2 * m
    assert n0 * (Q * Q - 4 * L) >= 12 * L
    for t in range(n0, n + 13):
        assert Q * t >= 2 * m * (t + 1)
        assert Q * Q * t * t >= 4 * L * (t + 1) ** 2
    for t in range(n, n + 13):
        assert all(conditions(t))
    return L, Q, n0, n


def exclusion_onset(k, m):
    L = lucas(2 * abs(k))
    assert m >= L and L * L - 1 < L * m
    n = 1
    while 16 * (L * L - 1) ** n >= (L * m) ** n:
        n += 1
    assert n == 1 or 16 * (L * L - 1) ** (n - 1) >= (L * m) ** (n - 1)
    for t in range(n, n + 13):
        assert 16 * (L * L - 1) ** t < (L * m) ** t
    return L, n


def permutation_cycles(permutation):
    unseen = set(range(len(permutation)))
    cycles = []
    while unseen:
        start = min(unseen)
        current = start
        orbit = []
        while current in unseen:
            unseen.remove(current)
            orbit.append(current)
            current = permutation[current]
        assert current == start
        cycles.append(tuple(orbit))
    return tuple(cycles)


def brute_reader_cs(permutation, n, m):
    """Direct labels/exclusion enumeration, without allocation patterns."""
    N = len(permutation)
    word_count = m ** n
    if N < word_count:
        return set()
    found = set()
    for labeling in itertools.product(range(-1, m), repeat=N):
        support = [i for i, value in enumerate(labeling) if value >= 0]
        if not support or len(support) % word_count:
            continue
        if any((labeling[i] < 0) != (labeling[permutation[i]] < 0)
               for i in range(N)):
            continue
        words = {}
        for start in support:
            state = start
            word = []
            for _ in range(n):
                word.append(labeling[state])
                state = permutation[state]
            key = tuple(word)
            words[key] = words.get(key, 0) + 1
        c = len(support) // word_count
        if len(words) == word_count and all(value == c for value in words.values()):
            found.add(c)
    return found


def integer_partitions(total, smallest=1):
    if total == 0:
        yield ()
    else:
        for first in range(smallest, total + 1):
            for tail in integer_partitions(total - first, first):
                yield (first,) + tail


def canonical_permutation(parts):
    permutation = []
    offset = 0
    for length in parts:
        permutation.extend(offset + ((i + 1) % length) for i in range(length))
        offset += length
    return tuple(permutation)


def run_permutation_controls():
    systems = set()
    for N in range(1, 5):
        systems.update(itertools.permutations(range(N)))
    for N in range(1, 9):
        systems.update(canonical_permutation(parts) for parts in integer_partitions(N))
    rows = 0
    tested_cs = 0
    for permutation in sorted(systems, key=lambda p: (len(p), p)):
        orbits = permutation_cycles(permutation)
        for n in range(1, 5):
            if any(n % len(orbit) for orbit in orbits):
                continue
            cycles = {d: sum(len(orbit) == d for orbit in orbits) for d in divisors(n)}
            for m in (2, 3):
                direct = brute_reader_cs(permutation, n, m)
                integer = set()
                for c in range(1, len(permutation) // m ** n + 1):
                    witness = solve_fixed_c(cycles, n, m, c)
                    if witness is not None:
                        integer.add(c)
                    tested_cs += 1
                assert direct == integer, (permutation, n, m, direct, integer)
                rows += 1
    label = (0, 0, 1, 1)
    windows = [tuple(label[(i + j) % 4] for j in range(2)) for i in range(4)]
    assert sorted(windows) == list(itertools.product(range(2), repeat=2))
    for N in range(1, 13):
        assert N < 2 ** N  # A single full-N cycle has at most N initial states.
    emit("PERMUTATION_CONTROL", all_permutations_up_to=4,
         all_cycle_types_up_to=8, horizons=[1, 2, 3, 4], alphabets=[2, 3],
         rows=rows, tested_c_values=tested_cs, status="PASS",
         de_bruijn_label=list(label), de_bruijn_windows=windows)


def run_small_quotient_control():
    # The map sum(coefficients) mod 5 is onto F_5 and is a ring map.
    # If the relation has norm 5 and maps to zero, its ideal has index 5
    # and must equal the map's kernel.  This certifies all five residue classes.
    basis = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
    for a in basis:
        for b in basis:
            assert sum(multiply(a, b)) % 5 == (sum(a) * sum(b)) % 5
    for n in range(1, 13):
        if n % 5 == 0:
            assert power(Z, n) == ONE and fixed_count(Z, n) is None
            continue
        relation = list(power(Z, n))
        relation[0] -= 1
        assert sum(relation) % 5 == 0 and abs(norm(tuple(relation))) == 5
        tick = [sum(multiply(Z, (x, 0, 0, 0))) % 5 for x in range(5)]
        assert tick == list(range(5))
        assert primitive_count(Z, 1) == 5
        assert all(primitive_count(Z, d) == (5 if d == 1 else 0)
                   for d in divisors(n))
        emit("SMALL_QUOTIENT", unit="z", n=n, representatives=list(range(5)),
             tick=tick, F=5, status="PASS")


def main():
    units = (("J", J, 1), ("phi^-1", PHI_INV, 1),
             ("z", Z, 0), ("J^2", multiply(J, J), 2))
    assert power(Z, 5) == ONE
    assert tuple(sum(power(Z, j)[i] for j in range(5)) for i in range(4)) == ZERO
    assert multiply(PHI_INV, (0, 0, -1, -1)) == ONE
    emit("CONTRACT", name="C-J-CLOSED-WORLD-READ-CAPACITY-N",
         implementation="independent coefficient/resultant breaker",
         units=[u[0] for u in units], n_max=12, m_min=2, m_max=7)
    row_count = 0
    for name, unit, k in units:
        for n in range(1, 13):
            F = fixed_count(unit, n)
            if F is None:
                assert name == "z" and n % 5 == 0
                for m in range(2, 8):
                    emit("CENSUS", unit=name, m=m, n=n, F="INFINITE", P=None,
                         possible="INFINITE", c=None, witness=None)
                    row_count += 1
                continue
            cycles = {d: primitive_count(unit, d) // d for d in divisors(n)}
            assert sum(d * count for d, count in cycles.items()) == F
            for m in range(2, 8):
                possible, c, witness, decision = decide(cycles, n, m)
                if possible:
                    assert c * primitive_words(m, n) <= primitive_count(unit, n)
                    validate_witness(cycles, n, m, c, witness)
                if name == "z":
                    assert possible == (n == 1 and m <= 5)
                if name == "J" and m == 2 and n in (1, 5):
                    assert not possible
                emit("CENSUS", unit=name, m=m, n=n, F=F,
                     P=primitive_count(unit, n), cycles=cycles,
                     W=primitive_words(m, n), possible=possible, c=c,
                     witness=witness, decision=decision)
                row_count += 1
    assert tuple(fixed_count(J, n) for n in range(1, 6)) == (1, 11, 31, 55, 121)
    assert tuple(primitive_count(J, n) for n in range(1, 6)) == (1, 10, 30, 44, 120)
    for n, c in ((2, 2), (3, 3)):
        cycles = {d: primitive_count(J, d) // d for d in divisors(n)}
        witness = solve_fixed_c(cycles, n, 2, c)
        assert witness is not None
        emit("EXPOSED_WITNESS_CONTROL", unit="J", m=2, n=n, c=c,
             support=c * 2 ** n, witness=witness, status="PASS")
    for k, alphabets in ((1, (2,)), (2, tuple(range(2, 7)))):
        for m in alphabets:
            L, Q, n0, onset = sufficient_onset(k, m)
            emit("ONSET", k=k, m=m, L=L, Q=Q, n0=n0, n_star=onset,
                 inequalities=True, monotonicity=True)
            for name, unit, unit_k in units:
                if unit_k != k:
                    continue
                for n in range(onset, onset + 13):
                    P = primitive_count(unit, n)
                    assert P >= n * m ** n
                    emit("ONSET_AUDIT", unit=name, k=k, m=m, n=n,
                         F=fixed_count(unit, n), P=P, required=n * m ** n,
                         status="PASS")
    for k, alphabets in ((1, tuple(range(3, 8))), (2, (7,))):
        for m in alphabets:
            L, onset = exclusion_onset(k, m)
            emit("EXCLUSION_ONSET", k=k, m=m, L=L, n_star=onset,
                 inequality=True, monotonicity=True)
    stride_answers = []
    for b in (2, 5, 16, 256):
        k = 1
        while b >= lucas(2 * k):
            k += 1
        assert b < lucas(2 * k)
        assert k == 1 or b >= lucas(2 * (k - 1))
        stride_answers.append(k)
        emit("STRIDE", denominator=b, stride=k, L=lucas(2 * k),
             previous_L=None if k == 1 else lucas(2 * k - 2))
    assert stride_answers == [1, 2, 3, 6]
    run_small_quotient_control()
    run_permutation_controls()
    assert row_count == 4 * 12 * 6
    emit("SUMMARY", census_rows=row_count, status="PASS")


if __name__ == "__main__":
    main()
