#!/usr/bin/env python3
"""P-RECORD-QUOTIENT-CALCULUS-1 accepted verifier.

Scope: exactly the record-quotient calculus R1-R6 at layer L1. No physical
selection of an ideal, apparatus, event semantics, atom selection, decoder,
measure, coarse-graining, RG or continuum statement, write/read/scale naming,
neighbouring-ring census, unit-rank minimality, or L2-L6 lift is verified.

R = Z[zeta_5] = Z[X]/Phi_5, basis (1, z, z^2, z^3), lambda = 1 - z.
Ideals are Hermite normal forms of sublattices of Z^4; quotients R/I are
enumerated over the HNF box, so ideals that are not rational conductors
(such as lambda^L (2)) are handled directly.

Design rule: scientific gates use explicit finite constructions and, where a
comparison is load-bearing, the separate routes are named. This accepted
implementation is adapted from result-exposed incubation work, but these exact
bytes must be pinned before any formal execution. The incubation mutation audit
is discovery context only and is not part of this five-file evidence bundle.

LOEWY CONVENTION (load-bearing): n_I = rad(I)/I and n^0 = R/I, so layer k is
n^k/n^(k+1) for k >= 0 and the FIRST listed layer is n^0/n^1 = R/rad(I) of
order N(rad I). Starting the list at n^1 gives a different, wrong table;
gate L4 exhibits that difference against a route that never sees the chain.

Standard library only, exact integers, no floats, deterministic, single
process, no file writes, no network.

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
        python3 probes/P-RECORD-QUOTIENT-CALCULUS-1/verify.py
"""

from itertools import combinations, product

GATES = []


def gate(label, condition, detail=""):
    GATES.append((label, bool(condition)))
    line = ("PASS " if condition else "FAIL ") + label
    if detail:
        line += "   " + detail
    print(line)


# --------------------------------------------------------------- ring R

def rmul(a, b):
    c = [0] * 7
    for i in range(4):
        if a[i]:
            for j in range(4):
                c[i + j] += a[i] * b[j]
    for i in range(6, 3, -1):
        t = c[i]
        if t:
            c[i] = 0
            for j in range(i - 4, i):
                c[j] -= t
    return tuple(c[:4])


def radd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def rsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def rpow(a, n):
    r = (1, 0, 0, 0)
    for _ in range(n):
        r = rmul(r, a)
    return r


ONE = (1, 0, 0, 0)
ZERO = (0, 0, 0, 0)
Z = (0, 1, 0, 0)
LAM = rsub(ONE, Z)
BASIS = [rpow(Z, j) for j in range(4)]


# ------------------------------------------------------ ideals as lattices

def hnf(rows):
    rows = [list(r) for r in rows if any(r)]
    H = []
    for col in range(4):
        while True:
            nz = [r for r in rows if r[col] != 0]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda r: abs(r[col]))
            base = nz[0]
            for r in nz[1:]:
                q = r[col] // base[col]
                for j in range(4):
                    r[j] -= q * base[j]
        nz = [r for r in rows if r[col] != 0]
        if nz:
            p = nz[0]
            if p[col] < 0:
                p = [-x for x in p]
            H.append(p[:])
            rows = [r for r in rows if r[col] == 0 or r is not nz[0]]
            rows = [r for r in rows if any(r)]
            for r in rows:
                if r[col] != 0:
                    q = r[col] // p[col]
                    for j in range(4):
                        r[j] -= q * p[j]
        else:
            H.append([0] * 4)
    for i in range(4):
        for k in range(i):
            if H[i][i]:
                q = H[k][i] // H[i][i]
                for j in range(4):
                    H[k][j] -= q * H[i][j]
    return tuple(tuple(r) for r in H)


def ideal(gens):
    return hnf([rmul(g, b) for g in gens for b in BASIS])


def inorm(H):
    return H[0][0] * H[1][1] * H[2][2] * H[3][3]


