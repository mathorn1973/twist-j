"""Replay the saved-state SHA-256 ledger without reading phase observables."""
import argparse
import hashlib
from itertools import islice
import json
from pathlib import Path
import re
import time

from analyze_ordered import ENDPOINTS, SAMPLES, VOLUMES
from run_ordered_volume import (
    CHAIN_IDS, affinity_record, chain_settings, json_file, parse_affinity, run_chain,
    run_chains, state_size, validate_affinity,
)

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


def replay_chains(volume, L, sampler, output, deadline, endpoint, ledger, chain_workers, *, affinity=None):
    """Replay with one private monotone cursor and digest tuple per chain."""
    binding = {"affinity": affinity} if affinity is not None else {}
    def worker(i, cohort):
        name = chain_settings(L, i)[0]
        expected = tuple(ledger[(name, sample)] for sample in range(SAMPLES))
        verified = 0

        def verify_state(data, actual_L, chain, sample, macrocycle):
            nonlocal verified
            if (verified >= len(expected)
                    or (actual_L, chain, sample, macrocycle)
                    != (L, name, verified, endpoint + verified + 1)):
                raise ValueError(f"Unexpected replay state identity for {name}: {sample}")
            if hashlib.sha256(data).hexdigest() != expected[verified]:
                raise ValueError(f"Replay SHA-256 mismatch for {name} sample {sample}")
            verified += 1

        original = volume / f"measurement-c{i}" / "protocol.log"
        prefix = verified_prefix(original, endpoint)
        run_chain(sampler, output / f"replay-c{i}", deadline, L, i, endpoint, SAMPLES,
                  prefix, verify_state, cohort=cohort, **binding)
        if verified != len(expected):
            raise ValueError(f"Replay did not consume every saved-state receipt for {name}")
        return {"chain": name, "verified_states": verified}

    return run_chains(worker, chain_workers)


def replay(volume, L, sampler, output, wall_seconds, *, chain_workers=1, affinity=None):
    environment = json.loads((volume / "environment.json").read_text(encoding="utf-8"))
    executable_digest = hashlib.sha256(sampler.read_bytes()).hexdigest()
    receipt = json.loads((volume / "receipts.json").read_text(encoding="utf-8"))[str(L)]
    endpoint = receipt.get("endpoint")
    validate_affinity(affinity, chain_workers)
    binding_record = affinity_record(affinity) if affinity is not None else None
    if environment.get("affinity") != binding_record:
        raise ValueError("Replay affinity differs from generation")
    if (environment["L"] != L or executable_digest != environment["sampler_sha256"]
            or receipt["sampler_sha256"] != executable_digest
            or receipt["status"] != "PASS" or endpoint not in ENDPOINTS):
        raise ValueError("Invalid original configuration or incomplete measurement")
    series_digest, ledger = read_ledger(volume / "measurements.jsonl", L, endpoint)

    output.mkdir()
    deadline = time.monotonic() + wall_seconds
    binding = {"affinity": affinity} if affinity is not None else {}
    chains = replay_chains(volume, L, sampler, output, deadline, endpoint, ledger,
                           chain_workers, **binding)
    verified_states = sum(chain["verified_states"] for chain in chains)
    if verified_states != len(ledger):
        raise ValueError("Replay did not consume every saved-state receipt")
    replay_record = {
        "status": "PASS", "L": L, "endpoint": endpoint, "sampler_sha256": executable_digest,
        "measurement_sha256": series_digest, "verified_states": verified_states,
        "chains": chains,
        "wall_seconds": wall_seconds,
    }
    if binding_record is not None:
        replay_record["affinity"] = binding_record
    json_file(output / "replay-receipt.json", replay_record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", required=True, choices=VOLUMES, type=int)
    parser.add_argument("--original", required=True, type=Path)
    parser.add_argument("--sampler", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--wall-seconds", required=True, type=int)
    parser.add_argument("--chain-workers", type=int, choices=(1, 4), default=1)
    parser.add_argument("--affinity", type=parse_affinity, metavar="CPU-LIST;CPU-LIST;CPU-LIST;CPU-LIST")
    args = parser.parse_args()
    if args.wall_seconds < 1:
        parser.error("Wall budget must be positive")
    replay(args.original.resolve(strict=True), args.volume, args.sampler.resolve(strict=True),
           args.output.resolve(), args.wall_seconds, chain_workers=args.chain_workers,
           affinity=args.affinity)


if __name__ == "__main__":
    main()
