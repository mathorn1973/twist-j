#!/usr/bin/env python3
"""Exact checks for notes/J-WEIL-WEIGHT-AND-CARLITZ-RANK-2026-09-16.md.

NON-CANONICAL. Audit input only. Python standard library, exact integer
and Fraction arithmetic, no float in any assertion.

Part A: Galois moduli of the axiom data in Q(zeta_5).
Part B: Weil-weight classification (Gauss element weight 1, unitary factor
        weight 0, J not a Weil number).
Part C: Rank-one census of cyclotomic number fields (phi(n) = 4).
Part D: Rank-one census of Carlitz cyclotomic function fields
        K(Lambda_M) over F_q(t), by shape enumeration and by brute force.
"""
from fractions import Fraction as Fr
from itertools import product

# ---------------------------------------------------------------------------
# Z[zeta_5] as integer 4-vectors on the basis 1, z, z^2, z^3 with
# z^4 = -1 - z - z^2 - z^3.
# ---------------------------------------------------------------------------

def zmul(a, b):
    r = [0] * 7
    for i in range(4):
        for j in range(4):
            r[i + j] += a[i] * b[j]
    # reduce z^4, z^5, z^6
    for k in (6, 5, 4):
        c = r[k]
        if c:
            r[k] = 0
            for i in range(4):
                r[k - 4 + i] -= c
    return tuple(r[:4])


def zadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def zscale(c, a):
    return tuple(c * x for x in a)


def zpow_vec(k):
    """z^k as a vector."""
    v = (1, 0, 0, 0)
    z = (0, 1, 0, 0)
    for _ in range(k % 5):
        v = zmul(v, z)
    return v


def galois(a, b):
    """sigma_b : z -> z^b applied to vector a."""
    r = (0, 0, 0, 0)
    for i in range(4):
        r = zadd(r, zscale(a[i], zpow_vec(i * b)))
    return r


def conj(a):
    return galois(a, 4)


ONE = (1, 0, 0, 0)
Z = (0, 1, 0, 0)
J = zadd(ONE, zpow_vec(2))            # 1 + z^2
PHI = zscale(-1, zadd(zpow_vec(2), zpow_vec(3)))   # -z^2 - z^3
PHI_INV = zadd(zpow_vec(1), zpow_vec(4))            # z + z^4 = phi - 1
CHI = {1: 1, 2: -1, 3: -1, 4: 1}
GAMMA = (0, 0, 0, 0)
for a_ in range(1, 5):
    GAMMA = zadd(GAMMA, zscale(CHI[a_], zpow_vec(a_)))   # z - z^2 - z^3 + z^4

# Z[phi] as pairs (x, y) meaning x + y*phi, phi^2 = phi + 1, Fractions.

def pmul(u, v):
    x1, y1 = u
    x2, y2 = v
    return (x1 * x2 + y1 * y2, x1 * y2 + y1 * x2 + y1 * y2)


def real_of(a):
    """Element of Z[zeta_5] fixed by conjugation, returned in Z[phi].
    Uses z + z^4 = phi - 1 and z^2 + z^3 = -phi."""
    assert conj(a) == a, "not real"
    c0, c1, c2, c3 = a
    # a = c0 + c1 z + c2 z^2 + c3 z^3, real forces c1 = -c0' ... solve via
    # z^4 = -1 - z - z^2 - z^3: write with z^4 explicitly.
    # Real elements satisfy c1 = c(z^4) after rewriting; simplest: evaluate
    # both sigma_1 and sigma_4 symbolically through the pair (phi) map.
    # Map: 1 -> (1,0); z -> ?  Not in Z[phi]; use symmetric combination.
    # Since a is real, a = c0 + c1 (z + z^4) + c2 (z^2 + z^3) + (c3 - c2) z^3
    #   + (0 - c1) z^4 ... do it by linear algebra instead:
    # Express a on the basis z, z^2, z^3, z^4 (sum of basis = -1):
    d = [c1 - c0, c2 - c0, c3 - c0, -c0]   # coefficients on z, z^2, z^3, z^4
    assert d[0] == d[3] and d[1] == d[2], "not real on the symmetric basis"
    # a = d0 (z + z^4) + d1 (z^2 + z^3) = d0 (phi - 1) + d1 (-phi)
    return (Fr(-d[0]), Fr(d[0] - d[1]))


PHI_P = (Fr(0), Fr(1))
PHI_INV_P = (Fr(-1), Fr(1))
PHI2_P = pmul(PHI_P, PHI_P)
PHI_INV2_P = pmul(PHI_INV_P, PHI_INV_P)
FIVE_P = (Fr(5), Fr(0))
ONE_P = (Fr(1), Fr(0))

checks = []

def ck(name, ok):
    checks.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)


