#!/usr/bin/env python3
"""Exact finite Gaussian algebra, ideal-word and complete-source audits.

PUBLIC NON-CANONICAL. This is NOT a floating waveform solver or its oracle.
Rational Gaussian displacement/area identities are checked without evaluating
any exponential, sine, cosine, square root or floating-point number. Positive
closed-loop areas below are declared analytic fixtures, not computed pulse data.
The complete-source audit tests the phase-free coherent lift of the specified
classical C and EXPOSES its informative full-source-preservation overclaim.

The ideal-word implementation below is adapted without scientific changes from
P-U-CA40-PAIR-KERNEL-1/verify.py at pin
179199a8972187edb70f576ae4af8aa9078805d2, SHA-256
a2033a585be759a7e65ae726a6a942cba00ad94ad774f231bd758c94bedcc850.
That predecessor audit is credited reuse, not a newly independent result.

No apparatus or harmonic waveform is verified here. The assumed broad-force
primitive is omega**(-sigma * number_of_physical_S0_ions**2), omega**5 = 1.
All phases are integer exponents of zeta=exp(2*pi*i/20); no floating point.
The six local labels are the five code labels 0..4 and shelf a=5.

API: run_checks() returns a deterministic JSON-compatible dictionary.
CLI: python verify.py (no arguments); one JSON line, exit 0 on PASS.
The module does no work on import. It reads no data files and uses no network.
Original text/code Apache-2.0. Author: A. M. Thorn.
"""

from fractions import Fraction
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


def check_ideal_word():
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
    payload = json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    sys.stdout.buffer.write((payload + "\n").encode("ascii"))
    return exit_code


# Gaussian quantities are exact rational pairs (real, imaginary). Phases in
# this section are unwrapped rational radians; they are NOT reduced modulo 20.
ZERO = (Fraction(0), Fraction(0))


def qcomplex(real=0, imaginary=0):
    return Fraction(real), Fraction(imaginary)


def qadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def qneg(a):
    return -a[0], -a[1]


def qnorm(a):
    return a[0] * a[0] + a[1] * a[1]


def weyl(beta, alpha):
    """Im(beta conjugate(alpha)); new displacement acts on the LEFT."""
    return beta[1] * alpha[0] - beta[0] * alpha[1]


def chronological(segments):
    alpha, phase = ZERO, Fraction(0)
    for beta, local_phase in segments:
        phase += local_phase + weyl(beta, alpha)
        alpha = qadd(alpha, beta)
    return alpha, phase


def direct_pair_sum(segments):
    """Independent nonrecursive bilinear expansion, with literal coordinates."""
    real = sum((item[0][0] for item in segments), Fraction(0))
    imaginary = sum((item[0][1] for item in segments), Fraction(0))
    phase = sum((item[1] for item in segments), Fraction(0))
    for later in range(len(segments)):
        for earlier in range(later):
            br, bi = segments[later][0]
            ar, ai = segments[earlier][0]
            phase += bi * ar - br * ai
    return (real, imaginary), phase


def thermal_exponents(left, right, nu):
    """Return (damping, phase) for exp(-damping+i*phase), without exp()."""
    a, phi = left
    b, psi = right
    delta = qadd(a, qneg(b))
    return nu * qnorm(delta), phi - psi + weyl(a, b)


def encoded_fraction(value):
    return [value.numerator, value.denominator]


