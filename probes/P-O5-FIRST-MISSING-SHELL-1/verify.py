#!/usr/bin/env python3
"""Exact audit for P-O5-FIRST-MISSING-SHELL-1."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


def check(label, ok, detail=""):
    if not ok:
        raise AssertionError(f"{label} failed: {detail}")


def chi5(n):
    r = n % 5
    return 0 if r == 0 else (1 if r in (1, 4) else -1)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def split_primes(limit):
    return tuple(
        p for p in range(2, limit + 1)
        if is_prime(p) and chi5(p) == 1
    )


SPLIT_TABLE = split_primes(20000)


def support_faces(N, allowed=None):
    if allowed is None:
        ps = split_primes(N)
    else:
        ps = tuple(p for p in allowed if p <= N)
    out = []

    def extend(start, chosen, norm):
        out.append(tuple(chosen))
        for index in range(start, len(ps)):
            p = ps[index]
            nxt = norm * p
            if nxt > N:
                break
            chosen.append(p)
            extend(index + 1, chosen, nxt)
            chosen.pop()

    extend(0, [], 1)
    return tuple(out)


def face_product(face):
    value = 1
    for p in face:
        value *= p
    return value


def least_missing(face):
    used = set(face)
    for p in SPLIT_TABLE:
        if p not in used:
            return p
    raise AssertionError("split table exhausted")


def second_missing(face):
    used = set(face)
    seen = 0
    for p in SPLIT_TABLE:
        if p not in used:
            seen += 1
            if seen == 2:
                return p
    raise AssertionError("split table exhausted")


def link_faces(N, J):
    J = tuple(sorted(J))
    j = face_product(J)
    M = N // j
    used = set(J)
    allowed = tuple(p for p in split_primes(M) if p not in used)
    return support_faces(M, allowed)


def terminal_faces(N, J, *, weak=False, allow_r=False):
    J = tuple(sorted(J))
    M = N // face_product(J)
    r = least_missing(J)
    out = []
    for F in link_faces(N, J):
        if not allow_r and r in F:
            continue
        lhs = r * face_product(F)
        terminal = lhs >= M if weak else lhs > M
        if terminal:
            out.append(F)
    return tuple(out)


def cone_member(N, J, F):
    M = N // face_product(J)
    r = least_missing(J)
    if r in F:
        return True
    return r * face_product(F) <= M


def grouped(faces):
    out = {}
    for F in faces:
        out.setdefault(len(F) - 1, []).append(F)
    return out


def rank_q(matrix):
    if not matrix or not matrix[0]:
        return 0
    A = [[Fraction(x) for x in row] for row in matrix]
    nrow = len(A)
    ncol = len(A[0])
    row = 0
    for col in range(ncol):
        pivot = next(
            (i for i in range(row, nrow) if A[i][col]),
            None,
        )
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        q = A[row][col]
        A[row] = [x / q for x in A[row]]
        for i in range(nrow):
            if i != row and A[i][col]:
                q = A[i][col]
                A[i] = [
                    A[i][j] - q * A[row][j]
                    for j in range(ncol)
                ]
        row += 1
        if row == nrow:
            break
    return row


def boundary_rank(faces, degree):
    groups = grouped(faces)
    source = groups.get(degree, [])
    target = groups.get(degree - 1, [])
    if not source or not target:
        return 0
    target_index = {F: i for i, F in enumerate(target)}
    matrix = [[0] * len(source) for _ in target]
    for col, F in enumerate(source):
        for i in range(len(F)):
            lower = F[:i] + F[i + 1:]
            matrix[target_index[lower]][col] += -1 if i % 2 else 1
    return rank_q(matrix)


def betti_augmented(faces):
    groups = grouped(faces)
    low = min(groups)
    high = max(groups)
    ranks = {
        degree: boundary_rank(faces, degree)
        for degree in range(low, high + 2)
    }
    out = {}
    for degree in range(low, high + 1):
        value = (
            len(groups.get(degree, []))
            - ranks.get(degree, 0)
            - ranks.get(degree + 1, 0)
        )
        if value:
            out[degree] = value
    return out


def terminal_counts(N, J):
    out = {}
    for F in terminal_faces(N, J):
        degree = len(F) - 1
        out[degree] = out.get(degree, 0) + 1
    return out


def partitions_of_support(S):
    for mask in range(1 << len(S)):
        J = tuple(S[i] for i in range(len(S)) if mask >> i & 1)
        F = tuple(S[i] for i in range(len(S)) if not (mask >> i & 1))
        yield J, F


def pair_sign(J, F):
    return -1 if (len(J) + len(F)) % 2 else 1


def pair_norm(J, F):
    return face_product(J) * face_product(F)


def toggle_pair(N, J, F):
    r = least_missing(J)
    if r in F:
        return J, tuple(p for p in F if p != r)
    if pair_norm(J, F) * r <= N:
        return J, tuple(sorted(F + (r,)))
    return None


def s5_sum(N):
    return sum((-2) ** len(S) for S in support_faces(N))


def first_missing_sum(
    N,
    *,
    missing_mode="least",
    weak=False,
    multiplicity="tail",
    require_terminal=True,
):
    total = 0
    for S in support_faces(N):
        n = face_product(S)
        r = least_missing(S) if missing_mode == "least" else second_missing(S)
        terminal = n * r >= N if weak else n * r > N
        if require_terminal and not terminal:
            continue
        if multiplicity == "tail":
            exponent = sum(1 for p in S if p > r)
        else:
            exponent = len(S)
        total += (-1) ** len(S) * (2 ** exponent)
    return total


def tail_sum(X, q):
    if X <= 0:
        return 0
    allowed = tuple(p for p in split_primes(X) if p > q)
    total = 0
    for S in support_faces(X, allowed):
        total += (-2) ** len(S)
    return total


def primorial_shell_sum(N):
    total = 0
    Q = 1
    index = 0
    while Q <= N:
        q = SPLIT_TABLE[index]
        X = N // Q
        total += (-1) ** index * (
            tail_sum(X, q) - tail_sum(N // (Q * q), q)
        )
        Q *= q
        index += 1
    return total


def gate_01():
    check("first split primes", SPLIT_TABLE[:5] == (11, 19, 29, 31, 41))
    for N in (1, 11, 19, 121, 209, 500):
        for J in support_faces(N):
            r = least_missing(J)
            used = set(J)
            check(
                "least missing",
                r not in used and all(p in used for p in SPLIT_TABLE if p < r),
                (N, J, r),
            )
            for p in {x for F in link_faces(N, J) for x in F}:
                if p != r:
                    check("link order", p > r, (N, J, r, p))


def gate_02():
    for N in (1, 10, 11, 19, 121, 209, 500, 1000):
        for J in support_faces(N):
            L = link_faces(N, J)
            C = set(terminal_faces(N, J))
            A = {F for F in L if cone_member(N, J, F)}
            check("partition", A.isdisjoint(C) and A | C == set(L), (N, J))
            r = least_missing(J)
            M = N // face_product(J)
            if r > M:
                check("empty base case", L == ((),) and C == {()}, (N, J))
            for F in C:
                for i in range(len(F)):
                    lower = F[:i] + F[i + 1:]
                    check("terminal boundary in cone", lower in A, (N, J, F))


def gate_03():
    for N in (1, 11, 19, 121, 209, 500):
        for J in support_faces(N):
            actual = betti_augmented(link_faces(N, J))
            expected = terminal_counts(N, J)
            check("Betti terminal count", actual == expected, (N, J, actual, expected))


def gate_04():
    for N in (1, 10, 11, 19, 121, 209, 500, 1000):
        pairs = []
        for S in support_faces(N):
            pairs.extend(partitions_of_support(S))
        pair_set = set(pairs)
        unmatched = []
        for J, F in pairs:
            partner = toggle_pair(N, J, F)
            if partner is None:
                unmatched.append((J, F))
            else:
                check("partner exists", partner in pair_set, (N, J, F, partner))
                check(
                    "involution",
                    toggle_pair(N, *partner) == (J, F),
                    (N, J, F, partner),
                )
                check(
                    "sign reversal",
                    pair_sign(J, F) == -pair_sign(*partner),
                    (N, J, F),
                )
        check(
            "pair sum",
            sum(pair_sign(J, F) for J, F in unmatched) == s5_sum(N),
            N,
        )
        fibres = {}
        for J, F in unmatched:
            S = tuple(sorted(J + F))
            n = face_product(S)
            fibres[n] = fibres.get(n, 0) + 1
        for S in support_faces(N):
            n = face_product(S)
            r = least_missing(S)
            expected = 0
            if n * r > N:
                expected = 2 ** sum(1 for p in S if p > r)
            check("terminal fibre", fibres.get(n, 0) == expected, (N, S))


def gate_05():
    for N in range(1, 401):
        check("first-missing identity", first_missing_sum(N) == s5_sum(N), N)
    for N in (500, 1000, 2000, 5000, 10000):
        check("first-missing witness", first_missing_sum(N) == s5_sum(N), N)


def gate_06():
    for N in (1, 10, 11, 19, 50, 121, 209, 500, 1000, 5000, 10000):
        check("primorial shell", primorial_shell_sum(N) == s5_sum(N), N)


def gate_07():
    check(
        "B1",
        first_missing_sum(11, missing_mode="second") != s5_sum(11),
    )
    check(
        "B2",
        first_missing_sum(11, weak=True) != s5_sum(11),
    )
    check(
        "B3",
        (11,) in terminal_faces(11, (), allow_r=True)
        and (11,) not in terminal_faces(11, ()),
    )
    check(
        "B4",
        first_missing_sum(11, multiplicity="omega") != s5_sum(11),
    )
    check(
        "B5",
        first_missing_sum(11, require_terminal=False) != s5_sum(11),
    )


def imported_root(node):
    if isinstance(node, ast.Import):
        return node.names[0].name.split(".")[0]
    if isinstance(node, ast.ImportFrom):
        return (node.module or "").split(".")[0]
    return ""


def gate_08():
    path = Path(__file__)
    raw = path.read_bytes()
    check("final LF", raw.endswith(b"\n"))
    check("LF only", b"\r" not in raw)
    text = raw.decode("utf-8")
    tree = ast.parse(text, filename=path.name)
    allowed = {"__future__", "ast", "fractions", "pathlib"}
    forbidden_roots = {
        "cmath", "http", "math", "mpmath", "numpy", "random",
        "requests", "socket", "subprocess", "sympy", "urllib",
    }
    forbidden_calls = {
        "compile", "complex", "eval", "exec", "float", "input", "open",
    }
    imports = []
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(imported_root(node))
        if isinstance(node, ast.Constant):
            check(
                "no float or complex literal",
                not isinstance(node.value, (float, complex)),
            )
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
    check("import allowlist", set(imports) <= allowed, imports)
    check("forbidden imports", not (set(imports) & forbidden_roots))
    check("dynamic calls", not (set(calls) & forbidden_calls))


def main():
    gate_01()
    print("G01 PASS split order and link carrier")
    gate_02()
    print("G02 PASS terminal cone quotient")
    gate_03()
    print("G03 PASS link Betti terminal counts")
    gate_04()
    print("G04 PASS sign-reversing terminal-pair involution")
    gate_05()
    print("G05 PASS first-missing terminal-shell identity")
    gate_06()
    print("G06 PASS primorial terminal-shell identity")
    gate_07()
    print("G07 PASS breakers B1=B2=B3=B4=B5=11")
    gate_08()
    print("G08 PASS exact-rational stdlib firewall")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
