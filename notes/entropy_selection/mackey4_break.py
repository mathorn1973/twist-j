#!/usr/bin/env python3
# mackey4_break.py
#
# Independent breaker for candidate C-ENTROPY-MACKEY-OBSTRUCTION-4-N.
# Preregistration: PREREG-BREAKER-MACKEY4-1_2026-07-30.md
#   sha256 d02badef96706f4c1e3f88edf1430e4641e2276245873b875e56f399fafc8a51
# Session: M2 breaker session, Cowork claude-fable-5, 2026-07-30.
#
# INDEPENDENCE: this file was authored without reading mackey4_verify.py,
# mackey4_primary.stdout.txt, or MACKEY4-PRIMARY-RUN.md, and imports nothing
# from the recon branch. Source route: integer multiplication matrix plus
# Smith normal form (not lambda-digit arithmetic). Target route: rebuilt from
# the public canon v28 generator table only.
#
# Exact arithmetic only: int and Fraction. No float anywhere. Stdlib only.
# Deterministic: fixed encodings, sorted iteration, no set-order dependence
# in any printed line.

from fractions import Fraction
from math import gcd

FAILURES = []
GATES = 0

def gate(name, ok, detail):
    global GATES
    GATES += 1
    status = "PASS" if ok else "FAIL"
    print("%s %s  %s" % (name, status, detail))
    if not ok:
        FAILURES.append(name)

print("mackey4_break.py  independent breaker for C-ENTROPY-MACKEY-OBSTRUCTION-4-N")
print("public basis: Public Canon v28, tag canon-v28,")
print("  content 86a046007f89a64a696d013112a44f02e624dd2e")
print("prereg: PREREG-BREAKER-MACKEY4-1 sha256 d02badef96706f4c1e3f88edf1430e4641e2276245873b875e56f399fafc8a51")
print("platform note: ONE platform run; candidate grade at best; r >= 2 scoping")
print("  is attached to every 629 statement below.")
print("")

# ----------------------------------------------------------------------
# PART T. Target reconstruction from the public generator table.
# State: (p1, p4, p1p, p4p, q, r), all coordinates in F_5.
# Encoding: index = ((((p1*5+p4)*5+p1p)*5+p4p)*5+q)*5+r  (lexicographic).
# ----------------------------------------------------------------------

N = 5 ** 6  # 15625

def enc(t):
    x = 0
    for v in t:
        x = x * 5 + (v % 5)
    return x

def dec(x):
    out = []
    for _ in range(6):
        out.append(x % 5)
        x //= 5
    out.reverse()
    return tuple(out)

STATES = [dec(i) for i in range(N)]

def g_a(t):
    p1, p4, p1p, p4p, q, r = t
    return (p4, p1, p4p, p1p, q, r)

def g_b(t):
    p1, p4, p1p, p4p, q, r = t
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5, (-q) % 5, (-r) % 5)

def g_c(t):
    p1, p4, p1p, p4p, q, r = t
    # piston -> b4(piston) + s_c + r*u_c ; q -> 1-q ; r -> -r
    # b4(p1,p4,p1p,p4p) = (-p1p,-p4p,-p1,-p4); s_c=(2,1,2,1); u_c=(0,1,0,-1)
    return ((-p1p + 2) % 5, (-p4p + 1 + r) % 5, (-p1 + 2) % 5,
            (-p4 + 1 - r) % 5, (1 - q) % 5, (-r) % 5)

def g_d(t):
    p1, p4, p1p, p4p, q, r = t
    # x -> c_d - x, c_d = (2,1,3,4,1,1)
    return ((2 - p1) % 5, (1 - p4) % 5, (3 - p1p) % 5, (4 - p4p) % 5,
            (1 - q) % 5, (1 - r) % 5)

def g_e(t):
    p1, p4, p1p, p4p, q, r = t
    # x -> (c_d + v_e) - x, v_e = (0,0,0,0,1,0)
    return ((2 - p1) % 5, (1 - p4) % 5, (3 - p1p) % 5, (4 - p4p) % 5,
            (2 - q) % 5, (1 - r) % 5)

GENFUN = [g_a, g_b, g_c, g_d, g_e]
GENNAME = ["a", "b", "c", "d", "e"]

