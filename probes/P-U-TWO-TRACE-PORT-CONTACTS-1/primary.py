#!/usr/bin/env python3
"""Frozen exact audit of the declared two-use trace-port construction.

No external data, prior scientific program, fitted loading map or endpoint reader
is imported. Execute only after the coordinator's complete public pre-run pin.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import io
from itertools import product
import json
import os
from pathlib import Path
import sys


PROBE = "P-U-TWO-TRACE-PORT-CONTACTS-1"
RHO = (0, 0, 0, 0, 1, 0)
SECOND_READY = (2, 1, 3, 4, 0, 4)
CELL_NAMES = ("p1", "p4", "p1p", "p4p", "q", "r")


class AuditFailure(RuntimeError):
    """A falsifier of a frozen assertion; never silently repaired."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditFailure(message)


def trace(cell: tuple[int, ...]) -> int:
    return sum(cell) % 5


def pointer(cell: tuple[int, ...]) -> int:
    return (cell[0] + cell[2]) % 5


def second_pointer(cell: tuple[int, ...]) -> int:
    return (cell[1] + cell[3]) % 5


def read(cell: tuple[int, ...]) -> int:
    return pointer(cell) ** 2 % 5


def target(a: int) -> int:
    """Verification target only; never called by preparation or dynamics."""
    return (a + 1) // 5


