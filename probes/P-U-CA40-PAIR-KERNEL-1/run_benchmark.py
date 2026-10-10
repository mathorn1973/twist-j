#!/usr/bin/env python3
"""Linux-only, stdlib benchmark runner. Source creation does not authorize a run.

Run only after the approved source/input pin. This records an engineering
benchmark, not hardware admission or the independent exact scientific oracle.
The binary is built separately; this script never compiles or installs anything.
"""

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import signal
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path


CONFIGS = (("avx2", 40), ("avx512", 40), ("avx2", 80), ("avx512", 80))
CANDIDATES = 512
STATE_COUNT = 78125
DIAGNOSTICS = ("checksum", "phase_max", "r_max")
CAPTURE_LIMIT = 2 * 1024 * 1024
CONTROLLED_ENV = ("OMP_NUM_THREADS", "OMP_THREAD_LIMIT", "OMP_PLACES", "OMP_PROC_BIND",
                  "OMP_DYNAMIC", "OMP_MAX_ACTIVE_LEVELS", "OPENBLAS_NUM_THREADS",
                  "MKL_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
                  "NUMEXPR_NUM_THREADS", "MKL_DYNAMIC", "LC_ALL")


def cpu_list(value):
    found = set()
    for part in value.strip().split(","):
        ends = part.split("-")
        if not 1 <= len(ends) <= 2 or not all(x.isdecimal() for x in ends):
            raise ValueError("invalid sysfs CPU list: " + value)
        low, high = int(ends[0]), int(ends[-1])
        if high < low:
            raise ValueError("reversed CPU range")
        members = set(range(low, high + 1))
        if found & members:
            raise ValueError("duplicate CPU in sysfs list")
        found.update(members)
    return found


def topology():
    if sys.platform != "linux" or not hasattr(os, "sched_getaffinity"):
        raise RuntimeError("Linux sched_getaffinity is required")
    allowed = set(os.sched_getaffinity(0))
    if len(allowed) != 80:
        raise RuntimeError("strict target requires 80 allowed logical CPUs")
    records, cores = [], {}
    for cpu in sorted(allowed):
        root = Path("/sys/devices/system/cpu") / ("cpu" + str(cpu))
        topo = root / "topology"
        package = int((topo / "physical_package_id").read_text().strip())
        core = int((topo / "core_id").read_text().strip())
        siblings = cpu_list((topo / "thread_siblings_list").read_text())
        nodes = [int(p.name[4:]) for p in root.glob("node[0-9]*")
                 if p.name[4:].isdecimal()]
        if len(nodes) != 1:
            raise RuntimeError("one actual NUMA node per CPU is required")
        row = dict(cpu=cpu, package=package, core=core, node=nodes[0],
                   siblings=sorted(siblings))
        records.append(row)
        cores.setdefault((package, core), []).append(row)
    packages = {r["package"] for r in records}
    nodes = {r["node"] for r in records}
    if len(cores) != 40 or len(packages) != 2 or len(nodes) != 2:
        raise RuntimeError("expected 40 physical cores, two packages and two NUMA nodes")
    for package in packages:
        if sum(key[0] == package for key in cores) != 20:
            raise RuntimeError("expected 20 physical cores per package")
    for rows in cores.values():
        members = {r["cpu"] for r in rows}
        if len(rows) != 2 or len({r["node"] for r in rows}) != 1:
            raise RuntimeError("expected two same-node SMT siblings per physical core")
        if any(set(r["siblings"]) != members for r in rows):
            raise RuntimeError("partial or inconsistent physical-core affinity")
    per_node = {}
    for node in sorted(nodes):
        members = sorted(min(r["cpu"] for r in rows)
                         for rows in cores.values() if rows[0]["node"] == node)
        if len(members) != 20:
            raise RuntimeError("expected 20 physical cores per NUMA node")
        per_node[node] = members
    # Alternate NUMA nodes; never infer physical cores from CPU-number parity.
    selected40 = [cpu for group in zip(*per_node.values()) for cpu in group]
    by_cpu = {r["cpu"]: r for r in records}
    partners = [next(c for c in by_cpu[cpu]["siblings"] if c != cpu)
                for cpu in selected40]
    selected80 = selected40 + partners
    return records, {40: selected40, 80: selected80}, allowed


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def reject_constant(value):
    raise ValueError("non-finite JSON constant: " + value)


