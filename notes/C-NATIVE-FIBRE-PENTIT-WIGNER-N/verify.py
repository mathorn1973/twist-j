#!/usr/bin/env python3
# Verifier: C-NATIVE-FIBRE-PENTIT-WIGNER-N (candidate, NON-CANONICAL, action layer L1 only).
# Frozen together with PREREG-C-NATIVE-FIBRE-PENTIT-WIGNER-N.md before first execution.
# Authority at freeze: Public Canon v97, tag canon-v97, main 738e0421bd15aaea5bb6ef2a56f1cab752d44de5.
# Python standard library only. Exact arithmetic only: integers mod 5, integer cyclotomic
# coefficient vectors, Fractions and exact Q(sqrt5) pairs. No float anywhere.
# Run from the root of mathorn1973/twist-j:
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <this file>
import functools
import hashlib
import importlib.util
import itertools
import sys
from fractions import Fraction as Fr

P = 5
CENSUS_PATH = "reproduce/census/verify.py"
CENSUS_SHA256 = "1df13ba2218acaa9cf48dab2480e6472b107691aac868618dc7f91d511718a5c"

RESULTS = []


def check(cid, text, cond):
    RESULTS.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + cid + " " + text)


def info(text):
    print("     " + text)


# ---------------------------------------------------------------- custody
with open(CENSUS_PATH, "rb") as fh:
    census_bytes = fh.read()
check("0.1", "generator source file matches the pinned SHA-256",
      hashlib.sha256(census_bytes).hexdigest() == CENSUS_SHA256)
spec = importlib.util.spec_from_file_location("census", CENSUS_PATH)
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)
GENS = census.GENS
NAMES = "abcde"
STATES = census.STATES
ZTAB = census.ZTAB
NST = census.N
ENC = census.enc

# ---------------------------------------------------------------- exact helpers


def cyc_norm(c):
    # element sum c_m zeta^m of Z[zeta_5] or Q(zeta_5); unique form with c_4 = 0
    return tuple(c[i] - c[4] for i in range(4))


def cyc_eq_int(c, n):
    return cyc_norm(c) == (n, 0, 0, 0)


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
    # real element -> (x, y) meaning x + y*sqrt5, using zeta+zeta^4 = (-1+sqrt5)/2
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


def q5_cmp(a, b):
    return q5_sign(a[0] - b[0], a[1] - b[1])


def q5_str(v):
    return "(" + str(v[0]) + ") + (" + str(v[1]) + ")*sqrt5"


# monomial operators on C^5: list of (target index, exponent of zeta) per column k
def mono_mul(M, N):
    return [(M[N[k][0]][0], (M[N[k][0]][1] + N[k][1]) % P) for k in range(P)]


def mono_inv(M):
    R = [None] * P
    for k in range(P):
        R[M[k][0]] = (k, (-M[k][1]) % P)
    return R


def mono_trace(M):
    c = [0] * P
    for k in range(P):
        if M[k][0] == k:
            c[M[k][1]] += 1
    return c


IDENT = [(k, 0) for k in range(P)]
PARITY = [((-k) % P, 0) for k in range(P)]


def A(q, r):
    # phase point operator: A_(q,r)|j> = zeta^(2r(q-j)) |2q-j>
    return [((2 * q - j) % P, (2 * r * (q - j)) % P) for j in range(P)]


def D(q, r):
    # Weyl operator: D_(q,r)|k> = tau^(q r) zeta^(r k) |k+q>, tau = zeta^3 so tau^2 = zeta
    return [((k + q) % P, (3 * q * r + r * k) % P) for k in range(P)]


PTS = list(itertools.product(range(P), repeat=2))

# ================================================================ PART A
print("PART A  geometry and representation")


def affine(g):
    c = g((0,) * 6)
    cols = []
    for i in range(6):
        v = g(tuple(1 if k == i else 0 for k in range(6)))
        cols.append(tuple((v[k] - c[k]) % P for k in range(6)))
    L = [[cols[j][i] for j in range(6)] for i in range(6)]
    for x in STATES:
        y = tuple((sum(L[i][j] * x[j] for j in range(6)) + c[i]) % P for i in range(6))
        if y != g(x):
            return None
    return L, c


AFF = {n: affine(g) for n, g in zip(NAMES, GENS)}
check("A1.1", "each of a,b,c,d,e is an affine map on all 15625 states",
      all(AFF[n] is not None for n in NAMES))

