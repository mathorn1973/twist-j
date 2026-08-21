#!/usr/bin/env python3
# breaker_rh_hankel_hard_edge_2.py
# Independent attack and diagnosis path for P-RH-HANKEL-HARD-EDGE-2.
# Floats allowed. NO AUTHORITY. Nothing here gates anything.
# Independent choices: closed-form R only, plain Fraction Horner for exact
# signs, Simpson quadrature, complex floats for detection and the ceiling
# recomputation (FH5 cross-check of the verifier's exact table).
import math
import random
from fractions import Fraction as Fr

random.seed(0)
FINDINGS = []


def note(line):
    print(line)


def R_closed(m):
    f = math.factorial
    return [Fr(f(2 * m - k) * 2 ** k, 4 ** m * f(m) * f(k) * f(m - k))
            for k in range(m + 1)]


RMAX = 60
R = [R_closed(m) for m in range(RMAX + 1)]


def pmul(a, b):
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x != 0:
            for j, y in enumerate(b):
                r[i + j] += x * y
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def cscale(d):
    return Fr(33, 4) * d + 21


def gate_poly(P):
    k = pmul([Fr(0), Fr(2), Fr(-1)], pmul(P, P))
    G = [Fr(0)]
    for m in range(1, len(k)):
        if k[m] != 0:
            RR = R[m - 1]
            if len(G) < len(RR):
                G = G + [Fr(0)] * (len(RR) - len(G))
            for i, c in enumerate(RR):
                G[i] += k[m] * c
    while len(G) > 1 and G[-1] == 0:
        G.pop()
    return G


def sign_exact(G, x):
    acc = Fr(0)
    for c in reversed(G):
        acc = acc * x + c
    return (acc > 0) - (acc < 0)


def last_crossing(G, xlo_f, hint_hi):
    x = xlo_f
    grid = []
    while x < hint_hi:
        grid.append(x)
        x += 0.25
    signs = [sign_exact(G, Fr(int(round(g * 4096)), 4096)) for g in grid]
    idx = None
    for i in range(len(signs) - 1):
        if signs[i] > 0 and signs[i + 1] < 0:
            idx = i
    if idx is None:
        return None
    a, b = grid[idx], grid[idx + 1]
    for _ in range(40):
        m = 0.5 * (a + b)
        if sign_exact(G, Fr(int(round(m * 2 ** 20)), 2 ** 20)) > 0:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


LOG2 = math.log(2.0)
DSET = [2, 4, 8, 16, 24]
CEILD = [8, 16, 24, 32, 48]
THETAS = [Fr(0), Fr(-399, 100), Fr(-19599, 100), Fr(-575, 16)]

note("P-RH-HANKEL-HARD-EDGE-2 breaker (no authority, floats allowed)")

# B1: quadrature vs closed form
note("B1 quadrature vs closed form")
worst = 0.0
for (m, x) in [(1, 0.7), (2, 1.3), (3, 2.0), (4, 3.5), (5, 5.0), (6, 8.0)]:
    L, n = 120.0, 240000
    h = L / n
    s = 0.0
    for i in range(n + 1):
        t = i * h
        w = 1.0 if i in (0, n) else (4.0 if i % 2 == 1 else 2.0)
        s += w * math.cos(x * t) / (1.0 + t * t) ** m
    s *= 2.0 * h / 3.0
    s += -2.0 * math.sin(x * L) / (x * (1.0 + L * L) ** m)
    Rv = 0.0
    for k, cf in enumerate(R_closed(m - 1)):
        Rv += float(cf) * x ** k
    ref = math.pi * math.exp(-x) * Rv
    rel = abs(s - ref) / abs(ref)
    worst = max(worst, rel)
    note("  m=%d x=%.2f rel=%.2e" % (m, x, rel))
note("B1 worst rel error %.2e -> %s" % (worst, "OK" if worst < 1e-5 else "DISCREPANCY"))
if worst >= 1e-5:
    FINDINGS.append("B1 quadrature discrepancy")

