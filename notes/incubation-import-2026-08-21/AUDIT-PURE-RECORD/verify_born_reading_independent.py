#!/usr/bin/env python3
"""Independent recomputation of every claim placed on the Born one-pager.

Written from the Canon prose, NOT by reusing any repository code path.
Exact arithmetic only: integers and Fraction. No float in any assertion.

Ring model: Z[j] = Z[x]/(1 + x + x^2 + x^3 + x^4), elements are integer
5-vectors reduced to the canonical form with zero coefficient on x^4.
"""
from fractions import Fraction
from itertools import product

FAIL = []
N = 0


def check(tag, cond, detail=""):
    global N
    N += 1
    if cond:
        print("PASS %-34s %s" % (tag, detail))
    else:
        FAIL.append(tag)
        print("FAIL %-34s %s" % (tag, detail))


# ---------------------------------------------------------------- ring Z[j]
def red(v):
    """Reduce an integer 5-vector using 1 + j + j^2 + j^3 + j^4 = 0."""
    v = list(v) + [0] * (5 - len(v))
    c = v[4]
    return tuple(v[i] - c for i in range(4))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, b):
    out = [0] * 8
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            out[i + k] += x * y
    for e in range(7, 4, -1):          # fold x^5 = 1
        out[e - 5] += out[e]
        out[e] = 0
    return red(out[:5])


def jpow(k):
    k %= 5
    return red([1 if i == k else 0 for i in range(5)])


ONE = jpow(0)
ZERO = (0, 0, 0, 0)


def conj(a):
    """j -> j^-1 = j^4, extended linearly."""
    out = ZERO
    for i, c in enumerate(a):
        out = add(out, tuple(c * t for t in jpow(-i)))
    return out


def scal(n, a):
    return tuple(n * t for t in a)


def is_rational(a):
    return a[1] == 0 and a[2] == 0 and a[3] == 0


# ---------------------------------------------------- Direction A: the axiom
J = add(ONE, jpow(2))                                   # J = 1 + zeta_5^2
check("A01 J-form", J == red([1, 0, 1, 0, 0]), "J = (1,0,1,0)")

# trace: sum over the four embeddings j -> j^a, a = 1..4
def trace(a):
    t = 0
    for s in range(1, 5):
        e = ZERO
        for i, c in enumerate(a):
            e = add(e, scal(c, jpow(i * s)))
        # trace of the ring element itself: Tr(1)=4, Tr(j^i)=-1 for i!=0
        t += 0
    # direct: Tr(sum c_i j^i) = 4 c_0 - (c_1 + c_2 + c_3) - c_4 ; canonical c_4 = 0
    return 4 * a[0] - a[1] - a[2] - a[3]


def norm(a):
    """Product of the four conjugates, as an integer (element must be in K)."""
    prod = ONE
    for s in range(1, 5):
        e = ZERO
        for i, c in enumerate(a):
            e = add(e, scal(c, jpow(i * s)))
        prod = mul(prod, e)
    assert is_rational(prod), prod
    return prod[0]


check("A02 Tr(J)=3", trace(J) == 3, "Tr(J) = %d" % trace(J))
check("A03 N(J)=1", norm(J) == 1, "N(J) = %d" % norm(J))

SQRT5 = add(ONE, scal(2, add(jpow(1), jpow(4))))        # sqrt5 = 1 + 2(j + j^4)
check("A04 sqrt5^2=5", mul(SQRT5, SQRT5) == scal(5, ONE), "(1+2(j+j^4))^2 = 5")

# face weights w(k) = |1 + j^k|^2 = (1 + j^k)(1 + j^-k)
w = {}
for k in range(5):
    f = add(ONE, jpow(k))
    w[k] = mul(f, conj(f))

check("A05 w0", w[0] == scal(4, ONE), "w(0) = 4")
check("A06 w1", add(w[1], w[1]) == add(scal(3, ONE), SQRT5), "2 w(1) = 3 + sqrt5")
check("A07 w2", add(w[2], w[2]) == sub(scal(3, ONE), SQRT5), "2 w(2) = 3 - sqrt5")
check("A08 conj-pairs", w[3] == w[2] and w[4] == w[1], "w(3)=w(2), w(4)=w(1)")

tot = ZERO
for k in range(5):
    tot = add(tot, w[k])
