#!/usr/bin/env python3
"""Exact L1 audit for P-MOBIUS-TM-PRIME2-1.

This verifier audits finite instances of the written theorem package in
PREREG.md. The all-n and all-function claims rest on the written proofs, not on
finite enumeration. Standard library only. No floats, tolerances, external
inputs, or prior incubation transcript.
"""

from __future__ import annotations


CHECKS: list[tuple[str, bool, str]] = []


def check(label: str, condition: bool, extra: str = "") -> None:
    CHECKS.append((label, bool(condition), extra))


def tau(n: int) -> int:
    return -1 if n.bit_count() & 1 else 1


N = 32768
SYNTH_N = 4096
LAMBERT_N = 2048

# Exact Moebius sieve, plus omega and smallest prime factor for audit helpers.
mu = [0] * (N + 1)
omega = [0] * (N + 1)
spf = [0] * (N + 1)
primes: list[int] = []
mu[1] = 1
for i in range(2, N + 1):
    if spf[i] == 0:
        spf[i] = i
        primes.append(i)
        mu[i] = -1
        omega[i] = 1
    for p in primes:
        v = i * p
        if v > N:
            break
        spf[v] = p
        if i % p == 0:
            mu[v] = 0
            omega[v] = omega[i]
            break
        mu[v] = -mu[i]
        omega[v] = omega[i] + 1

TAU = [tau(n) for n in range(N + 1)]


