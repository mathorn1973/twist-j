#!/usr/bin/env python3
"""Frozen floating trajectory campaign; no execution on import.

PUBLIC NON-CANONICAL. Conditional model estimates, not interval certificates.
Original code Apache-2.0, A. M. Thorn. Custody/topology patterns are credited
reuse from P-U-CA40-WAVEFORM-SOURCE-1; the independent two-frequency oracle
and this fixed campaign are newly implemented. No waveform is constructed,
optimized, selected or retried here. Run only after immutable public pin.
"""

import argparse
import cmath
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import signal
import statistics
import subprocess
import sys
import time


SOURCE_NAMES = {"README.md", "PREREG.md", "DERIVATION.md", "EXACT-DESIGN.md",
                "input.json", "verify.py", "trajectory.cpp", "numerical_run.py"}
INTERIOR = ((0, 1/512), (0, 511/512), (15, 255/512), (16, 1/512),
            (39, 257/512), (40, 1/512), (64, 255/512), (79, 511/512))
METRICS = ("alpha_rwa_sample", "alpha_linear_sample", "alpha_difference_sample",
           "alpha_rwa_envelope", "alpha_linear_envelope", "alpha_difference_envelope",
           "ld_rms_sample", "ld_rms_envelope", "adjacent_rms_sample", "adjacent_rms_envelope",
           "adjacent_coherent_sample", "adjacent_coherent_envelope")
LD_FIELDS = ("ld_duhamel_uncapped", "ld_midpoint_integral", "ld_quartic_envelope",
             "ld_lipschitz_allowance", "ld_envelope_gap")
CHILD_TIMEOUT = 180
CAMPAIGN_TIMEOUT = 1800


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def artifact(path):
    return {"sha256": digest(path), "bytes": Path(path).stat().st_size}


def write_json(path, obj):
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(obj, stream, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())


def duplicates(items):
    out = {}
    for key, value in items:
        require(key not in out, "Duplicate JSON key: " + key)
        out[key] = value
    return out


def bad_constant(value):
    raise ValueError("Nonfinite JSON constant: " + value)


def finite_tree(value):
    if isinstance(value, float):
        require(math.isfinite(value), "Nonfinite JSON number")
    elif isinstance(value, list):
        for child in value:
            finite_tree(child)
    elif isinstance(value, dict):
        for child in value.values():
            finite_tree(child)


def load_json_bytes(raw):
    value = json.loads(raw.decode("utf-8"), object_pairs_hook=duplicates,
                       parse_constant=bad_constant)
    finite_tree(value)
    return value


def number(value, label, lo=None, hi=None):
    require(type(value) in (float, int) and math.isfinite(value), "Invalid number: " + label)
    require((lo is None or value >= lo) and (hi is None or value <= hi),
            "Out-of-range number: " + label)
    return value


def source_pins(source, binary):
    manifest = source / "SOURCE_SHA256SUMS"
    rows = manifest.read_text(encoding="ascii").splitlines()
    pins = {}
    for row in rows:
        parts = row.split()
        require(len(parts) == 2, "Malformed source manifest")
        expected, name = parts
        require(name in SOURCE_NAMES and name not in pins, "Unexpected/duplicate source name")
        require(len(expected) == 64 and all(c in "0123456789abcdef" for c in expected),
                "Invalid manifest SHA256")
        pins[name] = expected
    require(set(pins) == SOURCE_NAMES, "Incomplete source manifest")
    paths = {str(source/name): value for name, value in pins.items()}
    paths[str(manifest)] = digest(manifest)
    paths[str(binary)] = digest(binary)
    check_pins(paths)
    return paths


def check_pins(pins):
    for path, expected in pins.items():
        require(digest(path) == expected, "Pinned file changed: " + path)


def cpu_list(text):
    found = set()
    for part in text.strip().split(","):
        ends = part.split("-")
        require(1 <= len(ends) <= 2 and all(s.isdecimal() for s in ends), "CPU list syntax")
        lo, hi = int(ends[0]), int(ends[-1])
        require(hi >= lo, "CPU range reversed")
        values = set(range(lo, hi+1))
        require(not values & found, "Duplicate CPU range")
        found.update(values)
    return found


