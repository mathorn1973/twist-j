#!/usr/bin/env python3
# P-TM-SYM2-REVERSAL-CLOSURE-1 formal verifier.
#
# Run from the repository root with no arguments:
#   python3 probes/P-TM-SYM2-REVERSAL-CLOSURE-1/verify.py
#
# Python standard library only. Exact arithmetic only: int, Fraction,
# and Q(sqrt5) as pairs of Fractions. No float anywhere. Deterministic.
#
# This pin embeds NO expected route, translation, transport verdict,
# orbit count, or output hash. Both scientific routes REVERSAL-TOGGLE
# and REVERSAL-SILENT are live, first-class, exit-zero results. The
# route is derived from computed fields by the frozen table of the
# preregistration. Any structural failure is STOP (exit 1), never a
# scientific route.
#
# Frozen source snapshots (byte-for-byte copies of public transcripts;
# input, not output):
#   SOURCE-MEASURE1-EXPECTED.txt
#     sha256 395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f
#   SOURCE-SEMILINEAR-EXPECTED.txt
#     sha256 47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296aaa371177f662bfd19
import hashlib
import itertools
import re
import sys
from fractions import Fraction

PROBE_DIR = "probes/P-TM-SYM2-REVERSAL-CLOSURE-1/"
SRC_MEASURE = PROBE_DIR + "SOURCE-MEASURE1-EXPECTED.txt"
SRC_SEMI = PROBE_DIR + "SOURCE-SEMILINEAR-EXPECTED.txt"
SHA_MEASURE = ("395209f15d0943f38b1d8af4f6d20769c5e113c65bac9"
               "455944613ab3b40726f")
SHA_SEMI = ("47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296a"
            "aa371177f662bfd19")

FAILURES = []


def cert(label, ok):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAILURES.append(label)


def stop_if_failed(stage):
    if FAILURES:
        print("RESULT: STOP (%d structural failures at stage %s)"
              % (len(FAILURES), stage))
        sys.exit(1)


# ============================================================ stage A
# The drive, the carrier, the reversal, the children, the transfer.
def popcount_theta(n):
    return bin(n).count("1") % 2


THETA = [popcount_theta(n) for n in range(0, 4100)]

word = "0"
while len(word) < 4100:
    word = "".join("01" if c == "0" else "10" for c in word)
cert("A1 the popcount drive equals the substitution fixed point on the "
     "first 4100 letters",
     all(int(word[n]) == THETA[n] for n in range(4100)))

W3 = [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0)]
WIDX = {w: i for i, w in enumerate(W3)}
windows_seen = sorted({(THETA[n - 1], THETA[n], THETA[n + 1])
                       for n in range(1, 4098)})
factors_seen = sorted({tuple(THETA[i:i + 3]) for i in range(0, 4095)})
cert("A2 centered windows and length-3 factors both exhaust exactly the "
     "six-word carrier W3",
     windows_seen == W3 and factors_seen == W3)


def wN(w):
    return (1 - w[0], 1 - w[1], 1 - w[2])


def wR(w):
    return (w[2], w[1], w[0])


cert("A3 N is a fixed-point-free involution, R is an involution, they "
     "commute, and R fixes exactly the palindromes 010 and 101",
     all(wN(w) in WIDX and wN(wN(w)) == w and wN(w) != w for w in W3)
     and all(wR(w) in WIDX and wR(wR(w)) == w for w in W3)
     and all(wR(wN(w)) == wN(wR(w)) for w in W3)
     and sorted(w for w in W3 if wR(w) == w) == [(0, 1, 0), (1, 0, 1)])

PERM_N = tuple(WIDX[wN(w)] for w in W3)
PERM_R = tuple(WIDX[wR(w)] for w in W3)


def E_even(w):
    return (1 - w[0], w[1], 1 - w[1])


def E_odd(w):
    return (w[1], 1 - w[1], w[2])


