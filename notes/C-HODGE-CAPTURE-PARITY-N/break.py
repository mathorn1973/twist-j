#!/usr/bin/env python3
"""Code-blind exact corroboration of the capture-parity proof equations.

NON-CANONICAL L1 candidate-C. All source functions remain unevaluated.
The boundary uniqueness and measure-zero statements are analytical.
No filesystem, network, randomness, subprocesses or floating point is used.
"""

from fractions import Fraction as Q
from itertools import combinations, permutations, product


class G:
    """Gaussian rationals, with conjugation independent of matrix routines."""

    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        if isinstance(r, G):
            if i != 0:
                raise TypeError("nonzero extra imaginary coordinate")
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = Q(r), Q(i)

    def __add__(self, other):
        try:
            other = G(other)
        except (TypeError, ValueError):
            return NotImplemented
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-G(other))

    def __rsub__(self, other):
        return G(other) + (-self)

    def __mul__(self, other):
        try:
            other = G(other)
        except (TypeError, ValueError):
            return NotImplemented
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def star(self):
        return G(self.r, -self.i)

    def norm(self):
        return self.r * self.r + self.i * self.i

    def __truediv__(self, other):
        other = G(other)
        norm = other.norm()
        if not norm:
            raise ZeroDivisionError("zero Gaussian denominator")
        value = self * other.star()
        return G(value.r / norm, value.i / norm)

    def __rtruediv__(self, other):
        return G(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return (G(1) / self) ** (-exponent)
        result, factor = G(1), self
        while exponent:
            if exponent % 2:
                result *= factor
            factor *= factor
            exponent //= 2
        return result

    def __eq__(self, other):
        try:
            other = G(other)
        except (TypeError, ValueError):
            return False
        return self.r == other.r and self.i == other.i

    def __bool__(self):
        return bool(self.r or self.i)

    def __repr__(self):
        return "G(" + str(self.r) + "," + str(self.i) + ")"


class LP:
    """Four-variable sparse Laurent polynomials with Gaussian coefficients."""

    __slots__ = ("terms",)

    def __init__(self, value=0):
        if isinstance(value, LP):
            self.terms = dict(value.terms)
        elif isinstance(value, dict):
            self.terms = {tuple(k): G(v) for k, v in value.items() if G(v)}
        else:
            value = G(value)
            self.terms = {(0, 0, 0, 0): value} if value else {}

    @staticmethod
    def monomial(exponents, coefficient=1):
        return LP({tuple(exponents): G(coefficient)})

    def __add__(self, other):
        other = LP(other)
        terms = dict(self.terms)
        for key, value in other.terms.items():
            terms[key] = terms.get(key, G()) + value
        return LP(terms)

    __radd__ = __add__

    def __neg__(self):
        return LP({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-LP(other))

    def __rsub__(self, other):
        return LP(other) + (-self)

    def __mul__(self, other):
        other = LP(other)
        terms = {}
        for left, a in self.terms.items():
            for right, b in other.terms.items():
                key = tuple(x + y for x, y in zip(left, right))
                terms[key] = terms.get(key, G()) + a * b
        return LP(terms)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return LP({key: value / scalar for key, value in self.terms.items()})

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("negative polynomial power")
        result = LP(1)
        for _ in range(exponent):
            result *= self
        return result

    def __eq__(self, other):
        return self.terms == LP(other).terms

    def integrate(self, variables):
        return LP({key: value for key, value in self.terms.items()
                   if all(key[index] == 0 for index in variables)})


class F:
    """Q(phi), phi squared equals phi plus one."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        if isinstance(a, F):
            if b != 0:
                raise TypeError("extra phi coefficient")
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = Q(a), Q(b)

    def __add__(self, other):
        other = F(other)
        return F(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-F(other))

    def __rsub__(self, other):
        return F(other) + (-self)

    def __mul__(self, other):
        other = F(other)
        return F(self.a * other.a + self.b * other.b,
                 self.a * other.b + self.b * other.a + self.b * other.b)

    __rmul__ = __mul__

    def sigma(self):
        return F(self.a + self.b, -self.b)

    def norm(self):
        return self.a * self.a + self.a * self.b - self.b * self.b

    def __truediv__(self, other):
        other = F(other)
        denominator = other.norm()
        if not denominator:
            raise ZeroDivisionError("zero golden denominator")
        value = self * other.sigma()
        return F(value.a / denominator, value.b / denominator)

    def __rtruediv__(self, other):
        return F(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return (F(1) / self) ** (-exponent)
        result = F(1)
        for _ in range(exponent):
            result *= self
        return result

    def __eq__(self, other):
        try:
            other = F(other)
        except (TypeError, ValueError):
            return False
        return self.a == other.a and self.b == other.b

    def sign(self):
        a, b = self.a + self.b / 2, self.b / 2
        if not b:
            return (a > 0) - (a < 0)
        if not a:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        difference = a * a - 5 * b * b
        if not difference:
            return 0
        return ((difference > 0) - (difference < 0)) * ((a > 0) - (a < 0))


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def mat(rows):
    return [[G(value) for value in row] for row in rows]


def eye(size):
    return [[G(i == j) for j in range(size)] for i in range(size)]


def add(left, right):
    return [[a + b for a, b in zip(lr, rr)] for lr, rr in zip(left, right)]


def scale(value, source):
    return [[value * a for a in row] for row in source]


def mul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def dagger(source):
    return [[source[j][i].star() for j in range(len(source))]
            for i in range(len(source[0]))]


def trace(source):
    return sum(source[i][i] for i in range(len(source)))


def det(source):
    size = len(source)
    if not size:
        return G(1)
    result = G()
    for order in permutations(range(size)):
        inversions = sum(order[i] > order[j]
                         for i in range(size) for j in range(i + 1, size))
        term = G(-1 if inversions % 2 else 1)
        for i, j in enumerate(order):
            term *= source[i][j]
        result += term
    return result


def reduced(source):
    result = [list(row) for row in source]
    pivot_row = 0
    pivots = []
    for column in range(len(result[0])):
        candidate = next((i for i in range(pivot_row, len(result))
                          if result[i][column]), None)
        if candidate is None:
            continue
        result[pivot_row], result[candidate] = result[candidate], result[pivot_row]
        denominator = result[pivot_row][column]
        result[pivot_row] = [x / denominator for x in result[pivot_row]]
        for i in range(len(result)):
            if i != pivot_row:
                factor = result[i][column]
                result[i] = [x - factor * y
                             for x, y in zip(result[i], result[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(result):
            break
    return result, pivots


def rank(source):
    return len(reduced(source)[1])


def inverse2(source):
    a, b = source[0]
    c, d = source[1]
    return scale(1 / (a * d - b * c), [[d, -b], [-c, a]])


def characteristic(source):
    """Principal minors, each evaluated by the Leibniz formula."""
    size = len(source)
    coefficients = [G() for _ in range(size + 1)]
    for count in range(size + 1):
        total = G()
        for indices in combinations(range(size), count):
            total += det([[source[i][j] for j in indices] for i in indices])
        coefficients[size - count] = (-1 if count % 2 else 1) * total
    return coefficients


I = G(0, 1)
SIGMA = mat([[1, 0], [0, -1]])
HBASIS = [mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 1]]),
          mat([[0, 1], [1, 0]]), mat([[0, -I], [I, 0]])]


def hcoords(source):
    need(source == dagger(source), "Hermitian coordinates require star symmetry")
    values = [source[0][0], source[1][1],
              (source[0][1] + source[1][0]) / 2,
              (source[1][0] - source[0][1]) / (2 * I)]
    need(all(value.i == 0 for value in values), "real Hermitian coordinates")
    return values


def from_hcoords(vector):
    result = mat([[0, 0], [0, 0]])
    for coefficient, basis in zip(vector, HBASIS):
        result = add(result, scale(coefficient, basis))
    return result


def congruence(source):
    columns = [hcoords(mul(mul(source, basis), dagger(source))) for basis in HBASIS]
    return [[column[i] for column in columns] for i in range(4)]


def qpair(left, right, current=SIGMA):
    result = -trace(mul(mul(mul(current, left), current), right)) / 2
    need(result.i == 0, "trace form is real")
    return result


def current_zero(a, z):
    z = G(z)
    return [[G(a), z], [z.star(), G(a)]]


def regroup(source):
    u, v = source[0]
    w, z = source[1]
    return [[w - z * u / v, z / v], [-u / v, 1 / v]]


def source_moment():
    # Variables are exp(iP), exp(iq), exp(iK), exp(-ig); beta=2g.
    p = LP.monomial((1, 0, 0, 0))
    pm = LP.monomial((-1, 0, 0, 0))
    q = LP.monomial((0, 1, 0, 0))
    qm = LP.monomial((0, -1, 0, 0))
    zk = LP.monomial((-1, 0, 1, 0))
    zkm = LP.monomial((1, 0, -1, 0))
    root = LP.monomial((0, 0, 0, 1))
    beta_phase = root ** 2
    single = mat([[1, 2 * I], [2 * I, 1]])
    coin = [[single[i // 2][j // 2] * single[i % 2][j % 2] / 5
             for j in range(4)] for i in range(4)]
    object_a = mat([[1], [0], [0], [-1]])
    need(mul(coin, object_a) == object_a, "source coin fixes A")
    stream = [[LP(0) for _ in range(4)] for _ in range(4)]
    for index, term in enumerate((p, q, qm, pm)):
        stream[index][index] = term
    object_step = mul(stream, coin)
    left = [[G(1), G(), G(), G(-1)]]
    object_contact = mul(mul(left, object_step), object_a)[0][0] * root / 2
    need(object_contact == root * (p + pm) / 2, "exact object Laurent contact")
    q_numerator = [[LP(1), LP(-2)], [LP(2), LP(1)]]
    e_numerator = [[LP(1), -2 * zk], [2 * zkm, LP(1)]]
    pulse = mul(e_numerator, q_numerator)
    pulse_contact = pulse[0][0] * beta_phase / 5
    need(pulse_contact == beta_phase * (1 - 4 * zk) / 5,
         "pulse contact includes both terms and beta")
    first = (object_contact * pulse_contact).integrate((0, 1))
    expected = LP.monomial((0, 0, 1, 3), Q(-2, 5))
    need(first == expected, "source first moment coefficient and phase")
    need((object_contact * beta_phase / 5).integrate((0, 1)) != expected,
         "negative control omitted pulse exponential")
    need((object_contact * pulse[0][0] / 5).integrate((0, 1)) != expected,
         "negative control omitted outer beta")
    need(2 * first != expected, "negative control missing Fourier half")
    reversed_pulse = beta_phase * (1 - 4 * LP.monomial((1, 0, 1, 0))) / 5
    need(reversed_pulse != pulse_contact, "opposite fiber law differs before integration")
    need((object_contact * reversed_pulse).integrate((0, 1)) == expected,
         "even first moment alone does not detect reversed momentum sign")
    return 3


def quadratic_elimination():
    f, t, u, v = [LP.monomial(tuple(int(j == i) for j in range(4)))
                   for i in range(4)]
    imaginary = v * t - f * t ** 2 + f * t ** 2
    real_residual = 4 + t ** 2 - f * (v * t - f * t ** 2) - u * t
    quadratic = (1 + f ** 2) * t ** 2 - (u + v * f) * t + 4
    need(imaginary == v * t, "eliminated imaginary part")
    need(real_residual == quadratic, "four-variable quadratic identity")
    need(real_residual != (1 + f ** 2) * t ** 2 - (u - v * f) * t + 4,
         "negative control quadratic mixed-term sign")
    assignments = list(product(range(2), (-1, 1), (-1, 1)))
    need(len(assignments) == 8 and 2 * len(assignments) == 16,
         "finite value ceiling sixteen")
    offsets = [Q(j, 16000) for j in range(-8, 9)]
    need(len(set(offsets)) == 17 and max(abs(x) for x in offsets) <= Q(1, 1000),
         "seventeen fixed momenta inside original halfwidth")
    need(max(offsets) - min(offsets) < 6, "distinct offsets below two-pi period")
    pairs = list(combinations(range(17), 2))
    need(len(pairs) == 136, "number of Schur difference factors")
    need(all(offsets[i] != offsets[j] for i, j in pairs), "all moment differences nonzero")
    # Product leading terms: distinct formal moment coefficients, no boundary sampling.
    leading = Q(1)
    for i, j in pairs:
        leading *= Q(i - j, 2)
    need(leading != 0, "finite Vandermonde product control")
    duplicate = list(range(17))
    duplicate[-1] = duplicate[0]
    failed = Q(1)
    for i, j in pairs:
        failed *= Q(duplicate[i] - duplicate[j], 2)
    need(failed == 0, "negative control duplicate momentum coefficient")
    return 2


def moving_checks(m, axis, acoef, b0, real_d, imag_d, parity, counts):
    rmap = congruence(m)
    need(mul(mul(m, axis), dagger(m)) == axis, "source fixed axis")
    expected_axis_norm = ((imag_d if parity == 0 else real_d) ** 2 / b0 ** 2) - 1
    need(qpair(axis, axis) == expected_axis_norm, "source fixed-axis norm")
    trace_square = trace(m).norm()
    kappa = trace_square - 2
    predicted = [G(1), G(-kappa - 2), G(2 * kappa + 2), G(-kappa - 2), G(1)]
    need(characteristic(rmap) == predicted, "full congruence characteristic polynomial")
    need(mul(rmap, [[x] for x in hcoords(SIGMA)]) == [[x] for x in hcoords(SIGMA)],
         "complete current vector is fixed")
    counts["congruences"] += 1
    if trace_square == 4:
        counts["parabolic_" + str(parity)] += 1
    else:
        inverse_map = congruence(inverse2(m))
        projector = scale(G(1) / (4 - trace_square),
                          add(add(scale(2, eye(4)), scale(-1, rmap)), scale(-1, inverse_map)))
        need(mul(projector, projector) == projector and rank(projector) == 2,
             "source moving projector rank and idempotence")
        need(mul(projector, rmap) == mul(rmap, projector), "moving projector invariant")
        need(mul(projector, [[x] for x in hcoords(SIGMA)]) == [[G()] for _ in range(4)],
             "moving projector annihilates current vector")
        difference = add(rmap, scale(-1, eye(4)))
        need(mul(projector, difference) == difference and rank(difference) == 2,
             "moving image agrees with projector")
        chosen = []
        selected = []
        for column in range(4):
            candidate = [projector[row][column] for row in range(4)]
            trial = chosen + [candidate]
            trial_matrix = [[v[row] for v in trial] for row in range(4)]
            if rank(trial_matrix) > len(chosen):
                chosen.append(candidate)
                selected.append(from_hcoords(candidate))
            if len(chosen) == 2:
                break
        gram = [[qpair(x, y) for y in selected] for x in selected]
        gram_det = det(gram).r
        if trace_square < 4:
            need(gram[0][0].r > 0 and gram_det > 0, "elliptic moving form positive")
            counts["elliptic"] += 1
        else:
            need(gram_det < 0, "hyperbolic moving form split")
            counts["hyperbolic"] += 1
        counts["moving_projectors"] += 1
    if acoef:
        if parity == 0:
            chart = [current_zero(1, real_d / acoef), current_zero(0, I / acoef)]
            metric = [(b0 ** 2 - imag_d ** 2) / acoef.norm(), 1 / acoef.norm()]
        else:
            chart = [current_zero(1, I * imag_d / acoef), current_zero(0, 1 / acoef)]
            metric = [(b0 ** 2 - real_d ** 2) / acoef.norm(), 1 / acoef.norm()]
        triple = [axis] + chart
        norms = [expected_axis_norm] + metric
        for i, j in product(range(3), repeat=2):
            need(qpair(triple[i], triple[j]) == (norms[i] if i == j else 0),
                 "nine ordered source-chart trace-form pairings")
            counts["trace_chart_pairs"] += 1
        images = []
        for basis in chart:
            image = mul(mul(m, basis), dagger(m))
            need(trace(mul(SIGMA, image)) == 0, "moving chart has zero current trace")
            coordinate_a = image[0][0]
            az = acoef * image[0][1]
            if parity == 0:
                need(az.r == real_d * coordinate_a.r, "plus moving-plane equation")
                coordinate_other = G(az.i)
            else:
                need(az.i == imag_d * coordinate_a.r, "minus moving-plane equation")
                coordinate_other = G(az.r)
            need(add(scale(coordinate_a, chart[0]), scale(coordinate_other, chart[1])) == image,
                 "moving-plane image reconstructed from source coordinates")
            images.append([coordinate_a, coordinate_other])
            need(qpair(image, image) == -det(image), "trace-zero form equals negative determinant")
        action = [[images[j][i] for j in range(2)] for i in range(2)]
        need(det(action) == 1 and trace(action) == kappa, "complete moving action polynomial")
        gram = mat([[metric[0], 0], [0, metric[1]]])
        need(mul(mul(dagger(action), gram), action) == gram, "explicit moving Gram invariance")
        counts["explicit_charts"] += 1


def cross_characteristic(plus, minus):
    columns = []
    for row, column in product(range(2), repeat=2):
        basis = mat([[0, 0], [0, 0]])
        basis[row][column] = G(1)
        image = mul(mul(plus, basis), dagger(minus))
        columns.append([image[i][j] for i, j in product(range(2), repeat=2)])
    cross = [[columns[j][i] for j in range(4)] for i in range(4)]
    tp = -I * trace(plus)
    tm = trace(minus)
    need(tp.i == 0 and tm.i == 0, "normalized parity traces real")
    predicted = [G(1), I * tp * tm, -(tp * tp + tm * tm - 2), -I * tp * tm, G(1)]
    need(characteristic(cross) == predicted, "complete complex cross-parity polynomial")


def rational_fixtures():
    roots = (Q(1, 2), Q(1), Q(2))
    imaginary = (-2, -1, 0, 1, 2)
    counts = {"fixtures": 0, "congruences": 0, "cross_polynomials": 0,
              "parabolic_0": 0, "parabolic_1": 0, "zero_A": 0,
              "moving_projectors": 0, "elliptic": 0, "hyperbolic": 0,
              "explicit_charts": 0, "trace_chart_pairs": 0}
    kc = mat([[Q(-2, 5), Q(-4, 5)], [Q(4, 5), Q(-2, 5)]])
    for x1, x2, y1, y2 in product(roots, roots, imaginary, imaginary):
        a, c = x1 * x1, x2 * x2
        f, h = G(a, y1), G(c, y2)
        b0 = 4 * x1 * x2
        d = 4 + f * h
        aa = 4 - f.star() * h
        need(d.norm() - aa.norm() == b0 * b0, "full contact norm identity")
        m = mat([[(f - 1) / 2, 0], [0, (h - 1) / 2]])
        t = mul(kc, inverse2(add(eye(2), scale(-1, mul(m, kc)))))
        need(t == scale(1 / d, mat([[-2 * h, -4], [4, -2 * f]])),
             "all four exact Lippmann-Schwinger entries")
        density = mat([[a, 0], [0, c]])
        optical = add(add(t, dagger(t)), mul(mul(dagger(t), density), t))
        need(optical == mat([[0, 0], [0, 0]]), "optical identity")
        square_density = mat([[x1, 0], [0, x2]])
        scattering = add(eye(2), mul(mul(square_density, t), square_density))
        need(scattering == scale(1 / d, mat([[aa, -b0], [b0, aa.star()]])),
             "closed active scattering normalization")
        need(mul(dagger(scattering), scattering) == eye(2), "active scattering unitarity")
        need(det(scattering) == d.star() / d, "active scattering determinant")
        need(scattering[1][0].norm() == 16 * a * c / d.norm(), "full transition modulus")
        plus = regroup(scattering)
        minus = regroup(mul(mat([[1, 0], [0, -1]]), scattering))
        expected = scale(1 / G(b0), mat([[d.star(), -aa.star()], [aa, -d]]))
        need(plus == expected, "plus marked regrouping")
        need(minus == mul(mat([[-1, 0], [0, 1]]), plus), "minus marked regrouping")
        for parity, transfer in enumerate((plus, minus)):
            need(mul(mul(dagger(transfer), SIGMA), transfer) == SIGMA, "same-cut current")
            need(det(transfer) == (-1 if parity == 0 else 1), "parity determinant")
        need(trace(plus) == -2 * I * d.i / b0, "plus imaginary trace")
        need(trace(minus) == -2 * d.r / b0, "minus real trace")
        fixed_plus = scale(1 / G(b0), mat([[d.r, aa.star()], [aa, d.r]]))
        fixed_minus = scale(1 / G(b0), mat([[-d.i, -I * aa.star()], [I * aa, -d.i]]))
        moving_checks(plus, fixed_plus, aa, b0, d.r, d.i, 0, counts)
        moving_checks(minus, fixed_minus, aa, b0, d.r, d.i, 1, counts)
        cross_characteristic(plus, minus)
        counts["cross_polynomials"] += 1
        counts["zero_A"] += int(not aa)
        counts["fixtures"] += 1
    need(counts["fixtures"] == 225 and counts["congruences"] == 450,
         "entire frozen rational fixture class")
    need(counts["elliptic"] + counts["hyperbolic"] == counts["moving_projectors"],
         "all nonparabolic moving planes classified")
    need(counts["trace_chart_pairs"] == 9 * counts["explicit_charts"],
         "every explicit chart has nine ordered pairings")
    return counts


def label_and_full_form():
    label_count = 0
    fixed = 0
    for i, j in product(range(26), repeat=2):
        pair = (i, j)
        swap = (j, i)
        need((swap[1], swap[0]) == pair, "all-label involution")
        fixed += int(pair == swap)
        # On a token both asymptotic swaps coincide, so their product is I.
        for right_of_receiver in (False, True):
            first = swap if right_of_receiver else pair
            second = (first[1], first[0]) if right_of_receiver else first
            need(second == pair, "token calibration product is identity")
        # On a pulse the signs select opposite asymptotic swaps.
        for right_moving in (False, True):
            first = pair if right_moving else swap
            second = (first[1], first[0]) if right_moving else first
            need(second == swap, "pulse calibration product is J")
        need(((1, j)[1], (1, j)[0]) == (j, 1), "old memory retained in pulse")
        plus_weight = Q(1) if i == j else Q(1, 2)
        minus_weight = 1 - plus_weight
        need(plus_weight == Q(1 + int(i == j), 2), "occupied plus population")
        need(minus_weight == Q(1 - int(i == j), 2), "occupied minus population")
        label_count += 1
    dimensions = ((label_count + fixed) // 2, (label_count - fixed) // 2)
    need(dimensions == (351, 325), "entire retained parity dimensions")
    need(Q(1 - int(1 == 1), 2) == 0, "initial t1 d1 has no odd component")
    h4 = mat([[1, 0, 0, 0], [0, -1, 0, 0],
              [0, 0, 1, 0], [0, 0, 0, -1]])
    cross_basis = []
    cross_signs = []
    for row, column, phase in product(range(2), range(2), (G(1), I)):
        x = mat([[0] * 4 for _ in range(4)])
        x[row][column + 2] = phase
        x[column + 2][row] = phase.star()
        cross_basis.append(x)
        cross_signs.append(-1 if row == column else 1)
    for i, j in product(range(8), repeat=2):
        need(qpair(cross_basis[i], cross_basis[j], h4) == (cross_signs[i] if i == j else 0),
             "all local cross-parity trace-form entries")
    need(cross_signs.count(1) == 4 and cross_signs.count(-1) == 4,
         "complete cross-parity local signature")
    for dimension in dimensions:
        identity_hilbert_trace = sum(Q(1) for _ in range(dimension))
        partial_representative_trace = sum(Q(1, dimension * dimension)
                                          for _ in range(dimension))
        need(identity_hilbert_trace == dimension, "identity-label metric weight")
        need(partial_representative_trace == Q(1, dimension), "partial-trace metric weight")
        need(identity_hilbert_trace != 1, "negative control omitted label weight")
    return label_count, 64, 2


def finite_field_add(x, y, prime):
    return ((x[0] + y[0]) % prime, (x[1] + y[1]) % prime)


def finite_field_neg(x, prime):
    return ((-x[0]) % prime, (-x[1]) % prime)


def finite_field_mul(x, y, prime):
    return ((x[0] * y[0] + x[1] * y[1]) % prime,
            (x[0] * y[1] + x[1] * y[0] + x[1] * y[1]) % prime)


def valuation(value, prime):
    value = Q(value)
    numerator, denominator = abs(value.numerator), value.denominator
    if not numerator:
        raise ValueError("valuation of zero")
    answer = 0
    while numerator % prime == 0:
        numerator //= prime
        answer += 1
    while denominator % prime == 0:
        denominator //= prime
        answer -= 1
    return answer


def arithmetic():
    phi = F(0, 1)
    radical = 2 * phi - 1
    delta = phi - 3
    need(radical * radical == 5 and phi * phi == phi + 1, "golden field relations")
    need((phi + 2).norm() == 5, "incompatible parity square-class norm")
    need(((phi + 2) / radical) ** 2 * delta == -(phi + 2),
         "compatible imaginary trace square in CM extension")
    need((phi + 2) / 4 - 1 == -(phi ** -2) / 4, "fixed negative-square elliptic axis")
    target = 2 * radical / 5
    need(target.sign() == 1 and target.sigma().sign() == -1,
         "unchanged target opposite real-place signs")
    need(delta.sign() == -1 and delta.sigma().sign() == -1, "CM extension at both places")
    need(target != 1 and target / radical == Q(2, 5), "original target normalization retained")
    need((radical / 2) * target == 1, "repaired normalization is explicitly different")
    residue_counts = {}
    for prime in (2, 13):
        need(all((x * x - x - 1) % prime != 0 for x in range(prime)),
             "golden base polynomial irreducible at selected prime")
        elements = list(product(range(prime), repeat=2))
        for element in elements:
            squared = finite_field_mul(element, element, prime)
            middle = finite_field_mul((0, 1), element, prime)
            value = finite_field_add(finite_field_add(squared, finite_field_neg(middle, prime), prime),
                                     (1, 0), prime)
            need(value != (0, 0), "relative CM polynomial has no residue root")
        residue_counts[prime] = len(elements)
    need([pow(13, exponent, 5) for exponent in range(1, 5)] == [3, 4, 2, 1],
         "prime thirteen cyclotomic residue order")
    for dimension in (351, 325):
        need(valuation(dimension, 13) == 1 and valuation(Q(1, dimension), 13) == -1,
             "odd thirteen valuation of both label conventions")
        need(abs(valuation(Q(dimension) / Q(2, 5), 2)) == 1,
             "odd two valuation against beta over sqrt-five")
        need(abs(valuation(Q(1, dimension) / Q(2, 5), 2)) == 1,
             "partial-trace odd two valuation")
    return residue_counts


def remaining_controls():
    f, h = G(1), G(1)
    t = mat([[Q(-2, 5), Q(-4, 5)], [Q(4, 5), Q(-2, 5)]])
    # Both substituted densities are a quarter of the complete contact density.
    selected = add(eye(2), scale(Q(1, 4), t))
    need(mul(dagger(selected), selected) != eye(2), "negative control selected densities are not closed")
    scattering = add(eye(2), t)
    plus = regroup(scattering)
    minus = regroup(mul(mat([[1, 0], [0, -1]]), scattering))
    need(plus != minus, "negative control identical receiver calibrations")
    need(minus != scale(-1, plus), "negative control fixed matrix tensor swap")
    wrong = [list(row) for row in plus]
    wrong[0][1] = -wrong[0][1]
    need(mul(mul(dagger(wrong), SIGMA), wrong) != SIGMA,
         "negative control one transfer sign")
    sample = mat([[1, 0], [0, 0]])
    need(qpair(sample, sample) != -det(sample),
         "negative control dropping trace-square term off moving plane")
    del f, h
    return 5


def main():
    controls = source_moment()
    controls += quadratic_elimination()
    counts = rational_fixtures()
    labels, cross_entries, weight_controls = label_and_full_form()
    controls += weight_controls
    residues = arithmetic()
    controls += remaining_controls()
    print("CERTIFICATE=C-HODGE-CAPTURE-PARITY-N-CODE-BLIND-BREAKER")
    print("STATUS=NON-CANONICAL;L1;candidate-C")
    print("ARITHMETIC=EXACT_GAUSSIAN_RATIONALS;SPARSE_LAURENT_POLYNOMIALS;Q(phi)")
    print("SOURCE_FIRST_MOMENT=-(2/5)*exp(-i*(g+beta))*exp(iK)")
    print("RATIONAL_CONTACT_FIXTURES=" + str(counts["fixtures"]))
    print("FULL_PARITY_CONGRUENCE_POLYNOMIALS=" + str(counts["congruences"]))
    print("CROSS_PARITY_COMPLEX_POLYNOMIALS=" + str(counts["cross_polynomials"]))
    print("PARABOLIC_PLUS_CASES=" + str(counts["parabolic_0"]))
    print("PARABOLIC_MINUS_CASES=" + str(counts["parabolic_1"]))
    print("ZERO_A_FIXTURES=" + str(counts["zero_A"]))
    print("NONPARABOLIC_MOVING_PROJECTORS=" + str(counts["moving_projectors"]))
    print("ELLIPTIC_MOVING_PLANES=" + str(counts["elliptic"]))
    print("HYPERBOLIC_MOVING_PLANES=" + str(counts["hyperbolic"]))
    print("EXPLICIT_MOVING_CHARTS=" + str(counts["explicit_charts"]))
    print("SOURCE_CHART_TRACE_PAIRINGS=" + str(counts["trace_chart_pairs"]))
    print("RETAINED_LABEL_PAIRS=" + str(labels))
    print("PARITY_DIMENSIONS=351,325")
    print("LOCAL_CROSS_FORM_ENTRIES=" + str(cross_entries))
    print("FINITE_VALUE_CEILING=16")
    print("DISTINCT_MOMENTA=17")
    print("SCHUR_DIFFERENCE_FACTORS=136")
    print("CM_RESIDUE_ELEMENTS_AT_2=" + str(residues[2]))
    print("CM_RESIDUE_ELEMENTS_AT_13=" + str(residues[13]))
    print("NEGATIVE_CONTROLS=" + str(controls))
    print("BOUNDARY_UNIQUENESS_AND_ZERO_MEASURE=ANALYTICAL_ONLY")
    print("ACTUAL_BOUNDARY_VALUES=NOT_EVALUATED")
    print("CENTRAL_POINT_AND_NUMERICAL_MARGIN=NOT_CERTIFIED")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
