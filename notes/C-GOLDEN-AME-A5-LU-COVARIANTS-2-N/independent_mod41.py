#!/usr/bin/env python3
"""Independent post-pin n=4 AME(4,6) covariant audit.

This file deliberately contains its own MATLAB-literal parser and a small
named-index tensor contractor.  It does not import any implementation or
result from the project under audit.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np


SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
PREREG_SHA256 = "b03ed300806c993cb4f4eac7249d9a6c2e7e9df9d96669d989445d4a1ade68f3"
CORES = (
    ((1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)),
    ((1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1)),
    ((1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)),
    ((1, 2, 3, 0), (3, 0, 1, 2), (2, 3, 0, 1)),
)


def sha256_bytes(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def parse_matlab_source(path: Path) -> tuple[list[str], np.ndarray]:
    """Return 1296 amplitude labels and the 36x36 phase-exponent array."""
    blob = path.read_bytes()
    got = sha256_bytes(blob)
    if got != SOURCE_SHA256:
        raise ValueError(f"source SHA mismatch: {got}")
    text = blob.decode("ascii")
    match = re.search(
        r"\bU\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        text,
        flags=re.S,
    )
    if match is None:
        raise ValueError("could not locate the two MATLAB 36x36 literals")
    amp_tokens = [x for x in re.split(r"[,;\s]+", match.group(1).strip()) if x]
    if any(x not in {"0", "a", "b", "c"} for x in amp_tokens):
        bad = sorted(set(amp_tokens) - {"0", "a", "b", "c"})
        raise ValueError(f"unexpected amplitude token(s): {bad}")
    phase_tokens = [int(x) for x in re.findall(r"\d+", match.group(2))]
    if len(amp_tokens) != 36 * 36 or len(phase_tokens) != 36 * 36:
        raise ValueError(
            f"literal sizes are amplitudes={len(amp_tokens)}, phases={len(phase_tokens)}"
        )
    return amp_tokens, np.array(phase_tokens, dtype=np.int64).reshape(36, 36)


def tensor_at_root(
    amp_tokens: Sequence[str], phases: np.ndarray, p: int, z: int, conjugate: bool
) -> np.ndarray:
    """Evaluate A or bar(A) in F_p, with w=z^2 and exact denominators."""
    inv = lambda x: pow(int(x), p - 2, p)
    w = z * z % p
    c = (pow(z, 5, p) + pow(inv(z), 5, p)) * inv(2) % p
    a = c * inv((w + inv(w)) % p) % p
    b = (pow(w, 2, p) + pow(inv(w), 2, p)) * a % p
    values = {"0": 0, "a": a, "b": b, "c": c}
    flat = np.fromiter((values[x] for x in amp_tokens), dtype=np.int64, count=1296)
    e = phases.reshape(-1)
    phase = np.fromiter(
        (pow(z, (-2 * int(k) if conjugate else 2 * int(k)) % (p - 1), p) for k in e),
        dtype=np.int64,
        count=1296,
    )
    return (flat * phase % p).reshape(6, 6, 6, 6)


@dataclass
class NamedTensor:
    data: np.ndarray
    labels: tuple[object, ...]
    name: str

    def __post_init__(self) -> None:
        if self.data.ndim != len(self.labels):
            raise ValueError(f"{self.name}: rank/label mismatch")
        if len(set(self.labels)) != len(self.labels):
            raise ValueError(f"{self.name}: duplicate index label")


def contract_pair(x: NamedTensor, y: NamedTensor, p: int, name: str) -> NamedTensor:
    shared = [label for label in x.labels if label in set(y.labels)]
    if not shared:
        raise ValueError(f"outer product forbidden: {x.name}, {y.name}")
    ax = [x.labels.index(label) for label in shared]
    ay = [y.labels.index(label) for label in shared]
    data = np.tensordot(x.data, y.data, axes=(ax, ay)) % p
    labels = tuple(label for label in x.labels if label not in shared) + tuple(
        label for label in y.labels if label not in shared
    )
    return NamedTensor(data, labels, name)


def build_network(
    left: np.ndarray,
    right: np.ndarray,
    q: int,
    core: Sequence[Sequence[int]],
    fix_row: int | None = None,
    fix_col: int | None = None,
) -> dict[str, NamedTensor]:
    """Build the bipartite colored network with p_q=id on copies 1,2,3."""
    if q not in range(4):
        raise ValueError(q)
    colors = [c for c in range(4) if c != q]
    permutations: dict[int, Sequence[int]] = {q: (0, 1, 2, 3)}
    permutations.update(zip(colors, core))

    labels_a: list[list[object | None]] = [[None] * 4 for _ in range(4)]
    labels_b: list[list[object | None]] = [[None] * 4 for _ in range(4)]
    for c in range(4):
        p_c = permutations[c]
        for r in range(4):
            s = p_c[r]
            if c == q and r == 0:
                labels_a[r][c] = "ROW"
                labels_b[s][c] = "COL"
            else:
                edge = ("e", c, r, s)
                labels_a[r][c] = edge
                labels_b[s][c] = edge

    out: dict[str, NamedTensor] = {}
    for r in range(4):
        data = left
        labels = list(labels_a[r])
        if r == 0 and fix_row is not None:
            data = np.take(data, fix_row, axis=q)
            del labels[q]
        out[f"A{r}"] = NamedTensor(data, tuple(labels), f"A{r}")
    for s in range(4):
        data = right
        labels = list(labels_b[s])
        if s == 0 and fix_col is not None:
            data = np.take(data, fix_col, axis=q)
            del labels[q]
        out[f"B{s}"] = NamedTensor(data, tuple(labels), f"B{s}")
    return out


def finish_output(x: NamedTensor) -> np.ndarray:
    wanted = [label for label in ("ROW", "COL") if label in x.labels]
    if set(x.labels) != set(wanted):
        raise ValueError(f"uncontracted labels: {x.labels}")
    if not wanted:
        return np.asarray(x.data).reshape(())
    axes = [x.labels.index(label) for label in wanted]
    return np.transpose(x.data, axes=axes)


def contract_frozen(nodes: dict[str, NamedTensor], p: int) -> np.ndarray:
    """The preregistered binary tree; works also with fixed output indices."""
    x03 = contract_pair(nodes["A0"], nodes["B3"], p, "X03")
    x32 = contract_pair(nodes["A3"], nodes["B2"], p, "X32")
    x = contract_pair(x03, x32, p, "X0332")
    x21 = contract_pair(nodes["A2"], nodes["B1"], p, "X21")
    x = contract_pair(x, x21, p, "Xmid")
    x = contract_pair(x, nodes["A1"], p, "XplusA1")
    x = contract_pair(x, nodes["B0"], p, "C")
    return finish_output(x) % p


def contract_greedy(
    nodes: dict[str, NamedTensor], p: int, trace: list[dict] | None = None
) -> np.ndarray:
    """Independent binary ordering chosen from labels, not the frozen tree."""
    work = list(nodes.values())
    while len(work) > 1:
        candidates = []
        for i in range(len(work)):
            for j in range(i + 1, len(work)):
                shared = set(work[i].labels) & set(work[j].labels)
                if not shared:
                    continue
                out_rank = work[i].data.ndim + work[j].data.ndim - 2 * len(shared)
                out_size = work[i].data.size * work[j].data.size // (6 ** (2 * len(shared)))
                # Reverse lexical names breaks the preregistered initial A0,B3 choice.
                candidates.append((out_rank, out_size, -len(shared), i, j))
        if not candidates:
            raise ValueError("network split into components")
        _, _, _, i, j = min(candidates)
        y = work.pop(j)
        x = work.pop(i)
        shared = [label for label in x.labels if label in set(y.labels)]
        z = contract_pair(x, y, p, f"({x.name}.{y.name})")
        if trace is not None:
            trace.append(
                {
                    "left": x.name,
                    "right": y.name,
                    "shared_count": len(shared),
                    "output_rank": z.data.ndim,
                }
            )
        work.append(z)
    return finish_output(work[0]) % p


def covariant(
    left: np.ndarray,
    right: np.ndarray,
    q: int,
    core: Sequence[Sequence[int]],
    p: int,
    method: str = "frozen",
    fix_row: int | None = None,
    fix_col: int | None = None,
) -> np.ndarray:
    nodes = build_network(left, right, q, core, fix_row, fix_col)
    if method == "frozen":
        return contract_frozen(nodes, p)
    if method == "greedy":
        return contract_greedy(nodes, p)
    raise ValueError(method)


def matrix_hash(a: np.ndarray) -> str:
    payload = "\n".join(",".join(str(int(x)) for x in row) for row in a.tolist()) + "\n"
    return sha256_bytes(payload.encode("ascii"))


def inverse_perm(p: Sequence[int]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for i, x in enumerate(p):
        ans[x] = i
    return tuple(ans)


def compose(p: Sequence[int], q: Sequence[int]) -> tuple[int, ...]:
    """Function composition p o q."""
    return tuple(p[q[i]] for i in range(len(q)))


def star_conjugator(core: Sequence[Sequence[int]]) -> tuple[int, ...] | None:
    for tail in itertools.permutations((1, 2, 3)):
        h = (0,) + tail
        hi = inverse_perm(h)
        transformed = tuple(compose(compose(h, inverse_perm(p)), hi) for p in core)
        if transformed == tuple(tuple(p) for p in core):
            return h
    return None


def is_scalar(a: np.ndarray, p: int) -> bool:
    return np.array_equal(a % p, np.eye(6, dtype=np.int64) * int(a[0, 0]) % p)


def first_nonzero(a: np.ndarray, p: int) -> tuple[int, int, int] | None:
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            v = int(a[i, j]) % p
            if v:
                return i, j, v
    return None


def first_commutator(mats: Sequence[np.ndarray], p: int):
    for j in range(len(mats)):
        for i in range(j):
            comm = (mats[i] @ mats[j] - mats[j] @ mats[i]) % p
            nz = first_nonzero(comm, p)
            if nz is not None:
                return {"pair": [i, j], "entry": list(nz), "matrix": comm.tolist()}
    return None


def rank_mod(rows: np.ndarray, p: int) -> int:
    a = np.array(rows, dtype=np.int64) % p
    m, n = a.shape
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if int(a[r, col]) % p), None)
        if pivot is None:
            continue
        a[[rank, pivot]] = a[[pivot, rank]]
        a[rank] = a[rank] * pow(int(a[rank, col]), p - 2, p) % p
        for r in range(m):
            if r != rank and a[r, col]:
                a[r] = (a[r] - int(a[r, col]) * a[rank]) % p
        rank += 1
        if rank == m:
            break
    return rank


def first_three_minor(mats: Sequence[np.ndarray], p: int):
    if len(mats) < 3:
        return None
    for ids in itertools.combinations(range(len(mats)), 3):
        flat = np.stack([mats[i].reshape(-1) for i in ids]) % p
        if rank_mod(flat, p) < 3:
            continue
        for cols in itertools.combinations(range(36), 3):
            sub = flat[:, cols]
            det = (
                int(sub[0, 0]) * (int(sub[1, 1]) * int(sub[2, 2]) - int(sub[1, 2]) * int(sub[2, 1]))
                - int(sub[0, 1]) * (int(sub[1, 0]) * int(sub[2, 2]) - int(sub[1, 2]) * int(sub[2, 0]))
                + int(sub[0, 2]) * (int(sub[1, 0]) * int(sub[2, 1]) - int(sub[1, 1]) * int(sub[2, 0]))
            ) % p
            if det:
                return {"matrices": list(ids), "flat_columns": list(cols), "det": det}
    return None


def closure_to_three(gens: Sequence[np.ndarray], p: int) -> dict:
    """Unital multiplication closure, retaining the first independent words."""
    basis = [np.eye(6, dtype=np.int64)]
    words = ["I"]

    def add(candidate: np.ndarray, word: str) -> bool:
        old = rank_mod(np.stack([x.reshape(-1) for x in basis]), p)
        trial = basis + [candidate % p]
        new = rank_mod(np.stack([x.reshape(-1) for x in trial]), p)
        if new > old:
            basis.append(candidate % p)
            words.append(word)
            return True
        return False

    for i, g in enumerate(gens):
        add(g, f"R{i}")
        if len(basis) >= 3:
            break
    while len(basis) < 3:
        before = len(basis)
        snapshot = list(zip(basis, words))
        for x, wx in snapshot:
            for y, wy in snapshot:
                if add(x @ y % p, f"({wx}*{wy})") and len(basis) >= 3:
                    break
            if len(basis) >= 3:
                break
        if len(basis) == before:
            break
    minor = first_three_minor(basis, p) if len(basis) >= 3 else None
    return {
        "dimension_reached": len(basis),
        "basis_words": words,
        "first_minor": minor,
    }


def modular_scan(source_path: Path, out_path: Path) -> dict:
    amp, phase = parse_matlab_source(source_path)
    p, z = 41, 6
    if pow(z, 40, p) != 1 or any(pow(z, d, p) == 1 for d in (1, 2, 4, 5, 8, 10, 20)):
        raise ValueError("z=6 does not have order 40")
    A = tensor_at_root(amp, phase, p, z, False)
    B = tensor_at_root(amp, phase, p, z, True)
    result: dict = {
        "source_sha256": SOURCE_SHA256,
        "prereg_sha256": PREREG_SHA256,
        "field": {"p": p, "z": z, "z_inverse": pow(z, p - 2, p)},
        "graph_star_conjugators": [],
        "legs": [],
    }
    for rid, core in enumerate(CORES):
        h = star_conjugator(core)
        if h is None:
            raise AssertionError(f"R{rid} not self-star under S3 fixing zero")
        result["graph_star_conjugators"].append(list(h))

    first_hard = None
    for q in range(4):
        matrices = []
        recs = []
        prefixes = []
        for rid, core in enumerate(CORES):
            C = covariant(A, B, q, core, p)
            # Correct star: swap A/bar(A), then transpose the open indices.
            Cstar = covariant(B, A, q, core, p).T % p
            if not np.array_equal(C, Cstar):
                delta = first_nonzero((C - Cstar) % p, p)
                raise AssertionError(f"star mismatch q={q} R{rid}: {delta}")
            matrices.append(C)
            recs.append(
                {
                    "core": rid,
                    "matrix": C.tolist(),
                    "star_matrix": Cstar.tolist(),
                    "matrix_sha256": matrix_hash(C),
                    "star_matrix_sha256": matrix_hash(Cstar),
                    "scalar": is_scalar(C, p),
                    "first_nonscalar_entry": None
                    if is_scalar(C, p)
                    else list(first_nonzero((C - np.eye(6, dtype=np.int64) * int(C[0, 0])) % p, p)),
                }
            )
            comm = first_commutator(matrices, p)
            direct = first_three_minor([np.eye(6, dtype=np.int64)] + matrices, p)
            closure = closure_to_three(matrices, p)
            prefix = {
                "through_core": rid,
                "first_commutator": comm,
                "direct_span_minor": direct,
                "closure": closure,
            }
            prefixes.append(prefix)
            if first_hard is None:
                if comm is not None:
                    first_hard = {"q": q, "through_core": rid, "kind": "commutator", "certificate": comm}
                elif direct is not None:
                    first_hard = {"q": q, "through_core": rid, "kind": "direct_span", "certificate": direct}
                elif closure["dimension_reached"] >= 3:
                    first_hard = {"q": q, "through_core": rid, "kind": "closure", "certificate": closure}
        seeded = [np.eye(6, dtype=np.int64)] + matrices
        leg = {
            "q": q,
            "cores": recs,
            "first_commutator": first_commutator(matrices, p),
            "span_rank_I_R0_R1_R2_R3": rank_mod(np.stack([x.reshape(-1) for x in seeded]), p),
            "first_three_minor_in_I_R0_R1_R2_R3": first_three_minor(seeded, p),
            "prefix_priority_audit": prefixes,
        }
        result["legs"].append(leg)
        print(
            f"q={q}: hashes={[r['matrix_sha256'][:12] for r in recs]} "
            f"scalar={[r['scalar'] for r in recs]} comm={leg['first_commutator'] and leg['first_commutator']['pair']} "
            f"span={leg['span_rank_I_R0_R1_R2_R3']}",
            flush=True,
        )
    result["first_hard_witness"] = first_hard
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--scan", action="store_true")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("INDEPENDENT_MOD41.json"),
    )
    args = parser.parse_args()
    if args.scan:
        modular_scan(args.source, args.output)
    else:
        parser.error("choose --scan")


if __name__ == "__main__":
    main()
