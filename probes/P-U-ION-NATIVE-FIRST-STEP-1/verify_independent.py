#!/usr/bin/env python3
"""Independent exact audit; neither import nor execute before the public pin.

The arithmetic uses the radical tower Q(r,t,i), r^2=2, t^2=2+r,
with r=sqrt(2)>0 and t=sqrt(2+sqrt(2))>0. No floating point, primary
implementation, physical calibration, oscillator cutoff simulation or
numerical integration is used. Global-LS scalar phases are factored only
by the symbolic counting identities checked below. The physical premises
and the continuous-mode derivation remain those of the frozen model.
"""

from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
import json
import sys


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def field(*coefficients):
    require(len(coefficients) == 8, "radical field coefficient count")
    return tuple(F(value) for value in coefficients)


# Basis: 1,r,t,rt,i,ir,it,irt. This is not a cyclotomic-polynomial compiler.
ZERO = field(0, 0, 0, 0, 0, 0, 0, 0)
ONE = field(1, 0, 0, 0, 0, 0, 0, 0)
IMAG = field(0, 0, 0, 0, 1, 0, 0, 0)
ROOT_TWO = field(0, 1, 0, 0, 0, 0, 0, 0)
ROOT_T = field(0, 0, 1, 0, 0, 0, 0, 0)
COS_EIGHTH = field(0, 0, F(1, 2), 0, 0, 0, 0, 0)
SIN_EIGHTH = field(0, 0, F(-1, 2), F(1, 2), 0, 0, 0, 0)
HALF_ROOT = field(0, F(1, 2), 0, 0, 0, 0, 0, 0)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def qmul(x, y):
    a, b = x
    c, d = y
    return a*c + 2*b*d, a*d + b*c


def qadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def real_mul(x, y):
    a, b = x[:2], x[2:]
    c, d = y[:2], y[2:]
    low = qadd(qmul(a, c), qmul(qmul(b, d), (F(2), F(1))))
    high = qadd(qmul(a, d), qmul(b, c))
    return low + high


def mul(x, y):
    if x == ZERO or y == ZERO:
        return ZERO
    if x == ONE:
        return y
    if y == ONE:
        return x
    ac, bd = real_mul(x[:4], y[:4]), real_mul(x[4:], y[4:])
    ad, bc = real_mul(x[:4], y[4:]), real_mul(x[4:], y[:4])
    return tuple(a - b for a, b in zip(ac, bd)) + tuple(a + b for a, b in zip(ad, bc))


def conjugate(x):
    return x[:4] + tuple(-a for a in x[4:])


def accumulate(state, key, value):
    combined = add(state.get(key, ZERO), value)
    if combined == ZERO:
        state.pop(key, None)
    else:
        state[key] = combined


@lru_cache(maxsize=None)
def rotation_columns(j, angle, phase):
    """Physical 0-j pulse: positive angle in pi/4 units, phase in pi/2 units."""
    require(j in (1, 2, 3, 4), "not an admitted star edge")
    require(angle in (1, 2, 4, 8), "undeclared carrier area")
    cosine, sine = {
        1: (COS_EIGHTH, SIN_EIGHTH),
        2: (HALF_ROOT, HALF_ROOT),
        4: (ZERO, ONE),
        8: (neg(ONE), ZERO),
    }[angle]
    phase_value = (ONE, IMAG, neg(ONE), neg(IMAG))[phase % 4]
    columns = [{level: ONE} for level in range(5)]
    columns[0] = {}
    columns[j] = {}
    if cosine != ZERO:
        columns[0][0] = cosine
        columns[j][j] = cosine
    if sine != ZERO:
        minus_i_sine = mul(neg(IMAG), sine)
        columns[0][j] = mul(minus_i_sine, phase_value)
        columns[j][0] = mul(minus_i_sine, conjugate(phase_value))
    return tuple(tuple(sorted(column.items())) for column in columns)


def dagger_columns(columns):
    result = [{} for _ in columns]
    for source, column in enumerate(columns):
        for destination, amplitude in column:
            result[destination][source] = conjugate(amplitude)
    return tuple(tuple(sorted(column.items())) for column in result)


