#!/usr/bin/env python3
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MOBILITY_PATH = (
    ROOT
    / "probes"
    / "P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1"
    / "mobility_kernel.py"
)

WARMUP = 4096
SAMPLES = 256
THIN = 64
VALIDATE_EVERY = 32
AUG_XOR = 0x5A5A5A5A5A5A5A5A5A5A5A5A5A5A5A5A
AUG_DOMAIN = b"r3diag1202-aug"


@dataclass(frozen=True)
class Spec:
    label: str
    L: int
    start: str
    seed: int


SPECS = (
    Spec("L3_cold_r1", 3, "cold", 0xD120203000000000000000000000101),
    Spec("L3_cold_r2", 3, "cold", 0xD120203000000000000000000000102),
    Spec("L3_witness_r1", 3, "witness", 0xD120203000000000000000000000201),
    Spec("L3_minus_r1", 3, "minus_witness", 0xD120203000000000000000000000301),
    Spec("L4_cold_r1", 4, "cold", 0xD120204000000000000000000000101),
    Spec("L4_cold_r2", 4, "cold", 0xD120204000000000000000000000102),
    Spec("L4_witness_r1", 4, "witness", 0xD120204000000000000000000000201),
    Spec("L4_minus_r1", 4, "minus_witness", 0xD120204000000000000000000000301),
)


