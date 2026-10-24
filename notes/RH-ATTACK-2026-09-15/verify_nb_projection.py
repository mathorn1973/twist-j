#!/usr/bin/env python3
"""verify_nb_projection.py -- exact projection census for the Nyman-Beurling
binary-routing route and the mean-channel debt of the Mobius mean-channel note.

NON-CANONICAL incubation verifier (lane A, 2026-09-15; repaired after referee
review on the same date).  Python 3 standard library only: int and
fractions.Fraction.  Every predicate that decides a PASS/FAIL is exact.
Floating-point renderings appear only in lines and blocks that carry the
word DIAGNOSTIC, and they assert nothing.  All values that the checks decide
on (approximant errors, distances at the cuts, mean-channel norms, lower
bounds, efficiency ratios) are printed exactly: as fractions up to 8000
digits, beyond that as digit count plus SHA-256 of the string num/den.

Objects (see ATTACK-NB-PROJECTION.md for the definitions and proofs):
  r_k(n) = n mod k (n >= 1, k >= 2);  A_Q(n) = [n = Q mod 2Q] for Q = 2^j;
  ||x||_B^2 = sum_{j>=0} 4^{-j} sum_{2^j <= n < 2^{j+1}} x(n)^2;
  t_Q = mu * Delta A_Q with Delta x(n) = x(n) - x(n-1), x(0) = 0 (backward
  difference, the convention encoded in the Mobius note's identities (4) and
  (23); check C12 confirms its consequences and records what the forward
  difference would do instead);
  K_h = 4 Q 2^h;  p_h = -sum_{k<K_h} (t_Q(k)/k) r_k + T_{Q,K_h-1} r_{K_h};
  e_h = A_Q - p_h;  S_{Q,J} = sum_{h<J} e_h;
  (Hx)(n) = x(2n+1) - x(2n);  (Lx)(n) = (x(2n) + x(2n+1))/2;
  D_{Q,J} = H S_{Q,J};  Y_{Q,J} = L S_{Q,J}.

Run:  LC_ALL=C PYTHONHASHSEED=0 python3 verify_nb_projection.py [KMAX]
Exit status 0 iff every check passes.  One line per check, PASS/FAIL, and a
final "CHECKS: k of n PASS" line.
"""
from __future__ import annotations

import hashlib
import math
import random
import sys
import time
from fractions import Fraction as Fr
from itertools import accumulate
from math import gcd

sys.set_int_max_str_digits(0)

T_START = time.time()
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 72
QLIST = (2, 4, 8)
NPT = 4096          # range of the Mobius data used for the gamma bound (3)
RESULTS: list[tuple[str, bool, str]] = []


def report(cid: str, ok: bool, msg: str) -> None:
    RESULTS.append((cid, ok, msg))
    print(f"{cid}: {'PASS' if ok else 'FAIL'} -- {msg}", flush=True)


# ---------------------------------------------------------------------------
# 1. exact binary inner product of integer-periodic sequences
# ---------------------------------------------------------------------------

def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def mult_order_2(m: int) -> int:
    """multiplicative order of 2 modulo odd m (order 1 for m = 1)."""
    if m == 1:
        return 1
    t, x = 1, 2 % m
    while x != 1:
        x = (2 * x) % m
        t += 1
    return t


def bsum(q) -> Fr:
    """sum_{j>=0} 4^{-j} sum_{2^j <= n < 2^{j+1}} q[n mod L],  L = len(q).

    Derivation (own): with prefix sums P(r) = sum_{a<r} q[a], S = P(L),
    A(M) := sum_{n<M} q_n = M S/L + eta(M mod L), eta(r) = P(r) - r S/L.
    Block j sums to 2^j S/L + eta(b_{j+1}) - eta(b_j), b_j = 2^j mod L.
    (b_j) has pre-period h = v_2(L) and period t = ord_{L/2^h}(2), so the
    weighted sum is 2S/L + sum_{j<h} 4^{-j} d_j + 4^{-h} (1-4^{-t})^{-1}
    sum_{a<t} 4^{-a} d_{h+a},  d_j = eta(b_{j+1}) - eta(b_j).
    Everything is kept integral (L*eta) until the final division."""
    L = len(q)
    P = [0]
    P.extend(accumulate(q))
    S = P[L]
    h = v2(L)
    t = mult_order_2(L >> h)
    b = [pow(2, j, L) for j in range(h + t + 1)]
    assert b[h + t] == b[h], "cycle bookkeeping"
    def etaL(r):
        return L * P[r] - r * S
    d = [etaL(b[j + 1]) - etaL(b[j]) for j in range(h + t)]
    pre = sum((Fr(d[j], 4 ** j) for j in range(h)), Fr(0))
    cyc = sum((Fr(d[h + a], 4 ** a) for a in range(t)), Fr(0))
    return Fr(2 * S, L) + (pre + Fr(4 ** t, 4 ** h * (4 ** t - 1)) * cyc) / L


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def enclosure_coarse(q, J0: int):
    """partial sum over blocks j < J0 plus the crude tail box
    [2^{1-J0} min q, 2^{1-J0} max q]  (independent of the closed form)."""
    L = len(q)
    part = Fr(0)
    for j in range(J0):
        blk = sum(q[n % L] for n in range(2 ** j, 2 ** (j + 1)))
        part += Fr(blk, 4 ** j)
    return part + Fr(2, 2 ** J0) * min(q), part + Fr(2, 2 ** J0) * max(q)


