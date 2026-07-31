#!/usr/bin/env python3
# P-ENTROPY-RG-RETURN-1 exact verifier. The fixed-point tower and the
# multiplier spectra of the renormalized block maps Phi^(k)_eps on the
# recurrent core of the F_5^6 kernel, dyadic scales k = 0..14, both letters.
# Exact integer arithmetic, Python standard library only, no float anywhere,
# no filesystem writes, one process. See PREREG.md in this directory;
# gates G01 to G13.

import sys

S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-r) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + r * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + r * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + r * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + r * U_VEC[3]) % 5,
            (1 - q) % 5, (-r) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)

N = 15625
K_MAX = 14
INV5 = (0, 1, 3, 2, 4)
IDM = tuple(1 if i == j else 0 for i in range(6) for j in range(6))
MINUS_I = tuple((-v) % 5 for v in IDM)

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


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


STATES = [dec(i) for i in range(N)]
ZTAB = [sum(s) % 5 for s in STATES]

_MEMO = {}


def mm(A, B):
    key = (A, B)
    val = _MEMO.get(key)
    if val is not None:
        return val
    out = []
    ap = out.append
    for i in range(0, 36, 6):
        a0, a1, a2, a3, a4, a5 = A[i:i + 6]
        for j in range(6):
            ap((a0 * B[j] + a1 * B[6 + j] + a2 * B[12 + j]
                + a3 * B[18 + j] + a4 * B[24 + j] + a5 * B[30 + j]) % 5)
    val = tuple(out)
    _MEMO[key] = val
    return val


def msub(A, B):
    return tuple((A[i] - B[i]) % 5 for i in range(36))


def mvec(A, v):
    return tuple(sum(A[6 * i + k] * v[k] for k in range(6)) % 5
                 for i in range(6))


def det6(A):
    m = [list(A[6 * i:6 * i + 6]) for i in range(6)]
    det = 1
    for c in range(6):
        piv = -1
        for r in range(c, 6):
            if m[r][c] % 5:
                piv = r
                break
        if piv == -1:
            return 0
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            det = (-det) % 5
        det = (det * m[c][c]) % 5
        inv = INV5[m[c][c] % 5]
        for r in range(c + 1, 6):
            f = (m[r][c] * inv) % 5
            if f:
                for cc in range(c, 6):
                    m[r][cc] = (m[r][cc] - f * m[c][cc]) % 5
    return det % 5


def polymul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] = (out[i + j] + a * b) % 5
    return tuple(out)


def polysub(p, q):
    n = max(len(p), len(q))
    return tuple(((p[i] if i < len(p) else 0)
                  - (q[i] if i < len(q) else 0)) % 5 for i in range(n))


def polyscal(p, s):
    return tuple((a * s) % 5 for a in p)


def charpoly(M):
    # det(xI - M) over F_5, monic of degree 6, coefficients c0..c6 low
    # degree first. Hessenberg reduction by similarity, then the standard
    # leading-principal-minor recurrence.
    H = [[M[6 * i + j] % 5 for j in range(6)] for i in range(6)]
    n = 6
    for j in range(n - 2):
        piv = -1
        for i in range(j + 1, n):
            if H[i][j] % 5:
                piv = i
                break
        if piv == -1:
            continue
        if piv != j + 1:
            H[j + 1], H[piv] = H[piv], H[j + 1]
            for r in range(n):
                H[r][j + 1], H[r][piv] = H[r][piv], H[r][j + 1]
        inv = INV5[H[j + 1][j] % 5]
        for i in range(j + 2, n):
            f = (H[i][j] * inv) % 5
            if f:
                for cc in range(n):
                    H[i][cc] = (H[i][cc] - f * H[j + 1][cc]) % 5
                for r in range(n):
                    H[r][j + 1] = (H[r][j + 1] + f * H[r][i]) % 5
    polys = [(1,)]
    for m in range(1, n + 1):
        pm = polymul(polys[m - 1], ((-H[m - 1][m - 1]) % 5, 1))
        prod = 1
        for k in range(m - 1, 0, -1):
            prod = (prod * H[k][k - 1]) % 5
            term = (H[k - 1][m - 1] * prod) % 5
            if term:
                pm = polysub(pm, polyscal(polys[k - 1], term))
        polys.append(pm)
    out = list(polys[n]) + [0] * (7 - len(polys[n]))
    return tuple(a % 5 for a in out[:7])


