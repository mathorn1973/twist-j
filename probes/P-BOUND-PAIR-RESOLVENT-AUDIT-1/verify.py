#!/usr/bin/env python3
"""Original-operator, exact Laurent-polynomial resolvent audit.

Author: A. M. Thorn <thorn@twistj.com>
SPDX-License-Identifier: Apache-2.0

No numerical quadrature, predecessor import, fixture, network or float.
All scientific objects are constructed only inside main().
"""

from fractions import Fraction
from itertools import permutations


NV = 6  # lambda, w, z, gamma, q, i
L, W, Z, GAMMA, Q, IMAG = range(NV)


class Poly:
    """Sparse rational Laurent polynomials, with i**2 = -1.

    lambda,w,z,gamma may have negative powers; q is polynomial.
    q's quadratic relation is applied explicitly, only by reduce_q().
    """

    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.terms = dict(value.terms)
            return
        raw = value if isinstance(value, dict) else {(0,) * NV: Fraction(value)}
        out = {}
        for exponent, coefficient in raw.items():
            if len(exponent) != NV or exponent[Q] < 0:
                raise ValueError("invalid Laurent exponent")
            coefficient = Fraction(coefficient)
            exponent = list(exponent)
            remainder = exponent[IMAG] % 4
            if remainder >= 2:
                coefficient = -coefficient
            exponent[IMAG] = remainder % 2
            key = tuple(exponent)
            out[key] = out.get(key, Fraction(0)) + coefficient
        self.terms = {key: value for key, value in out.items() if value}

    @staticmethod
    def variable(index):
        exponent = [0] * NV
        exponent[index] = 1
        return Poly({tuple(exponent): Fraction(1)})

    def __add__(self, other):
        other = Poly(other)
        out = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            out[exponent] = out.get(exponent, Fraction(0)) + coefficient
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) + (-self)

    def __mul__(self, other):
        other = Poly(other)
        out = {}
        for a, ca in self.terms.items():
            for b, cb in other.terms.items():
                exponent = tuple(x + y for x, y in zip(a, b))
                out[exponent] = out.get(exponent, Fraction(0)) + ca * cb
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        if isinstance(scalar, Poly):
            raise TypeError("only rational scalar division is admitted")
        return self * (Fraction(1) / Fraction(scalar))

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("integer powers only")
        if power < 0:
            if len(self.terms) != 1:
                raise ValueError("negative powers require a single monomial")
            (exponent, coefficient), = self.terms.items()
            return Poly({tuple(power * v for v in exponent): coefficient ** power})
        answer, base = Poly(1), self
        while power:
            if power % 2:
                answer = answer * base
            base = base * base
            power //= 2
        return answer


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum((a[r][j] * b[j][c] for j in range(len(b))), Poly(0))
             for c in range(len(b[0]))] for r in range(len(a))]


def identity(n):
    return [[Poly(int(r == c)) for c in range(n)] for r in range(n)]


def matrix_difference(a, b):
    return [a[r][c] - b[r][c] for r in range(len(a))
            for c in range(len(a[0]))]


def determinant(a):
    n = len(a)
    answer = Poly(0)
    for permutation in permutations(range(n)):
        inversions = sum(permutation[r] > permutation[c]
                         for r in range(n) for c in range(r + 1, n))
        term = Poly((-1) ** inversions)
        for r in range(n):
            term = term * a[r][permutation[r]]
        answer = answer + term
    return answer


def adjugate(a):
    n = len(a)
    return [[((-1) ** (r + c)) * determinant(
        [[a[j][k] for k in range(n) if k != r]
         for j in range(n) if j != c])
        for c in range(n)] for r in range(n)]


def coefficient(poly, index, power):
    out = {}
    for exponent, value in poly.terms.items():
        if exponent[index] == power:
            exponent = list(exponent)
            exponent[index] = 0
            out[tuple(exponent)] = value
    return Poly(out)


