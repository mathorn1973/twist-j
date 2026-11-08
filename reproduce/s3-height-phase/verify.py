#!/usr/bin/env python3
"""Hash-bound replay of the unchanged S3 compiler and finite assembly audits."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
NOTE = Path("notes/C-S3-HEIGHT-PHASE-INTERFACE-N/CONSTRUCTIVE-3")
FIXTURE = Path("probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/WORD535.txt")
TIMEOUT_SECONDS = 30
# Exact source bytes and already published outputs; no new search or threshold.
FILES = (
    (NOTE / "verify.py", 8725,
     "356e0c8320fab781b1587f763e759a5356b66630d4a370e152cb92f92ec4345c"),
    (NOTE / "audit.py", 10404,
     "b362fb0e6094ca67a02469bb53b8508ea966484352f511eb98c01ca2795d5fc9"),
    (NOTE / "assembly.py", 8898,
     "0d0743ec8ffba6e0a122beb812492cfa43521c5790d3691d2e80e45e94d192a1"),
    (NOTE / "EXPECTED.txt", 4165,
     "724329795a84ff5f00a908a72ab31ab9ccf8be486def5e58c43a09fcc64c2203"),
    (NOTE / "AUDIT_EXPECTED.txt", 3707,
     "163342bdcd442a962d2281fd9406cb50dc946ebf0fa7e8d0e526b23446a2e9db"),
    (NOTE / "ASSEMBLY_EXPECTED.txt", 2906,
     "fcc72a214caf784942ffdc5a0ed1c05b48c69c8a1558148d6987382c7b9ae74f"),
    (FIXTURE, 4877,
     "ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b"),
)
PROGRAMS = (
    ("verify", "EXPECTED.txt"),
    ("audit", "AUDIT_EXPECTED.txt"),
    ("assembly", "ASSEMBLY_EXPECTED.txt"),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check_custody() -> None:
    for relative, size, digest in FILES:
        data = (ROOT / relative).read_bytes()
        if len(data) != size or sha256(data) != digest:
            raise RuntimeError("S3 input custody mismatch: " + relative.as_posix())


def failure_diagnostics(name: str, stdout: bytes, stderr: bytes) -> None:
    sys.stderr.buffer.write(("S3 " + name + " failed\nSTDOUT:\n").encode("ascii"))
    sys.stderr.buffer.write(stdout)
    sys.stderr.buffer.write(b"\nSTDERR:\n" + stderr + b"\n")


def main() -> None:
    receipt = []
    try:
        if not __debug__:
            raise RuntimeError("S3 reproduction requires assertions enabled")
        check_custody()
        environment = os.environ.copy()
        environment.update(LC_ALL="C", LANG="C", TZ="UTC", PYTHONHASHSEED="0",
                           PYTHONDONTWRITEBYTECODE="1", PYTHONOPTIMIZE="")
        with tempfile.TemporaryDirectory(prefix="s3-height-phase-") as temporary:
            primary_stdout = Path(temporary) / "verify.stdout"
            for name, expected_name in PROGRAMS:
                command = [sys.executable, str(ROOT / NOTE / (name + ".py"))]
                if name == "audit":
                    command.append(str(primary_stdout))
                try:
                    result = subprocess.run(command, cwd=ROOT, env=environment,
                                            capture_output=True, timeout=TIMEOUT_SECONDS)
                except subprocess.TimeoutExpired as error:
                    try:
                        failure_diagnostics(name + " timeout", error.stdout or b"",
                                            error.stderr or b"")
                    except Exception:
                        # A diagnostic-stream failure must not replace the timeout.
                        pass
                    raise
                expected = (ROOT / NOTE / expected_name).read_bytes()
                if result.returncode != 0 or result.stderr or result.stdout != expected:
                    failure_diagnostics(name, result.stdout, result.stderr)
                    raise RuntimeError("S3 reproduction failure: " + name)
                if name == "verify":
                    primary_stdout.write_bytes(result.stdout)
                receipt.append("S3 " + name + " PASS " + str(len(result.stdout))
                               + " " + sha256(result.stdout))
    finally:
        original_error = sys.exc_info()[1]
        try:
            check_custody()
        except Exception as custody_error:
            if original_error is None:
                raise
            try:
                sys.stderr.write("S3 secondary custody failure: " + str(custody_error) + "\n")
            except Exception:
                # Preserve the original program failure even if diagnostics fail.
                pass
    sys.stdout.buffer.write(("\n".join(receipt) + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
