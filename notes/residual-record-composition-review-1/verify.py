#!/usr/bin/env python3
"""Bounded exact audit of V100-JOIN-1; never run before its public pin.

This is NOT an execution of CW-ALG-1, T_alg, or their enormous expansions.
All scientific work, including imports of pinned scientific dependencies,
is inside main(). Dependencies are local byte-identical copies, verified
against VERIFIER-PINS.json before either is imported. No network or Canon
read, randomness, floating point, generated code expansion, or file writes.

Universal claims use the proof steps mapped in CHECK-MAP.md. In particular,
the symbolic H operator has an arbitrary FULL FACTOR key; H is never I by
assumption and no finite collection of sample H families replaces its
compiler-defined value. Small complete tables certify its required fibre
law, not its concrete value.
"""

from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import re
import sys
import types


F = range(5)
BITS = range(2)
ZERO = (0, 0, 0)
IDENTITY_L = (1, 0, 0, 1)
STATE_SCHEMA = "symbolic=(piston_bit,q,rx,ry); fibre=(qx,qy,rx,ry)"
B_READ = ((1, 4, 2), (4, 0, 1), (3, 4, 4))
L5 = ((3, 3, 2), (3, 4, 2), (3, 2, 0))


class AuditFailure(Exception):
    pass


def require(condition, claim, detail=None):
    if not condition:
        raise AuditFailure(json.dumps({"claim": claim, "detail": detail},
                                     sort_keys=True, separators=(",", ":")))


def load_dependencies():
    """Hash both frozen files before importing either; no mutable authority."""
    directory = Path(__file__).resolve().parent
    manifest = json.loads((directory / "VERIFIER-PINS.json").read_text("utf-8"))
    require(manifest.get("schema") == "V100-JOIN-1/dependencies/v1", "pins_schema",
            manifest.get("schema"))
    entries = manifest.get("dependencies")
    require(isinstance(entries, list) and len(entries) == 2, "pins_count",
            len(entries) if isinstance(entries, list) else type(entries).__name__)
    names = {"algebra": "algebra_dependency.py", "contact": "contact_dependency.py"}
    staged = {}
    for entry in entries:
        name = entry.get("name")
        require(name in names and name not in staged, "pins_unique_name", name)
        require(entry.get("filename") == names[name], "pins_exact_filename", name)
        digest = entry.get("sha256", "")
        commit = entry.get("source_commit", "")
        source_path = entry.get("source_path", "")
        require(re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
                "pins_sha256_format", name)
        require(re.fullmatch(r"[0-9a-f]{40}", commit) is not None,
                "pins_public_commit_format", name)
        require(isinstance(source_path, str) and source_path.startswith("notes/")
                and ".." not in source_path and "\\" not in source_path,
                "pins_public_source_path", name)
        data = (directory / names[name]).read_bytes()
        actual_digest = sha256(data).hexdigest()
        require(actual_digest == digest, "pins_byte_identity",
                {"name": name, "expected": digest, "actual": actual_digest})
        staged[name] = (names[name], data, digest)
    modules = {}
    for name in ("algebra", "contact"):
        filename, data, _digest = staged[name]
        module = types.ModuleType("v100_pinned_" + name)
        module.__file__ = str(directory / filename)
        sys.modules[module.__name__] = module
        # The dependency's __main__ guard remains false. No pyc is written.
        exec(compile(data, filename, "exec"), module.__dict__)
        modules[name] = module
    return modules["algebra"], modules["contact"], {
        name: staged[name][2] for name in ("algebra", "contact")}


def delta(g):
    return int(g[1] == 0)


def mv3(matrix, vector):
    return tuple(sum(a*b for a, b in zip(row, vector)) % 5 for row in matrix)


def apply_matrix(h, q):
    a, b, c, d = h
    return ((a*q[0]+b*q[1]) % 5, (c*q[0]+d*q[1]) % 5)


def inverse_matrix(h):
    a, b, c, d = h
    determinant = (a*d-b*c) % 5
    require(determinant != 0, "invertible_H_required", h)
    s = pow(determinant, 3, 5)
    return (s*d % 5, -s*b % 5, -s*c % 5, s*a % 5)


def reader_formula(values, side, d, p_table, inverse=False):
    """PROOF (1)/(6), all occupied r; the other two entries are retained."""
    result = list(values)
    q = values[side]
    qout = (q + (-3 if inverse else 3)*d) % 5
    result[side] = qout
    result[side+2] = p_table[qout][p_table[q][values[side+2]]]
    return tuple(result)


