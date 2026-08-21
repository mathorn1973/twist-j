#!/usr/bin/env python3
# Recon, outside the frozen gates: locate the smallest real nonbalanced
# extremal quadruple. Round two of the break attempt reported 326 of them
# below 4e9 including n = 7461177; that count was an artifact of an inertia
# routine that returned None on a zero pivot with no fallback, and None
# compares unequal to the balanced triple. Every inertia below is decided by
# two paths that both return a value.

import sys
from bisect import bisect_right
from fractions import Fraction


def pc(x):
    return bin(x).count("1")


def t(n):
    return -1 if (pc(n) & 1) else 1


def c_val(N, plist):
    supp = [p for p in plist if N % p == 0]
    s = 0
    for A in range(1 << len(supp)):
        d = 1
        for i in range(len(supp)):
            if (A >> i) & 1:
                d *= supp[i]
        v = t(N // d)
        s += -v if (pc(A) & 1) else v
    return s


def berkowitz(A):
    n = len(A)
    C = [1, -A[0][0]]
    for r in range(1, n):
        a = A[r][r]
        S = [A[r][j] for j in range(r)]
        R = [A[i][r] for i in range(r)]
        M = [row[:r] for row in A[:r]]
        v = R[:]
        moms = [a, sum(S[i] * v[i] for i in range(r))]
        for _ in range(r - 1):
            v = [sum(M[i][j] * v[j] for j in range(r)) for i in range(r)]
            moms.append(sum(S[i] * v[i] for i in range(r)))
        col = [1] + [-mm for mm in moms]
        Cn = [0] * (r + 2)
        for i in range(r + 2):
            s = 0
            for j in range(min(i, len(C) - 1) + 1):
                if i - j < len(col):
                    s += col[i - j] * C[j]
            Cn[i] = s
        C = Cn
    return C


def inertia_berk(A):
    C = berkowitz(A)
    n = len(C) - 1
    z = 0
    while z < n and C[n - z] == 0:
        z += 1
    seq = [v for v in C if v != 0]
    pos = sum(1 for i in range(len(seq) - 1)
              if (seq[i] > 0) != (seq[i + 1] > 0))
    seqm = [(C[i] if ((n - i) & 1) == 0 else -C[i]) for i in range(n + 1)]
    seqm = [v for v in seqm if v != 0]
    neg = sum(1 for i in range(len(seqm) - 1)
              if (seqm[i] > 0) != (seqm[i + 1] > 0))
    assert pos + neg + z == n
    return (neg, z, pos)


def inertia_minors(A):
    n = len(A)
    M = [row[:] for row in A]
    prev = 1
    neg = 0
    last = 1
    for k in range(n):
        piv = M[k][k]
        if piv == 0:
            return None
        if (piv > 0) != (last > 0):
            neg += 1
        last = piv
        if k == n - 1:
            break
        for i in range(k + 1, n):
            mik = M[i][k]
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * piv - mik * M[k][j]) // prev
        prev = piv
    return (neg, 0, n - neg)


def inertia(A):
    a = inertia_minors(A)
    b = inertia_berk(A)
    if a is not None and a != b:
        raise AssertionError("path disagreement")
    return b


def block(P):
    M = 1 << len(P)
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        nS[x] = nS[x ^ lb] * P[lb.bit_length() - 1]
    return [[c_val(nS[S] * nS[T], P) for T in range(M)] for S in range(M)]


def evil_primes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= limit:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [p for p in range(3, limit + 1, 2) if sieve[p] and t(p) == 1]


def main():
    LIMIT = 4 * 10 ** 9
    ev = evil_primes(LIMIT // (3 * 5 * 17))
    print("RECON smallest real k=4 failure, n <= %d" % LIMIT)
    print("evil primes: %d" % len(ev))
    n_quads = 0
    n_zero_pivot = 0
    fails = []
    np_ = len(ev)
    for a in range(np_):
        p = ev[a]
        if p ** 4 > LIMIT:
            break
        for b in range(a + 1, np_):
            q = ev[b]
            if p * q ** 3 > LIMIT:
                break
            if t(p * q) != -1:
                continue
            for c in range(b + 1, np_):
                r = ev[c]
                if p * q * r * r > LIMIT:
                    break
                if t(p * r) != -1 or t(q * r) != -1 or t(p * q * r) != 1:
                    continue
                hi = LIMIT // (p * q * r)
                for d in range(c + 1, bisect_right(ev, hi)):
                    s = ev[d]
                    if not (t(p * s) == -1 and t(q * s) == -1
                            and t(r * s) == -1 and t(p * q * s) == 1
                            and t(p * r * s) == 1 and t(q * r * s) == 1
                            and t(p * q * r * s) == -1):
                        continue
                    n_quads += 1
                    P = [p, q, r, s]
                    A = block(P)
                    if inertia_minors(A) is None:
                        n_zero_pivot += 1
                    i = inertia(A)
                    if i != (8, 0, 8):
                        fails.append((p * q * r * s, tuple(P), i))
    fails.sort()
    print("extremal quadruples: %d" % n_quads)
    print("zero-pivot cases routed to the char-poly path: %d" % n_zero_pivot)
    print("nonbalanced: %d" % len(fails))
    for n, P, i in fails[:12]:
        print("FAIL n=%d P=%s inertia=%s" % (n, P, i))
    if fails:
        n, P, i = fails[0]
        print("SMALLEST n=%d P=%s inertia=%s" % (n, P, i))
        for y in P:
            s3 = tuple(x for x in P if x != y)
            print("  sub-triple %s n=%d inertia=%s"
                  % (s3, s3[0] * s3[1] * s3[2], inertia(block(list(s3)))))
    profiles = {}
    for _n, _P, i in fails:
        profiles[i] = profiles.get(i, 0) + 1
    print("failure inertia profiles: %s" % (sorted(profiles.items()),))
    return 0


if __name__ == "__main__":
    sys.exit(main())
