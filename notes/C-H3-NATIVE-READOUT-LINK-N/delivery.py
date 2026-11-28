#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL #2141 A: exact endpoint pullback and common preparation.

No backward state is assumed to have the prescribed source inventory. The
source boundary is inverted as an actual slot swap, and its recovered input
is scored separately. Later feasible full-cut preparations are diagnostics;
they do not pass the original-start gate. The old endpoint probe reserve is
not imposed on a different early preparation.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
MODEL_SHA256 = '7b2f12553efe075e97a3814e68b6402690d1f66c389e1a6c45694aeccd91365d'
PREREG_SHA256 = '31baa223b9bc63c97a72d229f0f40f08b474565a89d4d38746de7847785f8370'
assert hashlib.sha256((HERE / 'model.py').read_bytes()).hexdigest() == MODEL_SHA256
assert hashlib.sha256((HERE / 'PREREG-A.md').read_bytes()).hexdigest() == PREREG_SHA256
import model as M


INPUTS = tuple(product(range(5), repeat=2))
FIELD_KEYS = tuple(M.KEYS)
CANDIDATES = ((107, 3, 2), (107, 3, 1), (93, 0, 2),
              (93, 0, 1), (89, 0, 2), (89, 0, 1))
NATIVE_SIZE = 8 * 6 * 4
MATERIAL = tuple(i for i in range(NATIVE_SIZE) if i % 4 < 2)
RADIATION = tuple(i for i in range(NATIVE_SIZE) if i % 4 >= 2)
SOURCE_MATERIAL = tuple(M.ix(0, y, r) for y, r in product(range(6), (0, 1)))
SOURCE_SWAP = tuple(M.ix(0, y, r) for y, r in product(range(0, 6, 2), (0, 1)))
BANK_MATERIAL = tuple(M.ix(4, y, r) for y, r in product(range(6), (0, 1)))
ARCHIVE_MATERIAL = tuple(M.ix(x, y, r)
                         for x, y, r in product((5, 7), range(6), (0, 1)))
AUDIT = Counter()


def emit(label, value):
    print('DELIVERY', label, json.dumps(value, sort_keys=True,
                                       separators=(',', ':'), ensure_ascii=True))


def field_key(case):
    p, fresh = case
    return int(p == 1), fresh


def coordinate(i):
    return i // 24, (i % 24) // 4, i % 4


def ordered_digest(fields):
    return M.digest([fields[k] for k in INPUTS])


def stock_account(values, material=False):
    total = M.H.ring_sum(values)
    hermitian = M.H.ring_sum(M.H.h(z) for z in values)
    scalar = sum(M.q(z) for z in values)
    assert scalar == M.H.scalar_account(hermitian)
    return (total, M.Z, hermitian, scalar) if material else (M.Z, total, hermitian, scalar)


def account_groups(accounts):
    groups = {}
    for case in INPUTS:
        groups.setdefault(accounts[case], []).append(case)
    return [dict(account=ac, inputs=cases) for ac, cases in groups.items()]


def first_difference(actual, expected, indices):
    """Input order is lexicographic (p,q); each input uses raw coordinate order."""
    for case in INPUTS:
        for i in indices:
            if actual[case][i] != expected[case][i]:
                return dict(input=case, raw_index=i, coordinate=coordinate(i),
                            expected=expected[case][i], actual=actual[case][i])
    return None


def cut_failure(actual, expected, indices, segment, tick, stage):
    result = first_difference(actual, expected, indices)
    if result is not None:
        result = dict(segment=segment, tick=tick,
                      absolute=tick if segment == 'first' else 114 + tick,
                      stage=stage, **result)
    return result


def first_failure(records):
    return next((record for record in records if record is not None), None)


