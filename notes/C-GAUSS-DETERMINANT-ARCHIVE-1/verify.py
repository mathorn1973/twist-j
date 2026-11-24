#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact notes audit; not a formal Canon gate. Read PREREG.md first."""
import hashlib
import itertools
import json

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
T = 2**35
CHECKS = 0


def require(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError("exact certificate mismatch")


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def scale(a, n):
    return tuple(n*x for x in a)


def total(items):
    out = ZERO
    for a in items:
        out = add(out, a)
    return out


def mul(a, b):
    c = [0]*7
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            c[i+k] += x*y
    for k in range(6, 3, -1):
        for d in range(1, 5):
            c[k-d] -= c[k]
        c[k] = 0
    return tuple(c[:4])


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


def conjugate(a):
    return total(scale(power(JROOT, (-k) % 5), x)
                 for k, x in enumerate(a))


def h(a):
    return mul(a, conjugate(a))


def q(a):
    numerator = 5*sum(x*x for x in a)-sum(a)**2
    require(numerator % 2 == 0)
    return numerator//2


def area_coeff(a):
    require(a[1] == 0 and a[2] == a[3])
    return [a[0], -a[2]]


def residue(a):
    return sum(a) % 5


def contact(bank, pair):
    a, b = pair
    old_a, old_b = bank[a], bank[b]
    difference = sub(old_a, old_b)
    if any(x % 2 for x in difference):
        return False, False, ZERO, ZERO
    t = tuple(x//2 for x in difference)
    middle = tuple(x//2 for x in add(old_a, old_b))
    rotated = mul(RHO, t)
    bank[a], bank[b] = add(middle, rotated), sub(middle, rotated)
    return True, t != ZERO, t, sub(old_a, bank[a])


def bank_audit(bank, initial):
    require(total(bank) == total(initial))
    require(sum(q(a) for a in bank) == sum(q(a) for a in initial))
    require([residue(a) for a in bank] == [residue(a) for a in initial])


def determinant(matrix):
    # Leibniz expansion, no inferred phase/count in the actual-state readout.
    out = ZERO
    n = len(matrix)
    for perm in itertools.permutations(range(n)):
        sign = (-1)**sum(perm[a] > perm[b]
                        for a in range(n) for b in range(a+1, n))
        term = ONE
        for row, column in enumerate(perm):
            term = mul(term, matrix[row][column])
        out = add(out, scale(term, sign))
    return out


def fingerprint(banks):
    raw = json.dumps(banks, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def pair(token):
    return int(token[0])-1, int(token[1])-1


B = sub(ONE, RHO)
U = sub(ONE, JROOT)
X = (1, 1, 0, -2)
I1 = [B, neg(B), U, U, X, (2, 0, 0, 0)]
P27 = [pair(s) for s in
       "12 12 12 12 35 36 16 16 16 16 46 46 46 46 24 "
       "36 36 36 36 16 12 12 46 45 45 45 45".split()]
P27 += [pair("13")]*8
P35 = [pair("12")]*5 + ([pair("35")]+[pair("36")]*5
                         +[pair("35")]*4)*3
WORDS = [("P27", P27, 27, power(JROOT, 4)), ("P35", P35, 35, ONE)]
EDGES = list(itertools.combinations(range(6), 2))


def divergence(field):
    out = [ZERO]*6
    for (a, b), value in zip(EDGES, field):
        out[a] = sub(out[a], value)
        out[b] = add(out[b], value)
    return out


def continuity_audit(word):
    state = I1.copy()
    background = [neg(total(I1))] + [ZERO]*5
    field = [I1[b] if a == 0 else ZERO for a, b in EDGES]
    original_field = field.copy()
    fixed_field_first_bad = None
    diagnostic_account_first_bad = None
    initial_account = sum(map(q, I1))+sum(map(q, field))
    require(divergence(field) == [add(a, b) for a, b in zip(state, background)])
    for step, edge in enumerate(word, 1):
        _, _, _, current = contact(state, edge)
        at = EDGES.index(edge)
        field[at] = add(field[at], current)
        charge = [add(a, b) for a, b in zip(state, background)]
        require(divergence(field) == charge)
        require(list(map(residue, field)) == list(map(residue, original_field)))
        bank_audit(state, I1)
        if divergence(original_field) != charge and fixed_field_first_bad is None:
            fixed_field_first_bad = step
        if sum(map(q, state))+sum(map(q, field)) != initial_account:
            if diagnostic_account_first_bad is None:
                diagnostic_account_first_bad = step
    require(state == I1)
    delta = [sub(a, b) for a, b in zip(field, original_field)]
    require(divergence(delta) == [ZERO]*6)
    terminal_account_change = sum(map(q, field))-sum(map(q, original_field))
    returned = field == original_field
    for edge in reversed(word):
        for _ in range(4):
            _, _, _, current = contact(state, edge)
            at = EDGES.index(edge)
            field[at] = add(field[at], current)
            require(divergence(field) == [add(a, b) for a, b in zip(state, background)])
            require(list(map(residue, field)) == list(map(residue, original_field)))
            bank_audit(state, I1)
    require(state == I1 and field == original_field)
    return {
        "delta_field": delta,
        "delta_field_35": delta[EDGES.index(pair("35"))],
        "field_return": returned,
        "fixed_field_first_gauss_failure": fixed_field_first_bad,
        "diagnostic_account_first_failure": diagnostic_account_first_bad,
        "diagnostic_terminal_field_account_change": terminal_account_change,
        "gauss_violations": 0,
        "cuts_forward_inverse": 175,
        "scope": "continuity-only; not the loaded energy-preserving law",
    }


def matrix_audit(word, expected_admitted, expected_phase):
    banks = [I1.copy() for _ in range(7)]
    for k in range(6):
        banks[k+1][k] = add(banks[k+1][k], scale(ONE, T))
    initial = [row.copy() for row in banks]
    account = sum(q(a) for row in banks for a in row)
    require(account == 12*T*T+23*T+301)
    base_h = ZERO
    extended_h = ZERO
    admitted = changing = 0
    # Scaled branch matrix updated independently of difference-column readout.
    reference = [[scale(ONE, T) if r == c else ZERO for c in range(6)]
                 for r in range(6)]
    for step, edge in enumerate(word, 1):
        flags = []
        for k, bank in enumerate(banks):
            accepted, moved, half, _ = contact(bank, edge)
            flags.append(accepted)
            extended_h = add(extended_h, h(half))
            if k == 0:
                admitted += accepted
                changing += moved
                base_h = add(base_h, h(half))
            bank_audit(bank, initial[k])
        require(all(flag == flags[0] for flag in flags))
        if flags[0]:
            a, b = edge
            old_a, old_b = reference[a].copy(), reference[b].copy()
            for c in range(6):
                difference = sub(old_a[c], old_b[c])
                summation = add(old_a[c], old_b[c])
                require(all(x % 2 == 0 for x in difference+summation))
                middle = tuple(x//2 for x in summation)
                half = tuple(x//2 for x in difference)
                reference[a][c] = add(middle, mul(RHO, half))
                reference[b][c] = sub(middle, mul(RHO, half))
        actual = [[sub(banks[c+1][r], banks[0][r]) for c in range(6)]
                  for r in range(6)]
        require(actual == reference)
        require(all(x % (2**(35-step)) == 0
                    for row in actual for a in row for x in a))
    require(banks[0] == I1)
    require(admitted == changing == expected_admitted)
    require(area_coeff(base_h) == [55, 20])
    require(extended_h == add(scale(base_h, 7), scale(ONE, T*T*admitted//2)))
    det = determinant(actual)
    require(det == scale(expected_phase, T**6))
    require(all(x % (T**6) == 0 for x in det))
    phase = tuple(x//(T**6) for x in det)
    returns = banks == initial
    require(returns == (expected_phase == ONE))
    digest = fingerprint(banks)
    for edge in reversed(word):
        for k in range(6, -1, -1):
            for _ in range(4):
                contact(banks[k], edge)
                bank_audit(banks[k], initial[k])
    require(banks == initial)
    return {
        "admitted": admitted,
        "state_changing": changing,
        "refused": 35-admitted,
        "source_H": area_coeff(base_h),
        "source_path_Q": 2*base_h[0]-base_h[2],
        "source_state_Q": sum(map(q, I1)),
        "extended_H": area_coeff(extended_h),
        "initial_complete_Q": account,
        "normalized_determinant": phase,
        "terminal_banks_sha256": digest,
        "all_banks_return": returns,
        "primitive_forward_inverse": [245, 980],
        "residue_account_violations": 0,
        "inverse": True,
    }


def fixed_field_pair_diagnostic():
    values = list(itertools.product((-1, 0, 1), repeat=4))
    moved = unchanged = 0
    for x in values:
        for helper in values:
            bank = [x, helper]
            contact(bank, (0, 1))
            delta_charge = sub(bank[0], x)
            gauss_residual = neg(delta_charge)
            if bank[0] == x:
                require(bank[1] == helper and gauss_residual == ZERO)
                unchanged += 1
            else:
                require(gauss_residual != ZERO)
                moved += 1
            bank_audit(bank, [x, helper])
    return {"pairs": len(values)**2, "charged_changes_forbidden_by_gauss": moved,
            "unchanged_pairs": unchanged}


def receiver_control():
    responses = []
    word = [(0, 2), (0, 1)]*5
    for r in range(5):
        root = power(JROOT, r)
        initial = [root, neg(root), (3, 4, 2, 0)]
        bank = initial.copy()
        require(sum(map(q, bank)) == 36)
        for edge in word:
            contact(bank, edge)
            bank_audit(bank, initial)
        responses.append(q(bank[2]))
        for edge in reversed(word):
            for _ in range(4):
                contact(bank, edge)
                bank_audit(bank, initial)
        require(bank == initial)
    require(responses == [32, 17, 2, 7, 27])
    return responses


def main():
    require(power(JROOT, 5) == ONE)
    require(len(P27) == len(P35) == 35)
    require(sum(map(q, I1)) == 43)
    diagonal = contact([ZERO, ZERO], (0, 1))
    refused = contact([ZERO, ONE], (0, 1))
    require(diagonal[0] and not refused[0])
    require(diagonal[3] == refused[3] == ZERO)
    a, b = add(ONE, RHO), sub(ONE, RHO)
    require(determinant([[a, b], [b, a]]) == scale(RHO, 4))
    require(determinant([[scale(ONE, 2), ZERO], [ZERO, scale(ONE, 2)]]) == scale(ONE, 4))
    results = {}
    for name, word, count, phase in WORDS:
        matrix = matrix_audit(word, count, phase)
        continuity = continuity_audit(word)
        require(continuity["delta_field_35"] == (neg(X) if name == "P27" else ZERO))
        require(continuity["field_return"] == (name == "P35"))
        results[name] = {"matrix": matrix, "continuity": continuity}
    require(results["P35"]["matrix"]["extended_H"][0]
            - results["P27"]["matrix"]["extended_H"][0] == 4*T*T)
    output = {
        "candidate": "C-GAUSS-DETERMINANT-ARCHIVE-1",
        "status": "NON-CANONICAL/L1/candidate-C finite audit",
        "primary_coupled_root_pair_target": "NOT_REALIZED",
        "direct_continuity_lift_P27": "REJECTED_FIELD_RETURN",
        "T": T,
        "words": results,
        "fixed_field_diagnostic": fixed_field_pair_diagnostic(),
        "zero_current_determinants": [RHO, ONE],
        "receiver_control": receiver_control(),
        "scope": "One architecture; exact scoped certificates, no integrated port",
    }
    output["checks"] = CHECKS
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