def subst_word(eps, k):
    w = [eps]
    for _ in range(k):
        nw = []
        for a in w:
            nw.extend((a, 1 - a))
        w = nw
    return w


def main():
    # ---------------- branch maps and selector ----------------
    F = [[0] * N, [0] * N]
    SEL = [[0] * N, [0] * N]
    for t in (0, 1):
        Ft = F[t]
        St = SEL[t]
        for i in range(N):
            g = (ZTAB[i] + 2 * t) % 5
            St[i] = g
            Ft[i] = enc(GENS[g](STATES[i]))

    tm = [bin(n).count("1") & 1 for n in range(1024)]

    # ---------------- G01 census, warmup 400, window 300 ----------------
    warm = [F[tm[n]] for n in range(400)]
    wind = [F[tm[n]] for n in range(400, 700)]
    sigs = []
    seen = set()
    for seed in range(N):
        s = seed
        for T in warm:
            s = T[s]
        w1 = set()
        for T in wind:
            w1.add(s)
            s = T[s]
        fs = frozenset(w1)
        if fs not in seen:
            seen.add(fs)
            sigs.append(fs)
    sizes = {}
    comp_of = {}
    disjoint = True
    for ci, fs in enumerate(sigs):
        sizes[len(fs)] = sizes.get(len(fs), 0) + 1
        for x in fs:
            if x in comp_of:
                disjoint = False
            comp_of[x] = ci
    R = sorted(comp_of)
    Rset = set(R)
    singles = [ci for ci, fs in enumerate(sigs) if len(fs) == 10]
    check("G01 CENSUS      recurrent core 6250 on 313 components,"
          " sizes 312 x 20 + 1 x 10, pairwise disjoint",
          len(R) == 6250 and len(sigs) == 313
          and sizes == {20: 312, 10: 1} and disjoint and len(singles) == 1)
    singlet = singles[0] if singles else -1

    # ---------------- G02 living halves ----------------
    H = [set(F[0][x] for x in R), set(F[1][x] for x in R)]
    check("G02 HALVES      H_0 and H_1 disjoint, 3125 each, union the core,"
          " and F_t maps the core into the core",
          len(H[0]) == 3125 and len(H[1]) == 3125
          and not (H[0] & H[1]) and (H[0] | H[1]) == Rset
          and H[0] <= Rset and H[1] <= Rset)

    if not (CHECKS[0][1] and CHECKS[1][1]):
        print("P-ENTROPY-RG-RETURN-1 exact verifier")
        print()
        for i, (nm, okk) in enumerate(CHECKS, 1):
            print("%s %02d %s" % ("PASS" if okk else "FAIL", i, nm))
        print()
        print("GATES STOP the carrier audit failed; nothing below is"
              " evaluable")
        return 1

    # ---------------- G03, G04 generator linear parts ----------------
    LIN = []
    CST = []
    for g in GENS:
        c0 = g((0, 0, 0, 0, 0, 0))
        cols = []
        for j in range(6):
            ej = tuple(1 if i == j else 0 for i in range(6))
            gj = g(ej)
            cols.append(tuple((gj[i] - c0[i]) % 5 for i in range(6)))
        LIN.append(tuple(cols[j][i] for i in range(6) for j in range(6)))
        CST.append(tuple(v % 5 for v in c0))
    affine = True
    for x in STATES:
        for gi, g in enumerate(GENS):
            lhs = tuple(v % 5 for v in g(x))
            lin = mvec(LIN[gi], x)
            rhs = tuple((lin[i] + CST[gi][i]) % 5 for i in range(6))
            if lhs != rhs:
                affine = False
    check("G03 AFFINE      every generator equals its linear part plus its"
          " constant on all 15625 states", affine)
    check("G04 LINPARTS    every linear part is an involution of"
          " determinant 1", all(mm(L, L) == IDM and det6(L) == 1
                                for L in LIN))

    # ---------------- G05 characteristic polynomial self-tests ----------
    target = (4, 2, 0, 3, 0, 0, 1)
    comp = [[0] * 6 for _ in range(6)]
    for i in range(1, 6):
        comp[i][i - 1] = 1
    for i in range(6):
        comp[i][5] = (-target[i]) % 5
    compM = tuple(comp[i][j] for i in range(6) for j in range(6))
    p_plus = (1,)
    p_minus = (1,)
    for _ in range(6):
        p_plus = polymul(p_plus, (1, 1))
        p_minus = polymul(p_minus, (4, 1))
    p_plus = tuple(list(p_plus) + [0] * (7 - len(p_plus)))[:7]
    p_minus = tuple(list(p_minus) + [0] * (7 - len(p_minus)))[:7]
    check("G05 CHARPOLY    companion, identity and minus identity"
          " self-tests over F_5",
          charpoly(compM) == target and charpoly(IDM) == p_minus
          and charpoly(MINUS_I) == p_plus)

    # ---------------- the scale loop ----------------
    Ridx = {x: i for i, x in enumerate(R)}
    cur = [F[0][:], F[1][:]]
    curM = [[LIN[SEL[eps][x]] for x in R] for eps in (0, 1)]

    word_ok = True
    mult_ok = True
    realized = set()
    halving_ok = True
    halflaw_ok = True
    empty_ok = True
    return_ok = True
    k0_ok = True
    tower = []
    spectra = []
    nonempty_scales = []

    K0_STATE = (enc((1, 3, 4, 2, 1, 3)), enc((1, 3, 4, 2, 3, 3)))

    for k in range(K_MAX + 1):
        for eps in (0, 1):
            arr = cur[eps]
            img = len(set(arr[x] for x in R))
            halving_ok = halving_ok and img == 3125

            fixed_all = [x for x in range(N) if arr[x] == x]
            fix = [x for x in fixed_all if x in Rset]
            off = len(fixed_all) - len(fix)
            nsing = sum(1 for x in fix if comp_of.get(x) == singlet)
            ncomp = len(set(comp_of[x] for x in fix)) if fix else 0
            mults = [curM[eps][Ridx[x]] for x in fix]
            nident = sum(1 for M in mults if M == IDM)
            realized.update(mults)

            th = (eps + k) % 2
            halflaw_ok = halflaw_ok and all(x in H[th] for x in fix)

            if k == 0:
                k0_ok = (k0_ok and len(fix) == 1 and off == 125
                         and fix[0] == K0_STATE[eps]
                         and comp_of.get(fix[0]) == singlet
                         and mults == [MINUS_I])
            elif k % 4 == 1:
                return_ok = (return_ok and set(fix) == H[1 - eps]
                             and len(fix) == 3125
                             and all(M == IDM for M in mults)
                             and off == (3125 if k == 1 else 0))
            else:
                empty_ok = empty_ok and not fix and off == 0

            if fix:
                nonempty_scales.append(k)

            specs = {}
            for M in mults:
                cp = charpoly(M)
                specs[cp] = specs.get(cp, 0) + 1
            tower.append(
                "TOWER k=%2d eps=%d core_fix=%5d offcore=%5d image=%4d"
                " singlet=%3d components=%4d identity=%5d"
                % (k, eps, len(fix), off, img, nsing, ncomp, nident))
            for cp in sorted(specs):
                spectra.append(
                    "SPECTRUM k=%2d eps=%d count=%5d charpoly_c0..c6=%s"
                    % (k, eps, specs[cp],
                       ",".join(str(c) for c in cp)))
            if fix:
                spectra.append(
                    "SPECTRUM k=%2d eps=%d distinct_multipliers=%d"
                    % (k, eps, len(set(mults))))

            if k <= 6:
                w = subst_word(eps, k)
                arrw = list(range(N))
                for th2 in w:
                    Ft = F[th2]
                    arrw = [Ft[y] for y in arrw]
                word_ok = word_ok and arrw == arr
            if k <= 8:
                w = subst_word(eps, k)
                for x in fix[:10]:
                    m = IDM
                    y = x
                    for th2 in w:
                        m = mm(LIN[SEL[th2][y]], m)
                        y = F[th2][y]
                    mult_ok = (mult_ok and y == x
                               and m == curM[eps][Ridx[x]])

        if k < K_MAX:
            nxt = []
            nxtM = []
            for eps in (0, 1):
                a_first = cur[eps]
                a_then = cur[1 - eps]
                nxt.append([a_then[a_first[x]] for x in range(N)])
                Mf = curM[eps]
                Mt = curM[1 - eps]
                nxtM.append([mm(Mt[Ridx[a_first[x]]], Mf[i])
                             for i, x in enumerate(R)])
            cur = nxt
            curM = nxtM

    check("G06 WORD        the doubling recursion equals the literal"
          " substitution-word composition, k = 0..6, both letters", word_ok)
    check("G07 MULTWALK    the multiplier recursion equals the literal"
          " ordered substep product at fixed states, k = 0..8", mult_ok)
    check("G08 HALVING     the image of the level-k block map on the core"
          " has 3125 states for every k = 0..14, both letters", halving_ok)
    check("G09 K0-CENTRES  at k = 0 each letter has exactly one recurrent"
          " fixed state, the reflection centres 3(C_D + V_E) and 3 C_D in"
          " the singlet, 125 off-core each, multiplier exactly minus the"
          " identity, and no state is fixed by both letters",
          k0_ok and not any(F[0][i] == i and F[1][i] == i
                            for i in range(N)))
    check("G10 RETURN      at every k = 1 mod 4 in range the fixed set is"
          " exactly the opposite living half, 3125 states, every"
          " multiplier the identity, off-core 3125 at k = 1 and 0 at"
          " k = 5, 9, 13", return_ok)
    check("G11 EMPTY       at every other k = 2..14 the block map has no"
          " fixed state on the core and none off it", empty_ok)
    check("G12 HALF-LAW    every fixed state lies in the half"
          " H_(eps xor k mod 2), k = 0..14", halflaw_ok)

    scales = sorted(set(nonempty_scales))
    two_pow = [k for k in range(K_MAX + 1) if pow(2, k, 5) == 2]
    unit_pow = [k for k in range(K_MAX + 1) if pow(2, k, 5) == 1]
    full_return = sorted(set(k for k in scales if k != 0))
    check("G13 CLOCK       the scales carrying a full-half return are"
          " exactly those with block length 2^k = 2 mod 5, and no scale"
          " with 2^k = 1 mod 5 carries one",
          full_return == two_pow and not set(full_return) & set(unit_pow)
          and unit_pow == [0, 4, 8, 12])

    print("P-ENTROPY-RG-RETURN-1 exact verifier")
    print("fixed points and multiplier spectra of the renormalized block")
    print("maps Phi^(k)_eps on the recurrent core of the F_5^6 kernel,")
    print("dyadic scales k = 0..14, both letters, exact arithmetic")
    print()
    passed = 0
    for i, (nm, okk) in enumerate(CHECKS, 1):
        tag = "PASS" if okk else "FAIL"
        if okk:
            passed += 1
        print("%s %02d %s" % (tag, i, nm))
    print()
    for line in tower:
        print(line)
    print()
    for line in spectra:
        print(line)
    print()
    print("CLOCK nonempty scales in range: %s"
          % ",".join(str(k) for k in scales))
    print("CLOCK scales with 2^k = 2 mod 5:  %s"
          % ",".join(str(k) for k in two_pow))
    print("CLOCK scales with 2^k = 1 mod 5:  %s"
          % ",".join(str(k) for k in unit_pow))
    print("CLOCK distinct multiplier matrices realized at fixed states: %d"
          % len(realized))
    print("CLOCK realized multipliers are exactly the identity and its"
          " negative: %s" % ("yes" if realized == {IDM, MINUS_I} else "no"))
    print()
    print("GATES %d/%d %s" % (passed, len(CHECKS),
                              "ALL PASS" if passed == len(CHECKS)
                              else "FALSIFIER FIRED"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
