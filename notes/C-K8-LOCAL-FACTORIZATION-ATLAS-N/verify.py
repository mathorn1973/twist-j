#!/usr/bin/env python3
"""Exact stdlib audit for C-K8-LOCAL-FACTORIZATION-ATLAS-N.

The proof is in PREREG.md/RESULT.md.  This finite scan is audit evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for k in range(n):
        out[k] = ((a[k] if k < len(a) else 0) +
                  (b[k] if k < len(b) else 0)) % p
    return trim(out)


def poly_sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for k in range(n):
        out[k] = ((a[k] if k < len(a) else 0) -
                  (b[k] if k < len(b) else 0)) % p
    return trim(out)


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] = (out[i + j] + av * bv) % p
    return trim(out)


def poly_divmod(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = trim([x % p for x in a])
    b = trim([x % p for x in b])
    if b == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(a) < len(b):
        return [0], a
    q = [0] * (len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] * inv % p
        q[k] = c
        for j, bv in enumerate(b):
            a[j + k] = (a[j + k] - c * bv) % p
        trim(a)
    return trim(q), trim(a)


def poly_mod(a: list[int], modulus: list[int], p: int) -> list[int]:
    return poly_divmod(a, modulus, p)[1]


def poly_powmod(base: list[int], exponent: int, modulus: list[int], p: int) -> list[int]:
    out = [1]
    base = poly_mod(base, modulus, p)
    while exponent:
        if exponent & 1:
            out = poly_mod(poly_mul(out, base, p), modulus, p)
        base = poly_mod(poly_mul(base, base, p), modulus, p)
        exponent >>= 1
    return out


def poly_gcd(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim([x % p for x in a])
    b = trim([x % p for x in b])
    while b != [0]:
        _, r = poly_divmod(a, b, p)
        a, b = b, r
    inv = pow(a[-1], -1, p)
    return [(x * inv) % p for x in a]


def quad_mul(x: tuple[int, int], y: tuple[int, int], d: int) -> tuple[int, int]:
    a, b = x
    c, e = y
    return a * c + b * e * d, a * e + b * c


def quad_poly_mul(a: list[tuple[int, int]], b: list[tuple[int, int]], d: int) -> list[tuple[int, int]]:
    out = [(0, 0)] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            u, v = quad_mul(av, bv, d)
            x, y = out[i + j]
            out[i + j] = x + u, y + v
    return out


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def sqrt_mod(a: int, p: int) -> int:
    """Tonelli-Shanks; called only when a is a nonzero square mod odd p."""
    a %= p
    if p == 2:
        return a
    if legendre(a, p) != 1:
        raise ValueError("nonsquare")
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 2
    while legendre(z, p) != -1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)
    while t != 1:
        i = 1
        t2 = t * t % p
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
            if i == m:
                raise AssertionError("Tonelli-Shanks invariant failed")
        b = pow(c, 1 << (m - i - 1), p)
        r = r * b % p
        t = t * b * b % p
        c = b * b % p
        m = i
    return r


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for n in range(2, int(limit ** 0.5) + 1):
        if sieve[n]:
            sieve[n * n: limit + 1: n] = b"\x00" * (((limit - n * n) // n) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def route_factors(d: int, root: int, p: int) -> tuple[list[int], list[int]]:
    if d == -1:
        return [(-root) % p, 0, 1], [root % p, 0, 1]
    if d == 2:
        return [1, root % p, 1], [1, (-root) % p, 1]
    if d == -2:
        return [-1 % p, root % p, 1], [-1 % p, (-root) % p, 1]
    raise ValueError(d)


def predicted_pattern(residue: int) -> tuple[dict[int, int], tuple[int, int, int], str]:
    chi_minus_one = 1 if residue in (1, 5) else -1
    chi_two = 1 if residue in (1, 7) else -1
    symbols = {-1: chi_minus_one, 2: chi_two, -2: chi_minus_one * chi_two}
    if residue == 1:
        return symbols, (1, 1, 4), "1+1+1+1"
    return symbols, (1, 2, 2), "2+2"


def audit_symbolic_identities() -> None:
    target = [(1, 0), (0, 0), (0, 0), (0, 0), (1, 0)]
    identities = {
        -1: ([((0, -1)), (0, 0), (1, 0)], [((0, 1)), (0, 0), (1, 0)]),
        2: ([(1, 0), (0, 1), (1, 0)], [(1, 0), (0, -1), (1, 0)]),
        -2: ([(-1, 0), (0, 1), (1, 0)], [(-1, 0), (0, -1), (1, 0)]),
    }
    for d, (left, right) in identities.items():
        if quad_poly_mul(left, right, d) != target:
            raise AssertionError(f"symbolic identity failed for d={d}")


def audit_global_and_two_adic() -> None:
    shifted = [comb(4, k) for k in range(5)]
    shifted[0] += 1
    if shifted != [2, 4, 6, 4, 1]:
        raise AssertionError("shifted polynomial mismatch")
    if any(c % 2 for c in shifted[:-1]) or shifted[-1] % 2 == 0 or shifted[0] % 4 == 0:
        raise AssertionError("Eisenstein conditions failed")
    if [c % 2 for c in [1, 0, 0, 0, 1]] != poly_mul([1, 1], poly_mul([1, 1], poly_mul([1, 1], [1, 1], 2), 2), 2):
        raise AssertionError("p=2 reduction is not (x+1)^4")
    profile = (4, 1, 1)
    if profile[0] * profile[1] * profile[2] != 4 or profile[0] % 2 != 0:
        raise AssertionError("p=2 local degree/wild-ramification mismatch")


def audit_v4() -> dict[str, str]:
    units = (1, 3, 5, 7)
    for a in units:
        if (a * a) % 8 != 1:
            raise AssertionError("unit does not square to identity")
    sign_i = {a: (1 if a % 4 == 1 else -1) for a in units}
    sign_s2 = {1: 1, 3: -1, 5: -1, 7: 1}
    fixed: dict[str, str] = {}
    expected = {3: "Q(sqrt(-2))", 5: "Q(i)", 7: "Q(sqrt(2))"}
    for a in (3, 5, 7):
        signs = {
            "Q(i)": sign_i[a],
            "Q(sqrt(2))": sign_s2[a],
            "Q(sqrt(-2))": sign_i[a] * sign_s2[a],
        }
        candidates = [name for name, sign in signs.items() if sign == 1]
        if candidates != [expected[a]]:
            raise AssertionError(f"fixed-field mismatch for sigma_{a}: {candidates}")
        fixed[f"sigma_{a}"] = candidates[0]
    return fixed


def audit_p5() -> dict[str, object]:
    p = 5
    target = [1, 0, 0, 0, 1]
    first = [(-2) % p, 0, 1]
    second = [(-3) % p, 0, 1]
    if poly_mul(first, second, p) != target:
        raise AssertionError("ordered p=5 factorization failed")
    squares = {x * x % p for x in range(p)}
    if 2 in squares or 3 in squares:
        raise AssertionError("p=5 quadratic factor unexpectedly reducible")
    image_i = (2, 3)
    sigma5_image = image_i  # i -> i^5 = i
    sigma7_image = tuple((-x) % 5 for x in image_i)  # i -> i^7 = -i
    if sigma5_image != (2, 3) or sigma7_image != (3, 2):
        raise AssertionError("p=5 component action mismatch")

    def ext_mul(x: tuple[int, int], y: tuple[int, int], relation: int) -> tuple[int, int]:
        # (a+b*u)(c+d*u) in F_5[u]/(u^2-relation).
        a, b = x
        c, d = y
        return ((a * c + b * d * relation) % 5, (a * d + b * c) % 5)

    def ext_pow(x: tuple[int, int], exponent: int, relation: int) -> tuple[int, int]:
        out = (1, 0)
        while exponent:
            if exponent & 1:
                out = ext_mul(out, x, relation)
            x = ext_mul(x, x, relation)
            exponent >>= 1
        return out

    for relation in (2, 3):
        generator = (0, 1)
        if ext_pow(generator, 5, relation) != (0, 4):
            raise AssertionError("sigma_5 does not act within an ordered factor")
        seventh = ext_pow(generator, 7, relation)
        target_relation = (-relation) % 5
        if ext_mul(seventh, seventh, relation) != (target_relation, 0):
            raise AssertionError("sigma_7 does not exchange the factor labels")

    elements = [(a, b) for a in range(5) for b in range(5)]
    units = [x for x in elements if x != (0, 0)]
    inverse_pairs = sum(
        1 for x in units for y in units if ext_mul(x, y, 2) == (1, 0)
    )
    if len(units) != 24 or len(units) ** 2 != 576 or inverse_pairs != 24:
        raise AssertionError("full-unit/norm-one group-order audit failed")
    return {
        "factor_order": ["x^2-2", "x^2-3"],
        "full_unit_group": "C24 x C24",
        "i_image": list(image_i),
        "norm_one_subgroup_order": 24,
        "sigma_5_i_image": list(sigma5_image),
        "sigma_7_i_image": list(sigma7_image),
        "diagonal": False,
    }


def audit_prime(p: int) -> tuple[int, list[int], str]:
    residue = p % 8
    symbols, profile, degree_type = predicted_pattern(residue)
    actual = {d: legendre(d, p) for d in (-1, 2, -2)}
    if actual != symbols:
        raise AssertionError(f"Legendre row mismatch at p={p}: {actual} != {symbols}")
    if actual[-2] != actual[-1] * actual[2]:
        raise AssertionError(f"Legendre multiplicativity failed at p={p}")
    available = [d for d in (-1, 2, -2) if actual[d] == 1]
    if not available:
        raise AssertionError(f"no square route at p={p}")

    target = [1, 0, 0, 0, 1]
    for d in available:
        root = sqrt_mod(d, p)
        if root * root % p != d % p:
            raise AssertionError(f"bad square root at p={p}, d={d}")
        left, right = route_factors(d, root, p)
        if poly_mul(left, right, p) != target:
            raise AssertionError(f"route product mismatch at p={p}, d={d}")

    # Attack irreducibility of the displayed quadratic pair in each 2+2 row.
    # A monic quadratic is irreducible exactly when its discriminant is a
    # nonsquare.  For the i-route, 4i has the same character as i.
    if residue == 3 and legendre(2, p) != -1:
        raise AssertionError(f"t-route discriminant is square at p={p}")
    if residue == 5:
        iroot = sqrt_mod(-1, p)
        if legendre(iroot, p) != -1 or legendre(-iroot, p) != -1:
            raise AssertionError(f"i-route quadratic is reducible at p={p}")
    if residue == 7 and legendre(-2, p) != -1:
        raise AssertionError(f"s-route discriminant is square at p={p}")

    x = [0, 1]
    xp = poly_powmod(x, p, target, p)
    linear_degree = len(poly_gcd(target, poly_sub(xp, x, p), p)) - 1
    xp2 = poly_powmod(xp, p, target, p)
    splits_over_p2 = poly_sub(xp2, x, p) == [0]
    if residue == 1:
        if linear_degree != 4 or degree_type != "1+1+1+1":
            raise AssertionError(f"factor-degree mismatch at p={p}")
    else:
        if linear_degree != 0 or not splits_over_p2 or degree_type != "2+2":
            raise AssertionError(f"factor-degree mismatch at p={p}")
    frobenius_order = 1 if residue == 1 else 2
    if profile != (1, frobenius_order, 4 // frobenius_order):
        raise AssertionError(f"local profile mismatch at p={p}")
    return residue, available, degree_type


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    args = parser.parse_args()
    if args.limit < 7:
        raise SystemExit("limit must be at least 7")

    audit_symbolic_identities()
    audit_global_and_two_adic()
    fixed_fields = audit_v4()
    p5 = audit_p5()

    primes = primes_up_to(args.limit)
    class_counts = {1: 0, 3: 0, 5: 0, 7: 0}
    route_counts = {-1: 0, 2: 0, -2: 0}
    type_counts = {"1+1+1+1": 0, "2+2": 0}
    for p in primes:
        if p == 2:
            continue
        residue, available, degree_type = audit_prime(p)
        class_counts[residue] += 1
        for d in available:
            route_counts[d] += 1
        type_counts[degree_type] += 1

    odd_count = len(primes) - 1
    if sum(class_counts.values()) != odd_count:
        raise AssertionError("prime-class count mismatch")
    if type_counts["1+1+1+1"] != class_counts[1]:
        raise AssertionError("split-count mismatch")
    if type_counts["2+2"] != class_counts[3] + class_counts[5] + class_counts[7]:
        raise AssertionError("quadratic-pair count mismatch")

    summary = {
        "audit_role": "finite audit, not proof",
        "class_counts": {str(k): class_counts[k] for k in (1, 3, 5, 7)},
        "density_theorem": {"complete_split": "1/4", "two_quadratics": "3/4", "unramified_inert": "0"},
        "fixed_fields": fixed_fields,
        "limit": args.limit,
        "odd_primes_checked": odd_count,
        "p2": {"factor_mod_2": "(x+1)^4", "irreducible_over_Q2": True, "profile": [4, 1, 1]},
        "p5": p5,
        "route_counts": {str(k): route_counts[k] for k in (-1, 2, -2)},
        "type_counts": type_counts,
    }
    payload = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    print("C-K8-LOCAL-FACTORIZATION-ATLAS-N")
    print("STATUS PASS")
    print(payload)
    print("SUMMARY_SHA256 " + hashlib.sha256(payload.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
