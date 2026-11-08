#!/usr/bin/env python3
"""Independent exact recurrence/dual audit of the frozen scalar completion.

This file reads only the five normative files.  It neither imports nor reads
another scientific program.  Its sole output is the unmodified certificate.
"""

from fractions import Fraction as Q
from hashlib import sha256
from math import comb, lcm
from pathlib import Path


ORDER = 6
NAME = "P-INTEGER-SCALAR-LAPSE-RIGIDITY-1"
AUTHORITY = (
    ("CANON.md", 1052518,
     "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714,
     "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382,
     "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811,
     "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770,
     "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class Failure(Exception):
    pass


def need(condition, kind):
    if not condition:
        raise Failure(kind)


class Dual:
    """Forward directional derivative over Q, with no numerical evaluation."""

    __slots__ = ("value", "tangent")

    def __init__(self, value, tangent=0):
        self.value = Q(value)
        self.tangent = Q(tangent)

    @staticmethod
    def lift(other):
        return other if isinstance(other, Dual) else Dual(other)

    def __add__(self, other):
        other = self.lift(other)
        return Dual(self.value + other.value, self.tangent + other.tangent)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.tangent)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) + (-self)

    def __mul__(self, other):
        other = self.lift(other)
        return Dual(self.value * other.value,
                    self.tangent * other.value + self.value * other.tangent)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        return Dual(self.value / other.value,
                    (self.tangent * other.value - self.value * other.tangent)
                    / (other.value * other.value))

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, degree):
        if degree == 0:
            return Dual(1)
        return Dual(self.value ** degree,
                    degree * self.value ** (degree - 1) * self.tangent)

    def __eq__(self, other):
        other = self.lift(other)
        return self.value == other.value and self.tangent == other.tangent


def value(number):
    return number.value if isinstance(number, Dual) else number


def tangent(number):
    return number.tangent if isinstance(number, Dual) else Q(0)


def zeros(rows, cols=None):
    return [[Q(0) for _ in range(rows if cols is None else cols)]
            for _ in range(rows)]


def eye(size):
    return [[Q(i == j) for j in range(size)] for i in range(size)]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def plus(left, right):
    return [[a + b for a, b in zip(row, other)]
            for row, other in zip(left, right)]


def scale(matrix, scalar):
    return [[entry * scalar for entry in row] for row in matrix]


def times(left, right):
    result = zeros(len(left), len(right[0]))
    for i, row in enumerate(left):
        for k, coefficient in enumerate(row):
            if coefficient != 0:
                for j, entry in enumerate(right[k]):
                    if entry != 0:
                        result[i][j] += coefficient * entry
    return result


def apply(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), Q(0))
            for row in matrix]


def inner(left, right):
    return sum((a * b for a, b in zip(left, right)), Q(0))


def vplus(left, right):
    return [a + b for a, b in zip(left, right)]


def vscale(vector, scalar):
    return [entry * scalar for entry in vector]


def vminus(left, right):
    return [a - b for a, b in zip(left, right)]


def quadratic(left, matrix, right=None):
    return inner(left, apply(matrix, left if right is None else right))


def inverse(matrix):
    size = len(matrix)
    unit = eye(size)
    rows = [list(matrix[i]) + unit[i] for i in range(size)]
    for col in range(size):
        pivot = next((i for i in range(col, size)
                      if value(rows[i][col]) != 0), None)
        if pivot is None:
            raise Failure("F_RATIONAL")
        rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [entry / divisor for entry in rows[col]]
        for i in range(size):
            if i != col and rows[i][col] != 0:
                multiplier = rows[i][col]
                rows[i] = [a - multiplier * b
                           for a, b in zip(rows[i], rows[col])]
    return [row[size:] for row in rows]


def coefficient_product(left, right, degree):
    result = zeros(len(left[0]), len(right[0][0]))
    for i in range(degree + 1):
        result = plus(result, times(left[i], right[degree - i]))
    return result