def substitute_nonnegative(poly, index, value):
    answer = Poly(0)
    for exponent, scalar in poly.terms.items():
        exponent = list(exponent)
        power = exponent[index]
        if power < 0:
            raise ValueError("nonnegative substitution only")
        exponent[index] = 0
        answer = answer + Poly({tuple(exponent): scalar}) * value ** power
    return answer


def reduce_q(poly):
    """Unique degree <= 1 remainder modulo q^2 - (t/2)q + 1."""
    lam, w, q = (Poly.variable(index) for index in (L, W, Q))
    t_half = (w + w ** -1 - 5 * lam - 5 * lam ** -1) / 4
    largest = max((key[Q] for key in poly.terms), default=0)
    powers = [Poly(1), q]
    for degree in range(2, largest + 1):
        powers.append(t_half * powers[-1] - powers[-2])
    answer = Poly(0)
    for exponent, scalar in poly.terms.items():
        exponent = list(exponent)
        degree = exponent[Q]
        exponent[Q] = 0
        answer = answer + Poly({tuple(exponent): scalar}) * powers[degree]
    return answer


def conjugate_torus(poly, unit_indices):
    """Conjugate i, invert specified unit variables, fix real variables."""
    out = {}
    for exponent, scalar in poly.terms.items():
        exponent = list(exponent)
        if exponent[IMAG]:
            scalar = -scalar
        for index in unit_indices:
            exponent[index] = -exponent[index]
        out[tuple(exponent)] = scalar
    return Poly(out)


def at_infinity_residual(poly, minimum_lambda_power):
    return Poly({key: value for key, value in poly.terms.items()
                 if key[L] >= minimum_lambda_power})


def contact_moments(coin, initial, lam, w, gamma):
    """Enumerate one/two original lattice steps, no resolvent formula."""
    del lam  # The path enumeration has no spectral parameter.
    state = {(0, c): Poly(amplitude) for c, amplitude in enumerate(initial)
             if amplitude}
    relative_shift = (0, -1, 1, 0)
    center_phase = (w, Poly(1), Poly(1), w ** -1)
    moments = []
    for _step in range(2):
        target = {}
        for (position, source_coin), amplitude in state.items():
            for destination_coin in range(4):
                new_position = position + relative_shift[destination_coin]
                key = (new_position, destination_coin)
                term = (amplitude * coin[destination_coin][source_coin]
                        * center_phase[destination_coin])
                if new_position == 0:
                    term = gamma * term
                target[key] = target.get(key, Poly(0)) + term
        state = target
        moments.append(sum((amplitude * state.get((0, c), Poly(0))
                            for c, amplitude in enumerate(initial)), Poly(0)) / 2)
    return moments


class Audit:
    def __init__(self):
        self.failed = []
        self.groups = 0
        self.identities = 0

    def check(self, label, polynomials, quotient=False, nonzero=False):
        self.groups += 1
        bad = []
        for number, polynomial in enumerate(polynomials):
            remainder = reduce_q(polynomial) if quotient else Poly(polynomial)
            self.identities += 1
            success = bool(remainder.terms) if nonzero else not remainder.terms
            if not success:
                bad.append((number, remainder))
        if bad:
            self.failed.append(label)
            print(label + ": FAIL")
            for number, remainder in bad:
                # Finite, exact witnesses, in deterministic exponent order.
                terms = sorted(remainder.terms.items())
                print("  entry=" + str(number) + "; terms=" + str(len(terms)))
                for exponent, scalar in terms[:3]:
                    print("  " + repr(exponent) + " : " + str(scalar))
        else:
            print(label + ": PASS")