def exchange(source: int, cell: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    """Generic C: exchange the source with z in the bijective (P,z,r) chart."""
    pistons = cell[:4]
    radius = cell[5]
    new_q = (source - sum(pistons) - radius) % 5
    return trace(cell), (*pistons, new_q, radius)


def generator(index: int, cell: tuple[int, ...]) -> tuple[int, ...]:
    """Literal Canon v97 coordinate definitions, in a,b,c,d,e order."""
    p1, p4, p1p, p4p, q, r = cell
    if index == 0:
        result = (p4, p1, p4p, p1p, q, r)
    elif index == 1:
        result = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif index == 2:
        result = (-p1p + 2, -p4p + 1 + r,
                  -p1 + 2, -p4 + 1 - r, 1 - q, -r)
    elif index == 3:
        result = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    elif index == 4:
        result = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    else:
        raise AuditFailure("Native generator index outside 0,...,4")
    return tuple(value % 5 for value in result)


def native_step(n: int, cell: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    selected = (trace(cell) + 2 * (n.bit_count() % 2)) % 5
    return selected, generator(selected, cell)


@dataclass(frozen=True)
class State:
    n: int
    s1: int
    s2: int
    r1: tuple[int, ...]
    r2: tuple[int, ...]

    def row(self) -> list[int]:
        return [self.n, self.s1, self.s2, *self.r1, *self.r2]


def canonical(state: State) -> None:
    require(type(state.n) is int and state.n >= 0, "Invalid counter")
    require(len(state.r1) == len(state.r2) == 6, "Incomplete receiver")
    require(all(type(value) is int and 0 <= value < 5
                for value in state.row()[1:]), "Noncanonical complete state")


def prepare(a1: int, a2: int) -> State:
    return State(0, (a1 + 1) % 5, (a2 + 1) % 5, RHO, RHO)


def step(state: State, *, no_exchange: bool = False):
    """One enlarged update; the flag is solely the frozen negative control.

    Returns next boundary, algebraic post-C state, addressed cell (or None),
    and the two native selected indices. No source label enters this function.
    """
    addressed = None
    intermediate = state
    if not no_exchange and state.n == 0:
        source, cell = exchange(state.s1, state.r1)
        intermediate = State(state.n, source, state.s2, cell, state.r2)
        addressed = 1
    elif not no_exchange and state.n == 6:
        source, cell = exchange(state.s2, state.r2)
        intermediate = State(state.n, state.s1, source, state.r1, cell)
        addressed = 2
    i1, r1 = native_step(state.n, intermediate.r1)
    i2, r2 = native_step(state.n, intermediate.r2)
    following = State(state.n + 1, intermediate.s1, intermediate.s2, r1, r2)
    return following, intermediate, addressed, (i1, i2)


def json_bytes(value) -> bytes:
    return (json.dumps(value, separators=(",", ":")) + "\n").encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def csv_bytes(header, rows) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def check_primitive() -> int:
    count = 0
    for values in product(range(5), repeat=7):
        source, *coordinates = values
        cell = tuple(coordinates)
        exported, changed = exchange(source, cell)
        require(exchange(exported, changed) == (source, cell), "C is not involutive")
        require(exported == trace(cell) and trace(changed) == source,
                "C does not exchange the actual trace and source")
        require(changed[:4] == cell[:4] and changed[5] == cell[5],
                "C changed a protected coordinate")
        require(pointer(changed) == pointer(cell)
                and second_pointer(changed) == second_pointer(cell),
                "C changed A or B")
        require(all(type(v) is int and 0 <= v < 5 for v in (exported, *changed)),
                "C output is not canonical")
        count += 1
    require(count == 78125, "Primitive coverage incomplete")
    return count


def run():
    """Return (deterministic report, filename->bytes evidence), without file I/O."""
    primitive_inputs = check_primitive()
    require(tuple(n.bit_count() % 2 for n in (0, 1, 2)) == (0, 1, 1),
            "First native prefix mismatch")
    require(tuple(n.bit_count() % 2 for n in (6, 7, 8)) == (0, 1, 1),
            "Second native prefix mismatch")
    histories = {}
    history_rows, contact_rows, full_contacts, native_rows, control_rows = [], [], [], [], []
    endpoints, selector_rows = [], []
    record_counts = {"0,0": 0, "0,1": 0, "1,0": 0, "1,1": 0}
    control_target_failures = 0

    for a1 in range(5):
        for a2 in range(5):
            state = prepare(a1, a2)
            path = []
            contacts = 0
            for n in range(10):
                canonical(state)
                require(state.n == n, "Counter skipped or reset")
                path.append(state)
                history_rows.append([a1, a2, *state.row()])
                require(state.s1 == ((a1 + 1) % 5 if n == 0 else 1),
                        "First source export/retention failed")
                require(state.s2 == ((a2 + 1) % 5 if n <= 6 else 4),
                        "Second source changed early or export failed")
                if n >= 3:
                    require(trace(state.r1) in (1, 4) and read(state.r1) == target(a1),
                            "First record or protected continuation failed")
                if n == 6:
                    require(state.r2 == SECOND_READY, "Second full ready state failed")
                if n == 9:
                    require(trace(state.r2) in (1, 4) and read(state.r2) == target(a2),
                            "Second record failed")
                    break

                following, intermediate, addressed, indices = step(state)
                selector_rows.append([a1, a2, n, *indices])
                canonical(intermediate)
                require(intermediate.n == state.n, "Exchange altered the native counter")
                require(following.n == state.n + 1, "Enlarged step counter mismatch")
                if addressed is not None:
                    contacts += 1
                    require((n, addressed) in ((0, 1), (6, 2)), "Wrong contact address")
                    if addressed == 1:
                        before_s, after_s = state.s1, intermediate.s1
                        before_r, after_r = state.r1, intermediate.r1
                        require((state.s2, state.r2) == (intermediate.s2, intermediate.r2),
                                "First contact touched another factor")
                        require(after_r == (0, 0, 0, 0, (a1 + 1) % 5, 0),
                                "First loaded full state mismatch")
                    else:
                        before_s, after_s = state.s2, intermediate.s2
                        before_r, after_r = state.r2, intermediate.r2
                        require((state.s1, state.r1) == (intermediate.s1, intermediate.r1),
                                "Second contact touched the first record or source")
                        require(after_r == (2, 1, 3, 4, (a2 + 2) % 5, 4),
                                "Second loaded full state mismatch")
                    require(trace(after_r) == before_s
                            and pointer(after_r) == second_pointer(after_r) == 0,
                            "Loaded trace/readiness mismatch")
                    contact_rows.append([a1, a2, n, before_s, after_s, *before_r, *after_r])
                    full_contacts.append({"a1": a1, "a2": a2, "n": n,
                                          "receiver": addressed,
                                          "before": state.row(),
                                          "after": intermediate.row()})
                else:
                    require(intermediate == state, "Unscheduled exchange")
                for receiver, before, after, selected in (
                    (1, intermediate.r1, following.r1, indices[0]),
                    (2, intermediate.r2, following.r2, indices[1]),
                ):
                    require(selected == (sum(before) + 2 * (n.bit_count() % 2)) % 5,
                            "Native selector did not use actual post-C state")
                    require(after == generator(selected, before), "Wrong native transition")
                    native_rows.append([a1, a2, n, receiver, selected, *before, *after])
                state = following

            require(contacts == 2 and len(path) == 10, "Incomplete two-use history")
            histories[a1, a2] = path
            records = (read(state.r1), read(state.r2))
            require(records == (target(a1), target(a2)), "Wrong ordered endpoint records")
            record_counts[f"{records[0]},{records[1]}"] += 1
            endpoints.append({"a1": a1, "a2": a2, "state": state.row(),
                              "records": list(records)})

            control = prepare(a1, a2)
            for n in range(10):
                canonical(control)
                require(control.n == n, "Control counter mismatch")
                require((control.s1, control.s2) == ((a1 + 1) % 5, (a2 + 1) % 5),
                        "Control consumed a source")
                require(trace(control.r1) in (1, 4) and trace(control.r2) in (1, 4)
                        and read(control.r1) == read(control.r2) == 0,
                        "Native-only control unexpectedly wrote a record")
                control_rows.append([a1, a2, *control.row()])
                if n < 9:
                    control, unchanged, address, unused = step(control, no_exchange=True)
                    require(address is None, "Control executed an exchange")
            if (0, 0) != (target(a1), target(a2)):
                control_target_failures += 1
    require(control_target_failures > 0, "Negative control did not expose coupling need")

    for a1 in range(5):
        for a2 in range(5):
            for n in range(10):
                state = histories[a1, a2][n]
                require(state.r1 == histories[a1, 0][n].r1,
                        "First complete receiver depends on second source")
                require(state.r2 == histories[0, a2][n].r2,
                        "Second complete receiver depends on first source")
                if n <= 6:
                    require(state.r2 == histories[0, 0][n].r2,
                            "Unused second receiver depends on an input")

    require(histories[0, 0][0] != histories[1, 0][0], "Collision inputs are not distinct")
    for n in range(3, 10):
        require(histories[0, 0][n] == histories[1, 0][n], "Full-state collision missing")
    collision = {"input_pairs": [[0, 0], [1, 0]],
                 "initial_states": [histories[0, 0][0].row(), histories[1, 0][0].row()],
                 "common_n3": histories[0, 0][3].row(),
                 "common_n9": histories[0, 0][9].row(),
                 "scope": "Complete state equality; future equality follows by determinism."}

    require(len(history_rows) == 250 and all(len(row) == 17 for row in history_rows),
            "History coverage/shape mismatch")
    require(len(contact_rows) == 50 and all(len(row) == 17 for row in contact_rows),
            "Contact coverage/shape mismatch")
    require(len(native_rows) == 450 and len(selector_rows) == 225 and len(control_rows) == 250,
            "Native/control coverage mismatch")
    history_header = ["a1", "a2", "n", "s1", "s2"] + [
        f"r{receiver}_{name}" for receiver in (1, 2) for name in CELL_NAMES]
    contact_header = ["a1", "a2", "n", "source_before", "source_after"] + [
        f"{stage}_{name}" for stage in ("before", "after") for name in CELL_NAMES]
    native_header = ["a1", "a2", "n", "receiver", "selected_index"] + [
        f"{stage}_{name}" for stage in ("before", "after") for name in CELL_NAMES]
    artifacts = {
        "HISTORY.json": json_bytes(history_rows),
        "CONTACTS.json": json_bytes(contact_rows),
        "SELECTORS.json": json_bytes(selector_rows),
        "CONTROL-HISTORIES.json": json_bytes(control_rows),
        "HISTORY.csv": csv_bytes(history_header, history_rows),
        "CONTACTS.csv": csv_bytes(contact_header, contact_rows),
        "FULL-CONTACTS.json": json_bytes(full_contacts),
        "NATIVE-STEPS.csv": csv_bytes(native_header, native_rows),
        "NO-EXCHANGE-CONTROL.csv": csv_bytes(history_header, control_rows),
        "ENDPOINTS.json": json_bytes(endpoints),
        "FULL-STATE-COLLISION.json": json_bytes(collision),
    }
    require(all(len(data) < 5 * 1024 * 1024 for data in artifacts.values()),
            "Evidence exceeds the frozen per-artifact size bound")
    report = {"probe": PROBE, "status": "PASS", "input_pairs": len(histories),
              "history_rows": len(history_rows), "contact_rows": len(contact_rows),
              "history_sha256": sha256(artifacts["HISTORY.json"]),
              "contact_sha256": sha256(artifacts["CONTACTS.json"]),
              "selectors_sha256": sha256(artifacts["SELECTORS.json"]),
              "control_sha256": sha256(artifacts["CONTROL-HISTORIES.json"]),
              "primitive_inputs": primitive_inputs, "native_cell_steps": len(native_rows),
              "control_history_rows": len(control_rows),
              "control_target_failures": control_target_failures,
              "record_pair_counts": record_counts, "full_state_collision": "PASS",
              "all_time_retention": "analytical PROOF.md; finite audit through n=9",
              "artifacts": {name: {"bytes": len(data), "sha256": sha256(data)}
                            for name, data in sorted(artifacts.items())}}
    return report, artifacts


def main() -> None:
    if sys.flags.optimize:
        raise AuditFailure("Optimized Python is outside the frozen contract")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        help="New evidence directory; an existing directory is rejected")
    args = parser.parse_args()
    destination = args.output_dir
    if destination is None and os.environ.get("TWISTJ_EVIDENCE_DIR"):
        destination = Path(os.environ["TWISTJ_EVIDENCE_DIR"]) / "primary"
    if destination is not None and destination.exists():
        raise AuditFailure("Evidence destination already exists; preserve earlier runs")
    report, artifacts = run()
    if destination is not None:
        destination.mkdir(parents=True, exist_ok=False)
        for name, data in sorted(artifacts.items()):
            with (destination / name).open("xb") as stream:
                stream.write(data)
    sys.stdout.buffer.write((json.dumps(report, sort_keys=True,
                                       separators=(",", ":")) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
