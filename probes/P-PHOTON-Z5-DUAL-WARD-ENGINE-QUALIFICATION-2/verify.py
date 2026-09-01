#!/usr/bin/env python3
"""Deterministic verifier for the dual Ward engine qualification.

The public fixture is intentionally synthetic.  This verifier first checks
source custody, then compiles and runs the C++ sampler fixture and the Python
supervisor fixture.  A separate Python model audits the exact dyadic draws and
the diagnostic records before the frozen combined transcript is accepted.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import itertools
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from typing import BinaryIO, Iterable, Sequence


BASE = Path(__file__).resolve().parent
REPOSITORY_ROOT = BASE.parents[1]
PUBLIC_BASE = "d0bc920b27117ea4a409282e3481340f50433763"
SOURCE_NAMES = (
    "PREREG.md",
    "README.md",
    "orbit_qualification.cpp",
    "supervisor_qualification.py",
    "verify.py",
    "FIXTURE_EXPECTED.txt",
)
POST_RUN_NAMES = ("EXPECTED.txt", "RUN.md", "RESULT.md")
MANIFEST_NAME = "SOURCE_SHA256SUMS"
PINNED_NAMES = SOURCE_NAMES + (MANIFEST_NAME,)
MANIFEST_LINE = re.compile(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)")
PIN_LINE = re.compile(r"^pin_commit: ([0-9a-f]{40})$", re.MULTILINE)
DOMAIN = b"photon-z5-dual-mobility-qualification-1"
SEED = bytes(range(16))
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
PROCESS_CAP = 1_048_576
PROCESS_TIMEOUT = 180
PROCESS_CLEANUP_TIMEOUT = 10
PROCESS_POLL_SECONDS = 0.01
SYSTEM_GIT = Path("/usr/bin/git")
SYSTEM_GXX = Path("/usr/bin/g++")
SYSTEM_PATH = "/usr/bin:/bin"
CANONICAL_ENVIRONMENT = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONHASHSEED": "0",
}
LOADER_INJECTION_ENV = (
    "LD_PRELOAD",
    "LD_AUDIT",
    "DYLD_INSERT_LIBRARIES",
    "DYLD_FORCE_FLAT_NAMESPACE",
)
PYTHON_LOADER_PRESERVE = ("LD_LIBRARY_PATH",)
GIT_REDIRECT_ENV = {
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_CEILING_DIRECTORIES",
    "GIT_COMMON_DIR",
    "GIT_CONFIG",
    "GIT_CONFIG_COUNT",
    "GIT_CONFIG_GLOBAL",
    "GIT_CONFIG_PARAMETERS",
    "GIT_CONFIG_SYSTEM",
    "GIT_DIR",
    "GIT_DISCOVERY_ACROSS_FILESYSTEM",
    "GIT_EXEC_PATH",
    "GIT_GRAFT_FILE",
    "GIT_INDEX_FILE",
    "GIT_INTERNAL_SUPER_PREFIX",
    "GIT_NAMESPACE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_OBJECT_DIRECTORY_RELATIVE",
    "GIT_PREFIX",
    "GIT_REPLACE_REF_BASE",
    "GIT_SHALLOW_FILE",
    "GIT_WORK_TREE",
}
TOOLCHAIN_ENV_SCRUB = (
    "CPATH",
    "CPLUS_INCLUDE_PATH",
    "C_INCLUDE_PATH",
    "OBJC_INCLUDE_PATH",
    "LIBRARY_PATH",
    "LD_LIBRARY_PATH",
    "LD_RUN_PATH",
    "DYLD_LIBRARY_PATH",
    "DYLD_FRAMEWORK_PATH",
    "DYLD_FALLBACK_FRAMEWORK_PATH",
    "DYLD_FALLBACK_LIBRARY_PATH",
    *LOADER_INJECTION_ENV,
    "COMPILER_PATH",
    "GCC_EXEC_PREFIX",
    "COLLECT_GCC",
    "COLLECT_GCC_OPTIONS",
    "COLLECT_LTO_WRAPPER",
    "DEPENDENCIES_OUTPUT",
    "SUNPRO_DEPENDENCIES",
    "CCC_OVERRIDE_OPTIONS",
    "SDKROOT",
    "MACOSX_DEPLOYMENT_TARGET",
    "SOURCE_DATE_EPOCH",
    "INCLUDE",
    "LIB",
    "CL",
    "_CL_",
    "LINK",
    "VIRTUAL_ENV",
    "CONDA_PREFIX",
    "CONDA_DEFAULT_ENV",
    "CONDA_PYTHON_EXE",
)


class VerifyFailure(RuntimeError):
    """A frozen qualification invariant did not hold."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strict_regular(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise VerifyFailure(f"regular_file:{path.name}")
    return path.read_bytes()