def inverse_step(out, tick, ac):
    """Recover the matching bit, undo B, then undo the actual integral C."""
    bit_after = tick % 2
    bit_before = 1 - bit_after
    mid, _ = M.H.collide(out, M.NY)
    previous = M.H.transport(mid, M.NY, bit_before, True)
    forward_mid = M.H.transport(previous, M.NY, bit_before)
    forward_out, forward_events = M.H.collide(forward_mid, M.NY)
    assert forward_mid == mid and forward_out == out
    assert M.H.collide(forward_out, M.NY)[0] == mid
    assert M.H.transport(forward_mid, M.NY, bit_before, True) == previous
    assert M.account(mid) == ac and M.account(previous) == ac
    assert bit_after == 1 - bit_before
    AUDIT['inverse_ticks'] += 1
    AUDIT['two_sided_native_compositions'] += 1
    AUDIT['inverse_cut_account_checks'] += 2
    return previous, mid, forward_events


def pullback(target, last_tick):
    full = [None] * (last_tick + 1)
    mids = [None] * (last_tick + 1)
    events = [None] * (last_tick + 1)
    full[last_tick] = target
    ac = M.account(target)
    AUDIT['inverse_seed_account_checks'] += 1
    AUDIT['inverse_histories'] += 1
    for tick in range(last_tick, 0, -1):
        full[tick - 1], mids[tick], events[tick] = inverse_step(full[tick], tick, ac)
    return full, mids, events


def radiation_swap(field, indices, incoming):
    """A whole-slot swap retaining the ordered outgoing radiation inventory."""
    assert len(indices) == len(incoming) and len(set(indices)) == len(indices)
    assert all(i in RADIATION for i in indices)
    outgoing = tuple(field[i] for i in indices)
    result = list(field)
    for i, value in zip(indices, incoming):
        result[i] = value
    result = tuple(result)
    assert M.total_account(field, radstock=incoming) == M.total_account(result, radstock=outgoing)
    reverse = list(result)
    for i, value in zip(indices, outgoing):
        reverse[i] = value
    assert tuple(reverse) == field and tuple(result[i] for i in indices) == incoming
    AUDIT['radiation_swap_account_and_inverse_checks'] += 1
    return result, outgoing


def undo_source_exchange(after, retained_p):
    """Always invert the swap; q-compatibility is a later scientific test."""
    recovered = tuple(after[i] for i in SOURCE_SWAP)
    before = list(after)
    for i, value in zip(SOURCE_SWAP, retained_p):
        before[i] = value
    before = tuple(before)
    assert M.total_account(after, matstock=retained_p) == M.total_account(before, matstock=recovered)
    forward = list(before)
    for i, value in zip(SOURCE_SWAP, recovered):
        forward[i] = value
    assert tuple(forward) == after
    assert tuple(before[i] for i in SOURCE_SWAP) == retained_p
    AUDIT['source_swap_account_and_inverse_checks'] += 1
    return before, recovered


def common_preparation(pulled, baseline, source_stocks):
    """Exact minimal-support criterion, independent of boundary compatibility.

The supplied source_stocks are the prescribed q stocks for original full0,
or the retained p stocks for a later second-run cut. A passing field-only
criterion does not assert that the backward-recovered q stocks equal them.
"""
    assert tuple(pulled) == tuple(baseline) == INPUTS
    support = tuple(i for i in RADIATION
                    if any(pulled[k][i] != baseline[k][i] for k in INPUTS))
    material_failure = first_difference(pulled, baseline, MATERIAL)
    noncommon = None
    for i in support:
        values = tuple(pulled[k][i] for k in INPUTS)
        if len(set(values)) != 1:
            noncommon = dict(raw_index=i, coordinate=coordinate(i),
                             values=tuple((k, pulled[k][i]) for k in INPUTS))
            break
    result = dict(passes=material_failure is None and noncommon is None,
                  support_size=len(support), first_material_disagreement=material_failure,
                  first_noncommon_radiation=noncommon)
    if not result['passes']:
        return result, None
    incoming = tuple(pulled[INPUTS[0]][i] for i in support)
    outgoing_stocks, totals = {}, {}
    for case in INPUTS:
        out, outgoing = radiation_swap(baseline[case], support, incoming)
        assert out == pulled[case]
        before_account = M.total_account(baseline[case], matstock=source_stocks[case],
                                         radstock=incoming)
        after_account = M.total_account(out, matstock=source_stocks[case], radstock=outgoing)
        assert before_account == after_account
        outgoing_stocks[case] = outgoing
        totals[case] = before_account
        AUDIT['common_preparation_compound_checks'] += 1
    assert len(set(totals.values())) == 1
    result.update(raw_indices=support, S=tuple(coordinate(i) for i in support),
                  incoming=incoming, incoming_stock_account=stock_account(incoming),
                  complete_account=totals[INPUTS[0]],
                  outgoing_stock_accounts=account_groups({k: stock_account(outgoing_stocks[k])
                                                         for k in INPUTS}),
                  outgoing_stocks_sha256=M.digest([outgoing_stocks[k] for k in INPUTS]))
    return result, outgoing_stocks


