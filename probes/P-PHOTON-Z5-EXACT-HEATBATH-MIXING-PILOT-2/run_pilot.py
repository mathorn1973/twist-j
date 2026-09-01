#!/usr/bin/env python3
"""One-shot data generator for the frozen second Z5 mixing pilot.

This one-shot program refuses to start when any decision artifact already
exists, validates the immutable source manifest, builds the accepted C++
source in a temporary directory, checks both frozen small-lattice fixtures,
runs exactly the eight registered chains, writes their custody manifest,
records the frozen analyzer output, and invokes the accepted ``verify.py``
exactly once.  Its captured stdout becomes ``EXPECTED.txt``.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile


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

MODELED_STOP_EXPECTED = (
    b"KERNEL_STATUS STOP_INTEGRITY\n"
    b"INTEGRITY_REASON value=STOP_INTEGRITY_modeled_cap_fixture\n"
    b"EVIDENTIAL_STATUS ZERO_PILOT_ONLY\n"
)


@dataclass(frozen=True)
class ChainSpec:
    filename: str
    L: int
    start: str
    replica: int
    seed: int
    thermal: int
    measurements: int
    between: int


@dataclass(frozen=True)
class ChainResult:
    spec: ChainSpec
    stdout: bytes
    stderr: bytes
    returncode: int


CHAINS = tuple(
    ChainSpec(
        filename=f"L{L}_{start}_r{replica}.log",
        L=L,
        start=start,
        replica=replica,
        seed=(0xE755060000000000 if L == 6 else 0xE755080000000000)
        + (0x100 if start == "cold" else 0x200)
        + replica,
        thermal=512 if L == 6 else 1024,
        measurements=512,
        between=4 if L == 6 else 8,
    )
    for L in (6, 8)
    for start in ("cold", "hot")
    for replica in (1, 2)
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str, code: int = 2) -> int:
    print(f"DRIVER_ERROR {message}", file=sys.stderr)
    return code


def parse_pin_manifest(base: Path) -> None:
    manifest = base / "SHA256SUMS"
    try:
        raw = manifest.read_bytes()
    except OSError as error:
        raise RuntimeError(f"cannot_read_SHA256SUMS:{error.__class__.__name__}") from error
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise RuntimeError("SHA256SUMS_not_LF_final_newline")
    entries: dict[str, str] = {}
    for line in raw.decode("ascii").splitlines():
        parts = line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64:
            raise RuntimeError("SHA256SUMS_malformed")
        digest, name = parts
        if name in entries or any(ch not in "0123456789abcdef" for ch in digest):
            raise RuntimeError("SHA256SUMS_malformed")
        entries[name] = digest
    if tuple(entries) != PINNED_FILES:
        raise RuntimeError("SHA256SUMS_inventory_or_order_mismatch")
    for name, expected in entries.items():
        path = base / name
        try:
            actual = sha256(path.read_bytes())
        except OSError as error:
            raise RuntimeError(f"cannot_read_pinned_file:{name}") from error
        if actual != expected:
            raise RuntimeError(f"pinned_hash_mismatch:{name}")


def require_frozen_output(label: str, completed: subprocess.CompletedProcess[bytes], expected: bytes) -> None:
    if completed.returncode != 0:
        raise RuntimeError(f"{label}_exit_{completed.returncode}")
    if completed.stderr:
        raise RuntimeError(f"{label}_stderr_nonempty")
    if completed.stdout != expected:
        raise RuntimeError(f"{label}_stdout_mismatch")


def run_chain(binary: Path, spec: ChainSpec) -> ChainResult:
    command = (
        str(binary),
        "--pilot",
        "--L",
        str(spec.L),
        "--seed",
        f"0x{spec.seed:016x}",
        "--start",
        spec.start,
        "--replica",
        str(spec.replica),
        "--thermal-cycles",
        str(spec.thermal),
        "--measurements",
        str(spec.measurements),
        "--between-cycles",
        str(spec.between),
        "--t",
        "1",
    )
    completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return ChainResult(spec, completed.stdout, completed.stderr, completed.returncode)


def validate_log_bytes(result: ChainResult) -> None:
    data = result.stdout
    if result.returncode != 0:
        raise RuntimeError(f"{result.spec.filename}_exit_{result.returncode}")
    if result.stderr:
        raise RuntimeError(f"{result.spec.filename}_stderr_nonempty")
    if len(data) > 5 * 1024 * 1024:
        raise RuntimeError(f"{result.spec.filename}_over_5MiB")
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"{result.spec.filename}_not_LF_final_newline")
    try:
        data.decode("ascii")
    except UnicodeDecodeError as error:
        raise RuntimeError(f"{result.spec.filename}_not_ASCII") from error


def custody_row(result: ChainResult) -> str:
    spec = result.spec
    return "\t".join(
        (
            spec.filename,
            str(spec.L),
            spec.start,
            str(spec.replica),
            f"0x{spec.seed:016x}",
            str(spec.thermal),
            str(spec.measurements),
            str(spec.between),
            str(len(result.stdout)),
            sha256(result.stdout),
            str(result.returncode),
            str(len(result.stderr)),
        )
    )


def main() -> int:
    if len(sys.argv) != 1:
        return fail("usage: python3 run_pilot.py", 64)
    base = Path(__file__).resolve().parent
    repository_root = base.parent.parent

    try:
        expected_pre_run = set(PINNED_FILES) | {"SHA256SUMS"}
        observed_pre_run = {path.name for path in base.iterdir()}
        if observed_pre_run != expected_pre_run:
            missing = sorted(expected_pre_run - observed_pre_run)
            extra = sorted(observed_pre_run - expected_pre_run)
            details = []
            if missing:
                details.append("missing=" + ",".join(missing))
            if extra:
                details.append("extra=" + ",".join(extra))
            raise RuntimeError("pre_run_inventory_mismatch:" + ";".join(details))
        nonregular = sorted(
            name
            for name in expected_pre_run
            if (base / name).is_symlink() or not (base / name).is_file()
        )
        if nonregular:
            raise RuntimeError("pre_run_nonregular_entry:" + ",".join(nonregular))
        parse_pin_manifest(base)
        if tuple(spec.filename for spec in CHAINS) != LOG_NAMES:
            raise RuntimeError("internal_chain_order_mismatch")

        with tempfile.TemporaryDirectory(prefix="photon-z5-pilot-2-") as temporary:
            binary = Path(temporary) / "photon_z5"
            compile_command = (
                "g++",
                "-std=c++20",
                "-O3",
                "-DNDEBUG",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                str(base / "photon_z5.cpp"),
                "-o",
                str(binary),
            )
            built = subprocess.run(
                compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
            )
            if built.returncode != 0:
                sys.stderr.buffer.write(built.stderr)
                raise RuntimeError(f"compile_exit_{built.returncode}")
            if built.stdout or built.stderr:
                raise RuntimeError("compile_output_nonempty")

            self_test = subprocess.run(
                (str(binary), "--self-test"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            require_frozen_output(
                "selftest", self_test, (base / "SELFTEST_EXPECTED.txt").read_bytes()
            )

            modeled_stop = subprocess.run(
                (str(binary), "--stop-integrity-fixture"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            require_frozen_output("modeled_stop", modeled_stop, MODELED_STOP_EXPECTED)

            cpp_fixture = subprocess.run(
                (str(binary), "--fixture"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            require_frozen_output(
                "cpp_fixture",
                cpp_fixture,
                (base / "REFERENCE_EXPECTED.txt").read_bytes(),
            )

            reference = subprocess.run(
                (
                    sys.executable,
                    str(base / "reference_check.py"),
                    "--cpp",
                    str(binary),
                ),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                cwd=base,
            )
            require_frozen_output(
                "reference", reference, (base / "REFERENCE_EXPECTED.txt").read_bytes()
            )

            results: dict[str, ChainResult] = {}
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = {executor.submit(run_chain, binary, spec): spec for spec in CHAINS}
                for future in as_completed(futures):
                    result = future.result()
                    results[result.spec.filename] = result
                    print(f"CHAIN_COMPLETE {result.spec.filename}", flush=True)

        ordered = [results[name] for name in LOG_NAMES]
        for result in ordered:
            validate_log_bytes(result)

        for result in ordered:
            (base / result.spec.filename).write_bytes(result.stdout)
        manifest_text = MANIFEST_HEADER + "\n" + "\n".join(custody_row(item) for item in ordered) + "\n"
        (base / "PILOT_RUNS.tsv").write_bytes(manifest_text.encode("ascii"))

        analyzer = subprocess.run(
            (
                sys.executable,
                str(base / "analyze_pilot.py"),
                *(str(base / name) for name in LOG_NAMES),
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            cwd=base,
        )
        if analyzer.returncode != 0:
            sys.stderr.buffer.write(analyzer.stderr)
            raise RuntimeError(f"analyzer_exit_{analyzer.returncode}")
        if analyzer.stderr:
            raise RuntimeError("analyzer_stderr_nonempty")
        if b"\r" in analyzer.stdout or not analyzer.stdout.endswith(b"\n"):
            raise RuntimeError("analyzer_not_LF_final_newline")
        analyzer.stdout.decode("ascii")
        (base / "PILOT_ANALYSIS.txt").write_bytes(analyzer.stdout)

        formal = subprocess.run(
            (
                "python3",
                (base / "verify.py").relative_to(repository_root).as_posix(),
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            cwd=repository_root,
        )
        if formal.returncode != 0:
            sys.stderr.buffer.write(formal.stderr)
            raise RuntimeError(f"formal_verifier_exit_{formal.returncode}")
        if formal.stderr:
            raise RuntimeError("formal_verifier_stderr_nonempty")
        if b"\r" in formal.stdout or not formal.stdout.endswith(b"\n"):
            raise RuntimeError("formal_verifier_not_LF_final_newline")
        formal.stdout.decode("ascii")
        (base / "EXPECTED.txt").write_bytes(formal.stdout)
        print("DRIVER_RESULT COMPLETE_EIGHT_LOGS_ANALYSIS_AND_EXPECTED")
        return 0
    except (OSError, RuntimeError, UnicodeError, subprocess.SubprocessError) as error:
        return fail(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
