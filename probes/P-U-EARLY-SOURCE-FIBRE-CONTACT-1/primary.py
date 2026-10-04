#!/usr/bin/env python3
"""Exact native early-contact audit. No run is authorized before public pin.

No arguments: stdout-only deterministic JSON for the repository wrapper.
--output-dir NEW: also retain the frozen scientific CSV/JSON evidence there.
Only standard-library exact integers are used. No sealed verifier is imported.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import itertools
import json
import os
from pathlib import Path
import re
import sys


FIVE = range(5)
POINTS = tuple(itertools.product(FIVE, repeat=2))
NONZERO_POINTS = tuple(p for p in POINTS if p != (0, 0))
INVERSE = (0, 1, 3, 2, 4)
MAX_EVIDENCE_BYTES = 5 * 1024 * 1024


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: object, *, pretty: bool = False) -> bytes:
    kwargs = {"sort_keys": True, "ensure_ascii": True}
    if pretty:
        kwargs["indent"] = 2
    else:
        kwargs["separators"] = (",", ":")
    return (json.dumps(value, **kwargs) + "\n").encode("utf-8")


def check_integrity(bundle: Path, repository: Path) -> dict:
    need(sys.flags.optimize == 0, "Python optimization is forbidden")
    source_path = bundle / "SOURCE.json"
    source = json.loads(source_path.read_text(encoding="utf-8"))
    pin_path = bundle / "INPUTS.sha256"
    pin_bytes = pin_path.read_bytes()
    pinned = {}
    for line in pin_bytes.decode("utf-8").splitlines():
        need(bool(line), "blank INPUTS line")
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        need(match is not None, "invalid INPUTS line")
        digest, name = match.groups()
        need(name not in pinned, "duplicate INPUTS entry")
        need(name != "INPUTS.sha256", "self-referential INPUTS entry")
        need(sha256((bundle / name).read_bytes()) == digest,
             "bundle hash mismatch: " + name)
        pinned[name] = digest
    independent = source["independent_script"]
    need(independent == "independent_native.py", "unexpected independent script")
    required = {"primary.py", "verify.py", independent,
                "PREREG.md", "PROOF.md", "SOURCE.json"}
    need(required <= pinned.keys(), "missing required pinned dependency")
    need(source["public_commit"] ==
         "5e872c22a18043c8126945a982efad55472cea82", "unexpected source base")
    for name, entry in source["files"].items():
        rel = Path(name)
        need(not rel.is_absolute() and ".." not in rel.parts,
             "invalid source path")
        data = (repository / rel).read_bytes()
        need(len(data) == entry["bytes"], "source byte-count mismatch: " + name)
        need(sha256(data) == entry["sha256"], "source hash mismatch: " + name)
    return {"input_manifest_sha256": sha256(pin_bytes),
            "source_manifest_sha256": sha256(source_path.read_bytes()),
            "bound_bundle_files": len(pinned),
            "bound_public_source_files": len(source["files"])}


def native_generator(state: tuple[int, ...], index: int) -> tuple[int, ...]:
    p1, p4, p1p, p4p, q, r = state
    if index == 0:
        output = (p4, p1, p4p, p1p, q, r)
    elif index == 1:
        output = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif index == 2:
        output = (-p1p + 2, -p4p + 1 + r,
                  -p1 + 2, -p4 + 1 - r, 1 - q, -r)
    elif index == 3:
        output = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    elif index == 4:
        output = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    else:
        raise AssertionError("invalid native generator index")
    return tuple(v % 5 for v in output)


def native_step(n: int, state: tuple[int, ...]) -> tuple:
    theta = n.bit_count() % 2
    index = (sum(state) + 2 * theta) % 5
    return n + 1, native_generator(state, index), index


def projection(state: tuple[int, ...]) -> tuple[int, int, int]:
    return sum(state[:4]) % 5, state[4], state[5]


def projected_generator(state: tuple[int, int, int], index: int) -> tuple:
    k, q, r = state
    outputs = ((k, q, r), (-k, -q, -r), (1-k, 1-q, -r),
               (-k, 1-q, 1-r), (-k, 2-q, 1-r))
    return tuple(v % 5 for v in outputs[index])


def expected_fibres(z: int, u: tuple[int, int]) -> tuple:
    q, r = u
    one = ((q, r), (-q, -r), (1-q, -r),
           (1-q, 1-r), (2-q, 1-r))[z]
    two = ((1-q, -r), (q, r), (q, r),
           (q-1, r-1), (q-2, r-1))[z]
    three = ((q+1, r+1), (1-q, 1-r), (2-q, 1-r),
             (2-q, 2-r), (3-q, 2-r))[z]
    return tuple(tuple(c % 5 for c in point) for point in (one, two, three))


def encode(state: tuple[int, ...]) -> int:
    value = 0
    for coordinate in state:
        value = 5 * value + coordinate
    return value


def csv_buffer(header: list[str]) -> tuple[io.StringIO, object]:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(header)
    return stream, writer


def full_native_audit() -> tuple:
    names = ("p1", "p4", "p1p", "p4p", "q", "r")
    header = ["seed_id"]
    for n in range(4):
        header += ["n" + str(n)] + [name + "_" + str(n) for name in names]
        if n < 3:
            header += ["selected_" + str(n)]
    stream, writer = csv_buffer(header)
    trajectories = []
    reduced_records = {}
    generator_checks = 0
    expected_indices = ((0, 2, 4), (1, 1, 3), (2, 2, 4),
                        (3, 1, 3), (4, 1, 3))
    expected_traces = ((0, 2, 1), (4, 1, 1), (0, 2, 1),
                       (4, 1, 1), (4, 1, 1))
    for seed_id, seed in enumerate(itertools.product(FIVE, repeat=6)):
        need(encode(seed) == seed_id, "seed enumeration/encoding mismatch")
        projected = projection(seed)
        for index in FIVE:
            need(projection(native_generator(seed, index)) ==
                 projected_generator(projected, index),
                 "native generator projection mismatch")
            generator_checks += 1
        n, current = 0, seed
        states = [seed]
        indices = []
        row = [seed_id, n, *current]
        for _ in range(3):
            old_projected = projection(current)
            new_n, output, index = native_step(n, current)
            need(new_n == n + 1, "counter increment mismatch")
            need(all(0 <= c < 5 for c in output), "noncanonical state")
            need(projection(output) == projected_generator(old_projected, index),
                 "selected projection mismatch")
            row += [index, new_n, *output]
            states.append(output)
            indices.append(index)
            n, current = new_n, output
        writer.writerow(row)
        z = sum(seed) % 5
        need(tuple(indices) == expected_indices[z], "actual selector table mismatch")
        need(tuple(sum(state) % 5 for state in states[1:]) == expected_traces[z],
             "actual trace table mismatch")
        fibre_history = tuple(state[4:] for state in states[1:])
        need(fibre_history == expected_fibres(z, seed[4:]),
             "actual early fibre table mismatch")
        need(fibre_history[2] == tuple((v + 1) % 5 for v in fibre_history[0]),
             "third/first fibre translation mismatch")
        key = (z, *seed[4:])
        record = (tuple(indices), fibre_history)
        if key in reduced_records:
            need(reduced_records[key] == record, "transverse source dependence")
        else:
            reduced_records[key] = record
        trajectories.append(tuple(states))
    need(len(trajectories) == 15625, "incomplete full-state carrier")
    need(generator_checks == 78125, "incomplete generator projection audit")
    need(len(reduced_records) == 125, "incomplete projected table")
    fibre_stream, fibre_writer = csv_buffer([
        "initial_z", "initial_q", "initial_r", "selected_0", "selected_1",
        "selected_2", "q1", "r1", "q2", "r2", "q3", "r3"])
    for key in sorted(reduced_records):
        indices, history = reduced_records[key]
        fibre_writer.writerow([*key, *indices, *(v for point in history for v in point)])
    payloads = {
        "NATIVE-STEPS.csv": stream.getvalue().encode("utf-8"),
        "FIBRE-TABLE.csv": fibre_stream.getvalue().encode("utf-8"),
    }
    return trajectories, payloads, generator_checks


def representative_preparation(k0: int, s: int, f0: tuple,
                               w: tuple, x: int, y: int) -> tuple:
    if s:
        pistons = ((k0 + s * x) % 5, 0, 0, 0)
    else:
        pistons = ((k0 + x) % 5, (-x) % 5, 0, 0)
    return (*pistons, (f0[0] + w[0] * y) % 5, (f0[1] + w[1] * y) % 5)


def representative_source_reader(state: tuple, k0: int, s: int) -> int:
    coefficient = INVERSE[s] if s else 1
    return (coefficient * (state[0] - k0)) % 5


def receiver_audit(trajectories: list) -> tuple:
    names = ("p1", "p4", "p1p", "p4p", "q", "r")
    header = ["k0", "s", "q0", "r0", "wq", "wr", "Bq", "Br", "b",
              "x", "y", "target_y", "actual_y", "representative_actual_x",
              "initial_n", "final_n", "seed_id"]
    header += ["initial_" + name for name in names]
    header += ["final_" + name for name in names]
    streams_and_writers = [csv_buffer(header) for _ in range(3)]
    survivor_stream, survivor_writer = csv_buffer(
        ["t", "k0", "s", "q0", "r0", "wq", "wr", "Bq", "Br", "b"])
    survivors_by_time = [0, 0, 0]
    survivors_by_s_and_time = [[0] * 5 for _ in range(3)]
    rejections_by_time = [0, 0, 0]
    first_witness_digest = hashlib.sha256()
    configurations = 0
    input_checks = 0
    for k0 in FIVE:
        for s in FIVE:
            for f0 in POINTS:
                for w in NONZERO_POINTS:
                    readers = tuple(B for B in POINTS
                                    if (B[0] * w[0] + B[1] * w[1]) % 5 == 1)
                    need(len(readers) == 5, "incomplete receiver-reader class")
                    for B in readers:
                        configurations += 1
                        b = (-B[0] * f0[0] - B[1] * f0[1]) % 5
                        first_failures = [None, None, None]
                        parameters = (k0, s, *f0, *w, *B, b)
                        for x in FIVE:
                            for y in FIVE:
                                seed = representative_preparation(k0, s, f0, w, x, y)
                                need(projection(seed)[0] == (k0 + s * x) % 5,
                                     "source-sum representative mismatch")
                                need(representative_source_reader(seed, k0, s) == x,
                                     "initial source reader mismatch")
                                need((B[0] * seed[4] + B[1] * seed[5] + b) % 5 == y,
                                     "initial receiver reader mismatch")
                                seed_id = encode(seed)
                                history = trajectories[seed_id]
                                need(history[0] == seed, "native-table lookup mismatch")
                                target_y = (x + y) % 5
                                for t in (1, 2, 3):
                                    final = history[t]
                                    actual_y = (B[0] * final[4] + B[1] * final[5] + b) % 5
                                    input_checks += 1
                                    if actual_y != target_y and first_failures[t-1] is None:
                                        actual_x = representative_source_reader(final, k0, s)
                                        first_failures[t-1] = (
                                            *parameters, x, y, target_y, actual_y, actual_x,
                                            0, t, seed_id, *seed, *final)
                        for t in (1, 2, 3):
                            row = first_failures[t-1]
                            if row is None:
                                survivors_by_time[t-1] += 1
                                survivors_by_s_and_time[t-1][s] += 1
                                survivor_writer.writerow([t, *parameters])
                            else:
                                rejections_by_time[t-1] += 1
                                streams_and_writers[t-1][1].writerow(row)
                                first_witness_digest.update(canonical_json(list(row)))
    need(configurations == 75000, "incomplete receiver configuration enumeration")
    need(input_checks == 5625000, "incomplete all-25/time checks")
    for t in range(3):
        need(rejections_by_time[t] + survivors_by_time[t] == 75000,
             "incomplete receiver decision partition")
    payloads = {
        "FALSIFIERS-T" + str(t+1) + ".csv": streams_and_writers[t][0].getvalue().encode("utf-8")
        for t in range(3)
    }
    payloads["RECEIVER-SURVIVORS.csv"] = survivor_stream.getvalue().encode("utf-8")
    summary = {
        "receiver_configurations": configurations,
        "receiver_time_configurations": 3 * configurations,
        "input_time_checks": input_checks,
        "receiver_survivors_by_time": survivors_by_time,
        "receiver_survivors_by_s_and_time": survivors_by_s_and_time,
        "receiver_rejections_by_time": rejections_by_time,
        "first_witness_stream_sha256": first_witness_digest.hexdigest(),
    }
    return summary, payloads


def run(bundle: Path, repository: Path, output_dir: Path | None) -> tuple[dict, int]:
    integrity = check_integrity(bundle, repository)
    if output_dir is not None:
        need(not output_dir.exists(), "output directory must be new")
    trajectories, payloads, generator_checks = full_native_audit()
    counts, receiver_payloads = receiver_audit(trajectories)
    payloads.update(receiver_payloads)
    manifest = {}
    for name, data in sorted(payloads.items()):
        need(len(data) <= MAX_EVIDENCE_BYTES, "evidence file exceeds 5 MiB: " + name)
        manifest[name] = {"bytes": len(data), "sha256": sha256(data)}
    no_survivors = not any(counts["receiver_survivors_by_time"])
    summary = {
        "schema": "native-early-contact-primary-v1",
        "decision": ("NO_SUM_IN_FROZEN_CLASS" if no_survivors else
                     "RECEIVER_LEMMA_FALSIFIED_FULL_SUM_UNRESOLVED"),
        "full_parameter_tuples_including_time": 438750000000,
        "full_native_seeds": len(trajectories),
        "full_native_steps": 3 * len(trajectories),
        "generator_projection_checks": generator_checks,
        "projected_fibre_table_rows": 125,
        **counts,
        "integrity": integrity,
        "evidence": manifest,
    }
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=False)
        for name, data in sorted(payloads.items()):
            (output_dir / name).write_bytes(data)
        (output_dir / "SUMMARY.json").write_bytes(canonical_json(summary, pretty=True))
    return summary, 0 if no_survivors else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    bundle = Path(__file__).resolve().parent
    repository = args.repo_root.resolve() if args.repo_root else bundle.parents[1]
    environment_output = os.environ.get("TWISTJ_EVIDENCE_DIR")
    if args.output_dir and environment_output:
        need(args.output_dir.resolve() == Path(environment_output).resolve(),
             "CLI and environment evidence directories disagree")
    requested_output = args.output_dir or (Path(environment_output) if environment_output else None)
    output = requested_output.resolve() if requested_output else None
    summary, status = run(bundle, repository, output)
    sys.stdout.buffer.write(canonical_json(summary))
    return status


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        sys.stderr.write("FAIL " + type(error).__name__ + ": " + str(error) + "\n")
        raise SystemExit(1)
