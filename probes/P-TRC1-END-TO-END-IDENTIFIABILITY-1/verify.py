"""Exact finite audit of the conditional TRC1 chain; no physical realization.

Execute only after public preregistration, source pin and byte readback.
The proof supplies general statements; this bounded census audits this adapter.
"""
from collections import defaultdict
from dataclasses import fields, is_dataclass, replace
from fractions import Fraction as Q
from itertools import product
import json

import chain as C


NAME = "P-TRC1-END-TO-END-IDENTIFIABILITY-1"
ZERO, ONE = Q(0), Q(1)
COUNTS, CENSUS, FAILURES = {}, {}, []
FAILURE_COUNT, FAILURE_CAP = 0, 40
ENERGIES = {}
ORIGIN = (0, 0, 0)


def json_value(value):
    if type(value) is Q:
        return {"numerator": value.numerator, "denominator": value.denominator}
    if is_dataclass(value) and not isinstance(value, type):
        return {"type": type(value).__name__,
                **{field.name: json_value(getattr(value, field.name)) for field in fields(value)}}
    if type(value) in (tuple, list):
        return [json_value(item) for item in value]
    if type(value) is dict:
        return {key: json_value(item) for key, item in value.items()}
    if value is None or type(value) in (str, int, bool):
        return value
    raise TypeError("unsupported exact audit presentation")


def check(condition, section, label):
    global FAILURE_COUNT
    COUNTS[section] = COUNTS.get(section, 0) + 1
    if not condition:
        FAILURE_COUNT += 1
        if len(FAILURES) < FAILURE_CAP:
            FAILURES.append({"section": section, "label": label})


def rejects(thunk, section, label):
    try:
        thunk()
    except (TypeError, ValueError):
        check(True, section, label)
    else:
        check(False, section, label)


def head(z, counter=0, qr=(0, 0)):
    return counter, tuple(a % 5 for a in z) + qr


def context(gamma=(), quantum=ONE, horizon=0):
    return C.Context(C.wave.field(gamma), Q(quantum), horizon)


def energy(pair):
    if pair not in ENERGIES:
        ENERGIES[pair] = C.wave.energy(pair)
    return ENERGIES[pair]


def native_oracle(source):
    n, (a, b, c, d, q, r) = source
    selector = (a + b + c + d + q + r + 2 * (bin(n).count("1") % 2)) % 5
    candidates = (
        (b, a, d, c, q, r),
        (-c, -d, -a, -b, -q, -r),
        (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r),
        (2-a, 1-b, 3-c, 4-d, 1-q, 1-r),
        (2-a, 1-b, 3-c, 4-d, 2-q, 1-r),
    )
    return n + 1, tuple(a % 5 for a in candidates[selector])


def source_census():
    section = "SOURCE_AND_NATIVE_CENSUS"
    empty = context()
    antipodal = set()
    for z in product(range(-2, 3), repeat=4):
        h = head(z)
        prepared = C.prepare(h, empty)
        qdd = C.native.direct_qdd(h)
        s = sum(z)
        mass = sum(Q(a*a) for a in z) - Q(s*s, 5)
        low, high = Q(s*s, 20), sum(Q(a*a) for a in z) - Q(s*s, 4)
        check(C.native.balanced_head(h) == z, section, (z, "signed_read"))
        check(C.support(h) == ("SUPPORTED" if any(z) else "ZERO_SOURCE", h),
              section, (z, "typed_source_support_decision"))
        check(qdd.total_weight == mass and qdd.branch_weights == (low, high),
              section, (z, "direct_cyclotomic_weights"))
        check(prepared.pair == C.wave.prepare(z)
              and C.wave.norm2(prepared.pair.current) == mass,
              section, (z, "five_site_preparation"))
        check(prepared.source == h and prepared.checkpoint == h
              and prepared.tick == 0 and prepared.history == ()
              and prepared.apparatus.tape == () and prepared.apparatus.heat == (),
              section, (z, "complete_ready_state"))
        matter = C.matter_at(h, empty, 0)
        check(matter.source_head == h and matter.signed_source == z
              and matter.support_state == qdd.support_state
              and matter.total_weight == qdd.total_weight
              and matter.branch_weights == qdd.branch_weights
              and matter.density_state == qdd.density_state
              and matter.normalized_weight_state == qdd.normalized_weight_state
              and matter.linear_tr4 == sum(h[1][:4]) % 5
              and matter.binary_theta == 0,
              section, (z, "all_nine_matter_fields"))
        neg = tuple(-a for a in z)
        check(qdd == C.native.direct_qdd(head(neg)), section, (z, "antipodal_qdd"))
        antipodal.add(min(z, neg))
    check(len(antipodal) == 313, section, "625_signed_heads_313_antipodal_classes")
    for n in (0, 1, 32):
        for x in product(range(5), repeat=6):
            h = (n, x)
            check(C.native.u_step(h) == native_oracle(h), section, (n, x, "native_update"))
    CENSUS.update(canonical_signed_heads=625, antipodal_classes=313,
                  native_checkpoint_values=15625, native_counter_starts=(0, 1, 32))