# Precompute generator permutations and z6.
GEN = []
for f in GENFUN:
    GEN.append([enc(f(STATES[i])) for i in range(N)])
Z6 = [sum(STATES[i]) % 5 for i in range(N)]

# B01 involutions
ok = True
for gi in range(5):
    P = GEN[gi]
    for x in range(N):
        if P[P[x]] != x:
            ok = False
            break
    if not ok:
        break
gate("B01", ok, "all five generators are involutions on all 15625 states")

# B02 (bc)^5 = id, both composition orders
Pbc = [GEN[1][GEN[2][x]] for x in range(N)]
Pcb = [GEN[2][GEN[1][x]] for x in range(N)]
def apply_k(P, k):
    Q = list(range(N))
    for _ in range(k):
        Q = [P[x] for x in Q]
    return Q
ok = apply_k(Pbc, 5) == list(range(N)) and apply_k(Pcb, 5) == list(range(N))
gate("B02", ok, "(bc)^5 = id and (cb)^5 = id on all 15625 states")

# B03 canon step formula equals M_J columns (source-side kernel identity).
# Multiplication in Z[z]/Phi_5, basis (1, z, z^2, z^3), z^4 = -(1+z+z^2+z^3).
def poly_mul(u, v):
    # u, v: 4-coefficient lists over Z. Multiply, reduce by z^4 = -(1+z+z^2+z^3).
    raw = [0] * 7
    for i in range(4):
        for j in range(4):
            raw[i + j] += u[i] * v[j]
    # reduce degrees 6,5,4
    for deg in (6, 5, 4):
        c = raw[deg]
        if c:
            raw[deg] = 0
            for k in range(deg - 4, deg):
                raw[k] -= c
    return raw[:4]

J_COEF = [1, 0, 1, 0]  # 1 + z^2
BASIS = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
MJ = [[0] * 4 for _ in range(4)]
for j in range(4):
    col = poly_mul(J_COEF, BASIS[j])
    for i in range(4):
        MJ[i][j] = col[i]

def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(4)) for i in range(4)]

def step_formula(v):
    a_, b_, c_, d_ = v
    return [a_ - c_ + d_, b_ - c_, a_, b_ - c_ + d_]

ok = True
testvecs = BASIS + [[1, 2, 3, 4], [2, 0, 4, 1], [3, 3, 1, 0]]
for v in testvecs:
    if mat_vec(MJ, v) != step_formula(v):
        ok = False
gate("B03", ok, "M_J columns reproduce the canon step (a,b,c,d)->(a-c+d,b-c,a,b-c+d)")

# B04 z6 transformation laws
ok = True
for x in range(N):
    z = Z6[x]
    if Z6[GEN[0][x]] != z: ok = False; break
    if Z6[GEN[1][x]] != (-z) % 5: ok = False; break
    if Z6[GEN[2][x]] != (2 - z) % 5: ok = False; break
    if Z6[GEN[3][x]] != (2 - z) % 5: ok = False; break
    if Z6[GEN[4][x]] != (3 - z) % 5: ok = False; break
gate("B04", ok, "z6 laws: a fixes, b negates, c and d give 2-z, e gives 3-z")

# Branch maps F_t(x) = g_{(z6+2t) mod 5}(x)
F = []
for t in (0, 1):
    Ft = [GEN[(Z6[x] + 2 * t) % 5][x] for x in range(N)]
    F.append(Ft)

# B05 certified recurrent core via image iteration plus closure certificate
def tm_bit(n):
    return bin(n).count("1") & 1

Y = set(range(N))
sizes = []
H0_candidates = []
H1_candidates = []
STEPS = 1000
for k in range(STEPS):
    t = tm_bit(k)
    Y = {F[t][x] for x in Y}
    sizes.append(len(Y))
    if k >= STEPS - 40:
        if t == 0:
            H0_candidates.append(frozenset(Y))
        else:
            H1_candidates.append(frozenset(Y))

stable = all(s == 3125 for s in sizes[-40:])
same0 = len(set(H0_candidates)) == 1 and len(H0_candidates) > 0
same1 = len(set(H1_candidates)) == 1 and len(H1_candidates) > 0
H0 = set(H0_candidates[-1]) if H0_candidates else set()
H1 = set(H1_candidates[-1]) if H1_candidates else set()

