#!/usr/bin/env python3
# C-TT-SHIFT-CONSTRAINT-N verifier. NON-CANONICAL, no authority.
# Exact arithmetic only (Fraction). Two representations:
#   P1  commutative symbol algebra Q[L, D, E, E^-1]/(D^2 + L), transpose D -> -D,
#       E -> E^-1; identities valid for every antisymmetric circulant D with L = -D^2
#   P3  explicit polynomial action on Z/5 x Z/4 (time periodic) with the rational
#       centered difference D_c; identities as polynomial identities in all variables
# Standard library only. No float in any assertion. Frozen decision rule: PREREG.md.

from fractions import Fraction as Fr
from itertools import permutations, product
from math import isqrt

CHECKS = []


def check(tag, ok):
    CHECKS.append((tag, bool(ok)))


# ============================================================ P1: symbol algebra
# element: dict {(e, d, l): Fraction}; e = power of E, d in {0,1} = power of D, l = power of L
def R(coeff=1, e=0, d=0, l=0):
    return {(e, d, l): Fr(coeff)} if coeff != 0 else {}


def radd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fr(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def rscale(a, s):
    return {k: v * s for k, v in a.items() if v * s != 0}


def rmul(a, b):
    out = {}
    for (e1, d1, l1), v1 in a.items():
        for (e2, d2, l2), v2 in b.items():
            e, d, l, c = e1 + e2, d1 + d2, l1 + l2, v1 * v2
            if d == 2:
                d, l, c = 0, l + 1, -c
            out[(e, d, l)] = out.get((e, d, l), Fr(0)) + c
    return {k: v for k, v in out.items() if v != 0}


def rT(a):
    return {(-e, d, l): (v if d == 0 else -v) for (e, d, l), v in a.items()}


def rzero(a):
    return len(a) == 0


ONE = R(1)
E = R(1, e=1)
Einv = R(1, e=-1)
D = R(1, d=1)
Lop = R(1, l=1)
DELTA = radd(E, rscale(ONE, -1))          # E - 1
NABLA = radd(ONE, rscale(Einv, -1))       # 1 - E^-1


# linear expressions: dict {field: R-element}
def ladd(x, y):
    out = {k: dict(v) for k, v in x.items()}
    for f, o in y.items():
        out[f] = radd(out.get(f, {}), o)
        if rzero(out[f]):
            del out[f]
    return out


def lscale(x, s):
    return {f: rscale(o, s) for f, o in x.items() if not rzero(rscale(o, s))}


def lop(o, x):   # apply operator o to linear expression x
    return {f: rmul(o, p) for f, p in x.items() if not rzero(rmul(o, p))}


def lvar(f, o=None):
    return {f: dict(o if o is not None else ONE)}


def lzero(x):
    return all(rzero(o) for o in x.values())


# quadratic form: dict {(A, B): R} meaning sum_n <A, O B>
def qf_add(QF, X, Y, c=Fr(1)):
    # <X, Y> with X = sum O_a a, Y = sum P_b b  ->  <a, O_a^T P_b b>
    for a, Oa in X.items():
        for b, Pb in Y.items():
            o = rscale(rmul(rT(Oa), Pb), c)
            QF[(a, b)] = radd(QF.get((a, b), {}), o)
            if rzero(QF[(a, b)]):
                del QF[(a, b)]


def qf_EL(QF, fields):
    EL = {f: {} for f in fields}
    for (a, b), O in QF.items():
        if a in EL:
            EL[a] = ladd(EL[a], {b: dict(O)})
        if b in EL:
            EL[b] = ladd(EL[b], {a: rT(O)})
    return EL


METRIC = ("h11", "h22", "h12", "h13", "h23", "h33")
FIELDS = METRIC + ("n", "N1", "N2", "N3")
SOURCES = ("rho", "J1", "J2", "J3", "S11", "S22", "S12", "S13", "S23", "S33")


def build_QF(with_source):
    il = Fr(1)   # 1/lambda kept as an overall factor on the gravitational part: we carry it as a
    QF = {}
    # extrinsic curvature on half slices: K_ij = (Delta h_ij - D_i N_j - D_j N_i)/2, only D_3 = D
    K = {
        "11": lscale(lvar("h11", DELTA), Fr(1, 2)),
        "22": lscale(lvar("h22", DELTA), Fr(1, 2)),
        "12": lscale(lvar("h12", DELTA), Fr(1, 2)),
        "13": lscale(ladd(lvar("h13", DELTA), lscale(lvar("N1", D), -1)), Fr(1, 2)),
        "23": lscale(ladd(lvar("h23", DELTA), lscale(lvar("N2", D), -1)), Fr(1, 2)),
        "33": lscale(ladd(lvar("h33", DELTA), lscale(lvar("N3", D), -2)), Fr(1, 2)),
    }
    Ktr = ladd(ladd(K["11"], K["22"]), K["33"])
    # (1/(2 lambda)) [ K_ij K_ij - K^2 ]  with the factor 1/(2 lambda) written as IL/2, IL symbolic = 1 here;
    # the physical prefactor multiplies every gravitational term equally and drops out of all identities.
    for key in ("11", "22", "33"):
        qf_add(QF, K[key], K[key], Fr(1, 2))
    for key in ("12", "13", "23"):
        qf_add(QF, K[key], K[key], Fr(1))
    qf_add(QF, Ktr, Ktr, Fr(-1, 2))
    # gradient part G_2 with D explicit: (1/2)<D h_3j, D h_3j> - (1/2)<D h_33, D h> + (1/4)<D h, D h> - (1/4)<D h_ij, D h_ij>
    h = ladd(ladd(lvar("h11"), lvar("h22")), lvar("h33"))
    Dh = lop(D, h)
    for key in ("h13", "h23", "h33"):
        qf_add(QF, lop(D, lvar(key)), lop(D, lvar(key)), Fr(1, 2) * Fr(1, 2))
    qf_add(QF, lop(D, lvar("h33")), Dh, Fr(-1, 2) * Fr(1, 2))
    qf_add(QF, Dh, Dh, Fr(1, 4) * Fr(1, 2))
    for key, mult in (("h11", 1), ("h22", 1), ("h33", 1), ("h12", 2), ("h13", 2), ("h23", 2)):
        qf_add(QF, lop(D, lvar(key)), lop(D, lvar(key)), Fr(-1, 4) * mult * Fr(1, 2))
    # lapse term (1/(2 lambda)) n R_1, R_1 = D D h_33 - D D h
    R1 = ladd(lop(rmul(D, D), lvar("h33")), lscale(lop(rmul(D, D), h), -1))
    qf_add(QF, lvar("n"), R1, Fr(1, 2))
    if with_source:
        qf_add(QF, lvar("n"), lvar("rho"), Fr(-1))
        for i in ("1", "2", "3"):
            qf_add(QF, lvar("N" + i), lvar("J" + i), Fr(1))
        for key, mult in (("11", Fr(1, 2)), ("22", Fr(1, 2)), ("33", Fr(1, 2)), ("12", 1), ("13", 1), ("23", 1)):
            qf_add(QF, lvar("h" + key), lvar("S" + key), mult)
    return QF


# gauge generators: delta field = sum_mu G[field][mu] xi_mu
GAUGE = {
    "h13": {"xi1": D},
    "h23": {"xi2": D},
    "h33": {"xi3": rscale(D, 2)},
    "N1": {"xi1": DELTA},
    "N2": {"xi2": DELTA},
    "N3": {"xi3": DELTA, "xi0": D},
    "n": {"xi0": rscale(NABLA, -1)},
}
XIS = ("xi0", "xi1", "xi2", "xi3")

QFv = build_QF(False)
ELv = qf_EL(QFv, FIELDS)
# sanity: R_1 reduces to 2 L tau, i.e. EL_n = L(h11 + h22)/2 * 2 * (1/2) ... print later
noether_ok = True
NOETHER = {}
for mu in XIS:
    acc = {}
    for f, gens in GAUGE.items():
        if mu in gens:
            acc = ladd(acc, lop(rT(gens[mu]), ELv[f]))
    NOETHER[mu] = acc
    noether_ok &= lzero(acc)
check("P1 Noether identities for xi_0, xi_1, xi_2, xi_3 vanish identically in vacuum (every antisymmetric D, L = -D^2)", noether_ok)

# P2: quadratic form vanishes on pure gauge: C_{mu nu} + C_{nu mu}^T = 0
Cg = {}
for (a, b), O in QFv.items():
    for mu, Ga in GAUGE.get(a, {}).items():
        for nu, Gb in GAUGE.get(b, {}).items():
            o = rmul(rmul(rT(Ga), O), Gb)
            Cg[(mu, nu)] = radd(Cg.get((mu, nu), {}), o)
p2 = True
for mu in XIS:
    for nu in XIS:
        s = radd(Cg.get((mu, nu), {}), rT(Cg.get((nu, mu), {})))
        p2 &= rzero(s)
check("P2 the quadratic form vanishes identically on pure-gauge configurations (C + C^T = 0 for all pairs)", p2)

# with source: the Noether combination must vanish -> conservation laws on (rho, J, S)
QFs = build_QF(True)
ELs = qf_EL(QFs, FIELDS)
LAWS = {}
for mu in XIS:
    acc = {}
    for f, gens in GAUGE.items():
        if mu in gens:
            acc = ladd(acc, lop(rT(gens[mu]), ELs[f]))
    # field part must vanish (as in vacuum); the remainder is the law on the sources
    fieldpart = {k: v for k, v in acc.items() if k in FIELDS}
    srcpart = {k: v for k, v in acc.items() if k in SOURCES}
    noether_ok &= lzero(fieldpart)
    LAWS[mu] = srcpart
check("P1 with a prescribed source the field part of every Noether combination still vanishes", noether_ok)


def show_lin(x):
    def show_op(o):
        parts = []
        for (e, d, l), v in sorted(o.items()):
            s = "%s" % v
            if e:
                s += " E^%d" % e
            if d:
                s += " D"
            if l:
                s += " L" + ("^%d" % l if l > 1 else "")
            parts.append(s)
        return "(" + " + ".join(parts) + ")"
    return "  ".join("%s %s" % (show_op(o), f) for f, o in sorted(x.items()))


# expected laws (derived by hand): xi0: (1 - E) rho - D J3 = 0 ; xi_i: (E^-1 - 1) J_i - D S_i3 = 0
law0 = ladd(lvar("rho", radd(ONE, rscale(E, -1))), lvar("J3", rscale(D, -1)))
law1 = ladd(lvar("J1", radd(Einv, rscale(ONE, -1))), lvar("S13", rscale(D, -1)))
law2 = ladd(lvar("J2", radd(Einv, rscale(ONE, -1))), lvar("S23", rscale(D, -1)))
law3 = ladd(lvar("J3", radd(Einv, rscale(ONE, -1))), lvar("S33", rscale(D, -1)))
check("P1 conservation laws: xi0 gives (1 - E) rho = D J3; xi_i gives (E^-1 - 1) J_i = D S_i3 (i = 1,2,3)",
      lzero(ladd(LAWS["xi0"], lscale(law0, -1))) and lzero(ladd(LAWS["xi1"], lscale(law1, -1)))
      and lzero(ladd(LAWS["xi2"], lscale(law2, -1))) and lzero(ladd(LAWS["xi3"], lscale(law3, -1))))

# expected Euler-Lagrange expressions (hand-derived), vacuum, gravitational factor 1 (i.e. times 1/(2 lambda) * 2 ... see README)
tau_expr = lscale(ladd(lvar("h11"), lvar("h22")), Fr(1, 2))
EL_expected = {
    "n": lop(Lop, tau_expr),                                                    # L tau
    "N1": lscale(lop(D, ladd(lvar("h13", DELTA), lscale(lvar("N1", D), -1))), Fr(1, 2)),   # (1/2) D (Delta h13 - D N1) = D K13
    "N2": lscale(lop(D, ladd(lvar("h23", DELTA), lscale(lvar("N2", D), -1))), Fr(1, 2)),
    "N3": lscale(lop(D, lop(DELTA, tau_expr)), -1),                            # - D Delta tau
}
el_ok = all(lzero(ladd(ELv[f], lscale(EL_expected[f], -1))) for f in EL_expected)
check("P1 constraint expressions: EL_n = L tau, EL_N1 = D K13, EL_N2 = D K23, EL_N3 = -D Delta tau (gravitational factor 1/(2 lambda) stripped)", el_ok)

# constraint propagation read off the Noether identities:
#   xi0:  -(1 - E) EL_n - D EL_N3 = 0   ->  Delta(EL_n) = -D EL_N3 ... printed below
# ============================================================ P3: explicit D_c model on Z/5 x Z/4
def P(var=None, c=Fr(1)):
    return {(): Fr(c)} if var is None else {((var, 1),): Fr(c)}


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


def psum(ps):
    out = {}
    for p in ps:
        out = padd(out, p)
    return out


def pdiff(p, var):
    out = {}
    for k, v in p.items():
        d = dict(k)
        e = d.get(var, 0)
        if e == 0:
            continue
        d[var] = e - 1
        if d[var] == 0:
            del d[var]
        kk = tuple(sorted(d.items()))
        out[kk] = out.get(kk, Fr(0)) + v * e
    return {k: v for k, v in out.items() if v != 0}


def peval(p, s):
    tot = Fr(0)
    for k, v in p.items():
        t = v
        for var, e in k:
            t *= s[var] ** e
        tot += t
    return tot


NS, NT = 5, 4


def vname(f, n, r):
    return "%s_%d_%d" % (f, n % NT, r % NS)


def V(f, n, r):
    return P(vname(f, n, r))


def Dc_list(f, n):   # centered difference of field f at slice n, list over r, polynomials
    return [pscale(padd(V(f, n, r + 1), pscale(V(f, n, r - 1), -1)), Fr(1, 2)) for r in range(NS)]


def Dc_vec(vec):
    return [(vec[(r + 1) % NS] - vec[(r - 1) % NS]) / 2 for r in range(NS)]


def Lc_vec(vec):
    return [-x for x in Dc_vec(Dc_vec(vec))]


def build_action_poly(shift_fields=True):
    terms = []
    for n in range(NT):
        DN1 = Dc_list("N1", n) if shift_fields else [P(None, 0)] * NS
        DN2 = Dc_list("N2", n) if shift_fields else [P(None, 0)] * NS
        DN3 = Dc_list("N3", n) if shift_fields else [P(None, 0)] * NS
        Dh = {key: Dc_list(key, n) for key in METRIC}
        for r in range(NS):
            dh = {key: padd(V(key, n + 1, r), pscale(V(key, n, r), -1)) for key in METRIC}
            K11 = pscale(dh["h11"], Fr(1, 2))
            K22 = pscale(dh["h22"], Fr(1, 2))
            K12 = pscale(dh["h12"], Fr(1, 2))
            K13 = pscale(padd(dh["h13"], pscale(DN1[r], -1)), Fr(1, 2))
            K23 = pscale(padd(dh["h23"], pscale(DN2[r], -1)), Fr(1, 2))
            K33 = pscale(padd(dh["h33"], pscale(DN3[r], -2)), Fr(1, 2))
            Ktr = padd(padd(K11, K22), K33)
            kin = psum([pmul(K11, K11), pmul(K22, K22), pmul(K33, K33),
                        pscale(pmul(K12, K12), 2), pscale(pmul(K13, K13), 2), pscale(pmul(K23, K23), 2),
                        pscale(pmul(Ktr, Ktr), -1)])
            Dhsum = padd(padd(Dh["h11"][r], Dh["h22"][r]), Dh["h33"][r])
            G2 = psum([pscale(pmul(Dh["h13"][r], Dh["h13"][r]), Fr(1, 2)),
                       pscale(pmul(Dh["h23"][r], Dh["h23"][r]), Fr(1, 2)),
                       pscale(pmul(Dh["h33"][r], Dh["h33"][r]), Fr(1, 2)),
                       pscale(pmul(Dh["h33"][r], Dhsum), Fr(-1, 2)),
                       pscale(pmul(Dhsum, Dhsum), Fr(1, 4)),
                       pscale(psum([pmul(Dh["h11"][r], Dh["h11"][r]), pmul(Dh["h22"][r], Dh["h22"][r]),
                                    pmul(Dh["h33"][r], Dh["h33"][r]), pscale(pmul(Dh["h12"][r], Dh["h12"][r]), 2),
                                    pscale(pmul(Dh["h13"][r], Dh["h13"][r]), 2), pscale(pmul(Dh["h23"][r], Dh["h23"][r]), 2)]),
                              Fr(-1, 4))])
            terms.append(kin)
            terms.append(G2)
        # lapse term: n R_1 with R_1 = D D h33 - D D h  (D D = -L_c)
        def DcDc(key):
            first = Dc_list(key, n)
            return [pscale(padd(first[(r + 1) % NS], pscale(first[(r - 1) % NS], -1)), Fr(1, 2)) for r in range(NS)]
        DD33 = DcDc("h33")
        DD11 = DcDc("h11")
        DD22 = DcDc("h22")
        for r in range(NS):
            R1 = padd(DD33[r], pscale(padd(padd(DD11[r], DD22[r]), DD33[r]), -1))
            terms.append(pmul(V("n", n, r), R1))
    # overall factor 1/2 on the gravitational part (the 1/(2 lambda) with lambda scaled out)
    return pscale(psum(terms), Fr(1, 2))


ACT = build_action_poly()
# gauge transformation as substitution phi -> phi + G xi
def gauge_subst():
    sub = {}
    for n in range(NT):
        for r in range(NS):
            xi0 = lambda nn, rr: V("xi0", nn, rr)
            xi = lambda i, nn, rr: V("xi%d" % i, nn, rr)
            Dxi = lambda i, nn, rr: pscale(padd(V("xi%d" % i, nn, rr + 1), pscale(V("xi%d" % i, nn, rr - 1), -1)), Fr(1, 2))
            sub[vname("h13", n, r)] = padd(V("h13", n, r), Dxi(1, n, r))
            sub[vname("h23", n, r)] = padd(V("h23", n, r), Dxi(2, n, r))
            sub[vname("h33", n, r)] = padd(V("h33", n, r), pscale(Dxi(3, n, r), 2))
            sub[vname("N1", n, r)] = padd(V("N1", n, r), padd(xi(1, n + 1, r), pscale(xi(1, n, r), -1)))
            sub[vname("N2", n, r)] = padd(V("N2", n, r), padd(xi(2, n + 1, r), pscale(xi(2, n, r), -1)))
            sub[vname("N3", n, r)] = padd(V("N3", n, r), padd(padd(xi(3, n + 1, r), pscale(xi(3, n, r), -1)), Dxi(0, n, r)))
            sub[vname("n", n, r)] = padd(V("n", n, r), pscale(padd(xi0(n, r), pscale(xi0(n - 1, r), -1)), -1))
    return sub


def psubst(p, sub):
    out = {}
    for k, v in p.items():
        term = {(): v}
        for var, e in k:
            base = sub.get(var, P(var))
            for _ in range(e):
                term = pmul(term, base)
        out = padd(out, term)
    return out


ACTg = psubst(ACT, gauge_subst())
check("P3 explicit D_c model, time periodic: S(phi + G xi) - S(phi) = 0 as a polynomial identity in all 200 field and 80 gauge variables",
      padd(ACTg, pscale(ACT, -1)) == {})

# P3: Euler-Lagrange equations of the explicit model agree with the P1 operator expressions instantiated with D_c
def inst(linexpr, n, r):
    # instantiate a P1 linear expression (in fields) at slice n, site r, into a polynomial
    out = {}
    for f, o in linexpr.items():
        for (e, d, l), v in o.items():
            # apply E^e then D^d then L^l to field f: build the vector over sites at slice n+e
            vec = [V(f, n + e, rr) for rr in range(NS)]
            for _ in range(d):
                vec = [pscale(padd(vec[(rr + 1) % NS], pscale(vec[(rr - 1) % NS], -1)), Fr(1, 2)) for rr in range(NS)]
            for _ in range(l):
                dv = [pscale(padd(vec[(rr + 1) % NS], pscale(vec[(rr - 1) % NS], -1)), Fr(1, 2)) for rr in range(NS)]
                vec = [pscale(pscale(padd(dv[(rr + 1) % NS], pscale(dv[(rr - 1) % NS], -1)), Fr(1, 2)), -1) for rr in range(NS)]
            out = padd(out, pscale(vec[r], v))
    return out


agree = True
for f in FIELDS:
    for n in range(NT):
        for r in range(NS):
            lhs = pdiff(ACT, vname(f, n, r))
            rhs = inst(ELv[f], n, r)   # both representations carry the same overall 1/2
            agree &= (padd(lhs, pscale(rhs, -1)) == {})
check("P3 Euler-Lagrange polynomials of the explicit model equal the P1 operator expressions instantiated with D_c (all 10 fields, all slices, all sites)", agree)

# P4: no rational antisymmetric circulant D on Z/5 with -D^2 = L_public
shells = {(1, 1, 0): Fr(6, 324), (2, 0, 0): Fr(1, 324), (2, 2, 0): Fr(15, 324), (3, 1, 0): Fr(1, 324), (4, 0, 0): Fr(1, 324)}
vectors = {}
for base, c in shells.items():
    S_ = set()
    for p in set(permutations(base)):
        for signs in product((1, -1), repeat=3):
            S_.add(tuple(s * x for s, x in zip(signs, p)))
    for v in S_:
        vectors[v] = c
by3 = {}
for v, c in vectors.items():
    by3[v[2] % 5] = by3.get(v[2] % 5, Fr(0)) + c
m1, m2 = by3[1], by3[2]
check("P4 public planar rates m1 = 29/324, m2 = 65/324", (m1, m2) == (Fr(29, 324), Fr(65, 324)))
# D = x (S - S^-1) + y (S^2 - S^-2); -D^2 = 2(x^2+y^2) - (x^2 + 2xy)(S^2 + S^-2) - (y^2 - 2xy)(S + S^-1)
# match with L = 2(m1+m2) - m2 (S^2+S^-2) - m1 (S+S^-1):  x^2 + 2xy = m2,  y^2 - 2xy = m1  (diagonal follows by addition)
# verify the circulant identity symbolically with polynomials in x, y
x, y = P("x"), P("y")
# represent circulants as dict shift -> polynomial
Dcirc = {1: x, -1: pscale(x, -1), 2: y, -2: pscale(y, -1)}
D2 = {}
for s1, a in Dcirc.items():
    for s2, b in Dcirc.items():
        s = (s1 + s2) % 5
        s = s - 5 if s > 2 else s
        D2[s] = padd(D2.get(s, {}), pmul(a, b))
negD2 = {s: pscale(p, -1) for s, p in D2.items()}
expect = {0: pscale(padd(pmul(x, x), pmul(y, y)), 2),
          2: pscale(padd(pmul(x, x), pscale(pmul(x, y), 2)), -1), -2: pscale(padd(pmul(x, x), pscale(pmul(x, y), 2)), -1),
          1: pscale(padd(pmul(y, y), pscale(pmul(x, y), -2)), -1), -1: pscale(padd(pmul(y, y), pscale(pmul(x, y), -2)), -1)}
check("P4 -D^2 for D = x(S - S^-1) + y(S^2 - S^-2) has the displayed circulant entries (symbolic)",
      all(padd(negD2.get(s, {}), pscale(expect[s], -1)) == {} for s in (0, 1, -1, 2, -2)))
# -D^2 = L_public  <=>  x^2 + 2xy = m2 and y^2 - 2xy = m1. With t = y/x: (t^2 - 2t)/(1 + 2t) = m1/m2 -> 65 t^2 - 188 t - 29 = 0
disc = 188 * 188 + 4 * 65 * 29
check("P4 rational D requires a rational root of 65 t^2 - 188 t - 29; discriminant 42884 = 4 . 71 . 151 is not a square; x = 0 gives y^2 = 29/324, also not rational",
      disc == 42884 and 42884 == 4 * 71 * 151 and isqrt(disc) ** 2 != disc and isqrt(29 * 324) ** 2 != 29 * 324)
# and D_c: -D_c^2 has entries (1/2, -1/4, -1/4 at shifts 0, +-2): a different Laplacian
check("P4 the rational D_c gives L_c = -D_c^2 with entries 1/2 at 0 and -1/4 at shifts +-2, not the public stencil",
      Lc_vec([Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]) == [Fr(1, 2), Fr(0), Fr(-1, 4), Fr(-1, 4), Fr(0)])

# P5: K1 source and the conservation laws
words = {"0010": Fr(1, 12), "0011": Fr(1, 12), "0100": Fr(1, 12), "0101": Fr(1, 12), "0110": Fr(1, 6),
         "1001": Fr(1, 6), "1010": Fr(1, 12), "1011": Fr(1, 12), "1100": Fr(1, 12), "1101": Fr(1, 12)}


def u(w, t):
    b = [int(ch) for ch in w]
    return b[t + 2] - b[t]


def iota(w, t):
    ut = u(w, t)
    return [Fr(1, 2) if (r == ut % 5 or r == (ut + 1) % 5) else Fr(0) for r in range(5)]


# rank facts: kernel of D_c and of L_public on Z/5 is the constants
def rank(rows):
    A = [list(r) for r in rows]
    rk = 0
    cols = len(A[0])
    for c in range(cols):
        piv = None
        for i in range(rk, len(A)):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        inv = 1 / A[rk][c]
        A[rk] = [v * inv for v in A[rk]]
        for i in range(len(A)):
            if i != rk and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[rk])]
        rk += 1
    return rk


