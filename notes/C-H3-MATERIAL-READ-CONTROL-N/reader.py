#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL #2139 B: prepared delayed material reader, fixed family."""
from collections import Counter
from pathlib import Path
import hashlib
import importlib.util
import sys

SOURCE = Path(__file__).with_name('model.py')
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == (
    '7b2f12553efe075e97a3814e68b6402690d1f66c389e1a6c45694aeccd91365d')
spec = importlib.util.spec_from_file_location('material_read_model', SOURCE)
M = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = M
spec.loader.exec_module(M)


def target_pair(field, row):
    return M.cell(field, 4, row)[2:4]


def probe_load(field, start, row, f):
    assert start % 2 == 1
    partner = (row + 1 if row % 2 else row - 1) % 6
    indices = (M.ix(4, row, 2), M.ix(4, partner, 2),
               M.ix(4, row, 3), M.ix(3, row, 3))
    incoming = (f, f, M.neg(f), M.neg(f))
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
    M.AUDIT['probe_swaps'] += 1
    return result, outgoing, indices


def census(data):
    labels, passes, reasons = [], [], Counter()
    for start in range(119, 88, -2):
        tau = start + 1
        fields = {key: hh[0][start] for key, hh in data['second'].items()}
        mids = {key: hh[1][tau] for key, hh in data['second'].items()}
        donors = (M.material(fields[0, 0]), M.material(fields[0, 1]))
        assert all(M.material(field) == donors[int(key[1] == 1)] for key, field in fields.items())
        row_summary = []
        for row in range(6):
            plus = M.cell(mids[0, 1], 4, row)[:2]
            minus = M.cell(mids[0, 0], 4, row)[:2]
            assert all(M.cell(mid, 4, row)[:2] == (plus if key[1] == 1 else minus)
                       for key, mid in mids.items())
            difference = M.sub(*plus)
            for tag in (2, 1):
                if not M.H.even(difference) or difference == M.Z:
                    reason = 'POSITIVE_INELIGIBLE'
                    f, observed = None, None
                else:
                    dplus = tuple(a // 2 for a in difference)
                    f = M.mul(M.JI if tag == 2 else M.J, dplus)
                    observed = tuple(M.H.collision(M.cell(mids[key], 4, row)[:2] +
                                                 (f, M.neg(f)))[1] for key in M.KEYS)
                    assert all(observed[i] == tag for i, key in enumerate(M.KEYS) if key[1] == 1)
                    reason = 'PASS' if all(observed[i] == 0 for i, key in enumerate(M.KEYS)
                                           if key[1] != 1) else 'NEGATIVE_ACTIVE'
                record = (start, row, tag, reason, f, observed)
                labels.append(record)
                reasons[reason] += 1
                row_summary.append((row, tag, reason,
                                    None if observed is None else (observed[0], observed[1])))
                if reason == 'PASS':
                    passes.append((start, row, tag, f))
        print('B_CENSUS_ROW', start, row_summary)
    assert len(labels) == 192
    print('B_CENSUS', 'LABELS', len(labels), 'COUNTS', sorted(reasons.items()),
          'FULL_LABEL_SHA256', M.digest(labels), 'PASS_COUNT', len(passes))
    return passes[0] if passes else None


def make_runs(data, selected, controlled):
    start, row, tag, f = selected
    tau = start + 1
    expected_positive = M.mul(M.J if tag == 2 else M.JI, f)
    values = ((f, M.neg(f)), (expected_positive, M.neg(expected_positive)))
    old_fields = {key: data['second'][int(key[0] == 1), key[1]][0][start]
                  for key in M.ALL25}
    donors = (M.material(old_fields[0, 0]), M.material(old_fields[0, 1]))
    probe = (f, f, M.neg(f), M.neg(f))
    outputs, stocks, preaccounts, postaccounts, sides, strict = {}, {}, set(), set(), Counter(), True
    case_keys = tuple((p, new, a) for p, new in M.ALL25 for a in (0, 1)) if controlled else M.ALL25
    representatives = {}
    for key in case_keys:
        p, new = key[:2]
        a = key[2] if controlled else int(new == 1)
        original = old_fields[p, new]
        source = data['source_reserves'][p, new]
        stock_before = source + (donors[0] + donors[1] if controlled else ())
        before = M.total_account(original, stock_before, probe)
        preaccounts.add(before)
        if controlled:
            field, donor_after = M.swap_material(original, donors, a)
            material_stock = source + donor_after[0] + donor_after[1]
        else:
            field, material_stock = original, source
        field, outgoing, indices = probe_load(field, start, row, f)
        after = M.total_account(field, material_stock, outgoing)
        assert before == after
        mid, out, events = M.advance(field, tau)
        assert M.total_account(mid, material_stock, outgoing) == before
        assert M.total_account(out, material_stock, outgoing) == before
        expected_material_mid = data['second'][0, 1 if a else 0][1][tau]
        assert M.cell(mid, 4, row)[:2] == M.cell(expected_material_mid, 4, row)[:2]
        assert target_pair(mid, row) == (f, M.neg(f))
        observed_tag = M.tag_at(events, row)
        assert observed_tag == (tag if a else 0)
        assert target_pair(out, row) == values[a]
        old_reference = M.old_record(data['second'][int(p == 1), new][0][tau])
        old_ok = M.old_record(out) == old_reference
        strict = strict and old_ok
        for event in events:
            if event != (4, row, tag) or not a:
                sides[event] += 1
        outputs[key] = out
        stocks[key] = (material_stock, outgoing)
        postaccounts.add(M.account(out))
        representatives.setdefault(a, (key, M.cell(mid, 4, row), M.cell(out, 4, row),
                                        M.sum0(out), events, old_ok))
    assert len(preaccounts) == 1
    classify_data = (lambda k: k[2]) if controlled else (lambda k: int(k[1] == 1))
    classify_old = lambda k: int(k[0] == 1)
    radio_classes = M.clean_classes(outputs, lambda field: target_pair(field, row), classify_data)
    old_classes = M.clean_classes(outputs, M.old_record, classify_old)
    joint_classes = M.clean_classes(outputs, lambda field: (M.old_record(field), target_pair(field, row)),
                                    lambda k: (classify_old(k), classify_data(k)))
    assert radio_classes
    strict = strict and old_classes and joint_classes
    name = 'CONTROL' if controlled else 'ACTUAL'
    print('B_READ', name, 'CASES', len(outputs), 'STRICT_PASS', strict,
          'RADIATION_CLASSES', radio_classes, 'OLD_CLASSES', old_classes,
          'JOINT_CLASSES', joint_classes, 'RADIATION_VALUES', values)
    print('B_ACCOUNT', name, 'COMMON_COMPOUND', next(iter(preaccounts)),
          'ACTIVE_FIELD_ACCOUNT_COUNT', len(postaccounts),
          'ACTIVE_FIELD_Q_VALUES', sorted({ac[3] for ac in postaccounts}),
          'PROBE_Q', 4 * M.q(f), 'PROBE_H', M.sc(4, M.H.h(f)),
          'DONOR_Q', sum(M.q(z) for z in donors[0] + donors[1]) if controlled else 0)
    print('B_REPRESENTATIVES', name, sorted(representatives.items()))
    print('B_SIDE_CONTACTS', name, sorted(sides.items()))
    print('B_READ_STATE', name, 'FIELD_DISTINCT', len(set(outputs.values())),
          'FIELD_SHA256', M.digest([outputs[k] for k in case_keys]),
          'COMPOUND_DISTINCT', len({(outputs[k], tau % 2, stocks[k]) for k in case_keys}),
          'COMPOUND_SHA256', M.digest([(outputs[k], tau % 2, stocks[k]) for k in case_keys]))
    return outputs, stocks, strict


def follow(outputs, stocks, selected, controlled):
    start, row, tag, f = selected
    tau = start + 1
    keys = tuple(outputs)
    references_radio = {k: target_pair(outputs[k], row) for k in keys}
    references_old = {k: M.old_record(outputs[k]) for k in keys}
    accounts = {k: M.account(outputs[k]) for k in keys}
    compound = {k: M.total_account(outputs[k], *stocks[k]) for k in keys}
    classify_data = (lambda k: k[2]) if controlled else (lambda k: int(k[1] == 1))
    classify_old = lambda k: int(k[0] == 1)
    losses = dict(literal_radiation=None, radiation_classes=None, literal_old=None,
                  old_classes=None, joint_classes=None, bank_B=None, archive_B=None)
    events_count = Counter()
    for t in range(tau + 1, tau + 33):
        mids, next_fields, eventsets = {}, {}, {}
        for key in keys:
            mid, out, events = M.advance(outputs[key], t, accounts[key])
            mids[key], next_fields[key], eventsets[key] = mid, out, events
            # Inert ordered stocks have not changed; their accounts add to each cut.
            assert M.total_account(mid, *stocks[key]) == compound[key]
            assert M.total_account(out, *stocks[key]) == compound[key]
        for stage, fields in (('post-C', mids), ('full', next_fields)):
            for key in keys:
                if losses['literal_radiation'] is None and target_pair(fields[key], row) != references_radio[key]:
                    losses['literal_radiation'] = (t, stage, key, target_pair(fields[key], row))
                if losses['literal_old'] is None and M.old_record(fields[key]) != references_old[key]:
                    losses['literal_old'] = (t, stage, key)
            for name, feature, classify in (
                ('radiation_classes', lambda field: target_pair(field, row), classify_data),
                ('old_classes', M.old_record, classify_old),
                ('joint_classes', lambda field: (M.old_record(field), target_pair(field, row)),
                 lambda key: (classify_old(key), classify_data(key)))):
                if losses[name] is None and not M.clean_classes(fields, feature, classify):
                    losses[name] = (t, stage)
        for key in keys:
            for event in eventsets[key]:
                x, y, event_tag = event
                if x == 4:
                    events_count['bank_B'] += 1
                    if losses['bank_B'] is None:
                        losses['bank_B'] = (t, key, event)
                if x in M.ARCH:
                    events_count['archive_B'] += 1
                    if losses['archive_B'] is None:
                        losses['archive_B'] = (t, key, event)
        outputs = next_fields
    name = 'CONTROL' if controlled else 'ACTUAL'
    print('B_SUCCESSOR', name, 'LAST_RELATIVE', tau + 32, 'LAST_ABSOLUTE', tau + 146,
          'SUBSEQUENT_TICKS', 32, 'FIRST_LOSSES', losses,
          'EVENT_COUNTS', sorted(events_count.items()))
    print('B_END_STATE', name, 'FIELD_DISTINCT', len(set(outputs.values())),
          'FIELD_SHA256', M.digest([outputs[k] for k in keys]),
          'COMPOUND_DISTINCT', len({(outputs[k], (tau + 32) % 2, stocks[k]) for k in keys}),
          'COMPOUND_SHA256', M.digest([(outputs[k], (tau + 32) % 2, stocks[k]) for k in keys]))
    for old in (0, 1):
        for data in (0, 1):
            selected_keys = [k for k in keys if classify_old(k) == old and classify_data(k) == data]
            print('B_END_FIBER', name, old, data, 'CASES', len(selected_keys),
                  'FIELD_DISTINCT', len({outputs[k] for k in selected_keys}))


def main():
    print('NON-CANONICAL #2139 B; prepared endpoint, not uninterrupted continuation')
    data = M.prefix()
    M.print_prefix(data)
    selected = census(data)
    print('B_SELECTED', selected)
    if selected is None:
        print('B_BOUNDED_NEGATIVE no candidate in the frozen192-label family')
        return
    start, row, tag, f = selected
    print('B_TIMING', 'START_RELATIVE', start, 'READ_RELATIVE', start + 1,
          'START_ABSOLUTE', start + 114, 'READ_ABSOLUTE', start + 115,
          'FULL_TICKS_AFTER_WRITE_BEFORE_LOAD', start - 89)
    passed = []
    for controlled in (False, True):
        outputs, stocks, strict = make_runs(data, selected, controlled)
        passed.append(strict)
        follow(outputs, stocks, selected, controlled)
    print('B_COMPLETE', 'STRICT_ACTUAL_AND_CONTROL', all(passed),
          'AUDIT', sorted(M.AUDIT.items()))
    print('DONE candidate-C finite stored-family reader; no native loader, summing circuit or permanence')


if __name__ == '__main__':
    main()
