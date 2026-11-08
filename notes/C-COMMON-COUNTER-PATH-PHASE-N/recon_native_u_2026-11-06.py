#!/usr/bin/env python3
"""RECON-PATH-PHASE-ONE-CARRIER, Part U. NON-CANONICAL, L1, exact.

Native U of Public Canon v109 on all 15625 origin-zero states: is the fibre
phase blind to the course of a trajectory at a common counter?
Own code path, standard library only, integers only.
"""
from itertools import product

HORIZON = 64
FAILS = []


def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)


def theta(n):
    return bin(n).count("1") % 2


def trace(x):
    return sum(x) % 5


def gen_a(x):
    x0, x1, x2, x3, q, r = x
    return (x1, x0, x3, x2, q, r)


def gen_b(x):
    x0, x1, x2, x3, q, r = x
    return (-x2 % 5, -x3 % 5, -x0 % 5, -x1 % 5, -q % 5, -r % 5)


def gen_c(x):
    x0, x1, x2, x3, q, r = x
    return ((2 - x2) % 5, (1 - x3 + r) % 5, (2 - x0) % 5, (1 - x1 - r) % 5, (1 - q) % 5, -r % 5)


def gen_d(x):
    x0, x1, x2, x3, q, r = x
    return ((2 - x0) % 5, (1 - x1) % 5, (3 - x2) % 5, (4 - x3) % 5, (1 - q) % 5, (1 - r) % 5)


def gen_e(x):
    x0, x1, x2, x3, q, r = x
    return ((2 - x0) % 5, (1 - x1) % 5, (3 - x2) % 5, (4 - x3) % 5, (2 - q) % 5, (1 - r) % 5)


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)
LETTER = "abcde"
EPS_KAPPA = {"a": (1, 0), "b": (-1, 0), "c": (-1, 0), "d": (-1, 1), "e": (-1, 1)}
TRACE_MAP = {"a": lambda z: z, "b": lambda z: -z % 5, "c": lambda z: (2 - z) % 5,
             "d": lambda z: (2 - z) % 5, "e": lambda z: (3 - z) % 5}


def tick(n, x):
    idx = (trace(x) + 2 * theta(n)) % 5
    return LETTER[idx], GENS[idx](x)


ALL = list(product(range(5), repeat=6))
assert len(ALL) == 15625

# ---------------------------------------------------------------- U1
ok = True
for x in ALL:
    z = trace(x)
    for t in (0, 1):
        idx = (z + 2 * t) % 5
        y = GENS[idx](x)
        eps, kappa = EPS_KAPPA[LETTER[idx]]
        ok &= trace(y) == TRACE_MAP[LETTER[idx]](z)
        ok &= y[5] == (eps * x[5] + kappa) % 5
chk("U1 letter, new trace and fibre kick depend on (z,t) only", ok, "states=15625 bits=2")

# ---------------------------------------------------------------- trajectories
# state[n][i] = checkpoint of origin state i at counter n; lift[n][i] integer fibre lift
state = [ALL]
lift = [[x[5] for x in ALL]]
letters = []                      # letters[n][i]
for n in range(HORIZON):
    cur = state[-1]
    nxt, lt, row = [], [], []
    for i, x in enumerate(cur):
        L, y = tick(n, x)
        eps, kappa = EPS_KAPPA[L]
        nxt.append(y)
        lt.append(eps * lift[-1][i] + kappa)
        row.append(L)
    assert all(l % 5 == y[5] for l, y in zip(lt, nxt))
    state.append(nxt)
    lift.append(lt)
    letters.append(row)

# ---------------------------------------------------------------- U2
sizes = [len(set(state[n])) for n in range(HORIZON + 1)]
chk("U2 image sizes after ticks 1,2,3", sizes[1:4] == [6250, 6250, 3125], "sizes=%s" % sizes[:5])
ok = True
for n in range(3, HORIZON + 1):
    En = set(state[n])
    zn = (4 + 2 * theta(n - 1)) % 5
    ok &= len(En) == 3125 and all(trace(x) == zn for x in En)
chk("U2 for 3<=n<=64 the reachable set is the full sheet z_n=4+2theta_(n-1)", ok)
ok = True
for n in range(3, HORIZON):
    En = set(state[n])
    img = {tick(n, x)[1] for x in En}
    ok &= len(img) == 3125 and img == set(state[n + 1])
chk("U2 tick is a bijection E_n -> E_(n+1) for 3<=n<64", ok)

# ---------------------------------------------------------------- U3
def swapP(v):
    return (v[2], v[3], v[0], v[1], v[4], v[5])


ok_affine, ok_single = True, True
word = []
for n in range(3, HORIZON):
    En = sorted(set(state[n]))
    L0, y0 = tick(n, En[0])
    used = {tick(n, x)[0] for x in En}
    ok_single &= len(used) == 1
    word.append(L0)
    for x in En:
        dx = tuple((a - b) % 5 for a, b in zip(x, En[0]))
        Lx, y = tick(n, x)
        dy = tuple((a - b) % 5 for a, b in zip(y, y0))
        lin = swapP(dx) if L0 == "b" else dx
        ok_affine &= dy == tuple(-a % 5 for a in lin)
