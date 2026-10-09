#!/usr/bin/env python3
"""Exact matrix audit for P-U-NATIVE-FIXED-READ-1.

Original implementation: A. M. Thorn. Apache-2.0.
This program is an independent homogeneous-matrix path. It imports no
primary verifier and implements no direct-coordinate native generator.

Scope: one original F5^6 carrier; origin-zero native U^3; the fixed
source preparation (q,r)=(u-1,1-u); all affine piston preparations
with S=0 and M=y whose post-shot M is affine in (u,y); fixed-read SUM;
the selected two-code context record including its first-tick failure;
and the dependency obstruction for three independent coordinate
subsystems in a common trace layer. No physical preparation, energy,
renewal, coherent instrument or complete contact is asserted.
"""

from itertools import combinations, product
import json

P = 5
FIELD = range(P)


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def matrix(rows):
    return tuple(tuple(value % P for value in row) for row in rows)


def identity(size):
    return tuple(
        tuple(int(i == j) for j in range(size)) for i in range(size)
    )


def transpose(a):
    return tuple(zip(*a))


def mm(a, b):
    need(len(a[0]) == len(b), "matrix dimensions")
    return tuple(
        tuple(
            sum(a[i][k] * b[k][j] for k in range(len(b))) % P
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def mv(a, v):
    need(len(a[0]) == len(v), "matrix/vector dimensions")
    return tuple(sum(x * y for x, y in zip(row, v)) % P for row in a)


def rm(v, a):
    return tuple(
        sum(v[i] * a[i][j] for i in range(len(v))) % P
        for j in range(len(a[0]))
    )


def congruence(a, q):
    return mm(transpose(a), mm(q, a))


def inverse(value):
    value %= P
    need(value != 0, "nonzero inverse")
    return pow(value, P - 2, P)


# Column-vector convention; the seventh coordinate is the constant 1.
G_A = matrix((
    (0, 1, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 1, 0),
    (0, 0, 0, 0, 0, 0, 1),
))
G_B = matrix((
    (0, 0, -1, 0, 0, 0, 0),
    (0, 0, 0, -1, 0, 0, 0),
    (-1, 0, 0, 0, 0, 0, 0),
    (0, -1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, -1, 0, 0),
    (0, 0, 0, 0, 0, -1, 0),
    (0, 0, 0, 0, 0, 0, 1),
))
G_C = matrix((
    (0, 0, -1, 0, 0, 0, 2),
    (0, 0, 0, -1, 0, 1, 1),
    (-1, 0, 0, 0, 0, 0, 2),
    (0, -1, 0, 0, 0, -1, 1),
    (0, 0, 0, 0, -1, 0, 1),
    (0, 0, 0, 0, 0, -1, 0),
    (0, 0, 0, 0, 0, 0, 1),
))
G_D = matrix((
    (-1, 0, 0, 0, 0, 0, 2),
    (0, -1, 0, 0, 0, 0, 1),
    (0, 0, -1, 0, 0, 0, 3),
    (0, 0, 0, -1, 0, 0, 4),
    (0, 0, 0, 0, -1, 0, 1),
    (0, 0, 0, 0, 0, -1, 1),
    (0, 0, 0, 0, 0, 0, 1),
))
G_E = matrix((
    (-1, 0, 0, 0, 0, 0, 2),
    (0, -1, 0, 0, 0, 0, 1),
    (0, 0, -1, 0, 0, 0, 3),
    (0, 0, 0, -1, 0, 0, 4),
    (0, 0, 0, 0, -1, 0, 2),
    (0, 0, 0, 0, 0, -1, 1),
    (0, 0, 0, 0, 0, 0, 1),
))
GENERATORS = (G_A, G_B, G_C, G_D, G_E)
I7 = identity(7)
SHOT = mm(G_E, mm(G_C, G_A))

SHOT_FORMULA = matrix((
    (0, 0, 0, 1, 0, 0, 0),
    (0, 0, 1, 0, 0, -1, 0),
    (0, 1, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 3),
    (0, 0, 0, 0, 1, 0, 1),
    (0, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 0, 0, 1),
))

# M is represented by a symmetric homogeneous quadratic matrix.
# The centered piston coordinates are p-(1,3,4,2).
center = [list(row) for row in I7]
for index, value in enumerate((1, 3, 4, 2)):
    center[index][6] = -value
CENTER = matrix(center)
q_center = [[0] * 7 for _ in range(7)]
for i, j in ((0, 1), (1, 0), (2, 3), (3, 2)):
    q_center[i][j] = 1
Q_M = congruence(CENTER, matrix(q_center))
k_center = [[0] * 7 for _ in range(7)]
k_center[0][0] = 1
k_center[2][2] = 1
Q_K = congruence(CENTER, matrix(k_center))
ROW_S = (1, 1, 1, 1, 0, 0, 0)
ROW_Z = (1, 1, 1, 1, 1, 1, 0)
ROW_X = (0, 0, 0, 0, 3, 2, 1)
ROW_SUM_SOURCE = (0, 0, 0, 0, 2, 3, 0)
Y_FORM = matrix((
    (0, 0, 0),
    (0, 0, 3),
    (0, 3, 0),
))


def scalar(row, v):
    return sum(x * y for x, y in zip(row, v)) % P


def read_m(v):
    return sum(v[i] * Q_M[i][j] * v[j]
               for i in range(7) for j in range(7)) % P


def read_k(v):
    return sum(v[i] * Q_K[i][j] * v[j]
               for i in range(7) for j in range(7)) % P


def read_context(v):
    s = scalar(ROW_S, v)
    return ((1 - s * s) * 2 * v[3]
            + s * s * 2 * (read_k(v) - 1)) % P


def read_sum(v):
    s = scalar(ROW_S, v)
    length_read = (v[0] + v[3]) % P
    return ((1 - s * s) * length_read + s * s * read_m(v)) % P


def selected_step(v, time):
    index = (sum(v[:6]) + 2 * (time.bit_count() & 1)) % P
    return mv(GENERATORS[index], v), index


def origin_three(v):
    word = []
    for time in range(3):
        v, index = selected_step(v, time)
        word.append(index)
    return v, tuple(word)


def embedding(p0, direction):
    # Input columns are (u,y,1); source and receiver are independent.
    return matrix(tuple((0, direction[i], p0[i]) for i in range(4)) + (
        (1, 0, -1),
        (-1, 0, 1),
        (0, 0, 1),
    ))


def affine_coefficients(form):
    if any(form[i][j] for i in range(2) for j in range(2)):
        return None
    # Order is receiver coefficient A, source coefficient B, offset C.
    return ((2 * form[1][2]) % P,
            (2 * form[0][2]) % P,
            form[2][2])


def audit_matrix_laws():
    need(SHOT == SHOT_FORMULA, "whole affine ace identity")
    for g in GENERATORS:
        need(mm(g, g) == I7, "generator involution")
    need(rm(ROW_X, SHOT) == ROW_X, "common source reading across shot")
    need(rm(ROW_SUM_SOURCE, SHOT) == ROW_SUM_SOURCE,
         "SUM source reading across shot")

    # These are exact whole-carrier polynomial identities.
    for g in (G_B, G_D, G_E):
        need(congruence(g, Q_M) == Q_M, "M invariant under b,d,e")
        need(congruence(g, Q_K) == Q_K, "K invariant under b,d,e")
        need(rm(ROW_S, g) == tuple((-x) % P for x in ROW_S),
             "piston S changes sign under b,d,e")

    trace_signs = (1, -1, -1, -1, -1)
    trace_offsets = (0, 0, 2, 2, 3)
    for g, sign, offset in zip(GENERATORS, trace_signs, trace_offsets):
        expected = tuple((sign * x) % P for x in ROW_Z[:6]) + (
            offset % P,
        )
        need(rm(ROW_Z, g) == expected, "trace factor")

    tables = []
    for bit in (0, 1):
        row = []
        for z in FIELD:
            representative = (0, 0, 0, 0, z, 0, 1)
            output = mv(GENERATORS[(z + 2 * bit) % P], representative)
            row.append(scalar(ROW_Z, output))
        tables.append(tuple(row))
    need(tuple(tables) == ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1)),
         "both selected trace tables")
    for initial in FIELD:
        z = initial
        for time in range(3):
            z = tables[time.bit_count() & 1][z]
        need(z == 1, "origin synchronization")
    for z in (1, 4):
        for bit in (0, 1):
            need((z + 2 * bit) % P in (1, 3, 4),
                 "only b,d,e after synchronization")
            need(tables[bit][z] in (1, 4), "stable trace union")

    count = 0
    for first_five in product(FIELD, repeat=5):
        v = tuple(first_five) + ((-sum(first_five)) % P, 1)
        actual, word = origin_three(v)
        need(word == (0, 2, 4), "actual H0 word")
        need(actual == mv(SHOT, v), "all-H0 actual three-tick equality")
        count += 1
    need(count == 3125, "complete H0 cardinality")
    return count


