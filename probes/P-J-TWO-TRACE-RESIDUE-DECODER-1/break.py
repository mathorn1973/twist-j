#!/usr/bin/env python3
"""Independent exact L1 adversarial audit for the frozen preregistration.

Scientific exposure: PREREG.md only. Its target counts were disclosed;
implementation independence, not result blinding, is claimed. This file
imports no probe implementation and neither reads nor writes any files.
The finite box audit uses the preregistered mathematical coefficient bound;
it does not turn a finite search into an independent infinite-domain proof.

Original work under Apache-2.0.
"""

from collections import defaultdict
from hashlib import sha256
from itertools import combinations, product
import json


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
J = (1, 0, 1, 0)
J_INVERSE = (0, -1, -1, 0)
NORM_BOUND = 941
RESIDUE_MODULUS = 25


def _require(condition, detail):
    """Checks remain active under Python optimization flags."""
    if not condition:
        raise AssertionError(detail)


def _canonical(cyclic):
    """Reduce Z[C5] by 1+z+z^2+z^3+z^4, in the specified basis."""
    return tuple(cyclic[i] - cyclic[4] for i in range(4))


def _multiply(left, right):
    cyclic = [0, 0, 0, 0, 0]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            cyclic[(i + j) % 5] += x * y
    return _canonical(cyclic)


def _galois(value, exponent):
    """sigma_exponent(z)=z^exponent, for exponent in {1,2,3,4}."""
    cyclic = [0, 0, 0, 0, 0]
    for i, coefficient in enumerate(value):
        cyclic[(i * exponent) % 5] += coefficient
    return _canonical(cyclic)


def _plus(left, right):
    return tuple(x + y for x, y in zip(left, right))


def _rational(value, context):
    _require(value[1:] == (0, 0, 0), (context, value))
    return value[0]


def _absolute_square(value):
    return _multiply(value, _galois(value, 4))


def _trace_of_absolute_square(value):
    square = _absolute_square(value)
    # The two distinct real conjugates sum to Tr_K/Q(square)/2.
    return _rational(_plus(square, _galois(square, 2)), "real trace")


def _norm(value):
    """Norm from all four Galois images, without a coordinate formula."""
    accumulated = value
    for exponent in (2, 3, 4):
        accumulated = _multiply(accumulated, _galois(value, exponent))
    return _rational(accumulated, "four-conjugate norm")


def _inspect(value, check_neighbors=False):
    """Derive (u,v,N,S0,S1) and cross-check exact independent identities."""
    square = _absolute_square(value)
    u, v = square[0], -square[2]
    _require(square == (u, 0, -v, -v), ("real subfield", value, square))
    conjugate_square = _galois(square, 2)
    s0 = _rational(_plus(square, conjugate_square), "S0")
    shifted = _multiply(J, value)
    s1 = _trace_of_absolute_square(shifted)
    norm = _norm(value)
    _require(
        _multiply(square, conjugate_square) == (norm, 0, 0, 0),
        ("norm grouping", value),
    )
    _require(norm == u * u + u * v - v * v, ("norm coordinates", value))
    _require(5 * u == s0 + s1, ("u reconstruction", value))
    _require(5 * v == 3 * s0 - 2 * s1, ("v reconstruction", value))
    _require(
        5 * norm == 3 * s0 * s1 - s0 * s0 - s1 * s1,
        ("trace norm", value),
    )
    _require(s0 == 2 * u + v, ("S0 coordinates", value))
    _require(s1 == 3 * u - v, ("S1 coordinates", value))
    _require(
        (0 <= v < u) == (2 * s0 < 3 * s1 and 2 * s1 <= 3 * s0),
        ("strip inequalities", value),
    )
    if value == ZERO:
        _require((u, v, norm, s0, s1) == (0, 0, 0, 0, 0), "zero")
    else:
        _require(norm > 0 and s0 > 0 and s1 > 0 and u > 0,
                 ("total positivity", value))
    if check_neighbors:
        s2 = _trace_of_absolute_square(_multiply(J, shifted))
        sm1 = _trace_of_absolute_square(_multiply(J_INVERSE, value))
        _require(s2 == 3 * s1 - s0, ("forward recurrence", value))
        _require(sm1 == 3 * s0 - s1, ("backward recurrence", value))
    return u, v, norm, s0, s1


def _j_power(exponent):
    base = J if exponent >= 0 else J_INVERSE
    remaining = abs(exponent)
    accumulated = ONE
    while remaining:
        if remaining & 1:
            accumulated = _multiply(accumulated, base)
        remaining //= 2
        if remaining:
            base = _multiply(base, base)
    return accumulated