def series_inverse(series):
    first = inverse(series[0])
    result = [first]
    for degree in range(1, len(series)):
        total = zeros(len(first))
        for j in range(1, degree + 1):
            total = plus(total, times(series[j], result[degree - j]))
        result.append(scale(times(first, total), -1))
    return result


def flatten(matrix):
    return [entry for row in matrix for entry in row]


def csv(entries):
    return ",".join(str(Q(entry)) for entry in entries)


def geometry():
    # Each oriented edge contributes its weighted outer incidence product.
    laplacian = zeros(5)
    for jump, numerator in ((1, 29), (2, 65)):
        for tail in range(5):
            incidence = [Q(0)] * 5
            incidence[tail] = -1
            incidence[(tail + jump) % 5] = 1
            for row in range(5):
                for col in range(5):
                    laplacian[row][col] += (Q(numerator, 324)
                                           * incidence[row] * incidence[col])
    expected_l = [[Q(188 if r == c else
                     -29 if (c-r) % 5 in (1, 4) else -65, 324)
                   for c in range(5)] for r in range(5)]
    need(laplacian == expected_l, "F_CARRIER")
    potential = zeros(6)
    for row in range(5):
        potential[row][:5] = laplacian[row]
    potential[0][5] = potential[5][0] = Q(-1, 324)
    potential[1][5] = potential[5][1] = Q(1, 324)
    potential[5][5] = Q(1)
    c = plus(eye(6), scale(potential, Q(-1, 2)))
    d = plus(eye(6), scale(times(c, c), -1))
    k, m, j, metric = (zeros(12) for _ in range(4))
    for row in range(6):
        for col in range(6):
            delta = Q(row == col)
            k[row][col + 6] = delta
            k[row + 6][col] = -d[row][col]
            m[row][col] = m[row + 6][col + 6] = c[row][col]
            m[row][col + 6] = delta
            m[row + 6][col] = -d[row][col]
            j[row][col + 6] = delta
            j[row + 6][col] = -delta
            metric[row][col] = d[row][col]
            metric[row + 6][col + 6] = delta
    for matrix in (potential, c, d, metric):
        need(matrix == transpose(matrix), "F_CARRIER")
    need(times(times(transpose(m), j), m) == j, "F_CARRIER")
    need(times(times(transpose(m), metric), m) == metric, "F_CARRIER")
    need(times(m, k) == times(k, m), "F_CARRIER")
    need(sum(d[i][i] for i in range(6)) == Q(163223, 52488), "F_CARRIER")
    square_k = times(k, k)
    need(sum(square_k[i][i] for i in range(12)) == Q(-163223, 26244),
         "F_CARRIER")
    uniform = [Q(1)] * 5 + [Q(0)]
    need(apply(d, uniform) == [0] * 6, "F_CARRIER")
    basis = zeros(6, 5)
    for col in range(4):
        basis[col][col], basis[4][col] = Q(1), Q(-1)
    basis[5][4] = Q(1)
    gram = times(times(transpose(basis), d), basis)
    lower, pivots = eye(5), []
    for col in range(5):
        pivot = gram[col][col] - sum(lower[col][a] ** 2 * pivots[a]
                                    for a in range(col))
        need(pivot > 0, "F_CARRIER")
        pivots.append(pivot)
        for row in range(col + 1, 5):
            lower[row][col] = (gram[row][col]
                              - sum(lower[row][a] * lower[col][a] * pivots[a]
                                    for a in range(col))) / pivot
    return potential, c, d, k, m, j, metric, uniform, pivots