def audit_all_affine_preparations():
    # Every affine piston map in S=0 has one of these 125 bases and
    # one of these 125 directions. No successful family is selected first.
    plane = tuple((a, b, c, (-a - b - c) % P)
                  for a, b, c in product(FIELD, repeat=3))
    accepted = {}
    examined = 0
    for p0, direction in product(plane, repeat=2):
        examined += 1
        e = embedding(p0, direction)
        if congruence(e, Q_M) != Y_FORM:
            continue
        coefficients = affine_coefficients(congruence(mm(SHOT, e), Q_M))
        if coefficients is not None:
            accepted[(p0, direction)] = coefficients
    need(examined == 15625, "all affine S=0 preparation maps")

    # A separately derived closed formula must match the complete search.
    derived = {}
    for b, d in product(FIELD, repeat=2):
        b0 = (b - d - 1) % P
        if b0 == 0:
            continue
        slope = inverse(2 * b0)
        a0 = ((b - 3) + (b + d + 4) * (d - 2)) * inverse(b0) % P
        p0 = (a0, b, (-a0 - b - d) % P, d)
        direction = (slope, 0, (-slope) % P, 0)
        h = (d - b) % P
        coefficients = (
            (h + 2) * inverse(h + 1) % P,
            2 * (h + 2) % P,
            (3 * a0 + 2 * b + 3 * h - 1) % P,
        )
        derived[(p0, direction)] = coefficients
    need(len(derived) == 20, "twenty closed-form preparation maps")
    need(accepted == derived, "complete affine classification")

    unitals = {
        key: coefficients for key, coefficients in accepted.items()
        if (coefficients[0] + coefficients[1]) % P == 1
        and coefficients[2] == 0
    }
    expected_unitals = {
        ((3, 3, 4, 0), (4, 0, 1, 0)): (3, 3, 0),
        ((2, 2, 2, 4), (4, 0, 1, 0)): (3, 3, 0),
        ((0, 3, 4, 3), (2, 0, 3, 0)): (2, 4, 0),
        ((3, 1, 0, 1), (2, 0, 3, 0)): (2, 4, 0),
    }
    need(unitals == expected_unitals, "exactly four unital zero-offset codes")

    native_count = 0
    for (p0, direction), (a, b, offset) in unitals.items():
        e = embedding(p0, direction)
        for u, y in product(FIELD, repeat=2):
            initial = mv(e, (u, y, 1))
            actual, word = origin_three(initial)
            need(scalar(ROW_Z, initial) == 0, "prepared H0")
            need(read_m(initial) == y, "same input receiver reading")
            need(scalar(ROW_X, initial) == u, "same input source reading")
            need(word == (0, 2, 4), "unital code actual ace")
            need(actual == mv(SHOT, initial), "unital code full output")
            need(scalar(ROW_X, actual) == u, "same output source reading")
            need(read_m(actual) == (a * y + b * u + offset) % P,
                 "unital code native receiver output")
            need(scalar(ROW_Z, actual) == 1, "unital code output H1")
            native_count += 1
    need(native_count == 100, "all four times twenty-five native inputs")
    templates = [[list(p0), list(direction), *coefficients]
                 for (p0, direction), coefficients in sorted(accepted.items())]
    unital_codes = [[list(p0), list(direction), *coefficients]
                    for (p0, direction), coefficients in sorted(unitals.items())]
    return (examined, len(accepted), len(unitals), native_count,
            templates, unital_codes)


