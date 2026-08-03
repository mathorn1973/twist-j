#!/usr/bin/env python3
"""Adversarial, from-scratch verifier for witness_6_3_6_6.json.

Written independently. Imports nothing from this directory.
Boundary convention derived ONLY from the public reference
reproduce/photon-electron/verify.py:

    partial f_(mu,nu)(x) = e_mu(x) + e_nu(x + e_mu)
                         - e_mu(x + e_nu) - e_nu(x)

with a face stored as (v, a, b), a < b, and an edge as (v, d):
the edge from v to v + e_d.

Default stance: REFUTED unless every check passes.
"""

import json
import sys
from collections import deque

PATH = "witness_6_3_6_6.json"

FAILURES = []
REPORT = []


def note(msg):
    REPORT.append(msg)
    print(msg)


def fail(msg):
    FAILURES.append(msg)
    print("REFUTE-CANDIDATE: " + msg)


def addv(v, d, s=1):
    w = list(v)
    w[d] += s
    return tuple(w)


def face_boundary(v, a, b):
    """From the reference convention, verbatim semantics:
    +e_a(v), +e_b(v+e_a), -e_a(v+e_b), -e_b(v)."""
    return (
        ((v, a), 1),
        ((addv(v, a), b), 1),
        ((addv(v, b), a), -1),
        ((v, b), -1),
    )


