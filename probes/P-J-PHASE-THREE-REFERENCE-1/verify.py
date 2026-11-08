#!/usr/bin/env python3
"""Five phases, restored shared references, and one existing funded apparatus.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, Apache-2.0.
No scientific execution before the public preregistration/source pin.
The original contact and apparatus are immutable dependencies. A second
sparse wave/tape calculation below uses the primary equations directly.
"""
from collections import Counter
from dataclasses import asdict, dataclass, replace
from fractions import Fraction as Q
import hashlib
import importlib.util
from itertools import permutations, product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CONTACT = "probes/P-CONTACT-RECORD-1/verify.py"
APPARATUS = "probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py"
DOMAIN = "probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/DOMAIN.tsv"
DEPENDENCIES = {
    CONTACT: "99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134",
    APPARATUS: "f0edfd80157c8993322a5338e88120c552908d3830fe5f9ea7536257213c6173",
    DOMAIN: "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0",
}
ROOTS = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0),
         (0, 0, 0, 1), (4, 4, 4, 4))
REFS = ((0, 2, 2, 0), (4, 2, 2, 0), (1, 1, 0, 1))
WEIGHTS = (1, 2, 4)
COLLECTOR = (4, 0, 4, 2, 0, 0)
M_BY_K = (3, 4, 0, 1, 2)
QR_BY_M = ((1, 0), (2, 4), (1, 2), (3, 3), (4, 2))
Z_BY_M = ((Q(1, 2), Q(1, 2), Q(0), Q(0)),
          (Q(1), Q(0), Q(0), Q(0)),
          (Q(1, 2), Q(3, 2), Q(0), Q(0)),
          (Q(-1), Q(-1, 2), Q(0), Q(0)),
          (Q(-1, 2), Q(3, 2), Q(0), Q(0)))
COLD_ENERGIES = (Q(3, 20), Q(2, 5), Q(17, 20), Q(2, 5), Q(23, 20))
BUDGET, ENERGY_BOUND = Q(5), Q(23, 5)
PERM = ((0, 2, 1, 3, 4), (0, 1, 2, 3, 4), (2, 1, 0, 3, 4),
        (1, 0, 2, 3, 4), (1, 0, 2, 3, 4))
WORD = ("Uy", "ey", "dy", "W", "bx", "by", "W",
        "dy", "ey", "W", "by", "bx", "W", "Uy")