chk("U3 one letter per tick on E_n, 3<=n<64 (letters b,d,e only)", ok_single and set(word) <= set("bde"),
    "word(3..18)=%s" % "".join(word[:16]))
chk("U3 the tick on E_n is one affine map with linear part -P (b) or -I (d,e)", ok_affine)

ok, nwin = True, 0
for n0 in range(3, HORIZON):
    for n1 in range(n0 + 1, HORIZON + 1):
        sgn = 1 if (n1 - n0) % 2 == 0 else -1
        vals = {lift[n1][i] - sgn * lift[n0][i] for i in range(15625)}
        ok &= len(vals) == 1
        nwin += 1
chk("U3 lifted shift rt_n1-(-1)^(n1-n0) rt_n0 is one integer on all 15625 trajectories", ok,
    "windows=%d (3<=n0<n1<=64)" % nwin)
ok = True
for n in range(3, HORIZON):
    ok &= all((state[n + 1][i][5] - state[n + 1][0][5]) % 5 == (-(state[n][i][5] - state[n][0][5])) % 5
              for i in range(15625))
chk("U3 fibre difference of any two trajectories only changes sign, n>=3", ok)

# ---------------------------------------------------------------- U4
ok = True
for n in range(3, HORIZON):
    f = {}
    for i in range(15625):
        p, p2 = state[n][i][:4], state[n + 1][i][:4]
        if f.setdefault(p, p2) != p2:
            ok = False
    ok &= len(f) == 625 and len(set(f.values())) == 625
chk("U4 pistons at n+1 are a bijective function of pistons at n alone, 3<=n<64", ok)

# ---------------------------------------------------------------- U5
fib = {}
for i, x in enumerate(ALL):
    fib.setdefault(state[3][i], []).append(i)
ok_count = all(len(v) == 5 for v in fib.values()) and len(fib) == 3125
ok_sheets = all(sorted(trace(ALL[i]) for i in v) == [0, 1, 2, 3, 4] for v in fib.values())
RULE = {0: (1, 1), 1: (-1, 1), 2: (-1, 1), 3: (-1, 2), 4: (-1, 2)}
ok_r = all(state[3][i][5] == (RULE[trace(ALL[i])][0] * ALL[i][5] + RULE[trace(ALL[i])][1]) % 5
           for i in range(15625))
words3 = {}
for i, x in enumerate(ALL):
    words3.setdefault(trace(x), set()).add(letters[0][i] + letters[1][i] + letters[2][i])
chk("U5 every y in E_3 has exactly five origin preimages, one per trace sheet", ok_count and ok_sheets)
chk("U5 r_3 = r_0+1 (z0=0), 1-r_0 (z0=1,2), 2-r_0 (z0=3,4)", ok_r,
    "first-three-tick words by z0: %s" % {z: sorted(w) for z, w in sorted(words3.items())})

# ---------------------------------------------------------------- U6
def A(M):
    tot, p = 0, 1
    while p <= M:
        tot += M // p - M // (2 * p)
        p *= 4
    return tot


def closed(n0, n1):
    m = (n1 - n0) // 2
    if n0 % 2:
        k0 = (n0 + 1) // 2
        return A(k0 + m - 1) - A(k0 - 1)
    k0 = n0 // 2
    return -(A(k0 + m - 1) - A(k0 - 1))


adm = [i for i, x in enumerate(ALL) if trace(x) in (1, 4)]
assert len(adm) == 6250
ok_all, ok_adm, nw = True, True, 0
for n0 in range(1, HORIZON):
    for n1 in range(n0 + 2, HORIZON + 1, 2):
        want = closed(n0, n1)
        if n0 >= 3:
            ok_all &= all(lift[n1][i] - lift[n0][i] == want for i in range(15625))
        ok_adm &= all(lift[n1][i] - lift[n0][i] == want for i in adm)
        nw += 1
chk("U6 closed form of the even-window shift, all states for n0>=3", ok_all)
chk("U6 closed form of the even-window shift, X1 union X4 for n0>=1", ok_adm, "even windows=%d" % nw)
pr = (closed(1, 11), closed(11, 21), closed(21, 31), closed(1, 31), closed(2, 32))
chk("U6 PR #1915 windows 1->11, 11->21, 21->31 give +4,+2,+4; 1->31 and 2->32 give +10,-10",
    pr == (4, 2, 4, 10, -10), "values=%s" % (pr,))

# ---------------------------------------------------------------- U7 census
marks = (1, 0, 1)
hist, hist_all = {}, {}
for n0 in range(1, 4096, 2):
    s = closed(n0, n0 + 10)
    hist_all[s] = hist_all.get(s, 0) + 1
    if (n0 % 5, theta(n0 - 1), theta(n0)) == marks:
        hist[s] = hist.get(s, 0) + 1
print("CENSUS ten-tick shift over odd n0<4096 with marks (n0 mod 5,theta_(n0-1),theta_n0)=(1,0,1):",
      dict(sorted(hist.items())))
print("CENSUS ten-tick shift over all odd n0<4096:", dict(sorted(hist_all.items())))
chk("U7 equal finite marks do not fix the shift (more than one value occurs)", len(hist) > 1)

print("RESULT", "PASS" if not FAILS else "FAIL", "fails=%d" % len(FAILS))
