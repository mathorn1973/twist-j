#!/usr/bin/env python3
"""Exact L1 audit for P-TM-MULTIPLICATION-CARRY-DEFECT-1.

The all-integer claims rest on the written proof in PREREG.md. This verifier
audits exact finite instances, the complete Boolean truth table, and fixed
counter-controls. Standard library only; no floats, tolerances, randomness,
external data, or prior transcript.
"""

from __future__ import annotations


CHECKS: list[tuple[str, bool, str]] = []


def check(label: str, condition: bool, extra: str = "") -> None:
    CHECKS.append((label, bool(condition), extra))


def s2(n: int) -> int:
    return n.bit_count()


def tau(n: int) -> int:
    return -1 if (s2(n) & 1) else 1


def raw_columns(a: int, b: int) -> list[int]:
    aa = [int(ch) for ch in reversed(bin(a)[2:])]
    bb = [int(ch) for ch in reversed(bin(b)[2:])]
    raw = [0] * (len(aa) + len(bb) - 1)
    for i, ai in enumerate(aa):
        if not ai:
            continue
        for j, bj in enumerate(bb):
            if bj:
                raw[i + j] += 1
    return raw


def carry_normalize(a: int, b: int) -> tuple[int, list[int], list[int]]:
    raw = raw_columns(a, b)
    out: list[int] = []
    carries: list[int] = []
    q_prev = 0
    k = 0
    while k < len(raw) or q_prev:
        r = raw[k] if k < len(raw) else 0
        u = r + q_prev
        z = u & 1
        q = (u - z) // 2
        out.append(z)
        carries.append(q)
        q_prev = q
        k += 1
    value = sum(bit << i for i, bit in enumerate(out))
    return value, raw, carries


def kappa(a: int, b: int) -> int:
    return s2(a) * s2(b) - s2(a * b)


def c_semiprime(p: int, q: int) -> int:
    return tau(p * q) - tau(p) - tau(q) - 1


def c_prime_square(p: int) -> int:
    return tau(p * p) - tau(p)


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = False
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]


print("P-TM-MULTIPLICATION-CARRY-DEFECT-1 exact verifier")
print("scope=L1 public-probe audit")

# ---------------------------------------------------------------------------
# S1. Direct schoolbook carry normalization versus the closed formula.
# ---------------------------------------------------------------------------
s1_reconstruct = True
s1_mass = True
s1_nonnegative = True
for a in range(1, 257):
    for b in range(1, 257):
        value, raw, carries = carry_normalize(a, b)
        if value != a * b:
            s1_reconstruct = False
        kap = kappa(a, b)
        if sum(raw) != s2(a) * s2(b) or sum(carries) != kap:
            s1_mass = False
        if kap < 0:
            s1_nonnegative = False

check("S1-01 schoolbook carry normalization reconstructs ab", s1_reconstruct)
check("S1-02 total carry value equals popcount defect", s1_mass)
check("S1-03 carry mass is nonnegative", s1_nonnegative)

# ---------------------------------------------------------------------------
# S2. AND+carry XOR parity and multiplicativity-defect sign.
# ---------------------------------------------------------------------------
s2_parity = True
s2_defect = True
for a in range(1, 513):
    for b in range(1, 513):
        P = s2(a) & 1
        Q = s2(b) & 1
        K = kappa(a, b) & 1
        R = s2(a * b) & 1
        if R != ((P & Q) ^ K):
            s2_parity = False
            break
        lhs = tau(a * b) * tau(a) * tau(b)
        rhs = -1 if (((P | Q) ^ K) & 1) else 1
        if lhs != rhs:
            s2_defect = False
            break
    if not (s2_parity and s2_defect):
        break

check("S2-01 output parity is AND XOR carry parity", s2_parity)
check("S2-02 Thue-Morse multiplicativity defect is OR XOR carry parity", s2_defect)

# ---------------------------------------------------------------------------
# S3. Complete abstract table and prime semiprime audit.
# ---------------------------------------------------------------------------
expected = {
    (0, 0, 0): -2,
    (0, 0, 1): -4,
    (0, 1, 0): 0,
    (0, 1, 1): -2,
    (1, 0, 0): 0,
    (1, 0, 1): -2,
    (1, 1, 0): 0,
    (1, 1, 1): 2,
}
table_ok = True
shadow_rule_ok = True
for P in (0, 1):
    for Q in (0, 1):
        for K in (0, 1):
            R = (P & Q) ^ K
            cval = (-1 if R else 1) - (-1 if P else 1) - (-1 if Q else 1) - 1
            if cval != expected[(P, Q, K)]:
                table_ok = False
            if (cval == 0) != (K == 0 and (P | Q) == 1):
                shadow_rule_ok = False

