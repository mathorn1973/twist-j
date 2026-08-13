#!/usr/bin/env python3
"""Exact G2 audit for the six TWIST-J golden projective lines.

No floating-point arithmetic and no external packages are used.  The base
field is Q(phi), phi^2 = phi + 1.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from math import factorial


@dataclass(frozen=True, order=True)
class F:
    """a + b*phi in Q(phi), with phi^2 = phi + 1."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __init__(self, a=0, b=0):
        object.__setattr__(self, "a", Fraction(a))
        object.__setattr__(self, "b", Fraction(b))

    def __add__(self, other):
        other = q(other)
        return F(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-q(other))

    def __rsub__(self, other):
        return q(other) - self

    def __mul__(self, other):
        other = q(other)
        return F(
            self.a * other.a + self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    __rmul__ = __mul__

    def inv(self):
        norm = self.a * self.a + self.a * self.b - self.b * self.b
        if norm == 0:
            raise ZeroDivisionError
        return F((self.a + self.b) / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * q(other).inv()

    def __rtruediv__(self, other):
        return q(other) / self

    def __pow__(self, n):
        if n < 0:
            return (self.inv()) ** (-n)
        out, x = F(1), self
        while n:
            if n & 1:
                out *= x
            x *= x
            n >>= 1
        return out

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        return f"({self.a}+{self.b}*phi)"


def q(x):
    return x if isinstance(x, F) else F(x)


Z, O, PHI = F(0), F(1), F(0, 1)


def vec(*xs):
    return tuple(q(x) for x in xs)


def mat(rows):
    return tuple(tuple(q(x) for x in row) for row in rows)


I3 = mat(((1, 0, 0), (0, 1, 0), (0, 0, 1)))


def transpose(A):
    return tuple(zip(*A))


def mm(A, B):
    Bt = transpose(B)
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in Bt) for row in A)


def mpow(A, n):
    out = I3
    for _ in range(n):
        out = mm(A, out)
    return out


def mv(A, x):
    return tuple(sum(a * b for a, b in zip(row, x)) for row in A)


def madd(A, B):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(A, B))


def mscale(c, A):
    return tuple(tuple(q(c) * x for x in row) for row in A)


def outer(x, y):
    return tuple(tuple(a * b for b in y) for a in x)


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def inv3(A):
    d = det3(A)
    cof = (
        (A[1][1] * A[2][2] - A[1][2] * A[2][1], A[1][2] * A[2][0] - A[1][0] * A[2][2], A[1][0] * A[2][1] - A[1][1] * A[2][0]),
        (A[0][2] * A[2][1] - A[0][1] * A[2][2], A[0][0] * A[2][2] - A[0][2] * A[2][0], A[0][1] * A[2][0] - A[0][0] * A[2][1]),
        (A[0][1] * A[1][2] - A[0][2] * A[1][1], A[0][2] * A[1][0] - A[0][0] * A[1][2], A[0][0] * A[1][1] - A[0][1] * A[1][0]),
    )
    return mscale(1 / d, cof)


def columns(*cols):
    return transpose(cols)


def flatten_sym(A):
    return (A[0][0], A[1][1], A[2][2], A[0][1], A[0][2], A[1][2])


