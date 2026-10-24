#!/usr/bin/env python3
"""Independent exact audit of one PUBLIC / NON-CANONICAL L1 cell law.

Scientific input: the frozen PREREG.md, SHA-256
0cc0e1cffe396d6dbef867549c6bf7634ea1e9c453f8ccec9eb6aab72a2ed753.
No other implementation, predecessor program or measured output is an input.
State equality below is equality of all 31 stored integer coordinates.
"""

from fractions import Fraction
from itertools import combinations, product
from math import gcd


K = ((6, 2, -1, 2), (2, 6, 2, -1),
     (-1, 2, 6, 2), (2, -1, 2, 6))
B = ((4, -2, 2, -1), (-2, 6, -1, 3),
     (2, -1, 2, 0), (-1, 3, 0, 2))
A = ((1, 0, 1, 0), (0, 1, 0, 1),
     (-2, 1, -1, 1), (1, -3, 1, -2))
L = ((1, -3, -1, -2), (-3, 4, -2, 1),
     (0, 5, 1, 2), (5, -5, 2, -1))
N = ((1, 2, 1, 2), (2, -1, 2, -1),
     (0, -5, 1, -3), (-5, 5, -3, 4))
C = ((1, -1), (-1, 0), (0, 1), (0, 1))
R = (1, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
END = (1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 0)
ZERO_B = (0,) * 12


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def transpose(matrix):
    return tuple(zip(*matrix))


def mv(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def mm(left, right):
    return tuple(tuple(sum(a * b for a, b in zip(row, col))
                       for col in transpose(right)) for row in left)


def scale(number, matrix):
    return tuple(tuple(number * value for value in row) for row in matrix)


def difference(left, right):
    return tuple(tuple(a - b for a, b in zip(row_a, row_b))
                 for row_a, row_b in zip(left, right))


def power(matrix, exponent):
    result = eye(len(matrix))
    for _ in range(exponent):
        result = mm(result, matrix)
    return result


def determinant(matrix):
    work = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work))
                      if work[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result = -result
        value = work[col][col]
        result *= value
        for row in range(col + 1, len(work)):
            ratio = work[row][col] / value
            for index in range(col + 1, len(work)):
                work[row][index] -= ratio * work[col][index]
            work[row][col] = Fraction(0)
    return result


def positive(matrix):
    assert matrix == transpose(matrix)
    for size in range(1, len(matrix) + 1):
        assert determinant(tuple(row[:size] for row in matrix[:size])) > 0


def linear_matrix(function, dimension):
    return transpose(tuple(function(unit) for unit in eye(dimension)))


def primitive_columns(matrix):
    width = len(matrix[0])
    divisor = 0
    for indices in combinations(range(len(matrix)), width):
        minor = determinant(tuple(matrix[i] for i in indices))
        assert minor.denominator == 1
        divisor = gcd(divisor, abs(minor.numerator))
    assert divisor == 1


def active(vector):
    a, b, c, d = vector
    return (a - b, -a, b, b, c, d)


def static(pair):
    u, v = pair
    return (u, u, v, u - v, 0, 0)


def field(vector, pair=(0, 0)):
    return tuple(a + b for a, b in zip(active(vector), static(pair)))


def high(vector):
    a, b, c, d = vector
    return (a - 3*b - c - 2*d, -3*a + 4*b - 2*c + d,
            5*b + c + 2*d, 5*a - 5*b + 2*c - d)


def numerator(vector):
    a, b, c, d = vector
    return (a + 2*b + c + 2*d, 2*a - b + 2*c - d,
            -5*b + c - 3*d, -5*a + 5*b - 3*c + 4*d)


def split(raw):
    e0, e1, e2, e3, m0, m1 = raw
    g = 2*e0 - 3*e1 + e2 + e3
    if g % 5:
        return None
    numerators = (g, -e0-e1+2*e2+2*e3,
                  2*e0+2*e1+e2+e3, e0+e1+3*e2-2*e3)
    assert all(value % 5 == 0 for value in numerators)
    a, b, u, v = (value // 5 for value in numerators)
    return (a, b, m0, m1), (u, v)


def image_member(vector):
    a, b, c, d = vector
    return (a + 2*b) % 5 == 0 and (c + 2*d) % 5 == 0


def active_energy(vector):
    a, b, c, d = vector
    return (2*a*a + 3*b*b + c*c + d*d - 2*a*b + 2*a*c
            - a*d - b*c + 3*b*d)


def matter_energy(vector):
    a, b, c, d = vector
    return (6*(a*a+b*b+c*c+d*d) + 4*(a*b+b*c+c*d+d*a)
            - 2*(a*c+b*d))


def raw_energy(raw):
    e0, e1, e2, e3, m0, m1 = raw
    return (sum(value*value for value in raw) + (e0-e1)*m0
            + (-e0+e2+e3)*m1)


def matter_sum(flat):
    return tuple(sum(flat[offset + phase] for offset in (0, 4, 8))
                 for phase in range(4))


def stored_state(matter, spectators, raw, resource):
    result = tuple(matter) + tuple(spectators) + tuple(raw) + (resource,)
    legal(result)
    return result


def legal(state):
    assert len(state) == 31
    assert all(type(value) is int for value in state)
    assert state[30] >= 0


def total(state):
    return (sum(matter_energy(state[i:i+4]) for i in range(0, 24, 4))
            + raw_energy(state[24:30]) + state[30])


def divergence(raw):
    e0, e1, e2, e3 = raw[:4]
    return (e0+e1+e2, -e0-e1-e3, -e2+e3)


def charge(state):
    return (sum(state[:12]) + sum(state[12:16]),
            sum(state[16:20]), sum(state[20:24]))


def defect(state):
    return tuple(a - b for a, b in zip(divergence(state[24:30]),
                                      charge(state)))


def gate(state):
    """Total funded map, with every rejection returning the identical tuple."""
    matter = state[:12]
    if matter != R and matter != END:
        return state
    parts = split(state[24:30])
    if parts is None:
        return state
    vector, pair = parts
    if matter == R:
        if not image_member(vector):
            return state
        numerators = numerator(vector)
        assert all(value % 5 == 0 for value in numerators)
        low = tuple(value // 5 for value in numerators)
        new_resource = state[30] + 4*active_energy(low) - 2
        replacement = END
        new_raw = field(low, pair)
    else:
        new_resource = state[30] + 2 - 4*active_energy(vector)
        replacement = R
        new_raw = field(high(vector), pair)
    if new_resource < 0:
        return state
    return replacement + state[12:24] + new_raw + (new_resource,)


def free_raw(raw):
    e0, e1, e2, e3, m0, m1 = raw
    f0, f1, f2, f3 = e0+m0-m1, e1-m0, e2+m1, e3+m1
    return (f0, f1, f2, f3, m0-f0+f1, m1+f0-f2-f3)


def backward_raw(raw):
    f0, f1, f2, f3, n0, n1 = raw
    m0, m1 = n0+f0-f1, n1-f0+f2+f3
    return (f0-m0+m1, f1+m0, f2-m1, f3-m1, m0, m1)


def free(state):
    return state[:24] + free_raw(state[24:30]) + state[30:]


def backward(state):
    return state[:24] + backward_raw(state[24:30]) + state[30:]


def cell(state):
    return free(gate(state))


def inverse_cell(state):
    return gate(backward(state))


def conserved(before, after):
    legal(after)
    assert total(after) == total(before) >= 0
    assert after[12:24] == before[12:24]
    assert matter_sum(after[:12]) == matter_sum(before[:12])
    assert defect(after) == defect(before)


def audit(state, extensive=True):
    legal(state)
    switched = gate(state)
    conserved(state, switched)
    assert gate(switched) == state
    original_parts = split(state[24:30])
    switched_parts = split(switched[24:30])
    if original_parts is not None:
        assert switched_parts is not None
        assert switched_parts[1] == original_parts[1]
    if extensive:
        forward = cell(state)
        conserved(state, free(state))
        conserved(state, backward(state))
        conserved(state, forward)
        conserved(state, inverse_cell(state))
        assert free(state)[:24] == state[:24]
        assert free(state)[30] == state[30]
        assert backward(free(state)) == state
        assert free(backward(state)) == state
        assert gate(free(state)) == free(switched)
        assert inverse_cell(forward) == state
        assert cell(inverse_cell(state)) == state
    return switched


def certificates():
    # The incidence is reconstructed from four ordered, distinct edges.
    edges = ((0, 1), (0, 1), (0, 2), (2, 1))
    incidence = tuple(tuple(int(vertex == tail) - int(vertex == head)
                            for tail, head in edges) for vertex in range(3))
    assert incidence == ((1, 1, 1, 0), (-1, -1, 0, -1), (0, 0, -1, 1))
    assert mm(incidence, C) == ((0, 0),) * 3
    assert linear_matrix(divergence, 6) == tuple(row + (0, 0)
                                                for row in incidence)

    identity = eye(4)
    assert power(A, 5) == identity
    assert mm(mm(transpose(A), B), A) == B
    assert L == mm(difference(identity, A), difference(identity, power(A, 2)))
    assert mm(A, L) == mm(L, A)
    assert N == mm(power(A, 2), L)
    assert mm(N, L) == mm(L, N) == scale(5, identity)
    assert mm(mm(transpose(L), B), L) == scale(5, B)
    assert determinant(L) == 25
    assert linear_matrix(high, 4) == L
    assert linear_matrix(numerator, 4) == N
    assert all(B[i][i] % 2 == 0 for i in range(4))
    positive(B)
    positive(K)
    for vector, eigenvalue in (((1, 1, 1, 1), 9),
                              ((1, -1, 1, -1), 1),
                              ((1, 0, -1, 0), 7),
                              ((0, 1, 0, -1), 7)):
        assert mv(K, vector) == tuple(eigenvalue*v for v in vector)
    eigenbasis = ((1, 1, 1, 1), (1, -1, 1, -1),
                  (1, 0, -1, 0), (0, 1, 0, -1))
    assert determinant(eigenbasis) != 0

    p = linear_matrix(active, 4)
    s = linear_matrix(static, 2)
    combined = tuple(left + right for left, right in zip(p, s))
    primitive_columns(p)
    primitive_columns(s)
    assert abs(determinant(combined)) == 5
    # This integer numerator matrix is a certificate over all raw fields.
    extraction = ((2, -3, 1, 1, 0, 0), (-1, -1, 2, 2, 0, 0),
                  (0, 0, 0, 0, 5, 0), (0, 0, 0, 0, 0, 5),
                  (2, 2, 1, 1, 0, 0), (1, 1, 3, -2, 0, 0))
    assert mm(extraction, combined) == mm(combined, extraction) == scale(5, eye(6))
    for row, multiple in zip(extraction, (1, 2, 0, 0, 1, 3)):
        assert all((value - multiple*g) % 5 == 0
                   for value, g in zip(row, extraction[0]))
    # Modulo five, Ny has coordinates (p+q, 2p+2q, q, 2q).
    residues = ((1, 2, 1, 2), (2, 4, 2, 4),
                (0, 0, 1, 2), (0, 0, 2, 4))
    assert all((a-b) % 5 == 0 for row_a, row_b in zip(N, residues)
               for a, b in zip(row_a, row_b))
    quotient = ((1, 2, 0, 0), (0, 0, 1, 2))
    quotient_action = mm(((1, 1), (0, 1)), quotient)
    assert all((a-b) % 5 == 0
               for row_a, row_b in zip(mm(quotient, A), quotient_action)
               for a, b in zip(row_a, row_b))
    assert determinant(((1, 1), (0, 1))) == 1

    # Twice the raw quadratic form has the cross block C.
    raw_metric = tuple(tuple(2*int(i == j) for j in range(4)) + C[i]
                       for i in range(4))
    raw_metric += tuple(row + tuple(2*int(i == j) for j in range(2))
                        for i, row in enumerate(transpose(C)))
    positive(raw_metric)
    static_metric = ((6, -2), (-2, 4))
    block = tuple(row + (0, 0) for row in B)
    block += tuple((0, 0, 0, 0) + row for row in static_metric)
    assert mm(mm(transpose(combined), raw_metric), combined) == block
    assert mm(incidence, tuple(row[:4] for row in p[:4])) == ((0, 0, 0, 0),) * 3
    assert mm(incidence, s[:4]) == ((2, 1), (-3, 1), (1, -2))

    transform = linear_matrix(free_raw, 6)
    transform_inverse = linear_matrix(backward_raw, 6)
    assert mm(transform, transform_inverse) == mm(transform_inverse, transform) == eye(6)
    assert power(transform, 5) == eye(6)
    assert mm(mm(transpose(transform), raw_metric), transform) == raw_metric
    assert mm(transform, p) == mm(p, A)
    assert mm(transform, s) == s
    extended_d = tuple(row + (0, 0) for row in incidence)
    assert mm(extended_d, transform) == extended_d
    for mapping in (transform, transform_inverse):
        moved = mm((extraction[0],), mapping)[0]
        assert all((a-b) % 5 == 0 for a, b in zip(moved, extraction[0]))

    # Polarization checks direct energy formulas against independent matrices.
    for dimension, formula, metric in ((4, active_energy, B),
                                        (4, matter_energy, scale(2, K)),
                                        (6, raw_energy, raw_metric)):
        units = eye(dimension)
        for i in range(dimension):
            assert 2*formula(units[i]) == metric[i][i]
            for j in range(dimension):
                vector = tuple(a+b for a, b in zip(units[i], units[j]))
                assert formula(vector)-formula(units[i])-formula(units[j]) == metric[i][j]
    assert sum(matter_energy(R[i:i+4]) for i in (0, 4, 8)) == 18
    assert sum(matter_energy(END[i:i+4]) for i in (0, 4, 8)) == 20
    assert matter_sum(R) == matter_sum(END) == (1, -2, 1, 0)
    assert sum(R) == sum(END) == 0
    assert R != END
    # SPD forms, exact stored r >= 0 and the block identity establish
    # nonnegative total energy. T preserves split membership; A preserves
    # image membership and h. Static data, endpoints and funding therefore
    # commute with T even on rejected states. Together T^5=I and G^2=I
    # imply U^5=G and U^10=I on the complete domain, including defects.


def spectators_for(pair, error=0):
    values = list(divergence(static(pair)))
    values[0] += error
    return tuple(entry for value in values for entry in (value, 0, 0, 0))


def cube_fixtures():
    for vector in product((-1, 0, 1), repeat=4):
        h = active_energy(vector)
        assert h >= 0 and (h == 0) == (vector == (0, 0, 0, 0))
        delta = 4*h - 2
        budgets = {0, 1, 2, max(0, delta-1), max(0, delta), max(0, delta+1)}
        for pair in ((0, 0), (1, 0), (0, 1), (1, -2)):
            high_raw, low_raw = field(high(vector), pair), field(vector, pair)
            assert split(high_raw) == (high(vector), pair)
            assert split(low_raw) == (vector, pair)
            assert raw_energy(low_raw) == h + 3*pair[0]**2 - 2*pair[0]*pair[1] + 2*pair[1]**2
            for error in (0, 1):
                spectators = spectators_for(pair, error)
                for budget in sorted(budgets):
                    for matter, raw, next_matter, next_raw, change in (
                            (R, high_raw, END, low_raw, delta),
                            (END, low_raw, R, high_raw, -delta)):
                        state = stored_state(matter, spectators, raw, budget)
                        assert defect(state) == (-error, 0, 0)
                        if budget + change >= 0:
                            expected = stored_state(next_matter, spectators,
                                                    next_raw, budget+change)
                            assert expected != state
                        else:
                            expected = state
                        assert audit(state) == expected


def residue_fixtures():
    image_count = 0
    counts = {0: [0, 0], 2: [0, 0]}
    for vector in product(range(5), repeat=4):
        assert split(field(vector)) == (vector, (0, 0))
        member = image_member(vector)
        nums = mv(N, vector)
        assert member == all(value % 5 == 0 for value in nums)
        inverse = tuple(Fraction(value, 5) for value in nums)
        assert mv(L, inverse) == vector
        assert member == all(value.denominator == 1 for value in inverse)
        low = None
        if member:
            image_count += 1
            low = tuple(value.numerator for value in inverse)
            assert high(low) == vector
            assert active_energy(vector) == 5*active_energy(low)
        for budget in (0, 2):
            state = stored_state(R, ZERO_B, field(vector), budget)
            should_switch = member and budget+4*active_energy(low)-2 >= 0
            output = audit(state, extensive=False)
            assert (output != state) == should_switch
            if should_switch:
                assert output == stored_state(END, ZERO_B, field(low),
                                               budget+4*active_energy(low)-2)
            counts[budget][int(not should_switch)] += 1
    assert image_count == 25
    assert counts == {0: [24, 601], 2: [25, 600]}


def explicit_fixtures():
    w = (0, 0, 1, 0)
    neutral_high = stored_state(R, ZERO_B, field(high(w)), 0)
    neutral_low = stored_state(END, ZERO_B, field(w), 2)
    assert audit(neutral_high) == neutral_low
    assert total(neutral_high) == total(neutral_low) == 23
    assert active_energy(w) == 1

    charged_b = spectators_for((1, 0))
    assert charged_b == (2, 0, 0, 0, -3, 0, 0, 0, 1, 0, 0, 0)
    charged_high = stored_state(R, charged_b, (2, 2, -2, -1, 1, 2), 0)
    charged_low = stored_state(END, charged_b, (1, 1, 0, 1, 1, 0), 2)
    assert charged_high[24:30] == field(high(w), (1, 0))
    assert charged_low[24:30] == field(w, (1, 0))
    assert audit(charged_high) == charged_low
    assert divergence(charged_high[24:30]) == divergence(charged_low[24:30]) == (2, -3, 1)
    assert defect(charged_high) == defect(charged_low) == (0, 0, 0)
    assert raw_energy(charged_high[24:30]) == 8
    assert raw_energy(charged_low[24:30]) == 4
    assert sum(matter_energy(charged_b[i:i+4]) for i in (0, 4, 8)) == 84
    assert total(charged_high) == 18+8+84+0 == 110
    assert total(charged_low) == 20+4+84+2 == 110

    for budget in (0, 1, 2):
        reverse = stored_state(END, ZERO_B, field(w), budget)
        assert audit(reverse) == (neutral_high if budget == 2 else reverse)
        zero_r = stored_state(R, ZERO_B, (0,)*6, budget)
        expected = stored_state(END, ZERO_B, (0,)*6, 0) if budget == 2 else zero_r
        assert audit(zero_r) == expected
    zero_a = stored_state(END, ZERO_B, (0,)*6, 0)
    assert audit(zero_a) == stored_state(R, ZERO_B, (0,)*6, 2)

    assert active_energy((0, 0, 1, -2)) == 5
    for vector in ((0, 0, 1, -2), (0, 0, 1, 1)):
        assert not image_member(vector)
        rejected = stored_state(R, ZERO_B, field(vector), 100)
        assert audit(rejected) == rejected
    admitted = (0, 0, 1, 2)
    assert image_member(admitted)
    assert tuple(value // 5 for value in numerator(admitted)) == (1, 0, -1, 1)
    admitted_state = stored_state(R, ZERO_B, field(admitted), 0)
    assert audit(admitted_state)[:12] == END

    nonsplit = stored_state(R, (1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
                           (1, 0, 0, 0, 0, 0), 100)
    assert defect(nonsplit) == (0, 0, 0)
    assert split(nonsplit[24:30]) is None
    assert audit(nonsplit) == nonsplit
    off_endpoints = ((0,)*12, END[4:8]+END[:4]+END[8:12],
                     (0, 1, -2, 1)+(0,)*8)
    for matter in off_endpoints:
        assert matter not in (R, END)
        for raw in (field(w), field(high(w))):
            for budget in (0, 2, 100):
                state = stored_state(matter, ZERO_B, raw, budget)
                assert audit(state) == state

    # Negative controls are literal erroneous endpoints, not alternative laws.
    discarded_surplus = neutral_low[:30] + (0,)
    assert total(discarded_surplus) == total(neutral_high)-2
    underfunded_reverse = stored_state(END, ZERO_B, field(w), 0)
    clipped_reverse = neutral_high
    assert gate(underfunded_reverse) == underfunded_reverse
    assert total(clipped_reverse) == total(underfunded_reverse)+2
    charged_without_spectators = stored_state(R, ZERO_B, charged_high[24:30], 0)
    assert total(charged_high)-total(charged_without_spectators) == 84
    deleted_static = stored_state(R, charged_b, field(high(w)), 0)
    assert divergence(deleted_static[24:30]) == (0, 0, 0)
    assert defect(deleted_static) == (-2, 3, -1)
    assert deleted_static != charged_high
    conflated_branch = R + neutral_low[12:]
    assert matter_sum(conflated_branch[:12]) == matter_sum(neutral_low[:12])
    assert gate(conflated_branch) != neutral_high
    assert gate(discarded_surplus) != neutral_high
    cleared_spectator = charged_low[:12] + (0,)*4 + charged_low[16:]
    assert gate(cleared_spectator) != charged_high
    assert gate(cleared_spectator)[12:16] == (0,)*4

    return (neutral_high, charged_high)


def period_witnesses(initial_states):
    for initial, pair in zip(initial_states, ((0, 0), (1, 0))):
        state = initial
        vector = (0, 0, 1, 0)
        orbit = []
        for k in range(11):
            matter, resource = (END, 2) if k % 2 else (R, 0)
            raw = field(vector if k % 2 else high(vector), pair)
            expected = stored_state(matter, initial[12:24], raw, resource)
            assert state == expected
            conserved(initial, state)
            if 0 < k < 10:
                assert state != initial
            orbit.append(state)
            if k < 10:
                state = cell(state)
                vector = mv(A, vector)
        assert orbit[5] == gate(initial)
        assert orbit[10] == initial
        assert len(set(orbit[:10])) == 10


def main():
    if not __debug__:
        raise RuntimeError("The exact audit requires enabled assertions")
    certificates()
    cube_fixtures()
    residue_fixtures()
    period_witnesses(explicit_fixtures())
    print("CHALLENGER PASS: independent coupling audit; image, funding and branch controls")


if __name__ == "__main__":
    main()
