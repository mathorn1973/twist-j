#!/usr/bin/env python3
"""Pinned, read-only terminal wrapper for the second exact Z5 mixing pilot.

The wrapper has no command-line arguments and performs no filesystem writes.
It owns three logically separate decisions, in this strict precedence:

1. an independent exact-local theorem audit may emit ``BREAK_KERNEL``;
2. pinned-artifact, reference-fixture, raw-custody, or analyzer-custody
   failures emit ``STOP_INTEGRITY``;
3. otherwise the terminal is copied from the byte-identical frozen analyzer
   stdout: ``STOP_MIXING`` or ``PILOT_READY_FOR_PRODUCTION_PREREG``.

An untrusted raw-log marker can never select ``BREAK_KERNEL``.  All modeled
terminals exit zero with LF-only ASCII stdout and empty stderr.  A command-line
misuse exits 64; an uncaught internal programming failure remains nonzero.
Only the Python standard library is used.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from itertools import product
import math
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Iterable, Sequence


PILOT_ID = "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
MAX_RAW_BYTES = 5 * 1024 * 1024
EXPECTED_SAMPLES = 512
EXPECTED_BIT_CAP = 256
FRACTION_COUNT_TOLERANCE = 1.0e-15

PINNED_FILES = (
    "PREREG.md",
    "PILOT_PIN.md",
    "README.md",
    "photon_z5.cpp",
    "photon_z5_part1.inc",
    "photon_z5_part2.inc",
    "photon_z5_part3.inc",
    "photon_z5_part4.inc",
    "analyze_pilot.py",
    "reference_check.py",
    "verify.py",
    "run_pilot.py",
    "SELFTEST_EXPECTED.txt",
    "REFERENCE_EXPECTED.txt",
)

LOG_NAMES = (
    "L6_cold_r1.log",
    "L6_cold_r2.log",
    "L6_hot_r1.log",
    "L6_hot_r2.log",
    "L8_cold_r1.log",
    "L8_cold_r2.log",
    "L8_hot_r1.log",
    "L8_hot_r2.log",
)

MANIFEST_HEADER = (
    "filename\tL\tstart\treplica\tseed\tthermal_cycles\tmeasurements"
    "\tbetween_cycles\tbytes\tsha256\texit_code\tstderr_bytes"
)

MIXING_METRICS = (
    "logw",
    "polyakov_radius_mean",
    "polyakov_radius_0",
    "polyakov_radius_1",
    "polyakov_radius_2",
    "polyakov_radius_3",
    "vortex_density",
    "monopole_density",
    "score_mean",
    "flux_asym_14",
    "flux_asym_23",
    "flux_fraction_0",
    "flux_fraction_1",
    "flux_fraction_2",
    "flux_fraction_3",
    "flux_fraction_4",
)

FLUX_COUNT_FIELDS = tuple(f"flux_count_{value}" for value in range(5))

HEX64_RE = re.compile(r"[0-9a-f]{64}\Z")
HEX16_RE = re.compile(r"[0-9a-f]{16}\Z")
PIN_LINE_RE = re.compile(r"([0-9a-f]{64})  ([A-Za-z0-9][A-Za-z0-9_.-]*)\Z")


@dataclass(frozen=True, slots=True)
class ChainSpec:
    filename: str
    linear_size: int
    start: str
    replica: int
    seed: int
    thermal_cycles: int
    measurements: int
    between_cycles: int

    @property
    def total_cycles(self) -> int:
        return self.thermal_cycles + self.measurements * self.between_cycles


CHAINS = tuple(
    ChainSpec(
        filename=f"L{linear_size}_{start}_r{replica}.log",
        linear_size=linear_size,
        start=start,
        replica=replica,
        seed=(
            (0xE755060000000000 if linear_size == 6 else 0xE755080000000000)
            + (0x100 if start == "cold" else 0x200)
            + replica
        ),
        thermal_cycles=512 if linear_size == 6 else 1024,
        measurements=EXPECTED_SAMPLES,
        between_cycles=4 if linear_size == 6 else 8,
    )
    for linear_size in (6, 8)
    for start in ("cold", "hot")
    for replica in (1, 2)
)

TOTAL_HEATBATH_DECISIONS = sum(
    spec.total_cycles
    * (4 * spec.linear_size**4 + 4 * spec.linear_size**3)
    for spec in CHAINS
)


class IntegrityFailure(RuntimeError):
    """A modeled artifact, custody, fixture, or analysis integrity failure."""


@dataclass(frozen=True, slots=True)
class BreakWitness:
    reason: str
    environment: tuple[int, ...] | None = None
    candidate: int | None = None
    expected: str | None = None
    actual: str | None = None

    def line(self) -> str:
        fields = [f"reason={safe_token(self.reason)}"]
        if self.environment is not None:
            fields.append("environment=" + ",".join(map(str, self.environment)))
        if self.candidate is not None:
            fields.append(f"candidate={self.candidate}")
        if self.expected is not None:
            fields.append(f"expected={safe_token(self.expected)}")
        if self.actual is not None:
            fields.append(f"actual={safe_token(self.actual)}")
        return "BREAK_WITNESS " + " ".join(fields)


@dataclass(frozen=True, slots=True)
class QPhi:
    """The exact algebraic integer ``a + b*phi``, with ``phi^2=phi+1``."""

    a: int
    b: int = 0

    def __add__(self, other: "QPhi") -> "QPhi":
        return QPhi(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "QPhi":
        return QPhi(-self.a, -self.b)

    def __sub__(self, other: "QPhi") -> "QPhi":
        return self + (-other)

    def __mul__(self, other: "QPhi") -> "QPhi":
        return QPhi(
            self.a * other.a + self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    def scale(self, integer: int) -> "QPhi":
        return QPhi(integer * self.a, integer * self.b)

    def token(self) -> str:
        return f"{self.a},{self.b}"


PHI = QPhi(0, 1)
FACE_WEIGHTS = (
    QPhi(4),
    QPhi(1, 1),
    QPhi(2, -1),
    QPhi(2, -1),
    QPhi(1, 1),
)
INCIDENT_SIGNS = (1, 1, 1, -1, -1, -1)
EXPECTED_ZERO_MASSES = (
    QPhi(4096),
    QPhi(89, 144),
    QPhi(233, -144),
    QPhi(233, -144),
    QPhi(89, 144),
)


def safe_token(value: str) -> str:
    return "".join(
        character if character.isalnum() or character in "._,:;=+-" else "_"
        for character in value
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def emit(data: bytes) -> None:
    stream = getattr(sys.stdout, "buffer", None)
    if stream is not None:
        stream.write(data)
        stream.flush()
    else:
        sys.stdout.write(data.decode("ascii"))
        sys.stdout.flush()


def usage() -> int:
    message = b"USAGE_ERROR expected_no_arguments\n"
    stream = getattr(sys.stderr, "buffer", None)
    if stream is not None:
        stream.write(message)
        stream.flush()
    else:
        sys.stderr.write(message.decode("ascii"))
        sys.stderr.flush()
    return 64


def qsign(value: QPhi) -> int:
    """Exact sign in the real embedding ``phi=(1+sqrt(5))/2``."""

    c = 2 * value.a + value.b
    d = value.b
    if c == 0 and d == 0:
        return 0
    if c >= 0 and d >= 0:
        return 1
    if c <= 0 and d <= 0:
        return -1
    left = c * c
    right = 5 * d * d
    if left == right:
        raise ArithmeticError("impossible_nonzero_square_equality_in_Q_sqrt5")
    if c > 0 and d < 0:
        return 1 if left > right else -1
    return 1 if right > left else -1


def qsum(values: Iterable[QPhi]) -> QPhi:
    total = QPhi(0)
    for value in values:
        total = total + value
    return total


def local_masses(environment: tuple[int, ...]) -> tuple[QPhi, ...]:
    if len(environment) != 6:
        raise ValueError("local_environment_must_have_six_residuals")
    result: list[QPhi] = []
    for candidate in range(5):
        mass = QPhi(1)
        for residual, incidence in zip(environment, INCIDENT_SIGNS):
            mass = mass * FACE_WEIGHTS[(residual + incidence * candidate) % 5]
        result.append(mass)
    return tuple(result)


def mass_vector_token(values: Sequence[QPhi]) -> str:
    return ";".join(value.token() for value in values)


def independent_exact_local_audit() -> tuple[BreakWitness | None, tuple[str, ...]]:
    """Recompute the exact-local PR #760 contract without importing its code."""

    if PHI * PHI != PHI + QPhi(1):
        return BreakWitness("phi_relation", expected="0,1_squared=1,1"), ()
    for candidate, weight in enumerate(FACE_WEIGHTS):
        if qsign(weight) <= 0:
            return BreakWitness(
                "nonpositive_face_weight", candidate=candidate, actual=weight.token()
            ), ()
    if FACE_WEIGHTS[1] != FACE_WEIGHTS[4] or FACE_WEIGHTS[2] != FACE_WEIGHTS[3]:
        return BreakWitness("face_weight_inversion_covariance"), ()

    zero_masses = local_masses((0, 0, 0, 0, 0, 0))
    if zero_masses != EXPECTED_ZERO_MASSES:
        return BreakWitness(
            "all_zero_mass_vector",
            environment=(0, 0, 0, 0, 0, 0),
            expected=mass_vector_token(EXPECTED_ZERO_MASSES),
            actual=mass_vector_token(zero_masses),
        ), ()
    zero_total = qsum(zero_masses)
    if zero_total != QPhi(4740):
        return BreakWitness(
            "all_zero_normalization", expected="4740,0", actual=zero_total.token()
        ), ()
    divisor = math.gcd(zero_masses[0].a, zero_total.a)
    numerator = zero_masses[0].a // divisor
    denominator = zero_total.a // divisor
    if (numerator, denominator) != (1024, 1185):
        return BreakWitness(
            "all_zero_probability",
            expected="1024/1185",
            actual=f"{numerator}/{denominator}",
        ), ()
    if denominator <= 0 or denominator & (denominator - 1) == 0:
        return BreakWitness(
            "all_zero_probability_became_dyadic", actual=f"{numerator}/{denominator}"
        ), ()

    environment_count = 0
    candidate_count = 0
    balance_count = 0
    for residuals in product(range(5), repeat=6):
        environment = tuple(residuals)
        masses = local_masses(environment)
        for candidate, mass in enumerate(masses):
            if qsign(mass) <= 0:
                return BreakWitness(
                    "nonpositive_local_mass",
                    environment=environment,
                    candidate=candidate,
                    actual=mass.token(),
                ), ()
            candidate_count += 1
        normalization = qsum(masses)
        if qsign(normalization) <= 0:
            return BreakWitness(
                "nonpositive_local_normalization",
                environment=environment,
                actual=normalization.token(),
            ), ()

        shifted_environment = tuple(
            (residual + incidence) % 5
            for residual, incidence in zip(environment, INCIDENT_SIGNS)
        )
        shifted_masses = local_masses(shifted_environment)
        for candidate in range(5):
            expected = masses[(candidate + 1) % 5]
            if shifted_masses[candidate] != expected:
                return BreakWitness(
                    "local_translation_covariance",
                    environment=environment,
                    candidate=candidate,
                    expected=expected.token(),
                    actual=shifted_masses[candidate].token(),
                ), ()

        # The common exterior factor and normalization cancel.  These exact
        # numerators are the pairwise detailed-balance identity L_a L_b.
        for left in range(5):
            for right in range(5):
                forward = masses[left] * masses[right]
                reverse = masses[right] * masses[left]
                if forward != reverse:
                    return BreakWitness(
                        "local_pairwise_detailed_balance",
                        environment=environment,
                        candidate=5 * left + right,
                        expected=reverse.token(),
                        actual=forward.token(),
                    ), ()
                balance_count += 1
        environment_count += 1

    if environment_count != 5**6 or candidate_count != 5**7:
        return BreakWitness(
            "local_environment_census",
            expected=f"{5**6}/{5**7}",
            actual=f"{environment_count}/{candidate_count}",
        ), ()

    lines = (
        "EXACT_LOCAL_AUDIT environments=15625 candidates=78125 positivity=PASS covariance=PASS",
        f"EXACT_LOCAL_DETAILED_BALANCE pairs={balance_count} status=PASS",
        "EXACT_LOCAL_Q witness=all_zero mass=4096 total=4740 probability=1024/1185 nondyadic=PASS",
    )
    return None, lines


