#!/usr/bin/env python3
"""Independent exact transporter census for C-GOLDEN-AME-GALOIS-DESCENT-1-N.

This implementation intentionally parses only the pinned MATLAB source and
does not import any implementation from the main incubation workspace.
"""

from __future__ import annotations

import hashlib
import argparse
import itertools
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


EXPECTED_SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
UNITS = tuple(k for k in range(40) if math.gcd(k, 40) == 1)


# Q(zeta_40) in the power basis, Phi_40=x^16-x^12+x^8-x^4+1.
@dataclass(frozen=True)
class K40:
    v: tuple[Fraction, ...]

    def __post_init__(self):
        if len(self.v) != 16:
            raise ValueError("K40 vectors have length 16")

    @staticmethod
    def zero() -> "K40":
        return K40((Fraction(0),) * 16)

    @staticmethod
    def one() -> "K40":
        return K40((Fraction(1),) + (Fraction(0),) * 15)

    @staticmethod
    def scalar(x: int | Fraction) -> "K40":
        return K40((Fraction(x),) + (Fraction(0),) * 15)

    def __add__(self, other: "K40") -> "K40":
        return K40(tuple(a + b for a, b in zip(self.v, other.v)))

    def __sub__(self, other: "K40") -> "K40":
        return K40(tuple(a - b for a, b in zip(self.v, other.v)))

    def __neg__(self) -> "K40":
        return K40(tuple(-a for a in self.v))

    def __mul__(self, other: "K40") -> "K40":
        c = [Fraction(0)] * 31
        for i, a in enumerate(self.v):
            if a:
                for j, b in enumerate(other.v):
                    if b:
                        c[i + j] += a * b
        for n in range(30, 15, -1):
            t = c[n]
            if t:
                # x^n=x^(n-4)-x^(n-8)+x^(n-12)-x^(n-16)
                c[n - 4] += t
                c[n - 8] -= t
                c[n - 12] += t
                c[n - 16] -= t
                c[n] = 0
        return K40(tuple(c[:16]))

    def __truediv__(self, other: "K40") -> "K40":
        return self * other.inverse()

    def __pow__(self, n: int) -> "K40":
        if n < 0:
            return (self.inverse()) ** (-n)
        out = K40.one()
        a = self
        while n:
            if n & 1:
                out = out * a
            a = a * a
            n //= 2
        return out

    def inverse(self) -> "K40":
        if self == K40.zero():
            raise ZeroDivisionError
        # Solve the multiplication matrix self*x=1 over Q.
        cols = []
        for j in range(16):
            basis = [Fraction(0)] * 16
            basis[j] = 1
            cols.append((self * K40(tuple(basis))).v)
        aug = [[cols[j][i] for j in range(16)] + [Fraction(i == 0)] for i in range(16)]
        for col in range(16):
            pivot = next(r for r in range(col, 16) if aug[r][col])
            aug[col], aug[pivot] = aug[pivot], aug[col]
            u = aug[col][col]
            aug[col] = [x / u for x in aug[col]]
            for r in range(16):
                if r != col and aug[r][col]:
                    u = aug[r][col]
                    aug[r] = [x - u * y for x, y in zip(aug[r], aug[col])]
        return K40(tuple(aug[i][-1] for i in range(16)))

    def aut(self, k: int) -> "K40":
        out = K40.zero()
        for i, a in enumerate(self.v):
            if a:
                out = out + K40.scalar(a) * zpow(i * k)
        return out

    def compact(self) -> str:
        terms = []
        for i, a in enumerate(self.v):
            if not a:
                continue
            coeff = str(a.numerator) if a.denominator == 1 else f"{a.numerator}/{a.denominator}"
            terms.append(f"{coeff}*z^{i}")
        return "0" if not terms else " + ".join(terms)


def zpow(n: int) -> K40:
    n %= 40
    # Construct/reduce x^n directly.
    c = [Fraction(0)] * max(17, n + 1)
    c[n] = 1
    for j in range(len(c) - 1, 15, -1):
        t = c[j]
        if t:
            c[j - 4] += t
            c[j - 8] -= t
            c[j - 12] += t
            c[j - 16] -= t
            c[j] = 0
    c += [Fraction(0)] * (16 - len(c))
    return K40(tuple(c[:16]))


