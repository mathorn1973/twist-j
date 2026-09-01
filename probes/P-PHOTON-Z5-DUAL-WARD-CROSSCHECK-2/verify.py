#!/usr/bin/env python3
"""Deterministic committed-record verifier for CROSSCHECK-2.

The verifier never compiles or invokes a Monte Carlo engine.  It validates
custody, redecodes the retained state frames through ``state_reader.py`` and
reruns ``analyze_crosscheck2.py`` over the committed raw transcripts.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
import subprocess
import sys
from typing import Sequence

import run_crosscheck2 as runner


SOURCE_FILES = runner.SOURCE_FILES

# Every listed byte is intentionally opened by manifest verification.  This
# includes the immutable component/governance dependencies as well as source
# and raw inputs imported or compiled by the pinned package.  No consumed
# CROSSCHECK-1 dual transcript is present.
INPUT_FILES = (
    "notes/canon/PHOTON-PRODUCTION-PREREG-FREEZE-1.md",
    "notes/canon/PHOTON-PRODUCTION-PREREG-FREEZE-1.schema.json",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/PREREG.md",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/README.md",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/dual_cycle_kernel.py",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/verify.py",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/RESULT.md",
    "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/PREREG.md",
    "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_chain.py",
    "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/analyze_crosscheck.py",
    "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/primal_replay.cpp",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/PREREG.md",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/QUALIFICATION_PIN.md",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/RESULT.md",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/RUN.md",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/EXPECTED.txt",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/SOURCE_SHA256SUMS",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/INPUT_SHA256SUMS",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/qualification_engine.cpp",
    "probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/qualification_analysis.py",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/SHA256SUMS",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5.cpp",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5_part1.inc",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5_part2.inc",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5_part3.inc",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5_part4.inc",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/analyze_pilot.py",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_cold_r1.log",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_cold_r2.log",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_hot_r1.log",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_hot_r2.log",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_cold_r1.log",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_cold_r2.log",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_hot_r1.log",
    "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_hot_r2.log",
)

PRIMAL_HEADER = (
    "filename\tkind\tL\tstart\tseed\tthermal\tmeasurements\tbetween"
    "\tbytes\tsha256\texit_code\tstderr_bytes"
)
DUAL_HEADER = (
    "filename\tkind\tL\tstart\treplica\tseed\tseed_sha256\twarm_bottom"
    "\tcheckpoints\tthin\tvalidation_stride\ttransition_cap"
    "\tengine_pipe_cap\tengine_pipe_bytes\tengine_pipe_sha256"
    "\treader_cap\tbytes\tsha256\tengine_exit\treader_exit"
    "\tengine_stderr_bytes\treader_stderr_bytes"
)
LOWER_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
ALLOWED_TERMINALS = {
    "DUAL_CROSSCHECK_PASS",
    "STOP_DUAL_MIXING",
    "STOP_DUAL_INTEGRITY",
    "BREAK_DUAL_DICTIONARY",
}


class VerificationError(RuntimeError):
    """A deterministic custody or replay contract failed."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strict_text(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise VerificationError(f"nonregular:{path}")
    raw = path.read_bytes()
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise VerificationError(f"newline_contract:{path.name}")
    try:
        raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise VerificationError(f"nonascii:{path.name}") from error
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
        if len(parts) != 2 or LOWER_SHA256.fullmatch(parts[0]) is None:
            raise VerificationError(f"malformed_manifest:{manifest.name}")
        if any(name == parts[1] for _, name in entries):
            raise VerificationError(f"duplicate_manifest_entry:{manifest.name}:{parts[1]}")
        entries.append((parts[0], parts[1]))
    if tuple(name for _, name in entries) != tuple(expected_names):
        raise VerificationError(f"manifest_inventory:{manifest.name}")
    for expected, name in entries:
        path = root / name
        if path.is_symlink() or not path.is_file():
            raise VerificationError(f"manifest_nonregular:{manifest.name}:{name}")
        if sha256(path.read_bytes()) != expected:
            raise VerificationError(f"manifest_mismatch:{manifest.name}:{name}")
    return sha256(raw)


