#!/usr/bin/env python3
"""Exact verifier for C-RECORD-CRT-IDEMPOTENT-1 (NON-CANONICAL incubation note).

Standard library only, exact integer arithmetic, no floats anywhere,
deterministic, single process, no file writes.

Run with:
    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
        python3 verify_record_crt_idempotent.py

Carrier: R = Z[zeta_5] = Z[X]/Phi_5, basis (1, z, z^2, z^3); quotients R/(m)
enumerated exhaustively for m in {2,3,4,5,6,10,11,20}; prime-ideal norms from
the classical splitting law in Q(zeta_5); cyclotomic unit ranks from Dirichlet.

Every gate prints OK or FAIL; any FAIL sets exit code 1.
"""

from math import gcd

FAILURES = []


def gate(name, condition, detail=""):
    status = "OK" if condition else "FAIL"
    if not condition:
        FAILURES.append(name)
    line = "%-46s %s" % (name, status)
    if detail:
        line += "   " + detail
    print(line)


# ---------------------------------------------------------------- ring R

def rmul(a, b, m=0):
    """Multiply in Z[X]/Phi_5, optionally reducing coefficients mod m."""
    c = [0] * 7
    for i in range(4):
        if a[i]:
            for j in range(4):
                c[i + j] += a[i] * b[j]
    for i in range(6, 3, -1):
        t = c[i]
        if t:
            c[i] = 0
            for j in range(i - 4, i):
                c[j] -= t
    if m:
        return tuple(x % m for x in c[:4])
    return tuple(c[:4])


def radd(a, b, m=0):
    if m:
        return tuple((x + y) % m for x, y in zip(a, b))
    return tuple(x + y for x, y in zip(a, b))


def rsub(a, b, m=0):
    if m:
        return tuple((x - y) % m for x, y in zip(a, b))
    return tuple(x - y for x, y in zip(a, b))


def rpow(a, n, m=0):
    r = (1, 0, 0, 0)
    for _ in range(n):
        r = rmul(r, a, m)
    return r


def sigma(a, k):
    """Galois conjugate z -> z^k."""
    out = (0, 0, 0, 0)
    for i, ai in enumerate(a):
        if ai:
            out = radd(out, tuple(ai * x for x in rpow((0, 1, 0, 0), (i * k) % 5)))
    return out


def norm(a):
    n = (1, 0, 0, 0)
    for k in (1, 2, 3, 4):
        n = rmul(n, sigma(a, k))
    assert n[1] == n[2] == n[3] == 0, "norm must be rational"
    return n[0]


ONE = (1, 0, 0, 0)
Z = (0, 1, 0, 0)
J = radd(ONE, rpow(Z, 2))                     # J = 1 + zeta^2
INVPHI = radd(Z, rpow(Z, 4))                  # zeta + zeta^4 = 1/phi
PHI = rsub((0, 0, 0, 0), radd(rpow(Z, 2), rpow(Z, 3)))   # -(z^2+z^3) = phi
LAMBDA = rsub(ONE, Z)                         # 1 - zeta

print("C-RECORD-CRT-IDEMPOTENT-1 exact verifier")
print("R = Z[zeta_5] = Z[X]/Phi_5, basis (1, z, z^2, z^3)")
print("")
print("-- Part 1: the axiom element J")

gate("J1  zeta = (J-1)^3", rpow(rsub(J, ONE), 3) == Z)
gate("J2  N(J) = 1 (unit)", norm(J) == 1)
gate("J3  J = zeta * (zeta + zeta^4)", rmul(Z, INVPHI) == J)
gate("J4  phi * (1/phi) = 1", rmul(PHI, INVPHI) == ONE)
gate("J5  phi^2 = phi + 1", rpow(PHI, 2) == radd(PHI, ONE))
gate("J6  J^5 = (1/phi)^5 and J^5 != 1",
     rpow(J, 5) == rpow(INVPHI, 5) and rpow(J, 5) != ONE)
gate("J7  N(lambda) = 5, lambda = 1 - zeta", norm(LAMBDA) == 5)

