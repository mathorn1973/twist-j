#!/usr/bin/env python3
"""Exact L1 audit for P-C8-PAULI-QUOTIENT-TRANSPORT-1.

Only standard-library rational arithmetic, F25 pairs and Q[z]/(z^4+1).
No numerical approximation, external input, filesystem, network or randomness.
Universal scopes are proved in PREREG.md; finite bases/residues are audited here.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd

Scalar = tuple[F, F, F, F]
Matrix = tuple[tuple[Scalar, ...], ...]
ZERO: Scalar = (F(0), F(0), F(0), F(0))
ONE: Scalar = (F(1), F(0), F(0), F(0))


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def const(n: int, d: int = 1) -> Scalar:
    return (F(n, d), F(0), F(0), F(0))


def root(n: int) -> Scalar:
    n %= 8
    a = [F(0)] * 4
    a[n % 4] = F(1 if n < 4 else -1)
    return tuple(a)


def add(a: Scalar, b: Scalar) -> Scalar:
    return tuple(a[j] + b[j] for j in range(4))


def scale(a: Scalar, n: int, d: int = 1) -> Scalar:
    return tuple(F(n, d) * c for c in a)


def mul(a: Scalar, b: Scalar) -> Scalar:
    c = [F(0)] * 7
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            c[j + k] += x * y
    return tuple(c[j] - (c[j + 4] if j < 3 else 0) for j in range(4))


def total(items) -> Scalar:
    out = ZERO
    for a in items:
        out = add(out, a)
    return out


def conj(a: Scalar) -> Scalar:
    return total(tuple(c * x for x in root(-j)) for j, c in enumerate(a))


def mmul(a: Matrix, b: Matrix) -> Matrix:
    need(len(a[0]) == len(b), "matrix dimensions")
    return tuple(tuple(total(mul(a[i][k], b[k][j]) for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def dagger(a: Matrix) -> Matrix:
    return tuple(tuple(conj(a[i][j]) for i in range(len(a)))
                 for j in range(len(a[0])))


def mscale(a: Matrix, c: Scalar) -> Matrix:
    return tuple(tuple(mul(x, c) for x in row) for row in a)


def madd(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(add(x, y) for x, y in zip(ar, br))
                 for ar, br in zip(a, b))


def trace(a: Matrix) -> Scalar:
    return total(a[j][j] for j in range(len(a)))


def kron(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(mul(a[i][j], b[k][l])
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def act(u: Matrix, a: Matrix) -> Matrix:
    return mmul(mmul(u, a), dagger(u))


def phase(k: int) -> Matrix:
    return ((ONE, ZERO), (ZERO, root(k)))


I = phase(0)
X = ((ZERO, ONE), (ONE, ZERO))
Y = ((ZERO, root(-2)), (root(2), ZERO))
Z = phase(4)


def state(k: int) -> Matrix:
    return ((const(1, 2), scale(root(-k), 1, 2)),
            (scale(root(k), 1, 2), const(1, 2)))


def bell(c: Scalar) -> Matrix:
    a = [[ZERO for _ in range(4)] for _ in range(4)]
    a[0][0] = a[3][3] = const(1, 2)
    a[0][3] = scale(conj(c), 1, 2)
    a[3][0] = scale(c, 1, 2)
    return tuple(tuple(row) for row in a)


def fmul(x, y):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % 5, (a * d + b * c) % 5)


def fpow(x, n: int):
    if n < 0:
        raise ValueError("nonnegative field exponent required")
    out = (1, 0)
    while n:
        if n & 1:
            out = fmul(out, x)
        x = fmul(x, x)
        n >>= 1
    return out


def main() -> None:
    e = tuple(k for k in range(8) if gcd(k, 8) == 1)
    need(e == (1, 3, 5, 7), "C8 generators")
    need(mul(root(1), root(3)) == root(4), "cyclotomic reduction")
    for k in range(8):
        need(mul(root(k), conj(root(k))) == ONE, "complex root norm")
    for a in (I, X, Y, Z):
        need(dagger(a) == a and mmul(a, a) == I, "Pauli matrices")

    fibres = tuple(tuple(k for k in e if (2 * k) % 8 == r) for r in (2, 6))
    need(fibres == ((1, 5), (3, 7)), "restriction fibres")
    for k, l in product(e, repeat=2):
        same = any(phase(k) == mmul(p, phase(l)) for p in (I, Z))
        need(same == ((k - l) % 4 == 0), "left-Z equality")
        pauli_same = any(phase(k) == mscale(mmul(p, phase(l)), root(t))
                         for p in (I, X, Y, Z) for t in range(8))
        need(pauli_same == same, "left-Pauli equality on diagonal family")
    for k in e:
        need(phase(k + 4) == mmul(Z, phase(k)), "branch is left Z")
        need(mmul(mmul(X, phase(k)), X) == mscale(phase(-k), root(k)),
             "additional X frame conjugation")
        need({k, (k + 4) % 8, (-k) % 8, (-k + 4) % 8} == set(e),
             "frame-enlarged orbit")
    print("G1 PASS: two left-Z classes; extra X-frame equivalence would merge them")

    tau = (0, 1)
    hlog = {fpow(tau, n): n for n in range(8)}
    need(len(hlog) == 8 and fpow(tau, 2) == (2, 0), "source order and square")
    roots = {x for x in product(range(5), repeat=2) if fmul(x, x) == (2, 0)}
    need(roots == {(0, 1), (0, 4)}, "source root pair")
    log2 = {pow(2, n, 5): n for n in range(4)}

    def chi(k, x):
        return root(k * hlog[x])

    def beta(a):
        return root(2 * log2[a])

    for k in e:
        for x, y in product(hlog, repeat=2):
            need(chi(k, fmul(x, y)) == mul(chi(k, x), chi(k, y)),
                 "multiplicative character")
    extensions = tuple(k for k in e if all(chi(k, (a, 0)) == beta(a)
                                           for a in range(1, 5)))
    need(extensions == (1, 5), "conditional marked extension orbit")
    need(beta(2) == root(2) and beta(3) == root(6), "marked C4 character")
    print("G2 PASS: beta_plus(2)=i fixes one extension orbit, not one C8 lift")

    eta = fpow(tau, 3)

    def shadow(sign):
        r = fmul((sign % 5, 0), eta)
        ys = [fpow(r, s) for s in range(8)]
        return (tuple((pow(2, s, 5), 0) for s in range(8))
                + tuple(ys[s] for s in range(0, 8, 2))
                + tuple(fmul(ys[s], ys[t])
                        for s in range(1, 8, 2) for t in range(1, 8, 2)))

    v = shadow(1)
    need(v == shadow(-1), "complete registered shadow branch equality")
    need(len(v) == 28 and all(b == 0 and a != 0 for a, b in v), "shadow type")
    transported = {k: tuple(chi(k, x) for x in v) for k in e}
    for k in extensions:
        need(transported[k] == tuple(beta(a) for a, _ in v), "shadow transport")
    for k, l in product(e, repeat=2):
        need((transported[k] == transported[l]) == ((k - l) % 4 == 0),
             "complete transported-shadow fibres")
    need(transported[1][1] == root(2) and transported[3][1] == root(6),
         "Theta_1 orientation witness")
    need(all(c in {root(2 * j) for j in range(4)}
             for values in transported.values() for c in values), "mu4 outputs")
    for s in range(0, 8, 2):
        need(fpow(eta, s) == (pow(3, s // 2, 5), 0), "even all-residue law")
    for s, t in product(range(1, 8, 2), repeat=2):
        need(fmul(fpow(eta, s), fpow(eta, t)) == (pow(3, (s + t) // 2, 5), 0),
             "odd-pair all-residue law")
    print("G3 PASS: existing bilinear shadow descends exactly; all outputs lie in mu4")

    for k in e:
        for x, n in hlog.items():
            need(chi(k + 4, x) == scale(chi(k, x), (-1) ** n), "parity action")
            need((chi(k + 4, x) == chi(k, x)) == (n % 2 == 0),
                 "maximal invariant scalar subgroup")
        for s, t in product(range(8), repeat=2):
            a = fmul(fpow(eta, s), fpow(eta, t))
            need((chi(k + 4, a) == chi(k, a)) == ((s + t) % 2 == 0),
                 "common-branch product parity")
    need(chi(1, eta) != chi(5, eta), "mixed-parity non-descent witness")
    print("G4 PASS: even total degree descends; every odd-total-degree scalar separates branches")

    rho0 = ((ONE, ZERO), (ZERO, ZERO))
    rho1 = ((ZERO, ZERO), (ZERO, ONE))
    need(madd(rho0, rho1) == I, "density basis I")
    need(madd(rho0, mscale(rho1, const(-1))) == Z, "density basis Z")
    need(madd(mscale(state(0), const(2)), mscale(I, const(-1))) == X,
         "density basis X")
    need(madd(mscale(state(2), const(2)), mscale(I, const(-1))) == Y,
         "density basis Y")
    for a, sign in ((I, 1), (X, -1), (Y, -1), (Z, 1)):
        need(act(Z, a) == mscale(a, const(sign)), "exact commutant basis")
    for k in e:
        for a in (I, Z):
            need(act(dagger(phase(k)), a) == a, "diagonal read is phase-blind")
        out = act(phase(k), state(0))
        other = act(phase(k + 4), state(0))
        need(out == state(k) and other == state(k + 4), "coherent input")
        need(trace(out) == ONE and mmul(out, out) == out, "pure normalized state")
        need(out != other and trace(mmul(out, other)) == ZERO, "orthogonal branches")
        for bit in (0, 1):
            need(mmul(phase(4 * bit), phase(k + 4 * bit)) == phase(k),
                 "tracked correction is not forgotten correction")
    print("G5 PASS: fixed one-copy Z-blind linear reads are diagonal and phase-blind; gates differ")

    xy = kron(X, Y)
    zz = kron(Z, Z)
    zi = kron(Z, I)
    for k in e:
        u = kron(phase(k), phase(k))
        out = act(u, bell(ONE))
        sign = 1 if k % 4 == 1 else -1
        need(out == bell(root(2 * k)), "correlated two-use state")
        need(act(zz, out) == out, "common branch invariance")
        need(act(kron(phase(k + 4), phase(k + 4)), bell(ONE)) == out,
             "common character-branch shift")
        need(mmul(xy, out) == mscale(out, const(sign)), "deterministic XY read")
        need(trace(mmul(xy, out)) == const(sign), "two-use orientation output")
        need(trace(mmul(xy, act(zi, out))) == const(-sign),
             "independent branch counterexample")
    print("G6 PASS: common-branch two-use XY read separates orientations; independent branches fail")

    need(fpow(tau, 5) == (0, 4), "source Frobenius")
    need(fpow(tau, 6) == (3, 0), "finite-field norm")
    need(beta(3) == root(6) != ONE, "finite norm is not a Born norm")
    for k in e:
        need(chi(k, fpow(tau, 5)) != conj(chi(k, tau)), "involutions differ")
        need(mul(chi(k, tau), conj(chi(k, tau))) == ONE, "complex norm one")
    compatible = tuple(k for k in range(8) if root(5 * k) == root(-k))
    need(compatible == (0, 4), "only nonfaithful sign characters intertwine involutions")
    need(beta(2) != add(beta(1), beta(1)), "character is not additive")
    need(scale(ONE, 5) != ZERO and 5 % 5 == 0, "characteristic mismatch")
    print("G7 PASS: Frobenius is not complex conjugation; transport preserves no Born norm or field sum")
    print("RESULT 7/7 ALL PASS: conditional L1 readout transport only; no physical gauge or qubit bridge")


if __name__ == "__main__":
    main()
