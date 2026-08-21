#!/usr/bin/env python3
# breaker_rh_hankel_hard_edge_1.py
# Independent attack and diagnosis path for P-RH-HANKEL-HARD-EDGE-1.
# Floats allowed. NO AUTHORITY. Nothing here gates anything.
# Independent choices: closed-form R only (no recurrence), plain Fraction
# Horner for exact signs (no homogenization), Simpson quadrature for the
# Fourier identity, complex floats for detection values.
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


RMAX = 55
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


def cscale(d, beta=Fr(9, 2)):
    return Fr(33, 4) * d + beta


def cheb(kind, d):
    y = [Fr(-1), Fr(2)]
    if kind == "T":
        p0, p1 = [Fr(1)], list(y)
    else:
        p0, p1 = [Fr(1)], [Fr(-2), Fr(4)]
    for _ in range(d - 1):
        nxt = pmul([Fr(-2), Fr(4)], p1)
        nxt = [nxt[i] - (p0[i] if i < len(p0) else 0) for i in range(len(nxt))]
        p0, p1 = p1, nxt
    return p1 if d >= 1 else p0


def members(d, beta=Fr(9, 2)):
    c = cscale(d, beta)
    out = [("F0", "-", [Fr(0)] * d + [Fr(1)])]
    for th in [Fr(0), Fr(-399, 100), Fr(-19599, 100), Fr(-575, 16)]:
        a = 1 + th / (c * c)
        out.append(("F1", str(th), [Fr(0)] * d + [-a, Fr(1)]))
    out.append(("F2", "-", cheb("T", d)))
    out.append(("F3", "-", cheb("U", d)))
    return out


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
    # numeric-guided, exact-sign bisection of the last +to- crossing at or
    # above xlo_f; returns None if G already negative on the scanned grid
    lo = None
    x = xlo_f
    step = 0.25
    top = hint_hi
    grid = []
    while x < top:
        grid.append(x)
        x += step
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

note("P-RH-HANKEL-HARD-EDGE-1 breaker (no authority, floats allowed)")

# B1: quadrature check of FT[ (1+t^2)^-m ](x) = pi exp(-x) R_{m-1}(x)
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
    s *= 2.0 * h / 3.0  # even integrand, both half-lines
    # first-order integration-by-parts tail correction, both half-lines
    s += -2.0 * math.sin(x * L) / (x * (1.0 + L * L) ** m)
    Rv = 0.0
    for k, cf in enumerate(R_closed(m - 1)):
        Rv += float(cf) * x ** k
    ref = math.pi * math.exp(-x) * Rv
    rel = abs(s - ref) / abs(ref)
    worst = max(worst, rel)
    note("  m=%d x=%.2f quad=%.10e closed=%.10e rel=%.2e" % (m, x, s, ref, rel))
note("B1 worst rel error %.2e -> %s" % (worst, "OK" if worst < 1e-5 else "DISCREPANCY"))
if worst >= 1e-5:
    FINDINGS.append("B1 quadrature discrepancy")

# B2: locate the last crossing of every member, exact sign at xhi
note("B2 last +to- crossing of G vs threshold c_d log2 (exact-sign bisection)")
for d in DSET:
    c = float(cscale(d))
    xlo = c * LOG2
    for (fam, tag, P) in members(d):
        G = gate_poly(P)
        xhi_fr = cscale(d) * Fr(693148, 10 ** 6)
        s_hi = sign_exact(G, xhi_fr)
        r = last_crossing(G, max(0.5, xlo - 30.0), xlo + 40.0)
        if r is None:
            note("  d=%d %s theta=%s no +to- crossing in scan, sign(xhi)=%+d"
                 % (d, fam, tag, s_hi))
            continue
        note("  d=%d %s theta=%s crossing=%.4f xlo=%.4f deficit=%.4f "
             "offset_b=%.4f sign(xhi)=%+d"
             % (d, fam, tag, r, xlo, r - xlo,
                r - 2.0 * math.sqrt(2.0) * (2 * d), s_hi))
        if s_hi > 0:
            FINDINGS.append("certified positive at xhi: %s theta=%s d=%d"
                            % (fam, tag, d))

# B3: independent float recomputation of every GATEA value at d=24
note("B3 independent detection values, complex float")
ALPHAS = [("alpha1", 0.1, 2.0), ("alpha2", 0.1, 14.0), ("alpha3", 0.25, 6.0)]
c24 = float(cscale(24))
for (name, de, T) in ALPHAS:
    al2 = complex(de * de - T * T, 2 * de * T)
    for (fam, tag, P) in members(24):
        q = c24 * c24 / (c24 * c24 - al2)
        Pq = 0j
        for cf in reversed(P):
            Pq = Pq * q + complex(float(cf))
        V = 2.0 * (q * (2 - q) * Pq * Pq).real
        note("  %s %s theta=%s V=%.6e sign=%+d" % (name, fam, tag, V,
             (V > 0) - (V < 0)))

# B4: roam random quartets, matched F1 member at d=24
note("B4 roam: 200 random quartets, matched theta, d=24")
fails = 0
worst_case = None
for i in range(200):
    de = random.uniform(0.01, 0.49)
    T = random.uniform(0.5, 30.0)
    th = de * de - T * T
    a = 1 + th / (c24 * c24)
    al2 = complex(th, 2 * de * T)
    q = c24 * c24 / (c24 * c24 - al2)
    Pq = (q ** 24) * (q - a)
    V = 2.0 * (q * (2 - q) * Pq * Pq).real
    if V >= 0:
        fails += 1
        if worst_case is None:
            worst_case = (de, T, V)
note("  detection failures: %d of 200%s"
     % (fails, "" if worst_case is None else
        "  first fail delta=%.4f T=%.4f V=%.3e" % worst_case))
if fails:
    FINDINGS.append("B4 matched-detection failures at d=24: %d/200" % fails)

# B5: diagnostic beta scan for F1 theta=-399/100 (no authority, successor aim)
note("B5 beta scan, F1 theta=-399/100: minimal integer beta with clean pass")
for d in [2, 8, 24]:
    found = None
    for bint in range(5, 21):
        beta = Fr(bint)
        c = cscale(d, beta)
        th = Fr(-399, 100)
        a = 1 + th / (c * c)
        P = [Fr(0)] * d + [-a, Fr(1)]
        G = gate_poly(P)
        xlo_fr = c * Fr(693147, 10 ** 6)
        if sign_exact(G, xlo_fr) < 0:
            r = last_crossing(G, float(xlo_fr), float(xlo_fr) + 40.0)
            if r is None:
                found = bint
                break
    note("  d=%d minimal beta=%s" % (d, found))

note("FINDINGS: %d" % len(FINDINGS))
for f in FINDINGS:
    note("  " + f)
note("breaker done")
