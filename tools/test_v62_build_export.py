#!/usr/bin/env python3
"""Temporary non-canonical builder/exporter for the frozen Public Canon v62 maintenance fold."""

from __future__ import annotations

import base64
import csv
from dataclasses import dataclass
import hashlib
import io
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
import zipfile

CLAIM = "J-ODD-MOTOR-MEDIATED-BRIDGE"
OLD_PATH = "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2"
OLD_HASH = "03db973566ae068b5ed8eb65f4e79ae13af398ac067f325c26a25c1553bf636b"
NEW_PATH = "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2"
NEW_HASH = "f6b2ca8bf117ee709eba29356b4e5ad61e60801c1975e5405cab1fefbbaa624b"
SCOPE_HASH = "a1f5d43376bafced23478edd0857dfc2c2d1566ee960db32e8d67d493191ad9a"
FROZEN_BASE = "d9841380d137bdf7d1465b71af96e8733f69b536"
CHANGELOG_HEADER = "# Canon changelog (public series)"
CURRENT_COUNTS_BEGIN = "<!-- BEGIN GENERATED CURRENT COUNTS -->"
CURRENT_COUNTS_END = "<!-- END GENERATED CURRENT COUNTS -->"
EXPECTED_CHANGELOG_BYTES = 127430
EXPECTED_HISTORICAL_MARKER_BYTES_REMOVED = 156

EXPORT_FILES = (
    "canon/CANON.md",
    "canon/CHANGELOG.md",
    "canon/CORE.md",
    "canon/EVIDENCE.tsv",
    "canon/FRONTIER.md",
    "canon/HISTORY.tsv",
    "canon/REGISTRY.tsv",
    "canon/SHA256SUMS",
    "canon/STATUS_COUNTS.tsv",
    "reproduce/status-separation/EXPECTED.txt",
    "reproduce/status-separation/README.md",
    "reproduce/status-separation/verify.py",
)
EXPECTED_CONTENT_CHANGED_FILES = tuple(
    path for path in EXPORT_FILES
    if path not in ("canon/FRONTIER.md", "canon/STATUS_COUNTS.tsv")
)
EXPORT_FILE_COUNT = 12
EXPORT_MANIFEST_HEADER = "relative_path\tbyte_count\tsha256\n"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
ZIP_CREATE_SYSTEM = 3
ZIP_CREATE_VERSION = 20
ZIP_EXTRACT_VERSION = 20
ZIP_EXTERNAL_ATTR = (stat.S_IFREG | 0o644) << 16
ZIP_COMPRESSION = zipfile.ZIP_DEFLATED
ZIP_COMPRESSION_LEVEL = 9
EXPECTED_EXPORT_MANIFEST_SHA256 = "3a8d89bb6670a6a86935bb22e9711023928f53477ac49f596d14de72d1f44334"
EXPECTED_ZIP_SHA256 = "2934a42d953cfdca623678d870a1dc071616d76b9df32c5b84c1c08710196173"
EXPECTED_ZIP_BYTES = 399222
EXPECTED_CHANGELOG_SHA256 = "92c968bee0329d8580500a3bd328ba2f6816d8ebec043e88838624286bcb19f4"
EXPECTED_SHA256SUMS_SHA256 = "236a4eaeab3412fb86478683799f3becb96464273e39b209c6277e07ce58c9e7"

UNCHANGED_CERTIFIED_FILES = {
    "canon/CANON.md": (334109, "1575eedbbe9e6b6e20e0e49decc5a4a8aaeb264f54a950860a677b740634351d"),
    "canon/CORE.md": (11304, "232da1e23686263453339751650783d77ecb69569825a3c6e55966fa9f669bb1"),
    "canon/EVIDENCE.tsv": (63218, "6930149081b0381184976771dbf3b820a23548e13066bec9676fb8d2a478be3d"),
    "canon/FRONTIER.md": (26974, "a761f327261d1d07a216f84d470f5cd46a21b8754cb18f772b18c79e0e5f5f3d"),
    "canon/HISTORY.tsv": (353467, "a5c16e5d8441d035632b4ec0e3548bf925b297e6d2a7a9ad56dafb11e99db0f9"),
    "canon/REGISTRY.tsv": (265407, "abf9a17dd8868959baa484972d80a33e32658fa57549f48b4fdf8d38102d4d1f"),
    "canon/STATUS_COUNTS.tsv": (243, "96f82b9757e9036ab30688995107a5f8f8f5956ba9cbf326b88872aae4055c77"),
    "reproduce/status-separation/EXPECTED.txt": (7918, "08a9df602d0c6f8a5e26ebf03c83470b6f1268c4100f958d2b82c7b8e06b37a1"),
    "reproduce/status-separation/README.md": (14916, "3252b1a6351b2afcedda79a8b2c6a63acc84ff0481b9d53235c9aa807cdafac3"),
    "reproduce/status-separation/verify.py": (187288, "181a1252eea8672fd25f799ffbb909d8ade2b554c77dca12f9b1b058265a5127"),
}