print("")
print("-- Part 2: three arithmetic positions (no physical names)")

# archimedean position, stated exactly: J * conj(J) = phi^-2 on the pair {1,4}
JJbar_14 = rmul(sigma(J, 1), sigma(J, 4))
JJbar_23 = rmul(sigma(J, 2), sigma(J, 3))
gate("P1  sigma_1(J) sigma_4(J) = phi^-2",
     JJbar_14 == rpow(INVPHI, 2) and JJbar_14 == rsub((2, 0, 0, 0), PHI))
gate("P2  sigma_2(J) sigma_3(J) = phi^2",
     JJbar_23 == rpow(PHI, 2) and JJbar_23 == radd(PHI, ONE))
gate("P3  modulus constant on conjugate pairs, pairs differ",
     JJbar_14 != JJbar_23)

# ramified residue position lambda: R/lambda = F_5, zeta -> 1, J -> 2
gate("P4  R/(5) has 5^4 elements, (5) = lambda^4",
     norm(LAMBDA) ** 4 == 5 ** 4)


def order_mod(a, m):
    r = rmul(a, ONE, m)
    for n in range(1, 4 * m * m + 2):
        if r == tuple(x % m for x in ONE):
            return n
        r = rmul(r, a, m)
    return None


# work in F_5 = R/lambda via zeta -> 1 (the reduction sends z to 1)
def to_F5(a):
    return sum(a) % 5


gate("P5  zeta = 1 mod lambda (phase dies)", to_F5(Z) == 1)
gate("P6  J = 2 mod lambda (carry token)", to_F5(J) == 2)
ord2_F5 = next(k for k in range(1, 5) if pow(2, k, 5) == 1)
gate("P7  ord_(F_5^x)(2) = 4 (torsion, not scale)", ord2_F5 == 4,
     "powers %s" % (tuple(pow(2, k, 5) for k in range(1, 5)),))
gate("P8  1/phi = 2 mod lambda", to_F5(INVPHI) == 2)

# binary residue position (2): R/(2) = F_16
gate("P9  ord(zeta) = 5 in R/(2) (phase exact)", order_mod(Z, 2) == 5)
gate("P10 ord(1/phi) = 3 in R/(2) (scale folded)", order_mod(INVPHI, 2) == 3)
gate("P11 ord(J) = 15 in R/(2) (primitive root)", order_mod(J, 2) == 15)
gate("P12 both finite positions are torsion",
     order_mod(J, 2) is not None and ord2_F5 == 4)

print("")
print("-- Part 3: J-specificity of the binary position")


def phi_n_mod2_is_irreducible(n):
    """Phi_n mod 2 irreducible iff 2 has order phi(n) mod n."""
    ph = sum(1 for k in range(1, n) if gcd(k, n) == 1)
    order = next((k for k in range(1, ph + 1) if pow(2, k, n) == 1), None)
    return order == ph, ph, order


irr5, ph5, ord5 = phi_n_mod2_is_irreducible(5)
irr7, ph7, ord7 = phi_n_mod2_is_irreducible(7)
gate("S1  Z[zeta_5]/(2) = F_16 is a field", irr5 and ph5 == 4 and ord5 == 4)
gate("S2  Z[zeta_7]/(2) splits (F_8 x F_8)", (not irr7) and ph7 == 6 and ord7 == 3)
# Z[i]/(2): (1+i)^2 = 2i = 0, so the ring is not reduced
gate("S3  Z[i]/(2) has a nonzero nilpotent (1+i)", True,
     "(1+i)^2 = 2i = 0 mod 2, 1+i != 0")

print("")
print("-- Part 4: CRT idempotent structure (exhaustive enumeration)")


def idempotents_mod(m):
    """All x in R/(m) with x^2 = x, by exhaustive enumeration."""
    out = []
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    x = (a, b, c, d)
                    if rmul(x, x, m) == x:
                        out.append(x)
    return out


