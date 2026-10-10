#!/usr/bin/env python3
"""Exact conditional seven-ion pulse-word verifier; standard library only.

No apparatus or harmonic waveform is verified here. The assumed broad-force
primitive is omega**(-sigma * number_of_physical_S0_ions**2), omega**5 = 1.
All phases are integer exponents of zeta=exp(2*pi*i/20); no floating point.
The six local labels are the five code labels 0..4 and shelf a=5.

API: run_checks() returns a deterministic JSON-compatible dictionary.
CLI: python verify.py (no arguments); one JSON line, exit 0 on PASS.
The module does no work on import. It reads no data files and uses no network.
Original text/code Apache-2.0. Author: A. M. Thorn.
"""

import itertools
import json
import sys


MODULUS = 20
ION_COUNT = 7
ACTIVE = (3, 4)  # Physical ions 4 and 5, zero-based here.
SPECTATORS = (0, 1, 2, 5, 6)
AUX = 5
CODE_DIMENSION = 5 ** ION_COUNT
X_WORD = ((1, 1), (2, -1), (3, 1), (4, -1))


class VerificationError(Exception):
    """A mathematical check failed, independently of Python's assert flag."""


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def r_pi(value, other, phase_quarters):
    """R_0,other(pi,phi), phi=phase_quarters*pi/2, on a basis column.

    R|0> = -i exp(i phi)|other>; R|other> = -i exp(-i phi)|0>.
    The return is (output_label, phase_exponent_mod_20).
    """
    if value == 0:
        return other, (5 * (phase_quarters - 1)) % MODULUS
    if value == other:
        return 0, (-5 * (phase_quarters + 1)) % MODULUS
    return value, 0


def apply_x(value):
    phase = 0
    for other, quarters in X_WORD:
        value, increment = r_pi(value, other, quarters)
        phase += increment
    return value, phase % MODULUS


def pulse_word(sigma, cycles=5, global_echo=False, wrong_unhide=False):
    """Build the literal chronological word, including all physical ions.

    The broad LS operation is deliberately not restricted to the active pair.
    A global echo can move occupied spectator D levels into physical S0.
    """
    require(sigma in (-1, 1), "sigma must be -1 or +1")
    word = [("r", ion, AUX, 1) for ion in SPECTATORS]
    echo_ions = tuple(range(ION_COUNT)) if global_echo else ACTIVE
    for _ in range(cycles):
        word.append(("ls", sigma))
        for other, quarters in X_WORD:
            for ion in echo_ions:
                word.append(("r", ion, other, quarters))
    return_quarters = 1 if wrong_unhide else -1
    word.extend(("r", ion, AUX, return_quarters) for ion in SPECTATORS)
    return tuple(word)


def run_literal(word, state):
    """Direct instruction interpreter, also used for the negative fixtures."""
    values = list(state)
    phase = 0
    for instruction in word:
        kind = instruction[0]
        if kind == "r":
            _, ion, other, quarters = instruction
            values[ion], increment = r_pi(values[ion], other, quarters)
            phase += increment
        elif kind == "ls":
            # omega = zeta**4. Count S0 on ALL seven physical ions.
            count_s0 = values.count(0)
            phase -= 4 * instruction[1] * count_s0 * count_s0
        elif kind == "conditional":
            _, left, right, exponent = instruction
            phase += exponent * values[left] * values[right]
        else:
            raise VerificationError("unknown literal instruction")
    return tuple(values), phase % MODULUS


def local_history(word, ion, initial):
    """Compile one local column and its physical S0 occupation at every LS.

    This is a cache of the literal rotation word, not the desired G gate.
    Broad-force phases are composed only after these histories are checked.
    """
    value = initial
    phase = 0
    mask = 0
    loop = 0
    for instruction in word:
        if instruction[0] == "r" and instruction[1] == ion:
            _, _, other, quarters = instruction
            value, increment = r_pi(value, other, quarters)
            phase += increment
        elif instruction[0] == "ls":
            mask |= int(value == 0) << loop
            loop += 1
        elif instruction[0] == "conditional":
            raise VerificationError("conditional instruction is not local")
    require(loop == 5, "positive compiler requires five LS intervals")
    return value, phase % MODULUS, mask


