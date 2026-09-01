#!/usr/bin/env python3
"""Pinned runner and deterministic replay for the L<=4 mobility qualification.

``--formal`` is the sole pre-result execution and requires the public pin.
``--replay`` is available only from a clean repository-root checkout whose
immutable result trio is byte-bound to the first result commit after the pin;
the public attempt and qualification refs must simultaneously read back the
pin and that result commit.  Replay is used by ``verify.py``.  ``--fixture``
opens only short development L3/L4 streams and is permitted before the pin.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from types import ModuleType
from typing import Iterator, Sequence


PROBE_ID = "P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1"
BRANCH = "probe/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1"
DOMAIN = "photon-z5-dual-mobility-qualification-1"
PUBLIC_BASE = "ebf1d8a2100cb26c58721edaade67a278a0004a7"
PUBLIC_REMOTE = "https://github.com/mathorn1973/twist-j.git"
PUBLIC_OWNER = "mathorn1973"
RESERVATION_COMMENT_ID = "5495515902"
ATTEMPT_REF = f"refs/probe-attempts/{PROBE_ID}"
PUBLIC_ATTEMPT_REF = f"refs/heads/probe-attempts/{PROBE_ID}"
ZERO_OID = "0" * 40
BUILD_DIRECTORY = ".photon-z5-dual-mobility-qualification-build"
ISSUE_RECEIPT_RE = re.compile(
    r"https://github\.com/mathorn1973/twist-j/issues/756#issuecomment-[0-9]+\Z"
)
LOWER_HEX40_RE = re.compile(r"[0-9a-f]{40}\Z")

PINNED_FILES = (
    "PREREG.md",
    "QUALIFICATION_PIN.md",
    "README.md",
    "qualification_engine.cpp",
    "qualification_analysis.py",
    "mobility_kernel.py",
    "sector_ladder.py",
    "qualification_run.py",
    "verify.py",
    "FIXTURE_EXPECTED.txt",
)

INPUT_FILES = (
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/PREREG.md",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/README.md",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/dual_cycle_kernel.py",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/verify.py",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/analyze_pilot.py",
)

POST_RUN_FILES = ("EXPECTED.txt", "RUN.md", "RESULT.md")
PIN_COMMIT_FILES = PINNED_FILES + ("SOURCE_SHA256SUMS", "INPUT_SHA256SUMS")
STATS_RELATIVE = INPUT_FILES[-1]
STATS_SHA256 = "d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce"
WARM_BOTTOM = 16_384
CHECKPOINTS = 2_048
THIN = 256
VALIDATION_STRIDE = 256
TRANSITION_CAP = 67_108_864
FORMAL_PREFIX = 0xF7560000000000000000000000000000
MAX_TRANSCRIPT_BYTES = 5 * 1024 * 1024


@dataclass(frozen=True)
class ChainSpec:
    label: str
    L: int
    start: str
    seed: int

    @property
    def seed_token(self) -> str:
        return f"0x{self.seed:032x}"


FORMAL_SPECS = tuple(
    ChainSpec(
        label=f"L{L}_{start}_r{replica}",
        L=L,
        start=start,
        seed=FORMAL_PREFIX + L * 0x10000 + family * 0x100 + replica,
    )
    for L in (3, 4)
    for start, family in (("cold", 1), ("stratified", 2))
    for replica in (1, 2)
)

FIXTURE_SPECS = (
    ChainSpec("fixture_L3_stratified", 3, "stratified", 0x0123456789ABCDEFFEDCBA9876543210),
    ChainSpec("fixture_L4_cold", 4, "cold", 0x13579BDF2468ACE00123456789ABCDEF),
)


class PreflightError(RuntimeError):
    """A source, environment, execution, or custody condition failed."""


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


def compile_engine(base: Path, executable: Path) -> None:
    environment = os.environ.copy()
    environment.update({"LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    result = subprocess.run(
        (
            "g++",
            "-std=c++17",
            "-O3",
            "-DNDEBUG",
            "-Wall",
            "-Wextra",
            "-Wpedantic",
            "-Werror",
            str(base / "qualification_engine.cpp"),
            "-o",
            str(executable),
        ),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=environment,
    )
    if result.returncode or result.stdout or result.stderr:
        raise PreflightError(
            "compile_failed:"
            f"rc={result.returncode}:stdout={result.stdout!r}:stderr={result.stderr!r}"
        )


@contextmanager
def build_executable(repository_root: Path) -> Iterator[Path]:
    """Own one explicit workspace-local build slot and remove it exactly.

    Default temporary-directory creation yields ACL-inaccessible directories
    on the managed Windows runner.  A fixed directory also makes concurrent
    or stale attempts fail closed.  It is created only after the caller's
    formal/replay preflight.
    """

    directory = repository_root / BUILD_DIRECTORY
    if directory.is_symlink() or directory.exists():
        raise PreflightError("build_workspace_preexisting")
    directory.mkdir()
    executable = directory / (
        "qualification_engine.exe" if os.name == "nt" else "qualification_engine"
    )
    try:
        yield executable
    finally:
        try:
            if executable.is_symlink() or executable.exists():
                executable.unlink()
            extras = tuple(directory.iterdir())
            if extras:
                raise PreflightError(
                    "build_workspace_unexpected_entries:"
                    + ",".join(sorted(path.name for path in extras))
                )
            directory.rmdir()
        except OSError as error:
            raise PreflightError("build_workspace_cleanup_failed") from error


def checked_process(command: Sequence[str], *, max_bytes: int = MAX_TRANSCRIPT_BYTES) -> bytes:
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
    result = subprocess.run(
        tuple(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=environment,
    )
    if result.returncode:
        raise PreflightError(f"child_nonzero:{Path(command[0]).name}:{result.returncode}:{result.stderr!r}")
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


def engine_command(
    executable: Path,
    chain: ChainSpec,
    *,
    formal: bool,
    pin_commit: str = "",
    pin_receipt: str = "",
    warm_bottom: int = WARM_BOTTOM,
    checkpoints: int = CHECKPOINTS,
    thin: int = THIN,
    validation_stride: int = VALIDATION_STRIDE,
    transition_cap: int = TRANSITION_CAP,
) -> tuple[str, ...]:
    mode: tuple[str, ...]
    if formal:
        mode = (
            "--qualification",
            "--pin-commit",
            pin_commit,
            "--pin-receipt",
            pin_receipt,
        )
    else:
        mode = ("--development",)
    return (
        str(executable),
        *mode,
        "--L",
        str(chain.L),
        "--seed",
        chain.seed_token,
        "--start",
        chain.start,
        "--warm-bottom",
        str(warm_bottom),
        "--checkpoints",
        str(checkpoints),
        "--thin",
        str(thin),
        "--validation-stride",
        str(validation_stride),
        "--transition-cap",
        str(transition_cap),
    )


def parse_generated_records(raw: bytes, label: str) -> list[dict[str, object]]:
    try:
        records = [json.loads(line) for line in raw.decode("ascii").splitlines()]
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PreflightError(f"fixture_json:{label}") from error
    if any(not isinstance(record, dict) for record in records):
        raise PreflightError(f"fixture_record_type:{label}")
    return records


def fixture_bytes(base: Path, executable: Path) -> bytes:
    selftest = checked_process((str(executable), "--selftest"), max_bytes=16_384)
    sys.dont_write_bytecode = True
    if str(base) not in sys.path:
        sys.path.insert(0, str(base))
    sector = load_module("mobility_qualification_sector_fixture", base / "sector_ladder.py")
    lines = [selftest.decode("ascii").rstrip("\n")]
    for chain in FIXTURE_SPECS:
        raw = checked_process(
            engine_command(
                executable,
                chain,
                formal=False,
                warm_bottom=0,
                checkpoints=1,
                thin=128,
                validation_stride=32,
                transition_cap=1_048_576,
            )
        )
        records = parse_generated_records(raw, chain.label)
        if len(records) != 3:
            raise PreflightError(f"fixture_record_count:{chain.label}")
        checkpoint = records[1]
        summary = records[2]
        ladder = sector.SectorLadder(chain.L, chain.seed, chain.start)
        while ladder.diagnostics.swap_attempts[0] < 128:
            ladder.step()
            if ladder.diagnostics.transitions >= 1_048_576:
                raise PreflightError(f"fixture_python_transition_cap:{chain.label}")
        target = ladder.replicas[0]
        expected = {
            "transition": ladder.diagnostics.transitions,
            "state_sha256": sector.state_sha256(target.values),
            "support": target.support,
            "homology": list(target.homology),
            "j_nnz": target.current_nonzero_count,
            "walker_id": ladder.labels[0],
        }
        actual = {
            "transition": checkpoint.get("transition"),
            "state_sha256": checkpoint.get("state_sha256"),
            "support": checkpoint.get("support"),
            "homology": checkpoint.get("homology"),
            "j_nnz": checkpoint.get("j_nnz"),
            "walker_id": checkpoint.get("walker_id"),
        }
        if actual != expected:
            raise PreflightError(f"fixture_cpp_python_mismatch:{chain.label}")
        if summary.get("final_state_sha256") != expected["state_sha256"]:
            raise PreflightError(f"fixture_summary_mismatch:{chain.label}")
        homology = ",".join(str(value) for value in expected["homology"])
        lines.append(
            f"PARITY L={chain.L} start={chain.start} bottom_attempts=128 "
            f"transitions={expected['transition']} support={expected['support']} "
            f"j_nnz={expected['j_nnz']} H2={homology} walker={expected['walker_id']} "
            f"state_sha256={expected['state_sha256']} status=PASS"
        )
    lines.append("FIXTURE_RESULT PASS")
    return ("\n".join(lines) + "\n").encode("ascii")


def validate_pin_tokens(pin_commit: str, pin_receipt: str) -> None:
    if LOWER_HEX40_RE.fullmatch(pin_commit) is None:
        raise PreflightError("pin_commit_not_lower_hex40")
    if ISSUE_RECEIPT_RE.fullmatch(pin_receipt) is None:
        raise PreflightError("pin_receipt_not_issue_756_comment")
    if pin_receipt.rsplit("-", 1)[-1] == RESERVATION_COMMENT_ID:
        raise PreflightError("pin_receipt_is_reservation_not_qualification_pin")


def git_stdout(repository_root: Path, *arguments: str) -> bytes:
    result = subprocess.run(
        ("git", *arguments),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        cwd=repository_root,
    )
    if result.returncode or result.stderr:
        raise PreflightError(f"git_{arguments[0]}_failed:{result.stderr!r}")
    return result.stdout


def validate_pin_commit(
    repository_root: Path,
    pin_commit: str,
    *,
    require_ancestor: bool,
) -> None:
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
        result = subprocess.run(
            ("git", "merge-base", "--is-ancestor", pin_commit, "HEAD"),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            cwd=repository_root,
        )
        if result.returncode or result.stdout or result.stderr:
            raise PreflightError(
                "pin_not_ancestor_of_HEAD:"
                f"rc={result.returncode}:stdout={result.stdout!r}:stderr={result.stderr!r}"
            )


def pinned_package_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
) -> None:
    for name in PIN_COMMIT_FILES:
        current = base / name
        if current.is_symlink() or not current.is_file():
            raise PreflightError(f"pinned_package_nonregular:{name}")
        relative = current.relative_to(repository_root).as_posix()
        pinned = git_stdout(repository_root, "show", f"{pin_commit}:{relative}")
        if current.read_bytes() != pinned:
            raise PreflightError(f"pinned_package_changed_since_pin:{name}")


def public_receipt_preflight(
    base: Path,
    pin_commit: str,
    pin_receipt: str,
) -> None:
    comment_id = pin_receipt.rsplit("-", 1)[-1]
    environment = os.environ.copy()
    environment.update({"LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    result = subprocess.run(
        (
            "gh",
            "api",
            "--hostname",
            "github.com",
            "--method",
            "GET",
            f"repos/mathorn1973/twist-j/issues/comments/{comment_id}",
        ),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=environment,
    )
    if result.returncode or result.stderr or len(result.stdout) > 1_048_576:
        raise PreflightError(
            "public_receipt_fetch_failed:"
            f"rc={result.returncode}:stdout_bytes={len(result.stdout)}:"
            f"stderr={result.stderr!r}"
        )
    try:
        payload = json.loads(result.stdout)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PreflightError("public_receipt_not_JSON") from error
    if not isinstance(payload, dict):
        raise PreflightError("public_receipt_not_object")
    user = payload.get("user")
    if not isinstance(user, dict) or user.get("login") != PUBLIC_OWNER:
        raise PreflightError("public_receipt_wrong_author")
    if payload.get("html_url") != pin_receipt:
        raise PreflightError("public_receipt_wrong_html_url")
    if payload.get("issue_url") != (
        "https://api.github.com/repos/mathorn1973/twist-j/issues/756"
    ):
        raise PreflightError("public_receipt_wrong_issue")
    body = payload.get("body")
    if not isinstance(body, str):
        raise PreflightError("public_receipt_missing_body")
    source_manifest_sha = sha256(strict_text(base / "SOURCE_SHA256SUMS"))
    input_manifest_sha = sha256(strict_text(base / "INPUT_SHA256SUMS"))
    expected_body = "\n".join(
        (
            f"{PROBE_ID} PUBLIC QUALIFICATION PIN",
            f"probe: {PROBE_ID}",
            f"branch: {BRANCH}",
            f"pin_commit: {pin_commit}",
            f"parent_commit: {PUBLIC_BASE}",
            f"source_manifest_sha256: {source_manifest_sha}",
            f"input_manifest_sha256: {input_manifest_sha}",
            f"attempt_ref: {PUBLIC_ATTEMPT_REF}",
            "formal_data_opened: NO",
            "authorization: SOLE_FORMAL_RUN",
        )
    )
    if body not in (expected_body, expected_body + "\n") or "\r" in body:
        raise PreflightError("public_receipt_body_contract")


def claim_formal_attempt(repository_root: Path, pin_commit: str) -> None:
    """Atomically consume the sole formal attempt in this Git repository."""

    result = subprocess.run(
        ("git", "update-ref", ATTEMPT_REF, pin_commit, ZERO_OID),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        cwd=repository_root,
    )
    if result.returncode or result.stdout or result.stderr:
        raise PreflightError(
            "formal_attempt_already_claimed_or_ref_failed:"
            f"rc={result.returncode}:stdout={result.stdout!r}:stderr={result.stderr!r}"
        )


def claim_public_formal_attempt(
    repository_root: Path,
    pin_commit: str,
) -> None:
    """Atomically publish the sole authorized attempt ref before any data."""

    environment = os.environ.copy()
    environment.update({"LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    result = subprocess.run(
        (
            "gh",
            "api",
            "--hostname",
            "github.com",
            "--method",
            "POST",
            "repos/mathorn1973/twist-j/git/refs",
            "-f",
            f"ref={PUBLIC_ATTEMPT_REF}",
            "-f",
            f"sha={pin_commit}",
        ),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=environment,
    )
    if (
        result.returncode
        or result.stderr
        or not result.stdout
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
    if not isinstance(payload, dict):
        raise PreflightError("public_attempt_ref_response_not_object")
    if payload.get("ref") != PUBLIC_ATTEMPT_REF:
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


def formal_public_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
    pin_receipt: str,
) -> None:
    if Path.cwd().resolve() != repository_root.resolve():
        raise PreflightError("formal_cwd_must_be_repository_root")
    validate_pin_commit(repository_root, pin_commit, require_ancestor=False)
    head = git_stdout(repository_root, "rev-parse", "HEAD").decode("ascii").strip()
    if head != pin_commit:
        raise PreflightError(f"formal_HEAD_not_pin:{head}")
    status = git_stdout(
        repository_root,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
    )
    if status:
        raise PreflightError(f"formal_worktree_not_clean:{status!r}")
    origin = git_stdout(repository_root, "remote", "get-url", "origin").decode(
        "ascii"
    )
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
    pinned_package_preflight(base, repository_root, pin_commit)
    public_receipt_preflight(base, pin_commit, pin_receipt)


def committed_result_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
) -> str:
    """Bind the checked-out trio to the first immutable commit after the pin.

    The first ancestry-path commit is the result commit even when ``HEAD`` is
    a later GitHub PR merge commit whose second-parent history contains the
    pin and result.  Requiring that commit to have only the pin as its parent
    also rejects histories with an intervening or synthetic pre-result commit.
    """

    ancestry = git_stdout(
        repository_root,
        "rev-list",
        "--ancestry-path",
        "--reverse",
        "--topo-order",
        f"{pin_commit}..HEAD",
    ).decode("ascii").splitlines()
    if not ancestry:
        raise PreflightError("replay_result_commit_missing_after_pin")
    result_commit = ancestry[0]
    if LOWER_HEX40_RE.fullmatch(result_commit) is None:
        raise PreflightError(f"replay_result_commit_malformed:{result_commit!r}")
    parents = git_stdout(
        repository_root,
        "rev-list",
        "--parents",
        "-n",
        "1",
        result_commit,
    ).decode("ascii").split()
    if parents != [result_commit, pin_commit]:
        raise PreflightError(f"replay_result_parent_contract:{parents!r}")

    probe_relative = base.relative_to(repository_root).as_posix()
    expected_paths = {
        f"{probe_relative}/{name}"
        for name in POST_RUN_FILES
    }
    changed_paths = git_stdout(
        repository_root,
        "diff-tree",
        "--no-commit-id",
        "--name-only",
        "--no-renames",
        "-r",
        result_commit,
    ).decode("utf-8").splitlines()
    if len(changed_paths) != len(expected_paths) or set(changed_paths) != expected_paths:
        raise PreflightError(
            "replay_result_changed_paths_contract:"
            f"observed={changed_paths!r}:expected={sorted(expected_paths)!r}"
        )

    for name in POST_RUN_FILES:
        current = strict_text(base / name)
        relative = f"{probe_relative}/{name}"
        committed = git_stdout(repository_root, "show", f"{result_commit}:{relative}")
        if current != committed:
            raise PreflightError(f"replay_result_changed_since_commit:{name}")
    return result_commit


def committed_run_preflight(
    base: Path,
    pin_commit: str,
    pin_receipt: str,
) -> None:
    """Bind the replay arguments to the unique fields in committed RUN.md."""

    lines = strict_text(base / "RUN.md").decode("ascii").splitlines()
    commit_fields = [line for line in lines if line.startswith("pin_commit:")]
    receipt_fields = [line for line in lines if line.startswith("pin_receipt:")]
    if len(commit_fields) != 1:
        raise PreflightError(
            f"replay_RUN_pin_commit_cardinality:{len(commit_fields)}"
        )
    if len(receipt_fields) != 1:
        raise PreflightError(
            f"replay_RUN_pin_receipt_cardinality:{len(receipt_fields)}"
        )
    commit_match = re.fullmatch(r"pin_commit: ([0-9a-f]{40})", commit_fields[0])
    receipt_match = re.fullmatch(
        r"pin_receipt: "
        r"(https://github\.com/mathorn1973/twist-j/issues/756#issuecomment-[0-9]+)",
        receipt_fields[0],
    )
    if commit_match is None:
        raise PreflightError("replay_RUN_pin_commit_malformed")
    if receipt_match is None:
        raise PreflightError("replay_RUN_pin_receipt_malformed")
    committed_pin = commit_match.group(1)
    committed_receipt = receipt_match.group(1)
    validate_pin_tokens(committed_pin, committed_receipt)
    if committed_pin != pin_commit:
        raise PreflightError("replay_RUN_pin_commit_argument_mismatch")
    if committed_receipt != pin_receipt:
        raise PreflightError("replay_RUN_pin_receipt_argument_mismatch")


def public_replay_refs_preflight(
    repository_root: Path,
    pin_commit: str,
    result_commit: str,
) -> None:
    """Read back both public refs that jointly authorize deterministic replay."""

    qualification_ref = f"refs/heads/{BRANCH}"
    raw = git_stdout(
        repository_root,
        "ls-remote",
        "--refs",
        PUBLIC_REMOTE,
        PUBLIC_ATTEMPT_REF,
        qualification_ref,
    )
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeDecodeError as error:
        raise PreflightError("replay_public_refs_nonascii") from error
    observed: dict[str, str] = {}
    for line in lines:
        parts = line.split("\t")
        if (
            len(parts) != 2
            or LOWER_HEX40_RE.fullmatch(parts[0]) is None
            or parts[1] in observed
        ):
            raise PreflightError(f"replay_public_refs_malformed:{lines!r}")
        observed[parts[1]] = parts[0]
    expected = {
        PUBLIC_ATTEMPT_REF: pin_commit,
        qualification_ref: result_commit,
    }
    if observed != expected:
        raise PreflightError(
            f"replay_public_refs_contract:observed={observed!r}:expected={expected!r}"
        )


def replay_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
    pin_receipt: str,
) -> None:
    if Path.cwd().resolve() != repository_root.resolve():
        raise PreflightError("replay_cwd_must_be_repository_root")
    status = git_stdout(
        repository_root,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
    )
    if status:
        raise PreflightError(f"replay_worktree_not_clean:{status!r}")
    observed = {path.name for path in base.iterdir()}
    expected = set(PIN_COMMIT_FILES) | set(POST_RUN_FILES)
    if observed != expected:
        raise PreflightError(
            f"replay_inventory:missing={sorted(expected-observed)!r}:"
            f"extra={sorted(observed-expected)!r}"
        )
    validate_pin_commit(repository_root, pin_commit, require_ancestor=True)
    pinned_package_preflight(base, repository_root, pin_commit)
    result_commit = committed_result_preflight(base, repository_root, pin_commit)
    committed_run_preflight(base, pin_commit, pin_receipt)
    public_replay_refs_preflight(repository_root, pin_commit, result_commit)


def chain_custody_lines(
    logs: dict[str, bytes],
    *,
    integrity_failed: bool,
) -> list[str]:
    """Render deterministic raw-log custody without reparsing failed input."""

    lines: list[str] = []
    for chain in FORMAL_SPECS:
        raw = logs[chain.label]
        prefix = f"CHAIN {chain.label} bytes={len(raw)} sha256={sha256(raw)}"
        if integrity_failed:
            lines.append(f"{prefix} status=INTEGRITY_UNPARSED")
            continue
        records = parse_generated_records(raw, chain.label)
        if len(records) != CHECKPOINTS + 2:
            raise PreflightError(f"formal_record_count:{chain.label}")
        summary = records[-1]
        lines.append(
            f"{prefix} transitions={summary.get('total_transitions')} "
            f"final_state_sha256={summary.get('final_state_sha256')}"
        )
    return lines


def validate_modeled_record_shape(logs: dict[str, bytes]) -> None:
    """Reject incomplete streams without interpreting JSON or schema."""

    expected_labels = {chain.label for chain in FORMAL_SPECS}
    if set(logs) != expected_labels:
        raise PreflightError(
            "formal_record_labels:"
            f"missing={sorted(expected_labels - set(logs))!r}:"
            f"extra={sorted(set(logs) - expected_labels)!r}"
        )
    expected_records = CHECKPOINTS + 2
    for chain in FORMAL_SPECS:
        raw = logs[chain.label]
        if not raw.endswith(b"\n"):
            raise PreflightError(f"formal_record_shape:{chain.label}:missing_final_LF")
        records = raw[:-1].split(b"\n")
        has_blank = any(not record for record in records)
        if len(records) != expected_records or has_blank:
            raise PreflightError(
                f"formal_record_shape:{chain.label}:records={len(records)}:"
                f"expected={expected_records}:blank={int(has_blank)}"
            )


def analysis_module(base: Path) -> ModuleType:
    sys.dont_write_bytecode = True
    return load_module("mobility_qualification_analysis", base / "qualification_analysis.py")


def run_chain(
    executable: Path,
    chain: ChainSpec,
    pin_commit: str,
    pin_receipt: str,
) -> tuple[str, bytes]:
    raw = checked_process(
        engine_command(
            executable,
            chain,
            formal=True,
            pin_commit=pin_commit,
            pin_receipt=pin_receipt,
        )
    )
    return chain.label, raw


def qualification_bytes(
    base: Path,
    repository_root: Path,
    pin_commit: str,
    pin_receipt: str,
) -> bytes:
    validate_pin_tokens(pin_commit, pin_receipt)
    source_manifest_sha = parse_manifest(
        base / "SOURCE_SHA256SUMS", base, PINNED_FILES
    )
    input_manifest_sha = parse_manifest(
        base / "INPUT_SHA256SUMS", repository_root, INPUT_FILES
    )
    with build_executable(repository_root) as executable:
        compile_engine(base, executable)
        fixture = fixture_bytes(base, executable)
        expected_fixture = strict_text(base / "FIXTURE_EXPECTED.txt")
        if fixture != expected_fixture:
            raise PreflightError("fixture_expected_mismatch")
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(
                pool.map(
                    lambda chain: run_chain(
                        executable, chain, pin_commit, pin_receipt
                    ),
                    FORMAL_SPECS,
                )
            )

    logs = {label: raw for label, raw in results}
    validate_modeled_record_shape(logs)
    analysis = analysis_module(base)
    expectations = tuple(
        analysis.RunExpectation(
            label=chain.label,
            L=chain.L,
            bitstream_domain=DOMAIN,
            development_only=False,
            seed=chain.seed_token,
            start=chain.start,
            warm_bottom=WARM_BOTTOM,
            checkpoints=CHECKPOINTS,
            thin=THIN,
            validation_stride=VALIDATION_STRIDE,
            transition_cap=TRANSITION_CAP,
        )
        for chain in FORMAL_SPECS
    )
    decision = analysis.analyze_logs(
        logs,
        expectations,
        statistics_path=repository_root / STATS_RELATIVE,
        statistics_sha256=STATS_SHA256,
    )
    integrity_failed = any(
        failure.startswith("INTEGRITY:") for failure in decision.failures
    )
    if integrity_failed:
        terminal = "STOP_MOBILITY_INTEGRITY"
    elif decision.failures:
        terminal = "STOP_MOBILITY_QUALITY"
    else:
        terminal = "DUAL_MOBILITY_QUALIFICATION_PASS"

    lines = [
        f"PROBE {PROBE_ID}",
        f"PIN commit={pin_commit} receipt={pin_receipt}",
        f"SOURCE_CUSTODY PASS manifest_sha256={source_manifest_sha}",
        f"INPUT_CUSTODY PASS manifest_sha256={input_manifest_sha}",
        f"FIXTURE_CUSTODY PASS fixture_sha256={sha256(fixture)}",
    ]
    lines.extend(chain_custody_lines(logs, integrity_failed=integrity_failed))
    lines.extend(decision.lines)
    lines.extend(f"FAILURE {failure}" for failure in decision.failures)
    lines.extend(
        (
            "PROSPECTIVE_MAP L6 warm_bottom=98304 checkpoints=2048 thin=1536 "
            "transition_cap=1073741824",
            "PROSPECTIVE_MAP L8 warm_bottom=262144 checkpoints=2048 thin=4096 "
            "transition_cap=4294967296",
            f"TERMINAL {terminal}",
            "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY",
            "SCOPE L3_L4_ONLY NO_WARD NO_F3 NO_PHASE NO_CANON_MOVEMENT",
        )
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def parse_mode_arguments(arguments: Sequence[str]) -> tuple[str, str, str]:
    if list(arguments) == ["--fixture"]:
        return "fixture", "", ""
    if len(arguments) == 5 and arguments[0] in ("--formal", "--replay"):
        if arguments[1] != "--pin-commit" or arguments[3] != "--pin-receipt":
            raise PreflightError("argument_order")
        return arguments[0][2:], arguments[2], arguments[4]
    raise PreflightError(
        "usage: qualification_run.py --fixture | "
        "--formal|--replay --pin-commit HEX40 --pin-receipt ISSUE_COMMENT_URL"
    )


def main() -> int:
    base = Path(__file__).resolve().parent
    repository_root = base.parent.parent
    try:
        mode, pin_commit, pin_receipt = parse_mode_arguments(sys.argv[1:])
        if mode == "fixture":
            with build_executable(repository_root) as executable:
                compile_engine(base, executable)
                sys.stdout.buffer.write(fixture_bytes(base, executable))
            return 0
        validate_pin_tokens(pin_commit, pin_receipt)
        if mode == "formal":
            formal_public_preflight(
                base, repository_root, pin_commit, pin_receipt
            )
            claim_formal_attempt(repository_root, pin_commit)
            claim_public_formal_attempt(repository_root, pin_commit)
        elif mode == "replay":
            replay_preflight(base, repository_root, pin_commit, pin_receipt)
        else:
            raise AssertionError("unreachable mode")
        output = qualification_bytes(base, repository_root, pin_commit, pin_receipt)
        sys.stdout.buffer.write(output)
        return 0
    except (OSError, PreflightError, RuntimeError, UnicodeError, subprocess.SubprocessError) as error:
        print(f"QUALIFICATION_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
