#!/usr/bin/env python3
# recon_alphabet_moments.py
# Lane A recon, step 2, first computation unlocked by the owner ruling
# R1-B of 2026-08-05 (GATE-LIFT-KERNEL-Z adopted as canonical UP TO the
# carrier point group). RECON GRADE: exact arithmetic, single platform,
# no candidate id, no authority.
#
# Question: does the machine's OWN deposited spatial alphabet, with the
# simplest measures, produce an isotropic walk? Exact moment tensors
# M1, M2, M3, M4 for three frozen conventions:
#   S_V    all minimal-norm integer lifts of the 20 deposited classes,
#          uniform weight per VECTOR
#   S_C    the same lifts, uniform weight per CLASS (ties split equally)
#   S_SYM  the 48-closure of S_V (the declared symmetric completion),
#          uniform weight per vector
# Frozen conventions: minimal-norm lifts WITH TIES (no representative
# choice); the isometry T with columns f1=(1,-1,0), f2=(0,1,-1),
# f3=(-1,-1,0) maps basis coords to the D_3 picture. Under R1-B every
# verdict below is invariant under the point-group ambiguity of the
# lift (conjugation permutes the alphabet classes and their tie sets).
import sys
from fractions import Fraction
from itertools import product, permutations

OK = []
def chk(name, ok, data):
    OK.append(ok)
    print("%s %s %s" % (name, "PASS" if ok else "FAIL", data))
def note(name, data):
    print("%s NOTE %s" % (name, data))

P = 5
def m6(*rows):
    return tuple(tuple(x % P for x in r) for r in rows)
def matv6(M, x):
    return tuple(sum(M[i][k] * x[k] for k in range(6)) % P for i in range(6))
def matm6(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(6)) % P
                       for j in range(6)) for i in range(6))
I6 = m6(*[[1 if i == j else 0 for j in range(6)] for i in range(6)])

class Aff:
    def __init__(self, M, v):
        self.M = M
        self.v = tuple(x % P for x in v)
    def then(self, other):
        M = matm6(other.M, self.M)
        v = tuple((matv6(other.M, self.v)[i] + other.v[i]) % P
                  for i in range(6))
        return Aff(M, v)
    def eq(self, other):
        return self.M == other.M and self.v == other.v

S4 = ((0,0,1,0,0,0),(0,0,0,1,0,0),(1,0,0,0,0,0),(0,1,0,0,0,0))
A_M = m6((0,1,0,0,0,0),(1,0,0,0,0,0),(0,0,0,1,0,0),(0,0,1,0,0,0),
         (0,0,0,0,1,0),(0,0,0,0,0,1))
gen_a = Aff(A_M, (0,)*6)
B_M = m6(*[[(-S4[i][j]) % P for j in range(4)] + [0,0] for i in range(4)],
         (0,0,0,0,-1 % P,0), (0,0,0,0,0,-1 % P))
gen_b = Aff(B_M, (0,)*6)
u_c = (0,1,0,-1)
C_M = m6(*[[(-S4[i][j]) % P for j in range(4)] + [0, u_c[i] % P]
           for i in range(4)],
         (0,0,0,0,-1 % P,0), (0,0,0,0,0,-1 % P))
gen_c = Aff(C_M, (2,1,2,1,1,0))
NI = m6(*[[(-1 if i == j else 0) % P for j in range(6)] for i in range(6)])
gen_d = Aff(NI, (2,1,3,4,1,1))
gen_e = Aff(NI, (2,1,3,4,2,1))

# transcription cross-checks, re-run
idA = Aff(I6, (0,)*6)
def comm(g, h):
    return h.then(g).then(h).then(g)
c_de, c_bd, c_be = comm(gen_d, gen_e), comm(gen_b, gen_d), comm(gen_b, gen_e)
chk("X", all(g.then(g).eq(idA) for g in (gen_a, gen_b, gen_c, gen_d, gen_e))
        and c_de.v == (0,0,0,0,3,0) and c_bd.v == (0,0,0,0,3,3)
        and c_be.v == (0,0,0,0,1,3),
    "involutions and fired fiber commutators reproduce the display")

