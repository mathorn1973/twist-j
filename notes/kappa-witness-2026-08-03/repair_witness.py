"""Stage 3: connect layers, repair boundary defects with a shell ILP,
and verify the full kappa falsifier certificate exactly.

Bridges: reroute edge e_0(v) of layer l through layer l' = l + e_2 (or
e_3): the rerouted segment cancels the opposite-sign pattern edge of
l' exactly, so j stays ternary and closed and |supp j| is unchanged,
while supp j becomes connected across the two layers.
"""
import sys
from pathlib import Path
from kappa_lib import (unit4, addv, chain_d, edge_d, is_ternary,
                       check_connected_edge_simple, faces_of_edge,
                       face_boundary)
from checker_witness import (alpha, tau, plane_walk, build_current,
                             build_bulk)


def _local_ok(j, center, radius=3):
    """five-of-six local check on charged edges near center."""
    from kappa_lib import faces_of_edge, face_boundary
    cx = center
    for e, je in j.items():
        v = e[0]
        if max(abs(v[i] - cx[i]) for i in range(4)) > radius:
            continue
        blocked = 0
        for f in faces_of_edge(e):
            inc_e = next(i for ee, i in face_boundary(f) if ee == e)
            want = inc_e * je
            for ee, inc2 in face_boundary(f):
                if ee == e or ee not in j:
                    continue
                if inc2 * j[ee] != want:
                    blocked += 1
                    break
        if 6 - blocked < 5:
            return False
    return True


def add_bridges(j, P, m, C, D):
    """serpentine over the (x2,x3) grid; one bridge per adjacent layer
    pair.  Each bridge reroutes one dir-0 or dir-1 pattern edge of the
    lower layer through its neighbor, where the opposite pattern sign
    cancels; anchors are searched until the five-of-six local check
    stays clean."""
    order = []
    for x2 in range(C):
        rng = range(D) if x2 % 2 == 0 else range(D - 1, -1, -1)
        for x3 in rng:
            order.append((x2, x3))
    bridges = []
    for i in range(len(order) - 1):
        l, l2 = order[i], order[i + 1]
        d23 = 2 if l[0] != l2[0] else 3
        lo = l if l[d23 - 2] < l2[d23 - 2] else l2
        placed = False
        for d01 in (0, 1):
            if placed:
                break
            for k in range(m):
                if placed:
                    break
                for shalf in range(1, P):
                    x0, x1 = 2 * k + shalf, shalf
                    v = (x0, x1, lo[0], lo[1])
                    e_here = (v, d01)
                    e_there = (addv(v, unit4(d23)), d01)
                    b1 = (v, d23)
                    b2 = (addv(v, unit4(d01)), d23)
                    if e_here not in j or e_there not in j:
                        continue
                    if b1 in j or b2 in j:
                        continue
                    c = j[e_here]
                    if j[e_there] != -c:
                        continue
                    del j[e_here]
                    del j[e_there]
                    j[b1] = c
                    j[b2] = -c
                    if _local_ok(j, v):
                        bridges.append((v, d01, d23))
                        placed = True
                        break
                    j[e_here] = c
                    j[e_there] = -c
                    del j[b1]
                    del j[b2]
        assert placed, "no clean bridge for layer pair %d" % i
    return bridges


def shell_ilp(j, n, defect, rings=2, time_limit=600):
    import pulp
    var_faces = set()
    frontier = set(defect)
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
    print("ILP: %d variable faces, %d edge constraints"
          % (len(var_faces), len(cons_edges)))
    prob = pulp.LpProblem("repair", pulp.LpMinimize)
    xp = {f: pulp.LpVariable("p%d" % i, 0, 1, cat="Binary")
          for i, f in enumerate(var_faces)}
    xm = {f: pulp.LpVariable("m%d" % i, 0, 1, cat="Binary")
          for i, f in enumerate(var_faces)}
    prob += pulp.lpSum(list(xp.values()) + list(xm.values()))
    for e in cons_edges:
        terms = []
        fixed = 0
        for f in faces_of_edge(e):
            inc = next(i for ee, i in face_boundary(f) if ee == e)
            if f in xp:
                terms.append(inc * (xp[f] - xm[f]))
            else:
                fixed += inc * n.get(f, 0)
        prob += (pulp.lpSum(terms) + fixed == 5 * j.get(e, 0),
                 "e%d_%s" % (len(prob.constraints), "x"))
    try:
        solver = pulp.HiGHS(msg=True, timeLimit=time_limit)
        assert solver.available()
    except Exception:
        solver = pulp.PULP_CBC_CMD(msg=1, timeLimit=time_limit)
    status = prob.solve(solver)
    print("ILP status:", pulp.LpStatus[status])
    if pulp.LpStatus[status] != "Optimal":
        return None
    patch = {}
    try:
        for f in var_faces:
            val = round(xp[f].value() or 0) - round(xm[f].value() or 0)
            patch[f] = val
    except Exception:
        return None
    return patch


def main():
    P, m, C, D = (int(x) for x in (sys.argv[1:5] or (6, 3, 6, 6)))
    rings = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    tl = int(sys.argv[6]) if len(sys.argv) > 6 else 600
    j = build_current(P, m, C, D)
    add_bridges(j, P, m, C, D)
    assert is_ternary(j) and edge_d(j) == {}
    L, walk = check_connected_edge_simple(j)
    print("current: L = %d, connected closed, Eulerian walk certified"
          % L)
    n, deviant, core = build_bulk(j, C, D)
    dn = chain_d(n)
    defect = {}
    for e in set(dn) | set(j):
        d = 5 * j.get(e, 0) - dn.get(e, 0)
        if d:
            defect[e] = d
    print("defect edges %d, mass %d"
          % (len(defect), sum(abs(c) for c in defect.values())))
    patch = shell_ilp(j, n, defect, rings, tl)
    assert patch is not None, "ILP failed"
    for f, val in patch.items():
        if val == 0:
            n.pop(f, None)
        else:
            n[f] = val
    # final exact verification
    assert is_ternary(n), "final n not ternary"
    dn = chain_d(n)
    want = {e: 5 * c for e, c in j.items()}
    assert dn == want, "partial n != 5j"
    F = len(n)
    print("WITNESS: L = %d, F = %d, F/L = %.4f" % (L, F, F / L))
    ok = 2 ** F <= 7 ** L
    print("exact check 2^F <= 7^L:", ok)
    if ok:
        import json
        out = {"P": P, "m": m, "C": C, "D": D, "L": L, "F": F,
               "j": [[list(v), d, c] for (v, d), c in sorted(j.items())],
               "n": [[list(v), a, b, c]
                     for (v, a, b), c in sorted(n.items())]}
        output = Path("witness_%d_%d_%d_%d.json" % (P, m, C, D))
        if output.exists():
            raise FileExistsError("refusing to overwrite %s" % output)
        with output.open("x", encoding="utf-8") as fh:
            json.dump(out, fh)
        print("witness written:", output)


if __name__ == "__main__":
    main()
