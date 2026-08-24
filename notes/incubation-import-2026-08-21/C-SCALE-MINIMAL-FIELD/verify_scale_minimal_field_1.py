#!/usr/bin/env python3
# C-SCALE-MINIMAL-FIELD-1  verifier
# Standard library only. Integers and Fractions only. No float in any assertion.
import sys, itertools
from fractions import Fraction as Fr

FIND = []; NG = [0, 0]
def rep(tag, broken, note=""):
    NG[1] += 1
    if broken: FIND.append(tag); print("%-56s FIRED %s" % (tag, note))
    else: NG[0] += 1; print("%-56s HOLDS %s" % (tag, note))

print("C-SCALE-MINIMAL-FIELD-1   exact integers and Fractions, no float")
print("prereg sha256 bc1ce96f63dd9086d3b090ffcda1ea881687a4508fcec13467fb64a51a570d77")
print()

# ---------------------------------------------------------------- S0 (a preregistered NEGATIVE)
# ANF / Zhegalkin: {1, XOR, AND} is functionally complete, so it selects nothing.
def anf_bijection(n):
    subsets = list(itertools.chain.from_iterable(
        itertools.combinations(range(n), k) for k in range(n + 1)))
    pts = list(itertools.product((0, 1), repeat=n))
    seen = set()
    for coef in itertools.product((0, 1), repeat=len(subsets)):
        tt = []
        for p in pts:
            v = 0
            for aS, S in zip(coef, subsets):
                if aS:
                    t = 1
                    for i in S: t &= p[i]
                    v ^= t
            tt.append(v)
        seen.add(tuple(tt))
    return len(seen) == 2 ** (2 ** n)
rep("S0a-ANF over {1,XOR,AND} realizes every f:{0,1}^n->{0,1}, n=1..3",
    not all(anf_bijection(n) for n in (1, 2, 3)),
    "counts 4, 16, 256 all attained")
rep("S0b-half adder: a + b = (a XOR b) + 2(a AND b)",
    any(av + bv != (av ^ bv) + 2 * (av & bv) for av in (0,1) for bv in (0,1)))
def ripple(u, v, bits):
    carry = 0; out = 0
    for k in range(bits):
        ak = (u >> k) & 1; bk = (v >> k) & 1
        s1 = ak ^ bk; c1 = ak & bk
        s2 = s1 ^ carry; c2 = s1 & carry
        carry = c1 | c2
        out |= s2 << k
    return out | (carry << bits)
rep("S0c-integer addition from XOR and AND alone, exhaustive 6-bit",
    any(ripple(u, v, 6) != u + v for u in range(64) for v in range(64)))
rep("S0d-PREREGISTERED NEGATIVE: Boolean completeness selects no prime", False,
    "universal representability has zero selection power. Stated as a defeat.")
print()

# ---------------------------------------------------------------- Minkowski, exact
PI_LO = Fr(314159, 100000)      # 3.14159 < pi
def fact(k):
    r = 1
    for i in range(2, k + 1): r *= i
    return r
def mink_sqrt_lower(m, r2):
    # sqrt|disc| >= (m^m / m!) (pi/4)^r2 ; smallest at r2 = m//2
    return Fr(m ** m, fact(m)) * (PI_LO / 4) ** r2