def mobius_transform(values: list[int], bound: int) -> list[int]:
    out = [0] * (bound + 1)
    for d in range(1, bound + 1):
        md = mu[d]
        if md == 0:
            continue
        for k in range(1, bound // d + 1):
            out[d * k] += md * values[k]
    return out


def divisor_sum(values: list[int], bound: int) -> list[int]:
    out = [0] * (bound + 1)
    for d in range(1, bound + 1):
        vd = values[d]
        if vd == 0:
            continue
        for k in range(1, bound // d + 1):
            out[d * k] += vd
    return out


def remove_p_power(n: int, p: int) -> int:
    while n % p == 0:
        n //= p
    return n


def distinct_prime_factors(n: int) -> list[int]:
    out: list[int] = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


C = mobius_transform(TAU, N)
SUM_C = divisor_sum(C, N)

print("P-MOBIUS-TM-PRIME2-1 exact verifier")
print("scope=L1 public-probe audit")
print(f"N={N} SYNTH_N={SYNTH_N} LAMBERT_N={LAMBERT_N}")

# S1. Audit both directions on fresh synthetic prime-dilation lanes.
s1_forward = True
s1_reverse = True
for p in (2, 3, 5, 7, 11):
    f = [0] * (SYNTH_N + 1)
    for n in range(1, SYNTH_N + 1):
        r = remove_p_power(n, p)
        f[n] = ((7 * r * r + 3 * r + 5) % 37) - 18
    g = mobius_transform(f, SYNTH_N)
    if any(g[n] != 0 for n in range(p, SYNTH_N + 1, p)):
        s1_forward = False

    h = [0] * (SYNTH_N + 1)
    for n in range(1, SYNTH_N + 1):
        if n % p:
            h[n] = ((5 * n * n * n + 2 * n + 9) % 41) - 20
    f2 = divisor_sum(h, SYNTH_N)
    if any(f2[p * n] != f2[n] for n in range(1, SYNTH_N // p + 1)):
        s1_reverse = False

check("S1-01 dilation invariance implies p-free Moebius support", s1_forward)
check("S1-02 p-free primitive support implies dilation invariance", s1_reverse)

# S2. Exact Thue-Morse recurrences, scope correction, annihilation and inversion.
check(
    "S2-01 Thue-Morse binary recurrences",
    all(TAU[2 * n] == TAU[n] for n in range(0, N // 2 + 1))
    and all(TAU[2 * n + 1] == -TAU[n] for n in range(0, (N - 1) // 2 + 1)),
)
check(
    "S2-02 mu(2x)=-mu(x) on odd x",
    all(mu[2 * x] == -mu[x] for x in range(1, N // 2 + 1, 2)),
)
check(
    "S2-03 unrestricted mu(2x) wording is false at x=2",
    (mu[4], -mu[2]) == (0, 1),
    "witness x=2",
)
check(
    "S2-04 every even c coefficient vanishes",
    all(C[n] == 0 for n in range(2, N + 1, 2)),
)
check(
    "S2-05 Moebius inversion reconstructs tau",
    all(SUM_C[n] == TAU[n] for n in range(1, N + 1)),
)

SUM_C_ODD = [0] * (N + 1)
for d in range(1, N + 1, 2):
    cd = C[d]
    if cd == 0:
        continue
    for k in range(1, N // d + 1):
        SUM_C_ODD[d * k] += cd
check(
    "S2-06 odd primitive spectrum reconstructs tau",
    all(SUM_C_ODD[n] == TAU[n] for n in range(1, N + 1)),
)

# S3. Complete Boolean expansion for every odd squarefree n in the audit range.
s3_ok = True
s3_cases = 0
for n in range(1, 8193, 2):
    if mu[n] == 0:
        continue
    ps = distinct_prime_factors(n)
    k = len(ps)
    total = 0
    for mask in range(1 << k):
        q = 1
        chosen = 0
        for j, p in enumerate(ps):
            if (mask >> j) & 1:
                q *= p
                chosen += 1
        sign = -1 if ((k - chosen) & 1) else 1
        total += sign * TAU[q]
    if total != C[n]:
        s3_ok = False
        break
    s3_cases += 1
check("S3-01 Boolean mixed-difference formula", s3_ok, f"cases={s3_cases}")
check(
    "S3-02 nonmultiplicativity guard",
    (C[3], C[5], C[15]) == (2, 2, -2) and C[15] != C[3] * C[5],
    "witness 3,5,15",
)

prime_filter_ok = True
prime_power_ok = True
for p in primes:
    if p == 2:
        continue
    if C[p] != TAU[p] + 1 or C[p] not in (0, 2):
        prime_filter_ok = False
    q = p
    prev = 1
    while q <= N:
        if C[q] != TAU[q] - TAU[prev] or C[q] not in (-2, 0, 2):
            prime_power_ok = False
            break
        if q > N // p:
            break
        prev = q
        q *= p
check("S3-03 odd-prime filter", prime_filter_ok)
check("S3-04 odd-prime-power filter", prime_power_ok)

# S4. Divisor-sum form of the odd Thue-Morse recurrence.
check(
    "S4-01 odd divisor recursion",
    all(SUM_C[2 * n + 1] == -SUM_C[n] for n in range(1, (N - 1) // 2 + 1)),
)

# S5. Coefficient audit of the product and odd Lambert bridge.
poly = [0] * (LAMBERT_N + 1)
poly[0] = 1
power = 1
while power <= LAMBERT_N:
    old = poly[:]
    for i in range(0, LAMBERT_N - power + 1):
        poly[i + power] -= old[i]
    power *= 2
check(
    "S5-01 finite Thue-Morse product coefficients",
    all(poly[n] == TAU[n] for n in range(0, LAMBERT_N + 1)),
)

lambert = [0] * (LAMBERT_N + 1)
for d in range(1, LAMBERT_N + 1, 2):
    cd = C[d]
    if cd == 0:
        continue
    for n in range(d, LAMBERT_N + 1, d):
        lambert[n] += cd
check(
    "S5-02 odd Lambert coefficients equal product minus one",
    all(lambert[n] == poly[n] == TAU[n] for n in range(1, LAMBERT_N + 1)),
)

# S6. Dirichlet products are coefficientwise the divisor-sum identities.
check(
    "S6-01 coefficient audit of zeta*C=T",
    all(SUM_C[n] == TAU[n] for n in range(1, N + 1)),
)
check(
    "S6-02 coefficient audit of zeta_odd*C=T_odd",
    all(SUM_C_ODD[n] == TAU[n] for n in range(1, N + 1, 2)),
)

# Extra exact scope guards, not additional theorem claims.
parity_size_ok = C[1] == -1
for n in range(2, N + 1):
    if C[n] & 1:
        parity_size_ok = False
        break
    if abs(C[n]) > (1 << omega[n]):
        parity_size_ok = False
        break
check("G-01 parity and size scope guard", parity_size_ok)

for label, passed, extra in CHECKS:
    print(("PASS " if passed else "FAIL ") + label + (("  " + extra) if extra else ""))

failures = [label for label, passed, _extra in CHECKS if not passed]
print(f"CHECKS {len(CHECKS)}")
if failures:
    print("DECISION MISMATCH")
    print("FAILURES " + " | ".join(failures))
    raise SystemExit(0)

print("DECISION BRIDGE-PASS")
raise SystemExit(0)
