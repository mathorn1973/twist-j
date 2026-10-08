#!/usr/bin/env python3
"""Independent integer breaker for the frozen static-transposition completion.

NON-CANONICAL, candidate-C finite audit, L1, one execution architecture.
Written from PREREG.md without reading verify.py or any uploaded program.
The analytical conjecture was previously known to this implementation author.
This source has not been imported, compiled, or executed before its first pin.

G uses raw electric/magnetic integer numerators and residue tests. H(x) is
evaluated by the raw field form on P*x, not by the supplied Bf polynomial.
All loops, mechanically selected boundary stocks, and extra finite support
enumerations are fixed here before either implementation's first evaluation.
No random sampling, floating point, external data, or output-file mutation.
"""

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json
import sys


PREREG_SHA256 = "58b8e76488c0eda439407b8e52ee667dfb33ba7ffab6c88dada2a7f30c6470d1"
ADDENDUM_SHA256 = "d9ada337b321f16659ead0ee0dcc76ae25efdc229f18ad4d24ef23e4cdc23320"
Z = (0, 0, 0, 0)
V = (1, 0, 0, 0)
NEUTRAL = (1, -1, 0, 0)
ZM = (Z, Z, Z)
R = ((1, -2, 1, 0), Z, Z)
AM = (V, (0, -1, 0, 0), (0, -1, 1, 0))
R_CHARGED = ((2, -2, 1, 0), Z, Z)
MATTER_FIXTURES = (R, AM, ZM, R_CHARGED)
CHARGE_FIXTURES = (
    (0, 0, 0), (5, -5, 0), (5, 0, -5), (0, 5, -5),
    (1, 0, -1), (2, -1, -1), (10, -5, -5), (-5, 5, 0),
)
C = ((1, -1), (-1, 0), (0, 1), (0, 1))
D = ((1, 1, 1, 0), (-1, -1, 0, -1), (0, 0, -1, 1))
K = ((6, 2, -1, 2), (2, 6, 2, -1), (-1, 2, 6, 2), (2, -1, 2, 6))
L = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
VINV = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
AF = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
BF = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
PAIRS = ("01", "02", "12")
KV = {"01": (-2, -2, -1, -1), "02": (1, 1, 3, -2), "12": (-1, -1, 2, -3)}
KNORM = {"01": 10, "02": 15, "12": 15}
INDICES = {"01": (0, 1), "02": (0, 2), "12": (1, 2)}
PRIMARY_SIGMAS = ((-1, 0), (0, 0), (1, 0), (2, 1), (1, 3))
BASE_STOCKS = (0, 1, 2, 5, 6, 7, 20)

CHECKS = Counter()
DOMAINS = Counter()
REACTION_BRANCHES = Counter()
CONTACT_BRANCHES = {pair: Counter() for pair in PAIRS}
STATE_FEATURES = Counter()
MAXIMALITY = Counter()
TRACE = sha256()


class AuditFailure(Exception):
    def __init__(self, label, context):
        self.label = label
        self.context = context
        super().__init__(label)


def require(label, condition, context=None):
    CHECKS[label] += 1
    if not condition:
        raise AuditFailure(label, context)


def mv(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def mm(left, right):
    columns = tuple(zip(*right))
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in columns)
                 for row in left)


def transpose(matrix):
    return tuple(zip(*matrix))


def determinant(matrix):
    total = 0
    for perm in permutations(range(len(matrix))):
        inversions = sum(perm[i] > perm[j] for i in range(len(perm))
                         for j in range(i + 1, len(perm)))
        term = -1 if inversions % 2 else 1
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def pfield(y):
    a, b, c, d = y
    return (a - b, -a, b, b), (c, d)


def assemble(y, sigma):
    active_e, magnetic = pfield(y)
    u, w = sigma
    static_e = (u, u, w, u - w)
    return tuple(active_e[i] + static_e[i] for i in range(4)), magnetic


def charges(electric):
    a, b, c, d = electric
    return (a + b + c, -a - b - d, -c + d)


def spectators(q, decorated=False):
    values = [(value, 0, 0, 0) for value in q]
    if decorated:
        values[0] = tuple(values[0][i] + NEUTRAL[i] for i in range(4))
    return tuple(values)


@lru_cache(maxsize=4096)
def qform(vector):
    a, b, c, d = vector
    return (6 * (a*a + b*b + c*c + d*d)
            + 4 * (a*b + b*c + c*d + a*d) - 2 * (a*c + b*d))


@lru_cache(maxsize=32768)
def hraw(electric, magnetic):
    a, b, c, d = electric
    u, w = magnetic
    return a*a + b*b + c*c + d*d + u*u + w*w + (a-b)*u + (-a+c+d)*w


