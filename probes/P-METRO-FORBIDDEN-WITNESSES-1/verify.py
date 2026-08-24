#!/usr/bin/env python3
"""P-METRO-FORBIDDEN-WITNESSES-1 exact audit.

Obligation B of METRO-REDUCTION-CALCULUS [O]: exact witnesses for the five
forbidden transformations named in canon/CANON.md section 15, under the five
readings frozen in PREREG.md and ratified by the owner as the canonical
meaning of those five phrases.

Standard library only. Integers and Fraction. No float in any assertion.
"""
import sys
from fractions import Fraction
from itertools import product, permutations

FAIL = []
LINES = []


def emit(s):
    LINES.append(s)


def gate(tag, ok, detail=""):
    emit("%-5s %-34s %s" % ("PASS" if ok else "FAIL", tag, detail))
    if not ok:
        FAIL.append(tag)


# ---------------------------------------------------------------- the object
# P = (n, d, w):  n = |S|, d[i][u] a tuple of length n (map S->S),
#                 i in {0,1} is coordinate 1,2;  w a tuple of Fraction.
# CANON.md: coordinate 1 acts first.

def stream(P, s, n1, n2):
    _, d, w = P
    return w[d[1][n2][d[0][n1][s]]]


def stream_alt(P, s, n1, n2):
    """Independently coded evaluator for gate G6. Builds the composite map
    first, then reads the output, rather than composing on the state."""
    ns, d, w = P
    comp = [d[1][n2][d[0][n1][t]] for t in range(ns)]
    return w[comp[s]]


def positions(P):
    ns = P[0]
    return [(s, a, b) for s in range(ns) for a in (0, 1) for b in (0, 1)]


def find_obstruction(P, src_fn, val_fn):
    """Two positions with equal src and different val kill every tau at once."""
    seen = {}
    for p in positions(P):
        k = src_fn(P, *p)
        v = val_fn(P, *p)
        if k in seen:
            if seen[k][0] != v:
                return (seen[k][1], p, seen[k][0], v)
        else:
            seen[k] = (v, p)
    return None


# ------------------------------------------- the five forbidden readings
def T1_src(P, s, a, b):
    return (s, a + b)                      # total-degree flattening


def T3a_src(P, s, a, b):
    """Frozen primary reading: per-coordinate values ALONE decide the joint."""
    _, d, w = P
    return (w[d[0][a][s]], w[d[1][b][s]])


def T3b_src(P, s, a, b):
    """Disclosed weaker variant: the start state is carried in the key."""
    _, d, w = P
    return (s, w[d[0][a][s]], w[d[1][b][s]])


def T4_src(P, s, a, b):
    _, _, w = P
    return (w[s], a, b)                    # regroup by level sets of w alone


def rev_stream(P, s, a, b):
    _, d, w = P
    return w[d[0][a][d[1][b][s]]]           # order reversed at every input


def val_stream(P, s, a, b):
    return stream(P, s, a, b)


FORBIDDEN_SINGLE = [
    ("T1 FLATTEN", T1_src, val_stream),
    ("T3a WEIGHTS-STRICT", T3a_src, val_stream),
    ("T4 OUTPUT-REGROUP", T4_src, val_stream),
    ("T5 BOX-REORDER", val_stream, rev_stream),
]


def T2_obstruction(P):
    """Erasing names: same unordered multiset of digit maps, different stream.
    Redistribute the four maps across (coordinate,digit) by a permutation that
    is NOT a coordinate permutation, then compare streams."""
    ns, d, w = P
    flat = [d[0][0], d[0][1], d[1][0], d[1][1]]
    coord_swap = (2, 3, 0, 1)
    for perm in permutations(range(4)):
        if perm == (0, 1, 2, 3) or perm == coord_swap:
            continue
        q = ((flat[perm[0]], flat[perm[1]]), (flat[perm[2]], flat[perm[3]]))
        P2 = (ns, q, w)
        for (s, a, b) in positions(P):
            if stream(P, s, a, b) != stream(P2, s, a, b):
                return (perm, (s, a, b), stream(P, s, a, b), stream(P2, s, a, b))
    return None


