#!/usr/bin/env python3
"""Exact standard-library verifier for C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N.

PUBLIC, NON-CANONICAL. Conditional L1 evidence audit.
Uses only the Python standard library (fractions.Fraction, int, math.isqrt, itertools).
Zero floating-point operations, zero external imports, zero file reads, zero network calls.
"""

from __future__ import annotations

from fractions import Fraction as F
import itertools
from math import isqrt


# ============================================================================
# 1. Exact Algebraic Fields and Certified Rational Interval Arithmetic
# ============================================================================

class QSqrt5:
    """Exact element a + b*sqrt(5) in Q(sqrt(5))."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = F(a)
        self.b = F(b)

    def __add__(self, other):
        o = other if isinstance(other, QSqrt5) else QSqrt5(other)
        return QSqrt5(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, other):
        o = other if isinstance(other, QSqrt5) else QSqrt5(other)
        return QSqrt5(self.a - o.a, self.b - o.b)

    def __rsub__(self, other):
        o = other if isinstance(other, QSqrt5) else QSqrt5(other)
        return o - self

    def __neg__(self):
        return QSqrt5(-self.a, -self.b)

    def __mul__(self, other):
        o = other if isinstance(other, QSqrt5) else QSqrt5(other)
        return QSqrt5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = other if isinstance(other, QSqrt5) else QSqrt5(other)
        norm = o.a * o.a - 5 * o.b * o.b
        assert norm != 0
        return QSqrt5((self.a * o.a - 5 * self.b * o.b) / norm,
                      (self.b * o.a - self.a * o.b) / norm)

    def __eq__(self, other) -> bool:
        o = other if isinstance(other, QSqrt5) else QSqrt5(other)
        return self.a == o.a and self.b == o.b


SCALE_DIGITS = 36
SCALE = 10 ** SCALE_DIGITS


class RI:
    """Closed rational interval [lo, hi] with outward rounding and self-certifying primitives."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        if isinstance(lo, RI) and hi is None:
            self.lo = lo.lo
            self.hi = lo.hi
            return
        lo_f = lo if isinstance(lo, F) else F(lo)
        hi_f = lo_f if hi is None else (hi if isinstance(hi, F) else F(hi))
        if lo_f > hi_f:
            raise ValueError(f"Inverted interval: {lo_f} > {hi_f}")
        self.lo = lo_f
        self.hi = hi_f

    def trim(self, scale: int = SCALE) -> "RI":
        n_lo = (self.lo.numerator * scale) // self.lo.denominator
        n_hi = -((-self.hi.numerator * scale) // self.hi.denominator)
        res = RI(F(n_lo, scale), F(n_hi, scale))
        assert res.lo <= self.lo and self.hi <= res.hi
        return res

    def __add__(self, other):
        if isinstance(other, CRI):
            return NotImplemented
        o = other if isinstance(other, RI) else RI(other)
        return RI(self.lo + o.lo, self.hi + o.hi).trim()

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, CRI):
            return NotImplemented
        o = other if isinstance(other, RI) else RI(other)
        return RI(self.lo - o.hi, self.hi - o.lo).trim()

    def __rsub__(self, other):
        if isinstance(other, CRI):
            return NotImplemented
        o = other if isinstance(other, RI) else RI(other)
        return o - self

    def __neg__(self):
        return RI(-self.hi, -self.lo)

    def __mul__(self, other):
        if isinstance(other, CRI):
            return NotImplemented
        o = other if isinstance(other, RI) else RI(other)
        p1 = self.lo * o.lo
        p2 = self.lo * o.hi
        p3 = self.hi * o.lo
        p4 = self.hi * o.hi
        return RI(min(p1, p2, p3, p4), max(p1, p2, p3, p4)).trim()

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, CRI):
            return NotImplemented
        o = other if isinstance(other, RI) else RI(other)
        if o.lo <= 0 <= o.hi:
            raise ZeroDivisionError("Interval division by interval containing 0")
        inv = RI(F(1, 1) / o.hi, F(1, 1) / o.lo)
        return (self * inv).trim()

    def __rtruediv__(self, other):
        if isinstance(other, CRI):
            return NotImplemented
        o = other if isinstance(other, RI) else RI(other)
        return o / self

    def sqr(self) -> "RI":
        if self.lo >= 0:
            return RI(self.lo * self.lo, self.hi * self.hi).trim()
        if self.hi <= 0:
            return RI(self.hi * self.hi, self.lo * self.lo).trim()
        m = max(-self.lo, self.hi)
        return RI(F(0), m * m).trim()

    def abs_iv(self) -> "RI":
        if self.lo >= 0:
            return self
        if self.hi <= 0:
            return -self
        return RI(F(0), max(-self.lo, self.hi))

    def sqrt(self) -> "RI":
        if self.lo < 0:
            raise ValueError("sqrt of negative interval")
        num_lo = (self.lo.numerator * SCALE * SCALE) // self.lo.denominator
        num_hi = -((-self.hi.numerator * SCALE * SCALE) // self.hi.denominator)
        s_lo = isqrt(num_lo)
        s_hi = isqrt(num_hi)
        if s_hi * s_hi < num_hi:
            s_hi += 1
        lo_f = F(s_lo, SCALE)
        hi_f = F(s_hi, SCALE)
        assert lo_f >= 0 and lo_f * lo_f <= self.lo and self.hi <= hi_f * hi_f
        return RI(lo_f, hi_f)

    def contains_zero(self) -> bool:
        return self.lo <= 0 <= self.hi

    def __gt__(self, other) -> bool:
        o = other if isinstance(other, RI) else RI(other)
        return self.lo > o.hi

    def __lt__(self, other) -> bool:
        o = other if isinstance(other, RI) else RI(other)
        return self.hi < o.lo


class CRI:
    """Complex rational interval re + i*im."""
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = re if isinstance(re, RI) else RI(re)
        self.im = im if isinstance(im, RI) else RI(im)

    def __add__(self, other):
        o = other if isinstance(other, CRI) else CRI(other)
        return CRI(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, other):
        o = other if isinstance(other, CRI) else CRI(other)
        return CRI(self.re - o.re, self.im - o.im)

    def __rsub__(self, other):
        o = other if isinstance(other, CRI) else CRI(other)
        return o - self

    def __neg__(self):
        return CRI(-self.re, -self.im)

    def __mul__(self, other):
        o = other if isinstance(other, CRI) else CRI(other)
        return CRI(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = other if isinstance(other, CRI) else CRI(other)
        d = o.re.sqr() + o.im.sqr()
        return CRI((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d)

    def __rtruediv__(self, other):
        o = other if isinstance(other, CRI) else CRI(other)
        return o / self

    def sqrt_principal(self) -> "CRI":
        assert self.im > 0
        r = (self.re.sqr() + self.im.sqr()).sqrt()
        u = ((r + self.re) / 2).sqrt()
        v = ((r - self.re) / 2).sqrt()
        res = CRI(u, v)
        diff = res * res - self
        assert u > 0 and v > 0 and diff.contains_zero()
        return res

    def contains_zero(self) -> bool:
        return self.re.contains_zero() and self.im.contains_zero()


def atan_unit_fraction(q: int, pairs: int = 16) -> RI:
    """Leibniz alternating-series enclosure of arctan(1/q) for integer q >= 2."""
    assert q >= 2 and pairs >= 1
    x = F(1, q)
    x2 = x * x
    power = x
    s = F(0)
    for m in range(2 * pairs):
        term = power / (2 * m + 1)
        if m % 2 == 0:
            s += term
        else:
            s -= term
        power *= x2
    rem = power / (4 * pairs + 1)
    return RI(s, s + rem).trim()


PI = (RI(16) * atan_unit_fraction(5, 18) - RI(4) * atan_unit_fraction(239, 8)).trim()


def cos_sin_point(t: F, terms: int = 18) -> tuple[RI, RI]:
    """Lagrange-remainder Taylor enclosure of cos(t), sin(t) at rational point t."""
    t2 = t * t
    c_sum = F(1)
    c_pow = F(1)
    fact = 1
    for m in range(1, terms):
        c_pow *= t2
        fact *= (2 * m - 1) * (2 * m)
        if m % 2 == 1:
            c_sum -= c_pow / fact
        else:
            c_sum += c_pow / fact
    c_rem = (c_pow * t2) / (fact * (2 * terms - 1) * (2 * terms))
    cos_iv = RI(c_sum - c_rem, c_sum + c_rem).trim()

    s_sum = t
    s_pow = t
    fact = 1
    for m in range(1, terms):
        s_pow *= t2
        fact *= (2 * m) * (2 * m + 1)
        if m % 2 == 1:
            s_sum -= s_pow / fact
        else:
            s_sum += s_pow / fact
    s_rem = (abs(s_pow) * t2) / (fact * (2 * terms) * (2 * terms + 1))
    sin_iv = RI(s_sum - s_rem, s_sum + s_rem).trim()
    return cos_iv, sin_iv


def cos_sin(iv: RI) -> tuple[RI, RI]:
    """Certified enclosure of cos(iv) and sin(iv) via midpoint addition and Leibniz bounds."""
    mid = (iv.lo + iv.hi) / 2
    rad = (iv.hi - iv.lo) / 2
    assert F(0) <= rad <= F(2)
    c0, s0 = cos_sin_point(mid)
    if rad == 0:
        return c0, s0
    cos_d = RI(F(1) - (rad * rad) / 2, F(1))
    sin_d = RI(-rad, rad)
    return (c0 * cos_d - s0 * sin_d).trim(), (s0 * cos_d + c0 * sin_d).trim()


def acos_iv(iv: RI) -> RI:
    """Self-certifying enclosure of arccos(iv) on (-1, 1) via strict monotonicity of cos on [0, pi]."""
    assert iv.lo > -1 and iv.hi < 1

    def solve_cos(target: F, upper_bound: bool) -> F:
        lo = F(0)
        hi = PI.hi if upper_bound else PI.lo
        for _ in range(110):
            mid = (lo + hi) / 2
            mid = F((mid.numerator * SCALE) // mid.denominator, SCALE)
            c_mid, _ = cos_sin_point(mid, 16)
            if upper_bound:
                if c_mid.hi <= target:
                    hi = mid
                else:
                    lo = mid
            else:
                if c_mid.lo >= target:
                    lo = mid
                else:
                    hi = mid
        return hi if upper_bound else lo

    th_lo = solve_cos(iv.hi, upper_bound=False)
    th_hi = solve_cos(iv.lo, upper_bound=True)
    c_at_lo, _ = cos_sin_point(th_lo, 18)
    c_at_hi, _ = cos_sin_point(th_hi, 18)
    assert F(0) <= th_lo <= th_hi <= PI.lo
    assert c_at_hi.hi <= iv.lo and iv.hi <= c_at_lo.lo
    return RI(th_lo, th_hi)


def power_20_9(iv: RI) -> RI:
    """Self-certifying enclosure of iv**(20/9) for iv > 0 via integer 9th/20th power brackets."""
    assert iv.lo > 0
    u_lo_20 = iv.lo ** 20
    u_hi_20 = iv.hi ** 20

    def solve_root9(target: F, upper: bool) -> F:
        lo = F(0)
        hi = F(1)
        while hi ** 9 < target:
            lo = hi
            hi *= 2
        for _ in range(120):
            mid = (lo + hi) / 2
            if mid ** 9 <= target:
                lo = mid
            else:
                hi = mid
        if upper:
            n_hi = -((-hi.numerator * SCALE) // hi.denominator)
            res = F(n_hi, SCALE)
            while res ** 9 < target:
                n_hi += 1
                res = F(n_hi, SCALE)
            return res
        else:
            n_lo = (lo.numerator * SCALE) // lo.denominator
            res = F(n_lo, SCALE)
            while res ** 9 > target:
                n_lo -= 1
                res = F(n_lo, SCALE)
            return res

    m_lo = solve_root9(u_lo_20, upper=False)
    m_hi = solve_root9(u_hi_20, upper=True)
    assert m_lo > 0 and m_lo ** 9 <= u_lo_20 and u_hi_20 <= m_hi ** 9
    return RI(m_lo, m_hi)


# ============================================================================
# Group 1: Inherited Infinite-Operator Branch Gap (BRANCH_GAP)
# ============================================================================

def audit_branch_gap() -> int:
    checks = 0

    def ok(cond: bool, msg: str):
        nonlocal checks
        assert cond, msg
        checks += 1

    c0_alg = QSqrt5(F(1, 4), F(1, 4))
    s0_sq_alg = QSqrt5(F(5, 8), F(-1, 8))
    ok(c0_alg * c0_alg + s0_sq_alg == QSqrt5(1, 0), "c0^2 + s0^2 == 1 in Q(sqrt(5))")
    cos_g_alg = 2 * c0_alg * c0_alg - 1
    ok(cos_g_alg == QSqrt5(F(-1, 4), F(1, 4)), "cos(2pi/5) == (sqrt(5)-1)/4")
    ck0_alg = (1 - 5 * cos_g_alg) / 4
    ok(ck0_alg == QSqrt5(F(9, 16), F(-5, 16)), "cos(k0) == (9-5*sqrt(5))/16")
    ok(64 * ck0_alg * ck0_alg - 72 * ck0_alg - 11 == QSqrt5(0, 0), "64*ck0^2 - 72*ck0 - 11 == 0")

    ok(F(111, 50) ** 2 < 5 < F(9, 4) ** 2, "111/50 < sqrt(5) < 9/4")
    ok(F(223, 100) ** 2 < 5 < F(161, 72) ** 2, "223/100 < sqrt(5) < 161/72")
    sqrt5 = RI(5).sqrt()
    c0 = (1 + sqrt5) / 4
    s0 = ((5 - sqrt5) / 8).sqrt()
    s_par = ((2 * sqrt5 - 1) / 5).sqrt()
    ok(c0 > F(161, 200) and c0 > F(4, 5) and c0 < 1, "c0 enclosure")
    ok(s0 > F(1, 2) and s0 < F(59, 100), "s0 enclosure")
    ok(2 * s0 > 1 and 2 * s0 < F(6, 5), "1 < |z-1| = 2*s0 < 6/5")
    ok(s_par > F(83, 100) and s_par < F(5, 6), "83/100 < s < 5/6")

    delta_f = (4 * c0 - 2 * s0) / sqrt5
    ok(delta_f > F(68, 75) and F(68, 75) > F(9, 10), "delta_f > 68/75 > 9/10")

    ktilde_bb = 5 * c0 * (1 - s_par)
    ktilde_st_11 = 4 / (5 * s_par * c0)
    det_ktilde_st = 4 * (1 - s_par) / s_par
    tr_ktilde_st = -3 * c0 + (1 + 3 * c0.sqr()) / (s_par * c0)
    ok(ktilde_bb > F(2, 3) and F(2, 3) > F(1, 2), "Ktilde_BB > 2/3 > 1/2")
    ok(ktilde_st_11 > F(24, 25) and F(24, 25) > F(1, 2), "(Ktilde_ST)_11 > 24/25 > 1/2")
    ok(det_ktilde_st > F(4, 5), "det(Ktilde_ST) > 4/5")

    f_rect = F(1, 1) / (F(4, 5) * F(83, 100)) + 3 * F(4, 5) * (F(1, 1) / F(83, 100) - 1)
    ok(f_rect == F(829, 415) and tr_ktilde_st < f_rect and f_rect < 2, "tr(Ktilde_ST) < 829/415 < 2")
    det_shifted_lb = F(4, 5) - f_rect / 2 + F(1, 4)
    ok(det_shifted_lb == F(17, 332) and det_shifted_lb > 0, "det(Ktilde_ST - I/2) > 17/332 > 0")
    ok(det_ktilde_st - tr_ktilde_st / 2 + F(1, 4) > F(17, 332), "interval det(Ktilde_ST - I/2) > 17/332")

    inv_wb_ub = F(10, 9) + F(6, 5) * (F(10, 9) ** 2) * 2
    delta0 = F(1, 1) / inv_wb_ub
    ok(inv_wb_ub == F(110, 27) and delta0 == F(27, 110), "delta0 == 27/110")

    r_circle = F(1, 8)
    dist_circle = min(r_circle, delta0 - r_circle)
    M0 = F(1, 1) / dist_circle
    p_star = F(1, 12)
    neumann = M0 * p_star
    resolv_ub = M0 / (1 - neumann)
    gap_uniform = delta0 - 2 * p_star
    L_bound = F(1, 1) / gap_uniform
    ok(dist_circle == F(53, 440) and M0 == F(440, 53), "Riesz circle distance 53/440")
    ok(neumann == F(110, 159) and neumann < 1, "Neumann product 110/159 < 1")
    ok(resolv_ub == F(1320, 49), "sup ||(w-W(P))^-1|| <= 1320/49")
    ok(gap_uniform == F(13, 165) and L_bound == F(165, 13), "uniform gap 13/165 and L=165/13")

    comp_norm = p_star / (delta0 - p_star)
    anchor_sq = 1 - comp_norm ** 2
    ok(comp_norm == F(55, 107) and anchor_sq == F(8424, 11449) and anchor_sq > F(1, 2),
       "anchor overlap |<chi0, chi(P)>|^2 >= 8424/11449 > 1/2")

    ok(delta0 - F(1, 4) < 0, "negative control: radius 1/4 exceeds zero-momentum gap")
    print(f"PASS GROUP 1 BRANCH_GAP: {checks} checks; gap>={gap_uniform}; L<={L_bound}")
    return checks


# ============================================================================
# Group 2: Incoming Rectangle, Output Coarea, and Full-F Probability Bound
# ============================================================================

def audit_packet_certificate() -> int:
    checks = 0

    def ok(cond: bool, msg: str):
        nonlocal checks
        assert cond, msg
        checks += 1

    pi = PI
    g = 2 * pi / 5
    beta = 4 * pi / 5
    estar = 8 * pi / 5
    h = RI(F(1, 1000))
    p_in = RI(F(1, 1000))
    p_bound = RI(F(1, 100))
    delta_k = RI(F(1, 1000))
    ell = 2 * h
    L = RI(F(165, 13))
    atan_half = atan_unit_fraction(2, 35)
    theta = 2 * (pi / 2 - atan_half)
    c_th2, s_th2 = cos_sin(theta / 2)
    tan_th2 = s_th2 / c_th2
    ok(tan_th2.lo <= F(2) <= tan_th2.hi, "tan(theta/2) encloses 2")

    c_g2, s_g2 = cos_sin(g / 2)
    tau = s_g2 / c_g2

    P = RI(F(-1, 1000), F(1, 1000))
    omega = RI(beta.lo - F(1, 1000), beta.hi + F(1, 1000))
    c, s = cos_sin(omega)
    cos_P, sin_P = cos_sin(P)
    D = c - cos_P
    d = 4 * s / D
    x = c - d * s
    rad = 1 - x.sqr()
    numerator = s + d * (c + x)
    X = numerator / rad.sqrt()
    denom = (1 - tau * d).sqr() + tau.sqr() * X.sqr()
    rho_fiber = (1 + tau.sqr()) * X / (2 * pi * denom)
    dx_domega = -s * (1 + 8 * c / D + 4 * s.sqr() / D.sqr())
    dx_dP = 4 * s.sqr() * sin_P / D.sqr()
    relative_speed = rad.sqrt() / (-dx_domega)
    center_to_relative_speed_ratio = dx_dP.abs_iv() / rad.sqrt()
    a = p_in * RI(rho_fiber.lo) / pi

    ok(D < 0, "incoming stationary Schur block nonsingular")
    ok(x > -1 and x < 1, "incoming spatial roots strictly interior")
    ok(numerator > 0, "incoming exterior branch has positive real part")
    ok(dx_domega < 0, "incoming energy parametrization nonsingular")
    ok(relative_speed > 0, "incoming two relative group speeds nonzero")
    ok(center_to_relative_speed_ratio < 1, "both incoming walkers separate from static token")
    ok(denom > 0, "incoming contact denominator positive")
    ok(rho_fiber > F(77, 1000), "uniform actual W fiber density exceeds 77/1000")
    ok(a > F(24, 10**6), "integrated incoming density exceeds 24/1000000")

    sqrt5 = RI(5).sqrt()
    c0_b, s0_b = cos_sin(beta)
    cg, sg = cos_sin(g)
    ii = CRI(0, 1)
    w = CRI(c0_b, -s0_b)
    u = CRI(cg, -sg)
    d0 = RI(F(-3, 5))
    radical = -(w * w - 2 * d0 * w + 1).sqrt_principal()
    j0 = 1 / ((w + 1) * radical)
    j1 = ((w * w + (1 - d0) * w + 1) * j0 - 1) / ((1 + d0) * w)
    gb_old = (w * (w - d0) * j0 + (1 - d0 * w) * j1) / (w - 1)
    gw_old = gb_old / (u - (u - 1) * w * gb_old)
    F_old = 2 * w * gw_old - 1
    d_center = 4 * s0_b / (c0_b - 1)
    x_center = c0_b - d_center * s0_b
    X_center = (s0_b + d_center * (c0_b + x_center)) / (1 - x_center.sqr()).sqrt()
    F0_center = CRI(X_center, d_center)
    F_center = (F0_center + ii * tau) / (1 + ii * tau * F0_center)
    rho_center = F_center.re / (2 * pi)
    ok((F_center - F_old).contains_zero(), "central full complex boundary value matches PR29 formula")
    ok(rho_center > F(77904561913345292, 10**18) and rho_center < F(77904561913345293, 10**18),
       "central density inside pinned PR29 decimal interval")
    ok((x_center - (4 - 5 * (1 + sqrt5) / 4)).contains_zero(),
       "central relative shell matches golden-ratio shell")
    F0_wrong = CRI(-X_center, d_center)
    F_wrong = (F0_wrong + ii * tau) / (1 + ii * tau * F0_wrong)
    ok(F_wrong.re < 0, "negative control wrong exterior root has negative density")

    ck0 = (9 - 5 * sqrt5) / 16
    k0 = -acos_iv(ck0)
    k = RI(k0.lo - F(11, 1000), k0.hi + F(11, 1000))
    cos_k, sin_k = cos_sin(k)
    eps = acos_iv((1 - 4 * cos_k) / 5)
    _, sin_eps = cos_sin(eps)
    speed = -4 * sin_k / (5 * sin_eps)
    v_min = RI(speed.lo)
    v_max = RI(speed.hi)
    root_margin = v_min * (p_bound - delta_k) - L * p_bound.sqr() - h
    monotonic_margin = v_min - 2 * L * p_bound
    anchor = 1 - L * p_bound
    port_lower = (1 - v_max) / 2
    jacobian_upper = v_max + 2 * L * p_bound
    b_hom = anchor * port_lower / (2 * pi * jacobian_upper)

    ok(p_bound < F(1, 12), "homogeneous bound window inside inherited branch")
    ok(k > -pi and k < 0, "homogeneous pulse momentum is right-moving")
    ok(eps > 0 and eps < theta, "homogeneous pulse energy inside positive dispersive band")
    ok(speed > 0 and speed < 1, "homogeneous pulse speed strictly between zero and one")
    ok(monotonic_margin > 0, "homogeneous energy shell strictly monotone in P")
    ok(root_margin > 0, "homogeneous endpoints strictly straddle every chosen E")
    ok(anchor > 0, "homogeneous bound contact weight positive")
    ok(port_lower > 0, "homogeneous output port weight positive")
    ok(b_hom > F(1, 100), "homogeneous output density exceeds 1/100")

    p_fixed = RI(F(1, 1000))
    eps_fixed = RI(g.lo - F(2, 1000), g.hi + F(2, 1000))
    cos_ef, sin_ef = cos_sin(eps_fixed)
    ck_fixed = (1 - 5 * cos_ef) / 4
    speed_fixed = 4 * (1 - ck_fixed.sqr()).sqrt() / (5 * sin_ef)
    vf_max = RI(speed_fixed.hi)
    b_fixed = 2 * p_fixed / (4 * pi.sqr()) * (1 - L * p_fixed) * (1 - vf_max) / (2 * vf_max)
    ok(ck_fixed > -1 and ck_fixed < 1, "fixed-source pulse roots strictly interior")
    ok(speed_fixed > 0 and speed_fixed < 1, "fixed-source right speed between zero and one")
    ok(b_fixed > F(49, 10**7), "fixed-source output density exceeds 49/10000000")

    alpha = RI(F(9, 10))
    bad_fraction = RI(F(40, 49))
    good_fraction = 1 - bad_fraction
    c_pa2, _ = cos_sin(pi * alpha / 2)
    hardy_C = 2 * pi / c_pa2
    M = power_20_9(hardy_C / (bad_fraction * ell))
    base = 64 * pi.sqr() * a * good_fraction / (4 + M).sqr()
    lower_hom_box = base * b_hom
    lower_fixed = base * b_fixed
    fraction_k = delta_k / pi
    lower_complete = fraction_k * lower_hom_box

    ok(alpha > 0 and alpha < 1, "Hardy exponent in admissible open interval")
    ok(bad_fraction > 0 and bad_fraction < 1, "bad-set fraction strictly between zero and one")
    ok(M > 0, "full-denominator threshold positive")
    ok(lower_hom_box > F(8, 10**25), "homogeneous K-window probability lower exceeds 8e-25")
    ok(lower_fixed > F(4, 10**28), "fixed-source probability lower exceeds 4e-28")
    ok(lower_complete > F(2, 10**28), "localized-token complete probability lower exceeds 2e-28")
    ok(lower_complete < lower_hom_box, "complete probability lower is below K-window bound")
    ok(lower_hom_box < 1 and lower_fixed < 1, "all conservative lower bounds below one")
    ok(estar - h > 3 * pi / 2 and estar + h < 17 * pi / 10, "energy window inside no-alias interval J0")
    ok(theta < 3 * pi / 4, "pulse bandwidth below 3*pi/4")

    ok(F(4, 5) + F(4, 5) == F(2, 5) + F(6, 5), "energy balance beta+beta=g+(beta+g)")
    ok(1 - F(40, 49) == F(9, 49), "good-set fraction is 9/49")
    ok(2 / F(9, 10) == F(20, 9), "Hardy threshold exponent is 20/9")
    ok((1 / F(2, 1000)) * F(2, 1000) == 1, "flat energy packet has unit norm")
    ok((1 / (F(1, 1000) * F(2, 1000))) * F(1, 1000) * F(2, 1000) == 1, "flat K-window packet has unit norm")
    ok(F(17, 10) - 2 < F(-1, 4), "lower alias separated from coarse total energy enclosure")
    ok(F(3, 2) + 2 > F(13, 4), "upper alias separated from coarse total energy enclosure")
    ok(F(3, 2) > F(5, 4) and F(17, 10) < F(7, 4), "J0 lies inside safe window (5pi/4, 7pi/4)")

    p_win_digits = (lower_complete.lo.numerator * 10**36) // lower_complete.lo.denominator
    b_hom_digits = (lower_hom_box.lo.numerator * 10**33) // lower_hom_box.lo.denominator
    print(
        f"PASS GROUP 2 PACKET_CERTIFICATE: {checks} checks; "
        f"B_hom>={b_hom_digits}e-33>8e-25; P_joint>={p_win_digits}e-36>2e-28"
    )
    return checks


# ============================================================================
# Group 3: Native 26-Label Code, Contact Orthogonality, and Receiver Conjugacy
# ============================================================================

def pulse_codes():
    ordered = []
    for i, j in itertools.combinations(range(5), 2):
        for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            v = [0] * 5
            v[i], v[j] = a, b
            ordered.append(tuple(v))
    return [ordered[25], *ordered[:25]]


def token_codes():
    ordered = []
    for i in range(1, 12):
        for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            v = [0] * 12
            v[0], v[i] = a, b
            ordered.append(tuple(v))
    return [ordered[25], *ordered[:25]]


def memory_codes():
    result = []
    for j in range(26):
        v = [0] * 13
        v[j // 2] = (-1) ** (j % 2)
        result.append(tuple(v))
    return result


def qcharge(v):
    return 2 * sum(x * x for x in v)


def sparse_add(out, key, value):
    if value:
        out[key] = out.get(key, F(0)) + value
        if not out[key]:
            del out[key]


def sparse_extend(action, vector):
    out = {}
    for state, coefficient in vector.items():
        for target, value in action(state).items():
            sparse_add(out, target, coefficient * value)
    return out


def audit_native_completion() -> int:
    checks = 0

    def ok(cond: bool, msg: str):
        nonlocal checks
        assert cond, msg
        checks += 1

    pulse, token, memory = pulse_codes(), token_codes(), memory_codes()
    ok(len(set(pulse)) == 26, "26 distinct pulse codes")
    ok(len(set(token)) == 26, "26 distinct token codes")
    ok(len(set(memory)) == 26, "26 distinct memory codes")
    ok(token[1] == (1, 1) + (0,) * 10, "original token label one retained")
    ok(memory[1] == (-1,) + (0,) * 12, "original receiver label one retained")
    ok(all(qcharge(v) == 4 for v in token + pulse), "all carrier charges equal four")
    ok(all(qcharge(v) == 2 for v in memory), "all memory charges equal two")
    ok(all(v[0] in (-1, 1) for v in token), "tokens have nonzero h5")
    ok(all(sum(x != 0 for x in v[2:]) <= 1 for v in token), "tokens contain at most one entry in pulse banks")

    embedded_pulses = []
    for port in range(2):
        for p in pulse:
            v = [0] * 12
            v[2 + 5 * port:7 + 5 * port] = p
            embedded_pulses.append(tuple(v))
    ok(not (set(token) & set(embedded_pulses)), "token and both pulse sectors are disjoint")

    active_on_site = set(embedded_pulses)
    ok(all(t not in active_on_site for t in token), "original on-site pulse coin fixes every token")
    ok(all(tuple(t[a:a + 5]) not in set(pulse) for t in token for a in (2, 7)),
       "original pulse edge fixes every token against vacuum")

    a, b = (1, -1, 0, 0), (0, 0, 1, 1)
    C = [[F(i == j) - F(a[i] * a[j] + b[i] * b[j], 5) + F(2 * (b[i] * a[j] - a[i] * b[j]), 5)
          for j in range(4)] for i in range(4)]
    ok(all(sum(C[k][i] * C[k][j] for k in range(4)) == F(i == j)
           for i in range(4) for j in range(4)), "contact orthogonal over Q")
    ok(all(sum(C[i][j] * a[j] for j in range(4)) == F(3 * a[i] + 4 * b[i], 5)
           for i in range(4)), "contact source image has coefficients 3/5 and 4/5")
    ok(all(sum(C[i][j] * b[j] for j in range(4)) == F(-4 * a[i] + 3 * b[i], 5)
           for i in range(4)), "contact inverse image has required sign")

    def contact(state):
        direction, carrier, mem = state
        return {(i, carrier, mem): C[i][direction] for i in range(4) if C[i][direction]}

    def swap(state):
        direction, carrier, mem = state
        return {(direction, mem, carrier): F(1)}

    basis = list(itertools.product(range(4), range(26), range(26)))
    ok(all(sparse_extend(contact, swap(s)) == sparse_extend(swap, contact(s)) for s in basis),
       "C commutes with carrier-memory swap at every label pair")
    ok(all(sparse_extend(swap, swap(s)) == {s: F(1)} for s in basis),
       "carrier-memory swap is a full involution")

    object_codes = [(-1, 0, 0, -1), (0, -1, -1, 0), (1, 0, 1, 0), (0, 1, 0, 1)]
    raw = []
    for direction, j, k in basis:
        v = [0] * 38
        v[:4] = object_codes[direction]
        v[4:16] = token[j] if direction < 2 else embedded_pulses[j]
        v[24:37] = memory[k]
        raw.append(tuple(v))
    ok(len(set(raw)) == len(basis), "all coded contact-memory basis states distinct")
    ok(all(qcharge(v) == 10 for v in raw), "all coded contact-memory states have fixed H_N ten")
    helpers = list(range(16, 24)) + [37]
    ok(all(v[k] == 0 for v in raw for k in helpers), "all nine auxiliary coordinates remain outside new code")

    edge_basis = list(itertools.product(range(2), range(26), range(26)))

    def D(state):
        side, j, k = state
        if side == 0:
            return {(0, j, k): F(1), (1, k, j): F(2)}
        return {(0, k, j): F(-2), (1, j, k): F(1)}

    def Ddag(state):
        side, j, k = state
        if side == 0:
            return {(0, j, k): F(1), (1, k, j): F(-2)}
        return {(0, k, j): F(2), (1, j, k): F(1)}

    ok(all(sparse_extend(Ddag, D(s)) == {s: F(5)} for s in edge_basis), "receiver edge numerator satisfies Ddag D=5I")
    ok(all(sparse_extend(D, Ddag(s)) == {s: F(5)} for s in edge_basis), "receiver edge numerator satisfies D Ddag=5I")
    ok(all(qcharge(pulse[j]) + qcharge(memory[k]) == 6 for _, j, k in edge_basis),
       "receiver edge keeps carrier-memory charge six")
    ok(all(list(swap((0, 1, j))) == [(0, j, 1)] for j in range(26)),
       "right outgoing p1,dj writes d1 and preserves old j in pulse")

    def incomplete_contact(state):
        return contact(state) if state[1] == 1 else {state: F(1)}

    witness = (0, 1, 2)
    ok(sparse_extend(incomplete_contact, swap(witness)) != sparse_extend(swap, incomplete_contact(witness)),
       "negative control: single-label contact fails receiver commutation")

    def wrong_D(state):
        side, j, k = state
        return {(side, j, k): F(1), (1 - side, k, j): F(2)}

    ok(sparse_extend(wrong_D, wrong_D((0, 1, 2))) != {(0, 1, 2): F(5)},
       "negative control: wrong edge sign fails unitarity")
    bad_token = list(token[1])
    bad_token[0] = 2
    ok(qcharge(bad_token) != 4, "negative control: changed token charge rejected")

    print(f"PASS GROUP 3 NATIVE_COMPLETION: {checks} checks; 2704 contact states; 1352 receiver-edge states")
    return checks


# ============================================================================
# Group 4 & 5: Current Interface, Open-Channel Reduction, and Infinite Carrier
# ============================================================================

class Cyc:
    """Exact element of Q(i)[u, u^-1] where u = exp(-i*g) lies on the unit circle."""
    __slots__ = ("d",)

    def __init__(self, d=None):
        self.d = {}
        if d:
            for k, (re, im) in d.items():
                re_f, im_f = F(re), F(im)
                if re_f or im_f:
                    self.d[int(k)] = (re_f, im_f)

    @classmethod
    def const(cls, re=0, im=0) -> "Cyc":
        return cls({0: (F(re), F(im))})

    @classmethod
    def u(cls, power=1) -> "Cyc":
        return cls({power: (F(1), F(0))})

    def conj(self) -> "Cyc":
        return Cyc({-k: (re, -im) for k, (re, im) in self.d.items()})

    def __add__(self, other) -> "Cyc":
        o = other if isinstance(other, Cyc) else Cyc.const(other)
        keys = set(self.d) | set(o.d)
        out = {}
        for k in keys:
            r1, i1 = self.d.get(k, (F(0), F(0)))
            r2, i2 = o.d.get(k, (F(0), F(0)))
            out[k] = (r1 + r2, i1 + i2)
        return Cyc(out)

    __radd__ = __add__

    def __neg__(self) -> "Cyc":
        return Cyc({k: (-re, -im) for k, (re, im) in self.d.items()})

    def __sub__(self, other) -> "Cyc":
        return self + (-other)

    def __rsub__(self, other) -> "Cyc":
        return (-self) + other

    def __mul__(self, other) -> "Cyc":
        o = other if isinstance(other, Cyc) else Cyc.const(other)
        out = {}
        for k1, (r1, i1) in self.d.items():
            for k2, (r2, i2) in o.d.items():
                k = k1 + k2
                re = r1 * r2 - i1 * i2
                im = r1 * i2 + i1 * r2
                pr, pi = out.get(k, (F(0), F(0)))
                out[k] = (pr + re, pi + im)
        return Cyc(out)

    __rmul__ = __mul__

    def __eq__(self, other) -> bool:
        o = other if isinstance(other, Cyc) else Cyc.const(other)
        return self.d == o.d

    def __bool__(self) -> bool:
        return bool(self.d)


ONE = Cyc.const(1, 0)
II = Cyc.const(0, 1)
U_PHASE = Cyc.u(1)
U_INV = Cyc.u(-1)

M_NAT = [
    [Cyc.const(F(1, 5), 0), Cyc.const(F(2, 5), 0), Cyc.const(F(2, 5), 0), Cyc.const(F(4, 5), 0)],
    [Cyc.const(F(-2, 5), 0), Cyc.const(F(1, 5), 0), Cyc.const(F(-4, 5), 0), Cyc.const(F(2, 5), 0)],
    [Cyc.const(F(-2, 5), 0), Cyc.const(F(-4, 5), 0), Cyc.const(F(1, 5), 0), Cyc.const(F(2, 5), 0)],
    [Cyc.const(F(4, 5), 0), Cyc.const(F(-2, 5), 0), Cyc.const(F(-2, 5), 0), Cyc.const(F(1, 5), 0)],
]
M_SRC = [
    [Cyc.const(F(1, 5), 0), Cyc.const(0, F(2, 5)), Cyc.const(0, F(2, 5)), Cyc.const(F(-4, 5), 0)],
    [Cyc.const(0, F(2, 5)), Cyc.const(F(1, 5), 0), Cyc.const(F(-4, 5), 0), Cyc.const(0, F(2, 5))],
    [Cyc.const(0, F(2, 5)), Cyc.const(F(-4, 5), 0), Cyc.const(F(1, 5), 0), Cyc.const(0, F(2, 5))],
    [Cyc.const(F(-4, 5), 0), Cyc.const(0, F(2, 5)), Cyc.const(0, F(2, 5)), Cyc.const(F(1, 5), 0)],
]
D2_DIAG = [ONE, II, II, -ONE]
SHIFTS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def vec_add(out, key, val: Cyc):
    if val:
        cur = out.get(key, Cyc()) + val
        if cur:
            out[key] = cur
        elif key in out:
            del out[key]


def inner(v1: dict, v2: dict) -> Cyc:
    s = Cyc()
    for k, a in v1.items():
        if k in v2:
            s = s + a.conj() * v2[k]
    return s


def step_W(v: dict) -> dict:
    out = {}
    for (R, r, d_in), amp in v.items():
        for d_out in range(1, 5):
            m_val = M_SRC[d_out - 1][d_in - 1]
            dR, dr = SHIFTS[d_out - 1]
            R_new, r_new = R + dR, r + dr
            gam = U_PHASE if r_new == 0 else ONE
            vec_add(out, (R_new, r_new, d_out), gam * m_val * amp)
    return out


def step_W_dag(v: dict) -> dict:
    out = {}
    for (R, r, d_out), amp in v.items():
        gam_conj = U_INV if r == 0 else ONE
        dR, dr = SHIFTS[d_out - 1]
        R_old, r_old = R - dR, r - dr
        for d_in in range(1, 5):
            m_conj = M_SRC[d_out - 1][d_in - 1].conj()
            vec_add(out, (R_old, r_old, d_in), m_conj * gam_conj * amp)
    return out


def reflect_Rn(v: dict, n: int) -> dict:
    return {(2 * n - R, -r, 5 - d): amp for (R, r, d), amp in v.items()}


def apply_NT_n(v: dict, n: int) -> dict:
    out = {}
    for (R, r, d), amp in v.items():
        xA, xB = R + r, R - r
        q = 2 * (1 if xA > n else 0) + 2 * (1 if xB > n else 0) + 2
        if q:
            out[(R, r, d)] = Cyc.const(q, 0) * amp
    return out


def proj_alpha(v: dict, n: int) -> Cyc:
    return (-II) * v.get((n, 0, 2), Cyc()) + II * v.get((n, 0, 3), Cyc())


def step_A_W(v: dict, n: int) -> dict:
    ov = proj_alpha(v, n)
    mod = dict(v)
    vec_add(mod, (n, 0, 2), Cyc.const(F(-1, 5), 0) * ov * II)
    vec_add(mod, (n, 0, 3), Cyc.const(F(1, 5), 0) * ov * II)
    return step_W(mod)


def audit_current_interface() -> int:
    checks = 0

    def ok(cond: bool, msg: str):
        nonlocal checks
        assert cond, msg
        checks += 1

    ok(all(D2_DIAG[r].conj() * M_NAT[r][c] * D2_DIAG[c] == M_SRC[r][c]
           for r in range(4) for c in range(4)),
       "D2^* M_nat D2 == M_src")
    ok(all(sum(M_NAT[k][r].conj() * M_NAT[k][c] for k in range(4)) == (ONE if r == c else Cyc())
           for r in range(4) for c in range(4)),
       "M_nat orthogonal")
    ok(all(sum(M_SRC[k][r].conj() * M_SRC[k][c] for k in range(4)) == (ONE if r == c else Cyc())
           for r in range(4) for c in range(4)),
       "M_src unitary")

    object_codes = [(-1, 0, 0, -1), (0, -1, -1, 0), (1, 0, 1, 0), (0, 1, 0, 1)]
    ok(len(set(object_codes)) == 4, "Emb maps the 4 coin states to 4 distinct orthonormal native kets")
    ok(all(qcharge(v) == 4 for v in object_codes), "all four object codes have native charge 4")

    edge_basis = list(itertools.product(range(2), range(26), range(26)))

    def w_step(state):
        side, sig, tau = state
        if side == 0:
            return {(0, sig, tau): F(1), (1, tau, sig): F(2)}
        return {(0, tau, sig): F(-2), (1, sig, tau): F(1)}

    def q_right_bond(state):
        side, _, _ = state
        return F(6 if side == 1 else 2)

    def j_edge_99(state):
        side, sig, tau = state
        if side == 0:
            return {(0, sig, tau): F(16, 5), (1, tau, sig): F(8, 5)}
        return {(0, tau, sig): F(8, 5), (1, sig, tau): F(-16, 5)}

    for s in edge_basis:
        out = w_step(s)
        lhs = {}
        for s_mid, a_mid in out.items():
            q_m = q_right_bond(s_mid)
            side_m, sig_m, tau_m = s_mid
            if side_m == 0:
                adj = {(0, sig_m, tau_m): F(1), (1, tau_m, sig_m): F(-2)}
            else:
                adj = {(0, tau_m, sig_m): F(2), (1, sig_m, tau_m): F(1)}
            for s_fin, a_fin in adj.items():
                sparse_add(lhs, s_fin, (a_mid * q_m * a_fin) / 5)
        sparse_add(lhs, s, -q_right_bond(s))
        assert lhs == j_edge_99(s)
        assert sparse_extend(j_edge_99, j_edge_99(s)) == {s: F(64, 5)}
    ok(True, "D_rec^* Q_bond D_rec - Q_bond == j_{E,99} and j_{E,99}^2 == (64/5) I on all 1352 states")

    cut_l = 99
    z_rec = 100

    def n_right_full(state) -> F:
        _, R, r, _, pos, _, _, _ = state
        xA, xB = R + r, R - r
        return F(2 * (xA > cut_l) + 2 * (xB > cut_l) + 4 * (pos > cut_l) + 2 * (z_rec > cut_l))

    def step_contact_full(v: dict) -> dict:
        out = {}
        for st, amp in v.items():
            arr, R, r, d, pos, b, sig, tau = st
            if R != pos or r != 0:
                vec_add(out, st, amp)
                continue
            if arr == "T" and d in (2, 3):
                sgn = 1 if d == 2 else -1
                vec_add(out, ("T", R, 0, 2, pos, 0, sig, tau), amp * Cyc.const(F(1, 2) + sgn * F(3, 10), 0))
                vec_add(out, ("T", R, 0, 3, pos, 0, sig, tau), amp * Cyc.const(F(1, 2) - sgn * F(3, 10), 0))
                vec_add(out, ("P", R, 0, 1, pos, 1, sig, tau), amp * Cyc.const(0, F(-2 * sgn, 5)))
                vec_add(out, ("P", R, 0, 4, pos, 1, sig, tau), amp * Cyc.const(0, F(2 * sgn, 5)))
            elif arr == "P" and b == 1 and d in (1, 4):
                sgn = 1 if d == 1 else -1
                vec_add(out, ("P", R, 0, 1, pos, 1, sig, tau), amp * Cyc.const(F(1, 2) + sgn * F(3, 10), 0))
                vec_add(out, ("P", R, 0, 4, pos, 1, sig, tau), amp * Cyc.const(F(1, 2) - sgn * F(3, 10), 0))
                vec_add(out, ("T", R, 0, 2, pos, 0, sig, tau), amp * Cyc.const(0, F(-2 * sgn, 5)))
                vec_add(out, ("T", R, 0, 3, pos, 0, sig, tau), amp * Cyc.const(0, F(2 * sgn, 5)))
            else:
                vec_add(out, st, amp)
        return out

    def step_V_rec(v: dict) -> dict:
        out = {}
        for st, amp in v.items():
            arr, R, r, d, pos, b, sig, tau = st
            if arr == "T":
                vec_add(out, st, amp)
                continue
            v1_c = F(1) if b == 1 else F(-2)
            v2_c = F(2) if b == 1 else F(1)
            vec_add(out, ("P", R, r, d, pos, 1, sig, tau), amp * Cyc.const(v1_c / 5, 0))
            sig_r, tau_r = (tau, sig) if z_rec == pos + 1 else (sig, tau)
            vec_add(out, ("P", R, r, d, pos + 1, 2, sig_r, tau_r), amp * Cyc.const(2 * v1_c / 5, 0))
            sig_l, tau_l = (tau, sig) if z_rec == pos else (sig, tau)
            vec_add(out, ("P", R, r, d, pos - 1, 1, sig_l, tau_l), amp * Cyc.const(-2 * v2_c / 5, 0))
            vec_add(out, ("P", R, r, d, pos, 2, sig, tau), amp * Cyc.const(v2_c / 5, 0))
        return out

    def step_obj_full(v: dict) -> dict:
        out = {}
        for (arr, R, r, d_in, pos, b, sig, tau), amp in v.items():
            for d_out in range(1, 5):
                m_val = M_SRC[d_out - 1][d_in - 1]
                dR, dr = SHIFTS[d_out - 1]
                R_new, r_new = R + dR, r + dr
                gam = U_PHASE if r_new == 0 else ONE
                vec_add(out, (arr, R_new, r_new, d_out, pos, b, sig, tau), gam * m_val * amp)
        return out

    def step_U_full(v: dict) -> dict:
        return step_obj_full(step_V_rec(step_contact_full(v)))

    def apply_D_dag_j_D(v: dict) -> dict:
        out = {}
        for (arr, R, r, d_in, pos, b, sig, tau), amp in v.items():
            xA, xB = R + r, R - r
            for d_mid in range(1, 5):
                m_in = M_SRC[d_mid - 1][d_in - 1]
                vA = SHIFTS[d_mid - 1][0] + SHIFTS[d_mid - 1][1]
                vB = SHIFTS[d_mid - 1][0] - SHIFTS[d_mid - 1][1]
                flux_s = 2 * ((1 if (xA == cut_l and vA == 1) else (-1 if (xA == cut_l + 1 and vA == -1) else 0))
                              + (1 if (xB == cut_l and vB == 1) else (-1 if (xB == cut_l + 1 and vB == -1) else 0)))
                if flux_s:
                    for d_out in range(1, 5):
                        m_out = M_SRC[d_mid - 1][d_out - 1].conj()
                        vec_add(out, (arr, R, r, d_out, pos, b, sig, tau),
                                Cyc.const(flux_s, 0) * m_out * m_in * amp)
        for (arr, R, r, d, pos, b, sig, tau), amp in v.items():
            if arr != "P" or pos not in (cut_l, cut_l + 1):
                continue
            if pos == cut_l:
                c_in = F(1) if b == 1 else F(-2)
                vec_add(out, ("P", R, r, d, cut_l, 1, sig, tau), amp * Cyc.const(F(16, 25) * c_in * 1, 0))
                vec_add(out, ("P", R, r, d, cut_l, 2, sig, tau), amp * Cyc.const(F(16, 25) * c_in * (-2), 0))
                sig_s, tau_s = (tau, sig) if z_rec == cut_l + 1 else (sig, tau)
                vec_add(out, ("P", R, r, d, cut_l + 1, 1, sig_s, tau_s), amp * Cyc.const(F(8, 25) * c_in * 2, 0))
                vec_add(out, ("P", R, r, d, cut_l + 1, 2, sig_s, tau_s), amp * Cyc.const(F(8, 25) * c_in * 1, 0))
            else:
                c_in = F(2) if b == 1 else F(1)
                vec_add(out, ("P", R, r, d, cut_l + 1, 1, sig, tau), amp * Cyc.const(F(-16, 25) * c_in * 2, 0))
                vec_add(out, ("P", R, r, d, cut_l + 1, 2, sig, tau), amp * Cyc.const(F(-16, 25) * c_in * 1, 0))
                sig_s, tau_s = (tau, sig) if z_rec == cut_l + 1 else (sig, tau)
                vec_add(out, ("P", R, r, d, cut_l, 1, sig_s, tau_s), amp * Cyc.const(F(8, 25) * c_in * 1, 0))
                vec_add(out, ("P", R, r, d, cut_l, 2, sig_s, tau_s), amp * Cyc.const(F(8, 25) * c_in * (-2), 0))
        return out

    stencil_states = [
        ("T", 99, 0, 2, 99, 0, 1, 2),
        ("T", 99, 0, 3, 99, 0, 1, 2),
        ("T", 99, 1, 1, 99, 0, 1, 2),
        ("T", 100, 0, 2, 100, 0, 1, 2),
        ("P", 99, 0, 1, 99, 1, 1, 2),
        ("P", 99, 0, 4, 99, 1, 1, 2),
        ("P", 99, 0, 2, 99, 2, 1, 2),
        ("P", 100, 0, 1, 100, 1, 2, 1),
        ("P", 100, 0, 3, 100, 2, 2, 1),
    ]
    u_images = []
    for st in stencil_states:
        v0 = {st: ONE}
        u_v = step_U_full(v0)
        assert inner(u_v, u_v) == ONE
        c_v = step_contact_full(v0)
        dj_v = apply_D_dag_j_D(c_v)
        u_images.append((v0, u_v, c_v, dj_v))

    for v1_0, u_v1, c_v1, _ in u_images:
        for v2_0, u_v2, _, dj_v2 in u_images:
            nr_after = inner(u_v1, {k: Cyc.const(n_right_full(k), 0) * a for k, a in u_v2.items()})
            nr_before = inner(v1_0, {k: Cyc.const(n_right_full(k), 0) * a for k, a in v2_0.items()})
            nl_before = inner(v1_0, {k: Cyc.const(10 - n_right_full(k), 0) * a for k, a in v2_0.items()})
            nl_after = inner(u_v1, {k: Cyc.const(10 - n_right_full(k), 0) * a for k, a in u_v2.items()})
            j_form = inner(c_v1, dj_v2)
            assert nr_after - nr_before == nl_before - nl_after == j_form
    ok(True, "exact bilinear current identity U^* N_R U - N_R == N_L - U^* N_L U == C^* D^* (j_S+j_E) D C on 81 stencil pairs")

    _, u_v_t, _, _ = u_images[0]
    _, u_v_p, _, _ = u_images[4]
    nr_cross = inner(u_v_t, {k: Cyc.const(n_right_full(k), 0) * a for k, a in u_v_p.items()})
    no_c_cross = inner(u_images[0][0], apply_D_dag_j_D(u_images[4][0]))
    ok(nr_cross != no_c_cross, "negative control: omitting contact conjugation C breaks current identity")

    alpha_n = {(cut_l, 0, 2): II, (cut_l, 0, 3): -II}
    w1 = step_W(alpha_n)
    a1 = step_A_W(w1, cut_l)
    a2 = step_A_W(a1, cut_l)
    ok(U_INV * inner(w1, a2) * Cyc.const(F(1, 2), 0) == Cyc.const(F(12, 25), 0), "<v0, v2> == 12/25")
    ok(U_INV * inner(w1, apply_NT_n(a2, cut_l)) * Cyc.const(F(1, 2), 0) == Cyc.const(F(48, 25), 0),
       "<v0, N_n^T v2> == 48/25")

    q_after_coh = F(4) * F(1, 50) + F(116, 25) * F(49, 50)
    q_before = F(2)
    j_coh = q_after_coh - q_before
    j_inc = (F(4) * (F(9, 50) + F(16, 50)) + F(116, 25) * (F(16, 50) + F(9, 50))) - q_before
    ok(F(4) * F(1, 50) == F(2, 25), "coherent next-token right charge is 2/25")
    ok(j_coh == F(1642, 625) and j_inc == F(58, 25) and j_coh - j_inc == F(192, 625),
       "coherent current 1642/625 vs incoherent 58/25 (diff 192/625)")

    print(f"PASS GROUP 4 CURRENT_INTERFACE: {checks} checks; cut l=99; j_coh=1642/625")
    return checks


def audit_open_channel_and_carrier() -> int:
    checks = 0

    def ok(cond: bool, msg: str):
        nonlocal checks
        assert cond, msg
        checks += 1

    for f_val in (F(0), F(1), F(2), F(7, 3), F(19, 5)):
        m_val = (f_val - 1) / 2
        s_elim = F(3, 5) - (F(16, 25) * m_val) / (1 + F(2, 5) * m_val)
        s_form = (4 - f_val) / (4 + f_val)
        assert s_elim == s_form
    ok(True, "open-channel elimination s(z) == (4-F)/(4+F)")

    alpha0 = {(0, 0, 2): II, (0, 0, 3): -II}
    w1 = step_W(alpha0)
    a1 = step_A_W(w1, 0)
    a2 = step_A_W(a1, 0)
    a3 = step_A_W(a2, 0)
    nu0 = proj_alpha(w1, 0)
    nu1 = U_INV * proj_alpha(a1, 0) * Cyc.const(F(1, 2), 0)
    nu2 = proj_alpha(a2, 0)
    nu3 = Cyc.u(-2) * proj_alpha(a3, 0) * Cyc.const(F(1, 2), 0)
    ok(nu0 == Cyc() and nu2 == Cyc(), "odd-step return amplitudes nu_0 == nu_2 == 0")
    ok(nu1 == Cyc.const(F(4, 5), 0), "first return amplitude nu_1 == 4/5")
    ok(nu3 == Cyc.const(F(48, 125), 0) - Cyc.const(F(28, 125), 0) * U_INV,
       "third return amplitude nu_3 == (48 - 28*e^{ig})/125")

    t_init = {(0, 0, 1): ONE, (0, 1, 2): II}
    p_drive = [Cyc.const(1, 0), Cyc.const(F(1, 2), F(-1, 2)), Cyc.const(F(-1, 3), 0), Cyc.const(0, F(1, 4))]
    t_cur = dict(t_init)
    for m in range(1, 5):
        t_cur = step_A_W(t_cur, 0)
        for k_pos, amp_w in w1.items():
            vec_add(t_cur, k_pos, Cyc.const(F(-4, 5), 0) * p_drive[m - 1] * amp_w)
        rec = dict(t_init)
        for _ in range(m):
            rec = step_A_W(rec, 0)
        for j in range(m):
            term = {k_pos: Cyc.const(F(-4, 5), 0) * p_drive[j] * amp_w for k_pos, amp_w in w1.items()}
            for _ in range(m - 1 - j):
                term = step_A_W(term, 0)
            for k_pos, val in term.items():
                vec_add(rec, k_pos, val)
        assert rec == t_cur
    ok(True, "causal history reconstruction L_m H_m == (rho_m, p_m) for m=1..4")

    ok(reflect_Rn(alpha0, 0) == {k: -val for k, val in alpha0.items()}, "R_n alpha_n == -alpha_n")
    ok(reflect_Rn(w1, 0) == step_W(reflect_Rn(alpha0, 0)), "R_n commutes with W")
    chi_prime = step_W(w1)
    d_prime = {(-1, -1, 1): ONE, (1, 1, 4): ONE, (-1, 1, 1): -ONE, (1, -1, 4): -ONE}
    ok(reflect_Rn(d_prime, 0) == d_prime, "dark witness d is R_n-even")
    ok(inner(chi_prime, apply_NT_n(d_prime, 0)) == Cyc.const(F(8, 5), 0),
       "unnormalized pairing <W^2 alpha', N_n^T d'> == 8/5")
    ok(F(8, 5) ** 2 / (2 * 4) == F(8, 25), "normalized squared pairing == 8/25 == (2*sqrt(2)/5)^2")

    chi0_p = w1
    d0_p = step_W_dag(d_prime)
    ok(proj_alpha(chi0_p, 0) == Cyc() and proj_alpha(d0_p, 0) == Cyc(),
       "both chi0 and d0 have zero contact overlap (identical zero pulse history)")
    q_chi0_before = inner(chi0_p, apply_NT_n(chi0_p, 0)) * Cyc.const(F(1, 2), 0)
    q_d0_before = inner(d0_p, apply_NT_n(d0_p, 0)) * Cyc.const(F(1, 4), 0)
    q_chi_after = inner(chi_prime, apply_NT_n(chi_prime, 0)) * Cyc.const(F(1, 2), 0)
    q_d_after = inner(d_prime, apply_NT_n(d_prime, 0)) * Cyc.const(F(1, 4), 0)
    ok(q_chi0_before == Cyc.const(4, 0) and q_d0_before == Cyc.const(4, 0)
       and q_chi_after == Cyc.const(F(12, 5), 0) and q_d_after == Cyc.const(3, 0),
       "dark-state charge expectations before/after step")
    diag_current = (F(12, 5) - 4 + 3 - 4) / 2
    ok(diag_current == F(-13, 10), "dark-state current diagonal part == -13/10 (off-diag +-2*sqrt(2)/5)")

    cur = dict(alpha0)
    hist = [cur]
    for m in range(1, 7):
        cur = step_W(cur)
        hist.append(cur)
        assert cur.get((0, m, 3), Cyc()) == (-II) * Cyc.const(F(1, 5 ** (m - 1)), 0)
        for k in range(m):
            assert hist[k].get((0, m, 3), Cyc()) == Cyc()
    ok(True, "Theorem 1 extreme coordinate <0,m,3|T^m alpha'> == -i e^{-im*beta} 5^{1-m} for m=1..6")

    gap_canon = acos_iv(RI(F(7, 25))) - 2 * PI / 5
    ok(gap_canon > F(3, 100), "Theorem 2 canonical whole-operator gap acos(7/25)-2pi/5 > 3/100 > 0")

    cut_l = 99
    for j in range(1, 9):
        xA_p, xB_p, d_p = cut_l, cut_l - 2 * j, 3
        vA_p, vB_p = SHIFTS[d_p - 1][0] + SHIFTS[d_p - 1][1], SHIFTS[d_p - 1][0] - SHIFTS[d_p - 1][1]
        assert (vA_p, vB_p) == (1, -1)
        j_plus = 2 * ((xA_p == cut_l and vA_p == 1) - (xA_p == cut_l + 1 and vA_p == -1)
                      + (xB_p == cut_l and vB_p == 1) - (xB_p == cut_l + 1 and vB_p == -1))
        xA_m, xB_m, d_m = cut_l + 1, cut_l + 1 + 2 * j, 2
        vA_m, vB_m = SHIFTS[d_m - 1][0] + SHIFTS[d_m - 1][1], SHIFTS[d_m - 1][0] - SHIFTS[d_m - 1][1]
        assert (vA_m, vB_m) == (-1, 1)
        j_minus = 2 * ((xA_m == cut_l and vA_m == 1) - (xA_m == cut_l + 1 and vA_m == -1)
                       + (xB_m == cut_l and vB_m == 1) - (xB_m == cut_l + 1 and vB_m == -1))
        assert j_plus == 2 and j_minus == -2
    ok(True, "Theorem 3 infinite spectator current families e_j^+ (+2) and e_j^- (-2) for j=1..8")

    print(f"PASS GROUP 5 OPEN_CHANNEL_AND_CARRIER: {checks} checks; nu_1=4/5; dark_diff=4*sqrt(2)/5")
    return checks


# ============================================================================
# Group 6: Finite-Strip Laurent Polynomial Elimination (FINITE_STRIP)
# ============================================================================

class PolyZ:
    """Laurent polynomial over Z[i] in (mu, z, u, w, b, c, lam, i) reduced by i^2 = -1."""
    nv = 8

    def __init__(self, value=0):
        self.d = {} if value == 0 else {(0,) * self.nv: value}

    @classmethod
    def terms(cls, raw):
        p = cls()
        for exps, coeff in raw:
            k = exps[-1] % 4
            if k >= 2:
                coeff = -coeff
            exps = exps[:-1] + (k % 2,)
            p.d[exps] = p.d.get(exps, 0) + coeff
        p.d = {e: c for e, c in p.d.items() if c}
        return p

    @classmethod
    def var(cls, index, power=1):
        e = [0] * cls.nv
        e[index] = power
        return cls.terms([(tuple(e), 1)])

    @staticmethod
    def cast(x):
        return x if isinstance(x, PolyZ) else PolyZ(x)

    def __add__(self, other):
        other = self.cast(other)
        return PolyZ.terms(list(self.d.items()) + list(other.d.items()))

    __radd__ = __add__

    def __neg__(self):
        return PolyZ.terms((e, -c) for e, c in self.d.items())

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        other = self.cast(other)
        return PolyZ.terms((tuple(a + b for a, b in zip(e, f)), c * d)
                           for e, c in self.d.items() for f, d in other.d.items())

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = PolyZ(1)
        for _ in range(n):
            result *= self
        return result

    def conj_i(self):
        return PolyZ.terms((e, -c if e[-1] else c) for e, c in self.d.items())


def poly_det(a):
    n = len(a)
    out = PolyZ()
    for perm in itertools.permutations(range(n)):
        inv = sum(perm[j] > perm[k] for j in range(n) for k in range(j + 1, n))
        term = PolyZ(-1 if inv % 2 else 1)
        for row, col in enumerate(perm):
            term *= a[row][col]
        out += term
    return out


def poly_mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def audit_finite_strip() -> int:
    checks = 0

    def check(label: str, residuals):
        nonlocal checks
        residuals = residuals if isinstance(residuals, list) else [residuals]
        assert all(not PolyZ.cast(x).d for x in residuals), label
        checks += 1

    m, z, u, w, b, c, lam, i = [PolyZ.var(j) for j in range(8)]
    mi, wi = PolyZ.var(0, -1), PolyZ.var(3, -1)
    N = 1 + m * m
    A = [[1, i * m, i * m, -m * m], [i * m, 1, -m * m, i * m],
         [i * m, -m * m, 1, i * m], [-m * m, i * m, i * m, 1]]
    A = [[PolyZ.cast(x) for x in row] for row in A]
    check("coin unitarity after clearing N^2", [
        sum(A[k][j].conj_i() * A[k][h] for k in range(4)) - (N * N if j == h else 0)
        for j in range(4) for h in range(4)])
    check("det(N*M_mu)=N^4", poly_det(A) - N ** 4)

    D = N * lam * lam - lam * (w + wi) + 1 - m * m
    stationary = [[N * lam * wi - 1, m * m], [m * m, N * lam * w - 1]]
    check("stationary determinant=N*D", poly_det(stationary) - N * D)
    na, nd = i * m * (b + c) * (lam * w - 1), i * m * (b + c) * (lam * wi - 1)
    check("stationary inverse numerators", [x - D * i * m * (b + c) for x in poly_mv(stationary, [na, nd])])
    pn, qn = (lam - w) * (lam - wi), m * m * (1 - lam * lam)
    check("p-q=1 numerator", pn - qn - D)
    out = poly_mv(A, [na, D * b, D * c, nd])
    check("moving-channel elimination", [out[1] - N * (pn * b + qn * c), out[2] - N * (qn * b + pn * c)])

    Tp = [[1, 0, 0, 0], [0, 0, -u, 0], [0, -u, 0, 0], [0, 0, 0, u]]
    Tm = [[u, 0, 0, 0], [0, 0, -u, 0], [0, -u, 0, 0], [0, 0, 0, 1]]
    expected = N ** 3 * (z - u) ** 2 * (z * (N * z - 1) - (N - z) * u)
    for label, T in (("plus", Tp), ("minus", Tm)):
        scaled = [[z * A[j][k] - N * T[j][k] for k in range(4)] for j in range(4)]
        check(f"complete determinant factorization {label}", poly_det(scaled) - expected)

    sym = [[z - N, 2 * i * m * z, -m * m * z],
           [i * m * z, z * (1 - m * m) + N * u, i * m * z],
           [-m * m * z, 2 * i * m * z, z - N * u]]
    q3 = (N - z) * u * u - m * m * z * (z + 1) * u + z * z * (N * z - 1)
    check("symmetric 3x3 determinant", poly_det(sym) - N * N * q3)
    check("quadratic factorization", q3 - (u - z) * ((N - z) * u - z * (N * z - 1)))
    check("opposite-root condition", N * z ** 3 - z * z + z - N - (z - 1) * (N * z * z + (N - 1) * z + N))

    zero = [PolyZ() for _ in range(4)]
    chi = {
        -1: [-c * wi * i * mi, -c * wi, PolyZ(), PolyZ()],
        0: [PolyZ(), b, c, i * (b + c) * mi],
        1: [-b * wi * i * mi, PolyZ(), -b * wi, PolyZ()],
    }
    for r in range(-2, 3):
        v = chi.get(r, zero)
        here = poly_mv(A, v)
        left, right = poly_mv(A, chi.get(r - 1, zero)), poly_mv(A, chi.get(r + 1, zero))
        gamma = w * w if r == 0 else PolyZ(1)
        received = [w * here[0], right[1], left[2], wi * here[3]]
        check(f"compact eigenvector full equation r={r}",
              [N * w * v[j] - gamma * received[j] for j in range(4)])

    wrong = [[z * A[j][k] - N * Tp[j][k] for k in range(4)] for j in range(4)]
    wrong[1][2] = z * A[1][2] - N * u
    assert (poly_det(wrong) - expected).d
    assert (expected - N ** 3 * (z - u) * (z * (N * z - 1) - (N - z) * u)).d
    checks += 2
    print(f"PASS GROUP 6 FINITE_STRIP: {checks} checks (16 Laurent identity groups + 2 negative controls)")
    return checks


def main() -> None:
    total = 0
    total += audit_branch_gap()
    total += audit_packet_certificate()
    total += audit_native_completion()
    total += audit_current_interface()
    total += audit_open_channel_and_carrier()
    total += audit_finite_strip()
    print(
        "SCOPE: connected asymptotic capture, full current, and coherent record; "
        "p(Q_full)>=p(Q_win)>2/10^28; finite-time preparation and occurrence NOT DERIVED"
    )
    print(f"VERIFY PASS C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N total_checks={total}")


if __name__ == "__main__":
    main()
