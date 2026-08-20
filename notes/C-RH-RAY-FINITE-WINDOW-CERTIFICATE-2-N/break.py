#!/usr/bin/env python3
"""Breaker-first exact attack for C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N.

The v56 synthetic result is exposed. This fresh v57 breaker is therefore a
replay and attack, not blind discovery. It is frozen before the new accepted
verifier exists. It imports no project code, uses only Fraction, and treats all
synthetic points as theorem controls, never as zeta zeros.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt


@dataclass(frozen=True, order=True)
class QC:
    re: Fraction
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "QC":
        z = as_qc(other)
        return QC(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self) -> "QC":
        return QC(-self.re, -self.im)

    def __sub__(self, other: object) -> "QC":
        return self + (-as_qc(other))

    def __rsub__(self, other: object) -> "QC":
        return as_qc(other) - self

    def __mul__(self, other: object) -> "QC":
        z = as_qc(other)
        return QC(
            self.re * z.re - self.im * z.im,
            self.re * z.im + self.im * z.re,
        )

    __rmul__ = __mul__

    def conj(self) -> "QC":
        return QC(self.re, -self.im)

    def norm2(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def inv(self) -> "QC":
        n = self.norm2()
        assert n != 0
        return QC(self.re / n, -self.im / n)

    def __truediv__(self, other: object) -> "QC":
        return self * as_qc(other).inv()

    def __rtruediv__(self, other: object) -> "QC":
        return as_qc(other) / self

    def __pow__(self, exponent: int) -> "QC":
        assert exponent >= 0
        out = QC(Fraction(1))
        base = self
        n = exponent
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out


def as_qc(value: object) -> QC:
    if isinstance(value, QC):
        return value
    if isinstance(value, Fraction):
        return QC(value)
    if isinstance(value, int):
        return QC(Fraction(value))
    raise TypeError(type(value))


def tau(z: QC) -> QC:
    return QC(-z.re, z.im)


def sqrt_fraction(x: Fraction) -> Fraction:
    assert x >= 0
    a = isqrt(x.numerator)
    b = isqrt(x.denominator)
    assert a * a == x.numerator and b * b == x.denominator
    return Fraction(a, b)


def modulus(z: QC) -> Fraction:
    return sqrt_fraction(z.norm2())


def modulus_lower(z: QC) -> Fraction:
    return max(abs(z.re), abs(z.im))


def trim(p: list[QC]) -> list[QC]:
    out = p[:]
    while len(out) > 1 and out[-1] == QC(0):
        out.pop()
    return out


def add_poly(p: list[QC], q: list[QC]) -> list[QC]:
    n = max(len(p), len(q))
    out = [QC(0) for _ in range(n)]
    for i in range(n):
        if i < len(p):
            out[i] = out[i] + p[i]
        if i < len(q):
            out[i] = out[i] + q[i]
    return trim(out)


def scale_poly(p: list[QC], a: QC) -> list[QC]:
    return trim([a * x for x in p])


def mul_poly(p: list[QC], q: list[QC]) -> list[QC]:
    out = [QC(0) for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = out[i + j] + x * y
    return trim(out)


def eval_poly(p: list[QC], z: QC) -> QC:
    out = QC(0)
    for x in reversed(p):
        out = out * z + x
    return out


def shift_poly(p: list[QC], r: int) -> list[QC]:
    assert r >= 0
    return [QC(0) for _ in range(r)] + p


def t_coord(beta: QC, c: Fraction) -> QC:
    return (QC(c) - beta.conj()).inv()


def interpolation_polynomial(
    window: frozenset[QC], target: tuple[QC, QC], c: Fraction, r: int
) -> tuple[list[QC], list[QC]]:
    alpha, alpha_tau = target
    assert alpha in window and alpha_tau in window
    assert tau(alpha) == alpha_tau and tau(alpha_tau) == alpha
    assert alpha != alpha_tau

    h = [QC(1)]
    for beta in sorted(window - frozenset(target)):
        h = mul_poly(h, [-t_coord(beta, c), QC(1)])

    t1 = t_coord(alpha, c)
    t2 = t_coord(alpha_tau, c)
    h1 = eval_poly(h, t1)
    h2 = eval_poly(h, t2)
    assert t1 != t2 and h1 != QC(0) and h2 != QC(0)

    v1 = QC(1) / ((t1 ** r) * h1)
    v2 = QC(-1) / ((t2 ** r) * h2)
    l1 = scale_poly([-t2, QC(1)], v1 / (t1 - t2))
    l2 = scale_poly([-t1, QC(1)], v2 / (t2 - t1))
    ell = add_poly(l1, l2)
    return shift_poly(mul_poly(h, ell), r), h


def j_form(spectrum: dict[QC, int], p: list[QC], c: Fraction) -> QC:
    out = QC(0)
    for beta, mult in spectrum.items():
        assert spectrum[tau(beta)] == mult
        out = out + mult * eval_poly(p, t_coord(tau(beta), c)) * eval_poly(
            p, t_coord(beta, c)
        ).conj()
    return out


def restricted_j_form(
    spectrum: dict[QC, int], p: list[QC], c: Fraction, carrier: frozenset[QC]
) -> QC:
    out = QC(0)
    for beta, mult in spectrum.items():
        if beta in carrier and tau(beta) in carrier:
            out = out + mult * eval_poly(p, t_coord(tau(beta), c)) * eval_poly(
                p, t_coord(beta, c)
            ).conj()
    return out


def tail_norm(
    spectrum: dict[QC, int], p: list[QC], c: Fraction, window: frozenset[QC]
) -> Fraction:
    return sum(
        Fraction(mult) * eval_poly(p, t_coord(beta, c)).norm2()
        for beta, mult in spectrum.items()
        if beta not in window
    )


def gram_entry(spectrum: dict[QC, int], c: Fraction, j: int, k: int) -> QC:
    out = QC(0)
    for beta, mult in spectrum.items():
        out = out + mult * (t_coord(tau(beta), c) ** j) * (
            t_coord(beta, c) ** k
        ).conj()
    return out


def coefficient_form(
    spectrum: dict[QC, int], p: list[QC], c: Fraction
) -> QC:
    out = QC(0)
    for j in range(1, len(p)):
        for k in range(1, len(p)):
            out = out + p[j] * gram_entry(spectrum, c, j, k) * p[k].conj()
    return out


def taylor_derivative(
    spectrum: dict[QC, int], c: Fraction, j: int, k: int
) -> QC:
    sign = -1 if (j + k - 2) % 2 else 1
    factor = Fraction(sign * factorial(j - 1) * factorial(k - 1))
    out = QC(0)
    for beta, mult in spectrum.items():
        out = out + mult * factor * ((QC(c) + beta).inv() ** j) * (
            (QC(c) - beta).inv() ** k
        )
    return out


def value_form(spectrum: dict[QC, int], values: dict[QC, QC]) -> QC:
    return sum(
        (
            mult
            * values.get(tau(beta), QC(0))
            * values.get(beta, QC(0)).conj()
        )
        for beta, mult in spectrum.items()
    )


def main() -> int:
    c = Fraction(7, 5)
    alpha = QC(Fraction(2, 5), Fraction(12, 5))
    alpha_tau = tau(alpha)
    alpha_bar = alpha.conj()
    alpha_tau_bar = alpha_tau.conj()
    high = QC(Fraction(0), Fraction(24, 5))
    high_bar = high.conj()

    spectrum = {
        alpha: 1,
        alpha_tau: 1,
        alpha_bar: 1,
        alpha_tau_bar: 1,
        high: 10**6,
        high_bar: 10**6,
    }
    window = frozenset({alpha, alpha_tau, alpha_bar, alpha_tau_bar})
    target = (alpha, alpha_tau)

    generated = {
        z
        for beta in spectrum
        for z in (beta, -beta, beta.conj(), tau(beta))
    }
    assert set(spectrum) == generated
    assert all(abs(beta.re) < Fraction(1, 2) for beta in spectrum)
    assert all(spectrum[tau(beta)] == mult for beta, mult in spectrum.items())
    print("BREAK B1 exact symmetry carrier PASS")

    t1 = t_coord(alpha, c)
    t2 = t_coord(alpha_tau, c)
    assert modulus(t1) == Fraction(5, 13)
    assert modulus(t2) == Fraction(1, 3)
    tau0 = Fraction(1, 3)
    assert modulus(t1 - t2) == Fraction(52, 507)
    outside_moduli = [
        modulus(t_coord(beta, c)) for beta in spectrum if beta not in window
    ]
    assert outside_moduli == [Fraction(1, 5), Fraction(1, 5)]
    q_w = Fraction(3, 5)
    assert max(outside_moduli) / tau0 == q_w < 1
    print("BREAK B2 exact Cauchy geometry PASS q_W=3/5")

    transition: int | None = None
    first_tail: Fraction | None = None
    transition_tail: Fraction | None = None
    transition_p: list[QC] | None = None
    transition_h: list[QC] | None = None

    for r in range(1, 81):
        p, h = interpolation_polynomial(window, target, c, r)
        assert eval_poly(p, t_coord(alpha, c)) == QC(1)
        assert eval_poly(p, t_coord(alpha_tau, c)) == QC(-1)
        assert all(
            eval_poly(p, t_coord(beta, c)) == QC(0)
            for beta in window - frozenset(target)
        )
        current_tail = tail_norm(spectrum, p, c, window)
        if r == 1:
            first_tail = current_tail
        if current_tail < 2 and transition is None:
            transition = r
            transition_tail = current_tail
            transition_p = p
            transition_h = h

    assert first_tail is not None and first_tail >= 2
    assert transition == 14
    assert transition_tail is not None and transition_tail < 2
    assert transition_p is not None and transition_h is not None
    print("BREAK B3 nonvacuous tail transition PASS r=14 N=17")

    p = transition_p
    full = j_form(spectrum, p, c)
    window_form = restricted_j_form(spectrum, p, c, window)
    complement = frozenset(set(spectrum) - set(window))
    outside_form = restricted_j_form(spectrum, p, c, complement)
    assert window_form == QC(-2)
    assert full == window_form + outside_form
    assert outside_form.im == 0
    assert abs(outside_form.re) <= transition_tail
    assert full.im == 0 and full.re < 0
    assert coefficient_form(spectrum, p, c) == full
    print("BREAK B4 invariant split and negative coefficient form PASS")

    for j in range(1, 5):
        for k in range(1, 5):
            factor = Fraction(
                (-1 if (j + k - 2) % 2 else 1)
                * factorial(j - 1)
                * factorial(k - 1)
            )
            assert taylor_derivative(spectrum, c, j, k) == factor * gram_entry(
                spectrum, c, j, k
            )
    print("BREAK B5 derivative sign and factorial route PASS")

    c2 = sum(
        Fraction(mult) * t_coord(beta, c).norm2()
        for beta, mult in spectrum.items()
    )
    m_c = sum(
        Fraction(mult) * (QC(c) - beta).inv().re
        for beta, mult in spectrum.items()
    )
    assert m_c > 0
    assert c2 <= m_c / (c - Fraction(1, 2))
    print("BREAK B6 ordinary Cauchy norm comparison PASS")

    h1 = eval_poly(transition_h, t1)
    h2 = eval_poly(transition_h, t2)
    h_lower = min(modulus_lower(h1), modulus_lower(h2))
    assert h_lower > 0
    b_upper = (
        2 * q_w * tau0 + modulus(t1) + modulus(t2)
    ) / (modulus(t1 - t2) * h_lower)
    c_upper = Fraction(1)
    for beta in window - frozenset(target):
        c_upper *= q_w * tau0 + modulus(t_coord(beta, c))
    a_upper = (
        b_upper
        * b_upper
        * c_upper
        * c_upper
        * m_c
        / ((c - Fraction(1, 2)) * tau0 * tau0)
    )
    for r in range(1, 31):
        p_r, _h = interpolation_polynomial(window, target, c, r)
        assert tail_norm(spectrum, p_r, c, window) <= a_upper * q_w ** (
            2 * (r - 1)
        )
    bound_threshold = next(
        r for r in range(1, 501) if a_upper * q_w ** (2 * (r - 1)) < 2
    )
    assert bound_threshold == 19
    print("BREAK B7 uniform majorant PASS r_bound=19")

    both = value_form(spectrum, {alpha: QC(1), alpha_tau: QC(1)})
    left = value_form(spectrum, {alpha: QC(1)})
    right = value_form(spectrum, {alpha_tau: QC(1)})
    assert both - left - right != QC(0)
    print("BREAK B8 noninvariant support cross term PASS")

    assert tau(high) == high
    assert tau(alpha) != alpha
    print("BREAK B9 tau-fixed and nontrivial-orbit controls PASS")

    small_window = frozenset(target)
    q2_small = max(
        t_coord(beta, c).norm2() / (tau0 * tau0)
        for beta in spectrum
        if beta not in small_window
    )
    assert q2_small > 1
    print("BREAK B10 q_W>=1 rejection control PASS")

    print("BREAKER FINDINGS 0/10")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
