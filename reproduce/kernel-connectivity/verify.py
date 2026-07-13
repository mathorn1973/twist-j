#!/usr/bin/env python3
# TWIST-J kernel connectivity witness. Exact arithmetic only: integers
# and F_5, standard library only, no floats anywhere. The generators
# are the registered kernel generators of the census (section 3 of the
# Canon), taken verbatim; the wedge of a cell pair is
# w_ij = x0_i x1_j - x0_j x1_i over F_5, the inter cell symplectic
# area.
#
# The arc: every generator is affine, g(x) = M_g x + v_g on all 15625
# states with det M_g = 1 over F_5, a and b linear, c, d, e strictly
# affine; the two CSUM transvections x1 -> x1 + x0 and x0 -> x0 + x1
# preserve all 15 wedges as an exact polynomial identity in 12
# variables and generate SL2(F_5), order 120, acting diagonally; the
# linear sector acts on the wedge by congruence W -> M_g W M_g^T and
# preserves the wedge rank strata, with rank 0 exactly on dependent
# pairs; only the affine translations cross strata, lifting exactly
# 62480 of the 78125 dependent pairs each for c, d, e and none for a,
# b; and the single cell component census over all seventeen recorded
# generator subsets is exact, from {ac} at 945 components to the full
# verb {abcde} at 1.
#
# Claims verified: KERNEL-WEDGE-AFFINITY, KERNEL-WEDGE-COUPLING,
# KERNEL-WEDGE-LINEAR-STRATA, KERNEL-WEDGE-AFFINE-MIX,
# KERNEL-CELL-COMPONENTS; the reading layer KERNEL-MACRO-READING is
# carried by the same structure. The live hypothesis
# KERNEL-CONNECT-ALL-K carries no witness here by design: the k = 2
# and k = 3 connectivity witnesses live at the sealed internal scope
# beyond the public 120 s budget, and nothing in this file claims
# them.

import sys

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


# ------------------------------------------- the kernel generators
S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x):
    p1, p4, p1p, p4p, q, t = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-t) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, t = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + t * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + t * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + t * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + t * U_VEC[3]) % 5,
            (1 - q) % 5, (-t) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (("a", gen_a), ("b", gen_b), ("c", gen_c), ("d", gen_d),
        ("e", gen_e))


def dec(i):
    out = []
    for _ in range(6):
        out.append(i % 5)
        i //= 5
    return tuple(out)


def enc(x):
    i = 0
    for k in range(5, -1, -1):
        i = i * 5 + x[k]
    return i


N = 15625
STATES = [dec(i) for i in range(N)]


def f5_rank(rows):
    m = [[x % 5 for x in row] for row in rows]
    rank = 0
    col = 0
    ncols = len(m[0])
    while rank < len(m) and col < ncols:
        piv = next((r for r in range(rank, len(m)) if m[r][col] % 5), None)
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = pow(m[rank][col], 3, 5)
        m[rank] = [(x * inv) % 5 for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col] % 5:
                f = m[r][col]
                m[r] = [(x - f * y) % 5 for x, y in zip(m[r], m[rank])]
        rank += 1
        col += 1
    return rank


def f5_det(mat):
    m = [[x % 5 for x in row] for row in mat]
    n = len(m)
    det = 1
    for col in range(n):
        piv = next((r for r in range(col, n) if m[r][col] % 5), None)
        if piv is None:
            return 0
        if piv != col:
            m[col], m[piv] = m[piv], m[col]
            det = (-det) % 5
        det = (det * m[col][col]) % 5
        inv = pow(m[col][col], 3, 5)
        m[col] = [(x * inv) % 5 for x in m[col]]
        for r in range(col + 1, n):
            f = m[r][col]
            if f % 5:
                m[r] = [(x - f * y) % 5 for x, y in zip(m[r], m[col])]
    return det % 5


def wedge(x0, x1):
    return [(x0[i] * x1[j] - x0[j] * x1[i]) % 5
            for i in range(6) for j in range(i + 1, 6)]


def wedge_mat(x0, x1):
    return [[(x0[i] * x1[j] - x0[j] * x1[i]) % 5 for j in range(6)]
            for i in range(6)]


# --------------------------- linear polynomials in 12 variables over F_5
# a polynomial is a dict {sorted variable index tuple: coefficient}
def pvar(i):
    return {(i,): 1}


def padd(p, q):
    r = dict(p)
    for m, c in q.items():
        r[m] = (r.get(m, 0) + c) % 5
    return {m: c for m, c in r.items() if c % 5}


def pneg(p):
    return {m: (-c) % 5 for m, c in p.items()}