def enclosure_fine(q, J0: int):
    """partial sum over blocks j < J0 plus a window-based tail box.
    Block j is 2^j = f L + g consecutive terms: f full periods plus a window
    of g < L consecutive terms, whose sum lies in [mn[g], mx[g]] (min/max
    over all starting residues).  Then 4^{-j} B_j = 2^{-j} S/L + 4^{-j}(W_j -
    g_j S/L) and the tail lies in 2^{1-J0} S/L + (4/3) 4^{-J0} [c_lo, c_hi]
    with c_lo = min_g (mn[g] - g S/L), c_hi = max_g (mx[g] - g S/L).
    Uses only floor counting, no cycle structure."""
    L = len(q)
    S = sum(q)
    part = Fr(0)
    for j in range(J0):
        blk = sum(q[n % L] for n in range(2 ** j, 2 ** (j + 1)))
        part += Fr(blk, 4 ** j)
    qq = list(q) + list(q)
    c_lo, c_hi = None, None
    for g in range(L):
        wins = [sum(qq[s:s + g]) for s in range(L)]
        lo = min(wins) - Fr(g * S, L)
        hi = max(wins) - Fr(g * S, L)
        c_lo = lo if c_lo is None or lo < c_lo else c_lo
        c_hi = hi if c_hi is None or hi > c_hi else c_hi
    base = part + Fr(2 * S, 2 ** J0 * L)
    return base + Fr(4, 3 * 4 ** J0) * c_lo, base + Fr(4, 3 * 4 ** J0) * c_hi


rng = random.Random(20260915)
N_RANDOM = 240
periods = [1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 31, 32, 60, 64, 96, 100, 127, 128]
ok_c, ok_f, ok_inv, cases = 0, 0, 0, 0
for trial in range(N_RANDOM):
    if trial < len(periods):
        L = periods[trial]
    else:
        L = rng.randint(1, 120)
    if trial % 3 == 0:
        q = [Fr(rng.randint(-9, 9), rng.randint(1, 5)) for _ in range(L)]
    else:
        q = [rng.randint(-9, 9) for _ in range(L)]
    val = bsum(q)
    J0 = max(12, L.bit_length())
    lo, hi = enclosure_coarse(q, J0)
    if lo <= val <= hi:
        ok_c += 1
    lo2, hi2 = enclosure_fine(q, J0)
    if lo2 <= val <= hi2 and (hi2 - lo2) <= (hi - lo):
        ok_f += 1
    # invariance under period multiples and linearity
    q2 = [rng.randint(-9, 9) for _ in range(L)]
    if (bsum(q * 2) == val and bsum(q * 3) == val
            and bsum([a + 2 * c for a, c in zip(q, q2)]) == val + 2 * bsum(q2)):
        ok_inv += 1
    cases += 1
report("C01-ENCLOSURE-COARSE", ok_c == cases,
       f"closed form inside brute-force partial sum + crude tail box in {ok_c} of {cases} random periodic cases")
report("C02-ENCLOSURE-FINE", ok_f == cases,
       f"closed form inside the window-based tail box (tighter than C01) in {ok_f} of {cases} cases")
report("C03-PERIOD-INVARIANCE", ok_inv == cases,
       f"invariance under period doubling/tripling and linearity in {ok_inv} of {cases} cases")


# ---------------------------------------------------------------------------
# 2. calibration against the record (NOTE-SOURCE-CZ sec. 1, 3, 6, 7; REVIEW-CZ sec. 1, 7)
# ---------------------------------------------------------------------------

def A_seq(Q: int, L: int):
    """A_Q on residues 0..L-1 (2Q | L); A_1 := r_2 = 1_{odd}."""
    if Q == 1:
        return [n % 2 for n in range(L)]
    return [1 if n % (2 * Q) == Q else 0 for n in range(L)]


calib = []
calib.append(bsum([1]) == 2)
for j in range(0, 9):
    Q = 2 ** j
    calib.append(bsum(A_seq(Q, 2 * Q)) == Fr(3, 2 * 4 ** j))
    for i in range(j):
        Qi = 2 ** i
        L = 2 * Q
        calib.append(bsum([a * b for a, b in zip(A_seq(Q, L), A_seq(Qi, L))]) == 0)
for J in range(0, 8):
    calib.append(bsum([1 if n % 2 ** J == 0 else 0 for n in range(2 ** J)]) == Fr(2, 4 ** J))
# ||1 - f_J||^2 = 2/4^J (routing note sec. 3)
report("C04-CALIB-NORMS", all(calib),
       f"||1||_B^2 = 2, ||a_j||_B^2 = 3/(2*4^j) and layer orthogonality for j <= 8, single dyadic residue 2/4^J ({len(calib)} equalities)")


