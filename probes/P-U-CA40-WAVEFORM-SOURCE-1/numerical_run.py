#!/usr/bin/env python3
"""Frozen waveform model campaign. Source preparation never authorizes a run.

Linux, stdlib, AVX512/80 only. Compile separately. Run only after the public
source pin. Floating bounds below are estimates, not interval certificates.
"""
import argparse
import cmath
import hashlib
import importlib.util
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
from pathlib import Path

N = 78125
BRANCHES = 24 * N
TIMEOUT_SECONDS = 55
CAPTURE_LIMIT = 2 * 1024 * 1024
PHASE_TOL = 1e-8
ALPHA_TOL = 1e-9
REPEAT_ABS_TOL = 1e-12
REPEAT_REL_TOL = 1e-12
DIAGNOSTICS = ("gate_phase_max", "gate_r_max", "source_phase_max", "source_r_max",
               "motion_energy_quanta_max", "gate_bound", "source_bound", "checksum")


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path, value):
    with Path(path).open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, sort_keys=True, indent=2, allow_nan=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())


def artifact(path):
    return {"sha256": sha256(path), "bytes": Path(path).stat().st_size}


def check_pins(pins):
    for path, expected in pins.items():
        if sha256(path) != expected:
            raise RuntimeError("Pinned file changed: " + path)


def cpu_list(text):
    found = set()
    for part in text.strip().split(","):
        ends = part.split("-")
        if not 1 <= len(ends) <= 2 or not all(s.isdecimal() for s in ends):
            raise ValueError("Invalid sysfs CPU list")
        lo, hi = int(ends[0]), int(ends[-1])
        if hi < lo:
            raise ValueError("Reversed CPU range")
        entries = set(range(lo, hi + 1))
        if entries & found:
            raise ValueError("Duplicate CPU in sysfs list")
        found.update(entries)
    return found


def topology():
    if sys.platform != "linux" or not hasattr(os, "sched_getaffinity"):
        raise RuntimeError("Linux sched_getaffinity required")
    allowed = set(os.sched_getaffinity(0))
    if len(allowed) != 80:
        raise RuntimeError("Expected exactly 80 allowed logical CPUs")
    rows, cores = [], {}
    for cpu in sorted(allowed):
        root = Path("/sys/devices/system/cpu") / ("cpu" + str(cpu))
        top = root / "topology"
        package = int((top / "physical_package_id").read_text().strip())
        core = int((top / "core_id").read_text().strip())
        siblings = cpu_list((top / "thread_siblings_list").read_text())
        nodes = [int(p.name[4:]) for p in root.glob("node[0-9]*") if p.name[4:].isdecimal()]
        if len(nodes) != 1:
            raise RuntimeError("Exactly one actual NUMA node per CPU required")
        row = dict(cpu=cpu, package=package, core=core, node=nodes[0], siblings=sorted(siblings))
        rows.append(row)
        cores.setdefault((package, core), []).append(row)
    packages, nodes = {r["package"] for r in rows}, {r["node"] for r in rows}
    if len(cores) != 40 or len(packages) != 2 or len(nodes) != 2:
        raise RuntimeError("Expected 40 physical cores, two packages and two NUMA nodes")
    for package in packages:
        if sum(key[0] == package for key in cores) != 20:
            raise RuntimeError("Expected 20 cores per package")
    for siblings in cores.values():
        cpus = {r["cpu"] for r in siblings}
        if len(siblings) != 2 or len({r["node"] for r in siblings}) != 1:
            raise RuntimeError("Expected two same-node SMT siblings per core")
        if any(set(r["siblings"]) != cpus for r in siblings):
            raise RuntimeError("Partial or inconsistent physical-core affinity")
    by_node = {}
    for node in sorted(nodes):
        selected = sorted(min(r["cpu"] for r in group)
                          for group in cores.values() if group[0]["node"] == node)
        if len(selected) != 20:
            raise RuntimeError("Expected 20 physical cores per NUMA node")
        by_node[node] = selected
    first = [cpu for pair in zip(*by_node.values()) for cpu in pair]
    lookup = {r["cpu"]: r for r in rows}
    places = first + [next(c for c in lookup[cpu]["siblings"] if c != cpu) for cpu in first]
    if len(set(places)) != 80 or set(places) != allowed:
        raise RuntimeError("Invalid explicit CPU placement")
    return rows, places, allowed


