#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction


D = 4
PAIRS = tuple((a, b) for a in range(D) for b in range(a + 1, D))
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}


class Torus:
    def __init__(self, L: int):
        self.L = L
        self.V = L**4
        self.n_faces = len(PAIRS) * self.V
        self.n_edges = D * self.V

    def site(self, x: tuple[int, int, int, int]) -> int:
        v = 0
        for c in x:
            v = v * self.L + (c % self.L)
        return v

    def coord(self, s: int) -> tuple[int, int, int, int]:
        out = [0] * 4
        for i in range(3, -1, -1):
            out[i] = s % self.L
            s //= self.L
        return tuple(out)  # type: ignore[return-value]

    def shift(
        self, x: tuple[int, int, int, int], axis: int, delta: int = 1
    ) -> tuple[int, int, int, int]:
        y = list(x)
        y[axis] = (y[axis] + delta) % self.L
        return tuple(y)  # type: ignore[return-value]

    def face(self, x: tuple[int, int, int, int], a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        return self.site(x) * len(PAIRS) + PAIR_INDEX[(a, b)]

    def face_data(self, p: int):
        site, pi = divmod(p, len(PAIRS))
        return self.coord(site), PAIRS[pi]

    def edge(self, x: tuple[int, int, int, int], axis: int) -> int:
        return self.site(x) * D + axis

    def edge_data(self, e: int):
        site, axis = divmod(e, D)
        return self.coord(site), axis

    def face_boundary(
        self, x: tuple[int, int, int, int], a: int, b: int
    ) -> tuple[tuple[int, int], ...]:
        if a > b:
            a, b = b, a
        return (
            (self.edge(x, a), +1),
            (self.edge(self.shift(x, a), b), +1),
            (self.edge(self.shift(x, b), a), -1),
            (self.edge(x, b), -1),
        )


def sigma(x: tuple[int, int, int, int]) -> int:
    return 1 if (x[1] + x[2] + x[3]) % 2 == 0 else -1


def matching_base(x: tuple[int, int, int, int]) -> bool:
    return (x[1] - x[2]) % 2 == 0


def make_state(t: Torus) -> dict[int, int]:
    n: dict[int, int] = {}
    for site in range(t.V):
        x = t.coord(site)
        s = sigma(x)
        n[t.face(x, 0, 2)] = s
        n[t.face(x, 0, 3)] = s
        if not matching_base(x):
            n[t.face(x, 0, 1)] = s
    return n


def boundary(t: Torus, n: dict[int, int]) -> list[int]:
    out = [0] * t.n_edges
    for p, value in n.items():
        x, (a, b) = t.face_data(p)
        for e, eps in t.face_boundary(x, a, b):
            out[e] += value * eps
    return out


def perfect_matching_and_complement_connected(t: Torus) -> None:
    # Cross-section vertices represented by (x1,x2,x3), fixing x0=0.
    L = t.L

    def yidx(y: tuple[int, int, int]) -> int:
        a, b, c = y
        return (a * L + b) * L + c

    def yshift(y: tuple[int, int, int], axis: int, delta: int):
        z = list(y)
        z[axis] = (z[axis] + delta) % L
        return tuple(z)

    match_degree = [0] * (L**3)
    adj = [[] for _ in range(L**3)]

    for x1 in range(L):
        for x2 in range(L):
            for x3 in range(L):
                y = (x1, x2, x3)
                i = yidx(y)

                # e1 edge based at y.
                yp = yshift(y, 0, +1)
                j = yidx(yp)
                is_match = (x1 - x2) % 2 == 0
                if is_match:
                    match_degree[i] += 1
                    match_degree[j] += 1
                else:
                    adj[i].append(j)
                    adj[j].append(i)

                # e2 and e3 are never in P. Add once from positive base.
                for axis in (1, 2):
                    yp = yshift(y, axis, +1)
                    j = yidx(yp)
                    adj[i].append(j)
                    adj[j].append(i)

    assert set(match_degree) == {1}, (L, set(match_degree))

    seen = {0}
    q = deque([0])
    while q:
        i = q.popleft()
        for j in adj[i]:
            if j not in seen:
                seen.add(j)
                q.append(j)
    assert len(seen) == L**3, (L, len(seen), L**3)


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1


def audit_L(L: int) -> tuple[int, int, int, int, int]:
    assert L >= 4 and L % 2 == 0
    t = Torus(L)
    perfect_matching_and_complement_connected(t)

    n = make_state(t)
    A = len(n)
    assert A == Fraction(5, 2) * L**4

    dn = boundary(t, n)
    j = [0] * t.n_edges

    for e, value in enumerate(dn):
        x, axis = t.edge_data(e)
        if axis == 0:
            expected = 5 * sigma(x)
            assert value == expected, (L, x, axis, value, expected)
            j[e] = value // 5
        else:
            assert value == 0, (L, x, axis, value)

    M = sum(v != 0 for v in j)
    assert M == L**4

    # Zero total winding in each direction. Only e0 can be nonzero.
    winding = [0, 0, 0, 0]
    for e, value in enumerate(j):
        if not value:
            continue
        _, axis = t.edge_data(e)
        winding[axis] += value
    assert winding == [0, 0, 0, 0], (L, winding)

    # Edge incidences and augmented connectivity.
    edge_entries: list[list[tuple[int, int]]] = [
        [] for _ in range(t.n_edges)
    ]
    for p, value in n.items():
        x, (a, b) = t.face_data(p)
        for e, eps in t.face_boundary(x, a, b):
            edge_entries[e].append((p, value * eps))

    dsu = DSU(t.n_faces)
    deg0 = deg2 = deg5 = 0
    charged = 0
    neutral = 0

    for e, entries in enumerate(edge_entries):
        if not entries:
            deg0 += 1
            continue
        total = sum(s for _, s in entries)
        if total:
            assert len(entries) == 5, (L, e, len(entries), total)
            assert abs(total) == 5
            sign = 1 if total > 0 else -1
            assert all(s == sign for _, s in entries)
            deg5 += 1
            charged += 1
            p0 = entries[0][0]
            for p, _ in entries[1:]:
                dsu.union(p0, p)
        else:
            assert len(entries) == 2, (L, e, len(entries))
            assert entries[0][1] == -entries[1][1]
            deg2 += 1
            neutral += 1
            dsu.union(entries[0][0], entries[1][0])

    assert charged == M
    assert deg5 == L**4
    assert deg0 + deg2 + deg5 == t.n_edges

    occupied_roots = {dsu.find(p) for p in n}
    assert len(occupied_roots) == 1, (L, len(occupied_roots))

    # Signed axial slice B(r) in the x1 direction.
    B = [0] * L
    for e, value in enumerate(j):
        if not value:
            continue
        x, axis = t.edge_data(e)
        assert axis == 0
        B[x[1]] += value
    assert B == [0] * L, (L, B)

    ell = 0
    R3_component_num = M**4
    R3_component_den = 4 * L**4
    expected = Fraction(L**12, 4)
    assert Fraction(R3_component_num, R3_component_den) == expected

    return A, M, deg0, deg2, deg5


def main() -> int:
    for L in (4, 6, 8, 10):
        A, M, d0, d2, d5 = audit_L(L)
        print(
            f"PASS L={L} A={A} M={M} A_over_M=5/2 "
            f"edge_degrees=0:{d0},2:{d2},5:{d5} "
            f"B_zero=YES ell=0 R3_component={L**12}/4"
        )
    print("ALL PASS: dense one-hole current family audit complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