check("S3-01 complete eight-state semiprime table", table_ok)
check("S3-02 zero-shadow criterion", shadow_rule_ok)

prime_pair_ok = True
ps = [p for p in primes_upto(257) if p != 2]
pair_count = 0
for i, p in enumerate(ps):
    for q in ps[i + 1:]:
        P = s2(p) & 1
        Q = s2(q) & 1
        K = kappa(p, q) & 1
        cval = c_semiprime(p, q)
        if cval not in (-4, -2, 0, 2):
            prime_pair_ok = False
        if (cval == 0) != (K == 0 and (P | Q) == 1):
            prime_pair_ok = False
        pair_count += 1

check("S3-03 odd-prime pair classification", prime_pair_ok, f"pairs={pair_count}")
check(
    "S3-04 nonzero-carry zero-shadow control",
    kappa(3, 11) == 4 and c_semiprime(3, 11) == 0,
    "p=3 q=11",
)
check(
    "S3-05 zero-carry shadow and odd-carry excitation controls",
    kappa(7, 17) == 0
    and c_semiprime(7, 17) == 0
    and kappa(3, 113) == 3
    and c_semiprime(3, 113) == -4,
)

# ---------------------------------------------------------------------------
# S4. Prime-square identity and carry-parity criterion.
# ---------------------------------------------------------------------------
square_ok = True
square_count = 0
for p in primes_upto(2000):
    cval = c_prime_square(p)
    if (cval == 0) != ((kappa(p, p) & 1) == 0):
        square_ok = False
        break
    square_count += 1

check("S4-01 prime-square shadow criterion", square_ok, f"primes={square_count}")
check(
    "S4-02 named square controls",
    c_prime_square(3) == 0
    and c_prime_square(7) == 0
    and c_prime_square(5) == -2,
)

# ---------------------------------------------------------------------------
# S5. Carry-field representation on complete subset cubes.
# ---------------------------------------------------------------------------
def mixed_difference(prime_list: list[int]) -> tuple[int, int, bool]:
    m = len(prime_list)
    direct = 0
    carry_field = 0
    nonnegative = True
    for mask in range(1 << m):
        n_s = 1
        a_s = 1
        chosen = 0
        and_p = 1
        for i, p in enumerate(prime_list):
            if (mask >> i) & 1:
                n_s *= p
                a_s *= s2(p)
                and_p &= (s2(p) & 1)
                chosen += 1
        kap = a_s - s2(n_s)
        if kap < 0:
            nonnegative = False
        sign = -1 if ((m - chosen) & 1) else 1
        direct += sign * tau(n_s)
        exponent = and_p ^ (kap & 1)
        carry_tau = -1 if exponent else 1
        carry_field += sign * carry_tau
    return direct, carry_field, nonnegative


cube_ok = True
cube_nonnegative = True
cube_count = 0
base_primes = [3, 5, 7, 11, 13, 17, 19]
for mask in range(1, 1 << len(base_primes)):
    subset = [p for i, p in enumerate(base_primes) if (mask >> i) & 1]
    direct, field, nonnegative = mixed_difference(subset)
    if direct != field:
        cube_ok = False
        break
    if not nonnegative:
        cube_nonnegative = False
        break
    cube_count += 1

check("S5-01 higher squarefree carry-field identity", cube_ok, f"cubes={cube_count}")
check("S5-02 multi-product carry mass nonnegative on audit cubes", cube_nonnegative)

# Scope guards.
check(
    "G-01 c=0 does not mean zero carries",
    kappa(3, 11) > 0 and c_semiprime(3, 11) == 0,
)

for label, passed, extra in CHECKS:
    print(("PASS " if passed else "FAIL ") + label + (("  " + extra) if extra else ""))

failures = [label for label, passed, _extra in CHECKS if not passed]
print(f"CHECKS {len(CHECKS)}")
if failures:
    print("DECISION MISMATCH")
    print("FAILURES " + " | ".join(failures))
    raise SystemExit(0)

print("DECISION CARRY-PASS")
raise SystemExit(0)
