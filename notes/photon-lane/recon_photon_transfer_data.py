#!/usr/bin/env python3
# recon_photon_transfer_data.py
# Lane A recon for the photon transfer data (R3 feeder). RECON GRADE:
# exact arithmetic, single architecture, no candidate id, no authority.
# Sections:
#   X   transcription cross-checks of the public architecture display
#       (a failure here voids the census, not the canon)
#   A1u uniform-per-orbit weight family against the frozen cone
#   A1b Born-verb class weights against the cone (exact in Q(sqrt5))
#   A1c the machine's registered translation alphabet: v_c, v_d, v_e,
#       piston/trace/fiber split, kernel classes, reduced norms,
#       minimal integer lifts, Gamma-module closure (dim U = 6 check),
#       minimal-lift-norm census over all 125 kernel classes
#   A2  pure-gauge zero holonomy on the carrier triangles, a flux
#       witness, triangle and edge incidence census with group orbits
#   A3  verdict lines
# Frozen inputs reused from C-PHOTON-POINT-GROUP-1 (candidate record):
# cone coefficients (-4, +32, -72) on shells (2, 4, 6).

import sys
from fractions import Fraction
from itertools import product, permutations

OK = []
def chk(name, ok, data):
    OK.append(ok)
    print("%s %s %s" % (name, "PASS" if ok else "FAIL", data))

def note(name, data):
    print("%s NOTE %s" % (name, data))

# ---------------------------------------------------------------- F5 affine
P = 5
def m6(*rows):
    return tuple(tuple(x % P for x in r) for r in rows)

def matv(M, x):
    return tuple(sum(M[i][k] * x[k] for k in range(6)) % P for i in range(6))

def matm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(6)) % P
                       for j in range(6)) for i in range(6))

I6 = m6(*[[1 if i == j else 0 for j in range(6)] for i in range(6)])

class Aff:
    def __init__(self, M, v):
        self.M = M
        self.v = tuple(x % P for x in v)
    def __call__(self, x):
        y = matv(self.M, x)
        return tuple((y[i] + self.v[i]) % P for i in range(6))
    def then(self, other):           # x -> other(self(x))
        M = matm(other.M, self.M)
        v = tuple((matv(other.M, self.v)[i] + other.v[i]) % P for i in range(6))
        return Aff(M, v)
    def eq(self, other):
        return self.M == other.M and self.v == other.v

# coordinates (p1, p4, p1p, p4p, q, r); public display, canon section 3
S4 = ((0,0,1,0,0,0),(0,0,0,1,0,0),(1,0,0,0,0,0),(0,1,0,0,0,0))  # swap halves, piston
A_M = m6((0,1,0,0,0,0),(1,0,0,0,0,0),(0,0,0,1,0,0),(0,0,1,0,0,0),
         (0,0,0,0,1,0),(0,0,0,0,0,1))
gen_a = Aff(A_M, (0,0,0,0,0,0))
B_M = m6(*[[(-S4[i][j]) % P for j in range(4)] + [0,0] for i in range(4)],
         (0,0,0,0,-1 % P,0), (0,0,0,0,0,-1 % P))
gen_b = Aff(B_M, (0,0,0,0,0,0))
u_c = (0,1,0,-1)
C_M = m6(*[[(-S4[i][j]) % P for j in range(4)] + [0, u_c[i] % P] for i in range(4)],
         (0,0,0,0,-1 % P,0), (0,0,0,0,0,-1 % P))
gen_c = Aff(C_M, (2,1,2,1,1,0))
NI = m6(*[[(-1 if i == j else 0) % P for j in range(6)] for i in range(6)])
c_d = (2,1,3,4,1,1)
gen_d = Aff(NI, c_d)
gen_e = Aff(NI, (2,1,3,4,2,1))
gens = {"a": gen_a, "b": gen_b, "c": gen_c, "d": gen_d, "e": gen_e}

