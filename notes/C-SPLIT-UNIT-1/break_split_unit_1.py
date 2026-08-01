#!/usr/bin/env python3
# break_split_unit_1.py
# Candidate C-SPLIT-UNIT-1, the break attempt. NON-CANONICAL, no authority.
# Independent code paths: Faddeev-LeVerrier characteristic polynomial,
# Sylvester resultants, brute-force sign-map enumeration, direct membership
# of scanned units in {+-zeta^k phi^m}. Plus constructed counterexample
# attempts. Exact arithmetic only, no float anywhere in this file.
# Run: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
#      python3 break_split_unit_1.py
import sys
from fractions import Fraction as F
from itertools import product as iproduct

PASS = 0
FAIL = 0


def gate(gid, text, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("PASS %s %s" % (gid, text))
    else:
        FAIL += 1
        print("FAIL %s %s" % (gid, text))


# ---- shared exact ring layer (re-implemented, small, for self-containment) -
def red(c):
    c = list(c) + [0] * (8 - len(c))
    c[0] += c[5]
    c[1] += c[6]
    c[2] += c[7]
    q = c[4]
    return (c[0] - q, c[1] - q, c[2] - q, c[3] - q)


def zmul(a, b):
    c = [0] * 8
    for i in range(4):
        if a[i]:
            for j in range(4):
                c[i + j] += a[i] * b[j]
    return red(c)


def zadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def zneg(a):
    return tuple(-x for x in a)


ONE = (1, 0, 0, 0)
ZERO = (0, 0, 0, 0)


def zpow5(k):
    k %= 5
    if k < 4:
        t = [0, 0, 0, 0]
        t[k] = 1
        return tuple(t)
    return (-1, -1, -1, -1)


def sigma(a, x):
    acc = ZERO
    for k in range(4):
        if x[k]:
            acc = zadd(acc, tuple(x[k] * t for t in zpow5(a * k)))
    return acc


def norm(x):
    p = ONE
    for a in (1, 2, 3, 4):
        p = zmul(p, sigma(a, x))
    if p[1] != 0 or p[2] != 0 or p[3] != 0:
        return None
    return p[0]


def qmul(p, q):
    a, b = p
    c, d = q
    return (a * c + b * d, a * d + b * c + b * d)


def qpow(n):
    r = (1, 0)
    step = (0, 1) if n >= 0 else (-1, 1)
    for _ in range(abs(n)):
        r = qmul(r, step)
    return r


J = (1, 0, 1, 0)
PHI = (0, 0, -1, -1)

print("C-SPLIT-UNIT-1 break attempt. Independent paths.")

# ---- K1. charpoly of multiplication by x0 = 2 + z^2 + z^3 -----------------
# Independent of the direct conjugate-product path. A wrong modulus pattern
# (for example phi, phi, phi, phi^-1) would change this polynomial.
x0 = (2, 0, 1, 1)
cols = []
for jdx in range(4):
    cols.append(zmul(x0, zpow5(jdx)))
M = [[F(cols[jdx][i]) for jdx in range(4)] for i in range(4)]


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]


def mat_sub_scalar(A, s):
    return [[A[i][j] - (s if i == j else 0) for j in range(4)]
            for i in range(4)]


def trace(A):
    return sum(A[i][i] for i in range(4))


# Faddeev-LeVerrier: p(x) = x^4 - c1 x^3 - c2 x^2 - c3 x - c4
Ak = [row[:] for row in M]
c1 = trace(Ak)
Ak = mat_mul(M, mat_sub_scalar(Ak, c1))
c2 = trace(Ak) / 2
Ak = mat_mul(M, mat_sub_scalar(Ak, c2))
c3 = trace(Ak) / 3
Ak = mat_mul(M, mat_sub_scalar(Ak, c3))
c4 = trace(Ak) / 4
gate("K1", "charpoly of mult by (2 + z^2 + z^3) is (x^2 - 3x + 1)^2 = "
     "x^4 - 6x^3 + 11x^2 - 6x + 1",
     (c1, c2, c3, c4) == (F(6), F(-11), F(6), F(-1)))

# ---- K2. norms of 1 + w by Sylvester resultant ----------------------------
PHI5 = [1, 1, 1, 1, 1]  # x^4 + x^3 + x^2 + x + 1, low degree first


def deg(p):
    d = len(p) - 1
    while d >= 0 and p[d] == 0:
        d -= 1
    return d


