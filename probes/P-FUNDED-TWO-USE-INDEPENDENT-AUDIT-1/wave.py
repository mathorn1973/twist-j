# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 A. M. Thorn
"""Independent exact classical wave/tape implementation for lane V.

NON-CANONICAL / conditional L1 audit.  This module is derived from the
declared classical contract, R1 equations, and A2 equations, not another
lane's implementation or output.  Importing constructs the frozen geometry;
all scientific audit functions require an explicit call after the pin.

Sparse fields store exactly the nonzero rational entries on lexicographic D.
The direct energy path uses L_D with its full Dirichlet diagonal.  The
contact-work path uses the separately expanded H expression.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import lcm
from typing import Iterable, Mapping

Q = Fraction
Point = tuple[int, int, int]
Vec = dict[int, Fraction]
Port = tuple[Fraction, Fraction, Fraction, Fraction]
ZERO_PORT: Port = (Q(0), Q(0), Q(0), Q(0))
Y: tuple[Point, ...] = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))
SHELL_WEIGHTS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}


def _point_sum(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


STENCIL: tuple[tuple[Point, int], ...] = tuple(
    (d, SHELL_WEIGHTS[sum(t * t for t in d)])
    for d in product(range(-4, 5), repeat=3)
    if sum(d) % 2 == 0 and sum(t * t for t in d) in SHELL_WEIGHTS
)
B_ZERO: tuple[Point, ...] = ((0, 0, 0),) + tuple(d for d, _ in STENCIL)
D: tuple[Point, ...] = tuple(sorted({
    _point_sum(_point_sum(y, d), e)
    for y in Y for d in B_ZERO for e in B_ZERO
}))
INDEX: dict[Point, int] = {site: i for i, site in enumerate(D)}
PORT_IDS: tuple[int, ...] = tuple(INDEX[y] for y in Y[:4])
_PORT_SET = frozenset(PORT_IDS)
_Y_IDS: tuple[int, ...] = tuple(INDEX[y] for y in Y)

# The finite restriction removes only off-domain neighbors.  It never
# subtracts their weights from the full diagonal 288/324 = 8/9.
_NEIGHBORS: tuple[tuple[tuple[int, int], ...], ...] = tuple(
    tuple((INDEX[target], weight) for delta, weight in STENCIL
          if (target := _point_sum(site, delta)) in INDEX)
    for site in D
)


def rational(value: Fraction | int) -> Fraction:
    """Accept only exact input types; in particular never convert a float."""
    if not isinstance(value, (int, Fraction)):
        raise TypeError("only int and Fraction are permitted")
    return Q(value)


def port(values: Iterable[Fraction | int]) -> Port:
    result = tuple(rational(value) for value in values)
    if len(result) != 4:
        raise ValueError("a port vector has exactly four coordinates")
    return result  # type: ignore[return-value]


def vector(values: Mapping[int, Fraction | int]) -> Vec:
    result = {}
    for i, value in values.items():
        if not isinstance(i, int) or not 0 <= i < len(D):
            raise ValueError("sparse vector index outside D")
        value = rational(value)
        if value:
            result[i] = value
    return result


def add(*vectors: Mapping[int, Fraction]) -> Vec:
    result: Vec = {}
    for values in vectors:
        for i, value in values.items():
            total = result.get(i, Q(0)) + value
            if total:
                result[i] = total
            else:
                result.pop(i, None)
    return result


def scale(values: Mapping[int, Fraction], scalar: Fraction | int) -> Vec:
    scalar = rational(scalar)
    if not scalar:
        return {}
    return {i: scalar * value for i, value in values.items() if value}


def sub(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Vec:
    return add(left, scale(right, -1))


def linear_combination(
    *terms: tuple[Fraction | int, Mapping[int, Fraction]],
) -> Vec:
    return add(*(scale(values, coefficient) for coefficient, values in terms))


def dot(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Fraction:
    if len(left) > len(right):
        left, right = right, left
    return sum((value * right[i] for i, value in left.items() if i in right), Q(0))


def norm2(values: Mapping[int, Fraction]) -> Fraction:
    return sum((value * value for value in values.values()), Q(0))


def port_add(left: Port, right: Port) -> Port:
    return port(a + b for a, b in zip(left, right))


def port_scale(values: Port, scalar: Fraction | int) -> Port:
    scalar = rational(scalar)
    return port(scalar * value for value in values)


def port_norm2(values: Port) -> Fraction:
    return sum((value * value for value in values), Q(0))


def P(values: Iterable[Fraction | int]) -> Vec:
    return {i: value for i, value in zip(PORT_IDS, port(values)) if value}


def PT(values: Mapping[int, Fraction]) -> Port:
    return port(values.get(i, Q(0)) for i in PORT_IDS)


def S(values: Iterable[Fraction | int]) -> Vec:
    z = port(values)
    mean = sum(z, Q(0)) / 5
    return {i: value for i, value in zip(_Y_IDS, tuple(v - mean for v in z) + (-mean,))
            if value}


def K(values: Mapping[int, Fraction]) -> Vec:
    return {i: value / 2 if i in _PORT_SET else value
            for i, value in values.items() if value}


def J0(values: Mapping[int, Fraction]) -> Vec:
    return {i: value for i, value in values.items()
            if i not in _PORT_SET and value}


def _key(values: Mapping[int, Fraction]) -> tuple[tuple[int, Fraction], ...]:
    return tuple(sorted((i, rational(value)) for i, value in values.items() if value))


def _integers(key: tuple[tuple[int, Fraction], ...]) -> tuple[int, list[tuple[int, int]]]:
    denominator = lcm(*(value.denominator for _, value in key))
    return denominator, [(i, value.numerator * (denominator // value.denominator))
                         for i, value in key]


@lru_cache(maxsize=256)
def _h_cached(key: tuple[tuple[int, Fraction], ...]) -> tuple[tuple[int, Fraction], ...]:
    denominator, entries = _integers(key)
    totals: dict[int, int] = {}
    for i, value in entries:
        totals[i] = totals.get(i, 0) + 360 * value
        for j, weight in _NEIGHBORS[i]:
            totals[j] = totals.get(j, 0) + weight * value
    return tuple((i, Q(value, 324 * denominator)) for i, value in totals.items() if value)


def H(values: Mapping[int, Fraction]) -> Vec:
    """H=2I-L_D, using integer stencil sums then rational normalization."""
    return dict(_h_cached(_key(values)))


def L(values: Mapping[int, Fraction]) -> Vec:
    """Direct full-diagonal Dirichlet L_D; does not call H or contact work."""
    denominator, entries = _integers(_key(values))
    totals: dict[int, int] = {}
    for i, value in entries:
        totals[i] = totals.get(i, 0) + 288 * value
        for j, weight in _NEIGHBORS[i]:
            totals[j] = totals.get(j, 0) - weight * value
    return {i: Q(value, 324 * denominator) for i, value in totals.items() if value}


@dataclass(frozen=True)
class X:
    u: Vec
    v: Vec
    A0: Port = ZERO_PORT
    A1: Port = ZERO_PORT
    B0: Port = ZERO_PORT
    B1: Port = ZERO_PORT
    k: int = 0

    def __post_init__(self) -> None:
        # Copies prevent argument aliasing.  Fields are treated as immutable
        # by every operation in this module; no operation mutates an input.
        object.__setattr__(self, "u", vector(self.u))
        object.__setattr__(self, "v", vector(self.v))
        for name in ("A0", "A1", "B0", "B1"):
            object.__setattr__(self, name, port(getattr(self, name)))
        if not isinstance(self.k, int) or self.k not in (0, 1):
            raise ValueError("pointer k must be 0 or 1")


def zero_X(c0: Port = ZERO_PORT, c1: Port = ZERO_PORT) -> X:
    return X({}, {}, B0=c0, B1=c1)


def F(state: X) -> X:
    w = K(linear_combination((1, H(state.v)), (-1, J0(state.u)), (4, P(state.A0))))
    outgoing = port_add(state.A0, port_scale(PT(sub(w, state.u)), -Q(1, 2)))
    return X(state.v, w, state.A1, state.B1, outgoing, state.B0, 1 - state.k)


def F_inv(state: X) -> X:
    # Here state.u=v and state.v=w in the forward coupling notation.
    old_u = K(linear_combination((1, H(state.u)), (-1, J0(state.v)), (4, P(state.B0))))
    old_a = port_add(state.B0, port_scale(PT(sub(state.v, old_u)), Q(1, 2)))
    return X(old_u, state.u, old_a, state.A0, state.B1, state.A1, 1 - state.k)


def wave_energy(u: Mapping[int, Fraction], v: Mapping[int, Fraction]) -> Fraction:
    """Definition E_D directly: (||v-u||^2 + u^T L_D v)/2."""
    return (norm2(sub(v, u)) + dot(u, L(v))) / 2


def energy(state: X) -> Fraction:
    return wave_energy(state.u, state.v) + 2 * sum(
        (port_norm2(values) for values in (state.A0, state.A1, state.B0, state.B1)), Q(0)
    )


def contact_delta(
    u: Mapping[int, Fraction], v: Mapping[int, Fraction],
    sigma: int, z: Iterable[Fraction | int],
) -> Fraction:
    """Expanded contact work, deliberately separate from direct energy."""
    if not isinstance(sigma, int) or sigma not in (-1, 1):
        raise ValueError("contact direction must be -1 or +1")
    a = S(z)
    return norm2(a) / 2 + sigma * dot(a, sub(v, scale(H(u), Q(1, 2))))


def audit_geometry() -> dict[str, int]:
    """Exact geometry and every finite matrix coefficient; call post-pin."""
    if len(D) != 869 or tuple(sorted(D)) != D:
        raise AssertionError("wrong finite causal domain or ordering")
    if len(STENCIL) != 60 or sum(weight for _, weight in STENCIL) != 288:
        raise AssertionError("wrong full stencil")
    if any(sum(site) % 2 for site in D):
        raise AssertionError("D contains a point outside D3")
    checked = 0
    for i, neighbors in enumerate(_NEIGHBORS):
        for j, weight in neighbors:
            if (i, weight) not in _NEIGHBORS[j]:
                raise AssertionError("finite H/L coefficient matrix is asymmetric")
            checked += 1
    return {"domain_sites": len(D), "stencil_sites": len(STENCIL),
            "symmetric_directed_offdiagonal_coefficients": checked,
            "retained_full_diagonal_coefficients": len(D)}


def _amplitude_basis() -> Iterable[X]:
    for i in range(len(D)):
        yield X({i: Q(1)}, {})
        yield X({}, {i: Q(1)})
    for name in ("A0", "A1", "B0", "B1"):
        for j in range(4):
            yield X({}, {}, **{name: port(int(i == j) for i in range(4))})


def audit_inverse_basis() -> dict[str, int]:
    """Coefficient-complete linear inverse and coupling-identity audit.

    Every amplitude column of both composition maps is tested.  In addition,
    the local identity w+u-Hv=2P(a+b) is checked on every column; together
    with symmetric H and b=a-P^T(w-u)/2 this proves the energy identity
    algebraically (see PROOF.md), including all cross terms.  This does not
    claim that merely comparing energy on unit vectors covers cross terms.
    """
    count = 0
    for state in _amplitude_basis():
        forward = F(state)
        if F_inv(forward) != state or F(F_inv(state)) != state:
            raise AssertionError("F inverse composition failed on an amplitude column")
        residual = linear_combination(
            (1, forward.v), (1, state.u), (-1, H(state.v)),
            (-2, P(port_add(state.A0, forward.B0))),
        )
        if residual:
            raise AssertionError("coupling energy identity failed on an amplitude column")
        count += 1
    for k in (0, 1):
        state = X({}, {}, k=k)
        if F_inv(F(state)) != state or F(F_inv(state)) != state:
            raise AssertionError("F inverse pointer composition failed")
    if count != 2 * len(D) + 16:
        raise AssertionError("incomplete amplitude basis")
    return {"amplitude_columns": count, "inverse_compositions": 2 * count,
            "coupling_identity_columns": count, "zero_pointer_compositions": 4}
