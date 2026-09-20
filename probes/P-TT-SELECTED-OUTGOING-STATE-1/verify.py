#!/usr/bin/env python3
"""Exact bounded audit of the selected isolated TT outgoing-state law.

Runtime authority is this file alone.  No floating point, numerical roots,
external files, random draws or horizon extrapolation are used.  Histories
are audited at m=0,...,10.  Universal claims belong to PROOF.md.

Radical identities are certified in the commutative polynomial quotient
X_q^2=q for positive rational q.  Every identity in that quotient holds
when X_q is the positive real square root.  Algebraic independence of the
roots is NOT asserted, and a nonzero formal polynomial is never used as a
certificate of a nonzero real number.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import isqrt


N = 10
WORDS = ("0010", "0011", "0100", "0101", "0110", "1001",
         "1010", "1011", "1100", "1101")
SIGNS = tuple(product((-1, 1), repeat=2))
WEIGHTS = {w: F(1, 6) if w in ("0110", "1001") else F(1, 12)
           for w in WORDS}
ZERO = (F(0),) * 5
I5 = tuple(tuple(F(i == j) for j in range(5)) for i in range(5))
L = tuple(tuple(F(188 if i == j else -29 if (i-j) % 5 in (1, 4)
                   else -65, 324) for j in range(5)) for i in range(5))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def mv(a, v):
    return tuple(dot(row, v) for row in a)


def outer(a, b):
    return tuple(tuple(x*y for y in b) for x in a)


def transpose(a):
    return tuple(zip(*a))


def mm(a, b):
    return tuple(tuple(dot(row, col) for col in transpose(b)) for row in a)


def madd(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))


def mscale(c, a):
    return tuple(scale(c, row) for row in a)


def rank(a):
    a = [list(map(F, row)) for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][j]
        a[r] = [v/q for v in a[r]]
        for i in range(r+1, len(a)):
            if a[i][j]:
                q = a[i][j]
                a[i] = [x-q*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def evolve(phi, horizon=N):
    h = [ZERO, ZERO]
    for m in range(1, horizon):
        nxt = sub(sub(scale(2, h[m]), mv(L, h[m])), h[m-1])
        h.append(add(nxt, phi) if m == 1 else nxt)
    return tuple(h[:horizon+1])


def source(word):
    bits = tuple(map(int, word))
    u0, u1 = bits[2]-bits[0], bits[3]-bits[1]
    def h(u):
        return tuple(F(int(r == u % 5) + int(r == (u+1) % 5), 2)
                     for r in range(5))
    return sub(h(u1), h(u0))


class Rad:
    """Exact certificates using positive-root symbols; no factoring needed."""
    def __init__(self, value=0):
        if isinstance(value, Rad):
            self.terms = value.terms.copy()
        elif isinstance(value, dict):
            self.terms = {k: F(v) for k, v in value.items() if v}
        else:
            self.terms = {(): F(value)} if value else {}

    def __add__(self, other):
        other = Rad(other)
        d = self.terms.copy()
        for key, value in other.terms.items():
            d[key] = d.get(key, F(0)) + value
        return Rad(d)

    __radd__ = __add__

    def __neg__(self):
        return Rad({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-Rad(other))

    def __mul__(self, other):
        other = Rad(other)
        d = defaultdict(F)
        for ka, ca in self.terms.items():
            for kb, cb in other.terms.items():
                common = set(ka).intersection(kb)
                coefficient = ca*cb
                for q in common:
                    coefficient *= q
                key = tuple(sorted(set(ka).symmetric_difference(kb)))
                d[key] += coefficient
        return Rad(d)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.terms == Rad(other).terms


def root(q):
    q = F(q)
    assert q >= 0
    if not q:
        return Rad()
    a, b = isqrt(q.numerator), isqrt(q.denominator)
    if a*a == q.numerator and b*b == q.denominator:
        return Rad(F(a, b))
    return Rad({(q,): F(1)})


class ComplexRad:
    def __init__(self, re=0, im=0):
        self.re, self.im = Rad(re), Rad(im)

    def __add__(self, other):
        if not isinstance(other, ComplexRad):
            other = ComplexRad(other)
        return ComplexRad(self.re+other.re, self.im+other.im)

    __radd__ = __add__

    def __mul__(self, other):
        if not isinstance(other, ComplexRad):
            other = ComplexRad(other)
        return ComplexRad(self.re*other.re-self.im*other.im,
                          self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def conj(self):
        return ComplexRad(self.re, -self.im)

    def __eq__(self, other):
        if not isinstance(other, ComplexRad):
            other = ComplexRad(other)
        return self.re == other.re and self.im == other.im


def amplitude(h, signs):
    if h > 0:
        return ComplexRad(signs[0]*root(h))
    if h < 0:
        return ComplexRad(0, signs[1]*root(-h))
    return ComplexRad()


def atom_key(h, signs):
    """Literal positive-root coordinate; sign and branch are unambiguous."""
    return tuple((0, 0, F(0)) if q == 0 else
                 (1, signs[0], q) if q > 0 else (2, signs[1], -q)
                 for q in h)


# Q(zeta_5), in basis 1,z,z^2,z^3, with z^4=-1-z-z^2-z^3.
def cyc(value=0):
    if isinstance(value, tuple):
        assert len(value) == 4
        return tuple(map(F, value))
    return (F(value), F(0), F(0), F(0))


def cmul(a, b):
    p = [F(0)]*7
    for i in range(4):
        for j in range(4):
            p[i+j] += a[i]*b[j]
    for i in range(6, 3, -1):
        for j in range(4):
            p[i-4+j] -= p[i]
    return tuple(p[:4])


ZPOW = (cyc(1), cyc((0, 1, 0, 0)), cyc((0, 0, 1, 0)),
        cyc((0, 0, 0, 1)), cyc((-1, -1, -1, -1)))
SQRT5 = cyc((-1, 0, -2, -2))


def cconj(a):
    out = cyc()
    for i, q in enumerate(a):
        out = add(out, scale(q, ZPOW[(-i) % 5]))
    return out


def q5(a=0, b=0):
    return add(cyc(a), scale(F(b), SQRT5))


def q5_pair(x):
    assert x == cconj(x)
    assert x[1] == 0 and x[2] == x[3]
    b = -x[2]/2
    a = x[0]+b
    assert q5(a, b) == x
    return a, b


def q5_positive(x):
    a, b = q5_pair(x)
    if b == 0:
        return a > 0
    if b > 0:
        return a >= 0 or 5*b*b > a*a
    return a > 0 and a*a > 5*b*b


def fourier_unscaled(v, k):
    out = cyc()
    for r, value in enumerate(v):
        out = add(out, scale(value, ZPOW[(k*r) % 5]))
    return out


def fpower(v, k):
    f = fourier_unscaled(v, k)
    return scale(F(1, 5), cmul(f, cconj(f)))


def covariance(vectors):
    d = len(next(iter(vectors.values())))
    mean = tuple(sum((WEIGHTS[w]*vectors[w][i] for w in WORDS), F(0))
                 for i in range(d))
    cov = tuple(tuple(sum((WEIGHTS[w]*vectors[w][i]*vectors[w][j]
                           for w in WORDS), F(0))-mean[i]*mean[j]
                      for j in range(d)) for i in range(d))
    return mean, cov


def spectrum(vectors, k, connected=True):
    mean = tuple(sum((WEIGHTS[w]*vectors[w][i] for w in WORDS), F(0))
                 for i in range(5))
    raw = cyc()
    for w in WORDS:
        raw = add(raw, scale(WEIGHTS[w], fpower(vectors[w], k)))
    return sub(raw, fpower(mean, k)) if connected else raw


def fourier_covariance(cov, k, ell):
    out = cyc()
    for r in range(5):
        for s in range(5):
            out = add(out, scale(cov[r][s]/5, ZPOW[(k*r-ell*s) % 5]))
    return out


def sample_fourier_covariance(vectors, k, ell):
    mean = tuple(sum((WEIGHTS[w]*vectors[w][i] for w in WORDS), F(0))
                 for i in range(5))
    out = cyc()
    for w in WORDS:
        centered = sub(vectors[w], mean)
        fk, fl = fourier_unscaled(centered, k), fourier_unscaled(centered, ell)
        out = add(out, scale(WEIGHTS[w]/5, cmul(fk, cconj(fl))))
    return out


def main():
    # G1: unchanged finite source law and the independent outgoing recurrence.
    assert len(WORDS) == len(set(WORDS)) == 10
    assert all(p > 0 for p in WEIGHTS.values())
    assert sum(WEIGHTS.values(), F(0)) == 1
    assert L == transpose(L) and mv(L, (F(1),)*5) == ZERO
    pi0 = tuple(tuple(F(i == j)-F(1, 5) for j in range(5)) for i in range(5))
    eigen_sum = F(470, 324)
    eigen_product = F(235**2-18**2*5, 324**2)
    annihilator = madd(madd(mm(L, L), mscale(-eigen_sum, L)),
                       mscale(eigen_product, pi0))
    assert annihilator == (ZERO,)*5 and rank(L) == 4
    for eigenvalue in (q5(F(235, 324), F(1, 18)), q5(F(235, 324), F(-1, 18))):
        assert q5_positive(eigenvalue) and q5_positive(sub(cyc(1), eigenvalue))
    phis = {w: source(w) for w in WORDS}
    history = {w: evolve(phis[w]) for w in WORDS}
    static = tuple(w for w in WORDS if phis[w] == ZERO)
    assert static == ("0011", "0101", "1010", "1100")
    d1 = (F(1, 2), F(0), F(-1, 2), F(0), F(0))
    d2 = (F(0), F(-1, 2), F(0), F(0), F(1, 2))
    atoms = {ZERO, d1, scale(-1, d1), d2, scale(-1, d2),
             add(d1, d2), scale(-1, add(d1, d2))}
    assert set(phis.values()) == atoms
    for w in WORDS:
        assert history[w][:2] == (ZERO, ZERO)
        assert history[w][2] == phis[w]
        assert all(sum(h, F(0)) == 0 for h in history[w])
        for m in range(2, N):
            assert history[w][m+1] == sub(sub(scale(2, history[w][m]),
                                                        mv(L, history[w][m])),
                                                    history[w][m-1])
        for n in range(2, N+1):
            assert evolve(phis[w], n) == history[w][:n+1]
    print("G1 PASS: ten positive source weights, seven impulses, four static words; exact m=0..10 histories")

    # G2: atom quotient, restriction consistency and noncollapse after onset.
    flat = {w: tuple(q for h in history[w] for q in h) for w in WORDS}
    labels = [(w, signs, WEIGHTS[w]/4) for w in WORDS for signs in SIGNS]
    assert len(labels) == 40 and sum(p for _, _, p in labels) == 1
    distributions = []
    for n in range(N+1):
        dist = defaultdict(F)
        for w, signs, p in labels:
            dist[atom_key(flat[w][:5*(n+1)], signs)] += p
        assert sum(dist.values(), F(0)) == 1 and all(p > 0 for p in dist.values())
        if n < 2:
            assert len(dist) == 1
        else:
            assert Counter(dist.values()) == {F(1, 3): 1, F(1, 48): 16, F(1, 24): 8}
        if n:
            restricted = defaultdict(F)
            for key, mass in dist.items():
                restricted[key[:-5]] += mass
            assert dict(restricted) == dict(distributions[-1])
        distributions.append(dist)
    basis_histories = [evolve(col) for col in transpose(I5)]
    propagators = []
    for m in range(N+1):
        a = transpose(tuple(h[m] for h in basis_histories))
        propagators.append(a)
        if m >= 2:
            restricted = tuple(tuple(row[j]-row[4] for j in range(4)) for row in a)
            assert rank(restricted) == 4
            assert len({history[w][m] for w in WORDS}) == 7
            dist = defaultdict(F)
            for w, signs, p in labels:
                dist[atom_key(history[w][m], signs)] += p
            assert Counter(dist.values()) == {F(1, 3): 1, F(1, 48): 16, F(1, 24): 8}
    spectral_roots = (q5(F(413, 324), F(1, 18)), q5(F(413, 324), F(-1, 18)))
    trace_root = F(413, 162)
    assert add(*spectral_roots) == cyc(trace_root) and trace_root.denominator != 1
    assert cmul(*spectral_roots) == cyc(F(413**2-18**2*5, 324**2))
    print("G2 PASS: 40 labelled atoms, 25 histories, exact prefix masses; rank-four propagators m=2..10")

    # G3: pointwise square, modulus, spin-two tensor and determinant identities.
    vector = {}
    for w, signs, _ in labels:
        v = tuple(amplitude(q, signs) for q in flat[w])
        vector[w, signs] = v
        for h, a in zip(flat[w], v):
            assert a*a == h
            assert a*a.conj() == abs(h)
            hplus = a.re*a.re-a.im*a.im
            hcross = 2*a.re*a.im
            assert hplus == h and hcross == 0
            determinant = (Rad(1)+hplus)*(Rad(1)-hplus)-hcross*hcross
            assert determinant == 1-h*h
            if h == 0:
                assert a == 0
    print("G3 PASS: positive-root certificates give v^2=h, |v|^2=|h|, zero convention and det=1-h^2")

    # G4: exact K4 orbit and the complete sign-monomial fourth-order rule.
    for w in WORDS:
        states = {atom_key(flat[w], signs) for signs in SIGNS}
        assert len(states) == (1 if w in static else 4)
        if w not in static:
            assert any(q > 0 for q in flat[w]) and any(q < 0 for q in flat[w])
        for signs in SIGNS:
            v = vector[w, signs]
            assert tuple(a.conj() for a in v) == vector[w, (signs[0], -signs[1])]
            assert tuple((-1)*a for a in v) == vector[w, (-signs[0], -signs[1])]
            for q in flat[w]:
                assert ComplexRad(0, 1)*amplitude(-q, signs) == amplitude(q, (-signs[1], signs[0]))
    for exponents in product(range(5), repeat=2):
        exact = sum((F(ep**exponents[0]*em**exponents[1], 4) for ep, em in SIGNS), F(0))
        assert exact == int(all(e % 2 == 0 for e in exponents))
    for branches in product((0, 1), repeat=4):
        for conjugations in product((False, True), repeat=4):
            observed = ComplexRad()
            unsigned = ComplexRad(1)
            for q, branch, conjugate in zip((2, 3, 5, 7), branches, conjugations):
                a = ComplexRad(root(q), 0) if branch == 0 else ComplexRad(0, root(q))
                unsigned = unsigned*(a.conj() if conjugate else a)
            for signs in SIGNS:
                term = ComplexRad(1)
                for q, branch, conjugate in zip((2, 3, 5, 7), branches, conjugations):
                    a = amplitude(F(q if branch == 0 else -q), signs)
                    term = term*(a.conj() if conjugate else a)
                observed = observed+F(1, 4)*term
            even = all(branches.count(j) % 2 == 0 for j in (0, 1))
            assert observed == (unsigned if even else ComplexRad())
    print("G4 PASS: free K4 orbits, frame redescription and all 256 fourth-moment sign/conjugation patterns")

    # G5: second moments and TT fourth contraction at all 55 x 55 point pairs.
    size = 5*(N+1)
    for w in WORDS:
        for i in range(size):
            assert sum((F(1, 4)*vector[w, s][i] for s in SIGNS), ComplexRad()) == 0
    tensor_mean, tensor_cov = covariance(flat)
    assert tensor_mean == (F(0),)*size
    for i in range(size):
        for j in range(size):
            global_pseudo = Rad()
            contraction = F(0)
            for w in WORDS:
                x, y = flat[w][i], flat[w][j]
                same = x*y > 0
                radical = root(abs(x))*root(abs(y)) if same else Rad()
                pseudo = radical if x > 0 else -radical
                c = sum((F(1, 4)*(vector[w, s][i]*vector[w, s][j].conj())
                         for s in SIGNS), ComplexRad())
                p = sum((F(1, 4)*(vector[w, s][i]*vector[w, s][j])
                         for s in SIGNS), ComplexRad())
                assert c == ComplexRad(radical) and p == ComplexRad(pseudo)
                global_pseudo = global_pseudo+WEIGHTS[w]*pseudo
                # G3 has already certified every individual v_i^2=h_i.
                contraction += WEIGHTS[w]*x*y
            assert global_pseudo == 0
            assert contraction == tensor_cov[i][j]
    print("G5 PASS: zero vector mean and global pseudocovariance; second moments and TT fourth contraction on all 55x55 pairs")

    # G6: exact source covariance, eigenvalues and rank-two history covariance.
    mean_phi, cphi = covariance(phis)
    expected_cphi = madd(mscale(F(1, 6), madd(outer(d1, d1), outer(d2, d2))),
                         mscale(F(1, 3), outer(add(d1, d2), add(d1, d2))))
    assert mean_phi == ZERO and cphi == expected_cphi and rank(cphi) == 2
    assert mv(cphi, add(d1, d2)) == scale(F(5, 12), add(d1, d2))
    assert mv(cphi, sub(d1, d2)) == scale(F(1, 12), sub(d1, d2))
    d1hist = tuple(q for h in evolve(d1) for q in h)
    d2hist = tuple(q for h in evolve(d2) for q in h)
    expected_full = madd(mscale(F(1, 6), madd(outer(d1hist, d1hist), outer(d2hist, d2hist))),
                         mscale(F(1, 3), outer(add(d1hist, d2hist), add(d1hist, d2hist))))
    assert tensor_cov == expected_full
    for m in range(2, N+1):
        assert rank(tuple((a, b) for a, b in zip(d1hist[:5*(m+1)], d2hist[:5*(m+1)]))) == 2
        slice_vectors = {w: history[w][m] for w in WORDS}
        _, cov = covariance(slice_vectors)
        assert cov == mm(mm(propagators[m], cphi), transpose(propagators[m]))
        assert rank(cov) == 2
    print("G6 PASS: source eigenvalues 5/12,1/12; complete prefix covariance factorization and rank two")

    # G7: coefficient identity with pi kept as a formal nonzero symbol.
    # lambda=216*pi; original action coefficient 1/(4*lambda).
    # h_can=h/sqrt(2*lambda): (1/2)*h_can^2 has that same coefficient.
    pi_laurent_original = {-1: F(1, 4*216)}
    pi_laurent_canonical = {-1: F(1, 2)*F(1, 2*216)}
    assert pi_laurent_original == pi_laurent_canonical
    # v_can=v/(2*lambda)^(1/4) makes v_can^2=h_can; its fourth
    # contraction scales by 1/(2*lambda), not by a vector Gaussian law.
    for w in WORDS:
        for m in range(N):
            bracket = dot(sub(history[w][m+1], history[w][m]),
                          sub(history[w][m+1], history[w][m]))-dot(history[w][m], mv(L, history[w][m]))
            assert {-1: bracket/(4*216)} == {-1: F(1, 2)*bracket/(2*216)}
    phi = phis["0010"]
    onset_action = dot(phi, phi)/2
    assert onset_action > 0 and 16*onset_action != 4*onset_action
    print("G7 PASS: lambda=216*pi action normalization; quadratic h action is quartic in v, not a selected vector action")

    # G8: connected finite spectra at every audited post-onset slice.
    assert cmul(SQRT5, SQRT5) == cyc(5)
    onset_t = (cyc(), q5(F(1, 8), F(1, 24)), q5(F(1, 8), F(-1, 24)),
               q5(F(1, 8), F(-1, 24)), q5(F(1, 8), F(1, 24)))
    onset_s = (cyc(F(2, 15)), q5(F(7, 240), F(-1, 120)), q5(F(7, 240), F(1, 120)),
               q5(F(7, 240), F(1, 120)), q5(F(7, 240), F(-1, 120)))
    onset_ratio = (cyc(), q5(F(310, 29), F(130, 29)), q5(F(310, 29), F(-130, 29)),
                   q5(F(310, 29), F(-130, 29)), q5(F(310, 29), F(130, 29)))
    all_spectra = {}
    for m in range(N+1):
        hv = {w: history[w][m] for w in WORDS}
        sv = {w: tuple(abs(x) for x in history[w][m]) for w in WORDS}
        mean_h, cov_h = covariance(hv)
        mean_s, cov_s = covariance(sv)
        ts = tuple(spectrum(hv, k) for k in range(5))
        ss = tuple(spectrum(sv, k) for k in range(5))
        all_spectra[m] = ts, ss
        for k in range(5):
            assert ts[k] == fourier_covariance(cov_h, k, k)
            assert ss[k] == fourier_covariance(cov_s, k, k)
            q5_pair(ts[k])
            q5_pair(ss[k])
            if m >= 2:
                assert q5_positive(ss[k])
                assert q5_positive(ts[k]) if k else ts[k] == cyc()
            else:
                assert ts[k] == ss[k] == cyc()  # ZERO_SUPPORT; ratio undefined.
            for ell in range(5):
                assert fourier_covariance(cov_h, k, ell) == sample_fourier_covariance(hv, k, ell)
                assert fourier_covariance(cov_s, k, ell) == sample_fourier_covariance(sv, k, ell)
        if m >= 2:
            assert any(fourier_covariance(cov_h, k, ell) != cyc()
                       for k in range(5) for ell in range(5) if k != ell)
        assert ts[1] == ts[4] and ts[2] == ts[3]
        assert ss[1] == ss[4] and ss[2] == ss[3]
        assert sum((q5_pair(x)[0] for x in ts), F(0)) == sum(cov_h[i][i] for i in range(5))
        assert sum((q5_pair(x)[1] for x in ts), F(0)) == 0
        assert sum((q5_pair(x)[0] for x in ss), F(0)) == sum(cov_s[i][i] for i in range(5))
        assert sum((q5_pair(x)[1] for x in ss), F(0)) == 0
        assert mean_h == ZERO
        if m == 2:
            assert ts == onset_t and ss == onset_s
            assert mean_s == (F(1, 4), F(1, 4), F(1, 4), F(0), F(1, 4))
            a, b = tuple(abs(x) for x in d1), tuple(abs(x) for x in d2)
            expected_cs = madd(mscale(F(1, 6), madd(outer(a, a), outer(b, b))),
                               mscale(F(1, 12), outer(add(a, b), add(a, b))))
            assert cov_s == expected_cs
            for k in range(5):
                assert cmul(onset_ratio[k], ss[k]) == ts[k]
            assert sum(cov_h[i][i] for i in range(5)) == F(1, 2)
            assert sum(cov_s[i][i] for i in range(5)) == F(1, 4)
    print("G8 PASS: full tensor/intensity Fourier covariances m=0..10; onset powers and ratios exact in Q(sqrt5)")

    # G9: persistent signs, unbiasedness, zero pullback and Fourier boundaries.
    w = "0010"
    i = next(i for i, q in enumerate(history[w][2]) if q > 0 and history[w][3][i] > 0)
    x, y = history[w][2][i], history[w][3][i]
    assert x > 0 and y > 0  # positive real root certifies nonzero, not formal inequality.
    persistent = sum((F(1, 4)*(amplitude(x, s)*amplitude(y, s).conj()) for s in SIGNS), ComplexRad())
    fresh = sum((F(1, 16)*(amplitude(x, s)*amplitude(y, t).conj())
                 for s in SIGNS for t in SIGNS), ComplexRad())
    assert persistent == ComplexRad(root(x)*root(y)) and fresh == 0
    biased = {(1, 1): F(3, 8), (1, -1): F(3, 8),
              (-1, 1): F(1, 8), (-1, -1): F(1, 8)}
    assert sum(biased.values(), F(0)) == 1
    assert sum((p*s[0] for s, p in biased.items()), F(0)) == F(1, 2)
    assert biased[1, 1] != biased[-1, -1]
    assert sum((p*amplitude(x, s) for s, p in biased.items()), ComplexRad()) == ComplexRad(root(x)*F(1, 2))
    # d(v^2)=2v dv vanishes at v=0, while the independently imposed h impulse is nonzero.
    assert amplitude(F(0), (1, 1)) == 0 and phis[w] != ZERO
    assert all(2*F(0)*x == 0 for x in phis[w])
    # At onset k=0, Fh is zero but Fv is not: each root branch has positive sum.
    h = history[w][2]
    positive_count, negative_count = sum(q > 0 for q in h), sum(q < 0 for q in h)
    assert positive_count == negative_count == 1
    v_sum = sum((amplitude(q, (1, 1)) for q in h), ComplexRad())
    assert v_sum*v_sum.conj() == 1
    assert fourier_unscaled(h, 0) == cyc()
    assert F(1, 5) > 0  # |Fv(0)|^2 = 1/5, whereas Fh(0)=0.
    s_onset = {w: tuple(abs(x) for x in history[w][2]) for w in WORDS}
    assert spectrum(s_onset, 0, connected=False) == cyc(F(1, 3))
    assert spectrum(s_onset, 0) == cyc(F(2, 15))
    print("G9 PASS: fresh signs, biased signs, singular zero pullback, Fourier-before-square and raw intensity are distinct")

    # G10: actual distribution is non-Gaussian; no hidden division by silent atoms.
    # At onset site 0: E|v|^2=1/4, E|v|^4=1/8, so this one site alone
    # happens to satisfy the proper-Gaussian diagonal relation.  Use instead
    # a genuine nonzero off-diagonal fourth test at sites 0 and 2.
    # The nonzero silent-history atom (mass 1/3) already excludes every
    # nondegenerate Gaussian law on the active two-dimensional field image.
    assert distributions[N][atom_key((F(0),)*size, (1, 1))] == F(1, 3)
    assert rank(cphi) == 2
    # Direct Wick counterexample: h_2(0) and h_2(2) are exact negatives;
    # E[v(0)^2 conjugate(v(2))^2]=-1/8, but C(0,2)=P(0,2)=0.
    a, b = 0, 2
    tt = sum((WEIGHTS[w]*history[w][2][a]*history[w][2][b] for w in WORDS), F(0))
    c = ComplexRad()
    p = ComplexRad()
    for w, signs, mass in labels:
        va, vb = amplitude(history[w][2][a], signs), amplitude(history[w][2][b], signs)
        c = c+mass*(va*vb.conj())
        p = p+mass*(va*vb)
    assert tt == F(-1, 8) and c == 0 and p == 0
    assert tt != 0  # Proper-Gaussian Wick predicts 2*C(a,b)^2=0 here.
    assert all_spectra[0] == all_spectra[1] == ((cyc(),)*5, (cyc(),)*5)
    print("G10 PASS: explicit non-Gaussian fourth-moment witness; silent mass 1/3 retained; pre-onset ratios undefined")
    print("VERDICT: SELECTED-OUTGOING-STATE; conditional L1 law, persistent sign lift and intensity comparison adopted")


if __name__ == "__main__":
    main()