def strict_ascii_lf(path: Path) -> bytes:
    raw = strict_regular(path)
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise VerifyFailure(f"lf_contract:{path.name}")
    try:
        raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise VerifyFailure(f"ascii_contract:{path.name}") from error
    return raw


def git_environment() -> dict[str, str]:
    environment = os.environ.copy()
    for name in tuple(environment):
        upper = name.upper()
        if (
            upper.startswith("GIT_")
            or upper.startswith("PYTHON")
            or upper.startswith("LD_")
            or upper.startswith("DYLD_")
        ):
            environment.pop(name)
    environment.update(CANONICAL_ENVIRONMENT)
    environment["PATH"] = SYSTEM_PATH
    environment.update(
        {
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_NO_REPLACE_OBJECTS": "1",
            "GIT_OPTIONAL_LOCKS": "0",
            "GIT_PAGER": "cat",
            "GIT_TERMINAL_PROMPT": "0",
        }
    )
    return environment


def git_result(arguments: Sequence[str]) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            (
                "git",
                "--no-replace-objects",
                "--no-pager",
                "-c",
                "core.fsmonitor=false",
                "-c",
                "core.untrackedCache=false",
                *arguments,
            ),
            cwd=REPOSITORY_ROOT,
            env=git_environment(),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as error:
        raise VerifyFailure("git_process") from error


def git_stdout(arguments: Sequence[str], label: str) -> bytes:
    completed = git_result(arguments)
    if completed.returncode != 0:
        raise VerifyFailure(f"git_{label}:{completed.returncode}")
    return completed.stdout


def resolve_and_verify_pin(post_present: set[str]) -> str:
    head_raw = git_stdout(("rev-parse", "HEAD"), "head")
    try:
        head = head_raw.decode("ascii").strip()
    except UnicodeDecodeError as error:
        raise VerifyFailure("git_head_ascii") from error
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise VerifyFailure("git_head_shape")

    if post_present:
        run_text = strict_ascii_lf(BASE / "RUN.md").decode("ascii")
        matches = PIN_LINE.findall(run_text)
        if len(matches) != 1:
            raise VerifyFailure("run_pin_field")
        pin = matches[0]
    else:
        pin = head

    parents_raw = git_stdout(
        ("rev-list", "--parents", "-n", "1", pin), "pin_parents"
    )
    try:
        parents = parents_raw.decode("ascii").strip().split()
    except UnicodeDecodeError as error:
        raise VerifyFailure("git_parent_ascii") from error
    if parents != [pin, PUBLIC_BASE]:
        raise VerifyFailure("pin_not_unique_child_of_public_base")

    ancestor = git_result(("merge-base", "--is-ancestor", pin, "HEAD"))
    if ancestor.returncode != 0:
        raise VerifyFailure("pin_not_ancestor_of_head")

    prefix = f"probes/{BASE.name}/"
    diff_raw = git_stdout(
        ("diff-tree", "--no-commit-id", "--name-only", "-r", pin),
        "pin_diff",
    )
    try:
        changed = tuple(diff_raw.decode("ascii").splitlines())
    except UnicodeDecodeError as error:
        raise VerifyFailure("git_diff_ascii") from error
    expected_changed = tuple(prefix + name for name in PINNED_NAMES)
    if tuple(sorted(changed)) != tuple(sorted(expected_changed)):
        raise VerifyFailure("pin_changed_path_set")

    for name in PINNED_NAMES:
        pinned = git_stdout(("show", f"{pin}:{prefix}{name}"), f"pin_show_{name}")
        if pinned != strict_regular(BASE / name):
            raise VerifyFailure(f"pin_byte_identity:{name}")

    status = git_stdout(
        ("status", "--porcelain=v1", "--untracked-files=all"), "status"
    )
    if status:
        raise VerifyFailure("worktree_not_clean")
    return pin


