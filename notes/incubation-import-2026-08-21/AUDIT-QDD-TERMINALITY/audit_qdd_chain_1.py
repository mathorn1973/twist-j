#!/usr/bin/env python3
"""audit_qdd_chain_1.py

Correction leg for AUDIT-QDD-CENTRALIZER-TERMINALITY, per
PREREG-AUDIT-QDD-TERMINALITY-1-CORRECTION.md, frozen with this file.

Two blocks:
  CH1..CH8  chain of custody of the audited sealed probe, from git history
            rather than file hashes alone;
  PR1..PR5  the finitely many exact matrix inputs of the written proofs the
            owner review supplies (sharp coordinates, effect coordinates,
            projective idempotence, quotient congruence, the R - C witness).

Exact integer and Fraction arithmetic; no float is formed. Gates are
collected in fixed order and never fail fast. Stdout carries no time, path,
host, or other variable datum.

Return codes: 0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP, 2 AUDIT-DISAGREEMENT.
"""

from fractions import Fraction as F
import subprocess
import sys

REPO = "/home/claude/twist-j"
PROBE = "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1"
PIN = "e1cf7394279d07318571f99d1c81762919a761f9"
RESULT_COMMIT = "936a396d57a659e45c8e5c3923aaa19896306662"
PR_HEAD = "aef78f6815fc874eb2d759b025789d16b95cb6fe"
MERGE = "4ed6cb72ab1110b68ed0574115e9dacbaf65e954"
PINNED = ("PREREG.md", "verify.py", "exact_matrix.py")
RESULT_FILES = ("EXPECTED.txt", "RUN.md", "RESULT.md")

CHAIN = []
MATH = []
STOP = []


def chain(label, cond):
    CHAIN.append((label, bool(cond)))


def math(label, cond):
    MATH.append((label, bool(cond)))


def git(*args):
    try:
        p = subprocess.run(("git",) + args, cwd=REPO, capture_output=True,
                           timeout=120)
    except subprocess.TimeoutExpired:
        STOP.append("git subprocess exceeded the frozen 120 second limit")
        return None
    if p.returncode != 0:
        return None
    return p.stdout.decode().strip()


def blob(commit, path):
    return git("rev-parse", "%s:%s" % (commit, path))


# ---------------------------------------------------------------------------
# CH1..CH8 chain of custody
# ---------------------------------------------------------------------------

ancestor_ok = True
for child in (RESULT_COMMIT, PR_HEAD, MERGE):
    p = subprocess.run(("git", "merge-base", "--is-ancestor", PIN, child),
                       cwd=REPO, capture_output=True, timeout=120)
    ancestor_ok = ancestor_ok and p.returncode == 0
chain("CH1 pin commit is an ancestor of result commit, final PR head and merge",
      ancestor_ok)

blobs_ok = True
for name in PINNED:
    ids = [blob(c, "%s/%s" % (PROBE, name)) for c in (PIN, RESULT_COMMIT, PR_HEAD, MERGE)]
    blobs_ok = blobs_ok and all(i is not None for i in ids) and len(set(ids)) == 1
chain("CH2 the three pinned blobs are byte-identical at all four commits", blobs_ok)

absent_ok = all(blob(PIN, "%s/%s" % (PROBE, name)) is None for name in RESULT_FILES)
chain("CH3 EXPECTED.txt, RUN.md and RESULT.md do not exist at the pin", absent_ok)

after_ok = True
for name in PINNED:
    changed = git("log", "--format=%H", "%s..%s" % (PIN, MERGE), "--",
                  "%s/%s" % (PROBE, name))
    after_ok = after_ok and (changed == "" or changed is None and False)
chain("CH4 no pinned file changes in any commit after the pin up to the merge",
      after_ok)

main_ok = True
for name in PINNED + RESULT_FILES:
    a = blob(MERGE, "%s/%s" % (PROBE, name))
    b = blob("origin/main", "%s/%s" % (PROBE, name))
    main_ok = main_ok and a is not None and a == b
chain("CH5 current-main copies of all six sealed files equal the merge copies",
      main_ok)

status = git("status", "--porcelain")
chain("CH6 the audit checkout worktree is clean", status == "")

head = git("rev-parse", "HEAD")
chain("CH7 the audit checkout HEAD is exactly the audited merge commit", head == MERGE)

canon_same = blob(MERGE, "canon/CANON.md") == blob("origin/main", "canon/CANON.md")
row_merge = git("show", "%s:canon/REGISTRY.tsv" % MERGE)
row_main = git("show", "origin/main:canon/REGISTRY.tsv")


