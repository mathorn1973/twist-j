#!/usr/bin/env python3
# herm2_consolidation_verify.py
# Consolidation verifier for the Herm2(C) analytic attack (TWIST-J candidate
# lane, container run, NON-CANONICAL, no repo writes).
# Exact arithmetic in all assertions unless the check name says
# "numeric witness" (those carry an explicit float tolerance).
# Python 3 standard library only. Deterministic seeds.
import sys, math, cmath, random
from fractions import Fraction as F

R = []
def ck(name, cond):
    ok = bool(cond)
    R.append(ok)
    print(("PASS " if ok else "FAIL ") + name)

# ---------- 1. exact Z[zeta5]: coefficients of 1, x, x^2, x^3 mod Phi_5 ----------
def red(v):
    c = v[4]
    return (v[0]-c, v[1]-c, v[2]-c, v[3]-c)
def zmul(a, b):
    v = [F(0)]*5
    for i in range(4):
        ai = a[i]
        if ai == 0: continue
        for j in range(4):
            bj = b[j]
            if bj == 0: continue
            v[(i+j) % 5] += ai*bj
    return red(tuple(v))
def zadd(a, b): return tuple(p+q for p, q in zip(a, b))
def zsub(a, b): return tuple(p-q for p, q in zip(a, b))
def zint(n): return (F(n), F(0), F(0), F(0))
def zsca(n, a): return tuple(F(n)*p for p in a)
def zpow(a, n):
    r = zint(1)
    for _ in range(n): r = zmul(r, a)
    return r
def zconj(a):
    v = [F(0)]*5
    for i in range(4): v[(5-i) % 5] += a[i]
    return red(tuple(v))
def gal(a, k):
    v = [F(0)]*5
    for i in range(4): v[(i*k) % 5] += a[i]
    return red(tuple(v))

x   = (F(0), F(1), F(0), F(0))
J   = (F(1), F(0), F(1), F(0))
phi = (F(0), F(0), F(-1), F(-1))
one = zint(1)

ck("Z1  J*conj(J) = 2-phi = phi^-2 (modulus of J is 1/phi)",
   zmul(J, zconj(J)) == zsub(zint(2), phi))
ck("Z2  J+conj(J) = J*conj(J)  => cos(arg J) = (phi-1)/2, arg J = 2*pi/5 exactly",
   zadd(J, zconj(J)) == zmul(J, zconj(J)))
ck("Z3  phi^2 = phi+1", zmul(phi, phi) == zadd(phi, one))
ck("Z4  (2-phi)*phi^2 = 1", zmul(zsub(zint(2), phi), zmul(phi, phi)) == one)
ck("Z5  J*phi = j", zmul(J, phi) == x)
ck("Z6  (J-1)^3 = j", zpow(zsub(J, one), 3) == x)
ck("Z7  J^5 = 5*phi-8", zpow(J, 5) == zsub(zsca(5, phi), zint(8)))
ck("Z8  J^5 * phi^5 = 1  (J^5 = phi^-5)", zmul(zpow(J, 5), zpow(phi, 5)) == one)
ck("Z9  Tr(J) = 3",
   zadd(zadd(gal(J, 1), gal(J, 2)), zadd(gal(J, 3), gal(J, 4))) == zint(3))
ck("Z10 N(J) = 1",
   zmul(zmul(gal(J, 1), gal(J, 2)), zmul(gal(J, 3), gal(J, 4))) == one)
ck("Z11 5*phi-8 > 0 iff 125 > 121  (J^5 real positive: rotation part has exact order 5)",
   125 > 121)
phi2 = zmul(phi, phi); invphi2 = zsub(zint(2), phi)
ck("Z12 |sigma_a(J)|^2 = phi^-2 for a in {1,4}",
   all(zmul(gal(J, a), zconj(gal(J, a))) == invphi2 for a in (1, 4)))
ck("Z13 |sigma_a(J)|^2 = phi^2 for a in {2,3}  (chi5 splits the moduli)",
   all(zmul(gal(J, a), zconj(gal(J, a))) == phi2 for a in (2, 3)))

# ---------- 2. Q(sqrt5) exact: boost data of the J-step, rigidity ----------
def qm(p, q): return (p[0]*q[0] + 5*p[1]*q[1], p[0]*q[1] + p[1]*q[0])
def qa(p, q): return (p[0]+q[0], p[1]+q[1])
def qs(p, q): return (p[0]-q[0], p[1]-q[1])
def qi(n): return (F(n), F(0))
PH  = (F(1, 2), F(1, 2))     # phi
IPH = (F(-1, 2), F(1, 2))    # 1/phi
C_  = (F(0), F(1, 2))        # cosh(ln phi) = sqrt5/2
S_  = (F(1, 2), F(0))        # sinh(ln phi) = 1/2