def topology():
    require(sys.platform == "linux" and hasattr(os, "sched_getaffinity"), "Linux affinity required")
    allowed = set(os.sched_getaffinity(0))
    require(len(allowed) == 80, "Exactly 80 allowed logical CPUs required")
    rows, cores = [], {}
    for cpu in sorted(allowed):
        root = Path("/sys/devices/system/cpu") / ("cpu" + str(cpu))
        top = root / "topology"
        package = int((top/"physical_package_id").read_text().strip())
        core = int((top/"core_id").read_text().strip())
        siblings = cpu_list((top/"thread_siblings_list").read_text())
        nodes = [int(p.name[4:]) for p in root.glob("node[0-9]*") if p.name[4:].isdecimal()]
        require(len(nodes) == 1, "Exactly one NUMA node per CPU required")
        row = dict(cpu=cpu, package=package, core=core, node=nodes[0], siblings=sorted(siblings))
        rows.append(row)
        cores.setdefault((package, core), []).append(row)
    packages = {row["package"] for row in rows}
    nodes = {row["node"] for row in rows}
    require(len(cores) == 40 and len(packages) == len(nodes) == 2, "Frozen 40-core/two-node topology")
    for package in packages:
        require(sum(key[0] == package for key in cores) == 20, "20 cores per package required")
    for group in cores.values():
        cpus = {row["cpu"] for row in group}
        require(len(group) == 2 and len({row["node"] for row in group}) == 1, "Complete SMT pairs required")
        require(all(set(row["siblings"]) == cpus for row in group), "Partial SMT affinity")
    by_node = {node: sorted(min(row["cpu"] for row in group)
                    for group in cores.values() if group[0]["node"] == node) for node in sorted(nodes)}
    require(all(len(values) == 20 for values in by_node.values()), "20 cores per NUMA node required")
    first = [cpu for pair in zip(*by_node.values()) for cpu in pair]
    lookup = {row["cpu"]: row for row in rows}
    places = first + [next(c for c in lookup[cpu]["siblings"] if c != cpu) for cpu in first]
    require(len(set(places)) == 80 and set(places) == allowed, "Invalid explicit places")
    return rows, places


def environment(places):
    env = {k: v for k, v in os.environ.items() if not k.startswith(("OMP_", "GOMP_", "KMP_"))}
    overrides = dict(OMP_NUM_THREADS="80", OMP_THREAD_LIMIT="80",
        OMP_PLACES=",".join("{"+str(cpu)+"}" for cpu in places), OMP_PROC_BIND="true",
        OMP_DYNAMIC="FALSE", OMP_MAX_ACTIVE_LEVELS="1", OPENBLAS_NUM_THREADS="1",
        MKL_NUM_THREADS="1", BLIS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1",
        NUMEXPR_NUM_THREADS="1", MKL_DYNAMIC="FALSE", LC_ALL="C")
    env.update(overrides)
    return env, overrides


