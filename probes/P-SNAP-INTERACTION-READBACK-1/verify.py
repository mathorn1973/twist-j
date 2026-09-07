#!/usr/bin/env python3
"""Exact standalone finite audit of the separately written proofs.

Python >= 3.10; no external files, randomness or floating point.
Mathematical failures are retained in JSON with exit zero. Unexpected
exceptions remain uncaught and constitute an integrity/runtime STOP.
"""

import json
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial


NAME = "P-SNAP-INTERACTION-READBACK-1"
COUNTS = {}
FAILURES = []
CELLS = (None, 0, 1, -1)  # None=BLANK; numeric zero is PRESENT(0).


def check(condition, section, case):
    COUNTS[section] = COUNTS.get(section, 0) + 1
    if not condition:
        FAILURES.append((section, case))


def matrix(rows):
    return tuple(tuple(Q(value) for value in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def diagonal(entries):
    return matrix([[entries[i] if i == j else 0 for j in range(len(entries))]
                   for i in range(len(entries))])


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, column)) for column in transpose(b))
                 for row in a)


def matvec(a, vector):
    return tuple(sum(x * y for x, y in zip(row, vector)) for row in a)


def subtract(a, b):
    return tuple(tuple(x - y for x, y in zip(row_a, row_b)) for row_a, row_b in zip(a, b))