def load_mobility():
    spec = importlib.util.spec_from_file_location("r3diag_mobility", MOBILITY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen mobility kernel")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1


def shuffle_exact(values: list[int], rng) -> None:
    for i in range(len(values) - 1, 0, -1):
        j = rng.bounded(i + 1)
        values[i], values[j] = values[j], values[i]


def augmented_observables(mk, chain, aug_rng) -> tuple[int, int, int]:
    lattice = chain.lattice
    state = chain.state
    dsu = DSU(lattice.n_plaq)
    occupied = [False] * lattice.n_plaq
    edge_entries: list[list[tuple[int, int]]] = [
        [] for _ in range(lattice.n_links)
    ]

    for site in range(lattice.volume):
        x = lattice.site_coord(site)
        for a, b in mk.PAIRS:
            p = lattice.plaq_index(x, a, b)
            value = mk.principal(state[p])
            if value == 0:
                continue
            occupied[p] = True
            for edge, eps in lattice.plaquette_boundary(x, a, b).items():
                edge_entries[edge].append((p, value * eps))

    charged_representatives: list[int] = []

    for entries in edge_entries:
        if not entries:
            continue
        total = sum(sign for _, sign in entries)
        if total == 0:
            positive = sorted(p for p, sign in entries if sign == 1)
            negative = sorted(p for p, sign in entries if sign == -1)
            if len(positive) != len(negative):
                raise AssertionError("neutral edge sign imbalance")
            shuffle_exact(negative, aug_rng)
            for p, q in zip(positive, negative):
                dsu.union(p, q)
        elif total in (-5, 5):
            if len(entries) != 5:
                raise AssertionError("charged edge degree is not five")
            expected = 1 if total == 5 else -1
            if any(sign != expected for _, sign in entries):
                raise AssertionError("charged edge is not aligned")
            root_face = entries[0][0]
            for p, _ in entries[1:]:
                dsu.union(root_face, p)
            charged_representatives.append(root_face)
        else:
            raise AssertionError(f"unexpected integer boundary {total}")

    current_nnz = sum(value != 0 for value in chain.current)
    if len(charged_representatives) != current_nnz:
        raise AssertionError(
            f"charged edge count mismatch {len(charged_representatives)} != {current_nnz}"
        )

    by_component: dict[int, int] = {}
    for p in charged_representatives:
        root = dsu.find(p)
        by_component[root] = by_component.get(root, 0) + 1

    C = len(charged_representatives)
    Mmax = max(by_component.values(), default=0)
    S4 = sum(M**4 for M in by_component.values())
    return C, Mmax, S4


def run_chain(spec: Spec) -> dict[str, object]:
    mk = load_mobility()
    chain = mk.MobilityChain(spec.L, spec.seed, spec.start)
    aug_rng = mk.BitStream(spec.seed ^ AUG_XOR, domain=AUG_DOMAIN)

    chain.steps(WARMUP, validate_every=1024)
    mk.validate_state(chain.lattice, chain.state)

    current_hashes: set[str] = set()
    previous_C: int | None = None
    C_changes = 0
    sum_C = 0
    sum_Mmax = 0
    sum_S4 = 0
    min_S4: int | None = None
    max_S4: int | None = None

    for sample in range(SAMPLES):
        chain.steps(THIN)
        if (sample + 1) % VALIDATE_EVERY == 0:
            mk.validate_state(chain.lattice, chain.state)

        current_hashes.add(mk.current_hash(chain.current))
        C, Mmax, S4 = augmented_observables(mk, chain, aug_rng)
        if previous_C is not None and C != previous_C:
            C_changes += 1
        previous_C = C

        sum_C += C
        sum_Mmax += Mmax
        sum_S4 += S4
        min_S4 = S4 if min_S4 is None else min(min_S4, S4)
        max_S4 = S4 if max_S4 is None else max(max_S4, S4)

    denom = SAMPLES * 4 * spec.L**4
    mean_R3 = Fraction(sum_S4, denom)
    mobility_pass = len(current_hashes) >= 16 and C_changes >= 16

    return {
        "label": spec.label,
        "L": spec.L,
        "start": spec.start,
        "seed": f"0x{spec.seed:032x}",
        "distinct_current_hashes": len(current_hashes),
        "C_changes": C_changes,
        "sum_C": sum_C,
        "sum_Mmax": sum_Mmax,
        "sum_S4": sum_S4,
        "min_S4": int(min_S4 or 0),
        "max_S4": int(max_S4 or 0),
        "mean_R3_num": mean_R3.numerator,
        "mean_R3_den": mean_R3.denominator,
        "mobility_pass": mobility_pass,
        "final_state_sha256": mk.state_sha256(chain.state),
    }


def frac_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def main() -> int:
    dependency_sha = hashlib.sha256(MOBILITY_PATH.read_bytes()).hexdigest()
    print(f"DEPENDENCY mobility_kernel_sha256={dependency_sha}")
    print(
        f"SCHEDULE warmup={WARMUP} samples={SAMPLES} thin={THIN} "
        f"validate_every={VALIDATE_EVERY}"
    )

    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(run_chain, SPECS))

    results.sort(key=lambda row: str(row["label"]))

    for row in results:
        mean = Fraction(int(row["mean_R3_num"]), int(row["mean_R3_den"]))
        print(
            "CHAIN "
            f"label={row['label']} L={row['L']} start={row['start']} "
            f"current_hashes={row['distinct_current_hashes']} "
            f"C_changes={row['C_changes']} sum_C={row['sum_C']} "
            f"sum_Mmax={row['sum_Mmax']} sum_S4={row['sum_S4']} "
            f"min_S4={row['min_S4']} max_S4={row['max_S4']} "
            f"mean_R3={frac_text(mean)} mobility={'PASS' if row['mobility_pass'] else 'FAIL'} "
            f"state_sha256={row['final_state_sha256']}"
        )

    all_mobile = all(bool(row["mobility_pass"]) for row in results)
    pooled: dict[int, Fraction] = {}
    overlap: dict[int, bool] = {}

    for L in (3, 4):
        rows = [row for row in results if int(row["L"]) == L]
        total_S4 = sum(int(row["sum_S4"]) for row in rows)
        pooled[L] = Fraction(total_S4, len(rows) * SAMPLES * 4 * L**4)

        cold = [row for row in rows if str(row["start"]) == "cold"]
        charged = [row for row in rows if str(row["start"]) != "cold"]
        cold_min = min(int(row["min_S4"]) for row in cold)
        cold_max = max(int(row["max_S4"]) for row in cold)
        charged_min = min(int(row["min_S4"]) for row in charged)
        charged_max = max(int(row["max_S4"]) for row in charged)
        overlap[L] = max(cold_min, charged_min) <= min(cold_max, charged_max)

        print(
            f"POOL L={L} mean_R3={frac_text(pooled[L])} "
            f"cold_S4_range={cold_min}:{cold_max} "
            f"charged_S4_range={charged_min}:{charged_max} "
            f"start_overlap={'PASS' if overlap[L] else 'FAIL'}"
        )

    if pooled[3] == 0:
        terminal = "INCONCLUSIVE"
    elif (
        all_mobile
        and overlap[3]
        and overlap[4]
        and pooled[4] <= 2 * pooled[3]
    ):
        terminal = "STABLE-DIAGNOSTIC"
    elif all_mobile and pooled[4] >= 4 * pooled[3] and pooled[4] > 0:
        terminal = "GROWTH-DIAGNOSTIC"
    else:
        terminal = "INCONCLUSIVE"

    ratio = Fraction(pooled[4], pooled[3]) if pooled[3] else Fraction(0, 1)
    print(
        f"RATIO mean_R3_L4_over_L3={frac_text(ratio)} "
        f"all_mobile={'PASS' if all_mobile else 'FAIL'}"
    )
    print(f"TERMINAL {terminal}")
    print("STATUS ZERO_EVIDENCE_DIAGNOSTIC_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
