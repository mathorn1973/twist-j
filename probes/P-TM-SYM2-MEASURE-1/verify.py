#!/usr/bin/env python3
"""Hermetic result-neutral wrapper for P-TM-SYM2-MEASURE-1.

The three raw byte blocks below are exact public Canon-v16 inputs. Static
review extracts and compares them without importing or executing this file.
The formal no-argument run validates them, stages the table inputs in a
temporary root, and invokes the embedded checker's main exactly once with
--evaluate. No expected scientific outcome is encoded.
"""

from __future__ import annotations

import hashlib
import io
import os
from pathlib import Path
import sys
import tempfile


EXPECTED_ENV = {
    "LC_ALL": "C",
    "LANG": "C",
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONHASHSEED": "0",
    "TZ": "UTC",
}

CHECKER_SOURCE = rb'''#!/usr/bin/env python3
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
'''
NORMATIVE_SOURCE = rb'''item_id	item_type	claim_id	status	layer	gate_ids	statement_source
AXIOM-J	AXIOM			FOUNDATION		canon/CANON.md::Axiom (A0)
DEF-MJ	DEFINITION			FOUNDATION		canon/CANON.md::Primitive and architecture inventory
DEF-CHECKPOINT	DEFINITION			L1		canon/CANON.md::2. Time, space, and the decoder
DEF-ODOMETER-ORBIT	DEFINITION			L1		canon/CANON.md::2. Time, space, and the decoder
DEF-KERNEL-GENERATORS	DEFINITION			L1		canon/CANON.md::3. The kernel and the census
DEF-SELECTOR	DEFINITION			L1		canon/CANON.md::2. Time, space, and the decoder
DEF-AUTONOMOUS-STATE	DEFINITION			L1		canon/CANON.md::2. Time, space, and the decoder
DEF-LOG-STREAM	DEFINITION			L5	GATE-L1-L5-LOG-PROJECTION	canon/CANON.md::2. Time, space, and the decoder
DEF-DECODER-MATTER	DEFINITION			MULTI		canon/CANON.md::2. Time, space, and the decoder
DEF-DECODER-GEOMETRY	DEFINITION			MULTI		canon/CANON.md::2. Time, space, and the decoder
DEF-DECODER-CLOCK	DEFINITION			MULTI		canon/CANON.md::2. Time, space, and the decoder
DEF-DECODER-COMPLETION-CONTRACT	DEFINITION			MULTI		canon/CANON.md::2. Time, space, and the decoder
DEF-ARCHITECTURE	DEFINITION			MULTI		canon/CANON.md::Primitive and architecture inventory
DEF-ACTION-LAYERS	DEFINITION			MULTI		canon/CANON.md::Conventions
DEF-PUBLIC-STATUSES	DEFINITION			NOT_APPLICABLE		canon/CANON.md::Statuses
ANCHOR-ELECTRON-MASS	EMPIRICAL_ANCHOR			MULTI		canon/CANON.md::Primitive and architecture inventory
J-UNIT	THEOREM	J-UNIT	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
J-PROJECTIONS	THEOREM	J-PROJECTIONS	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
AXIOM-PROJECTION-DICTIONARY	DICTIONARY	AXIOM-PROJECTION-DICTIONARY	D	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
PI-FROM-J	THEOREM	PI-FROM-J	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
J-GOLDEN-BRIDGE	THEOREM	J-GOLDEN-BRIDGE	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
J-STEP	THEOREM	J-STEP	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
J-MODULUS-CHORD	THEOREM	J-MODULUS-CHORD	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
J-TENTH-ROOT	THEOREM	J-TENTH-ROOT	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
J-RAMIFIED-CHORD	THEOREM	J-RAMIFIED-CHORD	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
PLENUM-POINT	THEOREM	PLENUM-POINT	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
LOG-AXES-INDEPENDENCE	THEOREM	LOG-AXES-INDEPENDENCE	T	NOT_APPLICABLE		canon/CANON.md::1. The axiom and the two projections
ALPHA-SEED	THEOREM	ALPHA-SEED	T	NOT_APPLICABLE		canon/CANON.md::6. Alpha and the observable register
BORN-FACE-WEIGHTS	THEOREM	BORN-FACE-WEIGHTS	T	NOT_APPLICABLE		canon/CANON.md::8. The measure and Born
BORN-HALF-ANGLE	THEOREM	BORN-HALF-ANGLE	T	NOT_APPLICABLE		canon/CANON.md::8. The measure and Born
BORN-RESIDUAL-SPLIT	THEOREM	BORN-RESIDUAL-SPLIT	T	NOT_APPLICABLE		canon/CANON.md::8. The measure and Born
SPIN-BISECTOR	THEOREM	SPIN-BISECTOR	T	NOT_APPLICABLE		canon/CANON.md::8. The measure and Born
BORN-ORDER-STAIRCASE	THEOREM	BORN-ORDER-STAIRCASE	T	NOT_APPLICABLE		canon/CANON.md::8. The measure and Born
CENSUS-313	COMPUTATION	CENSUS-313	C	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
CENSUS-Z5-SHEET	COMPUTATION	CENSUS-Z5-SHEET	C	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
CENSUS-PAIRING	COMPUTATION	CENSUS-PAIRING	C	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
CENSUS-HOSTING	COMPUTATION	CENSUS-HOSTING	C	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
DIRAC-LADDER	DICTIONARY	DIRAC-LADDER	D	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
LADDER-LIGHTCONE	THEOREM	LADDER-LIGHTCONE	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
SPINOR-FLOOR	THEOREM	SPINOR-FLOOR	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
FIB-ROOT-TIES	THEOREM	FIB-ROOT-TIES	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
FIB-ROOT-CARRIER	DICTIONARY	FIB-ROOT-CARRIER	D	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
DIRAC-STEP-THEOREMS	THEOREM	DIRAC-STEP-THEOREMS	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
DIRAC-STEP	DICTIONARY	DIRAC-STEP	D	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
LADDER-SPIN-PLACES	THEOREM	LADDER-SPIN-PLACES	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
CHECKERBOARD-GAUSS-TOWER	THEOREM	CHECKERBOARD-GAUSS-TOWER	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
FERMIONIZER	THEOREM	FERMIONIZER	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
LADDER-ALTERNATOR-BASIS	THEOREM	LADDER-ALTERNATOR-BASIS	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
TM-BREATH-TOWER	THEOREM	TM-BREATH-TOWER	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
BOOST-READING-SPLIT	THEOREM	BOOST-READING-SPLIT	T	NOT_APPLICABLE		canon/CANON.md::10. Relativity as counting
BOOST-COUNT-LADDER	DICTIONARY	BOOST-COUNT-LADDER	D	NOT_APPLICABLE		canon/CANON.md::10. Relativity as counting
OBSERVER-ALTERNATOR	DICTIONARY	OBSERVER-ALTERNATOR	D	NOT_APPLICABLE		canon/CANON.md::10. Relativity as counting
BOOST-AXIS	DICTIONARY	BOOST-AXIS	D	NOT_APPLICABLE		canon/CANON.md::10. Relativity as counting
COLOR-RETURN-D5	THEOREM	COLOR-RETURN-D5	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-TORSOR-HOLONOMY	THEOREM	COLOR-TORSOR-HOLONOMY	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-SPLIT-12	DICTIONARY	COLOR-SPLIT-12	D	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-LADDER-DICTIONARY	DICTIONARY	COLOR-LADDER-DICTIONARY	D	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-DYNAMICAL-COLOR	FALSIFIED	COLOR-DYNAMICAL-COLOR	F	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-KIN-NORMALIZER	THEOREM	COLOR-KIN-NORMALIZER	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-KINEMATICAL-GL2	DICTIONARY	COLOR-KINEMATICAL-GL2	D	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-CORE-2I	THEOREM	COLOR-CORE-2I	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-GOLDEN-TABLE	THEOREM	COLOR-GOLDEN-TABLE	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-MCKAY-E8	THEOREM	COLOR-MCKAY-E8	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-MOMENT-FINGERPRINT	THEOREM	COLOR-MOMENT-FINGERPRINT	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-SPECTRAL-INVARIANTS	THEOREM	COLOR-SPECTRAL-INVARIANTS	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-DICKSON-RAMIFICATION	THEOREM	COLOR-DICKSON-RAMIFICATION	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-KLEIN-REDUCTION	THEOREM	COLOR-KLEIN-REDUCTION	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-INTEGRAL-LIFT	THEOREM	COLOR-INTEGRAL-LIFT	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
COLOR-MEASURE-TRANSPORT	THEOREM	COLOR-MEASURE-TRANSPORT	T	NOT_APPLICABLE		canon/CANON.md::12. The color door
KAHLER-CAPACITY	THEOREM	KAHLER-CAPACITY	T	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
FRW-CANONICAL-FORM	THEOREM	FRW-CANONICAL-FORM	T	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
DE-TRACE-DENSITY-UNDERDETERMINATION	THEOREM	DE-TRACE-DENSITY-UNDERDETERMINATION	T	L5		canon/CANON.md::13. Gravity and cosmology
GRAVITY-BRIDGE-LAW	DICTIONARY	GRAVITY-BRIDGE-LAW	D	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
MU-TAU-COEFFICIENT	THEOREM	MU-TAU-COEFFICIENT	T	NOT_APPLICABLE		canon/CANON.md::7. The mass ladder and the parity law
MU-EXCHANGE-IDENTITY	THEOREM	MU-EXCHANGE-IDENTITY	T	NOT_APPLICABLE		canon/CANON.md::7. The mass ladder and the parity law
MASS-LADDER-FORMS	DICTIONARY	MASS-LADDER-FORMS	D	NOT_APPLICABLE		canon/CANON.md::7. The mass ladder and the parity law
PARITY-LAW	THEOREM	PARITY-LAW	T	NOT_APPLICABLE		canon/CANON.md::7. The mass ladder and the parity law
BRIDGE-DEFECT	THEOREM	BRIDGE-DEFECT	T	NOT_APPLICABLE		canon/CANON.md::7. The mass ladder and the parity law
WEINBERG-TREE	THEOREM	WEINBERG-TREE	T	NOT_APPLICABLE		canon/CANON.md::6. Alpha and the observable register
HYPERCHARGE-LAW	THEOREM	HYPERCHARGE-LAW	T	NOT_APPLICABLE		canon/CANON.md::6. Alpha and the observable register
WEINBERG-FORM	DICTIONARY	WEINBERG-FORM	D	NOT_APPLICABLE		canon/CANON.md::6. Alpha and the observable register
MAXWELL-BIANCHI	THEOREM	MAXWELL-BIANCHI	T	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
MAXWELL-GAUSS-CHAIN	THEOREM	MAXWELL-GAUSS-CHAIN	T	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
MAXWELL-AMPERE-CHAIN	THEOREM	MAXWELL-AMPERE-CHAIN	T	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
MAXWELL-OBSTRUCTION-P	THEOREM	MAXWELL-OBSTRUCTION-P	T	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
MAXWELL-CLOSED	DICTIONARY	MAXWELL-CLOSED	D	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
ALPHA-PREFACTOR-UNIFICATION	THEOREM	ALPHA-PREFACTOR-UNIFICATION	T	NOT_APPLICABLE		canon/CANON.md::6. Alpha and the observable register
ALPHA-FORM	DICTIONARY	ALPHA-FORM	D	NOT_APPLICABLE		canon/CANON.md::6. Alpha and the observable register
ALPHA-VALUE-DIGITS	COMPUTATION	ALPHA-VALUE-DIGITS	C	NOT_APPLICABLE		canon/CANON.md::6. Alpha and the observable register
TT-LINEAR-ZERO	THEOREM	TT-LINEAR-ZERO	T	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
TT-QUADRATIC-INDUCED	DICTIONARY	TT-QUADRATIC-INDUCED	D	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
GYRON-DENSITY	THEOREM	GYRON-DENSITY	T	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
COSMOLOGY-READING-DICTIONARY	DICTIONARY	COSMOLOGY-READING-DICTIONARY	D	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
COSMOLOGY-REGISTER	DICTIONARY	COSMOLOGY-REGISTER	D	NOT_APPLICABLE		canon/CANON.md::13. Gravity and cosmology
CONFORMAL-PREFACTOR	DICTIONARY	CONFORMAL-PREFACTOR	D	L5		canon/CANON.md::13. Gravity and cosmology
TT-SQUARING-DECODER	DICTIONARY	TT-SQUARING-DECODER	D	NOT_APPLICABLE		canon/CANON.md::14. The gravitational wave program
SCHWARZSCHILD-TT-ENDPOINT	THEOREM	SCHWARZSCHILD-TT-ENDPOINT	T	NOT_APPLICABLE		canon/CANON.md::14. The gravitational wave program
TT-QUADRATIC-GERM	DICTIONARY	TT-QUADRATIC-GERM	D	L2		canon/CANON.md::14. The gravitational wave program
COUPLINGS-DETERMINE	THEOREM	COUPLINGS-DETERMINE	T	NOT_APPLICABLE		canon/CANON.md::15. Couplings, instruments, and metrology
DEWITT-TWELVES	THEOREM	DEWITT-TWELVES	T	NOT_APPLICABLE		canon/CANON.md::15. Couplings, instruments, and metrology
METRO-TICK	THEOREM	METRO-TICK	T	NOT_APPLICABLE		canon/CANON.md::15. Couplings, instruments, and metrology
MEASURE-SPATIAL-ONLY	THEOREM	MEASURE-SPATIAL-ONLY	T	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
STRONG-SEED	DICTIONARY	STRONG-SEED	D	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
HYPERPLANE-BOUNDARY-CLASS	THEOREM	HYPERPLANE-BOUNDARY-CLASS	T	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
HYPERPLANE-BOUNDARY-REALIZATION	COMPUTATION	HYPERPLANE-BOUNDARY-REALIZATION	C	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
CODEC-TR4	THEOREM	CODEC-TR4	T	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
PHIBIT-NOT-TAU	FALSIFIED	PHIBIT-NOT-TAU	F	NOT_APPLICABLE		canon/CANON.md::11. The pentit ring and the magic boundary
KERNEL-WEDGE-AFFINITY	THEOREM	KERNEL-WEDGE-AFFINITY	T	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
KERNEL-WEDGE-COUPLING	THEOREM	KERNEL-WEDGE-COUPLING	T	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
KERNEL-WEDGE-LINEAR-STRATA	THEOREM	KERNEL-WEDGE-LINEAR-STRATA	T	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
KERNEL-WEDGE-AFFINE-MIX	THEOREM	KERNEL-WEDGE-AFFINE-MIX	T	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
KERNEL-CELL-COMPONENTS	COMPUTATION	KERNEL-CELL-COMPONENTS	C	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
KERNEL-MACRO-READING	DICTIONARY	KERNEL-MACRO-READING	D	NOT_APPLICABLE		canon/CANON.md::3. The kernel and the census
ODOMETER-INTERNALIZED	DICTIONARY	ODOMETER-INTERNALIZED	D	NOT_APPLICABLE		canon/CANON.md::2. Time, space, and the decoder
READING-SPLIT	DICTIONARY	READING-SPLIT	D	NOT_APPLICABLE		canon/CANON.md::2. Time, space, and the decoder
TIME-QUANTUM-TOWER	COMPUTATION	TIME-QUANTUM-TOWER	C	NOT_APPLICABLE		canon/CANON.md::2. Time, space, and the decoder
DEGREES-BY-PRIME	THEOREM	DEGREES-BY-PRIME	T	NOT_APPLICABLE		canon/CANON.md::4. The two places
Z2-PLACES-SPLIT	THEOREM	Z2-PLACES-SPLIT	T	NOT_APPLICABLE		canon/CANON.md::4. The two places
TWO-PLACE-PHYSICS	DICTIONARY	TWO-PLACE-PHYSICS	D	NOT_APPLICABLE		canon/CANON.md::4. The two places
I-BILOCATED	DICTIONARY	I-BILOCATED	D	NOT_APPLICABLE		canon/CANON.md::4. The two places
SILVER-RING-FACTS	COMPUTATION	SILVER-RING-FACTS	C	NOT_APPLICABLE		canon/CANON.md::4. The two places
SILVER-SIBLING	DICTIONARY	SILVER-SIBLING	D	NOT_APPLICABLE		canon/CANON.md::4. The two places
FORCE-WEYL-HOLONOMY	THEOREM	FORCE-WEYL-HOLONOMY	T	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
FORCE-AS-CURVATURE	DICTIONARY	FORCE-AS-CURVATURE	D	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
COULOMB-GREEN-COMPUTATION	COMPUTATION	COULOMB-GREEN-COMPUTATION	C	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
COULOMB-PROJECTION	DICTIONARY	COULOMB-PROJECTION	D	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
FORCE-POLAR-SIGN	DICTIONARY	FORCE-POLAR-SIGN	D	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
ABELIAN-FACE-DICTIONARY	DICTIONARY	ABELIAN-FACE-DICTIONARY	D	NOT_APPLICABLE		canon/CANON.md::5. The force is the curvature
MEASURE-BORN-VERB	DICTIONARY	MEASURE-BORN-VERB	D	NOT_APPLICABLE	GATE-L5-L6-BORN-READING	canon/CANON.md::8. The measure and Born
KERNEL-CELL-DICTIONARY	DICTIONARY	KERNEL-CELL-DICTIONARY	D	NOT_APPLICABLE		canon/CANON.md::8. The measure and Born
SUBSTRATE-KNIT	THEOREM	SUBSTRATE-KNIT	T	NOT_APPLICABLE		canon/CANON.md::8. The measure and Born
METRO-ADMISSIBILITY	OBLIGATION	METRO-ADMISSIBILITY	O	NOT_APPLICABLE	GATE-L5-L6-METRO-NORMALIZATION	canon/CANON.md::18. The frontier
METRO-EDGE-SCALE	OBLIGATION	METRO-EDGE-SCALE	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
QUANT-SUBSTRATE	OBLIGATION	QUANT-SUBSTRATE	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
COLOR-MEASURE-SELECTION	OBLIGATION	COLOR-MEASURE-SELECTION	O	NOT_APPLICABLE	GATE-L4-L6-COLOR-MEASURE	canon/CANON.md::18. The frontier
TT-SOURCE	OBLIGATION	TT-SOURCE	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
QNM-LEAVER-MU	OBLIGATION	QNM-LEAVER-MU	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
POL-READ	DICTIONARY	POL-READ	D	NOT_APPLICABLE		canon/CANON.md::14. The gravitational wave program
TT-VECTOR-STATE-NORMALIZATION	OBLIGATION	TT-VECTOR-STATE-NORMALIZATION	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
FRW-INHOM	OBLIGATION	FRW-INHOM	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
DRESS-CROSSCOUNT	OBLIGATION	DRESS-CROSSCOUNT	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
NS-TILT	HYPOTHESIS	NS-TILT	H	NOT_APPLICABLE		canon/CANON.md::18. The frontier
DE-CONFORMAL-WEIGHT	OBLIGATION	DE-CONFORMAL-WEIGHT	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
ALPHA-S-RUNNING	OBLIGATION	ALPHA-S-RUNNING	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
SCHEME-DICTIONARY	OBLIGATION	SCHEME-DICTIONARY	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
GENERATIONS-L3	OBLIGATION	GENERATIONS-L3	O	L3	GATE-L2-L3-GENERATIONS	canon/CANON.md::18. The frontier
SPIN-LIFT-FORCED	FALSIFIED	SPIN-LIFT-FORCED	F	L3		canon/CANON.md::12. The color door
KC3-PLENUM-READOUT	HYPOTHESIS	KC3-PLENUM-READOUT	H	NOT_APPLICABLE		canon/CANON.md::18. The frontier
TM-SYM2-MEASURE	HYPOTHESIS	TM-SYM2-MEASURE	H	MULTI	GATE-L1-L5-TM-SYM2-SELECTOR-STREAM;GATE-L5-L6-TM-SYM2-BORN-MEASURE	canon/CANON.md::18. The frontier
QUADRATIC-DECODER-DATA	OBLIGATION	QUADRATIC-DECODER-DATA	O	MULTI		canon/CANON.md::18. The frontier
NEUTRON-DELTA-EM	OBLIGATION	NEUTRON-DELTA-EM	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
PROTON-RESIDUAL-IS-QCD	OBLIGATION	PROTON-RESIDUAL-IS-QCD	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
SQRT-PHI-TIME-GRAVITY	OBLIGATION	SQRT-PHI-TIME-GRAVITY	O	MULTI		canon/CANON.md::18. The frontier
KERNEL-CONNECT-ALL-K	THEOREM	KERNEL-CONNECT-ALL-K	T	L1		canon/CANON.md::3. The kernel and the census
CURVATURE-HISTORICAL-TRACE	THEOREM	CURVATURE-HISTORICAL-TRACE	T	L2		canon/CANON.md::2. Time, space, and the decoder
CURVATURE-TRACE-VALUE	FALSIFIED	CURVATURE-TRACE-VALUE	F	L2		canon/CANON.md::2. Time, space, and the decoder
CURVATURE-OPERATOR-CANONICAL	OBLIGATION	CURVATURE-OPERATOR-CANONICAL	O	L2	GATE-L1-L2-CURVATURE-CANONICAL	canon/CANON.md::2. Time, space, and the decoder
OBSERVER-WRITE-PORT	HYPOTHESIS	OBSERVER-WRITE-PORT	H	NOT_APPLICABLE		canon/CANON.md::18. The frontier
PHOTON-WINDOW-COORDINATES	THEOREM	PHOTON-WINDOW-COORDINATES	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
PHOTON-UNIVERSAL-BIT	THEOREM	PHOTON-UNIVERSAL-BIT	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
MONOPOLE-FIFTHS	THEOREM	MONOPOLE-FIFTHS	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
MONOPOLE-COST	COMPUTATION	MONOPOLE-COST	C	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
KAPPA-BOUNDS	THEOREM	KAPPA-BOUNDS	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
KAPPA-SHAPES	COMPUTATION	KAPPA-SHAPES	C	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
CENTER-SPLIT-RECIPROCITY	THEOREM	CENTER-SPLIT-RECIPROCITY	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
CENTER-SPLIT-CLOSURE	THEOREM	CENTER-SPLIT-CLOSURE	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
CENTER-SPLIT-SELECTION	DICTIONARY	CENTER-SPLIT-SELECTION	D	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
ELECTRON-G-RATIO	THEOREM	ELECTRON-G-RATIO	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
ELECTRON-G-DOUBLE-COVER	THEOREM	ELECTRON-G-DOUBLE-COVER	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
ELECTRON-G-TREE	DICTIONARY	ELECTRON-G-TREE	D	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
ELECTRON-SIGN-LAWS	THEOREM	ELECTRON-SIGN-LAWS	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
ELECTRON-SIGN	DICTIONARY	ELECTRON-SIGN	D	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
PHOTON-WINDOW-PROOF	OBLIGATION	PHOTON-WINDOW-PROOF	O	NOT_APPLICABLE		canon/CANON.md::18. The frontier
PENTIT-ROOT-FACTS	THEOREM	PENTIT-ROOT-FACTS	T	NOT_APPLICABLE		canon/CANON.md::11. The pentit ring and the magic boundary
PENTIT-ROOT-READING	DICTIONARY	PENTIT-ROOT-READING	D	NOT_APPLICABLE		canon/CANON.md::11. The pentit ring and the magic boundary
MAGIC-PRIME-GATE	THEOREM	MAGIC-PRIME-GATE	T	NOT_APPLICABLE		canon/CANON.md::11. The pentit ring and the magic boundary
QUBIT-FROM-F5	THEOREM	QUBIT-FROM-F5	T	NOT_APPLICABLE		canon/CANON.md::11. The pentit ring and the magic boundary
BELL-MAGIC-BOUNDARY	THEOREM	BELL-MAGIC-BOUNDARY	T	L3		canon/CANON.md::11. The pentit ring and the magic boundary
P5-ROOT-SELECTION	THEOREM	P5-ROOT-SELECTION	T	NOT_APPLICABLE		canon/CANON.md::16. p = 5 and the wall
ENTROPY-LAYER-BRIDGE	OBLIGATION	ENTROPY-LAYER-BRIDGE	O	MULTI	GATE-L2-L5-ENTROPY-BRIDGE	canon/CANON.md::ENTROPY-LAYER-BRIDGE
ENTROPY-CYLINDER-CUT	FALSIFIED	ENTROPY-CYLINDER-CUT	F	L5		canon/CANON.md::ENTROPY-CYLINDER-CUT [F]
ENTROPY-LIFT-DEFECT	FALSIFIED	ENTROPY-LIFT-DEFECT	F	L5		canon/CANON.md::ENTROPY-LIFT-DEFECT [F]
ENTROPY-JOINT-CESARO-LAW	COMPUTATION	ENTROPY-JOINT-CESARO-LAW	C	MULTI		canon/CANON.md::ENTROPY-JOINT-CESARO-LAW [C]
ENTROPY-BLOCK-HALVING	COMPUTATION	ENTROPY-BLOCK-HALVING	C	L5		canon/CANON.md::ENTROPY-BLOCK-HALVING [C]
ENTROPY-LIVING-SET	COMPUTATION	ENTROPY-LIVING-SET	C	L5		canon/CANON.md::ENTROPY-LIVING-SET [C]
ENTROPY-UNIQUE-PAST	COMPUTATION	ENTROPY-UNIQUE-PAST	C	L5		canon/CANON.md::ENTROPY-UNIQUE-PAST [C]
ENTROPY-COUNT-MATCH	COMPUTATION	ENTROPY-COUNT-MATCH	C	L5		canon/CANON.md::ENTROPY-COUNT-MATCH [C]
ENTROPY-PENTAGON-QUOTIENT	COMPUTATION	ENTROPY-PENTAGON-QUOTIENT	C	L5		canon/CANON.md::ENTROPY-PENTAGON-QUOTIENT [C]
ENTROPY-AFFINE-COCYCLE	COMPUTATION	ENTROPY-AFFINE-COCYCLE	C	L5		canon/CANON.md::ENTROPY-AFFINE-COCYCLE [C]
ENTROPY-COMPONENT-NOGO	COMPUTATION	ENTROPY-COMPONENT-NOGO	C	L5		canon/CANON.md::ENTROPY-COMPONENT-NOGO [C]
ENTROPY-MIRROR-LAW	COMPUTATION	ENTROPY-MIRROR-LAW	C	L5		canon/CANON.md::ENTROPY-MIRROR-LAW [C]
CURVATURE-HISTORICAL-GAUSS-SPLIT	THEOREM	CURVATURE-HISTORICAL-GAUSS-SPLIT	T	L2		canon/CANON.md::2. Time, space, and the decoder
PENTAGON-NORMALIZATION	THEOREM	PENTAGON-NORMALIZATION	T	L5		canon/CANON.md::16. p = 5 and the wall
J-LI-TORAL-HAAR-NOGO	THEOREM	J-LI-TORAL-HAAR-NOGO	T	L6		canon/CANON.md::J-LI-TORAL-HAAR-NOGO [T]
J-LI-E8-SHELL-MULTIPLICITY-NOGO	THEOREM	J-LI-E8-SHELL-MULTIPLICITY-NOGO	T	L6		canon/CANON.md::J-LI-E8-SHELL-MULTIPLICITY-NOGO [T]
MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER	FALSIFIED	MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER	F	L6		canon/CANON.md::MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER [F]
J-LI-LAMBDA-HAAR-HS-NOGO	THEOREM	J-LI-LAMBDA-HAAR-HS-NOGO	T	L6		canon/CANON.md::J-LI-LAMBDA-HAAR-HS-NOGO [T]
LAMBDA-BOUNDARY-HS-KOOPMAN	FALSIFIED	LAMBDA-BOUNDARY-HS-KOOPMAN	F	L6		canon/CANON.md::LAMBDA-BOUNDARY-HS-KOOPMAN [F]
J-LI-LAMBDA-SHIFT-NOGO	THEOREM	J-LI-LAMBDA-SHIFT-NOGO	T	L6		canon/CANON.md::J-LI-LAMBDA-SHIFT-NOGO [T]
LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER	FALSIFIED	LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER	F	L6		canon/CANON.md::LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER [F]
LAMBDA-COCYCLE-ANGLES	HYPOTHESIS	LAMBDA-COCYCLE-ANGLES	H	L6		canon/CANON.md::LAMBDA-COCYCLE-ANGLES [H]
O-R2-K-JUNCTION-PIN	COMPUTATION	O-R2-K-JUNCTION-PIN	C	L6		canon/CANON.md::O-R2-K-JUNCTION-PIN [C]
RAMIFIED-TM-LIFT	THEOREM	RAMIFIED-TM-LIFT	T	L1		canon/CANON.md::3. The kernel and the census
CARRY-J-CHECKPOINT	THEOREM	CARRY-J-CHECKPOINT	T	L1		canon/CANON.md::3. The kernel and the census
CARRY-PENTAD	THEOREM	CARRY-PENTAD	T	L1		canon/CANON.md::3. The kernel and the census
METAL-TRACE-CASCADE	THEOREM	METAL-TRACE-CASCADE	T	L2		canon/CANON.md::4. The two places
SQRT-PHI-DIGIT-LIFT	THEOREM	SQRT-PHI-DIGIT-LIFT	T	L1		canon/CANON.md::3. The kernel and the census
GOLDEN-SIX-LINE-SYM2-FRAME	THEOREM	GOLDEN-SIX-LINE-SYM2-FRAME	T	L1		canon/CANON.md::13. Gravity and cosmology
FIRED-COMMUTATOR-NOGO	THEOREM	FIRED-COMMUTATOR-NOGO	T	L1		canon/CANON.md::FIRED-COMMUTATOR-NOGO [T]
TIME-CUT-READING	DICTIONARY	TIME-CUT-READING	D	NOT_APPLICABLE		canon/CANON.md::TIME-CUT-READING [D]
'''
DEPENDENCIES_SOURCE = rb'''item_id	depends_on	relation	basis
DEF-MJ	AXIOM-J	REQUIRES	M_J is multiplication by J
DEF-AUTONOMOUS-STATE	DEF-CHECKPOINT	REQUIRES	Omega contains the finite checkpoint
DEF-AUTONOMOUS-STATE	DEF-ODOMETER-ORBIT	REQUIRES	Omega contains the forward odometer orbit
DEF-AUTONOMOUS-STATE	DEF-KERNEL-GENERATORS	REQUIRES	U applies one declared generator
DEF-AUTONOMOUS-STATE	DEF-SELECTOR	REQUIRES	U reads the declared selector
DEF-LOG-STREAM	DEF-AUTONOMOUS-STATE	REQUIRES	the Log is a derived orbit record
DEF-DECODER-MATTER	DEF-AUTONOMOUS-STATE	REQUIRES	D_matter reads a forward orbit
DEF-DECODER-GEOMETRY	DEF-DECODER-MATTER	REQUIRES	geometry reads MatterData
DEF-DECODER-CLOCK	DEF-DECODER-GEOMETRY	REQUIRES	clock reads accumulated geometry
DEF-DECODER-COMPLETION-CONTRACT	DEF-DECODER-CLOCK	REQUIRES	the completion-contract schema refines the declared partial decoder chain without asserting a completed decoder
DEF-DECODER-COMPLETION-CONTRACT	DEF-ACTION-LAYERS	REQUIRES	every declared contract transition records its L1-L6 endpoints without asserting or authorizing a lift
DEF-ARCHITECTURE	DEF-AUTONOMOUS-STATE	REQUIRES	declared architecture contains Omega and U
DEF-ARCHITECTURE	DEF-DECODER-CLOCK	REQUIRES	declared architecture contains the partial decoder
J-UNIT	AXIOM-J	REQUIRES	unit theorem starts from J
J-PROJECTIONS	AXIOM-J	REQUIRES	polar decomposition starts from J
J-MODULUS-CHORD	AXIOM-J	REQUIRES	chord identity starts from J
PI-FROM-J	AXIOM-J	REQUIRES	principal logarithm identity starts from J
J-TENTH-ROOT	AXIOM-J	REQUIRES	root identity starts from J
J-GOLDEN-BRIDGE	AXIOM-J	REQUIRES	bridge identities start from J
J-STEP	DEF-MJ	REQUIRES	J-STEP is the matrix action of M_J
PLENUM-POINT	AXIOM-J	REQUIRES	plenum identities start from J
J-RAMIFIED-CHORD	AXIOM-J	REQUIRES	ramified chord starts from J
LOG-AXES-INDEPENDENCE	AXIOM-J	REQUIRES	the two logarithmic axes are projections of J
AXIOM-PROJECTION-DICTIONARY	J-PROJECTIONS	REQUIRES	registry scope names the theorem input
AXIOM-PROJECTION-DICTIONARY	PLENUM-POINT	REQUIRES	registry scope names the theorem input
AXIOM-PROJECTION-DICTIONARY	J-MODULUS-CHORD	REQUIRES	registry scope names the theorem input
AXIOM-PROJECTION-DICTIONARY	J-RAMIFIED-CHORD	REQUIRES	registry scope names the theorem input
BOOST-COUNT-LADDER	BOOST-READING-SPLIT	REQUIRES	count dictionary rests on the exact split
READING-SPLIT	CODEC-TR4	REQUIRES	linear leg is CODEC-TR4
SILVER-SIBLING	SILVER-RING-FACTS	REQUIRES	dictionary rests on finite ring facts
FORCE-AS-CURVATURE	FORCE-WEYL-HOLONOMY	REQUIRES	curvature reading rests on the Weyl theorem
MEASURE-BORN-VERB	BORN-FACE-WEIGHTS	REQUIRES	registry scope names the theorem input
COSMOLOGY-READING-DICTIONARY	TT-LINEAR-ZERO	REQUIRES	dictionary reads the exact zero response
COSMOLOGY-READING-DICTIONARY	GYRON-DENSITY	REQUIRES	dictionary reads the exact density
COSMOLOGY-READING-DICTIONARY	COSMOLOGY-REGISTER	REQUIRES	dictionary reads the committed forms
ELECTRON-G-TREE	ELECTRON-G-RATIO	REQUIRES	dictionary rests on the exact ratio
ELECTRON-G-TREE	ELECTRON-G-DOUBLE-COVER	REQUIRES	dictionary rests on the exact double cover
ELECTRON-SIGN	ELECTRON-SIGN-LAWS	REQUIRES	dictionary rests on the exhaustive laws
FRW-INHOM	FRW-CANONICAL-FORM	REQUIRES	inhomogeneous extension starts from the homogeneous theorem
DE-TRACE-DENSITY-UNDERDETERMINATION	FRW-CANONICAL-FORM	REQUIRES	the registered homogeneous continuity identity is the sole coefficient relation tested for density-character selection
DE-CONFORMAL-WEIGHT	DE-TRACE-DENSITY-UNDERDETERMINATION	BOUNDED_BY	FRW continuity alone has at least two exact density-character solutions, so the open dictionary is not derived from that relation
TM-SYM2-MEASURE	GYRON-DENSITY	REQUIRES	registered measure residual uses rho = 1/6
MASS-LADDER-FORMS	NEUTRON-DELTA-EM	BOUNDED_BY	neutron comparison remains open
TT-QUADRATIC-INDUCED	TT-VECTOR-STATE-NORMALIZATION	BOUNDED_BY	normalization remains open
COSMOLOGY-REGISTER	NS-TILT	BOUNDED_BY	tilt remains a live hypothesis
CONFORMAL-PREFACTOR	FRW-INHOM	BOUNDED_BY	inhomogeneous action remains open
CONFORMAL-PREFACTOR	METRO-EDGE-SCALE	BOUNDED_BY	SI clause remains open
STRONG-SEED	ALPHA-S-RUNNING	BOUNDED_BY	running remains open
STRONG-SEED	SCHEME-DICTIONARY	BOUNDED_BY	measurement scheme remains open
ELECTRON-G-TREE	QUANT-SUBSTRATE	BOUNDED_BY	quantum substrate remains open
ALPHA-SEED	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BORN-FACE-WEIGHTS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BORN-HALF-ANGLE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BORN-RESIDUAL-SPLIT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SPIN-BISECTOR	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BORN-ORDER-STAIRCASE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CENSUS-313	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CENSUS-Z5-SHEET	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CENSUS-PAIRING	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CENSUS-HOSTING	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DIRAC-LADDER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
LADDER-LIGHTCONE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SPINOR-FLOOR	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FIB-ROOT-TIES	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FIB-ROOT-CARRIER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DIRAC-STEP-THEOREMS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DIRAC-STEP	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
LADDER-SPIN-PLACES	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CHECKERBOARD-GAUSS-TOWER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FERMIONIZER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
LADDER-ALTERNATOR-BASIS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TM-BREATH-TOWER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BOOST-READING-SPLIT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BOOST-COUNT-LADDER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
OBSERVER-ALTERNATOR	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BOOST-AXIS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-RETURN-D5	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-TORSOR-HOLONOMY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-SPLIT-12	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-LADDER-DICTIONARY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-DYNAMICAL-COLOR	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-KIN-NORMALIZER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-KINEMATICAL-GL2	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-CORE-2I	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-GOLDEN-TABLE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-MCKAY-E8	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-MOMENT-FINGERPRINT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-SPECTRAL-INVARIANTS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-DICKSON-RAMIFICATION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-KLEIN-REDUCTION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-INTEGRAL-LIFT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-MEASURE-TRANSPORT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KAHLER-CAPACITY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FRW-CANONICAL-FORM	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DE-TRACE-DENSITY-UNDERDETERMINATION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
GRAVITY-BRIDGE-LAW	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MU-TAU-COEFFICIENT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MU-EXCHANGE-IDENTITY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MASS-LADDER-FORMS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PARITY-LAW	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BRIDGE-DEFECT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
WEINBERG-TREE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
HYPERCHARGE-LAW	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
WEINBERG-FORM	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MAXWELL-BIANCHI	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MAXWELL-GAUSS-CHAIN	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MAXWELL-AMPERE-CHAIN	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MAXWELL-OBSTRUCTION-P	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MAXWELL-CLOSED	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ALPHA-PREFACTOR-UNIFICATION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ALPHA-FORM	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ALPHA-VALUE-DIGITS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TT-LINEAR-ZERO	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TT-QUADRATIC-INDUCED	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
GYRON-DENSITY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COSMOLOGY-READING-DICTIONARY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COSMOLOGY-REGISTER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CONFORMAL-PREFACTOR	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TT-SQUARING-DECODER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SCHWARZSCHILD-TT-ENDPOINT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TT-QUADRATIC-GERM	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COUPLINGS-DETERMINE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DEWITT-TWELVES	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
METRO-TICK	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MEASURE-SPATIAL-ONLY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
STRONG-SEED	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
HYPERPLANE-BOUNDARY-CLASS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
HYPERPLANE-BOUNDARY-REALIZATION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CODEC-TR4	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PHIBIT-NOT-TAU	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-WEDGE-AFFINITY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-WEDGE-COUPLING	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-WEDGE-LINEAR-STRATA	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-WEDGE-AFFINE-MIX	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-CELL-COMPONENTS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-MACRO-READING	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ODOMETER-INTERNALIZED	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
READING-SPLIT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TIME-QUANTUM-TOWER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DEGREES-BY-PRIME	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
Z2-PLACES-SPLIT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TWO-PLACE-PHYSICS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
I-BILOCATED	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SILVER-RING-FACTS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SILVER-SIBLING	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FORCE-WEYL-HOLONOMY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FORCE-AS-CURVATURE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COULOMB-GREEN-COMPUTATION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COULOMB-PROJECTION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FORCE-POLAR-SIGN	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ABELIAN-FACE-DICTIONARY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MEASURE-BORN-VERB	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-CELL-DICTIONARY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SUBSTRATE-KNIT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
METRO-ADMISSIBILITY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
METRO-EDGE-SCALE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
QUANT-SUBSTRATE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
COLOR-MEASURE-SELECTION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TT-SOURCE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
QNM-LEAVER-MU	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
POL-READ	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TT-VECTOR-STATE-NORMALIZATION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
FRW-INHOM	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DRESS-CROSSCOUNT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
NS-TILT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
DE-CONFORMAL-WEIGHT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ALPHA-S-RUNNING	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SCHEME-DICTIONARY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
GENERATIONS-L3	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SPIN-LIFT-FORCED	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KC3-PLENUM-READOUT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
TM-SYM2-MEASURE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
QUADRATIC-DECODER-DATA	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
NEUTRON-DELTA-EM	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PROTON-RESIDUAL-IS-QCD	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
SQRT-PHI-TIME-GRAVITY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KERNEL-CONNECT-ALL-K	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CURVATURE-HISTORICAL-TRACE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: the frozen historical operator is conditional on the declared checkpoint architecture
CURVATURE-TRACE-VALUE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: the falsified historical proposal is conditional on the declared checkpoint architecture
CURVATURE-OPERATOR-CANONICAL	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: canonical spatial-curvature selection is conditional on the declared architecture
OBSERVER-WRITE-PORT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PHOTON-WINDOW-COORDINATES	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PHOTON-UNIVERSAL-BIT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MONOPOLE-FIFTHS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MONOPOLE-COST	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KAPPA-BOUNDS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
KAPPA-SHAPES	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CENTER-SPLIT-RECIPROCITY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CENTER-SPLIT-CLOSURE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
CENTER-SPLIT-SELECTION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ELECTRON-G-RATIO	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ELECTRON-G-DOUBLE-COVER	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ELECTRON-G-TREE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ELECTRON-SIGN-LAWS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ELECTRON-SIGN	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PHOTON-WINDOW-PROOF	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PENTIT-ROOT-FACTS	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
PENTIT-ROOT-READING	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
MAGIC-PRIME-GATE	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
QUBIT-FROM-F5	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
BELL-MAGIC-BOUNDARY	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
P5-ROOT-SELECTION	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: every downstream statement is conditional on the declared architecture
ENTROPY-CYLINDER-CUT	DEF-ARCHITECTURE	REQUIRES	the finite-cylindrical ansatz is formulated on the declared checkpoint architecture and Thue-Morse driver
ENTROPY-LIFT-DEFECT	DEF-ARCHITECTURE	REQUIRES	the literal lift falsifier is a statement about the declared finite-generator presentation
ENTROPY-JOINT-CESARO-LAW	DEF-ARCHITECTURE	REQUIRES	the frozen window law is computed for the declared driven kernel
ENTROPY-BLOCK-HALVING	DEF-ARCHITECTURE	REQUIRES	the block maps are compositions of the declared branch maps along the declared driver
ENTROPY-LIVING-SET	DEF-ARCHITECTURE	REQUIRES	the living halves and restricted bijections are finite facts of the declared driven kernel
ENTROPY-UNIQUE-PAST	ENTROPY-LIVING-SET	REQUIRES	the caterpillar backward structure uses the bijections between the two living halves
ENTROPY-COUNT-MATCH	ENTROPY-LIVING-SET	REQUIRES	the arithmetic carrier count is compared with the living-trajectory count
ENTROPY-PENTAGON-QUOTIENT	ENTROPY-LIVING-SET	REQUIRES	the pentagon partition is computed on the two declared living halves
ENTROPY-AFFINE-COCYCLE	ENTROPY-PENTAGON-QUOTIENT	REQUIRES	the affine cell maps use the finite pentagon quotient and its coherent level-2 gauge
ENTROPY-COMPONENT-NOGO	DEF-ARCHITECTURE	REQUIRES	the bounded cylinder systems are formulated on the declared driven kernel and frozen components
ENTROPY-MIRROR-LAW	ENTROPY-LIVING-SET	REQUIRES	the own-half involutions and alternating inverse maps refine the declared living-half bijections
ENTROPY-MIRROR-LAW	ENTROPY-PENTAGON-QUOTIENT	REQUIRES	the cell swap and reflection law use the canonical pentagon partition and frozen coherent level-2 gauge
ENTROPY-LAYER-BRIDGE	ENTROPY-CYLINDER-CUT	REQUIRES	the open selection family must be non-cylindrical because the finite-cylinder ansatz is falsified
ENTROPY-LAYER-BRIDGE	ENTROPY-JOINT-CESARO-LAW	REQUIRES	the remaining measure clause is equality with the frozen joint Cesaro law
ENTROPY-LAYER-BRIDGE	ENTROPY-BLOCK-HALVING	REQUIRES	the one-bit-per-scale computation constrains the unbounded driver dependence
ENTROPY-LAYER-BRIDGE	ENTROPY-UNIQUE-PAST	REQUIRES	the selection form uses the unique living past over the driver word
ENTROPY-LAYER-BRIDGE	ENTROPY-COUNT-MATCH	REQUIRES	the depth-five lambda carrier supplies exactly the living-set cardinality
ENTROPY-LAYER-BRIDGE	ENTROPY-PENTAGON-QUOTIENT	REQUIRES	the open selection must respect the finite equivariant pentagon quotient on the living carrier
ENTROPY-LAYER-BRIDGE	ENTROPY-AFFINE-COCYCLE	REQUIRES	the gauge-specific finite cocycle constrains but does not solve the open canonical selection problem
ENTROPY-LAYER-BRIDGE	ENTROPY-COMPONENT-NOGO	BOUNDED_BY	the 900 exact zero counts exclude only the enumerated component-local cylinder cases
ENTROPY-LAYER-BRIDGE	ENTROPY-MIRROR-LAW	REQUIRES	the open equivariant selection must be compatible with the finite mirror law on the living pentagon carrier
CURVATURE-HISTORICAL-GAUSS-SPLIT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: the frozen historical full-carrier split is conditional on the declared checkpoint architecture
CURVATURE-HISTORICAL-GAUSS-SPLIT	CURVATURE-HISTORICAL-TRACE	REQUIRES	the ambient member of the split is the previously typed historical operator and retains its exact trace anchor
CURVATURE-OPERATOR-CANONICAL	CURVATURE-HISTORICAL-GAUSS-SPLIT	BOUNDED_BY	the exact historical equality constrains one declared full-carrier candidate but does not select a canonical operator class
PENTAGON-NORMALIZATION	J-GOLDEN-BRIDGE	REQUIRES	the identity j = (J - 1)^3 identifies the fifth-root filter with the J-generated pentagon
J-LI-TORAL-HAAR-NOGO	J-STEP	REQUIRES	the named dimension-four specialization uses the public multiplication-by-J matrix M_J; the general no-go depends only on the frozen root-of-unity-free toral carrier class
J-LI-E8-SHELL-MULTIPLICITY-NOGO	COLOR-MCKAY-E8	REQUIRES	the E8 shell obstruction uses the public E8 identification; the probe independently supplies the theta-series shell multiplicities needed by the declared functional-calculus scope
MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER	J-LI-E8-SHELL-MULTIPLICITY-NOGO	REQUIRES	the falsified carrier is exactly the positive trace-class functional-calculus route excluded by the shell-multiplicity no-go
J-LI-LAMBDA-HAAR-HS-NOGO	J-RAMIFIED-CHORD	REQUIRES	the compact boundary is the lambda-adic completion named by the public ramified fifth-root chord; the no-go then uses its conductor filtration
LAMBDA-BOUNDARY-HS-KOOPMAN	J-LI-LAMBDA-HAAR-HS-NOGO	REQUIRES	the falsified Hilbert-Schmidt and S2 route is exactly the subroute excluded by the compact-boundary Hilbert-Schmidt theorem
LAMBDA-COCYCLE-ANGLES	J-LI-LAMBDA-HAAR-HS-NOGO	BOUNDED_BY	the theorem excludes Hilbert-Schmidt and S2 forms but explicitly leaves the all-vector cocycle form as the surviving bounded scope
LAMBDA-COCYCLE-ANGLES	J-LI-TORAL-HAAR-NOGO	REQUIRES	the compact-boundary cocycle hypothesis is the remaining Haar-Koopman local route after the toral Haar carrier no-go; it does not reopen that excluded carrier
O-R2-K-JUNCTION-PIN	PLENUM-POINT	REQUIRES	the computed junction identity uses the public plenum quantities s_J and phi and verifies their exact K-side arithmetic match
J-LI-LAMBDA-SHIFT-NOGO	J-RAMIFIED-CHORD	REQUIRES	the scaling carrier is defined by the lambda uniformizer from the public ramified fifth-root chord
J-LI-LAMBDA-SHIFT-NOGO	J-LI-TORAL-HAAR-NOGO	REQUIRES	the forced Li spectral-measure comparison is inherited from the toral Haar no-go, while the scaling probe supplies the absolutely-continuous shift contradiction
LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER	J-LI-LAMBDA-SHIFT-NOGO	REQUIRES	the falsified carrier is exactly the discrete-time single-unitary and declared tensor-composite class excluded by the scaling-shift no-go
KERNEL-CONNECT-ALL-K	KERNEL-WEDGE-AFFINITY	REQUIRES	the all-k proof imports the verbatim affine letter matrices and translations from the public kernel census before closing their Gamma-invariant translation span
KERNEL-CONNECT-ALL-K	KERNEL-WEDGE-COUPLING	REQUIRES	the all-k proof applies the registered pair of two-way CSUM transvections at every adjacent edge of the coupled ring; the new proof, not the prior pair statement alone, supplies the all-k transport step
KERNEL-CONNECT-ALL-K	KERNEL-CELL-COMPONENTS	BOUNDED_BY	the one-cell census gives nine components for {a, c, d, e}, so the theorem's k >= 2 lower boundary is exact and is not extended to k = 1
RAMIFIED-TM-LIFT	DEF-ARCHITECTURE	REQUIRES	Canon definition boundary: the L1 state and readout statement is conditional on the declared public architecture
RAMIFIED-TM-LIFT	DEF-ODOMETER-ORBIT	REQUIRES	the digit sum and carry cocycle use only the declared forward odometer carrier N_0 and do not extend parity to all of Z_2
RAMIFIED-TM-LIFT	PENTIT-ROOT-FACTS	REQUIRES	the ramified image J_lambda = 2 and its exact order-four orbit are inherited theorem inputs
RAMIFIED-TM-LIFT	QUBIT-FROM-F5	REQUIRES	the C4 to C2 sign quotient is the registered two-class quotient of F_5^*
RAMIFIED-TM-LIFT	CODEC-TR4	REQUIRES	the all-k realization and unique multiplier 2 use the exact fixed M_J/Tr_4 channel
CARRY-J-CHECKPOINT	RAMIFIED-TM-LIFT	REQUIRES	the checkpoint no-go targets exactly the registered L1 lift, with no larger phase or physical scope
CARRY-J-CHECKPOINT	DEF-AUTONOMOUS-STATE	REQUIRES	any checkpoint-only factorization must be stated on a separately frozen forward carrier of the declared autonomous update U
CARRY-PENTAD	J-UNIT	REQUIRES	the integral cyclotomic bridge uses the public unit J = 1 + zeta_5^2
CARRY-PENTAD	J-STEP	REQUIRES	the root-lattice operator I+C^2 is identified with the public integral multiplication matrix M_J
CARRY-PENTAD	CODEC-TR4	REQUIRES	the public M_J matrix and its ramified characteristic shadow are used at their registered exact scope
METAL-TRACE-CASCADE	DEGREES-BY-PRIME	REQUIRES	the two metallic laws use the registered exact sqrt5 and sqrt2 place facts
METAL-TRACE-CASCADE	Z2-PLACES-SPLIT	REQUIRES	the discriminants 5 and 8 are placed in the two registered disjoint cyclotomic fields
METAL-TRACE-CASCADE	J-UNIT	REQUIRES	the golden pure form uses the registered exact norm N(J) = 1
METAL-TRACE-CASCADE	J-MODULUS-CHORD	REQUIRES	the golden recurrence uses the registered exact phi arithmetic
POL-READ	TT-SQUARING-DECODER	REQUIRES	the plus/cross components, conjugation parity, and doubled-angle covariance are exact polynomial consequences of the registered complex square; no independent propagation law is introduced
POL-READ	TT-SOURCE	BOUNDED_BY	the component readout does not construct the still-open emission map
POL-READ	TT-VECTOR-STATE-NORMALIZATION	BOUNDED_BY	the component readout does not select a state normalization or produce a numerical r_T(k)
SQRT-PHI-DIGIT-LIFT	PENTIT-ROOT-FACTS	REQUIRES	the registered F_25 block J = 2, phi = 3, tau^3 = sqrt(phi), and tau of order eight supplies the inherited field input; root uniqueness, the restricted norm, and nonsplitting are proved by this claim
SQRT-PHI-DIGIT-LIFT	QUBIT-FROM-F5	REQUIRES	the sign quotient supplies the final C4 to C2 projection
SQRT-PHI-DIGIT-LIFT	RAMIFIED-TM-LIFT	REQUIRES	the binary digit recursion and chronological carry law are lifted through the two square-root branches without adding a physical reading
SQRT-PHI-TIME-GRAVITY	SQRT-PHI-DIGIT-LIFT	REQUIRES	the exact L1 digit lift is a necessary algebraic input, while the typed clock and gravity bridge remains open
TM-SYM2-MEASURE	GOLDEN-SIX-LINE-SYM2-FRAME	REQUIRES	the exact golden frame supplies only the candidate coefficient ratio; Thue-Morse selection, Born halving, and a physical measure remain open
QUADRATIC-DECODER-DATA	DEF-DECODER-MATTER	REQUIRES	the open action and its frozen fields are the write performed by the declared D_matter interface
QUADRATIC-DECODER-DATA	READING-SPLIT	REQUIRES	the row concerns only the registered quadratic/Born decoder leg and explicitly excludes the linear CODEC-TR4 and binary Thue-Morse/census legs
QUADRATIC-DECODER-DATA	COUPLINGS-DETERMINE	REQUIRES	the exact Gram-normalized density and Born identity are inherited inputs, not an instrument-selection theorem
QUADRATIC-DECODER-DATA	MEASURE-BORN-VERB	REQUIRES	the physical data effect uses the registered Born-square measure dictionary
OBSERVER-WRITE-PORT	QUADRATIC-DECODER-DATA	REQUIRES	completed output terminality requires the typed D_matter data action and complete dependency graph
OBSERVER-WRITE-PORT	DEF-DECODER-CLOCK	REQUIRES	positive closure concerns terminality of the declared final decoder stage
OBSERVER-WRITE-PORT	METRO-ADMISSIBILITY	REQUIRES	every admissible output cannot be quantified until the admissible protocol class is public
SQRT-PHI-TIME-GRAVITY	DEF-DECODER-CLOCK	REQUIRES	the clock leg targets the declared D_clock and ObservableHistory interface
SQRT-PHI-TIME-GRAVITY	METRO-TICK	REQUIRES	the registered dimensionless tick is an inherited clock input, not the missing bridge
SQRT-PHI-TIME-GRAVITY	GRAVITY-BRIDGE-LAW	REQUIRES	the existing equation-layer gravity dictionary is an input but supplies no Y-to-source map
SQRT-PHI-TIME-GRAVITY	METRO-EDGE-SCALE	BOUNDED_BY	any SI time or gravity scale remains outside scope until the selector and SI clause close
TM-SYM2-MEASURE	DEF-AUTONOMOUS-STATE	REQUIRES	the selector must read the declared omega and U dynamics rather than the checkpoint alone
TM-SYM2-MEASURE	MEASURE-BORN-VERB	REQUIRES	the physical measure clause rests on the Born-square dictionary, which does not itself derive the halving
FIRED-COMMUTATOR-NOGO	DEF-ARCHITECTURE	REQUIRES	the L1 fired-algebra theorem is conditional on the declared checkpoint architecture
FIRED-COMMUTATOR-NOGO	DEF-KERNEL-GENERATORS	REQUIRES	the commutators use the five declared public census involutions
FIRED-COMMUTATOR-NOGO	DEF-SELECTOR	REQUIRES	the declared sheet selector determines that only b, d, and e fire
TIME-CUT-READING	DEF-ARCHITECTURE	REQUIRES	the dictionary composition is conditional on the declared public architecture
TIME-CUT-READING	RAMIFIED-TM-LIFT	REQUIRES	the four-phase J-channel and its sign quotient realize the binary cut
TIME-CUT-READING	GYRON-DENSITY	REQUIRES	the matter-channel pair 00 has the registered exact density 1/6
TIME-CUT-READING	FIRED-COMMUTATOR-NOGO	REQUIRES	the spatial channel uses the exact fired-algebra no-go before reading the silent pair
TIME-CUT-READING	CURVATURE-HISTORICAL-TRACE	REQUIRES	the silent-pair commutator has the registered exact historical trace reading
TIME-CUT-READING	KERNEL-MACRO-READING	REQUIRES	the spatial dictionary inherits the registered macro-space commutator reading
TIME-CUT-READING	CURVATURE-OPERATOR-CANONICAL	BOUNDED_BY	the canonical curvature operator remains explicitly open and is not selected by this composition
TIME-CUT-READING	METRO-TICK	REQUIRES	the terminal dimensionless proper-time reading is the registered exact tick
TM-SYM2-MEASURE	DEF-ACTION-LAYERS	REQUIRES	the lane's layer endpoints and both lane gates use the registered six-layer protocol
TM-SYM2-MEASURE	RAMIFIED-TM-LIFT	REQUIRES	the window carrier reads the registered drive cut and its sign-quotient realization theta_n = s_2(n) mod 2
TM-SYM2-MEASURE	SUBSTRATE-KNIT	REQUIRES	the coefficient-side Born carrier rests on the registered position/Fourier overlap and Plancherel mass statement
TM-SYM2-MEASURE	ABELIAN-FACE-DICTIONARY	REQUIRES	literal Fourier inversion of the phaseful verb Psi(k) = 1 + zeta_5^k is conditional on the dictionary's explicitly supplied magnetic axiom pair, for which no uniqueness or selection theorem is claimed
'''