def image(Ft, S):
    return {Ft[x] for x in S}

closure = (image(F[0], H0) == H0 and image(F[0], H1) == H0 and
           image(F[1], H0) == H1 and image(F[1], H1) == H1)
gate("B05", stable and same0 and same1 and closure,
     "image sizes stabilize at 3125; late images depend only on the last bit; "
     "closure certificate F_t(H_s) = H_t holds for all four (s,t), bijectively")

R = H0 | H1
ok = (len(R) == 6250 and len(H0) == 3125 and len(H1) == 3125 and
      len(H0 & H1) == 0 and
      all(Z6[x] == 4 for x in H0) and all(Z6[x] == 1 for x in H1))
gate("B06", ok, "|R| = 6250 = 3125 + 3125, disjoint halves, H0 on sheet 4, H1 on sheet 1")

# fired selector values on R
fired = set()
for x in sorted(R):
    for t in (0, 1):
        fired.add((Z6[x] + 2 * t) % 5)
gate("B07", fired == {1, 3, 4},
     "selector on R fires only {1,3,4}, that is b, d, e; a and c stay silent")

# B08 mirror law
ok = (all(F[0][F[0][x]] == x for x in H0) and
      all(F[1][F[1][x]] == x for x in H1) and
      all(F[0][F[1][x]] == x for x in H0) and
      all(F[1][F[0][x]] == x for x in H1))
gate("B08", ok, "mirror law: own-half involutions, cross restrictions mutually inverse")

