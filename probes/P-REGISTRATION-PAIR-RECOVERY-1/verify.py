"""Exact finite renewal and pair-reading audit; no empirical data or file access."""

import json
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb


NAME = "P-REGISTRATION-PAIR-RECOVERY-1"
COUNTS = {}
CENSUS = {}
FAILURES = []
FAILURE_COUNT = 0
FAILURE_CAP = 24
ZERO = Q(0)
ONE = Q(1)


def check(condition, section, case):
    global FAILURE_COUNT
    COUNTS[section] = COUNTS.get(section, 0) + 1
    if not condition:
        FAILURE_COUNT += 1
        if len(FAILURES) < FAILURE_CAP:
            FAILURES.append({"section": section, "case": case})


def json_value(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(key): json_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(item) for item in value]
    return value


def exact_tuple(values):
    if type(values) is not tuple or any(type(value) is not Q for value in values):
        raise ValueError("EXPECTED_TUPLE_OF_FRACTIONS")
    return values


def hazards(values):
    exact_tuple(values)
    if any(not ZERO <= value <= ONE for value in values):
        raise ValueError("HAZARD_OUTSIDE_UNIT_INTERVAL")
    return values


def gap_law(prefix):
    hazards(prefix)
    survival = [ONE]
    gaps = []
    for hazard in prefix:
        gaps.append(survival[-1] * hazard)
        survival.append(survival[-1] * (ONE - hazard))
    return tuple(gaps), tuple(survival)


def renewal(gaps):
    exact_tuple(gaps)
    values = [ONE]
    for n in range(1, len(gaps) + 1):
        values.append(sum((gaps[i - 1] * values[n - i]
                           for i in range(1, n + 1)), ZERO))
    return tuple(values[1:])


def inverse_gaps(values):
    exact_tuple(values)
    gaps = []
    for n, value in enumerate(values, 1):
        gaps.append(value - sum((gaps[i - 1] * values[n - i - 1]
                                 for i in range(1, n)), ZERO))
    return tuple(gaps)


def invert(values):
    """Numeric inadmissibility is a result, not an input-type exception."""
    gaps = inverse_gaps(values)
    cumulative = ZERO
    canonical = []
    readback = []
    for n, gap in enumerate(gaps, 1):
        before = ONE - cumulative
        cumulative += gap
        if gap < ZERO:
            return {"valid": False, "gaps": gaps,
                    "failure": (n, "NEGATIVE_GAP", gap, cumulative)}
        if cumulative > ONE:
            return {"valid": False, "gaps": gaps,
                    "failure": (n, "CUMULATIVE_EXCEEDS_ONE", gap, cumulative)}
        if before == ZERO:
            canonical.append(ZERO)
            readback.append("UNREACHABLE")
        else:
            canonical.append(gap / before)
            readback.append(gap / before)
    return {"valid": True, "gaps": gaps, "failure": None,
            "canonical": tuple(canonical), "readback": tuple(readback)}


def construct_from_marginals(values):
    """Independent age-state recursion, without computing gap coefficients."""
    exact_tuple(values)
    ages = (ONE,)
    chosen = []
    readback = []
    for n, target in enumerate(values, 1):
        other = sum((mass * chosen[age]
                     for age, mass in enumerate(ages[:-1])), ZERO)
        virgin = ages[-1]
        if virgin == ZERO:
            if target != other:
                return {"valid": False, "failure_index": n}
            candidate = ZERO
            readback.append("UNREACHABLE")
        else:
            candidate = (target - other) / virgin
            if not ZERO <= candidate <= ONE:
                return {"valid": False, "failure_index": n}
            readback.append(candidate)
        chosen.append(candidate)
        occurred = sum((mass * chosen[age]
                        for age, mass in enumerate(ages)), ZERO)
        ages = (occurred,) + tuple(mass * (ONE - chosen[age])
                                   for age, mass in enumerate(ages))
    return {"valid": True, "canonical": tuple(chosen),
            "readback": tuple(readback), "ages": ages}


def event_word_law(prefix):
    """Enumerate histories from time since the last event, anchored at time 0."""
    hazards(prefix)
    weights = []
    marginals = [ZERO] * len(prefix)
    first_gaps = [ZERO] * len(prefix)
    for word in product((0, 1), repeat=len(prefix)):
        weight = ONE
        age = 1
        for bit in word:
            hazard = prefix[age - 1]
            weight *= hazard if bit else ONE - hazard
            age = 1 if bit else age + 1
        weights.append((word, weight))
        first = None
        for index, bit in enumerate(word):
            if bit:
                marginals[index] += weight
                if first is None:
                    first = index
        if first is not None:
            first_gaps[first] += weight
    return tuple(weights), tuple(marginals), tuple(first_gaps)


