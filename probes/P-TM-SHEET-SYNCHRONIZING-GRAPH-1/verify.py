#!/usr/bin/env python3
"""P-TM-SHEET-SYNCHRONIZING-GRAPH-1 exact verifier.

Exact L1 probe for the candidate claim TM-SHEET-SYNCHRONIZING-GRAPH. The
verifier derives the sheet pair T0, T1 from the declared generators, proves
the reset-word theorem by finite graph plus brute force, rebuilds the exact
Thue-Morse language of length at most 16 from mu^4 blocks, and checks the
eight frozen clauses of PREREG.md. Standard library only, exact integer
arithmetic, no float, reads no files. Exit 0 pass, 1 STOP, 2 FALSIFIED.
"""

import os
import sys
from collections import deque
from itertools import product

BASE_COMMIT = "cef0a08cec219a41333b36fbfe0a0e4dc780045f"
PREREG_SHA256 = "a66dbc167a90e89b315122137035076386751a857e06f194e5b6ab6388d41ce3"
REQUIRED_ENVIRONMENT = (
    ("LC_ALL", "C"),
    ("LANG", "C"),
    ("PYTHONDONTWRITEBYTECODE", "1"),
    ("PYTHONHASHSEED", "0"),
    ("TZ", "UTC"),
)

MOD = 5
S_C = (2, 1, 2, 1)
U_C = (0, 1, 0, 4)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)
CE = tuple((C_D[i] + V_E[i]) % MOD for i in range(6))
WSTAR = "10100101"


class Falsified(Exception):
    pass


class Stop(Exception):
    pass


LINES = []


def emit(line):
    LINES.append(line)


def gate(name, condition, detail):
    if not condition:
        raise Falsified(name + " " + detail)
    emit(name + " " + detail + ": PASS")


def g_a(s):
    return (s[1], s[0], s[3], s[2], s[4], s[5])


def g_b(s):
    return ((-s[2]) % MOD, (-s[3]) % MOD, (-s[0]) % MOD, (-s[1]) % MOD,
            (-s[4]) % MOD, (-s[5]) % MOD)


def g_c(s):
    b4p = ((-s[2]) % MOD, (-s[3]) % MOD, (-s[0]) % MOD, (-s[1]) % MOD)
    r = s[5]
    piston = tuple((b4p[i] + S_C[i] + r * U_C[i]) % MOD for i in range(4))
    return piston + ((1 - s[4]) % MOD, (-r) % MOD)


def g_d(s):
    return tuple((C_D[i] - s[i]) % MOD for i in range(6))


def g_e(s):
    return tuple((CE[i] - s[i]) % MOD for i in range(6))


GENS = (g_a, g_b, g_c, g_d, g_e)


def z6(s):
    return sum(s) % MOD


def theta(n):
    return bin(n).count("1") & 1