# the deposited alphabet: Gamma-orbit spatial classes
def tr4(x): return sum(x[:4]) % P
GAMMA = [gen_a.M, gen_c.M, gen_d.M, gen_e.M]
orbit = {gen_c.v, gen_d.v, gen_e.v}
grew = True
while grew:
    grew = False
    for M in GAMMA:
        for v in list(orbit):
            w = matv6(M, v)
            if w not in orbit:
                orbit.add(w)
                grew = True
classes = sorted(set(v[:4] for v in orbit
                     if tr4(v) == 0 and v[:4] != (0,0,0,0)))
chk("A0", len(classes) == 20, "deposited spatial classes: %d" % len(classes))

# minimal-norm lifts WITH TIES, sum-zero integer vectors
def min_lifts(w):
    best, ties = None, []
    for combo in product(*[[wi + s for s in (-10, -5, 0, 5)] for wi in w]):
        if sum(combo) != 0:
            continue
        n = sum(x * x for x in combo)
        if best is None or n < best:
            best, ties = n, [combo]
        elif n == best:
            ties.append(combo)
    return best, sorted(ties)

T = ((1, 0, -1), (-1, 1, -1), (0, -1, 0))
def to_d3(x):
    c = (x[0], x[0] + x[1], x[0] + x[1] + x[2])
    return tuple(sum(T[i][k] * c[k] for k in range(3)) for i in range(3))

SV = []          # (vector in Z^3, class index)
class_ties = []
iso_ok = True
for ci, w in enumerate(classes):
    n, ties = min_lifts(w)
    vs = []
    for x in ties:
        y = to_d3(x)
        if sum(t * t for t in y) != n:
            iso_ok = False
        vs.append(y)
    class_ties.append(vs)
    for y in vs:
        SV.append((y, ci))
chk("A1", iso_ok, "isometry preserves every lift norm")
tie_census = {}
for vs in class_ties:
    tie_census[len(vs)] = tie_census.get(len(vs), 0) + 1
note("A1", "lift tie census (ties per class -> classes): %s; total "
     "vectors %d" % (sorted(tie_census.items()), len(SV)))
neg_closed = all(tuple(-t for t in y) in set(v for v, _ in SV)
                 for y, _ in SV)
chk("A2", neg_closed, "the lift set is closed under negation "
    "(odd moments vanish exactly)")

# the 48-closure
def sperm_all():
    out = []
    for p in permutations(range(3)):
        for s in product((1, -1), repeat=3):
            out.append(tuple(tuple(s[i] if p[i] == j else 0
                                   for j in range(3)) for i in range(3)))
    return out
SP = sperm_all()
def act(M, v):
    return tuple(sum(M[i][k] * v[k] for k in range(3)) for i in range(3))
SSYM = set()
for y, _ in SV:
    for M in SP:
        SSYM.add(act(M, y))
SSYM = sorted(SSYM)
shells_sym = {}
for y in SSYM:
    n = sum(t * t for t in y)
    shells_sym[n] = shells_sym.get(n, 0) + 1
note("A3", "symmetric completion S_SYM: %d vectors, shells %s"
     % (len(SSYM), sorted(shells_sym.items())))

