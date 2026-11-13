# Author: A. M. Thorn <thorn@twistj.com>.
# SPDX-License-Identifier: Apache-2.0.

"""Complete scalar contact model for the one root-owned absolute-capture pin.

This module performs no scientific calculation on import.  All constants,
including pi, are initialized lazily on the first model-method invocation.
No root census, quadrature, radial extrapolation, or probability run occurs
here.  See notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/PROOF.md, Part I for the algebra and physical-sheet convention.

Integration variable: k in [-pi, pi], with object momentum P = K-k.
AD2 derivatives returned by pHdata are with respect to this k, not P.
K and E are constant interval parameters, so every enclosure is uniform
over their complete supplied intervals.

Public API:
    CaptureModel(K, E, g=None, beta=None), also named Model
    .pHdata(k, sigma, derivatives=True) -> GapData
    .pole_data(k, sigma, derivatives=True) -> GapData (same method)
    .boundary(k, sigma) -> CI for the COMPLETE weighted h_sigma*f_A
    .scalar_data(k, sigma), .geometry(k, sigma) -> ScalarData
    .scalar_A_at(P, omega) -> ScalarData, unweighted
    .selectedF1integrand(P), .f1_integrand(P) -> CI for complete f_B
    .f1(P) -> CI (same complete odd-port integrand)
    .no_pole(k, sigma) -> a one-sided proof predicate
    .incoming_density() -> the frozen selected incoming window density
    .incoming_density_at(P) -> Re(f_B)/(2*pi)

Guards:
* sigma is exactly +1 or -1.
* k boxes describe points on the physical [-pi,pi] chart.  The endpoints
  may use the outer enclosure of pi; no extension of the physical chart
  beyond those endpoints is inferred.
* pHdata requires a strict relative gap and an unambiguous sign of
  sin(omega).  It raises Uncertain otherwise.
* boundary is a pointwise boundary value AWAY FROM POLES.  The caller
  must add the complete real pole weights and the specified PV subtraction.
* A denominator box containing zero is never silently replaced by a
  selected branch.  interval_core raises Uncertain, requiring subdivision
  or the caller's certified pole/critical-point treatment.
* ScalarData retains N and D before any endpoint cancellation.  At exact
  P=0 or pi the analytic compact formula in notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/PROOF.md, Part I is authoritative;
  boxes containing an A-invisible removable factor may need a separate
  certified local treatment.
"""

from dataclasses import dataclass

from interval_core import AD2, CI, I, Q, S, Uncertain, init_constants


@dataclass(frozen=True)
class GapData:
    t: I
    H: AD2
    G: AD2
    weight: AD2
    B: AD2
    v: I
    cos_omega: I
    sin_omega: I
    eta_sign: int


@dataclass(frozen=True)
class ScalarData:
    t: I
    R: CI
    q: CI
    x: CI
    N: CI
    D: CI
    weight: I
    v: I
    cos_omega: I
    sin_omega: I
    region: str

    def f_A(self) -> CI:
        """Complete unweighted scalar, provided D is provably nonzero."""
        return 2 * self.x * self.N / self.D - 1


@dataclass(frozen=True)
class _PhaseData:
    v: AD2
    cos_omega: AD2
    sin_omega: AD2
    cos_delta: AD2
    sin_delta: AD2
    cos_delta_half: AD2
    sin_delta_half: AD2
    t: AD2
    weight: AD2


def _sign(a: I) -> int:
    if a.lo > 0:
        return 1
    if a.hi < 0:
        return -1
    return 0


def _clip(a: I, lo: int, hi: int) -> I:
    """Intersect with an independently proved exact integer range."""
    return a.intersect(I(lo * S, hi * S))


def _ad_clip(a: AD2, lo: int, hi: int) -> AD2:
    # Restricting the value by a proved range does not alter the validity
    # of the independently enclosed first and second derivatives.
    return AD2(_clip(a.v, lo, hi), a.d1, a.d2)


def _nonnegative(a: I) -> I:
    if a.hi < 0:
        raise AssertionError("A proved nonnegative boundary quantity has an empty enclosure")
    return I(max(0, a.lo), a.hi)


def _region(t: I) -> str:
    if t.lo > -4 * S and t.hi < 4 * S:
        return "gap"
    if t.lo > 4 * S or t.hi < -4 * S:
        return "continuum"
    return "threshold_box"