def typed_boundaries():
    section = "TYPED_BOUNDARIES"
    e0 = head((1, 0, 0, 0))
    for label, bad in (("bool_counter", (True, e0[1])),
                       ("negative_counter", (-1, e0[1])),
                       ("bool_pentit", (0, (True, 0, 0, 0, 0, 0))),
                       ("pentit_outside_F5", (0, (5, 0, 0, 0, 0, 0)))):
        rejects(lambda bad=bad: C.prepare(bad, context()), section, label)
    for label, thunk in (
        ("zero_quantum", lambda: context((), ZERO, 1)),
        ("negative_quantum", lambda: context((), Q(-1), 1)),
        ("float_quantum", lambda: C.Context((), 0.125, 1)),
        ("bool_horizon", lambda: C.Context((), ONE, True)),
        ("negative_horizon", lambda: context((), ONE, -1)),
        ("negative_gamma", lambda: context(((ORIGIN, Q(-1)),), ONE, 1)),
        ("non_D3_site", lambda: context((((1, 0, 0), ONE),), ONE, 1)),
        ("duplicate_site", lambda: context(((ORIGIN, ONE), (ORIGIN, ONE)), ONE, 1)),
    ):
        rejects(thunk, section, label)
    c = context()
    invalid_head = (False, e0[1])
    unsupported = C.prepare_request(invalid_head, c)
    check(unsupported[0] == "UNSUPPORTED_REQUEST"
          and type(unsupported[1]) is str and bool(unsupported[1])
          and unsupported[2][0] is invalid_head and unsupported[2][1] is c,
          section, "administrative_invalid_request_retains_original_input")
    zero_head = head((0, 0, 0, 0))
    prepared_zero = C.prepare_request(zero_head, c)
    check(prepared_zero == ("PREPARED_MODEL", C.prepare(zero_head, c)),
          section, "administrative_valid_zero_is_prepared")
    physical = C.physical_request((zero_head, c))
    check(physical == ("STOP_PHYSICAL", (zero_head, c))
          and len({unsupported[0], prepared_zero[0], physical[0]}) == 3,
          section, "invalid_zero_and_physical_absence_have_distinct_tags")