def ired(v, H):
    v = list(v)
    for i in range(4):
        if H[i][i]:
            q = v[i] // H[i][i]
            for j in range(4):
                v[j] -= q * H[i][j]
    return tuple(v)


def cells(H):
    return [ired(v, H) for v in product(*[range(H[i][i]) for i in range(4)])]


def isum(A, B):
    return hnf([list(r) for r in A] + [list(r) for r in B])


def imul(A, B):
    return hnf([rmul(a, b) for a in A for b in B])


def ipow(A, k):
    r = ideal([ONE])
    for _ in range(k):
        r = imul(r, A)
    return r


def isub(A, B):
    """A contained in B?"""
    return all(ired(r, B) == ZERO for r in A)


R_FULL = ideal([ONE])

print("P-RECORD-QUOTIENT-CALCULUS-1 -- exact record quotient calculus R1-R6")
print("R = Z[zeta_5] = Z[X]/Phi_5; ideals as HNF sublattices of Z^4")
print("LOEWY CONVENTION: n^0 = R/I; layer k is n^k/n^(k+1); the first listed")
print("layer is n^0/n^1 = R/rad(I), of order N(rad I). See gate L4.")
print("ROUTE DISCIPLINE: independent exact constructions; finite audit of a written proof")
print("FORMAL SCOPE: 31 gates, L1 only, no sampling claim beyond the frozen carrier")
print("")
print("-- Part 0: ring and lattice machinery")

gate("W1  z^5 = 1 and 1+z+z^2+z^3+z^4 = 0",
     rpow(Z, 5) == ONE
     and radd(radd(radd(radd(ONE, Z), rpow(Z, 2)), rpow(Z, 3)),
              rpow(Z, 4)) == ZERO,
     "repeated multiplication vs the summed defining relation")
gate("W2  rmul agrees with hand expansion: (1+z)(1+z^2) = 1+z+z^2+z^3",
     rmul(radd(ONE, Z), radd(ONE, rpow(Z, 2))) == (1, 1, 1, 1),
     "independent hand expansion")
_I80 = ideal([rmul(LAM, (2, 0, 0, 0))])
_box80 = cells(_I80)
_sweep = set(ired(v, _I80) for v in product(range(-6, 7), repeat=4))
gate("W3  HNF box is a complete irredundant residue system",
     len(set(_box80)) == len(_box80) == inorm(_I80)
     and _sweep == set(_box80)
     and all(ired(radd(v, r), _I80) == v for v in _box80 for r in _I80),
     "box size vs determinant; a 13^4 sweep lands in the same %d classes; "
     "reduction is constant on cosets" % inorm(_I80))
_A, _B = ideal([LAM]), ideal([(2, 0, 0, 0)])
gate("W4  selected ideal products have the frozen multiplicative norms",
     inorm(imul(_A, _B)) == inorm(_A) * inorm(_B) == 80
     and inorm(ipow(_A, 4)) == inorm(ideal([(5, 0, 0, 0)])) == 625,
     "lattice determinant of the product vs product of determinants")

print("")
print("-- Part 1: primes above p and residue fields")


def poly_factor_mod_p(p):
    phi = [1, 1, 1, 1, 1]

    def pdiv(num, den):
        num = list(num)
        dd = len(den) - 1
        q = [0] * max(1, len(num) - dd)
        for i in range(len(num) - 1, dd - 1, -1):
            if num[i] % p:
                c = (num[i] * pow(den[dd], p - 2, p)) % p
                q[i - dd] = c
                for j in range(dd + 1):
                    num[i - dd + j] = (num[i - dd + j] - c * den[j]) % p
        return q, [x % p for x in num[:dd]]

    facs, rest = [], phi
    changed = True
    while changed:
        changed = False
        for d in (1, 2):
            if len(rest) - 1 < d or changed:
                continue
            for co in product(range(p), repeat=d):
                cand = list(co) + [1]
                q, rem = pdiv(rest, cand)
                if all(x == 0 for x in rem):
                    facs.append(tuple(cand))
                    rest = [x % p for x in q]
                    changed = True
                    break
    if len(rest) > 1:
        facs.append(tuple(x % p for x in rest))
    # DISTINCT primes: the ramified factor (x-1) occurs with multiplicity 4
    # at p = 5, but it is one prime ideal.  Ramification indices are recovered
    # independently by valuation(), never from this multiplicity.
    return sorted(set(facs))


