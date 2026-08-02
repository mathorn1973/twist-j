#!/usr/bin/env python3
# verify_common_carrier_icosian.py
# Exact verifier for the icosian common-carrier candidate
# C-COMMON-CARRIER-ICOSIAN-1 (TWIST-J incubation lane, NON-CANONICAL,
# no canon writes). Against Public Canon v30.
#
# Thesis. The icosian ring O (the maximal Z[phi]-order of the definite
# quaternion algebra B = (-1,-1) over F = Q(sqrt5)) is one carrier on which
# the following live simultaneously and without further choices:
#   (i)   2I, the 120 units of reduced norm 1, acting on the right,
#         h-unitarily for the canonical CM-Hermitian form h(x,y) = pi_K(x ybar)
#         on B = K + K e, K = Q(zeta5) embedded by zeta5 -> q, an icosian of
#         multiplicative order 5 with trd(q) = phi - 1 (single 2I-class);
#   (ii)  the left K-action, with J = 1 + q^2 an h-similitude of totally
#         positive multiplier J Jbar = 2 - phi = phi^-2 (J-MODULUS-CHORD);
#   (iii) both actions commute by associativity;
#   (iv)  O is a FREE rank-2 Z[zeta5]-module, O = Z[q].1 + Z[q].omega with
#         omega = (1+i+j+k)/2, while the h-orthogonal splitting K.1 + K.e is
#         GLUED: [O : Z[q].1 + Z[q].e] = 5, supported at the ramified prime
#         p5 = (q - q^4), and h(O,O) lies in p5^-1 Z[zeta5], not in Z[zeta5];
#   (v)   the boost diag(D1, D2) along the h-splitting preserves O exactly
#         when the two slots agree in the ramified residue field F5
#         (res J = 2 = J_lambda of RAMIFIED-TM-LIFT, res J^-1 = 3), so the
#         even loxodromic tick is integral only in the twisted form
#         diag(J, -J^-1), whose coherence phase is 1 - J = -zeta5^2, the
#         registered primitive tenth root (J-TENTH-ROOT); the single tick has
#         no F-rational carrier realization at all, because nrd(y) = +-phi^-1
#         is not totally positive: K(sqrt J) = K(sqrt phi);
#   (vi)  the golden-twisted trace form Tr_{F/Q}(phi trd(x ybar)/sqrt5) makes
#         O the E8 root lattice (even, unimodular, positive definite);
#   (vii) the right action in the free basis is an integral 2x2 matrix model
#         over Z[zeta5] with the same (order, trace) class function as the
#         registered COLOR-INTEGRAL-LIFT generators S, T, hence GL2(K)-
#         conjugate to it (equal irreducible characters), and the class of q
#         reduces to the registered class 5a: the conjugation 3-space is the
#         canon row 3a with chi(5a) = 1 - phi.
#
# Exact arithmetic in every assertion: Fraction over Q(sqrt5), Q(zeta5),
# and integer lattices. Python 3 standard library only. Deterministic,
# no randomness.
import sys
from fractions import Fraction as F

R = []
def ck(name, cond):
    ok = bool(cond)
    R.append(ok)
    print(("PASS " if ok else "FAIL ") + name)

# ---------- 0. F = Q(sqrt5) exact: pairs (a, b) = a + b*sqrt5 ----------
def fa(p, q): return (p[0]+q[0], p[1]+q[1])
def fs(p, q): return (p[0]-q[0], p[1]-q[1])
def fm(p, q): return (p[0]*q[0] + 5*p[1]*q[1], p[0]*q[1] + p[1]*q[0])
def fneg(p): return (-p[0], -p[1])
def fint(n): return (F(n), F(0))
def finv(p):
    d = p[0]*p[0] - 5*p[1]*p[1]
    return (p[0]/d, -p[1]/d)
def fgal(p): return (p[0], -p[1])           # nontrivial element of Gal(F/Q)
def fsign(p):                                # exact sign of a + b*sqrt5
    a, b = p
    if a == 0 and b == 0: return 0
    if a >= 0 and b >= 0: return 1
    if a <= 0 and b <= 0: return -1
    big = 1 if a*a > 5*b*b else -1
    return big if a > 0 else -big
F0 = fint(0); F1 = fint(1)
PHI  = (F(1, 2), F(1, 2))                    # phi
IPHI = (F(-1, 2), F(1, 2))                   # 1/phi = phi - 1
ck("R0  phi^2 = phi+1, phi (phi-1) = 1, sigma(phi) = 1-phi, exact in Q(sqrt5)",
   fm(PHI, PHI) == fa(PHI, F1) and fm(PHI, IPHI) == F1
   and fgal(PHI) == fs(F1, PHI) and fs(PHI, F1) == IPHI)

