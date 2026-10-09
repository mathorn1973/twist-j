#!/usr/bin/env python3
"""Exact primary audit for the frozen local static-transposition candidate.

NON-CANONICAL; conditional candidate-T / finite candidate-C; L1.
Implementation: Fraction splitting and general quadratic forms.  This file
does not import project code or the independently written break checker.
Scientific evaluation occurs only from main(), after the joint source pin.
Finite success is not a proof on the infinite carrier or a public gate.
"""

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
import sys


C = ((1, -1), (-1, 0), (0, 1), (0, 1))
D = ((1, 1, 1, 0), (-1, -1, 0, -1), (0, 0, -1, 1))
K = ((6, 2, -1, 2), (2, 6, 2, -1), (-1, 2, 6, 2), (2, -1, 2, 6))
L = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
VINV = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
AF = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
BF = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
P = ((1, -1, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0),
     (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
STATIC = ((1, 0), (1, 0), (0, 1), (1, -1), (0, 0), (0, 0))
ZERO = (0, 0, 0, 0)
R = ((1, -2, 1, 0), ZERO, ZERO)
AM = ((1, 0, 0, 0), (0, -1, 0, 0), (0, -1, 1, 0))
NEUTRAL = (1, -1, 0, 0)
KINDS = ("01", "02", "12")
SHIFTS = {"01": (-2, -2, -1, -1), "02": (1, 1, 3, -2),
          "12": (-1, -1, 2, -3)}
PAIRS = {"01": (0, 1), "02": (0, 2), "12": (1, 2)}
CHARGE_FIXTURES = ((0, 0, 0), (5, -5, 0), (5, 0, -5), (0, 5, -5),
                   (1, 0, -1), (2, -1, -1), (10, -5, -5), (-5, 5, 0))


@dataclass(frozen=True, slots=True)
class Cell:
    m: tuple
    b: tuple
    E: tuple
    M: tuple
    r: int


@dataclass(frozen=True, slots=True)
class Chain:
    source: Cell
    receiver: Cell
    eta: int
    p: int


class AuditFailure(Exception):
    pass


CHECKS = 0
ROWS = Counter()
BRANCHES = Counter()
INPUTS = Counter()
CONTACTS = {kind: Counter() for kind in KINDS}
DIRECTIONS = Counter()
WITNESSES = []


def require(condition, claim, context=None):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AuditFailure(f"{claim}; context={context!r}")


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mv(a, x):
    return tuple(dot(row, x) for row in a)


def transpose(a):
    return tuple(zip(*a))


CT = transpose(C)


def mm(a, b):
    return tuple(tuple(dot(row, col) for col in transpose(b)) for row in a)


def ident(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def scale(a, k):
    return tuple(tuple(k * x for x in row) for row in a)


def quad(a, x):
    return dot(x, mv(a, x))


def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    row = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(row, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = a[row][col]
        a[row] = [x / divisor for x in a[row]]
        for j in range(len(a)):
            if j != row and a[j][col]:
                factor = a[j][col]
                a[j] = [x - factor * y for x, y in zip(a[j], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def integral(xs):
    return all(Fraction(x).denominator == 1 for x in xs)


def ints(xs):
    if not integral(xs):
        raise AuditFailure(f"attempted nonintegral carrier construction: {xs!r}")
    return tuple(int(x) for x in xs)


@lru_cache(maxsize=None)
def split(E, M):
    e0, e1, e2, e3 = E
    y = (Fraction(2 * e0 - 3 * e1 + e2 + e3, 5),
         Fraction(-e0 - e1 + 2 * e2 + 2 * e3, 5),
         Fraction(M[0]), Fraction(M[1]))
    sigma = (Fraction(2 * e0 + 2 * e1 + e2 + e3, 5),
             Fraction(e0 + e1 + 3 * e2 - 2 * e3, 5))
    return y, sigma


def compose(y, sigma):
    z = tuple(a + b for a, b in zip(mv(P, y), mv(STATIC, sigma)))
    return z[:4], z[4:]


@lru_cache(maxsize=None)
def active_energy(y):
    return Fraction(quad(BF, y), 2)


def static_energy(sigma):
    return quad(((3, -1), (-1, 2)), sigma)


def ec(q):
    if sum(q) != 0:
        raise AuditFailure(f"EC called outside sum-zero charges: {q!r}")
    return Fraction(quad(((1, 0, 0), (0, 1, 0), (0, 0, 2)), q), 5)


@lru_cache(maxsize=None)
def raw_energy(E, M):
    return dot(E, E) + dot(M, M) + dot(E, mv(C, M))


@lru_cache(maxsize=None)
def h1(s):
    return sum(quad(K, v) for v in s.m + s.b) + raw_energy(s.E, s.M) + s.r


def rho(s):
    return (sum(s.b[0]) + sum(map(sum, s.m)), sum(s.b[1]), sum(s.b[2]))


@lru_cache(maxsize=None)
def defect(s):
    return tuple(x - y for x, y in zip(mv(D, s.E), rho(s)))


@lru_cache(maxsize=None)
def reaction(s):
    """The complete G, including the unmodified cell on every rejection."""
    if s.m not in (R, AM):
        return s, "nonreactive_m"
    y, sigma = split(s.E, s.M)
    if not integral(y + sigma):
        return s, "nonintegral_split"
    if s.m == R:
        x = tuple(Fraction(v, 5) for v in mv(VINV, y))
        if not integral(x):
            return s, "R_image_rejection"
        delta = 4 * active_energy(x) - 2
        new_m, new_y, branch = AM, x, "R_accepted"
        rejection = "R_stock_rejection"
    else:
        delta = 2 - 4 * active_energy(y)
        new_m, new_y, branch = R, mv(L, y), "AM_accepted"
        rejection = "AM_stock_rejection"
    if s.r + delta < 0:
        return s, rejection
    E, M = compose(new_y, sigma)
    return Cell(new_m, s.b, ints(E), ints(M), ints((s.r + delta,))[0]), branch


def G(s):
    return reaction(s)[0]


def aG(s):
    return int(G(s).m != s.m)


def event(s):
    return int(s.m == R and G(s).m == AM)


def ghat(record):
    s, p = record
    return G(s), (p + event(s)) % 5


def f_fields(E, M):
    new_E = tuple(x + y for x, y in zip(E, mv(C, M)))
    new_M = tuple(x - y for x, y in zip(M, mv(CT, new_E)))
    return new_E, new_M


@lru_cache(maxsize=None)
def F(s):
    E, M = f_fields(s.E, s.M)
    return replace(s, E=E, M=M)


def finv(s):
    M = tuple(x + y for x, y in zip(s.M, mv(CT, s.E)))
    E = tuple(x - y for x, y in zip(s.E, mv(C, M)))
    return replace(s, E=E, M=M)


@lru_cache(maxsize=None)
def raw_geometry(s, kind):
    i, j = PAIRS[kind]
    charges = tuple(map(sum, s.b))
    t = charges[0] - charges[1] if kind == "01" else charges[j] - charges[i]
    if t % 5:
        return t, None, None
    q = t // 5
    E = tuple(x + q * k for x, k in zip(s.E, SHIFTS[kind]))
    b = list(s.b)
    b[i], b[j] = b[j], b[i]
    kappa = raw_energy(E, s.M) - raw_energy(s.E, s.M)
    return t, kappa, replace(s, b=tuple(b), E=E, r=s.r - kappa)


@lru_cache(maxsize=None)
def completed(s, kind):
    _, kappa, proposal = raw_geometry(s, kind)
    if proposal is None:
        return s, "integrality_rejection"
    if proposal.r < 0:
        return s, "stock_rejection"
    if aG(proposal) != aG(s):
        return s, "admission_rejection"
    return proposal, "committed"


def S(s, kind):
    return completed(s, kind)[0]


def srecord(record, kind):
    s, p = record
    return S(s, kind), p


def naive(s, kind):
    _, _, proposal = raw_geometry(s, kind)
    return proposal if proposal is not None and proposal.r >= 0 else s


@lru_cache(maxsize=None)
def check_field(E, M):
    y, sigma = split(E, M)
    require(compose(y, sigma) == (E, M), "rational split reconstruction", (E, M))
    require(raw_energy(E, M) == active_energy(y) + static_energy(sigma),
            "orthogonal energy split", (E, M))
    require(static_energy(sigma) == ec(mv(D, E)), "static EC identity", (E, M))
    require(integral(y + sigma) == ((2 * E[0] - 3 * E[1] + E[2] + E[3]) % 5 == 0),
            "integral-split residue criterion", (E, M))
    if integral(y):
        image = integral(tuple(Fraction(x, 5) for x in mv(VINV, y)))
        residues = (int(y[0] + 2 * y[1]) % 5 == 0 and
                    int(y[2] + 2 * y[3]) % 5 == 0)
        require(image == residues, "L-image residue criterion", y)
    Ef, Mf = f_fields(E, M)
    yf, sf = split(Ef, Mf)
    require(yf == mv(AF, y) and sf == sigma, "F split intertwining", (E, M))
    require(raw_energy(Ef, Mf) == raw_energy(E, M), "F raw energy", (E, M))
    e5, m5 = E, M
    for _ in range(5):
        e5, m5 = f_fields(e5, m5)
    require((e5, m5) == (E, M), "F fifth iterate", (E, M))


def check_state(s, domain):
    ROWS[domain] += 1
    require(s.r >= 0, "input carrier stock", s)
    require(integral(s.E + s.M), "input carrier field", s)
    check_field(s.E, s.M)
    y, sigma = split(s.E, s.M)
    gs, branch = reaction(s)
    BRANCHES[branch] += 1
    INPUTS["nonzero_defect" if any(defect(s)) else "zero_defect"] += 1
    INPUTS["nonneutral_m" if sum(map(sum, s.m)) else "neutral_m"] += 1
    INPUTS["integral_split" if integral(y + sigma) else "nonintegral_split"] += 1
    require(G(gs) == s, "inherited full G involution", s)
    require(h1(gs) == h1(s), "inherited G H1", s)
    require(defect(gs) == defect(s), "inherited G defect", s)
    require(F(gs) == G(F(s)), "inherited full FG=GF", s)
    require(finv(F(s)) == s and F(finv(s)) == s, "inherited full F inverse", s)
    require(h1(F(s)) == h1(s) and defect(F(s)) == defect(s), "inherited F invariants", s)
    if not aG(s):
        require(gs == s, "inherited whole-state G rejection", s)
    else:
        require(gs.b == s.b and split(gs.E, gs.M)[1] == sigma,
                "G static registers", s)
    for kind in KINDS:
        tally = CONTACTS[kind]
        t, kappa, proposal = raw_geometry(s, kind)
        shift = tuple(Fraction(t * k, 5) for k in SHIFTS[kind])
        require(integral(shift) == (t % 5 == 0), "T1 exact integrality", (kind, s))
        require(mv(CT, shift) == (0, 0), "T1 cut shift", (kind, s))
        i, j = PAIRS[kind]
        swapped_b = list(s.b)
        swapped_b[i], swapped_b[j] = swapped_b[j], swapped_b[i]
        target_rho = rho(replace(s, b=tuple(swapped_b)))
        require(mv(D, shift) == tuple(a - b for a, b in zip(target_rho, rho(s))),
                "T1 prescribed defect change", (kind, s))
        out, decision = completed(s, kind)
        tally[decision] += 1
        tally["input_accepted" if aG(s) else "input_rejected"] += 1
        tally["actual_nonidentity" if out != s else "actual_identity"] += 1
        if decision == "committed":
            tally["commit_accepted" if aG(s) else "commit_rejected"] += 1
        else:
            require(out == s, "whole-state contact rejection", (kind, s))
        require(out.r >= 0 and integral(out.E + out.M), "T2 output carrier", (kind, s))
        require(S(out, kind) == s, "T2 full involution", (kind, s))
        require(h1(out) == h1(s), "T2 H1", (kind, s))
        require(defect(out) == defect(s), "T2 full defect", (kind, s))
        require((out.m, out.M, split(out.E, out.M)[0]) == (s.m, s.M, y),
                "T2 m M active-coordinate preservation", (kind, s))
        require(S(gs, kind) == G(out), "T2 full SG=GS", (kind, s))
        require(S(F(s), kind) == F(out), "T2 full SF=FS", (kind, s))
        require(event(out) == event(s), "T2 event preservation", (kind, s))
        require(aG(out) == aG(s), "T3 admission preservation", (kind, s))
        for p in range(5):
            require(ghat(srecord((s, p), kind)) == srecord(ghat((s, p)), kind),
                    "T2 full recorder commutation", (kind, p, s))
            tally["recorder_values_checked"] += 1
        if t % 5 == 0:
            q = t // 5
            expected_price = q * q * dot(SHIFTS[kind], SHIFTS[kind]) + 2 * q * dot(s.E, SHIFTS[kind])
            require(kappa == expected_price, "T1 raw price polynomial", (kind, s))
            require(kappa == ec(mv(D, proposal.E)) - ec(mv(D, s.E)),
                    "T1 static EC price", (kind, s))
            require(kappa % 2 == (0 if kind == "01" else q % 2),
                    "T5 raw parity formula", (kind, s))
            tally["raw_integral"] += 1
            tally["raw_odd_price" if kappa % 2 else "raw_even_price"] += 1
            if aG(s):
                expected = kappa <= min(s.r, gs.r)
                require((decision == "committed") == expected,
                        "T3 accepted min-stock criterion", (kind, s, kappa))
            if proposal.r >= 0:
                tally["raw_funded"] += 1
                tr, kr, reverse = raw_geometry(proposal, kind)
                require((tr, kr, reverse) == (-t, -kappa, s),
                        "T1 raw full reversal", (kind, s))
                require(h1(proposal) == h1(s) and defect(proposal) == defect(s),
                        "raw funded proposal invariants", (kind, s))
                require(split(proposal.E, proposal.M)[0] == y,
                        "raw active preservation", (kind, s))
                if aG(proposal) == aG(s):
                    require(S(proposal, kind) == s, "T3 symmetric acceptance", (kind, s))
                else:
                    direction = f"{aG(s)}_to_{aG(proposal)}"
                    DIRECTIONS[direction] += 1
                    require(S(proposal, kind) == proposal,
                            "T3 symmetric admission rejection", (kind, s))
                    require(G(proposal).m != gs.m,
                            "T4 mismatch obstructs every m-preserving proposal/identity choice", (kind, s))
        else:
            require(proposal is None and decision == "integrality_rejection",
                    "nonintegral proposal rejected", (kind, s))
        if decision == "committed":
            require((out.r - s.r) == -kappa, "funding equality", (kind, s))
            require((out.r % 2 - s.r % 2) % 2 == kappa % 2,
                    "T5 committed stock parity", (kind, s))
        if kind == "01":
            require(out.r % 2 == s.r % 2, "T5 complete S01 preserves every Hc", s)


def check_matrices():
    require(mm(D, C) == ((0, 0),) * 3, "D C zero")
    require(rank(D + CT) == 4, "T1 uniqueness rank four")
    require(mm(VINV, L) == scale(ident(4), 5), "Vinv L = 5 I")
    require(mm(L, VINV) == scale(ident(4), 5), "L Vinv = 5 I")
    require(mm(AF, L) == mm(L, AF), "Af L = L Af")
    require(mm(mm(transpose(L), BF), L) == scale(BF, 5), "L energy scaling")
    require(mm(mm(transpose(AF), BF), AF) == BF, "Af energy invariance")
    a5 = ident(4)
    for _ in range(5):
        a5 = mm(AF, a5)
    require(a5 == ident(4), "Af fifth power")
    columns = []
    for basis in ident(6):
        e, m = f_fields(basis[:4], basis[4:])
        columns.append(e + m)
    tf = transpose(tuple(columns))
    require(mm(tf, P) == mm(P, AF), "F P = P Af")
    require(mm(tf, STATIC) == STATIC, "F S = S")
    br = tuple(tuple(2 * int(i == j) if i < 4 and j < 4 else
                     2 * int(i == j) if i >= 4 and j >= 4 else
                     C[i][j - 4] if i < 4 else C[j][i - 4]
                     for j in range(6)) for i in range(6))
    require(mm(mm(transpose(P), br), P) == BF, "active Gram identity")
    require(mm(mm(transpose(STATIC), br), STATIC) == ((6, -2), (-2, 4)),
            "static Gram identity")
    require(mm(mm(transpose(P), br), STATIC) == ((0, 0),) * 4,
            "active/static orthogonality")
    require(sum(quad(K, v) for v in R) == 18, "R material energy")
    require(sum(quad(K, v) for v in AM) == 20, "AM material energy")
    for kind in KINDS:
        require(mv(CT, SHIFTS[kind]) == (0, 0), "static basis cut vector", kind)
        require(dot(SHIFTS[kind], SHIFTS[kind]) == (10 if kind == "01" else 15),
                "static basis norm", kind)


def charged_b(charges, neutral=False):
    b = [(q, 0, 0, 0) for q in charges]
    if neutral:
        b[0] = tuple(x + y for x, y in zip(b[0], NEUTRAL))
    return tuple(b)


def primary_raw_domain():
    matter = (R, AM, (ZERO, ZERO, ZERO), ((2, -2, 1, 0), ZERO, ZERO))
    index = 0
    for E in product((-1, 0, 1), repeat=4):
        for M in ((0, 0), (1, 0), (0, 1)):
            b = charged_b(CHARGE_FIXTURES[index % 8], neutral=bool(index % 2))
            for m in matter:
                for r in (0, 2, 7):
                    check_state(Cell(m, b, E, M, r), "primary_raw")
            index += 1
    require(ROWS["primary_raw"] == 81 * 3 * 4 * 3, "primary raw row count")


def primary_integral_domain():
    sigmas = ((-1, 0), (0, 0), (1, 0), (2, 1), (1, 3))
    for index, x in enumerate(product((-1, 0, 1), repeat=4)):
        hx = active_energy(x)
        for sigma in sigmas:
            for m, y, delta in ((R, mv(L, x), 4 * hx - 2), (AM, x, 2 - 4 * hx)):
                E, M = compose(y, sigma)
                E, M = ints(E), ints(M)
                h = max(0, -ints((delta,))[0])
                stocks = sorted(set(range(13)) | {0, 1, h, h + 1, h + 5, h + 7})
                b = charged_b(mv(D, E), neutral=bool(index % 2))
                for r in stocks:
                    s = Cell(m, b, E, M, r)
                    require(defect(s) == (0, 0, 0), "integral fixture Gauss constraint", s)
                    check_state(s, "primary_integral")


def fixed_witnesses():
    base = Cell(R, charged_b((5, -5, 0)), (2, 2, 1, 1), (0, 0), 7)
    check_state(base, "fixed_witnesses")
    require(split(base.E, base.M)[0] == (0, 0, 0, 0), "+5 witness active zero")
    expected_E = {"02": (1, 1, -2, 3), "12": (1, 1, 3, -2)}
    expected_b = {"02": charged_b((0, -5, 5)), "12": charged_b((5, 0, -5))}
    for kind in ("02", "12"):
        out = S(base, kind)
        expected = replace(base, E=expected_E[kind], b=expected_b[kind], r=2)
        require(out == expected, "+5 witness full output", kind)
        require(raw_geometry(base, kind)[1] == 5, "+5 witness price", kind)
        require(G(base).r == 5 and G(out).r == 0, "+5 witness G stocks", kind)
        require(all(h1(s) == 335 for s in (base, G(base), out, G(out))),
                "+5 witness complete-square H1", kind)
        require(aG(base) == aG(out) == 1, "+5 witness admissions", kind)
        require(out.r % 2 - base.r % 2 == -1, "+5 witness Hc coefficient", kind)
        WITNESSES.append({"name": "positive_five", "contact": kind,
                          "price": 5, "stock_before": 7, "stock_after": out.r,
                          "G_stock_before": G(base).r, "G_stock_after": G(out).r,
                          "H1": h1(out), "delta_parity": -1, "E_after": out.E})
        check_state(out, "fixed_witnesses")
        check_state(G(base), "fixed_witnesses")
        check_state(G(out), "fixed_witnesses")
        for r in (5, 6):
            s = replace(base, r=r)
            raw = naive(s, kind)
            require(raw.r == r - 5 and raw.E == expected_E[kind], "funded naive output", (kind, r))
            require(aG(s) == 1 and aG(raw) == 0, "forward admission mismatch", (kind, r))
            require(S(s, kind) == s and S(G(s), kind) == G(s),
                    "T6 whole rejection at state and G partner", (kind, r))
            require(S(raw, kind) == raw and naive(raw, kind) == s,
                    "T6 reverse admission mismatch", (kind, r))
            require(G(naive(s, kind)) != naive(G(s), kind),
                    "T6 mandatory naive noncommutation", (kind, r))
            for boundary in (s, G(s), raw):
                check_state(boundary, "fixed_witnesses")
            WITNESSES.append({"name": "admission_mismatch", "contact": kind,
                              "stock": r, "raw_stock": raw.r,
                              "G_partner_stock": G(s).r,
                              "complete_contact_identity": True,
                              "naive_commutator_equal": False})
        nontrivial = replace(base, m=AM, M=(1, 0))
        require(split(nontrivial.E, nontrivial.M) == ((0, 0, 1, 0), (2, 1)),
                "nontrivial F witness split", kind)
        require(F(nontrivial) != nontrivial, "nontrivial F witness", kind)
        require(raw_geometry(nontrivial, kind)[1] == 5 and
                aG(nontrivial) == aG(S(nontrivial, kind)) == 1 and
                S(nontrivial, kind).r == 2, "nontrivial F accepted price", kind)
        check_state(nontrivial, "fixed_witnesses")
        check_state(F(nontrivial), "fixed_witnesses")
        WITNESSES.append({"name": "nontrivial_field_step", "contact": kind,
                          "price": 5, "F_changes_state": True,
                          "SF_equals_FS": S(F(nontrivial), kind) == F(S(nontrivial, kind))})
        # B exchanges the complete nonnegative cell stock and external eta.
        after_s_then_b = (replace(out, r=0), out.r)
        after_b_then_s = (S(replace(base, r=0), kind), base.r)
        require(after_s_then_b == (replace(expected, r=0), 2), "B after S full output", kind)
        require(after_b_then_s == (replace(base, r=0), 7), "S after B full output", kind)
        require(after_s_then_b != after_b_then_s, "T6 mandatory occupied-stock noncommutation", kind)
        WITNESSES.append({"name": "stock_swap_B", "contact": kind,
                          "B_after_S_eta": 2, "S_after_B_eta": 7,
                          "both_cell_stocks": 0, "commutator_equal": False})
    common = Cell(R, charged_b((5, 0, -5)), (2, 2, 1, -4), (0, 0), 81)
    check_state(common, "fixed_witnesses")
    prices = tuple(raw_geometry(common, kind)[1] for kind in KINDS)
    require(prices == (0, 0, -5), "common PR input prices")
    common_out = S(common, "12")
    expected = replace(common, b=charged_b((5, -5, 0)), E=(3, 3, -1, -1), r=86)
    require(common_out == expected, "common PR input full S12 output")
    require(h1(common) == h1(common_out) == 424, "common PR input H1")
    require(aG(common) == aG(common_out) == 1, "common PR input admissions")
    check_state(common_out, "fixed_witnesses")
    WITNESSES.append({"name": "common_PR_input", "prices_01_02_12": prices,
                      "S12_E_after": common_out.E, "S12_stock_after": common_out.r,
                      "H1": h1(common_out), "delta_parity": common_out.r % 2 - common.r % 2})


def chain_energy(s):
    return h1(s.source) + h1(s.receiver) + s.eta


def chain_G(s):
    return Chain(G(s.source), G(s.receiver), s.eta, (s.p + event(s.receiver)) % 5)


def chain_A(s):
    return Chain(replace(s.source, r=s.eta), s.receiver, s.source.r, s.p)


def chain_B(s):
    return Chain(s.source, replace(s.receiver, r=s.eta), s.receiver.r, s.p)


def chain_F(s):
    return Chain(F(s.source), F(s.receiver), s.eta, s.p)


def inverse_history(s, kind):
    s = replace(s, receiver=S(s.receiver, kind))
    s = Chain(finv(s.source), finv(s.receiver), s.eta, s.p)
    s = chain_A(chain_B(s))
    receiver = G(s.receiver)
    return Chain(G(s.source), receiver, s.eta, (s.p - event(receiver)) % 5)


def check_readout_addendum():
    empty = Cell((ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO), ZERO, (0, 0), 0)
    target_receiver = Cell(R, charged_b((5, 0, -5)), (2, 2, 1, -4), (0, 0), 81)
    target = Chain(empty, target_receiver, 0, 0)
    require(h1(target_receiver) == 424, "T7 common receiver energy")
    gains = []
    histories = []
    specifications = (
        ("01", 81, charged_b((0, 5, -5)), (-2, 0, 2, -3), (-1, 2), 343,
         (-5, 0, 5, 0), (0, 0, 0, -5), 0),
        ("12", 86, charged_b((5, -5, 0)), (1, 3, 1, 1), (2, 1), 338,
         (-2, 3, 4, 4), (3, 3, -1, -1), 5),
    )
    for kind, source_stock, b, initial_E, sigma, receiver_energy, after_G_E, after_F_E, price in specifications:
        receiver = Cell(AM, b, initial_E, (0, 0), 6)
        initial = Chain(replace(empty, r=source_stock), receiver, 0, 0)
        require(split(receiver.E, receiver.M) == ((-1, 0, 0, 0), sigma),
                "T7 exact initial active and static coordinates", kind)
        require(active_energy(split(receiver.E, receiver.M)[0]) == 2,
                "T7 active energy", kind)
        require(receiver.r + 2 - 4 * active_energy(split(receiver.E, receiver.M)[0]) == 0,
                "T7 exact AM funding boundary", kind)
        require(reaction(receiver)[1] == "AM_accepted" and event(receiver) == 0,
                "T7 genuinely accepted AM with e zero", kind)
        require(h1(receiver) == receiver_energy and h1(initial.source) == source_stock,
                "T7 initial individual energies", kind)
        states = [("initial", initial)]
        after_g = chain_G(initial)
        expected_g_receiver = Cell(R, b, after_G_E, (0, -5), 0)
        require(after_g == Chain(initial.source, expected_g_receiver, 0, 0),
                "T7 full state after G", kind)
        states.append(("after_G", after_g))
        after_a = chain_A(after_g)
        require(after_a == Chain(empty, expected_g_receiver, source_stock, 0),
                "T7 full state after A", kind)
        states.append(("after_A", after_a))
        after_b = chain_B(after_a)
        require(after_b == Chain(empty, replace(expected_g_receiver, r=source_stock), 0, 0),
                "T7 full state after B", kind)
        states.append(("after_B", after_b))
        after_f = chain_F(after_b)
        expected_pre_contact = Cell(R, b, after_F_E, (0, 0), source_stock)
        require(after_f == Chain(empty, expected_pre_contact, 0, 0),
                "T7 full state after F", kind)
        require(after_f.receiver == S(target_receiver, kind),
                "T7 exact inverse contact predecessor", kind)
        require(aG(after_f.receiver) == aG(target_receiver) == 1,
                "T7 pre-contact and final admissions", kind)
        require(raw_geometry(after_f.receiver, kind)[1] == price and
                completed(after_f.receiver, kind)[1] == "committed",
                "T7 final price and complete guard", kind)
        states.append(("after_F", after_f))
        final = replace(after_f, receiver=S(after_f.receiver, kind))
        require(final == target, "T7 identical complete old-carrier final state Y", kind)
        states.append(("after_contact", final))
        require(inverse_history(target, kind) == initial,
                "T7 exact inverse with retained contact context", kind)
        gain = h1(final.receiver) - h1(initial.receiver)
        require(gain == source_stock, "T7 specified last receiver energy change", kind)
        gains.append(gain)
        stage_records = []
        for stage, state in states:
            require(state.p == 0, "T7 pointer fixed at every stage", (kind, stage))
            require(chain_energy(state) == 424, "T7 cell and link energy at every stage", (kind, stage))
            require(chain_energy(state) + 1 == 425,
                    "T7 common pointer-offset total at every stage", (kind, stage))
            check_state(state.receiver, "readout_addendum")
            stage_records.append({"stage": stage, "source_stock": state.source.r,
                                  "receiver_m": "R" if state.receiver.m == R else "AM",
                                  "receiver_b_charges": tuple(map(sum, state.receiver.b)),
                                  "receiver_E": state.receiver.E, "receiver_M": state.receiver.M,
                                  "receiver_stock": state.receiver.r,
                                  "receiver_H1": h1(state.receiver), "eta": state.eta, "p": state.p,
                                  "cell_link_energy": chain_energy(state), "energy_plus_pointer": 425})
        histories.append({"contact": kind, "last_receiver_gain": gain,
                          "full_final_equals_Y": final == target,
                          "contextual_inverse_equals_initial": inverse_history(target, kind) == initial,
                          "final_contact_price": price, "stages": stage_records})
    require(tuple(gains) == (81, 86), "T7 unequal gains on the identical final argument")
    require(Fraction(abs(gains[0] - gains[1]), 2) == Fraction(5, 2),
            "T7 exact worst-case estimate lower bound")
    WITNESSES.append({"name": "same_final_state_distinct_last_gains", "gains": gains,
                      "worst_case_absolute_error_lower_bound": "5/2",
                      "attaining_midpoint_estimate": "167/2", "histories": histories})


def check_coverage():
    for branch in ("nonreactive_m", "nonintegral_split", "R_image_rejection",
                   "R_stock_rejection", "AM_stock_rejection", "R_accepted", "AM_accepted"):
        require(BRANCHES[branch] > 0, "mandatory reaction branch coverage", branch)
    aggregate = sum(CONTACTS.values(), Counter())
    for category in ("integrality_rejection", "stock_rejection", "admission_rejection",
                     "commit_accepted", "commit_rejected", "actual_nonidentity"):
        require(aggregate[category] > 0, "mandatory contact coverage", category)
    require(DIRECTIONS["0_to_1"] > 0 and DIRECTIONS["1_to_0"] > 0,
            "both admission mismatch directions covered")
    require(INPUTS["nonzero_defect"] > 0 and INPUTS["nonneutral_m"] > 0,
            "unrestricted carrier covered")
    for kind in KINDS:
        require(CONTACTS[kind]["recorder_values_checked"] == 5 * sum(ROWS.values()),
                "all five recorder values for every input and contact", kind)


def main():
    print("C-FIELD-STATIC-TRANSPOSITION-COMPLETION-N primary exact audit", flush=True)
    print("NON-CANONICAL candidate-C finite audit; Fraction implementation; L1", flush=True)
    print("Frozen source; no random sampling; finite success is not an infinite-carrier proof.", flush=True)
    check_matrices()
    primary_raw_domain()
    print("primary_raw_domain: completed", flush=True)
    primary_integral_domain()
    print("primary_integral_domain: completed", flush=True)
    fixed_witnesses()
    check_readout_addendum()
    check_coverage()
    report = {"status": "PASS", "exact_assertions": CHECKS,
              "input_rows": dict(ROWS), "reaction_branches": dict(BRANCHES),
              "input_properties": dict(INPUTS),
              "contacts": {k: dict(v) for k, v in CONTACTS.items()},
              "admission_mismatch_directions": dict(DIRECTIONS),
              "witnesses": WITNESSES}
    print(json.dumps(report, sort_keys=True, indent=2), flush=True)
    print("PASS: all frozen finite comparisons completed; no formal gate or physical derivation.", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        raise
