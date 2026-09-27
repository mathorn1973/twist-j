#!/usr/bin/env python3
"""Exact prospective audit of the all-contact quarter-turn contribution.

PUBLIC, NON-CANONICAL. Author: A. M. Thorn <thorn@twistj.com>.
Apache-2.0. Scope and fixed examples: PREREG.md. No external dependencies.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb

Vec = tuple[int, int, int, int]
Edge = tuple[Vec, int]


def shift(x: Vec, i: int, d: int, L: int | None = None) -> Vec:
    y = tuple(v + (d if k == i else 0) for k, v in enumerate(x))
    return tuple(v % L for v in y) if L else y


def project(x: Vec, L: int | None) -> Vec:
    return tuple(v % L for v in x) if L else x


def edges_from_path(path: tuple[Vec, ...], L: int | None = None):
    assert path[0] == path[-1]
    projected = tuple(project(x, L) for x in path)
    assert len(set(projected[:-1])) == len(path) - 1
    edges: dict[Edge, int] = {}
    axes = []
    for x, y in zip(path, path[1:]):
        diff = tuple(y[i] - x[i] for i in range(4))
        active = [i for i in range(4) if diff[i]]
        assert len(active) == 1
        i = active[0]
        assert abs(diff[i]) == 1
        base = x if diff[i] == 1 else y
        key = (project(base, L), i)
        assert key not in edges
        edges[key] = diff[i]
        axes.append(i)
    c = sum(axes[k] != axes[(k + 1) % len(axes)] for k in range(len(axes)))
    assert c >= 4
    div: dict[Vec, int] = defaultdict(int)
    for (x, i), sign in edges.items():
        div[x] -= sign
        div[shift(x, i, 1, L)] += sign
    assert not any(div.values())
    assert all(sum(s for (_, i), s in edges.items() if i == a) == 0 for a in range(4))
    return edges, c


def contact_data(edges: dict[Edge, int], c: int, L: int | None = None):
    """Use actual oriented plaquette boundary incidences, not sign shortcuts."""
    plaquettes = defaultdict(list)
    for (x, i), s in edges.items():
        for j in range(4):
            if i == j:
                continue
            lo, hi = sorted((i, j))
            coeff = 1 if i < j else -1
            plaquettes[(x, lo, hi)].append(((x, i), coeff * s))
            base = shift(x, j, -1, L)
            plaquettes[(base, lo, hi)].append(((x, i), -coeff * s))
    plus = minus = perpendicular = 0
    groups = defaultdict(set)
    for (base, lo, hi), entries in plaquettes.items():
        assert len(entries) <= 4
        for (ea, sa), (eb, sb) in combinations(entries, 2):
            if ea[1] != eb[1]:
                perpendicular += 1
                continue
            if sa == sb:
                plus += 1
                i = ea[1]
                j = hi if i == lo else lo
                transverse = tuple(base[k] for k in range(4) if k != i)
                groups[(i, j, transverse)].add(base[i])
            else:
                minus += 1
    assert perpendicular == c
    assert plus + minus <= 3 * len(edges)
    lens = []
    for ts in groups.values():
        if L:
            assert len(ts) < L
        starts = [t for t in ts if ((t - 1) % L if L else t - 1) not in ts]
        assert starts
        used = set()
        for start in sorted(starts):
            t, length = start, 0
            while t in ts:
                assert t not in used
                used.add(t)
                length += 1
                t = (t + 1) % L if L else t + 1
            lens.append(length)
        assert used == ts
    assert sum(lens) == plus
    assert len(lens) <= 6 * c
    for R in range(1, 12):
        if plus > 6 * c * (R - 1):
            assert max(lens, default=0) >= R
    return plus, minus, tuple(sorted(lens))


def primitive_cost(edges: dict[Edge, int], a: int, b: int, L: int | None = None) -> int:
    B = defaultdict(int)
    for (x, i), s in edges.items():
        if i == a:
            B[x[b]] += s
    assert sum(B.values()) == 0
    if not B:
        return 0
    indices = range(L) if L else range(min(B), max(B) + 1)
    h, H = 0, []
    for r in indices:
        h += B.get(r, 0)
        H.append(h)
    assert h == 0
    center = sorted(H)[len(H) // 2] if L else 0
    ell = sum(abs(v - center) for v in H)
    na = sum(i == a for (_, i) in edges)
    nb = sum(i == b for (_, i) in edges)
    assert 4 * ell <= na * nb
    assert 16 * ell <= len(edges)**2
    return ell


def corners_path(corners: tuple[Vec, ...]) -> tuple[Vec, ...]:
    out = [corners[0]]
    for endpoint in corners[1:] + (corners[0],):
        active = [i for i in range(4) if endpoint[i] != out[-1][i]]
        assert len(active) == 1
        i = active[0]
        while out[-1] != endpoint:
            out.append(shift(out[-1], i, 1 if endpoint[i] > out[-1][i] else -1))
    return tuple(out)


def rectangle(w: int, h: int) -> tuple[Vec, ...]:
    return corners_path(((0,0,0,0),(w,0,0,0),(w,h,0,0),(0,h,0,0)))


def lstrip(n: int) -> tuple[Vec, ...]:
    return corners_path(((0,0,0,0),(n+1,0,0,0),(n+1,1,0,0),
                         (1,1,0,0),(1,n+1,0,0),(0,n+1,0,0)))


def stair_ribbon(n: int) -> tuple[Vec, ...]:
    base = [(0,0,0,0)]
    for _ in range(n):
        base.append(shift(base[-1], 0, 1))
        base.append(shift(base[-1], 1, 1))
    return tuple(base + [shift(x, 2, 1) for x in reversed(base)] + [base[0]])


def geometry_audit() -> None:
    cases = [("rectangle", (w, h), rectangle(w, h)) for w in range(1,9) for h in range(1,9)]
    cases += [("L", (n,), lstrip(n)) for n in range(2,21)]
    cases += [("stair", (n,), stair_ribbon(n)) for n in range(2,11)]
    nonplanar = ((0,0,0,0),(1,0,0,0),(1,1,0,0),(1,1,1,0),(1,1,1,1),
                 (0,1,1,1),(0,0,1,1),(0,0,0,1),(0,0,0,0))
    cases.append(("4D", (), nonplanar))
    assert len(cases) == 93
    geometry_checks = slice_checks = 0
    r3, tau = F(41,25), F(73,70)
    assert r3**10 > tau**24
    assert r3**2 > tau**4
    for name, args, path in cases:
        lift_edges, c = edges_from_path(path)
        lift_contacts = contact_data(lift_edges, c)
        if name == "rectangle":
            assert primitive_cost(lift_edges,0,1) == args[0] * args[1]
        if name == "L":
            n = args[0]
            assert (len(lift_edges), c, lift_contacts) == (4*n+4,6,(2*n,0,(n,n)))
            assert primitive_cost(lift_edges,0,1) == 2*n+1
            if n >= 5:
                assert 4*c <= len(lift_edges)
                assert r3**(2*n) > tau**(4*n+4)
        mins = tuple(min(p[i] for p in path) for i in range(4))
        span = max(max(p[i] for p in path) - mins[i] for i in range(4))
        L = 2*(span+4)
        shifted = tuple(tuple(p[i]+L-2-mins[i] for i in range(4)) for p in path)
        for torus_path in (path, shifted):
            edges, tc = edges_from_path(torus_path, L)
            assert tc == c
            assert contact_data(edges,c,L) == lift_contacts
            for a, b in permutations(range(4), 2):
                assert primitive_cost(edges,a,b,L) == primitive_cost(lift_edges,a,b)
                slice_checks += 1
            geometry_checks += 1
    print(f"GEOMETRY PASS cycles={len(cases)} periodic_embeddings={geometry_checks} observed_axis_pairs={slice_checks}")
    print("L_STRIP PASS n=2..20; all_n_ge_5_quarter_turn_and_outside_SC_by_base_and_ratio; ribbons=n,n")


def periodization_audit() -> None:
    cases = 0
    for L in (4,6,8):
        profiles = ({r: 1 for r in range(2*L+1)},
                    {r: (-1)**r for r in range(2*L+1)},
                    {r: (2 if r < L else -1) for r in range(2*L)})
        for H in profiles:
            lo, hi = min(H), max(H)
            B = {r: H.get(r,0)-H.get(r-1,0) for r in range(lo,hi+2)}
            hp, bp = [0]*L, [0]*L
            for r, v in H.items(): hp[r%L] += v
            for r, v in B.items(): bp[r%L] += v
            assert [(hp[r]-hp[(r-1)%L]) for r in range(L)] == bp
            assert sum(abs(v) for v in hp) <= sum(abs(v) for v in H.values())
            cases += 1
    print(f"PERIODIZATION PASS synthetic_profiles={cases} support_spans_multiple_periods")


def cosh_log2(k: int) -> F:
    k = abs(k)
    return (F(2**k)+F(1,2**k))/2


def arithmetic_audit() -> tuple[F, F]:
    a, r, v = F(15625,131072), F(34,25), F(1,16)
    assert a == cosh_log2(1)**6/F(2**5)
    B = a*r**3
    A, q = 4*B, 2*B*(1+6*r*v)
    assert B == F(4913,16384) and A == F(4913,4096)
    assert q == F(741863,819200) and 0 < q < 1
    assert r*v == F(17,200) < 1
    local = 0
    for k in range(5):
        rhs = cosh_log2(1)**k*r**comb(k,2)
        for signs in product((-1,1),repeat=k):
            assert cosh_log2(sum(signs)) <= rhs
            local += 1
    tilts = 0
    for m in range(129):
        for c in range(m//4+1):
            assert (r**c)**4 <= (F(2**m)*(r*v)**c)**4
            tilts += 1
    dirs = tuple((i,s) for i in range(4) for s in (-1,1))
    state = {d: F(d==(0,1)) for d in dirs}
    for m in range(1,11):
        assert sum(state.values()) == (1+6*r*v)**(m-1)
        nxt = {d:F(0) for d in dirs}
        for (i,s), weight in state.items():
            for (j,t) in dirs:
                if (i,s)==(j,-t): continue
                nxt[j,t] += weight * (1 if i==j else r*v)
        state = nxt
    print(f"SOURCE_TILT PASS sign_patterns={local} quarter_turn_pairs={tilts} direction_transfer_lengths=1..10")
    print(f"CONSTANTS PASS B={B} A={A} q={q} integer_gap={819200-741863}")
    return A,q


def tail(q: F, R: int) -> F:
    return q**(R-1)*(F(R**3)/(1-q)+3*R**2*q/(1-q)**2+
                     3*R*q*(1+q)/(1-q)**3+q*(1+4*q+q*q)/(1-q)**4)


def series_audit(A: F, q: F) -> None:
    for n in range(33):
        coeff = sum(mult*comb(n-shift+3,3) for shift,mult in ((0,1),(1,4),(2,1)) if n>=shift)
        assert coeff == (n+1)**3
    full = (1+4*q+q*q)/(1-q)**4
    for R in range(1,25):
        assert tail(q,R) == full-sum((F(m**3)*q**(m-1) for m in range(1,R)),F(0))
        assert tail(q,R)-tail(q,R+1) == R**3*q**(R-1)
    C = A*tail(q,16)/64
    assert C > 0
    strict_integer_upper = C.numerator//C.denominator+1
    assert C < strict_integer_upper
    print("SERIES PASS coefficients=0..32 exact_tail_identities_R=1..24")
    print(f"BOUND PASS C_quarter={C}")
    print(f"INTEGER_CEILING C_quarter<{strict_integer_upper}")


def main() -> None:
    A,q = arithmetic_audit()
    geometry_audit()
    periodization_audit()
    series_audit(A,q)
    print("AUDIT PASS; quarter_turn_single_cycle_Xi=UNIFORM; full_Xi=OPEN; P1=OPEN")


if __name__ == '__main__':
    main()