def audit_reader_tables(contact, counts):
    for q, r in product(F, repeat=2):
        double = contact.P[q][contact.P[q][r]]
        literal = contact.swap_read(q, r)
        require(double == r, "P_involution", [q, r, double])
        require(contact.P[q][r] == literal, "P_literal_table",
                [q, r, contact.P[q][r], literal])
    cases = 0
    for side, d in product(BITS, repeat=2):
        images = set()
        for values in product(F, repeat=4):
            forward = reader_formula(values, side, d, contact.P)
            backward = reader_formula(values, side, d, contact.P, True)
            expected_forward = contact.fibre_reader(values, side, d, 1)
            expected_backward = contact.fibre_reader(values, side, d, 1, True)
            recovered = reader_formula(forward, side, d, contact.P, True)
            replayed = reader_formula(backward, side, d, contact.P)
            witness = {"side": side, "delta": d, "input": values,
                       "forward": forward, "inverse": backward}
            require(forward == expected_forward, "A_complete_forward",
                    dict(witness, expected=expected_forward))
            require(backward == expected_backward, "A_complete_inverse",
                    dict(witness, expected=expected_backward))
            require(recovered == values, "A_inverse_after_forward",
                    dict(witness, result=recovered))
            require(replayed == values, "A_forward_after_inverse",
                    dict(witness, result=replayed))
            require(forward[1-side] == values[1-side]
                    and forward[3-side] == values[3-side], "A_spectators", witness)
            if values[side+2] == 0:
                require(forward[side+2] == d, "A_ready_output_all_q", witness)
            require((backward[side+2] == 0) == (values[side+2] == d),
                    "A_inverse_ready_iff_record", witness)
            require((forward[side+2] in (0, 1, 2)) ==
                    (values[side+2] in (0, 1, 2)), "A_three_value_subset", witness)
            if d == 0:
                require(forward == values, "inactive_A_full_identity", witness)
            images.add(forward)
            cases += 1
        require(len(images) == 625, "A_complete_bijection",
                {"side": side, "delta": d, "image_count": len(images)})
    require(cases == 2500, "complete_A_rows_count", cases)
    counts["P_table_entries"] = 25
    counts["complete_A_fibre_rows"] = cases


def audit_linear_fibres(counts):
    """Every GL2(F5) and every q; no product with the full carrier."""
    matrices = rows = 0
    for h in product(F, repeat=4):
        if (h[0]*h[3]-h[1]*h[2]) % 5 == 0:
            continue
        hi = inverse_matrix(h)
        images = set()
        for q in product(F, repeat=2):
            forward = apply_matrix(h, q)
            backward = apply_matrix(hi, q)
            recovered = apply_matrix(hi, forward)
            replayed = apply_matrix(h, backward)
            images.add(forward)
            witness = {"H": h, "Hinv": hi, "q": q,
                       "forward": forward, "inverse": backward}
            require(recovered == q, "H_left_inverse", dict(witness, result=recovered))
            require(replayed == q, "H_right_inverse", dict(witness, result=replayed))
            rows += 1
        require(len(images) == 25, "H_whole_fibre_bijection",
                {"H": h, "image_count": len(images)})
        matrices += 1
    require(matrices == 480 and rows == 12000, "GL2_exact_counts",
            {"matrices": matrices, "q_rows": rows})
    counts["GL2_matrices"] = matrices
    counts["GL2_q_rows"] = rows


# Exact term algebra. Only the explicitly justified identities below rewrite:
# vector translations add, P_q^2=I, R^-1 R=R R^-1=I, and the keyed inverse of
# H_f cancels H_f. There is deliberately NO H_f=I rewrite or commutation rule.
def s_shift(q, shift):
    shift = tuple(x % 5 for x in shift)
    if q[0] == "shift":
        base, old = q[1:]
        return s_shift(base, tuple(a+b for a, b in zip(old, shift)))
    return q if shift == (0, 0) else ("shift", q, shift)


def s_component(q, side):
    if q[0] == "shift" and q[2][side] == 0:
        return s_component(q[1], side)
    return ("component", q, side)


def s_P(q, r):
    return r[2] if r[0] == "P" and r[1] == q else ("P", q, r)


def s_R(piston_bit, inverse=False):
    name, opposite = ("Rinv", "R") if inverse else ("R", "Rinv")
    if piston_bit[0] == opposite:
        return piston_bit[1]
    return (name, piston_bit)


def s_H(key, q, inverse=False):
    name, opposite = ("Hinv", "H") if inverse else ("H", "Hinv")
    if q[0] == opposite and q[1] == key:
        return q[2]
    return (name, key, q)