# B2: crossing localization vs the beta=21 threshold on D
note("B2 last +to- crossing vs threshold c_d log2, beta=21")
for d in DSET:
    c = float(cscale(d))
    xlo = c * LOG2
    for th in [None] + THETAS:
        if th is None:
            P = [Fr(0)] * d + [Fr(1)]
            tag = "F0"
        else:
            cc = cscale(d)
            a = 1 + th / (cc * cc)
            P = [Fr(0)] * d + [-a, Fr(1)]
            tag = "F1 theta=%s" % th
        G = gate_poly(P)
        xhi_fr = cscale(d) * Fr(693148, 10 ** 6)
        s_hi = sign_exact(G, xhi_fr)
        r = last_crossing(G, max(0.5, xlo - 40.0), xlo + 10.0)
        if r is None:
            note("  d=%d %s no crossing in scan, sign(xhi)=%+d" % (d, tag, s_hi))
            continue
        note("  d=%d %s crossing=%.4f xlo=%.4f margin=%.4f sign(xhi)=%+d"
             % (d, tag, r, xlo, xlo - r, s_hi))
        if s_hi > 0:
            FINDINGS.append("positive at xhi: %s d=%d" % (tag, d))

# B3: float recheck of pinned detection values at d=24
note("B3 float recheck of GATEA at d=24")
ALPHAS = [("alpha1", 0.1, 2.0), ("alpha2", 0.1, 14.0), ("alpha3", 0.25, 6.0)]
c24 = float(cscale(24))
MATCH = {"alpha1": -3.99, "alpha2": -195.99, "alpha3": -35.9375}
for (name, de, T) in ALPHAS:
    al2 = complex(de * de - T * T, 2 * de * T)
    for th in [0.0, -3.99, -195.99, -35.9375]:
        a = 1 + th / (c24 * c24)
        q = c24 * c24 / (c24 * c24 - al2)
        Pq = (q ** 24) * (q - a)
        V = 2.0 * (q * (2 - q) * Pq * Pq).real
        note("  %s theta=%s V=%.6e sign=%+d" % (name, th, V, (V > 0) - (V < 0)))

# B4: roam 200 random quartets, matched theta, d=24, against the ceiling law
note("B4 roam: 200 random quartets, matched theta, d=24, c=%.1f" % c24)
fails = 0
below_ceiling_fails = 0
law = 1.27  # diagnostic constant from the verifier table, [R] only
for i in range(200):
    de = random.uniform(0.01, 0.49)
    T = random.uniform(0.5, 30.0)
    th = de * de - T * T
    a = 1 + th / (c24 * c24)
    al2 = complex(th, 2 * de * T)
    q = c24 * c24 / (c24 * c24 - al2)
    Pq = (q ** 24) * (q - a)
    V = 2.0 * (q * (2 - q) * Pq * Pq).real
    Tstar = law * de ** (1.0 / 3.0) * c24 ** (2.0 / 3.0)
    if V >= 0:
        fails += 1
        if T < 0.85 * Tstar:
            below_ceiling_fails += 1
note("  failures: %d of 200, failures below 0.85*T*(law): %d"
     % (fails, below_ceiling_fails))
if below_ceiling_fails:
    FINDINGS.append("B4 detection failure well below the ceiling law: %d"
                    % below_ceiling_fails)

# B5: independent float recomputation of the full ceiling table (FH5)
note("B5 ceiling table recomputation, complex float")
mism = 0
expected = {}
for de_f, de_s in [(0.1, "1/10"), (0.25, "1/4")]:
    for d in CEILD:
        c = float(cscale(d))
        n_fail = 0
        t_ff = None
        for k in range(1, 101):
            T = 0.5 * k
            th = de_f * de_f - T * T
            a = 1 + th / (c * c)
            al2 = complex(th, 2 * de_f * T)
            q = c * c / (c * c - al2)
            Pq = (q ** d) * (q - a)
            V = 2.0 * (q * (2 - q) * Pq * Pq).real
            if V >= 0:
                n_fail += 1
                if t_ff is None:
                    t_ff = T
        ratio = (t_ff ** 3) / (de_f * c * c) if t_ff else float("nan")
        note("  delta=%s d=%d T_ff=%s n_fail=%d Tff^3/(delta c^2)=%.4f"
             % (de_s, d, t_ff, n_fail, ratio))
note("B5 compare these rows against the verifier CEILING lines by eye and")
note("   by the committed stdouts; any T_ff or n_fail mismatch fires FH5.")

note("FINDINGS: %d" % len(FINDINGS))
for f in FINDINGS:
    note("  " + f)
note("breaker done")