def _key(value, s0, s1, modulus):
    return (s0, s1) + tuple(coefficient % modulus for coefficient in value)


def _inverse(s0, s1, residue):
    """Invert an exact D_25 datum without consulting the enumerated strip.

    The real-coordinate descent and modular ring actions normalize the input.
    In either strict non-strip case the positive integer u decreases; the
    upper equality takes one step directly to the admitted lower boundary.
    Thus every syntactically admitted input is accepted or rejected finitely.
    The uniquely centered residue is then checked as an actual ring element.
    """
    if type(s0) is not int or type(s1) is not int:
        return None
    if not isinstance(residue, (tuple, list)) or len(residue) != 4:
        return None
    if any(type(c) is not int or not 0 <= c < RESIDUE_MODULUS for c in residue):
        return None
    if s0 <= 0 or s1 <= 0 or (s0 + s1) % 5:
        return None
    u = (s0 + s1) // 5
    v_numerator = 3 * s0 - 2 * s1
    if v_numerator % 5:
        return None
    v = v_numerator // 5
    norm = u * u + u * v - v * v
    if u <= 0 or not 0 < norm <= NORM_BOUND:
        return None

    normalized_residue = tuple(residue)
    exponent = 0
    while not 0 <= v < u:
        previous_u, previous_v = u, v
        if v < 0:
            u, v = u + v, u + 2 * v
            factor = J_INVERSE
            exponent += 1
        else:
            u, v = 2 * u - v, v - u
            factor = J
            exponent -= 1
        _require(u > 0, ("normalization positivity", previous_u, previous_v))
        _require(
            u < previous_u or (previous_v == previous_u and v == 0),
            ("normalization descent", previous_u, previous_v, u, v),
        )
        _require(u * u + u * v - v * v == norm, "normalization norm")
        normalized_residue = tuple(
            c % RESIDUE_MODULUS for c in _multiply(factor, normalized_residue)
        )

    beta = tuple(c if c <= 12 else c - RESIDUE_MODULUS
                 for c in normalized_residue)
    if any(abs(c) > 8 for c in beta):
        return None
    actual_u, actual_v, actual_norm, _, _ = _inspect(beta)
    if (actual_u, actual_v, actual_norm) != (u, v, norm):
        return None
    alpha = _multiply(_j_power(exponent), beta)
    _, _, reconstructed_norm, reconstructed_s0, reconstructed_s1 = _inspect(alpha)
    if reconstructed_norm != norm:
        return None
    if (reconstructed_s0, reconstructed_s1) != (s0, s1):
        return None
    if tuple(c % RESIDUE_MODULUS for c in alpha) != tuple(residue):
        return None
    return alpha, beta, exponent


def _basis_and_boundary_checks():
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    _require(_multiply(J, J_INVERSE) == ONE, "J inverse")
    _require(_multiply(J_INVERSE, J) == ONE, "inverse J")
    for element in basis:
        _require(_multiply(J_INVERSE, _multiply(J, element)) == element,
                 ("J inverse basis", element))
        _require(_multiply(J, _multiply(J_INVERSE, element)) == element,
                 ("inverse J basis", element))
        for exponent in (1, 2, 3, 4):
            for other in basis:
                _require(
                    _galois(_multiply(element, other), exponent)
                    == _multiply(_galois(element, exponent), _galois(other, exponent)),
                    ("Galois multiplicativity", element, other, exponent),
                )
        # Every basis root has u=1,v=0. J^-1 takes it to u=v=1.
        u, v, norm, s0, s1 = _inspect(element, check_neighbors=True)
        _require((u, v, norm) == (1, 0, 1), "included strip boundary")
        _require(_inverse(s0, s1, tuple(c % 25 for c in element))
                 == (element, element, 0), "lower boundary inverse")
        upper = _multiply(J_INVERSE, element)
        u, v, norm, s0, s1 = _inspect(upper, check_neighbors=True)
        _require((u, v, norm) == (1, 1, 1), "excluded strip boundary")
        _require(not 0 <= v < u, "upper boundary must be excluded")
        _require(_inverse(s0, s1, tuple(c % 25 for c in upper))
                 == (upper, element, -1), "upper boundary normalization")


