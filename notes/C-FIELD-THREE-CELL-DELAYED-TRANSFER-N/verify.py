#!/usr/bin/env python3
"""Exact primary audit of the frozen NON-CANONICAL three-cell delayed law."""

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
LAYERS = (('G0', 'G1', 'G2'), ('A0', 'A1'), ('B0', 'B1'), ('F0', 'F1', 'F2'))
BA = (LAYERS[0], LAYERS[2], LAYERS[1], LAYERS[3])
SWEEP = (LAYERS[0], ('A0',), ('B0',), ('A1',), ('B1',), LAYERS[3])


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


def cell_energy(cell):
    m, b, z, r = cell
    return sum(matter_energy(v) for v in m+b) + raw_energy(z) + r


def rho(cell):
    m, b, _, _ = cell
    return (sum(b[0])+sum(map(sum, m)), sum(b[1]), sum(b[2]))


def defect(cell):
    return tuple(a-b for a, b in zip(mv(D, cell[2][:4]), rho(cell)))


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


def energy(state):
    return sum(cell_energy(c) for c in state[:3]) + sum(state[3:])


def resources(state):
    return tuple(c[3] for c in state[:3]) + state[3:]


def legal(state):
    assert len(state) == 5
    values = []
    for m, b, z, r in state[:3]:
        assert len(m) == len(b) == 3 and all(len(v) == 4 for v in m+b)
        assert len(z) == 6 and r >= 0
        values.extend(v for row in m+b for v in row)
        values.extend(z+(r,))
    values.extend(state[3:])
    assert len(values) == 95 and all(type(v) is int for v in values)
    assert all(q >= 0 for q in state[3:])


def primitive(state, label, inverse=False):
    result = list(state)
    kind, j = label[0], int(label[1])
    if kind in ('G', 'F'):
        result[j] = gate(state[j]) if kind == 'G' else free(state[j], inverse)
    else:
        assert kind in ('A', 'B') and j in (0, 1)
        i = j if kind == 'A' else j+1
        result[i] = with_resource(state[i], state[3+j])
        result[3+j] = state[i][3]
    return tuple(result)


def labels(layers=LAYERS, reverse_within=False, cut=None):
    return tuple(label for layer in layers
                 for label in (reversed(layer) if reverse_within else layer)
                 if not (label[0] in ('A', 'B') and int(label[1]) == cut))


def evolve(state, inverse=False, layers=LAYERS, reverse_within=False, cut=None):
    order = labels(layers, reverse_within, cut)
    for label in reversed(order) if inverse else order:
        state = primitive(state, label, inverse)
    return state


def invariants(before, after):
    legal(after)
    assert energy(after) == energy(before) >= 0
    for old, new in zip(before[:3], after[:3]):
        assert old[1] == new[1] and vector_sum(old[0]) == vector_sum(new[0])
        assert rho(old) == rho(new) and defect(old) == defect(new)


def audit_primitive(before, label):
    after = primitive(before, label)
    invariants(before, after)
    kind, j = label[0], int(label[1])
    if kind in ('G', 'F'):
        assert before[3:] == after[3:]
        for i in range(3):
            if i != j:
                assert before[i] == after[i]
        if kind == 'G':
            audit_gate(before[j])
            assert primitive(after, label) == before
        else:
            assert before[j][:2] == after[j][:2] and before[j][3] == after[j][3]
            assert primitive(after, label, True) == before
    else:
        i = j if kind == 'A' else j+1
        for k in range(3):
            assert before[k][:3] == after[k][:3]
            if k != i:
                assert before[k] == after[k]
        assert before[4-j] == after[4-j]
        old_r, old_q = before[i][3], before[3+j]
        assert (after[i][3], after[3+j]) == (old_q, old_r)
        assert cell_energy(after[i])-cell_energy(before[i]) == old_q-old_r
        assert after[3+j]-old_q == old_r-old_q
        assert primitive(after, label) == before
    return after


def audit(state, cut=None, layers=LAYERS):
    legal(state)
    current = state
    boundaries = [state]
    for layer in layers:
        for label in layer:
            if not (label[0] in ('A', 'B') and int(label[1]) == cut):
                current = audit_primitive(current, label)
        invariants(state, current)
        boundaries.append(current)
    assert current == evolve(state, cut=cut, layers=layers)
    assert evolve(current, True, layers=layers, cut=cut) == state
    inverse = evolve(state, True, layers=layers, cut=cut)
    assert evolve(inverse, layers=layers, cut=cut) == state
    invariants(state, inverse)
    assert current == evolve(state, layers=layers, reverse_within=True, cut=cut)
    if layers == LAYERS and cut is None:
        a, b, c, p, q = resources(boundaries[1])
        assert resources(boundaries[2]) == (p, q, c, a, b)
        assert resources(boundaries[3]) == (p, a, b, q, c)
    return current


