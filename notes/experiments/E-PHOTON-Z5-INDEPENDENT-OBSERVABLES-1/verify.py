#!/usr/bin/env python3
"""One-shot fixture gate for the independent Z5 observable reader.

The gate consumes only frozen synthetic states.  It audits their external
custody, reconstructs their analytic link fields, checks exact Python-oracle
invariants, compiles the C++ reader, and requires canonical JSON byte identity.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import types
from typing import Callable, Iterable, Sequence


BASE = Path(__file__).resolve().parent
FIXTURE_DIR = BASE / "fixtures"
MANIFEST = BASE / "SOURCE_SHA256SUMS"
UINT64_MAX = 18446744073709551615
EXPECTED_GXX_VERSION_LINE = (
    "g++.exe (MinGW-W64 x86_64-ucrt-posix-seh, built by Brecht Sanders, r7) 15.2.0"
)
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
TRIPLES = tuple(itertools.combinations(range(4), 3))
SHA_RE = re.compile(r"[0-9a-f]{64}")
DECIMAL_RE = re.compile(r"0|[1-9][0-9]*")
PATH_COMPONENT_RE = re.compile(r"[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*")
oracle = types.ModuleType("_twistj_oracle_not_loaded")

FIXTURE_METADATA = {
    "contractible_vortex.state": (3, "fixture-correlator-block", 2, 102),
    "contractible_vortex_cc.state": (3, "contractible-vortex-cc", 3, 103),
    "flat_holonomy.state": (3, "fixture-correlator-block", 1, 101),
    "monopole_nonwrapped.state": (2, "monopole-nonwrapped", 5, 105),
    "monopole_wrapped.state": (2, "monopole-wrapped", 6, 106),
    "periodic_orientation.state": (3, "periodic-orientation", 7, 107),
    "support_winding_zero_charge.state": (
        3,
        "fixture_support_winding_zero_charge",
        0,
        0,
    ),
    "wrapped_vortex_pair.state": (3, "wrapped-vortex-pair", 4, 104),
    "zero.state": (2, "zero", 0, 100),
}
FIXTURE_NAMES = tuple(sorted(FIXTURE_METADATA, key=lambda value: value.encode("ascii")))
SOURCE_PATHS = (
    "PREREG.md",
    "README.md",
    "STATE_SCHEMA.md",
    "fixture_oracle.py",
    "independent_reader.cpp",
    "verify.py",
)
EXPECTED_MANIFEST_PATHS = tuple(
    sorted(
        (*SOURCE_PATHS, *(f"fixtures/{name}" for name in FIXTURE_NAMES)),
        key=lambda value: value.encode("ascii"),
    )
)

ZERO_HOMOLOGY = [0, 0, 0, 0, 0, 0]
EXPECTED_CORE = {
    "contractible_vortex.state": {
        "flux": [480, 3, 0, 0, 3],
        "polyakov": [[26, 1, 0, 0, 0], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0]],
        "vortex": [(186, 6, 6, ZERO_HOMOLOGY, False)],
        "current_counts": [0, 0, 324, 0, 0],
        "monopole": [],
    },
    "contractible_vortex_cc.state": {
        "flux": [480, 3, 0, 0, 3],
        "polyakov": [[26, 0, 0, 0, 1], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0]],
        "vortex": [(186, 6, 6, ZERO_HOMOLOGY, False)],
        "current_counts": [0, 0, 324, 0, 0],
        "monopole": [],
    },
    "flat_holonomy.state": {
        "flux": [486, 0, 0, 0, 0],
        "polyakov": [[0, 27, 0, 0, 0], [0, 0, 27, 0, 0], [0, 0, 0, 27, 0], [0, 0, 0, 0, 27]],
        "vortex": [],
        "current_counts": [0, 0, 324, 0, 0],
        "monopole": [],
    },
    "monopole_nonwrapped.state": {
        "flux": [85, 3, 4, 2, 2],
        "polyakov": [[7, 1, 0, 0, 0], [7, 0, 1, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0]],
        "vortex": [(7, 11, 17, ZERO_HOMOLOGY, False)],
        "current_counts": [0, 2, 60, 2, 0],
        "monopole": [(18, 4, 4, [0, 0, 0, 0], False)],
    },
    "monopole_wrapped.state": {
        "flux": [76, 3, 4, 8, 5],
        "polyakov": [[8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [6, 1, 1, 0, 0], [6, 0, 1, 1, 0]],
        "vortex": [(19, 20, 32, ZERO_HOMOLOGY, False)],
        "current_counts": [0, 4, 56, 4, 0],
        "monopole": [
            (5, 4, 4, [0, 1, 0, 0], True),
            (37, 4, 4, [0, -1, 0, 0], True),
        ],
    },
    "periodic_orientation.state": {
        "flux": [480, 3, 0, 0, 3],
        "polyakov": [[26, 1, 0, 0, 0], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0]],
        "vortex": [(169, 6, 6, ZERO_HOMOLOGY, False)],
        "current_counts": [0, 0, 324, 0, 0],
        "monopole": [],
    },
    "support_winding_zero_charge.state": {
        "flux": [450, 18, 0, 0, 18],
        "polyakov": [[27, 0, 0, 0, 0], [24, 0, 0, 3, 0], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0]],
        "vortex": [
            (18, 12, 12, ZERO_HOMOLOGY, False),
            (72, 12, 12, ZERO_HOMOLOGY, False),
            (126, 12, 12, ZERO_HOMOLOGY, False),
        ],
        "current_counts": [0, 0, 324, 0, 0],
        "monopole": [],
    },
    "wrapped_vortex_pair.state": {
        "flux": [432, 27, 0, 0, 27],
        "polyakov": [[27, 0, 0, 0, 0], [18, 0, 0, 9, 0], [27, 0, 0, 0, 0], [27, 0, 0, 0, 0]],
        "vortex": [
            (0, 9, 9, [0, 0, 0, 0, 0, 1], True),
            (54, 9, 9, [0, 0, 0, 0, 0, 1], True),
            (108, 9, 9, [0, 0, 0, 0, 0, 1], True),
            (162, 9, 9, [0, 0, 0, 0, 0, 4], True),
            (216, 9, 9, [0, 0, 0, 0, 0, 4], True),
            (270, 9, 9, [0, 0, 0, 0, 0, 4], True),
        ],
        "current_counts": [0, 0, 324, 0, 0],
        "monopole": [],
    },
    "zero.state": {
        "flux": [96, 0, 0, 0, 0],
        "polyakov": [[8, 0, 0, 0, 0]] * 4,
        "vortex": [],
        "current_counts": [0, 0, 64, 0, 0],
        "monopole": [],
    },
}

CORRELATOR_SHA256 = {
    "contractible_vortex.state": "c745659f54080831cb1287867020851f5a76067876f17fc2fa1d8d2fe4bba714",
    "contractible_vortex_cc.state": "c745659f54080831cb1287867020851f5a76067876f17fc2fa1d8d2fe4bba714",
    "flat_holonomy.state": "d9c5b503d232ebc92c5b43a530b6accd759efd2ce4bbec742f451c7d1d73b48b",
    "monopole_nonwrapped.state": "4b1759e44b8ceec09eefa50c411060e50d53eb5af23ed04a6234353b3b8bebaa",
    "monopole_wrapped.state": "bc7f143ad7a3dad47930a3cc9a891e57bf8e6c69fcc5180b6138751a408e2588",
    "periodic_orientation.state": "c745659f54080831cb1287867020851f5a76067876f17fc2fa1d8d2fe4bba714",
    "support_winding_zero_charge.state": "1efc69853d4a45a85294ddae0e2ff5204c8375b70ba06457fa2ba3ba780859fd",
    "wrapped_vortex_pair.state": "17cc97d65bb562aa44dcee2b4be150ec82ffb152cd3de9ad9178ce90d1d9ffb8",
    "zero.state": "17d48258f19d7c02c9749e51368bb8e58bbb3ddd0f037c187b5e328fb3a84fa0",
}

RECORD_SHA256 = {
    "contractible_vortex.state": "d66d88e5f3c799c03aff0e1dcd57ecc48abbb4bb6c676c4aad0d27cd0989db30",
    "contractible_vortex_cc.state": "b3b4e330aeb18ff0c1d41175e3ff1f0725fd2d1ab9f45427ee13a932c7569a8d",
    "flat_holonomy.state": "d37d64a7afcb3a2b5cf8c848dba726de8322d20daa59069671e8a9eb06666155",
    "monopole_nonwrapped.state": "2a1277b0c447b13cd4070b9aeb02413896d325ba83029e9db29620d22926603c",
    "monopole_wrapped.state": "0d28a00bf9e0c4b2133f0b10b9cb74b36c3bc419cbe7d1fbde28ffd7371194dd",
    "periodic_orientation.state": "c8a3992a20338442597eb1abb5cf5bba1ab3279fc23d9990f93a83c107e4ed61",
    "support_winding_zero_charge.state": "ee933c8de6227e8616d6dcb5cd8952af3b46c320a6de346aa2110f366db8535c",
    "wrapped_vortex_pair.state": "d82e436c734c3817875be20c951dcb06bb791fce8de7df9c66df7b9850283a39",
    "zero.state": "cefacadc4e8289294f64afa8c4c0d49c5b893ceeed1be16cd74594d1e84f03fb",
}

FINGERPRINTS = {
    "contractible_vortex.state": ("61a2e76b75626af36060a10c66d28973fb51962d9a6c5039b3c00dc754ce3b38", "cf8f5baee7ef7e8d", "544f4ae1e0060380"),
    "contractible_vortex_cc.state": ("0997b6675c57bbfcd75be398b0ffca0110258065159cda70aa030beafb65817f", "5f90a31badaa513c", "e3bea102b4ad0fb0"),
    "flat_holonomy.state": ("7e7a18038fa328d02e3cc67422c36e6714412e6b65e171c184967fbba7501feb", "bc635d8af1d3f143", "ee87cf7a97fc5cab"),
    "monopole_nonwrapped.state": ("d1166b1f54b39db37cf5749ab5aed39bdf3ab89cb134eaab88af195ad1bfb8ca", "e3c6f1b5b2f0983d", "c2a13dab49fbd43a"),
    "monopole_wrapped.state": ("7567ca69d298e977cc916a3707d2ffe30bd13b335e43d9fdd11e639f68f888c9", "8df61003498481f2", "60a00ad475bbbbce"),
    "periodic_orientation.state": ("952fe000e2c965c86f921d326fbd0a47b23c96c3e1d06e9de7733763ed7745d3", "dc5b2c1a02146365", "b018a5c4e46fbd40"),
    "support_winding_zero_charge.state": ("44f66f78f49a84b96905728996523b6f9803f6e5217f399747f36813467a7f0c", "e6a4ab1e8f165636", "c2995d8f36cf0ce5"),
    "wrapped_vortex_pair.state": ("5a26b93dfc2fb7065c0ae88897236473c20aa79bd31bb20a81849b53a6a329d8", "6b30e62a6dd076cd", "38c175717b8fbe6e"),
    "zero.state": ("f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b", "e69fafcd15fb0b03", "2b20d83c8eacc803"),
}


class GateError(RuntimeError):
    pass


def require(condition: bool, label: str) -> None:
    if not condition:
        raise GateError(label)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_owned_bytes(path: Path, label: str) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        raise GateError(label) from exc


def _path_is_canonical(value: str) -> bool:
    if not value or value.startswith("/") or "\\" in value:
        return False
    parts = value.split("/")
    return all(
        part not in ("", ".", "..") and PATH_COMPONENT_RE.fullmatch(part) is not None
        for part in parts
    )


def audit_candidate_inventory() -> None:
    expected_files = set(EXPECTED_MANIFEST_PATHS) | {"SOURCE_SHA256SUMS"}
    expected_directories = {"fixtures"}
    actual_files: set[str] = set()
    actual_directories: set[str] = set()
    pending = [(BASE, "")]
    try:
        while pending:
            directory, prefix = pending.pop()
            with os.scandir(directory) as entries:
                for entry in entries:
                    relative = f"{prefix}/{entry.name}" if prefix else entry.name
                    if entry.is_symlink():
                        raise GateError("candidate_symlink")
                    if entry.is_dir(follow_symlinks=False):
                        actual_directories.add(relative)
                        pending.append((Path(entry.path), relative))
                    elif entry.is_file(follow_symlinks=False):
                        actual_files.add(relative)
                    else:
                        raise GateError("candidate_nonregular_entry")
    except OSError as exc:
        raise GateError("candidate_inventory_unreadable") from exc
    require(actual_files == expected_files, "candidate_file_inventory")
    require(actual_directories == expected_directories, "candidate_directory_inventory")


def read_manifest() -> dict[str, tuple[int, str]]:
    raw = read_owned_bytes(MANIFEST, "manifest_unreadable")
    require(raw.endswith(b"\n") and b"\r" not in raw, "manifest_lf")
    require(all(byte in (9, 10) or 32 <= byte <= 126 for byte in raw), "manifest_ascii")
    pieces = raw.split(b"\n")
    require(pieces[-1] == b"", "manifest_final_lf")
    lines = pieces[:-1]
    require(len(lines) >= 4, "manifest_record_count")
    require(lines[0] == b"TWISTJ_Z5_SOURCE_SHA256SUMS_V1", "manifest_magic")
    require(lines[1] == b"path\tbytes\tsha256", "manifest_columns")
    require(lines[-1] == b"END", "manifest_end")
    rows: dict[str, tuple[int, str]] = {}
    ordered_paths: list[str] = []
    for raw_line in lines[2:-1]:
        fields = raw_line.split(b"\t")
        require(len(fields) == 3, "manifest_field_count")
        try:
            path_text, byte_text, digest_text = (field.decode("ascii") for field in fields)
        except UnicodeDecodeError as exc:
            raise GateError("manifest_ascii_field") from exc
        require(_path_is_canonical(path_text), "manifest_path")
        require(DECIMAL_RE.fullmatch(byte_text) is not None, "manifest_bytes_decimal")
        require(SHA_RE.fullmatch(digest_text) is not None, "manifest_sha")
        require(path_text not in rows, "manifest_duplicate")
        rows[path_text] = (int(byte_text), digest_text)
        ordered_paths.append(path_text)
    require(tuple(ordered_paths) == EXPECTED_MANIFEST_PATHS, "manifest_inventory_or_order")
    audit_candidate_inventory()
    for relative, (expected_size, expected_sha) in rows.items():
        pure = PurePosixPath(relative)
        path = BASE.joinpath(*pure.parts)
        require(path.is_file(), "manifest_missing_file")
        data = read_owned_bytes(path, "manifest_owned_file_unreadable")
        require(len(data) == expected_size, "manifest_size_mismatch")
        require(sha256(data) == expected_sha, "manifest_hash_mismatch")
    return rows


def load_verified_oracle(manifest: dict[str, tuple[int, str]]) -> None:
    global oracle
    source_path = BASE / "fixture_oracle.py"
    source_bytes = read_owned_bytes(source_path, "oracle_source_unreadable")
    expected_size, expected_sha = manifest["fixture_oracle.py"]
    require(len(source_bytes) == expected_size, "oracle_source_size")
    require(sha256(source_bytes) == expected_sha, "oracle_source_sha")
    module_name = "_twistj_manifest_verified_fixture_oracle"
    require(module_name not in sys.modules, "oracle_module_collision")
    module = types.ModuleType(module_name)
    module.__file__ = str(source_path)
    module.__package__ = ""
    sys.modules[module_name] = module
    code = compile(
        source_bytes,
        str(source_path),
        "exec",
        dont_inherit=True,
        optimize=0,
    )
    exec(code, module.__dict__)
    require(module.__name__ != "__main__", "oracle_module_name")
    for name in (
        "IntegrityError",
        "LinkState",
        "canonical_json",
        "encode_state_bytes",
        "observe",
        "parse_state_bytes",
    ):
        require(hasattr(module, name), "oracle_api")
    oracle = module


def site_index(L: int, coordinate: Sequence[int]) -> int:
    result = 0
    for value in coordinate:
        require(0 <= value < L, "coordinate_range")
        result = result * L + value
    return result


def decode_site(L: int, site: int) -> tuple[int, int, int, int]:
    coordinate = [0, 0, 0, 0]
    for mu in range(3, -1, -1):
        coordinate[mu] = site % L
        site //= L
    return tuple(coordinate)  # type: ignore[return-value]


def shifted_site(L: int, site: int, mu: int, amount: int = 1) -> int:
    coordinate = list(decode_site(L, site))
    coordinate[mu] = (coordinate[mu] + amount) % L
    return site_index(L, coordinate)


def link_index(L: int, coordinate: Sequence[int], mu: int) -> int:
    return site_index(L, coordinate) * 4 + mu


def generated_links(name: str) -> list[int]:
    L, _chain, _sample, _macrocycle = FIXTURE_METADATA[name]
    links = [0] * (4 * L**4)
    if name == "flat_holonomy.state":
        for coordinate in itertools.product(range(L), repeat=4):
            for mu in range(4):
                if coordinate[mu] == 0:
                    links[link_index(L, coordinate, mu)] = mu + 1
    elif name == "contractible_vortex.state":
        links[link_index(L, (1, 1, 1, 1), 0)] = 1
    elif name == "contractible_vortex_cc.state":
        links[link_index(L, (1, 1, 1, 1), 0)] = 4
    elif name == "wrapped_vortex_pair.state":
        for coordinate in itertools.product(range(L), repeat=4):
            if coordinate[0] == 1:
                links[link_index(L, coordinate, 1)] = 1
    elif name == "support_winding_zero_charge.state":
        for coordinate in itertools.product(range(L), repeat=4):
            if coordinate[0] == 1 and coordinate[2] == 1:
                links[link_index(L, coordinate, 1)] = 1
    elif name == "periodic_orientation.state":
        links[link_index(L, (1, 0, 1, 1), 0)] = 1
    elif name == "monopole_nonwrapped.state":
        links[12] = 1
        links[29] = 2
    elif name == "monopole_wrapped.state":
        for index, value in ((46, 1), (47, 3), (54, 2), (63, 2)):
            links[index] = value
    elif name != "zero.state":
        raise GateError("unknown_fixture")
    return links


def generated_state_bytes(name: str) -> bytes:
    L, chain, sample, macrocycle = FIXTURE_METADATA[name]
    return oracle.encode_state_bytes(L, chain, sample, macrocycle, generated_links(name))


def independent_flux(state: oracle.LinkState) -> list[int]:
    flux = [0] * (6 * state.L**4)
    for site in range(state.L**4):
        for pair_number, (a, b) in enumerate(PAIRS):
            value = (
                state.links[site * 4 + a]
                + state.links[shifted_site(state.L, site, a) * 4 + b]
                - state.links[shifted_site(state.L, site, b) * 4 + a]
                - state.links[site * 4 + b]
            ) % 5
            flux[site * 6 + pair_number] = value
    return flux


def audit_local_flux_closure(state: oracle.LinkState, flux: Sequence[int]) -> None:
    for site in range(state.L**4):
        for a, b, c in TRIPLES:
            boundary = (
                flux[shifted_site(state.L, site, a) * 6 + PAIR_INDEX[(b, c)]]
                - flux[site * 6 + PAIR_INDEX[(b, c)]]
                - flux[shifted_site(state.L, site, b) * 6 + PAIR_INDEX[(a, c)]]
                + flux[site * 6 + PAIR_INDEX[(a, c)]]
                + flux[shifted_site(state.L, site, c) * 6 + PAIR_INDEX[(a, b)]]
                - flux[site * 6 + PAIR_INDEX[(a, b)]]
            )
            require(boundary % 5 == 0, "local_flux_closure")


def expect_oracle_rejection(data: bytes, expected_sha: str | None = None) -> None:
    digest = sha256(data) if expected_sha is None else expected_sha
    try:
        oracle.parse_state_bytes(data, digest)
    except oracle.IntegrityError:
        return
    raise GateError("oracle_parser_false_accept")


def replace_once(data: bytes, old: bytes, new: bytes) -> bytes:
    require(data.count(old) == 1, "mutation_anchor")
    return data.replace(old, new, 1)


def audit_parser(valid_zero: bytes) -> list[bytes]:
    oracle.parse_state_bytes(valid_zero, sha256(valid_zero))
    max_bytes = oracle.encode_state_bytes(
        2,
        "uint64-boundary",
        UINT64_MAX,
        UINT64_MAX,
        [0] * 64,
    )
    oracle.parse_state_bytes(max_bytes, sha256(max_bytes))
    try:
        oracle.encode_state_bytes(2, "overflow", UINT64_MAX + 1, 0, [0] * 64)
    except oracle.IntegrityError:
        pass
    else:
        raise GateError("oracle_generator_overflow_accept")

    link_marker = b"LINKS="
    marker_at = valid_zero.index(link_marker) + len(link_marker)
    malformed = [
        valid_zero.replace(b"\n", b"\r\n"),
        valid_zero[:-1],
        valid_zero + b"\n",
        replace_once(valid_zero, b"\nEND\n", b"\nEXTRA\nEND\n"),
        replace_once(valid_zero, b"L=2\n", b"L=02\n"),
        replace_once(valid_zero, b"L=2\n", b"L=1\n"),
        replace_once(valid_zero, b"L=2\n", b"L=33\n"),
        replace_once(valid_zero, b"CHAIN=zero\n", b"CHAIN=-zero\n"),
        replace_once(valid_zero, b"CHAIN=zero\n", b"CHAIN=\n"),
        replace_once(valid_zero, b"SAMPLE=0\n", b"SAMPLE=00\n"),
        replace_once(valid_zero, b"SAMPLE=0\n", b"SAMPLE=18446744073709551616\n"),
        replace_once(valid_zero, b"MACROCYCLE=100\n", b"MACROCYCLE=0100\n"),
        replace_once(valid_zero, b"MACROCYCLE=100\n", b"MACROCYCLE=18446744073709551616\n"),
        valid_zero[:marker_at] + b"5" + valid_zero[marker_at + 1 :],
        valid_zero[:marker_at] + valid_zero[marker_at + 1 :],
        replace_once(valid_zero, b"CHAIN=zero", b"CHAIN=ze\x0bro"),
        replace_once(valid_zero, b"CHAIN=zero", b"CHAIN=ze\x1cro"),
        replace_once(valid_zero, b"CHAIN=zero", b"CHAIN=z\x80ro"),
        replace_once(valid_zero, b"SAMPLE=0\n", b"SAMPLES=0\n"),
    ]
    expect_oracle_rejection(valid_zero, "0" * 64)
    expect_oracle_rejection(valid_zero, sha256(valid_zero).upper())
    expect_oracle_rejection(valid_zero, "")
    for data in malformed:
        expect_oracle_rejection(data)
    return malformed


def component_tuple(component: dict[str, object]) -> tuple[object, ...]:
    return (
        component["anchor_face"],
        component["support_faces"],
        component["charged_area"],
        component["charged_homology_f5"],
        component["wraps"],
    )


def monopole_tuple(component: dict[str, object]) -> tuple[object, ...]:
    return (
        component["anchor_link"],
        component["support_links"],
        component["charged_length"],
        component["windings_z"],
        component["wraps"],
    )


def conjugate_counts(counts: Sequence[int]) -> list[int]:
    return [counts[0], counts[4], counts[3], counts[2], counts[1]]


def cyclotomic_from_histogram(counts: Sequence[int]) -> list[int]:
    require(len(counts) == 5, "cyclotomic_histogram_length")
    # Phi_5(z)=z^4+z^3+z^2+z+1, hence z^4=-(1+z+z^2+z^3).
    return [counts[index] - counts[4] for index in range(4)]


def cyclotomic_multiply(left: Sequence[int], right: Sequence[int]) -> list[int]:
    require(len(left) == 4 and len(right) == 4, "cyclotomic_degree")
    product = [0] * 7
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            product[left_degree + right_degree] += left_value * right_value
    for degree in range(6, 3, -1):
        coefficient = product[degree]
        product[degree] = 0
        for shift in range(1, 5):
            product[degree - shift] -= coefficient
    return product[:4]


def cyclotomic_add(left: Sequence[int], right: Sequence[int]) -> list[int]:
    return [a + b for a, b in zip(left, right)]


def cyclotomic_subtract(left: Sequence[int], right: Sequence[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def cyclotomic_scale(value: Sequence[int], factor: int) -> list[int]:
    return [factor * coefficient for coefficient in value]


def find_correlator_separation(
    result: dict[str, object],
    kind: str,
    rho: int,
    pair: list[int],
    separation: int,
) -> dict[str, object]:
    matches = [
        term
        for term in result["correlator"]["terms"]
        if term["kind"] == kind and term["rho"] == rho and term["pair"] == pair
    ]
    require(len(matches) == 1, "block_trap_term")
    separation_matches = [
        entry for entry in matches[0]["separations"] if entry["n"] == separation
    ]
    require(len(separation_matches) == 1, "block_trap_separation")
    return separation_matches[0]


def audit_block_centering_trap(observations: dict[str, dict[str, object]]) -> None:
    flat_state = observations["flat_holonomy.state"]["state"]
    local_state = observations["contractible_vortex.state"]["state"]
    require(
        flat_state["chain"] == local_state["chain"] == "fixture-correlator-block",
        "block_trap_chain",
    )
    require(
        [flat_state["sample"], local_state["sample"]] == [1, 2]
        and [flat_state["macrocycle"], local_state["macrocycle"]] == [101, 102],
        "block_trap_order",
    )
    flat = find_correlator_separation(
        observations["flat_holonomy.state"], "plus", 0, [0, 1], 1
    )
    local = find_correlator_separation(
        observations["contractible_vortex.state"], "plus", 0, [0, 1], 1
    )
    require(flat["count"] == local["count"] == 81, "block_trap_equal_count")
    require(
        [flat[key] for key in ("product_counts", "left_counts", "right_counts")]
        == [[81, 0, 0, 0, 0]] * 3,
        "block_trap_flat_histograms",
    )
    require(
        [local[key] for key in ("product_counts", "left_counts", "right_counts")]
        == [[77, 2, 0, 0, 2], [79, 1, 0, 0, 1], [79, 1, 0, 0, 1]],
        "block_trap_local_histograms",
    )
    aggregated = {
        key: [flat[key][phase] + local[key][phase] for phase in range(5)]
        for key in ("product_counts", "left_counts", "right_counts")
    }
    require(aggregated["product_counts"] == [158, 2, 0, 0, 2], "block_trap_product_sum")
    require(aggregated["left_counts"] == [160, 1, 0, 0, 1], "block_trap_left_sum")
    require(aggregated["right_counts"] == [160, 1, 0, 0, 1], "block_trap_right_sum")
    require(all(sum(histogram) == 162 for histogram in aggregated.values()), "block_trap_census")

    count = 81
    product_sum = cyclotomic_from_histogram(aggregated["product_counts"])
    left_sum = cyclotomic_from_histogram(aggregated["left_counts"])
    right_sum = cyclotomic_from_histogram(aggregated["right_counts"])
    block_covariance_scaled = cyclotomic_subtract(
        cyclotomic_scale(product_sum, 2 * count),
        cyclotomic_multiply(left_sum, right_sum),
    )

    per_configuration_products = [0, 0, 0, 0]
    for record in (flat, local):
        per_configuration_products = cyclotomic_add(
            per_configuration_products,
            cyclotomic_multiply(
                cyclotomic_from_histogram(record["left_counts"]),
                cyclotomic_from_histogram(record["right_counts"]),
            ),
        )
    configuration_centered_scaled = cyclotomic_subtract(
        cyclotomic_scale(product_sum, 2 * count),
        cyclotomic_scale(per_configuration_products, 2),
    )
    # Both vectors have denominator 4*81^2 in Q(zeta_5).  Their exact
    # difference is nonzero, so averaging per-configuration covariances cannot
    # substitute for integer histogram addition within the complete block.
    require(
        cyclotomic_subtract(block_covariance_scaled, configuration_centered_scaled)
        == [10, 0, 5, 5],
        "block_centering_exact_difference",
    )


def audit_correlator(name: str, state: oracle.LinkState, result: dict[str, object]) -> None:
    correlator = result["correlator"]
    require(isinstance(correlator, dict), "correlator_object")
    require(correlator["n_max"] == state.L // 2, "correlator_n_max")
    terms = correlator["terms"]
    require(isinstance(terms, list) and len(terms) == 24, "correlator_term_count")
    inventory = []
    for kind in ("plus", "minus"):
        for rho in range(4):
            for pair in PAIRS:
                if (rho in pair) == (kind == "plus"):
                    inventory.append((kind, rho, list(pair)))
    require(len(inventory) == 24, "correlator_expected_census")
    for term, expected in zip(terms, inventory):
        kind, rho, pair = expected
        require(
            term["kind"] == kind and term["rho"] == rho and term["pair"] == pair,
            "correlator_order",
        )
        separations = term["separations"]
        require(
            [entry["n"] for entry in separations] == list(range(1, state.L // 2 + 1)),
            "correlator_separations",
        )
        for entry in separations:
            require(entry["count"] == state.L**4, "correlator_count")
            for key in ("product_counts", "left_counts", "right_counts"):
                counts = entry[key]
                require(
                    isinstance(counts, list)
                    and len(counts) == 5
                    and all(isinstance(value, int) and value >= 0 for value in counts)
                    and sum(counts) == state.L**4,
                    "correlator_histogram",
                )
                if name in ("zero.state", "flat_holonomy.state"):
                    require(counts == [state.L**4, 0, 0, 0, 0], "zero_correlator_histogram")
    digest = sha256(oracle.canonical_json(correlator).encode("ascii"))
    require(digest == CORRELATOR_SHA256[name], "correlator_exact_histograms")


def audit_observations(
    name: str,
    state: oracle.LinkState,
    result: dict[str, object],
) -> None:
    core = EXPECTED_CORE[name]
    require(
        sha256(oracle.canonical_json(result).encode("ascii")) == RECORD_SHA256[name],
        "frozen_reader_json",
    )
    require(result["schema"] == "TWISTJ_Z5_INDEPENDENT_OBSERVABLES_V1", "observable_schema")
    state_record = result["state"]
    require(state_record["schema"] == "TWISTJ_Z5_LINK_STATE_V1", "state_schema")
    require(state_record["sha256"] == state.sha256, "state_sha")
    require(state_record["bytes"] == len(state.raw), "state_bytes")
    require(
        [state_record["L"], state_record["chain"], state_record["sample"], state_record["macrocycle"]]
        == [state.L, state.chain, state.sample, state.macrocycle],
        "state_metadata",
    )
    require(
        (
            state_record["links_sha256"],
            state_record["state_fingerprint"],
            state_record["cache_fingerprint"],
        )
        == FINGERPRINTS[name],
        "frozen_fingerprints",
    )
    require(result["flux"]["counts"] == core["flux"], "flux_counts")
    require(sum(result["flux"]["counts"]) == 6 * state.L**4, "flux_census")

    polyakov = result["polyakov"]
    require(polyakov["line_count"] == state.L**3, "polyakov_line_count")
    require(
        [direction["mu"] for direction in polyakov["directions"]] == [0, 1, 2, 3],
        "polyakov_direction_order",
    )
    require(
        [direction["phase_counts"] for direction in polyakov["directions"]]
        == core["polyakov"],
        "polyakov_exact_counts",
    )
    for direction in polyakov["directions"]:
        require(sum(direction["phase_counts"]) == state.L**3, "polyakov_census")

    vortex = result["vortex"]
    require(vortex["closure"] == "PASS", "vortex_closure")
    require(vortex["homology_order"] == ["01", "02", "03", "12", "13", "23"], "homology_order")
    require(vortex["global_charged_homology_f5"] == ZERO_HOMOLOGY, "global_vortex_homology")
    expected_vortex = core["vortex"]
    require(
        [component_tuple(component) for component in vortex["components"]] == expected_vortex,
        "vortex_components",
    )
    require(vortex["occupied_faces"] == sum(item[1] for item in expected_vortex), "vortex_support")
    require(vortex["charged_area"] == sum(item[2] for item in expected_vortex), "vortex_area")
    require(vortex["wraps"] == any(item[4] for item in expected_vortex), "vortex_wraps")
    require(
        vortex["support_size_tail_desc"] == sorted((item[1] for item in expected_vortex), reverse=True),
        "vortex_tail",
    )

    monopole = result["monopole"]
    require(monopole["closure"] == "PASS", "monopole_closure")
    require(monopole["current_count_order"] == [-2, -1, 0, 1, 2], "current_order")
    require(monopole["current_counts"] == core["current_counts"], "current_counts")
    require(sum(monopole["current_counts"]) == 4 * state.L**4, "current_census")
    expected_monopole = core["monopole"]
    require(
        [monopole_tuple(component) for component in monopole["components"]] == expected_monopole,
        "monopole_components",
    )
    require(monopole["occupied_links"] == sum(item[1] for item in expected_monopole), "monopole_support")
    require(monopole["charged_length"] == sum(item[2] for item in expected_monopole), "monopole_length")
    require(monopole["wraps"] == any(item[4] for item in expected_monopole), "monopole_wraps")
    global_winding = [sum(item[3][mu] for item in expected_monopole) for mu in range(4)]
    require(monopole["global_windings_z"] == global_winding, "global_monopole_winding")
    require(monopole["global_windings_z"] == [0, 0, 0, 0], "exact_state_global_winding")
    support_tail = sorted((item[1] for item in expected_monopole), reverse=True)
    charged_tail = sorted((item[2] for item in expected_monopole), reverse=True)
    require(monopole["support_size_tail_desc"] == support_tail, "monopole_support_tail")
    require(monopole["charged_length_tail_desc"] == charged_tail, "monopole_charged_tail")
    require(
        monopole["largest_support_over_volume"] == [max(support_tail, default=0), state.L**4],
        "monopole_largest_ratio",
    )
    audit_correlator(name, state, result)


def audit_charge_conjugation(
    states: dict[str, oracle.LinkState],
    observations: dict[str, dict[str, object]],
) -> None:
    positive = states["contractible_vortex.state"]
    negative = states["contractible_vortex_cc.state"]
    require(
        list(negative.links) == [(-value) % 5 for value in positive.links],
        "charge_conjugate_links",
    )
    positive_flux = independent_flux(positive)
    negative_flux = independent_flux(negative)
    require(negative_flux == [(-value) % 5 for value in positive_flux], "charge_conjugate_flux")
    left_terms = observations["contractible_vortex.state"]["correlator"]["terms"]
    right_terms = observations["contractible_vortex_cc.state"]["correlator"]["terms"]
    for left, right in zip(left_terms, right_terms):
        require(
            (left["kind"], left["rho"], left["pair"])
            == (right["kind"], right["rho"], right["pair"]),
            "charge_conjugate_correlator_order",
        )
        for left_sep, right_sep in zip(left["separations"], right["separations"]):
            for key in ("product_counts", "left_counts", "right_counts"):
                require(
                    right_sep[key] == conjugate_counts(left_sep[key]),
                    "charge_conjugate_histogram",
                )


def audit_support_winding_trap(
    state: oracle.LinkState,
    result: dict[str, object],
    flux: Sequence[int],
) -> None:
    for coordinate in itertools.product(range(state.L), repeat=4):
        for mu in range(4):
            expected = 1 if mu == 1 and coordinate[0] == 1 and coordinate[2] == 1 else 0
            require(state.links[link_index(state.L, coordinate, mu)] == expected, "support_trap_link_pattern")
    occupied = [index for index, value in enumerate(flux) if value]
    require(
        {PAIRS[index % 6] for index in occupied} == {(0, 1), (1, 2)},
        "support_trap_face_orientations",
    )
    # Hodge duals of F01 and F12 both contain direction 3.  For every x1 copy,
    # the support hits every x3 slice, including the periodic 2->0 seam, while
    # the exact charged periods remain zero.  This is the frozen support-only
    # winding trap that a geometric proxy must not call charged homology.
    for x1 in range(state.L):
        seen_x3 = {
            decode_site(state.L, index // 6)[3]
            for index in occupied
            if decode_site(state.L, index // 6)[1] == x1
        }
        require(seen_x3 == set(range(state.L)), "support_trap_periodic_cycle")
    vortex = result["vortex"]
    require(len(vortex["components"]) == state.L, "support_trap_components")
    require(all(not component["wraps"] for component in vortex["components"]), "support_trap_false_wrap")
    require(
        all(component["charged_homology_f5"] == ZERO_HOMOLOGY for component in vortex["components"]),
        "support_trap_zero_charge",
    )


def audit_fixtures(
    manifest: dict[str, tuple[int, str]],
) -> tuple[dict[str, oracle.LinkState], dict[str, dict[str, object]], list[bytes]]:
    states: dict[str, oracle.LinkState] = {}
    observations: dict[str, dict[str, object]] = {}
    for name in FIXTURE_NAMES:
        path = FIXTURE_DIR / name
        raw = read_owned_bytes(path, "fixture_unreadable")
        try:
            analytic_bytes = generated_state_bytes(name)
        except oracle.IntegrityError as exc:
            raise GateError("oracle_fixture_encode") from exc
        require(raw == analytic_bytes, "fixture_analytic_bytes")
        expected_size, digest = manifest[f"fixtures/{name}"]
        require(len(raw) == expected_size and sha256(raw) == digest, "fixture_custody")
        try:
            state = oracle.parse_state_bytes(raw, digest)
            result = oracle.observe(state)
        except oracle.IntegrityError as exc:
            raise GateError("oracle_fixture_integrity") from exc
        require(tuple(generated_links(name)) == state.links, "fixture_analytic_links")
        flux = independent_flux(state)
        require(result["flux"]["counts"] == [flux.count(value) for value in range(5)], "independent_flux_counts")
        audit_local_flux_closure(state, flux)
        audit_observations(name, state, result)
        states[name] = state
        observations[name] = result

    periodic = states["periodic_orientation.state"]
    periodic_flux = independent_flux(periodic)
    positive_site = site_index(3, (1, 0, 1, 1))
    seam_site = site_index(3, (1, 2, 1, 1))
    require(periodic_flux[positive_site * 6 + PAIR_INDEX[(0, 1)]] == 1, "periodic_orientation_positive")
    require(periodic_flux[seam_site * 6 + PAIR_INDEX[(0, 1)]] == 4, "periodic_orientation_negative")
    require(sum(value != 0 for value in periodic_flux) == 6, "periodic_orientation_support")

    audit_charge_conjugation(states, observations)
    audit_block_centering_trap(observations)
    trap = states["support_winding_zero_charge.state"]
    audit_support_winding_trap(trap, observations["support_winding_zero_charge.state"], independent_flux(trap))
    try:
        malformed = audit_parser(states["zero.state"].raw)
    except oracle.IntegrityError as exc:
        raise GateError("oracle_parser_audit") from exc
    return states, observations, malformed


def require_clean_process_bytes(data: bytes, label: str) -> None:
    require(data.endswith(b"\n") and b"\r" not in data, label + "_lf")
    require(all(byte == 10 or 32 <= byte <= 126 for byte in data), label + "_ascii")


def run_process(command: Sequence[str], timeout: int = 120) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            list(command),
            cwd=BASE,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise GateError("process_failure") from exc


def audit_environment() -> str:
    require(sys.version_info[:3] == (3, 12, 10), "python_version")
    require(bool(sys.flags.dont_write_bytecode), "python_minus_B")
    require(sys.flags.optimize == 0, "python_optimize")
    require(os.name == "nt" and platform.system() == "Windows", "operating_system")
    require(platform.version() == "10.0.26200", "windows_platform_version")
    require(platform.machine() == "AMD64", "windows_machine")
    require(os.environ.get("PROCESSOR_ARCHITECTURE") == "AMD64", "windows_architecture")
    try:
        windows_version = sys.getwindowsversion()
    except AttributeError as exc:
        raise GateError("windows_version_api") from exc
    require(
        (windows_version.major, windows_version.minor, windows_version.build)
        == (10, 0, 26200),
        "windows_build",
    )
    require("CXX" not in os.environ, "CXX_must_be_unset")
    require(shutil.which("g++") is not None, "gxx_missing")
    require(shutil.which("g++.exe") is not None, "gxx_exe_missing")
    version = run_process(["g++.exe", "--version"])
    require(version.returncode == 0 and version.stderr == b"", "gxx_version_process")
    try:
        version_lines = version.stdout.decode("ascii").splitlines()
    except UnicodeDecodeError as exc:
        raise GateError("gxx_version_ascii") from exc
    require(bool(version_lines) and version_lines[0] == EXPECTED_GXX_VERSION_LINE, "gxx_version")
    return "g++.exe"


def require_cpp_rejection(process: subprocess.CompletedProcess[bytes]) -> None:
    require(process.returncode != 0, "cpp_false_accept")
    require(process.stdout == b"", "cpp_reject_stdout")
    require_clean_process_bytes(process.stderr, "cpp_reject_stderr")
    require(process.stderr.startswith(b"STOP_INTEGRITY "), "cpp_reject_terminal")


def run_cpp_rejection(executable: Path, path: Path, digest: str) -> None:
    require_cpp_rejection(
        run_process(
            [str(executable), "--state", str(path), "--expected-sha256", digest]
        )
    )


def audit_cpp(
    compiler: str,
    manifest: dict[str, tuple[int, str]],
    states: dict[str, oracle.LinkState],
    observations: dict[str, dict[str, object]],
    malformed: list[bytes],
) -> None:
    with tempfile.TemporaryDirectory(prefix="twistj-photon-reader-") as temporary:
        temporary_path = Path(temporary)
        executable = temporary_path / ("independent_reader.exe" if os.name == "nt" else "independent_reader")
        compile_process = run_process(
            [
                compiler,
                "-std=c++20",
                "-O2",
                "-Wall",
                "-Wextra",
                "-pedantic",
                str(BASE / "independent_reader.cpp"),
                "-o",
                str(executable),
            ],
            timeout=180,
        )
        require(compile_process.returncode == 0, "compile_exit")
        require(compile_process.stdout == b"" and compile_process.stderr == b"", "compile_output")
        require(executable.is_file(), "compile_product")

        for name in FIXTURE_NAMES:
            digest = manifest[f"fixtures/{name}"][1]
            process = run_process(
                [
                    str(executable),
                    "--state",
                    str(FIXTURE_DIR / name),
                    "--expected-sha256",
                    digest,
                ]
            )
            require(process.returncode == 0, "cpp_fixture_exit")
            require(process.stderr == b"", "cpp_fixture_stderr")
            require_clean_process_bytes(process.stdout, "cpp_fixture_stdout")
            expected = oracle.canonical_json(observations[name]).encode("ascii")
            require(process.stdout == expected, "cpp_oracle_byte_identity")
            require(sha256(process.stdout) == RECORD_SHA256[name], "cpp_reader_json_sha")
            try:
                parsed = json.loads(process.stdout)
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise GateError("cpp_json_parse") from exc
            require(
                oracle.canonical_json(parsed).encode("ascii") == process.stdout,
                "cpp_json_not_canonical",
            )

        zero_path = FIXTURE_DIR / "zero.state"
        run_cpp_rejection(executable, zero_path, "0" * 64)
        zero_digest = manifest["fixtures/zero.state"][1]
        run_cpp_rejection(executable, zero_path, zero_digest.upper())
        run_cpp_rejection(executable, zero_path, "")
        require_cpp_rejection(
            run_process(
                [str(executable), "--state", str(zero_path), "--expected-sha256"]
            )
        )
        require_cpp_rejection(
            run_process([str(executable), "--state", str(zero_path)])
        )
        for index, malformed_bytes in enumerate(malformed):
            path = temporary_path / f"malformed-{index}.state"
            path.write_bytes(malformed_bytes)
            run_cpp_rejection(executable, path, sha256(malformed_bytes))
        require_cpp_rejection(run_process([str(executable)]))


def run_gate() -> None:
    compiler = audit_environment()
    manifest = read_manifest()
    load_verified_oracle(manifest)
    states, observations, malformed = audit_fixtures(manifest)
    audit_cpp(compiler, manifest, states, observations, malformed)


def main() -> int:
    try:
        run_gate()
    except GateError:
        sys.stdout.buffer.write(
            b"STOP_INTEGRITY\nEVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY\n"
        )
        return 0
    sys.stdout.buffer.write(
        b"INDEPENDENT_READER_FIXTURE_PASS\n"
        b"EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
