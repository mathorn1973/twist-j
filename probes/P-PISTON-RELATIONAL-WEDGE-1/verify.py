#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact audit for P-PISTON-RELATIONAL-WEDGE-1.

Scientific authority: none.  Initial zero-run preregistration verifier.  The written proofs in
PREREG.md carry the universal claims; this standard-library verifier audits
the frozen 2x2 reshape of the balanced piston, the piston actions of the
five public generators, the frozen Tr_4 occurrence-weight closed forms, and
the finite census over the 625 pistons.  Rational and integer arithmetic
only; no cyclotomic carrier is touched.  It must not be imported as a module.

Formal run (only after the immutable pin and public remote readback):
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 probes/P-PISTON-RELATIONAL-WEDGE-1/verify.py

Exit code map: 0 pass, 1 STOP (integrity), 2 FALSIFIED (a gate failed).
"""

import sys
from fractions import Fraction
from itertools import product, permutations


F = Fraction
ZERO = F(0)
ONE = F(1)
QUARTER = F(1, 4)

FAILURES = []
GATE_COUNT = 0


# ------------------------------------------------------------------- gates

def gate(name, condition, detail=""):
    global GATE_COUNT
    GATE_COUNT += 1
    ok = bool(condition)
    if not ok:
        FAILURES.append(name)
    line = "CHECK %-52s %s" % (name, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)


def integrity(name, condition, detail=""):
    global GATE_COUNT
    GATE_COUNT += 1
    ok = bool(condition)
    line = "CHECK %-52s %s" % (name, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)
    if not ok:
        raise RuntimeError("integrity gate failed: " + name)


def report(name, value):
    print("REPORT %-51s %s" % (name, value))


# --------------------------------------------------------- rational matrices

def frac_rank(rows):
    M = [list(r) for r in rows]
    nrows = len(M)
    ncols = len(M[0]) if M else 0
    rank = 0
    col = 0
    while rank < nrows and col < ncols:
        pivot = None
        for r in range(rank, nrows):
            if M[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            col += 1
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        pv = M[rank][col]
        M[rank] = [v / pv for v in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
        col += 1
    return rank


def kron2(A, B):
    out = []
    for i in range(2):
        for k in range(2):
            row = []
            for j in range(2):
                for l in range(2):
                    row.append(A[i][j] * B[k][l])
            out.append(tuple(row))
    return tuple(out)


# ------------------------------------------------------------ piston block
# Checkpoint coordinates (p1, p4, p1p, p4p, q, r); the piston is the first
# four.  Balanced lift ell(0,1,2,3,4) = (0, 1, 2, -2, -1).

ELL = {0: 0, 1: 1, 2: 2, 3: -2, 4: -1}
PISTONS = tuple(product(range(5), repeat=4))   # (p1, p4, p1p, p4p)


def lift(p):
    return tuple(ELL[t] for t in p)


def reshape(p):
    """X_p = ((ell p1, ell p4), (ell p1p, ell p4p))."""
    v = lift(p)
    return ((v[0], v[1]), (v[2], v[3]))


def d_z(p):
    X = reshape(p)
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]


def d_5(p):
    return (p[0] * p[3] - p[1] * p[2]) % 5


def norm2(p):
    return sum(t * t for t in lift(p))


def piston_sum(p):
    return sum(lift(p))


def c_z(p):
    n2 = norm2(p)
    if n2 == 0:
        return None
    return F(2 * abs(d_z(p)), n2)


def area_z(p):
    n2 = norm2(p)
    if n2 == 0:
        return None
    return F(d_z(p) * d_z(p), n2 * n2)


def act_a(p):
    return (p[1], p[0], p[3], p[2])


def act_b(p):
    return ((-p[2]) % 5, (-p[3]) % 5, (-p[0]) % 5, (-p[1]) % 5)


def act_d(p):
    c_d = (2, 1, 3, 4)
    return tuple((c_d[i] - p[i]) % 5 for i in range(4))


def act_e(p):
    # e = (c_d + v_e) - x with v_e supported on the fiber; piston part as d
    return act_d(p)


def act_c(p, r):
    # piston -> b4(piston) + s_c + r u_c,  b4 = piston part of b
    b4 = act_b(p)
    s_c = (2, 1, 2, 1)
    u_c = (0, 1, 0, -1)
    return tuple((b4[i] + s_c[i] + r * u_c[i]) % 5 for i in range(4))


def closed_forms(p):
    """QDD-PROJECTOR-PAIR-TR4 closed forms (m, w_low, w_high)."""
    v = lift(p)
    s = sum(v)
    q = sum(t * t for t in v)
    return (F(q) - F(s * s, 5), F(s * s, 20), F(q) - F(s * s, 4))


def signed_permutation_matrix(action):
    """4x4 matrix M with M ell(p) = ell(action(p)) for the linear actions."""
    cols = []
    for i in range(4):
        e = [0, 0, 0, 0]
        e[i] = 1
        img = action(tuple(e))
        cols.append(tuple(ELL[t] for t in img))
    return tuple(tuple(F(cols[j][i]) for j in range(4)) for i in range(4))


# ------------------------------- rational kappa coefficient (consistency)
# Over K = Q with V = W = Q^2, reorder (V tensor W)^{tensor 2} to
# V_1 V_2 W_1 W_2, index (i, k, j, l); alpha swaps i<->k, beta swaps j<->l;
# P_-- = (1 - alpha)(1 - beta)/4; kappa = (e0 wedge e1) tensor (f0 wedge f1).
# This is QPAIR-SYM2-TENSOR-DEFECT specialised to K = Q, audited here only as
# a named consistency check of the reshape convention.

def kappa_coefficient_rational(X):
    vec = {}
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    vec[(i, k, j, l)] = F(X[i][j]) * F(X[k][l])

    def swap(v, which):
        out = {}
        for (i, k, j, l), p in v.items():
            key = (k, i, j, l) if which == "alpha" else (i, k, l, j)
            out[key] = out.get(key, ZERO) + p
        return out

    def vsub(u, v):
        return {key: u.get(key, ZERO) - v.get(key, ZERO)
                for key in set(u) | set(v)}

    ma = vsub(vec, swap(vec, "alpha"))
    mb = vsub(ma, swap(ma, "beta"))
    proj = {key: p / 4 for key, p in mb.items()}
    kappa = {(0, 1, 0, 1): 1, (1, 0, 0, 1): -1,
             (0, 1, 1, 0): -1, (1, 0, 1, 0): 1}
    coeff = proj.get((0, 1, 0, 1), ZERO)
    for key in product(range(2), repeat=4):
        if proj.get(key, ZERO) != kappa.get(key, 0) * coeff:
            return None
    return coeff


# ------------------------------------------------------------------- main

def main():
    print("P-PISTON-RELATIONAL-WEDGE-1 verifier")
    print("2x2 reshape of the balanced piston selected by the two linear "
          "generators, the piston wedge D_Z, the frozen Tr_4 occurrence "
          "weights as a non-separating map, and the F_5 / Z lift census")
    print("")

    if len(sys.argv) != 1:
        raise RuntimeError("no arguments accepted")
    if sys.version_info < (3, 8):
        raise RuntimeError("Python 3.8 or newer required")
    integrity("I01.environment", True)
    integrity("I01.piston.count.625", len(PISTONS) == 625)

    # ============================================================== R3
    Ma = signed_permutation_matrix(act_a)
    Mb = signed_permutation_matrix(act_b)
    I2 = ((ONE, ZERO), (ZERO, ONE))
    SX = ((ZERO, ONE), (ONE, ZERO))
    gate("R3a.a.equals.1_t.tensor.sigma_i", Ma == kron2(I2, SX))
    gate("R3a.b.equals.-(sigma_t.tensor.1_i)",
         Mb == tuple(tuple(-v for v in row) for row in kron2(SX, I2)))
    lin_a = all(lift(act_a(p)) == tuple(sum(Ma[i][j] * lift(p)[j] for j in range(4))
                                         for i in range(4)) for p in PISTONS)
    lin_b = all(lift(act_b(p)) == tuple(sum(Mb[i][j] * lift(p)[j] for j in range(4))
                                         for i in range(4)) for p in PISTONS)
    gate("R3a.a.b.linear.and.lift-compatible.on.625", lin_a and lin_b)
    zero_p = (0, 0, 0, 0)
    gate("R3a.c.d.e.move.the.zero.piston",
         act_d(zero_p) != zero_p and act_e(zero_p) != zero_p
         and all(act_c(zero_p, r) != zero_p for r in range(5)))
    gate("R3a.a.b.commute",
         all(act_a(act_b(p)) == act_b(act_a(p)) for p in PISTONS))
    gate("R3a.a.b.involutions",
         all(act_a(act_a(p)) == p and act_b(act_b(p)) == p for p in PISTONS))

    coords = ("p1", "p4", "p1p", "p4p")
    a_perm = {"p1": "p4", "p4": "p1", "p1p": "p4p", "p4p": "p1p"}
    b_perm = {"p1": "p1p", "p1p": "p1", "p4": "p4p", "p4p": "p4"}
    labels = tuple(product((0, 1), repeat=2))
    admissible = []
    for perm in permutations(labels):
        L = dict(zip(coords, perm))

        def flip_bit(pm):
            bits = set()
            for cname in coords:
                l1, l2 = L[cname], L[pm[cname]]
                diff = tuple(i for i in range(2) if l1[i] != l2[i])
                if len(diff) != 1:
                    return None
                bits.add(diff[0])
            return bits.pop() if len(bits) == 1 else None

        fa = flip_bit(a_perm)
        fb = flip_bit(b_perm)
        if fa is not None and fb is not None and fa != fb:
            admissible.append(L)
    gate("R3b.admissible.labelings.8.of.24", len(admissible) == 8)

    def wedge_under(L, p):
        v = dict(zip(coords, lift(p)))
        Xl = {}
        for cname in coords:
            Xl[L[cname]] = v[cname]
        return Xl[(0, 0)] * Xl[(1, 1)] - Xl[(0, 1)] * Xl[(1, 0)]

    same_abs = all(
        len(set(abs(wedge_under(L, p)) for L in admissible)) == 1
        for p in PISTONS) if admissible else False
    gate("R3b.labelings.share.|D_Z|", same_abs)
    frozen_L = {"p1": (0, 0), "p4": (0, 1), "p1p": (1, 0), "p4p": (1, 1)}
    gate("R3b.frozen.reshape.admissible", frozen_L in admissible)
    gate("R3b.frozen.reshape.D_Z.equals.det.X_p",
         all(wedge_under(frozen_L, p) == d_z(p) for p in PISTONS))

    def relabel(L, flip_t, flip_i, exchange):
        out = {}
        for cname, (t, i) in L.items():
            t2, i2 = t ^ flip_t, i ^ flip_i
            out[cname] = (i2, t2) if exchange else (t2, i2)
        return out
    orbit = []
    for ft in (0, 1):
        for fi in (0, 1):
            for ex in (0, 1):
                orbit.append(relabel(frozen_L, ft, fi, ex))
    gate("R3b.one.class.under.relabel.and.exchange",
         all(L in orbit for L in admissible)
         and all(L in admissible for L in orbit) and len(orbit) == 8)

    gate("R3c.sign.a.on.all.pistons",
         all(d_z(act_a(p)) == -d_z(p) for p in PISTONS))
    gate("R3c.sign.b.on.all.pistons",
         all(d_z(act_b(p)) == -d_z(p) for p in PISTONS))
    gate("R3c.lift.odd", all(ELL[(-k) % 5] == -ELL[k] for k in range(5)))
    gate("R3c.|D_Z|.and.c_Z.<a,b>-invariant",
         all(abs(d_z(act_a(p))) == abs(d_z(p)) == abs(d_z(act_b(p)))
             and c_z(act_a(p)) == c_z(p) == c_z(act_b(p)) for p in PISTONS))
    d_changes = sum(1 for p in PISTONS if abs(d_z(act_d(p))) != abs(d_z(p)))
    gate("R3c.d.changes.|D_Z|.somewhere", d_changes > 0)
    report("R3c.d.changes.|D_Z|.count", d_changes)

    ok_slot = True
    ok_kappa = True
    ok_det = True
    for p in PISTONS:
        v = lift(p)
        # transpose slot A_T = v v^T (DEF-QDD-QPAIR, DEF-QDD-TRANSPOSE)
        S = tuple(tuple(F(v[i] * v[j]) for j in range(4)) for i in range(4))
        if S[0][3] - S[1][2] != d_z(p):
            ok_slot = False
        kc = kappa_coefficient_rational(reshape(p))
        if kc is None or kc != F(d_z(p), 2):
            ok_kappa = False
        X = reshape(p)
        XXt = tuple(tuple(sum(X[i][t] * X[k][t] for t in range(2))
                          for k in range(2)) for i in range(2))
        if XXt[0][0] * XXt[1][1] - XXt[0][1] * XXt[1][0] != d_z(p) ** 2:
            ok_det = False
    gate("R3d.D_Z.equals.transpose-slot.functional.(14)-(23)", ok_slot)
    gate("R3d.consistency.D_Z.equals.2.kappa_coef.over.Q", ok_kappa)
    gate("R3d.det(X_p.X_p^T).equals.D_Z^2", ok_det)
    gate("R3e.D_5.zero.count.145", sum(1 for p in PISTONS if d_5(p) == 0) == 145)
    gate("R3e.GL2(F5).order.480", 625 - 145 == 480 == (25 - 1) * (25 - 5))
    gate("R3e.D_Z.mod.5.equals.D_5", all(d_z(p) % 5 == d_5(p) for p in PISTONS))

    # ============================================================== R4
    G = tuple(tuple(ONE * (i == j) - F(1, 5) for j in range(4)) for i in range(4))
    E_low = tuple(tuple(QUARTER for _ in range(4)) for _ in range(4))
    ok_cf = True
    for p in PISTONS:
        v = [F(t) for t in lift(p)]
        vG = [sum(v[i] * G[i][j] for i in range(4)) for j in range(4)]
        m = sum(vG[j] * v[j] for j in range(4))
        vvTG = [[v[i] * vG[j] for j in range(4)] for i in range(4)]
        w_low = sum(E_low[i][j] * vvTG[j][i] for i in range(4) for j in range(4))
        w_high = m - w_low
        if (m, w_low, w_high) != closed_forms(p):
            ok_cf = False
    gate("R4a.Tr4.closed.forms.on.all.pistons", ok_cf)
    by_class = {}
    for p in PISTONS:
        by_class.setdefault((piston_sum(p), norm2(p)), set()).add(closed_forms(p))
    gate("R4a.closed.forms.depend.on.(s,|v|^2).only",
         all(len(s) == 1 for s in by_class.values()))
    v1 = (1, 0, 0, 1)
    v2 = (1, 1, 0, 0)
    gate("R4b.witness.same.(s,|v|^2)",
         (piston_sum(v1), norm2(v1)) == (2, 2) == (piston_sum(v2), norm2(v2)))
    gate("R4b.witness.same.occurrence.weights",
         closed_forms(v1) == closed_forms(v2) == (F(6, 5), F(1, 5), F(1)))
    gate("R4b.witness.same.normalized.pair",
         (closed_forms(v1)[1] / closed_forms(v1)[0],
          closed_forms(v1)[2] / closed_forms(v1)[0]) == (F(1, 6), F(5, 6))
         == (closed_forms(v2)[1] / closed_forms(v2)[0],
             closed_forms(v2)[2] / closed_forms(v2)[0]))
    gate("R4b.witness.different.D_Z.and.c_Z",
         d_z(v1) == 1 and d_z(v2) == 0 and c_z(v1) == ONE and c_z(v2) == ZERO)
    # The full record carries the wedge: on SUPPORTED records the pair
    # (total_weight m, density rho) recovers v v^T = m rho G^-1.
    # Density alone is scale-blind.
    def density(p):
        v = [F(t) for t in lift(p)]
        vG = [sum(v[i] * G[i][j] for i in range(4)) for j in range(4)]
        m = closed_forms(p)[0]
        return tuple(tuple(v[i] * vG[j] / m for j in range(4)) for i in range(4))
    Ginv = tuple(tuple(ONE * (i == j) + ONE for j in range(4)) for i in range(4))
    gate("R4b.G.inverse.is.I+11^T",
         all(sum(G[i][t] * Ginv[t][j] for t in range(4)) == ONE * (i == j)
             for i in range(4) for j in range(4)))
    def wedge_from_record(p):
        m = closed_forms(p)[0]
        if m == ZERO:
            return ZERO
        rho = density(p)
        vvT = tuple(tuple(sum(rho[i][t] * Ginv[t][j] for t in range(4)) * m
                          for j in range(4)) for i in range(4))
        return vvT[0][3] - vvT[1][2]
    gate("R4b.total-weight+density.recovers.D_Z.all.625",
         all(wedge_from_record(p) == d_z(p) for p in PISTONS))
    v_scaled = (2, 0, 0, 2)
    gate("R4b.density-alone.scale-blind.witness",
         density(v1) == density(v_scaled)
         and d_z(v1) == 1 and d_z(v_scaled) == 4
         and closed_forms(v1)[0] == F(6, 5)
         and closed_forms(v_scaled)[0] == F(24, 5))
    # guard gates, not claims: G is not a product metric for the reshape,
    # and the wedge form is outside the span of the two Tr_4 quadratic forms
    Re = []
    for i1 in range(2):
        for i2 in range(2):
            row = []
            for j1 in range(2):
                for j2 in range(2):
                    row.append(G[2 * i1 + j1][2 * i2 + j2])
            Re.append(tuple(row))
    integrity("G1.guard.realignment.rank.of.G.is.2", frac_rank(Re) == 2)
    ones = tuple(tuple(ONE for _ in range(4)) for _ in range(4))
    ident = tuple(tuple(ONE * (i == j) for j in range(4)) for i in range(4))
    W = [[ZERO] * 4 for _ in range(4)]
    W[0][3] = W[3][0] = F(1, 2)
    W[1][2] = W[2][1] = F(-1, 2)
    flat = lambda M: [M[i][j] for i in range(4) for j in range(4)]
    integrity("G2.guard.W.outside.span{I,11^T}",
              frac_rank([flat(ident), flat(ones), flat(W)]) == 3)
    integrity("G2.guard.W.quadratic.form.is.D_Z",
              all(sum(F(lift(p)[i]) * W[i][j] * F(lift(p)[j])
                      for i in range(4) for j in range(4)) == d_z(p)
                  for p in PISTONS))
    classes = {}
    for p in PISTONS:
        classes.setdefault((piston_sum(p), norm2(p)), set()).add(abs(d_z(p)))
    report("R4v.(s,|v|^2).classes", len(classes))
    report("R4v.classes.with.several.|D_Z|",
           sum(1 for s in classes.values() if len(s) > 1))

    # ============================================================== R5
    dz = {p: d_z(p) for p in PISTONS}
    gate("R5a.|D_Z|.max.8", max(abs(t) for t in dz.values()) == 8)
    gate("R5a.count.|D_Z|=8.is.8", sum(1 for t in dz.values() if abs(t) == 8) == 8)
    five = [p for p in PISTONS if abs(dz[p]) == 5]
    gate("R5b.count.|D_Z|=5.is.16", len(five) == 16)
    gate("R5b.|D_Z|=5.all.|v|^2=10.c_Z=1",
         all(norm2(p) == 10 and c_z(p) == ONE for p in five))
    gate("R5b.singular.mod.5.iff.D_Z.in.{0,+-5}",
         all((d_5(p) == 0) == (dz[p] in (0, 5, -5)) for p in PISTONS))
    gate("R5b.count.D_Z=0.is.129", sum(1 for t in dz.values() if t == 0) == 129)
    gate("R5b.145.equals.129+16", 129 + 16 == 145)
    maximal = [p for p in PISTONS if c_z(p) == ONE]
    gate("R5c.count.c_Z=1.is.48", len(maximal) == 48)

    def rows_orthogonal_equal_norm(p):
        X = reshape(p)
        r1, r2 = X[0], X[1]
        return (r1[0] * r2[0] + r1[1] * r2[1] == 0
                and r1[0] ** 2 + r1[1] ** 2 == r2[0] ** 2 + r2[1] ** 2
                and r1 != (0, 0))
    gate("R5c.c_Z=1.iff.X_p.X_p^T.scalar",
         all((c_z(p) == ONE) == rows_orthogonal_equal_norm(p)
             for p in PISTONS if norm2(p) > 0))
    gate("R5c.16.five-pistons.among.the.48", all(p in maximal for p in five))
    cz_values = [c_z(p) for p in PISTONS if norm2(p) > 0]
    gate("R5d.c_Z.bounds.all.624", len(cz_values) == 624
         and all(ZERO <= c <= ONE for c in cz_values))
    gate("R5d.area.equals.c_Z^2/4.all.624",
         all(area_z(p) == c_z(p) * c_z(p) / 4 for p in PISTONS if norm2(p) > 0))
    multiset = {}
    for c in cz_values:
        multiset[c] = multiset.get(c, 0) + 1
    report("R5v.distinct.c_Z.values", len(multiset))
    for c in sorted(multiset):
        report("R5v.c_Z.%s" % c, multiset[c])
    report("R5v.value.set.c_Z", " ".join(str(c) for c in sorted(multiset)))

    print("")
    print("gates: %d  failures: %d" % (GATE_COUNT, len(FAILURES)))
    if FAILURES:
        for name in FAILURES:
            print("FALSIFIED %s" % name)
        print("RESULT FALSIFIED")
        return 2
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as exc:  # integrity, not science
        print("STOP %s: %s" % (type(exc).__name__, exc))
        code = 1
    sys.stdout.flush()
    sys.exit(code)
