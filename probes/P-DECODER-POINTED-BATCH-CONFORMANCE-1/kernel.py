"""Autonomous Canon U and the direct cyclotomic five-field QDD write.

The n>0 head adapter is an explicit new dictionary choice. On K_QDD (n=0)
the direct write uses only the first four head coordinates. No quadratic
factor interface, apparatus output or later checkpoint enters this write.
"""

from dataclasses import dataclass
from fractions import Fraction


Checkpoint = tuple[int, tuple[int, int, int, int, int, int]]
Field = tuple[Fraction, Fraction, Fraction, Fraction]
Matrix4 = tuple[tuple[Fraction, ...], ...]


def validate_head(head: Checkpoint) -> Checkpoint:
    if (type(head) is not tuple or len(head) != 2
            or type(head[0]) is not int or head[0] < 0
            or type(head[1]) is not tuple or len(head[1]) != 6
            or any(type(x) is not int or not 0 <= x < 5 for x in head[1])):
        raise ValueError("head must be (nonnegative integer, six pentits)")
    return head


def theta(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("theta requires a nonnegative integer")
    return n.bit_count() % 2


def generator(index: int, x: tuple[int, ...]) -> tuple[int, ...]:
    validate_head((0, x))
    if type(index) is not int or not 0 <= index < 5:
        raise ValueError("generator index must lie in 0..4")
    p, s, pp, sp, q, r = x
    if index == 0:
        y = (s, p, sp, pp, q, r)
    elif index == 1:
        y = (-pp, -sp, -p, -s, -q, -r)
    elif index == 2:
        y = (2 - pp, 1 - sp + r, 2 - p, 1 - s - r, 1 - q, -r)
    elif index == 3:
        y = tuple(c - z for c, z in zip((2, 1, 3, 4, 1, 1), x))
    else:
        y = tuple(c - z for c, z in zip((2, 1, 3, 4, 2, 1), x))
    return tuple(z % 5 for z in y)


def u_step(head: Checkpoint) -> Checkpoint:
    n, x = validate_head(head)
    return n + 1, generator((sum(x) + 2 * theta(n)) % 5, x)


def balanced_head(head: Checkpoint) -> tuple[int, int, int, int]:
    _, x = validate_head(head)
    return tuple(z if z <= 2 else z - 5 for z in x[:4])


def linear_tr4(checkpoint: Checkpoint) -> int:
    """The registered piston-sum covector over F5, not field trace."""
    _, x = validate_head(checkpoint)
    return sum(x[:4]) % 5


def field_mul(x: Field, y: Field) -> Field:
    coefficients = [Fraction(0)] * 5
    for i in range(4):
        for j in range(4):
            coefficients[(i + j) % 5] += x[i] * y[j]
    return tuple(coefficients[i] - coefficients[4] for i in range(4))


def field_conjugate(x: Field) -> Field:
    coefficients = [Fraction(0)] * 5
    for i in range(4):
        coefficients[(4 * i) % 5] += x[i]
    return tuple(coefficients[i] - coefficients[4] for i in range(4))


def field_trace(x: Field) -> Fraction:
    return 4 * x[0] - x[1] - x[2] - x[3]


def trace_pairing(x: Field, y: Field) -> Fraction:
    return field_trace(field_mul(x, field_conjugate(y))) / 5


@dataclass(frozen=True, slots=True)
class Density:
    matrix: Matrix4


@dataclass(frozen=True, slots=True)
class Normalized:
    weights: tuple[Fraction, Fraction]


@dataclass(frozen=True, slots=True)
class QDDRecord:
    support_state: str
    total_weight: Fraction
    branch_weights: tuple[Fraction, Fraction]
    density_state: Density | str
    normalized_weight_state: Normalized | str


def direct_qdd(head: Checkpoint) -> QDDRecord:
    """Direct field-level rule; exactly the original five slots.

    Counter and last two pentits are validated but have no value dependency.
    On a nonzero-counter head, applying this rule is the declared reset-anchor
    extension, not an extension theorem for ALGEBRAIC-DMATTER.
    """
    w = tuple(Fraction(z) for z in balanced_head(head))
    zero = Fraction(0)
    if not any(w):
        return QDDRecord("ZERO_SUPPORT", zero, (zero, zero),
                         "ZERO_DENOMINATOR", "ZERO_DENOMINATOR")
    lam = (Fraction(1),) * 4
    m = trace_pairing(w, w)
    low_coefficient = trace_pairing(w, lam) / trace_pairing(lam, lam)
    low = tuple(low_coefficient * z for z in lam)
    high = tuple(z - ell for z, ell in zip(w, low))
    weights = (trace_pairing(low, low), trace_pairing(high, high))
    basis = tuple(tuple(Fraction(i == j) for i in range(4)) for j in range(4))
    columns = tuple(tuple(z * trace_pairing(e, w) / m for z in w) for e in basis)
    density = tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))
    return QDDRecord("SUPPORTED", m, weights, Density(density),
                     Normalized(tuple(weight / m for weight in weights)))