def _physical_R(t: I, sin_omega: I) -> CI:
    """Rectangular enclosure of the exterior radial physical R sheet.

    A threshold-straddling box uses the union of the relevant real and
    imaginary arcs.  This deliberately loses correlations but never
    chooses a sheet from a sampled midpoint.
    """
    zero = Q(0)
    region = _region(t)
    if region == "continuum":
        magnitude = (t * t - 16).sqrt()
        return CI(magnitude if t.lo > 4 * S else -magnitude, zero)
    sign_sin = _sign(sin_omega)
    if region == "gap":
        magnitude = (16 - t * t).sqrt()
        if sign_sin > 0:
            return CI(zero, magnitude)
        if sign_sin < 0:
            return CI(zero, -magnitude)
        return CI(zero, I(-magnitude.hi, magnitude.hi))

    real_lo = 0
    real_hi = 0
    if t.lo < -4 * S:
        endpoint = I(t.lo, t.lo)
        real_lo = -((endpoint * endpoint - 16).sqrt().hi)
    if t.hi > 4 * S:
        endpoint = I(t.hi, t.hi)
        real_hi = (endpoint * endpoint - 16).sqrt().hi

    overlap_lo = max(t.lo, -4 * S)
    overlap_hi = min(t.hi, 4 * S)
    imag_max = 0
    if overlap_lo <= overlap_hi:
        if overlap_lo <= 0 <= overlap_hi:
            min_abs = 0
        else:
            min_abs = min(abs(overlap_lo), abs(overlap_hi))
        closest = I(min_abs, min_abs)
        imag_max = (16 - closest * closest).sqrt().hi
    if sign_sin > 0:
        imag_lo, imag_hi = 0, imag_max
    elif sign_sin < 0:
        imag_lo, imag_hi = -imag_max, 0
    else:
        imag_lo, imag_hi = -imag_max, imag_max
    return CI(I(real_lo, real_hi), I(imag_lo, imag_hi))