cert("A4 the child maps are grounded in the drive for every counter "
     "m in [1, 2048], preserve W3, and commute with N",
     all((THETA[2 * m - 1], THETA[2 * m], THETA[2 * m + 1])
         == E_even((THETA[m - 1], THETA[m], THETA[m + 1]))
         and (THETA[2 * m], THETA[2 * m + 1], THETA[2 * m + 2])
         == E_odd((THETA[m - 1], THETA[m], THETA[m + 1]))
         for m in range(1, 2049))
     and all(E_even(w) in WIDX and E_odd(w) in WIDX for w in W3)
     and all(E_even(wN(w)) == wN(E_even(w))
             and E_odd(wN(w)) == wN(E_odd(w)) for w in W3))
cert("A5 reversal intertwines the children up to negation: "
     "R o E_even = N o E_odd o R on W3",
     all(wR(E_even(w)) == wN(E_odd(wR(w))) for w in W3))

FROZEN_TRANSFER = {
    (0, 0, 1): [(1, 0, 1), (0, 1, 1)],
    (0, 1, 0): [(1, 1, 0), (1, 0, 0)],
    (0, 1, 1): [(1, 1, 0), (1, 0, 1)],
    (1, 0, 0): [(0, 0, 1), (0, 1, 0)],
    (1, 0, 1): [(0, 0, 1), (0, 1, 1)],
    (1, 1, 0): [(0, 1, 0), (1, 0, 0)],
}
cert("A6 the child maps reproduce the frozen public transfer",
     all(sorted([E_even(w), E_odd(w)]) == sorted(FROZEN_TRANSFER[w])
         for w in W3))

T = [[0] * 6 for _ in range(6)]
for w in W3:
    for ch in (E_even(w), E_odd(w)):
        T[WIDX[ch]][WIDX[w]] += 1


def rank_frac(mat):
    m = [[Fraction(x) for x in row] for row in mat]
    r = 0
    for c in range(len(m[0])):
        piv = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
    return r


F_UNIF = [Fraction(1, 6)] * 6
cert("A7 transfer row and column sums are 2; rank(T - 2I) = 5; the "
     "unique normalized stationary law is uniform and invariant under "
     "both N and R pushforward; T commutes with the negation "
     "permutation",
     all(sum(T[i][j] for j in range(6)) == 2 for i in range(6))
     and all(sum(T[i][j] for i in range(6)) == 2 for j in range(6))
     and rank_frac([[T[i][j] - (2 if i == j else 0) for j in range(6)]
                    for i in range(6)]) == 5
     and all(sum(Fraction(T[i][j]) * F_UNIF[j] for j in range(6))
             == 2 * F_UNIF[i] for i in range(6))
     and all(F_UNIF[PERM_N[i]] == F_UNIF[i] for i in range(6))
     and all(F_UNIF[PERM_R[i]] == F_UNIF[i] for i in range(6))
     and all(T[PERM_N[i]][PERM_N[j]] == T[i][j]
             for i in range(6) for j in range(6)))
stop_if_failed("A")

# ============================================================ stage B
# Frozen sources, the class, the fibers, the published blocks.
mbytes = open(SRC_MEASURE, "rb").read()
sbytes = open(SRC_SEMI, "rb").read()
cert("B1 both source snapshots are byte-identical to their pinned "
     "SHA-256",
     hashlib.sha256(mbytes).hexdigest() == SHA_MEASURE
     and hashlib.sha256(sbytes).hexdigest() == SHA_SEMI)
stop_if_failed("B1")

BLOCKS = []
mtext = mbytes.decode("ascii")
for k in (1, 2, 3, 4):
    m = re.search(r"B5 ORBIT %d MEMBERS: (.*)" % k, mtext)
    ok = m is not None
    cert("B2.%d published orbit block %d parsed" % (k, k), ok)
    if ok:
        tup = re.findall(r"\(([0-9, ]+)\)", m.group(1))
        BLOCKS.append({tuple(int(x) for x in t.split(",")) for t in tup})
stop_if_failed("B2")

stext = sbytes.decode("ascii")


def semifield(name):
    m = re.search(r"^%s: (.*)$" % name, stext, re.M)
    return m.group(1) if m else None


SEMI = {name: semifield(name) for name in (
    "ROUTE", "GAMMA_SL_ORDER", "EXPONENT_ONE_COUNT", "COSET_CHARACTER",
    "RESIDUAL_INVARIANT", "SELECTOR_ORBIT_COUNT", "SELECTOR_ORBIT_SIZES")}