def environment(places):
    env = {k: v for k, v in os.environ.items() if not k.startswith(("OMP_", "GOMP_", "KMP_"))}
    env.update(OMP_NUM_THREADS="80", OMP_THREAD_LIMIT="80",
               OMP_PLACES=",".join("{" + str(cpu) + "}" for cpu in places),
               OMP_PROC_BIND="true", OMP_DYNAMIC="FALSE", OMP_MAX_ACTIVE_LEVELS="1",
               OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", BLIS_NUM_THREADS="1",
               VECLIB_MAXIMUM_THREADS="1", NUMEXPR_NUM_THREADS="1", MKL_DYNAMIC="FALSE",
               LC_ALL="C")
    return env


def finite_tree(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("Nonfinite JSON number")
    if isinstance(value, dict):
        for child in value.values():
            finite_tree(child)
    elif isinstance(value, list):
        for child in value:
            finite_tree(child)


def duplicate_guard(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("Nonfinite JSON constant: " + value)


def number(value, name, lower=None, upper=None):
    if type(value) not in (float, int) or not math.isfinite(value):
        raise ValueError("Missing or nonnumeric field: " + name)
    if (lower is not None and value < lower) or (upper is not None and value > upper):
        raise ValueError("Out-of-range field: " + name)
    return value


def parse_scanner(raw, names, places):
    obj = json.loads(raw.decode("utf-8"), object_pairs_hook=duplicate_guard,
                     parse_constant=reject_constant)
    if not isinstance(obj, dict):
        raise ValueError("Scanner stdout is not one JSON object")
    finite_tree(obj)
    if obj.get("status") != "PASS" or obj.get("backend") != "avx512":
        raise ValueError("Scanner status/backend mismatch")
    if type(obj.get("threads")) is not int or obj["threads"] != 80:
        raise ValueError("Scanner thread count mismatch")
    if type(obj.get("branches")) is not int or obj["branches"] != BRANCHES:
        raise ValueError("Scanner branch count mismatch")
    number(obj.get("kernel_seconds"), "kernel_seconds", 1e-12)
    number(obj.get("validation_seconds"), "validation_seconds", 1e-12)
    number(obj.get("max_abs_error"), "max_abs_error", 0.0, 1e-9)
    cases = obj.get("cases")
    if not isinstance(cases, list) or len(cases) != 24:
        raise ValueError("Scanner must contain 24 cases")
    if [case.get("name") for case in cases] != names:
        raise ValueError("Scanner case order/names mismatch")
    for case in cases:
        for key in DIAGNOSTICS:
            number(case.get(key), key, None if key == "checksum" else 0.0,
                   1.0 if key in ("gate_bound", "source_bound") else None)
        witnesses = case.get("witness_indices")
        if not isinstance(witnesses, list) or len(witnesses) != 5 or any(
                type(z) is not int or not 0 <= z < N for z in witnesses):
            raise ValueError("Invalid scanner witness indices")
    mapping = obj.get("thread_map")
    if not isinstance(mapping, list) or len(mapping) != 80:
        raise ValueError("Missing full thread map")
    tids, cpus, actual_places = set(), set(), set()
    for row in mapping:
        if not isinstance(row, dict) or any(type(row.get(k)) is not int for k in ("thread", "cpu", "place")):
            raise ValueError("Malformed thread-map row")
        tid, cpu, place = row["thread"], row["cpu"], row["place"]
        if not 0 <= tid < 80 or not 0 <= place < 80 or cpu != places[place]:
            raise ValueError("Actual thread-map placement mismatch")
        if tid in tids or cpu in cpus or place in actual_places:
            raise ValueError("Duplicate thread, CPU or place")
        tids.add(tid)
        cpus.add(cpu)
        actual_places.add(place)
    if cpus != set(places):
        raise ValueError("Actual CPU set differs from requested set")
    return obj


def digits(index):
    out = []
    for _ in range(7):
        out.append(index % 5)
        index //= 5
    return out


def fixture_branches():
    records = []
    for a in range(5):
        for b in range(5):
            labels = [0] * 7
            labels[3], labels[4] = a, b
            records.append(("active_anchor_{}_{}".format(a, b), labels))
    for k in range(32):
        records.append(("full_branch_{}".format(k), digits((12345 + 1871 * k) % N)))
    for ion in (0, 5, 6):
        for label in range(1, 5):
            labels = [0, 0, 0, 1, 3, 0, 0]
            labels[ion] = label
            records.append(("source_{}_{}".format(ion + 1, label), labels))
    return records


def independent_segment(delta, start, duration, amplitude):
    """Endpoint sin/cos formula, independently written from builder sinc.

    Returns displacement per unit complex force and intra-segment phase.
    The exact delta==0 limit is used; frozen nonzero detunings use the
    direct formula. No builder integral or factored-loop helper is called.
    """
    if delta == 0.0:
        return -1j * amplitude * duration, 0.0
    stop = start + duration
    real = (math.sin(delta * stop) - math.sin(delta * start)) / delta
    imag = (math.cos(delta * start) - math.cos(delta * stop)) / delta
    displacement = -1j * amplitude * complex(real, imag)
    phase = amplitude * amplitude * (delta * duration - math.sin(delta * duration)) / (delta * delta)
    return displacement, phase


def direct_schedule(model, job):
    duration = model["config"]["loop_seconds"] / 16.0
    eta = [[complex(*z) for z in mode] for mode in model["modes"]["eta_by_mode_ion"]]
    schedule = []
    for cycle in range(5):
        for k, amplitude in enumerate(job["applied_amplitudes_rad_s"]):
            start = (16 * cycle + k) * duration
            terms = [independent_segment(delta, start, duration, amplitude) for delta in job["delta_rad_s"]]
            schedule.append((cycle, terms))
    return eta, schedule


def direct_branch(job, eta, schedule, labels):
    forces = [[sum((eta[m][i] * job["profiles"][c][i][labels[i]] for i in range(7)), 0j)
               for m in range(7)] for c in range(5)]
    alpha, phi = [0j] * 7, 0.0
    for cycle, terms in schedule:
        for m, (displacement, intrinsic_phase) in enumerate(terms):
            g = forces[cycle][m]
            increment = displacement * g
            phi += intrinsic_phase * (g.real * g.real + g.imag * g.imag)
            phi += (increment * alpha[m].conjugate()).imag
            alpha[m] += increment
    return alpha, phi


def coefficient_branch(job, labels):
    table = job["coefficients"]
    alpha = [complex(*z) for z in table["alpha_common"]]
    phi = table["phi_common_raw"]
    for i, label in enumerate(labels):
        phi += table["phi_unary"][i][label]
        for m in range(7):
            alpha[m] += complex(*table["alpha"][m][i][label])
    for pair in table["phi_pair"]:
        i, j = pair["ions_zero_based"]
        phi += pair["values"][labels[i]][labels[j]]
    return alpha, phi


def overlap(alpha, phi, anchor_alpha, anchor_phi, weights):
    r = math.fsum(w * abs(a - b) ** 2 for w, a, b in zip(weights, alpha, anchor_alpha))
    phase = phi - anchor_phi + math.fsum((b.conjugate() * a).imag for a, b in zip(alpha, anchor_alpha))
    value = cmath.exp(complex(-r, phase))
    return value, r, phase


def analytic_fixtures():
    # A resonant constant force: zero geometric phase and linear displacement.
    resonant, resonant_phase = independent_segment(0.0, 0.0, 2.0, 0.25)
    # Four quarter-arcs form one closed circle: delta=1, u=1/4, T=2*pi.
    circle, circle_phase = 0j, 0.0
    for k in range(4):
        step, phase = independent_segment(1.0, k * math.pi / 2.0, math.pi / 2.0, 0.25)
        circle_phase += phase + (step * circle.conjugate()).imag
        circle += step
    gaussian, _, _ = overlap([1 + 0j], 0.0, [0j], 0.0, [0.5])
    weyl, _, _ = overlap([0.25j], 0.0, [0.5 + 0j], 0.0, [0.5])
    expected_weyl = math.exp(-5.0 / 32.0) * complex(math.cos(1.0 / 8.0), math.sin(1.0 / 8.0))
    checks = {
        "resonant_displacement_error": abs(resonant + 0.5j),
        "resonant_phase_error": abs(resonant_phase),
        "circle_closure_error": abs(circle),
        "circle_phase_error": abs(circle_phase - math.pi / 8.0),
        "vacuum_gaussian_error": abs(gaussian - math.exp(-0.5)),
        "weyl_sign_and_gaussian_error": abs(weyl - expected_weyl),
    }
    return {"errors": checks, "tolerance": 1e-12,
            "passed": all(math.isfinite(e) and e <= 1e-12 for e in checks.values())}


def independent_validation(model):
    analytic = analytic_fixtures()
    result = {"phase_absolute_tolerance": PHASE_TOL, "alpha_absolute_tolerance": ALPHA_TOL,
              "analytic_fixtures": analytic, "jobs": [], "passed": analytic["passed"]}
    branches = fixture_branches()
    for job in model["jobs"]:
        eta, schedule = direct_schedule(model, job)
        cache, fixtures = {}, []
        max_phase, max_alpha = 0.0, 0.0
        for name, labels in branches:
            actual_a, actual_p = direct_branch(job, eta, schedule, labels)
            cache[tuple(labels)] = (actual_a, actual_p)
            table_a, table_p = coefficient_branch(job, labels)
            ae = [abs(a - b) for a, b in zip(actual_a, table_a)]
            pe = abs(actual_p - table_p)
            max_phase, max_alpha = max(max_phase, pe), max(max_alpha, *ae)
            fixtures.append({"name": name, "labels": labels, "phase_abs_error": pe,
                             "alpha_abs_error_by_mode": ae,
                             "direct_phi_raw": actual_p, "coefficient_phi_raw": table_p,
                             "direct_alpha": [[z.real, z.imag] for z in actual_a]})
        witnesses = []
        weights = [n + 0.5 for n in job["nbar_by_mode"]]
        for a in range(5):
            for b in range(5):
                anchor = [0, 0, 0, a, b, 0, 0]
                anchor_a, anchor_p = cache[tuple(anchor)]
                for ion in (0, 5, 6):
                    for label in range(1, 5):
                        labels = anchor[:]
                        labels[ion] = label
                        key = tuple(labels)
                        if key not in cache:
                            cache[key] = direct_branch(job, eta, schedule, labels)
                        actual_a, actual_p = cache[key]
                        value, exponent, phase = overlap(actual_a, actual_p, anchor_a, anchor_p, weights)
                        witnesses.append({"source_ion_one_based": ion + 1, "source_label": label,
                            "active_labels": [a, b], "labels": labels,
                            "coherence": [value.real, value.imag], "gaussian_exponent": exponent,
                            "relative_phase_unwrapped": phase,
                            "bell_fidelity": (1.0 + value.real) / 2.0,
                            "trace_distance": abs(value - 1.0) / 2.0})
        worst = max(witnesses, key=lambda w: w["trace_distance"])
        passed = max_phase <= PHASE_TOL and max_alpha <= ALPHA_TOL
        result["passed"] = result["passed"] and passed
        result["jobs"].append({"name": job["name"], "fixtures": fixtures,
            "fixture_count": len(fixtures), "phase_abs_error_max": max_phase,
            "alpha_abs_error_max": max_alpha, "passed": passed,
            "source_bell_witness_count": len(witnesses), "source_bell_witnesses": witnesses,
            "worst_source_bell_witness": worst,
            "minimum_source_bell_fidelity": min(w["bell_fidelity"] for w in witnesses)})
    finite_tree(result)
    return result


def export_coefficients(model, path):
    jobs = model["jobs"]
    if len(jobs) != 24 or len({job["name"] for job in jobs}) != 24:
        raise ValueError("Expected 24 uniquely named model jobs")
    lines = ["24"]
    def numbers(values, count):
        if len(values) != count:
            raise ValueError("Coefficient field has wrong flattened size")
        for value in values:
            number(value, "coefficient")
        lines.append(" ".join(repr(float(value)) for value in values))
    for job in jobs:
        name = job["name"]
        if not name or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for c in name):
            raise ValueError("Invalid coefficient case name")
        table = job["coefficients"]
        lines.append(name)
        numbers([job["theta_target_rad"], table["phi_common_corrected"]], 2)
        numbers([n + 0.5 for n in job["nbar_by_mode"]], 7)
        numbers(model["modes"]["omega_rad_s"], 7)
        numbers([v for row in table["phi_unary"] for v in row], 35)
        expected_pairs = [[i, j] for i in range(7) for j in range(i + 1, 7)]
        if [pair["ions_zero_based"] for pair in table["phi_pair"]] != expected_pairs:
            raise ValueError("Pair order mismatch")
        numbers([v for pair in table["phi_pair"] for row in pair["values"] for v in row], 525)
        numbers([z[0] for z in table["alpha_common"]], 7)
        numbers([z[1] for z in table["alpha_common"]], 7)
        numbers([z[0] for mode in table["alpha"] for ion in mode for z in ion], 245)
        numbers([z[1] for mode in table["alpha"] for ion in mode for z in ion], 245)
    with Path(path).open("x", encoding="ascii", newline="\n") as handle:
        handle.write("\n".join(lines) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def compare_repeats(reference, observed):
    differences = []
    for baseline, current in zip(reference["cases"], observed["cases"]):
        if baseline["name"] != current["name"] or baseline["witness_indices"] != current["witness_indices"]:
            raise ValueError("Repeated scan names or witness indices changed")
        row = {"name": baseline["name"]}
        for key in DIAGNOSTICS:
            row[key] = abs(current[key] - baseline[key])
            if not math.isclose(current[key], baseline[key], rel_tol=REPEAT_REL_TOL, abs_tol=REPEAT_ABS_TOL):
                raise ValueError("Repeated scan diagnostic changed: " + baseline["name"] + "/" + key)
        differences.append(row)
    return differences


def terminate_child(child):
    if child is not None and child.poll() is None:
        try:
            os.killpg(child.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        child.wait(timeout=2)


def invoke(binary, coefficients, output, index, places, pins, names, reference):
    check_pins(pins)
    tag = "warmup" if index == 0 else "measured_" + str(index)
    stdout_path, stderr_path = output / "raw" / (tag + ".stdout.json"), output / "raw" / (tag + ".stderr.txt")
    command = [str(binary), "--input", str(coefficients)]
    record = {"name": tag, "phase": "warmup" if index == 0 else "measured",
              "command": command, "started_utc": utc(), "status": "FAILED",
              "stdout_file": str(stdout_path.relative_to(output)),
              "stderr_file": str(stderr_path.relative_to(output)), "timeout_seconds": TIMEOUT_SECONDS}
    started, child = time.perf_counter(), None
    try:
        with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
            original = os.sched_getaffinity(0)
            try:
                os.sched_setaffinity(0, set(places))
                child = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                    env=environment(places), start_new_session=True)
            finally:
                os.sched_setaffinity(0, original)
            try:
                child.wait(timeout=TIMEOUT_SECONDS)
            except subprocess.TimeoutExpired:
                record["timed_out"] = True
                raise RuntimeError("Scanner exceeded 55-second invocation watchdog")
        record["wall_seconds"] = time.perf_counter() - started
        record["exit_code"] = child.returncode
        if child.returncode != 0:
            raise RuntimeError("Scanner exited nonzero: " + str(child.returncode))
        if stderr_path.stat().st_size != 0:
            raise RuntimeError("Scanner wrote stderr")
        if stdout_path.stat().st_size > CAPTURE_LIMIT:
            raise RuntimeError("Scanner stdout exceeds capture limit")
        obj = parse_scanner(stdout_path.read_bytes(), names, places)
        record["result"] = obj
        if reference is not None:
            record["diagnostic_abs_differences_from_warmup"] = compare_repeats(reference, obj)
        check_pins(pins)
        record["status"] = "PASS"
        return record
    except BaseException as exc:
        record["error"] = type(exc).__name__ + ": " + str(exc)
        terminate_child(child)
        if child is not None:
            record["exit_code"] = child.returncode
        raise
    finally:
        record.setdefault("wall_seconds", time.perf_counter() - started)
        record["invocation_with_custody_seconds"] = time.perf_counter() - started
        record["finished_utc"] = utc()
        pin_error = None
        try:
            check_pins(pins)
            record["pins_unchanged_after"] = True
        except Exception as exc:
            pin_error = exc
            record["pins_unchanged_after"] = False
            record["pin_error"] = str(exc)
            record["status"] = "FAILED"
        for label, path in (("stdout", stdout_path), ("stderr", stderr_path)):
            if path.exists():
                record[label] = artifact(path)
        write_json(output / "raw" / (tag + ".record.json"), record)
        if pin_error is not None:
            raise pin_error


def classification(model, validation, scanner):
    validations = {job["name"]: job for job in validation["jobs"]}
    scanned = {case["name"]: case for case in scanner["cases"]}
    requirements, jobs, consistency = [], [], []
    for job in model["jobs"]:
        actual = scanned[job["name"]]
        witness = validations[job["name"]]["worst_source_bell_witness"]
        consistency.append({"name": job["name"], "direct_Bell_trace_distance": witness["trace_distance"],
                            "scanner_source_bound": actual["source_bound"], "numerical_slack": 1e-7,
                            "passed": witness["trace_distance"] <= actual["source_bound"] + 1e-7})
        jobs.append({"name": job["name"], "context": job["context"], "arm": job["arm"],
                     "sign": job["sign"], "scanner": actual,
                     "worst_source_bell_witness": witness,
                     "scope": "numerical_estimates_in_declared_harmonic_model"})
        if job["context"] != "nominal":
            continue
        if job["arm"] == "G":
            requirements.extend([
                {"name": job["name"] + "/gate", "observed": actual["gate_bound"],
                 "comparison": "<=", "threshold": 1e-6, "passed": actual["gate_bound"] <= 1e-6},
                {"name": job["name"] + "/source", "observed": actual["source_bound"],
                 "comparison": "<=", "threshold": 1e-8, "passed": actual["source_bound"] <= 1e-8}])
        elif job["arm"] == "I":
            requirements.extend([
                {"name": job["name"] + "/" + key, "observed": actual[key],
                 "comparison": "<=", "threshold": 1e-10, "passed": actual[key] <= 1e-10}
                for key in ("gate_bound", "source_bound")])
        else:
            observed = witness["trace_distance"]
            requirements.append({"name": job["name"] + "/exposed_source_Bell", "observed": observed,
                 "comparison": ">", "threshold": 1e-6, "passed": observed > 1e-6})
    efficacy_passed = all(row["passed"] for row in requirements)
    consistency_passed = all(row["passed"] for row in consistency)
    status = "MODEL_WAVEFORM_CHECK" if efficacy_passed else "MODEL_CONSTRAINTS_NOT_MET"
    if not consistency_passed:
        status = "NUMERICAL_CONSISTENCY_FAILED"
    return {"status": status, "acceptance_passed": efficacy_passed and consistency_passed,
            "nominal_requirements_passed": efficacy_passed, "requirements": requirements, "jobs": jobs,
            "consistency_gate": {"passed": consistency_passed, "checks": consistency,
                "violations": [row for row in consistency if not row["passed"]],
                "scope": "Direct Bell witness versus computed source bound; numerical consistency only, not a new efficacy threshold"},
            "scope": "Floating estimates, not interval proofs or physical apparatus admission",
            "stress_context_policy": "Report all values; no universal-pass requirement or post-run retuning"}


def interruption(signum, frame):
    raise KeyboardInterrupt("Signal " + str(signum))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="New campaign directory")
    args = parser.parse_args()
    if not args.binary.is_absolute() or not args.binary.is_file():
        parser.error("--binary must be an existing absolute file path")
    args.binary = args.binary.resolve()
    args.output = args.output.resolve()
    if args.output.exists():
        parser.error("--output must not exist")
    if not args.output.parent.is_dir():
        parser.error("--output parent directory must already exist")
    started, start_utc = time.perf_counter(), utc()
    args.output.mkdir()
    (args.output / "raw").mkdir()
    signal.signal(signal.SIGTERM, interruption)
    signal.signal(signal.SIGINT, interruption)
    try:
        rows, places, allowed = topology()
        source_dir = Path(__file__).resolve().parent
        required = [source_dir / name for name in ("model_builder.py", "numerical_run.py", "waveform_scan.cpp", "SOURCE_SHA256SUMS")]
        if any(not path.is_file() for path in required):
            raise RuntimeError("Required source file absent from runner directory")
        sources = sorted(path for path in source_dir.iterdir() if path.is_file() and
                         (path.suffix in (".py", ".cpp", ".md") or path.name == "SOURCE_SHA256SUMS"))
        pins = {str(path.resolve()): sha256(path) for path in sources + [args.binary]}
        env = environment(places)
        metadata = {"started_utc": start_utc, "scope": "waveform_derived_harmonic_model_only",
            "python": sys.version, "platform": platform.platform(), "architecture": platform.machine(),
            "allowed_cpus": sorted(allowed), "topology": rows, "requested_places": places,
            "source_and_binary_hashes": pins, "selection": "avx512_80_fixed_from_prior_synthetic_pilot",
            "environment": {key: value for key, value in env.items() if key.startswith("OMP_") or
                key in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
                        "NUMEXPR_NUM_THREADS", "MKL_DYNAMIC", "LC_ALL")},
            "warmup_invocations": 1, "measured_invocations": 5,
            "per_invocation_timeout_seconds": TIMEOUT_SECONDS,
            "repeat_absolute_tolerance": REPEAT_ABS_TOL, "repeat_relative_tolerance": REPEAT_REL_TOL}
        write_json(args.output / "metadata.json", metadata)
        check_pins(pins)
        spec = importlib.util.spec_from_file_location("pinned_waveform_model_builder", source_dir / "model_builder.py")
        if spec is None or spec.loader is None:
            raise RuntimeError("Cannot load pinned model source")
        model_builder = importlib.util.module_from_spec(spec)
        builder_path = source_dir / "model_builder.py"
        builder_bytes = builder_path.read_bytes()
        if hashlib.sha256(builder_bytes).hexdigest() != pins[str(builder_path.resolve())]:
            raise RuntimeError("Model source changed before loading")
        # Execute the pinned source bytes, never a potentially stale .pyc cache.
        exec(compile(builder_bytes, str(builder_path), "exec"), model_builder.__dict__)
        check_pins(pins)
        build_started = time.perf_counter()
        model = model_builder.build_model()
        model_seconds = time.perf_counter() - build_started
        write_json(args.output / "model.json", model)
        check_pins(pins)
        if model.get("status") != "MODEL_BUILT_NOT_VALIDATED":
            result = {"status": "INCOMPLETE", "reason": model.get("reason", "Builder did not complete"),
                      "model": artifact(args.output / "model.json"), "model_build_seconds": model_seconds,
                      "end_to_end_seconds": time.perf_counter() - started, "finished_utc": utc()}
            write_json(args.output / "result.json", result)
            print(json.dumps(result, sort_keys=True, allow_nan=False))
            return 2
        validation_started = time.perf_counter()
        validation = independent_validation(model)
        validation_seconds = time.perf_counter() - validation_started
        write_json(args.output / "independent_validation.json", validation)
        check_pins(pins)
        if not validation["passed"]:
            raise RuntimeError("Independent chronological integration or analytic fixture failed")
        coefficients = args.output / "coefficients.txt"
        export_coefficients(model, coefficients)
        pins.update({str(coefficients): sha256(coefficients),
                     str(args.output / "model.json"): sha256(args.output / "model.json"),
                     str(args.output / "independent_validation.json"): sha256(args.output / "independent_validation.json")})
        write_json(args.output / "campaign_pins.json", pins)
        samples, reference = [], None
        names = [job["name"] for job in model["jobs"]]
        for index in range(6):
            sample = invoke(args.binary, coefficients, args.output, index, places, pins, names, reference)
            if reference is None:
                reference = sample["result"]
            samples.append(sample)
        result = classification(model, validation, reference)
        kernels = [sample["result"]["kernel_seconds"] for sample in samples[1:]]
        walls = [sample["wall_seconds"] for sample in samples[1:]]
        result.update({"model_build_seconds": model_seconds,
            "independent_validation_seconds": validation_seconds,
            "kernel_seconds_measured": kernels, "kernel_median_seconds": statistics.median(kernels),
            "kernel_min_seconds": min(kernels), "kernel_max_seconds": max(kernels),
            "subprocess_wall_seconds_measured": walls, "subprocess_wall_median_seconds": statistics.median(walls),
            "all_six_invocations": [{"name": sample["name"], "wall_seconds": sample["wall_seconds"],
                "kernel_seconds": sample["result"]["kernel_seconds"],
                "validation_seconds": sample["result"]["validation_seconds"],
                "max_abs_error": sample["result"]["max_abs_error"],
                "stdout": sample["stdout"], "stderr": sample["stderr"]} for sample in samples],
            "branches_per_scanner_pass": BRANCHES, "independent_fixture_count": 24 * 69,
            "direct_source_Bell_witness_count": 24 * 300,
            "artifacts": {name: artifact(args.output / name) for name in
                ("metadata.json", "model.json", "independent_validation.json", "coefficients.txt", "campaign_pins.json")}})
        check_pins(pins)
        result["end_to_end_seconds"] = time.perf_counter() - started
        result["finished_utc"] = utc()
        write_json(args.output / "result.json", result)
        print(json.dumps({"status": result["status"], "kernel_median_seconds": result["kernel_median_seconds"],
              "end_to_end_seconds": result["end_to_end_seconds"], "result": str(args.output / "result.json")},
              sort_keys=True, allow_nan=False))
        if not result["consistency_gate"]["passed"]:
            return 4
        return 0 if result["acceptance_passed"] else 3
    except BaseException as exc:
        failure = {"status": "FAILED", "error": type(exc).__name__ + ": " + str(exc),
                   "started_utc": start_utc, "finished_utc": utc(),
                   "end_to_end_seconds": time.perf_counter() - started,
                   "scope": "Campaign did not complete; preserve all existing outputs"}
        write_json(args.output / "failure.json", failure)
        print(json.dumps(failure, sort_keys=True, allow_nan=False), file=sys.stderr)
        return 130 if isinstance(exc, KeyboardInterrupt) else 1


if __name__ == "__main__":
    raise SystemExit(main())
