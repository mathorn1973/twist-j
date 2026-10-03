#!/usr/bin/env python3
# Verifier for ADDENDUM 1 of C-NATIVE-FIBRE-PENTIT-WIGNER-N: reader boundary (B7) and state change (B8).
# NON-CANONICAL candidate, action layer L1 only. Frozen with the addendum before first execution.
# Python standard library only. Exact arithmetic only: integer cyclotomic coefficient vectors,
# Fractions and exact Q(sqrt5) pairs. No float. It uses no repository file.
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <this file>
import functools
import itertools
import sys
from fractions import Fraction as Fr

P = 5
RESULTS = []


def check(cid, text, cond):
    RESULTS.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + cid + " " + text)


def info(text):
    print("     " + text)


def cyc_norm(c):
    return tuple(c[i] - c[4] for i in range(4))


def cyc_mul(a, b):
    out = [0] * P
    for i in range(P):
        if a[i]:
            for j in range(P):
                if b[j]:
                    out[(i + j) % P] += a[i] * b[j]
    return out


def cyc_conj(a):
    return [a[(-m) % P] for m in range(P)]


def cyc_real_to_q5(c):
    assert c[1] == c[4] and c[2] == c[3], "element is not real"
    return (Fr(c[0]) - Fr(c[1] + c[2], 2), Fr(c[1] - c[2], 2))


def q5_sign(x, y):
    if y == 0:
        return (x > 0) - (x < 0)
    if x == 0:
        return (y > 0) - (y < 0)
    if (x > 0) == (y > 0):
        return 1 if x > 0 else -1
    big = (x * x > 5 * y * y) - (x * x < 5 * y * y)
    return big if x > 0 else -big


def q5_key():
    return functools.cmp_to_key(lambda a, b: q5_sign(a[0][0] - b[0][0], a[0][1] - b[0][1]))


def q5_str(v):
    return "(" + str(v[0]) + ") + (" + str(v[1]) + ")*sqrt5"


def A(q, r):
    return [((2 * q - j) % P, (2 * r * (q - j)) % P) for j in range(P)]


def dense_from_mono(M):
    X = [[[0] * P for _ in range(P)] for _ in range(P)]
    for k in range(P):
        X[M[k][0]][k][M[k][1]] += 1
    return X


def dense_add(X, Y):
    return [[[X[j][k][m] + Y[j][k][m] for m in range(P)] for k in range(P)] for j in range(P)]


def dense_mul(X, Y):
    Z = [[[0] * P for _ in range(P)] for _ in range(P)]
    for j in range(P):
        for k in range(P):
            acc = [0] * P
            for l in range(P):
                if any(X[j][l]) and any(Y[l][k]):
                    pr = cyc_mul(X[j][l], Y[l][k])
                    for m in range(P):
                        acc[m] += pr[m]
            Z[j][k] = acc
    return Z


def dense_trace_prod(X, Y):
    acc = [0] * P
    for j in range(P):
        for k in range(P):
            if any(X[j][k]) and any(Y[k][j]):
                pr = cyc_mul(X[j][k], Y[k][j])
                for m in range(P):
                    acc[m] += pr[m]
    return acc


PTS = list(itertools.product(range(P), repeat=2))
DIRS = [(0, 1)] + [(1, m) for m in range(P)]
LINES = []
LDIR = []
LINE_OF = {}
for di, (dq, dr) in enumerate(DIRS):
    seen = {}
    for u in PTS:
        L = frozenset(((u[0] + t * dq) % P, (u[1] + t * dr) % P) for t in range(P))
        if L not in seen:
            seen[L] = len(LINES)
            LINES.append(L)
            LDIR.append(di)
        LINE_OF[(di, u)] = seen[L]
NL = len(LINES)
PI5 = []
for L in LINES:
    X = [[[0] * P for _ in range(P)] for _ in range(P)]
    for u in sorted(L):
        X = dense_add(X, dense_from_mono(A(*u)))
    PI5.append(X)
TR = [[None] * NL for _ in range(NL)]
tr_ok = True
for i in range(NL):
    for j in range(NL):
        c = cyc_norm(dense_trace_prod(PI5[i], PI5[j]))
        tr_ok &= c[1:] == (0, 0, 0)
        TR[i][j] = Fr(c[0], 25)
        tr_ok &= TR[i][j] == Fr(len(LINES[i] & LINES[j]), 5)
check("0.1", "30 lines; Tr(Pi_L Pi_M) = |L cap M|/5 recomputed from dense projectors for all 900 pairs", NL == 30 and tr_ok)

# ---------------------------------------------------------------- effects as scaled integer symmetric matrices
LOWV = [4, -1, -1, -1, -1]
LOW20 = [[LOWV[j] * LOWV[k] for k in range(P)] for j in range(P)]            # 20 * P_l
ACC5 = [[(5 if j == k else 0) - 1 for k in range(P)] for j in range(P)]      # 5 * (I - |+><+|)
HIGH20 = [[4 * ACC5[j][k] - LOW20[j][k] for k in range(P)] for j in range(P)]  # 20 * (accept - P_l)
EFFECTS = [("LOW", LOW20, 20), ("ACC", ACC5, 5), ("HIGH", HIGH20, 20)]