def s_A(state, side, d, inverse=False):
    piston_bit, q, rx, ry = state
    step = (-3 if inverse else 3)*d
    qout = s_shift(q, (step, 0) if side == 0 else (0, step))
    record = rx if side == 0 else ry
    changed = s_P(s_component(qout, side), s_P(s_component(q, side), record))
    return (piston_bit, qout, changed, ry) if side == 0 else (
        piston_bit, qout, rx, changed)


def s_T(state, inverse=False):
    piston_bit, q, rx, ry = state
    if inverse:
        before = s_R(piston_bit, True)
        return before, s_H((before, rx, ry), q, True), rx, ry
    return s_R(piston_bit), s_H((piston_bit, rx, ry), q), rx, ry


def s_V(state, d0, d1, inverse=False):
    if inverse:
        return s_A(s_T(s_A(state, 1, d1, True), True), 0, d0, True)
    return s_A(s_T(s_A(state, 0, d0)), 1, d1)


def audit_symbolic_composition(counts):
    """PROOF (3)-(6): arbitrary factor-keyed H, q and occupied r symbols."""
    source = (("piston_bit", "input"), ("q", "input"),
              ("rx", "input"), ("ry", "input"))
    rows = 0
    for d0, d1 in product(BITS, repeat=2):
        first = s_A(source, 0, d0)
        transported = s_T(first)
        final = s_V(source, d0, d1)
        u = s_shift(source[1], (3*d0, 0))
        rxhat = s_P(s_component(u, 0), s_P(s_component(source[1], 0), source[2]))
        fx = (source[0], rxhat, source[3])
        v = s_H(fx, u)
        expected = (s_R(source[0]), s_shift(v, (0, 3*d1)), rxhat,
                    s_P(s_component(s_shift(v, (0, 3*d1)), 1),
                        s_P(s_component(v, 1), source[3])))
        witness = {"d0": d0, "d1": d1, "source": source, "after_Ax": first,
                   "after_T": transported, "result": final}
        require(final == expected, "V_exact_symbolic_formula_4",
                dict(witness, expected=expected))
        require(transported[2:] == first[2:], "T_restores_both_occupied_records", witness)
        recovered = s_V(final, d0, d1, True)
        inverse_first = s_V(source, d0, d1, True)
        replayed = s_V(inverse_first, d0, d1)
        require(recovered == source, "V_symbolic_inverse_forward",
                dict(witness, recovered=recovered))
        require(replayed == source, "V_symbolic_forward_inverse",
                dict(witness, inverse_first=inverse_first, recovered=replayed))
        keyed_q = s_H((first[0], first[2], first[3]), first[1])
        require(transported[1] == keyed_q, "H_key_is_actual_factor_after_Ax",
                dict(witness, expected_keyed_q=keyed_q))
        rows += 1
    # A deliberately different factor key must not cancel, demonstrating the
    # formal system never silently identifies distinct state-dependent H's.
    key1, key2 = ("factor", 1), ("factor", 2)
    q = ("q", "arbitrary")
    mixed = s_H(key2, s_H(key1, q), True)
    single = s_H(key1, q)
    require(mixed != q, "different_H_keys_not_cancelled", [key1, key2, q, mixed])
    require(single != q, "H_not_assumed_identity", [key1, q, single])
    counts["symbolic_delta_pairs"] = rows
    counts["symbolic_roundtrip_identities"] = 2*rows


def audit_target(algebra, counts):
    rows = 0
    for g in product(F, repeat=3):
        mg = algebra.target(g)
        lhs, rhs = mv3(B_READ, mg), mv3(L5, mv3(B_READ, g))
        recovered = algebra.target_inverse(mg)
        replayed = algebra.target(algebra.target_inverse(g))
        require(lhs == rhs, "fixed_readout_matrix", [g, mg, lhs, rhs])
        require(recovered == g, "M_inverse_forward", [g, mg, recovered])
        require(replayed == g, "M_forward_inverse", [g, replayed])
        require(delta(mg) == (1-pow(sum(g) % 5, 4, 5)) % 5,
                "second_record_delta_formula", [g, mg, delta(mg)])
        rows += 1
    counts["Gram_target_rows"] = rows


