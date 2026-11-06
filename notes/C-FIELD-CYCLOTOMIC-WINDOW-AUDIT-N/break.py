#!/usr/bin/env python3
"""Independent exact audit authored from the frozen successor preregistration.

PUBLIC / NON-CANONICAL L1.  No primary or predecessor implementation is used.
The finite assertions support, but do not replace, the accompanying proof.
"""

from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd


def need(condition, clause):
    if not condition:
        raise AssertionError(clause)


class Matrix:
    """Small immutable rational matrices, retaining empty-dimension shapes."""

    def __init__(self, rows=(), width=None):
        self.rows = tuple(tuple(Q(x) for x in row) for row in rows)
        self.h = len(self.rows)
        self.w = len(self.rows[0]) if self.h else (0 if width is None else width)
        need(all(len(row) == self.w for row in self.rows), "rectangular matrix")
        need(width is None or width == self.w, "declared width")

    def __eq__(self, other):
        return isinstance(other, Matrix) and (self.h, self.w, self.rows) == (
            other.h, other.w, other.rows
        )

    def __add__(self, other):
        need((self.h, self.w) == (other.h, other.w), "addition shape")
        return Matrix([[self.rows[i][j] + other.rows[i][j]
                        for j in range(self.w)] for i in range(self.h)], self.w)

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, scalar):
        return Matrix([[x * Q(scalar) for x in row] for row in self.rows], self.w)

    __rmul__ = __mul__

    def __matmul__(self, other):
        need(self.w == other.h, "multiplication shape")
        return Matrix([[sum(self.rows[i][k] * other.rows[k][j]
                            for k in range(self.w))
                        for j in range(other.w)] for i in range(self.h)], other.w)

    @property
    def t(self):
        return Matrix([[self.rows[i][j] for i in range(self.h)]
                       for j in range(self.w)], self.h)

    def sub(self, row_ids, col_ids):
        return Matrix([[self.rows[i][j] for j in col_ids] for i in row_ids],
                      len(col_ids))

    def integral(self):
        return all(x.denominator == 1 for row in self.rows for x in row)


def zero(h, w):
    return Matrix([[0] * w for _ in range(h)], w)


def eye(n):
    return Matrix([[int(i == j) for j in range(n)] for i in range(n)], n)


def col(values):
    return Matrix([[x] for x in values], 1)


def join(block_rows):
    heights = [row[0].h for row in block_rows]
    widths = [a.w for a in block_rows[0]]
    need(all(len(row) == len(widths) for row in block_rows), "block count")
    need(all(a.h == heights[i] and a.w == widths[j]
             for i, row in enumerate(block_rows) for j, a in enumerate(row)),
         "block shape")
    rows = []
    for block_row, height in zip(block_rows, heights):
        rows.extend([sum((a.rows[i] for a in block_row), ()) for i in range(height)])
    return Matrix(rows, sum(widths))


def power(a, n):
    need(a.h == a.w and n >= 0, "power domain")
    result = eye(a.h)
    while n:
        if n & 1:
            result = result @ a
        a = a @ a
        n //= 2
    return result


def echelon(a):
    rows = [list(row) for row in a.rows]
    pivot_columns = []
    sign, pivot_product = 1, Q(1)
    for j in range(a.w):
        k = len(pivot_columns)
        pivot = next((i for i in range(k, a.h) if rows[i][j]), None)
        if pivot is None:
            continue
        if pivot != k:
            rows[k], rows[pivot] = rows[pivot], rows[k]
            sign = -sign
        value = rows[k][j]
        pivot_product *= value
        rows[k] = [x / value for x in rows[k]]
        for i in range(a.h):
            if i != k:
                factor = rows[i][j]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[k])]
        pivot_columns.append(j)
        if len(pivot_columns) == a.h:
            break
    return Matrix(rows, a.w), pivot_columns, sign * pivot_product


def rank(a):
    return len(echelon(a)[1])


def determinant(a):
    need(a.h == a.w, "determinant square")
    _, pivots, value = echelon(a)
    return value if len(pivots) == a.h else Q(0)


