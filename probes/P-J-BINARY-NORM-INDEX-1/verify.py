#!/usr/bin/env python3
"""P-J-BINARY-NORM-INDEX-1 accepted verifier.

Exact arithmetic only: integers and integer coefficient tuples. No float, no
complex, no randomness, no network, no subprocess, no external data, no
filesystem read or write, no read of canon/. Zero arguments. Deterministic
stdout with no environment, platform, timing or path field, so stdout is
byte-identical on every architecture. Run from the repository root:

    python3 probes/P-J-BINARY-NORM-INDEX-1/verify.py

Notation, pinned in block N. K = Q(zeta_5), O_K = Z[zeta_5], J = 1 + zeta_5^2.
For a prime p inert in K the residue ring O_K/(p) is carried as
F_p[x]/(Phi_5) with Phi_5 = 1 + x + x^2 + x^3 + x^4 and x the image of zeta_5,
so an element is the coefficient tuple (c0, c1, c2, c3) of c0 + c1 x + c2 x^2
+ c3 x^3 with entries reduced mod p.
"""

CENSUS_LIMIT = 2000
NORM_PATH_LIMIT = 300
CENSUS_HITS = (2, 3)
INERT_COUNT = 156

CHECKS = []


def check(label, ok):
    CHECKS.append((label, bool(ok)))


# ------------------------------------------------------------- integers

def sieve(n):
    flags = [True] * (n + 1)
    flags[0] = flags[1] = False
    i = 2
    while i * i <= n:
        if flags[i]:
            for m in range(i * i, n + 1, i):
                flags[m] = False
        i += 1
    return [k for k in range(2, n + 1) if flags[k]]


def factor(n):
    acc = {}
    for d in (2, 3):
        while n % d == 0:
            acc[d] = acc.get(d, 0) + 1
            n //= d
    d, step = 5, 2
    while d * d <= n:
        while n % d == 0:
            acc[d] = acc.get(d, 0) + 1
            n //= d
        d += step
        step = 6 - step
    if n > 1:
        acc[n] = acc.get(n, 0) + 1
    return acc


def factor_p4m1(p):
    """Factor p^4 - 1 = (p - 1)(p + 1)(p^2 + 1) piecewise, each factor small."""
    acc = {}
    for m in (p - 1, p + 1, p * p + 1):
        for q, e in factor(m).items():
            acc[q] = acc.get(q, 0) + e
    return acc


def ord_mod(a, m):
    """Multiplicative order of a modulo m, for gcd(a, m) = 1."""
    k, x = 1, a % m
    while x != 1:
        x = (x * a) % m
        k += 1
    return k


# --------------------------------------------------- residue field F_p^4

ONE = (1, 0, 0, 0)
ZERO = (0, 0, 0, 0)
X = (0, 1, 0, 0)
J = (1, 0, 1, 0)
W = (2, 1, 0, 0)


def fmul(a, b, p):
    r = [0] * 7
    for i in range(4):
        ai = a[i]
        if ai:
            for k in range(4):
                r[i + k] = (r[i + k] + ai * b[k]) % p
    for d in (6, 5, 4):
        c = r[d]
        if c:
            r[d] = 0
            for k in range(4):
                r[d - 4 + k] = (r[d - 4 + k] - c) % p
    return (r[0], r[1], r[2], r[3])


def fpow(a, e, p):
    r = ONE
    while e:
        if e & 1:
            r = fmul(r, a, p)
        a = fmul(a, a, p)
        e >>= 1
    return r