cert("B3 the semilinear scientific block parsed with route "
     "SEMILINEAR-DOUBLE and residual invariant chi_Q chi_F",
     SEMI["ROUTE"] == "SEMILINEAR-DOUBLE"
     and SEMI["RESIDUAL_INVARIANT"] == "chi_Q chi_F"
     and None not in SEMI.values())
stop_if_failed("B3")

SIGMA = (1, 0, 3, 2, 5, 4)


def compose(p, q):
    return tuple(p[q[i]] for i in range(6))


def inverse(p):
    inv = [0] * 6
    for i in range(6):
        inv[p[i]] = i
    return tuple(inv)


def parity(seq):
    inv = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                inv += 1
    return inv % 2


CLASS = []
for t in itertools.product(range(6), repeat=6):
    if len(set(t)) != 6:
        continue
    if all(t[PERM_N[i]] == SIGMA[t[i]] for i in range(6)):
        CLASS.append(t)
CLASS_SET = set(CLASS)
cert("B4 the complete function-space scan (46656 maps) yields exactly "
     "48 equivariant bijections, equal to the union of the four "
     "published blocks (sizes 12,12,12,12, pairwise disjoint)",
     len(CLASS) == 48
     and [len(b) for b in BLOCKS] == [12, 12, 12, 12]
     and len(BLOCKS[0] | BLOCKS[1] | BLOCKS[2] | BLOCKS[3]) == 48
     and set().union(*BLOCKS) == CLASS_SET)
cert("B5 precomposition by R and by N stabilizes the class",
     all(compose(s, PERM_R) in CLASS_SET
         and compose(s, PERM_N) in CLASS_SET for s in CLASS))
stop_if_failed("B")

LPAIR = (0, 0, 1, 1, 2, 2)
LORIENT = (0, 1, 0, 1, 0, 1)
WBASE = (0, 1, 2)


def fiber_route1(s):
    pi = tuple(LPAIR[s[WBASE[i]]] for i in range(3))
    eps = tuple(LORIENT[s[WBASE[i]]] for i in range(3))
    return (parity(pi), sum(eps) % 2)


def wchar(a):
    q = parity(tuple(LPAIR[a[2 * i]] for i in range(3)))
    f = parity(a)
    return (q, f)


S0 = min(CLASS)
S0INV = inverse(S0)
F0 = fiber_route1(S0)


def fiber_route2(s):
    qa, fa = wchar(compose(s, S0INV))
    return ((qa + F0[0]) % 2, (fa + F0[1]) % 2)


cert("B6 two independent fiber routes agree on all 48 members",
     all(fiber_route1(s) == fiber_route2(s) for s in CLASS))
FIBER = {s: fiber_route1(s) for s in CLASS}
block_fibers = []
single = True
for b in BLOCKS:
    fs = {FIBER[s] for s in b}
    if len(fs) != 1:
        single = False
    block_fibers.append(sorted(fs)[0])
cert("B7 each published block carries a single fiber and the four "
     "block fibers are pairwise distinct",
     single and len(set(block_fibers)) == 4)
stop_if_failed("B")

# ============================================================ stage C
# Exact Q(sqrt5); the 96-case realizability scan by two independent
# internal methods with mandatory per-case agreement.
HALF = Fraction(1, 2)
PHI = (HALF, HALF)
ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def kadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def ksub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def kmul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def kneg(x):
    return (-x[0], -x[1])


def kinv(x):
    d = x[0] * x[0] - 5 * x[1] * x[1]
    return (x[0] / d, -x[1] / d)


def kconj(x):
    return (x[0], -x[1])


def kzero(x):
    return x[0] == 0 and x[1] == 0


V = [
    (ZERO, ONE, PHI),
    (ZERO, ONE, kneg(PHI)),
    (ONE, PHI, ZERO),
    (ONE, kneg(PHI), ZERO),
    (PHI, ZERO, ONE),
    (PHI, ZERO, kneg(ONE)),
]


def cross(u, v):
    return (
        ksub(kmul(u[1], v[2]), kmul(u[2], v[1])),
        ksub(kmul(u[2], v[0]), kmul(u[0], v[2])),
        ksub(kmul(u[0], v[1]), kmul(u[1], v[0])),
    )


