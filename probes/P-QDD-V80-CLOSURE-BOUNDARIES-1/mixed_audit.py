"""Exact finite audit for MIXED-PROOF.md; imported only by the pinned verifier.

No import-time execution, file I/O, external data, randomness or floating point.
The universal Kraus statements are carried by the written proof.
"""

from fractions import Fraction as F
from itertools import permutations


def matrix(rows):
    return tuple(tuple(F(value) for value in row) for row in rows)


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    assert len(a[0]) == len(b)
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def scale(c, a):
    return tuple(tuple(c * value for value in row) for row in a)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br))
                 for ar, br in zip(a, b))


def subtract(a, b):
    return add(a, scale(F(-1), b))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def rank(a):
    work = [list(row) for row in a]
    pivot_row = 0
    for col in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work))
                      if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][col]
        work[pivot_row] = [value / divisor for value in work[pivot_row]]
        for r in range(len(work)):
            if r != pivot_row:
                coefficient = work[r][col]
                work[r] = [x - coefficient * y
                           for x, y in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def inverse(a):
    n = len(a)
    work = [list(a[i]) + list(identity(n)[i]) for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if work[r][col])
        work[col], work[pivot] = work[pivot], work[col]
        divisor = work[col][col]
        work[col] = [value / divisor for value in work[col]]
        for r in range(n):
            if r != col:
                coefficient = work[r][col]
                work[r] = [x - coefficient * y
                           for x, y in zip(work[r], work[col])]
    assert tuple(tuple(row[:n]) for row in work) == identity(n)
    return tuple(tuple(row[n:]) for row in work)


def determinant3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def audit():
    """Return compact summary lines after exact finite certificate assertions."""
    h = matrix([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
    a = matrix([[-1, -1, F(-3, 4)], [0, 0, F(1, 4)],
                [1, 0, F(1, 4)]])
    eye = identity(3)
    zero = scale(F(0), eye)
    h_inv = inverse(h)

    def sharp(x):
        return multiply(multiply(h_inv, transpose(x)), h)

    def product(*items):
        result = items[0]
        for item in items[1:]:
            result = multiply(result, item)
        return result

    def projector(v):
        dual = multiply(transpose(v), h)
        norm = multiply(dual, v)[0][0]
        assert norm > 0
        return scale(1 / norm, multiply(v, dual))

    def flatten(x):
        return tuple(value for row in x for value in row)

    assert h[0][0] == 2
    assert h[0][0] * h[1][1] - h[0][1] * h[1][0] == 3
    assert determinant3(h) == 4
    assert determinant3(a) == F(-1, 4)
    assert trace(a) == F(-3, 4)
    assert subtract(h, product(transpose(a), h, a)) == matrix(
        [[0, 0, 0], [0, 0, 0], [0, 0, F(5, 4)]]
    )
    d = (matrix([[-1], [-1], [3]]),
         matrix([[11], [-5], [-1]]),
         matrix([[-9], [-25], [-5]]))
    assert multiply(sharp(a), d[0]) == scale(F(1, 4), d[1])
    assert multiply(sharp(a), d[1]) == scale(F(1, 4), d[2])
    columns = tuple(tuple(d[j][i][0] for j in range(3)) for i in range(3))
    assert determinant3(columns) == -1024
    assert product(transpose(d[0]), h, d[1])[0][0] == -4
    assert product(transpose(d[0]), h, d[2])[0][0] == -20
    projectors = tuple(projector(v) for v in d)
    for r in projectors:
        assert multiply(r, r) == r
        assert sharp(r) == r
        assert trace(r) == 1
        assert rank(r) == 1

    powers = [eye]
    for _ in range(3):
        powers.append(multiply(powers[-1], a))
    b = tuple(multiply(sharp(p), p) for p in powers)
    defect_traces = (F(15, 16), F(215, 256), F(2815, 4096))
    for n in range(3):
        defect = subtract(b[n], b[n + 1])
        assert defect == product(sharp(powers[n]), subtract(eye, b[1]),
                                 powers[n])
        assert trace(defect) == defect_traces[n]
        assert defect == scale(defect_traces[n], projectors[n])
        assert rank(defect) == 1

    units = tuple(matrix([[int(row == i and col == j) for col in range(3)]
                          for row in range(3)])
                  for i in range(3) for j in range(3))
    columns_commutator = []
    for unit in units:
        columns_commutator.append(tuple(
            value for r in projectors
            for value in flatten(subtract(multiply(unit, r), multiply(r, unit)))
        ))
    commutator_system = transpose(tuple(columns_commutator))
    assert rank(commutator_system) == 8
    assert all(subtract(multiply(eye, r), multiply(r, eye)) == zero
               for r in projectors)

    span = tuple(tuple(d[j][i][0] for j in range(2)) for i in range(3))
    span_gram = product(transpose(span), h, span)
    span_projector = product(span, inverse(span_gram), transpose(span), h)
    complement = subtract(eye, span_projector)
    assert sharp(span_projector) == span_projector
    assert multiply(span_projector, span_projector) == span_projector
    assert rank(span_projector) == 2
    assert add(product(sharp(span_projector), span_projector),
               product(sharp(complement), complement)) == eye

    def pinching(x):
        return add(product(span_projector, x, span_projector),
                   product(complement, x, complement))

    assert pinching(b[1]) == b[1]
    assert pinching(b[2]) == b[2]
    assert pinching(b[3]) != b[3]
    assert pinching(projectors[2]) != projectors[2]
    assert any(pinching(unit) != unit for unit in units)

    group = []
    for perm in permutations(range(4)):
        rep = matrix([[int(row == perm[col]) - int(row == perm[3])
                       for col in range(3)] for row in range(3)])
        assert product(sharp(rep), rep) == eye
        group.append(rep)
    assert len(set(group)) == 24
    assert F(1, 36) + F(1, 144) + F(1, 144) == F(1, 24)
    assert sum(F(1, 36) + 2 * F(1, 144) for _ in group) == 1

    def depolarizing(x):
        return scale(trace(x) / 3, eye)

    for unit in units:
        twirl = zero
        for rep in group:
            twirl = add(twirl, scale(F(1, 24), product(rep, unit, sharp(rep))))
        assert twirl == depolarizing(unit)
        assert depolarizing(depolarizing(unit)) == depolarizing(unit)
        assert trace(depolarizing(unit)) == trace(unit)
    pure = projectors[0]
    mixed = depolarizing(pure)
    assert trace(multiply(pure, pure)) == 1
    assert trace(multiply(mixed, mixed)) == F(1, 3)
    assert pure != mixed
    assert depolarizing(b[1]) != b[1]
    assert depolarizing(product(a, pure, sharp(a))) != product(a, mixed, sharp(a))

    return (
        "MIXED carrier=real-or-complex dim=3 detH=4 detA=-1/4",
        "MIXED rank1_defects=3 traces=15/16,215/256,2815/4096",
        "MIXED cyclic_determinant=-1024 overlap=-4,-20 commutant_rank=8",
        "MIXED two_pass_pinching=NONSELECTING third_pass=SEPARATES",
        "MIXED depolarization=NONSELECTING rational_kraus=72 purity=1/3",
        "MIXED three_pass_selector=IDENTITY proof=UNIVERSAL_CPTP",
    )