def hactive(y):
    electric, magnetic = pfield(y)
    return hraw(electric, magnetic)


@lru_cache(maxsize=32768)
def energy(state):
    m, b, electric, magnetic, stock = state
    return sum(qform(v) for v in m) + sum(qform(v) for v in b) + hraw(electric, magnetic) + stock


def defect(state):
    m, b, electric, _magnetic, _stock = state
    rho = (sum(b[0]) + sum(sum(v) for v in m), sum(b[1]), sum(b[2]))
    return tuple(q-r for q, r in zip(charges(electric), rho))


def active_numerators(state):
    a, b, c, d = state[2]
    u, w = state[3]
    return (2*a - 3*b + c + d, -a - b + 2*c + 2*d, 5*u, 5*w)


def static_numerators(state):
    a, b, c, d = state[2]
    return (2*a + 2*b + c + d, a + b + 3*c - 2*d)


def ffield(electric, magnetic):
    a, b, c, d = electric
    u, w = magnetic
    ep = (a + u - w, b - u, c + w, d + w)
    ap, bp, cp, dp = ep
    return ep, (u - ap + bp, w + ap - cp - dp)


def fstep(state):
    m, b, electric, magnetic, stock = state
    ep, mp = ffield(electric, magnetic)
    return (m, b, ep, mp, stock)


def finverse(state):
    m, b, electric, magnetic, stock = state
    a, bb, c, d = electric
    u = magnetic[0] + a - bb
    w = magnetic[1] - a + c + d
    return (m, b, (a-u+w, bb+u, c-w, d-w), (u, w), stock)