def require_regular_file(path: Path, label: str) -> bytes:
    if path.is_symlink():
        raise IntegrityFailure(f"symlink_forbidden:{label}")
    try:
        if not path.is_file():
            raise IntegrityFailure(f"missing_file:{label}")
        return path.read_bytes()
    except OSError as error:
        raise IntegrityFailure(f"unreadable_file:{label}:{error.__class__.__name__}") from error


def decode_ascii_lf(data: bytes, label: str) -> str:
    if not data or not data.endswith(b"\n") or b"\r" in data:
        raise IntegrityFailure(f"not_LF_with_final_LF:{label}")
    try:
        return data.decode("ascii")
    except UnicodeDecodeError as error:
        raise IntegrityFailure(f"not_ASCII:{label}") from error


def verify_pin_manifest(base: Path) -> tuple[str, int]:
    manifest_data = require_regular_file(base / "SHA256SUMS", "SHA256SUMS")
    manifest_text = decode_ascii_lf(manifest_data, "SHA256SUMS")
    entries: list[tuple[str, str]] = []
    seen: set[str] = set()
    for line in manifest_text.splitlines():
        match = PIN_LINE_RE.fullmatch(line)
        if match is None:
            raise IntegrityFailure("SHA256SUMS_malformed")
        digest, filename = match.groups()
        if filename in seen:
            raise IntegrityFailure(f"SHA256SUMS_duplicate:{filename}")
        entries.append((filename, digest))
        seen.add(filename)
    if tuple(filename for filename, _ in entries) != PINNED_FILES:
        raise IntegrityFailure("SHA256SUMS_inventory_or_order_mismatch")
    for filename, expected_digest in entries:
        actual_data = require_regular_file(base / filename, filename)
        actual_digest = sha256_bytes(actual_data)
        if actual_digest != expected_digest:
            raise IntegrityFailure(f"pinned_hash_mismatch:{filename}")
    return sha256_bytes(manifest_data), len(entries)