# ---------- 1. quaternions over F: (a, b, c, d) = a + b i + c j + d k ----------
def qadd(x, y): return tuple(fa(p, r) for p, r in zip(x, y))
def qsub(x, y): return tuple(fs(p, r) for p, r in zip(x, y))
def qmul(x, y):
    a1, b1, c1, d1 = x; a2, b2, c2, d2 = y
    return (fs(fs(fm(a1, a2), fm(b1, b2)), fa(fm(c1, c2), fm(d1, d2))),
            fs(fa(fa(fm(a1, b2), fm(b1, a2)), fm(c1, d2)), fm(d1, c2)),
            fa(fs(fm(a1, c2), fm(b1, d2)), fa(fm(c1, a2), fm(d1, b2))),
            fa(fa(fm(a1, d2), fm(b1, c2)), fs(fm(d1, a2), fm(c1, b2))))
def qconj(x): return (x[0], fneg(x[1]), fneg(x[2]), fneg(x[3]))
def qneg(x): return tuple(fneg(p) for p in x)
def qsca(s, x): return tuple(fm(s, p) for p in x)
def trd(x): return fm(fint(2), x[0])
def nrd(x):
    return fa(fa(fm(x[0], x[0]), fm(x[1], x[1])), fa(fm(x[2], x[2]), fm(x[3], x[3])))
QZERO = (F0, F0, F0, F0)
QONE  = (F1, F0, F0, F0)
QI    = (F0, F1, F0, F0)
QJ    = (F0, F0, F1, F0)
QK    = (F0, F0, F0, F1)

# ---------- 2. the icosian group 2I by closure ----------
H2 = (F(1, 2), F(0))
g5 = (fm(H2, IPHI), fm(H2, PHI), H2, F0)     # (phi^-1 + phi i + j)/2
g6 = (H2, H2, H2, H2)                         # (1 + i + j + k)/2
grp = {QONE}
frontier = [QONE]
overflow = False
while frontier and not overflow:
    x = frontier.pop()
    for g in (QI, g5, g6):
        y = qmul(x, g)
        if y not in grp:
            grp.add(y); frontier.append(y)
            if len(grp) > 130:
                overflow = True; break
ICO = sorted(grp)
ck("I1  the group generated by i, (phi^-1 + phi i + j)/2, (1+i+j+k)/2 closes with exactly 120 elements",
   not overflow and len(ICO) == 120
   and all(qmul(a, b) in grp for a in ICO for b in ICO))
ck("I2  all 120 icosians have nrd = 1, and -1 is central",
   all(nrd(g) == F1 for g in ICO) and qneg(QONE) in grp
   and all(qmul(qneg(QONE), g) == qmul(g, qneg(QONE)) for g in ICO))
def order_of(g):
    n = 1; x = g
    while x != QONE:
        x = qmul(x, g); n += 1
        if n > 200: return 0
    return n
ORD = {g: order_of(g) for g in ICO}
orders = {}
for g in ICO: orders[ORD[g]] = orders.get(ORD[g], 0) + 1
ck("I3  element-order profile of 2I: 1x1, 2x1, 3x20, 4x30, 5x24, 6x20, 10x24",
   orders == {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24})
proj = set()
for g in ICO:
    m = qneg(g)
    proj.add(g if g <= m else m)
porders = {}
for g in proj:
    n = 1; x = g
    while x != QONE and x != qneg(QONE):
        x = qmul(x, g); n += 1
    porders[n] = porders.get(n, 0) + 1
ck("I4  2I/{+-1} has 60 elements, order profile 1x1, 2x15, 3x20, 5x24: six Sylow 5-subgroups force simplicity, the quotient is A5",
   len(proj) == 60 and porders == {1: 1, 2: 15, 3: 20, 5: 24})

# ---------- 3. internal CM: q of order 5 with trd(q) = phi - 1 ----------
qcands = sorted(g for g in ICO if ORD[g] == 5 and trd(g) == IPHI)
ck("Q1  exactly 12 icosians of order 5 have trd = phi-1 (deterministic pick: smallest)",
   len(qcands) == 12)
q = qcands[0]
q2 = qmul(q, q); q3 = qmul(q2, q); q4 = qmul(q3, q)
ck("Q2  q^2 - (phi-1) q + 1 = 0: the quadratic pins K = F(q) as the CM extension of F inside B",
   qadd(qsub(q2, qsca(IPHI, q)), QONE) == QZERO)