def check_gaussian_algebra():
    # This fixed grid contains nonzero intrinsic phases as well as displacements.
    alphabet = (
        (qcomplex(0, 0), Fraction(0)),
        (qcomplex(1, 0), Fraction(1, 8)),
        (qcomplex(0, 1), Fraction(-3, 8)),
        (qcomplex(-1, 0), Fraction(1, 3)),
        (qcomplex(0, -1), Fraction(-1, 3)),
        (qcomplex(Fraction(1, 2), Fraction(-1, 3)), Fraction(2, 7)),
    )
    count = 0
    for length in range(1, 5):
        for segments in itertools.product(alphabet, repeat=length):
            require(chronological(segments) == direct_pair_sum(segments),
                    "chronological Weyl composition differs from pair sum")
            inverse = tuple((qneg(beta), -phase)
                            for beta, phase in reversed(segments))
            require(chronological(segments + inverse) == (ZERO, 0),
                    "complete chronological inverse failed")
            count += 1
    square = tuple((qcomplex(*p), Fraction(0))
                   for p in ((1, 0), (0, 1), (-1, 0), (0, -1)))
    require(chronological(square) == (ZERO, 2), "oriented square area")
    reverse = tuple(reversed(square))
    require(chronological(reverse) == (ZERO, -2), "orientation reversal")
    negated = tuple((qneg(beta), phase) for beta, phase in square)
    require(chronological(negated) == (ZERO, 2),
            "force-sign inversion must not reverse geometric area")
    # Negative controls expose three mistakes even though a closed loop has alpha=0.
    require(sum((p for _, p in square), Fraction(0)) != chronological(square)[1],
            "resetting displacement between segments escaped")
    require(direct_pair_sum(square)[1] != -chronological(square)[1],
            "wrong Weyl sign escaped")
    perturbed = square[:-1] + ((qcomplex(Fraction(1, 8), -1), Fraction(0)),)
    require(chronological(perturbed)[0] != ZERO, "closure perturbation escaped")
    a = (qcomplex(Fraction(1, 4), Fraction(1, 2)), Fraction(1, 8))
    b = (qcomplex(Fraction(-1, 2), Fraction(1, 4)), Fraction(-3, 8))
    require(thermal_exponents(a, b, Fraction(3, 2)) ==
            (Fraction(15, 16), Fraction(3, 16)), "thermal Weyl sign fixture")
    for left in (a, b, (ZERO, Fraction(0))):
        require(thermal_exponents(left, left, Fraction(3, 2)) == (0, 0),
                "diagonal thermal overlap is not one")
        for right in (a, b, (ZERO, Fraction(0))):
            damping, phase = thermal_exponents(left, right, Fraction(3, 2))
            reverse_damping, reverse_phase = thermal_exponents(right, left, Fraction(3, 2))
            require(damping >= 0 and damping == reverse_damping and phase == -reverse_phase,
                    "thermal exponent hermiticity or positivity")
    require(qnorm(a[0]) > 0 and thermal_exponents(a, a, Fraction(3, 2)) == (0, 0),
            "common displacement versus spin coherence distinction")
    # Composition, not an independent reset, retains memory across intervals.
    first = chronological(square[:2])
    second = chronological(square[2:])
    concatenated = chronological(((first[0], first[1]), (second[0], second[1])))
    require(concatenated == chronological(square), "block composition lost memory")
    return {
        "arithmetic": "rational_complex_and_unwrapped_rational_phase",
        "sequence_fixtures": count,
        "inverse_fixtures": count,
        "square_area": 2,
        "reversed_area": -2,
        "globally_negated_force_area": 2,
        "thermal_fixture_damping": [15, 16],
        "thermal_fixture_phase": [3, 16],
        "negative_controls_exposed": ["reset_between_segments", "wrong_weyl_sign",
                                      "nonclosed_perturbation", "sign_flip_is_not_orientation_flip"],
    }


def indicator_product(left, right):
    """Exact function algebra: e_(i,a)e_(i,b)=delta_ab e_(i,a), a,b!=0."""
    if left is None and right is None:
        return ()
    if left is None:
        return (right,)
    if right is None:
        return (left,)
    if left[0] == right[0]:
        return (left,) if left == right else None
    return tuple(sorted((left, right)))


def add_polynomial(target, key, value):
    if key is not None and value:
        target[key] = target.get(key, Fraction(0)) + value
        if not target[key]:
            del target[key]


