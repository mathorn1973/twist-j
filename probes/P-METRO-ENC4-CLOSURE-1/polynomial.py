"""Exact univariate Q[x], with ascending coefficient tuples."""

from collections import Counter
from fractions import Fraction
from itertools import count, product
from math import gcd, isqrt, lcm


def trim(poly):
    values = list(map(Fraction, poly))
    while len(values) > 1 and not values[-1]:
        values.pop()
    return tuple(values) or (Fraction(0),)


ZERO = trim(())
ONE = trim((1,))


def add(a, b):
    result = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        result[i] += value
    for i, value in enumerate(b):
        result[i] += value
    return trim(result)


def scale(a, value):
    return trim(x * value for x in a)


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return trim(result)


def divmod_poly(a, b):
    remainder, divisor = trim(a), trim(b)
    if divisor == ZERO:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [Fraction(0)] * max(1, len(remainder) - len(divisor) + 1)
    while remainder != ZERO and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] = coefficient
        remainder = sub(remainder, (Fraction(0),) * degree + scale(divisor, coefficient))
    return trim(quotient), remainder


def mod(a, b):
    return divmod_poly(a, b)[1]


def xgcd(a, b):
    """Return monic gcd g and coefficients s,t such that s*a+t*b=g."""
    a, b = trim(a), trim(b)
    s, t = ONE, ZERO
    u, v = ZERO, ONE
    while b != ZERO:
        q, remainder = divmod_poly(a, b)
        a, b = b, remainder
        s, u = u, sub(s, mul(q, u))
        t, v = v, sub(t, mul(q, v))
    if a == ZERO:
        return ZERO, ZERO, ZERO
    factor = 1 / a[-1]
    return scale(a, factor), scale(s, factor), scale(t, factor)


def power(a, exponent):
    if exponent < 0:
        raise ValueError("negative polynomial exponent")
    result = ONE
    while exponent:
        if exponent & 1:
            result = mul(result, a)
        exponent >>= 1
        if exponent:
            a = mul(a, a)
    return result


def evaluate(poly, x):
    answer = 0
    for coefficient in reversed(poly):
        answer = answer * x + coefficient
    return answer


def primitive(poly):
    denominator = lcm(*(x.denominator for x in poly))
    integer = tuple(int(x * denominator) for x in poly)
    content = gcd(*integer)
    sign = 1 if integer[-1] > 0 else -1
    return tuple(sign * x // content for x in integer)


def signed_divisors(n):
    absolute = abs(n)
    positive = set()
    for divisor in range(1, isqrt(absolute) + 1):
        if absolute % divisor == 0:
            positive.update((divisor, absolute // divisor))
    return tuple(sign * divisor for divisor in sorted(positive) for sign in (1, -1))


def interpolation_basis(points):
    basis = []
    for x in points:
        poly = ONE
        denominator = 1
        for y in points:
            if y != x:
                poly = mul(poly, trim((-y, 1)))
                denominator *= x - y
        basis.append(scale(poly, Fraction(1, denominator)))
    return basis


def sample_points(poly, needed):
    """Choose small nonzero evaluations from a finite oversized sample."""
    candidates = []
    for radius in count():
        for x in (0,) if radius == 0 else (radius, -radius):
            value = evaluate(poly, x)
            if value:
                candidates.append((abs(value), x, value))
        if len(candidates) >= 2 * needed:
            break
    return sorted(candidates)[:needed]


def proper_factor(poly):
    integer = primitive(poly)
    for degree in range(1, (len(poly) - 1) // 2 + 1):
        samples = sample_points(integer, degree + 1)
        basis = interpolation_basis([x for _, x, _ in samples])
        for values in product(*(signed_divisors(value) for _, _, value in samples)):
            candidate = ZERO
            for value, term in zip(values, basis):
                candidate = add(candidate, scale(term, value))
            if len(candidate) != degree + 1 or candidate[-1] <= 0:
                continue
            if any(x.denominator != 1 for x in candidate):
                continue
            if gcd(*(int(x) for x in candidate)) != 1:
                continue
            candidate = scale(candidate, 1 / candidate[-1])
            quotient, remainder = divmod_poly(poly, candidate)
            if remainder == ZERO:
                return candidate, quotient
    return None


def factor(poly):
    """Return sorted monic irreducible factors and multiplicities over Q."""
    poly = trim(poly)
    if poly == ZERO:
        raise ValueError("the zero polynomial has no finite factorization")
    if len(poly) == 1:
        return []
    pending = [scale(poly, 1 / poly[-1])]
    irreducible = Counter()
    while pending:
        current = pending.pop()
        split = proper_factor(current)
        if split is None:
            irreducible[current] += 1
        else:
            pending.extend(split)
    return sorted(irreducible.items())