def child_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment.update(
        {
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
        }
    )
    return environment


def run_python(script: Path, arguments: Sequence[Path] = ()) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            (sys.executable, str(script), *(str(argument) for argument in arguments)),
            cwd=script.parent,
            env=child_environment(),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=300,
        )
    except (OSError, subprocess.SubprocessError) as error:
        raise IntegrityFailure(
            f"subprocess_failure:{script.name}:{error.__class__.__name__}"
        ) from error


def verify_reference_fixture(base: Path) -> tuple[str, int]:
    expected = require_regular_file(base / "REFERENCE_EXPECTED.txt", "REFERENCE_EXPECTED.txt")
    decode_ascii_lf(expected, "REFERENCE_EXPECTED.txt")
    completed = run_python(base / "reference_check.py")
    if completed.returncode != 0:
        raise IntegrityFailure(f"reference_exit:{completed.returncode}")
    if completed.stderr:
        raise IntegrityFailure("reference_stderr_nonempty")
    if completed.stdout != expected:
        raise IntegrityFailure("reference_stdout_mismatch")
    return sha256_bytes(completed.stdout), len(completed.stdout)


def parse_fields(line: str, record: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    tokens = line.split()
    if not tokens or tokens[0] != record:
        raise IntegrityFailure(f"unexpected_record:{record}")
    for token in tokens[1:]:
        if "=" not in token:
            raise IntegrityFailure(f"malformed_field:{record}")
        key, value = token.split("=", 1)
        if not key or not value or key in fields:
            raise IntegrityFailure(f"duplicate_or_empty_field:{record}")
        fields[key] = value
    return fields


def canonical_uint(value: str, label: str) -> int:
    if (
        not value
        or (value != "0" and value.startswith("0"))
        or any(character not in "0123456789" for character in value)
    ):
        raise IntegrityFailure(f"noncanonical_uint:{label}")
    return int(value, 10)


def finite_float(value: str, label: str) -> float:
    try:
        result = float(value)
    except ValueError as error:
        raise IntegrityFailure(f"invalid_float:{label}") from error
    if not math.isfinite(result):
        raise IntegrityFailure(f"nonfinite_float:{label}")
    return result


def validate_raw_log(spec: ChainSpec, data: bytes) -> None:
    if len(data) > MAX_RAW_BYTES:
        raise IntegrityFailure(f"raw_over_5MiB:{spec.filename}")
    text = decode_ascii_lf(data, spec.filename)
    if any(byte != 10 and not 32 <= byte <= 126 for byte in data):
        raise IntegrityFailure(f"raw_nonprinting_ASCII:{spec.filename}")
    lines = text.splitlines()
    if len(lines) != 1 + EXPECTED_SAMPLES + 3:
        raise IntegrityFailure(f"raw_record_count:{spec.filename}")

    run_fields = parse_fields(lines[0], "RUN")
    expected_run = {
        "model": "TWIST_Z5_FACE_WEIGHT_V1",
        "L": str(spec.linear_size),
        "t": "1",
        "seed": f"0x{spec.seed:016x}",
        "start": spec.start,
        "replica": str(spec.replica),
        "thermal_cycles": str(spec.thermal_cycles),
        "measurements": str(spec.measurements),
        "between_cycles": str(spec.between_cycles),
        "bit_cap": str(EXPECTED_BIT_CAP),
    }
    if run_fields != expected_run:
        raise IntegrityFailure(f"raw_RUN_mismatch:{spec.filename}")

    expected_sample_fields = {
        "index",
        *MIXING_METRICS,
        *FLUX_COUNT_FIELDS,
        "state_hash",
        "cache_hash",
    }
    expected_flux_total = 6 * spec.linear_size**4
    for index in range(EXPECTED_SAMPLES):
        sample = parse_fields(lines[index + 1], "SAMPLE")
        if set(sample) != expected_sample_fields:
            raise IntegrityFailure(f"raw_SAMPLE_inventory:{spec.filename}:{index}")
        if sample["index"] != str(index):
            raise IntegrityFailure(f"raw_SAMPLE_index:{spec.filename}:{index}")
        if HEX16_RE.fullmatch(sample["state_hash"]) is None:
            raise IntegrityFailure(f"raw_state_hash_syntax:{spec.filename}:{index}")
        if HEX16_RE.fullmatch(sample["cache_hash"]) is None:
            raise IntegrityFailure(f"raw_cache_hash_syntax:{spec.filename}:{index}")
        flux_counts = [
            canonical_uint(sample[field], f"{spec.filename}_{index}_{field}")
            for field in FLUX_COUNT_FIELDS
        ]
        if sum(flux_counts) != expected_flux_total:
            raise IntegrityFailure(f"raw_flux_count_total:{spec.filename}:{index}")
        for value, count in enumerate(flux_counts):
            fraction = finite_float(
                sample[f"flux_fraction_{value}"],
                f"{spec.filename}_{index}_flux_fraction_{value}",
            )
            expected_fraction = count / expected_flux_total
            if abs(fraction - expected_fraction) > FRACTION_COUNT_TOLERANCE:
                raise IntegrityFailure(
                    f"raw_flux_fraction_count_mismatch:{spec.filename}:{index}:{value}"
                )

    diagnostics = parse_fields(lines[EXPECTED_SAMPLES + 1], "UPDATE_DIAGNOSTICS")
    expected_diagnostic_fields = {
        *(f"line_nonzero_{direction}" for direction in range(4)),
        "flat_cache_identity",
        "bit_cap_exhaustions",
        "max_prefix_bits",
        "local_decisions",
        "line_decisions",
        "flat_sheets",
        "charge_trials",
    }
    if set(diagnostics) != expected_diagnostic_fields:
        raise IntegrityFailure(f"raw_diagnostics_inventory:{spec.filename}")
    for direction in range(4):
        canonical_uint(diagnostics[f"line_nonzero_{direction}"], "line_nonzero")
    if diagnostics["flat_cache_identity"] != "PASS":
        raise IntegrityFailure(f"raw_flat_cache_identity:{spec.filename}")
    if canonical_uint(diagnostics["bit_cap_exhaustions"], "bit_cap_exhaustions") != 0:
        raise IntegrityFailure(f"raw_bit_cap_exhaustion:{spec.filename}")
    max_prefix = canonical_uint(diagnostics["max_prefix_bits"], "max_prefix_bits")
    if max_prefix > EXPECTED_BIT_CAP:
        raise IntegrityFailure(f"raw_max_prefix_bits:{spec.filename}:{max_prefix}")

    cycles = spec.total_cycles
    expected_counts = {
        "local_decisions": cycles * 4 * spec.linear_size**4,
        "line_decisions": cycles * 4 * spec.linear_size**3,
        "flat_sheets": cycles * 4,
        "charge_trials": cycles,
    }
    for field, expected in expected_counts.items():
        actual = canonical_uint(diagnostics[field], field)
        if actual != expected:
            raise IntegrityFailure(
                f"raw_decision_count:{spec.filename}:{field}:{actual}_expected_{expected}"
            )
    if lines[EXPECTED_SAMPLES + 2] != "KERNEL_STATUS PASS":
        raise IntegrityFailure(f"raw_kernel_status:{spec.filename}")
    if lines[EXPECTED_SAMPLES + 3] != "EVIDENTIAL_STATUS ZERO_PILOT_ONLY":
        raise IntegrityFailure(f"raw_evidential_status:{spec.filename}")


def verify_raw_custody(base: Path) -> tuple[tuple[Path, ...], str, int]:
    if tuple(spec.filename for spec in CHAINS) != LOG_NAMES:
        raise RuntimeError("internal_chain_order_mismatch")
    if TOTAL_HEATBATH_DECISIONS != 439_418_880:
        raise RuntimeError("internal_heatbath_decision_budget_mismatch")
    try:
        observed_logs = tuple(
            sorted(path.name for path in base.iterdir() if path.suffix == ".log")
        )
    except OSError as error:
        raise IntegrityFailure(
            f"raw_directory_inventory:{error.__class__.__name__}"
        ) from error
    if observed_logs != tuple(sorted(LOG_NAMES)):
        raise IntegrityFailure("raw_log_inventory_mismatch")
    manifest_data = require_regular_file(base / "PILOT_RUNS.tsv", "PILOT_RUNS.tsv")
    manifest_text = decode_ascii_lf(manifest_data, "PILOT_RUNS.tsv")
    lines = manifest_text.splitlines()
    if len(lines) != 1 + len(CHAINS) or lines[0] != MANIFEST_HEADER:
        raise IntegrityFailure("PILOT_RUNS_header_or_row_count")

    paths: list[Path] = []
    total_bytes = 0
    for row_index, (line, spec) in enumerate(zip(lines[1:], CHAINS), start=1):
        columns = line.split("\t")
        if len(columns) != 12:
            raise IntegrityFailure(f"PILOT_RUNS_column_count:{row_index}")
        (
            filename,
            linear_size,
            start,
            replica,
            seed,
            thermal,
            measurements,
            between,
            byte_count,
            digest,
            exit_code,
            stderr_bytes,
        ) = columns
        expected_prefix = (
            spec.filename,
            str(spec.linear_size),
            spec.start,
            str(spec.replica),
            f"0x{spec.seed:016x}",
            str(spec.thermal_cycles),
            str(spec.measurements),
            str(spec.between_cycles),
        )
        if tuple(columns[:8]) != expected_prefix:
            raise IntegrityFailure(f"PILOT_RUNS_schedule:{row_index}")
        if filename != LOG_NAMES[row_index - 1]:
            raise IntegrityFailure(f"PILOT_RUNS_filename_order:{row_index}")
        declared_bytes = canonical_uint(byte_count, f"manifest_bytes_{row_index}")
        if HEX64_RE.fullmatch(digest) is None:
            raise IntegrityFailure(f"PILOT_RUNS_sha256:{row_index}")
        if exit_code != "0" or stderr_bytes != "0":
            raise IntegrityFailure(f"PILOT_RUNS_process_custody:{row_index}")

        path = base / filename
        data = require_regular_file(path, filename)
        if len(data) != declared_bytes:
            raise IntegrityFailure(f"raw_byte_count:{filename}")
        if sha256_bytes(data) != digest:
            raise IntegrityFailure(f"raw_sha256:{filename}")
        validate_raw_log(spec, data)
        paths.append(path)
        total_bytes += len(data)
    return tuple(paths), sha256_bytes(manifest_data), total_bytes


def verify_analyzer_custody(base: Path, raw_paths: Sequence[Path]) -> tuple[bytes, str]:
    frozen = require_regular_file(base / "PILOT_ANALYSIS.txt", "PILOT_ANALYSIS.txt")
    decode_ascii_lf(frozen, "PILOT_ANALYSIS.txt")
    completed = run_python(base / "analyze_pilot.py", raw_paths)
    if completed.returncode != 0:
        raise IntegrityFailure(f"analyzer_exit:{completed.returncode}")
    if completed.stderr:
        raise IntegrityFailure("analyzer_stderr_nonempty")
    decode_ascii_lf(completed.stdout, "analyzer_stdout")
    if completed.stdout != frozen:
        raise IntegrityFailure("analyzer_stdout_custody_mismatch")

    lines = completed.stdout.decode("ascii").splitlines()
    result_lines = [line for line in lines if line.startswith("RESULT ")]
    if len(result_lines) != 1 or result_lines[0] != lines[-1]:
        raise IntegrityFailure("analyzer_terminal_grammar")
    terminal = result_lines[0].removeprefix("RESULT ")
    if terminal not in {
        "STOP_INTEGRITY",
        "STOP_MIXING",
        "PILOT_READY_FOR_PRODUCTION_PREREG",
    }:
        raise IntegrityFailure(f"analyzer_terminal_forbidden:{terminal}")
    return completed.stdout, terminal


def terminal_output(prefix_lines: Sequence[str], terminal: str) -> bytes:
    lines = [f"PILOT_VERIFY {PILOT_ID} V1", *prefix_lines, f"RESULT {terminal}"]
    return ("\n".join(lines) + "\n").encode("ascii")


def main(argv: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments:
        return usage()

    witness, exact_lines = independent_exact_local_audit()
    if witness is not None:
        emit(terminal_output(("EXACT_LOCAL_AUDIT status=BREAK", witness.line()), "BREAK_KERNEL"))
        return 0

    base = Path(__file__).resolve().parent
    status_lines = list(exact_lines)
    try:
        manifest_digest, pinned_count = verify_pin_manifest(base)
        status_lines.append(
            f"PINNED_INVENTORY files={pinned_count} sha256sums={manifest_digest} status=PASS"
        )

        reference_digest, reference_bytes = verify_reference_fixture(base)
        status_lines.append(
            f"REFERENCE_CHECK bytes={reference_bytes} sha256={reference_digest} status=PASS"
        )

        raw_paths, custody_digest, raw_bytes = verify_raw_custody(base)
        status_lines.append(
            "RAW_CUSTODY"
            f" logs={len(raw_paths)} samples={len(raw_paths) * EXPECTED_SAMPLES}"
            f" heatbath_decisions={TOTAL_HEATBATH_DECISIONS}"
            f" bytes={raw_bytes} manifest_sha256={custody_digest} status=PASS"
        )

        analyzer_stdout, analyzer_terminal = verify_analyzer_custody(base, raw_paths)
        status_lines.append(
            f"ANALYZER_CUSTODY bytes={len(analyzer_stdout)}"
            f" sha256={sha256_bytes(analyzer_stdout)} status=PASS"
        )
    except IntegrityFailure as error:
        status_lines.append(f"INTEGRITY_FAILURE reason={safe_token(str(error))}")
        emit(terminal_output(status_lines, "STOP_INTEGRITY"))
        return 0

    prefix = terminal_output(status_lines + ["ANALYZER_STDOUT_BEGIN"], "__PLACEHOLDER__")
    # Remove the placeholder terminal; append the frozen analyzer bytes and a
    # stable wrapper terminator without text-mode newline translation.
    placeholder = b"RESULT __PLACEHOLDER__\n"
    if not prefix.endswith(placeholder):
        raise RuntimeError("internal_output_assembly_failure")
    output = prefix[: -len(placeholder)]
    output += analyzer_stdout
    output += b"ANALYZER_STDOUT_END\n"
    output += f"RESULT {analyzer_terminal}\n".encode("ascii")
    emit(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
