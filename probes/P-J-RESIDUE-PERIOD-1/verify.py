#!/usr/bin/env python3
"""P-J-RESIDUE-PERIOD-1 exact audit.

Standard library only. Integer arithmetic only. No float appears in any
assertion or in any printed field. Deterministic output, final digest line.

Audited statements, all carried by the written proofs in PREREG.md:

  (A) ord_m(zeta_5) = 5 for every rational integer m >= 2
  (B) ord_m(J) = lcm(5, ord_m(phi)) for every rational integer m >= 2
  (C) in any quotient in which zeta_5 has order exactly 5,
      lcm(5, ord(phi)) / ord(J) divides 5, and the value 5 is attained,
      so (B) does not extend to a single prime ideal above a split prime
"""

import hashlib
from math import gcd, isqrt

MMIN, MMAX = 2, 1000
CENSUS = (2, 3, 4, 5, 7, 11)
PMAX = 4000

# multiplication matrices on Z[zeta_5] in the basis (1, zeta, zeta^2, zeta^3)
MJ = ((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1))
MZ = ((0, 0, 0, -1), (1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1))
I4 = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))


def mul(A, B, m=None):
    if m is None:
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4))
                           for j in range(4)) for i in range(4))
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) % m
                       for j in range(4)) for i in range(4))


def mpow(A, e, m):
    R = tuple(tuple(x % m for x in row) for row in I4)
    B = tuple(tuple(x % m for x in row) for row in A)
    while e:
        if e & 1:
            R = mul(R, B, m)
        B = mul(B, B, m)
        e >>= 1
    return R


def mvec(A, v, m=None):
    r = [sum(A[i][k] * v[k] for k in range(4)) for i in range(4)]
    return tuple(x % m for x in r) if m is not None else tuple(r)


def det4(A):
    def det(M):
        n = len(M)
        if n == 1:
            return M[0][0]
        total = 0
        for j in range(n):
            sub = [[M[r][c] for c in range(n) if c != j] for r in range(1, n)]
            total += (-1) ** j * M[0][j] * det(sub)
        return total
    return det([list(r) for r in A])


