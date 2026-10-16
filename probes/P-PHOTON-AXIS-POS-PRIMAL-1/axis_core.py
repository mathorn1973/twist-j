#!/usr/bin/env python3
"""Frozen analysis core of P-PHOTON-AXIS-POS-PRIMAL-1 (Python standard library).

One module owns every rule that turns engine output into the terminal:

* the exact reduction S -> R -> Q of the #1116 axis estimator in Z[phi];
* the deterministic floating readout of D_r and D_L from exact integers;
* record parsing and the exact integrity checks;
* the #757 thermal and post-measurement mixing gates on the sixteen pilot-2
  sentinels, with the pilot-2 rank, tie, quantile and Geyer conventions;
* the #757 section 7 block jackknife and the M1/M2 intercept fits;
* the terminal precedence.

The production supervisor imports the thermal rule from here, the analysis is
``python3 axis_core.py analyze <probe-dir>``, and verify.py replays the same
functions on a second architecture.  Nothing here reads a link state; the
independent state reader is axis_reader.py.

The pilot-2 statistics are imported from the immutable pilot-2 analyzer.  Its
Geyer and pooled-ESS loops evaluate every lag before truncating; the lazy
versions below evaluate the same expressions in the same order and stop at
the same truncation lag, so they are bit-identical.  verify.py checks that
identity against the imported originals.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import importlib.util
import math
from pathlib import Path
import statistics
import sys
from fractions import Fraction
from typing import Sequence

sys.dont_write_bytecode = True

PROBE_ID = "P-PHOTON-AXIS-POS-PRIMAL-1"
SEED_ANCHOR = "89d3c850a673b5941ffd9831058c6ee9c345710b"
MODEL = "TWIST_Z5_FACE_WEIGHT_V1"
BIT_CAP = 256
FRACTION_COUNT_TOLERANCE = 1.0e-15

HERE = Path(__file__).resolve().parent
PILOT_DIR = HERE.parent / "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
PILOT_ANALYZER_SHA256 = "d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce"

TERMINALS = (
    "STOP_INTEGRITY",
    "STOP_MIXING",
    "AXIS_POS_EVIDENCE",
    "AXIS_NONPOS_EVIDENCE",
    "AXIS_UNRESOLVED",
)

# #1116 ordered orientations; CONTAINS[I][r] is r in I.
ORIENT = ("01", "02", "03", "23", "31", "12")
ORIENT_AXES = tuple((int(name[0]), int(name[1])) for name in ORIENT)
CONTAINS = tuple(tuple(str(r) in name for r in range(4)) for name in ORIENT)

# Score G = (0, 1, 2+sqrt5, -(2+sqrt5), -1) as u + v*phi, 2+sqrt5 = 1+2phi.
SCORE_UV = ((0, 0), (1, 0), (1, 2), (-1, -2), (-1, 0))


class IntegrityError(ValueError):
    """Malformed, inconsistent or non-frozen input: STOP_INTEGRITY."""


def _load_pilot():
    path = PILOT_DIR / "analyze_pilot.py"
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != PILOT_ANALYZER_SHA256:
        raise IntegrityError("pilot-2 analyzer hash mismatch")
    spec = importlib.util.spec_from_file_location("axis_pilot2_analyzer", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = _load_pilot()
MIXING_METRICS = P.MIXING_METRICS
FLUX_COUNT_FIELDS = P.FLUX_COUNT_FIELDS
SAMPLE_FIELDS = P.SAMPLE_FIELDS
fmt = P.fmt


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Gates:
    unique_min: float
    ess_min: float
    rhat_max: float
    bulk_min: float
    tail_min: float
    z_max: float


@dataclass(frozen=True)
class Config:
    name: str
    seed_prefix: str
    sizes: tuple[int, ...]
    fit_sizes: tuple[int, ...]
    spacing: tuple[tuple[int, int], ...]
    endpoints: tuple[int, ...]
    window: int
    samples: int
    thermal: Gates
    post: Gates
    b_min: int
    min_blocks: int

    def spacing_for(self, L: int) -> int:
        return dict(self.spacing)[L]

    def chains(self) -> tuple[tuple[str, int, str, int], ...]:
        return tuple(
            (chain_name(L, start, replica), L, start, replica)
            for L in self.sizes
            for start in ("cold", "hot")
            for replica in (1, 2)
        )

    def seed(self, L: int, start: str, replica: int) -> int:
        preimage = f"{self.seed_prefix}|L={L}|start={start}|replica={replica}"
        return int.from_bytes(hashlib.sha256(preimage.encode("ascii")).digest()[:8], "big")


def chain_name(L: int, start: str, replica: int) -> str:
    return f"L{L}_{start}_r{replica}"


FORMAL = Config(
    name="FORMAL",
    seed_prefix=f"{PROBE_ID}|{SEED_ANCHOR}",
    sizes=(8, 12, 16, 24, 32),
    fit_sizes=(12, 16, 24, 32),
    spacing=((8, 1), (12, 1), (16, 2), (24, 4), (32, 8)),
    endpoints=(1024, 2048, 4096, 8192),
    window=512,
    samples=1024,
    thermal=Gates(0.99, 64.0, 1.05, 400.0, 200.0, 4.0),
    post=Gates(0.99, 128.0, 1.03, 800.0, 400.0, 3.0),
    b_min=16,
    min_blocks=16,
)

# Plumbing tests only: sizes outside the production set (L <= 6), short
# schedules, relaxed gates and a seed family that cannot collide with FORMAL.
# Its estimator output is not opened before the pin.  verify.py never uses it.
DEVELOPMENT = Config(
    name="DEVELOPMENT",
    seed_prefix=f"DEVELOPMENT|{PROBE_ID}",
    sizes=(3, 4, 5, 6),
    fit_sizes=(3, 4, 5, 6),
    spacing=((3, 1), (4, 2), (5, 2), (6, 2)),
    endpoints=(32, 64),
    window=32,
    samples=64,
    thermal=Gates(0.5, 4.0, 1.5, 20.0, 10.0, 6.0),
    post=Gates(0.5, 4.0, 1.5, 20.0, 10.0, 6.0),
    b_min=2,
    min_blocks=4,
)

CONFIGS = {"FORMAL": FORMAL, "DEVELOPMENT": DEVELOPMENT}


# ---------------------------------------------------------------------------
# Exact Z[phi] reduction
# ---------------------------------------------------------------------------


def zphi_mul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """(a0 + a1 phi)(b0 + b1 phi) with phi^2 = phi + 1."""
    return (a[0] * b[0] + a[1] * b[1], a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def autocorrelation(series: Sequence[tuple[int, int]]) -> list[tuple[int, int]]:
    """R(k) = sum_t S(t) S(t+k) in Z[phi] for k = 0..L//2."""
    L = len(series)
    out: list[tuple[int, int]] = []
    for k in range(L // 2 + 1):
        u = v = 0
        for t in range(L):
            a = series[t]
            b = series[(t + k) % L]
            u += a[0] * b[0] + a[1] * b[1]
            v += a[0] * b[1] + a[1] * b[0] + a[1] * b[1]
        out.append((u, v))
    return out


def reduce_sample(S: dict[tuple[str, int], list[tuple[int, int]]], L: int):
    """Exact S[(I, r)] -> (R[(I, r)], Q[r]) with k = 0..L//2."""
    R = {}
    Q = [[[0, 0] for _ in range(L // 2 + 1)] for _ in range(4)]
    for i, name in enumerate(ORIENT):
        for r in range(4):
            series = S[(name, r)]
            if len(series) != L:
                raise IntegrityError("slice-sum length mismatch")
            row = autocorrelation(series)
            R[(name, r)] = row
            sign = 1 if CONTAINS[i][r] else -1
            for k, (u, v) in enumerate(row):
                Q[r][k][0] += sign * u
                Q[r][k][1] += sign * v
    return R, [[(u, v) for u, v in row] for row in Q]


# ---------------------------------------------------------------------------
# Deterministic floating readout (sqrt is correctly rounded on every IEEE host)
# ---------------------------------------------------------------------------

SQRT2 = math.sqrt(2.0)
SQRT3 = math.sqrt(3.0)
SQRT5 = math.sqrt(5.0)
SQRT6 = math.sqrt(6.0)
PHI = (1.0 + SQRT5) / 2.0
KAPPA2 = 5.0 - 2.0 * SQRT5

_COS_BASE = {
    Fraction(0): 1.0,
    Fraction(1, 4): 0.0,
    Fraction(1, 6): 0.5,
    Fraction(1, 8): SQRT2 / 2.0,
    Fraction(1, 12): SQRT3 / 2.0,
    Fraction(1, 16): math.sqrt(2.0 + SQRT2) / 2.0,
    Fraction(3, 16): math.sqrt(2.0 - SQRT2) / 2.0,
    Fraction(1, 24): (SQRT6 + SQRT2) / 4.0,
    Fraction(5, 24): (SQRT6 - SQRT2) / 4.0,
    Fraction(1, 32): math.sqrt(2.0 + math.sqrt(2.0 + SQRT2)) / 2.0,
    Fraction(3, 32): math.sqrt(2.0 + math.sqrt(2.0 - SQRT2)) / 2.0,
    Fraction(5, 32): math.sqrt(2.0 - math.sqrt(2.0 - SQRT2)) / 2.0,
    Fraction(7, 32): math.sqrt(2.0 - math.sqrt(2.0 + SQRT2)) / 2.0,
    Fraction(1, 5): (SQRT5 - 1.0) / 4.0,
    Fraction(1, 10): (SQRT5 + 1.0) / 4.0,
    Fraction(1, 20): math.sqrt(10.0 + 2.0 * SQRT5) / 4.0,
    Fraction(3, 20): math.sqrt(10.0 - 2.0 * SQRT5) / 4.0,
}


def cos_turn(turn: Fraction) -> float:
    """cos(2 pi turn) from closed forms in sqrt only."""
    x = turn % 1
    if x > Fraction(1, 2):
        x = 1 - x
    sign = 1.0
    if x > Fraction(1, 4):
        x = Fraction(1, 2) - x
        sign = -1.0
    if x not in _COS_BASE:
        raise IntegrityError(f"no closed-form cosine for turn {turn}")
    return sign * _COS_BASE[x]


def fold_weights(L: int) -> tuple[float, ...]:
    """mult_k cos(2 pi k/L) for the folded sum over k = 0..L//2."""
    weights = []
    for k in range(L // 2 + 1):
        mult = 1 if k == 0 or 2 * k == L else 2
        weights.append(mult * cos_turn(Fraction(k, L)))
    return tuple(weights)


def zphi_weighted(weights: Sequence[float], row: Sequence[tuple[int, int]]) -> float:
    a = math.fsum(w * u for w, (u, _) in zip(weights, row))
    b = math.fsum(w * v for w, (_, v) in zip(weights, row))
    return a + b * PHI


def d_values(Q: Sequence[Sequence[tuple[int, int]]], L: int) -> tuple[list[float], float]:
    """D_r = kappa^2/(3 L^4) sum_k w_k Q_r(k); D_L = mean over r."""
    weights = fold_weights(L)
    scale = 3.0 * float(L**4)
    d_r = [KAPPA2 * zphi_weighted(weights, Q[r]) / scale for r in range(4)]
    return d_r, math.fsum(d_r) / 4.0


def a_value(counts: Sequence[int], L: int) -> float:
    """Per-sample (1 + mean_p X_p^2)/2 with X_p^2 = kappa^2 G_p^2.

    kappa^2 G^2 is 5 - 2 sqrt5 for flux 1, 4 and 5 + 2 sqrt5 for flux 2, 3.
    """
    n14 = counts[1] + counts[4]
    n23 = counts[2] + counts[3]
    x2 = (5.0 * float(n14 + n23) + 2.0 * SQRT5 * float(n23 - n14)) / (6.0 * float(L**4))
    return (1.0 + x2) / 2.0


def orientation_power(rtot: Sequence[tuple[int, int]], L: int, samples: int) -> float:
    """Mean |G~_I(q_r)|^2 from an exact per-chain total of R_{I,r}(k)."""
    return zphi_weighted(fold_weights(L), rtot) / (float(samples) * float(L**4))


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def parse_fields(line: str, tag: str) -> dict[str, str]:
    parts = line.split(" ")
    if parts[0] != tag:
        raise IntegrityError(f"expected {tag}, found {parts[0][:40]}")
    fields: dict[str, str] = {}
    for token in parts[1:]:
        key, sep, value = token.partition("=")
        if not sep or not key or key in fields:
            raise IntegrityError(f"malformed field in {tag}")
        fields[key] = value
    return fields


def require_keys(fields: dict[str, str], keys: Sequence[str], tag: str) -> None:
    if tuple(fields) != tuple(keys):
        raise IntegrityError(f"{tag} field inventory or order mismatch")


def canonical_uint(value: str, name: str) -> int:
    if not value or any(c not in "0123456789" for c in value) or (value != "0" and value[0] == "0"):
        raise IntegrityError(f"noncanonical unsigned integer {name}")
    return int(value)


def canonical_int(value: str, name: str) -> int:
    body = value[1:] if value.startswith("-") else value
    if value == "-0":
        raise IntegrityError(f"noncanonical integer {name}")
    return (-1 if value.startswith("-") else 1) * canonical_uint(body, name)


def parse_pairs(text: str, count: int, name: str) -> list[tuple[int, int]]:
    cells = text.split(";")
    if len(cells) != count:
        raise IntegrityError(f"{name} length mismatch")
    out = []
    for cell in cells:
        u, sep, v = cell.partition(",")
        if not sep:
            raise IntegrityError(f"{name} malformed pair")
        out.append((canonical_int(u, name), canonical_int(v, name)))
    return out


def format_pairs(pairs: Sequence[tuple[int, int]]) -> str:
    return ";".join(f"{u},{v}" for u, v in pairs)


def is_lower_hex(value: str, width: int) -> bool:
    return len(value) == width and all(c in "0123456789abcdef" for c in value)


def validate_sample(line: str, L: int, index: int) -> dict[str, str]:
    """The pilot-2 SAMPLE contract, positionally exact."""
    sample = parse_fields(line, "SAMPLE")
    if set(sample) != SAMPLE_FIELDS or len(sample) != len(SAMPLE_FIELDS):
        raise IntegrityError("SAMPLE field inventory mismatch")
    if sample["index"] != str(index):
        raise IntegrityError(f"SAMPLE index {sample['index']} expected {index}")
    for metric in MIXING_METRICS:
        value = P.parse_finite(sample[metric], metric)
        if not math.isfinite(value):
            raise IntegrityError("nonfinite sentinel")
    if not is_lower_hex(sample["state_hash"], 16) or not is_lower_hex(sample["cache_hash"], 16):
        raise IntegrityError("SAMPLE hash format")
    counts = [canonical_uint(sample[f], f) for f in FLUX_COUNT_FIELDS]
    total = 6 * L**4
    if sum(counts) != total:
        raise IntegrityError("SAMPLE flux counts do not sum to 6 L^4")
    fractions = [float(sample[f"flux_fraction_{v}"]) for v in range(5)]
    for count, fraction in zip(counts, fractions):
        if abs(fraction - count / total) > FRACTION_COUNT_TOLERANCE:
            raise IntegrityError("SAMPLE flux fraction disagrees with count")
    if abs(math.fsum(fractions) - 1.0) > 5.0 * FRACTION_COUNT_TOLERANCE:
        raise IntegrityError("SAMPLE flux fractions do not sum to one")
    return sample


PROGRESS_KEYS = (
    "completed", "state_hash", "line_nonzero_0", "line_nonzero_1", "line_nonzero_2",
    "line_nonzero_3", "bit_cap_exhaustions", "max_prefix_bits", "local_decisions",
    "line_decisions", "census",
)


def validate_progress(line: str, tag: str, L: int, completed: int, last_hash: str) -> tuple[int, ...]:
    fields = parse_fields(line, tag)
    require_keys(fields, PROGRESS_KEYS, tag)
    if canonical_uint(fields["completed"], "completed") != completed:
        raise IntegrityError(f"{tag} completed mismatch")
    if fields["state_hash"] != last_hash:
        raise IntegrityError(f"{tag} state hash differs from last SAMPLE")
    if fields["census"] != "PASS":
        raise IntegrityError(f"{tag} census failed")
    if canonical_uint(fields["bit_cap_exhaustions"], "bit_cap") != 0:
        raise IntegrityError(f"{tag} exact-prefix cap exhausted")
    if canonical_uint(fields["max_prefix_bits"], "max_prefix_bits") > BIT_CAP:
        raise IntegrityError(f"{tag} prefix exceeds cap")
    if canonical_uint(fields["local_decisions"], "local") != completed * 4 * L**4:
        raise IntegrityError(f"{tag} local decision count")
    if canonical_uint(fields["line_decisions"], "line") != completed * 4 * L**3:
        raise IntegrityError(f"{tag} line decision count")
    return tuple(canonical_uint(fields[f"line_nonzero_{mu}"], "line_nonzero") for mu in range(4))


@dataclass
class ThermalRecord:
    name: str
    L: int
    start: str
    replica: int
    windows: dict[int, list[dict[str, str]]]
    line_moves: dict[int, tuple[int, ...]]
    commands: dict[int, str]
    accepted: int  # 0 when exhausted


@dataclass
class MeasureRecord:
    name: str
    samples: list[dict[str, str]]
    Q: list[list[list[tuple[int, int]]]]
    rtot: dict[tuple[str, int], list[tuple[int, int]]]
    line_moves: tuple[int, ...]


def text_lines(data: bytes, label: str, allow_tab: bool = False) -> list[str]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise IntegrityError(f"{label} is not LF with final LF")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError as error:
        raise IntegrityError(f"{label} is not ASCII") from error
    if any(b != 10 and not (allow_tab and b == 9) and not 32 <= b <= 126 for b in data):
        raise IntegrityError(f"{label} contains nonprinting bytes")
    return text.split("\n")[:-1]


RUN_KEYS = ("model", "L", "t", "seed", "start", "chain", "window", "samples", "spacing", "bit_cap")


def parse_thermal(data: bytes, cfg: Config, name: str, L: int, start: str, replica: int) -> ThermalRecord:
    lines = text_lines(data, name + " thermal record")
    run = parse_fields(lines[0], "AXIS_RUN")
    require_keys(run, RUN_KEYS, "AXIS_RUN")
    expected = {
        "model": MODEL, "L": str(L), "t": "1", "seed": f"0x{cfg.seed(L, start, replica):016x}",
        "start": start, "chain": name, "window": str(cfg.window), "samples": str(cfg.samples),
        "spacing": str(cfg.spacing_for(L)), "bit_cap": str(BIT_CAP),
    }
    if run != expected:
        raise IntegrityError(f"{name} AXIS_RUN differs from the frozen chain")
    cursor = 1
    record = ThermalRecord(name, L, start, replica, {}, {}, {}, 0)
    for endpoint in cfg.endpoints:
        window = []
        for offset in range(cfg.window):
            index = endpoint - cfg.window + 1 + offset
            window.append(validate_sample(lines[cursor], L, index))
            cursor += 1
        record.windows[endpoint] = window
        record.line_moves[endpoint] = validate_progress(
            lines[cursor], "ENDPOINT", L, endpoint, window[-1]["state_hash"])
        cursor += 1
        command = parse_fields(lines[cursor], "RUNNER_COMMAND")
        require_keys(command, ("endpoint", "command"), "RUNNER_COMMAND")
        if command["endpoint"] != str(endpoint) or command["command"] not in ("MEASURE", "CONTINUE"):
            raise IntegrityError(f"{name} malformed RUNNER_COMMAND")
        record.commands[endpoint] = command["command"]
        cursor += 1
        if command["command"] == "MEASURE":
            record.accepted = endpoint
            if lines[cursor:] != [f"MEASURE_BEGIN thermal_endpoint={endpoint}"]:
                raise IntegrityError(f"{name} thermal record tail after MEASURE")
            return record
    tail = [
        f"THERMAL_EXHAUSTED completed={cfg.endpoints[-1]}",
        "AXIS_STATUS THERMAL_EXHAUSTED",
        "EVIDENTIAL_STATUS ZERO_UNTIL_ANALYSIS",
    ]
    if lines[cursor:] != tail:
        raise IntegrityError(f"{name} thermal record tail after exhaustion")
    return record


def parse_measure(data: bytes, cfg: Config, name: str, L: int, accepted: int) -> MeasureRecord:
    lines = text_lines(data, name + " measure record")
    m = cfg.spacing_for(L)
    head = parse_fields(lines[0], "AXIS_MEASURE_RECORD")
    require_keys(head, ("chain", "L", "thermal_endpoint", "spacing", "transcript_sha256",
                        "transcript_bytes"), "AXIS_MEASURE_RECORD")
    if (head["chain"], head["L"], head["thermal_endpoint"], head["spacing"]) != (
            name, str(L), str(accepted), str(m)):
        raise IntegrityError(f"{name} measure record header mismatch")
    if not is_lower_hex(head["transcript_sha256"], 64):
        raise IntegrityError(f"{name} transcript hash format")
    canonical_uint(head["transcript_bytes"], "transcript_bytes")
    width = L // 2 + 1
    per_sample = 5
    expected_lines = 1 + cfg.samples * per_sample + 24 + 3
    if len(lines) != expected_lines:
        raise IntegrityError(f"{name} measure record has {len(lines)} lines")
    samples, Q = [], []
    cursor = 1
    for s in range(cfg.samples):
        samples.append(validate_sample(lines[cursor], L, s))
        cursor += 1
        rows = []
        for r in range(4):
            q = parse_fields(lines[cursor], "AXIS_Q")
            require_keys(q, ("index", "r", "Q"), "AXIS_Q")
            if q["index"] != str(s) or q["r"] != str(r):
                raise IntegrityError(f"{name} AXIS_Q order")
            rows.append(parse_pairs(q["Q"], width, "AXIS_Q"))
            cursor += 1
        Q.append(rows)
    rtot = {}
    for I in ORIENT:
        for r in range(4):
            row = parse_fields(lines[cursor], "AXIS_RTOT")
            require_keys(row, ("I", "r", "R"), "AXIS_RTOT")
            if row["I"] != I or row["r"] != str(r):
                raise IntegrityError(f"{name} AXIS_RTOT order")
            rtot[(I, r)] = parse_pairs(row["R"], width, "AXIS_RTOT")
            cursor += 1
    completed = accepted + cfg.samples * m
    line_moves = validate_progress(lines[cursor], "AXIS_DIAGNOSTICS", L, completed,
                                   samples[-1]["state_hash"])
    if lines[cursor + 1:] != ["AXIS_STATUS PASS", "EVIDENTIAL_STATUS ZERO_UNTIL_ANALYSIS"]:
        raise IntegrityError(f"{name} measure record footer")
    # Exact closure: the per-sample contrasts must sum to the contrast of the
    # exact per-chain autocorrelation totals.
    for r in range(4):
        for k in range(width):
            qu = sum(Q[s][r][k][0] for s in range(cfg.samples))
            qv = sum(Q[s][r][k][1] for s in range(cfg.samples))
            tu = sum((1 if CONTAINS[i][r] else -1) * rtot[(I, r)][k][0] for i, I in enumerate(ORIENT))
            tv = sum((1 if CONTAINS[i][r] else -1) * rtot[(I, r)][k][1] for i, I in enumerate(ORIENT))
            if (qu, qv) != (tu, tv):
                raise IntegrityError(f"{name} AXIS_Q does not close against AXIS_RTOT")
    return MeasureRecord(name, samples, Q, rtot, line_moves)


# ---------------------------------------------------------------------------
# Lazy, bit-identical pilot-2 statistics
# ---------------------------------------------------------------------------


def geyer_tau_int(data: Sequence[float]) -> float:
    if len(data) < 4:
        raise IntegrityError("Geyer IMS requires at least four values")
    centre = P.arithmetic_mean(data)
    gamma0 = P.autocovariance(data, 0, centre)
    if gamma0 <= 0.0:
        return 0.5

    def rho(lag: int) -> float:
        return 1.0 if lag == 0 else P.autocovariance(data, lag, centre) / gamma0

    pairs: list[float] = []
    lag = 0
    while lag < len(data) - 1:
        pair = rho(lag) + rho(lag + 1)
        if pair <= 0.0:
            break
        if pairs and pair > pairs[-1]:
            pair = pairs[-1]
        pairs.append(pair)
        lag += 2
    return max(0.5, -0.5 + math.fsum(pairs))


def series_stats(data: Sequence[float]):
    if len(data) < 4:
        raise IntegrityError("series has fewer than four values")
    centre = P.arithmetic_mean(data)
    variance = statistics.variance(data)
    tau = geyer_tau_int(data)
    ess = min(float(len(data)), len(data) / (2.0 * tau))
    mcse = math.sqrt(max(0.0, variance) * 2.0 * tau / len(data))
    return P.SeriesStats(centre, mcse, tau, ess, variance)


def half_drift_z(data: Sequence[float]) -> float:
    if len(data) % 2:
        raise IntegrityError("half drift requires an even sample count")
    mid = len(data) // 2
    left = series_stats(data[:mid])
    right = series_stats(data[mid:])
    return P.z_difference(left.mean, left.mcse, right.mean, right.mcse)


def multi_chain_ess(chains: Sequence[Sequence[float]]) -> float:
    if len(chains) < 2:
        raise IntegrityError("pooled ESS requires at least two chains")
    length = len(chains[0])
    if length < 4 or any(len(chain) != length for chain in chains):
        raise IntegrityError("pooled ESS chains must have equal length >= 4")
    chain_means = [P.arithmetic_mean(chain) for chain in chains]
    within = P.arithmetic_mean(statistics.variance(chain) for chain in chains)
    between = length * statistics.variance(chain_means)
    var_plus = ((length - 1.0) / length) * within + between / length
    total_count = len(chains) * length
    if var_plus <= 0.0:
        return float(total_count) if between == 0.0 else 0.0

    def rho(lag: int) -> float:
        if lag == 0:
            return 1.0
        mean_gamma = P.arithmetic_mean(
            P.autocovariance(chain, lag, centre) for chain, centre in zip(chains, chain_means))
        return min(1.0, 1.0 - (within - mean_gamma) / var_plus)

    pairs: list[float] = []
    lag = 0
    while lag < length - 1:
        pair = rho(lag) + rho(lag + 1)
        if pair <= 0.0:
            break
        if pairs and pair > pairs[-1]:
            pair = pairs[-1]
        pairs.append(pair)
        lag += 2
    tau = max(1.0, -1.0 + 2.0 * math.fsum(pairs))
    return min(float(total_count), total_count / tau)


def bulk_tail_ess(chains: Sequence[Sequence[float]]) -> tuple[float, float]:
    split = P.split_chains(chains)
    bulk = multi_chain_ess(P.rank_normalize(split))
    flat = [value for chain in split for value in chain]
    low = P.empirical_quantile(flat, 0.05)
    high = P.empirical_quantile(flat, 0.95)
    low_indicator = [[1.0 if value <= low else 0.0 for value in chain] for chain in split]
    high_indicator = [[1.0 if value >= high else 0.0 for value in chain] for chain in split]
    tail = min(multi_chain_ess(low_indicator), multi_chain_ess(high_indicator))
    return bulk, tail


# ---------------------------------------------------------------------------
# Mixing gates (#757 sections 5 and 6, pilot-2 conventions)
# ---------------------------------------------------------------------------

CHAIN_KEYS = (("cold", 1), ("cold", 2), ("hot", 1), ("hot", 2))


def mixing_gate(label: str, L: int, windows: dict[tuple[str, int], list[dict[str, str]]],
                line_moves: dict[tuple[str, int], tuple[int, ...]], gates: Gates,
                block_rule: bool, cfg: Config, out: list[str]) -> list[str]:
    """Return mixing failures; print the full surface into ``out``."""
    failures: list[str] = []
    series: dict[tuple[tuple[str, int], str], list[float]] = {}
    stats_cache = {}
    for key in CHAIN_KEYS:
        rows = windows[key]
        unique = len({row["state_hash"] for row in rows}) / len(rows)
        moves = line_moves[key]
        tag = f"L{L}_{key[0]}_r{key[1]}"
        out.append(f"{label}_CHAIN L={L} chain={tag} samples={len(rows)} unique_state_fraction={fmt(unique)} "
                   + " ".join(f"line_nonzero_{mu}={moves[mu]}" for mu in range(4)))
        if unique < gates.unique_min:
            failures.append(f"{label}_low_unique_{tag}")
        for mu in range(4):
            if moves[mu] == 0:
                failures.append(f"{label}_no_line_move_{tag}_mu{mu}")
        for metric in MIXING_METRICS:
            data = [float(row[metric]) for row in rows]
            st = series_stats(data)
            drift = half_drift_z(data)
            series[(key, metric)] = data
            stats_cache[(key, metric)] = st
            out.append(f"{label}_METRIC L={L} chain={tag} name={metric} mean={fmt(st.mean)} "
                       f"mcse={fmt(st.mcse)} tau_int={fmt(st.tau_int)} ess={fmt(st.ess)} "
                       f"half_drift_z={fmt(drift)}")
            if not (st.variance > 0.0 and math.isfinite(st.variance)):
                failures.append(f"{label}_zero_variance_{tag}_{metric}")
            if st.ess < gates.ess_min:
                failures.append(f"{label}_low_ess_{tag}_{metric}")
            if drift > gates.z_max:
                failures.append(f"{label}_half_drift_{tag}_{metric}")
    for metric in MIXING_METRICS:
        group = [series[(key, metric)] for key in CHAIN_KEYS]
        rank_rhat, folded_rhat = P.rank_folded_rhat(group)
        bulk, tail = bulk_tail_ess(group)
        cold_mean, cold_se = P.conservative_group_mean_se([stats_cache[(k, metric)] for k in CHAIN_KEYS[:2]])
        hot_mean, hot_se = P.conservative_group_mean_se([stats_cache[(k, metric)] for k in CHAIN_KEYS[2:]])
        z = P.z_difference(cold_mean, cold_se, hot_mean, hot_se)
        extra = ""
        if block_rule:
            # #757 section 7 applied to a sentinel: an unresolved sentinel is STOP_MIXING.
            b = block_size(max(stats_cache[(k, metric)].tau_int for k in CHAIN_KEYS), cfg)
            blocks = len(group[0]) // b
            extra = f" block={b} blocks_per_chain={blocks}"
            if blocks < cfg.min_blocks:
                failures.append(f"{label}_sentinel_unresolved_L{L}_{metric}")
        out.append(f"{label}_POOLED L={L} name={metric} rank_rhat={fmt(rank_rhat)} "
                   f"folded_rhat={fmt(folded_rhat)} bulk_ess={fmt(bulk)} tail_ess={fmt(tail)} "
                   f"cold_mean={fmt(cold_mean)} hot_mean={fmt(hot_mean)} hot_cold_z={fmt(z)}{extra}")
        if rank_rhat > gates.rhat_max:
            failures.append(f"{label}_rank_rhat_L{L}_{metric}")
        if folded_rhat > gates.rhat_max:
            failures.append(f"{label}_folded_rhat_L{L}_{metric}")
        if bulk < gates.bulk_min:
            failures.append(f"{label}_low_bulk_ess_L{L}_{metric}")
        if tail < gates.tail_min:
            failures.append(f"{label}_low_tail_ess_L{L}_{metric}")
        if z > gates.z_max:
            failures.append(f"{label}_hot_cold_L{L}_{metric}")
    return failures


def thermal_decision(L: int, endpoint: int, windows, line_moves, cfg: Config,
                     out: list[str]) -> bool:
    """The automated #757 section 5 endpoint rule for the four chains at L."""
    label = f"THERMAL_E{endpoint}"
    failures = mixing_gate(label, L, windows, line_moves, cfg.thermal, False, cfg, out)
    accepted = not failures
    out.append(f"THERMAL_DECISION L={L} endpoint={endpoint} "
               f"result={'ACCEPT' if accepted else 'CONTINUE'} failures={len(failures)}")
    return accepted


# ---------------------------------------------------------------------------
# Block jackknife, Student-t quantile and asymptotic fits (#757 sections 7, 9)
# ---------------------------------------------------------------------------

Z995 = 2.5758293035489


def t995(nu: int) -> float:
    """Upper 0.995 Student-t quantile, Cornish-Fisher (Abramowitz-Stegun 26.7.5)."""
    if nu < 1:
        raise IntegrityError("t quantile needs nu >= 1")
    z = Z995
    z2 = z * z
    g1 = (z2 + 1.0) * z / 4.0
    g2 = ((5.0 * z2 + 16.0) * z2 + 3.0) * z / 96.0
    g3 = (((3.0 * z2 + 19.0) * z2 + 17.0) * z2 - 15.0) * z / 384.0
    g4 = ((((79.0 * z2 + 776.0) * z2 + 1482.0) * z2 - 1920.0) * z2 - 945.0) * z / 92160.0
    n = float(nu)
    return z + g1 / n + g2 / (n * n) + g3 / (n * n * n) + g4 / (n * n * n * n)


def block_size(tau_max: float, cfg: Config) -> int:
    target = max(cfg.b_min, math.ceil(4.0 * tau_max))
    b = 1
    while b < target:
        b *= 2
    return b


@dataclass(frozen=True)
class BlockResult:
    resolved: bool
    taus: tuple[float, ...]
    b: int
    blocks_per_chain: int
    mean: float
    se: float
    nu: int
    lower: float
    upper: float


def block_jackknife(chains: Sequence[Sequence[float]], cfg: Config) -> BlockResult:
    taus = tuple(geyer_tau_int(chain) for chain in chains)
    b = block_size(max(taus), cfg)
    n_c = len(chains[0]) // b
    if any(len(chain) != len(chains[0]) for chain in chains):
        raise IntegrityError("unequal chain lengths in block jackknife")
    if n_c < cfg.min_blocks:
        return BlockResult(False, taus, b, n_c, math.nan, math.nan, 0, math.nan, math.nan)
    means = [math.fsum(chain[j * b:(j + 1) * b]) / b for chain in chains for j in range(n_c)]
    n = len(means)
    total = math.fsum(means)
    mean = total / n
    loo = [(total - m) / (n - 1) for m in means]
    loo_mean = math.fsum(loo) / n
    var = (n - 1) / n * math.fsum((x - loo_mean) ** 2 for x in loo)
    se = math.sqrt(var)
    q = t995(n - 1)
    return BlockResult(True, taus, b, n_c, mean, se, n - 1, mean - q * se, mean + q * se)


@dataclass(frozen=True)
class FitResult:
    singular: bool
    intercept: float
    slope: float
    se: float
    chi2: float
    nu: int
    lower: float
    upper: float


def wls_fit(points: Sequence[tuple[int, float, float]], power: int, nu: int) -> FitResult:
    """Weighted least squares y = c + a L^-power, weights 1/se^2, intercept free."""
    nan = math.nan
    if any(not (math.isfinite(y) and math.isfinite(se) and se > 0.0) for _, y, se in points):
        return FitResult(True, nan, nan, nan, nan, nu, nan, nan)
    xs = [1.0 / float(L**power) for L, _, _ in points]
    ws = [1.0 / (se * se) for _, _, se in points]
    ys = [y for _, y, _ in points]
    s = math.fsum(ws)
    sx = math.fsum(w * x for w, x in zip(ws, xs))
    sxx = math.fsum(w * x * x for w, x in zip(ws, xs))
    sy = math.fsum(w * y for w, y in zip(ws, ys))
    sxy = math.fsum(w * x * y for w, x, y in zip(ws, xs, ys))
    det = s * sxx - sx * sx
    if not (math.isfinite(det) and det > 0.0):
        return FitResult(True, nan, nan, nan, nan, nu, nan, nan)
    c = (sxx * sy - sx * sxy) / det
    a = (s * sxy - sx * sy) / det
    se_c = math.sqrt(sxx / det)
    chi2 = math.fsum(w * (y - c - a * x) ** 2 for w, x, y in zip(ws, xs, ys))
    q = t995(nu)
    return FitResult(False, c, a, se_c, chi2, nu, c - q * se_c, c + q * se_c)


# ---------------------------------------------------------------------------
# Full analysis
# ---------------------------------------------------------------------------


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


CHAINS_HEADER = ("chain", "L", "start", "replica", "seed", "spacing", "thermal_endpoint",
                 "transcript_bytes", "transcript_sha256", "thermal_record_sha256",
                 "measure_record_sha256", "exit_code", "stderr_bytes")


def read_custody(probe: Path, cfg: Config) -> dict[str, dict[str, str]]:
    lines = text_lines((probe / "CHAINS.tsv").read_bytes(), "CHAINS.tsv", allow_tab=True)
    if tuple(lines[0].split("\t")) != CHAINS_HEADER:
        raise IntegrityError("CHAINS.tsv header")
    rows = {}
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) != len(CHAINS_HEADER):
            raise IntegrityError("CHAINS.tsv row width")
        row = dict(zip(CHAINS_HEADER, cells))
        rows[row["chain"]] = row
    if tuple(rows) != tuple(name for name, *_ in cfg.chains()):
        raise IntegrityError("CHAINS.tsv chain inventory or order")
    for name, L, start, replica in cfg.chains():
        row = rows[name]
        if (row["L"], row["start"], row["replica"], row["seed"], row["spacing"]) != (
                str(L), start, str(replica), f"0x{cfg.seed(L, start, replica):016x}",
                str(cfg.spacing_for(L))):
            raise IntegrityError(f"CHAINS.tsv frozen fields for {name}")
        if row["exit_code"] != "0" or row["stderr_bytes"] != "0":
            raise IntegrityError(f"{name} engine exit or stderr")
    return rows


def check_reader(probe: Path, cfg: Config, custody: dict[str, dict[str, str]]) -> None:
    lines = text_lines((probe / "READER.txt").read_bytes(), "READER.txt")
    if not lines or lines[-1] != "READER_STATUS PASS":
        raise IntegrityError("independent state reader did not pass")
    seen = {}
    manifest_receipt = None
    for line in lines:
        if line.startswith("READER_CHAIN "):
            fields = parse_fields(line, "READER_CHAIN")
            seen[fields.get("chain", "")] = fields
        elif line.startswith("READER_MANIFEST "):
            manifest_receipt = parse_fields(line, "READER_MANIFEST")
    manifest = (probe / "STATE_MANIFEST.tsv").read_bytes()
    measured_chains = sum(1 for row in custody.values() if row["thermal_endpoint"] != "0")
    if manifest_receipt != {"sha256": hashlib.sha256(manifest).hexdigest(),
                            "rows": str(measured_chains * cfg.samples)}:
        raise IntegrityError("STATE_MANIFEST.tsv differs from the reader receipt")
    for name, *_ in cfg.chains():
        row = custody[name]
        if row["thermal_endpoint"] == "0":
            continue
        fields = seen.get(name)
        if fields is None:
            raise IntegrityError(f"reader did not cover {name}")
        if fields.get("measure_record_sha256") != row["measure_record_sha256"] or fields.get(
                "transcript_sha256") != row["transcript_sha256"] or fields.get("mismatches") != "0" or fields.get(
                "states") != str(cfg.samples):
            raise IntegrityError(f"reader receipt mismatch for {name}")


def analyze(probe: Path, cfg: Config = FORMAL) -> tuple[list[str], str]:
    out: list[str] = [f"AXIS_ANALYSIS {PROBE_ID} {cfg.name} V1"]
    integrity: list[str] = []
    mixing: list[str] = []
    measured: dict[int, dict[tuple[str, int], MeasureRecord]] = {}
    try:
        custody = read_custody(probe, cfg)
        thermal: dict[str, ThermalRecord] = {}
        for name, L, start, replica in cfg.chains():
            path = probe / "records" / f"{name}.thermal.txt"
            data = path.read_bytes()
            if hashlib.sha256(data).hexdigest() != custody[name]["thermal_record_sha256"]:
                raise IntegrityError(f"{name} thermal record hash differs from CHAINS.tsv")
            thermal[name] = parse_thermal(data, cfg, name, L, start, replica)
            if str(thermal[name].accepted) != custody[name]["thermal_endpoint"]:
                raise IntegrityError(f"{name} thermal endpoint differs from CHAINS.tsv")
        # Replay the automated endpoint rule; it must reproduce every command.
        for L in cfg.sizes:
            names = {key: chain_name(L, *key) for key in CHAIN_KEYS}
            decided = 0
            for endpoint in cfg.endpoints:
                commands = {thermal[n].commands.get(endpoint) for n in names.values()}
                if commands == {None}:
                    break
                if len(commands) != 1:
                    raise IntegrityError(f"L{L} chains received different commands at {endpoint}")
                windows = {key: thermal[n].windows[endpoint] for key, n in names.items()}
                moves = {key: thermal[n].line_moves[endpoint] for key, n in names.items()}
                accepted = thermal_decision(L, endpoint, windows, moves, cfg, out)
                if ("MEASURE" if accepted else "CONTINUE") != commands.pop():
                    raise IntegrityError(f"L{L} recorded command disagrees with the rule at {endpoint}")
                if accepted:
                    decided = endpoint
                    break
            if decided == 0:
                mixing.append(f"STOP_MIXING_thermal_exhausted_L{L}")
                out.append(f"THERMAL_RESULT L={L} accepted_endpoint=NONE")
                continue
            out.append(f"THERMAL_RESULT L={L} accepted_endpoint={decided}")
            check_measure = {}
            for key, n in names.items():
                path = probe / "records" / f"{n}.measure.txt"
                data = path.read_bytes()
                if hashlib.sha256(data).hexdigest() != custody[n]["measure_record_sha256"]:
                    raise IntegrityError(f"{n} measure record hash differs from CHAINS.tsv")
                check_measure[key] = parse_measure(data, cfg, n, L, decided)
            measured[L] = check_measure
        check_reader(probe, cfg, custody)
    except (IntegrityError, OSError, KeyError, IndexError, ValueError, OverflowError,
            statistics.StatisticsError) as error:
        integrity.append(str(error).replace("\n", " ") or error.__class__.__name__)

    if integrity:
        out.append("AXIS_INTEGRITY " + integrity[0])
        out.append("AXIS_FAILURES STOP_INTEGRITY")
        out.append("AXIS_TERMINAL STOP_INTEGRITY")
        return out, "STOP_INTEGRITY"

    # Post-measurement mixing (#757 section 6) and the AXIS estimator.
    per_l: dict[int, BlockResult] = {}
    try:
        for L, records in sorted(measured.items()):
            windows = {key: rec.samples for key, rec in records.items()}
            moves = {key: rec.line_moves for key, rec in records.items()}
            mixing.extend(mixing_gate("POST", L, windows, moves, cfg.post, True, cfg, out))
            per_l[L] = estimator_block(L, records, cfg, out)
    except (IntegrityError, ValueError, OverflowError, statistics.StatisticsError) as error:
        out.append("AXIS_INTEGRITY statistics_" + (str(error).replace("\n", " ") or "error"))
        out.append("AXIS_FAILURES STOP_INTEGRITY")
        out.append("AXIS_TERMINAL STOP_INTEGRITY")
        return out, "STOP_INTEGRITY"

    sign_terminal, notes = fit_terminal(per_l, cfg, out)
    if mixing:
        terminal = "STOP_MIXING"
        failures = sorted(set(mixing))
        out.append("FIT_AUTHORITY NONE")
    else:
        terminal = sign_terminal
        failures = notes
        out.append("FIT_AUTHORITY PRIMARY")
    out.append("AXIS_FAILURES " + (",".join(failures) if failures else "NONE"))
    out.append(f"AXIS_TERMINAL {terminal}")
    return out, terminal


def estimator_block(L: int, records: dict[tuple[str, int], MeasureRecord], cfg: Config,
                    out: list[str]) -> BlockResult:
    d_series: dict[tuple[str, int], list[float]] = {}
    dr_series: dict[tuple[str, int], list[list[float]]] = {}
    a_series: dict[tuple[str, int], list[float]] = {}
    for key in CHAIN_KEYS:
        rec = records[key]
        ds, drs, avals = [], [[], [], [], []], []
        for s in range(cfg.samples):
            d_r, d = d_values(rec.Q[s], L)
            ds.append(d)
            for r in range(4):
                drs[r].append(d_r[r])
            counts = [int(rec.samples[s][f]) for f in FLUX_COUNT_FIELDS]
            avals.append(a_value(counts, L))
        d_series[key], dr_series[key], a_series[key] = ds, drs, avals
    chains = [d_series[key] for key in CHAIN_KEYS]
    primary = block_jackknife(chains, cfg)
    print_block(out, "AXIS_D", L, primary)
    for key in CHAIN_KEYS:
        st = series_stats(d_series[key])
        out.append(f"AXIS_D_CHAIN L={L} chain=L{L}_{key[0]}_r{key[1]} mean={fmt(st.mean)} "
                   f"mcse={fmt(st.mcse)} tau_int={fmt(st.tau_int)}")
    cold = [series_stats(d_series[k]) for k in CHAIN_KEYS[:2]]
    hot = [series_stats(d_series[k]) for k in CHAIN_KEYS[2:]]
    cm, cse = P.conservative_group_mean_se(cold)
    hm, hse = P.conservative_group_mean_se(hot)
    out.append(f"AXIS_D_HOTCOLD L={L} cold_mean={fmt(cm)} cold_se={fmt(cse)} hot_mean={fmt(hm)} "
               f"hot_se={fmt(hse)} z={fmt(P.z_difference(cm, cse, hm, hse))} authority=NONE")
    for r in range(4):
        print_block(out, f"AXIS_DR{r}", L, block_jackknife([dr_series[k][r] for k in CHAIN_KEYS], cfg))
    print_block(out, "AXIS_A", L, block_jackknife([a_series[k] for k in CHAIN_KEYS], cfg))
    rl = [[3.0 * (a - d) for a, d in zip(a_series[k], d_series[k])] for k in CHAIN_KEYS]
    print_block(out, "AXIS_RL", L, block_jackknife(rl, cfg))
    for I in ORIENT:
        for r in range(4):
            values = [orientation_power(records[k].rtot[(I, r)], L, cfg.samples) for k in CHAIN_KEYS]
            out.append(f"AXIS_POWER L={L} I={I} r={r} contains={int(str(r) in I)} "
                       + " ".join(f"{k[0]}_r{k[1]}={fmt(v)}" for k, v in zip(CHAIN_KEYS, values))
                       + f" pooled={fmt(math.fsum(values) / 4.0)} authority=NONE")
    return primary


def print_block(out: list[str], tag: str, L: int, res: BlockResult) -> None:
    taus = ",".join(fmt(t) for t in res.taus)
    if not res.resolved:
        out.append(f"{tag} L={L} resolved=NO tau_int={taus} block={res.b} "
                   f"blocks_per_chain={res.blocks_per_chain}")
        return
    out.append(f"{tag} L={L} resolved=YES tau_int={taus} block={res.b} "
               f"blocks_per_chain={res.blocks_per_chain} mean={fmt(res.mean)} se={fmt(res.se)} "
               f"nu={res.nu} t995={fmt(t995(res.nu))} lower99={fmt(res.lower)} upper99={fmt(res.upper)}")


def fit_terminal(per_l: dict[int, BlockResult], cfg: Config, out: list[str]) -> tuple[str, list[str]]:
    missing = [L for L in cfg.fit_sizes if L not in per_l]
    if missing:
        out.append("AXIS_FIT unavailable missing_sizes=" + ",".join(str(L) for L in missing))
        return "AXIS_UNRESOLVED", ["unmeasured_fit_sizes"]
    unresolved = [L for L in cfg.fit_sizes if not per_l[L].resolved]
    if unresolved:
        out.append("AXIS_FIT unavailable unresolved_sizes=" + ",".join(str(L) for L in unresolved))
        return "AXIS_UNRESOLVED", [f"D_unresolved_L{L}" for L in unresolved]
    nu = min(per_l[L].nu for L in cfg.fit_sizes)
    points = [(L, per_l[L].mean, per_l[L].se) for L in cfg.fit_sizes]
    fits = {}
    for model, power in (("M1", 1), ("M2", 2)):
        fit = wls_fit(points, power, nu)
        fits[model] = fit
        if fit.singular:
            out.append(f"AXIS_FIT model={model} singular=YES")
        else:
            out.append(f"AXIS_FIT model={model} power={power} delta_inf={fmt(fit.intercept)} "
                       f"slope={fmt(fit.slope)} se={fmt(fit.se)} nu={fit.nu} t995={fmt(t995(fit.nu))} "
                       f"lower99={fmt(fit.lower)} upper99={fmt(fit.upper)} chi2={fmt(fit.chi2)} "
                       f"chi2_dof={len(points) - 2} chi2_authority=NONE")
    if any(fit.singular for fit in fits.values()):
        return "AXIS_UNRESOLVED", ["singular_fit"]
    if all(fit.lower > 0.0 for fit in fits.values()):
        return "AXIS_POS_EVIDENCE", []
    if all(fit.upper <= 0.0 for fit in fits.values()):
        return "AXIS_NONPOS_EVIDENCE", []
    return "AXIS_UNRESOLVED", ["sign_not_earned_in_both_models"]


def main(argv: Sequence[str]) -> int:
    if len(argv) != 2 or argv[0] != "analyze":
        print("usage: python3 axis_core.py analyze <probe-dir>", file=sys.stderr)
        return 64
    lines, _ = analyze(Path(argv[1]).resolve(), FORMAL)
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
