#!/usr/bin/env python3
# C-TM-HANKEL-K4-SUBSTRATE-1 verifier
# Frozen against PREREG-C-TM-HANKEL-K4-SUBSTRATE-1.md
# sha256 130bd7649ccdeacd382c06080514782f85a59c9c46404a2c8ade7d736bb81b19
# Python standard library only. Exact integers only. No float anywhere.
# No wall clock, no hostname, no machine identifier.

import sys
from bisect import bisect_right
from math import comb

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS " + name)
    else:
        FAIL += 1
        print("FAIL " + name)


def pc(x):
    return bin(x).count("1")


def t(n):
    return -1 if (pc(n) & 1) else 1


def c_general(N, plist):
    supp = [p for p in plist if N % p == 0]
    m = len(supp)
    s = 0
    for A in range(1 << m):
        d = 1
        for i in range(m):
            if (A >> i) & 1:
                d *= supp[i]
        v = t(N // d)
        s += -v if (pc(A) & 1) else v
    return s


# ---------- exact linear algebra ----------

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
            jmax = min(i, len(C) - 1)
            for j in range(jmax + 1):
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
    if pos + neg + z != n:
        raise AssertionError("inertia count mismatch")
    return (neg, z, pos)


def inertia_flat(F, n):
    """Fraction-free leading principal minors on a flat n by n list.
    Returns None on a zero pivot, routing the caller to the characteristic
    polynomial path."""
    A = F[:]
    prev = 1
    neg = 0
    last = 1
    for k in range(n):
        piv = A[k * n + k]
        if piv == 0:
            return None
        if (piv > 0) != (last > 0):
            neg += 1
        last = piv
        if k == n - 1:
            break
        base_k = k * n
        for i in range(k + 1, n):
            base_i = i * n
            mik = A[base_i + k]
            if mik:
                for j in range(k + 1, n):
                    A[base_i + j] = (A[base_i + j] * piv
                                     - mik * A[base_k + j]) // prev
            else:
                for j in range(k + 1, n):
                    A[base_i + j] = (A[base_i + j] * piv) // prev
        prev = piv
    return (neg, 0, n - neg)


def inertia_safe(F, n):
    r = inertia_flat(F, n)
    if r is not None:
        return r
    A = [[F[i * n + j] for j in range(n)] for i in range(n)]
    return inertia_berk(A)


def inertia_two_paths(A):
    n = len(A)
    F = [A[i][j] for i in range(n) for j in range(n)]
    a = inertia_flat(F, n)
    b = inertia_berk(A)
    if a is not None and a != b:
        raise AssertionError("inertia path disagreement")
    return b


def matmul(A, B):
    n = len(A)
    m = len(B[0])
    l = len(B)
    return [[sum(A[i][x] * B[x][j] for x in range(l)) for j in range(m)]
            for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def W_matrix(M):
    return [[(1 << (pc(T) - pc(S))) if (S & T) == S else 0
             for T in range(M)] for S in range(M)]


# ---------- abstract substrate at general k ----------

def substrate(k):
    M = 1 << k
    allm = []
    for x in range(3 ** k):
        m = []
        y = x
        for _ in range(k):
            m.append(y % 3)
            y //= 3
        allm.append(tuple(reversed(m)))
    allm.sort(key=lambda m: sum(m[i] * 3 ** (k - 1 - i) for i in range(k)))
    free = [m for m in allm if max(m) == 2]
    fidx = {m: j for j, m in enumerate(free)}
    bval = {m: (1 if (sum(m) & 1) else -1) for m in allm if max(m) <= 1}
    K0 = [[0] * M for _ in range(M)]
    Mj = [[[0] * M for _ in range(M)] for _ in range(len(free))]
    for S in range(M):
        for T in range(M):
            m = tuple(((S >> i) & 1) + ((T >> i) & 1) for i in range(k))
            supp = [i for i in range(k) if m[i] >= 1]
            for A in range(1 << len(supp)):
                mm = list(m)
                for i in range(len(supp)):
                    if (A >> i) & 1:
                        mm[supp[i]] -= 1
                mm = tuple(mm)
                sgn = -1 if (pc(A) & 1) else 1
                if max(mm) <= 1:
                    K0[S][T] += sgn * bval[mm]
                else:
                    Mj[fidx[mm]][S][T] += sgn
    order = sorted(range(M), key=lambda S: (pc(S), S))
    return M, free, fidx, K0, Mj, order


def reduce_order(X, order):
    return [[X[a][b] for b in order] for a in order]


# ---------- gate A: the substrate split ----------

def weight2_presence(k):
    M, free, fidx, K0, Mj, order = substrate(k)
    W = W_matrix(M)
    Wt = transpose(W)
    nw2 = 1 + k + (k * (k - 1)) // 2
    present = []
    empty_clean = True
    for j in range(len(free)):
        N = reduce_order(matmul(Wt, matmul(Mj[j], W)), order)
        if any(N[0][b] != 0 or N[b][0] != 0 for b in range(M)):
            empty_clean = False
        present.append(any(N[a][b] != 0
                           for a in range(nw2) for b in range(nw2)))
    return free, present, empty_clean, nw2


def count_formula(k):
    s = 0
    for a in range(1, k + 1):
        for b in range(0, k - a + 1):
            if 2 * a + b <= 4:
                s += comb(k, a) * comb(k - a, b)
    return s


def gate_a():
    free3, present3, clean3, nw3 = weight2_presence(3)
    n3 = sum(1 for p in present3 if p)
    absent3 = sorted(set(tuple(sorted(m))
                         for m, p in zip(free3, present3) if not p))
    crit3 = all(p == (sum(m) <= 4) for m, p in zip(free3, present3))
    print("A k=3 control: cells=%d present=%d absent_types=%s" % (
        len(free3), n3, absent3))
    check("A.k3_control_19_cells_15_present",
          len(free3) == 19 and n3 == 15 and crit3
          and absent3 == [(1, 2, 2), (2, 2, 2)])
    free4, present4, clean4, nw4 = weight2_presence(4)
    n4 = sum(1 for p in present4 if p)
    crit4 = all(p == (sum(m) <= 4) for m, p in zip(free4, present4))
    absent4 = sorted(set(tuple(sorted(m))
                         for m, p in zip(free4, present4) if not p))
    print("A k=4: cells=%d weight2_directions=%d present=%d absent=%d" % (
        len(free4), nw4, n4, len(free4) - n4))
    print("A k=4 absent types: %s" % (absent4,))
    check("A.criterion_sum_le_4_exact_k4", crit4)
    check("A.counts_65_34_31",
          len(free4) == 65 and n4 == 34 and len(free4) - n4 == 31)
    check("A.empty_direction_carries_no_free_cell", clean3 and clean4)
    check("A.count_formula_reproduces_15_and_34",
          count_formula(3) == 15 and count_formula(4) == 34)


# ---------- the k = 4 table machinery ----------

M4, FREE4, FIDX4, K04, MJ4, ORDER4 = substrate(4)
NC = len(FREE4)

BASEFLAT = [0] * 256
for _a in range(16):
    for _b in range(16):
        _v = K04[_a][_b]
        for _j in range(NC):
            _v += MJ4[_j][_a][_b]
        BASEFLAT[_a * 16 + _b] = _v

NZ = []
for _j in range(NC):
    _lst = []
    for _a in range(16):
        for _b in range(16):
            if MJ4[_j][_a][_b]:
                _lst.append((_a * 16 + _b, 2 * MJ4[_j][_a][_b]))
    NZ.append(_lst)

TYPE_OF = [tuple(sorted(m)) for m in FREE4]
TYPES = sorted(set(TYPE_OF))
CELLS = {ty: [j for j in range(NC) if TYPE_OF[j] == ty] for ty in TYPES}
SIZE4 = [ty for ty in TYPES if len(CELLS[ty]) == 4]
SIZE6 = [ty for ty in TYPES if len(CELLS[ty]) == 6]
SIZE12 = [ty for ty in TYPES if len(CELLS[ty]) == 12]


def kflat(bits):
    F = BASEFLAT[:]
    b = bits
    while b:
        lb = b & (-b)
        j = lb.bit_length() - 1
        for idx, val in NZ[j]:
            F[idx] -= val
        b ^= lb
    return F


def klass(bits):
    return inertia_safe(kflat(bits), 16)


# ---------- S_4 invariant layer ----------

PERMS = []


def _build_perms(cur, rest):
    if not rest:
        PERMS.append(tuple(cur))
        return
    for i in range(len(rest)):
        _build_perms(cur + [rest[i]], rest[:i] + rest[i + 1:])


_build_perms([], [0, 1, 2, 3])
CELLPERM = [[FIDX4[tuple(m[sg[i]] for i in range(4))] for m in FREE4]
            for sg in PERMS]

OP = [(i, j) for i in range(4) for j in range(4) if i != j]
OPIDX = {p: i for i, p in enumerate(OP)}
OPPERM = [[OPIDX[(sg[i], sg[j])] for (i, j) in OP] for sg in PERMS]

CHAR = {"22": (2, 0, 2, -1, 0), "211": (3, -1, -1, 0, 1)}


def _cycle_class(sg):
    seen = [False] * 4
    shape = []
    for s in range(4):
        if not seen[s]:
            n = 0
            x = s
            while not seen[x]:
                seen[x] = True
                x = sg[x]
                n += 1
            shape.append(n)
    shape.sort()
    return {(1, 1, 1, 1): 0, (1, 1, 2): 1, (2, 2): 2,
            (1, 3): 3, (4,): 4}[tuple(shape)]


PCLS = [_cycle_class(sg) for sg in PERMS]

# canonical labels: size-4 orbit by the coordinate carrying the value that
# occurs once; size-6 orbit by the unordered pair of coordinates carrying
# the smallest value; size-12 orbit by the ordered pair of coordinates
# carrying the two values that occur once, smaller value first.
LAB4 = {}
for ty in SIZE4:
    rep = [v for v in set(ty) if list(ty).count(v) == 1][0]
    LAB4[ty] = [None] * 4
    for j in CELLS[ty]:
        m = FREE4[j]
        LAB4[ty][[x for x in range(4) if m[x] == rep][0]] = j
LAB6 = {}
for ty in SIZE6:
    lo = min(ty)
    LAB6[ty] = {}
    for j in CELLS[ty]:
        m = FREE4[j]
        LAB6[ty][tuple(sorted(x for x in range(4) if m[x] == lo))] = j
LAB12 = {}
for ty in SIZE12:
    _vals = sorted(set(ty))
    _single = [v for v in _vals if list(ty).count(v) == 1]
    LAB12[ty] = {}
    for j in CELLS[ty]:
        m = FREE4[j]
        ia = [x for x in range(4) if m[x] == _single[0]][0]
        ib = [x for x in range(4) if m[x] == _single[1]][0]
        LAB12[ty][(ia, ib)] = j


def _apply_char(u, lam):
    ch = CHAR[lam]
    out = [0] * 12
    for gi in range(24):
        w = ch[PCLS[gi]]
        if w == 0:
            continue
        pm = OPPERM[gi]
        for p in range(12):
            out[pm[p]] += w * u[p]
    return out


def invariant_vector(bits):
    """The declared canonical 109-entry S_4 invariant map: ten orbit sums,
    the Gram of the twelve [31] copies inside the standard part of Q^4, the
    Gram of the five [22] copies inside Q[ordered pairs], and the Gram of
    the three [211] copies there."""
    vals = [(-1 if (bits >> j) & 1 else 1) for j in range(NC)]
    sums = tuple(sum(vals[j] for j in CELLS[ty]) for ty in TYPES)
    std = []
    for ty in SIZE4:
        mu = [vals[LAB4[ty][i]] for i in range(4)]
        s = sum(mu)
        std.append([4 * mu[i] - s for i in range(4)])
    for ty in SIZE6:
        mu = [sum(vals[LAB6[ty][tuple(sorted((i, j)))]]
                  for j in range(4) if j != i) for i in range(4)]
        s = sum(mu)
        std.append([4 * mu[i] - s for i in range(4)])
    for ty in SIZE12:
        row = [sum(vals[LAB12[ty][(i, j)]] for j in range(4) if j != i)
               for i in range(4)]
        col = [sum(vals[LAB12[ty][(i, j)]] for i in range(4) if i != j)
               for j in range(4)]
        for mu in (row, col):
            s = sum(mu)
            std.append([4 * mu[i] - s for i in range(4)])
    g31 = []
    for a in range(len(std)):
        for b in range(a, len(std)):
            g31.append(sum(std[a][i] * std[b][i] for i in range(4)))
    op22 = []
    for ty in SIZE6:
        u = [0] * 12
        for p, (i, j) in enumerate(OP):
            u[p] = vals[LAB6[ty][tuple(sorted((i, j)))]]
        op22.append(u)
    for ty in SIZE12:
        u = [0] * 12
        for p, (i, j) in enumerate(OP):
            u[p] = vals[LAB12[ty][(i, j)]]
        op22.append(u)
    q22 = [_apply_char(u, "22") for u in op22]
    g22 = []
    for a in range(len(op22)):
        for b in range(a, len(op22)):
            g22.append(sum(q22[a][p] * op22[b][p] for p in range(12)))
    op211 = []
    for ty in SIZE12:
        u = [0] * 12
        for p, (i, j) in enumerate(OP):
            u[p] = vals[LAB12[ty][(i, j)]]
        op211.append(u)
    q211 = [_apply_char(u, "211") for u in op211]
    g211 = []
    for a in range(len(op211)):
        for b in range(a, len(op211)):
            g211.append(sum(q211[a][p] * op211[b][p] for p in range(12)))
    return sums + tuple(g31) + tuple(g22) + tuple(g211)


def permute_bits(bits, gi):
    pm = CELLPERM[gi]
    out = 0
    for j in range(NC):
        if (bits >> j) & 1:
            out |= 1 << pm[j]
    return out


# ---------- the frozen search domain ----------

def lcg_tables(count):
    x = 1
    mod = 1 << 64
    out = []
    for _ in range(count):
        x = (6364136223846793005 * x + 1442695040888963407) % mod
        lo = x % (1 << 33)
        x = (6364136223846793005 * x + 1442695040888963407) % mod
        hi = x % (1 << 32)
        out.append(lo + (hi << 33))
    return out


def k3_embeddings():
    """The k = 3 canonical falsifier sign pattern of 147965 = 5.101.293
    embedded on each 3-subset of the four coordinates, remaining cells +1."""
    P3 = [5, 101, 293]
    out = []
    subsets = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    for sub in subsets:
        bits = 0
        for j, m in enumerate(FREE4):
            rest = [x for x in range(4) if x not in sub]
            if any(m[x] != 0 for x in rest):
                continue
            n = 1
            for pos, coord in enumerate(sub):
                n *= P3[pos] ** m[coord]
            if t(n) == -1:
                bits |= 1 << j
        out.append(bits)
    return out


def gate_bcd():
    balanced = (8, 0, 8)
    tables = lcg_tables(2000)
    tables = tables + [0, (1 << NC) - 1] + k3_embeddings()
    print("B domain: %d tables (2000 seeded, all-plus, all-minus, "
          "4 k=3 embeddings)" % len(tables))
    first_of_type = {ty: min(CELLS[ty]) for ty in TYPES}
    rel = {}
    lin = None
    quad = None
    class_hist = {}
    two_path_checked = 0
    for bits in tables:
        base = klass(bits)
        class_hist[base] = class_hist.get(base, 0) + 1
        for ty in TYPES:
            if ty in rel:
                continue
            j = first_of_type[ty]
            other = klass(bits ^ (1 << j))
            if other != base:
                rel[ty] = (bits, j, base, other)
        if lin is None or quad is None:
            for ty in TYPES:
                plus = None
                minus = None
                for j in CELLS[ty]:
                    if (bits >> j) & 1:
                        if minus is None:
                            minus = j
                    else:
                        if plus is None:
                            plus = j
                if plus is None or minus is None:
                    continue
                nb = bits ^ (1 << plus) ^ (1 << minus)
                other = klass(nb)
                if other == base:
                    continue
                if lin is None:
                    lin = (bits, nb, ty, base, other)
                if quad is None:
                    if invariant_vector(bits) == invariant_vector(nb):
                        quad = (bits, nb, ty, base, other)
    for ty in sorted(rel):
        bits, j, b0, b1 = rel[ty]
        cell = FREE4[j]
        print("B relevance type=%s cell=%d%d%d%d base=%s flipped=%s" % (
            "".join(str(x) for x in ty), cell[0], cell[1], cell[2], cell[3],
            "".join(str(x) for x in b0), "".join(str(x) for x in b1)))
        f0 = kflat(bits)
        f1 = kflat(bits ^ (1 << j))
        A0 = [[f0[a * 16 + b] for b in range(16)] for a in range(16)]
        A1 = [[f1[a * 16 + b] for b in range(16)] for a in range(16)]
        if inertia_two_paths(A0) != b0 or inertia_two_paths(A1) != b1:
            check("B.witness_two_path_confirmation_type_%s" % (ty,), False)
        else:
            two_path_checked += 1
    print("B relevant types found: %d of %d" % (len(rel), len(TYPES)))
    print("B open types: %s" % (sorted(set(TYPES) - set(rel)),))
    check("B.every_reported_witness_two_path_confirmed",
          two_path_checked == len(rel))
    hist = sorted(class_hist.items())
    print("B class histogram over the domain: %s" % (
        [("".join(str(x) for x in c), n) for c, n in hist],))
    print("B balanced share: %d of %d" % (
        class_hist.get(balanced, 0), len(tables)))
    rep_ok = True
    for cl, _n in hist:
        wit = next(b for b in tables if klass(b) == cl)
        f = kflat(wit)
        A = [[f[a * 16 + b] for b in range(16)] for a in range(16)]
        if inertia_berk(A) != cl:
            rep_ok = False
    check("B.every_observed_class_confirmed_by_char_poly_path", rep_ok)
    if lin is None:
        print("C linear collision: NOT FOUND in the declared domain")
        check("C.reported_only_if_found", True)
    else:
        b0, b1, ty, i0, i1 = lin
        s0 = invariant_vector(b0)[:10]
        s1 = invariant_vector(b1)[:10]
        print("C linear collision type=%s sums=%s inertia %s vs %s" % (
            "".join(str(x) for x in ty), s0,
            "".join(str(x) for x in i0), "".join(str(x) for x in i1)))
        print("C tables 0x%017x 0x%017x" % (b0, b1))
        check("C.collision_sums_identical_inertia_differs",
              s0 == s1 and i0 != i1)
    if quad is None:
        print("Q quadratic collision: NOT FOUND in the declared domain; "
              "no sufficiency conclusion is drawn")
        check("Q.no_claim_without_witness", True)
    else:
        b0, b1, ty, i0, i1 = quad
        print("Q quadratic collision type=%s inertia %s vs %s" % (
            "".join(str(x) for x in ty),
            "".join(str(x) for x in i0), "".join(str(x) for x in i1)))
        print("Q tables 0x%017x 0x%017x" % (b0, b1))
        check("Q.collision_invariants_identical_inertia_differs",
              invariant_vector(b0) == invariant_vector(b1) and i0 != i1)
    probe = tables[:8]
    ok_inv = True
    for bits in probe:
        base = invariant_vector(bits)
        if len(base) != 109:
            ok_inv = False
        for gi in range(24):
            if invariant_vector(permute_bits(bits, gi)) != base:
                ok_inv = False
    check("Q.invariant_map_has_109_entries_and_is_S4_invariant", ok_inv)


# ---------- gate E: real extremal quadruples ----------

def evil_primes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= limit:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [p for p in range(3, limit + 1, 2) if sieve[p] and t(p) == 1]


def block_inertia(P):
    M = 1 << len(P)
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        nS[x] = nS[x ^ lb] * P[lb.bit_length() - 1]
    K = [[c_general(nS[S] * nS[T], P) for T in range(M)] for S in range(M)]
    return inertia_two_paths(K)


def is_extremal(P):
    M = 1 << len(P)
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        nS[x] = nS[x ^ lb] * P[lb.bit_length() - 1]
    return all(t(nS[x]) == (1 if (pc(x) & 1) else -1) for x in range(M))


def gate_e():
    LIMIT = 10 ** 8
    ev = evil_primes(LIMIT // (3 * 5 * 17))
    quads = []
    np = len(ev)
    for a in range(np):
        p = ev[a]
        if p ** 4 > LIMIT:
            break
        for b in range(a + 1, np):
            q = ev[b]
            if p * q * q * q > LIMIT:
                break
            if t(p * q) != -1:
                continue
            for c in range(b + 1, np):
                r = ev[c]
                if p * q * r * r > LIMIT:
                    break
                if t(p * r) != -1 or t(q * r) != -1 or t(p * q * r) != 1:
                    continue
                hi = LIMIT // (p * q * r)
                top = bisect_right(ev, hi)
                for d in range(c + 1, top):
                    s = ev[d]
                    if (t(p * s) == -1 and t(q * s) == -1 and t(r * s) == -1
                            and t(p * q * s) == 1 and t(p * r * s) == 1
                            and t(q * r * s) == 1
                            and t(p * q * r * s) == -1):
                        quads.append((p, q, r, s))
    balanced = (8, 0, 8)
    nbal = 0
    fails = []
    for P in quads:
        if not is_extremal(list(P)):
            fails.append((P, None))
            continue
        i = block_inertia(list(P))
        if i == balanced:
            nbal += 1
        else:
            fails.append((P, i))
    print("E extremal quadruples with n <= 10^8: %d" % len(quads))
    if quads:
        print("E smallest: %s n=%d" % (
            quads[0], quads[0][0] * quads[0][1] * quads[0][2] * quads[0][3]))
    print("E balanced NEG 8 ZERO 0 POS 8: %d; nonbalanced: %d"
          % (nbal, len(fails)))
    for P, i in fails[:8]:
        print("E NONBALANCED %s n=%d inertia=%s" % (
            P, P[0] * P[1] * P[2] * P[3],
            "none" if i is None else "".join(str(x) for x in i)))
    check("E.every_quadruple_certified_extremal_and_two_path",
          all(i is not None for _, i in fails))
    ext = []
    for s in range(3, 20001, 2):
        if s in (5, 101, 293):
            continue
        pr = True
        d = 3
        while d * d <= s:
            if s % d == 0:
                pr = False
                break
            d += 2
        if not pr:
            continue
        P = sorted([5, 101, 293, s])
        if is_extremal(P):
            ext.append((s, block_inertia(P)))
    print("E extensions of the k=3 falsifier {5,101,293} with s <= 20000: %d"
          % len(ext))
    for s, i in ext[:8]:
        print("E EXTENSION s=%d inertia=%s" % (
            s, "".join(str(x) for x in i)))
    check("E.extension_scan_completed", True)


def main():
    print("C-TM-HANKEL-K4-SUBSTRATE-1 verifier")
    print("INERTIA_ORDER NEG ZERO POS; balanced at k=4 is NEG 8 ZERO 0 POS 8")
    gate_a()
    gate_bcd()
    gate_e()
    print("SUMMARY PASS=%d FAIL=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