def typed_boundaries():
    section = "TYPED_BOUNDARIES"
    check(gap_law(()) == ((), (ONE,)) and renewal(()) == (), section, "empty_forward")
    check(invert(())["valid"] and construct_from_marginals(())["valid"],
          section, "empty_inverse")
    malformed = (None, [], [Q(1, 2)], "1/2", (0,), (True,),
                 ("1/2",), (None,), (Q(1, 2), 1))
    for index, value in enumerate(malformed):
        for name, function in (("hazards", hazards), ("inverse", invert)):
            try:
                function(value)
            except ValueError:
                rejected = True
            else:
                rejected = False
            check(rejected, section, (name, index))
    for value in (Q(-2), Q(-1, 4), Q(5, 4), Q(2)):
        try:
            hazards((value,))
        except ValueError:
            rejected = True
        else:
            rejected = False
        check(rejected, section, ("outside_hazard", value))
        inverse = invert((value,))
        check(not inverse["valid"] and inverse["failure"][0] == 1,
              section, ("outside_marginal", value))
    unreachable = invert(renewal(gap_law((ONE, Q(1, 2), ONE))[0]))
    check(unreachable["readback"] == (ONE, "UNREACHABLE", "UNREACHABLE")
          and unreachable["canonical"] == (ONE, ZERO, ZERO),
          section, "unreachable_is_not_a_recovered_zero")


def hazard_census():
    section = "HAZARD_PREFIX_CENSUS"
    prefix_count = 0
    event_word_count = 0
    extension_count = 0
    for family, alphabet, maximum in (
            ("ternary", (ZERO, Q(1, 2), ONE), 6),
            ("quarters", (Q(1, 4), Q(3, 4)), 4)):
        for n in range(1, maximum + 1):
            for index, prefix in enumerate(product(alphabet, repeat=n)):
                label = (family, n, index)
                prefix_count += 1
                gaps, survival = gap_law(prefix)
                values = renewal(gaps)
                words, reference_u, reference_w = event_word_law(prefix)
                event_word_count += len(words)
                check(sum((weight for _, weight in words), ZERO) == ONE
                      and all(weight >= ZERO for _, weight in words),
                      section, (label, "probability"))
                check(values == reference_u and gaps == reference_w,
                      section, (label, "independent_event_words"))
                check(sum(gaps, ZERO) + survival[-1] == ONE,
                      section, (label, "survival"))
                inverse = invert(values)
                check(inverse["valid"] and inverse["gaps"] == gaps,
                      section, (label, "triangular_inverse"))
                if inverse["valid"]:
                    check(gap_law(inverse["canonical"])[0] == gaps,
                          section, (label, "canonical_forward"))
                    for k, item in enumerate(inverse["readback"]):
                        check(item == (prefix[k] if survival[k] > ZERO else "UNREACHABLE"),
                              section, (label, "reachable_hazard", k + 1))
                if survival[-1] > ZERO:
                    extension_count += 1
                    short = gaps + (survival[-1],)
                    long = gaps + (ZERO,) * 6 + (survival[-1],)
                    mean_short = sum((Q(k) * mass for k, mass in enumerate(short, 1)), ZERO)
                    mean_long = sum((Q(k) * mass for k, mass in enumerate(long, 1)), ZERO)
                    check(sum(short, ZERO) == sum(long, ZERO) == ONE
                          and renewal(short)[:n] == values == renewal(long)[:n],
                          "FINITE_PREFIX_EXTENSIONS", (label, "same_prefix"))
                    check(mean_long - mean_short == 6 * survival[-1]
                          and ONE / mean_long < ONE / mean_short,
                          "FINITE_PREFIX_EXTENSIONS", (label, "different_rate"))
    CENSUS["hazard_prefixes"] = prefix_count
    CENSUS["hazard_event_words"] = event_word_count
    CENSUS["positive_survival_extensions"] = extension_count
    check(prefix_count == 1122 and event_word_count == 56326 and extension_count == 156,
          section, "frozen_census_coverage")
    empty_short = (ONE,)
    empty_long = (ZERO,) * 6 + (ONE,)
    check(renewal(empty_short)[:0] == renewal(empty_long)[:0] == ()
          and sum((Q(k) * mass for k, mass in enumerate(empty_short, 1)), ZERO) == ONE
          and sum((Q(k) * mass for k, mass in enumerate(empty_long, 1)), ZERO) == Q(7),
          "FINITE_PREFIX_EXTENSIONS", "empty_prefix_different_proper_extensions")
    for n in range(1, 7):
        zero_prefix = (ZERO,) * n
        later = zero_prefix + (ONE,)
        check(renewal(gap_law(later)[0]) == zero_prefix + (ONE,),
              "FINITE_PREFIX_EXTENSIONS", ("zero_prefix_not_forever_silent", n))