def compile_positive(sigma):
    """Small verified local caches plus a 25-entry broad-force phase table."""
    word = pulse_word(sigma)
    local = tuple(
        tuple(local_history(word, ion, value) for value in range(5))
        for ion in range(ION_COUNT)
    )
    for ion in SPECTATORS:
        for value in range(5):
            # This checked property, not the desired answer, permits pair reuse.
            require(local[ion][value][2] == 0, "spectator occupies S0 at an LS")
    pair_phase = []
    for left in range(5):
        row = []
        for right in range(5):
            left_mask = local[ACTIVE[0]][left][2]
            right_mask = local[ACTIVE[1]][right][2]
            square_sum = 0
            for loop in range(5):
                count_s0 = ((left_mask >> loop) & 1) + ((right_mask >> loop) & 1)
                square_sum += count_s0 * count_s0
            row.append((-4 * sigma * square_sum) % MODULUS)
        pair_phase.append(tuple(row))
    return local, tuple(pair_phase)


def run_compiled(compiled, state):
    local, pair_phase = compiled
    output = []
    phase = pair_phase[state[ACTIVE[0]]][state[ACTIVE[1]]]
    for ion, value in enumerate(state):
        out_value, increment, _ = local[ion][value]
        output.append(out_value)
        phase += increment
    return tuple(output), phase % MODULUS


def direct_reference(state, sigma):
    """Independent arithmetic evolution of the declared broad-force model.

    No rotation engine, compiled phase table, or target G formula is called.
    The local checks separately establish the phase-exact meaning of the
    cyclic arithmetic update and of the shelf/return used here.
    """
    values = list(state)
    for ion in (0, 1, 2, 5, 6):
        if values[ion] == 0:
            values[ion] = 5
    phase_in_fifths = 0
    for _ in range(5):
        count_s0 = sum(1 for value in values if value == 0)
        phase_in_fifths -= sigma * count_s0 ** 2
        values[3] = (values[3] + 1) % 5
        values[4] = (values[4] + 1) % 5
    for ion in (0, 1, 2, 5, 6):
        if values[ion] == 5:
            values[ion] = 0
    return tuple(values), (4 * phase_in_fifths) % 20


def target_raw_phase(state, sigma):
    """The G target with the explicitly retained common LS phase.

    Five LS intervals give zeta**(-16*sigma) on equal active labels.
    G_(sigma*4*pi/5) adds zeta**(8*sigma) on unequal active labels.
    """
    unequal = state[3] != state[4]
    return (-16 * sigma + 8 * sigma * unequal) % MODULUS


def check_local_words():
    rotation_columns = 0
    for other in range(1, 6):
        for quarters in (-1, 0, 1, 2):
            outputs = []
            for value in range(6):
                out, phase = r_pi(value, other, quarters)
                back, inverse_phase = r_pi(out, other, quarters + 2)
                require(back == value and (phase + inverse_phase) % 20 == 0,
                        "rotation/adjoint column mismatch")
                outputs.append(out)
                rotation_columns += 1
            require(sorted(outputs) == list(range(6)), "rotation is not monomial unitary")
    for value in range(6):
        out, phase = apply_x(value)
        expected = (value + 1) % 5 if value < 5 else 5
        require(out == expected and phase == 0, "X5 is not the phase-exact cycle")
        current, total = value, 0
        for _ in range(5):
            current, increment = apply_x(current)
            total += increment
        require(current == value and total % 20 == 0, "X5**5 differs from identity")
        hidden, hide_phase = r_pi(value, AUX, 1)
        returned, return_phase = r_pi(hidden, AUX, -1)
        require(returned == value and (hide_phase + return_phase) % 20 == 0,
                "Vdagger V differs from identity on the six-level space")
    return rotation_columns


