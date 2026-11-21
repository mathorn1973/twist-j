#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Independent exact breaker, specified only by the frozen PREREG.md.

Representation: five cyclic polynomial coefficients, modulo addition of
the same integer to all coefficients.  The unique representative has minimum
coefficient zero.  Multiplication is cyclic convolution, and conjugation
reverses exponents.  No predecessor checker or companion source is imported.
"""

import hashlib
import itertools
import json
import sys


class Cyclo:
    __slots__ = ("c",)

    def __init__(self, coefficients):
        coefficients = tuple(coefficients)
        if len(coefficients) != 5 or any(type(a) is not int for a in coefficients):
            raise TypeError("five integer cyclic coefficients required")
        m = min(coefficients)
        self.c = tuple(a - m for a in coefficients)

    @classmethod
    def integer(cls, n):
        return cls((n, 0, 0, 0, 0))

    def __add__(self, other):
        return Cyclo(a + b for a, b in zip(self.c, other.c))

    def __neg__(self):
        return Cyclo(-a for a in self.c)

    def __sub__(self, other):
        return self + (-other)

    def scale(self, n):
        return Cyclo(n * a for a in self.c)

    def __mul__(self, other):
        out = [0] * 5
        for a, x in enumerate(self.c):
            for b, y in enumerate(other.c):
                out[(a + b) % 5] += x * y
        return Cyclo(out)

    def __eq__(self, other):
        return isinstance(other, Cyclo) and self.c == other.c

    def __hash__(self):
        return hash(self.c)

    def divide_if_integral(self, divisor):
        # One coefficient is zero, so divisibility in the quotient is
        # equivalent to divisibility of all five chosen coefficients.
        if any(a % divisor for a in self.c):
            return None
        return Cyclo(a // divisor for a in self.c)

    def conjugate(self):
        return Cyclo(self.c[(-k) % 5] for k in range(5))

    def hermitian(self):
        return self * self.conjugate()

    def q(self):
        # This expression is invariant under the discarded common shift.
        numerator = 5 * sum(a * a for a in self.c) - sum(self.c) ** 2
        if numerator % 2:
            raise ArithmeticError("nonintegral quadratic account")
        return numerator // 2

    def residue(self):
        return sum(self.c) % 5

    def coefficients4(self):
        return [a - self.c[4] for a in self.c[:4]]


ZERO = Cyclo.integer(0)
ONE = Cyclo.integer(1)
THREE = Cyclo.integer(3)
ROOTS = tuple(Cyclo(int(a == b) for a in range(5)) for b in range(5))
JROOT = ROOTS[1]
RHO = ROOTS[2]
UNIT_J = ONE + RHO
PHI = -ROOTS[2] - ROOTS[3]
ROOT_INDEX = {value: index for index, value in enumerate(ROOTS)}


def total(values):
    out = ZERO
    for value in values:
        out = out + value
    return out


class Broken(Exception):
    def __init__(self, condition, context, details=None):
        self.report = {"condition": condition, "context": context}
        if details is not None:
            self.report["details"] = details
        super().__init__(condition)


def demand(condition, name, context, details=None):
    if not condition:
        raise Broken(name, context, details)


def dump_state(state):
    slots, field = state
    return {"slots": [v.coefficients4() for v in slots],
            "field": field.coefficients4()}


def full_account(state):
    slots, field = state
    references = (ZERO,) * (len(slots) - 1)
    q = slots[0].q() + field.q()
    h = slots[0].hermitian() + field.hermitian()
    for value, reference in zip(slots[1:], references):
        q += value.q() + reference.q() + (value - reference).q()
        h = h + value.hermitian() + reference.hermitian() + (value - reference).hermitian()
    return q, h


def gauss(state):
    slots, field = state
    return slots[0] + field, total(slots[1:]) - field


def ordinary(a, b):
    difference_half = (a - b).divide_if_integral(2)
    if difference_half is None:
        return a, b, False
    midpoint = (a + b).divide_if_integral(2)
    if midpoint is None:
        raise ArithmeticError("integral difference without integral midpoint")
    rotated = RHO * difference_half
    return midpoint + rotated, midpoint - rotated, True


def loaded(x, value, reference, field):
    displacement = (value.scale(2) - x - reference + field).divide_if_integral(4)
    if displacement is None:
        return x, value, field, False
    current = (RHO - ONE) * displacement
    return x - current, value + current, field + current, True


def actual_step(state, pair):
    slots, field = state
    out = list(slots)
    a, b = pair
    if 0 in pair:
        other = b if a == 0 else a
        out[0], out[other], field, admitted = loaded(slots[0], slots[other], ZERO, field)
    else:
        out[a], out[b], admitted = ordinary(slots[a], slots[b])
    return (tuple(out), field), admitted


def shadow_step(state, pair):
    slots, field = state
    out = list(slots)
    a, b = pair
    out[a], out[b], admitted = ordinary(slots[a], slots[b])
    if 0 in pair:
        other = b if a == 0 else a
        # Advance the shadow field from its own B-slot current.
        field = field + (out[other] - slots[other])
    return (tuple(out), field), admitted


def empty_counts():
    return {"attempts": 0, "admitted": 0, "refused": 0,
            "accepted_diagonal": 0, "state_changes": 0, "field_changes": 0}


def combine_counts(destination, source):
    for key, value in source.items():
        destination[key] += value


def check_cut(state, baseline, context, individual_q=None):
    slots, field = state
    demand(all(type(a) is int for value in (*slots, field) for a in value.c),
           "integrality", context, dump_state(state))
    demand(gauss(state) == (ZERO, ZERO), "Gauss at both vertices", context, dump_state(state))
    demand(total(slots) == ZERO, "total charge", context, dump_state(state))
    demand(full_account(state) == baseline["account"], "complete Q and Hermitian accounts", context,
           dump_state(state))
    demand(tuple(v.residue() for v in slots) == baseline["residues"], "slot residues", context,
           dump_state(state))
    demand(field.residue() == baseline["field_residue"], "field residue", context, dump_state(state))
    if individual_q is not None:
        demand(tuple(v.q() for v in slots) == individual_q, "individual slot Q", context,
               dump_state(state))


def execute_word(initial, word, label, individual_q=None):
    baseline = {"account": full_account(initial),
                "residues": tuple(v.residue() for v in initial[0]),
                "field_residue": initial[1].residue()}
    state = initial
    shadow = initial
    counts = empty_counts()
    check_cut(state, baseline, {"run": label, "cut": 0}, individual_q)
    for cut, pair in enumerate(word, 1):
        previous = state
        state, admitted = actual_step(state, pair)
        shadow, shadow_admitted = shadow_step(shadow, pair)
        context = {"run": label, "cut": cut, "contact": list(pair)}
        demand(state == shadow and admitted == shadow_admitted,
               "loaded/ordinary shadow equality", context,
               {"loaded": dump_state(state), "shadow": dump_state(shadow)})
        demand(admitted or state == previous, "refusal identity", context, dump_state(state))
        check_cut(state, baseline, context, individual_q)
        changed = state != previous
        counts["attempts"] += 1
        counts["admitted" if admitted else "refused"] += 1
        counts["accepted_diagonal"] += int(admitted and not changed)
        counts["state_changes"] += int(changed)
        counts["field_changes"] += int(state[1] != previous[1])
    return state, counts


def inverse_word(word):
    return tuple(pair for pair in reversed(word) for _ in range(4))


def two_contact_audit():
    word = ((0, 2), (0, 3))
    inputs = [("J", UNIT_J), ("phi", PHI)]
    inputs.extend(("J*rho^" + str(r), UNIT_J * ROOTS[(2 * r) % 5]) for r in range(1, 5))
    demand(len({d for _, d in inputs}) == 6, "six distinct inputs", "two-contact setup")
    rows = []
    counts = {"forward": empty_counts(), "inverse": empty_counts()}
    for name, d in inputs:
        initial = ((-d, d, -THREE - RHO, ZERO, THREE + RHO), d)
        demand(full_account(initial)[0] == 80, "initial account 80", name)
        endpoint, forward = execute_word(initial, word, "two-contact/" + name + "/forward")
        expected = (((-UNIT_J, UNIT_J, UNIT_J.scale(-2), RHO - ONE, THREE + RHO), UNIT_J)
                    if name == "J" else initial)
        demand(endpoint == expected, "predicted primary endpoint", name,
               {"actual": dump_state(endpoint), "expected": dump_state(expected)})
        demand(forward["admitted"] == (2 if name == "J" else 0), "admission table", name, forward)
        demand(endpoint[0][:2] == initial[0][:2] and endpoint[1] == initial[1],
               "whole source pair and field return", name)
        demand(total(initial[0][2:]) == ZERO and total(endpoint[0][2:]) == ZERO,
               "archive neutrality", name)
        record_q = endpoint[0][3].q()
        demand(record_q == (5 if name == "J" else 0), "record Q", name, record_q)
        restored, backward = execute_word(endpoint, inverse_word(word), "two-contact/" + name + "/inverse")
        demand(restored == initial, "literal inverse restores", name, dump_state(restored))
        combine_counts(counts["forward"], forward)
        combine_counts(counts["inverse"], backward)
        rows.append({"input": name, "d": d.coefficients4(), "endpoint": dump_state(endpoint),
                     "record_q": record_q, "account": full_account(endpoint)[0],
                     "forward": forward, "inverse": backward, "field_returned": True})
    return {"inputs": len(inputs), "rows": rows, "counts": counts}


def p_word(i, k):
    within = ((2 * i, 2 * i + 1),)
    across = ((2 * i, 2 * k + 1), (2 * i + 1, 2 * k))
    contacts = list(within)
    for power in range(1, 5):
        contacts.extend(across * power)
        contacts.extend(within)
    return tuple(contacts)


def pair_phases(slots, context):
    phases = []
    for index in range(0, len(slots), 2):
        demand(slots[index] in ROOT_INDEX and slots[index + 1] == -slots[index],
               "endpoint is an opposite root pair", context,
               [v.coefficients4() for v in slots[index:index + 2]])
        phases.append(ROOT_INDEX[slots[index]])
    return phases


def root_pair_audit():
    word = p_word(0, 1) * 2 + p_word(0, 2) * 2 + p_word(1, 2) * 2
    backward_word = inverse_word(word)
    demand(len(word) == 150 and len(backward_word) == 600, "word lengths", "root setup")
    counts = {"forward": empty_counts(), "inverse": empty_counts()}
    writer_counts = {"forward": empty_counts(), "inverse": empty_counts()}
    phase_table = []
    writer_table = []
    fixed_preparations = {}
    for r, s, t in itertools.product(range(5), repeat=3):
        phases = (r, s, t)
        slots = tuple(v for exponent in phases for v in (ROOTS[exponent], -ROOTS[exponent]))
        initial = (slots, -slots[0])
        initial_q = tuple(v.q() for v in slots)
        demand(full_account(initial)[0] == 24, "initial account 24", list(phases))
        run = "root-pairs/" + ",".join(str(k) for k in phases)
        endpoint, forward = execute_word(initial, word, run + "/forward", initial_q)
        observed = pair_phases(endpoint[0], list(phases))
        predicted = [(r + 3 * s + 2 * t) % 5, (r + 4 * s + t) % 5, (2 * s + 4 * t) % 5]
        demand(observed == predicted, "full phase matrix", list(phases),
               {"actual": observed, "expected": predicted})
        restored, backward = execute_word(endpoint, backward_word, run + "/inverse", initial_q)
        demand(restored == initial, "literal inverse restores", list(phases), dump_state(restored))
        combine_counts(counts["forward"], forward)
        combine_counts(counts["inverse"], backward)
        phase_table.append({"input": list(phases), "output": observed})
        if t == s:
            demand(observed == [r, r, s], "positive writer phase output", list(phases), observed)
            demand(endpoint[0][:2] == slots[:2], "writer source pair return", list(phases))
            demand(endpoint[0][4:] == slots[4:], "writer reference pair return", list(phases))
            demand(endpoint[0][2:4] == slots[:2], "writer memory reads source phase", list(phases))
            demand(endpoint[1] == initial[1], "writer field return", list(phases))
            if s in fixed_preparations:
                demand(slots[2:] == fixed_preparations[s], "common memory/reference preparation", list(phases))
            else:
                fixed_preparations[s] = slots[2:]
            blank_equal = endpoint[0][2:4] == slots[2:4]
            demand(blank_equal == (r == s), "blank coincidence exactly r=s", list(phases))
            combine_counts(writer_counts["forward"], forward)
            combine_counts(writer_counts["inverse"], backward)
            writer_table.append({"input": list(phases), "output": observed,
                                 "blank_equal": blank_equal, "field_returned": True,
                                 "forward": forward, "inverse": backward})
    demand(len(phase_table) == 125 and len(writer_table) == 25, "exhaustion cardinality", "root audit")
    encoded = json.dumps(phase_table, sort_keys=True, separators=(",", ":")).encode("ascii")
    return {"inputs": 125, "forward_word_length": len(word), "inverse_word_length": len(backward_word),
            "account": 24, "counts": counts, "phase_table": phase_table,
            "phase_table_sha256": hashlib.sha256(encoded).hexdigest(),
            "positive_writer": {"inputs": 25, "rows": writer_table, "counts": writer_counts,
                                "blank_outputs": sum(row["blank_equal"] for row in writer_table)}}


def general_loaded_audit():
    """Additional finite off-manifold audit of the declared loaded formula."""
    values = (ZERO, ONE, JROOT, RHO)
    counts = empty_counts()
    cases = 0

    def account(state):
        x, value, reference, field = state
        terms = (x, value, reference, value - reference, field)
        return sum(v.q() for v in terms), total(v.hermitian() for v in terms)

    for indices in itertools.product(range(4), repeat=4):
        initial = tuple(values[k] for k in indices)
        x, value, reference, field = initial
        baseline_account = account(initial)
        baseline_gauss = (x + field, value - field)
        baseline_sum = x + value
        baseline_residues = tuple(v.residue() for v in initial)
        state = initial
        # One contact, then its literal four-contact inverse.
        for cut in range(1, 6):
            old = state
            x, value, reference, field = old
            new_x, new_value, new_field, admitted = loaded(x, value, reference, field)
            state = (new_x, new_value, reference, new_field)
            context = {"run": "general-loaded", "input_indices": list(indices), "cut": cut}
            demand(account(state) == baseline_account, "general loaded Q and Hermitian account", context)
            demand((new_x + new_field, new_value - new_field) == baseline_gauss,
                   "general loaded Gauss residual preservation", context)
            demand(new_x + new_value == baseline_sum, "general loaded total charge", context)
            demand(tuple(v.residue() for v in state) == baseline_residues,
                   "general loaded residues", context)
            demand(all(type(a) is int for v in state for a in v.c), "general loaded integrality", context)
            demand(admitted or state == old, "general loaded refusal identity", context)
            counts["attempts"] += 1
            counts["admitted" if admitted else "refused"] += 1
            counts["accepted_diagonal"] += int(admitted and state == old)
            counts["state_changes"] += int(state != old)
            counts["field_changes"] += int(new_field != field)
        demand(state == initial, "general loaded literal inverse", list(indices))
        cases += 1
    return {"inputs": cases, "attempts_per_input": 5, "counts": counts}


def main():
    report = {"checker": "independently-constructed-breaker",
              "exposure": "frozen PREREG.md only; no verify.py, proof, prior checker or result read",
              "scope": "NON-CANONICAL L1 incubation; no authority; one execution architecture",
              "scientific_status": "candidate-C"}
    try:
        report["two_contact"] = two_contact_audit()
        report["root_pair"] = root_pair_audit()
        report["general_loaded"] = general_loaded_audit()
        report["outcome"] = "PASS"
        exit_code = 0
    except Broken as error:
        report["outcome"] = "FAIL"
        report["first_bad_cut"] = error.report
        exit_code = 1
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
