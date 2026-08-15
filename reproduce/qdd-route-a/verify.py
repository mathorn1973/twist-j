#!/usr/bin/env python3
"""
reproduce/qdd-route-a/verify.py

Exact reproduction of the QDD Route A dictionary on the finite balanced piston
carrier: direct cyclotomic write against the Gram/projector factor route on all
15625 checkpoints, the registered controls, the projector-pair theorem, the
diagonal boundary of the two Q slots, and the value table of the two-outcome
measure.  Rational arithmetic only (fractions).  No input, no randomness, no
files, no environment, no network.  Deterministic stdout.

Evidence for registry claims QDD-ALGEBRAIC-FACTORIZATION, QDD-PROJECTOR-PAIR-TR4,
QDD-QCARRIER-DIAGONAL-BOUNDARY and QDD-BORN-READOUT-MEASURE, and for the
QUADRATIC-DECODER-DATA dictionary after its fold.  The verifier confirms an
already derived identity; it is not an independent readout.

Run from the repository root:  python3 reproduce/qdd-route-a/verify.py
Expected: byte identical to EXPECTED.txt, RESULT 15/15 ALL PASS, exit 0, no stderr.
"""
from fractions import Fraction as Fr
from itertools import product

# ---------------------------------------------------------------- K = Q(zeta_5), basis B0 = (1, z, z^2, z^3)
def zpow(k):
    k %= 5
    if k < 4:
        e = [Fr(0)] * 4; e[k] = Fr(1); return tuple(e)
    return (Fr(-1),) * 4                       # z^4 = -1 - z - z^2 - z^3

def kadd(a, b): return tuple(x + y for x, y in zip(a, b))
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def kscale(c, a): return tuple(c * x for x in a)
def kmul(a, b):
    out = [Fr(0)] * 4
    for i in range(4):
        if a[i] == 0: continue
        for j in range(4):
            if b[j] == 0: continue
            z = zpow(i + j)
            for t in range(4): out[t] += a[i] * b[j] * z[t]
    return tuple(out)
def ksigma(a, s):                              # Galois automorphism z -> z^s
    out = (Fr(0),) * 4
    for i in range(4):
        if a[i] != 0: out = kadd(out, kscale(a[i], zpow(i * s)))
    return out
def kbar(a): return ksigma(a, 4)               # sigma_4 = complex conjugation
def ktr(a): return 4 * a[0] - a[1] - a[2] - a[3]  # Tr(1) = 4, Tr(z^k) = -1
def pair_tr(x, y): return ktr(kmul(x, kbar(y))) / 5     # <x,y>_tr = (1/5) Tr(x sigma_4(y))
def pair_bil(x, y): return ktr(kmul(x, y)) / 5          # bilinear trace form (1/5) Tr(x y)
ZERO_K = (Fr(0),) * 4
LAMBDA_B = kadd(kadd(zpow(0), zpow(1)), kadd(zpow(2), zpow(3)))   # 1 + z + z^2 + z^3

# ---------------------------------------------------------------- linear algebra over Q
def mmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
def mT(A): return [list(r) for r in zip(*A)]
def mtr(A): return sum(A[i][i] for i in range(len(A)))
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def outer(u, v): return [[a * b for b in v] for a in u]
I4 = [[Fr(int(i == j)) for j in range(4)] for i in range(4)]
ONE = [Fr(1)] * 4
G = [[Fr(int(i == j)) - Fr(1, 5) for j in range(4)] for i in range(4)]        # I - (1/5) 1 1^T
GINV = [[Fr(int(i == j)) + Fr(1) for j in range(4)] for i in range(4)]        # I + 1 1^T
E_LOW = [[Fr(1, 4)] * 4 for _ in range(4)]                                    # (1/4) 1 1^T
E_HIGH = [[I4[i][j] - E_LOW[i][j] for j in range(4)] for i in range(4)]

# ---------------------------------------------------------------- frozen maps
def ell(p): return Fr([0, 1, 2, -2, -1][p])   # balanced section F_5 -> Q
def beta(x): return [ell(x[0]), ell(x[1]), ell(x[2]), ell(x[3])]   # pre-update head, pistons only
def iota_B0(v): return tuple(Fr(c) for c in v)