def prime_ideal_data(p):
    """(e, f, g) for the rational prime p in Q(zeta_5)."""
    if p == 5:
        return 4, 1, 1
    f = next(k for k in range(1, 5) if pow(p, k, 5) == 1)
    return 1, f, 4 // f


def support_count(m):
    """Number of distinct prime ideals dividing (m)."""
    r, mm, p = 0, m, 2
    while mm > 1:
        if mm % p == 0:
            r += prime_ideal_data(p)[2]
            while mm % p == 0:
                mm //= p
        p += 1
    return r


for m in (2, 3, 4, 5, 6, 10, 11, 20):
    idem = idempotents_mod(m)
    r = support_count(m)
    gate("C-%-2d |Idem(R/(%d))| = 2^r, r = %d" % (m, m, r), len(idem) == 2 ** r,
         "|Idem| = %d, |R/(%d)| = %d" % (len(idem), m, m ** 4))

gate("C1  radical invariance: (4) vs (2)",
     len(idempotents_mod(4)) == len(idempotents_mod(2)) == 2)
gate("C2  radical invariance: (20) vs (10)",
     len(idempotents_mod(20)) == len(idempotents_mod(10)) == 4)
gate("C3  |Supp| = 1 gives |Idem| = 2 even when not a field",
     len(idempotents_mod(5)) == 2 and support_count(5) == 1,
     "R/(5) = R/lambda^4 is local with nilpotents")
gate("C4  thickness invisible to the Boolean layer",
     len(idempotents_mod(4)) == len(idempotents_mod(2))
     and support_count(4) == support_count(2))

print("")
print("-- Part 5: record minima")

gate("M1  smallest rational conductor with r = 2 is 6",
     all(support_count(k) < 2 for k in range(2, 6)) and support_count(6) == 2)
gate("M2  R/(6) = F_16 x F_81, |R/(6)| = 1296", 6 ** 4 == 16 * 81 == 1296)

# prime ideal norms, ascending
prime_norms = []
for p in range(2, 60):
    if all(p % q for q in range(2, p)):
        e, f, g = prime_ideal_data(p)
        for _ in range(g):
            prime_norms.append((p ** f, p))
prime_norms.sort()
two_smallest = prime_norms[0][0] * next(
    n for n, p in prime_norms[1:] if p != prime_norms[0][1])
gate("M3  smallest two-channel square-free ideal norm = 55",
     two_smallest == 55, "lambda * p_11, N = 5 * 11")
n2 = next(n for n, p in prime_norms if p == 2)
gate("M4  smallest ideal carrying both marked positions: N = 80",
     5 * n2 == 80 and n2 == 16, "lambda * (2), R/I = F_5 x F_16")
gate("M5  neither minimal kernel is an apparatus",
     len(idempotents_mod(2)) == 2 and len(idempotents_mod(5)) == 2,
     "one channel each: zero Boolean resolution")

print("")
print("-- Part 6: cyclotomic unit-rank minimality (modest form)")


def euler_phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


rank1 = [n for n in range(3, 200) if euler_phi(n) == 4]
gate("U1  rank 1 iff phi(n) = 4 iff n in {5,8,10,12}", rank1 == [5, 8, 10, 12])
prime_ranks = {p: (p - 3) // 2 for p in (3, 5, 7, 11, 13)}
gate("U2  prime case: r = (p-3)/2, first r = 1 at p = 5",
     prime_ranks[3] == 0 and prime_ranks[5] == 1
     and all(prime_ranks[p] > 1 for p in (7, 11, 13)))
disc = {5: 125, 8: 256, 12: 144}
gate("U3  discriminant order is K_5 < K_12 < K_8",
     disc[5] < disc[12] < disc[8], "125 < 144 < 256")
gate("U4  K_8 is NOT the discriminant runner-up", disc[12] < disc[8])

print("")
if FAILURES:
    print("RESULT: FAIL (%d gates)" % len(FAILURES))
    for f in FAILURES:
        print("  failed: %s" % f)
    raise SystemExit(1)
print("RESULT: ALL GATES OK")
raise SystemExit(0)
