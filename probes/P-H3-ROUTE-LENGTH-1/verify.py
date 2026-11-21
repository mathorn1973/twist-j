# SPDX-License-Identifier: Apache-2.0
"""Replay both distance experiments and emit deterministic JSON Lines."""
import json
from hashlib import sha256

import kernel as k
import natural
import paired
import phase


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def emit(section, value):
    print(encode(dict(section=section, value=value)))


def prepare(record):
    # The digest commits to the complete word-pair witnesses and phase components.
    record["word_evidence_sha256"] = sha256(encode(record).encode()).hexdigest()
    for arm in record["phase_arms"].values():
        for key in ("components", "singular_breaks"):
            arm.pop(key, None)
    for comparison in record["comparisons"].values():
        if record["rank"] not in (4, 44):
            comparison.pop("arrival")
            comparison.pop("conversion")
    return record


def main():
    phase.self_test()
    findings, digest = k.Findings(), sha256()
    cuts, _, arrivals = k.bare_reference(findings, digest)
    if findings.counts:
        raise AssertionError(findings.first)
    emit("bare", {"ticks": k.PERIOD, "ranks": len(arrivals), "sha256": digest.hexdigest()})
    observations = natural.run(cuts, arrivals)
    ranks = observations.pop("ranks")
    emit("natural", observations)
    for record in ranks:
        for lengths in record["directions"].values():
            for length, counts in lengths.items():
                lengths[length] = {key: n for key, n in counts.items() if n}
        emit("natural_rank", record)

    measured = paired.run(cuts, arrivals)
    records = measured.pop("records")
    expected_keys = {(r, d) for r in range(85) for d in range(1, 5)}
    if {(r["rank"], r["distance"]) for r in records} != expected_keys or len(records) != 340:
        raise AssertionError("prepared rank or distance coverage")
    emit("prepared_protocol", measured)
    expected_accounts = records[0]["accounts"]
    for record in records:
        accounts = record["accounts"]
        if accounts != expected_accounts:
            raise AssertionError(("unequal starting accounts across lengths", record["rank"]))
        if accounts["plus"][2:] != accounts["minus"][2:] or any(
            accounts[label][-1] != q for label, q in (("plus", 2054), ("minus", 2054), ("zero", 774))
        ):
            raise AssertionError(("pulse energy", accounts))
        emit("prepared", prepare(record))


if __name__ == "__main__":
    main()