ck("Q3  Phi_5(q) = 1 + q + q^2 + q^3 + q^4 = 0 and q^5 = 1: q realizes zeta5, Z[q] = Z[zeta5]",
   qadd(qadd(QONE, qadd(q, q2)), qadd(q3, q4)) == QZERO and qmul(q4, q) == QONE)
ck("Q4  phi = 1 + q + q^4 inside Z[q]: the golden ring lives in the internal CM ring",
   qadd(QONE, qadd(q, q4)) == qsca(PHI, QONE))
qclass = set()
for g in ICO: qclass.add(qmul(qmul(g, q), qconj(g)))
ck("Q5  the 2I-conjugacy class of q has exactly 12 elements, equals the trd = phi-1 order-5 set, and contains q^4 = q^-1: the CM embedding is unique up to inner 2I and CM conjugation (Sylow supplement)",
   qclass == set(qcands) and q4 in qclass)

# ---------- 4. J = 1 + q^2 as a golden unit of O ----------
Jq = qadd(QONE, q2)
ck("J1  nrd(J) = J Jbar = 2 - phi = phi^-2: totally positive unit multiplier (J-MODULUS-CHORD)",
   nrd(Jq) == fs(fint(2), PHI) and qmul(Jq, qconj(Jq)) == qsca(fs(fint(2), PHI), QONE)
   and fm(fs(fint(2), PHI), fm(PHI, PHI)) == F1)
ck("J2  J phi = q: the phase of the J-step is exactly the internal zeta5 (J-GOLDEN-BRIDGE)",
   qsca(PHI, Jq) == q)
Jinv = qsca(PHI, q4)
ck("J3  J^-1 = phi q^4 lies in Z[q]: J is a unit of O",
   qmul(Jq, Jinv) == QONE and qmul(Jinv, Jq) == QONE)

# ---------- 5. O as a Z-lattice; the free Z[zeta5]-basis {1, omega} ----------
def zvec(x):
    out = []
    for p in x:
        for t in (4*p[0], 4*p[1]):
            if t.denominator != 1: return None
            out.append(int(t))
    return out
def hnf(vectors):
    rows = [v[:] for v in vectors if v is not None and any(v)]
    basis = []
    for col in range(8):
        while True:
            nz = [r for r in rows if r[col] != 0]
            if len(nz) <= 1: break
            nz.sort(key=lambda r: abs(r[col]))
            p = nz[0]
            newrows = [p]
            for r in rows:
                if r is p: continue
                if r[col] != 0:
                    f = r[col] // p[col]
                    r = [a - f*b for a, b in zip(r, p)]
                if any(r): newrows.append(r)
            rows = newrows
        nz = [r for r in rows if r[col] != 0]
        if nz:
            p = nz[0] if nz[0][col] > 0 else [-t for t in nz[0]]
            basis.append((col, p))
            rows = [r for r in rows if r[col] == 0 and any(r)]
    return basis
def in_lattice(v, basis):
    if v is None: return False
    v = v[:]
    for col, b in basis:
        if v[col] % b[col] != 0: return False
        f = v[col] // b[col]
        v = [a - f*c for a, c in zip(v, b)]
    return not any(v)
def latdet(basis):
    d = 1
    for col, b in basis: d *= b[col]
    return d
LO = hnf([zvec(g) for g in ICO])
ck("O1  the Z-span of the 120 icosians is a full rank-8 lattice: O as a Z-module",
   len(LO) == 8)
def span_lattice(u1, u2):
    gensz = [zvec(qmul(z, u)) for u in (u1, u2) for z in (QONE, q, q2, q3)]
    if any(g is None for g in gensz): return None
    L = hnf(gensz)
    if len(L) != 8: return None
    if not all(in_lattice(g, LO) for g in gensz): return None
    return L
om = g6                                        # omega = (1+i+j+k)/2
qom = qmul(q, om)
Lfree = span_lattice(QONE, om)
ck("FB1 O = Z[q].1 + Z[q].omega with omega = (1+i+j+k)/2: the icosian ring is a FREE rank-2 Z[zeta5]-module (mutual inclusion, equal determinants)",
   Lfree is not None and latdet(Lfree) == latdet(LO)
   and all(in_lattice(zvec(g), Lfree) for g in ICO))

# ---------- 6. the h-splitting B = K.1 + K.e and its ramified glue ----------
ecands = sorted(g for g in ICO if trd(g) == F0 and qmul(g, q) == qmul(qconj(q), g))
ck("E1  exactly 10 pure icosians e satisfy e q = qbar e: the K e line meets 2I in the Dic5 lifts (deterministic pick: smallest)",
   len(ecands) == 10)
