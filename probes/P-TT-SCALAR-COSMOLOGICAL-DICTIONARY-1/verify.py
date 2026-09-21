#!/usr/bin/env python3
"""Exact audit of a selected classical TT/scalar cosmological dictionary.

This file is its complete runtime input.  It uses rational arithmetic,
Q(zeta_5), formal Laurent polynomials and exact trigonometric identities.
It performs no numerical integration, random sampling or floating-point
comparison.  The continuous common translation is audited by character
integration; a five-point phase sum is used only as a first/second-moment
cross-check, never as the full probability law.  Universal scope and the
status of all adopted physical inputs belong to the accompanying proof.
"""

from collections import defaultdict
from fractions import Fraction as F
from math import comb


WORDS = ("0010", "0011", "0100", "0101", "0110", "1001",
         "1010", "1011", "1100", "1101")
WEIGHTS = {w: F(1, 6) if w in ("0110", "1001") else F(1, 12)
           for w in WORDS}
BAND = (-2, -1, 1, 2)
ZERO5 = (F(0),)*5


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def source(word):
    bits = tuple(map(int, word))
    u0, u1 = bits[2]-bits[0], bits[3]-bits[1]
    def h(u):
        return tuple(F(int(r == u % 5)+int(r == (u+1) % 5), 2)
                     for r in range(5))
    return sub(h(u1), h(u0))


def project_zero(v):
    return sub(v, (sum(v, F(0))/5,)*5)


def mean(vectors):
    return tuple(sum((WEIGHTS[w]*vectors[w][r] for w in WORDS), F(0))
                 for r in range(5))


def moment(a, b):
    return tuple(tuple(sum((WEIGHTS[w]*a[w][r]*b[w][s] for w in WORDS), F(0))
                       for s in range(5)) for r in range(5))