F5 = range(5)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def exact(value):
    if isinstance(value, Q):
        return [value.numerator, value.denominator]
    if hasattr(value, "__dataclass_fields__"):
        return exact(asdict(value))
    if isinstance(value, dict):
        return {str(k): exact(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [exact(v) for v in value]
    return value


def digest(value):
    raw = json.dumps(exact(value), sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def emit(label, value):
    print(label + " " + json.dumps(exact(value), sort_keys=True, separators=(",", ":")))


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def custody():
    for path, expected in DEPENDENCIES.items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            raise RuntimeError("frozen dependency changed: " + path)


def add_cell(x, y, scale=1):
    return tuple((a + scale * b) % 5 for a, b in zip(x, y))


def det(p):
    return (p[0] * p[3] - p[1] * p[2]) % 5


def polar(p, y):
    return 3 * (det(add_cell(p, y)) - det(p) - det(y)) % 5


def quotient(x):
    return sum(x) % 5, x[4], x[5]


def pack(x, y, bit):
    return x[:4] + y[:4] + (x[4], y[4], x[5], y[5], bit)


def unpack(s):
    return s[:4] + (s[8], s[10]), s[4:8] + (s[9], s[11]), s[12]


def check_references():
    masks, h_vectors, oriented = Counter(), set(), Counter()
    separates = both = 0
    embedding_masks = {a: tuple(int((a*k) % 5 in (1, 2)) for k in range(1, 5))
                       for a in range(1, 5)}
    for y in product(F5, repeat=4):
        u, v, w, z = y
        h = tuple(polar(p, y) for p in ROOTS)
        expected = tuple(3*t % 5 for t in (z, -w, -v, u, v+w-u-z))
        require(h == expected and sum(h) % 5 == 0, "reference hyperplane map")
        require(y == (2*h[3] % 5, -2*h[2] % 5, -2*h[1] % 5, 2*h[0] % 5),
                "reference hyperplane inverse")
        h_vectors.add(h)
        bits = tuple(int(t == 0) for t in h)
        require(bits == tuple(1-pow(t, 4, 5) for t in h), "F5 zero predicate")
        require(bits == tuple(int(polar(p, tuple(-t % 5 for t in y)) == 0)
                             for p in ROOTS), "Y negation invariance")
        masks[bits] += 1
        separates += bits[1] != bits[4]
        orientation = bits[1] != bits[4] and bits[2] != bits[3]
        both += orientation
        if orientation:
            places = [a for a, pattern in embedding_masks.items() if bits[1:] == pattern]
            require(len(places) == 1, "unique marked embedding on nonidentity roots")
            oriented[places[0]] += 1
    expected_per_mask = {0: 204, 1: 52, 2: 12, 3: 4, 4: 0, 5: 1}
    for bits in product(range(2), repeat=5):
        require(masks[bits] == expected_per_mask[sum(bits)], "complete mask count")
    require(len(h_vectors) == 625 and len(masks) == 27, "reference classification size")
    require((separates, both, masks[(0,)*5] + masks[(1,)*5]) == (200, 64, 205),
            "review reference counts")
    require(dict(oriented) == {1: 16, 2: 16, 3: 16, 4: 16}, "four embedding counts")
    expected_masks = ((1, 0, 0, 1, 0), (1, 0, 0, 0, 1), (0, 1, 0, 0, 0))
    actual_masks = tuple(tuple(int(polar(p, y) == 0) for p in ROOTS) for y in REFS)
    require(actual_masks == expected_masks and all(det(y) == 1 for y in REFS),
            "fixed determinant-one reference code")
    require(tuple(sum(WEIGHTS[i]*actual_masks[i][k] for i in range(3)) % 5
                  for k in F5) == M_BY_K, "five-code image")
    require(tuple((m+2) % 5 for m in M_BY_K) == tuple(F5), "fixed phase decoder")
    require(all(quotient(p+(0, 1)) == (2, 0, 1) for p in ROOTS), "all roots share Q")
    require(2**2 < 5 <= 2**3, "binary query lower bound")
    emit("REFERENCE", {"references": 625, "root_evaluations": 3125,
         "mask_classes": 27, "per_mask_by_ones": expected_per_mask,
         "separates_j_j4": separates, "separates_both": both,
         "constant": 205, "oriented_by_embedding": dict(oriented),
         "fixed_references": REFS, "masks": actual_masks, "M_by_k": M_BY_K,
         "minimum_binary_results": 3, "physical_cell_minimum_claimed": False})


def check_contact_blocks(contact):
    require(contact.reader_word("y", 1) == WORD, "contact word changed")
    cases = ready = 0
    for p in ROOTS:
        for y, weight in zip(REFS, WEIGHTS):
            delta = int(polar(p, y) == 0)
            for qx, rx, qy, ry, bit in product(F5, F5, F5, F5, range(2)):
                initial = pack(p+(qx, rx), y+(qy, ry), bit)
                require(contact.h(initial) == polar(p, y), "independent determinant h")
                middle = contact.execute(initial, WORD)
                xp, yp, bp = unpack(middle)
                qo = (qy + 3*delta) % 5
                yo = y + (qo, PERM[qo][PERM[qy][ry]])
                require((xp, yp, bp) == (p+(qx, rx), yo, bit), "complete occupied map")
                collector = (4, 3, 2, 1, 0, 4)
                copied = collector
                for _ in range(weight):
                    copied = add_cell(copied, yp)
                restored = contact.execute(middle, tuple(reversed(WORD)))
                require(restored == initial, "complete source/reference/bit restoration")
                require(copied == add_cell(collector, yo, weight), "occupied block increment")
                for _ in range(weight):
                    copied = add_cell(copied, yp, -1)
                require(copied == collector, "occupied collector inverse")
                if ry == 0:
                    require(yp[5] == delta, "ready reference writes the bit")
                    ready += 1
                cases += 1
    # Full CSUM is linear. Zero and all 12 basis vectors certify its matrix
    # and inverse, on every complete pair, independently of any preparation.
    for index in range(-1, 12):
        xy = tuple(int(j == index) for j in range(12))
        x, y = xy[:6], xy[6:]
        require(add_cell(add_cell(y, x), x, -1) == y, "full CSUM inverse basis")
        require(quotient(add_cell(y, x)) == add_cell(quotient(y), quotient(x)),
                "CSUM quotient compatibility")
    emit("BLOCK", {"complete_occupied_cases": cases, "ready_cases": ready,
                   "CSUM_basis_rows": 13, "shared_bit_values": 2})


@dataclass(frozen=True)
class Joined:
    sources: tuple
    references: tuple
    bit: int
    apparatus: object


def initial_state(app, labels, bit=0):
    old = app.prepare_ready_state(COLLECTOR[:4], COLLECTOR[:4], BUDGET)
    apparatus = replace(old, x_A=COLLECTOR, x_B=COLLECTOR)
    return Joined(tuple(ROOTS[k]+(0, 1) for k in labels),
                  tuple(y+(0, 0) for y in REFS), bit, apparatus)


def prefix_operations(omit_w=False):
    word = tuple(x for x in WORD if not (omit_w and x == "W"))
    ops, endpoints = [], []
    for lane in range(2):
        for ref, weight in enumerate(WEIGHTS):
            ops.extend((lane, ref, leaf) for leaf in word)
            ops.extend((lane, ref, "+") for _ in range(weight))
            ops.extend((lane, ref, leaf) for leaf in reversed(word))
            endpoints.append(len(ops))
    return tuple(ops), tuple(endpoints)


def joined_leaf(contact, state, op, inverse=False):
    lane, ref, leaf = op
    if leaf == "+":
        field = ("x_A", "x_B")[lane]
        old = getattr(state.apparatus, field)
        new = add_cell(old, state.references[ref], -1 if inverse else 1)
        return replace(state, apparatus=replace(state.apparatus, **{field: new}))
    packed = pack(state.sources[lane], state.references[ref], state.bit)
    source, reference, bit = unpack(contact.literal_leaf(packed, leaf))
    sources, refs = list(state.sources), list(state.references)
    sources[lane], refs[ref] = source, reference
    return Joined(tuple(sources), tuple(refs), bit, state.apparatus)


def run_prefix(contact, state, omit_w=False):
    ops, endpoints = prefix_operations(omit_w)
    original = state
    checkpoints = []
    for index, op in enumerate(ops, 1):
        previous_A = state.apparatus.x_A
        state = joined_leaf(contact, state, op)
        if op[0] == 1:
            require(state.apparatus.x_A == previous_A, "first collector changed in second lane")
        require(state.apparatus.to_apparatus_substate() ==
                original.apparatus.to_apparatus_substate(), "prefix altered the classical apparatus")
        require((state.apparatus.n, state.apparatus.c) == (0, 0), "undeclared prefix clock change")
        if index in endpoints:
            require((state.sources, state.references, state.bit) ==
                    (original.sources, original.references, original.bit),
                    "shared resources not restored at a block boundary")
            checkpoints.append((state.apparatus.x_A, state.apparatus.x_B))
    recovered = state
    for op in reversed(ops):
        recovered = joined_leaf(contact, recovered, op, inverse=True)
    require(recovered == original, "complete 7-cell prefix inverse")
    return state, tuple(checkpoints)


# Second wave/tape implementation: coordinate dictionaries, a signed-shell
# stencil built by permutation, and explicit scalar port recurrences. It calls
# no old geometry, propagation, energy, or readout helper.
Y_SITES = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))


class SparseWave:
    def __init__(self):
        lines = (ROOT / DOMAIN).read_text(encoding="ascii").splitlines()
        require(lines[0] == "x\ty\tz", "domain header")
        self.sites = tuple(tuple(map(int, line.split("\t"))) for line in lines[1:])
        self.domain = set(self.sites)
        self.stencil = {}
        for base, weight in (((1, 1, 0), 6), ((2, 0, 0), 1), ((2, 2, 0), 15),
                             ((3, 1, 0), 1), ((4, 0, 0), 1)):
            for perm in set(permutations(base)):
                for signs in product((-1, 1), repeat=3):
                    delta = tuple(a*b for a, b in zip(perm, signs))
                    self.stencil[delta] = Q(weight, 324)
        require(len(self.stencil) == 60 and sum(self.stencil.values()) == Q(8, 9),
                "independent stencil and energy row bound")
        require(all(self.stencil[tuple(-x for x in d)] == w
                    for d, w in self.stencil.items()), "symmetric independent stencil")
        extended = tuple(self.stencil) + ((0, 0, 0),)
        derived = {tuple(y[i]+a[i]+b[i] for i in range(3))
                   for y in Y_SITES for a in extended for b in extended}
        require(self.domain == derived and len(self.sites) == 705,
                "independent 705-site domain")

    def H(self, v):
        out = {}
        for site, value in v.items():
            out[site] = out.get(site, Q(0)) + Q(10, 9)*value
            for delta, weight in self.stencil.items():
                dest = tuple(a+b for a, b in zip(site, delta))
                if dest in self.domain:
                    out[dest] = out.get(dest, Q(0)) + weight*value
        return {s: v for s, v in out.items() if v}

    def source(self, z):
        mean = sum(z)/5
        values = tuple(v-mean for v in z) + (-mean,)
        return {site: value for site, value in zip(Y_SITES, values) if value}

    def cold(self):
        return ({}, {}, ((Q(0),)*4,)*4, 0)

    def deposit(self, x, z):
        u, v, tapes, k = x
        out = dict(v)
        for site, value in self.source(z).items():
            out[site] = out.get(site, Q(0)) + value
        return u, {s: v for s, v in out.items() if v}, tapes, k

    def step(self, x):
        u, v, (a0, a1, b0, b1), k = x
        hv = self.H(v)
        ports = dict(zip(Y_SITES[:4], range(4)))
        w = {}
        for site in set(hv) | set(u) | set(ports):
            if site in ports:
                value = hv.get(site, Q(0))/2 + 2*a0[ports[site]]
            else:
                value = hv.get(site, Q(0)) - u.get(site, Q(0))
            if value:
                w[site] = value
        bout = tuple(a0[i] - (w.get(s, Q(0))-u.get(s, Q(0)))/2
                     for i, s in enumerate(Y_SITES[:4]))
        return v, w, (a1, b1, bout, b0), (k+1) % 2

    def energy(self, x):
        u, v, tapes, _ = x
        hv = self.H(v)
        energy = (sum((a*a for a in u.values()), Q(0))
                  + sum((a*a for a in v.values()), Q(0))
                  - sum((a*hv.get(s, Q(0)) for s, a in u.items()), Q(0)))/2
        return energy + 2*sum((a*a for t in tapes for a in t), Q(0))

    def compare(self, x, actual):
        u, v, tapes, k = x
        require(tuple(u.get(s, Q(0)) for s in self.sites) == actual.u,
                "independent complete wave u")
        require(tuple(v.get(s, Q(0)) for s in self.sites) == actual.v,
                "independent complete wave v")
        require(tapes == (actual.A0, actual.A1, actual.B0, actual.B1) and k == actual.k,
                "independent complete tape and pointer")

    def trajectory(self, za, zb):
        x = self.cold()
        history = [x, x]
        for action in (za, None, None, zb, None, None):
            x = self.step(x) if action is None else self.deposit(x, action)
            history.append(x)
        return tuple(history)


def check_port_and_energy(app, independent):
    for m, expected_qr in enumerate(QR_BY_M):
        head = (1, 0, 0, 1, 3*m % 5, m)
        n, actual = app.native_tick_single(0, head)
        require(n == 1 and app.receiver_of(actual) == expected_qr, "first native port")
        z = app.eta_lift(expected_qr)
        require(z == Z_BY_M[m], "fixed source lift")
        cold = independent.deposit(independent.cold(), z)
        algebraic_energy = (sum(t*t for t in z) - sum(z)**2/5)/2
        require(independent.energy(cold) == algebraic_energy == COLD_ENERGIES[m],
                "independent cold energies")
        require(app.wave_energy(app.zero_qd(), app.apply_S(z)) == COLD_ENERGIES[m],
                "original cold energies")
    require(len(set(Z_BY_M)) == 5 and 4*max(COLD_ENERGIES) == ENERGY_BOUND < BUDGET,
            "five injective sources and prospective funding bound")
    # Direct small-matrix proof audit, independently of the old response helper.
    columns = []
    for j in range(4):
        z = tuple(Q(int(i == j)) for i in range(4))
        hz = independent.H(independent.source(z))
        columns.append(tuple(hz.get(s, Q(0)) for s in Y_SITES[:4]))
    matrix = tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))
    offsets = (349, 354, 354, 348)
    expected = tuple(tuple(Q(59, 54)*int(i == j)-Q(offsets[i], 1620)
                           for j in range(4)) for i in range(4))
    require(matrix == expected, "direct P-transpose H S formula")
    r0 = tuple(tuple(-t/4 for t in row) for row in matrix)
    require(app.get_derived_operators().R0 == r0, "old response against direct stencil")
    eigen_factor = Q(59, 54)-Q(sum(offsets), 1620)
    require(eigen_factor == Q(73, 324) > 0, "rank-one determinant factor")
    emit("PORT", {"q_r_by_M": QR_BY_M, "source_vectors": Z_BY_M,
         "cold_energies": COLD_ENERGIES, "common_budget": BUDGET,
         "a_priori_two_input_bound": ENERGY_BOUND, "domain_sites": 705,
         "wave_tape_coordinates": 1426, "R0_determinant": Q(1, 4)**4*Q(59, 54)**3*eigen_factor})


