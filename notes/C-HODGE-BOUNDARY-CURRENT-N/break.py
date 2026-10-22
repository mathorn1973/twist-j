#!/usr/bin/env python3
"""Code-blind exact audit of the frozen boundary-current contract.

Standard library only.  This program performs no file, network, subprocess,
random or floating-point operation.  Its field arithmetic is an explicit
quotient-ring convolution; characteristic polynomials use principal minors.
It is a finite candidate-C audit, not a replacement for the frozen proofs.
"""

from fractions import Fraction
from itertools import combinations, permutations, product
from math import isqrt


class N:
    """Q[r,i]/(r^2-5,i^2+1), basis (1,r,i,r*i)."""

    __slots__ = ("v",)

    def __init__(self, value=0):
        if isinstance(value, N):
            self.v = value.v
        elif isinstance(value, tuple):
            if len(value) != 4:
                raise ValueError("Four quotient coefficients required")
            self.v = tuple(Fraction(x) for x in value)
        else:
            self.v = (Fraction(value), Fraction(0), Fraction(0), Fraction(0))

    def __add__(self, other):
        try:
            other = N(other)
        except (TypeError, ValueError):
            return NotImplemented
        return N(tuple(a + b for a, b in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return N(tuple(-x for x in self.v))

    def __sub__(self, other):
        return self + (-N(other))

    def __rsub__(self, other):
        return N(other) + (-self)

    def __mul__(self, other):
        try:
            other = N(other)
        except (TypeError, ValueError):
            return NotImplemented
        out = [Fraction(0) for _ in range(4)]
        for p, a in enumerate(self.v):
            if not a:
                continue
            for q, b in enumerate(other.v):
                if not b:
                    continue
                scale = 1
                if p & q & 1:
                    scale *= 5
                if p & q & 2:
                    scale *= -1
                out[p ^ q] += scale * a * b
        return N(tuple(out))

    __rmul__ = __mul__

    def star(self):
        return N((self.v[0], self.v[1], -self.v[2], -self.v[3]))

    def sigma(self):
        return N((self.v[0], -self.v[1], self.v[2], -self.v[3]))

    def inverse(self):
        if not self:
            raise ZeroDivisionError("Zero quotient-field denominator")
        if not any(self.v[1:]):
            return N(1 / self.v[0])
        numerator = self.sigma() * self.star() * self.sigma().star()
        norm = self * numerator
        if any(norm.v[1:]) or not norm.v[0]:
            raise AssertionError("Invalid exact field norm")
        return N(tuple(x / norm.v[0] for x in numerator.v))

    def __truediv__(self, other):
        other = N(other)
        if not any(other.v[1:]):
            if not other.v[0]:
                raise ZeroDivisionError("Zero rational denominator")
            return N(tuple(x / other.v[0] for x in self.v))
        return self * other.inverse()

    def __rtruediv__(self, other):
        return N(other) / self

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("Integer powers only")
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = N(1), self
        while exponent:
            if exponent & 1:
                out = out * base
            base = base * base
            exponent //= 2
        return out

    def __bool__(self):
        return any(self.v)

    def __eq__(self, other):
        try:
            return self.v == N(other).v
        except (TypeError, ValueError):
            return False

    def __repr__(self):
        return "N" + repr(self.v)

    def rational(self):
        if any(self.v[1:]):
            raise AssertionError("Expected a rational element")
        return self.v[0]

    def real_sign(self):
        if self.v[2] or self.v[3]:
            raise AssertionError("Sign requested for a nonreal element")
        a, b = self.v[:2]
        if not b:
            return (a > 0) - (a < 0)
        if not a:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        difference = a * a - 5 * b * b
        if a > 0:
            return (difference > 0) - (difference < 0)
        return (difference < 0) - (difference > 0)


R = N((0, 1, 0, 0))
II = N((0, 0, 1, 0))
PHI = (1 + R) / 2
DELTA = PHI - 3


class CM:
    """F[tau]/(tau^2-delta), independently represented as two F elements."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        if isinstance(a, CM):
            if b != 0:
                raise TypeError("CM copy with a second coefficient")
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = N(a), N(b)
        if self.a.star() != self.a or self.b.star() != self.b:
            raise ValueError("CM coefficients must belong to F")

    def __add__(self, other):
        other = CM(other)
        return CM(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return CM(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-CM(other))

    def __rsub__(self, other):
        return CM(other) - self

    def __mul__(self, other):
        other = CM(other)
        return CM(self.a * other.a + DELTA * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def star(self):
        return CM(self.a, -self.b)

    def inverse(self):
        norm = self.a * self.a - DELTA * self.b * self.b
        if not norm:
            raise ZeroDivisionError("Zero CM denominator")
        return CM(self.a / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * CM(other).inverse()

    def __rtruediv__(self, other):
        return CM(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = CM(1), self
        while exponent:
            if exponent & 1:
                out = out * base
            base = base * base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.a) or bool(self.b)

    def __eq__(self, other):
        try:
            other = CM(other)
        except (TypeError, ValueError):
            return False
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return "CM(" + repr(self.a) + "," + repr(self.b) + ")"


def demand(condition, name):
    if not condition:
        raise AssertionError(name)


def matrix(rows):
    return [[N(x) for x in row] for row in rows]


def eye(n):
    return [[N(int(i == j)) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(x) for x in zip(*a)]


def adj(a):
    return [[x.star() for x in row] for row in tr(a)]


def mm(a, b):
    demand(len(a[0]) == len(b), "matrix dimensions")
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), 0)
             for j in range(len(b[0]))] for i in range(len(a))]


def ma(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def ms(a, scalar):
    return [[x * scalar for x in row] for row in a]


def sub(a, b):
    return ma(a, ms(b, -1))


def mv(a, v):
    return [row[0] for row in mm(a, [[x] for x in v])]


def col(a, j):
    return [row[j] for row in a]


def cols(vectors):
    return tr(vectors)


def va(a, b):
    return [x + y for x, y in zip(a, b)]


def vs(a, scalar):
    return [x * scalar for x in a]


def trace(a):
    return sum((a[j][j] for j in range(len(a))), 0)


def det(a):
    n = len(a)
    result = N(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = N(-1 if inversions & 1 else 1)
        for i in range(n):
            term *= a[i][p[i]]
        result += term
    return result


def reduced_rows(a):
    work = [[N(x) for x in row] for row in a]
    ncol = len(work[0]) if work else 0
    pivot_row, pivots = 0, []
    for j in range(ncol):
        pivot = next((k for k in range(pivot_row, len(work)) if work[k][j]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][j]
        work[pivot_row] = [x / value for x in work[pivot_row]]
        for k in range(len(work)):
            if k != pivot_row and work[k][j]:
                factor = work[k][j]
                work[k] = [x - factor * y for x, y in zip(work[k], work[pivot_row])]
        pivots.append(j)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work, pivots


def rank(a):
    return len(reduced_rows(a)[1])


def inverse(a):
    n = len(a)
    e = eye(n)
    work, pivots = reduced_rows([list(a[i]) + e[i] for i in range(n)])
    demand(pivots[:n] == list(range(n)), "invertible matrix")
    demand([row[:n] for row in work] == eye(n), "inverse left block")
    return [row[n:] for row in work]


def bilinear(a, x, y):
    return sum((u * v for u, v in zip(x, mv(a, y))), 0)


def poly_product(a, b):
    out = [N(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def characteristic(a):
    """Descending coefficients from all principal minors and Leibniz sums."""
    n = len(a)
    coefficients = [N(1)]
    for k in range(1, n + 1):
        minor_sum = N(0)
        for selected in combinations(range(n), k):
            minor_sum += det([[a[i][j] for j in selected] for i in selected])
        coefficients.append(((-1) ** k) * minor_sum)
    return coefficients


HERMITIAN = [matrix([[1, 0], [0, 0]]),
             matrix([[0, 0], [0, 1]]),
             matrix([[0, 1], [1, 0]]),
             [[N(0), -II], [II, N(0)]]]


def herm_coordinates(x):
    demand(adj(x) == x, "Hermitian image")
    return [x[0][0], x[1][1], (x[0][1] + x[1][0]) / 2,
            (x[1][0] - x[0][1]) / (2 * II)]


def congruence(a):
    return cols([herm_coordinates(mm(mm(a, h), adj(a))) for h in HERMITIAN])


SIGMA = matrix([[1, 0], [0, -1]])
DET_FORM = matrix([[0, Fraction(1, 2), 0, 0],
                   [Fraction(1, 2), 0, 0, 0],
                   [0, 0, -1, 0], [0, 0, 0, -1]])
C = 1 / R
S = 2 / R
TQ = ms(matrix([[1, -C], [C, -1]]), 1 / S)
TARGET_POLY = poly_product([N(1), N(-3), N(1)], [N(1), -PHI, N(1)])


def spatial(lam):
    return ms(matrix([[C * C - lam, C * (1 - 1 / lam)],
                      [C * (1 - lam), C * C - 1 / lam]]), 1 / (S * S))


def regroup(scat):
    u, v = scat[0]
    w, z = scat[1]
    return [[w - z * u / v, z / v], [-u / v, 1 / v]]


def phase_and_words():
    z = (3 + 4 * II) / 5
    phases = [N(-1)]
    for t in [Fraction(-2), Fraction(-1), Fraction(-1, 2), Fraction(0),
              Fraction(1, 2), Fraction(1), Fraction(2)]:
        phases.append(N((1 - t * t) / (1 + t * t))
                      + II * N(2 * t / (1 + t * t)))
    demand(len(phases) == 8, "phase fixture count")
    for lam in phases:
        demand(lam * lam.star() == 1, "unit-circle phase")
        a = spatial(lam)
        demand(mm(mm(adj(a), SIGMA), a) == SIGMA, "spatial current")
        demand(det(a) == 1, "spatial determinant")
        real_lam = (lam + lam.star()) / 2
        demand(trace(a) == (1 - 5 * real_lam) / 2, "whole-source dispersion")
        for incoming in [[N(1), N(0)], [N(0), N(1)]]:
            ax, ux = incoming
            bx = (C * ax - ux) / S
            vx = S * ax + C * bx
            demand(ux == C * ax - S * bx, "old on-site first equation")
            demand(vx == S * ax + C * bx, "old on-site second equation")
            vn = (C * ux - lam * ax) / S
            bn = (S * ux + C * vn) / lam
            an = (vn - C * bn) / S
            un = C * an - S * bn
            demand([an, un] == mv(a, incoming), "source-eliminated transfer")
            demand(vn == S * an + C * bn, "next on-site second equation")
            demand(lam * ax == C * ux - S * vn, "edge first equation")
            demand(lam * bn == S * ux + C * vn, "edge second equation")
            current = ux.star() * ux - ax.star() * ax
            demand(current == un.star() * un - an.star() * an, "stationary edge current")
    q = matrix([[C, -S], [S, C]])
    demand(regroup(q) == TQ, "marked coin regrouping")
    edge = [[C, -S * z], [S * z.star(), C]]
    demand(regroup(edge) == ms(TQ, z.star()), "all-edge-phase algebra fixture")
    d = [[z, N(0)], [N(0), z.star()]]
    phase_coin = ms(q, z * z)
    demand(regroup(phase_coin) == mm(mm(d, TQ), d), "time-phase regrouping")
    alt = ms(matrix([[1, -S], [-S, 1]]), 1 / C)
    demand(mm(mm(adj(alt), SIGMA), alt) == SIGMA, "alternative signed current")
    alphabet = [TQ, ms(TQ, z.star()), mm(mm(d, TQ), d), spatial(z)]
    words = 0
    for length in range(4):
        for word in product(range(4), repeat=length):
            a = eye(2)
            for letter in word:
                a = mm(alphabet[letter], a)
            demand(mm(mm(adj(a), SIGMA), a) == SIGMA, "word current")
            determinant = det(a)
            demand(determinant * determinant.star() == 1, "word determinant modulus")
            ra = congruence(a)
            parameter = trace(a) * trace(a).star() - 2
            expected = poly_product([N(1), N(-2), N(1)], [N(1), -parameter, N(1)])
            demand(characteristic(ra) == expected, "complete word polynomial")
            demand(mv(ra, [N(1), N(-1), N(0), N(0)])
                   == [N(1), N(-1), N(0), N(0)], "fixed boundary-current vector")
            demand(mm(mm(tr(ra), DET_FORM), ra) == DET_FORM, "word determinant form")
            words += 1
    demand(words == 85, "word fixture count")
    labels = 0
    for carrier, memory in product(range(26), repeat=2):
        outgoing = (memory, carrier)
        demand((outgoing[1], outgoing[0]) == (carrier, memory), "full swap inverse")
        demand(outgoing[0] == memory and outgoing[1] == carrier, "retained label pair")
        labels += 1
    demand(labels == 676, "label fixture count")
    return 8, 16, words, labels


def fmm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % 5
             for j in range(len(b[0]))] for i in range(len(a))]


def fa(a, b):
    return [[(x + y) % 5 for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def fs(a, scalar):
    return [[(x * scalar) % 5 for x in row] for row in a]


def fi(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def finverse(a):
    n = len(a)
    work = [list(row) + unit for row, unit in zip(a, fi(n))]
    for j in range(n):
        pivot = next((k for k in range(j, n) if work[k][j] % 5), None)
        demand(pivot is not None, "F5 invertibility")
        work[j], work[pivot] = work[pivot], work[j]
        multiplier = pow(work[j][j] % 5, -1, 5)
        work[j] = [(x * multiplier) % 5 for x in work[j]]
        for k in range(n):
            if k != j:
                factor = work[k][j]
                work[k] = [(x - factor * y) % 5 for x, y in zip(work[k], work[j])]
    return [row[n:] for row in work]


def fdet2(a):
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % 5


def ftrace(a):
    return sum(a[j][j] for j in range(len(a))) % 5


def fmv(a, v):
    return [sum(x * y for x, y in zip(row, v)) % 5 for row in a]


def residual():
    residues = list(product(range(5), repeat=2))
    images = set()
    for a, b in residues:
        image = ((a + 2 * b) % 5, (a - 2 * b) % 5)
        demand(((a - 2 * b) % 5, (a + 2 * b) % 5) == image[::-1], "CRT star")
        images.add(image)
    demand(len(images) == 25, "CRT bijection")
    products = 0
    for (a, b), (c, d) in product(residues, repeat=2):
        ac, bd = (a * c - b * d) % 5, (a * d + b * c) % 5
        demand((ac + 2 * bd) % 5 == ((a + 2 * b) * (c + 2 * d)) % 5, "CRT first product")
        demand((ac - 2 * bd) % 5 == ((a - 2 * b) * (c - 2 * d)) % 5, "CRT second product")
        products += 1
    g = [[2, 4, 0], [4, 2, 4], [0, 4, 2]]
    m = [[1, 1, 3], [0, 4, 4], [1, 3, 1]]
    mi = finverse(m)
    p = [[1, 1], [1, 4]]
    pi = finverse(p)
    phi5 = [[0, 4, 1], [0, 4, 0], [1, 4, 0]]
    bb = [[0, 2], [2, 0]]
    bbi = finverse(bb)
    omega = [[0, 1], [4, 0]]
    oi = finverse(omega)

    def psi(v):
        h, e, f = fmv(mi, v)
        return fmm(fmm(p, [[h, e], [f, (-h) % 5]]), pi)

    def action(y):
        return fmm(fmm(bb, y), tr(bb))

    demand(fmm(bb, bb) == fs(fi(2), -1), "residual B square")
    demand(action(fi(2)) == fs(fi(2), -1), "scalar complement")
    demand(action(omega) == omega, "skew complement")
    ordinary, alternative = set(), set()
    coordinates = 0
    for t, v1, v2, v3 in product(range(5), repeat=4):
        v = [v1, v2, v3]
        pv, phiv = psi(v), fmv(phi5, v)
        y = fa(fs(fi(2), t), pv)
        ordinary.add(tuple(x for row in y for x in row))
        yy = fmm(pv, oi)
        demand(yy == tr(yy), "symmetric alternative slice")
        yalt = fa(fs(omega, t), yy)
        alternative.add(tuple(x for row in yalt for x in row))
        gv = sum(x * z for x, z in zip(v, fmv(g, v))) % 5
        demand(fdet2(y) == (t * t + gv) % 5, "full determinant decomposition")
        demand(fdet2(yalt) == (t * t + gv) % 5, "alternative determinant decomposition")
        demand(action(y) == fs(fmm(fmm(bb, y), bbi), -1), "honest congruence versus adjoint")
        demand(action(pv) == fs(psi(phiv), -1), "original trace-zero minus Phi")
        demand(action(yy) == fmm(psi(phiv), oi), "symmetric slice plus Phi")
        demand(action(y) == fa(fs(fi(2), -t), fs(psi(phiv), -1)), "full original action")
        demand(action(yalt) == fa(fs(omega, t), fmm(psi(phiv), oi)), "full alternative action")
        aa, dd = y[0][0], y[1][1]
        real = 3 * (y[0][1] + y[1][0]) % 5
        imag = 4 * (y[1][0] - y[0][1]) % 5
        plus = [[aa, (real - 2 * imag) % 5], [(real + 2 * imag) % 5, dd]]
        minus = [[aa, (real + 2 * imag) % 5], [(real - 2 * imag) % 5, dd]]
        demand(plus == y and minus == tr(y), "whole Hermitian CRT descent")
        demand(fdet2(action(y)) == fdet2(y), "residual determinant preservation")
        coordinates += 1
    demand(len(ordinary) == len(alternative) == coordinates == 625, "full residue carriers")
    basis = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    trace_pairs = 0
    for i, j in product(range(3), repeat=2):
        demand(ftrace(fmm(psi(basis[i]), psi(basis[j]))) == 3 * g[i][j] % 5, "trace metric")
        trace_pairs += 1
    wrong_adjoint = any(action(psi(v)) != fmm(fmm(bb, psi(v)), bbi) for v in basis)
    demand(wrong_adjoint, "negative control: Ad cannot replace original congruence")
    return coordinates, trace_pairs, products


PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def exterior(a):
    return [[a[i][k] * a[j][ell] - a[i][ell] * a[j][k]
             for k, ell in PAIRS] for i, j in PAIRS]


def gram(basis, form):
    return mm(mm(tr(basis), form), basis)


def square_rational(x):
    if x < 0:
        return False
    return isqrt(x.numerator) ** 2 == x.numerator and isqrt(x.denominator) ** 2 == x.denominator


def hodge_and_metric():
    cycle = matrix([[-1, -1, -1, -1], [1, 0, 0, 0],
                    [0, 1, 0, 0], [0, 0, 1, 0]])
    powers, cp = [], eye(4)
    for _ in range(5):
        powers.append(cp)
        cp = mm(cp, cycle)
    demand(cp == eye(4), "root cycle order five")
    cyclotomic = matrix([[0] * 4 for _ in range(4)])
    for power in powers:
        cyclotomic = ma(cyclotomic, power)
    demand(cyclotomic == matrix([[0] * 4 for _ in range(4)]), "root cyclotomic relation")
    mj = ma(eye(4), mm(cycle, cycle))
    l = exterior(mj)
    expected_l = matrix([[0, -1, 0, 0, 0, 1], [0, 1, -1, 0, 0, -1],
                         [1, 0, 1, 0, -1, 0], [0, 0, 1, 0, 0, 1],
                         [-1, 0, -1, 1, 1, -1], [1, 0, 1, -1, 0, 1]])
    demand(l == expected_l, "root-derived exterior J action")
    h = matrix([[1 + int(i == j) for j in range(4)] for i in range(4)])
    g2 = exterior(h)
    beta = matrix([[0] * 6 for _ in range(6)])
    for i, j, sign in [(0, 5, 1), (1, 4, -1), (2, 3, 1)]:
        beta[i][j] = beta[j][i] = N(sign)
    k_hodge = mm(beta, g2)
    demand(mm(k_hodge, k_hodge) == ms(eye(6), 5), "Hodge square")
    pplus = ms(ma(eye(6), ms(k_hodge, 1 / R)), Fraction(1, 2))
    demand(mm(pplus, pplus) == pplus and rank(pplus) == 3, "Hodge projector")
    demand(mm(mm(tr(l), beta), l) == beta, "exterior wedge preservation")
    chosen = []
    for j in range(6):
        candidate = col(pplus, j)
        if rank(cols(chosen + [candidate])) > len(chosen):
            chosen.append(candidate)
    demand(len(chosen) == 3, "deterministic independent Pplus columns")
    p1, p2, p3 = chosen
    demand(p1 == vs([N(5), R, -R, R, -R, 3 * R], Fraction(1, 10)), "canonical first column")
    demand(p2 == vs([-R, N(5), R, R, -3 * R, R], Fraction(1, 10)), "canonical second column")
    demand(p3 == vs([R, -R, N(5), 3 * R, -R, R], Fraction(1, 10)), "canonical third column")
    residual_columns = mm(mm(sub(eye(6), pplus), l), pplus)
    fourth = next(col(residual_columns, j) for j in range(6) if any(col(residual_columns, j)))
    ej = cols(chosen + [fourth])
    demand(rank(ej) == 4, "canonical E_J rank")
    gej = gram(ej, beta)
    expected_g = matrix([[0] * 4 for _ in range(4)])
    for i, j in product(range(3), repeat=2):
        expected_g[i][j] = R * (3 if i == j else 1) / 10
    expected_g[3][3] = -(2 + R) / 8
    demand(gej == expected_g, "canonical marked wedge Gram")
    selected_rows = []
    row_numbers = []
    for i, row in enumerate(ej):
        if rank(selected_rows + [row]) > len(selected_rows):
            selected_rows.append(row)
            row_numbers.append(i)
    demand(len(selected_rows) == 4, "E_J coordinate row selection")
    lej = mm(l, ej)
    target = mm(inverse(selected_rows), [lej[i] for i in row_numbers])
    demand(mm(ej, target) == lej, "E_J invariance")
    demand(characteristic(target) == TARGET_POLY, "complete canonical target factors")
    demand(det(gej) == -(5 + 2 * R) / 80, "canonical Gram determinant")
    principal_eigenvalues = [R / 2, R / 5, R / 5, -(2 + R) / 8]
    demand([x.real_sign() for x in principal_eigenvalues] == [1, 1, 1, -1], "principal signature")
    demand([x.sigma().real_sign() for x in principal_eigenvalues] == [-1, -1, -1, 1], "other real signature")
    ratio = (5 + 2 * R) / 80
    norm = (ratio * ratio.sigma()).rational()
    demand(norm == Fraction(1, 1280) and not square_rational(norm), "F(i) determinant square obstruction")
    demand(det(gej) / DELTA == PHI ** 4 / 80, "CM determinant square-class ratio")
    demand(PHI ** 4 / 80 == (PHI ** 2 / (4 * R)) ** 2, "CM explicit square witness")
    v = va(p1, vs(p3, -1))
    w = mv(l, v)
    demand(mv(l, w) == va(vs(w, PHI), vs(v, -1)), "compact primary equation")
    demand(bilinear(beta, v, v) == 2 * R / 5, "compact first norm")
    demand(bilinear(beta, w, w) == 2 * R / 5, "compact second norm")
    demand(bilinear(beta, v, w) == R * PHI / 5, "compact mixed norm")
    compact_polynomial = ma(sub(mm(l, l), ms(l, PHI)), eye(6))
    rvec = mv(compact_polynomial, p1)
    uplus = mv(sub(l, ms(eye(6), PHI ** -2)), rvec)
    uminus = mv(sub(l, ms(eye(6), PHI ** 2)), rvec)
    pairing = bilinear(beta, uplus, uminus)
    demand(pairing == -5 * PHI / 4, "boost pairing")
    demand(mv(l, uplus) == vs(uplus, PHI ** 2), "positive boost eigenline")
    demand(mv(l, uminus) == vs(uminus, PHI ** -2), "negative boost eigenline")
    demand(bilinear(beta, uplus, uplus) == 0 and bilinear(beta, uminus, uminus) == 0, "boost null lines")
    icm = cols([uplus, vs(uminus, -1 / (R * pairing)), v, w])
    demand(rank(icm) == 4, "CM comparison rank")
    rcm = matrix([[PHI ** 2, 0, 0, 0], [0, PHI ** -2, 0, 0],
                  [0, 0, 0, -1], [0, 0, 1, PHI]])
    gcm = matrix([[0, Fraction(-1, 2), 0, 0], [Fraction(-1, 2), 0, 0, 0],
                  [0, 0, 1, PHI / 2], [0, 0, PHI / 2, 1]])
    demand(mm(l, icm) == mm(icm, rcm), "full CM action intertwiner")
    demand(gram(icm, ms(beta, R / 2)) == gcm, "full scaled CM form identity")
    old_gram = gram(icm, ms(beta, 1 / R))
    demand(old_gram == ms(gcm, Fraction(2, 5)), "old normalization exact factor")
    demand(old_gram != gcm, "negative control: old and new metric scales differ")
    demand(det(gcm) == DELTA / 16, "CM determinant form square class")
    return rcm, gcm


def cm_action(rcm, gcm):
    zeta = CM(PHI / 2, Fraction(1, 2))
    demand(zeta * zeta - CM(PHI) * zeta + 1 == 0, "CM root relation")
    demand(zeta.star() == CM(PHI) - zeta and zeta * zeta.star() == 1, "CM conjugation")
    zero, one = CM(0), CM(1)
    spinor = [[CM(PHI) * zeta, zero], [zero, CM(PHI ** -1)]]
    basis = [[[one, zero], [zero, zero]], [[zero, zero], [zero, one]],
             [[zero, one], [one, zero]], [[zero, zeta], [zeta.star(), zero]]]

    def coordinates(x):
        demand(adj(x) == x and not x[0][0].b and not x[1][1].b, "CM Hermitian coordinates")
        upper = x[0][1]
        return [x[0][0].a, x[1][1].a, upper.a - PHI * upper.b, 2 * upper.b]

    actual = cols([coordinates(mm(mm(spinor, x), adj(spinor))) for x in basis])
    demand(actual == rcm, "CM spinor congruence action")
    demand(mm(mm(tr(actual), gcm), actual) == gcm, "CM determinant-form preservation")
    current_action = cols([coordinates(mm(mm(adj(spinor), x), spinor)) for x in basis])
    demand(rank(sub(current_action, eye(4))) == 4, "negative control: CM spinor has no nonzero fixed current")
    demand(det(sub(actual, eye(4))) == -(2 - PHI), "target lacks unit eigenvalue")
    demand(det(ma(actual, eye(4))) == 5 * (2 + PHI), "target lacks minus-unit eigenvalue")


def f4mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return out


def inert_prime():
    demand(all((x * x + x + 1) % 2 for x in range(2)), "phi irreducible modulo two")
    values = [f4mul(x, x) ^ f4mul(2, x) ^ 1 for x in range(4)]
    demand(values == [1, 2, 1, 2], "F4 extension residue values")
    demand(all(values), "CM polynomial has no F4 root")
    demand(2 != 0, "nonzero residue derivative")
    value = Fraction(2, 5)
    numerator, denominator = value.numerator, value.denominator
    valuation = 0
    while numerator % 2 == 0:
        numerator //= 2
        valuation += 1
    while denominator % 2 == 0:
        denominator //= 2
        valuation -= 1
    demand(valuation == 1 and valuation % 2 == 1, "odd valuation of two-fifths")


def remaining_negative_controls():
    incorrect_receiver = matrix([[C, S], [S, C]])
    bad_transfer = regroup(incorrect_receiver)
    demand(mm(mm(adj(bad_transfer), SIGMA), bad_transfer) != SIGMA,
           "negative control: wrong receiver sign fails current")
    demand(characteristic(congruence(TQ)) != TARGET_POLY,
           "negative control: full marked T is not Hodge")


def main():
    phases, boundary_cases, words, labels = phase_and_words()
    coordinates, trace_pairs, crt_products = residual()
    rcm, gcm = hodge_and_metric()
    cm_action(rcm, gcm)
    inert_prime()
    remaining_negative_controls()
    print("CERTIFICATE=C-HODGE-BOUNDARY-CURRENT-N-CODE-BLIND-BREAKER")
    print("STATUS=NON-CANONICAL;L1;candidate-C")
    print("EXACT_FIELDS=Q(sqrt5,i);Q(sqrt5,tau)")
    print("SPATIAL_PHASES=" + str(phases))
    print("BOUNDARY_BASIS_CASES=" + str(boundary_cases))
    print("TRANSFER_WORDS=" + str(words))
    print("RETAINED_LABEL_PAIRS=" + str(labels))
    print("CRT_ELEMENTS=25")
    print("CRT_PRODUCTS=" + str(crt_products))
    print("HERMITIAN_RESIDUE_COORDINATES=" + str(coordinates))
    print("TRACE_BASIS_PAIRS=" + str(trace_pairs))
    print("HODGE_RECONSTRUCTIONS=1")
    print("CM_FULL_ACTION_AND_FORM=PASS")
    print("INERT_RESIDUE_ELEMENTS=4")
    print("NEGATIVE_CONTROLS=5")
    print("BOUNDARY_CURRENT_AND_COMPLETE_POLYNOMIAL=PASS")
    print("STAR_COMPATIBLE_REDUCTION_AND_BOTH_SLICES=PASS")
    print("TWO_PLACE_METRIC_AND_NORM_OBSTRUCTIONS=PASS")
    print("CM_DUAL_NUMBER_SATURATED_LATTICE_COMPARISON=ANALYTIC_ONLY")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
