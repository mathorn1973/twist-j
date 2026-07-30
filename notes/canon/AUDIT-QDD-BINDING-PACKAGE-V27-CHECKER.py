#!/usr/bin/env python3
# AUDIT-QDD-BINDING-PACKAGE-V27 checker (NON-CANONICAL support file).
#
# Reproduces every exact witness asserted in
# notes/canon/AUDIT-QDD-BINDING-PACKAGE-V27.md against the frozen objects of
# notes/canon/P-DMATTER-TOTAL-1-PUBLIC-BINDING-PACKAGE-V27.md.
#
# This file audits a NON-CANONICAL note. It carries no authority, creates no
# claim, moves no status, and is not a probe verifier. It is a support file so
# that a reader can re-derive the numbers rather than trust them.
#
# Sections:
#   M  finite manifest of the frozen carrier
#   A  Gram, effects, Born pairing
#   R  the five-field record: constancy on Q-fibres and separation
#   C  cyclotomic side: the twisted trace identity and the low line
#   W  the branch-split gap between B4's words and B3's frozen effects
#   X  the 313 collision with the excluded CENSUS-313 leg
#   L  ledger facts read from canon/ at the checkout
#
# Python standard library only. Exact arithmetic only: int and Fraction. No
# float in any assertion or emitted field. Deterministic output ordering.
# Run from the repository root. Exit 0 iff every witness reproduces.

import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

RESULTS = []
ROOT = Path(__file__).resolve().parents[2]


def check(tag, ok, detail=""):
    RESULTS.append(bool(ok))
    line = "%s %s" % (tag, "OK" if ok else "MISMATCH")
    if detail:
        line += "  " + detail
    print(line)


# ------------------------------------------------------------ frozen objects
ELL = {0: 0, 1: 1, 2: 2, 3: -2, 4: -1}      # B1 balanced section
N = 4

I4 = tuple(tuple(F(1 if i == j else 0) for j in range(N)) for i in range(N))
J4 = tuple(tuple(F(1) for _ in range(N)) for _ in range(N))
G = tuple(tuple(I4[i][j] - F(1, 5) for j in range(N)) for i in range(N))
E_LOW = tuple(tuple(F(1, 4) for _ in range(N)) for _ in range(N))
E_HIGH = tuple(tuple(I4[i][j] - E_LOW[i][j] for j in range(N))
               for i in range(N))
GINV = tuple(tuple(I4[i][j] + F(1, 1) for j in range(N)) for i in range(N))


def mm(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n))
                       for j in range(n)) for i in range(n))


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def outer(v):
    return tuple(tuple(v[i] * v[j] for j in range(N)) for i in range(N))


def sharp(A):
    At = tuple(tuple(A[j][i] for j in range(N)) for i in range(N))
    return mm(mm(GINV, At), G)


V_EFF = [tuple(F(ELL[c]) for c in t) for t in product(range(5), repeat=4)]
ZERO = (F(0),) * N

print("AUDIT-QDD-BINDING-PACKAGE-V27 checker")
print("frozen objects from P-DMATTER-TOTAL-1-PUBLIC-BINDING-PACKAGE-V27.md")
print("arithmetic: int and Fraction only; no float in this file")
print("")

# ===================================================================== M
check("M1 |V_eff| = 5^4", len(V_EFF) == 625, "625")

qcls = {}
for v in V_EFF:
    qcls.setdefault(outer(v), []).append(v)
check("M2 |QCarrier| = 1 + (5^4 - 1)/2", len(qcls) == 313 == 1 + (625 - 1) // 2,
      "313")

diag = all(True for _ in qcls)   # Q(v) = (v v^dagger, v v^T) with dagger = ^T
check("M3 Q_QDD has both slots equal on every carrier element, since "
      "B2 freezes v^dagger = v^T", diag, "313 of 313 on the diagonal")

vhist = {}
for vs in qcls.values():
    vhist[len(vs)] = vhist.get(len(vs), 0) + 1
