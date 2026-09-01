#!/usr/bin/env python3
"""Exact public-path exceptions for the repository file policy."""

from __future__ import annotations

from pathlib import Path, PurePosixPath


FORBIDDEN_SUFFIXES = frozenset(
    {
        ".bak",
        ".bin",
        ".dll",
        ".dylib",
        ".env",
        ".exe",
        ".jam",
        ".jsonl",
        ".key",
        ".log",
        ".pem",
        ".pt",
        ".pth",
        ".pyc",
        ".so",
        ".token",
    }
)

PUBLIC_PROBE_TRANSCRIPTS = frozenset(
    {
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_cold_r1.log",
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_cold_r2.log",
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_hot_r1.log",
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L6_hot_r2.log",
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_cold_r1.log",
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_cold_r2.log",
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_hot_r1.log",
        "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/L8_hot_r2.log",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/primal_L6_cold_r1.log",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/primal_L6_hot_r1.log",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/primal_L8_cold_r1.log",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/primal_L8_hot_r1.log",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L6_cold_r1.jsonl",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L6_cold_r2.jsonl",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L6_surface_r1.jsonl",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L6_surface_r2.jsonl",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L8_cold_r1.jsonl",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L8_cold_r2.jsonl",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L8_surface_r1.jsonl",
        "probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/dual_L8_surface_r2.jsonl",
    }
)


def repository_key(relative: Path | PurePosixPath | str) -> str:
    """Return one stable slash-separated repository-relative key."""

    if isinstance(relative, str):
        return PurePosixPath(relative.replace("\\", "/")).as_posix()
    return PurePosixPath(relative.as_posix()).as_posix()


def is_forbidden_repository_file(relative: Path | PurePosixPath | str) -> bool:
    """Apply suffix policy with only the exact public transcript exceptions."""

    key = repository_key(relative)
    path = PurePosixPath(key)
    if path.name.startswith(".env"):
        return True
    if path.suffix.lower() not in FORBIDDEN_SUFFIXES:
        return False
    return key not in PUBLIC_PROBE_TRANSCRIPTS


def public_transcript_integrity_problem(
    path: Path, relative: Path | PurePosixPath | str
) -> str | None:
    """Return why an allowlisted transcript is not safe printable LF text."""

    if repository_key(relative) not in PUBLIC_PROBE_TRANSCRIPTS:
        return None
    if path.is_symlink() or not path.is_file():
        return "must be a regular non-symlink file"
    try:
        data = path.read_bytes()
    except OSError as error:
        return f"cannot be read ({error.__class__.__name__})"
    if not data or not data.endswith(b"\n") or b"\r" in data:
        return "must be nonempty LF-only text with a final LF"
    if any(byte != 10 and not 32 <= byte <= 126 for byte in data):
        return "must contain only printable ASCII and LF"
    return None