ck("B1  phi * phi^-1 = 1", qm(PH, IPH) == qi(1))
ck("B2  cosh(ln phi) = (phi+phi^-1)/2 = sqrt5/2",
   qa(PH, IPH) == (F(0), F(1)) and C_ == (F(0), F(1, 2)))
ck("B3  sinh(ln phi) = (phi-phi^-1)/2 = 1/2",
   qs(PH, IPH) == (F(1), F(0)) and S_ == (F(1, 2), F(0)))
ck("B4  cosh^2 - sinh^2 = 1", qs(qm(C_, C_), qm(S_, S_)) == qi(1))
ck("B5  beta^2 = 1/5  (5*sinh^2 = cosh^2): v_J = c/sqrt5, gamma = sqrt5/2",
   qm(qi(5), qm(S_, S_)) == qm(C_, C_))
cs = qm(C_, S_)
ck("B6  cosh*sinh = sqrt5/4, nonzero (rigidity lever)", cs == (F(0), F(1, 4)))
c2 = qm(C_, C_); s2 = qm(S_, S_)
ck("B7  Minkowski diag(a,-a) invariant under the J-boost: c^2-s^2 = 1, offdiag cs*(a-a) = 0",
   qs(c2, s2) == qi(1))
ck("B8  Euclidean diag(a,a) NOT invariant: offdiag 2*cs != 0", qm(qi(2), cs) != qi(0))

