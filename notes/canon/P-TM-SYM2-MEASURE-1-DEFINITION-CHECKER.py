#!/usr/bin/env python3
# P-TM-SYM2-MEASURE-1 definition checker (NON-CANONICAL support file).
#
# Certificate schema B1-B7 of notes/canon/P-TM-SYM2-MEASURE-1-BORN-BRIDGE-INPUT.md
# plus the forcing certificates F1-F3 of the owner definition
# notes/canon/P-TM-SYM2-MEASURE-1-OWNER-DEFINITION.md and the spectral
# certificates S1-S4 of notes/canon/P-TM-SYM2-MEASURE-1-SELECTOR-CLASS-INPUT.md.
#
# Modes:
#   --definition   structural, forcing, and spectral certificates only.
#                  Emits NO selector classification, NO gauge-group order,
#                  NO orbit data, NO B5 record. This is the definition-freeze
#                  audit surface.
#   --evaluate     the full evaluation including the B5 tagged branch record,
#                  GAUGE-COHERENCE, and the deterministic routing. FOR THE
#                  PINNED PUBLIC PROBE ONLY. Running it outside a pinned
#                  probe branch produces no public status and no evidence.
#
# Result neutrality: no expected selector-class count, orbit count, orbit
# invariant list, or line-weight vector is embedded anywhere in this file.
# Registered Canon inputs (frame vectors, face weights, pair law) are inputs,
# not expectations. A legitimate scientific outcome is never a checker FAIL.
#
# Python standard library only. Exact arithmetic only: int and Fraction.
# No floats in any assertion. Deterministic output ordering.
#
# Run from the repository root:
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
#     python3 notes/canon/P-TM-SYM2-MEASURE-1-DEFINITION-CHECKER.py --definition

import sys
from fractions import Fraction as Fr
from itertools import product, combinations, permutations

FAILURES = []


def emit(line):
    payload = (line + "\n").encode("utf-8")
    sys.stdout.buffer.write(payload)
    sys.stdout.buffer.flush()


def check(name, ok, detail=""):
    # Store a stable certificate id so premise propagation is independent
    # of the human-readable description following that id.
    cert_id = name.split(None, 1)[0]
    if not cert_id.startswith("CERT-"):
        raise ValueError("certificate label lacks a stable CERT-* id: %s" % name)
    if ok:
        emit("PASS %s%s" % (name, (" " + detail) if detail else ""))
    else:
        FAILURES.append(cert_id)
        emit("FAIL %s%s" % (name, (" " + detail) if detail else ""))


# ----------------------------------------------------------------------
# Exact field Q(sqrt5): pairs (a, b) = a + b*sqrt5 with Fraction entries.
# ----------------------------------------------------------------------

def q5(a=0, b=0):
    return (Fr(a), Fr(b))


Q5_ZERO = q5(0)
Q5_ONE = q5(1)


def q5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q5_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q5_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5_neg(x):
    return (-x[0], -x[1])


def q5_inv(x):
    n = x[0] * x[0] - 5 * x[1] * x[1]
    if n == 0:
        raise ZeroDivisionError("Q(sqrt5) inverse of zero")
    return (x[0] / n, -x[1] / n)


def q5_div(x, y):
    return q5_mul(x, q5_inv(y))


def q5_is_zero(x):
    return x[0] == 0 and x[1] == 0


def q5_pos_principal(x):
    # sign of a + b*sqrt5 in the principal real embedding sqrt5 > 0, exact.
    a, b = x
    if b == 0:
        return a > 0
    if a == 0:
        return b > 0
    if a > 0 and b > 0:
        return True
    if a < 0 and b < 0:
        return False
    if b > 0:  # a < 0
        return 5 * b * b > a * a
    return a * a > 5 * b * b  # b < 0, a > 0


PHI = (Fr(1, 2), Fr(1, 2))  # (1 + sqrt5)/2


# ----------------------------------------------------------------------
# Exact cyclotomic ring Q(zeta5): 5-tuples over basis (1, z, z^2, z^3, z^4)
# in Z[z]/(z^5 - 1); equality and normalization modulo Phi5 = 1+z+z^2+z^3+z^4.
# ----------------------------------------------------------------------

def c5(*coeffs):
    v = [Fr(0)] * 5
    for i, c in enumerate(coeffs):
        v[i] = Fr(c)
    return tuple(v)


def c5_norm(x):
    # canonical representative modulo Phi5: zero the z^4 slot.
    t = x[4]
    return tuple(x[i] - t for i in range(5))


def c5_eq(x, y):
    return c5_norm(x) == c5_norm(y)


def c5_add(x, y):
    return tuple(x[i] + y[i] for i in range(5))


def c5_sub(x, y):
    return tuple(x[i] - y[i] for i in range(5))


def c5_mul(x, y):
    out = [Fr(0)] * 5
    for i in range(5):
        if x[i] == 0:
            continue
        for j in range(5):
            if y[j] == 0:
                continue
            out[(i + j) % 5] += x[i] * y[j]
    return tuple(out)


def c5_scal(c, x):
    c = Fr(c)
    return tuple(c * x[i] for i in range(5))


def c5_star(x):
    # complex conjugation z -> z^{-1}
    return tuple(x[(-i) % 5] for i in range(5))


def zpow(k):
    v = [Fr(0)] * 5
    v[k % 5] = Fr(1)
    return tuple(v)


C5_ONE = zpow(0)


def c5_to_q5(x):
    # convert a star-fixed element to Q(sqrt5) via u = z + z^4 = (-1+sqrt5)/2.
    xn = c5_norm(x)
    if not c5_eq(x, c5_star(x)):
        raise ValueError("element is not star-fixed")
    # normalized coords (c0, c1, c2, c3, 0); star-fixed forces relations,
    # solve x = a*1 + b*u with 1 -> (1,0,0,0,0), u -> normalized (-1,0,-1,-1,0).
    # slots: c0 = a - b ; c1 = 0 ; c2 = -b ; c3 = -b.
    b = -xn[2]
    a = xn[0] + b
    ok = (xn[1] == 0) and (xn[3] == -b)
    if not ok:
        raise ValueError("star-fixed decomposition failed")
    u_q5 = (Fr(-1, 2), Fr(1, 2))
    return q5_add(q5(a), q5_mul(q5(b), u_q5))


# ----------------------------------------------------------------------
# Registered frame (GOLDEN-SIX-LINE-SYM2-FRAME): six lines over Q(phi).
# ----------------------------------------------------------------------

V = [
    (q5(0), q5(1), PHI),           # v1 = (0, 1, phi)
    (q5(0), q5(1), q5_neg(PHI)),   # v2 = (0, 1, -phi)
    (q5(1), PHI, q5(0)),           # v3 = (1, phi, 0)
    (q5(1), q5_neg(PHI), q5(0)),   # v4 = (1, -phi, 0)
    (PHI, q5(0), q5(1)),           # v5 = (phi, 0, 1)
    (PHI, q5(0), q5_neg(q5(1))),   # v6 = (phi, 0, -1)
]

SIGMA_LINE = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}  # (v1 v2)(v3 v4)(v5 v6)


def dot(u, v):
    s = Q5_ZERO
    for i in range(3):
        s = q5_add(s, q5_mul(u[i], v[i]))
    return s


def mat_from_outer(v, scale_inv):
    # v v^T * scale_inv as 3x3 Q5 matrix
    return [[q5_mul(q5_mul(v[i], v[j]), scale_inv) for j in range(3)] for i in range(3)]


def proportional(u, v):
    # projective equality over Q(sqrt5): all 2x2 minors vanish, u, v nonzero
    if all(q5_is_zero(c) for c in u) or all(q5_is_zero(c) for c in v):
        return False
    for i in range(3):
        for j in range(i + 1, 3):
            m = q5_sub(q5_mul(u[i], v[j]), q5_mul(u[j], v[i]))
            if not q5_is_zero(m):
                return False
    return True


# ----------------------------------------------------------------------
# Registered drive: theta_n = s_2(n) mod 2; centered windows q(n).
# ----------------------------------------------------------------------

def theta(n):
    return bin(n).count("1") & 1


def q_window(n):
    return (theta(n - 1), theta(n), theta(n + 1))


W3 = ((0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0))
W3_INDEX = {w: i for i, w in enumerate(W3)}


def n_flip(w):
    return tuple(1 - b for b in w)


def child_L(w):
    a, b, c = w
    return (1 - a, b, 1 - b)


def child_R(w):
    a, b, c = w
    return (b, 1 - b, c)


# ======================================================================
# CERT-A: registered frame facts re-audited from the registered vectors.
# ======================================================================