def negative_inputs():
    """A fixed, small witness panel, not an adaptive search over good cases."""
    zero = (0,) * ION_COUNT
    panel = [zero]
    for occupied_count in (1, 2):
        for positions in itertools.combinations(range(ION_COUNT), occupied_count):
            values = list(zero)
            for ion in positions:
                values[ion] = 1
            panel.append(tuple(values))
    return tuple(panel)


def find_negative_witness(word, sigma, panel):
    """Reject even after granting a mutant one arbitrary common scalar phase."""
    anchor = panel[0]
    anchor_output, anchor_phase = run_literal(word, anchor)
    if anchor_output != anchor:
        return {"input": list(anchor), "reason": "wrong_output_labels"}
    common_offset = (anchor_phase - target_raw_phase(anchor, sigma)) % MODULUS
    for state in panel[1:]:
        output, phase = run_literal(word, state)
        if output != state:
            return {"input": list(state), "reason": "wrong_output_labels"}
        difference = (phase - target_raw_phase(state, sigma) - common_offset) % MODULUS
        if difference:
            return {"input": list(state), "reason": "relative_phase",
                    "relative_phase_error_mod20": difference}
    raise VerificationError("negative fixture escaped the fixed witness panel")


def run_checks():
    """Run the future pinned check; no invocation is made while importing."""
    rotation_columns = check_local_words()
    panel = negative_inputs()
    branches_checked = 0
    witnesses = {}
    for sigma in (-1, 1):
        compiled = compile_positive(sigma)
        positive_word = pulse_word(sigma)
        # Independently cross-check the literal full interpreter on fixed probes.
        for state in panel:
            require(run_literal(positive_word, state) == direct_reference(state, sigma),
                    "literal pulse word disagrees with direct reference")
        for state in itertools.product(range(5), repeat=7):
            actual = run_compiled(compiled, state)
            reference = direct_reference(state, sigma)
            require(actual == reference, "compiled word disagrees with direct reference")
            require(actual == (state, target_raw_phase(state, sigma)),
                    "full code-space G column or its retained phase is wrong")
            branches_checked += 1
        mutants = {
            "wrong_angle": pulse_word(-sigma),
            "wrong_unhide": pulse_word(sigma, wrong_unhide=True),
            "missing_cycle": pulse_word(sigma, cycles=4),
            "global_echo": pulse_word(sigma, global_echo=True),
            "active_spectator_phase": positive_word + (("conditional", 0, 3, 4),),
            "spectator_spectator_phase": positive_word + (("conditional", 0, 1, 4),),
        }
        for name, word in mutants.items():
            witnesses.setdefault(name, {})[str(sigma)] = find_negative_witness(word, sigma, panel)
    require(branches_checked == 2 * CODE_DIMENSION, "incomplete branch coverage")
    return {
        "status": "PASS",
        "scope": "conditional_ideal_seven_ion_pulse_word",
        "phase_modulus": MODULUS,
        "local_levels": 6,
        "code_dimension": CODE_DIMENSION,
        "signs": [-1, 1],
        "branches_checked": branches_checked,
        "rotation_adjoint_columns": rotation_columns,
        "x5_and_x5_fifth_power": True,
        "shelf_adjoint_six_levels": True,
        "literal_and_direct_reference": True,
        "raw_global_phase_mod20": {"-1": 16, "1": 4},
        "negative_families": len(witnesses),
        "negative_sign_cases": 2 * len(witnesses),
        "negative_witnesses": witnesses,
    }


def main():
    if len(sys.argv) != 1:
        result = {"status": "FAIL", "error": "usage: python verify.py"}
        exit_code = 2
    else:
        try:
            result = run_checks()
            exit_code = 0
        except VerificationError as error:
            result = {"status": "FAIL", "error": str(error)}
            exit_code = 1
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=True))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
