#!/usr/bin/env python3
"""Independent F_41 locator for frozen balanced one-leg covariants."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import re
from pathlib import Path

import numpy as np


P = 41
Z = 6
SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
PREREG_COMMIT = "8f8bd9a2e364a6e071fadb3efe3eed01dcd209ab"
PREREG_SHA256 = "d13fa55157a3616fd40fcc5c53d50638a0c4ff9edb6299092dae6a5af35be8cc"


def parse_tensor(source: Path):
    raw = source.read_bytes()
    if len(raw) != 8515 or hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
        raise RuntimeError("source pin mismatch")
    text = raw.decode()
    tail = text.split("U = [", 1)[1]
    amplitude_text, exponent_tail = tail.split("] .* w.^[", 1)
    exponent_text = exponent_tail.rsplit("];", 1)[0]
    labels = re.findall(r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])", amplitude_text)
    exponents = [int(x) for x in re.findall(r"(?<![A-Za-z0-9_])-?\d+(?![A-Za-z0-9_])", exponent_text)]
    if len(labels) != 1296 or len(exponents) != 1296:
        raise RuntimeError((len(labels), len(exponents)))

    if pow(Z, 40, P) != 1 or any(pow(Z, d, P) == 1 for d in (1, 2, 4, 5, 8, 10, 20)):
        raise RuntimeError("6 does not have exact order 40 modulo 41")
    w = Z * Z % P
    c = (pow(Z, 5, P) + pow(Z, -5, P)) * pow(2, -1, P) % P
    a = c * pow((w + pow(w, -1, P)) % P, -1, P) % P
    b = (w * w + pow(w, -2, P)) * a % P
    values = {"0": 0, "a": a, "b": b, "c": c}
    A = np.zeros((6, 6, 6, 6), dtype=np.int64)
    B = np.zeros_like(A)
    support = 0
    for pos, (label, exponent) in enumerate(zip(labels, exponents)):
        row, col = divmod(pos, 36)
        x = (row // 6, row % 6, col // 6, col % 6)
        if label != "0":
            support += 1
        A[x] = values[label] * pow(w, exponent, P) % P
        B[x] = values[label] * pow(w, -exponent, P) % P
    if support != 112:
        raise RuntimeError(f"support {support}")
    return raw, A, B, {"z": Z, "w": w, "a": a, "b": b, "c": c}


def diagrams(n):
    """Frozen descriptor order: q, pi_q, then other legs increasingly."""
    full_perms = tuple(itertools.permutations(range(n)))
    q_perms = tuple(itertools.permutations(range(1, n)))
    out = []
    for q in range(4):
        other_legs = tuple(ell for ell in range(4) if ell != q)
        for pi_q_tuple in q_perms:
            for choices in itertools.product(full_perms, repeat=3):
                pi = [None] * 4
                pi[q] = (0,) + pi_q_tuple  # 0 is an open placeholder, not a wire.
                for ell, choice in zip(other_legs, choices):
                    pi[ell] = choice
                out.append({"q": q, "n": n, "pi": tuple(pi)})
    expected = 4 * (8 if n == 2 else 432)
    if len(out) != expected:
        raise RuntimeError((n, len(out), expected))
    return out


def descriptor_text(d):
    return f"q={d['q']};n={d['n']};" + ";".join(
        f"pi{ell}=" + ",".join(map(str, d["pi"][ell])) for ell in range(4)
    )


def diagram_hash(ds):
    payload = "".join(descriptor_text(d) + "\n" for d in ds).encode()
    return hashlib.sha256(payload).hexdigest()


def connected_components(factors):
    remaining = set(range(len(factors)))
    comps = []
    while remaining:
        start = min(remaining)
        comp = {start}
        frontier = [start]
        remaining.remove(start)
        while frontier:
            i = frontier.pop()
            li = set(factors[i][1])
            hits = [j for j in sorted(remaining) if li.intersection(factors[j][1])]
            for j in hits:
                remaining.remove(j)
                comp.add(j)
                frontier.append(j)
        comps.append(sorted(comp))
    return comps


def contract_pair(left, right):
    a, la, ida = left
    b, lb, idb = right
    shared = sorted(set(la).intersection(lb), key=repr)
    axes_a = [la.index(x) for x in shared]
    axes_b = [lb.index(x) for x in shared]
    c = np.tensordot(a, b, axes=(axes_a, axes_b)) % P
    labels = tuple(x for i, x in enumerate(la) if i not in axes_a) + tuple(
        x for i, x in enumerate(lb) if i not in axes_b
    )
    return c, labels, min(ida, idb)


def contract_component(factors):
    work = list(factors)
    while len(work) > 1:
        options = []
        for i in range(len(work)):
            for j in range(i + 1, len(work)):
                shared = len(set(work[i][1]).intersection(work[j][1]))
                if not shared:
                    continue
                output_rank = len(work[i][1]) + len(work[j][1]) - 2 * shared
                options.append((-shared, output_rank, work[i][2], work[j][2], i, j))
        if not options:
            raise RuntimeError("connected component lost all shared labels")
        _, _, _, _, i, j = min(options)
        merged = contract_pair(work[i], work[j])
        work = [x for k, x in enumerate(work) if k not in (i, j)] + [merged]
    return work[0]


def covariant(A, B, d):
    q, n, pi = d["q"], d["n"], d["pi"]
    inverse = []
    for ell in range(4):
        inv = {}
        domain = range(1, n) if ell == q else range(n)
        for r in domain:
            inv[pi[ell][r]] = r
        inverse.append(inv)

    factors = []
    serial = 0
    for r in range(n):
        labels = []
        for ell in range(4):
            if ell == q and r == 0:
                labels.append(("open-row", q))
            else:
                labels.append(("wire", ell, r))
        factors.append((A, tuple(labels), serial))
        serial += 1
    for s in range(n):
        labels = []
        for ell in range(4):
            if ell == q and s == 0:
                labels.append(("open-col", q))
            else:
                labels.append(("wire", ell, inverse[ell][s]))
        factors.append((B, tuple(labels), serial))
        serial += 1

    pieces = []
    for comp in connected_components(factors):
        pieces.append(contract_component([factors[i] for i in comp]))
    result = pieces[0]
    for piece in pieces[1:]:
        a, la, ida = result
        b, lb, idb = piece
        result = (np.tensordot(a, b, axes=0) % P, la + lb, min(ida, idb))
    matrix, labels, _ = result
    desired = (("open-row", q), ("open-col", q))
    if set(labels) != set(desired) or len(labels) != 2:
        raise RuntimeError((d, labels, matrix.shape))
    matrix = np.transpose(matrix, axes=(labels.index(desired[0]), labels.index(desired[1]))) % P
    if matrix.shape != (6, 6):
        raise RuntimeError(matrix.shape)
    return matrix


def first_nonzero_entry(M):
    for i in range(6):
        for j in range(6):
            if int(M[i, j] % P):
                return i, j, int(M[i, j] % P)
    return None


def matrix_hash(M):
    return hashlib.sha256(bytes(int(x) for x in M.reshape(-1))).hexdigest()


def add_to_basis(basis, M):
    """Incremental row basis over F_41; basis stores (pivot, normalized vector)."""
    v = [int(x % P) for x in M.reshape(-1)]
    for pivot, row in basis:
        if v[pivot]:
            f = v[pivot]
            v = [(x - f * y) % P for x, y in zip(v, row)]
    nz = next((i for i, x in enumerate(v) if x), None)
    if nz is None:
        return False
    inv = pow(v[nz], -1, P)
    v = [(inv * x) % P for x in v]
    # Keep reduced pivots for stable diagnostics.
    new_basis = []
    for pivot, row in basis:
        if row[nz]:
            f = row[nz]
            row = [(x - f * y) % P for x, y in zip(row, v)]
        new_basis.append((pivot, row))
    new_basis.append((nz, v))
    new_basis.sort()
    basis[:] = new_basis
    return True


def run(source: Path, output_path: Path):
    raw, A, B, residues = parse_tensor(source)
    ds2 = diagrams(2)
    ds3 = diagrams(3)
    all_ds = ds2 + ds3
    output = {
        "prereg_commit": PREREG_COMMIT,
        "prereg_sha256": PREREG_SHA256,
        "source_bytes": len(raw),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "support": int(np.count_nonzero(A)),
        "f41_residues": residues,
        "diagram_counts": {"n2_total": len(ds2), "n2_per_leg": 8, "n3_total": len(ds3), "n3_per_leg": 432},
        "diagram_list_sha256": diagram_hash(all_ds),
        "n2": [],
        "n3_scanned": [],
        "witness": None,
    }

    matrices = {q: [] for q in range(4)}
    bases = {q: [] for q in range(4)}
    identity = np.eye(6, dtype=np.int64)
    for q in range(4):
        add_to_basis(bases[q], identity)

    # Every frozen n=2 diagram is computed before any n=3 scan.
    for global_index, d in enumerate(ds2):
        M = covariant(A, B, d)
        q = d["q"]
        comm_witness = None
        for prev_index, prev_d, prev_M in matrices[q]:
            comm = (M @ prev_M - prev_M @ M) % P
            nz = first_nonzero_entry(comm)
            if nz:
                comm_witness = {"previous_global_index": prev_index, "previous_descriptor": descriptor_text(prev_d), "entry": nz}
                break
        independent = add_to_basis(bases[q], M)
        record = {
            "global_index": global_index,
            "descriptor": descriptor_text(d),
            "matrix": M.tolist(),
            "matrix_sha256": matrix_hash(M),
            "independent_added": independent,
            "span_dimension_with_identity": len(bases[q]),
            "first_commutator": comm_witness,
        }
        output["n2"].append(record)
        matrices[q].append((global_index, d, M))
        if comm_witness or len(bases[q]) > 2:
            output["witness"] = {"stage": "n2", "new": record, "kind": "commutator" if comm_witness else "dimension"}
            break

    # The preregistered branch reaches n=3 only if all 32 n=2 matrices pass.
    if output["witness"] is None:
        n3_offset = len(ds2)
        for local_global_index, d in enumerate(ds3):
            global_index = n3_offset + local_global_index
            M = covariant(A, B, d)
            q = d["q"]
            comm_witness = None
            comm_matrix = None
            previous_record = None
            for prev_index, prev_d, prev_M in matrices[q]:
                comm = (M @ prev_M - prev_M @ M) % P
                nz = first_nonzero_entry(comm)
                if nz:
                    comm_witness = {
                        "previous_global_index": prev_index,
                        "previous_descriptor": descriptor_text(prev_d),
                        "entry": nz,
                    }
                    comm_matrix = comm
                    previous_record = (prev_index, prev_d, prev_M)
                    break
            independent = add_to_basis(bases[q], M)
            record = {
                "global_index": global_index,
                "descriptor": descriptor_text(d),
                "matrix": M.tolist(),
                "matrix_sha256": matrix_hash(M),
                "independent_added": independent,
                "span_dimension_with_identity": len(bases[q]),
                "first_commutator": comm_witness,
            }
            output["n3_scanned"].append(record)
            matrices[q].append((global_index, d, M))
            if comm_witness:
                prev_index, prev_d, prev_M = previous_record
                output["witness"] = {
                    "stage": "n3",
                    "kind": "commutator",
                    "leg": q,
                    "previous_global_index": prev_index,
                    "previous_descriptor": descriptor_text(prev_d),
                    "previous_matrix": prev_M.tolist(),
                    "previous_matrix_sha256": matrix_hash(prev_M),
                    "new_global_index": global_index,
                    "new_descriptor": descriptor_text(d),
                    "new_matrix": M.tolist(),
                    "new_matrix_sha256": matrix_hash(M),
                    "commutator": comm_matrix.tolist(),
                    "first_nonzero_entry_row_col_value": list(comm_witness["entry"]),
                }
                break
            if len(bases[q]) > 2:
                output["witness"] = {
                    "stage": "n3", "kind": "dimension", "leg": q,
                    "new_global_index": global_index, "new_descriptor": descriptor_text(d),
                    "new_matrix": M.tolist(), "new_matrix_sha256": matrix_hash(M),
                    "span_dimension_with_identity": len(bases[q]),
                }
                break

    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    summary = {
        "source_sha256": output["source_sha256"],
        "f41_residues": residues,
        "diagram_counts": output["diagram_counts"],
        "diagram_list_sha256": output["diagram_list_sha256"],
        "n2_computed": len(output["n2"]),
        "n2_span_dimensions": {str(q): len([b for b in bases[q]]) for q in range(4)},
        "n3_scanned": len(output["n3_scanned"]),
        "witness": output["witness"],
        "result_sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, default=Path("CROSSCHECK.json"))
    args = parser.parse_args()
    run(args.source, args.output)
