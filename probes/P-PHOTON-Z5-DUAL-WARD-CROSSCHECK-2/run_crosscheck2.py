#!/usr/bin/env python3
"""One-shot pinned runner for P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2.

Formal execution claims both immutable attempt refs before compilation or any
L6/L8 state.  The full engine stream is pumped directly into the pinned state
reader and is never a filesystem artifact.  ``--fixture`` opens only the
frozen L3/L4 development fixture and no formal seed.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import signal
import subprocess
import sys
import threading
import time
from types import ModuleType
from typing import Iterator, Sequence


PROBE_ID = "P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2"
BRANCH = "probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2"
PUBLIC_BASE = "d0bc920b27117ea4a409282e3481340f50433763"
RESERVATION_ANCHOR = "072113d6a22fccef6468d2d647d006c262b6bf2d"
PUBLIC_REMOTE = "https://github.com/mathorn1973/twist-j.git"
PUBLIC_OWNER = "mathorn1973"
RESERVATION_COMMENT_ID = "5498022449"
GOVERNANCE_COMMENT_ID = "5497635560"
ATTEMPT_REF = f"refs/probe-attempts/{PROBE_ID}"
PUBLIC_ATTEMPT_REF = f"refs/heads/probe-attempts/{PROBE_ID}"
ZERO_OID = "0" * 40
BUILD_DIRECTORY = ".photon-z5-dual-ward-crosscheck-2-build"
SUPERVISOR_SECONDS = 172_800
FINAL_DUAL_CAP = 5_000_000
READER_RAW_TOTAL_CAP = 100_000_000
READER_RAW_LINE_CAP = 262_144
PRIMAL_CAP = 1_048_576
STDERR_CAP = 1_048_576
ANALYSIS_CAP = 4_194_304
ISSUE_RECEIPT_RE = re.compile(
    r"https://github\.com/mathorn1973/twist-j/issues/756#issuecomment-[0-9]+\Z"
)
LOWER_HEX40_RE = re.compile(r"[0-9a-f]{40}\Z")

SOURCE_FILES = (
    "PREREG.md",
    "CROSSCHECK_PIN.md",
    "README.md",
    "primal_replay.cpp",
    "crosscheck2_engine.cpp",
    "state_reader.py",
    "analyze_crosscheck2.py",
    "engine_fixture.py",
    "reader_fixture.py",
    "run_crosscheck2.py",
    "verify.py",
    "FIXTURE_EXPECTED.txt",
)
PIN_COMMIT_FILES = SOURCE_FILES + ("SOURCE_SHA256SUMS", "INPUT_SHA256SUMS")


@dataclass(frozen=True)
class PrimalSpec:
    name: str
    L: int
    start: str
    seed: int
    thermal: int
    between: int
    expected_bytes: int
    expected_sha256: str

    @property
    def seed_token(self) -> str:
        return f"0x{self.seed:016x}"


PRIMAL_SPECS = (
    PrimalSpec(
        "primal_L6_cold_r1.log", 6, "cold", 0xE755060000000101, 512, 4,
        265_645, "607b9d73b6b24a6a8c22375ecb6de6c1aedc5c6cd512f642ea40fe12b327043b",
    ),
    PrimalSpec(
        "primal_L6_hot_r1.log", 6, "hot", 0xE755060000000201, 512, 4,
        265_613, "6d981042cd9f94d3450d53705b5c85b834f2d3ac8083709cb8e2cd94a63d6d2f",
    ),
    PrimalSpec(
        "primal_L8_cold_r1.log", 8, "cold", 0xE755080000000101, 1024, 8,
        267_498, "0c0c180d0953bfaeaa2eb99b1f11f253bc07048eb2e7a70f99f6f30c3a6b7f87",
    ),
    PrimalSpec(
        "primal_L8_hot_r1.log", 8, "hot", 0xE755080000000201, 1024, 8,
        267_532, "645cb1d3d6992d585ed0903a3e28f72f226572ae0732fbc728b69244adf8e0b5",
    ),
)


@dataclass(frozen=True)
class DualSpec:
    name: str
    label: str
    L: int
    start: str
    replica: int
    seed: int
    seed_sha256: str
    warm_bottom: int
    checkpoints: int
    thin: int
    validation_stride: int
    transition_cap: int
    engine_pipe_cap: int

    @property
    def seed_token(self) -> str:
        return f"0x{self.seed:032x}"

    @property
    def seed_preimage(self) -> str:
        return (
            f"{PROBE_ID}|{RESERVATION_ANCHOR}|L={self.L}|"
            f"start={self.start}|replica={self.replica}"
        )


SEED_HASHES = {
    (6, "cold", 1): "bc2def7bcee975913c3b3b3999e83ad3ec5a159fe7bf5775c0ace3824a35b219",
    (6, "cold", 2): "1a7ab1ad0011b62c04dcf48da9be340377e3f0b9a21a8e5b28eb98daaf6c2654",
    (6, "stratified", 1): "5f0f36673dd145755b9a49e703aef3d6cfe3ca5bb474ccc6e106fb8b6cdc9ee8",
    (6, "stratified", 2): "2b19daecb5c523f30bee3be7c047eb40d3ff106b7fd941c9b6d0d840c766a8b2",
    (8, "cold", 1): "46ba01f80aec780ff9cc8b7e876c700c2dfe2457398c867cf91dc27ca64bf013",
    (8, "cold", 2): "2e0ccaa683e5f39f1237f05193b299c409fe2ebb85994aedcd00db4969cd1d31",
    (8, "stratified", 1): "f8f631709b4b9ce34f8a658bef3e1d0a678c2fa4e138bd6e7d0d556752ced23a",
    (8, "stratified", 2): "fcd563ecc8bf8179b96c20db2c388307235ed3ee622912f209065bd192200c21",
}


def _make_dual_spec(L: int, start: str, replica: int) -> DualSpec:
    digest = SEED_HASHES[(L, start, replica)]
    preimage = (
        f"{PROBE_ID}|{RESERVATION_ANCHOR}|L={L}|"
        f"start={start}|replica={replica}"
    )
    observed = hashlib.sha256(preimage.encode("ascii")).hexdigest()
    if observed != digest:
        raise RuntimeError(f"seed_derivation_source_mismatch:L{L}:{start}:r{replica}")
    if L == 6:
        warm, thin, cap, pipe_cap = 98_304, 1_536, 1_073_741_824, 8_388_608
    elif L == 8:
        warm, thin, cap, pipe_cap = 262_144, 4_096, 4_294_967_296, 20_971_520
    else:
        raise AssertionError("unreachable L")
    return DualSpec(
        name=f"dual_L{L}_{start}_r{replica}.jsonl",
        label=f"L{L}_{start}_r{replica}",
        L=L,
        start=start,
        replica=replica,
        seed=int(digest[:32], 16),
        seed_sha256=digest,
        warm_bottom=warm,
        checkpoints=2_048,
        thin=thin,
        validation_stride=thin,
        transition_cap=cap,
        engine_pipe_cap=pipe_cap,
    )


DUAL_SPECS = tuple(
    _make_dual_spec(L, start, replica)
    for L in (6, 8)
    for start in ("cold", "stratified")
    for replica in (1, 2)
)

# This fixed queue order gives the four-worker supervisor two L6 and two L8
# jobs at launch without changing canonical transcript/manifest order.
DUAL_EXECUTION_ORDER = tuple(
    next(
        spec for spec in DUAL_SPECS
        if spec.L == L and spec.start == start and spec.replica == replica
    )
    for start in ("cold", "stratified")
    for replica in (1, 2)
    for L in (8, 6)
)

PRIMAL_OUTPUTS = tuple(spec.name for spec in PRIMAL_SPECS)
DUAL_OUTPUTS = tuple(spec.name for spec in DUAL_SPECS)
OUTPUT_FILES = PRIMAL_OUTPUTS + DUAL_OUTPUTS + (
    "PRIMAL_RUNS.tsv",
    "DUAL_RUNS.tsv",
    "ANALYSIS.txt",
)
POST_RUN_FILES = OUTPUT_FILES + (
    "OUTPUT_SHA256SUMS",
    "EXPECTED.txt",
    "RUN.md",
    "RESULT.md",
)
ALLOWED_TERMINALS = {
    "DUAL_CROSSCHECK_PASS",
    "STOP_DUAL_MIXING",
    "STOP_DUAL_INTEGRITY",
    "BREAK_DUAL_DICTIONARY",
}


@dataclass(frozen=True)
class ProcessResult:
    name: str
    stdout: bytes
    stderr: bytes
    returncode: int


@dataclass(frozen=True)
class PipelineResult:
    name: str
    stdout: bytes
    engine_stderr: bytes
    reader_stderr: bytes
    engine_returncode: int
    reader_returncode: int
    engine_pipe_bytes: int
    engine_pipe_sha256: str


class PreflightError(RuntimeError):
    """A source, environment, execution or custody condition failed."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise PreflightError(f"cannot_load_module:{name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def strict_text(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise PreflightError(f"nonregular:{path}")
    raw = path.read_bytes()
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise PreflightError(f"newline_contract:{path.name}")
    try:
        raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise PreflightError(f"nonascii:{path.name}") from error
    return raw


def write_exclusive(path: Path, data: bytes) -> None:
    if path.is_symlink() or path.exists():
        raise PreflightError(f"exclusive_output_exists:{path.name}")
    with path.open("xb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def parse_manifest(
    manifest: Path,
    root: Path,
    expected_names: Sequence[str],
) -> str:
    raw = strict_text(manifest)
    entries: list[tuple[str, str]] = []
    for line in raw.decode("ascii").splitlines():
        parts = line.split("  ", 1)
        if len(parts) != 2 or re.fullmatch(r"[0-9a-f]{64}", parts[0]) is None:
            raise PreflightError(f"malformed_manifest:{manifest.name}")
        if any(name == parts[1] for _, name in entries):
            raise PreflightError(f"duplicate_manifest_entry:{manifest.name}:{parts[1]}")
        entries.append((parts[0], parts[1]))
    if tuple(name for _, name in entries) != tuple(expected_names):
        raise PreflightError(f"manifest_inventory:{manifest.name}")
    for expected, name in entries:
        target = root / name
        if target.is_symlink() or not target.is_file():
            raise PreflightError(f"manifest_nonregular:{manifest.name}:{name}")
        if sha256(target.read_bytes()) != expected:
            raise PreflightError(f"manifest_mismatch:{manifest.name}:{name}")
    return sha256(raw)


def verifier_input_files(base: Path) -> tuple[str, ...]:
    module = load_module("crosscheck2_verify_inventory", base / "verify.py")
    inventory = getattr(module, "INPUT_FILES", None)
    if (
        not isinstance(inventory, tuple)
        or not inventory
        or any(not isinstance(name, str) or not name for name in inventory)
        or len(set(inventory)) != len(inventory)
    ):
        raise PreflightError("verify_INPUT_FILES_invalid")
    return inventory


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


def formal_runtime_preflight(repository_root: Path) -> None:
    if sys.platform != "linux" or platform.system() != "Linux":
        raise PreflightError("formal_platform_must_be_Linux")
    if platform.machine() != "x86_64":
        raise PreflightError("formal_architecture_must_be_x86_64")
    try:
        release = platform.freedesktop_os_release()
    except OSError as error:
        raise PreflightError("formal_os_release_unavailable") from error
    if (
        release.get("ID") != "ubuntu"
        or release.get("VERSION_ID") != "22.04"
        or release.get("PRETTY_NAME") != "Ubuntu 22.04.5 LTS"
    ):
        raise PreflightError("formal_platform_must_be_Ubuntu_22.04.5_LTS")
    if platform.python_implementation() != "CPython":
        raise PreflightError("formal_python_must_be_CPython")
    if sys.version_info[:3] != (3, 10, 12):
        raise PreflightError("formal_python_version_must_be_3.10.12")
    for key, value in (
        ("LC_ALL", "C"),
        ("LANG", "C"),
        ("TZ", "UTC"),
        ("PYTHONDONTWRITEBYTECODE", "1"),
        ("PYTHONHASHSEED", "0"),
    ):
        if os.environ.get(key) != value:
            raise PreflightError(f"formal_environment_{key}")

    # Compiler and Boost probes are intentionally deferred until after both
    # attempt refs have been atomically claimed and publicly read back.


def formal_toolchain_preflight(repository_root: Path, deadline: float) -> None:
    compiler = bounded_process(
        ("g++", "-dumpfullversion", "-dumpversion"),
        cwd=repository_root,
        max_stdout=4_096,
        max_stderr=4_096,
        timeout=remaining_seconds(deadline),
    )
    if compiler.returncode or compiler.stderr or compiler.stdout != b"11.4.0\n":
        raise PreflightError("formal_gxx_version_must_be_11.4.0")

    boost = bounded_process(
        ("g++", "-std=c++20", "-x", "c++", "-fsyntax-only", "-"),
        input_bytes=(
            b"#include <boost/version.hpp>\n"
            b"#if BOOST_VERSION != 107400\n"
            b"#error unexpected_BOOST_VERSION\n"
            b"#endif\n"
            b"int main() { return 0; }\n"
        ),
        cwd=repository_root,
        max_stdout=65_536,
        max_stderr=65_536,
        timeout=remaining_seconds(deadline),
    )
    if boost.returncode or boost.stdout or boost.stderr:
        raise PreflightError("formal_BOOST_VERSION_must_be_107400")


def formal_cli_preflight(repository_root: Path) -> None:
    git_version = bounded_process(
        ("git", "--version"),
        cwd=repository_root,
        max_stdout=4_096,
        max_stderr=4_096,
        timeout=60,
    )
    if (
        git_version.returncode
        or git_version.stderr
        or git_version.stdout != b"git version 2.34.1\n"
    ):
        raise PreflightError("formal_git_version_must_be_2.34.1")

    gh_version = bounded_process(
        ("gh", "--version"),
        cwd=repository_root,
        max_stdout=65_536,
        max_stderr=4_096,
        timeout=60,
    )
    if (
        gh_version.returncode
        or gh_version.stderr
        or gh_version.stdout.splitlines()[:1]
        != [b"gh version 2.4.0+dfsg1 (2022-03-23 Ubuntu 2.4.0+dfsg1-2)"]
    ):
        raise PreflightError("formal_gh_version_must_be_Ubuntu_2.4.0_dfsg1")

    auth = bounded_process(
        ("gh", "auth", "status", "--hostname", "github.com"),
        cwd=repository_root,
        max_stdout=65_536,
        max_stderr=65_536,
        timeout=60,
    )
    if auth.returncode:
        raise PreflightError("formal_gh_auth_status_failed")
    identity = bounded_process(
        ("gh", "api", "--hostname", "github.com", "user", "--jq", ".login"),
        cwd=repository_root,
        max_stdout=4_096,
        max_stderr=65_536,
        timeout=60,
    )
    if identity.returncode or identity.stderr or identity.stdout != b"mathorn1973\n":
        raise PreflightError("formal_gh_identity_must_be_mathorn1973")


def compile_cpp(
    source: Path,
    executable: Path,
    standard: str,
    *,
    deadline: float,
) -> None:
    result = bounded_process(
        (
            "g++", f"-std={standard}", "-O3", "-DNDEBUG", "-Wall",
            "-Wextra", "-Wpedantic", "-Werror", str(source), "-o",
            str(executable),
        ),
        cwd=source.parent,
        max_stdout=1_048_576,
        max_stderr=1_048_576,
        timeout=remaining_seconds(deadline),
    )
    if result.returncode or result.stdout or result.stderr:
        raise PreflightError(
            f"compile_failed:{source.name}:rc={result.returncode}:"
            f"stdout={result.stdout!r}:stderr={result.stderr!r}"
        )


@contextmanager
def build_executables(
    base: Path,
    repository_root: Path,
    *,
    compile_primal_replay: bool,
    deadline: float,
) -> Iterator[tuple[Path, Path, Path | None]]:
    directory = repository_root / BUILD_DIRECTORY
    if directory.is_symlink() or directory.exists():
        raise PreflightError("build_workspace_preexisting")
    directory.mkdir()
    suffix = ".exe" if os.name == "nt" else ""
    successor = directory / f"crosscheck2_engine{suffix}"
    qualification = directory / f"qualification_engine{suffix}"
    primal = directory / f"primal_replay{suffix}"
    try:
        compile_cpp(
            base / "crosscheck2_engine.cpp",
            successor,
            "c++17",
            deadline=deadline,
        )
        compile_cpp(
            repository_root
            / "probes"
            / "P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1"
            / "qualification_engine.cpp",
            qualification,
            "c++17",
            deadline=deadline,
        )
        if compile_primal_replay:
            compile_cpp(
                base / "primal_replay.cpp",
                primal,
                "c++20",
                deadline=deadline,
            )
        yield successor, qualification, primal if compile_primal_replay else None
    finally:
        cleanup_error: Exception | None = None
        try:
            for path in (successor, qualification, primal):
                if path.is_symlink() or path.exists():
                    path.unlink()
            extras = tuple(directory.iterdir()) if directory.exists() else ()
            if extras:
                raise PreflightError(
                    "build_workspace_unexpected_entries:"
                    + ",".join(sorted(path.name for path in extras))
                )
            if directory.exists():
                directory.rmdir()
        except Exception as error:  # cleanup must fail closed
            cleanup_error = error
        if cleanup_error is not None:
            raise PreflightError("build_workspace_cleanup_failed") from cleanup_error


def bounded_process(
    command: Sequence[str],
    *,
    cwd: Path,
    max_stdout: int,
    max_stderr: int,
    input_bytes: bytes | None = None,
    timeout: float,
) -> ProcessResult:
    if timeout <= 0:
        raise PreflightError(f"child_timeout_before_start:{Path(command[0]).name}")
    try:
        process = subprocess.Popen(
            tuple(command),
            stdin=subprocess.DEVNULL if input_bytes is None else subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd,
            env=child_environment(),
            start_new_session=(os.name == "posix"),
        )
    except OSError as error:
        raise PreflightError(f"child_start_failed:{Path(command[0]).name}") from error
    assert process.stdout is not None and process.stderr is not None
    if input_bytes is not None:
        assert process.stdin is not None

    lock = threading.Lock()
    failures: list[str] = []
    storage: dict[str, bytes] = {}
    timed_out = threading.Event()

    def kill() -> None:
        try:
            if os.name == "posix":
                # The direct process may already have exited while a compiler
                # or tool descendant still owns a captured pipe.
                os.killpg(process.pid, signal.SIGKILL)
            elif process.poll() is None:
                process.kill()
        except OSError:
            pass

    def timeout_child() -> None:
        timed_out.set()
        kill()

    def collect(key: str, stream, cap: int) -> None:
        chunks: list[bytes] = []
        count = 0
        try:
            while True:
                chunk = stream.read(65_536)
                if not chunk:
                    break
                count += len(chunk)
                if count > cap:
                    raise PreflightError(f"{key}_cap:{Path(command[0]).name}")
                chunks.append(chunk)
            storage[key] = b"".join(chunks)
        except (OSError, PreflightError) as error:
            with lock:
                failures.append(str(error))
            kill()

    threads = (
        threading.Thread(
            target=collect,
            args=("stdout", process.stdout, max_stdout),
            name=f"stdout-{Path(command[0]).name}",
        ),
        threading.Thread(
            target=collect,
            args=("stderr", process.stderr, max_stderr),
            name=f"stderr-{Path(command[0]).name}",
        ),
    )
    timer = threading.Timer(timeout, timeout_child)
    timer.daemon = True
    timer.start()
    for thread in threads:
        thread.start()
    if input_bytes is not None:
        try:
            process.stdin.write(input_bytes)
            process.stdin.flush()
        except (BrokenPipeError, OSError) as error:
            failures.append(f"stdin_write:{error}")
            kill()
        finally:
            try:
                process.stdin.close()
            except OSError:
                pass
    end = time.monotonic() + timeout
    for thread in threads:
        thread.join(max(0.0, end - time.monotonic()))
    if any(thread.is_alive() for thread in threads):
        timed_out.set()
        kill()
        for thread in threads:
            thread.join(10)
    try:
        returncode = process.wait(timeout=10)
    except subprocess.TimeoutExpired as error:
        kill()
        raise PreflightError(f"child_reap_timeout:{Path(command[0]).name}") from error
    finally:
        timer.cancel()
    if timed_out.is_set():
        raise PreflightError(f"child_timeout:{Path(command[0]).name}")
    if failures:
        raise PreflightError(f"child_stream_failure:{Path(command[0]).name}:{failures!r}")
    if "stdout" not in storage or "stderr" not in storage:
        raise PreflightError(f"child_collection_incomplete:{Path(command[0]).name}")
    return ProcessResult(
        Path(command[0]).name,
        storage["stdout"],
        storage["stderr"],
        returncode,
    )


def checked_process(
    command: Sequence[str],
    *,
    cwd: Path,
    max_bytes: int,
    input_bytes: bytes | None = None,
    timeout: float,
) -> bytes:
    result = bounded_process(
        command,
        cwd=cwd,
        max_stdout=max_bytes,
        max_stderr=STDERR_CAP,
        input_bytes=input_bytes,
        timeout=timeout,
    )
    if result.returncode:
        raise PreflightError(
            f"child_nonzero:{Path(command[0]).name}:{result.returncode}:{result.stderr!r}"
        )
    if result.stderr:
        raise PreflightError(f"child_stderr:{Path(command[0]).name}:{result.stderr!r}")
    if len(result.stdout) > max_bytes:
        raise PreflightError(f"child_stdout_too_large:{Path(command[0]).name}")
    if b"\r" in result.stdout or not result.stdout.endswith(b"\n"):
        raise PreflightError(f"child_newline_contract:{Path(command[0]).name}")
    try:
        result.stdout.decode("ascii")
    except UnicodeDecodeError as error:
        raise PreflightError(f"child_nonascii:{Path(command[0]).name}") from error
    return result.stdout


def fixture_bytes(
    base: Path,
    repository_root: Path,
    successor: Path,
    qualification: Path,
    *,
    deadline: float,
) -> bytes:
    parts = (
        checked_process(
            (str(successor), "--selftest"), cwd=repository_root,
            max_bytes=1_048_576, timeout=remaining_seconds(deadline),
        ),
        checked_process(
            (str(qualification), "--selftest"), cwd=repository_root,
            max_bytes=1_048_576, timeout=remaining_seconds(deadline),
        ),
        checked_process(
            (
                sys.executable, "-B", str(base / "engine_fixture.py"),
                "--engine", str(successor),
                "--qualification-engine", str(qualification),
            ),
            cwd=repository_root,
            max_bytes=2_097_152,
            timeout=remaining_seconds(deadline),
        ),
        checked_process(
            (sys.executable, "-B", str(base / "reader_fixture.py")),
            cwd=repository_root,
            max_bytes=2_097_152,
            timeout=remaining_seconds(deadline),
        ),
    )
    return b"".join(parts)


def validate_pin_tokens(pin_commit: str, pin_receipt: str) -> None:
    if LOWER_HEX40_RE.fullmatch(pin_commit) is None:
        raise PreflightError("pin_commit_not_lower_hex40")
    if ISSUE_RECEIPT_RE.fullmatch(pin_receipt) is None:
        raise PreflightError("pin_receipt_not_issue_756_comment")
    if pin_receipt.rsplit("-", 1)[-1] in (
        RESERVATION_COMMENT_ID,
        GOVERNANCE_COMMENT_ID,
    ):
        raise PreflightError("pin_receipt_is_not_fresh_execution_pin")


def git_stdout(repository_root: Path, *arguments: str) -> bytes:
    result = bounded_process(
        ("git", *arguments),
        cwd=repository_root,
        max_stdout=16_777_216,
        max_stderr=1_048_576,
        timeout=300,
    )
    if result.returncode or result.stderr:
        raise PreflightError(f"git_{arguments[0]}_failed:{result.stderr!r}")
    return result.stdout


def validate_pin_commit(repository_root: Path, pin_commit: str, *, require_ancestor: bool) -> None:
    resolved = git_stdout(
        repository_root, "rev-parse", "--verify", f"{pin_commit}^{{commit}}"
    ).decode("ascii").strip()
    if resolved != pin_commit:
        raise PreflightError(f"pin_commit_not_exact_commit:{resolved}")
    parents = git_stdout(
        repository_root, "rev-list", "--parents", "-n", "1", pin_commit
    ).decode("ascii").split()
    if parents != [pin_commit, PUBLIC_BASE]:
        raise PreflightError(f"pin_parent_contract:{parents!r}")
    if require_ancestor:
        result = bounded_process(
            ("git", "merge-base", "--is-ancestor", pin_commit, "HEAD"),
            cwd=repository_root,
            max_stdout=4_096,
            max_stderr=65_536,
            timeout=60,
        )
        if result.returncode or result.stdout or result.stderr:
            raise PreflightError("pin_not_ancestor_of_HEAD")


def pinned_package_preflight(base: Path, repository_root: Path, pin_commit: str) -> None:
    probe_relative = base.relative_to(repository_root).as_posix()
    expected_paths = {
        f"{probe_relative}/{name}" for name in PIN_COMMIT_FILES
    }
    changed = git_stdout(
        repository_root,
        "diff-tree",
        "--no-commit-id",
        "--name-only",
        "--no-renames",
        "-r",
        pin_commit,
    ).decode("utf-8").splitlines()
    if len(changed) != len(expected_paths) or set(changed) != expected_paths:
        raise PreflightError(
            "pin_changed_paths:"
            f"observed={changed!r}:expected={sorted(expected_paths)!r}"
        )
    for name in PIN_COMMIT_FILES:
        current = base / name
        if current.is_symlink() or not current.is_file():
            raise PreflightError(f"pinned_package_nonregular:{name}")
        relative = current.relative_to(repository_root).as_posix()
        pinned = git_stdout(repository_root, "show", f"{pin_commit}:{relative}")
        if current.read_bytes() != pinned:
            raise PreflightError(f"pinned_package_changed_since_pin:{name}")


def github_comment(comment_id: str) -> dict[str, object]:
    result = bounded_process(
        (
            "gh", "api", "--hostname", "github.com", "--method", "GET",
            f"repos/mathorn1973/twist-j/issues/comments/{comment_id}",
        ),
        cwd=Path.cwd(),
        max_stdout=1_048_576,
        max_stderr=1_048_576,
        timeout=300,
    )
    if result.returncode or result.stderr or len(result.stdout) > 1_048_576:
        raise PreflightError(
            f"public_comment_fetch_failed:{comment_id}:rc={result.returncode}:"
            f"stdout_bytes={len(result.stdout)}:stderr={result.stderr!r}"
        )
    try:
        payload = json.loads(result.stdout)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PreflightError(f"public_comment_not_JSON:{comment_id}") from error
    if not isinstance(payload, dict):
        raise PreflightError(f"public_comment_not_object:{comment_id}")
    user = payload.get("user")
    expected_url = (
        "https://github.com/mathorn1973/twist-j/issues/756#issuecomment-"
        + comment_id
    )
    if not isinstance(user, dict) or user.get("login") != PUBLIC_OWNER:
        raise PreflightError(f"public_comment_wrong_author:{comment_id}")
    if payload.get("html_url") != expected_url:
        raise PreflightError(f"public_comment_wrong_html_url:{comment_id}")
    if payload.get("issue_url") != "https://api.github.com/repos/mathorn1973/twist-j/issues/756":
        raise PreflightError(f"public_comment_wrong_issue:{comment_id}")
    return payload


def governance_preflight() -> None:
    expected = {
        GOVERNANCE_COMMENT_ID: (
            2_494,
            "9c4cb1ac6c3dd176a2480a779b568fe67a449364656a13578263a9cccecdc5a2",
        ),
        RESERVATION_COMMENT_ID: (
            1_764,
            "7f837669ab1e2da337c107d45453db77c2862a6684902275b7492e6b011cdaec",
        ),
    }
    for comment_id, (expected_bytes, expected_sha) in expected.items():
        payload = github_comment(comment_id)
        body = payload.get("body")
        if not isinstance(body, str):
            raise PreflightError(f"public_comment_missing_body:{comment_id}")
        raw = body.encode("utf-8")
        if len(raw) != expected_bytes or sha256(raw) != expected_sha:
            raise PreflightError(f"public_comment_body_custody:{comment_id}")


def expected_public_receipt_body(base: Path, pin_commit: str) -> str:
    return "\n".join(
        (
            f"{PROBE_ID} PUBLIC EXECUTION PIN",
            f"probe: {PROBE_ID}",
            f"branch: {BRANCH}",
            f"pin_commit: {pin_commit}",
            f"parent_commit: {PUBLIC_BASE}",
            f"source_manifest_sha256: {sha256(strict_text(base / 'SOURCE_SHA256SUMS'))}",
            f"input_manifest_sha256: {sha256(strict_text(base / 'INPUT_SHA256SUMS'))}",
            f"attempt_ref: {PUBLIC_ATTEMPT_REF}",
            "formal_data_opened: NO",
            "authorization: SOLE_FORMAL_RUN",
        )
    )


def public_receipt_preflight(base: Path, pin_commit: str, pin_receipt: str) -> None:
    comment_id = pin_receipt.rsplit("-", 1)[-1]
    payload = github_comment(comment_id)
    if payload.get("html_url") != pin_receipt:
        raise PreflightError("public_receipt_wrong_html_url")
    body = payload.get("body")
    if not isinstance(body, str):
        raise PreflightError("public_receipt_missing_body")
    expected_body = expected_public_receipt_body(base, pin_commit)
    if body != expected_body or "\r" in body:
        raise PreflightError("public_receipt_body_contract")


def formal_public_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
    pin_receipt: str,
) -> tuple[str, str]:
    if Path.cwd().resolve() != repository_root.resolve():
        raise PreflightError("formal_cwd_must_be_repository_root")
    git_directory = repository_root / ".git"
    if git_directory.is_symlink() or not git_directory.is_dir():
        raise PreflightError("formal_repository_must_be_fresh_full_clone")
    validate_pin_commit(repository_root, pin_commit, require_ancestor=False)
    head = git_stdout(repository_root, "rev-parse", "HEAD").decode("ascii").strip()
    if head != pin_commit:
        raise PreflightError(f"formal_HEAD_not_pin:{head}")
    status = git_stdout(
        repository_root, "status", "--porcelain=v1", "--untracked-files=all"
    )
    if status:
        raise PreflightError(f"formal_worktree_not_clean:{status!r}")
    origin = git_stdout(repository_root, "remote", "get-url", "origin").decode("ascii")
    if origin != PUBLIC_REMOTE + "\n":
        raise PreflightError(f"formal_origin_URL_mismatch:{origin!r}")
    remote = git_stdout(
        repository_root,
        "ls-remote",
        "--heads",
        PUBLIC_REMOTE,
        f"refs/heads/{BRANCH}",
    ).decode("ascii")
    if remote != f"{pin_commit}\trefs/heads/{BRANCH}\n":
        raise PreflightError(f"formal_public_ref_mismatch:{remote!r}")
    observed = {path.name for path in base.iterdir()}
    expected = set(PIN_COMMIT_FILES)
    if observed != expected:
        raise PreflightError(
            f"formal_inventory:missing={sorted(expected-observed)!r}:"
            f"extra={sorted(observed-expected)!r}"
        )
    if any((base / name).exists() for name in POST_RUN_FILES):
        raise PreflightError("formal_preexisting_result_artifact")
    if (repository_root / BUILD_DIRECTORY).exists():
        raise PreflightError("formal_build_workspace_preexisting")
    source_manifest_sha = parse_manifest(
        base / "SOURCE_SHA256SUMS", base, SOURCE_FILES
    )
    input_manifest_sha = parse_manifest(
        base / "INPUT_SHA256SUMS", repository_root, verifier_input_files(base)
    )
    pinned_package_preflight(base, repository_root, pin_commit)
    governance_preflight()
    public_receipt_preflight(base, pin_commit, pin_receipt)
    return source_manifest_sha, input_manifest_sha


def claim_formal_attempt(repository_root: Path, pin_commit: str) -> None:
    result = bounded_process(
        ("git", "update-ref", ATTEMPT_REF, pin_commit, ZERO_OID),
        cwd=repository_root,
        max_stdout=4_096,
        max_stderr=65_536,
        timeout=60,
    )
    if result.returncode or result.stdout or result.stderr:
        raise PreflightError(
            "formal_attempt_already_claimed_or_ref_failed:"
            f"rc={result.returncode}:stdout={result.stdout!r}:stderr={result.stderr!r}"
        )


def claim_public_formal_attempt(repository_root: Path, pin_commit: str) -> None:
    result = bounded_process(
        (
            "gh", "api", "--hostname", "github.com", "--method", "POST",
            "repos/mathorn1973/twist-j/git/refs",
            "-f", f"ref={PUBLIC_ATTEMPT_REF}",
            "-f", f"sha={pin_commit}",
        ),
        cwd=repository_root,
        max_stdout=1_048_576,
        max_stderr=1_048_576,
        timeout=300,
    )
    if (
        result.returncode or result.stderr or not result.stdout
        or len(result.stdout) > 1_048_576
    ):
        raise PreflightError(
            "public_attempt_ref_create_failed:"
            f"rc={result.returncode}:stdout_bytes={len(result.stdout)}:"
            f"stderr={result.stderr!r}"
        )
    try:
        payload = json.loads(result.stdout)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PreflightError("public_attempt_ref_response_not_JSON") from error
    if not isinstance(payload, dict) or payload.get("ref") != PUBLIC_ATTEMPT_REF:
        raise PreflightError("public_attempt_ref_response_wrong_ref")
    target = payload.get("object")
    if not isinstance(target, dict) or target.get("sha") != pin_commit:
        raise PreflightError("public_attempt_ref_response_wrong_object")
    remote = git_stdout(
        repository_root,
        "ls-remote",
        "--refs",
        PUBLIC_REMOTE,
        PUBLIC_ATTEMPT_REF,
    ).decode("ascii")
    if remote != f"{pin_commit}\t{PUBLIC_ATTEMPT_REF}\n":
        raise PreflightError(f"public_attempt_ref_readback_mismatch:{remote!r}")


def remaining_seconds(deadline: float) -> float:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise PreflightError("formal_supervisor_deadline")
    return remaining


def run_primal(
    executable: Path,
    spec: PrimalSpec,
    pin_commit: str,
    pin_receipt: str,
    deadline: float,
) -> ProcessResult:
    result = bounded_process(
        (
            str(executable),
            "--formal",
            "--pin-commit", pin_commit,
            "--pin-receipt", pin_receipt,
            "--L", str(spec.L),
            "--seed", spec.seed_token,
            "--start", spec.start,
            "--thermal", str(spec.thermal),
            "--samples", "512",
            "--between", str(spec.between),
        ),
        cwd=executable.parent.parent,
        max_stdout=PRIMAL_CAP,
        max_stderr=STDERR_CAP,
        timeout=remaining_seconds(deadline),
    )
    return ProcessResult(spec.name, result.stdout, result.stderr, result.returncode)


def validate_primal_result(result: ProcessResult, spec: PrimalSpec) -> None:
    if result.returncode:
        raise PreflightError(f"primal_nonzero:{spec.name}:{result.returncode}")
    if result.stderr:
        raise PreflightError(f"primal_stderr:{spec.name}:{result.stderr!r}")
    if len(result.stdout) > PRIMAL_CAP:
        raise PreflightError(f"primal_cap:{spec.name}")
    if b"\r" in result.stdout or not result.stdout.endswith(b"\n"):
        raise PreflightError(f"primal_newlines:{spec.name}")
    try:
        result.stdout.decode("ascii")
    except UnicodeDecodeError as error:
        raise PreflightError(f"primal_nonascii:{spec.name}") from error
    if len(result.stdout) != spec.expected_bytes or sha256(result.stdout) != spec.expected_sha256:
        raise PreflightError(f"primal_not_byte_identical:{spec.name}")


def engine_command(
    executable: Path,
    spec: DualSpec,
    pin_commit: str,
    pin_receipt: str,
) -> tuple[str, ...]:
    return (
        str(executable),
        "--formal",
        "--pin-commit", pin_commit,
        "--pin-receipt", pin_receipt,
        "--L", str(spec.L),
        "--seed", spec.seed_token,
        "--start", spec.start,
        "--warm-bottom", str(spec.warm_bottom),
        "--checkpoints", str(spec.checkpoints),
        "--thin", str(spec.thin),
        "--validation-stride", str(spec.validation_stride),
        "--transition-cap", str(spec.transition_cap),
    )


def run_dual_pipeline(
    base: Path,
    repository_root: Path,
    executable: Path,
    spec: DualSpec,
    pin_commit: str,
    pin_receipt: str,
    deadline: float,
) -> PipelineResult:
    remaining = remaining_seconds(deadline)
    engine = subprocess.Popen(
        engine_command(executable, spec, pin_commit, pin_receipt),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=repository_root,
        env=child_environment(),
    )
    assert engine.stdout is not None and engine.stderr is not None
    try:
        reader = subprocess.Popen(
            (
                sys.executable,
                "-B",
                str(base / "state_reader.py"),
                "--expect-L",
                str(spec.L),
            ),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=repository_root,
            env=child_environment(),
        )
    except OSError:
        engine.kill()
        engine.wait()
        raise
    assert reader.stdin is not None and reader.stdout is not None and reader.stderr is not None

    lock = threading.Lock()
    failures: list[str] = []
    storage: dict[str, bytes | int | str] = {}
    timed_out = threading.Event()

    def kill_both() -> None:
        for process in (engine, reader):
            try:
                if process.poll() is None:
                    process.kill()
            except OSError:
                pass

    def timeout_both() -> None:
        timed_out.set()
        kill_both()

    timer = threading.Timer(remaining, timeout_both)
    timer.daemon = True

    def pump() -> None:
        count = 0
        digest = hashlib.sha256()
        try:
            while True:
                chunk = engine.stdout.read(65_536)
                if not chunk:
                    break
                count += len(chunk)
                if count > spec.engine_pipe_cap:
                    raise PreflightError(f"engine_pipe_cap:{spec.name}")
                digest.update(chunk)
                reader.stdin.write(chunk)
            reader.stdin.flush()
        except (BrokenPipeError, OSError, PreflightError) as error:
            with lock:
                failures.append(f"pump:{error}")
            kill_both()
        finally:
            try:
                reader.stdin.close()
            except OSError:
                pass
            storage["engine_pipe_bytes"] = count
            storage["engine_pipe_sha256"] = digest.hexdigest()

    def collect(key: str, stream, cap: int) -> None:
        chunks: list[bytes] = []
        count = 0
        try:
            while True:
                chunk = stream.read(65_536)
                if not chunk:
                    break
                count += len(chunk)
                if count > cap:
                    raise PreflightError(f"{key}_cap:{spec.name}")
                chunks.append(chunk)
            storage[key] = b"".join(chunks)
        except (OSError, PreflightError) as error:
            with lock:
                failures.append(f"{key}:{error}")
            kill_both()

    threads = (
        threading.Thread(target=pump, name=f"pump-{spec.label}"),
        threading.Thread(target=collect, args=("engine_stderr", engine.stderr, STDERR_CAP)),
        threading.Thread(target=collect, args=("reader_stdout", reader.stdout, FINAL_DUAL_CAP)),
        threading.Thread(target=collect, args=("reader_stderr", reader.stderr, STDERR_CAP)),
    )
    timer.start()
    for thread in threads:
        thread.start()
    for thread in threads:
        remaining = max(0.0, deadline - time.monotonic())
        if remaining == 0.0:
            break
        thread.join(remaining)
    if any(thread.is_alive() for thread in threads):
        timed_out.set()
        kill_both()
        for thread in threads:
            thread.join(10)
    try:
        engine_rc = engine.wait(timeout=10)
        reader_rc = reader.wait(timeout=10)
    except subprocess.TimeoutExpired as error:
        kill_both()
        raise PreflightError(f"pipeline_process_reap_timeout:{spec.name}") from error
    finally:
        timer.cancel()

    if timed_out.is_set():
        raise PreflightError(f"pipeline_supervisor_timeout:{spec.name}")
    if failures:
        raise PreflightError(f"pipeline_stream_failure:{spec.name}:{failures!r}")
    required = (
        "engine_pipe_bytes", "engine_pipe_sha256", "engine_stderr",
        "reader_stdout", "reader_stderr",
    )
    if any(key not in storage for key in required):
        raise PreflightError(f"pipeline_collection_incomplete:{spec.name}")
    return PipelineResult(
        name=spec.name,
        stdout=storage["reader_stdout"],  # type: ignore[arg-type]
        engine_stderr=storage["engine_stderr"],  # type: ignore[arg-type]
        reader_stderr=storage["reader_stderr"],  # type: ignore[arg-type]
        engine_returncode=engine_rc,
        reader_returncode=reader_rc,
        engine_pipe_bytes=storage["engine_pipe_bytes"],  # type: ignore[arg-type]
        engine_pipe_sha256=storage["engine_pipe_sha256"],  # type: ignore[arg-type]
    )


def validate_pipeline_result(result: PipelineResult, spec: DualSpec) -> None:
    if result.engine_returncode:
        raise PreflightError(f"engine_nonzero:{spec.name}:{result.engine_returncode}")
    if result.reader_returncode:
        raise PreflightError(f"reader_nonzero:{spec.name}:{result.reader_returncode}")
    if result.engine_stderr:
        raise PreflightError(f"engine_stderr:{spec.name}:{result.engine_stderr!r}")
    if result.reader_stderr:
        raise PreflightError(f"reader_stderr:{spec.name}:{result.reader_stderr!r}")
    if result.engine_pipe_bytes > spec.engine_pipe_cap:
        raise PreflightError(f"engine_pipe_cap_postcheck:{spec.name}")
    if len(result.stdout) > FINAL_DUAL_CAP:
        raise PreflightError(f"reader_output_cap:{spec.name}")
    if b"\r" in result.stdout or not result.stdout.endswith(b"\n"):
        raise PreflightError(f"reader_output_newlines:{spec.name}")
    records = result.stdout[:-1].split(b"\n")
    if len(records) != spec.checkpoints + 2 or any(not record for record in records):
        raise PreflightError(
            f"reader_output_shape:{spec.name}:records={len(records)}:"
            f"expected={spec.checkpoints+2}"
        )


def primal_manifest(results: dict[str, ProcessResult]) -> bytes:
    header = (
        "filename\tkind\tL\tstart\tseed\tthermal\tmeasurements\tbetween"
        "\tbytes\tsha256\texit_code\tstderr_bytes\n"
    )
    rows = []
    for spec in PRIMAL_SPECS:
        result = results[spec.name]
        rows.append(
            "\t".join(
                (
                    spec.name, "primal_replay", str(spec.L), spec.start,
                    spec.seed_token, str(spec.thermal), "512", str(spec.between),
                    str(len(result.stdout)), sha256(result.stdout),
                    str(result.returncode), str(len(result.stderr)),
                )
            )
        )
    return (header + "\n".join(rows) + "\n").encode("ascii")


def dual_manifest(results: dict[str, PipelineResult]) -> bytes:
    header = (
        "filename\tkind\tL\tstart\treplica\tseed\tseed_sha256\twarm_bottom"
        "\tcheckpoints\tthin\tvalidation_stride\ttransition_cap"
        "\tengine_pipe_cap\tengine_pipe_bytes\tengine_pipe_sha256"
        "\treader_cap\tbytes\tsha256\tengine_exit\treader_exit"
        "\tengine_stderr_bytes\treader_stderr_bytes\n"
    )
    rows = []
    for spec in DUAL_SPECS:
        result = results[spec.name]
        rows.append(
            "\t".join(
                (
                    spec.name, "exact_wrapper_filtered", str(spec.L), spec.start,
                    str(spec.replica), spec.seed_token, spec.seed_sha256,
                    str(spec.warm_bottom), str(spec.checkpoints), str(spec.thin),
                    str(spec.validation_stride), str(spec.transition_cap),
                    str(spec.engine_pipe_cap), str(result.engine_pipe_bytes),
                    result.engine_pipe_sha256, str(FINAL_DUAL_CAP),
                    str(len(result.stdout)), sha256(result.stdout),
                    str(result.engine_returncode), str(result.reader_returncode),
                    str(len(result.engine_stderr)), str(len(result.reader_stderr)),
                )
            )
        )
    return (header + "\n".join(rows) + "\n").encode("ascii")


def analysis_terminal(analysis: bytes) -> str:
    try:
        lines = analysis.decode("ascii").splitlines()
    except UnicodeDecodeError as error:
        raise PreflightError("analysis_nonascii") from error
    terminals = [line.split()[1] for line in lines if line.startswith("TERMINAL ")]
    if len(terminals) != 1 or terminals[0] not in ALLOWED_TERMINALS:
        raise PreflightError(f"analysis_terminal_grammar:{terminals!r}")
    if not lines or lines[-1] != "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY":
        raise PreflightError("analysis_evidential_status")
    return terminals[0]


def run_record_bytes(
    pin_commit: str,
    pin_receipt: str,
    source_manifest_sha: str,
    input_manifest_sha: str,
    output_manifest: bytes,
    analysis: bytes,
    receipt_body_sha: str,
    raw_bytes: int,
    output_bytes: int,
) -> bytes:
    if raw_bytes <= 0 or output_bytes < raw_bytes:
        raise PreflightError("run_record_byte_counts")
    command = (
        f"python3 probes/{PROBE_ID}/run_crosscheck2.py --formal "
        f"--pin-commit {pin_commit} --pin-receipt {pin_receipt}"
    )
    lines = (
        f"# {PROBE_ID} formal run",
        "status: COMPLETE_MODELED_RECORD",
        f"pin_commit: {pin_commit}",
        f"pin_receipt: {pin_receipt}",
        f"local_attempt_ref: {ATTEMPT_REF}",
        f"public_attempt_ref: {PUBLIC_ATTEMPT_REF}",
        f"source_manifest_sha256: {source_manifest_sha}",
        f"input_manifest_sha256: {input_manifest_sha}",
        f"receipt_body_sha256: {receipt_body_sha}",
        f"output_manifest_sha256: {sha256(output_manifest)}",
        f"analysis_sha256: {sha256(analysis)}",
        f"formal_command: {command}",
        "platform: Ubuntu 22.04.5 LTS",
        "architecture: x86_64",
        "python: CPython 3.10.12",
        "compiler: g++ 11.4.0",
        "boost_headers: BOOST_VERSION=107400",
        "git: 2.34.1",
        "github_cli: 2.4.0+dfsg1 (Ubuntu 2.4.0+dfsg1-2)",
        "github_identity: mathorn1973",
        "environment: LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0",
        f"output_file_count: {len(OUTPUT_FILES)}",
        f"output_bytes: {output_bytes}",
        f"raw_file_count: {len(PRIMAL_OUTPUTS) + len(DUAL_OUTPUTS)}",
        f"raw_bytes: {raw_bytes}",
        "formal_data_child_exit_codes: all 0",
        "formal_data_child_stderr_bytes: all 0",
        "driver_record_stage: before_formal_capture_and_successful_return",
        "formal_attempts: 1",
        "formal_rerun: NO",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def result_record_bytes(
    terminal: str,
    output_manifest: bytes,
    analysis: bytes,
) -> bytes:
    if terminal not in ALLOWED_TERMINALS:
        raise PreflightError(f"result_terminal:{terminal}")
    if terminal == "DUAL_CROSSCHECK_PASS":
        f3_status = "ELIGIBLE_ON_MERGE_AND_PUBLIC_READBACK"
        production = "REMAINS_FORBIDDEN_UNTIL_MERGE_AND_PUBLIC_READBACK"
    else:
        f3_status = "NOT_SATISFIED"
        production = "FORBIDDEN"
    lines = (
        f"# {PROBE_ID} result",
        f"terminal: {terminal}",
        "evidential_status: ZERO_ENGINEERING_ONLY",
        f"f3_status: {f3_status}",
        f"production_742: {production}",
        "canon: Public Canon v74",
        "canon_movement: NONE",
        f"output_manifest_sha256: {sha256(output_manifest)}",
        f"analysis_sha256: {sha256(analysis)}",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def run_formal(
    base: Path,
    repository_root: Path,
    pin_commit: str,
    pin_receipt: str,
) -> None:
    formal_runtime_preflight(repository_root)
    formal_cli_preflight(repository_root)
    source_manifest_sha, input_manifest_sha = formal_public_preflight(
        base, repository_root, pin_commit, pin_receipt
    )
    claim_formal_attempt(repository_root, pin_commit)
    claim_public_formal_attempt(repository_root, pin_commit)
    deadline = time.monotonic() + SUPERVISOR_SECONDS
    formal_toolchain_preflight(repository_root, deadline)

    with build_executables(
        base,
        repository_root,
        compile_primal_replay=True,
        deadline=deadline,
    ) as (
        successor,
        qualification,
        primal_executable,
    ):
        if primal_executable is None:
            raise AssertionError("formal_primal_executable_missing")
        fixture = fixture_bytes(
            base,
            repository_root,
            successor,
            qualification,
            deadline=deadline,
        )
        if fixture != strict_text(base / "FIXTURE_EXPECTED.txt"):
            raise PreflightError("fixture_expected_mismatch")

        primal_results: dict[str, ProcessResult] = {}
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {
                pool.submit(
                    run_primal,
                    primal_executable,
                    spec,
                    pin_commit,
                    pin_receipt,
                    deadline,
                ): spec
                for spec in PRIMAL_SPECS
            }
            for future in as_completed(futures):
                spec = futures[future]
                result = future.result()
                validate_primal_result(result, spec)
                primal_results[spec.name] = result
                write_exclusive(base / spec.name, result.stdout)
                print(f"PRIMAL_COMPLETE {spec.name}", flush=True)

        dual_results: dict[str, PipelineResult] = {}
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {
                pool.submit(
                    run_dual_pipeline,
                    base,
                    repository_root,
                    successor,
                    spec,
                    pin_commit,
                    pin_receipt,
                    deadline,
                ): spec
                for spec in DUAL_EXECUTION_ORDER
            }
            for future in as_completed(futures):
                spec = futures[future]
                result = future.result()
                validate_pipeline_result(result, spec)
                dual_results[spec.name] = result
                write_exclusive(base / spec.name, result.stdout)
                print(f"DUAL_COMPLETE {spec.name}", flush=True)

    if set(primal_results) != set(PRIMAL_OUTPUTS):
        raise PreflightError("primal_result_set")
    if set(dual_results) != set(DUAL_OUTPUTS):
        raise PreflightError("dual_result_set")
    write_exclusive(base / "PRIMAL_RUNS.tsv", primal_manifest(primal_results))
    write_exclusive(base / "DUAL_RUNS.tsv", dual_manifest(dual_results))

    analysis = checked_process(
        (sys.executable, "-B", str(base / "analyze_crosscheck2.py")),
        cwd=repository_root,
        max_bytes=ANALYSIS_CAP,
        timeout=remaining_seconds(deadline),
    )
    write_exclusive(base / "ANALYSIS.txt", analysis)

    output_manifest = "".join(
        f"{sha256((base / name).read_bytes())}  {name}\n" for name in OUTPUT_FILES
    ).encode("ascii")
    write_exclusive(base / "OUTPUT_SHA256SUMS", output_manifest)

    terminal = analysis_terminal(analysis)
    receipt_body_sha = sha256(
        expected_public_receipt_body(base, pin_commit).encode("utf-8")
    )
    raw_bytes = sum(
        len((base / name).read_bytes()) for name in PRIMAL_OUTPUTS + DUAL_OUTPUTS
    )
    output_bytes = sum(len((base / name).read_bytes()) for name in OUTPUT_FILES)
    write_exclusive(
        base / "RUN.md",
        run_record_bytes(
            pin_commit,
            pin_receipt,
            source_manifest_sha,
            input_manifest_sha,
            output_manifest,
            analysis,
            receipt_body_sha,
            raw_bytes,
            output_bytes,
        ),
    )
    write_exclusive(
        base / "RESULT.md",
        result_record_bytes(terminal, output_manifest, analysis),
    )

    expected = checked_process(
        (
            sys.executable,
            "-B",
            str(base / "verify.py"),
            "--formal-capture",
            "--pin-commit",
            pin_commit,
            "--pin-receipt",
            pin_receipt,
        ),
        cwd=repository_root,
        max_bytes=1_048_576,
        timeout=remaining_seconds(deadline),
    )
    write_exclusive(base / "EXPECTED.txt", expected)
    print(
        f"SOURCE_CUSTODY PASS manifest_sha256={source_manifest_sha}",
        flush=True,
    )
    print(
        f"INPUT_CUSTODY PASS manifest_sha256={input_manifest_sha}",
        flush=True,
    )
    print("DRIVER_RESULT COMPLETE_ZERO_EVIDENCE_CROSSCHECK_2", flush=True)


def parse_arguments(arguments: Sequence[str]) -> tuple[str, str, str]:
    if list(arguments) == ["--fixture"]:
        return "fixture", "", ""
    if len(arguments) == 5 and arguments[0] == "--formal":
        if arguments[1] != "--pin-commit" or arguments[3] != "--pin-receipt":
            raise PreflightError("argument_order")
        return "formal", arguments[2], arguments[4]
    raise PreflightError(
        "usage: run_crosscheck2.py --fixture | --formal --pin-commit HEX40 "
        "--pin-receipt ISSUE_COMMENT_URL"
    )


def main() -> int:
    base = Path(__file__).resolve().parent
    repository_root = base.parent.parent
    try:
        mode, pin_commit, pin_receipt = parse_arguments(sys.argv[1:])
        if mode == "fixture":
            deadline = time.monotonic() + 600
            with build_executables(
                base,
                repository_root,
                compile_primal_replay=False,
                deadline=deadline,
            ) as (
                successor,
                qualification,
                _primal,
            ):
                sys.stdout.buffer.write(
                    fixture_bytes(
                        base,
                        repository_root,
                        successor,
                        qualification,
                        deadline=deadline,
                    )
                )
            return 0
        validate_pin_tokens(pin_commit, pin_receipt)
        run_formal(base, repository_root, pin_commit, pin_receipt)
        return 0
    except (
        OSError,
        PreflightError,
        RuntimeError,
        UnicodeError,
        subprocess.SubprocessError,
    ) as error:
        print(f"CROSSCHECK2_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