def row_of(text, claim):
    if text is None:
        return None
    for line in text.split("\n"):
        if line.startswith(claim + "\t"):
            return line
    return None


qdd_row_same = (row_of(row_merge, "QDD-INSTRUMENT-APPARATUS")
                == row_of(row_main, "QDD-INSTRUMENT-APPARATUS")
                and row_of(row_main, "QDD-INSTRUMENT-APPARATUS") is not None)
chain("CH8 basis pair: canon/CANON.md DIFFERS between the audited merge and "
      "current main, and the QDD-INSTRUMENT-APPARATUS row is unchanged",
      (not canon_same) and qdd_row_same)

# ---------------------------------------------------------------------------
# rebuild the frozen class (same construction as the first leg, independent
# of it: this file imports nothing from it)
# ---------------------------------------------------------------------------

def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4))
                 for i in range(4))


def madd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(4)) for i in range(4))


def msub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(4)) for i in range(4))


def mscal(c, A):
    c = F(c)
    return tuple(tuple(c * A[i][j] for j in range(4)) for i in range(4))


def mT(A):
    return tuple(tuple(A[j][i] for j in range(4)) for i in range(4))


def mpow(A, e):
    R = I4
    B = A
    while e:
        if e & 1:
            R = mmul(R, B)
        B = mmul(B, B)
        e >>= 1
    return R


def mv(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(4)) for i in range(4))


def vadd(a, b):
    return tuple(a[i] + b[i] for i in range(4))


def vsub(a, b):
    return tuple(a[i] - b[i] for i in range(4))


def minv(A):
    n = 4
    M = [list(A[i]) + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][j] - f * M[col][j] for j in range(2 * n)]
    return tuple(tuple(M[i][n:]) for i in range(n))


I4 = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
Z4 = mat([[0] * 4] * 4)
E11 = mat([[1] * 4] * 4)
M_J = mat([[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]])
D = msub(M_J, I4)
G = msub(I4, mscal(F(1, 5), E11))
GINV = madd(I4, E11)


def sharp(A):
    return mmul(GINV, mmul(mT(A), G))


u = [(F(1), F(0), F(0), F(0))]
for _ in range(4):
    u.append(mv(D, u[-1]))
B_ = tuple(tuple(u[j][i] for j in range(4)) for i in range(4))
BINV = minv(B_)


def u_of(t):
    t %= 5
    if t <= 3:
        return u[t]
    return tuple(-(u[0][i] + u[1][i] + u[2][i] + u[3][i]) for i in range(4))


def rho(c, b):
    img = tuple(tuple(u_of(b + c * x)[i] for x in range(4)) for i in range(4))
    return mmul(img, BINV)


RHO = {(c, b): rho(c, b) for c in range(1, 5) for b in range(5)}
P = {}
Q = {}
g = {}
R = {}
C = {}
Jm = {}
for k in range(5):
    acc = Z4
    for a in range(1, 5):
        acc = madd(acc, RHO[(a, (k * (1 - a)) % 5)])
    P[k] = mscal(F(1, 4), acc)
    Q[k] = msub(I4, P[k])
    g[k] = RHO[(2, (-k) % 5)]
    R[k] = mscal(F(1, 4), madd(msub(I4, g[k]), msub(mpow(g[k], 2), mpow(g[k], 3))))
    C[k] = msub(Q[k], R[k])
    Jm[k] = mmul(g[k], C[k])

# ---------------------------------------------------------------------------
# PR1..PR5 exact inputs of the written proofs
# ---------------------------------------------------------------------------

math("PR1 R and C are self-sharp and J^sharp = -J at every token, so by "
     "linearity T(e,r,s)^sharp = e R + r C - s J for all rational e, r, s",
     all(sharp(R[k]) == R[k] and sharp(C[k]) == C[k]
         and sharp(Jm[k]) == mscal(-1, Jm[k]) for k in range(5)))

table_ok = True
for k in range(5):
    table_ok = table_ok and mmul(R[k], R[k]) == R[k] and mmul(C[k], C[k]) == C[k]
    table_ok = table_ok and mmul(R[k], C[k]) == Z4 and mmul(C[k], R[k]) == Z4
    table_ok = table_ok and mmul(Jm[k], Jm[k]) == mscal(-1, C[k])
    table_ok = table_ok and mmul(R[k], Jm[k]) == Z4 and mmul(Jm[k], R[k]) == Z4
    table_ok = table_ok and mmul(C[k], Jm[k]) == Jm[k] and mmul(Jm[k], C[k]) == Jm[k]
    table_ok = table_ok and madd(R[k], C[k]) == Q[k]