def run_audit():
    """Return the complete preregistered JSON-compatible census and counts."""
    _basis_and_boundary_checks()
    scanned = 0
    strip = []
    facts = {}
    for value in product(range(-9, 10), repeat=4):
        scanned += 1
        u, v, norm, s0, s1 = _inspect(value, check_neighbors=True)
        if 0 < norm <= NORM_BOUND and 0 <= v < u:
            strip.append(value)
            facts[value] = (norm, s0, s1)
    strip.sort()
    _require(scanned == 130321, ("complete box size", scanned))
    _require(bool(strip), "empty strip")
    max_abs_coefficient = max(abs(c) for value in strip for c in value)
    _require(max_abs_coefficient <= 8,
             ("preregistered coefficient bound", max_abs_coefficient))

    fibres5 = defaultdict(list)
    fibres25 = defaultdict(list)
    trace_pairs = set()
    below = 0
    for value in strip:
        norm, s0, s1 = facts[value]
        below += int(norm <= 940)
        trace_pairs.add((s0, s1))
        fibres5[_key(value, s0, s1, 5)].append(value)
        fibres25[_key(value, s0, s1, 25)].append(value)
    _require(all(len(group) == 1 for group in fibres25.values()),
             "D25 strip injectivity")

    roundtrips = 0
    shifts = (-37, -2, 0, 3, 41)
    powers = {exponent: _j_power(exponent) for exponent in shifts}
    for beta in strip:
        for exponent in shifts:
            alpha = _multiply(powers[exponent], beta)
            _, _, norm, s0, s1 = _inspect(alpha, check_neighbors=True)
            _require(norm == facts[beta][0], ("shift norm", beta, exponent))
            residue = tuple(c % RESIDUE_MODULUS for c in alpha)
            decoded = _inverse(s0, s1, residue)
            _require(decoded == (alpha, beta, exponent),
                     ("round trip", beta, exponent, decoded))
            roundtrips += 1

    collision_differences = 0
    collision_groups = 0
    first_collision = None
    for key, group in sorted(fibres5.items()):
        group.sort()
        if len(group) < 2:
            continue
        collision_groups += 1
        first = (facts[group[0]][0], key, group[0], group[1])
        if first_collision is None or first < first_collision:
            first_collision = first
        for left, right in combinations(group, 2):
            _require(facts[left] == facts[right], ("collision trace/norm", left, right))
            difference = tuple(y - x for x, y in zip(left, right))
            _require(difference != ZERO and all(c % 5 == 0 for c in difference),
                     ("collision divisibility", left, right))
            difference_norm = _norm(difference)
            _require(5 ** 4 <= difference_norm <= 16 * facts[left][0],
                     ("collision norm bound", left, right, difference_norm))
            quotient = tuple(c // 5 for c in difference)
            _require(difference_norm == 5 ** 4 * _norm(quotient),
                     ("collision norm scaling", left, right))
            collision_differences += 1

    # This disclosed witness is checked directly, not used to build fibres.
    witness_left, witness_right = (0, 1, 1, -2), (0, 1, 1, 3)
    for witness in (witness_left, witness_right):
        _require(witness in facts, ("witness in strip", witness))
        _require(_inspect(witness) == (7, 1, 55, 15, 20),
                 ("exposed collision witness", witness))
    _require(tuple(y - x for x, y in zip(witness_left, witness_right))
             == (0, 0, 0, 5), "exposed witness difference")

    _require(first_collision is not None, "missing D5 collision")
    first_norm, first_key, first_left, first_right = first_collision
    strip_sha256 = sha256(
        json.dumps(strip, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    summary = {
        "bound": NORM_BOUND,
        "strip_count": len(strip),
        "strip_below": below,
        "strip_sha256": strip_sha256,
        "max_abs_coefficient": max_abs_coefficient,
        "trace_pair_count": len(trace_pairs),
        "mod5_key_count": len(fibres5),
        "mod25_key_count": len(fibres25),
        "mod5_collision_groups": collision_groups,
        "mod5_max_fibre": max(len(group) for group in fibres5.values()),
        "mod5_capacity_shortfall": max(0, 3125 - len(fibres5)),
        "mod5_first_collision": {
            "norm": first_norm,
            "key": list(first_key),
            "left": list(first_left),
            "right": list(first_right),
        },
    }
    _require((len(strip), below, len(trace_pairs), len(fibres5), len(fibres25), first_norm)
             == (3150, 3110, 145, 2603, 3150, 55),
             ("frozen exposed census", summary))
    _require(roundtrips == 15750, ("frozen roundtrip count", roundtrips))
    return {
        "summary": summary,
        "scanned": scanned,
        "roundtrips": roundtrips,
        "collision_differences": collision_differences,
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), sort_keys=True, separators=(",", ":")))
