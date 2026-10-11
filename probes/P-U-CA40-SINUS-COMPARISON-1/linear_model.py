"""Shared frozen linear model and custody helpers, no execution on import.
Copied without scientific changes from P-U-CA40-TRAJECTORY-VALIDITY-1 at
604bad993830222ab8c34cee6f31a7a36043e350; Apache-2.0, A. M. Thorn.
The new campaign calls prepare_model/advance only after its public pin.
"""
import cmath
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import sys

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


