# SPDX-License-Identifier: Apache-2.0
"""Test onward transport of held site-2 output words on the original rank-43 orbit."""
import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "P-H3-DOUBLE-RENEWED-TRANSFER-1"
SOURCE_PINS = {
    "verify.py": "59d76ae81387c77f33fd127acd40a0007d61720a9919bdb866ab5304791319d0",
    "search.cpp": "bc5246b4b4ff723a682190250ebba7c91b386ef6abdf0dfc83b021f3be39e3a0",
    "confirm.py": "761ddce84b737fb28dfc8cddca6ecc377487bc0a612522830a8d4966f862c9ee",
    "EXPECTED.txt": "352cecd088f2ecd4f1da02d496bed63c81b6d5418fef1b77f5d5298fc9acfaaf",
}
COUNTERS = ("ticks", "limit", "recurrent_B2_site1", "reads_B1", "reads_B2", "relays_B1",
            "relays_B2", "pending_B1", "pending_B2")
TRAIL_FIELDS = ("read", "stop_tick", "stop_stage", "stop_site", "attempts", "refused_rails",
                "moved_rails", "first3_tick", "first3_admitted_rails", "first3_moved_rails", "third_tag")
RANK = 43
LIMIT = 1 << 26


def require(ok, message):
    if not ok:
        raise ValueError(message)


def predecessor():
    for filename, digest in SOURCE_PINS.items():
        require(sha256((SOURCE / filename).read_bytes()).hexdigest() == digest,
                "changed source: " + filename)
    spec = importlib.util.spec_from_file_location("h3_double_source", SOURCE / "verify.py")
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    return source.dependencies()


def fixed_events():
    rows = [json.loads(line) for line in (SOURCE / "EXPECTED.txt").read_bytes().splitlines()]
    events, = [row["value"] for row in rows if row["section"] == "witness"]
    return events


def arm_id(value):
    arm = int(value)
    require(arm in (1, 2, 3, 4), "unknown arm")
    return arm


def decode_trace(values):
    require(len(values) == 64, "each trace must encode four complete cells")
    numbers = list(map(int, values))
    return [[numbers[i:i + 4] for i in range(start, start + 16, 4)]
            for start in range(0, 64, 16)]


def parse(previous, data):
    scan = None
    events, trails, traces = {}, {}, {}
    for line in data.decode("ascii").splitlines():
        tag, *fields = line.split()
        if tag == "SCAN":
            require(scan is None, "duplicate scan")
            scan = dict(zip(COUNTERS, map(int, fields), strict=True))
        elif tag == "CERT":
            category, mode, arm, *values = fields
            require((category, mode) == ("RR", "BOTH_MOVED"), "unexpected upstream mode")
            arm = arm_id(arm)
            require(arm not in events, "duplicate upstream event")
            events[arm] = previous.event_record(values)
        elif tag == "RELAY":
            arm, *values = fields
            arm = arm_id(arm)
            require(arm not in trails, "duplicate relay")
            trails[arm] = {key: value if key == "stop_stage" else int(value)
                           for key, value in zip(TRAIL_FIELDS, values, strict=True)}
        elif tag == "TRACE":
            arm, label, *values = fields
            labels = traces.setdefault(arm_id(arm), {})
            require(label in ("FIRST3", "STOP") and label not in labels, "invalid trace label")
            labels[label] = decode_trace(values)
        else:
            raise ValueError("unexpected native record " + tag)
    require(scan is not None and set(events) == set(trails) == set(traces), "incomplete native record")
    for arm, labels in traces.items():
        trails[arm]["traces"] = labels
    return scan, events, trails


