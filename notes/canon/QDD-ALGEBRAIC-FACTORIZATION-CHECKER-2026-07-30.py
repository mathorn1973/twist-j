#!/usr/bin/env python3
# QDD-ALGEBRAIC-FACTORIZATION checker (NON-CANONICAL support file).
#
# Support file for
# notes/canon/QDD-ALGEBRAIC-FACTORIZATION-BINDING-PACKAGE-2026-07-30.md.
#
# It evaluates the two sides of the factorization target independently and
# compares them field by field on the whole domain:
#
#   direct side   built only from multiplication in Q(zeta_5), the Galois map
#                 sigma_4, and Tr_(Q(zeta_5)/Q). It never calls Q_QDD, never
#                 forms a matrix pair, never uses G, and never uses the
#                 projector matrices.
#   factor side   F_QDD o Q_QDD o beta_QDD, matrices only.
#
# This file carries no authority, creates no claim, moves no status, and is
# not a probe verifier. It exists so a reader can re-derive rather than trust.
#
# Python standard library only. Exact arithmetic: int and Fraction. No float
# in any assertion or emitted field. Deterministic output. Exit 0 iff every
# witness reproduces.

import sys
from fractions import Fraction as F
from itertools import product

RESULTS = []


def check(tag, ok, detail=""):
    RESULTS.append(bool(ok))
    line = "%s %s" % (tag, "OK" if ok else "MISMATCH")
    if detail:
        line += "  " + detail
    print(line)


# ============================================================ Q(zeta_5)
# Elements are rational 4-vectors in the power basis B0 = (1, z, z^2, z^3),
# reduced by 1 + z + z^2 + z^3 + z^4 = 0.

def red(c5):
    return tuple(c5[i] - c5[4] for i in range(4))


def cmul(a, b):
    raw = [F(0)] * 8
    for i in range(4):
        for j in range(4):
            raw[i + j] += a[i] * b[j]
    out = [F(0)] * 5
    for k in range(8):
        out[k % 5] += raw[k]
    return red(out)


def cscale(a, s):
    return tuple(a[i] * s for i in range(4))


def csub(a, b):
    return tuple(a[i] - b[i] for i in range(4))


def sigma4(a):
    """The Galois automorphism sigma_4 : zeta -> zeta^4."""
    raw = [F(0)] * 5
    for i in range(4):
        raw[(4 * i) % 5] += a[i]
    return red(raw)


def trace(a):
    """Tr_(Q(zeta_5)/Q). Tr(1) = 4 and Tr(zeta^k) = -1 for k = 1..4."""
    return 4 * a[0] - a[1] - a[2] - a[3]


def pair(x, y):
    """The frozen pairing <x, y> = (1/5) Tr(x sigma_4(y))."""
    return trace(cmul(x, sigma4(y))) / 5


LAM = (F(1), F(1), F(1), F(1))     # lambda_B = 1 + z + z^2 + z^3 = -z^4
NLAM = pair(LAM, LAM)


# ================================================== the direct write, D_direct
def direct_record(w):
    """The five fields of MatterData_QDD from w alone."""
    m = pair(w, w)
    if m == 0:
        return ("ZERO", F(0), (F(0), F(0)), "ZERO_DENOMINATOR",
                "ZERO_DENOMINATOR")
    lo = cscale(LAM, pair(w, LAM) / NLAM)
    hi = csub(w, lo)
    w_lo, w_hi = pair(lo, lo), pair(hi, hi)
    cols = []
    for j in range(4):
        e = tuple(F(1) if i == j else F(0) for i in range(4))
        cols.append(cscale(w, pair(e, w) / m))
    dens = tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
    return ("NONZERO", m, (w_lo, w_hi), dens, (w_lo / m, w_hi / m))


# ============================================== the quadratic side, F o Q
I4 = tuple(tuple(F(1 if i == j else 0) for j in range(4)) for i in range(4))
G = tuple(tuple(I4[i][j] - F(1, 5) for j in range(4)) for i in range(4))
P_LOW = tuple(tuple(F(1, 4) for _ in range(4)) for _ in range(4))
P_HIGH = tuple(tuple(I4[i][j] - P_LOW[i][j] for j in range(4))
               for i in range(4))


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def tr(A):
    return sum(A[i][i] for i in range(4))


def q_pair(v):
    A = tuple(tuple(v[i] * v[j] for j in range(4)) for i in range(4))
    return (A, A)


def factor_record(qp):
    A = qp[0]
    m = tr(mm(A, G))
    if m == 0:
        return ("ZERO", F(0), (F(0), F(0)), "ZERO_DENOMINATOR",
                "ZERO_DENOMINATOR")
    w_lo = tr(mm(mm(P_LOW, A), G))
    w_hi = tr(mm(mm(P_HIGH, A), G))
    dens = tuple(tuple(x / m for x in row) for row in mm(A, G))
    return ("NONZERO", m, (w_lo, w_hi), dens, (w_lo / m, w_hi / m))


