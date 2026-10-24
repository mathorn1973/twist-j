"""Exact Z7 algebra, finite lattice, sampler and source-Hessian reader.

PUBLIC / NON-CANONICAL. No phase inference is implemented.
Original code: A. M. Thorn, Apache-2.0.

The field generator x is the root in (1, 3/2) of x^3+x^2-2*x-1.
All transition comparisons use rationals and integer polynomial arithmetic.
The sampling theorem assumes an ideal independent fair-bit stream. A seeded
random.Random instance is a deterministic engineering realization, not a
mathematical source of independent randomness or a physical sampling law.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
import random


def _rational(value):
    if not isinstance(value, (int, Fraction)):
        raise TypeError("Only integers and Fraction coefficients are admitted")
    return Fraction(value)


_ROOT_LO = Fraction(1)
_ROOT_HI = Fraction(3, 2)


def _minimal(value):
    return value**3 + value**2 - 2 * value - 1


def _refine_root():
    global _ROOT_LO, _ROOT_HI
    middle = (_ROOT_LO + _ROOT_HI) / 2
    if _minimal(middle) < 0:
        _ROOT_LO = middle
    else:
        _ROOT_HI = middle


@dataclass(frozen=True)
class K7:
    """c0+c1*x+c2*x^2 with exact reduced rational coefficients."""

    c0: Fraction = Fraction(0)
    c1: Fraction = Fraction(0)
    c2: Fraction = Fraction(0)

    def __post_init__(self):
        for name in ("c0", "c1", "c2"):
            object.__setattr__(self, name, _rational(getattr(self, name)))

    @property
    def coefficients(self):
        return (self.c0, self.c1, self.c2)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, K7) else K7(value)

    def __add__(self, other):
        other = self.coerce(other)
        return K7(*(a + b for a, b in zip(self.coefficients, other.coefficients)))

    __radd__ = __add__

    def __neg__(self):
        return K7(*(-a for a in self.coefficients))

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        values = [Fraction(0) for _ in range(5)]
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                values[i + j] += a * b
        for degree in (4, 3):
            coefficient = values[degree]
            values[degree] = Fraction(0)
            # x^degree = x^(degree-3) * (1+2*x-x^2).
            values[degree - 3] += coefficient
            values[degree - 2] += 2 * coefficient
            values[degree - 1] -= coefficient
        return K7(*values[:3])

    __rmul__ = __mul__

    def inverse(self):
        if self == K7():
            raise ZeroDivisionError("Zero field element")
        basis = (K7(1), K7(0, 1), K7(0, 0, 1))
        columns = [(self * b).coefficients for b in basis]
        matrix = [
            [columns[col][row] for col in range(3)]
            + [Fraction(int(row == 0))]
            for row in range(3)
        ]
        for col in range(3):
            pivot = next(row for row in range(col, 3) if matrix[row][col])
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            scale = matrix[col][col]
            matrix[col] = [entry / scale for entry in matrix[col]]
            for row in range(3):
                if row != col:
                    factor = matrix[row][col]
                    matrix[row] = [
                        a - factor * b
                        for a, b in zip(matrix[row], matrix[col])
                    ]
        return K7(*(matrix[row][3] for row in range(3)))

    def __truediv__(self, other):
        other = self.coerce(other)
        if other.c1 == 0 and other.c2 == 0:
            if other.c0 == 0:
                raise ZeroDivisionError("Zero field element")
            return K7(*(coefficient / other.c0 for coefficient in self.coefficients))
        return self * other.inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("Integer exponent required")
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result, factor = K7(1), self
        while exponent:
            if exponent & 1:
                result *= factor
            factor *= factor
            exponent //= 2
        return result

    def interval(self):
        """A certified rational enclosure in the selected real embedding."""
        lower = upper = self.c0
        for coefficient, lo, hi in (
            (self.c1, _ROOT_LO, _ROOT_HI),
            (self.c2, _ROOT_LO**2, _ROOT_HI**2),
        ):
            if coefficient >= 0:
                lower += coefficient * lo
                upper += coefficient * hi
            else:
                lower += coefficient * hi
                upper += coefficient * lo
        return lower, upper

    def sign(self):
        if self == K7():
            return 0
        while True:
            lower, upper = self.interval()
            if lower > 0:
                return 1
            if upper < 0:
                return -1
            _refine_root()

    def to_json(self):
        return [[a.numerator, a.denominator] for a in self.coefficients]

    @staticmethod
    def from_json(values):
        if len(values) != 3:
            raise ValueError("Three rational coefficients required")
        return K7(*(Fraction(numerator, denominator) for numerator, denominator in values))


X7 = K7(0, 1)
R7 = (2 - X7) / (2 + X7)
WEIGHTS = (
    K7(4), 2 + X7, X7**2, 3 - X7 - X7**2,
    3 - X7 - X7**2, X7**2, 2 + X7,
)
_G2 = (2 + X7) / X7
_G3 = (1 + X7) / (X7 - 1)
G_SCORE = (K7(), K7(1), _G2, _G3, -_G3, -_G2, K7(-1))
SCORE_CURVATURE = tuple((1 + R7 * g**2) / 2 for g in G_SCORE)


def exact_categorical(masses, rng, counters=None):
    """Choose proportional to positive K7 masses, using a lazy bit interval.

    U is specified by successive 32-bit blocks. A category is returned only
    when the entire current half-open dyadic U interval lies in that category.
    Termination is almost sure for ideal fair bits; exact interval endpoints
    are handled without rounding. No numerical-precision timeout is imposed.
    """
    masses = tuple(K7.coerce(m) for m in masses)
    if not masses or any(m.sign() <= 0 for m in masses):
        raise ValueError("Every categorical mass must be strictly positive")
    cumulative = []
    total = K7()
    for mass in masses:
        total += mass
        cumulative.append(total)
    numerator, denominator = 0, 1
    while True:
        numerator = (numerator << 32) | rng.getrandbits(32)
        denominator <<= 32
        if counters is not None:
            counters["random_bits"] = counters.get("random_bits", 0) + 32
        lo, hi = numerator * total, (numerator + 1) * total
        previous = K7()
        for category, endpoint in enumerate(cumulative):
            lower_ok = (lo - denominator * previous).sign() >= 0
            upper_ok = (denominator * endpoint - hi).sign() >= 0
            if lower_ok and upper_ok:
                return category
            previous = endpoint


class CubicLattice:
    """Periodic positive-coordinate cubical lattice; every length is >=2.

    Edge index = site_index*D+mu. Face index = site_index*C(D,2)+orientation.
    Sites are lexicographic tuples; orientations are lexicographic (mu,nu).
    """

    def __init__(self, lengths):
        self.lengths = tuple(lengths)
        if len(self.lengths) < 2 or any(not isinstance(l, int) or l < 2 for l in self.lengths):
            raise ValueError("At least two integer lengths >=2 are required")
        self.dimension = len(self.lengths)
        self.sites = tuple(product(*(range(l) for l in self.lengths)))
        self.site_index = {site: index for index, site in enumerate(self.sites)}
        self.volume = len(self.sites)
        self.orientations = tuple(combinations(range(self.dimension), 2))
        self.orientation_index = {pair: index for index, pair in enumerate(self.orientations)}
        self.n_edges = self.volume * self.dimension
        self.n_faces = self.volume * len(self.orientations)
        self.edge_faces = [[] for _ in range(self.n_edges)]
        self.face_boundaries = []
        for site in self.sites:
            for mu, nu in self.orientations:
                boundary = (
                    (self.edge(site, mu), 1),
                    (self.edge(self.shift(site, mu), nu), 1),
                    (self.edge(self.shift(site, nu), mu), -1),
                    (self.edge(site, nu), -1),
                )
                face = len(self.face_boundaries)
                self.face_boundaries.append(boundary)
                for edge, sign in boundary:
                    self.edge_faces[edge].append((face, sign))

    def shift(self, site, direction, amount=1):
        result = list(site)
        result[direction] = (result[direction] + amount) % self.lengths[direction]
        return tuple(result)

    def edge(self, site, direction):
        return self.site_index[tuple(site)] * self.dimension + direction

    def face(self, site, mu, nu):
        return self.site_index[tuple(site)] * len(self.orientations) + self.orientation_index[(mu, nu)]

    def boundary(self, face):
        return self.face_boundaries[face]

    def curl(self, links):
        if len(links) != self.n_edges:
            raise ValueError("Wrong link count")
        return [sum(sign * links[edge] for edge, sign in boundary) % 7 for boundary in self.face_boundaries]

    def bianchi(self, flux):
        if len(flux) != self.n_faces:
            raise ValueError("Wrong face count")
        values = []
        for site in self.sites:
            for directions in combinations(range(self.dimension), 3):
                value = 0
                for i, direction in enumerate(directions):
                    mu, nu = tuple(d for d in directions if d != direction)
                    difference = flux[self.face(self.shift(site, direction), mu, nu)] - flux[self.face(site, mu, nu)]
                    value += (-1)**i * difference
                values.append(value % 7)
        return tuple(values)

    def orientation_faces(self, orientation):
        mu, nu = tuple(orientation)
        return tuple(self.face(site, mu, nu) for site in self.sites)

    def principal_plane_fluxes(self, flux):
        """Integer principal-lift plane sums /7, ONLY primal diagnostics.

        These are not the dual winding W in the source-partition theorem.
        Plane values can differ when principal-lift monopoles are present.
        """
        lift = (0, 1, 2, 3, -3, -2, -1)
        result = {}
        for mu, nu in self.orientations:
            others = tuple(d for d in range(self.dimension) if d not in (mu, nu))
            sums = {}
            for site in self.sites:
                key = tuple(site[d] for d in others)
                sums[key] = sums.get(key, 0) + lift[flux[self.face(site, mu, nu)]]
            if any(value % 7 for value in sums.values()):
                raise ValueError("Principal plane flux is not divisible by seven")
            result[f"{mu},{nu}"] = [sums[key] // 7 for key in sorted(sums)]
        return result


def source_hessian(flux, source):
    """Exact -log Z second-derivative estimator at zero real source.

    source contains rational direction coefficients on all faces. Global
    charge conjugation makes the equilibrium first derivative zero. A single
    sampled value may be negative; this is not Var(W) configuration by
    configuration and must never be clipped at zero.
    """
    if len(flux) != len(source):
        raise ValueError("Source and flux lengths differ")
    score = K7()
    curvature = K7()
    for residue, coefficient in zip(flux, source):
        coefficient = _rational(coefficient)
        if not 0 <= residue < 7:
            raise ValueError("Noncanonical Z7 residue")
        if coefficient == 0:
            continue
        g = G_SCORE[residue]
        score += coefficient * g
        curvature += coefficient**2 * SCORE_CURVATURE[residue]
    return curvature - R7 * score**2


def uniform_helicity(lattice, flux, orientation=None):
    """Uniform-source Hessian, averaged over all orientations if omitted.

    The N=7 identification with U(1) and winding variance uses D<=4.
    This finite Z7 curvature reader is also defined in other dimensions,
    where no U(1) or stack/uniform equality is implied by this module.
    """
    orientations = lattice.orientations if orientation is None else (tuple(orientation),)
    total = K7()
    for mu, nu in orientations:
        source = [Fraction(0)] * lattice.n_faces
        area = lattice.lengths[mu] * lattice.lengths[nu]
        for face in lattice.orientation_faces((mu, nu)):
            source[face] = Fraction(1, area)
        total += source_hessian(flux, source)
    return total / len(orientations)


def stack_helicity(lattice, flux, orientation=(0, 1), anchor=(0, 0)):
    """Stack-source Hessian; equality with uniform is an expectation identity."""
    mu, nu = tuple(orientation)
    source = [Fraction(0)] * lattice.n_faces
    for site in lattice.sites:
        if site[mu] == anchor[0] and site[nu] == anchor[1]:
            source[lattice.face(site, mu, nu)] = Fraction(1)
    return source_hessian(flux, source)


class ExactHeatBath:
    """Untwisted periodic Z7 heat bath; finite exact transitions, no mixing claim."""

    def __init__(self, lattice, seed, links=None):
        self.lattice = lattice
        self.rng = random.Random(seed)
        self.links = [0] * lattice.n_edges if links is None else list(links)
        if len(self.links) != lattice.n_edges or any(not isinstance(k, int) or not 0 <= k < 7 for k in self.links):
            raise ValueError("Invalid initial links")
        self.flux = lattice.curl(self.links)
        self.mass_cache = {}
        self.counters = {"random_bits": 0, "edge_updates": 0, "edge_changes": 0, "sweeps": 0}

    def staple_counts(self, edge):
        old = self.links[edge]
        counts = [0] * 7
        for face, sign in self.lattice.edge_faces[edge]:
            counts[(old - sign * self.flux[face]) % 7] += 1
        return tuple(counts)

    def conditional_masses(self, edge):
        counts = self.staple_counts(edge)
        if counts not in self.mass_cache:
            masses = []
            for proposed in range(7):
                mass = K7(1)
                for staple, multiplicity in enumerate(counts):
                    mass *= WEIGHTS[(proposed - staple) % 7] ** multiplicity
                masses.append(mass)
            self.mass_cache[counts] = tuple(masses)
        return self.mass_cache[counts]

    def step_edge(self, edge):
        if not isinstance(edge, int) or not 0 <= edge < self.lattice.n_edges:
            raise ValueError("Invalid edge index")
        proposed = exact_categorical(self.conditional_masses(edge), self.rng, self.counters)
        old = self.links[edge]
        self.links[edge] = proposed
        difference = proposed - old
        for face, sign in self.lattice.edge_faces[edge]:
            self.flux[face] = (self.flux[face] + sign * difference) % 7
        self.counters["edge_updates"] += 1
        self.counters["edge_changes"] += int(proposed != old)
        return proposed

    def sweep(self):
        for edge in range(self.lattice.n_edges):
            self.step_edge(edge)
        self.counters["sweeps"] += 1

    def assert_consistent(self):
        if self.flux != self.lattice.curl(self.links):
            raise AssertionError("Cached flux differs from direct curl")
        if any(self.lattice.bianchi(self.flux)):
            raise AssertionError("Mod-seven Bianchi identity failed")
        self.lattice.principal_plane_fluxes(self.flux)

