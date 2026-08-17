#!/usr/bin/env python3
"""Exact breakers for C-RH-PYTHAGORAS-HALFANGLE-2-N.

No floating point. Standard library only.
"""
from fractions import Fraction as F


def local_delayed_leg_breaker() -> None:
    # Normalize L=1 by homogeneity. For h_L(t)=(|t|-L)_+, either sign
    # of the polarized kernel has the same 2x2 determinant.
    # At t=L/2, u=3L/2 the matrix for g=+h_L is
    # [[0,-L/2],[-L/2,-L]].  Set L=1 exactly.
    M00 = F(0)
    M01 = -F(1, 2)
    M11 = -F(1)
    det = M00 * M11 - M01 * M01
    assert det == -F(1, 4)
    assert det < 0
    print("F1 PASS: single delayed leg is indefinite; det/L^2 = -1/4")


def half_angle_nonuniqueness_breaker() -> None:
    # For omega=c+is, the conjugate pair of quadratic norm differences
    # reconstructs a+ib whenever c*s != 0.  A non-root-of-unity-style
    # rational point (3/5,4/5) already works, so reconstruction alone
    # cannot force zeta_8.
    c, s = F(3, 5), F(4, 5)
    assert c*c + s*s == 1
    assert c*s != 0

    # Generic test cross term z=a+ib.
    a, b = F(7, 11), -F(5, 13)
    # Convention D_omega = 4 Re(omega z) = 4(ca-sb),
    # D_bar   = 4 Re(conj(omega) z) = 4(ca+sb).
    Dp = 4 * (c*a - s*b)
    Dm = 4 * (c*a + s*b)
    a_rec = (Dp + Dm) / (8*c)
    b_rec = (Dm - Dp) / (8*s)
    assert a_rec == a
    assert b_rec == b
    print("F2 PASS: bilinear reconstruction does not uniquely select zeta_8")


def balanced_selector_boundary() -> None:
    # If one separately requires a conjugate phase pair with equal sensitivity
    # to Re and Im quadratures, |c|=|s| together with c^2+s^2=1 forces
    # c^2=s^2=1/2, hence omega^2 is +/- i.  We check the algebraic squares
    # without introducing sqrt(2) numerically.
    c2 = s2 = F(1, 2)
    assert c2 + s2 == 1
    # (c+is)^2 has real part c^2-s^2=0 and imaginary magnitude 2|cs|=1.
    real_sq = c2 - s2
    imag_sq_abs2 = 4*c2*s2
    assert real_sq == 0
    assert imag_sq_abs2 == 1
    print("BOUNDARY PASS: balanced conjugate polarization forces omega^2 = +/- i")


if __name__ == "__main__":
    local_delayed_leg_breaker()
    half_angle_nonuniqueness_breaker()
    balanced_selector_boundary()
    print("ALL BREAKER CHECKS PASS")
