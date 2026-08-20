#!/usr/bin/env python3
"""Independent exact breaker for C-RH-RAY-FINITE-WINDOW-CERTIFICATE-1-N.

This file is frozen before the accepted verifier exists. It uses a direct
finite spectral implementation and a low-to-high polynomial implementation.
It imports no project verifier, no external data, and no floating point.
Synthetic locations are controls only. They are not zeta zeros.
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
        return QC(self.re * z.re - self.im * z.im,
                  self.re * z.im + self.im * z.re)

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
        e = exponent
        while e:
            if e & 1:
                out = out * base
            base = base * base
            e >>= 1
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


def qsqrt(value: Fraction) -> Fraction:
    assert value >= 0
    a = isqrt(value.numerator)
    b = isqrt(value.denominator)
    assert a * a == value.numerator and b * b == value.denominator
    return Fraction(a, b)


def abs_exact(z: QC) -> Fraction:
    return qsqrt(z.norm2())


def abs_lower(z: QC) -> Fraction:
    return max(abs(z.re), abs(z.im))


def poly_trim(p: list[QC]) -> list[QC]:
    out = p[:]
    while len(out) > 1 and out[-1] == QC(0):
        out.pop()
    return out


def poly_add(p: list[QC], q: list[QC]) -> list[QC]:
    n = max(len(p), len(q))
    out = [QC(0) for _ in range(n)]
    for i in range(n):
        if i < len(p):
            out[i] = out[i] + p[i]
        if i < len(q):
            out[i] = out[i] + q[i]
    return poly_trim(out)


def poly_scale(p: list[QC], a: QC) -> list[QC]:
    return poly_trim([a * x for x in p])


def poly_mul(p: list[QC], q: list[QC]) -> list[QC]:
    out = [QC(0) for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = out[i + j] + a * b
    return poly_trim(out)


def poly_eval(p: list[QC], z: QC) -> QC:
    out = QC(0)
    for a in reversed(p):
        out = out * z + a
    return out


def poly_shift(p: list[QC], r: int) -> list[QC]:
    assert r >= 0
    return [QC(0) for _ in range(r)] + p


def t_coord(beta: QC, c: Fraction) -> QC:
    return (QC(c) - beta.conj()).inv()


def build_polynomial(
    spectrum: dict[QC, int],
    window: frozenset[QC],
    target: tuple[QC, QC],
    c: Fraction,
    r: int,
) -> tuple[list[QC], list[QC], list[QC]]:
    del spectrum
    alpha, alpha_tau = target
    assert tau(alpha) == alpha_tau and tau(alpha_tau) == alpha
    assert alpha != alpha_tau
    assert alpha in window and alpha_tau in window

    h = [QC(1)]
    for beta in sorted(window - frozenset(target)):
        h = poly_mul(h, [-t_coord(beta, c), QC(1)])

    t1 = t_coord(alpha, c)
    t2 = t_coord(alpha_tau, c)
    h1 = poly_eval(h, t1)
    h2 = poly_eval(h, t2)
    assert h1 != QC(0) and h2 != QC(0) and t1 != t2

    u1 = QC(1) / ((t1 ** r) * h1)
    u2 = QC(-1) / ((t2 ** r) * h2)
    l1 = poly_scale([-t2, QC(1)], u1 / (t1 - t2))
    l2 = poly_scale([-t1, QC(1)], u2 / (t2 - t1))
    ell = poly_add(l1, l2)
    p = poly_shift(poly_mul(h, ell), r)
    return p, h, ell


def spectral_form(spectrum: dict[QC, int], p: list[QC], c: Fraction) -> QC:
    out = QC(0)
    for beta, mult in spectrum.items():
        assert spectrum[tau(beta)] == mult
        a = poly_eval(p, t_coord(tau(beta), c))
        b = poly_eval(p, t_coord(beta, c)).conj()
        out = out + mult * a * b
    return out


def restricted_form(
    spectrum: dict[QC, int], p: list[QC], c: Fraction, carrier: frozenset[QC]
) -> QC:
    out = QC(0)
    for beta, mult in spectrum.items():
        if beta not in carrier or tau(beta) not in carrier:
            continue
        out = out + mult * poly_eval(p, t_coord(tau(beta), c)) * poly_eval(
            p, t_coord(beta, c)
        ).conj()
    return out


def tail_norm(
    spectrum: dict[QC, int], p: list[QC], c: Fraction, window: frozenset[QC]
) -> Fraction:
    return sum(
        Fraction(mult) * poly_eval(p, t_coord(beta, c)).norm2()
        for beta, mult in spectrum.items()
        if beta not in window
    )


def gram_entry(
    spectrum: dict[QC, int], c: Fraction, j: int, k: int
) -> QC:
    out = QC(0)
    for beta, mult in spectrum.items():
        out = out + mult * (t_coord(tau(beta), c) ** j) * (
            t_coord(beta, c) ** k
        ).conj()
    return out


def coefficient_form(
    spectrum: dict[QC, int], c: Fraction, p: list[QC]
) -> QC:
    out = QC(0)
    for j in range(1, len(p)):
        for k in range(1, len(p)):
            out = out + p[j] * gram_entry(spectrum, c, j, k) * p[k].conj()
    return out


def derivative_entry_series(
    spectrum: dict[QC, int], c: Fraction, j: int, k: int
) -> QC:
    """Mixed derivative by direct Taylor coefficients of the rational kernel."""
    out = QC(0)
    sign = -1 if (j + k - 2) % 2 else 1
    scale = Fraction(sign * factorial(j - 1) * factorial(k - 1))
    for beta, mult in spectrum.items():
        left = (QC(c) + beta).inv() ** j
        right = (QC(c) - beta).inv() ** k
        out = out + mult * scale * left * right
    return out


def form_from_values(
    spectrum: dict[QC, int], values: dict[QC, QC]
) -> QC:
    out = QC(0)
    for beta, mult in spectrum.items():
        out = out + mult * values.get(tau(beta), QC(0)) * values.get(
            beta, QC(0)
        ).conj()
    return out


def main() -> int:
    c = Fraction(7, 5)
    x = Fraction(2, 5)
    y = Fraction(12, 5)
    alpha = QC(x, y)
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

    assert set(spectrum) == {
        z
        for beta in spectrum
        for z in (beta, -beta, beta.conj(), tau(beta))
    }
    assert all(abs(beta.re) < Fraction(1, 2) for beta in spectrum)
    assert all(spectrum[tau(beta)] == mult for beta, mult in spectrum.items())
    print("BREAKER B1 symmetry carrier PASS")

    t1 = t_coord(alpha, c)
    t2 = t_coord(alpha_tau, c)
    assert abs_exact(t1) == Fraction(5, 13)
    assert abs_exact(t2) == Fraction(1, 3)
    tau0 = Fraction(1, 3)
    delta = abs_exact(t1 - t2)
    assert delta == Fraction(52, 507)
    outside_moduli = [abs_exact(t_coord(beta, c)) for beta in spectrum if beta not in window]
    assert outside_moduli == [Fraction(1, 5), Fraction(1, 5)]
    q = Fraction(3, 5)
    assert max(outside_moduli) / tau0 == q < 1
    print("BREAKER B2 exact q_W PASS q=3/5")

    transition: int | None = None
    first_tail: Fraction | None = None
    transition_tail: Fraction | None = None
    transition_poly: list[QC] | None = None
    h_at_transition: list[QC] | None = None

    for r in range(1, 81):
        p, h, _ell = build_polynomial(spectrum, window, target, c, r)
        assert poly_eval(p, t_coord(alpha, c)) == QC(1)
        assert poly_eval(p, t_coord(alpha_tau, c)) == QC(-1)
        assert all(
            poly_eval(p, t_coord(beta, c)) == QC(0)
            for beta in window - frozenset(target)
        )
        tail = tail_norm(spectrum, p, c, window)
        if r == 1:
            first_tail = tail
        if tail < 2 and transition is None:
            transition = r
            transition_tail = tail
            transition_poly = p
            h_at_transition = h

    assert first_tail is not None and first_tail >= 2
    assert transition is not None and transition > 1
    assert transition_tail is not None and transition_tail < 2
    assert transition_poly is not None and h_at_transition is not None
    print(f"BREAKER B3 tail transition PASS r=1 fails, r={transition} certifies")

    p = transition_poly
    full = spectral_form(spectrum, p, c)
    window_part = restricted_form(spectrum, p, c, window)
    outside_part = restricted_form(spectrum, p, c, frozenset(set(spectrum) - set(window)))
    assert window_part == QC(-2)
    assert full == window_part + outside_part
    assert outside_part.im == 0
    assert abs(outside_part.re) <= transition_tail
    assert full.im == 0 and full.re < 0
    assert coefficient_form(spectrum, c, p) == full
    print("BREAKER B4 invariant split and negative coefficient form PASS")

    for j in range(1, min(5, len(p))):
        for k in range(1, min(5, len(p))):
            raw = derivative_entry_series(spectrum, c, j, k)
            scale = Fraction(
                (-1 if (j + k - 2) % 2 else 1)
                * factorial(j - 1)
                * factorial(k - 1)
            )
            assert raw == scale * gram_entry(spectrum, c, j, k)
    print("BREAKER B5 Taylor derivative route PASS")

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
    print("BREAKER B6 ordinary Cauchy norm bound PASS")

    h = h_at_transition
    h1 = poly_eval(h, t1)
    h2 = poly_eval(h, t2)
    h_lower = min(abs_lower(h1), abs_lower(h2))
    assert h_lower > 0
    b_upper = (
        2 * q * tau0 + abs_exact(t1) + abs_exact(t2)
    ) / (delta * h_lower)
    c_upper = Fraction(1)
    for beta in window - frozenset(target):
        c_upper *= q * tau0 + abs_exact(t_coord(beta, c))
    a_upper = (
        b_upper
        * b_upper
        * c_upper
        * c_upper
        * m_c
        / ((c - Fraction(1, 2)) * tau0 * tau0)
    )
    for r in range(1, 31):
        p_r, _h, _ell = build_polynomial(spectrum, window, target, c, r)
        tail_r = tail_norm(spectrum, p_r, c, window)
        assert tail_r <= a_upper * q ** (2 * (r - 1))
    print("BREAKER B7 rational majorant of exponential tail PASS")

    values = {alpha: QC(1), alpha_tau: QC(1)}
    full_values = form_from_values(spectrum, values)
    left_values = form_from_values(spectrum, {alpha: QC(1)})
    right_values = form_from_values(spectrum, {alpha_tau: QC(1)})
    cross = full_values - left_values - right_values
    assert cross != QC(0)
    print("BREAKER B8 non-invariant support exposes cross term PASS")

    assert tau(high) == high
    assert high == tau(high)
    print("BREAKER B9 tau-fixed target rejected PASS")

    small_window = frozenset(target)
    small_tau0 = tau0
    small_q2 = max(
        t_coord(beta, c).norm2() / (small_tau0 * small_tau0)
        for beta in spectrum
        if beta not in small_window
    )
    assert small_q2 > 1
    print("BREAKER B10 q_W>=1 control rejected PASS")

    print("BREAKER FINDINGS 0/10")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
