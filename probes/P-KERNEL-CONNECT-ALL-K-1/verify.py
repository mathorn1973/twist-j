#!/usr/bin/env python3
# C-KERNEL-CONNECT-ALL-K-1 verifier. In-project incubation lane. No authority.
#
# Target row: KERNEL-CONNECT-ALL-K [H] (public canon v8, section 3):
# "for every k >= 2 the generator set {a, c, d, e} with the two way CSUM
# ring coupling connects (F_5^6)^k into one component."
#
# Frozen model (the carrier): cells indexed by Z_k, cell space F_5^6,
# moves are the four diagonal letters D_g (g applied at every cell
# simultaneously, the diagonal action of the registered wedge cluster
# KERNEL-WEDGE-*) and, for every ring index i, the two CSUM transvections
# R_i: x_{i+1} += x_i and L_i: x_i += x_{i+1} (indices mod k). At k = 2
# this move set degenerates to the registered pair transvections. The
# per-cell letter variant contains every diagonal letter as a product, so
# one-component for the diagonal model implies it for the per-cell model.
#
# Decision structure (frozen): let Gamma = <M_a, M_c, M_d, M_e> and let
# U be the smallest Gamma-invariant subspace of F_5^6 containing the
# letter translations {v_c, v_d, v_e} (v_g = g(0)). Lemma chain proved in
# C-KERNEL-CONNECT-ALL-K-1.md:
#   confinement: every G_k-orbit of 0 lies in F_5^k tensor U (all k >= 1);
#   extraction:  [D_g, S_Q] = t_{(1 - Q 1) tensor v_g} for Q in the ring
#                transvection group, g in {c, d, e};
#   transport:   conjugation by letters closes the cell factor to U, ring
#                transvections reach every delta_i (k >= 2);
# hence: U = F_5^6  <=>  one component at every k >= 2, and
#        U ne F_5^6  =>  more than one component at every k >= 1.
# The verifier decides dim U exactly and certifies the finite lemma
# instances. PASS on all gates realizes the positive branch.
#
# Exact arithmetic only: integers mod 5, no floats anywhere, standard
# library only, deterministic, run from anywhere, target under 120 s with
# LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

import sys

P5 = 5
CD = 6                     # cell dimension
NST = P5 ** CD             # 15625 single-cell states

# ----------------------------------------------------------------------
# the five kernel generators, verbatim forms of the public witness
# reproduce/kernel-connectivity/verify.py (KERNEL-WEDGE-AFFINITY [T])
S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x):
    p1, p4, p1p, p4p, q, t = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-t) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, t = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + t * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + t * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + t * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + t * U_VEC[3]) % 5,
            (1 - q) % 5, (-t) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS5 = (("a", gen_a), ("b", gen_b), ("c", gen_c), ("d", gen_d),
         ("e", gen_e))
LETTERS = ("a", "c", "d", "e")     # the row's generator set, b excluded
AFFINE_LETTERS = ("c", "d", "e")   # strictly affine sector

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


def dec(i):
    out = []
    for _ in range(6):
        out.append(i % 5)
        i //= 5
    return tuple(out)


def enc(x):
    i = 0
    for k in range(5, -1, -1):
        i = i * 5 + x[k]
    return i


# ------------------------------------------------ exact F5 linear algebra
def matvec(M, x):
    return tuple(sum(M[r][j] * x[j] for j in range(len(x))) % 5
                 for r in range(len(M)))


def matmul(A, B):
    n = len(A)
    m = len(B[0])
    kk = len(B)
    return tuple(tuple(sum(A[r][j] * B[j][c] for j in range(kk)) % 5
                       for c in range(m)) for r in range(n))


def identity(n):
    return tuple(tuple(1 if r == c else 0 for c in range(n))
                 for r in range(n))