def main():
    print("P-BOUND-PAIR-RESOLVENT-AUDIT-1")
    print("arithmetic: rational Laurent polynomials; no floating point")
    lam, w, z, gamma, q, ii = (Poly.variable(j) for j in range(NV))
    audit = Audit()
    d, c, ell = Fraction(-3, 5), Fraction(4, 5), Fraction(2, 5)
    v = (w + w ** -1) / 2
    u = (w - w ** -1) / (2 * Fraction(1)) * (-ii)
    coin = [[Poly(1), 2 * ii, 2 * ii, Poly(-4)],
            [2 * ii, Poly(1), Poly(-4), 2 * ii],
            [2 * ii, Poly(-4), Poly(1), 2 * ii],
            [Poly(-4), 2 * ii, 2 * ii, Poly(1)]]
    coin = [[entry / 5 for entry in row] for row in coin]
    phases = (w, z, z ** -1, w ** -1)
    free = [[phases[r] * coin[r][s] for s in range(4)] for r in range(4)]
    free_star = transpose([[conjugate_torus(entry, (W, Z)) for entry in row]
                           for row in free])
    audit.check("original symbol unitarity", matrix_difference(
        multiply(free_star, free), identity(4)))

    resolvent = [[(lam if r == s else Poly(0)) - free[r][s]
                  for s in range(4)] for r in range(4)]
    raw_det = determinant(resolvent)
    raw_adj = adjugate(resolvent)
    audit.check("raw adjugate left and right", matrix_difference(
        multiply(resolvent, raw_adj),
        [[raw_det * int(r == s) for s in range(4)] for r in range(4)])
        + matrix_difference(multiply(raw_adj, resolvent),
        [[raw_det * int(r == s) for s in range(4)] for r in range(4)]))

    D0 = lam ** 2 - ell * v * lam + d
    D1 = d * lam ** 2 - ell * v * lam + 1
    aa = lam ** 4 - ell * v * lam ** 3 + 2 * d * lam ** 2 - ell * v * lam + 1
    bb = ell * lam * (lam ** 2 - 2 * v * lam + 1)
    audit.check("free determinant and Schur factors", [
        raw_det - aa + bb * (z + z ** -1) / 2,
        aa - lam ** 2 * D0 - D1,
        bb - lam * (D0 + D1),
        aa ** 2 - bb ** 2 - (lam ** 2 - 1) * (lam ** 2 * D0 ** 2 - D1 ** 2)])

    bell_columns = [[Poly(1), Poly(1), Poly(0), Poly(0)],
                    [Poly(0), Poly(0), Poly(1), Poly(1)],
                    [Poly(0), Poly(0), Poly(1), Poly(-1)],
                    [Poly(-1), Poly(1), Poly(0), Poly(0)]]
    bell_adj = multiply(multiply(transpose(bell_columns), raw_adj), bell_columns)
    bell_adj = [[entry / 2 for entry in row] for row in bell_adj]
    unsupported = [Poly({key: value for key, value in entry.terms.items()
                         if key[Z] not in (-1, 0, 1)})
                   for row in bell_adj for entry in row]
    audit.check("adjugate relative Laurent support", unsupported)
    n0 = [[coefficient(entry, Z, 0) for entry in row] for row in bell_adj]
    nc = [[coefficient(entry, Z, 1) + coefficient(entry, Z, -1)
           for entry in row] for row in bell_adj]
    t = v - Fraction(5, 2) * (lam + lam ** -1)
    rr = t - 4 * q
    sigma = -ell * lam * (lam ** 2 - 1) * rr
    audit.check("physical radical polynomial identities", [
        rr ** 2 - t ** 2 + 16,
        sigma ** 2 - aa ** 2 + bb ** 2,
        (lam + q) * (aa - sigma) - bb * (1 + lam * q),
        (lam * D0 - D1 * q) * (lam * bb - aa + sigma) - bb * sigma], quotient=True)
    numerator = [[bb * n0[r][s] + (aa - sigma) * nc[r][s]
                  for s in range(4)] for r in range(4)]
    denominator = bb * sigma
    even = [[numerator[r][s] for s in range(3)] for r in range(3)]
    ke = [[lam - v, -ii * d * u, c * u],
          [-ii * u, lam - d * v, -ii * c * v],
          [Poly(0), -ii * c * q, lam - d * q]]
    scalar_identity = [[denominator * int(r == s) for s in range(3)]
                       for r in range(3)]
    audit.check("full even contact inverse left and right", matrix_difference(
        multiply(ke, even), scalar_identity)
        + matrix_difference(multiply(even, ke), scalar_identity), quotient=True)
    audit.check("odd separation and direct BB cofactor", [
        numerator[r][3] for r in range(3)] + [numerator[3][r] for r in range(3)]
        + [numerator[3][3] - (bb * lam * D0 - D1 * (aa - sigma))], quotient=True)
    gbb_numerator = numerator[3][3]
    free_b_numerator = rr + 2 * (lam - lam ** -1)
    free_b_denominator = v - (lam + lam ** -1) / 2
    audit.check("complete free odd Caratheodory function", [
        (2 * lam * gbb_numerator - denominator) * free_b_denominator
        - free_b_numerator * denominator], quotient=True)

    x = lam * gamma ** -1
    shifted = [[ke[r][s] - (lam - x if r == s else Poly(0))
                for s in range(3)] for r in range(3)]
    nn = x ** 2 - d * (v + q) * x + v * q
    dd = x ** 3 - (ell * v + d * q) * x ** 2 + (d + ell * v * q) * x - q
    audit.check("all-coin contact determinant and A cofactor", [
        determinant(shifted) - dd, adjugate(shifted)[0][0] - nn])
    contact_b_numerator = (1 + gamma) * lam * gbb_numerator - gamma * denominator
    contact_b_denominator = gamma * denominator + (1 - gamma) * lam * gbb_numerator
    b_numerator = rr + 2 * (x - x ** -1)
    b_denominator = t + 2 * (x + x ** -1)
    audit.check("complete interacting odd function", [
        contact_b_numerator * b_denominator - b_numerator * contact_b_denominator],
        quotient=True)

    # Independent v, unit x and real q: continuum real-part identity.
    vf, xf, qf = gamma, w, z
    nf = xf ** 2 - d * (vf + qf) * xf + vf * qf
    df = xf ** 3 - (ell * vf + d * qf) * xf ** 2 + (d + ell * vf * qf) * xf - qf
    pf = 2 * xf * nf - df
    audit.check("even continuum density numerator", [
        pf * conjugate_torus(df, (W,)) + conjugate_torus(pf, (W,)) * df
        - Fraction(32, 25) * (1 - vf ** 2) * (1 - qf ** 2)])

    # q = x*a^2, a = exp(-i*chi): global gap identity, no sampled phases.
    aq = xf * z ** 2
    ng = xf ** 2 - d * (vf + aq) * xf + vf * aq
    dg = xf ** 3 - (ell * vf + d * aq) * xf ** 2 + (d + ell * vf * aq) * xf - aq
    pg = 2 * xf * ng - dg
    cd, sd = (xf + xf ** -1) / 2, (-ii) * (xf ** -1 - xf) / 2
    cc, sc = (z + z ** -1) / 2, (-ii) * (z ** -1 - z) / 2
    hh = (cd - vf) * sc - 4 * sd * cc
    gg = 4 * (cd + vf) * cc + sd * sc
    audit.check("full gap H/G representation", [hh * pg + ii * gg * dg])
    for sign in (-1, 1):
        ns = x ** 2 - d * (sign + q) * x + sign * q
        ds = x ** 3 - (ell * sign + d * q) * x ** 2 + (d + ell * sign * q) * x - q
        audit.check("compact A branch v=" + str(sign), [
            (2 * x * ns - ds) * (x - sign) - ds * (x + sign)])

    ma = contact_moments(coin, (1, 0, 0, -1), lam, w, gamma)
    mb = contact_moments(coin, (0, 1, -1, 0), lam, w, gamma)
    audit.check("direct original-walk return moments", [
        ma[0] - gamma * v, ma[1] - gamma ** 2 * (ell * v ** 2 - d),
        mb[0], mb[1] - Fraction(4, 5) * gamma])
    q_small = -Fraction(4, 5) * lam ** -1 - Fraction(8, 25) * v * lam ** -2
    audit.check("small exterior root through second order", [
        at_infinity_residual(2 * q_small ** 2 - t * q_small + 2, -1)])
    a_expansion = 1 + 2 * ma[0] * lam ** -1 + 2 * ma[1] * lam ** -2
    b_expansion = 1 + 2 * mb[0] * lam ** -1 + 2 * mb[1] * lam ** -2
    a_residual = substitute_nonnegative(2 * x * nn - dd - a_expansion * dd, Q, q_small)
    b_residual = substitute_nonnegative(b_numerator - b_expansion * b_denominator, Q, q_small)
    audit.check("resolvent moments on exterior sheet", [
        at_infinity_residual(a_residual, 1), at_infinity_residual(b_residual, -1)])
    q_large = t / 2 - q_small
    wrong_sheet = substitute_nonnegative(b_numerator - b_expansion * b_denominator, Q, q_large)
    audit.check("negative control wrong radical sheet", [
        at_infinity_residual(wrong_sheet, -1)], nonzero=True)
    audit.check("negative control omitted contact phase", [ma[0] - v], nonzero=True)

    # Here w,z are independent formal F1,F2; no q relation is used.
    core = [[Poly(Fraction(3, 5)), Poly(Fraction(-4, 5))],
            [Poly(Fraction(4, 5)), Poly(Fraction(3, 5))]]
    kc = [[core[r][s] - int(r == s) for s in range(2)] for r in range(2)]
    mm = [[(w - 1) / 2, Poly(0)], [Poly(0), (z - 1) / 2]]
    mmkc = multiply(mm, kc)
    capture_inverse = [[Poly(int(r == s)) - mmkc[r][s] for s in range(2)]
                       for r in range(2)]
    capture_adjugate = adjugate(capture_inverse)
    transition_numerator = multiply(kc, capture_adjugate)
    audit.check("rank-two scattering determinant and transition", [
        determinant(capture_inverse) - (4 + w * z) / 5,
        transition_numerator[0][0] + 2 * z / 5,
        transition_numerator[1][0] - Fraction(4, 5),
        transition_numerator[0][1] + Fraction(4, 5),
        transition_numerator[1][1] + 2 * w / 5])

    # Independent real/imaginary parts of the two full port functions.
    f1, f2 = w + ii * z, gamma + ii * lam
    full_denominator = 4 + f1 * f2
    tn = [[-2 * f2, Poly(-4)], [Poly(4), -2 * f1]]
    tn_star = transpose([[conjugate_torus(entry, ()) for entry in row]
                         for row in tn])
    re_f = [[w, Poly(0)], [Poly(0), gamma]]
    quadratic = multiply(multiply(tn_star, re_f), tn)
    audit.check("complete on-shell transition unitarity", [
        tn[r][s] * conjugate_torus(full_denominator, ())
        + tn_star[r][s] * full_denominator + quadratic[r][s]
        for r in range(2) for s in range(2)])
    audit.check("complete denominator positive identity", [
        full_denominator * conjugate_torus(full_denominator, ()) - 16 * w * gamma
        - (4 - f1 * conjugate_torus(f2, ()))
        * conjugate_torus(4 - f1 * conjugate_torus(f2, ()), ())])

    pulse = [[(1 - 4 * z) / 5, -2 * (1 + z) / 5],
             [2 * (1 + z ** -1) / 5, (1 - 4 * z ** -1) / 5]]
    pulse_star = transpose([[conjugate_torus(entry, (Z,)) for entry in row]
                            for row in pulse])
    audit.check("original pulse determinant trace and unitarity", [
        determinant(pulse) - 1,
        pulse[0][0] + pulse[1][1] - 2 * (1 - 2 * (z + z ** -1)) / 5]
        + matrix_difference(multiply(pulse_star, pulse), identity(2)))

    print("groups=" + str(audit.groups) + "; exact conditions=" + str(audit.identities))
    print("status: " + ("FALSIFIED" if audit.failed else "CERTIFIED"))
    print("scope: algebraic resolvent audit; not a new probability integration")


if __name__ == "__main__":
    main()