# B09 components by union-find on branch edges
parent = {}
def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root
def union(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        if rx > ry:
            rx, ry = ry, rx
        parent[ry] = rx

for x in R:
    parent[x] = x
for x in sorted(R):
    union(x, F[0][x])
    union(x, F[1][x])

comp_of = {}
for x in sorted(R):
    comp_of[x] = find(x)
comp_members = {}
for x in sorted(R):
    comp_members.setdefault(comp_of[x], []).append(x)
comps = sorted(comp_members.keys())
size_census = {}
for c in comps:
    size_census[len(comp_members[c])] = size_census.get(len(comp_members[c]), 0) + 1
ok = (len(comps) == 313 and size_census == {20: 312, 10: 1})
gate("B09", ok, "313 components: sizes census %s (expect 312 x 20, 1 x 10)"
     % str(sorted(size_census.items())))

singlet = None
generic = []
for c in comps:
    if len(comp_members[c]) == 10:
        singlet = c
    else:
        generic.append(c)

# ----------------------------------------------------------------------
# Dihedral machinery.  Element (e, k) means s^e r^k, apply r^k first.
# Multiplication: s^e1 r^k1 * s^e2 r^k2 =
#   e2 = 0 : (e1, k1 + k2)
#   e2 = 1 : (e1 + 1, k2 - k1)
# ----------------------------------------------------------------------

def dmul(g1, g2):
    e1, k1 = g1
    e2, k2 = g2
    if e2 == 0:
        return ((e1 + e2) % 2, (k1 + k2) % 5)
    return ((e1 + e2) % 2, (k2 - k1) % 5)

D5_ALL = [(e, k) for e in (0, 1) for k in range(5)]
SUBGROUPS = [("D5", D5_ALL),
             ("C5", [(0, k) for k in range(5)])]
for j in range(5):
    SUBGROUPS.append(("C2_ref%d" % j, [(0, 0), (1, j)]))
SUBGROUPS.append(("trivial", [(0, 0)]))

def compose_local(p, q, n):
    # apply q first, then p
    return tuple(p[q[i]] for i in range(n))

def build_half_data(members, half, F_own_t, F_cross_from, F_cross_back, F_other_t):
    """Return (ok, detail, data) for one component half.
    half: sorted list of states in this half.
    own mirror  s  = F[F_own_t] restricted to half
    pullback    s' = F[F_cross_back] o F[F_other_t] o F[F_cross_from]
    """
    n = len(half)
    idx = {x: i for i, x in enumerate(half)}
    s_l = []
    sp_l = []
    for x in half:
        y = F[F_own_t][x]
        if y not in idx:
            return (False, "own mirror leaves the half", None)
        s_l.append(idx[y])
        y2 = F[F_cross_back][F[F_other_t][F[F_cross_from][x]]]
        if y2 not in idx:
            return (False, "pullback mirror leaves the half", None)
        sp_l.append(idx[y2])
    s_l = tuple(s_l)
    sp_l = tuple(sp_l)
    ident = tuple(range(n))
    if compose_local(s_l, s_l, n) != ident or compose_local(sp_l, sp_l, n) != ident:
        return (False, "marked generators are not involutions", None)
    r_l = compose_local(s_l, sp_l, n)  # s o s'
    # order of r
    q = r_l
    order = 1
    while q != ident:
        q = compose_local(r_l, q, n)
        order += 1
        if order > 10:
            return (False, "rotation order exceeds 10", None)
    # group elements
    perms = {}
    rk = ident
    for k in range(5):
        perms[(0, k)] = rk
        perms[(1, k)] = compose_local(s_l, rk, n)
        rk = compose_local(r_l, rk, n)
    distinct = len(set(perms.values()))
    return (True, "", {"n": n, "idx": idx, "half": half, "s": s_l, "sp": sp_l,
                       "r": r_l, "order_r": order, "perms": perms,
                       "distinct": distinct})

# B10 generic H0 halves: regular dihedral order 10, isomorphism gate included
ok_all = True
detail = ""
comp_data0 = {}
for c in generic:
    half0 = sorted(x for x in comp_members[c] if x in H0)
    if len(half0) != 10:
        ok_all = False; detail = "half size != 10"; break
    okc, why, data = build_half_data(comp_members[c], half0, 0, 1, 0, 1)
    if not okc:
        ok_all = False; detail = why; break
    if data["order_r"] != 5 or data["distinct"] != 10:
        ok_all = False; detail = "not dihedral of order 10 (ord r = %d, distinct = %d)" % (data["order_r"], data["distinct"]); break
    # regularity: orbit of basepoint hits all, and freeness
    seen = set()
    free = True
    for g in D5_ALL:
        p = data["perms"][g]
        seen.add(p[0])
        if g != (0, 0) and any(p[i] == i for i in range(10)):
            free = False
    if len(seen) != 10 or not free:
        ok_all = False; detail = "action not regular/free"; break
    # multiplication table isomorphism gate: dmul matches composition
    for g1 in D5_ALL:
        for g2 in D5_ALL:
            if compose_local(data["perms"][g1], data["perms"][g2], 10) != data["perms"][dmul(g1, g2)]:
                ok_all = False; detail = "dihedral multiplication mismatch"; break
        if not ok_all:
            break
    if not ok_all:
        break
    # coordinates: point -> group element with g(basepoint 0) = point
    coord = {}
    for g in D5_ALL:
        coord[data["perms"][g][0]] = g
    data["coord"] = coord
    comp_data0[c] = data
gate("B10", ok_all and len(comp_data0) == 312,
     "all 312 generic H0 halves carry a free regular dihedral group of order 10, "
     "ord(s s') = 5, multiplication table verified" + ("" if ok_all else "  [" + detail + "]"))

# B11 the same on the H1 side
ok_all1 = True
comp_data1 = {}
for c in generic:
    half1 = sorted(x for x in comp_members[c] if x in H1)
    okc, why, data = build_half_data(comp_members[c], half1, 1, 0, 1, 0)
    if not okc or data["order_r"] != 5 or data["distinct"] != 10:
        ok_all1 = False
        break
    coord = {}
    for g in D5_ALL:
        coord[data["perms"][g][0]] = g
    data["coord"] = coord
    comp_data1[c] = data
gate("B11", ok_all1 and len(comp_data1) == 312,
     "H1-side symmetric gate: all 312 generic H1 halves regular dihedral order 10")

# B12 singlet: D5/C2 with five distinct reflection stabilizers
shalf0 = sorted(x for x in comp_members[singlet] if x in H0)
shalf1 = sorted(x for x in comp_members[singlet] if x in H1)
oks, whys, sdata = build_half_data(comp_members[singlet], shalf0, 0, 1, 0, 1)
singlet_ok = oks and len(shalf0) == 5 and len(shalf1) == 5
stab_ks = []
if singlet_ok:
    singlet_ok = (sdata["order_r"] == 5 and sdata["distinct"] == 10)
if singlet_ok:
    # transitivity and stabilizers
    orb = {sdata["perms"][g][0] for g in D5_ALL}
    singlet_ok = (len(orb) == 5)
    for p in range(5):
        stab = [g for g in D5_ALL if sdata["perms"][g][p] == p]
        if len(stab) != 2 or (0, 0) not in stab:
            singlet_ok = False
            break
        refl = [g for g in stab if g != (0, 0)][0]
        if refl[0] != 1:
            singlet_ok = False
            break
        stab_ks.append(refl[1])
    if singlet_ok and len(set(stab_ks)) != 5:
        singlet_ok = False
gate("B12", singlet_ok,
     "singlet half: transitive order-10 dihedral action on 5 points, five distinct "
     "reflection stabilizers k = %s (the five reflection axes)" % str(sorted(stab_ks)))

# B13 common cocycle gate: transported coordinates, all four edge maps are the
# frozen translations on every generic component; singlet compatible at coset level.
S_ELT = (1, 0)          # s
SP_ELT = dmul(S_ELT, (0, 1))  # s r = s'
cocycle_ok = True
for c in generic:
    d0 = comp_data0[c]
    half0 = d0["half"]
    # transported H1 coordinates: c-image of basepoint chain
    coord1t = {}
    for p_local in range(10):
        g = d0["coord"][p_local]
        y = F[1][half0[p_local]]
        coord1t[y] = g
    if len(coord1t) != 10:
        cocycle_ok = False
        break
    for p_local in range(10):
        x = half0[p_local]
        gx = d0["coord"][p_local]
        # edge (0,0): F0 on H0 must be left multiplication by s
        y = F[0][x]
        if d0["coord"][d0["idx"][y]] != dmul(S_ELT, gx):
            cocycle_ok = False
            break
        # edge (0,1): F1 cross must be id in transported coordinates
        if coord1t[F[1][x]] != gx:
            cocycle_ok = False
            break
    if not cocycle_ok:
        break
    for y, gy in sorted(coord1t.items()):
        # edge (1,1): F1 on H1 must be left multiplication by s'
        if coord1t[F[1][y]] != dmul(SP_ELT, gy):
            cocycle_ok = False
            break
        # edge (1,0): F0 cross back must be id
        if d0["coord"][d0["idx"][F[0][y]]] != gy:
            cocycle_ok = False
            break
    if not cocycle_ok:
        break
# singlet at coset level
if cocycle_ok and singlet_ok:
    cosets = {}
    for p in range(5):
        cosets[p] = frozenset(g for g in D5_ALL if sdata["perms"][g][0] == p)
    # normalize: coset of point = set of g with g(base)=point; edges act by left mult
    sidx = {x: i for i, x in enumerate(shalf0)}
    coord1t_s = {}
    for p in range(5):
        coord1t_s[F[1][shalf0[p]]] = cosets[p]
    for p in range(5):
        x = shalf0[p]
        cx = cosets[p]
        y = F[0][x]
        if frozenset(dmul(S_ELT, g) for g in cx) != cosets[sidx[y]]:
            cocycle_ok = False
            break
        if coord1t_s[F[1][x]] != cx:
            cocycle_ok = False
            break
    if cocycle_ok:
        for y, cy in sorted(coord1t_s.items()):
            if frozenset(dmul(SP_ELT, g) for g in cy) != coord1t_s[F[1][y]]:
                cocycle_ok = False
                break
            if cosets[sidx[F[0][y]]] != cy:
                cocycle_ok = False
                break
labels_summary = "(0,0)->s, (0,1)->id, (1,0)->id, (1,1)->s r; s and s r distinct reflections, <s, s r> = D5"
gate("B13", cocycle_ok,
     "common cocycle: one frozen reconstruction gives identical edge labels on all "
     "312 components and the singlet cosets: " + labels_summary)

# B14 Mackey menu by direct union-find on the H0 target half (3125 states)
target0 = []
state_pos = {}
for c in generic:
    d0 = comp_data0[c]
    for p_local in range(10):
        state_pos[(c, p_local)] = len(target0)
        target0.append((c, p_local))
for p in range(5):
    state_pos[(singlet, p)] = len(target0)
    target0.append((singlet, p))
assert len(target0) == 3125

def menu_counts(side_data, singlet_perms):
    counts = {}
    for name, M in SUBGROUPS:
        par = list(range(3125))
        def f2(a):
            root = a
            while par[root] != root:
                root = par[root]
            while par[a] != root:
                par[a], a = root, par[a]
            return root
        def u2(a, b):
            ra, rb = f2(a), f2(b)
            if ra != rb:
                if ra > rb:
                    ra, rb = rb, ra
                par[rb] = ra
        for pos, (c, p_local) in enumerate(target0):
            if c == singlet:
                for m in M:
                    q = singlet_perms[m][p_local]
                    u2(pos, state_pos[(c, q)])
            else:
                g = side_data[c]["coord"][p_local]
                for m in M:
                    g2 = dmul(m, g)
                    q = side_data[c]["perms"][g2][0]
                    u2(pos, state_pos[(c, q)])
        roots = set()
        for a in range(3125):
            roots.add(f2(a))
        counts[name] = len(roots)
    return counts

counts0 = menu_counts(comp_data0, sdata["perms"])
expected_menu = {"D5": 313, "C5": 625, "trivial": 3125}
for j in range(5):
    expected_menu["C2_ref%d" % j] = 1563
ok = counts0 == expected_menu
gate("B14", ok, "menu on the H0 target half: %s" % str(sorted(counts0.items())))

# B15 the same menu on the H1 side (symmetric control)
oks1, whys1, sdata1 = build_half_data(comp_members[singlet], shalf1, 1, 0, 1, 0)
ok = oks1
counts1 = {}
if ok:
    counts1 = menu_counts(comp_data1, sdata1["perms"])
    ok = counts1 == expected_menu
gate("B15", ok, "menu on the H1 target half: %s" % str(sorted(counts1.items())))

MENU = sorted(set(counts0.values()))

# ----------------------------------------------------------------------
# PART S. Source reconstruction: Smith normal form route.
# ----------------------------------------------------------------------

def mat_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def mat_mul(A, B):
    n = len(A)
    m = len(B[0])
    k2 = len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k2)) for j in range(m)] for i in range(n)]