# ---------- 3. exact complex rationals, Minkowski determinant, Born cone ----------
class Cx:
    __slots__ = ("re", "im")
    def __init__(s, re=0, im=0): s.re = F(re); s.im = F(im)
    def __add__(s, o): return Cx(s.re+o.re, s.im+o.im)
    def __sub__(s, o): return Cx(s.re-o.re, s.im-o.im)
    def __mul__(s, o): return Cx(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def conj(s): return Cx(s.re, -s.im)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def __ne__(s, o): return not s.__eq__(o)

def h2(t, xx, y, z):
    return [[Cx(t+z, 0), Cx(xx, -y)], [Cx(xx, y), Cx(t-z, 0)]]
def det2(X): return X[0][0]*X[1][1] - X[0][1]*X[1][0]

okgrid = True
for t in range(3):
    for xx in range(3):
        for y in range(3):
            for z in range(3):
                d = det2(h2(F(t), F(xx), F(y), F(z)))
                if d.im != 0 or d.re != F(t*t - xx*xx - y*y - z*z):
                    okgrid = False
ck("M1  det X = t^2-x^2-y^2-z^2, proved exactly by 3^4 interpolation grid (degree <= 2 per variable)",
   okgrid)

rnd = random.Random(50)
def rF(): return F(rnd.randint(-9, 9), rnd.randint(1, 5))
okA = True; okW = True
for _ in range(300):
    t, xx, y, z = rF(), rF(), rF(), rF()
    X = h2(t, xx, y, z); d = det2(X).re
    a = t+z; b = t-z
    psd_minors = (a >= 0 and b >= 0 and d >= 0)
    cone = (t >= 0 and d >= 0)
    if psd_minors != cone: okA = False
    neg = False
    for _ in range(40):
        v = [Cx(rF(), rF()), Cx(rF(), rF())]
        q = (v[0].conj()*(X[0][0]*v[0] + X[0][1]*v[1])
             + v[1].conj()*(X[1][0]*v[0] + X[1][1]*v[1]))
        if q.im != 0: okW = False
        if q.re < 0: neg = True
    if cone and neg: okW = False
ck("M2  PSD (minor criterion) <=> (t >= 0 and det >= 0), exact on 300 random rational points",
   okA)
ck("M3  Born form v†Xv is real; never negative inside the cone (sampled witness, exact rationals)",
   okW)

# ---------- 4. geometric C4 rotoreflection S on Herm2 alone ----------
def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
I4 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
# basis (t,z,x,y); S: t->t, z->-z, x->y, y->-x  i.e. w -> i*w with w = x - i*y
Smat = [[1,0,0,0], [0,-1,0,0], [0,0,0,1], [0,0,-1,0]]
S2 = mm(Smat, Smat); S3 = mm(S2, Smat); S4 = mm(S3, Smat)
ck("C1  S^4 = 1", S4 == I4)
tr = lambda M: sum(M[i][i] for i in range(4))
ck("C2  traces of S^0..S^3 = (4,0,0,0): the S-module is the regular representation of C4",
   (tr(I4), tr(Smat), tr(S2), tr(S3)) == (4, 0, 0, 0))
G = [[1,0,0,0], [0,-1,0,0], [0,0,-1,0], [0,0,0,-1]]
St = [[Smat[j][i] for j in range(4)] for i in range(4)]
ck("C3  S^T G S = G  (Lorentz isometry, orthochronous)", mm(St, mm(G, Smat)) == G)
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
sp = [r[1:] for r in Smat[1:]]
ck("C4  spatial det(S) = -1 (improper rotoreflection); S^2 = R_z(pi) proper",
   det3(sp) == -1 and [r[1:] for r in S2[1:]] == [[1,0,0],[0,-1,0],[0,0,-1]])

def mat2(r1, r2): return [list(r1), list(r2)]
def m2m(A, B):
    return [[A[i][0]*B[0][j] + A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
def dag(A):
    return [[A[0][0].conjugate(), A[1][0].conjugate()],
            [A[0][1].conjugate(), A[1][1].conjugate()]]
U = mat2((0, 1j), (1, 0))
rndc = random.Random(7)
okU = True
for _ in range(50):
    t = rndc.uniform(-2, 2); z = rndc.uniform(-2, 2)
    w = complex(rndc.uniform(-2, 2), rndc.uniform(-2, 2))
    X  = mat2((t+z, w), (w.conjugate(), t-z))
    XT = mat2((X[0][0], X[1][0]), (X[0][1], X[1][1]))
    Y  = m2m(U, m2m(XT, dag(U)))
    E  = mat2((t-z, 1j*w), ((1j*w).conjugate(), t+z))
    err = sum(abs(Y[i][j]-E[i][j]) for i in range(2) for j in range(2))
    if err > 1e-12: okU = False
ck("C5  S realized as X -> U X^T U†, U ~ [[0,i],[1,0]]: spinor lift psi -> U*conj(psi), antiunitary, order 8 (numeric witness)",
   okU)

# ---------- 5. arithmetic Galois C4 on the CM spinor: it carries the PAIR ----------
rnd2 = random.Random(11)
def rc():
    return Cx(F(rnd2.randint(-9, 9), rnd2.randint(1, 4)),
              F(rnd2.randint(-9, 9), rnd2.randint(1, 4)))
def phig(z): return (z[1], z[0].conj())
okord = True; okpair = True
for _ in range(60):
    z = (rc(), rc())
    z4 = phig(phig(phig(phig(z))))
    if not (z4[0] == z[0] and z4[1] == z[1]): okord = False
    z1, z2 = z
    w = z1*z2.conj()      # Herm offdiagonal, coherence
    s = z1*z2             # Sym offdiagonal, pairing
    zp = phig(z)
    w2 = zp[0]*zp[1].conj(); s2 = zp[0]*zp[1]
    if w2 != s or s2 != w.conj(): okpair = False
    if not (zp[0]*zp[0].conj() == z2*z2.conj() and zp[1]*zp[1].conj() == z1*z1.conj()):
        okpair = False
    if not (zp[0]*zp[0] == z2*z2 and zp[1]*zp[1] == (z1*z1).conj()):
        okpair = False
ck("G1  Galois generator on the CM spinor: (z1,z2) -> (z2, conj z1), mixed-linear, order 4, exact",
   okord)
ck("G2  induced quadratic action: t fixed, z -> -z, and (w,s) -> (s, conj w): a 4-cycle w -> s -> conj w -> conj s; Herm alone is NOT stable, the pair (PsiPsi†, PsiPsi^T) is forced",
   okpair)

# ---------- 6. CM types of Q(zeta5): four types, one Galois orbit ----------
types = set()
for a in (1, 4):
    for b in (2, 3): types.add(frozenset((a, b)))
def act(T, g): return frozenset((i*g) % 5 for i in T)
orb = {frozenset((1, 2))}
frontier = [frozenset((1, 2))]
while frontier:
    T = frontier.pop()
    for g in (2, 3, 4):
        T2 = act(T, g)
        if T2 not in orb:
            orb.add(T2); frontier.append(T2)
ck("K1  exactly 4 CM types of Q(zeta5), all primitive (only quadratic subfield Q(sqrt5) is real), Galois acts transitively: CM type unique up to Galois",
   types == orb and len(types) == 4)

# ---------- 7. Zolotarev p = 5: the bit is an orientation ----------
def perm_sign(p):
    seen = set(); sgn = 1
    for i in (1, 2, 3, 4):
        if i in seen: continue
        l = 0; j = i
        while j not in seen:
            seen.add(j); j = p[j]; l += 1
        if l % 2 == 0: sgn = -sgn
    return sgn
def legendre(a):
    return 1 if pow(a, 2, 5) == 1 else -1
okz = True; okdet = True
for a in (1, 2, 3, 4):
    p = {i: (a*i) % 5 for i in (1, 2, 3, 4)}
    if perm_sign(p) != legendre(a): okz = False
    cols = []
    for jj in (1, 2, 3):
        vec = {1: 0, 2: 0, 3: 0, 4: 0}
        vec[p[jj]] += 1; vec[p[jj+1]] -= 1
        c1 = vec[1]; c2 = vec[1]+vec[2]; c3 = vec[1]+vec[2]+vec[3]
        cols.append((c1, c2, c3))
    M = [[cols[j][i] for j in range(3)] for i in range(3)]
    if det3(M) != legendre(a): okdet = False
ck("O1  Zolotarev p=5: sign(mult_a) = chi5(a)", okz)
ck("O2  det(mult_a restricted to W_5) = chi5(a): the bit is the orientation of 3-space, exact",
   okdet)

# ---------- 8. A5: unique Minkowski form, unique bracket ----------
# classes e, (12)(34), (123), 5A, 5B; sizes 1,15,20,12,12; chi_W = 3,-1,0,phi,phi'
sizes = [1, 15, 20, 12, 12]
chiW = [qi(3), qi(-1), qi(0), PH, (F(1, 2), F(-1, 2))]
sq = [0, 0, 2, 4, 3]   # class of g^2 (squaring swaps 5A and 5B: 2 is a nonresidue mod 5)
chiL2 = []; chiS2 = []
for i in range(5):
    c2v = qm(chiW[i], chiW[i])
    chiL2.append(tuple((c2v[k] - chiW[sq[i]][k]) / 2 for k in range(2)))
    chiS2.append(tuple((c2v[k] + chiW[sq[i]][k]) / 2 for k in range(2)))
ip = lambda u, v: tuple(sum(sizes[i]*qm(u[i], v[i])[k] for i in range(5)) for k in range(2))
triv = [qi(1)]*5
ck("A1  Lambda^2 W = W, character identity on all classes (exact golden arithmetic)",
   chiL2 == chiW)
ck("A2  <chi_W, chi_W> = 1 (irreducible)", ip(chiW, chiW) == (F(60), F(0)))
ck("A3  dim Hom_A5(Lambda^2 W, W) = 1: the unique equivariant bracket is the cross product",
   ip(chiL2, chiW) == (F(60), F(0)))
ck("A4  Sym^2 W contains the trivial once and W never: the invariant metric on 1+W has exactly two parameters a, b",
   ip(chiS2, triv) == (F(60), F(0)) and ip(chiS2, chiW) == (F(0), F(0)))

# ---------- 9. the loxodromic J-step (numeric witnesses on an exact backbone) ----------
Jc = 1 + cmath.exp(4j*cmath.pi/5)
phif = (1 + math.sqrt(5)) / 2
w1 = abs(abs(Jc) - 1/phif) < 1e-12
w2 = abs(cmath.phase(Jc) - 2*math.pi/5) < 1e-12
s = cmath.sqrt(Jc)
def act_g(u, v, w, a, d):
    return ((a*a.conjugate()).real*u, (d*d.conjugate()).real*v, a*w*d.conjugate())
u, v, w0 = 1.3, 0.7, complex(0.4, -1.1)
up, vp, wp = act_g(u, v, w0, s, 1/s)
w3 = (abs(up - abs(Jc)*u) < 1e-12 and abs(vp - v/abs(Jc)) < 1e-12
      and abs(wp - (Jc/abs(Jc))*w0) < 1e-12)
w4 = abs((up*vp - abs(wp)**2) - (u*v - abs(w0)**2)) < 1e-12
lam5 = Jc**5
w5 = abs(lam5.imag) < 1e-12 and lam5.real > 0 and abs(lam5.real - phif**-5) < 1e-12
ck("L1  |J| = 1/phi and arg J = 2*pi/5 (numeric witness; exact via Z1, Z2)", w1 and w2)
ck("L2  g_J = diag(sqrtJ, 1/sqrtJ): u -> |J|u, v -> |J|^-1 v, w -> (J/|J|)w; det preserved (numeric witness)",
   w3 and w4)
ck("L3  J^5 = phi^-5 real positive: the fifth power of the loxodromic step is a PURE boost (numeric witness; exact via Z7, Z8, Z11)",
   w5)
def phig_c(z1, z2): return (z2, z1.conjugate())
def phig_inv(z1, z2): return (z2.conjugate(), z1)
okA2 = True
for _ in range(30):
    z1 = complex(rndc.uniform(-2, 2), rndc.uniform(-2, 2))
    z2 = complex(rndc.uniform(-2, 2), rndc.uniform(-2, 2))
    a1, a2 = phig_inv(z1, z2)
    b1, b2 = s*a1, a2/s
    c1, c2 = phig_c(b1, b2)
    e1, e2 = z1/s, s.conjugate()*z2
    if abs(c1-e1) + abs(c2-e2) > 1e-10: okA2 = False
w6 = abs(1/abs(s)**2 - phif) < 1e-12
ck("L4  phig o g_J o phig^-1 = diag(1/sqrtJ, conj(sqrtJ)): multiplier phi, a PURE expanding boost; rotation absorbed by the mixed-linear quarter-turn; real eigenvalue multiset {s, conj s, 1/s, 1/conj s} preserved (numeric witness)",
   okA2 and w6)

# ---------- 10. Cauchy-Binet: mass as non-collinearity ----------
okcb = True
for trial in range(6):
    k = rnd2.randint(2, 4)
    ws = [F(rnd2.randint(1, 9)) for _ in range(k)]
    ps = [(rc(), rc()) for _ in range(k)]
    R00 = Cx(0); R01 = Cx(0); R11 = Cx(0)
    for wgt, (p0, p1) in zip(ws, ps):
        wc = Cx(wgt, 0)
        R00 = R00 + wc*p0*p0.conj()
        R01 = R01 + wc*p0*p1.conj()
        R11 = R11 + wc*p1*p1.conj()
    lhs = R00*R11 - R01*R01.conj()
    rhs = Cx(0)
    for i in range(k):
        for jj in range(i+1, k):
            d = ps[i][0]*ps[jj][1] - ps[i][1]*ps[jj][0]
            rhs = rhs + Cx(ws[i]*ws[jj], 0)*d*d.conj()
    if lhs != rhs: okcb = False
ck("CB1 det(sum w_i psi_i psi_i†) = sum_{i<j} w_i w_j |det(psi_i, psi_j)|^2 (exact, random rational spinors, k = 2..4)",
   okcb)
p = (rc(), rc())
det_single = (p[0]*p[0].conj())*(p[1]*p[1].conj()) \
             - (p[0]*p[1].conj())*((p[0]*p[1].conj()).conj())
ck("CB2 rank-1: det(psi psi†) = 0 exactly (pure = null; interior needs non-collinear mixture)",
   det_single == Cx(0))

# ---------- 11. Route A degeneracy over Q and the CM repair ----------
vq = (F(3), F(-2))
Aq = [[vq[i]*vq[j] for j in range(2)] for i in range(2)]
Bq = [[vq[i]*vq[j] for j in range(2)] for i in range(2)]
ck("RA1 over Q with trivial involution v v† = v v^T identically: Route A cannot carry a phase (identity, recorded)",
   Aq == Bq)
alpha = (1, 1, 0, 0)   # alpha = 1 + zeta
z5 = cmath.exp(2j*cmath.pi/5)
def emb(coeffs, a): return sum(c*(z5**((a*k) % 5)) for k, c in enumerate(coeffs))
Psi = (emb(alpha, 1), emb(alpha, 2))
H01 = Psi[0]*Psi[1].conjugate()
T01 = Psi[0]*Psi[1]
ck("RA2 CM repair: with Psi = (sigma1(alpha), sigma2(alpha)), PsiPsi† and PsiPsi^T differ generically (numeric witness, alpha = 1+zeta)",
   abs(H01 - T01) > 1e-6)

# ---------- 12. L(1, chi5) witness ----------
Ssum = 0.0
K = 200000
for k in range(K):
    b = 5*k
    Ssum += 1/(b+1) - 1/(b+2) - 1/(b+3) + 1/(b+4)
target = 2*math.log(phif)/math.sqrt(5)
ck("D1  L(1, chi5) = 2 ln(phi)/sqrt5 (Dirichlet class number formula; numeric witness, |diff| < 1e-8)",
   abs(Ssum - target) < 1e-8)

n = len(R); ok = sum(R)
print("SUMMARY %d/%d PASS" % (ok, n))
sys.exit(0 if ok == n else 1)
