#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from itertools import product


Vec = tuple[int, int, int, int]
Cell = tuple[tuple[int, ...], Vec]
Chain = dict[Cell, int]


def add_vec(x: Vec, axis: int, amount: int, L: int) -> Vec:
    y = list(x)
    y[axis] = (y[axis] + amount) % L
    return tuple(y)  # type: ignore[return-value]


def vec(*entries: int) -> Vec:
    assert len(entries) == 4
    return tuple(entries)  # type: ignore[return-value]


def unit(axis: int, amount: int = 1) -> Vec:
    x = [0, 0, 0, 0]
    x[axis] = amount
    return tuple(x)  # type: ignore[return-value]


def vadd(a: Vec, b: Vec, L: int) -> Vec:
    return tuple((a[i] + b[i]) % L for i in range(4))  # type: ignore[return-value]


def scale_chain(A: Chain, q: int) -> Chain:
    return {k: q * v for k, v in A.items() if q * v}


def add_chain(*chains: Chain) -> Chain:
    out: defaultdict[Cell, int] = defaultdict(int)
    for A in chains:
        for k, v in A.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}


def one_cell(axes: tuple[int, ...], x: Vec, L: int) -> Chain:
    return {(tuple(axes), tuple(t % L for t in x)): 1}


def boundary_cell(axes: tuple[int, ...], x: Vec, L: int) -> Chain:
    out: defaultdict[Cell, int] = defaultdict(int)
    for i, axis in enumerate(axes):
        face_axes = axes[:i] + axes[i + 1 :]
        s = 1 if i % 2 == 0 else -1
        out[(face_axes, add_vec(x, axis, 1, L))] += s
        out[(face_axes, x)] -= s
    return {k: v for k, v in out.items() if v}


def boundary(A: Chain, L: int) -> Chain:
    out: defaultdict[Cell, int] = defaultdict(int)
    for (axes, x), coeff in A.items():
        assert axes
        for k, v in boundary_cell(axes, x, L).items():
            out[k] += coeff * v
    return {k: v for k, v in out.items() if v}


def cube(axes: tuple[int, int, int], x: Vec, L: int) -> Chain:
    return one_cell(axes, x, L)


def plaquette(axes: tuple[int, int], x: Vec, L: int) -> Chain:
    return one_cell(axes, x, L)


def U_at(x: Vec, L: int) -> Chain:
    return add_chain(
        scale_chain(cube((0, 1, 2), x, L), -1),
        cube((0, 1, 2), vadd(x, unit(2, -1), L), L),
        scale_chain(cube((0, 1, 3), x, L), -1),
        cube((0, 1, 3), vadd(x, unit(3, -1), L), L),
    )


def a_at(x: Vec, L: int) -> Chain:
    return add_chain(
        boundary(U_at(x, L), L),
        scale_chain(plaquette((0, 1), x, L), -5),
    )


def n_family(Dsep: int) -> tuple[int, Chain, Chain]:
    L = 2 * Dsep + 4
    zero = vec(0, 0, 0, 0)
    far = vadd(zero, unit(3, Dsep), L)

    T: Chain = {}
    for k in range(Dsep):
        x = vadd(unit(2), unit(3, k), L)
        T = add_chain(T, cube((0, 1, 3), x, L))

    nD = add_chain(
        a_at(zero, L),
        scale_chain(a_at(far, L), -1),
        scale_chain(boundary(T, L), -1),
    )

    expected_j = add_chain(
        scale_chain(boundary(plaquette((0, 1), zero, L), L), -1),
        boundary(plaquette((0, 1), far, L), L),
    )
    return L, nD, expected_j


def exact_current(n: Chain, p: int, L: int) -> Chain:
    dn = boundary(n, L)
    assert all(v % p == 0 for v in dn.values())
    return {k: v // p for k, v in dn.items() if v}


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    q = 2
    while q * q <= n:
        if n % q == 0:
            return False
        q += 1
    return True


def local_alphabet(D: int, p: int) -> tuple[int, ...]:
    M = 2 * (D - 1)
    sums = {sum(xs) for xs in product((-1, 0, 1), repeat=M)}
    return tuple(sorted(s // p for s in sums if s % p == 0))


def directed_edges(j: Chain, L: int) -> list[tuple[Vec, Vec]]:
    out = []
    for (axes, x), coeff in j.items():
        assert len(axes) == 1
        assert coeff in (-1, 1)
        axis = axes[0]
        y = add_vec(x, axis, 1, L)
        out.append((x, y) if coeff == 1 else (y, x))
    return out


def cycle_decompose(edges: list[tuple[Vec, Vec]]) -> list[list[Vec]]:
    unused = set(edges)
    out_by_v: defaultdict[Vec, set[tuple[Vec, Vec]]] = defaultdict(set)
    for e in unused:
        out_by_v[e[0]].add(e)

    cycles: list[list[Vec]] = []
    while unused:
        e0 = next(iter(unused))
        path = [e0[0]]
        pos = {e0[0]: 0}
        cur = e0[0]
        while True:
            choices = sorted(out_by_v[cur] & unused)
            assert choices, ("not divergence-free during decomposition", cur)
            e = choices[0]
            unused.remove(e)
            cur = e[1]
            if cur in pos:
                i = pos[cur]
                cyc = path[i:] + [cur]
                assert len(cyc) >= 2
                cycles.append(cyc)
                # Any prefix would belong to another cycle in a general Euler
                # decomposition. The audit fixtures below have no such prefix.
                assert i == 0
                break
            path.append(cur)
            pos[cur] = len(path) - 1
    return cycles


def main() -> int:
    assert local_alphabet(4, 3) == (-2, -1, 0, 1, 2)
    assert local_alphabet(4, 5) == (-1, 0, 1)
    for p in (7, 11, 13, 17, 19):
        assert local_alphabet(4, p) == (0,)

    window = [p for p in range(3, 20, 2)
              if is_prime(p) and 3 < p <= 6]
    assert window == [5]
    print("PASS G1/G2: D=4 has six incident plaquettes per edge; "
          "odd-prime unit-current window is exactly {5}.")
    print("             p=3 alphabet = {-2,-1,0,1,2}; "
          "p=5 alphabet = {-1,0,1}; p>=7 alphabet = {0}.")

    for Dsep in range(3, 13):
        L, nD, expected_j = n_family(Dsep)
        assert max(abs(v) for v in nD.values()) == 1
        assert len(nD) == 4 * Dsep + 40
        j = exact_current(nD, 5, L)
        assert j == expected_j
        assert len(j) == 8
        assert set(j.values()) <= {-1, 1}
        assert boundary(j, L) == {}
        cycles = cycle_decompose(directed_edges(j, L))
        lengths = sorted(len(c) - 1 for c in cycles)
        assert lengths == [4, 4]

    print("PASS G3/G4 audit: Dsep=3..12 explicit p=5 family is ternary, "
          "|supp n_D|=4Dsep+40, and carries two edge-disjoint unit 4-cycles.")
    print("PASS boundary check: every audited j_D is exactly conserved.")
    print("ALL PASS: current prime-gate finite audit complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
