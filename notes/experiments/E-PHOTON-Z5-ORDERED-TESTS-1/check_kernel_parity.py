"""PRE-PIN L3/L4 integrity fixtures only. No pilot or production CLI is invoked."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile
from prepare_capacity import ROOT, prepare

def invoke(args, timeout):
    result = subprocess.run(args, capture_output=True, timeout=timeout, check=False)
    if result.returncode or result.stderr:
        raise RuntimeError(str(args) + "\n" + result.stderr.decode(errors="replace"))
    return result.stdout

def check():
    prepare()
    compiler = os.environ.get("CXX") or shutil.which("g++")
    if not compiler:
        raise RuntimeError("C++20 g++ with Boost.Multiprecision headers is required")
    with tempfile.TemporaryDirectory(prefix="ordered-kernel-parity-") as temporary:
        temporary = Path(temporary)
        results = []
        for directory in ("upstream", "kernel64"):
            exe = temporary / (directory + (".exe" if os.name == "nt" else ""))
            invoke([compiler, "-std=c++20", "-O2", "-Wall", "-Wextra", "-Wpedantic", "-Werror",
                    str(ROOT / directory / "photon_z5.cpp"), "-o", str(exe)], 120)
            results.append(invoke([str(exe), "--fixture"], 45))
        if results[0] != results[1]:
            raise RuntimeError("capacity-only copy changed exact L3/L4 fixture bytes")
        print("PREPIN_SYNTHETIC_L3_L4_ORIGINAL_CAPACITY_PARITY PASS")

if __name__ == "__main__":
    check()
