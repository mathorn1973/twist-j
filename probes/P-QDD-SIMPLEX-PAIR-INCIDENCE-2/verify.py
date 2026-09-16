#!/usr/bin/env python3
"""Exact audit for P-QDD-SIMPLEX-PAIR-INCIDENCE-2."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd

COUNT = 0
CONTEXTS = 0


def require(ok: bool, label: str) -> None:
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(label)


def dot(x, y) -> F:
    return sum((F(a) * F(b) for a, b in zip(x, y)), F(0))


def norm(x) -> F:
    return dot(x, x)


def uvec(N: int, k: int) -> tuple[F, ...]:
    return tuple(F(N - 1, N) if r == k else F(-1, N) for r in range(N))


def avec(N: int, k: int) -> tuple[int, ...]:
    return tuple(N - 1 if r == k else -1 for r in range(N))


def low_project(N: int, k: int, y) -> tuple[F, ...]:
    u = uvec(N, k)
    c = F(N, N - 1) * dot(u, y)
    return tuple(c * a for a in u)


def relation(N: int, beta: tuple[int, ...], z: tuple[int, ...]) -> tuple[F, ...]:
    out = [F(0) for _ in range(N)]
    for i, b in enumerate(beta):
        u = uvec(N, b)
        for r in range(N):
            out[r] += z[i] * u[r]
    return tuple(out)


def lift(N: int, k: int, beta: tuple[int, ...], z: tuple[int, ...]) -> tuple[int, ...]:
    s = sum(z)
    U = N * (N - 1)
    out = [-(N - 1) * s for _ in range(N)]
    for i, b in enumerate(beta):
        out[b] += U * z[i]
    return tuple(out)


def as_ints(v) -> tuple[int, ...]:
    out = []
    for a in v:
        x = F(a)
        require(x.denominator == 1, "integrality")
        out.append(x.numerator)
    return tuple(out)


def scalar_counts(N: int, z: tuple[int, ...]) -> tuple[int, int, int, int, int]:
    s = sum(z)
    S2 = sum(a * a for a in z)
    diff2 = sum((z[i] - z[j]) ** 2 for i, j in combinations(range(N - 1), 2))
    A = s * s
    B = N * diff2
    return s, S2, A, B, A + B


def audit_context(
    N: int, k: int, beta: tuple[int, ...], z: tuple[int, ...], public_p5: bool = False
) -> None:
    global CONTEXTS
    CONTEXTS += 1
    U = N * (N - 1)
    s, S2, A, B, D = scalar_counts(N, z)
    require(set(beta) == set(range(N)) - {k}, "beta complement")

    diff2 = sum((z[i] - z[j]) ** 2 for i, j in combinations(range(N - 1), 2))
    require(diff2 == (N - 1) * S2 - s * s, "difference identity")
    require(D == (N - 1) * (N * S2 - s * s), "D identity")

    x = relation(N, beta, z)
    X = lift(N, k, beta, z)
    require(sum(x, F(0)) == 0, "x sum")
    require(sum(X) == 0, "X sum")
    require(tuple(U * a for a in x) == tuple(F(a) for a in X), "lift")

    for i, b in enumerate(beta):
        require(X[b] - X[k] == U * z[i], "source recovery")

    Px = low_project(N, k, x)
    Qx = tuple(x[r] - Px[r] for r in range(N))
    PX = as_ints(low_project(N, k, X))
    QX = as_ints(tuple(F(X[r]) - F(PX[r]) for r in range(N)))

    a = avec(N, k)
    require(PX == tuple(-s * v for v in a), "P integer formula")
    require(tuple(PX[r] + QX[r] for r in range(N)) == X, "branch reconstruct")
    require(dot(PX, QX) == 0, "orthogonal")

    require(norm(Px) == F(A, U), "P rational norm")
    require(norm(Qx) == F(B, U), "Q rational norm")
    require(norm(x) == F(D, U), "total rational norm")
    require(norm(PX) == U * A, "P integer norm")
    require(norm(QX) == U * B, "Q integer norm")
    require(norm(X) == U * D, "total integer norm")

    if any(z):
        require(D > 0, "positive D")
        require(norm(Px) / norm(x) == F(A, D), "P ratio")
        require(norm(Qx) / norm(x) == F(B, D), "Q ratio")
    else:
        require(D == 0 and norm(x) == 0, "zero")

    if s == 0:
        require(A == 0 and all(v == 0 for v in PX), "zero sum LOW")
    if len(set(z)) <= 1:
        require(B == 0 and all(v == 0 for v in QX), "equal HIGH")
    else:
        require(B > 0, "non-equal HIGH positive")

    if public_p5:
        require(N == 5 and U == 20, "p5 scale")
        require(B == 5 * (4 * S2 - s * s), "p5 B")
        require(D == 4 * (5 * S2 - s * s), "p5 D")
        require(norm(Px) == F(A, 20), "p5 LOW")
        require(norm(Qx) == F(B, 20), "p5 HIGH")
        require(norm(x) == F(D, 20), "p5 total")


def primitive_scales() -> None:
    sampled = 0
    for N in range(2, 33):
        U = N * (N - 1)
        for k in range(N):
            a = avec(N, k)
            g = 0
            for v in a:
                g = gcd(g, abs(v))
            require(g == 1, "primitive")
            require(norm(a) == U, "primitive norm")
            require(all(F(-U * v, U).denominator == 1 for v in a), "U clears")
            for M in sorted({1, N - 1, N, U // 2, U - 1}):
                if 0 < M < U:
                    require(any(F(-M * v, U).denominator != 1 for v in a), "smaller fails")
                    sampled += 1
    print(f"PRIMITIVE N=2..32 sampled_smaller={sampled} PASS")


def source_witnesses(m: int) -> tuple[tuple[int, ...], ...]:
    raw = [
        (0,) * m,
        (1,) + (0,) * (m - 1),
        (-1,) + (0,) * (m - 1),
        (1,) * m,
        (-1,) * m,
        tuple(1 if i % 2 == 0 else -1 for i in range(m)),
        tuple(i - (m // 2) for i in range(m)),
    ]
    if m >= 2:
        raw += [
            (1, -1) + (0,) * (m - 2),
            (2, -1) + (0,) * (m - 2),
            (2, -2) + tuple(1 if i % 2 == 0 else -1 for i in range(m - 2)),
        ]
    seen = []
    for z in raw:
        if z not in seen:
            seen.append(z)
    return tuple(seen)


def uniform_audit() -> None:
    total = 0
    for N in range(2, 9):
        for k in range(N):
            beta = tuple(r for r in range(N) if r != k)
            for z in source_witnesses(N - 1):
                audit_context(N, k, beta, z)
                total += 1
    print(f"UNIFORM N=2..8 contexts={total} PASS")


def qdd_context_audit() -> None:
    fixed = (
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (-1, 0, 0, 0),
        (1, -1, 0, 0),
        (1, 1, 1, 1),
        (-1, -1, -1, -1),
        (2, -1, 1, 0),
        (2, 2, -1, -3),
        (3, -2, 0, 1),
        (4, -4, 2, -2),
    )
    total = 0
    N = 5
    for k in range(5):
        comp = tuple(r for r in range(5) if r != k)
        for beta in permutations(comp):
            for z in fixed:
                audit_context(N, k, beta, z, public_p5=True)
                total += 1
    print(f"QDD_CONTEXTS settings=5 betas=24 sources=10 contexts={total} PASS")


def qdd_bounded_audit() -> None:
    N, k, beta = 5, 2, (0, 1, 3, 4)
    total = 0
    for z in product(range(-2, 3), repeat=4):
        audit_context(N, k, beta, z, public_p5=True)
        total += 1
    print(f"QDD_BOUNDED public_context sources={total} PASS")


def qdd_extended_audit() -> None:
    total = 0
    N = 5
    for k in range(5):
        beta = tuple(r for r in range(5) if r != k)
        for z in product((-4, 0, 4), repeat=4):
            audit_context(N, k, beta, z, public_p5=True)
            total += 1
    print(f"QDD_EXTENDED contexts={total} source_alphabet=-4,0,4 PASS")


def direct_pair_audit() -> None:
    N = 5
    low_total = high_total = sources = 0
    for z in product(range(-2, 3), repeat=4):
        s, _, A, B, _ = scalar_counts(N, z)
        low = sum(1 for _a in range(abs(s)) for _b in range(abs(s)))
        high = sum(
            1
            for _c in range(N)
            for i, j in combinations(range(4), 2)
            for _a in range(abs(z[i] - z[j]))
            for _b in range(abs(z[i] - z[j]))
        )
        require(low == A, "LOW pair set")
        require(high == B, "HIGH pair set")
        low_total += low
        high_total += high
        sources += 1
    print(
        f"PAIR_SETS sources={sources} low_total={low_total} "
        f"high_total={high_total} PASS"
    )


def main() -> int:
    primitive_scales()
    uniform_audit()
    qdd_context_audit()
    qdd_bounded_audit()
    qdd_extended_audit()
    direct_pair_audit()
    print(f"PASS exact_assertions={COUNT} contexts={CONTEXTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