def verify_source_custody() -> tuple[bytes, str, str]:
    manifest = strict_ascii_lf(BASE / MANIFEST_NAME)
    lines = manifest.decode("ascii").splitlines()
    if len(lines) != len(SOURCE_NAMES):
        raise VerifyFailure("source_manifest_line_count")
    parsed: list[tuple[str, str]] = []
    for line in lines:
        match = MANIFEST_LINE.fullmatch(line)
        if match is None:
            raise VerifyFailure("source_manifest_shape")
        parsed.append((match.group(1), match.group(2)))
    if tuple(name for _, name in parsed) != SOURCE_NAMES:
        raise VerifyFailure("source_manifest_order")
    if len({name for _, name in parsed}) != len(parsed):
        raise VerifyFailure("source_manifest_duplicate")
    for expected_hash, name in parsed:
        if sha256(strict_regular(BASE / name)) != expected_hash:
            raise VerifyFailure(f"source_hash:{name}")

    orbit_source = strict_ascii_lf(BASE / "orbit_qualification.cpp")
    if b"class ExactUInt" not in orbit_source:
        raise VerifyFailure("exact_uint_carrier_missing")
    for label, token in (
        ("boost", b"boost"),
        ("int128", b"__int128"),
        ("quoted_include", b'#include "'),
    ):
        if token in orbit_source:
            raise VerifyFailure(f"forbidden_cpp_dependency:{label}")

    allowed = set(SOURCE_NAMES) | {MANIFEST_NAME} | set(POST_RUN_NAMES)
    present = {item.name for item in BASE.iterdir()}
    if not set(SOURCE_NAMES).issubset(present) or MANIFEST_NAME not in present:
        raise VerifyFailure("source_inventory_missing")
    extras = sorted(present - allowed)
    if extras:
        raise VerifyFailure(f"source_inventory_extra:{','.join(extras)}")
    post_present = present.intersection(POST_RUN_NAMES)
    if post_present and post_present != set(POST_RUN_NAMES):
        raise VerifyFailure("post_run_inventory_incomplete")
    pin = resolve_and_verify_pin(post_present)
    return manifest, sha256(manifest), pin


def validated_python_loader(environment: dict[str, str]) -> str | None:
    raw = environment.get("LD_LIBRARY_PATH")
    if not raw:
        return None
    if len(raw.split(os.pathsep)) != 1:
        raise VerifyFailure("python_loader_path_components")
    candidate = Path(raw)
    expected = Path(sys.base_prefix) / "lib"
    if not candidate.is_absolute() or candidate.resolve() != expected.resolve():
        raise VerifyFailure("python_loader_path_outside_runtime")
    return raw