def audit_persistent_sum():
    count = 0
    for s, t in product(FIELD, repeat=2):
        initial = (t, 0, (-t) % P, 0, (-s) % P, s, 1)
        actual, word = origin_three(initial)
        v = (t + s) % P
        expected = (0, (-v) % P, 1, (v + 3) % P,
                    (1 - s) % P, (1 + s) % P, 1)
        need(scalar(ROW_Z, initial) == 0, "SUM H0 preparation")
        need(read_sum(initial) == t, "same initial SUM reading")
        need(scalar(ROW_SUM_SOURCE, initial) == s, "SUM initial source")
        need(word == (0, 2, 4), "SUM actual ace")
        need(actual == expected, "SUM complete native output")
        need(scalar(ROW_SUM_SOURCE, actual) == s, "SUM source at output")
        need(read_sum(actual) == v, "SUM same receiver reading at output")
        need(scalar(ROW_S, actual) == 4, "SUM stable piston square")
        need(read_m(actual) == v, "SUM invariant stored output")
        # All later times are covered by the exact matrix congruences,
        # S -> -S, and the stable selected alphabet in audit_matrix_laws.
        count += 1
    need(count == 25, "all independent SUM preparations")
    return count


def audit_selected_context():
    selected = (
        ((3, 3, 4, 0), (4, 0, 1, 0), 0),
        ((0, 3, 4, 3), (2, 0, 3, 0), 1),
    )
    raw_initial_witnesses = (
        (3, 3, 4, 0, 0, 0),
        (0, 3, 4, 3, 0, 0),
    )
    raw_output_witnesses = (
        (0, 4, 4, 1, 1, 1),
        (3, 4, 4, 3, 1, 1),
    )
    collision_inputs = []
    collision_outputs = []
    first_tick_witness = None
    count = 0
    for p0, direction, tag in selected:
        e = embedding(p0, direction)
        for u, y in product(FIELD, repeat=2):
            initial = mv(e, (u, y, 1))
            one, index_one = selected_step(initial, 0)
            two, index_two = selected_step(one, 1)
            three, index_three = selected_step(two, 2)
            need((index_one, index_two, index_three) == (0, 2, 4),
                 "selected context actual three-tick word")
            trace = [read_context(v) for v in (initial, one, two, three)]
            need(trace[0] == tag and trace[2] == tag and trace[3] == tag,
                 "context at preparation, second tick and output")
            expected_first = ((2 * y + 3) if tag == 0 else (y + 3)) % P
            need(trace[1] == expected_first, "actual first-tick context")
            need(scalar(ROW_X, initial) == u and scalar(ROW_X, three) == u,
                 "context source at both endpoints")
            need(read_m(initial) == y, "context initial receiver")
            need(read_m(three) == ((3 - tag) * y + (3 + tag) * u) % P,
                 "closed endpoint context law")
            if (u, y) == (1, 0):
                need(initial[:6] == raw_initial_witnesses[tag],
                     "context collision complete initial state")
                need(three[:6] == raw_output_witnesses[tag],
                     "context collision complete output state")
                collision_inputs.append([scalar(ROW_X, initial),
                                         read_m(initial)])
                collision_outputs.append(read_m(three))
                if tag == 0:
                    first_tick_witness = trace
            count += 1
    need(count == 50, "all selected two-code context preparations")
    need(collision_inputs == [[1, 0], [1, 0]], "same incomplete input read")
    need(collision_outputs == [3, 4], "different receiver outputs")
    need(first_tick_witness == [0, 3, 0, 0],
         "context is not an every-native-tick invariant")
    return (count,
            {"input": collision_inputs[0], "outputs": collision_outputs},
            first_tick_witness)


