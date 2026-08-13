#!/usr/bin/env python3
"""Exact support/label/phase breaker for the pinned AME(4,6) tensor.

Scientific arithmetic here is discrete: every nonzero entry is represented by
its amplitude label a/b/c and its exponent of w=zeta_20.  No floating point is
used.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from itertools import permutations, product
from pathlib import Path
import hashlib
import re

PIN_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"


def parse_rows(block: str, allowed: str):
    rows = [r.strip() for r in block.split(";") if r.strip()]
    out = []
    for n, row in enumerate(rows):
        toks = re.findall(allowed, row)
        if len(toks) != 36:
            raise ValueError(f"row {n}: expected 36 tokens, found {len(toks)}")
        out.append(toks)
    if len(out) != 36:
        raise ValueError(f"expected 36 rows, found {len(out)}")
    return out


def parse_source(path: Path):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    m = re.search(
        r"U\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        text,
        flags=re.S,
    )
    if not m:
        raise ValueError("matrix blocks not found")
    amps = parse_rows(m.group(1), r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])")
    exps = parse_rows(m.group(2), r"(?<![A-Za-z0-9_])(?:[0-9]|1[0-9])(?![A-Za-z0-9_])")
    A = {}
    for row in range(36):
        for col in range(36):
            lab = amps[row][col]
            if lab != "0":
                i, j = divmod(row, 6)
                k, l = divmod(col, 6)
                A[(i, j, k, l)] = (lab, int(exps[row][col]) % 20)
    return raw, A


def cycles(p):
    seen = set()
    cs = []
    for i in range(len(p)):
        if i not in seen:
            c = []
            j = i
            while j not in seen:
                seen.add(j)
                c.append(j)
                j = p[j]
            if len(c) > 1:
                cs.append("(" + " ".join(map(str, c)) + ")")
    return "".join(cs) or "()"


def transformed_index(x, sigma, legperm):
    # Enough for exhaustive S4 classification; inverse convention gives same set.
    return tuple(sigma[x[legperm[q]]] for q in range(4))


def projective_check(A, sigma, legperm):
    support = A.keys()
    delta = None
    for x in support:
        y = transformed_index(x, sigma, legperm)
        if y not in A:
            return None
        lab0, e0 = A[x]
        lab1, e1 = A[y]
        if lab0 != lab1:
            return None
        d = (e1 - e0) % 20
        if delta is None:
            delta = d
        elif d != delta:
            return None
    return delta


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def generated_group(gens, n):
    ident = tuple(range(n))
    seen = {ident}
    todo = deque([ident])
    while todo:
        x = todo.popleft()
        for g in gens:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def value_preserving_permutations(values):
    """All p with values[p[x]] == values[x]."""
    buckets = defaultdict(list)
    for x, value in enumerate(values):
        buckets[value].append(x)
    ordered = [buckets[v] for v in sorted(buckets)]
    ans = []
    for images in product(*(list(permutations(b)) for b in ordered)):
        p = list(range(len(values)))
        for domain, image in zip(ordered, images):
            for x, y in zip(domain, image):
                p[x] = y
        ans.append(tuple(p))
    return ans


def independent_label_support_check(A, ps):
    for x, value in A.items():
        y = tuple(ps[q][x[q]] for q in range(4))
        if y not in A or A[y][0] != value[0]:
            return False
    return True


def permutation_order(p):
    from math import gcd
    ans = 1
    seen = set()
    for x in range(len(p)):
        if x not in seen:
            n = 0
            y = x
            while y not in seen:
                seen.add(y)
                n += 1
                y = p[y]
            ans = ans * n // gcd(ans, n)
    return ans


def congruence_solvable_prime_power(coeffs, rhs, modulus, prime):
    """Existence for A*x=b mod p^k using exact unit-pivot elimination.

    If no unit pivot remains, every coefficient is divisible by p, so the
    residual system descends one p-adic level iff every residual RHS does.
    """
    rows = [([x % modulus for x in row], b % modulus) for row, b in zip(coeffs, rhs)]

    def rec(rows, mod):
        if mod == 1:
            return True
        cleaned = []
        for a, b in rows:
            if all(x % mod == 0 for x in a):
                if b % mod:
                    return False
            else:
                cleaned.append(([x % mod for x in a], b % mod))
        rows = cleaned
        if not rows:
            return True
        nvars = len(rows[0][0])
        pivot = None
        for ri, (a, _b) in enumerate(rows):
            for ci, x in enumerate(a):
                if x % prime:
                    pivot = (ri, ci)
                    break
            if pivot:
                break
        if pivot is None:
            divided = []
            for a, b in rows:
                if b % prime:
                    return False
                divided.append(([x // prime for x in a], b // prime))
            return rec(divided, mod // prime)

        ri, ci = pivot
        pa, pb = rows[ri]
        inv = pow(pa[ci], -1, mod)
        reduced = []
        for rj, (a, b) in enumerate(rows):
            if rj == ri:
                continue
            factor = (a[ci] * inv) % mod
            na = [(a[k] - factor * pa[k]) % mod for k in range(nvars)]
            nb = (b - factor * pb) % mod
            del na[ci]
            reduced.append((na, nb))
        return rec(reduced, mod)

    return rec(rows, modulus)


def monomial_phase_equations(A, ps):
    # A monomial action sends x to y=(p_q(x_q)); diagonal exponents are
    # variables in Z/40 and the final variable is the global projective phase.
    indices = []
    coeffs = []
    rhs = []
    for x, (_lab, ex) in A.items():
        y = tuple(ps[q][x[q]] for q in range(4))
        _laby, ey = A[y]
        row = [0] * 25
        for q in range(4):
            row[6 * q + y[q]] += 1
        row[24] = -1
        indices.append(x)
        coeffs.append(row)
        rhs.append((2 * (ey - ex)) % 40)
    return indices, coeffs, rhs


def monomial_mu40_phase_lift(A, ps):
    _indices, coeffs, rhs = monomial_phase_equations(A, ps)
    mod5 = congruence_solvable_prime_power(coeffs, rhs, 5, 5)
    mod8 = congruence_solvable_prime_power(coeffs, rhs, 8, 2)
    return mod5, mod8, mod5 and mod8, rank_mod_prime(coeffs, 5), rank_mod_prime(
        [row + [b] for row, b in zip(coeffs, rhs)], 5
    )


def inconsistency_certificate_mod_prime(coeffs, rhs, p):
    """Return lambda with lambda*A=0 and lambda*b != 0, if one is exposed."""
    m = len(coeffs)
    n = len(coeffs[0])
    rows = []
    for i, (a, b) in enumerate(zip(coeffs, rhs)):
        rows.append(
            [x % p for x in a]
            + [b % p]
            + [1 if i == j else 0 for j in range(m)]
        )
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if rows[i][c] % p), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][c] % p, -1, p)
        rows[r] = [(inv * x) % p for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][c] % p:
                factor = rows[i][c] % p
                rows[i] = [(x - factor * y) % p for x, y in zip(rows[i], rows[r])]
        r += 1
    for row in rows:
        if all(x % p == 0 for x in row[:n]) and row[n] % p:
            lam = row[n + 1 :]
            assert all(
                sum(lam[i] * coeffs[i][j] for i in range(m)) % p == 0
                for j in range(n)
            )
            assert sum(lam[i] * rhs[i] for i in range(m)) % p != 0
            return lam
    return None


def rank_mod_prime(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(inv * x) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    raw, A = parse_source(args.source)
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == PIN_SHA256
    print("SOURCE_SHA256", digest)
    print("SOURCE_BYTES", len(raw))
    print("NONZERO", len(A))
    print("AMPLITUDE_COUNTS", dict(sorted(Counter(v[0] for v in A.values()).items())))
    print("PHASE_EXPONENT_COUNTS", dict(sorted(Counter(v[1] for v in A.values()).items())))
    per_leg = []
    for q in range(4):
        per_leg.append(tuple(sum(1 for x in A if x[q] == z) for z in range(6)))
    print("SUPPORT_DEGREES_BY_LEG", per_leg)

    S6 = list(permutations(range(6)))
    S4 = list(permutations(range(4)))
    ident4 = tuple(range(4))

    strict = []
    all_stab = []
    by_legperm = Counter()
    for sigma in S6:
        for pi in S4:
            d = projective_check(A, sigma, pi)
            if d is not None:
                rec = (sigma, pi, d)
                all_stab.append(rec)
                by_legperm[pi] += 1
                if pi == ident4:
                    strict.append(rec)

    print("STRICT_DIAGONAL_PROJECTIVE_ORDER", len(strict))
    for sigma, pi, d in strict:
        print("STRICT", cycles(sigma), "sigma=", sigma, "chi=zeta20^", d)
    print("SIMULTANEOUS_S6_X_LEGPERM_S4_PROJECTIVE_COUNT", len(all_stab))
    print("ADMITTED_LEG_PERMUTATIONS", len(by_legperm))
    for pi, count in sorted(by_legperm.items()):
        print("LEG", cycles(pi), "pi=", pi, "sigma_count=", count)

    strict_perms = [x[0] for x in strict]
    G = generated_group(strict_perms, 6)
    print("STRICT_GENERATED_PERMUTATION_GROUP_ORDER", len(G))
    assert len(G) == len(set(strict_perms))
    print("STRICT_CONTAINS_ORDER60", len(G) >= 60 and len(G) % 60 == 0)

    # The complete independent-permutation search can be reduced, without
    # assumptions, to the per-leg degree classes of the colored support.
    candidates = [value_preserving_permutations(d) for d in per_leg]
    print("INDEPENDENT_DEGREE_PRESERVING_SEARCH_SIZE", tuple(map(len, candidates)))
    independent = []
    for ps in product(*candidates):
        if independent_label_support_check(A, ps):
            independent.append(ps)
    print("INDEPENDENT_LABEL_SUPPORT_AUTOMORPHISMS", len(independent))
    for n, ps in enumerate(independent):
        phase_lift = monomial_mu40_phase_lift(A, ps)
        print(
            "IND_SUPPORT",
            n,
            "orders=", tuple(permutation_order(p) for p in ps),
            "cycles=", tuple(cycles(p) for p in ps),
            "mu40_lift=(mod5,mod8,total,rank5,rank5_aug)=", phase_lift,
            "perms=", ps,
        )
        if not phase_lift[0]:
            indices, coeffs, rhs = monomial_phase_equations(A, ps)
            cert = inconsistency_certificate_mod_prime(coeffs, rhs, 5)
            assert cert is not None
            sparse = [(indices[i], z) for i, z in enumerate(cert) if z]
            print("MU40_MOD5_LEFT_NULL_CERTIFICATE", sparse)

    max_degree_multiplicity = tuple(max(Counter(d).values()) for d in per_leg)
    print("MAX_EQUAL_SUPPORT_DEGREE_MULTIPLICITY_BY_LEG", max_degree_multiplicity)
    print("ORDER5_LOCAL_PERMUTATION_POSSIBLE_BY_DEGREE", tuple(m >= 5 for m in max_degree_multiplicity))
    has_5_on_all_legs = any(all(permutation_order(p) == 5 for p in ps) for ps in independent)
    print("INDEPENDENT_SUPPORT_HAS_ORDER5_ON_ALL_LEGS", has_5_on_all_legs)
    print("A5_SIX_POINT_ACTION_SURVIVES_SUPPORT", has_5_on_all_legs)
    assert not has_5_on_all_legs
    print("RESULT G3_STRICT_ORDER=1 G4=FALSIFIER_FIRED")


if __name__ == "__main__":
    main()