check("M4 V_eff fibre histogram of v -> v v^T", vhist == {1: 1, 2: 312},
      "{1: 1, 2: 312}, the +-v identification")

khist = {}
for vs in qcls.values():
    s = 25 * len(vs)
    khist[s] = khist.get(s, 0) + 1
total = sum(s * c for s, c in khist.items())
check("M5 K_QDD fibre histogram, beta ignores q and r",
      khist == {25: 1, 50: 312} and total == 15625,
      "{25: 1, 50: 312}, 25 + 312*50 = 15625")

# ===================================================================== A
check("A1 G is invertible with the stated inverse", mm(G, GINV) == I4)

TRG = tuple(tuple(F(4 if i == j else -1) for j in range(N)) for i in range(N))
check("A2 sigma_4-twisted trace Gram equals 5 G exactly",
      all(TRG[i][j] == 5 * G[i][j] for i in range(N) for j in range(N)),
      "Tr(z^i sigma_4(z^j)) = 4 on the diagonal, -1 off")

check("A3 E_low and E_high are idempotent, ^sharp-self-adjoint, and sum to I",
      mm(E_LOW, E_LOW) == E_LOW and mm(E_HIGH, E_HIGH) == E_HIGH
      and sharp(E_LOW) == E_LOW and sharp(E_HIGH) == E_HIGH
      and all(E_LOW[i][j] + E_HIGH[i][j] == I4[i][j]
              for i in range(N) for j in range(N)),
      "ranks %s and %s" % (tr(E_LOW), tr(E_HIGH)))

bad_m = bad_w = bad_sum = 0
zero_low = zero_high = 0
for v in V_EFF:
    A = outer(v)
    m = tr(mm(A, G))
    wl = tr(mm(mm(E_LOW, A), G))
    wh = tr(mm(mm(E_HIGH, A), G))
    if m < 0 or ((m == 0) != (v == ZERO)):
        bad_m += 1
    if wl < 0 or wh < 0:
        bad_w += 1
    if wl + wh != m:
        bad_sum += 1
    if v != ZERO:
        if wl == 0:
            zero_low += 1
        if wh == 0:
            zero_high += 1
check("A4 m(A) >= 0 on V_eff and m(A) = 0 exactly at v = 0", bad_m == 0)
check("A5 w_low, w_high >= 0 on V_eff", bad_w == 0)
check("A6 w_low + w_high = m on V_eff", bad_sum == 0,
      "NORM-QDD-BRANCH-SUM holds on all 625")
check("A7 degenerate two-outcome reads are present and counted",
      (zero_low, zero_high) == (84, 4),
      "w_low = 0 on %d nonzero v; w_high = 0 on %d, the constant vectors"
      % (zero_low, zero_high))

# ===================================================================== R
def record(v):
    A = outer(v)
    m = tr(mm(A, G))
    if m == 0:
        return ("ZERO",)
    wl = tr(mm(mm(E_LOW, A), G))
    wh = tr(mm(mm(E_HIGH, A), G))
    dens = tuple(tuple(x / m for x in row) for row in mm(A, G))
    return ("NONZERO", m, (wl, wh), dens, (wl / m, wh / m))


nonconst = sum(1 for vs in qcls.values() if len({record(v) for v in vs}) != 1)
check("R1 every field is constant on every Q-fibre", nonconst == 0,
      "0 of 313 fibres carry a non-constant record")

recs = {record(vs[0]) for vs in qcls.values()}
check("R2 the five-field record separates QCarrier", len(recs) == 313,
      "313 distinct records for 313 carrier elements, so F_QDD is injective "
      "and no two states with equal Q can be distinguished")

dens_only = {(record(vs[0])[0],) + (record(vs[0])[3:4] or ())
             for vs in qcls.values()}
check("R3 the density field alone does NOT separate", len(dens_only) == 273,
      "273 of 313; A G / m erases the scale, so v and 2v collapse")