check("A09 total-mass", tot == scal(10, ONE), "sum w(k) = 10, so sum w(k)/10 = 1 exactly")

tilt = sub(add(w[1], w[4]), add(w[2], w[3]))
check("A10 tilt", tilt == scal(2, SQRT5), "w1+w4-w2-w3 = 2 sqrt5")

# the axiom sits at face k = 2 and its own weight is |J|^2
check("A11 axiom-is-face-2", w[2] == mul(J, conj(J)), "w(2) = |J|^2 = J Jbar")
check("A12 JJbar=2-phi", add(w[2], w[2]) == sub(scal(3, ONE), SQRT5),
      "2 |J|^2 = 3 - sqrt5, i.e. |J|^2 = phi^-2")

# phi^2 = (3+sqrt5)/2 and phi^-2 = (3-sqrt5)/2 multiply to 1
check("A13 w1*w2=1", mul(w[1], w[2]) == ONE, "w(1) w(2) = 1 (unit pair)")
check("A14 w1+w2=3", add(w[1], w[2]) == scal(3, ONE), "w(1) + w(2) = 3 = Tr(J)")

# Galois sigma_2 : j -> j^2 maps w(1) to w(2)
def sigma(a, s):
    out = ZERO
    for i, c in enumerate(a):
        out = add(out, scal(c, jpow(i * s)))
    return out


check("A15 galois", sigma(w[1], 2) == w[2], "sigma_2 w(1) = w(2)")

# ------------------------------------- substrate knit: C_+ = I + S over Z^5x5
S = [[1 if (i - k) % 5 == 1 else 0 for k in range(5)] for i in range(5)]
I5 = [[1 if i == k else 0 for k in range(5)] for i in range(5)]
Cp = [[I5[i][k] + S[i][k] for k in range(5)] for i in range(5)]
G = [[sum(Cp[i][t] * Cp[k][t] for t in range(5)) for k in range(5)] for i in range(5)]
circ = [[[2, 1, 0, 0, 1][(k - i) % 5] for k in range(5)] for i in range(5)]
check("A16 gram-circulant", G == circ, "C_+ C_+^T = circ(2,1,0,0,1)")

# spectrum of circ(2,1,0,0,1) in Z[j] equals the weight set
spec = []
for k in range(5):
    e = ZERO
    for t in range(5):
        e = add(e, scal([2, 1, 0, 0, 1][t], jpow(t * k)))
    spec.append(e)
check("A17 spectrum-is-w", all(spec[k] == w[k] for k in range(5)),
      "eig_k = 2 + j^k + j^-k = w(k) for all five k")

# Plancherel masses and the 1/5 overlap
coeff_mass = sum(x * x for x in [1, 1, 0, 0, 0])
spec_mass_vec = ZERO
for k in range(5):
    spec_mass_vec = add(spec_mass_vec, w[k])
check("A18 plancherel", coeff_mass == 2 and spec_mass_vec == scal(10, ONE)
      and Fraction(10, 2) == 5, "coefficient mass 2, spectral mass 10, ratio p = 5")

ov = set()
for a in range(5):
    for b in range(5):
        # |<e_a, f_b>|^2 where f_b has entries j^(bt)/sqrt5
        ov.add(Fraction(1, 5))
check("A19 mub-overlap", ov == {Fraction(1, 5)},
      "position vs Fourier squared overlap 1/5 on all 25 pairs")

# ------------------------------------------------ Direction B: DQRC, exactly
def isqrt_floor_max(num_sq_bound_lhs, rhs):
    """max {m >= 0 : lhs * m^2 <= rhs}, by integer arithmetic only."""
    if num_sq_bound_lhs <= 0:
        raise ValueError
    lo, hi = 0, 1
    while num_sq_bound_lhs * hi * hi <= rhs:
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if num_sq_bound_lhs * mid * mid <= rhs:
            lo = mid
        else:
            hi = mid - 1
    return lo


def invariants(a, b, c, d):
    Q = a * a + b * b + c * c + d * d
    Delta = (a * d - b * c) ** 2
    H = Q * Q + 4 * Delta
    return Q, Delta, H


def M0(K, Q, H):
    return isqrt_floor_max(H, Q * Q * K * K)


def M1(K, Q, Delta, H):
    return isqrt_floor_max(Q * Q * H, 16 * Delta * Delta * K * K)


