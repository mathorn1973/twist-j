#!/usr/bin/env python3
# break.py - independent blind-breaker attack for
# P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1 (public lock issue #256).
#
# Breaker firewall declaration: this program was authored from the frozen
# PREREG.md (SHA-256
# f8ac045f4f35a87a04a4f8578b1bb1a8b69c75f8434d981fc6d77e71ffea9e72,
# 19692 bytes, pin commit 7291c079811a2a0191ab536590f7a5d723a9a7c7),
# Public Canon v32, and the declared dependencies only. The builder
# verify.py, any EXPECTED.txt, and any builder stdout were not read.
#
# The program independently reconstructs every frozen object and attempts
# to produce an exact witness for each NEGATIVE clause of the
# preregistration: an omitted solution of phi(n) = 4, a wrong field
# identification, a different ramification decomposition, a false norm
# identity, or a false residue calculation. Exact integer arithmetic and
# the Python standard library only; no argv, environment, file, or
# network input.
import math
import sys
from fractions import Fraction

BREAKS = []


def gate(name, ok, witness=""):
    line = ("OK    " if ok else "BREAK ") + name
    if witness and not ok:
        line += " :: " + witness
    print(line)
    if not ok:
        BREAKS.append(name)


# ---------- exact polynomial arithmetic over Z (ascending coefficients) ----
def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def pdivmod_monic(a, b):
    # exact division by a monic b over Z
    a = list(a)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        if a[-1] == 0:
            a.pop()
            continue
        shift = len(a) - len(b)
        coeff = a[-1]
        q[shift] += coeff
        for i, y in enumerate(b):
            a[shift + i] -= coeff * y
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return q, a


def peval(a, x):
    v = 0
    for c in reversed(a):
        v = v * x + c
    return v


def cyclotomic(n, cache={}):
    if n in cache:
        return cache[n]
    poly = [-1] + [0] * (n - 1) + [1]          # x^n - 1
    for d in range(1, n):
        if n % d == 0:
            poly, rem = pdivmod_monic(poly, cyclotomic(d))
            assert rem == [0]
    cache[n] = poly
    return poly


def pderiv(a):
    return [i * c for i, c in enumerate(a)][1:] or [0]


