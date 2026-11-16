"""Replay the saved-state SHA-256 ledger without reading phase observables."""
import argparse
import hashlib
from itertools import islice
import json
from pathlib import Path
import re
import time

from analyze_ordered import ENDPOINTS, SAMPLES, VOLUMES
from run_ordered_volume import CHAIN_IDS, chain_settings, json_file, run_chain, state_size

SHA256 = re.compile(r"[a-f0-9]{64}\Z")


def read_ledger(path, L, endpoint):
    ledger = {}
    checksum = hashlib.sha256()
    chain_names = {chain_settings(L, i)[0] for i in CHAIN_IDS}
    with path.open("rb") as source:
        for line in source:
            checksum.update(line)
            row = json.loads(line)
            chain, sample = row["chain"], row["sample"]
            macrocycle = row["macrocycle"]
            identity = (chain, sample)
            digest = row["state_sha256"]
            if (row["L"] != L or chain not in chain_names or type(sample) is not int
                    or not 0 <= sample < SAMPLES or macrocycle != endpoint + sample + 1
                    or identity in ledger or not SHA256.fullmatch(digest)
                    or row["state_bytes"] != state_size(L, chain, sample, macrocycle)):
                raise ValueError("Invalid saved-state custody entry")
            ledger[identity] = digest
    if len(ledger) != len(CHAIN_IDS) * SAMPLES:
        raise ValueError("Replay requires a complete saved-state ledger")
    return checksum.hexdigest(), ledger


def verified_prefix(path, endpoint):
    with path.open(encoding="ascii") as source:
        prefix = [row.rstrip("\n") for row in islice(source, 2, 2 * endpoint + 1, 2)]
    if len(prefix) != endpoint or any(not row.startswith("SAMPLE ") for row in prefix):
        raise ValueError("Invalid measurement prefix log")
    return prefix


def replay(volume, L, sampler, output, wall_seconds):
    environment = json.loads((volume / "environment.json").read_text(encoding="utf-8"))
    executable_digest = hashlib.sha256(sampler.read_bytes()).hexdigest()
    receipt = json.loads((volume / "receipts.json").read_text(encoding="utf-8"))[str(L)]
    endpoint = receipt.get("endpoint")
    if (environment["L"] != L or executable_digest != environment["sampler_sha256"]
            or receipt["sampler_sha256"] != executable_digest
            or receipt["status"] != "PASS" or endpoint not in ENDPOINTS):
        raise ValueError("Invalid original configuration or incomplete measurement")
    series_digest, ledger = read_ledger(volume / "measurements.jsonl", L, endpoint)

    def verify_state(data, actual_L, chain, sample, macrocycle):
        if hashlib.sha256(data).hexdigest() != ledger.pop((chain, sample)):
            raise ValueError(f"Replay SHA-256 mismatch for {chain} sample {sample}")

    output.mkdir()
    deadline = time.monotonic() + wall_seconds
    for i in CHAIN_IDS:
        original = volume / f"measurement-c{i}" / "protocol.log"
        prefix = verified_prefix(original, endpoint)
        run_chain(sampler, output / f"replay-c{i}", deadline, L, i, endpoint, SAMPLES,
                  prefix, verify_state)
    if ledger:
        raise ValueError("Replay did not consume every saved-state receipt")
    json_file(output / "replay-receipt.json", {
        "status": "PASS", "L": L, "endpoint": endpoint, "sampler_sha256": executable_digest,
        "measurement_sha256": series_digest, "verified_states": len(CHAIN_IDS) * SAMPLES,
        "wall_seconds": wall_seconds,
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", required=True, choices=VOLUMES, type=int)
    parser.add_argument("--original", required=True, type=Path)
    parser.add_argument("--sampler", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--wall-seconds", required=True, type=int)
    args = parser.parse_args()
    if args.wall_seconds < 1:
        parser.error("Wall budget must be positive")
    replay(args.original.resolve(strict=True), args.volume, args.sampler.resolve(strict=True),
           args.output.resolve(), args.wall_seconds)


if __name__ == "__main__":
    main()