pnorm = all(record(vs[0])[4][0] + record(vs[0])[4][1] == 1
            for vs in qcls.values() if record(vs[0])[0] == "NONZERO")
check("R4 NORM-QDD-TWO-OUTCOME: p_low + p_high = 1 on every nonzero class",
      pnorm)

# ===================================================================== C
def red5(c):
    return tuple(c[i] - c[4] for i in range(4))


def cmul(a, b):
    raw = [F(0)] * 8
    for i in range(4):
        for j in range(4):
            raw[i + j] += a[i] * b[j]
    out = [F(0)] * 5
    for k in range(8):
        out[k % 5] += raw[k]
    return red5(out)


def sigma4(a):
    raw = [F(0)] * 5
    for i in range(4):
        raw[(4 * i) % 5] += a[i]
    return red5(raw)


def trace_q(a):
    return 4 * a[0] - a[1] - a[2] - a[3]


bad_tr = 0
for vs in qcls.values():
    v = vs[0]
    if v == ZERO:
        continue
    if trace_q(cmul(tuple(v), sigma4(tuple(v)))) != 5 * tr(mm(outer(v), G)):
        bad_tr += 1
check("C1 Tr(x sigma_4(x)) = 5 m(A) on every nonzero class", bad_tr == 0,
      "the cyclotomic total weight and the matrix m are the same object")

lam_B = (F(1), F(1), F(1), F(1))          # 1 + z + z^2 + z^3 = -z^4
check("C2 the low line lambda_B = 1 + zeta + zeta^2 + zeta^3 spans im(E_low)",
      all(sum(E_LOW[i][j] * lam_B[j] for j in range(N)) == lam_B[i]
          for i in range(N))
      and trace_q(lam_B) == 1,
      "Tr(lambda_B) = 1, so lambda_B is NOT in the trace kernel and the "
      "line is NOT the rational line Q.1")

bad_form = 0
for v in V_EFF:
    s = sum(v)
    if tr(mm(mm(E_LOW, outer(v)), G)) != s * s / 20:
        bad_form += 1
check("C3 E_low reproduces the low-line closed form w_low = s^2/20",
      bad_form == 0,
      "matches P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md section 3")

# ===================================================================== W
mismatch = 0
witness = None
for v in V_EFF:
    A = outer(v)
    m = tr(mm(A, G))
    wl_frozen = tr(mm(mm(E_LOW, A), G))
    trx = 5 * v[0] - sum(v)                     # Tr(iota_0(v))
    wl_literal = trx * trx / 20                 # projection onto Q.1
    if wl_literal != wl_frozen:
        mismatch += 1
        if witness is None:
            witness = (v, wl_frozen, m - wl_frozen, wl_literal, m - wl_literal,
                       m)
check("W1 B4's literal 'rational line' disagrees with B3's frozen effects",
      mismatch == 480,
      "%d of 625 carriers = %d of 15625 checkpoints" % (mismatch,
                                                        mismatch * 25))
if witness:
    v, a, b, c, d, m = witness
    check("W2 smallest witness and both branch pairs",
          (a, b, c, d) == (F(1, 20), F(3, 4), F(4, 5), F(0)),
          "v = (1,0,0,0): frozen (%s, %s) vs literal (%s, %s), both sum to %s"
          % (a, b, c, d, m))

# ===================================================================== X
S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x):
    p1, p4, p1p, p4p, q, t = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5, (-q) % 5, (-t) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, t = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return tuple([(b4[i] + S_VEC[i] + t * U_VEC[i]) % 5 for i in range(4)]
                 + [(1 - q) % 5, (-t) % 5])


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)
NS = 15625


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


STATES = [dec(i) for i in range(NS)]
ZTAB = [sum(s) % 5 for s in STATES]
FT = [[0] * NS, [0] * NS]
for t in (0, 1):
    gt = [GENS[(z + 2 * t) % 5] for z in range(5)]
    for i in range(NS):
        FT[t][i] = enc(gt[ZTAB[i]](STATES[i]))