def matrix_B0_Tw(w):                          # columns: T_w(z^j) = w <z^j, w>_tr in B0
    cols = [kscale(pair_tr(zpow(j), w), w) for j in range(4)]
    return [[cols[j][i] for j in range(4)] for i in range(4)]

ZERO_RECORD = ("ZERO_SUPPORT", Fr(0), (Fr(0), Fr(0)), "ZERO_DENOMINATOR", "ZERO_DENOMINATOR")

def R_cyc(w, low_line=LAMBDA_B):              # direct cyclotomic write; low_line varied only in a control
    if w == ZERO_K: return ZERO_RECORD
    m = pair_tr(w, w)
    c = pair_tr(w, low_line) / pair_tr(low_line, low_line)
    p_low = kscale(c, low_line); p_high = ksub(w, p_low)
    w_low = pair_tr(p_low, p_low); w_high = pair_tr(p_high, p_high)
    dens = tuple(tuple(x / m for x in row) for row in matrix_B0_Tw(w))
    return ("SUPPORTED", m, (w_low, w_high), ("DENSITY", dens), ("MEASURE", (w_low / m, w_high / m)))

def Q_QDD(v):                                 # ordered pair (A_dagger, A_T); dagger = transpose over Q
    return (outer(v, v), outer(v, v))

def F_QDD(qpair, gram=G):                     # factor map on the transpose slot A_T
    _, A_T = qpair
    if all(A_T[i][j] == 0 for i in range(4) for j in range(4)): return ZERO_RECORD
    AG = mmul(A_T, gram); m = mtr(AG)
    w_low = mtr(mmul(E_LOW, AG)); w_high = mtr(mmul(E_HIGH, AG))
    dens = tuple(tuple(x / m for x in row) for row in AG)
    return ("SUPPORTED", m, (w_low, w_high), ("DENSITY", dens), ("MEASURE", (w_low / m, w_high / m)))

# ---------------------------------------------------------------- checks
results = []
def check(idx, name, cond, text):
    results.append(bool(cond))
    print(f"{'PASS' if cond else 'FAIL'} {idx:02d} {name:<8} {text}")

print("TWIST-J QDD Route A reproduction (exact rational arithmetic, all 15625 checkpoints of F_5^6)")
print("K = Q(z), z = zeta_5, B0 = (1, z, z^2, z^3), <x,y>_tr = (1/5) Tr(x sigma_4(y)), G = I - (1/5) 1 1^T")
print("")

# 01 low line
check(1, "LOWLINE", LAMBDA_B == kscale(Fr(-1), zpow(4)) and ktr(LAMBDA_B) == 1 and pair_tr(LAMBDA_B, LAMBDA_B) == Fr(4, 5),
      "lambda_B = 1 + z + z^2 + z^3 = -z^4, Tr(lambda_B) = 1, <lambda_B,lambda_B> = 4/5")
# 02 Gram
gram_ok = all(pair_tr(zpow(i), zpow(j)) == G[i][j] for i in range(4) for j in range(4))
ginv1 = [sum(GINV[i][j] * ONE[j] for j in range(4)) for i in range(4)]
check(2, "GRAM", gram_ok and meq(mmul(G, GINV), I4) and ginv1 == [Fr(5)] * 4,
      "matrix of <.,.>_tr in B0 is G = I - (1/5) 1 1^T; G^-1 = I + 1 1^T; G^-1 1 = 5 1")

