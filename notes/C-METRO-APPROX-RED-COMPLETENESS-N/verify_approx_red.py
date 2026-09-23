#!/usr/bin/env python3
"""C-METRO-APPROX-RED-COMPLETENESS-N verifier. NON-CANONICAL incubation.

Obligation E of METRO-REDUCTION-CALCULUS. Standard library, exact.
Phi(P) = {F_x : x in S_reach(P)}, F_x(v) = w(delta_v x) over all V-tuples v.
E-INV (written proof): every admitted arrow of section 15 preserves Phi, so
approx_red implies equal Phi. This file checks:
  W-V   noncommuting pair with equal start V-futures and different Phi;
  W-S   rank-one pairs (MSD and LSD) with identical canonical streams and
        different Phi;
  CEN   q=2, a=2, |S|=2, A0={0}, binary w: every ~V pair of commuting tuples
        has isomorphic reach+Nerode normal forms (E-POS), and counts of
        Phi-splits among ~V pairs with a noncommuting member and among
        commuting stream-equivalent (MSD-E0) pairs.
"""
import itertools

FAIL = []


def compose(f, g):
    return tuple(f[g[x]] for x in range(len(g)))


def monoid(gens, m):
    idm = tuple(range(m))
    seen = {idm}
    frontier = [idm]
    while frontier:
        nxt = []
        for f in frontier:
            for g in gens:
                h = compose(g, f)
                if h not in seen:
                    seen.add(h)
                    nxt.append(h)
        frontier = nxt
    return seen


def vmaps(maps, m):
    """All delta_v = D_a(v_a) o ... o D_1(v_1)."""
    out = {tuple(range(m))}
    for mi in maps:
        Mi = monoid(mi, m)
        out = {compose(g, f) for f in out for g in Mi}
    return out


def future(maps, w, m, x, V=None):
    V = V if V is not None else vmaps(maps, m)
    return frozenset((f, w[f[x]]) for f in V)


def pair_futures_equal(P, x, Pp, xp):
    """F_x = F'_x' over all V-tuples, by the coordinate-ordered product closure."""
    (maps, w, m), (mapsp, wp, mp) = P, Pp
    pairs = {(x, xp)}
    for i in range(len(maps)):
        seen = set(pairs)
        frontier = list(pairs)
        while frontier:
            nxt = []
            for (a, b) in frontier:
                for u in range(len(maps[i])):
                    c = (maps[i][u][a], mapsp[i][u][b])
                    if c not in seen:
                        seen.add(c)
                        nxt.append(c)
            frontier = nxt
        pairs = seen
    return all(w[a] == wp[b] for a, b in pairs)


def s_reach(maps, A0, m):
    seen = set(A0)
    frontier = list(A0)
    while frontier:
        nxt = []
        for x in frontier:
            for mi in maps:
                for f in mi:
                    if f[x] not in seen:
                        seen.add(f[x])
                        nxt.append(f[x])
        frontier = nxt
    return seen


def phi_equal(P, A0, Pp, A0p):
    maps, w, m = P
    mapsp, wp, mp = Pp
    R, Rp = s_reach(maps, A0, m), s_reach(mapsp, A0p, mp)
    fw = all(any(pair_futures_equal(P, x, Pp, y) for y in Rp) for x in R)
    bw = all(any(pair_futures_equal(P, x, Pp, y) for x in R) for y in Rp)
    return fw and bw


def start_V_equal(P, A0, Pp, A0p):
    fw = all(any(pair_futures_equal(P, s, Pp, t) for t in A0p) for s in A0)
    bw = all(any(pair_futures_equal(P, s, Pp, t) for s in A0) for t in A0p)
    return fw and bw


def enc(n, q, conv):
    if n == 0:
        return [] if conv.endswith("E0") else [0]
    d = []
    while n:
        d.append(n % q)
        n //= q
    return d[::-1] if conv.startswith("MSD") else d


def stream(maps, w, s, n, conv):
    x = s
    for i, ni in enumerate(n):
        for u in enc(ni, 2, conv):
            x = maps[i][u][x]
    return w[x]


def streams_equal_exact(P, A0, Pp, A0p, conv):
    """Equal canonical start streams, decided exactly by a product automaton
    over canonical words (all n in N^a)."""
    (maps, w, m), (mapsp, wp, mp) = P, Pp

    def canon_pairs(pairs, i):
        out = set()
        for (a, b) in pairs:
            if conv.endswith("E0"):
                out.add((a, b))
            else:
                out.add((maps[i][0][a], mapsp[i][0][b]))
            if conv.startswith("MSD"):
                start = {(maps[i][u][a], mapsp[i][u][b]) for u in range(1, 2)}
                seen = set(start)
                fr = list(start)
                while fr:
                    nx = []
                    for (c, d) in fr:
                        for u in range(2):
                            e = (maps[i][u][c], mapsp[i][u][d])
                            if e not in seen:
                                seen.add(e)
                                nx.append(e)
                    fr = nx
                out |= seen
            else:
                start = {(maps[i][u][a], mapsp[i][u][b], u != 0) for u in range(2)}
                seen = set(start)
                fr = list(start)
                while fr:
                    nx = []
                    for (c, d, _) in fr:
                        for u in range(2):
                            e = (maps[i][u][c], mapsp[i][u][d], u != 0)
                            if e not in seen:
                                seen.add(e)
                                nx.append(e)
                    fr = nx
                out |= {(c, d) for (c, d, fl) in seen if fl}
        return out

    def eq(s, t):
        pairs = {(s, t)}
        for i in range(len(maps)):
            pairs = canon_pairs(pairs, i)
        return all(w[a] == wp[b] for a, b in pairs)

    fw = all(any(eq(s, t) for t in A0p) for s in A0)
    bw = all(any(eq(s, t) for s in A0) for t in A0p)
    return fw and bw


