"""Local feasibility diagnosis from five-of-six rigidity.

For a charged edge e, a face f incident to e is BLOCKED when some
other charged edge e' incident to f demands a sign of f incompatible
with e's demand (a nonzero f must serve every charged boundary edge
with its forced sign).  A charged edge with fewer than five unblocked
slots is locally unfillable; report every such edge and its context.
"""
import sys
from kappa_lib import faces_of_edge, face_boundary, is_ternary, edge_d
from checker_witness import build_current
from repair_witness import add_bridges


def diagnose(j, tag):
    bad = []
    for e, je in j.items():
        blocked = 0
        for f in faces_of_edge(e):
            inc_e = next(i for ee, i in face_boundary(f) if ee == e)
            want = inc_e * je          # required sign of f to serve e
            for ee, inc2 in face_boundary(f):
                if ee == e or ee not in j:
                    continue
                if inc2 * j[ee] != want:
                    blocked += 1
                    break
        if 6 - blocked < 5:
            bad.append((e, blocked))
    print("%s: %d locally unfillable charged edges" % (tag, len(bad)))
    for e, b in bad[:12]:
        print("   edge %r  blocked slots %d" % (e, b))
    return bad


def main():
    for P, m, C, D in ((4, 2, 4, 4), (6, 3, 6, 6), (6, 4, 6, 6),
                       (8, 4, 6, 6)):
        j = build_current(P, m, C, D)
        bad0 = diagnose(j, "(%d,%d,%d,%d) pre-bridge" % (P, m, C, D))
        add_bridges(j, P, m, C, D)
        assert is_ternary(j) and edge_d(j) == {}
        bad1 = diagnose(j, "(%d,%d,%d,%d) bridged " % (P, m, C, D))
        if bad1 and not bad0:
            print("   -> introduced by bridges")
        print()


if __name__ == "__main__":
    main()
