#!/usr/bin/env python3
# TWIST-J kernel census witness. Exact integer arithmetic on Z_5^6, no
# floats, standard library only.
#
# The kernel: state space Z_5^6 with coordinates (p1, p4, p1p, p4p, q,
# t); five involutive generators a, b, c, d, e (definitions below);
# Thue-Morse drive t_n = popcount(n) mod 2; phase z5(x) = sum of the
# six coordinates mod 5; selection law i_n = (z5 + 2 t_n) mod 5 with
# (g_0, ..., g_4) = (a, b, c, d, e).
#
# The census: full enumeration of all 15625 seeds, warmup 400 ticks,
# collection window 300 ticks; the attractor signature is the set of
# states visited in the window. Two closure properties back the word
# attractor: every signature is closed under both one step transitions
# (drive bit 0 and drive bit 1), and the next independent 300 tick
# window reproduces the signature exactly.
#
# Claims verified: CENSUS-313, CENSUS-Z5-SHEET, CENSUS-PAIRING,
# CENSUS-HOSTING.

import sys

S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x):
    p1, p4, p1p, p4p, q, t = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-t) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, t = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + t * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + t * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + t * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + t * U_VEC[3]) % 5,
            (1 - q) % 5, (-t) % 5)


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


def table(f):
    return tuple(enc(f(s)) for s in STATES)


def compose(f, g):
    # (f o g)[i] = f[g[i]]
    return tuple(f[g[i]] for i in range(N))


CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def main():
    A, B, C, D, E = (table(g) for g in GENS)
    IDT = tuple(range(N))

    # 01 relations on all states
    ok = all(compose(T, T) == IDT for T in (A, B, C, D, E))
    BC = compose(C, B)  # bc(s) = gen_c(gen_b(s))
    BC5 = compose(BC, compose(BC, compose(BC, compose(BC, BC))))
    ok = ok and BC5 == IDT
    check("RELATIONS      a^2 = b^2 = c^2 = d^2 = e^2 = id; (bc)^5 = id", ok)

    # transition tables for the two drive bits
    F = [[0] * N, [0] * N]
    for t in (0, 1):
        gt = [GENS[(z + 2 * t) % 5] for z in range(5)]
        Ft = F[t]
        for i in range(N):
            Ft[i] = enc(gt[ZTAB[i]](STATES[i]))
    tm = [bin(n).count("1") & 1 for n in range(1000)]
    warm = [F[tm[n]] for n in range(400)]
    wind = [F[tm[n]] for n in range(400, 700)]
    wind2 = [F[tm[n]] for n in range(700, 1000)]

    # census with the independent second window
    sigs = {}
    basins = {}
    stable = True
    for seed in range(N):
        s = seed
        for T in warm:
            s = T[s]
        w1 = set()
        for T in wind:
            w1.add(s)
            s = T[s]
        sig = frozenset(w1)
        w2 = set()
        for T in wind2:
            w2.add(s)
            s = T[s]
        if frozenset(w2) != sig:
            stable = False
        if sig not in sigs:
            sigs[sig] = len(sigs)
        basins[sig] = basins.get(sig, 0) + 1

    atts = list(sigs)

    # 02 count
    check("COUNT-313      313 attractors", len(atts) == 313)

    # 03 sizes and disjoint support
    sizes = {}
    for sig in atts:
        sizes[len(sig)] = sizes.get(len(sig), 0) + 1
    support = set()
    total = 0
    for sig in atts:
        support |= sig
        total += len(sig)
    check("SIZES          312 of size 20, 1 of size 10; support 6250 disjoint",
          sizes == {20: 312, 10: 1} and total == 6250
          and len(support) == 6250)

    # 04 basins
    bh = {}
    for sig in atts:
        bh[basins[sig]] = bh.get(basins[sig], 0) + 1
    check("BASINS         312 basins of 50, 1 basin of 25; coverage 15625",
          bh == {50: 312, 25: 1} and sum(basins.values()) == N)

    # 05 the sum of two squares
    check("SUM-SQUARES    313 = 13^2 + 12^2", 313 == 13 ** 2 + 12 ** 2)

    # 06 the z5 sheet
    check("Z5-SHEET       every recurrent state has z5 in {1, 4}",
          all(ZTAB[i] in (1, 4) for i in support))

    # 07 the mirror algebra: only b, d, e fire on the sheet
    fired = set()
    for i in support:
        for t in (0, 1):
            fired.add((ZTAB[i] + 2 * t) % 5)
    check("MIRROR-ONLY    the selection law fires only b, d, e on the sheet",
          fired <= {1, 3, 4})

    # 08 the piston pairing Phi = (b4 d4 on pistons, identity fiber)
    def phi(x):
        p = gen_d(x)
        p = gen_b(p)
        return (p[0], p[1], p[2], p[3], x[4], x[5])

    PHI = table(phi)
    ok = compose(PHI, PHI) == IDT
    fixed = []
    moved = set()
    pairs = 0
    for sig in atts:
        img = frozenset(PHI[i] for i in sig)
        if img == sig:
            fixed.append(sig)
        else:
            ok = ok and (img in sigs)
            if sig not in moved:
                moved.add(sig)
                moved.add(img)
                pairs += 1
    fixed_sizes = {}
    for sig in fixed:
        fixed_sizes[len(sig)] = fixed_sizes.get(len(sig), 0) + 1
    ok = (ok and len(fixed) == 25 and pairs == 144
          and fixed_sizes == {20: 24, 10: 1}
          and pairs + len(fixed) == 169 == 13 ** 2)
    check("PAIRING        involution; 144 transpositions + 25 fixed"
          " (24 size 20 + singlet); classes 169 = 13^2", ok)

    # 09 the hosting formula
    BEB = compose(B, compose(E, B))
    group = {IDT}
    frontier = [IDT]
    while frontier:
        g = frontier.pop()
        for h in (D, BEB):
            ng = compose(h, g)
            if ng not in group:
                group.add(ng)
                frontier.append(ng)
    T0 = (0, 0, 0, 0, 3, 2)
    TT0 = tuple(enc(tuple((STATES[i][k] + T0[k]) % 5 for k in range(6)))
                for i in range(N))
    ok = len(group) == 10 and compose(D, BEB) == TT0
    hosted = 0
    for sig in atts:
        found = False
        for x in sorted(sig):
            orbit = {g[x] for g in group}
            orbit |= {B[y] for y in orbit}
            if orbit == sig:
                found = True
                break
        if found:
            hosted += 1
    ok = ok and hosted == 313
    check("HOSTING        |<d, b e b>| = 10; d(b e b) = T0 = (0,0,0,0,3,2);"
          " A = H1 x' union b H1 x' on 313 of 313", ok)

    # 10 closure under both one step transitions
    closed = all(all(F[0][i] in sig and F[1][i] in sig for i in sig)
                 for sig in atts)
    check("CLOSED-BOTH    every signature is closed under both transitions"
          " (drive bit 0 and drive bit 1)", closed)

    # 11 the next independent window reproduces every signature
    check("WINDOW-STABLE  the next independent 300 tick window reproduces"
          " every signature exactly", stable)

    print("TWIST-J kernel census witness (exact integer arithmetic on Z_5^6)")
    print("five involutions a, b, c, d, e; Thue-Morse drive; selection law")
    print("i = (z5 + 2 t) mod 5; full enumeration, warmup 400, window 300,")
    print("independent second window 300; closure under both transitions")
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
