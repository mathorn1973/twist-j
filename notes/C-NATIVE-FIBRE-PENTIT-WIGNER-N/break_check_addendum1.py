#!/usr/bin/env python3
# Breaker for ADDENDUM 1 of C-NATIVE-FIBRE-PENTIT-WIGNER-N. Written after the first pinned run.
# NON-CANONICAL, L1 only. Standard library, exact arithmetic, no float, no repository file.
# Independent path: line states are explicit vectors (basis vectors and quadratic-phase vectors),
# probabilities are inner products in the basis 1,z,z^2,z^3, the response comes from Weyl
# expectation values, outcomes of the point model are values of linear functionals, and
# signs in Q(sqrt5) are decided by rational brackets.
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <this file>
import itertools
import sys
from fractions import Fraction as Fr

RES = []


def check(cid, text, cond):
    RES.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + cid + " " + text)


def info(text):
    print("     " + text)


def zmul(a, b):
    c = [0] * 7
    for i in range(4):
        if a[i]:
            for j in range(4):
                c[i + j] += a[i] * b[j]
    c[0] += c[5]
    c[1] += c[6]
    return (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def zconj(a):
    return (a[0] - a[1], -a[1], a[3] - a[1], a[2] - a[1])


def zscal(n, a):
    return (n * a[0], n * a[1], n * a[2], n * a[3])


ZP = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (-1, -1, -1, -1)]
ZERO = (0, 0, 0, 0)
F2 = list(itertools.product(range(5), repeat=2))


def real_q5(a, den):
    assert a[1] == 0 and a[2] == a[3], "not real"
    return (Fr(2 * a[0] - a[2], 2 * den), Fr(-a[2], 2 * den))


def sgn(x, y):
    if y == 0:
        return (x > 0) - (x < 0)
    lo, hi = Fr(2), Fr(3)
    while True:
        a, b = x + y * lo, x + y * hi
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        mid = (lo + hi) / 2
        if mid * mid < 5:
            lo = mid
        else:
            hi = mid


def inner(v, w):
    # <v, w> = sum conj(v_k) w_k
    acc = ZERO
    for k in range(5):
        acc = zadd(acc, zmul(zconj(v[k]), w[k]))
    return acc


def wigner_support(psi, n2):
    # complex vector; W(u) = (1/(25 n2)) sum_v z^(r q' - q r') <psi|D_v|psi>
    chi = {}
    for (q, r) in F2:
        acc = ZERO
        for k in range(5):
            acc = zadd(acc, zmul(zconj(psi[(k + q) % 5]), zmul(ZP[(3 * q * r + r * k) % 5], psi[k])))
        chi[(q, r)] = acc
    W = {}
    for u in F2:
        acc = ZERO
        for v in F2:
            acc = zadd(acc, zmul(ZP[(u[1] * v[0] - u[0] * v[1]) % 5], chi[v]))
        W[u] = real_q5(acc, 25 * n2)
    return W


# ------------------------------------------------------------ the 30 line states as vectors
VECS = []
for k in range(5):
    VECS.append(([ZP[0] if j == k else ZERO for j in range(5)], 1))
for a in range(5):
    for b in range(5):
        VECS.append(([ZP[(a * j * j + b * j) % 5] for j in range(5)], 5))
LINE = []
ok = True
for psi, n2 in VECS:
    W = wigner_support(psi, n2)
    sup = frozenset(u for u in F2 if W[u] != (Fr(0), Fr(0)))
    ok &= len(sup) == 5 and all(W[u] == (Fr(1, 5), Fr(0)) for u in sup)
    LINE.append(sup)
check("V1", "the 5 basis vectors and 25 quadratic-phase vectors have Wigner function 1/5 on 30 distinct five-point sets",
      ok and len(set(LINE)) == 30)