def f5_rank(rows):
    m = [list(r) for r in rows]
    if not m:
        return 0
    rank = 0
    col = 0
    ncols = len(m[0])
    while rank < len(m) and col < ncols:
        piv = next((r for r in range(rank, len(m)) if m[r][col] % 5), None)
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = pow(m[rank][col], 3, 5)
        m[rank] = [(x * inv) % 5 for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col] % 5:
                f = m[r][col]
                m[r] = [(x - f * y) % 5 for x, y in zip(m[r], m[rank])]
        rank += 1
        col += 1
    return rank


def f5_det(mat):
    m = [list(r) for r in mat]
    n = len(m)
    det = 1
    for col in range(n):
        piv = next((r for r in range(col, n) if m[r][col] % 5), None)
        if piv is None:
            return 0
        if piv != col:
            m[col], m[piv] = m[piv], m[col]
            det = (-det) % 5
        det = (det * m[col][col]) % 5
        inv = pow(m[col][col], 3, 5)
        m[col] = [(x * inv) % 5 for x in m[col]]
        for r in range(col + 1, n):
            f = m[r][col]
            if f % 5:
                m[r] = [(x - f * y) % 5 for x, y in zip(m[r], m[col])]
    return det % 5


def f5_solve(B, y):
    # solve B z = y, B square invertible, exact Gauss-Jordan mod 5
    n = len(B)
    m = [list(B[r]) + [y[r] % 5] for r in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if m[r][col] % 5)
        m[col], m[piv] = m[piv], m[col]
        inv = pow(m[col][col], 3, 5)
        m[col] = [(x * inv) % 5 for x in m[col]]
        for r in range(n):
            if r != col and m[r][col] % 5:
                f = m[r][col]
                m[r] = [(x - f * yv) % 5 for x, yv in zip(m[r], m[col])]
    return tuple(m[r][n] for r in range(n))


# deterministic LCG, integers only
class LCG(object):
    def __init__(self, seed):
        self.s = seed % (2 ** 31)

    def next(self):
        self.s = (1103515245 * self.s + 12345) % (2 ** 31)
        return self.s

    def digit5(self):
        return (self.next() >> 16) % 5


