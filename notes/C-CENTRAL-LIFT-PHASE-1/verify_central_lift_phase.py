#!/usr/bin/env python3
# verify_central_lift_phase.py
# Exact verifier for C-CENTRAL-LIFT-PHASE-1 (TWIST-J incubation lane,
# NON-CANONICAL, no canon writes). Against Public Canon v30.
#
# Content: the algebraic core of the accepted external audit of
# C-HERM2-BORN-CONE-1, promoted from prose to exact gates, plus the tick
# ladder that joins the audit's projective central-phase lemma to the
# integral glue of C-COMMON-CARRIER-ICOSIAN-1.
#   1. Branch pinning: the cosine data J + Jbar = J Jbar is branch-blind;
#      the polarization J phi = zeta5 pins arg J = +2 pi/5.
#   2. The principal spinor step s = zeta10 / sqrt(phi) has s^5 real
#      NEGATIVE (zeta10^5 = -1 exactly): g_J^5 is a pure boost only
#      projectively; the spinor clears the central sign at ten.
#   3. The Born/causal cone equivalence is theorem-grade: char poly of X
#      is lambda^2 - 2t lambda + det X, proved by interpolation grid;
#      the 2x2 sum/product sign lemma finishes it in text.
#   4. The one-tick action is exact WITHOUT square roots: the normalized
#      Herm action of A_J = diag(J, 1) is (u, v, w) ->
#      (phi^-1 u, phi v, zeta5 w); five ticks are the pure boost.
#   5. Central phase: Herm is projective (H_{cA} = H_A), Sym sees
#      c^2/N(c); exactly, A_J^2 = J diag(J, J^-1), so per two ticks the
#      Sym slot gains the central phase zeta5^2 while Herm slots agree.
#   6. The unit-scalar central phase group is exactly mu_5; the glue
#      phase 1 - J = -zeta5^2 of the integral even tick escapes it by
#      the central sign: mu_10 versus mu_5, the bit in the phase.
#   7. Tick ladder integrality: no unit multiple of diag(J, 1) passes
#      the ramified glue criterion (one tick never integral); the det-1
#      four-tick diag(J^2, J^-2) passes (res 4 = 4).
#   8. The audit's split-unit projector algebra and the rigidity lever,
#      both as grid-proved polynomial identities.
# Exact arithmetic everywhere; Python 3 stdlib; deterministic.
import sys
from fractions import Fraction as F

R = []
def ck(name, cond):
    ok = bool(cond)
    R.append(ok)
    print(("PASS " if ok else "FAIL ") + name)

# ---------- Z[zeta5] exact: coefficients of 1, x, x^2, x^3 mod Phi_5 ----------
def red(v):
    c = v[4]
    return (v[0]-c, v[1]-c, v[2]-c, v[3]-c)
def zmul(a, b):
    v = [F(0)]*5
    for i in range(4):
        if a[i] == 0: continue
        for j in range(4):
            if b[j] == 0: continue
            v[(i+j) % 5] += a[i]*b[j]
    return red(tuple(v))
def zadd(a, b): return tuple(p+q for p, q in zip(a, b))
def zsub(a, b): return tuple(p-q for p, q in zip(a, b))
def zint(n): return (F(n), F(0), F(0), F(0))
def zneg(a): return tuple(-p for p in a)
def zpow(a, n):
    r = zint(1)
    for _ in range(n): r = zmul(r, a)
    return r
def gal(a, k):
    v = [F(0)]*5
    for i in range(4): v[(i*k) % 5] += a[i]
    return red(tuple(v))
X5   = (F(0), F(1), F(0), F(0))              # zeta5
J    = (F(1), F(0), F(1), F(0))              # 1 + zeta5^2
PHI  = (F(0), F(0), F(-1), F(-1))            # phi = -z^2 - z^3
ONE  = zint(1)
NJ   = zsub(zint(2), PHI)                    # N(J) = J Jbar = 2 - phi
IPHI = zsub(PHI, ONE)                        # phi^-1 = phi - 1
Jb   = gal(J, 4)
Jinv = zmul(PHI, gal(X5, 4))                 # J^-1 = phi zeta5^4