def det4(M):
    # Laplace along first row, exact ints, n <= 4
    n = len(M)
    if n == 1:
        return M[0][0]
    total = 0
    for j in range(n):
        minor = [[M[i][jj] for jj in range(n) if jj != j] for i in range(1, n)]
        total += ((-1) ** j) * M[0][j] * det4(minor)
    return total

def smith(Ain):
    n = len(Ain)
    A = [row[:] for row in Ain]
    U = mat_identity(n)
    V = mat_identity(n)
    for t in range(n):
        while True:
            piv = None
            best = None
            for i in range(t, n):
                for j in range(t, n):
                    if A[i][j] != 0 and (best is None or abs(A[i][j]) < best):
                        best = abs(A[i][j])
                        piv = (i, j)
            if piv is None:
                break
            pi, pj = piv
            if pi != t:
                A[pi], A[t] = A[t], A[pi]
                U[pi], U[t] = U[t], U[pi]
            if pj != t:
                for row in A:
                    row[pj], row[t] = row[t], row[pj]
                for row in V:
                    row[pj], row[t] = row[t], row[pj]
            clean = True
            for i in range(t + 1, n):
                if A[i][t] != 0:
                    qq = A[i][t] // A[t][t]
                    if qq:
                        for j in range(n):
                            A[i][j] -= qq * A[t][j]
                            U[i][j] -= qq * U[t][j]
                    if A[i][t] != 0:
                        clean = False
            for j in range(t + 1, n):
                if A[t][j] != 0:
                    qq = A[t][j] // A[t][t]
                    if qq:
                        for i in range(n):
                            A[i][j] -= qq * A[i][t]
                            V[i][j] -= qq * V[i][t]
                    if A[t][j] != 0:
                        clean = False
            if not clean:
                continue
            # divisibility fix: pivot must divide every remaining entry
            bad = None
            for i in range(t + 1, n):
                for j in range(t + 1, n):
                    if A[i][j] % A[t][t] != 0:
                        bad = (i, j)
                        break
                if bad:
                    break
            if bad is None:
                break
            bi, bj = bad
            for i in range(n):
                A[i][t] += A[i][bj]
                V[i][t] += V[i][bj]
    for t in range(n):
        if A[t][t] < 0:
            for j in range(n):
                A[t][j] = -A[t][j]
                U[t][j] = -U[t][j]
    return U, A, V

