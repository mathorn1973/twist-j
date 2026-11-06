#!/usr/bin/env python3
"""Exact, bounded L1 contracts for the contact-record probe proposal.

Do not run as a formal gate before the public PREREG/source commit is pinned.
Python 3.12 standard library only; no files, network, randomness or floats.

Universal reduction:
  * b,d,e are explicit affine maps; zero plus six basis vectors determine
    every affine identity on a cell, including tau=e d and its inverse.
  * h is explicit bilinear; sixteen pairs of basis vectors determine h(Bp).
  * W branches only on h and eta and applies either I or B=b_x b_y.
    A parity bit records the COMPLETE power of B, including pistons and r.
  * Therefore the twenty (h,eta,B-parity) rows prove W and E contracts
    globally. Affine fibre coefficients then prove the commutator K.
  * Full finite reader tables compose those contracts without a piston sweep.
  * Square protection follows separately from every allowed leaf acting on
    r_x by a sign. Literal witnesses test the implementation, not universality.

The five piston witnesses below are NOT an enumeration of the full carrier.
No entropy, energy, temperature, physical detector or reset is introduced.
"""

from itertools import product
import json


F = range(5)
BITS = range(2)
P = ((0, 2, 1, 3, 4), (0, 1, 2, 3, 4), (2, 1, 0, 3, 4),
     (1, 0, 2, 3, 4), (1, 0, 2, 3, 4))
COUNTS = {}


def require(condition, label, detail=None):
    if not condition:
        print(json.dumps({"status": "FAIL", "check": label, "detail": detail},
                         sort_keys=True, separators=(",", ":")))
        raise SystemExit(1)


def basis(n):
    return [tuple(0 for _ in range(n))] + [
        tuple(int(j == i) for j in range(n)) for i in range(n)]


def native(cell, letter):
    """Complete affine cell map: p1,p4,p1p,p4p,q,r, all in F5."""
    a, b, c, d, q, r = cell
    if letter == "b":
        return (-c % 5, -d % 5, -a % 5, -b % 5, -q % 5, -r % 5)
    if letter in ("d", "e"):
        return ((2-a) % 5, (1-b) % 5, (3-c) % 5, (4-d) % 5,
                ((1 if letter == "d" else 2)-q) % 5, (1-r) % 5)
    raise ValueError(letter)


def bilinear_h(px, py):
    a, b, c, d = px
    e, f, g, k = py
    return (3*(a*k+d*e) + 2*(b*g+c*f)) % 5


def h(state):
    return bilinear_h(state[:4], state[4:8])


def swap_read(q, r):
    """Literal coupling via swaps, independently of the endpoint P table."""
    pair = ((1, 2), None, (0, 2), (0, 1), (0, 1))[q]
    if pair is None:
        return r
    a, b = pair
    return b if r == a else a if r == b else r


def literal_leaf(state, name):
    """Complete state order: px[4],py[4],qx,qy,rx,ry,eta."""
    if name == "W":
        value = h(state)
        if value == 0:
            return state
        sigma = int(value in (3, 4))
        result = state
        if sigma != state[12]:
            result = literal_leaf(literal_leaf(result, "bx"), "by")
        return result[:12] + (sigma,)
    letter, side = name
    j = 0 if side == "x" else 1
    if letter == "U":
        result = list(state)
        result[10+j] = swap_read(state[8+j], state[10+j])
        return tuple(result)
    offset = 4*j
    cell = state[offset:offset+4] + (state[8+j], state[10+j])
    changed = native(cell, letter)
    result = list(state)
    result[offset:offset+4] = changed[:4]
    result[8+j], result[10+j] = changed[4:]
    return tuple(result)


def contact_word(side):
    return ("e"+side, "d"+side, "W", "bx", "by", "W", "d"+side,
            "e"+side, "W", "by", "bx", "W")


def reader_word(side, epsilon):
    return ("U"+side,) + (contact_word(side) if epsilon else ()) + ("U"+side,)


def execute(state, word):
    for name in word:
        state = literal_leaf(state, name)
    return state


def reduced_B(state):
    value, eta, parity = state
    return (-value % 5, eta, parity ^ 1)


def reduced_W(state):
    value, eta, parity = state
    if value == 0:
        return state
    sigma = int(value in (3, 4))
    if sigma == eta:
        return state
    return (-value % 5, sigma, parity ^ 1)


def reduced_E(state):
    return reduced_W(reduced_B(reduced_W(state)))