def resonant_drive_fixture(orientation):
    """One common rational drive: delta=0, segment length=1, f=i*beta.

    Four constant-force segments, seven independent modes, with an affine
    force on the 28 nonzero-level indicators of the SAME seven-ion label.
    Local segment area is exactly zero. All area comes from chronology.
    Conjugating the displacements reverses the geometric orientation.
    """
    variables = (None,) + tuple((ion, level) for ion in range(7) for level in range(1, 5))
    modes = []
    for mode in range(7):
        segments = []
        for step in range(4):
            affine = {}
            for index, variable in enumerate(variables):
                real = Fraction(((mode + 2) * (step + 1) + 3 * index + step * index) % 7 - 3, 16)
                imaginary = orientation * Fraction(((mode + 1) * (step + 3) + 2 * index + mode * index) % 9 - 4, 32)
                affine[variable] = real, imaginary
            segments.append(affine)
        modes.append(tuple(segments))
    return variables, tuple(modes)


def expand_drive_chronologically(variables, modes):
    displacements, polynomial = [], {}
    for segments in modes:
        accumulated = {variable: ZERO for variable in variables}
        for beta in segments:
            for left, b in beta.items():
                for right, a in accumulated.items():
                    add_polynomial(polynomial, indicator_product(left, right), weyl(b, a))
            accumulated = {variable: qadd(accumulated[variable], beta[variable]) for variable in variables}
        displacements.append(accumulated)
    return tuple(displacements), polynomial


def expand_drive_pairwise(variables, modes):
    """Nonrecursive formal coefficient contraction, not a call to the composer."""
    displacements, polynomial = [], {}
    for segments in modes:
        displacements.append({variable: (
            sum((segment[variable][0] for segment in segments), Fraction(0)),
            sum((segment[variable][1] for segment in segments), Fraction(0)))
            for variable in variables})
        for later in range(1, len(segments)):
            for earlier in range(later):
                for left in variables:
                    for right in variables:
                        br, bi = segments[later][left]
                        ar, ai = segments[earlier][right]
                        add_polynomial(polynomial, indicator_product(left, right), bi * ar - br * ai)
    return tuple(displacements), polynomial


def direct_drive_branch(modes, labels):
    """Evaluate the actual four-segment chronology, without polynomial tables."""
    alphas, phase = [], Fraction(0)
    for segments in modes:
        word = []
        for segment in segments:
            beta = segment[None]
            for ion, label in enumerate(labels):
                if label:
                    beta = qadd(beta, segment[(ion, label)])
            word.append((beta, Fraction(0)))
        alpha, area = chronological(tuple(word))
        alphas.append(alpha)
        phase += area
    return tuple(alphas), phase


def check_resonant_drive_coefficients():
    anchor_checks = displacement_checks = 0
    polynomials = []
    for orientation in (-1, 1):
        variables, modes = resonant_drive_fixture(orientation)
        expanded = expand_drive_chronologically(variables, modes)
        require(expanded == expand_drive_pairwise(variables, modes),
                "formal drive coefficients disagree with time-pair contraction")
        displacements, polynomial = expanded
        require(polynomial, "rational drive fixture must have nonzero geometric phase")
        polynomials.append(polynomial)
        zero = (0,) * 7
        common_alpha, common_phase = direct_drive_branch(modes, zero)
        require(common_phase == polynomial.get((), 0), "drive common phase")
        anchor_checks += 1
        singles = {}
        for variable in variables[1:]:
            ion, level = variable
            labels = list(zero)
            labels[ion] = level
            alpha, phase = direct_drive_branch(modes, tuple(labels))
            singles[variable] = phase - common_phase
            require(singles[variable] == polynomial.get((variable,), 0), "drive unary phase")
            anchor_checks += 1
            for mode in range(7):
                difference = qadd(alpha[mode], qneg(common_alpha[mode]))
                require(difference == displacements[mode][variable], "drive additive alpha coefficient")
                displacement_checks += 1
        for left_index, left in enumerate(variables[1:]):
            for right in variables[1:][left_index + 1:]:
                if left[0] == right[0]:
                    continue
                labels = list(zero)
                labels[left[0]], labels[right[0]] = left[1], right[1]
                _, phase = direct_drive_branch(modes, tuple(labels))
                extracted = phase - common_phase - singles[left] - singles[right]
                require(extracted == polynomial.get(tuple(sorted((left, right))), 0),
                        "drive pair phase anchor extraction")
                anchor_checks += 1
        for mode in range(7):
            require(common_alpha[mode] == displacements[mode][None], "drive common alpha")
            displacement_checks += 1
    # Displacement conjugation reverses every area coefficient, including common.
    require(polynomials[0] == {key: -value for key, value in polynomials[1].items()},
            "orientation failed to reverse the complete phase polynomial")
    return {
        "scope": "exact_resonant_piecewise_constant_drive_fixture",
        "modes": 7, "segments": 4, "levels_per_ion": 5, "ions": 7,
        "orientations": [-1, 1], "indicator_variables": 28,
        "common_unary_pair_basis_size": 365,
        "anchor_phase_checks": anchor_checks,
        "complex_displacement_coefficient_checks": displacement_checks,
        "formal_identity_domain_cardinality": 78125,
        "nominal_target_angle_realization_claimed": False,
        "floating_waveform_integration_claimed": False,
    }


