#!/usr/bin/env python3
"""Exact prospective R3 test for the existing even-timed contact apparatus.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, 2026.
SPDX-License-Identifier: Apache-2.0

No native or physical admission is inferred. Both rank outcomes complete
normally; corrupted inputs or disagreement between implementations STOP.
This module and its companion must not run before their public formal pin.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

PROBE = "P-EVEN-CONTACT-3ADIC-TEST-1"
SOURCE_COMMIT = "dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d"
SOURCE_SHA256 = "f0edfd80157c8993322a5338e88120c552908d3830fe5f9ea7536257213c6173"
DOMAIN_SHA256 = "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0"
DOMAIN_BYTES = 5029
INDEPENDENT_SHA256 = "e03c31b5d07294c8f1e4e35f186824ea6d1d38160d8e6d62965e3a48e2458f4d"
DIMENSION = 705
EXPONENT = 705
Y_SITES = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))
PORTS = Y_SITES[:4]
SHELL_WEIGHTS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
KERNEL_DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_domain(directory: Path) -> tuple[tuple[int, int, int], ...]:
    raw = (directory / "DOMAIN.tsv").read_bytes()
    require(len(raw) == DOMAIN_BYTES, "DOMAIN byte count")
    require(hashlib.sha256(raw).hexdigest() == DOMAIN_SHA256, "DOMAIN SHA-256")
    require(raw.endswith(b"\n") and b"\r" not in raw, "DOMAIN LF encoding")
    lines = raw.decode("ascii").splitlines()
    require(lines[0] == "x\ty\tz", "DOMAIN header")
    points = []
    for line in lines[1:]:
        fields = line.split("\t")
        require(len(fields) == 3, "DOMAIN row width")
        point = tuple(int(value) for value in fields)
        require("\t".join(str(value) for value in point) == line, "DOMAIN integer syntax")
        require(sum(point) % 2 == 0, "DOMAIN parity")
        points.append(point)
    domain = tuple(points)
    require(len(domain) == DIMENSION, "DOMAIN dimension")
    require(domain == tuple(sorted(set(domain))), "DOMAIN order or duplicate")
    require(all(point in domain for point in Y_SITES), "missing source coordinate")
    return domain


def make_stencil() -> tuple[tuple[tuple[int, int, int], int], ...]:
    stencil = []
    for dx in range(-4, 5):
        for dy in range(-4, 5):
            for dz in range(-4, 5):
                norm = dx * dx + dy * dy + dz * dz
                if (dx + dy + dz) % 2 == 0 and norm in SHELL_WEIGHTS:
                    stencil.append(((dx, dy, dz), SHELL_WEIGHTS[norm]))
    require(len(stencil) == 60, "full stencil cardinality")
    counts = {norm: sum(sum(t * t for t in delta) == norm for delta, _ in stencil)
              for norm in SHELL_WEIGHTS}
    require(counts == {2: 12, 4: 6, 8: 12, 10: 24, 16: 6}, "shell cardinalities")
    return tuple(stencil)


def verify_domain_geometry(
    domain: tuple[tuple[int, int, int], ...],
    stencil: tuple[tuple[tuple[int, int, int], int], ...],
) -> None:
    offsets = ((0, 0, 0),) + tuple(delta for delta, _ in stencil)
    first = {(x + dx, y + dy, z + dz)
             for x, y, z in Y_SITES for dx, dy, dz in offsets}
    require(len(first) == 142, "first source halo")
    second = {(x + dx, y + dy, z + dz)
              for x, y, z in first for dx, dy, dz in offsets}
    require(tuple(sorted(second)) == domain, "literal finite-domain reconstruction")


def source_columns(
    domain: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[int, int], ...]:
    # D_v = S[e1,e2]/2. At each of the five Y sites S subtracts sum(eta)/5.
    inverse_two, inverse_five = pow(2, -1, 3), pow(5, -1, 3)
    columns = []
    for point in domain:
        if point in Y_SITES:
            columns.append(tuple(
                (inverse_two * (int(point == Y_SITES[j]) - inverse_five)) % 3
                for j in range(2)
            ))
        else:
            columns.append((0, 0))
    return tuple(columns)


def primary_image(
    domain: tuple[tuple[int, int, int], ...],
    stencil: tuple[tuple[tuple[int, int, int], int], ...],
    source: tuple[tuple[int, int], ...],
) -> tuple[tuple[tuple[int, int], ...], int]:
    # 81*(weight/324) = weight/4; the diagonal is 81*(10/9)=90.
    require(90 % 3 == 0, "reduced H diagonal")
    reduced = tuple((delta, (weight * pow(4, -1, 3)) % 3)
                    for delta, weight in stencil if weight % 3 != 0)
    require(len(reduced) == 36, "reduced stencil cardinality")
    require(all(value == 1 for _, value in reduced), "reduced stencil weights")
    index = {point: i for i, point in enumerate(domain)}
    neighbours = []
    factors = []
    for x, y, z in domain:
        row = []
        for (dx, dy, dz), value in reduced:
            target = index.get((x - dx, y - dy, z - dz))
            if target is not None:
                row.append(target)
        require(len(row) == len(set(row)), "duplicate finite edge")
        neighbours.append(tuple(row))
        # K = I - PP^t/2; its four port diagonals reduce to 2.
        factors.append((1 - pow(2, -1, 3)) % 3 if (x, y, z) in PORTS else 1)
    image = source
    for _ in range(EXPONENT):
        image = tuple(
            ((factor * sum(image[j][0] for j in row)) % 3,
             (factor * sum(image[j][1] for j in row)) % 3)
            for row, factor in zip(neighbours, factors)
        )
    return image, sum(len(row) for row in neighbours)


def rank_by_elimination(image: tuple[tuple[int, int], ...]) -> int:
    # Work on the two rows of the transpose; no determinant criterion is used.
    rows = [[row[column] for row in image] for column in range(2)]
    pivot_row = 0
    for column in range(len(image)):
        pivot = next((i for i in range(pivot_row, 2) if rows[i][column] % 3), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, 3)
        rows[pivot_row] = [(value * inverse) % 3 for value in rows[pivot_row]]
        for i in range(pivot_row + 1, 2):
            multiplier = rows[i][column]
            rows[i] = [(a - multiplier * b) % 3
                       for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == 2:
            break
    return pivot_row


def rank_certificate(
    image: tuple[tuple[int, int], ...],
    domain: tuple[tuple[int, int, int], ...],
    rank: int,
) -> dict[str, object]:
    if rank == 2:
        for i in range(len(image)):
            for j in range(i + 1, len(image)):
                a, b = image[i]
                c, d = image[j]
                determinant = (a * d - b * c) % 3
                if determinant:
                    return {"kind": "nonzero_minor", "indices_zero_based": [i, j],
                            "coordinates": [domain[i], domain[j]],
                            "rows": [image[i], image[j]], "determinant_mod3": determinant}
        raise ValueError("rank two without a nonzero minor")
    for beta in KERNEL_DIRECTIONS:
        if all((row[0] * beta[0] + row[1] * beta[1]) % 3 == 0 for row in image):
            return {"kind": "kernel_direction", "beta": beta}
    raise ValueError("rank below two without a kernel direction")


def load_independent(directory: Path):
    path = directory / "check_independent.py"
    raw = path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == INDEPENDENT_SHA256,
            "independent implementation SHA-256")
    spec = importlib.util.spec_from_file_location("r3_check_independent", path)
    require(spec is not None and spec.loader is not None, "independent import specification")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    directory = Path(__file__).resolve().parent
    domain = read_domain(directory)
    independent = load_independent(directory)
    stencil = make_stencil()
    verify_domain_geometry(domain, stencil)
    source = source_columns(domain)
    require(rank_by_elimination(source) == 2, "initial source rank")
    image, nonzero_entries = primary_image(domain, stencil, source)
    other_image = independent.compute(domain)
    require(image == other_image, "independent full-image disagreement")
    rank = rank_by_elimination(image)
    other_rank = independent.rank(other_image)
    require(rank == other_rank and rank in (0, 1, 2), "independent rank disagreement")
    certificate = rank_certificate(image, domain, rank)
    image_bytes = ("c0\tc1\n" + "".join(f"{a}\t{b}\n" for a, b in image)).encode("ascii")
    payload = {
        "probe": PROBE,
        "source_commit": SOURCE_COMMIT,
        "source_apparatus_sha256": SOURCE_SHA256,
        "domain_sha256": DOMAIN_SHA256,
        "independent_sha256": INDEPENDENT_SHA256,
        "field": 3,
        "dimension": DIMENSION,
        "exponent": EXPONENT,
        "retained_stencil_vectors": 36,
        "operator_nonzero_entries": nonzero_entries,
        "port_indices_zero_based": [domain.index(point) for point in PORTS],
        "initial_source_rank": 2,
        "independent_full_image_equal": True,
        "image_rank": rank,
        "independent_rank": other_rank,
        "image_rows": image,
        "image_tsv_sha256": hashlib.sha256(image_bytes).hexdigest(),
        "rank_certificate": certificate,
        "r3": "HOLDS" if rank == 2 else "FAILS",
        "conditional_word_obstruction": "ESTABLISHED" if rank == 2 else "NOT_ESTABLISHED",
        "native_physical_admission": "NOT_CLAIMED",
        "verdict": "R3_CONFIRMED" if rank == 2 else "R3_FALSIFIED",
    }
    sys.stdout.write(json.dumps(payload, ensure_ascii=True, sort_keys=True,
                                separators=(",", ":")) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        sys.stderr.write(f"STOP: {error}\n")
        raise SystemExit(1) from None
