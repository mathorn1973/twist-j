# Author: A. M. Thorn <thorn@twistj.com>.
# SPDX-License-Identifier: Apache-2.0.

"""Fixed-grid rigorous real/complex intervals and second-order derivatives.

No scientific constants are evaluated at import time.  Call
``constants = init_constants(); pi = constants['pi']`` before sin/cos.

Grid/API
--------
``S = 2**96``.  ``I(lo, hi)`` takes RAW S-scaled integer endpoints.
``Q(n, d=1)`` encloses the exact rational n/d.  Python integers in
arithmetic are ordinary exact integers, not raw endpoints.
``I.exact_scaled(n)`` constructs the exact dyadic n/S.

All arithmetic uses integers, with outward rounding after each operation.
An insufficient interval-domain separation raises ``Uncertain``.  Type
errors, invalid constructors, and violated enclosure invariants raise normal
Python errors and must not be reported as a scientific inconclusive result.
No binary floating-point value enters a rigorous operation.

``AD2(v, d1, d2)`` stores actual first and second derivatives, not Taylor
coefficients.  ``AD2.variable(v)`` has derivatives (1, 0).  Its sqrt
requires v.lo > 0, because a second-order input jet cannot determine the
derivatives of sqrt at a zero.  ``CI(re, im)`` has real interval components.

Interval values should be treated as immutable.  Scalar trig cache entries
are raw integer tuples, so a caller cannot mutate a cached interval.
"""

from fractions import Fraction
from functools import lru_cache
from math import isqrt


SCALE_BITS = 96
S = 1 << SCALE_BITS


class Uncertain(Exception):
    """A requested certified operation is undefined or not separated."""


def _require_int(value, name="value"):
    if not isinstance(value, int):
        raise TypeError(name + " must be an integer; floats are not accepted")
    return value