def apply_columns(columns, state):
    result = {}
    for source, amplitude in state.items():
        for destination, entry in columns[source]:
            accumulate(result, destination, mul(entry, amplitude))
    return result


def inverse_star_word(word):
    return [(j, angle, (phase + 2) % 4) for j, angle, phase in reversed(word)]


def local_word_columns(word):
    result = []
    for source in range(5):
        state = {source: ONE}
        for pulse in word:
            state = apply_columns(rotation_columns(*pulse), state)
        result.append(tuple(sorted(state.items())))
    return tuple(result)


def transposition_word(a, b):
    require(a != b, "empty output transposition")
    if a == 0:
        return [(b, 4, 0)]
    if b == 0:
        return [(a, 4, 0)]
    return [(a, 4, 0), (b, 4, 0), (a, 4, 0)]


@lru_cache(maxsize=None)
def permutation_word(permutation):
    """Greedy output-label correction, independently of a cycle compiler."""
    require(sorted(permutation) == list(range(5)), "not a five-label permutation")
    current = list(range(5))
    word = []
    for source in range(5):
        if current[source] != permutation[source]:
            old, new = current[source], permutation[source]
            word.extend(transposition_word(old, new))
            current = [new if value == old else old if value == new else value
                       for value in current]
    require(current == list(permutation), "permutation compiler labels")
    columns = local_word_columns(word)
    for source, column in enumerate(columns):
        require(len(column) == 1 and column[0][0] == permutation[source],
                "physical permutation support")
        amplitude = column[0][1]
        require(mul(conjugate(amplitude), amplitude) == ONE, "monomial phase")
    require(local_word_columns(inverse_star_word(word)) == dagger_columns(columns),
            "physical permutation inverse phases")
    return tuple(word)


def projective_directions():
    directions = []
    for vector in product(range(5), repeat=3):
        first_nonzero = next((entry for entry in vector if entry), None)
        if first_nonzero == 1:
            directions.append(vector)
    require(len(directions) == 31 and len(set(directions)) == 31,
            "projective direction count")
    return directions


def assign_directions(active):
    require(len(set(active)) == 2 and all(0 <= ion < 17 for ion in active),
            "active ion pair")
    common = (1, 0, 0)
    spectators = [v for v in projective_directions() if v != common][:15]
    spectator_index = 0
    result = []
    for ion in range(17):
        if ion in active:
            result.append(common)
        else:
            result.append(spectators[spectator_index])
            spectator_index += 1
    for i, j in combinations(range(17), 2):
        determinants = [(result[i][a]*result[j][b] - result[i][b]*result[j][a]) % 5
                        for a, b in combinations(range(3), 2)]
        if {i, j} == set(active):
            require(not any(determinants), "active directions differ")
        else:
            require(any(determinants), "spectator pair has rank below two")
    return tuple(result)