class Prime(object):
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.f = len(g) - 1
        self.norm = p ** self.f
        gens = [(p, 0, 0, 0)]
        if self.f < 4:
            poly = ZERO
            for i, c in enumerate(g):
                poly = radd(poly, tuple(c * x for x in BASIS[i]))
            gens.append(poly)
        self.ideal = ideal(gens)

    def reduce(self, a):
        num = [x % self.p for x in a]
        d = len(self.g) - 1
        for i in range(len(num) - 1, d - 1, -1):
            c = num[i]
            if c:
                num[i] = 0
                for j in range(d + 1):
                    num[i - d + j] = (num[i - d + j] - c * self.g[j]) % self.p
        return tuple(num[:d])

    def __repr__(self):
        return "P(%d;%s)" % (self.p, "".join(str(c) for c in self.g))


PRIME_CACHE = {}


def primes_above(p):
    if p not in PRIME_CACHE:
        PRIME_CACHE[p] = [Prime(p, g) for g in poly_factor_mod_p(p)]
    return PRIME_CACHE[p]


P5, P2, P3, P11 = (primes_above(p) for p in (5, 2, 3, 11))

gate("F1  5 is totally ramified: one prime, f = 1, and lambda^4 = (5)",
     len(P5) == 1 and P5[0].f == 1
     and ipow(P5[0].ideal, 4) == ideal([(5, 0, 0, 0)])
     and inorm(P5[0].ideal) == 5,
     "factorization route and the lattice identity lambda^4 = (5) agree")
gate("F2  2 and 3 are inert, f = 4: factor degree = ord_5(p)",
     len(P2) == 1 and P2[0].norm == 16 and len(P3) == 1 and P3[0].norm == 81
     and all(next(k for k in range(1, 5) if pow(p, k, 5) == 1) == 4
             for p in (2, 3)),
     "N(P) = 16 and 81")
_roots11 = sorted(r for r in range(2, 11) if pow(r, 5, 11) == 1)
gate("F3  11 splits completely: four primes of norm 11, one per fifth root",
     len(P11) == 4 and all(P.f == 1 and P.norm == 11 for P in P11)
     and sorted((-P.g[0]) % 11 for P in P11) == _roots11 == [3, 4, 5, 9],
     "roots %s found by search match the linear factors" % (_roots11,))
gate("F4  ker(reduce) is P and the image has |kappa(P)| = N(P)",
     all(len(set(P.reduce(v)
                     for v in product(range(P.p), repeat=4))) == P.norm
             and inorm(P.ideal) == P.norm
             and all(P.reduce(r) == (0,) * P.f for r in P.ideal)
             for P in P2 + P5 + P3 + P11),
     "P lies in the kernel; equal finite indices identify it with the kernel")
