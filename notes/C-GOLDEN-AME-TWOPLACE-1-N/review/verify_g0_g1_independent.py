#!/usr/bin/env python3
# C-GOLDEN-AME-TWOPLACE-1-N -- gate G0 (source integrity, exact 2-unitarity)
# and gate G1 (two-place field) exact verifier.
#
# Preregistration: notes/C-GOLDEN-AME-TWOPLACE-1-N/PREREG.md,
# frozen at twist-j commit 494ce485e92911c107b2a171935f76d7e3f81ff5.
#
# Authority of the matrix input: matrix-toolbox/AME_4_6 commit
# 1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8, file AME46_ORIGINAL.m only.
#
# All algebra is exact over Q(zeta_40) represented as Q[x]/(Phi_40),
# Phi_40(x) = x^16 - x^12 + x^8 - x^4 + 1, with coefficients in Fraction.
# The frozen defining embedding is z -> exp(i*pi/20); it enters only through
# stated sign facts for real square roots (cos and sin positivity on the
# relevant intervals), never through floating point. No float appears in any
# verdict path.
#
# stdout is the certificate and must be byte-identical across platforms.
# Platform data goes to stderr.
#
# Usage: python3 verify_g0_g1.py --source /path/to/AME46_ORIGINAL.m
#                                [--pysource /path/to/AME46.py]

import argparse
import hashlib
import sys
from fractions import Fraction

PIN_M_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
PIN_M_BYTES = 8515
PIN_PY_SHA256 = None  # filled from file; py is textual cross-check only
PIN_COMMIT = "1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8"

N = 16  # degree of Q(zeta_40)
# Phi_40 reduction: x^16 = x^12 - x^8 + x^4 - 1
PHI40 = [1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1]

FAILURES = []


def report(line):
    sys.stdout.write(line + "\n")


def check(label, ok):
    report("%s : %s" % (label, "PASS" if ok else "FAIL"))
    if not ok:
        FAILURES.append(label)
    return ok


# ---------------------------------------------------------------- field engine

def _xk_mod_phi(k):
    """coefficients of x^k mod Phi_40 as list of 16 ints"""
    poly = [0] * (k + 1)
    poly[k] = 1
    for d in range(len(poly) - 1, N - 1, -1):
        c = poly[d]
        if c:
            poly[d] = 0
            # x^d = c * x^(d-16) * (x^12 - x^8 + x^4 - 1)
            poly[d - 4] += c
            poly[d - 8] -= c
            poly[d - 12] += c
            poly[d - 16] -= c
    out = poly[:N]
    while len(out) < N:
        out.append(0)
    return out


RED = [tuple(_xk_mod_phi(k)) for k in range(80)]

ZERO = tuple([Fraction(0)] * N)
ONE = tuple([Fraction(1)] + [Fraction(0)] * (N - 1))


def zpow(k):
    return tuple(Fraction(v) for v in RED[k % 40])


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def smul(q, u):
    q = Fraction(q)
    return tuple(q * a for a in u)


def mul(u, v):
    acc = [Fraction(0)] * (2 * N - 1)
    for i, ci in enumerate(u):
        if ci:
            for j, cj in enumerate(v):
                if cj:
                    acc[i + j] += ci * cj
    out = [Fraction(0)] * N
    for k in range(2 * N - 1):
        ck = acc[k]
        if ck:
            r = RED[k]
            for t in range(N):
                if r[t]:
                    out[t] += ck * r[t]
    return tuple(out)


def galois(u, m):
    """sigma_m : z -> z^m for gcd(m,40)=1"""
    out = [Fraction(0)] * N
    for i, ci in enumerate(u):
        if ci:
            r = RED[(i * m) % 40]
            for t in range(N):
                if r[t]:
                    out[t] += ci * r[t]
    return tuple(out)


def conj(u):
    return galois(u, 39)


def is_zero(u):
    return all(x == 0 for x in u)


def eq(u, v):
    return all(a == b for a, b in zip(u, v))


