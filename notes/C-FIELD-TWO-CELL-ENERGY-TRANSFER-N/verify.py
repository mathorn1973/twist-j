#!/usr/bin/env python3
"""Exact primary audit of the frozen NON-CANONICAL two-cell law."""

from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path


C = ((1, -1), (-1, 0), (0, 1), (0, 1))
D = ((1, 1, 1, 0), (-1, -1, 0, -1), (0, 0, -1, 1))
K = ((6, 2, -1, 2), (2, 6, 2, -1), (-1, 2, 6, 2), (2, -1, 2, 6))
A = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
B = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
L = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
N = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
P = ((1, -1, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0),
     (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
S = ((1, 0), (1, 0), (0, 1), (1, -1), (0, 0), (0, 0))
Z4, Z6 = (0,)*4, (0,)*6
ZM = (Z4,)*3
R = ((1, -2, 1, 0), Z4, Z4)
AM = ((1, 0, 0, 0), (0, -1, 0, 0), (0, -1, 1, 0))
W, V = (0, 0, 1, 0), (0, 0, 1, 1)
STAGES = ('Gs', 'Xs', 'Xt', 'Gt', 'Fs', 'Ft')


def tr(matrix):
    return tuple(zip(*matrix))


def ident(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def mv(matrix, vector):
    return tuple(sum(a*b for a, b in zip(row, vector)) for row in matrix)


def mm(left, right):
    return tuple(tuple(sum(a*b for a, b in zip(row, col)) for col in tr(right)) for row in left)


def mul(k, matrix):
    return tuple(tuple(k*v for v in row) for row in matrix)


def sub(left, right):
    return tuple(tuple(a-b for a, b in zip(x, y)) for x, y in zip(left, right))


def power(matrix, n):
    result = ident(len(matrix))
    for _ in range(n):
        result = mm(result, matrix)
    return result


def det(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    answer = Fraction(1)
    for i in range(len(rows)):
        pivot = next((j for j in range(i, len(rows)) if rows[j][i]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            rows[i], rows[pivot] = rows[pivot], rows[i]
            answer = -answer
        value = rows[i][i]
        answer *= value
        for j in range(i+1, len(rows)):
            ratio = rows[j][i]/value
            rows[j] = [a-ratio*b for a, b in zip(rows[j], rows[i])]
    return answer


def positive(matrix):
    assert matrix == tr(matrix)
    assert all(det(tuple(row[:n] for row in matrix[:n])) > 0 for n in range(1, len(matrix)+1))


def plus(a, b):
    return tuple(x+y for x, y in zip(a, b))


def vector_sum(matter):
    return tuple(sum(column) for column in zip(*matter))


def quadratic(matrix, vector):
    return sum(a*b for a, b in zip(vector, mv(matrix, vector)))


@lru_cache(None)
def matter_energy(v):
    return quadratic(K, v)


@lru_cache(None)
def active_energy(v):
    twice = quadratic(B, v)
    assert twice % 2 == 0
    return twice//2


@lru_cache(None)
def raw_energy(z):
    e, m = z[:4], z[4:]
    return sum(v*v for v in z) + sum(a*b for a, b in zip(e, mv(C, m)))


def join(x, static=(0, 0)):
    return plus(mv(P, x), mv(S, static))


@lru_cache(None)
def split(z):
    e0, e1, e2, e3, c, d = z
    g = 2*e0-3*e1+e2+e3
    if g % 5:
        return None
    numerators = (g, -e0-e1+2*e2+2*e3, 2*e0+2*e1+e2+e3, e0+e1+3*e2-2*e3)
    assert all(v % 5 == 0 for v in numerators)
    a, b, u, v = (n//5 for n in numerators)
    assert join((a, b, c, d), (u, v)) == z
    return (a, b, c, d), (u, v)


def image_inverse(y):
    a, b, c, d = y
    if (a+2*b) % 5 or (c+2*d) % 5:
        return None
    numerator = mv(N, y)
    assert all(v % 5 == 0 for v in numerator)
    x = tuple(v//5 for v in numerator)
    assert mv(L, x) == y
    return x


def gate(cell):
    matter, spectators, raw, resource = cell
    if matter not in (R, AM):
        return cell
    parts = split(raw)
    if parts is None:
        return cell
    y, static = parts
    if matter == R:
        x = image_inverse(y)
        if x is None:
            return cell
        output = (AM, spectators, join(x, static), resource+4*active_energy(x)-2)
    else:
        output = (R, spectators, join(mv(L, y), static), resource+2-4*active_energy(y))
    return output if output[3] >= 0 else cell


def field(raw, inverse=False):
    e, m = raw[:4], raw[4:]
    if inverse:
        old_m = plus(m, mv(tr(C), e))
        return tuple(a-b for a, b in zip(e, mv(C, old_m))) + old_m
    new_e = plus(e, mv(C, m))
    return new_e + tuple(a-b for a, b in zip(m, mv(tr(C), new_e)))


def free(cell, inverse=False):
    return cell[:2] + (field(cell[2], inverse), cell[3])


def with_resource(cell, value):
    return cell[:3] + (value,)


def step_stage(state, label, inverse=False):
    source, target, channel = state
    if label == 'Gs':
        return gate(source), target, channel
    if label == 'Gt':
        return source, gate(target), channel
    if label == 'Fs':
        return free(source, inverse), target, channel
    if label == 'Ft':
        return source, free(target, inverse), channel
    if label == 'Xs':
        return with_resource(source, channel), target, source[3]
    assert label == 'Xt'
    return source, with_resource(target, channel), target[3]


def evolve(state, inverse=False, contacts=True):
    labels = reversed(STAGES) if inverse else STAGES
    for label in labels:
        if contacts or label not in ('Xs', 'Xt'):
            state = step_stage(state, label, inverse)
    return state


def cell_energy(cell):
    m, b, z, r = cell
    return sum(matter_energy(v) for v in m+b) + raw_energy(z) + r


def energy(state):
    return cell_energy(state[0]) + cell_energy(state[1]) + state[2]


def rho(cell):
    m, b, _, _ = cell
    return (sum(b[0])+sum(map(sum, m)), sum(b[1]), sum(b[2]))


def defect(cell):
    return tuple(a-b for a, b in zip(mv(D, cell[2][:4]), rho(cell)))


def legal(state):
    source, target, channel = state
    values = []
    for m, b, z, r in (source, target):
        assert len(m) == len(b) == 3 and all(len(v) == 4 for v in m+b)
        assert len(z) == 6 and r >= 0
        values.extend(v for row in m+b for v in row)
        values.extend(z+(r,))
    values.append(channel)
    assert len(values) == 63 and all(type(v) is int for v in values) and channel >= 0


def invariants(before, after):
    legal(after)
    assert energy(after) == energy(before) >= 0
    for old, new in zip(before[:2], after[:2]):
        assert new[1] == old[1] and vector_sum(new[0]) == vector_sum(old[0])
        assert rho(new) == rho(old) and defect(new) == defect(old)


def audit_gate(cell):
    output = gate(cell)
    assert gate(output) == cell
    m, b, z, r = cell
    parts = split(z)
    if m not in (R, AM) or parts is None:
        assert output == cell
        return
    y, s = parts
    x = image_inverse(y) if m == R else y
    if x is None:
        assert output == cell
        return
    other_m = AM if m == R else R
    other_z = join(x if m == R else mv(L, x), s)
    # Independent resource oracle uses the complete raw-field energy difference.
    old_bare = sum(matter_energy(v) for v in m) + raw_energy(z)
    new_bare = sum(matter_energy(v) for v in other_m) + raw_energy(other_z)
    remaining = r+old_bare-new_bare
    expected = (other_m, b, other_z, remaining) if remaining >= 0 else cell
    assert output == expected


def audit(state):
    legal(state)
    current = state
    for label in STAGES:
        before = current
        current = step_stage(before, label)
        invariants(before, current)
        index = 0 if label.endswith('s') else 1
        other = 1-index
        assert current[other] == before[other]
        if label.startswith('X'):
            assert current[index][:3] == before[index][:3]
            assert current[index][3] == before[2] and current[2] == before[index][3]
            assert step_stage(current, label) == before
            assert cell_energy(current[index])-cell_energy(before[index]) == before[2]-before[index][3]
            assert current[2]-before[2] == before[index][3]-before[2]
        elif label.startswith('G'):
            assert current[2] == before[2]
            audit_gate(before[index])
        else:
            assert current[2] == before[2]
            assert current[index][:2] == before[index][:2] and current[index][3] == before[index][3]
            assert step_stage(current, label, True) == before
    assert evolve(current, inverse=True) == state
    assert evolve(evolve(state, inverse=True)) == state
    invariants(state, evolve(state, contacts=False))
    return current


def certificates():
    assert D == tuple(tuple(int(v == tail)-int(v == head)
                            for tail, head in ((0, 1), (0, 1), (0, 2), (2, 1))) for v in range(3))
    assert mm(D, C) == ((0, 0),)*3
    gram = mm(tr(C), C)
    assert gram == ((2, -1), (-1, 3))
    assert sub(mul(4, ident(2)), gram) == ((2, 1), (1, 1))
    positive(K)
    positive(B)
    for v, value in (((1, 1, 1, 1), 9), ((1, -1, 1, -1), 1),
                     ((1, 0, -1, 0), 7), ((0, 1, 0, -1), 7)):
        assert mv(K, v) == tuple(value*x for x in v)
    basis = ((1, 1, 1, 1), (1, -1, 1, -1), (1, 0, -1, 0), (0, 1, 0, -1))
    assert det(basis) != 0
    assert power(A, 5) == ident(4) and mm(mm(tr(A), B), A) == B
    assert L == mm(sub(ident(4), A), sub(ident(4), power(A, 2)))
    assert N == mm(power(A, 2), L) and mm(A, L) == mm(L, A)
    assert mm(L, N) == mm(N, L) == mul(5, ident(4))
    assert mm(mm(tr(L), B), L) == mul(5, B) and det(L) == 25
    vh = ((1, 1, 1, 1), (2, 1, 2, 1), (0, -1, 1, 0), (-5, -2, -3, -1))
    assert det(vh) == 1
    assert mm(L, vh) == ((5, 3, 0, 0), (0, 1, 0, 0), (0, 0, 5, 3), (0, 0, 0, 1))
    combined = tuple(p+s for p, s in zip(P, S))
    numerator = ((2, -3, 1, 1, 0, 0), (-1, -1, 2, 2, 0, 0),
                 (0, 0, 0, 0, 5, 0), (0, 0, 0, 0, 0, 5),
                 (2, 2, 1, 1, 0, 0), (1, 1, 3, -2, 0, 0))
    assert abs(det(combined)) == 5
    assert mm(combined, numerator) == mm(numerator, combined) == mul(5, ident(6))
    for row, multiple in zip(numerator, (1, 2, 0, 0, 1, 3)):
        assert all((v-multiple*g) % 5 == 0 for v, g in zip(row, numerator[0]))
    raw_metric = tuple(tuple(2*int(i == j) for j in range(4))+C[i] for i in range(4))
    raw_metric += tuple(row+tuple(2*int(i == j) for j in range(2)) for i, row in enumerate(tr(C)))
    block = tuple(row+(0, 0) for row in B)+tuple((0,)*4+row for row in ((6, -2), (-2, 4)))
    positive(raw_metric)
    assert mm(mm(tr(combined), raw_metric), combined) == block
    assert mm(D, P[:4]) == ((0,)*4,)*3 and mm(D, S[:4]) == ((2, 1), (-3, 1), (1, -2))
    transform = tr(tuple(field(unit) for unit in ident(6)))
    inverse = tr(tuple(field(unit, True) for unit in ident(6)))
    assert mm(transform, inverse) == mm(inverse, transform) == ident(6)
    assert power(transform, 5) == ident(6)
    assert mm(mm(tr(transform), raw_metric), transform) == raw_metric
    assert mm(transform, P) == mm(P, A) and mm(transform, S) == S
    extended_d = tuple(row+(0, 0) for row in D)
    assert mm(extended_d, transform) == extended_d
    assert sum(matter_energy(v) for v in R) == 18 and sum(matter_energy(v) for v in AM) == 20
    assert vector_sum(R) == vector_sum(AM) and sum(map(sum, R)) == 0
    assert active_energy(W) == 1 and active_energy(V) == 2
    count = 0
    for y in product(range(5), repeat=4):
        admitted = image_inverse(y)
        assert (admitted is not None) == all(v % 5 == 0 for v in mv(N, y))
        count += admitted is not None
    assert count == 25


def prepared_cell(m, raw, static=(0, 0), resource=0, error=0):
    z = plus(raw, mv(S, static))
    values = list(mv(D, z[:4]))
    values[0] += error
    b = tuple((value, 0, 0, 0) for value in values)
    return m, b, z, resource


def finite_audit():
    high, low = join(mv(L, W)), join(W)
    catalog = ((R, Z6), (AM, Z6), (R, high), (AM, low),
               (R, join(mv(L, V))), (AM, join(V)), (R, join((0, 0, 1, -2))),
               (R, (1, 0, 0, 0, 0, 0)), (ZM, high), ((AM[1], AM[0], AM[2]), low),
               (((0, 1, -2, 1), Z4, Z4), high))
    backgrounds = (((0, 0), (0, 0), 0, 0), ((1, 0), (0, 1), 0, 0), ((1, 0), (0, 1), 1, -1))
    pairs = ((0, 0), (2, 1), (1, 2), (5, 6), (7, 5), (6, 7))
    count = 0
    for a, b, pair, q, background in product(catalog, catalog, pairs, (0, 1, 2), backgrounds):
        sa, sb, ea, eb = background
        left = prepared_cell(*a, sa, pair[0], ea)
        right = prepared_cell(*b, sb, pair[1], eb)
        assert defect(left) == (-ea, 0, 0) and defect(right) == (-eb, 0, 0)
        audit((left, right, q))
        count += 1
    assert count == 6534


def explicit_witnesses():
    patterns = ((R, R, 0, 0, 0), (AM, AM, 0, 0, 0), (AM, R, 0, 2, 0),
                (AM, R, 0, 0, 2), (AM, R, 2, 0, 0), (R, R, 0, 0, 0))
    for ss, st, source_e, target_e in (((0, 0), (0, 0), 23, 18), ((1, 0), (0, 1), 110, 56)):
        initial = (prepared_cell(R, join(mv(L, W)), ss), prepared_cell(R, Z6, st), 0)
        assert energy(initial) == source_e+target_e
        triples = ((source_e, target_e, 0), (source_e, target_e, 0),
                   (source_e-2, target_e, 2), (source_e-2, target_e+2, 0),
                   (source_e-2, target_e+2, 0), (source_e-2, target_e+2, 0),
                   (source_e-2, target_e+2, 0))
        state = initial
        trace = [state]
        for label in STAGES:
            state = step_stage(state, label)
            trace.append(state)
        for current, expected in zip(trace, triples):
            assert (cell_energy(current[0]), cell_energy(current[1]), current[2]) == expected
            invariants(initial, current)
        source_low = (AM, initial[0][1], join(W, ss), 2)
        assert trace[1] == (source_low, initial[1], 0)
        assert trace[2] == (with_resource(source_low, 0), initial[1], 2)
        assert trace[3] == (with_resource(source_low, 0), with_resource(initial[1], 2), 0)
        receiver_done = (AM, initial[1][1], initial[1][2], 0)
        assert trace[4] == (with_resource(source_low, 0), receiver_done, 0)
        expected_final = (free(with_resource(source_low, 0)), receiver_done, 0)
        assert audit(initial) == state == expected_final
        control = evolve(initial, contacts=False)
        assert control == (free(source_low), initial[1], 0)
        assert state[0][3] == state[1][3] == state[2] == 0 and state[1][0] == AM
        if ss == (1, 0):
            assert state[0][2] == (2, 0, 0, 1, -1, 1) and state[1][2] == (0, 0, 1, -1, 0, 0)
            assert rho(state[0]) == (2, -3, 1) and rho(state[1]) == (1, 1, -2)
        current = initial
        for k, (ms, mt, rs, rt, q) in enumerate(patterns):
            phase = mv(power(A, k), W)
            source_z = join(mv(L, phase) if k in (0, 5) else phase, ss)
            predicted = ((ms, initial[0][1], source_z, rs), (mt, initial[1][1], initial[1][2], rt), q)
            assert current == predicted
            invariants(initial, current)
            if 0 < k < 5:
                assert current != initial
            if k < 5:
                current = evolve(current)
        assert current == initial
    offimage = (prepared_cell(R, join((0, 0, 1, -2))), prepared_cell(R, Z6), 0)
    assert raw_energy(offimage[0][2]) == 5 and energy(offimage) == 41
    assert gate(offimage[0]) == offimage[0]
    assert evolve(offimage)[1] == offimage[1]
    assert evolve(offimage)[0][2] != offimage[0][2]
    base = (prepared_cell(R, Z6, resource=2), prepared_cell(R, Z6, resource=3), 1)
    first = step_stage(base, 'Xs')
    second = step_stage(first, 'Xt')
    assert (base[0][3], base[2], base[1][3]) == (2, 1, 3)
    assert (first[0][3], first[2], first[1][3]) == (1, 2, 3)
    assert (second[0][3], second[2], second[1][3]) == (1, 3, 2)
    assert step_stage(step_stage(second, 'Xt'), 'Xs') == base
    initial = (prepared_cell(R, join(mv(L, W))), prepared_cell(R, Z6), 0)
    funded = step_stage(initial, 'Gs')
    copied = (funded[0], funded[1], funded[0][3])
    assert energy(copied) == energy(funded)+2
    def overwrite_send(state):
        return with_resource(state[0], 0), state[1], state[0][3]
    occupied = funded[:2]+(1,)
    assert overwrite_send(occupied) == overwrite_send(funded)
    assert energy(overwrite_send(occupied)) == energy(occupied)-1
    in_flight = step_stage(funded, 'Xs')
    def overwrite_receive(state):
        return state[0], with_resource(state[1], state[2]), 0
    occupied = (in_flight[0], with_resource(in_flight[1], 1), in_flight[2])
    assert overwrite_receive(occupied) == overwrite_receive(in_flight)
    assert energy(overwrite_receive(occupied)) == energy(occupied)-1
    wrong = initial
    for label in ('Gs', 'Gt', 'Xs', 'Xt', 'Fs', 'Ft'):
        wrong = step_stage(wrong, label)
    invariants(initial, wrong)
    assert wrong[1] == with_resource(initial[1], 2) and wrong[1][0] == R
    assert wrong != evolve(initial)


def main():
    if not __debug__:
        raise RuntimeError('Exact verification requires enabled assertions')
    root = Path(__file__).resolve().parents[2]
    hashes = {
        'canon/CANON.md': 'b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f',
        'canon/REGISTRY.tsv': 'a2abce1a4538785ac6a7c7874c2366a3531d460027188510394930c6d222559a',
        'canon/EVIDENCE.tsv': '1258ea3dd14a5e2b512b69b08ac647626d4fac169a1ba0b6cd770832bb735600',
        'canon/DEPENDENCIES.tsv': 'c1b0cee2b9e320ed05ba4004da3a2265cbd2bbafe45dd18f59fb29790d477214',
        'canon/GATES.tsv': '85f7db365ff38988dbf2a994f4d8d0ba380ac00d368bcc50e4313daee9aff744',
        'notes/INTEGER-AUTOMATON-COMPOSITION-PROGRAM.md': '354c4b5292c89ab521654a642f056c39f4c99e688b5e34891369c23980d9dfd7',
    }
    for name, digest in hashes.items():
        assert sha256((root/name).read_bytes()).hexdigest() == digest, name
    certificates()
    finite_audit()
    explicit_witnesses()
    print('PRIMARY PASS: two-cell transfer; exact work, inverse and pointwise Gauss defect')


if __name__ == '__main__':
    main()