math("PR2 the multiplication table gives T^sharp T = e^2 R + (r^2+s^2) C by "
     "linearity, so the effect equation is exactly e^2 = 1 and r^2+s^2 = 1",
     table_ok)


def T_of(k, e, r, s):
    return madd(mscal(e, R[k]), madd(mscal(r, C[k]), mscal(s, Jm[k])))


# PR3: the universal step needs Q_k T = T for every class member and the
# effect equation; both are certified here on the coordinate generators,
# from which linearity gives the general member.
absorb_ok = all(mmul(Q[k], X) == X for k in range(5) for X in (R[k], C[k], Jm[k]))
sample = [(1, F(1), F(0)), (1, F(3, 5), F(4, 5)), (-1, F(-3, 5), F(4, 5)),
          (1, F(-1), F(0)), (-1, F(1), F(0)), (1, F(0), F(1))]
step_ok = True
for k in range(5):
    for (e, r, s) in sample:
        T = T_of(k, e, r, s)
        if mmul(sharp(T), T) != Q[k]:
            continue
        for eps in (1, -1):
            if mmul(T, T) == mscal(eps, T):
                step_ok = step_ok and T == mscal(eps, Q[k])
        # the proof's own algebra, checked as an identity on this member
        step_ok = step_ok and mmul(sharp(T), mmul(T, T)) == mmul(mmul(sharp(T), T), T)
        step_ok = step_ok and mmul(Q[k], T) == T
math("PR3 projective idempotence: Q_k absorbs the generators, T^sharp T^2 = "
     "(T^sharp T) T and Q_k T = T hold, so T^2 = eps T forces T = eps Q_k",
     absorb_ok and step_ok)

cong_ok = True
for k in range(5):
    A = T_of(k, 1, F(3, 5), F(4, 5))
    Bm = T_of(k, 1, F(5, 13), F(12, 13))
    AB = mmul(A, Bm)
    cong_ok = cong_ok and mmul(mscal(-1, A), Bm) == mscal(-1, AB)
    cong_ok = cong_ok and mmul(A, mscal(-1, Bm)) == mscal(-1, AB)
    cong_ok = cong_ok and mmul(mscal(-1, A), mscal(-1, Bm)) == AB
math("PR4 T ~ -T is a congruence for composition, so the post-state quotient "
     "is a group with identity [Q_k] and its only idempotent is that identity",
     cong_ok)

wit_ok = True
for k in range(5):
    T = msub(R[k], C[k])
    wR = None
    wC = None
    for j in range(4):
        cR = tuple(R[k][i][j] for i in range(4))
        cC = tuple(C[k][i][j] for i in range(4))
        if any(cR) and wR is None:
            wR = cR
        if any(cC) and wC is None:
            wC = cC
    w = vadd(wR, wC)
    Tw = mv(T, w)
    T2w = mv(T, Tw)
    dep = all(Tw[i] * w[j] - Tw[j] * w[i] == 0 for i in range(4) for j in range(4))
    wit_ok = wit_ok and mmul(T, T) == Q[k]
    wit_ok = wit_ok and T != Q[k] and T != mscal(-1, Q[k])
    wit_ok = wit_ok and Tw == vsub(wR, wC) and T2w == w and not dep
math("PR5 R - C is an involution with (R-C)^2 = Q and R - C not +/- Q; on "
     "w = w_R + w_C it maps w to w_R - w_C and back, off the line of w",
     wit_ok)

# ---------------------------------------------------------------------------
# report, fixed order, no fail-fast
# ---------------------------------------------------------------------------

chain_failed = 0
for label, ok in CHAIN:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        chain_failed += 1

math_failed = 0
for label, ok in MATH:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        math_failed += 1

for note in STOP:
    print("STOP-NOTE " + note)

print("CHAIN %d/%d PASS" % (len(CHAIN) - chain_failed, len(CHAIN)))
print("PROOF-INPUTS %d/%d PASS" % (len(MATH) - math_failed, len(MATH)))

if chain_failed or STOP:
    print("DECISION AUDIT-INTEGRITY-STOP")
    sys.exit(1)
if math_failed:
    print("DECISION AUDIT-DISAGREEMENT")
    sys.exit(2)
print("DECISION AUDIT-PASS")
sys.exit(0)