def proportional(u, v):
    return all(kzero(x) for x in cross(u, v)) \
        and not all(kzero(x) for x in u)


def kdot(u, v):
    a = ZERO
    for i in range(3):
        a = kadd(a, kmul(u[i], v[i]))
    return a


cos_ok = True
for i in range(6):
    for j in range(i + 1, 6):
        num = kmul(kdot(V[i], V[j]), kdot(V[i], V[j]))
        den = kmul(kdot(V[i], V[i]), kdot(V[j], V[j]))
        if kmul(num, kinv(den)) != (Fraction(1, 5), Fraction(0)):
            cos_ok = False
cert("C1 all fifteen registered line pairs have squared cosine exactly "
     "1/5", cos_ok)

WPERMS = [p for p in itertools.permutations(range(6))
          if compose(p, SIGMA) == compose(SIGMA, p)]
cert("C2 the sigma_line centralizer W has exactly 48 elements",
     len(WPERMS) == 48)


def mat_from_cols(c1, c2, c3):
    return tuple(tuple((c1, c2, c3)[j][i] for j in range(3))
                 for i in range(3))


def mat_vec(m, v):
    return tuple(
        kadd(kadd(kmul(m[i][0], v[0]), kmul(m[i][1], v[1])),
             kmul(m[i][2], v[2]))
        for i in range(3))


def mat_mul(a, b):
    return tuple(
        tuple(
            kadd(kadd(kmul(a[i][0], b[0][j]), kmul(a[i][1], b[1][j])),
                 kmul(a[i][2], b[2][j]))
            for j in range(3))
        for i in range(3))


def det3(m):
    t1 = kmul(m[0][0], ksub(kmul(m[1][1], m[2][2]),
                            kmul(m[1][2], m[2][1])))
    t2 = kmul(m[0][1], ksub(kmul(m[1][0], m[2][2]),
                            kmul(m[1][2], m[2][0])))
    t3 = kmul(m[0][2], ksub(kmul(m[1][0], m[2][1]),
                            kmul(m[1][1], m[2][0])))
    return kadd(ksub(t1, t2), t3)


def mat_inv(m):
    di = kinv(det3(m))
    cof = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rows = [a for a in range(3) if a != i]
            cols = [b for b in range(3) if b != j]
            sub = ksub(kmul(m[rows[0]][cols[0]], m[rows[1]][cols[1]]),
                       kmul(m[rows[0]][cols[1]], m[rows[1]][cols[0]]))
            cof[i][j] = kmul(di, sub if (i + j) % 2 == 0 else kneg(sub))
    return tuple(tuple(cof[j][i] for j in range(3)) for i in range(3))


frame_degenerate = False


def realizable_frame(p, e):
    global frame_degenerate
    src = [tuple(kconj(c) for c in v) if e == 1 else v for v in V]
    tgt = [V[p[i]] for i in range(6)]
    Wm = mat_from_cols(src[0], src[1], src[2])
    Um = mat_from_cols(tgt[0], tgt[1], tgt[2])
    c = mat_vec(mat_inv(Wm), src[3])
    d = mat_vec(mat_inv(Um), tgt[3])
    if any(kzero(x) for x in c) or any(kzero(x) for x in d):
        frame_degenerate = True
        return False
    scale = [kmul(d[i], kinv(c[i])) for i in range(3)]
    Dm = ((scale[0], ZERO, ZERO), (ZERO, scale[1], ZERO),
          (ZERO, ZERO, scale[2]))
    B = mat_mul(Um, mat_mul(Dm, mat_inv(Wm)))
    if kzero(det3(B)):
        return False
    for i in range(6):
        if not proportional(mat_vec(B, src[i]), tgt[i]):
            return False
    return True


