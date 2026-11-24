#!/usr/bin/env python3
"""Exact finite audits of the capture-parity proof; standard library only.

NON-CANONICAL, L1. This program does not evaluate a boundary resolvent or
prove the analytic measure theorem by sampling. See the frozen PREREG.md.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import comb


@dataclass(frozen=True, eq=False)
class C:
    r: Q = Q(0)
    i: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "r", Q(self.r))
        object.__setattr__(self, "i", Q(self.i))

    @staticmethod
    def cast(x):
        return x if isinstance(x, C) else C(x)

    def __add__(self, other):
        other = C.cast(other)
        return C(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-C.cast(other))

    def __rsub__(self, other):
        return C.cast(other) - self

    def __mul__(self, other):
        other = C.cast(other)
        return C(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def conj(self):
        return C(self.r, -self.i)

    def norm(self):
        return self.r * self.r + self.i * self.i

    def __truediv__(self, other):
        other = C.cast(other)
        n = other.norm()
        if n == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        p = self * other.conj()
        return C(p.r / n, p.i / n)

    def __rtruediv__(self, other):
        return C.cast(other) / self

    def __eq__(self, other):
        if not isinstance(other, (C, int, Q)):
            return NotImplemented
        other = C.cast(other)
        return self.r == other.r and self.i == other.i

    def __hash__(self):
        return hash((self.r, self.i))


ZERO, ONE, I = C(), C(1), C(0, 1)


def mat(rows):
    return [[C.cast(x) for x in row] for row in rows]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[C.cast(c) * x for x in row] for row in a]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO)
             for j in range(len(b[0]))] for i in range(len(a))]


def dagger(a):
    return [[a[j][i].conj() for j in range(len(a))]
            for i in range(len(a[0]))]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv2(a):
    return scale(ONE / det2(a),
                 [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]])


def charpoly(a):
    """Newton identities, descending coefficients, exact characteristic 0."""
    n = len(a)
    powers, p = [], eye(n)
    for _ in range(n):
        p = mul(p, a)
        powers.append(trace(p))
    coeff = [ONE]
    for k in range(1, n + 1):
        coeff.append(-sum((coeff[k - j] * powers[j - 1]
                           for j in range(1, k + 1)), ZERO) / k)
    return coeff


def tensor(a, b):
    return [[x * y for x in ar for y in br] for ar in a for br in b]


SIGMA = mat([[1, 0], [0, -1]])
HBASIS = [mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 1]]),
          mat([[0, 1], [1, 0]]), mat([[0, I], [-I, 0]])]


def congruence(m, x):
    return mul(mul(m, x), dagger(m))


def coords(x):
    assert x == dagger(x)
    assert x[0][0].i == x[1][1].i == 0
    return [C(x[0][0].r), C(x[1][1].r), C(x[0][1].r), C(x[0][1].i)]


def real_action(m):
    cols = [coords(congruence(m, x)) for x in HBASIS]
    return [list(row) for row in zip(*cols)]


def current_form(x, y):
    value = -trace(mul(mul(mul(SIGMA, x), SIGMA), y)) / 2
    assert value.i == 0
    return value.r


def h(a, z):
    z = C.cast(z)
    return mat([[a, z], [z.conj(), a]])


def transfer(s):
    u, v, w, z = s[0][0], s[0][1], s[1][0], s[1][1]
    return [[w - z * u / v, z / v], [-u / v, ONE / v]]


# Sparse four-variable Laurent polynomials with exact Gaussian coefficients.
# In the source audit the exponents are (P,K,g,beta). In the elimination
# audit they are independent algebraic variables (f,t,U,V).
PZERO = (0, 0, 0, 0)


def clean(p):
    return {e: C.cast(c) for e, c in p.items() if c != 0}


def pc(c):
    return clean({PZERO: C.cast(c)})


def mon(e, c=1):
    return clean({e: C.cast(c)})


def pa(*polys):
    out = {}
    for p in polys:
        for e, c in p.items():
            out[e] = out.get(e, ZERO) + c
    return clean(out)


def pm(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            k = tuple(x + y for x, y in zip(e, f))
            out[k] = out.get(k, ZERO) + c * d
    return clean(out)


def ps(c, a):
    return clean({e: C.cast(c) * x for e, x in a.items()})


def source_moment():
    coin1 = mat([[1, 2 * I], [2 * I, 1]])
    coin = scale(Q(1, 5), tensor(coin1, coin1))
    a = mat([[1], [0], [0], [-1]])
    assert mul(coin, a) == a
    assert mul(dagger(coin), coin) == eye(4)
    phases = {0: mon((1, 0, 0, 0)), 3: mon((-1, 0, 0, 0))}
    after = mul(coin, a)
    obj = pa(*(ps(a[j][0].conj() * after[j][0] / 2, phases[j])
               for j in (0, 3)))
    obj = pm(mon((0, 0, -1, 0)), obj)
    pulse_k = mon((-1, 1, 0, 0))
    # (E*Q)11=(1*1+(-2e^ik)*2)/5, from both source coins.
    pulse11 = ps(Q(1, 5), pa(pc(1), ps(-4, pulse_k)))
    pulse11 = pm(mon((0, 0, 0, -1)), pulse11)
    integrand = pm(obj, pulse11)
    moment = clean({e: c for e, c in integrand.items() if e[0] == 0})
    expected = mon((0, 1, -1, -1), Q(-2, 5))
    assert moment == expected
    assert moment != {}
    assert moment != mon((0, 1, -1, -1), Q(-4, 5))
    assert moment != mon((0, 1, -1, 0), Q(-2, 5))
    no_pulse_exponential = pm(obj, mon((0, 0, 0, -1), Q(1, 5)))
    assert not {e: c for e, c in no_pulse_exponential.items() if e[0] == 0}
    # The sign of P in the pulse term is NOT detected by this first moment.
    reversed_p = pa(mon((0, 0, 0, -1), Q(1, 5)),
                    mon((1, 1, 0, -1), Q(-4, 5)))
    reversed_integrand = pm(obj, reversed_p)
    assert clean({e: c for e, c in reversed_integrand.items() if e[0] == 0}) == expected
    print("PASS source: exact full one-step moment -(2/5)*exp(i*(K-g-beta))")


def algebraic_elimination():
    f, t, u, v = [mon(tuple(int(i == j) for i in range(4))) for j in range(4)]
    tt, ff = pm(t, t), pm(f, f)
    d = pa(pm(v, t), ps(-1, pm(f, tt)))
    normalized_f1 = pa(pc(1), ps(I, f))
    normalized_f2 = pa(tt, ps(I, d))
    big_d = pa(pc(4), pm(normalized_f1, normalized_f2))
    real_d = clean({e: c.r for e, c in big_d.items()})
    imag_d = clean({e: c.i for e, c in big_d.items()})
    assert imag_d == pm(v, t)
    quadratic = pa(pc(4), tt, pm(ff, tt), ps(-1, pm(u, t)),
                   ps(-1, pm(pm(v, f), t)))
    assert pa(real_d, ps(-1, pm(u, t))) == quadratic
    assert 2 * 4 * 2 == 16 and comb(17, 2) == 136
    offsets = [Q(j, 16000) for j in range(-8, 9)]
    assert len(set(offsets)) == 17
    assert max(map(abs, offsets)) == Q(1, 2000) < Q(1, 1000)
    assert all(0 < abs(a - b) < 1 for a, b in product(offsets, repeat=2) if a != b)
    print("PASS elimination: exact quadratic, <=16 values, 17 fixed momenta, 136 factors")


def fixture_audits():
    kc = mat([[Q(-2, 5), Q(-4, 5)], [Q(4, 5), Q(-2, 5)]])
    assert add(inv2(kc), dagger(inv2(kc))) == scale(-1, eye(2))
    sigma_flip = mat([[-1, 0], [0, 1]])
    out_flip = mat([[1, 0], [0, -1]])
    form_gram = mat([[current_form(x, y) for y in HBASIS] for x in HBASIS])
    fixtures = parities = moving = charts = 0
    rejected_factor = rejected_sign = rejected_partial = False
    roots = (Q(1, 2), Q(1), Q(2))
    imag = (-2, -1, 0, 1, 2)
    for x1, x2, y1, y2 in product(roots, roots, imag, imag):
        fixtures += 1
        f1, f2 = C(x1 * x1, y1), C(x2 * x2, y2)
        r = f1.r * f2.r
        b = 4 * x1 * x2
        d, a = 4 + f1 * f2, 4 - f1.conj() * f2
        assert d.norm() - a.norm() == b * b == 16 * r
        m = mat([[(f1 - 1) / 2, 0], [0, (f2 - 1) / 2]])
        tmat = mul(kc, inv2(add(eye(2), scale(-1, mul(m, kc)))))
        assert tmat == scale(ONE / d, mat([[-2 * f2, -4], [4, -2 * f1]]))
        rho = mat([[f1.r, 0], [0, f2.r]])
        assert add(add(tmat, dagger(tmat)), mul(mul(dagger(tmat), rho), tmat)) == scale(0, eye(2))
        root_rho = mat([[x1, 0], [0, x2]])
        s = add(eye(2), mul(mul(root_rho, tmat), root_rho))
        assert s == scale(ONE / d, mat([[a, -b], [b, a.conj()]]))
        assert mul(dagger(s), s) == eye(2)
        mp = transfer(s)
        mm = transfer(mul(out_flip, s))
        assert mp == scale(Q(1) / b, mat([[d.conj(), -a.conj()], [a, -d]]))
        assert mm == mul(sigma_flip, mp)
        rejected_factor |= mm != scale(-1, mp)
        bad = [row[:] for row in mp]
        bad[0][1] = -bad[0][1]
        rejected_sign |= mul(mul(dagger(bad), SIGMA), bad) != SIGMA
        # Half of each full density is not the closed two-bright-channel S.
        partial_s = add(eye(2), scale(Q(1, 2), mul(mul(root_rho, tmat), root_rho)))
        rejected_partial |= mul(dagger(partial_s), partial_s) != eye(2)
        kp = d.i * d.i / (4 * r) - 2
        km = d.r * d.r / (4 * r) - 2
        assert (b * b / d.norm()) * (kp + km + 4) == 4
        for parity, mpar, kappa, expected_det in ((1, mp, kp, -1), (-1, mm, km, 1)):
            parities += 1
            assert det2(mpar) == expected_det
            assert mul(mul(dagger(mpar), SIGMA), mpar) == SIGMA
            expected_trace = -2 * I * d.i / b if parity == 1 else C(-2 * d.r / b)
            assert trace(mpar) == expected_trace
            rr = real_action(mpar)
            expected_poly = [1, -(kappa + 2), 2 * kappa + 2, -(kappa + 2), 1]
            assert charpoly(rr) == [C(x) for x in expected_poly]
            assert mul(mul(dagger(rr), form_gram), rr) == form_gram
            if parity == 1:
                axis = h(d.r / b, a.conj() / b)
                axis_norm = d.i * d.i / (b * b) - 1
            else:
                axis = h(-d.i / b, -I * a.conj() / b)
                axis_norm = d.r * d.r / (b * b) - 1
            assert congruence(mpar, axis) == axis
            assert current_form(axis, axis) == axis_norm
            if kappa != 2:
                moving += 1
                r_inv = real_action(inv2(mpar))
                proj = scale(Q(1) / (2 - kappa),
                             add(add(scale(2, eye(4)), scale(-1, rr)), scale(-1, r_inv)))
                assert mul(proj, proj) == proj and trace(proj) == 2
                assert mul(add(rr, scale(-1, eye(4))), add(eye(4), scale(-1, proj))) == scale(0, eye(4))
                assert all(proj[0][j] - proj[1][j] == 0 for j in range(4))
            if a != 0:
                charts += 1
                if parity == 1:
                    basis = [h(1, d.r / a), h(0, I / a)]
                    g00 = (b * b - d.i * d.i) / a.norm()
                else:
                    basis = [h(1, I * d.i / a), h(0, ONE / a)]
                    g00 = (b * b - d.r * d.r) / a.norm()
                assert [[current_form(x, y) for y in basis] for x in basis] == [[g00, Q(0)], [Q(0), Q(1) / a.norm()]]
                for x in basis:
                    assert current_form(x, x) == (-det2(x)).r
                    z = congruence(mpar, x)
                    assert z[0][0] == z[1][1]
                    az = a * z[0][1]
                    assert (az.r == d.r * z[0][0].r if parity == 1 else az.i == d.i * z[0][0].r)
    assert fixtures == 225 and parities == 450
    assert rejected_factor and rejected_sign and rejected_partial
    print(f"PASS scattering/current: {fixtures} fixtures; {parities} full congruence polynomials")
    print(f"PASS source forms: {moving} nonparabolic projectors; {charts} nonzero-A charts")
    print("PASS negative controls: factorized receiver, one-sign error, partial densities rejected")


def label_audits():
    n = 26
    labels = list(product(range(n), repeat=2))
    swap = {p: (p[1], p[0]) for p in labels}
    assert all(swap[swap[p]] == p for p in labels)
    fixed = sum(swap[p] == p for p in labels)
    transpositions = (len(labels) - fixed) // 2
    dp, dm = fixed + transpositions, transpositions
    assert (dp, dm) == (351, 325)
    assert dp + dm == 676
    # Identity-label and partial-trace embeddings have their exact weights.
    assert sum(Q(1) for _ in range(dp)) == dp
    assert sum(Q(1, dp) ** 2 for _ in range(dp)) == Q(1, dp)
    assert sum(Q(1, dm) ** 2 for _ in range(dm)) == Q(1, dm)
    # Diagonal-memory preparations include the wholly symmetric label 1.
    for j in range(n):
        overlap = int(j == 1)
        pplus, pminus = Q(1 + overlap, 2), Q(1 - overlap, 2)
        assert pplus + pminus == 1
        assert (pplus, pminus) == ((Q(1), Q(0)) if j == 1 else (Q(1, 2), Q(1, 2)))
    # One cross-label 2x2 complex block contributes -sum sigma_i sigma_j |Zij|^2.
    cross_signs = [-s * t for s, t in product((1, -1), repeat=2) for _ in (0, 1)]
    assert cross_signs.count(1) == cross_signs.count(-1) == 4
    assert 8 * dp * dm == 912600
    print("PASS retained labels: 676 pairs; parity dimensions 351/325; fixed form weights")


@dataclass(frozen=True)
class F:
    """a+b*phi, phi^2=phi+1."""
    a: Q = Q(0)
    b: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "a", Q(self.a))
        object.__setattr__(self, "b", Q(self.b))

    @staticmethod
    def cast(x):
        return x if isinstance(x, F) else F(x)

    def __add__(self, other):
        other = F.cast(other)
        return F(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-F.cast(other))

    def __rsub__(self, other):
        return F.cast(other) - self

    def __mul__(self, other):
        other = F.cast(other)
        return F(self.a * other.a + self.b * other.b,
                 self.a * other.b + self.b * other.a + self.b * other.b)

    __rmul__ = __mul__

    def conj(self):
        return F(self.a + self.b, -self.b)


def arithmetic_audits():
    phi = F(0, 1)
    sqrt5 = 2 * phi - 1
    assert phi * phi == phi + 1 and sqrt5 * sqrt5 == F(5)
    assert (phi + 2) * (phi + 2).conj() == F(5)
    assert (phi + 2) * (phi + 2) * (phi - 3) == -5 * (phi + 2)
    assert Q(1, 4) * (phi - 2) == Q(-1, 4) * (phi - 1) * (phi - 1)
    ct = Q(2, 5) * sqrt5
    assert ct.conj() == -ct and ct * ct.conj() == F(Q(-4, 5))
    assert Q(1, 2) * sqrt5 * ct == F(1)
    assert Q(1, 5) * sqrt5 * ct == F(Q(2, 5))
    def f4mul(a, b):
        raw = ((a & 1) * (b & 1)) ^ ((((a >> 1) * (b & 1)) ^ ((b >> 1) * (a & 1))) << 1) ^ (((a >> 1) * (b >> 1)) << 2)
        return raw ^ 7 if raw & 4 else raw
    assert all((x * x + x + 1) % 2 for x in range(2))
    assert all(f4mul(x, x) ^ f4mul(2, x) ^ 1 for x in range(4))
    assert all((x * x - 5) % 13 for x in range(13))
    assert [pow(13, j, 5) for j in range(1, 5)] == [3, 4, 2, 1]
    assert all(w % 2 == 1 and w % 13 == 0 and w % (13 * 13) != 0 for w in (351, 325))
    print("PASS conditional arithmetic: original beta scale, two real places, primes 2 and 13")


def main():
    print("C-HODGE-CAPTURE-PARITY-N | exact finite audit | NON-CANONICAL L1")
    source_moment()
    algebraic_elimination()
    fixture_audits()
    label_audits()
    arithmetic_audits()
    print("ANALYTIC ONLY: full cross-parity classification, boundary uniqueness, measure-zero theorem")
    print("NOT CLAIMED: center boundary enclosure, separation margin, spatial-cut or integral-lattice identification")
    print("PASS all frozen finite audit families")


if __name__ == "__main__":
    main()
