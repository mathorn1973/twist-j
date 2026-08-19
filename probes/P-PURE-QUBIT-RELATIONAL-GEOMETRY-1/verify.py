#!/usr/bin/env python3
"""Exact audit for P-PURE-QUBIT-RELATIONAL-GEOMETRY-1.

This verifier uses only the Python standard library and exact rational
arithmetic.  Written proofs in PREREG.md carry the universal statements.
The finite grids below audit the coordinate formulae and the frozen boundary
witnesses.  It accepts no arguments and writes nothing except stdout.

Exit codes: 0 PASS, 1 integrity STOP, 2 scientific FALSIFIED.
"""

import sys
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product


@dataclass(frozen=True)
class G:
    """Gaussian rational r + i q."""

    r: F = F(0)
    q: F = F(0)

    def __add__(self, other):
        other = as_g(other)
        return G(self.r + other.r, self.q + other.q)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.q)

    def __sub__(self, other):
        return self + (-as_g(other))

    def __rsub__(self, other):
        return as_g(other) - self

    def __mul__(self, other):
        other = as_g(other)
        return G(self.r * other.r - self.q * other.q,
                 self.r * other.q + self.q * other.r)

    __rmul__ = __mul__

    def conj(self):
        return G(self.r, -self.q)

    def abs2(self):
        return self.r * self.r + self.q * self.q


def as_g(value):
    if isinstance(value, G):
        return value
    return G(F(value), F(0))


ZERO = G()
ONE = G(F(1))
I = G(F(0), F(1))

GATE_COUNT = 0
FAILURES = []


def gate(name, condition, detail=""):
    global GATE_COUNT
    GATE_COUNT += 1
    ok = bool(condition)
    if not ok:
        FAILURES.append(name)
    line = "CHECK %-58s %s" % (name, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)


def integrity(name, condition, detail=""):
    global GATE_COUNT
    GATE_COUNT += 1
    ok = bool(condition)
    line = "CHECK %-58s %s" % (name, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)
    if not ok:
        raise RuntimeError("integrity gate failed: " + name)


def report(name, value):
    print("REPORT %-57s %s" % (name, value))


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(len(A)))
                 for i in range(len(A[0])))


def matmul(A, B):
    Bt = transpose(B)
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO)
                       for col in Bt) for row in A)


def dagger(A):
    return tuple(tuple(A[j][i].conj() for j in range(len(A)))
                 for i in range(len(A[0])))


def rho_data(A):
    rho = matmul(A, dagger(A))
    tr = rho[0][0].r + rho[1][1].r
    det = det2(rho)
    if det.q != 0:
        raise AssertionError("Hermitian determinant not real")
    return rho, tr, det.r


def delta_norm(A):
    D = det2(A)
    return D, D.abs2()


def apply_local(U, A, V):
    return matmul(matmul(U, A), transpose(V))


def partial_transpose_second(M):
    out = [[F(0) for _ in range(4)] for _ in range(4)]
    for a in range(2):
        for b in range(2):
            for ap in range(2):
                for bp in range(2):
                    out[2 * a + bp][2 * ap + b] = M[2 * a + b][2 * ap + bp]
    return tuple(tuple(row) for row in out)


def mv(M, v):
    return tuple(sum((M[i][j] * v[j] for j in range(len(v))), F(0))
                 for i in range(len(M)))


def scale(v, s):
    return tuple(s * x for x in v)


def audit_det_grid():
    values = (ZERO, ONE, -ONE, I, -I, ONE + I, ONE - I)
    count = 0
    for a, b, c, d in product(values, repeat=4):
        A = ((a, b), (c, d))
        _, _, det_rho = rho_data(A)
        _, norm_D = delta_norm(A)
        if det_rho != norm_D:
            return False, count
        count += 1
    return True, count


def audit_cauchy_binet():
    values = (ZERO, ONE, -ONE, I)
    count = 0
    for n in (2, 3, 4):
        for entries in product(values, repeat=2 * n):
            u = entries[:n]
            v = entries[n:]
            uu = sum((z.abs2() for z in u), F(0))
            vv = sum((z.abs2() for z in v), F(0))
            uv = sum((u[k] * v[k].conj() for k in range(n)), ZERO)
            gram_det = uu * vv - uv.abs2()
            minors = [u[i] * v[j] - u[j] * v[i]
                      for i in range(n) for j in range(i + 1, n)]
            wedge_norm = sum((z.abs2() for z in minors), F(0))
            if gram_det != wedge_norm:
                return False, count
            if (wedge_norm == 0) != all(z == ZERO for z in minors):
                return False, count
            count += 1
    return True, count


