#!/usr/bin/env python3
"""Prospectively frozen independent L1 audit; standard library, exact arithmetic."""
from fractions import Fraction as F
from itertools import product, permutations

Z = (0, 0, 0, 0)
E = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
A = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
B = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
CHART = ((0, 1, 0, 0), (0, 0, 1, -1), (1, -1, 0, -1), (0, 1, -2, 1))
UNCHART = ((2, -2, 1, -1), (1, 0, 0, 0), (1, -1, 0, -1), (1, -2, 0, -1))
L = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
V = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
INC = ((1, -1), (-1, 0), (0, 1), (0, 1))
K = ((6, 2, -1, 2), (2, 6, 2, -1), (-1, 2, 6, 2), (2, -1, 2, 6))
D = ((2, 0, -1, -1), (0, 2, 0, -1), (-1, 0, 2, 0), (-1, -1, 0, 2))
DINUM = ((6, 2, 3, 4), (2, 4, 1, 3), (3, 1, 4, 2), (4, 3, 2, 6))
BOUNDS = (3, 2, 2, 3)
J = (1, 0, 1, 0)
ROOT = (0, 1, 0, 0)
R = ((1, -2, 1, 0), Z, Z)
AM = ((1, 0, 0, 0), (0, -1, 0, 0), (0, -1, 1, 0))
ZM = (Z, Z, Z)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mv(m, v):
    return tuple(sum(x * y for x, y in zip(row, v)) for row in m)


def tr(m):
    return tuple(zip(*m))


def mm(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in tr(b)) for row in a)


def ma(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))


def scale(k, m):
    return tuple(tuple(k * x for x in row) for row in m)


def quadratic(m, a):
    return sum(x * y for x, y in zip(a, mv(m, a)))


def h(y):
    value = quadratic(B, y)
    assert value % 2 == 0
    return value // 2


def cyc(a, b):
    """Convolution in five cyclic positions, then subtract position four."""
    c = [0] * 5
    for i in range(4):
        for j in range(4):
            c[(i + j) % 5] += a[i] * b[j]
    return tuple(c[i] - c[4] for i in range(4))


def conjugate(a):
    c = [0] * 5
    for i, x in enumerate(a):
        c[(-i) % 5] += x
    return tuple(c[i] - c[4] for i in range(4))


def uv(a):
    a0, a1, a2, a3 = a
    t = a0 * a1 + a1 * a2 + a2 * a3
    return sum(x * x for x in a) - t, t - a0 * a2 - a0 * a3 - a1 * a3


def field_trace(a):
    return 4 * a[0] - sum(a[1:])


def s(a):
    return F(field_trace(cyc(a, conjugate(a))), 2)