def slot_map(algebra, slot, inverse=False):
    """Exact quotient via the pinned atlas; L,n remain symbolic spectators.

    g=0 denotes the ENTIRE zero-Gram identity branch of SPEC, not a sampled
    piston tuple. On nonzero branches one common atlas label reads off the
    quotient: SPEC proves that this action is independent of L,n,r.
    """
    g, j, eta = slot
    if g == ZERO:
        return slot
    p = algebra.atlas_decode(g, IDENTITY_L, 0, j)
    encoded = algebra.atlas_encode(p)
    witness = {"slot": slot, "inverse": inverse, "piston": p, "encoding": encoded}
    require(encoded == (g, IDENTITY_L, 0, j), "slot_chart_exact_roundtrip", witness)
    require(algebra.reachable(p, eta) == slot_reachable(algebra, slot),
            "slot_reachability_matches_pinned_atlas", witness)
    operation = algebra.pi_inverse if inverse else algebra.pi
    output, etaout = operation(p, eta)
    gout, lout, nout, jout = algebra.atlas_encode(output)
    require(lout == IDENTITY_L and nout == 0, "slot_spectators_retained",
            dict(witness, output_piston=output, output_bit=etaout, output_L=lout, output_n=nout))
    return gout, jout, etaout


def slot_reachable(algebra, slot):
    g, j, eta = slot
    return eta == 0 if g == ZERO else (
        j+algebra.width(g)*eta < algebra.orbit_width(g))


def slot_s1(algebra, slot, rx, ry):
    g, j, eta = slot
    if rx != delta(algebra.target_inverse(g)) or ry != delta(g):
        return False
    if g == ZERO:
        return eta == 0
    return j+algebra.width(g)*eta < algebra.width(algebra.target_inverse(g))


def audit_slots_and_s1(algebra, counts):
    slots = [(ZERO, 0, eta) for eta in BITS]
    for g in product(F, repeat=3):
        if g != ZERO:
            slots.extend((g, j, eta) for j in range(algebra.width(g)) for eta in BITS)
    require(len(slots) == 1282, "complete_slot_carrier_size", len(slots))
    slot_set = set(slots)
    images = set()
    reached = prepared = s1_weight = record_rows = 0
    for slot in slots:
        g, _j, eta = slot
        forward = slot_map(algebra, slot)
        backward = slot_map(algebra, slot, True)
        witness = {"slot": slot, "forward": forward, "inverse": backward}
        require(forward in slot_set and backward in slot_set, "slot_map_closed", witness)
        recovered = slot_map(algebra, forward, True)
        replayed = slot_map(algebra, backward)
        require(recovered == slot, "slot_left_inverse", dict(witness, result=recovered))
        require(replayed == slot, "slot_right_inverse", dict(witness, result=replayed))
        active = slot_reachable(algebra, slot)
        require(slot_reachable(algebra, forward) == active, "Omega_forward_closed",
                dict(witness, active=active))
        require(slot_reachable(algebra, backward) == active, "Omega_inverse_closed",
                dict(witness, active=active))
        if active:
            require(forward[0] == algebra.target(g), "Omega_target_step", witness)
            reached += int(g != ZERO)
        if eta == 0:
            prepared += int(g != ZERO)
            require(slot_s1(algebra, forward, delta(g), delta(forward[0])),
                    "S0_maps_to_S1", dict(witness, rx=delta(g), ry=delta(forward[0])))
        weight = 6625 if g == ZERO else 600
        for rx, ry in product(F, repeat=2):
            # Complete A inverse tables already prove, for EVERY q, that a
            # ready inverse exists iff each occupied output equals its delta.
            inverse_ready = (backward[2] == 0 and rx == delta(backward[0])
                             and ry == delta(g))
            declared = slot_s1(algebra, slot, rx, ry)
            require(declared == inverse_ready, "S1_iff_full_inverse_in_S0",
                    dict(witness, rx=rx, ry=ry, declared=declared, inverse_ready=inverse_ready))
            if declared:
                s1_weight += weight
            record_rows += 1
        images.add(forward)
    require(images == slot_set, "complete_slot_permutation",
            {"image_count": len(images), "carrier_count": len(slot_set),
             "first_missing": min(slot_set-images) if slot_set-images else None,
             "first_extra": min(images-slot_set) if images-slot_set else None})
    require(prepared == 640 and reached == 740, "prepared_reachable_slot_counts",
            {"prepared": prepared, "reachable": reached})
    require(s1_weight == 390625, "S1_piston_bit_record_count", s1_weight)
    require(s1_weight*25 == 9765625, "S1_full_q_count", s1_weight*25)
    require((6625+740*600)*25*25 == 281640625, "Omega_full_carrier_count",
            (6625+740*600)*25*25)
    require((6625+740*600)*25 == 11265625, "T_ready_records_reachable_count",
            (6625+740*600)*25)
    require(record_rows == 32050, "S1_occupied_record_rows_count", record_rows)
    counts.update(reduced_slots_including_zero_branches=len(slots),
                  nonzero_prepared_slots=prepared, nonzero_reachable_slots=reached,
                  S1_occupied_record_rows=record_rows,
                  S1_states=s1_weight*25, Omega_states=281640625)


