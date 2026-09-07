#!/usr/bin/env python3
"""Exact audit for P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1.

Standard library only. Universal conclusions are proved in PROOF.md.
This program audits frozen exact consequences and controls.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm
from random import Random

COUNT = 0


def require(ok: bool, label: str) -> None:
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(label)


def unit3(a: F | int) -> tuple[int, int]:
    z = F(a)
    if not z:
        raise ValueError("valuation at zero is undefined")
    n, d = z.numerator, z.denominator
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    while d % 3 == 0:
        d //= 3
        k -= 1
    return k, (n * pow(d, -1, 3)) % 3


def h(a: F | int) -> int:
    k, u = unit3(a)
    if k % 2 == 0:
        return 0
    return 1 if u == 2 else -1


def dot(x, y) -> F:
    return sum((F(a) * F(b) for a, b in zip(x, y)), F(0))


def norm(x) -> F:
    return dot(x, x)


def weight(v, t: F = F(1, 4)) -> F:
    return F(1, 4) + t * h(norm(v))


def determinant(a) -> F:
    m = [[F(x) for x in row] for row in a]
    sign = F(1)
    n = len(m)
    out = F(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if m[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            sign = -sign
        p = m[k][k]
        out *= p
        for i in range(k + 1, n):
            f = m[i][k] / p
            for j in range(k + 1, n):
                m[i][j] -= f * m[k][j]
    return sign * out


def primitive(v) -> tuple[int, ...]:
    vals = [F(x) for x in v]
    den = lcm(*(x.denominator for x in vals))
    ints = [int(x * den) for x in vals]
    g = 0
    for x in ints:
        g = gcd(g, abs(x))
    if g == 0:
        raise ValueError("zero vector")
    ints = [x // g for x in ints]
    first = next(x for x in ints if x)
    if first < 0:
        ints = [-x for x in ints]
    return tuple(ints)


def projector(v):
    q = norm(v)
    return [[F(a) * F(b) / q for b in v] for a in v]


def verify_residue_identities() -> None:
    values = sorted({F(n, d) for n in range(-24, 25) if n for d in range(1, 9)})
    pair_count = 0
    scales = (F(-9, 2), F(1, 27), F(3, 5), F(2, 3))
    for a in values:
        require(h(a) == -h(-a), "sign covariance")
        for s in scales:
            require(h(a * s * s) == h(a), "square invariance")
        for b in values:
            if a + b == 0:
                continue
            require(
                (h(a) + h(b) - h(a + b) - h(a * b / (a + b))) % 4 == 0,
                "binary diagonal-change identity",
            )
            pair_count += 1
    print(f"RESIDUE exact_pairs={pair_count} rational_values={len(values)} PASS")


def gram_schmidt_frames() -> None:
    rng = Random(20260907)
    target = 2000
    good = 0
    attempts = 0
    odd_counts = Counter()
    while good < target:
        attempts += 1
        raw = []
        for _ in range(4):
            a = [rng.randint(-20, 20) for _ in range(4)]
            raw.append(tuple(F(x) for x in a + [-sum(a)]))
        ys = []
        for x in raw:
            v = list(x)
            for y in ys:
                c = dot(v, y) / norm(y)
                v = [u - c * z for u, z in zip(v, y)]
            if not norm(v):
                break
            ys.append(tuple(v))
        if len(ys) != 4:
            continue
        good += 1
        norms = [norm(v) for v in ys]
        require(all(dot(a, b) == 0 for a, b in combinations(ys, 2)), "orthogonality")
        # Coordinates in the A4 basis (e0-e4,...,e3-e4) are the first four entries.
        cmat = [[ys[j][i] for j in range(4)] for i in range(4)]
        d = determinant(cmat)
        require(d != 0, "frame determinant nonzero")
        require(norms[0] * norms[1] * norms[2] * norms[3] == 5 * d * d, "A4 discriminant")
        require(sum(h(q) for q in norms) % 4 == 0, "mod-four basis invariant")
        require(sum(h(q) for q in norms) == 0, "exact frame-null identity")
        require(sum(weight(v) for v in ys) == 1, "positive frame normalization")
        require(sum(weight(v, F(1, 8)) for v in ys) == 1, "strict-positive normalization")
        require(all(weight(v, F(1, 8)) in (F(1, 8), F(1, 4), F(3, 8)) for v in ys), "strict-positive range")
        require(all(weight(v) == weight(primitive(v)) for v in ys), "projective ray value")
        odd = sum(unit3(q)[0] % 2 for q in norms)
        odd_counts[odd] += 1
        require(odd in (0, 2), "odd valuation count")
        units = [unit3(q)[1] for q in norms]
        require((units[0] * units[1] * units[2] * units[3]) % 3 == 2, "A4 unit discriminant")
    print(
        f"A4_FRAMES count={good} attempts={attempts} "
        f"odd_valuation_counts={odd_counts[0]},{odd_counts[2]} PASS"
    )


def inner_cl4_rays() -> None:
    rays = set()
    # Norm 2 and 4 primitive A4 rays.
    for v in product(range(-1, 2), repeat=5):
        if sum(v) != 0 or not any(v):
            continue
        q = sum(x * x for x in v)
        if q not in (2, 4):
            continue
        rays.add(primitive(v))
    # Five simplex rays of norm 20.
    for k in range(5):
        v = [-1] * 5
        v[k] = 4
        rays.add(primitive(v))
    counts = Counter(int(norm(v)) for v in rays)
    require(counts == Counter({4: 15, 2: 10, 20: 5}), "inner Cl4 norm census")
    require(len(rays) == 30, "inner Cl4 ray count")
    require(all(h(norm(v)) == 0 for v in rays), "inner Cl4 H zero")
    require(all(weight(v, F(1, 8)) == F(1, 4) for v in rays), "inner Cl4 fixed weight")
    print("INNER_CL4 rays=30 norms=2:10,4:15,20:5 H=0 PASS")


def cover_witness() -> None:
    ds = [
        (2, -1, -1, 0, 0),
        (-1, 2, -1, 0, 0),
        (-1, -1, 2, 0, 0),
    ]
    rs = [
        (0, 1, -1, 0, 0),
        (1, 0, -1, 0, 0),
        (1, -1, 0, 0, 0),
    ]
    require([norm(v) for v in ds] == [6, 6, 6], "d norms")
    require([norm(v) for v in rs] == [2, 2, 2], "r norms")
    require([h(norm(v)) for v in ds] == [1, 1, 1], "d H")
    require([h(norm(v)) for v in rs] == [0, 0, 0], "r H")
    pd = [projector(v) for v in ds]
    pr = [projector(v) for v in rs]
    require(
        all(sum(m[i][j] for m in pd) == sum(m[i][j] for m in pr) for i in range(5) for j in range(5)),
        "equal projector cover",
    )
    for t in (F(-1, 4), F(-1, 8), F(0), F(1, 8), F(1, 4)):
        defect = sum(weight(v, t) for v in ds) - sum(weight(v, t) for v in rs)
        require(defect == 3 * t, "D=3t")
    print("COVER equal_projectors D=3t endpoint_D=3/4 strict_positive_D=3/8 PASS")


def outside_control() -> None:
    # Columns form an orthogonal norm-3 basis of standard determinant-one Q^4.
    qmat = [
        [1, -1, -1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, -1],
        [0, -1, 1, 1],
    ]
    cols = list(zip(*qmat))
    require(all(dot(a, b) == 0 for a, b in combinations(cols, 2)), "outside orthogonality")
    require([norm(v) for v in cols] == [3, 3, 3, 3], "outside norm")
    require(sum(h(norm(v)) for v in cols) == -4, "outside H sum")
    print("OUTSIDE_CONTROL standard_Q4 norm=3x4 sum_H=-4 PASS")


def main() -> int:
    verify_residue_identities()
    gram_schmidt_frames()
    inner_cl4_rays()
    cover_witness()
    outside_control()
    print(f"PASS exact_assertions={COUNT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
