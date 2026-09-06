"""Accepted exact circuit; NON-CANONICAL, zero runs at pin, no physical claim.

The production path uses path mixing, cell permutations and a flag permutation.
It never calls a system projector. Coordinates are (path, flag, cell), with
flat index 10*path + 5*flag + cell. Every scalar is an int or Fraction.
"""

from fractions import Fraction


W = tuple(tuple(Fraction(x, 2) for x in row) for row in (
    (1, 1, 1, 1), (1, -1, 1, -1),
    (1, 1, -1, -1), (1, -1, -1, 1),
))


def _scalars(values, length):
    if not isinstance(values, tuple) or len(values) != length:
        raise ValueError("wrong rational tuple shape")
    if any(type(x) not in (int, Fraction) for x in values):
        raise ValueError("only exact rational scalars are admitted")
    return tuple(Fraction(x) for x in values)


def system_vector(v):
    v = _scalars(v, 5)
    if sum(v, Fraction(0)):
        raise ValueError("system vector must have zero sum")
    return v


def q(v):
    """Squared Euclidean norm on the declared five-cell zero-sum carrier."""
    return sum((x * x for x in system_vector(v)), Fraction(0))


def _setting(k):
    if type(k) is not int or not 0 <= k < 5:
        raise ValueError("setting must be an integer in F_5")


def _mixer(a):
    if not isinstance(a, tuple) or len(a) != 4:
        raise ValueError("mixer shape")
    a = tuple(_scalars(row, 4) for row in a)
    if any(sum((a[r][i] * a[r][j] for r in range(4)), Fraction(0))
           != int(i == j) for i in range(4) for j in range(4)):
        raise ValueError("mixer must be rational orthogonal")
    return a


def _mix(state, a):
    return tuple(
        sum((a[r][s] * state[10*s + 5*b + x] for s in range(4)), Fraction(0))
        for r in range(4) for b in range(2) for x in range(5)
    )


def prepare(v, flag=0):
    v = system_vector(v)
    if type(flag) is not int or flag not in (0, 1):
        raise ValueError("binary flag required")
    return tuple(v[x] if r == 0 and b == flag else Fraction(0)
                 for r in range(4) for b in range(2) for x in range(5))


def apply_v(state, k, inverse=False, mixer=W, order=(0, 1, 2, 3)):
    """Apply A^T diag(g^order[r]) A, or its exact inverse, on 40 modes."""
    state = _scalars(state, 40)
    _setting(k)
    if type(inverse) is not bool:
        raise ValueError("inverse flag must be boolean")
    if (not isinstance(order, tuple) or len(order) != 4
            or any(type(x) is not int for x in order)
            or sorted(order) != [0, 1, 2, 3]):
        raise ValueError("each group power must occur exactly once")
    a = _mixer(mixer)
    split = _mix(state, a)
    routed = [Fraction(0)] * 40
    for r in range(4):
        multiplier = pow(2, (-order[r] if inverse else order[r]) % 4, 5)
        for b in range(2):
            for x in range(5):
                destination = (k + multiplier * (x - k)) % 5
                routed[10*r + 5*b + destination] = split[10*r + 5*b + x]
    transpose = tuple(tuple(a[j][i] for j in range(4)) for i in range(4))
    return _mix(tuple(routed), transpose)


def apply_flag(state):
    state = _scalars(state, 40)
    return tuple(state[10*r + 5*(b ^ int(r != 0)) + x]
                 for r in range(4) for b in range(2) for x in range(5))


def apply_e(state, k, mixer=W, order=(0, 1, 2, 3)):
    before = apply_v(state, k, mixer=mixer, order=order)
    flagged = apply_flag(before)
    return apply_v(flagged, k, inverse=True, mixer=mixer, order=order)


def apply_r(state, k, mixer=W, order=(0, 1, 2, 3)):
    """Coarse control with retained fine paths and a redundant binary flag."""
    return apply_flag(apply_v(state, k, mixer=mixer, order=order))


def terminal(k, variant, v):
    """Return actual circuit outputs: E=(LOW,HIGH), R=(path0,...,path3)."""
    return terminal_with_mixer(k, variant, v, W, (0, 1, 2, 3))


def terminal_with_mixer(k, variant, v, mixer, order):
    state = prepare(v)
    if variant == "E":
        out = apply_e(state, k, mixer, order)
        if any(out[10:]):
            raise ArithmeticError("uncompute left a nonzero auxiliary path")
        return tuple(tuple(out[5*b + x] for x in range(5)) for b in range(2))
    if variant == "R":
        out = apply_r(state, k, mixer, order)
        if any(out[10*r + 5*(1-int(r != 0)) + x]
               for r in range(4) for x in range(5)):
            raise ArithmeticError("inconsistent path flag")
        return tuple(tuple(out[10*r + 5*int(r != 0) + x] for x in range(5))
                     for r in range(4))
    raise ValueError("variant must be E or R")


def branch_of_channel(variant, channel):
    if variant == "E" and type(channel) is int and 0 <= channel < 2:
        return channel
    if variant == "R" and type(channel) is int and 0 <= channel < 4:
        return int(channel != 0)
    raise ValueError("invalid variant or channel")
