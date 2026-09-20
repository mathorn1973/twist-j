#!/usr/bin/env python3
"""Independent exact finite-premise audit; the all-time proof is PROOF.md.

No accepted verifier is imported or consulted. Native maps are homogeneous
affine matrices, and amplitudes use exact Z[j]/Phi_5(j) coefficients.
"""

from itertools import product


MOD = 5
SIZE = 7


def row(*terms):
    out = [0] * SIZE
    for index, coefficient in terms:
        out[index] += coefficient
    return tuple(value % MOD for value in out)


IDENTITY = tuple(row((i, 1)) for i in range(SIZE))


def affine(rows):
    return tuple(rows) + (IDENTITY[6],)


# Coordinates a,b,c,d,q,r,1. These are transcriptions of the public formulas.
GENERATORS = {
    "a": affine([IDENTITY[1], IDENTITY[0], IDENTITY[3], IDENTITY[2],
                 IDENTITY[4], IDENTITY[5]]),
    "b": affine([row((2, -1)), row((3, -1)), row((0, -1)),
                 row((1, -1)), row((4, -1)), row((5, -1))]),
    "c": affine([row((2, -1), (6, 2)), row((3, -1), (5, 1), (6, 1)),
                 row((0, -1), (6, 2)), row((1, -1), (5, -1), (6, 1)),
                 row((4, -1), (6, 1)), row((5, -1))]),
    "d": affine([row((0, -1), (6, 2)), row((1, -1), (6, 1)),
                 row((2, -1), (6, 3)), row((3, -1), (6, 4)),
                 row((4, -1), (6, 1)), row((5, -1), (6, 1))]),
    "e": affine([row((0, -1), (6, 2)), row((1, -1), (6, 1)),
                 row((2, -1), (6, 3)), row((3, -1), (6, 4)),
                 row((4, -1), (6, 2)), row((5, -1), (6, 1))]),
}


def compose(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(SIZE))
                       % MOD for j in range(SIZE)) for i in range(SIZE))


def apply(matrix, point):
    vector = tuple(point) + (1,)
    return tuple(sum(a * b for a, b in zip(r, vector)) % MOD
                 for r in matrix[:6])


def shift(delta, source=False):
    out = [list(r) for r in IDENTITY]
    if source:
        out[1][6], out[3][6] = delta % MOD, (-delta) % MOD
    else:
        out[4][6], out[5][6] = (-delta) % MOD, delta % MOD
    return tuple(tuple(r) for r in out)


def sum_rows(matrix, indices):
    return tuple(sum(matrix[i][j] for i in indices) % MOD
                 for j in range(SIZE))


def affine_audit():
    trace = row(*((i, 1) for i in range(6)))
    source_sum = row(*((i, 1) for i in range(4)))
    for name, matrix in GENERATORS.items():
        assert compose(matrix, matrix) == IDENTITY, name
    for delta in range(5):
        paired = shift(delta)
        assert compose(paired, shift(-delta)) == IDENTITY
        assert sum_rows(paired, range(6)) == trace
        for name in "bde":
            matrix = GENERATORS[name]
            left = compose(matrix, paired)
            assert left == compose(shift(-delta), matrix), (name, delta)
            assert left[:4] == matrix[:4], (name, delta, "source")
            assert sum_rows(matrix, range(4)) == tuple(-c % MOD for c in source_sum)
            assert all(matrix[i][j] == 0 for i in range(4) for j in (4, 5))
        assert compose(GENERATORS["a"], paired) == compose(paired, GENERATORS["a"])
        assert compose(GENERATORS["c"], paired) == compose(
            shift(delta, source=True), compose(shift(-delta), GENERATORS["c"]))
    expected = {(1, 0): ("b", 4), (1, 1): ("d", 1),
                (4, 0): ("e", 4), (4, 1): ("b", 1)}
    for (z, bit), (name, next_z) in expected.items():
        assert "abcde"[(z + 2 * bit) % 5] == name
        trace_after = sum_rows(GENERATORS[name], range(6))
        assert trace_after[:6] == (4,) * 6
        assert (-z + trace_after[6]) % 5 == next_z
        assert next_z in (1, 4)
    origin = (0,) * 6
    assert apply(compose(GENERATORS["c"], shift(1)), origin)[:4] == (2, 2, 2, 0)
    assert apply(compose(shift(-1), GENERATORS["c"]), origin)[:4] == (2, 1, 2, 1)
    assert compose(GENERATORS["a"], shift(1)) != compose(shift(-1), GENERATORS["a"])
    print("affine_coefficients=5 generators; 15 stable conjugacies; 4 selectors PASS")