def response_direct(E, scale):
    out = {}
    for (q, r) in PTS:
        c = [0] * P
        for j in range(P):
            c[(2 * r * (q - j)) % P] += E[j][(2 * q - j) % P]
        x, y = cyc_real_to_q5(c)
        out[(q, r)] = (x / scale, y / scale)
    return out


def line_sums(E, scale):
    out = []
    for X in PI5:
        acc = [0] * P
        for j in range(P):
            for k in range(P):
                f = E[k][j]
                if f:
                    for m in range(P):
                        acc[m] += f * X[j][k][m]
        x, y = cyc_real_to_q5(acc)
        out.append((x / scale, y / scale))
    return out


def invert_response(sums):
    totals = []
    for di in range(len(DIRS)):
        tx = sum(sums[i][0] for i in range(NL) if LDIR[i] == di)
        ty = sum(sums[i][1] for i in range(NL) if LDIR[i] == di)
        totals.append((tx, ty))
    T = totals[0]
    xi = {}
    for u in PTS:
        sx = sum(sums[i][0] for i in range(NL) if u in LINES[i])
        sy = sum(sums[i][1] for i in range(NL) if u in LINES[i])
        xi[u] = ((sx - T[0]) / 5, (sy - T[1]) / 5)
    return xi, totals


print("PART B7  reader boundary")
XI = {}
SUMS = {}
dual_ok = True
for name, E, scale in EFFECTS:
    XI[name] = response_direct(E, scale)
    SUMS[name] = line_sums(E, scale)
    inv, totals = invert_response(SUMS[name])
    trace = Fr(sum(E[j][j] for j in range(P)), scale)
    dual_ok &= inv == XI[name] and all(t == (5 * trace, Fr(0)) for t in totals)
check("B7.1", "dual inversion: the response xi_E(u) = Tr(E A_u) is recovered from the 30 line sums, for LOW, acceptance and HIGH", dual_ok)


def multiset(d):
    m = {}
    for v in d:
        m[v] = m.get(v, 0) + 1
    return m


low_ms = multiset(XI["LOW"].values())
info("LOW response values: " + "; ".join(q5_str(v) + " x" + str(n) for v, n in sorted(low_ms.items(), key=q5_key())))
check("B7.2", "LOW response is 1 x1, 3/4 x4, -1/4 x4, (1+sqrt5)/8 x8, (1-sqrt5)/8 x8: twelve values below 0, so LOW is no point reader",
      low_ms == {(Fr(1), Fr(0)): 1, (Fr(3, 4), Fr(0)): 4, (Fr(-1, 4), Fr(0)): 4,
                 (Fr(1, 8), Fr(1, 8)): 8, (Fr(1, 8), Fr(-1, 8)): 8}
      and sum(n for v, n in low_ms.items() if q5_sign(*v) < 0) == 12)
amp = [0] * P
for k in range(P):
    amp[k] += LOWV[k]                       # <LOW, f> * sqrt(100) with f_k = zeta^k
mod2 = cyc_norm(cyc_mul(amp, cyc_conj(amp)))
four_line = [i for i in range(NL)
             if all(cyc_norm(PI5[i][j][k]) == cyc_norm([1 if m == (j - k) % P else 0 for m in range(P)])
                    for j in range(P) for k in range(P))]
p_low = [(s[0] / 5, s[1] / 5) for s in SUMS["LOW"]]
check("B7.3", "control: the Fourier vector f is the line state of one line of direction (1,0), and |<l,f>|^2 = 1/4 by direct product and by line sum",
      mod2 == (25, 0, 0, 0) and len(four_line) == 1 and DIRS[LDIR[four_line[0]]] == (1, 0)
      and p_low[four_line[0]] == (Fr(1, 4), Fr(0)))
fifths = [i for i in range(NL) if p_low[i][1] == 0 and (5 * p_low[i][0]).denominator == 1]
pl_ms = multiset(p_low)
info("LOW probability on the 30 line states: " + "; ".join(q5_str(v) + " x" + str(n) for v, n in sorted(pl_ms.items(), key=q5_key())))
info("line states with LOW probability a multiple of 1/5: " + str(len(fifths)) + ", values " + ",".join(str(p_low[i][0]) for i in fifths))
vert = [i for i in range(NL) if DIRS[LDIR[i]] == (0, 1)]
horz = [i for i in range(NL) if DIRS[LDIR[i]] == (1, 0)]
check("B7.4", "LOW probability is 4/5 and 1/20 x4 on the basis states, 0 and 1/4 x4 on the Fourier states; exactly 2 of 30 values are multiples of 1/5",
      sorted(p_low[i] for i in vert) == sorted([(Fr(4, 5), Fr(0))] + [(Fr(1, 20), Fr(0))] * 4)
      and sorted(p_low[i] for i in horz) == sorted([(Fr(0), Fr(0))] + [(Fr(1, 4), Fr(0))] * 4)
      and len(fifths) == 2)