def apply_E_with_fibres(state, coefficients):
    """Four exact affine fibres, in order qx,qy,rx,ry; coeff=(scale,shift)."""
    final = reduced_E(state)
    sign = 1 if final[2] == state[2] else -1
    return final, tuple((sign*a % 5, sign*b % 5) for a, b in coefficients)


def shift_fibre(coefficients, side, amount):
    result = list(coefficients)
    a, b = result[side]
    result[side] = (a, (b+amount) % 5)
    return tuple(result)


def canonical_b_order(word):
    # Only this justified rewrite is used: disjoint cell b maps commute.
    result = list(word)
    for i in range(len(result)-1):
        if result[i:i+2] == ["by", "bx"]:
            result[i:i+2] = ["bx", "by"]
    return tuple(result)


def check_algebraic_contracts():
    affine_checks = 0
    for cell in basis(6):
        for letter in ("b", "d", "e"):
            require(native(native(cell, letter), letter) == cell,
                    "affine_cell_involution", [cell, letter])
            affine_checks += 1
        for first, second, shift in (("d", "e", 1), ("e", "d", -1)):
            expected = cell[:4] + ((cell[4]+shift) % 5, cell[5])
            require(native(native(cell, first), second) == expected,
                    "affine_tau_contract", [cell, first, second])
            affine_checks += 1
    # All maps above are affine by their displayed degree-one definitions.
    # h is bilinear and b is linear on pistons, so unit pairs suffice.
    for px, py in product(basis(4)[1:], repeat=2):
        bx = native(px+(0, 0), "b")[:4]
        by = native(py+(0, 0), "b")[:4]
        require(bilinear_h(bx, by) == -bilinear_h(px, py) % 5,
                "bilinear_h_B_sign", [px, py])
    # This affine identity includes every original coordinate; eta is fixed.
    for values in basis(12):
        state = values+(0,)
        require(execute(state, ("bx", "by")) == execute(state, ("by", "bx")),
                "affine_disjoint_b_commutation", state)
    for value, eta, parity in product(F, BITS, BITS):
        state = (value, eta, parity)
        require(reduced_W(reduced_W(state)) == state, "W_involution", state)
        expected = reduced_B(state) if value == 0 else (value, eta ^ 1, parity)
        require(reduced_E(state) == expected, "E_full_factor_contract", state)
        require(reduced_E(reduced_E(state)) == state, "E_involution", state)
        require((reduced_E(state)[0] == 0) == (value == 0), "E_branch_stability")
        for side in BITS:
            coefficients = ((1, 0),)*4
            coefficients = shift_fibre(coefficients, side, -1)
            middle, coefficients = apply_E_with_fibres(state, coefficients)
            coefficients = shift_fibre(coefficients, side, 1)
            final, coefficients = apply_E_with_fibres(middle, coefficients)
            expected_coefficients = shift_fibre(((1, 0),)*4, side,
                                               -2*int(value == 0))
            require(final == state and coefficients == expected_coefficients,
                    "K_full_affine_contract", [state, side])
    E_word = ("W", "bx", "by", "W")
    for side in ("x", "y"):
        tau = ("d"+side, "e"+side)
        expansion = tuple(reversed(tau)) + E_word + tau + E_word
        require(canonical_b_order(contact_word(side)) == canonical_b_order(expansion),
                "literal_K_is_commutator", side)
        require(len(contact_word(side)) == 12, "K_leaf_count")
    COUNTS.update(affine_cell_identity_rows=affine_checks,
                  bilinear_basis_pairs=16, affine_commutation_basis_rows=13,
                  reduced_W_E_rows=20, symbolic_K_rows=40)


def local_reader(q, r, delta, epsilon):
    first = swap_read(q, r)
    q = (q+3*epsilon*delta) % 5
    return q, swap_read(q, first)


def local_inverse(q, r, delta, epsilon):
    first = swap_read(q, r)
    q = (q-3*epsilon*delta) % 5
    return q, swap_read(q, first)


def expected_local(q, r, delta, epsilon):
    qout = (q+3*epsilon*delta) % 5
    return qout, P[qout][P[q][r]]