def rank(A):
    M = [list(row) for row in A]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != Z), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pivot = M[r][c]
        M[r] = [x / pivot for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != Z:
                z = M[i][c]
                M[i] = [x - z * y for x, y in zip(M[i], M[r])]
        r += 1
    return r


def perm_comp(p, q):
    """p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


ID6 = tuple(range(6))


def perm_pow(p, n):
    out = ID6
    for _ in range(n):
        out = perm_comp(p, out)
    return out


def perm_order(p):
    x = ID6
    for n in range(1, 61):
        x = perm_comp(p, x)
        if x == ID6:
            return n
    raise AssertionError("order > 60")


def parity(p):
    inv = sum(p[i] > p[j] for i in range(6) for j in range(i + 1, 6))
    return inv % 2


def cycle_type(p):
    seen, lens = set(), []
    for i in range(6):
        if i not in seen:
            j, n = i, 0
            while j not in seen:
                seen.add(j)
                j = p[j]
                n += 1
            lens.append(n)
    return tuple(sorted(lens, reverse=True))


def closure(gens):
    G = {ID6}
    changed = True
    while changed:
        changed = False
        for x in tuple(G):
            for g in gens:
                for y in (perm_comp(g, x), perm_comp(x, g)):
                    if y not in G:
                        G.add(y)
                        changed = True
    return G


def inv_perm(p):
    out = [None] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def conjugate_perm(tau, p):
    """tau p tau^-1, where tau maps old labels to new labels."""
    return perm_comp(tau, perm_comp(p, inv_perm(tau)))


P1_POINTS = (None, 0, 1, 2, 3, 4)  # infinity, then F_5


def mobius_perm(A):
    a, b, c, d = (x % 5 for row in A for x in row)
    assert (a * d - b * c) % 5 == 1
    out = []
    for z in P1_POINTS:
        if z is None:
            w = None if c == 0 else (a * pow(c, -1, 5)) % 5
        else:
            den = (c * z + d) % 5
            w = None if den == 0 else ((a * z + b) * pow(den, -1, 5)) % 5
        out.append(P1_POINTS.index(w))
    return tuple(out)


def complexity(A):
    return sum(abs(x.a.numerator) + abs(x.b.numerator) + x.a.denominator + x.b.denominator for row in A for x in row)


def fmt_matrix(A):
    return "[" + ", ".join("[" + ", ".join(map(str, row)) + "]" for row in A) + "]"


def main():
    assert PHI * PHI == PHI + 1

    # Frozen order from GOLDEN-SIX-LINE-SYM2-FRAME.
    v = (
        vec(0, 1, PHI), vec(0, 1, -PHI),
        vec(1, PHI, 0), vec(1, -PHI, 0),
        vec(PHI, 0, 1), vec(PHI, 0, -1),
    )
    r = PHI + 2
    assert all(dot(x, x) == r for x in v)
    assert all(dot(v[i], v[j]) ** 2 == PHI ** 2 for i in range(6) for j in range(i + 1, 6))
    assert r * r == 5 * PHI * PHI

    P = tuple(mscale(1 / r, outer(x, x)) for x in v)
    assert all(mm(X, X) == X and trace(X) == O for X in P)
    assert madd(madd(madd(madd(madd(P[0], P[1]), P[2]), P[3]), P[4]), P[5]) == mscale(2, I3)
    assert rank(transpose(tuple(flatten_sym(X) for X in P))) == 6

    gram = tuple(tuple(trace(mm(X, Y)) for Y in P) for X in P)
    expected_gram = tuple(tuple(F(1) if i == j else F(Fraction(1, 5)) for j in range(6)) for i in range(6))
    assert gram == expected_gram

    Q = tuple(madd(X, mscale(F(Fraction(-1, 3)), I3)) for X in P)
    zero3 = mscale(0, I3)
    assert sum_matrices(Q) == zero3
    cgram = tuple(tuple(trace(mm(X, Y)) for Y in Q) for X in Q)
    expected_cgram = tuple(tuple(F(Fraction(2, 3)) if i == j else F(Fraction(-2, 15)) for j in range(6)) for i in range(6))
    assert cgram == expected_cgram
    assert rank(cgram) == 5

    # Exact frame operator on Sym_2: M = (1/3)P_1 + (2/15)P_5.
    sym_basis = (
        mat(((1, 0, 0), (0, 0, 0), (0, 0, 0))),
        mat(((0, 0, 0), (0, 1, 0), (0, 0, 0))),
        mat(((0, 0, 0), (0, 0, 0), (0, 0, 1))),
        mat(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        mat(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
        mat(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
    )
    for X in sym_basis:
        MX = sum_matrices(tuple(mscale(trace(mm(Pi, X)) / 6, Pi) for Pi in P))
        P1 = mscale(trace(X) / 3, I3)
        P5 = madd(X, mscale(-1, P1))
        target = madd(mscale(F(Fraction(1, 3)), P1), mscale(F(Fraction(2, 15)), P5))
        assert MX == target

    # Gamma_Gram is S6, not A5: every permutation preserves diag/off-diag Gram.
    assert factorial(6) == 720
    assert all(tuple(tuple(gram[p[i]][p[j]] for j in range(6)) for i in range(6)) == gram for p in permutations(range(6)))

    # Enumerate all ambient SO(3,Q(phi)) maps preserving the six lines.
    src = columns(v[0], v[2], v[4])
    src_inv = inv3(src)
    rotations = {}
    for targets in permutations(range(6), 3):
        for signs in product((-1, 1), repeat=3):
            B = columns(*(tuple(F(s) * z for z in v[j]) for s, j in zip(signs, targets)))
            A = mm(B, src_inv)
            if mm(transpose(A), A) != I3 or det3(A) != O:
                continue
            image = []
            for x in v:
                y = mv(A, x)
                hit = next((j for j, z in enumerate(v) if y == z or y == tuple(-t for t in z)), None)
                if hit is None:
                    break
                image.append(hit)
            else:
                p = tuple(image)
                assert len(set(p)) == 6
                if A in rotations:
                    assert rotations[A] == p
                rotations[A] = p

    assert len(rotations) == 60
    perms = set(rotations.values())
    assert len(perms) == 60             # faithful action
    assert all(perm_comp(p, q_) in perms for p in perms for q_ in perms)
    assert all(parity(p) == 0 for p in perms)
    assert {cycle_type(p) for p in perms} == {(1, 1, 1, 1, 1, 1), (2, 2, 1, 1), (3, 3), (5, 1)}
    counts = {ct: sum(cycle_type(p) == ct for p in perms) for ct in {cycle_type(p) for p in perms}}
    assert counts == {(1, 1, 1, 1, 1, 1): 1, (2, 2, 1, 1): 15, (3, 3): 20, (5, 1): 24}

    # Use the coordinate 3-cycle as y and find a simple x satisfying the A5 presentation.
    Y = mat(((0, 0, 1), (1, 0, 0), (0, 1, 0)))
    assert Y in rotations and perm_order(rotations[Y]) == 3
    candidates = []
    for A, px in rotations.items():
        if perm_order(px) != 2:
            continue
        py = rotations[Y]
        if perm_order(perm_comp(px, py)) == 5 and len(closure((px, py))) == 60:
            candidates.append((complexity(A), A, px))
    assert candidates
    _, X, px = min(candidates, key=lambda z: (z[0], repr(z[1])))
    py = rotations[Y]
    assert perm_order(px) == 2
    assert perm_order(py) == 3
    assert perm_order(perm_comp(px, py)) == 5
    assert len(closure((px, py))) == 60
    assert mpow(X, 2) == I3
    assert mpow(Y, 3) == I3
    assert mpow(mm(X, Y), 5) == I3

    # Deterministic pre-AME comparison with the marked quotient of COLOR-CORE-2I.
    # Reduction of the Canon generators modulo (1-zeta):
    # Sbar=[[0,-1],[1,0]], Tbar=[[1,1],[0,1]] in SL_2(F_5).
    ps = mobius_perm(((0, -1), (1, 0)))
    pt = mobius_perm(((1, 1), (0, 1)))
    psl = closure((ps, pt))
    assert len(psl) == 60
    comparisons = [tau for tau in permutations(range(6)) if {conjugate_perm(tau, p) for p in perms} == psl]
    assert len(comparisons) == 120
    perm_to_rotation = {p: A for A, p in rotations.items()}
    # The marked color lift T has spin trace phi-1, hence Sym^2 trace
    # (phi-1)^2-1 = 1-phi.  This fixes the outer-automorphism bit before
    # looking at AME.  The other 60 comparisons send Tbar to trace phi.
    assert (PHI - 1) ** 2 - 1 == 1 - PHI
    marked_comparisons = []
    trace_split = {}
    for t in comparisons:
        old_t = conjugate_perm(inv_perm(t), pt)
        tr = trace(perm_to_rotation[old_t])
        trace_split[tr] = trace_split.get(tr, 0) + 1
        if tr == 1 - PHI:
            marked_comparisons.append(t)
    assert trace_split == {1 - PHI: 60, PHI: 60}
    assert len(marked_comparisons) == 60
    tau = min(marked_comparisons)
    assert len(comparisons) == 120
    qx, qy = conjugate_perm(tau, px), conjugate_perm(tau, py)
    old_s = conjugate_perm(inv_perm(tau), ps)
    old_t = conjugate_perm(inv_perm(tau), pt)
    R_s, R_t = perm_to_rotation[old_s], perm_to_rotation[old_t]
    assert mpow(R_s, 2) == I3 and trace(R_s) == -O
    assert mpow(R_t, 5) == I3 and trace(R_t) == 1 - PHI
    assert mpow(mm(R_s, R_t), 3) == I3

    print("G2_EXACT_PASS")
    print("field=Q(phi), phi^2=phi+1")
    print("projector_rank=6")
    print("sum_projectors=2*I3")
    print("projector_gram=diag(1),offdiag(1/5)")
    print("centered_gram=diag(2/3),offdiag(-2/15)")
    print("moment_spectrum=1/3^1,2/15^5")
    print("Gamma_Gram=S6 order=720")
    print("Gamma_SO3_lines=A5 order=60 faithful")
    print("cycle_counts=" + repr(counts))
    print("X_order2=" + fmt_matrix(X))
    print("X_perm_1based=" + repr(tuple(i + 1 for i in px)))
    print("Y_order3=" + fmt_matrix(Y))
    print("Y_perm_1based=" + repr(tuple(i + 1 for i in py)))
    print("XY_order=5")
    print("generated_order=60")
    print("PSL2F5_action_order=60")
    print("P1_order=(infinity,0,1,2,3,4)")
    print("lex_comparison_line_to_P1_0based=" + repr(tau))
    print("number_of_labeled_comparisons=" + str(len(comparisons)))
    print("marked_T_trace_split={1-phi:60,phi:60}")
    print("marked_comparisons_mod_outer=60")
    print("marked_line_to_P1_0based=" + repr(tau))
    print("Sbar_pullback_perm_1based=" + repr(tuple(i + 1 for i in old_s)))
    print("Sbar_pullback_matrix=" + fmt_matrix(R_s))
    print("Tbar_pullback_perm_1based=" + repr(tuple(i + 1 for i in old_t)))
    print("Tbar_pullback_matrix=" + fmt_matrix(R_t))
    print("marked_relations=S^2=T^5=(ST)^3=I")
    print("X_on_P1_0based=" + repr(qx))
    print("Y_on_P1_0based=" + repr(qy))


def sum_matrices(xs):
    xs = tuple(xs)
    if not xs:
        raise ValueError("empty sum")
    out = mscale(0, xs[0])
    for X in xs:
        out = madd(out, X)
    return out


if __name__ == "__main__":
    main()
