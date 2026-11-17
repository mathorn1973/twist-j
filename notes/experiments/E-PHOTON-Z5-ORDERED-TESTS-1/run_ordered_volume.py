"""Local pre-pin driver for one registered volume and exact replay custody."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager, nullcontext
from functools import partial
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import threading
import time

import numpy as np

from analyze_ordered import A_VOLUMES, D_VOLUMES, ENDPOINTS, SAMPLES, VOLUMES, load_diagnostics
from ordered_reader import SCHEMA, measure_bytes

SEED_BASE = 0xC571000000000000
CHAIN_IDS = (1, 2, 3, 4)
TASKSET = "/usr/bin/taskset"
CATEGORICAL_KINDS = ("HOT", "LOCAL", "LINE", "FLAT", "CHARGE")


def parse_affinity(value):
    """Four canonical, equal-size, disjoint lists in chain order."""
    syntax = r"(?:0|[1-9][0-9]*)(?:,(?:0|[1-9][0-9]*))*"
    groups = value.split(";")
    if len(groups) != len(CHAIN_IDS) or any(not re.fullmatch(syntax, group) for group in groups):
        raise argparse.ArgumentTypeError("affinity requires four comma-separated CPU lists separated by semicolons")
    affinity = tuple(tuple(map(int, group.split(","))) for group in groups)
    if any(tuple(sorted(set(group))) != group or len(group) != len(affinity[0])
           for group in affinity):
        raise argparse.ArgumentTypeError("CPU lists must be increasing and have equal widths")
    if len(set().union(*affinity)) != len(CHAIN_IDS) * len(affinity[0]):
        raise argparse.ArgumentTypeError("CPU lists must be disjoint")
    return affinity


def validate_affinity(affinity, chain_workers):
    if affinity is None:
        return
    if chain_workers != len(CHAIN_IDS):
        raise ValueError("--affinity requires --chain-workers 4")
    if platform.system() != "Linux" or not os.access(TASKSET, os.X_OK):
        raise ValueError("--affinity requires Linux and executable /usr/bin/taskset")
    if not set().union(*affinity).issubset(os.sched_getaffinity(0)):
        raise ValueError("requested CPUs are outside the controller's affinity")


def affinity_record(affinity):
    width = str(len(affinity[0]))
    return {
        "taskset": TASKSET,
        "cpu_groups_in_chain_order": [list(group) for group in affinity],
        "environment": {
            "OMP_NUM_THREADS": width, "OMP_THREAD_LIMIT": width,
            "OMP_DYNAMIC": "FALSE", "OMP_PLACES": "cores",
            "OMP_PROC_BIND": "close", "OMP_WAIT_POLICY": "PASSIVE",
        },
    }


def named(line, marker):
    parts = line.split()
    if not parts or parts[0] != marker:
        raise ValueError(f"Expected {marker}")
    fields = {}
    for part in parts[1:]:
        key, sep, value = part.partition("=")
        if not sep or not key or not value or key in fields:
            raise ValueError(f"Malformed {marker} field")
        fields[key] = value
    return fields


def require_fields(line, marker, expected):
    actual = named(line, marker)
    if any(actual.get(k) != str(v) for k, v in expected.items()):
        raise ValueError(f"Unexpected {marker} metadata")
    return actual


def json_file(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as output:
        output.write(json.dumps(value, indent=2, allow_nan=False) + "\n")
        output.flush()
        os.fsync(output.fileno())


def json_line(output, value):
    output.write(json.dumps(value, separators=(",", ":"), allow_nan=False) + "\n")
    output.flush()
    os.fsync(output.fileno())


def chain_settings(L, chain):
    return f"L{L}-c{chain}", SEED_BASE + L * 65536 + chain, ("cold" if chain < 3 else "hot")


def state_size(L, chain_name, sample, macrocycle):
    metadata = (SCHEMA + f"\nL={L}\nCHAIN={chain_name}\nSAMPLE={sample}\n"
                f"MACROCYCLE={macrocycle}\nLINKS=\nEND\n".encode("ascii"))
    return len(metadata) + 4 * L**4


def read_frame(pipe, line, *, L, chain_name, sample, macrocycle):
    size = state_size(L, chain_name, sample, macrocycle)
    require_fields(line, "STATE_BEGIN", {"sample": sample, "bytes": size})
    payload = pipe.read(size)
    if len(payload) != size:
        raise ValueError("Truncated state frame")
    return payload


def read_control(pipe, log):
    raw = pipe.readline(16384)
    if not raw.endswith(b"\n"):
        raise ValueError("Truncated sampler control line")
    log.write(raw)
    return raw[:-1].decode("ascii")


def verify_counters(control, L, cycles):
    forward, reverse = (cycles + 1) // 2, cycles // 2
    local, line = 4 * L**4 * cycles, 4 * L**3 * cycles
    require_fields(control(), "UPDATE_DIAGNOSTICS", {
        "macro_cycles": cycles, "local_decisions": local, "line_decisions": line,
        "flat_sheets": 4 * cycles, "charge_trials": cycles,
    })
    totals = require_fields(control(), "DIAGNOSTICS", {
        "macro_cycles": cycles,
        "local_forward": forward, "local_reverse": reverse, "local_updates": local,
        "line_forward": forward, "line_reverse": reverse, "line_updates": line,
        "flat_trials": 4 * cycles, "flat_flux_identity_checks": 4 * cycles,
        "charge_trials": cycles, "charge_flux_identity_checks": cycles,
    })
    directions = named(control(), "LINE_CHANGES_BY_DIRECTION")
    counts = [int(directions[f"mu{axis}"]) for axis in range(4)]
    if any(x < 0 or x > cycles * L**3 for x in counts) or sum(counts) != int(totals["line_changes"]):
        raise ValueError("Line change counts do not reconcile")
    for kind in CATEGORICAL_KINDS:
        fields = require_fields(control(), "CATEGORICAL", {"kind": kind, "stops": 0})
        attempts, completed, bits = (int(fields[k]) for k in ("attempts", "completed", "max_bits"))
        expected = {"HOT": 0, "LOCAL": local, "LINE": line, "FLAT": 0, "CHARGE": 0}
        if completed != attempts or attempts != expected[kind] or not 0 <= bits <= 256:
            raise ValueError(f"Inconsistent exact prefix diagnostics for {kind}")
    if control() != "ORDERED_STATUS GENERATION_COMPLETE_UNCLASSIFIED":
        raise ValueError("Missing sampler completion marker")


class ChainCohort:
    """Track live sampler children so one failed chain cancels the stage."""
    def __init__(self):
        self.lock = threading.Lock()
        self.children = set()
        self.cancelled = False

    @contextmanager
    def supervise(self, child):
        with self.lock:
            if self.cancelled:
                child.kill()
                raise RuntimeError("Sampler stage cancelled")
            self.children.add(child)
        try:
            yield
        finally:
            with self.lock:
                self.children.remove(child)

    def cancel(self):
        with self.lock:
            self.cancelled = True
            for child in self.children:
                child.kill()


def run_chains(worker, chain_workers):
    """Run a four-chain stage and return results in chain ID order."""
    if chain_workers == 1:
        return [worker(i, None) for i in CHAIN_IDS]
    if chain_workers != len(CHAIN_IDS):
        raise ValueError("Use one worker or one per chain")
    cohort = ChainCohort()
    with ThreadPoolExecutor(max_workers=chain_workers) as executor:
        futures = {}
        try:
            futures = {executor.submit(worker, i, cohort): i for i in CHAIN_IDS}
            results = {}
            for future in as_completed(futures):
                results[futures[future]] = future.result()
        except BaseException:
            cohort.cancel()
            for future in futures:
                future.cancel()
            raise
    return [results[i] for i in CHAIN_IDS]


def require_time(deadline):
    if time.monotonic() >= deadline:
        raise TimeoutError("Volume time budget exhausted")


@contextmanager
def launch(args, directory, deadline, *, cohort=None, env=None):
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise TimeoutError("Volume time budget exhausted")
    directory.mkdir()
    json_file(directory / "command.json", args)
    with (directory / "stderr.log").open("xb") as error:
        with subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=error, env=env) as child:
            expired = threading.Event()

            def expire():
                expired.set()
                child.kill()

            timer = threading.Timer(deadline - time.monotonic(), expire)
            guard = cohort.supervise(child) if cohort is not None else nullcontext()
            with guard:
                timer.start()
                try:
                    yield child
                    if child.stdout.read(1) or child.wait() != 0:
                        raise ValueError("Unexpected output or failed sampler exit")
                    require_time(deadline)
                except BaseException as failure:
                    if expired.is_set():
                        raise TimeoutError("Volume time budget exhausted") from failure
                    raise
                finally:
                    timer.cancel()
                    if child.poll() is None:
                        child.kill()


def run_chain(sampler, directory, deadline, L, chain, thermal, samples,
              previous_prefix=(), accepted_state=None, *, cohort=None, affinity=None):
    chain_name, seed, start = chain_settings(L, chain)
    command = [str(sampler), "--mode", "run", "--L", str(L), "--seed", str(seed),
               "--start", start, "--thermal", str(thermal), "--samples", str(samples),
               "--between", "1", "--chain", chain_name, "--output-dir", "-", "--t", "1",
               "--transport", "stream", "--thermal-sentinels", "1"]
    options = {"cohort": cohort}
    if affinity is not None:
        cpus = ",".join(map(str, affinity[chain - 1]))
        command = [TASKSET, "-c", cpus, *command]
        options["env"] = {**os.environ, **affinity_record(affinity)["environment"]}
    with launch(command, directory, deadline, **options) as child:
        with (directory / "protocol.log").open("xb") as log:
            control = partial(read_control, child.stdout, log)
            require_fields(control(), "ORDERED_RUN", {
                "schema": SCHEMA.decode("ascii"), "L": L, "seed": seed, "start": start,
                "chain": chain_name, "thermal": thermal, "samples": samples, "between": 1,
                "t": 1, "mode": "run", "transport": "stream", "thermal_sentinels": 1,
            })
            prefix = []
            for cycle in range(1, thermal + 1):
                require_fields(control(), "THERMAL_SENTINEL", {"macrocycle": cycle})
                sentinel = control()
                require_fields(sentinel, "SAMPLE", {"index": cycle - 1})
                if cycle <= len(previous_prefix) and sentinel != previous_prefix[cycle - 1]:
                    raise ValueError("Thermal deterministic replay mismatch")
                prefix.append(sentinel)
            saved = []
            for sample in range(samples):
                macrocycle = thermal + sample + 1
                payload = read_frame(child.stdout, control(), L=L, chain_name=chain_name,
                                     sample=sample, macrocycle=macrocycle)
                require_fields(control(), "STATE_END", {"sample": sample})
                accepted_state(payload, L, chain_name, sample, macrocycle)
                del payload
                child.stdin.write(f"ACK {sample}\n".encode("ascii"))
                child.stdin.flush()
                sentinel = control()
                require_fields(sentinel, "SAMPLE", {"index": sample})
                saved.append(sentinel)
            verify_counters(control, L, thermal + samples)
    return prefix, saved


def scales_for(L):
    return (tuple(scale for scale, volumes in A_VOLUMES.items() if L in volumes),
            tuple(scale for scale, volumes in D_VOLUMES.items() if L in volumes))


def measure_state(output, requested_m, requested_R, payload, L, chain, sample, macrocycle,
                  *, reader=measure_bytes):
    digest = hashlib.sha256(payload).hexdigest()
    measurement = reader(payload, digest, requested_m, requested_R, secondary=True)
    identity = (measurement["L"], measurement["chain"], measurement["sample"], measurement["macrocycle"])
    if identity != (L, chain, sample, macrocycle):
        raise ValueError("Incorrect saved-state identity")
    json_line(output, {**measurement, "state_sha256": digest, "state_bytes": len(payload)})


def combine_measurements(directory, deadline):
    temporary = directory / "measurements.pending"
    with temporary.open("xb") as target:
        for i in CHAIN_IDS:
            require_time(deadline)
            with (directory / f"measurement-c{i}.jsonl").open("rb") as source:
                shutil.copyfileobj(source, target, length=1 << 20)
        target.flush()
        os.fsync(target.fileno())
    require_time(deadline)
    temporary.replace(directory / "measurements.jsonl")


def run_volume(sampler, diagnostics, directory, L, deadline, *, chain_workers=1, affinity=None,
               reader_workers=0):
    from ordered_sentinels import assess

    previous = [[] for _ in CHAIN_IDS]
    binding = {"affinity": affinity} if affinity is not None else {}
    for endpoint in sorted(ENDPOINTS):
        def thermal_worker(i, cohort):
            return run_chain(sampler, directory / f"thermal-{endpoint}-c{i}",
                             deadline, L, i, endpoint, 0, previous[i - 1],
                             cohort=cohort, **binding)[0]

        previous = run_chains(thermal_worker, chain_workers)
        candidate = assess(previous, diagnostics)
        require_time(deadline)
        json_file(directory / f"thermal-{endpoint}.json", candidate)
        if candidate["status"] == "PASS":
            break
    else:
        return {"status": "STOP_MIXING", "endpoint": None, "measurement_sentinels": None}

    requested_m, requested_R = scales_for(L)

    if reader_workers:
        from parallel_ordered_reader import ParallelReader
        reader_scope = ParallelReader(reader_workers)
    else:
        reader_scope = nullcontext()
    with reader_scope as service:
        reader = measure_bytes if service is None else service.measure_bytes

        def measurement_worker(i, cohort):
            with (directory / f"measurement-c{i}.jsonl").open("x", encoding="utf-8", newline="\n") as output:
                receive = partial(measure_state, output, requested_m, requested_R, reader=reader)
                return run_chain(sampler, directory / f"measurement-c{i}", deadline,
                                 L, i, endpoint, SAMPLES, previous[i - 1], receive,
                                 cohort=cohort, **binding)[1]

        measured = run_chains(measurement_worker, chain_workers)
    combine_measurements(directory, deadline)
    result = assess(measured, diagnostics, measurement=True)
    require_time(deadline)
    json_file(directory / "measurement-sentinels.json", result)
    return {"status": "PASS", "endpoint": endpoint, "measurement_sentinels": result["status"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", required=True, type=int, choices=VOLUMES)
    parser.add_argument("--sampler", required=True, type=Path)
    parser.add_argument("--sampler-sha256", required=True)
    parser.add_argument("--diagnostics", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--wall-seconds", required=True, type=int)
    parser.add_argument("--chain-workers", type=int, choices=(1, 4), default=1)
    parser.add_argument("--affinity", type=parse_affinity, metavar="CPU-LIST;CPU-LIST;CPU-LIST;CPU-LIST")
    parser.add_argument("--reader-workers", type=int, choices=range(25), default=0, metavar="0..24")
    args = parser.parse_args()
    try:
        validate_affinity(args.affinity, args.chain_workers)
    except ValueError as error:
        parser.error(str(error))
    if args.wall_seconds < 1:
        parser.error("Wall budget must be positive")
    sampler = args.sampler.resolve(strict=True)
    payload = sampler.read_bytes()
    if hashlib.sha256(payload).hexdigest() != args.sampler_sha256:
        raise ValueError("Sampler executable SHA-256 mismatch")
    diagnostics = load_diagnostics(args.diagnostics)
    output = args.output.resolve()
    output.mkdir()
    custody = output / sampler.name
    with custody.open("xb") as target:
        target.write(payload)
    custody.chmod(sampler.stat().st_mode & 0o777)
    environment = {
        "sampler_sha256": args.sampler_sha256, "python": platform.python_version(),
        "platform": platform.platform(), "machine": platform.machine(), "numpy": np.__version__,
        "longdouble_mantissa_bits": int(np.finfo(np.longdouble).nmant) + 1,
        "wall_seconds": args.wall_seconds, "chain_workers": args.chain_workers, "L": args.volume,
    }
    binding = {}
    if args.affinity is not None:
        environment["affinity"] = affinity_record(args.affinity)
        binding["affinity"] = args.affinity
    if args.reader_workers:
        environment["reader_workers"] = args.reader_workers
        binding["reader_workers"] = args.reader_workers
    json_file(output / "environment.json", environment)
    try:
        budget = time.monotonic() + args.wall_seconds
        receipt = run_volume(custody, diagnostics, output, args.volume, budget,
                             chain_workers=args.chain_workers, **binding)
    except Exception as failure:
        endpoint = next((t for t in sorted(ENDPOINTS)
                         if (path := output / f"thermal-{t}.json").is_file()
                         and json.loads(path.read_text(encoding="utf-8"))["status"] == "PASS"), None)
        stop = "STOP_BUDGET" if isinstance(failure, TimeoutError) else "STOP_INTEGRITY"
        receipt = {"status": stop, "endpoint": endpoint, "detail": str(failure),
                   "sampler_sha256": args.sampler_sha256}
        if stop == "STOP_INTEGRITY":
            json_file(output / "receipts.json", {str(args.volume): receipt})
            raise
    receipt["sampler_sha256"] = args.sampler_sha256
    json_file(output / "receipts.json", {str(args.volume): receipt})


if __name__ == "__main__":
    main()