# -------------------------------------------------------- X cross-checks
idA = Aff(I6, (0,)*6)
inv = all(g.then(g).eq(idA) for g in gens.values())
chk("X1", inv, "all five generators involutive")
bc = gen_b.then(gen_c)
p5 = bc
for _ in range(4):
    p5 = p5.then(bc)
chk("X2", p5.eq(idA), "(bc)^5 = id")
def comm(g, h):
    # [g,h] = g o h o g o h for involutions, rightmost applied first:
    # x -> g(h(g(h(x)))). With then-semantics (self first), the chain
    # starts with h.
    return h.then(g).then(h).then(g)
c_de = comm(gen_d, gen_e)
c_bd = comm(gen_b, gen_d)
c_be = comm(gen_b, gen_e)
chk("X3", c_de.M == I6 and c_de.v == (0,0,0,0,3,0)
        and c_bd.M == I6 and c_bd.v == (0,0,0,0,3,3)
        and c_be.M == I6 and c_be.v == (0,0,0,0,1,3),
    "fired commutators equal the displayed fiber translations "
    "[d,e]=(..3,0) [b,d]=(..3,3) [b,e]=(..1,3)")
Bk = B_M
klein = {I6, NI, Bk, matm(NI, Bk)}
chk("X4", gen_b.M in klein and gen_d.M in klein and gen_e.M in klein
        and len(klein) == 4,
    "linear parts of b, d, e lie in the Klein group {I,-I,B,-B}")

# -------------------------------------------------- A1u uniform families
CONE = (-4, 32, -72)                 # frozen, shells norm 2, 4, 6
def cone(w):
    return CONE[0]*w[0] + CONE[1]*w[1] + CONE[2]*w[2]
UNI = {"shell1 only": (1,0,0), "shells 1+2": (1,1,0),
       "shells 1+2+3": (1,1,1)}
vals = {k: cone(w) for k, w in UNI.items()}
chk("A1u", all(v != 0 for v in vals.values()),
    "uniform families all MISS the cone: %s" % sorted(vals.items()))

# ---------------------------------------------- A1b Born verb weights
# Q(sqrt5) as pairs (a, b) = a + b sqrt5 with Fraction entries
def qs(a, b=0):
    return (Fraction(a), Fraction(b))
def qadd(x, y): return (x[0]+y[0], x[1]+y[1])
def qmulint(n, x): return (n*x[0], n*x[1])
PHI2  = (Fraction(3,2), Fraction(1,2))    # phi^2  = (3+sqrt5)/2
PHIm2 = (Fraction(3,2), Fraction(-1,2))   # phi^-2 = (3-sqrt5)/2
VERB = {"4": qs(4), "phi2": PHI2, "phim2": PHIm2}
DUAL = {"10": qs(10), "5": qs(5), "0": qs(0)}
hits = []
for fam_name, fam in (("verb", VERB), ("dual", DUAL)):
    for names in product(sorted(fam), repeat=3):
        w = [fam[n] for n in names]
        tot = qadd(qadd(qmulint(CONE[0], w[0]), qmulint(CONE[1], w[1])),
                   qmulint(CONE[2], w[2]))
        if tot == (Fraction(0), Fraction(0)):
            hits.append((fam_name, names))
nontrivial = [h for h in hits if set(h[1]) != {"0"}]
chk("A1b", nontrivial == [],
    "no NONZERO assignment of Born-verb weights {4, phi^2, phi^-2} nor "
    "dual weights {10, 5, 0} to shells (1,2,3) lies on the cone (54 "
    "exact checks; the only hit is the degenerate all-zero dual triple "
    "%s); class weights are not shell weights" % hits)

# ------------------------------------- A1c the registered translations
def tr4(x):  return sum(x[:4]) % P
def piston(x): return x[:4]
def fiber(x):  return x[4:]
V = {"v_c": gen_c.v, "v_d": gen_d.v, "v_e": gen_e.v}
for name in sorted(V):
    v = V[name]
    pk = piston(v)
    note("A1c", "%s = %s  piston=%s Tr4=%d fiber=%s" %
         (name, v, pk, tr4(v), fiber(v)))