def resultant(p, q):
    m = deg(p)
    n = deg(q)
    if n < 0:
        return 0
    if n == 0:
        return q[0] ** m
    size = m + n
    S = [[F(0)] * size for _ in range(size)]
    prev = list(reversed(p[: m + 1]))
    qrev = list(reversed(q[: n + 1]))
    for i in range(n):
        for k, cf in enumerate(prev):
            S[i][i + k] = F(cf)
    for i in range(m):
        for k, cf in enumerate(qrev):
            S[n + i][i + k] = F(cf)
    # determinant by fraction Gaussian elimination
    det = F(1)
    for col in range(size):
        piv = None
        for row in range(col, size):
            if S[row][col] != 0:
                piv = row
                break
        if piv is None:
            return 0
        if piv != col:
            S[col], S[piv] = S[piv], S[col]
            det = -det
        det *= S[col][col]
        inv = 1 / S[col][col]
        for row in range(col + 1, size):
            if S[row][col] != 0:
                f = S[row][col] * inv
                for cc in range(col, size):
                    S[row][cc] -= f * S[col][cc]
    return det


gate("K2a", "resultant calibration: Res(Phi5, x) = 1, Res(Phi5, 1 - x) = 5, "
     "Res(Phi5, 2) = 16",
     resultant(PHI5, [0, 1]) == 1 and resultant(PHI5, [1, -1]) == 5
     and resultant(PHI5, [2]) == 16)
res_ok = True
for k in range(1, 5):
    fplus = [0] * 5
    fplus[0] = 1
    fplus[k] += 1          # 1 + x^k
    fminus = [0] * 5
    fminus[0] = 1
    fminus[k] -= 1         # 1 - x^k
    res_ok = res_ok and resultant(PHI5, fplus) == 1
    res_ok = res_ok and resultant(PHI5, fminus) == 5
gate("K2b", "second path: N(1 + zeta^k) = 1 and N(1 - zeta^k) = 5 for all k, "
     "so the only 1 + torsion units are the four conjugates of J", res_ok)

# ---- K3. all +-1-valued maps on (Z/5)^x: exactly two homomorphisms --------
Gset = (1, 2, 3, 4)
homs = []
for vals in iproduct((1, -1), repeat=4):
    f = dict(zip(Gset, vals))
    if all(f[(x * y) % 5] == f[x] * f[y] for x in Gset for y in Gset):
        homs.append(tuple(f[a] for a in Gset))
gate("K3", "brute force over 16 sign maps: exactly the trivial map and "
     "chi5 = (+, -, -, +) are multiplicative",
     sorted(homs) == sorted([(1, 1, 1, 1), (1, -1, -1, 1)]))
gate("K3b", "constructed counterexample: the partition map (+, +, -, -) "
     "is not multiplicative", (1, 1, -1, -1) not in homs)
gate("K3c", "direct attempts at a second index-2 subgroup fail: {1,2}, "
     "{1,3}, {1,2,3} are not closed",
     (2 * 2) % 5 not in {1, 2} and (3 * 3) % 5 not in {1, 3}
     and (2 * 2) % 5 not in {1, 2, 3})

# ---- K4. membership: every unit in [-2,2]^4 is +-zeta^k phi^m -------------
members = set()
for k in range(5):
    for sgn in (1, -1):
        base = zpow5(k) if sgn == 1 else zneg(zpow5(k))
        for m in range(-30, 31):
            pr = qpow(m)
            el = zmul(base, (pr[0], 0, -pr[1], -pr[1]))
            members.add(el)
count = 0
outside = 0
for co in iproduct(range(-2, 3), repeat=4):
    if co == ZERO:
        continue
    if norm(co) in (1, -1):
        count += 1
        if co not in members:
            outside += 1
gate("K4", "every unit with coefficients in [-2,2]^4 equals +-zeta^k phi^m "
     "(found %d, outside 0 expected)" % count,
     outside == 0 and count >= 10)

# ---- K5. attempt to move J off the minimal quantum ------------------------
# If some unit of the J orbit had an even smaller nonzero size, the lattice
# claim would break. The orbit sizes are exactly {phi^-1 twice, phi twice}.
sizes = []
for a in (1, 2, 3, 4):
    u = sigma(a, J)
    x = zmul(u, sigma(4, u))
    sizes.append((x[0], -x[2]))
gate("K5", "orbit size data are exactly {phi^-2 twice, phi^2 twice}: "
     "quantum |m| = 1 across the whole orbit",
     sorted(sizes) == sorted([qpow(-2), qpow(-2), qpow(2), qpow(2)]))

print("GATES %d PASS %d FAIL %d" % (PASS + FAIL, PASS, FAIL))
print("RESULT: %s" % ("ALL PASS" if FAIL == 0 else "FAILURES PRESENT"))
sys.exit(0 if FAIL == 0 else 1)