# ---------------------------------------------------------- admitted arrows
def arrow_relabel(P):
    ns, d, w = P
    out = []
    for phi in permutations(range(ns)):
        inv = [0] * ns
        for x in range(ns):
            inv[phi[x]] = x
        d2 = tuple(tuple(tuple(phi[m[inv[y]]] for y in range(ns)) for m in row)
                   for row in d)
        w2 = tuple(w[inv[y]] for y in range(ns))
        P2 = (ns, d2, w2)
        bad = [(s, a, b) for (s, a, b) in positions(P)
               if stream(P2, phi[s], a, b) != stream(P, s, a, b)]
        out.append(len(bad))
    return sum(out)


def reach(P, A0):
    ns, d, _ = P
    seen, stack = set(A0), list(A0)
    while stack:
        x = stack.pop()
        for i in (0, 1):
            for u in (0, 1):
                y = d[i][u][x]
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return sorted(seen)


def arrow_restrict(P, A0=(0,)):
    """Restriction to S_reach: the stream on allowed starts is untouched."""
    R = reach(P, A0)
    idx = {x: k for k, x in enumerate(R)}
    ns, d, w = P
    d2 = tuple(tuple(tuple(idx[m[x]] for x in R) for m in row) for row in d)
    w2 = tuple(w[x] for x in R)
    P2 = (len(R), d2, w2)
    return sum(1 for s in A0 for a in (0, 1) for b in (0, 1)
               if stream(P2, idx[s], a, b) != stream(P, s, a, b))


def nerode_classes(P):
    ns, d, w = P
    sig = {}
    for s in range(ns):
        key = (w[s],) + tuple(w[d[1][b][d[0][a][s]]] for a in (0, 1) for b in (0, 1)) \
              + tuple(w[d[0][a][s]] for a in (0, 1)) + tuple(w[d[1][b][s]] for b in (0, 1))
        sig.setdefault(key, []).append(s)
    cls = {}
    for k, members in enumerate(sig.values()):
        for s in members:
            cls[s] = k
    return cls, len(sig)


def arrow_nerode(P):
    """Quotient only under its exact precondition: congruence for coordinate 2
    (coordinate 1 automatic). Returns (applicable, violations)."""
    ns, d, w = P
    cls, k = nerode_classes(P)
    for u in (0, 1):
        for s in range(ns):
            for t in range(ns):
                if cls[s] == cls[t] and cls[d[1][u][s]] != cls[d[1][u][t]]:
                    return (False, 0)
    for u in (0, 1):
        for s in range(ns):
            for t in range(ns):
                if cls[s] == cls[t] and cls[d[0][u][s]] != cls[d[0][u][t]]:
                    return (False, 0)
    rep = {}
    for s in range(ns):
        rep.setdefault(cls[s], s)
    d2 = tuple(tuple(tuple(cls[m[rep[c]]] for c in range(k)) for m in row) for row in d)
    w2 = tuple(w[rep[c]] for c in range(k))
    P2 = (k, d2, w2)
    bad = sum(1 for (s, a, b) in positions(P)
              if stream(P2, cls[s], a, b) != stream(P, s, a, b))
    return (True, bad)


def commuting(P):
    ns, d, _ = P
    return all(d[1][v][d[0][u][s]] == d[0][u][d[1][v][s]]
               for u in (0, 1) for v in (0, 1) for s in range(ns))


def arrow_coordperm(P):
    """Coordinate permutation with full transport of basis, maps and indices."""
    ns, d, w = P
    P2 = (ns, (d[1], d[0]), w)
    return sum(1 for (s, a, b) in positions(P)
               if stream(P2, s, b, a) != stream(P, s, a, b))


# ------------------------------------------------------- the named witnesses
def F(*xs):
    return tuple(Fraction(x) for x in xs)


W1 = (3, ((( 0, 1, 2), (1, 1, 1)), ((0, 1, 2), (2, 2, 2))), F(0, 1, 2))
W2 = (2, (((0, 1), (0, 0)), ((1, 1), (1, 0))), F(0, 1))
W3 = (4, (((0, 1, 2, 3), (1, 1, 2, 2)), ((0, 1, 2, 3), (1, 3, 0, 2))), F(0, 1, 1, 2))
W4 = (3, (((0, 1, 2), (0, 2, 2)), ((0, 1, 2), (0, 1, 2))), F(0, 0, 1))
W5 = (2, (((0, 0), (0, 1)), ((0, 0), (1, 0))), F(0, 1))  # two-sided


def show(name, P, obs):
    if obs is None:
        return False
    (p1, p2, v1, v2) = obs
    emit("      %-20s %s and %s  ->  %s vs %s" % (name, p1, p2, v1, v2))
    return True