@dataclass(frozen=True)
class ExportFile:
    relative_path: str
    data: bytes

    @property
    def byte_count(self) -> int:
        return len(self.data)

    @property
    def sha256(self) -> str:
        return sha256_bytes(self.data)


@dataclass(frozen=True)
class ExportRun:
    files: tuple[ExportFile, ...]
    manifest: bytes
    archive: bytes
    canon_sha256: str
    canon_bytes: int

    @property
    def manifest_sha256(self) -> str:
        return sha256_bytes(self.manifest)

    @property
    def archive_sha256(self) -> str:
        return sha256_bytes(self.archive)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def changelog_section(text: str, version: int) -> str:
    heading = f"## Public Canon v{version}\n"
    if text.count(heading) != 1:
        raise AssertionError(f"CHANGELOG Public Canon v{version} section count={text.count(heading)}")
    start = text.index(heading)
    following = re.search(r"(?m)^## Public Canon v[1-9][0-9]*\n", text[start + len(heading):])
    end = len(text) if following is None else start + len(heading) + following.start()
    return text[start:end]


def marked_snapshot_payload(section: str, version: int) -> str:
    begin_line = CURRENT_COUNTS_BEGIN + "\n"
    end_line = CURRENT_COUNTS_END + "\n"
    if section.count(CURRENT_COUNTS_BEGIN) != 1 or section.count(CURRENT_COUNTS_END) != 1:
        raise AssertionError(f"Public Canon v{version} historical marker count mismatch")
    if section.splitlines(keepends=True).count(begin_line) != 1:
        raise AssertionError(f"Public Canon v{version} BEGIN marker is not one exact line")
    if section.splitlines(keepends=True).count(end_line) != 1:
        raise AssertionError(f"Public Canon v{version} END marker is not one exact line")
    before, separator, remainder = section.partition(begin_line)
    if not separator:
        raise AssertionError(f"Public Canon v{version} BEGIN marker missing")
    payload, separator, after = remainder.partition(end_line)
    if not separator or CURRENT_COUNTS_BEGIN in before + after or CURRENT_COUNTS_END in before + after:
        raise AssertionError(f"Public Canon v{version} historical count block is malformed")
    return payload


def strip_exact_historical_marker_lines(text: str) -> str:
    begin_line = CURRENT_COUNTS_BEGIN + "\n"
    end_line = CURRENT_COUNTS_END + "\n"
    lines = text.splitlines(keepends=True)
    if text.count(CURRENT_COUNTS_BEGIN) != 2 or lines.count(begin_line) != 2:
        raise AssertionError("historical CHANGELOG BEGIN marker count is not exactly two lines")
    if text.count(CURRENT_COUNTS_END) != 2 or lines.count(end_line) != 2:
        raise AssertionError("historical CHANGELOG END marker count is not exactly two lines")
    stripped = "".join(line for line in lines if line not in (begin_line, end_line))
    removed = len(text.encode("utf-8")) - len(stripped.encode("utf-8"))
    if removed != EXPECTED_HISTORICAL_MARKER_BYTES_REMOVED:
        raise AssertionError(f"historical CHANGELOG marker bytes removed={removed}")
    return stripped


def replace_status_field(text: str, field: str, value: str) -> str:
    pattern = rf"(?m)^({re.escape(field)}:\s*).*$"
    replaced, count = re.subn(pattern, rf"\g<1>{value}", text)
    if count != 1:
        raise AssertionError(f"STATUS field {field} replacement count={count}")
    return replaced


def collect_export_files(work: Path, relative_paths: tuple[str, ...]) -> tuple[ExportFile, ...]:
    if relative_paths != EXPORT_FILES:
        raise AssertionError("candidate export inventory differs from the frozen 12-file inventory")
    if len(relative_paths) != EXPORT_FILE_COUNT:
        raise AssertionError(f"candidate export file count={len(relative_paths)}")
    if len(set(relative_paths)) != len(relative_paths):
        raise AssertionError("candidate export inventory contains duplicate paths")
    if relative_paths != tuple(sorted(relative_paths)):
        raise AssertionError("candidate export inventory is not sorted")

    files = []
    for relative in relative_paths:
        posix = PurePosixPath(relative)
        if (
            not relative
            or "\\" in relative
            or "\t" in relative
            or "\r" in relative
            or "\n" in relative
            or posix.is_absolute()
            or ".." in posix.parts
            or posix.as_posix() != relative
        ):
            raise AssertionError(f"unsafe export path: {relative!r}")
        path = work / relative
        if not path.is_file():
            raise AssertionError(f"missing export file: {relative}")
        files.append(ExportFile(relative, path.read_bytes()))
    return tuple(files)


def canonical_manifest(files: tuple[ExportFile, ...]) -> bytes:
    lines = [EXPORT_MANIFEST_HEADER]
    lines.extend(
        f"{item.relative_path}\t{item.byte_count}\t{item.sha256}\n"
        for item in files
    )
    manifest = "".join(lines).encode("utf-8")
    if b"\r" in manifest or not manifest.endswith(b"\n"):
        raise AssertionError("export manifest is not canonical UTF-8/LF")
    return manifest