e = ecands[0]
qe = qmul(q, e)
ck("E2  e^2 = -1: the cyclic-algebra parameter is gamma = -1, B = (K/F, sigma, -1)",
   qmul(e, e) == qneg(QONE))
glue_ok = True
for cand in ecands:
    L = span_lattice(QONE, cand)
    if L is None or latdet(L) != 5*latdet(LO): glue_ok = False
ck("G1  for EVERY such e the sublattice Z[q].1 + Z[q].e has index exactly 5 in O: the h-splitting is glued, never free",
   glue_ok)
c5 = qsub(q, q4)                               # c = q - q^4, generator of p5
ck("G2  c = q - q^4 generates the ramified prime: -c^2 = 2 + phi with N_{F/Q}(2+phi) = 5; and c^-1 e is NOT in O, so O intersect K e = Z[q] e exactly (the glue is diagonal, not a line shift)",
   qmul(c5, c5) == qsca(fneg(fa(fint(2), PHI)), QONE)
   and fm(fa(fint(2), PHI), fgal(fa(fint(2), PHI))) == (F(5), F(0))
   and not in_lattice(zvec(qmul(qsca(finv(fneg(fa(fint(2), PHI))), c5), e)), LO))

def solve_in(basis4, x):
    M = [[basis4[j][i] for j in range(4)] for i in range(4)]
    v = [x[i] for i in range(4)]
    for col in range(4):
        piv = None
        for r in range(col, 4):
            if M[r][col] != F0: piv = r; break
        if piv is None: return None
        M[col], M[piv] = M[piv], M[col]; v[col], v[piv] = v[piv], v[col]
        inv = finv(M[col][col])
        M[col] = [fm(inv, t) for t in M[col]]; v[col] = fm(inv, v[col])
        for r in range(4):
            if r != col and M[r][col] != F0:
                f = M[r][col]
                M[r] = [fs(M[r][t], fm(f, M[col][t])) for t in range(4)]
                v[r] = fs(v[r], fm(f, v[col]))
    return ((v[0], v[1]), (v[2], v[3]))
BASE = [QONE, q, e, qe]
def coords_e(x): return solve_in(BASE, x)
ck("B1  {1, q, e, qe} is an F-basis of B: unique left-K coordinates exist for all of O",
   all(coords_e(g) is not None for g in ICO))

def kmul(u, v):
    c0 = fm(u[0], v[0]); c1 = fa(fm(u[0], v[1]), fm(u[1], v[0])); c2 = fm(u[1], v[1])
    return (fs(c0, c2), fa(c1, fm(IPHI, c2)))
def kadd(u, v): return (fa(u[0], v[0]), fa(u[1], v[1]))
def ksig(u): return (fa(u[0], fm(IPHI, u[1])), fneg(u[1]))
def knorm(u): return kmul(u, ksig(u))
def kquat(u): return qadd(qsca(u[0], QONE), qsca(u[1], q))
K0 = (F0, F0); K1 = (F1, F0); KQ = (F0, F1)
def fint_zphi(p):                              # is a + b sqrt5 in Z[phi]?
    a, b = p
    return (2*b).denominator == 1 and (a - b).denominator == 1
def kint(u): return fint_zphi(u[0]) and fint_zphi(u[1])

def h(x, y):
    cc = coords_e(qmul(x, qconj(y)))
    return cc[0]

omc = coords_e(om)
cK = (fneg(IPHI), fint(2))                     # c = q - q^4 = (1-phi) + 2q as K-pair
ck("G3  glue witness: omega = (1+i+j+k)/2 has K-coordinates with a genuine p5 denominator: alpha(omega) not in Z[zeta5] but c alpha(omega) in Z[zeta5]",
   kquat(cK) == c5 and not kint(omc[0]) and kint(kmul(cK, omc[0])))
ZB = [qmul(z, u) for u in (QONE, om) for z in (QONE, q, q2, q3)]
ck("G4  h(O,O) lies in p5^-1 Z[zeta5] and NOT in Z[zeta5]: c h(x,y) is integral on a full Z-basis of O (biadditivity extends), while h(1, omega) itself is not integral -- the Hermitian form is inverse-different-valued, the E8 signature of the carrier",
   all(kint(kmul(cK, h(x, y))) for x in ZB for y in ZB)
   and not kint(h(QONE, om)))

# ---------- 7. the form h and the two commuting actions ----------
ck("H1  Gram of h on {1, e} is the identity: h(1,1) = h(e,e) = 1, h(1,e) = h(e,1) = 0",
   h(QONE, QONE) == K1 and h(e, e) == K1 and h(QONE, e) == K0 and h(e, QONE) == K0)