def check_positive_loop_coefficients():
    """Exact coefficient consequence of DECLARED closed-loop areas chi=k*pi/5.

    Eta is the relative sign of the active forces. A closed interval gives
    chi*(n4+eta*n5)^2. Five phase-exact X5 cycles give an equal-column phase
    chi*(1+eta)^2 and unequal-minus-equal phase -2*eta*chi.
    This does not establish that an arbitrary multimode drive closes.
    """
    checked = 0
    contracts = []
    for eta in (-1, 1):
        for sigma in (-1, 1):
            k = 2 if eta * sigma == -1 else 3
            local, _ = compile_positive(sigma)
            common = (2 * k * (1 + eta) ** 2) % MODULUS
            require((-4 * eta * k - 8 * sigma) % MODULUS == 0,
                    "positive area is assigned to the wrong target sign")
            for state in itertools.product(range(5), repeat=7):
                phase, output = 0, []
                left_mask = local[3][state[3]][2]
                right_mask = local[4][state[4]][2]
                for loop in range(5):
                    signed_occupation = ((left_mask >> loop) & 1) + eta * ((right_mask >> loop) & 1)
                    phase += 2 * k * signed_occupation ** 2
                for ion, value in enumerate(state):
                    out, increment, mask = local[ion][value]
                    if ion in SPECTATORS:
                        require(mask == 0, "positive-loop spectator force is nonzero")
                    output.append(out)
                    phase += increment
                # Independent scalar formula for the five-cycle count.
                square_sum = (1 + eta) ** 2 if state[3] == state[4] else 2
                target = (common + 8 * sigma * (state[3] != state[4])) % MODULUS
                require(tuple(output) == state and phase % MODULUS == target and
                        phase % MODULUS == (2 * k * square_sum) % MODULUS,
                        "positive closed-loop ideal coefficient identity failed")
                checked += 1
            contracts.append({"relative_force_sign": eta, "target_sign": sigma,
                              "chi_pi_over_5": k, "global_phase_mod20": common})
    return {"branches_checked": checked, "contracts": contracts,
            "scope": "exact_consequence_of_declared_closed_loop_areas"}


def contact(state, inverse=False):
    """Centered seven-label C; any appended reference/archive label is untouched."""
    values = list(state)
    x, u, y, w, q, r, s = state[:7]
    kick = (2 * (y - x) * s) % 5
    if inverse:
        kick = -kick
    values[1], values[3] = (u - kick) % 5, (w + kick) % 5
    return tuple(values)


def shift(state, position, amount=1):
    values = list(state)
    values[position] = (values[position] + amount) % 5
    return tuple(values)