def audit():
    emit("P-TM-SHEET-SYNCHRONIZING-GRAPH-1 exact verifier")
    emit("authority base=" + BASE_COMMIT)
    emit("prereg sha256=" + PREREG_SHA256)

    if len(sys.argv) != 1:
        raise Stop("E-ARGUMENTS")
    for key, value in REQUIRED_ENVIRONMENT:
        if os.environ.get(key) != value:
            raise Stop("E-ENVIRONMENT-" + key)
    if "@" in BASE_COMMIT or "@" in PREREG_SHA256:
        raise Stop("E-UNPINNED")
    emit("I01 RUNTIME arguments=0 environment=5: PASS")

    states = [tuple(t) for t in product(range(5), repeat=6)]
    sheet_sizes = [0] * 5
    for s in states:
        sheet_sizes[z6(s)] += 1
    gate("C01 CARRIER",
         len(states) == 15625 and sheet_sizes == [3125] * 5,
         "states=15625 sheets=5 sheet_size=3125")

    ok = True
    for g in GENS:
        for s in states:
            if g(g(s)) != s:
                ok = False
    for s in states:
        x = s
        for _ in range(5):
            x = g_b(g_c(x))
        if x != s:
            ok = False
    for s in states:
        z = z6(s)
        if z6(g_a(s)) != z:
            ok = False
        if z6(g_b(s)) != (-z) % MOD:
            ok = False
        if z6(g_c(s)) != (2 - z) % MOD:
            ok = False
        if z6(g_d(s)) != (2 - z) % MOD:
            ok = False
        if z6(g_e(s)) != (3 - z) % MOD:
            ok = False
    gate("C02 GENERATORS", ok, "involutions=5 bc5=id sheet_laws=5")

    maps = {}
    ok = True
    for th in (0, 1):
        T = [None] * 5
        for s in states:
            z = z6(s)
            zn = z6(GENS[(z + 2 * th) % MOD](s))
            if T[z] is None:
                T[z] = zn
            elif T[z] != zn:
                ok = False
        maps[th] = tuple(T)
    T0, T1 = maps[0], maps[1]
    gate("C03 SHEET-TABLE",
         ok and T0 == (0, 4, 0, 4, 4) and T1 == (2, 1, 1, 3, 1),
         "t0=04044 t1=21131")

    IDM = (0, 1, 2, 3, 4)

    def compose(word):
        m = IDM
        for ch in word:
            T = T0 if ch == "0" else T1
            m = tuple(T[x] for x in m)
        return m

    def image(word):
        return frozenset(compose(word))

    def step(sub, ch):
        T = T0 if ch == "0" else T1
        return frozenset(T[z] for z in sub)

    reach_maps = {IDM}
    dq = deque([IDM])
    while dq:
        m = dq.popleft()
        for ch in "01":
            T = T0 if ch == "0" else T1
            nm = tuple(T[x] for x in m)
            if nm not in reach_maps:
                reach_maps.add(nm)
                dq.append(nm)
    sup = {}
    for m in reach_maps:
        sup.setdefault(frozenset(m), set()).add(m)
    multi = {tuple(sorted(k)): v for k, v in sup.items() if len(v) > 1}
    ok = (len(reach_maps) == 9 and len(reach_maps - {IDM}) == 8
          and len(sup) == 7
          and set(multi) == {(0, 4), (1, 2)}
          and multi[(0, 4)] == {(0, 4, 0, 4, 4), (0, 4, 4, 4, 4)}
          and multi[(1, 2)] == {(2, 1, 2, 1, 1), (2, 1, 1, 1, 1)})
    for k, v in sup.items():
        for ch in "01":
            T = T0 if ch == "0" else T1
            succ = {frozenset(tuple(T[x] for x in m)) for m in v}
            if len(succ) != 1:
                ok = False
    gate("A01 TRANSFORMATION-AUTOMATON", ok,
         "states=9 maps=8 supports=7 identifications=2")

    ok = all(len(image(a + b)) > 1 for a in "01" for b in "01")
    sync3 = sorted("".join(w) for w in product("01", repeat=3)
                   if len(image("".join(w))) == 1)
    gate("A02 MINIMAL-RESET",
         ok and sync3 == ["011", "110"] and image("11") == frozenset({1, 3}),
         "len2_sync=0 len3_sync=011,110 R11=13")

    FULL = frozenset(range(5))
    reach7 = {FULL}
    dq = deque([FULL])
    while dq:
        s = dq.popleft()
        for ch in "01":
            ns = step(s, ch)
            if ns not in reach7:
                reach7.add(ns)
                dq.append(ns)
    ok = len(reach7) == 7
    for S in reach7:
        for pat in ("011", "110"):
            s = S
            for ch in pat:
                s = step(s, ch)
            if len(s) != 1:
                ok = False
    start = (FULL, "")
    seen = {start}
    dq = deque([start])
    while dq:
        sub, mem = dq.popleft()
        for ch in "01":
            if (mem == "01" and ch == "1") or (mem == "11" and ch == "0"):
                continue
            ns = step(sub, ch)
            if len(ns) < 2:
                ok = False
                continue
            node = (ns, (mem + ch)[-2:])
            if node not in seen:
                seen.add(node)
                dq.append(node)
    brute = 0
    for k in range(1, 15):
        for w in product("01", repeat=k):
            ww = "".join(w)
            if (len(image(ww)) == 1) != (("011" in ww) or ("110" in ww)):
                ok = False
            brute += 1
    gate("A03 RESET-THEOREM",
         ok and len(seen) == 7 and brute == 32766,
         "directionA=14 productgraph_nodes=7 brute_words=32766")

    N = 1 << 16
    t = "".join(str(theta(n)) for n in range(N))
    pairs = {t[i:i + 2] for i in range(N - 1)}
    gate("L01 TM-PAIRS", pairs == {"00", "01", "10", "11"},
         "pairs=00,01,10,11")

    def mu(w):
        return "".join("01" if c == "0" else "10" for c in w)

    blocks = []
    for ab in sorted(pairs):
        w = ab
        for _ in range(4):
            w = mu(w)
        blocks.append(w)
    ok = all(len(w) == 32 for w in blocks)
    exactF = {}
    for k in range(1, 17):
        fk = set()
        for w in blocks:
            for i in range(0, 32 - k + 1):
                fk.add(w[i:i + k])
        exactF[k] = fk
    prefixF = {k: {t[i:i + k] for i in range(N - k + 1)}
               for k in range(1, 17)}
    for k in range(1, 13):
        if exactF[k] != prefixF[k]:
            ok = False
    for k in range(13, 17):
        if not prefixF[k] <= exactF[k]:
            ok = False
    counts = tuple(len(exactF[k]) for k in range(1, 17))
    frozen_counts = (2, 4, 6, 10, 12, 16, 20, 22, 24, 28,
                     32, 36, 40, 42, 44, 46)
    gate("L02 MU4-LANGUAGE",
         ok and counts == frozen_counts,
         "counts=" + ",".join(map(str, counts))
         + " prefix_equal=1..12 prefix_subset=13..16")

    nonsync = {}
    for k in range(1, 13):
        nonsync[k] = sorted(w for w in exactF[k] if len(image(w)) > 1)
    table = tuple(len(nonsync[k]) for k in range(1, 13))
    ok = table == (2, 4, 4, 5, 4, 3, 2, 1, 0, 0, 0, 0)
    for k in range(3, 17):
        for w in exactF[k]:
            if ("11" not in w) != (len(image(w)) > 1):
                ok = False
    gate("L03 NONSYNC-TABLE", ok,
         "table=" + ",".join(map(str, table)) + " no11_iff_nonsync=3..16")

    ok = (nonsync[8] == [WSTAR]
          and WSTAR == WSTAR[::-1]
          and sorted(w for w in exactF[8] if "11" not in w) == [WSTAR])
    for k in range(9, 17):
        if any("11" not in w for w in exactF[k]):
            ok = False
    rs8 = sorted(w for w in exactF[8]
                 if (w + "0" in exactF[9]) and (w + "1" in exactF[9]))
    ls8 = sorted(w for w in exactF[8]
                 if ("0" + w in exactF[9]) and ("1" + w in exactF[9]))
    ok = (ok and rs8 == ["01101001", "10010110"]
          and ls8 == ["01101001", "10010110"]
          and [c for c in "01" if WSTAR + c in exactF[9]] == ["1"]
          and [c for c in "01" if c + WSTAR in exactF[9]] == ["1"]
          and "1" + WSTAR + "1" in exactF[10])
    gate("W01 WSTAR", ok,
         "w=10100101 palindrome=1 unique_11free_8=1 flanks=1,1"
         + " sandwich=1101001011")

    T01 = compose("01")
    TW = compose(WSTAR)
    pre01 = compose("0")
    prew = compose("1010010")
    ok = (T01 == (2, 1, 2, 1, 1) and TW == (2, 1, 1, 1, 1)
          and sorted(z for z in range(5) if T01[z] == 2) == [0, 2]
          and sorted(z for z in range(5) if TW[z] == 2) == [0]
          and frozenset(T01) == frozenset(TW) == frozenset({1, 2})
          and pre01 == (0, 4, 0, 4, 4) and prew == (0, 4, 4, 4, 4)
          and frozenset(pre01) == frozenset(prew) == frozenset({0, 4})
          and T01 != TW)
    gate("W02 LEAF-TRANSFORM", ok,
         "T01=21211 TW=21111 pre01=04044 preW=04444")

    eps = {1: 0, 4: 0, 2: 1, 3: 1}
    ok = all(eps[TW[z]] == (1 if z == 0 else 0) for z in range(5))
    ok = ok and eps[1] == 0 and eps[4] == 0
    gate("W03 EPS-CUT", ok, "epsrow=10000 postsync_eps=0")

    ok = True
    for a in (0, 1):
        for b in (0, 1):
            T = T0 if b == 0 else T1
            if T[(4 + 2 * a) % 5] != (4 + 2 * b) % 5:
                ok = False
    nine = 0
    for u in sorted(exactF[9]):
        m = compose(u)
        if len(set(m)) != 1 or m[0] != (4 + 2 * int(u[-1])) % 5:
            ok = False
        nine += 1
    sizes = [5]
    s = FULL
    for ch in "011":
        s = step(s, ch)
        sizes.append(len(s))
    gate("G01 INVARIANT-GRAPH",
         ok and nine == 24 and sizes == [5, 2, 2, 1]
         and len(image(WSTAR)) == 2,
         "letter_pairs=4 nine_constancy=24 canonical_011=3 sharp8=2")

    ok = all((4 + 2 * th) % 5 == (-pow(-1, th, 5)) % 5 for th in (0, 1))
    for n in range(2048):
        if (4 + 2 * theta(n)) % 5 != (-pow(-1, theta(n), 5)) % 5:
            ok = False
    gate("G02 SIGN-LAW", ok, "checked_n=2048")

    emit("RESULT PASS")


def main():
    try:
        audit()
        payload = "\n".join(LINES) + "\n"
        sys.stdout.buffer.write(payload.encode("ascii"))
        return 0
    except Falsified as error:
        payload = "\n".join(LINES + ["FALSIFIED " + str(error)]) + "\n"
        sys.stdout.buffer.write(payload.encode("ascii"))
        return 2
    except Stop as error:
        sys.stdout.buffer.write(("STOP " + str(error) + "\n").encode("ascii"))
        return 1
    except BaseException as error:
        sys.stdout.buffer.write(
            ("STOP E-EXCEPTION-" + type(error).__name__.upper() + "\n")
            .encode("ascii"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