FIB = {}
fibre_ok = True
for n, g in zip(NAMES, GENS):
    img = {}
    for x in STATES:
        y = g(x)
        img.setdefault((x[4], x[5]), set()).add((y[4], y[5]))
    fibre_ok &= all(len(v) == 1 for v in img.values())
    FIB[n] = {k: next(iter(v)) for k, v in img.items()}
check("A1.2", "the fibre image (q,r) depends on the fibre only, for every generator", fibre_ok)
CENTRE = {}
refl_ok = all(FIB["a"][u] == u for u in PTS)
for n in "bcde":
    t = FIB[n][(0, 0)]
    refl_ok &= all(FIB[n][u] == ((t[0] - u[0]) % P, (t[1] - u[1]) % P) for u in PTS)
    CENTRE[n] = ((3 * t[0]) % P, (3 * t[1]) % P)
check("A1.3", "a is the identity on the fibre; b,c,d,e are point reflections u -> 2s-u", refl_ok)
info("centres s_b,s_c,s_d,s_e = " + ",".join(str(CENTRE[n]) for n in "bcde"))
check("A1.4", "centres are (0,0),(3,0),(3,3),(1,3) in the order b,c,d,e",
      [CENTRE[n] for n in "bcde"] == [(0, 0), (3, 0), (3, 3), (1, 3)])

# A2: group generated on the fibre
gens_f = [(4, ((2 * CENTRE[n][0]) % P, (2 * CENTRE[n][1]) % P)) for n in "bcde"]


def fcomp(m1, m2):
    # (s1,t1) o (s2,t2): u -> s1*(s2*u+t2)+t1
    return ((m1[0] * m2[0]) % P, ((m1[0] * m2[1][0] + m1[1][0]) % P, (m1[0] * m2[1][1] + m1[1][1]) % P))


group = {(1, (0, 0))}
frontier = [(1, (0, 0))]
while frontier:
    nxt = []
    for m in frontier:
        for g in gens_f:
            h = fcomp(g, m)
            if h not in group:
                group.add(h)
                nxt.append(h)
    frontier = nxt
check("A2.1", "the four reflections generate exactly 50 fibre maps u -> +-u + t",
      len(group) == 50 and {m[0] for m in group} == {1, 4})
check("A2.2", "the generated group contains all 25 translations and all 25 point reflections",
      len({m[1] for m in group if m[0] == 1}) == 25 and len({m[1] for m in group if m[0] == 4}) == 25)

# A3: operator identities over Z[zeta_5]
check("A3.1", "every A_u is a Hermitian involution with entries in mu_5 or zero",
      all(mono_mul(A(*u), A(*u)) == IDENT and mono_inv(A(*u)) == A(*u) for u in PTS))
check("A3.2", "Tr A_u = 1 for all 25 points",
      all(cyc_eq_int(mono_trace(A(*u)), 1) for u in PTS))
check("A3.3", "Tr(A_u A_v) = 5 delta_uv for all 625 ordered pairs",
      all(cyc_eq_int(mono_trace(mono_mul(A(*u), A(*v))), 5 if u == v else 0) for u in PTS for v in PTS))
check("A3.4", "A_s A_u A_s = A_(2s-u) for all 625 ordered pairs",
      all(mono_mul(mono_mul(A(*s), A(*u)), A(*s)) == A((2 * s[0] - u[0]) % P, (2 * s[1] - u[1]) % P)
          for s in PTS for u in PTS))
tot = [[[0] * P for _ in range(P)] for _ in range(P)]
for u in PTS:
    Au = A(*u)
    for k in range(P):
        tot[Au[k][0]][k][Au[k][1]] += 1
check("A3.5", "the 25 operators A_u sum to 5 times the identity",
      all(cyc_eq_int(tot[j][k], 5 if j == k else 0) for j in range(P) for k in range(P)))
check("A3.6", "A_u = D_u Par D_u^(-1) and D_v A_u D_v^(-1) = A_(u+v) for all pairs",
      all(mono_mul(mono_mul(D(*u), PARITY), mono_inv(D(*u))) == A(*u) for u in PTS)
      and all(mono_mul(mono_mul(D(*v), A(*u)), mono_inv(D(*v))) == A((u[0] + v[0]) % P, (u[1] + v[1]) % P)
              for u in PTS for v in PTS))
