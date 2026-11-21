# SPDX-License-Identifier: Apache-2.0
"""First double-recurrent, two-transfer B1/B2 witness on a single native orbit."""
import argparse
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent / "P-H3-RENEWED-WORD-CHOICE-1"
THIRD = HERE.parent / "P-H3-THIRD-CELL-1"
RANKS = (43, 0, 22, *(r for r in range(85) if r not in (43, 0, 22)))
PINS = {
    "verify.py": "a8b7acd92be8b3f168882f5188b515b3020b6ea6ebeae2a640daefcb44471ca3",
    "scan.cpp": "1b7f50a32d3e8d8aec55dae63e332e99628bdc81ce55b870efadadf575defafe",
    "matches.hpp": "2c146cffe7d7c1479f864ebb2ff0c2f82f199cdecf8eed62eb0e6b748472c827",
    "witness.py": "2c0542ce8c983e2cda452e5d7d243fd3dec4a89af5f4b7660fc55fa60cee5d9d",
    "EXPECTED.txt": "cd60930de63cc0f00a8af80e5f0c107f653f6429c48c1f571bd65ea996e3f8fe",
}


def require(ok, text):
    if not ok:
        raise ValueError(text)


def dependencies():
    for name, digest in PINS.items():
        require(sha256((PREVIOUS / name).read_bytes()).hexdigest() == digest, "predecessor drift: " + name)
    spec = importlib.util.spec_from_file_location("previous_search", PREVIOUS / "verify.py")
    previous = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(previous)
    for path, digest in previous.PINS.items():
        require(sha256(path.read_bytes()).hexdigest() == digest, "inherited input drift: " + path.name)
    sys.path[1:1] = [str(PREVIOUS), str(THIRD)]
    return previous


def ceiling(rank):
    if rank == 43:
        return 16777216
    return 4194304 if rank in (0, 22) else 262144


def old_ceiling(rank):
    if rank == 43:
        return 1048576
    return 65536 if rank in (0, 22) else 8192


def parse(previous, data):
    scans, arms = [], {}
    for line in data.decode("ascii").splitlines():
        tag, *fields = line.split()
        if tag == "SCAN":
            rank, ticks, limit, repeats, reads = map(int, fields)
            require(len(scans) < len(RANKS) and rank == RANKS[len(scans)], "unexpected rank order")
            require(0 < ticks <= limit == ceiling(rank) and min(repeats, reads) >= 0, "scan bounds")
            scans.append(dict(rank=rank, ticks=ticks, limit=limit, repeats=repeats, moved_active_reads=reads))
        elif tag == "CERT":
            category, mode, arm, *words = fields
            require((category, mode) == ("RR", "BOTH_MOVED") and arm in ("1", "2")
                    and arm not in arms, "invalid certificate")
            arms[arm] = previous.event_record(words)
        else:
            raise ValueError("unexpected native output: " + tag)
    require(scans and all(row["ticks"] == row["limit"] for row in scans[:-1]), "interrupted rank")
    if not arms:
        require(len(scans) == 85 and scans[-1]["ticks"] == scans[-1]["limit"], "incomplete negative census")
        return scans, []
    require(set(arms) == {"1", "2"}, "incomplete positive certificate")
    events = [arms["1"], arms["2"]]
    last = scans[-1]
    require(all(e["rank"] == last["rank"] for e in events)
            and old_ceiling(last["rank"]) < max(e["read"] for e in events) == last["ticks"],
            "witness inconsistent with stopping rule or previous zero")
    return scans, events


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-witness", action="store_true",
                        help="read the recorded certificate and replay every certified cut from launch in Python")
    args = parser.parse_args()
    previous = dependencies()
    import confirm
    import kernel
    import launches
    for name in ("multiply", "norm", "contact", "scatter"):
        operation = getattr(kernel, name)
        setattr(kernel, name, lru_cache(maxsize=131072)(operation.__wrapped__))
    fields = launches.four_wire(launches.bare_inputs())
    if args.full_witness:
        rows = [json.loads(line) for line in (HERE / "EXPECTED.txt").read_bytes().splitlines()]
        events, = [row["value"] for row in rows if row["section"] == "witness"]
        previous.emit("full_python_replay", confirm.check(fields, events, full=True))
        return
    queries = "".join(f"2 {r} 0 {launches.encode(f)}\n" for r, f in enumerate(fields)).encode("ascii")
    with tempfile.TemporaryDirectory() as temporary:
        exe = Path(temporary) / "double-transfer"
        subprocess.run(["g++", "-std=c++20", "-O3", str(HERE / "search.cpp"), "-o", str(exe)], check=True)
        result = subprocess.run([str(exe)], input=queries, capture_output=True, check=True)
        require(not result.stderr, "unexpected native stderr")
    scans, events = parse(previous, result.stdout)
    verification = confirm.check(fields, events)
    previous.emit("input", {"launches": 85, "ordered_sha256": launches.LAUNCH_DIGEST})
    previous.emit("coverage", scans)
    previous.emit("witness", events)
    previous.emit("confirmation", verification)


if __name__ == "__main__":
    main()
