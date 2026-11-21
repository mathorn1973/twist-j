"""Exercise Linux-bound exact streaming against the serial kernel on two sides."""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time
from unittest.mock import patch

import ordered_sentinels
import replay_ordered_volume as replay
import run_ordered_volume as driver


LIMIT = 205
SIDES = (16, 24)
ENDPOINTS = (1, 2)
SAMPLES = 2


def fixture_settings(side, chain):
    return f"L{side}-c{chain}", 0xF178A51000000000 + side * 16 + chain, (
        "cold" if chain < 3 else "hot"
    )


def fixture_assess(chains, diagnostics, *, measurement=False):
    sizes = {len(chain) for chain in chains}
    if len(chains) != len(driver.CHAIN_IDS) or len(sizes) != 1:
        raise ValueError("Unexpected engineering history lengths")
    size = sizes.pop()
    if size not in ENDPOINTS or (measurement and size != SAMPLES):
        raise ValueError("Unexpected engineering endpoint")
    return {"status": "PASS" if measurement or size == ENDPOINTS[-1] else "STOP_MIXING"}


def run_fixture(binary, root, side, deadline, affinity=None, reader_workers=0):
    root.mkdir()
    generated = root / "generation"
    generated.mkdir()
    digest = hashlib.sha256(binary.read_bytes()).hexdigest()
    environment = {"L": side, "sampler_sha256": digest}
    if affinity is not None:
        environment["affinity"] = driver.affinity_record(affinity)
    driver.json_file(generated / "environment.json", environment)
    started = time.monotonic()
    receipt = driver.run_volume(
        binary, None, generated, side, deadline, chain_workers=4, affinity=affinity,
        reader_workers=reader_workers,
    )
    expected = {"status": "PASS", "endpoint": 2, "measurement_sentinels": "PASS"}
    if receipt != expected:
        raise ValueError(f"Unexpected engineering fixture receipt: {receipt}")
    driver.json_file(generated / "receipts.json", {str(side): {**receipt, "sampler_sha256": digest}})
    generation_seconds = time.monotonic() - started

    remaining = math.floor(deadline - time.monotonic())
    if remaining < 1:
        raise TimeoutError("Engineering fixture budget exhausted before replay")
    replayed = root / "replay"
    replay.replay(generated, side, binary, replayed, remaining, chain_workers=4, affinity=affinity)
    driver.require_time(deadline)
    return {
        "replay_budget_seconds": remaining,
        "generation_seconds": generation_seconds,
        "replay_seconds": time.monotonic() - started - generation_seconds,
        "sampler_sha256": digest,
    }


def equal_file(reference, candidate, relative):
    if (reference / relative).read_bytes() != (candidate / relative).read_bytes():
        raise ValueError(f"Different canonical bytes for {relative}")


def check_pair(side, reference, candidate, affinity, runs):
    for filename in ("measurements.jsonl", "thermal-1.json", "thermal-2.json", "measurement-sentinels.json"):
        equal_file(reference, candidate, f"generation/{filename}")
    for group in ("generation/thermal-1-c", "generation/thermal-2-c",
                  "generation/measurement-c", "replay/replay-c"):
        for chain in driver.CHAIN_IDS:
            relative = f"{group}{chain}"
            equal_file(reference, candidate, f"{relative}/protocol.log")
            reference_command = json.loads((reference / relative / "command.json").read_bytes())
            candidate_command = json.loads((candidate / relative / "command.json").read_bytes())
            cpu_list = ",".join(map(str, affinity[chain - 1]))
            if (candidate_command[:3] != [driver.TASKSET, "-c", cpu_list]
                    or reference_command[1:] != candidate_command[4:]):
                raise ValueError(f"Unexpected affinity or changed sampler parameters for {relative}")

    ledger = (candidate / "generation" / "measurements.jsonl").read_bytes()
    ledger_digest = hashlib.sha256(ledger).hexdigest()
    expected_count = len(driver.CHAIN_IDS) * SAMPLES
    if len(ledger.splitlines()) != expected_count:
        raise ValueError("Engineering fixture ledger is incomplete")
    for mode, base in (("serial", reference), ("bound", candidate)):
        receipt = json.loads((base / "replay" / "replay-receipt.json").read_bytes())
        expected = {
            "status": "PASS", "L": side, "endpoint": 2,
            "sampler_sha256": runs[mode]["sampler_sha256"],
            "measurement_sha256": ledger_digest, "verified_states": expected_count,
            "chains": [
                {"chain": fixture_settings(side, chain)[0], "verified_states": SAMPLES}
                for chain in driver.CHAIN_IDS
            ],
            "wall_seconds": runs[mode]["replay_budget_seconds"],
        }
        if mode == "bound":
            expected["affinity"] = driver.affinity_record(affinity)
        if receipt != expected:
            raise ValueError(f"Unexpected full replay receipt for {mode}")
    return {"L": side, "ledger_sha256": ledger_digest, "verified_states_per_replay": expected_count,
            "runs": runs}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--serial", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--affinity", type=driver.parse_affinity, required=True)
    parser.add_argument("--reader-workers", type=int, choices=range(25), default=0)
    args = parser.parse_args()
    driver.validate_affinity(args.affinity, chain_workers=4)
    for binary in (args.candidate, args.serial):
        if not binary.is_absolute() or not binary.is_file() or not os.access(binary, os.X_OK):
            parser.error("Both sampler arguments must be absolute executable files")

    started = time.monotonic()
    deadline = started + LIMIT
    args.output.mkdir()
    results = []
    with patch.object(driver, "chain_settings", fixture_settings), \
         patch.object(replay, "chain_settings", fixture_settings), \
         patch.object(driver, "ENDPOINTS", ENDPOINTS), patch.object(driver, "SAMPLES", SAMPLES), \
         patch.object(replay, "ENDPOINTS", ENDPOINTS), patch.object(replay, "SAMPLES", SAMPLES), \
         patch.object(ordered_sentinels, "assess", fixture_assess):
        for side in SIDES:
            directory = args.output / f"L{side}"
            directory.mkdir()
            reference, candidate = directory / "serial", directory / "bound"
            runs = {
                "serial": run_fixture(args.serial, reference, side, deadline),
                "bound": run_fixture(args.candidate, candidate, side, deadline, args.affinity,
                                     reader_workers=args.reader_workers),
            }
            results.append(check_pair(side, reference, candidate, args.affinity, runs))
            driver.require_time(deadline)
    receipt = {"status": "PASS", "scope": "engineering fixture with scripted sentinel gate",
               "wall_seconds": time.monotonic() - started,
               "affinity": driver.affinity_record(args.affinity), "volumes": results,
               "reader_workers": args.reader_workers}
    driver.json_file(args.output / "BOUND-STREAM-PASS.json", receipt)
    print(json.dumps(receipt, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