check("A3.7", "conjugation by A_(s_g) sends A_u to A_(g(u)) for g in b,c,d,e and all 25 u",
      all(mono_mul(mono_mul(A(*CENTRE[n]), A(*u)), A(*CENTRE[n])) == A(*FIB[n][u]) for n in "bcde" for u in PTS))

# A4: invariant alternating forms on F_5^6


def nullspace(M, ncols):
    M = [r[:] for r in M]
    piv = []
    r = 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(M)) if M[i][c] % P), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], P - 2, P)
        M[r] = [(v * inv) % P for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % P:
                f = M[i][c]
                M[i] = [(a - f * b) % P for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    basis = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % P
        basis.append(v)
    return len(piv), basis


PAIRS = [(i, j) for i in range(6) for j in range(i + 1, 6)]


def omega(v):
    O = [[0] * 6 for _ in range(6)]
    for k, (i, j) in enumerate(PAIRS):
        O[i][j] = v[k] % P
        O[j][i] = (-v[k]) % P
    return O


def inv_rows(L, mult):
    out = []
    for (r, s) in PAIRS:
        row = [(L[i][r] * L[j][s] - L[j][r] * L[i][s]) % P for (i, j) in PAIRS]
        k0 = PAIRS.index((r, s))
        row[k0] = (row[k0] - mult) % P
        out.append(row)
    return out


def matmul6(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(6)) % P for j in range(6)] for i in range(6)]


I6 = [[1 if i == j else 0 for j in range(6)] for i in range(6)]
MINUS_I6 = [[(P - 1) if i == j else 0 for j in range(6)] for i in range(6)]
check("A4.1", "linear parts of a,b,c are involutions; linear parts of d,e equal -I",
      all(matmul6(AFF[n][0], AFF[n][0]) == I6 for n in "abc") and all(AFF[n][0] == MINUS_I6 for n in "de"))
dims = {}
max_rank = 0
rank_hist = {}
for mults in itertools.product((1, 2, 3, 4), repeat=3):
    rows = []
    for n, mu in zip("abc", mults):
        rows += inv_rows(AFF[n][0], mu)
    _, basis = nullspace(rows, 15)
    if basis:
        dims[mults] = len(basis)
    for co in itertools.product(range(P), repeat=len(basis)):
        if any(co):
            v = [sum(c * b[k] for c, b in zip(co, basis)) % P for k in range(15)]
            rk = nullspace(omega(v), 6)[0]
            rank_hist[rk] = rank_hist.get(rk, 0) + 1
            max_rank = max(max_rank, rk)
info("nonzero solution spaces by multiplier triple (a,b,c): " + str(sorted(dims.items())))
info("rank histogram over all nonzero solutions: " + str(sorted(rank_hist.items())))
check("A4.2", "over all 64 multiplier triples in (F_5^*)^3 only four triples admit nonzero forms, with dims 3,3,1,1",
      sorted(dims.items()) == [((1, 1, 1), 3), ((1, 4, 4), 1), ((4, 1, 1), 3), ((4, 4, 4), 1)])
check("A4.3", "every nonzero solution has rank exactly 2; no nondegenerate invariant alternating form exists",
      list(rank_hist.keys()) == [2] and max_rank == 2)
rows = []
for n in "abc":
    rows += inv_rows(AFF[n][0], 1)
_, basis111 = nullspace(rows, 15)
# the three displayed forms: dkappa^dq, dkappa^dr, dq^dr with kappa = p1+p4+p1p+p4p
displayed = []
for tgt in (4, 5):
    v = [0] * 15
    for i in range(4):
        v[PAIRS.index((i, tgt))] = 1
    displayed.append(v)
v = [0] * 15
v[PAIRS.index((4, 5))] = 1
displayed.append(v)
span_rank = nullspace([b[:] for b in basis111], 15)[0]
joint_rank = nullspace([b[:] for b in basis111] + [d[:] for d in displayed], 15)[0]
disp_rank = nullspace([d[:] for d in displayed], 15)[0]
check("A4.4", "the strictly invariant forms are exactly span{dkappa^dq, dkappa^dr, dq^dr}",
      span_rank == 3 and disp_rank == 3 and joint_rank == 3)
allrows = []
for b in basis111:
    allrows += omega(b)
_, rad = nullspace(allrows, 6)
rad_ok = len(rad) == 3 and all(sum(w[:4]) % P == 0 and w[4] == 0 and w[5] == 0 for w in rad)
each_rad4 = all(6 - nullspace(omega([sum(c * b[k] for c, b in zip(co, basis111)) % P for k in range(15)]), 6)[0] == 4
                for co in itertools.product(range(P), repeat=3) if any(co))