def completion(k, m, j, metric, d):
    # Solve the coefficient recurrence (n+1)R[n+1]=K R[n].
    relative = [eye(12)]
    for degree in range(1, ORDER + 1):
        relative.append(scale(times(k, relative[-1]), Q(1, degree)))
    transfers = [times(m, term) for term in relative]
    upper = [[row[:6] for row in term[:6]] for term in transfers]
    bond = [[row[6:] for row in term[:6]] for term in transfers]
    ecoef = series_inverse(bond)
    acoef = [coefficient_product(ecoef, upper, degree)
             for degree in range(ORDER + 1)]
    for degree in range(ORDER + 1):
        for form in (j, metric):
            result = zeros(12)
            for a in range(degree + 1):
                result = plus(result, times(times(transpose(relative[a]), form),
                                            relative[degree-a]))
            need(result == (form if degree == 0 else zeros(12)), "F_SERIES")
        invariant = plus(coefficient_product(upper, upper, degree),
                         times(d, coefficient_product(bond, bond, degree)))
        need(invariant == (eye(6) if degree == 0 else zeros(6)), "F_SERIES")
        need(acoef[degree] == transpose(acoef[degree]), "F_SERIES")
        need(ecoef[degree] == transpose(ecoef[degree]), "F_SERIES")
    pairs = 0
    for a in range(ORDER + 1):
        for b in range(ORDER + 1 - a):
            need(times(relative[a], relative[b])
                 == scale(relative[a+b], comb(a+b, a)), "F_SERIES")
            pairs += 1
    for degree in range(ORDER):
        need(scale(ecoef[degree+1], degree+1)
             == scale(coefficient_product(acoef, ecoef, degree), -1), "F_SERIES")
        need(scale(acoef[degree+1], degree+1)
             == scale(coefficient_product(ecoef, ecoef, degree), -1), "F_SERIES")
    return relative, ecoef, acoef, pairs


def fixture(seed, vertex, coordinate):
    return Q(((seed+2)*(vertex+1)*(coordinate+3)
              + (vertex-coordinate)**2) % 17 - 8, seed+2)


def unscaled_action(q, capital_q, acoef, ecoef):
    return [(quadratic(q, a) + quadratic(capital_q, a)) / 2
            - quadratic(q, e, capital_q) for a, e in zip(acoef, ecoef)]


def action_series(fields, alpha, potential, acoef, ecoef):
    result = [Q(0)] * len(acoef)
    result[0] = (quadratic(fields[0], potential)
                 + quadratic(fields[-1], potential)) / 4
    for b in range(1, len(fields)):
        coefficients = unscaled_action(fields[b-1], fields[b], acoef, ecoef)
        for degree, coefficient in enumerate(coefficients):
            result[degree] += alpha[b-1] ** degree * coefficient
    return result


def gradient_series(fields, alpha, acoef, ecoef):
    length = len(fields)
    result = [zeros(length, 6) for _ in acoef]
    for degree, (a, e) in enumerate(zip(acoef, ecoef)):
        for n in range(1, length-1):
            left = vminus(apply(a, fields[n]), apply(e, fields[n-1]))
            right = vminus(apply(a, fields[n]), apply(e, fields[n+1]))
            result[degree][n] = vplus(vscale(left, alpha[n-1] ** degree),
                                      vscale(right, alpha[n] ** degree))
    return result


def skew_action(fields_gradient, alpha, parameter):
    result = zeros(len(fields_gradient), 6)
    for n in range(1, len(fields_gradient)-2):
        weight = alpha[n] * (parameter[n] + parameter[n+1]) / 8
        result[n] = vplus(result[n], vscale(fields_gradient[n+1], weight))
        result[n+1] = vminus(result[n+1], vscale(fields_gradient[n], weight))
    return result


def generator(fields, alpha, parameter, acoef, ecoef, degree, adjusted):
    result = [zeros(len(fields), 6) for _ in range(degree+1)]
    for power in range(degree):
        for n in range(1, len(fields)-1):
            left = vminus(apply(acoef[power], fields[n]),
                          apply(ecoef[power], fields[n-1]))
            right = vminus(apply(ecoef[power], fields[n+1]),
                           apply(acoef[power], fields[n]))
            mean = vplus(vscale(left, alpha[n-1] ** power),
                         vscale(right, alpha[n] ** power))
            result[power+1][n] = vscale(mean, parameter[n] / 2)
    if adjusted:
        gradients = gradient_series(fields, alpha, acoef, ecoef)
        for power in range(2, degree+1):
            result[power] = plus(result[power],
                                 skew_action(gradients[power-2], alpha, parameter))
    return result


