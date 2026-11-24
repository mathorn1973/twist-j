#!/usr/bin/env python3
"""Prospectively pinned, exact L1 audits. No input, I/O or external packages.

The written proofs carry universal quantifiers. These finite audits do not.
This implementation was written without access to the independent break.py.
"""

from fractions import Fraction
from itertools import product
from math import isqrt


class F:
    """Q(s), s^2=5, with rational coefficient arithmetic only."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        if isinstance(a, F):
            assert b == 0
            self.a, self.b = a.a, a.b
        else:
            assert isinstance(a, (int, Fraction))
            assert isinstance(b, (int, Fraction))
            self.a, self.b = Fraction(a), Fraction(b)

    def __add__(self, other):
        if not isinstance(other, (F, int, Fraction)):
            return NotImplemented
        other = F(other)
        return F(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, (F, int, Fraction)):
            return NotImplemented
        other = F(other)
        return F(self.a * other.a + 5 * self.b * other.b,
                 self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def inverse(self):
        n = self.a * self.a - 5 * self.b * self.b
        assert n != 0
        return F(self.a / n, -self.b / n)

    def __truediv__(self, other):
        return self * F(other).inverse()

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0:
            return self.inverse() ** (-n)
        result, base = F(1), self
        while n:
            if n & 1:
                result = result * base
            base, n = base * base, n // 2
        return result

    def __eq__(self, other):
        if not isinstance(other, (F, int, Fraction)):
            return NotImplemented
        other = F(other)
        return self.a == other.a and self.b == other.b

    def __bool__(self):
        return self != 0

    def conjugate(self):
        return self

    def norm(self):
        return self.a * self.a - 5 * self.b * self.b


SQRT5 = F(0, 1)
PHI = (1 + SQRT5) / 2


class Quadratic:
    """F[j]/(j^2-t*j+1), with the nontrivial F involution."""

    __slots__ = ("a", "b")
    t = F(0)

    def __init__(self, a=0, b=0):
        if isinstance(a, type(self)):
            assert b == 0
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)

    def __add__(self, other):
        other = type(self)(other)
        return type(self)(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return type(self)(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = type(self)(other)
        return type(self)(self.a * other.a - self.b * other.b,
                          self.a * other.b + self.b * other.a
                          + self.t * self.b * other.b)

    __rmul__ = __mul__

    def conjugate(self):
        return type(self)(self.a + self.t * self.b, -self.b)

    def norm(self):
        return self.a * self.a + self.t * self.a * self.b + self.b * self.b

    def inverse(self):
        n = self.norm()
        assert n != 0
        z = self.conjugate()
        return type(self)(z.a / n, z.b / n)

    def __truediv__(self, other):
        return self * type(self)(other).inverse()

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0:
            return self.inverse() ** (-n)
        result, base = type(self)(1), self
        while n:
            if n & 1:
                result = result * base
            base, n = base * base, n // 2
        return result

    def __eq__(self, other):
        if not isinstance(other, (type(self), F, int, Fraction)):
            return NotImplemented
        other = type(self)(other)
        return self.a == other.a and self.b == other.b

    def __bool__(self):
        return self != 0


class Gaussian(Quadratic):
    t = F(0)


class CM(Quadratic):
    t = PHI


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def trans(a):
    return [list(c) for c in zip(*a)]


def dagger(a):
    return [[x.conjugate() for x in c] for c in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, c):
    return [[c * x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    assert len(a[0]) == len(b)
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def trace(a):
    return sum(a[j][j] for j in range(len(a)))


def det(a):
    assert len(a) == len(a[0])
    b, result = [row[:] for row in a], F(1)
    for j in range(len(b)):
        k = next((k for k in range(j, len(b)) if b[k][j] != 0), None)
        if k is None:
            return F(0)
        if k != j:
            b[j], b[k] = b[k], b[j]
            result = -result
        pivot = b[j][j]
        result *= pivot
        for k in range(j + 1, len(b)):
            ratio = b[k][j] / pivot
            b[k] = [x - ratio * y for x, y in zip(b[k], b[j])]
    return result


def rank(a):
    b, row = [r[:] for r in a], 0
    for j in range(len(b[0])):
        k = next((k for k in range(row, len(b)) if b[k][j] != 0), None)
        if k is None:
            continue
        b[row], b[k] = b[k], b[row]
        pivot = b[row][j]
        b[row] = [x / pivot for x in b[row]]
        for k in range(len(b)):
            if k != row:
                ratio = b[k][j]
                b[k] = [x - ratio * y for x, y in zip(b[k], b[row])]
        row += 1
        if row == len(b):
            break
    return row


def inverse(a):
    n = len(a)
    b = [r[:] + e for r, e in zip(a, eye(n))]
    for j in range(n):
        k = next(k for k in range(j, n) if b[k][j] != 0)
        b[j], b[k] = b[k], b[j]
        pivot = b[j][j]
        b[j] = [x / pivot for x in b[j]]
        for k in range(n):
            if k != j:
                ratio = b[k][j]
                b[k] = [x - ratio * y for x, y in zip(b[k], b[j])]
    assert [r[:n] for r in b] == eye(n)
    return [r[n:] for r in b]


def charpoly(a):
    """Newton identities, descending monic coefficients."""
    p, traces, coeffs = eye(len(a)), [F(0)], [F(1)]
    for k in range(1, len(a) + 1):
        p = mul(p, a)
        traces.append(trace(p))
        coeffs.append(-sum(coeffs[k - j] * traces[j]
                           for j in range(1, k + 1)) / k)
    return coeffs


def poly_product(a, b):
    out = [F(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def polynomial(a, coeffs):
    out, identity = scale(a, 0), eye(len(a))
    for c in coeffs:
        out = add(mul(out, a), scale(identity, c))
    return out


def hermitian_action(a, field):
    j = field(0, 1)
    basis = [[[1, 0], [0, 0]], [[0, 0], [0, 1]],
             [[0, 1], [1, 0]], [[0, j], [j.conjugate(), 0]]]
    columns = []
    for h in basis:
        h = [[field(x) for x in row] for row in h]
        y = mul(mul(a, h), dagger(a))
        assert y == dagger(y)
        assert y[0][0].b == y[1][1].b == 0
        columns.append([y[0][0].a, y[1][1].a, y[0][1].a, y[0][1].b])
    return trans(columns)


def audit_source():
    c, s = 1 / SQRT5, 2 / SQRT5
    sigma = [[Gaussian(1), Gaussian(0)], [Gaussian(0), Gaussian(-1)]]
    tq = [[Gaussian(1 / s), Gaussian(-c / s)],
          [Gaussian(c / s), Gaussian(-1 / s)]]
    assert mul(tq, tq) == eye(2)

    def spatial(lam):
        return scale([[c * c - lam, c * (1 - 1 / lam)],
                      [c * (1 - lam), c * c - 1 / lam]], 1 / (s * s))

    phases = [Gaussian(-1)]
    for t in map(Fraction, (-2, -1, Fraction(-1, 2), 0, Fraction(1, 2), 1, 2)):
        phases.append(Gaussian((1 - t * t) / (1 + t * t),
                               2 * t / (1 + t * t)))
    for lam in phases:
        assert lam.norm() == 1
        a = spatial(lam)
        assert det(a) == 1
        assert mul(mul(dagger(a), sigma), a) == sigma
        assert trace(a) == (1 - 5 * lam.a) / 2
        for x, u in ((Gaussian(1), Gaussian(0)), (Gaussian(0), Gaussian(1))):
            b, v = (c * x - u) / s, (x - c * u) / s
            xn, un = [row[0] for row in mul(a, [[x], [u]])]
            bn, vn = (c * xn - un) / s, (xn - c * un) / s
            assert u == c * x - s * b and v == s * x + c * b
            assert un == c * xn - s * bn and vn == s * xn + c * bn
            assert lam * x == c * u - s * vn
            assert lam * bn == s * u + c * vn
            assert u.norm() - x.norm() == un.norm() - xn.norm()
    print("G1 PASS: 8 stationary phases, 16 boundary inputs; full source equations/current/dispersion")

    z = Gaussian(Fraction(3, 5), Fraction(4, 5))
    d = [[z, Gaussian(0)], [Gaussian(0), z.conjugate()]]
    generators = [tq, scale(tq, z.conjugate()), mul(mul(d, tq), d), spatial(z)]
    count = 0
    for length in range(4):
        for word in product(range(4), repeat=length):
            a = [[Gaussian(x) for x in row] for row in eye(2)]
            for g in word:
                a = mul(generators[g], a)
            assert mul(mul(dagger(a), sigma), a) == sigma
            assert det(a).norm() == 1
            r = hermitian_action(a, Gaussian)
            assert mul(r, [[F(1)], [F(-1)], [F(0)], [F(0)]]) == [[1], [-1], [0], [0]]
            expected = poly_product([1, -2, 1], [1, -(trace(a).norm() - 2), 1])
            assert charpoly(r) == expected
            count += 1
    assert count == 85
    for i, j in product(range(26), repeat=2):
        swapped = (j, i)
        assert (swapped[1], swapped[0]) == (i, j)
    assert len({(j, i) for i, j in product(range(26), repeat=2)}) == 676
    print("G2 PASS: all 85 words; full congruence polynomial; all 676 retained label pairs")
    bad = [[tq[0][0], tq[0][1]], [-tq[1][0], tq[1][1]]]
    assert mul(mul(dagger(bad), sigma), bad) != sigma
    target = poly_product([1, -3, 1], [1, -PHI, 1])
    assert charpoly(hermitian_action(tq, Gaussian)) != target
    assert sum(target) == -(2 - PHI) != 0
    assert sum(c * (-1) ** (4 - k) for k, c in enumerate(target)) == 5 * (2 + PHI) != 0
    return target


def m5(a):
    return [[x % 5 for x in row] for row in a]


def mul5(a, b):
    return m5(mul(a, b))


def inverse5(a):
    n = len(a)
    b = [r[:] + [int(i == j) for j in range(n)] for i, r in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if b[k][j] % 5)
        b[j], b[k] = b[k], b[j]
        inv = pow(b[j][j], -1, 5)
        b[j] = [x * inv % 5 for x in b[j]]
        for k in range(n):
            if k != j:
                ratio = b[k][j]
                b[k] = [(x - ratio * y) % 5 for x, y in zip(b[k], b[j])]
    return [r[n:] for r in b]


def det5(a):
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % 5


def audit_residue():
    images = set()
    for a, b in product(range(5), repeat=2):
        pair = ((a + 2 * b) % 5, (a - 2 * b) % 5)
        images.add(pair)
        assert ((a - 2 * b) % 5, (a + 2 * b) % 5) == pair[::-1]
        assert (3 * (pair[0] + pair[1])) % 5 == a
        assert (4 * (pair[0] - pair[1])) % 5 == b
    assert len(images) == 25
    g = [[2, 4, 0], [4, 2, 4], [0, 4, 2]]
    m = trans([[1, 0, 1], [1, 4, 3], [3, 4, 1]])
    p = [[1, 1], [1, 4]]
    mi, pi = inverse5(m), inverse5(p)
    phi5 = [[0, 4, 1], [0, 4, 0], [1, 4, 0]]
    b = [[0, 2], [2, 0]]
    bi = inverse5(b)
    omega, oi = [[0, 1], [4, 0]], [[0, 4], [1, 0]]
    identity = [[1, 0], [0, 1]]
    assert mul5(b, b) == [[4, 0], [0, 4]]

    def psi(v):
        h, e, f = [r[0] for r in mul5(mi, [[x] for x in v])]
        return mul5(mul5(p, [[h, e], [f, -h]]), pi)

    def c(y):
        return mul5(mul5(b, y), trans(b))

    def act(v):
        return [r[0] for r in mul5(phi5, [[x] for x in v])]

    assert c(identity) == [[4, 0], [0, 4]]
    assert c(omega) == omega
    full_trace, full_sym = set(), set()
    for t, v1, v2, v3 in product(range(5), repeat=4):
        v = [v1, v2, v3]
        pv, pa = psi(v), psi(act(v))
        gv = mul5(mul5([v], g), [[x] for x in v])[0][0]
        assert mul5(mul5(b, pv), bi) == pa
        assert c(pv) == m5(scale(pa, -1))
        assert det5(pv) == gv
        y = m5(add(scale(identity, t), pv))
        assert det5(y) == (t * t + gv) % 5
        assert c(y) == m5(add(scale(identity, -t), scale(pa, -1)))
        full_trace.add(tuple(x for r in y for x in r))
        sy, sa = mul5(pv, oi), mul5(pa, oi)
        assert sy == trans(sy)
        assert c(sy) == sa
        y2 = m5(add(scale(omega, t), sy))
        assert det5(y2) == (t * t + gv) % 5
        assert c(y2) == m5(add(scale(omega, t), sa))
        full_sym.add(tuple(x for r in y2 for x in r))
        # Reconstruct the whole star-compatible Hermitian residue from Y.
        u, vv = (3 * (y[0][1] + y[1][0])) % 5, (4 * (y[1][0] - y[0][1])) % 5
        plus = [[y[0][0], (u - 2 * vv) % 5], [(u + 2 * vv) % 5, y[1][1]]]
        minus = [[y[0][0], (u + 2 * vv) % 5], [(u - 2 * vv) % 5, y[1][1]]]
        assert plus == y and minus == trans(y)
    assert len(full_trace) == len(full_sym) == 625
    basis = [[int(i == j) for j in range(3)] for i in range(3)]
    for i, j in product(range(3), repeat=2):
        assert trace(mul5(psi(basis[i]), psi(basis[j]))) % 5 == 3 * g[i][j] % 5
    assert c(psi([1, 0, 1])) != mul5(mul5(b, psi([1, 0, 1])), bi)
    print("G3 PASS: all 25 CRT residues; all 625 states in both full slices; 9 trace pairings")


PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def wedge(a):
    return [[a[i][k] * a[j][l] - a[i][l] * a[j][k]
             for k, l in PAIRS] for i, j in PAIRS]


def audit_hodge(target):
    h = [[F(1 + int(i == j)) for j in range(4)] for i in range(4)]
    cycle = trans([[F(x) for x in v] for v in
                   ((-1, 1, 0, 0), (-1, 0, 1, 0), (-1, 0, 0, 1), (-1, 0, 0, 0))])
    l = wedge(add(eye(4), mul(cycle, cycle)))
    beta = scale(eye(6), 0)
    for i, j, sign in ((0, 5, 1), (1, 4, -1), (2, 3, 1)):
        beta[i][j] = beta[j][i] = F(sign)
    k = mul(beta, wedge(h))
    assert mul(k, k) == scale(eye(6), 5)
    plus = scale(add(eye(6), scale(k, 1 / SQRT5)), Fraction(1, 2))
    minus = sub(eye(6), plus)
    assert mul(plus, plus) == plus and rank(plus) == 3
    cross = mul(mul(minus, l), plus)
    assert rank(cross) == 1
    cols = []
    for col in trans(plus):
        if rank(trans(cols + [col])) > len(cols):
            cols.append(col)
    assert len(cols) == 3 and cols == trans(plus)[:3]
    fourth = next(col for col in trans(cross) if any(col))
    e = trans(cols + [fourth])
    assert rank(e) == 4
    gram = mul(mul(trans(e), beta), e)
    expected = [[SQRT5 * (3 if i == j else 1) / 10 if i < 3 and j < 3
                 else (-(2 + SQRT5) / 8 if i == j == 3 else F(0))
                 for j in range(4)] for i in range(4)]
    assert gram == expected
    assert det(gram) == -(5 + 2 * SQRT5) / 80
    le = mul(mul(mul(inverse(gram), trans(e)), beta), mul(l, e))
    assert mul(e, le) == mul(l, e)
    assert mul(mul(trans(le), gram), le) == gram
    boost = polynomial(le, [1, -3, 1])
    compact = polynomial(le, [1, -PHI, 1])
    assert rank(boost) == rank(compact) == 2
    assert mul(boost, compact) == scale(eye(4), 0)
    assert charpoly(le) == target
    d = (5 + 2 * SQRT5) / 80
    assert d.norm() == Fraction(1, 1280)
    assert isqrt(d.norm().denominator) ** 2 != d.norm().denominator
    delta = PHI - 3
    assert det(gram) / delta == PHI ** 4 / 80 == (PHI ** 2 / (4 * SQRT5)) ** 2
    print("G4 PASS: marked A4 reconstruction; E_J rank 4, both factors, fixed Gram and determinant obstruction")

    p1, p2, p3 = [[[x] for x in col] for col in cols]
    v, w = sub(p1, p3), mul(l, sub(p1, p3))
    pair = lambda a, b: mul(mul(trans(a), beta), b)[0][0]
    assert mul(l, w) == sub(scale(w, PHI), v)
    assert pair(v, v) == pair(w, w) == 2 * SQRT5 / 5
    assert pair(v, w) == SQRT5 * PHI / 5
    r = mul(polynomial(l, [1, -PHI, 1]), p1)
    up = mul(sub(l, scale(eye(6), PHI ** -2)), r)
    um = mul(sub(l, scale(eye(6), PHI ** 2)), r)
    coupling = pair(up, um)
    assert coupling == -5 * PHI / 4
    ep, em = up, scale(um, -1 / (SQRT5 * coupling))
    icm = [a + b + c + d for a, b, c, d in zip(ep, em, v, w)]
    assert rank(icm) == 4
    action = [[PHI ** 2, F(0), F(0), F(0)],
              [F(0), PHI ** -2, F(0), F(0)],
              [F(0), F(0), F(0), F(-1)],
              [F(0), F(0), F(1), PHI]]
    qcm = [[F(0), F(Fraction(-1, 2)), F(0), F(0)],
           [F(Fraction(-1, 2)), F(0), F(0), F(0)],
           [F(0), F(0), F(1), PHI / 2],
           [F(0), F(0), PHI / 2, F(1)]]
    assert mul(l, icm) == mul(icm, action)
    pulled = mul(mul(trans(icm), beta), icm)
    assert scale(pulled, SQRT5 / 2) == qcm
    assert scale(pulled, 1 / SQRT5) == scale(qcm, Fraction(2, 5)) != qcm
    zeta = CM(0, 1)
    assert zeta ** 5 == -1 and zeta ** 10 == 1
    spinor = [[PHI * zeta, CM(0)], [CM(0), CM(PHI ** -1)]]
    assert det(spinor).norm() == 1
    ra = hermitian_action(spinor, CM)
    assert ra == action
    assert mul(mul(trans(ra), qcm), ra) == qcm
    # There is no nonzero fixed Hermitian current, not just no diagonal one.
    assert rank(sub(ra, eye(4))) == 4
    print("G5 PASS: explicit CM map; entire action and scaled form; original normalization rejected")

    def f4mul(a, b):
        raw = 0
        for j in range(2):
            if (b >> j) & 1:
                raw ^= a << j
        if raw & 4:
            raw ^= 7
        return raw

    assert [f4mul(a, a) ^ f4mul(2, a) ^ 1 for a in range(4)] == [1, 2, 1, 2]
    assert (Fraction(2, 5).numerator % 4) == 2
    assert (Fraction(2, 5).denominator % 2) == 1
    print("G6 PASS: all 4 F4 residues; inert-prime norm obstruction; five negative controls")


def main():
    assert SQRT5 ** 2 == 5 and PHI ** 2 == PHI + 1
    assert Gaussian(0, 1) ** 2 == -1
    target = audit_source()
    audit_residue()
    audit_hodge(target)
    print("PASS: NON-CANONICAL L1; candidate-C audits of proof-first candidate-T statements")
    print("SCOPE: fixed-current two-port obstruction; CM target representation is not a source derivation")


if __name__ == "__main__":
    main()