def determinant(m):
    total = 0
    for p in permutations(range(len(m))):
        sign = (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
        value = sign
        for i, j in enumerate(p):
            value *= m[i][j]
        total += value
    return total


def multiplication_matrix(a):
    return tr(tuple(cyc(a, e) for e in E))


def gram(fun):
    """Complete coefficient extraction for a homogeneous quadratic form."""
    diag = tuple(fun(e) for e in E)
    return tuple(tuple(diag[i] if i == j else F(fun(add(E[i], E[j])) - diag[i] - diag[j], 2)
                       for j in range(4)) for i in range(4))


def universal():
    assert mm(CHART, UNCHART) == mm(UNCHART, CHART) == E
    assert mm(A, CHART) == mm(CHART, multiplication_matrix(ROOT))
    jf = ma(E, mm(A, A))
    assert mm(jf, CHART) == mm(CHART, multiplication_matrix(J))
    assert mm(mm(tr(A), B), A) == B
    a5 = E
    for _ in range(5):
        a5 = mm(A, a5)
    assert a5 == E
    assert mm(mm(tr(CHART), B), CHART) == D
    assert mm(D, DINUM) == scale(5, E)
    assert mm(L, V) == mm(V, L) == scale(5, E)
    assert mm(L, A) == mm(A, L)
    assert mm(mm(tr(L), B), L) == scale(5, B)
    U = gram(lambda a: uv(a)[0])
    W = gram(lambda a: uv(a)[1])
    for i in range(4):
        actual = gram(lambda a, k=i: cyc(a, conjugate(a))[k])
        assert actual == (U if i == 0 else scale(0, U) if i == 1 else scale(-1, W))
    assert ma(U, W) == scale(F(1, 2), D)
    assert gram(lambda a: h(mv(jf, mv(CHART, a)))) == U
    assert gram(s) == ma(scale(2, U), W)
    assert gram(lambda a: s(cyc(J, a))) == ma(scale(3, U), scale(-1, W))
    # Norm's quadratic matrix in (u,v), pulled back along (e0,e1)->(u,v).
    norm_form = ((1, F(1, 2)), (F(1, 2), -1))
    change = ((0, 1), (1, -1))
    assert mm(mm(tr(change), norm_form), change) == ((-1, F(3, 2)), (F(3, 2), -1))
    assert h((1, 0, 0, 1)) == 2 and h(mv(jf, (1, 0, 0, 1))) == 1
    assert 5 ** 4 > 16 * 31
    print("universal quadratic coefficients and chart matrices: PASS")


def decode(key):
    if not isinstance(key, tuple) or len(key) != 3:
        return None
    e0, e1, residue = key
    if type(e0) is not int or type(e1) is not int:
        return None
    if not isinstance(residue, tuple) or len(residue) != 4:
        return None
    if any(type(x) is not int or not 0 <= x < 5 for x in residue):
        return None
    if not 0 <= e0 <= 5 or not 0 <= e1 <= 13:
        return None
    candidates = []
    lifts = [tuple(x for x in range(-bound, bound + 1) if x % 5 == r)
             for bound, r in zip(BOUNDS, residue)]
    for a in product(*lifts):
        u, v = uv(a)
        if (u + v, u) == (e0, e1):
            candidates.append((a, mv(CHART, a)))
    assert len(candidates) <= 1, ("inverse collision", key, candidates)
    return candidates[0] if candidates else None


def census():
    oracle = {}
    shells = [0] * 6
    norms = []
    seeds = []
    count = 0
    jf = ma(E, mm(A, A))
    for a in product(*(range(-b, b + 1) for b in BOUNDS)):
        count += 1
        y = mv(CHART, a)
        e0, e1 = h(y), h(mv(jf, y))
        u, v = uv(a)
        norm = determinant(multiplication_matrix(a))
        assert norm == u * u + u * v - v * v == -e0 * e0 + 3 * e0 * e1 - e1 * e1
        assert (e0, e1) == (u + v, u)
        if e0 <= 5:
            key = (e0, e1, tuple(x % 5 for x in a))
            assert key not in oracle
            oracle[key] = (a, y)
            assert decode(key) == (a, y)
            shells[e0] += 1
            norms.append(norm)
            if e0 == 1:
                seeds.append(y)
    assert count == 1225
    assert len(oracle) == 291 and shells == [1, 20, 30, 60, 60, 120]
    assert max(norms) == 31
    print("complete coefficient box:", count, "states:", len(oracle), "shells:", *shells, "max_norm:", max(norms))
    return oracle, seeds


def inverse_audit(oracle):
    count = 0
    for e0 in range(-2, 8):
        for e1 in range(-2, 16):
            for r in product(range(5), repeat=4):
                key = (e0, e1, r)
                assert decode(key) == oracle.get(key), key
                count += 1
    huge = 10 ** 100
    for e0 in (-huge, -1, 0, 1, 5, 6, huge):
        for e1 in (-huge, -1, 0, 1, 13, 14, huge):
            for r in product(range(5), repeat=4):
                key = (e0, e1, r)
                assert decode(key) == oracle.get(key), key
                count += 1
    bad = [None, False, 0, "", {}, [], (), (0,), (0, 0), (0, 0, Z, 0), [0, 0, Z]]
    for bad_value in (None, True, False, "0", F(0), (), [], {}):
        bad.extend(((bad_value, 0, Z), (0, bad_value, Z), (0, 0, bad_value)))
        for i in range(4):
            r = list(Z)
            r[i] = bad_value
            bad.append((0, 0, tuple(r)))
    for r in ((), (0,), (0, 0, 0), (0, 0, 0, 0, 0), [0, 0, 0, 0], (-1, 0, 0, 0), (5, 0, 0, 0)):
        bad.append((0, 0, r))
    for key in bad:
        assert decode(key) is None, repr(key)
    assert decode((1, 1, E[0])) == (E[0], mv(CHART, E[0]))
    assert decode((1, 1, E[1])) == (E[1], mv(CHART, E[1]))
    print("inverse typed keys:", count, "malformed:", len(bad), "PASS")


def context_audit():
    ell = cyc((1, -1, 0, 0), (1, 0, -1, 0))
    second = cyc(ROOT, ell)
    assert ell == (1, -1, -1, 1) and second == (-1, 0, -2, -2)
    w1 = (0, 0, 1, 0)
    w2 = mv(A, w1)
    assert w2 == (1, 0, -1, 1)
    assert mv(UNCHART, mv(L, w1)) == ell
    assert mv(UNCHART, mv(L, w2)) == second
    ratios = []
    observations = []
    for a in (ell, second):
        assert all(-2 <= x <= 2 for x in a)
        trace = field_trace(cyc(a, conjugate(a)))
        ratios.append(F(sum(a) ** 2, 4 * trace))
        observations.append((h(mv(CHART, a)), uv(a)[0], s(a), s(cyc(J, a))))
    assert observations == [(5, 5, 10, 15)] * 2
    assert ratios == [F(0), F(5, 16)]
    print("fixed B0 and LOW: ell=0 jell=5/16 equal_energy_trace_data: PASS")


def pfield(y):
    a, b, c, d = y
    return (a - b, -a, b, b, c, d)


def static(u, v):
    return (u, u, v, u - v, 0, 0)


def split(z):
    e0, e1, e2, e3, c, d = z
    nums = (2 * e0 - 3 * e1 + e2 + e3, -e0 - e1 + 2 * e2 + 2 * e3,
            2 * e0 + 2 * e1 + e2 + e3, e0 + e1 + 3 * e2 - 2 * e3)
    if any(x % 5 for x in nums):
        return None
    a, b, u, v = (x // 5 for x in nums)
    return (a, b, c, d), (u, v)


def cell(m=ZM, z=(0,) * 6, r=0, b=ZM):
    return (m, b, z, r)


def local(c):
    m, b, z, r = c
    if m not in (R, AM):
        return c, "matter"
    parts = split(z)
    if parts is None:
        return c, "split"
    y, sigma = parts
    if m == R:
        if (y[0] + 2 * y[1]) % 5:
            return c, "image0"
        if (y[2] + 2 * y[3]) % 5:
            return c, "image1"
        xnum = mv(V, y)
        assert all(v % 5 == 0 for v in xnum)
        x = tuple(v // 5 for v in xnum)
        newr = r + 4 * h(x) - 2
        newy = x
        newm = AM
    else:
        newr = r + 2 - 4 * h(y)
        newy = mv(L, y)
        newm = R
    if newr < 0:
        return c, "unfunded_R" if m == R else "unfunded_AM"
    return cell(newm, add(pfield(newy), static(*sigma)), newr, b), "R_to_AM" if m == R else "AM_to_R"


def fcell(c):
    m, b, z, r = c
    electric, magnetic = z[:4], z[4:]
    e = add(electric, mv(INC, magnetic))
    mag = tuple(x - y for x, y in zip(magnetic, mv(tr(INC), e)))
    return cell(m, e + mag, r, b)


def energy_cell(c):
    m, b, z, r = c
    e, mag = z[:4], z[4:]
    return (sum(quadratic(K, a) for a in m + b) + sum(x * x for x in z)
            + sum(x * y for x, y in zip(e, mv(INC, mag))) + r)


def flatten(c):
    m, b, z, r = c
    result = tuple(x for v in m + b for x in v) + z + (r,)
    assert len(result) == 31
    return result


def fixed_context_cells():
    w = (0, 0, 1, 0)
    spectator = ((1, 2, 3, 4), (0, -1, 2, 0), (1, 0, 0, -1))
    sig = static(2, -1)
    rejected = [
        (cell(ZM, sig, 7, spectator), "matter"),
        (cell((R[1], R[0], R[2]), sig, 7, spectator), "matter"),
        (cell(R, (1, 0, 0, 0, 0, 0), 7, spectator), "split"),
        (cell(R, add(pfield((1, 0, 0, 0)), sig), 7, spectator), "image0"),
        (cell(R, add(pfield((0, 0, 1, 0)), sig), 7, spectator), "image1"),
        (cell(R, sig, 1, spectator), "unfunded_R"),
        (cell(AM, add(pfield(w), sig), 1, spectator), "unfunded_AM"),
    ]
    for c, reason in rejected:
        out, actual = local(c)
        assert out == c and actual == reason
    accepted = []
    for seed in (Z, w):
        hh = h(seed)
        for m in (R, AM):
            y = mv(L, seed) if m == R else seed
            funding = max(0, 2 - 4 * hh) if m == R else max(0, 4 * hh - 2)
            c = cell(m, add(pfield(y), sig), funding, spectator)
            out, reason = local(c)
            assert out != c and reason in ("R_to_AM", "AM_to_R")
            assert local(out)[0] == c and energy_cell(out) == energy_cell(c)
            accepted.append(c)
    print("local whole-input rejection fixtures:", len(rejected), "funded endpoint pairs:", len(accepted), "PASS")


def reduced_layer(state, layer):
    ms, mt, resources, channels, pointer = state
    rr, qq = list(resources), list(channels)
    if layer == 0:
        if ms == 0:
            ms, rr[0] = 1, rr[0] + 2
        elif rr[0] >= 2:
            ms, rr[0] = 0, rr[0] - 2
        if mt == 0 and rr[-1] >= 2:
            mt, rr[-1], pointer = 1, rr[-1] - 2, (pointer + 1) % 5
        elif mt == 1:
            mt, rr[-1] = 0, rr[-1] + 2
    elif layer == 1:
        rr[:-1], qq[:] = qq[:], rr[:-1]
    elif layer == 2:
        rr[1:], qq[:] = qq[:], rr[1:]
    return ms, mt, tuple(rr), tuple(qq), pointer


def trajectory(n, seed, coverage):
    cells = [cell() for _ in range(n)]
    cells[0] = cell(R, pfield(mv(L, seed)))
    cells[-1] = cell(R)
    channels = [0] * (n - 1)
    pointer, fcount = 0, 0
    reduced = (0, 0, (0,) * n, (0,) * (n - 1), 0)

    def snapshot():
        nonlocal reduced
        ms, mt, rr, qq, pp = reduced
        assert (cells[0][0], cells[-1][0]) == ((R, AM)[ms], (R, AM)[mt])
        assert tuple(c[3] for c in cells) == rr and tuple(channels) == qq and pointer == pp
        phase = seed
        for _ in range(fcount % 5):
            phase = mv(A, phase)
        expected = mv(L, phase) if ms == 0 else phase
        assert cells[0][2] == pfield(expected)
        assert all(c[1] == ZM for c in cells)
        assert all(c[2] == (0,) * 6 for c in cells[1:])
        assert all(c[0] == ZM for c in cells[1:-1])
        assert sum(energy_cell(c) for c in cells) + sum(channels) + 1 == 42
        assert sum(rr) + sum(qq) + 2 * (1 - ms) + 2 * mt == 2
        assert all(x in (0, 2) for x in rr + qq)
        source = flatten(cells[0])
        # Every stored coordinate except the source's six raw entries.
        return source[:24] + source[30:] + tuple(x for c in cells[1:] for x in flatten(c)) + tuple(channels) + (pointer,)

    history = [snapshot()]
    for _ in range(160):
        for layer in range(4):
            if layer == 0:
                for i, c in enumerate(cells):
                    out, branch = local(c)
                    if i in (0, n - 1):
                        coverage.add(("source" if i == 0 else "receiver", branch))
                    if i == n - 1 and branch == "R_to_AM":
                        if pointer == 4:
                            coverage.add(("receiver", "pointer_wrap"))
                        pointer = (pointer + 1) % 5
                    cells[i] = out
            elif layer in (1, 2):
                for j in range(n - 1):
                    i = j if layer == 1 else j + 1
                    m, b, z, r = cells[i]
                    cells[i] = cell(m, z, channels[j], b)
                    channels[j] = r
            else:
                cells = [fcell(c) for c in cells]
                fcount += 1
            reduced = reduced_layer(reduced, layer)
            history.append(snapshot())
    return history


def chain_audit(seeds):
    assert len(seeds) == 20
    coverage = set()
    comparisons = 0
    for n in range(2, 8):
        reference = trajectory(n, (0, 0, 1, 0), coverage)
        for seed in seeds:
            actual = trajectory(n, seed, coverage)
            assert actual == reference, (n, seed)
            comparisons += len(actual)
    required = {("source", "R_to_AM"), ("source", "AM_to_R"), ("source", "unfunded_AM"),
                ("receiver", "R_to_AM"), ("receiver", "AM_to_R"), ("receiver", "unfunded_R"),
                ("receiver", "pointer_wrap")}
    assert required <= coverage, sorted(required - coverage)
    print("raw chain N=2..7 steps=160 unit_seeds=20 compared_boundaries:", comparisons)
    print("chain coverage:", "; ".join(a + ":" + b for a, b in sorted(coverage)))


def main():
    universal()
    oracle, seeds = census()
    inverse_audit(oracle)
    context_audit()
    fixed_context_cells()
    chain_audit(seeds)
    print("INDEPENDENT FINITE AUDIT PASS; universal conclusions rest on DERIVATION.md")


if __name__ == "__main__":
    main()