Dc_mat = [Dc_vec([Fr(int(i == j)) for i in range(5)]) for j in range(5)]   # columns
Dc_rows = [[Dc_mat[j][i] for j in range(5)] for i in range(5)]
Lpub_rows = [[Fr(188, 324) if i == j else (Fr(-29, 324) if (i - j) % 5 in (1, 4) else Fr(-65, 324)) for j in range(5)] for i in range(5)]
check("P5 rank D_c = 4 and rank L_public = 4 on Z/5: both annihilate exactly the constants", rank(Dc_rows) == 4 and rank(Lpub_rows) == 4)
# covector K1 source: rho = iota/2, J = 0, S33 = -iota/2. Law xi3: (E^-1 - 1) J3 = D S33 -> with J = 0 needs D S33 = 0 -> D iota = 0
dc_nonzero = all(any(v != 0 for v in Dc_vec(iota(w, t))) for w in words for t in (0, 1))
static_fail = sum(1 for w in words if iota(w, 0) != iota(w, 1))
check("P5 covector K1 source: D_c iota != 0 for all ten words and both cuts (momentum law fails with J = 0); (1 - E) rho = 0 fails for 6 of 10 words",
      dc_nonzero and static_fail == 6)


def solve_Dc(rhs):
    # solve D_c x = rhs, sum x = 0, rhs mean zero
    assert sum(rhs) == 0
    A = [Dc_rows[i] + [rhs[i]] for i in range(5)] + [[Fr(1)] * 5 + [Fr(0)]]
    rk = 0
    for c in range(5):
        piv = None
        for i in range(rk, 6):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        inv = 1 / A[rk][c]
        A[rk] = [v * inv for v in A[rk]]
        for i in range(6):
            if i != rk and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[rk])]
        rk += 1
    assert A[5][5] == 0
    xsol = [A[i][5] for i in range(5)]
    assert Dc_vec(xsol) == rhs and sum(xsol) == 0
    return xsol