check("A4.5", "each nonzero invariant form has a 4-dim radical; the common radical is the 3-dim space kappa=q=r=0",
      rad_ok and each_rad4)

# A5: boundary between generators and the selected step
TM = [bin(n).count("1") % 2 for n in range(2048)]
TAB = [[ENC(g(x)) for x in STATES] for g in GENS]
x0 = (0, 0, 0, 0, 0, 0)
x1 = (2, 1, 2, 1, 1, 0)
s0 = (ZTAB[ENC(x0)] + 2 * TM[0]) % P
s1 = (ZTAB[ENC(x1)] + 2 * TM[0]) % P
check("A5.1", "collision: at n=0 the states 000000 and 212110 select a and c and both map to 000000",
      (s0, s1) == (0, 2) and GENS[s0](x0) == x0 and GENS[s1](x1) == x0)
img_sizes = []
for t in (0, 1):
    img_sizes.append(len({TAB[(ZTAB[i] + 2 * t) % P][i] for i in range(NST)}))
info("image sizes of the selected one-step map for driver bit 0 and 1: " + str(img_sizes))
check("A5.2", "the selected one-step map is not injective for either driver bit (images 6250 and 9375)",
      img_sizes == [6250, 9375])
cur = list(range(NST))
for n in range(3):
    cur = [TAB[(ZTAB[i] + 2 * TM[n]) % P][i] for i in cur]
fib_count = {}
for i in cur:
    fib_count[i] = fib_count.get(i, 0) + 1
check("A5.3", "after ticks 0,1,2 all 15625 starts lie on 3125 states, each with exactly 5 preimages",
      len(fib_count) == 3125 and set(fib_count.values()) == {5})
cur = sorted(fib_count)
rule_ok = True
bij_ok = True
used = set()
N_LAST = 1026
RULE = {(0, 0): 4, (1, 1): 3, (0, 1): 1, (1, 0): 1}
for n in range(3, N_LAST + 1):
    sel = {(ZTAB[i] + 2 * TM[n]) % P for i in cur}
    rule_ok &= sel == {RULE[(TM[n - 1], TM[n])]}
    used |= sel
    g = next(iter(sel)) if len(sel) == 1 else 0
    nxt = sorted({TAB[(ZTAB[i] + 2 * TM[n]) % P][i] for i in cur})
    bij_ok &= len(nxt) == len(cur)
    cur = nxt
info("generators used on ticks 3.." + str(N_LAST) + ": " + "".join(sorted(NAMES[s] for s in used)))
check("A5.4", "on ticks 3..1026 all states select one common generator: b if the clock bit changed, d after 11, e after 00",
      rule_ok and used == {1, 3, 4})
check("A5.5", "on ticks 3..1026 the selected step is a bijection of the current 3125-state set", bij_ok)

# ================================================================ PART B
print("PART B  counting and its bounded prohibition")
LINES = []
for dq, dr in [(0, 1)] + [(1, m) for m in range(P)]:
    seen = set()
    for u in PTS:
        L = frozenset(((u[0] + t * dq) % P, (u[1] + t * dr) % P) for t in range(P))
        if L not in seen:
            seen.add(L)
            LINES.append(((dq, dr), L))
check("B1.1", "there are 30 affine lines in 6 parallel classes; every point lies on exactly 6 lines",
      len(LINES) == 30 and all(sum(1 for _, L in LINES if u in L) == 6 for u in PTS))


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
                pr = cyc_mul(X[j][l], Y[l][k])
                for m in range(P):
                    acc[m] += pr[m]
            Z[j][k] = acc
    return Z


def dense_trace_prod(X, Y):
    acc = [0] * P
    for j in range(P):
        for k in range(P):
            pr = cyc_mul(X[j][k], Y[k][j])
            for m in range(P):
                acc[m] += pr[m]
    return acc


PI5 = []   # 5*Pi_L as dense integer cyclotomic matrices
for _, L in LINES:
    X = [[[0] * P for _ in range(P)] for _ in range(P)]
    for u in sorted(L):
        X = dense_add(X, dense_from_mono(A(*u)))
    PI5.append(X)
