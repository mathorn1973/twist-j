#!/usr/bin/env python3
"""Prospective exact primary audit; execute only after the public freeze.

The scientific path is direct Q(phi) matrix moments and exact binomial
coefficients.  No companion/predecessor source or expected output is read.
The sibling is executed only to compare its complete raw certificate.
"""

from collections import namedtuple
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import subprocess
import sys


PROBE = "P-RELATIONAL-MASS-METRIC-RESPONSE-1"
AUTHORITY = (
    ("canon/CORE.md", "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("canon/CANON.md", "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("canon/FRONTIER.md", "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("canon/REGISTRY.tsv", "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("canon/CHANGELOG.md", "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class ScientificFailure(Exception):
    """Only explicitly declared, completed scientific failures use this type."""


def require(condition, code):
    if not condition:
        raise ScientificFailure(code)


class F:
    """a+b*phi, with phi**2=phi+1; both coefficients are Fractions."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __eq__(self, other):
        if isinstance(other, F):
            return self.a == other.a and self.b == other.b
        if isinstance(other, (int, Fraction)):
            return self.a == other and self.b == 0
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, F):
            return F(self.a + other.a, self.b + other.b)
        return F(self.a + other, self.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, F):
            return F(self.a * other.a + self.b * other.b,
                     self.a * other.b + self.b * other.a + self.b * other.b)
        return F(self.a * other, self.b * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, F):
            denominator = other.a * other.a + other.a * other.b - other.b * other.b
            return self * F((other.a + other.b) / denominator,
                            -other.b / denominator)
        return F(self.a / other, self.b / other)

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("F exponent must be a nonnegative integer")
        value = F(1)
        base = self
        while exponent:
            if exponent & 1:
                value = value * base
            base = base * base
            exponent >>= 1
        return value

    def tau(self):
        return F(self.a + self.b, -self.b)

    def sign(self):
        # 2*(a+b*phi) = x+y*sqrt(5).  Compare rational squares only
        # when the two summands have opposite signs.
        x, y = 2 * self.a + self.b, self.b
        sx = (x > 0) - (x < 0)
        sy = (y > 0) - (y < 0)
        if sx == 0:
            return sy
        if sy == 0 or sx == sy:
            return sx
        difference = x * x - 5 * y * y
        if difference == 0:
            return 0
        return sx if difference > 0 else sy


ZERO, ONE, PHI = F(), F(1), F(0, 1)
GAMMA = PHI - 1


class K:
    """Four rational coefficients modulo 1+j+j**2+j**3+j**4."""

    __slots__ = ("c",)

    def __init__(self, coefficients):
        self.c = tuple(Fraction(value) for value in coefficients)
        if len(self.c) != 4:
            raise ValueError("K needs four coefficients")

    def __eq__(self, other):
        if isinstance(other, K):
            return self.c == other.c
        return NotImplemented

    def __add__(self, other):
        return K(a + b for a, b in zip(self.c, other.c))

    def __neg__(self):
        return K(-a for a in self.c)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, K):
            return K(a * other for a in self.c)
        coefficients = [Fraction(0) for _ in range(7)]
        for i in range(4):
            for j in range(4):
                coefficients[i + j] += self.c[i] * other.c[j]
        for degree in range(6, 3, -1):
            for offset in range(4):
                coefficients[degree - 4 + offset] -= coefficients[degree]
        return K(coefficients[:4])

    __rmul__ = __mul__


KZERO = K((0, 0, 0, 0))
KONE = K((1, 0, 0, 0))
J = K((0, 1, 0, 0))
ROOTS = (KONE, J, K((0, 0, 1, 0)), K((0, 0, 0, 1)),
         K((-1, -1, -1, -1)))


def ksum(values):
    result = KZERO
    for value in values:
        result = result + value
    return result


def conjugate(value):
    return ksum(value.c[k] * ROOTS[(-k) % 5] for k in range(4))


def sigma(value):
    return ksum(value.c[k] * ROOTS[(2 * k) % 5] for k in range(4))


def embed(value):
    return K((value.a, 0, -value.b, -value.b))


def real_field(value):
    require(value.c[1] == 0 and value.c[2] == value.c[3], "F_GEOMETRY")
    return F(value.c[0], -value.c[2])


def real(value):
    return real_field((value + conjugate(value)) * Fraction(1, 2))


def norm(value):
    return real_field(value * conjugate(value))


def coordinates(value):
    c0, c1, c2, c3 = value.c
    return (F(c0 - c2) - c3 * GAMMA,
            F(c1) + (c2 - c3) * GAMMA)


def fsum(values):
    return sum(values, ZERO)


def add_matrix(left, right):
    return tuple(a + b for a, b in zip(left, right))


def subtract_matrix(left, right):
    return tuple(a - b for a, b in zip(left, right))


def scale_matrix(scalar, matrix):
    return tuple(scalar * entry for entry in matrix)


def outer(vector):
    return tuple(vector[i] * vector[j] for i in range(2) for j in range(2))


def matmul(left, right):
    return tuple(fsum(left[2 * i + k] * right[2 * k + j] for k in range(2))
                 for i in range(2) for j in range(2))


def transpose(matrix):
    return (matrix[0], matrix[2], matrix[1], matrix[3])


def matvec(matrix, vector):
    return tuple(fsum(matrix[2 * i + j] * vector[j] for j in range(2))
                 for i in range(2))


def congruence(matrix, tensor):
    return matmul(matmul(matrix, tensor), transpose(matrix))


def pairing(left, right):
    # tr(left*right); the two off-diagonal terms are both included.
    return fsum(left[2 * i + j] * right[2 * j + i]
                for i in range(2) for j in range(2))


def bilinear(left, matrix, right):
    return fsum(left[i] * matrix[2 * i + j] * right[j]
                for i in range(2) for j in range(2))


def quadratic(vector, matrix):
    return bilinear(vector, matrix, vector)


def determinant(matrix):
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def inverse(matrix):
    det = determinant(matrix)
    return tuple(value / det for value in
                 (matrix[3], -matrix[1], -matrix[2], matrix[0]))


def rank2(matrix):
    if all(value == 0 for value in matrix):
        return 0
    return 1 if determinant(matrix) == 0 else 2


def positive_semidefinite(matrix):
    return (matrix[1] == matrix[2] and matrix[0].sign() >= 0
            and matrix[3].sign() >= 0 and determinant(matrix).sign() >= 0)


def negative_semidefinite(matrix):
    return (matrix[1] == matrix[2] and matrix[0].sign() <= 0
            and matrix[3].sign() <= 0 and determinant(matrix).sign() >= 0)


G0 = (ONE, GAMMA / 2, GAMMA / 2, ONE)
U = ((ONE, ZERO), (ZERO, ONE), (-ONE, GAMMA),
     (-GAMMA, -GAMMA), (GAMMA, -ONE))
MOMENTS = tuple(outer(vector) for vector in U)
PAIRS = tuple(combinations(range(5), 2))
PAIR_MATRICES = tuple(outer(tuple(U[r][i] - U[q][i] for i in range(2)))
                      for r, q in PAIRS)
STRAIN_PARAMETERS = ((ONE, KZERO), (ZERO, KONE), (ZERO, J),
                     (ONE, 2 * KONE - J))
DIRECTIONS = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, -1))


def strain(alpha, beta):
    cross = alpha * GAMMA / 2 + real(beta * J)
    return (alpha + real(beta), cross, cross,
            alpha + real(beta * ROOTS[2]))


H = tuple(strain(alpha, beta) for alpha, beta in STRAIN_PARAMETERS)
A = tuple(tuple(quadratic(vector, matrix) for vector in U) for matrix in H)
ADIFF = tuple(tuple(A[s][r] - A[s][q] for s in range(3)) for r, q in PAIRS)
# Only count-independent geometric factors are cached.  Every preparation's
# weighted moments and every series coefficient are still computed below.
A_POWERS = tuple(tuple(tuple(A[s][k] ** m for m in range(5))
                       for k in range(5)) for s in range(4))
A_PRODUCTS = tuple(tuple(A[i][k] * A[j][k] for k in range(5))
                   for i in range(3) for j in range(3))
ADIFF_PRODUCTS = tuple(tuple(ADIFF[t][i] * ADIFF[t][j] for t in range(len(PAIRS)))
                       for i in range(3) for j in range(3))
PAIR_STRAIN_SQUARES = tuple(tuple((A[s][r] - A[s][q]) ** 2 for r, q in PAIRS)
                            for s in range(4))


def binomial_half(order):
    """Exact generalized binomial coefficients, with no square-root call."""
    coefficients = [Fraction(1)]
    for degree in range(1, order + 1):
        coefficients.append(coefficients[-1]
                            * (Fraction(1, 2) - (degree - 1)) / degree)
    return tuple(coefficients)


BINOMIAL = binomial_half(4)
ROOT_SERIES = tuple(tuple(tuple(BINOMIAL[m] * A_POWERS[s][k][m]
                               for m in range(5)) for k in range(5))
                    for s in range(4))
Preparation = namedtuple("Preparation", "N Z W P T R D Q")


def prepare(counts):
    total = sum(counts)
    z = ksum(counts[k] * ROOTS[k] for k in range(5))
    w = ksum(counts[k] * ROOTS[(2 * k) % 5] for k in range(5))
    momentum = tuple(fsum(counts[k] * U[k][i] for k in range(5))
                     for i in range(2))
    energy_tensor = tuple(fsum(counts[k] * MOMENTS[k][i] for k in range(5))
                          for i in range(4))
    response = subtract_matrix(scale_matrix(total, energy_tensor), outer(momentum))
    mass = F(total * total) - norm(z)
    anisotropy = total * w - z * z
    return Preparation(total, z, w, momentum, energy_tensor, response, mass, anisotropy)


def hessian(counts, total):
    first = tuple(fsum(counts[k] * A[i][k] for k in range(5)) for i in range(3))
    return tuple((first[i] * first[j]
                  - total * fsum(counts[k] * A_PRODUCTS[3 * i + j][k] for k in range(5))) / 2
                 for i in range(3) for j in range(3))


def energy_series(counts, strain_index):
    return tuple(fsum(counts[k] * ROOT_SERIES[strain_index][k][m]
                      for k in range(5)) for m in range(5))


def mass_series(preparation, energy, strain_index):
    coefficients = [fsum(energy[i] * energy[m - i] for i in range(m + 1))
                    for m in range(5)]
    coefficients[0] -= quadratic(preparation.P, G0)
    coefficients[1] -= quadratic(preparation.P, H[strain_index])
    return tuple(coefficients)


def ftext(values):
    return ",".join(str(coefficient) for value in values
                    for coefficient in (value.a, value.b))


def ktext(value):
    return ",".join(str(coefficient) for coefficient in value.c)


class Payload:
    def __init__(self):
        self.digest = sha256()
        self.records = 0

    def emit(self, *fields):
        self.digest.update(("|".join(str(field) for field in fields) + "\n").encode("ascii"))
        self.records += 1


def check_authority():
    root = Path(__file__).resolve().parents[2]
    for relative, expected_hash in AUTHORITY:
        path = root / relative
        try:
            actual = path.read_bytes()
        except FileNotFoundError:
            raise ScientificFailure("F_AUTHORITY") from None
        require(sha256(actual).hexdigest() == expected_hash, "F_AUTHORITY")


def check_geometry():
    require(PHI * PHI == PHI + 1 and GAMMA * GAMMA == 2 - PHI, "F_GEOMETRY")
    require(PHI.sign() > 0 and (PHI - 1).sign() > 0
            and (3 - PHI).sign() > 0, "F_GEOMETRY")
    require(ksum(ROOTS) == KZERO and ROOTS[4] * J == KONE, "F_GEOMETRY")
    require(embed(PHI) == -ROOTS[2] - ROOTS[3], "F_GEOMETRY")
    require(sigma(embed(PHI)) == embed(PHI.tau()), "F_GEOMETRY")
    for k in range(5):
        require(embed(U[k][0]) + embed(U[k][1]) * J == ROOTS[k], "F_GEOMETRY")
        require(quadratic(U[k], G0) == 1 and norm(ROOTS[k]) == 1, "F_GEOMETRY")
        require(conjugate(ROOTS[k]) == ROOTS[(-k) % 5], "F_GEOMETRY")
    require(determinant(G0) == (2 + PHI) / 4 and positive_semidefinite(G0), "F_GEOMETRY")
    require(determinant(G0).sign() > 0, "F_GEOMETRY")
    for s, (alpha, beta) in enumerate(STRAIN_PARAMETERS):
        require(H[s][1] == H[s][2], "F_GEOMETRY")
        for k in range(5):
            require(A[s][k] == alpha + real(beta * ROOTS[(2 * k) % 5]), "F_GEOMETRY")
        constant = all(value == A[s][0] for value in A[s])
        require(constant == (H[s] == scale_matrix(A[s][0], G0)), "F_GEOMETRY")
    require(H[0] == G0, "F_GEOMETRY")
    require(H[3] == subtract_matrix(add_matrix(H[0], scale_matrix(2, H[1])), H[2]),
            "F_GEOMETRY")
    # Determinant of the three coordinate columns (H00,H01,H11).
    basis = tuple((matrix[0], matrix[1], matrix[3]) for matrix in H[:3])
    basis_det = (basis[0][0] * (basis[1][1] * basis[2][2] - basis[1][2] * basis[2][1])
                 - basis[1][0] * (basis[0][1] * basis[2][2] - basis[0][2] * basis[2][1])
                 + basis[2][0] * (basis[0][1] * basis[1][2] - basis[0][2] * basis[1][1]))
    require(basis_det != 0, "F_GEOMETRY")
    require(BINOMIAL == (Fraction(1), Fraction(1, 2), Fraction(-1, 8),
                         Fraction(1, 16), Fraction(-5, 128)), "F_GEOMETRY")


def check_preparation(counts, p):
    z_norm, w_norm = norm(p.Z), norm(p.W)
    require(p.W == sigma(p.Z), "F_RESPONSE")
    require(coordinates(p.Z) == p.P and quadratic(p.P, G0) == z_norm, "F_RESPONSE")
    second_momentum = tuple(fsum(counts[k] * U[(2 * k) % 5][i] for k in range(5))
                            for i in range(2))
    require(coordinates(p.W) == second_momentum
            and quadratic(second_momentum, G0) == w_norm, "F_RESPONSE")
    require(w_norm == z_norm.tau()
            and p.D.tau() == F(p.N * p.N) - w_norm, "F_RESPONSE")
    require(all(value.denominator == 1 for value in p.Z.c), "F_FIBER")
    remainder = (Fraction(p.N) - sum(p.Z.c)) / 5
    reconstructed = tuple(value + remainder for value in p.Z.c) + (remainder,)
    require(remainder.denominator == 1 and reconstructed == counts
            and all(value >= 0 for value in reconstructed), "F_FIBER")
    rest = p.Z == KZERO
    require(rest == all(value == counts[0] for value in counts), "F_FIBER")
    require(rest == all(value == 0 for value in p.P), "F_FIBER")
    pair_response = tuple(fsum(counts[r] * counts[q] * PAIR_MATRICES[t][entry]
                              for t, (r, q) in enumerate(PAIRS)) for entry in range(4))
    require(p.R == pair_response, "F_RESPONSE")
    require(pairing(G0, p.T) == p.N and pairing(G0, p.R) == p.D, "F_RESPONSE")
    require(4 * determinant(G0) * determinant(p.T) == p.D.tau(), "F_RESPONSE")
    require(4 * determinant(G0) * determinant(p.R) == p.D * p.D - norm(p.Q),
            "F_RESPONSE")
    require(positive_semidefinite(p.T) and positive_semidefinite(p.R), "F_RANK")
    support = sum(value > 0 for value in counts)
    energy_rank, response_rank = rank2(p.T), rank2(p.R)
    require(energy_rank == (0 if support == 0 else 1 if support == 1 else 2), "F_RANK")
    require(response_rank == (0 if support <= 1 else 1 if support == 2 else 2), "F_RANK")
    require(p.D.sign() == (0 if support <= 1 else 1), "F_RANK")
    return support, energy_rank, response_rank, rest


def check_hessian(counts, matrix, support):
    pair_matrix = tuple(-fsum(counts[r] * counts[q] * ADIFF_PRODUCTS[entry][t]
                              for t, (r, q) in enumerate(PAIRS)) / 2
                        for entry in range(9))
    require(matrix == pair_matrix, "F_HESSIAN")
    require(all(matrix[i] == 0 for i in (0, 1, 2, 3, 6)), "F_HESSIAN")
    reduced = (matrix[4], matrix[5], matrix[7], matrix[8])
    require(negative_semidefinite(reduced), "F_HESSIAN")
    actual_rank = rank2(reduced)
    require(actual_rank == (0 if support <= 1 else 1 if support == 2 else 2), "F_HESSIAN")
    return actual_rank


def check_series(counts, p, matrix, support, s, energy, mass):
    alpha, beta = STRAIN_PARAMETERS[s]
    require(energy[0] == p.N and mass[0] == p.D, "F_SERIES")
    require(energy[1] == pairing(p.T, H[s]) / 2
            and energy[1] == (alpha * p.N + real(beta * p.W)) / 2, "F_RESPONSE")
    require(mass[1] == pairing(p.R, H[s])
            and mass[1] == alpha * p.D + real(beta * p.Q), "F_RESPONSE")
    direction = DIRECTIONS[s]
    second_derivative = fsum(direction[i] * matrix[3 * i + j] * direction[j]
                             for i in range(3) for j in range(3))
    pair_second = -fsum(counts[r] * counts[q] * PAIR_STRAIN_SQUARES[s][t]
                       for t, (r, q) in enumerate(PAIRS)) / 4
    require(mass[2] == second_derivative / 2 and mass[2] == pair_second, "F_SERIES")
    require(mass[2].sign() <= 0, "F_HESSIAN")
    occupied = [A[s][k] for k in range(5) if counts[k] > 0]
    equal_occupied = not occupied or all(value == occupied[0] for value in occupied)
    require((mass[2] == 0) == equal_occupied, "F_HESSIAN")
    if support >= 3:
        require((mass[2] == 0) == all(value == A[s][0] for value in A[s]), "F_HESSIAN")
    fourth = Fraction(-5, 128) * fsum(counts[k] * A_POWERS[s][k][4] for k in range(5))
    responding = any(counts[k] > 0 and A[s][k] != 0 for k in range(5))
    require(energy[4] == fourth and energy[4].sign() == (-1 if responding else 0), "F_SERIES")
    if not responding:
        require(all(value == 0 for value in energy[1:]), "F_SERIES")


def run_audit():
    check_authority()
    check_geometry()
    payload = Payload()
    payload.emit("G", ftext(G0), ftext(value for vector in U for value in vector))
    for s in range(4):
        payload.emit("B", s, ftext(H[s]), ftext(A[s]))
    energy_ranks, response_ranks, hessian_ranks = [0, 0, 0], [0, 0, 0], [0, 0, 0]
    count_cases = series_cases = rest_cases = 0
    for counts in product(range(5), repeat=5):
        p = prepare(counts)
        support, rank_t, rank_r, rest = check_preparation(counts, p)
        matrix = hessian(counts, p.N)
        rank_b = check_hessian(counts, matrix, support)
        energy_ranks[rank_t] += 1
        response_ranks[rank_r] += 1
        hessian_ranks[rank_b] += 1
        rest_cases += int(rest)
        count_cases += 1
        ntext = ",".join(str(value) for value in counts)
        payload.emit("C", ntext, p.N, ktext(p.Z), ktext(p.W), ftext((p.D,)),
                     ftext(p.T), ftext(p.R), ftext(matrix), f"{rank_t},{rank_r},{rank_b}")
        for s in range(4):
            energy = energy_series(counts, s)
            mass = mass_series(p, energy, s)
            check_series(counts, p, matrix, support, s, energy, mass)
            payload.emit("S", ntext, s, ftext(energy), ftext(mass))
            series_cases += 1

    require(count_cases == 3125 and series_cases == 12500 and rest_cases == 5, "F_COUNTS")
    require(energy_ranks == [1, 20, 3104] and response_ranks == [21, 160, 2944]
            and hessian_ranks == [21, 160, 2944], "F_COUNTS")
    primitive_counts = (1, 0, 1, 0, 0)
    primitive = prepare(primitive_counts)
    inverse_g = inverse(G0)
    fibers = []
    for h in range(8):
        p = prepare((1 + h, h, 1 + h, h, h))
        require(p.Z == KONE + ROOTS[2] and p.Z == primitive.Z and p.W == primitive.W,
                "F_FIBER")
        require(p.N == 2 + 5 * h and p.D == 2 + PHI + 20 * h + 25 * h * h, "F_FIBER")
        require(p.T == add_matrix(primitive.T, scale_matrix(Fraction(5 * h, 2), inverse_g)),
                "F_FIBER")
        require(p.P == primitive.P
                and p.R == subtract_matrix(scale_matrix(p.N, p.T), outer(primitive.P)), "F_FIBER")
        payload.emit("F", h, p.N, ktext(p.Z), ktext(p.W), ftext((p.D,)), ftext(p.T), ftext(p.R))
        fibers.append(p)

    rotation = (ZERO, -ONE, ONE, GAMMA)
    identity = (ONE, ZERO, ZERO, ONE)
    require(matmul(matmul(transpose(rotation), G0), rotation) == G0, "F_ROTATION")
    require(primitive.Q == (KONE - ROOTS[2]) * (KONE - ROOTS[2]), "F_ROTATION")
    rotations = []
    rotation_power = identity
    for r in range(5):
        counts = tuple(int(k in (r, (r + 2) % 5)) for k in range(5))
        p = prepare(counts)
        require(p.N == 2 and p.D == 2 + PHI and p.D.tau() == 3 - PHI, "F_ROTATION")
        require(p.Z == ROOTS[r] * primitive.Z and p.W == ROOTS[(2 * r) % 5] * primitive.W
                and p.Q == ROOTS[(2 * r) % 5] * primitive.Q, "F_ROTATION")
        require(p.P == matvec(rotation_power, primitive.P)
                and p.T == congruence(rotation_power, primitive.T)
                and p.R == congruence(rotation_power, primitive.R), "F_ROTATION")
        payload.emit("O", r, ktext(p.Z), ktext(p.W), ftext((p.D,)), ktext(p.Q), ftext(p.T), ftext(p.R))
        rotations.append(p)
        rotation_power = matmul(rotation, rotation_power)
    require(rotation_power == identity, "F_ROTATION")
    require(all(left.Q != right.Q and left.R != right.R
                for left, right in combinations(rotations, 2)), "F_ROTATION")

    single_counts = (1, 0, 0, 0, 0)
    single = prepare(single_counts)
    single_e = energy_series(single_counts, 0)
    single_d = mass_series(single, single_e, 0)
    primitive_e = energy_series(primitive_counts, 1)
    primitive_d = mass_series(primitive, primitive_e, 1)
    primitive_b = hessian(primitive_counts, primitive.N)
    cross = (ZERO, ONE, ONE, ZERO)
    cross_e1 = fsum(primitive_counts[k] * quadratic(U[k], cross) for k in range(5)) / 2
    controls = (
        single_e[1] == F(Fraction(1, 2)) and single_d[1] == 0 and single_e[1] != single_d[1],
        primitive_e[1] != real(primitive.Z) / 2,
        any(value != 0 for value in subtract_matrix(scale_matrix(primitive.N, primitive.T), primitive.R)),
        all((p.N, p.D, p.D.tau()) == (primitive.N, primitive.D, primitive.D.tau()) for p in rotations)
        and all(a.R != b.R for a, b in combinations(rotations, 2)),
        fibers[0].Z == fibers[1].Z and fibers[0].W == fibers[1].W and fibers[0].T != fibers[1].T
        and subtract_matrix(fibers[1].T, fibers[0].T) == scale_matrix(Fraction(5, 2), inverse_g),
        cross_e1 == primitive.T[1] and cross_e1 != primitive.T[1] / 2,
        primitive_d[2] != primitive_b[4] and primitive_b[4] == 2 * primitive_d[2],
        single_e[4] == F(Fraction(-5, 128)) and single_e[4] != 0,
    )
    for index, detected in enumerate(controls, 1):
        require(detected, "F_CONTROL")
        payload.emit("N", f"NC{index:02d}", "DETECTED")
    require(len(fibers) == 8 and len(rotations) == 5 and len(controls) == 8
            and payload.records == 15651, "F_COUNTS")
    lines = (
        f"CERTIFICATE={PROBE}",
        f"AUTHORITY_FILES={len(AUTHORITY)}",
        f"COUNT_CASES={count_cases}",
        f"STRAIN_DIRECTIONS={len(H)}",
        "SERIES_ORDER=4",
        f"SERIES_CASES={series_cases}",
        "ENERGY_RANK_COUNTS=" + ",".join(map(str, energy_ranks)),
        "MASS_RESPONSE_RANK_COUNTS=" + ",".join(map(str, response_ranks)),
        "HESSIAN_RANK_COUNTS=" + ",".join(map(str, hessian_ranks)),
        f"REST_CASES={rest_cases}",
        f"FIBER_CASES={len(fibers)}",
        f"ROTATION_CASES={len(rotations)}",
        f"NEGATIVE_CONTROLS={len(controls)}",
        f"PAYLOAD_RECORDS={payload.records}",
        f"PAYLOAD_SHA256={payload.digest.hexdigest()}",
        "CERTIFICATE_RESULT=PASS",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        certificate = run_audit()
        sibling = Path(__file__).with_name("breaker.py").resolve()
        companion = subprocess.run([sys.executable, "-I", str(sibling)],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=540, check=False)
        require(companion.returncode == 0 and companion.stderr == b""
                and companion.stdout == certificate, "F_BYTES")
    except ScientificFailure as failure:
        sys.stdout.write("FAILURE=" + str(failure) + "\nRESULT=FAIL\n")
        return 0
    # Unexpected exceptions, including a companion timeout, remain incomplete
    # nonzero executions; they are never converted to scientific success.
    sys.stdout.buffer.write(certificate + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