def inverse(a):
    need(a.h == a.w and determinant(a) != 0, "inverse domain")
    reduced, pivots, _ = echelon(join([[a, eye(a.h)]]))
    need(pivots == list(range(a.h)), "inverse pivots")
    result = reduced.sub(tuple(range(a.h)), tuple(range(a.w, 2 * a.w)))
    need(a @ result == result @ a == eye(a.h), "two-sided inverse")
    return result


def characteristic(a):
    """Coefficients in descending order, using principal minors."""
    need(a.h == a.w, "characteristic square")
    return tuple([Q(1)] + [(-1) ** k * sum(
        determinant(a.sub(ids, ids)) for ids in combinations(range(a.h), k)
    ) for k in range(1, a.h + 1)])


def polynomial_product(a, b):
    result = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return tuple(result)


def poly_at(coefficients, a):
    result = zero(a.h, a.w)
    for value in coefficients:
        result = result @ a + value * eye(a.h)
    return result


def phi5(a):
    return poly_at((1, 1, 1, 1, 1), a)


def minor_gcd(a, size):
    result = 0
    for rows in combinations(range(a.h), size):
        for columns in combinations(range(a.w), size):
            d = determinant(a.sub(rows, columns))
            need(d.denominator == 1, "integer minor")
            result = gcd(result, int(d))
    return result