def phase_from_vector(z):
    # Fixed calibration on the five already frozen rational outputs. The
    # reader has no source, reference, collector, work-bit or d argument.
    return (Z_BY_M.index(z)+2) % 5


def relay(app, independent, state, labels):
    history = app.run_seven_steps(state.apparatus, return_boundaries=True)
    require(tuple((s.n, s.c) for s in history) ==
            ((0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (5, 7)),
            "unchanged seven-step schedule")
    za, zb = (Z_BY_M[M_BY_K[k]] for k in labels)
    other = independent.trajectory(za, zb)
    for s, t in zip(history, other):
        independent_energy = independent.energy(t)
        require(isinstance(independent_energy, Q), "nonrational independent energy")
        require(s.B == BUDGET and 0 <= s.b <= BUDGET and s.W+s.b == BUDGET,
                "one shared stock/work account")
        require(0 <= s.W <= ENERGY_BOUND, "frozen family energy bound")
        require(app.full_classical_energy(s.X) == s.W == independent_energy,
                "two implementations of the full energy")
        independent.compare(t, s.X)
    require(history[2].sigma_A == history[5].sigma_B == -1, "both contacts accepted")
    final = history[-1]
    cuts = (history[3].X.B0, history[4].X.B0, history[6].X.B0, history[7].X.B0)
    records = (final.X.A0, final.X.A1, final.X.B1, final.X.B0)
    require(records == cuts, "first two records retained through second input")
    port = app.extract_direct_port_readout(final, include_d=False, include_sigma_B=True)
    require(port.d is None, "hidden d supplied to reader")
    decoded = app.direct_source_reader(port)
    require(decoded["alpha_A"] == decoded["alpha_B"] == 1, "acceptance read")
    require((decoded["z_A"], decoded["z_B"]) == (za, zb), "original record-only vector reader")
    phases = phase_from_vector(decoded["z_A"]), phase_from_vector(decoded["z_B"])
    require(phases == labels, "two phase labels from retained records alone")
    return history, records, port, phases


def main():
    custody()
    contact = load_module("three_reference_contact", CONTACT)
    app = load_module("three_reference_apparatus", APPARATUS)
    check_references()
    check_contact_blocks(contact)
    independent = SparseWave()
    check_port_and_energy(app, independent)
    ops, _ = prefix_operations()
    require(len(ops) == 182 and Counter(op[2] for op in ops)["+"] == 14,
            "declared operation count")
    records_by_pair, rows, prefix_checkpoints = {}, [], []
    first_records, first_histories = {}, {}
    control_common = None
    prefix_cases = controls = independent_boundaries = 0
    max_work = Q(0)
    for ka, kb in product(F5, repeat=2):
        labels = ka, kb
        for bit in range(2):
            before = initial_state(app, labels, bit)
            after, checkpoints = run_prefix(contact, before)
            expected_heads = tuple((1, 0, 0, 1, 3*M_BY_K[k] % 5, M_BY_K[k])
                                   for k in labels)
            require((after.apparatus.x_A, after.apparatus.x_B) == expected_heads,
                    "actual shared collector endpoints")
            prefix_checkpoints.append((labels, bit, checkpoints))
            prefix_cases += 1
            if bit == 0:
                prepared = after
        history, records, port, phases = relay(app, independent, prepared, labels)
        independent_boundaries += len(history)
        records_by_pair[labels] = records
        max_work = max(max_work, *(s.W for s in history))
        current_first = records[:2]
        current_history = tuple(s.to_apparatus_substate().X for s in history[:5])
        if ka in first_records:
            require(first_records[ka] == current_first, "first record depends on later source")
            require(first_histories[ka] == current_history, "first wave/tape depends on later source")
        else:
            first_records[ka], first_histories[ka] = current_first, current_history
        rows.append({"input": labels, "output": phases, "work": history[-1].W,
                     "stock": history[-1].b, "records_sha256": digest(records)})
        control, _ = run_prefix(contact, initial_state(app, labels), omit_w=True)
        require((control.apparatus.x_A, control.apparatus.x_B) ==
                ((1, 0, 0, 1, 1, 2),)*2, "no-W constant collector")
        if control_common is None:
            control_common = control.apparatus
        require(control.apparatus == control_common, "no-W control depends on phase")
        controls += 1
    require(len(set(records_by_pair.values())) == 25, "record collision between phase pairs")
    require(len(set(first_records.values())) == 5, "first phase not separately recorded")
    # One actual unchanged downstream control replay is sufficient once all
    # 25 downstream initial states are exactly equal.
    control_final = app.run_seven_steps(control_common)
    require((control_final.X.A0, control_final.X.A1, control_final.X.B1, control_final.X.B0)
            == records_by_pair[(4, 4)], "no-W actual control replay")
    # Zero pistons are OUTSIDE the frozen five-root domain, not an absence
    # event. This fixed comparison exposes a real alias after compression.
    zero_before = initial_state(app, (4, 4))
    zero_before = replace(zero_before, sources=((0, 0, 0, 0, 0, 1),)*2)
    zero_after, _ = run_prefix(contact, zero_before)
    require(zero_after.apparatus == control_common, "outside-domain zero alias boundary")
    emit("PREFIX", {"two_root_inputs": 25, "complete_bit_cases": prefix_cases,
         "restored_references": 3, "shared_work_bits": 1, "complete_native_cells": 7,
         "declared_operations": len(ops), "contact_leaves": 168, "CSUM_leaves": 14,
         "per_block_restoration_checks": 6*prefix_cases,
         "checkpoint_sha256": digest(prefix_checkpoints)})
    emit("RELAYS", rows)
    emit("AUDIT", {"distinct_record_sets": len(set(records_by_pair.values())),
         "distinct_first_records": len(set(first_records.values())),
         "accepted_contacts": 50, "independent_full_wave_tape_boundaries": independent_boundaries,
         "maximum_observed_work": max_work, "energy_bound": ENERGY_BOUND,
         "no_W_prefixes": controls, "no_W_actual_replays": 1,
         "zero_piston_alias_phase": 4, "physical_absence_detected": False,
         "native_admission": "OPEN", "prefix_energy": "UNSUPPLIED",
         "autonomous_prefix": "UNSUPPLIED", "scientific_authors": "same-session"})
    custody()
    print("PASS five phases through shared references, one work bit and one funded two-use record")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        emit("FALSIFIER", str(exc))
        print("FAIL frozen three-reference scientific assertion")