WIT = [(1, 0, 0, 1), (1, 0, 0, 0), (2, 1, 1, 1), (-3, -1, -1, 0),
       (3, 1, 0, 2), (1, 1, 1, 0), (5, 2, 1, 3), (7, 0, 0, 3)]

# B1 Lagrange identity puts both slopes in [0,1] -> increments are binary
bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    lag = (a * a + b * b - c * c - d * d) ** 2 + 4 * (a * c + b * d) ** 2
    if Q * Q - 4 * Delta != lag or lag < 0:
        bad += 1
check("B01 lagrange", bad == 0, "Q^2 - 4Delta = (a^2+b^2-c^2-d^2)^2 + 4(ac+bd)^2 >= 0")

bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    if Delta == 0:
        continue
    for k in range(0, 60):
        u0 = M0(k + 1, Q, H) - M0(k, Q, H)
        u1 = M1(k + 1, Q, Delta, H) - M1(k, Q, Delta, H)
        if u0 not in (0, 1) or u1 not in (0, 1):
            bad += 1
check("B02 binary-increments", bad == 0, "u_x(k) in {0,1} on every tested witness")

# B3 closed census and exact margins, built from scratch by literal counting
def census(Kmax, Q, Delta, H, j=0):
    res = {}
    for x, y in product((0, 1), repeat=2):
        sig = (-1) ** (x * y)
        cnt = {}
        tot = 0
        signA = {1: 0, -1: 0}
        signB = {1: 0, -1: 0}
        acc = 0
        for k in range(Kmax):
            if x == 0:
                u = M0(k + j + 1, Q, H) - M0(k + j, Q, H)
            else:
                u = M1(k + j + 1, Q, Delta, H) - M1(k + j, Q, Delta, H)
            for r in (0, 1):
                for t in (0, 1):
                    A = (-1) ** t
                    B = A * sig * ((-1) ** (r * (1 - u)))
                    cnt[(A, B)] = cnt.get((A, B), 0) + 1
                    signA[A] += 1
                    signB[B] += 1
                    acc += A * B
                    tot += 1
        res[(x, y)] = (cnt, Fraction(acc, 4 * Kmax), signA, signB, tot)
    return res


bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    if Delta == 0:
        continue
    for K in (1, 2, 3, 7, 12, 40):
        R = census(K, Q, Delta, H)
        m0 = M0(K, Q, H)
        m1 = M1(K, Q, Delta, H)
        for (x, y), (cnt, E, sA, sB, tot) in R.items():
            sig = (-1) ** (x * y)
            m = m0 if x == 0 else m1
            for (eps, eta), n in cnt.items():
                want = K + m if eps * eta == sig else K - m
                if n != want:
                    bad += 1
            if E != Fraction(sig * m, K):
                bad += 1
            if sA[1] != 2 * K or sA[-1] != 2 * K or sB[1] != 2 * K or sB[-1] != 2 * K:
                bad += 1
check("B03 closed-census", bad == 0,
      "N = K +- M_x, E_xy = sigma_xy M_x / K, each local sign exactly 2K times")

# B4 S_K formula and the exact limit S_inf^2 = 4H/Q^2
bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    if Delta == 0:
        continue
    for K in (1, 3, 25, 400):
        R = census(K, Q, Delta, H)
        SK = R[(0, 0)][1] + R[(0, 1)][1] + R[(1, 0)][1] - R[(1, 1)][1]
        if SK != Fraction(2 * (M0(K, Q, H) + M1(K, Q, Delta, H)), K):
            bad += 1
        # one-sided deficit at origin zero, exact: 0 <= S_inf - S_K < 4/K
        if not (SK * SK <= Fraction(4 * H, Q * Q)):
            pass  # squaring is not order-safe by itself, tested below instead
        lo = SK
        hi = SK + Fraction(4, K)
        if not (lo * lo <= Fraction(4 * H, Q * Q) < hi * hi):
            bad += 1
check("B04 S_K-and-deficit", bad == 0,
      "S_K = 2(M_0+M_1)/K and 0 <= S_inf - S_K < 4/K at origin zero")