# lambda^5 ideal matrix
lam = [1, -1, 0, 0]
lam5 = [1, 0, 0, 0]
for _ in range(5):
    lam5 = poly_mul(lam5, lam)
A_ideal = [[0] * 4 for _ in range(4)]
for j in range(4):
    col = poly_mul(lam5, BASIS[j])
    for i in range(4):
        A_ideal[i][j] = col[i]

U_s, D_s, V_s = smith(A_ideal)
UAV = mat_mul(mat_mul(U_s, A_ideal), V_s)
diag = [D_s[i][i] for i in range(4)]
detU = det4(U_s)
detV = det4(V_s)
ok = (UAV == D_s and abs(detU) == 1 and abs(detV) == 1 and
      all(D_s[i][j] == 0 for i in range(4) for j in range(4) if i != j) and
      all(diag[i] > 0 for i in range(4)) and
      all(diag[i + 1] % diag[i] == 0 for i in range(3)) and
      diag == [5, 5, 5, 25] and
      abs(det4(A_ideal)) == 3125)
gate("B16", ok, "SNF of the lambda^5 ideal lattice: U A V = D, U and V unimodular, "
     "invariant factors %s, |det A| = %d; additive type Z/25 + (Z/5)^3"
     % (str(diag), abs(det4(A_ideal))))

