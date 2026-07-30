#!/usr/bin/env python3
"""Exact verifier for P-TM-SYM2-FRAME-1.

Construct the six golden projective lines and their rank-one Sym2 frame
operator. No Thue-Morse average, clock density, or physical measure enters.
"""

from fractions import Fraction as Fr


class QPhi:
    """a + b phi over Q, with phi^2 = phi + 1."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, other):
        other = q(other)
        return QPhi(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __sub__(self, other):
        other = q(other)
        return QPhi(self.a - other.a, self.b - other.b)

    def __rsub__(self, other):
        other = q(other)
        return QPhi(other.a - self.a, other.b - self.b)

    def __neg__(self):
        return QPhi(-self.a, -self.b)

    def __mul__(self, other):
        other = q(other)
        return QPhi(
            self.a * other.a + self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    __rmul__ = __mul__

    def conjugate(self):
        return QPhi(self.a + self.b, -self.b)

    def inverse(self):
        norm = self.a * self.a + self.a * self.b - self.b * self.b
        if norm == 0:
            raise ZeroDivisionError("zero in Q(phi)")
        return QPhi((self.a + self.b) / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * q(other).inverse()

    def __rtruediv__(self, other):
        return q(other) * self.inverse()

    def __eq__(self, other):
        other = q(other)
        return self.a == other.a and self.b == other.b

    def is_zero(self):
        return self.a == 0 and self.b == 0


def q(a=0, b=0):
    return a if isinstance(a, QPhi) else QPhi(a, b)


ZERO = q(0)
ONE = q(1)
PHI = q(0, 1)
PHIBAR = PHI.conjugate()


def zeros(n, m):
    return [[ZERO for _ in range(m)] for _ in range(n)]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    c = q(c)
    return [[c * x for x in row] for row in a]


def mm(a, b):
    out = zeros(len(a), len(b[0]))
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i][k].is_zero():
                continue
            for j in range(len(b[0])):
                out[i][j] = out[i][j] + a[i][k] * b[k][j]
    return out


def commutator(a, b):
    return sub(mm(a, b), mm(b, a))


def matrix_equal(a, b):
    return all(a[i][j] == b[i][j]
               for i in range(len(a)) for j in range(len(a[0])))


def matrix_zero(a):
    return all(x.is_zero() for row in a for x in row)


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def outer(u, v):
    return [[u[i] * v[j] for j in range(len(v))] for i in range(len(u))]


def rank(a):
    if not a:
        return 0
    matrix = [row[:] for row in a]
    nrows = len(matrix)
    ncols = len(matrix[0])
    r = 0
    for c in range(ncols):
        pivot = next(
            (i for i in range(r, nrows) if not matrix[i][c].is_zero()),
            None,
        )
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        inv = matrix[r][c].inverse()
        matrix[r] = [inv * x for x in matrix[r]]
        for i in range(nrows):
            if i == r or matrix[i][c].is_zero():
                continue
            factor = matrix[i][c]
            matrix[i] = [
                matrix[i][j] - factor * matrix[r][j] for j in range(ncols)
            ]
        r += 1
        if r == nrows:
            break
    return r


def symmetric_basis():
    basis = []
    for i, j in ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)):
        a = zeros(3, 3)
        a[i][j] = ONE
        a[j][i] = ONE
        basis.append(a)
    return basis


BASIS = symmetric_basis()
I3 = eye(3)
I6 = eye(6)
GRAM = [[q(1 if i == j and i < 3 else 2 if i == j else 0)
         for j in range(6)] for i in range(6)]


def sym_coords(a):
    return [a[0][0], a[1][1], a[2][2], a[0][1], a[0][2], a[1][2]]


def from_columns(columns):
    return [[columns[j][i] for j in range(len(columns))]
            for i in range(len(columns[0]))]


def frobenius(a, b):
    return trace(mm(a, b))


def make_frame(root):
    radius = root + 2
    vectors = [
        [ZERO, ONE, root],
        [ZERO, ONE, -root],
        [ONE, root, ZERO],
        [ONE, -root, ZERO],
        [root, ZERO, ONE],
        [root, ZERO, -ONE],
    ]
    return [scale(ONE / radius, outer(v, v)) for v in vectors]


def frame_operator(projectors):
    columns = []
    for a in BASIS:
        out = zeros(3, 3)
        for p in projectors:
            out = add(out, scale(frobenius(p, a), p))
        columns.append(sym_coords(scale(Fr(1, len(projectors)), out)))
    return from_columns(columns)


def induced_lie(lie):
    columns = []
    for a in BASIS:
        columns.append(sym_coords(sub(mm(lie, a), mm(a, lie))))
    return from_columns(columns)


def centralizer_rank(generators):
    n = len(generators[0])
    equations = []
    for generator in generators:
        for i in range(n):
            for j in range(n):
                row = [ZERO for _ in range(n * n)]
                for k in range(n):
                    row[i * n + k] = row[i * n + k] + generator[k][j]
                    row[k * n + j] = row[k * n + j] - generator[i][k]
                equations.append(row)
    return rank(equations)


def projector_pair():
    p1 = zeros(6, 6)
    for i in range(3):
        for j in range(3):
            p1[i][j] = q(Fr(1, 3))
    return p1, sub(I6, p1)


P1, P5 = projector_pair()
AUDIT_FAILS = []
SCIENCE_FAILS = []


def audit(tag, condition, message):
    print(("PASS " if condition else "STOP ") + tag + " " + message)
    if not condition:
        AUDIT_FAILS.append(tag)


def test(tag, condition, message, falsifier):
    print(("PASS " if condition else "FAIL ") + tag + " " + message)
    if not condition:
        SCIENCE_FAILS.append(falsifier)


def main():
    basis_gram = [[frobenius(BASIS[i], BASIS[j]) for j in range(6)]
                  for i in range(6)]
    coordinate_basis = from_columns([sym_coords(a) for a in BASIS])
    basis_ok = (all(matrix_equal(a, transpose(a)) for a in BASIS)
                and matrix_equal(basis_gram, GRAM)
                and matrix_equal(coordinate_basis, I6)
                and rank(GRAM) == 6)
    field_ok = (PHI * PHI == PHI + 1 and PHIBAR * PHIBAR == PHIBAR + 1
                and PHI + PHIBAR == 1 and PHI * PHIBAR == -1)
    audit("01 FIELD", field_ok and basis_ok,
          "Q(phi), conjugate roots, raw Sym2 coordinates, and Gram verified")

    projectors = make_frame(PHI)
    projectors_bar = make_frame(PHIBAR)
    both = projectors + projectors_bar
    projectors_ok = all(
        matrix_equal(p, transpose(p)) and matrix_equal(mm(p, p), p)
        and trace(p) == 1 and rank(p) == 1 for p in both
    )
    gram_ok = all(
        frobenius(frame[i], frame[j]) == (1 if i == j else Fr(1, 5))
        for frame in (projectors, projectors_bar)
        for i in range(6) for j in range(6)
    )
    tight_ok = True
    for frame in (projectors, projectors_bar):
        total = zeros(3, 3)
        for p in frame:
            total = add(total, p)
        tight_ok = tight_ok and matrix_equal(total, scale(2, I3))
    test("02 FRAME", projectors_ok and gram_ok and tight_ok,
         "six trace-one projectors; Gram diagonal 1, off-diagonal 1/5; sum=2I",
         "F-GOLDEN-SIX-LINE-FRAME")

    centered = [sub(p, scale(Fr(1, 3), I3)) for p in projectors]
    centered_sum = zeros(3, 3)
    for p in centered:
        centered_sum = add(centered_sum, p)
    centered_gram = [[frobenius(centered[i], centered[j]) for j in range(6)]
                     for i in range(6)]
    simplex_ok = (matrix_zero(centered_sum) and rank(centered_gram) == 5
                  and all(centered_gram[i][i] == Fr(2, 3) for i in range(6))
                  and all(centered_gram[i][j] == Fr(-2, 15)
                          for i in range(6) for j in range(6) if i != j))
    test("03 SIMPLEX", simplex_ok,
         "traceless projectors form a rank-5 regular simplex",
         "F-GOLDEN-SIX-LINE-SPAN")

    lx = [[ZERO, ZERO, ZERO], [ZERO, ZERO, q(-1)], [ZERO, ONE, ZERO]]
    ly = [[ZERO, ZERO, ONE], [ZERO, ZERO, ZERO], [q(-1), ZERO, ZERO]]
    lz = [[ZERO, q(-1), ZERO], [ONE, ZERO, ZERO], [ZERO, ZERO, ZERO]]
    lie_ok = (matrix_equal(commutator(lx, ly), lz)
              and matrix_equal(commutator(ly, lz), lx)
              and matrix_equal(commutator(lz, lx), ly)
              and all(matrix_equal(transpose(lie), scale(-1, lie))
                      and trace(lie).is_zero() for lie in (lx, ly, lz)))
    induced = [induced_lie(lie) for lie in (lx, ly, lz)]
    representation_ok = (
        matrix_equal(commutator(induced[0], induced[1]), induced[2])
        and matrix_equal(commutator(induced[1], induced[2]), induced[0])
        and matrix_equal(commutator(induced[2], induced[0]), induced[1])
    )
    metric_action_ok = all(
        matrix_zero(add(mm(transpose(generator), GRAM), mm(GRAM, generator)))
        for generator in induced
    )
    p1_from_definition = from_columns([
        sym_coords(scale(trace(a) / 3, I3)) for a in BASIS
    ])
    projector_semantics = (
        matrix_equal(P1, p1_from_definition)
        and matrix_equal(mm(P1, P1), P1)
        and matrix_equal(mm(P5, P5), P5)
        and matrix_zero(mm(P1, P5))
        and matrix_equal(add(P1, P5), I6)
        and rank(P1) == 1 and rank(P5) == 5
        and all(matrix_equal(mm(transpose(p), GRAM), mm(GRAM, p))
                for p in (P1, P5))
    )
    c_rank = centralizer_rank(induced)
    p_commutes = all(matrix_zero(commutator(p, generator))
                     for p in (P1, P5) for generator in induced)
    p_independent = rank([
        [x for row in P1 for x in row],
        [x for row in P5 for x in row],
    ]) == 2
    if lie_ok and representation_ok and metric_action_ok and projector_semantics:
        test("04 COMMUTANT", c_rank == 34 and p_commutes and p_independent,
             "End(Sym2)^so(3) has nullity 2 = span{P1,P5}",
             "F-SO3-SYM2-COMMUTANT")
    else:
        audit("04 COMMUTANT", False,
              "carrier or induced so(3) audit failed before commutant decision")

    moment = frame_operator(projectors)
    moment_bar = frame_operator(projectors_bar)
    rational_descent = all(x.b == 0 for row in moment for x in row)
    galois_ok = matrix_equal(moment, moment_bar)
    central = all(matrix_zero(commutator(moment, generator))
                  for generator in induced)
    test("05 MOMENT", rational_descent and galois_ok and central,
         "direct frame moment descends to Q, is Galois-stable, and is so(3)-central",
         "F-GOLDEN-SIX-LINE-MOMENT")

    expected = add(scale(Fr(1, 3), P1), scale(Fr(2, 15), P5))
    scalar_mass = Fr(1, 3)
    tensor_mass = 5 * Fr(2, 15)
    spectral = (matrix_equal(moment, expected) and trace(moment) == 1
                and scalar_mass == Fr(1, 3) and tensor_mass == Fr(2, 3)
                and 2 * scalar_mass == tensor_mass)
    test("06 SPECTRAL", spectral,
         "coefficients 1/3:2/15=5:2; block masses 1/3:2/3=1:2; trace 1",
         "F-GOLDEN-SIX-LINE-5-TO-2")

    test("07 NONUNIFORM", not matrix_equal(moment, scale(Fr(1, 6), I6)),
         "M is not (1/6)I6; six equal channel weights are false at this frame scope",
         "F-GOLDEN-SIX-LINE-NONUNIFORM")

    cube_vectors = [
        [ONE, ONE, ONE], [ONE, ONE, q(-1)],
        [ONE, q(-1), ONE], [q(-1), ONE, ONE],
    ]
    cube = [scale(Fr(1, 3), outer(v, v)) for v in cube_vectors]
    cube_total = zeros(3, 3)
    for p in cube:
        cube_total = add(cube_total, p)
    cube_moment = frame_operator(cube)
    control_ok = (
        matrix_equal(scale(Fr(1, 4), cube_total), scale(Fr(1, 3), I3))
        and any(not matrix_zero(commutator(cube_moment, generator))
                for generator in induced)
    )
    audit("08 CONTROL", control_ok,
          "cube lines have isotropic second moment but fail the Sym2 centrality test")

    if AUDIT_FAILS:
        print("RESULT STOP audit=" + ",".join(AUDIT_FAILS))
        raise SystemExit(1)
    if SCIENCE_FAILS:
        print("RESULT NEGATIVE fired=" + ",".join(SCIENCE_FAILS))
        raise SystemExit(0)
    print("RESULT POSITIVE 8/8 ALL PASS")
    print("SCOPE GOLDEN-SIX-LINE-SYM2-FRAME algebra only; no TM or physical measure")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
