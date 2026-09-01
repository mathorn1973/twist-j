#!/usr/bin/env python3
"""One-shot orchestrator for the frozen zero-evidence #756 execution."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import hashlib
import importlib.util
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile


PINNED_FILES = (
    "PREREG.md",
    "CROSSCHECK_PIN.md",
    "README.md",
    "primal_replay.cpp",
    "dual_chain.py",
    "analyze_crosscheck.py",
    "run_crosscheck.py",
    "verify.py",
    "FIXTURE_EXPECTED.txt",
)

PRIMAL_SPECS = (
    ("primal_L6_cold_r1.log", 6, "cold", 0xE755060000000101, 512, 4),
    ("primal_L6_hot_r1.log", 6, "hot", 0xE755060000000201, 512, 4),
    ("primal_L8_cold_r1.log", 8, "cold", 0xE755080000000101, 1024, 8),
    ("primal_L8_hot_r1.log", 8, "hot", 0xE755080000000201, 1024, 8),
)

DUAL_SPECS = tuple(
    (
        f"dual_L{L}_{start}_r{replica}.jsonl",
        L,
        start,
        (0xE756060000000000 if L == 6 else 0xE756080000000000)
        + (0x100 if start == "cold" else 0x200)
        + replica,
        663552 if L == 6 else 2097152,
        2592 if L == 6 else 8192,
    )
    for L in (6, 8)
    for start in ("cold", "surface")
    for replica in (1, 2)
)

POST_RUN = (
    *(item[0] for item in PRIMAL_SPECS),
    *(item[0] for item in DUAL_SPECS),
    "PRIMAL_RUNS.tsv",
    "DUAL_RUNS.tsv",
    "OUTPUT_SHA256SUMS",
    "ANALYSIS.txt",
    "EXPECTED.txt",
    "RUN.md",
    "RESULT.md",
)


@dataclass(frozen=True)
class Result:
    name: str
    stdout: bytes
    stderr: bytes
    returncode: int


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_manifest(
    base: Path,
    manifest_name: str,
    local_only: bool,
    expected_names: tuple[str, ...],
) -> None:
    path = base / manifest_name
    raw = path.read_bytes()
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise RuntimeError(f"{manifest_name}_newlines")
    entries: list[tuple[str, str]] = []
    for line in raw.decode("ascii").splitlines():
        parts = line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64:
            raise RuntimeError(f"{manifest_name}_malformed")
        digest, name = parts
        if any(char not in "0123456789abcdef" for char in digest):
            raise RuntimeError(f"{manifest_name}_digest")
        if any(existing == name for _, existing in entries):
            raise RuntimeError(f"{manifest_name}_duplicate")
        entries.append((digest, name))
    if tuple(name for _, name in entries) != expected_names:
        raise RuntimeError(f"{manifest_name}_inventory")
    repository_root = base.parent.parent
    for expected, name in entries:
        target = (base / name) if local_only else (repository_root / name)
        if not target.is_file() or target.is_symlink():
            raise RuntimeError(f"{manifest_name}_nonregular:{name}")
        if sha256(target.read_bytes()) != expected:
            raise RuntimeError(f"{manifest_name}_mismatch:{name}")


def verifier_input_files(base: Path) -> tuple[str, ...]:
    """Load the pinned verifier's authoritative external-input inventory."""

    path = base / "verify.py"
    spec = importlib.util.spec_from_file_location("dual_ward_pin_verify", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot_load_verify_input_inventory")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    inventory = getattr(module, "INPUT_FILES", None)
    if (
        not isinstance(inventory, tuple)
        or not inventory
        or any(not isinstance(name, str) or not name for name in inventory)
        or len(set(inventory)) != len(inventory)
    ):
        raise RuntimeError("verify_INPUT_FILES_invalid")
    return inventory


def formal_runtime_preflight(base: Path) -> None:
    """Refuse every host/runtime outside the preregistered formal envelope."""

    if Path.cwd().resolve() != base:
        raise RuntimeError("formal_cwd_must_equal_package_base")
    if sys.platform != "linux" or platform.system() != "Linux":
        raise RuntimeError("formal_platform_must_be_Linux")
    if platform.machine() != "x86_64":
        raise RuntimeError("formal_architecture_must_be_x86_64")
    if platform.python_implementation() != "CPython":
        raise RuntimeError("formal_python_must_be_CPython")
    if sys.version_info[:3] != (3, 10, 12):
        raise RuntimeError("formal_python_version_must_be_3.10.12")

    compiler = subprocess.run(
        ("g++", "-dumpfullversion", "-dumpversion"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        cwd=base,
    )
    if compiler.returncode != 0 or compiler.stderr:
        raise RuntimeError("formal_gxx_version_probe_failed")
    if compiler.stdout != b"11.4.0\n":
        raise RuntimeError("formal_gxx_version_must_be_11.4.0")

    boost_probe = subprocess.run(
        ("g++", "-std=c++20", "-x", "c++", "-fsyntax-only", "-"),
        input=(
            b"#include <boost/version.hpp>\n"
            b"#if BOOST_VERSION != 107400\n"
            b"#error unexpected_BOOST_VERSION\n"
            b"#endif\n"
            b"int main() { return 0; }\n"
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        cwd=base,
    )
    if boost_probe.returncode != 0 or boost_probe.stdout or boost_probe.stderr:
        raise RuntimeError("formal_BOOST_VERSION_must_be_107400")


def validate_output(result: Result, suffix: str) -> None:
    if result.returncode != 0:
        raise RuntimeError(f"{result.name}_exit_{result.returncode}")
    if result.stderr:
        raise RuntimeError(f"{result.name}_stderr_nonempty")
    if len(result.stdout) > 5 * 1024 * 1024:
        raise RuntimeError(f"{result.name}_over_5MiB")
    if b"\r" in result.stdout or not result.stdout.endswith(b"\n"):
        raise RuntimeError(f"{result.name}_newlines")
    result.stdout.decode("ascii")
    if not result.name.endswith(suffix):
        raise RuntimeError(f"{result.name}_suffix")


def run_primal(binary: Path, spec: tuple[object, ...]) -> Result:
    name, L, start, seed, thermal, between = spec
    completed = subprocess.run(
        (
            str(binary),
            "--L", str(L),
            "--seed", f"0x{seed:016x}",
            "--start", str(start),
            "--thermal", str(thermal),
            "--samples", "512",
            "--between", str(between),
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return Result(str(name), completed.stdout, completed.stderr, completed.returncode)


def run_dual(base: Path, spec: tuple[object, ...]) -> Result:
    name, L, start, seed, thermal, between = spec
    completed = subprocess.run(
        (
            sys.executable,
            "-B",
            str(base / "dual_chain.py"),
            "decision",
            "--L", str(L),
            "--seed", f"0x{seed:016x}",
            "--start", str(start),
            "--thermal", str(thermal),
            "--samples", "512",
            "--between", str(between),
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        cwd=base,
    )
    return Result(str(name), completed.stdout, completed.stderr, completed.returncode)


def manifest_row(result: Result, spec: tuple[object, ...], kind: str) -> str:
    name, L, start, seed, thermal, between = spec
    return "\t".join(
        (
            str(name),
            kind,
            str(L),
            str(start),
            f"0x{seed:016x}",
            str(thermal),
            "512",
            str(between),
            str(len(result.stdout)),
            sha256(result.stdout),
            str(result.returncode),
            str(len(result.stderr)),
        )
    )


def main() -> int:
    if len(sys.argv) != 1:
        print("DRIVER_ERROR usage: python3 run_crosscheck.py", file=sys.stderr)
        return 64
    base = Path(__file__).resolve().parent
    try:
        formal_runtime_preflight(base)
        observed = {path.name for path in base.iterdir()}
        expected = set(PINNED_FILES) | {"SOURCE_SHA256SUMS", "INPUT_SHA256SUMS"}
        if observed != expected:
            raise RuntimeError(
                "pre_run_inventory:" +
                f"missing={','.join(sorted(expected-observed))}:" +
                f"extra={','.join(sorted(observed-expected))}"
            )
        if any((base / name).exists() for name in POST_RUN):
            raise RuntimeError("pre_existing_decision_artifact")
        parse_manifest(base, "SOURCE_SHA256SUMS", True, PINNED_FILES)
        parse_manifest(
            base,
            "INPUT_SHA256SUMS",
            False,
            verifier_input_files(base),
        )

        environment = os.environ.copy()
        for key, value in (
            ("LC_ALL", "C"),
            ("LANG", "C"),
            ("TZ", "UTC"),
            ("PYTHONDONTWRITEBYTECODE", "1"),
            ("PYTHONHASHSEED", "0"),
        ):
            if environment.get(key) != value:
                raise RuntimeError(f"environment_{key}")

        fixture = subprocess.run(
            (sys.executable, "-B", str(base / "verify.py"), "--fixture"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            cwd=base,
            env=environment,
        )
        if fixture.returncode or fixture.stderr:
            raise RuntimeError("fixture_process_failure")
        if fixture.stdout != (base / "FIXTURE_EXPECTED.txt").read_bytes():
            raise RuntimeError("fixture_stdout_mismatch")

        with tempfile.TemporaryDirectory(prefix="photon-z5-dual-ward-") as temporary:
            binary = Path(temporary) / "primal_replay"
            compile_result = subprocess.run(
                (
                    "g++", "-std=c++20", "-O3", "-DNDEBUG", "-Wall",
                    "-Wextra", "-Wpedantic", str(base / "primal_replay.cpp"),
                    "-o", str(binary),
                ),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                env=environment,
            )
            if compile_result.returncode or compile_result.stdout or compile_result.stderr:
                sys.stderr.buffer.write(compile_result.stderr)
                raise RuntimeError("primal_compile_failure")

            primal_results: dict[str, Result] = {}
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = {
                    executor.submit(run_primal, binary, spec): spec
                    for spec in PRIMAL_SPECS
                }
                for future in as_completed(futures):
                    result = future.result()
                    primal_results[result.name] = result
                    print(f"PRIMAL_COMPLETE {result.name}", flush=True)

        ordered_primal = [primal_results[str(spec[0])] for spec in PRIMAL_SPECS]
        for result in ordered_primal:
            validate_output(result, ".log")

        dual_results: dict[str, Result] = {}
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(run_dual, base, spec): spec for spec in DUAL_SPECS
            }
            for future in as_completed(futures):
                result = future.result()
                dual_results[result.name] = result
                print(f"DUAL_COMPLETE {result.name}", flush=True)
        ordered_dual = [dual_results[str(spec[0])] for spec in DUAL_SPECS]
        for result in ordered_dual:
            validate_output(result, ".jsonl")

        for result in (*ordered_primal, *ordered_dual):
            (base / result.name).write_bytes(result.stdout)

        header = (
            "filename\tkind\tL\tstart\tseed\tthermal\tmeasurements\tbetween"
            "\tbytes\tsha256\texit_code\tstderr_bytes\n"
        )
        primal_manifest = header + "\n".join(
            manifest_row(result, spec, "primal_replay")
            for result, spec in zip(ordered_primal, PRIMAL_SPECS)
        ) + "\n"
        dual_manifest = header + "\n".join(
            manifest_row(result, spec, "dual_independent")
            for result, spec in zip(ordered_dual, DUAL_SPECS)
        ) + "\n"
        (base / "PRIMAL_RUNS.tsv").write_bytes(primal_manifest.encode("ascii"))
        (base / "DUAL_RUNS.tsv").write_bytes(dual_manifest.encode("ascii"))

        analysis = subprocess.run(
            (sys.executable, "-B", str(base / "analyze_crosscheck.py")),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            cwd=base,
            env=environment,
        )
        if analysis.returncode or analysis.stderr:
            raise RuntimeError("analysis_process_failure")
        if b"\r" in analysis.stdout or not analysis.stdout.endswith(b"\n"):
            raise RuntimeError("analysis_newlines")
        analysis.stdout.decode("ascii")
        (base / "ANALYSIS.txt").write_bytes(analysis.stdout)

        output_names = (
            *(result.name for result in ordered_primal),
            *(result.name for result in ordered_dual),
            "PRIMAL_RUNS.tsv",
            "DUAL_RUNS.tsv",
            "ANALYSIS.txt",
        )
        output_manifest = "".join(
            f"{sha256((base/name).read_bytes())}  {name}\n" for name in output_names
        )
        (base / "OUTPUT_SHA256SUMS").write_bytes(output_manifest.encode("ascii"))

        formal = subprocess.run(
            (sys.executable, "-B", str(base / "verify.py")),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            cwd=base,
            env=environment,
        )
        if formal.returncode or formal.stderr:
            raise RuntimeError("formal_verifier_process_failure")
        if b"\r" in formal.stdout or not formal.stdout.endswith(b"\n"):
            raise RuntimeError("formal_verifier_newlines")
        formal.stdout.decode("ascii")
        (base / "EXPECTED.txt").write_bytes(formal.stdout)
        print("DRIVER_RESULT COMPLETE_ZERO_EVIDENCE_CROSSCHECK", flush=True)
        return 0
    except (OSError, RuntimeError, UnicodeError, subprocess.SubprocessError) as error:
        print(f"DRIVER_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