def verify_launch_ambient() -> None:
    if os.name != "posix" or sys.platform != "linux":
        raise VerifyFailure("linux_posix_process_group_required")
    for label, path in (("git", SYSTEM_GIT), ("gxx", SYSTEM_GXX)):
        try:
            resolved = path.resolve(strict=True)
        except OSError as error:
            raise VerifyFailure(f"system_tool:{label}") from error
        if (
            not path.is_file()
            or not os.access(path, os.X_OK)
            or not resolved.is_file()
            or Path("/usr") not in resolved.parents
            or shutil.which(path.name, path=SYSTEM_PATH) != str(path)
        ):
            raise VerifyFailure(f"system_tool:{label}")
    for name, expected in CANONICAL_ENVIRONMENT.items():
        if os.environ.get(name) != expected:
            raise VerifyFailure(f"canonical_environment:{name}")
    canonical_python = {"PYTHONDONTWRITEBYTECODE", "PYTHONHASHSEED"}
    for name in os.environ:
        if name.startswith("PYTHON") and name not in canonical_python:
            raise VerifyFailure(f"python_ambient:{name}")
    for name, value in os.environ.items():
        upper = name.upper()
        if value and (
            upper in GIT_REDIRECT_ENV
            or upper.startswith("GIT_CONFIG_KEY_")
            or upper.startswith("GIT_CONFIG_VALUE_")
        ):
            raise VerifyFailure(f"git_redirect_ambient:{name}")
        if value and (
            (upper.startswith("LD_") and upper != "LD_LIBRARY_PATH")
            or upper.startswith("DYLD_")
        ):
            raise VerifyFailure(f"loader_injection_ambient:{name}")
    validated_python_loader(os.environ)
    if os.environ.get("VIRTUAL_ENV") or os.environ.get("CONDA_PREFIX"):
        raise VerifyFailure("python_virtual_environment")
    if sys.prefix != sys.base_prefix or sys.exec_prefix != sys.base_exec_prefix:
        raise VerifyFailure("python_nonbase_runtime")
    expected_flags = {
        "debug": 0,
        "inspect": 0,
        "interactive": 0,
        "optimize": 0,
        "dont_write_bytecode": 1,
        "no_user_site": 0,
        "no_site": 0,
        "ignore_environment": 0,
        "verbose": 0,
        "bytes_warning": 0,
        "quiet": 0,
        "hash_randomization": 0,
        "isolated": 0,
        "dev_mode": False,
        "safe_path": False,
        "warn_default_encoding": 0,
    }
    for name, expected in expected_flags.items():
        if hasattr(sys.flags, name) and getattr(sys.flags, name) != expected:
            raise VerifyFailure(f"python_flag:{name}")
    if sys.warnoptions or sys._xoptions:
        raise VerifyFailure("python_runtime_options")


def deterministic_environment(*, python_runtime: bool = False) -> dict[str, str]:
    environment = os.environ.copy()
    for name in tuple(environment):
        upper = name.upper()
        if upper.startswith("PYTHON"):
            environment.pop(name)
            continue
        if upper.startswith("LD_") or upper.startswith("DYLD_"):
            if python_runtime and upper in PYTHON_LOADER_PRESERVE:
                continue
            environment.pop(name)
    blocked = {name.upper() for name in TOOLCHAIN_ENV_SCRUB}
    for name in tuple(environment):
        if name.upper() in blocked:
            environment.pop(name)
    if python_runtime:
        loader = validated_python_loader(os.environ)
        if loader is not None:
            environment["LD_LIBRARY_PATH"] = loader
    environment.update(CANONICAL_ENVIRONMENT)
    environment["PATH"] = SYSTEM_PATH
    return environment


@dataclass
class BoundedProcessStream:
    total: int = 0
    retained: bytearray | None = None
    error: str | None = None

    def __post_init__(self) -> None:
        if self.retained is None:
            self.retained = bytearray()


def drain_process_stream(
    stream: BinaryIO,
    capture: BoundedProcessStream,
    overflow: threading.Event,
) -> None:
    try:
        while True:
            chunk = os.read(stream.fileno(), 65_536)
            if not chunk:
                return
            capture.total += len(chunk)
            if capture.retained is None:
                capture.error = "capture_storage_missing"
                overflow.set()
                return
            if len(capture.retained) <= PROCESS_CAP:
                remaining = PROCESS_CAP + 1 - len(capture.retained)
                capture.retained.extend(chunk[:remaining])
            if capture.total > PROCESS_CAP:
                overflow.set()
    except OSError as error:
        capture.error = error.__class__.__name__
        overflow.set()
    finally:
        try:
            stream.close()
        except OSError:
            pass


def terminate_process_tree(process: subprocess.Popen[bytes]) -> None:
    try:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGKILL)
        elif process.poll() is None:
            process.kill()
    except (OSError, ProcessLookupError):
        pass


