#!/usr/bin/env python3
"""verify_lambda_grid_audit_1.py

Independent audit verifier for the angular clause of LAMBDA-COCYCLE-ANGLES [H]
and its theorem companions, per PREREG-AUDIT-LAMBDA-GRID-1 (sha256
39a3ef65576e14f41d1b408f5d662d85375f4dfb025c46a63e5dfec94230c215).

Representation: circulant 5-vectors over Z in Z[x]/(x^5 - 1); the class of an
element of Z[zeta_5] is its coset modulo the constant vector (the Phi_5 ideal
contribution). This is deliberately not the 4-tuple basis of the sealed public
probes. Exact integer and Fraction arithmetic only. No float is formed.
"""

from fractions import Fraction
import sys

CHECKS = []
CONJ = []


def check(label, cond):
    CHECKS.append((label, bool(cond)))


def conj(label, cond):
    CONJ.append((label, bool(cond)))


# ---------------------------------------------------------------------------
# circulant ring
# ---------------------------------------------------------------------------

def cmul(a, b, mod=None):
    r = [0, 0, 0, 0, 0]
    for i in range(5):
        ai = a[i]
        if ai:
            for j in range(5):
                r[(i + j) % 5] += ai * b[j]
    if mod is not None:
        r = [x % mod for x in r]
    return tuple(r)


def cadd(a, b, mod=None):
    r = [a[i] + b[i] for i in range(5)]
    if mod is not None:
        r = [x % mod for x in r]
    return tuple(r)


def csub(a, b, mod=None):
    r = [a[i] - b[i] for i in range(5)]
    if mod is not None:
        r = [x % mod for x in r]
    return tuple(r)


def cscal(k, a, mod=None):
    r = [k * a[i] for i in range(5)]
    if mod is not None:
        r = [x % mod for x in r]
    return tuple(r)


def canon(a, mod=None):
    t = a[4]
    r = [a[i] - t for i in range(5)]
    if mod is not None:
        r = [x % mod for x in r]
    return tuple(r)


def ceq(a, b, mod=None):
    d = canon(csub(a, b))
    if mod is None:
        return all(x == 0 for x in d)
    return all(x % mod == 0 for x in d)


def sigma(a, s):
    r = [0, 0, 0, 0, 0]
    for i in range(5):
        r[(i * s) % 5] += a[i]
    return tuple(r)


def cpow(a, e, mod=None):
    result = ONE
    base = a
    while e:
        if e & 1:
            result = cmul(result, base, mod)
        base = cmul(base, base, mod)
        e >>= 1
    return result


def zpow(k):
    r = [0, 0, 0, 0, 0]
    r[k % 5] = 1
    return tuple(r)


ZERO = (0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0)
Z1 = zpow(1)
J = (1, 0, 1, 0, 0)                 # 1 + zeta^2
PHI = (0, 0, -1, -1, 0)             # -zeta^2 - zeta^3
LAM = (1, -1, 0, 0, 0)              # 1 - zeta
UU = (0, -1, 1, -1, 0)              # -zeta + zeta^2 - zeta^3


def rat_of(a, mod=None):
    c = canon(a, mod)
    if mod is None:
        if c[1] == 0 and c[2] == 0 and c[3] == 0:
            return c[0]
        return None
    if c[1] % mod == 0 and c[2] % mod == 0 and c[3] % mod == 0:
        return c[0] % mod
    return None


def norm(a, mod=None):
    p = ONE
    for s in (1, 2, 3, 4):
        p = cmul(p, sigma(a, s), mod)
    return rat_of(p, mod)


def trace(a):
    t = ZERO
    for s in (1, 2, 3, 4):
        t = cadd(t, sigma(a, s))
    return rat_of(t)


def residue_mod_lambda(a):
    # zeta -> 1; well defined on classes because the constant vector maps to 5c = 0 mod 5
    return sum(a) % 5


def v5(n):
    v = 0
    while n % 5 == 0:
        n //= 5
        v += 1
    return v


PREC = 5 ** 40
VCAP = 30


def vlam(a_modded):
    """lambda-adic valuation via v_5(N(.)), for a class given mod 5^40."""
    r = norm(a_modded, PREC)
    if r is None or r == 0:
        raise AssertionError("vlam: norm not decidable at this precision")
    v = v5(r)
    if v > VCAP:
        raise AssertionError("vlam: valuation above declared cap")
    return v


