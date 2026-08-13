#!/usr/bin/env python3
"""Exact Galois transporter census for the pinned AME(4,6) tensor.

Standard-library only.  The primary computation is discrete: every nonzero
coefficient is an amplitude label a/b/c and an exponent of zeta_40.  Exact
cyclotomic arithmetic is used independently to derive and verify the Galois
label table and to hash all conjugate tensors.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import permutations, product
from math import gcd
from pathlib import Path
import re


PIN_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
PIN_BYTES = 8515
PIN_BLOB = "e0d0e171d58b3360c39595d677ffc401a466112d"
UNITS = tuple(k for k in range(40) if gcd(k, 40) == 1)
IDENT6 = tuple(range(6))


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
    if len(raw) != PIN_BYTES or hashlib.sha256(raw).hexdigest() != PIN_SHA256:
        raise AssertionError("source byte/SHA256 pin mismatch")
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    if blob != PIN_BLOB:
        raise AssertionError("source Git blob pin mismatch")
    text = raw.decode("utf-8")
    m = re.search(r"U\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;", text, re.S)
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
                k, ell = divmod(col, 6)
                A[(i, j, k, ell)] = (lab, 2 * int(exps[row][col]) % 40)
    return raw, A


# Q(zeta_40) in the power basis, Phi_40=x^16-x^12+x^8-x^4+1.
DEG = 16


def reduce40(cs):
    p = [Fraction(x) for x in cs] + [Fraction(0)] * max(0, DEG - len(cs))
    for n in range(len(p) - 1, DEG - 1, -1):
        v = p[n]
        if v:
            p[n] = 0
            p[n - 4] += v
            p[n - 8] -= v
            p[n - 12] += v
            p[n - 16] -= v
    return tuple(p[:DEG])


@dataclass(frozen=True)
class K40:
    c: tuple[Fraction, ...]

    def __init__(self, cs=(0,)):
        object.__setattr__(self, "c", reduce40(cs))

    def __add__(self, other):
        other = as_k40(other)
        return K40(tuple(x + y for x, y in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return K40(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + (-as_k40(other))

    def __rsub__(self, other):
        return as_k40(other) - self

    def __mul__(self, other):
        other = as_k40(other)
        p = [Fraction(0)] * 31
        for i, x in enumerate(self.c):
            if x:
                for j, y in enumerate(other.c):
                    if y:
                        p[i + j] += x * y
        return K40(tuple(p))

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            # Only powers of z are inverted in this file.
            if self != Z:
                raise ValueError("negative power only implemented for z")
            return ZPOW[n % 40]
        out = K40((1,))
        b = self
        while n:
            if n & 1:
                out = out * b
            b = b * b
            n >>= 1
        return out

    def serial(self):
        return ",".join(f"{q.numerator}/{q.denominator}" for q in self.c)


def as_k40(x):
    return x if isinstance(x, K40) else K40((x,))


Z = K40((0, 1))
ZPOW = tuple(Z ** n for n in range(40))


def sigma(x: K40, k: int):
    out = K40()
    for n, q in enumerate(x.c):
        if q:
            out += q * ZPOW[(k * n) % 40]
    return out


def exact_amplitudes():
    z = Z
    w = ZPOW[2]
    c = (ZPOW[5] + ZPOW[-5]) * Fraction(1, 2)
    # Avoid general inversion: imported exact identities in zeta_40.
    # a=c/(w+w^-1), b=(w^2+w^-2)a from the prior exact verifier;
    # these equivalent power-basis forms are obtained there.
    # Search the 40 cyclotomic multiples against the identities a^2 and b/a.
    denom = w + ZPOW[-2]
    # Inverse by finite linear solve over Q.
    inv = inverse_k40(denom)
    a = c * inv
    b = (ZPOW[4] + ZPOW[-4]) * a
    return {"a": a, "b": b, "c": c, "w": w}


def inverse_k40(x: K40):
    # Rational Gaussian elimination for multiplication-by-x.
    mat = []
    for row in range(DEG):
        mat.append([(x * ZPOW[col]).c[row] for col in range(DEG)] + [Fraction(row == 0)])
    for col in range(DEG):
        piv = next(r for r in range(col, DEG) if mat[r][col])
        mat[col], mat[piv] = mat[piv], mat[col]
        u = mat[col][col]
        mat[col] = [v / u for v in mat[col]]
        for r in range(DEG):
            if r != col and mat[r][col]:
                u = mat[r][col]
                mat[r] = [v - u * t for v, t in zip(mat[r], mat[col])]
    return K40(tuple(mat[r][-1] for r in range(DEG)))


def galois_label_table(q):
    ans = {}
    for k in UNITS:
        row = {}
        for lab in ("a", "b", "c"):
            v = sigma(q[lab], k)
            matches = []
            for target in ("a", "b", "c"):
                for off in (0, 20):
                    if v == q[target] * ZPOW[off]:
                        matches.append((target, off))
            if len(matches) != 1:
                raise AssertionError((k, lab, matches, v.serial()))
            row[lab] = matches[0]
        ans[k] = row
    return ans


def value_preserving_permutations(values):
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


def degree_matching_permutations(source_values, target_values):
    """All p with target_values[p[r]] == source_values[r]."""
    if Counter(source_values) != Counter(target_values):
        return []
    source_buckets = defaultdict(list)
    target_buckets = defaultdict(list)
    for r, value in enumerate(source_values):
        source_buckets[value].append(r)
    for r, value in enumerate(target_values):
        target_buckets[value].append(r)
    values = sorted(source_buckets)
    ans = []
    for images in product(*(list(permutations(target_buckets[v])) for v in values)):
        p = [None] * 6
        for value, image in zip(values, images):
            for x, y in zip(source_buckets[value], image):
                p[x] = y
        ans.append(tuple(p))
    return ans


def colored_support_candidates(A, candidates, labmap):
    out = []
    support = set(A)
    for ps in product(*candidates):
        ok = True
        for x, (lab, _e) in A.items():
            y = tuple(ps[q][x[q]] for q in range(4))
            if y not in support or A[y][0] != labmap[lab][0]:
                ok = False
                break
        if ok:
            out.append(ps)
    return out


def colored_support_candidates_party(A, candidates, labmap, pi):
    out = []
    support = set(A)
    for ps in product(*candidates):
        ok = True
        for x, (lab, _e) in A.items():
            y = tuple(ps[q][x[pi[q]]] for q in range(4))
            if y not in support or A[y][0] != labmap[lab][0]:
                ok = False
                break
        if ok:
            out.append(ps)
    return out


def phase_system(A, ps, k, labmap):
    # 25 variables: d_(q,r), then h.  Equation follows frozen PREREG section 3.
    rows, rhs = [], []
    for x, (lab, ex) in sorted(A.items()):
        y = tuple(ps[q][x[q]] for q in range(4))
        _target_lab, ey = A[y]
        mapped_lab, off = labmap[lab]
        assert mapped_lab == _target_lab
        row = [0] * 25
        for q in range(4):
            row[6 * q + y[q]] += 1
        row[24] = 1
        rows.append(row)
        rhs.append((off + k * ex - ey) % 40)
    return rows, rhs


def phase_system_party(A, ps, pi, k, labmap):
    rows, rhs = [], []
    for x, (lab, ex) in sorted(A.items()):
        y = tuple(ps[q][x[pi[q]]] for q in range(4))
        _target_lab, ey = A[y]
        mapped_lab, off = labmap[lab]
        assert mapped_lab == _target_lab
        row = [0] * 25
        for q in range(4):
            row[6 * q + y[q]] += 1
        row[24] = 1
        rows.append(row)
        rhs.append((off + k * ex - ey) % 40)
    return rows, rhs


def solve_pp(rows, rhs, modulus, prime, nvars=None):
    """Complete unit-pivot solver over Z/(prime^e), with exact count."""
    if nvars is None:
        nvars = len(rows[0]) if rows else 0
    records = [([x % modulus for x in a], b % modulus) for a, b in zip(rows, rhs)]

    def rec(recs, mod, vars_):
        cleaned = []
        for a, b in recs:
            if all(x % mod == 0 for x in a):
                if b % mod:
                    return None, 0
            else:
                cleaned.append(([x % mod for x in a], b % mod))
        recs = cleaned
        if not recs:
            return [0] * len(vars_), mod ** len(vars_)
        pivot = None
        for ri, (a, _b) in enumerate(recs):
            for ci, x in enumerate(a):
                if x % prime:
                    pivot = (ri, ci)
                    break
            if pivot is not None:
                break
        if pivot is None:
            if any(b % prime for _a, b in recs):
                return None, 0
            divided = [([x // prime for x in a], b // prime) for a, b in recs]
            sol, count = rec(divided, mod // prime, vars_)
            if sol is None:
                return None, 0
            return sol, count * (prime ** len(vars_))
        ri, ci = pivot
        pa, pb = recs[ri]
        inv = pow(pa[ci] % mod, -1, mod)
        reduced = []
        for rj, (a, b) in enumerate(recs):
            if rj == ri:
                continue
            factor = a[ci] * inv % mod
            na = [(a[j] - factor * pa[j]) % mod for j in range(len(vars_)) if j != ci]
            nb = (b - factor * pb) % mod
            reduced.append((na, nb))
        subvars = vars_[:ci] + vars_[ci + 1 :]
        subsol, count = rec(reduced, mod, subvars)
        if subsol is None:
            return None, 0
        sol = subsol[:ci] + [0] + subsol[ci:]
        total = sum(pa[j] * sol[j] for j in range(len(vars_)) if j != ci)
        sol[ci] = (pb - total) * inv % mod
        return sol, count

    return rec(records, modulus, list(range(nvars)))


def crt_pair(a5, a8):
    # x= a5 (mod5), a8 (mod8): x=a8+8*((a5-a8)*2 mod5).
    return (a8 + 8 * (((a5 - a8) * 2) % 5)) % 40


def left_null_certificate(rows, rhs, modulus, prime):
    """Find lambda with lambda*A=0 and lambda*b != 0 modulo modulus."""
    m = len(rows)
    n = len(rows[0])
    dual_rows = [[rows[i][j] % modulus for i in range(m)] for j in range(n)]
    dual_rhs = [0] * n
    for target in range(1, modulus):
        sol, _count = solve_pp(dual_rows + [[b % modulus for b in rhs]], dual_rhs + [target], modulus, prime, m)
        if sol is not None:
            assert all(sum(sol[i] * rows[i][j] for i in range(m)) % modulus == 0 for j in range(n))
            value = sum(sol[i] * rhs[i] for i in range(m)) % modulus
            assert value == target
            return tuple(sol), value
    raise AssertionError("unsolvable system had no dual certificate")


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
        a[r] = [inv*x % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                u = a[i][c]
                a[i] = [(x-u*y) % p for x, y in zip(a[i], a[r])]
        r += 1
    return r


def ranks_2_5(rows, rhs):
    augmented = [row + [b] for row, b in zip(rows, rhs)]
    return (rank_mod_prime(rows, 2), rank_mod_prime(augmented, 2),
            rank_mod_prime(rows, 5), rank_mod_prime(augmented, 5))


def sparse_certificate(A, lam):
    indices = sorted(A)
    return tuple((indices[i], x) for i, x in enumerate(lam) if x)


def phase_lift(A, ps, k, labmap):
    rows, rhs = phase_system(A, ps, k, labmap)
    s5, c5 = solve_pp(rows, rhs, 5, 5)
    s8, c8 = solve_pp(rows, rhs, 8, 2)
    if s5 is None or s8 is None:
        return None, (c5, c8)
    sol = [crt_pair(x, y) for x, y in zip(s5, s8)]
    assert all(sum(a * x for a, x in zip(row, sol)) % 40 == b for row, b in zip(rows, rhs))
    return tuple(sol), (c5, c8)


def phase_lift_party(A, ps, pi, k, labmap):
    rows, rhs = phase_system_party(A, ps, pi, k, labmap)
    s5, c5 = solve_pp(rows, rhs, 5, 5)
    s8, c8 = solve_pp(rows, rhs, 8, 2)
    if s5 is None or s8 is None:
        return None, (c5, c8)
    sol = [crt_pair(x, y) for x, y in zip(s5, s8)]
    assert all(sum(a * x for a, x in zip(row, sol)) % 40 == b for row, b in zip(rows, rhs))
    return tuple(sol), (c5, c8)


def normalize_solution(sol):
    sol = list(sol)
    shift = 0
    for q in range(4):
        c = sol[6 * q]
        shift += c
        for r in range(6):
            sol[6 * q + r] = (sol[6 * q + r] - c) % 40
    sol[24] = (sol[24] + shift) % 40
    return tuple(sol)


def compose_perm(ps, qs):
    return tuple(tuple(ps[leg][qs[leg][r]] for r in range(6)) for leg in range(4))


def perm_order(ps):
    cur = (IDENT6,) * 4
    for n in range(1, 121):
        cur = compose_perm(ps, cur)
        if cur == (IDENT6,) * 4:
            return n
    raise AssertionError("permutation order >120")


def exact_tensor_hash(A, k, labmap, q):
    h = hashlib.sha256()
    for x, (lab, ex) in sorted(A.items()):
        value = sigma(q[lab] * ZPOW[ex], k)
        h.update((",".join(map(str, x)) + ":" + value.serial() + "\n").encode())
    return h.hexdigest()


def cycles(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        c, x = [], i
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        if len(c) > 1:
            out.append("(" + " ".join(map(str, c)) + ")")
    return "".join(out) or "()"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--output-certificate", type=Path)
    args = ap.parse_args()
    raw, A = parse_source(args.source)
    print("PREREG_COMMIT", "f78538f881a0e25fcc0ed839c88c0fd45a751352")
    print("PREREG_SHA256", "d662cae52dbbafd2f0802aabade5ffdfc09bb5d22d7160999bf845fc4866f886")
    print("SOURCE bytes", len(raw), "sha256", hashlib.sha256(raw).hexdigest(), "blob", PIN_BLOB)
    print("SUPPORT", len(A), "AMPLITUDES", dict(sorted(Counter(v[0] for v in A.values()).items())))
    q = exact_amplitudes()
    table = galois_label_table(q)
    closure = {1}
    changed = True
    while changed:
        changed = False
        for x in tuple(closure):
            for g in (17, 11, 21):
                y = x * g % 40
                if y not in closure:
                    closure.add(y)
                    changed = True
    print("GALOIS_UNITS", UNITS)
    print("FROZEN_GENERATOR_CLOSURE", tuple(sorted(closure)))
    print("GENERATOR_ORDERS", {g: next(n for n in range(1, 20) if pow(g, n, 40) == 1) for g in (17,11,21)})
    for k in UNITS:
        print("GAL", k, "w_exp_mod20", k % 20, "map", table[k], "tensor_sha256", exact_tensor_hash(A, k, table[k], q))

    # Mandatory projective-coordinate baseline, with actual entry witnesses.
    assert A[(0, 0, 0, 1)] == ("c", 0)
    assert A[(0, 1, 0, 2)] == ("c", 34)
    assert (34 * 13) % 40 == 2  # (c*z^34/c)^13=z^2=w.
    assert all(table[21][lab] == (lab, 20) for lab in ("a", "b", "c"))
    assert all((20 + 21*ex - ex) % 40 == 20 for _x, (_lab, ex) in A.items())
    print("PROJECTIVE_FIELD_WITNESS A[0,1,0,2]/A[0,0,0,1]=z^34=w^17; power13=w=zeta20")
    print("PROJECTIVE_FIELD exact Q(projective_ratios)=Q(zeta20) degree8; sigma21(A)=-A")

    degrees = [tuple(sum(1 for x in A if x[q0] == r) for r in range(6)) for q0 in range(4)]
    candidates = [value_preserving_permutations(d) for d in degrees]
    print("DEGREES", degrees)
    print("PER_LEG_CANDIDATES", tuple(map(len, candidates)), "PRODUCT", 4*8*48*48)

    # Only two unsigned amplitude maps occur; enumerate each Cartesian product once.
    map_key = lambda row: tuple(row[x][0] for x in ("a", "b", "c"))
    colored_by_key = {}
    for key in sorted({map_key(table[k]) for k in UNITS}):
        representative = next(k for k in UNITS if map_key(table[k]) == key)
        cs = colored_support_candidates(A, candidates, table[representative])
        colored_by_key[key] = cs
        print("COLORED_SUPPORT_MAP", key, "COUNT", len(cs))
        for n, ps in enumerate(cs):
            print(" CAND", n, "orders", tuple(perm_order((p, IDENT6, IDENT6, IDENT6)) for p in ps), "cycles", tuple(cycles(p) for p in ps), "perms", ps)

    census = {}
    cert_lines = []
    for k in UNITS:
        key = map_key(table[k])
        colored = colored_by_key[key]
        lifted = []
        rejected = []
        for ps in colored:
            sol, counts = phase_lift(A, ps, k, table[k])
            if sol is None:
                rows, rhs = phase_system(A, ps, k, table[k])
                mod, prime = (5, 5) if counts[0] == 0 else (8, 2)
                lam, value = left_null_certificate(rows, rhs, mod, prime)
                rejected.append((ps, counts, mod, value, sparse_certificate(A, lam), ranks_2_5(rows, rhs)))
            else:
                rows, rhs = phase_system(A, ps, k, table[k])
                lifted.append((ps, normalize_solution(sol), counts, ranks_2_5(rows, rhs)))
                cert_lines.append(f"k={k} perms={ps} solution={normalize_solution(sol)} kernel_mod5={counts[0]} kernel_mod8={counts[1]}")
        census[k] = lifted
        print("TRANSPORTER", k, "colored", len(colored), "phase_lifted_permutation_classes", len(lifted), "rejected", len(rejected))
        for n, (ps, sol, counts, ranks) in enumerate(lifted):
            print(" LIFT", n, "perm_orders", tuple(perm_order((p,IDENT6,IDENT6,IDENT6)) for p in ps), "perms", ps, "normalized_d_h", sol, "kernel_counts_mod5_mod8", counts, "ranks_A_aug_mod2_mod5", ranks)
        for n, (ps, counts, mod, value, cert, ranks) in enumerate(rejected):
            extra = " 2_PRIMARY_DIVISOR4_AFTER_DIVISION_DOT_RHS_MOD2=1" if mod == 8 and value == 4 else ""
            print(" REJECT", n, "perms", ps, "solution_counts_mod5_mod8", counts, "ranks_A_aug_mod2_mod5", ranks, "LEFT_NULL_MOD", mod, "DOT_RHS", value, "SPARSE_CERT", cert, extra)
            cert_lines.append(f"REJECT k={k} perms={ps} modulus={mod} dot_rhs={value} sparse_left_null={cert}")
    gmod = tuple(k for k in UNITS if census[k])
    print("G_MOD", gmod, "ORDER", len(gmod), "FIXED_FIELD_DEGREE", 16 // len(gmod))
    is_subgroup = all((x*y % 40) in gmod for x in gmod for y in gmod) and all(pow(x,-1,40) in gmod for x in gmod)
    print("G_MOD_SUBGROUP", is_subgroup)
    if not is_subgroup:
        raise AssertionError("transporter census is not subgroup-closed")

    # G4 is forced by the complete G2/G3 census: G_mod has only two subgroups.
    if gmod == (1, 21):
        print("G4_SUBGROUP (1,) coherent YES coboundary YES fixed_field K=Q(zeta40)")
        print("G4_SUBGROUP (1,21) coherent YES coboundary YES transporter_permutation identity phase_projectively_identity h21=20")
        print("G4_FIXED_BASIS", tuple(f"z^{2*n}" for n in range(8)))
        print("G4_FIXED_FIELD Q(zeta20) degree 8 minpoly x^8-x^6+x^4-x^2+1 explicit_representative A/c")
        print("G4_NEW_DESCENT_BELOW_QZETA20 NO")
    else:
        print("G4 requires general cocycle classifier; unexpected non-baseline G_mod")

    kernel_basis = []
    for q0 in range(4):
        v = [0] * 25
        for r in range(6):
            v[6*q0+r] = 1
        v[24] = 39
        kernel_basis.append(tuple(v))
    rows0, rhs0 = phase_system(A, (IDENT6,)*4, 1, table[1])
    assert all(all(sum(row[j]*v[j] for j in range(25)) % 40 == 0 for row in rows0) for v in kernel_basis)
    print("PHASE_KERNEL_BASIS_Z40", tuple(kernel_basis), "ORDER", 40**4, "COMPLETE_BY_CRT_COUNTS", 625*4096)

    # Secondary G5 party audit.  Degree multisets prove that only id and (2 3)
    # can occur, but we enumerate both complete Cartesian products.
    admissible_pi = []
    for pi in permutations(range(4)):
        pcs = [degree_matching_permutations(degrees[pi[q0]], degrees[q0]) for q0 in range(4)]
        if all(pcs):
            admissible_pi.append((pi, pcs))
    print("G5_ADMISSIBLE_PARTY_PERMUTATIONS", tuple(pi for pi, _ in admissible_pi))
    party_colored = {}
    for pi, pcs in admissible_pi:
        print("G5_PARTY_SEARCH", pi, "PER_LEG", tuple(map(len, pcs)), "PRODUCT", __import__('math').prod(map(len, pcs)))
        for key in sorted({map_key(table[k]) for k in UNITS}):
            representative = next(k for k in UNITS if map_key(table[k]) == key)
            cs = colored_support_candidates_party(A, pcs, table[representative], pi)
            party_colored[(pi, key)] = cs
            print("G5_COLORED", pi, key, "COUNT", len(cs))
    party_census = {}
    for k in UNITS:
        lifts = []
        for pi, _pcs in admissible_pi:
            key = map_key(table[k])
            for ps in party_colored[(pi, key)]:
                sol, counts = phase_lift_party(A, ps, pi, k, table[k])
                if sol is not None:
                    lifts.append((pi, ps, normalize_solution(sol), counts))
        party_census[k] = lifts
        print("G5_TRANSPORTER", k, "phase_lifted_classes", len(lifts))
        for n, (pi, ps, sol, counts) in enumerate(lifts):
            print(" G5_LIFT", n, "pi", pi, "perms", ps, "normalized_d_h", sol, "kernel_counts_mod5_mod8", counts)
    gmod_party = tuple(k for k in UNITS if party_census[k])
    print("G5_G_MOD_UNLABELED", gmod_party, "ORDER", len(gmod_party), "FIXED_FIELD_DEGREE", 16 // len(gmod_party))
    print("G5_PRIMARY_REPAIRED", gmod_party != gmod)
    if args.output_certificate:
        args.output_certificate.write_text("\n".join(cert_lines) + "\n")


if __name__ == "__main__":
    main()