def parse_primal_manifest(base: Path) -> None:
    lines = strict_text(base / "PRIMAL_RUNS.tsv").decode("ascii").splitlines()
    if len(lines) != len(runner.PRIMAL_SPECS) + 1 or lines[0] != PRIMAL_HEADER:
        raise VerificationError("PRIMAL_RUNS_header_or_count")
    for index, (line, spec) in enumerate(zip(lines[1:], runner.PRIMAL_SPECS)):
        raw = strict_text(base / spec.name)
        expected = (
            spec.name,
            "primal_replay",
            str(spec.L),
            spec.start,
            spec.seed_token,
            str(spec.thermal),
            "512",
            str(spec.between),
            str(len(raw)),
            sha256(raw),
            "0",
            "0",
        )
        if tuple(line.split("\t")) != expected:
            raise VerificationError(f"PRIMAL_RUNS_row:{index}:{spec.name}")
        if len(raw) != spec.expected_bytes or sha256(raw) != spec.expected_sha256:
            raise VerificationError(f"primal_not_byte_identical:{spec.name}")


def canonical_uint(text: str, where: str) -> int:
    if not text or (text != "0" and text.startswith("0")) or not text.isascii() or not text.isdigit():
        raise VerificationError(f"noncanonical_uint:{where}")
    return int(text)


def parse_dual_manifest(base: Path) -> None:
    lines = strict_text(base / "DUAL_RUNS.tsv").decode("ascii").splitlines()
    if len(lines) != len(runner.DUAL_SPECS) + 1 or lines[0] != DUAL_HEADER:
        raise VerificationError("DUAL_RUNS_header_or_count")
    for index, (line, spec) in enumerate(zip(lines[1:], runner.DUAL_SPECS)):
        fields = tuple(line.split("\t"))
        if len(fields) != 22:
            raise VerificationError(f"DUAL_RUNS_field_count:{index}:{spec.name}")
        raw = strict_text(base / spec.name)
        fixed = (
            spec.name,
            "exact_wrapper_filtered",
            str(spec.L),
            spec.start,
            str(spec.replica),
            spec.seed_token,
            spec.seed_sha256,
            str(spec.warm_bottom),
            str(spec.checkpoints),
            str(spec.thin),
            str(spec.validation_stride),
            str(spec.transition_cap),
            str(spec.engine_pipe_cap),
        )
        if fields[:13] != fixed:
            raise VerificationError(f"DUAL_RUNS_fixed_fields:{index}:{spec.name}")
        engine_bytes = canonical_uint(fields[13], f"{spec.name}:engine_pipe_bytes")
        if engine_bytes <= 0 or engine_bytes > spec.engine_pipe_cap:
            raise VerificationError(f"DUAL_RUNS_engine_pipe_cap:{spec.name}")
        if LOWER_SHA256.fullmatch(fields[14]) is None:
            raise VerificationError(f"DUAL_RUNS_engine_pipe_sha256:{spec.name}")
        expected_tail = (
            str(runner.FINAL_DUAL_CAP),
            str(len(raw)),
            sha256(raw),
            "0",
            "0",
            "0",
            "0",
        )
        if fields[15:] != expected_tail:
            raise VerificationError(f"DUAL_RUNS_output_fields:{index}:{spec.name}")
        if len(raw) > runner.FINAL_DUAL_CAP:
            raise VerificationError(f"dual_output_cap:{spec.name}")
        records = raw[:-1].split(b"\n")
        if len(records) != spec.checkpoints + 2 or any(not record for record in records):
            raise VerificationError(f"dual_output_shape:{spec.name}")


def analysis_replay(base: Path, repository_root: Path) -> tuple[bytes, str]:
    analysis = strict_text(base / "ANALYSIS.txt")
    result = runner.bounded_process(
        (sys.executable, "-B", str(base / "analyze_crosscheck2.py")),
        cwd=repository_root,
        max_stdout=runner.ANALYSIS_CAP,
        max_stderr=runner.STDERR_CAP,
        timeout=3_600,
    )
    if result.returncode or result.stderr or result.stdout != analysis:
        raise VerificationError(
            f"analysis_replay:rc={result.returncode}:stderr={result.stderr!r}:"
            f"stdout_match={int(result.stdout == analysis)}"
        )
    lines = analysis.decode("ascii").splitlines()
    terminals = [line.split()[1] for line in lines if line.startswith("TERMINAL ")]
    if len(terminals) != 1 or terminals[0] not in ALLOWED_TERMINALS:
        raise VerificationError(f"terminal_grammar:{terminals!r}")
    if not lines or lines[-1] != "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY":
        raise VerificationError("evidential_status")
    return analysis, terminals[0]