_ringmap = True
for P in (P2[0], P5[0], P3[0], P11[0]):
    smp = list(product(range(P.p), repeat=4))[::max(1, P.p ** 4 // 50)]
    for a in smp:
        for b in smp:
            if P.reduce(radd(a, b)) != tuple(
                    (x + y) % P.p for x, y in zip(P.reduce(a), P.reduce(b))):
                _ringmap = False
            pa, pb = P.reduce(a), P.reduce(b)
            cc = [0] * (2 * len(pa) + 1)
            for i, x in enumerate(pa):
                for j, y in enumerate(pb):
                    cc[i + j] = (cc[i + j] + x * y) % P.p
            d = len(P.g) - 1
            for i in range(len(cc) - 1, d - 1, -1):
                c = cc[i]
                if c:
                    cc[i] = 0
                    for j in range(d + 1):
                        cc[i - d + j] = (cc[i - d + j] - c * P.g[j]) % P.p
            if P.reduce(rmul(a, b)) != tuple(cc[:d]):
                _ringmap = False
gate("F5  reduction R -> kappa(P) is a RING map (sum and product)", _ringmap,
     "reduce-then-operate vs operate-then-reduce, four primes")

print("")
print("-- Part 2: R1  Idem(R/I) = P(Supp I), canonically")

ALL_P = {"lam": P5[0], "2": P2[0], "3": P3[0]}
FAMILY = [
    ("lambda", ideal([LAM])),
    ("(2)", P2[0].ideal),
    ("(3)", P3[0].ideal),
    ("(4)", ipow(P2[0].ideal, 2)),
    ("(5)", ideal([(5, 0, 0, 0)])),
    ("(6)", ideal([(6, 0, 0, 0)])),
    ("lambda(2)", imul(ideal([LAM]), P2[0].ideal)),
    ("lambda^2(2)", imul(ipow(ideal([LAM]), 2), P2[0].ideal)),
    ("(10)", ideal([(10, 0, 0, 0)])),
    ("(11)", ideal([(11, 0, 0, 0)])),
    ("(20)", ideal([(20, 0, 0, 0)])),
]
CAND_PRIMES = [P for p in (2, 3, 5, 11) for P in primes_above(p)]


def support(I):
    return [P for P in CAND_PRIMES if isub(I, P.ideal)]


def idempotents(I):
    return [e for e in cells(I) if ired(rmul(e, e), I) == e]


DATA = {}
for lab, I in FAMILY:
    idm = idempotents(I)
    sup = support(I)
    DATA[lab] = (I, idm, sup,
                 {e: frozenset(P for P in sup
                               if P.reduce(e) == P.reduce(ONE)) for e in idm})

_bij = _wf = True
for lab, _ in FAMILY:
    I, idm, sup, sig = DATA[lab]
    for e in idm:
        for P in sup:
            if P.reduce(e) not in (P.reduce(ONE), P.reduce(ZERO)):
                _wf = False
    subsets = set(frozenset(s) for k in range(len(sup) + 1)
                  for s in combinations(sup, k))
    if set(sig.values()) != subsets or len(set(sig.values())) != len(idm):
        _bij = False
gate("R1a e -> {P : e = 1 in kappa(P)} is a BIJECTION onto the power set",
     _bij and _wf,
     "%d ideals; surjective AND injective onto P(Supp), not a count match"
     % len(FAMILY))
gate("R1b |Idem(R/I)| = 2^|Supp I|: enumeration vs prime count",
     all(len(DATA[l][1]) == 2 ** len(DATA[l][2]) for l, _ in FAMILY),
     "; ".join("%s:%d" % (l, len(DATA[l][1])) for l, _ in FAMILY))
_bool = True
for lab, _ in FAMILY:
    I, idm, sup, sig = DATA[lab]
    for a in idm:
        for b in idm:
            if sig[ired(rmul(a, b), I)] != sig[a] & sig[b]:
                _bool = False
            if sig[ired(rsub(radd(a, b), rmul(a, b)), I)] != sig[a] | sig[b]:
                _bool = False
        if sig[ired(rsub(ONE, a), I)] != frozenset(sup) - sig[a]:
            _bool = False
gate("R1c BOOLEAN isomorphism: ef -> cap, e+f-ef -> cup, 1-e -> complement",
     _bool, "every idempotent pair of every ideal in the family")
_atom = True
for lab, _ in FAMILY:
    I, idm, sup, sig = DATA[lab]
    at = [e for e in idm if len(sig[e]) == 1]
    if len(at) != len(sup):
        _atom = False
    t = ZERO
    for e in at:
        t = ired(radd(t, e), I)
    if at and t != ired(ONE, I):
        _atom = False
    for a, b in combinations(at, 2):
        if ired(rmul(a, b), I) != ZERO:
            _atom = False
gate("R1d atoms are orthogonal, one per prime, and sum to 1", _atom,
     "atoms are labelled by the primes themselves; no numbering is used")
gate("R1e support is by PRIME: 11 splits into four, so |Idem(R/(11))| = 16",
     len(DATA["(11)"][2]) == 4 and len(DATA["(11)"][1]) == 16
     and len(DATA["(6)"][2]) == 2 and len(DATA["(6)"][1]) == 4,
     "a rational-divisor count would give 2 for both")

print("")
print("-- Part 3: R2  Idem(R/I) -> Idem(R/rad I) is a bijection")


def radical(I):
    sup = support(I)
    r = R_FULL
    for P in sup:
        r = imul(r, P.ideal)
    return r


_r2 = True
_r2d = []
for lab, _ in FAMILY:
    I, idm, sup, sig = DATA[lab]
    rad = radical(I)
    idm_r = idempotents(rad)
    img = set(ired(e, rad) for e in idm)
    if (not isub(I, rad) or img != set(idm_r)
            or len(img) != len(idm)):
        _r2 = False
    _r2d.append("%s:%d" % (lab, len(idm_r)))
gate("R2a Idem(R/I) -> Idem(R/rad I) is onto and injective", _r2,
     "I is contained in rad(I), then two separate enumerations per ideal")
gate("R2b thickness is invisible to the Boolean layer",
     len(DATA["(4)"][1]) == len(DATA["(2)"][1]) == 2
     and len(DATA["(20)"][1]) == len(DATA["(10)"][1]) == 4
     and len(DATA["lambda^2(2)"][1]) == len(DATA["lambda(2)"][1]) == 4
     and DATA["(4)"][0] != DATA["(2)"][0],
     "same Boolean algebra, provably different ideals")
gate("R2c |Supp I| = 1 gives |Idem| = 2 even when R/I is NOT a field",
     all((len(DATA[l][2]) == 1) == (len(DATA[l][1]) == 2) for l, _ in FAMILY)
     and len(DATA["(5)"][1]) == 2 and inorm(DATA["(5)"][0]) == 625,
     "tested in BOTH directions; R/(5) is local of order 625, not a field")

print("")
print("-- Part 4: R3  exact Loewy profile")


def valuation(I, P):
    k = 0
    while isub(I, ipow(P.ideal, k + 1)):
        k += 1
        if k > 12:
            break
    return k


def loewy_lattice(I):
    """Route A: layer orders as indices of rad^k + I, via HNF determinants."""
    rad = radical(I)
    out, k = [], 0
    while True:
        Lk = isum(ipow(rad, k), I)
        Lk1 = isum(ipow(rad, k + 1), I)
        if Lk == I:
            break
        out.append(inorm(Lk1) // inorm(Lk))
        k += 1
        if k > 10:
            break
    return out


def loewy_formula(I):
    """Route B: layer orders from prime norms and exponents only."""
    ex = [(P, valuation(I, P)) for P in support(I)]
    out, k = [], 0
    while any(e > k for _, e in ex):
        pr = 1
        for P, e in ex:
            if e > k:
                pr *= P.norm
        out.append(pr)
        k += 1
    return out, ex


FROZEN = {
    "(2)": [16], "(4)": [16, 16], "lambda": [5], "(5)": [5, 5, 5, 5],
    "lambda(2)": [80], "(10)": [80, 5, 5, 5], "(20)": [80, 80, 5, 5],
    "lambda^2(2)": [80, 5], "(3)": [81], "(6)": [1296], "(11)": [14641],
}
_lw = _ln = True
_seen = {}
for lab, _ in FAMILY:
    I = DATA[lab][0]
    a = loewy_lattice(I)
    b, ex = loewy_formula(I)
    _seen[lab] = a
    if a != b or a != FROZEN[lab]:
        _lw = False
    if len(a) != max(e for _, e in ex):
        _ln = False
gate("L1  lattice-index route == prime-norm route == frozen hand table", _lw,
     "; ".join("%s:%s" % (l, _seen[l]) for l in ("(5)", "(10)", "(20)")))
gate("L2  L(R/I) = min{L : n^L = 0} = max_P e_P", _ln,
     "chain length from HNF determinants, max exponent from valuations")
gate("L3  |n^k/n^(k+1)| = product of N(P) over {P : e_P > k}",
     all(_seen[l] == loewy_formula(DATA[l][0])[0] for l, _ in FAMILY),
     "ORDERS only; no module decomposition is claimed")
gate("L4  the n^1 start CONTRADICTS the product formula, which never sees "
     "the chain",
     all(_seen[l][1:] != loewy_formula(DATA[l][0])[0]
         for l in ("(10)", "(20)", "(5)"))
     and _seen["(10)"][1:] == [5, 5, 5] and _seen["(10)"] == [80, 5, 5, 5],
     "(10): wrong %s vs correct %s" % (_seen["(10)"][1:], _seen["(10)"]))
def _prod(xs):
    r = 1
    for x in xs:
        r *= x
    return r


# route A: the first layer index from the lattice chain.  route B: the product
# of the residue-field sizes over the support, which never forms the radical
# ideal at all.  The two must not share radical(), or a broken radical would
# move both sides together.  The result-exposed incubation audit caught that
# shared-route defect before these accepted bytes were prepared.
gate("L5  the first layer is the product of N(P) over the support",
     all(_seen[l][0] == _prod(P.norm for P in support(DATA[l][0]))
         for l, _ in FAMILY),
     "chain index vs residue-field sizes, no shared radical computation")

print("")
print("-- Part 5: R4/R5  R-algebra maps classified by ideal inclusion")

HOM = [l for l, _ in FAMILY if inorm(DATA[l][0]) <= 2000]
hom_all, hom_un = {}, {}
for l1 in HOM:
    for l2 in HOM:
        I1, I2 = DATA[l1][0], DATA[l2][0]
        cand = []
        for t in cells(I2):
            # f(r + I1) = r t is R-linear; well defined iff I1 t = 0 in R/I2
            if any(ired(rmul(g, t), I2) != ZERO for g in I1):
                continue
            # multiplicative iff t^2 = t.  UNITALITY IS NOT IMPOSED HERE.
            if ired(rmul(t, t), I2) == t:
                cand.append(t)
        hom_all[(l1, l2)] = cand
        hom_un[(l1, l2)] = [t for t in cand if t == ired(ONE, I2)]

gate("H1  a unital map R/I1 -> R/I2 exists iff I1 is contained in I2",
     all((len(hom_un[(a, b)]) > 0) == isub(DATA[a][0], DATA[b][0])
         for a in HOM for b in HOM),
     "%d ordered pairs; existence from well-definedness vs lattice "
     "containment" % (len(HOM) ** 2))
_ma, _mu = (max(len(v) for v in hom_all.values()),
            max(len(v) for v in hom_un.values()))
gate("H2  THIN: many multiplicative maps exist; unitality leaves at most one",
     _mu == 1 and _ma == 4,
     "max multiplicative %d, max unital %d -- unitality applied AFTER the "
     "enumeration, not inside it" % (_ma, _mu))
_h3 = True
for a in HOM:
    for b in HOM:
        if not isub(DATA[a][0], DATA[b][0]):
            continue
        maps = hom_un[(a, b)]
        if len(maps) != 1:
            _h3 = False
            continue
        if not all(ired(rmul(maps[0], v), DATA[b][0])
                   == ired(v, DATA[b][0]) for v in BASIS):
            _h3 = False
gate("H3  the unique unital map is reduction on every basis vector", _h3,
     "requires exactly one map before checking f(z^j) = z^j for j = 0..3")
_strict = [(a, b) for a in HOM for b in HOM
           if isub(DATA[a][0], DATA[b][0]) and DATA[a][0] != DATA[b][0]]
gate("H5  R5: a strict quotient has NO unital section back",
     len(_strict) > 0
     and all(len(hom_un[(b, a)]) == 0 for a, b in _strict),
     "all %d strict quotients enumerated, none skipped" % len(_strict))
def hom_count_formula(I1, I2):
    """CRT route: a target component is selectable iff v_P(I1) >= v_P(I2)."""
    selectable = sum(valuation(I1, P) >= valuation(I2, P)
                     for P in support(I2))
    return 2 ** selectable


gate("H6  map enumeration agrees with the independent CRT valuation count",
     all(len(hom_all[(a, b)])
         == hom_count_formula(DATA[a][0], DATA[b][0])
         for a in HOM for b in HOM),
     "idempotent-image enumeration vs selectable local components")

print("")
print("-- Part 6: R6  fixed support admits arbitrary Loewy length (no-go)")

NG = {}
for L in range(1, 6):
    I = imul(ipow(ideal([LAM]), L), P2[0].ideal)
    NG[L] = (I, support(I), radical(I), idempotents(I), loewy_lattice(I))
gate("N1  all five tested I_L have the same support and radical",
     len(set(tuple(sorted(repr(P) for P in NG[L][1]))
             for L in range(1, 6))) == 1
     and len(set(NG[L][2] for L in range(1, 6))) == 1
     and inorm(NG[1][2]) == 80,
     "support and radical recomputed per L; N(rad) = 80")
gate("N2  all five tested I_L have the same Boolean algebra, |Idem| = 4",
     all(len(NG[L][3]) == 4 for L in range(1, 6))
     and [inorm(NG[L][0]) for L in range(1, 6)] == [80, 400, 2000, 10000,
                                                    50000],
     "enumerated separately in each R/I_L, up to 50000 cells")
_lens = [len(NG[L][4]) for L in range(1, 6)]
gate("N3  finite audit: L(R/I_L) = L for L = 1..5",
     _lens == [1, 2, 3, 4, 5],
     "lengths %s from the lattice route" % (_lens,))
gate("N4  finite witness: fixed Boolean data, five distinct depths",
     len(set(NG[L][2] for L in range(1, 6))) == 1
     and len(set(len(NG[L][3]) for L in range(1, 6))) == 1
     and len(set(_lens)) == 5,
     "the universal no-go is proved in PREREG.md; this gate is its finite witness")

print("")
_bad = [g for g, ok in GATES if not ok]
if _bad:
    print("DECISION RECORD-QUOTIENT-CALCULUS-FIRED")
    print("FIRED count=%d" % len(_bad))
    for g in _bad:
        print("FIRED gate=%s" % g)
else:
    print("DECISION RECORD-QUOTIENT-CALCULUS-CONFIRMED")
    print("BOOLEAN Idem(R/I)=P(Supp(I)); radical reduction preserves idempotents")
    print("THICKNESS layer_order=product_NP_for_eP_gt_k Loewy=max_eP")
    print("REDUCTIONS Hom_R_alg=canonical_projection_iff_I_subset_J; strict=no_section")
    print("NO_GO fixed_support_and_reduced_record_do_not_determine_Loewy_depth")
print("SCOPE L1 only; no selector, apparatus, event, atom choice, decoder, measure, "
      "coarse-graining, RG, continuum, or L2-L6 lift")
print("SAMPLING NOT PROVIDED")
print("RESULT %d/%d PASS" % (len(GATES) - len(_bad), len(GATES)))
raise SystemExit(1 if _bad else 0)
