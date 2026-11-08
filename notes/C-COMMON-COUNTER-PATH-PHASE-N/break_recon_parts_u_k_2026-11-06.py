#!/usr/bin/env python3
"""Breaker for RECON-PATH-PHASE-ONE-CARRIER. NON-CANONICAL, L1, exact.

Independent code paths that try to produce counterexamples:
 B-U  native U by composition of affine maps (no state enumeration), to n=4096;
 B-K  account exactness with a different digit algorithm and a second potential,
      on a fresh sample and on every admitted edge of the complete I_1 orbit;
 B-L  loop-area divisibility and count holonomy on random banks;
 (Section B-D of the session breaker is omitted from this public extract; see PROVENANCE.md.)
Standard library only, integers and Fractions only.
"""
from collections import deque
from fractions import Fraction as Fr
from itertools import product
import random

FAILS = []


def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)


# =============================================================== B-U
def theta(n):
    t = 0
    while n:
        t ^= n & 1
        n >>= 1
    return t


# affine maps on F5^6 as (M, t): x -> M x + t, coordinates (x0,x1,x2,x3,q,r)
def aff(rows, t):
    # Run 1 kept the entries unreduced (-1 instead of 4), so the r-row test against (1, 4)
    # failed at n = 3 on the bare table for b. Harness error; run 1 output is kept.
    return ([[v % 5 for v in r] for r in rows], [v % 5 for v in t])


I6 = [[int(i == k) for k in range(6)] for i in range(6)]
GEN = {
    "a": aff([I6[1], I6[0], I6[3], I6[2], I6[4], I6[5]], [0] * 6),
    "b": aff([[-v for v in I6[2]], [-v for v in I6[3]], [-v for v in I6[0]], [-v for v in I6[1]],
              [-v for v in I6[4]], [-v for v in I6[5]]], [0] * 6),
    "c": aff([[-v for v in I6[2]], [-a + b for a, b in zip(I6[3], I6[5])], [-v for v in I6[0]],
              [-a - b for a, b in zip(I6[1], I6[5])], [-v for v in I6[4]], [-v for v in I6[5]]], [2, 1, 2, 1, 1, 0]),
    "d": aff([[-v for v in r] for r in I6], [2, 1, 3, 4, 1, 1]),
    "e": aff([[-v for v in r] for r in I6], [2, 1, 3, 4, 2, 1]),
}
LETTERS = "abcde"


def apply(m, x):
    M, t = m
    return tuple((sum(a * b for a, b in zip(row, x)) + c) % 5 for row, c in zip(M, t))


def compose(m2, m1):
    """m2 after m1"""
    M2, t2 = m2
    M1, t1 = m1
    M = [[sum(M2[i][k] * M1[k][j] for k in range(6)) % 5 for j in range(6)] for i in range(6)]
    t = [(sum(M2[i][k] * t1[k] for k in range(6)) + t2[i]) % 5 for i in range(6)]
    return (M, t)


# the affine tables agree with the Canon formulas on every state
def canon(letter, x):
    x0, x1, x2, x3, q, r = x
    return {"a": (x1, x0, x3, x2, q, r),
            "b": (-x2 % 5, -x3 % 5, -x0 % 5, -x1 % 5, -q % 5, -r % 5),
            "c": ((2 - x2) % 5, (1 - x3 + r) % 5, (2 - x0) % 5, (1 - x1 - r) % 5, (1 - q) % 5, -r % 5),
            "d": ((2 - x0) % 5, (1 - x1) % 5, (3 - x2) % 5, (4 - x3) % 5, (1 - q) % 5, (1 - r) % 5),
            "e": ((2 - x0) % 5, (1 - x1) % 5, (3 - x2) % 5, (4 - x3) % 5, (2 - q) % 5, (1 - r) % 5)}[letter]


ok = all(apply(GEN[L], x) == canon(L, x) for L in LETTERS for x in product(range(5), repeat=6))
chk("B-U affine tables reproduce the five Canon generators on all 15625 states", ok)

# trace dynamics is autonomous: z' = f(letter, z); follow the five sheets symbolically
ZMAP = {"a": lambda z: z, "b": lambda z: -z % 5, "c": lambda z: (2 - z) % 5, "d": lambda z: (2 - z) % 5,
        "e": lambda z: (3 - z) % 5}
ok = all(sum(apply(GEN[L], x)) % 5 == ZMAP[L](sum(x) % 5) for L in LETTERS for x in product(range(5), repeat=6))
chk("B-U trace map z' = f(letter, z) on all states", ok)