check("B7.5", "the acceptance effect I - |+><+| is a deterministic point reader: response 1 off the line r=0 and 0 on it",
      all(XI["ACC"][(q, r)] == ((Fr(1), Fr(0)) if r else (Fr(0), Fr(0))) for (q, r) in PTS))
high_ms = multiset(XI["HIGH"].values())
info("HIGH response values: " + "; ".join(q5_str(v) + " x" + str(n) for v, n in sorted(high_ms.items(), key=q5_key())))
check("B7.6", "HIGH response has values outside [0,1], so HIGH is no point reader either",
      any(q5_sign(*v) < 0 or q5_sign(v[0] - 1, v[1]) > 0 for v in high_ms))

print("PART B8  state change")
upd_ok = True
for i in range(NL):
    for j in range(NL):
        Y = dense_mul(dense_mul(PI5[j], PI5[i]), PI5[j])
        f = int(25 * TR[i][j])
        upd_ok &= all(cyc_norm(Y[a][b]) == cyc_norm([f * t for t in PI5[j][a][b]]) for a in range(P) for b in range(P))
check("B8.1", "Pi_M Pi_L Pi_M = (|L cap M|/5) Pi_M for all 900 pairs: the post-reading state is the line state of the outcome", upd_ok)


def shift(u, di, t):
    return ((u[0] + t * DIRS[di][0]) % P, (u[1] + t * DIRS[di][1]) % P)


two_ok = True
post_ok = True
scen = 0
for i in range(NL):
    for d1 in range(6):
        for d2 in range(6):
            scen += 1
            cnt = {}
            end = {}
            for u in sorted(LINES[i]):
                for t1 in range(P):
                    m1 = LINE_OF[(d1, u)]
                    u1 = shift(u, d1, t1)
                    for t2 in range(P):
                        m2 = LINE_OF[(d2, u1)]
                        u2 = shift(u1, d2, t2)
                        cnt[(m1, m2)] = cnt.get((m1, m2), 0) + 1
                        end.setdefault((m1, m2), {})
                        end[(m1, m2)][u2] = end[(m1, m2)].get(u2, 0) + 1
            for m1 in range(NL):
                if LDIR[m1] != d1:
                    continue
                for m2 in range(NL):
                    if LDIR[m2] != d2:
                        continue
                    two_ok &= Fr(cnt.get((m1, m2), 0), 125) == TR[i][m1] * TR[m1][m2]
            for key, dist in end.items():
                post_ok &= set(dist) == set(LINES[key[1]]) and len(set(dist.values())) == 1
info("two-round scenarios (line, direction, direction): " + str(scen))
check("B8.2", "update U1: counting 125 microstates (u,t1,t2) returns the two-round law Tr(Pi_L Pi_M1) Tr(Pi_M1 Pi_M2) in all 1080 scenarios",
      scen == 1080 and two_ok)
check("B8.3", "update U1: given any two-round history the final point is uniform on the last outcome line", post_ok)
single = all(len(LINES[i] & LINES[m]) == 1 for i in range(NL) for m in range(NL) if LDIR[i] != LDIR[m])
check("B8.4", "necessity: a line transversal to the reading meets each outcome line in exactly one point, while the post-reading law needs all five points", single)
u0_bad = 0
u1_good = 0
n3 = 0
for i in range(NL):
    for d1 in range(6):
        for d2 in range(6):
            if d1 == d2:
                continue
            n3 += 1
            quantum = sum(TR[i][m1] * TR[m1][m2] * TR[m2][m1]
                          for m1 in range(NL) if LDIR[m1] == d1 for m2 in range(NL) if LDIR[m2] == d2)
            back0 = 0
            for u in LINES[i]:
                u2 = u                      # U0: both readings leave the point where it is
                back0 += LINE_OF[(d1, u2)] == LINE_OF[(d1, u)]
            back0 = Fr(back0, 5)
            back1 = 0
            for u in LINES[i]:
                for t1 in range(P):
                    for t2 in range(P):
                        u2 = shift(shift(u, d1, t1), d2, t2)
                        back1 += LINE_OF[(d1, u2)] == LINE_OF[(d1, u)]
            u0_bad += (quantum == Fr(1, 5) and back0 == 1)
            u1_good += Fr(back1, 125) == quantum
info("three-round scenarios with two different directions: " + str(n3))
check("B8.5", "control: the non-disturbing update U0 returns the first outcome with count 1 where the quantum law gives 1/5, in all 900 scenarios; U1 gives 1/5",
      n3 == 900 and u0_bad == 900 and u1_good == 900)

print("PART C  applicability")
info("no computation: STOP_APPLICABILITY / H_NOT_TESTED unchanged; U1 consumes one fresh uniformly counted pentit per reading, a supplied resource")
print("SUMMARY %d of %d checks PASS" % (sum(RESULTS), len(RESULTS)))
sys.exit(0 if all(RESULTS) else 1)