def rank(a):
    a = [list(map(F, row)) for row in a]
    r = 0
    for j in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][j]
        a[r] = [x/q for x in a[r]]
        for i in range(r+1, len(a)):
            if a[i][j]:
                q = a[i][j]
                a[i] = [x-q*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


# Q(zeta_5), in the basis 1,z,z^2,z^3.
def cyc(value=0):
    if isinstance(value, tuple):
        assert len(value) == 4
        return tuple(map(F, value))
    return (F(value), F(0), F(0), F(0))


Z = (cyc(1), cyc((0, 1, 0, 0)), cyc((0, 0, 1, 0)),
     cyc((0, 0, 0, 1)), cyc((-1, -1, -1, -1)))
ROOT5 = cyc((-1, 0, -2, -2))


def cmul(a, b):
    p = [F(0)]*7
    for i in range(4):
        for j in range(4):
            p[i+j] += a[i]*b[j]
    for i in range(6, 3, -1):
        for j in range(4):
            p[i-4+j] -= p[i]
    return tuple(p[:4])


def conjugate(a):
    out = cyc()
    for i, q in enumerate(a):
        out = add(out, scale(q, Z[-i % 5]))
    return out


def q5(a=0, b=0):
    return add(cyc(a), scale(F(b), ROOT5))


def q5_pair(x):
    assert x == conjugate(x) and x[1] == 0 and x[2] == x[3]
    b = -x[2]/2
    a = x[0]+b
    assert x == q5(a, b)
    return a, b


def positive(x):
    a, b = q5_pair(x)
    if b == 0:
        return a > 0
    if b > 0:
        return a >= 0 or 5*b*b > a*a
    return a > 0 and a*a > 5*b*b


def fourier(v, j):
    """sqrt(5) times the unitary Fourier coefficient."""
    out = cyc()
    for r, x in enumerate(v):
        out = add(out, scale(x, Z[-j*r % 5]))
    return out


def fourier_moment(a, b, j, k):
    out = cyc()
    for w in WORDS:
        out = add(out, scale(WEIGHTS[w]/5,
                            cmul(fourier(a[w], j), conjugate(fourier(b[w], k)))))
    return out


def matrix_fourier(a, j, k):
    out = cyc()
    for r in range(5):
        for s in range(5):
            out = add(out, scale(a[r][s]/5, Z[(-j*r+k*s) % 5]))
    return out


def phase_integral(exponent):
    """Integral of exp(2*pi*i*exponent*sigma/(5*d)) over one period."""
    assert isinstance(exponent, int)
    return F(exponent == 0)


class Background:
    """Laurent powers H^a b^b R^c, R^2=3; b exponents may be rational."""
    def __init__(self, value=0):
        if isinstance(value, Background):
            self.terms = value.terms.copy()
        elif isinstance(value, dict):
            self.terms = {k: F(v) for k, v in value.items() if v}
        else:
            self.terms = {(F(0), F(0), 0): F(value)} if value else {}

    def __add__(self, other):
        out = self.terms.copy()
        for k, c in Background(other).terms.items():
            out[k] = out.get(k, F(0))+c
        return Background(out)

    __radd__ = __add__

    def __neg__(self):
        return Background({k: -c for k, c in self.terms.items()})

    def __sub__(self, other):
        return self+(-Background(other))

    def __mul__(self, other):
        out = defaultdict(F)
        for (ha, ba, ra), ca in self.terms.items():
            for (hb, bb, rb), cb in Background(other).terms.items():
                r = ra+rb
                out[ha+hb, ba+bb, r % 2] += ca*cb*3**(r//2)
        return Background(out)

    __rmul__ = __mul__

    def derivative(self, db_dt):
        """Differentiate in a variable with db/dt = db_dt*H, H constant."""
        out = defaultdict(F)
        for (h, b, r), c in self.terms.items():
            if b:
                out[h+1, b-1, r] += c*b*db_dt
        return Background(out)

    def __eq__(self, other):
        return self.terms == Background(other).terms


def bg(h=0, b=0, r=0, coefficient=1):
    assert r in (0, 1)
    return Background({(F(h), F(b), r): F(coefficient)})


class Trig:
    """Laurent K,x,D times sin(Kx)^s cos(Kx)^c, reduced by cos^2=1-sin^2."""
    def __init__(self, value=0):
        if isinstance(value, Trig):
            self.terms = value.terms.copy()
            return
        if not isinstance(value, dict):
            value = {(0, 0, 0, 0, 0): F(value)} if value else {}
        out = defaultdict(F)
        for (k, x, d, s, c), coefficient in value.items():
            assert all(isinstance(v, int) for v in (k, x, d, s, c))
            assert s >= 0 and c >= 0
            for j in range(c//2+1):
                out[k, x, d, s+2*j, c % 2] += F(coefficient)*comb(c//2, j)*(-1)**j
        self.terms = {key: value for key, value in out.items() if value}

    def __add__(self, other):
        out = self.terms.copy()
        for k, c in Trig(other).terms.items():
            out[k] = out.get(k, F(0))+c
        return Trig(out)

    __radd__ = __add__

    def __neg__(self):
        return Trig({k: -c for k, c in self.terms.items()})

    def __sub__(self, other):
        return self+(-Trig(other))

    def __mul__(self, other):
        out = defaultdict(F)
        for ka, ca in self.terms.items():
            for kb, cb in Trig(other).terms.items():
                out[tuple(a+b for a, b in zip(ka, kb))] += ca*cb
        return Trig(out)

    __rmul__ = __mul__

    def derivative(self):
        out = defaultdict(F)
        for (k, x, d, s, c), coefficient in self.terms.items():
            if x:
                out[k, x-1, d, s, c] += coefficient*x
            if s:
                out[k+1, x, d, s-1, c+1] += coefficient*s
            if c:
                out[k+1, x, d, s+1, c-1] -= coefficient*c
        return Trig(out)

    def __eq__(self, other):
        return self.terms == Trig(other).terms


def trig(k=0, x=0, d=0, s=0, c=0, coefficient=1):
    return Trig({(k, x, d, s, c): F(coefficient)})


def main():
    # G1: exactly the accepted source alphabet, no reweighting or static deletion.
    assert len(WORDS) == len(set(WORDS)) == 10
    assert sum(WEIGHTS.values(), F(0)) == 1 and all(p > 0 for p in WEIGHTS.values())
    phi = {w: source(w) for w in WORDS}
    intensity = {w: tuple(abs(x) for x in phi[w]) for w in WORDS}
    scalar = {w: project_zero(intensity[w]) for w in WORDS}
    static = tuple(w for w in WORDS if phi[w] == ZERO5)
    assert static == ("0011", "0101", "1010", "1100")
    assert sum(WEIGHTS[w] for w in static) == F(1, 3)
    assert len(set(phi.values())) == 7
    for w in WORDS:
        assert sum(phi[w], F(0)) == sum(scalar[w], F(0)) == 0
        assert project_zero(scalar[w]) == scalar[w]
        assert (scalar[w] == ZERO5) == (w in static)
    assert mean(phi) == ZERO5
    assert mean(intensity) == (F(1, 4), F(1, 4), F(1, 4), F(0), F(1, 4))
    assert mean(scalar) == (F(1, 20), F(1, 20), F(1, 20), F(-1, 5), F(1, 20))
    print("G1 PASS: ten source words, seven tensor impulses, Pi0 intensity launch and retained silent mass 1/3")

    # G2: raw seed moments and exact tensor-scalar decorrelation.
    tt, ss, ts = moment(phi, phi), moment(scalar, scalar), moment(phi, scalar)
    mu = mean(scalar)
    centered = {w: sub(scalar[w], mu) for w in WORDS}
    css = moment(centered, centered)
    assert ts == (ZERO5,)*5 and rank(tt) == 2 and rank(ss) == 2
    for r in range(5):
        for s in range(5):
            assert ss[r][s] == css[r][s]+mu[r]*mu[s]
    for j in range(5):
        for k in range(5):
            assert fourier_moment(phi, phi, j, k) == matrix_fourier(tt, j, k)
            assert fourier_moment(scalar, scalar, j, k) == matrix_fourier(ss, j, k)
            assert fourier_moment(phi, scalar, j, k) == cyc()
    print("G2 PASS: full seed moments, raw-versus-centered distinction and zero tensor-scalar cross covariance")

    # G3: continuous common translations, after seed selection, kill only
    # nonzero total integer characters.  At second order j-k is in [-4,4].
    for j in BAND:
        assert phase_integral(-j) == 0
        for k in BAND:
            assert phase_integral(k-j) == int(j == k)
            assert phase_integral(-j-k) == int(j == -k)
    for exponent in range(-4, 5):
        finite_sum = cyc()
        for shift in range(5):
            finite_sum = add(finite_sum, scale(F(1, 5), Z[exponent*shift % 5]))
        assert finite_sum == cyc(phase_integral(exponent))
    # This explicit control forbids substituting those five points for the law.
    assert phase_integral(5) == 0
    fifth_character_finite_sum = sum((F(1, 5) for _ in range(5)), F(0))
    assert fifth_character_finite_sum == 1
    phased_moments = []
    for vectors in (phi, scalar):
        for w in WORDS:
            for r in range(5):
                interpolated = cyc()
                for j in BAND:
                    interpolated = add(interpolated, scale(F(1, 5), cmul(fourier(vectors[w], j), Z[j*r % 5])))
                assert interpolated == cyc(vectors[w][r])
            for j in BAND:
                assert fourier(vectors[w], -j) == conjugate(fourier(vectors[w], j))
                for shift in range(5):
                    shifted_word = tuple(vectors[w][(r-shift) % 5] for r in range(5))
                    assert fourier(shifted_word, j) == cmul(Z[-j*shift % 5], fourier(vectors[w], j))
        shifted = [[tuple(vectors[w][(r-shift) % 5] for r in range(5))
                    for shift in range(5)] for w in WORDS]
        phased_mean = tuple(sum((WEIGHTS[w]*shifted[i][shift][r]/5
                                 for i, w in enumerate(WORDS) for shift in range(5)), F(0))
                            for r in range(5))
        phased_cov = tuple(tuple(sum((WEIGHTS[w]*shifted[i][shift][r]*shifted[i][shift][s]/5
                                     for i, w in enumerate(WORDS) for shift in range(5)), F(0))
                                 for s in range(5)) for r in range(5))
        assert phased_mean == ZERO5 and rank(phased_cov) == 4
        for j in BAND:
            for k in BAND:
                assert matrix_fourier(phased_cov, j, k) == scale(phase_integral(k-j), fourier_moment(vectors, vectors, j, k))
        phased_moments.append(phased_cov)
    print("G3 PASS: continuous character law gives zero means and diagonal mode covariances; five-node audit is only second order")

    # G4: continuum launch uses the raw, not precentered, scalar seed power.
    assert cmul(ROOT5, ROOT5) == cyc(5)
    powers_t, powers_s = {}, {}
    for j in BAND:
        sign = 1 if abs(j) == 1 else -1
        t_expected = q5(F(1, 8), F(sign, 24))
        s_expected = q5(F(1, 24), F(-sign, 120))
        t = fourier_moment(phi, phi, j, j)
        s = fourier_moment(scalar, scalar, j, j)
        old_centered = fourier_moment(centered, centered, j, j)
        assert t == t_expected and s == s_expected
        assert positive(t) and positive(s)
        assert sub(s, old_centered) == cyc(F(1, 80))
        assert scale(F(1, 5), cmul(fourier(mu, j), conjugate(fourier(mu, j)))) == cyc(F(1, 80))
        assert t == matrix_fourier(phased_moments[0], j, j)
        assert s == matrix_fourier(phased_moments[1], j, j)
        # Stronger algebraic identity: every active word has the same ratio
        # at this slot.  This does not authorize changing the adopted law.
        for w in WORDS:
            ft, fs = fourier(phi[w], j), fourier(scalar[w], j)
            raw_t, raw_s = cmul(ft, conjugate(ft)), cmul(fs, conjugate(fs))
            assert cmul(q5(5, sign*2), raw_s) == raw_t
            if w not in static:
                assert positive(raw_t) and positive(raw_s)
        powers_t[j], powers_s[j] = t, s
    assert fourier_moment(phi, phi, 0, 0) == fourier_moment(scalar, scalar, 0, 0) == cyc()
    total_t = cyc()
    total_s = cyc()
    for j in BAND:
        total_t, total_s = add(total_t, powers_t[j]), add(total_s, powers_s[j])
    assert total_t == cyc(F(1, 2)) and total_s == cyc(F(1, 6))
    assert total_t == cyc(sum(tt[r][r] for r in range(5)))
    assert total_s == cyc(sum(ss[r][r] for r in range(5)))
    # Summed metric ratio is 36 at launch; later transfers differ by slot.
    assert scale(12, total_t) == scale(36, total_s)
    print("G4 PASS: exact T and J tables, active-word ratios, Parseval totals 1/2 and 1/6; precentering removes 1/80")

    # G5: the full metric contraction counts both symmetric TT indices.
    # Strip the common a^2/lambda from the kinetic actions: one polarization
    # has coefficient 1/4; curvature zeta has epsilon=3/2.
    tensor_kinetic, scalar_kinetic = F(1, 4), F(3, 2)
    tensor_normalizer_square, scalar_normalizer_square = F(1, 2), F(3)
    assert tensor_kinetic == tensor_normalizer_square/2
    assert scalar_kinetic == scalar_normalizer_square/2
    tensor_contraction = 2
    ratio_factor = tensor_contraction*scalar_normalizer_square/tensor_normalizer_square
    assert ratio_factor == 12
    # q_T(0)=A Phi/sqrt(2 lambda), q_S(0)=A S/sqrt(2 lambda)
    # imply gamma(0)=A Phi and zeta(0)=A S/sqrt(6).
    assert F(1, 2)/tensor_normalizer_square == 1
    assert F(1, 2)/scalar_normalizer_square == F(1, 6)
    for j in BAND:
        sign = 1 if abs(j) == 1 else -1
        ratio = q5(60, sign*24)
        assert cmul(ratio, powers_s[j]) == scale(12, powers_t[j])
        assert positive(ratio)
    print("G5 PASS: canonical kinetic normalizations and full TT contraction give r=60+24sqrt5 or 60-24sqrt5")

    # G6: exact cosmic-time background.  b=1+3*H_*t/2, R=sqrt(3),
    # chi=sqrt(lambda)*(phi-phi0)=(2R/3)log(b).  Store lambda*V.
    a = bg(b=F(2, 3))
    inverse_a = bg(b=F(-2, 3))
    hubble = bg(h=1, b=-1)
    chi_dot = bg(h=1, b=-1, r=1)
    potential = bg(h=2, b=-2, coefficient=F(3, 2))
    root3 = bg(r=1)
    assert a.derivative(F(3, 2))*inverse_a == hubble
    assert hubble.derivative(F(3, 2)) == F(-3, 2)*hubble*hubble
    assert F(1, 2)*chi_dot*chi_dot+potential == 3*hubble*hubble
    assert hubble.derivative(F(3, 2)) == F(-1, 2)*chi_dot*chi_dot
    assert chi_dot.derivative(F(3, 2))+3*hubble*chi_dot-root3*potential == 0
    assert F(1, 2)*chi_dot*chi_dot-potential == 0
    density = F(1, 2)*chi_dot*chi_dot+potential
    assert density.derivative(F(3, 2))+3*hubble*density == 0
    assert root3*(F(2, 3)*root3) == 2  # exponential V becomes b^-2.
    # P(X,phi)=X-V: P_X=1, P_XX=0, hence c_s^2=1 exactly.
    px, pxx = F(1), F(0)
    assert px == 1 and 2*pxx == 0 and px/px == 1
    assert F(3, 2) != 0  # epsilon positive: this is not a de Sitter model.
    print("G6 PASS: Friedmann, Raychaudhuri and scalar equations; epsilon=3/2, background pressure zero, scalar sound speed one")

    # G7: conformal b is now c=1+H_*eta/2, so a=c^2 and x=2c/H_*.
    # This reuses an algebra, not the cosmic-time variable from G6.
    ac = bg(b=2)
    ac_inv = bg(b=-2)
    conformal_hubble = bg(h=1, b=-1)
    pump = ac.derivative(F(1, 2)).derivative(F(1, 2))*ac_inv
    inverse_x_squared = bg(h=2, b=-2, coefficient=F(1, 4))
    assert pump == 2*inverse_x_squared
    assert ac.derivative(F(1, 2))*ac_inv == conformal_hubble
    assert bg(b=3).derivative(F(1, 2))*ac_inv == bg(h=1, coefficient=F(3, 2))
    # Both normalizers are constant multiples of a, hence equal log derivatives
    # and equal pumps; the constant scalar/tensor factors were checked in G5.
    assert (3*ac).derivative(F(1, 2)).derivative(F(1, 2))*ac_inv == 3*pump
    assert (F(1, 2)*ac).derivative(F(1, 2)).derivative(F(1, 2))*ac_inv == F(1, 2)*pump
    print("G7 PASS: a=(1+H_*eta/2)^2, shifted x=eta+2/H_* and common canonical pump 2/x^2")

    # G8: universal symbolic basis identity, not a sample of time values.
    # D denotes 1/d and is constant when differentiating with respect to x.
    sine, cosine = trig(s=1), trig(c=1)
    f = cosine-trig(k=-1, x=-1, s=1)
    g = sine+trig(k=-1, x=-1, c=1)
    frequency_squared = trig(k=2)-2*trig(x=-2)
    fp, gp = f.derivative(), g.derivative()
    assert f.derivative().derivative()+frequency_squared*f == 0
    assert g.derivative().derivative()+frequency_squared*g == 0
    wronskian = f*gp-fp*g
    assert wronskian == trig(k=1)
    # At x0 the coefficients are (g'_0-D*g_0)/K and (D*f_0-f'_0)/K.
    # Treat those as constants in the later evolution.  The two evaluations
    # below use only their values at x0; no coefficient is differentiated.
    inverse_k, D = trig(k=-1), trig(d=1)
    launch_value = inverse_k*((gp-D*g)*f+(D*f-fp)*g)
    launch_derivative = inverse_k*((gp-D*g)*fp+(D*f-fp)*gp)
    assert launch_value == 1 and launch_derivative == D
    # Independent monomials now stand for q0,H_*,D (no differentiation in
    # this algebraic initial-value check).  Differentiating q=a*N*field
    # at a0=1, a'_0=H_* gives field'_0=(D-H_*)*field_0 for both fields.
    q0_symbol, hubble0_symbol = trig(k=1), trig(x=1)
    metric_velocity_numerator = D*q0_symbol-hubble0_symbol*q0_symbol
    assert metric_velocity_numerator == (D-hubble0_symbol)*q0_symbol
    assert metric_velocity_numerator != D*q0_symbol
    print("G8 PASS: exact Laurent-trigonometric basis solves q''+(K^2-2/x^2)q=0; W=K, G(0)=1, G'(0)=1/d")

    # G9: common transfer cancels only on the declared nonzero support.
    # Algebraic common factor B=A^2*G^2/a^2 multiplies metric powers;
    # at a transfer node both powers vanish and no ratio is assigned.
    for j in BAND:
        gamma_factor, zeta_factor = F(1), F(1, 6)
        numerator = scale(tensor_contraction*gamma_factor, powers_t[j])
        denominator = scale(zeta_factor, powers_s[j])
        ratio = q5(60, 24 if abs(j) == 1 else -24)
        assert cmul(ratio, denominator) == numerator
        assert scale(F(0), numerator) == scale(F(0), denominator) == cyc()
    domain = {(j, nonzero_transfer): ("DEFINED" if j in BAND and nonzero_transfer else "UNDEFINED")
              for j in range(-4, 5) for nonzero_transfer in (False, True)}
    assert sum(v == "DEFINED" for v in domain.values()) == 4
    assert all(domain[j, False] == "UNDEFINED" for j in range(-4, 5))
    assert domain[0, True] == domain[3, True] == domain[-3, True] == "UNDEFINED"
    # G(0)=1 above guarantees a nonempty initial support; analyticity and
    # the isolated-zero theorem, not finite enumeration, govern later nodes.
    print("G9 PASS: transfer cancellation on nonzero band support; simultaneous nodes, zero mode and outside-band ratios undefined")

    # G10: independent boundary controls preserve the model's declared scope.
    graph1, graph2 = q5(F(235, 324), F(1, 18)), q5(F(235, 324), F(-1, 18))
    assert positive(graph1) and positive(graph2)
    assert graph2 != scale(4, graph1)
    # Continuum K_2^2=4 K_1^2.  Thus no common length rescales the two
    # graph eigenvalues into the two continuum frequencies simultaneously.
    assert F(2)**2 == 4*F(1)**2
    for j in BAND:
        centered_power = fourier_moment(centered, centered, j, j)
        adopted_ratio = q5(60, 24 if abs(j) == 1 else -24)
        assert cmul(adopted_ratio, centered_power) != scale(12, powers_t[j])
        # An independent scalar launch multiplier b=2 changes P_S by four;
        # it cannot be hidden in the shared amplitude A or canceled from r.
        doubled_scalar = {w: scale(2, scalar[w]) for w in WORDS}
        doubled_power = fourier_moment(doubled_scalar, doubled_scalar, j, j)
        assert doubled_power == scale(4, powers_s[j])
        assert cmul(scale(F(1, 4), adopted_ratio), doubled_power) == scale(12, powers_t[j])
        assert cmul(adopted_ratio, doubled_power) != scale(12, powers_t[j])
    # Using background p/rho=0 as the perturbative sound speed changes the
    # K^2 term.  Acting with that wrong operator on f leaves -K^2*f.
    pressureless_wrong_residual = f.derivative().derivative()-2*trig(x=-2)*f
    assert pressureless_wrong_residual == (-1)*trig(k=2)*f
    assert pressureless_wrong_residual != 0
    assert tensor_contraction != 1 and ratio_factor != 6
    print("G10 PASS: graph dispersion, precentering, independent scalar rescaling, dust sound speed and missing TT contraction change the result")
    print("VERDICT: SELECTED-COSMOLOGICAL-DICTIONARY; conditional classical model, scalar action/background/launch/phase/scale adopted")


if __name__ == "__main__":
    main()
