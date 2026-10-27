#!/usr/bin/env python3
"""Independent PUBLIC / NON-CANONICAL L1 audit of the frozen transfer law.

Written from PREREG.md, without reading the primary implementation, its proof,
predecessor implementations, or scientific outputs. The dynamic carrier is one
flat tuple of 63 integers; matrix operations are confined to certificates and
the separately expressed gate oracle. No scientific pre-pin run is permitted.
"""

from fractions import Fraction
from itertools import product
import sys


if not __debug__:
    raise RuntimeError("This exact audit requires enabled assertions")


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
R = (1, -2, 1, 0) + (0,) * 8
AM = (1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 0)
ZERO = (0,) * 12
W = (0, 0, 1, 0)
V = (0, 0, 1, 1)
FORWARD = ("Gs", "Xs", "Xt", "Gt", "Fs", "Ft")
BACKWARD = ("it", "is", "Gt", "Xt", "Xs", "Gs")
DISABLED = ("Gs", "Gt", "Fs", "Ft")
BRANCHES = set()


def mv(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def transpose(matrix):
    return tuple(zip(*matrix))


def mm(left, right):
    columns = transpose(right)
    return tuple(tuple(sum(a * b for a, b in zip(row, column))
                       for column in columns) for row in left)


def ident(size):
    return tuple(tuple(int(i == j) for j in range(size)) for i in range(size))


def scale(matrix, factor):
    return tuple(tuple(factor * value for value in row) for row in matrix)


def power(matrix, exponent):
    answer = ident(len(matrix))
    for _ in range(exponent):
        answer = mm(answer, matrix)
    return answer


def determinant(matrix):
    work = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for k in range(len(work)):
        pivot = next((i for i in range(k, len(work)) if work[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            work[pivot], work[k] = work[k], work[pivot]
            result = -result
        diagonal = work[k][k]
        result *= diagonal
        for i in range(k + 1, len(work)):
            ratio = work[i][k] / diagonal
            for j in range(k + 1, len(work)):
                work[i][j] -= ratio * work[k][j]
    return result


def q4(v):
    a, b, c, d = v
    return (6 * (a*a + b*b + c*c + d*d) + 4*a*b - 2*a*c
            + 4*a*d + 4*b*c - 2*b*d + 4*c*d)


def active_energy(v):
    a, b, c, d = v
    return 2*a*a + 3*b*b + c*c + d*d - 2*a*b + 2*a*c - a*d - b*c + 3*b*d


def raw_energy(v):
    e0, e1, e2, e3, m0, m1 = v
    return (e0*e0 + e1*e1 + e2*e2 + e3*e3 + m0*m0 + m1*m1
            + (e0-e1)*m0 + (-e0+e2+e3)*m1)


def inject(v):
    a, b, c, d = v
    return a-b, -a, b, b, c, d


def static(u, v):
    return u, u, v, u-v, 0, 0


def plus(left, right):
    return tuple(a+b for a, b in zip(left, right))


def field_forward(z):
    e0, e1, e2, e3, m0, m1 = z
    f0, f1, f2, f3 = e0+m0-m1, e1-m0, e2+m1, e3+m1
    return f0, f1, f2, f3, m0-f0+f1, m1+f0-f2-f3


def field_backward(z):
    f0, f1, f2, f3, n0, n1 = z
    m0, m1 = n0+f0-f1, n1-f0+f2+f3
    return f0-m0+m1, f1+m0, f2-m1, f3-m1, m0, m1


def quadratic_matrix(polynomial, dimension):
    """Twice the symmetric matrix, by exact coefficient polarization."""
    basis = ident(dimension)
    diagonal = tuple(polynomial(e) for e in basis)
    return tuple(tuple(2*diagonal[i] if i == j else
                       polynomial(plus(basis[i], basis[j])) - diagonal[i] - diagonal[j]
                       for j in range(dimension)) for i in range(dimension))


def linear_matrix(function, dimension):
    return transpose(tuple(function(e) for e in ident(dimension)))


def certificates():
    i4, i6 = ident(4), ident(6)
    assert mm(D, C) == ((0, 0),) * 3
    assert quadratic_matrix(q4, 4) == scale(K, 2)
    assert quadratic_matrix(active_energy, 4) == B
    raw = tuple(tuple(2*int(i == j) if (i < 4) == (j < 4)
                      else C[i][j-4] if i < 4 else C[j][i-4]
                      for j in range(6)) for i in range(6))
    assert quadratic_matrix(raw_energy, 6) == raw
    assert linear_matrix(inject, 4) == P
    assert linear_matrix(lambda z: static(*z), 2) == S

    # Q - ||v||^2 is a sum of positive integer weighted squares.
    def matter_squares(v):
        a, b, c, d = v
        return (2*(a+b)**2 + (a-c)**2 + 2*(a+d)**2
                + 2*(b+c)**2 + (b-d)**2 + 2*(c+d)**2)
    assert quadratic_matrix(lambda v: q4(v)-sum(t*t for t in v), 4) == quadratic_matrix(matter_squares, 4)

    # This identity is the coercivity certificate on every raw integer field.
    def raw_squares(v):
        e0, e1, e2, e3, m0, m1 = v
        return ((2*e0+m0-m1)**2 + (2*e1-m0)**2
                + (2*e2+m1)**2 + (2*e3+m1)**2 + m0*m0 + (m0+m1)**2)
    assert scale(raw, 4) == quadratic_matrix(raw_squares, 6)
    for matrix in (K, B, raw):
        assert matrix == transpose(matrix)
        for size in range(1, len(matrix)+1):
            assert determinant(tuple(row[:size] for row in matrix[:size])) > 0

    chart = tuple(P[i] + S[i] for i in range(6))
    numerators = ((2, -3, 1, 1, 0, 0), (-1, -1, 2, 2, 0, 0),
                  (0, 0, 0, 0, 5, 0), (0, 0, 0, 0, 0, 5),
                  (2, 2, 1, 1, 0, 0), (1, 1, 3, -2, 0, 0))
    inverse = tuple(tuple(Fraction(x, 5) for x in row) for row in numerators)
    assert mm(inverse, chart) == i6 == mm(chart, inverse)
    assert abs(determinant(chart)) == 5
    for row, multiplier in zip(numerators, (1, 2, 0, 0, 1, 3)):
        assert all((entry-multiplier*g) % 5 == 0 for entry, g in zip(row, numerators[0]))
    combined = mm(mm(transpose(chart), raw), chart)
    expected = tuple(tuple(B[i][j] if i < 4 and j < 4 else
                           ((6, -2), (-2, 4))[i-4][j-4] if i >= 4 and j >= 4 else 0
                           for j in range(6)) for i in range(6))
    assert combined == expected
    assert mm(D, P[:4]) == ((0, 0, 0, 0),) * 3
    assert mm(D, S[:4]) == ((2, 1), (-3, 1), (1, -2))

    assert mm(L, N) == scale(i4, 5) == mm(N, L)
    assert determinant(L) == 25
    assert mm(A, L) == mm(L, A)
    assert mm(A, N) == mm(N, A)
    assert power(A, 5) == i4
    assert mm(mm(transpose(A), B), A) == B
    assert mm(mm(transpose(L), B), L) == scale(B, 5)
    # An algebraic equivalence for the image test, separate from its finite
    # residue audit: Ny mod 5 encodes alpha=a+2b and beta=c+2d injectively.
    constraints = ((1, 2, 0, 0), (0, 0, 1, 2))
    encoding = ((1, 1), (2, 2), (0, 1), (0, 2))
    decoding = ((1, 0, -1, 0), (0, 0, 1, 0))
    encoded = mm(encoding, constraints)
    assert all((N[i][j]-encoded[i][j]) % 5 == 0 for i in range(4) for j in range(4))
    assert mm(decoding, encoding) == ident(2)
    assert all(value % 5 == 0 for row in mm(constraints, L) for value in row)
    residue_count = 0
    for y in product(range(5), repeat=4):
        admitted = (y[0]+2*y[1]) % 5 == 0 and (y[2]+2*y[3]) % 5 == 0
        divisible = all(value % 5 == 0 for value in mv(N, y))
        assert admitted == divisible
        residue_count += admitted
    assert residue_count == 25
    # N integrality is sufficient by LN=5I, necessary by NL=5I.

    t = linear_matrix(field_forward, 6)
    ti = linear_matrix(field_backward, 6)
    assert mm(t, ti) == i6 == mm(ti, t)
    assert mm(mm(transpose(t), raw), t) == raw
    assert power(t, 5) == i6
    assert mm(t, P) == mm(P, A)
    assert mm(t, S) == S
    boundary = tuple(row + (0, 0) for row in D)
    assert mm(boundary, t) == boundary == mm(boundary, ti)
    assert tuple(sum(R[4*j+k] for j in range(3)) for k in range(4)) == tuple(sum(AM[4*j+k] for j in range(3)) for k in range(4))
    assert sum(R) == 0 == sum(AM)
    assert sum(q4(R[i:i+4]) for i in (0, 4, 8)) == 18
    assert sum(q4(AM[i:i+4]) for i in (0, 4, 8)) == 20
    assert active_energy(W) == 1 and active_energy(V) == 2
    assert mv(L, W) == (-1, -2, 1, 2)
    assert inject(mv(L, W)) == (1, 1, -2, -2, 1, 2)
    assert inject(W) == (0, 0, 0, 0, 1, 0)
    assert inject(mv(A, W)) == (1, -1, 0, 0, -1, 1)
    # The positive forms and nonnegative resources bound every coordinate on
    # a fixed Hjoint shell: Q bounds matter/spectators; raw_squares bounds M0,
    # then M1, then all E coordinates. Thus the integer shell is finite.
    # The exact inverse makes every orbit in that shell periodic from k=0.


def legal(state):
    assert len(state) == 63
    assert all(type(value) is int for value in state)
    assert all(state[i] >= 0 for i in (30, 61, 62))


def operate(state, operation):
    """Read tracing enforces primitive support; writes are simultaneous locally."""
    base = 0 if operation[-1] == "s" else 31
    reads, writes = set(), {}

    def read(index):
        reads.add(index)
        return state[index]

    if operation[0] == "X":
        resource, channel = read(base+30), read(62)
        writes[base+30], writes[62] = channel, resource
        allowed_reads = allowed_writes = {base+30, 62}
    elif operation[0] in ("F", "i"):
        raw = tuple(read(base+24+j) for j in range(6))
        result = field_backward(raw) if operation[0] == "i" else field_forward(raw)
        writes.update((base+24+j, value) for j, value in enumerate(result))
        allowed_reads = allowed_writes = set(range(base+24, base+30))
    else:
        assert operation[0] == "G"
        matter = tuple(read(base+j) for j in range(12))
        allowed_reads = set(range(base, base+31))
        allowed_writes = set(range(base, base+12)) | set(range(base+24, base+31))
        if matter in (R, AM):
            e0, e1, e2, e3, c, d = (read(base+24+j) for j in range(6))
            g = 2*e0 - 3*e1 + e2 + e3
            if g % 5 == 0:
                a, b = g//5, (-e0-e1+2*e2+2*e3)//5
                u, v = (2*e0+2*e1+e2+e3)//5, (e0+e1+3*e2-2*e3)//5
                if matter == AM or ((a+2*b) % 5 == 0 and (c+2*d) % 5 == 0):
                    if matter == R:
                        x = ((a+2*b+c+2*d)//5, (2*a-b+2*c-d)//5,
                             (-5*b+c-3*d)//5, (-5*a+5*b-3*c+4*d)//5)
                        change = 4*active_energy(x)-2
                        next_matter = AM
                    else:
                        x = (a-3*b-c-2*d, -3*a+4*b-2*c+d,
                             5*b+c+2*d, 5*a-5*b+2*c-d)
                        change = 2-4*active_energy((a, b, c, d))
                        next_matter = R
                    resource = read(base+30)
                    if resource+change >= 0:
                        next_raw = plus(inject(x), static(u, v))
                        writes.update((base+j, value) for j, value in enumerate(next_matter))
                        writes.update((base+24+j, value) for j, value in enumerate(next_raw))
                        writes[base+30] = resource+change
    assert reads <= allowed_reads
    assert writes.keys() <= allowed_writes
    assert all(type(value) is int for value in writes.values())
    result = list(state)
    for index, value in writes.items():
        result[index] = value
    result = tuple(result)
    assert all(before == after for i, (before, after) in enumerate(zip(state, result)) if i not in allowed_writes)
    return result


def gate_oracle(cell):
    """The frozen recognition order, independently expressed using N and L."""
    matter, field, resource = cell[:12], cell[24:30], cell[30]
    if matter not in (R, AM):
        return cell, "matter"
    e0, e1, e2, e3, m0, m1 = field
    nums = (2*e0-3*e1+e2+e3, -e0-e1+2*e2+2*e3,
            2*e0+2*e1+e2+e3, e0+e1+3*e2-2*e3)
    if nums[0] % 5:
        return cell, "split"
    assert all(value % 5 == 0 for value in nums)
    y = (nums[0]//5, nums[1]//5, m0, m1)
    background = mv(S, (nums[2]//5, nums[3]//5))
    assert plus(mv(P, y), background) == field
    if matter == R:
        preimage = mv(N, y)
        if any(value % 5 for value in preimage):
            return cell, "image"
        next_active = tuple(value//5 for value in preimage)
        assert mv(L, next_active) == y
        next_resource = resource + 4*active_energy(next_active)-2
        endpoint = AM
    else:
        next_active = mv(L, y)
        next_resource = resource + 2-4*active_energy(y)
        endpoint = R
    if next_resource < 0:
        return cell, "funding"
    return (endpoint + cell[12:24] + plus(mv(P, next_active), background)
            + (next_resource,)), "R" if matter == R else "AM"


def cell_account(cell):
    return sum(q4(cell[i:i+4]) for i in range(0, 24, 4)) + raw_energy(cell[24:30]) + cell[30]


def energy_accounts(state):
    return cell_account(state[:31]), cell_account(state[31:62]), state[62]


def fixed_data(state):
    data = []
    for base in (0, 31):
        cell = state[base:base+31]
        vector_sum = tuple(cell[k]+cell[k+4]+cell[k+8] for k in range(4))
        spectators = cell[12:24]
        rho = (sum(cell[:12])+sum(spectators[:4]), sum(spectators[4:8]), sum(spectators[8:]))
        e0, e1, e2, e3 = cell[24:28]
        divergence = (e0+e1+e2, -e0-e1-e3, -e2+e3)
        defect = tuple(d-r for d, r in zip(divergence, rho))
        data.extend((spectators, vector_sum, rho, defect))
    return tuple(data)


def audit_stage(before, after, operation):
    legal(before)
    legal(after)
    accounts_before, accounts_after = energy_accounts(before), energy_accounts(after)
    assert sum(accounts_before) == sum(accounts_after)
    assert fixed_data(before) == fixed_data(after)
    base = 0 if operation[-1] == "s" else 31
    other = 31-base
    assert before[other:other+31] == after[other:other+31]
    if operation[0] == "X":
        index = base//31
        amount = before[62]-before[base+30]
        assert accounts_after[index]-accounts_before[index] == amount
        assert accounts_after[2]-accounts_before[2] == -amount
        assert operate(after, operation) == before
        assert after[base+30] == before[62] and after[62] == before[base+30]
    elif operation[0] == "G":
        expected, branch = gate_oracle(before[base:base+31])
        BRANCHES.add(branch)
        assert after[base:base+31] == expected
        assert after[62] == before[62]
        assert accounts_before == accounts_after
        assert operate(after, operation) == before
    else:
        reverse = ("i" if operation[0] == "F" else "F") + operation[-1]
        assert operate(after, reverse) == before
        assert accounts_before == accounts_after
        assert after[62] == before[62]


def schedule(initial, operations, audit=False):
    state = initial
    for operation in operations:
        next_state = operate(state, operation)
        if audit:
            audit_stage(state, next_state, operation)
        state = next_state
    return state


def make_cell(matter, field, resource, background=(0, 0), defect_shift=0):
    field = plus(field, static(*background))
    e0, e1, e2, e3 = field[:4]
    charges = (e0+e1+e2+defect_shift, -e0-e1-e3, -e2+e3)
    spectators = tuple(value for charge in charges for value in (charge, 0, 0, 0))
    return matter + spectators + field + (resource,)


def finite_audit():
    lw, lv = inject(mv(L, W)), inject(mv(L, V))
    catalog = ((R, (0,)*6), (AM, (0,)*6), (R, lw), (AM, inject(W)),
               (R, lv), (AM, inject(V)), (R, inject((0, 0, 1, -2))),
               (R, (1, 0, 0, 0, 0, 0)), (ZERO, lw),
               (AM[4:8]+AM[:4]+AM[8:], inject(W)), ((0, 1, -2, 1)+(0,)*8, lw))
    resources = ((0, 0), (2, 1), (1, 2), (5, 6), (7, 5), (6, 7))
    backgrounds = (((0, 0), (0, 0), 0), ((1, 0), (0, 1), 0), ((1, 0), (0, 1), 1))
    assert len(catalog) == 11 and all(sum(matter) == 0 for matter, _ in catalog)
    seen = set()
    for source, target, resource_pair, channel, background in product(catalog, catalog, resources, range(3), backgrounds):
        sb, tb, shift = background
        state = (make_cell(*source, resource_pair[0], sb, shift)
                 + make_cell(*target, resource_pair[1], tb, -shift) + (channel,))
        assert state not in seen
        seen.add(state)
        data = fixed_data(state)
        assert data[3] == (-shift, 0, 0) and data[7] == (shift, 0, 0)
        end = schedule(state, FORWARD, True)
        assert schedule(end, BACKWARD, True) == state
        preimage = schedule(state, BACKWARD, True)
        assert schedule(preimage, FORWARD) == state
        disabled = schedule(state, DISABLED, True)
        assert energy_accounts(disabled) == energy_accounts(state)
        assert disabled[62] == state[62]
        # F commutes with all gates and contacts; the certificate supplies the
        # universal AL=LA, energy and static identities behind this finite audit.
        f_state = schedule(state, ("Fs", "Ft"))
        reaction_contacts = ("Gs", "Xs", "Xt", "Gt")
        assert schedule(f_state, reaction_contacts) == schedule(schedule(state, reaction_contacts), ("Fs", "Ft"))
    assert len(seen) == 6534
    assert BRANCHES == {"matter", "split", "image", "funding", "R", "AM"}


def witness(charged):
    source_background, target_background = ((1, 0), (0, 1)) if charged else ((0, 0), (0, 0))
    source = make_cell(R, inject(mv(L, W)), 0, source_background)
    target = make_cell(R, (0,)*6, 0, target_background)
    initial = source + target + (0,)
    triples = ((110, 56, 0), (110, 56, 0), (108, 56, 2), (108, 58, 0),
               (108, 58, 0), (108, 58, 0), (108, 58, 0)) if charged else (
               (23, 18, 0), (23, 18, 0), (21, 18, 2), (21, 20, 0),
               (21, 20, 0), (21, 20, 0), (21, 20, 0))
    states = [initial]
    for operation in FORWARD:
        states.append(schedule(states[-1], (operation,), True))
    for index, state in enumerate(states):
        sm, tm = (R if index == 0 else AM), (R if index < 4 else AM)
        active = mv(L, W) if index == 0 else mv(A, W) if index >= 5 else W
        sraw = plus(inject(active), static(*source_background))
        expected_source = sm + source[12:24] + sraw + ((0, 2, 0, 0, 0, 0, 0)[index],)
        expected_target = tm + target[12:30] + ((0, 0, 0, 2, 0, 0, 0)[index],)
        assert state == expected_source + expected_target + ((0, 0, 2, 0, 0, 0, 0)[index],)
        assert energy_accounts(state) == triples[index]
        assert sum(triples[index]) == (166 if charged else 41)
        assert fixed_data(state)[2] == ((2, -3, 1) if charged else (0, 0, 0))
        assert fixed_data(state)[6] == ((1, 1, -2) if charged else (0, 0, 0))
        assert fixed_data(state)[3] == (0, 0, 0) == fixed_data(state)[7]
    assert triples[-1][0] == triples[0][0]-2
    assert triples[-1][1] == triples[0][1]+2
    if charged:
        assert states[-1][24:30] == (2, 0, 0, 1, -1, 1)
        assert states[-1][55:61] == (0, 0, 1, -1, 0, 0)
    disabled = schedule(initial, DISABLED, True)
    assert disabled == (AM + source[12:24] + plus(inject(mv(A, W)), static(*source_background))
                        + (2,) + target + (0,))
    assert disabled[31:62] == target

    endpoints = ((R, R), (AM, AM), (AM, R), (AM, R), (AM, R), (R, R))
    amounts = ((0, 0, 0), (0, 0, 0), (0, 2, 0), (0, 0, 2), (2, 0, 0), (0, 0, 0))
    state, x, recurrence = initial, W, []
    for k in range(6):
        sm, tm = endpoints[k]
        rs, rt, channel = amounts[k]
        active = mv(L, x) if k in (0, 5) else x
        expected = (sm + source[12:24] + plus(inject(active), static(*source_background)) + (rs,)
                    + tm + target[12:30] + (rt, channel))
        assert state == expected
        legal(state)
        assert sum(energy_accounts(state)) == (166 if charged else 41)
        assert fixed_data(state) == fixed_data(initial)
        recurrence.append(state)
        if k < 5:
            state = schedule(state, FORWARD, True)
            x = mv(A, x)
    assert len(set(recurrence[:5])) == 5
    assert recurrence[5] == recurrence[0] and x == W
    return initial, states


def replace_values(state, changes):
    return tuple(changes.get(index, value) for index, value in enumerate(state))


def attacks(neutral, neutral_stages):
    # Equal field energy does not imply admission to the L image.
    rejected = make_cell(R, inject((0, 0, 1, -2)), 0) + neutral[31:]
    assert raw_energy(rejected[24:30]) == raw_energy(neutral[24:30]) == 5
    assert gate_oracle(rejected[:31])[1] == "image"
    assert operate(rejected, "Gs") == rejected
    advanced = schedule(rejected, FORWARD, True)
    assert advanced != rejected and advanced[24:30] != rejected[24:30]
    assert advanced[31:] == rejected[31:]
    assert advanced == schedule(rejected, DISABLED, True)

    occupied = make_cell(ZERO, (0,)*6, 2) + make_cell(ZERO, (0,)*6, 3) + (1,)
    first = schedule(occupied, ("Xs",), True)
    second = schedule(first, ("Xt",), True)
    assert (occupied[30], occupied[62], occupied[61]) == (2, 1, 3)
    assert (first[30], first[62], first[61]) == (1, 2, 3)
    assert (second[30], second[62], second[61]) == (1, 3, 2)
    assert sum(energy_accounts(occupied)) == sum(energy_accounts(second)) == 6
    assert schedule(second, ("Xt", "Xs"), True) == occupied

    after_source = neutral_stages[1]
    copied = replace_values(after_source, {62: after_source[62]+after_source[30]})
    assert sum(energy_accounts(copied)) == sum(energy_accounts(after_source))+2

    # Wrong endpoint formulas erase the old destination; both collision and
    # missing energy are exhibited instead of installing these maps as laws.
    channel0 = after_source
    channel1 = replace_values(channel0, {62: 1})

    def overwrite_channel(s):
        return replace_values(s, {30: 0, 62: s[30]})

    assert channel0 != channel1
    assert overwrite_channel(channel0) == overwrite_channel(channel1)
    assert sum(energy_accounts(overwrite_channel(channel1))) == sum(energy_accounts(channel1))-1
    receiver0 = neutral_stages[2]
    receiver1 = replace_values(receiver0, {61: 1})

    def overwrite_receiver(s):
        return replace_values(s, {61: s[62], 62: 0})

    assert receiver0 != receiver1
    assert overwrite_receiver(receiver0) == overwrite_receiver(receiver1)
    assert sum(energy_accounts(overwrite_receiver(receiver1))) == sum(energy_accounts(receiver1))-1

    wrong_schedule = schedule(neutral, ("Gs", "Gt", "Xs", "Xt", "Fs", "Ft"), True)
    assert wrong_schedule[31:43] == R and wrong_schedule[61] == 2
    assert wrong_schedule != neutral_stages[-1]
    assert sum(energy_accounts(wrong_schedule)) == 41


def main():
    certificates()
    finite_audit()
    neutral, stages = witness(False)
    witness(True)
    attacks(neutral, stages)
    sys.stdout.write("CHALLENGER PASS: independent transfer audit; occupied channel and disabled control\n")


if __name__ == "__main__":
    main()