# integer inverse of U via adjugate
def mat_inverse_unimodular(M):
    n = len(M)
    d = det4(M)
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [[M[r][c] for c in range(n) if c != j] for r in range(n) if r != i]
            adj[j][i] = ((-1) ** (i + j)) * det4(minor)
    return [[adj[i][j] * d for j in range(n)] for i in range(n)]  # d in {1,-1}

U_inv = mat_inverse_unimodular(U_s)
ok = mat_mul(U_s, U_inv) == mat_identity(4)
W = mat_mul(mat_mul(U_s, MJ), U_inv)
# well-definedness of W mod diag
ok2 = all((W[i][j] * diag[j]) % diag[i] == 0 for i in range(4) for j in range(4))
gate("B17", ok and ok2, "U inverse is integer and W = U M_J U^-1 acts well-defined "
     "on the quotient coordinates mod %s" % str(diag))

# enumerate quotient, build J permutation
radix = diag  # (5,5,5,25)
Q_SIZE = 1
for d in radix:
    Q_SIZE *= d
assert Q_SIZE == 3125

def q_enc(cv):
    x = 0
    for i in range(4):
        x = x * radix[i] + cv[i]
    return x

def q_dec(x):
    out = [0] * 4
    for i in range(3, -1, -1):
        out[i] = x % radix[i]
        x //= radix[i]
    return out

JPERM = [0] * Q_SIZE
for x in range(Q_SIZE):
    cv = q_dec(x)
    img = [sum(W[i][j] * cv[j] for j in range(4)) % radix[i] for i in range(4)]
    JPERM[x] = q_enc(img)

# permutation check and cycle type
seen = [False] * Q_SIZE
cycle_census = {}
fixed_classes = []
visited_count = 0
for x in range(Q_SIZE):
    if not seen[x]:
        length = 0
        y = x
        while not seen[y]:
            seen[y] = True
            y = JPERM[y]
            length += 1
        cycle_census[length] = cycle_census.get(length, 0) + 1
        if length == 1:
            fixed_classes.append(x)
        visited_count += length
perm_ok = (visited_count == Q_SIZE and len(set(JPERM)) == Q_SIZE)
ok = (perm_ok and cycle_census == {1: 1, 4: 1, 20: 156} and fixed_classes == [0])
lcm = 1
for L in sorted(cycle_census):
    lcm = lcm * L // gcd(lcm, L)
gate("B18", ok and lcm == 20,
     "J cycle type on O/lambda^5: %s, unique fixed class 0, permutation order %d"
     % (str(sorted(cycle_census.items())), lcm))