def prepare_model(data):
    require(data.get("schema") == "CA40_FIXED_WAVEFORM_VALIDITY_INPUT_V1", "Input schema")
    cfg, modes, pulses = data["config"], data["modes"], data["pulses"]
    require(cfg["ions"] == 7 and cfg["cycles"] == 5 and cfg["segments"] == 16, "Frozen dimensions")
    require(cfg["loop_seconds"] == 1e-4 and cfg["nbar"] == 0.05, "Frozen duration/thermal occupation")
    omega, position, vectors = modes["omega_rad_s"], modes["positions_m"], modes["vectors_by_mode"]
    require(len(omega) == len(position) == len(vectors) == 7, "Seven modes/ions required")
    require(all(len(row) == 7 for row in vectors), "Mode vector shape")
    require(all(omega[m] > 0 for m in range(7)) and all(position[i+1] > position[i] for i in range(6)),
            "Mode/position order")
    k = 2*math.pi/cfg["wavelength_m"]
    kappa = [[k*vectors[m][i]*math.sqrt(cfg["hbar_Js"]/(2*cfg["mass_kg"]*omega[m]))
              for i in range(7)] for m in range(7)]
    eta_raw = modes["eta_by_mode_ion"]
    require(len(eta_raw) == 7 and all(len(row) == 7 for row in eta_raw), "Eta shape")
    require(all(len(z) == 2 for row in eta_raw for z in row), "Complex eta shape")
    eta = [[complex(*eta_raw[m][i]) for i in range(7)] for m in range(7)]
    require(all(abs(eta[m][i]-kappa[m][i]*cmath.exp(1j*k*position[i])) <= 1e-12
                for m in range(7) for i in range(7)), "Eta/kappa phase relation")
    require(len(pulses) == 2 and [p["sign"] for p in pulses] == [1, -1], "Pulse order")
    for pulse in pulses:
        require(len(pulse["amplitudes_rad_s"]) == 16 and pulse["loop_seconds"] == 1e-4,
                "Frozen pulse shape")
        require(abs(pulse["theta_rad"]-pulse["sign"]*4*math.pi/5) <= 1e-14, "Target angle")
    return dict(mu=2*math.pi*(cfg["axial_hz"]+cfg["beatnote_offset_hz"]), k=k,
                tau=cfg["loop_seconds"], dt=cfg["loop_seconds"]/16, nbar=cfg["nbar"],
                omega=omega, position=position, kappa=kappa, eta=eta, pulses=pulses)


def integral_exp(frequency, duration):
    if frequency == 0:
        return complex(duration, 0)
    angle = frequency*duration
    return complex(math.sin(angle), 2*math.sin(angle/2)**2)/frequency


def ordered_integral(a, b, duration):
    """Generic ordered triangle; no C++ diagonal-plus-mixed decomposition."""
    if b != 0:
        return (integral_exp(a, duration)-integral_exp(a-b, duration))/(1j*b)
    if a == 0:
        return complex(duration*duration/2, 0)
    if abs(a*duration) < 0.25:
        term, total = 1+0j, 0j
        for n in range(32):
            total += term*duration*duration/(n+2)
            term *= 1j*a*duration/(n+1)
        return total
    exponential = cmath.exp(1j*a*duration)
    return duration*exponential/(1j*a)+(exponential-1)/(a*a)


def zero_state():
    return {"r": [0j]*7, "l": [0j]*7, "pr": 0.0, "pl": 0.0, "unary": 0.0}