PINNED_INPUTS = (
    (
        "checker",
        CHECKER_SOURCE,
        69159,
        "f0499d1cd42ae199edff048277841bcea3074e28c9b73c8c12895b731d35100c",
    ),
    (
        "NORMATIVE.tsv",
        NORMATIVE_SOURCE,
        22453,
        "78bd84df4be6ba777c2d721d722b335b29b5f13644aae891814d51c6e080ad54",
    ),
    (
        "DEPENDENCIES.tsv",
        DEPENDENCIES_SOURCE,
        39547,
        "eb3b993015fa4e1a97a5fe9b78fa39e91391c5ffaf88f6a357458c03c6c137d1",
    ),
)

STEP6_ROUTE = (
    b"ROUTE: the Born/layer block is satisfied at evaluation grade (step 6); "
    b"parent closure remains gated on the owner definition surface"
)


def emit_stop(reason: str) -> int:
    sys.stdout.buffer.write(
        ("ROUTE: STOP (WRAPPER: " + reason + ")\n").encode("ascii")
    )
    sys.stdout.buffer.flush()
    return 2


def payload_is_exact(name: str, payload: bytes, size: int, digest: str) -> bool:
    if len(payload) != size or hashlib.sha256(payload).hexdigest() != digest:
        return False
    if not payload or payload.endswith(b"\n") is False:
        return False
    if b"\r" in payload or b"\x00" in payload:
        return False
    try:
        payload.decode("ascii")
    except UnicodeDecodeError:
        return False
    return True