def proposed_marginal_census():
    section = "PROPOSED_MARGINAL_CENSUS"
    total = valid = invalid = 0
    for n in range(1, 6):
        for index, values in enumerate(product((ZERO, Q(1, 2), ONE), repeat=n)):
            total += 1
            label = (n, index)
            inverse = invert(values)
            construction = construct_from_marginals(values)
            check(inverse["valid"] == construction["valid"],
                  section, (label, "independent_admission"))
            if inverse["valid"]:
                valid += 1
                check(construction["valid"]
                      and inverse["canonical"] == construction["canonical"]
                      and inverse["readback"] == construction["readback"],
                      section, (label, "constructed_hazards"))
                words, reference_u, reference_w = event_word_law(inverse["canonical"])
                check(reference_u == values and reference_w == inverse["gaps"]
                      and sum((weight for _, weight in words), ZERO) == ONE,
                      section, (label, "constructed_process"))
            else:
                invalid += 1
                k, reason, gap, cumulative = inverse["failure"]
                preceding = inverse["gaps"][:k - 1]
                earlier_valid = all(mass >= ZERO for mass in preceding)
                earlier_valid &= all(sum(preceding[:j], ZERO) <= ONE
                                     for j in range(1, len(preceding) + 1))
                fired = (gap < ZERO if reason == "NEGATIVE_GAP" else cumulative > ONE)
                check(earlier_valid and fired and not construction["valid"]
                      and construction["failure_index"] == k,
                      section, (label, "first_obstruction", reason, k))
    CENSUS["proposed_marginal_prefixes"] = total
    CENSUS["admitted_marginal_prefixes"] = valid
    CENSUS["rejected_marginal_prefixes"] = invalid
    check(total == 363 and valid > 0 and invalid > 0,
          section, "frozen_census_coverage")