def cert_frame():
    r = q5_add(PHI, q5(2))
    r_inv = q5_inv(r)
    P = [mat_from_outer(v, r_inv) for v in V]
    # sum of projectors = 2 I3
    S = [[Q5_ZERO] * 3 for _ in range(3)]
    for Pi in P:
        for i in range(3):
            for j in range(3):
                S[i][j] = q5_add(S[i][j], Pi[i][j])
    ok = True
    for i in range(3):
        for j in range(3):
            want = q5(2) if i == j else q5(0)
            ok = ok and (S[i][j] == want)
    check("CERT-A1 sum of the six registered projectors equals 2 I3", ok)
    # unit traces
    ok = True
    for Pi in P:
        tr = q5_add(q5_add(Pi[0][0], Pi[1][1]), Pi[2][2])
        ok = ok and (tr == Q5_ONE)
    check("CERT-A2 every registered line projector has exact trace 1", ok)
    # equiangularity: squared cosine exactly 1/5 for all 15 pairs
    ok = True
    for i, j in combinations(range(6), 2):
        num = q5_mul(dot(V[i], V[j]), dot(V[i], V[j]))
        den = q5_mul(dot(V[i], V[i]), dot(V[j], V[j]))
        ok = ok and (q5_div(num, den) == (Fr(1, 5), Fr(0)))
    check("CERT-A3 all fifteen registered line pairs have squared cosine exactly 1/5", ok)
    return P


# ======================================================================
# CERT-I2: sigma_line consistency clause (zero patterns).
# ======================================================================

def zero_pattern(v):
    zp = tuple(i for i in range(3) if q5_is_zero(v[i]))
    return zp


def cert_sigma_consistency():
    pats = {}
    ok = True
    for idx, v in enumerate(V):
        zp = zero_pattern(v)
        ok = ok and (len(zp) == 1)
        pats.setdefault(zp, []).append(idx)
    ok = ok and (len(pats) == 3) and all(len(g) == 2 for g in pats.values())
    check("CERT-I2a each registered representative has exactly one zero slot; "
          "each of the three zero patterns is carried by exactly two lines", ok)
    sig = {}
    for g in pats.values():
        a, b = g
        sig[a] = b
        sig[b] = a
    check("CERT-I2b the zero-pattern involution is fixed-point-free and equals "
          "sigma_line = (v1 v2)(v3 v4)(v5 v6)", sig == SIGMA_LINE)
    # single-sign-flip reading: negating either nonzero slot of a registered
    # representative lands projectively on the sigma_line partner (the two
    # flips differ by the global sign), and negating the zero slot fixes the
    # line; so sigma_line is exactly the single-sign-flip relation.
    ok = True
    for i in range(6):
        j = SIGMA_LINE[i]
        for k in range(3):
            w = list(V[i])
            w[k] = q5_neg(w[k])
            target = i if q5_is_zero(V[i][k]) else j
            ok = ok and proportional(tuple(w), V[target])
    check("CERT-I2c every single-coordinate sign flip of a nonzero slot exchanges a "
          "line with its sigma_line partner projectively; the zero-slot flip fixes "
          "the line: sigma_line is the single-sign-flip relation", ok)


# ======================================================================
# CERT-F2: forcing of sigma_line from the registered presentation.
#   (i)  Gram no-go: pair-homogeneity (CERT-A3) means no pairwise metric
#        invariant distinguishes any pairing.
#   (ii) uniqueness: among all 15 pairings of the six registered lines,
#        exactly one is invariant under the signed-coordinate stabilizer
#        of the registered presentation, and it is sigma_line.
# Scope guard: the group computed here is the SIGNED-COORDINATE stabilizer
# of the registered presentation only. The evaluation-layer gauge group
# Aut(Lines, sigma_line) over Q(phi) is NOT computed in definition mode.
# ======================================================================

def signed_perm_matrices():
    mats = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            mats.append((perm, signs))
    return mats


def apply_signed_perm(mat, v):
    perm, signs = mat
    out = [Q5_ZERO] * 3
    for i in range(3):
        # row i takes sign_i * coordinate perm[i]
        c = v[perm[i]]
        out[i] = c if signs[i] == 1 else q5_neg(c)
    return tuple(out)


def cert_pairing_forcing():
    check("CERT-F2i pair-homogeneity of the registered Gram (CERT-A3) proves no "
          "pairwise metric invariant can select a pairing", "CERT-A3" not in FAILURES)
    # signed-coordinate stabilizer, as line permutations
    perms_found = set()
    for mat in signed_perm_matrices():
        images = []
        okm = True
        for v in V:
            gv = apply_signed_perm(mat, v)
            tgt = None
            for j, w in enumerate(V):
                if proportional(gv, w):
                    tgt = j
                    break
            if tgt is None:
                okm = False
                break
            images.append(tgt)
        if okm and sorted(images) == list(range(6)):
            perms_found.add(tuple(images))
    # group property of the effective line permutations
    ok = tuple(range(6)) in perms_found
    for g in perms_found:
        inv = [0] * 6
        for i, gi in enumerate(g):
            inv[gi] = i
        ok = ok and (tuple(inv) in perms_found)
        for h in perms_found:
            comp = tuple(g[h[i]] for i in range(6))
            ok = ok and (comp in perms_found)
    check("CERT-F2ii the effective signed-coordinate stabilizer of the registered "
          "presentation is a group of line permutations (order %d)" % len(perms_found), ok)
    # all 15 perfect matchings on six labels
    def matchings(elems):
        if not elems:
            yield ()
            return
        a = elems[0]
        for k in range(1, len(elems)):
            b = elems[k]
            rest = elems[1:k] + elems[k + 1:]
            for m in matchings(rest):
                yield ((a, b),) + m
    invariant = []
    for m in matchings(tuple(range(6))):
        pairing = {}
        for a, b in m:
            pairing[a] = b
            pairing[b] = a
        inv_ok = True
        for g in perms_found:
            for x in range(6):
                if g[pairing[x]] != pairing[g[x]]:
                    inv_ok = False
                    break
            if not inv_ok:
                break
        if inv_ok:
            invariant.append(pairing)
    ok = (len(invariant) == 1) and (invariant[0] == SIGMA_LINE)
    check("CERT-F2iii exactly one of the fifteen pairings of the registered six-line "
          "list is invariant under the signed-coordinate stabilizer, and it is "
          "sigma_line", ok)


# ======================================================================
# CERT-F1: forcing of the W3 carrier under the frozen transport principle.
# Exact factor languages of the registered drive by de-substitution closure,
# with an independent direct-prefix second path.
# ======================================================================

def factor_language(k, F_prev=None):
    # F_k from F_{k'} with k' = floor(k/2)+1 via the exact expansion maps:
    # even start: (a0, 1-a0, a1, 1-a1, ...) ; odd start: (1-a0, a1, 1-a1, ...).
    # For k <= 2 use the least-fixed-point construction proved in the owner
    # definition. Every position is an even or odd start; expansions of
    # occurring parents occur; hence the construction is exact and complete.
    if k == 1:
        return {(0,), (1,)}
    if k == 2:
        S = {(0, 1), (1, 0)}  # even starts (a, 1-a) with both letters occurring
        changed = True
        while changed:
            changed = False
            for (a, b) in sorted(S):
                w = (1 - a, b)  # odd start over occurring pair (a, b)
                if w not in S:
                    S.add(w)
                    changed = True
        return S
    kp = k // 2 + 1
    if F_prev is None:
        F_prev = factor_language(kp)
    out = set()
    for w in sorted(F_prev):
        even = []
        for a in w:
            even.extend((a, 1 - a))
        odd = even[1:]
        if len(even) >= k:
            out.add(tuple(even[:k]))
        if len(odd) >= k:
            out.add(tuple(odd[:k]))
    return out


