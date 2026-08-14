#!/usr/bin/env python3
"""Exact checks for R-LAMBDA-COCYCLE-CONDUCTOR-CAPACITY-1-N-REVIEW.

Independent review of C-LAMBDA-COCYCLE-CONDUCTOR-CAPACITY-1-N.
No zeta-zero table is used anywhere in this file.  Section 0 re-derives the
reviewed constants from scratch; sections 1 to 4 check the four review
findings R1 to R4.
"""
from __future__ import annotations

from fractions import Fraction

import sympy as sp


def section0_reviewed_constants() -> sp.Expr:
    """Independent re-derivation of the reviewed note's own constants."""
    C = sp.symbols("C", positive=True)

    simple = sp.Rational(19, 27) - sp.Rational(1, 2)
    assert simple == sp.Rational(11, 54)

    kappa = sp.simplify(4 * simple)
    assert kappa == sp.Rational(22, 27)

    f1 = sp.Rational(11, 108) / C - sp.Rational(1, 4) / C**3
    C1 = 9 / sp.sqrt(11)
    assert sp.simplify(sp.diff(f1, C).subs(C, C1)) == 0
    assert sp.simplify(sp.diff(f1, C, 2).subs(C, C1)) < 0
    c1 = sp.simplify(f1.subs(C, C1) / (2 * sp.pi))
    assert c1 == 11 * sp.sqrt(11) / (2916 * sp.pi)

    for B in range(1, 16):
        qB = 4 * 5**B
        degrees = [sp.totient(n) for n in (5**B, 2 * 5**B, 4 * 5**B)]
        assert min(degrees) == qB // 5
        assert max(degrees) == 2 * qB // 5

    print("PASS 0: reviewed constants re-derived independently (11/54, 22/27,")
    print("        C*=9/sqrt(11), 11*sqrt(11)/(2916 pi), min degree q_B/5)")
    return c1


def section1_theorem4_is_v_independent() -> None:
    """R1.  mu_v(T \\ G_A) is determined by sigma alone, for every v.

    Model: a finite conjugation-symmetric point set with an involution.
    Given only the symmetrization identity (mu + check-mu)/2 = sigma/2 and a
    conjugation-invariant test set S, the value mu(S) is forced, independently
    of mu.  Deterministic LCG, no PRNG-version dependence.
    """
    n_pairs = 40
    state = 12345

    def nxt() -> int:
        nonlocal state
        state = (1103515245 * state + 12345) % (2**31)
        return state % 97 + 1

    # index i in 0..n_pairs-1 pairs with its conjugate n_pairs+i; last point fixed.
    size = 2 * n_pairs + 1
    conj = {i: (i + n_pairs if i < n_pairs else i - n_pairs) for i in range(2 * n_pairs)}
    conj[size - 1] = size - 1

    # S conjugation invariant: pick pairs 0..9 plus the fixed point.
    S = set(range(10)) | {conj[i] for i in range(10)} | {size - 1}
    assert {conj[i] for i in S} == S

    for trial in range(200):
        mu = [Fraction(nxt(), nxt()) for _ in range(size)]
        check_mu = [mu[conj[i]] for i in range(size)]
        sigma = [mu[i] + check_mu[i] for i in range(size)]
        assert sum(mu[i] for i in S) * 2 == sum(sigma[i] for i in S), trial

    print("PASS 1 (R1): on every conjugation-invariant set the symmetrization")
    print("        identity forces mu_v(S) = sigma(S)/2 for every v, so")
    print("        Theorem 4 constrains sigma, not the cocycle vector")