def chain_census():
    section = "COMPLETE_CHAIN"
    sources = (
        ("zero", head((0, 0, 0, 0))), ("e0", head((1, 0, 0, 0))),
        ("minus_e0", head((-1, 0, 0, 0))), ("twice_e0", head((2, 0, 0, 0))),
        ("e1", head((0, 1, 0, 0))), ("low_null", head((1, -1, 0, 0))),
        ("high_null", head((1, 1, 1, 1))),
        ("e0_qr_alias", head((1, 0, 0, 0), qr=(1, 2))),
        ("e0_counter_alias", head((1, 0, 0, 0), counter=7)),
    )
    contexts = (
        ("empty_0", context()), ("empty_2", context((), ONE, 2)),
        ("origin_16", context(((ORIGIN, ONE),), Q(1, 16), 2)),
        ("origin_8", context(((ORIGIN, ONE),), Q(1, 8), 2)),
        ("two_ports", context(((ORIGIN, ONE), ((1, 1, 0), Q(2))), Q(1, 16), 1)),
    )
    cache = {}
    for source_name, h in sources:
        z = C.native.balanced_head(h)
        for context_name, c in contexts:
            state = C.prepare(h, c)
            states = [state]
            seen_ordinals = set()
            native_checkpoint = h
            initial_energy = C.native.direct_qdd(h).total_weight / 2
            for tick in range(c.horizon):
                output = C.step(state)
                event = C.emit(output)
                after = C.append(state, event)
                native_checkpoint = native_oracle(native_checkpoint)
                label = (source_name, context_name, tick)
                check(C.persist(state.apparatus, event) == after.apparatus
                      == output.next_apparatus and after.pair == output.next_pair,
                      section, (label, "step_emit_persist_append_agree"))
                check(event.source == h and event.context == c and event.tick == tick
                      and event.start_checkpoint == state.checkpoint
                      and event.completed_checkpoint == native_checkpoint
                      and after.checkpoint == native_checkpoint,
                      section, (label, "actual_native_provenance"))
                matter = C.matter_at(h, c, tick + 1)
                check(matter.source_head == h and matter.signed_source == z
                      and matter.total_weight == 2*initial_energy
                      and matter.linear_tr4 == sum(native_checkpoint[1][:4]) % 5
                      and matter.binary_theta == bin(native_checkpoint[0]).count("1") % 2,
                      section, (label, "anchored_quadratic_actual_linear_binary"))
                check(event.pair_before == state.pair and event.pair_after == after.pair
                      and event.apparatus_before == state.apparatus
                      and event.apparatus_after == after.apparatus
                      and after.history == state.history + (event,),
                      section, (label, "complete_immutable_snapshots"))
                check(after.apparatus.tape == state.apparatus.tape + (event.outgoing,)
                      and len(after.apparatus.tape) == tick + 1,
                      section, (label, "one_fresh_vector_and_one_event"))
                outgoing = dict(event.outgoing)
                expected_deposit = C.wave.field((x, g*outgoing.get(x, ZERO)**2)
                                                for x, g in c.gamma)
                check(event.deposit == expected_deposit
                      and event.heat_before == state.apparatus.heat
                      and event.heat_after == after.apparatus.heat
                      == C.wave.add(state.apparatus.heat, expected_deposit),
                      section, (label, "signed_tape_heat_account"))
                check(energy(after.pair) + sum(dict(after.apparatus.heat).values(), ZERO)
                      == initial_energy, section, (label, "exact_energy_budget"))
                old_counts, new_counts = dict(event.counts_before), dict(event.counts_after)
                heat_after = dict(event.heat_after)
                rem = dict(event.remainder_after)
                check(tuple(new_counts) == tuple(x for x, _ in c.gamma)
                      and all(new_counts[x] == heat_after.get(x, ZERO)//c.quantum
                              and 0 <= rem.get(x, ZERO) < c.quantum
                              and heat_after.get(x, ZERO)
                              == c.quantum*new_counts[x] + rem.get(x, ZERO)
                              for x in new_counts),
                      section, (label, "floor_and_remainder"))
                newly = {(cross.site, ordinal) for cross in event.crossings
                         for ordinal in range(cross.first, cross.last + 1)}
                expected_new = {(x, ordinal) for x in new_counts
                                for ordinal in range(old_counts[x] + 1, new_counts[x] + 1)}
                check(newly == expected_new and not (newly & seen_ordinals),
                      section, (label, "all_new_ordinals_once"))
                seen_ordinals |= newly
                check(seen_ordinals == {(x, ordinal) for x in new_counts
                                         for ordinal in range(1, new_counts[x] + 1)},
                      section, (label, "complete_lifetime_addresses"))
                old_pair, incoming = C.reservoir.reverse(
                    after.pair, C.reservoir.Context(c.gamma, c.quantum), event.outgoing)
                check(old_pair == state.pair and incoming == (),
                      section, (label, "cold_interaction_reverse"))
                packet = C.model_read(event)
                visible = C.visible(packet)
                multiplicity = len(newly)
                category = ("ZERO_SOURCE_ACCOUNTING" if not any(z) else
                            "NO_THRESHOLD_CROSSING" if not multiplicity else
                            "SINGLE_THRESHOLD_CROSSING" if multiplicity == 1 else
                            "MULTIPLE_THRESHOLD_CROSSINGS")
                kind = ("NO_CROSSING" if not multiplicity else
                        "SINGLE_CROSSING" if multiplicity == 1 else "MULTIPLE_CROSSINGS")
                check(packet.event_ref == event and packet.category == category
                      and packet.origin == "MODEL_RRP1"
                      and packet.coverage_evidence == "MODEL_TRANSITION_COMPLETE"
                      and packet.calibration_refs == "UNRESOLVED",
                      section, (label, "full_model_packet_no_certificate"))
                check(visible.context == c and visible.tick == tick and visible.kind == kind
                      and visible.crossings == event.crossings
                      and dict(visible.multiplicities)
                      == {x: new_counts[x]-old_counts[x] for x in new_counts},
                      section, (label, "declared_visible_projection"))
                check(C.reread(event) == event and C.reread(C.reread(event)) == event,
                      section, (label, "passive_reread"))
                if not any(z):
                    check(after.pair == C.wave.Pair((), ()) and event.outgoing == ()
                          and event.deposit == () and not event.crossings,
                          section, (label, "zero_source_still_has_accounting_event"))
                state = after
                states.append(state)
            check(len(state.history) == c.horizon, section, (source_name, context_name, "horizon"))
            ended = C.advance(state)
            check(type(ended) is C.EndState and ended.payload == state
                  and C.advance(ended) == ended
                  and C.apparatus_of(ended) == state.apparatus,
                  section, (source_name, context_name, "END_retains_state"))
            check(C.reset_request(state) == ("REJECTED_RESET_DISABLED", state),
                  section, (source_name, context_name, "reset_disabled"))
            cache[source_name, context_name] = tuple(states)
    for context_name, c in contexts:
        for alias in ("minus_e0", "e0_qr_alias", "e0_counter_alias"):
            left, right = cache["e0", context_name][-1], cache[alias, context_name][-1]
            check(tuple(C.visible(C.model_read(e)) for e in left.history)
                  == tuple(C.visible(C.model_read(e)) for e in right.history),
                  section, (context_name, alias, "visible_factorization"))
            check(left != right, section, (context_name, alias, "full_source_provenance_retained"))
    for key in (("e0", "origin_16"), ("zero", "empty_2")):
        states = cache[key]
        h, c = states[0].source, states[0].context
        for k, state in enumerate(states):
            check(C.run(h, c, k) == state, section, (key, k, "same_context_prefix"))
            if k < c.horizon:
                check(C.advance(state) == states[k + 1], section, (key, k, "single_transition_composition"))
    CENSUS.update(propagated_sources=tuple(name for name, _ in sources),
                  propagated_contexts=tuple(name for name, _ in contexts))
    return cache