def fmt(u):
    terms = []
    for i, ci in enumerate(u):
        if ci:
            terms.append("%s*z^%d" % (str(ci), i))
    return " + ".join(terms) if terms else "0"


# ---------------------------------------------------------------- source parse

def parse_m(text):
    """strict token parse of AME46_ORIGINAL.m; returns (amp, exp) 36x36"""
    i0 = text.index("U = [")
    i1 = text.index("] .* w.^[", i0)
    i2 = text.index("];", i1 + 9)
    amp_block = text[i0 + len("U = ["):i1]
    exp_block = text[i1 + len("] .* w.^["):i2]

    def rows_of(block, allowed):
        rows = []
        for raw in block.split(";"):
            toks = raw.replace(",", " ").split()
            if not toks:
                continue
            if len(toks) != 36:
                raise ValueError("row with %d tokens" % len(toks))
            for t in toks:
                if t not in allowed:
                    raise ValueError("bad token %r" % t)
            rows.append(toks)
        if len(rows) != 36:
            raise ValueError("%d rows" % len(rows))
        return rows

    amp = rows_of(amp_block, {"0", "a", "b", "c"})
    expo = rows_of(exp_block, {str(k) for k in range(20)})
    return amp, [[int(t) for t in row] for row in expo]


def parse_py(text):
    """textual parse of AME46.py assignments U[r, c] = <letter><phase>"""
    entries = {}
    for line in text.splitlines():
        line = line.strip().rstrip(";")
        if not line.startswith("U[") or "=" not in line:
            continue
        lhs, rhs = line.split("=", 1)
        lhs = lhs.strip()
        rhs = rhs.strip()
        inside = lhs[2:lhs.index("]")]
        r, cc = [int(p.strip()) for p in inside.split(",")]
        # rhs forms: L | L*w | L*(w**K) | L*w**K | L/w | L/(w**K)
        letter = rhs[0]
        if letter not in "abc":
            raise ValueError("bad rhs %r" % rhs)
        rest = rhs[1:].replace(" ", "")
        if rest == "":
            k = 0
        elif rest == "*w":
            k = 1
        elif rest == "/w":
            k = -1
        elif rest.startswith("*(w**") and rest.endswith(")"):
            k = int(rest[5:-1])
        elif rest.startswith("/(w**") and rest.endswith(")"):
            k = -int(rest[5:-1])
        elif rest.startswith("*w**"):
            k = int(rest[4:])
        elif rest.startswith("/w**"):
            k = -int(rest[4:])
        else:
            raise ValueError("bad rhs %r" % rhs)
        if (r, cc) in entries:
            raise ValueError("duplicate (%d,%d)" % (r, cc))
        entries[(r, cc)] = (letter, k % 20)
    return entries


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--pysource", default=None)
    args = ap.parse_args()

    sys.stderr.write("platform: %s %s\n" % (sys.platform, sys.version.replace("\n", " ")))

    report("C-GOLDEN-AME-TWOPLACE-1-N exact verifier, gates G0 and G1")
    report("prereg commit 494ce485e92911c107b2a171935f76d7e3f81ff5")
    report("source pin: matrix-toolbox/AME_4_6 commit %s" % PIN_COMMIT)
    report("")
    report("== G0 SOURCE INTEGRITY ==")

    data = open(args.source, "rb").read()
    sha = hashlib.sha256(data).hexdigest()
    report("AME46_ORIGINAL.m bytes %d sha256 %s" % (len(data), sha))
    if not check("pinned byte count 8515", len(data) == PIN_M_BYTES):
        sys.exit(2)
    if not check("pinned sha256", sha == PIN_M_SHA256):
        sys.exit(2)

    amp, expo = parse_m(data.decode("ascii"))
    check("token parse 36x36 amplitudes in {0,a,b,c} and 36x36 exponents in 0..19", True)

    # support statistics
    support = [(r, cc) for r in range(36) for cc in range(36) if amp[r][cc] != "0"]
    nnz = len(support)
    letters = {"a": 0, "b": 0, "c": 0}
    for (r, cc) in support:
        letters[amp[r][cc]] += 1
    row_prof = []
    for r in range(36):
        prof = "".join(sorted(amp[r][cc] for cc in range(36) if amp[r][cc] != "0"))
        row_prof.append(prof)
    col_prof = []
    for cc in range(36):
        prof = "".join(sorted(amp[r][cc] for r in range(36) if amp[r][cc] != "0"))
        col_prof.append(prof)
    from collections import Counter
    rp = Counter(row_prof)
    cp = Counter(col_prof)
    report("support: %d nonzero entries; letters a=%d b=%d c=%d"
           % (nnz, letters["a"], letters["b"], letters["c"]))
    report("row letter profiles: %s" % ", ".join("%d x '%s'" % (n, k) for k, n in sorted(rp.items())))
    report("column letter profiles: %s" % ", ".join("%d x '%s'" % (n, k) for k, n in sorted(cp.items())))
    check("every row/column letter multiset is norm-admissible (in {cc, aabb, abc})",
          set(rp) <= {"cc", "aabb", "abc"} and set(cp) <= {"cc", "aabb", "abc"})
    off = sum(1 for r in range(36) for cc in range(36)
              if expo[r][cc] != 0 and amp[r][cc] == "0")
    check("no nonzero exponent off support (count %d)" % off, off == 0)
    canon = ";".join("%d,%d,%s,%d" % (r, cc, amp[r][cc], expo[r][cc]) for (r, cc) in support)
    report("support digest sha256 %s" % hashlib.sha256(canon.encode()).hexdigest())

    # exact constants in Q(zeta_40), z = zeta_40, frozen embedding z -> exp(i*pi/20)
    report("")
    report("exact constants over Q(zeta_40) = Q[x]/(Phi_40), z := zeta_40,")
    report("frozen embedding z -> exp(i*pi/20); square roots are the positive ones:")
    z = zpow(1)
    check("reduction self-test z^40 = 1", eq(zpow(40), ONE))
    sqrt2 = add(zpow(5), zpow(35))
    check("sqrt2 := z^5 + z^-5, sqrt2^2 = 2", eq(mul(sqrt2, sqrt2), smul(2, ONE)))
    report("  sign: z^5 + z^-5 -> 2*cos(pi/4) > 0 since 0 < pi/4 < pi/2")
    sqrt5 = sub(smul(2, add(zpow(4), zpow(36))), ONE)
    check("sqrt5 := 2(z^4 + z^-4) - 1, sqrt5^2 = 5", eq(mul(sqrt5, sqrt5), smul(5, ONE)))
    report("  sign: 4*cos(pi/5) - 1 > 4*cos(pi/3) - 1 = 1 > 0 (cos decreasing on (0,pi))")
    sqrt10 = mul(sqrt2, sqrt5)
    check("sqrt10 := sqrt2*sqrt5, sqrt10^2 = 10", eq(mul(sqrt10, sqrt10), smul(10, ONE)))
    report("  sign: product of two positives")
    phi = smul(Fraction(1, 2), add(ONE, sqrt5))
    check("phi := (1+sqrt5)/2 = z^4 + z^-4", eq(phi, add(zpow(4), zpow(36))))
    # s := -i (z^4 - z^-4) -> 2 sin(pi/5) > 0
    s = smul(-1, mul(zpow(10), sub(zpow(4), zpow(36))))
    check("s := -i(z^4 - z^-4), s^2 + phi = 3  (i.e. s^2 = 3 - phi = (10-2*sqrt5)/4)",
          eq(add(mul(s, s), phi), smul(3, ONE)))
    report("  (embedded identity: 4 sin^2(pi/5) + 2 cos(pi/5) = 3 exactly)")
    report("  sign: 2*sin(pi/5) > 0 since 0 < pi/5 < pi")
    t = add(zpow(2), zpow(38))
    report("t := z^2 + z^-2 = w + w^-1 -> 2*cos(pi/10) > 0 since 0 < pi/10 < pi/2")

    a_el = smul(Fraction(1, 10), mul(s, sqrt10))
    b_el = smul(Fraction(1, 10), mul(t, sqrt10))  # t = w + w^-1
    c_el = smul(Fraction(1, 2), sqrt2)
    w_el = zpow(2)

    check("a := s*sqrt10/10 > 0 and 4*a^2 = 1 - 1/sqrt5  [source def a = sqrt(1-1/sqrt5)/2]",
          eq(smul(20, mul(a_el, a_el)), sub(smul(5, ONE), sqrt5)))
    check("b := t*sqrt10/10 > 0 and 4*b^2 = 1 + 1/sqrt5  [source def b = sqrt(1+1/sqrt5)/2]",
          eq(smul(20, mul(b_el, b_el)), add(smul(5, ONE), sqrt5)))
    check("c := sqrt2/2 > 0 and c^2 = 1/2               [source def c = 1/sqrt2]",
          eq(smul(2, mul(c_el, c_el)), ONE))
    check("w := z^2 satisfies w = exp(2*pi*i/20) under the frozen embedding (definition)", True)
    check("w^20 = 1", eq(zpow(40), ONE))
    check("w primitive: w^k != 1 for 1 <= k <= 19",
          all(not eq(zpow(2 * k), ONE) for k in range(1, 20)))

    # build exact matrix
    LET = {"a": a_el, "b": b_el, "c": c_el}
    U = [[ZERO] * 36 for _ in range(36)]
    for (r, cc) in support:
        U[r][cc] = mul(LET[amp[r][cc]], zpow(2 * expo[r][cc]))

    report("")
    report("== G0 EXACT 2-UNITARITY ==")
    report("index conventions frozen by PREREG section 4 (zero-based):")
    report("  A[i,j,k,l] = U[6i+j, 6k+l]")
    report("  R(U)[6i+k, 6j+l] = A[i,j,k,l]")
    report("  Gamma2(U)[6i+l, 6k+j] = A[i,j,k,l]")

    def sparse_rows(M):
        rows = []
        for r in range(36):
            d = {}
            for cc in range(36):
                if not is_zero(M[r][cc]):
                    d[cc] = M[r][cc]
            rows.append(d)
        return rows

    def unitary_exact(M, name):
        rows = sparse_rows(M)
        crows = [{cc: conj(v) for cc, v in row.items()} for row in rows]
        ok = True
        for r in range(36):
            for q in range(36):
                accum = ZERO
                small, big = rows[r], crows[q]
                for cc, v in small.items():
                    if cc in big:
                        accum = add(accum, mul(v, big[cc]))
                want = ONE if r == q else ZERO
                if not eq(accum, want):
                    ok = False
                    report("  MISMATCH %s at (%d,%d): %s" % (name, r, q, fmt(accum)))
        return check("%s %s* = I_36 exactly (1296 exact inner products)" % (name, name), ok)

    A = {}
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    A[(i, j, k, l)] = U[6 * i + j][6 * k + l]
    R = [[ZERO] * 36 for _ in range(36)]
    G2 = [[ZERO] * 36 for _ in range(36)]
    for (i, j, k, l), v in A.items():
        R[6 * i + k][6 * j + l] = v
        G2[6 * i + l][6 * k + j] = v

    u_ok = unitary_exact(U, "U")
    r_ok = unitary_exact(R, "R(U)")
    g_ok = unitary_exact(G2, "Gamma2(U)")
    check("upstream assertion U U* = R(U) R(U)* = Gamma2(U) Gamma2(U)* = I_36 reproduced exactly",
          u_ok and r_ok and g_ok)

    # ---------------------------------------------------------------- py cross-check
    if args.pysource:
        report("")
        report("== G0 CROSS-CHECK (textual only; AME46.py carries no authority) ==")
        pdata = open(args.pysource, "rb").read()
        psha = hashlib.sha256(pdata).hexdigest()
        report("AME46.py bytes %d sha256 %s" % (len(pdata), psha))
        try:
            pent = parse_py(pdata.decode("utf-8"))
            report("AME46.py textual entries parsed: %d (own w = exp(i*pi/10), same w)" % len(pent))
            check("AME46.py support cardinality equals pinned support cardinality (112)",
                  len(pent) == nnz)
            # letter multiset
            plet = {"a": 0, "b": 0, "c": 0}
            for (letter, k) in pent.values():
                plet[letter] += 1
            check("AME46.py letter multiset equals pinned letter multiset",
                  plet == letters)
            # exact relation search: 24 slot permutations x {id, conj} x global w^t
            import itertools
            pmat = {}
            for (r, cc), (letter, k) in pent.items():
                pmat[(r, cc)] = mul(LET[letter], zpow(2 * k))
            best = None
            hits = []
            for perm in itertools.permutations(range(4)):
                for cj in (False, True):
                    # build candidate positions and detect needed global phase from
                    # first overlapping support element, then verify all
                    cand = {}
                    for (i, j, k, l), v in A.items():
                        idx = (i, j, k, l)
                        x = (idx[perm[0]], idx[perm[1]], idx[perm[2]], idx[perm[3]])
                        pos = (6 * x[0] + x[1], 6 * x[2] + x[3])
                        vv = conj(v) if cj else v
                        if not is_zero(vv):
                            cand[pos] = vv
                    if set(cand.keys()) != set(pmat.keys()):
                        continue
                    # try to find one global phase w^t (t in 0..39 over z) matching all
                    for tph in range(40):
                        ph = zpow(tph)
                        if all(eq(mul(ph, cand[p]), pmat[p]) for p in cand):
                            hits.append((perm, cj, tph))
                            break
            if hits:
                for (perm, cj, tph) in hits:
                    report("exact relation found: py[6x0+x1,6x2+x3] = z^%d * %sA[i,j,k,l] with (x0,x1,x2,x3) = perm%s of (i,j,k,l)"
                           % (tph, "conj " if cj else "", str(perm)))
                check("AME46.py matches the pinned tensor under a declared frozen slot map", True)
            else:
                # support-level diagnosis
                sup_hits = []
                for perm in itertools.permutations(range(4)):
                    cand = set()
                    for (i, j, k, l) in A:
                        if is_zero(A[(i, j, k, l)]):
                            continue
                        idx = (i, j, k, l)
                        x = (idx[perm[0]], idx[perm[1]], idx[perm[2]], idx[perm[3]])
                        cand.add((6 * x[0] + x[1], 6 * x[2] + x[3]))
                    if cand == set(pmat.keys()):
                        sup_hits.append(perm)
                report("no exact entry-level relation in the declared class (24 slot maps x conj x global z-phase)")
                report("support-level matches (slot maps carrying support onto support): %s"
                       % (str(sup_hits) if sup_hits else "none"))
                report("cross-check verdict: TEXTUAL AGREEMENT ONLY (constants, cardinality, letters);")
                report("no authority impact; AME46_ORIGINAL.m remains the sole matrix input")
        except ValueError as e:
            report("AME46.py parse stopped: %s" % str(e))
            report("cross-check verdict: TEXTUAL ONLY, file is syntactically incomplete as pinned")

    # ---------------------------------------------------------------- G1
    report("")
    report("== G1 SECTION-5 IDENTITIES (exact) ==")
    Tpl2 = zpow(6)
    check("T_pl/2 = zeta_20^3 = z^6 equals zeta_4^-1 * zeta_5^2 = z^30 * z^16  [PLENUM-POINT]",
          eq(Tpl2, mul(zpow(30), zpow(16))))
    p7 = ONE
    for _ in range(7):
        p7 = mul(p7, Tpl2)
    check("w = (T_pl/2)^7", eq(p7, w_el))
    sJ2 = sub(smul(3, ONE), phi)
    check("a^2 = (3 - phi)/10", eq(smul(10, mul(a_el, a_el)), sub(smul(3, ONE), phi)))
    check("a^2 = s_J^2/10 with s_J^2 = 3 - phi  [PLENUM-POINT]",
          eq(smul(10, mul(a_el, a_el)), sJ2))
    check("b^2 = (2 + phi)/10", eq(smul(10, mul(b_el, b_el)), add(smul(2, ONE), phi)))
    check("b = a*phi and a != 0  (hence b/a = phi)",
          eq(b_el, mul(a_el, phi)) and not is_zero(a_el))
    check("c^2 = 1/2", eq(smul(2, mul(c_el, c_el)), ONE))

    report("")
    report("== G1 MINIMAL FIELD F_U ==")
    report("Gal(Q(zeta_40)/Q) = (Z/40)^x = {1,3,7,9,11,13,17,19,21,23,27,29,31,33,37,39}, order 16")
    report("F_U := Q(all nonzero entries); by Galois correspondence F_U = Fix(H),")
    report("H := { sigma_m : sigma_m fixes every entry }.")
    units = [m for m in range(1, 40) if m % 2 == 1 and m % 5 != 0]
    ent_list = [(r, cc, U[r][cc]) for (r, cc) in support]
    Hset = []
    report("witness table (first support entry moved, row-major):")
    for m in units:
        if m == 1:
            continue
        wit = None
        for (r, cc, v) in ent_list:
            if not eq(galois(v, m), v):
                wit = (r, cc)
                break
        if wit is None:
            Hset.append(m)
            report("  sigma_%d : fixes every entry" % m)
        else:
            report("  sigma_%d : moves entry (%d,%d) = %s*w^%d"
                   % (m, wit[0], wit[1], amp[wit[0]][wit[1]], expo[wit[0]][wit[1]]))
    check("H = {identity}", len(Hset) == 0)
    check("F_U = Q(zeta_40), degree [F_U:Q] = 16", len(Hset) == 0)

    # generating witnesses (greedy, deterministic row-major)
    gens = []
    H = set(units)
    for (r, cc, v) in ent_list:
        if len(H) == 1:
            break
        H2 = {m for m in H if eq(galois(v, m), v)}
        if len(H2) < len(H):
            gens.append((r, cc))
            H = H2
    report("greedy generating witnesses (entries alone generating F_U over Q):")
    for (r, cc) in gens:
        report("  U[%d,%d] = %s*w^%d" % (r, cc, amp[r][cc], expo[r][cc]))
    check("witness subset generates F_U (stabilizer reduced to {1})", len(H) == 1)

    report("compositum certificates:")
    check("  zeta_5 = z^8, zeta_8 = z^5, and z = zeta_5^2 * zeta_8^-3  => Q(zeta_5,zeta_8) = Q(zeta_40)",
          eq(mul(zpow(16), zpow(25)), z))
    check("  zeta_8 = c*(1+i) with i = z^10  => zeta_8 in Q(zeta_20, sqrt2)",
          eq(mul(c_el, add(ONE, zpow(10))), zpow(5)))
    report("  zeta_20 = z^2 in Q(zeta_40); with zeta_5 = zeta_20^2 and the line above,")
    report("  z = zeta_5^2 * zeta_8^-3 in Q(zeta_20, sqrt2)  => Q(zeta_20, sqrt2) = Q(zeta_40)")
    report("  Q(zeta_5) intersect Q(zeta_8) = Q is frozen Canon [Z2-PLACES-SPLIT], cited not recomputed")
    report("field prediction of PREREG section 5: F_U = Q(zeta_20, sqrt2) = Q(zeta_40) = Q(zeta_5, zeta_8)")
    check("field prediction CONFIRMED from actual entries", len(Hset) == 0)

    report("")
    report("== VERDICT ==")
    if FAILURES:
        report("G0/G1 FAIL (%d failed checks)" % len(FAILURES))
        for f in FAILURES:
            report("  FAILED: %s" % f)
        sys.exit(1)
    report("G0 PASS -- pinned source reproduced exactly; U, R(U), Gamma2(U) exactly unitary")
    report("G1 PASS -- F_U = Q(zeta_20, sqrt2) = Q(zeta_40) = Q(zeta_5, zeta_8), degree 16,")
    report("           all section-5 identities proved exactly")
    report("scope note: per PREREG section 11, G0-G2 alone are insufficient for any bridge claim;")
    report("this certificate records source reproduction and an exact L1 coefficient statement only.")


if __name__ == "__main__":
    main()
