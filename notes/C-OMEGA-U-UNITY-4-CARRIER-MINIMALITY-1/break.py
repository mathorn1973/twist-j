#!/usr/bin/env python3
"""NON-CANONICAL adversarial second implementation for carrier minimality.

Written and frozen before execution. Same-session breaker, not independent confirmation.
Standard library only; exact arithmetic modulo 5.
"""

from collections import Counter
from itertools import product

P = 5


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def zero(n, m):
    return [[0] * m for _ in range(n)]


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % P
             for j in range(len(B[0]))] for i in range(len(A))]


def mpow(A, n):
    R = eye(len(A))
    X = [r[:] for r in A]
    while n:
        if n & 1:
            R = mmul(R, X)
        X = mmul(X, X)
        n //= 2
    return R


def rank(A):
    if not A:
        return 0
    B = [[x % P for x in row] for row in A]
    n, m = len(B), len(B[0])
    r = 0
    for c in range(m):
        q = next((i for i in range(r, n) if B[i][c]), None)
        if q is None:
            continue
        B[r], B[q] = B[q], B[r]
        z = pow(B[r][c], -1, P)
        B[r] = [(z * x) % P for x in B[r]]
        for i in range(n):
            if i != r and B[i][c]:
                z = B[i][c]
                B[i] = [(x - z * y) % P for x, y in zip(B[i], B[r])]
        r += 1
    return r


def inv(A):
    n = len(A)
    I = eye(n)
    B = [A[i][:] + I[i] for i in range(n)]
    r = 0
    for c in range(n):
        q = next((i for i in range(r, n) if B[i][c] % P), None)
        if q is None:
            raise ValueError("singular")
        B[r], B[q] = B[q], B[r]
        z = pow(B[r][c] % P, -1, P)
        B[r] = [(z * x) % P for x in B[r]]
        for i in range(n):
            if i != r and B[i][c] % P:
                z = B[i][c] % P
                B[i] = [(x - z * y) % P for x, y in zip(B[i], B[r])]
        r += 1
    return [row[n:] for row in B]


def nullspace(A):
    B = [[x % P for x in row] for row in A]
    n, m = len(B), len(B[0])
    pivots = []
    r = 0
    for c in range(m):
        q = next((i for i in range(r, n) if B[i][c]), None)
        if q is None:
            continue
        B[r], B[q] = B[q], B[r]
        z = pow(B[r][c], -1, P)
        B[r] = [(z * x) % P for x in B[r]]
        for i in range(n):
            if i != r and B[i][c]:
                z = B[i][c]
                B[i] = [(x - z * y) % P for x, y in zip(B[i], B[r])]
        pivots.append(c)
        r += 1
        if r == n:
            break
    free = [c for c in range(m) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * m
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = (-B[i][f]) % P
        basis.append(v)
    return basis


def vec_to_mat(v, n=4):
    return [v[i*n:(i+1)*n] for i in range(n)]


def intertwiner_space(M, M9):
    eqs = []
    n = 4
    def ix(i, j):
        return i * n + j
    for i in range(n):
        for j in range(n):
            row = [0] * (n*n)
            for k in range(n):
                row[ix(i, k)] = (row[ix(i, k)] + M[k][j]) % P
                row[ix(k, j)] = (row[ix(k, j)] - M9[i][k]) % P
            eqs.append(row)
    return nullspace(eqs)


def lincomb(coeffs, basis):
    out = [0] * len(basis[0])
    for c, b in zip(coeffs, basis):
        for i, x in enumerate(b):
            out[i] = (out[i] + c*x) % P
    return out


def block_diag(A, B):
    n = len(A)
    R = zero(2*n, 2*n)
    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j]
            R[n+i][n+j] = B[i][j]
    return R


def block_S(X):
    Xi = inv(X)
    n = len(X)
    R = zero(2*n, 2*n)
    for i in range(n):
        for j in range(n):
            R[i][n+j] = 2 * Xi[i][j] % P
            R[n+i][j] = X[i][j] % P
    return R