def parse_source(path: Path):
    raw = path.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != EXPECTED_SOURCE_SHA256 or len(raw) != 8515:
        raise RuntimeError(f"source pin mismatch: bytes={len(raw)} sha256={sha}")
    text = raw.decode("utf-8")
    after = text.split("U = [", 1)[1]
    amp_text, exp_tail = after.split("] .* w.^[", 1)
    exp_text = exp_tail.rsplit("];", 1)[0]
    amps = re.findall(r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])", amp_text)
    exps = [int(x) for x in re.findall(r"(?<![A-Za-z0-9_])-?\d+(?![A-Za-z0-9_])", exp_text)]
    if len(amps) != 1296 or len(exps) != 1296:
        raise RuntimeError(f"parse shape mismatch: amps={len(amps)} exps={len(exps)}")
    tensor = {}
    for n, (lab, exponent) in enumerate(zip(amps, exps)):
        if lab == "0":
            continue
        row, col = divmod(n, 36)
        x = (row // 6, row % 6, col // 6, col % 6)
        tensor[x] = (lab, exponent % 20)
    if len(tensor) != 112:
        raise RuntimeError(f"support mismatch: {len(tensor)}")
    return raw, tensor


def amplitude_maps():
    w = zpow(2)
    c = (zpow(5) + zpow(-5)) / K40.scalar(2)
    a = c / (w + w ** -1)
    b = (w ** 2 + w ** -2) * a
    base = {"a": a, "b": b, "c": c}
    maps = {}
    for k in UNITS:
        one = {}
        for label, value in base.items():
            image = value.aut(k)
            hits = []
            for outlabel, outvalue in base.items():
                for phase in range(40):
                    if image == zpow(phase) * outvalue:
                        hits.append((outlabel, phase))
            if len(hits) != 1:
                raise RuntimeError(f"amplitude image ambiguous k={k} label={label}: {hits}")
            one[label] = hits[0]
        maps[k] = one
    return base, maps


def degree_vectors(tensor):
    out = []
    for q in range(4):
        out.append(tuple(sum(x[q] == r for x in tensor) for r in range(6)))
    return tuple(out)


def preserving_perms(source_degree, target_degree=None):
    """Maps target symbols to source symbols with equal coordinate degrees."""
    if target_degree is None:
        target_degree = source_degree
    by_target = defaultdict(list)
    by_source = defaultdict(list)
    for i, d in enumerate(target_degree):
        by_target[d].append(i)
    for i, d in enumerate(source_degree):
        by_source[d].append(i)
    if {d: len(v) for d, v in by_target.items()} != {d: len(v) for d, v in by_source.items()}:
        return []
    groups = []
    for d in sorted(by_target):
        tg = by_target[d]
        sg = by_source[d]
        groups.append([(tg, image) for image in itertools.permutations(sg)])
    result = []
    for choices in itertools.product(*groups):
        p = [None] * 6
        for tg, image in choices:
            for x, y in zip(tg, image):
                p[x] = y
        result.append(tuple(p))
    return result


def candidate_census(tensor, degrees, color_map, leg_perm=(0, 1, 2, 3)):
    """Enumerate degree-pruned local tuples for A[x] -> A[y].

    y_q = p_q(x_{leg_perm[q]}), and p_q maps symbols on target/input leg
    leg_perm[q] to symbols on source tensor leg q.
    """
    pools = [preserving_perms(degrees[q], degrees[leg_perm[q]]) for q in range(4)]
    raw = math.prod(len(p) for p in pools)
    support = set(tensor)
    support_candidates = []
    colored_candidates = []
    for ps in itertools.product(*pools):
        support_ok = True
        color_ok = True
        for x, (lab, _) in tensor.items():
            y = tuple(ps[q][x[leg_perm[q]]] for q in range(4))
            if y not in support:
                support_ok = False
                color_ok = False
                break
            if color_map[lab] != tensor[y][0]:
                color_ok = False
        if support_ok:
            support_candidates.append(ps)
            if color_ok:
                colored_candidates.append(ps)
    return pools, raw, support_candidates, colored_candidates


def phase_system(tensor, amp_map, ps, leg_perm=(0, 1, 2, 3)):
    # Variables: h, then d_q(r), with phase indexed by the transformed symbol y_q.
    A = []
    b = []
    row_names = []
    for x in sorted(tensor):
        lab, e = tensor[x]
        y = tuple(ps[q][x[leg_perm[q]]] for q in range(4))
        outlab, amp_phase = amp_map[lab]
        ylab, ey = tensor[y]
        if outlab != ylab:
            raise RuntimeError("phase system received a color-invalid candidate")
        row = [0] * 25
        row[0] = 1
        for q in range(4):
            row[1 + 6 * q + y[q]] += 1
        rhs = (amp_phase + 2 * e * CURRENT_K - 2 * ey) % 40
        A.append(row)
        b.append(rhs)
        row_names.append(x)
    return A, b, row_names


def prime_rref(A, b, p):
    m, n = len(A), len(A[0])
    R = [[x % p for x in row] for row in A]
    rhs = [x % p for x in b]
    U = [[int(i == j) for j in range(m)] for i in range(m)]
    pivots = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if R[i][c] % p), None)
        if pivot is None:
            continue
        R[r], R[pivot] = R[pivot], R[r]
        rhs[r], rhs[pivot] = rhs[pivot], rhs[r]
        U[r], U[pivot] = U[pivot], U[r]
        inv = pow(R[r][c], -1, p)
        R[r] = [(inv * x) % p for x in R[r]]
        rhs[r] = inv * rhs[r] % p
        U[r] = [(inv * x) % p for x in U[r]]
        for i in range(m):
            if i == r or not R[i][c] % p:
                continue
            f = R[i][c] % p
            R[i] = [(x - f * y) % p for x, y in zip(R[i], R[r])]
            rhs[i] = (rhs[i] - f * rhs[r]) % p
            U[i] = [(x - f * y) % p for x, y in zip(U[i], U[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    rank_a = len(pivots)
    bad = next((i for i in range(m) if not any(R[i]) and rhs[i] % p), None)
    if bad is not None:
        cert = [x % p for x in U[bad]]
        scale = pow(sum(cert[i] * b[i] for i in range(m)) % p, -1, p)
        cert = [(scale * x) % p for x in cert]
        return {
            "solvable": False,
            "rank_a": rank_a,
            "rank_aug": rank_a + 1,
            "certificate": cert,
        }
    free = [c for c in range(n) if c not in pivots]
    sol = [0] * n
    for i, c in enumerate(pivots):
        sol[c] = rhs[i]
    kernel = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = (-R[i][f]) % p
        kernel.append(v)
    return {
        "solvable": True,
        "rank_a": rank_a,
        "rank_aug": rank_a,
        "solution": sol,
        "kernel": kernel,
    }


def mod8_diagonalize(A, b):
    """Exact solve/certificate over Z/8 using invertible row/column operations."""
    mod = 8
    m, n = len(A), len(A[0])
    R = [[x % mod for x in row] for row in A]
    rhs = [x % mod for x in b]
    U = [[int(i == j) for j in range(m)] for i in range(m)]
    V = [[int(i == j) for j in range(n)] for i in range(n)]

    def val2(x):
        x %= 8
        if x == 0:
            return 99
        if x % 2:
            return 0
        if x % 4:
            return 1
        return 2

    t = 0
    while t < min(m, n):
        choices = [(val2(R[i][j]), i, j) for i in range(t, m) for j in range(t, n) if R[i][j] % 8]
        if not choices:
            break
        _, pi, pj = min(choices)
        if pi != t:
            R[t], R[pi] = R[pi], R[t]
            rhs[t], rhs[pi] = rhs[pi], rhs[t]
            U[t], U[pi] = U[pi], U[t]
        if pj != t:
            for row in R:
                row[t], row[pj] = row[pj], row[t]
            for row in V:
                row[t], row[pj] = row[pj], row[t]

        v = val2(R[t][t])
        d = 1 << v
        odd = (R[t][t] // d) % (8 // d)
        # An odd inverse modulo 8 normalizes the pivot to d modulo 8.
        inv = pow(odd, -1, 8)
        R[t] = [(inv * x) % 8 for x in R[t]]
        rhs[t] = inv * rhs[t] % 8
        U[t] = [(inv * x) % 8 for x in U[t]]
        if R[t][t] != d:
            raise RuntimeError("failed to normalize Z/8 pivot")

        # Minimal valuation ensures all remaining entries are divisible by d.
        for i in range(t + 1, m):
            a = R[i][t] % 8
            if a % d:
                raise RuntimeError("Z/8 valuation invariant failed in column")
            q = (a // d) % (8 // d)
            if q:
                R[i] = [(x - q * y) % 8 for x, y in zip(R[i], R[t])]
                rhs[i] = (rhs[i] - q * rhs[t]) % 8
                U[i] = [(x - q * y) % 8 for x, y in zip(U[i], U[t])]
        for j in range(t + 1, n):
            a = R[t][j] % 8
            if a % d:
                raise RuntimeError("Z/8 valuation invariant failed in row")
            q = (a // d) % (8 // d)
            if q:
                for i in range(m):
                    R[i][j] = (R[i][j] - q * R[i][t]) % 8
                for i in range(n):
                    V[i][j] = (V[i][j] - q * V[i][t]) % 8
        if any(R[i][t] for i in range(t + 1, m)) or any(R[t][j] for j in range(t + 1, n)):
            raise RuntimeError("Z/8 diagonal clearing failed")
        t += 1

    diag = [R[i][i] if i < min(m, n) else 0 for i in range(m)]
    for i in range(m):
        d = diag[i] if i < n else 0
        need = math.gcd(d, 8)
        if rhs[i] % need:
            factor = {0: 1, 2: 4, 4: 2}.get(d)
            if factor is None:
                raise RuntimeError(f"unexpected failing diagonal {d}")
            cert = [(factor * x) % 8 for x in U[i]]
            lhs = [sum(cert[r] * A[r][c] for r in range(m)) % 8 for c in range(n)]
            dotb = sum(cert[r] * b[r] for r in range(m)) % 8
            if any(lhs) or dotb == 0:
                raise RuntimeError("invalid Z/8 inconsistency certificate")
            return {
                "solvable": False,
                "diagonal": diag[:t],
                "rank_unit": sum(d == 1 for d in diag[:t]),
                "certificate": cert,
                "certificate_dot_b": dotb,
            }

    y = [0] * n
    kernel_y = []
    kernel_orders = []
    for i in range(n):
        d = R[i][i] if i < min(m, n) else 0
        bi = rhs[i] if i < m else 0
        if d == 1:
            y[i] = bi % 8
        elif d == 2:
            y[i] = (bi // 2) % 4
            v = [0] * n
            v[i] = 4
            kernel_y.append(v)
            kernel_orders.append(2)
        elif d == 4:
            y[i] = (bi // 4) % 2
            v = [0] * n
            v[i] = 2
            kernel_y.append(v)
            kernel_orders.append(4)
        elif d == 0:
            y[i] = 0
            v = [0] * n
            v[i] = 1
            kernel_y.append(v)
            kernel_orders.append(8)
        else:
            raise RuntimeError(f"unexpected diagonal {d}")

    def mat_vec(M, x):
        return [sum(M[i][j] * x[j] for j in range(len(x))) % 8 for i in range(len(M))]

    sol = mat_vec(V, y)
    kernel = [mat_vec(V, v) for v in kernel_y]
    if any((sum(A[i][j] * sol[j] for j in range(n)) - b[i]) % 8 for i in range(m)):
        raise RuntimeError("invalid Z/8 solution")
    return {
        "solvable": True,
        "diagonal": diag[:t],
        "rank_unit": sum(d == 1 for d in diag[:t]),
        "solution": sol,
        "kernel": kernel,
        "kernel_orders": kernel_orders,
    }


def crt_phase_solution(sol5, sol8):
    # x = sol8 (mod 8), x = sol5 (mod 5); 16=0 mod8 and 1 mod5.
    return [(a + 16 * ((b - a) % 5)) % 40 for a, b in zip(sol8, sol5)]


def sparse_vector(v):
    return [[i, x] for i, x in enumerate(v) if x]


def perm_code(ps):
    return [list(p) for p in ps]


def conjugate_hash(tensor, k, amp_map):
    lines = []
    for x in sorted(tensor):
        lab, e = tensor[x]
        outlab, phase = amp_map[lab]
        exponent = (phase + 2 * k * e) % 40
        lines.append(f"{','.join(map(str, x))}:{outlab}:{exponent}\n")
    return hashlib.sha256("".join(lines).encode()).hexdigest()


def field_fixed_data(H):
    H = tuple(sorted(H))
    # Deterministically search averaged monomial orbit sums with exact stabilizer H.
    theta = None
    description = None
    for exponent in range(1, 40):
        candidate = K40.zero()
        for h in H:
            candidate += zpow(h * exponent)
        candidate = candidate / K40.scalar(len(H))
        stabilizer = tuple(k for k in UNITS if candidate.aut(k) == candidate)
        if stabilizer == H:
            theta = candidate
            description = f"(1/{len(H)})*sum_{{h in H}} z^(h*{exponent})"
            break
    if theta is None:
        # Small deterministic linear combinations if a monomial average is insufficient.
        for e1 in range(1, 12):
            for e2 in range(e1 + 1, 16):
                candidate = K40.zero()
                for h in H:
                    candidate += zpow(h * e1) + K40.scalar(2) * zpow(h * e2)
                candidate = candidate / K40.scalar(len(H))
                stabilizer = tuple(k for k in UNITS if candidate.aut(k) == candidate)
                if stabilizer == H:
                    theta = candidate
                    description = f"avg_H(z^{e1}+2*z^{e2})"
                    break
            if theta is not None:
                break
    if theta is None:
        raise RuntimeError("failed to find primitive fixed-field element")

    orbit = []
    for k in UNITS:
        v = theta.aut(k)
        if v not in orbit:
            orbit.append(v)
    poly = [K40.one()]
    for root in orbit:
        nxt = [K40.zero()] * (len(poly) + 1)
        for i, coeff in enumerate(poly):
            nxt[i] = nxt[i] - coeff * root
            nxt[i + 1] = nxt[i + 1] + coeff
        poly = nxt
    rational_coeffs = []
    for coeff in poly:
        if any(coeff.v[i] for i in range(1, 16)):
            raise RuntimeError(f"minimal polynomial coefficient not rational: {coeff.compact()}")
        rational_coeffs.append(str(coeff.v[0]))
    return {
        "subgroup": list(H),
        "degree": len(orbit),
        "generator_description": description,
        "generator": theta.compact(),
        "minimal_polynomial_coefficients_low_to_high": rational_coeffs,
    }


def verify_certificate(A, b, cert, mod):
    lhs = [sum(cert[i] * A[i][j] for i in range(len(A))) % mod for j in range(len(A[0]))]
    dot = sum(cert[i] * b[i] for i in range(len(A))) % mod
    return not any(lhs) and dot != 0, dot


def run(source: Path, output: Path):
    raw, tensor = parse_source(source)
    base, amap = amplitude_maps()
    degrees = degree_vectors(tensor)
    amp_classes = {}
    for k in UNITS:
        key = tuple(amap[k][label][0] for label in ("a", "b", "c"))
        amp_classes.setdefault(key, k)

    class_census = {}
    for key in amp_classes:
        cmap = dict(zip(("a", "b", "c"), key))
        pools, raw_count, supports, colored = candidate_census(tensor, degrees, cmap)
        class_census[key] = {
            "pool_sizes": [len(x) for x in pools],
            "raw": raw_count,
            "support": supports,
            "colored": colored,
        }

    swap = (0, 1, 3, 2)
    swap_class_census = {}
    for key in amp_classes:
        cmap = dict(zip(("a", "b", "c"), key))
        pools, raw_count, supports, colored = candidate_census(tensor, degrees, cmap, swap)
        swap_class_census[key] = {
            "pool_sizes": [len(x) for x in pools],
            "raw": raw_count,
            "support": supports,
            "colored": colored,
        }

    results = {
        "implementation": "independent crosscheck.py",
        "prereg_commit": "f78538f881a0e25fcc0ed839c88c0fd45a751352",
        "prereg_sha256": "d662cae52dbbafd2f0802aabade5ffdfc09bb5d22d7160999bf845fc4866f886",
        "source": {
            "path": source.name,
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "support": len(tensor),
            "amplitude_counts": dict(sorted(Counter(l for l, _ in tensor.values()).items())),
            "degree_vectors": degrees,
        },
        "units": list(UNITS),
        "amplitude_maps": {},
        "labeled": {},
        "party_swap_23": {},
    }
    for k in UNITS:
        results["amplitude_maps"][str(k)] = {
            label: {"label": out, "z40_phase": phase}
            for label, (out, phase) in amap[k].items()
        }

    global CURRENT_K
    for leg_mode, leg_perm, destination, census_by_class in (
        ("labeled", (0, 1, 2, 3), results["labeled"], class_census),
        ("swap23", swap, results["party_swap_23"], swap_class_census),
    ):
        for k in UNITS:
            CURRENT_K = k
            color_key = tuple(amap[k][label][0] for label in ("a", "b", "c"))
            census = census_by_class[color_key]
            item = {
                "conjugate_sha256": conjugate_hash(tensor, k, amap[k]),
                "degree_pool_sizes": census["pool_sizes"],
                "raw_candidates": census["raw"],
                "support_candidates": len(census["support"]),
                "colored_support_candidates": len(census["colored"]),
                "candidate_phase_audits": [],
            }
            transporter_count = 0
            for candidate_index, ps in enumerate(census["colored"]):
                Aeq, beq, row_names = phase_system(tensor, amap[k], ps, leg_perm)
                m5 = prime_rref(Aeq, beq, 5)
                m8 = mod8_diagonalize(Aeq, beq)
                audit = {
                    "candidate_index": candidate_index,
                    "permutations": perm_code(ps),
                    "mod5": {
                        "solvable": m5["solvable"],
                        "rank_a": m5["rank_a"],
                        "rank_aug": m5["rank_aug"],
                    },
                    "mod8": {
                        "solvable": m8["solvable"],
                        "diagonal": m8["diagonal"],
                        "rank_unit": m8["rank_unit"],
                    },
                }
                if not m5["solvable"]:
                    ok, dot = verify_certificate(Aeq, beq, m5["certificate"], 5)
                    if not ok:
                        raise RuntimeError("bad mod5 certificate")
                    audit["mod5"]["left_null_certificate_sparse"] = sparse_vector(m5["certificate"])
                    audit["mod5"]["certificate_dot_b"] = dot
                    audit["mod5"]["certificate_rows"] = [
                        {"row": i, "coefficient": c, "tensor_index": row_names[i]}
                        for i, c in enumerate(m5["certificate"]) if c
                    ]
                else:
                    audit["mod5"]["solution"] = m5["solution"]
                    audit["mod5"]["kernel_basis"] = m5["kernel"]
                if not m8["solvable"]:
                    ok, dot = verify_certificate(Aeq, beq, m8["certificate"], 8)
                    if not ok:
                        raise RuntimeError("bad mod8 certificate")
                    audit["mod8"]["left_null_certificate_sparse"] = sparse_vector(m8["certificate"])
                    audit["mod8"]["certificate_dot_b"] = dot
                    audit["mod8"]["certificate_rows"] = [
                        {"row": i, "coefficient": c, "tensor_index": row_names[i]}
                        for i, c in enumerate(m8["certificate"]) if c
                    ]
                else:
                    audit["mod8"]["solution"] = m8["solution"]
                    audit["mod8"]["kernel_basis"] = m8["kernel"]
                    audit["mod8"]["kernel_orders"] = m8["kernel_orders"]

                if m5["solvable"] and m8["solvable"]:
                    sol40 = crt_phase_solution(m5["solution"], m8["solution"])
                    residuals = [
                        (sum(row[j] * sol40[j] for j in range(25)) - rhs) % 40
                        for row, rhs in zip(Aeq, beq)
                    ]
                    if any(residuals):
                        raise RuntimeError("CRT phase solution failed all-entry substitution")
                    transporter_count += 1
                    audit["mod40_solution"] = sol40
                    audit["all_112_substitution"] = True
                else:
                    audit["mod40_solution"] = None
                    audit["all_112_substitution"] = False
                item["candidate_phase_audits"].append(audit)
            item["liftable_permutation_candidates"] = transporter_count
            destination[str(k)] = item

    Gmod = tuple(k for k in UNITS if results["labeled"][str(k)]["liftable_permutation_candidates"] > 0)
    # Subgroup checks.
    subgroup_ok = 1 in Gmod and all((a * b) % 40 in Gmod for a in Gmod for b in Gmod)
    if not subgroup_ok:
        raise RuntimeError(f"computed G_mod is not a subgroup: {Gmod}")
    results["G_mod"] = list(Gmod)
    results["G_mod_order"] = len(Gmod)
    results["G_mod_subgroup_check"] = subgroup_ok
    results["fixed_field"] = field_fixed_data(Gmod)
    results["only_possible_party_permutations_from_degree_signatures"] = [
        [0, 1, 2, 3], [0, 1, 3, 2]
    ]

    out = output
    out.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "source": results["source"],
        "amplitude_maps": results["amplitude_maps"],
        "labeled_summary": {
            k: {field: v[field] for field in (
                "raw_candidates", "support_candidates", "colored_support_candidates",
                "liftable_permutation_candidates")}
            for k, v in results["labeled"].items()
        },
        "swap23_summary": {
            k: {field: v[field] for field in (
                "raw_candidates", "support_candidates", "colored_support_candidates",
                "liftable_permutation_candidates")}
            for k, v in results["party_swap_23"].items()
        },
        "G_mod": results["G_mod"],
        "fixed_field": results["fixed_field"],
        "result_path": out.name,
        "result_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
    }, indent=2, sort_keys=True))


CURRENT_K = 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, default=Path("CROSSCHECK.json"))
    args = parser.parse_args()
    run(args.source, args.output)