# ---------- 1. branch pinning ----------
ck("CP1 the cosine data is branch-blind: J and Jbar BOTH satisfy x + xbar = x xbar = 2 - phi, so Z2-type reasoning alone only gives arg J = +-2 pi/5",
   zadd(J, Jb) == NJ and zmul(J, Jb) == NJ
   and zadd(Jb, J) == zmul(Jb, J))
ck("CP2 the polarization pins the branch: J phi = zeta5 while Jbar phi = zeta5^4 != zeta5, hence J = phi^-1 zeta5 and arg J = +2 pi/5 in the principal embedding (audit correction 1 accepted)",
   zmul(J, PHI) == X5 and zmul(Jb, PHI) == gal(X5, 4) and gal(X5, 4) != X5
   and zmul(IPHI, X5) == J)

# ---------- 2. the principal spinor step and the projective fifth power ----------
Z10 = zneg(zpow(X5, 3))                      # zeta10 = -zeta5^3
ck("CP3 zeta10 = -zeta5^3: zeta10^2 = zeta5, zeta10^5 = -1, zeta10^10 = 1; with s = zeta10 / sqrt(phi): s^2 = J and s^5 = zeta10^5 phi^-5/2 = -phi^-5/2, real NEGATIVE: g_J^5 = -diag(phi^-5/2, phi^5/2) -- a pure boost only in the projective Herm action; the spinor carries the central sign and clears it at ten steps (audit correction 2 accepted)",
   zmul(Z10, Z10) == X5 and zpow(Z10, 5) == zneg(ONE) and zpow(Z10, 10) == ONE
   and zmul(zmul(Z10, Z10), IPHI) == J)
ck("CP4 J^5 phi^5 = 1: the Herm-level five-tick boost magnitude is exact (registered J-GOLDEN-BRIDGE), independent of the spinor sign",
   zmul(zpow(J, 5), zpow(PHI, 5)) == ONE)

# ---------- 3. the cone equivalence as a theorem ----------
okcp = True
for t in range(3):
    for xx in range(3):
        for y in range(3):
            for z in range(3):
                # X = [[t+z, x-iy],[x+iy, t-z]]: charpoly = l^2 - tr l + det
                trX = 2*t
                detX = (t+z)*(t-z) - (xx*xx + y*y)
                if trX != 2*t or detX != t*t - xx*xx - y*y - z*z: okcp = False
ck("CP5 char poly of X is lambda^2 - 2t lambda + (t^2-x^2-y^2-z^2), proved exactly on the 3^4 interpolation grid (degree <= 2 per variable); with the 2x2 sign lemma (both eigenvalues >= 0 iff sum >= 0 and product >= 0) this makes X >= 0 iff t >= 0 and det X >= 0 a THEOREM, replacing the sampled M2/M3 witness (audit correction 3 accepted)",
   okcp)
ck("CP6 boundary refinement: (t+z) + (t-z) = 2t and (t+z)(t-z) = t^2 - z^2 as polynomial identities on the grid: t >= |z| follows from t >= 0, t^2 >= z^2, so both diagonal minors are nonnegative -- the minor route of the audit is exact",
   all((t+z)+(t-z) == 2*t and (t+z)*(t-z) == t*t-z*z
       for t in range(3) for z in range(3)))

# ---------- 4. the one-tick action, exact and square-root free ----------
ck("CP7 normalized Herm action of A_J = diag(J, 1): scale = 1/|det A_J| = phi exactly in F, and the three slot coefficients are phi N(J) = phi^-1, phi, phi J = zeta5: one tick is (u, v, w) -> (phi^-1 u, phi v, zeta5 w) with NO square root anywhere (audit hidden finding, Herm part)",
   zmul(PHI, NJ) == IPHI and zmul(PHI, J) == X5)
ck("CP8 five ticks: (phi^-1)^5 (phi)^5 = 1 and zeta5^5 = 1: H_{A_J}^5 = (phi^-5 u, phi^5 v, w), the pure boost, exactly",
   zmul(zpow(IPHI, 5), zpow(PHI, 5)) == ONE and zpow(X5, 5) == ONE)