def history_fields(histories, stage, tick):
    return {k: histories[k][stage][tick] for k in INPUTS}


def path_failures(pulled, baseline, indices, segment, end):
    """Ordered cuts: full0, post-C1, full1, ..., post-Cend, fullend."""
    failures = [cut_failure(history_fields(pulled, 0, 0),
                            history_fields(baseline, 0, 0), indices, segment, 0, 'full')]
    for tick in range(1, end + 1):
        for stage, name in ((1, 'post-C'), (0, 'full')):
            failures.append(cut_failure(history_fields(pulled, stage, tick),
                                        history_fields(baseline, stage, tick),
                                        indices, segment, tick, name))
    return failures


def probe_targets(prefix, label):
    start, row, tag = label
    tau = start + 1
    representative = prefix['second'][0, 1][1][tau]
    a, b = tuple(representative[M.ix(4, row, r)] for r in (0, 1))
    difference = M.sub(a, b)
    assert M.H.even(difference) and difference != M.Z
    d = M.H.half(difference)
    f = M.mul(M.JI if tag == 2 else M.J, d)
    partner = (row + 1) % 6 if row % 2 else (row - 1) % 6
    slots = (M.ix(4, row, 2), M.ix(4, partner, 2), M.ix(4, row, 3), M.ix(3, row, 3))
    incoming = (f, f, M.neg(f), M.neg(f))
    targets, old_probe_reserves = {}, {}
    for key in FIELD_KEYS:
        ref = prefix['second'][key][0][start]
        targets[key], old_probe_reserves[key] = radiation_swap(ref, slots, incoming)
        assert tuple(targets[key][i] for i in MATERIAL) == tuple(ref[i] for i in MATERIAL)
        ref_mid = prefix['second'][key][1][tau]
        material_pair = tuple(ref_mid[M.ix(4, row, r)] for r in (0, 1))
        _, actual_tag = M.H.collision(material_pair + (f, M.neg(f)))
        assert actual_tag == (tag if key[1] == 1 else 0)
        AUDIT['known_endpoint_local_checks'] += 1
    endpoint_accounts = {}
    for case in INPUTS:
        key = field_key(case)
        endpoint_accounts[case] = M.total_account(targets[key],
                                                 matstock=prefix['source_reserves'][case],
                                                 radstock=old_probe_reserves[key])
    assert len(set(endpoint_accounts.values())) == 1
    emit('TARGET', dict(label=label, read_tick=tau, f=f,
                       original_endpoint_probe_slots=tuple(coordinate(i) for i in slots),
                       original_endpoint_probe_stock_account=stock_account(incoming),
                       original_endpoint_compound_account=endpoint_accounts[INPUTS[0]],
                       old_probe_reserve_is_not_an_early_preparation_constraint=True))
    return targets