def main():
    with open(PATH, "r") as fh:
        data = json.load(fh)

    note("top-level keys: %s" % sorted(data.keys()))
    note("declared header: P=%s m=%s C=%s D=%s L=%s F=%s" % (
        data.get("P"), data.get("m"), data.get("C"),
        data.get("D"), data.get("L"), data.get("F")))

    raw_j = data["j"]
    raw_n = data["n"]
    note("raw list lengths: len(j)=%d len(n)=%d" % (len(raw_j), len(raw_n)))

    # ---------------- (1) j well-formed ----------------
    j = {}
    dup_j = 0
    bad_j = 0
    for item in raw_j:
        if (not isinstance(item, list)) or len(item) != 3:
            bad_j += 1
            continue
        vv, d, c = item
        if (not isinstance(vv, list)) or len(vv) != 4 \
                or not all(isinstance(x, int) for x in vv):
            bad_j += 1
            continue
        if d not in (0, 1, 2, 3):
            bad_j += 1
            continue
        if c not in (-1, 1):
            bad_j += 1
            continue
        key = (tuple(vv), d)
        if key in j:
            dup_j += 1
            continue
        j[key] = c
    if bad_j:
        fail("(1) %d malformed j entries (bad vertex/dir/coeff)" % bad_j)
    if dup_j:
        fail("(1) %d duplicated edges in j" % dup_j)
    if not j:
        fail("(1) j is empty / zero")
    note("(1) j: %d distinct edges, coeffs all in {-1,+1}: %s" % (
        len(j), all(c in (-1, 1) for c in j.values())))

    # ---------------- (2) partial j = 0 at every vertex ----------------
    # boundary of edge (v, d): +1 at v + e_d, -1 at v (standard 1-chain
    # boundary consistent with the face_boundary orientation above).
    vert = {}
    for (v, d), c in j.items():
        h = addv(v, d)
        vert[h] = vert.get(h, 0) + c
        vert[v] = vert.get(v, 0) - c
    nz_vert = {v: c for v, c in vert.items() if c != 0}
    if nz_vert:
        fail("(2) partial j nonzero at %d vertices, sample: %s" % (
            len(nz_vert), list(nz_vert.items())[:5]))
    else:
        note("(2) partial j = 0 at all %d touched vertices" % len(vert))

    # ---------------- (3) support graph connected, even degrees --------
    adj = {}
    deg = {}
    for (v, d) in j:
        h = addv(v, d)
        adj.setdefault(v, []).append(h)
        adj.setdefault(h, []).append(v)
        deg[v] = deg.get(v, 0) + 1
        deg[h] = deg.get(h, 0) + 1
    odd = [v for v, k in deg.items() if k % 2 != 0]
    if odd:
        fail("(3) %d vertices of odd degree, sample %s" % (
            len(odd), odd[:5]))
    else:
        degs = sorted(set(deg.values()))
        note("(3) all %d support vertices have even degree; "
             "degree values seen: %s" % (len(deg), degs))
    if adj:
        start = next(iter(adj))
        seen = {start}
        q = deque([start])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
        if len(seen) != len(adj):
            fail("(3) support graph disconnected: reached %d of %d "
                 "vertices" % (len(seen), len(adj)))
        else:
            note("(3) support graph connected: BFS reached all %d "
                 "vertices" % len(adj))
    else:
        fail("(3) empty support graph")

    # ---------------- (4) n well-formed ----------------
    n = {}
    dup_n = 0
    bad_n = 0
    for item in raw_n:
        if (not isinstance(item, list)) or len(item) != 4:
            bad_n += 1
            continue
        vv, a, b, c = item
        if (not isinstance(vv, list)) or len(vv) != 4 \
                or not all(isinstance(x, int) for x in vv):
            bad_n += 1
            continue
        if a not in (0, 1, 2, 3) or b not in (0, 1, 2, 3) or not a < b:
            bad_n += 1
            continue
        if c not in (-1, 1):
            bad_n += 1
            continue
        key = (tuple(vv), a, b)
        if key in n:
            dup_n += 1
            continue
        n[key] = c
    if bad_n:
        fail("(4) %d malformed n entries (bad vertex/dirs/coeff)" % bad_n)
    if dup_n:
        fail("(4) %d duplicated faces in n" % dup_n)
    note("(4) n: %d distinct faces, coeffs all in {-1,+1}: %s" % (
        len(n), all(c in (-1, 1) for c in n.values())))

    # ---------------- (5) partial n = 5 j on EVERY edge ----------------
    dn = {}
    for (v, a, b), c in n.items():
        for e, inc in face_boundary(v, a, b):
            dn[e] = dn.get(e, 0) + c * inc
    dn_nz = {e: c for e, c in dn.items() if c != 0}
    target = {e: 5 * c for e, c in j.items()}
    # Edges outside both supports are untouched by any face of n, so
    # they carry 0 on both sides automatically; comparing the nonzero
    # dictionaries is exactly the everywhere statement.
    extra = [e for e in dn_nz if e not in target]
    missing = [e for e in target if e not in dn_nz]
    wrong = [(e, dn_nz[e], target[e]) for e in dn_nz
             if e in target and dn_nz[e] != target[e]]
    if extra:
        fail("(5) partial n nonzero on %d edges outside supp j, "
             "sample %s" % (len(extra),
                            [(e, dn_nz[e]) for e in extra[:5]]))
    if missing:
        fail("(5) partial n = 0 on %d edges where 5j is nonzero, "
             "sample %s" % (len(missing), missing[:5]))
    if wrong:
        fail("(5) partial n != 5j on %d shared edges, sample %s"
             % (len(wrong), wrong[:5]))
    if not (extra or missing or wrong):
        vals = sorted(set(dn_nz.values()))
        note("(5) partial n = 5j on every edge of Z^4 "
             "(nonzero boundary support %d edges, values %s, "
             "all edges of Z^4 outside carry 0 = 5*0)"
             % (len(dn_nz), vals))

    # ---------------- (6) L and F ----------------
    L = len(j)
    F = len(n)
    if L != 3240:
        fail("(6) L = |supp j| = %d, claimed 3240" % L)
    if F != 7993:
        fail("(6) F = |supp n| = %d, claimed 7993" % F)
    if data.get("L") != L:
        fail("(6) header L=%s disagrees with computed %d"
             % (data.get("L"), L))
    if data.get("F") != F:
        fail("(6) header F=%s disagrees with computed %d"
             % (data.get("F"), F))
    note("(6) computed L = %d, F = %d" % (L, F))

    # ---------------- (7) 2^F <= 7^L exactly ----------------
    lhs = 2 ** F
    rhs = 7 ** L
    ok7 = lhs <= rhs
    if not ok7:
        fail("(7) 2^F > 7^L")
    B = rhs.bit_length() - 1          # max m with 2^m <= 7^L
    assert 2 ** B <= rhs < 2 ** (B + 1)
    note("(7) 2^F <= 7^L is %s; bit lengths: 2^F has %d bits, "
         "7^L has %d bits" % (ok7, lhs.bit_length(), rhs.bit_length()))
    note("(7) B = max m with 2^m <= 7^L = %d; F = %d; F <= B: %s; "
         "slack B - F = %d" % (B, F, F <= B, B - F))

    print()
    if FAILURES:
        print("VERDICT: REFUTED (%d failing checks)" % len(FAILURES))
        for m in FAILURES:
            print("  - " + m)
        return 1
    print("VERDICT: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