def verification_bytes(
    base: Path,
    repository_root: Path,
    pin_commit: str,
    pin_receipt: str,
) -> bytes:
    source_sha = parse_manifest(base / "SOURCE_SHA256SUMS", base, SOURCE_FILES)
    input_sha = parse_manifest(base / "INPUT_SHA256SUMS", repository_root, INPUT_FILES)
    output_sha = parse_manifest(
        base / "OUTPUT_SHA256SUMS", base, runner.OUTPUT_FILES
    )
    parse_primal_manifest(base)
    parse_dual_manifest(base)
    analysis, terminal = analysis_replay(base, repository_root)
    lines = (
        f"PROBE {runner.PROBE_ID}",
        f"PIN commit={pin_commit} receipt={pin_receipt}",
        f"SOURCE_CUSTODY PASS manifest_sha256={source_sha}",
        f"INPUT_CUSTODY PASS manifest_sha256={input_sha}",
        f"OUTPUT_CUSTODY PASS manifest_sha256={output_sha}",
        f"ANALYSIS_REPLAY PASS analysis_sha256={sha256(analysis)}",
        f"TERMINAL {terminal}",
        "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def git_stdout(repository_root: Path, *arguments: str) -> bytes:
    result = runner.bounded_process(
        ("git", *arguments),
        cwd=repository_root,
        max_stdout=16_777_216,
        max_stderr=1_048_576,
        timeout=300,
    )
    if result.returncode or result.stderr:
        raise VerificationError(f"git_{arguments[0]}_failed:{result.stderr!r}")
    return result.stdout


def validate_pin_commit(repository_root: Path, pin_commit: str, *, require_ancestor: bool) -> None:
    resolved = git_stdout(
        repository_root, "rev-parse", "--verify", f"{pin_commit}^{{commit}}"
    ).decode("ascii").strip()
    if resolved != pin_commit:
        raise VerificationError(f"pin_commit_not_exact:{resolved}")
    parents = git_stdout(
        repository_root, "rev-list", "--parents", "-n", "1", pin_commit
    ).decode("ascii").split()
    if parents != [pin_commit, runner.PUBLIC_BASE]:
        raise VerificationError(f"pin_parent_contract:{parents!r}")
    if require_ancestor:
        result = runner.bounded_process(
            ("git", "merge-base", "--is-ancestor", pin_commit, "HEAD"),
            cwd=repository_root,
            max_stdout=4_096,
            max_stderr=65_536,
            timeout=60,
        )
        if result.returncode or result.stdout or result.stderr:
            raise VerificationError("pin_not_ancestor_of_HEAD")


def pinned_package_preflight(base: Path, repository_root: Path, pin_commit: str) -> None:
    probe_relative = base.relative_to(repository_root).as_posix()
    expected_paths = {
        f"{probe_relative}/{name}" for name in runner.PIN_COMMIT_FILES
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
        raise VerificationError(
            "pin_changed_paths:"
            f"observed={changed!r}:expected={sorted(expected_paths)!r}"
        )
    for name in runner.PIN_COMMIT_FILES:
        current = base / name
        if current.is_symlink() or not current.is_file():
            raise VerificationError(f"pinned_package_nonregular:{name}")
        relative = current.relative_to(repository_root).as_posix()
        if current.read_bytes() != git_stdout(repository_root, "show", f"{pin_commit}:{relative}"):
            raise VerificationError(f"pinned_package_changed:{name}")


def parse_committed_run(base: Path) -> tuple[str, str]:
    raw = strict_text(base / "RUN.md")
    lines = raw.decode("ascii").splitlines()
    if len(lines) != 30:
        raise VerificationError(f"RUN_line_count:{len(lines)}")
    commit = re.fullmatch(r"pin_commit: ([0-9a-f]{40})", lines[2])
    receipt = re.fullmatch(
        r"pin_receipt: (https://github\.com/mathorn1973/twist-j/issues/756#issuecomment-[0-9]+)",
        lines[3],
    )
    if commit is None or receipt is None:
        raise VerificationError("RUN_pin_field_syntax")
    pin_commit, pin_receipt = commit.group(1), receipt.group(1)
    runner.validate_pin_tokens(pin_commit, pin_receipt)
    receipt_body_sha = sha256(
        runner.expected_public_receipt_body(base, pin_commit).encode("utf-8")
    )
    raw_bytes = sum(
        len((base / name).read_bytes())
        for name in runner.PRIMAL_OUTPUTS + runner.DUAL_OUTPUTS
    )
    output_bytes = sum(
        len((base / name).read_bytes()) for name in runner.OUTPUT_FILES
    )
    expected = runner.run_record_bytes(
        pin_commit,
        pin_receipt,
        sha256(strict_text(base / "SOURCE_SHA256SUMS")),
        sha256(strict_text(base / "INPUT_SHA256SUMS")),
        strict_text(base / "OUTPUT_SHA256SUMS"),
        strict_text(base / "ANALYSIS.txt"),
        receipt_body_sha,
        raw_bytes,
        output_bytes,
    )
    if raw != expected:
        raise VerificationError("RUN_exact_schema_or_digest_mismatch")
    return pin_commit, pin_receipt


def parse_committed_result(base: Path) -> str:
    analysis = strict_text(base / "ANALYSIS.txt")
    terminal = runner.analysis_terminal(analysis)
    expected = runner.result_record_bytes(
        terminal,
        strict_text(base / "OUTPUT_SHA256SUMS"),
        analysis,
    )
    if strict_text(base / "RESULT.md") != expected:
        raise VerificationError("RESULT_exact_schema_terminal_or_digest_mismatch")
    return terminal


def result_commit_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
) -> str:
    ancestry = git_stdout(
        repository_root,
        "rev-list",
        "--ancestry-path",
        "--reverse",
        "--topo-order",
        f"{pin_commit}..HEAD",
    ).decode("ascii").splitlines()
    if not ancestry:
        raise VerificationError("result_commit_missing")
    result_commit = ancestry[0]
    if runner.LOWER_HEX40_RE.fullmatch(result_commit) is None:
        raise VerificationError("result_commit_malformed")
    parents = git_stdout(
        repository_root, "rev-list", "--parents", "-n", "1", result_commit
    ).decode("ascii").split()
    if parents != [result_commit, pin_commit]:
        raise VerificationError(f"result_parent_contract:{parents!r}")

    probe_relative = base.relative_to(repository_root).as_posix()
    expected_names = set(runner.POST_RUN_FILES)
    expected_paths = {f"{probe_relative}/{name}" for name in expected_names}
    changed = git_stdout(
        repository_root,
        "diff-tree",
        "--no-commit-id",
        "--name-only",
        "--no-renames",
        "-r",
        result_commit,
    ).decode("utf-8").splitlines()
    if len(changed) != len(expected_paths) or set(changed) != expected_paths:
        raise VerificationError(
            f"result_changed_paths:observed={changed!r}:expected={sorted(expected_paths)!r}"
        )
    for name in runner.POST_RUN_FILES:
        current = strict_text(base / name)
        relative = f"{probe_relative}/{name}"
        if current != git_stdout(repository_root, "show", f"{result_commit}:{relative}"):
            raise VerificationError(f"result_file_changed:{name}")
    return result_commit


def public_refs_preflight(
    repository_root: Path,
    pin_commit: str,
    branch_commit: str,
) -> None:
    branch_ref = f"refs/heads/{runner.BRANCH}"
    raw = git_stdout(
        repository_root,
        "ls-remote",
        "--refs",
        runner.PUBLIC_REMOTE,
        runner.PUBLIC_ATTEMPT_REF,
        branch_ref,
    )
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeDecodeError as error:
        raise VerificationError("public_refs_nonascii") from error
    observed: dict[str, str] = {}
    for line in lines:
        parts = line.split("\t")
        if (
            len(parts) != 2
            or runner.LOWER_HEX40_RE.fullmatch(parts[0]) is None
            or parts[1] in observed
        ):
            raise VerificationError(f"public_refs_malformed:{lines!r}")
        observed[parts[1]] = parts[0]
    expected = {
        runner.PUBLIC_ATTEMPT_REF: pin_commit,
        branch_ref: branch_commit,
    }
    if observed != expected:
        raise VerificationError(
            f"public_refs_contract:observed={observed!r}:expected={expected!r}"
        )


def formal_capture_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
) -> None:
    if Path.cwd().resolve() != repository_root.resolve():
        raise VerificationError("formal_capture_cwd_must_be_repository_root")
    validate_pin_commit(repository_root, pin_commit, require_ancestor=False)
    head = git_stdout(repository_root, "rev-parse", "HEAD").decode("ascii").strip()
    if head != pin_commit:
        raise VerificationError("formal_capture_HEAD_not_pin")
    local_attempt = git_stdout(
        repository_root, "rev-parse", "--verify", runner.ATTEMPT_REF
    ).decode("ascii").strip()
    if local_attempt != pin_commit:
        raise VerificationError("formal_capture_local_attempt_ref")
    public_refs_preflight(repository_root, pin_commit, pin_commit)
    pinned_package_preflight(base, repository_root, pin_commit)
    expected = set(runner.PIN_COMMIT_FILES) | set(runner.OUTPUT_FILES) | {
        "OUTPUT_SHA256SUMS",
        "RUN.md",
        "RESULT.md",
    }
    observed = {path.name for path in base.iterdir()}
    if observed != expected:
        raise VerificationError(
            f"formal_capture_inventory:missing={sorted(expected-observed)!r}:"
            f"extra={sorted(observed-expected)!r}"
        )


