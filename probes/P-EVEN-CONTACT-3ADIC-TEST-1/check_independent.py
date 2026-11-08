#!/usr/bin/env python3
"""Independent exact image calculation for P-EVEN-CONTACT-3ADIC-TEST-1.

NON-CANONICAL / L1. Original work Apache-2.0, A. M. Thorn, 2026-10-18.
SPDX-License-Identifier: Apache-2.0

Source definitions: probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py
and its frozen DOMAIN.tsv, at public main commit
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d of mathorn1973/twist-j.
Only their static definitions were read while preparing this implementation.

The declared reduction is Bbar = Kbar Abar over F_3. Abar is the adjacency
matrix for squared distances 4, 10, 16 on the literal frozen domain. Kbar
multiplies the four port rows by 2 and all other rows by 1. The two source
columns are the reduction of S_source[e_1,e_2]/2, specified below.

This implementation constructs unordered edges by pairwise distances, then
propagates each source column separately through 705 applications of Bbar.
Rank uses a determinant test on the two-column image. It imports neither
the apparatus nor verify.py and has no import-time scientific computation,
command-line entry point, output, or file writes.
"""

from __future__ import annotations

import hashlib


Point = tuple[int, int, int]
Image = tuple[tuple[int, int], ...]

DOMAIN_SIZE = 705
DOMAIN_SHA256 = (
    "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0"
)
PORTS: tuple[Point, ...] = (
    (0, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
)
SOURCE_ROWS: dict[Point, tuple[int, int]] = {
    (0, 0, 0): (1, 2),
    (1, 1, 0): (2, 1),
    (1, 0, 1): (2, 2),
    (0, 1, 1): (2, 2),
    (2, 0, 0): (2, 2),
}


def _validate_domain(domain: tuple[Point, ...]) -> None:
    """Bind coordinates and their ordering to the preregistered TSV bytes."""
    if type(domain) is not tuple or len(domain) != DOMAIN_SIZE:
        raise ValueError("Independent calculation requires a 705-point tuple")
    for point in domain:
        if (
            type(point) is not tuple
            or len(point) != 3
            or any(type(value) is not int for value in point)
        ):
            raise TypeError("Domain points must be triples of exact integers")
    if len(set(domain)) != DOMAIN_SIZE or tuple(sorted(domain)) != domain:
        raise ValueError("Domain must have distinct lexicographically sorted points")
    raw = (
        "x\ty\tz\n"
        + "".join(f"{x}\t{y}\t{z}\n" for x, y, z in domain)
    ).encode("ascii")
    if len(raw) != 5029 or hashlib.sha256(raw).hexdigest() != DOMAIN_SHA256:
        raise ValueError("Independent domain identity check failed")


def compute(domain: tuple[Point, ...]) -> Image:
    """Return all rows of Bbar**705 Dbar in the supplied frozen order."""
    _validate_domain(domain)

    edges: list[tuple[int, int]] = []
    for i in range(DOMAIN_SIZE):
        xi, yi, zi = domain[i]
        for j in range(i):
            xj, yj, zj = domain[j]
            dx, dy, dz = xi - xj, yi - yj, zi - zj
            if dx * dx + dy * dy + dz * dz in (4, 10, 16):
                edges.append((i, j))

    row_factors = tuple(2 if point in PORTS else 1 for point in domain)
    source = tuple(SOURCE_ROWS.get(point, (0, 0)) for point in domain)
    columns: list[list[int]] = []
    for column in (0, 1):
        current = [row[column] for row in source]
        for _ in range(DOMAIN_SIZE):
            following = [0] * DOMAIN_SIZE
            for i, j in edges:
                following[i] += current[j]
                following[j] += current[i]
            current = [
                (factor * value) % 3
                for factor, value in zip(row_factors, following)
            ]
        columns.append(current)

    return tuple(zip(columns[0], columns[1]))


def rank(image: Image) -> int:
    """Determine column rank over F_3 by testing row determinants."""
    if type(image) is not tuple:
        raise TypeError("Image must be a tuple of pairs")
    for row in image:
        if (
            type(row) is not tuple
            or len(row) != 2
            or any(type(value) is not int or value not in (0, 1, 2) for value in row)
        ):
            raise TypeError("Image entries must be canonical F_3 integers")

    pivot = (0, 0)
    for row in image:
        if pivot == (0, 0):
            pivot = row
        elif (pivot[0] * row[1] - pivot[1] * row[0]) % 3:
            return 2
    return 0 if pivot == (0, 0) else 1
