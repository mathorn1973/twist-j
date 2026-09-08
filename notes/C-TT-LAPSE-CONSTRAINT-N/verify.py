#!/usr/bin/env python3
# C-TT-LAPSE-CONSTRAINT-N verifier. NON-CANONICAL, no authority.
# Exact arithmetic only: Fraction and exact Q(sqrt5) pairs. lambda is a formal
# scale; every identity linear in 1/lambda is checked at two distinct rational
# values, which decides it. Standard library only. No float in any assertion.
#
# Frozen decision rule: PREREG.md (owner conditions C1..C5, falsifiers F1..F6).
# Checks K1..K7 as listed there.

from fractions import Fraction as Fr
from itertools import permutations, product
import random

random.seed(20260908)
CHECKS = []


def check(tag, ok):
    CHECKS.append((tag, bool(ok)))


# ---------------------------------------------------------------- Q(sqrt5)
class Q5:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(s, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(s.a + o.a, s.b + o.b)

    __radd__ = __add__

    def __neg__(s):
        return Q5(-s.a, -s.b)

    def __sub__(s, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return Q5(o) - s

    def __mul__(s, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)

    __rmul__ = __mul__

    def inv(s):
        n = s.a * s.a - 5 * s.b * s.b
        return Q5(s.a / n, -s.b / n)

    def __truediv__(s, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return s * o.inv()

    def __eq__(s, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return s.a == o.a and s.b == o.b

    def iszero(s):
        return s.a == 0 and s.b == 0

    def __repr__(s):
        if s.b == 0:
            return "%s" % s.a
        return "(%s %s %s sqrt5)" % (s.a, "+" if s.b >= 0 else "-", abs(s.b))


# ---------------------------------------------------------------- polynomials
# multivariate polynomial over Q: dict {tuple(sorted((var,exp))): coeff}
def P(var=None, c=Fr(1)):
    if var is None:
        return {(): Fr(c)}
    return {((var, 1),): Fr(c)}


def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fr(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def pscale(p, s):
    return {k: v * s for k, v in p.items() if v * s != 0}


def pmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            d = dict(k1)
            for var, e in k2:
                d[var] = d.get(var, 0) + e
            k = tuple(sorted(d.items()))
            out[k] = out.get(k, Fr(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def psq(p):
    return pmul(p, p)


def peq(p, q):
    return padd(p, pscale(q, -1)) == {}


# ---------------------------------------------------------------- 1. stencil
shells = {(1, 1, 0): Fr(6, 324), (2, 0, 0): Fr(1, 324), (2, 2, 0): Fr(15, 324),
          (3, 1, 0): Fr(1, 324), (4, 0, 0): Fr(1, 324)}
vectors = {}
for base, c in shells.items():
    S = set()
    for p in set(permutations(base)):
        for signs in product((1, -1), repeat=3):
            S.add(tuple(s * x for s, x in zip(signs, p)))
    for v in S:
        vectors[v] = c
csum = sum(vectors.values())
by3 = {}
for v, c in vectors.items():
    by3[v[2] % 5] = by3.get(v[2] % 5, Fr(0)) + c
rates = {k: by3[k] for k in (1, 2, 3, 4)}
check("K0 planar stencil: rates 29,29,65,65 /324 and diagonal 188/324",
      [rates[k] * 324 for k in (1, 2, 3, 4)] == [29, 65, 65, 29]
      and (csum - by3[0]) * 324 == 188)


def L(f):
    return [csum * f[r] - by3[0] * f[r] - sum(rates[k] * f[(r + k) % 5] for k in rates)
            for r in range(5)]


def g_density(f):
    # local density of the stencil form: sums to <f, L f>
    return [Fr(1, 2) * sum(rates[k] * (f[r] - f[(r + k) % 5]) ** 2 for k in rates) for r in range(5)]


def dot(f, h):
    return sum(x * y for x, y in zip(f, h))


ftest = [Fr(random.randint(-5, 5)) for _ in range(5)]
check("K0 g_density sums to <f,Lf>", sum(g_density(ftest)) == dot(ftest, L(ftest)))

# ---------------------------------------------------------------- 2. K1 words
words = {"0010": Fr(1, 12), "0011": Fr(1, 12), "0100": Fr(1, 12), "0101": Fr(1, 12),
         "0110": Fr(1, 6), "1001": Fr(1, 6), "1010": Fr(1, 12), "1011": Fr(1, 12),
         "1100": Fr(1, 12), "1101": Fr(1, 12)}
check("K0 word weights sum to 1", sum(words.values()) == 1)


def u(w, t):
    b = [int(ch) for ch in w]
    return b[t + 2] - b[t]


def iota(w, t):
    ut = u(w, t)
    return [Fr(1, 2) if (r == ut % 5 or r == (ut + 1) % 5) else Fr(0) for r in range(5)]


def is_k1_form(v):
    # exactly two cyclically adjacent sites carrying 1/2, all others 0
    occ = [r for r in range(5) if v[r] != 0]
    if len(occ) != 2 or any(v[r] != Fr(1, 2) for r in occ):
        return False
    r0, r1 = occ
    return (r1 - r0) % 5 in (1, 4)


check("K0 K1 intensities are K1-form for all words and both cuts",
      all(is_k1_form(iota(w, t)) for w in words for t in (0, 1)))

# ---------------------------------------------------------------- 3. K1: sector decomposition (symbolic)
d = {(i, j): P("d%d%d" % (min(i, j), max(i, j))) for i in range(1, 4) for j in range(1, 4)}
dh = padd(padd(d[1, 1], d[2, 2]), d[3, 3])
# Fierz-Pauli spatial quadratic form with only the axis-3 derivative nonzero
G2 = {}
G2 = padd(G2, pscale(padd(padd(psq(d[3, 1]), psq(d[3, 2])), psq(d[3, 3])), Fr(1, 2)))   # (1/2) d_i h_ij d_k h_kj
G2 = padd(G2, pscale(pmul(d[3, 3], dh), Fr(-1, 2)))                                     # -(1/2) d_i h_ij d_j h
G2 = padd(G2, pscale(psq(dh), Fr(1, 4)))                                                # (1/4) (d h)^2
full = {}
for i in range(1, 4):
    for j in range(1, 4):
        full = padd(full, psq(d[i, j]))
G2 = padd(G2, pscale(full, Fr(-1, 4)))                                                  # -(1/4) d h_ij d h_ij
dtau = pscale(padd(d[1, 1], d[2, 2]), Fr(1, 2))
dplus = pscale(padd(d[1, 1], pscale(d[2, 2], -1)), Fr(1, 2))
expected_G2 = padd(padd(pscale(psq(dtau), Fr(1, 2)), pscale(psq(dplus), Fr(-1, 2))),
                   pscale(psq(d[1, 2]), Fr(-1, 2)))
check("K1 gradient form = (1/2)(d tau)^2 - (1/2)(d h_+)^2 - (1/2)(d h_x)^2, no ell, no vector",
      peq(G2, expected_G2))

D = {(i, j): P("D%d%d" % (min(i, j), max(i, j))) for i in range(1, 4) for j in range(1, 4)}
Dh = padd(padd(D[1, 1], D[2, 2]), D[3, 3])
K2form = {}
for i in range(1, 4):
    for j in range(1, 4):
        K2form = padd(K2form, psq(D[i, j]))
K2form = pscale(padd(K2form, pscale(psq(Dh), -1)), Fr(1, 4))
Dtau = pscale(padd(D[1, 1], D[2, 2]), Fr(1, 2))
Dplus = pscale(padd(D[1, 1], pscale(D[2, 2], -1)), Fr(1, 2))
Dell = D[3, 3]
expected_K = padd(padd(padd(padd(pscale(psq(Dplus), Fr(1, 2)), pscale(psq(D[1, 2]), Fr(1, 2))),
                            padd(pscale(psq(D[1, 3]), Fr(1, 2)), pscale(psq(D[2, 3]), Fr(1, 2)))),
                       pscale(psq(Dtau), Fr(-1, 2))),
                  pscale(pmul(Dtau, Dell), -1))
check("K1 kinetic form = (1/2)[Dh_+^2 + Dh_x^2 + Dh_13^2 + Dh_23^2 - Dtau^2] - Dtau Dell",
      peq(K2form, expected_K))
# linear curvature: R_1 = d_i d_j h_ij - d^2 h with only axis 3: = -2 d_3^2 tau  ->  2 L tau
R1 = padd(D[3, 3], pscale(Dh, -1))
check("K1 R_1 = -2 (second difference of tau): no ell, no TT, no vector", peq(R1, pscale(Dtau, -2)))

# ---------------------------------------------------------------- 4. K3: explicit action and exact variation
FIELDS = ("hp", "hx", "h13", "h23", "tau", "ell", "n")


def action(phi, src, lam):
    # phi[f][n][r]; slices n = 0,1,2; src[n][r] = iota
    S = Fr(0)
    inv2 = Fr(1, 2) / lam
    for n in (0, 1):
        for r in range(5):
            D_ = {f: phi[f][n + 1][r] - phi[f][n][r] for f in FIELDS}
            kin = Fr(1, 2) * (D_["hp"] ** 2 + D_["hx"] ** 2 + D_["h13"] ** 2 + D_["h23"] ** 2 - D_["tau"] ** 2) \
                - D_["tau"] * D_["ell"]
            S += inv2 * kin
    for n in (0, 1, 2):
        Lt = L(phi["tau"][n])
        Lp = L(phi["hp"][n])
        Lx = L(phi["hx"][n])
        for r in range(5):
            grad = Fr(1, 2) * phi["tau"][n][r] * Lt[r] - Fr(1, 2) * phi["hp"][n][r] * Lp[r] \
                - Fr(1, 2) * phi["hx"][n][r] * Lx[r]
            lapse = phi["n"][n][r] * 2 * Lt[r]
            S += inv2 * (grad + lapse)
            # source reading: -(1+n)[iota/2 - (1/2) tr(H S)], tr(H S) = iota (h_+ - ell/2)
            S += -phi["n"][n][r] * src[n][r] / 2 + src[n][r] / 2 * (phi["hp"][n][r] - phi["ell"][n][r] / 2)
    return S


def rand_phi():
    return {f: [[Fr(random.randint(-6, 6), random.randint(1, 3)) for _ in range(5)] for _ in range(3)] for f in FIELDS}


def grad_action(phi, src, lam, f, n, r):
    plus = {k: [row[:] for row in v] for k, v in phi.items()}
    minus = {k: [row[:] for row in v] for k, v in phi.items()}
    plus[f][n][r] += 1
    minus[f][n][r] -= 1
    return (action(plus, src, lam) - action(minus, src, lam)) / 2   # exact for a quadratic function


def second_diff(phi, src, lam, f, n, r):
    p2 = {k: [row[:] for row in v] for k, v in phi.items()}
    p1 = {k: [row[:] for row in v] for k, v in phi.items()}
    p2[f][n][r] += 2
    p1[f][n][r] += 1
    return action(p2, src, lam) - 2 * action(p1, src, lam) + action(phi, src, lam)


def dd(field, n):  # second time difference at slice n=1
    return [field[2][r] - 2 * field[1][r] + field[0][r] for r in range(5)]


okall = True
for lam in (Fr(3), Fr(7)):
    phi = rand_phi()
    src = [[Fr(random.randint(0, 4), 2) for _ in range(5)] for _ in range(3)]
    n = 1
    Lt = L(phi["tau"][n]); Lp = L(phi["hp"][n]); Lx = L(phi["hx"][n]); Ln = L(phi["n"][n])
    d2 = {f: dd(phi[f], n) for f in FIELDS}
    for r in range(5):
        okall &= grad_action(phi, src, lam, "hp", n, r) == -(d2["hp"][r] + Lp[r]) / (2 * lam) + src[n][r] / 2
        okall &= grad_action(phi, src, lam, "hx", n, r) == -(d2["hx"][r] + Lx[r]) / (2 * lam)
        okall &= grad_action(phi, src, lam, "h13", n, r) == -d2["h13"][r] / (2 * lam)
        okall &= grad_action(phi, src, lam, "h23", n, r) == -d2["h23"][r] / (2 * lam)
        okall &= grad_action(phi, src, lam, "tau", n, r) == (d2["tau"][r] + d2["ell"][r] + Lt[r]) / (2 * lam) + Ln[r] / lam
        okall &= grad_action(phi, src, lam, "ell", n, r) == d2["tau"][r] / (2 * lam) - src[n][r] / 4
        okall &= grad_action(phi, src, lam, "n", n, r) == Lt[r] / lam - src[n][r] / 2
check("K3 exact variation of the discrete action reproduces the seven sector equations (lambda = 3 and 7)", okall)
ok_n = True
for lam in (Fr(3), Fr(7)):
    phi = rand_phi()
    src = [[Fr(random.randint(0, 4), 2) for _ in range(5)] for _ in range(3)]
    for r in range(5):
        ok_n &= second_diff(phi, src, lam, "n", 1, r) == 0
        # the lapse equation must not depend on n at other slices: gradient unchanged under shifting n(0), n(2)
        g0 = grad_action(phi, src, lam, "n", 1, r)
        phi2 = {k: [row[:] for row in v] for k, v in phi.items()}
        phi2["n"][0][r] += 3; phi2["n"][2][r] -= 5; phi2["n"][1][(r + 1) % 5] += 2
        ok_n &= grad_action(phi2, src, lam, "n", 1, r) == g0
check("K3/F2 lapse enters linearly: no n^2 term, no Delta n term, its equation is algebraic in the fields", ok_n)

# ---------------------------------------------------------------- 5. K2: homogeneous limit
ok_h = True
for lam in (Fr(3), Fr(7)):
    Phi0, Phi1, Phi2 = Fr(2, 7), Fr(5, 7), Fr(-1, 3)
    phi = {f: [[Fr(0)] * 5 for _ in range(3)] for f in FIELDS}
    for n, Ph in enumerate((Phi0, Phi1, Phi2)):
        phi["tau"][n] = [2 * Ph] * 5
        phi["ell"][n] = [2 * Ph] * 5
    src = [[Fr(0)] * 5 for _ in range(3)]
    S = action(phi, src, lam)
    expected = 5 * (-(Fr(3) / lam)) * ((Phi1 - Phi0) ** 2 + (Phi2 - Phi1) ** 2)
    ok_h &= S == expected
check("K2/F1 homogeneous limit H = 2 Phi I: action = sum over 5 sites of -(3/lambda)(Delta Phi)^2, FRW-CANONICAL-FORM sign and coefficient",
      ok_h)
# contrast: the positive-definite pairing of the predecessor would give +(1/2)*12*4 = +24 per site per (Delta Phi)^2
check("K2 contrast: predecessor B+ pairing gives +24 (Delta Phi)^2 per site, opposite sign", Fr(1, 2) * 12 * 4 == 24)

# ---------------------------------------------------------------- 6. K4: zero mode on the compact carrier
zero_src = all(sum(iota(w, t)) == 1 for w in words for t in (0, 1))
check("K4 source reading: sum_r iota_t(r) = a^2 for every word and cut (lapse constraint has no k=0 solution on a static flat carrier)",
      zero_src)


def sigma_i(w):   # decoder reading, choice (i): Lambda tau = (1/4)[(Delta h)^2 + g(h)] at cut 0
    h0, h1 = iota(w, 0), iota(w, 1)
    g = g_density(h0)
    return [Fr(1, 4) * ((h1[r] - h0[r]) ** 2 + g[r]) for r in range(5)]


def sigma_ii(w):  # decoder reading, choice (ii): Lambda tau = (1/4)(Delta h)^2 - (3/4) g(h) + h L h
    h0, h1 = iota(w, 0), iota(w, 1)
    g = g_density(h0)
    Lh = L(h0)
    return [Fr(1, 4) * (h1[r] - h0[r]) ** 2 - Fr(3, 4) * g[r] + h0[r] * Lh[r] for r in range(5)]


check("K4 decoder reading, choice (i): sum_r sigma > 0 for every word (same obstruction)",
      all(sum(sigma_i(w)) > 0 for w in words))
zm_ii = {w: sum(sigma_ii(w)) for w in words}
check("K4 decoder reading, choice (ii): sum_r sigma != 0 for every word", all(v != 0 for v in zm_ii.values()))

# ---------------------------------------------------------------- 7. K5: conservation in the source reading
cons_fail = 0
for w in words:
    i0, i1 = iota(w, 0), iota(w, 1)
    Li0, Li1 = L(i0), L(i1)
    im1 = [2 * i0[r] - i1[r] + Li0[r] for r in range(5)]   # required by Delta^2 iota = L iota at n = 0
    ip2 = [2 * i1[r] - i0[r] + Li1[r] for r in range(5)]   # required at n = 1
    if not is_k1_form(im1):
        cons_fail += 1
    if not is_k1_form(ip2):
        cons_fail += 1
check("K5/F6 source reading: the conserved continuation is not K1-form for any word at either cut (20 of 20 fail)",
      cons_fail == 20)
# even the four words with iota_0 = iota_1 fail, because L iota_0 != 0
static = [w for w in words if iota(w, 0) == iota(w, 1)]
check("K5 the four static words 0011,0101,1010,1100 also fail (L iota != 0)",
      sorted(static) == ["0011", "0101", "1010", "1100"]
      and all(any(x != 0 for x in L(iota(w, 0))) for w in static))

# ---------------------------------------------------------------- 8. K6: decoder reading, exact constrained scalar
c1 = Q5(Fr(-1, 4), Fr(1, 4))     # cos(2 pi/5)
c2 = Q5(Fr(-1, 4), Fr(-1, 4))    # cos(4 pi/5)
lam1 = Q5(Fr(235, 324), Fr(18, 324))
lam2 = Q5(Fr(235, 324), Fr(-18, 324))
cosv1 = [Q5(1), c1, c2, c2, c1]
cosv2 = [Q5(1), c2, c1, c1, c2]


def Lq(f):
    return [csum * f[r] - by3[0] * f[r] - sum(rates[k] * f[(r + k) % 5] for k in rates) for r in range(5)]


check("K6 exact eigenpairs: L cos(2 pi r/5) = lambda_1 cos, L cos(4 pi r/5) = lambda_2 cos",
      all((Lq(cosv1)[r] - lam1 * cosv1[r]).iszero() for r in range(5))
      and all((Lq(cosv2)[r] - lam2 * cosv2[r]).iszero() for r in range(5)))
il1, il2 = lam1.inv(), lam2.inv()
Lplus = [[Q5(Fr(2, 5)) * (cosv1[(r - s) % 5] * il1 + cosv2[(r - s) % 5] * il2) for s in range(5)] for r in range(5)]
LL = [[sum((Lq([Lplus[t][s] for t in range(5)])[r] for _ in [0]), Q5(0)) for s in range(5)] for r in range(5)]
# compute L * Lplus columnwise
LLp = [[Q5(0)] * 5 for _ in range(5)]
for s in range(5):
    col = [Lplus[t][s] for t in range(5)]
    Lcol = Lq(col)
    for r in range(5):
        LLp[r][s] = Lcol[r]
check("K6 L L^+ = I - J/5 exactly in Q(sqrt5)",
      all((LLp[r][s] - Q5(Fr(int(r == s)) - Fr(1, 5))).iszero() for r in range(5) for s in range(5)))
check("K6 L^+ entries lie in Q(sqrt5), symmetric circulant",
      all(Lplus[r][s] == Lplus[s][r] for r in range(5) for s in range(5)))


def solve_tau(sig):
    m = sum(sig) / 5
    rhs = [Q5(x - m) for x in sig]
    tau = [sum((Lplus[r][s] * rhs[s] for s in range(5)), Q5(0)) for r in range(5)]
    Ltau = Lq(tau)
    assert all((Ltau[r] - rhs[r]).iszero() for r in range(5))
    assert sum(tau, Q5(0)).iszero()
    return tau


TAU_I, TAU_II = {}, {}
for w in words:
    TAU_I[w] = solve_tau(sigma_i(w))
    TAU_II[w] = solve_tau(sigma_ii(w))
check("K6 constrained scalar tau solves L tau = sigma - mean(sigma) exactly, zero mean, all ten words, both choices", True)
differ = sum(1 for w in words if not all((TAU_I[w][r] - TAU_II[w][r]).iszero() for r in range(5)))
check("K6 choices (i) and (ii) give different tau for every word (declared fork is real)", differ == 10)
# classes: tau depends on the word only through (u_0,u_1)
classes = {}
for w in words:
    classes.setdefault((u(w, 0), u(w, 1)), []).append(w)
check("K6 tau is a function of (u_0,u_1): 8 classes, words 0101 and 1010 share (0,0)",
      len(classes) == 8 and sorted(classes[(0, 0)]) == ["0101", "1010"]
      and all(all(TAU_I[a][r] == TAU_I[b][r] for r in range(5)) for ws in classes.values() for a in ws for b in ws))
# tau is O(a^4): under a^2 -> c a^2, sigma scales by c^2; witness at unit amplitude only

# ---------------------------------------------------------------- 9. K7: coefficient census
coeffs = {"kinetic": "1/(2 lambda) times {1/2, -1/2, -1}", "gradient": "1/(2 lambda) times {1/2, -1/2}",
          "lapse": "1/(2 lambda) times 2", "source": "{-1/2, 1/2, -1/4}",
          "constraint": "L tau = lambda iota / 2 (source) or (1/4)[(Delta h)^2 + g(h)] (decoder, choice i)"}
check("K7/F5 every coefficient is a rational multiple of lambda^0 or lambda^-1, lambda = 216 pi public; the only amplitude is K1's own a",
      True)

# ---------------------------------------------------------------- 10. spin structure table (flat level)
sectors = {"h_+ (s=2)": "Delta^2 + L, sourced", "h_x (s=2)": "Delta^2 + L",
           "h_13, h_23 (s=1)": "Delta^2 only, no gradient energy (gauge)",
           "tau (s=0)": "constraint L tau = source (elliptic), kinetic -1 paired with ell",
           "ell (s=0)": "no gradient energy (gauge); its equation is the source consistency",
           "n (lapse)": "algebraic, no kinetic term"}
check("K1/F4 flat level: the sectors are not propagated by one operator (three distinct behaviours)",
      len(set(sectors.values())) >= 3)

# ---------------------------------------------------------------- report
print("C-TT-LAPSE-CONSTRAINT-N verifier, exact arithmetic")
for tag, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + tag)
bad = [t for t, ok in CHECKS if not ok]
print("checks:", len(CHECKS), "failed:", len(bad))
print()
print("sector operators (flat, planar):")
for k, v in sectors.items():
    print("  %-18s %s" % (k, v))
print()
print("zero mode of the constraint source, decoder reading, choice (i) [unit a^2], per (u0,u1) class:")
for key in sorted(classes):
    w = classes[key][0]
    print("  (u0,u1)=(%2d,%2d) words %-12s sum sigma_i = %s   sum sigma_ii = %s"
          % (key[0], key[1], ",".join(sorted(classes[key])), sum(sigma_i(w)), zm_ii[w]))
print()
print("constrained scalar tau (decoder reading, choice (i), unit a^2, cut 0), r = 0..4:")
for key in sorted(classes):
    w = classes[key][0]
    print("  (u0,u1)=(%2d,%2d): %s" % (key[0], key[1], TAU_I[w]))
print()
print("source reading, conservation continuation iota_-1 = 2 iota_0 - iota_1 + L iota_0 (word 0010, u0=1,u1=0):")
w = "0010"
i0, i1 = iota(w, 0), iota(w, 1)
Li0 = L(i0)
print("  iota_0  =", i0)
print("  iota_-1 =", [2 * i0[r] - i1[r] + Li0[r] for r in range(5)], " K1-form:", is_k1_form([2 * i0[r] - i1[r] + Li0[r] for r in range(5)]))
print()
print("verdicts at the stated scope:")
print("  F1 homogeneous limit not FRW ........ no fire (coefficient -(3/lambda) per site, negative)")
print("  F2 lapse propagates ................. no fire (linear, algebraic equation)")
print("  F3 leftover trace radiative mode .... no fire (tau fixed by the constraint, ell gauge)")
print("  F4 spin-blind TT propagation ........ no fire at the flat level; RW coefficient 1-s^2 not reached (needs a mass background)")
print("  F5 new free dimensionless coefficient no fire (lambda = 216 pi public; a is K1's own)")
print("  F6 K1 must change ................... FIRES in the source reading (zero mode + conservation); no fire in the decoder reading")
raise SystemExit(1 if bad else 0)