def echo_audit():
    """All 17 one-ion and all 136 pair input-frequency identities."""
    active = (6, 14)
    directions = assign_directions(active)
    frames = []
    affine_words = {}
    for a in range(1, 5):
        for b in range(5):
            p = tuple((a*x + b) % 5 for x in range(5))
            affine_words[p] = permutation_word(p)
    require(len(affine_words) == 20, "affine permutation family")
    carrier_count = 0
    for a in range(1, 5):
        for u in product(range(5), repeat=3):
            row = []
            for vector in directions:
                offset = sum(v*w for v, w in zip(vector, u)) % 5
                p = tuple((a*x + offset) % 5 for x in range(5))
                row.append(p)
                carrier_count += 2 * len(affine_words[p])
            frames.append(tuple(row))
    require(len(frames) == 500, "echo row count")
    require(carrier_count == 17*25*2*sum(len(w) for w in affine_words.values()),
            "independent echo carrier accounting")

    local_checks = 0
    pair_checks = 0
    for ion in range(17):
        for x in range(5):
            frequency = [0] * 5
            for row in frames:
                frequency[row[ion][x]] += 1
            require(frequency == [100] * 5, "one-ion scalar twirl")
            local_checks += 1
    active_equal = None
    active_unequal = None
    for i, j in combinations(range(17), 2):
        is_active = {i, j} == set(active)
        for x in range(5):
            for y in range(5):
                frequency = [0] * 25
                for row in frames:
                    frequency[5*row[i][x] + row[j][y]] += 1
                if is_active:
                    if x == y:
                        expected = [100 if r == s else 0 for r in range(5) for s in range(5)]
                        active_equal = frequency
                    else:
                        expected = [0 if r == s else 25 for r in range(5) for s in range(5)]
                        active_unequal = frequency
                else:
                    expected = [20] * 25
                require(frequency == expected, "global LS pair-profile frequency")
                pair_checks += 1

    # Collapse the difference into unordered d_r*d_s coefficients.
    # It equals 25 B; the Hamiltonian cross term then supplies 50 Re(c_i c_j*) B.
    difference = {(r, s): 0 for r in range(5) for s in range(r, 5)}
    for r in range(5):
        for s in range(5):
            difference[tuple(sorted((r, s)))] += active_equal[5*r+s] - active_unequal[5*r+s]
    require(difference == {(r, s): (100 if r == s else -50)
                           for r in range(5) for s in range(r, 5)},
            "active coefficient is not 25 B")
    require({key: 2*value for key, value in difference.items()} ==
            {(r, s): (200 if r == s else -100)
             for r in range(5) for s in range(r, 5)}, "cross coefficient is not 50 B")
    require(local_checks == 85 and pair_checks == 3400, "echo input coverage")
    return carrier_count


def mask_frame(pair, target_level):
    low, high = sorted(pair)
    require(low != high and target_level in (1, 2, 3, 4), "mask frame arguments")
    mapping = [None] * 5
    mapping[low], mapping[high] = 0, target_level
    sources = [label for label in range(5) if label not in pair]
    outputs = [label for label in range(5) if label not in (0, target_level)]
    for source, output in zip(sources, outputs):
        mapping[source] = output
    return permutation_word(tuple(mapping))


def crot_word(j, k):
    require(j in range(5) and k in (1, 2, 3, 4), "CROT labels")
    b, c = [value for value in range(5) if value != j][:2]
    word = []
    for pair, beta_sign in (((j, b), 1), ((j, c), 1), ((b, c), -1)):
        frame = mask_frame(pair, k)
        word.extend(("R", 0, *pulse) for pulse in frame)
        word.extend((("G",), ("G",)))
        word.append(("R", 1, k, 1, (-beta_sign) % 4))
        word.extend((("G",), ("G",)))
        word.append(("R", 1, k, 1, beta_sign % 4))
        word.extend(("R", 0, *pulse) for pulse in inverse_star_word(frame))
    return tuple(word)


def apply_pair_pulse(state, role, pulse):
    result = {}
    columns = rotation_columns(*pulse)
    for source, amplitude in state.items():
        control, target = divmod(source, 5)
        label = control if role == 0 else target
        for output, entry in columns[label]:
            destination = 5*output + target if role == 0 else 5*control + output
            accumulate(result, destination, mul(entry, amplitude))
    return result


def compiled_crot(j, k, g_sign, omit_ls=False):
    require(g_sign in (-1, 1), "signed echo convention")
    # g_sign is sign(Re(c_i*conjugate(c_j))); G has exp(-i*g_sign*pi/2) on E.
    echo_equal = neg(IMAG) if g_sign == 1 else IMAG
    # Both physical signs give the same exact Z=G^2=I-2E.
    require(mul(echo_equal, echo_equal) == neg(ONE), "signed G square")
    columns = []
    for source in range(25):
        state = {source: ONE}
        for token in crot_word(j, k):
            if token[0] == "G":
                if not omit_ls:
                    state = {index: mul(amplitude, echo_equal) if index // 5 == index % 5 else amplitude
                             for index, amplitude in state.items()}
            else:
                _, role, level, angle, phase = token
                state = apply_pair_pulse(state, role, (level, angle, phase))
        columns.append(tuple(sorted(state.items())))
    return tuple(columns)


TARGET_R1 = (
    (0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 4, 0),
    (2, 1, 2, 1, 4, 0),
    (2, 1, 3, 4, 3, 1),
    (2, 1, 3, 4, 3, 1),
)