hbas = [QONE, q, e, qe]
ck("H2  h(y,x) = sigma(h(x,y)) on all 16 basis pairs: h is Hermitian for the CM involution; sesquilinearity extends this to all of B",
   all(h(y, x) == ksig(h(x, y)) for x in hbas for y in hbas))
ck("H3  h(g,g) = 1 for all 120 icosians: every icosian is an h-unit vector of the definite CM-Hermitian form",
   all(h(g, g) == K1 for g in ICO))
ck("A1  the RIGHT action of all 120 icosians is h-unitary: h(x g, y g) = h(x, y) on basis pairs, hence everywhere by sesquilinearity",
   all(h(qmul(x, g), qmul(y, g)) == h(x, y)
       for g in ICO for x in (QONE, e) for y in (QONE, e)))
ck("A2  LEFT multiplication by q is K-linear with h(q x, q y) = N(q) h = h; left K and right 2I commute by associativity (all basis-times-group triples)",
   all(h(qmul(q, x), qmul(q, y)) == h(x, y) for x in hbas for y in hbas)
   and all(qmul(qmul(q, x), g) == qmul(q, qmul(x, g)) for x in hbas for g in ICO))
ck("A3  LEFT multiplication by J is an h-similitude with multiplier nrd(J) = 2 - phi = phi^-2 exactly: J lives in GU(2), unitary at neither place",
   all(h(qmul(Jq, x), qmul(Jq, y)) == kmul((fs(fint(2), PHI), F0), h(x, y))
       for x in hbas for y in hbas))

# ---------- 8. the ramified residue criterion and the twisted even tick ----------
JK  = coords_e(Jq)[0]
JKi = coords_e(Jinv)[0]
ck("T1  J as K-scalar: J = phi^-1 q, J J^-1 = 1, J sigma(J) = 2 - phi, J / sigma(J) = q^2",
   JK == (F0, IPHI) and kmul(JK, JKi) == K1
   and knorm(JK) == (fs(fint(2), PHI), F0)
   and kmul(JK, JK) == kmul(knorm(JK), kmul(KQ, KQ)))
def kres(u):                                   # reduction mod p5 = (q - q^4): zeta5 -> 1
    v = u[0][0] + 5*u[0][1] + u[1][0] + 5*u[1][1]
    if v.denominator != 1: return None
    return int(v) % 5
ck("T2  ramified residues: res(q) = 1, res(phi) = 3, res(J) = 2 = J_lambda (RAMIFIED-TM-LIFT), res(J^-1) = 3, res(-J^-1) = 2: the golden pair shadows to {2, 3}",
   kres(KQ) == 1 and kres((PHI, F0)) == 3 and kres(JK) == 2
   and kres(JKi) == 3 and kres(kmul((fneg(F1), F0), JKi)) == 2)
def dmap(D1, D2, x):
    cc = coords_e(x)
    if cc is None: return None
    return qadd(kquat(kmul(D1, cc[0])), qmul(kquat(kmul(D2, cc[1])), e))
LOB = [ZB[i] for i in range(8)]                # Z-basis of O (valid by FB1)
def integral(D1, D2):
    return all(in_lattice(zvec(dmap(D1, D2, x)), LO) for x in LOB)
FAM = []
qp = K1
for a in range(5):
    for s in (K1, (fneg(F1), F0)):
        for Jc in (K1, JK):
            FAM.append(kmul(kmul(s, qp), Jc))
    qp = kmul(qp, KQ)
crit_ok = True
for D1 in FAM:
    for D2 in FAM:
        if integral(D1, D2) != (kres(D1) == kres(D2)): crit_ok = False
ck("T3  the glue criterion, swept over all 400 pairs from {+-q^a, +-q^a J}: diag(D1, D2) preserves O exactly when res(D1) = res(D2) in the ramified residue field F5",
   crit_ok)
MJK = kmul((fneg(F1), F0), JKi)                # -J^-1
ck("T4  the twisted even tick diag(J, -J^-1) preserves O in both directions (res 2 = 2), while its coordinate action is u -> (2-phi) u, v -> phi^2 v, w -> (1-J) w with 1 - J = -q^2 the registered primitive TENTH root (J-TENTH-ROOT): the glue converts the naive fifth-root phase q^2 into the tenth root -q^2 -- the double cover appears in the phase",
   integral(JK, MJK) and integral(JKi, kmul((fneg(F1), F0), JK))
   and knorm(JK) == (fs(fint(2), PHI), F0) and knorm(MJK) == (fm(PHI, PHI), F0)
   and kmul(JK, ksig(MJK)) == kmul((fneg(F1), F0), kmul(KQ, KQ))
   and kadd(K1, kmul((fneg(F1), F0), JK)) == kmul((fneg(F1), F0), kmul(KQ, KQ)))