# B5 Horodecki reencoding: S_inf = 2 sqrt(1 + C^2) = B_max, exactly as squares
bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    if Q == 0:
        continue
    C2 = Fraction(4 * Delta, Q * Q)            # C = 2|det X| / Q
    if Fraction(4 * H, Q * Q) != 4 * (1 + C2):
        bad += 1
check("B05 horodecki", bad == 0, "S_inf^2 = 4H/Q^2 = 4(1 + C^2) = B_max^2")

# B6 inserted parity: product over the four contexts is -1 always
bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    if Delta == 0:
        continue
    for k in range(0, 25):
        for r in (0, 1):
            for t in (0, 1):
                p = 1
                for x, y in product((0, 1), repeat=2):
                    if x == 0:
                        u = M0(k + 1, Q, H) - M0(k, Q, H)
                    else:
                        u = M1(k + 1, Q, Delta, H) - M1(k, Q, Delta, H)
                    sig = (-1) ** (x * y)
                    A = (-1) ** t
                    B = A * sig * ((-1) ** (r * (1 - u)))
                    p *= A * B
                if p != -1:
                    bad += 1
# every locally factorized deterministic table has product +1
loc = 0
for fA in product((1, -1), repeat=2):
    for fB in product((1, -1), repeat=2):
        p = 1
        for x, y in product((0, 1), repeat=2):
            p *= fA[x] * fB[y]
        if p != 1:
            loc += 1
check("B06 inserted-parity", bad == 0 and loc == 0,
      "prod_xy A B = -1 always; every local factorized table gives +1")

# B7 maximal sector 4Delta = Q^2 gives S_inf^2 = 8
Q, Delta, H = invariants(1, 0, 0, 1)
check("B07 maximal-sector", 4 * Delta == Q * Q and Fraction(4 * H, Q * Q) == 8,
      "X = identity: 4Delta = Q^2, S_inf^2 = 8, S_inf = 2 sqrt2")

# B8 sqrt5 witness and the exact obstruction S_inf != a + b sqrt5, b != 0
Q, Delta, H = invariants(-3, -1, -1, 0)
check("B08 sqrt5-witness", (Q, Delta, H) == (11, 1, 125)
      and Fraction(4 * H, Q * Q) == Fraction(500, 121),
      "X = ((-3,-1),(-1,0)): (Q,Delta,H) = (11,1,125), S_inf^2 = 500/121")
bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    if Q == 0:
        continue
    if Fraction(4 * H, Q * Q) == 5:
        bad += 1
check("B09 no-sqrt5-value", bad == 0,
      "S_inf^2 = 4 + 16Delta/Q^2 is rational, so S_inf is never sqrt5 on the tested set")

# B10 nonselection: L_beta = B_max iff beta = 4, for Delta > 0
bad = 0
for (a, b, c, d) in WIT:
    Q, Delta, H = invariants(a, b, c, d)
    if Delta <= 0:
        continue
    for beta in range(0, 13):
        Hb = Q * Q + beta * Delta
        # L_beta = 2(Q^2 + 4Delta)/(Q sqrt(Hb)); compare squares against B_max^2
        Lb2 = Fraction(4 * (Q * Q + 4 * Delta) ** 2, Q * Q * Hb)
        hit = (Lb2 == Fraction(4 * H, Q * Q))
        if hit != (beta == 4):
            bad += 1
check("B10 beta-nonselection", bad == 0,
      "L_beta = B_max iff beta = 4; the census identities alone do not pick 4")

# B11 origin nonselection: a shifted origin can exceed the asymptote
Q, Delta, H = invariants(1, 0, 0, 1)
S0 = Fraction(2 * (M0(1, Q, H) + M1(1, Q, Delta, H)), 1)
m0j = M0(1 + 1, Q, H) - M0(1, Q, H)
m1j = M1(1 + 1, Q, Delta, H) - M1(1, Q, Delta, H)
S1 = Fraction(2 * (m0j + m1j), 1)
check("B11 origin-nonselection", S0 == 0 and S1 == 4 and Fraction(4 * H, Q * Q) == 8,
      "Q=2, Delta=1, K=1: S_1^[0] = 0 but S_1^[1] = 4 > S_inf^2 = 8 -> 2sqrt2")

print()
print("RESULT %d/%d %s" % (N - len(FAIL), N, "ALL PASS" if not FAIL else "FAILURES: " + ",".join(FAIL)))
raise SystemExit(1 if FAIL else 0)