def pmul(p, q):
    r = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(sorted(m1 + m2))
            r[m] = (r.get(m, 0) + c1 * c2) % 5
    return {m: c for m, c in r.items() if c % 5}


def main():
    # ------------------------------ 01 affinity split with det 1
    tables = {}
    lin = {}
    ok = True
    strictly_affine = []
    for name, g in GENS:
        v = list(g((0, 0, 0, 0, 0, 0)))
        cols = []
        for i in range(6):
            e = [0] * 6
            e[i] = 1
            gi = g(tuple(e))
            cols.append([(gi[r] - v[r]) % 5 for r in range(6)])
        M = [[cols[i][r] for i in range(6)] for r in range(6)]
        tab = [0] * N
        okg = True
        for idx in range(N):
            x = STATES[idx]
            gx = g(x)
            tab[idx] = enc(gx)
            aff = tuple((sum(M[r][k] * x[k] for k in range(6)) + v[r]) % 5
                        for r in range(6))
            if aff != gx:
                okg = False
                break
        ok &= okg
        ok &= f5_det(M) == 1
        tables[name] = tab
        lin[name] = (M, tuple(vv % 5 for vv in v))
        if any(vv % 5 for vv in v):
            strictly_affine.append(name)
    ok &= all(not any(lin[n][1]) for n in ("a", "b"))
    ok &= strictly_affine == ["c", "d", "e"]
    check("AFFINITY",
          "every kernel generator is affine on all 15625 states,"
          " g(x) = M_g x + v_g exactly, with det M_g = 1 over F_5 for"
          " all five; a and b are linear (v = 0) and c, d, e are"
          " strictly affine: the translational sector is exactly"
          " {c, d, e}", ok)

    # ------------------------------ 02 the CSUM transvections fix wedges
    x0 = [pvar(i) for i in range(6)]
    x1 = [pvar(6 + i) for i in range(6)]

    def wpoly(a, b):
        return [padd(pmul(a[i], b[j]), pneg(pmul(a[j], b[i])))
                for i in range(6) for j in range(i + 1, 6)]

    base = wpoly(x0, x1)
    t1 = wpoly(x0, [padd(x1[i], x0[i]) for i in range(6)])
    t2 = wpoly([padd(x0[i], x1[i]) for i in range(6)], x1)
    ok = t1 == base and t2 == base
    check("CSUM-WEDGE",
          "the two CSUM transvections x1 -> x1 + x0 and"
          " x0 -> x0 + x1 preserve all 15 wedges"
          " w_ij = x0_i x1_j - x0_j x1_i as an exact polynomial"
          " identity in 12 variables over F_5: the coupling moves"
          " within a fixed symplectic stratum", ok)

    # ------------------------------ 03 the coupling group is SL2(F_5)
    t1m = ((1, 0), (1, 1))
    t2m = ((1, 1), (0, 1))

    def mmul2(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % 5
                           for j in range(2)) for i in range(2))

    group = {((1, 0), (0, 1))}
    frontier = [((1, 0), (0, 1))]
    while frontier:
        nxt = []
        for m in frontier:
            for gmat in (t1m, t2m):
                prod = mmul2(m, gmat)
                if prod not in group:
                    group.add(prod)
                    nxt.append(prod)
        frontier = nxt
    ok = len(group) == 120
    ok &= all((m[0][0] * m[1][1] - m[0][1] * m[1][0]) % 5 == 1
              for m in group)
    sl2 = sum(1 for a in range(5) for b in range(5) for c in range(5)
              for d in range(5) if (a * d - b * c) % 5 == 1)
    ok &= sl2 == 120
    check("SL2",
          "the two transvection matrices generate a group of order"
          " exactly 120 with every determinant 1, and the full"
          " determinant one count over all 625 matrices is 120: the"
          " coupling group is all of SL2(F_5), the order of the"
          " binary icosahedral bridge of the color door", ok)

    # ------------------------------ 04 linear sector: congruence
    ok = True
    for name in ("a", "b"):
        M, v = lin[name]
        for i in range(6):
            for j in range(6):
                e_i = [0] * 6
                e_i[i] = 1
                e_j = [0] * 6
                e_j[j] = 1
                gi = STATES[tables[name][enc(tuple(e_i))]]
                gj = STATES[tables[name][enc(tuple(e_j))]]
                left = wedge_mat(gi, gj)
                W = wedge_mat(e_i, e_j)
                MW = [[sum(M[r][k] * W[k][c] for k in range(6)) % 5
                       for c in range(6)] for r in range(6)]
                right = [[sum(MW[r][k] * M[c][k] for k in range(6)) % 5
                          for c in range(6)] for r in range(6)]
                ok &= left == right
    check("CONGRUENCE",
          "for the linear generators a and b the diagonal action obeys"
          " W(g x0, g x1) = M_g W M_g^T on all 36 basis pairs; both"
          " sides are bilinear in (x0, x1), so the identity holds on"
          " all pairs, and congruence by an invertible matrix"
          " preserves the wedge rank", ok)

    # ------------------------------ 05 the rank dichotomy on the slice
    e0 = (1, 0, 0, 0, 0, 0)
    rank0 = 0
    rank2 = 0
    bad = False
    for idx in range(N):
        x = STATES[idx]
        w = wedge(x, e0)
        if any(w):
            r = f5_rank(wedge_mat(x, e0))
            if r != 2:
                bad = True
                break
            rank2 += 1
        else:
            dep = all((x[k] * e0[0] - x[0] * e0[k]) % 5 == 0
                      for k in range(6)) and all(
                          x[k] % 5 == 0 for k in range(1, 6))
            if not dep:
                bad = True
                break
            rank0 += 1
    ok = (not bad) and rank0 == 5 and rank2 == 15620
    check("RANK",
          "on the exhaustive slice x1 = e_0 (15625 pairs) the wedge"
          " rank is 0 exactly on the 5 dependent pairs (x0 a multiple"
          " of e_0) and 2 on the other 15620: rank 0 is parallel"
          " cells, rank 2 is independent cells, and no other rank"
          " occurs", ok)

    # ------------------------------ 06 the affine sector crosses strata
    counts = {}
    dec_tab = STATES
    for name, _ in GENS:
        tab = tables[name]
        lift = 0
        for idx in range(N):
            x = dec_tab[idx]
            gx = dec_tab[tab[idx]]
            for m in range(5):
                mx = (m * x[0] % 5, m * x[1] % 5, m * x[2] % 5,
                      m * x[3] % 5, m * x[4] % 5, m * x[5] % 5)
                gy = dec_tab[tab[enc(mx)]]
                for i in range(6):
                    xi = gx[i]
                    yi = gy[i]
                    hit = False
                    for j in range(i + 1, 6):
                        if (xi * gy[j] - gx[j] * yi) % 5:
                            lift += 1
                            hit = True
                            break
                    if hit:
                        break
        counts[name] = lift
    ok = counts["a"] == 0 and counts["b"] == 0
    ok &= counts["c"] == counts["d"] == counts["e"] == 62480
    ok &= 62480 == 2 ** 4 * 5 * 11 * 71
    check("AFFINE-MIX",
          "exhaustively over the full dependent stratum x1 = m x0"
          " (78125 pairs per generator): the linear generators a and b"
          " lift 0 pairs off rank 0, while the affine translations c,"
          " d, and e each lift exactly 62480 = 2^4 . 5 . 11 . 71 pairs"
          " to rank 2: only the translational sector crosses the"
          " symplectic strata", ok)

    # ------------------------------ 07 the seventeen subset census
    TABLE = (("bde", 169), ("cde", 169), ("abc", 195), ("ade", 189),
             ("abd", 117), ("abe", 117), ("acd", 39), ("ace", 39),
             ("bcd", 39), ("bce", 39), ("ac", 945), ("abcd", 3),
             ("abce", 3), ("abde", 27), ("acde", 9), ("bcde", 9),
             ("abcde", 1))

    def components(subset):
        parent = list(range(N))

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for name in subset:
            tab = tables[name]
            for i in range(N):
                ri = find(i)
                rj = find(tab[i])
                if ri != rj:
                    parent[ri] = rj
        return sum(1 for i in range(N) if find(i) == i)

    got = {}
    ok = True
    for subset, expected in TABLE:
        got[subset] = components(subset)
        ok &= got[subset] == expected
    for s1, c1 in TABLE:
        for s2, c2 in TABLE:
            if set(s1) < set(s2):
                ok &= c1 >= c2
    ok &= got["abcde"] == 1
    check("COMPONENTS",
          "the single cell component census matches the recorded"
          " table on all seventeen generator subsets, from {ac} at 945"
          " and {bde} = {cde} = 169 = 13^2 down to the full verb"
          " {abcde} at 1: one cell is connected by the five letters"
          " alone; monotonicity holds on every comparable pair"
          " (enlarging the set never increases the count)", ok)

    print("TWIST-J kernel connectivity witness (exact arithmetic)")
    print("every generator is affine with det 1; the CSUM coupling is"
          " SL2(F_5), order 120, preserving all 15 wedges")
    print("linear preserves the wedge strata, affine crosses exactly"
          " 62480 of 78125; one cell connects at {abcde} = 1")
    print()
    passed = 0
    for i, (name, okv) in enumerate(CHECKS, 1):
        tag = "PASS" if okv else "FAIL"
        if okv:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