# ---------- polynomial arithmetic over F_p ---------------------------------
def pmod(a, p):
    a = [c % p for c in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul_p(a, b, p):
    return pmod(pmul(a, b), p)


def pdivmod_p(a, b, p):
    a = pmod(a, p)
    b = pmod(b, p)
    inv = pow(b[-1], -1, p)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        if a[-1] % p == 0:
            a.pop()
            continue
        shift = len(a) - len(b)
        coeff = (a[-1] * inv) % p
        q[shift] = (q[shift] + coeff) % p
        for i, y in enumerate(b):
            a[shift + i] = (a[shift + i] - coeff * y) % p
        a = pmod(a, p)
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return pmod(q, p), pmod(a, p)


def pgcd_p(a, b, p):
    a, b = pmod(a, p), pmod(b, p)
    while b != [0]:
        a, b = b, pdivmod_p(a, b, p)[1]
    inv = pow(a[-1], -1, p)
    return pmod([c * inv for c in a], p)


def monic_irreducibles(p, max_deg):
    # exhaustive: degree 1 all x + a; degree >= 2 by rootlessness and
    # trial division by all smaller-degree irreducibles
    irr = {1: [[a % p, 1] for a in range(p)]}
    for d in range(2, max_deg + 1):
        found = []
        for code in range(p ** d):
            coeffs = []
            c = code
            for _ in range(d):
                coeffs.append(c % p)
                c //= p
            poly = coeffs + [1]
            reducible = False
            for dd in range(1, d // 2 + 1):
                for g in irr[dd]:
                    if pdivmod_p(poly, g, p)[1] == [0]:
                        reducible = True
                        break
                if reducible:
                    break
            if not reducible:
                found.append(poly)
        irr[d] = found
    return irr


def factor_deg4_p(f, p):
    # complete factorization of a monic degree-4 polynomial over F_p by
    # exhaustive trial division with irreducibles of degree 1 and 2; a
    # rootless remainder of degree 3 or 4 with no quadratic factor is
    # irreducible
    f = pmod(f, p)
    assert len(f) == 5 and f[-1] % p == 1
    irr = monic_irreducibles(p, 2)
    factors = {}
    rest = f
    for d in (1, 2):
        for g in irr[d]:
            while len(rest) > 1:
                q, r = pdivmod_p(rest, g, p)
                if r == [0]:
                    key = tuple(g)
                    factors[key] = factors.get(key, 0) + 1
                    rest = q
                else:
                    break
    if len(rest) > 1:
        factors[tuple(rest)] = factors.get(tuple(rest), 0) + 1
    # audit: product of factors reproduces f
    prod = [1]
    for g, e in factors.items():
        for _ in range(e):
            prod = pmul_p(prod, list(g), p)
    assert prod == f
    return factors


def profile_efg(factors, degree):
    # Galois field: all factors share one degree f and one multiplicity e
    degs = {len(g) - 1 for g in factors}
    mults = set(factors.values())
    if len(degs) != 1 or len(mults) != 1:
        return None
    fdeg = degs.pop()
    e = mults.pop()
    g = len(factors)
    if e * fdeg * g != degree:
        return None
    return (e, fdeg, g)


# ---------- exact linear algebra: resultant via Sylvester ------------------
def resultant(f, g):
    m, n = len(f) - 1, len(g) - 1
    size = m + n
    rows = []
    fd = list(reversed(f))
    gd = list(reversed(g))
    for i in range(n):
        rows.append([0] * i + fd + [0] * (size - m - 1 - i))
    for i in range(m):
        rows.append([0] * i + gd + [0] * (size - n - 1 - i))
    mat = [[Fraction(x) for x in row] for row in rows]
    det = Fraction(1)
    for col in range(size):
        pivot = next((r for r in range(col, size) if mat[r][col] != 0), None)
        if pivot is None:
            return 0
        if pivot != col:
            mat[col], mat[pivot] = mat[pivot], mat[col]
            det = -det
        det *= mat[col][col]
        inv = mat[col][col]
        for r in range(col + 1, size):
            factor = mat[r][col] / inv
            if factor:
                for c in range(col, size):
                    mat[r][c] -= factor * mat[col][c]
    assert det.denominator == 1
    return int(det)


def discriminant(f):
    d = len(f) - 1
    sign = -1 if (d * (d - 1) // 2) % 2 else 1
    return sign * resultant(f, pderiv(f))


# ---------- number-theoretic helpers ---------------------------------------
def factorize(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def phi(n):
    result = 1
    for p, a in factorize(n).items():
        result *= p ** (a - 1) * (p - 1)
    return result


def primes_below(limit):
    sieve = bytearray([1]) * limit
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [i for i in range(limit) if sieve[i]]


# ===========================================================================
print("BLIND BREAKER break.py"
      " P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1")
print("FIREWALL frozen PREREG.md sha256 f8ac045f4f35a87a04a4f8578b1bb1a8b6"
      "9c75f8434d981fc6d77e71ffea9e72; builder verify.py not read")
print()

# B01: attack the index census phi(n) = 4.
# Structural completeness, derived independently: for odd p | n the factor
# p - 1 divides phi(n) = 4, so p in {3, 5}; an odd p^2 | n would put p | 4;
# phi(2^a) = 2^(a-1) divides 4, so a <= 3. The box below is therefore
# complete; a wider box and a sieve to 10^6 hunt for omitted solutions.
odd_allowed = [p for p in primes_below(1000)
               if p % 2 == 1 and 4 % (p - 1) == 0]
box = set()
for a in range(0, 6):
    for b in range(0, 3):
        for c in range(0, 3):
            n = (2 ** a) * (3 ** b) * (5 ** c)
            if phi(n) == 4:
                box.add(n)
LIMIT = 10 ** 6
phis = list(range(LIMIT))
for p in primes_below(LIMIT):
    for multiple in range(p, LIMIT, p):
        phis[multiple] -= phis[multiple] // p
scan = {n for n in range(1, LIMIT) if phis[n] == 4}
gate("B01 TOTIENT-CENSUS  phi(n)=4 exactly on {5,8,10,12}",
     odd_allowed == [3, 5] and box == {5, 8, 10, 12}
     and scan == {5, 8, 10, 12},
     "odd primes %s box %s scan %s" % (odd_allowed, sorted(box),
                                       sorted(scan)))

# B02: independent reconstruction of the cyclotomic polynomials.
PHI5 = cyclotomic(5)
PHI8 = cyclotomic(8)
PHI10 = cyclotomic(10)
PHI12 = cyclotomic(12)
gate("B02 CYCLOTOMIC-POLYS Phi_5, Phi_8, Phi_10, Phi_12 reconstructed",
     PHI5 == [1, 1, 1, 1, 1] and PHI8 == [1, 0, 0, 0, 1]
     and PHI10 == [1, -1, 1, -1, 1] and PHI12 == [1, 0, -1, 0, 1],
     "got %s %s %s %s" % (PHI5, PHI8, PHI10, PHI12))

# B03: attack the field equality Q(zeta_10) = Q(zeta_5).
# zeta_10 := -zeta_5^3 in the power basis of K_5; check it is a primitive
# 10th root and that its square is zeta_5 (both inclusions).
def reduce5(poly):
    return pdivmod_monic(poly, PHI5)[1]


t = [0, 0, 0, -1]                       # -y^3
powers = {1: t}
for k in range(2, 11):
    powers[k] = reduce5(pmul(powers[k - 1], t))
is_one = {k: powers[k] == [1] for k in powers}
subst = [1]
acc = [0]
for coeff in PHI10:
    L = max(len(acc), len(subst))
    acc_new = [(acc[i] if i < len(acc) else 0)
               + coeff * (subst[i] if i < len(subst) else 0)
               for i in range(L)]
    acc = reduce5(acc_new)
    subst = reduce5(pmul(subst, t))
gate("B03 FIELD-EQUALITY  zeta_10 = -zeta_5^3 primitive of order 10;"
     " zeta_10^2 = zeta_5; Phi_10(-zeta_5^3) = 0",
     acc == [0] and powers[10] == [1] and powers[2] == [0, 1]
     and not any(is_one[k] for k in range(1, 10)),
     "Phi_10 at -y^3 -> %s; square -> %s" % (acc, powers[2]))

# B04: attack the discriminants by two independent exact routes.
def disc_formula(n):
    ph = phi(n)
    num = n ** ph
    den = 1
    for p in factorize(n):
        den *= p ** (ph // (p - 1))
    assert num % den == 0
    return (-1) ** (ph // 2) * (num // den)


routes = {
    5: (discriminant(PHI5), disc_formula(5), 125),
    8: (discriminant(PHI8), disc_formula(8), 256),
    10: (discriminant(PHI10), disc_formula(10), 125),
    12: (discriminant(PHI12), disc_formula(12), 144),
}
gate("B04 DISCRIMINANTS   resultant route = formula route ="
     " (125, 256, 125, 144) for n = 5, 8, 10, 12",
     all(a == b == c for a, b, c in routes.values()),
     str(routes))

# B05: attack the four modular reductions and the (e,f,g) profiles by
# exhaustive independent factorization.
cases = {
    ("Phi_5", 5): (PHI5, (4, 1, 1), [((4, 1), 4)]),
    ("Phi_8", 2): (PHI8, (4, 1, 1), [((1, 1), 4)]),
    ("Phi_12", 2): (PHI12, (2, 2, 1), [((1, 1, 1), 2)]),
    ("Phi_12", 3): (PHI12, (2, 2, 1), [((1, 0, 1), 2)]),
}
profiles_ok = True
witness = []
for (label, p), (poly, expected_efg, expected_factors) in cases.items():
    factors = factor_deg4_p(poly, p)
    efg = profile_efg(factors, 4)
    want = {tuple(g): e for g, e in expected_factors}
    if efg != expected_efg or factors != want:
        profiles_ok = False
        witness.append("%s mod %d -> %s efg %s" % (label, p, factors, efg))
irr2_ok = (pgcd_p([1, 1, 1], pderiv([1, 1, 1]), 2) == [1]
           and all(peval([1, 1, 1], a) % 2 != 0 for a in range(2))
           and all(peval([1, 0, 1], a) % 3 != 0 for a in range(3)))
gate("B05 PROFILES        (x-1)^4 mod 5, (x+1)^4 mod 2, (x^2+x+1)^2 mod 2,"
     " (x^2+1)^2 mod 3; quadratics rootless; (e,f,g) = (4,1,1), (4,1,1),"
     " (2,2,1), (2,2,1)", profiles_ok and irr2_ok, "; ".join(witness))

# B06: attack the completeness of the ramified-prime support: for every
# prime p < 200, Phi_n mod p is squarefree iff p does not divide disc(K_n).
support = {5: {5}, 8: {2}, 12: {2, 3}}
sq_ok = True
sq_witness = []
for n, poly in ((5, PHI5), (8, PHI8), (12, PHI12)):
    for p in primes_below(200):
        squarefree = pgcd_p(poly, pderiv(poly), p) == [1]
        if squarefree != (p not in support[n]):
            sq_ok = False
            sq_witness.append("n=%d p=%d squarefree=%s" % (n, p, squarefree))
gate("B06 OTHER-PRIMES    for p < 200, Phi_n mod p squarefree exactly"
     " off the discriminant support {5}, {2}, {2,3}", sq_ok,
     "; ".join(sq_witness))

# B07: attack the norm identities N(1 - zeta_n) = Phi_n(1).
norms = (peval(PHI5, 1), peval(PHI8, 1), peval(PHI10, 1), peval(PHI12, 1))
gate("B07 NORMS           Phi_5(1) = 5, Phi_8(1) = 2; the controls"
     " Phi_10(1) = Phi_12(1) = 1 make 1 - zeta a unit there",
     norms == (5, 2, 1, 1), str(norms))

# B08: attack the residue-unit census by complete enumeration.
def unit_orders_prime_field(p):
    return {a: next(k for k in range(1, p) if pow(a, k, p) == 1)
            for a in range(1, p)}


f5 = unit_orders_prime_field(5)
f2 = unit_orders_prime_field(2)


def ext_field_units(p, modulus):
    # F_p[x]/(modulus), modulus monic quadratic irreducible
    elements = [[a, b] for a in range(p) for b in range(p)]
    nonzero = [e for e in elements if e != [0, 0]]
    orders = {}
    for e in nonzero:
        acc, k = [1], 0
        while True:
            k += 1
            acc = pdivmod_p(pmul(acc, e), modulus, p)[1]
            if acc == [1]:
                break
            assert k <= p * p
        orders[tuple(e)] = k
    return orders


f4 = ext_field_units(2, [1, 1, 1])       # F_2[t]/(t^2+t+1)
f9 = ext_field_units(3, [1, 0, 1])       # F_3[u]/(u^2+1)
chain = (pdivmod_p(pmul([1, 1], [1, 1]), [1, 0, 1], 3)[1] == [0, 2]
         and f9[(1, 1)] == 8)            # (1+u)^2 = -u = 2u, ord(1+u) = 8
gate("B08 RESIDUE-UNITS   F_5^x = C_4 with ord(2) = 4; F_2^x = C_1;"
     " F_4^x = C_3 with ord(t) = 3; F_9^x = C_8 with ord(1+u) = 8",
     max(f5.values()) == 4 and f5[2] == 4
     and sorted(f5.values()) == [1, 2, 4, 4]
     and f2 == {1: 1}
     and sorted(f4.values()) == [1, 3, 3] and f4[(0, 1)] == 3
     and sorted(f9.values()) == sorted([1, 2, 4, 4, 8, 8, 8, 8])
     and chain,
     "f5 %s f4 %s f9 %s" % (f5, sorted(f4.values()), sorted(f9.values())))

# B09: attack the inherited reduction J mod p_(5,5) = 2 (mismatch would be
# repository STOP, not an ordinary negative).
q, r = pdivmod_monic([-1, 0, 1], [-1, 1])    # (y^2 - 1) / (y - 1)
j_at_1 = peval([1, 0, 1], 1)                 # J = 1 + y^2 at zeta_5 -> 1
gen = sorted(pow(2, k, 5) for k in range(4))
gate("B09 INHERITED-J     (1 + y^2) - 2 divisible by y - 1; J mod p = 2;"
     " ord(2) = 4 and <2> = F_5^x",
     r == [0] and j_at_1 == 2 and f5[2] == 4 and gen == [1, 2, 3, 4],
     "rem %s J(1) %s <2> %s" % (r, j_at_1, gen))

# B10: breaker extras beyond the listed gates: Galois-group exponents
# distinguish the cyclic K_5 from the biquadratic K_8 and K_12; the same
# field K_10 = K_5 shows the same total profile at 5 via Phi_10; no prime
# below 200 is totally ramified anywhere except the two selected pairs.
def unit_group_exponent(m):
    units = [a for a in range(1, m) if math.gcd(a, m) == 1]
    exp = 1
    for a in units:
        k = next(j for j in range(1, m + 1) if pow(a, j, m) == 1)
        exp = exp * k // math.gcd(exp, k)
    return exp


def totally_ramified(poly, p):
    # e = 4 in a Galois quartic iff Phi mod p = (x - r)^4 for some r
    target = pmod(poly, p)
    for r in range(p):
        fourth = [1]
        for _ in range(4):
            fourth = pmul_p(fourth, [-r, 1], p)
        if fourth == target:
            return True
    return False


phi10_mod5 = factor_deg4_p(PHI10, 5)
total_pairs = []
for n, poly in ((5, PHI5), (8, PHI8), (12, PHI12)):
    for p in primes_below(200):
        if totally_ramified(poly, p):
            total_pairs.append((n, p))
gate("B10 EXTRAS          exponents of (Z/5)^x, (Z/8)^x, (Z/12)^x are"
     " 4, 2, 2; Phi_10 mod 5 = (x+1)^4; total pairs below 200 are"
     " exactly (K_5, 5) and (K_8, 2)",
     unit_group_exponent(5) == 4 and unit_group_exponent(8) == 2
     and unit_group_exponent(12) == 2
     and phi10_mod5 == {(1, 1): 4}
     and total_pairs == [(5, 5), (8, 2)],
     "totals %s phi10mod5 %s" % (total_pairs, phi10_mod5))

print()
if BREAKS:
    print("BREAK FOUND %d/%d" % (len(BREAKS), 10))
    sys.exit(1)
print("NO BREAK FOUND 10/10; the frozen census survives this"
      " independent attack")
sys.exit(0)
