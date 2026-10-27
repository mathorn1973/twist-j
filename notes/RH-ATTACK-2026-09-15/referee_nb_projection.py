#!/usr/bin/env python3
"""referee_nb_projection.py -- independent referee re-implementation for lane A (ATTACK-NB-PROJECTION).
Run from its own directory next to verify_nb_projection.py:
  LC_ALL=C PYTHONHASHSEED=0 python3 referee_nb_projection.py
Exit 0 iff every referee check passes; one PASS/FAIL line per check; final REFEREE CHECKS line.
Own code throughout: brute-force cycle detection for the periodic binary sum,
divisor-sum Mobius convolution, Fraction Gaussian elimination for K <= 16,
multi-prime modular LDL for the full census K <= 72, direct periodic channel
norms.  Compares against lane_dump.json (the lane's exact internal tables) and
against the exact fractions printed in the lane's stdout."""
import json, random, sys, time
sys.set_int_max_str_digits(0)
from fractions import Fraction as Fr
from math import gcd, log

import os, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
KMAX = 72
fails = []


def check(name, ok, msg=""):
    print(f"{name}: {'PASS' if ok else 'FAIL'} {msg}", flush=True)
    if not ok:
        fails.append(name)


def lcm(a, b):
    return a * b // gcd(a, b)


