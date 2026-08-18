#!/usr/bin/env python3
"""Breaker for C-ENTANGLEMENT-RELATIONAL-WEDGE-1-N.

Written from PREREG.md before comparison with any positive verifier.
Uses exact SymPy arithmetic only. It attacks scope overreach, not the
already-public QPAIR-SYM2-TENSOR-DEFECT theorem.
"""
from sympy import Matrix, Rational, I, simplify


def partial_transpose_B(rho: Matrix) -> Matrix:
    out = Matrix.zeros(4, 4)
    for a in range(2):
        for b in range(2):
            for ap in range(2):
                for bp in range(2):
                    i = 2*a + b
                    j = 2*ap + bp
                    ii = 2*a + bp
                    jj = 2*ap + b
                    out[ii, jj] = rho[i, j]
    return out


def main() -> int:
    # B1 mixed-state breaker: Werner p=1/2.
    p = Rational(1, 2)
    psi = Matrix([0, 1, -1, 0]) / 2**Rational(1, 2)
    singlet = psi * psi.conjugate().T
    rho = p * singlet + (1-p) * Matrix.eye(4) / 4
    pt = partial_transpose_B(rho)
    pt_eigs = sorted([simplify(ev) for ev in pt.eigenvals().keys()], key=str)
    assert Rational(-1, 8) in pt_eigs
    # Werner correlation matrix is -p I_3, so Horodecki top-two sum is 2 p^2.
    M_chsh = 2 * p**2
    assert M_chsh == Rational(1, 2) < 1
    print("B1 PASS mixed breaker: Werner p=1/2 is PPT-negative but CHSH-subcritical")

    # B2 higher-Schmidt-rank breaker: same e2, different Schmidt spectra/rank.
    lam_A = [Rational(1,2), Rational(1,2), Rational(0)]
    lam_B = [Rational(2,3), Rational(1,6), Rational(1,6)]
    def e2(lam):
        return sum(lam[i]*lam[j] for i in range(3) for j in range(i+1,3))
    assert sum(lam_A) == sum(lam_B) == 1
    assert e2(lam_A) == e2(lam_B) == Rational(1,4)
    assert sum(x != 0 for x in lam_A) == 2
    assert sum(x != 0 for x in lam_B) == 3
    print("B2 PASS higher-rank breaker: equal exterior-2 scalar e2=1/4, different Schmidt spectra")

    # B3 local-basis phase breaker.
    A = Matrix([[1, 0], [0, 1]])
    U = Matrix([[I, 0], [0, 1]])
    V = Matrix.eye(2)
    d0 = A.det()
    d1 = (U*A*V.T).det()
    assert d0 == 1 and d1 == I
    assert simplify(d1 * d1.conjugate() - d0 * d0.conjugate()) == 0
    print("B3 PASS phase breaker: U(2) changes determinant phase while preserving modulus")

    print("BREAKER PASS: pure-2x2 scope is necessary; mixed/universal scalar readings are false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
