"""Pre-pin diagnostic analysis for the ordered Z5 tests."""
import argparse
from collections import defaultdict
from decimal import Decimal
import hashlib
import types
import json
import math
import re
from pathlib import Path
from statistics import NormalDist, stdev
import sys

SCALES = (4, 6, 8)
RATIOS = (4, 6, 8)
SAMPLES = 4096
ENDPOINTS = {1024, 2048, 4096, 8192}
A_VOLUMES = {m: tuple(m * r for r in RATIOS) for m in SCALES}
D_VOLUMES = {r: tuple(8 * ((k * r + 7) // 8) for k in RATIOS)
             for r in SCALES}
D_MOMENTA = ("pi/4", "pi/2")
D_ORIENTATIONS = ("12", "01", "02", "03")
ROW_VOLUMES = {
    **{f"A:{channel}:{m}": A_VOLUMES[m]
       for channel in ("E", "M") for m in SCALES},
    **{f"D:{r}:{q}:{orientation}:2": D_VOLUMES[r]
       for r in SCALES for q in D_MOMENTA for orientation in D_ORIENTATIONS},
}
VOLUMES = sorted({L for row in ROW_VOLUMES.values() for L in row})
PRIMARY_COUNT = sum(map(len, ROW_VOLUMES.values()))
ROUNDING = Decimal(2) ** -30
SHA256 = re.compile(r"[a-f0-9]{64}\Z")
Z = NormalDist().inv_cdf(1 - 0.01 / (2 * PRIMARY_COUNT))
PILOT_DIAGNOSTICS_SHA = "d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce"


def load_diagnostics(path):
    payload = path.read_bytes()
    if hashlib.sha256(payload).hexdigest() != PILOT_DIAGNOSTICS_SHA:
        raise ValueError("Inherited diagnostics source hash mismatch")
    module = types.ModuleType("pinned_pilot_diagnostics")
    module.__file__ = str(path)
    sys.modules[module.__name__] = module
    exec(compile(payload, str(path), "exec", dont_inherit=True), module.__dict__)
    return module


def invalid_constant(value):
    raise ValueError("Non-finite JSON number: " + value)


def json_record(line):
    return json.loads(line, parse_float=Decimal, parse_constant=invalid_constant)


def get_chains(files, thermal):
    """Verify primary per-state enclosures and custody coordinates."""
    cells = defaultdict(lambda: defaultdict(dict))
    seen = set()
    for filename in files:
        with filename.open(encoding="utf-8") as source:
            for line in source:
                row = json_record(line)
                L, chain = row["L"], row["chain"]
                sample, macro = row["sample"], row["macrocycle"]
                identity = (L, chain, sample)
                if identity in seen:
                    raise ValueError(f"Duplicate state record {identity}")
                seen.add(identity)
                if L not in VOLUMES or type(L) is not int:
                    raise ValueError(f"Unregistered volume in record {identity}")
                if chain not in {f"L{L}-c{i}" for i in (1, 2, 3, 4)}:
                    raise ValueError(f"Unregistered chain in record {identity}")
                endpoint = thermal.get(str(L), {}).get("endpoint")
                if endpoint not in ENDPOINTS:
                    raise ValueError(f"No valid thermal endpoint for {identity}")
                if type(sample) is not int or not 0 <= sample < SAMPLES:
                    raise ValueError(f"Unregistered sample index {identity}")
                if type(macro) is not int or macro != endpoint + sample + 1:
                    raise ValueError(f"Wrong macrocycle for {identity}")
                digest = row.get("state_sha256")
                size = row.get("state_bytes")
                if not isinstance(digest, str) or not SHA256.fullmatch(digest) \
                        or type(size) is not int or not 4 * L**4 < size <= 4 * L**4 + 256:
                    raise ValueError(f"Invalid state SHA-256 or length for {identity}")
                values = row["observables"]
                for key, volumes in ROW_VOLUMES.items():
                    if L not in volumes:
                        continue
                    if key not in values:
                        raise ValueError(f"Missing primary {key} in {identity}")
                    bounds = values[key]
                    if not isinstance(bounds, list) or len(bounds) != 2:
                        raise ValueError(f"Invalid interval for {key} in {identity}")
                    lo, hi = map(Decimal, bounds)
                    if not lo.is_finite() or not hi.is_finite() or lo > hi:
                        raise ValueError(f"Invalid interval for {key} in {identity}")
                    if (hi - lo) / 2 > ROUNDING:
                        raise ValueError(f"Arithmetic budget exceeded for {key} in {identity}")
                    cells[(key, L)][chain][sample] = (lo + hi) / 2
    return cells


def batches(xs, length):
    return [math.fsum(xs[i:i + length]) / length
            for i in range(0, len(xs) - length + 1, length)]


def statistic(series, diagnostics):
    """Diagnostic Monte Carlo error; not a certified confidence bound."""
    values = [[float(x) for x in chain] for chain in series]
    mean = float(sum(sum(chain) for chain in series) / (4 * SAMPLES))
    chain_means = [math.fsum(chain) / SAMPLES for chain in values]
    sse = [stdev(chain_means) / 2]
    for length in (64, 128, 256, 512):
        per_chain = [batches(chain, length) for chain in values]
        sse.append(math.sqrt(sum(stdev(b) ** 2 / len(b) for b in per_chain)) / 4)
    se = max(sse)
    rh, folded = diagnostics.rank_folded_rhat(values)
    bulk, tail = diagnostics.bulk_tail_ess(values)
    mix_pass = (all(map(math.isfinite, (rh, folded, bulk, tail)))
                and rh <= 1.05 and folded <= 1.05 and bulk >= 400 and tail >= 200)
    half = math.nextafter(Z * se + float(ROUNDING), math.inf)
    low = math.nextafter(mean - half, -math.inf)
    high = math.nextafter(mean + half, math.inf)
    return {"mean": mean, "standard_error": se, "halfwidth": half,
            "interval": [low, high], "rhat": rh if math.isfinite(rh) else None,
            "folded": folded if math.isfinite(folded) else None,
            "bulk_ess": bulk if math.isfinite(bulk) else None,
            "tail_ess": tail if math.isfinite(tail) else None,
            "mix_pass": mix_pass}


def volume_rows(cells, thermal, diagnostics):
    rows = {}
    for key, volumes in ROW_VOLUMES.items():
        results = {}
        for L in volumes:
            cell = cells.get((key, L), {})
            chains = [cell.get(f"L{L}-c{i}", {}) for i in (1, 2, 3, 4)]
            counts = list(map(len, chains))
            thermal_record = thermal.get(str(L), {})
            if counts != [SAMPLES] * 4:
                results[str(L)] = {"status": "incomplete", "counts": counts}
                continue
            if (thermal_record.get("status") != "PASS"
                    or thermal_record.get("measurement_sentinels") != "PASS"):
                results[str(L)] = {"status": "mixing-unresolved", "counts": counts}
                continue
            if not thermal_record.get("replay_pass"):
                results[str(L)] = {"status": "replay-unverified", "counts": counts}
                continue
            data = [[chain[i] for i in range(SAMPLES)] for chain in chains]
            result = statistic(data, diagnostics)
            lo, hi = result["interval"]
            if not result["mix_pass"]:
                status = "mixing-unresolved"
            elif hi < 0 or (key.startswith("D:") and lo > 1):
                status = "finite-identity-flag"
            elif result["halfwidth"] > 1 / 128:
                status = "precision-unresolved"
            else:
                status = "diagnostic"
            results[str(L)] = {"status": status, **result}
        first = [results[str(L)] for L in volumes]
        row = {"volumes": results, "status": "volume-unresolved"}
        if all(x["status"] == "diagnostic" for x in first):
            drift = [abs(y["mean"] - x["mean"]) + x["halfwidth"] + y["halfwidth"]
                     for x, y in zip(first, first[1:])]
            row["volume_pair_drift"] = drift
            if max(drift) <= 1 / 32:
                row["status"] = "finite-volume-stable"
                row["envelope"] = [min(x["interval"][0] for x in first),
                                   max(x["interval"][1] for x in first)]
                if key.startswith("D:"):
                    row["tail_upper_display"] = min(1.0, row["envelope"][1] * 4 / 3)
        rows[key] = row
    return rows


def decisions(rows):
    def available(keys, predicate):
        return all("envelope" in rows[k] and predicate(rows[k]) for k in keys)

    positive_channels = [
        channel for channel in ("E", "M")
        if available((f"A:{channel}:{m}" for m in (6, 8)),
                     lambda row: row["envelope"][0] >= 1 / 64)
    ]
    small_a = available((f"A:{alpha}:{m}" for alpha in ("E", "M") for m in (6, 8)),
                        lambda row: row["envelope"][1] < 1 / 64)
    small_d = available(
        (f"D:{r}:{q}:{o}:2" for r in (6, 8)
         for q in D_MOMENTA for o in D_ORIENTATIONS),
        lambda row: row["tail_upper_display"] < 1 / 16,
    )
    return {
        "A": "finite-grid-support" if positive_channels else
             "finite-grid-small" if small_a else "unresolved",
        "positive_channels": positive_channels,
        "B": "finite-grid-tail-small" if small_d else "unresolved",
        "scope": "finite-grid diagnostic only",
    }


def series_identity(path):
    with path.open("rb") as data:
        first = data.readline()
        if not first:
            return None
        L = json_record(first.decode("utf-8"))["L"]
        checksum = hashlib.sha256(first)
        for chunk in iter(lambda: data.read(1 << 20), b""):
            checksum.update(chunk)
    return L, checksum.hexdigest()


def verify_replay_receipts(thermal, files, receipts):
    pending = set()
    available = {}
    if not receipts:
        return
    for file in files:
        if (identity := series_identity(file)) is not None:
            L, digest = identity
            if L in available:
                raise ValueError("Replay verification needs one ledger per volume")
            available[L] = digest
    for path in receipts:
        receipt = json.loads(path.read_text(encoding="utf-8"))
        L = receipt["L"]
        data = thermal.get(str(L))
        if (type(L) is not int or L not in VOLUMES or L in pending or not data
                or receipt["status"] != "PASS" or receipt["verified_states"] != 4 * SAMPLES
                or receipt["endpoint"] != data["endpoint"]
                or receipt["measurement_sha256"] != available.get(L)
                or receipt["sampler_sha256"] != data.get("sampler_sha256")
                or not SHA256.fullmatch(receipt["sampler_sha256"])):
            raise ValueError(f"Invalid replay receipt for volume {L}")
        pending.add(L)
        data["replay_pass"] = True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostics", required=True, type=Path)
    parser.add_argument("--thermal-receipts", required=True, type=Path, action="append")
    parser.add_argument("--replay-receipt", type=Path, action="append", default=[])
    parser.add_argument("measurement_jsonl", type=Path, nargs="*")
    args = parser.parse_args()
    diagnostics = load_diagnostics(args.diagnostics)
    thermal = {}
    for path in args.thermal_receipts:
        receipt = json.loads(path.read_text(encoding="utf-8"))
        if thermal.keys() & receipt.keys():
            raise ValueError("Duplicate thermal receipt for a volume")
        for record in receipt.values():
            record.pop("replay_pass", None)
        thermal.update(receipt)
    verify_replay_receipts(thermal, args.measurement_jsonl, args.replay_receipt)
    rows = volume_rows(get_chains(args.measurement_jsonl, thermal), thermal, diagnostics)
    print(json.dumps({"volume_rows": rows, "decisions": decisions(rows)},
                     allow_nan=False, indent=2))


if __name__ == "__main__":
    main()