def commuting(maps):
    for i in range(len(maps)):
        for j in range(i + 1, len(maps)):
            for f in maps[i]:
                for g in maps[j]:
                    if compose(f, g) != compose(g, f):
                        return False
    return True


def normal_form(maps, w, A0, m):
    """reach + Nerode(V) quotient, canonicalized by futures (Pre_3 checked)."""
    R = sorted(s_reach(maps, A0, m))
    V = vmaps(maps, m)
    fut = {x: future(maps, w, m, x, V) for x in R}
    classes = sorted(set(fut.values()), key=lambda F: sorted(F))
    # Pre_3: congruence for every digit map
    for mi in maps:
        for f in mi:
            for x in R:
                for y in R:
                    if fut[x] == fut[y] and fut[f[x]] != fut[f[y]]:
                        return None
    return classes, fut


def main():
    print("C-METRO-APPROX-RED-COMPLETENESS-N verify (NON-CANONICAL, L5, exact)")
    # W-V
    s, t, z = 0, 1, 2
    d1 = (0, 2, 2)
    d2 = (1, 1, 2)
    maps = [[d1, d1], [d2, d2]]
    P = (maps, (0, 1, 0), 3)
    Pp = (maps, (0, 1, 1), 3)
    a = start_V_equal(P, [s], Pp, [s])
    b = phi_equal(P, [s], Pp, [s])
    c = commuting(maps)
    ok = a and not b and not c
    if not ok:
        FAIL.append("W-V")
    print(f"W-V noncommuting={not c} start V-futures equal={a} Phi equal={b}: {'PASS' if ok else 'FAIL'}")
    # W-S MSD and LSD rank one
    for label, d0, dd1, convs in (
        ("MSD", (1, 3, 2, 3), (2, 3, 2, 3), ("MSD-E0", "MSD-Z0")),
        ("LSD", (1, 3, 3, 3), (2, 2, 2, 2), ("LSD-E0", "LSD-Z0")),
    ):
        maps = [[d0, dd1]]
        P = (maps, (0, 0, 0, 0), 4)
        Pp = (maps, (0, 0, 0, 1), 4)
        res = []
        for conv in convs:
            se = streams_equal_exact(P, [0], Pp, [0], conv)
            brute = all(stream(maps, P[1], 0, [n], conv) == stream(maps, Pp[1], 0, [n], conv) for n in range(4096))
            res.append(se and brute)
        ph = phi_equal(P, [0], Pp, [0])
        ok = all(res) and not ph
        if not ok:
            FAIL.append("W-S " + label)
        print(f"W-S {label} streams equal (exact automaton and n<4096) under {convs}: {res}; Phi equal={ph}: {'PASS' if ok else 'FAIL'}")
    # census
    AM = list(itertools.product(range(2), repeat=2))
    tuples = []
    for d in itertools.product(AM, repeat=4):
        maps = [[d[0], d[1]], [d[2], d[3]]]
        for w in itertools.product((0, 1), repeat=2):
            tuples.append((maps, w))
    print(f"CEN tuples={len(tuples)}")
    nf = {}
    comm = {}
    for j, (maps, w) in enumerate(tuples):
        comm[j] = commuting(maps)
        if comm[j]:
            r = normal_form(maps, w, [0], 2)
            if r is None:
                FAIL.append(f"CEN Pre_3 failure on commuting {maps} {w}")
            nf[j] = r
    comm_pairs = comm_split = mixed_pairs = mixed_split = s_pairs = s_split = 0
    idx = list(range(len(tuples)))
    for i in idx:
        Pi = (tuples[i][0], tuples[i][1], 2)
        for j in idx:
            if j <= i:
                continue
            Pj = (tuples[j][0], tuples[j][1], 2)
            veq = start_V_equal(Pi, [0], Pj, [0])
            if veq:
                ph = phi_equal(Pi, [0], Pj, [0])
                if comm[i] and comm[j]:
                    comm_pairs += 1
                    if not ph:
                        comm_split += 1
                    # isomorphic normal forms: same start future and same Phi set
                    if nf[i] is not None and nf[j] is not None and not ph:
                        FAIL.append("E-POS split")
                else:
                    mixed_pairs += 1
                    mixed_split += (not ph)
            if comm[i] and comm[j] and streams_equal_exact(Pi, [0], Pj, [0], "MSD-E0"):
                s_pairs += 1
                s_split += not phi_equal(Pi, [0], Pj, [0])
    print(f"CEN ~V pairs both commuting={comm_pairs} Phi-splits={comm_split}")
    print(f"CEN ~V pairs with a noncommuting member={mixed_pairs} Phi-splits={mixed_split}")
    print(f"CEN stream-equal (MSD-E0) pairs both commuting={s_pairs} Phi-splits={s_split}")
    print(f"FAILURES {len(FAIL)}")
    for f in FAIL[:10]:
        print("  " + f)
    print("RESULT " + ("PASS" if not FAIL else "FIRED"))


if __name__ == "__main__":
    main()