def native_branch(index, state):
    p1, p4, p1p, p4p, q, r = state
    maps = (
        (p4, p1, p4p, p1p, q, r),
        (-p1p, -p4p, -p1, -p4, -q, -r),
        (2-p1p, 1-p4p+r, 2-p1, 1-p4-r, 1-q, -r),
        (2-p1, 1-p4, 3-p1p, 4-p4p, 1-q, 1-r),
        (2-p1, 1-p4, 3-p1p, 4-p4p, 2-q, 1-r),
    )
    return tuple(value % 5 for value in maps[index])


def physical_input(s, t):
    return (1, t, 0, 0, 0, 0, s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def native_target(s, t):
    start = physical_input(s, t)
    r1 = start[2:8]
    j1 = sum(r1) % 5
    r2_logical = list(start[8:14])
    r2_logical[4] = (r2_logical[4] + 1) % 5
    j2 = sum(r2_logical) % 5
    r2_output = list(native_branch(j2, r2_logical))
    r2_output[4] = (r2_output[4] - 1) % 5
    return (start[0], start[1], *native_branch(j1, r1), *r2_output, j1, j2, 1)


def program():
    operations = []
    for k in range(1, 5):
        operations.append(("C", 6, 14, k, k))
        operations.append(("C", 14, 6, k, k))
    for s in range(1, 5):
        for coordinate, value in enumerate(TARGET_R1[s], start=2):
            if value:
                operations.append(("C", 14, coordinate, s, value))
    operations.extend(("R", 14, j, 8, 0) for j in range(1, 5))
    operations.extend((("R", 12, 3, 4, 1), ("R", 15, 1, 4, 1), ("R", 16, 1, 4, 1)))
    return tuple(operations)


def apply_global_pair(state, control, target, columns):
    require(control != target, "identical CROT factors")
    result = {}
    for labels, amplitude in state.items():
        source = 5*labels[control] + labels[target]
        for destination, entry in columns[source]:
            output = list(labels)
            output[control], output[target] = divmod(destination, 5)
            accumulate(result, tuple(output), mul(entry, amplitude))
    return result


def apply_global_local(state, ion, columns):
    result = {}
    for labels, amplitude in state.items():
        for destination, entry in columns[labels[ion]]:
            output = list(labels)
            output[ion] = destination
            accumulate(result, tuple(output), mul(entry, amplitude))
    return result


def run_program(state, operations, crot_matrices, inverse=False):
    for token in reversed(operations) if inverse else operations:
        if token[0] == "C":
            _, control, target, j, k = token
            columns = crot_matrices[j, k]
            state = apply_global_pair(state, control, target,
                                      dagger_columns(columns) if inverse else columns)
        else:
            _, ion, j, angle, phase = token
            columns = rotation_columns(j, angle, phase)
            state = apply_global_local(state, ion,
                                       dagger_columns(columns) if inverse else columns)
    return state


def audit():
    require(mul(ROOT_TWO, ROOT_TWO) == field(2, 0, 0, 0, 0, 0, 0, 0), "r squared")
    require(mul(ROOT_T, ROOT_T) == field(2, 1, 0, 0, 0, 0, 0, 0), "t squared")
    require(mul(IMAG, IMAG) == neg(ONE), "i squared")
    require(add(mul(COS_EIGHTH, COS_EIGHTH), mul(SIN_EIGHTH, SIN_EIGHTH)) == ONE,
            "pi/8 normalization")
    for j in range(1, 5):
        for angle in (1, 2, 4, 8):
            for phase in range(4):
                columns = rotation_columns(j, angle, phase)
                require(rotation_columns(j, angle, (phase + 2) % 4) == dagger_columns(columns),
                        "positive-time carrier inverse")
                for source in range(5):
                    require(apply_columns(dagger_columns(columns),
                                          apply_columns(columns, {source: ONE})) == {source: ONE},
                            "carrier unitarity")

    echo_carriers = echo_audit()
    crot_matrices = {}
    omitted_matrices = {}
    for j in range(5):
        for k in range(1, 5):
            physical_word = crot_word(j, k)
            require(sum(token[0] == "G" for token in physical_word) == 12,
                    "CROT echo count")
            plus = compiled_crot(j, k, 1)
            minus = compiled_crot(j, k, -1)
            require(plus == minus, "CROT depends on the physical G sign")
            for source, column in enumerate(plus):
                control, target = divmod(source, 5)
                if control == j and target == 0:
                    expected = {5*control + k: ONE}
                elif control == j and target == k:
                    expected = {5*control: neg(ONE)}
                else:
                    expected = {source: ONE}
                require(dict(column) == expected, "complete CROT phase or spectator action")
                require(apply_columns(dagger_columns(plus), dict(column)) == {source: ONE},
                        "CROT algebraic inverse")
            crot_matrices[j, k] = plus
            omitted_matrices[j, k] = compiled_crot(j, k, 1, omit_ls=True)

    operations = program()
    controlled = [token for token in operations if token[0] == "C"]
    fixed = [token for token in operations if token[0] == "R"]
    require(len(controlled) == 26 and len(fixed) == 7, "first-step operation count")
    for s in range(5):
        require(native_branch(s, (0, 0, 0, 0, s, 0)) == TARGET_R1[s],
                "preparation table differs from current-state native law")
    # Every actual interaction pair uses the same proven direction construction.
    for active in {tuple(sorted((token[1], token[2]))) for token in controlled}:
        assigned = assign_directions(active)
        require(sorted(assigned) == sorted(assign_directions((6, 14))),
                "an actual pair changed the global direction multiset")

    omitted_success = 0
    for s in range(5):
        for t in range(5):
            initial = {physical_input(s, t): ONE}
            expected = {native_target(s, t): ONE}
            actual = run_program(initial, operations, crot_matrices)
            require(actual == expected, "complete coherent first-step column")
            require(run_program(actual, operations, crot_matrices, inverse=True) == initial,
                    "complete first-step algebraic inverse")
            for output in actual:
                require(output[0] == 1 and output[1] == t and output[14:] == (s, 1, 1),
                        "source, history or finite-counter output")
            omitted = run_program(initial, operations, omitted_matrices)
            target_probability = mul(conjugate(omitted.get(native_target(s, t), ZERO)),
                                     omitted.get(native_target(s, t), ZERO))
            require(target_probability in (ZERO, ONE), "omitted-LS control is not deterministic")
            omitted_success += target_probability == ONE
    require(omitted_success == 5, "omitted global LS control differs from the frozen five successes")

    echo_count = sum(sum(token[0] == "G" for token in crot_word(item[3], item[4]))
                     for item in controlled)
    exterior = [token for item in controlled for token in crot_word(item[3], item[4])
                if token[0] == "R"]
    require(echo_count == 312 and 500*echo_count == 156000, "global LS loop count")
    independent_carriers = echo_count*echo_carriers + len(exterior) + len(fixed)
    independent_angle_pi = F(echo_count*echo_carriers)
    independent_angle_pi += sum((F(token[3], 4) for token in exterior), F(0))
    independent_angle_pi += sum((F(token[3], 4) for token in fixed), F(0))
    require(independent_carriers - independent_angle_pi == 113,
            "independent pulse area accounting")
    return {
        "status": "PASS",
        "arithmetic": "Q(sqrt(2),sqrt(2+sqrt(2)),i); exact Fraction tower",
        "actual_inputs": 25,
        "crot_columns": 500,
        "g_signs_checked": 2,
        "echo_rows": 500,
        "echo_local_inputs": 85,
        "echo_pair_inputs": 3400,
        "projective_directions": 31,
        "ions": 17,
        "crot_count": 26,
        "ls_loops": 156000,
        "independent_echo_carriers": echo_carriers,
        "independent_program_carriers": independent_carriers,
        "independent_program_angle_pi": str(independent_angle_pi),
        "compiler_counts_scope": "independent greedy implementation, not primary bound reproduction",
        "omitted_ls_success": omitted_success,
        "old_history_reset": False,
        "physical_error_bound": "NOT_PROVIDED",
    }


if __name__ == "__main__":
    sys.stdout.buffer.write((json.dumps(audit(), sort_keys=True, separators=(",", ":")) + "\n")
                            .encode("utf-8"))