def cleanup_checked_process(
    process: subprocess.Popen[bytes],
    started: Sequence[threading.Thread],
    *,
    force_tree_kill: bool,
) -> tuple[bool, bool]:
    deadline = time.monotonic() + PROCESS_CLEANUP_TIMEOUT
    if force_tree_kill or process.poll() is None:
        terminate_process_tree(process)
    reaped = True
    try:
        process.wait(timeout=max(0.0, deadline - time.monotonic()))
    except (OSError, subprocess.TimeoutExpired):
        reaped = False
        terminate_process_tree(process)
    for thread in started:
        thread.join(max(0.0, deadline - time.monotonic()))
    threads_alive = any(thread.is_alive() for thread in started)
    if threads_alive:
        terminate_process_tree(process)
    for stream in (process.stdout, process.stderr):
        if stream is not None:
            try:
                stream.close()
            except OSError:
                pass
    return reaped, threads_alive


def checked_process(
    command: Sequence[str],
    *,
    cwd: Path,
    label: str,
    python_runtime: bool = False,
) -> bytes:
    if os.name != "posix" or sys.platform != "linux":
        raise VerifyFailure(f"process_linux_posix_required:{label}")
    keyword: dict[str, object] = {}
    keyword["start_new_session"] = True
    try:
        process = subprocess.Popen(
            tuple(command),
            cwd=cwd,
            env=deterministic_environment(python_runtime=python_runtime),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            **keyword,
        )
    except OSError as error:
        raise VerifyFailure(f"process_start:{label}") from error
    if process.stdout is None or process.stderr is None:
        reaped, threads_alive = cleanup_checked_process(
            process, (), force_tree_kill=True
        )
        if not reaped or threads_alive:
            raise VerifyFailure(f"process_cleanup:{label}")
        raise VerifyFailure(f"process_capture_pipe:{label}")

    stdout_capture = BoundedProcessStream()
    stderr_capture = BoundedProcessStream()
    overflow = threading.Event()
    threads = (
        threading.Thread(
            target=drain_process_stream,
            args=(process.stdout, stdout_capture, overflow),
            name=f"stdout-{label}",
            daemon=True,
        ),
        threading.Thread(
            target=drain_process_stream,
            args=(process.stderr, stderr_capture, overflow),
            name=f"stderr-{label}",
            daemon=True,
        ),
    )
    started: list[threading.Thread] = []
    timed_out = False
    start_failed = False
    try:
        for thread in threads:
            thread.start()
            started.append(thread)
    except RuntimeError:
        start_failed = True

    deadline = time.monotonic() + PROCESS_TIMEOUT
    if not start_failed:
        while process.poll() is None or any(thread.is_alive() for thread in started):
            if overflow.is_set():
                terminate_process_tree(process)
                break
            if time.monotonic() >= deadline:
                timed_out = True
                terminate_process_tree(process)
                break
            time.sleep(PROCESS_POLL_SECONDS)

    reaped, threads_alive = cleanup_checked_process(
        process, started, force_tree_kill=True
    )
    if not reaped:
        raise VerifyFailure(f"process_reap:{label}")
    if threads_alive:
        raise VerifyFailure(f"process_stream_reap:{label}")
    if start_failed:
        raise VerifyFailure(f"process_stream_start:{label}")

    if timed_out:
        raise VerifyFailure(f"process_timeout:{label}")
    if stdout_capture.error or stderr_capture.error:
        raise VerifyFailure(f"process_stream:{label}")
    if stdout_capture.total > PROCESS_CAP:
        raise VerifyFailure(f"process_stdout_cap:{label}")
    if stderr_capture.total > PROCESS_CAP:
        raise VerifyFailure(f"process_stderr_cap:{label}")
    if process.returncode != 0:
        raise VerifyFailure(f"process_exit:{label}:{process.returncode}")
    stdout = bytes(stdout_capture.retained or b"")
    stderr = bytes(stderr_capture.retained or b"")
    if stderr:
        raise VerifyFailure(f"process_stderr:{label}:{len(stderr)}")
    if stdout and (b"\r" in stdout or not stdout.endswith(b"\n")):
        raise VerifyFailure(f"process_lf:{label}")
    try:
        stdout.decode("ascii")
    except UnicodeDecodeError as error:
        raise VerifyFailure(f"process_ascii:{label}") from error
    return stdout