def advance(model, old, case, segment, duration):
    start = segment*model["dt"]
    cycle = segment//16
    left, right = divmod(case % 25, 5)
    responses = (int((left+cycle) % 5 == 0), int((right+cycle) % 5 == 0))
    u = model["pulses"][case//25]["amplitudes_rad_s"][segment % 16]
    out = {"r": list(old["r"]), "l": list(old["l"]),
           "pr": old["pr"], "pl": old["pl"], "unary": old["unary"]}
    for m in range(7):
        g = sum(model["eta"][m][i+3]*responses[i] for i in range(2))
        frequencies = (model["omega"][m]-model["mu"], model["omega"][m]+model["mu"])
        coefficients = (u*g, u*g.conjugate())
        amplitudes = [coefficient*cmath.exp(1j*frequency*start)
                      for coefficient, frequency in zip(coefficients, frequencies)]
        for field, phase_field, count in (("r", "pr", 1), ("l", "pl", 2)):
            beta = -1j*sum(amplitudes[p]*integral_exp(frequencies[p], duration) for p in range(count))
            area = sum(amplitudes[p]*amplitudes[q].conjugate()
                       * ordered_integral(frequencies[p], frequencies[q], duration)
                       for p in range(count) for q in range(count)).imag
            out[phase_field] += area + (beta*old[field][m].conjugate()).imag
            out[field][m] += beta
    half_angle = model["mu"]*duration/2
    sinc = math.sin(half_angle)/half_angle if half_angle else 1.0
    out["unary"] -= 2*u*duration*sinc*sum(responses[j]*math.sin(
         model["k"]*model["position"][j+3]-model["mu"]*(start+duration/2)) for j in range(2))
    return out


def fixture_row(case, segment, fraction, state):
    values = [state["pr"], state["pl"], state["unary"]]
    values += [v for field in ("r", "l") for z in state[field] for v in (z.real, z.imag)]
    require(all(math.isfinite(x) for x in values), "Nonfinite independent fixture")
    return [case, segment, fraction] + values


def build_fixtures(model):
    fixtures = []
    for case in range(50):
        prefixes = [zero_state()]
        for segment in range(80):
            prefixes.append(advance(model, prefixes[-1], case, segment, model["dt"]))
        fixtures.extend(fixture_row(case, boundary, 0.0, prefixes[boundary]) for boundary in range(81))
        for segment, fraction in INTERIOR:
            state = advance(model, prefixes[segment], case, segment, model["dt"]*fraction)
            fixtures.append(fixture_row(case, segment, fraction, state))
    require(len(fixtures) == 4450 and len({tuple(row[:3]) for row in fixtures}) == 4450,
            "Independent fixture coverage")
    return fixtures


def serialize_input(path, model, fixtures):
    lines = ["256", " ".join(format(model[k], ".17g") for k in ("mu", "k", "tau", "nbar"))]
    lines.extend(" ".join(format(x, ".17g") for x in model[key]) for key in ("omega", "position"))
    for matrix in (model["kappa"], [[z.real for z in row] for row in model["eta"]],
                   [[z.imag for z in row] for row in model["eta"]]):
        lines.extend(" ".join(format(x, ".17g") for x in row) for row in matrix)
    for pulse in model["pulses"]:
        lines.append(" ".join(format(x, ".17g") for x in [pulse["theta_rad"]]+pulse["amplitudes_rad_s"]))
    lines.append(str(len(fixtures)))
    lines.extend(" ".join(str(x) if type(x) is int else format(x, ".17g") for x in row) for row in fixtures)
    with path.open("x", encoding="ascii", newline="\n") as stream:
        stream.write("\n".join(lines)+"\n")
        stream.flush()
        os.fsync(stream.fileno())


def map_check(mapping, places, label):
    require(type(mapping) is list and len(mapping) == 80, label + " size")
    tids, cpus, pids = set(), set(), set()
    for row in mapping:
        require(type(row) is dict and all(type(row.get(k)) is int for k in ("thread", "cpu", "place")),
                label + " row")
        tid, cpu, place = row["thread"], row["cpu"], row["place"]
        require(0 <= tid < 80 and 0 <= place < 80 and cpu == places[place], label + " placement")
        require(tid not in tids and cpu not in cpus and place not in pids, label + " duplicate")
        tids.add(tid); cpus.add(cpu); pids.add(place)
    require(tids == pids == set(range(80)) and cpus == set(places), label + " coverage")


def parse_scanner(raw, places):
    obj = load_json_bytes(raw)
    require(type(obj) is dict and obj.get("status") == "PASS" and obj.get("backend") == "avx512",
            "Scanner status/backend")
    for field, value in {"threads": 80, "nsub": 256, "cases": 50, "tasks": 4000,
                         "midpoints_per_model": 1024000, "oracle_fixtures": 4450}.items():
        require(type(obj.get(field)) is int and obj[field] == value, "Scanner dimension: " + field)
    number(obj.get("oracle_alpha_error"), "oracle_alpha_error", 0, 1e-9)
    number(obj.get("oracle_phase_error"), "oracle_phase_error", 0, 1e-8)
    number(obj.get("scalar_simd_error"), "scalar_simd_error", 0)
    for field in ("preparation_seconds", "scalar_seconds", "kernel_seconds"):
        number(obj.get(field), field, 1e-12)
    for field in ("thread_map", "scalar_thread_map"):
        map_check(obj.get(field), places, field)
    require(len(obj.get("initial_thermal_rms_by_ion", [])) == 7, "Thermal RMS size")
    for value in obj["initial_thermal_rms_by_ion"]:
        number(value, "initial thermal RMS", 0)
    branches = obj.get("branches")
    require(type(branches) is list and len(branches) == 50, "Branch count")
    for case, branch in enumerate(branches):
        require(branch.get("case") == case and branch.get("sign") == (1 if case < 25 else -1)
                and branch.get("active_labels") == [(case % 25)//5, case % 5], "Branch order")
        for field in METRICS+LD_FIELDS:
            number(branch.get(field), field, 0)
        witnesses = branch.get("witness_cells")
        require(type(witnesses) is list and len(witnesses) == len(METRICS) and
                all(type(x) is int and 0 <= x < 80*256 for x in witnesses), "Witness cell indices")
    comparisons = obj.get("comparisons")
    require(type(comparisons) is list and len(comparisons) == 2, "Comparison count")
    for index, row in enumerate(comparisons):
        require(row.get("sign") == (1 if index == 0 else -1), "Comparison order")
        for key in ("rwa_linear_raw_bound", "rwa_linear_optimized_bound", "bell_trace_distance_max",
                    "rwa_linear_continuous_anchor_bound"):
            number(row.get(key), key, 0, 1)
        for key in ("rwa_ideal_phase_error", "rwa_endpoint_alpha_max", "linear_endpoint_alpha_max",
                    "unary_branch_spread", "rwa_continuous_phase_envelope", "rwa_continuous_r_envelope"):
            number(row.get(key), key, 0)
        for key in ("common_phase_gamma", "uncompensated_unary_phase"):
            number(row.get(key), key)
        for key in ("raw_phase_differences", "displacement_exponents"):
            require(type(row.get(key)) is list and len(row[key]) == 25, key + " shape")
            for value in row[key]:
                number(value, key, 0 if key == "displacement_exponents" else None)
        pair = row.get("bell_pair")
        require(type(pair) is list and len(pair) == 2 and all(type(z) is int for z in pair)
                and 0 <= pair[0] < pair[1] < 25, "Bell pair")
        continuous_witness = row.get("rwa_continuous_witness")
        require(type(continuous_witness) is list and len(continuous_witness) == 2
                and all(type(z) is int for z in continuous_witness)
                and 25*index <= continuous_witness[0] < 25*(index+1)
                and 0 <= continuous_witness[1] < 80, "Continuous RWA witness")
        require(row["bell_trace_distance_max"] <= row["rwa_linear_optimized_bound"]+1e-7,
                "Bell lower witness exceeds comparison upper estimate")
        require(row["rwa_ideal_phase_error"] <= 1e-8 and row["rwa_endpoint_alpha_max"] <= 1e-9
                and row["unary_branch_spread"] <= 1e-8, "Prior endpoint/unary consistency")
    return obj


def diagnostic_tree(obj):
    return {key: value for key, value in obj.items()
            if key not in ("preparation_seconds", "scalar_seconds", "kernel_seconds")}


def compare_repeat(actual, expected, path="diagnostic"):
    require(type(actual) is type(expected), "Repeat type mismatch at " + path)
    if type(actual) is float:
        require(math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12), "Repeat value at " + path)
    elif type(actual) is dict:
        require(set(actual) == set(expected), "Repeat keys at " + path)
        for key in actual:
            compare_repeat(actual[key], expected[key], path+"/"+key)
    elif type(actual) is list:
        require(len(actual) == len(expected), "Repeat length at " + path)
        for index, value in enumerate(actual):
            compare_repeat(value, expected[index], path+"/"+str(index))
    else:
        require(actual == expected, "Repeat exact value at " + path)


def run_child(binary, input_path, output, name, env):
    stdout_path, stderr_path = output/(name+".stdout"), output/(name+".stderr")
    record = {"name": name, "command": [str(binary), "--input", str(input_path)],
              "started_utc": utc(), "timeout_seconds": CHILD_TIMEOUT, "timed_out": False}
    process = None
    error = None
    with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
        started = time.perf_counter()
        try:
            process = subprocess.Popen(record["command"], stdout=stdout, stderr=stderr,
                                       env=env, start_new_session=True)
            try:
                record["exit_code"] = process.wait(timeout=CHILD_TIMEOUT)
            except subprocess.TimeoutExpired:
                record["timed_out"] = True
                raise TimeoutError("Scanner exceeded frozen 180-second watchdog")
        except BaseException as exc:
            error = exc
            record["exception"] = type(exc).__name__ + ": " + str(exc)
            if process is not None and process.poll() is None:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                except BaseException as kill_error:
                    record["kill_error"] = type(kill_error).__name__ + ": " + str(kill_error)
                try:
                    process.wait(timeout=2)
                except BaseException as reap_error:
                    record["reap_error"] = type(reap_error).__name__ + ": " + str(reap_error)
            record["exit_code"] = None if process is None else process.returncode
        finally:
            record["subprocess_wall_seconds"] = time.perf_counter()-started
            record["finished_utc"] = utc()
            stdout.flush(); stderr.flush()
            os.fsync(stdout.fileno()); os.fsync(stderr.fileno())
    # Preserve the completed/timeout process BEFORE parse, custody or scientific checks.
    record["stdout"], record["stderr"] = artifact(stdout_path), artifact(stderr_path)
    write_json(output/(name+".record.json"), record)
    if error is not None:
        raise error
    require(record["exit_code"] == 0 and record["stderr"]["bytes"] == 0, "Scanner failed: " + name)
    return record, stdout_path.read_bytes()


def classify(obj):
    rows = []
    for index, comparison in enumerate(obj["comparisons"]):
        branches = obj["branches"][25*index:25*(index+1)]
        rwa = comparison["rwa_linear_optimized_bound"]
        witness = comparison["bell_trace_distance_max"]
        ld = max(row["ld_duhamel_uncapped"] for row in branches)
        rms = max(row["ld_rms_envelope"] for row in branches)
        rwa_status = ("NUMERICAL_SCREEN_PASS" if rwa <= 1e-3 else
                      "NUMERICAL_WITNESS_VIOLATION" if witness > 1e-3 else "NOT_CERTIFIED_BY_THIS_BOUND")
        rows.append({"sign": comparison["sign"], "rwa_upper_estimate": rwa,
            "rwa_threshold": 1e-3, "rwa_witness": witness, "rwa_status": rwa_status,
            "rwa_screen_time_scope": "endpoint only",
            "rwa_continuous_anchor_bound_diagnostic": comparison["rwa_linear_continuous_anchor_bound"],
            "rwa_continuous_phase_envelope_diagnostic": comparison["rwa_continuous_phase_envelope"],
            "rwa_continuous_r_envelope_diagnostic": comparison["rwa_continuous_r_envelope"],
            "ld_uncapped_upper_estimate": ld, "ld_threshold": 1e-2,
            "ld_screen_time_scope": "full interval",
            "ld_status": "NUMERICAL_SCREEN_PASS" if ld <= 1e-2 else "NOT_CERTIFIED_BY_THIS_BOUND",
            "rms_upper_estimate": rms, "rms_threshold": 0.1,
            "rms_heuristic_passed": rms <= 0.1,
            "combined_uncapped_upper_estimate": ld+rwa})
    return rows


def interrupted(signum, frame):
    raise TimeoutError("Campaign watchdog expired") if signum == signal.SIGALRM else KeyboardInterrupt(
        "Campaign interrupted by signal " + str(signum))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    binary, output = Path(args.binary), Path(args.output)
    require(binary.is_absolute() and output.is_absolute(), "Absolute binary/output paths required")
    binary, output = binary.resolve(strict=True), output.resolve()
    source = Path(__file__).resolve().parent
    require(binary.is_file(), "Binary must be a file")
    require(source != output and source not in output.parents, "Output must be outside the source directory")
    output.mkdir(parents=False, exist_ok=False)
    started, begun = time.perf_counter(), utc()
    receipts = []
    pins = None
    old_handlers = {}
    try:
        require(sys.platform == "linux", "Frozen Linux execution required")
        for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGALRM):
            old_handlers[sig] = signal.signal(sig, interrupted)
        signal.setitimer(signal.ITIMER_REAL, CAMPAIGN_TIMEOUT)
        pins = source_pins(source, binary)
        write_json(output/"source-pins.json", pins)
        rows, places = topology()
        env, overrides = environment(places)
        write_json(output/"metadata.json", {"started_utc": begun, "python": platform.python_version(),
            "platform": platform.platform(), "architecture": platform.machine(), "topology": rows,
            "places": places, "environment_overrides": overrides, "sources_and_binary": pins,
            "command": sys.argv, "watchdog_seconds": CAMPAIGN_TIMEOUT,
            "invocations": ["warmup", "measured_1", "measured_2", "measured_3"],
            "scope": "Private operational custody; sanitize before public reporting"})
        preparation_started = time.perf_counter()
        data = load_json_bytes((source/"input.json").read_bytes())
        model = prepare_model(data)
        fixtures = build_fixtures(model)
        write_json(output/"independent-fixtures.json", {"count": len(fixtures), "interior": INTERIOR,
             "fields": ["case", "segment", "fraction", "pr", "pl", "unary", "r[7].re/im", "l[7].re/im"],
             "fixtures": fixtures, "method": "generic ordered two-frequency triangle with absolute clock"})
        input_path = output/"input.txt"
        serialize_input(input_path, model, fixtures)
        pins[str(input_path)] = digest(input_path)
        write_json(output/"execution-pins.json", pins)
        preparation_seconds = time.perf_counter()-preparation_started
        baseline = None
        for name in ("warmup", "measured_1", "measured_2", "measured_3"):
            check_pins(pins)
            record, raw = run_child(binary, input_path, output, name, env)
            receipts.append(record)
            check_pins(pins)
            parsed = parse_scanner(raw, places)
            diagnostic = diagnostic_tree(parsed)
            if baseline is None:
                baseline = diagnostic
                write_json(output/"baseline.json", baseline)
            else:
                compare_repeat(diagnostic, baseline)
            record["kernel_seconds"] = parsed["kernel_seconds"]
            record["scalar_seconds"] = parsed["scalar_seconds"]
            record["preparation_seconds"] = parsed["preparation_seconds"]
            write_json(output/(name+".validated.json"), record)
        check_pins(pins)
        # The first retained outcome is the reference, not a favorable later invocation.
        decisions = classify(baseline)
        measured = receipts[1:]
        result = {"status": "NUMERICAL_CAMPAIGN_COMPLETED", "consistency_passed": True,
            "scope": "FP estimates of continuous analytic envelopes; no interval or hardware certificate",
            "decisions": decisions, "independent_fixtures": 4450,
            "model_and_fixture_preparation_seconds": preparation_seconds, "invocations": receipts,
            "kernel_median_seconds": statistics.median(r["kernel_seconds"] for r in measured),
            "subprocess_wall_median_seconds": statistics.median(r["subprocess_wall_seconds"] for r in measured),
            "final_diagnostics": baseline, "finished_utc": utc(),
            "end_to_end_seconds": time.perf_counter()-started,
            "endpoint_RWA_and_full_interval_LD_screens_passed": all(
                r["rwa_status"] == r["ld_status"] == "NUMERICAL_SCREEN_PASS" for r in decisions),
            "all_RMS_heuristics_passed": all(r["rms_heuristic_passed"] for r in decisions)}
        write_json(output/"result.json", result)
        write_json(output/"complete.json", {"result": artifact(output/"result.json"), "finished_utc": utc()})
        print(json.dumps({"status": result["status"], "consistency_passed": True,
             "endpoint_RWA_and_full_interval_LD_screens_passed":
                 result["endpoint_RWA_and_full_interval_LD_screens_passed"],
             "result_sha256": digest(output/"result.json")}, sort_keys=True, allow_nan=False))
        return 0
    except BaseException as exc:
        custody = None
        if pins is not None:
            try:
                check_pins(pins)
                custody = "UNCHANGED"
            except BaseException as pin_error:
                custody = type(pin_error).__name__ + ": " + str(pin_error)
        write_json(output/"failure.json", {"status": "INCOMPLETE", "exception": type(exc).__name__,
            "message": str(exc), "finished_utc": utc(), "elapsed_seconds": time.perf_counter()-started,
            "custody_at_failure": custody, "completed_receipts": receipts,
            "raw_process_records": sorted(p.name for p in output.glob("*.record.json")),
            "scope": "No retry or replacement; raw files and first outcome retained"})
        print(json.dumps({"status": "INCOMPLETE", "error": str(exc)}, allow_nan=False), file=sys.stderr)
        return 2
    finally:
        if old_handlers:
            signal.setitimer(signal.ITIMER_REAL, 0)
            for sig, handler in old_handlers.items():
                signal.signal(sig, handler)


if __name__ == "__main__":
    sys.exit(main())