# B19 dyadic product law by direct orbit count
ok = True
for m in (1, 4, 20):
    for r_lvl in range(0, 9):
        two = 2 ** r_lvl
        total = m * two
        seenp = [False] * total
        orbits = 0
        for start in range(total):
            if not seenp[start]:
                orbits += 1
                i, j = start // two, start % two
                while not seenp[i * two + j]:
                    seenp[i * two + j] = True
                    i = (i + 1) % m
                    j = (j + 1) % two
        if orbits != gcd(m, two):
            ok = False
gate("B19", ok, "product component law verified by direct orbit count: "
     "components(C_m x Z/2^r) = gcd(m, 2^r) for m in {1,4,20}, r = 0..8")

# B20 c_src table from the measured cycle type
cyc_list = []
for L in sorted(cycle_census):
    cyc_list += [L] * cycle_census[L]
def c_src(r_lvl):
    two = 2 ** r_lvl
    return sum(gcd(m, two) for m in cyc_list)
table = [(r_lvl, c_src(r_lvl)) for r_lvl in range(0, 9)]
v2max = max((m & -m).bit_length() - 1 for m in cyc_list)
ok = (c_src(0) == 158 and c_src(1) == 315 and
      all(c_src(r_lvl) == 629 for r_lvl in range(2, 9)) and v2max == 2)
gate("B20", ok, "c_src table %s; stabilization exactly from r = max v_2 = %d; "
     "c_src(r) = 629 holds for r >= 2 ONLY" % (str(table), v2max))

# B21 the obstruction and the mixed control
in_menu = 629 in MENU
sols = [(a_, b_) for a_ in (1, 2, 5, 10) for b_ in (1, 3, 5) if 312 * a_ + b_ == 629]
ok = (not in_menu) and MENU == [313, 625, 1563, 3125] and sols == [(2, 5)]
gate("B21", ok, "629 not in menu %s; mixed control 312a + b = 629 has unique "
     "solution %s = (C5 on generic blocks, trivial on singlet), unavailable to "
     "one common Mackey range" % (str(MENU), str(sols)))

# B22 embedding arithmetic and Haar finite shadow
frac_ok = (Fraction(1, 2) * Fraction(1, 3125) == Fraction(1, 6250))
# translation transitivity on the quotient group: translation by u maps 0 to u
trans_ok = True
for x in range(Q_SIZE):
    cv = q_dec(x)
    img = [(0 + cv[i]) % radix[i] for i in range(4)]
    if q_enc(img) != x:
        trans_ok = False
        break
gate("B22", frac_ok and trans_ok,
     "exact embedding arithmetic (1/2)(1/3125) = 1/6250; additive translations act "
     "transitively on the 3125 quotient classes (finite shadow of the Haar lemma)")

# Diagnostic, non-falsifying by the frozen prereg: independent-basepoint
# cross-edge census over the 312 generic components.
census = {}
for c in generic:
    d0 = comp_data0[c]
    d1 = comp_data1[c]
    x0 = d0["half"][0]
    y = F[1][x0]
    gam = d1["coord"][d1["idx"][y]]
    census[gam] = census.get(gam, 0) + 1
census_items = sorted(census.items())
print("")
print("DIAGNOSTIC (non-falsifying, convention-dependent): independent-basepoint")
print("cross-edge census over 312 generic components: %s" % str(census_items))
print("count multiset %s; primary reported {155, 157} under its own conventions"
      % str(sorted(census.values())))

print("")
if FAILURES:
    print("RESULT: BREAKER %d/%d PASS; FIRED GATES: %s" % (GATES - len(FAILURES), GATES, ",".join(FAILURES)))
    print("DECISION: DISAGREEMENT OR DEFECT; first-class; both sides preserved; STOP")
else:
    print("RESULT: BREAKER %d/%d ALL PASS" % (GATES, GATES))
    print("DECISION: independent route AGREES with the primary on every load-bearing")
    print("value: source additive type, cycle type 1^1 4^1 20^156, c_src = 629 at")
    print("r >= 2, target 312 regular D5 torsors plus D5/C2 singlet, common cocycle,")
    print("menu {313, 625, 1563, 3125}, 629 not in menu, mixed control (2,5).")
    print("SCOPE: fixed depth five, fiberwise bijective, r >= 2 subclass only.")
    print("This is not A_A = empty; ENTROPY-LAYER-BRIDGE [O] stays open; one")
    print("platform; candidate grade; promotion needs the public probe protocol.")
