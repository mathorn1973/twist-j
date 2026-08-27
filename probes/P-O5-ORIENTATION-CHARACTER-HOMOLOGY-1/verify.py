#!/usr/bin/env python3
"""Exact audit for P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1.

This verifier audits the finite Walsh-character boundary decomposition of the
oriented split threshold complex. It uses exact integer and Fraction arithmetic.
It does not evaluate zeta or L-functions, inspect zeros, or prove cancellation.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


def fail(label: str, detail: object = "") -> None:
    message = f"{label} failed"
    if detail != "":
        message += f": {detail}"
    raise AssertionError(message)


def check(label: str, condition: bool, detail: object = "") -> None:
    if not condition:
        fail(label, detail)


def chi5(n: int) -> int:
    residue = n % 5
    if residue == 0:
        return 0
    return 1 if residue in (1, 4) else -1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def split_primes(N: int) -> tuple[int, ...]:
    return tuple(p for p in range(2, N + 1) if is_prime(p) and chi5(p) == 1)


def support_faces(N: int) -> tuple[tuple[int, ...], ...]:
    primes = split_primes(N)
    faces: list[tuple[int, ...]] = [()]
    for size in range(1, len(primes) + 1):
        for subset in combinations(primes, size):
            norm = 1
            for p in subset:
                norm *= p
                if norm > N:
                    break
            if norm <= N:
                faces.append(subset)
    return tuple(faces)


def subsets(source: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    out: list[tuple[int, ...]] = []
    for size in range(len(source) + 1):
        out.extend(combinations(source, size))
    return tuple(out)


def orientations(S: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(product((-1, 1), repeat=len(S)))


def oriented_face(S: tuple[int, ...], eps: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple((p, sign) for p, sign in zip(S, eps))


def walsh_vector(
    S: tuple[int, ...],
    J: tuple[int, ...],
) -> dict[tuple[tuple[int, int], ...], int]:
    Jset = set(J)
    out: dict[tuple[tuple[int, int], ...], int] = {}
    for eps in orientations(S):
        weight = 1
        for p, sign in zip(S, eps):
            if p in Jset:
                weight *= sign
        out[oriented_face(S, eps)] = weight
    return out


def add_scaled(
    target: dict[object, Fraction],
    source: dict[object, int | Fraction],
    scale: int | Fraction,
) -> None:
    factor = Fraction(scale)
    for key, value in source.items():
        target[key] = target.get(key, Fraction(0)) + factor * Fraction(value)
        if target[key] == 0:
            del target[key]


def boundary_oriented(
    face: tuple[tuple[int, int], ...],
) -> dict[tuple[tuple[int, int], ...], int]:
    if not face:
        return {}
    out: dict[tuple[tuple[int, int], ...], int] = {}
    for index in range(len(face)):
        lower = face[:index] + face[index + 1 :]
        out[lower] = out.get(lower, 0) + (-1 if index % 2 else 1)
    return out


def boundary_walsh_direct(
    S: tuple[int, ...],
    J: tuple[int, ...],
) -> dict[tuple[tuple[int, int], ...], Fraction]:
    out: dict[tuple[tuple[int, int], ...], Fraction] = {}
    for face, coefficient in walsh_vector(S, J).items():
        add_scaled(out, boundary_oriented(face), coefficient)
    return out


def boundary_walsh_formula(
    S: tuple[int, ...],
    J: tuple[int, ...],
    *,
    keep_J_deletions: bool = False,
    omit_factor_two: bool = False,
) -> dict[tuple[tuple[int, int], ...], Fraction]:
    Jset = set(J)
    out: dict[tuple[tuple[int, int], ...], Fraction] = {}
    factor = 1 if omit_factor_two else 2
    for index, p in enumerate(S):
        if p in Jset and not keep_J_deletions:
            continue
        lower = S[:index] + S[index + 1 :]
        lower_J = tuple(q for q in J if q != p)
        add_scaled(
            out,
            walsh_vector(lower, lower_J),
            factor * (-1 if index % 2 else 1),
        )
    return out


def link_faces(
    delta: tuple[tuple[int, ...], ...],
    J: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    face_set = set(delta)
    Jset = set(J)
    vertices = sorted({p for face in delta for p in face if p not in Jset})
    out: list[tuple[int, ...]] = []
    for size in range(len(vertices) + 1):
        for T in combinations(vertices, size):
            if tuple(sorted(J + T)) in face_set:
                out.append(T)
    return tuple(out)


def nu(J: tuple[int, ...], T: tuple[int, ...]) -> int:
    return sum(1 for j in J for t in T if j < t)


def psi_vector(
    J: tuple[int, ...],
    T: tuple[int, ...],
    *,
    omit_sign: bool = False,
) -> dict[tuple[tuple[int, int], ...], Fraction]:
    S = tuple(sorted(J + T))
    sign = 1 if omit_sign or nu(J, T) % 2 == 0 else -1
    scale = Fraction(sign, 2 ** len(T))
    out: dict[tuple[tuple[int, int], ...], Fraction] = {}
    add_scaled(out, walsh_vector(S, J), scale)
    return out


def boundary_support(
    T: tuple[int, ...],
) -> dict[tuple[int, ...], int]:
    if not T:
        return {}
    out: dict[tuple[int, ...], int] = {}
    for index in range(len(T)):
        lower = T[:index] + T[index + 1 :]
        out[lower] = out.get(lower, 0) + (-1 if index % 2 else 1)
    return out


def gate_walsh_basis() -> None:
    for size in range(0, 6):
        S = tuple(range(1, size + 1))
        Js = subsets(S)
        epss = orientations(S)
        matrix: list[list[int]] = []
        for J in Js:
            Jset = set(J)
            row: list[int] = []
            for eps in epss:
                weight = 1
                for p, sign in zip(S, eps):
                    if p in Jset:
                        weight *= sign
                row.append(weight)
            matrix.append(row)
        target = 2 ** size
        for i, left in enumerate(matrix):
            for j, right in enumerate(matrix):
                dot = sum(a * b for a, b in zip(left, right))
                check("Walsh orthogonality", dot == (target if i == j else 0), (size, i, j, dot))


def gate_boundary_formula() -> None:
    for N in (11, 121, 209, 500):
        delta = support_faces(N)
        for S in delta:
            for J in subsets(S):
                direct = boundary_walsh_direct(S, J)
                formula = boundary_walsh_formula(S, J)
                check("Walsh boundary formula", direct == formula, (N, S, J))


def gate_link_chain_map() -> None:
    for N in (11, 121, 209, 500):
        delta = support_faces(N)
        for J in delta:
            link = link_faces(delta, J)
            for T in link:
                left: dict[tuple[tuple[int, int], ...], Fraction] = {}
                for face, coefficient in psi_vector(J, T).items():
                    add_scaled(left, boundary_oriented(face), coefficient)

                right: dict[tuple[tuple[int, int], ...], Fraction] = {}
                for lower, coefficient in boundary_support(T).items():
                    add_scaled(right, psi_vector(J, lower), coefficient)
                check("link chain map", left == right, (N, J, T))


def k_faces(N: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    out: list[tuple[tuple[int, int], ...]] = [()]
    for S in support_faces(N):
        if not S:
            continue
        out.extend(oriented_face(S, eps) for eps in orientations(S))
    return tuple(out)


def faces_by_degree(faces: tuple[tuple, ...]) -> dict[int, list[tuple]]:
    out: dict[int, list[tuple]] = {}
    for face in faces:
        out.setdefault(len(face) - 1, []).append(face)
    return out


def rank_fraction(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [[Fraction(value) for value in row] for row in matrix]
    nrows = len(rows)
    ncols = len(rows[0]) if rows else 0
    rank = 0
    col = 0
    while rank < nrows and col < ncols:
        pivot = next((r for r in range(rank, nrows) if rows[r][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for r in range(nrows):
            if r == rank or rows[r][col] == 0:
                continue
            factor = rows[r][col]
            rows[r] = [
                rows[r][c] - factor * rows[rank][c]
                for c in range(ncols)
            ]
        rank += 1
        col += 1
    return rank


def boundary_rank(faces_by_dim: dict[int, list[tuple]], degree: int) -> int:
    source = faces_by_dim.get(degree, [])
    target = faces_by_dim.get(degree - 1, [])
    if not source or not target:
        return 0
    row_index = {face: i for i, face in enumerate(target)}
    matrix = [[0 for _ in source] for _ in target]
    for col, face in enumerate(source):
        for index in range(len(face)):
            lower = face[:index] + face[index + 1 :]
            matrix[row_index[lower]][col] += -1 if index % 2 else 1
    return rank_fraction(matrix)


def betti_numbers(faces: tuple[tuple, ...]) -> dict[int, int]:
    grouped = faces_by_degree(faces)
    if not grouped:
        return {}
    min_degree = -1
    max_degree = max(grouped)
    ranks = {degree: boundary_rank(grouped, degree) for degree in range(min_degree, max_degree + 1)}
    betti: dict[int, int] = {}
    for degree in range(min_degree, max_degree + 1):
        dim = len(grouped.get(degree, []))
        value = dim - ranks.get(degree, 0) - ranks.get(degree + 1, 0)
        if value:
            betti[degree] = value
    return betti


def link_chain_faces(delta: tuple[tuple[int, ...], ...], J: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return link_faces(delta, J)


def gate_betti_decomposition() -> None:
    for N in (1, 11, 121, 209, 500):
        delta = support_faces(N)
        full = betti_numbers(k_faces(N))
        expected: dict[int, int] = {}
        for J in delta:
            link_betti = betti_numbers(link_chain_faces(delta, J))
            shift = len(J)
            for degree, value in link_betti.items():
                q = degree + shift
                expected[q] = expected.get(q, 0) + value
        expected = {q: v for q, v in expected.items() if v}
        check("Betti decomposition", full == expected, (N, full, expected))


def parity_sign(integer: int) -> int:
    return -1 if integer % 2 else 1


def reduced_euler_from_faces(faces: tuple[tuple, ...]) -> int:
    return sum(parity_sign(len(face) - 1) for face in faces)


def gate_euler_decomposition() -> None:
    for N in (1, 11, 121, 209, 500, 1000):
        delta = support_faces(N)
        lhs = reduced_euler_from_faces(k_faces(N))
        rhs = 0
        for J in delta:
            rhs += parity_sign(len(J)) * reduced_euler_from_faces(link_chain_faces(delta, J))
        check("Euler decomposition", lhs == rhs, (N, lhs, rhs))


def rank_mod2(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [[value & 1 for value in row] for row in matrix]
    nrows = len(rows)
    ncols = len(rows[0]) if rows else 0
    rank = 0
    col = 0
    while rank < nrows and col < ncols:
        pivot = next((r for r in range(rank, nrows) if rows[r][col]), None)
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for r in range(nrows):
            if r != rank and rows[r][col]:
                rows[r] = [a ^ b for a, b in zip(rows[r], rows[rank])]
        rank += 1
        col += 1
    return rank


def gate_breakers() -> list[str]:
    fired: list[str] = []

    # B1: removing character signs makes two support-level Walsh rows equal.
    unsigned = [[1, 1], [1, 1]]
    check("B1 unsigned Walsh collapse", rank_fraction(unsigned) == 1)
    fired.append("B1=11")

    # B2: a J-deletion term is forbidden. S=J={11} has zero true boundary.
    S = (11,)
    J = (11,)
    check(
        "B2 keep J deletion",
        boundary_walsh_direct(S, J) != boundary_walsh_formula(S, J, keep_J_deletions=True),
    )
    fired.append("B2=11")

    # B3: the factor two is load-bearing in the trivial character sector.
    J = ()
    check(
        "B3 omit factor two",
        boundary_walsh_direct(S, J) != boundary_walsh_formula(S, J, omit_factor_two=True),
    )
    fired.append("B3=11")

    # B4: the ordering correction is load-bearing at J={11}, T={19}.
    J = (11,)
    T = (19,)
    left: dict[tuple[tuple[int, int], ...], Fraction] = {}
    for face, coefficient in psi_vector(J, T, omit_sign=True).items():
        add_scaled(left, boundary_oriented(face), coefficient)
    right: dict[tuple[tuple[int, int], ...], Fraction] = {}
    for lower, coefficient in boundary_support(T).items():
        add_scaled(right, psi_vector(J, lower, omit_sign=True), coefficient)
    check("B4 omit nu sign", left != right)
    fired.append("B4=(209;11,19)")

    # B5: the 2x2 Walsh matrix collapses in characteristic two.
    walsh_2 = [[1, 1], [1, -1]]
    check("B5 characteristic two collapse", rank_mod2(walsh_2) == 1)
    fired.append("B5=char2")

    return fired


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
    allowed = {"__future__", "ast", "fractions", "itertools", "pathlib"}
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
            check("no float/complex literal", not isinstance(node.value, (float, complex)))
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
    check("import allowlist", set(imports) <= allowed, imports)
    check("forbidden imports", not (set(imports) & forbidden_roots))
    check("dynamic calls", not (set(calls) & forbidden_calls))
    check("no target zero token", ("ZERO" + "_TABLE") not in text)


def main() -> int:
    gate_walsh_basis()
    print("G01 PASS support-level Walsh families are Q-bases")
    gate_boundary_formula()
    print("G02 PASS character boundary deletes only outside J with factor two")
    gate_link_chain_map()
    print("G03 PASS explicit nu_J sign and 2^-|T| scale give link chain maps")
    gate_betti_decomposition()
    print("G04 PASS rational Betti numbers equal shifted link-sector sums")
    gate_euler_decomposition()
    print("G05 PASS reduced Euler characteristic equals signed link sum")
    fired = gate_breakers()
    print("G06 PASS breakers FIRE " + " ".join(fired))
    gate_source_firewall()
    print("G07 PASS exact-rational stdlib source firewall")
    print("VERIFY RESULT 7/7 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
