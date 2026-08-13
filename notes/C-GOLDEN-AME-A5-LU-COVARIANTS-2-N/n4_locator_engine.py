#!/usr/bin/env python3
"""Post-lock F_41 engine for the four n=4 double-edge-free cores.

This module contains no golden-tensor parser and is not executed on the
pinned tensor during preregistration design.  Call ``scan(A, Abar)`` only
after a public computational pin; both arrays must have shape (6,6,6,6).
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass

import numpy as np


P = 41
IDENTITY = (0, 1, 2, 3)
CORES = (
    ((1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)),
    ((1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1)),
    ((1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)),
    ((1, 2, 3, 0), (3, 0, 1, 2), (2, 3, 0, 1)),
)


def inverse(p):
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


@dataclass
class Factor:
    value: np.ndarray
    labels: tuple
    name: str


def merge(a: Factor, b: Factor, expected_shared: int) -> Factor:
    shared = sorted(set(a.labels).intersection(b.labels), key=repr)
    if len(shared) != expected_shared:
        raise RuntimeError(f"path mismatch {a.name},{b.name}: {len(shared)} != {expected_shared}")
    axes_a = [a.labels.index(x) for x in shared]
    axes_b = [b.labels.index(x) for x in shared]
    value = np.tensordot(a.value, b.value, axes=(axes_a, axes_b)) % P
    labels = tuple(x for i, x in enumerate(a.labels) if i not in axes_a) + tuple(
        x for i, x in enumerate(b.labels) if i not in axes_b
    )
    return Factor(value, labels, f"({a.name}*{b.name})")


def factors(A, B, q, core):
    matchings = [None] * 4
    matchings[q] = IDENTITY
    for ell, p in zip((x for x in range(4) if x != q), core):
        matchings[ell] = p
    inverses = [inverse(p) for p in matchings]
    out = {}
    for r in range(4):
        labels = tuple(("row", q) if ell == q and r == 0 else ("wire", ell, r) for ell in range(4))
        out[f"A{r}"] = Factor(A, labels, f"A{r}")
    for s in range(4):
        labels = tuple(
            ("col", q) if ell == q and s == 0 else ("wire", ell, inverses[ell][s])
            for ell in range(4)
        )
        out[f"B{s}"] = Factor(B, labels, f"B{s}")
    return out


def core_covariant(A, B, q, core):
    """Optimal exact-mod-41 tree: max rank 8, 122059872 multiply-adds."""
    f = factors(A, B, q, core)
    x03 = merge(f["A0"], f["B3"], 1)
    x32 = merge(f["A3"], f["B2"], 1)
    x = merge(x03, x32, 2)
    x21 = merge(f["A2"], f["B1"], 1)
    x = merge(x, x21, 4)
    x = merge(x, f["A1"], 3)
    x = merge(x, f["B0"], 3)
    desired = (("row", q), ("col", q))
    if set(x.labels) != set(desired) or len(x.labels) != 2:
        raise RuntimeError((x.labels, x.value.shape))
    return np.transpose(x.value, (x.labels.index(desired[0]), x.labels.index(desired[1]))) % P


def scalar_value(M):
    lam = int(M[0, 0] % P)
    target = np.eye(6, dtype=np.int64) * lam
    return lam if np.array_equal(M % P, target % P) else None


def first_nonzero(M):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if int(M[i, j] % P):
                return (i, j, int(M[i, j] % P))
    return None


def rank_and_pivots(matrices):
    R = [[int(x % P) for x in M.reshape(-1)] for M in matrices]
    pivots = []
    r = 0
    for c in range(36):
        pivot = next((i for i in range(r, len(R)) if R[i][c]), None)
        if pivot is None:
            continue
        R[r], R[pivot] = R[pivot], R[r]
        inv = pow(R[r][c], -1, P)
        R[r] = [(inv * x) % P for x in R[r]]
        for i in range(len(R)):
            if i != r and R[i][c]:
                a = R[i][c]
                R[i] = [(x - a * y) % P for x, y in zip(R[i], R[r])]
        pivots.append(c)
        r += 1
        if r == len(R):
            break
    return r, pivots


def determinant3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) % P


def independent_minor3(matrices):
    if len(matrices) != 3:
        raise ValueError
    rank, pivots = rank_and_pivots(matrices)
    if rank != 3:
        return None
    # Find lexicographically first nonzero 3-column minor, a small exact cert.
    rows = [[int(x % P) for x in M.reshape(-1)] for M in matrices]
    for cols in itertools.combinations(range(36), 3):
        d = determinant3([[rows[i][j] for j in cols] for i in range(3)])
        if d:
            return {"flattened_positions": cols, "row_col_positions": tuple(divmod(x, 6) for x in cols), "determinant_mod41": d}
    raise RuntimeError("rank/minor contradiction")


def add_independent(basis, descriptions, M, description):
    rank0, _ = rank_and_pivots(basis)
    rank1, _ = rank_and_pivots(basis + [M])
    if rank1 > rank0:
        basis.append(M)
        descriptions.append(description)
        return True
    return False


def close_star_algebra(basis, descriptions):
    """Stop as soon as a three-dimensional modular subspace is certified."""
    changed = True
    while changed and len(basis) <= 2:
        changed = False
        snapshot = list(zip(basis, descriptions))
        for i, (A, da) in enumerate(snapshot):
            for j, (B, db) in enumerate(snapshot):
                C = A @ B % P
                if add_independent(basis, descriptions, C, f"({da})*({db})"):
                    changed = True
                    if len(basis) > 2:
                        return


def scan(A, Abar):
    A = np.asarray(A, dtype=np.int64) % P
    Abar = np.asarray(Abar, dtype=np.int64) % P
    if A.shape != (6, 6, 6, 6) or Abar.shape != A.shape:
        raise ValueError("A and Abar must both have shape (6,6,6,6)")
    result = {"first_nonscalar": None, "hard_witness": None, "matrices": []}
    for q in range(4):
        basis = [np.eye(6, dtype=np.int64)]
        descriptions = ["I"]
        generators = []
        for core_index, core in enumerate(CORES):
            M = core_covariant(A, Abar, q, core)
            Mstar = core_covariant(Abar, A, q, core).T % P
            item = {
                "q": q, "core_index": core_index, "core": core,
                "matrix": M.tolist(), "star": Mstar.tolist(),
                "scalar": scalar_value(M), "star_scalar": scalar_value(Mstar),
            }
            result["matrices"].append(item)
            if item["scalar"] is None and result["first_nonscalar"] is None:
                result["first_nonscalar"] = {"q": q, "core_index": core_index, "core": core, "matrix": M.tolist()}

            own_comm = (M @ Mstar - Mstar @ M) % P
            own_nz = first_nonzero(own_comm)
            if own_nz:
                result["hard_witness"] = {
                    "kind": "commutator-with-own-star", "q": q,
                    "new": f"core{core_index}", "entry": own_nz,
                }
                return result
            for old, old_desc in generators:
                comm = (old @ M - M @ old) % P
                nz = first_nonzero(comm)
                if nz:
                    result["hard_witness"] = {
                        "kind": "commutator", "q": q, "old": old_desc,
                        "new": f"core{core_index}", "entry": nz,
                    }
                    return result
                comm = (old @ Mstar - Mstar @ old) % P
                nz = first_nonzero(comm)
                if nz:
                    result["hard_witness"] = {
                        "kind": "commutator-with-star", "q": q, "old": old_desc,
                        "new": f"core{core_index}*", "entry": nz,
                    }
                    return result
            generators.extend(((M, f"core{core_index}"), (Mstar, f"core{core_index}*")))
            add_independent(basis, descriptions, M, f"core{core_index}")
            add_independent(basis, descriptions, Mstar, f"core{core_index}*")
            if len(basis) > 2:
                result["hard_witness"] = {
                    "kind": "dimension", "q": q, "descriptions": descriptions[:3],
                    "minor": independent_minor3(basis[:3]),
                }
                return result
            close_star_algebra(basis, descriptions)
            if len(basis) > 2:
                result["hard_witness"] = {
                    "kind": "star-algebra-dimension", "q": q,
                    "descriptions": descriptions[:3], "minor": independent_minor3(basis[:3]),
                }
                return result
    return result


if __name__ == "__main__":
    raise SystemExit("Library-only design module: call scan(A,Abar) after a public pin.")