# ---------------------------------------------------------------------------
# 3. Gram tables for k, l <= KMAX  (three tables from one pass per pair)
#    G[k][l]  = <r_k, r_l>_B
#    GL[k][l] = <u_k, u_l>_B,  u_k(m) = r_k(2m) + r_k(2m+1) = 2 (L r_k)(m)
#    GH[k][l] = <v_k, v_l>_B,  v_k(m) = r_k(2m+1) - r_k(2m) = (H r_k)(m)
# ---------------------------------------------------------------------------
t0 = time.time()
G = {}
GL = {}
GH = {}
for k in range(2, KMAX + 1):
    for l in range(k, KMAX + 1):
        L = lcm(k, l)
        rk = [n % k for n in range(L)]
        rl = [n % l for n in range(L)]
        G[(k, l)] = G[(l, k)] = bsum([a * b for a, b in zip(rk, rl)])
        uk = [(2 * m) % k + (2 * m + 1) % k for m in range(L)]
        ul = [(2 * m) % l + (2 * m + 1) % l for m in range(L)]
        vk = [(2 * m + 1) % k - (2 * m) % k for m in range(L)]
        vl = [(2 * m + 1) % l - (2 * m) % l for m in range(L)]
        GL[(k, l)] = GL[(l, k)] = bsum([a * b for a, b in zip(uk, ul)])
        GH[(k, l)] = GH[(l, k)] = bsum([a * b for a, b in zip(vk, vl)])
print(f"# gram tables for k,l <= {KMAX} built in {time.time() - t0:.1f} s", file=sys.stderr, flush=True)