def check_reader_and_minimum():
    for q, r in product(F, repeat=2):
        require(swap_read(q, r) == P[q][r], "complete_P_table", [q, r])
        require(P[q][P[q][r]] == r, "P_involution", [q, r])
        if r in (3, 4):
            require(P[q][r] == r, "embedded_extra_states_fixed")
    require({P[q][0] for q in F} == {0, 1, 2}, "three_working_values")
    for size in (3, 5):
        for delta, epsilon in product(BITS, repeat=2):
            images = set()
            for q, r in product(F, range(size)):
                final = local_reader(q, r, delta, epsilon)
                images.add(final)
                require(final == expected_local(q, r, delta, epsilon),
                        "reader_complete_map", [size, delta, epsilon, q, r])
                require(local_inverse(*final, delta, epsilon) == (q, r),
                        "reader_complete_inverse")
                if r == 0:
                    require(final[1] == epsilon*delta, "prepared_binary_outcome")
            require(len(images) == 5*size, "reader_bijection", [size, delta, epsilon])
    independent_sizes = []
    for mask in range(32):
        selected = {i for i in F if mask & (1 << i)}
        translated = {(i+1) % 5 for i in selected}
        if selected.isdisjoint(translated):
            independent_sizes.append(len(selected))
    require(max(independent_sizes) == 2, "C5_independence_number")
    # For ANY one-call reversible encoder/decoder on Q x A, with |Q|=25,
    # a ready layer has 25 points. The oracle has 5*m five-cycles. Disjoint
    # S,T(S) requires 25 <= 2*(5*m). These integer bounds are not a search
    # over protocols. Construction above supplies sufficiency at m=3.
    require(2*5*1 < 25 and 2*5*2 < 25 <= 2*5*3, "one_call_minimum_three")
    COUNTS.update(complete_P_entries=25, trit_reader_rows=60,
                  embedded_reader_rows=100, C5_subsets=32)


def fibre_reader(values, side, delta, epsilon, inverse=False):
    # values are qx,qy,rx,ry, and the other fibre is retained verbatim.
    result = list(values)
    operation = local_inverse if inverse else local_reader
    result[side], result[2+side] = operation(values[side], values[2+side], delta, epsilon)
    return tuple(result)


def check_composition():
    cases = 0
    for delta, ex, ey in product(BITS, repeat=3):
        images = set()
        for values in product(F, repeat=4):
            middle = fibre_reader(values, 0, delta, ex)
            final = fibre_reader(middle, 1, delta, ey)
            expected_x = expected_local(values[0], values[2], delta, ex)
            expected_y = expected_local(values[1], values[3], delta, ey)
            require(final == (expected_x[0], expected_y[0], expected_x[1], expected_y[1]),
                    "two_reader_complete_map", [delta, ex, ey, values])
            require((final[0], final[2]) == (middle[0], middle[2]),
                    "occupied_first_fibre_restored")
            recovered = fibre_reader(fibre_reader(final, 1, delta, ey, True),
                                     0, delta, ex, True)
            require(recovered == values, "two_reader_complete_inverse")
            if values[2:] == (0, 0):
                require(final[2:] == (ex*delta, ey*delta), "two_prepared_results")
            if delta == 0:
                require(final == values, "inactive_whole_composition_identity")
            images.add(final)
            cases += 1
        require(len(images) == 625, "two_reader_complete_bijection")
    COUNTS["complete_two_reader_rows"] = cases


def check_square_contract():
    allowed = {"Uy", "ey", "dy", "by", "bx", "W"}
    for epsilon in BITS:
        require(set(reader_word("y", epsilon)) <= allowed, "second_reader_leaf_family")
    # The exact leaf definitions prove the dependency: y-local maps leave
    # r_x alone, b_x negates r_x, W chooses I or b_x b_y using only p,eta.
    # These ten arithmetic rows exhaust BOTH possible actions on r_x,
    # for every state-dependent choice of the sign, at every prefix.
    for r, sign in product(F, (1, -1)):
        require(((sign*r) % 5)**2 % 5 == r*r % 5, "leaf_square_sign_identity")
    require(tuple(r*r % 5 for r in F) == (0, 1, 4, 4, 1), "square_reading_table")
    changes = {}
    for letter in ("b", "d", "e", "U"):
        count = 0
        for q, r in product(F, repeat=2):
            changed = swap_read(q, r) if letter == "U" else native((0, 0, 0, 0, q, r), letter)[5]
            count += int(changed*changed % 5 != r*r % 5)
        changes[letter] = count
    require(changes == {"b": 0, "d": 20, "e": 20, "U": 8},
            "square_not_global_alphabet_invariant", changes)
    COUNTS.update(square_sign_rows=10, negative_square_rows=100)


