#!/usr/bin/env python3
"""C-METRO-COMMON-BLOCKING-N verifier. NON-CANONICAL incubation candidate.

Obligation D of METRO-REDUCTION-CALCULUS inside the declared encoding family
ENC4 = {MSD,LSD} x {E0,Z0}. Standard library only, integers and Fraction.
"""
import itertools
from fractions import Fraction

CONVS = ["MSD-E0", "MSD-Z0", "LSD-E0", "LSD-Z0"]
FAIL = []


def check(cond, label):
    if not cond:
        FAIL.append(label)
    return cond


def enc(n, q, conv):
    if n == 0:
        return [] if conv.endswith("E0") else [0]
    d = []
    while n:
        d.append(n % q)
        n //= q
    return d[::-1] if conv.startswith("MSD") else d


def dec(word, q, conv):
    ds = word if conv.startswith("MSD") else word[::-1]
    n = 0
    for u in ds:
        n = n * q + u
    return n


def word_k(U, q, k, conv):
    d = []
    for _ in range(k):
        d.append(U % q)
        U //= q
    return d[::-1] if conv.startswith("MSD") else d


def compose(f, g):
    """(f o g)(x) = f(g(x)) for map tuples."""
    return tuple(f[g[x]] for x in range(len(g)))


def ident(m):
    return tuple(range(m))


def word_map(maps_i, word, m):
    out = ident(m)
    for u in word:
        out = compose(maps_i[u], out)
    return out


def blocked_maps(maps_i, q, k, conv, m):
    return [word_map(maps_i, word_k(U, q, k, conv), m) for U in range(q ** k)]


def run_state(maps, q, conv, s, n, m):
    x = s
    for i, ni in enumerate(n):
        x = word_map(maps[i], enc(ni, q, conv), m)[x]
    return x


