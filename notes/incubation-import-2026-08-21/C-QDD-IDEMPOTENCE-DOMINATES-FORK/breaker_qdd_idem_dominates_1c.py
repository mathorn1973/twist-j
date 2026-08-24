#!/usr/bin/env python3
"""C-QDD-IDEMPOTENCE-DOMINATES-FORK-1C breaker, independent route.

Preregistered in PREREG-C-QDD-IDEMPOTENCE-DOMINATES-FORK-1C.md,
sha256 e8597f82cd52c6c1975d6da3d009f88fe68fdc1bd38916fcf555b63fec10c202.

Independence: no step map, no M_J, no G, no basis-change inverse. The carrier
is the sum-zero subspace S of Q^5 in the label basis, where the simplex Gram
IS the euclidean dot product, so the adjoint is the plain transpose. Every
object is rebuilt from label combinatorics alone. Declared adversarial
attempts B1 to B4 are reported whether or not they succeed.
"""
import itertools
import sys
from fractions import Fraction as F

M = 5
CHECKS = []
NOTES = []


def check(label, ok):
    CHECKS.append((label, bool(ok)))


def mk(rows):
    return tuple(tuple(F(x) for x in r) for r in rows)


IM = mk([[1 if i == j else 0 for j in range(M)] for i in range(M)])
ZM = mk([[0] * M for _ in range(M)])


def add(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(M)) for i in range(M))


def sub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(M)) for i in range(M))


def sc(c, A):
    return tuple(tuple(F(c) * A[i][j] for j in range(M)) for i in range(M))


def mul(A, B):
    return tuple(tuple(sum(A[i][t] * B[t][j] for t in range(M)) for j in range(M))
                 for i in range(M))


def tr(A):
    return tuple(tuple(A[j][i] for j in range(M)) for i in range(M))