def deterministic_zip(files: tuple[ExportFile, ...]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(
        buffer,
        "w",
        compression=ZIP_COMPRESSION,
        compresslevel=ZIP_COMPRESSION_LEVEL,
        allowZip64=False,
    ) as archive:
        archive.comment = b""
        for item in files:
            info = zipfile.ZipInfo(item.relative_path, date_time=ZIP_TIMESTAMP)
            info.create_system = ZIP_CREATE_SYSTEM
            info.create_version = ZIP_CREATE_VERSION
            info.extract_version = ZIP_EXTRACT_VERSION
            info.reserved = 0
            info.flag_bits = 0
            info.volume = 0
            info.internal_attr = 0
            info.external_attr = ZIP_EXTERNAL_ATTR
            info.compress_type = ZIP_COMPRESSION
            info.extra = b""
            info.comment = b""
            archive.writestr(
                info,
                item.data,
                compress_type=ZIP_COMPRESSION,
                compresslevel=ZIP_COMPRESSION_LEVEL,
            )
    return buffer.getvalue()


def validate_zip(payload: bytes, files: tuple[ExportFile, ...]) -> None:
    expected_paths = [item.relative_path for item in files]
    with zipfile.ZipFile(io.BytesIO(payload), "r") as archive:
        infos = archive.infolist()
        if archive.comment != b"":
            raise AssertionError("ZIP archive comment is not empty")
        if [info.filename for info in infos] != expected_paths:
            raise AssertionError("ZIP member ordering differs from the canonical inventory")
        if archive.testzip() is not None:
            raise AssertionError("ZIP CRC validation failed")
        for info, item in zip(infos, files, strict=True):
            expected = {
                "date_time": ZIP_TIMESTAMP,
                "create_system": ZIP_CREATE_SYSTEM,
                "create_version": ZIP_CREATE_VERSION,
                "extract_version": ZIP_EXTRACT_VERSION,
                "reserved": 0,
                "flag_bits": 0,
                "volume": 0,
                "internal_attr": 0,
                "external_attr": ZIP_EXTERNAL_ATTR,
                "compress_type": ZIP_COMPRESSION,
                "extra": b"",
                "comment": b"",
                "file_size": item.byte_count,
            }
            for field, value in expected.items():
                if getattr(info, field) != value:
                    raise AssertionError(
                        f"ZIP {item.relative_path} {field}={getattr(info, field)!r}, "
                        f"expected {value!r}"
                    )
            if archive.read(info) != item.data:
                raise AssertionError(f"ZIP member bytes differ: {item.relative_path}")


def rewrite_tsv(path: Path, key: str, mutate) -> None:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = tuple(reader.fieldnames or ())
        rows = list(reader)
    matches = [row for row in rows if row[key] == CLAIM]
    if len(matches) != 1:
        raise AssertionError(f"{path.name}: target rows={len(matches)}")
    mutate(matches[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def patch_status_separation(work: Path) -> None:
    path = work / "reproduce/status-separation/verify.py"
    text = path.read_text(encoding="utf-8")
    replacements = {
        '"registry and companion-ledger counts match Public Canon v61"':
            '"registry and companion-ledger counts match Public Canon v62"',
        "and len(history) == 845": "and len(history) == 846",
        f'"T", "THEOREM", "{OLD_PATH}",\n            "{OLD_HASH}",':
            f'"T", "THEOREM", "{NEW_PATH}",\n            "{NEW_HASH}",',
        'and row["evidence_location"] == v61_rows[claim][2]\n'
        '            and row["evidence_sha256"] == v61_rows[claim][3]':
            'and row["evidence_location"] == (\n'
            f'                "{OLD_PATH}" if claim == "{CLAIM}"\n'
            '                else v61_rows[claim][2]\n'
            '            )\n'
            '            and row["evidence_sha256"] == (\n'
            f'                "{OLD_HASH}" if claim == "{CLAIM}"\n'
            '                else v61_rows[claim][3]\n'
            '            )',
    }
    for old, new in replacements.items():
        if text.count(old) != 1:
            raise AssertionError(f"status-separation replacement count {text.count(old)} for {old[:60]}")
        text = text.replace(old, new, 1)

    anchor = "    fw_requires = {}\n"
    if text.count(anchor) != 1:
        raise AssertionError("status-separation V62 insertion anchor mismatch")
    block = f'''    v62_events = [
        row for row in history
        if row["claim_id"] == "{CLAIM}"
        and row["event_id"] == "CANON62-EVIDENCE-{CLAIM}"
    ]
    checks.append((
        "V62-MAINTENANCE",
        "v62 changes only the odd-motor evidence pointer and one lifecycle event while status, scope, dependencies, gates and science counts stay fixed",
        len(v62_events) == 1
        and has_status(index, "{CLAIM}", "T")
        and scope_sha256(index, "{CLAIM}") == "{SCOPE_HASH}"
        and index["{CLAIM}"]["evidence"] == "{NEW_PATH}"
        and evidence["{CLAIM}"]["evidence_id"] == "EV-{CLAIM}"
        and evidence["{CLAIM}"]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence["{CLAIM}"]["location"] == "{NEW_PATH}"
        and evidence["{CLAIM}"]["sha256"] == "{NEW_HASH}"
        and evidence["{CLAIM}"]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence["{CLAIM}"]["architecture_requirement"] == "two-architecture"
        and {{
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == "{CLAIM}"
        }} == {{
            ("AFFINE-READING-DEGREE-CENSUS", "REQUIRES"),
            ("AFFINE-QUADRATIC-FORM-UNIQUENESS", "REQUIRES"),
        }}
        and normative["{CLAIM}"]["status"] == "T"
        and normative["{CLAIM}"]["layer"] == "L1"
        and normative["{CLAIM}"]["gate_ids"] == ""
        and all(row["owner_item_id"] != "{CLAIM}" for row in gates.values())
        and v62_events[0]["event_sequence"] == "2"
        and v62_events[0]["event_date"] == "2026-08-24"
        and v62_events[0]["release"] == "canon-v62-candidate"
        and v62_events[0]["event_type"] == "EVIDENCE_CHANGE"
        and v62_events[0]["previous_status"] == "T"
        and v62_events[0]["new_status"] == "T"
        and v62_events[0]["scope_sha256"] == "{SCOPE_HASH}"
        and v62_events[0]["evidence_id"] == "EV-{CLAIM}"
        and v62_events[0]["evidence_location"] == "{NEW_PATH}"
        and v62_events[0]["evidence_sha256"] == "{NEW_HASH}"
    ))

'''
    text = text.replace(anchor, block + anchor, 1)
    path.write_text(text, encoding="utf-8", newline="\n")

    readme_path = work / "reproduce/status-separation/README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "RESULT 54/54 ALL PASS" not in readme:
        raise AssertionError("status-separation README result anchor missing")
    readme = readme.replace("RESULT 54/54 ALL PASS", "RESULT 55/55 ALL PASS", 1)
    anchor = "The v61 count check reads the folded tree"
    if readme.count(anchor) != 1:
        raise AssertionError("status-separation README v61 anchor mismatch")
    paragraph = (
        "The v62 count check reads the maintenance tree (324 claims, 23 reproductions, "
        "11 gates). The V62-MAINTENANCE check requires the odd-motor theorem to retain "
        "its T status, exact scope, dependencies, layer and no-gate boundary while its "
        "single current evidence pointer moves to the completed two-architecture "
        "COVERAGE-2 bundle and HISTORY records exactly one sequence-2 EVIDENCE_CHANGE. "
        "No scientific count or status moves.\n\n"
    )
    readme = readme.replace(anchor, paragraph + anchor, 1)
    readme_path.write_text(readme, encoding="utf-8", newline="\n")

    result = subprocess.run(
        [sys.executable, "reproduce/status-separation/verify.py"],
        cwd=work, capture_output=True, check=False,
    )
    if result.returncode != 0 or result.stderr:
        raise AssertionError(
            "patched status-separation failed: "
            + result.stdout.decode("utf-8", "replace")
            + result.stderr.decode("utf-8", "replace")
        )
    (work / "reproduce/status-separation/EXPECTED.txt").write_bytes(result.stdout)


def build_candidate(root: Path, work: Path) -> tuple[tuple[str, ...], str, int]:
    canon_dir = work / "canon"
    frontier_before = (canon_dir / "FRONTIER.md").read_bytes()
    status_counts_before = (canon_dir / "STATUS_COUNTS.tsv").read_bytes()
    deps_before = (canon_dir / "DEPENDENCIES.tsv").read_bytes()
    normative_before = (canon_dir / "NORMATIVE.tsv").read_bytes()
    gates_before = (canon_dir / "GATES.tsv").read_bytes()
    programs_before = (canon_dir / "FRONTIER_PROGRAMS.tsv").read_bytes()

    canon_path = canon_dir / "CANON.md"
    canon = canon_path.read_text(encoding="utf-8")
    head, sep, tail = canon.partition("\n---\n")
    if not sep or "# TWIST-J Public Canon v61" not in head:
        raise AssertionError("CANON current release title missing")
    head = head.replace("Public Canon v61", "Public Canon v62")
    old_sentence = f"Evidence is `{OLD_PATH}`."
    new_sentence = f"Evidence is `{NEW_PATH}`."
    if tail.count(old_sentence) != 1:
        raise AssertionError(f"CANON evidence sentence count={tail.count(old_sentence)}")
    tail = tail.replace(old_sentence, new_sentence, 1)
    canon_path.write_text(head + sep + tail, encoding="utf-8", newline="\n")

    def mutate_registry(row):
        if row["status"] != "T" or sha256_bytes(row["scope"].encode()) != SCOPE_HASH:
            raise AssertionError("REGISTRY target status/scope drift")
        if row["evidence"] != OLD_PATH:
            raise AssertionError("REGISTRY old evidence mismatch")
        row["evidence"] = NEW_PATH
    rewrite_tsv(canon_dir / "REGISTRY.tsv", "claim_id", mutate_registry)

    def mutate_evidence(row):
        if row["evidence_id"] != f"EV-{CLAIM}" or row["location"] != OLD_PATH or row["sha256"] != OLD_HASH:
            raise AssertionError("EVIDENCE target old row mismatch")
        if row["architecture_requirement"] != "two-architecture":
            raise AssertionError("EVIDENCE architecture drift")
        row["location"] = NEW_PATH
        row["sha256"] = NEW_HASH
    rewrite_tsv(canon_dir / "EVIDENCE.tsv", "claim_id", mutate_evidence)

    history_path = canon_dir / "HISTORY.tsv"
    history = history_path.read_text(encoding="utf-8")
    if f"CANON62-EVIDENCE-{CLAIM}\t" in history:
        raise AssertionError("v62 history event already exists")
    event = "\t".join((
        f"CANON62-EVIDENCE-{CLAIM}", "2", "2026-08-24", "canon-v62-candidate",
        CLAIM, "EVIDENCE_CHANGE", "T", "T", SCOPE_HASH, f"EV-{CLAIM}",
        NEW_PATH, NEW_HASH,
        "Public Canon v62 re-pins the unchanged T theorem to the complete RESULT-EXPOSED two-architecture coverage bundle; status, scope, falsifier, dependencies, gate surface and scientific content are unchanged, and the stopped predecessor supplies no evidence.",
    ))
    if history and not history.endswith("\n"):
        history += "\n"
    history_path.write_text(history + event + "\n", encoding="utf-8", newline="\n")

    changelog_path = canon_dir / "CHANGELOG.md"
    changelog = changelog_path.read_text(encoding="utf-8")
    header, separator, historical = changelog.partition("\n\n")
    if header != CHANGELOG_HEADER or separator != "\n\n":
        raise AssertionError("CHANGELOG header mismatch")
    historical_snapshot_payloads_before = {
        version: marked_snapshot_payload(changelog_section(historical, version), version)
        for version in (61, 60)
    }
    historical_without_markers = strip_exact_historical_marker_lines(historical)
    historical_sections_without_markers_before = {
        version: changelog_section(historical_without_markers, version)
        for version in (61, 60)
    }
    historical = historical_without_markers
    v62 = f'''## Public Canon v62

<!-- BEGIN GENERATED CURRENT COUNTS -->
PLACEHOLDER
<!-- END GENERATED CURRENT COUNTS -->

Public Canon v62 is an integrity and evidence-maintenance release. It adds no
scientific claim, status move, scope move, dependency move, gate verdict,
physical dictionary or layer lift. Scientific registry counts are unchanged
from v61.

The released tree incorporates the already merged gate-contract maintenance
from PR #541. Every public gate row remains governed by the closed `gate_kind`
contract, including the explicit same-layer `OPEN_DECISION` case; no gate row
or verdict changes in this fold.

`J-ODD-MOTOR-MEDIATED-BRIDGE [T]` keeps its v61 status, scope, falsifier,
dependencies and nonselection boundary. Its single current evidence pointer is
re-pinned from `{OLD_PATH}` to
`{NEW_PATH}`, the complete RESULT-EXPOSED
two-architecture evidence-maintenance bundle. That bundle combines the frozen
G2-G8 implementation with the later native-sector and explicit-Schur
hardening, while explicitly not consuming the 624-channel-box H3 value.
The stopped COVERAGE-1 predecessor supplies no evidence.

The v62 ledger change is:

```text
claims: 324, unchanged,
T: 202, D: 43, C: 33, H: 3, O: 27, F: 16, unchanged,
live H/O: 30, unchanged,
normative items: 370, unchanged,
dependencies: 581, unchanged,
evidence rows: 324, unchanged,
gates: 11, unchanged,
history rows: 845 + 1 evidence-change event = 846,
two-architecture evidence: 240, unchanged,
reproduction witnesses: 23, unchanged.
```

'''
    changelog_path.write_text(
        header + separator + v62 + historical, encoding="utf-8", newline="\n"
    )

    patch_status_separation(work)

    subprocess.run(
        [sys.executable, "tools/generate_canon_views.py", "--root", str(work), "--apply"],
        cwd=work, check=True, text=True,
    )
    completed_changelog = changelog_path.read_text(encoding="utf-8")
    begin_count = completed_changelog.count(CURRENT_COUNTS_BEGIN)
    end_count = completed_changelog.count(CURRENT_COUNTS_END)
    if begin_count != 1 or end_count != 1:
        raise AssertionError(
            f"completed CHANGELOG marker counts BEGIN={begin_count} END={end_count}"
        )
    v62_position = completed_changelog.index("## Public Canon v62")
    v61_position = completed_changelog.index("## Public Canon v61")
    begin_position = completed_changelog.index(CURRENT_COUNTS_BEGIN)
    end_position = completed_changelog.index(CURRENT_COUNTS_END)
    if not v62_position < begin_position < end_position < v61_position:
        raise AssertionError("unique generated current-count block is not inside Public Canon v62")
    for version in (61, 60):
        completed_section = changelog_section(completed_changelog, version)
        if completed_section != historical_sections_without_markers_before[version]:
            raise AssertionError(f"Public Canon v{version} historical section text changed")
        payload = historical_snapshot_payloads_before[version]
        if not payload or completed_section.count(payload) != 1:
            raise AssertionError(f"Public Canon v{version} historical snapshot payload changed")
    changelog_bytes = changelog_path.stat().st_size
    if changelog_bytes != EXPECTED_CHANGELOG_BYTES:
        raise AssertionError(
            f"corrected candidate CHANGELOG bytes={changelog_bytes}, "
            f"expected {EXPECTED_CHANGELOG_BYTES}"
        )
    if (canon_dir / "FRONTIER.md").read_bytes() != frontier_before:
        raise AssertionError("FRONTIER changed although no live row moved")
    if (canon_dir / "STATUS_COUNTS.tsv").read_bytes() != status_counts_before:
        raise AssertionError("STATUS_COUNTS changed although science counts are frozen")
    for name, before in (
        ("DEPENDENCIES.tsv", deps_before), ("NORMATIVE.tsv", normative_before),
        ("GATES.tsv", gates_before), ("FRONTIER_PROGRAMS.tsv", programs_before),
    ):
        if (canon_dir / name).read_bytes() != before:
            raise AssertionError(f"{name} changed in maintenance fold")

    hashed = ("CANON.md", "CORE.md", "FRONTIER.md", "REGISTRY.tsv", "CHANGELOG.md")
    sums = []
    for name in hashed:
        sums.append(f"{sha256_bytes((canon_dir / name).read_bytes())}  canon/{name}\n")
    (canon_dir / "SHA256SUMS").write_text("".join(sums), encoding="utf-8", newline="\n")

    subprocess.run([sys.executable, "tools/check_policy.py"], cwd=work, check=True, text=True)
    subprocess.run([sys.executable, "tools/check_canon.py"], cwd=work, check=True, text=True)
    subprocess.run([sys.executable, "tools/check_ledger.py"], cwd=work, check=True, text=True)
    subprocess.run([sys.executable, "tools/check_gate_contract.py"], cwd=work, check=True, text=True)
    subprocess.run(
        [sys.executable, "tools/generate_canon_views.py", "--root", str(work),
         "--check-dir", str(canon_dir)],
        cwd=work, check=True, text=True,
    )
    result = subprocess.run(
        [sys.executable, "reproduce/status-separation/verify.py"],
        cwd=work, capture_output=True, check=False,
    )
    if result.returncode != 0 or result.stderr or result.stdout != (work / "reproduce/status-separation/EXPECTED.txt").read_bytes():
        raise AssertionError("status-separation exact replay mismatch")

    canon_hash = sha256_bytes(canon_path.read_bytes())
    canon_bytes = canon_path.stat().st_size
    return EXPORT_FILES, canon_hash, canon_bytes


def build_export(root: Path, temporary_root: Path) -> ExportRun:
    work = temporary_root / "repo"
    shutil.copytree(
        root, work,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
    )
    export_paths, canon_hash, canon_bytes = build_candidate(root, work)
    files = collect_export_files(work, export_paths)
    manifest = canonical_manifest(files)
    archive = deterministic_zip(files)
    validate_zip(archive, files)
    return ExportRun(files, manifest, archive, canon_hash, canon_bytes)


def checked_process(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise AssertionError(
            f"command failed ({' '.join(args)}):\n{result.stdout}{result.stderr}"
        )
    return result


def validate_activation_overlay(root: Path, files: tuple[ExportFile, ...]) -> None:
    by_path = {item.relative_path: item for item in files}
    if tuple(by_path) != EXPORT_FILES:
        raise AssertionError("activation overlay export inventory mismatch")

    with tempfile.TemporaryDirectory(prefix="twistj-v62-activation-overlay-") as td:
        overlay = Path(td) / "repo"
        clone = subprocess.run(
            ["git", "clone", "--quiet", "--no-local", str(root), str(overlay)],
            capture_output=True, text=True, check=False,
        )
        if clone.returncode != 0:
            raise AssertionError(f"activation overlay clone failed:\n{clone.stdout}{clone.stderr}")
        checked_process(["git", "switch", "--detach", FROZEN_BASE], overlay)
        if checked_process(["git", "rev-parse", "HEAD"], overlay).stdout.strip() != FROZEN_BASE:
            raise AssertionError("activation overlay did not start at the frozen base")
        if checked_process(["git", "status", "--porcelain"], overlay).stdout:
            raise AssertionError("activation overlay base is not clean")

        for relative in EXPORT_FILES:
            path = overlay / relative
            path.write_bytes(by_path[relative].data)
        changed = tuple(
            checked_process(["git", "diff", "--name-only"], overlay).stdout.splitlines()
        )
        if changed != EXPECTED_CONTENT_CHANGED_FILES:
            raise AssertionError(f"activation overlay content paths={changed!r}")
        checked_process(["git", "add", "--", *EXPORT_FILES], overlay)
        checked_process([
            "git", "-c", "user.name=A. M. Thorn", "-c", "user.email=thorn@twistj.com",
            "commit", "--quiet", "-m", "Ephemeral v62 content for activation certification",
        ], overlay)
        content_commit = checked_process(["git", "rev-parse", "HEAD"], overlay).stdout.strip()
        if checked_process(["git", "rev-parse", "HEAD^"], overlay).stdout.strip() != FROZEN_BASE:
            raise AssertionError("ephemeral content commit parent differs from frozen base")

        canon_bytes = (overlay / "canon/CANON.md").read_bytes()
        status_path = overlay / "STATUS.md"
        status = status_path.read_text(encoding="utf-8")
        if status.count("Public Canon v61") != 2 or status.count("canon-v61") != 2:
            raise AssertionError("v61 STATUS release identity occurrence count changed")
        status = status.replace("Public Canon v61", "Public Canon v62")
        status = status.replace("canon-v61", "canon-v62")
        status = replace_status_field(status, "STATE", "ACTIVE")
        status = replace_status_field(status, "CANON", "Public Canon v62")
        status = replace_status_field(status, "AUTHORITY", "mathorn1973/twist-j main")
        status = replace_status_field(status, "TAG", "canon-v62")
        status = replace_status_field(status, "CONTENT_COMMIT", content_commit)
        status = replace_status_field(status, "CANON_SHA256", sha256_bytes(canon_bytes))
        status = replace_status_field(status, "CANON_BYTES", str(len(canon_bytes)))
        if "CUTOVER:        2026-08-21" not in status:
            raise AssertionError("activation overlay changed the established CUTOVER")
        status_path.write_text(status, encoding="utf-8", newline="\n")

        readme_path = overlay / "README.md"
        readme = readme_path.read_text(encoding="utf-8")
        if readme.count("Public Canon v61") != 3 or readme.count("canon-v61") != 2:
            raise AssertionError("v61 README release identity occurrence count changed")
        readme = readme.replace("Public Canon v61", "Public Canon v62")
        readme = readme.replace("canon-v61", "canon-v62")
        readme_path.write_text(readme, encoding="utf-8", newline="\n")

        citation_path = overlay / "CITATION.cff"
        citation = citation_path.read_text(encoding="utf-8")
        replacements = (
            (
                'message: "If you use TWIST-J Public Canon v61, cite it as below."',
                'message: "If you use TWIST-J Public Canon v62, cite it as below."',
            ),
            ('version: "61"', 'version: "62"'),
            ('date-released: 2026-08-23', 'date-released: 2026-08-24'),
        )
        for old, new in replacements:
            if citation.count(old) != 1:
                raise AssertionError(f"CITATION release identity count={citation.count(old)} for {old}")
            citation = citation.replace(old, new, 1)
        citation_path.write_text(citation, encoding="utf-8", newline="\n")

        release_paths = tuple(
            checked_process(["git", "diff", "--name-only"], overlay).stdout.splitlines()
        )
        if release_paths != ("CITATION.cff", "README.md", "STATUS.md"):
            raise AssertionError(f"activation release-form paths={release_paths!r}")
        checked_process(
            ["git", "add", "--", "STATUS.md", "README.md", "CITATION.cff"], overlay
        )
        checked_process([
            "git", "-c", "user.name=A. M. Thorn", "-c", "user.email=thorn@twistj.com",
            "commit", "--quiet", "-m", "Ephemeral v62 release form for activation certification",
        ], overlay)
        if checked_process(["git", "status", "--porcelain"], overlay).stdout:
            raise AssertionError("activation release-form overlay is not clean")
        committed_release_paths = tuple(
            checked_process(
                ["git", "diff", "--name-only", f"{content_commit}..HEAD"], overlay
            ).stdout.splitlines()
        )
        if committed_release_paths != ("CITATION.cff", "README.md", "STATUS.md"):
            raise AssertionError(
                f"committed activation release-form paths={committed_release_paths!r}"
            )

        activation = subprocess.run(
            [
                sys.executable, "tools/check_activation.py", "--full",
                "--content-commit", content_commit,
            ],
            cwd=overlay, capture_output=True, text=True, check=False,
        )
        if activation.returncode != 0:
            raise AssertionError(
                "full activation overlay failed:\n"
                + activation.stdout + activation.stderr
            )
        if "ACTIVATION PASS mode=active full=True" not in activation.stdout:
            raise AssertionError("full activation overlay lacked its exact PASS line")
        print(
            "V62_ACTIVATION_OVERLAY_PASS full=YES "
            "unique_changelog_marker_gate=YES"
        )


class V62BuildExportTest(unittest.TestCase):
    def test_build_validate_and_export(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with (
            tempfile.TemporaryDirectory(prefix="twistj-v62-export-run-1-") as td1,
            tempfile.TemporaryDirectory(prefix="twistj-v62-export-run-2-") as td2,
        ):
            self.assertNotEqual(Path(td1).resolve(), Path(td2).resolve())
            run1 = build_export(root, Path(td1))
            run2 = build_export(root, Path(td2))

            paths1 = tuple(item.relative_path for item in run1.files)
            paths2 = tuple(item.relative_path for item in run2.files)
            sizes1 = tuple(item.byte_count for item in run1.files)
            sizes2 = tuple(item.byte_count for item in run2.files)
            hashes1 = tuple(item.sha256 for item in run1.files)
            hashes2 = tuple(item.sha256 for item in run2.files)
            bytes1 = tuple(item.data for item in run1.files)
            bytes2 = tuple(item.data for item in run2.files)

            self.assertEqual(paths1, EXPORT_FILES)
            self.assertEqual(paths2, EXPORT_FILES)
            self.assertEqual(len(paths1), EXPORT_FILE_COUNT)
            self.assertEqual(paths1, paths2)
            self.assertEqual(sizes1, sizes2)
            self.assertEqual(hashes1, hashes2)
            self.assertEqual(bytes1, bytes2)
            self.assertEqual(run1.manifest, run2.manifest)
            self.assertEqual(run1.manifest_sha256, run2.manifest_sha256)
            self.assertEqual(run1.manifest_sha256, EXPECTED_EXPORT_MANIFEST_SHA256)
            self.assertEqual(run1.archive, run2.archive)
            self.assertEqual(run1.archive_sha256, run2.archive_sha256)
            self.assertEqual(run1.archive_sha256, EXPECTED_ZIP_SHA256)
            self.assertEqual(len(run1.archive), EXPECTED_ZIP_BYTES)
            self.assertEqual(run1.canon_sha256, run2.canon_sha256)
            self.assertEqual(run1.canon_bytes, run2.canon_bytes)

            files_by_path = {item.relative_path: item for item in run1.files}
            self.assertEqual(tuple(files_by_path), EXPORT_FILES)
            for relative, expected in UNCHANGED_CERTIFIED_FILES.items():
                item = files_by_path[relative]
                self.assertEqual((item.byte_count, item.sha256), expected)
            self.assertEqual(
                (
                    files_by_path["canon/CHANGELOG.md"].byte_count,
                    files_by_path["canon/CHANGELOG.md"].sha256,
                ),
                (EXPECTED_CHANGELOG_BYTES, EXPECTED_CHANGELOG_SHA256),
            )
            self.assertEqual(
                files_by_path["canon/SHA256SUMS"].sha256,
                EXPECTED_SHA256SUMS_SHA256,
            )
            changelog = files_by_path["canon/CHANGELOG.md"].data.decode("utf-8")
            self.assertEqual(changelog.count(CURRENT_COUNTS_BEGIN), 1)
            self.assertEqual(changelog.count(CURRENT_COUNTS_END), 1)
            self.assertLess(changelog.index("## Public Canon v62"), changelog.index(CURRENT_COUNTS_BEGIN))
            self.assertLess(changelog.index(CURRENT_COUNTS_BEGIN), changelog.index(CURRENT_COUNTS_END))
            self.assertLess(changelog.index(CURRENT_COUNTS_END), changelog.index("## Public Canon v61"))

            validate_activation_overlay(root, run1.files)

            for number, run in enumerate((run1, run2), start=1):
                print(
                    f"V62_DETERMINISM_RUN run={number} "
                    f"EXPORT_FILE_COUNT={len(run.files)} "
                    f"EXPORT_MANIFEST_SHA256={run.manifest_sha256} "
                    f"ZIP_BYTES={len(run.archive)} ZIP_SHA256={run.archive_sha256}"
                )

            for item in run1.files:
                print(
                    f"V62_EXPORT_FILE\t{item.relative_path}\t"
                    f"{item.byte_count}\t{item.sha256}"
                )

            manifest_encoded = base64.b64encode(run1.manifest).decode("ascii")
            print("V62_EXPORT_MANIFEST_BEGIN")
            for offset in range(0, len(manifest_encoded), 6000):
                print(
                    f"V62_EXPORT_MANIFEST_CHUNK {offset//6000:04d} "
                    f"{manifest_encoded[offset:offset+6000]}"
                )
            print("V62_EXPORT_MANIFEST_END")

            print(
                "V62_DETERMINISM_PASS inventory_identical=YES "
                "file_byte_counts_identical=YES per_file_sha256_identical=YES "
                "manifest_identical=YES zip_identical=YES"
            )
            print(
                f"V62_BUILD_PASS canon_sha256={run1.canon_sha256} "
                f"canon_bytes={run1.canon_bytes} files={len(run1.files)} "
                f"EXPORT_FILE_COUNT={len(run1.files)} "
                f"EXPORT_MANIFEST_SHA256={run1.manifest_sha256} "
                f"zip_bytes={len(run1.archive)} zip_sha256={run1.archive_sha256} "
                f"ZIP_SHA256={run1.archive_sha256}"
            )
            encoded = base64.b64encode(run1.archive).decode("ascii")
            print("V62_EXPORT_BEGIN")
            for offset in range(0, len(encoded), 6000):
                print(f"V62_EXPORT_CHUNK {offset//6000:04d} {encoded[offset:offset+6000]}")
            print("V62_EXPORT_END")


if __name__ == "__main__":
    unittest.main()
