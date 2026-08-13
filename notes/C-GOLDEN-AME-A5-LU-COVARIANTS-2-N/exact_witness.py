#!/usr/bin/env python3
"""Exact Q(zeta_40) lift of the frozen q=0,R1 dimension witness.

Uses an independent sparse contraction ordering and tracks power-basis
coefficients modulo Phi_40.  No code is imported from the modular engine.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import re
import sys
from fractions import Fraction
from pathlib import Path


SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
CORE_R1 = ((1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1))
P = 41


def load_k40(path):
    spec = importlib.util.spec_from_file_location("independent_k40", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_exact(kmod, source):
    raw = source.read_bytes()
    if len(raw) != 8515 or hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
        raise RuntimeError("source pin mismatch")
    text = raw.decode()
    tail = text.split("U = [", 1)[1]
    amp_text, exp_tail = tail.split("] .* w.^[", 1)
    exp_text = exp_tail.rsplit("];", 1)[0]
    labels = re.findall(r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])", amp_text)
    exponents = [int(x) for x in re.findall(r"(?<![A-Za-z0-9_])-?\d+(?![A-Za-z0-9_])", exp_text)]
    w = kmod.ZPOW[2]
    c = (kmod.ZPOW[5] + kmod.ZPOW[-5]) / 2
    a = c / (w + w ** -1)
    b = (w**2 + w**-2) * a
    base = {"a": a, "b": b, "c": c}
    A = {}
    B = {}
    for pos, (label, exponent) in enumerate(zip(labels, exponents)):
        if label == "0":
            continue
        row, col = divmod(pos, 36)
        x = (row // 6, row % 6, col // 6, col % 6)
        A[x] = base[label] * (w ** exponent)
        B[x] = base[label] * (w ** (-exponent))
    if len(A) != 112:
        raise RuntimeError("support mismatch")
    return A, B


class SparseFactor:
    def __init__(self, data, labels, name):
        self.data = data
        self.labels = tuple(labels)
        self.name = name


def make_factors(A, B, q, core):
    matchings = [None] * 4
    matchings[q] = (0, 1, 2, 3)
    for ell, p in zip((x for x in range(4) if x != q), core):
        matchings[ell] = p
    inverses = []
    for p in matchings:
        inv = [0] * 4
        for i, x in enumerate(p):
            inv[x] = i
        inverses.append(inv)
    out = {}
    for r in range(4):
        labels = [("row", q) if ell == q and r == 0 else ("wire", ell, r) for ell in range(4)]
        out[f"A{r}"] = SparseFactor(dict(A), labels, f"A{r}")
    for s in range(4):
        labels = [
            ("col", q) if ell == q and s == 0 else ("wire", ell, inverses[ell][s])
            for ell in range(4)
        ]
        out[f"B{s}"] = SparseFactor(dict(B), labels, f"B{s}")
    return out


def merge(a, b, zero):
    shared = sorted(set(a.labels).intersection(b.labels), key=repr)
    apos = [a.labels.index(x) for x in shared]
    bpos = [b.labels.index(x) for x in shared]
    bucket = {}
    for ib, vb in b.data.items():
        bucket.setdefault(tuple(ib[i] for i in bpos), []).append((ib, vb))
    output = {}
    joins = 0
    for ia, va in a.data.items():
        key = tuple(ia[i] for i in apos)
        for ib, vb in bucket.get(key, ()):
            index = tuple(ia[i] for i in range(len(ia)) if i not in apos) + tuple(
                ib[i] for i in range(len(ib)) if i not in bpos
            )
            output[index] = output.get(index, zero) + va * vb
            joins += 1
    output = {i: v for i, v in output.items() if v != zero}
    labels = tuple(x for i, x in enumerate(a.labels) if i not in apos) + tuple(
        x for i, x in enumerate(b.labels) if i not in bpos
    )
    factor = SparseFactor(output, labels, f"({a.name}*{b.name})")
    stat = {"factor": factor.name, "shared": len(shared), "joins": joins, "nnz": len(output), "rank": len(labels)}
    return factor, stat


def contract_sparse(A, B, kmod, ordering):
    f = make_factors(A, B, 0, CORE_R1)
    zero = kmod.ZERO
    stats = []

    def mm(x, y):
        z, st = merge(x, y, zero)
        stats.append(st)
        return z

    if ordering == "cycle-optimal-a":
        x = mm(mm(f["A0"], f["B1"]), mm(f["A1"], f["B2"]))
        x = mm(x, mm(f["A2"], f["B3"]))
        x = mm(x, f["A3"])
        x = mm(x, f["B0"])
    elif ordering == "cycle-optimal-b":
        x = mm(mm(f["A0"], f["B3"]), mm(f["A3"], f["B2"]))
        x = mm(x, mm(f["A2"], f["B1"]))
        x = mm(x, f["A1"])
        x = mm(x, f["B0"])
    else:
        raise ValueError(ordering)
    desired = (("row", 0), ("col", 0))
    if set(x.labels) != set(desired):
        raise RuntimeError(x.labels)
    matrix = [[zero for _ in range(6)] for _ in range(6)]
    for idx, value in x.data.items():
        matrix[idx[x.labels.index(desired[0])]][idx[x.labels.index(desired[1])]] = value
    return matrix, stats


def reduce_f41(value):
    total = 0
    for i, coeff in enumerate(value.c):
        numerator = coeff.numerator % P
        denominator = coeff.denominator % P
        if denominator == 0:
            raise RuntimeError("denominator divisible by 41")
        total = (total + numerator * pow(denominator, -1, P) * pow(6, i, P)) % P
    return total


def coeffs(value):
    return [str(x) for x in value.c]


def det3_exact(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--field-module", type=Path, default=Path(__file__).with_name("verify_source_field.py"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("EXACT_WITNESS.json"))
    args = parser.parse_args()
    kmod = load_k40(args.field_module)
    A, B = parse_exact(kmod, args.source)
    M1, stats1 = contract_sparse(A, B, kmod, "cycle-optimal-a")
    M2, stats2 = contract_sparse(A, B, kmod, "cycle-optimal-b")
    if M1 != M2:
        raise RuntimeError("independent contraction orderings disagree")
    star_exact, star_stats = contract_sparse(B, A, kmod, "cycle-optimal-a")
    star_exact = [list(row) for row in zip(*star_exact)]
    if star_exact != M1:
        raise RuntimeError("exact star audit failed")
    zero, one = kmod.ZERO, kmod.ONE
    # Frozen first modular minor uses flattened positions 0,7,21, i.e. diagonal
    # entries (0,0),(1,1),(3,3) of I,M,M^2.
    positions = ((0, 0), (1, 1), (3, 3))
    M_sq = [[sum((M1[i][k] * M1[k][j] for k in range(6)), zero) for j in range(6)] for i in range(6)]
    exact_minor_matrix = [
        [one, one, one],
        [M1[i][j] for i, j in positions],
        [M_sq[i][j] for i, j in positions],
    ]
    determinant = det3_exact(exact_minor_matrix)
    if determinant == zero:
        raise RuntimeError("exact determinant vanished")
    modular_matrix = [[reduce_f41(x) for x in row] for row in M1]
    modular_m2 = [[reduce_f41(x) for x in row] for row in M_sq]
    determinant_mod41 = reduce_f41(determinant)
    if determinant_mod41 != 31:
        raise RuntimeError(f"unexpected modular determinant {determinant_mod41}")

    denominator_lcm = 1
    for value in itertools.chain.from_iterable(M1):
        for x in value.c:
            denominator_lcm = math_lcm(denominator_lcm, x.denominator)
    for x in determinant.c:
        denominator_lcm = math_lcm(denominator_lcm, x.denominator)
    if denominator_lcm % 41 == 0:
        raise RuntimeError("exact witness denominator not 41-integral")

    # The exact matrix is diagonal.  Its three repeated diagonal values give
    # the exact eigenvalue multiplicities without symbolic root finding.
    if any(M1[i][j] != zero for i in range(6) for j in range(6) if i != j):
        raise RuntimeError("expected exact witness matrix to be diagonal")
    eigen_groups = []
    for i in range(6):
        value = M1[i][i]
        hit = next((g for g in eigen_groups if g["value"] == value), None)
        if hit is None:
            eigen_groups.append({"value": value, "indices": [i]})
        else:
            hit["indices"].append(i)
    eigen_groups.sort(key=lambda g: g["indices"][0])
    if sorted(len(g["indices"]) for g in eigen_groups) != [2, 2, 2]:
        raise RuntimeError("unexpected exact eigenvalue multiplicities")

    result = {
        "q": 0,
        "descriptor": [list(p) for p in CORE_R1],
        "ordering_a": stats1,
        "ordering_b": stats2,
        "ordering_matrices_equal": True,
        "star_ordering": star_stats,
        "star_exact_equal": True,
        "matrix_exact_power_basis": [[coeffs(x) for x in row] for row in M1],
        "matrix_mod41": modular_matrix,
        "matrix_square_mod41": modular_m2,
        "minor_positions": [list(x) for x in positions],
        "minor_exact_power_basis": coeffs(determinant),
        "minor_mod41": determinant_mod41,
        "exact_eigenvalue_groups": [
            {
                "indices": g["indices"],
                "multiplicity": len(g["indices"]),
                "power_basis": coeffs(g["value"]),
                "mod41": reduce_f41(g["value"]),
            }
            for g in eigen_groups
        ],
        "all_witness_denominators_lcm": denominator_lcm,
        "denominators_prime_to_41": True,
    }
    out = args.output
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "q": 0,
        "descriptor": result["descriptor"],
        "matrix_mod41": modular_matrix,
        "minor_positions": result["minor_positions"],
        "minor_exact_power_basis": result["minor_exact_power_basis"],
        "minor_mod41": determinant_mod41,
        "exact_eigenvalue_groups": result["exact_eigenvalue_groups"],
        "denominator_lcm": denominator_lcm,
        "ordering_a": stats1,
        "ordering_b": stats2,
        "result_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
    }, indent=2, sort_keys=True))


def math_lcm(a, b):
    import math
    return abs(a * b) // math.gcd(a, b)


if __name__ == "__main__":
    main()