def elt_order(a, p, group_order, prime_divisors):
    o = group_order
    for q in prime_divisors:
        while o % q == 0 and fpow(a, o // q, p) == ONE:
            o //= q
    return o


def const(c, p):
    return (c % p, 0, 0, 0)


PRIMES = sieve(CENSUS_LIMIT)
INERT = [p for p in PRIMES if p % 5 in (2, 3)]
NORM_PATH = [p for p in INERT if p < NORM_PATH_LIMIT]

# ------------------------------------------------------------- block N

check("N1 x^5 equals 1 in F_p[x]/(Phi_5) for every inert p below the census limit",
      all(fpow(X, 5, p) == ONE for p in INERT))

check("N2 (J - 1)^3 equals x in every such residue ring, so J generates it",
      all(fpow(tuple((J[i] - ONE[i]) % p for i in range(4)), 3, p) == X
          for p in INERT))

check("N3 ord_5(p) equals 4 for every inert p, so Phi_5 is irreducible over F_p "
      "and the quotient is the field of p^4 elements",
      all(ord_mod(p, 5) == 4 for p in INERT))

check("N4 the inert primes below the census limit are exactly the primes "
      "congruent to 2 or 3 mod 5, and there are the recorded number of them",
      len(INERT) == INERT_COUNT and all(p % 5 in (2, 3) for p in INERT))

# ------------------------------------------------------------- block A

check("A1 (p^4 - 1)/(p - 1) equals (p + 1)(p^2 + 1) equals 1 + p + p^2 + p^3 "
      "for every inert p",
      all((p ** 4 - 1) % (p - 1) == 0
          and (p ** 4 - 1) // (p - 1) == (p + 1) * (p * p + 1)
          and (p + 1) * (p * p + 1) == 1 + p + p * p + p ** 3
          for p in INERT))

check("A2 the index of the norm-one subgroup in F_(p^4)^x is p - 1, so that "
      "subgroup is the whole group exactly when p equals 2",
      all((p ** 4 - 1) // ((p ** 4 - 1) // (p - 1)) == p - 1 for p in INERT)
      and [p for p in INERT if (p ** 4 - 1) // (p - 1) == p ** 4 - 1] == [2])

check("A3 the index is p - 1 in degrees 2, 3, 4, 6 and 8 alike, so the "
      "mechanism is generic and is not a property of J or of the prime 5",
      all((p ** n - 1) // ((p ** n - 1) // (p - 1)) == p - 1
          for n in (2, 3, 4, 6, 8) for p in PRIMES[:40])
      and all(((p ** n - 1) // (p - 1) == p ** n - 1) == (p == 2)
              for n in (2, 3, 4, 6, 8) for p in PRIMES[:40]))

# ------------------------------------------------------------- block B

def frobenius_norm(a, p):
    acc = ONE
    for k in range(4):
        acc = fmul(acc, fpow(a, p ** k, p), p)
    return acc


check("B1 N(Jbar) equals 1 by the Frobenius product for every inert p below "
      "the norm-path limit",
      all(frobenius_norm(J, p) == ONE for p in NORM_PATH))

check("B2 N(Jbar) equals 1 by the exponent path for the same primes, so the "
      "two independent norm routes agree",
      all(fpow(J, (p ** 4 - 1) // (p - 1), p) == ONE for p in NORM_PATH))

ORDERS = {}
for p in INERT:
    divisors = sorted(factor_p4m1(p))
    ORDERS[p] = elt_order(J, p, p ** 4 - 1, divisors)

check("B3 ord(Jbar) divides (p + 1)(p^2 + 1) for every inert p below the "
      "census limit, which is the norm-one constraint made explicit",
      all((p + 1) * (p * p + 1) % ORDERS[p] == 0 for p in INERT))

# ------------------------------------------------------------- block C

ELEMENTS = [(a, b, c, d)
            for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
NONZERO = [e for e in ELEMENTS if e != ZERO]

check("C1 the quotient at p = 2 has sixteen elements and all fifteen nonzero "
      "ones are invertible, so it is the field of sixteen elements",
      len(ELEMENTS) == 16
      and all(any(fmul(e, f, 2) == ONE for f in NONZERO) for e in NONZERO))

check("C2 at p = 2, J^3 equals x^3 and has order five, and J^5 equals "
      "x^2 + x^3 and has order three",
      fpow(J, 3, 2) == (0, 0, 0, 1)
      and elt_order(fpow(J, 3, 2), 2, 15, (3, 5)) == 5
      and fpow(J, 5, 2) == (0, 0, 1, 1)
      and elt_order(fpow(J, 5, 2), 2, 15, (3, 5)) == 3)

check("C3 ord(Jbar) equals 15 at p = 2 by exhaustion over exponents 1 to 15",
      all(fpow(J, n, 2) != ONE for n in range(1, 15))
      and fpow(J, 15, 2) == ONE)

check("C4 p = 2 is the only inert p below the census limit at which ord(Jbar) "
      "equals p^4 - 1, so a norm-one unit generates the residue field there "
      "and nowhere else",
      [p for p in INERT if ORDERS[p] == p ** 4 - 1] == [2])

# ------------------------------------------------------------- block D

CONJ = [tuple((ONE[i] + fpow(X, k, 2)[i]) % 2 for i in range(4)) for k in (1, 2, 3, 4)]

check("D1 1 + x^k has order fifteen at p = 2 for k = 1, 2, 3 and 4",
      all(elt_order(e, 2, 15, (3, 5)) == 15 for e in CONJ))

check("D2 those four elements are J, J^2, J^4 and J^8, one Frobenius orbit, so "
      "generating F_16^x is Galois invariant and selects no exponent a in "
      "J = 1 + zeta_5^a",
      sorted([n for n in range(1, 16) for e in CONJ if fpow(J, n, 2) == e])
      == [1, 2, 4, 8])

# ------------------------------------------------------------- block E

check("E1 ord(Jbar) equals the full norm-one order (p + 1)(p^2 + 1) exactly at "
      "p = 2 and p = 3 among the inert p below the census limit",
      tuple(p for p in INERT if ORDERS[p] == (p + 1) * (p * p + 1)) == CENSUS_HITS)

check("E2 at every other inert p below the census limit the order is a proper "
      "divisor of (p + 1)(p^2 + 1)",
      all(ORDERS[p] < (p + 1) * (p * p + 1)
          for p in INERT if p not in CENSUS_HITS))

# ------------------------------------------------------------- block F

check("F1 control: xbar has norm one and order five at p = 2, so norm one "
      "permits generation but does not force it",
      frobenius_norm(X, 2) == ONE and elt_order(X, 2, 15, (3, 5)) == 5)

check("F2 control: w = 2 + x has N(w) = 11, and its residue norm is 11 mod p "
      "at every inert p below the norm-path limit, which is 2 at p = 3, so a "
      "non-unit is not confined to the norm-one subgroup",
      all(fpow(W, (p ** 4 - 1) // (p - 1), p) == const(11, p) for p in NORM_PATH)
      and const(11, 3) == (2, 0, 0, 0)
      and (3 + 1) * (3 * 3 + 1)
      % elt_order(W, 3, 3 ** 4 - 1, sorted(factor_p4m1(3))) != 0)

# ------------------------------------------------------------- report

fails = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    fails += not ok
if fails:
    print("DECISION J-BINARY-NORM-INDEX-FIRED")
    print("FIRED count=%d" % fails)
else:
    print("DECISION J-BINARY-NORM-INDEX-CONFIRMED")
    print("INDEX index=p-1 norm_one_order=(p+1)(p^2+1)")
    print("UNIQUENESS full_group_possible_only_at=2")
    print("ATTAINMENT p=2 ord_Jbar=15 group_order=15")
    print("CENSUS full_norm_one_generation=2,3 inert_count=%d range=%d"
          % (INERT_COUNT, CENSUS_LIMIT))
    print("GALOIS orbit=1+x,1+x^2,1+x^3,1+x^4 orders=15 selects=nothing")
print("SCOPE L1 only; no selector, no apparatus, no instrument, no event, "
      "no measure, no L2-L6 lift")
print("RESULT %d/%d PASS" % (len(CHECKS) - fails, len(CHECKS)))
raise SystemExit(1 if fails else 0)