def stage_composition_controls(cache):
    section = "STAGE_COMPOSITION"
    state = cache["e0", "origin_16"][1]
    event = state.history[0]
    geom = C.geometry(state)
    check(geom.pair_sequence == (event.pair_before, event.pair_after)
          and geom.port_sequence == (event.outgoing,)
          and geom.energy_sequence == (energy(event.pair_before), energy(event.pair_after))
          and len(geom.local_current_sequence) == 1,
          section, "complete_geometry_stage")
    current = geom.local_current_sequence[0]
    edges = ((ORIGIN, (1, 1, 0)), (ORIGIN, (2, 0, 0)),
             ((1, 1, 0), (0, 1, 1)), (ORIGIN, (8, 0, 0)))
    for x, y in edges:
        value = current.value(x, y)
        check(value == C.wave.current(event.pair_before, event.pair_after.current, x, y)
              and value == -current.value(y, x), section, (x, y, "fixed_current_and_antisymmetry"))
    check(current.value(ORIGIN, (8, 0, 0)) == ZERO,
          section, "non_stencil_current_zero")
    for source_name in ("e0", "zero"):
        states = cache[source_name, "origin_16"]
        for tick, state in enumerate(states):
            successor, observation = C.transition(state)
            expected_successor = states[tick + 1] if tick < 2 else C.EndState(state)
            expected_observation = (C.visible(C.model_read(states[tick + 1].history[-1]))
                                    if tick < 2 else "END")
            check(successor == expected_successor and observation == expected_observation
                  and C.kernel_mass(state, successor, observation) == ONE
                  and C.kernel_mass(state, successor, "NOT_THE_OUTPUT") == ZERO,
                  section, (source_name, tick, "Dirac_kernel_successor_output"))
    evidence = ("unidentified_source", "unrealized_fresh_slots")
    check(C.physical_request(evidence) == ("STOP_PHYSICAL", evidence),
          section, "physical_missing_premises_retained")


