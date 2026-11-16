"""End-to-end driver check on the inherited two-cycle L3 integrity fixture."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory
import time
from unittest.mock import patch

from prepare_capacity import ROOT, prepare
from ordered_reader import parse_state
from run_ordered_volume import run_chain, state_size


def check():
    prepare()
    compiler = os.environ.get("CXX") or shutil.which("g++")
    if compiler is None:
        raise RuntimeError("g++ with Boost headers required")
    with TemporaryDirectory(prefix="ordered-driver-fixture-") as scratch:
        directory = Path(scratch)
        executable = directory / ("adapter.exe" if os.name == "nt" else "adapter")
        subprocess.run([compiler, "-std=c++20", "-O2", "-Wall", "-Wextra", "-Wpedantic",
                        "-Werror", str(ROOT / "ordered_sampler.cpp"), "-o", str(executable)],
                       check=True, timeout=120)
        settings = ("fixture", 0x123456789ABCDEF0, "hot")
        deadline = time.monotonic() + 45

        def receive(payload, L, chain, sample, macrocycle):
            sha256 = hashlib.sha256(payload).hexdigest()
            meta, _ = parse_state(payload, sha256)
            assert meta == {"L": L, "chain": chain, "sample": sample, "macrocycle": macrocycle}
            assert len(payload) == state_size(L, chain, sample, macrocycle)

        with patch("run_ordered_volume.chain_settings", return_value=settings):
            prefix, no_measurement = run_chain(executable, directory / "thermal", deadline,
                                               3, 1, 1, 0)
            assert len(prefix) == 1 and not no_measurement
            replay, measured = run_chain(executable, directory / "measurement", deadline,
                                         3, 1, 1, 1, prefix, receive)
            assert replay == prefix
            assert len(measured) == 1 and "state_hash=f2ddb5b90debf718" in measured[0]
            try:
                run_chain(executable, directory / "wrong-prefix", deadline, 3, 1, 1, 0,
                          ["SAMPLE index=0 state_hash=bad"])
            except ValueError as error:
                assert "replay mismatch" in str(error)
            else:
                raise AssertionError("Wrong warm prefix accepted")
    print("PREPIN DRIVER L3 PREFIX, CUSTODY, COUNTERS AND REJECTION PASS")


if __name__ == "__main__":
    check()