def validate(scan, events, trails):
    require(set(events) in ({1, 2}, {1, 2, 3, 4}) and set(events) == set(trails),
            "incomplete event inventory")
    require([events[1], events[2]] == fixed_events(), "the full fixed upstream cuts must match #2049")
    ticks = scan["ticks"]
    require(set(scan) == set(COUNTERS) and 0 < ticks <= scan["limit"] == LIMIT
            and min(scan.values()) >= 0 and scan["pending_B1"] + scan["pending_B2"] <= 1,
            "scan bounds")
    for tag in (1, 2):
        reads, relays, pending = (scan[f"{kind}_B{tag}"] for kind in ("reads", "relays", "pending"))
        require(1 <= reads and relays + pending <= reads, "invalid per-branch coverage")
        recorded = {events[i]["read"] for i in events if events[i]["reader_tag"] == tag
                    and trails[i]["moved_rails"]}
        require(len(recorded) <= relays, "missing successful relay in coverage")
    for arm, trail in trails.items():
        require(trail["read"] == events[arm]["read"] <= trail["stop_tick"] <= ticks
                and (trail["stop_stage"] != "END" or trail["stop_tick"] == LIMIT),
                "relay outside scan or prematurely censored")
    fixed_hit = all(trails[i]["moved_rails"] > 0 for i in (1, 2))
    if fixed_hit:
        require(len(events) == 2 and ticks == max(t["stop_tick"] for t in trails.values()),
                "fixed positive stopping rule")
    elif 3 in events:
        require(all(trails[i]["moved_rails"] > 0 for i in (3, 4))
                and events[3]["read"] < events[4]["read"]
                and ticks == max(t["stop_tick"] for t in trails.values()),
                "alternative positive stopping rule")
    else:
        require(ticks == LIMIT, "incomplete finite search")


def unpack(rows):
    events, trails = {}, {}
    for arm, entry in enumerate(rows["fixed"] + rows["alternative"], 1):
        events[arm], trails[arm] = entry["event"], entry["relay"]
    require(len(rows["fixed"]) == 2 and len(rows["alternative"]) in (0, 2), "invalid result pairs")
    return events, trails


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-witness", action="store_true", help="replay all certified episodes from launch in Python")
    args = parser.parse_args()
    previous = predecessor()
    import confirm
    import launches
    fields = launches.four_wire(launches.bare_inputs())
    input_record = {"rank": RANK, "ordered_launch_sha256": launches.LAUNCH_DIGEST,
                    "source_witness_file_sha256": SOURCE_PINS["EXPECTED.txt"]}
    if args.full_witness:
        records = [json.loads(line) for line in (HERE / "EXPECTED.txt").read_bytes().splitlines()]
        require([r["section"] for r in records] == ["input", "scan", "fixed", "alternative", "confirmation"],
                "unexpected recorded sections")
        rows = {r["section"]: r["value"] for r in records}
        require(rows["input"] == input_record, "unexpected recorded launch")
        events, trails = unpack(rows)
        validate(rows["scan"], events, trails)
        result = confirm.check(fields, events, trails, full=True)
        require(rows["confirmation"] == json.loads(json.dumps(dict(result, full_replayed=0))),
                "recorded local confirmation differs")
        previous.emit("full_python_replay", result)
        return

    query = f"2 {RANK} 0 {launches.encode(fields[RANK])}\n".encode("ascii")
    with tempfile.TemporaryDirectory() as temporary:
        exe = Path(temporary) / "relay"
        subprocess.run(["g++", "-std=c++20", "-O3", str(HERE / "relay.cpp"), "-o", str(exe)], check=True)
        run = subprocess.run([str(exe)], input=query, capture_output=True, check=True)
    require(not run.stderr, "unexpected native stderr")
    scan, events, trails = parse(previous, run.stdout)
    validate(scan, events, trails)
    result = confirm.check(fields, events, trails)
    entries = [{"event": events[i], "relay": trails[i]} for i in sorted(events)]
    previous.emit("input", input_record)
    previous.emit("scan", scan)
    previous.emit("fixed", entries[:2])
    previous.emit("alternative", entries[2:])
    previous.emit("confirmation", result)


if __name__ == "__main__":
    main()