def record_forgery_controls(cache):
    section = "RECORD_FORGERY_CONTROLS"
    states = cache["e0", "origin_16"]
    initial, first, final = states
    event = first.history[0]
    rejects(lambda: C.append(first, event), section, "duplicate_event")
    rejects(lambda: C.append(initial, final.history[1]), section, "skipped_event")
    rejects(lambda: C.append(cache["e1", "origin_16"][0], event), section, "foreign_source")
    rejects(lambda: C.append(cache["e0", "origin_8"][0], event), section, "foreign_context")
    rejects(lambda: C.persist(final.apparatus, event), section, "wrong_old_apparatus")
    rejects(lambda: C.append(initial, replace(event, tick=1)), section, "forged_tick")
    rejects(lambda: C.append(initial, replace(event, completed_checkpoint=event.start_checkpoint)),
            section, "incomplete_native_transition")
    rejects(lambda: C.append(initial, replace(event, transition_complete=False)),
            section, "false_completion")
    negative_outgoing = C.wave.scale(event.outgoing, -1)
    check(C.reservoir.port_energy(negative_outgoing,
                                 C.reservoir.Context(event.context.gamma, event.context.quantum))
          == C.reservoir.port_energy(event.outgoing,
                                    C.reservoir.Context(event.context.gamma, event.context.quantum)),
          section, "forged_sign_preserves_energy")
    rejects(lambda: C.append(initial, replace(event, outgoing=negative_outgoing)),
            section, "energy_only_tape_forgery_rejected")
    negative_pair = C.wave.Pair(C.wave.scale(event.pair_after.previous, -1),
                                C.wave.scale(event.pair_after.current, -1))
    check(energy(negative_pair) == energy(event.pair_after), section, "forged_pair_preserves_energy")
    rejects(lambda: C.append(initial, replace(event, pair_after=negative_pair)),
            section, "energy_only_pair_forgery_rejected")
    rejects(lambda: C.append(initial, replace(event, source=head((0, 1, 0, 0)))),
            section, "forged_source_field")
    altered = (C.reservoir.Crossing(ORIGIN, 1, 2),)
    rejects(lambda: C.append(initial, replace(event, crossings=altered)),
            section, "altered_crossing_range")
    rejects(lambda: C.append(initial, replace(event, counts_after=((ORIGIN, True),))),
            section, "bool_count_equal_to_integer_one_rejected")
    packet = C.model_read(event)
    rejects(lambda: replace(packet, interval_id=False), section, "bool_packet_interval_rejected")
    rejects(lambda: replace(packet, multiplicities=((ORIGIN, True),)),
            section, "bool_packet_multiplicity_rejected")
    false_head = (False, event.source[1])
    check(false_head == event.source, section, "Python_bool_integer_equality_control")
    rejects(lambda: replace(packet, source_run_context_refs=(false_head, event.context)),
            section, "bool_in_nested_packet_head_rejected")
    other = cache["e1", "origin_16"][1].history[0]
    local = C.reservoir.couple(other.pair_before,
                              C.reservoir.Context(event.context.gamma, event.context.quantum))
    check(local.after == other.pair_after and local.outgoing == other.outgoing
          and local.transfer == other.deposit and other.pair_before != event.pair_before,
          section, "wrong_initial_pair_is_still_a_locally_valid_cold_step")
    false_before = C.Apparatus(event.source, event.context, 0, (), ())
    false_after = C.Apparatus(event.source, event.context, 1,
                              (other.outgoing,), other.heat_after)
    def wrong_preparation_record():
        return replace(other, source=event.source,
                       start_checkpoint=event.start_checkpoint,
                       completed_checkpoint=event.completed_checkpoint,
                       apparatus_before=false_before, apparatus_after=false_after)
    rejects(wrong_preparation_record, section,
            "locally_consistent_foreign_preparation_rejected_as_Event")


