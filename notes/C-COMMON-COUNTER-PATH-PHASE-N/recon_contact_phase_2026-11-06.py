#!/usr/bin/env python3
"""RECON-PATH-PHASE-ONE-CARRIER, Part K. NON-CANONICAL, L1, exact.

Contact carrier of PR #1908 (O=Z[j], total relative contact with parity
admission). Which five-position phases see the course of a path at a common
counter, and is the count phase a function of the area vector on closed loops?
Own code path, standard library only, integers only.
Usage: python3 -I -B recon_contact_phase_2026-11-06.py <path to WORD.txt>
"""
from collections import deque
from hashlib import sha256
from itertools import product
import random
import sys

WORD_SHA256 = "6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7"
CAP = 200000
FAILS = []


def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)


# ---------------------------------------------------------------- ring O = Z[j], power basis
def rho_times(v):
    a, b, c, d = v
    return (d - c, -c, a - c, b - c)          # j^2 * (a + b j + c j^2 + d j^3)


def contact(x, y):
    """returns x', y', admitted, changed, d"""
    delta = (x[0] - y[0], x[1] - y[1], x[2] - y[2], x[3] - y[3])
    if delta[0] & 1 or delta[1] & 1 or delta[2] & 1 or delta[3] & 1:
        return x, y, False, False, None
    d = (delta[0] // 2, delta[1] // 2, delta[2] // 2, delta[3] // 2)
    s = ((x[0] + y[0]) // 2, (x[1] + y[1]) // 2, (x[2] + y[2]) // 2, (x[3] + y[3]) // 2)
    r = rho_times(d)
    x2 = (s[0] + r[0], s[1] + r[1], s[2] + r[2], s[3] + r[3])
    y2 = (s[0] - r[0], s[1] - r[1], s[2] - r[2], s[3] - r[3])
    return x2, y2, True, (x2 != x or y2 != y), d


def res(v):
    return sum(v) % 5


def AB(v):
    a0, a1, a2, a3 = v
    s1 = a0 * a1 + a1 * a2 + a2 * a3
    s2 = a0 * a2 + a1 * a3 + a0 * a3
    return a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3 - s1, s1 - s2      # v vbar = A + B phi


def Q(v):
    A, B = AB(v)
    return 2 * A + B


def first_digit(v):
    """c((v - ct)/u) for u = 1 - j, ct in {0..4} the lift of the residue"""
    ct = res(v)
    z = (v[0] - ct, v[1], v[2], v[3])
    tot = sum(z)
    assert tot % 5 == 0
    m = -tot // 5
    b = (z[0] + m, z[1] + m, z[2] + m, z[3] + m, m)
    q0 = b[0]
    q1 = b[1] + q0
    q2 = b[2] + q1
    q3 = b[3] + q2
    assert b[4] + q3 == 0
    return (q0 + q1 + q2 + q3) % 5


def psi(state):
    return (2 * sum(res(v) * first_digit(v) for v in state)) % 5


assert AB((1, -1, 0, 0)) == (3, -1) and Q((1, -1, 0, 0)) == 5 and Q((2, 0, 0, 0)) == 8
assert Q((1, 1, 0, -2)) == 15 and Q((1, 0, -1, 0)) == 5
assert first_digit((1, -1, 0, 0)) == 1 and first_digit((2, 0, 0, 0)) == 0

U = (1, -1, 0, 0)
B0 = (1, 0, -1, 0)
X = (1, 1, 0, -2)
TWO = (2, 0, 0, 0)
ZERO = (0, 0, 0, 0)


def sc(t, v):
    return tuple(t * a for a in v)


def add(v, w):
    return tuple(a + b for a, b in zip(v, w))


def prep(t):
    return (sc(t, B0), sc(-t, B0), U, U, X, TWO)


def target(t):
    return (add(U, sc(t, B0)), add(U, sc(-t, B0)), ZERO, ZERO, X, TWO)


# ---------------------------------------------------------------- K1..K4 on the public word
raw = open(sys.argv[1], "rb").read()
chk("K1 WORD.txt custody", sha256(raw).hexdigest() == WORD_SHA256 and len(raw) == 966)
word = [(int(l[0]) - 1, int(l[1]) - 1) for l in raw.decode("ascii").split()]
assert len(word) == 322
perm = (1, 0, 2, 3, 4, 5)
sigma = [tuple(sorted((perm[i], perm[k]))) for i, k in word]


def run(program, start):
    st = list(start)
    tot = dict(adm=0, ref=0, chg=0, dia=0, N6=0, S=0, A=0, B=0, inner_bad=0, k2_bad=0)
    p_before = psi(st)
    for i, k in program:
        x2, y2, admitted, changed, d = contact(st[i], st[k])
        if not admitted:
            tot["ref"] += 1
            continue
        tot["adm"] += 1
        tot["chg" if changed else "dia"] += 1
        a, b = AB(d)
        qd = 2 * a + b
        tot["S"] += qd
        tot["A"] += a
        tot["B"] += b
        if k == 5 or i == 5:
            tot["N6"] += 1
        elif qd % 5:
            tot["inner_bad"] += 1
        st[i], st[k] = x2, y2
        p_after = psi(st)
        if (p_after - p_before - qd) % 5:
            tot["k2_bad"] += 1
        p_before = p_after
    return tuple(st), tot


TABLE = {-2: (137, 185, 135, 2), -1: (177, 145, 170, 7), 0: (112, 210, 100, 12),
         1: (177, 145, 170, 7), 2: (123, 199, 123, 0)}
runs = {}
ok_end, ok_cnt, ok_mirror = True, True, True
for name, program in (("w", word), ("sigma", sigma)):
    for t in (-2, -1, 0, 1, 2):
        end, tot = run(program, prep(t))
        runs[name, t] = tot
        ok_end &= end == target(t)
        got = (tot["adm"], tot["ref"], tot["chg"], tot["dia"])
        want = TABLE[t] if name == "w" else TABLE[-t]
        ok_cnt &= got == want
        print("RUN %-5s t=%+d adm=%d ref=%d chg=%d dia=%d N6=%d S=%d sumA=%d sumB=%d  mod5: chg=%d adm=%d N6=%d S=%d A=%d B=%d"
              % (name, t, tot["adm"], tot["ref"], tot["chg"], tot["dia"], tot["N6"], tot["S"], tot["A"], tot["B"],
                 tot["chg"] % 5, tot["adm"] % 5, tot["N6"] % 5, tot["S"] % 5, tot["A"] % 5, tot["B"] % 5))
chk("K1 all ten runs end at the complete target G_t", ok_end)
chk("K1 counts (admitted, refused, changed, diagonal) equal the public table; sigma at t equals w at -t", ok_cnt)
chk("K2 on the ten runs: Q(d) = psi(after) - psi(before) mod 5 at every admitted contact",
    all(v["k2_bad"] == 0 for v in runs.values()), "admitted contacts=%d" % sum(v["adm"] for v in runs.values()))
chk("K3 N6 = 0 mod 5 in each of the ten runs", all(v["N6"] % 5 == 0 for v in runs.values()),
    "N6=%s" % [runs[n, t]["N6"] for n in ("w", "sigma") for t in (-2, -1, 0, 1, 2)])
chk("K3 S = sum Q(d) = 0 mod 5 in each of the ten runs", all(v["S"] % 5 == 0 for v in runs.values()),
    "S=%s" % [runs[n, t]["S"] for n in ("w", "sigma") for t in (-2, -1, 0, 1, 2)])
chk("K3 every admitted contact inside slots 1..5 has Q(d) = 0 mod 5", all(v["inner_bad"] == 0 for v in runs.values()))
dN = {t: runs["w", t]["chg"] - runs["sigma", t]["chg"] for t in (-2, -1, 0, 1, 2)}
chk("K4 count difference w minus sigma at common start, end and 322 contacts", dN == {-2: 12, -1: 0, 0: 0, 1: 0, 2: -12},
    "dN=%s mod5=%s" % (dN, {t: v % 5 for t, v in dN.items()}))

# ---------------------------------------------------------------- K2 audits
bad, admitted_pairs = 0, 0
box = list(product(range(-2, 3), repeat=4))
for x in box:
    for y in box:
        x2, y2, admitted, changed, d = contact(x, y)
        if admitted:
            admitted_pairs += 1
            if (psi((x2, y2)) - psi((x, y)) - Q(d)) % 5:
                bad += 1
chk("K2 box audit [-2,2]^4 x [-2,2]^4", bad == 0, "ordered pairs=%d admitted=%d" % (len(box) ** 2, admitted_pairs))
rng = random.Random(20261106)
bad, admitted_rand = 0, 0
for _ in range(200000):
    st = [tuple(rng.randint(-9, 9) for _ in range(4)) for _ in range(6)]
    i, k = rng.sample(range(6), 2)
    if rng.random() < 0.7:                      # force admission in most trials
        st[k] = tuple(a - 2 * rng.randint(-4, 4) for a in st[i])
    x2, y2, admitted, changed, d = contact(st[i], st[k])
    if admitted:
        admitted_rand += 1
        p0 = psi(st)
        st[i], st[k] = x2, y2
        if (psi(st) - p0 - Q(d)) % 5:
            bad += 1
chk("K2 seeded random six-slot audit", bad == 0, "trials=200000 admitted=%d" % admitted_rand)

# ---------------------------------------------------------------- K5 holonomy
def span_f5(vectors, width):
    """row echelon basis over F5 of a set of integer tuples"""
    basis = []
    for v in sorted(set(vectors)):
        v = [a % 5 for a in v]
        for b in basis:
            piv = next(i for i, a in enumerate(b) if a)
            if v[piv]:
                f = v[piv] * pow(b[piv], -1, 5) % 5
                v = [(a - f * c) % 5 for a, c in zip(v, b)]
        if any(v):
            piv = next(i for i, a in enumerate(v) if a)
            inv = pow(v[piv], -1, 5)
            basis.append([a * inv % 5 for a in v])
    return basis


def classify(defects):
    """defects: set of (nchg, a, b) mod 5"""
    basis = span_f5(defects, 3)
    on_v = all((2 * a + b) % 5 == 0 for _, a, b in defects)
    dim = len(basis)
    if dim == 0:
        kind = "EXACT (no holonomy)"
    elif dim == 2:
        kind = "COUNT NOT A FUNCTION OF AREA (dim 2, contains (1,0,0))"
    else:
        n0, a0, b0 = basis[0]
        if a0 == 0 and b0 == 0:
            kind = "COUNT HOLONOMY WITH ZERO AREA (H_AREA fired)"
        elif n0 == 0:
            kind = "AREA HOLONOMY, COUNT EXACT (kappa=0)"
        else:
            kind = "LAW N=kappa*a, kappa=%d" % (n0 * pow(a0, -1, 5) % 5)
    return dim, basis, on_v, kind


def orbit_holonomy(start, cap=CAP):
    n = len(start)
    pairs = [(i, k) for i in range(n) for k in range(i + 1, n)]
    pot = {start: (0, 0, 0, 0)}                 # (nchg, nadm, A, B) mod 5 along the BFS tree
    queue = deque([start])
    defects = set()
    edges, skipped, capped = 0, 0, False
    while queue:
        st = queue.popleft()
        p = pot[st]
        for i, k in pairs:
            x2, y2, admitted, changed, d = contact(st[i], st[k])
            if not admitted:
                continue
            edges += 1
            if changed:
                a, b = AB(d)
                w = (1, 1, a % 5, b % 5)
                nl = list(st)
                nl[i], nl[k] = x2, y2
                nxt = tuple(nl)
            else:
                w = (0, 1, 0, 0)
                nxt = st
            cand = ((p[0] + w[0]) % 5, (p[1] + w[1]) % 5, (p[2] + w[2]) % 5, (p[3] + w[3]) % 5)
            have = pot.get(nxt)
            if have is None:
                if len(pot) >= cap:
                    capped = True
                    skipped += 1
                    continue
                pot[nxt] = cand
                queue.append(nxt)
            else:
                df = tuple((c - h) % 5 for c, h in zip(cand, have))
                if any(df):
                    defects.add(df)
    return len(pot), edges, capped, skipped, defects


def report(label, start, cap=CAP):
    size, edges, capped, skipped, defects = orbit_holonomy(start, cap)
    prim = {(d[0], d[2], d[3]) for d in defects}
    sec = {(d[1], d[2], d[3]) for d in defects}
    dim, basis, on_v, kind = classify(prim)
    dim2, basis2, on_v2, kind2 = classify(sec)
    print("ORBIT %s states=%d%s admitted_edges=%d distinct_defects=%d | primary dim H=%d basis(n,a,b)=%s on V(2a+b=0)=%s -> %s | secondary(all admitted) dim=%d basis=%s -> %s"
          % (label, size, " (CAPPED, %d edges skipped)" % skipped if capped else " (complete)", edges, len(defects),
             dim, basis, on_v, kind, dim2, basis2, kind2))
    return size, capped, dim, basis, on_v, kind, dim2, kind2


# (i) the single loop w * sigma^-1 at I_-2
a, b = runs["w", -2], runs["sigma", -2]
loop = ((a["chg"] - b["chg"]) % 5, (a["A"] - b["A"]) % 5, (a["B"] - b["B"]) % 5)
print("LOOP w*sigma^-1 at I_-2: integer differences dNchg=%d dNadm=%d dS=%d dA=%d dB=%d ; mod 5 (n,a,b)=%s ; 2a+b=%d"
      % (a["chg"] - b["chg"], a["adm"] - b["adm"], a["S"] - b["S"], a["A"] - b["A"], a["B"] - b["B"], loop,
         (2 * loop[1] + loop[2]) % 5))
chk("K5(i) loop vector lies on V (2a+b=0)", (2 * loop[1] + loop[2]) % 5 == 0)
if loop[1] == 0 and loop[0] != 0:
    print("K5(i) OUTCOME: count holonomy %d with zero area vector mod 5 -> H_AREA FIRED on this loop" % loop[0])
elif loop[1] != 0:
    print("K5(i) OUTCOME: one loop fixes kappa = %d (to be confronted with the orbits)" % (loop[0] * pow(loop[1], -1, 5) % 5))
else:
    print("K5(i) OUTCOME: loop vector is zero")

# (ii),(iii) six-slot orbits
six = {}
six[0] = report("six-slot I_0", prep(0), cap=10 ** 7)
six[1] = report("six-slot I_1", prep(1))
six[-2] = report("six-slot I_-2", prep(-2))
# Run 1 asserted 1556 states here. That number is the orbit under the 64-macro bank K0 of the
# 2026-11-04 review, not under all fifteen single contacts; the side assertion was a harness
# error outside the frozen clauses. Run 1 output is kept; the size is now only recorded.
print("NOTE six-slot orbit sizes under all fifteen single contacts: I_0=%d complete=%s, I_1=%d complete=%s"
      % (six[0][0], not six[0][1], six[1][0], not six[1][1]))
chk("K5 all six-slot defects lie on V (2a+b=0)", all(v[4] for v in six.values()))

# (iv) three-slot orbits
NEG_U = (-1, 1, 0, 0)
NEG_B0 = (-1, 0, 1, 0)
SET7 = {"0": ZERO, "1": (1, 0, 0, 0), "2": TWO, "u": U, "-u": NEG_U, "B0": B0, "-B0": NEG_B0}
hist, hist2, sizes, on_v_all, any_capped = {}, {}, [], True, 0
examples = {}
seen_orbits = {}
for names in product(SET7, repeat=3):
    start = tuple(SET7[nm] for nm in names)
    size, edges, capped, skipped, defects = orbit_holonomy(start)
    prim = {(d[0], d[2], d[3]) for d in defects}
    sec = {(d[1], d[2], d[3]) for d in defects}
    dim, basis, on_v, kind = classify(prim)
    dim2, basis2, on_v2, kind2 = classify(sec)
    hist[kind] = hist.get(kind, 0) + 1
    hist2[kind2] = hist2.get(kind2, 0) + 1
    sizes.append(size)
    on_v_all &= on_v
    any_capped += capped
    examples.setdefault(kind, (names, size, basis))
print("THREE-SLOT 343 triples: orbit sizes min=%d max=%d capped=%d" % (min(sizes), max(sizes), any_capped))
for kind, cnt in sorted(hist.items()):
    print("THREE-SLOT primary  %4d  %s   e.g. %s states=%d basis=%s" % ((cnt, kind) + examples[kind]))
for kind, cnt in sorted(hist2.items()):
    print("THREE-SLOT secondary %4d  %s" % (cnt, kind))
chk("K5 all three-slot defects lie on V (2a+b=0)", on_v_all)

fired = [k for k in list(hist) + [v[5] for v in six.values()] if k.startswith("COUNT")]
laws = sorted({k for k in list(hist) + [v[5] for v in six.values()] if k.startswith("LAW")})
print("K5 VERDICT: H_AREA %s ; kinds with a law: %s" % ("FIRED (count phase is not a function of the area vector)" if fired else "not fired", laws))
print("RESULT", "PASS" if not FAILS else "FAIL", "fails=%d" % len(FAILS))