PISTON_PERMUTATIONS = (
    (0, 1, 2, 3),
    (1, 0, 3, 2),
    (2, 3, 0, 1),
    (3, 2, 1, 0),
)


def incoming(block, permutation):
    # This deliberately includes every possible r contribution. A
    # coefficient that is zero only removes dependencies and cannot
    # evade the necessary-condition obstruction.
    result = set()
    for coordinate in block:
        if coordinate < 4:
            result.update((permutation[coordinate], 5))
        else:
            result.add(coordinate)
    return result


def audit_dependency_obstruction():
    # Verify the generator normal form, then closure of its permutation
    # component. Closure of the affine r term is an exact proof identity.
    for g in GENERATORS:
        epsilon = g[4][4]
        need(epsilon in (1, 4) and g[5][5] == epsilon,
             "shared nonzero native sign")
        need(all(g[4][j] == 0 for j in (0, 1, 2, 3, 5)),
             "q depends only on q")
        need(all(g[5][j] == 0 for j in (0, 1, 2, 3, 4)),
             "r depends only on r")
        permutation = []
        for i in range(4):
            support = tuple(j for j in range(4) if g[i][j] != 0)
            need(len(support) == 1, "one piston input per piston output")
            need(g[i][support[0]] == epsilon and g[i][4] == 0,
                 "signed piston permutation and no q input")
            permutation.append(support[0])
        need(tuple(permutation) in PISTON_PERMUTATIONS,
             "native piston permutation class")
    for first, second in product(PISTON_PERMUTATIONS, repeat=2):
        composed = tuple(first[second[i]] for i in range(4))
        need(composed in PISTON_PERMUTATIONS, "Klein permutation closure")

    coordinates = frozenset(range(6))
    count = 0
    for permutation in PISTON_PERMUTATIONS:
        for source_tuple in combinations(range(6), 2):
            source = frozenset(source_tuple)
            remainder = coordinates - source
            for receiver_tuple in combinations(sorted(remainder), 2):
                receiver = frozenset(receiver_tuple)
                reference = remainder - receiver
                source_inputs = incoming(source, permutation)
                receiver_inputs = incoming(receiver, permutation)
                reference_inputs = incoming(reference, permutation)
                necessary = (
                    bool(source_inputs & source)
                    and bool(reference_inputs & reference)
                    and all(receiver_inputs & block
                            for block in (source, receiver, reference))
                )
                need(not necessary,
                     "three-local-factor necessary dependence obstruction")
                count += 1
    need(count == 360, "all ordered three-pair dependency cases")
    return count


def main():
    h0_count = audit_matrix_laws()
    (examined, accepted, unitals, native_count,
     templates, unital_codes) = audit_all_affine_preparations()
    sum_count = audit_persistent_sum()
    dependency_count = audit_dependency_obstruction()
    context_count, collision, first_tick_witness = audit_selected_context()
    report = {
        "status": "PASS",
        "method": "homogeneous-matrix",
        "h0_word_states": h0_count,
        "affine_candidates": examined,
        "affine_preparations": accepted,
        "unital_preparations": unitals,
        "unital_inputs": native_count,
        "sum_inputs": sum_count,
        "dependency_cases": dependency_count,
        "dependency_survivors": 0,
        "context_inputs": context_count,
        "context_collision": collision,
        "first_tick_context_witness": first_tick_witness,
        "templates": templates,
        "unital_codes": unital_codes,
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