def field_work(gradient, variation, degree):
    return sum((inner(flatten(gradient[a]), flatten(variation[degree-a]))
                for a in range(degree+1)), Q(0))


def jet_check(fields, alpha, parameter, c, acoef, ecoef, raw, adjusted):
    c2 = times(c, c)
    one_plus_c2 = plus(eye(6), c2)
    expected = [zeros(len(fields), 6) for _ in range(4)]
    f0, f1 = zeros(len(fields), 6), zeros(len(fields), 6)
    for n in range(1, len(fields)-1):
        previous, middle, following = fields[n-1:n+2]
        expected[1][n] = vscale(vminus(following, previous), parameter[n]/2)
        expected[2][n] = vscale(vminus(
            vscale(vminus(middle, apply(c, following)), alpha[n]),
            vscale(vminus(middle, apply(c, previous)), alpha[n-1])),
            parameter[n]/2)
        expected[3][n] = vscale(vplus(
            vscale(vminus(vscale(apply(c, middle), 2),
                          apply(one_plus_c2, previous)), alpha[n-1]**2),
            vscale(vminus(apply(one_plus_c2, following),
                          vscale(apply(c, middle), 2)), alpha[n]**2)),
            parameter[n]/4)
        f0[n] = vminus(vminus(vscale(apply(c, middle), 2), previous), following)
        f1[n] = vplus(vscale(middle, -alpha[n-1]-alpha[n]),
                      vplus(vscale(apply(c, previous), alpha[n-1]),
                            vscale(apply(c, following), alpha[n])))
    for power in (1, 2, 3):
        need(raw[power] == expected[power], "F_JET")
    need(adjusted[1] == expected[1], "F_JET")
    need(adjusted[2] == plus(expected[2], skew_action(f0, alpha, parameter)),
         "F_JET")
    need(adjusted[3] == plus(expected[3], skew_action(f1, alpha, parameter)),
         "F_JET")
    exact_gradient = gradient_series(fields, alpha, acoef, ecoef)
    need(exact_gradient[0] == f0 and exact_gradient[1] == f1, "F_JET")


def cayley(scalar, k, m):
    minus = plus(eye(12), scale(k, -scalar/2))
    positive = plus(eye(12), scale(k, scalar/2))
    relative = times(inverse(minus), positive)
    return relative, times(m, relative)


def cayley_coefficients(scalar, k, m):
    _, transfer = cayley(scalar, k, m)
    upper = [row[:6] for row in transfer[:6]]
    bond = [row[6:] for row in transfer[:6]]
    e = inverse(bond)
    return times(e, upper), e


def actual_bracket(fields, alpha, first, second, acoef, ecoef, adjusted):
    """Differentiate the actual generator in every tangent direction.

    The alpha tangent is order zero; each coefficient of the field tangent
    supplies a separate dual differentiation followed by degree convolution.
    No predicted bracket formula enters this construction.
    """
    degree = 3

    def directional(outer_parameter, direction_parameter):
        result = [zeros(len(fields), 6) for _ in range(degree+1)]
        dalpha = [direction_parameter[b+1] - direction_parameter[b]
                  for b in range(len(alpha))]
        dual_alpha = [Dual(a, da) for a, da in zip(alpha, dalpha)]
        evaluation = generator(fields, dual_alpha, outer_parameter,
                               acoef, ecoef, degree, adjusted)
        for power in range(degree+1):
            result[power] = [[tangent(entry) for entry in row]
                             for row in evaluation[power]]
        field_tangent = generator(fields, alpha, direction_parameter,
                                  acoef, ecoef, degree, adjusted)
        for offset in range(1, degree+1):
            dual_fields = [[Dual(entry, delta) for entry, delta in zip(row, drow)]
                           for row, drow in zip(fields, field_tangent[offset])]
            evaluation = generator(dual_fields, alpha, outer_parameter,
                                   acoef, ecoef, degree-offset, adjusted)
            for power in range(degree-offset+1):
                derivative = [[tangent(entry) for entry in row]
                              for row in evaluation[power]]
                result[power+offset] = plus(result[power+offset], derivative)
        return result

    delta_first_second = directional(second, first)
    delta_second_first = directional(first, second)
    return [plus(left, scale(right, -1))
            for left, right in zip(delta_first_second, delta_second_first)]