def coord_table(maps_i, q, conv, N, m):
    """Map tuple D_i(enc(n)) for n < N, by the prefix recursion."""
    T = [None] * N
    for n in range(N):
        T[n] = word_map(maps_i, enc(n, q, conv), m) if n < q else None
    for n in range(q, N):
        if conv.startswith("MSD"):
            T[n] = compose(maps_i[n % q], T[n // q])
        else:
            T[n] = compose(T[n // q], maps_i[n % q])
    return T


# ---------------------------------------------------------------- L0
def lemma_L0():
    ok = True
    for q in (2, 3):
        for k in (2, 3, 4):
            for conv in CONVS:
                for n in range(2 ** 10):
                    e = enc(n, q, conv)
                    flat = []
                    for U in enc(n, q ** k, conv):
                        flat += word_k(U, q, k, conv)
                    rho = (-len(e)) % k
                    want = [0] * rho + e if conv.startswith("MSD") else e + [0] * rho
                    if flat != want:
                        ok = False
    check(ok, "F3 L0")
    print(f"L0 flattening q in (2,3), k in (2,3,4), four conventions, n < 1024: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- automaton
def pairs_step(pairs, maps_i, q, k, conv, m):
    """All (D_i(pad(v))x, D_i(v)y) over canonical v, with one witness word each."""
    z = maps_i[0]
    out = {}
    for (x, y), wit in pairs.items():
        cand = []
        if conv.startswith("MSD"):
            for rho in range(k):
                x0 = x
                for _ in range(rho):
                    x0 = z[x0]
                if conv.endswith("E0") and rho == 0:
                    cand.append(((x0, y), []))
                if conv.endswith("Z0") and (rho + 1) % k == 0:
                    cand.append(((z[x0], z[y]), [0]))
                # nonempty canonical: first letter nonzero, then anything
                seen = {}
                frontier = []
                for u in range(1, q):
                    st = (maps_i[u][x0], maps_i[u][y], 1 % k)
                    if st not in seen:
                        seen[st] = [u]
                        frontier.append(st)
                while frontier:
                    nxt = []
                    for st in frontier:
                        for u in range(q):
                            s2 = (maps_i[u][st[0]], maps_i[u][st[1]], (st[2] + 1) % k)
                            if s2 not in seen:
                                seen[s2] = seen[st] + [u]
                                nxt.append(s2)
                    frontier = nxt
                for st, wd in seen.items():
                    if (rho + st[2]) % k == 0:
                        cand.append(((st[0], st[1]), wd))
        else:
            if conv.endswith("E0"):
                cand.append(((x, y), []))
            else:
                xk = x
                for _ in range(k):
                    xk = z[xk]
                cand.append(((xk, z[y]), [0]))
            seen = {}
            frontier = []
            for u in range(q):
                st = (maps_i[u][x], maps_i[u][y], 1 % k, u != 0)
                if st not in seen:
                    seen[st] = [u]
                    frontier.append(st)
            while frontier:
                nxt = []
                for st in frontier:
                    for u in range(q):
                        s2 = (maps_i[u][st[0]], maps_i[u][st[1]], (st[2] + 1) % k, u != 0)
                        if s2 not in seen:
                            seen[s2] = seen[st] + [u]
                            nxt.append(s2)
                frontier = nxt
            for st, wd in seen.items():
                if st[3]:
                    rho = (-st[2]) % k
                    x2 = st[0]
                    for _ in range(rho):
                        x2 = z[x2]
                    cand.append(((x2, st[1]), wd))
        for pr, wd in cand:
            if pr not in out:
                out[pr] = wit + [wd]
    return out


def pre_blk(maps, A0, w, q, k, conv, m):
    pairs = {(s, s): [s] for s in A0}
    for i in range(len(maps)):
        pairs = pairs_step(pairs, maps[i], q, k, conv, m)
    bad = [(pr, wit) for pr, wit in pairs.items() if w[pr[0]] != w[pr[1]]]
    return len(bad) == 0, bad, pairs


def realize(bad, maps, q, k, conv, m, w):
    """F1(b): every failing automaton pair must be realized by an explicit n."""
    bmaps = [blocked_maps(maps[i], q, k, conv, m) for i in range(len(maps))]
    for pr, wit in bad:
        s = wit[0]
        n = [dec(v, q, conv) for v in wit[1:]]
        if enc(n[0], q, conv) != wit[1] and not (wit[1] == [] and n[0] == 0):
            return False
        xs = run_state(maps, q, conv, s, n, m)
        xb = run_state(bmaps, q ** k, conv, s, n, m)
        if (xb, xs) != pr or w[xb] == w[xs]:
            return False
    return True


def brute(maps, A0, w, q, k, conv, m, HB):
    """Stream comparison below the horizon with the explicit blocked tuple."""
    N = q ** HB
    a = len(maps)
    TP = [coord_table(maps[i], q, conv, N, m) for i in range(a)]
    bm = [blocked_maps(maps[i], q, k, conv, m) for i in range(a)]
    TB = [coord_table(bm[i], q ** k, conv, N, m) for i in range(a)]
    for n in itertools.product(range(N), repeat=a):
        fp = ident(m)
        fb = ident(m)
        for i in range(a):
            fp = compose(TP[i][n[i]], fp)
            fb = compose(TB[i][n[i]], fb)
        for s in A0:
            if w[fp[s]] != w[fb[s]]:
                return False
    return True


# ---------------------------------------------------------------- Blk#
def blk_sharp(maps, q, k, conv, m):
    """Explicit augmented blocked tuple (MSD) on carrier S x {0,1}^a."""
    a = len(maps)
    states = [(x, f) for x in range(m) for f in itertools.product((0, 1), repeat=a)]
    idx = {st: j for j, st in enumerate(states)}
    out = []
    for i in range(a):
        mi = []
        for U in range(q ** k):
            full = word_map(maps[i], word_k(U, q, k, conv), m)
            if U != 0:
                wk = word_k(U, q, k, conv)
                j = 0
                while wk[j] == 0:
                    j += 1
                strip = word_map(maps[i], wk[j:], m)
            else:
                strip = maps[i][0] if conv.endswith("Z0") else ident(m)
            tbl = []
            for (x, f) in states:
                if f[i] == 1:
                    tbl.append(idx[(full[x], f)])
                else:
                    f2 = f[:i] + (1,) + f[i + 1:]
                    tbl.append(idx[(strip[x], f2)])
            mi.append(tuple(tbl))
        out.append(mi)
    return states, idx, out


def check_blk_sharp(maps, A0, w, q, k, conv, m, HB):
    states, idx, smaps = blk_sharp(maps, q, k, conv, m)
    a = len(maps)
    M = len(states)
    N = q ** HB
    for s in A0:
        for n in itertools.product(range(N), repeat=a):
            xs = run_state(maps, q, conv, s, list(n), m)
            xb = run_state(smaps, q ** k, conv, idx[(s, (0,) * a)], list(n), M)
            fn = tuple(0 if enc(n[i], q, conv) == [] else 1 for i in range(a))
            if states[xb] != (xs, fn) or w[states[xb][0]] != w[xs]:
                return False, smaps
    return True, smaps


def commuting(maps):
    a = len(maps)
    for i in range(a):
        for j in range(i + 1, a):
            for f in maps[i]:
                for g in maps[j]:
                    if compose(f, g) != compose(g, f):
                        return False
    return True


# ---------------------------------------------------------------- witnesses
def witnesses():
    swap, idm = (1, 0), (0, 1)
    # W-D1
    maps = [[swap, idm]]
    w = (0, 1)
    sp = w[run_state(maps, 2, "MSD-E0", 0, [1], 2)]
    bm = [blocked_maps(maps[0], 2, 2, "MSD-E0", 2)]
    sb = w[run_state(bm, 4, "MSD-E0", 0, [1], 2)]
    check(sp == 0 and sb == 1, "F4 W-D1")
    print(f"W-D1 Stream_P(0,1)={sp} Stream_Blk2(0,1)={sb}: {'PASS' if (sp, sb) == (0, 1) else 'FAIL'}")
    # W-D2
    maps = [[swap, swap], [idm, idm]]
    W5 = {0: (1, 0), 1: (0, 1)}
    check(commuting(maps), "F4 W-D2 commuting")
    bm = [blocked_maps(maps[i], 2, 2, "MSD-E0", 2) for i in range(2)]
    check(commuting(bm), "F5 W-D2 blocked commuting")
    ok = True
    lines = []
    for mexp in range(2, 9):
        N = 2 ** mexp
        tot_p = [0, 0]
        tot_b = [0, 0]
        for n1 in range(N, 2 * N):
            for n2 in range(0, N):
                xp = run_state(maps, 2, "MSD-E0", 0, [n1, n2], 2)
                xb = run_state(bm, 4, "MSD-E0", 0, [n1, n2], 2)
                tot_p = [tot_p[c] + W5[xp][c] for c in range(2)]
                tot_b = [tot_b[c] + W5[xb][c] for c in range(2)]
        sp = sum(tot_p)
        sb = sum(tot_b)
        norm_p = tuple(Fraction(t, sp) for t in tot_p)
        norm_b = tuple(Fraction(t, sb) for t in tot_b)
        want_p = (Fraction(1), Fraction(0)) if mexp % 2 == 1 else (Fraction(0), Fraction(1))
        if norm_p != want_p or norm_b != (Fraction(1), Fraction(0)):
            ok = False
        lines.append(f"  m={mexp} box R((2^m,0),(2^m,2^m)) P:{tuple(str(v) for v in norm_p)} Blk2:{tuple(str(v) for v in norm_b)}")
    check(ok, "F4 W-D2")
    print("W-D2 normalized translated-box averages:")
    for ln in lines:
        print(ln)
    print(f"W-D2 decision P: INADMISSIBLE (alternating limits); Blk2: ADMISSIBLE(PROBABILITY(1,0)): {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- census
def all_maps(m):
    return list(itertools.product(range(m), repeat=m))


def census_B1():
    m, q, HB = 3, 2, 7
    A0 = [0, 1, 2]
    AM = all_maps(m)
    counts = {}
    for conv in CONVS:
        for k in (2, 3):
            c_true = 0
            for d0 in AM:
                for d1 in AM:
                    maps = [[d0, d1]]
                    for w in itertools.product((0, 1), repeat=m):
                        ok, bad, _ = pre_blk(maps, A0, w, q, k, conv, m)
                        br = brute(maps, A0, w, q, k, conv, m, HB)
                        if ok and not br:
                            check(False, f"F1a B1 {conv} k={k} {maps} {w}")
                        if not ok and not realize(bad, maps, q, k, conv, m, w):
                            check(False, f"F1b B1 {conv} k={k} {maps} {w}")
                        if ok:
                            c_true += 1
                        if conv.startswith("MSD") and k == 2:
                            good, _ = check_blk_sharp(maps, A0, w, q, k, conv, m, 5)
                            check(good, f"F2 B1 {conv} {maps} {w}")
            counts[(conv, k)] = c_true
    return counts


def census_B2():
    m, q, HB = 2, 2, 5
    A0 = [0]
    AM = all_maps(m)
    counts = {}
    for conv in CONVS:
        for k in (2, 3):
            c_true = c_comm = c_comm_true = 0
            for d in itertools.product(AM, repeat=4):
                maps = [[d[0], d[1]], [d[2], d[3]]]
                com = commuting(maps)
                if com:
                    bm = [blocked_maps(maps[i], q, k, conv, m) for i in range(2)]
                    check(commuting(bm), f"F5 B2 Blk {conv} k={k} {maps}")
                    if conv.startswith("MSD"):
                        _, _, smaps = blk_sharp(maps, q, k, conv, m)
                        check(commuting(smaps), f"F5 B2 Blk# {conv} k={k} {maps}")
                for w in itertools.product((0, 1), repeat=m):
                    ok, bad, _ = pre_blk(maps, A0, w, q, k, conv, m)
                    br = brute(maps, A0, w, q, k, conv, m, HB)
                    if ok and not br:
                        check(False, f"F1a B2 {conv} k={k} {maps} {w}")
                    if not ok and not realize(bad, maps, q, k, conv, m, w):
                        check(False, f"F1b B2 {conv} k={k} {maps} {w}")
                    if conv.startswith("MSD") and k == 2:
                        good, _ = check_blk_sharp(maps, A0, w, q, k, conv, m, 4)
                        check(good, f"F2 B2 {conv} {maps} {w}")
                    c_true += ok
                    c_comm += com
                    c_comm_true += ok and com
            counts[(conv, k)] = (c_true, c_comm, c_comm_true)
    return counts


def main():
    print("C-METRO-COMMON-BLOCKING-N verify (NON-CANONICAL, L5, stdlib exact)")
    lemma_L0()
    witnesses()
    c1 = census_B1()
    for (conv, k), v in sorted(c1.items()):
        print(f"B1 q=2 a=1 |S|=3 A0=S tuples=5832 {conv} k={k} Pre_blk_true={v}")
    c2 = census_B2()
    for (conv, k), v in sorted(c2.items()):
        print(f"B2 q=2 a=2 |S|=2 A0={{0}} tuples=1024 {conv} k={k} Pre_blk_true={v[0]} commuting={v[1]} commuting_and_Pre_blk={v[2]}")
    print(f"FAILURES {len(FAIL)}")
    for f in FAIL[:20]:
        print("  " + f)
    print("RESULT " + ("PASS" if not FAIL else "FIRED"))


if __name__ == "__main__":
    main()
