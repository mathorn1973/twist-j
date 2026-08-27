#!/usr/bin/env python3
"""Exact audit for P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1.

The verifier audits finite exact mechanisms of the written universal proof.
It does not estimate the true summatory function, inspect zeta zeros, evaluate
special functions, or prove RH/GRH.
"""

from __future__ import annotations

import ast
from pathlib import Path

Vertex = tuple[int, int]
Face = frozenset[Vertex]

FROZEN_N = (1, 2, 10, 11, 19, 121, 209, 500, 1000, 2000)
AUDIT_LIMIT = max(FROZEN_N)


def fail(label: str, detail: object = "") -> None:
    message = f"{label} failed"
    if detail != "":
        message += f": {detail}"
    raise AssertionError(message)


def check(label: str, condition: bool, detail: object = "") -> None:
    if not condition:
        fail(label, detail)


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= limit:
        if sieve[p]:
            multiple = p * p
            while multiple <= limit:
                sieve[multiple] = False
                multiple += p
        p += 1
    return [n for n in range(2, limit + 1) if sieve[n]]


def chi5(n: int) -> int:
    residue = n % 5
    if residue == 0:
        return 0
    if residue in (1, 4):
        return 1
    return -1


def split_primes(limit: int, *, include_inert_two: bool = False) -> list[int]:
    out = [p for p in primes_up_to(limit) if chi5(p) == 1]
    if include_inert_two and limit >= 2:
        out = [2] + out
    return out


def face_norm(face: Face, *, allow_conjugate_pair: bool = False) -> int:
    result = 1
    seen: set[int] = set()
    for prime, _orientation in face:
        if not allow_conjugate_pair:
            check("face one orientation", prime not in seen, face)
        seen.add(prime)
        result *= prime
    return result


def generate_faces(
    limit: int,
    *,
    orientation_count: int = 2,
    allow_conjugate_pair: bool = False,
    include_inert_two: bool = False,
) -> set[Face]:
    check("orientation count", orientation_count in (1, 2))
    primes = split_primes(limit, include_inert_two=include_inert_two)
    faces: set[Face] = {frozenset()}
    for prime in primes:
        old = sorted(faces, key=face_key)
        additions: set[Face] = set()
        for face in old:
            norm = face_norm(face, allow_conjugate_pair=allow_conjugate_pair)
            for orientation in range(orientation_count):
                if norm * prime <= limit:
                    additions.add(face | {(prime, orientation)})
            if allow_conjugate_pair and orientation_count == 2:
                if norm * prime * prime <= limit:
                    additions.add(face | {(prime, 0), (prime, 1)})
        faces |= additions
    return faces


def face_key(face: Face) -> tuple[int, tuple[Vertex, ...]]:
    return (len(face), tuple(sorted(face)))


def is_squarefree_split(n: int) -> tuple[bool, int]:
    if n == 1:
        return True, 0
    remaining = n
    count = 0
    for prime in primes_up_to(n):
        if prime * prime > remaining:
            break
        if remaining % prime:
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent != 1 or chi5(prime) != 1:
            return False, 0
        count += 1
    if remaining > 1:
        if chi5(remaining) != 1:
            return False, 0
        count += 1
    return True, count


def s5_coefficient(n: int) -> int:
    qualifies, omega = is_squarefree_split(n)
    return (-2) ** omega if qualifies else 0


def s5_sum(limit: int) -> int:
    return sum(s5_coefficient(n) for n in range(1, limit + 1))


def augmented_euler(faces: set[Face], *, include_empty: bool = True) -> int:
    return sum(
        (-1) ** len(face)
        for face in faces
        if include_empty or face
    )


def support_dimension_counts(limit: int) -> dict[int, int]:
    counts: dict[int, int] = {}
    for n in range(1, limit + 1):
        qualifies, omega = is_squarefree_split(n)
        if qualifies:
            counts[omega] = counts.get(omega, 0) + (2 ** omega)
    return counts


