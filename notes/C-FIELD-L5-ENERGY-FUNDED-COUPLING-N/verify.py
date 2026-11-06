#!/usr/bin/env python3
"""Exact selected local coupling; all-state conclusions require PROOF.md."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path


C = ((1, -1), (-1, 0), (0, 1), (0, 1))
D = ((1, 1, 1, 0), (-1, -1, 0, -1), (0, 0, -1, 1))
A = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
B = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
L = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
N = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
K = ((6, 2, -1, 2), (2, 6, 2, -1), (-1, 2, 6, 2), (2, -1, 2, 6))
P = ((1, -1, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0),
     (0, 0, 1, 0), (0, 0, 0, 1))
S = ((1, 0), (1, 0), (0, 1), (1, -1), (0, 0), (0, 0))
ZERO4 = (0, 0, 0, 0)
ZERO6 = (0,) * 6
ZERO_MATTER = (ZERO4,) * 3
R = ((1, -2, 1, 0), ZERO4, ZERO4)
AM = ((1, 0, 0, 0), (0, -1, 0, 0), (0, -1, 1, 0))
W = (0, 0, 1, 0)


def transpose(a):
    return tuple(zip(*a))


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def mv(a, x):
    assert all(len(row) == len(x) for row in a)
    return tuple(sum(u * v for u, v in zip(row, x)) for row in a)


def mm(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, column))
                       for column in transpose(b)) for row in a)


def scale(a, k):
    return tuple(tuple(k * v for v in row) for row in a)


def difference(a, b):
    return tuple(tuple(x - y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def power(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = mm(out, a)
    return out


def determinant(a):
    rows = [list(map(Fraction, row)) for row in a]
    answer = Fraction(1)
    for k in range(len(rows)):
        pivot = next((i for i in range(k, len(rows)) if rows[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            rows[k], rows[pivot] = rows[pivot], rows[k]
            answer = -answer
        value = rows[k][k]
        answer *= value
        for i in range(k + 1, len(rows)):
            q = rows[i][k] / value
            rows[i] = [x - q * y for x, y in zip(rows[i], rows[k])]
    return answer


def positive(a):
    return all(determinant(tuple(row[:k] for row in a[:k])) > 0
               for k in range(1, len(a) + 1))


def vector_add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def vector_sum(vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(4))


def quadratic(a, x):
    return sum(u * v for u, v in zip(x, mv(a, x)))


def active_energy(x):
    a, b, c, d = x
    return 2*a*a - 2*a*b + 3*b*b + c*c + d*d + 2*a*c - a*d - b*c + 3*b*d


def field_energy(z):
    electric, magnetic = z[:4], z[4:]
    return sum(v*v for v in z) + sum(x*y for x, y in zip(electric, mv(C, magnetic)))


def join_field(x, static):
    return vector_add(mv(P, x), mv(S, static))


def split_field(z):
    e0, e1, e2, e3, m0, m1 = z
    if (2*e0 - 3*e1 + e2 + e3) % 5:
        return None
    nums = (2*e0 - 3*e1 + e2 + e3, -e0 - e1 + 2*e2 + 2*e3,
            2*e0 + 2*e1 + e2 + e3, e0 + e1 + 3*e2 - 2*e3)
    assert all(n % 5 == 0 for n in nums)
    a, b, u, v = (n // 5 for n in nums)
    x, static = (a, b, m0, m1), (u, v)
    assert join_field(x, static) == z
    return x, static


def image_inverse(y):
    if (y[0] + 2*y[1]) % 5 or (y[2] + 2*y[3]) % 5:
        return None
    nums = mv(N, y)
    assert all(n % 5 == 0 for n in nums)
    x = tuple(n // 5 for n in nums)
    assert mv(L, x) == y
    return x


def gate(state):
    matter, spectators, raw, reservoir = state
    assert reservoir >= 0
    if matter not in (R, AM):
        return state
    coordinates = split_field(raw)
    if coordinates is None:
        return state
    field, static = coordinates
    if matter == R:
        low = image_inverse(field)
        if low is None:
            return state
        new_r = reservoir + 4*active_energy(low) - 2
        target, new_field = AM, low
    else:
        new_r = reservoir + 2 - 4*active_energy(field)
        target, new_field = R, mv(L, field)
    if new_r < 0:
        return state
    return target, spectators, join_field(new_field, static), new_r


def free_field(state, backward=False):
    matter, spectators, raw, reservoir = state
    electric, magnetic = raw[:4], raw[4:]
    if backward:
        old_m = vector_add(magnetic, mv(transpose(C), electric))
        old_e = vector_add(electric, tuple(-x for x in mv(C, old_m)))
        new_z = old_e + old_m
    else:
        new_e = vector_add(electric, mv(C, magnetic))
        new_m = vector_add(magnetic, tuple(-x for x in mv(transpose(C), new_e)))
        new_z = new_e + new_m
    return matter, spectators, new_z, reservoir


def cell_step(state):
    return free_field(gate(state))


def cell_inverse(state):
    return gate(free_field(state, backward=True))


def energy(state):
    matter, spectators, raw, reservoir = state
    return sum(quadratic(K, v) for v in matter + spectators) + field_energy(raw) + reservoir


def charges(state):
    matter, spectators, _, _ = state
    return (sum(spectators[0]) + sum(map(sum, matter)),
            sum(spectators[1]), sum(spectators[2]))


def defect(state):
    return tuple(x - y for x, y in zip(mv(D, state[2][:4]), charges(state)))


def valid(state):
    matter, spectators, raw, reservoir = state
    assert len(matter) == len(spectators) == 3 and len(raw) == 6
    assert all(len(v) == 4 for v in matter + spectators)
    flat = tuple(x for v in matter + spectators for x in v) + raw + (reservoir,)
    assert len(flat) == 31 and all(type(x) is int for x in flat)
    assert reservoir >= 0 and energy(state) >= 0


def audit_state(state):
    valid(state)
    out = gate(state)
    valid(out)
    assert gate(out) == state
    assert out[1] == state[1]
    assert vector_sum(out[0]) == vector_sum(state[0])
    assert energy(out) == energy(state) and defect(out) == defect(state)
    assert charges(out) == charges(state)
    assert free_field(out) == gate(free_field(state))
    advanced = cell_step(state)
    valid(advanced)
    assert cell_inverse(advanced) == state
    assert cell_step(cell_inverse(state)) == state
    assert energy(advanced) == energy(state) and defect(advanced) == defect(state)


def spectators_for(static):
    rho = mv(D, mv(S, static)[:4])
    return tuple((q, 0, 0, 0) for q in rho)


def certificates():
    endpoints = ((0, 1), (0, 1), (0, 2), (2, 1))
    assert D == tuple(tuple(int(tail == j) - int(head == j)
                           for tail, head in endpoints) for j in range(3))
    assert mm(D, C) == ((0, 0),) * 3
    assert mm(transpose(C), C) == ((2, -1), (-1, 3))
    raw_metric = tuple(tuple(2*int(i == j) if (i < 4) == (j < 4)
                            else C[i][j-4] if i < 4 else C[j][i-4]
                            for j in range(6)) for i in range(6))
    assert positive(K) and positive(B) and positive(raw_metric)
    t = transpose(tuple(free_field((ZERO_MATTER, ZERO_MATTER, basis, 0))[2]
                        for basis in eye(6)))
    ti = transpose(tuple(free_field((ZERO_MATTER, ZERO_MATTER, basis, 0), True)[2]
                         for basis in eye(6)))
    assert mm(t, ti) == mm(ti, t) == eye(6)
    assert power(t, 5) == eye(6) and power(A, 5) == eye(4)
    assert mm(t, P) == mm(P, A) and mm(t, S) == S
    assert mm(mm(transpose(t), raw_metric), t) == raw_metric
    assert mm(mm(transpose(P), raw_metric), P) == B
    assert mm(mm(transpose(A), B), A) == B
    assert mm(mm(transpose(L), B), L) == scale(B, 5)
    assert mm(L, A) == mm(A, L) and mm(N, A) == mm(A, N)
    assert mm(N, L) == mm(L, N) == scale(eye(4), 5)
    assert N == mm(power(A, 2), L)
    assert L == mm(difference(eye(4), A), difference(eye(4), power(A, 2)))
    assert determinant(L) == 25
    hermite_change = ((1, 1, 1, 1), (2, 1, 2, 1), (0, -1, 1, 0), (-5, -2, -3, -1))
    hermite = ((5, 3, 0, 0), (0, 1, 0, 0), (0, 0, 5, 3), (0, 0, 0, 1))
    assert determinant(hermite_change) == 1 and mm(L, hermite_change) == hermite
    split_basis = tuple(P[i] + S[i] for i in range(6))
    split_numerator = ((2, -3, 1, 1, 0, 0), (-1, -1, 2, 2, 0, 0),
                       (0, 0, 0, 0, 5, 0), (0, 0, 0, 0, 0, 5),
                       (2, 2, 1, 1, 0, 0), (1, 1, 3, -2, 0, 0))
    assert mm(split_numerator, split_basis) == mm(split_basis, split_numerator) == scale(eye(6), 5)
    assert abs(determinant(split_basis)) == 5
    split_metric = mm(mm(transpose(split_basis), raw_metric), split_basis)
    expected_split_metric = tuple(B[i] + (0, 0) for i in range(4)) + (
        (0, 0, 0, 0, 6, -2), (0, 0, 0, 0, -2, 4))
    assert split_metric == expected_split_metric
    assert mm(D, tuple(row[:2] for row in S[:4])) == ((2, 1), (-3, 1), (1, -2))
    assert sum(quadratic(K, v) for v in R) == 18
    assert sum(quadratic(K, v) for v in AM) == 20
    assert vector_sum(R) == vector_sum(AM) == (1, -2, 1, 0)
    assert tuple(map(sum, R)) == (0, 0, 0)
    assert tuple(map(sum, AM)) == (1, -1, 0)


def finite_domain():
    for x in product((-1, 0, 1), repeat=4):
        h = active_energy(x)
        assert 2*h == quadratic(B, x) and h >= 0
        delta = 4*h - 2
        budgets = sorted({0, 1, 2, max(0, delta-1), max(0, delta), max(0, delta+1)})
        for static in ((0, 0), (1, 0), (0, 1), (1, -2)):
            high, low = join_field(mv(L, x), static), join_field(x, static)
            spectators = spectators_for(static)
            variants = (spectators, (vector_add(spectators[0], (1, 0, 0, 0)),) + spectators[1:])
            for variant, b in enumerate(variants):
                for r in budgets:
                    sr, sa = (R, b, high, r), (AM, b, low, r)
                    assert defect(sr) == defect(sa) == (-variant, 0, 0)
                    er = (AM, b, low, r+delta) if r+delta >= 0 else sr
                    ea = (R, b, high, r-delta) if r-delta >= 0 else sa
                    assert gate(sr) == er and gate(sa) == ea
                    audit_state(sr)
                    audit_state(sa)
    for r, expected in ((0, (24, 601)), (2, (25, 600))):
        switched = fixed = members = 0
        for y in product(range(5), repeat=4):
            inverse = image_inverse(y)
            divisible = all(v % 5 == 0 for v in mv(N, y))
            assert (inverse is not None) == divisible
            members += divisible
            state = (R, ZERO_MATTER, join_field(y, (0, 0)), r)
            result = gate(state)
            switched += result != state
            fixed += result == state
            audit_state(state)
        assert members == 25 and (switched, fixed) == expected


def witnesses():
    for static, expected_energy in (((0, 0), 23), ((1, 0), 110)):
        spectators = spectators_for(static)
        high, low = join_field(mv(L, W), static), join_field(W, static)
        initial = (R, spectators, high, 0)
        target = (AM, spectators, low, 2)
        assert gate(initial) == target and gate(target) == initial
        assert energy(initial) == energy(target) == expected_energy
        if static == (1, 0):
            assert high == (2, 2, -2, -1, 1, 2) and low == (1, 1, 0, 1, 1, 0)
            assert mv(D, high[:4]) == mv(D, low[:4]) == (2, -3, 1)
            assert sum(quadratic(K, b) for b in spectators) == 84
            assert field_energy(high) == 8 and field_energy(low) == 4
            assert energy(initial) - 84 == 26
            erased_static = (AM, spectators, join_field(W, (0, 0)), 2)
            assert defect(erased_static) == (-2, 3, -1) != defect(target)
        seen = []
        current = initial
        for k in range(11):
            phase = mv(power(A, k), W)
            predicted = ((R, spectators, join_field(mv(L, phase), static), 0) if k % 2 == 0
                         else (AM, spectators, join_field(phase, static), 2))
            assert current == predicted and energy(current) == expected_energy
            assert defect(current) == (0, 0, 0)
            if k == 5:
                assert current == gate(initial)
            if k == 10:
                assert current == initial
            else:
                seen.append(current)
                current = cell_step(current)
        assert len(set(seen)) == 10
    high, low = join_field(mv(L, W), (0, 0)), join_field(W, (0, 0))
    for r in (0, 1):
        state = (AM, ZERO_MATTER, low, r)
        assert gate(state) == state
        audit_state(state)
    assert gate((AM, ZERO_MATTER, low, 2)) == (R, ZERO_MATTER, high, 0)
    for r in (0, 1):
        state = (R, ZERO_MATTER, ZERO6, r)
        assert gate(state) == state
    assert gate((R, ZERO_MATTER, ZERO6, 2)) == (AM, ZERO_MATTER, ZERO6, 0)
    assert gate((AM, ZERO_MATTER, ZERO6, 0)) == (R, ZERO_MATTER, ZERO6, 2)
    for y in ((0, 0, 1, -2), (0, 0, 1, 1)):
        state = (R, ZERO_MATTER, join_field(y, (0, 0)), 100)
        assert image_inverse(y) is None and gate(state) == state
        audit_state(state)
    assert active_energy((0, 0, 1, -2)) == 5
    assert image_inverse((0, 0, 1, 2)) == (1, 0, -1, 1)
    nonsplit = (R, ((1, 0, 0, 0), (-1, 0, 0, 0), ZERO4), (1, 0, 0, 0, 0, 0), 100)
    assert defect(nonsplit) == (0, 0, 0) and split_field(nonsplit[2]) is None
    assert gate(nonsplit) == nonsplit
    audit_state(nonsplit)
    off = (ZERO_MATTER, (AM[1], AM[0], AM[2]), ((0, 1, -2, 1), ZERO4, ZERO4))
    for m, z, r in product(off, (high, low), (0, 2, 100)):
        state = (m, ZERO_MATTER, z, r)
        assert gate(state) == state
        audit_state(state)
    first = (R, ZERO_MATTER, high, 0)
    lost_surplus = (AM, ZERO_MATTER, low, 0)
    clipped_reverse = (R, ZERO_MATTER, high, 0)
    assert energy(first) - energy(lost_surplus) == 2
    assert energy(clipped_reverse) - energy(lost_surplus) == 2
    assert gate(lost_surplus) == lost_surplus != first
    branch_r = (R, ZERO_MATTER, ZERO6, 0)
    branch_a = (AM, ZERO_MATTER, ZERO6, 0)
    assert branch_r[1:] == branch_a[1:]
    assert gate(branch_r)[1:] != gate(branch_a)[1:]


def main():
    root = Path(__file__).resolve().parents[2]
    sources = {
        'canon/CANON.md': 'b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f',
        'canon/REGISTRY.tsv': 'a2abce1a4538785ac6a7c7874c2366a3531d460027188510394930c6d222559a',
        'canon/EVIDENCE.tsv': '1258ea3dd14a5e2b512b69b08ac647626d4fac169a1ba0b6cd770832bb735600',
        'canon/DEPENDENCIES.tsv': 'c1b0cee2b9e320ed05ba4004da3a2265cbd2bbafe45dd18f59fb29790d477214',
        'canon/GATES.tsv': '85f7db365ff38988dbf2a994f4d8d0ba380ac00d368bcc50e4313daee9aff744',
        'notes/INTEGER-AUTOMATON-COMPOSITION-PROGRAM.md': '354c4b5292c89ab521654a642f056c39f4c99e688b5e34891369c23980d9dfd7',
    }
    for name, digest in sources.items():
        assert sha256((root/name).read_bytes()).hexdigest() == digest, name
    certificates()
    finite_domain()
    witnesses()
    print('PRIMARY PASS: local L5 coupling; exact account, inverse and pointwise Gauss defect')


if __name__ == '__main__':
    main()