proj_ok = True
herm_ok = True
tr_ok = True
stab_ok = True
for (dirn, L), X in zip(LINES, PI5):
    X2 = dense_mul(X, X)
    proj_ok &= all(cyc_norm(X2[j][k]) == cyc_norm([5 * t for t in X[j][k]]) for j in range(P) for k in range(P))
    herm_ok &= all(cyc_norm(X[j][k]) == cyc_norm(cyc_conj(X[k][j])) for j in range(P) for k in range(P))
    acc = [0] * P
    for j in range(P):
        for m in range(P):
            acc[m] += X[j][j][m]
    tr_ok &= cyc_eq_int(acc, 5)
    DX = dense_mul(dense_from_mono(D(*dirn)), X)
    found = False
    for e in range(P):
        unit = [1 if m == e else 0 for m in range(P)]
        if all(cyc_norm(DX[j][k]) == cyc_norm(cyc_mul(unit, X[j][k])) for j in range(P) for k in range(P)):
            found = True
    stab_ok &= found
check("B1.2", "each Pi_L = (1/5) sum_(u in L) A_u is a Hermitian idempotent of trace 1 (a rank-one projector)",
      proj_ok and herm_ok and tr_ok)
check("B1.3", "each Pi_L is an eigenprojector of the Weyl operator of its own direction (a stabilizer state)", stab_ok)
inter_ok = True
for (_, L), X in zip(LINES, PI5):
    for (_, M), Y in zip(LINES, PI5):
        inter_ok &= cyc_eq_int(dense_trace_prod(X, Y), 5 * len(L & M))
check("B1.4", "Tr(Pi_L Pi_M) = |L cap M| / 5 for all 900 ordered pairs of lines", inter_ok)


def wigner(w):
    # w integer vector; W(q,r) = (1/(5 |w|^2)) sum_k w_k w_(2q-k) zeta^(2r(q-k)); returns dict point -> (x,y)
    n2 = sum(t * t for t in w)
    W = {}
    for (q, r) in PTS:
        c = [0] * P
        for k in range(P):
            c[(2 * r * (q - k)) % P] += w[k] * w[(2 * q - k) % P]
        x, y = cyc_real_to_q5(c)
        W[(q, r)] = (x / (5 * n2), y / (5 * n2))
    return W


def line_probs(w):
    # p(L) = w^T (5 Pi_L) w / (5 |w|^2), computed from the dense projectors, not from W
    n2 = sum(t * t for t in w)
    out = []
    for X in PI5:
        acc = [0] * P
        for j in range(P):
            if w[j]:
                for k in range(P):
                    if w[k]:
                        f = w[j] * w[k]
                        for m in range(P):
                            acc[m] += f * X[j][k][m]
        x, y = cyc_real_to_q5(acc)
        out.append((x / (5 * n2), y / (5 * n2)))
    return out


def invert_lines(pl):
    mu = {}
    for u in PTS:
        sx = sy = Fr(0)
        for (_, L), pv in zip(LINES, pl):
            if u in L:
                sx += pv[0]
                sy += pv[1]
        mu[u] = ((sx - 1) / 5, sy / 5)
    return mu


def negativity(W):
    sx = sy = Fr(0)
    for (x, y) in W.values():
        if q5_sign(x, y) < 0:
            sx -= x
            sy -= y
    return (sx, sy)


LOW = [4, -1, -1, -1, -1]     # 5*e_0 - (1,1,1,1,1): the LOW direction, coordinate 0 carries no source
W_LOW = wigner(LOW)
mult = {}
for val in W_LOW.values():
    mult[val] = mult.get(val, 0) + 1
low_sorted = sorted(mult.items(), key=functools.cmp_to_key(lambda a, b: q5_cmp(a[0], b[0])))
info("LOW Wigner values with multiplicity: " + "; ".join(q5_str(v) + " x" + str(m) for v, m in low_sorted))
expected_low = {(Fr(1, 5), Fr(0)): 1, (Fr(3, 20), Fr(0)): 4, (Fr(-1, 20), Fr(0)): 4,
                (Fr(1, 40), Fr(1, 40)): 8, (Fr(1, 40), Fr(-1, 40)): 8}
check("B4.1", "LOW Wigner multiset is 1/5 x1, 3/20 x4, -1/20 x4, (1+sqrt5)/40 x8, (1-sqrt5)/40 x8", mult == expected_low)
N_LOW = negativity(W_LOW)
check("B4.2", "LOW negativity is exactly sqrt5/5", N_LOW == (Fr(0), Fr(1, 5)))

