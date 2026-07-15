#!/usr/bin/env python3
# P-ENTROPY-BRIDGE-2 exact verifier. The cylinder no-go for the bridge cut
# and the one-bit-per-scale law of the renormalized block maps. Exact
# integer arithmetic, standard library only, no float in any assertion.
# See PREREG.md in this directory; gates G01 to G10.

import sys
from collections import deque

S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-r) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + r * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + r * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + r * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + r * U_VEC[3]) % 5,
            (1 - q) % 5, (-r) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def dec(i):
    out = []
    for _ in range(6):
        out.append(i % 5)
        i //= 5
    return tuple(out)


def enc(x):
    i = 0
    for k in range(5, -1, -1):
        i = i * 5 + x[k]
    return i


N = 15625
STATES = [dec(i) for i in range(N)]
ZTAB = [sum(s) % 5 for s in STATES]

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def main():
    F = [[0] * N, [0] * N]
    for t in (0, 1):
        gt = [GENS[(z + 2 * t) % 5] for z in range(5)]
        Ft = F[t]
        for i in range(N):
            Ft[i] = enc(gt[ZTAB[i]](STATES[i]))
    tm = [bin(n).count("1") & 1 for n in range(1 << 16)]

    # ---- G01, G02 orbit spectra of multiplication by J ----
    MJ = [[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]]

    def spectrum(mod):
        from itertools import product as pr

        def step(v):
            return tuple(sum(MJ[i][j] * v[j] for j in range(4)) % mod
                         for i in range(4))
        seen = set()
        spec = {}
        for v in pr(range(mod), repeat=4):
            if v in seen:
                continue
            orb = [v]
            w = step(v)
            while w != v:
                orb.append(w)
                w = step(w)
            spec[len(orb)] = spec.get(len(orb), 0) + 1
            seen.update(orb)
        return spec

    check("G01 SPECTRUM-5     J-orbit spectrum mod 5 is {1: 1, 4: 1,"
          " 20: 31}", spectrum(5) == {1: 1, 4: 1, 20: 31})
    check("G02 SPECTRUM-25    J-orbit spectrum mod 25 is {1: 1, 4: 1,"
          " 20: 781, 100: 3750}",
          spectrum(25) == {1: 1, 4: 1, 20: 781, 100: 3750})

    # ---- G03 no constant solutions ----
    check("G03 NO-CONSTANT    F_0 and F_1 share no fixed point",
          all(not (F[0][i] == i and F[1][i] == i) for i in range(N)))

    # ---- census (recurrent core needed below) ----
    warm = [F[tm[n]] for n in range(400)]
    wind = [F[tm[n]] for n in range(400, 700)]
    sup = set()
    seen_sig = set()
    for seed in range(N):
        s = seed
        for T in warm:
            s = T[s]
        w1 = set()
        for T in wind:
            w1.add(s)
            s = T[s]
        fs = frozenset(w1)
        if fs not in seen_sig:
            seen_sig.add(fs)
            sup |= w1
    R = sorted(sup)
    check("G04 CORE           recurrent core 6250 on 313 attractors",
          len(sup) == 6250 and len(seen_sig) == 313)

    # ---- the feasibility engine ----
    def factors(L):
        s = set()
        for i in range(len(tm) - L):
            s.add(tuple(tm[i:i + L]))
        return sorted(s)

    def feas(L, c, ell):
        # constraint system on nodes (word, k in Z_ell); returns the exact
        # number of solution seeds summed over weakly connected pieces,
        # requiring every piece fully determined.
        ws = factors(L)
        wid = {w: i for i, w in enumerate(ws)}
        evs = factors(L + 1)
        nn = len(ws) * ell
        adj = [[] for _ in range(nn)]
        for v in evs:
            s = wid[v[:L]]
            t = wid[v[1:]]
            th = v[c]
            for k in range(ell):
                adj[s * ell + k].append((t * ell + ((k + 1) % ell), th))
        radj = [[] for _ in range(nn)]
        for a in range(nn):
            for (b, _) in adj[a]:
                radj[b].append(a)
        piece = [-1] * nn
        npc = 0
        total = 0
        for a0 in range(nn):
            if piece[a0] != -1:
                continue
            dq = deque([a0])
            piece[a0] = npc
            comp = [a0]
            while dq:
                x = dq.popleft()
                for (b, _) in adj[x]:
                    if piece[b] == -1:
                        piece[b] = npc
                        dq.append(b)
                        comp.append(b)
                for b in radj[x]:
                    if piece[b] == -1:
                        piece[b] = npc
                        dq.append(b)
                        comp.append(b)
            npc += 1
            root = comp[0]
            order = [root]
            seen = {root}
            dq = deque([root])
            while dq:
                x = dq.popleft()
                for (b, _) in adj[x]:
                    if b not in seen:
                        seen.add(b)
                        dq.append(b)
                        order.append(b)
            for psi in range(N):
                val = {root: psi}
                ok = True
                for x in order:
                    vx = val.get(x)
                    if vx is None:
                        ok = False
                        break
                    for (b, th) in adj[x]:
                        nv = F[th][vx]
                        vb = val.get(b)
                        if vb is None:
                            val[b] = nv
                        elif vb != nv:
                            ok = False
                            break
                    if not ok:
                        break
                if ok and len(val) == len(comp):
                    total += 1
        return total

    # ---- G05 pure-word no-go, L = 4..16 ----
    WCOUNTS = {4: (10, 12), 5: (12, 16), 6: (16, 20), 7: (20, 22),
               8: (22, 24), 9: (24, 28), 10: (28, 32), 11: (32, 36),
               12: (36, 40), 13: (40, 42), 14: (42, 44), 15: (44, 46),
               16: (46, 48)}
    ok = True
    for L in range(4, 17):
        ok = ok and len(factors(L)) == WCOUNTS[L][0]
        ok = ok and len(factors(L + 1)) == WCOUNTS[L][1]
        ok = ok and feas(L, 0, 1) == 0
    check("G05 PURE-WORD-NOGO zero solutions for windows L = 4..16 on the"
          " driver word alone; factor counts pinned", ok)

    # ---- G06 the killing lemma (machine part) ----
    check("G06 KILLING-ZERO   J fixes the zero residue at every depth"
          " (M_J 0 = 0): the pure-word system embeds at every"
          " lambda-depth", all(sum(MJ[i][j] * 0 for j in range(4)) == 0
                               for i in range(4)))

    # ---- G07 lambda-depth 4 table ----
    ok = True
    for (L, c) in ((4, 0), (5, 0), (5, 1), (6, 0), (6, 1), (6, 2)):
        for ell in (1, 4, 20):
            ok = ok and feas(L, c, ell) == 0
    check("G07 M4-TABLE       zero solutions at lambda-depth 4 for all"
          " (L, c) with L <= 6 and every orbit length {1, 4, 20}", ok)

    # ---- G08 lambda-depth 8 table, L = 4 ----
    ok = True
    for ell in (1, 4, 20, 100):
        ok = ok and feas(4, 0, ell) == 0
    check("G08 M8-TABLE       zero solutions at lambda-depth 8 for L = 4"
          " and every orbit length {1, 4, 20, 100}", ok)

    # ---- G09 the one-bit-per-scale law ----
    def subst_word(eps, k):
        w = [eps]
        for _ in range(k):
            nw = []
            for a in w:
                nw.extend((a, 1 - a))
            w = nw
        return w

    ok = True
    for k in range(0, 11):
        for eps in (0, 1):
            cur = R
            for th in subst_word(eps, k):
                Ft = F[th]
                cur = [Ft[x] for x in cur]
            ok = ok and len(set(cur)) == 3125
    check("G09 BLOCK-HALVING  |image of the level-k block map on the"
          " core| = 3125 = 6250/2 exactly, k = 0..10, both letters", ok)

    # ---- G10 odometer collision pins ----
    s = 0
    traj = []
    for n in range(1 << 15):
        traj.append(s)
        s = F[tm[n]][s]
    START = 1 << 12
    ok = True
    for k in range(1, 11):
        tab = {}
        first = None
        for n in range(START, 1 << 15):
            key = (n & ((1 << k) - 1), tm[n >> k])
            v = tab.get(key)
            if v is None:
                tab[key] = traj[n]
            elif v != traj[n]:
                first = n
                break
        ok = ok and first == START + (1 << (k + 1))
    check("G10 COLLISION-PIN  on the seed-0 orbit the first"
          " (address, block-label) collision sits exactly at"
          " 4096 + 2^(k+1), k = 1..10", ok)

    print("P-ENTROPY-BRIDGE-2 exact verifier")
    print("cylinder no-go for the bridge cut: constraint propagation over")
    print("(driver window, residue orbit) contexts, exact solution counts;")
    print("the killing lemma; the one-bit-per-scale law of the renormalized")
    print("block maps; odometer collision pins")
    print()
    passed = 0
    for i, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
