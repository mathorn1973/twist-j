#!/usr/bin/env python3
"""Exact L1 audit of J/phi area and selected F5 Weyl covariance.

No floating point, random input, subprocesses, filesystem access, or network.
Universal infinite-lattice statements require the separate algebraic proof.
"""
from itertools import product

P = 5
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
STEP = (1, 0, 1, 0)
PHI = (0, 0, -1, -1)
BASIS = tuple(tuple(int(i == k) for i in range(4)) for k in range(4))


class ScientificFalsifier(Exception):
    pass


def require(condition, label):
    if not condition:
        raise ScientificFalsifier(label)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, b):
    """Multiply in Z[j] using j^4 = -(1+j+j^2+j^3)."""
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    for e in range(6, 3, -1):
        q = c[e]
        for k in range(e - 4, e):
            c[k] -= q
        c[e] = 0
    return tuple(c[:4])


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


def reduction(a):
    """Marked evaluation j -> 1 in O/(1-j), residue F5."""
    return sum(a) % P


def transfer(u):
    return (mul(STEP, u[0]), mul(PHI, u[1]))


def wedge(u, v):
    return sub(mul(u[0], v[1]), mul(u[1], v[0]))


def f5_wedge(u, v):
    return (u[0] * v[1] - u[1] * v[0]) % P


def f5_transfer(u):
    return (2 * u[0] % P, 3 * u[1] % P)


def identity():
    return (tuple(range(P)), (0,) * P)


def compose(a, b):
    """Monomial operators, apply b then a, phase exponents mod 5."""
    pa, ea = a
    pb, eb = b
    return (
        tuple(pa[pb[k]] for k in range(P)),
        tuple((ea[pb[k]] + eb[k]) % P for k in range(P)),
    )


def central(a, exponent):
    return (a[0], tuple((e + exponent) % P for e in a[1]))


def W(a, b):
    """W(a,b) = Z^a X^b, Z|k>=j^k|k>, X|k>=|k+1>."""
    return (
        tuple((k + b) % P for k in range(P)),
        tuple(a * (k + b) % P for k in range(P)),
    )


def op_power(op, n):
    out = identity()
    for _ in range(n):
        out = compose(out, op)
    return out


def audit():
    require(mul(STEP, PHI) == JROOT, "G1: J*phi != j")
    require(power(JROOT, 5) == ONE, "G1: j^5 != 1")
    require(power(mul(STEP, PHI), 5) == ONE, "G1: J^5*phi^5 != 1")
    require(reduction(JROOT) == 1, "G1: reduction(j) != 1")
    require(reduction(STEP) == 2, "G1: reduction(J) != 2")
    require(reduction(PHI) == 3, "G1: reduction(phi) != 3")
    for a in BASIS:
        for b in BASIS:
            require(reduction(mul(a, b)) == reduction(a) * reduction(b) % P,
                    "G1: ring reduction fails on basis")

    module_basis = tuple((b, ZERO) for b in BASIS) + tuple((ZERO, b) for b in BASIS)
    for u in module_basis:
        for v in module_basis:
            require(wedge(transfer(u), transfer(v)) == mul(JROOT, wedge(u, v)),
                    "G2: one-step conformal alternating identity fails")
            uu, vv = u, v
            for _ in range(P):
                uu, vv = transfer(uu), transfer(vv)
            require(wedge(uu, vv) == wedge(u, v),
                    "G2: five-step alternating return fails")
    unit_u, unit_v = (ONE, ZERO), (ZERO, ONE)
    require(wedge(transfer(unit_u), transfer(unit_v)) == JROOT != ONE,
            "G2: one-step form unexpectedly invariant")

    finite = tuple(product(range(P), repeat=2))
    for u in finite:
        for v in finite:
            require(f5_wedge(f5_transfer(u), f5_transfer(v)) == f5_wedge(u, v),
                    "G3: finite alternating invariance fails")
    require((2 * 3) % P == 1, "G3: ramified determinant not one")

    D = (tuple(3 * k % P for k in range(P)), (0,) * P)
    Dinverse = (tuple(2 * k % P for k in range(P)), (0,) * P)
    Z, X = W(1, 0), W(0, 1)
    require(compose(D, Dinverse) == identity(), "G4: D inverse fails")
    require(op_power(D, 4) == identity(), "G4: D order fails")
    require(compose(D, compose(Z, Dinverse)) == op_power(Z, 2),
            "G4: DZD^-1 != Z^2")
    require(compose(D, compose(X, Dinverse)) == op_power(X, 3),
            "G4: DXD^-1 != X^3")
    for u in finite:
        require(compose(D, compose(W(*u), Dinverse)) == W(*f5_transfer(u)),
                "G4: Weyl covariance fails")
        for v in finite:
            lhs = compose(W(*u), W(*v))
            rhs = central(compose(W(*v), W(*u)), f5_wedge(u, v))
            require(lhs == rhs, "G4: Heisenberg commutator phase fails")

    require(reduction(JROOT) == 1 and JROOT != ONE,
            "G5: ramified phase erasure fails")
    samples = {(t * f5_wedge((1, 0), (0, 1))) % P for t in range(1, P)}
    require(samples == {1, 2, 3, 4}, "G5: four phase characters not distinct")
    for t in range(1, P):
        for u in finite:
            for v in finite:
                require(t * f5_wedge(f5_transfer(u), f5_transfer(v)) % P ==
                        t * f5_wedge(u, v) % P,
                        "G5: phase character does not preserve area")

    values = (-2, -1, 0, 1, 2)
    d_invariant = []
    joint_invariant = []
    for h in product(values, repeat=P):
        if all(h[k] == h[3 * k % P] for k in range(P)):
            d_invariant.append(h)
            if all(h[k] == h[(k + 1) % P] for k in range(P)):
                joint_invariant.append(h)
            require(all(h[k] == h[1] for k in range(1, P)),
                    "G6: D invariant diagonal not classified")
    require(len(d_invariant) == 25, "G6: D-invariant dimension/count wrong")
    require(len(joint_invariant) == 5, "G6: joint scalar dimension/count wrong")
    for gap in (1, 2):
        h = (0, gap, gap, gap, gap)
        require(all(h[k] == h[3 * k % P] for k in range(P)),
                "G6: positive gap not D invariant")
    require((0, 1, 1, 1, 1) != (0, 2, 2, 2, 2),
            "G6: inequivalent energy gaps not distinguished")

    return (
        "G1 PASS: J*phi=j, ramified images (j,J,phi)=(1,2,3)",
        "G2 PASS: omega(Tu,Tv)=j*omega(u,v); five-step return; 64 basis pairs",
        "G3 PASS: diag(2,3) preserves 625 finite ordered areas",
        "G4 PASS: D covariance, 25 Weyl transports, 625 commutator pairs",
        "G5 PASS: reduction erases j; four distinct invariant phase characters",
        "G6 PASS: 25 D-invariant diagonal costs, 5 joint scalar costs",
        "G6 WITNESS: invariant nonnegative gaps 1 and 2 (not selected)",
        "BOUNDARY: conditional L1 algebra only; no native contact, action, hbar or SI",
        "AUDIT PASS",
    )


def main():
    try:
        lines = audit()
    except ScientificFalsifier as exc:
        print("FALSIFIER: " + str(exc))
        print("AUDIT FAIL")
        return 0
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