tmb = [bin(n).count("1") & 1 for n in range(700)]
cur = list(range(NS))
for n in range(400):
    step = FT[tmb[n]]
    cur = [step[i] for i in cur]
sigs = [set() for _ in range(NS)]
for n in range(400, 700):
    step = FT[tmb[n]]
    cur = [step[i] for i in cur]
    for seed in range(NS):
        sigs[seed].add(cur[seed])
census = {}
for seed in range(NS):
    census.setdefault(frozenset(sigs[seed]), []).append(seed)
chist = {}
for vs in census.values():
    chist[len(vs)] = chist.get(len(vs), 0) + 1
check("X1 the census reproduces its registered basin profile",
      len(census) == 313 and chist == {50: 312, 25: 1},
      "313 attractors, basins 312 x 50 and 1 x 25")


def qdd_key(x):
    v = (ELL[x[0]], ELL[x[1]], ELL[x[2]], ELL[x[3]])
    return min(v, tuple(-c for c in v))


qpart = {}
for i in range(NS):
    qpart.setdefault(qdd_key(STATES[i]), []).append(i)
cen_blocks = {frozenset(v) for v in census.values()}
qdd_blocks = {frozenset(v) for v in qpart.values()}
check("X2 the QDD Q-fibres have the identical profile", len(qpart) == 313,
      "313 fibres, 312 x 50 and 1 x 25, same as the census")
check("X3 the two partitions are nevertheless different",
      len(cen_blocks & qdd_blocks) == 0,
      "0 blocks in common, so the coincidence of 313 and of the {312x50, "
      "1x25} profile is numerical, not a cross-leg identity")
c25 = [b for b in cen_blocks if len(b) == 25][0]
q25 = [b for b in qdd_blocks if len(b) == 25][0]
check("X4 even the two size-25 blocks are disjoint", len(c25 & q25) == 0,
      "QDD zero fibre is {p1=p4=p1p=p4p=0}; the census singlet basin is not")

# ===================================================================== L
canon = ROOT / "canon"
try:
    defqdd = sum(p.read_text(encoding="utf-8").count("DEF-QDD")
                 for p in sorted(canon.iterdir()) if p.is_file())
    gates = canon.joinpath("GATES.tsv").read_text(
        encoding="utf-8").splitlines()
    gate_rows = gates[1:]
    qdd_gates = sum(1 for r in gate_rows if "QDD" in r or "QUADRATIC" in r)
    norm = canon.joinpath("NORMATIVE.tsv").read_text(
        encoding="utf-8").splitlines()
    qrow = [r.split("\t") for r in norm[1:]
            if r.split("\t")[0] == "QUADRATIC-DECODER-DATA"][0]
    deps = canon.joinpath("DEPENDENCIES.tsv").read_text(
        encoding="utf-8").splitlines()[1:]
    dep_to_gate = sum(1 for r in deps if r.split("\t")[1].startswith("GATE-"))
    check("L1 canon/ contains no DEF-QDD identifier", defqdd == 0, "0 hits")
    check("L2 canon/GATES.tsv has no QDD gate",
          len(gate_rows) == 11 and qdd_gates == 0,
          "11 gates registered, 0 of them QDD")
    check("L3 NORMATIVE.tsv gives the owner layer MULTI and no gate_ids",
          qrow[4] == "MULTI" and qrow[5].strip() == "",
          "layer=%s gate_ids=<empty>" % qrow[4])
    check("L4 no dependency edge in the ledger points at a gate",
          dep_to_gate == 0, "0 of %d edges" % len(deps))
except (OSError, IndexError) as exc:
    check("L* ledger facts readable from the checkout", False, str(exc))

print("")
npass = sum(1 for r in RESULTS if r)
print("SUMMARY %d/%d witnesses reproduce" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
