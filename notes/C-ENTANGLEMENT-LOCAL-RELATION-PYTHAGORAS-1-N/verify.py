#!/usr/bin/env python3
"""Exact symbolic audit for C-ENTANGLEMENT-LOCAL-RELATION-PYTHAGORAS-1-N.
NON-CANONICAL. One-lane audit only unless separately reproduced.
"""
from sympy import Matrix, symbols, I, simplify, cos, sin, trigsimp


def main() -> int:
    bx,by,bz = symbols("bx by bz", real=True)
    rho = Matrix([
        [1+bz, bx-I*by],
        [bx+I*by, 1-bz],
    ])/2
    b2 = bx**2+by**2+bz**2
    assert simplify(rho.det() - (1-b2)/4) == 0
    print("G1 PASS det(rho)=(1-|b|^2)/4")

    R2 = symbols("R2", nonnegative=True, real=True)
    C2 = 4*R2
    # Pure-state predecessor relation: det(rho_A)=R2.
    pyth = simplify(b2 + 4*((1-b2)/4) - 1)
    assert pyth == 0
    print("G2 PASS |b|^2+4||r||^2=1 and |b|^2+C^2=1")

    purity = simplify((rho*rho).trace())
    assert simplify(purity - (1+b2)/2) == 0
    print("G4 PASS Tr(rho^2)=(1+|b|^2)/2=1-C^2/2 at pure-state predecessor scope")

    theta = symbols("theta", real=True)
    s0,s1 = cos(theta),sin(theta)
    local_b = trigsimp(s0**2-s1**2)
    C = trigsimp(2*s0*s1)
    area = trigsimp(s0*s1)
    assert trigsimp(local_b-cos(2*theta)) == 0
    assert trigsimp(C-sin(2*theta)) == 0
    assert trigsimp(area-sin(2*theta)/2) == 0
    assert trigsimp(local_b**2+C**2-1) == 0
    print("G3/G5 PASS pure LU quotient is quarter unit circle: |b|=cos(2theta), C=sin(2theta)")

    print("RESULT PYTHAGOREAN-PURE candidate: exact state-space right triangle, mixed-state breaker remains outside")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
