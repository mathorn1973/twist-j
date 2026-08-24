#!/usr/bin/env python3
"""Exact audit for C-QDD-DIRECT-QUADRATIC-LINEARIZATION-1-N.

NON-CANONICAL incubation. Standard library only. Fractions throughout.
The direct branch is implemented in Q(zeta_5) from multiplication, conjugation,
field trace, the public B0 basis and the frozen LOW line. The factor formulas
are reconstructed afterwards by rational-linear interpolation on q(v)=vv^T.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from typing import Iterable, Sequence

N = 4
PAIRS = tuple((i, j) for i in range(N) for j in range(i, N))
LIFT = (-2, -1, 0, 1, 2)

Vec = tuple[F, F, F, F]
Mat = tuple[tuple[F, ...], ...]


def q(x: int | F) -> F:
    return x if isinstance(x, F) else F(x)


def vadd(a: Sequence[F], b: Sequence[F]) -> tuple[F, ...]:
    return tuple(x + y for x, y in zip(a, b))


def vscale(c: F, a: Sequence[F]) -> tuple[F, ...]:
    return tuple(c * x for x in a)


def mat(rows: Iterable[Iterable[int | F]]) -> Mat:
    return tuple(tuple(q(x) for x in row) for row in rows)


def eye(n: int) -> Mat:
    return tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))


def madd(a: Mat, b: Mat) -> Mat:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def msub(a: Mat, b: Mat) -> Mat:
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def mscale(c: F, a: Mat) -> Mat:
    return tuple(tuple(c * x for x in row) for row in a)


def mmul(a: Mat, b: Mat) -> Mat:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0])))
        for i in range(len(a))
    )


def mtranspose(a: Mat) -> Mat:
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def mtrace(a: Mat) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def outer(v: Sequence[F], w: Sequence[F]) -> Mat:
    return tuple(tuple(v[i] * w[j] for j in range(len(w))) for i in range(len(v)))


def minv(a: Mat) -> Mat:
    n = len(a)
    aug = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            c = aug[r][col]
            if c:
                aug[r] = [x - c * y for x, y in zip(aug[r], aug[col])]
    return tuple(tuple(row[n:]) for row in aug)


def rank(rows: Sequence[Sequence[F]]) -> int:
    if not rows:
        return 0
    a = [list(row) for row in rows]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def solve_square(a: Sequence[Sequence[F]], b: Sequence[F]) -> tuple[F, ...]:
    n = len(a)
    if any(len(row) != n for row in a) or len(b) != n:
        raise ValueError("square system required")
    aug = [list(a[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular interpolation matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            c = aug[r][col]
            if c:
                aug[r] = [x - c * y for x, y in zip(aug[r], aug[col])]
    return tuple(aug[i][-1] for i in range(n))


# Q(zeta_5) in basis B0=(1,z,z^2,z^3). z^4=-(1+z+z^2+z^3).
ZERO: Vec = (F(0), F(0), F(0), F(0))
BASIS: tuple[Vec, ...] = tuple(
    tuple(F(int(i == j)) for i in range(N))  # type: ignore[misc]
    for j in range(N)
)
POWER: tuple[Vec, ...] = BASIS + ((F(-1), F(-1), F(-1), F(-1)),)


def kmul(a: Sequence[F], b: Sequence[F]) -> Vec:
    out = [F(0)] * N
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if ai == 0 or bj == 0:
                continue
            p = POWER[(i + j) % 5]
            for k in range(N):
                out[k] += ai * bj * p[k]
    return tuple(out)  # type: ignore[return-value]


def kconj(a: Sequence[F]) -> Vec:
    out = [F(0)] * N
    for i, ai in enumerate(a):
        p = POWER[(-i) % 5]
        for k in range(N):
            out[k] += ai * p[k]
    return tuple(out)  # type: ignore[return-value]


def ktrace(a: Sequence[F]) -> F:
    # Trace of multiplication by a, computed from the regular matrix.
    columns = [kmul(a, e) for e in BASIS]
    return sum((columns[j][j] for j in range(N)), F(0))


def pairing(a: Sequence[F], b: Sequence[F]) -> F:
    return ktrace(kmul(a, kconj(b))) / 5


LAMBDA: Vec = (F(1), F(1), F(1), F(1))
LAMBDA_NORM = pairing(LAMBDA, LAMBDA)


def direct_raw(v: Sequence[int | F]) -> tuple[F, F, F, Mat]:
    w: Vec = tuple(q(x) for x in v)  # B0 coordinates
    m = pairing(w, w)
    c = pairing(w, LAMBDA) / LAMBDA_NORM
    low = vscale(c, LAMBDA)
    high = tuple(w[i] - low[i] for i in range(N))
    lo = pairing(low, low)
    hi = pairing(high, high)
    # Matrix of T_w(x)=w<x,w> in B0; construct columns directly.
    cols = [vscale(pairing(BASIS[j], w), w) for j in range(N)]
    t = tuple(tuple(cols[j][i] for j in range(N)) for i in range(N))
    return m, lo, hi, t


def sym_features(a: Mat) -> tuple[F, ...]:
    return tuple(a[i][j] for i, j in PAIRS)


def qmat(v: Sequence[int | F]) -> Mat:
    vf = tuple(q(x) for x in v)
    return outer(vf, vf)


def functional_matrix(coeff: Sequence[F]) -> Mat:
    out = [[F(0) for _ in range(N)] for _ in range(N)]
    for c, (i, j) in zip(coeff, PAIRS):
        if i == j:
            out[i][j] = c
        else:
            out[i][j] = out[j][i] = c / 2
    return tuple(tuple(row) for row in out)


def apply_coeff(coeff: Sequence[F], a: Mat) -> F:
    return sum((c * x for c, x in zip(coeff, sym_features(a))), F(0))


def apply_linear_matrix(coeffs: Sequence[Sequence[F]], a: Mat) -> Mat:
    vals = [apply_coeff(c, a) for c in coeffs]
    return tuple(tuple(vals[N * i + j] for j in range(N)) for i in range(N))


def expected_map_on_basis(g: Mat, a: Mat) -> Mat:
    return mmul(a, g)


def fmt(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_flat(a: Mat) -> str:
    return "[" + ";".join(",".join(fmt(x) for x in row) for row in a) + "]"


def main() -> None:
    # Deterministic interpolation basis: e_i and e_i+e_j.
    samples: list[tuple[int, int, int, int]] = []
    for i in range(N):
        v = [0] * N
        v[i] = 1
        samples.append(tuple(v))
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N
            v[i] = v[j] = 1
            samples.append(tuple(v))

    sample_x = [sym_features(qmat(v)) for v in samples]
    sample_rank = rank(sample_x)
    all_v = list(product(LIFT, repeat=N))
    all_x = [sym_features(qmat(v)) for v in all_v]
    all_rank = rank(all_x)

    direct_samples = [direct_raw(v) for v in samples]
    m_coeff = solve_square(sample_x, [r[0] for r in direct_samples])
    l_coeff = solve_square(sample_x, [r[1] for r in direct_samples])
    h_coeff = solve_square(sample_x, [r[2] for r in direct_samples])
    n_coeffs = []
    for i in range(N):
        for j in range(N):
            n_coeffs.append(solve_square(sample_x, [r[3][i][j] for r in direct_samples]))

    one = tuple(F(1) for _ in range(N))
    jmat = outer(one, one)
    ident = eye(N)
    g = msub(ident, mscale(F(1, 5), jmat))
    e_low = mscale(F(1, 4), jmat)
    e_high = msub(ident, e_low)
    h_low = mmul(g, e_low)
    h_high = mmul(g, e_high)

    assert sample_rank == 10
    assert all_rank == 10
    assert functional_matrix(m_coeff) == g
    assert functional_matrix(l_coeff) == h_low
    assert functional_matrix(h_coeff) == h_high

    # Compare the recovered matrix-valued map with A -> A G on a basis of S.
    sym_basis: list[Mat] = []
    for i, j in PAIRS:
        a = [[F(0) for _ in range(N)] for _ in range(N)]
        a[i][j] = F(1)
        a[j][i] = F(1)
        if i == j:
            a[i][j] = F(1)
        sym_basis.append(tuple(tuple(row) for row in a))
    for a in sym_basis:
        assert apply_linear_matrix(n_coeffs, a) == expected_map_on_basis(g, a)

    mismatch = 0
    positive_nonzero = True
    carrier: dict[tuple[F, ...], list[tuple[int, ...]]] = defaultdict(list)
    for v in all_v:
        a = qmat(v)
        raw = direct_raw(v)
        got = (
            apply_coeff(m_coeff, a),
            apply_coeff(l_coeff, a),
            apply_coeff(h_coeff, a),
            apply_linear_matrix(n_coeffs, a),
        )
        if got != raw:
            mismatch += 1
        if any(v) and got[0] <= 0:
            positive_nonzero = False
        carrier[sym_features(a)].append(v)

    assert mismatch == 0
    assert positive_nonzero
    assert len(carrier) == 313
    piston_fibres = Counter(len(xs) for xs in carrier.values())
    assert piston_fibres == Counter({2: 312, 1: 1})
    orbit_fibres = Counter({25 * k: n for k, n in piston_fibres.items()})
    assert orbit_fibres == Counter({50: 312, 25: 1})

    g_inv = minv(g)
    e_low_rec_left = mmul(g_inv, functional_matrix(l_coeff))
    e_low_rec_right = mmul(functional_matrix(l_coeff), g_inv)
    assert e_low_rec_left == e_low
    assert e_low_rec_right == e_low
    assert mmul(e_low, e_low) == e_low
    assert mmul(e_high, e_high) == e_high
    assert mmul(e_low, e_high) == mscale(F(0), ident)
    assert madd(e_low, e_high) == ident
    assert mmul(mtranspose(e_low), g) == mmul(g, e_low)
    assert mmul(mtranspose(e_high), g) == mmul(g, e_high)

    # Direct normalized records reconstructed from Lambda on every carrier class.
    normalized_mismatch = 0
    for feat, preimages in carrier.items():
        v = preimages[0]
        a = qmat(v)
        m0, l0, h0, n0 = direct_raw(v)
        m1 = apply_coeff(m_coeff, a)
        l1 = apply_coeff(l_coeff, a)
        h1 = apply_coeff(h_coeff, a)
        n1 = apply_linear_matrix(n_coeffs, a)
        if m1 == 0:
            if any(x != 0 for x in feat):
                normalized_mismatch += 1
        else:
            density0 = mscale(F(1, 1) / m0, n0)
            density1 = mscale(F(1, 1) / m1, n1)
            if (density0, (l0 / m0, h0 / m0)) != (density1, (l1 / m1, h1 / m1)):
                normalized_mismatch += 1
    assert normalized_mismatch == 0

    print("C-QDD-DIRECT-QUADRATIC-LINEARIZATION-1-N")
    print("STATUS NON-CANONICAL INCUBATION")
    print(f"T1 SPAN_RANK sample={sample_rank} full={all_rank} PASS")
    print("T2 UNIQUE_RATIONAL_LINEAR_EXTENSION nullity=0 PASS")
    print(f"T3 G {matrix_flat(g)}")
    print(f"T3 E_LOW {matrix_flat(e_low)}")
    print(f"T3 E_HIGH {matrix_flat(e_high)}")
    print(f"T3 FULL_CARRIER_MISMATCHES {mismatch} PASS")
    print("T4 EFFECT_RECONSTRUCTION idempotent=1 orthogonal=1 complete=1 G_self_adjoint=1 PASS")
    print(f"T5 NONZERO_POSITIVITY {int(positive_nonzero)} NORMALIZED_MISMATCHES {normalized_mismatch} PASS")
    print(f"T6 QCARRIER {len(carrier)} PISTON_FIBRES 1x1+312x2 ORBIT_FIBRES 1x25+312x50 PASS")
    print("GUARD direct_write_and_LOW_line_are_frozen_inputs; no Born/measure/apparatus/decoder-ownership/layer-lift")
    print("RESULT candidate-T")


if __name__ == "__main__":
    main()
