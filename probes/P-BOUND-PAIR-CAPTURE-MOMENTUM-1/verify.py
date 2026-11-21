#!/usr/bin/env python3
"""Prospectively pinned exact relative capture-profile certificate.

NON-CANONICAL / L1. Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Standard library only; no float operations, file reads, network or randomness.
The analytical probability-envelope theorem is a stated input, not inferred
from this finite audit. No absolute capture rate is evaluated.
"""

from fractions import Fraction as F
from math import factorial, isqrt


SCALE = 10**36
PRINT_SCALE = 10**6
TAYLOR_TERMS = 32
ATAN_TERMS = 40
DELTA = F(1, 1000)
ERROR = DELTA**2
CENTERS = tuple(F(j, 10) for j in range(10)) + (F(999, 1000),)
CHECKS = 0


def require(condition, name):
    global CHECKS
    if not condition:
        raise AssertionError(name)
    CHECKS += 1


def floor_scaled(x, scale):
    return (x.numerator * scale) // x.denominator


def ceil_scaled(x, scale):
    return -((-x.numerator * scale) // x.denominator)


class I:
    """Closed exact rational interval; every operation rounds outwards."""

    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        if lo > hi:
            raise ValueError("inverted interval")
        self.lo = F(floor_scaled(lo, SCALE), SCALE)
        self.hi = F(ceil_scaled(hi, SCALE), SCALE)

    @staticmethod
    def of(other):
        return other if isinstance(other, I) else I(other)

    def __add__(self, other):
        o = I.of(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.of(other))

    def __rsub__(self, other):
        return I.of(other) - self

    def __mul__(self, other):
        o = I.of(other)
        products = (self.lo * o.lo, self.lo * o.hi,
                    self.hi * o.lo, self.hi * o.hi)
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = I.of(other)
        if o.lo <= 0 <= o.hi:
            raise ZeroDivisionError("interval includes zero")
        return self * I(1 / o.hi, 1 / o.lo)

    def __rtruediv__(self, other):
        return I.of(other) / self

    def square(self):
        if self.lo <= 0 <= self.hi:
            return I(0, max(self.lo**2, self.hi**2))
        return I(min(self.lo**2, self.hi**2),
                 max(self.lo**2, self.hi**2))

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("negative square-root interval")
        low = isqrt((self.lo.numerator * SCALE**2) // self.lo.denominator)
        high = isqrt((self.hi.numerator * SCALE**2) // self.hi.denominator)
        if F(high, SCALE)**2 < self.hi:
            high += 1
        result = I(F(low, SCALE), F(high, SCALE))
        if not (result.lo**2 <= self.lo and result.hi**2 >= self.hi):
            raise AssertionError("invalid square-root enclosure")
        return result

    def width(self):
        return self.hi - self.lo


def atan_reciprocal(n):
    """Alternating series and first omitted term, all exact."""
    x = F(1, n)
    value = sum(((-1)**j * x**(2*j + 1) / (2*j + 1)
                 for j in range(ATAN_TERMS)), F(0))
    next_term = (-1)**ATAN_TERMS * x**(2*ATAN_TERMS + 1) / (2*ATAN_TERMS + 1)
    return I(min(value, value + next_term), max(value, value + next_term))


def trig(x, sine=False):
    """Taylor polynomial plus Lagrange remainder, |x| <= 4."""
    x = I.of(x)
    bound = max(abs(x.lo), abs(x.hi))
    if bound > 4:
        raise ValueError("argument outside frozen Taylor domain")
    xx = x.square()
    term = x if sine else I(1)
    result = term
    for j in range(1, TAYLOR_TERMS):
        denominator = ((2*j)*(2*j+1) if sine else (2*j-1)*(2*j))
        term = -term * xx / denominator
        result = result + term
    # Include the zero coefficient of the opposite parity before bounding
    # the derivative remainder; derivatives of real sin and cos have norm <=1.
    degree = 2*TAYLOR_TERMS + (1 if sine else 0)
    remainder = bound**degree / factorial(degree)
    return result + I(-remainder, remainder)


def cos(x):
    return trig(x)


def sin(x):
    return trig(x, sine=True)


def density_without_2pi(p, omega, g):
    t = cos(I(p)) - 5*cos(omega)
    return (t.square() - 16).sqrt() / (t + 4*cos(omega-g))


def original_density_without_2pi(p, omega, g):
    """Independent inherited Schur/Mobius spelling for a finite audit."""
    u, s, v = cos(omega), sin(omega), cos(I(p))
    d = 4*s/(u-v)
    x = u-d*s
    X = (s+d*(u+x))/(1-x.square()).sqrt()
    tau = sin(g)/(1+cos(g))
    return (1+tau.square())*X/((1-tau*d).square()+tau.square()*X.square())


def point_ratio(p, omega, g):
    return density_without_2pi(p, omega, g)/density_without_2pi(0, omega, g)


def compatible_tight(a, b):
    return (max(a.lo, b.lo) <= min(a.hi, b.hi)
            and a.width() < F(1, 10**24)
            and b.width() < F(1, 10**24))


def main():
    pi = 16*atan_reciprocal(5)-4*atan_reciprocal(239)
    require(3 < pi.lo < pi.hi < F(22, 7), "Machin pi enclosure")
    require(pi.width() < F(1, 10**30), "pi precision")
    g, middle = 2*pi/5, 4*pi/5
    low, high = middle-DELTA, middle+DELTA
    phi = (1+I(5).sqrt())/2
    require(F(161, 100) < phi.lo < phi.hi < F(13, 8), "golden bounds")
    require(compatible_tight(cos(g), (phi-1)/2), "principal golden coefficient")
    require(compatible_tight(cos(middle), -phi/2), "central energy cosine")

    # Bounds used by the all-rectangle analytic argument, not a sample scan.
    require(low.lo > (pi/2).hi and high.hi < pi.lo, "energy quadrant")
    require((low-g).lo > 0 and (high-g).hi < (pi/2).lo, "phase quadrant")
    require(cos(high).lo > F(-41, 50) and cos(low).hi < F(-4, 5), "u box")
    require(cos(high-g).lo > F(3, 10) and cos(low-g).hi < F(1, 3), "c box")
    require(cos(I(1)).lo > F(1, 2), "momentum box")
    require(F(1108, 289) < 4, "second derivative bound")
    require(F(2, 3)/(1-DELTA) < 1, "symmetric-window error")
    require((1-ERROR)/(1+ERROR)*F(5, 8)*2 > 1, "inherited positive bound")

    # Thirty-three independent inherited/simplified formula comparisons.
    for p in CENTERS:
        for omega in (low, middle, high):
            a = density_without_2pi(p, omega, g)
            b = original_density_without_2pi(p, omega, g)
            require(compatible_tight(a, b), "Schur/Mobius identity")

    rows = []
    previous_low = None
    for p in CENTERS:
        if p == 0:
            lo = hi = F(1)
        else:
            left = point_ratio(p, low, g)*(1-ERROR)/(1+ERROR)
            right = point_ratio(p, high, g)*(1+ERROR)/(1-ERROR)
            lo = F(floor_scaled(left.lo, PRINT_SCALE), PRINT_SCALE)
            hi = F(ceil_scaled(right.hi, PRINT_SCALE), PRINT_SCALE)
            require(0 < lo <= hi < 1, "relative probability range")
            require(hi-lo <= F(1, 200), "fixed enclosure-width budget")
            require(hi < previous_low, "separated decreasing grid")
            require(compatible_tight(point_ratio(-p, middle, g),
                                     point_ratio(p, middle, g)), "evenness audit")
        rows.append((p, lo, hi))
        previous_low = lo

    print("P-BOUND-PAIR-CAPTURE-MOMENTUM-1")
    print("layer=L1; arithmetic=exact rational intervals; absolute_rate=not_evaluated")
    print("delta=1/1000; energy_halfwidth=1/1000; reference_probability=P_win(0)")
    for p, lo, hi in rows:
        print(f"p={p.numerator}/{p.denominator} ratio=[{lo.numerator}/{lo.denominator},{hi.numerator}/{hi.denominator}]")
    print(f"PASS checks={CHECKS}; centers={len(CENTERS)}; crosschecks=Schur_form_and_evenness")


if __name__ == "__main__":
    main()