def audit_prefixes_and_boundaries(contact, counts):
    """All possible W sign choices give a universal overapproximation.

    This does not claim that all abstract choices are dynamically reachable.
    Every actual branch is covered, and no T_alg prefix is audited here.
    """
    expected = ("Uy", "ey", "dy", "W", "bx", "by", "W", "dy", "ey",
                "W", "by", "bx", "W", "Uy")
    word = contact.reader_word("y", 1)
    require(word == expected, "Ay_literal_word_scope", {"actual": word, "expected": expected})
    require(len(word) == 14 and word.count("W") == 4, "Ay_leaf_W_counts",
            {"leaves": len(word), "W": word.count("W")})
    require(set(word) == {"Uy", "ey", "dy", "W", "bx", "by"}, "Ay_sign_leaf_family",
            sorted(set(word)))
    boundaries = 0
    for direction, current in enumerate((word, tuple(reversed(word)))):
        for choices in product((1, -1), repeat=4):
            for initial in F:
                r = initial
                k = 0
                witness = {"direction": "reverse" if direction else "forward",
                           "W_signs": choices, "initial_r": initial}
                require(r*r % 5 == initial*initial % 5, "square_empty_prefix",
                        dict(witness, leaf_position=0, result_r=r))
                boundaries += 1
                for position, leaf in enumerate(current, 1):
                    sign = 1
                    if leaf == "bx":
                        sign = -1
                    elif leaf == "W":
                        sign = choices[k]
                        k += 1
                    r = sign*r % 5
                    require(r*r % 5 == initial*initial % 5,
                            "square_all_possible_second_reader_prefixes",
                            dict(witness, leaf_position=position, leaf=leaf, result_r=r))
                    boundaries += 1
                require(k == 4, "all_W_choices_used", dict(witness, used=k))
    require(boundaries == 2400, "prefix_boundary_count", boundaries)
    squares = tuple(r*r % 5 for r in F)
    require(squares == (0, 1, 4, 4, 1), "square_not_globally_binary", squares)
    zero = (0,)*13
    changed = contact.literal_leaf(zero, "dx")
    require(changed[10] == 1, "square_protection_not_global",
            {"input": zero, "leaf": "dx", "result": changed})
    once = contact.local_reader(0, 0, 1, 1)
    twice = contact.local_reader(*once, 1, 1)
    require(once == (3, 1) and twice == (1, 0), "whole_reader_reuse_can_erase",
            {"input": (0, 0), "first": once, "second": twice})
    for q, r in product(F, repeat=2):
        completed_zero = contact.local_reader(q, r, 1, 0)
        inactive_contact = contact.local_reader(q, r, 0, 1)
        inactive_zero = contact.local_reader(q, r, 0, 0)
        require(completed_zero == (q, r), "unused_completed_zero_equal",
                {"input": (q, r), "result": completed_zero})
        require(inactive_contact == inactive_zero == (q, r),
                "inactive_completed_contact_equals_zero_experiment",
                {"input": (q, r), "contact": inactive_contact, "zero": inactive_zero})
    counts["second_reader_prefix_boundaries_forward_reverse"] = boundaries
    counts["unused_completed_zero_rows"] = 25


def main():
    require(sys.version_info[:2] == (3, 12), "Python_3_12_required", tuple(sys.version_info[:2]))
    algebra, contact, hashes = load_dependencies()
    counts = {}
    audit_reader_tables(contact, counts)
    audit_linear_fibres(counts)
    audit_symbolic_composition(counts)
    audit_target(algebra, counts)
    audit_slots_and_s1(algebra, counts)
    audit_prefixes_and_boundaries(contact, counts)
    output = {
        "status": "PASS_LIMITED_COMPOSITION_CONTRACTS",
        "contract": "V100-JOIN-1",
        "dependency_sha256": hashes,
        "counts": counts,
        "proof_dependencies": ["PROOF.md (1)-(12)", "CW-ALG-1 exact keyed q lift",
                               "P-CONTACT-RECORD-1 complete leaf contracts"],
        "not_executed": ["CW-ALG-1 expansion", "T_alg native word", "V native word",
                         "full X enumeration", "exact repeated V reachable-set census"],
        "scope": "Exact small contracts and symbolic composition; theorem dependencies remain explicit."
    }
    sys.stdout.buffer.write((json.dumps(output, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8"))


if __name__ == "__main__":
    try:
        main()
    except AuditFailure as failure:
        sys.stdout.buffer.write((json.dumps({"status": "FAIL", "detail": str(failure)},
                                           sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8"))
        raise SystemExit(1)
