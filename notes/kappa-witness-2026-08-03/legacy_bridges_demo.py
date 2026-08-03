"""Reproduction artifact: the ORIGINAL fixed-formula bridge placement
(before the searched-anchor fix) and the local five-of-six obstruction
it creates.  This is the placement that made the (6,3,6,6) shell MIPs
infeasible; the archived add_bridges in repair_witness.py searches
anchors under the local check and does not exhibit the failure."""
from kappa_lib import addv, unit4, is_ternary, edge_d
from checker_witness import build_current
from diagnose_local import diagnose


def add_bridges_legacy(j, P, m, C, D):
    order = []
    for x2 in range(C):
        rng = range(D) if x2 % 2 == 0 else range(D - 1, -1, -1)
        for x3 in rng:
            order.append((x2, x3))
    for i in range(len(order) - 1):
        l, l2 = order[i], order[i + 1]
        d23 = 2 if l[0] != l2[0] else 3
        lo = l if (l[0] + l[1]) < (l2[0] + l2[1]) else l2
        k = 1 + (i % max(1, m - 1))
        s = 2 + 2 * ((i // max(1, m - 1)) % max(1, P - 2))
        x0, x1 = 2 * k + s // 2, s // 2
        v = (x0, x1, lo[0], lo[1])
        e_here = (v, 0)
        e_there = (addv(v, unit4(d23)), 0)
        c = j[e_here]
        assert j[e_there] == -c
        del j[e_here]
        del j[e_there]
        j[(v, d23)] = c
        j[(addv(v, unit4(0)), d23)] = -c


def main():
    for shape in ((4, 2, 4, 4), (6, 3, 6, 6)):
        j = build_current(*shape)
        add_bridges_legacy(j, *shape)
        assert is_ternary(j) and edge_d(j) == {}
        diagnose(j, "%s legacy-bridged" % (shape,))


if __name__ == "__main__":
    main()
