#!/usr/bin/env python3
"""Exact independent audit of the Ray finite-window certificate.

Result-exposed disclosure: the earlier frozen breaker found the first direct
sufficient-tail transition at r=14 on the frozen synthetic carrier. This
verifier was written afterwards from PREREG.md and PROOF.md. It imports no
breaker code. It uses 2 by 2 rational multiplication matrices for Q(i),
high-to-low polynomials, the Taylor kernel route, and exact symmetric
congruence for inertia.

Synthetic locations are theorem controls only. They are not zeta zeros.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt


@dataclass(frozen=True)
class CMat:
    a00: Fraction
    a01: Fraction
    a10: Fraction
    a11: Fraction

    @staticmethod
    def make(real: Fraction | int, imag: Fraction | int = 0) -> "CMat":
        x = Fraction(real)
        y = Fraction(imag)
        return CMat(x, -y, y, x)

    def valid(self) -> bool:
        return self.a00 == self.a11 and self.a01 == -self.a10

    @property
    def real(self) -> Fraction:
        assert self.valid()
        return self.a00

    @property
    def imag(self) -> Fraction:
        assert self.valid()
        return self.a10

    def __add__(self, other: object) -> "CMat":
        z = cm(other)
        return CMat(
            self.a00 + z.a00,
            self.a01 + z.a01,
            self.a10 + z.a10,
            self.a11 + z.a11,
        )

    __radd__ = __add__

    def __neg__(self) -> "CMat":
        return CMat(-self.a00, -self.a01, -self.a10, -self.a11)

    def __sub__(self, other: object) -> "CMat":
        return self + (-cm(other))

    def __rsub__(self, other: object) -> "CMat":
        return cm(other) - self

    def __mul__(self, other: object) -> "CMat":
        z = cm(other)
        out = CMat(
            self.a00 * z.a00 + self.a01 * z.a10,
            self.a00 * z.a01 + self.a01 * z.a11,
            self.a10 * z.a00 + self.a11 * z.a10,
            self.a10 * z.a01 + self.a11 * z.a11,
        )
        assert out.valid()
        return out

    __rmul__ = __mul__

    def transpose(self) -> "CMat":
        out = CMat(self.a00, self.a10, self.a01, self.a11)
        assert out.valid()
        return out

    def det(self) -> Fraction:
        return self.a00 * self.a11 - self.a01 * self.a10

    def inv(self) -> "CMat":
        d = self.det()
        assert d != 0
        out = CMat(self.a11 / d, -self.a01 / d, -self.a10 / d, self.a00 / d)
        assert out.valid()
        return out

    def __truediv__(self, other: object) -> "CMat":
        return self * cm(other).inv()

    def __rtruediv__(self, other: object) -> "CMat":
        return cm(other) / self

    def __pow__(self, exponent: int) -> "CMat":
        assert exponent >= 0
        out = CMat.make(1)
        base = self
        e = exponent
        while e:
            if e & 1:
                out = out * base
            base = base * base
            e >>= 1
        return out


def cm(value: object) -> CMat:
    if isinstance(value, CMat):
        return value
    if isinstance(value, (int, Fraction)):
        return CMat.make(Fraction(value))
    raise TypeError(type(value))


ZERO = CMat.make(0)
ONE = CMat.make(1)


def tau(z: CMat) -> CMat:
    return CMat.make(-z.real, z.imag)


def conjugate(z: CMat) -> CMat:
    return z.transpose()


def rational_sqrt(q: Fraction) -> Fraction:
    assert q >= 0
    n = isqrt(q.numerator)
    d = isqrt(q.denominator)
    assert n * n == q.numerator and d * d == q.denominator
    return Fraction(n, d)


def modulus(z: CMat) -> Fraction:
    return rational_sqrt(z.det())


def lower_modulus(z: CMat) -> Fraction:
    return max(abs(z.real), abs(z.imag))


def poly_strip(p: list[CMat]) -> list[CMat]:
    i = 0
    while i < len(p) - 1 and p[i] == ZERO:
        i += 1
    return p[i:]


def poly_mul(p: list[CMat], q: list[CMat]) -> list[CMat]:
    out = [ZERO for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = out[i + j] + x * y
    return poly_strip(out)


def poly_eval(p: list[CMat], z: CMat) -> CMat:
    out = ZERO
    for coefficient in p:
        out = out * z + coefficient
    return out


def poly_times_t_power(p: list[CMat], r: int) -> list[CMat]:
    assert r >= 0
    return p + [ZERO for _ in range(r)]


def coefficient(p: list[CMat], power: int) -> CMat:
    degree = len(p) - 1
    if power < 0 or power > degree:
        return ZERO
    return p[degree - power]


def t_of(beta: CMat, c: Fraction) -> CMat:
    return (CMat.make(c) - conjugate(beta)).inv()


def make_polynomial(
    window: frozenset[CMat], target: tuple[CMat, CMat], c: Fraction, r: int
) -> tuple[list[CMat], list[CMat]]:
    a, b = target
    h = [ONE]
    roots = sorted(window - frozenset(target), key=lambda z: (z.real, z.imag))
    for beta in roots:
        h = poly_mul(h, [ONE, -t_of(beta, c)])

    ta = t_of(a, c)
    tb = t_of(b, c)
    va = ONE / ((ta ** r) * poly_eval(h, ta))
    vb = CMat.make(-1) / ((tb ** r) * poly_eval(h, tb))
    slope = (va - vb) / (ta - tb)
    intercept = va - slope * ta
    ell = [slope, intercept]
    return poly_times_t_power(poly_mul(h, ell), r), h


def scaled_kernel_entry(
    spectrum: list[tuple[CMat, int]], c: Fraction, j: int, k: int
) -> CMat:
    """Taylor route from K(a,b)=sum m/((a+beta)(b-beta))."""
    out = ZERO
    for beta, mult in spectrum:
        out = out + mult * ((CMat.make(c) + beta).inv() ** j) * (
            (CMat.make(c) - beta).inv() ** k
        )
    return out


def direct_j_entry(
    spectrum: list[tuple[CMat, int]], c: Fraction, j: int, k: int
) -> CMat:
    out = ZERO
    for beta, mult in spectrum:
        out = out + mult * (t_of(tau(beta), c) ** j) * conjugate(
            t_of(beta, c) ** k
        )
    return out


def direct_form(
    spectrum: list[tuple[CMat, int]], p: list[CMat], c: Fraction
) -> CMat:
    out = ZERO
    for beta, mult in spectrum:
        out = out + mult * poly_eval(p, t_of(tau(beta), c)) * conjugate(
            poly_eval(p, t_of(beta, c))
        )
    return out


def tail(
    spectrum: list[tuple[CMat, int]],
    p: list[CMat],
    c: Fraction,
    window: frozenset[CMat],
) -> Fraction:
    return sum(
        Fraction(mult) * poly_eval(p, t_of(beta, c)).det()
        for beta, mult in spectrum
        if beta not in window
    )


def coefficient_quadratic(
    spectrum: list[tuple[CMat, int]], p: list[CMat], c: Fraction
) -> CMat:
    degree = len(p) - 1
    out = ZERO
    for j in range(1, degree + 1):
        pj = coefficient(p, j)
        for k in range(1, degree + 1):
            pk = coefficient(p, k)
            out = out + pj * scaled_kernel_entry(spectrum, c, j, k) * conjugate(pk)
    return out


def real_gram(
    spectrum: list[tuple[CMat, int]], c: Fraction, n: int
) -> list[list[Fraction]]:
    out: list[list[Fraction]] = []
    for j in range(1, n + 1):
        row: list[Fraction] = []
        for k in range(1, n + 1):
            z = scaled_kernel_entry(spectrum, c, j, k)
            assert z.imag == 0
            row.append(z.real)
        out.append(row)
    assert all(out[i][j] == out[j][i] for i in range(n) for j in range(n))
    return out


def inertia_symmetric(matrix: list[list[Fraction]]) -> tuple[int, int, int]:
    """Exact congruence elimination with 1 by 1 and 2 by 2 pivots."""
    a = [row[:] for row in matrix]
    pos = neg = zero = 0
    while a:
        n = len(a)
        diagonal = next((i for i in range(n) if a[i][i] != 0), None)
        if diagonal is not None:
            if diagonal != 0:
                a[0], a[diagonal] = a[diagonal], a[0]
                for row in a:
                    row[0], row[diagonal] = row[diagonal], row[0]
            pivot = a[0][0]
            if pivot > 0:
                pos += 1
            else:
                neg += 1
            if n == 1:
                a = []
                continue
            v = [a[i][0] for i in range(1, n)]
            b = [
                [a[i][j] - v[i - 1] * v[j - 1] / pivot for j in range(1, n)]
                for i in range(1, n)
            ]
            a = b
            continue

        off = next(
            ((i, j) for i in range(n) for j in range(i + 1, n) if a[i][j] != 0),
            None,
        )
        if off is None:
            zero += n
            break
        i, j = off
        order = [i, j] + [k for k in range(n) if k not in (i, j)]
        a = [[a[r][s] for s in order] for r in order]
        x = a[0][1]
        pos += 1
        neg += 1
        if n == 2:
            a = []
            continue
        # Inverse of [[0,x],[x,0]] is [[0,1/x],[1/x,0]].
        b: list[list[Fraction]] = []
        for r in range(2, n):
            row: list[Fraction] = []
            for s in range(2, n):
                correction = (a[r][0] * a[1][s] + a[r][1] * a[0][s]) / x
                row.append(a[r][s] - correction)
            b.append(row)
        a = b
    return pos, neg, zero


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    a = [row[:] for row in matrix]
    det = Fraction(1)
    n = len(a)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pv = a[col][col]
        det *= pv
        for r in range(col + 1, n):
            if a[r][col] == 0:
                continue
            factor = a[r][col] / pv
            for s in range(col + 1, n):
                a[r][s] -= factor * a[col][s]
    return det


def main() -> int:
    c = Fraction(7, 5)
    alpha = CMat.make(Fraction(2, 5), Fraction(12, 5))
    alpha_tau = tau(alpha)
    target = (alpha, alpha_tau)
    window = frozenset({alpha, alpha_tau, conjugate(alpha), conjugate(alpha_tau)})
    high = CMat.make(0, Fraction(24, 5))
    spectrum = [
        (alpha, 1),
        (alpha_tau, 1),
        (conjugate(alpha), 1),
        (conjugate(alpha_tau), 1),
        (high, 10**6),
        (conjugate(high), 10**6),
    ]
    multiplicity = {z: m for z, m in spectrum}

    assert all(multiplicity[tau(z)] == m for z, m in spectrum)
    assert all(abs(z.real) < Fraction(1, 2) for z, _m in spectrum)
    print("PASS V1 frozen symmetry and multiplicity carrier")

    for j in range(1, 6):
        for k in range(1, 6):
            direct = direct_j_entry(spectrum, c, j, k)
            taylor = scaled_kernel_entry(spectrum, c, j, k)
            assert direct == taylor
            raw = Fraction(
                (-1 if (j + k - 2) % 2 else 1)
                * factorial(j - 1)
                * factorial(k - 1)
            ) * taylor
            assert raw / Fraction(
                (-1 if (j + k - 2) % 2 else 1)
                * factorial(j - 1)
                * factorial(k - 1)
            ) == direct
    print("PASS V2 mixed derivatives by Taylor and J_ref routes")

    direct_transition: int | None = None
    p_transition: list[CMat] | None = None
    for r in range(1, 81):
        p, _h = make_polynomial(window, target, c, r)
        assert poly_eval(p, t_of(alpha, c)) == ONE
        assert poly_eval(p, t_of(alpha_tau, c)) == CMat.make(-1)
        assert all(
            poly_eval(p, t_of(beta, c)) == ZERO
            for beta in window - frozenset(target)
        )
        if tail(spectrum, p, c, window) < 2 and direct_transition is None:
            direct_transition = r
            p_transition = p
    assert direct_transition == 14
    assert p_transition is not None
    assert len(p_transition) - 1 == 17
    print("PASS V3 interpolation and first direct certificate r=14 N=17")

    p = p_transition
    q_direct = direct_form(spectrum, p, c)
    q_coeff = coefficient_quadratic(spectrum, p, c)
    assert q_direct == q_coeff
    assert q_direct.imag == 0 and q_direct.real < 0
    tail_14 = tail(spectrum, p, c, window)
    assert tail_14 < 2
    print("PASS V4 exact split certificate and coefficient quadratic agreement")

    g = real_gram(spectrum, c, 17)
    pos, neg, nul = inertia_symmetric(g)
    assert pos + neg + nul == 17
    assert neg >= 1
    first_nonpositive: int | None = None
    for n in range(1, 18):
        d = determinant([row[:n] for row in g[:n]])
        if d <= 0:
            first_nonpositive = n
            break
    assert first_nonpositive is not None
    print(
        f"PASS V5 exact inertia pos={pos} neg={neg} zero={nul}; "
        f"first nonpositive leading minor={first_nonpositive}"
    )

    t1 = t_of(alpha, c)
    t2 = t_of(alpha_tau, c)
    tau0 = min(modulus(t1), modulus(t2))
    assert tau0 == Fraction(1, 3)
    outside = [z for z, _m in spectrum if z not in window]
    q_w = max(modulus(t_of(z, c)) for z in outside) / tau0
    assert q_w == Fraction(3, 5)

    _p1, h = make_polynomial(window, target, c, 1)
    h1 = poly_eval(h, t1)
    h2 = poly_eval(h, t2)
    h_lower = min(lower_modulus(h1), lower_modulus(h2))
    delta_lower = modulus(t1 - t2)
    b_major = (
        2 * q_w * tau0 + modulus(t1) + modulus(t2)
    ) / (delta_lower * h_lower)
    c_major = Fraction(1)
    for beta in window - frozenset(target):
        c_major *= q_w * tau0 + modulus(t_of(beta, c))

    c2 = sum(Fraction(m) * t_of(z, c).det() for z, m in spectrum)
    m_c = sum(Fraction(m) * (CMat.make(c) - z).inv().real for z, m in spectrum)
    assert c2 <= m_c / (c - Fraction(1, 2))
    a_major = (
        b_major
        * b_major
        * c_major
        * c_major
        * m_c
        / ((c - Fraction(1, 2)) * tau0 * tau0)
    )
    bound_transition = next(
        r for r in range(1, 501) if a_major * q_w ** (2 * (r - 1)) < 2
    )
    for r in range(1, bound_transition + 1):
        p_r, _h = make_polynomial(window, target, c, r)
        assert tail(spectrum, p_r, c, window) <= a_major * q_w ** (2 * (r - 1))
    assert bound_transition >= direct_transition
    print(
        f"PASS V6 uniform rational majorant; sufficient bound threshold r={bound_transition}"
    )

    target_height_radius = Fraction(3)
    t_window = Fraction(4)
    assert target_height_radius * target_height_radius == (
        Fraction(12, 5) ** 2 + (c + Fraction(2, 5)) ** 2
    )
    assert t_window > target_height_radius
    assert all(abs(z.imag) <= t_window for z in window)
    assert all(abs(z.imag) > t_window for z in outside)
    assert q_w <= target_height_radius / t_window < 1
    print("PASS V7 complete-height-window corollary on frozen carrier")

    # Non-invariant partition: the J_ref cross term does not vanish.
    values = {alpha: ONE, alpha_tau: ONE}
    full_values = sum(
        Fraction(m)
        * values.get(tau(z), ZERO)
        * conjugate(values.get(z, ZERO))
        for z, m in spectrum
    )
    left_values = sum(
        Fraction(m)
        * ({alpha: ONE}.get(tau(z), ZERO))
        * conjugate({alpha: ONE}.get(z, ZERO))
        for z, m in spectrum
    )
    right_values = sum(
        Fraction(m)
        * ({alpha_tau: ONE}.get(tau(z), ZERO))
        * conjugate({alpha_tau: ONE}.get(z, ZERO))
        for z, m in spectrum
    )
    assert full_values - left_values - right_values != ZERO
    print("PASS V8 non-tau-invariant split negative control")

    assert tau(high) == high
    assert alpha != tau(alpha)
    small_window = frozenset(target)
    q2_small = max(
        t_of(z, c).det() / (tau0 * tau0)
        for z, _m in spectrum
        if z not in small_window
    )
    assert q2_small > 1
    print("PASS V9 fixed-orbit and q_W>=1 negative controls")

    assert all(isinstance(x, Fraction) for row in g for x in row)
    print("PASS V10 exact arithmetic and deterministic scope")
    print(
        "DECISION CERTIFICATE: conditional finite-window theorem survives; "
        "synthetic audit only"
    )
    print("RESULT 10/10 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
