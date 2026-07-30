#!/usr/bin/env python3
# C-METAL-TRACE-1_verifier.py
# Candidate C-METAL-TRACE-1: the metallic-trace cascade.
# Target line on promotion: Public Canon v10 (mathorn1973/twist-j), section 4, The two places.
# Status of claim: candidate-T (exact algebraic identities). The run/record physical
#   reading is NOT asserted here; it is carried separately as H and is not promoted.
# Action layer: L2 (manifold / field arithmetic).
# Rules: Python standard library only. Exact arithmetic (Fraction / integer cyclotomic).
#   No floats in any assertion. Run from repo root with
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
# Provenance: formalizes the prior exploration verify_metals_deep.py (same 19 assertions).

from fractions import Fraction as Fr
checks = []
def ck(name, cond): checks.append((name, bool(cond)))

# ---------- gold field Q(sqrt5): pairs (a,b) = a + b*sqrt5
def m5(u, v):
    a, b = u; c, d = v; return (a*c + 5*b*d, a*d + b*c)
def add5(u, v): return (u[0]+v[0], u[1]+v[1])
def sc5(k, u):  return (k*u[0], k*u[1])
def cj5(u):     return (u[0], -u[1])
ONE5 = (Fr(1), Fr(0)); PHI = (Fr(1, 2), Fr(1, 2))          # phi = (1 + sqrt5)/2
ck("gold law: phi^2 = phi + 1        (trace 1)", m5(PHI, PHI) == add5(PHI, ONE5))
ck("gold: N(phi) = phi*phi' = -1     (unit)",    m5(PHI, cj5(PHI)) == (Fr(-1), Fr(0)))
ck("gold: Tr(phi) = phi + phi' = 1   (middle coefficient is the trace)",
   add5(PHI, cj5(PHI)) == (Fr(1), Fr(0)))

# ---------- silver field Q(sqrt2): pairs (a,b) = a + b*sqrt2
def m2(u, v):
    a, b = u; c, d = v; return (a*c + 2*b*d, a*d + b*c)
def add2(u, v): return (u[0]+v[0], u[1]+v[1])
def sc2(k, u):  return (k*u[0], k*u[1])
def cj2(u):     return (u[0], -u[1])
ONE2 = (Fr(1), Fr(0)); DELTA = (Fr(1), Fr(1))              # delta = 1 + sqrt2
ck("silver law: delta^2 = 2*delta + 1 (trace 2)",
   m2(DELTA, DELTA) == add2(add2(DELTA, DELTA), ONE2))
ck("silver: N(delta) = -1            (unit)", m2(DELTA, cj2(DELTA)) == (Fr(-1), Fr(0)))
ck("silver: Tr(delta) = 2            (middle coefficient is the trace)",
   add2(DELTA, cj2(DELTA)) == (Fr(2), Fr(0)))

# ---------- trace -> discriminant -> ramified prime.  x^2 - t x - 1 has disc = t^2 + 4
ck("trace 1 -> disc = 1 + 4 = 5  -> Q(sqrt5) -> prime 5", 1*1 + 4 == 5)
ck("trace 2 -> disc = 4 + 4 = 8  -> Q(sqrt2) -> prime 2", 2*2 + 4 == 8)
ck("gold prime divides its disc:   5 | 5", 5 % 5 == 0)
ck("silver prime divides its disc: 2 | 8", 8 % 2 == 0)

# ---------- growth laws: Fibonacci (trace 1) vs Pell (trace 2), verified to n = 11
F = [0, 1]; P = [0, 1]
for _ in range(12):
    F.append(F[-1] + F[-2])          # gold
    P.append(2*P[-1] + P[-2])        # silver
gp = ONE5; okg = True
for n in range(1, 12):
    gp = m5(gp, PHI)
    if gp != add5(sc5(Fr(F[n]), PHI), (Fr(F[n-1]), Fr(0))): okg = False
ck("gold growth is Fibonacci:  phi^n = F_n * phi + F_(n-1)  [n <= 11]", okg)
dp = ONE2; oks = True
for n in range(1, 12):
    dp = m2(dp, DELTA)
    if dp != add2(sc2(Fr(P[n]), DELTA), (Fr(P[n-1]), Fr(0))): oks = False
ck("silver growth is Pell:     delta^n = P_n * delta + P_(n-1)  [n <= 11]", oks)

# ---------- Z[zeta_8]: (a,b,c,d) = a + b m + c m^2 + d m^3, m^4 = -1
def mul8(u, v):
    d = [0]*4
    for i in range(4):
        for k in range(4):
            q, r = divmod(i + k, 4); d[r] += u[i]*v[k]*((-1)**q)
    return tuple(d)
def gal8(u, k):
    d = [0]*4
    for i in range(4):
        q, r = divmod(i*k, 4); d[r] += u[i]*((-1)**q)
    return tuple(d)
ONE8 = (1, 0, 0, 0); M = (0, 1, 0, 0)
SQRT2 = (0, 1, 0, -1)      # m - m^3 = m + m^-1
PEN   = (1, 0, 1, 0)       # 1 + m^2 = 1 + i, the silver pure form (the pen)
ck("silver phase atom:     m^2 = i", mul8(M, M) == (0, 0, 1, 0))
ck("silver amplitude atom: (m + m^-1)^2 = 2  so m + m^-1 = sqrt2", mul8(SQRT2, SQRT2) == (2, 0, 0, 0))
ck("Hadamard coefficient:  m + m^-1 = sqrt2  (1/sqrt2 undoes one write)", SQRT2 == (0, 1, 0, -1))
ck("sqrt(2i) squared:      (1 + i)^2 = 2i", mul8(PEN, PEN) == (0, 0, 2, 0))
ck("sqrt(2i) factored:     sqrt2 * m = 1 + i   (amplitude sqrt2, phase pi/4)", mul8(SQRT2, M) == PEN)
np = ONE8
for k in (1, 3, 5, 7): np = mul8(np, gal8(PEN, k))
ck("silver pure form NOT a unit: N(1 + i) = 4 over Q(zeta_8)", np == (4, 0, 0, 0))

# ---------- gold pure form J = 1 + j^2 IS a unit, N(J) = 1  (contrast with the pen)
def red5c(pairs):
    d = [0]*5
    for e, v in pairs: d[e % 5] += v
    a4 = d[4]; return (d[0]-a4, d[1]-a4, d[2]-a4, d[3]-a4)
def mul5c(u, v): return red5c([(i+k, u[i]*v[k]) for i in range(4) for k in range(4)])
def gal5c(u, k): return red5c([(i*k, u[i]) for i in range(4)])
J5 = (1, 0, 1, 0); ONEZ5 = (1, 0, 0, 0); nJ = ONEZ5
for k in (1, 2, 3, 4): nJ = mul5c(nJ, gal5c(J5, k))
ck("gold pure form IS a unit: N(J = 1 + j^2) = 1", nJ == ONEZ5)

ok = all(r for _, r in checks)
for n, r in checks: print(("OK   " if r else "FAIL ") + n)
print(("ALL OK, %d checks" % len(checks)) if ok else "SOME FAILED")
raise SystemExit(0 if ok else 1)