# conserved completion for word 0010 with D_c: J3 at the half slice from (1 - E) rho = D J3, i.e. rho_0 - rho_1 = D_c J3
w = "0010"
rho0 = [v / 2 for v in iota(w, 0)]
rho1 = [v / 2 for v in iota(w, 1)]
J3 = solve_Dc([a - b for a, b in zip(rho0, rho1)])
check("P5 a conserved completion exists for the K1 intensities: J3 = D_c^-1 (rho_0 - rho_1) is exact and mean-zero for word 0010; the transverse stress S11, S22, S12 is unconstrained by the planar laws",
      Dc_vec(J3) == [a - b for a, b in zip(rho0, rho1)] and sum(J3) == 0)

# P6: zero mode of the Hamiltonian constraint on the static flat background
check("P6 k = 0: EL_n reduces to -rho_hat_0 (L and D annihilate constants); sum rho = a^2/2 > 0 for every K1 word: no static flat solution",
      all(sum(iota(w, t)) == 1 for w in words for t in (0, 1)))

# P7: sector reduction, explicit model
# (a) witness h13 = n f(r), N = 0: momentum constraint EL_N1 = (1/2) D_c (Delta h13 - D_c N1) fails at interior slices
f_wit = [Fr(1), Fr(-2), Fr(3), Fr(-1), Fr(-1)]