def unique_object(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON object key: " + key)
        result[key] = value
    return result


def finite_tree(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("non-finite JSON number")
    if isinstance(value, dict):
        for child in value.values():
            finite_tree(child)
    elif isinstance(value, list):
        for child in value:
            finite_tree(child)


def parse_result(raw, backend, threads, cpus, repeats):
    result = json.loads(raw.decode("utf-8"), parse_constant=reject_constant,
                        object_pairs_hook=unique_object)
    if not isinstance(result, dict):
        raise ValueError("stdout must contain exactly one JSON object")
    finite_tree(result)
    if result.get("backend") != backend or type(result.get("threads")) is not int:
        raise ValueError("wrong backend or invalid thread count")
    if result["threads"] != threads or result.get("validation_passed") is not True:
        raise ValueError("wrong thread count or failed binary validation")
    elapsed = result.get("elapsed_seconds")
    if type(elapsed) not in (float, int) or elapsed <= 0:
        raise ValueError("elapsed_seconds must be positive and finite")
    branches = result.get("branches_processed")
    if type(branches) is not int or branches != STATE_COUNT * CANDIDATES * repeats:
        raise ValueError("branches_processed differs from 78125*candidates*repeats")
    for key, expected in (("candidates", CANDIDATES), ("repeats", repeats)):
        if type(result.get(key)) is not int or result[key] != expected:
            raise ValueError("wrong or missing " + key)
    error = result.get("max_abs_error")
    if type(error) not in (float, int) or not 0 <= error <= 1e-12:
        raise ValueError("max_abs_error must be in [0, 1e-12]")
    for key in DIAGNOSTICS:
        if key not in result or type(result[key]) not in (float, int):
            raise ValueError("missing numeric diagnostic: " + key)
    mapping = result.get("thread_map")
    if not isinstance(mapping, list) or len(mapping) != threads:
        raise ValueError("missing or incomplete thread_map")
    tids, seen_cpus, places = set(), set(), set()
    for row in mapping:
        if not isinstance(row, dict) or any(type(row.get(k)) is not int
                                           for k in ("thread", "cpu", "place")):
            raise ValueError("invalid thread_map entry")
        tid, cpu, place = row["thread"], row["cpu"], row["place"]
        if not 0 <= tid < threads or not 0 <= place < threads:
            raise ValueError("thread or place outside configured range")
        if tid in tids or cpu in seen_cpus or place in places:
            raise ValueError("duplicate thread, CPU or place")
        if cpu != cpus[place]:
            raise ValueError("actual CPU does not match its explicit OpenMP place")
        tids.add(tid)
        seen_cpus.add(cpu)
        places.add(place)
    if seen_cpus != set(cpus):
        raise ValueError("worker CPU set differs from requested affinity")
    return result


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False)
                    + "\n", encoding="utf-8")


def make_env(threads, cpus):
    # Remove inherited vendor affinity overrides before supplying one contract.
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("OMP_", "GOMP_", "KMP_"))}
    env.update(OMP_NUM_THREADS=str(threads), OMP_THREAD_LIMIT=str(threads),
               OMP_PLACES=",".join("{" + str(cpu) + "}" for cpu in cpus),
               OMP_PROC_BIND="true", OMP_DYNAMIC="FALSE", OMP_MAX_ACTIVE_LEVELS="1",
               OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", BLIS_NUM_THREADS="1",
               VECLIB_MAXIMUM_THREADS="1", NUMEXPR_NUM_THREADS="1",
               MKL_DYNAMIC="FALSE", LC_ALL="C")
    return env


def check_pins(pins):
    for name, expected in pins.items():
        if sha256(Path(name)) != expected:
            raise RuntimeError("source or binary changed during campaign: " + name)


def interrupt(signum, frame):
    raise KeyboardInterrupt("received signal " + str(signum))


