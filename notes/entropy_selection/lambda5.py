"""Exact local model of :math:`Z[zeta_5]/(1-zeta_5)^5`.

NON-CANONICAL LOCAL ANALYSIS.  This module is a recon tool, not a public
verifier and not evidence for a Canon claim.

The public P-ENTROPY-BRIDGE-3 convention uses column vectors in the power
basis ``(1, zeta, zeta^2, zeta^3)``.  We retain its matrices exactly and use
the auxiliary basis ``(1, lambda, lambda^2, lambda^3)``, where
``lambda = 1-zeta``, to expose the quotient.

Substitution in ``Phi_5(zeta)=0`` gives

    lambda^4 = -5 + 10 lambda - 10 lambda^2 + 5 lambda^3.

The coefficient of ``lambda^4`` divided by 5 is a lambda-adic unit, hence
``(lambda^5) = (5 lambda)``.  In the lambda basis this ideal is exactly

    25 Z  +  5 Z lambda  +  5 Z lambda^2  +  5 Z lambda^3.

Consequently every quotient class has a unique normal form
``(a0 mod 25, a1 mod 5, a2 mod 5, a3 mod 5)`` and, equivalently, a unique
five-digit expansion ``sum(d_i lambda^i, i=0..4)`` with ``d_i in F_5``.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from math import factorial
from typing import Iterable, Iterator, Mapping, Sequence


Vector4 = tuple[int, int, int, int]
Digit5 = tuple[int, int, int, int, int]
Permutation = tuple[int, ...]
Matrix4 = tuple[Vector4, Vector4, Vector4, Vector4]

PRIME = 5
DEPTH = 5
SIZE = PRIME**DEPTH

# Public P-ENTROPY-BRIDGE-3 matrices.  Matrices act on column vectors.
ZETA_MATRIX: Matrix4 = (
    (0, 0, 0, -1),
    (1, 0, 0, -1),
    (0, 1, 0, -1),
    (0, 0, 1, -1),
)
IDENTITY_MATRIX: Matrix4 = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
LAMBDA_MATRIX: Matrix4 = tuple(
    tuple(IDENTITY_MATRIX[i][j] - ZETA_MATRIX[i][j] for j in range(4))
    for i in range(4)
)  # type: ignore[assignment]
J_POWER_MATRIX: Matrix4 = (
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)

# Change of basis from lambda coordinates to power coordinates.  It is its
# own inverse because zeta=1-lambda is an involutive substitution.
LAMBDA_TO_POWER: Matrix4 = (
    (1, 1, 1, 1),
    (0, -1, -2, -3),
    (0, 0, 1, 3),
    (0, 0, 0, -1),
)
POWER_TO_LAMBDA: Matrix4 = LAMBDA_TO_POWER

# lambda^4 in the lambda basis.
LAMBDA4_RELATION: Vector4 = (-5, 10, -10, 5)


def _mat_vec(matrix: Matrix4, vector: Sequence[int]) -> Vector4:
    if len(vector) != 4:
        raise ValueError("a power-basis vector must have four coordinates")
    return tuple(
        sum(matrix[i][j] * int(vector[j]) for j in range(4))
        for i in range(4)
    )  # type: ignore[return-value]


def _mat_mul(left: Matrix4, right: Matrix4) -> Matrix4:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(4))
            for j in range(4)
        )
        for i in range(4)
    )  # type: ignore[return-value]


def _mat_pow(matrix: Matrix4, exponent: int) -> Matrix4:
    if exponent < 0:
        raise ValueError("matrix exponent must be non-negative")
    result = IDENTITY_MATRIX
    base = matrix
    while exponent:
        if exponent & 1:
            result = _mat_mul(result, base)
        base = _mat_mul(base, base)
        exponent >>= 1
    return result


def lambda_to_power(vector: Sequence[int]) -> Vector4:
    """Convert exact lambda-basis coordinates to the public power basis."""

    return _mat_vec(LAMBDA_TO_POWER, vector)


def power_to_lambda(vector: Sequence[int]) -> Vector4:
    """Convert exact public power-basis coordinates to the lambda basis."""

    return _mat_vec(POWER_TO_LAMBDA, vector)


def _encode_digits(digits: Sequence[int]) -> int:
    if len(digits) != DEPTH:
        raise ValueError("a lambda^5 class needs exactly five digits")
    index = 0
    place = 1
    for digit in digits:
        value = int(digit)
        if not 0 <= value < PRIME:
            raise ValueError("canonical lambda digits must lie in range(5)")
        index += value * place
        place *= PRIME
    return index


def _decode_index(index: int) -> Digit5:
    if not 0 <= index < SIZE:
        raise ValueError("lambda^5 class index must lie in range(3125)")
    digits = []
    value = index
    for _ in range(DEPTH):
        digits.append(value % PRIME)
        value //= PRIME
    return tuple(digits)  # type: ignore[return-value]


@dataclass(frozen=True, order=True, slots=True)
class Lambda5:
    """One class in ``O/lambda^5``, canonically indexed by five digits."""

    index: int

    def __post_init__(self) -> None:
        if not isinstance(self.index, int) or not 0 <= self.index < SIZE:
            raise ValueError("lambda^5 class index must lie in range(3125)")

    @classmethod
    def zero(cls) -> Lambda5:
        return cls(0)

    @classmethod
    def one(cls) -> Lambda5:
        return cls(1)

    @classmethod
    def from_digits(cls, digits: Sequence[int]) -> Lambda5:
        """Reduce an arbitrary five-term lambda expansion modulo lambda^5."""

        if len(digits) != DEPTH:
            raise ValueError("a lambda^5 expansion needs exactly five terms")
        d0, d1, d2, d3, d4 = (int(value) for value in digits)
        return cls.from_lambda_coeffs(
            (
                d0 - 5 * d4,
                d1 + 10 * d4,
                d2 - 10 * d4,
                d3 + 5 * d4,
            )
        )

    @classmethod
    def from_lambda_coeffs(cls, vector: Sequence[int]) -> Lambda5:
        """Reduce a four-vector in ``(1,lambda,lambda^2,lambda^3)``."""

        if len(vector) != 4:
            raise ValueError("a lambda-basis vector must have four coordinates")
        a0 = int(vector[0]) % 25
        a1 = int(vector[1]) % 5
        a2 = int(vector[2]) % 5
        a3 = int(vector[3]) % 5
        d0 = a0 % 5
        d4 = ((d0 - a0) // 5) % 5
        return cls(_encode_digits((d0, a1, a2, a3, d4)))

    @classmethod
    def from_power_coeffs(cls, vector: Sequence[int]) -> Lambda5:
        """Reduce a public power-basis vector modulo ``lambda^5``."""

        return cls.from_lambda_coeffs(power_to_lambda(vector))

    @property
    def digits(self) -> Digit5:
        """The unique digits ``d_0,...,d_4`` in ``F_5``."""

        return _decode_index(self.index)

    @property
    def lambda_coeffs(self) -> Vector4:
        """The unique additive normal form modulo ``(25,5,5,5)``."""

        d0, d1, d2, d3, d4 = self.digits
        return ((d0 - 5 * d4) % 25, d1, d2, d3)

    @property
    def power_coeffs(self) -> Vector4:
        """A canonical representative in the public power basis."""

        return lambda_to_power(self.lambda_coeffs)

    def valuation(self) -> int:
        """Return the truncated lambda valuation in ``0..5``.

        The zero class has value 5, recording divisibility by lambda^5 in
        this truncated ring.
        """

        for position, digit in enumerate(self.digits):
            if digit:
                return position
        return DEPTH

    def is_unit(self) -> bool:
        """Return whether this class is a unit of the local quotient ring."""

        return self.valuation() == 0

    def inverse(self) -> Lambda5:
        """Return the multiplicative inverse of a unit.

        If ``a`` in ``{1,2,3,4}`` inverts the residue digit, then
        ``a*self = 1+n`` with ``n`` in ``lambda R``.  Since ``n^5=0`` in
        this quotient, the finite geometric series
        ``1-n+n^2-n^3+n^4`` is the exact inverse of ``1+n``.
        """

        if not self.is_unit():
            raise ValueError("only valuation-zero classes are units")
        residue_inverse = pow(self.digits[0], -1, PRIME)
        scaled = residue_inverse * self
        nilpotent = scaled - ONE
        series = ONE
        term = ONE
        for _ in range(1, DEPTH):
            term = -(term * nilpotent)
            series = series + term
        result = residue_inverse * series
        if self * result != ONE:
            raise AssertionError("finite unit inverse construction failed")
        return result

    def mul_by_lambda(self) -> Lambda5:
        """Multiply by lambda in the quotient."""

        return Lambda5.from_digits((0,) + self.digits[:4])

    def mul_by_j(self) -> Lambda5:
        """Apply the public regular-representation matrix of ``J``."""

        return Lambda5.from_power_coeffs(
            _mat_vec(J_POWER_MATRIX, self.power_coeffs)
        )

    def __add__(self, other: object) -> Lambda5:
        if not isinstance(other, Lambda5):
            return NotImplemented
        return Lambda5.from_lambda_coeffs(
            tuple(a + b for a, b in zip(self.lambda_coeffs, other.lambda_coeffs))
        )

    def __neg__(self) -> Lambda5:
        return Lambda5.from_lambda_coeffs(tuple(-a for a in self.lambda_coeffs))

    def __sub__(self, other: object) -> Lambda5:
        if not isinstance(other, Lambda5):
            return NotImplemented
        return self + (-other)

    def __mul__(self, other: object) -> Lambda5:
        if not isinstance(other, Lambda5):
            return NotImplemented
        left = self.lambda_coeffs
        right = other.lambda_coeffs
        product = [0] * 7
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                product[i + j] += a * b

        # Reduce high powers by lambda^4=(-5,10,-10,5), from high to low.
        for degree in range(6, 3, -1):
            coefficient = product[degree]
            if not coefficient:
                continue
            product[degree] = 0
            offset = degree - 4
            for j, relation_coefficient in enumerate(LAMBDA4_RELATION):
                product[offset + j] += coefficient * relation_coefficient
        return Lambda5.from_lambda_coeffs(product[:4])

    def __rmul__(self, scalar: object) -> Lambda5:
        if not isinstance(scalar, int):
            return NotImplemented
        return Lambda5.from_lambda_coeffs((scalar, 0, 0, 0)) * self


ZERO = Lambda5.zero()
ONE = Lambda5.one()
LAMBDA = Lambda5.from_digits((0, 1, 0, 0, 0))
J = Lambda5.from_power_coeffs((1, 0, 1, 0))  # J = 1 + zeta^2.


def elements() -> Iterator[Lambda5]:
    """Iterate through all 3125 canonical representatives."""

    return (Lambda5(index) for index in range(SIZE))


def units() -> Iterator[Lambda5]:
    """Iterate through all ``4*5^4 = 2500`` quotient-ring units."""

    return (element for element in elements() if element.is_unit())


def equivalent_power_vectors(left: Sequence[int], right: Sequence[int]) -> bool:
    """Test exact congruence modulo lambda^5 in the public power basis."""

    return Lambda5.from_power_coeffs(left) == Lambda5.from_power_coeffs(right)


@lru_cache(maxsize=1)
def j_permutation() -> Permutation:
    """Return the full permutation, indexed by canonical digit index."""

    return tuple(element.mul_by_j().index for element in elements())


def permutation_cycles(permutation: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    """Return canonically based and ordered oriented cycles."""

    size = len(permutation)
    if set(permutation) != set(range(size)):
        raise ValueError("mapping is not a permutation")
    unseen = set(range(size))
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        state = start
        while state in unseen:
            unseen.remove(state)
            cycle.append(state)
            state = permutation[state]
        if state != start:
            raise ValueError("mapping contains a tail, not a cycle")
        cycles.append(tuple(cycle))
    cycles.sort(key=lambda cycle: (len(cycle), cycle[0]))
    return tuple(cycles)


@lru_cache(maxsize=1)
def j_orbits() -> tuple[tuple[int, ...], ...]:
    """Return the oriented J-orbits in canonical order."""

    return permutation_cycles(j_permutation())


def j_orbit_spectrum() -> dict[int, int]:
    """Return ``{orbit_length: orbit_count}`` for multiplication by J."""

    return dict(sorted(Counter(map(len, j_orbits())).items()))


@lru_cache(maxsize=1)
def j_orbit_coordinates() -> tuple[tuple[int, int, int], ...]:
    """Map each class index to ``(length, cycle_number, position)``."""

    cycles_by_length: dict[int, list[tuple[int, ...]]] = {}
    for cycle in j_orbits():
        cycles_by_length.setdefault(len(cycle), []).append(cycle)
    coordinates: list[tuple[int, int, int] | None] = [None] * SIZE
    for length, cycles in cycles_by_length.items():
        for cycle_number, cycle in enumerate(cycles):
            for position, point in enumerate(cycle):
                coordinates[point] = (length, cycle_number, position)
    if any(coordinate is None for coordinate in coordinates):
        raise AssertionError("J-orbit coordinates do not cover the quotient")
    return tuple(coordinates)  # type: ignore[return-value]


@dataclass(frozen=True, slots=True)
class CycleAction:
    """One wreath-product factor of a centralizer element.

    ``cycle_permutation[i]`` is the destination of source cycle ``i`` and
    ``shifts[i]`` is its rotation in the J-oriented destination cycle.
    """

    length: int
    cycle_permutation: tuple[int, ...]
    shifts: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class CentralizerDescription:
    cycle_counts: tuple[tuple[int, int], ...]
    abstract_factors: tuple[str, ...]
    order: int
    canonical_generator_count: int


@dataclass(frozen=True, slots=True)
class ArithmeticCentralizerDescription:
    """The faithful ring-unit subgroup of the full permutation centralizer."""

    name: str
    order: int
    factorization: tuple[tuple[int, int], ...]
    full_centralizer_order: int
    index_in_full_centralizer: int
    faithful: bool


@lru_cache(maxsize=1)
def centralizer_description() -> CentralizerDescription:
    """Describe ``Cent_Sym(3125)(J)`` by its wreath-product factors."""

    spectrum = tuple(j_orbit_spectrum().items())
    factors = tuple(
        ("C_%d" % length if count == 1 else "C_%d wr S_%d" % (length, count))
        for length, count in spectrum
        if not (length == 1 and count == 1)
    )
    order = 1
    generator_count = 0
    for length, count in spectrum:
        order *= (length**count) * factorial(count)
        if length > 1:
            generator_count += count
        generator_count += max(0, count - 1)
    return CentralizerDescription(spectrum, factors, order, generator_count)


@lru_cache(maxsize=1)
def arithmetic_centralizer_description() -> ArithmeticCentralizerDescription:
    """Describe multiplication by ``(O/lambda^5)^x`` on the quotient.

    Units are exactly the 2500 valuation-zero classes.  Their multiplication
    action is faithful (the image of 1 recovers the unit), and commutativity
    of the quotient ring puts this group inside the full centralizer of J.
    """

    order = (PRIME - 1) * PRIME ** (DEPTH - 1)
    full_order = centralizer_description().order
    if full_order % order:
        raise AssertionError("ring-unit action order must divide Cent(J)")
    return ArithmeticCentralizerDescription(
        name="(O/lambda^5)^x by multiplication",
        order=order,
        factorization=((2, 2), (5, 4)),
        full_centralizer_order=full_order,
        index_in_full_centralizer=full_order // order,
        faithful=True,
    )


def unit_multiplication_permutation(unit: Lambda5) -> Permutation:
    """Return the carrier permutation ``x -> unit*x``.

    The unit check is semantic, not inferred from a coincidental image size.
    Its inverse permutation is multiplication by ``unit.inverse()``.
    """

    if not isinstance(unit, Lambda5) or not unit.is_unit():
        raise ValueError("multiplication centralizer elements require a unit")
    return tuple((unit * element).index for element in elements())


def iter_unit_multiplication_permutations() -> Iterator[tuple[Lambda5, Permutation]]:
    """Lazily enumerate all 2500 arithmetic centralizer permutations."""

    return ((unit, unit_multiplication_permutation(unit)) for unit in units())


def verify_unit_multiplication(unit: Lambda5, *, full_carrier: bool = True) -> bool:
    """Verify bijectivity and commutation of one ring-unit action.

    The algebraic gate always checks a two-sided inverse and the commutator
    with J.  ``full_carrier=True`` additionally materializes the 3125-point
    action and checks it as a permutation commuting with the public J map.
    """

    if not isinstance(unit, Lambda5) or not unit.is_unit():
        return False
    inverse = unit.inverse()
    if unit * inverse != ONE or inverse * unit != ONE:
        return False
    if unit * J != J * unit:
        return False
    if not full_carrier:
        return True
    mapping = unit_multiplication_permutation(unit)
    return is_permutation(mapping) and commutes_with_j(mapping)


def verify_arithmetic_centralizer() -> bool:
    """Exhaustively verify the 2500-unit arithmetic subgroup algebraically.

    For every unit this checks an exact inverse and commutation with J.
    These identities prove that its multiplication map is a bijection in the
    full carrier centralizer; representative full-carrier materializations
    are exercised separately by the focused tests.
    """

    unit_list = tuple(units())
    description = arithmetic_centralizer_description()
    if len(unit_list) != description.order or len(set(unit_list)) != description.order:
        return False
    if any(not verify_unit_multiplication(unit, full_carrier=False) for unit in unit_list):
        return False
    # Faithfulness: evaluation at 1 maps the multiplication action back to u.
    return all(unit * ONE == unit for unit in unit_list)


def _cycles_by_length() -> dict[int, tuple[tuple[int, ...], ...]]:
    grouped: dict[int, list[tuple[int, ...]]] = {}
    for cycle in j_orbits():
        grouped.setdefault(len(cycle), []).append(cycle)
    return {length: tuple(cycles) for length, cycles in grouped.items()}


def centralizer_element(actions: Iterable[CycleAction] = ()) -> Permutation:
    """Build an arbitrary element of the full permutation centralizer.

    Omitted cycle lengths use the identity action.  Every centralizer element
    is represented uniquely by one cycle permutation and one rotation per
    source cycle at each length.
    """

    grouped = _cycles_by_length()
    supplied: dict[int, CycleAction] = {}
    for action in actions:
        if action.length in supplied:
            raise ValueError("duplicate centralizer action for one length")
        supplied[action.length] = action
    if not set(supplied).issubset(grouped):
        raise ValueError("centralizer action names an absent cycle length")

    result = list(range(SIZE))
    for length, cycles in grouped.items():
        count = len(cycles)
        action = supplied.get(
            length,
            CycleAction(length, tuple(range(count)), (0,) * count),
        )
        sigma = action.cycle_permutation
        shifts = action.shifts
        if len(sigma) != count or set(sigma) != set(range(count)):
            raise ValueError("cycle_permutation is not a permutation")
        if len(shifts) != count:
            raise ValueError("one shift is required per source cycle")
        for source_number, source_cycle in enumerate(cycles):
            target_cycle = cycles[sigma[source_number]]
            shift = shifts[source_number] % length
            for position, point in enumerate(source_cycle):
                result[point] = target_cycle[(position + shift) % length]
    return tuple(result)


def iter_centralizer_generators() -> Iterator[tuple[str, Permutation]]:
    """Yield a transparent generating family for the full centralizer.

    For each nontrivial J-cycle this includes its unit rotation.  For each
    adjacent equal-length pair it includes the unshifted cycle swap.  These
    are the standard generators of ``product_l C_l wr S_(m_l)``.
    """

    grouped = _cycles_by_length()
    for length, cycles in sorted(grouped.items()):
        count = len(cycles)
        if length > 1:
            for cycle_number in range(count):
                shifts = [0] * count
                shifts[cycle_number] = 1
                action = CycleAction(
                    length, tuple(range(count)), tuple(shifts)
                )
                yield "rotate-%d-%d" % (length, cycle_number), centralizer_element(
                    (action,)
                )
        for cycle_number in range(count - 1):
            sigma = list(range(count))
            sigma[cycle_number], sigma[cycle_number + 1] = (
                sigma[cycle_number + 1],
                sigma[cycle_number],
            )
            action = CycleAction(length, tuple(sigma), (0,) * count)
            yield "swap-%d-%d" % (length, cycle_number), centralizer_element(
                (action,)
            )


def centralizer_orbits() -> tuple[tuple[int, ...], ...]:
    """Return the carrier orbits of the full centralizer.

    The full wreath product is transitive on all points lying on J-cycles of
    a fixed length, so these blocks are indexed exactly by orbit length.
    """

    grouped = _cycles_by_length()
    return tuple(
        tuple(point for cycle in grouped[length] for point in cycle)
        for length in sorted(grouped)
    )


def is_permutation(mapping: Sequence[int]) -> bool:
    return len(mapping) == SIZE and set(mapping) == set(range(SIZE))


def commutes_with_j(mapping: Sequence[int]) -> bool:
    """Check whether a carrier permutation commutes with multiplication by J."""

    if not is_permutation(mapping):
        return False
    j_map = j_permutation()
    return all(mapping[j_map[x]] == j_map[mapping[x]] for x in range(SIZE))


def ideal_power_generators() -> tuple[Vector4, ...]:
    """Return the four public power-basis columns generating lambda^5 O."""

    matrix = _mat_pow(LAMBDA_MATRIX, DEPTH)
    return tuple(
        tuple(matrix[row][column] for row in range(4))
        for column in range(4)
    )  # type: ignore[return-value]


__all__ = [
    "ArithmeticCentralizerDescription",
    "CentralizerDescription",
    "CycleAction",
    "DEPTH",
    "J",
    "J_POWER_MATRIX",
    "LAMBDA",
    "LAMBDA4_RELATION",
    "LAMBDA_MATRIX",
    "Lambda5",
    "ONE",
    "PRIME",
    "SIZE",
    "ZERO",
    "ZETA_MATRIX",
    "centralizer_description",
    "arithmetic_centralizer_description",
    "centralizer_element",
    "centralizer_orbits",
    "commutes_with_j",
    "elements",
    "equivalent_power_vectors",
    "ideal_power_generators",
    "is_permutation",
    "iter_centralizer_generators",
    "iter_unit_multiplication_permutations",
    "j_orbit_coordinates",
    "j_orbit_spectrum",
    "j_orbits",
    "j_permutation",
    "lambda_to_power",
    "permutation_cycles",
    "power_to_lambda",
    "unit_multiplication_permutation",
    "units",
    "verify_arithmetic_centralizer",
    "verify_unit_multiplication",
]