# ---------------------------------------------------------------- gates
def main():
    # ---------------- 01 VERBATIM: affine forms, involutions, det 1
    MG = {}
    VG = {}
    ok = True
    for name, g in GENS5:
        v = tuple(x % 5 for x in g((0, 0, 0, 0, 0, 0)))
        cols = []
        for i in range(6):
            e = [0] * 6
            e[i] = 1
            gi = g(tuple(e))
            cols.append(tuple((gi[r] - v[r]) % 5 for r in range(6)))
        M = tuple(tuple(cols[i][r] for i in range(6)) for r in range(6))
        okg = True
        for idx in range(NST):
            x = dec(idx)
            gx = g(x)
            if tuple((sum(M[r][j] * x[j] for j in range(6)) + v[r]) % 5
                     for r in range(6)) != tuple(z % 5 for z in gx):
                okg = False
                break
            if tuple(z % 5 for z in g(gx)) != x:
                okg = False
                break
        ok &= okg
        ok &= f5_det(M) == 1
        MG[name] = M
        VG[name] = v
    ok &= not any(VG["a"]) and not any(VG["b"])
    ok &= all(any(VG[n]) for n in AFFINE_LETTERS)
    ok &= VG["c"] == (2, 1, 2, 1, 1, 0)
    ok &= VG["d"] == (2, 1, 3, 4, 1, 1)
    ok &= VG["e"] == (2, 1, 3, 4, 2, 1)
    check("VERBATIM",
          "all five kernel generators are the verbatim census maps,"
          " affine involutions g(x) = M_g x + v_g on all 15625 states"
          " with det M_g = 1; a, b linear; translations v_c, v_d, v_e"
          " as extracted", ok)

    # ---------------- 02 U-CLOSURE: the decision computation
    # U = smallest subspace containing {v_c, v_d, v_e} with M_g U = U
    # for g in {a, c, d, e}; provenance words recorded for gate 06.
    basis = []          # list of (vector, seed_letter, chain tuple)
    rows = []
    trace = []

    def try_add(vec, seed, chain):
        if f5_rank(rows + [list(vec)]) > len(rows):
            rows.append(list(vec))
            basis.append((tuple(z % 5 for z in vec), seed, chain))
            trace.append(len(rows))
            return True
        return False

    for h in AFFINE_LETTERS:
        try_add(VG[h], h, ())
    qi = 0
    while qi < len(basis) and len(rows) < 6:
        vec, seed, chain = basis[qi]
        qi += 1
        for gname in LETTERS:
            if len(rows) >= 6:
                break
            try_add(matvec(MG[gname], vec), seed, chain + (gname,))
    dimU = len(rows)
    ok = dimU == 6
    check("U-CLOSURE",
          "the Gamma closure of span{v_c, v_d, v_e} under"
          " {M_a, M_c, M_d, M_e} reaches dimension 6: U = F_5^6, the"
          " positive branch of the frozen dichotomy; growth trace"
          " %s" % ("-".join(str(t) for t in trace)), ok)

    # big-space builders -------------------------------------------------
    def big_letter(gname, k):
        n = CD * k
        M = [[0] * n for _ in range(n)]
        Mg = MG[gname]
        for cell in range(k):
            o = CD * cell
            for r in range(CD):
                for c in range(CD):
                    M[o + r][o + c] = Mg[r][c]
        v = tuple(VG[gname][r % CD] for r in range(n))
        return (tuple(tuple(rr) for rr in M), v)

    def big_coupling(src, dst, k):
        n = CD * k
        M = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
        for r in range(CD):
            M[CD * dst + r][CD * src + r] = 1
        return (tuple(tuple(rr) for rr in M), tuple(0 for _ in range(n)))

    def compose_seq(seq, k):
        # seq applied first to last; each item (M, v); net = last o ... o first
        n = CD * k
        Mn = identity(n)
        vn = tuple(0 for _ in range(n))
        for (M, v) in seq:
            Mn = matmul(M, Mn)
            vn = tuple((matvec(M, vn)[r] + v[r]) % 5 for r in range(n))
        return (Mn, vn)

    def comm_seq(h, i, k):
        # word for [D_h, S_Q] with Q = E_{i, i-1}(4): t_{delta_i tensor v_h}
        # map = D_h o S_Q o D_h o S_Q^{-1}; S_Q = R_{i-1}^4, S_Q^{-1} = R_{i-1}
        pre = (i - 1) % k
        Dh = big_letter(h, k)
        R = big_coupling(pre, i, k)
        return [R, Dh, R, R, R, R, Dh]

    def chain_seq(h, i, chain, k):
        # word for t_{delta_i tensor (M_chain v_h)}: conjugate comm word
        # by D_{g_1} ... D_{g_m} innermost-first
        inner = comm_seq(h, i, k)
        seq = list(inner)
        for gname in chain:
            Dg = big_letter(gname, k)
            seq = [Dg] + seq + [Dg]
        return seq

    # ---------------- 03 COMMUTATOR: exact pure-translation extraction
    ok = True
    for k in (2, 3, 4):
        n = CD * k
        idm = identity(n)
        for h in AFFINE_LETTERS:
            for i in range(k):
                M, v = compose_seq(comm_seq(h, i, k), k)
                exp = tuple(VG[h][r - CD * i] if CD * i <= r < CD * (i + 1)
                            else 0 for r in range(n))
                ok &= M == idm and v == exp
    check("COMMUTATOR",
          "for k = 2, 3, 4, every h in {c, d, e} and every cell i, the"
          " 7-move word D_h R_{i-1}^4 D_h R_{i-1} composes exactly to"
          " the pure translation t_{delta_i tensor v_h} (linear part"
          " the identity), realizing the extraction lemma", ok)

    # ---------------- 04 TRANSVECTION ORBIT: ring transvections reach
    # every nonzero vector of F_5^k, k = 2..6, exhaustive BFS
    ok = True
    orbit_sizes = []
    for k in range(2, 7):
        moves = []
        for i in range(k):
            moves.append((i, (i + 1) % k))
            moves.append(((i + 1) % k, i))
        start = tuple(1 for _ in range(k))
        seen = {start}
        frontier = [start]
        while frontier:
            nxt = []
            for u in frontier:
                for (src, dst) in moves:
                    w = list(u)
                    w[dst] = (w[dst] + u[src]) % 5
                    w = tuple(w)
                    if w not in seen:
                        seen.add(w)
                        nxt.append(w)
            frontier = nxt
        orbit_sizes.append(len(seen))
        ok &= len(seen) == P5 ** k - 1
    check("TRANSVECTION",
          "the two-way ring transvections acting on F_5^k reach every"
          " nonzero vector from the all-ones vector, exhaustively for"
          " k = 2..6 (orbit sizes %s), the finite instances of the"
          " all-k transitivity lemma" %
          ",".join(str(s) for s in orbit_sizes), ok)

    # ---------------- 05 SPAN: delta_i tensor basis(U) spans F_5^(6k)
    ok = True
    for k in (2, 3):
        vecs = []
        for i in range(k):
            for (bv, _s, _c) in basis:
                vecs.append([bv[r - CD * i] if CD * i <= r < CD * (i + 1)
                             else 0 for r in range(CD * k)])
        ok &= f5_rank(vecs) == CD * k
    check("SPAN",
          "the extracted translations delta_i tensor b_j, b_j the six"
          " closure basis vectors, span all of F_5^(6k) at k = 2 and"
          " k = 3: the translation subgroup is everything", ok)

    # ---------------- 06 REDUCTION: end-to-end constructive connectivity
    # random states reduced to zero by explicit generator words, applied
    # state-by-state (independent of matrix composition)
    def apply_letter_state(state, gname, k):
        g = dict(GENS5)[gname]
        return tuple(tuple(z % 5 for z in g(state[i])) for i in range(k))

    def apply_coupling_state(state, src, dst, k):
        cells = [list(c) for c in state]
        for r in range(CD):
            cells[dst][r] = (cells[dst][r] + cells[src][r]) % 5
        return tuple(tuple(c) for c in cells)

    def apply_seq_state(state, ops, k):
        for op in ops:
            if op[0] == "L":
                state = apply_letter_state(state, op[1], k)
            else:
                state = apply_coupling_state(state, op[1], op[2], k)
        return state

    def comm_ops(h, i, k):
        pre = (i - 1) % k
        return ([("C", pre, i), ("L", h), ("C", pre, i), ("C", pre, i),
                 ("C", pre, i), ("C", pre, i), ("L", h)])

    def chain_ops(h, i, chain, k):
        ops = comm_ops(h, i, k)
        for gname in chain:
            ops = [("L", gname)] + ops + [("L", gname)]
        return ops

    # validate each word once by matrix composition, then push states
    Bcell = tuple(tuple(basis[j][0][r] for j in range(6))
                  for r in range(6))  # columns = basis vectors
    ok = True
    rng = LCG(20260718)
    for k in (2, 3, 5):
        words = {}
        n = CD * k
        idm = identity(n)
        for i in range(k):
            for j in range(6):
                bv, seed, chain = basis[j]
                seq = chain_seq(seed, i, chain, k)
                M, v = compose_seq(seq, k)
                exp = tuple(bv[r - CD * i] if CD * i <= r < CD * (i + 1)
                            else 0 for r in range(n))
                ok &= M == idm and v == exp
                words[(i, j)] = chain_ops(seed, i, chain, k)
        for _trial in range(40):
            state = tuple(tuple(rng.digit5() for _ in range(CD))
                          for _ in range(k))
            target = state
            for i in range(k):
                need = tuple((-target[i][r]) % 5 for r in range(CD))
                coef = f5_solve(Bcell, need)
                for j in range(6):
                    for _rep in range(coef[j]):
                        target = apply_seq_state(target, words[(i, j)], k)
            ok &= target == tuple(tuple(0 for _ in range(CD))
                                  for _ in range(k))
    check("REDUCTION",
          "for k = 2, 3, 5, forty deterministic pseudo-random states"
          " each reduce exactly to the zero state by explicit generator"
          " words (every word first verified as a pure translation by"
          " exact composition): any state connects to any state", ok)

    # ---------------- 07 K1-SHARPNESS: the k = 1 boundary is real
    tables = {}
    for name, g in GENS5:
        tables[name] = [enc(tuple(z % 5 for z in g(dec(i))))
                        for i in range(NST)]

    def components(subset):
        parent = list(range(NST))

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for name in subset:
            tab = tables[name]
            for i in range(NST):
                ri = find(i)
                rj = find(tab[i])
                if ri != rj:
                    parent[ri] = rj
        return sum(1 for i in range(NST) if find(i) == i)

    c_acde = components("acde")
    c_abcde = components("abcde")
    ok = c_acde == 9 and c_abcde == 1
    check("K1-SHARP",
          "the single cell census is reproduced: {a, c, d, e} alone"
          " leaves 9 components at k = 1 and the full verb {a, b, c,"
          " d, e} leaves 1; the k >= 2 bound of the theorem is sharp"
          " and the coupling is doing real work", ok)

    # ---------------- 08 TENSOR SHAPE: linear parts factor as P tensor M
    ok = True
    rng2 = LCG(777)
    k = 2
    n = CD * k
    pool = []
    for gname in LETTERS:
        pool.append(big_letter(gname, k))
    pool.append(big_coupling(0, 1, k))
    pool.append(big_coupling(1, 0, k))
    for _trial in range(60):
        ln = 3 + (rng2.next() % 8)
        seq = [pool[rng2.next() % len(pool)] for _ in range(ln)]
        M, _v = compose_seq(seq, k)
        blocks = [[tuple(tuple(M[CD * bi + r][CD * bj + c]
                               for c in range(CD)) for r in range(CD))
                   for bj in range(k)] for bi in range(k)]
        ref = None
        for bi in range(k):
            for bj in range(k):
                if any(any(row) for row in blocks[bi][bj]):
                    ref = blocks[bi][bj]
                    break
            if ref:
                break
        rp = next((r, c) for r in range(CD) for c in range(CD)
                  if ref[r][c])
        Pmat = []
        okw = True
        for bi in range(k):
            prow = []
            for bj in range(k):
                blk = blocks[bi][bj]
                lam = (blk[rp[0]][rp[1]] * pow(ref[rp[0]][rp[1]], 3, 5)) % 5
                okw &= all(blk[r][c] == (lam * ref[r][c]) % 5
                           for r in range(CD) for c in range(CD))
                prow.append(lam)
            Pmat.append(tuple(prow))
        okw &= f5_det(tuple(Pmat)) != 0
        ok &= okw
    check("TENSOR",
          "sixty deterministic pseudo-random generator words at k = 2"
          " all have linear part of the exact tensor form P tensor M"
          " with P invertible, the structural fact behind the"
          " confinement lemma and the negative branch", ok)

    # ------------------------------------------------------------- report
    print("C-KERNEL-CONNECT-ALL-K-1 verifier (exact arithmetic, stdlib only)")
    print("model: diagonal letters {a, c, d, e} plus two-way CSUM ring"
          " transvections on (F_5^6)^k")
    print("decision: U = Gamma-closure of span{v_c, v_d, v_e};"
          " U = F_5^6 gives one component for every k >= 2")
    print()
    passed = 0
    for i, (name, okv) in enumerate(CHECKS, 1):
        tag = "PASS" if okv else "FAIL"
        if okv:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