def candidate(prefix, label):
    audit_before = AUDIT.copy()
    start, row, tag = label
    targets_by_key = probe_targets(prefix, label)
    second_by_key = {k: pullback(targets_by_key[k], start) for k in FIELD_KEYS}
    second = {k: second_by_key[field_key(k)] for k in INPUTS}
    baseline_second = {k: prefix['second'][field_key(k)] for k in INPUTS}
    baseline_first = {k: prefix['first'][k[0]] for k in INPUTS}
    baseline_initial = {k: prefix['starts'][k[0]] for k in INPUTS}
    prescribed_q = {k: M.source_reserve(k[1]) for k in INPUTS}
    retained_p = {k: prefix['source_reserves'][k] for k in INPUTS}
    targets = {k: targets_by_key[field_key(k)] for k in INPUTS}
    after_exchange = history_fields(second, 0, 0)
    before_exchange, recovered_q, first = {}, {}, {}
    for case in INPUTS:
        before_exchange[case], recovered_q[case] = undo_source_exchange(after_exchange[case],
                                                                        retained_p[case])
        first[case] = pullback(before_exchange[case], 114)
    initial = history_fields(first, 0, 0)
    mathematical_accounts = {}
    for case in INPUTS:
        mathematical_accounts[case] = M.total_account(initial[case], matstock=recovered_q[case])
        assert mathematical_accounts[case] == M.total_account(targets[case], matstock=retained_p[case])
        AUDIT['compound_pullback_account_checks'] += 1
    source_failures = [dict(input=k, prescribed_q=prescribed_q[k], recovered_q=recovered_q[k])
                       for k in INPUTS if recovered_q[k] != prescribed_q[k]]
    before_source_failure = cut_failure(before_exchange, history_fields(baseline_first, 0, 114),
                                        SOURCE_MATERIAL, 'first', 114, 'full-before-exchange')
    after_source_failure = cut_failure(after_exchange, history_fields(baseline_second, 0, 0),
                                       SOURCE_MATERIAL, 'second', 0, 'full-after-exchange')
    initial_criterion, initial_outgoing = common_preparation(initial, baseline_initial, prescribed_q)
    initial_criterion.update(cut=dict(segment='first', tick=0, absolute=0, stage='full'),
                             source_stock_interpretation='prescribed q; recovered q scored separately')
    emit('INITIAL_COMMON_PREPARATION', dict(label=label, criterion=initial_criterion))
    emit('SOURCE_BOUNDARY', dict(label=label, recovered_q_pass_count=25 - len(source_failures),
                                 recovered_q_failures=source_failures,
                                 first_source_material_before_failure=before_source_failure,
                                 first_source_material_after_failure=after_source_failure,
                                 all_mathematical_preimages_retained=True,
                                 mathematical_initial_compound_accounts=account_groups(mathematical_accounts)))

    bank_failures = path_failures(second, baseline_second, BANK_MATERIAL, 'second', start)
    archive_failures = path_failures(second, baseline_second, ARCHIVE_MATERIAL, 'second', start)
    material_second_failures = path_failures(second, baseline_second, MATERIAL, 'second', start)
    material_first_failures = path_failures(first, baseline_first, MATERIAL, 'first', 114)
    first_archive_114 = cut_failure(before_exchange, history_fields(baseline_first, 0, 114),
                                    ARCHIVE_MATERIAL, 'first', 114, 'full')
    strict_archive_failure = first_archive_114 or first_failure(archive_failures)
    strict_bank_failure = first_failure(bank_failures[2 * 89 - 1:])
    whole_prefix_failure = first_failure(material_first_failures) or first_failure(material_second_failures)
    gates = dict(initial_common_radiation_replacement=initial_criterion['passes'],
                 recovered_source_inventory_q=not source_failures,
                 original_source_material_before_exchange=before_source_failure is None,
                 original_source_material_after_exchange=after_source_failure is None,
                 archive_preservation=strict_archive_failure is None,
                 bank_material_89_through_s=strict_bank_failure is None)
    failed_clauses = tuple(name for name, passed in gates.items() if not passed)
    if not failed_clauses:
        assert initial_outgoing is not None
        for case in INPUTS:
            assert M.total_account(initial[case], matstock=prescribed_q[case],
                                   radstock=initial_outgoing[case]) == M.total_account(
                                       targets[case], matstock=retained_p[case],
                                       radstock=initial_outgoing[case])
            AUDIT['strict_delivery_compound_checks'] += 1
    emit('ORIGINAL_START_VERDICT', dict(label=label, passes=not failed_clauses, gates=gates,
                                        failed_clauses=failed_clauses,
                                        first_failed_clause=failed_clauses[0] if failed_clauses else None,
                                        first_archive_failure=strict_archive_failure,
                                        first_bank_failure=strict_bank_failure,
                                        stronger_whole_prefix_material_first_failure=whole_prefix_failure))

    later_passes = []
    for tick in range(start + 1):
        pulled = history_fields(second, 0, tick)
        reference = history_fields(baseline_second, 0, tick)
        criterion, outgoing = common_preparation(pulled, reference, retained_p)
        if not criterion['passes']:
            continue
        for case in INPUTS:
            assert M.total_account(pulled[case], matstock=retained_p[case],
                                   radstock=outgoing[case]) == M.total_account(
                                       targets[case], matstock=retained_p[case], radstock=outgoing[case])
            AUDIT['late_suffix_compound_checks'] += 1
        bank_failure = first_failure(bank_failures[2 * tick:])
        archive_failure = first_failure(archive_failures[2 * tick:])
        record = dict(tick=tick, absolute=114 + tick, lead=start - tick,
                      bank_preserved=bank_failure is None, bank_first_failure=bank_failure,
                      archive_preserved=archive_failure is None, archive_first_failure=archive_failure)
        later_passes.append(record)
        emit('LATER_COMMON_PREPARATION', dict(label=label, criterion=criterion, suffix=record))
    assert later_passes and later_passes[-1]['tick'] == start
    emit('LATER_SUMMARY', dict(label=label, passing_cuts=tuple(x['tick'] for x in later_passes),
                               earliest=later_passes[0], diagnostic_only=True))

    compounds_initial = [(initial[k], 0, recovered_q[k]) for k in INPUTS]
    compounds_endpoint = [(targets[k], start % 2, retained_p[k]) for k in INPUTS]
    hashes = dict(target_fields=ordered_digest(targets),
                  second_full0_fields=ordered_digest(after_exchange),
                  first_full114_before_exchange_fields=ordered_digest(before_exchange),
                  original_full0_preimage_fields=ordered_digest(initial),
                  original_full0_mathematical_compounds=M.digest(compounds_initial),
                  endpoint_field_and_source_compounds=M.digest(compounds_endpoint),
                  recovered_q_stocks=M.digest([recovered_q[k] for k in INPUTS]))
    counts = dict(ordered_inputs=25, second_replay_keys=len(FIELD_KEYS),
                  target_distinct_fields=len(set(targets.values())),
                  original_full0_distinct_fields=len(set(initial.values())),
                  original_full0_mathematical_compounds=len(set(compounds_initial)),
                  endpoint_field_and_source_compounds=len(set(compounds_endpoint)))
    audit = AUDIT - audit_before
    assert audit['inverse_ticks'] == 10 * start + 25 * 114
    assert audit['two_sided_native_compositions'] == audit['inverse_ticks']
    assert audit['inverse_cut_account_checks'] == 2 * audit['inverse_ticks']
    assert audit['inverse_histories'] == audit['inverse_seed_account_checks'] == 35
    assert audit['source_swap_account_and_inverse_checks'] == 25
    emit('CANDIDATE_COMPLETE', dict(label=label, strict_pass=not failed_clauses,
                                    hashes=hashes, counts=counts, audit=dict(sorted(audit.items()))))
    return not failed_clauses


def main():
    prefix = M.prefix()
    M.print_prefix(prefix)
    emit('CONTRACT', dict(prereg_commit='a52c0e68fccbde84210bc2c4d9de65844c3715a3',
                          clarification_commit='1c978d0acdcc9a9fef557b400b0ec48abc1f1437',
                          prereg_sha256=PREREG_SHA256, model_sha256=MODEL_SHA256,
                          candidates=CANDIDATES, input_order=INPUTS,
                          hash_encoding='compact JSON, no newline, four coefficients per slot',
                          first_failure_order='chronological cuts, then lexicographic input, then raw coordinate',
                          initial_matching_bit=0, source_exchange_absolute_full=114))
    results = []
    for label in CANDIDATES:
        results.append((label, candidate(prefix, label)))
    emit('COMPLETE', dict(verdicts=results, passing_count=sum(passed for _, passed in results),
                          native_prefix_audit=dict(sorted(M.AUDIT.items())),
                          pullback_audit=dict(sorted(AUDIT.items())),
                          scope='six exact active-field targets; later cuts do not pass original-start delivery'))


if __name__ == '__main__':
    main()
