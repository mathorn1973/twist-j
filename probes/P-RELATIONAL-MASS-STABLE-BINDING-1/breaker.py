#!/usr/bin/env python3
"""Independent integer-pair/Picard audit of the prospective binding carrier.

Only the fixed authority bytes are read.  All payload values are calculated
in memory.  This implementation has no scientific imports or subprocesses.
"""

from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path


class AuditFailure(Exception):
    pass


def require(condition, code):
    if not condition:
        raise AuditFailure(code)


class Rational:
    """A reduced integer pair with a positive denominator."""

    __slots__ = ("n", "d")

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, Rational):
            numerator, denominator = numerator.n, numerator.d * denominator
        if denominator == 0:
            raise ZeroDivisionError("zero rational denominator")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        common = gcd(numerator, denominator)
        self.n = numerator // common
        self.d = denominator // common

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        if not self.n:
            return other
        if not other.n:
            return self
        common = gcd(self.d, other.d)
        return Rational(self.n * (other.d // common)
                        + other.n * (self.d // common),
                        self.d * (other.d // common))

    __radd__ = __add__

    def __neg__(self):
        return Rational(-self.n, self.d)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        if not self.n or not other.n:
            return Rational(0)
        first = gcd(abs(self.n), other.d)
        second = gcd(abs(other.n), self.d)
        return Rational((self.n // first) * (other.n // second),
                        (self.d // second) * (other.d // first))

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        return self * Rational(other.d, other.n)

    def __rtruediv__(self, other):
        return Rational(other) / self

    def __pow__(self, power):
        if not isinstance(power, int):
            return NotImplemented
        if power < 0:
            return Rational(self.d, self.n) ** (-power)
        return Rational(self.n ** power, self.d ** power)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.n == other * self.d
        if isinstance(other, Rational):
            return self.n == other.n and self.d == other.d
        return NotImplemented

    def __lt__(self, other):
        other = Rational(other)
        return self.n * other.d < other.n * self.d

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __bool__(self):
        return self.n != 0

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return str(self.n) + "/" + str(self.d)


class Jet:
    """Ordinary (not factorial-scaled) finite power-series coefficients."""

    __slots__ = ("a", "order")

    def __init__(self, coefficients):
        self.a = tuple(x if isinstance(x, Rational) else Rational(x)
                       for x in coefficients)
        self.order = len(self.a) - 1

    @classmethod
    def constant(cls, value, order):
        return cls([value] + [0] * order)

    def lift(self, other):
        if isinstance(other, Jet):
            if self.order != other.order:
                raise ValueError("unequal series orders")
            return other
        return Jet.constant(other, self.order)

    def __add__(self, other):
        other = self.lift(other)
        return Jet([x + y for x, y in zip(self.a, other.a)])

    __radd__ = __add__

    def __neg__(self):
        return Jet([-x for x in self.a])

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = self.lift(other)
        result = [Rational(0) for _ in self.a]
        for i, x in enumerate(self.a):
            if not x:
                continue
            for j, y in enumerate(other.a[:self.order + 1 - i]):
                if y:
                    result[i + j] = result[i + j] + x * y
        return Jet(result)

    __rmul__ = __mul__

    def inverse(self):
        values = [1 / self.a[0]]
        for n in range(1, self.order + 1):
            values.append(-sum(self.a[k] * values[n - k]
                               for k in range(1, n + 1)) / self.a[0])
        return Jet(values)

    def __truediv__(self, other):
        if isinstance(other, Jet):
            return self * other.inverse()
        return Jet([x / other for x in self.a])

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __eq__(self, other):
        if isinstance(other, (int, Rational)):
            other = self.lift(other)
        if not isinstance(other, Jet):
            return NotImplemented
        return self.a == other.a

    def truncate(self, order):
        return Jet(self.a[:order + 1])

    def derivative(self):
        return Jet([n * self.a[n] for n in range(1, self.order + 1)])

    def root(self, positive_constant):
        root0 = Rational(positive_constant)
        require(root0 > 0 and root0 * root0 == self.a[0], "F02_GEOMETRY")
        roots = [root0]
        for n in range(1, self.order + 1):
            residual = self.a[n] - sum(roots[i] * roots[n - i]
                                       for i in range(1, n))
            roots.append(residual / (2 * root0))
        return Jet(roots)


def transpose(matrix):
    return [[matrix[j][i] for j in range(2)] for i in range(2)]


def madd(left, right):
    return [[left[i][j] + right[i][j] for j in range(2)] for i in range(2)]


def mscale(matrix, scalar):
    return [[entry * scalar for entry in row] for row in matrix]


def mmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def mvec(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2)]


def vscale(vector, scalar):
    return [x * scalar for x in vector]


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


def outer(left, right):
    return [[x * y for y in right] for x in left]


def trace(matrix):
    return matrix[0][0] + matrix[1][1]


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def scalar_inverse(matrix):
    """Gauss-Jordan initial inverse, separate from the series recurrence."""
    rows = [[Rational(matrix[i][j]) for j in range(2)]
            + [Rational(int(i == j)) for j in range(2)] for i in range(2)]
    for col in range(2):
        pivot = next((i for i in range(col, 2) if rows[i][col]), None)
        require(pivot is not None, "F02_GEOMETRY")
        rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [entry / divisor for entry in rows[col]]
        for i in range(2):
            if i != col:
                multiple = rows[i][col]
                rows[i] = [x - multiple * y for x, y in zip(rows[i], rows[col])]
    return [row[2:] for row in rows]


def matrix_coefficient(matrix, index):
    return [[entry.a[index] for entry in row] for row in matrix]


def matrix_inverse(matrix):
    """R_n = -R_0 sum_{j=1}^n G_j R_{n-j}, at every declared order."""
    degree = matrix[0][0].order
    coefficients = [matrix_coefficient(matrix, n) for n in range(degree + 1)]
    values = [scalar_inverse(coefficients[0])]
    for n in range(1, degree + 1):
        convolution = [[Rational(0), Rational(0)], [Rational(0), Rational(0)]]
        for j in range(1, n + 1):
            convolution = madd(convolution, mmul(coefficients[j], values[n - j]))
        values.append(mscale(mmul(values[0], convolution), -1))
    return [[Jet([values[n][i][j] for n in range(degree + 1)])
             for j in range(2)] for i in range(2)]


def constant_matrix(matrix, order):
    return [[Jet.constant(entry, order) for entry in row] for row in matrix]


def constant_state(g, p, r, rho, order):
    return (constant_matrix(g, order), constant_matrix(p, order),
            [Jet.constant(x, order) for x in r],
            [Jet.constant(x, order) for x in rho])


def map_state(state, function):
    g, p, r, rho = state
    return ([[function(x) for x in row] for row in g],
            [[function(x) for x in row] for row in p],
            [function(x) for x in r], [function(x) for x in rho])


def flat_state(state):
    g, p, r, rho = state
    return [x for row in g for x in row] + [x for row in p for x in row] + r + rho


def equal_state(left, right):
    return flat_state(left) == flat_state(right)


def rhs(state, kappa, root0):
    g, p, r, rho = state
    inverse = matrix_inverse(g)
    energy = dot(rho, mvec(g, rho)).root(root0)
    radius_dual = mvec(inverse, r)
    gdot = mmul(mmul(g, p), g)
    pdot = madd(mscale(mmul(mmul(p, g), p), -1),
                madd(mscale(outer(rho, rho), -1 / (2 * energy)),
                     mscale(outer(radius_dual, radius_dual), kappa)))
    rdot = vscale(mvec(g, rho), 1 / energy)
    rhodot = vscale(radius_dual, -2 * kappa)
    return gdot, pdot, rdot, rhodot


def picard(initial, kappa, root0):
    """Exactly four complete formal integral iterations from the constant germ."""
    current = map_state(initial, lambda x: Jet.constant(x.a[0], 4))
    for _ in range(4):
        velocity = rhs(map_state(current, lambda x: x.truncate(3)), kappa, root0)
        primitives = map_state(velocity, lambda x: Jet([0] + [
            x.a[n] / (n + 1) for n in range(4)]))
        pg, pp, pr, pq = primitives
        current = ([[pg[i][j] + initial[0][i][j].a[0] for j in range(2)]
                    for i in range(2)],
                   [[pp[i][j] + initial[1][i][j].a[0] for j in range(2)]
                    for i in range(2)],
                   [pr[i] + initial[2][i].a[0] for i in range(2)],
                   [pq[i] + initial[3][i].a[0] for i in range(2)])
    return current


def evaluate(state, kappa, root0):
    g, p, r, rho = state
    inverse = matrix_inverse(g)
    gp = mmul(g, p)
    squared_energy = dot(rho, mvec(g, rho))
    energy = squared_energy.root(root0)
    radius_squared = dot(r, mvec(inverse, r))
    kinetic = trace(mmul(gp, gp)) / 2
    potential = kappa * radius_squared
    charge = madd(mscale(gp, 2), outer(r, rho))
    c = trace(gp)
    z = dot(r, rho)
    delta = determinant(charge) - trace(charge) * trace(charge) / 4
    gap = energy * energy * potential - 4 * kappa * delta
    return {"G": g, "Pi": p, "r": r, "rho": rho, "R": inverse,
            "K": kinetic, "E": energy, "V": potential,
            "H": kinetic + energy + potential, "D": squared_energy,
            "d2": 4 * radius_squared, "C": c, "z": z, "J": charge,
            "delta": delta, "gap": gap,
            "A": dot(rho, mvec(mmul(mmul(g, p), g), rho)) / (2 * energy),
            "B": kappa * dot(r, mvec(p, r)), "W": 2 * kappa * z / energy}


def constant_jet(series):
    return all(x == 0 for x in series.a[1:])


def audit_trajectory(state, initial, kappa, root0):
    g, p, r, rho = state
    for matrix in (g, p):
        require(matrix == transpose(matrix), "F02_GEOMETRY")
    require(equal_state(map_state(state, lambda x: x.truncate(0)),
                        map_state(initial, lambda x: x.truncate(0))), "F02_GEOMETRY")
    g0 = matrix_coefficient(g, 0)
    require(g0[0][0] > 0 and determinant(g0) > 0, "F02_GEOMETRY")
    require(any(x.a[0] != 0 for x in rho), "F02_GEOMETRY")
    result = evaluate(state, kappa, root0)
    identity = constant_matrix([[1, 0], [0, 1]], 4)
    require(result["R"] == transpose(result["R"]), "F02_GEOMETRY")
    require(mmul(g, result["R"]) == identity
            and mmul(result["R"], g) == identity, "F02_GEOMETRY")
    require(result["E"] * result["E"] == result["D"], "F02_GEOMETRY")
    velocity = rhs(map_state(state, lambda x: x.truncate(3)), kappa, root0)
    require(equal_state(map_state(state, lambda x: x.derivative()), velocity), "F03_FLOW")
    require(constant_jet(result["H"]), "F04_EXCHANGE")
    for equation in (("E", result["A"] - result["W"]),
                     ("V", result["W"] - result["B"]),
                     ("K", -result["A"] + result["B"]),
                     ("C", -result["E"] / 2 + result["V"]),
                     ("z", result["E"] - 2 * result["V"])):
        require(result[equation[0]].derivative() == equation[1].truncate(3),
                "F04_EXCHANGE")
    require(all(constant_jet(x) for row in result["J"] for x in row)
            and constant_jet(result["delta"]), "F05_CHARGE")
    require(trace(result["J"]) == 2 * result["C"] + result["z"], "F05_CHARGE")
    require(result["d2"] == 4 * result["V"] / kappa, "F06_BOUND")
    charge = result["J"]
    q = trace(mmul(mmul(mmul(result["R"], charge), g), transpose(charge)))
    gap_identity = kappa * (result["z"] * result["z"]
                           + trace(mmul(charge, charge)) + q
                           - trace(charge) * trace(charge))
    require(result["gap"] == gap_identity and result["gap"].a[0] >= 0, "F06_BOUND")
    delta0, h0, e0, d20 = (result[key].a[0] for key in ("delta", "H", "E", "d2"))
    require(result["K"].a[0] >= 0 and result["V"].a[0] >= 0
            and e0 > 0 and h0 > 0, "F06_BOUND")
    if delta0 > 0:
        require(e0 * e0 * h0 >= 4 * kappa * delta0
                and d20 * h0 * h0 >= 16 * delta0
                and d20 <= 4 * h0 / kappa and e0 > 0, "F06_BOUND")
    return result


def initial_direction(state, direction):
    initial = map_state(state, lambda x: Jet([x.a[0], 0]))
    g, p, r, rho = initial
    family, i, j = direction
    if family in (0, 1):
        matrix = (g, p)[family]
        matrix[i][j] = Jet([matrix[i][j].a[0], 1])
        if i != j:
            matrix[j][i] = Jet([matrix[j][i].a[0], 1])
    else:
        vector = (r, rho)[family - 2]
        vector[i] = Jet([vector[i].a[0], 1])
    return initial


def audit_gradients(state, kappa, root0):
    velocity = rhs(map_state(state, lambda x: x.truncate(0)), kappa, root0)
    for family in range(4):
        indices = ((0, 0), (1, 1), (0, 1)) if family < 2 else ((0, 0), (1, 0))
        for i, j in indices:
            perturbed = initial_direction(state, (family, i, j))
            actual = evaluate(perturbed, kappa, root0)["H"].a[1]
            if family == 0:
                expected = -velocity[1][i][j].a[0] * (1 if i == j else 2)
            elif family == 1:
                expected = velocity[0][i][j].a[0] * (1 if i == j else 2)
            elif family == 2:
                expected = -velocity[3][i].a[0]
            else:
                expected = velocity[2][i].a[0]
            require(actual == expected, "F03_FLOW")


def transformed(state, matrix):
    degree = state[0][0][0].order
    a = constant_matrix(matrix, degree)
    inverse = constant_matrix(scalar_inverse(matrix), degree)
    g, p, r, rho = state
    return (mmul(mmul(a, g), transpose(a)),
            mmul(mmul(transpose(inverse), p), inverse),
            mvec(a, r), mvec(transpose(inverse), rho))


def numbers(values):
    return ",".join(str(value) for value in values)


def matrix_numbers(matrix):
    return numbers([entry for row in matrix for entry in row])


def fields(result, index):
    output = []
    for key in ("G", "Pi", "r", "rho", "K", "E", "V", "D", "d2", "C", "J", "delta", "gap"):
        value = result[key]
        if key in ("G", "Pi", "J"):
            output.append(numbers([entry.a[index] for row in value for entry in row]))
        elif key in ("r", "rho"):
            output.append(numbers([entry.a[index] for entry in value]))
        else:
            output.append(str(value.a[index]))
    require(len(output) == 13, "F11_PAYLOAD")
    return "|".join(output)


def exact_positive_root(value, code):
    value = Rational(value)
    require(value >= 0, code)
    numerator, denominator = isqrt(value.n), isqrt(value.d)
    require(numerator * numerator == value.n and denominator * denominator == value.d, code)
    return Rational(numerator, denominator)


def group_exponential(generator, sign, degree):
    matrices = [[[Rational(int(i == j)) for j in range(2)] for i in range(2)]]
    for n in range(1, degree + 1):
        matrices.append(mscale(mmul(matrices[-1], generator), Rational(sign, n)))
    return [[Jet([matrices[n][i][j] for n in range(degree + 1)])
             for j in range(2)] for i in range(2)]


def tangent_values(initial, velocity, kappa, root0):
    g, p, r, rho = initial
    dg, dp, dr, dq = velocity
    germ = ([[Jet([g[i][j].a[0], dg[i][j].a[0]]) for j in range(2)] for i in range(2)],
            [[Jet([p[i][j].a[0], dp[i][j].a[0]]) for j in range(2)] for i in range(2)],
            [Jet([r[i].a[0], dr[i].a[0]]) for i in range(2)],
            [Jet([rho[i].a[0], dq[i].a[0]]) for i in range(2)])
    return evaluate(germ, kappa, root0)


def authority():
    records = (
        ("canon/CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
        ("canon/CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
        ("canon/FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
        ("canon/REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
        ("canon/CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
    )
    root = Path(__file__).resolve().parents[2]
    for path, size, digest in records:
        try:
            data = (root / path).read_bytes()
        except OSError:
            raise AuditFailure("F01_AUTHORITY") from None
        require(len(data) == size and sha256(data).hexdigest() == digest, "F01_AUTHORITY")
    return len(records)


def certificate():
    authority_count = authority()
    order = 4
    one = [[Rational(1), Rational(0)], [Rational(0), Rational(1)]]
    half = Rational(1, 2)
    zero = [[Rational(0), Rational(0)], [Rational(0), Rational(0)]]
    momenta = [zero, [[0, -half], [-half, 0]], [[0, half], [half, 0]],
               [[half, -half], [-half, 0]], [[0, -half], [-half, -half]],
               [[half, -1], [-1, -half]], [[-half, 1], [1, half]]]
    momenta = [[[Rational(x) for x in row] for row in matrix] for matrix in momenta]
    covectors = [(0, 1), (0, 2), (0, -2), (3, 4), (3, -4)]
    roots = [Rational(x) for x in (1, 2, 2, 5, 5)]
    positions = [(1, 0), (2, 0)]
    couplings = [half, Rational(1), Rational(2)]
    payload = ["G|" + matrix_numbers(one)]
    for bi, matrix in enumerate(momenta):
        payload.append("B|" + str(bi) + "|" + matrix_numbers(matrix))
    for qi, (rho, e0) in enumerate(zip(covectors, roots)):
        payload.append("Q|" + str(qi) + "|" + numbers(rho) + "|" + str(e0))
    for ri, r in enumerate(positions):
        payload.append("R|" + str(ri) + "|" + numbers(r))
    for ki, kappa in enumerate(couplings):
        payload.append("K|" + str(ki) + "|" + str(kappa))
    require(len(payload) == 18, "F11_PAYLOAD")
    counts = {"POS": 0, "ZERO": 0, "NEG": 0}
    bases = {}
    base_indices = ((1, 0, 1, 1), (2, 1, 2, 6))
    trajectory_count = coefficient_count = 0
    for ki, kappa in enumerate(couplings):
        for ri, r in enumerate(positions):
            for qi, (rho, root0) in enumerate(zip(covectors, roots)):
                for bi, p in enumerate(momenta):
                    key = (ki, ri, qi, bi)
                    initial = constant_state(one, p, r, rho, order)
                    state = picard(initial, kappa, root0)
                    result = audit_trajectory(state, initial, kappa, root0)
                    audit_gradients(initial, kappa, root0)
                    delta0 = result["delta"].a[0]
                    category = "POS" if delta0 > 0 else "NEG" if delta0 < 0 else "ZERO"
                    counts[category] += 1
                    trajectory_count += 1
                    prefix = "|".join(str(x) for x in key)
                    payload.append("C|" + prefix + "|" + str(kappa) + "|" + str(delta0) + "|" + category)
                    for m in range(order + 1):
                        payload.append("S|" + prefix + "|" + str(m) + "|" + fields(result, m))
                        coefficient_count += 1
                    if key in base_indices:
                        bases[key] = (state, result, kappa, root0)
    require(trajectory_count == 210 and sum(counts.values()) == trajectory_count
            and all(value > 0 for value in counts.values()), "F11_PAYLOAD")
    require(coefficient_count == 1050, "F11_PAYLOAD")
    transformations = ([[1, 1], [0, 1]], [[0, 1], [1, 0]], [[2, 0], [0, 1]])
    covariance_count = 0
    for key in base_indices:
        state, original, kappa, root0 = bases[key]
        for matrix in transformations:
            changed = transformed(state, matrix)
            initial = map_state(changed, lambda x: Jet.constant(x.a[0], order))
            result = audit_trajectory(changed, initial, kappa, root0)
            for name in ("K", "E", "V", "D", "d2", "C", "delta", "gap"):
                require(result[name] == original[name], "F07_COVARIANCE")
            left = constant_matrix(matrix, order)
            right = constant_matrix(scalar_inverse(matrix), order)
            require(result["J"] == mmul(mmul(left, original["J"]), right), "F07_COVARIANCE")
            payload.append("A|" + str(covariance_count) + "|" + numbers(key) + "|" + matrix_numbers(matrix))
            for m in range(order + 1):
                payload.append("Y|" + str(covariance_count) + "|" + str(m) + "|" + fields(result, m))
            covariance_count += 1
    require(covariance_count == 6, "F11_PAYLOAD")

    kappa = Rational(3)
    periodic_p = [[0, -1], [-1, 0]]
    periodic_initial = constant_state(one, periodic_p, (1, 0), (0, 6), order)
    periodic_state = picard(periodic_initial, kappa, Rational(6))
    periodic = audit_trajectory(periodic_state, periodic_initial, kappa, Rational(6))
    omega = [[Rational(0), Rational(-2)], [Rational(1), Rational(0)]]
    require(mmul(omega, omega) == mscale(one, -2), "F08_PERIODIC")
    exp_plus = group_exponential(omega, 1, order)
    exp_minus = group_exponential(omega, -1, order)
    g, p, r, rho = periodic_initial
    group_state = (mmul(mmul(exp_plus, g), transpose(exp_plus)),
                   mmul(mmul(transpose(exp_minus), p), exp_minus),
                   mvec(exp_plus, r), mvec(transpose(exp_minus), rho))
    require(equal_state(periodic_state, group_state), "F08_PERIODIC")
    base0 = map_state(periodic_initial, lambda x: x.truncate(0))
    g, p, r, rho = base0
    omega0 = constant_matrix(omega, 0)
    generator_velocity = (madd(mmul(omega0, g), mmul(g, transpose(omega0))),
                          mscale(madd(mmul(transpose(omega0), p), mmul(p, omega0)), -1),
                          mvec(omega0, r), vscale(mvec(transpose(omega0), rho), -1))
    require(equal_state(rhs(base0, kappa, Rational(6)), generator_velocity), "F08_PERIODIC")
    for name, expected in (("K", 1), ("E", 6), ("V", 3), ("H", 10),
                           ("D", 36), ("d2", 4), ("C", 0), ("z", 0),
                           ("delta", 8)):
        require(periodic[name] == expected, "F08_PERIODIC")
    jstar = [[Rational(0), Rational(4)], [Rational(-2), Rational(0)]]
    require(periodic["J"] == constant_matrix(jstar, order)
            and omega == mscale(jstar, Rational(-1, 2)), "F08_PERIODIC")
    g, p, r, rho = base0
    r0, rho0 = [x.a[0] for x in r], [x.a[0] for x in rho]
    area = r0[0] * rho0[1] - r0[1] * rho0[0]
    a = (area if area >= 0 else -area) / 2
    delta = periodic["delta"].a[0]
    b = exact_positive_root(a * a - delta, "F09_MINIMUM")
    u = b / a
    c = Rational(1)
    require(a == 3 and b == 1 and u == Rational(1, 3)
            and c ** 3 == kappa / a and b * b == a * a - delta, "F09_MINIMUM")
    require(delta ** 2 * (1 - u) ** 4 == 64 * kappa * u ** 3 * (1 + u) ** 2, "F09_MINIMUM")
    d = a - b
    first = 2 * c - d * d / (2 * b)
    second = -2 * c / (3 * a) + d * d / (b * b) + a * d * d / (2 * b ** 3)
    require(first == 0 and second == Rational(88, 9), "F09_MINIMUM")
    e0, v0 = periodic["E"].a[0], periodic["V"].a[0]
    w = exact_positive_root(dot(r0, r0) * dot(rho0, rho0), "F09_MINIMUM")
    sym_j = mscale(madd(jstar, transpose(jstar)), half)
    rq = outer(r0, rho0)
    sym_rq = mscale(madd(rq, transpose(rq)), half)
    require(dot(r0, rho0) == 0 and dot(r0, r0) == 1 and dot(rho0, rho0) == 36
            and area > 0 and w == 2 * a and sym_j == mscale(sym_rq, Rational(1, 3)), "F09_MINIMUM")
    require((e0 + v0) ** 3 == 27 * kappa * a * a and e0 == 2 * v0
            and periodic["K"].a[0] == (w / 2 - b) ** 2 / 4
            and periodic["H"].a[0] == 3 * c * a + d * d / 4, "F09_MINIMUM")
    payload.append("W|" + str(kappa) + "|" + matrix_numbers(omega) + "|"
                   + "|".join(str(x) for x in (a, b, u, second)))
    for m in range(order + 1):
        payload.append("T|" + str(m) + "|" + fields(periodic, m))
    periodic_count = sum(line.startswith("T|0|") for line in payload)
    require(periodic_count == 1, "F11_PAYLOAD")
    displaced_state = constant_state(one, periodic_p, (2, 0), (0, 3), 0)
    displaced = evaluate(displaced_state, kappa, Rational(3))
    require(displaced["J"] == constant_matrix(jstar, 0)
            and displaced["delta"] == delta and displaced["H"] == 16
            and displaced["H"].a[0] > periodic["H"].a[0], "F09_MINIMUM")
    payload.append("F|RADIAL_DISPLACEMENT|" + fields(displaced, 0))

    detected = []
    nc1 = constant_state(one, zero, (1, 0), (3, 4), 0)
    velocity = rhs(nc1, Rational(1), Rational(5))
    g, p, r, rho = nc1
    radius_dual = mvec(matrix_inverse(g), r)
    omitted_both = (velocity[0], madd(velocity[1], mscale(outer(radius_dual, radius_dual), -1)),
                    velocity[2], [Jet.constant(0, 0), Jet.constant(0, 0)])
    wrong = tangent_values(nc1, omitted_both, Rational(1), Rational(5))
    require(wrong["H"].a[1] == Rational(6, 5) and wrong["H"].a[1] != 0, "F10_NEGATIVE_CONTROL")
    detected.append("NC01")
    rho2 = [Rational(0), Rational(2)]
    pplus, pminus = vscale(rho2, half), vscale(rho2, -half)
    eplus = exact_positive_root(dot(pplus, mvec(one, pplus)), "F10_NEGATIVE_CONTROL")
    eminus = exact_positive_root(dot(pminus, mvec(one, pminus)), "F10_NEGATIVE_CONTROL")
    epair = exact_positive_root(dot(rho2, mvec(one, rho2)), "F10_NEGATIVE_CONTROL")
    require(eplus == 1 and eminus == 1 and epair == 2
            and eplus + eminus == epair and eplus != epair, "F10_NEGATIVE_CONTROL")
    detected.append("NC02")
    base, original, coupling, root0 = bases[base_indices[0]]
    dilation = transformed(base, [[2, 0], [0, 2]])
    dilated = evaluate(dilation, coupling, root0)
    coordinate = 4 * dot(base[2], base[2])
    coordinate_scaled = 4 * dot(dilation[2], dilation[2])
    require(dilated["d2"] == original["d2"] and dilated["H"] == original["H"]
            and coordinate_scaled == 4 * coordinate
            and coordinate_scaled.a[0] != coordinate.a[0], "F10_NEGATIVE_CONTROL")
    detected.append("NC03")
    nc4zero = evaluate(constant_state(one, zero, (1, 0), rho2, 0), Rational(1), Rational(2))
    nc4metric = evaluate(constant_state(one, momenta[1], (1, 0), rho2, 0), Rational(1), Rational(2))
    require(nc4zero["delta"] == 0 and nc4metric["delta"] == 1, "F10_NEGATIVE_CONTROL")
    detected.append("NC04")
    nc5 = constant_state(one, one, (1, 0), rho2, 0)
    nc5values = evaluate(nc5, Rational(1), Rational(2))
    det_j = determinant(nc5values["J"]).a[0]
    require(nc5values["delta"] == 0 and det_j == 4
            and nc5values["E"].a[0] ** 2 * nc5values["V"].a[0] < 4 * det_j, "F10_NEGATIVE_CONTROL")
    detected.append("NC05")
    nc5velocity = rhs(nc5, Rational(1), Rational(2))
    radius_dual = mvec(matrix_inverse(nc5[0]), nc5[2])
    omitted_metric = (nc5velocity[0], madd(nc5velocity[1], mscale(outer(radius_dual, radius_dual), -1)),
                      nc5velocity[2], nc5velocity[3])
    wrong = tangent_values(nc5, omitted_metric, Rational(1), Rational(2))
    require(wrong["H"].a[1] == -1 and wrong["H"].a[1] != 0, "F10_NEGATIVE_CONTROL")
    detected.append("NC06")
    correct = tangent_values(nc1, velocity, Rational(1), Rational(5))
    require(correct["E"].a[1] == Rational(-6, 5) and correct["V"].a[1] == Rational(6, 5)
            and correct["K"].a[1] == 0 and correct["H"].a[1] == 0, "F10_NEGATIVE_CONTROL")
    detected.append("NC07")
    require(displaced["delta"].a[0] == periodic["delta"].a[0] == 8
            and displaced["J"] == constant_matrix(matrix_coefficient(periodic["J"], 0), 0)
            and periodic["H"].a[0] == 10 and displaced["H"].a[0] == 16
            and displaced["H"].a[0] != periodic["H"].a[0], "F10_NEGATIVE_CONTROL")
    detected.append("NC08")
    require(detected == ["NC" + str(i).zfill(2) for i in range(1, 9)], "F11_PAYLOAD")
    payload.extend("N|" + name + "|DETECTED" for name in detected)
    require(len(payload) == 1329, "F11_PAYLOAD")
    payload_bytes = ("\n".join(payload) + "\n").encode("ascii")
    require(payload_bytes.count(b"\n") == len(payload) and b"\r" not in payload_bytes, "F11_PAYLOAD")
    lines = [
        "CERTIFICATE=P-RELATIONAL-MASS-STABLE-BINDING-1",
        "AUTHORITY_FILES=" + str(authority_count),
        "COUPLINGS=" + str(len(couplings)),
        "SEPARATIONS=" + str(len(positions)),
        "MOMENTA=" + str(len(covectors)),
        "METRIC_MOMENTA=" + str(len(momenta)),
        "TRAJECTORY_CASES=" + str(trajectory_count),
        "ELLIPTIC_CASES=" + str(counts["POS"]),
        "PARABOLIC_CASES=" + str(counts["ZERO"]),
        "HYPERBOLIC_CASES=" + str(counts["NEG"]),
        "FORMAL_ORDER=" + str(order),
        "COEFFICIENT_ROWS=" + str(coefficient_count),
        "COVARIANCE_CASES=" + str(covariance_count),
        "PERIODIC_CASES=" + str(periodic_count),
        "NEGATIVE_CONTROLS=" + str(len(detected)),
        "PAYLOAD_RECORDS=" + str(len(payload)),
        "PAYLOAD_SHA256=" + sha256(payload_bytes).hexdigest(),
        "CERTIFICATE_RESULT=PASS",
    ]
    require(len(lines) == 18, "F11_PAYLOAD")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    try:
        print(certificate(), end="")
    except AuditFailure as failure:
        print("FALSIFIER=" + str(failure))
        print("RESULT=FAIL")
