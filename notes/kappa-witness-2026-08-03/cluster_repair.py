"""Clustered repair: group defect edges into connected clusters (via
shared faces), then fix each cluster with a local ILP whose shell
radius grows on infeasibility.  Sequential application with defect
recomputation keeps the state exact at every step."""
import sys
import json
from kappa_lib import (chain_d, edge_d, is_ternary, faces_of_edge,
                       face_boundary, check_connected_edge_simple)
from checker_witness import build_current, build_bulk
from repair_witness import add_bridges


def compute_defect(j, n):
    dn = chain_d(n)
    defect = {}
    for e in set(dn) | set(j):
        d = 5 * j.get(e, 0) - dn.get(e, 0)
        if d:
            defect[e] = d
    return defect


def clusters_of(defect):
    """union defect edges that share a face (distance-1 coupling)."""
    parent = {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for e in defect:
        parent[e] = e
    by_face = {}
    for e in defect:
        for f in faces_of_edge(e):
            by_face.setdefault(f, []).append(e)
    for edges in by_face.values():
        for e in edges[1:]:
            union(edges[0], e)
    out = {}
    for e in defect:
        out.setdefault(find(e), []).append(e)
    return list(out.values())


def solve_cluster(j, n, cluster, rings, time_limit=120):
    import pulp
    var_faces = set()
    frontier = set(cluster)
    for _r in range(rings):
        newf = set()
        for e in frontier:
            for f in faces_of_edge(e):
                if f not in var_faces:
                    var_faces.add(f)
                    newf.add(f)
        frontier = set()
        for f in newf:
            for e, _inc in face_boundary(f):
                frontier.add(e)
    cons_edges = set()
    for f in var_faces:
        for e, _inc in face_boundary(f):
            cons_edges.add(e)
    prob = pulp.LpProblem("c", pulp.LpMinimize)
    xp = {f: pulp.LpVariable("p%d" % i, 0, 1, cat="Binary")
          for i, f in enumerate(var_faces)}
    xm = {f: pulp.LpVariable("m%d" % i, 0, 1, cat="Binary")
          for i, f in enumerate(var_faces)}
    prob += pulp.lpSum(list(xp.values()) + list(xm.values()))
    for k, e in enumerate(cons_edges):
        terms = []
        fixed = 0
        for f in faces_of_edge(e):
            inc = next(i for ee, i in face_boundary(f) if ee == e)
            if f in xp:
                terms.append(inc * (xp[f] - xm[f]))
            else:
                fixed += inc * n.get(f, 0)
        prob += pulp.lpSum(terms) + fixed == 5 * j.get(e, 0), "e%d" % k
    try:
        solver = pulp.HiGHS(msg=False, timeLimit=time_limit)
        assert solver.available()
    except Exception:
        solver = pulp.PULP_CBC_CMD(msg=0, timeLimit=time_limit)
    status = prob.solve(solver)
    if pulp.LpStatus[status] != "Optimal":
        return None
    return {f: round((xp[f].value() or 0)) - round((xm[f].value() or 0))
            for f in var_faces}


def main():
    P, m, C, D = (int(x) for x in (sys.argv[1:5] or (6, 3, 6, 6)))
    j = build_current(P, m, C, D)
    add_bridges(j, P, m, C, D)
    assert is_ternary(j) and edge_d(j) == {}
    L, _walk = check_connected_edge_simple(j)
    print("current: L = %d connected closed" % L)
    n, deviant, core = build_bulk(j, C, D)
    defect = compute_defect(j, n)
    print("defect edges %d mass %d"
          % (len(defect), sum(abs(c) for c in defect.values())))
    cls = clusters_of(defect)
    cls.sort(key=len)
    print("clusters: %d, sizes %s%s"
          % (len(cls), [len(c) for c in cls[:12]],
             "..." if len(cls) > 12 else ""))
    total = len(cls)
    for i, cluster in enumerate(cls):
        # cluster membership may be stale after earlier patches
        cluster = [e for e in cluster if e in compute_defect(j, n)] \
            if i else cluster
        if not cluster:
            continue
        patch = None
        for rings in (3, 4, 5, 6):
            patch = solve_cluster(j, n, cluster, rings)
            if patch is not None:
                break
        assert patch is not None, "cluster %d unsolved" % i
        for f, val in patch.items():
            if val == 0:
                n.pop(f, None)
            else:
                n[f] = val
        if (i + 1) % 10 == 0 or i + 1 == total:
            print("  cluster %d/%d done (rings=%d), F now %d"
                  % (i + 1, total, rings, len(n)))
    defect = compute_defect(j, n)
    assert not defect, "residual defects: %d" % len(defect)
    assert is_ternary(n)
    F = len(n)
    print("WITNESS: L = %d  F = %d  F/L = %.4f" % (L, F, F / L))
    ok = 2 ** F <= 7 ** L
    print("exact 2^F <= 7^L:", ok)
    out = {"P": P, "m": m, "C": C, "D": D, "L": L, "F": F, "ok": ok,
           "j": [[list(v), d, c] for (v, d), c in sorted(j.items())],
           "n": [[list(v), a, b, c]
                 for (v, a, b), c in sorted(n.items())]}
    with open("witness_%d_%d_%d_%d.json" % (P, m, C, D), "w") as fh:
        json.dump(out, fh)
    print("witness json written")


if __name__ == "__main__":
    main()