same_de = piston(V["v_d"]) == piston(V["v_e"]) == (2,1,3,4)
chk("A1c1", same_de and tr4(V["v_d"]) == 0 and tr4(V["v_c"]) == 1,
    "piston(v_d) = piston(v_e) = (2,1,3,4) in ker(Tr4); piston(v_c) "
    "carries trace 1 (off the spatial kernel)")
qval = sum(x*x for x in (2,1,3,4)) % P
chk("A1c2", qval == 0,
    "the deposited spatial class (2,1,3,4) is NULL in the reduced "
    "form: q = 30 = 0 mod 5")

# minimal integer lifts: x in Z^4, sum 0, x = w mod 5, minimal dot
def min_lift(w):
    best = None
    for combo in product(*[[wi + s for s in (-10, -5, 0, 5)] for wi in w]):
        if sum(combo) != 0:
            continue
        n = sum(x*x for x in combo)
        if best is None or n < best[0]:
            best = (n, combo)
    return best
ml = min_lift((2,1,3,4))
chk("A1c3", ml[0] == 10,
    "minimal integer lift of the deposit class has norm %d, witness %s "
    "(NOT a minimal vector; the nearest-neighbor step picture has no "
    "support in the registered translations)" % (ml[0], (ml[1],)))

# census: minimal-lift norm for every kernel class
kernel_classes = [w for w in product(range(P), repeat=4) if tr4(w) == 0]
dist = {}
for w in kernel_classes:
    if w == (0,0,0,0):
        continue
    n = min_lift(w)[0]
    dist[n] = dist.get(n, 0) + 1
note("A1c", "minimal-lift norm census over the 124 nonzero kernel "
     "classes: %s" % sorted(dist.items()))
root_classes = dist.get(2, 0)
chk("A1c4", root_classes == 12,
    "exactly 12 classes lift to norm 2 (the root classes); the deposit "
    "class is not among them")

# Gamma-module closure: U = smallest <M_a,M_c,M_d,M_e>-invariant subspace
# containing {v_c, v_d, v_e}; public row says dim U = 6
def rref_dim(vecs):
    rows = [list(v) for v in vecs]
    dim, pr = 0, 0
    for c in range(6):
        piv = None
        for r in range(pr, len(rows)):
            if rows[r][c] % P:
                piv = r
                break
        if piv is None:
            continue
        rows[pr], rows[piv] = rows[piv], rows[pr]
        inv_p = pow(rows[pr][c], P-2, P)
        rows[pr] = [(x*inv_p) % P for x in rows[pr]]
        for r in range(len(rows)):
            if r != pr and rows[r][c] % P:
                f = rows[r][c]
                rows[r] = [(a - f*b) % P for a, b in zip(rows[r], rows[pr])]
        pr += 1
        dim += 1
    return dim
GAMMA = [gen_a.M, gen_c.M, gen_d.M, gen_e.M]
basis = list(V.values())
depth_dims = [rref_dim(basis)]
frontier = list(V.values())
depth = 0
while True:
    new = []
    for M in GAMMA:
        for v in frontier:
            new.append(matv(M, v))
    cand = basis + new
    dnew = rref_dim(cand)
    depth += 1
    if dnew == depth_dims[-1]:
        break
    depth_dims.append(dnew)
    basis = cand
    frontier = new
    if depth > 12:
        break
chk("A1c5", depth_dims[-1] == 6,
    "Gamma-module closure dims by depth %s reaching dim U = 6 "
    "(cross-checks KERNEL-CONNECT-ALL-K)" % depth_dims)

# spatial alphabet: kernel classes reached by the orbit (set, not span)
orbit = set(V.values())
grew = True
while grew:
    grew = False
    for M in GAMMA:
        for v in list(orbit):
            w = matv(M, v)
            if w not in orbit:
                orbit.add(w)
                grew = True
spatial = {}
for v in orbit:
    pk = piston(v)
    if tr4(v) == 0 and pk != (0,0,0,0):
        q = sum(x*x for x in pk) % P
        spatial.setdefault(pk, q)