# ---------------------------------------------------------------------------
# grid membership on Fraction turns
# ---------------------------------------------------------------------------

def strip5(q):
    while q % 5 == 0:
        q //= 5
    return q


def in_grid(fr):
    q = (fr % 1).denominator
    return 4 % strip5(q) == 0


def in_half_lattice(fr):
    q = (fr % 1).denominator
    return 2 % strip5(q) == 0


def level_of(fr):
    q = (fr % 1).denominator
    a = 0
    while q % 5 == 0:
        q //= 5
        a += 1
    return a


# ---------------------------------------------------------------------------
# Z[phi] pairs (a + b phi with Fraction a, b), phi^2 = phi + 1
# ---------------------------------------------------------------------------

def pmul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def padd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def psub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def pscal(k, x):
    return (k * x[0], k * x[1])


def pinv(x):
    a, b = x
    n = a * a + a * b - b * b
    if n == 0:
        raise AssertionError("pinv of zero-norm element")
    return (Fraction(a + b, 1) / n, Fraction(-b, 1) / n)


P_ZERO = (Fraction(0), Fraction(0))
P_ONE = (Fraction(1), Fraction(0))


# ---------------------------------------------------------------------------
# polynomial pairs over Q for the symbolic ordinate g: complex values as
# (real poly, imag poly), each poly a coefficient list
# ---------------------------------------------------------------------------

def pol(*coeffs):
    return [Fraction(c) for c in coeffs]


def pol_add(p, q):
    n = max(len(p), len(q))
    return [ (p[i] if i < len(p) else Fraction(0)) + (q[i] if i < len(q) else Fraction(0)) for i in range(n) ]


def pol_sub(p, q):
    n = max(len(p), len(q))
    return [ (p[i] if i < len(p) else Fraction(0)) - (q[i] if i < len(q) else Fraction(0)) for i in range(n) ]


def pol_mul(p, q):
    r = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return r


def pol_eq(p, q):
    d = pol_sub(p, q)
    return all(c == 0 for c in d)


def cx_mul(x, y):
    xr, xi = x
    yr, yi = y
    return (pol_sub(pol_mul(xr, yr), pol_mul(xi, yi)),
            pol_add(pol_mul(xr, yi), pol_mul(xi, yr)))


def cx_add(x, y):
    return (pol_add(x[0], y[0]), pol_add(x[1], y[1]))


def cx_sub(x, y):
    return (pol_sub(x[0], y[0]), pol_sub(x[1], y[1]))


def cx_eq(x, y):
    return pol_eq(x[0], y[0]) and pol_eq(x[1], y[1])


# ---------------------------------------------------------------------------
# A1 ring anchors and the template chain
# ---------------------------------------------------------------------------

check("A1-01 J phi = zeta", ceq(cmul(J, PHI), Z1))
check("A1-02 N(J) = 1", norm(J) == 1)
check("A1-03 Tr(J) = 3", trace(J) == 3)
check("A1-04 (J-1)^3 = zeta", ceq(cpow(csub(J, ONE), 3), Z1))
check("A1-05 J = 2 mod lambda", residue_mod_lambda(canon(J)) == 2)
check("A1-06 lambda^4 = 5 u with u = -z+z^2-z^3", ceq(cpow(LAM, 4), cscal(5, UU)))
check("A1-07 u is a unit, N(u) = 1", norm(UU) == 1)

rou = []
for s in (1, -1):
    for k in range(5):
        rou.append(cscal(s, zpow(k)))
check("A1-08 J is none of the ten roots of unity", all(not ceq(J, r) for r in rou))

XI = cscal(-1, zpow(3))             # -zeta^3
check("A1-09 Cayley triangle: (1 - J)(-zeta^3) = 1", ceq(cmul(csub(ONE, J), XI), ONE))

RHO = cmul(PHI, Z1)                 # phi zeta
check("A1-10 rho_T (1 + zeta^3) = 1", ceq(cmul(RHO, cadd(ONE, zpow(3))), ONE))
check("A1-11 rho_T + conj(rho_T) = 1", rat_of(cadd(RHO, sigma(RHO, 4))) == 1)
check("A1-12 |rho_T|^2 = phi^2", ceq(cmul(RHO, sigma(RHO, 4)), cmul(PHI, PHI)))
check("A1-13 1 - 1/rho_T = -zeta^3, as rho_T - 1 = -zeta^3 rho_T",
      ceq(csub(RHO, ONE), cmul(XI, RHO)))

