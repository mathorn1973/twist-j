#!/usr/bin/env python3
"""Frozen engineering run controller. Never invoke before public pin readback."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import argparse
import hashlib
import json
import platform
import subprocess
import time

WORKERS = 4
AUDIT_TIMEOUT_SECONDS = 600
JOB_TIMEOUT_SECONDS = 2400
SIZES = (10, 8, 6, 4)  # largest first so the longest jobs start immediately
CONTROL_SIZES = (6, 4)
MODES = (1, 2)
MAIN_CHAINS = (0, 1, 2, 3, 4)
CONTROL_CHAINS = (0, 1, 2, 3)
MAIN_BASE = 0
CONTROL_BASE = 2


def declared_jobs():
    """All 56 jobs, largest volume first; main groups before the control groups of the same L."""
    jobs = []
    for L in SIZES:
        jobs += [(L, k, MAIN_BASE, chain) for k in MODES for chain in MAIN_CHAINS]
        if L in CONTROL_SIZES:
            jobs += [(L, k, CONTROL_BASE, chain) for k in MODES for chain in CONTROL_CHAINS]
    return jobs


def stem_of(L, k, base, chain):
    return f"L{L}_k{k}_c{chain}" if base == MAIN_BASE else f"L{L}_k{k}_b{base}_c{chain}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("binary", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    binary = args.binary.resolve(strict=True)
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    environment = {"architecture": platform.machine(), "system": platform.system(),
                   "python": platform.python_version(), "workers": WORKERS,
                   "audit_timeout_seconds": AUDIT_TIMEOUT_SECONDS,
                   "per_chain_timeout_seconds": JOB_TIMEOUT_SECONDS,
                   "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest()}
    (out / "environment.json").write_text(json.dumps(environment, indent=2) + "\n")

    def invoke(command, stem, timeout):
        started = time.monotonic()
        with (out / (stem + ".tsv")).open("wb") as stdout, \
             (out / (stem + ".stderr")).open("wb") as stderr:
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
                "stdout_bytes": (out / (stem + ".tsv")).stat().st_size,
                "stderr_bytes": (out / (stem + ".stderr")).stat().st_size,
                "stdout_sha256": hashlib.sha256((out / (stem + ".tsv")).read_bytes()).hexdigest(),
                "stderr_sha256": hashlib.sha256((out / (stem + ".stderr")).read_bytes()).hexdigest()}

    records = [invoke([str(binary), "--audit"], "audit", AUDIT_TIMEOUT_SECONDS)]
    (out / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
    if records[0]["exit_code"] != 0 or records[0]["stderr_bytes"]:
        print("FAIL_IMPLEMENTATION: audit; no sampling started", flush=True)
        return 1

    jobs = declared_jobs()
    # All 56 jobs are declared before observation; no resubmission or extension.
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(invoke, [str(binary), str(L), str(k), str(chain), str(base)],
                               stem_of(L, k, base, chain), JOB_TIMEOUT_SECONDS): (L, k, base, chain)
                   for L, k, base, chain in jobs}
        for future in as_completed(futures):
            record = future.result()
            records.append(record)
            (out / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
            print(json.dumps(record, sort_keys=True), flush=True)
    files = sorted(p for p in out.iterdir() if p.is_file())
    (out / "SHA256SUMS").write_text("".join(
        hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.name + "\n" for p in files))
    failed = any(r["exit_code"] != 0 or r["stderr_bytes"] for r in records)
    print("FAIL_IMPLEMENTATION_OR_TIMEOUT" if failed else "EXECUTION_COMPLETE", flush=True)
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