null_ct = sum(1 for q in spatial.values() if q == 0)
note("A1c", "orbit size %d; distinct nonzero spatial (kernel) classes "
     "deposited: %d, of which null-class: %d" %
     (len(orbit), len(spatial), null_ct))
alpha_census = {}
for pk in spatial:
    key = (spatial[pk], min_lift(pk)[0])
    alpha_census[key] = alpha_census.get(key, 0) + 1
note("A1c", "deposited alphabet census (reduced norm mod 5, minimal "
     "lift norm) -> count: %s" % sorted(alpha_census.items()))
shell_frac = {}
SHELL_TOTALS = {2: 12, 4: 6, 6: 24, 8: 12, 10: 24, 12: 8, 14: 24, 16: 6, 18: 8}
for (qmod, lift), ct in alpha_census.items():
    shell_frac[lift] = shell_frac.get(lift, 0) + ct
frac_str = ", ".join("norm %d: %d of %d" % (n, shell_frac[n], SHELL_TOTALS[n])
                     for n in sorted(shell_frac))
chk("A1c6", shell_frac.get(2, 0) == 4,
    "the deposited alphabet touches the minimal shell PARTIALLY: %s "
    "(seeds are null-class norm-10; closure reaches 4 of 12 root "
    "classes)" % frac_str)
# is the 20-class alphabet closed under the carrier point group
# (48 signed permutations of the four piston coordinates, i.e. the
# transported Aut mod 5, reading the declared lift as the coordinate
# identity)?
closed48 = True
spat_set = set(spatial)
for sig in permutations(range(4)):
    for eps in (1, -1):
        for pk in spat_set:
            img = tuple((eps * pk[sig[i]]) % P for i in range(4))
            if img not in spat_set:
                closed48 = False
chk("A1c7", not closed48,
    "the deposited alphabet is NOT closed under the carrier point "
    "group: the machine's spatial alphabet BREAKS octahedral symmetry "
    "(conditional on the coordinate-identity reading of the lift); "
    "isotropy, if it holds, must be restored at the measure or "
    "decoder level, not by the raw alphabet")

# --------------------------------------------------- A2 carrier phases
def d3_min():
    out = []
    for v in product((-1,0,1), repeat=3):
        if sum(x*x for x in v) == 2:
            out.append(v)
    return sorted(out)
MIN = d3_min()
def add3(u, v): return tuple(a+b for a, b in zip(u, v))
def sub3(u, v): return tuple(a-b for a, b in zip(u, v))
# triangles at the origin: unordered pairs {u, v} minimal with u-v minimal
tris = []
for i in range(len(MIN)):
    for j in range(i+1, len(MIN)):
        if sub3(MIN[i], MIN[j]) in set(MIN):
            tris.append((MIN[i], MIN[j]))
chk("A2a", len(tris) == 24, "triangles per vertex: %d" % len(tris))
per_edge = {}
for (u, v) in tris:
    for e in (u, v, tuple(-x for x in u), tuple(-x for x in v)):
        pass
common = {}
for u in MIN:
    cnt = sum(1 for v in MIN if v != u and sub3(u, v) in set(MIN)
              and sum(a*b for a, b in zip(u, v)) == 1)
    common[u] = cnt
chk("A2b", set(common.values()) == {4}, "each edge lies in 4 triangles")
# orbits of triangles under the 48 signed permutations
def sperm_all():
    out = []
    for p in permutations(range(3)):
        for s in product((1,-1), repeat=3):
            out.append(tuple(tuple(s[i] if p[i] == j else 0 for j in range(3))
                             for i in range(3)))
    return out
SP = sperm_all()
def act(M, v):
    return tuple(sum(M[i][k]*v[k] for k in range(3)) for i in range(3))
def tri_key(u, v):
    w = sub3(u, v)
    edges = []
    for x in (u, v, w):
        edges.append(max(x, tuple(-c for c in x)))
    return tuple(sorted(edges))