def reduced_audit():
    count = 0
    for epsilon, mark in product((1, -1), range(5)):
        images = set()
        for error, old in product(range(5), repeat=2):
            after_write = (error + mark) % 5
            after_wait = epsilon * after_write % 5
            actual = (epsilon * old % 5, epsilon * after_wait % 5)
            expected = (epsilon * old % 5, (error + mark) % 5)
            assert actual == expected
            images.add(actual)
            inverse = ((actual[1] - mark) % 5, epsilon * actual[0] % 5)
            assert inverse == (error, old)
            # Covariance: exchange immediately, then let the port evolve.
            immediate = (old, (error + mark) % 5)
            assert actual == (epsilon * immediate[0] % 5, immediate[1])
            # A signed exchange squares to identity on the full pair.
            exchange = (epsilon * old % 5, epsilon * error % 5)
            assert (epsilon * exchange[1] % 5, epsilon * exchange[0] % 5) == (error, old)
            if error == old == 0:
                assert actual == (0, mark)
            if old != 0:
                assert actual[0] != 0
            if error != 0:
                assert actual[1] != mark
            count += 1
        assert len(images) == 25
    assert count == 250
    # Odd waiting followed by an unsigned exchange writes 4 instead of 1.
    assert (-1 * 1) % 5 == 4 != 1
    print("reduced_pairs=250; bijection, covariance, readiness and capacity PASS")


ZERO = (0, 0, 0, 0)


def cyclotomic_reduce(coefficients):
    assert len(coefficients) == 5
    return tuple(coefficients[i] - coefficients[4] for i in range(4))


def root_power(exponent):
    coefficients = [0] * 5
    coefficients[exponent % 5] = 1
    return cyclotomic_reduce(coefficients)


def add(*elements):
    return tuple(sum(element[i] for element in elements) for i in range(4))


def scale(number, element):
    return tuple(number * value for value in element)


def multiply(left, right):
    out = [0] * 5
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[(i + j) % 5] += a * b
    return cyclotomic_reduce(out)


def conjugate(element):
    return add(*(scale(value, root_power(-i)) for i, value in enumerate(element)))


def source_basis_audit():
    order = (1, 2, 4, 3)
    hadamard = ((1, 1, 1, 1), (1, -1, 1, -1),
                (1, 1, -1, -1), (1, -1, -1, 1))
    # W=(sqrt(5)/10)*raw. Cancel the nonzero scalar before testing 4DW=W11^T.
    raw = tuple(tuple(add(*(scale(hadamard[k][a], root_power(order[a] * power))
                            for a in range(4))) for power in range(1, 5))
                for k in range(4))
    sqrt5 = cyclotomic_reduce((1, 2, 0, 0, 2))
    assert multiply(sqrt5, sqrt5) == (5, 0, 0, 0)
    for k, j in product(range(4), repeat=2):
        assert add(*raw[k]) == (scale(4, raw[k][j]) if k == 0 else ZERO)
        gram = add(*(multiply(conjugate(raw[i][k]), raw[i][j]) for i in range(4)))
        assert gram == ((16 if k == j else -4), 0, 0, 0)
    # Exact source HIGH input v=(1,-1,0,0): endpoint LOW is zero,
    # while the sum of endpoint amplitudes is not zero.
    high = tuple(add(raw[k][0], scale(-1, raw[k][1])) for k in range(4))
    assert high[0] == ZERO and add(*high) != ZERO
    print("cyclotomic_W=16 intertwining and 16 Gram entries; two bases distinguished PASS")


def joint_unit(h, j, records):
    return {((h, records[h]), (j, records[j])): 1}


def trace_archive(operator):
    out = {}
    for ((h, a), (j, b)), value in operator.items():
        if a == b:
            out[(h, j)] = out.get((h, j), 0) + value
    return out


def coherence_audit():
    marks = (1, 2, 2, 2)
    coarse = tuple((mark,) for mark in marks)
    fine = tuple((mark,) for mark in (1, 2, 4, 3))
    retained = fine_retained = cross_joint = 0
    for h, j in product(range(4), repeat=2):
        unit = {(h, j): 1}
        joint = joint_unit(h, j, coarse)
        assert len(joint) == 1  # Including every LOW/HIGH cross term.
        expected = unit if marks[h] == marks[j] else {}
        assert trace_archive(joint) == expected
        retained += bool(expected)
        cross_joint += marks[h] != marks[j]
        for outcome in (1, 2):
            conditioned = {pair: value for pair, value in joint.items()
                           if pair[0][1] == (outcome,) and pair[1][1] == (outcome,)}
            assert trace_archive(conditioned) == (unit if marks[h] == marks[j] == outcome else {})
        fine_trace = trace_archive(joint_unit(h, j, fine))
        assert fine_trace == (unit if h == j else {})
        fine_retained += bool(fine_trace)
        if h != j and h > 0 and j > 0:
            assert trace_archive(joint) == unit and fine_trace == {}
        # Reusing the same transported mark in three fresh cells.
        records = tuple(() for _ in marks)
        for repeat in range(1, 4):
            records = tuple(records[i] + (marks[i],) for i in range(4))
            repeated = joint_unit(h, j, records)
            assert records[h] == (marks[h],) * repeat
            assert records[j] == (marks[j],) * repeat
            assert trace_archive(repeated) == expected
    assert (retained, fine_retained, cross_joint) == (10, 4, 6)
    print("matrix_units=16; joint cross terms=6; coarse/fine survivors=10/4; repetition PASS")


def main():
    print("P-QDD-UNINTERRUPTED-RECORD-1 independent breaker")
    affine_audit()
    reduced_audit()
    source_basis_audit()
    coherence_audit()
    print("finite_audit=PASS all_durations=WRITTEN_INDUCTION physical_realization=OPEN")


if __name__ == "__main__":
    main()