# ==================================================================== domain
ELL = {0: 0, 1: 1, 2: 2, 3: -2, 4: -1}
X = list(product(range(5), repeat=6))


def beta(x):
    """The four piston coordinates only. q and r are forbidden inputs."""
    return tuple(F(ELL[c]) for c in x[:4])


print("QDD-ALGEBRAIC-FACTORIZATION checker")
print("direct side: field multiplication, sigma_4 and Tr only")
print("factor side: F_QDD o Q_QDD o beta_QDD, matrices only")
print("arithmetic: int and Fraction only; no float in this file")
print("")

# ---- L, the low line
BASIS = [tuple(F(1 if j == i else 0) for j in range(4)) for i in range(4)]
Z4 = red([F(0), F(0), F(0), F(0), F(1)])          # zeta^4, reduced into B0
check("L1 lambda_B = 1 + z + z^2 + z^3 equals -z^4",
      LAM == tuple(-c for c in Z4),
      "zeta^4 reduces to %s in B0" % (tuple(str(c) for c in Z4),))
check("L1b sigma_4 has order exactly 2",
      all(sigma4(sigma4(b)) == b for b in BASIS)
      and any(sigma4(b) != b for b in BASIS),
      "the multiplicative order of 4 modulo 5 is 2, so sigma_4 o sigma_4 = id "
      "and sigma_4 is not the identity; this is what makes the pairing "
      "symmetric")
check("L1c the pairing is symmetric, as the order-2 fact requires",
      all(pair(a, b) == pair(b, a) for a in BASIS for b in BASIS))
check("L2 lambda_B is NOT rational and NOT in the trace kernel",
      (LAM[1], LAM[2], LAM[3]) != (F(0), F(0), F(0)) and trace(LAM) != 0,
      "Tr(lambda_B) = %s, so Q.lambda_B is neither Q.1 nor ker Tr"
      % trace(LAM))
check("L3 the low line norm", NLAM == F(4, 5), "<lambda_B, lambda_B> = 4/5")

# ---- P, the pairing and its Gram
gram = tuple(tuple(pair(tuple(F(1 if k == i else 0) for k in range(4)),
                        tuple(F(1 if k == j else 0) for k in range(4)))
                   for j in range(4)) for i in range(4))
check("P1 the Gram of <x,y> in B0 is exactly G",
      gram == G, "so the 1/5 in the pairing is the whole normalisation")

# ---- D, the target
mismatch = {}
first = None
for x in X:
    v = beta(x)
    d = direct_record(v)
    f = factor_record(q_pair(v))
    if d != f:
        for k, name in enumerate(("support", "total_weight", "branch_weights",
                                  "density", "normalized")):
            if d[k] != f[k]:
                mismatch[name] = mismatch.get(name, 0) + 1
        if first is None:
            first = (x, d, f)
check("D1 D_direct equals F_QDD o Q_QDD o beta_QDD on all %d checkpoints"
      % len(X), not mismatch,
      "complete tagged record, all five fields"
      if not mismatch else str(mismatch))

# ---- C, closed forms the package displays
bad = 0
for x in X[:3125]:
    v = beta(x)
    s = sum(v)
    if pair(v, v) != sum(c * c for c in v) - s * s / 5:
        bad += 1
    lo = cscale(LAM, pair(v, LAM) / NLAM)
    if pair(lo, lo) != s * s / 20:
        bad += 1
check("C1 closed forms m = sum v_i^2 - s^2/5 and w_low = s^2/20", bad == 0)

# ---- A, allowlist
byv = {}
for x in X:
    byv.setdefault(beta(x), set()).add(direct_record(beta(x)))
check("A1 the direct side reads only the four piston coordinates",
      all(len(s) == 1 for s in byv.values()) and len(byv) == 625,
      "625 piston tuples, one record each, independent of q and r")

# ---- E, the honest disclosure: even degree makes +-w automatic
check("E1 direct_record is even, so factoring through +-w is automatic",
      all(direct_record(v) == direct_record(tuple(-c for c in v))
          for v in byv),
      "disclosed, not claimed as content of the target")

# ---- S, separation, so the target is not vacuous
recs = {direct_record(v) for v in byv}
qs = {q_pair(v) for v in byv}
check("S1 the record separates the quadratic carrier",
      len(recs) == len(qs) == 313,
      "313 distinct records for 313 distinct Q values")

print("")
npass = sum(1 for r in RESULTS if r)
print("SUMMARY %d/%d witnesses reproduce" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