# main sweep
X = list(product(range(5), repeat=6))
rec = {}; mism = 0; zeros = 0; supported = 0; norm_fail = 0; sign_fail = 0
fibres = {}; fibre_size = {}
wrong_line = set(); wrong_gram = set(); seen = set()
for x in X:
    v = beta(x); w = iota_B0(v)
    d = R_cyc(w); f = F_QDD(Q_QDD(v))
    rec[x] = d
    if d != f: mism += 1
    if d[0] == "ZERO_SUPPORT":
        zeros += 1
        if d != ZERO_RECORD: norm_fail += 1
    else:
        supported += 1
        m, (wl, wh) = d[1], d[2]
        pl, ph = d[4][1]
        if wl + wh != m or pl + ph != 1: norm_fail += 1
        if wl < 0 or wh < 0 or m <= 0 or pl < 0 or ph < 0: sign_fail += 1
    key = tuple(tuple(r) for r in Q_QDD(v)[1])
    fibres.setdefault(key, set()).add(d); fibre_size[key] = fibre_size.get(key, 0) + 1
    p = tuple(x[:4])
    if p not in seen:
        seen.add(p)
        if w != ZERO_K and R_cyc(w, low_line=zpow(0)) != f: wrong_line.add(p)
        if w != ZERO_K and F_QDD(Q_QDD(v), gram=I4) != d: wrong_gram.add(p)
size_hist = {}
for k, c in fibre_size.items(): size_hist[c] = size_hist.get(c, 0) + 1
distinct_records = len(set(rec.values()))
indep_qr = all(rec[x] == rec[x[:4] + (0, 0)] for x in X)
dep = []
for i in range(4):
    found = False
    for x in X:
        for c in range(5):
            if c != x[i]:
                y = list(x); y[i] = c
                if rec[x] != rec[tuple(y)]: found = True; break
        if found: break
    dep.append(found)

check(3, "TARGET", mism == 0, f"D_direct = F_QDD o Q_QDD o beta field by field on 15625 checkpoints, mismatches {mism}")
check(4, "TOTAL", zeros == 25 and supported == 15600, f"tagged record total: ZERO_SUPPORT heads {zeros}, SUPPORTED heads {supported}, no division on the zero branch")
check(5, "NORM", norm_fail == 0 and sign_fail == 0, f"w_low + w_high = m and p_low + p_high = 1 on all supported heads, nonnegative weights, m > 0; violations {norm_fail + sign_fail}")
check(6, "FIBRES", len(fibres) == 313 and size_hist == {25: 1, 50: 312} and all(len(s) == 1 for s in fibres.values()) and distinct_records == 313,
      f"|QCarrier_QDD| = {len(fibres)}, fibre sizes {dict(sorted(size_hist.items()))}, constant on every fibre, distinct records {distinct_records} (injective)")
check(7, "ALLOW", indep_qr and all(dep), f"record independent of (q, r): {indep_qr}; depends on each piston coordinate: {dep}")
check(8, "NEGLINE", len(wrong_line) == 480, f"control: rational-line reading Q.1 instead of the LOW LINE mismatches on {len(wrong_line)} of 625 pistons")
check(9, "NEGGRAM", len(wrong_gram) == 540, f"control: omitting G in the factor map mismatches on {len(wrong_gram)} of 625 pistons")

# 10 projector pair theorem (QDD-PROJECTOR-PAIR-TR4)
P = [[ONE[i] * ONE[j] / 4 for j in range(4)] for i in range(4)]
proj_ok = (meq(P, E_LOW) and meq(mmul(E_LOW, E_LOW), E_LOW) and meq(mmul(E_HIGH, E_HIGH), E_HIGH)
           and meq([[E_LOW[i][j] + E_HIGH[i][j] for j in range(4)] for i in range(4)], I4)
           and meq(mmul(G, E_LOW), mmul(mT(E_LOW), G)) and meq(mmul(G, E_HIGH), mmul(mT(E_HIGH), G))
           and all(sum(mmul(E_HIGH, [[Fr(c)] for c in v])[i][0] for i in range(4)) == 0 for v in product(range(-2, 3), repeat=4))
           and all(mmul(E_LOW, [[Fr(c)] for c in v]) == [[Fr(0)]] * 4 for v in product(range(-2, 3), repeat=4) if sum(v) == 0))
check(10, "PROJ", proj_ok, "E_low = projector onto span(1) along ker Tr_4, E_high = I - E_low, both G-self-adjoint idempotents, im(E_high) = ker Tr_4, ker(E_low) = ker Tr_4")