@lru_cache(maxsize=32768)
def ginfo(state):
    """Complete G, implemented directly from raw integer field residues.

    The R inverse coordinate x has denominator 5 and numerator rows
      (0,-1,1,1, 1, 2), (1,-1,0,0, 2,-1),
      (1, 1,-2,-2,1,-3), (-3,2,1,1,-3,4)
    acting on (E0,E1,E2,E3,M0,M1).
    No rational split or matrix inverse is evaluated by this implementation.
    """
    m, b, electric, magnetic, stock = state
    if m != R and m != AM:
        return state, "other_matter"
    e0, e1, e2, e3 = electric
    m0, m1 = magnetic
    split_num = 2*e0 - 3*e1 + e2 + e3
    if split_num % 5:
        return state, "nonintegral_split"
    if m == R:
        if (-e1 + e2 + e3) % 5 or (m0 + 2*m1) % 5:
            return state, "R_image_rejection"
        nums = (-e1 + e2 + e3 + m0 + 2*m1,
                e0 - e1 + 2*m0 - m1,
                e0 + e1 - 2*e2 - 2*e3 + m0 - 3*m1,
                -3*e0 + 2*e1 + e2 + e3 - 3*m0 + 4*m1)
        if any(value % 5 for value in nums):
            raise AuditFailure("BASE_raw_R_residue_equivalence", state)
        a, bb, c, d = (value // 5 for value in nums)
        new_stock = stock + 4*hactive((a, bb, c, d)) - 2
        if new_stock < 0:
            return state, "R_stock_rejection"
        increment_b = 3*a - 3*bb + 2*c - d
        ep = (e0 - 3*a + 6*bb - c + 3*d,
              e1 - 3*bb - c - 2*d,
              e2 + increment_b, e3 + increment_b)
        return (AM, b, ep, (c, d), new_stock), "R_accepted"
    bnum = -e0 - e1 + 2*e2 + 2*e3
    if bnum % 5:
        raise AuditFailure("BASE_raw_AM_residue_equivalence", state)
    a, bb, c, d = split_num // 5, bnum // 5, m0, m1
    new_stock = stock + 2 - 4*hactive((a, bb, c, d))
    if new_stock < 0:
        return state, "AM_stock_rejection"
    increment_b = -3*a + 3*bb - 2*c + d
    ep = (e0 + 3*a - 6*bb + c - 3*d,
          e1 + 3*bb + c + 2*d,
          e2 + increment_b, e3 + increment_b)
    mp = (5*bb + c + 2*d, 5*a - 5*bb + 2*c - d)
    return (R, b, ep, mp, new_stock), "AM_accepted"


def accepted(state):
    return ginfo(state)[0][0] != state[0]


def event(state):
    return int(state[0] == R and ginfo(state)[0][0] == AM)


def transfer_t(state, pair):
    q = tuple(sum(v) for v in state[1])
    if pair == "01":
        return q[0] - q[1]
    i, j = INDICES[pair]
    return q[j] - q[i]


def proposal(state, pair):
    """Return (possibly negative-stock proposed cell, price, t), or None."""
    m, b, electric, magnetic, stock = state
    t = transfer_t(state, pair)
    if t % 5:
        return None
    n = t // 5
    k = KV[pair]
    price = n*n*KNORM[pair] + 2*n*sum(e*k0 for e, k0 in zip(electric, k))
    ep = tuple(e + n*k0 for e, k0 in zip(electric, k))
    bp = list(b)
    i, j = INDICES[pair]
    bp[i], bp[j] = bp[j], bp[i]
    return (m, tuple(bp), ep, magnetic, stock-price), price, t


def naive(state, pair):
    candidate = proposal(state, pair)
    return candidate[0] if candidate is not None and candidate[0][4] >= 0 else state


@lru_cache(maxsize=32768)
def contact(state, pair):
    candidate = proposal(state, pair)
    if candidate is None:
        return state, "integrality_rejection"
    output, _price, _t = candidate
    if output[4] < 0:
        return state, "stock_rejection"
    a0, a1 = accepted(state), accepted(output)
    if a0 != a1:
        return state, "admission_mismatch"
    return output, "committed_accepted" if a0 else "committed_rejected"


def matrix_audit():
    identity = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
    five_identity = tuple(tuple(5*v for v in row) for row in identity)
    require("BASE_L_inverse_left", mm(L, VINV) == five_identity)
    require("BASE_L_inverse_right", mm(VINV, L) == five_identity)
    require("BASE_Af_L", mm(AF, L) == mm(L, AF))
    apower = identity
    for _ in range(5):
        apower = mm(AF, apower)
    require("BASE_Af_order5", apower == identity)
    require("BASE_L_energy", mm(mm(transpose(L), BF), L)
            == tuple(tuple(5*v for v in row) for row in BF))
    for y in product((-1, 0, 1), repeat=4):
        require("BASE_Hactive_Bf", 2*hactive(y) == sum(a*b for a, b in zip(y, mv(BF, y))), y)
        require("BASE_Hactive_L", hactive(mv(L, y)) == 5*hactive(y), y)
        require("BASE_F_P", ffield(*pfield(y)) == pfield(mv(AF, y)), y)
        require("BASE_Q_literal_matrix", qform(y) == sum(a*b for a, b in zip(y, mv(K, y))), y)
    for sigma in product((-2, -1, 0, 1, 2), repeat=2):
        fields = assemble(Z, sigma)
        require("BASE_F_static", ffield(*fields) == fields, sigma)
    selector = transpose(C) + D[:2]
    require("T1_unique_rational_static_shift", determinant(selector) == 5)
    expected_divergences = {"01": (-5, 5, 0), "02": (5, 0, -5), "12": (0, 5, -5)}
    for pair in PAIRS:
        k = KV[pair]
        require("T1_static_vector", mv(transpose(C), k) == (0, 0), pair)
        require("T1_divergence_vector", charges(k) == expected_divergences[pair], pair)
        require("T1_primitive_vector", any(abs(v) == 1 for v in k), pair)
        require("T1_squared_norm", sum(v*v for v in k) == KNORM[pair], pair)


def check_inherited(state):
    gs, reaction_branch = ginfo(state)
    fs = fstep(state)
    hs = energy(state)
    ds = defect(state)
    REACTION_BRANCHES[reaction_branch] += 1
    require("BASE_nonnegative_input_stock", state[4] >= 0, state)
    require("BASE_G_involution", ginfo(gs)[0] == state, state)
    require("BASE_G_energy", energy(gs) == hs, state)
    require("BASE_G_defect", defect(gs) == ds, state)
    require("BASE_G_static", static_numerators(gs) == static_numerators(state), state)
    require("BASE_F_energy", energy(fs) == hs, state)
    require("BASE_F_defect", defect(fs) == ds, state)
    require("BASE_F_inverse", finverse(fs) == state, state)
    require("BASE_G_F", ginfo(fs)[0] == fstep(gs), state)
    yn = active_numerators(state)
    u, w = static_numerators(state)
    scaled_active_energy = hactive(yn)
    static_numerator = 3*u*u - 2*u*w + 2*w*w
    q0, q1, q2 = charges(state[2])
    coulomb_numerator = q0*q0 + q1*q1 + 2*q2*q2
    require("BASE_raw_split_energy", 25*hraw(state[2], state[3])
            == scaled_active_energy + static_numerator, state)
    require("BASE_raw_Coulomb_energy", static_numerator == 5*coulomb_numerator, state)
    return gs, fs, hs, ds


def audit_state(state, domain):
    DOMAINS[domain] += 1
    STATE_FEATURES["visits"] += 1
    STATE_FEATURES["non_Gauss"] += int(defect(state) != (0, 0, 0))
    STATE_FEATURES["charged_reacting_matter"] += int(sum(sum(v) for v in state[0]) != 0)
    STATE_FEATURES["nonintegral_split"] += int(active_numerators(state)[0] % 5 != 0)
    gs, fs, hs, ds = check_inherited(state)
    was_accepted = gs[0] != state[0]
    before_event = event(state)
    outputs = []
    for pair in PAIRS:
        output, branch = contact(state, pair)
        counts = CONTACT_BRANCHES[pair]
        counts[branch] += 1
        counts["actual_nonidentity"] += int(output != state)
        counts["actual_charge_change"] += int(output != state and transfer_t(state, pair) != 0)
        counts["committed_fixed"] += int(branch.startswith("committed") and output == state)
        outputs.append(output)
        require("T2_involution", contact(output, pair)[0] == state, (pair, state))
        require("T2_energy", energy(output) == hs, (pair, state))
        require("T2_Gauss_defect", defect(output) == ds, (pair, state))
        require("T2_matter_fixed", output[0] == state[0], (pair, state))
        require("T2_magnetic_fixed", output[3] == state[3], (pair, state))
        require("T2_active_fixed", active_numerators(output) == active_numerators(state), (pair, state))
        gout = ginfo(output)[0]
        sgs = contact(gs, pair)[0]
        require("T2_G_commutation", gout == sgs, (pair, state))
        require("T2_F_commutation", fstep(output) == contact(fs, pair)[0], (pair, state))
        require("T2_event_preservation", event(output) == before_event, (pair, state))
        require("T3_acceptance_preservation", accepted(output) == was_accepted, (pair, state))
        for pointer in range(5):
            left = (gout, (pointer + event(output)) % 5)
            right = (sgs, (pointer + before_event) % 5)
            require("T2_Ghat_full_pointer", left == right, (pair, state, pointer))
        candidate = proposal(state, pair)
        if candidate is not None:
            proposed, price, t = candidate
            counts["integral_raw_proposals"] += 1
            require("T1_raw_price", price == hraw(proposed[2], proposed[3])
                    - hraw(state[2], state[3]), (pair, state))
            q = charges(state[2])
            qp = charges(proposed[2])
            ec5 = lambda z: z[0]*z[0] + z[1]*z[1] + 2*z[2]*z[2]
            require("T1_Coulomb_price", 5*price == ec5(qp)-ec5(q), (pair, state))
            require("T1_proposed_active", active_numerators(proposed) == active_numerators(state),
                    (pair, state))
            require("T1_proposed_defect", defect(proposed) == ds, (pair, state))
            expected_parity = 0 if pair == "01" else (t//5) % 2
            require("T5_raw_price_parity", price % 2 == expected_parity, (pair, state))
            if proposed[4] >= 0:
                counts["funded_raw_proposals"] += 1
                back = proposal(proposed, pair)
                require("T2_raw_proposal_reverse", back is not None and back[0] == state
                        and back[1] == -price and back[2] == -t, (pair, state))
                require("T3_symmetric_admission_filter",
                        contact(proposed, pair)[1] == branch, (pair, state))
                if branch == "admission_mismatch":
                    direction = "mismatch_accepted_to_rejected" if was_accepted else "mismatch_rejected_to_accepted"
                    counts[direction] += 1
            if was_accepted:
                predicted = price <= min(state[4], gs[4])
                require("T3_full_reaction_pair_guard",
                        branch.startswith("committed") == predicted, (pair, state))
        elif was_accepted:
            require("T3_nonintegral_guard", not branch.startswith("committed"), (pair, state))
        if pair == "01":
            require("T5_S01_all_profile_coefficient", output[4] % 2 == state[4] % 2, state)
        if branch.startswith("committed"):
            counts["committed_odd_stock_change"] += int((output[4]-state[4]) % 2 != 0)
    TRACE.update(repr((domain, state, tuple(outputs))).encode("ascii"))


def boundary_stocks(state, delta):
    """Frozen additions: neighboring integers around every funding boundary.

    Start with 0,1,2,5,6,7,20. Add h-1,h,h+1 where h=max(0,-delta).
    For each integral contact add z-1,z,z+1 for z=kappa and z=kappa-delta.
    Keep only nonnegative integers. These formulas do not inspect test results.
    """
    values = set(BASE_STOCKS)
    h = max(0, -delta)
    boundaries = {h}
    for pair in PAIRS:
        raw = proposal(state, pair)
        if raw is not None:
            boundaries.add(raw[1])
            boundaries.add(raw[1] - delta)
    for boundary in boundaries:
        values.update(v for v in (boundary-1, boundary, boundary+1) if v >= 0)
    return values


def raw_domains():
    electric_values = tuple(product((-1, 0, 1), repeat=4))
    magnetic_values = tuple(product((-1, 0, 1), repeat=2))
    for ei, electric in enumerate(electric_values):
        for mi, magnetic in enumerate(magnetic_values):
            index = 9*ei + mi
            m = MATTER_FIXTURES[index % len(MATTER_FIXTURES)]
            q = CHARGE_FIXTURES[(index//4) % len(CHARGE_FIXTURES)]
            stock = (0, 2, 7)[(index//32) % 3]
            yield (m, spectators(q, bool(ei % 2)), electric, magnetic, stock), "breaker_raw_rotation"
    index = 0
    for ei, electric in enumerate(electric_values):
        for magnetic in ((0, 0), (1, 0), (0, 1)):
            for m in MATTER_FIXTURES:
                for stock in (0, 2, 7):
                    q = CHARGE_FIXTURES[index % len(CHARGE_FIXTURES)]
                    yield (m, spectators(q, bool(ei % 2)), electric, magnetic, stock), "primary_raw_crosscheck"
                    index += 1


def integral_domains():
    sigmas = tuple(product((-2, -1, 0, 1, 2), repeat=2)) + ((1, 3),)
    for xi, x in enumerate(product((-1, 0, 1), repeat=4)):
        hx = hactive(x)
        for sigma in sigmas:
            for m in (R, AM):
                y = mv(L, x) if m == R else x
                electric, magnetic = assemble(y, sigma)
                b = spectators(charges(electric), bool(xi % 2))
                base = (m, b, electric, magnetic, 0)
                delta = 4*hx-2 if m == R else 2-4*hx
                stocks = boundary_stocks(base, delta)
                if sigma in PRIMARY_SIGMAS:
                    h = max(0, -delta)
                    stocks.update(range(13))
                    stocks.update((0, 1, h, h+1, h+5, h+7))
                for stock in sorted(stocks):
                    yield base[:4] + (stock,), "integral_branches_with_funding_boundaries"
            # Two explicitly different nonimage residue cosets: a+2b and c+2d.
            ly = mv(L, x)
            for coordinate in (0, 2):
                y = tuple(value + int(i == coordinate) for i, value in enumerate(ly))
                electric, magnetic = assemble(y, sigma)
                b = spectators(charges(electric), bool(xi % 2))
                base = (R, b, electric, magnetic, 0)
                for stock in sorted(boundary_stocks(base, 0)):
                    yield base[:4] + (stock,), "R_image_cosets_with_funding_boundaries"


def maximality_audit(start, pair):
    """Exhaust every proposal-or-identity map on a finite closed G/P orbit.

    No involution or bijectivity is imposed on the competing maps, in accord
    with T4's class of complete maps. The closure is generated by complete G
    and the naive funded proposal. At most four cells are expected here;
    the guard at sixteen is an explicit audit failure, not a silent cutoff.
    """
    orbit = {start}
    pending = [start]
    while pending:
        state = pending.pop()
        for nxt in (ginfo(state)[0], naive(state, pair)):
            if nxt not in orbit:
                orbit.add(nxt)
                pending.append(nxt)
                require("T4_finite_orbit_bound", len(orbit) <= 16, (pair, start, len(orbit)))
    ordered = tuple(sorted(orbit))
    require("T4_expected_Klein_orbit_bound", len(ordered) <= 4, (pair, start, ordered))
    movable = tuple(s for s in ordered if naive(s, pair) != s)
    largest_support = {s for s in ordered if contact(s, pair)[0] != s}
    require("T4_completed_orbit_closed", all(contact(s, pair)[0] in orbit for s in ordered),
            (pair, start))
    valid = 0
    reaches_largest = 0
    for choices in product((False, True), repeat=len(movable)):
        mapping = {s: s for s in ordered}
        for s, use_proposal in zip(movable, choices):
            if use_proposal:
                mapping[s] = naive(s, pair)
        MAXIMALITY["competing_maps"] += 1
        if not all(ginfo(mapping[s])[0] == mapping[ginfo(s)[0]] for s in ordered):
            continue
        valid += 1
        support = {s for s in ordered if mapping[s] != s}
        require("T4_support_domination", support <= largest_support, (pair, start, mapping))
        if support == largest_support:
            reaches_largest += 1
            require("T4_unique_greatest_map",
                    all(mapping[s] == contact(s, pair)[0] for s in ordered), (pair, start, mapping))
    require("T4_largest_map_present", reaches_largest == 1, (pair, start, valid, reaches_largest))
    MAXIMALITY["orbit_cases"] += 1
    MAXIMALITY["orbit_cell_visits"] += len(ordered)
    MAXIMALITY["G_commuting_maps"] += valid


def witness_audit():
    b = spectators((5, -5, 0))
    base = (R, b, (2, 2, 1, 1), (0, 0), 7)
    expected_fields = {"02": (1, 1, -2, 3), "12": (1, 1, 3, -2)}
    expected_b = {"02": spectators((0, -5, 5)), "12": spectators((5, 0, -5))}
    records = []
    require("W_positive_energy", energy(base) == 335, base)
    for pair in ("02", "12"):
        output, branch = contact(base, pair)
        expected = (R, expected_b[pair], expected_fields[pair], (0, 0), 2)
        require("W_positive_complete_output", output == expected and branch == "committed_accepted", pair)
        require("W_positive_price", proposal(base, pair)[1] == 5, pair)
        require("W_positive_square_stocks", ginfo(base)[0][4] == 5 and ginfo(output)[0][4] == 0, pair)
        require("W_positive_square_energy", all(energy(s) == 335 for s in
                (base, output, ginfo(base)[0], ginfo(output)[0])), pair)
        require("W_positive_profile_coefficients", energy(output)-energy(base) == 0
                and output[4] % 2 - base[4] % 2 == -1, pair)
        records.append({"witness": "positive_static_price", "pair": pair,
                        "input_stock": 7, "price": 5, "output_stock": output[4],
                        "output_E": output[2], "H1": energy(output), "deltaPi": -1})
        for stock in (5, 6):
            state = base[:4] + (stock,)
            raw = proposal(state, pair)[0]
            gs = ginfo(state)[0]
            require("W_naive_funded", raw[4] == stock-5 and accepted(state) and not accepted(raw),
                    (pair, stock))
            require("W_naive_G_noncommutation",
                    ginfo(naive(state, pair))[0] != naive(gs, pair), (pair, stock))
            require("W_repair_identity", contact(state, pair)[0] == state
                    and contact(gs, pair)[0] == gs, (pair, stock))
            require("W_reverse_mismatch", contact(raw, pair)[0] == raw
                    and contact(raw, pair)[1] == "admission_mismatch"
                    and naive(raw, pair) == state, (pair, stock))
            for value in (state, raw, gs):
                audit_state(value, "frozen_mismatch_witnesses")
                maximality_audit(value, pair)
            records.append({"witness": "funded_admission_mismatch", "pair": pair,
                            "input_stock": stock, "raw_output_stock": raw[4],
                            "reaction_partner_stock": gs[4], "new_contact": "identity"})
        # B(S(cell),0) versus S(B(cell,0)): the external stock is retained.
        left = (output[:4] + (0,), output[4])
        swapped_first = base[:4] + (0,)
        right = (contact(swapped_first, pair)[0], 7)
        require("W_stock_swap_noncommutation", left != right, pair)
        require("W_stock_swap_expected", left[0][2] == expected_fields[pair] and left[0][4] == 0
                and left[1] == 2 and right[0] == swapped_first and right[1] == 7, pair)
        audit_state(base, "frozen_positive_witness")
        audit_state(output, "frozen_positive_witness")
        maximality_audit(base, pair)
    am_fields = assemble((0, 0, 1, 0), (2, 1))
    am_state = (AM, b, am_fields[0], am_fields[1], 7)
    require("W_AM_nontrivial_F", fstep(am_state) != am_state, am_state)
    for pair in ("02", "12"):
        require("W_AM_positive_contact", proposal(am_state, pair)[1] == 5
                and contact(am_state, pair)[1] == "committed_accepted"
                and contact(am_state, pair)[0][4] == 2, pair)
        maximality_audit(am_state, pair)
    audit_state(am_state, "frozen_AM_nontrivial_F")
    common = (R, spectators((5, 0, -5)), (2, 2, 1, -4), (0, 0), 81)
    require("W_common_prices", tuple(proposal(common, p)[1] for p in PAIRS) == (0, 0, -5), common)
    common_output = contact(common, "12")[0]
    require("W_common_output", common_output ==
            (R, spectators((5, -5, 0)), (3, 3, -1, -1), (0, 0), 86), common_output)
    require("W_common_energy", energy(common) == energy(common_output) == 424, common)
    audit_state(common, "frozen_common_input")
    audit_state(common_output, "frozen_common_input")
    for pair in PAIRS:
        maximality_audit(common, pair)
    records.append({"witness": "old_common_input", "prices": (0, 0, -5),
                    "S12_output_E": common_output[2], "output_stock": 86, "H1": 424})
    # Literal endpoints and occupied zero-charge spectator data must survive.
    permuted = ((Z, R[0], Z), spectators((0, 0, 0), True), (0, 0, 0, 0), (0, 0), 20)
    require("W_literal_matter_endpoint", ginfo(permuted)[1] == "other_matter", permuted)
    audit_state(permuted, "literal_endpoint_and_occupied_neutral_register")
    for record in records:
        print("WITNESS " + json.dumps(record, sort_keys=True, separators=(",", ":")))


def final_coverage_checks():
    for name in ("nonintegral_split", "R_image_rejection", "R_stock_rejection",
                 "AM_stock_rejection", "R_accepted", "AM_accepted", "other_matter"):
        require("COVERAGE_reaction_branch", REACTION_BRANCHES[name] > 0, (name, REACTION_BRANCHES[name]))
    for pair in PAIRS:
        counts = CONTACT_BRANCHES[pair]
        for name in ("integrality_rejection", "committed_accepted", "committed_rejected", "actual_nonidentity"):
            require("COVERAGE_contact_branch", counts[name] > 0, (pair, name, counts[name]))
        if pair in ("02", "12"):
            for name in ("stock_rejection", "admission_mismatch", "mismatch_accepted_to_rejected",
                         "mismatch_rejected_to_accepted", "committed_odd_stock_change"):
                require("COVERAGE_vertex2_branch", counts[name] > 0, (pair, name, counts[name]))
    require("COVERAGE_nonGauss", STATE_FEATURES["non_Gauss"] > 0)
    require("COVERAGE_nonneutral_matter", STATE_FEATURES["charged_reacting_matter"] > 0)
    require("COVERAGE_nonintegral_split", STATE_FEATURES["nonintegral_split"] > 0)


def full_chain_stages(initial, pair):
    """Literal complete Ghat;A;B;F;S chronology, retaining the occupied link."""
    source, receiver, eta, pointer = initial
    source_g = ginfo(source)[0]
    receiver_g = ginfo(receiver)[0]
    pointer_g = (pointer + event(receiver)) % 5
    after_g = (source_g, receiver_g, eta, pointer_g)
    source_a = source_g[:4] + (eta,)
    eta_a = source_g[4]
    after_a = (source_a, receiver_g, eta_a, pointer_g)
    receiver_b = receiver_g[:4] + (eta_a,)
    eta_b = receiver_g[4]
    after_b = (source_a, receiver_b, eta_b, pointer_g)
    after_f = (fstep(source_a), fstep(receiver_b), eta_b, pointer_g)
    after_s = (after_f[0], contact(after_f[1], pair)[0], eta_b, pointer_g)
    return (after_g, after_a, after_b, after_f, after_s)


def full_energy(full_state):
    source, receiver, eta, _pointer = full_state
    return energy(source) + energy(receiver) + eta + 1


def readout_addendum_audit():
    """T7: two explicitly frozen full histories with the same complete old output."""
    zero_cell = (ZM, ZM, (0, 0, 0, 0), (0, 0), 0)
    common_receiver = (R, spectators((5, 0, -5)), (2, 2, 1, -4), (0, 0), 81)
    target = (zero_cell, common_receiver, 0, 0)
    definitions = (
        ("01", 81, (0, 5, -5), (-2, 0, 2, -3), (-5, 0, 5, 0), (0, 0, 0, -5), 343, 0),
        ("12", 86, (5, -5, 0), (1, 3, 1, 1), (-2, 3, 4, 4), (3, 3, -1, -1), 338, 5),
    )
    endpoints = []
    changes = []
    for pair, source_stock, bq, initial_e, after_g_e, after_f_e, receiver_h, price in definitions:
        initial_source = zero_cell[:4] + (source_stock,)
        initial_receiver = (AM, spectators(bq), initial_e, (0, 0), 6)
        initial = (initial_source, initial_receiver, 0, 0)
        require("T7_initial_receiver_energy", energy(initial_receiver) == receiver_h, pair)
        require("T7_initial_active_coordinate", active_numerators(initial_receiver) == (-5, 0, 0, 0), pair)
        require("T7_AM_accepted_zero_guard", ginfo(initial_receiver)[1] == "AM_accepted"
                and ginfo(initial_receiver)[0][4] == 0 and event(initial_receiver) == 0, pair)
        stages = full_chain_stages(initial, pair)
        receiver_g = (R, spectators(bq), after_g_e, (0, -5), 0)
        receiver_b = receiver_g[:4] + (source_stock,)
        receiver_f = (R, spectators(bq), after_f_e, (0, 0), source_stock)
        expected_stages = (
            (initial_source, receiver_g, 0, 0),
            (zero_cell, receiver_g, source_stock, 0),
            (zero_cell, receiver_b, 0, 0),
            (zero_cell, receiver_f, 0, 0),
            target,
        )
        for stage_name, actual, expected in zip(("Ghat", "A", "B", "F", "S"), stages, expected_stages):
            require("T7_full_intermediate_tuple", actual == expected, (pair, stage_name, actual, expected))
            require("T7_full_intermediate_energy", full_energy(actual) == 425, (pair, stage_name, actual))
            require("T7_pointer_unchanged", actual[3] == 0, (pair, stage_name))
        require("T7_initial_full_energy", full_energy(initial) == 425, pair)
        require("T7_precontact_inverse", receiver_f == contact(common_receiver, pair)[0], pair)
        require("T7_forward_contact_price", proposal(receiver_f, pair)[1] == price, pair)
        require("T7_forward_contact_accepted", contact(receiver_f, pair)[1] == "committed_accepted", pair)
        difference = energy(stages[-1][1]) - energy(initial_receiver)
        require("T7_last_receiver_change", difference == source_stock, pair)
        endpoints.append(stages[-1])
        changes.append(difference)
        audit_state(initial_receiver, "T7_frozen_initial_receiver")
        audit_state(receiver_f, "T7_frozen_precontact_receiver")
        print("WITNESS " + json.dumps({
            "witness": "T7_same_complete_old_output", "pair": pair,
            "source_energy_before": source_stock, "receiver_energy_before": receiver_h,
            "receiver_energy_after": 424, "last_receiver_change": difference,
            "last_contact_field_price": price, "pointer": 0,
            "total_energy": 425,
        }, sort_keys=True, separators=(",", ":")))
    require("T7_equal_complete_output", endpoints[0] == endpoints[1] == target, endpoints)
    require("T7_distinct_changes", tuple(changes) == (81, 86), changes)
    # The exact two-point minimax radius is represented by twice its value.
    require("T7_twice_minimax_radius", abs(changes[1]-changes[0]) == 5, changes)
    require("T7_distinct_context_labels", (endpoints[0], "01") != (endpoints[1], "12"))


def main():
    directory = Path(__file__).resolve().parent
    actual_prereg = sha256((directory / "PREREG.md").read_bytes()).hexdigest()
    require("PIN_preregistration", actual_prereg == PREREG_SHA256, actual_prereg)
    actual_addendum = sha256((directory / "ADDENDUM-READOUT.md").read_bytes()).hexdigest()
    require("PIN_preexecution_addendum", actual_addendum == ADDENDUM_SHA256, actual_addendum)
    print("STATUS NON-CANONICAL candidate-C finite exact audit; no all-state promotion")
    print("IMPLEMENTATION independent raw integer G; no verifier or uploaded program imports")
    print("COUNTING state visits; duplicates between explicitly named domains retained")
    print("PREREG_SHA256 " + actual_prereg)
    print("ADDENDUM_SHA256 " + actual_addendum)
    print("SOURCE_SHA256 " + sha256(Path(__file__).read_bytes()).hexdigest())
    matrix_audit()
    witness_audit()
    readout_addendum_audit()
    for state, domain in raw_domains():
        audit_state(state, domain)
    for state, domain in integral_domains():
        audit_state(state, domain)
    final_coverage_checks()
    print("DOMAINS " + json.dumps(dict(DOMAINS), sort_keys=True, separators=(",", ":")))
    print("STATE_FEATURES " + json.dumps(dict(STATE_FEATURES), sort_keys=True, separators=(",", ":")))
    print("REACTION_BRANCHES " + json.dumps(dict(REACTION_BRANCHES), sort_keys=True, separators=(",", ":")))
    branch_keys = (
        "integrality_rejection", "stock_rejection", "admission_mismatch",
        "committed_accepted", "committed_rejected", "actual_nonidentity",
        "actual_charge_change", "committed_fixed", "integral_raw_proposals",
        "funded_raw_proposals", "mismatch_accepted_to_rejected",
        "mismatch_rejected_to_accepted", "committed_odd_stock_change",
    )
    for pair in PAIRS:
        print("CONTACT_BRANCHES_" + pair + " " +
              json.dumps({key: CONTACT_BRANCHES[pair][key] for key in branch_keys},
                         sort_keys=True, separators=(",", ":")))
    print("MAXIMALITY " + json.dumps(dict(MAXIMALITY), sort_keys=True, separators=(",", ":")))
    print("CHECK_COUNTS " + json.dumps(dict(CHECKS), sort_keys=True, separators=(",", ":")))
    print("TRACE_SHA256 " + TRACE.hexdigest())
    print("PASS no exact discrepancy in the declared finite audit domains")


if __name__ == "__main__":
    try:
        main()
    except AuditFailure as failure:
        print("FAIL " + failure.label)
        print("COUNTEREXAMPLE " + repr(failure.context))
        sys.exit(1)
