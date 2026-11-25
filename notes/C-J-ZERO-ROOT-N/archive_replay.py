#!/usr/bin/env python3
"""NON-CANONICAL replay of the exposed archive in ARCHIVE-PREREG.md.

New wrapper, not a recovered original verifier. The external source bytes
are identified by ARCHIVE-MANIFEST.tsv and are never modified or published
by this program. Output belongs outside the repository.
"""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tarfile

ARCHIVE_SHA256 = "137a48e98c1643fdc0fa6134279778333e2a7044dae68b529a7f5b8c8f43aa5d"
ARCHIVE_BYTES = 36076
MASKS = (3, 5, 6, 9, 10, 12)
CROSSING = (3, 6, 9, 12)
BOOT = (
    "import pathlib,runpy,sys; "
    "p=sys.argv.pop(1); "
    "sys.path.insert(0,str(pathlib.Path(p).resolve().parent)); "
    "sys.argv[0]=p; runpy.run_path(p,run_name='__main__')"
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def witnesses(source):
    """Two exposed finite witnesses; no new independent motor implementation."""
    motor = load_module("received_motor", source / "A/motor_A.py")
    observations = []
    for u, v, tick in ((3, 0, 3), (2, 4, 28)):
        state = motor.prep_E(u, v)
        for n in range(tick):
            _, state = motor.step(n, state)
        receiver = tuple(state[i] for i in (1, 3, 4, 5))
        reading = motor.reader(state)
        require(receiver == (4, 0, 4, 2), "exposed receiver collision failed")
        require(reading == ("PRESENT",) + motor.target(u, v), "E reading failed")
        observations.append(reading[1:])
    require(observations == [(4, 0), (0, 1)], "collision readings failed")
    print("receiver collision: (4,0,4,2); E(3,0) at 3 -> (4,0); E(2,4) at 28 -> (0,1)")

    ring = load_module("received_ring", source / "B/oring.py")
    w = ring.mul(ring.sqrt5, ring.sub(ring.J, ring.conj(ring.J)))
    reference = ring.smul(-5, ring.phi)
    x = ring.add(w, ring.smul(4, ring.ONE))
    _, pointer = ring.contact(x, reference)
    two = ring.smul(2, ring.ONE)
    require(ring.divisible(ring.sub(pointer, two), 2), "overwrite not admitted")
    _, mark = ring.contact(pointer, two)
    difference = ring.sub(mark, ring.J)
    one_minus_rho = ring.sub(ring.ONE, ring.rho)
    require(difference == ring.mul(one_minus_rho, one_minus_rho), "mark identity failed")
    require(difference == (0, -1, -3, -1), "mark difference failed")
    require(not ring.divisible(difference, 5), "mark unexpectedly equals J mod 5")
    print("x=w+4: overwrite admitted; mark-J=(0,-1,-3,-1), nonzero modulo 5")
    print("PASS")


def table_guard(data):
    lines = data.decode("ascii").splitlines()
    ids = []
    for line in lines:
        match = re.match(r"split\s+(\d+)\s+S=", line)
        require(match is not None, "invalid split table line")
        ids.append(int(match.group(1)))
    require(ids == list(range(1, 63)), "split table must contain all 62 rows once in order")


def early_guard(data, mask):
    rows = {}
    summaries = []
    for line in data.decode("ascii").splitlines():
        match = re.fullmatch(r"mask (\d+) r0 (\d+) t (\d+) tick (\d+) hist (\d+)", line)
        if match is None:
            summaries.append(line)
            continue
        seen_mask, ready, tick, current, history = map(int, match.groups())
        require(seen_mask == mask, "wrong early split")
        require((ready, tick) not in rows, "duplicate early observation")
        rows[ready, tick] = current, history
    require(set(rows) == {(r, t) for r in range(625) for t in range(4)}, "early coverage incomplete")
    require(len(summaries) == 1 and re.match(r"split\s+" + str(mask) + r"\s+S=", summaries[0]), "early summary invalid")
    bound = 17 if mask in CROSSING else 9
    for ready in range(625):
        require(rows[ready, 0] == (1, 1), "receiver not initially common")
        require(rows[ready, 1][1] == rows[ready, 1][0], "history did not start at cut one")
        if mask in CROSSING:
            require(rows[ready, 2][1] == 25, "two-cut crossing decoder failed")
        else:
            require(all(rows[ready, t][1] <= 9 for t in range(4)), "same-index history bound failed")
    maximum = max(current for current, _ in rows.values())
    require(maximum == bound, "single-cut maximum failed")
    return {"mask": mask, "common_preparations": 625, "maximum_single_cut_0_to_3": maximum,
            "all_crossing_histories_at_cuts_1_and_2": 25 if mask in CROSSING else None}


def main(archive, destination):
    require(platform.python_implementation() == "CPython" and platform.python_version() == "3.12.14", "unfrozen Python")
    require(platform.system() == "Linux" and platform.machine() == "x86_64", "unfrozen platform")
    raw = archive.read_bytes()
    require(len(raw) == ARCHIVE_BYTES and digest(raw) == ARCHIVE_SHA256, "archive custody mismatch")
    manifest_path = Path(__file__).with_name("ARCHIVE-MANIFEST.tsv")
    lines = manifest_path.read_text(encoding="ascii").splitlines()
    require(lines.pop(0) == "path\tbytes\tsha256", "manifest header")
    manifest = {}
    for line in lines:
        name, size, sha = line.split("\t")
        require(name not in manifest, "duplicate manifest member")
        manifest[name] = (int(size), sha)
    require(len(manifest) == 29, "manifest size")
    received = {}
    directories = set()
    with tarfile.open(archive, "r:gz") as tar:
        members = tar.getmembers()
        require(len(members) == 33, "tar member count")
        seen = set()
        for member in members:
            name = member.name.rstrip("/")
            require(name not in seen, "duplicate tar member")
            seen.add(name)
            if member.isdir():
                directories.add(name)
                continue
            require(member.isfile() and name in manifest, "unapproved tar member")
            data = tar.extractfile(member).read()
            require((len(data), digest(data)) == manifest[name], "member custody mismatch: " + name)
            received[name] = data
    require(directories == {"A", "B", "C", "X"} and set(received) == set(manifest), "tar inventory mismatch")
    table_guard(received["C/splits_n0_T32.txt"])
    rows = [tuple(map(int, line.split())) for line in received["A/exact_t3_list.txt"].decode("ascii").splitlines()]
    require(len(rows) == len(set(rows)) == 125 and all(len(row) == 3 and all(0 <= x < 625 for x in row) for row in rows), "125-preparation list incomplete")

    destination.mkdir(parents=True, exist_ok=False)
    source = destination / "source"
    # Extract only reviewed execution dependencies, retaining all original bytes.
    selected = ("A/motor_A.py", "A/check_A.py", "A/analyze_exact_A.py", "A/exact_t3_list.txt",
                "B/oring.py", "B/verify_B.py", "C/enum_splits.c", "C/break_splits.py")
    for name in selected:
        path = source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(received[name])
    env = {"PATH": "/usr/bin:/bin", "LC_ALL": "C", "PYTHONHASHSEED": "0", "PYTHONIOENCODING": "utf-8"}
    report = {"archive_sha256": ARCHIVE_SHA256, "wrapper_sha256": digest(Path(__file__).read_bytes()),
              "manifest_sha256": digest(manifest_path.read_bytes()), "python": platform.python_version(),
              "system": platform.system(), "architecture": platform.machine(), "runs": [], "complete": False}

    def save():
        (destination / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    def run(label, argv, cwd, timeout, expected=None):
        record = {"label": label, "argv": argv, "timeout_seconds": timeout}
        report["runs"].append(record)
        try:
            completed = subprocess.run(argv, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
            stdout, stderr = completed.stdout, completed.stderr
            record["exit_code"] = completed.returncode
        except subprocess.TimeoutExpired as error:
            stdout, stderr = error.stdout or b"", error.stderr or b""
            record["exit_code"] = None
            record["timeout"] = True
        (destination / (label + ".stdout")).write_bytes(stdout)
        (destination / (label + ".stderr")).write_bytes(stderr)
        record.update(stdout_bytes=len(stdout), stdout_sha256=digest(stdout), stderr_bytes=len(stderr), stderr_sha256=digest(stderr))
        if expected is not None:
            record["byte_identical_to_received"] = stdout == expected
        save()
        require(record["exit_code"] == 0 and not stderr, "execution failure: " + label)
        require(expected is None or stdout == expected, "output mismatch: " + label)
        print(json.dumps({"stage": label, "exit_code": 0, "stdout_bytes": len(stdout), "sha256": digest(stdout)}), flush=True)
        return stdout

    def py(relative, *args):
        return [sys.executable, "-I", "-B", "-c", BOOT, str(source / relative), *args]

    try:
        run("compiler-version", ["/usr/bin/gcc", "-dumpfullversion"], destination, 30, b"14.2.0\n")
        binary = destination / "enum_splits"
        run("compile", ["/usr/bin/gcc", "-O2", "-std=c99", "-Wall", "-Wextra", str(source / "C/enum_splits.c"), "-o", str(binary)], destination, 30, b"")
        run("B", py("B/verify_B.py"), source / "B", 120, received["B/verify_B.stdout"])
        table = run("C32", [str(binary), "0", "32"], destination, 120, received["C/splits_n0_T32.txt"])
        table_guard(table)
        run("C-matrix", py("C/break_splits.py", str(destination / "C32.stdout")), source / "C", 600, received["C/break_splits.stdout"])
        report["early_cuts"] = []
        for mask in MASKS:
            data = run("early-" + str(mask), [str(binary), "0", "3", str(mask), "1"], destination, 60)
            report["early_cuts"].append(early_guard(data, mask))
            save()
        run("A-million", py("A/check_A.py", "1000000"), source / "A", 600, received["A/check_A.stdout"])
        listing = run("A125", py("A/analyze_exact_A.py"), source / "A", 120)
        require(listing.startswith(b"count 125\n") and listing.endswith(b"all 125: direct simulation confirms target at t=3 and reader BLANK 0..2, PRESENT(target) 3..200\n"), "125-preparation check failed")
        expected_witnesses = (
            b"receiver collision: (4,0,4,2); E(3,0) at 3 -> (4,0); E(2,4) at 28 -> (0,1)\n"
            b"x=w+4: overwrite admitted; mark-J=(0,-1,-3,-1), nonzero modulo 5\nPASS\n"
        )
        run("witnesses", [sys.executable, "-I", "-B", str(Path(__file__).resolve()), "--witnesses", str(source)], destination, 30, expected_witnesses)
        require(all((source / name).read_bytes() == received[name] for name in selected), "source changed during execution")
        report["complete"] = True
        save()
        print("PASS: archive replay completed; single architecture; exposed inputs; no promotion", flush=True)
    except BaseException as error:
        report["failure"] = type(error).__name__ + ": " + str(error)
        save()
        raise


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--witnesses":
        witnesses(Path(sys.argv[2]).resolve())
    else:
        require(len(sys.argv) == 3, "usage: archive_replay.py ARCHIVE NEW_OUTPUT_DIRECTORY")
        main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