def partitions(n, hi=5):
    if n == 0:
        yield ()
        return
    for a in range(min(n, hi), 0, -1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


def det2(T):
    return (T[0][0]*T[1][1] - T[0][1]*T[1][0]) % P


def tup(T):
    return tuple(x for row in T for x in row)


def mat2_from_tuple(x):
    return [[x[0], x[1]], [x[2], x[3]]]


def main():
    print("C-OMEGA-U-UNITY-4-CARRIER-MINIMALITY-1 breaker")
    print("status NON-CANONICAL same-session adversarial implementation")

    M = [
        [1, 0, 4, 1],
        [0, 1, 4, 0],
        [1, 0, 0, 0],
        [0, 1, 4, 1],
    ]
    M9 = mpow(M, 9)
    basis = intertwiner_space(M, M9)
    assert len(basis) == 4
    invertible = []
    for coeffs in product(range(P), repeat=len(basis)):
        X = vec_to_mat(lincomb(coeffs, basis))
        if rank(X) == 4:
            invertible.append(X)
    assert len(invertible) == 500
    X = invertible[0]
    assert mmul(X, M) == mmul(M9, X)
    print("PASS B1 independent linear solve: intertwiner dimension 4, invertible intertwiners 500")

    # Determinant parity attack on exact Jordan multiplicity spaces.
    squares = {x*x % P for x in range(P)}
    assert squares == {0, 1, 4}
    for m in range(1, 9):
        rhs = pow(2, m, P)
        possible = rhs in squares
        assert possible == (m % 2 == 0)
    print("PASS B2 determinant attack: T^2=2I can occur only in even F5 dimension")

    survivors = []
    killed = []
    for n in range(4, 9):
        for part in partitions(n):
            if max(part) < 4:
                continue
            counts = Counter(part)
            bad = [r for r, mult in counts.items() if mult % 2]
            if bad:
                killed.append((n, part, tuple(bad)))
            else:
                survivors.append((n, part))
    assert all(n >= 8 for n, _ in survivors)
    assert [p for n, p in survivors if n == 8] == [(4, 4)]
    print(f"PASS B3 partition attack: killed={len(killed)}, survivors_through_8={survivors}")

    # Direct attack on the 2D top: classify all square roots of 2I and their lines.
    I2 = eye(2)
    roots = []
    for vals in product(range(P), repeat=4):
        T = mat2_from_tuple(vals)
        if mmul(T, T) == [[2,0],[0,2]]:
            roots.append(T)
    assert len(roots) == 20
    gl2 = [mat2_from_tuple(vals) for vals in product(range(P), repeat=4)
           if det2(mat2_from_tuple(vals)) != 0]
    assert len(gl2) == 480
    base = roots[0]
    orbit = set()
    for G in gl2:
        Gi = inv(G)
        orbit.add(tup(mmul(mmul(G, base), Gi)))
    assert orbit == {tup(T) for T in roots}
    for T in roots:
        for v in product(range(P), repeat=2):
            if v == (0,0):
                continue
            Tv = ((T[0][0]*v[0] + T[0][1]*v[1]) % P,
                  (T[1][0]*v[0] + T[1][1]*v[1]) % P)
            wedge = (v[0]*Tv[1] - v[1]*Tv[0]) % P
            assert wedge != 0
    print("PASS B4 top attack: 20 roots form one GL2 class and every nonzero line is moved")

    # Reconstruct a doubled witness without importing the predecessor's X.
    A = block_diag(M, M)
    S = block_S(X)
    I8 = eye(8)
    assert mmul(S, S) == [[2*x % P for x in row] for row in I8]
    assert mpow(A, 5) == [[2*x % P for x in row] for row in I8]
    assert mmul(S, A) == mmul(mpow(A, 9), S)
    print("PASS B5 fresh rank-8 witness reconstructed from the full intertwiner space")

    print("NO BREAK G1-G5")
    print("G6 STOP full pair classification remains outside this breaker")


if __name__ == "__main__":
    main()
