"""PRE-PIN streaming check; only inherited two-cycle L3 integrity trajectory."""
from pathlib import Path
import hashlib
import os
import re
import shutil
import subprocess
import tempfile
import threading
from prepare_capacity import ROOT, prepare

def check():
    prepare()
    compiler = os.environ.get("CXX") or shutil.which("g++")
    if not compiler:
        raise RuntimeError("g++ with Boost headers required")
    with tempfile.TemporaryDirectory(prefix="ordered-stream-fixture-") as temporary:
        exe = Path(temporary) / ("adapter.exe" if os.name == "nt" else "adapter")
        built = subprocess.run([compiler, "-std=c++20", "-O2", "-Wall", "-Wextra", "-Wpedantic", "-Werror",
                                str(ROOT / "ordered_sampler.cpp"), "-o", str(exe)],
                               capture_output=True, timeout=120)
        assert built.returncode == 0 and not built.stderr, built.stderr
        common = [str(exe), "--mode", "run", "--L", "3", "--seed", str(0x123456789ABCDEF0),
                  "--start", "hot", "--between", "1", "--chain", "synthetic-stream-L3",
                  "--output-dir", "-", "--t", "1", "--transport", "stream"]
        thermal = subprocess.run(common + ["--thermal", "2", "--samples", "0", "--thermal-sentinels", "1"],
                                 capture_output=True, timeout=45)
        assert thermal.returncode == 0 and not thermal.stderr
        assert thermal.stdout.count(b"THERMAL_SENTINEL ") == 2
        assert b"STATE_BEGIN" not in thermal.stdout
        assert b"state_hash=f2ddb5b90debf718" in thermal.stdout
        assert b"UPDATE_DIAGNOSTICS macro_cycles=2" in thermal.stdout
        args = common + ["--thermal", "0", "--samples", "2", "--thermal-sentinels", "0"]
        child = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        watchdog = threading.Timer(45, child.kill)
        watchdog.start()
        transcripts = []
        states = []
        try:
            while True:
                line = child.stdout.readline()
                if not line:
                    break
                transcripts.append(line)
                if not line.startswith(b"STATE_BEGIN "):
                    continue
                match = re.fullmatch(rb"STATE_BEGIN sample=([0-9]+) bytes=([0-9]+)\n", line)
                assert match
                index, size = map(int, match.groups())
                data = child.stdout.read(size)
                assert len(data) == size and data.endswith(b"\nEND\n")
                assert len(data.splitlines()) == 7 and b"\r" not in data
                assert b"MACROCYCLE=" + str(index + 1).encode() + b"\n" in data
                assert child.stdout.readline() == b"STATE_END sample=" + str(index).encode() + b"\n"
                states.append((index, size, hashlib.sha256(data).hexdigest()))
                child.stdin.write(b"ACK " + str(index).encode() + b"\n")
                child.stdin.flush()
            child.wait(timeout=5)
            assert child.returncode == 0 and child.stderr.read() == b""
        finally:
            watchdog.cancel()
            if child.poll() is None:
                child.kill()
            child.wait()
        assert len(states) == 2
        combined = b"".join(transcripts)
        assert b"state_hash=f2ddb5b90debf718" in combined
        assert b"UPDATE_DIAGNOSTICS macro_cycles=2" in combined
        # Bad acknowledgement must stop before advancing to a second state.
        bad = subprocess.run(args, input=b"BAD\n", capture_output=True, timeout=45)
        assert bad.returncode != 0 and b"invalid state ACK" in bad.stderr
        assert bad.stdout.count(b"STATE_BEGIN ") == 1
        print("PREPIN_STREAM_FIXTURE L3_TWO_CYCLES_THERMAL_REPLAY_ACK_AND_BAD_ACK PASS")
        for index, size, digest in states:
            print("MEMORY_STATE", index, size, digest)

if __name__ == "__main__":
    check()
