#!/usr/bin/env python3
"""Post-run format comparison only; imports or executes no scientific code.

Created after the independently frozen review.py completed.  Reads its own
scratch dump and the exact pinned target files, hashes their bytes, and
reformats already observed values into the author's published hash streams.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re


TARGET_HEAD = "26731e2bd7f1394b4d274528525e6d78cbe6bbf9"
TARGET_HASHES = {
    "verify.py": "fbee888930ac613c517c2ec0b4312c5b7b9860d1e1f21be21e9d12ba03cf0884",
    "EXPECTED.txt": "40a71401c28406605aea666a40fec5f773505d3a5b56b82897cdc09ad4c1952c",
    "WORD535.txt": "ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b",
}
FROZEN_REVIEW = "e615346185100da3aa68bc5d6432ac5781752ce16311a97cac71378586de1eb8"
FROZEN_SCOPE = "0e9a48d6d5c41dc2def54a911c45e8a3aa8e1e6673d2b99d6c98ebb71b75f482"


def compact(value):
    return json.dumps(value, separators=(",", ":")).encode("ascii")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stream_hash(rows):
    digest = hashlib.sha256()
    for row in rows:
        digest.update(compact(row))
    return digest.hexdigest()


def selector(state):
    token = [1, 0, -1, 0]
    indices = [i for i, value in enumerate(state[6:9]) if value == token]
    if len(indices) != 1:
        raise AssertionError("postcomparison selector outside frozen chart")
    return indices[0]


def labels_from_current_banks(state):
    absent = [[0, 1, 1, 1], [0, -1, -1, -1]]
    present = [[0, -1, -1, 0], [0, 1, 1, 0]]
    labels = []
    for base in (11, 21, 31, 41):
        changed = []
        for p in range(5):
            pair = state[base + 2 * p : base + 2 * p + 2]
            if pair not in (absent, present):
                raise AssertionError("postcomparison bank outside valid alphabet")
            if pair == present:
                changed.append(p)
        if len(changed) != 1:
            raise AssertionError("postcomparison bank is not singly occupied")
        labels.append(changed[0])
    return labels


def decode(labels):
    values = []
    for x, y in (labels[:2], labels[2:]):
        difference = (x - y) % 5
        if difference not in (1, 3):
            raise AssertionError("postcomparison record difference invalid")
        values.extend([int(difference == 3), (-x) % 5])
    return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--review-dir", type=Path, default=Path(__file__).parent)
    parser.add_argument("--target-dir", type=Path, required=True)
    parser.add_argument("--dump", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.review_dir
    assert sha((root / "review.py").read_bytes()) == FROZEN_REVIEW
    assert sha((root / "REVIEW-SCOPE.md").read_bytes()) == FROZEN_SCOPE
    for name, expected in TARGET_HASHES.items():
        assert sha((args.target_dir / name).read_bytes()) == expected, name
    own_bytes = (root / "EXPECTED.txt").read_bytes()
    own = json.loads(own_bytes)
    run = json.loads((root / "run_review.json").read_text())
    assert sha(own_bytes) == run["stdout_sha256"]
    assert run["exit_code"] == 0 and run["stderr_bytes"] == 0
    target = json.loads((args.target_dir / "EXPECTED.txt").read_text())
    dump = json.loads((args.dump or root / "review-dump.json").read_text())
    assert sha(compact(dump["endpoints"])) == own["endpoint_sha256"]
    assert sha(compact(dump["checkpoints"])) == own["checkpoint_sha256"]
    line_word = "".join(f"{kind},{i},{j}\n" for kind, i, j in dump["operations"]).encode("ascii")
    assert sha(line_word) == own["operation_word_sha256"]

    target_word = [(int(i) - 1, int(j) - 1)
                   for i, j in re.findall(r"C\((\d+),(\d+)\)",
                                         (args.target_dir / "WORD535.txt").read_text())]
    same_oriented_s = [list(edge) for edge in target_word] == dump["S_edges"]
    assert len(target_word) == 535

    checkpoints = dump["checkpoints"]
    read_rows, step_rows, reload_rows = [], [], []
    by_boundary = {}
    for parameters, kind, stage, step, read_index, state in checkpoints:
        by_boundary[(tuple(parameters), kind, stage, step, read_index)] = state
        if kind == "R":
            read_rows.append([parameters, stage, step, read_index, state])
        elif kind == "S":
            step_rows.append([parameters, stage, step + 1, state])
        elif kind == "LOAD":
            reload_rows.append([parameters, state])
        else:
            raise AssertionError("unknown frozen checkpoint kind")

    # Recover actual pre-read selectors from earlier observed complete states.
    # The only initial value used is the declared common selector A at stage0.
    event_stages = {}
    for parameters, stage, events in dump["events"]:
        reformatted = []
        for step, read_index, onset_c, onset_op, completion_c, completion_op in events:
            params = tuple(parameters)
            if read_index == 1:
                prior = by_boundary[(params, "R", stage, step, 0)]
                before = selector(prior)  # F inverse touches source only.
            elif step:
                before = selector(by_boundary[(params, "S", stage, step - 1, -1)])
            elif stage:
                before = selector(by_boundary[(params, "LOAD", -1, -1, -1)])
            else:
                before = 0
            reformatted.append({
                "tick": step, "read": read_index, "selector_before": before,
                "onset_contact": onset_c, "onset_operation": onset_op,
                "completion_contact": completion_c, "completion_operation": completion_op,
            })
        event_stages[(tuple(parameters), stage)] = reformatted

    event_rows, decoded_rows, codes = [], [], []
    for parameters, state in dump["endpoints"]:
        event_rows.append([parameters, [event_stages[(tuple(parameters), 0)],
                                        event_stages[(tuple(parameters), 1)]]])
        labels = labels_from_current_banks(state)
        answer = decode(labels)
        assert answer == parameters
        decoded_rows.append([parameters, labels, answer])
        codes.append(labels)

    converted = {
        "complete_program_sha256": sha(compact(dump["operations"])),
        "endpoint_sha256": stream_hash(dump["endpoints"]),
        "read_checkpoint_sha256": stream_hash(read_rows),
        "step_checkpoint_sha256": stream_hash(step_rows),
        "reload_checkpoint_sha256": stream_hash(reload_rows),
        "event_sha256": stream_hash(event_rows),
        "decoded_sha256": stream_hash(decoded_rows),
    }
    matches = {name: value == target[name] for name, value in converted.items()}
    counter_mapping = {
        "R_checkpoints": "full_read_checkpoints",
        "S_checkpoints": "full_step_checkpoints",
        "reload_checkpoints": "full_reload_checkpoints",
        "designated_events": "events",
        "full_native_inverses": "complete_inverses",
        "trajectory_contact_applications": "paired_arithmetic_contact_applications",
        "trajectory_swap_applications": "paired_arithmetic_swap_applications",
        "separate_fixture_contacts": "source_orbit_setup_contacts_excluded",
        "distinct_ordered_contact_pairs": "distinct_four_coefficient_pair_checks",
    }
    count_matches = {name: own[name] == target[author] for name, author in counter_mapping.items()}
    assert same_oriented_s and all(matches.values()) and all(count_matches.values())
    assert sorted(codes) == target["record_quadruples"]
    result = {
        "status": "PASS",
        "target_head": TARGET_HEAD,
        "independent_source_pin": run["source_pin"],
        "comparison_after_own_scientific_execution": True,
        "target_source_hashes": TARGET_HASHES,
        "frozen_review_sha256": FROZEN_REVIEW,
        "frozen_scope_sha256": FROZEN_SCOPE,
        "same_literal_535_oriented_edges": same_oriented_s,
        "published_hash_matches_after_explicit_format_conversion": matches,
        "converted_published_hashes": converted,
        "counter_matches": count_matches,
        "same_sorted_actual_record_quadruples": sorted(codes) == target["record_quadruples"],
        "independent_reader_rejection_count": own["strict_reader_rejections"],
        "converted_read_rows": len(read_rows),
        "converted_step_rows": len(step_rows),
        "converted_reload_rows": len(reload_rows),
        "normalization": "stream compact per-row JSON; S tick+1; explicit event dictionaries; no trajectory rerun",
    }
    output = args.output or root / "COMPARISON.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
