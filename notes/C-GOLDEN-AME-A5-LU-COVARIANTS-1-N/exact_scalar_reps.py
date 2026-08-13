#!/usr/bin/env python3
"""Exact Q(zeta_40) replay of one representative of every F_41 class."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import verify_a5lu_covariants as scan


def import_k40(path: Path):
    spec = importlib.util.spec_from_file_location("k40verify", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def build_exact(source: Path, k):
    base, exponent = k.parse_source(source.read_bytes())
    U, _ = k.build_matrix(base, exponent)
    A = np.empty((6, 6, 6, 6), dtype=object)
    A.fill(k.ZERO)
    for row, entries in enumerate(U):
        i, j = divmod(row, 6)
        for col, value in entries.items():
            r, s = divmod(col, 6)
            A[i, j, r, s] = value
    B = np.vectorize(k.conjugate, otypes=[object])(A)
    return A, B


def expanded_permutations(d):
    q, n, pis = d
    out = []
    for ell, pi in enumerate(pis):
        out.append((0,) + pi if ell == q else pi)
    return tuple(out)


def contract_exact(A, B, d):
    q, n, _ = d
    pis = expanded_permutations(d)
    labels_a = [[4 * r + ell for ell in range(4)] for r in range(n)]
    open_y = 4 * n
    labels_b = [[None] * 4 for _ in range(n)]
    for ell in range(4):
        inv = [0] * n
        for r, s in enumerate(pis[ell]):
            inv[s] = r
        for s in range(n):
            labels_b[s][ell] = (
                open_y if ell == q and s == 0 else labels_a[inv[s]][ell]
            )
    args = []
    for r in range(n):
        args.extend((A, labels_a[r]))
    for s in range(n):
        args.extend((B, labels_b[s]))
    args.append([labels_a[0][q], open_y])
    return np.einsum(*args, optimize="greedy")


def scalar_value(C, k):
    value = C[0, 0]
    for i in range(6):
        for j in range(6):
            assert C[i, j] == (value if i == j else k.ZERO)
    return value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("k40_verifier", type=Path)
    args = ap.parse_args()
    k = import_k40(args.k40_verifier)
    _, entries = scan.parse_source(args.source)
    Af, Bf, _ = scan.build_tensors(entries)
    A, B = build_exact(args.source, k)
    for q in range(4):
        for n in (2, 3):
            first = {}
            ds = [d for d in scan.diagrams_for(n) if d[0] == q]
            for ordinal, d in enumerate(ds):
                C = scan.contract(Af, Bf, d)
                first.setdefault(int(C[0, 0]) % scan.P, (ordinal, d))
            for residue, (ordinal, d) in sorted(first.items()):
                value = scalar_value(contract_exact(A, B, d), k)
                print(q, n, residue, ordinal, value.short(), scan.descriptor_text(d))


if __name__ == "__main__":
    main()