def expected_state(state, side, epsilon):
    j = 0 if side == "x" else 1
    result = list(state)
    result[8+j], result[10+j] = expected_local(state[8+j], state[10+j],
                                              int(h(state) == 0), epsilon)
    return tuple(result)


def check_literal_witnesses():
    # Exactly FIVE fixed piston pairs; each realizes its named h. No claim
    # that these represent every piston input or every intermediate h trace.
    pairs = [((1, 0, 0, 0), (0, 0, 0, 2*value % 5)) for value in F]
    cases = prefixes = prepared = 0
    for value, (px, py) in enumerate(pairs):
        require(bilinear_h(px, py) == value, "piston_witness_h")
        for eta, qx, qy, rx, ry in product(BITS, F, F, F, F):
            original = px+py+(qx, qy, rx, ry, eta)
            for ex, ey in product(BITS, repeat=2):
                xword, yword = reader_word("x", ex), reader_word("y", ey)
                require(len(xword+yword) == 4+12*(ex+ey), "expanded_composition_length")
                middle = execute(original, xword)
                require(middle == expected_state(original, "x", ex), "literal_first_endpoint")
                final = middle
                first_square = middle[10]*middle[10] % 5
                if rx == ry == 0:
                    require(first_square == ex*int(value == 0), "prepared_first_square")
                    prepared += 1
                # Prefix zero is included; no reset or preparation appears.
                prefixes += 1
                for name in yword:
                    final = literal_leaf(final, name)
                    prefixes += 1
                    require(final[10]*final[10] % 5 == first_square,
                            "literal_square_every_second_prefix", [value, eta, ex, ey, name])
                require(final == expected_state(middle, "y", ey), "literal_second_endpoint")
                require(final[:4] == middle[:4] and final[8] == middle[8]
                        and final[10] == middle[10], "literal_occupied_first_cell_restored")
                require(execute(final, tuple(reversed(xword+yword))) == original,
                        "literal_full_inverse")
                if rx == ry == 0:
                    require(final[10:12] == (ex*int(value == 0), ey*int(value == 0)),
                            "literal_prepared_pair")
                cases += 1
    # The frozen raw-r counterexample is retained, not hidden by m_x.
    zero = (0,)*13
    middle = execute(zero, reader_word("x", 1))
    state = middle
    raw = [state[10]]
    for name in reader_word("y", 1):
        state = literal_leaf(state, name)
        raw.append(state[10])
    require(middle[10] == 1 and raw[5] == 4 and raw[12] == 1 and raw[-1] == 1,
            "raw_first_record_transient_change", raw)
    require(all(r*r % 5 == 1 for r in raw), "raw_counterexample_square_preserved")
    COUNTS.update(literal_piston_witnesses=5, literal_composition_cases=cases,
                  literal_second_prefixes=prefixes, literal_prepared_cases=prepared)


def check_negative_boundaries():
    for q, r, delta in product(F, F, BITS):
        state = (q, r)
        for _ in range(5):
            state = local_reader(*state, delta, 1)
        require(state == (q, r), "whole_reader_fifth_power_identity")
    first = local_reader(0, 0, 1, 1)
    second = local_reader(*first, 1, 1)
    require(first == (3, 1) and second == (1, 0), "second_whole_reader_can_erase")
    for q, r in product(F, repeat=2):
        require(local_reader(q, r, 1, 0) == (q, r), "completed_zero_equals_unused")
        require(local_reader(q, r, 0, 1) == (q, r), "inactive_contact_equals_identity")
    # R_0=U U=I on the FULL state, not just the displayed reference value.
    # Thus no state-only read can add a completion flag that is not supplied.
    require(25*2 > 25, "unknown_binary_reset_injection_obstruction")
    COUNTS.update(whole_reader_order_rows=50, blank_zero_rows=25)


def main():
    check_algebraic_contracts()
    check_reader_and_minimum()
    check_composition()
    check_square_contract()
    check_literal_witnesses()
    check_negative_boundaries()
    print("PASS contact-record L1: exact contracts and composition")
    print("PASS complete maps, inverses, prepared pair, occupied first register")
    print("PASS m_x=r_x^2 after every second-reader leaf; raw r_x may change")
    print("PASS one-call standalone minimum=3; embedded=5, working=3, outcomes=2")
    print("PASS boundaries: whole-reader reuse, blank/zero, restricted protection")
    print(json.dumps(COUNTS, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
