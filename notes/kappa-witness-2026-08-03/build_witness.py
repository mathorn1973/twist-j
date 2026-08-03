"""Stage 1+2: the slab current j(n, K) and the bulk filling.

Current (section 7.1 family of the kappa predefinition note):
  columns over S_n = {0,1} x [n]^2 in coords (1,2,3), K strand edges
  each in direction 0, closed by the two matchings of a Hamiltonian
  cycle on S_n.  Strand sign at column v is the checkerboard parity
  sigma(v) = (-1)^(v1+v2+v3) (up to one global sign fixed by the cycle).

Bulk filling per t-slice:
  dir-1 faces f_01 at x1=0, value sigma; transverse dirs 2,3 solved as
  an exact min-cost unit-capacity flow with cell imbalance 4*sigma.
"""
import sys
from collections import deque
from kappa_lib import (unit4, addv, chain_d, edge_d, is_ternary,
                       check_connected_edge_simple, face_boundary)


def sigma3(v):
    return -1 if (v[0] + v[1] + v[2]) % 2 else 1


def ham_cycle(n):
    """Hamiltonian cycle on {0,1} x [n]^2 (coords (x1,x2,x3)),
    n even; consecutive vertices are lattice neighbors."""
    layer0 = []
    for x3 in range(n):
        row = list(range(n)) if x3 % 2 == 0 else list(range(n - 1, -1, -1))
        for x2 in row:
            layer0.append((0, x2, x3))
    cyc = layer0 + [(1, v[1], v[2]) for v in reversed(layer0)]
    m = len(cyc)
    for i in range(m):
        a, b = cyc[i], cyc[(i + 1) % m]
        d = sum(abs(x - y) for x, y in zip(a, b))
        assert d == 1, "not a lattice step at %d" % i
    assert len(set(cyc)) == 2 * n * n
    return cyc


def build_current(n, K):
    cyc = ham_cycle(n)
    m = len(cyc)
    # global sign: make strand coefficient equal sigma3
    flip = 1 if sigma3(cyc[0]) == 1 else -1
    j = {}
    for i, v in enumerate(cyc):
        s = flip * (1 if i % 2 == 0 else -1)
        assert s == sigma3(v), "cycle parity mismatch"
        for t in range(K):
            j[((t,) + v, 0)] = s
    # matching edges: even i at top (x0=K), odd i at bottom (x0=0)
    for i in range(m):
        a, b = cyc[i], cyc[(i + 1) % m]
        t0 = K if i % 2 == 0 else 0
        # traversal direction along the polygon: even strand ends up,
        # crosses a->b at top; odd strand ends down, crosses a->b at
        # bottom -- both traverse a->b, with the polygon sign flip
        d = next(k for k in range(3) if a[k] != b[k])
        s = flip * (1 if b[d] > a[d] else -1)
        base = a if b[d] > a[d] else b
        e = ((t0,) + base, d + 1)
        assert e not in j
        j[e] = s
    return j, cyc