def kpow(u, n):
    r = K1
    for _ in range(n): r = kmul(r, u)
    return r
PH5 = fm(PHI, fm(PHI, fm(PHI, fm(PHI, PHI))))
ck("T5  five twisted even ticks are the pure boost with an e-slot sign, diag(phi^-5, -phi^5); ten are the pure boost diag(phi^-10, phi^10): J^5 = phi^-5 (J-GOLDEN-BRIDGE) and the residual bit closes only on the tenth",
   kpow(JK, 5) == (finv(PH5), F0) and kpow(MJK, 5) == (fneg(PH5), F0)
   and kpow(MJK, 10) == (fm(PH5, PH5), F0))
ck("T6  half-step obstruction: y^2 = J forces nrd(y) = +-phi^-1, neither is totally positive (sigma(phi^-1) = -phi < 0, -phi^-1 < 0), and nrd is totally positive on B \\ {0}: the single tick has NO F-rational carrier realization",
   fm(IPHI, IPHI) == fs(fint(2), PHI)
   and fsign(fgal(IPHI)) == -1 and fsign(fneg(IPHI)) == -1
   and fsign(IPHI) == 1 and fsign(fgal(fneg(IPHI))) == 1)
ck("T7  K(sqrt J) = K(sqrt phi): zeta5 = (-zeta5^3)^2 is already a square in K and J phi = zeta5, so the spinorial single tick lives exactly one golden square root away",
   qmul(qneg(q3), qneg(q3)) == q and qsca(PHI, Jq) == q)

# ---------- 9. the conjugation 3-space and its golden branch ----------
def conj_mat(g):
    cols = []
    for b in (QI, QJ, QK):
        v = qmul(qmul(g, b), qconj(g))
        cols.append((v[1], v[2], v[3]))
    return cols
def mtrace(m): return fa(fa(m[0][0], m[1][1]), m[2][2])
ck("C1  conjugation by q acts on the pure 3-space with trace 1 - phi; by q^2 with trace phi: the arithmetic CM generator sits in the branch whose 3-space character is the Galois-conjugate golden value",
   mtrace(conj_mat(q)) == fs(F1, PHI) and mtrace(conj_mat(q2)) == PHI)
cls5 = sorted(set(mtrace(conj_mat(g)) for g in ICO if ORD[g] in (5, 10)))
ck("C2  the 5-classes realize exactly the two golden traces {1-phi, phi}: the branch pair is complete and Galois-conjugate",
   cls5 == sorted([fs(F1, PHI), PHI]))

# ---------- 10. the golden-twisted trace form is E8 ----------
TW = fm(PHI, (F(0), F(1, 5)))                  # phi / sqrt5
GM = []
tw_ok = True
for x in ZB:
    row = []
    for y in ZB:
        v = fm(TW, trd(qmul(x, qconj(y))))
        t = 2*v[0]
        if t.denominator != 1: tw_ok = False; t = F(0)
        row.append(int(t))
    GM.append(row)
ck("X1  the golden-twisted trace form B(x,y) = Tr_{F/Q}(phi trd(x ybar)/sqrt5) is integral and even on O (the p5^-1 of h absorbed by the inverse different times the unit phi)",
   tw_ok and all(GM[i][i] % 2 == 0 for i in range(8)))
def fdet(M):
    n = len(M)
    A = [[F(M[i][j]) for j in range(n)] for i in range(n)]
    det = F(1)
    for c in range(n):
        p = None
        for r in range(c, n):
            if A[r][c] != 0: p = r; break
        if p is None: return F(0)
        if p != c: A[c], A[p] = A[p], A[c]; det = -det
        det *= A[c][c]
        inv = 1/A[c][c]
        A[c] = [t*inv for t in A[c]]
        for r in range(c+1, n):
            if A[r][c] != 0:
                f = A[r][c]
                A[r] = [u - f*w for u, w in zip(A[r], A[c])]
    return det
minors_pos = all(fdet([row[:k] for row in GM[:k]]) > 0 for k in range(1, 9))
ck("X2  det = 1 and all leading principal minors positive: (O, B) is an even unimodular positive definite rank-8 lattice, hence THE E8 root lattice (uniqueness); the icosian carrier meets the registered affine-E8 ladder (COLOR-MCKAY-E8) at the lattice level with no new parameter",
   fdet(GM) == 1 and minors_pos)

# ---------- 11. bridge to the registered integral 2I model over Z[zeta5] ----------
def red5(v):
    cc = v[4]
    return (v[0]-cc, v[1]-cc, v[2]-cc, v[3]-cc)