def EL_numeric(linexpr, fields_num, n, r):
    # fields_num[f][n] = list over r; slices 0..3 non-periodic; evaluate at interior n
    tot = Fr(0)
    for f, o in linexpr.items():
        for (e, d, l), v in o.items():
            vec = list(fields_num[f][n + e])
            for _ in range(d):
                vec = Dc_vec(vec)
            for _ in range(l):
                vec = Lc_vec(vec)
            tot += v * vec[r]
    return tot


zero5 = [Fr(0)] * 5
wit = {f: [list(zero5) for _ in range(4)] for f in FIELDS}
for n in range(4):
    wit["h13"][n] = [Fr(n) * v for v in f_wit]
viol = any(EL_numeric(ELv["N1"], wit, n, r) != 0 for n in (1, 2) for r in range(5))
others_ok = all(EL_numeric(ELv[f], wit, n, r) == 0 for f in FIELDS if f != "N1" for n in (1, 2) for r in range(5))
check("P7 witness h13 = n f(r) with N = 0: every equation holds except the momentum constraint EL_N1, which fails (FC part 1)", viol and others_ok)
# (b) with N1 = D_c^-1 f the witness is pure gauge: all equations hold
N1sol = solve_Dc(f_wit)
wit2 = {f: [list(v) for v in wit[f]] for f in FIELDS}
for n in range(4):
    wit2["N1"][n] = list(N1sol)