N = 4096
ident = (I6, [0] * 6)
sheet_map = {z: ident for z in range(5)}          # composite affine map for origin states on sheet z
sheet_z = {z: z for z in range(5)}
words = {z: "" for z in range(5)}
first_sync = None
ok_r_row, ok_piston_block, ok_one_letter = True, True, True
ref = None                                        # composite from counter 3 on (common to all sheets)
shift_from_3 = [0]                                # r-constant of the composite 3 -> n, as integer lift
lift_sign, lift_const = 1, 0
for n in range(N):
    t = theta(n)
    used = set()
    for z0 in range(5):
        L = LETTERS[(sheet_z[z0] + 2 * t) % 5]
        used.add(L)
        if n < 3:
            words[z0] += L
        sheet_map[z0] = compose(GEN[L], sheet_map[z0])
        sheet_z[z0] = ZMAP[L](sheet_z[z0])
    if len(set(sheet_z.values())) == 1 and first_sync is None:
        first_sync = n + 1
    if n >= 3:
        ok_one_letter &= len(used) == 1 and used <= set("bde")
        L = next(iter(used))
        ref = GEN[L] if ref is None else compose(GEN[L], ref)
        M, tt = ref
        # r-row touches r only; piston rows do not touch q, r
        ok_r_row &= M[5][:5] == [0] * 5 and M[5][5] in (1, 4)
        ok_piston_block &= all(M[i][4] == 0 and M[i][5] == 0 for i in range(4))
        eps, kappa = (-1, 1) if L in "de" else (-1, 0)
        lift_sign, lift_const = eps * lift_sign, eps * lift_const + kappa
        shift_from_3.append(lift_const)
chk("B-U all five sheets are synchronized from counter 3 on", first_sync == 3, "first common sheet at n=%s" % first_sync)
chk("B-U first-three-tick words per initial sheet", words == {0: "ace", 1: "bbd", 2: "cce", 3: "dbd", 4: "ebd"}, str(words))
rrows = {z: (sheet_map_z := None) for z in range(5)}
# recompute the three-tick composites for the r-row
three = {}
for z0 in range(5):
    m = ident
    for L in words[z0]:
        m = compose(GEN[L], m)
    three[z0] = (m[0][5], m[1][5])
chk("B-U three-tick fibre maps: r+1 (z0=0), 1-r (z0=1,2), 2-r (z0=3,4), no other coordinate enters",
    three == {0: ([0, 0, 0, 0, 0, 1], 1), 1: ([0, 0, 0, 0, 0, 4], 1), 2: ([0, 0, 0, 0, 0, 4], 1),
              3: ([0, 0, 0, 0, 0, 4], 2), 4: ([0, 0, 0, 0, 0, 4], 2)})
chk("B-U for 3<=n<4096: one letter per tick (b,d,e)", ok_one_letter)
chk("B-U for 3<=n<4096: composite 3->n has r-row (0,0,0,0,0,+-1) and piston rows free of q,r", ok_r_row and ok_piston_block)


def A(M):
    tot, p = 0, 1
    while p <= M:
        tot += M // p - M // (2 * p)
        p *= 4
    return tot


ok = True
for n1 in range(5, N + 1, 2):                      # even windows from n0 = 3 = 2*2 - 1
    m = (n1 - 3) // 2
    ok &= shift_from_3[n1 - 3] == A(2 + m - 1) - A(1)
chk("B-U integer lift of the composite 3->n equals the closed form A(k)-A(1) on all even windows to 4096", ok)

# =============================================================== B-K
def red5(v5):
    return tuple(a - v5[4] for a in v5[:4])


def mul(x, y):
    acc = [0] * 5
    for i, a in enumerate(x):
        if a:
            for k, b in enumerate(y):
                acc[(i + k) % 5] += a * b
    return red5(acc)


def gal(a, x):
    acc = [0] * 5
    for i, c in enumerate(x):
        acc[(a * i) % 5] += c
    return red5(acc)


RHO = (0, 0, 1, 0)
UINV5 = (0, -1, -2, -3)                            # 5/(1-j) = -(j + 2j^2 + 3j^3 + 4j^4) = 4 + 3j + 2j^2 + j^3 ... reduced below
UINV5 = red5((0, -1, -2, -3, -4))