# ---------------- Part A: Galois moduli of J ----------------
print("== A. Galois moduli of J = 1 + zeta_5^2 in Z[zeta_5] ==")
ck("A1 J * conj(J) = phi^-2", real_of(zmul(J, conj(J))) == PHI_INV2_P)
ck("A2 phi * phi^-1 = 1", zmul(PHI, PHI_INV) == ONE)
okA3 = True
okA4 = True
for a in range(1, 5):
    sJ = galois(J, a)
    modsq = real_of(zmul(sJ, conj(sJ)))
    target = PHI_INV2_P if CHI[a] == 1 else PHI2_P
    okA3 &= (modsq == target)
    # sigma_a(J) = chi(a) * z^a * phi^(-chi(a))
    unit = PHI_INV if CHI[a] == 1 else PHI
    rhs = zscale(CHI[a], zmul(zpow_vec(a), unit))
    okA4 &= (sJ == rhs)
    print("   a=%d chi=%+d |sigma_a(J)|^2 = %s + %s phi" % (a, CHI[a], modsq[0], modsq[1]))
ck("A3 |sigma_a(J)|^2 = phi^(-2 chi_5(a)) for a = 1..4", okA3)
ck("A4 sigma_a(J) = chi_5(a) zeta^a phi^(-chi_5(a)) exactly", okA4)
ck("A5 the conjugate moduli take exactly two values", len({real_of(zmul(galois(J, a), conj(galois(J, a)))) for a in range(1, 5)}) == 2)

# ---------------- Part B: Weil weights ----------------
print("== B. Weil weights ==")
ck("B1 Gamma^2 = 5", zmul(GAMMA, GAMMA) == (5, 0, 0, 0))
okB2 = all(galois(GAMMA, b) == zscale(CHI[b], GAMMA) for b in range(1, 5))
ck("B2 sigma_b(Gamma) = chi_5(b) Gamma", okB2)
okB3 = all(real_of(zmul(galois(GAMMA, b), conj(galois(GAMMA, b)))) == FIVE_P for b in range(1, 5))
ck("B3 |sigma_b(Gamma)|^2 = 5 for all b (Weil 5-number, weight 1)", okB3)
# unitary factor on the character-a line: u_a = chi(a) z^a; modulus 1
okB4 = all(real_of(zmul(zscale(CHI[a], zpow_vec(a)), conj(zscale(CHI[a], zpow_vec(a))))) == ONE_P for a in range(1, 5))
ck("B4 unitary factor chi_5(a) zeta^a has modulus 1 on every line (weight 0)", okB4)
# J is a unit that is not a root of unity: J^10 != 1 (order would divide 10)
Jp = ONE
notroot = True
for k in range(1, 11):
    Jp = zmul(Jp, J)
    if Jp == ONE:
        notroot = False
ck("B5 N(J) = 1 and J^k != 1 for 1 <= k <= 10 (J is not a root of unity)", notroot and real_of(zmul(zmul(J, conj(J)), zmul(galois(J, 2), conj(galois(J, 2))))) == ONE_P)
ck("B6 J is not a Weil q-number of any weight: two conjugate moduli (A5)", okA3 and len({PHI_INV2_P, PHI2_P}) == 2)

# ---------------- Part C: number-field rank-one census ----------------
print("== C. Cyclotomic number fields with unit rank one ==")