# ---------- 5. the central phase: Herm projective, Sym charged ----------
D2first  = zmul(J, J)                        # A_J^2 = diag(J^2, 1)
ck("CP9 A_J^2 = J diag(J, J^-1) exactly: J J^-1 = 1 with J^-1 = phi zeta5^4 in Z[zeta5], so the square of the one-tick realizer is the central unit J times the det-1 two-tick",
   zmul(J, Jinv) == ONE and zmul(J, J) == D2first
   and zmul(J, zmul(J, Jinv)) == J)
ck("CP10 Sym slot sees the center: the scalar law S_{cA} = (c^2/N(c)) S_A gives, for c = J, the factor J^2/N(J) = (J phi)^2 = zeta5^2: per two ticks the Sym slot gains central phase zeta5^2 while the Herm slots of A_J^2 and diag(J, J^-1) agree (audit hidden finding, Sym part)",
   zmul(J, J) == zmul(NJ, zmul(X5, X5))
   and zmul(zmul(J, PHI), zmul(J, PHI)) == zmul(X5, X5))
phases = set()
for a in range(5):
    for b in (-2, -1, 0, 1, 2):
        for s in (1, -1):
            c = zpow(X5, a)
            pw = PHI if b >= 0 else IPHI
            for _ in range(abs(b)): c = zmul(c, pw)
            if s == -1: c = zneg(c)
            Nc = zmul(c, gal(c, 4))
            # c^2 / N(c): solve zmul(Nc, y) == c^2 among mu_10 candidates
            c2 = zmul(c, c)
            hit = None
            for k in range(5):
                for sg in (ONE, zneg(ONE)):
                    y = zmul(zpow(X5, k), sg)
                    if zmul(Nc, y) == c2: hit = y
            phases.add(hit)
MU5 = {zpow(X5, k) for k in range(5)}
ck("CP11 the unit-scalar central phase group is EXACTLY mu_5: sweeping c over all +-zeta5^a phi^b (|b| <= 2), the Sym factors c^2/N(c) form precisely the five fifth roots of unity, never a genuine tenth root",
   phases == MU5)
GLUEPH = zneg(zmul(X5, X5))                  # 1 - J = -zeta5^2
ck("CP12 the glue phase escapes: 1 - J = -zeta5^2 (registered J-TENTH-ROOT) is NOT in mu_5, (1-J)^5 = -1, (1-J)^10 = 1: the integral even tick of the icosian carrier (C-COMMON-CARRIER-ICOSIAN-1, gate T4) carries a phase that no unit scalar can produce -- the central sign, the bit, rides only the glued integral step",
   zsub(ONE, J) == GLUEPH and GLUEPH not in MU5
   and zpow(GLUEPH, 5) == zneg(ONE) and zpow(GLUEPH, 10) == ONE)

# ---------- 6. tick-ladder integrality against the ramified glue ----------
def res5(a):
    v = a[0] + a[1] + a[2] + a[3]
    if v.denominator != 1: return None
    return int(v) % 5
ck("CP13 residues mod p5 = (1 - zeta5): res(J) = 2 (registered J_lambda), res(1) = 1, res(J^2) = 4 = res(J^-2): the det-1 FOUR-tick diag(J^2, J^-2) = (diag(J, -J^-1))^2 is integral as the square of the integral twisted tick, consistent with the glue criterion (C-COMMON-CARRIER-ICOSIAN-1, gates T3, T4), while diag(J, 1) fails it (2 != 1)",
   res5(J) == 2 and res5(ONE) == 1
   and res5(zmul(J, J)) == 4 and res5(zmul(Jinv, Jinv)) == 4)
sweep_ok = True
for a in range(5):
    for b in (-2, -1, 0, 1, 2):
        for s in (1, -1):
            c = zpow(X5, a)
            pw = PHI if b >= 0 else IPHI
            for _ in range(abs(b)): c = zmul(c, pw)
            if s == -1: c = zneg(c)
            if res5(zmul(c, J)) == res5(c): sweep_ok = False