def _ceil_div(n, d):
    """Exact ceiling of n/d, with an integer nonzero denominator."""
    if d == 0:
        raise ZeroDivisionError("integer division by zero")
    if d < 0:
        n, d = -n, -d
    return -((-n) // d)


def _up_shift(n):
    return -((-n) >> SCALE_BITS)


class I:
    """Closed real interval [lo/S, hi/S]; constructor endpoints are raw."""

    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi):
        _require_int(lo, "lo")
        _require_int(hi, "hi")
        if lo > hi:
            raise ValueError("reversed interval endpoints")
        self.lo = lo
        self.hi = hi

    @classmethod
    def exact_scaled(cls, value):
        _require_int(value, "raw endpoint")
        return cls(value, value)

    @classmethod
    def coerce(cls, value):
        return _iv(value)

    def contains_zero(self):
        return self.lo <= 0 <= self.hi

    def width_raw(self):
        return self.hi - self.lo

    def midpoint_raw(self):
        """Floor of the exact midpoint, in raw grid units."""
        return (self.lo + self.hi) // 2

    def midpoint(self):
        return I.exact_scaled(self.midpoint_raw())

    def radius_raw(self):
        return (self.hi - self.lo + 1) // 2

    def is_point(self):
        return self.lo == self.hi

    def contains(self, other):
        other = _iv(other)
        return self.lo <= other.lo and other.hi <= self.hi

    def subset_of(self, other):
        return _iv(other).contains(self)

    def disjoint(self, other):
        other = _iv(other)
        return self.hi < other.lo or other.hi < self.lo

    def hull(self, other):
        other = _iv(other)
        return I(min(self.lo, other.lo), max(self.hi, other.hi))

    def intersect(self, other):
        other = _iv(other)
        lo, hi = max(self.lo, other.lo), min(self.hi, other.hi)
        if lo > hi:
            raise ValueError("empty interval intersection")
        return I(lo, hi)

    intersection = intersect

    def min(self, other):
        """Enclosure of the pointwise minimum, not an ordering predicate."""
        other = _iv(other)
        return I(min(self.lo, other.lo), min(self.hi, other.hi))

    def max(self, other):
        """Enclosure of the pointwise maximum, not an ordering predicate."""
        other = _iv(other)
        return I(max(self.lo, other.lo), max(self.hi, other.hi))

    def __repr__(self):
        return "I(%d, %d)" % (self.lo, self.hi)

    def __bool__(self):
        raise TypeError("interval truth value is undefined; compare endpoints")

    def __eq__(self, other):
        if isinstance(other, I):
            return self.lo == other.lo and self.hi == other.hi
        if isinstance(other, int):
            return self.lo == self.hi == other * S
        return NotImplemented

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __pos__(self):
        return self

    def __add__(self, other):
        if isinstance(other, (AD2, CI)):
            return NotImplemented
        if isinstance(other, int):
            value = other << SCALE_BITS
            return I(self.lo + value, self.hi + value)
        other = _iv(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (AD2, CI)):
            return NotImplemented
        if isinstance(other, int):
            value = other << SCALE_BITS
            return I(self.lo - value, self.hi - value)
        other = _iv(other)
        return I(self.lo - other.hi, self.hi - other.lo)

    def __rsub__(self, other):
        return _iv(other) - self

    def __mul__(self, other):
        if isinstance(other, (AD2, CI)):
            return NotImplemented
        if isinstance(other, int):
            if other >= 0:
                return I(self.lo * other, self.hi * other)
            return I(self.hi * other, self.lo * other)
        other = _iv(other)
        a, b, c, d = self.lo, self.hi, other.lo, other.hi
        if a >= 0:
            if c >= 0:
                low, high = a * c, b * d
            elif d <= 0:
                low, high = b * c, a * d
            else:
                low, high = b * c, b * d
        elif b <= 0:
            if c >= 0:
                low, high = a * d, b * c
            elif d <= 0:
                low, high = b * d, a * c
            else:
                low, high = a * d, a * c
        elif c >= 0:
            low, high = a * d, b * d
        elif d <= 0:
            low, high = b * c, a * c
        else:
            low, high = min(a * d, b * c), max(a * c, b * d)
        return I(low >> SCALE_BITS, _up_shift(high))

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (AD2, CI)):
            return NotImplemented
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("division by the exact integer zero")
            if other > 0:
                return I(self.lo // other, _ceil_div(self.hi, other))
            return I(self.hi // other, _ceil_div(self.lo, other))
        other = _iv(other)
        if other.contains_zero():
            raise Uncertain("real denominator interval contains zero")
        if other.hi < 0:
            return (-self) / (-other)
        a, b, c, d = self.lo, self.hi, other.lo, other.hi
        # Here 0 < c <= d.  Each endpoint is a directly rounded ratio.
        if a >= 0:
            return I((a << SCALE_BITS) // d,
                     _ceil_div(b << SCALE_BITS, c))
        if b <= 0:
            return I((a << SCALE_BITS) // c,
                     _ceil_div(b << SCALE_BITS, d))
        return I((a << SCALE_BITS) // c,
                 _ceil_div(b << SCALE_BITS, c))

    def __rtruediv__(self, other):
        return _iv(other) / self

    def reciprocal(self):
        return 1 / self

    def square(self):
        if self.lo >= 0:
            low, high = self.lo * self.lo, self.hi * self.hi
        elif self.hi <= 0:
            low, high = self.hi * self.hi, self.lo * self.lo
        else:
            low, high = 0, max(self.lo * self.lo, self.hi * self.hi)
        return I(low >> SCALE_BITS, _up_shift(high))

    sqr = square

    def __pow__(self, power):
        _require_int(power, "power")
        if power == 0:
            return Q(1)
        if power == 1:
            return self
        if power == 2:
            return self.square()
        if power < 0:
            return self.reciprocal() ** (-power)
        shift = SCALE_BITS * (power - 1)
        if power % 2:
            low, high = self.lo ** power, self.hi ** power
        elif self.lo >= 0:
            low, high = self.lo ** power, self.hi ** power
        elif self.hi <= 0:
            low, high = self.hi ** power, self.lo ** power
        else:
            low, high = 0, max(-self.lo, self.hi) ** power
        return I(low >> shift, -((-high) >> shift))

    def __abs__(self):
        if self.lo >= 0:
            return self
        if self.hi <= 0:
            return -self
        return I(0, max(-self.lo, self.hi))

    def abs(self):
        return abs(self)

    def sqrt(self):
        if self.lo < 0:
            raise Uncertain("square-root interval has a negative lower endpoint")
        low = isqrt(self.lo << SCALE_BITS)
        target = self.hi << SCALE_BITS
        high = isqrt(target)
        if high * high < target:
            high += 1
        return I(low, high)

    def sincos(self):
        return _sincos_interval(self)

    def sin(self):
        return _sincos_interval(self)[0]

    def cos(self):
        return _sincos_interval(self)[1]


def _iv(value):
    if isinstance(value, I):
        return value
    if isinstance(value, int):
        raw = value << SCALE_BITS
        return I(raw, raw)
    raise TypeError("expected an interval or exact Python integer")


def Q(n, d=1):
    """Outward fixed-grid enclosure of the exact rational n/d."""
    _require_int(n, "numerator")
    _require_int(d, "denominator")
    if d == 0:
        raise ZeroDivisionError("zero rational denominator")
    if d < 0:
        n, d = -n, -d
    raw_n = n << SCALE_BITS
    return I(raw_n // d, _ceil_div(raw_n, d))


def hull(*values):
    if not values:
        raise ValueError("hull requires at least one interval")
    result = _iv(values[0])
    for value in values[1:]:
        result = result.hull(value)
    return result


def intersect(*values):
    if not values:
        raise ValueError("intersection requires at least one interval")
    result = _iv(values[0])
    for value in values[1:]:
        result = result.intersect(value)
    return result


def interval_min(*values):
    if not values:
        raise ValueError("interval_min requires at least one interval")
    result = _iv(values[0])
    for value in values[1:]:
        result = result.min(value)
    return result


def interval_max(*values):
    if not values:
        raise ValueError("interval_max requires at least one interval")
    result = _iv(values[0])
    for value in values[1:]:
        result = result.max(value)
    return result


minimum = interval_min
maximum = interval_max


_PI = None
_HALF_PI = None
_TWO_PI = None
_SIN_COEFF = None
_COS_COEFF = None
_SIN_ERROR_RAW = None
_COS_ERROR_RAW = None


def _atan_reciprocal_40(q):
    """Exact rational bounds from 40 terms; next term bounds the tail."""
    partial = Fraction(0)
    qpower = q
    q2 = q * q
    for j in range(40):
        term = Fraction(1, (2 * j + 1) * qpower)
        partial = partial + term if j % 2 == 0 else partial - term
        qpower *= q2
    # Forty terms end with a negative term.  The remaining tail is in
    # [0, 1/(81*q**81)], by the decreasing alternating-series theorem.
    tail = Fraction(1, 81 * qpower)
    return partial, partial + tail


def init_constants():
    """Initialize rigorous pi and Taylor data; return ``{'pi': I}``.

    Pi uses Machin's identity and exactly 40 alternating terms for each
    arctangent.  The two partial sums and their tails are exact Fractions;
    only the final pi enclosure is rounded to the fixed grid.  Repeated
    calls are idempotent.  No scientific initialization happens on import.
    """
    global _PI, _HALF_PI, _TWO_PI
    global _SIN_COEFF, _COS_COEFF, _SIN_ERROR_RAW, _COS_ERROR_RAW
    if _PI is not None:
        return {"pi": _PI}
    a_lo, a_hi = _atan_reciprocal_40(5)
    b_lo, b_hi = _atan_reciprocal_40(239)
    pi_lo = 16 * a_lo - 4 * b_hi
    pi_hi = 16 * a_hi - 4 * b_lo
    pi = I((pi_lo.numerator << SCALE_BITS) // pi_lo.denominator,
           _ceil_div(pi_hi.numerator << SCALE_BITS, pi_hi.denominator))
    if not (3 * S < pi.lo <= pi.hi < 4 * S):
        raise AssertionError("Machin pi enclosure failed its domain check")
    factorials = [1]
    for j in range(1, 50):
        factorials.append(factorials[-1] * j)
    sin_coeff = tuple(Q(1 if j % 2 == 0 else -1, factorials[2 * j + 1])
                      for j in range(24))
    cos_coeff = tuple(Q(1 if j % 2 == 0 else -1, factorials[2 * j])
                      for j in range(24))
    # After reduction |r|<=1.  The 24-term polynomials have rigorous
    # remainders <=1/49! (sin) and <=1/48! (cos), respectively.
    _SIN_ERROR_RAW = _ceil_div(S, factorials[49])
    _COS_ERROR_RAW = _ceil_div(S, factorials[48])
    _SIN_COEFF = sin_coeff
    _COS_COEFF = cos_coeff
    _HALF_PI = pi / 2
    _TWO_PI = pi * 2
    _PI = pi
    return {"pi": _PI}


def _require_trig_init():
    if _PI is None:
        raise RuntimeError("call init_constants() before sin/cos")


@lru_cache(maxsize=65536)
def _sincos_scalar_raw(raw):
    """Enclose sin/cos at the exact dyadic raw/S; return four integers."""
    _require_trig_init()
    if raw == 0:
        return 0, 0, S, S
    hp_mid = _HALF_PI.midpoint_raw()
    quadrant = (raw + hp_mid // 2) // hp_mid
    remainder = I.exact_scaled(raw) - quadrant * _HALF_PI
    if max(abs(remainder.lo), abs(remainder.hi)) > S:
        # Finite-precision pi may lose useful phase information for huge
        # arguments.  The full range is still a rigorous enclosure.
        return -S, S, -S, S
    r2 = remainder.square()
    ps = _SIN_COEFF[-1]
    pc = _COS_COEFF[-1]
    for j in range(22, -1, -1):
        ps = ps * r2 + _SIN_COEFF[j]
        pc = pc * r2 + _COS_COEFF[j]
    sr = remainder * ps
    cr = pc
    sr = I(max(-S, sr.lo - _SIN_ERROR_RAW),
           min(S, sr.hi + _SIN_ERROR_RAW))
    cr = I(max(-S, cr.lo - _COS_ERROR_RAW),
           min(S, cr.hi + _COS_ERROR_RAW))
    which = quadrant % 4
    if which == 0:
        return sr.lo, sr.hi, cr.lo, cr.hi
    if which == 1:
        return cr.lo, cr.hi, -sr.hi, -sr.lo
    if which == 2:
        return -sr.hi, -sr.lo, -cr.hi, -cr.lo
    return -cr.hi, -cr.lo, sr.lo, sr.hi


def _possible_halfpi_multiples(value):
    """All integers n for which n*pi/2 could belong to value."""
    a, b = value.lo, value.hi
    c, d = _HALF_PI.lo, _HALF_PI.hi
    if a >= 0:
        return _ceil_div(a, d), b // c
    if b <= 0:
        return _ceil_div(a, c), b // d
    return _ceil_div(a, c), b // c


def _has_residue(low, high, residue):
    return low <= high and low + ((residue - low) % 4) <= high


def _sincos_interval(value):
    _require_trig_init()
    if value.width_raw() >= _TWO_PI.hi:
        return I(-S, S), I(-S, S)
    a = _sincos_scalar_raw(value.lo)
    b = a if value.hi == value.lo else _sincos_scalar_raw(value.hi)
    sin_lo, sin_hi = min(a[0], b[0]), max(a[1], b[1])
    cos_lo, cos_hi = min(a[2], b[2]), max(a[3], b[3])
    low, high = _possible_halfpi_multiples(value)
    if _has_residue(low, high, 1):
        sin_hi = S
    if _has_residue(low, high, 3):
        sin_lo = -S
    if _has_residue(low, high, 0):
        cos_hi = S
    if _has_residue(low, high, 2):
        cos_lo = -S
    return I(sin_lo, sin_hi), I(cos_lo, cos_hi)


def clear_trig_cache():
    """Discard cached dyadic endpoint values; constants are unchanged."""
    _sincos_scalar_raw.cache_clear()


def trig_cache_info():
    return _sincos_scalar_raw.cache_info()


class AD2:
    """Real interval value and its actual first/second derivatives."""

    __slots__ = ("v", "d1", "d2")

    def __init__(self, v, d1=0, d2=0):
        self.v = _iv(v)
        self.d1 = _iv(d1)
        self.d2 = _iv(d2)

    @classmethod
    def variable(cls, value):
        return cls(value, 1, 0)

    @classmethod
    def constant(cls, value):
        return cls(value, 0, 0)

    @classmethod
    def coerce(cls, value):
        return value if isinstance(value, cls) else cls.constant(value)

    def __repr__(self):
        return "AD2(%r, %r, %r)" % (self.v, self.d1, self.d2)

    def __bool__(self):
        raise TypeError("AD2 truth value is undefined; inspect .v endpoints")

    def __neg__(self):
        return AD2(-self.v, -self.d1, -self.d2)

    def __pos__(self):
        return self

    def __add__(self, other):
        if isinstance(other, AD2):
            return AD2(self.v + other.v, self.d1 + other.d1,
                       self.d2 + other.d2)
        return AD2(self.v + _iv(other), self.d1, self.d2)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, AD2):
            return AD2(self.v - other.v, self.d1 - other.d1,
                       self.d2 - other.d2)
        return AD2(self.v - _iv(other), self.d1, self.d2)

    def __rsub__(self, other):
        return AD2.coerce(other) - self

    def __mul__(self, other):
        if not isinstance(other, AD2):
            value = _iv(other)
            return AD2(self.v * value, self.d1 * value, self.d2 * value)
        return AD2(self.v * other.v,
                   self.d1 * other.v + self.v * other.d1,
                   self.d2 * other.v + 2 * self.d1 * other.d1
                   + self.v * other.d2)

    __rmul__ = __mul__

    def reciprocal(self):
        inv = 1 / self.v
        inv2 = inv.square()
        return AD2(inv, -self.d1 * inv2,
                   2 * self.d1.square() * inv2 * inv - self.d2 * inv2)

    def __truediv__(self, other):
        if isinstance(other, AD2):
            return self * other.reciprocal()
        value = _iv(other)
        return AD2(self.v / value, self.d1 / value, self.d2 / value)

    def __rtruediv__(self, other):
        return AD2.coerce(other) * self.reciprocal()

    def square(self):
        return AD2(self.v.square(), 2 * self.v * self.d1,
                   2 * self.d1.square() + 2 * self.v * self.d2)

    sqr = square

    def __pow__(self, power):
        _require_int(power, "power")
        if power == 0:
            return AD2.constant(1)
        if power == 1:
            return self
        if power == 2:
            return self.square()
        vprev = self.v ** (power - 1)
        return AD2(self.v ** power, power * vprev * self.d1,
                   power * vprev * self.d2
                   + power * (power - 1) * (self.v ** (power - 2))
                   * self.d1.square())

    def sqrt(self):
        if self.v.lo <= 0:
            raise Uncertain("AD2 sqrt needs a strictly positive value interval")
        root = self.v.sqrt()
        half_inv = 1 / (2 * root)
        first = self.d1 * half_inv
        second = (self.d2 - 2 * first.square()) * half_inv
        return AD2(root, first, second)

    def sincos(self):
        sv, cv = self.v.sincos()
        first2 = self.d1.square()
        return (AD2(sv, cv * self.d1, cv * self.d2 - sv * first2),
                AD2(cv, -sv * self.d1, -sv * self.d2 - cv * first2))

    def sin(self):
        return self.sincos()[0]

    def cos(self):
        return self.sincos()[1]

    def __abs__(self):
        if self.v.lo > 0:
            return self
        if self.v.hi < 0:
            return -self
        raise Uncertain("AD2 abs needs a sign-separated value interval")

    def abs(self):
        return abs(self)


class CI:
    """Complex rectangle with interval components; coerces I and int."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = _iv(re)
        self.im = _iv(im)

    @classmethod
    def coerce(cls, value):
        return value if isinstance(value, cls) else cls(_iv(value), 0)

    def __repr__(self):
        return "CI(%r, %r)" % (self.re, self.im)

    def __bool__(self):
        raise TypeError("complex-interval truth value is undefined")

    def __neg__(self):
        return CI(-self.re, -self.im)

    def __pos__(self):
        return self

    def __add__(self, other):
        if isinstance(other, CI):
            return CI(self.re + other.re, self.im + other.im)
        return CI(self.re + _iv(other), self.im)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, CI):
            return CI(self.re - other.re, self.im - other.im)
        return CI(self.re - _iv(other), self.im)

    def __rsub__(self, other):
        return CI.coerce(other) - self

    def __mul__(self, other):
        if isinstance(other, CI):
            return CI(self.re * other.re - self.im * other.im,
                      self.re * other.im + self.im * other.re)
        value = _iv(other)
        return CI(self.re * value, self.im * value)

    __rmul__ = __mul__

    def conjugate(self):
        return CI(self.re, -self.im)

    conj = conjugate

    def norm2(self):
        return self.re.square() + self.im.square()

    def __truediv__(self, other):
        if isinstance(other, CI):
            denominator = other.norm2()
            if denominator.lo <= 0:
                raise Uncertain("complex denominator is not separated from zero")
            product = self * other.conjugate()
            return CI(product.re / denominator, product.im / denominator)
        value = _iv(other)
        return CI(self.re / value, self.im / value)

    def __rtruediv__(self, other):
        return CI.coerce(other) / self

    def reciprocal(self):
        return 1 / self

    def square(self):
        return CI(self.re.square() - self.im.square(),
                  2 * self.re * self.im)

    sqr = square

    def __pow__(self, power):
        _require_int(power, "power")
        if power < 0:
            return self.reciprocal() ** (-power)
        if power == 0:
            return CI(1, 0)
        if power == 1:
            return self
        if power == 2:
            return self.square()
        result, base, exponent = CI(1, 0), self, power
        while exponent:
            if exponent & 1:
                result = result * base
            exponent >>= 1
            if exponent:
                base = base.square()
        return result

    def __abs__(self):
        return self.norm2().sqrt()

    def abs(self):
        return abs(self)


def sqrt(value):
    return value.sqrt() if isinstance(value, AD2) else _iv(value).sqrt()


def sin(value):
    return value.sin() if isinstance(value, AD2) else _iv(value).sin()


def cos(value):
    return value.cos() if isinstance(value, AD2) else _iv(value).cos()


def sincos(value):
    return value.sincos() if isinstance(value, AD2) else _iv(value).sincos()
