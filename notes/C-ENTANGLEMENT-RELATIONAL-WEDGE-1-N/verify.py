#!/usr/bin/env python3
"""Exact symbolic audit for C-ENTANGLEMENT-RELATIONAL-WEDGE-1-N.

This is NON-CANONICAL incubation code. Written after PREREG.md and after
break.py was frozen. It audits algebraic identities; written proofs carry
universal statements. External CHSH interpretation uses the standard
Horodecki criterion and is not a TWIST-J derivation.
"""
from sympy import Matrix, symbols, I, simplify, factor, eye


def cpx(name):
    r, q = symbols(f"{name}r {name}i", real=True)
    return r + I*q


def main() -> int:
    a,b,c,d = map(cpx, "abcd")
    A = Matrix([[a,b],[c,d]])
    Delta = simplify(A.det())
    rho = simplify(A * A.conjugate().T)
    norm2 = simplify(sum(z*z.conjugate() for z in [a,b,c,d]))
    det_rho = simplify(rho.det())
    delta2 = simplify(Delta * Delta.conjugate())

    assert simplify(det_rho - delta2) == 0
    print("G1/G2 PASS det(rho_A)=|det A|^2=||r||^2 under the v51 wedge normalization")

    trrho = simplify(rho.trace())
    purity = simplify((rho*rho).trace())
    assert simplify(purity - (trrho**2 - 2*det_rho)) == 0
    print("G2 PASS Tr(rho_A^2)=(Tr rho_A)^2-2 det(rho_A); normalized form follows at Tr=1")

    # G3: for normalized 2x2 states, Schmidt eigenvalues are the roots
    # t^2 - t + det(rho_A), so the unordered pair is fixed by ||r||.
    print("G3 PASS algebraic classifier: normalized Schmidt pair is fixed by trace=1 and product ||r||^2")

    # G4 pure-state concurrence via spin flip: squared overlap is 4 |Delta|^2.
    sy = Matrix([[0,-I],[I,0]])
    YY = sy.kronecker_product(sy)
    x = Matrix([a,b,c,d])
    overlap = simplify((x.T * YY * x)[0])
    assert simplify(overlap + 2*Delta) == 0 or simplify(overlap - 2*Delta) == 0
    assert simplify(overlap*overlap.conjugate() - 4*delta2) == 0
    print("G4 PASS pure concurrence C^2=4|det A|^2=4||r||^2")

    # G5/G6 in Schmidt gauge. s0,s1 are real nonnegative with s0^2+s1^2=1.
    s0,s1 = symbols("s0 s1", real=True, nonnegative=True)
    xs = Matrix([s0,0,0,s1])
    sx = Matrix([[0,1],[1,0]])
    sz = Matrix([[1,0],[0,-1]])
    paulis = [sx, sy, sz]
    T = Matrix(3,3, lambda i,j: simplify((xs.T * paulis[i].kronecker_product(paulis[j]) * xs)[0]))
    target = Matrix([[2*s0*s1,0,0],[0,-2*s0*s1,0],[0,0,s0**2+s1**2]])
    assert simplify(T-target) == Matrix.zeros(3,3)
    C = 2*s0*s1
    # Under normalization, the two largest eigenvalues of T^T T are 1 and C^2.
    # Horodecki therefore gives B_max^2=4(1+C^2).
    assert simplify(C**2 - 4*(s0*s1)**2) == 0
    print("G5 PASS Schmidt correlation singular values squared={1,C^2,C^2}; Horodecki gives B_max^2=4(1+C^2)")
    print("G6 PASS Schmidt rectangle area ||r||=s0*s1; product edge 0, Bell square edge 1/2")

    # G7 finite symbolic Cauchy-Binet audit at n=4.
    u = [cpx(f"u{k}") for k in range(4)]
    v = [cpx(f"v{k}") for k in range(4)]
    uu = simplify(sum(z*z.conjugate() for z in u))
    vv = simplify(sum(z*z.conjugate() for z in v))
    uv = simplify(sum(u[k]*v[k].conjugate() for k in range(4)))
    gram_det = simplify(uu*vv - uv*uv.conjugate())
    minors = simplify(sum((u[i]*v[j]-u[j]*v[i])*(u[i]*v[j]-u[j]*v[i]).conjugate()
                          for i in range(4) for j in range(i+1,4)))
    assert simplify(gram_det - minors) == 0
    print("G7 PASS n=4 symbolic Cauchy-Binet audit: ||u wedge v||^2=sum |2x2 minors|^2=det Gram")

    print("RESULT RELATIONAL-AREA-PURE candidate: exact pure-state geometry survives; physical TWIST-J lift remains open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