def rref_null(rowsm, cols):
    m = [row[:] for row in rowsm]
    r = 0
    pivots = []
    for c in range(cols):
        piv = None
        for i in range(r, len(m)):
            if not kzero(m[i][c]):
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = kinv(m[r][c])
        m[r] = [kmul(pv, x) for x in m[r]]
        for i in range(len(m)):
            if i != r and not kzero(m[i][c]):
                f = m[i][c]
                m[i] = [ksub(a, kmul(f, b)) for a, b in zip(m[i], m[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(cols) if c not in pivots]
    basis = []
    for fc in free:
        vec = [ZERO] * cols
        vec[fc] = ONE
        for rr, pc in enumerate(pivots):
            vec[pc] = kneg(m[rr][fc])
        basis.append(vec)
    return basis


def realizable_null(p, e):
    src = [tuple(kconj(c) for c in v) if e == 1 else v for v in V]
    tgt = [V[p[i]] for i in range(6)]
    rowsm = []
    for i in range(6):
        for r in range(3):
            row = [ZERO] * 15
            for c in range(3):
                row[3 * r + c] = src[i][c]
            row[9 + i] = kneg(tgt[i][r])
            rowsm.append(row)
    basis = rref_null(rowsm, 15)
    if not basis:
        return False
    for combo in itertools.product(range(4), repeat=len(basis)):
        vec = [ZERO] * 15
        for coef, bvec in zip(combo, basis):
            if coef:
                cf = (Fraction(coef), Fraction(0))
                vec = [kadd(v, kmul(cf, x)) for v, x in zip(vec, bvec)]
        B = [[vec[3 * r + c] for c in range(3)] for r in range(3)]
        if kzero(det3(B)):
            continue
        lam = vec[9:]
        if any(kzero(x) for x in lam):
            continue
        ok = True
        for i in range(6):
            img = [kadd(kadd(kmul(B[r][0], src[i][0]),
                             kmul(B[r][1], src[i][1])),
                        kmul(B[r][2], src[i][2])) for r in range(3)]
            if img != [kmul(lam[i], tgt[i][r]) for r in range(3)]:
                ok = False
                break
        if ok:
            return True
    return False


ACCEPT = {0: set(), 1: set()}
agree = True
decided = 0
for e in (0, 1):
    for p in WPERMS:
        a1 = realizable_frame(p, e)
        a2 = realizable_null(p, e)
        if a1 != a2:
            agree = False
        decided += 1
        if a1:
            ACCEPT[e].add(p)
cert("C3 exactly 96 incidence cases decided, projective-frame and "
     "RREF-nullspace methods agree on every case, and no frame "
     "degeneracy occurred",
     decided == 96 and agree and not frame_degenerate)
stop_if_failed("C3")

G0 = {p for p in WPERMS if wchar(p) == (0, 0)}
cert("C4 the exponent-zero image equals the common character kernel "
     "ker(chi_Q) cap ker(chi_F) of order 12",
     ACCEPT[0] == G0 and len(ACCEPT[0]) == 12)
e1chars = {wchar(p) for p in ACCEPT[1]}
cert("C5 the exponent-one image has the inherited count with one "
     "common nonzero character equal to the published coset character",
     len(ACCEPT[1]) == int(SEMI["EXPONENT_ONE_COUNT"])
     and len(e1chars) == 1
     and "(%d,%d)" % sorted(e1chars)[0] == SEMI["COSET_CHARACTER"])
GAMMA = ACCEPT[0] | ACCEPT[1]
cert("C6 Gamma_sl order equals the published order",
     len(GAMMA) == int(SEMI["GAMMA_SL_ORDER"]))


def orbits(perms, members):
    seen = set()
    out = []
    for s in sorted(members):
        if s in seen:
            continue
        orb = {compose(p, s) for p in perms}
        seen |= orb
        out.append(orb)
    return out


SL_ORBITS = orbits(sorted(GAMMA), CLASS)
cert("C7 the Gamma_sl selector orbits match the published count and "
     "sizes and are unions of published blocks along equal chi_Q chi_F",
     len(SL_ORBITS) == int(SEMI["SELECTOR_ORBIT_COUNT"])
     and ",".join(str(len(o)) for o in
                  sorted(SL_ORBITS, key=len, reverse=True))
     == SEMI["SELECTOR_ORBIT_SIZES"]
     and all(len({(FIBER[s][0] + FIBER[s][1]) % 2 for s in o}) == 1
             for o in SL_ORBITS))
stop_if_failed("C")

# ============================================================ stage D
# The information-bearing computation: translations, transports,
# closure, and the derived route. No expected values.
PERM_NR = compose(PERM_N, PERM_R)
INVOL = (("N", PERM_N), ("R", PERM_R), ("NR", PERM_NR))

cert("D1 the exact identity s o N = sigma_line o s holds for all 48",
     all(compose(s, PERM_N) == compose(SIGMA, s) for s in CLASS))

TRANS = {}
uniform_ok = True
for name, bperm in INVOL:
    diffs = {((FIBER[compose(s, bperm)][0] + FIBER[s][0]) % 2,
              (FIBER[compose(s, bperm)][1] + FIBER[s][1]) % 2)
             for s in CLASS}
    if len(diffs) != 1:
        uniform_ok = False
        TRANS[name] = None
    else:
        TRANS[name] = sorted(diffs)[0]
cert("D2 every structural involution translates the fibers uniformly "
     "across the class", uniform_ok and None not in TRANS.values())
stop_if_failed("D2")
cert("D3 the translation of NR is the sum of the translations of N "
     "and R",
     TRANS["NR"] == ((TRANS["N"][0] + TRANS["R"][0]) % 2,
                     (TRANS["N"][1] + TRANS["R"][1]) % 2))

TPORT = {}
tport_ok = True
for name, bperm in INVOL:
    verdicts = set()
    for s in CLASS:
        c = compose(s, compose(bperm, inverse(s)))
        if compose(c, SIGMA) != compose(SIGMA, c):
            tport_ok = False
            continue
        if wchar(c) != TRANS[name]:
            tport_ok = False
        if c in ACCEPT[0]:
            verdicts.add("REALIZABLE-E0")
        elif c in ACCEPT[1]:
            verdicts.add("REALIZABLE-E1")
        else:
            verdicts.add("NONREALIZABLE")
    if len(verdicts) != 1:
        tport_ok = False
        TPORT[name] = None
    else:
        TPORT[name] = sorted(verdicts)[0]
cert("D4 every transport centralizes sigma_line, carries the "
     "translation character of its involution, and has a uniform "
     "realizability verdict across the class",
     tport_ok and None not in TPORT.values())
stop_if_failed("D4")


def closure_orbits():
    seen = set()
    out = []
    for seed in sorted(CLASS):
        if seed in seen:
            continue
        orb = {seed}
        frontier = [seed]
        while frontier:
            s = frontier.pop()
            for p in sorted(GAMMA):
                t2 = compose(p, s)
                if t2 not in orb:
                    orb.add(t2)
                    frontier.append(t2)
            t2 = compose(s, PERM_R)
            if t2 not in orb:
                orb.add(t2)
                frontier.append(t2)
        seen |= orb
        out.append(orb)
    return out


EXT = closure_orbits()
EXT_SIZES = sorted((len(o) for o in EXT), reverse=True)

toggle = (TRANS["R"][0] + TRANS["R"][1]) % 2
if toggle == 1:
    route = "REVERSAL-TOGGLE"
    consistent = (len(EXT) == 1 and EXT_SIZES == [48])
else:
    route = "REVERSAL-SILENT"
    consistent = (len(EXT) == 2 and EXT_SIZES == [24, 24])
cert("D5 the derived route is consistent with the extended orbit "
     "partition (frozen table: toggle <-> one orbit of 48, silent <-> "
     "two orbits of 24)", consistent)
stop_if_failed("D")

# ==================================================== scientific block
print("SCIENTIFIC_RESULT_BEGIN")
print("ROUTE: " + route)
print("TRANSLATION_N: (%d,%d)" % TRANS["N"])
print("TRANSLATION_R: (%d,%d)" % TRANS["R"])
print("TRANSLATION_NR: (%d,%d)" % TRANS["NR"])
print("TRANSPORT_N: " + TPORT["N"])
print("TRANSPORT_R: " + TPORT["R"])
print("TRANSPORT_NR: " + TPORT["NR"])
print("EXTENDED_ORBIT_COUNT: %d" % len(EXT))
print("EXTENDED_ORBIT_SIZES: " + ",".join(str(x) for x in EXT_SIZES))
print("RESULT: PASS")
print("SCIENTIFIC_RESULT_END")
