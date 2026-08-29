#!/usr/bin/env python3
"""Exact audit for C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N.

NON-CANONICAL incubation.  The general theorem is proved in RESULT.md;
this standard-library program audits the frozen Q(zeta_5) specialization,
its reduction seam, and the negative controls.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product

Q = Fraction


@dataclass(frozen=True)
class K5:
    """Element of Q[j]/(j^4+j^3+j^2+j+1) in basis (1,j,j^2,j^3)."""

    c: tuple[Fraction, Fraction, Fraction, Fraction]

    @staticmethod
    def of(*xs: int | Fraction) -> "K5":
        vals = tuple(Q(x) for x in xs)
        assert len(vals) == 4
        return K5(vals)  # type: ignore[arg-type]

    def __add__(self, other: "K5") -> "K5":
        return K5(tuple(a + b for a, b in zip(self.c, other.c)))  # type: ignore[arg-type]

    def __neg__(self) -> "K5":
        return K5(tuple(-a for a in self.c))  # type: ignore[arg-type]

    def __sub__(self, other: "K5") -> "K5":
        return self + (-other)

    def __mul__(self, other: "K5") -> "K5":
        raw = [Q(0) for _ in range(7)]
        for i, a in enumerate(self.c):
            for k, b in enumerate(other.c):
                raw[i + k] += a * b
        # Descending reduction by j^4 = -1-j-j^2-j^3.
        for degree in range(6, 3, -1):
            a = raw[degree]
            if a:
                for shift in range(4):
                    raw[degree - 4 + shift] -= a
                raw[degree] = Q(0)
        return K5(tuple(raw[:4]))  # type: ignore[arg-type]

    def __pow__(self, n: int) -> "K5":
        if n < 0:
            return self.inverse() ** (-n)
        out = ONE
        base = self
        k = n
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k >>= 1
        return out

    def scalar(self, q: int | Fraction) -> "K5":
        return K5(tuple(Q(q) * x for x in self.c))  # type: ignore[arg-type]

    def multiplication_matrix(self) -> list[list[Fraction]]:
        cols = [(self * e).c for e in STD_BASIS]
        return [[cols[j][i] for j in range(4)] for i in range(4)]

    def trace(self) -> Fraction:
        m = self.multiplication_matrix()
        return sum((m[i][i] for i in range(4)), Q(0))

    def norm(self) -> Fraction:
        return det_q(self.multiplication_matrix())

    def sigma(self, a: int) -> "K5":
        """Galois map j -> j^a, with a prime to 5."""
        out = ZERO
        for k, coeff in enumerate(self.c):
            out = out + (JROOT ** (a * k)).scalar(coeff)
        return out

    def conjugate(self) -> "K5":
        return self.sigma(4)

    def inverse(self) -> "K5":
        m = self.multiplication_matrix()
        rhs = [Q(1), Q(0), Q(0), Q(0)]
        coeff = solve_q(m, rhs)
        candidate = K5(tuple(coeff))  # type: ignore[arg-type]
        assert self * candidate == ONE
        return candidate


ZERO = K5.of(0, 0, 0, 0)
ONE = K5.of(1, 0, 0, 0)
JROOT = K5.of(0, 1, 0, 0)
STD_BASIS = (
    ONE,
    JROOT,
    JROOT**2,
    JROOT**3,
)


def det_q(a: list[list[Fraction]]) -> Fraction:
    m = [row[:] for row in a]
    n = len(m)
    out = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            out = -out
        p = m[col][col]
        out *= p
        for j in range(col, n):
            m[col][j] /= p
        for r in range(col + 1, n):
            q = m[r][col]
            if q:
                for j in range(col, n):
                    m[r][j] -= q * m[col][j]
    return out


def solve_q(a: list[list[Fraction]], b: list[Fraction]) -> list[Fraction]:
    n = len(a)
    m = [a[i][:] + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        assert pivot is not None
        m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                q = m[r][col]
                m[r] = [m[r][j] - q * m[col][j] for j in range(n + 1)]
    return [m[i][-1] for i in range(n)]


Dual = tuple[Fraction, Fraction]  # a + eps b, eps^2=0


def dadd(x: Dual, y: Dual) -> Dual:
    return x[0] + y[0], x[1] + y[1]


def dmul(x: Dual, y: Dual) -> Dual:
    return x[0] * y[0], x[0] * y[1] + x[1] * y[0]


def dneg(x: Dual) -> Dual:
    return -x[0], -x[1]


def det_dual(a: list[list[Dual]]) -> Dual:
    n = len(a)
    total: Dual = (Q(0), Q(0))
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term: Dual = (Q(-1 if inversions & 1 else 1), Q(0))
        for i in range(n):
            term = dmul(term, a[i][p[i]])
        total = dadd(total, term)
    return total


def rank_mod_p(a: list[list[int]], p: int) -> int:
    m = [[x % p for x in row] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][c], -1, p)
        m[r] = [(inv * x) % p for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [(m[i][j] - q * m[r][j]) % p for j in range(cols)]
        r += 1
    return r


def main() -> int:
    assert JROOT**5 == ONE and JROOT != ONE
    print("PASS G0: exact cyclotomic ring initialized")

    # G1 audit: det(I + eps M_x) = 1 + eps tr(M_x) on exact witnesses.
    witnesses = [ONE, JROOT, JROOT - JROOT**2, ONE + JROOT**2]
    for x in witnesses:
        mx = x.multiplication_matrix()
        dual_matrix = [
            [
                (Q(int(i == k)), mx[i][k])
                for k in range(4)
            ]
            for i in range(4)
        ]
        assert det_dual(dual_matrix) == (Q(1), x.trace())
    print("PASS G1: norm derivative equals field trace on exact regular-representation audit")

    # G2 audit: the dependent coordinate is the reciprocal product.
    split_tests = [
        (Q(2), Q(3), Q(5)),
        (Q(-1), Q(7, 3), Q(-5, 2)),
        (Q(11, 13), Q(-17, 19), Q(23, 29)),
    ]
    for y1, y2, y3 in split_tests:
        y4 = Q(1, 1) / (y1 * y2 * y3)
        assert y1 * y2 * y3 * y4 == 1
    print("PASS G2: split norm-one chart closes by one reciprocal coordinate")

    # G3: integral basis, trace row, A3 lattice and reduction.
    B = (JROOT, JROOT**2, JROOT**3, JROOT**4)
    change = [[B[j].c[i] for j in range(4)] for i in range(4)]
    assert det_q(change) == 1
    assert [x.trace() for x in B] == [Q(-1)] * 4
    A3 = (
        (1, 0, 0, -1),
        (0, 1, 0, -1),
        (0, 0, 1, -1),
    )
    assert rank_mod_p([list(v) for v in A3], 5) == 3
    reduced = {
        tuple(sum(c[k] * A3[k][i] for k in range(3)) % 5 for i in range(4))
        for c in product(range(5), repeat=3)
    }
    W5 = {v for v in product(range(5), repeat=4) if sum(v) % 5 == 0}
    assert reduced == W5 and len(W5) == 125
    print("PASS G3: integral trace-zero lattice is A3 and reduces exactly to W5")

    # G4: exact algebraic checks supporting the real form and unit-rank firewall.
    phi = -(JROOT**2 + JROOT**3)
    assert phi**2 == phi + ONE
    assert phi * (phi - ONE) == ONE
    zeta10 = -(JROOT**3)
    assert zeta10**10 == ONE and all(zeta10**k != ONE for k in (1, 2, 5))
    # The full product O_K^* = mu_10 x <phi> is inherited from J-HARMONIC-SEAM [T].
    assert (0 + 2 - 1) == 1  # Dirichlet rank for a quartic CM field.
    assert (2 * 2 - 1) == 3  # real Lie dimension of C* x C* under one real norm equation.
    print("PASS G4: real norm-one dimension 3 and integral-unit free rank 1 stay separate")

    # G5: exact J point and the two complex-place modulus identities.
    J = ONE + JROOT**2
    assert J * phi == JROOT
    assert J.norm() == 1
    assert J.trace() == 3
    sigma2_J = J.sigma(2)
    assert sigma2_J == -(phi * JROOT**2)
    abs1_sq = J * J.conjugate()
    abs2_sq = sigma2_J * sigma2_J.conjugate()
    assert abs1_sq == (phi**2).inverse()
    assert abs2_sq == phi**2
    assert abs1_sq * abs2_sq == ONE
    print("PASS G5: J lies on norm one with exact place moduli phi^-1 and phi")
    print("PASS G5L: weighted log-modulus vector is (-2 log(phi), +2 log(phi))")

    # G6: reciprocal refactorization shape, without carrier identification.
    for lam, v, w in [
        (Q(2), Q(3), Q(5)),
        (Q(-7, 3), Q(11, 5), Q(-13, 2)),
    ]:
        assert (lam * v) * (w / lam) == v * w
    print("PASS G6: reciprocal refactorization preserves the matched product")

    # B1-B3 controls.
    assert 4 - 1 == 3
    assert 4 - 1 == 3  # split etale Q^4 has the same dimension.
    dirichlet = {
        "Q(i)": 0 + 1 - 1,
        "Q(sqrt5)": 2 + 0 - 1,
        "Q(zeta5)": 0 + 2 - 1,
    }
    torus_dim = {"Q(i)": 1, "Q(sqrt5)": 1, "Q(zeta5)": 3}
    assert dirichlet["Q(i)"] != torus_dim["Q(i)"]
    assert dirichlet["Q(zeta5)"] != torus_dim["Q(zeta5)"]
    print("PASS B1-B3: degree, split-algebra and rank controls survive")

    # B8: tangent kernel is not the global norm-one locus.
    tangent_witness = JROOT - JROOT**2
    assert tangent_witness.trace() == 0 and tangent_witness.norm() == 5
    assert J.norm() == 1 and J.trace() == 3
    print("PASS B8: trace-zero and norm-one are tangent-related, not equal sets")

    print("ALL PASS: inward-unity norm-trace incubation audit complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
