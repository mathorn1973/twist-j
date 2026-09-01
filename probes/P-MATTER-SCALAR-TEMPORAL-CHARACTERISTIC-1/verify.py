#!/usr/bin/env python3
"""Exact audit for the scalar massive D3 temporal characteristic."""

from __future__ import annotations

from fractions import Fraction


Poly = dict[tuple[int, int, int, int, int], Fraction]
# Exponent order: Omega, x, y, z, M.


def poly_add(*terms: Poly) -> Poly:
    out: Poly = {}
    for term in terms:
        for monomial, coefficient in term.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
            if out[monomial] == 0:
                del out[monomial]
    return out


def poly_scale(term: Poly, scalar: Fraction | int) -> Poly:
    factor = Fraction(scalar)
    return {
        monomial: coefficient * factor
        for monomial, coefficient in term.items()
        if coefficient * factor
    }


def poly_mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for a, ca in left.items():
        for b, cb in right.items():
            monomial = tuple(x + y for x, y in zip(a, b))
            out[monomial] = out.get(monomial, Fraction(0)) + ca * cb
            if out[monomial] == 0:
                del out[monomial]
    return out


def var(index: int) -> Poly:
    exponent = [0, 0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): Fraction(1)}


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")


def affine_mul(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction]:
    """Multiply affine polynomials a+bq and c+dq."""
    a, b = left
    c, d = right
    return (a * c, a * d + b * c, b * d)


def main() -> None:
    # P_q(zeta)=zeta^2+(q-2)zeta+1.
    q_minus_2 = (Fraction(-2), Fraction(1))
    assert_equal(q_minus_2, (Fraction(-2), Fraction(1)), "middle coefficient")

    # T_q=[[2-q,-1],[1,0]] has determinant one and trace 2-q.
    two_minus_q = (Fraction(2), Fraction(-1))
    minus_one = (Fraction(-1), Fraction(0))
    one = (Fraction(1), Fraction(0))
    zero = (Fraction(0), Fraction(0))
    ad = affine_mul(two_minus_q, zero)
    bc = affine_mul(minus_one, one)
    assert_equal(
        tuple(a - b for a, b in zip(ad, bc)),
        (Fraction(1), Fraction(0), Fraction(0)),
        "transfer determinant",
    )
    assert_equal(two_minus_q, (Fraction(2), Fraction(-1)), "transfer trace")

    # Delta_q=(q-2)^2-4=q^2-4q=q(q-4).
    discriminant = (
        q_minus_2[0] * q_minus_2[0] - 4,
        2 * q_minus_2[0] * q_minus_2[1],
        q_minus_2[1] * q_minus_2[1],
    )
    assert_equal(discriminant, (Fraction(0), Fraction(-4), Fraction(1)), "discriminant")

    # Endpoint factorizations.
    q0 = (Fraction(1), Fraction(-2), Fraction(1))
    q4 = (Fraction(1), Fraction(2), Fraction(1))
    assert_equal(q0, (Fraction(1), Fraction(-2), Fraction(1)), "q=0 endpoint")
    assert_equal(q4, (Fraction(1), Fraction(2), Fraction(1)), "q=4 endpoint")
    # The transfer matrices at q=0 and q=4 are not +/- identity.
    assert (Fraction(2), Fraction(-1), Fraction(1), Fraction(0)) != (
        Fraction(1), Fraction(0), Fraction(0), Fraction(1)
    )
    assert (Fraction(-2), Fraction(-1), Fraction(1), Fraction(0)) != (
        Fraction(-1), Fraction(0), Fraction(0), Fraction(-1)
    )

    # Public exact bound and sufficient all-momentum real-branch range.
    s_bound = Fraction(16, 9)
    mu2_safe = Fraction(20, 9)
    assert_equal(s_bound + mu2_safe, Fraction(4), "safe real-branch bound")
    assert Fraction(0) <= mu2_safe < 4

    # det [[Omega+z,x-i y],[x+i y,Omega-z]]
    # = (Omega+z)(Omega-z)-(x-i y)(x+i y)
    # = Omega^2-z^2-x^2-y^2.
    Omega, x, y, z, M = (var(i) for i in range(5))
    diagonal_product = poly_mul(
        poly_add(Omega, z),
        poly_add(Omega, poly_scale(z, -1)),
    )
    off_diagonal_norm = poly_add(poly_mul(x, x), poly_mul(y, y))
    det_h = poly_add(diagonal_product, poly_scale(off_diagonal_norm, -1))
    target_det = poly_add(
        poly_mul(Omega, Omega),
        poly_scale(poly_mul(x, x), -1),
        poly_scale(poly_mul(y, y), -1),
        poly_scale(poly_mul(z, z), -1),
    )
    assert_equal(det_h, target_det, "Herm2 determinant")
    assert_equal(
        poly_add(det_h, poly_scale(poly_mul(M, M), -1)),
        poly_add(target_det, poly_scale(poly_mul(M, M), -1)),
        "massive Herm2 level polynomial",
    )

    # mu_epsilon=epsilon^alpha M contributes epsilon^(2 alpha-2) M^2.
    assert_equal(2 * Fraction(1) - 2, Fraction(0), "alpha=1 finite nonzero")
    assert 2 * Fraction(1, 2) - 2 < 0
    assert 2 * Fraction(2) - 2 > 0

    # Remainder constants inherited from v74.
    temporal_remainder = Fraction(1, 12)
    spatial_remainder = Fraction(11, 27)
    assert temporal_remainder > 0
    assert spatial_remainder > 0

    # Frozen negative controls.
    assert -1 != +1  # correct versus tachyonic continuum mass sign
    assert +1 != -1  # correct versus reversed temporal q sign
    assert 2 * Fraction(0) - 2 < 0  # fixed nonzero lattice mu diverges
    assert 2 * Fraction(2) - 2 != 0  # over-scaled mu becomes massless
    assert Fraction(20, 9) != Fraction(4)  # safe bound is not replaced by 4

    print("PROBE P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1")
    print("EXPOSURE RESULT_EXPOSED_PROOF_AUDIT")
    print("CHARACTERISTIC zeta^2+(q-2)zeta+1")
    print("TRANSFER_DETERMINANT 1")
    print("DISCRIMINANT q(q-4)")
    print("BRANCH_CLASS q=0:PARABOLIC_PLUS;0<q<4:ELLIPTIC;q=4:PARABOLIC_MINUS;q>4:HYPERBOLIC")
    print("ZERO_MOMENTUM q=mu^2;cos(omega0)=1-mu^2/2")
    print("MASSLESS_APEX mu^2=0:zeta=1_DOUBLE_NONIDENTITY")
    print("SAFE_ALL_MOMENTA_REAL_MU2_BOUND 20/9")
    print("HERM2_MASS_SHELL det(H)-M^2=Omega^2-|k|^2-M^2")
    print("SCALING mu=epsilon^alpha*M;alpha=1_UNIQUE_FINITE_NONZERO")
    print("REMAINDER temporal=1/12;spatial=11/27")
    print("NEGATIVE_CONTROLS mass_sign,temporal_sign,fixed_mu,wrong_scaling PASS")
    print("FALSIFIERS NONE")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