def replay_preflight(
    base: Path,
    repository_root: Path,
    pin_commit: str,
) -> None:
    if Path.cwd().resolve() != repository_root.resolve():
        raise VerificationError("replay_cwd_must_be_repository_root")
    status = git_stdout(
        repository_root, "status", "--porcelain=v1", "--untracked-files=all"
    )
    if status:
        raise VerificationError(f"replay_worktree_not_clean:{status!r}")
    expected = set(runner.PIN_COMMIT_FILES) | set(runner.POST_RUN_FILES)
    observed = {path.name for path in base.iterdir()}
    if observed != expected:
        raise VerificationError(
            f"replay_inventory:missing={sorted(expected-observed)!r}:"
            f"extra={sorted(observed-expected)!r}"
        )
    validate_pin_commit(repository_root, pin_commit, require_ancestor=True)
    pinned_package_preflight(base, repository_root, pin_commit)
    result_commit = result_commit_preflight(base, repository_root, pin_commit)
    public_refs_preflight(repository_root, pin_commit, result_commit)


def parse_arguments(arguments: Sequence[str]) -> tuple[str, str, str]:
    if not arguments:
        return "replay", "", ""
    if len(arguments) == 5 and arguments[0] == "--formal-capture":
        if arguments[1] != "--pin-commit" or arguments[3] != "--pin-receipt":
            raise VerificationError("argument_order")
        return "formal-capture", arguments[2], arguments[4]
    raise VerificationError(
        "usage: verify.py | --formal-capture --pin-commit HEX40 "
        "--pin-receipt ISSUE_COMMENT_URL"
    )


def main() -> int:
    base = Path(__file__).resolve().parent
    repository_root = base.parent.parent
    try:
        mode, pin_commit, pin_receipt = parse_arguments(sys.argv[1:])
        if mode == "formal-capture":
            runner.validate_pin_tokens(pin_commit, pin_receipt)
            formal_capture_preflight(base, repository_root, pin_commit)
            recorded_commit, recorded_receipt = parse_committed_run(base)
            if (recorded_commit, recorded_receipt) != (pin_commit, pin_receipt):
                raise VerificationError("formal_capture_RUN_pin_mismatch")
            parse_committed_result(base)
        else:
            pin_commit, pin_receipt = parse_committed_run(base)
            parse_committed_result(base)
            replay_preflight(base, repository_root, pin_commit)
        output = verification_bytes(
            base, repository_root, pin_commit, pin_receipt
        )
        if mode == "replay" and output != strict_text(base / "EXPECTED.txt"):
            raise VerificationError("EXPECTED_replay_mismatch")
        sys.stdout.buffer.write(output)
        return 0
    except (
        OSError,
        VerificationError,
        RuntimeError,
        UnicodeError,
        subprocess.SubprocessError,
    ) as error:
        print(f"VERIFY_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