def div_u(v):
    """v/(1-j) for v in (1-j)O, through multiplication by 5/(1-j) and exact division by 5"""
    w = mul(v, UINV5)
    assert all(a % 5 == 0 for a in w), (v, w)
    return tuple(a // 5 for a in w)


assert mul((1, -1, 0, 0), UINV5) == (5, 0, 0, 0)


def res(v):
    return sum(v) % 5


def q_cyclic(v):
    c = (v[0], v[1], v[2], v[3], 0)
    return sum((c[i] - c[k]) ** 2 for i in range(5) for k in range(i + 1, 5)) // 2


def digit1(v):
    ct = res(v)
    return res(div_u((v[0] - ct, v[1], v[2], v[3])))


def psi(state):
    return (2 * sum(res(v) * digit1(v) for v in state)) % 5


def twist(state):
    """T = sum_i x_i * sigma_2(x_i) in O"""
    tot = (0, 0, 0, 0)
    for v in state:
        tot = tuple(a + b for a, b in zip(tot, mul(v, gal(2, v))))
    return tot


def contact(x, y):
    delta = tuple(a - b for a, b in zip(x, y))
    if any(a & 1 for a in delta):
        return x, y, False, None
    d = tuple(a // 2 for a in delta)
    s = tuple((a + b) // 2 for a, b in zip(x, y))
    r = mul(RHO, d)
    return tuple(a + b for a, b in zip(s, r)), tuple(a - b for a, b in zip(s, r)), True, d


rng = random.Random(6112026)
bad1 = bad2 = adm = 0
for _ in range(100000):
    n = rng.randint(2, 6)
    st = [tuple(rng.randint(-12, 12) for _ in range(4)) for _ in range(n)]
    i, k = rng.sample(range(n), 2)
    st[k] = tuple(a - 2 * rng.randint(-6, 6) for a in st[i])
    x2, y2, admitted, d = contact(st[i], st[k])
    assert admitted
    adm += 1
    p0, t0 = psi(st), twist(st)
    st[i], st[k] = x2, y2
    qd = q_cyclic(d)
    bad1 += (psi(st) - p0 - qd) % 5 != 0
    dT = tuple(a - b for a, b in zip(twist(st), t0))
    bad2 += (qd + res(div_u(dT))) % 5 != 0
chk("B-K fresh sample: Q(d) = psi' - psi mod 5 with the independent digit algorithm", bad1 == 0, "admitted contacts=%d" % adm)
chk("B-K second potential: Q(d) = -c((T'-T)/u) mod 5 with T = sum x*sigma_2(x)", bad2 == 0)

U = (1, -1, 0, 0)
B0 = (1, 0, -1, 0)
X = (1, 1, 0, -2)
TWO = (2, 0, 0, 0)
start = (B0, tuple(-a for a in B0), U, U, X, TWO)            # I_1
seen = {start: psi(start)}
queue = deque([start])
edges = bad = 0
while queue:
    st = queue.popleft()
    for i in range(6):
        for k in range(i + 1, 6):
            x2, y2, admitted, d = contact(st[i], st[k])
            if not admitted:
                continue
            nl = list(st)
            nl[i], nl[k] = x2, y2
            nxt = tuple(nl)
            if nxt not in seen:
                seen[nxt] = psi(nxt)
                queue.append(nxt)
            edges += 1
            bad += (seen[nxt] - seen[st] - q_cyclic(d)) % 5 != 0
chk("B-K every admitted edge of the complete I_1 orbit: Q(d) = psi(head) - psi(tail) mod 5", bad == 0,
    "states=%d admitted edges=%d" % (len(seen), edges))


# =============================================================== B-L
def AB(v):
    c = mul(v, gal(4, v))                          # A + B phi = (A, 0, -B, -B)
    assert c[1] == 0 and c[2] == c[3]
    return c[0], -c[2]


def loop_census(start, cap):
    n = len(start)
    pot = {start: (0, 0, 0)}
    queue = deque([start])
    area_bad, count_hol, capped = 0, False, False
    while queue:
        st = queue.popleft()
        p = pot[st]
        for i in range(n):
            for k in range(i + 1, n):
                x2, y2, admitted, d = contact(st[i], st[k])
                if not admitted or (x2 == st[i] and y2 == st[k]):
                    continue
                a, b = AB(d)
                nl = list(st)
                nl[i], nl[k] = x2, y2
                nxt = tuple(nl)
                cand = (p[0] + 1, p[1] + a, p[2] + b)
                have = pot.get(nxt)
                if have is None:
                    if len(pot) >= cap:
                        capped = True
                        continue
                    pot[nxt] = cand
                    queue.append(nxt)
                else:
                    dn, da, db = (c - h for c, h in zip(cand, have))
                    area_bad += (da % 5 != 0) or (db % 5 != 0)
                    count_hol |= dn % 5 != 0
    return len(pot), capped, area_bad, count_hol


stats = dict(banks=0, capped=0, area_bad=0, count_hol=0, maxsize=0)
for trial in range(400):
    n = 3 if trial % 2 == 0 else 4
    base = tuple(rng.randint(-3, 3) for _ in range(4))
    st = [base]
    for _ in range(n - 1):                         # keep parities aligned so that contacts are admitted
        st.append(tuple(a - 2 * rng.randint(-2, 2) for a in base))
    size, capped, area_bad, count_hol = loop_census(tuple(st), 20000)
    stats["banks"] += 1
    stats["capped"] += capped
    stats["area_bad"] += area_bad
    stats["count_hol"] += count_hol
    stats["maxsize"] = max(stats["maxsize"], size)
chk("B-L random three- and four-slot banks: every closed loop has Hermitian area in 5 Z[phi]", stats["area_bad"] == 0, str(stats))
print("   banks with count holonomy mod 5: %d of %d" % (stats["count_hol"], stats["banks"]))

# Section B-D of the session breaker is omitted from this public extract.
print("RESULT", "PASS" if not FAILS else "FAIL", "fails=%d" % len(FAILS))