def totient(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def is_prime_power(n):
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
        p += 1
    return n > 1


deg4 = [n for n in range(3, 10000) if totient(n) == 4]
ck("C1 phi(n) = 4 exactly for n in {5, 8, 10, 12}", deg4 == [5, 8, 10, 12])
pp = [n for n in deg4 if is_prime_power(n)]
ck("C2 prime-power conductors with unit rank one are exactly {5, 8}", pp == [5, 8])
ck("C3 unit rank of Q(zeta_n) = phi(n)/2 - 1 is 1 exactly when phi(n) = 4", all((totient(n) // 2 - 1 == 1) == (totient(n) == 4) for n in range(3, 10000)))
ck("C4 Q(zeta_40) = compositum of Q(zeta_5) and Q(zeta_8): degree 16, unit rank 7", totient(40) == 16 and totient(40) // 2 - 1 == 7)

# ---------------- Part D: Carlitz rank-one census ----------------
print("== D. Carlitz cyclotomic function fields K(Lambda_M) over F_q(t) ==")
# Import: the infinite place of F_q(t) splits in K(Lambda_M) into
# Phi(M)/(q-1) places (Hayes 1974; Rosen, Number Theory in Function Fields,
# ch. 12), so the S-unit rank of the integral closure of F_q[t] is
# Phi(M)/(q-1) - 1, with Phi(M) = |(F_q[t]/M)^x|.

def n_irr(q, d):
    # number of monic irreducibles of degree d over F_q (Gauss)
    def mob(n):
        r, m, p = 1, n, 2
        while p * p <= m:
            if m % p == 0:
                m //= p
                if m % p == 0:
                    return 0
                r = -r
            p += 1
        if m > 1:
            r = -r
        return r
    s = 0
    for k in range(1, d + 1):
        if d % k == 0:
            s += mob(d // k) * q ** k
    return s // d


def phi_shape(q, shape):
    r = 1
    for d, e in shape:
        r *= (q ** d - 1) * q ** (d * (e - 1))
    return r


hits = {}
for q in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25]:
    target = 2 * (q - 1)
    found = []
    # every prime-power factor contributes at least q - 1, so at most
    # log_(q-1)(2(q-1)) + 1 factors; degrees d with q^d - 1 <= target
    maxd = 1
    while q ** (maxd + 1) - 1 <= target:
        maxd += 1
    prims = [(d, e) for d in range(1, maxd + 1) for e in range(1, 4)]
    for k in range(1, 4):
        for shape in product(prims, repeat=k):
            if list(shape) != sorted(shape):
                continue
            ok = all(sum(1 for (d2, _) in shape if d2 == d) <= n_irr(q, d) for d in range(1, maxd + 1))
            if ok and phi_shape(q, shape) == target:
                found.append(shape)
    hits[q] = found
expected = {2: [((1, 2),), ((1, 1), (1, 2))], 3: [((1, 1), (1, 1))]}
okD1 = all((hits[q] == expected.get(q, [])) for q in hits)
ck("D1 shape census: rank one only for q=2 (P^2, P^2 Q) and q=3 (P Q); none for q >= 4", okD1)
for q in hits:
    print("   q=%d rank-one shapes (deg,exp): %s" % (q, hits[q]))

# Brute force over actual monic polynomials for prime q (independent path):
# Phi(M) = |(F_q[t]/M)^x| counted by gcd, no formula used.

def pdivmod(a, b, p):
    a = list(a)
    db = len(b) - 1
    while len(a) - 1 >= db and any(a):
        if a[-1] == 0:
            a.pop()
            continue
        c = (a[-1] * pow(b[-1], -1, p)) % p
        shift = len(a) - 1 - db
        for i in range(len(b)):
            a[shift + i] = (a[shift + i] - c * b[i]) % p
        while a and a[-1] == 0:
            a.pop()
    return a


def pgcd_is_one(a, b, p):
    a = [x % p for x in a]
    b = [x % p for x in b]
    while a and a[-1] == 0:
        a.pop()
    while b and b[-1] == 0:
        b.pop()
    while b:
        a, b = b, pdivmod(a, b, p)
    return len(a) == 1


def brute_rank_one(p, maxdeg):
    out = []
    for n in range(1, maxdeg + 1):
        for coeffs in product(range(p), repeat=n):
            M = list(coeffs) + [1]           # monic, degree n
            units = 0
            for m in range(p ** n):
                r = []
                x = m
                for _ in range(n):
                    r.append(x % p)
                    x //= p
                if pgcd_is_one(r, M, p):
                    units += 1
            if units == 2 * (p - 1):
                out.append(M)
    return out


B2 = brute_rank_one(2, 4)
B3 = brute_rank_one(3, 4)
B5 = brute_rank_one(5, 3)
B7 = brute_rank_one(7, 2)
# q = 2: t^2, (t+1)^2 = t^2+1, t^2(t+1) = t^3+t^2, t(t+1)^2 = t^3+t
ck("D2 brute force q=2, deg<=4: exactly [0,0,1], [1,0,1], [0,0,1,1], [0,1,0,1]", sorted(B2) == sorted([[0, 0, 1], [1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]]))
# q = 3: t(t+1) = t^2+t, t(t+2) = t^2+2t, (t+1)(t+2) = t^2+2 (mod 3: t^2+3t+2 = t^2+2)
ck("D3 brute force q=3, deg<=4: exactly t(t+1), t(t+2), (t+1)(t+2)", sorted(B3) == sorted([[0, 1, 1], [0, 2, 1], [2, 0, 1]]))
ck("D4 brute force q=5, deg<=3: no rank-one M", B5 == [])
ck("D5 brute force q=7, deg<=2: no rank-one M", B7 == [])
# degree bound closing D4 for all degrees: any M of degree >= 4 over F_5 has
# Phi(M) >= 4 * 5^3 ... not needed; the shape census D1 is complete for all
# degrees by the factor bound (each prime-power factor >= q - 1).
ck("D6 Phi(M) for q=5 and M=t, t^2, t^2+2 (irreducible), t(t+1): 4, 20, 24, 16 (none equals 8)",
   [phi_shape(5, s) for s in [((1, 1),), ((1, 2),), ((2, 1),), ((1, 1), (1, 1))]] == [4, 20, 24, 16])

print("== summary ==")
npass = sum(1 for _, ok in checks if ok)
print("%d/%d PASS" % (npass, len(checks)))
raise SystemExit(0 if npass == len(checks) else 1)