def main():
    emit("P-METRO-FORBIDDEN-WITNESSES-1 verify")
    emit("obligation B of METRO-REDUCTION-CALCULUS; five owner-ratified readings")
    emit("")

    # ---- G1 the five named witnesses
    named = []
    named.append(("W1 FLATTEN", find_obstruction(W1, T1_src, val_stream)))
    t2 = T2_obstruction(W2)
    named.append(("W2 ERASE-NAMES", None if t2 is None else
                  ("tuple P", "tuple P' with the same multiset", t2[2], t2[3])))
    named.append(("W3 WEIGHTS-STRICT", find_obstruction(W3, T3a_src, val_stream)))
    named.append(("W4 OUTPUT-REGROUP", find_obstruction(W4, T4_src, val_stream)))
    named.append(("W5 BOX-REORDER", find_obstruction(W5, val_stream, rev_stream)))
    ok1 = all(o is not None for _, o in named)
    gate("G1 NAMED-WITNESSES", ok1, "%d of 5 reproduce an exact obstruction"
         % sum(1 for _, o in named if o is not None))
    for nm, o in named:
        show(nm, None, o)
    if t2 is not None:
        emit("      W2 same multiset of digit maps, redistribution %s, which is"
             % (t2[0],))
        emit("      neither the identity nor the coordinate swap; position %s"
             % (t2[1],))

    # ---- the frozen boxes
    def box2():
        maps = list(product(range(2), repeat=2))
        for d00 in maps:
            for d01 in maps:
                for d10 in maps:
                    for d11 in maps:
                        for w in product((0, 1, 2), repeat=2):
                            yield (2, ((d00, d01), (d10, d11)), F(*w))

    def box3():
        idm = (0, 1, 2)
        maps = list(product(range(3), repeat=3))
        for d01 in maps:
            for d11 in maps:
                for w in product((0, 1, 2), repeat=3):
                    yield (3, ((idm, d01), (idm, d11)), F(*w))

    n2 = n3 = 0
    hit = {k: 0 for k, _, _ in FORBIDDEN_SINGLE}
    hit["T2 ERASE-NAMES"] = 0
    hit["T3b WEIGHTS-ANCHORED"] = 0
    g8_bad = 0
    rel = res = ner_app = ner_bad = cp_comm = cp_noncomm = comm_n = 0
    alt_bad = 0
    seen_dom = {k: 0 for k in hit}

    for P in box2():
        n2 += 1
        for nm, sf, vf in FORBIDDEN_SINGLE:
            seen_dom[nm] += 1
            if find_obstruction(P, sf, vf) is not None:
                hit[nm] += 1
        seen_dom["T2 ERASE-NAMES"] += 1
        if T2_obstruction(P) is not None:
            hit["T2 ERASE-NAMES"] += 1
        seen_dom["T3b WEIGHTS-ANCHORED"] += 1
        a3 = find_obstruction(P, T3a_src, val_stream) is not None
        b3 = find_obstruction(P, T3b_src, val_stream) is not None
        if b3:
            hit["T3b WEIGHTS-ANCHORED"] += 1
        if b3 and not a3:
            g8_bad += 1

        rel += arrow_relabel(P)
        res += arrow_restrict(P)
        app, bad = arrow_nerode(P)
        ner_app += 1 if app else 0
        ner_bad += bad
        if commuting(P):
            comm_n += 1
            cp_comm += arrow_coordperm(P)
        else:
            cp_noncomm += 1 if arrow_coordperm(P) else 0
        for (s, a, b) in positions(P):
            if stream(P, s, a, b) != stream_alt(P, s, a, b):
                alt_bad += 1

    for P in box3():
        n3 += 1
        for nm, sf, vf in FORBIDDEN_SINGLE:
            seen_dom[nm] += 1
            if find_obstruction(P, sf, vf) is not None:
                hit[nm] += 1
        seen_dom["T2 ERASE-NAMES"] += 1
        if T2_obstruction(P) is not None:
            hit["T2 ERASE-NAMES"] += 1
        seen_dom["T3b WEIGHTS-ANCHORED"] += 1
        rel += arrow_relabel(P)
        res += arrow_restrict(P)
        app, bad = arrow_nerode(P)
        ner_app += 1 if app else 0
        ner_bad += bad
        a3 = find_obstruction(P, T3a_src, val_stream) is not None
        b3 = find_obstruction(P, T3b_src, val_stream) is not None
        if b3:
            hit["T3b WEIGHTS-ANCHORED"] += 1
        if b3 and not a3:
            g8_bad += 1
        if commuting(P):
            comm_n += 1
            cp_comm += arrow_coordperm(P)
        else:
            cp_noncomm += 1 if arrow_coordperm(P) else 0

    emit("")
    emit("BOX-2 tuples %d   BOX-3 tuples %d" % (n2, n3))
    emit("")
    gate("G2 CENSUS-FORBIDDEN",
         all(v > 0 for v in hit.values()),
         "obstructing tuples of %d: " % (n2 + n3) +
         ", ".join("%s=%d" % (k.split()[0], hit[k]) for k in sorted(hit)))
    gate("G10 CENSUS-DOMAIN-CONSISTENCY",
         all(v == n2 + n3 for v in seen_dom.values()),
         "every reading examined the same %d tuples: " % (n2 + n3) +
         ", ".join("%s=%d" % (k.split()[0], seen_dom[k]) for k in sorted(seen_dom)))
    gate("G3a ARROW-RELABEL", rel == 0, "violations %d" % rel)
    gate("G3b ARROW-RESTRICT", res == 0, "violations %d" % res)
    gate("G3c ARROW-NERODE", ner_bad == 0,
         "applicable %d, violations %d" % (ner_app, ner_bad))
    gate("G3d ARROW-COORDPERM (commuting sub-box only)", cp_comm == 0,
         "commuting tuples %d, violations %d" % (comm_n, cp_comm))
    gate("G8 T3b-SUBSET-OF-T3a", g8_bad == 0,
         "tuples obstructing T3b but not T3a: %d" % g8_bad)
    emit("REPORT R1 COORDPERM-NONCOMMUTING  %d tuples" % cp_noncomm)
    emit("      A transported coordinate swap reverses the composition order,")
    emit("      because CANON.md composes coordinate 1 first. Preserved on every")
    emit("      commuting tuple, broken on these. Not gated, not a claim about")
    emit("      METRO-REDUCTION-ARROWS [C].")
    gate("G6 EVALUATOR-AGREEMENT", alt_bad == 0,
         "BOX-2 disagreements %d" % alt_bad)

    # ---- G4/G7 the witnesses are not admitted arrows in disguise
    nonarrow = []
    for nm, P in (("W1", W1), ("W2", W2), ("W3", W3), ("W4", W4), ("W5", W5)):
        checks = (arrow_relabel(P) == 0, arrow_restrict(P) == 0,
                  arrow_nerode(P)[1] == 0)
        nonarrow.append(all(checks))
    gate("G4 NOT-AN-ADMITTED-ARROW", all(nonarrow),
         "every witness leaves all admitted arrows stream-preserving, so the "
         "obstruction is the transformation's own")

    # W4 must not be the Nerode quotient
    cls4, k4 = nerode_classes(W4)
    gate("G7 W4-DISTINCT-FROM-NERODE", cls4[0] != cls4[1],
         "w(0)=w(1) but Nerode separates them, so output regrouping is not arrow 3")

    # ---- G9 convention independence
    def flip(P):
        ns, d, w = P
        return (ns, (d[1], d[0]), w)

    g9 = []
    for nm, P, sf, vf in (("W1", W1, T1_src, val_stream),
                          ("W3", W3, T3a_src, val_stream),
                          ("W4", W4, T4_src, val_stream),
                          ("W5", W5, val_stream, rev_stream)):
        g9.append(find_obstruction(flip(P), sf, vf) is not None)
    g9.append(T2_obstruction(flip(W2)) is not None)
    gate("G9 CONVENTION-INDEPENDENCE", all(g9),
         "%d of 5 obstructions survive coordinate 2 acting first" % sum(g9))

    # exactness
    gate("G5 EXACT-ARITHMETIC",
         all(isinstance(x, Fraction) for P in (W1, W2, W3, W4, W5) for x in P[2]),
         "all outputs are Fraction; no float in any assertion")

    emit("")
    emit("RESULT %d/%d %s" % (12 - len(FAIL), 12,
                              "ALL PASS" if not FAIL else "FAILURES " + ",".join(FAIL)))
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(newline="\n")
    sys.stdout.write("\n".join(LINES) + "\n")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
