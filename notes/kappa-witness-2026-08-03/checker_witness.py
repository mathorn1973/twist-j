"""Checkerboard-staircase witness candidate for the kappa falsifier.

Plane pattern in dirs (0,1), per layer (x2,x3) with sign
tau = (-1)^(x2+x3), alpha(v) = (-1)^(x0+x1):

    j(e_0(v)) = +alpha tau,   j(e_1(v)) = -alpha tau      (in region)

Bulk filling (exact local identity, verified here):
    n_01(v) = alpha tau                       serves 4 edges
    n_02(v) = alpha tau, n_12(v) = -alpha tau serve 2 edges each,
                                              e_2 dumps cancel
    n_03(v) = alpha tau g(x3), n_13 = -n_03,  g alternating in x3,
                                              serves 1, e_3 dumps cancel
    per charged edge: 2 + 2 + 1 = 5; per site 4 faces / 2 edges = 2.0

The finite carrier: per plane a closed serpentine of NE/SW diagonal
staircases (P steps, m hairpins) plus a return run outside the strip;
layers (x2,x3) in [0,C) x [0,D).  Boundary defects are computed and
reported; repair happens in a later stage.
"""
import sys
from kappa_lib import (unit4, addv, chain_d, edge_d, is_ternary,
                       check_connected_edge_simple)


def alpha(v):
    return -1 if (v[0] + v[1]) % 2 else 1


def tau(l):
    return -1 if (l[0] + l[1]) % 2 else 1


def plane_walk(P, m):
    """closed serpentine in the (x0,x1) plane: m hairpins of NE/SW
    staircases with P (+e0,+e1) pairs each, connectors, and a return
    run along x1 = -1.  Returns list of (vertex2d, dir2d, sign)."""
    steps = []
    v = (0, 0)

    def go(d, s):
        nonlocal v
        w = (v[0] + (s if d == 0 else 0), v[1] + (s if d == 1 else 0))
        base = v if s > 0 else w
        steps.append((base, d, s))
        v = w

    for k in range(m):
        for _i in range(P):          # NE staircase S1 from (2k, 0)
            go(0, +1)
            go(1, +1)
        go(0, +1)                    # top rung
        for _i in range(P):          # SW staircase S2 down
            go(1, -1)
            go(0, -1)
        # S2 ends at (2k+1, 0); bottom connector detours below the
        # strip to the next hairpin start (2k+2, 0)
        if k < m - 1:
            go(1, -1)
            go(0, +1)
            go(1, +1)
    # last hairpin ends at (2m-1, 0); return along x1 = -2
    assert v == (2 * m - 1, 0), v
    go(1, -1)
    go(1, -1)
    for _i in range(2 * m - 1):
        go(0, -1)
    go(1, +1)
    go(1, +1)
    assert v == (0, 0)
    seen = set()
    for (b2, d2, _s) in steps:
        assert (b2, d2) not in seen, "edge reused: %r" % ((b2, d2),)
        seen.add((b2, d2))
    return steps


def build_current(P, m, C, D):
    j = {}
    for x2 in range(C):
        for x3 in range(D):
            t = tau((x2, x3))
            for (b2, d2, s) in plane_walk(P, m):
                vertex = (b2[0], b2[1], x2, x3)
                e = (vertex, d2)
                assert e not in j
                j[e] = s * t
    return j


def build_bulk(j, C, D):
    """verified local recipe, laid per SITE over the core region:
    sites whose e_0 and e_1 edges are both charged with the exact
    checkerboard sign.  x2-boundary layers omit outward dir-2 faces
    and would need dir-3 densification (left to repair for now)."""
    deviant = []
    pattern0, pattern1 = set(), set()
    for (v, d), c in j.items():
        l = (v[2], v[3])
        at = alpha(v) * tau(l)
        want = at if d == 0 else -at
        if d in (0, 1) and c == want:
            (pattern0 if d == 0 else pattern1).add(v)
        else:
            deviant.append(((v, d), c))
    core = pattern0 & pattern1
    n = {}

    def put(f, c):
        if c == 0:
            return
        assert f not in n
        n[f] = c

    for v in core:
        l = (v[2], v[3])
        at = alpha(v) * tau(l)
        x2, x3 = v[2], v[3]
        boundary2 = x2 in (0, C - 1)
        if boundary2:
            g = 1 if x3 < D - 1 else 0
        else:
            g = (x3 + 1) % 2
        put((v, 0, 1), at)
        if x2 < C - 1:
            put((v, 0, 2), at)
            put((v, 1, 2), -at)
        if g:
            put((v, 0, 3), at)
            put((v, 1, 3), -at)
    return n, deviant, core


def defect_histogram(j, n, defect):
    """where do the defects sit?  classify by in-plane diagonal
    (x0 - x1) and by layer position kind."""
    by_diag = {}
    by_layer = {}
    for (v, d), c in defect.items():
        by_diag[v[0] - v[1]] = by_diag.get(v[0] - v[1], 0) + abs(c)
        by_layer[(v[2], v[3])] = by_layer.get((v[2], v[3]), 0) + abs(c)
    print("defect mass by diagonal x0-x1 (top 8):",
          sorted(by_diag.items(), key=lambda kv: -kv[1])[:8])
    print("defect mass by layer (top 8):",
          sorted(by_layer.items(), key=lambda kv: -kv[1])[:8])


def defect_report(j, n):
    dn = chain_d(n)
    want = {e: 5 * c for e, c in j.items()}
    defect = {}
    for e in set(dn) | set(want):
        d = want.get(e, 0) - dn.get(e, 0)
        if d:
            defect[e] = d
    # classify
    by_dir = {}
    for (v, d), c in defect.items():
        by_dir.setdefault(d, []).append(abs(c))
    print("defect edges: %d, total |defect| = %d"
          % (len(defect), sum(abs(c) for c in defect.values())))
    for d in sorted(by_dir):
        print("  dir %d: %d edges, max |c| = %d"
              % (d, len(by_dir[d]), max(by_dir[d])))
    return defect


def main():
    P, m, C, D = (int(x) for x in (sys.argv[1:5] or (6, 3, 6, 6)))
    j = build_current(P, m, C, D)
    assert is_ternary(j)
    assert edge_d(j) == {}
    L = len(j)
    print("current: L = %d edges (per plane %d, layers %d)"
          % (L, L // (C * D), C * D))
    n, deviant, core = build_bulk(j, C, D)
    assert is_ternary(n), "bulk not ternary"
    print("bulk faces F0 = %d, core sites = %d, deviant/plane = %d"
          % (len(n), len(core), len(deviant) // (C * D)))
    print("bulk-only ratio F0/L = %.4f  (target <= 2.8073)"
          % (len(n) / L))
    defect = defect_report(j, n)
    defect_histogram(j, n, defect)
    return j, n, defect


if __name__ == "__main__":
    main()