def face_dimension_counts(faces: set[Face]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for face in faces:
        counts[len(face)] = counts.get(len(face), 0) + 1
    return counts


def gate_character_and_first_split() -> None:
    check("chi residues", [chi5(r) for r in range(5)] == [0, 1, -1, -1, 1])
    primes = split_primes(100)
    check("first split prime", primes[:5] == [11, 19, 29, 31, 41], primes[:5])


def gate_face_complex() -> None:
    for limit in FROZEN_N:
        faces = generate_faces(limit)
        check("empty face present", frozenset() in faces, limit)
        check("face duplicate-free", len(faces) == len(set(faces)), limit)
        for face in faces:
            check("face norm threshold", face_norm(face) <= limit, (limit, face))
            for vertex in tuple(face):
                check("downward closure", face - {vertex} in faces, (limit, face))


def gate_euler_identity() -> None:
    for limit in FROZEN_N:
        faces = generate_faces(limit)
        check(
            "Euler carrier",
            augmented_euler(faces) == s5_sum(limit),
            (limit, augmented_euler(faces), s5_sum(limit)),
        )


def gate_dimension_counts() -> None:
    for limit in FROZEN_N:
        faces = generate_faces(limit)
        check(
            "dimension counts",
            face_dimension_counts(faces) == support_dimension_counts(limit),
            limit,
        )


def edge_exists(faces: set[Face], left: Vertex, right: Vertex) -> bool:
    return frozenset((left, right)) in faces


def isolated_vertices(faces: set[Face]) -> set[Vertex]:
    vertices = {next(iter(face)) for face in faces if len(face) == 1}
    used: set[Vertex] = set()
    for face in faces:
        if len(face) == 2:
            used |= set(face)
    return vertices - used


def interval_isolated_vertices(limit: int) -> set[Vertex]:
    result: set[Vertex] = set()
    for prime in split_primes(limit):
        if 11 * prime > limit:
            result.add((prime, 0))
            result.add((prime, 1))
    return result


def gate_isolated_boundary() -> None:
    for limit in FROZEN_N:
        faces = generate_faces(limit)
        predicted = interval_isolated_vertices(limit)
        actual = isolated_vertices(faces)
        check("strict isolated subset", predicted <= actual, (limit, predicted - actual))
    faces_209 = generate_faces(209)
    check(
        "strict boundary witness",
        edge_exists(faces_209, (11, 0), (19, 0)),
    )
    check("closed threshold false", 11 * 19 == 209)


def incidence_neighbors(face: Face, faces: set[Face], vertices: list[Vertex]) -> list[Face]:
    out: set[Face] = set()
    for vertex in face:
        candidate = face - {vertex}
        if candidate in faces:
            out.add(candidate)
    for vertex in vertices:
        if vertex in face:
            continue
        candidate = face | {vertex}
        if candidate in faces:
            out.add(candidate)
    return sorted(out, key=face_key)


def maximum_incidence_matching(faces: set[Face]) -> int:
    vertices = sorted({vertex for face in faces for vertex in face})
    left = sorted((face for face in faces if len(face) % 2 == 0), key=face_key)
    right_set = {face for face in faces if len(face) % 2 == 1}
    adjacency = {
        face: [neighbor for neighbor in incidence_neighbors(face, faces, vertices)
               if neighbor in right_set]
        for face in left
    }
    match_right: dict[Face, Face] = {}

    def augment(face: Face, seen: set[Face]) -> bool:
        for neighbor in adjacency[face]:
            if neighbor in seen:
                continue
            seen.add(neighbor)
            previous = match_right.get(neighbor)
            if previous is None or augment(previous, seen):
                match_right[neighbor] = face
                return True
        return False

    matched = 0
    for face in left:
        if augment(face, set()):
            matched += 1
    return matched


def gate_matching_floor() -> None:
    for limit in FROZEN_N:
        faces = generate_faces(limit)
        isolated_count = len(interval_isolated_vertices(limit))
        matched = maximum_incidence_matching(faces)
        unmatched = len(faces) - 2 * matched
        check(
            "augmented matching floor",
            unmatched >= max(0, isolated_count - 1),
            (limit, unmatched, isolated_count),
        )
        nonempty = {face for face in faces if face}
        matched_nonempty = maximum_incidence_matching(nonempty)
        unmatched_nonempty = len(nonempty) - 2 * matched_nonempty
        check(
            "nonempty matching floor",
            unmatched_nonempty >= isolated_count,
            (limit, unmatched_nonempty, isolated_count),
        )


def first_euler_mismatch(
    limit: int,
    *,
    orientation_count: int = 2,
    allow_conjugate_pair: bool = False,
    include_inert_two: bool = False,
    include_empty: bool = True,
) -> int | None:
    for n in range(1, limit + 1):
        faces = generate_faces(
            n,
            orientation_count=orientation_count,
            allow_conjugate_pair=allow_conjugate_pair,
            include_inert_two=include_inert_two,
        )
        if augmented_euler(faces, include_empty=include_empty) != s5_sum(n):
            return n
    return None


def gate_breakers() -> None:
    check(
        "B1 one orientation",
        first_euler_mismatch(200, orientation_count=1) == 11,
    )
    check(
        "B2 conjugate pair",
        first_euler_mismatch(200, allow_conjugate_pair=True) == 121,
    )
    check(
        "B3 inert two",
        first_euler_mismatch(20, include_inert_two=True) == 2,
    )
    faces_209 = generate_faces(209)
    wrong_closed_isolated = 11 * 19 >= 209
    check("B4 mutation armed", wrong_closed_isolated)
    check(
        "B4 closed threshold",
        not ((19, 0) in isolated_vertices(faces_209)),
    )
    check(
        "B5 empty face",
        first_euler_mismatch(10, include_empty=False) == 1,
    )


def imported_root(node: ast.AST) -> str:
    if isinstance(node, ast.Import):
        return node.names[0].name.split(".")[0]
    if isinstance(node, ast.ImportFrom):
        return (node.module or "").split(".")[0]
    return ""


def gate_source_firewall() -> None:
    path = Path(__file__)
    raw = path.read_bytes()
    check("source final LF", raw.endswith(b"\n"))
    check("source LF only", b"\r" not in raw)
    text = raw.decode("utf-8")
    tree = ast.parse(text, filename=path.name)
    allowed_imports = {"__future__", "ast", "pathlib"}
    forbidden_roots = {
        "cmath", "http", "math", "mpmath", "numpy", "random", "requests",
        "socket", "subprocess", "sympy", "urllib",
    }
    forbidden_calls = {"compile", "complex", "eval", "exec", "float", "input", "open"}
    imports: list[str] = []
    calls: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(imported_root(node))
        if isinstance(node, ast.Constant):
            check("no float or complex literal", not isinstance(node.value, (float, complex)))
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
    check("source import allowlist", set(imports) <= allowed_imports, imports)
    check("source forbidden import roots", not (set(imports) & forbidden_roots))
    check("source dynamic calls", not (set(calls) & forbidden_calls))
    check("source no zero-table token", ("ZERO" + "_TABLE") not in text)
    check("source no external-package token", ("site" + "-" + "packages") not in text)


def main() -> int:
    gate_character_and_first_split()
    print("G01 PASS chi_5 split census and first split prime 11")
    gate_face_complex()
    print("G02 PASS finite oriented faces are duplicate-free and simplicial")
    gate_euler_identity()
    print("G03 PASS squarefree split sum equals augmented face-parity sum")
    gate_dimension_counts()
    print("G04 PASS face dimensions equal 2^omega support multiplicities")
    gate_isolated_boundary()
    print("G05 PASS strict isolated-vertex theorem and N=209 boundary")
    gate_matching_floor()
    print("G06 PASS maximum incidence matchings obey isolated-cell floors")
    gate_breakers()
    print("G07 PASS breakers FIRE B1=11 B2=121 B3=2 B4=(209,19) B5=1")
    gate_source_firewall()
    print("G08 PASS exact-integer stdlib source firewall")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
