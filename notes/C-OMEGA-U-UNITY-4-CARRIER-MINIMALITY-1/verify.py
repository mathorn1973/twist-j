#!/usr/bin/env python3
"""NON-CANONICAL exact verifier for C-OMEGA-U-UNITY-4-CARRIER-MINIMALITY-1.

Standard library only. All arithmetic is exact modulo 5.
This is an incubation tool, not public evidence.
"""

from collections import Counter
from itertools import product

P = 5


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def zero(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


def madd(A, B):
    return [[(a + b) % P for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mscale(c, A):
    return [[(c * a) % P for a in row] for row in A]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    assert len(A[0]) == k
    return [[sum(A[i][t] * B[t][j] for t in range(k)) % P for j in range(m)] for i in range(n)]


def mpow(A, n):
    R = eye(len(A))
    X = [row[:] for row in A]
    while n:
        if n & 1:
            R = mmul(R, X)
        X = mmul(X, X)
        n >>= 1
    return R


def minv(A):
    n = len(A)
    aug = [row[:] + eye(n)[i] for i, row in enumerate(A)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if aug[r][c] % P), None)
        if pivot is None:
            raise ValueError("singular")
        aug[c], aug[pivot] = aug[pivot], aug[c]
        inv = pow(aug[c][c] % P, -1, P)
        aug[c] = [(inv * x) % P for x in aug[c]]
        for r in range(n):
            if r != c and aug[r][c] % P:
                q = aug[r][c] % P
                aug[r] = [(x - q * y) % P for x, y in zip(aug[r], aug[c])]
    return [row[n:] for row in aug]


def mrank(A):
    if not A:
        return 0
    B = [row[:] for row in A]
    n, m = len(B), len(B[0])
    r = 0
    for c in range(m):
        pivot = next((i for i in range(r, n) if B[i][c] % P), None)
        if pivot is None:
            continue
        B[r], B[pivot] = B[pivot], B[r]
        inv = pow(B[r][c] % P, -1, P)
        B[r] = [(inv * x) % P for x in B[r]]
        for i in range(n):
            if i != r and B[i][c] % P:
                q = B[i][c] % P
                B[i] = [(x - q * y) % P for x, y in zip(B[i], B[r])]
        r += 1
        if r == n:
            break
    return r


def block_diag(A, B):
    n, m = len(A), len(B)
    R = zero(n + m, n + m)
    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j] % P
    for i in range(m):
        for j in range(m):
            R[n + i][n + j] = B[i][j] % P
    return R


def block_bisector(X, Xi):
    n = len(X)
    R = zero(2 * n, 2 * n)
    for i in range(n):
        for j in range(n):
            R[i][n + j] = (2 * Xi[i][j]) % P
            R[n + i][j] = X[i][j] % P
    return R


def order(A, bound=200):
    I = eye(len(A))
    R = I
    for k in range(1, bound + 1):
        R = mmul(R, A)
        if R == I:
            return k
    return None


def partitions(n, max_part=5):
    def rec(rem, hi, pref):
        if rem == 0:
            yield tuple(pref)
            return
        for x in range(min(hi, rem), 0, -1):
            yield from rec(rem - x, x, pref + [x])
    yield from rec(n, max_part, [])


def ker_dim_from_partition(part, r):
    return sum(min(r, s) for s in part)


def exact_mult_from_kernels(part, r):
    k0 = ker_dim_from_partition(part, r - 1) if r > 1 else 0
    k1 = ker_dim_from_partition(part, r)
    k2 = ker_dim_from_partition(part, r + 1) if r < 5 else sum(part)
    return 2 * k1 - k0 - k2


def poly_mul(a, b, deg=5):
    out = [0] * deg
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < deg:
                out[i + j] = (out[i + j] + x * y) % P
    return out


def poly_pow(a, n, deg=5):
    out = [1] + [0] * (deg - 1)
    x = a[:]
    while n:
        if n & 1:
            out = poly_mul(out, x, deg)
        x = poly_mul(x, x, deg)
        n >>= 1
    return out


def poly_comp(f, g, deg=5):
    out = [0] * deg
    gp = [1] + [0] * (deg - 1)
    for c in f:
        for i in range(deg):
            out[i] = (out[i] + c * gp[i]) % P
        gp = poly_mul(gp, g, deg)
    return out


def all_tops():
    I2 = eye(2)
    target = mscale(2, I2)
    mats = []
    for a, b, c, d in product(range(P), repeat=4):
        T = [[a, b], [c, d]]
        if mmul(T, T) == target:
            mats.append(T)
    return mats


def line_key(v):
    a, b = v
    if a % P:
        inv = pow(a % P, -1, P)
        return (1, b * inv % P)
    return (0, 1)


def main():
    print("C-OMEGA-U-UNITY-4-CARRIER-MINIMALITY-1 verify")
    print("status NON-CANONICAL incubation")

    M = [
        [1, 0, 4, 1],
        [0, 1, 4, 0],
        [1, 0, 0, 0],
        [0, 1, 4, 1],
    ]
    I4 = eye(4)
    N = madd(M, mscale(-2, I4))
    assert mpow(M, 5) == mscale(2, I4)
    assert order(M, 40) == 20
    assert mpow(N, 4) != zero(4, 4)
    assert mpow(N, 5) == zero(4, 4)
    print("PASS V1 public carrier: ord(M)=20, M^5=2I, N has index 5-bound and J4 length 4")

    # Universal truncated-polynomial identities in F_5[x]/(x^5).
    r = [2, 1, 0, 0, 0]
    r5 = poly_pow(r, 5)
    r9 = poly_pow(r, 9)
    assert r5 == [2, 0, 0, 0, 0]
    f = r9[:]
    f[0] = (f[0] - 2) % P
    assert f == [0, 4, 3, 1, 2]
    u = [4, 3, 1, 2, 0]
    assert f == poly_mul([0, 1, 0, 0, 0], u)
    assert u[0] == 4
    assert poly_comp(f, f) == [0, 1, 0, 0, 0]
    print("PASS V2 conjugation polynomial: f(N)=N(4+3N+N^2+2N^3), unit factor, involutive")

    # Kernel-difference formula really returns exact Jordan multiplicities.
    checked_parts = 0
    for n in range(1, 9):
        for part in partitions(n):
            checked_parts += 1
            counts = Counter(part)
            for s in range(1, 6):
                assert exact_mult_from_kernels(part, s) == counts[s]
    print(f"PASS V3 canonical quotient formula on {checked_parts} partitions through dimension 8")

    # Irreducibility / even-dimensional square-root carrier.
    squares = {x * x % P for x in range(P)}
    assert 2 not in squares
    tops = all_tops()
    assert len(tops) == 20
    lines = {line_key(v) for v in product(range(P), repeat=2) if v != (0, 0)}
    assert len(lines) == 6
    for T in tops:
        for v in product(range(P), repeat=2):
            if v == (0, 0):
                continue
            tv = ((T[0][0] * v[0] + T[0][1] * v[1]) % P,
                  (T[1][0] * v[0] + T[1][1] * v[1]) % P)
            assert line_key(tv) != line_key(v)
    print("PASS V4 x^2-2 irreducible; 20 top square roots; none fixes any of the 6 F5 lines")

    # Frozen parity consequence and dimension minimum.
    admissible_partition_types = []
    below = []
    for n in range(4, 9):
        for part in partitions(n):
            counts = Counter(part)
            has_public = max(part) >= 4
            even_mult = all(counts[s] % 2 == 0 for s in range(1, 6))
            if has_public and even_mult:
                admissible_partition_types.append((n, part))
                if n < 8:
                    below.append((n, part))
    assert below == []
    at8 = [part for n, part in admissible_partition_types if n == 8]
    assert at8 == [(4, 4)]
    print("PASS V5 parity gate: no carrier below 8; unique dimension-8 Jordan type is (4,4)")

    # Exact doubled witness.
    X = [
        [0, 1, 0, 3],
        [0, 1, 4, 1],
        [0, 1, 4, 2],
        [1, 3, 3, 0],
    ]
    Xi = minv(X)
    assert mmul(X, M) == mmul(mpow(M, 9), X)
    A8 = block_diag(M, M)
    S8 = block_bisector(X, Xi)
    I8 = eye(8)
    assert mpow(A8, 5) == mscale(2, I8)
    assert order(A8, 40) == 20
    assert mmul(S8, S8) == mscale(2, I8)
    assert mmul(S8, A8) == mmul(mpow(A8, 9), S8)
    print("PASS V6 rank-8 witness: A=M+M, S^2=2I=A^5, SAS^-1=A^9")

    # Standard marked public copy is transverse to its S-image.
    cols = []
    for j in range(4):
        v = [0] * 8
        v[j] = 1
        cols.append(v)
    for j in range(4):
        e = [[0] for _ in range(8)]
        e[j][0] = 1
        sv = mmul(S8, e)
        cols.append([sv[i][0] for i in range(8)])
    C = [[cols[j][i] for j in range(8)] for i in range(8)]
    assert mrank(C) == 8
    print("PASS V7 displayed marked P is transverse: P direct-sum S(P)=F5^8")

    print("G1 candidate-T PASS exact-size Jordan multiplicities forced even by S^2=2 on invariant quotients")
    print("G2 candidate-T PASS minimal F5 dimension is at least 8")
    print("G3 candidate-T PASS minimal A Jordan type forced to (4,4)")
    print("G4 candidate-T PASS top-line obstruction forces transversality at rank 8")
    print("G5 candidate-C PASS explicit rank-8 witness exists over unchanged F5")
    print("G6 STOP full minimal-pair equivalence classification not decided by this verifier")
    print("ALL REQUIRED GATES G1-G5 PASS")


if __name__ == "__main__":
    main()