def build_and_run_fixtures() -> tuple[bytes, bytes]:
    with tempfile.TemporaryDirectory(prefix="ward-engine-qualification-") as slot:
        executable = Path(slot) / (
            "orbit_qualification.exe" if os.name == "nt" else "orbit_qualification"
        )
        compile_stdout = checked_process(
            (
                "g++",
                "-std=c++17",
                "-O2",
                "-DNDEBUG",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                "-Werror",
                str(BASE / "orbit_qualification.cpp"),
                "-o",
                str(executable),
            ),
            cwd=BASE,
            label="compile_orbit",
        )
        if compile_stdout:
            raise VerifyFailure("compiler_stdout")
        orbit = checked_process(
            (str(executable), "--fixture"), cwd=BASE, label="orbit_fixture"
        )
    supervisor = checked_process(
        (
            sys.executable,
            "-S",
            "-s",
            "-B",
            str(BASE / "supervisor_qualification.py"),
            "--fixture",
        ),
        cwd=BASE,
        label="supervisor_fixture",
        python_runtime=True,
    )
    return orbit, supervisor


@dataclass
class CounterBits:
    seed: bytes = SEED
    counter: int = 0
    block: bytes = b""
    position: int = 256
    consumed: int = 0

    def bit(self) -> int:
        if self.position == 256:
            if self.counter >= 1 << 128:
                raise VerifyFailure("independent_counter_overflow")
            self.block = hashlib.sha256(
                DOMAIN + self.seed + self.counter.to_bytes(16, "big")
            ).digest()
            self.counter += 1
            self.position = 0
        result = (self.block[self.position // 8] >> (7 - self.position % 8)) & 1
        self.position += 1
        self.consumed += 1
        return result

    def bits(self, count: int) -> int:
        value = 0
        for _ in range(count):
            value = (value << 1) | self.bit()
        return value

    def bounded(self, bound: int) -> int:
        if bound <= 0:
            raise VerifyFailure("independent_nonpositive_bound")
        width = (bound - 1).bit_length()
        while True:
            value = self.bits(width)
            if value < bound:
                return value


def weights_for(exponents: Iterable[int]) -> list[int]:
    values = list(exponents)
    if not values:
        raise VerifyFailure("independent_empty_table")
    minimum = min(values)
    return [1 << (value - minimum) for value in values]


def exact_sample(exponents: Iterable[int]) -> tuple[list[int], int, int, int, int]:
    weights = weights_for(exponents)
    total = sum(weights)
    stream = CounterBits()
    draw = stream.bounded(total)
    cumulative = 0
    for index, weight in enumerate(weights):
        cumulative += weight
        if draw < cumulative:
            return weights, total, index, draw, stream.consumed
    raise VerifyFailure("independent_selection_fell_through")


def record_fields(line: str, prefix: str) -> dict[str, str]:
    if not line.startswith(prefix + " "):
        raise VerifyFailure(f"record_prefix:{prefix}")
    fields: dict[str, str] = {}
    for token in line[len(prefix) + 1 :].split(" "):
        if "=" not in token:
            raise VerifyFailure(f"record_token:{prefix}")
        key, value = token.split("=", 1)
        if not key or key in fields:
            raise VerifyFailure(f"record_key:{prefix}")
        fields[key] = value
    return fields


def expect_fields(
    actual: dict[str, str], expected: dict[str, str], label: str
) -> None:
    if actual != expected:
        raise VerifyFailure(f"independent_record:{label}")


def sample_fields(exponents: Sequence[int], path: str) -> dict[str, str]:
    weights, total, choice, draw, bits = exact_sample(exponents)
    return {
        "span": str(max(exponents) - min(exponents)),
        "weights": ",".join(str(value) for value in weights),
        "total": str(total),
        "path": path,
        "choice": str(choice),
        "draw": str(draw),
        "bits": str(bits),
        "status": "PASS",
    }


def independent_orbit_audit(raw: bytes) -> None:
    lines = raw.decode("ascii").splitlines()
    if len(lines) != 17:
        raise VerifyFailure("orbit_line_count")
    expect_fields(
        record_fields(lines[0], "ORBIT_QUALIFICATION"),
        {
            "bitstream": "sha256-counter-msb-first",
            "bounded_rejection": "PASS",
            "legacy_equivalence_cases": "2048",
            "status": "PASS",
        },
        "orbit_header",
    )

    table_count = sum(9**length - 8**length for length in range(1, 6))
    draw_count = 0
    ratio_count = 0
    interval_count = 0
    for length in range(1, 6):
        for vector in itertools.product(range(9), repeat=length):
            if min(vector) != 0:
                continue
            draw_count += sum(1 << shift for shift in vector)
            ratio_count += length * length
            interval_count += 2 * length
    expect_fields(
        record_fields(lines[1], "SMALL_ENVELOPE_EXHAUSTIVE"),
        {
            "lengths": "1..5",
            "normalized_q": "0..8",
            "tables": str(table_count),
            "draws": str(draw_count),
            "transcripts": str(table_count),
            "status": "PASS",
        },
        "small_envelope",
    )

    spans = (0, 1, 32, 62, 63, 64, 72, 128, 192)
    for offset, span in enumerate(spans, start=2):
        path = "legacy-u64" if span < 63 else "exact-uint"
        expect_fields(
            record_fields(lines[offset], "SPAN_KAT"),
            sample_fields((0, -span, -span), path),
            f"span_{span}",
        )

    sum_fields = sample_fields((0, 0, 0, 0, -62), "exact-uint")
    sum_fields["old_guard"] = "orbit_weight_sum_overflow"
    # The source prints old_guard before path; dictionary equality is order-free.
    expect_fields(
        record_fields(lines[11], "SUM_OVERFLOW_KAT"),
        sum_fields,
        "sum_overflow",
    )

    width_fields = sample_fields((0, 0, -62), "exact-uint")
    width_fields["old_guard"] = "bitstream_bits_width_exceeds_63"
    width_fields["guard_bits"] = "0"
    expect_fields(
        record_fields(lines[12], "WIDTH64_KAT"),
        width_fields,
        "width64",
    )

    for offset, lattice_size in enumerate((6, 8), start=13):
        area = lattice_size * lattice_size
        exponents = (0, -2 * area, -area)
        fields = sample_fields(exponents, "exact-uint")
        fields["spread"] = fields.pop("span")
        fields.update(
            {
                "L": str(lattice_size),
                "states": "k0,k1,k4",
                "support_B": f"{area}:1,{2 * area}:0,{2 * area}:1",
                "exponents": f"0,-{2 * area},-{area}",
                "old_guard": "orbit_integer_weight_overflow",
                "guard_bits": "0",
            }
        )
        expect_fields(
            record_fields(lines[offset], "TWO_PLANE_ENVELOPE"),
            fields,
            f"two_plane_L{lattice_size}",
        )

    extra_lengths = (3,) * 9 + (5, 3, 3, 3)
    expect_fields(
        record_fields(lines[15], "EXACT_AUDIT"),
        {
            "tables": str(table_count + len(extra_lengths)),
            "weight_ratios": str(
                ratio_count + sum(length * length for length in extra_lengths)
            ),
            "detailed_balance_pairs": str(
                ratio_count + sum(length * length for length in extra_lengths)
            ),
            "interval_endpoints": str(
                interval_count + sum(2 * length for length in extra_lengths)
            ),
            "exhaustive_draws": "7",
            "totals_above_2^64": "YES",
            "status": "PASS",
        },
        "exact_audit",
    )
    if lines[16] != "ORBIT_QUALIFICATION PASS":
        raise VerifyFailure("orbit_terminal")


def independent_supervisor_audit(raw: bytes) -> None:
    lines = raw.decode("ascii").splitlines()
    if len(lines) != 16:
        raise VerifyFailure("supervisor_line_count")
    fixed = {
        0: "SUPERVISOR_BATCH PASS",
        1: "FAILING_SPEC dual_rc",
        2: "ENGINE_RC 7",
        3: "READER_RC 11",
        7: "SIBLING_WAS_RUNNING true",
        8: "SIBLING_CANCELLED true",
        9: "SIBLING_ENGINE_REAPED true",
        10: "SIBLING_READER_REAPED true",
        11: "QUEUED_FUTURES_CANCELLED_AT_LEAST_TWO true",
        12: "QUEUED_CHILDREN_NEVER_STARTED true",
        13: "ALL_FUTURES_DONE true",
        14: "SURVIVING_PIDS 0",
        15: "SUPERVISOR_QUALIFICATION PASS",
    }
    for index, expected in fixed.items():
        if lines[index] != expected:
            raise VerifyFailure(f"supervisor_record:{index}")

    for index, label, marker, tail in (
        (4, "ENGINE_STDERR", b"E", b"engine-tail\n"),
        (5, "READER_STDERR", b"R", b"reader-tail\n"),
    ):
        payload = marker * 4096 + tail
        expect_fields(
            record_fields(lines[index], label),
            {
                "stderr_total_bytes": str(len(payload)),
                "stderr_full_sha256": sha256(payload),
                "stderr_prefix_bytes": "4096",
                "stderr_prefix_hex": (marker * 4096).hex(),
                "stderr_truncated": "true",
            },
            label.lower(),
        )
    pipe = b"synthetic-pipe-payload\n"
    expect_fields(
        record_fields(lines[6], "PIPE_CAPTURE"),
        {"bytes": str(len(pipe)), "sha256": sha256(pipe)},
        "pipe_capture",
    )


def main() -> int:
    if len(sys.argv) != 1:
        print("VERIFY_ERROR expected_no_arguments", file=sys.stderr)
        return 64
    try:
        verify_launch_ambient()
        manifest, manifest_hash, pin = verify_source_custody()
        fixture = strict_ascii_lf(BASE / "FIXTURE_EXPECTED.txt")
        orbit, supervisor = build_and_run_fixtures()
        independent_orbit_audit(orbit)
        independent_supervisor_audit(supervisor)
        combined = orbit + supervisor
        if combined != fixture:
            raise VerifyFailure("fixture_byte_mismatch")
        output = (
            f"SOURCE_CUSTODY pin_commit={pin} files={len(SOURCE_NAMES)} "
            f"manifest_bytes={len(manifest)} manifest_sha256={manifest_hash} PASS\n"
            f"ORBIT_FIXTURE bytes={len(orbit)} sha256={sha256(orbit)} PASS\n"
            f"SUPERVISOR_FIXTURE bytes={len(supervisor)} "
            f"sha256={sha256(supervisor)} PASS\n"
            f"COMBINED_FIXTURE bytes={len(combined)} sha256={sha256(combined)} PASS\n"
            "INDEPENDENT_EXACT_AUDIT tables=28994 "
            "small_tables=28981 small_draws=6791443 PASS\n"
            "LEGACY_PATH choice_draw_bits_successor=BYTE_IDENTICAL PASS\n"
            "SUPERVISOR_FAIL_CLOSED rc=7,11 "
            "queued_cancel_at_least_two=true queued_children_started=0 "
            "running_reaped=true survivors=0 PASS\n"
            "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY\n"
            "F3_STATUS NOT_SATISFIED\n"
            "PRODUCTION_742 FORBIDDEN\n"
            "TERMINAL WARD_ENGINE_QUALIFICATION_PASS\n"
        ).encode("ascii")
        sys.stdout.buffer.write(output)
        return 0
    except (OSError, UnicodeError, VerifyFailure, subprocess.SubprocessError) as error:
        print(f"VERIFY_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
