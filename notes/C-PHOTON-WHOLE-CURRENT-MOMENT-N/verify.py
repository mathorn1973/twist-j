#!/usr/bin/env python3
from __future__ import annotations

from itertools import product


def ell_of_source(B: tuple[int, ...]) -> int:
    assert sum(B) == 0
    L = len(B)
    H = [0] * L
    for r in range(1, L):
        H[r] = H[r - 1] + B[r]
    assert H[0] - H[-1] == B[0]
    hs = sorted(H)
    med = hs[(L - 1) // 2]
    return sum(abs(x - med) for x in H)


def audit_transport() -> int:
    tested = 0
    for L in range(2, 8):
        for B in product(range(-2, 3), repeat=L):
            if sum(B) != 0:
                continue
            n1 = sum(abs(x) for x in B)
            ell = ell_of_source(B)
            assert 4 * ell <= L * n1, (L, B, ell, n1)
            tested += 1
    return tested


def audit_sharpness() -> list[tuple[int, int, int]]:
    out = []
    for L in range(4, 22, 2):
        B = [0] * L
        B[0] = L
        B[L // 2] = -L
        ell = ell_of_source(tuple(B))
        M = 2 * L
        assert 8 * ell == M * M
        out.append((L, M, ell))
    return out


def audit_tail_identity() -> None:
    for M in range(1, 1001):
        rhs = sum(3 * r * r - 3 * r + 1 for r in range(1, M + 1))
        assert rhs == M**3


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    q = 2
    while q * q <= n:
        if n % q == 0:
            return False
        q += 1
    return True


def audit_cyclotomic_corollary() -> list[int]:
    hits = []
    for p in range(3, 102, 2):
        if not is_prime(p):
            continue
        D = p - 1
        if p == 2 * D - 3:
            hits.append(p)
    assert hits == [5]
    return hits


def main() -> int:
    tested = audit_transport()
    print(
        "PASS G3: exhaustive cyclic zero-sum sources "
        f"L=2..7, entries -2..2 ({tested} sources) satisfy "
        "4 ell <= L ||B||_1."
    )

    sharp = audit_sharpness()
    assert sharp[0] == (4, 8, 8)
    assert sharp[-1] == (20, 40, 200)
    print(
        "PASS G6: opposite winding-loop source saturates "
        "ell=M^2/8 for every even L=4..20."
    )

    audit_tail_identity()
    print("PASS G8: M^3 tail identity verified exactly for M=1..1000.")

    hits = audit_cyclotomic_corollary()
    print(
        "PASS G10: among odd primes p<=101, D=p-1 and p=2D-3 "
        f"intersect only at p={hits[0]}, D=4."
    )

    print("ALL PASS: whole-current moment audit complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
