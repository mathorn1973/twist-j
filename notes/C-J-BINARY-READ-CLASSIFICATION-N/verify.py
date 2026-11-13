#!/usr/bin/env python3
"""C-J-BINARY-READ-CLASSIFICATION-N: proof-structured exact audit.

NON-CANONICAL, L1. Python standard library only, exact integers only.
Frozen by PREREG.md in this directory before its first execution.
"""
import hashlib
import sys
from itertools import product

N_COUNT = 150          # counts and tail audit horizon
N_CLASSIFY = 30        # exact finite classification horizon
TAIL_FROM = 31         # Lemma 5 onset

FAILURES = []


def fail(msg):
    FAILURES.append(msg)
    print("FAIL " + msg)


# ---------------------------------------------------------------- O = Z[z]
def o_mul(x, y):
    a = [0] * 7
    for i in range(4):
        if x[i]:
            for j in range(4):
                a[i + j] += x[i] * y[j]
    for k in (6, 5, 4):            # z^k = -z^(k-4) - z^(k-3) - z^(k-2) - z^(k-1)
        c = a[k]
        if c:
            a[k] = 0
            for t in range(k - 4, k):
                a[t] -= c
    return tuple(a[:4])


ONE = (1, 0, 0, 0)
Z = (0, 1, 0, 0)
J = (1, 0, 1, 0)
PHI = (0, 0, -1, -1)
PHI_INV = (-1, 0, -1, -1)


def o_pow(x, k):
    r = ONE
    for _ in range(k):
        r = o_mul(r, x)
    return r


# --------------------------------------------------------------- Z[phi] path
def zm(p, q):
    a, b = p
    c, d = q
    return (a * c + b * d, a * d + b * c + b * d)


def zs(p, q):
    return (p[0] - q[0], p[1] - q[1])


def zpow(p, k):
    r = (1, 0)
    for _ in range(k):
        r = zm(r, p)
    return r


ZETA_TRACE = {0: (2, 0), 1: (-1, 1), 4: (-1, 1), 2: (0, -1), 3: (0, -1)}
PHI_Z = (0, 1)
PHI_INV_Z = (-1, 1)


def count_v1(eps, a, k, n):
    """|N(u^n - 1)| via the relative norm to K+ = Q(phi)."""
    base = PHI_Z if k > 0 else PHI_INV_Z
    phik = zpow(base, abs(k))
    t = zm(ZETA_TRACE[a % 5], phik)
    if eps == -1:
        t = (-t[0], -t[1])
    p = zm(phik, phik)
    s_prev, s_cur = (2, 0), t
    for _ in range(n - 1):
        s_prev, s_cur = s_cur, zs(zm(t, s_cur), zm(p, s_prev))
    rel = zs(zpow(p, n), s_cur)
    rel = (rel[0] + 1, rel[1])
    x, y = rel
    return abs(x * x + x * y - y * y)


# ------------------------------------------------------------ integer matrices
def mult_matrix(u):
    cols = [o_mul(u, o_pow(Z, c)) for c in range(4)]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def mat_mul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(4)) for j in range(4)] for i in range(4)]


def det_bareiss(A):
    M = [row[:] for row in A]
    n = len(M)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = M[i][j] * M[k][k] - M[i][k] * M[k][j]
                if num % prev != 0:
                    raise ArithmeticError("Bareiss division not exact")
                M[i][j] = num // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def count_v2_table(u, nmax):
    M = mult_matrix(u)
    P = [[int(i == j) for j in range(4)] for i in range(4)]
    out = {}
    for n in range(1, nmax + 1):
        P = mat_mul(P, M)
        A = [[P[i][j] - (1 if i == j else 0) for j in range(4)] for i in range(4)]
        out[n] = abs(det_bareiss(A))
    return out


# -------------------------------------------------------------- number theory
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    r, x, p = 1, n, 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0:
                return 0
            r = -r
        p += 1
    if x > 1:
        r = -r
    return r


def is_prime(n):
    return n >= 2 and all(n % p for p in range(2, n))


