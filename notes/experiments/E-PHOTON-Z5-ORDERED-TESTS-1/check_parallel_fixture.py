"""Small engineering fixture for the complete serial/four-chain path."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import threading
import time
from unittest.mock import patch

import ordered_sentinels
from prepare_capacity import ROOT, prepare
import replay_ordered_volume as replay
import run_ordered_volume as driver


SIDE = 16


def engineering_settings(side, i):
    return f"L{side}-c{i}", 0x123456789ABCDEF0 + i, "cold" if i < 3 else "hot"


def assess_fixture(chains, diagnostics, *, measurement=False):
    lengths = list(map(len, chains))
    if len(set(lengths)) != 1:
        raise ValueError("Unequal engineering histories")
    return {"status": "PASS" if measurement or lengths[0] == 2 else "STOP_MIXING"}


def duration(action):
    started = time.monotonic()
    result = action()
    return result, time.monotonic() - started


def fixture_run(executable, root, workers, digest):
    root.mkdir()
    generated = root / "generation"
    generated.mkdir()
    driver.json_file(generated / "environment.json", {"L": SIDE, "sampler_sha256": digest})
    with patch.object(driver, "chain_settings", engineering_settings), \
         patch.object(replay, "chain_settings", engineering_settings), \
         patch.object(driver, "ENDPOINTS", (1, 2)), patch.object(driver, "SAMPLES", 2), \
         patch.object(replay, "ENDPOINTS", (1, 2)), patch.object(replay, "SAMPLES", 2), \
         patch.object(ordered_sentinels, "assess", assess_fixture):
        receipt, measurement_seconds = duration(lambda: driver.run_volume(
            executable, None, generated, SIDE, time.monotonic() + 55, chain_workers=workers,
        ))
        assert receipt == {"status": "PASS", "endpoint": 2, "measurement_sentinels": "PASS"}
        driver.json_file(generated / "receipts.json", {
            str(SIDE): {**receipt, "sampler_sha256": digest},
        })
        replayed = root / "replay"
        _, replay_seconds = duration(lambda: replay.replay(
            generated, SIDE, executable, replayed, 55, chain_workers=workers,
        ))
    return measurement_seconds, replay_seconds


def cancellation_fixture(directory):
    ready = threading.Barrier(4, timeout=8)
    deadline = time.monotonic() + 12
    children = {}
    def worker(i, cohort):
        args = [sys.executable, "-c", "import time; time.sleep(30)"]
        with driver.launch(args, directory / f"worker-{i}", deadline, cohort=cohort) as child:
            children[i] = child
            ready.wait()
            if i == 1:
                raise ValueError("synthetic worker failure")
            assert not child.stdout.read(1)
    begin = time.monotonic()
    try:
        driver.run_chains(worker, 4)
    except ValueError as error:
        assert str(error) == "synthetic worker failure"
    else:
        raise AssertionError("Missing worker failure")
    assert len(children) == 4 and all(child.poll() is not None for child in children.values())
    assert time.monotonic() - begin < 10


def main():
    prepare()
    compiler = os.environ.get("CXX") or shutil.which("g++")
    if compiler is None:
        raise RuntimeError("g++ and Boost are required")
    with TemporaryDirectory(prefix="ordered-parallel-fixture-") as scratch:
        root = Path(scratch)
        executable = root / ("adapter.exe" if os.name == "nt" else "adapter")
        subprocess.run([compiler, "-std=c++20", "-O2", "-Wall", "-Wextra", "-Wpedantic",
                        "-Werror", str(ROOT / "ordered_sampler.cpp"), "-o", str(executable)],
                       check=True, timeout=30)
        digest = hashlib.sha256(executable.read_bytes()).hexdigest()
        serial = fixture_run(executable, root / "serial", 1, digest)
        parallel = fixture_run(executable, root / "parallel", 4, digest)
        paths = [
            "generation/measurements.jsonl", "generation/receipts.json",
            "generation/thermal-1.json", "generation/thermal-2.json",
            "generation/measurement-sentinels.json", "replay/replay-receipt.json",
        ]
        paths.extend(f"{stage}{i}/protocol.log" for stage in
                     ("generation/thermal-1-c", "generation/thermal-2-c",
                      "generation/measurement-c", "replay/replay-c")
                     for i in driver.CHAIN_IDS)
        for name in paths:
            one, four = root / "serial" / name, root / "parallel" / name
            assert one.read_bytes() == four.read_bytes(), name
        cancellation = root / "cancel"
        cancellation.mkdir()
        cancellation_fixture(cancellation)
        series = root / "parallel" / "generation" / "measurements.jsonl"
        sha256 = hashlib.sha256(series.read_bytes()).hexdigest()
        print(f"PARALLEL L16 MEASUREMENT, REPLAY AND CANCELLATION PASS sha256={sha256}")
        print(f"workers=1 generation_seconds={serial[0]:.3f} replay_seconds={serial[1]:.3f}")
        print(f"workers=4 generation_seconds={parallel[0]:.3f} replay_seconds={parallel[1]:.3f}")


if __name__ == "__main__":
    main()