# order and turn of xi = -zeta^3
xi_orders = [n for n in range(1, 21) if ceq(cpow(XI, n), ONE)]
check("A1-14 order of -zeta^3 is 10", xi_orders and xi_orders[0] == 10)
check("A1-15 turn 1/10 lies on the grid", in_grid(Fraction(1, 10)))

# cot^2(pi/10) = 4 phi^2 - 1 = 4 phi + 3 in Z[phi]
lhs = psub(pscal(4, pmul((Fraction(0), Fraction(1)), (Fraction(0), Fraction(1)))), P_ONE)
rhs = padd(pscal(4, (Fraction(0), Fraction(1))), (Fraction(3), Fraction(0)))
check("A1-16 4 phi^2 - 1 = 4 phi + 3 in Z[phi]", lhs == rhs)

check("A1-17 uniformizer identity (1 - zeta^4)(-zeta) = 1 - zeta",
      ceq(cmul(csub(ONE, zpow(4)), cscal(-1, Z1)), LAM))
# hence e^(2 i theta) = -zeta for theta = arg lambda; both half-angle branches:
for br in (Fraction(7, 20), Fraction(17, 20)):
    check("A1-18 lambda turn branch %s on grid" % br, in_grid(br))
    check("A1-19 lambda turn branch %s not in (1/2) Z[1/5]" % br, not in_half_lattice(br))
# quadrant sign certificate for the branch 17/20 (fourth quadrant):
pol_phi = lambda x: x * x - x - 1
check("A1-20 phi sandwich certificate p(3/2) < 0 < p(2)",
      pol_phi(Fraction(3, 2)) < 0 and pol_phi(Fraction(2)) > 0)

# ---------------------------------------------------------------------------
# A2 orbit and valuation structure, independent recomputation
# ---------------------------------------------------------------------------

JMOD = tuple(x % PREC for x in J)

ladder = []
for m in range(0, 7):
    z = cpow(JMOD, 4 * 5 ** m, PREC)
    ladder.append(vlam(csub(z, ONE, PREC)))

check("A2-01 v_lambda(J^4 - 1) = 1", ladder[0] == 1)
check("A2-02 v_lambda(J^20 - 1) = 6", ladder[1] == 6)
check("A2-03 v_lambda(J^(4.5^m) - 1) = 4m + 2 for m = 2..6",
      all(ladder[m] == 4 * m + 2 for m in range(2, 7)))
check("A2-04 ladder strictly increasing", all(ladder[i] < ladder[i + 1] for i in range(6)))

def ord_lambda_k(k):
    # least divisor d = 2^e 5^f of 4 * 5^(k-1) with v_lambda(J^d - 1) >= k
    divisors = sorted(2 ** e * 5 ** f for e in range(3) for f in range(k))
    for d in divisors:
        z = cpow(JMOD, d, PREC)
        r = norm(csub(z, ONE, PREC), PREC)
        if r is None:
            continue
        if r == 0:
            return d  # valuation beyond precision, certainly >= k for k <= 14
        if v5(r) >= k:
            return d
    return None

ord_table = {k: ord_lambda_k(k) for k in range(1, 15)}

check("A2-05 ord_lambda(J) = 4", ord_table[1] == 4)
check("A2-06 registered ord_(lambda^(4m))(J) = 4.5^m at m = 1, 2, 3",
      ord_table[4] == 20 and ord_table[8] == 100 and ord_table[12] == 500)
