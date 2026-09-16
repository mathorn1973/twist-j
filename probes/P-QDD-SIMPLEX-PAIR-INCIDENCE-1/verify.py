#!/usr/bin/env python3
"""Exact audit for P-QDD-SIMPLEX-PAIR-INCIDENCE-1.

Standard library only. Universal conclusions are proved in PROOF.md.
This program audits frozen exact consequences and controls.
"""
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
    coeff = F(N, N - 1) * dot(u, y)
    return tuple(coeff * a for a in u)


def rational_relation(
    N: int, k: int, beta: tuple[int, ...], z: tuple[int, ...]
) -> tuple[F, ...]:
    out = [F(0) for _ in range(N)]
    for i, b in enumerate(beta):
        u = uvec(N, b)
        for r in range(N):
            out[r] += z[i] * u[r]
    return tuple(out)


def integer_lift(
    N: int, k: int, beta: tuple[int, ...], z: tuple[int, ...]
) -> tuple[int, ...]:
    s = sum(z)
    U = N * (N - 1)
    out = [-(N - 1) * s for _ in range(N)]
    for i, b in enumerate(beta):
        out[b] += U * z[i]
    return tuple(out)


def ints(v) -> tuple[int, ...]:
    out = []
    for a in v:
        x = F(a)
        require(x.denominator == 1, "integrality")
        out.append(x.numerator)
    return tuple(out)


def counts(N: int, z: tuple[int, ...]) -> tuple[int, int, int, int, int]:
    s = sum(z)
    S2 = sum(a * a for a in z)
    diff2 = sum(
        (z[i] - z[j]) ** 2 for i, j in combinations(range(N - 1), 2)
    )
    A = s * s
    B = N * diff2
    D = A + B
    return s, S2, A, B, D


def audit_context(
    N: int,
    k: int,
    beta: tuple[int, ...],
    z: tuple[int, ...],
    public_p5: bool = False,
) -> None:
    global CONTEXTS
    CONTEXTS += 1
    U = N * (N - 1)
    s, S2, A, B, D = counts(N, z)

    require(len(beta) == N - 1, "beta arity")
    require(set(beta) == set(range(N)) - {k}, "beta complement")
    diff2 = sum(
        (z[i] - z[j]) ** 2 for i, j in combinations(range(N - 1), 2)
    )
    require(diff2 == (N - 1) * S2 - s * s, "difference identity")
    require(D == (N - 1) * (N * S2 - s * s), "D closed form")

    x = rational_relation(N, k, beta, z)
    require(sum(x, F(0)) == 0, "rational relation sum zero")
    X = integer_lift(N, k, beta, z)
    require(sum(X) == 0, "integer lift sum zero")
    require(tuple(U * a for a in x) == tuple(F(a) for a in X), "lift equality")

    for i, b in enumerate(beta):
        require(X[b] - X[k] == U * z[i], "source recovery")

    Px_f = low_project(N, k, x)
    Qx_f = tuple(x[r] - Px_f[r] for r in range(N))
    PX_f = low_project(N, k, X)
    QX_f = tuple(F(X[r]) - PX_f[r] for r in range(N))
    PX = ints(PX_f)
    QX = ints(QX_f)

    a = avec(N, k)
    require(PX == tuple(-s * t for t in a), "integer low branch")
    require(
        tuple(PX[r] + QX[r] for r in range(N)) == X,
        "integer branch reconstruction",
    )
    require(dot(PX, QX) == 0, "branch orthogonality")

    require(norm(Px_f) == F(A, U), "LOW rational norm")
    require(norm(Qx_f) == F(B, U), "HIGH rational norm")
    require(norm(x) == F(D, U), "total rational norm")
    require(norm(PX) == U * A, "LOW integer norm")
    require(norm(QX) == U * B, "HIGH integer norm")
    require(norm(X) == U * D, "total integer norm")

    if any(z):
        require(D > 0, "nonzero total count")
        require(norm(Px_f) / norm(x) == F(A, D), "LOW normalized ratio")
        require(norm(Qx_f) / norm(x) == F(B, D), "HIGH normalized ratio")
    else:
        require(D == 0 and norm(x) == 0, "zero boundary")

    if s == 0:
        require(A == 0 and all(v == 0 for v in PX), "zero-sum LOW boundary")
    if len(set(z)) <= 1:
        require(B == 0 and all(v == 0 for v in QX), "all-equal HIGH boundary")
    elif B == 0:
        raise AssertionError("HIGH zero outside all-equal source")

    if public_p5:
        require(N == 5, "public N")
        require(B == 5 * (4 * S2 - s * s), "public B")
        require(D == 4 * (5 * S2 - s * s), "public D")
        require(norm(Px_f) == F(A, 20), "public LOW")
        require(norm(Qx_f) == F(B, 20), "public HIGH")
        require(norm(x) == F(D, 20), "public total")


