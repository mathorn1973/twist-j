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
import subprocess
import sys
import tempfile
from typing import Iterable, Sequence


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


def git_result(arguments: Sequence[str]) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            ("git", *arguments),
            cwd=REPOSITORY_ROOT,
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


def deterministic_environment() -> dict[str, str]:
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


def checked_process(
    command: Sequence[str],
    *,
    cwd: Path,
    label: str,
) -> bytes:
    try:
        completed = subprocess.run(
            tuple(command),
            cwd=cwd,
            env=deterministic_environment(),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=PROCESS_TIMEOUT,
        )
    except (OSError, subprocess.SubprocessError) as error:
        raise VerifyFailure(f"process_start:{label}") from error
    if completed.returncode != 0:
        raise VerifyFailure(f"process_exit:{label}:{completed.returncode}")
    if completed.stderr:
        raise VerifyFailure(f"process_stderr:{label}:{len(completed.stderr)}")
    if len(completed.stdout) > PROCESS_CAP:
        raise VerifyFailure(f"process_stdout_cap:{label}")
    if completed.stdout and (
        b"\r" in completed.stdout or not completed.stdout.endswith(b"\n")
    ):
        raise VerifyFailure(f"process_lf:{label}")
    try:
        completed.stdout.decode("ascii")
    except UnicodeDecodeError as error:
        raise VerifyFailure(f"process_ascii:{label}") from error
    return completed.stdout


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
            "-B",
            str(BASE / "supervisor_qualification.py"),
            "--fixture",
        ),
        cwd=BASE,
        label="supervisor_fixture",
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
        path = "legacy-u64" if span < 63 else "cpp-int"
        expect_fields(
            record_fields(lines[offset], "SPAN_KAT"),
            sample_fields((0, -span, -span), path),
            f"span_{span}",
        )

    sum_fields = sample_fields((0, 0, 0, 0, -62), "cpp-int")
    sum_fields["old_guard"] = "orbit_weight_sum_overflow"
    # The source prints old_guard before path; dictionary equality is order-free.
    expect_fields(
        record_fields(lines[11], "SUM_OVERFLOW_KAT"),
        sum_fields,
        "sum_overflow",
    )

    width_fields = sample_fields((0, 0, -62), "cpp-int")
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
        fields = sample_fields(exponents, "cpp-int")
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