# ---------- own periodic binary sum: brute-force cycle detection ----------
def bsum_own(q):
    L = len(q)
    P = [Fr(0)]
    for v in q:
        P.append(P[-1] + v)
    S = P[L]
    def A(M):  # sum_{n<M} q_n
        return (M // L) * S + P[M % L]
    # block j value depends only on residue pair (2^j mod L, 2^{j+1} mod L) plus 2^j S/L
    seen = {}
    j = 0
    b = 1 % L
    dseq = []
    while b not in seen:
        seen[b] = j
        b2 = (2 * b) % L
        # eta(r) = P(r) - r S/L ; d_j = eta(b_{j+1}) - eta(b_j)
        dseq.append((P[b2] - Fr(b2 * S, L)) - (P[b] - Fr(b * S, L)))
        b = b2
        j += 1
    h = seen[b]
    t = j - h
    total = Fr(2 * S, L)
    for i in range(h):
        total += dseq[i] / 4 ** i
    cyc = sum(dseq[h + a] / 4 ** a for a in range(t))
    total += cyc / (4 ** h * (1 - Fr(1, 4 ** t)))
    return total


def bsum_brute(q, J0=14):
    L = len(q)
    tot = Fr(0)
    for j in range(J0):
        tot += Fr(sum(q[n % L] for n in range(2 ** j, 2 ** (j + 1))), 4 ** j)
    tail = Fr(2, 2 ** J0)
    return tot + tail * min(q), tot + tail * max(q)


rng = random.Random(7)
ok = True
for _ in range(120):
    L = rng.randint(1, 90)
    q = [Fr(rng.randint(-7, 7), rng.randint(1, 4)) for _ in range(L)]
    v = bsum_own(q)
    lo, hi = bsum_brute(q)
    ok = ok and lo <= v <= hi
check("R01-own-bsum-enclosure", ok, "120 random periodic sequences inside brute-force enclosure")
check("R02-own-norm-1-and-layers", bsum_own([Fr(1)]) == 2 and all(
    bsum_own([Fr(1 if n % (2 ** (j + 1)) == 2 ** j else 0) for n in range(2 ** (j + 1))]) == Fr(3, 2 * 4 ** j) for j in range(0, 7)))


# ---------- Gram tables (own) ----------
def rk(k, L):
    return [n % k for n in range(L)]


def A_seq(Q, L):
    if Q == 1:
        return [n % 2 for n in range(L)]
    return [1 if n % (2 * Q) == Q else 0 for n in range(L)]


t0 = time.time()
G = {}
for k in range(2, KMAX + 1):
    for l in range(k, KMAX + 1):
        L = lcm(k, l)
        a, b = rk(k, L), rk(l, L)
        G[(k, l)] = G[(l, k)] = bsum_own([Fr(x * y) for x, y in zip(a, b)])
print(f"# own Gram in {time.time() - t0:.1f}s", flush=True)
targets = {}
for name, Q in (("1", 0), ("A2", 2), ("A4", 4), ("A8", 8)):
    if Q == 0:
        nrm = Fr(2)
        bv = {k: bsum_own([Fr(x) for x in rk(k, k)]) for k in range(2, KMAX + 1)}
    else:
        nrm = bsum_own([Fr(x) for x in A_seq(Q, 2 * Q)])
        bv = {}
        for k in range(2, KMAX + 1):
            L = lcm(2 * Q, k)
            bv[k] = bsum_own([Fr(x * y) for x, y in zip(A_seq(Q, L), rk(k, L))])
    targets[name] = (nrm, bv)
check("R03-calib-gram", G[(2, 2)] == Fr(3, 2) and G[(2, 3)] == Fr(13, 10) and G[(3, 3)] == Fr(14, 5)
      and targets["1"][1][2] == Fr(3, 2) and targets["1"][1][3] == 2)

# run the lane's verifier in-process (stdout suppressed) and take its exact tables
t0 = time.time()
_argv = sys.argv
sys.argv = ["verify_nb_projection.py"]
_g = {"__name__": "__main__"}
_buf = io.StringIO()
try:
    with contextlib.redirect_stdout(_buf):
        exec(compile(open(os.path.join(HERE, "verify_nb_projection.py")).read(), "verify_nb_projection.py", "exec"), _g)
except SystemExit:
    pass
sys.argv = _argv
lane_stdout = _buf.getvalue()
print(f"# lane verifier executed in-process in {time.time() - t0:.0f}s; its final line: {lane_stdout.strip().splitlines()[-1]}", flush=True)
lane = {"DK": {name: {str(K): str(v) for K, v in tab.items()} for name, tab in _g["DK"].items()},
        "PH": {f"{Q},{h}": str(v) for (Q, h), v in _g["PH"].items()},
        "AVG": {f"{Q},{J}": str(v) for (Q, J), v in _g["AVG"].items()},
        "YN": {f"{Q},{J}": str(v) for (Q, J), v in _g["YN"].items()},
        "DN": {f"{Q},{J}": str(v) for (Q, J), v in _g["DN"].items()},
        "G": {f"{k},{l}": str(v) for (k, l), v in _g["G"].items() if k <= l}}
laneG = {tuple(map(int, k.split(","))): Fr(v) for k, v in lane["G"].items()}
check("R04-gram-equals-lane", all(G[(k, l)] == laneG[(k, l)] for k in range(2, KMAX + 1) for l in range(k, KMAX + 1)),
      "all 2556 Gram entries equal the lane's (different cycle bookkeeping)")


# ---------- exact d_K^2 by Gaussian elimination, K <= 16 ----------
def solve(A, bb):
    m = len(A)
    M = [row[:] + [bb[i]] for i, row in enumerate(A)]
    for c in range(m):
        p = next(i for i in range(c, m) if M[i][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for i in range(m):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[c])]
    return [M[i][m] for i in range(m)]


laneDK = {name: {int(K): Fr(v) for K, v in tab.items()} for name, tab in lane["DK"].items()}
ok = True
for name, (nrm, bv) in targets.items():
    for K in range(2, 17):
        ii = list(range(2, K + 1))
        c = solve([[G[(k, l)] for l in ii] for k in ii], [bv[k] for k in ii])
        d2 = nrm - sum(bv[k] * ck for k, ck in zip(ii, c))
        ok = ok and d2 == laneDK[name][K]
check("R05-dK-exact-K<=16", ok, "own Gaussian elimination equals lane LDL for 4 targets, K <= 16")

# stdout exact fractions (K <= 12) transcribed from the lane's stdout file
stdout_lines = lane_stdout.splitlines()
ok = True
cnt = 0
for ln in stdout_lines:
    if ln.startswith("  d_") and ")^2 = " in ln:
        head, val = ln.split(" = ")
        K = int(head[4:6])
        name = head[head.index("(") + 1:head.index(")")]
        ii = list(range(2, K + 1))
        nrm, bv = targets[name]
        c = solve([[G[(k, l)] for l in ii] for k in ii], [bv[k] for k in ii])
        ok = ok and (nrm - sum(bv[k] * ck for k, ck in zip(ii, c)) == Fr(val))
        cnt += 1
check("R06-dK-stdout-K<=12", ok and cnt == 44, f"{cnt} printed exact fractions reproduced")


# ---------- modular LDL for all K <= 72 (three primes) ----------
def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


PRIMES = [(1 << 61) - 1, 10 ** 18 + 3, 10 ** 18 + 9]
check("R07-primes", all(is_prime(p) for p in PRIMES))


def modfr(x, p):
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


ok = True
idx = list(range(2, KMAX + 1))
n = len(idx)
for p in PRIMES:
    Gm = [[modfr(G[(k, l)], p) for l in idx] for k in idx]
    Lm = [[0] * n for _ in range(n)]
    D = [0] * n
    for j in range(n):
        s = (Gm[j][j] - sum(Lm[j][k] * Lm[j][k] % p * D[k] for k in range(j))) % p
        D[j] = s
        if s == 0:
            ok = False
            break
        sinv = pow(s, -1, p)
        Lm[j][j] = 1
        for i in range(j + 1, n):
            Lm[i][j] = (Gm[i][j] - sum(Lm[i][k] * Lm[j][k] % p * D[k] for k in range(j))) * sinv % p
    for name, (nrm, bv) in targets.items():
        y = [0] * n
        for i in range(n):
            y[i] = (modfr(bv[idx[i]], p) - sum(Lm[i][k] * y[k] for k in range(i))) % p
        acc = modfr(nrm, p)
        for i in range(n):
            acc = (acc - y[i] * y[i] % p * pow(D[i], -1, p)) % p
            if acc != modfr(laneDK[name][idx[i]], p):
                ok = False
check("R08-dK-modular-K<=72", ok, "lane's exact d_K(x)^2 for all K <= 72, 4 targets, agree mod three 60-bit primes with own modular LDL")

# monotone/positive on the lane values, and the DIAGNOSTIC range claims
ok = True
for name in targets:
    prev = targets[name][0]
    for K in idx:
        v = laneDK[name][K]
        ok = ok and 0 < v <= prev
        prev = v
check("R09-lane-dK-positive-monotone", ok)
rng_claims = {"1": (0.0969, 0.1004), "A2": (0.0935, 0.1004), "A4": (0.0608, 0.0649), "A8": (0.0283, 0.0305)}
for name, (lo, hi) in rng_claims.items():
    vals = [float(laneDK[name][K]) * log(K) for K in range(32, 73)]
    print(f"  DIAGNOSTIC {name}: d_K^2 log K on 32..72 in [{min(vals):.4f}, {max(vals):.4f}]  (lane sec. 8.2 claims [{lo}, {hi}]); summary item 2 claims [0.0990, 0.1004] for target 1")
print(f"  DIAGNOSTIC d_72(A2)^2/d_72(1)^2 = {float(laneDK['A2'][72] / laneDK['1'][72]):.4f}")


# ---------- own Mobius data ----------
N = 4096
mu = [1] * (N + 1)
mu[0] = 0
for i in range(2, N + 1):
    if mu[i] == 1 or mu[i] == -1:
        pass
# simple mu via factorisation
def mobius(k):
    m, res, p = k, 1, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res


MU = [0] + [mobius(k) for k in range(1, N + 1)]


def Aq(Q, n):
    return 1 if n >= 1 and n % (2 * Q) == Q else 0


def t_own(Q, forward=False):
    dA = [0] * (N + 2)
    for m in range(1, N + 1):
        dA[m] = (Aq(Q, m + 1) - Aq(Q, m)) if forward else (Aq(Q, m) - Aq(Q, m - 1))
    t = [0] * (N + 1)
    for k in range(1, N + 1):
        s = 0
        for d in range(1, k + 1):
            if k % d == 0 and MU[d]:
                s += MU[d] * dA[k // d]
        t[k] = s
    return t


T = {}
for Q in (2, 4, 8):
    T[Q] = t_own(Q)
# t_Q(k) k<=40 vs stdout
tq_lines = {2: "[0, 1, -1, -1, 0, 1, -1, 0, 1, 0, -1, 0, 0, 1, 0, 0, 0, -1, -1, 0, 2, 1, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 2, 0, 0, 0, 0, 1, 0, 0]",
            4: "[0, 0, 0, 1, -1, 0, 0, -1, 0, 1, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1, 0, 0, -1, -1, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0]",
            8: "[0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"}
check("R10-tQ-k<=40", all(str(T[Q][1:41]) == tq_lines[Q] for Q in (2, 4, 8)))
# closed form check of t_Q: t_Q(k) = sum_{m: k = m Q u, u odd} mu(m) - sum_{k = m(Qu+1), u odd} mu(m)
ok = True
for Q in (2, 4, 8):
    for k in range(1, 2001):
        v = 0
        for m in range(1, k + 1):
            if k % m == 0 and MU[m]:
                r = k // m
                if r % (2 * Q) == Q:
                    v += MU[m]
                if r >= 2 and (r - 1) % (2 * Q) == Q:
                    v -= MU[m]
        ok = ok and v == T[Q][k]
check("R11-tQ-source-pairs", ok, "t_Q = sum over source pairs (mQu, m(Qu+1)) -- the backward convention is the one encoded in the Mobius note's (4) and (23)")


def partials(t):
    s = [0] * (N + 1)
    TT = [Fr(0)] * (N + 1)
    for k in range(1, N + 1):
        s[k] = s[k - 1] + t[k]
        TT[k] = TT[k - 1] + Fr(t[k], k)
    return s, TT


S_, TT_ = {}, {}
for Q in (2, 4, 8):
    S_[Q], TT_[Q] = partials(T[Q])


def gamma(Q, K):
    return TT_[Q][K - 1] - Fr(S_[Q][K - 1], K)


gm = {}
ok = True
for Q in (2, 4, 8):
    vals = [abs(gamma(Q, K)) for K in range(2, N + 1)]
    gm[Q] = max(vals)
    ok = ok and all(v < Fr(5, 4 * Q * Q) for v in vals)
check("R12-bound3-K<=4096", ok and gm == {2: Fr(1, 6), 4: Fr(1, 20), 8: Fr(1, 72)}, f"maxima {gm}")
argmax = {Q: [K for K in range(2, N + 1) if abs(gamma(Q, K)) == gm[Q]] for Q in (2, 4, 8)}
print(f"  K attaining max |gamma|: {argmax}")
# (12)
check("R13-identity-12", all(gamma(Q, K) == sum(Fr(S_[Q][u], u * (u + 1)) for u in range(1, K)) for Q in (2, 4, 8) for K in range(2, 300)))
# gamma at the cuts vs stdout
cut_vals = {(2, 8): "11/168", (2, 16): "89/2772", (2, 32): "6461513/450627408", (2, 64): "921199518865/94031632629396",
            (4, 16): "23/1560", (4, 32): "19043/2111200", (4, 64): "16110959369/6250460416200", (8, 32): "43/10800", (8, 64): "95647/58892400"}
check("R14-gamma-cuts", all(gamma(Q, K) == Fr(v) for (Q, K), v in cut_vals.items()))


def p_coeffs(Q, h, t=None, TTx=None):
    t = T[Q] if t is None else t
    TTx = TT_[Q] if TTx is None else TTx
    Kh = 4 * Q * 2 ** h
    c = {k: -Fr(t[k], k) for k in range(2, Kh)}
    c[Kh] = TTx[Kh - 1]
    return c


def pval(c, n):
    return sum(ck * (n % k) for k, ck in c.items())


# Lemma C, (13), (14) pointwise (own)
ok13 = ok14 = okC = True
for Q in (2, 4, 8):
    for h in range(0, 4):
        K = 4 * Q * 2 ** h
        if K > 72:
            break
        c = p_coeffs(Q, h)
        g = gamma(Q, K)
        for m in range(1, 601):
            e = Aq(Q, m) - pval(c, m)
            if m < K:
                okC = okC and e == 0
            rhs13 = sum(S_[Q][m // l] for l in range(1, m // K + 1)) + K * (m // K) * g
            ok13 = ok13 and e == rhs13
            rhs14 = sum(TT_[Q][u] * ((m % (u + 1)) - (m % u)) for u in range(K, m + 1))
            ok14 = ok14 and e == rhs14
check("R15-lemmaC-below-cut", okC)
check("R16-identity-13-n<=600", ok13)
check("R17-identity-14-n<=600", ok14)

# forward convention: p^+_h(n) = A_Q(n+1) below the cut for ALL Q incl. Q = 2; S(1) = -J for Q = 2 only
ok = True
for Q in (2, 4, 8):
    tf = t_own(Q, forward=True)
    sf, TTf = partials(tf)
    c = p_coeffs(Q, 0, tf, TTf)
    K = 4 * Q
    ok = ok and all(pval(c, m) == Aq(Q, m + 1) for m in range(1, K))
    ok = ok and (pval(c, 1) == (1 if Q == 2 else 0))
check("R18-forward-shift-all-Q", ok, "forward convention shifts p_h(n) = A_Q(n+1) for Q = 2, 4, 8 alike (lane states it only for Q = 4, 8); S(1) != 0 only for Q = 2")


# ---------- direct periodic channel norms ----------
def direct(Q, J):
    K = 4 * Q * 2 ** (J - 1)
    Lp = 2 * Q
    for k in range(2, K + 1):
        Lp = lcm(Lp, k)
    C = {}
    for h in range(J):
        for k, ck in p_coeffs(Q, h).items():
            C[k] = C.get(k, Fr(0)) + ck
    S = [J * Aq(Q, m) - sum(ck * (m % k) for k, ck in C.items()) for m in range(Lp)]
    S[0] = Fr(0)
    nS = bsum_own([v * v for v in S])
    Dd = [S[(2 * m + 1) % Lp] - S[(2 * m) % Lp] for m in range(Lp)]
    Yy = [(S[(2 * m) % Lp] + S[(2 * m + 1) % Lp]) / 2 for m in range(Lp)]
    return nS, bsum_own([v * v for v in Dd]), bsum_own([v * v for v in Yy]), S[1]


t0 = time.time()
nS, nD, nY, s1 = direct(2, 1)
check("R19-direct-(2,1)", nS == Fr("217759/3210480") and nY == Fr("47507/802620") and nD == Fr("167/546") and s1 == 0
      and nS == nY / 2 + nD / 8, "stdout fractions for (Q,J)=(2,1) reproduced by direct period-840 evaluation; identity (1) exact")
nS, nD, nY, s1 = direct(4, 1)
check("R20-direct-(4,1)", nS == Fr("245736174487/4536558936000") and nY == Fr("47599861003/567069867000") and nD == Fr("4365817/44739240") and s1 == 0
      and nS == nY / 2 + nD / 8)
nS, nD, nY, s1 = direct(2, 2)
lanePH = {k: Fr(v) for k, v in lane["PH"].items()}
laneAVG = {k: Fr(v) for k, v in lane["AVG"].items()}
laneYN = {k: Fr(v) for k, v in lane["YN"].items()}
laneDN = {k: Fr(v) for k, v in lane["DN"].items()}
check("R21-direct-(2,2)", nS == 4 * laneAVG["2,2"] and nY == laneYN["2,2"] and nD == laneDN["2,2"] and s1 == 0 and nS / 4 == nY / 8 + nD / 32,
      f"period 720720 direct evaluation equals lane tables ({time.time() - t0:.0f}s)")
# single cut h = 1 for Q = 2 directly (period 720720)
c = p_coeffs(2, 1)
Lp = 720720
S = [Aq(2, m) - pval(c, m) for m in range(Lp)]
check("R22-direct-||A2-p_1||^2", bsum_own([v * v for v in S]) == Fr("16888898572930617627517/246084177629303845731900"))

# Lemma D chain and efficiency on lane values
ok = True
for key, v in laneAVG.items():
    Q, J = map(int, key.split(","))
    K = 4 * Q * 2 ** (J - 1)
    d2 = laneDK[f"A{Q}"][K]
    ok = ok and v >= d2 and laneYN[key] >= 2 * J * J * d2 - laneDN[key] / 4 and v == laneYN[key] / (2 * J * J) + laneDN[key] / (8 * J * J)
for key, v in lanePH.items():
    Q, h = map(int, key.split(","))
    ok = ok and v >= laneDK[f"A{Q}"][4 * Q * 2 ** h]
check("R23-lemmaD-chain-on-lane-values", ok)
print("  DIAGNOSTIC efficiency sharp Q=2:", [round(float(lanePH[f'2,{h}'] / laneDK['A2'][8 * 2 ** h]), 4) for h in range(4)])
print("  DIAGNOSTIC efficiency avg   Q=2:", [round(float(laneAVG[f'2,{J}'] / laneDK['A2'][8 * 2 ** (J - 1)]), 4) for J in range(1, 5)])
print("  DIAGNOSTIC ||D_{2,J}||^2:", [round(float(laneDN[f'2,{J}']), 4) for J in range(1, 5)], " increments:",
      [round(float(laneDN[f'2,{J + 1}'] - laneDN[f'2,{J}']), 4) for J in range(1, 4)])
print("  DIAGNOSTIC ||Y_{2,J}||^2/J:", [round(float(laneYN[f'2,{J}']) / J, 4) for J in range(1, 5)])

# Lemma A on random sequences with own weights
def wB(n):
    return Fr(1, 4 ** (n.bit_length() - 1))


ok = True
for _ in range(40):
    x = {n: Fr(rng.randint(-6, 6), rng.randint(1, 3)) for n in rng.sample(range(1, 300), 15)}
    xv = lambda n: x.get(n, Fr(0))
    lhs = sum(wB(n) * v * v for n, v in x.items())
    rhs = xv(1) ** 2 + sum(wB(m) * ((xv(2 * m) + xv(2 * m + 1)) / 2) ** 2 for m in range(1, 300)) / 2 \
        + sum(wB(m) * (xv(2 * m + 1) - xv(2 * m)) ** 2 for m in range(1, 300)) / 8
    ok = ok and lhs == rhs
check("R24-lemmaA-random", ok)

npass = 24 - len(fails)
print(f"REFEREE CHECKS: {npass} of 24 PASS; failures {fails}; {time.time() - T0:.0f}s")
sys.exit(0 if not fails else 1)