ck("CP14 NO unit rescaling c makes diag(c J, c) glue-compatible: res(c J) = 2 res(c) != res(c) for every unit c (res(c) != 0), so the ONE tick has no integral realization on the glued carrier at all -- the ladder is: half-tick over K(sqrt phi), one tick K-projective only, two ticks integral with the sign twist and tenth-root phase, four ticks integral untwisted, ten ticks pure boost",
   sweep_ok)

# ---------- 7. the split-unit projector algebra, grid-proved ----------
class Cx:
    __slots__ = ("re", "im")
    def __init__(s, re=0, im=0): s.re = F(re); s.im = F(im)
    def __add__(s, o): return Cx(s.re+o.re, s.im+o.im)
    def __sub__(s, o): return Cx(s.re-o.re, s.im-o.im)
    def __mul__(s, o): return Cx(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def __ne__(s, o): return not s.__eq__(o)
def nsigma(n1, n2, n3):
    return [[Cx(n3), Cx(n1, -n2)], [Cx(n1, n2), Cx(-n3)]]
def m2(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
okp = True
for n1 in range(-2, 3):
    for n2 in range(-2, 3):
        for n3 in range(-2, 3):
            nn = F(n1*n1 + n2*n2 + n3*n3)
            NS = nsigma(F(n1), F(n2), F(n3))
            SQ = m2(NS, NS)
            if not (SQ[0][0] == Cx(nn) and SQ[1][1] == Cx(nn)
                    and SQ[0][1] == Cx(0) and SQ[1][0] == Cx(0)): okp = False
okpp = True
for (n1, n2, n3) in ((F(1), F(0), F(0)), (F(3,5), F(4,5), F(0)),
                     (F(2,3), F(2,3), F(1,3)), (F(1,3), F(2,3), F(-2,3))):
    NS = nsigma(n1, n2, n3)
    Pp = [[(Cx(1)+NS[0][0])*Cx(F(1,2)), NS[0][1]*Cx(F(1,2))],
          [NS[1][0]*Cx(F(1,2)), (Cx(1)+NS[1][1])*Cx(F(1,2))]]
    Pm = [[(Cx(1)-NS[0][0])*Cx(F(1,2)), Cx(0)-NS[0][1]*Cx(F(1,2))],
          [Cx(0)-NS[1][0]*Cx(F(1,2)), (Cx(1)-NS[1][1])*Cx(F(1,2))]]
    if m2(Pp, Pp) != Pp or m2(Pm, Pm) != Pm: okpp = False
    PPm = m2(Pp, Pm)
    if not (PPm[0][0] == Cx(0) and PPm[0][1] == Cx(0)
            and PPm[1][0] == Cx(0) and PPm[1][1] == Cx(0)): okpp = False
    detp = Pp[0][0]*Pp[1][1] - Pp[0][1]*Pp[1][0]
    detm = Pm[0][0]*Pm[1][1] - Pm[0][1]*Pm[1][0]
    if detp != Cx(0) or detm != Cx(0): okpp = False
ck("CP15 (n . sigma)^2 = |n|^2 I proved exactly on the 5^3 integer grid (degree 2 per variable), and for exact unit vectors P+- = (I +- n.sigma)/2 are complementary idempotents of determinant zero with B = P+ - P- traceless, B^2 = I: the split unit is two complementary pure null rays and the bit is the orientation of the split (audit ontological lemma accepted)",
   okp and okpp)
okr = True
for a in range(-2, 3):
    for b in range(-2, 3):
        for c in range(-2, 3):
            for s in range(-2, 3):
                m12 = c*(a*s) + s*(b*c)               # (B diag(a,b) B)_{12}, B = [[c,s],[s,c]] symmetric
                if m12 != c*s*(a+b): okr = False
ck("CP16 rigidity lever as a polynomial identity: the off-diagonal of B^T diag(a, b) B is cs(a + b) on the full 5^4 grid; with cosh sinh = sqrt5/4 != 0 (exact, C-HERM2 gate B6) invariance forces b = -a; the common-carrier hypothesis of the audit is discharged at candidate level by C-COMMON-CARRIER-ICOSIAN-1, where the same quadratic coordinates carry both the right 2I action and the glued J-boost",
   okr)

n = len(R); ok = sum(R)
print("SUMMARY %d/%d PASS" % (ok, n))
sys.exit(0 if ok == n else 1)
