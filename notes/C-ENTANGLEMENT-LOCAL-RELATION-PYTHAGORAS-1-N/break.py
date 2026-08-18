#!/usr/bin/env python3
"""Exact mixed-state breaker for C-ENTANGLEMENT-LOCAL-RELATION-PYTHAGORAS-1-N."""
from sympy import Matrix, Rational, sqrt, I, kronecker_product


def main() -> int:
    p = Rational(1,2)
    psi = Matrix([0,1,-1,0]) / sqrt(2)
    rho = p*(psi*psi.T) + (1-p)*Matrix.eye(4)/4

    # Every Werner marginal is maximally mixed.
    rhoA = Matrix([
        [rho[0,0]+rho[1,1], rho[0,2]+rho[1,3]],
        [rho[2,0]+rho[3,1], rho[2,2]+rho[3,3]],
    ])
    assert rhoA == Matrix.eye(2)/2
    bloch2 = 0

    # Exact Wootters spin flip. The Werner singlet state is spin-flip invariant,
    # so rho_tilde=rho and the square roots of eig(rho*rho_tilde) are the
    # Bell-diagonal eigenvalues of rho: 5/8,1/8,1/8,1/8.
    sy = Matrix([[0,-I],[I,0]])
    YY = kronecker_product(sy,sy)
    rho_tilde = YY * rho.conjugate() * YY
    assert rho_tilde == rho
    eigs = rho.eigenvals()
    assert eigs == {Rational(5,8):1, Rational(1,8):3}
    C = Rational(5,8) - 3*Rational(1,8)
    assert C == Rational(1,4)
    assert bloch2 + C**2 == Rational(1,16) != 1

    print("B1 PASS Werner p=1/2: |b|^2=0, C=1/4, sum=1/16 != 1")
    print("BREAKER PASS: Pythagorean equality cannot be universalized to mixed states")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