ELL = (0, 1, 2, -2, -1)
BOUND = (Fr(0), Fr(1, 20))          # sqrt5/20 = 1/(2 sqrt(d(d-1))) at d = 5
inv_ok = invert_lines(line_probs(LOW)) == W_LOW
row_zero_sum_ok = True
row_zero_neg_ok = True
bound_ok = True
allneg = True
closed_ok = True
overlap_ok = True
table = []
neg_hist = {}
for pvec in itertools.product(range(P), repeat=4):
    if not any(pvec):
        continue
    v = [ELL[t] for t in pvec]
    s = sum(v)
    Q = sum(t * t for t in v)
    w = [-s] + [5 * t - s for t in v]            # 5 * (sum-zero embedding), integers
    W = wigner(w)
    inv_ok &= invert_lines(line_probs(w)) == W
    row = [W[(q, 0)] for q in range(P)]
    row_zero_sum_ok &= (sum(t[0] for t in row), sum(t[1] for t in row)) == (Fr(0), Fr(0))
    row_zero_neg_ok &= any(q5_sign(*t) < 0 for t in row)
    Nv = negativity(W)
    allneg &= q5_sign(*Nv) > 0
    bound_ok &= q5_sign(Nv[0] - BOUND[0], Nv[1] - BOUND[1]) >= 0
    target = Fr(s * s, 4 * (5 * Q - s * s))
    ip = sum(a * b for a, b in zip(LOW, w))
    closed_ok &= Fr(ip * ip, sum(a * a for a in LOW) * sum(b * b for b in w)) == target
    ax = ay = Fr(0)
    for u in PTS:
        (x1, y1), (x2, y2) = W[u], W_LOW[u]
        ax += x1 * x2 + 5 * y1 * y2
        ay += x1 * y2 + x2 * y1
    overlap_ok &= (5 * ax, 5 * ay) == (target, Fr(0))
    table.append(("".join(str(t) for t in pvec), Nv))
    neg_hist[Nv] = neg_hist.get(Nv, 0) + 1
check("B2.1", "inversion mu(u) = (sum_(L through u) p(L) - 1)/5 from the 30 quantum line probabilities returns W exactly, for LOW and all 624 preparations", inv_ok)
check("B3.1", "row r=0 of W sums to zero for all 624 preparations", row_zero_sum_ok)
check("B3.2", "row r=0 of W contains a strictly negative entry for all 624 preparations", row_zero_neg_ok)
check("B3.3", "negativity is at least sqrt5/20 for all 624 preparations", bound_ok)
check("B5.1", "|<l,v~>|^2/|v~|^2 = s^2/(4(5Q-s^2)) by direct inner product for all 624 preparations", closed_ok)
check("B5.2", "the signed phase-space overlap 5 sum_u W_v(u) W_l(u) equals the same value for all 624 preparations", overlap_ok)
check("B6.1", "all 624 preparations have strictly positive negativity", allneg)
hist_sorted = sorted(neg_hist.items(), key=functools.cmp_to_key(lambda a, b: q5_cmp(a[0], b[0])))
nmin, nmax = hist_sorted[0][0], hist_sorted[-1][0]
minimizers = sorted(name for name, Nv in table if Nv == nmin)
info("distinct negativity values: " + str(len(hist_sorted)))
info("minimum " + q5_str(nmin) + " attained by " + str(len(minimizers)) + " preparations; first: " + ",".join(minimizers[:6]))
info("maximum " + q5_str(nmax) + " attained by " + str(hist_sorted[-1][1]) + " preparations")
info("five smallest values with counts: " + "; ".join(q5_str(v) + " x" + str(m) for v, m in hist_sorted[:5]))
check("B6.2", "the minimum over the 624 preparations is (1+sqrt5)/10 and source 1400, v=(1,-1,0,0), attains it",
      nmin == (Fr(1, 10), Fr(1, 10)) and "1400" in minimizers)
blob = "".join(name + " " + str(Nv[0]) + " " + str(Nv[1]) + "\n" for name, Nv in table).encode("ascii")
info("negativity table (624 lines, source x y) sha256 " + hashlib.sha256(blob).hexdigest())

# ================================================================ PART C
print("PART C  applicability")
info("no computation: disposition is fixed by the PREREG contract table, STOP_APPLICABILITY / H_NOT_TESTED unchanged")

print("SUMMARY %d of %d checks PASS" % (sum(RESULTS), len(RESULTS)))
sys.exit(0 if all(RESULTS) else 1)