def ensemble(*atoms):
    return tuple(sorted(atoms))


def word(state):
    return tuple(C.visible(C.model_read(event)) for event in state.history)


def ensemble_controls(cache):
    section = "ONCE_SAMPLED_ENSEMBLE"
    c = cache["e0", "origin_16"][0].context
    atoms = ensemble((head((0, 0, 0, 0)), Q(1, 2)), (head((2, 0, 0, 0)), Q(1, 2)))
    laws = []
    for k in range(c.horizon + 1):
        law = dict(C.pushforward(atoms, c, k))
        expected = {word(cache[name, "origin_16"][k]): Q(1, 2)
                    for name in ("zero", "twice_e0")}
        if k == 0:
            expected = {(): ONE}
        check(law == expected and sum(law.values(), ZERO) == ONE
              and all(weight > 0 for weight in law.values()), section, (k, "exact_pushforward"))
        if k:
            marginal = defaultdict(Q)
            for prefix, weight in law.items():
                marginal[prefix[:-1]] += weight
            check(dict(marginal) == laws[-1], section, (k, "prefix_consistency"))
        for prefix, weight in law.items():
            posterior = C.posterior(atoms, c, prefix)
            check(posterior.status == "CONDITIONAL_MODEL_LAW"
                  and posterior.evidence_mass == weight
                  and sum((p for _, p in posterior.atoms), ZERO) == ONE
                  and tuple(state.source for state in posterior.states)
                  == tuple(h for h, _ in posterior.atoms)
                  and all(word(state) == prefix for state in posterior.states),
                  section, (k, prefix, "source_survivor_conditioning"))
            expected_next = defaultdict(Q)
            for h, posterior_weight in posterior.atoms:
                key = "END" if k == c.horizon else word(C.run(h, c))[k]
                expected_next[key] += posterior_weight
            check(dict(posterior.next_law) == dict(expected_next),
                  section, (k, prefix, "conditional_next_without_resampling"))
        laws.append(law)
    full_law = dict(C.full_pushforward(atoms, c, 2))
    projected_full = defaultdict(Q)
    for events, weight in full_law.items():
        projected_full[tuple(C.visible(C.model_read(event)) for event in events)] += weight
    prediction = C.prediction(atoms, c, 2)
    check(dict(projected_full) == laws[2]
          and prediction.context_ref == c and prediction.ensemble_ref == atoms
          and prediction.horizon == 2 and dict(prediction.packet_prefix_mass_table) == laws[2],
          section, "full_history_projection_and_prediction_record")
    first_marginal, second_marginal = defaultdict(Q), defaultdict(Q)
    for prefix, weight in laws[2].items():
        first_marginal[prefix[0]] += weight
        second_marginal[prefix[1]] += weight
    # Independent trajectory-label selection for each observation cut. This
    # product does not simulate physical re-injection into retained memory.
    product_law = {(a, b): pa*pb for a, pa in first_marginal.items()
                   for b, pb in second_marginal.items()}
    check(len(first_marginal) == len(second_marginal) == 2
          and product_law != laws[2], section, "product_of_time_marginals_changes_two_tick_law")
    first_words = tuple(laws[2])
    impossible = (first_words[0][0], first_words[1][1])
    result = C.posterior(atoms, c, impossible)
    check(impossible not in laws[2] and result.status == "IMPOSSIBLE_UNDER_FIXED_MODEL"
          and result.evidence_mass == ZERO and result.atoms == () and result.next_law == (),
          section, "zero_mass_prefix_has_no_posterior")
    rejects(lambda: C.pushforward((), c, 1), section, "empty_ensemble")
    rejects(lambda: C.pushforward(((atoms[0][0], ZERO), (atoms[1][0], ONE)), c, 1),
            section, "zero_atoms_not_canonical")
    rejects(lambda: C.pushforward(((atoms[0][0], Q(1, 2)),), c, 1),
            section, "unnormalized_ensemble")
    rejects(lambda: C.pushforward((atoms[0], atoms[0]), c, 1), section, "duplicate_heads")
    rejects(lambda: C.pushforward(tuple(reversed(atoms)), c, 1), section, "unsorted_heads")
    return {"initial_atoms": atoms, "two_tick_law": tuple(laws[2].items()),
            "product_of_time_marginals_atom_count": len(product_law),
            "product_control_scope": "Independent trajectory-label selection per observation cut; no physical re-injection model"}