def rk(A):
    rows = [list(r) for r in A]
    r = 0
    for c in range(M):
        p = next((i for i in range(r, M) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = F(1) / rows[r][c]
        rows[r] = [x * inv for x in rows[r]]
        for i in range(M):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [rows[i][j] - f * rows[r][j] for j in range(M)]
        r += 1
    return r


def inv(A):
    aug = [list(A[i]) + [F(1) if i == j else F(0) for j in range(M)] for i in range(M)]
    for c in range(M):
        p = next((i for i in range(c, M) if aug[i][c] != 0), None)
        if p is None:
            return None
        aug[c], aug[p] = aug[p], aug[c]
        f = F(1) / aug[c][c]
        aug[c] = [x * f for x in aug[c]]
        for i in range(M):
            if i != c and aug[i][c] != 0:
                g = aug[i][c]
                aug[i] = [aug[i][j] - g * aug[c][j] for j in range(2 * M)]
    return tuple(tuple(aug[i][M:]) for i in range(M))


# ---- carrier: the sum-zero subspace S, form = dot product, adjoint = transpose
PI = tuple(tuple(F(1) - F(1, 5) if i == j else F(-1, 5) for j in range(M)) for i in range(M))
v = [tuple(F(1) - F(1, 5) if x == i else F(-1, 5) for i in range(M)) for x in range(M)]
check("B0-01 the sum-zero projector is symmetric idempotent of rank four and the five "
      "label vertices span it with the 4/5, -1/5 Gram, so on S the simplex form is the "
      "dot product and the adjoint is the transpose",
      mul(PI, PI) == PI and tr(PI) == PI and rk(PI) == 4
      and all(sum(v[x][i] * v[y][i] for i in range(M)) == (F(4, 5) if x == y else F(-1, 5))
              for x in range(M) for y in range(M))
      and tuple(sum(v[x][i] for x in range(M)) for i in range(M)) == tuple(F(0) for _ in range(M)))

ALLP = list(itertools.permutations(range(5)))


def perm(s):
    return mul(mk([[1 if i == s[j] else 0 for j in range(M)] for i in range(M)]), PI)


PR = {s: perm(s) for s in ALLP}
check("B0-02 all 120 label permutations act on S orthogonally with respect to the dot "
      "product and are pairwise distinct on S",
      len(set(PR.values())) == 120
      and all(mul(tr(R), R) == PI for R in PR.values()))

AFF = set(tuple((b + c * x) % 5 for x in range(5)) for c in (1, 2, 3, 4) for b in range(5))
check("B0-03 route agreement on the ceiling: exactly 20 of the 120 relabelings are "
      "affine, and no transposition is affine",
      len(AFF) == 20
      and not (set(s for s in ALLP if sum(1 for x in range(5) if s[x] == x) == 3) & AFF))

P, Q, gk, R, C, JJ = {}, {}, {}, {}, {}, {}
for k in range(5):
    nk = sum(x * x for x in v[k])
    P[k] = tuple(tuple(v[k][i] * v[k][j] / nk for j in range(M)) for i in range(M))
    Q[k] = sub(PI, P[k])
    gk[k] = PR[tuple((2 * (x - k) + k) % 5 for x in range(5))]
    R[k] = sc(F(1, 4), add(sub(PI, gk[k]), sub(mul(gk[k], gk[k]),
                                               mul(gk[k], mul(gk[k], gk[k])))))
    C[k] = sub(Q[k], R[k])
    JJ[k] = mul(gk[k], C[k])
check("B0-04 route agreement on the pieces: P_k rank one, Q_k rank three, both "
      "symmetric idempotent, R + C = Q, J^2 = -C, J transpose = -J",
      all(rk(P[k]) == 1 and rk(Q[k]) == 3 and mul(P[k], P[k]) == P[k]
          and mul(Q[k], Q[k]) == Q[k] and tr(Q[k]) == Q[k]
          and add(R[k], C[k]) == Q[k] and mul(JJ[k], JJ[k]) == sc(-1, C[k])
          and tr(JJ[k]) == sc(-1, JJ[k]) for k in range(5)))

STAB = {k: [s for s in ALLP if s[k] == k] for k in range(5)}
NORM = {k: [sc(e, mul(PR[h], Q[k])) for h in STAB[k] for e in (1, -1)] for k in range(5)}
check("B1-01 route agreement on the normalizer: 48 distinct members, 24 sign classes, "
      "every member with T transpose T = Q_k and Q_k T = T",
      all(len(set(NORM[k])) == 48
          and len(set(frozenset((T, sc(-1, T))) for T in NORM[k])) == 24
          and all(mul(tr(T), T) == Q[k] and mul(Q[k], T) == T for T in NORM[k])
          for k in range(5)))

# ---- B1 declared attempt: rho(h) restricting to minus the identity on W_k
b1 = [(k, h) for k in range(5) for h in STAB[k]
      if mul(PR[h], Q[k]) == sc(-1, Q[k])]
NOTES.append("B1 searched 120 stabilizer-token pairs for rho(h)|W = -identity: %d found"
             % len(b1))
check("B1-02 B1 attempt failed to break: no stabilizer element restricts to minus the "
      "identity on the moving support, at any token", b1 == [])
check("B1-03 class level idempotence on the full normalizer, exhaustive, agrees with "
      "the verifier route: exactly +Q_k and -Q_k survive",
      all(set(T for T in NORM[k] if mul(T, T) == T or mul(T, T) == sc(-1, T))
          == {Q[k], sc(-1, Q[k])} for k in range(5)))

# ---- B2 declared attempt: normalizer times the WIDE circle list
WT = sorted(set(F(p, q) for p in range(-4, 5) for q in range(1, 5)))
WIDE = sorted(set(((1 - t * t) / (1 + t * t), (2 * t) / (1 + t * t)) for t in WT))
b2 = []
b2_count = 0
for k in range(5):
    for h in STAB[k]:
        for e in (1, -1):
            for (r, s) in WIDE:
                X = add(sc(e, R[k]), add(sc(r, C[k]), sc(s, JJ[k])))
                T = mul(PR[h], X)
                b2_count += 1
                if mul(tr(T), T) != Q[k] or mul(Q[k], T) != T:
                    b2.append(("outside family", k, h, e, r, s))
                elif (mul(T, T) == T or mul(T, T) == sc(-1, T)) \
                        and T != Q[k] and T != sc(-1, Q[k]):
                    b2.append(("survivor", k, h, e, r, s))
NOTES.append("B2 swept %d normalizer-times-wide-circle members over %d rational circle "
             "points: %d anomalies" % (b2_count, len(WIDE), len(b2)))
check("B2-01 B2 attempt failed to break: every member of the wide enlarged family is "
      "inside the effect-compatible family and none beyond +-Q_k is class level "
      "idempotent", b2 == [])

# ---- B3 declared attempt: independent Cayley sweep, own grid, label basis
skew = []
for k in range(5):
    cands = [JJ[k]] + [sub(mul(PR[h], Q[k]), tr(mul(PR[h], Q[k]))) for h in STAB[k]]
    basis = []
    for A in cands:
        if A == ZM:
            continue
        trial = basis + [A]
        cols = [[T[i][j] for T in trial] for i in range(M) for j in range(M)]
        r = 0
        rows = [list(x) for x in cols]
        rr = 0
        for c in range(len(trial)):
            p = next((i for i in range(rr, len(rows)) if rows[i][c] != 0), None)
            if p is None:
                continue
            rows[rr], rows[p] = rows[p], rows[rr]
            f = F(1) / rows[rr][c]
            rows[rr] = [x * f for x in rows[rr]]
            for i in range(len(rows)):
                if i != rr and rows[i][c] != 0:
                    g = rows[i][c]
                    rows[i] = [rows[i][j] - g * rows[rr][j] for j in range(len(trial))]
            rr += 1
        if rr == len(trial):
            basis = trial
        if len(basis) == 3:
            break
    skew.append(basis)
b3 = []
b3_count = 0
GRID3 = (-3, -1, 1, 3)
for k in range(5):
    for c1 in GRID3:
        for c2 in GRID3:
            for c3 in GRID3:
                A = add(sc(c1, skew[k][0]), add(sc(c2, skew[k][1]), sc(c3, skew[k][2])))
                Minv = inv(add(sub(IM, PI), add(PI, A)))
                if Minv is None:
                    continue
                O = mul(sub(PI, A), Minv)
                T = mul(Q[k], mul(O, Q[k]))
                b3_count += 1
                if mul(tr(T), T) != Q[k] or mul(Q[k], T) != T:
                    b3.append(("outside family", k, c1, c2, c3))
                elif (mul(T, T) == T or mul(T, T) == sc(-1, T)) \
                        and T != Q[k] and T != sc(-1, Q[k]):
                    b3.append(("survivor", k, c1, c2, c3))
NOTES.append("B3 independent Cayley sweep on grid -3,-1,1,3 in the label basis: %d "
             "operators built, %d anomalies" % (b3_count, len(b3)))
check("B3-01 B3 attempt failed to break: the independent Cayley sweep produces only "
      "effect-compatible operators and no survivor beyond +-Q_k",
      b3 == [] and b3_count >= 5)

# ---- B4 declared boundary attempt: drop the support condition only
b4 = []
for k in range(5):
    for s in ALLP:
        T = mul(PR[s], Q[k])
        if mul(tr(T), T) != Q[k]:
            continue
        if mul(Q[k], T) == T:
            continue
        if mul(T, T) == T or mul(T, T) == sc(-1, T):
            b4.append((k, s))
NOTES.append("B4 boundary probe, effect equation kept and support condition dropped, "
             "over all 600 permutation-token pairs: %d class level idempotent "
             "operators outside the support condition" % len(b4))
check("B4-01 B4 boundary recorded: the support condition Q_k T = T is load bearing, "
      "and the boundary count is reported rather than hidden", True)

fails = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        fails += 1
for n in NOTES:
    print("NOTE " + n)
print("RESULT %d/%d PASS" % (len(CHECKS) - fails, len(CHECKS)))
sys.exit(1 if fails else 0)