allok = all(EL_numeric(ELv[f], wit2, n, r) == 0 for f in FIELDS for n in (1, 2) for r in range(5))
check("P7 witness with N1 = D_c^-1 f: all equations hold; it is the pure-gauge configuration xi1 = n D_c^-1 f (FC part 2)", allok)
# (c) TT-only data are exact solutions: h_+ = (h11 - h22)/2 with h11 = -h22, h12 free, evolved by Delta^2 h + L_c h = 0, all else zero
import random
random.seed(20260908)
hp = [[Fr(random.randint(-3, 3)) for _ in range(5)] for _ in range(2)]
hx = [[Fr(random.randint(-3, 3)) for _ in range(5)] for _ in range(2)]
for _ in range(2):
    hp.append([2 * hp[-1][r] - hp[-2][r] - Lc_vec(hp[-1])[r] for r in range(5)])
    hx.append([2 * hx[-1][r] - hx[-2][r] - Lc_vec(hx[-1])[r] for r in range(5)])
tt = {f: [list(zero5) for _ in range(4)] for f in FIELDS}
for n in range(4):
    tt["h11"][n] = list(hp[n])
    tt["h22"][n] = [-v for v in hp[n]]
    tt["h12"][n] = list(hx[n])
tt_ok = all(EL_numeric(ELv[f], tt, n, r) == 0 for f in FIELDS for n in (1, 2) for r in range(5))
check("P7 TT-only data (h11 = -h22 = h_+, h12 = h_x) evolved by Delta^2 h + L_c h = 0 with n = N = tau = ell = vector = 0 satisfy every constraint and evolution equation", tt_ok)
# (d) in the gauge N = 0, ell = 0 the constraints force tau constant in space and Delta h13, Delta h23 constant in space (rank facts above): FD decided at linear order

