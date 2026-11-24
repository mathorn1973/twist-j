"""Independent exact u-basis snapshots of the two-contact clock completion.

A data state is three four-integer tuples in the basis 1,u,u^2,u^3,
where u=1-j. A complete snapshot is (data,bank,hand,q,p). The hand is a
Fraction modulo 6, independently representing the primary half-window hand.
Controller quarter turns and cyclotomic multipliers are exact. This module
neither searches nor imports any preceding scientific probe.
"""

from fractions import Fraction


TRACE_GRAM = ((4, 5, 5, 5),
              (5, 10, 15, 20),
              (5, 15, 30, 50),
              (5, 20, 50, 100))
MULTIPLIERS = {
    "full": (1, -2, 1, 0),              # j^2
    "half": (-1, 1, 0, 0),             # -j
    "inverse": (1, -3, 3, -1),         # j^3
    "inverse_half": (4, -6, 4, -1),    # -j^4
}


def add(x, y):
    return tuple(x[i] + y[i] for i in range(4))


def subtract(x, y):
    return tuple(x[i] - y[i] for i in range(4))


def scale(x, factor):
    return tuple(factor * a for a in x)


def mul(x, y):
    """Convolve and reduce by u^4-5u^3+10u^2-10u+5."""
    product = [0] * 7
    for i in range(4):
        for k in range(4):
            product[i + k] += x[i] * y[k]
    for degree in range(6, 3, -1):
        value = product[degree]
        product[degree] = 0
        shift = degree - 4
        product[shift] -= 5 * value
        product[shift + 1] += 10 * value
        product[shift + 2] -= 10 * value
        product[shift + 3] += 5 * value
    return tuple(product[:4])


def _basis_change(x):
    a, b, c, d = x
    return (a + b + c + d, -b - 2 * c - 3 * d, c + 3 * d, -d)


def from_power(data):
    """Substitute j=1-u. This triangular basis change is an involution."""
    return tuple(_basis_change(v) for v in data)


def to_power(data):
    """Substitute u=1-j in the complete data state."""
    return tuple(_basis_change(v) for v in data)


def q(v):
    """Q(v)=Tr(v*conjugate(v))/2, using the independent u-trace Gram."""
    trace = sum(v[i] * TRACE_GRAM[i][k] * v[k]
                for i in range(4) for k in range(4))
    if trace % 2:
        raise ArithmeticError("nonintegral half-trace account")
    return trace // 2


def R(data):
    return sum(q(v) for v in data)


def I(data):
    return q(subtract(data[0], data[1])) + q(subtract(data[1], data[2]))


def parity(data, edge):
    i, k = edge
    return all(a % 2 == 0 for a in subtract(data[i], data[k]))


def _half(v):
    if any(a % 2 for a in v):
        raise ArithmeticError("nonintegral contact snapshot")
    return tuple(a // 2 for a in v)


def contact(data, edge, multiplier="full", admitted=True):
    """Exact selected pair map, including the declared half-step scalars."""
    if type(admitted) is not bool:
        raise ValueError("admission flag must be Boolean")
    if not admitted:
        return data
    if not parity(data, edge):
        raise ArithmeticError("active contact lacks integral admission")
    i, k = edge
    total = add(data[i], data[k])
    rotated = mul(MULTIPLIERS[multiplier], subtract(data[i], data[k]))
    output = list(data)
    output[i] = _half(add(total, rotated))
    output[k] = _half(subtract(total, rotated))
    return tuple(output)


def control_energy(ctrl_q, ctrl_p):
    return 4 * ((Fraction(ctrl_q) - Fraction(1, 2)) ** 2 + Fraction(ctrl_p) ** 2)


def base_energy(data, ctrl_q, ctrl_p, lam):
    return R(data) + lam * I(data) + control_energy(ctrl_q, ctrl_p)


def energy(state, lam):
    data, bank, _hand, ctrl_q, ctrl_p = state
    return base_energy(data, ctrl_q, ctrl_p, lam) + bank


def _controller_turn(ctrl_q, ctrl_p, amount):
    """Exact exp of the clockwise generator [[0,1],[-1,0]]."""
    x, y = Fraction(ctrl_q) - Fraction(1, 2), Fraction(ctrl_p)
    if amount == Fraction(1, 2):
        matrix = ((0, 1), (-1, 0))
    elif amount == Fraction(-1, 2):
        matrix = ((0, -1), (1, 0))
    elif amount in (Fraction(1), Fraction(-1)):
        matrix = ((-1, 0), (0, -1))
    else:
        raise ValueError("unsupported normalized pulse amount")
    new_x = matrix[0][0] * x + matrix[0][1] * y
    new_y = matrix[1][0] * x + matrix[1][1] * y
    return new_x + Fraction(1, 2), new_y


def pulse(state, edge, kind, lam, amount=Fraction(1)):
    """Audit one full/half pulse or its inverse on the prepared snapshot class.

    The compute and uncompute Hamiltonians have the same exact quarter-turn
    action. A contact pulse requires a coherent logical controller at q=0/1,
    p=0. No claim about arbitrary real off-ready states is made by this audit.
    Bank compensation includes the complete data and controller energy.
    """
    amount = Fraction(amount)
    if amount not in (Fraction(1), Fraction(-1), Fraction(1, 2), Fraction(-1, 2)):
        raise ValueError("unsupported normalized pulse amount")
    data, bank, hand, ctrl_q, ctrl_p = state
    before = base_energy(data, ctrl_q, ctrl_p, lam)
    admitted = parity(data, edge)
    if kind in ("compute", "uncompute"):
        if admitted:
            ctrl_q, ctrl_p = _controller_turn(ctrl_q, ctrl_p, amount)
    elif kind == "contact":
        if ctrl_q != int(admitted) or ctrl_p != 0:
            raise ArithmeticError("contact controller is not the coherent parity bit")
        if amount == Fraction(1):
            multiplier = "full"
        elif amount == Fraction(-1):
            multiplier = "inverse"
        elif amount == Fraction(1, 2):
            multiplier = "half"
        else:
            multiplier = "inverse_half"
        data = contact(data, edge, multiplier, admitted)
    else:
        raise ValueError("unknown pulse kind")
    after = base_energy(data, ctrl_q, ctrl_p, lam)
    return (data, bank + before - after, (Fraction(hand) + amount) % 6,
            Fraction(ctrl_q), Fraction(ctrl_p))