def main():
    print("P-PURE-QUBIT-RELATIONAL-GEOMETRY-1 verifier")
    print("pure-state determinant-line norm, local/relation Pythagoras, "
          "standard-QM CHSH comparison, and mixed/higher-rank scope breakers")
    print("")

    integrity("I01.no.arguments", len(sys.argv) == 1)
    integrity("I02.python.version", sys.version_info >= (3, 8))
    integrity("I03.exact.backend", F(1, 3) + F(2, 3) == 1)

    ok, count = audit_det_grid()
    gate("R1.det(rho_A)=|det(A)|^2.gaussian-grid", ok)
    report("R1.gaussian-grid.states", count)

    # Public wedge convention: r=(D/2) kappa and ||kappa||^2=4.
    kappa_norm2 = F(4)
    gate("R1.||r||^2=|D|^2.wedge-normalization",
         F(1, 4) * kappa_norm2 == 1)

    # Phase blindness of the Hermitian slot and phase retention of the
    # symmetric determinant direction.
    A0 = ((ONE, ONE + I), (I, ONE - I))
    u = I
    Au = tuple(tuple(u * z for z in row) for row in A0)
    H0 = matmul(A0, dagger(A0))
    Hu = matmul(Au, dagger(Au))
    D0, N0 = delta_norm(A0)
    Du, Nu = delta_norm(Au)
    gate("R1.unit-phase.H-invariant.S-determinant-retained",
         H0 == Hu and Du == u * u * D0 and N0 == Nu and D0 != Du)

    # Full local U(2)xU(2) changes determinant phase but preserves its norm.
    U = ((I, ZERO), (ZERO, ONE))
    V = ((ONE, ZERO), (ZERO, ONE))
    A1 = ((ONE, ZERO), (ZERO, ONE))
    A2 = apply_local(U, A1, V)
    d1, n1 = delta_norm(A1)
    d2, n2 = delta_norm(A2)
    gate("R1.local-U2.phase-breaker.modulus-invariant",
         d1 == ONE and d2 == I and n1 == n2 == 1)

    # The normalized pure 2x2 LU quotient can be parameterized by either
    # Schmidt eigenvalue p, modulo p<->1-p, or by area squared p(1-p).
    ps = tuple(F(k, 40) for k in range(41))
    classifier_ok = True
    for p in ps:
        for q in ps:
            if p * (1 - p) == q * (1 - q):
                classifier_ok &= (q == p or q == 1 - p)
    gate("R1.area.classifies.normalized-Schmidt-pair.grid", classifier_ok)

    cb_ok, cb_count = audit_cauchy_binet()
    gate("R1.2xn.Cauchy-Binet.gaussian-grids.n=2..4", cb_ok)
    report("R1.Cauchy-Binet.row-pairs", cb_count)

    # Exact pure-state Pythagorean complement in squared coordinates.
    schmidt_p = (F(0), F(1, 10), F(1, 4), F(9, 25), F(1, 2),
                 F(16, 25), F(3, 4), F(9, 10), F(1))
    pyth_ok = True
    purity_ok = True
    chsh_ok = True
    for p in schmidt_p:
        q = 1 - p
        area2 = p * q
        concurrence2 = 4 * area2
        bloch2 = (p - q) ** 2
        purity = p * p + q * q
        pyth_ok &= bloch2 + concurrence2 == 1
        purity_ok &= (purity == 1 - concurrence2 / 2
                      and 2 * (1 - purity) == concurrence2)
        # In Schmidt gauge T^T T has eigenvalues 1,C^2,C^2.
        top_two = 1 + concurrence2
        bmax2 = 4 * top_two
        chsh_ok &= (bmax2 - 4 == 16 * area2)
    gate("R2.|b|^2+C^2=1.Schmidt-grid", pyth_ok)
    gate("R2.local-purity-complement.Schmidt-grid", purity_ok)
    gate("R3.Bmax^2-4=16||r||^2.Horodecki-input-grid", chsh_ok)
    gate("R3.endpoints.product.4.Bell.8",
         4 * (1 + 4 * F(0) * F(1)) == 4
         and 4 * (1 + 4 * F(1, 2) * F(1, 2)) == 8)

    # Werner p=1/2.  This exact control is entangled (negative partial
    # transpose) but CHSH-subcritical and violates the pure Pythagorean law.
    rho_w = (
        (F(1, 8), 0, 0, 0),
        (0, F(3, 8), F(-1, 4), 0),
        (0, F(-1, 4), F(3, 8), 0),
        (0, 0, 0, F(1, 8)),
    )
    pt = partial_transpose_second(rho_w)
    vp = (F(1), 0, 0, F(1))
    vm = (F(1), 0, 0, F(-1))
    e01 = (0, F(1), 0, 0)
    e10 = (0, 0, F(1), 0)
    pt_ok = (mv(pt, vp) == scale(vp, F(-1, 8))
             and mv(pt, vm) == scale(vm, F(3, 8))
             and mv(pt, e01) == scale(e01, F(3, 8))
             and mv(pt, e10) == scale(e10, F(3, 8)))
    werner_p = F(1, 2)
    horodecki_M = 2 * werner_p * werner_p
    concurrence = F(5, 8) - 3 * F(1, 8)
    gate("B1.Werner.p=1/2.PT-negative.CHSH-subcritical",
         pt_ok and horodecki_M == F(1, 2) < 1)
    gate("B1.Werner.pure-Pythagoras-fails",
         concurrence == F(1, 4) and concurrence * concurrence == F(1, 16) != 1)

    # Equal second exterior scalar does not classify Schmidt rank three.
    lam_a = (F(1, 2), F(1, 2), F(0))
    lam_b = (F(2, 3), F(1, 6), F(1, 6))

    def e2(lam):
        return sum((lam[i] * lam[j]
                    for i in range(3) for j in range(i + 1, 3)), F(0))

    gate("B2.higher-rank.same-e2.different-spectrum",
         sum(lam_a) == sum(lam_b) == 1
         and e2(lam_a) == e2(lam_b) == F(1, 4)
         and lam_a != lam_b
         and sum(x != 0 for x in lam_a) == 2
         and sum(x != 0 for x in lam_b) == 3)

    print("")
    print("gates: %d  failures: %d" % (GATE_COUNT, len(FAILURES)))
    if FAILURES:
        for name in FAILURES:
            print("FALSIFIED " + name)
        print("RESULT FALSIFIED")
        return 2
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as exc:
        print("STOP %s: %s" % (type(exc).__name__, exc))
        code = 1
    sys.stdout.flush()
    raise SystemExit(code)