def smith_certificates(a):
    """Euclidean row/column reduction, recording both unimodular factors."""
    need(a.integral(), "Smith integer input")
    d = [[int(x) for x in row] for row in a.rows]
    u = [[int(i == j) for j in range(a.h)] for i in range(a.h)]
    v = [[int(i == j) for j in range(a.w)] for i in range(a.w)]

    def row_swap(i, j):
        d[i], d[j] = d[j], d[i]
        u[i], u[j] = u[j], u[i]

    def column_swap(i, j):
        for b in (d, v):
            for row in b:
                row[i], row[j] = row[j], row[i]

    def row_add(i, j, multiplier):
        for b in (d, u):
            b[i] = [x + multiplier * y for x, y in zip(b[i], b[j])]

    def column_add(i, j, multiplier):
        for b in (d, v):
            for row in b:
                row[i] += multiplier * row[j]

    for k in range(min(a.h, a.w)):
        candidates = [(abs(d[i][j]), i, j) for i in range(k, a.h)
                      for j in range(k, a.w) if d[i][j]]
        if not candidates:
            break
        _, i, j = min(candidates)
        row_swap(k, i)
        column_swap(k, j)
        while True:
            changed = False
            for i in range(k + 1, a.h):
                if d[i][k]:
                    row_add(i, k, -(d[i][k] // d[k][k]))
                    if d[i][k]:
                        row_swap(i, k)
                    changed = True
                    break
            if changed:
                continue
            for j in range(k + 1, a.w):
                if d[k][j]:
                    column_add(j, k, -(d[k][j] // d[k][k]))
                    if d[k][j]:
                        column_swap(j, k)
                    changed = True
                    break
            if changed:
                continue
            offending = next(((i, j) for i in range(k + 1, a.h)
                              for j in range(k + 1, a.w)
                              if d[i][j] % d[k][k]), None)
            if offending is None:
                break
            row_add(k, offending[0], 1)
        if d[k][k] < 0:
            d[k] = [-x for x in d[k]]
            u[k] = [-x for x in u[k]]
    result, left, right = Matrix(d, a.w), Matrix(u, a.h), Matrix(v, a.w)
    need(left @ a @ right == result, "Smith certificate identity")
    need(abs(determinant(left)) == abs(determinant(right)) == 1,
         "Smith certificates unimodular")
    return result, left, right


def field(c):
    e, f = c.h, c.w
    g = c.t @ c
    t = join([[eye(e), c], [-c.t, eye(f) - g]])
    back = join([[eye(e) - c @ c.t, -c], [c.t, eye(f)]])
    reflection = join([[eye(e), c], [zero(f, e), -eye(f)]])
    metric = join([[2 * eye(e), c], [c.t, 2 * eye(f)]])
    completed = join([[eye(e), Q(1, 2) * c], [zero(f, e), eye(f)]])
    diagonal = join([[2 * eye(e), zero(e, f)],
                     [zero(f, e), 2 * eye(f) - Q(1, 2) * g]])
    need(t @ back == back @ t == eye(e + f), "field inverse")
    need(t.t @ metric @ t == metric, "field energy invariant")
    need(reflection @ reflection == eye(e + f), "reflection involution")
    need(reflection @ t @ reflection == back, "time reversal")
    need(reflection.t @ metric @ reflection == metric, "reflection energy")
    need(completed.t @ diagonal @ completed == metric, "completed square")
    need(rank(t - eye(e + f)) == 2 * rank(c), "static kernel dimension")
    return t, metric, reflection


def energy(metric, vector):
    return (vector.t @ metric @ vector).rows[0][0] / 2


def exact_order(a, n):
    need(power(a, n) == eye(a.h), "specified finite order")
    need(all(power(a, d) != eye(a.h) for d in range(1, n) if n % d == 0),
         "order is exact")


def positive(a):
    return all(determinant(a.sub(tuple(range(k)), tuple(range(k)))) > 0
               for k in range(1, a.h + 1))


def audit():
    c = Matrix([[1, -1], [-1, 0], [0, 1], [0, 1]])
    d = Matrix([[1, 1, 1, 0], [-1, -1, 0, -1], [0, 0, -1, 1]])
    g = Matrix([[2, -1], [-1, 3]])
    a = Matrix([[1, 0, 1, 0], [0, 1, 0, 1],
                [-2, 1, -1, 1], [1, -3, 1, -2]])
    b = Matrix([[4, -2, 2, -1], [-2, 6, -1, 3],
                [2, -1, 2, 0], [-1, 3, 0, 2]])
    p = Matrix([[1, -1, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0],
                [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    f = Matrix([[0, -1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
    s = Matrix([[1, 0], [1, 0], [0, 1], [1, -1], [0, 0], [0, 0]])
    static_extract = Matrix([[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]])
    t, raw_metric, reflection = field(c)
    charge = join([[d, zero(3, 2)]])
    need(c.t @ c == g and d @ c == zero(3, 2), "selected Gram and boundary")
    need(charge @ t == charge @ reflection == charge, "actual charge retained")
    need(positive(g) and positive(4 * eye(2) - g), "strict spectral window")
    need(positive(raw_metric) and positive(b), "positive definite energy")

    # The exposed graph is reconstructed from the stated oriented endpoints.
    endpoints = ((0, 1), (0, 1), (0, 2), (2, 1))
    incidence = Matrix([[int(tail == vertex) - int(head == vertex)
                         for tail, head in endpoints] for vertex in range(3)])
    need(incidence == d, "actual selected multigraph incidence")
    need(c.sub((0, 1, 2, 3), (0,)) == col((1, -1, 0, 0)), "digon face")
    need(c.sub((0, 1, 2, 3), (1,)) == col((-1, 0, 1, 1)), "triangle face")

    need(f @ p == eye(4), "active integral retraction")
    need(t @ p == p @ a and p.t @ raw_metric @ p == b, "active restriction")
    need(phi5(a) == zero(4, 4) and characteristic(a) == (1, 1, 1, 1, 1),
         "active cyclotomic polynomial")
    exact_order(a, 5)
    exact_order(t, 5)
    need(phi5(t) @ p == zero(6, 4) and rank(phi5(t)) == 2,
         "rational active kernel has dimension four")
    need(minor_gcd(p, 4) == 1, "active saturation")
    need(static_extract @ s == eye(2) and t @ s == s, "static retraction")
    need(minor_gcd(s, 2) == 1 and rank(t - eye(6)) == 4, "static saturation")
    need(charge @ p == zero(3, 4) and rank(charge) == 2,
         "fixed actual charge fibers have the active translation lattice")
    charge_section = Matrix([[1, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]])
    need(charge @ charge_section == Matrix([[1, 0], [-1, -1], [0, 1]]),
         "all zero-sum integer charges are realized")

    # A primitive basis and a rank computation, rather than spectral splitting,
    # certify the intersection with the raw integer lattice.
    static_sample = s @ col((1, 0))
    need(p @ f @ static_sample != static_sample, "extraction alone rejected")
    need(phi5(t) @ static_sample == 5 * static_sample,
         "Phi1 contamination deliberately rejected")
    contaminated = join([[p, static_sample]])
    need(rank(contaminated) == 5 and phi5(t) @ contaminated != zero(6, 5),
         "contaminated purported active carrier fails")
    double = Matrix([[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    need(minor_gcd(p @ double, 4) == 2 and f @ p @ double != eye(4),
         "index-two active basis deliberately rejected")

    k = Matrix([[0, 1, 0, 0], [0, 0, 1, -1],
                [1, -1, 0, -1], [0, 1, -2, 1]])
    w = col((0, 0, 1, 0))
    need(k == join([[power(a, n) @ w for n in range(4)]]), "cyclic module basis")
    need(determinant(k) == -1 and inverse(k).integral(), "integral cyclic basis")
    companion = Matrix([[0, 0, 0, -1], [1, 0, 0, -1],
                        [0, 1, 0, -1], [0, 0, 1, -1]])
    need(a @ k == k @ companion, "Z[zeta5] module multiplication")
    lambda_operator = join([[g, zero(2, 2)], [zero(2, 2), g]])
    need(a + inverse(a) == 2 * eye(4) - lambda_operator,
         "mu plus inverse relation to lambda")
    need((eye(4) - a) @ (eye(4) - inverse(a)) == lambda_operator,
         "unit-circle squared-distance relation")
    j = eye(4) + power(a, 2)
    need(characteristic(j) == (1, -3, 4, -2, 1), "J characteristic polynomial")
    need(sum(j.rows[i][i] for i in range(4)) == 3 and determinant(j) == 1,
         "J trace and determinant")
    need(inverse(j) == -a - power(a, 2) and inverse(j).integral(), "J inverse")
    first = col((1, 0, 0, 0))
    need(energy(b, first) == 2 and energy(b, j @ first) == 3,
         "J isometry claim deliberately rejected")
    need(j.t @ b @ j != b, "J fails energy-metric equality")

    ell = Matrix([[1, -3, -1, -2], [-3, 4, -2, 1],
                  [0, 5, 1, 2], [5, -5, 2, -1]])
    adjoint = Matrix([[1, 2, 1, 2], [2, -1, 2, -1],
                      [0, -5, 1, -3], [-5, 5, -3, 4]])
    need(ell == (eye(4) - a) @ (eye(4) - power(a, 2)), "L polynomial")
    need(ell @ a == a @ ell and ell @ ell == 5 * power(a, 3), "L algebra")
    need(adjoint == power(a, 2) @ ell, "N polynomial")
    need(adjoint @ ell == ell @ adjoint == 5 * eye(4), "scaled inverse")
    need(determinant(ell) == 25 and ell.t @ b @ ell == 5 * b, "L norm scaling")
    need(inverse(b) @ ell.t @ b == adjoint, "energy adjoint")
    need(ell.t != adjoint, "Euclidean adjoint substitution deliberately rejected")
    smith, _, _ = smith_certificates(ell)
    need(smith == Matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                          [0, 0, 5, 0], [0, 0, 0, 5]]), "Smith invariants")
    need(tuple(minor_gcd(ell, size) for size in range(5)) == (1, 1, 1, 5, 25),
         "all determinantal divisors")
    hermite = Matrix([[5, 3, 0, 0], [0, 1, 0, 0],
                      [0, 0, 5, 3], [0, 0, 0, 1]])
    hermite_change = inverse(ell) @ hermite
    need(hermite_change.integral() and abs(determinant(hermite_change)) == 1,
         "column Hermite unimodular certificate")
    need(ell @ hermite_change == hermite, "column Hermite identity")
    need(all(hermite.rows[i][i] > 0 for i in range(4)) and
         all(hermite.rows[i][j] == 0 for i in range(4) for j in range(i)) and
         all(0 <= hermite.rows[i][j] < hermite.rows[i][i]
             for i in range(4) for j in range(i + 1, 4)), "column Hermite form")

    def admitted(vector):
        need(vector.h == 4 and vector.w == 1 and vector.integral(), "image input")
        x = [int(row[0]) for row in vector.rows]
        return (x[0] + 2 * x[1]) % 5 == (x[2] + 2 * x[3]) % 5 == 0

    def partial_inverse(vector):
        # Admission is evaluated before any numerator or division is formed.
        if not admitted(vector):
            raise ValueError("outside the integral L image")
        result = Q(1, 5) * (adjoint @ vector)
        need(result.integral() and ell @ result == vector, "admitted inverse")
        return result

    def rejected(vector):
        try:
            partial_inverse(vector)
        except ValueError:
            return True
        return False

    bad = col((0, 0, 1, 1))
    old_image = col((0, 0, 1, 2))
    shell_counterexample = col((0, 0, 1, -2))
    need(adjoint @ bad == col((3, 1, -2, 1)) and rejected(bad),
         "first predecessor regression")
    need((0 + 2 * 0) % 5 == 0 and (3 * 0 - 0 + 1 - 1) % 5 == 0,
         "known false shortcut accepts first regression")
    need(not (Q(1, 5) * (adjoint @ bad)).integral(), "hidden division rejected")
    need(partial_inverse(old_image) == col((1, 0, -1, 1)) and
         energy(b, partial_inverse(old_image)) == 1, "second predecessor regression")
    need(energy(b, shell_counterexample) == 5 and rejected(shell_counterexample) and
         adjoint @ shell_counterexample == col((-3, 4, 7, -11)),
         "true energy-five nonimage regression")
    need(energy(b, w) == 1 and energy(b, ell @ w) == 5 and
         partial_inverse(ell @ w) == w, "nonempty admitted energy-five image")

    residues = tuple(product(range(5), repeat=4))

    def residue(vector):
        need(vector.integral(), "integer residue input")
        return tuple(int(row[0]) % 5 for row in vector.rows)

    image_mod5 = {residue(ell @ col(x)) for x in residues}
    need(len(image_mod5) == 25, "complete enumerated mod-five image")
    accepted = denied = 0
    for values in residues:
        vector = col(values)
        numerical = all(int(row[0]) % 5 == 0 for row in (adjoint @ vector).rows)
        need(admitted(vector) == numerical == (values in image_mod5),
             "625 image residue equivalence")
        if admitted(vector):
            partial_inverse(vector)
            accepted += 1
        else:
            need(rejected(vector), "residue rejected before division")
            denied += 1
    need((accepted, denied) == (25, 600), "complete image domain counts")
    quotient_map = Matrix([[1, 2, 0, 0], [0, 0, 1, 2]])
    quotient_section = Matrix([[1, 0], [0, 0], [0, 1], [0, 0]])
    need(quotient_map @ quotient_section == eye(2), "quotient is onto")
    need(all(int(x) % 5 == 0 for row in (quotient_map @ ell).rows for x in row),
         "L lies in quotient kernel")

    split = join([[p, s]])
    split_inverse = inverse(split)
    need(abs(determinant(split)) == 5, "active-static index five")
    expected_inverse = Matrix([[Q(2, 5), Q(-3, 5), Q(1, 5), Q(1, 5), 0, 0],
                               [Q(-1, 5), Q(-1, 5), Q(2, 5), Q(2, 5), 0, 0],
                               [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1],
                               [Q(2, 5), Q(2, 5), Q(1, 5), Q(1, 5), 0, 0],
                               [Q(1, 5), Q(1, 5), Q(3, 5), Q(-2, 5), 0, 0]])
    need(split_inverse == expected_inverse, "explicit rational split coordinates")
    split_smith, _, _ = smith_certificates(split)
    need(split_smith == Matrix([[int(i == j) * (5 if i == 5 else 1)
                                for j in range(6)] for i in range(6)]),
         "gluing quotient order five")
    static_projector = Q(1, 5) * phi5(t)
    active_projector = eye(6) - static_projector
    need(static_projector @ static_projector == static_projector and
         static_projector @ p == zero(6, 4) and static_projector @ s == s,
         "rational static projector")
    need(active_projector @ p == p and active_projector @ s == zero(6, 2),
         "rational active projector")
    need(static_projector == split @ join([[zero(4, 4), zero(4, 2)],
                                          [zero(2, 4), eye(2)]]) @ split_inverse,
         "projectors agree with rational splitting")
    glue_row = Matrix([[2, -3, 1, 1, 0, 0]])
    charge_glue = Matrix([[2, 0, 1]]) @ charge
    need(charge_glue - glue_row == Matrix([[0, 5, 0, 0, 0, 0]]),
         "gluing uses actual D")
    need((5 * static_projector).integral() and
         static_projector.sub(tuple(range(6)), (4, 5)) == zero(6, 2),
         "full extension domain depends only on electric residues mod five")
    split_count = nonsplit_count = 0
    for electric in residues:
        vector = col(electric + (0, 0))
        charges = charge @ vector
        congruence = int((glue_row @ vector).rows[0][0]) % 5 == 0
        charge_congruence = int(2 * charges.rows[0][0] + charges.rows[2][0]) % 5 == 0
        need(congruence == charge_congruence == (split_inverse @ vector).integral()
             == (static_projector @ vector).integral(), "625 gluing equivalence")
        if congruence:
            split_count += 1
        else:
            nonsplit_count += 1
    need((split_count, nonsplit_count) == (125, 500), "complete gluing domain counts")

    raw_ell = (eye(6) - t) @ (eye(6) - power(t, 2))
    extension = raw_ell + static_projector
    extension_in_split = join([[ell, zero(4, 2)], [zero(2, 4), eye(2)]])
    need(raw_ell @ p == p @ ell and raw_ell @ s == zero(6, 2), "raw L action")
    need(charge @ raw_ell == zero(3, 6), "raw L annihilates actual charges")
    need(extension == split @ extension_in_split @ split_inverse and
         charge @ extension == charge, "extension retains actual charges")
    raw_first = col((1, 0, 0, 0, 0, 0))
    need(extension @ raw_first == col((Q(17, 5), Q(-3, 5), Q(-9, 5),
                                       Q(-9, 5), -1, 3)), "nonintegral extension witness")
    need(not (extension @ raw_first).integral() and not extension.integral(),
         "unrestricted integral extension claim rejected")
    static_metric = s.t @ raw_metric @ s
    split_metric = join([[b, zero(4, 2)], [zero(2, 4), static_metric]])
    need(split.t @ raw_metric @ split == split_metric, "energy orthogonal rational split")
    weighted_metric = join([[5 * b, zero(4, 2)], [zero(2, 4), static_metric]])
    need((extension @ split).t @ raw_metric @ (extension @ split) == weighted_metric,
         "extension energy is five active plus static")
    extension_inverse = split @ join([[Q(1, 5) * adjoint, zero(4, 2)],
                                      [zero(2, 4), eye(2)]]) @ split_inverse
    need(extension_inverse @ extension == extension @ extension_inverse == eye(6),
         "rational extension inverse")

    def extend_integer(vector):
        need(vector.integral(), "extension integer input")
        coordinates = split_inverse @ vector
        if not coordinates.integral():
            raise ValueError("outside the split integer domain")
        result = extension @ vector
        need(result.integral(), "integral extension on its domain")
        return result

    def inverse_extension_integer(vector):
        need(vector.integral(), "extension image integer input")
        coordinates = split_inverse @ vector
        if not coordinates.integral():
            raise ValueError("outside the split integer image carrier")
        active = partial_inverse(coordinates.sub((0, 1, 2, 3), (0,)))
        result = split @ join([[active], [coordinates.sub((4, 5), (0,))]])
        need(result.integral() and extend_integer(result) == vector,
             "partial integral extension inverse")
        return result

    for i in range(6):
        vector = split.sub(tuple(range(6)), (i,))
        image = extend_integer(vector)
        need(inverse_extension_integer(image) == vector and charge @ image == charge @ vector,
             "extension restricted basis and actual charges")
    for function, vector in ((extend_integer, raw_first),
                             (inverse_extension_integer, raw_first),
                             (inverse_extension_integer, p @ bad)):
        try:
            function(vector)
        except ValueError:
            pass
        else:
            raise AssertionError("extension domain or image rejection missing")

    # Entire declared finite control family, including all static directions.
    crit = Matrix([[1, 1], [1, 0], [1, 0], [0, 1], [0, 1]])
    controls = (zero(2, 3), Matrix([[1], [0]]), Matrix([[1, 0], [0, 0]]),
                Matrix([[2, 0], [0, 0]]), Matrix([[3, 0], [0, 0]]), c, crit)
    control_fields = [field(matrix) for matrix in controls]
    for index, order in ((0, 1), (1, 6), (2, 6), (5, 5)):
        exact_order(control_fields[index][0], order)
        need(positive(control_fields[index][1]), "stable control positive energy")
    need(control_fields[0][0] == eye(5), "zero carrier is static")
    phi1, phi2, phi4, phi6 = (1, -1), (1, 1), (1, 0, 1), (1, -1, 1)
    need(characteristic(control_fields[1][0]) == polynomial_product(phi1, phi6),
         "rectangular stable control")
    need(characteristic(control_fields[2][0]) ==
         polynomial_product(polynomial_product(phi1, phi1), phi6),
         "rank-deficient stable control")
    dynamic_inclusion = Matrix([[1, 0], [0, 0], [0, 1], [0, 0]])
    critical_block = Matrix([[1, 2], [-2, -3]])
    need(control_fields[3][0] @ dynamic_inclusion == dynamic_inclusion @ critical_block,
         "lambda-four critical block")
    critical_nilpotent = critical_block + eye(2)
    need(critical_nilpotent != zero(2, 2) and
         critical_nilpotent @ critical_nilpotent == zero(2, 2), "critical Jordan growth")
    need(characteristic(control_fields[3][0]) == polynomial_product(
        polynomial_product(phi1, phi1), polynomial_product(phi2, phi2)),
        "critical control spectrum")
    unstable_block = Matrix([[1, 3], [-3, -8]])
    unstable = control_fields[4][0]
    need(unstable @ dynamic_inclusion == dynamic_inclusion @ unstable_block and
         characteristic(unstable_block) == (1, 7, 1), "unstable block spectrum")
    need((-7) ** 2 + 7 * (-7) + 1 > 0 and (-6) ** 2 + 7 * (-6) + 1 < 0,
         "real eigenvalue strictly between minus seven and minus six")
    bounded_special = col((0, 1, 0, 0))
    need(bounded_special != zero(4, 1) and unstable @ bounded_special == bounded_special,
         "unstable carrier has nonzero bounded static special orbit")
    need(characteristic(unstable) == polynomial_product(
        polynomial_product(phi1, phi1), (1, 7, 1)), "unstable full spectrum")
    need(not positive(control_fields[3][1]) and not positive(control_fields[4][1]),
         "critical and unstable energy lack strict positivity")
    # Empty edge/magnetic dimensions preserve the explicitly defined convention.
    for empty in (zero(0, 0), zero(0, 2), zero(3, 0)):
        empty_t, _, _ = field(empty)
        need(empty_t == eye(empty.h + empty.w), "empty spectral maximum zero control")

    crit_t, crit_metric, _ = control_fields[6]
    need(crit.t @ crit == Matrix([[3, 1], [1, 3]]), "exact v95 critical Gram")
    vv = col((1, 1))
    cv = crit @ vv
    crit_embedding = join([[cv, zero(5, 1)], [zero(2, 1), vv]])
    crit_block = Matrix([[1, 1], [-4, -3]])
    need(crit_t @ crit_embedding == crit_embedding @ crit_block, "v95 lambda-four block")
    nn = crit_block + eye(2)
    need(nn != zero(2, 2) and nn @ nn == zero(2, 2), "v95 nontrivial Jordan block")
    state = join([[zero(5, 1)], [vv]])
    for n in range(13):
        expected = join([[((-1) ** (n + 1) * n) * cv],
                         [((-1) ** n * (2 * n + 1)) * vv]])
        need(state == expected and energy(crit_metric, state) == 2,
             "v95 critical formula at n=" + str(n))
        need(power(crit_block, n) == ((-1) ** n) * (eye(2) - n * nn),
             "Jordan power formula control")
        state = crit_t @ state
    need(characteristic(crit_t) == polynomial_product(
        polynomial_product(polynomial_product(phi1, phi1), phi1),
        polynomial_product(polynomial_product(phi2, phi2), phi4)), "v95 full spectrum")
    for sign in (-1, 1):
        triangle_gram = Matrix([[3, sign], [sign, 3]])
        need(characteristic(triangle_gram) == (1, -6, 8) and
             determinant(4 * eye(2) - triangle_gram) == 0,
             "ordinary adjacent signed triangle eigenvalues four and two")
    need(5 * 1 - 1 == 4 and 4 != 2, "energy reversal is not the R18-A20 resource match")


if __name__ == "__main__":
    audit()
    print("CHALLENGER PASS: independent exact audit, scope controls and both predecessor regressions")
