#!/usr/bin/env python3
"""Exact lambda-six scalar interface for pure J multiplication, L1 only.

No computation is performed on import. The finite strip index is derived
lazily from the complete proved box, not loaded from an external oracle.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from functools import lru_cache
from itertools import product
import json
import sys

Scalar = tuple[int, int, int, int]
Digits = tuple[int, int, int, int, int, int]
Reading = tuple[int, int, Digits]
BOUND = 941
DEPTH = 6


class InvalidReading(ValueError):
    """Malformed data or data outside the exact image of the reader."""


def _integers(value, length: int, name: str, error=ValueError) -> tuple:
    if not isinstance(value, (tuple, list)) or len(value) != length:
        raise error(f'{name} must be a tuple or list of length {length}')
    if any(type(c) is not int for c in value):
        raise error(f'{name} must contain exact integers, excluding bool')
    return tuple(value)


def _reading(s0, s1, digits) -> Reading:
    if type(s0) is not int or type(s1) is not int:
        raise InvalidReading('traces must be exact integers, excluding bool')
    r = _integers(digits, DEPTH, 'digits', InvalidReading)
    if any(c < 0 or c > 4 for c in r):
        raise InvalidReading('digits must be canonical integers from 0 to 4')
    return s0, s1, r


def uv(x: Scalar) -> tuple[int, int]:
    a, b, c, d = x
    return (a*a - a*b + b*b - b*c + c*c - c*d + d*d,
            a*b - a*c - a*d + b*c - b*d + c*d)


def norm(x: Scalar) -> int:
    u, v = uv(x)
    return u*u + u*v - v*v


def trace_pair(x: Scalar) -> tuple[int, int]:
    u, v = uv(x)
    return 2*u + v, 3*u - v


def step(x: Scalar) -> Scalar:
    a, b, c, d = x
    return a-c+d, b-c, a, b-c+d


def inverse_step(x: Scalar) -> Scalar:
    a, b, c, d = x
    return c, -a+c+d, -a-b+c+d, -b+d


def apply_steps(x: Scalar, exponent: int) -> Scalar:
    if type(exponent) is not int:
        raise ValueError('exponent must be an exact integer, excluding bool')
    f = step if exponent >= 0 else inverse_step
    for _ in range(abs(exponent)):
        x = f(x)
    return x


def _lambda_times(x: Scalar) -> Scalar:
    a, b, c, d = x
    return a+d, b-a+d, c-b+d, 2*d-c


def _digits(x: Scalar) -> Digits:
    answer = []
    for _ in range(DEPTH):
        r = sum(x) % 5
        answer.append(r)
        a, b, c, d = x
        a -= r
        t = (a+b+c+d)//5
        x = a-t, a+b-2*t, a+b+c-3*t, t
    return tuple(answer)


def _representative(r: Digits) -> Scalar:
    x = (0, 0, 0, 0)
    for digit in reversed(r):
        a, b, c, d = _lambda_times(x)
        x = a+digit, b, c, d
    return x


def residue_digits(alpha) -> Digits:
    """Canonical lambda-six digits of any integral scalar, including zero."""
    return _digits(_integers(alpha, 4, 'scalar'))


def residue_representative(digits) -> Scalar:
    """The exact integral representative sum_i digits[i]*lambda**i."""
    return _representative(_reading(0, 0, digits)[2])


@lru_cache(maxsize=31250)
def _transport(r: Digits, forward: bool) -> Digits:
    f = step if forward else inverse_step
    return _digits(f(_representative(r)))


def T6(s0, s1, digits) -> Reading:
    """Forward pure-J data step on all syntactically well-formed readings."""
    s0, s1, r = _reading(s0, s1, digits)
    return s1, 3*s1-s0, _transport(r, True)


def T6_inverse(s0, s1, digits) -> Reading:
    """Inverse pure-J data step on all syntactically well-formed readings."""
    s0, s1, r = _reading(s0, s1, digits)
    return 3*s0-s1, s0, _transport(r, False)


def encode(alpha) -> Reading:
    """Encode exactly the nonzero integral norm-at-most-941 domain."""
    x = _integers(alpha, 4, 'scalar')
    if not 1 <= norm(x) <= BOUND:
        raise ValueError('scalar norm must be between 1 and 941')
    return *trace_pair(x), _digits(x)


@lru_cache(maxsize=1)
def _strip_index() -> dict[Reading, Scalar]:
    index = {}
    for x in product(range(-8, 9), repeat=4):
        u, v = uv(x)
        if 0 <= v < u and 1 <= u*u+u*v-v*v <= BOUND:
            key = (2*u+v, 3*u-v, _digits(x))
            if key in index:
                raise ArithmeticError('proved lambda-six injectivity failed')
            index[key] = x
    return index


@dataclass(frozen=True)
class Decoded:
    coefficients: Scalar
    strip_coefficients: Scalar
    unit_exponent: int
    norm: int


def decode(s0, s1, digits) -> Decoded:
    """Terminate with exact original/strip/exponent data, or reject.

    Termination precedes any scalar-representability test: the positive
    integer 2*u + int(v >= u) strictly decreases at each normalization step.
    """
    original = _reading(s0, s1, digits)
    s0, s1, r = original
    if s0 <= 0 or s1 <= 0 or (s0+s1) % 5:
        raise InvalidReading('nonpositive or nonintegral trace pair')
    u, v = (s0+s1)//5, (3*s0-2*s1)//5
    n = u*u+u*v-v*v
    if not 1 <= n <= BOUND:
        raise InvalidReading('norm is outside 1 through 941')
    exponent = 0
    while True:
        u, v = (s0+s1)//5, (3*s0-2*s1)//5
        if 0 <= v < u:
            break
        if v < 0:
            s0, s1, r = T6_inverse(s0, s1, r)
            exponent += 1
        else:
            s0, s1, r = T6(s0, s1, r)
            exponent -= 1
    beta = _strip_index().get((s0, s1, r))
    if beta is None:
        raise InvalidReading('normalized trace and residue have no scalar')
    alpha = apply_steps(beta, exponent)
    if encode(alpha) != original:
        raise ArithmeticError('exact reconstruction invariant failed')
    return Decoded(alpha, beta, exponent, n)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('encode', 'decode', 'forward', 'backward'))
    parser.add_argument('integers', type=int, nargs='+')
    args = parser.parse_args()
    try:
        if args.operation == 'encode':
            result = encode(args.integers)
        else:
            if len(args.integers) != 8:
                raise InvalidReading('expected two traces and six digits')
            s0, s1, *r = args.integers
            f = {'decode': decode, 'forward': T6, 'backward': T6_inverse}[args.operation]
            result = f(s0, s1, r)
            if isinstance(result, Decoded):
                result = asdict(result)
    except ValueError as exc:
        parser.error(str(exc))
    sys.stdout.buffer.write((json.dumps(result, sort_keys=True, separators=(',', ':')) + '\n').encode('utf-8'))


if __name__ == '__main__':
    main()
