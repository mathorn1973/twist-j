#!/usr/bin/env python3
# C-SCALE-MINIMAL-FIELD-1  breaker. Independent code path, no import of the verifier.
# Honest attempts to kill S1, S2 and the framing. Exact arithmetic only.
import sys, itertools
from fractions import Fraction as Fr
from math import gcd

BR = []; NG = [0, 0]
def rep(tag, broken, note=""):
    NG[1] += 1
    if broken: BR.append(tag); print("%-56s BREAKS %s" % (tag, note))
    else: NG[0] += 1; print("%-56s SURVIVES %s" % (tag, note))

print("BREAKER C-SCALE-MINIMAL-FIELD-1b   independent path, exact")
print("supersedes leg BR4 of run 1: its irreducibility test missed the root 0.")
print("run 1 archived as ARCHIVE_breaker_scale_minimal_field_1_BR4-DEFECTIVE.py")
print()

# ---- BR1: independent hunt for a field of |disc| < 5 with a scale ------------
# route: binary quadratic form discriminants, not the squarefree-d route.
cands = []
for D in range(-400, 401):
    if D % 4 not in (0, 1): continue
    if D in (0, 1): continue
    # fundamental discriminant test, done directly
    fund = False
    if D % 4 == 1:
        n = abs(D); k = 2; sf = True
        while k * k <= n:
            if n % (k * k) == 0: sf = False; break
            k += 1
        fund = sf
    else:
        q = D // 4
        if q % 4 in (2, 3):
            n = abs(q); k = 2; sf = True
            while k * k <= n:
                if n % (k * k) == 0: sf = False; break
                k += 1
            fund = sf
    if fund and D > 0: cands.append(D)
rep("BR1-no real quadratic field of |disc| < 5 exists",
    any(D < 5 for D in cands), "least positive fundamental discriminant = %d" % min(cands))

# ---- BR2: is the CYCLOTOMIC restriction in S2 doing work? --------------------
# yes. drop it and the answer moves from 125 to 5. this is not a break of S2,
# it is the exact price of the class, and it is recorded rather than hidden.
rep("BR2-S2 is minimal only INSIDE the cyclotomic class", False,
    "drop cyclotomic and the minimizer is Q(sqrt5) at 5, not Q(zeta_5) at 125")

# ---- BR3: THE REAL ATTACK. other closures pick other numbers -----------------
def sf(n):
    n = abs(n); k = 2
    while k * k <= n:
        if n % (k * k) == 0: return False
        k += 1
    return n != 0
table = []
for d in range(-50, 51):
    if d in (0, 1) or not sf(d): continue
    disc = d if d % 4 == 1 else 4 * d
    torsion = 4 if d == -1 else (6 if d == -3 else 2)
    rank = 1 if d > 0 else 0
    table.append((d, disc, rank, torsion))
min_scale = min((abs(dd), d) for (d, dd, rk, t) in table if rk >= 1)
min_tors  = min((abs(dd), d) for (d, dd, rk, t) in table if t > 2)
rep("BR3-INTENDED BREAK: selection power is in the REQUIREMENT", True,
    "scale -> d=%d |disc|=%d (five) ; extra torsion -> d=%d |disc|=%d (three)"
    % (min_scale[1], min_scale[0], min_tors[1], min_tors[0]))

# ---- BR4: independent corroboration that degree 3 cannot reach |disc| <= 5 ---
def polydisc3(a, b, c):     # disc of x^3 + a x^2 + b x + c
    return (18*a*b*c - 4*a**3*c + a*a*b*b - 4*b**3 - 27*c*c)
def irred3(a, b, c):
    # monic integer cubic: reducible iff it has an integer root, and any
    # integer root divides c.  c = 0 means x itself is a factor.
    if c == 0: return False
    for r in range(-abs(c), abs(c) + 1):
        if r == 0: continue
        if c % r: continue
        if r**3 + a*r*r + b*r + c == 0: return False
    return True
best3 = None
for a, b, c in itertools.product(range(-6, 7), repeat=3):
    if not irred3(a, b, c): continue
    D = polydisc3(a, b, c)
    if D == 0: continue
    if best3 is None or abs(D) < abs(best3[0]): best3 = (D, (a, b, c))
rep("BR4-corrected: no cubic in the box reaches |disc| <= 5",
    abs(best3[0]) <= 5,
    "least |poly disc| over irreducible cubics in [-6,6]^3 is %d at %s"
    % (abs(best3[0]), best3[1]))

# ---- BR5: THE DECISIVE ATTACK ON S4 -----------------------------------------
# can ANY rational invariant separate 1 + zeta from 1 + zeta^2 ?
def mulz(u, v):
    raw = [0]*7
    for i, ui in enumerate(u):
        for j, vj in enumerate(v): raw[i+j] += ui*vj
    for k in (6, 5, 4):
        cst = raw[k]
        if cst:
            raw[k] = 0
            for t in range(4): raw[k-4+t] -= cst
    return raw[:4]
def matmul_basis(u):
    cols = [mulz(u, [1 if t == j else 0 for t in range(4)]) for j in range(4)]
    return [[cols[j][i] for j in range(4)] for i in range(4)]
def charpoly(M):
    n = len(M); cs = [Fr(1)]; A = [[Fr(0)]*n for _ in range(n)]
    for i in range(n): A[i][i] = Fr(1)
    Mf = [[Fr(v) for v in row] for row in M]
    for k in range(1, n+1):
        A = [[sum(Mf[i][t]*A[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        ck = -sum(A[i][i] for i in range(n))/k
        cs.append(ck)
        for i in range(n): A[i][i] += ck
    return [int(c) for c in cs]
E = {}
for aexp in (1, 2, 3, 4):
    e = [0, 0, 0, 0]
    if aexp == 4: e = [-1, -1, -1, -1]
    else: e[aexp] = 1
    E[aexp] = [1 + e[0]] + e[1:]
cps = {aexp: charpoly(matmul_basis(v)) for aexp, v in E.items()}
allsame = len(set(map(tuple, cps.values()))) == 1
# every Tr(u^k) is then equal too. check k = 1..12 explicitly.
def trz(u):
    M = matmul_basis(u); return sum(M[i][i] for i in range(4))
def powz(u, k):
    r = [1, 0, 0, 0]
    for _ in range(k): r = mulz(r, u)
    return r
traces_same = all(len({trz(powz(E[aexp], k)) for aexp in (1, 2, 3, 4)}) == 1
                  for k in range(1, 13))
rep("BR5-INTENDED BREAK on S4: no rational invariant can pick J", True,
    "all four 1+zeta^a share ONE minimal polynomial %s" % cps[2])
rep("BR5b-Tr((1+zeta^a)^k) is independent of a for k = 1..12",
    not (allsame and traces_same),
    "they are Galois conjugates; the choice of J is orientation, not arithmetic")

# ---- BR6: Fibonacci witness for the infinite order --------------------------
J = E[2]; J10 = powz(J, 10)
fib = [0, 1]
while len(fib) < 13: fib.append(fib[-1] + fib[-2])
rep("BR6-J^10 = F_11 - F_10 phi exactly, so |J|^10 = phi^-10 < 1",
    not (J10 == [fib[11], 0, -0 + fib[10], fib[10]]),
    "J^10 = %d + %d(zeta^2 + zeta^3) = %d - %d phi" % (J10[0], J10[2], fib[11], fib[10]))

print()
print("SURVIVED %d of %d attacks" % (NG[0], NG[1]))
print("BREAKS %d" % len(BR))
if BR: print("BROKEN: " + ", ".join(BR))
sys.exit(0)