def invoke(args, phase, round_index, backend, threads, cpus, pins, stream, reference):
    check_pins(pins)
    tag = "{}_{}_{}_{}".format(phase, round_index, backend, threads)
    stdout_path = args.output / "raw" / (tag + ".stdout.json")
    stderr_path = args.output / "raw" / (tag + ".stderr.txt")
    command = [str(args.binary), "--backend", backend, "--threads", str(threads),
               "--repeats", str(args.repeats), "--candidates", str(CANDIDATES)]
    record = dict(phase=phase, round=round_index, backend=backend, threads=threads,
                  command=command, requested_cpus=cpus, status="failed",
                  stdout_file=str(stdout_path.relative_to(args.output)),
                  stderr_file=str(stderr_path.relative_to(args.output)))
    started = time.perf_counter()
    try:
        with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
            child = None
            try:
                previous = os.sched_getaffinity(0)
                try:
                    # Single-threaded runner; the child inherits the exact mask.
                    os.sched_setaffinity(0, set(cpus))
                    child = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                             env=make_env(threads, cpus), start_new_session=True)
                finally:
                    os.sched_setaffinity(0, previous)
                try:
                    child.wait(timeout=args.timeout)
                except subprocess.TimeoutExpired:
                    record["timed_out"] = True
                    raise RuntimeError("binary exceeded per-invocation watchdog")
            except BaseException:
                if child is not None and child.poll() is None:
                    try:
                        os.killpg(child.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    child.wait(timeout=2)
                if child is not None:
                    record["returncode"] = child.returncode
                raise
        record["wall_seconds"] = time.perf_counter() - started
        record["returncode"] = child.returncode
        if child.returncode != 0:
            raise RuntimeError("binary exited with status " + str(child.returncode))
        if stderr_path.stat().st_size:
            raise RuntimeError("binary wrote to stderr; see preserved raw file")
        if stdout_path.stat().st_size > CAPTURE_LIMIT:
            raise RuntimeError("unexpectedly large JSON stdout")
        result = parse_result(stdout_path.read_bytes(), backend, threads, cpus, args.repeats)
        record["result"] = result
        if not reference:
            reference.update({key: result[key] for key in DIAGNOSTICS})
            write_json(args.output / "baseline.json", dict(invocation=tag, diagnostics=reference))
        # Decimal strings keep even an extreme mismatch's delta finite/serializable.
        record["diagnostic_differences"] = {
            key: str(Decimal(str(result[key])) - Decimal(str(reference[key])))
            for key in DIAGNOSTICS}
        if any(result[key] != reference[key] for key in DIAGNOSTICS):
            raise ValueError("checksum/phase_max/r_max differ from first warmup baseline")
        check_pins(pins)
        record["status"] = "ok"
        return record
    except BaseException as error:
        record["wall_seconds"] = time.perf_counter() - started
        record["error"] = str(error)
        raise
    finally:
        stream.write(json.dumps(record, sort_keys=True, allow_nan=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
        print(json.dumps({k: record[k] for k in
                          ("phase", "round", "backend", "threads", "status")}), flush=True)


def summarize(output, samples):
    fields = ["backend", "threads", "rounds", "wall_median_s", "wall_min_s",
              "wall_max_s", "wall_stdev_s", "kernel_median_s",
              "kernel_min_s", "kernel_max_s", "branches_per_kernel_second_median",
              "max_abs_error_max"]
    fields += [key + suffix for key in DIAGNOSTICS for suffix in ("_delta_min", "_delta_max")]
    with (output / "summary.csv").open("x", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for backend, threads in CONFIGS:
            rows = [r for r in samples if r["backend"] == backend and r["threads"] == threads]
            wall = [r["wall_seconds"] for r in rows]
            kernel = [r["result"]["elapsed_seconds"] for r in rows]
            rate = [r["result"]["branches_processed"] / r["result"]["elapsed_seconds"]
                    for r in rows]
            summary = dict(backend=backend, threads=threads, rounds=len(rows),
                           wall_median_s=statistics.median(wall), wall_min_s=min(wall),
                           wall_max_s=max(wall), wall_stdev_s=statistics.stdev(wall),
                           kernel_median_s=statistics.median(kernel), kernel_min_s=min(kernel),
                           kernel_max_s=max(kernel), branches_per_kernel_second_median=statistics.median(rate),
                           max_abs_error_max=max(r["result"]["max_abs_error"] for r in rows))
            for key in DIAGNOSTICS:
                differences = [Decimal(r["diagnostic_differences"][key]) for r in rows]
                summary[key + "_delta_min"] = str(min(differences))
                summary[key + "_delta_max"] = str(max(differences))
            writer.writerow(summary)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="new, nonexistent directory")
    parser.add_argument("--rounds", type=int, default=5, help="at least five interleaved rotating rounds")
    parser.add_argument("--repeats", type=int, default=4)
    parser.add_argument("--source", type=Path, action="append", help="repeatable; default binary.cpp")
    parser.add_argument("--timeout", type=float, default=55, help="watchdog seconds, 0 < value <= 55")
    args = parser.parse_args()
    if args.rounds < 5 or args.repeats < 1 or not 0 < args.timeout <= 55:
        parser.error("require rounds >= 5, repeats >= 1 and 0 < timeout <= 55")
    args.binary = args.binary.resolve(strict=True)
    if not args.binary.is_file() or not os.access(args.binary, os.X_OK):
        parser.error("binary must be an executable regular file")
    sources = args.source or [args.binary.with_suffix(".cpp")]
    paths = [args.binary, Path(__file__).resolve()] + [p.resolve(strict=True) for p in sources]
    pins = {str(path): sha256(path) for path in paths}
    args.output = args.output.absolute()
    args.output.mkdir(parents=True, exist_ok=False)
    try:
        signal.signal(signal.SIGTERM, interrupt)
        records, selections, allowed = topology()
        (args.output / "raw").mkdir()
        metadata = dict(schema_version=1, started_utc=datetime.now(timezone.utc).isoformat(),
                        platform=platform.system(), release=platform.release(), machine=platform.machine(),
                        python=sys.version, initial_affinity=sorted(allowed), topology=records,
                        selections=selections, file_sha256=pins, candidates=CANDIDATES,
                        state_count=STATE_COUNT, max_abs_error_limit=1e-12,
                        exact_diagnostic_agreement=list(DIAGNOSTICS),
                        repeats=args.repeats, rounds=args.rounds, timeout_seconds=args.timeout,
                        base_config_order=CONFIGS, order_rule="round r rotates base order left by r modulo 4",
                        warmups_per_config=1,
                        controlled_environment={str(n): {key: env[key] for key in CONTROLLED_ENV}
                                                for n, cpus in selections.items()
                                                for env in (make_env(n, cpus),)},
                        wall_seconds_definition="capture-file opening through child exit; excludes parsing and pin checks",
                        scope="engineering benchmark; binary internal validation is separate from exact oracle")
        # These records aid auditing; ancestor cgroup quotas still need operator review.
        metadata["cgroup_metadata"] = {str(p): p.read_text().strip() for p in
                                      (Path("/proc/self/cgroup"), Path("/sys/fs/cgroup/cpu.max"))
                                      if p.is_file()}
        write_json(args.output / "metadata.json", metadata)
        measured = []
        reference = {}
        with (args.output / "samples.jsonl").open("x", encoding="utf-8") as stream:
            for backend, threads in CONFIGS:
                invoke(args, "warmup", 0, backend, threads, selections[threads], pins, stream, reference)
            for round_index in range(args.rounds):
                offset = round_index % len(CONFIGS)
                order = CONFIGS[offset:] + CONFIGS[:offset]
                for backend, threads in order:
                    measured.append(invoke(args, "measured", round_index, backend, threads,
                                           selections[threads], pins, stream, reference))
        check_pins(pins)
        summarize(args.output, measured)
        write_json(args.output / "complete.json", dict(status="complete", measured_invocations=len(measured),
                                                       finished_utc=datetime.now(timezone.utc).isoformat()))
    except BaseException as error:
        write_json(args.output / "failure.json", dict(status="failed", error=str(error),
                                                      finished_utc=datetime.now(timezone.utc).isoformat()))
        print("benchmark stopped: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
