#!/usr/bin/env python3
"""Exact finite-rank verifier for the W2K-C IT2 breaker.

NON-CANONICAL. Standard library only. No floating point.

It builds the minimal graded category forced by:
  * source self Ext dimensions (1,r,8+2r,r,1);
  * pairwise source cross Ext concentrated in degree 2 with dimension 10;
  * perfect degree-2 x degree-2 Serre pairing into top degree;
  * W2K-A L-shaped outer cells and factorwise degree-2 arrows.

The twisted endomorphism differential is represented over a large prime field.
"""

from collections import defaultdict

P = 1000003


def source_homs(i, j, r):
    e = 8 + 2 * r
    dims = (1, r, e, r, 1)
    out = []
    if i == j:
        for d, n in enumerate(dims):
            for k in range(n):
                out.append((d, ("S", i, d, k)))
    else:
        for k in range(10):
            out.append((2, ("X", i, j, k)))
    return out


def source_comp(g, f):
    # f:i->j, g:j->k. Only compositions involving the selected IT2 structure
    # are needed for [q,-].
    if f[0] == "S":
        _, fi, df, kf = f
        fj = fi
    else:
        _, fi, fj, kf = f
        df = 2
    if g[0] == "S":
        _, gj, dg, kg = g
        gk = gj
    else:
        _, gj, gk, kg = g
        dg = 2
    if fj != gj:
        return []
    if g[0] == "S" and dg == 0:
        return [(1, f)]
    if f[0] == "S" and df == 0:
        return [(1, g)]
    if f[0] == "X" and g[0] == "X" and fi == gk and kf == kg:
        return [(1, ("S", fi, 4, 0))]
    # Positive self Ext composed with an IT2 cross class would land in a
    # cross degree >2, which is zero by hypothesis.
    return []


def outer_homs(a, b, r):
    out = []
    for d1, x1 in source_homs(a[0], b[0], r):
        for d2, x2 in source_homs(a[1], b[1], r):
            out.append((d1 + d2, (x1, x2, d1, d2)))
    return out


def outer_comp(g, f):
    g1, g2, gd1, gd2 = g
    f1, f2, fd1, fd2 = f
    c1 = source_comp(g1, f1)
    c2 = source_comp(g2, f2)
    sign = -1 if (gd2 * fd1) % 2 else 1
    out = []
    for a, y1 in c1:
        for b, y2 in c2:
            out.append((sign * a * b, (y1, y2, gd1 + fd1, gd2 + fd2)))
    return out


CELLS = {
    "1": ((1, 0), 0),
    "2": ((0, 2), 0),
    "0": ((0, 0), 1),
}


def find_tag(a, b, degree, pred, r):
    for d, t in outer_homs(a, b, r):
        if d == degree and pred(t):
            return t
    raise AssertionError("tag not found")


def qs(r):
    q1 = find_tag(
        (1, 0), (0, 0), 2,
        lambda t: t[0][0] == "X" and t[0][3] == 0 and t[1][0] == "S" and t[1][2] == 0,
        r,
    )
    q2 = find_tag(
        (0, 2), (0, 0), 2,
        lambda t: t[1][0] == "X" and t[1][3] == 0 and t[0][0] == "S" and t[0][2] == 0,
        r,
    )
    return {("1", "0"): q1, ("2", "0"): q2}


def total_basis(n, r):
    out = []
    for ci, (oi, si) in CELLS.items():
        for cj, (oj, sj) in CELLS.items():
            d = n + sj - si
            if d < 0:
                continue
            for dd, t in outer_homs(oi, oj, r):
                if dd == d:
                    out.append((ci, cj, t))
    return out


def differential(n, r):
    qmap = qs(r)
    src = total_basis(n, r)
    dst = total_basis(n + 1, r)
    pos = {b: i for i, b in enumerate(dst)}
    cols = []
    for ci, cj, t in src:
        v = defaultdict(int)
        # q after x
        for (a, b), qt in qmap.items():
            if a == cj:
                for c, tt in outer_comp(qt, t):
                    key = (ci, b, tt)
                    if key in pos:
                        v[pos[key]] = (v[pos[key]] + c) % P
        # x after q, with graded commutator sign
        sign = -1 if n % 2 == 0 else 1
        for (a, b), qt in qmap.items():
            if b == ci:
                for c, tt in outer_comp(t, qt):
                    key = (a, cj, tt)
                    if key in pos:
                        v[pos[key]] = (v[pos[key]] + sign * c) % P
        cols.append({i: c for i, c in v.items() if c % P})
    return len(src), len(dst), cols


def sparse_rank(cols):
    piv = {}
    rk = 0
    for col in cols:
        v = dict(col)
        while v:
            row = min(v)
            if row not in piv:
                inv = pow(v[row], -1, P)
                v = {i: (a * inv) % P for i, a in v.items()}
                piv[row] = v
                rk += 1
                break
            f = v[row]
            pv = piv[row]
            for i, a in pv.items():
                x = (v.get(i, 0) - f * a) % P
                if x:
                    v[i] = x
                else:
                    v.pop(i, None)
    return rk


def audit(r):
    d1_src, d1_dst, M1 = differential(1, r)
    d2_src, d2_dst, M2 = differential(2, r)
    rk1 = sparse_rank(M1)
    rk2 = sparse_rank(M2)
    e = 8 + 2 * r
    expected_D1 = 6 * r + 20
    expected_D2 = 3 * r * r + 32 * r + 48
    expected_rk1 = 2 * r
    expected_rk2 = 2 * e
    expected_h2 = 3 * r * r + 26 * r + 32
    assert d1_src == expected_D1
    assert d1_dst == expected_D2
    assert d2_src == expected_D2
    assert rk1 == expected_rk1
    assert rk2 == expected_rk2
    h2 = expected_D2 - rk1 - rk2
    assert h2 == expected_h2
    return (d1_src, d2_src, rk1, rk2, h2)


for r in (12, 13, 17):
    audit(r)

D1, D2, R1, R2, H2 = audit(12)
assert H2 == 776
assert H2 > 104

print("r                              =", 12)
print("raw D1, D2                     =", D1, D2)
print("rank d1, d2                    =", R1, R2)
print("Ext2                            =", H2)
print("W2K-B semiregularity target     =", 104)
print("RESULT: W2K-C generic IT2 route FAIL")