#!/usr/bin/env python3
"""Exact primary audit; no scientific companion code is imported or read.

The field is represented by rational pairs in the basis (1, phi).  Formal
solutions use triangular coefficient recursion, and roots use the binomial
series.  Every serialized state and invariant is computed from these states.
"""

from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path
import subprocess
import sys


class AuditFailure(Exception):
    """A discrepancy against an explicitly frozen scientific check."""


def require(condition, code):
    if not condition:
        raise AuditFailure(code)


class F:
    """Q(phi), phi**2 = phi + 1, as two reduced rational components."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = a if isinstance(a, Fraction) else Fraction(a)
        self.b = b if isinstance(b, Fraction) else Fraction(b)

    def __add__(self, other):
        if isinstance(other, (int, Fraction)):
            other = F(other)
        if not isinstance(other, F):
            return NotImplemented
        return F(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        if isinstance(other, (int, Fraction)):
            other = F(other)
        if not isinstance(other, F):
            return NotImplemented
        return F(self.a - other.a, self.b - other.b)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            return F(self.a * other, self.b * other)
        if not isinstance(other, F):
            return NotImplemented
        if not self or not other:
            return ZERO
        if not self.b:
            return F(self.a * other.a, self.a * other.b)
        if not other.b:
            return F(self.a * other.a, self.b * other.a)
        bb = self.b * other.b
        return F(self.a * other.a + bb,
                 self.a * other.b + self.b * other.a + bb)

    __rmul__ = __mul__

    def inverse(self):
        # Conjugation sends phi to 1-phi.
        norm = self.a * self.a + self.a * self.b - self.b * self.b
        if not norm:
            raise ZeroDivisionError("zero field denominator")
        return F((self.a + self.b) / norm, -self.b / norm)

    def __truediv__(self, other):
        if isinstance(other, (int, Fraction)):
            return F(self.a / other, self.b / other)
        if not isinstance(other, F):
            return NotImplemented
        return self * other.inverse()

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __eq__(self, other):
        if isinstance(other, (int, Fraction)):
            return self.a == other and not self.b
        if isinstance(other, F):
            return self.a == other.a and self.b == other.b
        return NotImplemented

    def __bool__(self):
        return bool(self.a or self.b)

    def sign(self):
        # 2(a+b phi)=(2a+b)+b sqrt(5); compare rational squares
        # only when the two summands have opposing signs.
        u = 2 * self.a + self.b
        v = self.b
        if not v:
            return (u > 0) - (u < 0)
        if not u:
            return (v > 0) - (v < 0)
        if (u > 0) == (v > 0):
            return (u > 0) - (u < 0)
        delta = u * u - 5 * v * v
        if not delta:
            return 0
        return ((u > 0) - (u < 0)) * ((delta > 0) - (delta < 0))


ZERO = F()
ONE = F(1)
PHI = F(0, 1)
GAMMA = PHI - ONE
ORDER = 4


class Jet:
    """A fixed-length, exact truncated power series; no global order state."""

    __slots__ = ("c",)

    def __init__(self, coefficients):
        self.c = tuple(coefficients)

    def constant(self, value):
        if not isinstance(value, F):
            value = F(value)
        return Jet((value,) + (ZERO,) * (len(self.c) - 1))

    def __add__(self, other):
        if not isinstance(other, Jet):
            other = self.constant(other)
        if len(self.c) != len(other.c):
            raise ValueError("inconsistent formal orders")
        return Jet(tuple(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Jet(tuple(-a for a in self.c))

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, Jet):
            return Jet(tuple(a * other for a in self.c))
        if len(self.c) != len(other.c):
            raise ValueError("inconsistent formal orders")
        out = [ZERO] * len(self.c)
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(other.c[:len(self.c) - i]):
                    if b:
                        out[i + j] = out[i + j] + a * b
        return Jet(out)

    __rmul__ = __mul__

    def inverse(self):
        lead = self.c[0].inverse()
        out = [lead]
        for m in range(1, len(self.c)):
            out.append(-lead * sum((self.c[j] * out[m - j]
                                    for j in range(1, m + 1)), ZERO))
        result = Jet(out)
        # Checking the actual inverse is part of every denominator audit.
        require(self * result == self.constant(ONE), "F02_GEOMETRY")
        return result

    def __truediv__(self, other):
        if isinstance(other, Jet):
            return self * other.inverse()
        return Jet(tuple(a / other for a in self.c))

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __eq__(self, other):
        if not isinstance(other, Jet):
            other = self.constant(other)
        return self.c == other.c


def root_one(value, code):
    """(1+v)^(1/2) by the binomial expansion, with exact truncation."""
    require(value.c[0] == ONE, code)
    v = value - ONE
    power = value.constant(ONE)
    root = power
    coefficient = Fraction(1)
    for k in range(1, len(value.c)):
        coefficient *= (Fraction(1, 2) - k + 1) / k
        power = power * v
        root = root + power * coefficient
    require(root * root == value and root.c[0].sign() > 0, code)
    return root


def madd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def msub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, s):
    return tuple(x * s for x in a)


def mm(a, b):
    return (a[0] * b[0] + a[1] * b[2],
            a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2],
            a[2] * b[1] + a[3] * b[3])


def transpose(a):
    return (a[0], a[2], a[1], a[3])


def mv(a, p):
    return (a[0] * p[0] + a[1] * p[1],
            a[2] * p[0] + a[3] * p[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def outer(a, b):
    return (a[0] * b[0], a[0] * b[1],
            a[1] * b[0], a[1] * b[1])


def trace(a):
    return a[0] + a[3]


def determinant(a):
    return a[0] * a[3] - a[1] * a[2]


def matrix_inverse(a):
    det = determinant(a)
    require(bool(det), "F02_GEOMETRY")
    out = scale((a[3], -a[1], -a[2], a[0]), ONE / det)
    require(mm(a, out) == IDENTITY, "F02_GEOMETRY")
    return out


def spd(a):
    return a[1] == a[2] and a[0].sign() > 0 and determinant(a).sign() > 0


IDENTITY = (ONE, ZERO, ZERO, ONE)
ZERO_MATRIX = (ZERO,) * 4
ZERO_VECTOR = (ZERO, ZERO)
G0 = (ONE, GAMMA / 2, GAMMA / 2, ONE)
U = ((ONE, ZERO), (ZERO, ONE), (-ONE, GAMMA),
     (-GAMMA, -GAMMA), (GAMMA, -ONE))


def lift(values, degree):
    return tuple(Jet((v,) + (ZERO,) * degree) for v in values)


def initial_state(g, pi, degree):
    return (lift(g, degree), lift(pi, degree),
            tuple(lift(ZERO_VECTOR, degree) for _ in U))


def total_p(counts, p):
    return tuple(sum((F(n) * v[j] for n, v in zip(counts, p)), ZERO)
                 for j in range(2))


def lengths(g, p, code):
    return tuple(root_one(dot(v, mv(g, v)), code) for v in p)


def matter(counts, p, roots):
    zero = roots[0] * 0
    energy = zero
    t = (zero,) * 4
    for n, v, e in zip(counts, p, roots):
        if n:
            energy = energy + n * e
            t = madd(t, scale(outer(v, v), n / e))
    return energy, t


def invariant_values(state, counts, p, roots):
    g, pi, positions = state
    energy = sum((n * e for n, e in zip(counts, roots) if n), roots[0] * 0)
    gp = mm(g, pi)
    kinetic = trace(mm(gp, gp)) / 2
    momentum = total_p(counts, p)
    mass = energy * energy - dot(momentum, mv(g, momentum))
    dilation = trace(gp)
    charge = scale(gp, 2)
    for n, x, v in zip(counts, positions, p):
        if n:
            charge = madd(charge, scale(outer(x, v), n))
    return (kinetic, energy, mass, dilation, charge)


def flow_rhs(state, counts, p, code, roots=None):
    g, pi, positions = state
    if roots is None:
        roots = lengths(g, p, code)
    _, t = matter(counts, p, roots)
    dg = mm(mm(g, pi), g)
    dpi = scale(madd(mm(mm(pi, g), pi), scale(t, Fraction(1, 2))), -1)
    zero = g[0] * 0
    dx = tuple(scale(mv(g, v), 1 / e) if n else (zero, zero)
               for n, v, e in zip(counts, p, roots))
    return (dg, dpi, dx)


def dg_rhs(old, new, counts, p, old_roots, new_roots):
    g0, pi0, _ = old
    g1, pi1, _ = new
    gs = madd(g0, g1)
    ps = madd(pi0, pi1)
    a = scale(madd(mm(mm(pi0, gs), pi0), mm(mm(pi1, gs), pi1)),
              Fraction(1, 4))
    b = scale(madd(mm(mm(g0, ps), g0), mm(mm(g1, ps), g1)),
              Fraction(1, 4))
    zero = g1[0] * 0
    q = (zero,) * 4
    dx = []
    for n, v, em, ep in zip(counts, p, old_roots, new_roots):
        inv = 1 / (em + ep)
        if n:
            q = madd(q, scale(outer(v, v), n * inv))
            dx.append(scale(mv(gs, v), inv))
        else:
            dx.append((zero, zero))
    return (b, scale(madd(a, q), -1), tuple(dx)), (a, b, q)


def state_flat(state):
    g, pi, positions = state
    return tuple(g) + tuple(pi) + tuple(v for x in positions for v in x)


def state_unflat(values):
    return (tuple(values[:4]), tuple(values[4:8]),
            tuple(tuple(values[8 + 2*k:10 + 2*k]) for k in range(5)))


def solve(counts, pi, method):
    """Compute coefficient m from only coefficients 0,...,m-1."""
    columns = [[v] for v in state_flat((G0, pi, (ZERO_VECTOR,) * 5))]
    for m in range(1, ORDER + 1):
        state = state_unflat(tuple(Jet(c) for c in columns))
        if method == "FLOW":
            rhs = flow_rhs(state, counts, U, "F03_FLOW")
            divisor = m
        else:
            old = initial_state(G0, pi, m - 1)
            old_roots = tuple(old[0][0].constant(ONE) for _ in U)
            new_roots = lengths(state[0], U, "F05_DG")
            rhs, _ = dg_rhs(old, state, counts, U, old_roots, new_roots)
            divisor = 1
        for c, r in zip(columns, state_flat(rhs)):
            c.append(r.c[m - 1] / divisor)
    return state_unflat(tuple(Jet(c) for c in columns))


def derivative(series):
    return tuple((m + 1) * series.c[m + 1] for m in range(ORDER))


def zero_higher(series):
    return all(not value for value in series.c[1:])


def h_times(series):
    return Jet((ZERO,) + series.c[:-1])


def charge_defect(old, new):
    gm, pm, _ = old
    gp, pp, _ = new
    mean_g = scale(madd(gm, gp), Fraction(1, 2))
    mean_p = scale(madd(pm, pp), Fraction(1, 2))
    d = msub(gp, gm)
    e = msub(pp, pm)
    right = msub(mm(mm(mm(d, mean_p), d), mean_p),
                 mm(mm(mm(mean_g, e), mean_g), e))
    return scale(right, Fraction(1, 2))


def audit_series(state, counts, p, g_initial, pi_initial, method, code=None):
    g, pi, positions = state
    main_code = code or ("F03_FLOW" if method == "FLOW" else "F05_DG")
    charge_code = code or "F06_CHARGE"
    exchange_code = code or "F04_EXCHANGE"
    old = initial_state(g_initial, pi_initial, ORDER)
    require(tuple(v.c[0] for v in state_flat(state)) ==
            tuple(v.c[0] for v in state_flat(old)), main_code)
    require(g[1] == g[2] and pi[1] == pi[2], main_code)
    for n, x in zip(counts, positions):
        if not n:
            require(all(v == 0 for v in x), main_code)
    roots = lengths(g, p, main_code)
    invs = invariant_values(state, counts, p, roots)
    kinetic, energy, mass, dilation, charge = invs
    require(zero_higher(kinetic + energy), exchange_code)
    if method == "FLOW":
        rhs = flow_rhs(state, counts, p, main_code, roots)
        for value, r in zip(state_flat(state), state_flat(rhs)):
            require(derivative(value) == r.c[:ORDER], main_code)
        require(all(zero_higher(v) for v in charge), charge_code)
        _, t = matter(counts, p, roots)
        gd = tuple(Jet(tuple((m + 1) * v.c[m + 1]
                            for m in range(ORDER)) + (ZERO,)) for v in g)
        exchange = trace(mm(t, gd)) / 2
        require(derivative(energy) == exchange.c[:ORDER], exchange_code)
        require(derivative(kinetic) == tuple(-v for v in exchange.c[:ORDER]),
                exchange_code)
        require(derivative(dilation) == tuple(-v / 2 for v in energy.c[:ORDER]),
                exchange_code)
    else:
        old_roots = lengths(old[0], p, main_code)
        rhs, _ = dg_rhs(old, state, counts, p, old_roots, roots)
        for value, base, r in zip(state_flat(state), state_flat(old),
                                  state_flat(rhs)):
            require(value - base == h_times(r), main_code)
        old_inv = invariant_values(old, counts, p, old_roots)
        predicted = tuple(h_times(v) for v in charge_defect(old, state))
        require(msub(charge, old_inv[4]) == predicted, charge_code)
        if all(not v for v in pi_initial):
            _, t0 = matter(counts, p, old_roots)
            gt = mm(old[0], t0)
            cubic = scale(mm(gt, gt), Fraction(-1, 8))
            require(tuple(v.c[3] for v in charge) ==
                    tuple(v.c[0] for v in cubic), charge_code)
    return invs


def directional_audit(counts, pi):
    base = initial_state(G0, pi, 1)
    roots = lengths(base[0], U, "F02_GEOMETRY")
    _, t = matter(counts, U, roots)
    grad_g = mm(mm(base[1], base[0]), base[1])
    grad_pi = mm(mm(base[0], base[1]), base[0])
    directions = ((ONE, ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO, ONE),
                  (ZERO, ONE, ONE, ZERO))
    derivatives = []
    for s in directions:
        varied_g = tuple(Jet((g, d)) for g, d in zip(G0, s))
        inv_g = invariant_values((varied_g, base[1], base[2]), counts, U,
                                 lengths(varied_g, U, "F02_GEOMETRY"))
        varied_pi = tuple(Jet((p, d)) for p, d in zip(pi, s))
        inv_pi = invariant_values((base[0], varied_pi, base[2]), counts, U, roots)
        kg = inv_g[0].c[1]
        kp = inv_pi[0].c[1]
        eg = inv_g[1].c[1]
        require(kg == trace(mm(grad_g, s)).c[0], "F04_EXCHANGE")
        require(kp == trace(mm(grad_pi, s)).c[0], "F04_EXCHANGE")
        require(eg == trace(mm(t, s)).c[0] / 2, "F04_EXCHANGE")
        derivatives.append((kg, kp, eg))
    return tuple(derivatives)


def encode(values):
    return ",".join(str(component) for value in values
                    for component in (value.a, value.b))


def state_fields(state, invs, degree=None):
    g, pi, positions = state
    kinetic, energy, mass, dilation, charge = invs
    fields = (g, pi, tuple(v for x in positions for v in x),
              (kinetic,), (energy,), (mass,), (dilation,), charge)
    if degree is not None:
        fields = tuple(tuple(v.c[degree] for v in field) for field in fields)
    return tuple(encode(field) for field in fields)


def authority_check():
    root = Path(__file__).resolve().parents[2]
    authority = (
        ("canon/CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
        ("canon/CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
        ("canon/FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
        ("canon/REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
        ("canon/CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
    )
    checked = 0
    for name, size, digest in authority:
        path = root / name
        require(path.is_file(), "F01_AUTHORITY")
        data = path.read_bytes()
        require(len(data) == size and sha256(data).hexdigest() == digest,
                "F01_AUTHORITY")
        checked += 1
    return checked


def finite_witness(g_inverse):
    counts = (1,) * 5
    h = F(Fraction(1100, 1921))
    old = (scale(G0, Fraction(36, 25)), ZERO_MATRIX, (ZERO_VECTOR,) * 5)
    new = (G0, scale(g_inverse, -1),
           tuple(scale(mv(G0, v), Fraction(1220, 1921)) for v in U))
    roots_old = (F(Fraction(6, 5)),) * 5
    roots_new = (ONE,) * 5
    for state, roots in ((old, roots_old), (new, roots_new)):
        require(spd(state[0]), "F08_WITNESS")
        for p, e in zip(U, roots):
            require(e.sign() > 0 and e * e == dot(p, mv(state[0], p)),
                    "F08_WITNESS")
    rhs, quantities = dg_rhs(old, new, counts, U, roots_old, roots_new)
    for before, after, r in zip(state_flat(old), state_flat(new), state_flat(rhs)):
        require(after - before == h * r, "F08_WITNESS")
    vi = invariant_values(old, counts, U, roots_old)
    vf = invariant_values(new, counts, U, roots_new)
    require(vi[:4] == (F(0), F(6), F(36), F(0)), "F08_WITNESS")
    require(vf[:4] == (F(1), F(5), F(25), F(-2)), "F08_WITNESS")
    require(vi[0] + vi[1] == vf[0] + vf[1] == F(6), "F08_WITNESS")
    require(total_p(counts, U) == ZERO_VECTOR, "F08_WITNESS")
    delta_j = msub(vf[4], vi[4])
    require(vi[4] == ZERO_MATRIX and
            delta_j == scale(IDENTITY, Fraction(-792, 1921)), "F08_WITNESS")
    require(delta_j == scale(charge_defect(old, new), h), "F08_WITNESS")
    a, b, q = quantities
    dg = msub(new[0], old[0])
    dpi = msub(new[1], old[1])
    require(vf[0] - vi[0] == trace(mm(a, dg)) + trace(mm(b, dpi)), "F08_WITNESS")
    require(vf[1] - vi[1] == trace(mm(q, dg)), "F08_WITNESS")
    require(vf[0] - vi[0] == -h * trace(mm(b, q)), "F08_WITNESS")

    # Differentiate f1 and f2 using their frozen derivative formulas.
    x, y, xx, yy = F(Fraction(36, 25)), ZERO, ONE, -ONE
    sx, sxx = F(Fraction(6, 5)), ONE
    denominator = (sx + sxx) * (sx + sxx)
    f1_xx = ONE - h * xx * (y + yy) / 2
    f1_yy = -h * (x * x + xx * xx) / 4
    f2_xx = h * (y * y + yy * yy) / 4 - 5 * h / (4 * sxx * denominator)
    f2_yy = ONE + h * yy * (x + xx) / 2
    f1_x = -ONE - h * x * (y + yy) / 2
    f1_y = f1_yy
    f2_x = h * (y * y + yy * yy) / 4 - 5 * h / (4 * sx * denominator)
    f2_y = -ONE + h * y * (x + xx) / 2
    det_out = determinant((f1_xx, f1_yy, f2_xx, f2_yy))
    det_in = determinant((f1_x, f1_y, f2_x, f2_y))
    ratio = det_in / det_out
    require(det_out == F(Fraction(1423025, 1921**2)) and det_out.sign() > 0,
            "F08_WITNESS")
    require(det_in == F(Fraction(6875, 6 * 1921)) and det_in.sign() > 0,
            "F08_WITNESS")
    require(ratio == F(Fraction(528275, 341526)) and ratio != ONE, "F08_WITNESS")
    return h, old, new, vi, vf, delta_j, det_out, det_in, ratio


def negative_controls(g_inverse, witness):
    detected = []

    def record(name, condition):
        require(condition, "F09_NEGATIVE_CONTROL")
        detected.append(name)

    one_count = (1, 0, 0, 0, 0)
    base = initial_state(G0, ZERO_MATRIX, 0)
    roots = lengths(base[0], U, "F09_NEGATIVE_CONTROL")
    energy, tj = matter(one_count, U, roots)
    t = tuple(v.c[0] for v in tj)
    p = total_p(one_count, U)
    r = msub(scale(t, energy.c[0]), outer(p, p))
    record("NC01", r == ZERO_MATRIX and scale(t, Fraction(1, 2)) != r)

    # Actual directional polynomial derivatives are contracted with the
    # false vector field dG=G Pi G, dPi=0 (empty preparation).
    empty = (0,) * 5
    grads = directional_audit(empty, g_inverse)
    false_gdot = mm(mm(G0, g_inverse), G0)
    false_hdot = (grads[0][0] * false_gdot[0] +
                  grads[1][0] * false_gdot[3] +
                  grads[2][0] * false_gdot[1])
    record("NC02", bool(false_hdot))

    counts_two = (2, 0, 0, 0, 0)
    # Vary p0, with fixed G, in each independent covector direction.
    # Its occupied root has constant one, so the same binomial rule applies.
    momentum_gradient = []
    gjet = lift(G0, 1)
    for direction in ((ONE, ZERO), (ZERO, ONE)):
        v = tuple(Jet((component, d)) for component, d in zip(U[0], direction))
        e = root_one(dot(v, mv(gjet, v)), "F09_NEGATIVE_CONTROL")
        momentum_gradient.append((counts_two[0] * e).c[1])
    correct_velocity = scale(tuple(momentum_gradient), Fraction(1, counts_two[0]))
    unweighted_velocity = tuple(momentum_gradient)
    record("NC03", correct_velocity == mv(G0, U[0]) and
           unweighted_velocity == scale(correct_velocity, 2) and
           unweighted_velocity != correct_velocity)

    off = (ZERO, ONE, ONE, ZERO)
    derivative_off = directional_audit(empty, off)[2][0]
    single_entry = mm(mm(off, G0), off)[1]
    record("NC04", derivative_off == GAMMA and single_entry == GAMMA / 2 and
           single_entry * 2 == derivative_off and single_entry != derivative_off)

    _, _, _, vi, vf, delta_j, _, _, ratio = witness
    record("NC05", bool(vf[1] - vi[1]))
    record("NC06", any(bool(value) for value in delta_j))
    record("NC07", ratio != ONE)
    hamiltonian = vi[0] + vi[1]
    clock_momentum = F(-6)
    record("NC08", bool(hamiltonian) and clock_momentum + hamiltonian == ZERO)
    return detected


def build_certificate():
    authority_count = authority_check()
    require(PHI * PHI == PHI + ONE and PHI.sign() > 0 and GAMMA.sign() > 0,
            "F02_GEOMETRY")
    require(spd(G0), "F02_GEOMETRY")
    g_inverse = matrix_inverse(G0)
    require(all(dot(v, mv(G0, v)) == ONE for v in U), "F02_GEOMETRY")
    require(total_p((1,) * 5, U) == ZERO_VECTOR, "F02_GEOMETRY")
    moment = ZERO_MATRIX
    for v in U:
        moment = madd(moment, outer(v, v))
    require(moment == scale(g_inverse, Fraction(5, 2)), "F02_GEOMETRY")
    pi_cases = (ZERO_MATRIX, g_inverse, scale(g_inverse, -1),
                (ONE, ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO, ONE),
                (ZERO, ONE, ONE, ZERO), (ZERO, -ONE, -ONE, ZERO))
    rows = []

    def emit(*fields):
        row = "|".join(fields)
        require("\n" not in row and "\r" not in row and row.isascii(), "F10_PAYLOAD")
        rows.append(row + "\n")

    emit("G", encode(G0), encode(tuple(v for p in U for v in p)))
    for index, pi in enumerate(pi_cases):
        emit("B", str(index), encode(pi))
    count_cases = list(product(range(2), repeat=5))
    total_cases = 0
    coefficient_counts = {"FLOW": 0, "DG": 0}
    covariance_bases = {}
    for counts in count_cases:
        ntext = "".join(map(str, counts))
        for index, pi in enumerate(pi_cases):
            directional_audit(counts, pi)
            states = {}
            invariant_sets = {}
            for method in ("FLOW", "DG"):
                states[method] = solve(counts, pi, method)
                invariant_sets[method] = audit_series(states[method], counts, U,
                                                       G0, pi, method)
            for f, d in zip(state_flat(states["FLOW"]), state_flat(states["DG"])):
                require(f.c[:3] == d.c[:3], "F05_DG")
            adjacent = sum(counts[k] * counts[(k + 1) % 5] for k in range(5))
            diagonal = sum(counts[k] * counts[(k + 2) % 5] for k in range(5))
            expected_d0 = (3 - PHI) * adjacent + (2 + PHI) * diagonal
            for invs in invariant_sets.values():
                require(invs[2].c[0] == expected_d0, "F04_EXCHANGE")
            emit("C", ntext, str(index), str(sum(counts)), encode(total_p(counts, U)),
                 encode((invariant_sets["FLOW"][2].c[0],)))
            for method in ("FLOW", "DG"):
                for degree in range(ORDER + 1):
                    emit("S", ntext, str(index), method, str(degree),
                         *state_fields(states[method], invariant_sets[method], degree))
                    coefficient_counts[method] += 1
            if (counts, index) in (((1, 0, 1, 0, 0), 5), ((1, 1, 1, 1, 1), 0)):
                covariance_bases[(counts, index)] = (states, invariant_sets)
            total_cases += 1

    transformations = ((ONE, ONE, ZERO, ONE), (ZERO, ONE, ONE, ZERO),
                       (F(2), ZERO, ZERO, ONE))
    covariance_count = 0
    covariance_methods = set()
    for counts, index in (((1, 0, 1, 0, 0), 5), ((1, 1, 1, 1, 1), 0)):
        states, invariant_sets = covariance_bases[(counts, index)]
        for a in transformations:
            ai = matrix_inverse(a)
            at = transpose(a)
            ait = transpose(ai)
            p = tuple(mv(ait, v) for v in U)
            gi = mm(mm(a, G0), at)
            pii = mm(mm(ait, pi_cases[index]), ai)
            require(spd(gi) and all(dot(v, mv(gi, v)) == ONE for v in p),
                    "F07_COVARIANCE")
            emit("A", str(covariance_count), "".join(map(str, counts)), str(index),
                 encode(a), encode(tuple(v for vector in p for v in vector)))
            for method in ("FLOW", "DG"):
                g, pi, positions = states[method]
                transformed = (mm(mm(a, g), at), mm(mm(ait, pi), ai),
                               tuple(mv(a, x) for x in positions))
                actual = audit_series(transformed, counts, p, gi, pii, method,
                                      "F07_COVARIANCE")
                original = invariant_sets[method]
                require(actual[:4] == original[:4], "F07_COVARIANCE")
                require(actual[4] == mm(mm(a, original[4]), ai), "F07_COVARIANCE")
                for degree in range(ORDER + 1):
                    emit("Y", str(covariance_count), method, str(degree),
                         *state_fields(transformed, actual, degree))
                covariance_methods.add(method)
            covariance_count += 1

    witness = finite_witness(g_inverse)
    h, old, new, vi, vf, delta_j, det_out, det_in, ratio = witness
    finite_count = 0
    require(h.b == 0, "F10_PAYLOAD")
    emit("W", str(h.a))
    emit("F", "0", *state_fields(old, vi))
    emit("F", "1", *state_fields(new, vf))
    emit("R", "DG_J_DEFECT", encode(delta_j), encode((det_out,)),
         encode((det_in,)), encode((ratio,)))
    finite_count += 1
    controls = negative_controls(g_inverse, witness)
    for name in controls:
        emit("N", name, "DETECTED")
    require(authority_count == 5 and len(count_cases) == 32 and len(pi_cases) == 7,
            "F10_PAYLOAD")
    require(total_cases == 224 and coefficient_counts == {"FLOW": 1120, "DG": 1120},
            "F10_PAYLOAD")
    require(covariance_count == 6 and len(covariance_methods) == 2 and finite_count == 1,
            "F10_PAYLOAD")
    require(controls == ["NC%02d" % i for i in range(1, 9)] and len(rows) == 2550,
            "F10_PAYLOAD")
    payload = "".join(rows).encode("ascii")
    require(payload.count(b"\n") == len(rows) and b"\r" not in payload, "F10_PAYLOAD")
    certificate = (
        ("CERTIFICATE", "P-RELATIONAL-MASS-JOINT-ACTION-1"),
        ("AUTHORITY_FILES", authority_count),
        ("COUNT_PREPARATIONS", len(count_cases)),
        ("MOMENTUM_CASES", len(pi_cases)),
        ("TRAJECTORY_CASES", total_cases),
        ("FORMAL_ORDER", ORDER),
        ("FLOW_COEFFICIENTS", coefficient_counts["FLOW"]),
        ("DG_COEFFICIENTS", coefficient_counts["DG"]),
        ("COVARIANCE_CASES", covariance_count),
        ("COVARIANCE_METHODS", len(covariance_methods)),
        ("FINITE_EXCHANGE_CASES", finite_count),
        ("NEGATIVE_CONTROLS", len(controls)),
        ("PAYLOAD_RECORDS", len(rows)),
        ("PAYLOAD_SHA256", sha256(payload).hexdigest()),
        ("CERTIFICATE_RESULT", "PASS"),
    )
    require(len(certificate) == 15, "F10_PAYLOAD")
    return "".join("%s=%s\n" % item for item in certificate).encode("ascii")


def main():
    try:
        certificate = build_certificate()
        environment = {"LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1",
                       "PYTHONHASHSEED": "0", "TZ": "UTC"}
        try:
            companion = subprocess.run(
                [sys.executable, "-I", str(Path(__file__).with_name("breaker.py"))],
                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                env=environment, timeout=540, check=False, shell=False,
            )
        except subprocess.TimeoutExpired:
            raise AuditFailure("F11_BREAKER") from None
        require(companion.returncode == 0 and companion.stderr == b"" and
                companion.stdout == certificate, "F11_BREAKER")
        sys.stdout.buffer.write(certificate + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except AuditFailure as failure:
        sys.stdout.buffer.write(("FALSIFIER=%s\nRESULT=FAIL\n" % failure).encode("ascii"))


if __name__ == "__main__":
    main()