def primitive_low_scales() -> None:
    checks = 0
    for N in range(2, 33):
        U = N * (N - 1)
        for k in range(N):
            a = avec(N, k)
            g = 0
            for v in a:
                g = gcd(g, abs(v))
            require(g == 1, "primitive low ray")
            require(norm(a) == U, "primitive low norm")
            if N <= 10:
                samples = range(1, U)
            else:
                samples = sorted({1, N - 1, N, U // 2, U - 1})
            for M in samples:
                if not 0 < M < U:
                    continue
                require(
                    any(F(-M * v, U).denominator != 1 for v in a),
                    "lift minimality",
                )
                checks += 1
    print(f"PRIMITIVE N=2..32 minimality_checks={checks} PASS")


def uniform_small() -> None:
    total = 0
    for N in range(2, 9):
        for k in range(N):
            beta = tuple(r for r in range(N) if r != k)
            for z in product((-1, 0, 1), repeat=N - 1):
                audit_context(N, k, beta, z)
                total += 1
    print(f"UNIFORM N=2..8 contexts={total} PASS")


def qdd_all_betas() -> None:
    N = 5
    total = 0
    for k in range(N):
        comp = tuple(r for r in range(N) if r != k)
        for beta in permutations(comp):
            for z in product(range(-2, 3), repeat=4):
                audit_context(N, k, beta, z, public_p5=True)
                total += 1
    print(
        f"QDD_ALL_BETAS contexts={total} sources=625 settings=5 betas=24 PASS"
    )


def qdd_extended() -> None:
    N = 5
    total = 0
    for k in range(N):
        beta = tuple(r for r in range(N) if r != k)
        for z in product(range(-4, 5), repeat=4):
            audit_context(N, k, beta, z, public_p5=True)
            total += 1
    print(f"QDD_EXTENDED contexts={total} source_box=-4..4 PASS")


def direct_pair_sets() -> None:
    N = 5
    k = 2
    beta = (0, 1, 3, 4)
    total_low = 0
    total_high = 0
    sources = 0
    for z in product(range(-2, 3), repeat=4):
        s, _, A, B, _ = counts(N, z)
        low = sum(1 for _a in range(abs(s)) for _b in range(abs(s)))
        high = sum(
            1
            for _c in range(N)
            for i, j in combinations(range(4), 2)
            for _a in range(abs(z[i] - z[j]))
            for _b in range(abs(z[i] - z[j]))
        )
        require(low == A, "direct LOW pair cardinality")
        require(high == B, "direct HIGH pair cardinality")
        audit_context(N, k, beta, z, public_p5=True)
        total_low += low
        total_high += high
        sources += 1
    print(
        f"PAIR_SETS public_context sources={sources} "
        f"low_total={total_low} high_total={total_high} PASS"
    )


def public_witnesses() -> None:
    N = 5
    k = 2
    beta = (0, 1, 3, 4)
    witnesses = (
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (1, -1, 0, 0),
        (1, 1, 1, 1),
        (2, -1, 1, 0),
    )
    for z in witnesses:
        audit_context(N, k, beta, z, public_p5=True)
    print("BOUNDARIES zero zero_sum all_equal mixed PASS")


def main() -> int:
    primitive_low_scales()
    uniform_small()
    qdd_all_betas()
    qdd_extended()
    direct_pair_sets()
    public_witnesses()
    print(f"PASS exact_assertions={COUNT} contexts={CONTEXTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