def rref(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    width = len(rows[0])
    pivots, row = [], 0
    for col in range(width):
        pivot = next((i for i in range(row, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        factor = rows[row][col]
        rows[row] = [a/factor for a in rows[row]]
        for i in range(len(rows)):
            if i != row:
                factor = rows[i][col]
                rows[i] = [a-factor*b for a, b in zip(rows[i], rows[row])]
        pivots.append(col)
        row += 1
        if row == len(rows):
            break
    return tuple(map(tuple, rows)), tuple(pivots)


def nullspace(matrix):
    reduced, pivots = rref(matrix)
    width = len(matrix[0])
    basis = []
    for free in (j for j in range(width) if j not in pivots):
        vector = [ZERO]*width
        vector[free] = ONE
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        basis.append(tuple(vector))
    return tuple(basis)


def matvec(matrix, vector):
    return tuple(sum((a*b for a, b in zip(row, vector)), ZERO) for row in matrix)


def identifies(calibration, prediction):
    return all(not any(matvec(prediction, vector)) for vector in nullspace(calibration))


def identifiability_controls():
    section = "ACTUAL_CHAIN_IDENTIFIABILITY"
    a, b, twice = head((1, 0, 0, 0)), head((0, 1, 0, 0)), head((2, 0, 0, 0))
    qa, qb, qt = (C.native.direct_qdd(h) for h in (a, b, twice))
    c = context(((ORIGIN, ONE),), Q(1, 16), 1)
    sa, sb = C.run(a, c), C.run(b, c)
    ea, eb = sa.history[0], sb.history[0]
    deposit_a, deposit_b = Q(1421, 4860)**2, Q(349, 4860)**2
    check(dict(ea.deposit)[ORIGIN] == deposit_a and dict(eb.deposit)[ORIGIN] == deposit_b,
          section, "exact_origin_response_basis_heads")
    check(dict(ea.counts_after)[ORIGIN] == 1 and dict(eb.counts_after)[ORIGIN] == 0,
          section, "same_weights_different_actual_counts")
    check(qa.total_weight == qb.total_weight == Q(4, 5)
          and qa.branch_weights == qb.branch_weights == (Q(1, 20), Q(3, 4))
          and qa.normalized_weight_state == qb.normalized_weight_state
          and qa.density_state != qb.density_state,
          section, "scalar_calibration_explicitly_excludes_density")
    calibration = ((ONE, ONE), (qa.total_weight, qb.total_weight),
                   (qa.branch_weights[0], qb.branch_weights[0]),
                   (qa.branch_weights[1], qb.branch_weights[1]))
    prediction = ((ZERO, ONE), (ONE, ZERO))
    left, right = (Q(1, 3), Q(2, 3)), (Q(2, 3), Q(1, 3))
    check(len(rref(calibration)[1]) == 1 and len(rref(prediction)[1]) == 2
          and nullspace(calibration) == ((Q(-1), ONE),)
          and not identifies(calibration, prediction), section, "rank_and_kernel_failure")
    check(matvec(calibration, left) == matvec(calibration, right)
          and matvec(prediction, left) != matvec(prediction, right),
          section, "two_interior_mixtures_same_calibration_different_prediction")
    for weights in (left, right):
        law = dict(C.pushforward(ensemble((a, weights[0]), (b, weights[1])), c, 1))
        check(law == {word(sa): weights[0], word(sb): weights[1]},
              section, (weights, "matrix_prediction_equals_whole_chain"))
    augmented = calibration + ((ONE, ZERO),)
    check(len(rref(augmented)[1]) == 2 and nullspace(augmented) == ()
          and identifies(augmented, prediction), section, "declared_source_indicator_positive_control")
    c8 = context(((ORIGIN, ONE),), Q(1, 8), 1)
    sa8, st8 = C.run(a, c8), C.run(twice, c8)
    check(dict(sa8.history[0].counts_after)[ORIGIN] == 0
          and dict(st8.history[0].counts_after)[ORIGIN] == 2
          and dict(st8.history[0].deposit)[ORIGIN] == 4*deposit_a,
          section, "scale_heads_actual_counts_zero_and_two")
    check(qa.normalized_weight_state == qt.normalized_weight_state
          and qa.density_state == qt.density_state
          and qa.total_weight != qt.total_weight,
          section, "normalized_calibration_excludes_absolute_energy")
    scale_laws = []
    for weights in (left, right):
        law = dict(C.pushforward(ensemble((a, weights[0]), (twice, weights[1])), c8, 1))
        check(law == {word(sa8): weights[0], word(st8): weights[1]},
              section, (weights, "scale_mixture_whole_chain"))
        scale_laws.append(tuple(law.items()))
    return {"source_order": (a, b), "scalar_calibration": calibration,
            "prediction_rows_counts_0_then_1": prediction,
            "kernel": nullspace(calibration), "interior_weights": (left, right),
            "origin_deposits": (deposit_a, deposit_b),
            "positive_control": "Extra declared source-indicator row; physical availability not inferred",
            "scale_laws": tuple(scale_laws)}


def retained_energy_obstruction(cache):
    section = "RETAINED_POINTWISE_ENERGY_OBSTRUCTION"
    first_low_null = cache["low_null", "origin_16"][1].history[0]
    first_high_null = cache["high_null", "origin_16"][1].history[0]
    q_low_null = C.native.direct_qdd(first_low_null.source)
    q_high_null = C.native.direct_qdd(first_high_null.source)
    check(q_low_null.branch_weights[0] == ZERO
          and dict(first_low_null.deposit)[ORIGIN] == Q(59, 162)**2 > 0,
          section, "positive_first_slot_on_LOW_null_head")
    check(q_high_null.branch_weights[1] == ZERO
          and dict(first_high_null.deposit)[ORIGIN] == Q(187, 2430)**2 > 0,
          section, "same_positive_first_slot_on_HIGH_null_head")


def main():
    output = {}
    for section, action in (("SOURCE_AND_NATIVE_CENSUS", source_census),
                            ("TYPED_BOUNDARIES", typed_boundaries)):
        try:
            action()
        except Exception as exc:
            check(False, section, ("UNEXPECTED_EXCEPTION", type(exc).__name__, str(exc)))
    cache = None
    try:
        cache = chain_census()
    except Exception as exc:
        check(False, "COMPLETE_CHAIN", ("UNEXPECTED_EXCEPTION", type(exc).__name__, str(exc)))
    if cache is not None:
        for section, action in (
            ("STAGE_COMPOSITION", lambda: stage_composition_controls(cache)),
            ("RECORD_FORGERY_CONTROLS", lambda: record_forgery_controls(cache)),
            ("ONCE_SAMPLED_ENSEMBLE", lambda: ensemble_controls(cache)),
            ("RETAINED_POINTWISE_ENERGY_OBSTRUCTION", lambda: retained_energy_obstruction(cache)),
        ):
            try:
                result = action()
                if result is not None:
                    output[section] = result
            except Exception as exc:
                check(False, section, ("UNEXPECTED_EXCEPTION", type(exc).__name__, str(exc)))
    try:
        output["ACTUAL_CHAIN_IDENTIFIABILITY"] = identifiability_controls()
    except Exception as exc:
        check(False, "ACTUAL_CHAIN_IDENTIFIABILITY", ("UNEXPECTED_EXCEPTION", type(exc).__name__, str(exc)))
    output.update(name=NAME, counts=COUNTS, total=sum(COUNTS.values()), census=CENSUS,
                  failure_count=FAILURE_COUNT, failures=FAILURES, failure_list_cap=FAILURE_CAP,
                  result="PROOF_AUDIT_FAIL" if FAILURE_COUNT else "PROOF_AUDIT_PASS",
                  scope="Conditional rational TRC1 integration and finite ensemble identifiability; imported preparation law and fresh cold slots; no physical realization, occurrence derivation, renewal or Born promotion")
    print(json.dumps(json_value(output), sort_keys=True, ensure_ascii=True,
                     separators=(",", ":"), allow_nan=False))


if __name__ == "__main__":
    main()