def mink_disc_lower(m):
    b = mink_sqrt_lower(m, m // 2)
    return (b * b)
B = {m: mink_disc_lower(m) for m in range(1, 61)}
mono = all(mink_sqrt_lower(m + 1, (m + 1) // 2) > mink_sqrt_lower(m, m // 2)
           for m in range(1, 60))
rep("M1-Minkowski lower bound is strictly increasing in degree, m=1..60",
    not mono, "B(3) >= %d, B(4) >= %d, B(6) >= %d" %
    (-(-B[3] // 1), -(-B[4] // 1), -(-B[6] // 1)))
ratio_ok = all((Fr(m + 1, m) ** m) * Fr(88, 100) > 1 for m in range(1, 200))
rep("M2-tail: (1+1/m)^m sqrt(pi/4) > 1.76 > 1 for every m, so B keeps growing",
    not (ratio_ok and Fr(88,100)**2 < PI_LO/4))
print()

# ---------------------------------------------------------------- S1
# quadratic fields: disc and unit rank
def squarefree(d):
    if d == 0: return False
    n = abs(d); k = 2
    while k * k <= n:
        if n % (k * k) == 0: return False
        k += 1
    return True
quad = []
for d in range(-200, 201):
    if d in (0, 1) or not squarefree(d): continue
    disc = d if d % 4 == 1 else 4 * d
    r1, r2 = (2, 0) if d > 0 else (0, 1)
    quad.append((d, disc, r1 + r2 - 1))
rank_ge1 = [(d, disc) for (d, disc, rk) in quad if rk >= 1]
best = min(abs(disc) for (_, disc) in rank_ge1)
who = [d for (d, disc) in rank_ge1 if abs(disc) == best]
rep("S1a-degree 2: minimal |disc| with unit rank >= 1 is 5, uniquely Q(sqrt5)",
    not (best == 5 and who == [5]), "minimizer d = %s, |disc| = %d" % (who, best))
rep("S1b-degree 1: Q has unit rank 0", not (1 + 0 - 1 == 0))
rep("S1c-imaginary quadratic always has unit rank 0",
    any(rk >= 1 for (d, _, rk) in quad if d < 0))
rep("S1d-every degree >= 3 has |disc| >= 13 > 5, so degree 2 is forced",
    not all(B[m] > 5 for m in range(3, 61)), "B(3) >= %d" % (-(-B[3] // 1)))
rep("S1-[candidate-T] Q(sqrt5) is THE minimal arithmetic home of a scale",
    not (best == 5 and who == [5] and all(B[m] > 5 for m in range(3, 61))),
    "|disc| = 5, fundamental unit phi = (1+sqrt5)/2")
print()

# ---------------------------------------------------------------- S2
def phi_euler(n):
    r = n; p = 2; m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0: m //= p
            r -= r // p
        p += 1
    if m > 1: r -= r // m
    return r
def primes_of(n):
    ps = []; m = n; p = 2
    while p * p <= m:
        if m % p == 0:
            ps.append(p)
            while m % p == 0: m //= p
        p += 1
    if m > 1: ps.append(m)
    return ps
def disc_cyclo(n):
    if n in (1, 2): return 1
    m = phi_euler(n)
    num = n ** m
    den = 1
    for p in primes_of(n): den *= p ** (m // (p - 1))
    assert num % den == 0
    return ((-1) ** (m // 2)) * (num // den)
def rank_cyclo(n):
    if n in (1, 2): return 0
    return phi_euler(n) // 2 - 1
cyc = []
for n in range(1, 201):
    if n % 4 == 2 and n > 2: continue        # Q(zeta_2m) = Q(zeta_m), m odd
    cyc.append((n, disc_cyclo(n), rank_cyclo(n), phi_euler(n)))
cr = [(n, dd) for (n, dd, rk, _) in cyc if rk >= 1]
bestc = min(abs(dd) for (_, dd) in cr)
whoc = [n for (n, dd) in cr if abs(dd) == bestc]
phi4 = sorted(n for n in range(1, 1000) if phi_euler(n) == 4)
rep("S2a-cyclotomic rank >= 1 iff phi(n) >= 4",
    any((rank_cyclo(n) >= 1) != (phi_euler(n) >= 4) for n in range(3, 201)))
rep("S2b-phi(n) = 4 has exactly n in {5,8,10,12}", phi4 != [5, 8, 10, 12],
    "discs %s" % [abs(disc_cyclo(n)) for n in phi4])
rep("S2c-degree >= 6 forces |disc| >= 985 > 125",
    not all(B[m] > 125 for m in range(6, 61)), "B(6) >= %d" % (-(-B[6] // 1)))
rep("S2-[candidate-T] Q(zeta_5) is the unique cyclotomic minimizer at 125",
    not (bestc == 125 and whoc == [5] and all(B[m] > 125 for m in range(6, 61))),
    "minimizer n = %s (n = 10 is the same field, excluded as a duplicate)" % whoc)
print()

# ---------------------------------------------------------------- S3 independent route
# discriminant of Z[zeta_n] as det of the trace form on the power basis
def ramanujan(n, k):
    # Tr_{Q(zeta_n)/Q}(zeta_n^k) = c_n(k) = mu(n/g) phi(n)/phi(n/g), g = gcd(n,k)
    from math import gcd
    g = gcd(n, k); q = n // g
    mu = 1; m = q; p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            mu = -mu
        p += 1
    if m > 1: mu = -mu
    assert phi_euler(n) % phi_euler(q) == 0
    return mu * (phi_euler(n) // phi_euler(q))
def det_int(M):
    M = [[Fr(v) for v in row] for row in M]
    n = len(M); det = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None: return 0
        if p != i: M[i], M[p] = M[p], M[i]; det = -det
        det *= M[i][i]
        inv = M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / inv
            if f: M[r] = [x - f * yv for x, yv in zip(M[r], M[i])]
    assert det.denominator == 1
    return int(det)
bad = []
for n in range(3, 25):
    if n % 4 == 2: continue
    m = phi_euler(n)
    G = [[ramanujan(n, i + j) for j in range(m)] for i in range(m)]
    if det_int(G) != disc_cyclo(n): bad.append(n)
rep("S3-trace-form route agrees with the conductor formula, n = 3..24",
    bool(bad), "mismatches: %s" % (bad or "none"))
rep("S3b-disc(Q(zeta_p)) = (-1)^((p-1)/2) p^(p-2) for odd primes p <= 31",
    any(disc_cyclo(p) != ((-1) ** ((p - 1) // 2)) * p ** (p - 2)
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)),
    "disc Q(zeta_5) = %d" % disc_cyclo(5))
print()

# ---------------------------------------------------------------- S4, stated as OPEN
# Z[zeta_5]: the four elements 1 + zeta^a . norms, traces, and which is a unit.
def mulz(u, v):            # multiply in Z[x]/(1+x+x^2+x^3+x^4), basis 1,z,z^2,z^3
    raw = [0] * 7
    for i, ui in enumerate(u):
        for j, vj in enumerate(v): raw[i + j] += ui * vj
    for k in range(6, 3, -1):
        c = raw[k]
        if c:
            raw[k] = 0
            for t in range(4): raw[(k - 4 + t) % 5 if False else t] -= 0
            # z^4 = -1-z-z^2-z^3 ; reduce degree k >= 4 by z^k = z^(k-4) * z^4
            sh = k - 4
            for t in range(4):
                idx = sh + t
                raw[idx] -= c
            # the above subtracts c*(z^sh + z^(sh+1) + z^(sh+2) + z^(sh+3))
    while len(raw) > 4 and raw[-1] == 0: raw.pop()
    return raw[:4] if len(raw) >= 4 else raw + [0] * (4 - len(raw))
def powz(u, k):
    r = [1, 0, 0, 0]
    for _ in range(k): r = mulz(r, u)
    return r
def normz(u):              # N = det of multiplication matrix
    cols = [mulz(u, [1 if t == j else 0 for t in range(4)]) for j in range(4)]
    M = [[cols[j][i] for j in range(4)] for i in range(4)]
    return det_int(M)
def tracez(u):
    cols = [mulz(u, [1 if t == j else 0 for t in range(4)]) for j in range(4)]
    return sum(cols[j][j] for j in range(4))
els = {}
for aexp in (1, 2, 3, 4):
    e = [0, 0, 0, 0]; e[aexp % 4] = 1
    if aexp == 4: e = [-1, -1, -1, -1]
    v = [1, 0, 0, 0]
    v = [v[t] + e[t] for t in range(4)]
    els[aexp] = (v, normz(v), tracez(v))
allunit = all(nn == 1 for (_, nn, _) in els.values())
alltr3  = all(tt == 3 for (_, _, tt) in els.values())
J = els[2][0]
tors = powz(J, 10) == [1, 0, 0, 0]
rep("S4a-all four 1 + zeta^a are units of norm 1 and trace 3", not (allunit and alltr3),
    "norm and trace do NOT separate them")
rep("S4b-J = 1 + zeta^2 is NOT torsion: J^10 != 1", tors,
    "J^10 = %s, so J has infinite order" % powz(J, 10))
rep("S4-[candidate-O] the FIELD is selected, the ELEMENT is not", False,
    "S1 and S2 stop at Q(zeta_5); nothing here picks 1+zeta^2 over 1+zeta")
print()
print("GATES %d of %d PASS" % (NG[0], NG[1]))
print("FINDINGS %d" % len(FIND))
if FIND: print("FIRED: " + ", ".join(FIND))
sys.exit(1 if FIND else 0)