def finite_audit():
    high, low = join(mv(L, W)), join(W)
    core = ((R, Z6), (R, high), (AM, low), (ZM, Z6))
    baseline = ((R, high), (ZM, Z6), (R, Z6))
    exceptions = ((AM, Z6), (R, join(mv(L, V))), (AM, join(V)),
                  (R, join((0, 0, 1, -2))), (R, (1, 0, 0, 0, 0, 0)),
                  ((AM[1], AM[0], AM[2]), low), (((0, 1, -2, 1), Z4, Z4), high))
    triples = list(product(core, repeat=3))
    for exceptional, i in product(exceptions, range(3)):
        row = list(baseline)
        row[i] = exceptional
        triples.append(tuple(row))
    assert len(triples) == 85
    stocks = ((0, 0, 0), (1, 2, 5), (2, 5, 6), (5, 6, 7), (6, 7, 1), (7, 1, 2))
    channels = ((0, 0), (1, 2), (2, 1), (3, 4))
    backgrounds = ((((0, 0),)*3, (0, 0, 0)),
                   (((1, 0), (1, 0), (0, 1)), (0, 0, 0)),
                   (((1, 0), (1, 0), (0, 1)), (1, -1, 2)))
    count = 0
    for triple, stock, qs, (statics, errors) in product(triples, stocks, channels, backgrounds):
        cells = tuple(prepared_cell(*template, static, r, error)
                      for template, static, r, error in zip(triple, statics, stock, errors))
        for cell, error in zip(cells, errors):
            assert defect(cell) == (-error, 0, 0)
        audit(cells+qs)
        count += 1
    assert count == 6120


def preparation(statics=((0, 0),)*3, middle=ZM):
    return (prepared_cell(R, join(mv(L, W)), statics[0]),
            prepared_cell(middle, Z6, statics[1]),
            prepared_cell(R, Z6, statics[2]), 0, 0)


def expected_state(initial, k, matter, stock, source_high=None):
    # Exposed complete-state oracle from the frozen symbolic boundary table.
    phase = mv(power(A, k), W)
    high = k == 0 if source_high is None else source_high
    raw = join(mv(L, phase) if high else phase)
    static = split(initial[0][2])[1]
    source = (matter[0], initial[0][1], plus(raw, mv(S, static)), stock[0])
    middle = (matter[1], initial[1][1], initial[1][2], stock[1])
    target = (matter[2], initial[2][1], initial[2][2], stock[2])
    return source, middle, target, stock[3], stock[4]