# target vectors
b1 = {k: bsum([n % k for n in range(k)]) for k in range(2, KMAX + 1)}
bA = {}     # bA[Q][k]  = <A_Q, r_k>
bLA = {}    # bLA[Q][k] = <A_{Q/2}, u_k>
bHA = {}    # bHA[Q][k] = <A_{Q/2}, v_k>
nA = {}     # ||A_Q||^2
nAh = {}    # ||A_{Q/2}||^2
for Q in QLIST:
    bA[Q], bLA[Q], bHA[Q] = {}, {}, {}
    nA[Q] = bsum(A_seq(Q, 2 * Q))
    nAh[Q] = bsum(A_seq(Q // 2, Q))
    for k in range(2, KMAX + 1):
        L = lcm(2 * Q, k)
        aq = A_seq(Q, L)
        bA[Q][k] = bsum([a * (n % k) for n, a in enumerate(aq)])
        L2 = lcm(Q, k)
        ah = A_seq(Q // 2, L2)
        bLA[Q][k] = bsum([a * ((2 * m) % k + (2 * m + 1) % k) for m, a in enumerate(ah)])
        bHA[Q][k] = bsum([a * ((2 * m + 1) % k - (2 * m) % k) for m, a in enumerate(ah)])

cal = [G[(2, 2)] == Fr(3, 2), G[(2, 3)] == Fr(13, 10), G[(3, 3)] == Fr(14, 5),
       b1[2] == Fr(3, 2), b1[3] == 2]
report("C05-CALIB-GRAM-ENTRIES", all(cal), "G_22 = 3/2, G_23 = 13/10, G_33 = 14/5, b_2 = 3/2, b_3 = 2 (NOTE-SOURCE-CZ sec. 7)")

# polarised split identity  <x,y> = x(1)y(1) + <Lx,Ly>/2 + <Hx,Hy>/8 on the tables
split_ok = 0
split_n = 0
for k in range(2, KMAX + 1):
    for l in range(k, KMAX + 1):
        split_n += 1
        if G[(k, l)] == 1 + GL[(k, l)] / 8 + GH[(k, l)] / 8:
            split_ok += 1
for Q in QLIST:
    split_n += 1
    if nA[Q] == nAh[Q] / 4:
        split_ok += 1
    for k in range(2, KMAX + 1):
        split_n += 1
        if bA[Q][k] == bLA[Q][k] / 8 - bHA[Q][k] / 8:
            split_ok += 1
# and on random finitely supported sequences (direct weights)
def wB(n):
    return Fr(1, 4 ** (n.bit_length() - 1))
for trial in range(60):
    x = {n: Fr(rng.randint(-5, 5), rng.randint(1, 3)) for n in rng.sample(range(1, 400), 12)}
    def xv(n):
        return x.get(n, Fr(0))
    nx = sum(wB(n) * v * v for n, v in x.items())
    mmax = 400
    nL = sum(wB(m) * ((xv(2 * m) + xv(2 * m + 1)) / 2) ** 2 for m in range(1, mmax))
    nH = sum(wB(m) * (xv(2 * m + 1) - xv(2 * m)) ** 2 for m in range(1, mmax))
    split_n += 1
    if nx == xv(1) ** 2 + nL / 2 + nH / 8:
        split_ok += 1
report("C06-SPLIT-IDENTITY", split_ok == split_n,
       f"||x||^2 = x(1)^2 + ||Lx||^2/2 + ||Hx||^2/8 (polarised) on all three Gram tables, target vectors and 60 random sequences ({split_ok} of {split_n})")


# ---------------------------------------------------------------------------
# 4. LDL^T of the Gram matrix in the order k = 2, 3, ..., KMAX; all d_K(x)^2 at once
# ---------------------------------------------------------------------------
t0 = time.time()
idx = list(range(2, KMAX + 1))
n = len(idx)
Lm = [[Fr(0)] * n for _ in range(n)]
W = [[Fr(0)] * n for _ in range(n)]   # W[i][k] = Lm[i][k] * Dv[k]
Dv = [Fr(0)] * n
for j in range(n):
    Lj = Lm[j]
    s = G[(idx[j], idx[j])] - sum((Lj[k] * W[j][k] for k in range(j)), Fr(0))
    Dv[j] = s
    Lj[j] = Fr(1)
    W[j][j] = s
    Wj = W[j]
    for i in range(j + 1, n):
        Li = Lm[i]
        val = (G[(idx[i], idx[j])] - sum((Li[k] * Wj[k] for k in range(j)), Fr(0))) / s
        Li[j] = val
        W[i][j] = val * s
print(f"# LDL^T of the {n}x{n} Gram matrix in {time.time() - t0:.1f} s", file=sys.stderr, flush=True)
report("C07-GRAM-POSITIVE-DEFINITE", all(dv > 0 for dv in Dv) and all(G[(k, l)] == G[(l, k)] for k in idx for l in idx),
       f"all {n} LDL pivots positive (Gram matrix of r_2..r_{KMAX} positive definite), symmetry")


def dist_table(norm2: Fr, bvec: dict) -> dict:
    """d_K(x)^2 = ||x||^2 - sum_{k<=K} y_k^2/D_k with L y = b, for every K."""
    y = [Fr(0)] * n
    for i in range(n):
        y[i] = bvec[idx[i]] - sum((Lm[i][k] * y[k] for k in range(i)), Fr(0))
    out = {}
    acc = norm2
    for i in range(n):
        acc -= y[i] * y[i] / Dv[i]
        out[idx[i]] = acc
    return out


targets = {"1": (Fr(2), b1)}
for Q in QLIST:
    targets[f"A{Q}"] = (nA[Q], bA[Q])
DK = {name: dist_table(nrm, bv) for name, (nrm, bv) in targets.items()}

# calibration of d_K(1)^2 against the record
REVIEW_D2 = {
    2: Fr(1, 2), 3: Fr(52, 251), 4: Fr(95, 766), 5: Fr(987196, 11709287), 6: Fr(168677, 2018075),
    7: Fr(427057462138410, 8196142861502003),
    8: Fr(99798522848850307, 1929506790431462857),
    9: Fr(60622737896864509142, 1176007057940578080117),
    10: Fr(705092006280271911060007117, 13738605773891725756927498559),
    11: Fr(686207536743458026894714275945316772273971947939344604876021356425,
           15059920615250898389512923536227145754348675013619693128994128394507),
    12: Fr(183851305318925536040280960699936162672013570439990762944861330456,
           4034915606109957903742912484982284673842201555870931088194639213827),
}
cal_d = [DK["1"][K] == v for K, v in REVIEW_D2.items()]
report("C08-CALIB-DK-RECORD", all(cal_d),
       "d_K(1)^2 for K = 2..12 equal the review's exact values (52/251, 95/766, ..., K = 12)")


def solve(A, bb):
    m = len(A)
    M = [row[:] + [bb[i]] for i, row in enumerate(A)]
    for col in range(m):
        piv = next(i for i in range(col, m) if M[i][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for i in range(m):
            if i != col and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * c for a, c in zip(M[i], M[col])]
    return [M[i][m] for i in range(m)]


# coefficients of the K = 3 minimiser for target 1, and two-method agreement for K <= 16
c3 = solve([[G[(2, 2)], G[(2, 3)]], [G[(3, 2)], G[(3, 3)]]], [b1[2], b1[3]])
two_ok = c3 == [Fr(160, 251), Fr(105, 251)]
two_n = 1
COEF = {}
for name, (nrm, bv) in targets.items():
    for K in range(2, 17):
        ii = list(range(2, K + 1))
        c = solve([[G[(k, l)] for l in ii] for k in ii], [bv[k] for k in ii])
        COEF[(name, K)] = c
        two_n += 1
        if nrm - sum(bv[k] * ck for k, ck in zip(ii, c)) == DK[name][K]:
            two_ok += 1
report("C09-DK-TWO-METHODS", two_ok == two_n,
       f"c_2 = 160/251, c_3 = 105/251 for target 1; LDL distances equal direct normal-equation solves for all four targets, K <= 16 ({two_ok} of {two_n})")

# normal equations pointwise for A_2, K = 8 (period 840): residual orthogonal to r_2..r_8 and its norm equals d_8(A_2)^2
K = 8
ii = list(range(2, K + 1))
c = COEF[("A2", K)]
den = 1
for ck in c:
    den = lcm(den, ck.denominator)
Lp = 840
resid = [den * A_seq(2, Lp)[m_] - sum(int(ck * den) * (m_ % k) for k, ck in zip(ii, c)) for m_ in range(Lp)]
ne_ok = all(bsum([e * (m_ % k) for m_, e in enumerate(resid)]) == 0 for k in ii)
ne_ok = ne_ok and bsum([e * e for e in resid]) == DK["A2"][8] * den * den
report("C10-NORMAL-EQUATIONS-POINTWISE", ne_ok,
       "K = 8 minimiser for A_2: residual orthogonal to r_2..r_8 over period 840 and ||residual||^2 = d_8(A_2)^2")

mono_ok = True
for name, (nrm, bv) in targets.items():
    prev = nrm
    for K in idx:
        v = DK[name][K]
        if not (0 < v <= prev):
            mono_ok = False
        prev = v
report("C11-DK-POSITIVE-MONOTONE", mono_ok,
       f"0 < d_K(x)^2 <= d_{{K-1}}(x)^2 <= ||x||^2 for x in {{1, A_2, A_4, A_8}} and 2 <= K <= {KMAX}")


# ---------------------------------------------------------------------------
# 5. Mobius data: t_Q, T, s, gamma; the Delta convention; identities (12), (13), (14); bound (3)
# ---------------------------------------------------------------------------
def mobius_sieve(N: int):
    mu = [1] * (N + 1)
    is_p = [True] * (N + 1)
    mu[0] = 0
    for p in range(2, N + 1):
        if is_p[p]:
            for q in range(p, N + 1, p):
                if q > p:
                    is_p[q] = False
                mu[q] = -mu[q]
            for q in range(p * p, N + 1, p * p):
                mu[q] = 0
    return mu


MU = mobius_sieve(NPT)


def A_val(Q: int, n: int) -> int:
    return 1 if n >= 1 and n % (2 * Q) == Q else 0


def t_seq(Q: int, N: int, forward: bool = False):
    """t_Q(k) = sum_{d|k} mu(d) (Delta A_Q)(k/d), k <= N.
    backward: Delta A(m) = A(m) - A(m-1);  forward (test only): A(m+1) - A(m)."""
    dA = [0] * (N + 1)
    for m in range(1, N + 1):
        dA[m] = (A_val(Q, m + 1) - A_val(Q, m)) if forward else (A_val(Q, m) - A_val(Q, m - 1))
    t = [0] * (N + 1)
    for d in range(1, N + 1):
        if MU[d] == 0:
            continue
        md = MU[d]
        for k in range(d, N + 1, d):
            t[k] += md * dA[k // d]
    return t


TQ = {Q: t_seq(Q, NPT) for Q in QLIST}
TQF = {Q: t_seq(Q, NPT, forward=True) for Q in QLIST}


def partials(t):
    N = len(t) - 1
    s = [0] * (N + 1)
    T = [Fr(0)] * (N + 1)
    for k in range(1, N + 1):
        s[k] = s[k - 1] + t[k]
        T[k] = T[k - 1] + Fr(t[k], k)
    return s, T


SQ, TT = {}, {}
for Q in QLIST:
    SQ[Q], TT[Q] = partials(TQ[Q])


def gamma(Q: int, K: int, s=None, T=None) -> Fr:
    s = SQ[Q] if s is None else s
    T = TT[Q] if T is None else T
    return T[K - 1] - Fr(s[K - 1], K)


def p_coeffs(Q: int, h: int) -> dict:
    """coefficients of p_h on r_k, 2 <= k <= K_h  (k = 1 carries t_Q(1) = 0 and r_1 = 0)."""
    Kh = 4 * Q * 2 ** h
    c = {k: -Fr(TQ[Q][k], k) for k in range(2, Kh)}
    c[Kh] = TT[Q][Kh - 1]
    return c


def p_value(c: dict, n: int) -> Fr:
    return sum((ck * (n % k) for k, ck in c.items()), Fr(0))


# convention test
conv = []
conv_msgs = []
for Q in QLIST:
    conv.append(TQ[Q][1] == 0)
    h = 0
    while 4 * Q * 2 ** h <= KMAX:
        Kh = 4 * Q * 2 ** h
        c = p_coeffs(Q, h)
        conv.append(all(p_value(c, m_) == A_val(Q, m_) for m_ in range(1, Kh)))
        conv.append(p_value(c, 1) == 0)
        h += 1
# forward-difference alternative, recorded as evidence (exact computations at finite scope)
fwd_fail_1 = TQF[2][1] == 1          # p_h(1) = t(1) = 1 != A_2(1) = 0 for Q = 2
sF, TF = partials(TQF[2])
fwd_gamma_viol = [K for K in range(2, 65) if abs(gamma(2, K, sF, TF)) >= Fr(5, 16)]
fwd_shift = []
fwd_coef = {}
for Q in QLIST:
    tF = TQF[Q]
    sF2, TF2 = partials(tF)
    Kh = 4 * Q
    cF = {k: -Fr(tF[k], k) for k in range(2, Kh)}
    cF[Kh] = TF2[Kh - 1]
    fwd_coef[Q] = cF
    fwd_shift.append(all(p_value(cF, m_) == A_val(Q, m_ + 1) for m_ in range(1, Kh))
                     and (p_value(cF, 1) == A_val(Q, 2)))
# forward convention, Q = 2, h = 0 (period 840): S^fwd = A_2 - p^fwd_0 has S(1) = -1 and identity (1)
# fails by exactly S(1)^2 = 1; computed directly with bsum, not inferred from Lemma A
cF = fwd_coef[2]
denF = 1
for ck in cF.values():
    denF = lcm(denF, ck.denominator)
LpF = 840
SF = [denF * A_val(2, m_) - sum(int(ck * denF) * (m_ % k) for k, ck in cF.items()) for m_ in range(LpF)]
nSF = bsum([v * v for v in SF]) / (denF * denF)
nDF = bsum([(SF[(2 * m + 1) % LpF] - SF[(2 * m) % LpF]) ** 2 for m in range(LpF)]) / (denF * denF)
nYF = bsum([(SF[(2 * m) % LpF] + SF[(2 * m + 1) % LpF]) ** 2 for m in range(LpF)]) / (4 * denF * denF)
fwd_gap = nSF - (nYF / 2 + nDF / 8)
fwd_id1 = (Fr(SF[1], denF) == -1) and (fwd_gap == 1)
report("C12-DELTA-CONVENTION", all(conv) and fwd_fail_1 and all(fwd_shift) and len(fwd_gamma_viol) > 0 and fwd_id1,
       "backward Delta: t_Q(1) = 0, p_h(1) = 0 and p_h = A_Q on 1 <= n < K_h for all cuts K_h <= KMAX; forward Delta: t_2(1) = 1, "
       f"p_h(n) = A_Q(n+1) on 1 <= n < K_0 for every Q in {QLIST}, S^fwd_{{2,1}}(1) = {Fr(SF[1], denF)} and "
       f"||A_2 - p^fwd_0||^2 - ||Y^fwd||^2/2 - ||D^fwd||^2/8 = {fwd_gap} (identity (1) fails by exactly S(1)^2 = 1, period 840), "
       f"|gamma^fwd_{{2,K}}| >= 5/16 at K in {fwd_gamma_viol[:6]}{'...' if len(fwd_gamma_viol) > 6 else ''}")

# identity (12) and bound (3)
id12 = all(gamma(Q, K) == sum((Fr(SQ[Q][u], u * (u + 1)) for u in range(1, K)), Fr(0))
           for Q in QLIST for K in range(2, KMAX + 2))
report("C13-IDENTITY-12", id12, f"gamma_{{Q,K}} = sum_{{u<K}} s_Q(u)/(u(u+1)) for Q in {{2,4,8}}, 2 <= K <= {KMAX + 1} (pure summation by parts, convention-free)")
b3 = all(abs(gamma(Q, K)) < Fr(5, 4 * Q * Q) for Q in QLIST for K in range(2, NPT + 1))
gmax = {Q: max((abs(gamma(Q, K)) for K in range(2, NPT + 1))) for Q in QLIST}
gargmax = {Q: [K for K in range(2, NPT + 1) if abs(gamma(Q, K)) == gmax[Q]] for Q in QLIST}
report("C14-BOUND-3-FINITE", b3,
       f"|gamma_{{Q,K}}| < 5/(4Q^2) for Q in {{2,4,8}} and all 2 <= K <= {NPT}; max |gamma| = "
       + ", ".join(f"Q={Q}: {gmax[Q]} (bound {Fr(5, 4 * Q * Q)}, attained at K in {gargmax[Q]})" for Q in QLIST)
       + "; DIAGNOSTIC floats: " + ", ".join(f"{float(gmax[Q]):.3e} vs {float(Fr(5, 4 * Q * Q)):.3e}" for Q in QLIST))

# identities (13) and (14) pointwise
NPT13, NPT14 = 2000, 400
id13 = id14 = True
cnt13 = cnt14 = 0
for Q in QLIST:
    h = 0
    while 4 * Q * 2 ** h <= KMAX:
        K = 4 * Q * 2 ** h
        c = p_coeffs(Q, h)
        g = gamma(Q, K)
        s = SQ[Q]
        T = TT[Q]
        for m_ in range(1, NPT13 + 1):
            e = A_val(Q, m_) - p_value(c, m_)
            rhs13 = sum(s[m_ // l] for l in range(1, m_ // K + 1)) + K * (m_ // K) * g
            cnt13 += 1
            if e != rhs13:
                id13 = False
            if m_ <= NPT14:
                rhs14 = sum((T[u] * ((m_ % (u + 1)) - (m_ % u)) for u in range(K, m_ + 1)), Fr(0))
                cnt14 += 1
                if e != rhs14:
                    id14 = False
        h += 1
report("C15-IDENTITY-13", id13, f"e_K(n) = sum_{{l<=n/K}} s_Q(floor(n/l)) + K floor(n/K) gamma_{{Q,K}} pointwise, all cuts K_h <= {KMAX}, n <= {NPT13} ({cnt13} points)")
report("C16-IDENTITY-14", id14, f"e_K(n) = sum_{{u=K}}^n T_Q(u) [r_{{u+1}}(n) - r_u(n)] pointwise, all cuts K_h <= {KMAX}, n <= {NPT14} ({cnt14} points)")


# ---------------------------------------------------------------------------
# 6. norms of the approximants, the average, the two channels; identity (1); lemma; efficiency
# ---------------------------------------------------------------------------
def quad(tab, c: dict) -> Fr:
    ks = list(c.items())
    tot = Fr(0)
    for a, (k, ck) in enumerate(ks):
        tot += ck * ck * tab[(k, k)]
        for l, cl in ks[a + 1:]:
            tot += 2 * ck * cl * tab[(k, l)]
    return tot


def dotv(vec: dict, c: dict) -> Fr:
    return sum((ck * vec[k] for k, ck in c.items()), Fr(0))


PH = {}     # ||A_Q - p_h||^2
AVG = {}    # ||A_Q - avg_J||^2
YN = {}     # ||Y_{Q,J}||^2
DN = {}     # ||D_{Q,J}||^2
CUTS = {}
for Q in QLIST:
    hs = []
    h = 0
    while 4 * Q * 2 ** h <= KMAX:
        hs.append(h)
        h += 1
    CUTS[Q] = hs
    Csum = {}
    for h in hs:
        c = p_coeffs(Q, h)
        PH[(Q, h)] = nA[Q] - 2 * dotv(bA[Q], c) + quad(G, c)
        for k, ck in c.items():
            Csum[k] = Csum.get(k, Fr(0)) + ck
        J = h + 1
        C = dict(Csum)
        AVG[(Q, J)] = nA[Q] - Fr(2, J) * dotv(bA[Q], C) + quad(G, C) / (J * J)
        YN[(Q, J)] = Fr(J * J, 4) * nAh[Q] - Fr(J, 2) * dotv(bLA[Q], C) + quad(GL, C) / 4
        DN[(Q, J)] = J * J * nAh[Q] + 2 * J * dotv(bHA[Q], C) + quad(GH, C)

id1 = all(AVG[(Q, J)] == YN[(Q, J)] / (2 * J * J) + DN[(Q, J)] / (8 * J * J)
          for Q in QLIST for J in range(1, len(CUTS[Q]) + 1))
pairs = [(Q, J) for Q in QLIST for J in range(1, len(CUTS[Q]) + 1)]
report("C17-IDENTITY-1", id1,
       f"||A_Q - avg_J||^2 = ||Y||^2/(2J^2) + ||D||^2/(8J^2) exactly for (Q,J) in {pairs}, the three norms from the three independent tables")


# direct periodic evaluation for small cuts (independent of the bilinear expansion)
def direct_norms(Q: int, J: int):
    Kmax_h = 4 * Q * 2 ** (J - 1)
    Lp = 2 * Q
    for k in range(2, Kmax_h + 1):
        Lp = lcm(Lp, k)
    C = {}
    for h in range(J):
        for k, ck in p_coeffs(Q, h).items():
            C[k] = C.get(k, Fr(0)) + ck
    den = 1
    for ck in C.values():
        den = lcm(den, ck.denominator)
    Ci = {k: int(ck * den) for k, ck in C.items()}
    aq = A_seq(Q, Lp)
    S = [J * den * aq[m_] - sum(ci * (m_ % k) for k, ci in Ci.items()) for m_ in range(Lp)]
    nS = bsum([v * v for v in S]) / (den * den)
    Dd = [S[(2 * m + 1) % Lp] - S[(2 * m) % Lp] for m in range(Lp)]
    Yy = [S[(2 * m) % Lp] + S[(2 * m + 1) % Lp] for m in range(Lp)]
    nD = bsum([v * v for v in Dd]) / (den * den)
    nY = bsum([v * v for v in Yy]) / (4 * den * den)
    return nS, nD, nY, S[1] == 0 and S[0] == 0


t0 = time.time()
dir_ok = True
dir_msgs = []
for (Q, J) in ((2, 1), (4, 1), (2, 2)):
    nS, nD, nY, s1 = direct_norms(Q, J)
    okq = (nS == J * J * AVG[(Q, J)]) and (nD == DN[(Q, J)]) and (nY == YN[(Q, J)]) and s1
    if J == 1:
        okq = okq and nS == PH[(Q, 0)]
    dir_ok = dir_ok and okq
    dir_msgs.append(f"(Q,J)=({Q},{J})")
report("C18-DIRECT-PERIODIC-CROSSCHECK", dir_ok,
       "||S||^2, ||D||^2, ||Y||^2 and S(1) = 0 by direct evaluation over the full period (840 and 720720) agree with the bilinear table expansion for " + ", ".join(dir_msgs))

# lemma: avg_J in span{r_k : 2 <= k <= K_{J-1}}, hence ||A_Q - avg_J||^2 >= d_{K_{J-1}}(A_Q)^2, hence the Y lower bound
lem_ok = True
eff_ok = True
EFF_P = {}
EFF_A = {}
LOWER_Y = {}
for Q in QLIST:
    for h in CUTS[Q]:
        Kh = 4 * Q * 2 ** h
        c = p_coeffs(Q, h)
        # substantive part: the k = 1 coefficient of p_h is -t_Q(1)/1 and vanishes (t_Q(1) = 0, also C12);
        # the range check on the keys of p_coeffs is by construction and is recorded only for completeness
        if not (TQ[Q][1] == 0 and min(c) >= 2 and max(c) == Kh):
            lem_ok = False
        EFF_P[(Q, h)] = PH[(Q, h)] / DK[f"A{Q}"][Kh]
        if EFF_P[(Q, h)] < 1:
            eff_ok = False
        J = h + 1
        d2 = DK[f"A{Q}"][Kh]
        if not AVG[(Q, J)] >= d2:
            lem_ok = False
        LOWER_Y[(Q, J)] = 2 * J * J * d2 - DN[(Q, J)] / 4
        if not YN[(Q, J)] >= LOWER_Y[(Q, J)]:
            lem_ok = False
        EFF_A[(Q, J)] = AVG[(Q, J)] / d2
        if EFF_A[(Q, J)] < 1:
            eff_ok = False
report("C19-LEMMA-SPAN-INEQUALITY", lem_ok,
       "k = 1 coefficient -t_Q(1) of p_h is 0 and p_h has no r_k with k > K_h, so p_h in span{r_2..r_{K_h}}; "
       "||A_Q - avg_J||^2 >= d_{K_{J-1}}(A_Q)^2 and ||Y||^2 >= 2 J^2 d_{K_{J-1}}(A_Q)^2 - ||D||^2/4 exactly on all computed (Q,J)")
report("C20-EFFICIENCY-RATIOS", eff_ok,
       "every efficiency ratio ||A_Q - p_h||^2 / d_{K_h}(A_Q)^2 and ||A_Q - avg_J||^2 / d_{K_{J-1}}(A_Q)^2 is >= 1 "
       "(corollary of Lemma D, i.e. of C19; recorded as a consistency line, not an independent test)")

# ---------------------------------------------------------------------------
# 7. tables
# ---------------------------------------------------------------------------
print()
print(f"# exact d_K(x)^2 for K <= 12 (x in 1, A_2, A_4, A_8); KMAX = {KMAX}")
for name in targets:
    for K in range(2, 13):
        print(f"  d_{K:2d}({name})^2 = {DK[name][K]}")
print()
print("# DIAGNOSTIC (float, asserts nothing): d_K(x)^2 and d_K(x)^2 * log K")
print("  K      d_K(1)^2  *logK    d_K(A2)^2 *logK    d_K(A4)^2 *logK    d_K(A8)^2 *logK")
for K in idx:
    row = f"  {K:3d}"
    for name in targets:
        v = float(DK[name][K])
        row += f"  {v:.6f} {v * math.log(K):.4f}"
    print(row)
FULL_DIGITS = 8000


def exact_str(fr: Fr) -> str:
    """exact record of a fraction: the fraction itself when it has at most FULL_DIGITS
    digits, otherwise its digit count and the SHA-256 of the canonical string num/den
    (a replay on another architecture compares the fingerprint exactly)."""
    s = f"{fr.numerator}/{fr.denominator}"
    nd = len(str(fr.numerator)) + len(str(fr.denominator))
    if nd <= FULL_DIGITS:
        return s
    return f"<{nd} digits; sha256(num/den) = {hashlib.sha256(s.encode('ascii')).hexdigest()}>"


print()
print(f"# exact approximant errors ||A_Q - p_h||^2, distances d_{{K_h}}(A_Q)^2 and efficiency ratios ||A_Q - p_h||^2 / d^2")
print(f"#   (fractions printed in full up to {FULL_DIGITS} digits, longer ones as digit count plus SHA-256 of num/den)")
for Q in QLIST:
    for h in CUTS[Q]:
        Kh = 4 * Q * 2 ** h
        print(f"  Q={Q} h={h} K_h={Kh}: ||A_Q - p_h||^2 = {exact_str(PH[(Q, h)])}")
        print(f"      d_{Kh}(A_{Q})^2 = {exact_str(DK[f'A{Q}'][Kh])}")
        print(f"      ratio = {exact_str(EFF_P[(Q, h)])}")
print("# DIAGNOSTIC (float renderings of the fractions above, assert nothing)")
for Q in QLIST:
    for h in CUTS[Q]:
        Kh = 4 * Q * 2 ** h
        print(f"  Q={Q} h={h} K_h={Kh}: ||A_Q - p_h||^2 ~ {float(PH[(Q, h)]):.6e}  d^2 ~ {float(DK[f'A{Q}'][Kh]):.6e}  ratio ~ {float(EFF_P[(Q, h)]):.6f}")
print()
print("# exact mean-channel data: ||A_Q - avg_J||^2, ||Y||^2, ||D||^2, lower bound 2J^2 d^2 - ||D||^2/4, efficiency ||A_Q - avg_J||^2 / d^2")
for Q in QLIST:
    for J in range(1, len(CUTS[Q]) + 1):
        K = 4 * Q * 2 ** (J - 1)
        print(f"  Q={Q} J={J} K_(J-1)={K}:")
        print(f"      ||A_Q - avg_J||^2 = {exact_str(AVG[(Q, J)])}")
        print(f"      ||Y||^2 = {exact_str(YN[(Q, J)])}")
        print(f"      ||D||^2 = {exact_str(DN[(Q, J)])}")
        print(f"      lowerY = {exact_str(LOWER_Y[(Q, J)])}")
        print(f"      eff = {exact_str(EFF_A[(Q, J)])}")
print("# DIAGNOSTIC (float renderings of the fractions above and derived ratios, assert nothing)")
for Q in QLIST:
    for J in range(1, len(CUTS[Q]) + 1):
        K = 4 * Q * 2 ** (J - 1)
        print(f"  Q={Q} J={J} K_(J-1)={K}: ||A_Q-avg||^2 ~ {float(AVG[(Q, J)]):.6e}  ||Y||^2 ~ {float(YN[(Q, J)]):.6e}  "
              f"||D||^2 ~ {float(DN[(Q, J)]):.6e}  lowerY ~ {float(LOWER_Y[(Q, J)]):.6e}  eff ~ {float(EFF_A[(Q, J)]):.6f}  "
              f"||Y||^2/J ~ {float(YN[(Q, J)]) / J:.6e}  ||D||^2/(8J^2) ~ {float(DN[(Q, J)]) / (8 * J * J):.6e}  ||Y||^2/(2J^2) ~ {float(YN[(Q, J)]) / (2 * J * J):.6e}")
print()
print("# gamma_{Q,K} at the cuts (exact) and the bound 5/(4Q^2) (exact); DIAGNOSTIC float renderings in parentheses")
for Q in QLIST:
    for h in CUTS[Q]:
        K = 4 * Q * 2 ** h
        print(f"  Q={Q} K={K}: gamma = {gamma(Q, K)}  bound = {Fr(5, 4 * Q * Q)}  (DIAGNOSTIC ~{float(gamma(Q, K)):.4e} vs {float(Fr(5, 4 * Q * Q)):.4e})")
print()
print("# t_Q(k) for k <= 40:")
for Q in QLIST:
    print(f"  Q={Q}: {TQ[Q][1:41]}")

# ---------------------------------------------------------------------------
npass = sum(1 for _, ok, _ in RESULTS if ok)
print()
print(f"# total runtime {time.time() - T_START:.1f} s", file=sys.stderr)
print(f"CHECKS: {npass} of {len(RESULTS)} PASS")
sys.exit(0 if npass == len(RESULTS) else 1)