def words_exact(d):
    w = sum(mobius(d // e) * 2 ** e for e in divisors(d))
    if w % d:
        raise ArithmeticError("necklace count not integral")
    return w


# ------------------------------------------------------------- certificates
CERTS = {
    ("J", 4): (2, {4: [({4: 2}, 3)], 2: [({2: 2}, 1)], 1: [({2: 1}, 2)]}),
    ("J", 6): (2, {6: [({6: 2}, 9)], 3: [({3: 2}, 2)], 2: [({2: 2}, 1)],
                   1: [({2: 1}, 2)]}),
    ("phi^-1", 6): (3, {6: [({6: 3}, 9)], 3: [({3: 1, 6: 1}, 2)],
                        2: [({6: 1}, 1)], 1: [({3: 1}, 2)]}),
    ("phi^-1", 8): (4, {8: [({8: 4}, 30)], 4: [({4: 4}, 1), ({8: 2}, 2)],
                        2: [({8: 1}, 1)], 1: [({4: 1}, 2)]}),
}

PREDICTED = {
    "J": {1: "L0", 2: "E1", 3: "E1", 4: "CERT", 5: "L1", 6: "CERT"},
    "phi^-1": {1: "L0", 2: "L0", 3: "L1", 4: "L2", 5: "L1", 6: "CERT",
               7: "L1", 8: "CERT"},
}
PREDICTED_EXCEPTIONS = {"J": [1, 5], "phi^-1": [1, 2, 3, 4, 5, 7]}


def necklaces_by_period(n):
    reps = {}
    for w in product((0, 1), repeat=n):
        per = next(p for p in divisors(n) if all(w[i] == w[(i + p) % n] for i in range(n)))
        base = w[:per]
        if base == min(base[i:] + base[:i] for i in range(per)):
            reps.setdefault(per, []).append(base)
    return reps


def check_cert(name, n, C, B):
    c, assign = CERTS[(name, n)]
    ok = True
    use = {e: 0 for e in divisors(n)}
    for d in divisors(n):
        if B[d] == 0:
            continue
        items = assign.get(d, [])
        if sum(cnt for _, cnt in items) != B[d]:
            fail("cert %s n=%d d=%d covers %d of %d necklaces"
                 % (name, n, d, sum(cnt for _, cnt in items), B[d]))
            ok = False
        for pat, cnt in items:
            for e in pat:
                if n % e or e % d:
                    fail("cert %s n=%d d=%d uses invalid e=%d" % (name, n, d, e))
                    ok = False
            val = sum((e // d) * y for e, y in pat.items())
            if val != c:
                fail("cert %s n=%d d=%d pattern value %d != c=%d" % (name, n, d, val, c))
                ok = False
            for e, y in pat.items():
                use[e] = use.get(e, 0) + y * cnt
    for e in use:
        if use[e] > C.get(e, 0):
            fail("cert %s n=%d uses %d cycles of length %d, capacity %d"
                 % (name, n, use[e], e, C.get(e, 0)))
            ok = False
    if not ok:
        return False, c, use
    # abstract realization with this cycle inventory
    reps = necklaces_by_period(n)
    counts = {}
    for d, items in assign.items():
        queue = list(reps[d])
        for pat, cnt in items:
            for _ in range(cnt):
                neck = queue.pop(0)
                for e in sorted(pat):
                    lab = neck * (e // d)
                    for _ in range(pat[e]):
                        for start in range(e):
                            w = tuple(lab[(start + t) % e] for t in range(n))
                            counts[w] = counts.get(w, 0) + 1
        if queue:
            fail("cert %s n=%d d=%d leaves necklaces unassigned" % (name, n, d))
            return False, c, use
    if len(counts) != 2 ** n or any(v != c for v in counts.values()):
        fail("cert %s n=%d abstract realization not uniform" % (name, n))
        return False, c, use
    return True, c, use


def main():
    print("C-J-BINARY-READ-CLASSIFICATION-N verify")
    # carrier identities
    assert o_mul(PHI, PHI_INV) == ONE
    assert o_mul(Z, PHI_INV) == J
    print("CARRIER phi*phi^-1=1 OK; J = z*phi^-1 OK")
    units = [("J", J, (1, 1, -1)), ("phi^-1", PHI_INV, (1, 0, -1))]

    tables = {}
    for name, u, (eps, a, k) in units:
        v2 = count_v2_table(u, N_COUNT)
        F = {}
        for n in range(1, N_COUNT + 1):
            v1 = count_v1(eps, a, k, n)
            if v1 != v2[n]:
                fail("count paths disagree %s n=%d V1=%d V2=%d" % (name, n, v1, v2[n]))
            F[n] = v1
        P = {}
        for n in range(1, N_COUNT + 1):
            P[n] = sum(mobius(n // d) * F[d] for d in divisors(n))
            if P[n] < 0 or P[n] % n:
                fail("non-integral cycle count %s n=%d P=%d" % (name, n, P[n]))
        tables[name] = (F, P)
        h = hashlib.sha256()
        for n in range(1, N_COUNT + 1):
            row = "COUNT %s %d F=%d P=%d" % (name, n, F[n], P[n])
            print(row)
            h.update((row + "\n").encode())
        print("COUNT_TABLE_SHA256 %s %s" % (name, h.hexdigest()))

    for name, u, _ in units:
        F, P = tables[name]
        exceptions = []
        for n in range(1, N_CLASSIFY + 1):
            C = {d: P[d] // d for d in divisors(n)}
            B = {d: words_exact(d) // d for d in divisors(n)}
            cmax = F[n] // 2 ** n
            rule = None
            if P[n] >= n * 2 ** n:
                rule = "E1"
                why = "P=%d >= n*2^n=%d" % (P[n], n * 2 ** n)
                verdict = "YES"
            elif (name, n) in CERTS:
                ok, c, use = check_cert(name, n, C, B)
                rule = "CERT"
                why = "c=%d uses %s capacity %s %s" % (
                    c, ",".join("%d:%d" % (e, use[e]) for e in sorted(use)),
                    ",".join("%d:%d" % (e, C[e]) for e in sorted(C)), "OK" if ok else "FAILED")
                verdict = "YES" if ok else "UNDECIDED"
            elif F[n] < 2 ** n:
                rule = "L0"
                why = "F=%d < 2^n=%d" % (F[n], 2 ** n)
                verdict = "NO"
            elif is_prime(n) and F[1] == 1 and cmax < n:
                rule = "L1"
                why = "n prime, F_1=1, floor(F/2^n)=%d < n" % cmax
                verdict = "NO"
            elif cmax == 1 and F[1] < 2:
                rule = "L2"
                why = "floor(F/2^n)=1, F_1=%d < 2" % F[1]
                verdict = "NO"
            else:
                rule = "NONE"
                why = "no frozen rule applies"
                verdict = "UNDECIDED"
            pred = PREDICTED[name].get(n, "E1")
            if rule != pred:
                fail("decision %s n=%d rule %s, predicted %s" % (name, n, rule, pred))
            if verdict == "NO":
                exceptions.append(n)
            if verdict == "UNDECIDED":
                fail("undecided %s n=%d" % (name, n))
            print("WHY %s %d %s %s" % (name, n, rule, why))
            print("CLASS %s %d %s" % (name, n, verdict))
        ok = exceptions == PREDICTED_EXCEPTIONS[name]
        if not ok:
            fail("exceptions %s %s predicted %s" % (name, exceptions, PREDICTED_EXCEPTIONS[name]))
        print("EXCEPTIONS %s %s predicted %s %s" % (
            name, ",".join(map(str, exceptions)),
            ",".join(map(str, PREDICTED_EXCEPTIONS[name])), "OK" if ok else "MISMATCH"))

    # Lemma 5 integer inequalities and thresholds
    n = TAIL_FROM
    a_ok = 25 ** n >= 512 ** 2 * n * n * 12 ** n
    b_ok = 5 ** n >= 32 * n * 4 ** n
    b_prev = 5 ** (n - 1) >= 32 * (n - 1) * 4 ** (n - 1)
    # ratio (25/12)^k/k^2 nondecreasing iff 25 k^2 >= 12 (k+1)^2, true for every k>=3
    # because (1+1/k)^2 decreases in k; ratio (5/4)^k/k nondecreasing iff 5k >= 4(k+1),
    # true for every k>=4. Both reduce to the first admissible k.
    mono_a = 25 * 3 * 3 >= 12 * (3 + 1) ** 2
    mono_b = 5 * 4 >= 4 * (4 + 1)
    print("TAIL (A) at n=%d %s; (B) at n=%d %s; (B) at n=%d %s" % (
        n, "OK" if a_ok else "FAIL", n, "OK" if b_ok else "FAIL",
        n - 1, "holds" if b_prev else "fails"))
    print("TAIL monotone (A) from 3 %s; (B) from 4 %s" % (
        "OK" if mono_a else "FAIL", "OK" if mono_b else "FAIL"))
    if not (a_ok and b_ok and mono_a and mono_b):
        fail("tail lemma integer premises")
    if b_prev:
        fail("onset not first at 31 as frozen")
    for name, _, _ in units:
        F, P = tables[name]
        bad = [m for m in range(TAIL_FROM, N_COUNT + 1) if P[m] < m * 2 ** m]
        if bad:
            fail("tail audit %s fails at %s" % (name, bad[:5]))
        print("TAIL_AUDIT %s n=%d..%d %s" % (name, TAIL_FROM, N_COUNT, "OK" if not bad else "FAIL"))

    print("VERDICT %s" % ("PASS" if not FAILURES else "FAIL %d" % len(FAILURES)))
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