def charpoly(A):
    n, c, Mk = 4, [1], [[0] * 4 for _ in range(4)]
    for k in range(1, n + 1):
        AM = [[sum(A[i][t] * Mk[t][j] for t in range(n)) for j in range(n)]
              for i in range(n)]
        for i in range(n):
            AM[i][i] += c[-1]
        Mk = AM
        AMk = [[sum(A[i][t] * Mk[t][j] for t in range(n)) for j in range(n)]
               for i in range(n)]
        tr = sum(AMk[i][i] for i in range(n))
        if tr % k:
            raise AssertionError("charpoly division")
        c.append(-tr // k)
    return tuple(c)


def divisors(n):
    ds, d = [], 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
        d += 1
    return sorted(ds)


def lcm(a, b):
    return a * b // gcd(a, b)


def pisano(m):
    """ord_m(phi). phi^n = F_n phi + F_(n-1), so phi^n = 1 exactly when
    F_n = 0 and F_(n-1) = 1 mod m, the Pisano period. The bound pi(m) <= 6m
    is a theorem, so this loop is exhaustive and never a truncated scan."""
    a, b, n = 0, 1, 0
    while n <= 6 * m:
        a, b = b, (a + b) % m
        n += 1
        if a == 0 and b == 1:
            return n
    raise AssertionError("pisano bound 6m exceeded at m=%d" % m)


def matrix_order(A, L, m):
    """The order as the least divisor of a verified multiple L. Returns None
    if A^L is not the identity, which fires the falsifier."""
    Im = tuple(tuple(x % m for x in row) for row in I4)
    if mpow(A, L, m) != Im:
        return None
    for d in divisors(L):
        if mpow(A, d, m) == Im:
            return d
    raise AssertionError("unreachable")


def census_orbits(m):
    counts = {}
    seen = bytearray(m ** 4)

    def idx(v):
        return ((v[0] * m + v[1]) * m + v[2]) * m + v[3]

    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    v = (a, b, c, d)
                    if seen[idx(v)]:
                        continue
                    ln, w = 0, v
                    while not seen[idx(w)]:
                        seen[idx(w)] = 1
                        w = mvec(MJ, w, m)
                        ln += 1
                    counts[ln] = counts.get(ln, 0) + 1
    return counts


def fp_order(x, p):
    n, y = 1, x % p
    while y != 1:
        y = y * x % p
        n += 1
        if n > p:
            raise AssertionError("order exceeded p")
    return n


def primes_1_mod_5(limit):
    out = []
    for p in range(7, limit):
        if p % 5 != 1:
            continue
        r = isqrt(p)
        if all(p % q for q in range(2, r + 1)):
            out.append(p)
    return out


rows = []
lines = []


def emit(s):
    lines.append(s)
    print(s)


emit("P-J-RESIDUE-PERIOD-1 exact audit")

# --- structural guards, before any order is computed
MZ2 = mul(MZ, MZ)
MZ3 = mul(MZ2, MZ)
PHI = tuple(tuple(-(MZ2[i][j] + MZ3[i][j]) for j in range(4)) for i in range(4))
g1 = mul(MJ, PHI) == MZ
g2 = det4(MJ) == 1
g3 = charpoly(MJ) == (1, -3, 4, -2, 1)
g4 = mul(mul(MZ2, MZ2), MZ) == I4
emit("G1 J . phi = zeta_5                        %s" % ("PASS" if g1 else "FAIL"))
emit("G2 det M_J = 1                             %s" % ("PASS" if g2 else "FAIL"))
emit("G3 char M_J = X^4-3X^3+4X^2-2X+1           %s" % ("PASS" if g3 else "FAIL"))
emit("G4 zeta_5^5 = I                            %s" % ("PASS" if g4 else "FAIL"))
guards_ok = g1 and g2 and g3 and g4
if not guards_ok:
    raise SystemExit(1)

# --- A and B: rational moduli
fired_a = fired_b = 0
for m in range(MMIN, MMAX + 1):
    Im = tuple(tuple(x % m for x in row) for row in I4)
    oz = 0
    for k in range(1, 6):
        if mpow(MZ, k, m) == Im:
            oz = k
            break
    d = pisano(m)
    L = lcm(5, d)
    oj = matrix_order(MJ, L, m)
    rows.append("A %d %d %d %s %d" % (m, oz, d, oj, L))
    if oz != 5:
        fired_a += 1
    if oj != L:
        fired_b += 1
emit("A  rational moduli %d..%d rows %d ord_zeta_firings %d period_law_firings %d"
     % (MMIN, MMAX, MMAX - MMIN + 1, fired_a, fired_b))

# --- census: independent route through exhaustive orbit enumeration
fired_c = 0
for m in CENSUS:
    cc = census_orbits(m)
    l = 1
    for x in sorted(cc):
        l = lcm(l, x)
    if l != lcm(5, pisano(m)):
        fired_c += 1
    rows.append("B %d %d %s" % (m, l, " ".join("%d:%d" % (x, cc[x]) for x in sorted(cc))))
emit("B  census moduli %s orbit_lcm_vs_period_firings %d"
     % (",".join(str(x) for x in CENSUS), fired_c))

# --- C: the collapse theorem at oriented places
ps = primes_1_mod_5(PMAX)
r1 = r5 = rother = 0
for p in ps:
    for z in range(2, p):
        if z == 1 or pow(z, 5, p) != 1:
            continue
        ph = (-(pow(z, 2, p) + pow(z, 3, p))) % p
        jj = (1 + pow(z, 2, p)) % p
        oz = fp_order(z, p)
        d = fp_order(ph, p)
        oj = fp_order(jj, p)
        L = lcm(5, d)
        if oz != 5 or L % oj:
            rother += 1
        elif L // oj == 1:
            r1 += 1
        elif L // oj == 5:
            r5 += 1
        else:
            rother += 1
        rows.append("C %d %d %d %d %d" % (p, z, d, oj, L))
emit("C  split primes below %d count %d prime ideals %d ratio_1 %d ratio_5 %d ratio_other %d"
     % (PMAX, len(ps), 4 * len(ps), r1, r5, rother))

# --- D: the smallest oriented witness, stated explicitly
wz = 3
wp = 11
wphi = (-(pow(wz, 2, wp) + pow(wz, 3, wp))) % wp
wj = (1 + pow(wz, 2, wp)) % wp
emit("D  oriented witness p %d zeta %d phi %d ord_phi %d ord_J %d lcm %d ratio %d"
     % (wp, wz, wphi, fp_order(wphi, wp), fp_order(wj, wp),
        lcm(5, fp_order(wphi, wp)), lcm(5, fp_order(wphi, wp)) // fp_order(wj, wp)))
rows.append("D %d %d %d %d" % (wp, wz, fp_order(wphi, wp), fp_order(wj, wp)))

# --- E: no finite orbit on the full lattice
v, sup = (1, 0, 0, 0), []
for _ in range(12):
    v = mvec(MJ, v)
    sup.append(max(abs(x) for x in v))
emit("E  lattice sup norms %s" % " ".join(str(x) for x in sup))
rows.append("E " + " ".join(str(x) for x in sup))

fired = fired_a + fired_b + fired_c + rother
if fired:
    emit("DECISION J-RESIDUE-PERIOD-FALSIFIED firings %d" % fired)
else:
    emit("DECISION J-RESIDUE-PERIOD-CONFIRMED")
emit("SCOPE L1 exact residue arithmetic only")
emit("digest %s" % hashlib.sha256("\n".join(rows).encode("ascii")).hexdigest())
raise SystemExit(1 if fired else 0)