def uniform_reduction(orthogonal_terms, keep):
    """Reduced density of a phase-free equal coherent sum; exact 1/n entries.

    Distinct complete basis terms have amplitude 1/sqrt(n). No square root
    is evaluated: pair coefficients are exactly 1/n, followed by a partial trace.
    """
    require(len(set(orthogonal_terms)) == len(orthogonal_terms), "duplicate coherent term")
    trace = tuple(i for i in range(len(orthogonal_terms[0])) if i not in keep)
    answer = {}
    weight = Fraction(1, len(orthogonal_terms))
    for left in orthogonal_terms:
        for right in orthogonal_terms:
            if tuple(left[i] for i in trace) == tuple(right[i] for i in trace):
                key = (tuple(left[i] for i in keep), tuple(right[i] for i in keep))
                answer[key] = answer.get(key, Fraction(0)) + weight
    return answer


def density_purity(density):
    return sum((weight * density.get((right, left), 0)
                for (left, right), weight in density.items()), Fraction(0))


def overlap_uniform(density, labels):
    return sum((density.get((left, right), 0) for left in labels for right in labels),
               Fraction(0)) / len(labels)


def check_complete_source():
    inverse_columns, spectator_commutations = 0, 0
    source_x_not_conserved = False
    for state in itertools.product(range(5), repeat=7):
        after = contact(state)
        require(contact(after, inverse=True) == state and contact(contact(state, True)) == state,
                "complete C inverse failed")
        require(after[0] == state[0] and after[2] == state[2] and after[4:] == state[4:],
                "C changed a preserved computational coordinate")
        # X and Z generate the full q/r observable algebras. Z conservation
        # follows from unchanged q/r labels; X is checked column by column.
        for position in (4, 5):
            require(contact(shift(state, position)) == shift(after, position),
                    "q/r coherent spectator shift failed")
            spectator_commutations += 1
        heisenberg = contact(shift(after, 6), inverse=True)
        expected = list(shift(state, 6))
        expected[1] = (state[1] + 2 * (state[2] - state[0])) % 5
        expected[3] = (state[3] - 2 * (state[2] - state[0])) % 5
        require(heisenberg == tuple(expected), "Udagger X_source U sign is wrong")
        source_x_not_conserved |= heisenberg != shift(state, 6)
        inverse_columns += 1
    require(source_x_not_conserved, "informative C incorrectly conserves source X")

    receiver_count, trivial, informative, matrix_units = 0, 0, 0, 0
    for receiver in itertools.product(range(5), repeat=6):
        outputs = tuple(contact(receiver + (s,))[:6] for s in range(5))
        nontrivial = receiver[0] != receiver[2]
        require(len(set(outputs)) == (5 if nontrivial else 1), "source record injectivity")
        for s in range(5):
            for t in range(5):
                # Tr_E |C_s(v)><C_t(v)| is their exact basis inner product.
                gamma = int(outputs[s] == outputs[t])
                expected = int(s == t) if nontrivial else 1
                require(gamma == expected, "source matrix-unit Schur factor")
                matrix_units += 1
        receiver_count += 1
        informative += int(nontrivial)
        trivial += int(not nontrivial)

    receiver = (0, 0, 1, 0, 0, 0)  # h=1; neither hidden raw-coordinate shift nor postselection.
    initial = tuple(receiver + (s,) for s in range(5))
    final = tuple(contact(state) for state in initial)
    labels = tuple((s,) for s in range(5))
    source_input = uniform_reduction(initial, (6,))
    source_output = uniform_reduction(final, (6,))
    dephased = {(label, label): Fraction(1, 5) for label in labels}
    require(source_output == dephased and source_output != source_input,
            "coherent source negative control not exposed")
    require(density_purity(source_input) == 1 and density_purity(source_output) == Fraction(1, 5),
            "source purity witness")
    require(overlap_uniform(source_output, labels) == Fraction(1, 5), "source overlap witness")
    require(sum((source_input.get(((s,), ((s + 1) % 5,)), 0) for s in range(5)), Fraction(0)) == 1,
            "initial X expectation")
    require(sum((source_output.get(((s,), ((s + 1) % 5,)), 0) for s in range(5)), Fraction(0)) == 0,
            "final X expectation")
    restored = tuple(contact(state, inverse=True) for state in final)
    require(restored == initial and uniform_reduction(restored, (6,)) == source_input,
            "joint inverse must restore source while uncomputing receiver record")

    # A genuinely external reference is appended; it is never reset or acted upon.
    entangled_initial = tuple(receiver + (s, s) for s in range(5))
    entangled_final = tuple(contact(state) for state in entangled_initial)
    sr_input = uniform_reduction(entangled_initial, (6, 7))
    sr_output = uniform_reduction(entangled_final, (6, 7))
    bell_labels = tuple((s, s) for s in range(5))
    require(sr_output == {(label, label): Fraction(1, 5) for label in bell_labels} and sr_output != sr_input,
            "source/reference coherence negative control")
    require(density_purity(sr_input) == 1 and density_purity(sr_output) == Fraction(1, 5) and
            overlap_uniform(sr_output, bell_labels) == Fraction(1, 5), "reference overlap/purity")
    require(uniform_reduction(entangled_initial, (7,)) == uniform_reduction(entangled_final, (7,)),
            "untouched reference marginal changed")

    # Copying the classical label to an archive before inverse retains dephasing.
    archived = tuple(state + (state[6],) for state in final)
    undo_with_archive = tuple(contact(state, inverse=True) for state in archived)
    require(all(state[:6] == receiver and state[7] == state[6] for state in undo_with_archive),
            "archive/readout or receiver restoration fixture")
    require(uniform_reduction(undo_with_archive, (6,)) == dephased,
            "retained informative archive falsely restores unknown source coherence")

    # A coherent invariant receiver is a legal exception, but its output is not informative.
    orbit = tuple(contact(receiver + (s,))[:6] for s in range(5))
    eigen_terms = tuple(v + (s,) for v in orbit for s in range(5))
    eigen_after = tuple(contact(state) for state in eigen_terms)
    require(set(eigen_after) == set(eigen_terms), "invariant coherent receiver exception")
    require(uniform_reduction(eigen_after, (6,)) == source_input, "eigen-receiver source preservation")
    for s in range(5):
        require({contact(v + (s,))[:6] for v in orbit} == set(orbit),
                "eigen-receiver produced an informative conditional output")
    # The same orbit's diagonal mixture commutes with V but still dephases S.
    mixed_source = {}
    for v in orbit:
        reduction = uniform_reduction(tuple(contact(v + (s,)) for s in range(5)), (6,))
        for key, value in reduction.items():
            mixed_source[key] = mixed_source.get(key, Fraction(0)) + value / 5
    require(mixed_source == dephased, "commuting mixed receiver mistaken for eigen-receiver")
    return {
        "complete_C_inverse_columns": inverse_columns,
        "q_r_shift_commutations": spectator_commutations,
        "basis_receiver_preparations": receiver_count,
        "trivial_receiver_preparations": trivial,
        "informative_receiver_preparations": informative,
        "source_matrix_units": matrix_units,
        "classical_source_labels_preserved": True,
        "full_unknown_source_preserved_at_informative_basis_receiver": False,
        "source_plus_output_purity": [1, 5],
        "source_plus_output_overlap": [1, 5],
        "source_X_before_after": [1, 0],
        "source_reference_output_purity": [1, 5],
        "source_reference_output_overlap": [1, 5],
        "joint_inverse_restores_and_erases_receiver_record": True,
        "retained_archive_restoration_overclaim_exposed": True,
        "coherent_eigen_receiver_exception_noninformative": True,
        "commuting_mixed_receiver_counterexample": True,
        "scope": "phase_free_coherent_C_and_fixed_independent_receiver",
    }


def run_checks():
    return {
        "status": "PASS",
        "scope": "exact_conditional_algebra_and_source_boundary_only",
        "predecessor_ideal_word": check_ideal_word(),
        "gaussian_algebra": check_gaussian_algebra(),
        "resonant_drive_coefficients": check_resonant_drive_coefficients(),
        "positive_loop_coefficients": check_positive_loop_coefficients(),
        "complete_source": check_complete_source(),
        "waveform_numeric_execution_certified": False,
        "hardware_admission": False,
    }


if __name__ == "__main__":
    sys.exit(main())
