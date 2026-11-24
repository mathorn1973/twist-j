"""PRE-PIN exporter check using only the inherited two-cycle L3/L4 fixtures."""
from pathlib import Path
import hashlib
import os
import shutil
import subprocess
import tempfile
from prepare_capacity import ROOT, prepare

def invoke(args, timeout=45):
    result = subprocess.run(args, capture_output=True, timeout=timeout, check=False)
    if result.returncode or result.stderr:
        raise RuntimeError(str(args) + "\n" + result.stderr.decode(errors="replace"))
    return result.stdout

def check():
    prepare()
    compiler = os.environ.get("CXX") or shutil.which("g++")
    if not compiler:
        raise RuntimeError("g++ and Boost.Multiprecision required")
    with tempfile.TemporaryDirectory(prefix="ordered-export-fixture-") as temporary:
        temporary = Path(temporary)
        exe = temporary / ("adapter.exe" if os.name == "nt" else "adapter")
        invoke([compiler, "-std=c++20", "-O2", "-Wall", "-Wextra", "-Wpedantic", "-Werror",
                str(ROOT / "ordered_sampler.cpp"), "-o", str(exe)], 120)
        for L, expected in ((3, "f2ddb5b90debf718"), (4, "6119d2e215a1020b")):
            output = temporary / ("fixture-L" + str(L))
            stdout = invoke([str(exe), "--mode", "run", "--L", str(L), "--seed",
                             str(0x123456789ABCDEF0), "--start", "hot", "--thermal", "0",
                             "--samples", "1", "--between", "2", "--chain", "synthetic-integrity-L" + str(L),
                             "--output-dir", str(output), "--t", "1"])
            assert b"state_hash=" + expected.encode() in stdout
            state = (output / "sample-0000000000.state").read_bytes()
            assert state.endswith(b"\n") and b"\r" not in state
            lines = state.splitlines()
            assert len(lines) == 7
            assert lines[0] == b"TWISTJ_Z5_ORDERED_LINK_STATE_V1"
            assert lines[1] == b"L=" + str(L).encode()
            assert lines[2] == b"CHAIN=synthetic-integrity-L" + str(L).encode()
            assert lines[3:5] == [b"SAMPLE=0", b"MACROCYCLE=2"]
            assert lines[6] == b"END" and lines[5].startswith(b"LINKS=")
            payload = lines[5][6:]
            assert len(payload) == 4 * L**4 and set(payload) <= set(b"01234")
            assert b"\n".join(lines) + b"\n" == state
            print("PREPIN_EXPORT_FIXTURE L=" + str(L) + " bytes=" + str(len(state))
                  + " sha256=" + hashlib.sha256(state).hexdigest() + " PASS")
        print("PREPIN_EXPORT_FIXTURES_ONLY PASS")

if __name__ == "__main__":
    check()
