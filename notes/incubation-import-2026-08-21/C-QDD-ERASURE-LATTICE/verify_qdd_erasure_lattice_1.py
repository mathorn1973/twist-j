#!/usr/bin/env python3
# C-QDD-ERASURE-LATTICE-1 verifier. Candidate lane, no authority.
# Exact arithmetic only: int and Fraction. No float in any assertion.
# Python standard library only. Zero arguments. Deterministic stdout.
# Fixed gate order, no fail-fast.

from fractions import Fraction as F
import sys

PASS = []
FAIL = []

def gate(name, ok, note=""):
    tag = "PASS" if ok else "FAIL"
    (PASS if ok else FAIL).append(name)
    print("%s %s%s" % (name, tag, (" " + note) if note else ""))

# ---------- exact linear algebra ----------

def mat(rows):
    return tuple(tuple(F(x) for x in r) for r in rows)

def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(m))
                       for j in range(p)) for i in range(n))

def madd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def msub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def smul(c, A):
    c = F(c)
    return tuple(tuple(c * A[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def mT(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))

def eye(n):
    return tuple(tuple(F(1) if i == j else F(0) for j in range(n))
                 for i in range(n))

def zeros(n, m):
    return tuple(tuple(F(0) for _ in range(m)) for _ in range(n))

def minv(A):
    n = len(A)
    M = [list(A[i]) + [F(1) if i == j else F(0) for j in range(n)]
         for i in range(n)]
    for col in range(n):
        piv = None
        for r in range(col, n):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            raise ValueError("singular")
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return tuple(tuple(row[n:]) for row in M)

def rank_rows(rows):
    R = [list(r) for r in rows]
    n = len(R)
    if n == 0:
        return 0
    m = len(R[0])
    rank = 0
    row = 0
    for col in range(m):
        piv = None
        for r in range(row, n):
            if R[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        R[row], R[piv] = R[piv], R[row]
        pv = R[row][col]
        R[row] = [x / pv for x in R[row]]
        for r in range(n):
            if r != row and R[r][col] != 0:
                f = R[r][col]
                R[r] = [a - f * b for a, b in zip(R[r], R[row])]
        row += 1
        rank += 1
        if row == n:
            break
    return rank

def flat(A):
    return tuple(A[i][j] for i in range(len(A)) for j in range(len(A[0])))

def vec_is_zero(v):
    return all(x == 0 for x in v)

# nullity of the joint linear system on a 4x4 unknown A:
#   [A, m] = 0 for every m in comms;  A*l = 0 for every l in lann;
#   l*A = 0 for every l in rann
def law_space_nullity(comms, lann=(), rann=()):
    rows = []
    E = [[zeros(4, 4) for _ in range(4)] for _ in range(4)]
    basis = []
    for i in range(4):
        for j in range(4):
            B = [[F(0)] * 4 for _ in range(4)]
            B[i][j] = F(1)
            basis.append(mat(B))
    for m in comms:
        cols = [flat(msub(mmul(b, m), mmul(m, b))) for b in basis]
        for eq in range(16):
            rows.append(tuple(cols[v][eq] for v in range(16)))
    for l in lann:
        cols = [flat(mmul(b, l)) for b in basis]
        for eq in range(16):
            rows.append(tuple(cols[v][eq] for v in range(16)))
    for l in rann:
        cols = [flat(mmul(l, b)) for b in basis]
        for eq in range(16):
            rows.append(tuple(cols[v][eq] for v in range(16)))
    return 16 - rank_rows(rows)

def in_law_space(A, comms, lann=(), rann=()):
    for m in comms:
        if mmul(A, m) != mmul(m, A):
            return False
    for l in lann:
        if mmul(A, l) != zeros(4, 4):
            return False
    for l in rann:
        if mmul(l, A) != zeros(4, 4):
            return False
    return True

def independent(mats):
    return rank_rows([flat(m) for m in mats]) == len(mats)

# ---------- permutations of F_5 ----------

def pcomp(p, q):  # apply q then p
    return tuple(p[q[x]] for x in range(5))

def pinv(p):
    r = [0] * 5
    for x in range(5):
        r[p[x]] = x
    return tuple(r)

PID = (0, 1, 2, 3, 4)

def all_perms():
    out = []
    def rec(pref, rest):
        if not rest:
            out.append(tuple(pref))
            return
        for i, x in enumerate(rest):
            rec(pref + [x], rest[:i] + rest[i + 1:])
    rec([], [0, 1, 2, 3, 4])
    return sorted(out)

def closure(gens):
    S = set(gens)
    S.add(PID)
    frontier = list(S)
    while frontier:
        new = []
        cur = list(S)
        for a in frontier:
            for b in cur:
                c = pcomp(a, b)
                if c not in S:
                    S.add(c)
                    new.append(c)
                d = pcomp(b, a)
                if d not in S:
                    S.add(d)
                    new.append(d)
        frontier = new
    return frozenset(S)

# ---------- build the frozen objects ----------

MJ = mat([[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]])
I4 = eye(4)
D = msub(MJ, I4)
ONE = tuple(F(1) for _ in range(4))
G = msub(I4, smul(F(1, 5), mat([[1] * 4] * 4)))
GINV = minv(G)

def sharp(X):
    return mmul(GINV, mmul(mT(X), G))

def col(v):
    return tuple((x,) for x in v)

def apply(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(4)) for i in range(4))

e0 = (F(1), F(0), F(0), F(0))
U = [e0]
for _ in range(4):
    U.append(apply(D, U[-1]))
# u_0..u_4; B has columns u_0..u_3
B = tuple(tuple(U[j][i] for j in range(4)) for i in range(4))
BINV = minv(B)

def rho(p):
    cols = []
    for x in range(4):
        t = p[x]
        if t < 4:
            c = [F(0)] * 4
            c[t] = F(1)
        else:
            c = [F(-1)] * 4
        cols.append(c)
    Mp = tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
    return mmul(B, mmul(Mp, BINV))

PERMS = all_perms()
RHO = {p: rho(p) for p in PERMS}

def gram(x, y):
    gy = apply(G, y)
    return sum(x[i] * gy[i] for i in range(4))

# ---------- G01 motor ----------

D2 = mmul(D, D)
D3 = mmul(D2, D)
D4 = mmul(D3, D)
D5 = mmul(D4, D)
phi5 = madd(madd(I4, D), madd(D2, madd(D3, D4)))
gate("G01a-D5-identity", D5 == I4)
gate("G01b-Phi5(D)=0", phi5 == zeros(4, 4))
gate("G01c-motor-powers-independent", independent([I4, D, D2, D3]))

# ---------- G02 simplex ----------

sumu = tuple(U[0][i] + U[1][i] + U[2][i] + U[3][i] + U[4][i] for i in range(4))
gate("G02a-vertex-sum-zero", vec_is_zero(sumu))
gram_ok = True
for x in range(5):
    for y in range(5):
        want = F(4, 5) if x == y else F(-1, 5)
        if gram(U[x], U[y]) != want:
            gram_ok = False
gate("G02b-gram-table", gram_ok)
gate("G02c-u2-is-minus-one", U[2] == tuple(F(-1) for _ in range(4)))

# ---------- G03 representation ----------

distinct = len(set(RHO.values())) == 120
gate("G03a-faithful-120", distinct)
orth_ok = all(mmul(mT(RHO[p]), mmul(G, RHO[p])) == G for p in PERMS)
gate("G03b-G-orthogonal-all-120", orth_ok)
act_ok = True
for p in PERMS:
    Rp = RHO[p]
    for x in range(5):
        if apply(Rp, U[x]) != U[p[x]]:
            act_ok = False
gate("G03c-vertex-action-600", act_ok)
hom_ok = True
for p in PERMS:
    Rp = RHO[p]
    for q in PERMS:
        if mmul(Rp, RHO[q]) != RHO[pcomp(p, q)]:
            hom_ok = False
            break
    if not hom_ok:
        break
gate("G03d-homomorphism-14400", hom_ok)
cyc = (1, 2, 3, 4, 0)  # x -> x+1
gate("G03e-motor-is-rho(01234)", RHO[cyc] == D)

# ---------- G04 token, stabilizer, projectors ----------

K = 2
Sk = sorted([p for p in PERMS if p[K] == K])
gate("G04a-stabilizer-order-24", len(Sk) == 24)
Pk = zeros(4, 4)
for p in Sk:
    Pk = madd(Pk, RHO[p])
Pk = smul(F(1, 24), Pk)
Qk = msub(I4, Pk)
gate("G04b-Pk-projector", mmul(Pk, Pk) == Pk and sharp(Pk) == Pk)
gate("G04c-ranks", rank_rows(list(Pk)) == 1 and rank_rows(list(Qk)) == 3)
gate("G04d-Pk-image-is-uk-line", apply(Pk, U[K]) == U[K])

# ---------- G05 architecture residual H_k ----------

def mult_perm(a, k):
    return tuple((k + a * (x - k)) % 5 for x in range(5))

Hk = sorted([mult_perm(a, K) for a in (1, 2, 3, 4)])
gate("G05a-Hk-order-4", len(set(Hk)) == 4)
gperm = mult_perm(2, K)
pw = PID
orders_ok = True
seen = []
for i in range(1, 5):
    pw = pcomp(gperm, pw)
    seen.append(pw)
gate("G05b-Hk-cyclic-gen-order-4", pw == PID and len(set(seen)) == 4
     and set(seen) == set(Hk))
agl = closure([cyc, mult_perm(2, 0)])
gate("G05c-AGL-order-20", len(agl) == 20)
gate("G05d-Hk-equals-AGL-cap-Sk", set(Hk) == set(p for p in agl if p[K] == K))

# ---------- G06 lattice completeness ----------

HkSet = frozenset(Hk)
SkSet = frozenset(Sk)
order8 = set()
counts = {8: 0, 24: 0, "other": 0}
for s in Sk:
    if s in HkSet:
        continue
    cl = closure(list(Hk) + [s])
    if len(cl) == 8:
        counts[8] += 1
        order8.add(cl)
    elif len(cl) == 24:
        counts[24] += 1
    else:
        counts["other"] += 1
gate("G06a-closures-over-Hk", counts["other"] == 0 and counts[8] == 4
     and counts[24] == 16,
     "orders {8:%d, 24:%d, other:%d}" % (counts[8], counts[24], counts["other"]))
gate("G06b-unique-D4", len(order8) == 1)
Dk = sorted(next(iter(order8))) if len(order8) == 1 else []
DkSet = frozenset(Dk)
up_ok = True
for s in Sk:
    if s in DkSet:
        continue
    if len(closure(list(Dk) + [s])) != 24:
        up_ok = False
gate("G06c-closures-over-Dk-all-S4", up_ok)

# ---------- G07 dihedral certificate ----------

refl = [s for s in Dk if s not in HkSet]
dihe = (len(refl) == 4
        and all(pcomp(s, s) == PID for s in refl)
        and all(pcomp(s, pcomp(gperm, pinv(s))) == pinv(gperm) for s in refl))
gate("G07-Dk-dihedral-relations", dihe)

# ---------- G08 sharp calculus and R, C, J ----------

g = RHO[gperm]
Rk = smul(F(1, 4), madd(msub(I4, g), msub(mmul(g, g), mmul(g, mmul(g, g)))))
Ck = msub(Qk, Rk)
Jk = mmul(g, Ck)
tab = {
    "R2=R": mmul(Rk, Rk) == Rk,
    "C2=C": mmul(Ck, Ck) == Ck,
    "RC=0": mmul(Rk, Ck) == zeros(4, 4),
    "CR=0": mmul(Ck, Rk) == zeros(4, 4),
    "RJ=0": mmul(Rk, Jk) == zeros(4, 4),
    "JR=0": mmul(Jk, Rk) == zeros(4, 4),
    "CJ=J": mmul(Ck, Jk) == Jk,
    "JC=J": mmul(Jk, Ck) == Jk,
    "J2=-C": mmul(Jk, Jk) == smul(-1, Ck),
    "R#=R": sharp(Rk) == Rk,
    "C#=C": sharp(Ck) == Ck,
    "J#=-J": sharp(Jk) == smul(-1, Jk),
    "R+C=Q": madd(Rk, Ck) == Qk,
    "RC J indep": independent([Rk, Ck, Jk]),
}
gate("G08-product-table", all(tab.values()),
     "" if all(tab.values()) else str([k for k, v in tab.items() if not v]))

# Consequence, written proof shape: for T = e R + r C + s J,
#   T# T = e^2 R + (r^2 + s^2) C
# by bilinearity and the table above; with R, C independent and
# R + C = Q, the effect equation T# T = Q is exactly e^2 = 1 and
# r^2 + s^2 = 1. Over Q, x^2 = 1 iff x = 1 or x = -1.

def Tlaw(e, r, s):
    return madd(smul(e, Rk), madd(smul(r, Ck), smul(s, Jk)))

def admitted(T):
    return (mmul(T, Pk) == zeros(4, 4) and mmul(Pk, T) == zeros(4, 4)
            and mmul(sharp(T), T) == Qk)

# ---------- G09 centralizer dimensions ----------

Hmats = [RHO[p] for p in Hk]
Dmats = [RHO[p] for p in Dk]
Smats = [RHO[p] for p in Sk]
nH = law_space_nullity(Hmats, lann=[Pk], rann=[Pk])
nD = law_space_nullity(Dmats, lann=[Pk], rann=[Pk])
nS = law_space_nullity(Smats, lann=[Pk], rann=[Pk])
gate("G09a-dims-3-2-1", (nH, nD, nS) == (3, 2, 1), "got (%d,%d,%d)" % (nH, nD, nS))
gate("G09b-H-basis-RCJ", independent([Rk, Ck, Jk])
     and all(in_law_space(X, Hmats, [Pk], [Pk]) for X in (Rk, Ck, Jk)))
gate("G09c-D-basis-RC", independent([Rk, Ck])
     and all(in_law_space(X, Dmats, [Pk], [Pk]) for X in (Rk, Ck))
     and not in_law_space(Jk, Dmats, [Pk], [Pk]))
gate("G09d-S-basis-Q", in_law_space(Qk, Smats, [Pk], [Pk]))

# ---------- G10 H rung: rational circle, nonselection ----------

wits = [(F(1), F(1), F(0)), (F(1), F(-1), F(0)), (F(1), F(3, 5), F(4, 5)),
        (F(1), F(0), F(1)), (F(1), F(-3, 5), F(4, 5))]
circle_ok = all(e * e == 1 and r * r + s * s == 1 for (e, r, s) in wits)
Ts = [Tlaw(*w) for w in wits]
adm_ok = all(admitted(T) for T in Ts)
dist = True
for i in range(len(Ts)):
    for j in range(i + 1, len(Ts)):
        if Ts[i] == Ts[j] or Ts[i] == smul(-1, Ts[j]):
            dist = False
gate("G10a-H-circle-witnesses-admitted", circle_ok and adm_ok)
gate("G10b-five-distinct-physical-classes", dist)
inj_ok = True
for t in (F(0), F(1), F(1, 2), F(1, 3), F(2, 3)):
    r = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    if r * r + s * s != 1 or not admitted(Tlaw(F(1), r, s)):
        inj_ok = False
    if 1 + r != 0 and s / (1 + r) != t:
        inj_ok = False
gate("G10c-injective-rational-family", inj_ok)

# ---------- G11 D rung: exactly two physical classes ----------

# On span{R, C}: T = r R + c C, T# T = r^2 R + c^2 C = Q iff r^2 = c^2 = 1.
members = []
for r in (F(1), F(-1)):
    for c in (F(1), F(-1)):
        T = madd(smul(r, Rk), smul(c, Ck))
        members.append(T)
memb_ok = all(admitted(T) and in_law_space(T, Dmats, [Pk], [Pk])
              for T in members)
gate("G11a-D-four-members-admitted-covariant", memb_ok)
Tstar = msub(Rk, Ck)
classes = []
for T in members:
    if not any(T == X or T == smul(-1, X) for X in classes):
        classes.append(T)
gate("G11b-exactly-two-classes", len(classes) == 2
     and Tstar != Qk and Tstar != smul(-1, Qk))
# nonterminality witness: first and second conditioned rays differ
w = apply(Qk, U[0])
wR = apply(Rk, w)
wC = apply(Ck, w)
Tw = apply(Tstar, w)
TTw = apply(Tstar, Tw)
ray_move = rank_rows([w, Tw]) == 2
gate("G11c-Rk-Ck-components-nonzero", not vec_is_zero(wR)
     and not vec_is_zero(wC))
gate("G11d-nonterminal-witness", mmul(Tstar, Tstar) == Qk and TTw == w
     and ray_move)

# ---------- G12 S rung: unique class, Lueders ----------

lam_ok = (admitted(Qk) and admitted(smul(-1, Qk))
          and mmul(Qk, Qk) == Qk
          and mmul(smul(-1, Qk), smul(-1, Qk)) != smul(-1, Qk))
gate("G12-S-unique-class-idempotent-plusQ", lam_ok)

# ---------- G13 motor rung: EMPTY ----------

nM = law_space_nullity([D])
gate("G13a-motor-commutant-dim-4", nM == 4)
gate("G13b-motor-commutant-basis", independent([I4, D, D2, D3])
     and all(in_law_space(X, [D]) for X in (I4, D, D2, D3)))
nM0 = law_space_nullity([D], lann=[Pk])
gate("G13c-motor-with-record-anchor-zero", nM0 == 0)
# hence no admitted law commutes with the motor: T = 0 fails T# T = Q_k != 0
gate("G13d-Qk-nonzero", Qk != zeros(4, 4))
big = {
    "C5": [cyc],
    "AGL": [cyc, mult_perm(2, 0)],
    "A5": [cyc, (1, 2, 0, 3, 4)],
    "S5": [cyc, (1, 0, 2, 3, 4)],
}
big_ok = True
for name in sorted(big):
    gens = [RHO[p] for p in big[name]] + [D]
    if law_space_nullity(gens, lann=[Pk]) != 0:
        big_ok = False
gate("G13e-transitive-witnesses-empty", big_ok)

# ---------- G14 transport across tokens ----------

trans_ok = True
dims_ok = True
for kk in range(5):
    Skk = frozenset(p for p in PERMS if p[kk] == kk)
    Hkk = frozenset(mult_perm(a, kk) for a in (1, 2, 3, 4))
    o8 = set()
    for s in sorted(Skk - Hkk):
        cl = closure(sorted(Hkk) + [s])
        if len(cl) == 8:
            o8.add(cl)
    if len(o8) != 1:
        trans_ok = False
        continue
    Dkk = next(iter(o8))
    nxt = (kk + 1) % 5
    conjS = frozenset(pcomp(cyc, pcomp(p, pinv(cyc))) for p in Skk)
    conjH = frozenset(pcomp(cyc, pcomp(p, pinv(cyc))) for p in Hkk)
    conjD = frozenset(pcomp(cyc, pcomp(p, pinv(cyc))) for p in Dkk)
    Snxt = frozenset(p for p in PERMS if p[nxt] == nxt)
    Hnxt = frozenset(mult_perm(a, nxt) for a in (1, 2, 3, 4))
    o8n = set()
    for s in sorted(Snxt - Hnxt):
        cl = closure(sorted(Hnxt) + [s])
        if len(cl) == 8:
            o8n.add(cl)
    Dnxt = next(iter(o8n)) if len(o8n) == 1 else None
    if not (conjS == Snxt and conjH == Hnxt and conjD == Dnxt):
        trans_ok = False
    Pkk = zeros(4, 4)
    for p in sorted(Skk):
        Pkk = madd(Pkk, RHO[p])
    Pkk = smul(F(1, 24), Pkk)
    Pn = zeros(4, 4)
    for p in sorted(Snxt):
        Pn = madd(Pn, RHO[p])
    Pn = smul(F(1, 24), Pn)
    if mmul(D, mmul(Pkk, minv(D))) != Pn:
        trans_ok = False
    dH = law_space_nullity([RHO[p] for p in sorted(Hkk)], [Pkk], [Pkk])
    dD = law_space_nullity([RHO[p] for p in sorted(Dkk)], [Pkk], [Pkk])
    dS = law_space_nullity([RHO[p] for p in sorted(Skk)], [Pkk], [Pkk])
    if (dH, dD, dS) != (3, 2, 1):
        dims_ok = False
gate("G14a-motor-transports-ladder", trans_ok)
gate("G14b-dims-3-2-1-all-tokens", dims_ok)

# ---------- G15 target comparison, LAST ----------

Elow = smul(F(1, 4), mat([[1] * 4] * 4))
Ehigh = msub(I4, Elow)
gate("G15-target-last-P2-Elow-Q2-Ehigh", Pk == Elow and Qk == Ehigh)

# ---------- G16 firewalls ----------

print("G16 FIREWALLS: candidate labels only; O1 and O2 remain open; L4")
print("  apparatus/support only, no L5/L6 lift; SAMPLING NOT PROVIDED is")
print("  untouched; apparatus records are not public D_clock records; the")
print("  lattice quantifies only over subgroups containing H_k; premises")
print("  discarding the architecture residual are out of scope; the")
print("  naturality-versus-normalizer axis is separate and sealed; the")
print("  registered post-state equivalence T ~ -T is used unchanged.")
gate("G16-firewalls-printed", True)

# ---------- decision ----------

print("gates: %d PASS, %d FAIL" % (len(PASS), len(FAIL)))
if not FAIL:
    print("E1 LATTICE: {H_k, D_k, S_k} complete, D_k unique dihedral order 8")
    print("E2 CENTRALIZERS: dims 3, 2, 1 with bases {R,C,J}, {R,C}, {Q}")
    print("E3 CLASSES: H rung rational circle (nonselection, injective")
    print("   family); D rung exactly two physical classes [Q] and [R-C];")
    print("   S rung exactly one physical class [Q], idempotence selects +Q")
    print("E4 MOTOR: commutant Q[D], no admitted law; EMPTY for every")
    print("   subgroup of S_5 containing the motor cycle")
    print("E5 TRANSPORT: the motor conjugates the complete ladder token to")
    print("   token; dims 3-2-1 at all five tokens")
    print("DECISION: ERASURE-LADDER")
    sys.exit(0)
else:
    print("DECISION: FIRED (see FAIL gates)")
    sys.exit(2)