def run():
    root = Path(__file__).resolve().parents[2]
    for filename, byte_count, digest in AUTHORITY:
        try:
            data = (root / "canon" / filename).read_bytes()
        except OSError as error:
            raise Failure("F_AUTHORITY") from error
        need(len(data) == byte_count and sha256(data).hexdigest() == digest,
             "F_AUTHORITY")
    potential, c, d, k, m, j, metric, uniform, pivots = geometry()
    relative, ecoef, acoef, pairs = completion(k, m, j, metric, d)
    payload = ["P|" + csv(pivots)]
    for label, coefficients in (("R", relative), ("E", ecoef), ("A", acoef)):
        for power, matrix in enumerate(coefficients):
            payload.append(label + "|" + str(power) + "|" + csv(flatten(matrix)))
    controls = [False] * 8
    states = bonds = parameter_cases = integer_cases = 0
    c2, c3 = times(c, c), times(times(c, c), c)
    for horizon in (3, 4, 5):
        for seed in (1, 2):
            fields = [[fixture(seed, n, r) for r in range(6)]
                      for n in range(horizon+1)]
            alpha = [fixture(seed, b, 6) for b in range(1, horizon+1)]
            action = action_series(fields, alpha, potential, acoef, ecoef)
            autonomous = sum(inner(vminus(fields[b], fields[b-1]),
                                   vminus(fields[b], fields[b-1])) / 2
                             for b in range(1, horizon+1))
            autonomous -= sum(quadratic(fields[n], potential)/2
                              for n in range(1, horizon))
            need(action[0] == autonomous, "F_JET")
            for b in range(1, horizon+1):
                q, capital_q = fields[b-1:b+1]
                computed = unscaled_action(q, capital_q, acoef, ecoef)
                fzero = (quadratic(q, c) + quadratic(capital_q, c))/2
                fzero -= inner(q, capital_q)
                hbond = (inner(q, q) + inner(capital_q, capital_q))/2
                hbond -= quadratic(q, c, capital_q)
                kbond = inner(vminus(apply(c, capital_q), q),
                              vminus(capital_q, apply(c, q)))
                tbond = -quadratic(q, plus(eye(6), scale(c2, 2)))
                tbond -= quadratic(capital_q, plus(eye(6), scale(c2, 2)))
                tbond += quadratic(q, plus(scale(c, 5), c3), capital_q)
                need(computed[:4] == [fzero, -hbond, kbond/2, tbond/6], "F_JET")
                bonds += 1
            payload.append("S|%s|%s|%s" % (horizon, seed, csv(action)))
            parameters = []
            for n in range(1, horizon):
                parameter = [Q(0)] * (horizon+1)
                parameter[n] = Q(1)
                parameters.append(parameter)
            parameters.append([Q(0)] + [fixture(seed+2, n, 7)
                                        for n in range(1, horizon)] + [Q(0)])
            gradients = gradient_series(fields, alpha, acoef, ecoef)
            for index, parameter in enumerate(parameters):
                dual_alpha = [Dual(alpha[b], parameter[b+1] - parameter[b])
                              for b in range(horizon)]
                parameter_work = [tangent(entry) for entry in action_series(
                    fields, dual_alpha, potential, acoef, ecoef)]
                raw = generator(fields, alpha, parameter, acoef, ecoef, ORDER, False)
                adjusted = generator(fields, alpha, parameter, acoef, ecoef,
                                     ORDER, True)
                jet_check(fields, alpha, parameter, c, acoef, ecoef, raw, adjusted)
                raw_work = [field_work(gradients, raw, degree)
                            for degree in range(ORDER+1)]
                adjusted_work = [field_work(gradients, adjusted, degree)
                                 for degree in range(ORDER+1)]
                skew = [plus(adjusted[p], scale(raw[p], -1))
                        for p in range(ORDER+1)]
                for degree in range(ORDER+1):
                    need(parameter_work[degree] + raw_work[degree] == 0,
                         "F_WARD")
                    need(parameter_work[degree] + adjusted_work[degree] == 0,
                         "F_WARD")
                    need(field_work(gradients, skew, degree) == 0, "F_WARD")
                    if degree:
                        terms = [parameter_work[degree], raw_work[degree],
                                 adjusted_work[degree]]
                        common = lcm(*(term.denominator for term in terms))
                        integral = [term * common for term in terms]
                        need(all(term.denominator == 1 for term in integral)
                             and integral[0] + integral[1] == 0
                             and integral[0] + integral[2] == 0, "F_INTEGER")
                        integer_cases += 1
                for omitted in (2, 3):
                    broken_parameter_work = list(parameter_work)
                    broken_parameter_work[omitted] = Q(0)
                    broken_gradient = list(gradients)
                    broken_gradient[omitted] = zeros(horizon+1, 6)
                    residual = (broken_parameter_work[omitted]
                                + field_work(broken_gradient, adjusted, omitted))
                    controls[omitted-2] |= residual != 0
                payload.append("W|%s|%s|%s|%s|%s|%s" % (
                    horizon, seed, index, csv(parameter_work), csv(raw_work),
                    csv(adjusted_work)))
                parameter_cases += 1
            states += 1
    mixed_count = 0
    fields = [[fixture(1, n, r) for r in range(6)] for n in range(6)]
    absent = action_series(fields, [Q(0)]*5, potential, acoef, ecoef)
    unit_actions = []
    for b in range(5):
        unit_actions.append(action_series(fields, [Q(i == b) for i in range(5)],
                                          potential, acoef, ecoef))
    for first in range(5):
        for second in range(first+1, 5):
            combined = action_series(fields, [Q(i in (first, second))
                                               for i in range(5)],
                                     potential, acoef, ecoef)
            for degree in range(2, ORDER+1):
                mixed = (combined[degree] - unit_actions[first][degree]
                         - unit_actions[second][degree] + absent[degree])
                need(mixed == 0, "F_LOCALITY")
                payload.append("L|%s|%s|%s|%s" % (first, second, degree, mixed))
                mixed_count += 1
    wrong = [row[:] for row in k]
    for row in range(6, 12):
        for col in range(6):
            wrong[row][col] = -wrong[row][col]
    controls[2] = plus(times(transpose(wrong), metric), times(metric, wrong)) != zeros(12)
    cayleys = {}
    cayley_count = 0
    cd = times(c, d)
    for parameter in (Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2)):
        rc, mc = cayley(parameter, k, m)
        cayleys[parameter] = rc, mc
        need(times(times(transpose(rc), j), rc) == j, "F_RATIONAL")
        need(times(times(transpose(rc), metric), rc) == metric, "F_RATIONAL")
        need(times(rc, cayley(-parameter, k, m)[0]) == eye(12), "F_RATIONAL")
        need(times(rc, m) == times(m, rc), "F_RATIONAL")
        denominator = plus(eye(6), scale(d, parameter**2/4))
        numerator = plus(plus(eye(6), scale(c, parameter)),
                         scale(d, -parameter**2/4))
        upper_numerator = plus(plus(c, scale(d, -parameter)),
                               scale(cd, -parameter**2/4))
        expected_b = times(numerator, inverse(denominator))
        expected_u = times(upper_numerator, inverse(denominator))
        need([row[6:] for row in mc[:6]] == expected_b, "F_RATIONAL")
        need([row[:6] for row in mc[:6]] == expected_u, "F_RATIONAL")
        actual_a, actual_e = cayley_coefficients(parameter, k, m)
        need(actual_e == times(denominator, inverse(numerator)), "F_RATIONAL")
        need(actual_a == times(upper_numerator, inverse(numerator)), "F_RATIONAL")
        payload.append("C|%s|%s|%s" % (parameter, csv(flatten(rc)), csv(flatten(mc))))
        cayley_count += 1
    cr = [eye(12), k]
    for degree in range(2, ORDER+1):
        cr.append(scale(times(k, cr[-1]), Q(1, 2)))
    cm = [times(m, term) for term in cr]
    cu = [[row[:6] for row in term[:6]] for term in cm]
    cb = [[row[6:] for row in term[:6]] for term in cm]
    ce = series_inverse(cb)
    ca = [coefficient_product(ce, cu, degree) for degree in range(ORDER+1)]
    need(ce[:3] == ecoef[:3] and ca[:3] == acoef[:3], "F_RATIONAL")
    composition = times(cayleys[Q(1)][0], cayleys[Q(1)][0])
    controls[3] = composition != cayleys[Q(2)][0]
    need(controls[3], "F_RATIONAL")
    free_p = [Q(0)]*6 + uniform
    # The q increment is exactly twice v, forcing candidate parameter 2.
    need(apply(composition, free_p) == vscale(uniform, 2) + uniform,
         "F_RATIONAL")
    need(apply(cayleys[Q(2)][0], free_p) == vscale(uniform, 2) + uniform,
         "F_RATIONAL")
    chi = [Q(0)]*5 + [Q(1)]
    z1 = [Q(0)]*6 + chi
    z0 = apply(inverse(cayleys[Q(1)][1]), z1)
    z2, z3 = apply(m, z1), apply(m, apply(m, z1))
    stationary_fields = [state[:6] for state in (z0, z1, z2, z3)]
    cayley_gradient = zeros(4, 6)
    cayley_derivative = Q(0)
    for b, (parameter, direction) in enumerate(((1, 1), (0, -1), (0, 0))):
        a, e = cayley_coefficients(Dual(parameter, direction), k, m)
        q, capital_q = stationary_fields[b:b+2]
        expression = (quadratic(q, a) + quadratic(capital_q, a))/2
        expression -= quadratic(q, e, capital_q)
        cayley_derivative += tangent(expression)
        a_value = [[value(entry) for entry in row] for row in a]
        e_value = [[value(entry) for entry in row] for row in e]
        if b > 0:
            cayley_gradient[b] = vplus(cayley_gradient[b],
                                      vminus(apply(a_value, q),
                                             apply(e_value, capital_q)))
        if b+1 < 3:
            cayley_gradient[b+1] = vplus(cayley_gradient[b+1],
                                        vminus(apply(a_value, capital_q),
                                               apply(e_value, q)))
    prediction = (1 - quadratic(chi, inverse(plus(eye(6), scale(d, Q(1, 4))))))/2
    need(cayley_gradient == zeros(4, 6), "F_STATIONARY")
    need(cayley_derivative == prediction and cayley_derivative > 0, "F_RATIONAL")
    controls[4] = cayley_derivative != 0
    payload.append("CW|" + str(cayley_derivative))
    u = [Q(1), Q(0), Q(-1), Q(0), Q(0), Q(0)]
    state = [Q(0)]*6 + u
    initial_energy = quadratic(state, metric)/2
    energy_states = 0
    for n in range(9):
        energy = quadratic(state, metric)/2
        need(energy == 1, "F_STATIONARY")
        payload.append("EN|%s|%s|%s" % (n, csv(state), energy))
        state = apply(m, state)
        energy_states += 1
    static = uniform + [Q(0)]*6
    need(apply(m, static) == static and apply(k, static) == [0]*12,
         "F_STATIONARY")
    minus_transfer = cayley(Q(-1), k, m)[1]
    need(apply([row[6:] for row in minus_transfer[:6]], uniform) == [0]*6,
         "F_STATIONARY")
    need(apply(times(k, k), free_p) == [0]*12, "F_STATIONARY")
    need(apply(times(m, relative[0]), free_p)[:6] == uniform,
         "F_STATIONARY")
    need(apply(times(m, relative[1]), free_p)[:6] == uniform,
         "F_STATIONARY")
    need(all(apply(times(m, relative[degree]), free_p) == [0]*12
             for degree in range(2, ORDER+1)), "F_STATIONARY")
    witness_fields = zeros(5, 6)
    witness_fields[3] = u
    witness_alpha = [Q(0), Q(0), Q(1), Q(0)]
    first, second = [Q(0), Q(1), Q(0), Q(0), Q(0)], [Q(0), Q(0), Q(1), Q(0), Q(0)]
    raw_bracket = actual_bracket(witness_fields, witness_alpha, first, second,
                                 acoef, ecoef, False)
    adjusted_bracket = actual_bracket(witness_fields, witness_alpha, first, second,
                                      acoef, ecoef, True)
    raw_two, raw_three, adjusted_three = (zeros(5, 6) for _ in range(3))
    raw_two[1] = vscale(u, Q(-1, 4))
    raw_three[1] = vscale(apply(c, u), Q(1, 4))
    adjusted_three[1] = vscale(apply(c, u), Q(-1, 8))
    cubic = [Q(-395, 5184), Q(0), Q(395, 5184), Q(-1, 144), Q(1, 144), Q(-1, 5184)]
    need(adjusted_three[1] == cubic, "F_BRACKET")
    need(raw_bracket[2] == raw_two and raw_bracket[3] == raw_three,
         "F_BRACKET")
    need(adjusted_bracket[2] == zeros(5, 6)
         and adjusted_bracket[3] == adjusted_three, "F_BRACKET")
    for label, array in (("RAW2", raw_bracket[2]), ("ADJUSTED2", adjusted_bracket[2]),
                         ("RAW3", raw_bracket[3]), ("ADJUSTED3", adjusted_bracket[3])):
        payload.append("B|" + label + "|" + csv(flatten(array)))
    controls[5] = raw_bracket[2] != zeros(5, 6)
    controls[6] = adjusted_bracket[3] != zeros(5, 6)
    # Actual s derivative of the prepared E=1 initial bond at s=0.
    prepared_q = [Q(0)]*6
    prepared_Q = apply(m, prepared_q + u)[:6]
    lapse_constraint = unscaled_action(prepared_q, prepared_Q, acoef, ecoef)[1]
    controls[7] = (initial_energy == 1 and lapse_constraint == -initial_energy
                   and lapse_constraint == -1 and lapse_constraint + 1 == 0)
    for index, detected in enumerate(controls, 1):
        need(detected, "F_CONTROL")
        payload.append("N|NC%02d|DETECTED" % index)
    need((len(AUTHORITY), ORDER, len(relative), pairs, len(pivots), states,
          bonds, parameter_cases, integer_cases, mixed_count, cayley_count,
          energy_states, len(controls)) == (5, 6, 7, 28, 5, 6, 24, 24, 144,
                                           50, 5, 9, 8), "F_COUNTS")
    digest = sha256(("\n".join(payload) + "\n").encode("ascii")).hexdigest()
    certificate = [
        "CERTIFICATE=" + NAME,
        "AUTHORITY_FILES=5",
        "SERIES_ORDER=6",
        "SERIES_COEFFICIENTS=7",
        "COMPOSITION_PAIRS=28",
        "POSITIVE_PIVOTS=5",
        "OFF_SHELL_STATES=6",
        "BOND_JETS=24",
        "WARD_PARAMETER_CASES=24",
        "INTEGER_WARD_COEFFICIENTS=144",
        "MIXED_LAPSE_COEFFICIENTS=50",
        "CAYLEY_PARAMETERS=5",
        "POSITIVE_ENERGY_STATES=9",
        "COMMUTATOR_WITNESSES=1",
        "CUBIC_ADJUSTED_WITNESS=" + csv(adjusted_bracket[3][1]),
        "PAYLOAD_SHA256=" + digest,
        "NEGATIVE_CONTROLS=8",
        "CERTIFICATE_RESULT=PASS",
    ]
    print("\n".join(certificate))


if __name__ == "__main__":
    try:
        run()
    except Failure as failure:
        print(str(failure))
        print("RESULT=FAIL")