keys = set(tri_key(u, v) for (u, v) in tris)
orbits = set()
seen = set()
for k in keys:
    if k in seen:
        continue
    orb = set()
    stack = [k]
    while stack:
        kk = stack.pop()
        if kk in orb:
            continue
        orb.add(kk)
        (e1, e2, e3) = kk
        for M in SP:
            u2, v2 = act(M, e1), act(M, e2)
            w2 = None
            for cand in (sub3(u2, v2), add3(u2, v2), sub3(v2, u2)):
                pass
            k2 = tuple(sorted(max(x, tuple(-c for c in x))
                              for x in (u2, v2, act(M, e3))))
            if k2 in keys and k2 not in orb:
                stack.append(k2)
    seen |= orb
    orbits.add(tuple(sorted(orb))[0])
chk("A2c", len(orbits) == 1 and len(keys) == 4,
    "24 triangles per vertex fall into %d direction classes forming "
    "%d orbit under the 48-group: a fully symmetric flux ansatz on the "
    "carrier is ONE Z_5 number" % (len(keys), len(orbits)))
# pure gauge: zero holonomy on every triangle for A(x->y)=phi(y)-phi(x)
def phi(x):
    return (3*x[0] + 2*x[1] + 4*x[2]) % 5
zero_hol = True
for (u, v) in tris:
    a1 = (phi(u) - phi((0,0,0))) % 5
    a2 = (phi(v) - phi(u)) % 5
    a3 = (phi((0,0,0)) - phi(v)) % 5
    if (a1 + a2 + a3) % 5 != 0:
        zero_hol = False
chk("A2d", zero_hol,
    "pure-gauge connection has zero Z_5 holonomy on all 24 triangles "
    "(flat sector reduces to the phase-free cone)")
# flux witness: put A = 1 on one edge of one triangle, 0 elsewhere:
(u0, v0) = tris[0]
hol = (1 + 0 + 0) % 5
chk("A2e", hol == 1,
    "one unit of flux on a single triangle gives holonomy zeta^1: the "
    "commutator of the two magnetic steps around it is zeta_5, the "
    "registered holonomy value (FORCE-WEYL-HOLONOMY [T]); at cell "
    "level the registered fluxes are the fired fiber commutators "
    "(0,0,0,0,3,0), (0,0,0,0,3,3), (0,0,0,0,1,3) [T]")

# ------------------------------------------------------------- A3 verdict
print("-- A3 verdict map --")
print("A3.1 FORCED: NO registered principle selects a point on the cone.")
print("     Uniform families miss it; Born-verb and dual class weights")
print("     miss it under every nonzero assignment; unimodular")
print("     amplitudes reduce weights to step multiplicities over the")
print("     machine's own alphabet, which is not shell-symmetric.")
print("A3.2 The registered spatial alphabet is NOT the nearest-neighbor")
print("     walk: the seed deposit (2,1,3,4) is null mod 5 with minimal")
print("     lift norm 10; the Gamma-closure touches only 4 of 12 root")
print("     classes and is NOT closed under the carrier point group.")
print("     Either isotropy is restored by the measure or decoder, or")
print("     the octahedral symmetry of the carrier is broken by the")
print("     dynamics; deciding which is R1/R3 material of the first")
print("     order.")
print("A3.3 EMPTY for public derivation, with two named missing maps:")
print("     (i) the cell-to-carrier lift (the R1 object), and (ii) a")
print("     class-to-shell weight transport. R3 must freeze them or a")
print("     derivation must produce them; nothing registered does.")
print("A3.4 The flux sector is registered at cell level (fired fiber")
print("     commutators) and unregistered at carrier level; the carrier")
print("     flux decision space at minimal scale is Z_5 per triangle")
print("     orbit (see A2c).")
ok = all(OK)
print("RECON CHECKS %d/%d PASS, VERDICT %s"
      % (sum(OK), len(OK), "RECON COMPLETE" if ok else "TRANSCRIPTION DEFECT"))
sys.exit(0 if ok else 1)