def dead_time_census():
    section = "HARD_DEAD_TIME"
    cases = 0
    horizon = 24
    for dead in range(5):
        for alpha in (Q(1, 4), Q(1, 2), Q(3, 4), ONE):
            cases += 1
            prefix = tuple(ZERO if k <= dead else alpha for k in range(1, horizon + 1))
            gaps, _ = gap_law(prefix)
            values = renewal(gaps)
            rate = alpha / (ONE + dead * alpha)
            for n in range(1, horizon + 1):
                closed_w = (ZERO if n <= dead else
                            alpha * (ONE - alpha) ** (n - dead - 1))
                closed_u = sum((Q(comb(n - j * dead - 1, j - 1))
                                * alpha ** j
                                * (ONE - alpha) ** (n - j * (dead + 1))
                                for j in range(1, n // (dead + 1) + 1)), ZERO)
                check(gaps[n - 1] == closed_w and values[n - 1] == closed_u,
                      section, (dead, alpha, n, "shifted_negative_binomial"))
                if dead == 0:
                    check(values[n - 1] == alpha and values[n - 1] / rate == ONE,
                          section, (alpha, n, "memoryless"))
            # A finite age-state chain gives an independent stationary rate oracle.
            state_weights = (ONE / (ONE + dead * alpha),) + (rate,) * dead
            transitioned = [ZERO] * (dead + 1)
            if dead == 0:
                transitioned[0] = state_weights[0]
            else:
                transitioned[0] += state_weights[0] * (ONE - alpha)
                transitioned[dead] += state_weights[0] * alpha
                for remaining in range(1, dead + 1):
                    transitioned[remaining - 1] += state_weights[remaining]
            check(sum(state_weights, ZERO) == ONE and tuple(transitioned) == state_weights
                  and state_weights[0] * alpha == rate,
                  section, (dead, alpha, "stationary_chain"))
    silent_gaps, _ = gap_law((ZERO,) * horizon)
    check(silent_gaps == (ZERO,) * horizon and renewal(silent_gaps) == (ZERO,) * horizon,
          section, "alpha_zero_no_events")
    silent_rate = ZERO
    normalized_silent = "UNDEFINED_ZERO_RATE" if silent_rate == ZERO else ONE / silent_rate
    check(normalized_silent == "UNDEFINED_ZERO_RATE", section, "alpha_zero_no_normalization")
    witness_h = (ZERO,) + (Q(1, 2),) * 5
    witness_u = renewal(gap_law(witness_h)[0])
    witness_g = tuple(value / Q(1, 3) for value in witness_u)
    check(witness_u[1:4] == (Q(1, 2), Q(1, 4), Q(3, 8))
          and witness_g[1:4] == (Q(3, 2), Q(3, 4), Q(9, 8))
          and all(value != ONE for value in witness_g[1:4]),
          section, "all_pairs_not_efficiency_primary_counterexample")
    CENSUS["dead_time_positive_parameter_pairs"] = cases
    check(cases == 20, section, "frozen_census_coverage")
    return {"dead_slots": 1, "alpha": Q(1, 2), "rate": Q(1, 3),
            "lags": (2, 3, 4), "u": witness_u[1:4], "g": witness_g[1:4],
            "efficiency": (ONE, ONE, ONE), "alpha_zero_normalization": normalized_silent}


def dilute_census():
    section = "DILUTE_BOUND"
    cases = 0
    for alpha in (Q(1, 4), Q(1, 2), Q(3, 4), ONE):
        for n in range(1, 6):
            for index, efficiency in enumerate(product((ZERO, Q(1, 2), ONE), repeat=n)):
                cases += 1
                prefix = tuple(alpha * value for value in efficiency)
                gaps, survival = gap_law(prefix)
                values = renewal(gaps)
                for k in range(1, n + 1):
                    error = abs(values[k - 1] - prefix[k - 1])
                    bound1 = alpha * (ONE - survival[k - 1])
                    bound2 = alpha * (ONE - (ONE - alpha) ** (k - 1))
                    bound3 = alpha * alpha * (k - 1)
                    check(error <= bound1 <= bound2 <= bound3,
                          section, (alpha, n, index, k))
        sharp_h = (alpha, ZERO)
        sharp_u = renewal(gap_law(sharp_h)[0])
        check(sharp_u[1] - sharp_h[1] == alpha * alpha,
              section, (alpha, "k2_sharpness"))
    CENSUS["dilute_efficiency_prefixes"] = cases
    check(cases == 1452, section, "frozen_census_coverage")


def input_efficiency_ambiguity():
    section = "INPUT_EFFICIENCY_AMBIGUITY"
    prefix = (ZERO, Q(1, 4), Q(1, 2), Q(1, 4))
    reference = event_word_law(prefix)
    for alpha in (Q(1, 2), Q(3, 4), ONE):
        efficiency = tuple(value / alpha for value in prefix)
        rebuilt = tuple(alpha * value for value in efficiency)
        check(all(ZERO <= value <= ONE for value in efficiency)
              and rebuilt == prefix and event_word_law(rebuilt) == reference,
              section, (alpha, "same_complete_prefix_process"))
    for alpha in (Q(1, 8), Q(1, 4), Q(3, 8), Q(1, 2), Q(3, 4), ONE):
        efficiency = tuple(value / alpha for value in prefix)
        check(all(ZERO <= value <= ONE for value in efficiency) == (max(prefix) <= alpha <= ONE),
              section, (alpha, "feasible_interval"))
    for n in range(1, 6):
        zero_word_law = event_word_law((ZERO,) * n)[0]
        check(all(weight == (ONE if word == (0,) * n else ZERO)
                  for word, weight in zero_word_law),
              section, (n, "zero_hazard_prefix_process"))
        for efficiency in product((ZERO, Q(1, 2), ONE), repeat=n):
            check(tuple(ZERO * value for value in efficiency) == (ZERO,) * n,
                  section, (n, efficiency, "zero_alpha_efficiency_unidentified"))
        for alpha in (Q(1, 4), Q(1, 2), Q(3, 4), ONE):
            check(tuple(alpha * ZERO for _ in range(n)) == (ZERO,) * n,
                  section, (n, alpha, "zero_prefix_positive_alpha_zero_efficiency"))
    check(max((ZERO, ZERO)) == ZERO, section, "all_zero_feasible_lower_endpoint")


def finite_parity_control():
    section = "NONRENEWAL_PARITY"
    iid = tuple((word, Q(1, 8)) for word in product((0, 1), repeat=3))
    parity = tuple((word, Q(1, 4)) for word in product((0, 1), repeat=3)
                   if sum(word) % 2 == 0)

    def marginal(law, indices, values):
        return sum((weight for word, weight in law
                    if tuple(word[index] for index in indices) == values), ZERO)

    for size in (1, 2):
        for indices in combinations(range(3), size):
            for values in product((0, 1), repeat=size):
                check(marginal(iid, indices, values) == marginal(parity, indices, values),
                      section, (indices, values, "matching_low_order_marginals"))
    check(marginal(iid, (0, 1, 2), (1, 1, 1)) == Q(1, 8)
          and marginal(parity, (0, 1, 2), (1, 1, 1)) == ZERO,
          section, "different_triple")
    u_iid = tuple(marginal(iid, (index,), (1,)) for index in range(3))
    u_parity = tuple(marginal(parity, (index,), (1,)) for index in range(3))
    inverse = invert(u_parity)
    w3_iid = marginal(iid, (0, 1, 2), (0, 0, 1))
    w3_parity = marginal(parity, (0, 1, 2), (0, 0, 1))
    check(u_iid == u_parity == (Q(1, 2),) * 3
          and inverse["valid"] and inverse["gaps"][2] == w3_iid == Q(1, 8)
          and w3_parity == ZERO,
          section, "same_anchored_pairs_different_true_first_gap")


def stationary_homometric_control():
    section = "STATIONARY_HOMOMETRIC_CONTROL"
    period = 12
    sets = ((0, 1, 4, 6), (0, 1, 3, 7))
    pair_vectors = []
    gap_vectors = []
    for label, positions in enumerate(sets):
        phase_words = tuple(tuple(int((time + phase) % period in positions)
                                  for time in range(49)) for phase in range(period))
        anchors = tuple(word for word in phase_words if word[0])
        check(Q(len(anchors), period) == Q(1, 3), section, (label, "intensity"))
        pair_values = tuple(Q(sum(word[lag] for word in anchors), len(anchors))
                            for lag in range(49))
        direct_residues = tuple(Q(sum((origin + lag) % period in positions
                                     for origin in positions), len(positions))
                                for lag in range(period))
        for lag, value in enumerate(pair_values):
            expected = ONE if lag % period == 0 else Q(1, 2) if lag % period == 6 else Q(1, 4)
            check(value == expected == direct_residues[lag % period],
                  section, (label, lag, "all_pair_formula"))
        first_gaps = tuple(next(time for time in range(1, period + 1) if word[time])
                           for word in anchors)
        gap_vector = tuple(Q(first_gaps.count(gap), len(anchors))
                           for gap in range(1, period + 1))
        sorted_cycle = tuple(positions[(index + 1) % len(positions)] - origin
                             if index + 1 < len(positions) else period + positions[0] - origin
                             for index, origin in enumerate(positions))
        check(sorted(first_gaps) == sorted(sorted_cycle)
              and sum(gap_vector, ZERO) == ONE
              and sum((Q(n) * value for n, value in enumerate(gap_vector, 1)), ZERO) == Q(3),
              section, (label, "next_gap_from_phase_and_cycle"))
        pair_vectors.append(pair_values)
        gap_vectors.append(gap_vector)
    check(pair_vectors[0] == pair_vectors[1] and gap_vectors[0] != gap_vectors[1],
          section, "same_all_lags_and_rate_different_next_gaps")
    expected_supports = ((1, 2, 3, 6), (1, 2, 4, 5))
    for label, support in enumerate(expected_supports):
        check(gap_vectors[label] == tuple(Q(1, 4) if n in support else ZERO
                                          for n in range(1, period + 1)),
              section, (label, "exact_gap_vector"))
    CENSUS["homometric_uniform_phases"] = 24
    CENSUS["homometric_lags_per_process"] = 49
    return {"period": period, "sets": sets, "intensity": Q(1, 3),
            "palm_pair_residues": pair_vectors[0][:period],
            "first_gap_A": gap_vectors[0], "first_gap_B": gap_vectors[1]}


def main():
    typed_boundaries()
    hazard_census()
    proposed_marginal_census()
    primary = dead_time_census()
    dilute_census()
    input_efficiency_ambiguity()
    finite_parity_control()
    homometric = stationary_homometric_control()
    output = {
        "name": NAME,
        "counts": COUNTS,
        "total": sum(COUNTS.values()),
        "census": CENSUS,
        "failure_count": FAILURE_COUNT,
        "failures": FAILURES,
        "failure_list_cap": FAILURE_CAP,
        "result": "FALSIFIED" if FAILURE_COUNT else "PROOF_AUDIT_PASS",
        "counterexamples": {"dead_time": primary, "homometric": homometric},
        "scope": "Exact finite renewal-model audit and nonrenewal counterexamples; no empirical calibration, detector identification, or Born inference",
    }
    print(json.dumps(json_value(output), sort_keys=True, ensure_ascii=True,
                     separators=(",", ":"), allow_nan=False))


if __name__ == "__main__":
    main()