def section2_dyadic_sum() -> sp.Expr:
    """R2.  Summing all dyadic windows improves the Theorem 3 constant by sqrt(7)."""
    C = sp.symbols("C", positive=True)
    j = sp.symbols("j", nonnegative=True, integer=True)

    # window j contributes  11/(216 pi C) 2^-j  -  1/(8 pi C^3) 8^-j
    S1 = sp.summation(sp.Rational(11, 216) / C * 2 ** (-j), (j, 0, sp.oo))
    S2 = sp.summation(sp.Rational(1, 8) / C**3 * 8 ** (-j), (j, 0, sp.oo))
    f2 = sp.simplify(S1 - S2)
    assert sp.simplify(f2 - (sp.Rational(11, 108) / C - sp.Rational(1, 7) / C**3)) == 0

    crit = [c for c in sp.solve(sp.diff(f2, C), C) if c.is_positive]
    assert len(crit) == 1
    C2 = sp.simplify(crit[0])
    assert sp.simplify(C2 - 18 / sp.sqrt(77)) == 0
    assert sp.simplify(sp.diff(f2, C, 2).subs(C, C2)) < 0

    c2 = sp.simplify(f2.subs(C, C2) / sp.pi)
    assert sp.simplify(c2 - 11 * sp.sqrt(77) / (2916 * sp.pi)) == 0

    # every window from j=0 up is already positive at C2
    assert sp.simplify(27 / (11 * C2**2)) == sp.Rational(7, 12)

    print("PASS 2 (R2): dyadic sum gives C*=18/sqrt(77) and the constant")
    print("        11*sqrt(77)/(2916 pi), all windows positive from j=0")
    return c2


def section3_theorem5_window_invariance() -> None:
    """R3.  The Theorem 5 coefficient does not depend on the window index."""
    j = sp.symbols("j", nonnegative=True, integer=True)
    # window j allows kappa < (22/27) 4^j, but then gamma <= 2^(j+1) T,
    # so T^2 >= gamma^2 / 4^(j+1) and the factor 4^j cancels.
    coeff = sp.simplify(sp.Rational(22, 27) * 4**j / (5 * 4 ** (j + 1)))
    assert coeff == sp.Rational(11, 270)
    print("PASS 3 (R3): Theorem 5 coefficient = 11/270 for every window j,")
    print("        so that route is already optimal for this method")


def section4_height_bound() -> None:
    """R4.  rho = 1/(1-xi) with xi a root of unity has height at most log 2.

    Checked here as the underlying algebraic identity plus the standard
    height inequality h(a-b) <= h(a)+h(b)+log 2 with h(1)=h(xi)=0, and
    h(1/x)=h(x).  Northcott therefore cannot fire: the degree is unbounded
    while the height is not.
    """
    from math import gcd, log

    from mpmath import mp, mpf

    mp.dps = 60
    log2 = mp.log(2)
    for m in (5, 20, 100, 500, 2500, 4 * 5**4, 4 * 5**5):
        # exact: 1/(1-zeta) has real part 1/2 for every root of unity zeta != 1
        xi = sp.exp(2 * sp.pi * sp.I / m)
        assert sp.simplify(sp.re(1 / (1 - xi)) - sp.Rational(1, 2)) == 0
        # height of 1-zeta_m via the Mahler measure of its minimal polynomial
        # (the conjugates of 1-zeta_m are exactly 1-zeta_m^k, gcd(k,m)=1)
        deg = 0
        logM = mp.mpf(0)
        for k in range(1, m):
            if gcd(k, m) == 1:
                deg += 1
                r = abs(1 - mp.e ** (2j * mp.pi * k / m))
                if r > 1:
                    logM += mp.log(r)
        h = logM / deg
        assert h <= log2 + mpf("1e-40"), (m, h)
    print("PASS 4 (R4): rho = 1/(1-xi) sits on Re s = 1/2 and has height")
    print("        at most log 2, so closure step 3 cannot use Northcott")


def main() -> int:
    c1 = section0_reviewed_constants()
    section1_theorem4_is_v_independent()
    c2 = section2_dyadic_sum()
    section3_theorem5_window_invariance()
    section4_height_bound()

    ratio = sp.simplify(c2 / c1)
    assert ratio == sp.sqrt(7)
    print("PASS 5: improvement ratio new/old = sqrt(7)")

    print("ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