def zm(a, b):
    v = [0]*5
    for i in range(4):
        if a[i] == 0: continue
        for j in range(4):
            if b[j] == 0: continue
            v[(i+j) % 5] += a[i]*b[j]
    return red5(tuple(v))
def za(a, b): return tuple(p+r for p, r in zip(a, b))
Z0 = (0, 0, 0, 0); Z1 = (1, 0, 0, 0); ZETA = (0, 1, 0, 0)
ZETA4 = red5((0, 0, 0, 0, 1))
def mmul(A, B):
    return ((za(zm(A[0][0], B[0][0]), zm(A[0][1], B[1][0])),
             za(zm(A[0][0], B[0][1]), zm(A[0][1], B[1][1]))),
            (za(zm(A[1][0], B[0][0]), zm(A[1][1], B[1][0])),
             za(zm(A[1][0], B[0][1]), zm(A[1][1], B[1][1]))))
SM = ((Z0, tuple(-t for t in Z1)), (Z1, Z0))
TM = ((ZETA, Z1), (Z0, ZETA4))
ID2 = ((Z1, Z0), (Z0, Z1))
lift = {ID2}
frontier = [ID2]
overflow2 = False
while frontier and not overflow2:
    x = frontier.pop()
    for g in (SM, TM):
        y = mmul(x, g)
        if y not in lift:
            lift.add(y); frontier.append(y)
            if len(lift) > 130:
                overflow2 = True; break
LIFT = sorted(lift)
def mdet(A):
    return tuple(p-r for p, r in zip(zm(A[0][0], A[1][1]), zm(A[0][1], A[1][0])))
ck("L1  the registered generators S = ((0,-1),(1,0)), T = ((zeta,1),(0,zeta^4)) close to exactly 120 matrices over Z[zeta5], all of determinant 1 (COLOR-INTEGRAL-LIFT reproduced)",
   not overflow2 and len(LIFT) == 120 and all(mdet(A) == Z1 for A in LIFT))
def zres(t): return sum(t) % 5
def mres(A):
    return (zres(A[0][0]), zres(A[0][1]), zres(A[1][0]), zres(A[1][1]))
RED = [mres(A) for A in LIFT]
ck("L2  reduction zeta -> 1 mod 5 sends the lift bijectively onto 120 distinct det-1 matrices: SL2(F5), the registered mod-(1-zeta) bijection",
   len(set(RED)) == 120 and all((r[0]*r[3] - r[1]*r[2]) % 5 == 1 for r in RED))
BASE2 = [QONE, q, om, qom]
def coords_om(x): return solve_in(BASE2, x)
def rho(g):
    gc = qconj(g)
    c1 = coords_om(qmul(QONE, gc))
    c2 = coords_om(qmul(om, gc))
    return ((c1[0], c2[0]), (c1[1], c2[1]))    # columns = images of 1, omega
def kdet2(A):
    return fs(kmul(A[0][0], A[1][1])[0], kmul(A[0][1], A[1][0])[0]), \
           fs(kmul(A[0][0], A[1][1])[1], kmul(A[0][1], A[1][0])[1])
RHO = {g: rho(g) for g in ICO}
ck("L3  rho(g) = (right multiplication by gbar) in the free basis {1, omega} is an INTEGRAL 2x2 representation over Z[zeta5] with det = nrd = 1, and rho(g h) = rho(g) rho(h) on the generator pairs",
   all(kint(RHO[g][i][j]) for g in ICO for i in range(2) for j in range(2))
   and all(kdet2(RHO[g]) == (F1, F0) for g in ICO)
   and all(RHO[qmul(a, b)] == ((kadd(kmul(RHO[a][0][0], RHO[b][0][0]), kmul(RHO[a][0][1], RHO[b][1][0])),
                                kadd(kmul(RHO[a][0][0], RHO[b][0][1]), kmul(RHO[a][0][1], RHO[b][1][1]))),
                               (kadd(kmul(RHO[a][1][0], RHO[b][0][0]), kmul(RHO[a][1][1], RHO[b][1][0])),
                                kadd(kmul(RHO[a][1][0], RHO[b][0][1]), kmul(RHO[a][1][1], RHO[b][1][1]))))
           for a in (QI, g5, g6) for b in (QI, g5, g6)))
SQRT5Z = (-1, 0, -2, -2)                        # sqrt5 = zeta-zeta^2-zeta^3+zeta^4 reduced
def conv_F(p):
    a, b = p
    v = [a + b*SQRT5Z[0], b*SQRT5Z[1], b*SQRT5Z[2], b*SQRT5Z[3]]
    return tuple(v)