def completed_route_is_well_formed(payload: bytes, return_code: int) -> bool:
    if not payload or not payload.endswith(b"\n") or b"\r" in payload:
        return False
    try:
        lines = payload.decode("ascii").splitlines()
    except UnicodeDecodeError:
        return False
    routes = [line.encode("ascii") for line in lines if line.startswith("ROUTE: ")]
    if len(routes) != 1:
        return False
    route = routes[0]
    known = (
        route.startswith(b"ROUTE: STOP (")
        or route.startswith(b"ROUTE: NEGATIVE (")
        or route == STEP6_ROUTE
    )
    if not known:
        return False
    final_pass = (
        lines[-1] == "RESULT: PASS (all certificates green in mode --evaluate)"
    )
    final_fail = lines[-1].startswith("RESULT: FAIL (")
    final_stop = (
        route.startswith(b"ROUTE: STOP (") and lines[-1].encode("ascii") == route
    )
    if return_code == 0:
        return final_pass
    return route.startswith(b"ROUTE: STOP (") and (final_fail or final_stop)


def main() -> int:
    if len(sys.argv) != 1:
        return emit_stop("ARGV-INTEGRITY")
    if any(os.environ.get(key) != value for key, value in EXPECTED_ENV.items()):
        return emit_stop("ENV-INTEGRITY")
    for name, payload, size, digest in PINNED_INPUTS:
        if not payload_is_exact(name, payload, size, digest):
            return emit_stop("INPUT-INTEGRITY " + name)

    original_argv = sys.argv[:]
    original_cwd = Path.cwd()
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    stdout_bytes = io.BytesIO()
    stderr_bytes = io.BytesIO()
    captured_stdout = io.TextIOWrapper(
        stdout_bytes, encoding="utf-8", newline="\n", write_through=True
    )
    captured_stderr = io.TextIOWrapper(
        stderr_bytes, encoding="utf-8", newline="\n", write_through=True
    )
    return_code = None
    execution_failed = False

    try:
        with tempfile.TemporaryDirectory(prefix="tm-sym2-measure-") as temporary:
            temp_root = Path(temporary)
            canon = temp_root / "canon"
            canon.mkdir()
            (canon / "NORMATIVE.tsv").write_bytes(NORMATIVE_SOURCE)
            (canon / "DEPENDENCIES.tsv").write_bytes(DEPENDENCIES_SOURCE)
            namespace = {
                "__name__": "_pinned_tm_sym2_checker",
                "__file__": "<pinned-tm-sym2-checker>",
            }
            code = compile(
                CHECKER_SOURCE,
                "<pinned-tm-sym2-checker>",
                "exec",
                dont_inherit=True,
            )
            exec(code, namespace)
            checker_main = namespace.get("main")
            if not callable(checker_main):
                return emit_stop("CHECKER-MAIN-INTEGRITY")
            sys.argv = ["<pinned-tm-sym2-checker>", "--evaluate"]
            os.chdir(temp_root)
            sys.stdout = captured_stdout
            sys.stderr = captured_stderr
            return_code = checker_main()
            captured_stdout.flush()
            captured_stderr.flush()
    except Exception:
        execution_failed = True
    finally:
        sys.argv = original_argv
        os.chdir(original_cwd)
        sys.stdout = original_stdout
        sys.stderr = original_stderr

    if execution_failed:
        return emit_stop("EXECUTION-INTEGRITY")
    payload = stdout_bytes.getvalue()
    error_payload = stderr_bytes.getvalue()
    if error_payload:
        original_stderr.buffer.write(error_payload)
        original_stderr.buffer.flush()
        return emit_stop("STDERR-INTEGRITY")
    if not isinstance(return_code, int):
        return emit_stop("RETURN-INTEGRITY")
    if not completed_route_is_well_formed(payload, return_code):
        return emit_stop("ROUTE-INTEGRITY")

    original_stdout.buffer.write(payload)
    original_stdout.buffer.flush()
    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
