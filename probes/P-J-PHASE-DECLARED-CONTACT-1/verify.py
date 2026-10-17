#!/usr/bin/env python3
"""Pinned application of an existing declared contact to the j/inverse-j pair.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, Apache-2.0.
Both contact leaves and the funded apparatus are reused unchanged.
This is a declared finite composition, not a native/physical admission proof.
"""
from dataclasses import asdict, dataclass, replace
from fractions import Fraction as Q
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CONTACT = "probes/P-CONTACT-RECORD-1/verify.py"
APPARATUS = "probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py"
DEPENDENCIES = {
    CONTACT: "99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134",
    APPARATUS: "f0edfd80157c8993322a5338e88120c552908d3830fe5f9ea7536257213c6173",
    "probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/DOMAIN.tsv":
        "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0",
}
PISTONS = {"+": (0, 1, 0, 0), "-": (4, 4, 4, 4)}
REFERENCE = (1, 0, 0, 1, 0, 0)
SOURCE_VECTORS = {"+": (Q(1), Q(0), Q(0), Q(0)),
                  "-": (Q(1, 2), Q(1, 2), Q(0), Q(0))}
BUDGET = Q(2)
F5 = range(5)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def custody():
    for path, expected in DEPENDENCIES.items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            raise RuntimeError("frozen runtime changed: " + path)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def exact(value):
    if isinstance(value, Q):
        return [value.numerator, value.denominator]
    if hasattr(value, "__dataclass_fields__"):
        return exact(asdict(value))
    if isinstance(value, dict):
        return {k: exact(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [exact(v) for v in value]
    return value


def emit(label, value):
    print(label + " " + json.dumps(exact(value), sort_keys=True, separators=(",", ":")))


def digest(value):
    data = json.dumps(exact(value), sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def pack(x, y, bit):
    return x[:4] + y[:4] + (x[4], y[4], x[5], y[5], bit)


def unpack(state):
    return (state[:4] + (state[8], state[10]),
            state[4:8] + (state[9], state[11]), state[12])


def quotient(x):
    return sum(x) % 5, x[4], x[5]


def pair_quotient(state):
    x, y, bit = unpack(state)
    return quotient(x), quotient(y), bit


def det(p):
    return (p[0] * p[3] - p[1] * p[2]) % 5


def h_from_determinants(px, py):
    total = tuple((a + b) % 5 for a, b in zip(px, py))
    return 3 * (det(total) - det(px) - det(py)) % 5


def leaf_history(contact, state, word):
    history = [state]
    for leaf in word:
        state = contact.literal_leaf(state, leaf)
        history.append(state)
    return history


def check_contact(contact):
    word = contact.reader_word("y", 1)
    require(word == ("Uy", "ey", "dy", "W", "bx", "by", "W",
                     "dy", "ey", "W", "by", "bx", "W", "Uy"),
            "declared fourteen-leaf word changed")
    cases = ready_cases = prefixes = 0
    endpoints = {}
    for label, px in PISTONS.items():
        delta = int(label == "+")
        require(h_from_determinants(px, REFERENCE[:4]) == (0 if delta else 4),
                "phase/reference polarization mismatch")
        for qx, qy, rx, ry, bit in product(F5, F5, F5, F5, range(2)):
            original = pack(px + (qx, rx), REFERENCE[:4] + (qy, ry), bit)
            require(contact.h(original) == h_from_determinants(px, REFERENCE[:4]),
                    "literal h differs from determinant definition")
            hist = leaf_history(contact, original, word)
            final = hist[-1]
            expected = list(original)
            expected[9] = (qy + 3 * delta) % 5
            expected[11] = contact.P[expected[9]][contact.P[qy][ry]]
            require(final == tuple(expected), "complete contact endpoint mismatch")
            require(contact.execute(final, tuple(reversed(word))) == original,
                    "literal inverse failed")
            if ry == 0:
                require(final[11] == delta, "common-ready phase bit not written")
                ready_cases += 1
            for continuation in (contact.reader_word("x", 1),
                                 tuple(reversed(contact.reader_word("x", 1)))):
                continued = leaf_history(contact, final, continuation)
                require(all(s[11] * s[11] % 5 == final[11] * final[11] % 5
                            for s in continued), "retained square changed at a leaf")
                require(unpack(continued[-1])[1] == unpack(final)[1],
                        "other contact did not restore the complete y cell")
                prefixes += len(continued)
            cases += 1
        original = pack(px + (0, 1), REFERENCE, 0)
        hist = leaf_history(contact, original, word)
        endpoints[label] = hist
        require(unpack(hist[-1]) == (px + (0, 1),
                    (1, 0, 0, 1, 3 * delta, delta), 0), "fixed witness changed")
    first = next(i for i, (a, b) in enumerate(zip(endpoints["+"], endpoints["-"]))
                 if pair_quotient(a) != pair_quotient(b))
    require(first == 4 and word[first - 1] == "W", "wrong quotient-breaking leaf")
    roots = ((1, 0, 0, 0), PISTONS["+"], (0, 0, 1, 0),
             (0, 0, 0, 1), PISTONS["-"])
    require(tuple(int(h_from_determinants(p, REFERENCE[:4]) == 0) for p in roots)
            == (0, 1, 1, 0, 0), "single bit must not claim all five phases")
    emit("CONTACT", {"word": word, "complete_control_cases": cases,
         "ready_cases": ready_cases, "continuation_prefixes": prefixes,
         "first_quotient_difference_leaf": first,
         "receiver_endpoints": {k: unpack(v[-1])[1] for k, v in endpoints.items()},
         "literal_pair_histories_sha256": digest(endpoints), "mu5_bits": (0, 1, 1, 0, 0)})


def check_factor_alphabet(contact, app):
    basis = [(0,) * 6] + [tuple(int(i == j) for i in range(6)) for j in range(6)]
    for cell in basis:
        z, q, r = quotient(cell)
        expected = ((z, q, r), (-z, -q, -r), (2-z, 1-q, -r),
                    (2-z, 1-q, 1-r), (3-z, 2-q, 1-r))
        for i in F5:
            out = app.apply_generator(i, cell)
            require(quotient(out) == tuple(v % 5 for v in expected[i]),
                    "affine quotient certificate failed")
            require(app.apply_generator(i, out) == cell, "native involution failed")
        for i, letter in ((1, "b"), (3, "d"), (4, "e")):
            require(app.apply_generator(i, cell) == contact.native(cell, letter),
                    "the two existing implementations use different cell conventions")
    for z, q, r in product(F5, repeat=3):
        x = ((z-q-r) % 5, 0, 0, 0, q, r)
        actual = unpack(contact.literal_leaf(pack(x, (0,) * 6, 0), "Ux"))[0]
        rp = contact.P[q][r]
        require(quotient(actual) == ((z-r+rp) % 5, q, rp), "Ucal quotient mismatch")
    # Complete-cell additions and swaps are linear. The following basis
    # checks certify their full quotient identities, not a word-length search.
    for j in range(-1, 12):
        values = tuple(int(i == j) for i in range(12))
        x, y = values[:6], values[6:]
        for sign in (1, -1):
            result = tuple((a + sign * b) % 5 for a, b in zip(y, x))
            require(quotient(result) == tuple((a + sign * b) % 5
                    for a, b in zip(quotient(y), quotient(x))), "complete-cell sum factor failed")
    emit("FACTOR", {"affine_native_basis_rows": 35, "shared_native_convention_rows": 21,
         "Ucal_quotient_rows": 125, "complete_cell_sum_basis_rows": 26,
         "scope": "q/r histories only; complete piston copying is possible"})


@dataclass(frozen=True)
class JoinedState:
    sources: tuple
    bits: tuple
    apparatus: object


def common_initial(app, labels):
    # All receiver, clock, tape and budget fields are common before contact.
    # The common r=0 here is explicit, not the old p-only ready family r=1.
    old = app.prepare_ready_state(REFERENCE[:4], REFERENCE[:4], BUDGET)
    common = replace(old, x_A=REFERENCE, x_B=REFERENCE)
    return JoinedState(tuple(PISTONS[k] + (0, 1) for k in labels), (0, 0), common)


def contact_prefix(contact, state, omit_w=False):
    # The contact receiver IS the downstream native head. Each literal leaf
    # updates that shared cell, the real source and its bit in one joined state.
    initial_sources = state.sources
    for lane, field in enumerate(("x_A", "x_B")):
        for leaf in contact.reader_word("y", 1):
            if omit_w and leaf == "W":
                continue
            packed = pack(state.sources[lane], getattr(state.apparatus, field), state.bits[lane])
            source, head, bit = unpack(contact.literal_leaf(packed, leaf))
            sources, bits = list(state.sources), list(state.bits)
            sources[lane], bits[lane] = source, bit
            state = JoinedState(tuple(sources), tuple(bits), replace(state.apparatus, **{field: head}))
    require(state.sources == initial_sources and state.bits == (0, 0),
            "prefix did not restore original sources and bits")
    return state


def receiver(s):
    return s.n, s.c, s.to_apparatus_substate()


def relay(app, state):
    trajectory = app.run_seven_steps(state.apparatus, return_boundaries=True)
    require([(s.n, s.c) for s in trajectory]
            == [(0,0),(1,1),(1,2),(2,3),(3,4),(3,5),(4,6),(5,7)], "schedule changed")
    for s in trajectory:
        require(0 <= s.b <= s.B == BUDGET, "stock guard failed")
        require(s.b + s.W == BUDGET, "stock/work account failed")
        require(app.full_classical_energy(s.X) == s.W, "wave/tape energy account failed")
        require(0 <= s.W <= Q(8, 5), "declared a priori energy bound failed")
    require(trajectory[2].sigma_A == trajectory[5].sigma_B == -1,
            "both funded contacts must accept")
    final = trajectory[-1]
    cuts = (trajectory[3].X.B0, trajectory[4].X.B0,
            trajectory[6].X.B0, trajectory[7].X.B0)
    require((final.X.A0, final.X.A1, final.X.B1, final.X.B0) == cuts,
            "actual first records not retained through second use")
    port = app.extract_direct_port_readout(final, include_d=False, include_sigma_B=True)
    require(port.d is None, "hidden second-source buffer leaked into reader")
    decoded = app.direct_source_reader(port)
    require(decoded["alpha_A"] == decoded["alpha_B"] == 1, "record acceptance read failed")
    return trajectory, cuts, port, decoded


def main():
    custody()
    contact = load_module("declared_phase_contact", CONTACT)
    app = load_module("declared_phase_apparatus", APPARATUS)
    print("P-J-PHASE-DECLARED-CONTACT-1 exact declared-composition audit")
    check_contact(contact)
    check_factor_alphabet(contact, app)
    require(app.get_geometry().n_sites == 705 and app.get_geometry().wave_tape_basis_dim == 1426,
            "classical carrier changed")
    trajectories, records, controls = {}, {}, []
    common_y = None
    for labels in product(("+", "-"), repeat=2):
        key = "".join(labels)
        initial = common_initial(app, labels)
        if common_y is None:
            common_y = initial.apparatus
        require(initial.apparatus == common_y, "receiver prepared using source label")
        joined = contact_prefix(contact, initial)
        require(receiver(joined.apparatus) == receiver(initial.apparatus),
                "native prefix unexpectedly changed the classical apparatus")
        trajectory, cuts, port, decoded = relay(app, joined)
        for lane, field in enumerate(("x_A", "x_B")):
            actual_source = app.eta_lift(app.receiver_of(getattr(trajectory[1], field)))
            require(actual_source == SOURCE_VECTORS[labels[lane]], "actual U source differs")
            require(decoded["z_A" if lane == 0 else "z_B"] == actual_source,
                    "record-only reader did not recover the transmitted source")
        trajectories[key], records[key] = trajectory, (cuts, port, decoded)
        controls.append(contact_prefix(contact, initial, omit_w=True))
        final = trajectory[-1]
        emit("RELAY_" + key, {"native_heads_after_contact": (joined.apparatus.x_A, joined.apparatus.x_B),
             "cuts": cuts, "decoded": decoded, "first_cost": trajectory[2].W,
             "second_cost": trajectory[5].W - trajectory[4].W,
             "work": final.W, "stock": final.b, "budget": final.B,
             "complete_receiver_history_sha256": digest([receiver(s) for s in trajectory])})
    require(len({(r[1].b0, r[1].b2) for r in records.values()}) == 4,
            "four phase pairs are not separated by the actual retained port")
    for first in ("+", "-"):
        left, right = trajectories[first + "+"], trajectories[first + "-"]
        require([s.X for s in left[:5]] == [s.X for s in right[:5]],
                "second source altered wave/tape before its contact")
        require(left[5].X != right[5].X, "second accepted input has no wave/tape effect")
        require(records[first + "+"][0][:2] == records[first + "-"][0][:2],
                "second input changed the retained first records")
    # The fixed omitted-W word uses only quotient-compatible remaining leaves.
    # Full downstream starting states agree before the one control replay.
    require(all(s.apparatus == controls[0].apparatus for s in controls),
            "omitted-W word unexpectedly transmits phase to the port")
    control_run = relay(app, controls[0])
    require([receiver(s) for s in control_run[0]]
            == [receiver(s) for s in trajectories["++"]], "omitted-W control changed")
    emit("CONTROL", {"word_change": "omit the four W leaves in each A_y",
         "ordered_prefixes": 4, "downstream_replays": 1,
         "identical_complete_downstream_start": True, "decoded": control_run[3]})
    custody()
    print("CLOSURE declared-contact=TRANSMITTED funded-records=DISTINGUISHED both-contacts=ACCEPTED")
    print("BOUNDARY native/physical admission, native energy cost, autonomous prefix control, late arrival and renewal OPEN")
    print("AUDIT PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print("FALSIFIER " + str(exc))
        print("AUDIT FAIL")