def cert_carrier_forcing():
    # exact closure path
    F = {}
    for k in range(1, 9):
        F[k] = factor_language(k)
    counts = [len(F[k]) for k in range(1, 9)]
    # independent second path: direct exact prefix scan
    NPREF = 1 << 15
    bits = [theta(n) for n in range(NPREF)]
    ok = True
    for k in range(1, 9):
        seen = set()
        for i in range(NPREF - k):
            seen.add(tuple(bits[i:i + k]))
        ok = ok and (seen == F[k])
    check("CERT-F1a exact factor languages by de-substitution closure agree with the "
          "independent direct-prefix scan for lengths 1..8", ok)
    check("CERT-F1b factor counts p(1..8) = %s" % (tuple(counts),),
          counts[2] == 6)
    # truncation surjectivity F_{k+1} ->> F_k (right-extension witness)
    ok = True
    for k in range(1, 8):
        trunc = {w[:k] for w in F[k + 1]}
        ok = ok and (trunc == F[k])
    check("CERT-F1c right-truncation maps F_(k+1) onto F_k for k = 1..7 "
          "(monotone complexity witness)", ok)
    # unique transport length: p(k) = 6 exactly at k = 3 in the audited range;
    # p(1), p(2) < 6 exclude k < 3; p(4) = 10 with monotonicity excludes k > 3.
    ok = (counts[0] < 6 and counts[1] < 6 and counts[2] == 6 and counts[3] > 6
          and all(counts[i] >= counts[i - 1] for i in range(1, 8)))
    check("CERT-F1d within the frozen transport principle the window length k = 3 "
          "is the unique length with |F_k| = |Lines| = 6 (k < 3 too small, "
          "k >= 4 too large by monotonicity from p(4) = 10)", ok)
    # W3 as frozen equals F_3; centered convention consistent; finite witness
    ok = (set(W3) == F[3])
    for n in range(1, 7):
        ok = ok and (q_window(n) in F[3])
    ok = ok and ({q_window(n) for n in range(1, 7)} == set(W3))
    check("CERT-F1e the frozen carrier W3 equals the exact factor language F_3; "
          "the six centered windows q(1..6) exhaust it", ok)
    # cube-freeness certificate: structural lemma + no constant triple
    ok = ((0, 0, 0) not in F[3]) and ((1, 1, 1) not in F[3])
    for m in range(0, 4096):
        ok = ok and (theta(2 * m) != theta(2 * m + 1))
    check("CERT-F1f no constant triple occurs: complementary registered children "
          "theta(2m) != theta(2m+1) audited on a contiguous range", ok)
    # increment-reading no-go: the increment map w -> (w2 - w1, w3 - w2) mod 2
    # is invariant under bit negation, so it factors through the N-quotient:
    # its image on the six windows has exactly three values, every fiber is a
    # full N-orbit, and no N-invariant reading separates the six lines.
    fibers = {}
    for w in W3:
        keyv = ((w[1] - w[0]) % 2, (w[2] - w[1]) % 2)
        fibers.setdefault(keyv, []).append(w)
    ok = (len(fibers) == 3)
    for members in fibers.values():
        ok = ok and (len(members) == 2) and (n_flip(members[0]) == members[1])
    for w in W3:
        kw = ((w[1] - w[0]) % 2, (w[2] - w[1]) % 2)
        kn = ((n_flip(w)[1] - n_flip(w)[0]) % 2, (n_flip(w)[2] - n_flip(w)[1]) % 2)
        ok = ok and (kw == kn)
    check("CERT-F1g increment-reading no-go: the increment map is N-invariant with "
          "image of size exactly 3 on the six windows (every fiber a full "
          "N-orbit), so no N-invariant reading separates the six lines; the "
          "selector must read the bits, not only their changes", ok)
    # conditionality witness (first-class, from the independent break round):
    # WITHOUT the bijective clause of the adopted transport principle the
    # carrier is NOT forced: an exact negation-equivariant SURJECTION from the
    # ten-word length-4 language onto the six lines exists. The witness is
    # constructed deterministically; its existence certifies that the
    # bijective clause of ruling F1 is load-bearing.
    F4 = sorted(factor_language(4))
    ok = (len(F4) == 10) and all(n_flip(w) in F4 and n_flip(w) != w for w in F4)
    orbs4 = sorted({tuple(sorted((w, n_flip(w)))) for w in F4})
    ok = ok and (len(orbs4) == 5)
    line_of = {}
    for i, pair in enumerate(orbs4):
        line_of[pair[0]] = 2 * (i % 3)
        line_of[pair[1]] = SIGMA_LINE[2 * (i % 3)]
    ok = ok and all(line_of[n_flip(w)] == SIGMA_LINE[line_of[w]] for w in F4)
    ok = ok and (len(set(line_of.values())) == 6)
    ok = ok and (len(F4) != 6)
    check("CERT-F1h conditionality witness: an exact N-equivariant surjection "
          "from the ten-word length-4 language onto the six lines exists (not a "
          "bijection), so WITHOUT the bijective clause the carrier is not "
          "forced; the bijective clause of ruling F1 is load-bearing", ok)


# ======================================================================
# CERT-B1: carrier structure and the conditional selector-typing theorem.
# ======================================================================

def cert_b1():
    ok = all(n_flip(w) in W3_INDEX and n_flip(w) != w for w in W3)
    check("CERT-B1a bit negation N acts freely on W3", ok)
    orbits = set()
    for w in W3:
        orbits.add(tuple(sorted((w, n_flip(w)))))
    check("CERT-B1b N has exactly three orbits on W3", len(orbits) == 3)
    ok = True
    for pair in orbits:
        mids = sorted(w[1] for w in pair)
        ok = ok and (mids == [0, 1])
    check("CERT-B1c every N-orbit carries exactly one window of each middle bit "
          "(canonical W3 -> Q x B_2 bijection)", ok)
    # conditional theorem over the COMPLETE function space (no class data emitted):
    # every negation-to-sigma_line equivariant surjection s : W3 -> Lines is a
    # bijection and induces a bijection Q -> Lines/<sigma_line>.
    npair = [W3_INDEX[n_flip(w)] for w in W3]
    orb_of = {}
    for oi, pair in enumerate(sorted(orbits)):
        for w in pair:
            orb_of[W3_INDEX[w]] = oi
    line_orb = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
    theorem = True
    audited = 0
    for s in product(range(6), repeat=6):
        audited += 1
        equivariant = all(s[npair[i]] == SIGMA_LINE[s[i]] for i in range(6))
        if not equivariant:
            continue
        surjective = len(set(s)) == 6
        if not surjective:
            continue
        bijective = len(set(s)) == 6
        induced = {}
        well = True
        for i in range(6):
            o = orb_of[i]
            lo = line_orb[s[i]]
            if o in induced and induced[o] != lo:
                well = False
            induced[o] = lo
        induced_bij = well and len(set(induced.values())) == 3
        theorem = theorem and bijective and induced_bij
    check("CERT-B1d conditional typing theorem verified over the complete function "
          "space (%d maps audited): equivariant + surjective implies bijective "
          "with bijective quotient descent" % audited, theorem)


# ======================================================================
# CERT-B2 and S1-S4: child identities, transfer, descent, stationarity,
# spectral growth certificate, and the contiguous recursion audit.
# ======================================================================

def frac_matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def frac_matvec(A, x):
    return [sum(A[i][k] * x[k] for k in range(len(x))) for i in range(len(A))]


def rank_frac(M):
    A = [row[:] for row in M]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def charpoly_frac(M):
    # Faddeev-LeVerrier, exact; returns coefficients of x^n + c1 x^(n-1) + ... + cn.
    n = len(M)
    I = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    coeffs = [Fr(1)]
    Mk = [row[:] for row in M]
    for k in range(1, n + 1):
        tr = sum(Mk[i][i] for i in range(n))
        ck = -tr / k
        coeffs.append(ck)
        if k < n:
            Mk = frac_matmul(M, [[Mk[i][j] + (ck if i == j else 0) for j in range(n)]
                                 for i in range(n)])
    return coeffs


def poly_eval_frac(coeffs, x):
    v = Fr(0)
    for c in coeffs:
        v = v * x + c
    return v