# 11 closed forms
cf = True
for v in product(range(-2, 3), repeat=4):
    vv = [Fr(c) for c in v]; s = sum(vv); n2 = sum(c * c for c in vv)
    AG = mmul(outer(vv, vv), G)
    if not (mtr(AG) == n2 - s * s / 5 and mtr(mmul(E_LOW, AG)) == s * s / 20 and mtr(mmul(E_HIGH, AG)) == n2 - s * s / 4): cf = False
check(11, "CLOSED", cf, "m = |v|^2 - s^2/5, w_low = s^2/20, w_high = |v|^2 - s^2/4 on all 625 pistons (s = sum v_i)")

# 12 diagonal boundary of the two slots (QDD-QCARRIER-DIAGONAL-BOUNDARY)
diag = all(meq(Q_QDD([Fr(c) for c in v])[0], Q_QDD([Fr(c) for c in v])[1]) for v in product(range(-2, 3), repeat=4))
check(12, "DIAG", diag, "Q_QDD(v) = (A_dagger, A_T) with A_dagger = A_T = v v^T on all 625 pistons of V_eff (dagger = transpose over Q)")

# 13 cyclotomic pair diagnostic
Gbil = [[pair_bil(zpow(i), zpow(j)) for j in range(4)] for i in range(4)]
herm = {}; pairs = {}
for v in product(range(-2, 3), repeat=4):
    w = iota_B0(v); h = kmul(w, kbar(w)); s2 = kmul(w, w); r = R_cyc(w)
    herm.setdefault(h, set()).add(r); pairs.setdefault((h, s2), set()).add(r)
multi = sum(1 for s in herm.values() if len(s) > 1)
tw_fun = all(len({r[1] for r in s}) == 1 for s in herm.values())
dens_fun = all(len({r[3] for r in s}) == 1 for s in herm.values())
check(13, "SLOTS", (not meq(Gbil, G)) and len(herm) == 90 and len(pairs) == 313 and multi == 80 and tw_fun and not dens_fun,
      f"cyclotomic pair (w sigma_4(w), w^2): {len(herm)} Herm slots, {len(pairs)} pairs, {multi} Herm slots with more than one record; total_weight is a function of the Herm slot ({tw_fun}), density is not ({dens_fun}); bilinear Gram G' differs from G")

# 14 value table of p_low over the 312 nonzero classes
hist = {}; classes = set()
for v in product(range(-2, 3), repeat=4):
    if all(c == 0 for c in v): continue
    key = tuple(tuple(r) for r in outer([Fr(c) for c in v], [Fr(c) for c in v]))
    if key in classes: continue
    classes.add(key); pl = R_cyc(iota_B0(v))[4][1][0]; hist[pl] = hist.get(pl, 0) + 1
check(14, "TABLE", len(classes) == 312 and len(hist) == 22 and hist.get(Fr(0)) == 42 and hist.get(Fr(1)) == 2 and hist.get(Fr(1, 6)) == 12,
      f"p_low over 312 nonzero classes: {len(hist)} distinct values, {hist.get(Fr(0))} classes at 0, {hist.get(Fr(1))} at 1, {hist.get(Fr(1, 6))} at 1/6 (numerical witness only)")
print("       table   " + " ".join(f"{str(k)}:{hist[k]}" for k in sorted(hist)))

# 15 rational zero sum versus the mod-5 hyperplane
sum0 = sum(1 for v in product(range(-2, 3), repeat=4) if sum(v) == 0)
mod0 = sum(1 for v in product(range(-2, 3), repeat=4) if sum(v) % 5 == 0)
check(15, "SUMS", sum0 == 85 and mod0 == 125, f"pistons with rational sum zero {sum0} (p_low = 0), pistons with Tr_4 = 0 in F_5 {mod0}; the first set is a proper subset of the second")

print("")
print(f"RESULT {sum(results)}/{len(results)} {'ALL PASS' if all(results) else 'FAIL'}")
raise SystemExit(0 if all(results) else 1)
