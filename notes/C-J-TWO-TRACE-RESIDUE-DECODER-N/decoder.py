#!/usr/bin/env python3
"""Exact L1 scalar inversion, NON-CANONICAL; no physical apparatus claim.

Data: S(alpha), S(J*alpha), four coefficients modulo 25.
Domain: alpha != 0 in Z[zeta_5], algebraic norm <= 941.
The observed transition must be a pure J step.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict, dataclass
import json
from typing import Sequence

Scalar = tuple[int, int, int, int]
BOUND = 941
MODULUS = 25


class InvalidReading(ValueError):
    """The supplied data are not in the exact image of this reader."""


def step(x: Scalar) -> Scalar:
    a, b, c, d = x
    return a - c + d, b - c, a, b - c + d


def inverse_step(x: Scalar) -> Scalar:
    a, b, c, d = x
    return c, -a + c + d, -a - b + c + d, -b + d


def apply_steps(x: Scalar, exponent: int) -> Scalar:
    f = step if exponent >= 0 else inverse_step
    for _ in range(abs(exponent)):
        x = f(x)
    return x


def uv(x: Scalar) -> tuple[int, int]:
    a, b, c, d = x
    u = a*a - a*b + b*b - b*c + c*c - c*d + d*d
    v = a*b - a*c - a*d + b*c - b*d + c*d
    return u, v


def norm(x: Scalar) -> int:
    u, v = uv(x)
    return u*u + u*v - v*v


def trace_pair(x: Scalar) -> tuple[int, int]:
    u, v = uv(x)
    return 2*u + v, 3*u - v


def reading(x: Scalar, modulus: int = MODULUS) -> tuple[int, int, Scalar]:
    if type(modulus) is not int or modulus < 1:
        raise ValueError('modulus must be a positive integer')
    s0, s1 = trace_pair(x)
    return s0, s1, tuple(c % modulus for c in x)


@dataclass(frozen=True)
class Decoded:
    coefficients: Scalar
    unit_exponent: int
    strip_coefficients: Scalar
    norm: int


def decode(s0: int, s1: int, residue: Sequence[int]) -> Decoded:
    """Terminate with the unique domain element, or reject the data.

    The unbounded integer traces are part of the input. A valid reading
    changed into another valid reading cannot be detected by this routine.
    """
    if type(s0) is not int or type(s1) is not int:
        raise InvalidReading('traces must be integers, not approximate values')
    if s0 <= 0 or s1 <= 0 or (s0 + s1) % 5:
        raise InvalidReading('nonpositive or nonintegral trace pair')
    if not isinstance(residue, (tuple, list)) or len(residue) != 4:
        raise InvalidReading('exactly four canonical residues are required')
    if any(type(c) is not int or not 0 <= c < MODULUS for c in residue):
        raise InvalidReading('residues must be integers from 0 through 24')
    u, v = (s0 + s1)//5, (3*s0 - 2*s1)//5
    n = u*u + u*v - v*v
    if not 1 <= n <= BOUND:
        raise InvalidReading('algebraic norm is outside 1 through 941')
    original = (s0, s1, tuple(residue))
    r = tuple(residue)
    exponent = 0
    while True:
        u, v = (s0 + s1)//5, (3*s0 - 2*s1)//5
        if v >= 0 and u - v > 0:
            break
        if v < 0:
            s0, s1 = 3*s0 - s1, s0
            r = tuple(c % MODULUS for c in inverse_step(r))
            exponent += 1
        else:
            s0, s1 = s1, 3*s1 - s0
            r = tuple(c % MODULUS for c in step(r))
            exponent -= 1
    beta = tuple(c if c <= 12 else c - MODULUS for c in r)
    if any(abs(c) > 8 for c in beta):
        raise InvalidReading('normalized residue is outside the proved coefficient box')
    if trace_pair(beta) != (s0, s1) or norm(beta) != n:
        raise InvalidReading('residue and trace pair do not describe the same scalar')
    alpha = apply_steps(beta, exponent)
    if reading(alpha) != original:
        raise InvalidReading('reconstructed state does not reproduce the input')
    return Decoded(alpha, exponent, beta, n)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('s0', type=int)
    parser.add_argument('s1', type=int)
    parser.add_argument('residue', nargs=4, type=int, metavar='r')
    args = parser.parse_args()
    try:
        result = decode(args.s0, args.s1, args.residue)
    except InvalidReading as exc:
        parser.error(str(exc))
    print(json.dumps(asdict(result), sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