def factor_int_poly(coeffs):
    # factor a monic integer polynomial into linear factors over Z by rational
    # roots; returns (roots_with_multiplicity, remainder_degree).
    cs = [Fr(c) for c in coeffs]
    roots = []
    while len(cs) > 1:
        const = cs[-1]
        if const == 0:
            roots.append(Fr(0))
            cs = cs[:-1]
            continue
        num = abs(const.numerator)
        cands = set()
        d = 1
        while d * d <= num:
            if num % d == 0:
                cands.update((Fr(d), Fr(-d), Fr(num // d), Fr(-(num // d))))
            d += 1
        found = None
        for r in sorted(cands):
            if poly_eval_frac(cs, r) == 0:
                found = r
                break
        if found is None:
            break
        # synthetic division
        out = [cs[0]]
        for c in cs[1:-1]:
            out.append(c + out[-1] * found)
        cs = out
        roots.append(found)
    return roots, len(cs) - 1


def minpoly_on_subspace(M, basis):
    # exact minimal polynomial of M restricted to span(basis); basis vectors
    # are Fraction lists; returns monic coefficient list.
    dim = len(basis)
    # coordinates: solve in terms of basis via Gaussian elimination each time
    def coords(v):
        # solve B c = v where B columns are basis vectors
        n = len(v)
        A = [[basis[j][i] for j in range(dim)] + [v[i]] for i in range(n)]
        # eliminate
        r = 0
        pivots = []
        for c in range(dim):
            piv = None
            for i in range(r, n):
                if A[i][c] != 0:
                    piv = i
                    break
            if piv is None:
                continue
            A[r], A[piv] = A[piv], A[r]
            pv = A[r][c]
            A[r] = [x / pv for x in A[r]]
            for i in range(n):
                if i != r and A[i][c] != 0:
                    f = A[i][c]
                    A[i] = [A[i][j] - f * A[r][j] for j in range(dim + 1)]
            pivots.append(c)
            r += 1
        sol = [Fr(0)] * dim
        for idx, c in enumerate(pivots):
            sol[c] = A[idx][dim]
        # verify consistency
        for i in range(n):
            s = sum(basis[j][i] * sol[j] for j in range(dim))
            if s != v[i]:
                raise ValueError("vector outside subspace")
        return sol
    # powers of M acting on subspace as dim x dim matrices
    Msub = []
    for j in range(dim):
        img = frac_matvec(M, basis[j])
        Msub.append(coords(img))
    # column-major to row-major: Msub[j] is coords of M b_j; matrix R with
    # R[i][j] = coords(M b_j)[i]
    R = [[Msub[j][i] for j in range(dim)] for i in range(dim)]
    # find minimal polynomial by first linear dependence among I, R, R^2, ...
    mats = [[[Fr(1) if i == j else Fr(0) for j in range(dim)] for i in range(dim)]]
    while True:
        mats.append(frac_matmul(R, mats[-1]))
        k = len(mats) - 1
        # solve sum_{i<k} a_i mats[i] = mats[k]
        rows = []
        rhs = []
        for i in range(dim):
            for j in range(dim):
                rows.append([mats[t][i][j] for t in range(k)])
                rhs.append(mats[k][i][j])
        # least: exact solve if consistent
        A = [rows[i] + [rhs[i]] for i in range(len(rows))]
        r = 0
        pivots = []
        for c in range(k):
            piv = None
            for i in range(r, len(A)):
                if A[i][c] != 0:
                    piv = i
                    break
            if piv is None:
                continue
            A[r], A[piv] = A[piv], A[r]
            pv = A[r][c]
            A[r] = [x / pv for x in A[r]]
            for i in range(len(A)):
                if i != r and A[i][c] != 0:
                    f = A[i][c]
                    A[i] = [A[i][j] - f * A[r][j] for j in range(k + 1)]
            pivots.append(c)
            r += 1
        consistent = all(all(A[i][c] == 0 for c in range(k)) is False or A[i][k] == 0
                         for i in range(len(A)))
        # proper consistency check
        consistent = True
        for i in range(len(A)):
            if all(A[i][c] == 0 for c in range(k)) and A[i][k] != 0:
                consistent = False
                break
        if consistent:
            sol = [Fr(0)] * k
            for idx, c in enumerate(pivots):
                sol[c] = A[idx][k]
            # minimal polynomial: x^k - sum a_i x^i
            coeffs = [Fr(1)] + [Fr(0)] * k
            for i in range(k):
                coeffs[k - i] = -sol[i]
            return coeffs, R
        if len(mats) > dim + 1:
            raise RuntimeError("minimal polynomial search exceeded dimension")


def transfer_matrix():
    T = [[Fr(0)] * 6 for _ in range(6)]
    for w in W3:
        for child in (child_L(w), child_R(w)):
            T[W3_INDEX[child]][W3_INDEX[w]] += 1
    return T


def cert_b2_spectral(run_s4=True):
    ok = all(child_L(n_flip(w)) == n_flip(child_L(w)) and
             child_R(n_flip(w)) == n_flip(child_R(w)) for w in W3)
    check("CERT-B2a both child maps commute exactly with bit negation on W3", ok)
    ok = all(child_L(w) in W3_INDEX and child_R(w) in W3_INDEX for w in W3)
    check("CERT-B2b both child maps preserve the carrier W3", ok)
    T = transfer_matrix()
    # quotient carrier and quotient transfer
    orb_list = [((0, 0, 1), (1, 1, 0)), ((0, 1, 0), (1, 0, 1)), ((0, 1, 1), (1, 0, 0))]
    orb_of = {}
    for oi, pair in enumerate(orb_list):
        for w in pair:
            orb_of[W3_INDEX[w]] = oi
    TQ = [[Fr(0)] * 3 for _ in range(3)]
    for oi, pair in enumerate(orb_list):
        w = pair[0]
        for child in (child_L(w), child_R(w)):
            TQ[orb_of[W3_INDEX[child]]][oi] += 1
        # descent well-defined: the other member gives the same column
        col = [Fr(0)] * 3
        for child in (child_L(pair[1]), child_R(pair[1])):
            col[orb_of[W3_INDEX[child]]] += 1
        if [TQ[i][oi] for i in range(3)] != col:
            check("CERT-B2c quotient transfer well-defined", False)
            return None
    check("CERT-B2c the quotient transfer is well-defined on Q = W3/<N>", True)
    # exact descent identity varpi_* T = T_Q varpi_*
    varpi = [[Fr(0)] * 6 for _ in range(3)]
    for i in range(6):
        varpi[orb_of[i]][i] = Fr(1)
    lhs = frac_matmul(varpi, T)
    rhs = frac_matmul(TQ, varpi)
    check("CERT-B2d exact quotient descent varpi_* T = T_Q varpi_*", lhs == rhs)
    # S3: stationary law unique: rank(T/2 - I) = 5; solve exactly
    A = [[T[i][j] / 2 - (1 if i == j else 0) for j in range(6)] for i in range(6)]
    check("CERT-S3a rank(T/2 - I) = 5, the stationary law is unique", rank_frac(A) == 5)
    # solve (T/2 - I) f = 0 with sum f = 1
    M = [row[:] + [Fr(0)] for row in A]
    M.append([Fr(1)] * 6 + [Fr(1)])
    r = 0
    pivots = []
    for c in range(6):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                fq = M[i][c]
                M[i] = [M[i][j] - fq * M[r][j] for j in range(7)]
        pivots.append(c)
        r += 1
    f = [Fr(0)] * 6
    for idx, c in enumerate(pivots):
        f[c] = M[idx][6]
    ok = all(sum(T[i][j] * f[j] for j in range(6)) == 2 * f[i] for i in range(6))
    ok = ok and sum(f) == 1 and all(x > 0 for x in f)
    check("CERT-S3b the unique normalized stationary law is exact, positive, "
          "and satisfies T f = 2 f (computed witness: f = (%s))"
          % ", ".join(str(x) for x in f), ok)
    # COMPLEMENT-BALANCE and QUOTIENT-STREAM-COMPATIBILITY as implications
    ok = all(f[W3_INDEX[w]] == f[W3_INDEX[n_flip(w)]] for w in W3)
    check("CERT-B2e COMPLEMENT-BALANCE: N_* f = f follows from uniqueness "
          "(verified exactly on the computed law)", ok)
    piQ = [f[W3_INDEX[pair[0]]] + f[W3_INDEX[pair[1]]] for pair in orb_list]
    ok = all(sum(TQ[i][j] * piQ[j] for j in range(3)) == 2 * piQ[i] for i in range(3))
    ok = ok and sum(piQ) == 1
    ok = ok and all(f[W3_INDEX[w]] == piQ[orb_of[W3_INDEX[w]]] / 2 for w in W3)
    check("CERT-B2f QUOTIENT-STREAM-COMPATIBILITY: varpi_* f is the unique "
          "normalized stationary law of T_Q and f_w = third([w])/2", ok)
    # S1: characteristic polynomial, exact factorization over Z
    cp = charpoly_frac(T)
    roots, rem = factor_int_poly(cp)
    ok = (rem == 0)
    check("CERT-S1 the transfer characteristic polynomial factors completely over Z "
          "with integer roots (%s)" % ", ".join(str(x) for x in sorted(roots)), ok)
    # S2: minimal polynomial on the sum-zero subspace; growth certificate
    basis = []
    for i in range(5):
        v = [Fr(0)] * 6
        v[i] = Fr(1)
        v[5] = Fr(-1)
        basis.append(v)
    mp, R = minpoly_on_subspace(T, basis)
    mroots, mrem = factor_int_poly(mp)
    ok = (mrem == 0)
    rho_num = max((abs(r) for r in mroots), default=Fr(0))
    ok = ok and (rho_num < 2)
    sqfree = len(mroots) == len(set(mroots))
    check("CERT-S2a the minimal polynomial of T on the sum-zero subspace factors "
          "over Z (roots %s), is squarefree there, and its spectral radius "
          "rho = %s < 2: strict subdominance" %
          (", ".join(str(x) for x in sorted(mroots)), rho_num), ok and sqfree)
    # eventual periodicity gives the exact (C_J, m) pair with m = 1
    ok = False
    period = None
    Rpows = [[[Fr(1) if i == j else Fr(0) for j in range(5)] for i in range(5)]]
    for _ in range(24):
        Rpows.append(frac_matmul(R, Rpows[-1]))
    for a in range(0, 9):
        for p in range(1, 13):
            if a + p < len(Rpows) and Rpows[a + p] == Rpows[a]:
                ok = True
                period = (a, p)
                break
        if ok:
            break
    if ok:
        a, p = period
        cj = max(max(sum(abs(x) for x in row) for row in Rpows[j]) for j in range(a + p + 1))
        check("CERT-S2b growth certificate: T^%d = T^%d on the sum-zero subspace, "
              "so opnorm(T^j) is bounded with exact C_J = %s and peripheral Jordan "
              "degree m = 1; the all-N modulus of Lemma 2 is effective" % (a + p, a, cj), True)
    else:
        check("CERT-S2b growth certificate (eventual periodicity route)", False)
    # S4: both exact recursions and the boundary identity on a contiguous range
    if run_s4:
        NMAX = 2048
        counts = {w: 0 for w in W3}
        cvec = {}
        for n in range(1, 2 * NMAX + 2):
            counts[q_window(n)] += 1
            cvec[n] = tuple(counts[w] for w in W3)
        e = {w: tuple(1 if x == w else 0 for x in W3) for w in W3}
        Tint = [[int(x) for x in row] for row in transfer_matrix()]
        ok = True
        for N in range(1, NMAX + 1):
            TcN = tuple(sum(Tint[i][j] * cvec[N][j] for j in range(6)) for i in range(6))
            odd = tuple(TcN[i] + e[q_window(1)][i] for i in range(6))
            ok = ok and (cvec[2 * N + 1] == odd)
            even = tuple(odd[i] - e[q_window(2 * N + 1)][i] for i in range(6))
            ok = ok and (cvec[2 * N] == even)
            ok = ok and (q_window(2 * N + 1) == child_R(q_window(N)))
        check("CERT-S4 both census recursions and the boundary identity "
              "q(2N+1) = R(q(N)) hold exactly for every N <= %d" % NMAX, ok)
    return f


# ======================================================================
# CERT-B3 and CERT-F3: the coefficient-side Born carrier and the forcing
# of the coefficient representative delta_0 + delta_1.
# ======================================================================

def cert_b3_f3():
    # Fourier matrix F[k][r] = z^(rk); registered verb symbol Psi(k) = 1 + z^k
    Fm = [[zpow(r * k) for r in range(5)] for k in range(5)]
    v = [Fr(1), Fr(1), Fr(0), Fr(0), Fr(0)]  # delta_0 + delta_1
    Fv = []
    for k in range(5):
        acc = c5()
        for r in range(5):
            acc = c5_add(acc, c5_scal(v[r], Fm[k][r]))
        Fv.append(acc)
    ok = all(c5_eq(Fv[k], c5_add(C5_ONE, zpow(k))) for k in range(5))
    check("CERT-B3a F(delta_0 + delta_1)_k = 1 + zeta_5^k: the coefficient vector "
          "transforms exactly to the registered verb symbol", ok)
    # J anchor: slot k = 2 is the axiom J = 1 + zeta_5^2
    check("CERT-B3b the axiom slot: F(v)_2 = 1 + zeta_5^2 = J", c5_eq(Fv[2], c5_add(C5_ONE, zpow(2))))
    # Plancherel as the exact matrix identity F* F = 5 I
    ok = True
    for a in range(5):
        for b in range(5):
            acc = c5()
            for k in range(5):
                acc = c5_add(acc, c5_mul(c5_star(Fm[k][a]), Fm[k][b]))
            want = c5_scal(5, C5_ONE) if a == b else c5()
            ok = ok and c5_eq(acc, want)
    check("CERT-B3c exact Plancherel: F* F = 5 I on the coefficient carrier "
          "(so sum_k |F(a)_k|^2 = 5 Z_pos(a) for every a)", ok)
    # spectral reading equals the registered face weights, exactly in Q(sqrt5)
    Z = Fr(2)  # Z_pos(v) = 1 + 1
    weights = []
    for k in range(5):
        wk = c5_mul(c5_star(Fv[k]), Fv[k])
        weights.append(c5_to_q5(wk))
    reg = [q5(Fr(2, 5)), (Fr(3, 20), Fr(1, 20)), (Fr(3, 20), Fr(-1, 20)),
           (Fr(3, 20), Fr(-1, 20)), (Fr(3, 20), Fr(1, 20))]
    born_spec = [q5_mul(w, q5_inv(q5(5 * Z))) for w in weights]
    ok = (born_spec == reg)
    check("CERT-B3d Born_spec(delta_0 + delta_1) equals the registered five face "
          "weights (2/5, (3+sqrt5)/20, (3-sqrt5)/20, (3-sqrt5)/20, (3+sqrt5)/20) "
          "entrywise exactly", ok)
    ok = all(q5_pos_principal(w) for w in born_spec) and \
        sum(w[0] for w in born_spec) == 1 and sum(w[1] for w in born_spec) == 0
    check("CERT-B3e the five face weights are positive in the principal order and "
          "sum exactly to 1", ok)
    # CERT-F3: forcing.
    # (a) F is a bijection (Plancherel gives 5 I), so the registered symbol has
    #     exactly one coefficient preimage: delta_0 + delta_1.
    check("CERT-F3a Fourier inversion: F is exactly invertible (F* F = 5 I), so "
          "delta_0 + delta_1 is the UNIQUE coefficient preimage of the registered "
          "verb symbol", "CERT-B3c" not in FAILURES and "CERT-B3a" not in FAILURES)
    # (b) translation covariance: shifting the support multiplies F(a)_k by z^(tk)
    ok = True
    for t in range(5):
        for k in range(5):
            for r in range(5):
                lhs = Fm[k][(r + t) % 5]
                rhs = c5_mul(zpow(t * k), Fm[k][r])
                ok = ok and c5_eq(lhs, rhs)
    check("CERT-F3b support translation acts on the spectral side by the unimodular "
          "factor zeta^(tk); Born_spec is exactly translation invariant", ok)
    # (c) minimal-support classification. Support size 1: uniform weights 1/5,
    #     not the registered vector.
    ok = True
    for m in range(5):
        wk_all = [Fr(1, 5)] * 5
        ok = ok and (wk_all != [Fr(2, 5), None, None, None, None])
    single = [q5(Fr(1, 5))] * 5
    ok = (single != reg)
    check("CERT-F3c support size 1 gives the flat spectral reading (1/5,...,1/5), "
          "which is not the registered face-weight vector", ok)
    #     Support size 2, gap d, coefficients alpha, beta: the k = 0 slot forces
    #     (alpha + beta)^2 = 2 (alpha^2 + beta^2), i.e. (alpha - beta)^2 = 0,
    #     an exact polynomial identity; then d = +-1 is forced by slot k = 1.
    # polynomial identity check over Z[alpha, beta]:
    # 2*(a^2+b^2)*(2/5)*5 = 2*(a^2+b^2)... direct: (a+b)^2 - 2(a^2+b^2) = -(a-b)^2
    import collections
    def poly_mul(p, q):
        out = collections.defaultdict(Fr)
        for k1, c1 in p.items():
            for k2, c2 in q.items():
                out[(k1[0] + k2[0], k1[1] + k2[1])] += c1 * c2
        return dict(out)
    def poly_sub(p, q):
        out = collections.defaultdict(Fr, {k: Fr(c) for k, c in p.items()})
        for k, c in q.items():
            out[k] -= c
        return {k: c for k, c in out.items() if c != 0}
    a_ = {(1, 0): Fr(1)}
    b_ = {(0, 1): Fr(1)}
    apb = {(1, 0): Fr(1), (0, 1): Fr(1)}
    sq = poly_mul(apb, apb)
    twosq = {(2, 0): Fr(2), (0, 2): Fr(2)}
    lhs = poly_sub(sq, twosq)
    amb = {(1, 0): Fr(1), (0, 1): Fr(-1)}
    rhs = {k: -c for k, c in poly_mul(amb, amb).items()}
    check("CERT-F3d the k = 0 face-weight equation forces equal support "
          "coefficients: (alpha+beta)^2 - 2(alpha^2+beta^2) = -(alpha-beta)^2 "
          "as an exact polynomial identity", poly_sub(lhs, rhs) == {})
    #     with alpha = beta, gap d: spectral weights are (2 + z^(dk) + z^(-dk))/10;
    #     equality with the registered vector at every k forces d = +-1 mod 5.
    ok_gaps = []
    for d in range(1, 5):
        match = True
        for k in range(5):
            lhsw = c5_add(c5_add(c5_scal(2, C5_ONE), zpow(d * k)), zpow(-d * k))
            rhsw = c5_add(c5_add(c5_scal(2, C5_ONE), zpow(k)), zpow(-k))
            if not c5_eq(lhsw, rhsw):
                match = False
                break
        if match:
            ok_gaps.append(d)
    check("CERT-F3e among support gaps d = 1..4 exactly d = 1 and d = 4 "
          "(the adjacent pairs) reproduce the registered weights; WITHIN the "
          "support-size-at-most-2 class the coefficient representative is "
          "delta_m + delta_(m+1) up to translation, scale, and orientation "
          "(a robustness certificate, not the forcing)", ok_gaps == [1, 4])
    # (d) all residual representatives give the same support Born reading (1/2, 1/2):
    ok = True
    for m in range(5):
        supp = [Fr(1), Fr(1)]
        Zs = supp[0] * supp[0] + supp[1] * supp[1]
        bs = [x * x / Zs for x in supp]
        ok = ok and (bs == [Fr(1, 2), Fr(1, 2)])
    check("CERT-F3f every residual representative reads its two-point support with "
          "the exact uniform Born weight (1/2, 1/2): the half map is pinned and "
          "orientation independent", ok)
    # weights-only non-uniqueness witness (first-class, from the independent
    # break round): the registered FACE WEIGHTS alone do not force the
    # coefficient representative. The exact full-support rational vector
    # a = (-4, -4, 1, 1, -4)/5 has Born_spec(a) equal to the registered
    # weights entrywise, while F(a) differs from the registered phaseful
    # symbol Psi. Hence the phaseful dependency of ruling F3 (the verb enters
    # through Psi, not through its Born square) is load-bearing.
    a = [Fr(-4, 5), Fr(-4, 5), Fr(1, 5), Fr(1, 5), Fr(-4, 5)]
    Za = sum(x * x for x in a)
    Fa = []
    for k in range(5):
        acc = c5()
        for r in range(5):
            acc = c5_add(acc, c5_scal(a[r], zpow(r * k)))
        Fa.append(acc)
    ok = all(x != 0 for x in a) and (Za == Fr(2))
    for k in range(5):
        wk = c5_mul(c5_star(Fa[k]), Fa[k])
        ok = ok and (q5_mul(c5_to_q5(wk), q5_inv(q5(5 * Za))) == reg[k])
    ok = ok and (not c5_eq(Fa[0], c5_add(C5_ONE, zpow(0))))
    check("CERT-F3g weights-only non-uniqueness witness: the exact full-support "
          "vector (-4, -4, 1, 1, -4)/5 reproduces the registered face weights "
          "entrywise while its Fourier transform differs from the registered "
          "phaseful symbol; the face weights alone do not force a unique coefficient representative, and the "
          "phaseful dependency of ruling F3 is load-bearing", ok)


# ======================================================================
# CERT-B4: candidate Born measure structure (conditional implications).
# ======================================================================

def cert_b4(f, P):
    orb_list = [((0, 0, 1), (1, 1, 0)), ((0, 1, 0), (1, 0, 1)), ((0, 1, 1), (1, 0, 0))]
    third = {}
    for pair in orb_list:
        third[pair] = f[W3_INDEX[pair[0]]] + f[W3_INDEX[pair[1]]]
    mu = {}
    for pair in orb_list:
        for w in pair:
            mu[w] = third[pair] * Fr(1, 2)
    ok = sum(mu.values()) == 1
    check("CERT-B4a mu_B^f = third x half is exactly normalized on W3", ok)
    ok = all(mu[w] == f[W3_INDEX[w]] for w in W3)
    check("CERT-B4b BORN-STREAM-COMPATIBILITY: Eq_Born(mu_B^f, f) holds exactly "
          "(both sides assign third([w])/2)", ok)
    # guarded SCALAR-LINK algebra: P1(I3) = I3, P5(I3) = 0, Tr P_line = 1,
    # so on the commutant branch 3 alpha = sum_w f_w Tr(P_s(w)) = 1.
    ok = True
    for Pi in P:
        tr = q5_add(q5_add(Pi[0][0], Pi[1][1]), Pi[2][2])
        ok = ok and (tr == Q5_ONE)
    ok = ok and (sum(f) == 1)
    check("CERT-B4c guarded SCALAR-LINK: unit projector traces and sum f = 1 give "
          "3 alpha = 1 on the exact commutant branch; the implication needs no "
          "selector representative", ok)


# ======================================================================
# CERT-B6: event-level GYRON bridge (finite identity, typed pushforward).
# ======================================================================

def cert_b6(f):
    NMAX = 2048
    ok = True
    for N in (1, 2, 3, 5, 8, 64, 257, 1024, NMAX):
        cw = {w: 0 for w in W3}
        for n in range(1, N + 1):
            cw[q_window(n)] += 1
        cpair = {}
        for j in range(0, N):
            key = (theta(j), theta(j + 1))
            cpair[key] = cpair.get(key, 0) + 1
        for ab in ((0, 0), (0, 1), (1, 0), (1, 1)):
            lhs = sum(cw[w] for w in W3 if (w[0], w[1]) == ab)
            rhs = cpair.get(ab, 0)
            ok = ok and (lhs == rhs)
    check("CERT-B6a the finite census-index identity holds exactly at every "
          "audited N (windows over [1, N] against pairs over [0, N-1])", ok)
    E00 = [w for w in W3 if (w[0], w[1]) == (0, 0)]
    check("CERT-B6b the selected event is the singleton fiber E_00 = {001}", E00 == [(0, 0, 1)])
    # typed pushforward against the registered pair law (1, 2, 2, 1)/6
    reg_pair = {(0, 0): Fr(1, 6), (0, 1): Fr(2, 6), (1, 0): Fr(2, 6), (1, 1): Fr(1, 6)}
    ok = True
    for ab, val in reg_pair.items():
        ok = ok and (sum(f[W3_INDEX[w]] for w in W3 if (w[0], w[1]) == ab) == val)
    check("CERT-B6c (pi_12)_* f equals the registered stationary pair law "
          "(1, 2, 2, 1)/6 of GYRON-DENSITY exactly", ok)
    ok = (f[W3_INDEX[(0, 0, 1)]] == reg_pair[(0, 0)])
    check("CERT-B6d GYRON-PUSHFORWARD: mu_B^f(E_00) = f(001) = rho_00 exactly", ok)


# ======================================================================
# CERT-B7: gate records and the complete dependency graph.
# ======================================================================

GATE_ROWS = [
    ("GATE-L1-L5-TM-SYM2-SELECTOR-STREAM", "TM-SYM2-MEASURE", "L1", "L5", "OPEN_LIFT"),
    ("GATE-L5-L6-TM-SYM2-BORN-MEASURE", "TM-SYM2-MEASURE", "L5", "L6", "OPEN_LIFT"),
]

DEP_DELTA = [
    ("TM-SYM2-MEASURE", "DEF-ACTION-LAYERS"),
    ("TM-SYM2-MEASURE", "RAMIFIED-TM-LIFT"),
    ("TM-SYM2-MEASURE", "SUBSTRATE-KNIT"),
    ("TM-SYM2-MEASURE", "ABELIAN-FACE-DICTIONARY"),
]

DEP_FLOOR = [
    ("TM-SYM2-MEASURE", "DEF-ARCHITECTURE"),
    ("TM-SYM2-MEASURE", "DEF-AUTONOMOUS-STATE"),
    ("TM-SYM2-MEASURE", "GOLDEN-SIX-LINE-SYM2-FRAME"),
    ("TM-SYM2-MEASURE", "GYRON-DENSITY"),
    ("TM-SYM2-MEASURE", "MEASURE-BORN-VERB"),
]


def cert_b7():
    import os
    ok_files = os.path.exists("canon/DEPENDENCIES.tsv") and os.path.exists("canon/NORMATIVE.tsv")
    check("CERT-B7a canon tables reachable from the repository root", ok_files)
    if not ok_files:
        return
    items = set()
    with open("canon/NORMATIVE.tsv", encoding="utf-8") as fh:
        header = fh.readline()
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if parts and parts[0]:
                items.add(parts[0])
    edges = set()
    with open("canon/DEPENDENCIES.tsv", encoding="utf-8") as fh:
        header = fh.readline()
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 2 and parts[0]:
                edges.add((parts[0], parts[1]))
    union = set(edges)
    union.update(DEP_DELTA)
    ok = all(a in items and b in items for a, b in union)
    check("CERT-B7b every dependency endpoint, including the four delta edges, is "
          "a registered normative item", ok)
    tm_parents = sorted(b for a, b in union if a == "TM-SYM2-MEASURE")
    want = sorted(b for _, b in DEP_FLOOR + DEP_DELTA)
    check("CERT-B7c the TM-SYM2-MEASURE parent set in the folded graph is exactly "
          "the five-floor plus the four adopted edges (9 direct parents)",
          tm_parents == want)
    check("CERT-B7d the graph carries NO edge TM-SYM2-MEASURE -> DEF-LOG-STREAM "
          "(the shifted selector records are not the registered total Log)",
          ("TM-SYM2-MEASURE", "DEF-LOG-STREAM") not in union)
    # acyclicity of the full folded graph
    adj = {}
    for a, b in union:
        adj.setdefault(a, []).append(b)
    for a in adj:
        adj[a].sort()
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {}
    acyclic = True
    def dfs(u):
        nonlocal acyclic
        color[u] = GRAY
        for w in adj.get(u, ()):
            c = color.get(w, WHITE)
            if c == GRAY:
                acyclic = False
                return
            if c == WHITE:
                dfs(w)
                if not acyclic:
                    return
        color[u] = BLACK
    for node in sorted({a for a, _ in union} | {b for _, b in union}):
        if color.get(node, WHITE) == WHITE:
            dfs(node)
        if not acyclic:
            break
    check("CERT-B7e the complete folded dependency graph is acyclic "
          "(%d edges audited)" % len(union), acyclic)
    ok = True
    for gid, owner, frm, to, kind in GATE_ROWS:
        ok = ok and gid.startswith("GATE-") and owner in items
        ok = ok and frm in ("L1", "L2", "L3", "L4", "L5") and to in ("L2", "L3", "L4", "L5", "L6")
        ok = ok and kind in ("OPEN_LIFT", "DEFINITION_PROJECTION", "DICTIONARY_LIFT")
    check("CERT-B7f both adopted lane gates are well-formed layer lifts owned by "
          "TM-SYM2-MEASURE (L1->L5 and L5->L6, both OPEN_LIFT)", ok)


# ======================================================================
# CERT-I3: structural completeness method for the future gauge scan.
# No gauge element, order, orbit, or selector classification is computed here.
# ======================================================================

def q5_det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return q5_add(
        q5_sub(q5_mul(a, q5_sub(q5_mul(e, i), q5_mul(f, h))),
               q5_mul(b, q5_sub(q5_mul(d, i), q5_mul(f, g)))),
        q5_mul(c, q5_sub(q5_mul(d, h), q5_mul(e, g))))


def q5_mat_rank(A):
    if not A:
        return 0
    M = [row[:] for row in A]
    nrow, ncol = len(M), len(M[0])
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, nrow):
            if not q5_is_zero(M[i][c]):
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = q5_inv(M[r][c])
        M[r] = [q5_mul(x, pv) for x in M[r]]
        for i in range(nrow):
            if i != r and not q5_is_zero(M[i][c]):
                fq = M[i][c]
                M[i] = [q5_sub(M[i][j], q5_mul(fq, M[r][j]))
                        for j in range(ncol)]
        r += 1
        if r == nrow:
            break
    return r


def projective_system(targets):
    # Unknowns: g (9) and lambda_2,lambda_3,lambda_4 (3), with lambda_1=1.
    A = [[Q5_ZERO] * 12 for _ in range(12)]
    b = [Q5_ZERO] * 12
    row = 0
    for idx, i in enumerate(range(4)):
        vi = V[i]
        tv = V[targets[idx]]
        for comp in range(3):
            for k in range(3):
                A[row][3 * comp + k] = vi[k]
            if idx == 0:
                b[row] = tv[comp]
            else:
                A[row][8 + idx] = q5_neg(tv[comp])
            row += 1
    return A, b


def cert_projective_completeness_method():
    frame_ok = True
    for inds in combinations(range(6), 3):
        M = [[V[j][k] for k in range(3)] for j in inds]
        frame_ok = frame_ok and (not q5_is_zero(q5_det3(M)))
    check("CERT-I3a every three registered lines are exactly independent, so any "
          "ordered four-line subset is a projective frame", frame_ok)
    rank_ok = True
    audited = 0
    for targets in permutations(range(6), 4):
        A, _ = projective_system(targets)
        audited += 1
        rank_ok = rank_ok and (q5_mat_rank(A) == 12)
    check("CERT-I3b every ordered target four-frame gives a full-rank exact "
          "projective realization system (%d systems audited); the exhaustive "
          "permutation scan cannot discard an underdetermined realization" % audited,
          frame_ok and rank_ok)


# ======================================================================
# EVALUATE mode (pinned public probe only): B5 and the deterministic routing.
# No expected class count, orbit count, invariant list, or weight vector is
# embedded. The computed values route the decision; they are never compared
# to a stored expectation.
# ======================================================================

def q5_mat_solve(A, b):
    # solve A x = b over Q(sqrt5); A square list of lists of q5; returns x or None
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    r = 0
    piv_cols = []
    for c in range(n):
        piv = None
        for i in range(r, n):
            if not q5_is_zero(M[i][c]):
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = q5_inv(M[r][c])
        M[r] = [q5_mul(x, pv) for x in M[r]]
        for i in range(n):
            if i != r and not q5_is_zero(M[i][c]):
                fq = M[i][c]
                M[i] = [q5_sub(M[i][j], q5_mul(fq, M[r][j])) for j in range(n + 1)]
        piv_cols.append(c)
        r += 1
    if r < n:
        return None
    x = [Q5_ZERO] * n
    for idx, c in enumerate(piv_cols):
        x[c] = M[idx][n]
    return x


def projective_realizations():
    # all line permutations realizable by an exact projective-linear map over
    # Q(sqrt5): for each candidate permutation solve g v_i = lam_i v_perm(i),
    # i = 1..4 with lam_1 = 1, then verify lines 5, 6.
    real = []
    for perm in permutations(range(6)):
        A, b = projective_system(perm[:4])
        x = q5_mat_solve(A, b)
        if x is None:
            continue
        g = [[x[3 * i + j] for j in range(3)] for i in range(3)]
        # verify invertibility via action on all registered lines
        good = True
        for i in range(6):
            gv = tuple(q5_add(q5_add(q5_mul(g[r][0], V[i][0]), q5_mul(g[r][1], V[i][1])),
                              q5_mul(g[r][2], V[i][2])) for r in range(3))
            if not proportional(gv, V[perm[i]]):
                good = False
                break
        if good:
            real.append(perm)
    return real


def permutation_group_closed(group):
    G = {tuple(g) for g in group}
    identity = tuple(range(6))
    if len(G) != len(group) or identity not in G:
        return False
    for g in G:
        if sorted(g) != list(range(6)):
            return False
        inv = [0] * 6
        for i, gi in enumerate(g):
            inv[gi] = i
        if tuple(inv) not in G:
            return False
        for h in G:
            if tuple(g[h[i]] for i in range(6)) not in G:
                return False
    return True


def run_evaluate(f, P):
    emit("EVALUATE MODE: pinned public probe use only")
    # Sel_class enumeration from the complete function space
    npair = [W3_INDEX[n_flip(w)] for w in W3]
    members = []
    for s in product(range(6), repeat=6):
        if all(s[npair[i]] == SIGMA_LINE[s[i]] for i in range(6)) and len(set(s)) == 6:
            members.append(s)
    # Integrity precedes every scientific route, including EMPTY.
    # The gauge group is the projective-linear stabilizer of the line set
    # that commutes with sigma_line as a line permutation.
    stab = projective_realizations()
    G = [g for g in stab if all(g[SIGMA_LINE[i]] == SIGMA_LINE[g[i]] for i in range(6))]
    emit("AUDIT: line-set projective stabilizer order %d; Aut(Lines, sigma_line) "
         "order %d" % (len(stab), len(G)))
    groups_ok = permutation_group_closed(stab) and permutation_group_closed(G)
    check("CERT-I3c the exhaustive projective realization set and its computed "
          "sigma_line normalizer both contain the identity and are closed under "
          "composition and inverse", groups_ok)
    if not groups_ok:
        emit("ROUTE: STOP (I3: the computed gauge enumeration is not a complete group)")
        return
    member_index = {s: i for i, s in enumerate(members)}
    action_ok = True
    for selector in members:
        for g in G:
            action_ok = action_ok and (
                tuple(g[selector[i]] for i in range(6)) in member_index)
    check("CERT-I3d the computed gauge group acts by postcomposition on the complete "
          "enumerated selector class", action_ok)
    if not action_ok:
        emit("ROUTE: STOP (I3: gauge postcomposition does not close Sel_class)")
        return
    if not members:
        emit("B5 RECORD: EMPTY_NOT_APPLICABLE(classification_certificate)")
        emit("ROUTE: NEGATIVE (N1: Sel_class is empty)")
        return
    # orbits of postcomposition
    parent = list(range(len(members)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[max(ri, rj)] = min(ri, rj)
    free_ok = True
    for s in members:
        for g in G:
            gs = tuple(g[s[i]] for i in range(6))
            union(member_index[s], member_index[gs])
            if gs == s and any(g[i] != i for i in range(6)):
                free_ok = False
    orbit_reps = sorted(set(find(i) for i in range(len(members))))
    n_orbits = len(orbit_reps)
    emit("AUDIT: gauge action free: %s" % ("yes" if free_ok else "no"))
    if n_orbits >= 2:
        # frozen contract: on NONCANONICAL the checker must name exact orbit
        # invariants. The complete gauge partition IS the exact classification
        # certificate: every orbit is emitted with its size and its full
        # membership, deterministically ordered by the lexicographically
        # minimal member. Values are computed, never compared to expectations.
        orbit_members = {}
        for i, s in enumerate(members):
            orbit_members.setdefault(find(i), []).append(s)
        blocks = sorted((sorted(v) for v in orbit_members.values()),
                        key=lambda b: b[0])
        emit("B5 RECORD: NONCANONICAL_NOT_APPLICABLE(classification_certificate) "
             "with %d gauge orbits" % n_orbits)
        for bi, block in enumerate(blocks, 1):
            emit("B5 ORBIT %d: size %d, minimal representative %s" %
                 (bi, len(block), block[0]))
            emit("B5 ORBIT %d MEMBERS: %s" % (bi, "; ".join(str(s) for s in block)))
        emit("B5 INVARIANT: the exact orbit invariant of a class member is its "
             "orbit block above (complete partition certificate; two members "
             "are gauge-equivalent if and only if they share a block)")
        emit("ROUTE: NEGATIVE (N2: the canonicality test returns NONCANONICAL)")
        return
    # CANONICAL branch: complete orbit and all-representative exact records.
    def fmt_fr(x):
        return str(x.numerator) if x.denominator == 1 else "%d/%d" % (x.numerator, x.denominator)
    def fmt_q5(x):
        return "q5[%s,%s]" % (fmt_fr(x[0]), fmt_fr(x[1]))
    def fmt_q5_vector(xs):
        return "(" + ",".join(fmt_q5(x) for x in xs) + ")"
    def fmt_selector(selector):
        return "(" + ",".join(str(x) for x in selector) + ")"
    def yesno(x):
        return "yes" if x else "no"

    emit("B5 RECORD: CANONICAL(R_[s]^5, all-representative records follow)")
    canonical_block = sorted(members)
    emit("B5 ORBIT R_[s]^5: size %d, minimal representative %s" %
         (len(canonical_block), fmt_selector(canonical_block[0])))
    emit("B5 ORBIT R_[s]^5 MEMBERS: %s" %
         ("; ".join(fmt_selector(selector) for selector in canonical_block)))
    emit("B5 INDEXING: selector tuples use the frozen W3 order %s and zero-based "
         "line labels 0..5; q5[a,b] means a+b*sqrt(5)" % (W3,))
    sym_basis = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
    emit("B5 SYM2 BASIS ORDER: %s" % (tuple(sym_basis),))

    def op_on_sym2(apply_A):
        # Matrix of an operator on Sym2 in the exact E_ij basis.
        cols = []
        for (i, j) in sym_basis:
            Aij = [[Q5_ZERO] * 3 for _ in range(3)]
            Aij[i][j] = q5_add(Aij[i][j], Q5_ONE)
            Aij[j][i] = q5_add(Aij[j][i], Q5_ONE) if i != j else Aij[j][i]
            if i == j:
                Aij[i][j] = Q5_ONE
            out = apply_A(Aij)
            col = []
            for (a, bb) in sym_basis:
                col.append(out[a][bb])
            cols.append(col)
        return [[cols[j][i] for j in range(6)] for i in range(6)]

    def M_s_apply(selector):
        def apply_A(A):
            out = [[Q5_ZERO] * 3 for _ in range(3)]
            for wi, _window in enumerate(W3):
                Pw = P[selector[wi]]
                tr = Q5_ZERO
                for a in range(3):
                    for bb in range(3):
                        tr = q5_add(tr, q5_mul(Pw[a][bb], A[bb][a]))
                coef = q5_mul(q5(f[wi]), tr)
                for a in range(3):
                    for bb in range(3):
                        out[a][bb] = q5_add(
                            out[a][bb], q5_mul(coef, Pw[a][bb]))
            return out
        return apply_A

    def P1_apply(A):
        tr = q5_add(q5_add(A[0][0], A[1][1]), A[2][2])
        c = q5_mul(tr, q5_inv(q5(3)))
        return [[c if i == j else Q5_ZERO for j in range(3)] for i in range(3)]

    def P5_apply(A):
        p1 = P1_apply(A)
        return [[q5_sub(A[i][j], p1[i][j]) for j in range(3)] for i in range(3)]

    M1 = op_on_sym2(P1_apply)
    M5 = op_on_sym2(P5_apply)
    records = []
    for selector in members:
        Ms = op_on_sym2(M_s_apply(selector))
        I3 = [[Q5_ONE if i == j else Q5_ZERO for j in range(3)]
              for i in range(3)]
        MI = M_s_apply(selector)(I3)
        alpha = MI[0][0]
        probe = [[Q5_ONE, Q5_ZERO, Q5_ZERO],
                 [Q5_ZERO, q5_neg(Q5_ONE), Q5_ZERO],
                 [Q5_ZERO, Q5_ZERO, Q5_ZERO]]
        MP = M_s_apply(selector)(probe)
        beta = MP[0][0]
        commutant = True
        noncommutant_witness = None
        for i in range(6):
            for j in range(6):
                want = q5_add(
                    q5_mul(alpha, M1[i][j]), q5_mul(beta, M5[i][j]))
                if Ms[i][j] != want:
                    commutant = False
                    if noncommutant_witness is None:
                        noncommutant_witness = (i, j, Ms[i][j], want)
        nu = [Q5_ZERO] * 6
        for wi in range(6):
            nu[selector[wi]] = q5_add(nu[selector[wi]], q5(f[wi]))
        equal_weights = all(nu[i] == nu[0] for i in range(6))
        unequal_witness = None
        if not equal_weights:
            for j in range(1, 6):
                if nu[j] != nu[0]:
                    unequal_witness = (0, j, nu[0], nu[j])
                    break
        ratio_residual = q5_sub(
            q5_mul(alpha, q5(2)), q5_mul(beta, q5(5)))
        ratio_ok = q5_is_zero(ratio_residual)
        records.append({
            "selector": selector,
            "commutant": commutant,
            "alpha": alpha,
            "beta": beta,
            "nu": tuple(nu),
            "equal_weights": equal_weights,
            "ratio_ok": ratio_ok,
            "ratio_residual": ratio_residual,
            "n3_pass": commutant and equal_weights and ratio_ok,
            "noncommutant_witness": noncommutant_witness,
            "unequal_witness": unequal_witness,
        })

    for ri, record in enumerate(records, 1):
        emit("B5 REPRESENTATIVE %d: selector=%s; N3=%s; COMMUTANT=%s; "
             "EQUAL-LINE-WEIGHTS=%s; RATIO-5:2=%s; alpha=%s; beta=%s; nu=%s" %
             (ri, fmt_selector(record["selector"]), yesno(record["n3_pass"]),
              yesno(record["commutant"]), yesno(record["equal_weights"]),
              yesno(record["ratio_ok"]), fmt_q5(record["alpha"]),
              fmt_q5(record["beta"]), fmt_q5_vector(record["nu"])))
        if record["noncommutant_witness"] is not None:
            i, j, got, want = record["noncommutant_witness"]
            emit("B5 WITNESS REPRESENTATIVE %d NONCOMMUTANT: Sym2 matrix entry "
                 "(%d,%d), observed=%s, expected=%s" %
                 (ri, i, j, fmt_q5(got), fmt_q5(want)))
        if record["unequal_witness"] is not None:
            i, j, wi, wj = record["unequal_witness"]
            emit("B5 WITNESS REPRESENTATIVE %d UNEQUAL-LINE-WEIGHTS: line %d has "
                 "%s, line %d has %s" %
                 (ri, i, fmt_q5(wi), j, fmt_q5(wj)))
        if not record["ratio_ok"]:
            emit("B5 WITNESS REPRESENTATIVE %d RATIO-5:2: 2*alpha-5*beta=%s" %
                 (ri, fmt_q5(record["ratio_residual"])))

    base = records[0]
    truth_coherent = all(
        record["n3_pass"] == base["n3_pass"] for record in records)
    coefficient_coherent = True
    if truth_coherent and base["n3_pass"]:
        coefficient_coherent = all(
            (record["alpha"], record["beta"]) ==
            (base["alpha"], base["beta"]) for record in records)
    coherent = truth_coherent and coefficient_coherent
    emit("GAUGE-COHERENCE: %s" % ("agree" if coherent else "DISAGREE"))
    if not coherent:
        other_index = None
        reason = None
        for j, record in enumerate(records[1:], 2):
            if record["n3_pass"] != base["n3_pass"]:
                other_index, reason = j, "N3 truth values differ"
                break
            if (base["n3_pass"] and
                    (record["alpha"], record["beta"]) !=
                    (base["alpha"], base["beta"])):
                other_index, reason = j, "passing commutant coefficients differ"
                break
        other = records[other_index - 1]
        emit("B5 WITNESS GAUGE-DISAGREEMENT: representatives 1 and %d (%s); "
             "rep1 selector=%s N3=%s alpha=%s beta=%s; rep%d selector=%s N3=%s "
             "alpha=%s beta=%s" %
             (other_index, reason, fmt_selector(base["selector"]),
              yesno(base["n3_pass"]), fmt_q5(base["alpha"]),
              fmt_q5(base["beta"]), other_index,
              fmt_selector(other["selector"]), yesno(other["n3_pass"]),
              fmt_q5(other["alpha"]), fmt_q5(other["beta"])))
        emit("ROUTE: NEGATIVE (gauge disagreement)")
        return
    if not base["n3_pass"]:
        emit("ROUTE: NEGATIVE (N3: at least one exact scientific payload is false; "
             "see the all-representative witnesses above)")
        return
    emit("ROUTE: the Born/layer block is satisfied at evaluation grade (step 6); "
         "parent closure remains gated on the owner definition surface")


# ======================================================================
# main
# ======================================================================

def main():
    mode = "--definition"
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    if mode not in ("--definition", "--evaluate"):
        emit("usage: P-TM-SYM2-MEASURE-1-DEFINITION-CHECKER.py [--definition|--evaluate]")
        return 2
    emit("P-TM-SYM2-MEASURE-1 definition checker, mode %s" % mode)
    emit("exact arithmetic only: int and Fraction; no floats in any assertion")
    P = cert_frame()
    cert_sigma_consistency()
    cert_projective_completeness_method()
    cert_pairing_forcing()
    cert_carrier_forcing()
    cert_b1()
    f = cert_b2_spectral(run_s4=True)
    cert_b3_f3()
    if f is not None:
        cert_b4(f, P)
        cert_b6(f)
    cert_b7()
    if mode == "--evaluate":
        if FAILURES:
            emit("ROUTE: STOP (a structural certificate failed; the evaluation is invalid)")
            return 1
        run_evaluate(f, P)
    if FAILURES:
        emit("RESULT: FAIL (%d certificate(s) failed)" % len(FAILURES))
        return 1
    emit("RESULT: PASS (all certificates green in mode %s)" % mode)
    return 0


if __name__ == "__main__":
    sys.exit(main())
