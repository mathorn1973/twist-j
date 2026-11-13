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
SAMPLES = 512
THIN = 64
VALIDATE_EVERY = 32


@dataclass(frozen=True)
class Spec:
    label: str
    L: int
    start: str
    seed: int


SPECS = (
    Spec("L3_cold_r1", 3, "cold", 0xD1210030000000000000000000000101),
    Spec("L3_cold_r2", 3, "cold", 0xD1210030000000000000000000000102),
    Spec("L3_witness_r1", 3, "witness", 0xD1210030000000000000000000000201),
    Spec("L3_minus_r1", 3, "minus_witness", 0xD1210030000000000000000000000301),
    Spec("L4_cold_r1", 4, "cold", 0xD1210040000000000000000000000101),
    Spec("L4_cold_r2", 4, "cold", 0xD1210040000000000000000000000102),
    Spec("L4_witness_r1", 4, "witness", 0xD1210040000000000000000000000201),
    Spec("L4_minus_r1", 4, "minus_witness", 0xD1210040000000000000000000000301),
)


def load_mobility():
    spec = importlib.util.spec_from_file_location("sector_flux_mobility", MOBILITY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen mobility kernel")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def site_coord_spatial(index: int, L: int) -> tuple[int, int, int]:
    x = [0, 0, 0]
    for axis in range(2, -1, -1):
        x[axis] = index % L
        index //= L
    return tuple(x)  # type: ignore[return-value]


def transfer_reading(mk, chain) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    lattice = chain.lattice
    L = lattice.L
    state = chain.state

    # r_by_t[t][spatial_site][i-1] for i=1,2,3.
    r_by_t = [
        [[0, 0, 0] for _ in range(L**3)]
        for _ in range(L)
    ]

    for t in range(L):
        for spatial_site in range(L**3):
            y = site_coord_spatial(spatial_site, L)
            x = (t, y[0], y[1], y[2])
            for j, i in enumerate((1, 2, 3)):
                p = lattice.plaq_index(x, 0, i)
                r_by_t[t][spatial_site][j] = mk.principal(state[p])

    common_w: tuple[int, int, int] | None = None
    sum_time_R = [0, 0, 0]

    for t in range(L):
        # Exact spatial mod-five divergence.
        for spatial_site in range(L**3):
            y = site_coord_spatial(spatial_site, L)
            div = 0
            for j in range(3):
                yprev = list(y)
                yprev[j] = (yprev[j] - 1) % L
                prev_site = (yprev[0] * L + yprev[1]) * L + yprev[2]
                div += r_by_t[t][prev_site][j] - r_by_t[t][spatial_site][j]
            if div % 5 != 0:
                raise AssertionError(("spatial_divergence", L, t, y, div))

        w_here = []
        for j in range(3):
            cut_values = []
            for cut in range(L):
                flux = 0
                for spatial_site in range(L**3):
                    y = site_coord_spatial(spatial_site, L)
                    if y[j] == cut:
                        flux += r_by_t[t][spatial_site][j]
                cut_values.append(flux % 5)
            if len(set(cut_values)) != 1:
                raise AssertionError(("cut_flux_not_constant", L, t, j, cut_values))
            w_here.append(cut_values[0])

            R = sum(r_by_t[t][s][j] for s in range(L**3))
            if (R - L * cut_values[0]) % 5 != 0:
                raise AssertionError(("R_congruence", L, t, j, R, cut_values[0]))
            sum_time_R[j] += R

        w_tuple = tuple(w_here)
        if common_w is None:
            common_w = w_tuple
        elif w_tuple != common_w:
            raise AssertionError(("time_winding_changed", L, t, common_w, w_tuple))

    assert common_w is not None
    return common_w, tuple(sum_time_R)


def run_chain(spec: Spec) -> dict[str, object]:
    mk = load_mobility()
    chain = mk.MobilityChain(spec.L, spec.seed, spec.start)
    chain.steps(WARMUP, validate_every=1024)
    mk.validate_state(chain.lattice, chain.state)

    counts: dict[tuple[int, int, int], int] = {}
    sum_time_R: dict[tuple[int, int, int], list[int]] = {}

    distinct_w: set[tuple[int, int, int]] = set()
    previous_w: tuple[int, int, int] | None = None
    changes = 0

    for sample in range(SAMPLES):
        chain.steps(THIN)
        if (sample + 1) % VALIDATE_EVERY == 0:
            mk.validate_state(chain.lattice, chain.state)

        w, Rsum = transfer_reading(mk, chain)
        distinct_w.add(w)
        if previous_w is not None and w != previous_w:
            changes += 1
        previous_w = w

        counts[w] = counts.get(w, 0) + 1
        bucket = sum_time_R.setdefault(w, [0, 0, 0])
        for i in range(3):
            bucket[i] += Rsum[i]

    guard = len(distinct_w) >= 16 and changes >= 32

    rows = []
    for w in sorted(counts):
        rows.append(
            {
                "w": w,
                "count": counts[w],
                "sum_time_R": tuple(sum_time_R[w]),
            }
        )

    return {
        "label": spec.label,
        "L": spec.L,
        "start": spec.start,
        "seed": f"0x{spec.seed:032x}",
        "distinct_w": len(distinct_w),
        "w_changes": changes,
        "guard": guard,
        "rows": rows,
        "state_sha256": mk.state_sha256(chain.state),
    }


def frac_text(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def merge_rows(results: list[dict[str, object]], L: int):
    counts: dict[tuple[int, int, int], int] = {}
    sums: dict[tuple[int, int, int], list[int]] = {}
    for result in results:
        if int(result["L"]) != L:
            continue
        for row in result["rows"]:  # type: ignore[index]
            w = tuple(row["w"])  # type: ignore[index]
            count = int(row["count"])  # type: ignore[index]
            rs = tuple(row["sum_time_R"])  # type: ignore[index]
            counts[w] = counts.get(w, 0) + count
            bucket = sums.setdefault(w, [0, 0, 0])
            for i in range(3):
                bucket[i] += int(rs[i])
    return counts, sums


def empirical_mazur(
    L: int,
    counts: dict[tuple[int, int, int], int],
    sums: dict[tuple[int, int, int], list[int]],
) -> tuple[Fraction, Fraction, Fraction]:
    N = sum(counts.values())
    assert N == 4 * SAMPLES
    out = []
    for i in range(3):
        q = Fraction(0)
        for w, count in counts.items():
            mean = Fraction(sums[w][i], L * count)
            q += Fraction(count, N) * mean * mean
        out.append(q / (L * L))
    return tuple(out)  # type: ignore[return-value]


def compact_sector_json(
    L: int,
    counts: dict[tuple[int, int, int], int],
    sums: dict[tuple[int, int, int], list[int]],
) -> str:
    data = {}
    for w in sorted(counts):
        key = "".join(str(x) for x in w)
        count = counts[w]
        means = [
            frac_text(Fraction(sums[w][i], L * count))
            for i in range(3)
        ]
        data[key] = [count, *means]
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def main() -> int:
    dependency_sha = hashlib.sha256(MOBILITY_PATH.read_bytes()).hexdigest()
    print(f"DEPENDENCY mobility_kernel_sha256={dependency_sha}")
    print(
        f"SCHEDULE warmup={WARMUP} samples={SAMPLES} thin={THIN} "
        f"validate_every={VALIDATE_EVERY}"
    )

    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(run_chain, SPECS))

    results.sort(key=lambda x: str(x["label"]))
    for result in results:
        print(
            "CHAIN "
            f"label={result['label']} L={result['L']} start={result['start']} "
            f"distinct_w={result['distinct_w']} w_changes={result['w_changes']} "
            f"guard={'PASS' if result['guard'] else 'FAIL'} "
            f"state_sha256={result['state_sha256']}"
        )

    all_guard = all(bool(r["guard"]) for r in results)
    mazur: dict[int, tuple[Fraction, Fraction, Fraction]] = {}

    for L in (3, 4):
        counts, sums = merge_rows(results, L)
        mazur[L] = empirical_mazur(L, counts, sums)
        N = sum(counts.values())
        p_nonzero = Fraction(N - counts.get((0, 0, 0), 0), N)
        print(
            f"POOL L={L} sectors={len(counts)} p_nonzero={frac_text(p_nonzero)} "
            f"M1={frac_text(mazur[L][0])} "
            f"M2={frac_text(mazur[L][1])} "
            f"M3={frac_text(mazur[L][2])}"
        )
        print(f"SECTORS L={L} data={compact_sector_json(L, counts, sums)}")

    if (
        all_guard
        and all(q > 0 for q in mazur[3])
        and all(mazur[4][i] >= mazur[3][i] / 2 for i in range(3))
    ):
        terminal = "NONCOLLAPSE-DIAGNOSTIC"
    elif (
        all_guard
        and all(mazur[4][i] <= mazur[3][i] / 4 for i in range(3))
    ):
        terminal = "COLLAPSE-DIAGNOSTIC"
    else:
        terminal = "INCONCLUSIVE"

    print(
        "RATIOS "
        + " ".join(
            f"M{i+1}_L4_over_L3={frac_text(mazur[4][i] / mazur[3][i]) if mazur[3][i] else 'NA'}"
            for i in range(3)
        )
    )
    print(f"ALL_GUARDS {'PASS' if all_guard else 'FAIL'}")
    print(f"TERMINAL {terminal}")
    print("STATUS ZERO_EVIDENCE_DIAGNOSTIC_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
