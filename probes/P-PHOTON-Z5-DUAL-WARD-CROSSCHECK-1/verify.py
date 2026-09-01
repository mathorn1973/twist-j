#!/usr/bin/env python3
"""Deterministic verifier for the committed #756 cross-check record."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


SOURCE_FILES = (
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

INPUT_FILES = (
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/PREREG.md",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/README.md",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/dual_cycle_kernel.py",
    "probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/verify.py",
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

RUN_MANIFEST_HEADER = (
    "filename\tkind\tL\tstart\tseed\tthermal\tmeasurements\tbetween"
    "\tbytes\tsha256\texit_code\tstderr_bytes"
)
SAMPLES = 512

OUTPUT_FILES = (
    *(str(spec[0]) for spec in PRIMAL_SPECS),
    *(str(spec[0]) for spec in DUAL_SPECS),
    "PRIMAL_RUNS.tsv",
    "DUAL_RUNS.tsv",
    "ANALYSIS.txt",
)

ALLOWED_TERMINALS = {
    "DUAL_CROSSCHECK_PASS",
    "STOP_DUAL_MIXING",
    "STOP_DUAL_INTEGRITY",
    "BREAK_DUAL_DICTIONARY",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot_load_{name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def parse_manifest(
    manifest: Path,
    root: Path,
    expected_names: tuple[str, ...],
) -> None:
    raw = manifest.read_bytes()
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise RuntimeError(f"{manifest.name}_newlines")
    entries: list[tuple[str, str]] = []
    for line in raw.decode("ascii").splitlines():
        parts = line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64:
            raise RuntimeError(f"{manifest.name}_malformed")
        digest, name = parts
        if any(character not in "0123456789abcdef" for character in digest):
            raise RuntimeError(f"{manifest.name}_digest")
        entries.append((digest, name))
    if tuple(name for _, name in entries) != expected_names:
        raise RuntimeError(f"{manifest.name}_inventory")
    for expected, name in entries:
        path = root / name
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"{manifest.name}_nonregular:{name}")
        if sha256(path.read_bytes()) != expected:
            raise RuntimeError(f"{manifest.name}_mismatch:{name}")


def transcript_bytes(path: Path) -> tuple[bytes, list[str]]:
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"run_transcript_nonregular:{path.name}")
    raw = path.read_bytes()
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise RuntimeError(f"run_transcript_newlines:{path.name}")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeDecodeError as error:
        raise RuntimeError(f"run_transcript_nonascii:{path.name}") from error
    return raw, lines


def validate_primal_transcript(
    name: str,
    lines: list[str],
    spec: tuple[object, ...],
) -> None:
    _, L, start, seed, thermal, between = spec
    expected_header = (
        "RUN model=TWIST_Z5_FACE_WEIGHT_V1 "
        "dependency=P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2 "
        f"L={L} seed=0x{int(seed):016x} start={start} "
        f"thermal_cycles={thermal} measurements={SAMPLES} "
        f"between_cycles={between}"
    )
    if len(lines) != SAMPLES + 2 or lines[0] != expected_header:
        raise RuntimeError(f"primal_transcript_layout_or_header:{name}")
    for index, line in enumerate(lines[1:-1]):
        if not line.startswith(f"SAMPLE index={index} "):
            raise RuntimeError(f"primal_transcript_sample_index:{name}:{index}")
    if not lines[-1].startswith("SUMMARY ") or not lines[-1].endswith(
        " status=PASS"
    ):
        raise RuntimeError(f"primal_transcript_summary:{name}")


def validate_dual_transcript(
    name: str,
    lines: list[str],
    spec: tuple[object, ...],
) -> None:
    _, L, start, seed, thermal, between = spec
    if len(lines) != SAMPLES + 2:
        raise RuntimeError(f"dual_transcript_layout:{name}")
    try:
        records = [json.loads(line) for line in lines]
    except json.JSONDecodeError as error:
        raise RuntimeError(f"dual_transcript_json:{name}") from error
    if any(not isinstance(record, dict) for record in records):
        raise RuntimeError(f"dual_transcript_record_type:{name}")
    header = records[0]
    expected_header = {
        "L": L,
        "between_steps": between,
        "domain": "dual756",
        "mode": "decision",
        "samples": SAMPLES,
        "seed": f"0x{int(seed):032x}",
        "start": start,
        "thermal_steps": thermal,
        "type": "run",
    }
    if any(header.get(key) != value for key, value in expected_header.items()):
        raise RuntimeError(f"dual_transcript_header:{name}")
    for index, record in enumerate(records[1:-1]):
        if record.get("type") != "sample" or record.get("index") != index:
            raise RuntimeError(f"dual_transcript_sample_index:{name}:{index}")
    summary = records[-1]
    if summary.get("type") != "summary" or summary.get("samples_emitted") != SAMPLES:
        raise RuntimeError(f"dual_transcript_summary:{name}")


def parse_run_manifest(
    base: Path,
    manifest_name: str,
    specs: tuple[tuple[object, ...], ...],
    kind: str,
) -> None:
    path = base / manifest_name
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"{manifest_name}_nonregular")
    raw = path.read_bytes()
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise RuntimeError(f"{manifest_name}_newlines")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeDecodeError as error:
        raise RuntimeError(f"{manifest_name}_nonascii") from error
    if len(lines) != len(specs) + 1 or not lines or lines[0] != RUN_MANIFEST_HEADER:
        raise RuntimeError(f"{manifest_name}_header_or_row_count")

    for row_index, (line, spec) in enumerate(zip(lines[1:], specs)):
        name, L, start, seed, thermal, between = spec
        transcript, transcript_lines = transcript_bytes(base / str(name))
        expected = (
            str(name),
            kind,
            str(L),
            str(start),
            f"0x{int(seed):016x}",
            str(thermal),
            str(SAMPLES),
            str(between),
            str(len(transcript)),
            sha256(transcript),
            "0",
            "0",
        )
        fields = tuple(line.split("\t"))
        if fields != expected:
            raise RuntimeError(f"{manifest_name}_row:{row_index}:{name}")
        if kind == "primal_replay":
            validate_primal_transcript(str(name), transcript_lines, spec)
        elif kind == "dual_independent":
            validate_dual_transcript(str(name), transcript_lines, spec)
        else:
            raise RuntimeError(f"{manifest_name}_unknown_kind")


def fixture(base: Path, repository_root: Path) -> None:
    fresh = load_module("dual_ward_fresh", base / "dual_chain.py")
    frozen = load_module(
        "dual_ward_frozen",
        repository_root
        / "probes"
        / "P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1"
        / "dual_cycle_kernel.py",
    )
    results: list[tuple[int, int, int, str]] = []
    for L, steps, seed in ((2, 2000, 0x75620260901), (3, 750, 0x7560301)):
        old_lattice = frozen.Torus4(L)
        old_state = [0] * old_lattice.n_plaq
        old_rng = frozen.BitStream(seed)
        new_chain = fresh.DualChain(fresh.Torus4(L), seed, "cold")
        for _ in range(steps):
            old_state, _ = frozen.metropolis_step(old_lattice, old_state, old_rng)
            new_chain.step()
        old_bytes = bytes(value % 5 for value in old_state)
        new_bytes = bytes(new_chain.state)
        if old_bytes != new_bytes:
            raise RuntimeError(f"kernel_equivalence_L{L}")
        state_hash = sha256(new_bytes)
        if L == 2 and state_hash != "580174dde4d285c6763bb69db5478bf2e90f56de9dfa08176e3e27a6ba2a2188":
            raise RuntimeError("frozen_L2_hash")
        results.append((L, steps, new_chain.support, state_hash))

    surface = fresh.DualChain(fresh.Torus4(2), 0x7560201, "surface")
    current = fresh.validate_state(surface.lattice, surface.state, surface.support)
    fresh.validate_current_conservation(surface.lattice, current)
    print("FIXTURE P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1")
    for L, steps, support, state_hash in results:
        print(
            f"KERNEL_EQUIVALENCE L={L} steps={steps} support={support} "
            f"state_sha256={state_hash} status=PASS"
        )
    print(
        "SURFACE_START L=2 support="
        f"{surface.support} closure=PASS integer_current=PASS partial_j=PASS"
    )
    print("FIXTURE_RESULT PASS")


def final_verify(base: Path, repository_root: Path) -> None:
    parse_manifest(base / "SOURCE_SHA256SUMS", base, SOURCE_FILES)
    parse_manifest(base / "INPUT_SHA256SUMS", repository_root, INPUT_FILES)
    parse_manifest(base / "OUTPUT_SHA256SUMS", base, OUTPUT_FILES)
    parse_run_manifest(base, "PRIMAL_RUNS.tsv", PRIMAL_SPECS, "primal_replay")
    parse_run_manifest(base, "DUAL_RUNS.tsv", DUAL_SPECS, "dual_independent")
    analysis = (base / "ANALYSIS.txt").read_bytes()
    replay = subprocess.run(
        (sys.executable, "-B", str(base / "analyze_crosscheck.py")),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        cwd=base,
    )
    if replay.returncode != 0 or replay.stderr or replay.stdout != analysis:
        raise RuntimeError("analysis_replay")
    lines = analysis.decode("ascii").splitlines()
    terminals = [line.split()[1] for line in lines if line.startswith("TERMINAL ")]
    if len(terminals) != 1 or terminals[0] not in ALLOWED_TERMINALS:
        raise RuntimeError("terminal_grammar")
    if not lines or lines[-1] != "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY":
        raise RuntimeError("evidential_status")
    print("PROBE P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1")
    print(
        "SOURCE_CUSTODY PASS manifest_sha256="
        + sha256((base / "SOURCE_SHA256SUMS").read_bytes())
    )
    print(
        "INPUT_CUSTODY PASS manifest_sha256="
        + sha256((base / "INPUT_SHA256SUMS").read_bytes())
    )
    print(
        "OUTPUT_CUSTODY PASS manifest_sha256="
        + sha256((base / "OUTPUT_SHA256SUMS").read_bytes())
    )
    print("ANALYSIS_REPLAY PASS analysis_sha256=" + sha256(analysis))
    print("TERMINAL " + terminals[0])
    print("EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY")


def main() -> int:
    base = Path(__file__).resolve().parent
    repository_root = base.parent.parent
    try:
        if sys.argv[1:] == ["--fixture"]:
            fixture(base, repository_root)
        elif len(sys.argv) == 1:
            final_verify(base, repository_root)
        else:
            print("usage: python3 verify.py [--fixture]", file=sys.stderr)
            return 64
        return 0
    except (OSError, RuntimeError, UnicodeError, subprocess.SubprocessError) as error:
        print(f"VERIFY_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
