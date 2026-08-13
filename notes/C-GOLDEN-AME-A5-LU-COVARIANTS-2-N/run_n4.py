#!/usr/bin/env python3
"""Independent G0--G3 runner for the publicly pinned n=4 continuation."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
import re
import sys
from pathlib import Path

import numpy as np


PIN_COMMIT = "1a813b6f50435d83e0dfd5011898a03fc5e4b089"
PIN_TREE = "1a61fc296079a9a2964ba4649900851f7b25ec9a"
PREREG_SHA256 = "b03ed300806c993cb4f4eac7249d9a6c2e7e9df9d96669d989445d4a1ade68f3"
SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"


def load_engine(path):
    spec = importlib.util.spec_from_file_location("pinned_n4_locator_engine", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_mod41(source):
    raw = source.read_bytes()
    if len(raw) != 8515 or hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
        raise RuntimeError("source pin mismatch")
    text = raw.decode()
    tail = text.split("U = [", 1)[1]
    amp_text, exp_tail = tail.split("] .* w.^[", 1)
    exp_text = exp_tail.rsplit("];", 1)[0]
    labels = re.findall(r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])", amp_text)
    exponents = [int(x) for x in re.findall(r"(?<![A-Za-z0-9_])-?\d+(?![A-Za-z0-9_])", exp_text)]
    if len(labels) != 1296 or len(exponents) != 1296:
        raise RuntimeError("parser shape mismatch")
    p, z = 41, 6
    if pow(z, 40, p) != 1 or any(pow(z, d, p) == 1 for d in (1, 2, 4, 5, 8, 10, 20)):
        raise RuntimeError("z residue lacks order 40")
    w = z * z % p
    c = (pow(z, 5, p) + pow(z, -5, p)) * pow(2, -1, p) % p
    a = c * pow((w + pow(w, -1, p)) % p, -1, p) % p
    b = (w * w + pow(w, -2, p)) * a % p
    values = {"0": 0, "a": a, "b": b, "c": c}
    A = np.zeros((6, 6, 6, 6), dtype=np.int64)
    Abar = np.zeros_like(A)
    amplitude_counts = {"a": 0, "b": 0, "c": 0}
    for pos, (label, exponent) in enumerate(zip(labels, exponents)):
        row, col = divmod(pos, 36)
        x = (row // 6, row % 6, col // 6, col % 6)
        A[x] = values[label] * pow(w, exponent, p) % p
        Abar[x] = values[label] * pow(w, -exponent, p) % p
        if label != "0":
            amplitude_counts[label] += 1
    if np.count_nonzero(A) != 112:
        raise RuntimeError("support mismatch")
    return raw, A, Abar, {"z": z, "zbar": pow(z, -1, p), "w": w, "a": a, "b": b, "c": c}, amplitude_counts


def matrix_sha(M):
    return hashlib.sha256(bytes(int(x % 41) for x in M.reshape(-1))).hexdigest()


def scalar_value(M):
    lam = int(M[0, 0] % 41)
    return lam if np.array_equal(M % 41, np.eye(6, dtype=np.int64) * lam % 41) else None


def first_nonzero(M):
    for i in range(6):
        for j in range(6):
            if int(M[i, j] % 41):
                return [i, j, int(M[i, j] % 41)]
    return None


def rank_mod41(matrices):
    rows = [[int(x % 41) for x in M.reshape(-1)] for M in matrices]
    rank = 0
    pivots = []
    for col in range(36):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, 41)
        rows[rank] = [inv * x % 41 for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(x - f * y) % 41 for x, y in zip(rows[i], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    return rank, pivots


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) % 41


def first_minor3(matrices):
    flat = [[int(x % 41) for x in M.reshape(-1)] for M in matrices]
    for cols in itertools.combinations(range(36), 3):
        value = det3([[flat[i][j] for j in cols] for i in range(3)])
        if value:
            return {
                "flat_positions": list(cols),
                "matrix_positions": [list(divmod(c, 6)) for c in cols],
                "determinant": value,
            }
    return None


def first_hard_witness(records):
    I = np.eye(6, dtype=np.int64)
    first_nonscalar = None
    per_leg = {}
    hard = None
    for q in range(4):
        generators = []
        basis = [(I, "I")]
        steps = []
        for record in [x for x in records if x["q"] == q]:
            M = np.asarray(record["matrix"], dtype=np.int64)
            desc = f"R{record['core_index']}"
            if record["scalar"] is None and first_nonscalar is None:
                first_nonscalar = {"q": q, "core_index": record["core_index"], "descriptor": record["descriptor"]}
            # Priority 1: all commutators with earlier generators. Self-star is
            # equal by the mandatory audit and has zero commutator.
            for N, olddesc in generators:
                comm = (N @ M - M @ N) % 41
                nz = first_nonzero(comm)
                if nz and hard is None:
                    hard = {
                        "kind": "commutator", "q": q, "left": olddesc,
                        "right": desc, "first_nonzero_row_col_value": nz,
                        "commutator": comm.tolist(),
                    }
                    break
            if hard is not None:
                steps.append({"after": desc, "hard": hard})
                break
            generators.append((M, desc))

            # Add if independent; priority 2 detects the first 3D span.
            old_rank, _ = rank_mod41([x[0] for x in basis])
            new_rank, _ = rank_mod41([x[0] for x in basis] + [M])
            if new_rank > old_rank:
                basis.append((M, desc))
            if len(basis) >= 3 and hard is None:
                triple = basis[:3]
                hard = {
                    "kind": "dimension", "q": q,
                    "matrices": [x[1] for x in triple],
                    "minor": first_minor3([x[0] for x in triple]),
                }
                steps.append({"after": desc, "basis": [x[1] for x in basis], "hard": hard})
                break

            # Priority 3: star algebra closure. Star adds nothing after the
            # graph-self-adjoint audit, so multiply the current basis.
            changed = True
            while changed and len(basis) < 3:
                changed = False
                snapshot = list(basis)
                for X, dx in snapshot:
                    for Y, dy in snapshot:
                        product = X @ Y % 41
                        old_rank, _ = rank_mod41([x[0] for x in basis])
                        new_rank, _ = rank_mod41([x[0] for x in basis] + [product])
                        if new_rank > old_rank:
                            basis.append((product, f"({dx})({dy})"))
                            changed = True
                            if len(basis) >= 3:
                                triple = basis[:3]
                                hard = {
                                    "kind": "star-algebra-dimension", "q": q,
                                    "matrices": [x[1] for x in triple],
                                    "minor": first_minor3([x[0] for x in triple]),
                                }
                                break
                    if hard is not None:
                        break
                if hard is not None:
                    break
            steps.append({"after": desc, "basis": [x[1] for x in basis], "hard": hard})
            if hard is not None:
                break
        per_leg[str(q)] = steps
        if hard is not None:
            break
    return first_nonscalar, hard, per_leg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--prereg", type=Path, default=Path(__file__).with_name("PREREG.md"))
    parser.add_argument("--engine", type=Path, default=Path(__file__).with_name("n4_locator_engine.py"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("MODULAR_RESULT.json"))
    args = parser.parse_args()
    engine = load_engine(args.engine)
    prereg_raw = args.prereg.read_bytes()
    if hashlib.sha256(prereg_raw).hexdigest() != PREREG_SHA256:
        raise RuntimeError("prereg hash mismatch")
    raw, A, Abar, residues, amplitude_counts = parse_mod41(args.source)

    records = []
    for q in range(4):
        for core_index, core in enumerate(engine.CORES):
            M = engine.core_covariant(A, Abar, q, core)
            star = engine.core_covariant(Abar, A, q, core).T % 41
            if not np.array_equal(M, star):
                raise RuntimeError(f"star audit failed q={q} R={core_index}")
            records.append({
                "q": q,
                "core_index": core_index,
                "descriptor": [list(p) for p in core],
                "matrix": M.tolist(),
                "star_matrix": star.tolist(),
                "matrix_sha256": matrix_sha(M),
                "star_matrix_sha256": matrix_sha(star),
                "star_equal": True,
                "scalar": scalar_value(M),
                "first_nonscalar_entry_after_subtracting_M00I": first_nonzero((M - np.eye(6, dtype=np.int64) * int(M[0, 0])) % 41),
            })
    first_nonscalar, hard, algebra_steps = first_hard_witness(records)
    result = {
        "public_pin": {"commit": PIN_COMMIT, "tree": PIN_TREE, "prereg_sha256": PREREG_SHA256},
        "source": {
            "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
            "support": int(np.count_nonzero(A)), "amplitude_counts": amplitude_counts,
        },
        "f41": {"residues": residues, "denominators": {"2": 2, "w_plus_w_inverse": (residues["w"] + pow(residues["w"], -1, 41)) % 41}},
        "representative_count": len(records),
        "records": records,
        "first_nonscalar": first_nonscalar,
        "first_hard_witness": hard,
        "algebra_steps_until_first_hard": algebra_steps,
    }
    out = args.output
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    summary = {
        "source": result["source"], "f41": result["f41"],
        "matrices": [
            {k: r[k] for k in ("q", "core_index", "descriptor", "matrix_sha256", "star_equal", "scalar", "matrix")}
            for r in records
        ],
        "first_nonscalar": first_nonscalar,
        "first_hard_witness": hard,
        "modular_result_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