def conv_K(u):
    t0 = conv_F(u[0]); t1 = conv_F(u[1])
    shifted = (-t1[3], t1[0]-t1[3], t1[1]-t1[3], t1[2]-t1[3])
    return tuple(t0[i]+shifted[i] for i in range(4))
def as_int_tuple(t):
    out = []
    for v in t:
        if F(v).denominator != 1: return None
        out.append(int(v))
    return tuple(out)
def mtord(A):
    n = 1; X = A
    while X != ID2:
        X = mmul(X, A); n += 1
        if n > 200: return 0
    return n
lift_classfn = {}
for A in LIFT:
    key = (mtord(A), za(A[0][0], A[1][1]))
    lift_classfn[key] = lift_classfn.get(key, 0) + 1
rho_classfn = {}
tr_sq_sum = F0
for g in ICO:
    t = kadd(RHO[g][0][0], RHO[g][1][1])
    tt = as_int_tuple(conv_K(t))
    key = (ORD[g], tt)
    rho_classfn[key] = rho_classfn.get(key, 0) + 1
    tr_sq_sum = fa(tr_sq_sum, fm(t[0], t[0]))  # trace is in F: second slot 0
trace_in_F = all(kadd(RHO[g][0][0], RHO[g][1][1])[1] == F0 for g in ICO)
ck("L4  the (order, trace) class functions of rho(2I) and of the registered lift agree exactly, traces lie in F, and sum of tr^2 over the group is 120 (irreducibility): equal irreducible characters over K force GL2(K)-conjugacy (Noether-Deuring) -- the icosian right action IS the registered COLOR-INTEGRAL-LIFT up to base change",
   trace_in_F and rho_classfn == lift_classfn and tr_sq_sum == fint(120))
tr_T = za(TM[0][0], TM[1][1])
cnt5 = {k: v for k, v in rho_classfn.items() if k[0] == 5}
ck("L5  character dictionary onto COLOR-GOLDEN-TABLE: tr(T) = zeta + zeta^4 = phi - 1 = trd(q), the 24 order-5 elements split 12+12 with traces {phi-1, -phi} = {chi_2a(5a), chi_2a(5b)}, and 5a/5b are separated by the spin trace: the class of q IS the registered class 5a, so with C1 the conjugation 3-space is the canon row 3a (chi(5a) = 1-phi, the McKay E8-arm row)",
   tr_T == as_int_tuple(conv_F(IPHI)) and trd(q) == IPHI
   and cnt5 == {(5, as_int_tuple(conv_F(IPHI))): 12,
                (5, as_int_tuple(conv_F(fneg(PHI)))): 12})
def rmres(A):
    r = (kres(A[0][0]), kres(A[0][1]), kres(A[1][0]), kres(A[1][1]))
    return None if any(t is None for t in r) else r
rq = rmres(RHO[q])
U0 = (1, 1, 0, 1); U2 = (1, 2, 0, 1)
def m2mul5(a, b):
    return ((a[0]*b[0]+a[1]*b[2]) % 5, (a[0]*b[1]+a[1]*b[3]) % 5,
            (a[2]*b[0]+a[3]*b[2]) % 5, (a[2]*b[1]+a[3]*b[3]) % 5)
def m2inv5(a):
    d = (a[0]*a[3]-a[1]*a[2]) % 5
    di = pow(d, 3, 5)
    return ((a[3]*di) % 5, (-a[1]*di) % 5, (-a[2]*di) % 5, (a[0]*di) % 5)
def conj5(a, b): return any(m2mul5(m2mul5(X, a), m2inv5(X)) == b for X in RED)
PF = (3, 0, 0, 1)                              # residue of the basis change diag(phi, 1)
rq_flip = m2mul5(m2mul5(PF, rq), m2inv5(PF))
ck("L6  residue gauge: rho(q) reduces to the OTHER unipotent residue class than the registered T (rho(q) ~ ((1,2),(0,1)), T -> ((1,1),(0,1))), my model's reduction is also a bijection, and one basis change diag(phi, 1) -- det residue 3, a non-square -- flips the class back: the 5a/5b RESIDUE labels are pinned only by the frozen matrices of COLOR-INTEGRAL-LIFT, not by the lattice; res(phi) = 3 being a non-residue is exactly why the canon must freeze explicit generators",
   rq is not None and mres(TM) == U0 and not conj5(rq, U0) and conj5(rq, U2)
   and len(set(rmres(RHO[g]) for g in ICO)) == 120
   and conj5(rq_flip, U0))

n = len(R); ok = sum(R)
print("SUMMARY %d/%d PASS" % (ok, n))
sys.exit(0 if ok == n else 1)