class CaptureModel:
    """Lazy, exact-enclosure coefficient model on fixed K and E boxes."""

    def __init__(self, K: I, E: I, g: I | None = None, beta: I | None = None):
        self.K = K
        self.E = E
        self._supplied_g = g
        self._supplied_beta = beta
        self._ready = False

    def _ensure(self) -> None:
        if self._ready:
            return
        self.PI = init_constants()["pi"]
        self.g = 2 * self.PI / 5 if self._supplied_g is None else self._supplied_g
        self.beta = 4 * self.PI / 5 if self._supplied_beta is None else self._supplied_beta
        self.sqrt5 = Q(5).sqrt()
        self.d = Q(-3, 5)
        self.ell = Q(2, 5)
        self.omega0 = self.E - self.beta
        self.cos_omega0 = self.omega0.cos()
        self.sin_omega0 = self.omega0.sin()
        self.delta_half_base = (self.E - self.beta - self.g) / 2
        self.cos_delta_half_base = self.delta_half_base.cos()
        self.sin_delta_half_base = self.delta_half_base.sin()
        self._ready = True

    def _phases(self, k: I, sigma: int, derivatives: bool) -> _PhaseData:
        self._ensure()
        if sigma not in (-1, 1):
            raise ValueError("sigma must be exactly -1 or +1")
        if k.lo < -self.PI.hi or k.hi > self.PI.hi:
            raise Uncertain("k box is outside the declared [-pi,pi] chart")

        kk = AD2.variable(k) if derivatives else AD2.constant(k)
        P = AD2.constant(self.K) - kk
        v = _ad_clip(P.cos(), -1, 1)
        half_k = kk / 2
        root = (3 - 2 * kk.cos()).sqrt()

        # cos(epsilon/2), sin(epsilon/2).  The latter is nonnegative on
        # the physical chart, including its one-sided endpoint limits.
        a = _ad_clip(root / self.sqrt5, 0, 1)
        b = _ad_clip(2 * half_k.cos() / self.sqrt5, 0, 1)
        cos_epsilon = _ad_clip(a * a - b * b, -1, 1)
        sin_epsilon = _ad_clip(2 * a * b, 0, 1)

        cos_omega = _ad_clip(
            cos_epsilon * self.cos_omega0
            + sigma * sin_epsilon * self.sin_omega0, -1, 1
        )
        sin_omega = _ad_clip(
            cos_epsilon * self.sin_omega0
            - sigma * sin_epsilon * self.cos_omega0, -1, 1
        )

        cos_delta_half = _ad_clip(
            a * self.cos_delta_half_base
            + sigma * b * self.sin_delta_half_base, -1, 1
        )
        sin_delta_half = _ad_clip(
            a * self.sin_delta_half_base
            - sigma * b * self.cos_delta_half_base, -1, 1
        )
        cos_delta = _ad_clip(
            cos_delta_half * cos_delta_half
            - sin_delta_half * sin_delta_half, -1, 1
        )
        sin_delta = _ad_clip(2 * sin_delta_half * cos_delta_half, -1, 1)

        pulse_velocity = -2 * half_k.sin() / root
        weight = _ad_clip((1 - sigma * pulse_velocity) / 2, 0, 1)
        t = v - 5 * cos_omega
        return _PhaseData(v, cos_omega, sin_omega, cos_delta,
                          sin_delta, cos_delta_half, sin_delta_half,
                          t, weight)

    @staticmethod
    def _gap_from_phases(ph: _PhaseData) -> GapData:
        if _region(ph.t.v) != "gap":
            raise Uncertain("pHdata requires a strict relative spectral gap")
        sign_sin = _sign(ph.sin_omega.v)
        if sign_sin == 0:
            raise Uncertain("The physical gap sheet needs a certified sign of sin(omega)")
        cos_eta_half = ((4 + ph.t) / 8).sqrt()
        sin_eta_half = sign_sin * ((4 - ph.t) / 8).sqrt()
        sin_chi = (sin_eta_half * ph.cos_delta_half
                   - cos_eta_half * ph.sin_delta_half)
        cos_chi = (cos_eta_half * ph.cos_delta_half
                   + sin_eta_half * ph.sin_delta_half)
        H = ((ph.cos_delta - ph.v) * sin_chi
             - 4 * ph.sin_delta * cos_chi)
        G = (4 * (ph.cos_delta + ph.v) * cos_chi
             + ph.sin_delta * sin_chi)
        return GapData(ph.t.v, H, G, ph.weight, ph.weight * G,
                       ph.v.v, ph.cos_omega.v, ph.sin_omega.v, sign_sin)

    def pHdata(self, k: I, sigma: int, derivatives: bool = True) -> GapData:
        """Real complete gap data; first/second derivatives are in k."""
        return self._gap_from_phases(self._phases(k, sigma, derivatives))

    def pole_data(self, k: I, sigma: int, derivatives: bool = True) -> GapData:
        return self.pHdata(k, sigma, derivatives)

    def _scalar(self, v: I, cos_omega: I, sin_omega: I,
                cos_delta: I, sin_delta: I, weight: I) -> ScalarData:
        self._ensure()
        t = v - 5 * cos_omega
        region = _region(t)
        R = _physical_R(t, sin_omega)
        zero = Q(0)
        if region == "continuum":
            # Same sheet, with a cancellation-free real q expression.
            q = CI(4 / (t + R.re), zero)
        else:
            q = (CI(t, zero) - R) / 4
        x = CI(cos_delta, -sin_delta)
        x2 = x * x
        vc = CI(v, zero)
        dc = CI(self.d, zero)
        lc = CI(self.ell, zero)
        N = x2 - (vc + q) * dc * x + vc * q
        D = (x2 * x - (lc * vc + dc * q) * x2
             + (dc + lc * vc * q) * x - q)
        return ScalarData(t, R, q, x, N, D, weight, v,
                          cos_omega, sin_omega, region)

    def scalar_data(self, k: I, sigma: int) -> ScalarData:
        """Full N,D,q data for geometry checks; no denominator division."""
        ph = self._phases(k, sigma, False)
        return self._scalar(ph.v.v, ph.cos_omega.v, ph.sin_omega.v,
                            ph.cos_delta.v, ph.sin_delta.v, ph.weight.v)

    def geometry(self, k: I, sigma: int) -> ScalarData:
        return self.scalar_data(k, sigma)

    def no_pole(self, k: I, sigma: int) -> bool:
        """Return True only after a complete no-pole proof for this box.

        The open-continuum exclusion includes the possible compact endpoint
        states only when the supplied g enclosure is inside (0,pi/2), which
        contains the frozen g=2pi/5.  Other parameters use the direct D test.
        An uncertain calculation is False, never a guessed exclusion.
        """
        try:
            data = self.scalar_data(k, sigma)
            if (data.region == "continuum" and self.g.lo > 0
                    and self.g.hi < (self.PI / 2).lo):
                return True
            return (not data.D.re.contains_zero()
                    or not data.D.im.contains_zero())
        except Uncertain:
            return False

    def scalar_A_at(self, P: I, omega: I) -> ScalarData:
        """Complete unweighted scalar data at independently supplied P,omega."""
        self._ensure()
        delta = omega - self.g
        return self._scalar(_clip(P.cos(), -1, 1),
                            _clip(omega.cos(), -1, 1),
                            _clip(omega.sin(), -1, 1),
                            _clip(delta.cos(), -1, 1),
                            _clip(delta.sin(), -1, 1), Q(1))

    def boundary(self, k: I, sigma: int) -> CI:
        """Full weighted pointwise boundary value, excluding pole residues.

        Gap values use -i*B/H with exact zero real part.  On the open
        continuum the real part is evaluated from its explicitly positive
        full spectral formula.  Threshold-straddling boxes use a safe
        rectangular algebraic-sheet enclosure.  All divisions are guarded.
        """
        ph = self._phases(k, sigma, False)
        if _region(ph.t.v) == "gap":
            data = self._gap_from_phases(ph)
            return CI(Q(0), -data.B.v / data.H.v)

        data = self._scalar(ph.v.v, ph.cos_omega.v, ph.sin_omega.v,
                            ph.cos_delta.v, ph.sin_delta.v, ph.weight.v)
        value = data.f_A() * data.weight
        if data.region == "continuum":
            # For real physical q, Re f_A = (16/25)(1-v^2)(1-q^2)/|D|^2.
            # Both factors are independently known to lie in [0,1].
            object_factor = _clip(1 - data.v * data.v, 0, 1)
            return_factor = _clip(1 - data.q.re * data.q.re, 0, 1)
            positive_real = (Q(16, 25) * data.weight * object_factor
                             * return_factor / data.D.norm2())
            return CI(_nonnegative(positive_real), value.im)
        return CI(_nonnegative(value.re), value.im)

    def selectedF1integrand(self, P: I) -> CI:
        """COMPLETE odd-port f_B at E-beta, not a restricted source density.

        Integrate this over all P with dP/(2*pi) to obtain complete F1.
        Restricting the integration range is allowed only for the separately
        named prepared incoming density, never for the scattering denominator.
        """
        self._ensure()
        v = _clip(P.cos(), -1, 1)
        t = v - 5 * self.cos_omega0
        R = _physical_R(t, self.sin_omega0)
        delta = self.omega0 - self.g
        denominator = t + 4 * delta.cos()
        return CI(R.re, R.im - 4 * delta.sin()) / denominator

    def f1_integrand(self, P: I) -> CI:
        return self.selectedF1integrand(P)

    def f1(self, P: I) -> CI:
        return self.selectedF1integrand(P)

    def incoming_density_at(self, P: I) -> I:
        """Object odd AC density at supplied P; source integration is external."""
        self._ensure()
        return _nonnegative(self.selectedF1integrand(P).re) / (2 * self.PI)

    def incoming_density(self, P: I | None = None) -> I:
        """Frozen selected density, with the CP-24 finite-window error.

        With no P argument this encloses integral_{-delta}^{delta}
        rho(P,E-beta)dP/(2*pi), delta=1/1000, for the frozen source
        rectangle.  CP-24 supplies a relative symmetric-average error
        smaller than delta^2.  It is a source-density calculation, never
        a replacement for complete F1.  An explicit P argument retains
        the separately named point-density operation for compatibility.
        """
        if P is not None:
            return self.incoming_density_at(P)
        self._ensure()
        delta = Q(1, 1000)
        error = Q(1, 10 ** 6)
        factor = I((1 - error).lo, (1 + error).hi)
        return (delta / self.PI) * self.incoming_density_at(Q(0)) * factor


Model = CaptureModel