def label(sup):
    # a five-point set is a line iff a nonzero linear functional is constant on it
    for dq, dr in [(0, 1)] + [(1, m) for m in range(5)]:
        vals = {(dr * u[0] - dq * u[1]) % 5 for u in sup}
        if len(vals) == 1:
            return ((dq, dr), next(iter(vals)))
    return None


LAB = [label(s) for s in LINE]
check("V2", "each support is an affine line: all 30 (direction, level) labels are present once", None not in LAB and len(set(LAB)) == 30)
IDX = {lab: i for i, lab in enumerate(LAB)}


def prob(i, j):
    a = inner(VECS[i][0], VECS[j][0])
    m = zmul(a, zconj(a))
    assert m[1:] == (0, 0, 0)
    return Fr(m[0], VECS[i][1] * VECS[j][1])


TR = [[prob(i, j) for j in range(30)] for i in range(30)]
check("V3", "|<v_L|v_M>|^2 = |L cap M|/5 for all 900 pairs of line vectors",
      all(TR[i][j] == Fr(len(LINE[i] & LINE[j]), 5) for i in range(30) for j in range(30)))

# ------------------------------------------------------------ B7 by inner products and Weyl route
LOW = [zscal(t, ZP[0]) for t in (4, -1, -1, -1, -1)]
plow = []
for psi, n2 in VECS:
    a = inner(LOW, psi)
    plow.append(real_q5(zmul(a, zconj(a)), 20 * n2))
ms = {}
for v in plow:
    ms[v] = ms.get(v, 0) + 1
expected = {(Fr(0), Fr(0)): 1, (Fr(1, 20), Fr(0)): 4, (Fr(3, 10), Fr(-1, 10)): 2, (Fr(7, 40), Fr(-1, 40)): 8,
            (Fr(7, 40), Fr(1, 40)): 8, (Fr(1, 4), Fr(0)): 4, (Fr(3, 10), Fr(1, 10)): 2, (Fr(4, 5), Fr(0)): 1}
fourier = IDX[((1, 0), [c for (d, c) in LAB if d == (1, 0)][0])]
f_idx = VECS.index(([ZP[j % 5] for j in range(5)], 5))
check("B7a", "LOW probabilities on the 30 line vectors by inner products equal the verifier's multiset; f gives 1/4 and lies in direction (1,0)",
      ms == expected and plow[f_idx] == (Fr(1, 4), Fr(0)) and LAB[f_idx][0] == (1, 0) and fourier is not None)
check("B7b", "exactly two line vectors have LOW probability a multiple of 1/5 (4/5 and 0)",
      sorted(v[0] for v in plow if v[1] == 0 and (5 * v[0]).denominator == 1) == [Fr(0), Fr(4, 5)])
WL = wigner_support(LOW, 20)
resp = {u: (5 * WL[u][0], 5 * WL[u][1]) for u in F2}
rm = {}
for v in resp.values():
    rm[v] = rm.get(v, 0) + 1
check("B7c", "Weyl-route LOW response: 1 x1, 3/4 x4, -1/4 x4, (1+sqrt5)/8 x8, (1-sqrt5)/8 x8, twelve negative",
      rm == {(Fr(1), Fr(0)): 1, (Fr(3, 4), Fr(0)): 4, (Fr(-1, 4), Fr(0)): 4, (Fr(1, 8), Fr(1, 8)): 8, (Fr(1, 8), Fr(-1, 8)): 8}
      and sum(1 for v in resp.values() if sgn(*v) < 0) == 12)
dual = True
T = (sum(5 * plow[i][0] for i in range(30) if LAB[i][0] == (0, 1)), sum(5 * plow[i][1] for i in range(30) if LAB[i][0] == (0, 1)))
for u in F2:
    sx = sum(5 * plow[i][0] for i in range(30) if u in LINE[i])
    sy = sum(5 * plow[i][1] for i in range(30) if u in LINE[i])
    dual &= ((sx - T[0]) / 5, (sy - T[1]) / 5) == resp[u]