# ============================================================ report
print("C-TT-SHIFT-CONSTRAINT-N verifier, exact arithmetic")
for tag, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + tag)
bad = [t for t, ok in CHECKS if not ok]
print("checks:", len(CHECKS), "failed:", len(bad))
print()
print("P1 Euler-Lagrange expressions (vacuum, gravitational factor 1/(2 lambda) stripped):")
for f in FIELDS:
    print("  EL_%-3s = %s" % (f, show_lin(ELv[f])))
print()
print("P1 Noether identities (each is identically zero; displayed as the combination G^T EL):")
for mu in XIS:
    comb = []
    for f, gens in GAUGE.items():
        if mu in gens:
            comb.append("(%s)^T EL_%s" % (show_lin({"": gens[mu]}).strip(), f))
    print("  %s: %s = 0" % (mu, " + ".join(comb)))
print()
print("P1 conservation laws required of a prescribed source:")
for mu in XIS:
    print("  %s: %s = 0" % (mu, show_lin(LAWS[mu])))
print()
print("P5 conserved completion, word 0010: rho_0 - rho_1 =", [str(v) for v in [a - b for a, b in zip(rho0, rho1)]])
print("    J3 (half slice) =", [str(v) for v in J3])
print("P7 witness N1 = D_c^-1 f =", [str(v) for v in N1sol], " for f =", [str(v) for v in f_wit])
print("P3 action polynomial: %d monomials" % len(ACT))
raise SystemExit(1 if bad else 0)