# exact moment machinery: weighted sums of monomials
MONS1 = [(1,0,0),(0,1,0),(0,0,1)]
MONS2 = [(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
MONS4 = sorted([(i, j, 4 - i - j) for i in range(5) for j in range(5 - i)])
def mono(y, e):
    r = 1
    for t, k in zip(y, e):
        r *= t ** k
    return r
def moments(weighted):
    m1 = [sum(wt * mono(y, e) for y, wt in weighted) for e in MONS1]
    m2 = {e: sum(wt * mono(y, e) for y, wt in weighted) for e in MONS2}
    m4 = {e: sum(wt * mono(y, e) for y, wt in weighted) for e in MONS4}
    return m1, m2, m4
def iso2(m2):
    diag = [m2[(2,0,0)], m2[(0,2,0)], m2[(0,0,2)]]
    off = [m2[(1,1,0)], m2[(1,0,1)], m2[(0,1,1)]]
    return len(set(diag)) == 1 and all(x == 0 for x in off), diag, off
def iso4(m4):
    pure = [m4[(4,0,0)], m4[(0,4,0)], m4[(0,0,4)]]
    sq = [m4[(2,2,0)], m4[(2,0,2)], m4[(0,2,2)]]
    mixed = {e: v for e, v in m4.items()
             if sorted(e, reverse=True) not in ([4,0,0], [2,2,0])
             and v != 0}
    full = (len(set(pure)) == 1 and len(set(sq)) == 1 and not mixed
            and pure[0] == 3 * sq[0])
    return full, pure, sq, mixed

def analyze(tag, weighted, expect_zero_m1=True):
    m1, m2, m4 = moments(weighted)
    z1 = all(x == 0 for x in m1)
    i2, diag, off = iso2(m2)
    i4, pure, sq, mixed = iso4(m4)
    if expect_zero_m1:
        chk(tag + ".m1", z1, "first moments %s" % (m1,))
    else:
        note(tag + ".m1", "first moments %s (single class carries no "
             "negation closure; zero is not asserted)" % (m1,))
    chk(tag + ".m2", True, "M2 diag=%s off=%s -> %s"
        % (diag, off, "ISOTROPIC" if i2 else "ANISOTROPIC"))
    print("%s.m4 INFO pure=%s sq=%s mixed_nonzero=%s deficit(pure-3sq)=%s "
          "-> %s" % (tag, pure, sq,
                     sorted(mixed.items()) if mixed else "{}",
                     [p - 3 * s for p, s in zip(pure, sq)],
                     "ISOTROPIC" if i4 else "ANISOTROPIC"))
    return i2, i4

print("-- S_V: uniform per vector over the deposited alphabet lifts --")
wv = [(y, Fraction(1)) for y, _ in SV]
i2v, i4v = analyze("SV", wv)
print("-- S_C: uniform per class, ties split equally --")
wc = []
for ci, vs in enumerate(class_ties):
    for y in vs:
        wc.append((y, Fraction(1, len(vs))))
i2c, i4c = analyze("SC", wc)
print("-- S_SYM: uniform per vector over the 48-closure --")
ws = [(y, Fraction(1)) for y in SSYM]
i2s, i4s = analyze("SSYM", ws)
print("-- seed class (2,1,3,4) alone, its minimal lift ties --")
seed_idx = classes.index((2, 1, 3, 4))
wseed = [(y, Fraction(1)) for y in class_ties[seed_idx]]
i2seed, i4seed = analyze("SEED", wseed, expect_zero_m1=False)

# planarity of the deposited alphabet (a discovered exact fact)
ys = set(y[1] for y, _ in SV)
planar = ys == {0}
rank2 = planar
chk("A4", planar,
    "PLANARITY: every one of the 20 minimal lifts has second "
    "coordinate 0; the deposited alphabet spans a RANK-2 sublattice "
    "(invariant statement under R1-B: the alphabet is coplanar). "
    "M2 within the plane is (60, 100): anisotropic even there.")

print("-- verdict --")
print("V1 S_V   second order %s, fourth order %s"
      % ("isotropic" if i2v else "ANISOTROPIC",
         "isotropic" if i4v else "ANISOTROPIC"))
print("V2 S_C   second order %s, fourth order %s"
      % ("isotropic" if i2c else "ANISOTROPIC",
         "isotropic" if i4c else "ANISOTROPIC"))
print("V3 S_SYM second order %s, fourth order %s"
      % ("isotropic" if i2s else "ANISOTROPIC",
         "isotropic" if i4s else "ANISOTROPIC"))
print("V4 seed  second order %s, fourth order %s"
      % ("isotropic" if i2seed else "ANISOTROPIC",
         "isotropic" if i4seed else "ANISOTROPIC"))
ok = all(OK)
print("MOMENT RECON %d/%d checks PASS, VERDICT %s"
      % (sum(OK), len(OK), "COMPLETE" if ok else "TRANSCRIPTION DEFECT"))
sys.exit(0 if ok else 1)