def block_diagonal(*blocks):
    total = sum(len(block) for block in blocks)
    result = [[Q(0) for _ in range(total)] for _ in range(total)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                result[offset + i][offset + j] = value
        offset += len(block)
    return matrix(result)


def rank(a):
    rows = [list(row) for row in a]
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][column]
        rows[pivot_row] = [entry / value for entry in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row:
                coefficient = rows[i][column]
                rows[i] = [x - coefficient * y for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def inverse(a):
    n = len(a)
    rows = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for column in range(n):
        pivot = next((i for i in range(column, n) if rows[i][column]), None)
        if pivot is None:
            raise ValueError("singular matrix in a purportedly nonsingular fixture")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        value = rows[column][column]
        rows[column] = [entry / value for entry in rows[column]]
        for i in range(n):
            if i != column:
                coefficient = rows[i][column]
                rows[i] = [x - coefficient * y for x, y in zip(rows[i], rows[column])]
    return matrix([row[n:] for row in rows])


def basis(n):
    return [tuple(Q(int(i == j)) for i in range(n)) for j in range(n)]


def polarization_samples(n):
    unit = basis(n)
    samples = [(Q(0),) * n] + unit + [tuple(-x for x in vector) for vector in unit]
    for i in range(n):
        for j in range(i + 1, n):
            for sign in (-1, 1):
                samples.append(tuple(x + sign * y for x, y in zip(unit[i], unit[j])))
    return samples


def energy(gram, vector):
    return sum(x * y for x, y in zip(vector, matvec(gram, vector)))


def zero_batch_boundary():
    section = "ZERO_BATCH_ERASURE"
    zero = (Q(0),) * 5
    channels = (zero, zero)
    context = ("stabilizer-E-k0", ("LOW", "HIGH"), Q(1))
    # Minimal exact inherited fixture: context, energy, counts, remainders,
    # lifetime counts, signed ordered batches. The zero batch is retained.
    account = (context, Q(0), (0, 0), (Q(0), Q(0)), (0, 0))
    ready = (account, ())
    zero_batch = (0, 0, channels, Q(0), ((), ()), (0, 0), (Q(0), Q(0)))
    deposited = (account, (zero_batch,))
    reread = ready
    check(sum(value * value for branch in channels for value in branch) == 0,
          section, "admitted-zero-input-energy")
    check(deposited[0] == reread[0], section, "same-complete-scalar-account")
    check(len(deposited[1]) - len(ready[1]) == 1 and len(reread[1]) - len(ready[1]) == 0,
          section, "batch-delta-one-versus-zero")
    check(deposited != reread, section, "retained-histories-differ")
    port = zero + zero
    cold_swap_before = (port, port)
    cold_swap_after = (cold_swap_before[1], cold_swap_before[0])
    passive_before = (port, port)
    passive_after = passive_before
    observation = lambda before, after: (before, after,
        tuple(sum(x * x for x in vector) for vector in before + after))
    check(observation(cold_swap_before, cold_swap_after) == observation(passive_before, passive_after),
          section, "equal-zero-amplitude-transition-observations")
    check(deposited[0][2] == reread[0][2] == (0, 0), section, "zero-marks-in-both")


def signed_permutations(n):
    for permutation in permutations(range(n)):
        for signs in product((-1, 1), repeat=n):
            yield matrix([[signs[j] if i == permutation[j] else 0 for j in range(n)]
                          for i in range(n)])


def two_port_loaders():
    section = "TWO_PORT_LOADERS"
    fixtures = []
    for n in range(1, 4):
        choices = list(signed_permutations(n))
        check(len(set(choices)) == factorial(n) * 2 ** n, section, ("signed-permutation-coverage", n))
        fixtures.extend(("signed-{}-{}".format(n, k), eye(n), b) for k, b in enumerate(choices))
    pairs = ((Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13)), (Q(8, 17), Q(15, 17)))
    rotations = [matrix(((c, -s), (s, c))) for c, s in pairs]
    fixtures.extend(("rotation-{}".format(k), eye(2), b) for k, b in enumerate(rotations))
    d = diagonal((1, 2))
    d_inverse = diagonal((1, Q(1, 2)))
    for k, b in enumerate(list(signed_permutations(2)) + rotations):
        conjugate = multiply(multiply(d_inverse, b), d)
        fixtures.append(("weighted-{}".format(k), diagonal((1, 4)), conjugate))
    for label, gram, b in fixtures:
        n = len(gram)
        ident = eye(n)
        zero_row = (Q(0),) * n
        w = matrix([zero_row + row for row in b] + [row + zero_row for row in ident])
        total_gram = block_diagonal(gram, gram)
        check(multiply(multiply(transpose(b), gram), b) == gram, section, (label, "B-isometry"))
        check(rank(b) == n, section, (label, "B-full-rank"))
        check(multiply(multiply(transpose(w), total_gram), w) == total_gram,
              section, (label, "whole-orthogonality"))
        check(multiply(w, w) == block_diagonal(b, b), section, (label, "square-blocks"))
        for i, vector in enumerate(basis(n)):
            source = vector + zero_row
            stored = zero_row + vector
            check(matvec(w, source) == stored, section, (label, "perfect-basis-load", i))
            check(matvec(w, stored) == matvec(b, vector) + zero_row,
                  section, (label, "record-export", i))
            check(matvec(w, stored) != stored, section, (label, "fails-passive-retention", i))
        for i, vector in enumerate(polarization_samples(2 * n)):
            after = matvec(w, vector)
            check(energy(total_gram, after) == energy(total_gram, vector),
                  section, (label, "polarized-energy", i))
            twice = matvec(w, after)
            expected = matvec(b, vector[:n]) + matvec(b, vector[n:])
            check(twice == expected, section, (label, "direct-two-applications", i))
    check(len(fixtures) == 72, section, "complete-frozen-fixture-inventory")

    section = "ALL_SIGNED_PORT_MAPS"
    for m in (1, 2):
        n = 2 * m
        vectors = basis(n)
        count = loaders = invariant = 0
        for index, w in enumerate(signed_permutations(n)):
            count += 1
            images = [matvec(w, vector) for vector in vectors]
            cold_loader = all(images[i] == vectors[m + i] for i in range(m))
            upper_left = matrix([row[:m] for row in w[:m]])
            upper_right = matrix([row[m:] for row in w[:m]])
            lower_left = matrix([row[:m] for row in w[m:]])
            lower_right = matrix([row[m:] for row in w[m:]])
            zero_block = matrix([[0] * m for _ in range(m)])
            classified = (upper_left == lower_right == zero_block and lower_left == eye(m)
                          and multiply(transpose(upper_right), upper_right) == eye(m))
            record_invariant = all(all(value == 0 for value in images[m + i][:m]) for i in range(m))
            no_incoming_transfer = all(all(value == 0 for value in images[i][m:]) for i in range(m))
            projected_passive = all(images[m + i][m:] == vectors[i][:m] for i in range(m))
            pointwise_fixed = all(images[m + i] == vectors[m + i] for i in range(m))
            check(multiply(transpose(w), w) == eye(n), section, (m, index, "orthogonal-candidate"))
            check(cold_loader == classified, section, (m, index, "loader-iff-block-class"))
            check(record_invariant == no_incoming_transfer, section, (m, index, "invariant-record-separation"))
            check(projected_passive == pointwise_fixed and (not projected_passive or no_incoming_transfer),
                  section, (m, index, "projected-passivity-forces-exact-fixation"))
            check(not cold_loader or not projected_passive, section, (m, index, "load-and-passive-incompatible"))
            loaders += int(cold_loader)
            invariant += int(record_invariant)
        check(count == factorial(n) * 2 ** n, section, (m, "complete-signed-census"))
        check(loaders == factorial(m) * 2 ** m, section, (m, "loader-census"))
        check(0 < invariant < count, section, (m, "both-invariant-and-transfer-controls"))


def fresh_embeddings():
    section = "FRESH_ISOMETRIC_SPACE"
    v = (Q(1), Q(2), Q(2))
    householder = matrix([[Q(int(i == j)) - Q(2, 9) * v[i] * v[j]
                          for j in range(3)] for i in range(3)])
    check(multiply(transpose(householder), householder) == eye(3), section, "rational-Householder")
    embeddings = (
        ("matched", eye(1), eye(1), matrix(((1,),))),
        ("two-weighted-coordinates", eye(1), diagonal((2, 2)), matrix(((Q(1, 2),), (Q(1, 2),)))),
        ("rotated-plane", eye(2), eye(3), matrix([row[:2] for row in householder])),
    )
    for label, source_gram, fresh_gram, jmap in embeddings:
        m, k = len(source_gram), len(fresh_gram)
        jstar = multiply(multiply(inverse(source_gram), transpose(jmap)), fresh_gram)
        projection = multiply(jmap, jstar)
        complement = subtract(eye(k), projection)
        check(multiply(multiply(transpose(jmap), fresh_gram), jmap) == source_gram,
              section, (label, "isometric-embedding"))
        check(rank(jmap) == m and k >= m, section, (label, "rank-and-necessary-dimension"))
        check(multiply(jstar, jmap) == eye(m), section, (label, "adjoint-left-inverse"))
        check(multiply(projection, projection) == projection, section, (label, "projection-idempotence"))
        check(multiply(transpose(projection), fresh_gram) == multiply(fresh_gram, projection),
              section, (label, "projection-Gram-self-adjoint"))
        check(all(value == 0 for row in multiply(jstar, complement) for value in row),
              section, (label, "orthogonal-complement-kernel"))
        for old in range(3):
            old_gram = diagonal((3, 5)[:old])
            dim = m + old + k  # Frozen order: source, old record, fresh capacity.
            rows = [[Q(0) for _ in range(dim)] for _ in range(dim)]
            for i in range(old):
                rows[m + i][m + i] = Q(1)
            for i in range(m):
                for a in range(k):
                    rows[i][m + old + a] = jstar[i][a]
            for a in range(k):
                for i in range(m):
                    rows[m + old + a][i] = jmap[a][i]
                for b in range(k):
                    rows[m + old + a][m + old + b] = complement[a][b]
            w = matrix(rows)
            gram = block_diagonal(source_gram, old_gram, fresh_gram)
            check(multiply(multiply(transpose(w), gram), w) == gram,
                  section, (label, old, "whole-orthogonality"))
            check(multiply(w, w) == eye(dim), section, (label, old, "involution"))
            for i, vector in enumerate(basis(old)):
                point = (Q(0),) * m + vector + (Q(0),) * k
                check(matvec(w, point) == point, section, (label, old, "fix-old-basis", i))
            for i, vector in enumerate(basis(m)):
                point = vector + (Q(0),) * (old + k)
                expected = (Q(0),) * (m + old) + matvec(jmap, vector)
                check(matvec(w, point) == expected, section, (label, old, "perfect-source-load", i))
            for i, vector in enumerate(basis(k)):
                residual = matvec(complement, vector)
                point = (Q(0),) * (m + old) + residual
                check(matvec(w, point) == point, section, (label, old, "fix-unused-fresh-space", i))
            for i, vector in enumerate(polarization_samples(dim)):
                source = vector[:m]
                old_value = vector[m:m + old]
                fresh = vector[m + old:]
                expected_fresh = tuple(x + y for x, y in zip(matvec(jmap, source), matvec(complement, fresh)))
                expected = matvec(jstar, fresh) + old_value + expected_fresh
                check(matvec(w, vector) == expected and energy(gram, expected) == energy(gram, vector),
                      section, (label, old, "direct-map-and-energy", i))
    for numerator in range(-12, 13):
        for denominator in range(1, 13):
            value = Q(numerator, denominator)
            check(2 * value * value != 1, section, ("bounded-nonsquare-control", numerator, denominator))
    shear = matrix(((1, 0), (1, 1)))
    check(multiply(inverse(shear), shear) == eye(2), section, "shear-invertible")
    check(matvec(shear, (0, 1)) == (0, 1) and matvec(shear, (1, 0)) == (1, 1),
          section, "shear-fixes-old-but-copies-source")
    check(multiply(transpose(shear), shear) != eye(2), section, "shear-is-not-orthogonal")


def flow(state):
    head, source, receiver = state
    source, receiver = list(source), list(receiver)
    source[head], receiver[head] = receiver[head], source[head]
    return ((head + 1) % len(source), tuple(source), tuple(receiver))


def reverse_flow(state):
    head, source, receiver = state
    head = (head - 1) % len(source)
    source, receiver = list(source), list(receiver)
    source[head], receiver[head] = receiver[head], source[head]
    return (head, tuple(source), tuple(receiver))


def emission(before, after):
    """Active-receiver pre/post formula, without an opcode input.

    Its zero value on an unchanged query pair does not assert that the query
    executed FLOW; the finite bank's actual steps are supplied separately.
    """
    head = before[0]
    if before[2][head] is None and after[2][head] is not None:
        return ((head, after[2][head]),)
    return ()


def cell_energy(cell):
    return 0 if cell is None else cell * cell


def accounts(state):
    cells = state[1] + state[2]
    return (sum(cell is not None for cell in cells), sum(cell_energy(cell) for cell in cells))


def read_cell(state, address):
    return state[2][address]


def amplitude_observation(state):
    return (state[0], tuple(0 if cell is None else cell for cell in state[1]),
            tuple(0 if cell is None else cell for cell in state[2]))


def bank_protocol():
    section = "COLD_BANK_PREFIXES"
    tested = 0
    for size in range(1, 7):
        for incoming in product(CELLS, repeat=size):
            tested += 1
            initial = (0, incoming, (None,) * size)
            state = initial
            initial_account = accounts(initial)
            marks = []
            for step in range(size):
                after = flow(state)
                marks.extend(emission(state, after))
                expected = ((step + 1) % size, (None,) * (step + 1) + incoming[step + 1:],
                            incoming[:step + 1] + (None,) * (size - step - 1))
                check(after == expected, section, ("first-lap-prefix", size, incoming, step))
                check(reverse_flow(after) == state and accounts(after) == initial_account,
                      section, ("inverse-energy-occupancy", size, incoming, step))
                old_value = read_cell(after, 0)
                check(read_cell(after, 0) == old_value == incoming[0] and emission(after, after) == (),
                      section, ("passive-repeat-is-not-flow", size, incoming, step))
                state = after
            expected_marks = [(address, value) for address, value in enumerate(incoming) if value is not None]
            check(marks == expected_marks and len({address for address, _ in marks}) == len(marks),
                  section, ("all-arrivals-and-distinct-IDs", size, incoming))
            for step in range(size):
                after = flow(state)
                expected = ((step + 1) % size, incoming[:step + 1] + (None,) * (size - step - 1),
                            (None,) * (step + 1) + incoming[step + 1:])
                check(after == expected and reverse_flow(after) == state
                      and accounts(after) == initial_account and emission(state, after) == (),
                      section, ("wrap-exports-old-record", size, incoming, step))
                state = after
            check(state == initial, section, ("two-laps-return", size, incoming))
    check(tested == sum(4 ** size for size in range(1, 7)), section, "cold-bank-coverage")

    section = "ALL_BANK_STATES"
    for size in range(1, 4):
        images = set()
        count = 0
        for contents in product(CELLS, repeat=2 * size):
            for head in range(size):
                count += 1
                state = (head, contents[:size], contents[size:])
                after = flow(state)
                images.add(after)
                check(reverse_flow(after) == state and flow(reverse_flow(state)) == state,
                      section, ("two-sided-inverse", size, head, contents))
                before_occ = sum(cell is not None for cell in state[2])
                after_occ = sum(cell is not None for cell in after[2])
                arrival = int(state[2][head] is None and state[1][head] is not None)
                returning = int(state[1][head] is None and state[2][head] is not None)
                check(accounts(after) == accounts(state) and after_occ - before_occ == arrival - returning
                      and len(emission(state, after)) == arrival,
                      section, ("exact-flow-balance", size, head, contents))
                lap = state
                for _ in range(size):
                    lap = flow(lap)
                full_lap = lap
                for _ in range(size):
                    full_lap = flow(full_lap)
                check(lap == (head, state[2], state[1]) and full_lap == state,
                      section, ("all-state-lap-and-double-lap", size, head, contents))
        check(count == size * 4 ** (2 * size) and len(images) == count,
              section, ("full-bijection-census", size))


def bank_boundaries():
    section = "PRESENCE_AND_QUERY_BOUNDARIES"
    zero_arrival = (0, (0,), (None,))
    zero_after = flow(zero_arrival)
    idle = (0, (None,), (None,))
    idle_after = flow(idle)
    zero_transition = (amplitude_observation(zero_arrival), amplitude_observation(zero_after))
    idle_transition = (amplitude_observation(idle), amplitude_observation(idle_after))
    passive_transition = (amplitude_observation(zero_after), amplitude_observation(zero_after))
    check(zero_transition == idle_transition == passive_transition,
          section, "same-amplitudes-for-zero-arrival-idle-and-reread")
    check(emission(zero_arrival, zero_after) == ((0, 0),)
          and emission(idle, idle_after) == emission(zero_after, zero_after) == (),
          section, "presence-separates-otherwise-identical-amplitudes")
    check(cell_energy(None) == cell_energy(0) == 0 and None != 0,
          section, "blank-is-not-occupied-zero")
    for payload in (0, 1, -1):
        initial = (0, (payload, payload), (None, None))
        first = flow(initial)
        second = flow(first)
        check(emission(initial, first) + emission(first, second) == ((0, payload), (1, payload)),
              section, ("equal-arrivals-distinct-cells", payload))
        check(read_cell(second, 0) == read_cell(second, 0) == payload
              and emission(second, second) == (), section, ("same-cell-passive-rereads", payload))
    warm = (0, (1,), (-1,))
    warm_after = flow(warm)
    check(warm_after != warm and cell_energy(warm_after[2][0]) - cell_energy(warm[2][0]) == 0,
          section, "signed-change-at-zero-net-energy-gain")
    check(flow(warm_after) == warm, section, "two-couplings-hidden-by-endpoint-return")
    cold = (0, (1,), (None,))
    cold_after = flow(cold)
    check(cell_energy(cold_after[2][0]) - cell_energy(cold[2][0]) == 1
          and emission(cold, cold_after) == ((0, 1),), section, "cold-nonzero-transfer")


def main():
    zero_batch_boundary()
    two_port_loaders()
    fresh_embeddings()
    bank_protocol()
    bank_boundaries()
    report = {
        "name": NAME,
        "counts": COUNTS,
        "total": sum(COUNTS.values()),
        "failures": [{"section": section, "case": case} for section, case in FAILURES],
        "result": "FALSIFIED" if FAILURES else "PROOF_AUDIT_PASS",
        "scope": "L1 finite proof audit; presence, fresh capacity and passive queries are explicit model choices",
    }
    print(json.dumps(report, ensure_ascii=True, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
