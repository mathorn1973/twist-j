#!/usr/bin/env python3
"""Prospectively frozen, single-attempt engineering controller; never auto-retry."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time

AUDIT = b"NON-CANONICAL floating-point engineering audit\nresult\tPASS\n"
TESTS = b"NON-CANONICAL analyzer fixture audit\nresult\tPASS\n"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("binary", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    binary = args.binary.resolve(strict=True)
    source = Path(__file__).resolve().parent
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    environment = {
        "status": "NON-CANONICAL engineering only; ZERO scientific evidential weight",
        "architecture": platform.machine(), "system": platform.system(),
        "python": platform.python_version(), "workers": 8,
        "per_chain_timeout_seconds": 900, "audit_timeout_seconds": 180,
        "test_timeout_seconds": 60, "analysis_timeout_seconds": 180,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "binary_sha256": digest(binary),
        "source_sha256": {name: digest(source / name) for name in
                          ("sample.cpp", "analyze.py", "test_analyze.py", "run_pilot.py")},
    }
    write_json(out / "environment.json", environment)

    def invoke(command, stem, timeout, extension="tsv"):
        started = time.monotonic()
        stdout_path, stderr_path = out / f"{stem}.{extension}", out / f"{stem}.stderr"
        with stdout_path.open("wb") as stdout, stderr_path.open("wb") as stderr:
            try:
                result = subprocess.run(command, stdout=stdout, stderr=stderr,
                                        timeout=timeout, check=False)
                code = result.returncode
            except subprocess.TimeoutExpired:
                code = 124
            except OSError as error:
                code = 127
                stderr.write(("Launch failure: " + error.__class__.__name__ + "\n").encode())
        return {"stem": stem, "exit_code": code,
                "seconds": round(time.monotonic() - started, 3),
                "stdout_bytes": stdout_path.stat().st_size,
                "stderr_bytes": stderr_path.stat().st_size,
                "stdout_sha256": digest(stdout_path), "stderr_sha256": digest(stderr_path)}

    records = []

    def preserve(record):
        records.append(record)
        write_json(out / "execution.json", records)
        print(json.dumps(record, sort_keys=True), flush=True)

    def finish(disposition, exit_code):
        environment["finished_utc"] = datetime.now(timezone.utc).isoformat()
        write_json(out / "environment.json", environment)
        write_json(out / "controller_result.json", {"disposition": disposition,
                                                    "exit_code": exit_code})
        files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "SHA256SUMS")
        (out / "SHA256SUMS").write_text("".join(digest(p) + "  " + p.name + "\n" for p in files))
        print(disposition, flush=True)
        return exit_code

    preserve(invoke([str(binary), "--audit"], "audit", 180))
    if (records[-1]["exit_code"] != 0 or records[-1]["stderr_bytes"]
            or (out / "audit.tsv").read_bytes() != AUDIT):
        return finish("FAIL_IMPLEMENTATION_AUDIT; no production started", 1)

    preserve(invoke([sys.executable, str(source / "test_analyze.py")], "analyzer_tests", 60))
    if (records[-1]["exit_code"] != 0 or records[-1]["stderr_bytes"]
            or (out / "analyzer_tests.tsv").read_bytes() != TESTS):
        return finish("FAIL_IMPLEMENTATION_ANALYZER_TESTS; no production started", 1)

    jobs = [(4, k, base, chain) for k in (1, 2) for base in (0, 2) for chain in range(5)]
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(invoke, [str(binary), *map(str, (L, k, base, chain))],
                               f"L{L}_k{k}_b{base}_c{chain}", 900)
                   for L, k, base, chain in jobs]
        for future in as_completed(futures):
            preserve(future.result())

    # Invoke the frozen analyzer once even if a declared chain failed. It must
    # preserve that failure rather than silently omit or resubmit the chain.
    analysis = invoke([sys.executable, str(source / "analyze.py"), str(out)],
                      "analysis", 180, "json")
    write_json(out / "analysis_execution.json", analysis)
    failed = any(record["exit_code"] != 0 or record["stderr_bytes"] for record in records)
    failed = failed or analysis["exit_code"] != 0 or analysis["stderr_bytes"] != 0
    return finish("FAIL_IMPLEMENTATION_OR_TIMEOUT" if failed else "EXECUTION_COMPLETE", int(failed))


if __name__ == "__main__":
    raise SystemExit(main())
