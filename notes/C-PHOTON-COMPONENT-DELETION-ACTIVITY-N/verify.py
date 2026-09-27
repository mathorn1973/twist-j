#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import factorial


Vec = tuple[int, int, int, int]
Cell = tuple[tuple[int, ...], Vec]
Chain = dict[Cell, int]


def vadd(a: Vec, b: Vec) -> Vec:
    return tuple(a[i] + b[i] for i in range(4))  # type: ignore[return-value]


def unit(axis: int, amount: int = 1) -> Vec:
    x = [0, 0, 0, 0]
    x[axis] = amount
    return tuple(x)  # type: ignore[return-value]


def add_chain(*chains: Chain) -> Chain:
    out: defaultdict[Cell, int] = defaultdict(int)
    for A in chains:
        for k, v in A.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}


def scale_chain(A: Chain, q: int) -> Chain:
    return {k: q * v for k, v in A.items() if q * v}


def cell(axes: tuple[int, ...], x: Vec) -> Chain:
    return {(tuple(axes), x): 1}


def boundary_cell(axes: tuple[int, ...], x: Vec) -> Chain:
    out: defaultdict[Cell, int] = defaultdict(int)
    for i, axis in enumerate(axes):
        face_axes = axes[:i] + axes[i + 1 :]
        s = 1 if i % 2 == 0 else -1
        out[(face_axes, vadd(x, unit(axis)))] += s
        out[(face_axes, x)] -= s
    return {k: v for k, v in out.items() if v}


def boundary(A: Chain) -> Chain:
    out: defaultdict[Cell, int] = defaultdict(int)
    for (axes, x), coeff in A.items():
        for k, v in boundary_cell(axes, x).items():
            out[k] += coeff * v
    return {k: v for k, v in out.items() if v}


def four_cup(x: Vec) -> Chain:
    U = add_chain(
        scale_chain(cell((0, 1, 2), x), -1),
        cell((0, 1, 2), vadd(x, unit(2, -1))),
        scale_chain(cell((0, 1, 3), x), -1),
        cell((0, 1, 3), vadd(x, unit(3, -1))),
    )
    return add_chain(
        boundary(U),
        scale_chain(cell((0, 1), x), -5),
    )


def expected_current(N: int) -> Chain:
    out: Chain = {}
    for i in range(N):
        x = (0, 0, -i, -i)
        term = boundary(cell((0, 1), x))
        out = add_chain(out, scale_chain(term, -(1 if i % 2 == 0 else -1)))
    return out


def chain_N(N: int) -> Chain:
    out: Chain = {}
    for i in range(N):
        x = (0, 0, -i, -i)
        out = add_chain(
            out,
            scale_chain(four_cup(x), 1 if i % 2 == 0 else -1),
        )
    return out


def edge_incidence(n: Chain):
    inc: defaultdict[Cell, list[tuple[Cell, int]]] = defaultdict(list)
    for face, coeff in n.items():
        axes, x = face
        assert len(axes) == 2
        for edge, eps in boundary_cell(axes, x).items():
            inc[edge].append((face, coeff * eps))
    return inc


def component_graph(n: Chain):
    inc = edge_incidence(n)
    graph: defaultdict[Cell, set[Cell]] = defaultdict(set)
    degree_census: defaultdict[int, int] = defaultdict(int)
    charged = 0

    for entries in inc.values():
        d = len(entries)
        degree_census[d] += 1
        s = sum(v for _, v in entries)
        faces = [f for f, _ in entries]

        if s:
            assert d == 5
            assert abs(s) == 5
            assert len(set(v for _, v in entries)) == 1
            charged += 1
            # Degree-five junction links all five faces.
            for i in range(len(faces)):
                for j in range(i):
                    graph[faces[i]].add(faces[j])
                    graph[faces[j]].add(faces[i])
        else:
            # The frozen defect chain must have only degree-two neutral edges.
            assert d == 2
            assert entries[0][1] == -entries[1][1]
            f, g = faces
            graph[f].add(g)
            graph[g].add(f)

    faces = set(n)
    if faces:
        start = next(iter(faces))
        seen = {start}
        stack = [start]
        while stack:
            f = stack.pop()
            for g in graph[f]:
                if g not in seen:
                    seen.add(g)
                    stack.append(g)
    else:
        seen = set()

    return dict(degree_census), charged, len(seen)


def audit_factorials() -> int:
    count = 0
    for r in range(4):
        for t in range(r + 1):
            lhs = Fraction(factorial(r - t), factorial(r))
            rhs = Fraction(1, factorial(t))
            assert lhs <= rhs
            count += 1
    return count


def audit_local_motif() -> None:
    A = four_cup((0, 0, 0, 0))
    assert len(A) == 21
    dA = boundary(A)
    expected = scale_chain(boundary(cell((0, 1), (0, 0, 0, 0))), -5)
    assert dA == expected
    assert max(abs(v) for v in A.values()) == 1

    B = four_cup((0, 0, -1, -1))
    common = set(A) & set(B)
    assert len(common) == 2
    assert all(A[f] == B[f] for f in common)
    assert all(f[0] == (0, 1) for f in common)

    for sep in range(2, 8):
        C = four_cup((0, 0, -sep, -sep))
        assert set(A).isdisjoint(C)


def audit_chain() -> None:
    for N in range(1, 65):
        n = chain_N(N)
        assert max(abs(v) for v in n.values()) == 1
        assert len(n) == 17 * N + 4

        dn = boundary(n)
        assert all(v % 5 == 0 for v in dn.values())
        j = {k: v // 5 for k, v in dn.items() if v}
        assert j == expected_current(N)
        assert len(j) == 4 * N
        assert all(abs(v) == 1 for v in j.values())
        assert boundary(j) == {}

        degree_census, charged, seen = component_graph(n)
        assert set(degree_census) == {2, 5}
        assert charged == 4 * N
        assert seen == len(n)

        assert Fraction(len(n), len(j)) == Fraction(17, 4) + Fraction(1, N)


def main() -> int:
    count = audit_factorials()
    print(
        "PASS G1 audit: factorial deletion inequality holds for all "
        f"0<=t<=r<=3 ({count} cases)."
    )

    audit_local_motif()
    print(
        "PASS G4 motif: one defect has 21 faces; adjacent diagonal defects "
        "share exactly two equal 01 faces; separation >=2 is face-disjoint."
    )

    audit_chain()
    print(
        "PASS G4 chain: N=1..64 gives A=17N+4, M=4N, ternary conserved "
        "unit current, neutral degree 2, charged degree 5, one connected component."
    )

    print(
        "PASS G5 control: N=2 already has A/M=19/4 < 21/4; "
        "the family tends exactly to 17/4."
    )

    print("ALL PASS: component deletion/activity finite audit complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
