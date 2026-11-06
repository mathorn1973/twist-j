#!/usr/bin/env python3
"""C-J-BINARY-READ-CLASSIFICATION-N: code-distinct break attempt.

NON-CANONICAL, L1. Python standard library only, exact integers only.
Frozen by PREREG.md before its first execution. Shares no code with
verify.py. Paths:
  B1  counts from the characteristic polynomial by traces and Newton
      identities, F_n = |prod(lambda_i^n - 1)| from power sums t_(jn);
  B2  explicit enumeration of R_n(u) through a lower-triangular column
      Hermite form, explicit orbits, exhaustive assignment search for n<=8,
      and end-to-end realization of a reader on the enumerated quotient for
      every positive n<=12, checking every n-word by iterating the tick.
"""
import sys
from itertools import combinations_with_replacement, product

COUNT_MAX = 150
ENUM_MAX = 12
EXHAUST_MAX = 8
CLASS_MAX = 30
TAIL_FROM = 31

BAD = []


def bad(msg):
    BAD.append(msg)
    print("BREAK " + msg)


# ------------------------------------------------ polynomial ring Z[z]/(Phi_5)
def pmul(f, g):
    acc = [0] * 7
    for i, fi in enumerate(f):
        for j, gj in enumerate(g):
            acc[i + j] += fi * gj
    # reduce with z^5 = 1 first, then z^4 = -(1 + z + z^2 + z^3)
    acc[0] += acc[5]
    acc[1] += acc[6]
    top = acc[4]
    return tuple(acc[i] - top for i in range(4))


UNITS = [("J", (1, 0, 1, 0)), ("phi^-1", (-1, 0, -1, -1))]


def mat_of(u):
    basis = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    cols = [pmul(u, b) for b in basis]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def mvec(A, x):
    return tuple(sum(A[i][k] * x[k] for k in range(4)) for i in range(4))


def trace(A):
    return sum(A[i][i] for i in range(4))


# --------------------------------------------------------------- path B1
def charpoly_e(M):
    p = []
    P = M
    for _ in range(4):
        p.append(trace(P))
        P = mmul(P, M)
    e1 = p[0]
    e2 = e1 * p[0] - p[1]
    assert e2 % 2 == 0
    e2 //= 2
    e3 = e2 * p[0] - e1 * p[1] + p[2]
    assert e3 % 3 == 0
    e3 //= 3
    e4 = e3 * p[0] - e2 * p[1] + e1 * p[2] - p[3]
    assert e4 % 4 == 0
    e4 //= 4
    return (e1, e2, e3, e4)


def trace_sequence(e, jmax):
    e1, e2, e3, e4 = e
    t = [4]
    # Newton for j = 1..4, then the linear recurrence
    t.append(e1)
    t.append(e1 * t[1] - 2 * e2)
    t.append(e1 * t[2] - e2 * t[1] + 3 * e3)
    t.append(e1 * t[3] - e2 * t[2] + e3 * t[1] - 4 * e4)
    for j in range(5, jmax + 1):
        t.append(e1 * t[j - 1] - e2 * t[j - 2] + e3 * t[j - 3] - e4 * t[j - 4])
    return t


def counts_b1(u):
    M = mat_of(u)
    e = charpoly_e(M)
    # cross-check the first traces directly
    P = M
    t = trace_sequence(e, 4 * COUNT_MAX)
    for j in range(1, 9):
        if trace(P) != t[j]:
            bad("trace recurrence mismatch j=%d" % j)
        P = mmul(P, M)
    F = {}
    for n in range(1, COUNT_MAX + 1):
        q1, q2, q3, q4 = t[n], t[2 * n], t[3 * n], t[4 * n]
        E1 = q1
        E2 = E1 * q1 - q2
        if E2 % 2:
            bad("Newton divisibility E2 n=%d" % n)
        E2 //= 2
        E3 = E2 * q1 - E1 * q2 + q3
        if E3 % 3:
            bad("Newton divisibility E3 n=%d" % n)
        E3 //= 3
        E4 = E3 * q1 - E2 * q2 + E1 * q3 - q4
        if E4 % 4:
            bad("Newton divisibility E4 n=%d" % n)
        E4 //= 4
        F[n] = abs(E4 - E3 + E2 - E1 + 1)
    return e, F


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n):
    r, x, p = 1, n, 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0:
                return 0
            r = -r
        p += 1
    return -r if x > 1 else r