def flow2d(n, pad=4):
    """min-cost unit-cap flow on the padded 2D grid: cell imbalance
    4*sigma0 inside [n]^2, sigma0(x)=(-1)^(x2+x3); returns (u, w) as
    {(x2,x3): coeff} for face dirs 2 and 3, plus the support cost."""
    lo, hi = -pad, n - 1 + pad
    cells = [(a, b) for a in range(lo, hi + 1) for b in range(lo, hi + 1)]
    idx = {c: i for i, c in enumerate(cells)}
    N = len(cells)
    S, T = N, N + 1
    # arcs: [to, cap, cost, flow]; adjacency of arc ids
    arcs = []
    adj = [[] for _ in range(N + 2)]

    def add(a, b, cap, cost):
        adj[a].append(len(arcs))
        arcs.append([b, cap, cost, 0])
        adj[b].append(len(arcs))
        arcs.append([a, 0, -cost, 0])

    for c in cells:
        for d in ((1, 0), (0, 1)):
            c2 = (c[0] + d[0], c[1] + d[1])
            if c2 in idx:
                add(idx[c], idx[c2], 1, 1)
                add(idx[c2], idx[c], 1, 1)
    total = 0
    for c in cells:
        if 0 <= c[0] < n and 0 <= c[1] < n:
            s0 = 1 if (c[0] + c[1]) % 2 == 0 else -1
            if s0 == -1:          # net outflow 4: source side
                add(S, idx[c], 4, 0)
                total += 4
            else:                 # net inflow 4: sink side
                add(idx[c], T, 4, 0)
    # successive shortest paths (SPFA)
    sent = 0
    cost = 0
    while sent < total:
        dist = {S: 0}
        inq = deque([S])
        pre = {}
        while inq:
            a = inq.popleft()
            for ai in adj[a]:
                to, cap, c_, fl = arcs[ai]
                if cap - fl > 0 and dist.get(a, 10**9) + c_ \
                        < dist.get(to, 10**9):
                    dist[to] = dist[a] + c_
                    pre[to] = ai
                    inq.append(to)
        assert T in dist, "flow infeasible"
        # bottleneck
        b = 10**9
        v = T
        while v != S:
            ai = pre[v]
            b = min(b, arcs[ai][1] - arcs[ai][3])
            v = arcs[ai ^ 1][0]
        v = T
        while v != S:
            ai = pre[v]
            arcs[ai][3] += b
            arcs[ai ^ 1][3] -= b
            v = arcs[ai ^ 1][0]
        sent += b
        cost += b * dist[T]
    # extract u (dir 2) and w (dir 3): face at base cell x delivers
    # +coeff to cell x and -coeff to cell x+e_dir, i.e. flow from
    # x+e_dir into x of size coeff
    u, w = {}, {}
    for c in cells:
        for d, store in (((1, 0), u), ((0, 1), w)):
            c2 = (c[0] + d[0], c[1] + d[1])
            if c2 not in idx:
                continue
            net = 0
            for ai in adj[idx[c2]]:
                to, cap, c_, fl = arcs[ai]
                if to == idx[c] and cap > 0 and c_ == 1:
                    net += fl
            for ai in adj[idx[c]]:
                to, cap, c_, fl = arcs[ai]
                if to == idx[c2] and cap > 0 and c_ == 1:
                    net -= fl
            if net:
                store[c] = net
    # exact recheck of the divergence equation
    allc = set()
    for c in list(u) + list(w):
        allc.add(c)
        allc.add((c[0] + 1, c[1]))
        allc.add((c[0], c[1] + 1))
    for c in set(cells) | allc:
        div = (u.get(c, 0) - u.get((c[0] - 1, c[1]), 0)
               + w.get(c, 0) - w.get((c[0], c[1] - 1), 0))
        want = 0
        if 0 <= c[0] < n and 0 <= c[1] < n:
            want = 4 * (1 if (c[0] + c[1]) % 2 == 0 else -1)
        assert div == want, "divergence mismatch at %r" % (c,)
    assert is_ternary(u) and is_ternary(w)
    return u, w, cost


def build_bulk(n, K, u, w):
    """bulk faces for t in [0, K-1]; x1=1 slice uses the negated 2D
    pattern (sigma flips with x1); dir-1 faces at x1=0 with value
    sigma3."""
    nb = {}
    for t in range(K):
        for x2 in range(n):
            for x3 in range(n):
                v = (t, 0, x2, x3)
                nb[(v, 0, 1)] = sigma3((0, x2, x3))
        for x1 in (0, 1):
            s = 1 if x1 == 0 else -1
            for (a, b), c in u.items():
                nb[((t, x1, a, b), 0, 2)] = s * c
            for (a, b), c in w.items():
                nb[((t, x1, a, b), 0, 3)] = s * c
    return nb


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    j, cyc = build_current(n, K)
    L, _walk = check_connected_edge_simple(j)
    assert L == 2 * n * n * (K + 1)
    print("current OK: n=%d K=%d L=%d connected edge-simple closed" %
          (n, K, L))
    u, w, cost2d = flow2d(n)
    print("2D flow: support cost c2=%d (per-slice budget %d, LB-share %d)"
          % (cost2d, (5 * n * n + 4 * n - n * n) // 2 + 3,
             (5 * n * n + 4 * n - n * n) // 2))
    per_slice = n * n + 2 * cost2d
    print("per-t-slice faces = %d (LB per slice = %d)" %
          (per_slice, 5 * n * n + 4 * n))
    nb = build_bulk(n, K, u, w)
    assert is_ternary(nb)
    print("bulk faces = %d (= %d * K? %s)" %
          (len(nb), per_slice, len(nb) == per_slice * K))
    # residue: what the caps must still supply
    dn = chain_d(nb)
    res = {}
    for e, c in dn.items():
        want = 5 * j.get(e, 0)
        if c != want:
            res[e] = want - c
    for e, c in j.items():
        if e not in dn and e not in res:
            res[e] = 5 * c
    # where does the residue live?
    t_vals = sorted({e[0][0] for e in res})
    dirs = sorted({e[1] for e in res})
    print("residue edges = %d, t-range %s..%s, dirs %s" %
          (len(res), t_vals[0], t_vals[-1], dirs))
    interior = [e for e in res if 0 < e[0][0] < K]
    print("residue strictly inside 0<t<K: %d (must be 0)" % len(interior))
    # check bulk satisfied every strand edge exactly
    bad = [e for e, c in dn.items() if e[1] == 0 and c != 5 * j.get(e, 0)]
    print("longitudinal edges wrong: %d (must be 0)" % len(bad))
    return j, nb, res


if __name__ == "__main__":
    main()