def explicit_witnesses():
    boundary_stocks = ((0, 0, 0, 0, 0), (0, 2, 0, 0, 0),
                       (0, 0, 2, 0, 0), (0, 0, 0, 0, 0))
    fields = ((1, -1, 0, 0, -1, 1), (-1, 0, 1, 1, 0, -2), (1, 0, -1, -1, -1, 1))
    for k, raw in enumerate(fields, 1):
        assert join(mv(power(A, k), W)) == raw
    for statics, base in ((((0, 0),)*3, (23, 0, 18)),
                          (((1, 0), (1, 0), (0, 1)), (110, 87, 56))):
        initial = preparation(statics)
        current = initial
        assert energy(initial) == sum(base)
        for k in range(4):
            matter = (R if k == 0 else AM, ZM, AM if k == 3 else R)
            predicted = expected_state(initial, k, matter, boundary_stocks[k])
            assert current == predicted
            expected_energy = (base if k == 0 else
                               (base[0]-2, base[1]+(2 if k == 1 else 0), base[2]+(2 if k >= 2 else 0)))
            assert tuple(cell_energy(c) for c in current[:3])+current[3:] == expected_energy+(0, 0)
            invariants(initial, current)
            if k < 3:
                before = current
                current = audit(current)
                if k in (0, 1):
                    after_g = before
                    for label in LAYERS[0]:
                        after_g = primitive(after_g, label)
                    after_a = after_g
                    for label in LAYERS[1]:
                        after_a = primitive(after_a, label)
                    assert after_a[3+k] == 2
                    assert after_a[k][3] == 0
        assert cell_energy(current[0])-cell_energy(initial[0]) == -2
        assert cell_energy(current[2])-cell_energy(initial[2]) == 2
        assert cell_energy(current[1]) == cell_energy(initial[1])
        assert current[3:] == initial[3:]
        if statics[0] == (1, 0):
            assert tuple(rho(c) for c in current[:3]) == ((2, -3, 1), (2, -3, 1), (1, 1, -2))
            assert cell_energy(initial[1]) == 84+3
        for cut in (0, 1):
            state = initial
            for k in range(4):
                if cut == 0:
                    high = k % 2 == 0
                    matter = (R if high else AM, ZM, R)
                    stock = (0 if high else 2, 0, 0, 0, 0)
                else:
                    high = k == 0
                    matter = (R if high else AM, ZM, R)
                    stock = ((0, 0, 0, 0, 0), (0, 2, 0, 0, 0),
                             (0, 0, 0, 2, 0), (2, 0, 0, 0, 0))[k]
                assert state == expected_state(initial, k, matter, stock, high)
                assert state[2] == initial[2] and state[3+cut] == initial[3+cut]
                invariants(initial, state)
                if k < 3:
                    state = audit(state, cut=cut)

    paid = preparation(middle=R)
    assert energy(paid) == 59
    current = paid
    for k in range(3):
        matter = (R if k == 0 else AM, AM if k == 2 else R, R)
        stock = (0, 2 if k == 1 else 0, 0, 0, 0)
        assert current == expected_state(paid, k, matter, stock)
        if k < 2:
            current = audit(current)

    off = (prepared_cell(R, join((0, 0, 1, -2))),
           prepared_cell(ZM, Z6), prepared_cell(R, Z6), 0, 0)
    assert raw_energy(off[0][2]) == 5 and energy(off) == 41
    current = off
    for k in range(4):
        assert gate(current[0]) == current[0]
        assert current[0][0] == R and resources(current) == (0,)*5
        assert current[1:] == off[1:]
        assert current[0][2] == join(mv(power(A, k), (0, 0, 1, -2)))
        if k == 1:
            assert current[0][2] != off[0][2]
        if k < 3:
            current = audit(current)


def occupied_and_wrong_controls():
    empty = (prepared_cell(ZM, Z6),)*3+(0, 0)
    def set_stocks(values):
        return tuple(with_resource(empty[i], values[i]) for i in range(3))+tuple(values[3:])
    occupied = set_stocks((0, 1, 2, 3, 4))
    assert energy(occupied) == 10
    assert resources(audit(occupied)) == (3, 0, 1, 4, 2)
    assert resources(audit(occupied, layers=BA)) == (1, 2, 4, 0, 3)
    for cut in (0, 1):
        result = audit(occupied, cut=cut)
        expected = ((0, 4, 1, 3, 2), (3, 0, 2, 1, 4))[cut]
        assert result == set_stocks(expected)
        assert result[3+cut] == occupied[3+cut]

    funded = primitive(preparation(), 'G0')
    copied = funded[:3]+(funded[0][3], funded[4])
    assert energy(copied) == energy(funded)+2
    for j in (0, 1):
        def destructive_send(state):
            out = list(state)
            out[j] = with_resource(state[j], 0)
            out[3+j] = state[j][3]
            return tuple(out)
        x = [0]*5
        x[j], x[3+j] = 2, 1
        a = set_stocks(x)
        x[3+j] = 0
        b = set_stocks(x)
        assert a != b and destructive_send(a) == destructive_send(b)
        assert energy(destructive_send(a)) == energy(a)-1
        def destructive_receive(state):
            out = list(state)
            out[j+1] = with_resource(state[j+1], state[3+j])
            out[3+j] = 0
            return tuple(out)
        x = [0]*5
        x[j+1], x[3+j] = 1, 2
        a = set_stocks(x)
        x[j+1] = 0
        b = set_stocks(x)
        assert a != b and destructive_receive(a) == destructive_receive(b)
        assert energy(destructive_receive(a)) == energy(a)-1

    initial = preparation()
    for schedule, stocks in ((BA, ((0,)*5, (0, 0, 0, 2, 0), (0, 0, 0, 0, 2), (0, 0, 2, 0, 0))),
                             (SWEEP, ((0,)*5, (0, 0, 2, 0, 0), (0,)*5))):
        current = initial
        for k, stock in enumerate(stocks):
            matter = (R if k == 0 else AM, ZM, AM if schedule == SWEEP and k == 2 else R)
            assert current == expected_state(initial, k, matter, stock)
            if k < len(stocks)-1:
                current = audit(current, layers=schedule)
        assert evolve(initial, layers=schedule) != evolve(initial)


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
    occupied_and_wrong_controls()
    print('PRIMARY PASS: three-cell delay; 6120 states; full inverse, energy and Gauss')


if __name__ == '__main__':
    main()