check("A2-07 every orbit length is 4 times a power of 5",
      all(d is not None and d % 4 == 0 and strip5(d // 4) == 1 for d in ord_table.values()))
check("A2-08 n_0 = 4 occurs at level 1 and only at level 1",
      ord_table[1] == 4 and all(ord_table[k] > 4 for k in range(2, 15)))
check("A2-09 unit group order 4.5^(k-1) is a multiple of every orbit length",
      all((4 * 5 ** (k - 1)) % ord_table[k] == 0 for k in range(1, 15)))

# the audit's own frozen closed-form conjecture, tested honestly:
conj("CONJ-A2 ord_(lambda^k)(J) = 4.5^ceil((k-1)/4) for k = 1..14",
     all(ord_table[k] == 4 * 5 ** ((k - 1 + 3) // 4) for k in range(1, 15)))

measured_form = all(
    ord_table[k] == 4 * 5 ** (max(1, (k - 2 + 3) // 4) if k >= 2 else 0)
    for k in range(1, 15))
check("A2-10 measured closed form ord = 4.5^(max(1, ceil((k-2)/4))) for k >= 2, 4 at k = 1",
      measured_form)

# ---------------------------------------------------------------------------
# A3 grid canonicity three ways, denominators up to 500
# ---------------------------------------------------------------------------

orbit_lengths = sorted(set(ord_table.values())) + [1]
S1 = set()
for d in orbit_lengths:
    for j in range(d):
        S1.add(Fraction(j, d) % 1)

S2 = set()
for e in range(3):
    for f in range(4):
        q = 2 ** e * 5 ** f
        for p in range(q):
            fr = Fraction(p, q) % 1
            if fr.denominator == q:
                S2.add(fr)
S2 = set(fr for fr in S2)

def realizable(q):
    return 4 % strip5(q) == 0

S3 = set()
for q in range(1, 501):
    if realizable(q) and 500 % q == 0:
        for p in range(q):
            if Fraction(p, q).denominator == q:
                S3.add(Fraction(p, q) % 1)

check("A3-01 orbit set equals arithmetic set (denominators to 500)", S1 == S2)
check("A3-02 orbit set equals realizability set (denominators to 500)", S1 == S3)

# torsion certificates
roots4 = [t for t in range(5) if (t ** 4 - 1) % 5 == 0]
check("A3-03 x^4 - 1 has the four simple roots 1..4 mod 5",
      roots4 == [1, 2, 3, 4] and all((4 * t ** 3) % 5 != 0 for t in roots4))

t = 2
mod = 5
for _ in range(8):
    mod = mod * mod
    if mod > 5 ** 64:
        mod = 5 ** 64
    inv = pow((2 * t) % mod, -1, mod)
    t = (t - (t * t + 1) * inv) % mod
T60 = 5 ** 60
t %= T60
check("A3-04 Hensel: i in Z_5, t = 2 mod 5, t^2 + 1 = 0 mod 5^60",
      t % 5 == 2 and (t * t + 1) % T60 == 0)

check("A3-05 mu_3 obstruction: x^2 + x + 1 has no root mod 5",
      all((x * x + x + 1) % 5 != 0 for x in range(5)))
check("A3-06 mu_8 obstruction: x^4 + 1 has no root mod 5",
      all((x ** 4 + 1) % 5 != 0 for x in range(5)))

def cyclotomic_5k(k):
    # Phi_{5^k}(x) = sum_{t<5} x^(5^(k-1) t) as coefficient list
    n = 5 ** (k - 1)
    deg = 4 * n
    c = [0] * (deg + 1)
    for tt in range(5):
        c[n * tt] = 1
    return c

def shift_poly(c):
    # p(x+1) via Horner with polynomial coefficients
    res = [0]
    for coeff in reversed(c):
        # res = res * (x+1) + coeff
        new = [0] * (len(res) + 1)
        for i, a in enumerate(res):
            new[i] += a
            new[i + 1] += a
        new[0] += coeff
        res = new
    return res

eis_ok = True
for k in (1, 2, 3):
    sh = shift_poly(cyclotomic_5k(k))
    lead = sh[-1]
    const = sh[0]
    mids = sh[1:-1]
    eis_ok = eis_ok and lead == 1 and const == 5 and all(c % 5 == 0 for c in mids)
check("A3-07 Eisenstein certificates for Phi_5, Phi_25, Phi_125 at x + 1", eis_ok)

# ---------------------------------------------------------------------------
# A4 all-real annihilation, finite rational shadow
# ---------------------------------------------------------------------------

def nA(A):
    return 4 * 5 ** A

grid_shadow = [Fraction(1, 4), Fraction(3, 20), Fraction(7, 100), Fraction(9, 500),
               Fraction(1, 2), Fraction(1, 5), Fraction(2, 25)]
ok = True
for fr in grid_shadow:
    a = level_of(fr)
    for A in range(13):
        d = (Fraction(nA(A)) * fr) % 1
        dist = min(d, 1 - d)
        if A >= a:
            ok = ok and dist == 0
        else:
            ok = ok and dist >= 0
check("A4-01 grid fractions annihilated from their level on", ok)

offgrid = [3, 7, 8, 9, 11, 12, 16, 24, 60]
ok = True
for q in offgrid:
    ok = ok and all((4 * 5 ** a) % q != 0 for a in range(15))
    for p in (1, q - 1):
        fr = Fraction(p, q)
        for A in range(13):
            d = (Fraction(nA(A)) * fr) % 1
            dist = min(d, 1 - d)
            ok = ok and dist >= Fraction(1, q)
check("A4-02 off-grid denominators separated by 1/q at every A <= 12", ok)

# ---------------------------------------------------------------------------
# A5 second difference mechanism
# ---------------------------------------------------------------------------

g = pol(0, 1)
A_ = pol(-1, 0, 4)      # 4g^2 - 1
B_ = pol(0, 4)          # 4g
D_ = pol(1, 0, 4)       # 4g^2 + 1
check("A5-01 A^2 + B^2 = D^2 over Q[g]",
      pol_eq(pol_add(pol_mul(A_, A_), pol_mul(B_, B_)), pol_mul(D_, D_)))

RHO_C = (pol(Fraction(1, 2)), pol(0, 1))          # 1/2 + i g
W_NUM = (A_, B_)                                   # A + i B
# (A + iB) rho = D (rho - 1)
lhsc = cx_mul(W_NUM, RHO_C)
rhsc = (pol_mul(D_, pol(Fraction(-1, 2))), pol_mul(D_, pol(0, 1)))
check("A5-02 (A + iB) rho = D (rho - 1): the Cayley factor is -conj(rho)/rho", cx_eq(lhsc, rhsc))

# -rho^2 (A + iB) = (1/4 + g^2) D
RHO2 = cx_mul(RHO_C, RHO_C)
lhsc = cx_mul((pol_sub(pol(0), RHO2[0]), pol_sub(pol(0), RHO2[1])), W_NUM)
QQ = pol(Fraction(1, 4), 0, 1)
rhsc = (pol_mul(QQ, D_), pol(0))
check("A5-03 reciprocal square collapse -rho^2 (A + iB) = (1/4 + g^2) D", cx_eq(lhsc, rhsc))

check("A5-04 rho + conj(rho) = 1 and rho conj(rho) = 1/4 + g^2",
      pol_eq(pol_add(RHO_C[0], RHO_C[0]), pol(1)) and
      pol_eq(pol_add(pol_mul(RHO_C[0], RHO_C[0]), pol_mul(RHO_C[1], RHO_C[1])), QQ))

X = pol(0, 1)
okX = True
for n in range(1, 41):
    left = pol_sub(pol_add(pol_mul(X, [Fraction(0)] * n + [Fraction(1)]),
                           [Fraction(0)] * (n - 1) + [Fraction(1)]),
                   pol_mul(pol(2), [Fraction(0)] * n + [Fraction(1)]))
    right = pol_mul([Fraction(0)] * (n - 1) + [Fraction(1)],
                    pol_mul(pol(-1, 1), pol(-1, 1)))
    okX = okX and pol_eq(left, right)
check("A5-05 X^(n+1) + X^(n-1) - 2 X^n = X^(n-1)(X-1)^2 for n = 1..40", okX)

# Fejer second difference in exact Z[phi]/Q cosine arithmetic
angles = [("2pi/5", (Fraction(-1, 2), Fraction(1, 2)), True),
          ("pi/5", (Fraction(0), Fraction(1, 2)), True),
          ("pi/2", (Fraction(0), Fraction(0)), True),
          ("2pi/3", (Fraction(-1, 2), Fraction(0)), False)]
okF = True
for name, c1, _ in angles:
    cs = [P_ONE, c1]
    for n in range(2, 62):
        cs.append(psub(pscal(2, pmul(c1, cs[-1])), cs[-2]))
    denom_inv = pinv(psub(P_ONE, c1))
    Dn = [pmul(psub(P_ONE, cn), denom_inv) for cn in cs]
    okF = okF and Dn[0] == P_ZERO and Dn[1] == P_ONE
    for n in range(1, 60):
        second = psub(padd(Dn[n + 1], Dn[n - 1]), pscal(2, Dn[n]))
        okF = okF and second == pscal(2, cs[n])
check("A5-06 Fejer second difference D_(n+1)+D_(n-1)-2D_n = 2 cos(n theta), n = 1..59", okF)

# two initial value induction rebuild on a two-atom synthetic (angles 2pi/5, pi/2)
m1, m2 = Fraction(3, 7), Fraction(2, 5)
c1a = (Fraction(-1, 2), Fraction(1, 2))
c1b = (Fraction(0), Fraction(0))
csa = [P_ONE, c1a]
csb = [P_ONE, c1b]
for n in range(2, 62):
    csa.append(psub(pscal(2, pmul(c1a, csa[-1])), csa[-2]))
    csb.append(psub(pscal(2, pmul(c1b, csb[-1])), csb[-2]))
Da = [pmul(psub(P_ONE, cn), pinv(psub(P_ONE, c1a))) for cn in csa]
Db = [pmul(psub(P_ONE, cn), pinv(psub(P_ONE, c1b))) for cn in csb]
f_direct = [padd(pscal(m1, Da[n]), pscal(m2, Db[n])) for n in range(62)]
t_seq = [padd(pscal(2 * m1, csa[n]), pscal(2 * m2, csb[n])) for n in range(62)]
f_re = [P_ZERO, (m1 + m2, Fraction(0))]
for n in range(1, 61):
    f_re.append(psub(padd(t_seq[n], pscal(2, f_re[n])), f_re[n - 1]))
check("A5-07 two initial values + second differences rebuild the ladder, n <= 61",
      all(f_re[n] == f_direct[n] for n in range(62)))

# ---------------------------------------------------------------------------
# A6 adversarial synthetic tails, exact rationals
# ---------------------------------------------------------------------------

grid_atoms = [(Fraction(1, 20), Fraction(3, 7)), (Fraction(7, 100), Fraction(1, 3)),
              (Fraction(1, 4), Fraction(2, 5))]
M_syn = 2 * sum(m for _, m in grid_atoms)
okT = True
for A in range(2, 13):
    n = nA(A)
    res = Fraction(0)
    for r, m in grid_atoms:
        prod = (Fraction(n) * r) % 1
        if prod != 0:
            res = None
            break
        # cos = 1 exactly, contribution to M - t_n is 0
    okT = okT and res == Fraction(0)
check("A6-01 grid-supported synthetic: residual exactly 0 for all A >= 2", okT)

# shared angle merge: two masses on the same angle add before the choice
sh = [(Fraction(1, 20), Fraction(1, 6)), (Fraction(1, 20), Fraction(1, 3))]
merged = {}
for r, m in sh:
    merged[r] = merged.get(r, Fraction(0)) + m
check("A6-02 shared angle bookkeeping: masses add to one atom of mass 1/2",
      list(merged.items()) == [(Fraction(1, 20), Fraction(1, 2))])

def residual_offgrid(r, m, A):
    # exact residual contribution 2 m (1 - cos(2 pi n r)) at rational cosine points
    fr = (Fraction(nA(A)) * r) % 1
    table = {Fraction(0): Fraction(1), Fraction(1, 2): Fraction(-1),
             Fraction(1, 3): Fraction(-1, 2), Fraction(2, 3): Fraction(-1, 2)}
    if fr not in table:
        raise AssertionError("nonrational cosine reached in exact tail check")
    return 2 * m * (1 - table[fr])

okO = True
for A in range(0, 13):
    okO = okO and residual_offgrid(Fraction(1, 3), Fraction(1, 2), A) == 3 * Fraction(1, 2)
    okO = okO and residual_offgrid(Fraction(1, 8), Fraction(1, 6), A) == 4 * Fraction(1, 6)
    okO = okO and residual_offgrid(Fraction(5, 12), Fraction(1, 7), A) == 3 * Fraction(1, 7)
check("A6-03 off-grid atoms 1/3, 1/8, 5/12: residual constant 3m, 4m, 3m for all A <= 12", okO)

per3 = [pow(5, A, 3) for A in range(13)]
check("A6-04 period certificate: 5^A mod 3 cycles in {1, 2}, never 0",
      all(x in (1, 2) for x in per3))

# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

failures = 0
for label, ok_ in CHECKS:
    print(("PASS " if ok_ else "FAIL ") + label)
    if not ok_:
        failures += 1
for label, ok_ in CONJ:
    print(("CONJ-HELD " if ok_ else "CONJ-FIRED ") + label)

print("LADDER v_lambda(J^(4.5^m) - 1), m = 0..6: " + " ".join(str(v) for v in ladder))
print("ORDERS ord_(lambda^k)(J), k = 1..14: " +
      " ".join(str(ord_table[k]) for k in range(1, 15)))
print("RESULT %d/%d PASS, %d conjecture line(s) reported separately"
      % (len(CHECKS) - failures, len(CHECKS), len(CONJ)))
sys.exit(1 if failures else 0)