check("B7d", "dual inversion from the inner-product probabilities returns the Weyl-route response at all 25 points", dual and T == (Fr(5), Fr(0)))
plus = [ZP[0]] * 5
acc_ok = True
for u in F2:
    Wp = wigner_support(plus, 5)[u]
    acc_ok &= (1 - 5 * Wp[0], -5 * Wp[1]) == ((Fr(1), Fr(0)) if u[1] else (Fr(0), Fr(0)))
check("B7e", "acceptance response 1 - 5 W_plus(u) is the indicator of the complement of the line r=0", acc_ok)

# ------------------------------------------------------------ B8 point model with explicit microstates
DIRS = [(0, 1)] + [(1, m) for m in range(5)]


def level(d, u):
    return (d[1] * u[0] - d[0] * u[1]) % 5


def run_two(update):
    # returns True iff the counted two-round law equals the vector law in all 1080 scenarios
    for i in range(30):
        for d1 in DIRS:
            for d2 in DIRS:
                cnt = {}
                tot = 0
                for u in LINE[i]:
                    for u1 in update(u, d1):
                        for u2 in update(u1, d2):
                            key = (level(d1, u), level(d2, u1))
                            cnt[key] = cnt.get(key, 0) + 1
                            tot += 1
                for c1 in range(5):
                    for c2 in range(5):
                        m1, m2 = IDX[(d1, c1)], IDX[(d2, c2)]
                        if Fr(cnt.get((c1, c2), 0), tot) != TR[i][m1] * TR[m1][m2]:
                            return False
    return True


def U1(u, d):
    return [((u[0] + t * d[0]) % 5, (u[1] + t * d[1]) % 5) for t in range(5)]


def U0(u, d):
    return [u]


check("B8a", "U1 reproduces the two-round vector law in all 1080 scenarios; U0 does not", run_two(U1) and not run_two(U0))
three = True
for i in range(30):
    for d1 in DIRS:
        for d2 in DIRS:
            if d1 == d2:
                continue
            back = 0
            for u in LINE[i]:
                for u1 in U1(u, d1):
                    for u2 in U1(u1, d2):
                        back += level(d1, u2) == level(d1, u)
            q = sum(TR[i][IDX[(d1, c1)]] * TR[IDX[(d1, c1)]][IDX[(d2, c2)]] * TR[IDX[(d2, c2)]][IDX[(d1, c1)]]
                    for c1 in range(5) for c2 in range(5))
            three &= Fr(back, 125) == q == Fr(1, 5)
check("B8b", "three rounds d1,d2,d1 with d1 != d2: U1 returns the first outcome with weight 1/5, equal to the vector law, in all 900 scenarios", three)

# counterexample searches: deterministic updates without a fresh coordinate
native = [(s, t) for s in (1, 4) for t in F2]
hits = 0
for s, t in native:
    hits += run_two(lambda u, d, s=s, t=t: [((s * u[0] + t[0]) % 5, (s * u[1] + t[1]) % 5)])
info("S1 native fibre maps tested as a fixed update: " + str(len(native)) + ", reproducing the two-round law: " + str(hits))
hits2 = 0
n2 = 0
for h in itertools.product(range(5), repeat=5):
    n2 += 1
    hits2 += run_two(lambda u, d, h=h: [((u[0] + h[level(d, u)] * d[0]) % 5, (u[1] + h[level(d, u)] * d[1]) % 5)])
info("S2 outcome-indexed shifts along the reading direction tested: " + str(n2) + ", reproducing the two-round law: " + str(hits2))
check("S", "no deterministic update of the point alone, among the 50 native fibre maps and the 3125 outcome-indexed shifts, reproduces the two-round law",
      hits == 0 and hits2 == 0)

print("SUMMARY %d of %d checks PASS" % (sum(RES), len(RES)))
sys.exit(0 if all(RES) else 1)