def primitive(F, n):
    return sum(mu(n // d) * F[d] for d in divs(n))


# --------------------------------------------------------------- path B2
def hermite_lower(A):
    H = [row[:] for row in A]
    for i in range(4):
        for j in range(i + 1, 4):
            while H[i][j] != 0:
                q = H[i][i] // H[i][j]
                for r in range(4):
                    H[r][i] -= q * H[r][j]
                for r in range(4):
                    H[r][i], H[r][j] = H[r][j], H[r][i]
        if H[i][i] < 0:
            for r in range(4):
                H[r][i] = -H[r][i]
        if H[i][i] == 0:
            raise ArithmeticError("singular relation lattice")
    return H


def make_reducer(H):
    diag = [H[i][i] for i in range(4)]

    def red(x):
        x = list(x)
        for i in range(4):
            q = x[i] // diag[i]
            if q:
                for r in range(4):
                    x[r] -= q * H[r][i]
        return tuple(x)
    return red, diag


def enumerate_quotient(u, n, F_expected):
    M = mat_of(u)
    P = [[int(i == j) for j in range(4)] for i in range(4)]
    for _ in range(n):
        P = mmul(P, M)
    A = [[P[i][j] - (1 if i == j else 0) for j in range(4)] for i in range(4)]
    H = hermite_lower(A)
    red, diag = make_reducer(H)
    size = diag[0] * diag[1] * diag[2] * diag[3]
    lattice_ok = size == F_expected and all(
        red(tuple(A[r][c] for r in range(4))) == (0, 0, 0, 0) for c in range(4))
    if not lattice_ok:
        bad("lattice audit %d" % n)

    def index(x):
        return x[0] + diag[0] * (x[1] + diag[1] * (x[2] + diag[2] * x[3]))

    seen = bytearray(size)
    cycles = {}
    for x in product(range(diag[0]), range(diag[1]), range(diag[2]), range(diag[3])):
        x = tuple(x)
        if seen[index(x)]:
            continue
        orbit = []
        y = x
        while True:
            if seen[index(y)]:
                break
            seen[index(y)] = 1
            orbit.append(y)
            y = red(mvec(M, y))
        if y != x:
            bad("orbit of %s does not close at its start, n=%d" % (x, n))
        cycles.setdefault(len(orbit), []).append(orbit)
    if sum(seen) != size:
        bad("enumeration incomplete n=%d" % n)
    step = lambda z: red(mvec(M, z))
    return size, cycles, step, lattice_ok


def necklaces(n):
    out = {}
    for w in product((0, 1), repeat=n):
        per = next(p for p in divs(n) if all(w[i] == w[(i + p) % n] for i in range(n)))
        b = w[:per]
        if b == min(b[i:] + b[:i] for i in range(per)):
            out.setdefault(per, []).append(b)
    return out


def class_patterns(c, n, d):
    E = [e for e in divs(n) if e % d == 0]
    res = []

    def rec(i, rem, acc):
        if i == len(E):
            if rem == 0:
                res.append(tuple(acc))
            return
        v = E[i] // d
        for y in range(rem // v + 1):
            acc.append(y)
            rec(i + 1, rem - v * y, acc)
            acc.pop()
    rec(0, c, [])
    return E, res


def exhaustive(n, ncyc, F_n):
    """Return (minimal c, assignment) or (None, None). Complete search."""
    nk = necklaces(n)
    count = {d: len(v) for d, v in nk.items()}
    cmax = F_n // 2 ** n
    for c in range(1, cmax + 1):
        per_class = []
        for d in sorted(count):
            E, pats = class_patterns(c, n, d)
            options = {}
            for combo in combinations_with_replacement(range(len(pats)), count[d]):
                tot = {}
                for k in combo:
                    for e, y in zip(E, pats[k]):
                        if y:
                            tot[e] = tot.get(e, 0) + y
                key = tuple(sorted(tot.items()))
                if key not in options:
                    options[key] = [(E, pats[k]) for k in combo]
            per_class.append((d, options))
        keys = [list(opt.keys()) for _, opt in per_class]
        for choice in product(*keys):
            used = {}
            for key in choice:
                for e, y in key:
                    used[e] = used.get(e, 0) + y
            if all(used[e] <= ncyc.get(e, 0) for e in used):
                assign = []
                for (d, opt), key in zip(per_class, choice):
                    for neck, (E, pat) in zip(nk[d], opt[key]):
                        assign.append((neck, d, {e: y for e, y in zip(E, pat) if y}))
                return c, assign
    return None, None


def e1_assignment(n):
    nk = necklaces(n)
    return [(neck, d, {n: d}) for d in sorted(nk) for neck in nk[d]]


def realize(n, c, assign, cycles, step):
    pool = {e: list(v) for e, v in cycles.items()}
    label = {}
    for neck, d, pat in assign:
        for e in sorted(pat):
            for _ in range(pat[e]):
                if not pool.get(e):
                    return False, "pool of %d-cycles exhausted" % e
                orb = pool[e].pop()
                for j, x in enumerate(orb):
                    label[x] = neck[j % d]
    S = list(label)
    if len(S) != c * 2 ** n:
        return False, "support size %d != c*2^n" % len(S)
    counts = {}
    for x in S:
        y = x
        w = []
        for _ in range(n):
            if y not in label:
                return False, "support not invariant"
            w.append(label[y])
            y = step(y)
        if y != x:
            return False, "tick^n is not the identity on the support"
        counts[tuple(w)] = counts.get(tuple(w), 0) + 1
    if len(counts) != 2 ** n or any(v != c for v in counts.values()):
        return False, "n-words not uniform"
    return True, "support=%d words=%d each=%d" % (len(S), 2 ** n, c)


def main():
    print("C-J-BINARY-READ-CLASSIFICATION-N break")
    out_count = []
    out_class = []
    predicted = {"J": [1, 5], "phi^-1": [1, 2, 3, 4, 5, 7]}
    for name, u in UNITS:
        e, F = counts_b1(u)
        print("CHARPOLY %s x^4 - %d x^3 + %d x^2 - %d x + %d" % ((name,) + e))
        P = {n: primitive(F, n) for n in range(1, COUNT_MAX + 1)}
        for n in range(1, COUNT_MAX + 1):
            if P[n] < 0 or P[n] % n:
                bad("cycle count non-integral %s n=%d" % (name, n))
            out_count.append("COUNT %s %d F=%d P=%d" % (name, n, F[n], P[n]))
        verdicts = {}
        for n in range(1, ENUM_MAX + 1):
            size, cycles, step, lat = enumerate_quotient(u, n, F[n])
            ncyc = {e: len(v) for e, v in cycles.items()}
            for d in divs(n):
                fixed = sum(e * k for e, k in ncyc.items() if d % e == 0)
                if fixed != F[d]:
                    bad("fixed-point identity %s n=%d d=%d: %d != %d" % (name, n, d, fixed, F[d]))
            for e in ncyc:
                if n % e:
                    bad("cycle length %d does not divide n=%d" % (e, n))
            print("ENUM %s %d states=%d lattice=%s cycles=%s" % (
                name, n, size, "OK" if lat else "FAIL",
                ",".join("%d:%d" % (e, ncyc[e]) for e in sorted(ncyc))))
            if n <= EXHAUST_MAX:
                c, assign = exhaustive(n, ncyc, F[n])
                print("EXHAUST %s %d cmax=%d minimal_c=%s" % (
                    name, n, F[n] // 2 ** n, "NONE" if c is None else c))
                verdicts[n] = "NO" if c is None else "YES"
            else:
                if ncyc.get(n, 0) >= 2 ** n:
                    c, assign = n, e1_assignment(n)
                    verdicts[n] = "YES"
                else:
                    c, assign = None, None
                    verdicts[n] = "UNDECIDED"
                print("E1MEASURED %s %d n_cycles=%d need=%d" % (name, n, ncyc.get(n, 0), 2 ** n))
            if c is not None:
                ok, why = realize(n, c, assign, cycles, step)
                if not ok:
                    bad("realization %s n=%d: %s" % (name, n, why))
                print("REALIZE %s %d c=%d %s %s" % (name, n, c, why, "OK" if ok else "FAIL"))
        for n in range(ENUM_MAX + 1, CLASS_MAX + 1):
            verdicts[n] = "YES" if P[n] >= n * 2 ** n else "UNDECIDED"
        exceptions = [n for n in range(1, CLASS_MAX + 1) if verdicts[n] == "NO"]
        und = [n for n in range(1, CLASS_MAX + 1) if verdicts[n] == "UNDECIDED"]
        for n in range(1, CLASS_MAX + 1):
            out_class.append("CLASS %s %d %s" % (name, n, verdicts[n]))
        if und:
            bad("undecided %s %s" % (name, und))
        if exceptions != predicted[name]:
            bad("exceptions %s %s predicted %s" % (name, exceptions, predicted[name]))
        print("EXCEPTIONS %s %s predicted %s %s" % (
            name, ",".join(map(str, exceptions)), ",".join(map(str, predicted[name])),
            "OK" if exceptions == predicted[name] else "MISMATCH"))
        tail_bad = [n for n in range(TAIL_FROM, COUNT_MAX + 1) if P[n] < n * 2 ** n]
        if tail_bad:
            bad("tail audit %s %s" % (name, tail_bad[:5]))
        print("TAIL_AUDIT %s n=%d..%d %s" % (name, TAIL_FROM, COUNT_MAX, "OK" if not tail_bad else "FAIL"))
    for row in out_count:
        print(row)
    for row in out_class:
        print(row)
    print("VERDICT %s" % ("PASS" if not BAD else "FAIL %d" % len(BAD)))
    return 0 if not BAD else 1


if __name__ == "__main__":
    sys.exit(main())
