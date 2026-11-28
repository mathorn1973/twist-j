#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL #2141 B. Frozen paid native-link census; no post-start action."""
from collections import Counter
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

SOURCE = Path(__file__).with_name('model.py')
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == (
    '7b2f12553efe075e97a3814e68b6402690d1f66c389e1a6c45694aeccd91365d')
spec = importlib.util.spec_from_file_location('native_link_basis', SOURCE)
M = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = M
spec.loader.exec_module(M)

F = (-3, -5, -4, 0)
ETAI = M.sub(M.O, M.RI)
ETA2 = M.mul(M.ETA, M.ETA)
RAD = tuple(i for i in range(192) if i % 4 >= 2)
WORK = tuple(M.ix(6, y, r) for y in range(6) for r in (0, 1))
CONTROLS = tuple((p, q, a) for p, q in M.ALL25 for a in (0, 1))
ACTUAL = tuple((p, q, int(q == 1)) for p, q in M.ALL25)
LABELS = tuple((mode, m, k) for mode, ms in
               (('SEALED', range(1, 9)), ('DRAIN', (1, 3, 5, 7)))
               for m in ms for k in range(5))


def emit(label, value):
    print(label, json.dumps(value, separators=(',', ':'), sort_keys=True))


def local(field):
    return M.cell(field, 6, 3)[:2]


def s6(field):
    return M.H.ring_sum(field[M.ix(6, y, 0)] for y in range(6))


def receipt(field):
    return M.cell(field, 6, 3)[2:]


def replacements(label):
    mode, m, k = label
    v = M.sc(m, M.P[k])
    b = M.sub(M.neg(M.mul(M.J, F)), M.sc(8, v))
    w = M.mul(ETA2, v)
    d = M.neg(M.mul(M.J, w))
    radio = {}
    for x in range(8):
        for y in range(6):
            radio[M.ix(x, y, 2)] = F if x == 4 else b if x == 6 else M.add(b, M.J)
            radio[M.ix(x, y, 3)] = b
    radio[M.ix(4, 3, 2)] = M.add(F, ETAI)
    radio[M.ix(4, 4, 2)] = M.add(F, M.add(M.O, M.RI))
    radio[M.ix(4, 3, 3)] = M.neg(M.add(F, ETAI))
    radio[M.ix(3, 3, 3)] = M.neg(M.add(F, M.add(M.O, M.RI)))
    cplus = M.add(b, M.mul(M.add(M.sc(2, M.O), M.R), w))
    if mode == 'DRAIN':
        radio[M.ix(7, 3, 3)] = radio[M.ix(0, 3, 3)] = M.add(cplus, M.sc(2, M.O))
    return dict(v=v, b=b, w=w, d=d, cplus=cplus,
                mat=(d, M.neg(d)) * 6, rad=tuple(radio[i] for i in RAD))


def assemble(field, matstock, stock):
    before = M.total_account(field, matstock + stock['mat'], stock['rad'])
    out = list(field)
    worker_out, rad_out = tuple(field[i] for i in WORK), tuple(field[i] for i in RAD)
    for i, z in zip(WORK, stock['mat']):
        out[i] = z
    for i, z in zip(RAD, stock['rad']):
        out[i] = z
    out = tuple(out)
    retained = (matstock + worker_out, rad_out)
    assert M.total_account(out, *retained) == before
    reverse = list(out)
    for i, z in zip(WORK, worker_out):
        reverse[i] = z
    for i, z in zip(RAD, rad_out):
        reverse[i] = z
    assert tuple(reverse) == field
    assert tuple(out[i] for i in WORK) == stock['mat']
    assert tuple(out[i] for i in RAD) == stock['rad']
    M.AUDIT['module_swaps'] += 1
    return out, retained, before


def prepare(data, stock):
    original = {key: data['second'][int(key[0] == 1), key[1]][0][107]
                for key in M.ALL25}
    donors = (M.material(original[0, 0]), M.material(original[0, 1]))
    fields, stocks, accounts = {}, {}, {}
    for key in CONTROLS:
        p, q, a = key
        source = data['source_reserves'][p, q]
        f, after = M.swap_material(original[p, q], donors, a)
        fields[key], stocks[key], accounts[key] = assemble(f, source + after[0] + after[1], stock)
        assert M.total_account(original[p, q], source + donors[0] + donors[1] + stock['mat'],
                               stock['rad']) == accounts[key]
    actual_stocks, actual_accounts = {}, {}
    for key in ACTUAL:
        p, q, a = key
        f, actual_stocks[key], actual_accounts[key] = assemble(
            original[p, q], data['source_reserves'][p, q], stock)
        assert f == fields[key]
    assert len(set(accounts.values())) == len(set(actual_accounts.values())) == 1
    assert {local(f) for f in fields.values()} == {(stock['d'], M.neg(stock['d']))}
    assert all(M.material(f, 6) == stock['mat'] for f in fields.values())
    assert all(tuple(f[i] for i in RAD) == stock['rad'] for f in fields.values())
    assert all(M.old_record(f) == M.old_record(original[key[:2]]) for key, f in fields.items())
    return fields, dict(CONTROL=stocks, ACTUAL=actual_stocks), dict(
        CONTROL=accounts, ACTUAL=actual_accounts)


def compressed_state(fields, keys, stocks, t):
    values = [fields[k] for k in keys]
    compound = [(fields[k], t % 2, stocks[k]) for k in keys]
    return dict(cases=len(keys), fields=len(set(values)), compounds=len(set(compound)),
                field_sha256=M.digest(values), compound_sha256=M.digest(compound))


def class_failure(fields, keys, feature, classifier):
    buckets = {}
    for key in keys:
        label, value = classifier(key), feature(fields[key])
        buckets.setdefault(label, {}).setdefault(value, key)
    split = next(((lab, vals) for lab, vals in sorted(buckets.items()) if len(vals) != 1), None)
    overlap = None
    prior = {}
    for lab, vals in sorted(buckets.items()):
        for value, key in vals.items():
            if value in prior:
                overlap = (prior[value], key)
                break
            prior[value] = key
        if overlap is not None:
            break
    if split is None and overlap is None:
        return None
    result = dict(kind=[name for name, flag in (('SPLIT', split), ('COLLISION', overlap)) if flag is not None],
                  counts=[(lab, len(vals)) for lab, vals in sorted(buckets.items())])
    if split is not None:
        lab, vals = split
        entries = list(vals.items())[:2]
        result['split_keys'] = [entry[1] for entry in entries]
        result['split_value_sha256'] = [M.digest(entry[0]) for entry in entries]
    if overlap is not None:
        result['collision_keys'] = overlap
    return result


def fresh_report():
    return dict(first_contact=None, buffer_transfer=None, receiver_write=None, prefix_old=None,
                local_literal=None, local_classes=None, local_joint=None,
                sum_literal=None, sum_classes=None, sum_joint=None,
                old_literal=None, old_classes=None, first_receiver_B=None, first_archive_B=None)


def check_equal(report, name, actual, expected, t, stage, key):
    if report[name] is None and actual != expected:
        report[name] = dict(t=t, stage=stage, key=key, actual=actual, expected=expected)


def run_label(data, label):
    stock = replacements(label)
    fields, stocks, compound_accounts = prepare(data, stock)
    groups = dict(ACTUAL=ACTUAL, CONTROL=CONTROLS)
    reports = {name: fresh_report() for name in groups}
    event_counts = {name: Counter() for name in groups}
    first_events = {name: Counter() for name in groups}
    repr_of, representatives = {}, {}
    for key, field in fields.items():
        repr_of[key] = representatives.setdefault(field, key)
    representative_keys = tuple(representatives.values())
    active_accounts = {key: M.account(fields[key]) for key in representative_keys}
    initial_states = {name: compressed_state(fields, keys, stocks[name], 107)
                      for name, keys in groups.items()}
    references = None
    received_states = None
    w, d, b, v = stock['w'], stock['d'], stock['b'], stock['v']
    for t in range(108, 143):
        mids0, next0, ev0 = {}, {}, {}
        for key in representative_keys:
            mids0[key], next0[key], ev0[key] = M.advance(fields[key], t, active_accounts[key])
        mids = {key: mids0[repr_of[key]] for key in CONTROLS}
        next_fields = {key: next0[repr_of[key]] for key in CONTROLS}
        events = {key: ev0[repr_of[key]] for key in CONTROLS}
        for name, keys in groups.items():
            report = reports[name]
            for key in keys:
                a = key[2]
                if t <= 110:
                    for event in events[key]:
                        first_events[name][(t,) + event] += 1
                    reference_old = M.old_record(data['second'][int(key[0] == 1), key[1]][1][t])
                    check_equal(report, 'prefix_old', M.old_record(mids[key]), reference_old, t, 'post-C', key)
                    reference_old = M.old_record(data['second'][int(key[0] == 1), key[1]][0][t])
                    check_equal(report, 'prefix_old', M.old_record(next_fields[key]), reference_old, t, 'full', key)
                if t == 108:
                    expected_mat = M.cell(data['second'][0, a][1][t], 4, 3)[:2]
                    check_equal(report, 'first_contact', M.cell(mids[key], 4, 3),
                                expected_mat + (F, M.neg(F)), t, 'post-C', key)
                    check_equal(report, 'first_contact',
                                (mids[key][M.ix(4, 4, 2)], mids[key][M.ix(3, 3, 3)]),
                                (M.add(F, M.sc(2, M.O)), M.neg(M.add(F, M.sc(2, M.O)))),
                                t, 'post-C-companions', key)
                    value = M.mul(M.J, F) if a else F
                    check_equal(report, 'first_contact',
                                (M.tag_at(events[key], 3), M.cell(next_fields[key], 4, 3)[2:]),
                                (2 if a else 0, (value, M.neg(value))), t, 'full', key)
                if t == 109:
                    value = M.add(b, M.sc(4, M.mul(M.ETA, v))) if a else b
                    check_equal(report, 'buffer_transfer',
                                (mids[key][M.ix(5, 3, 3)], next_fields[key][M.ix(5, 3, 3)],
                                 M.tag_at(events[key], 3, 5)), (value, value, 0), t, 'both', key)
                if t == 110:
                    incoming = M.add(b, M.sc(2, w)) if a else b
                    check_equal(report, 'receiver_write', M.cell(mids[key], 6, 3),
                                (d, M.neg(d), b, incoming), t, 'post-C', key)
                    expected = ((M.neg(w), w, M.sub(b, M.mul(M.R, w)), stock['cplus'])
                                if a else (d, M.neg(d), b, b))
                    check_equal(report, 'receiver_write',
                                (M.cell(next_fields[key], 6, 3), M.tag_at(events[key], 3, 6)),
                                (expected, 2 if a else 0), t, 'full', key)
                if t > 110:
                    for event in events[key]:
                        x, y, tag = event
                        if x == 6 or x in M.ARCH:
                            event_counts[name][(x, y, tag)] += 1
                            loss = 'first_receiver_B' if x == 6 else 'first_archive_B'
                            if report[loss] is None:
                                report[loss] = dict(t=t, key=key, event=event)
            if t > 110:
                for stage, view in (('post-C', mids), ('full', next_fields)):
                    for feature_name, feature in (('local', local), ('sum', s6), ('old', M.old_record)):
                        literal_name = feature_name + '_literal'
                        if report[literal_name] is None:
                            for key in keys:
                                observed, expected = feature(view[key]), references[feature_name][key]
                                if observed != expected:
                                    report[literal_name] = dict(t=t, stage=stage, key=key,
                                        value_sha256=M.digest(observed), reference_sha256=M.digest(expected))
                                    if feature_name != 'old':
                                        report[literal_name].update(value=observed, reference=expected)
                                    break
                        classifier = (lambda key: int(key[0] == 1)) if feature_name == 'old' else (lambda key: key[2])
                        failure = class_failure(view, keys, feature, classifier)
                        loss = feature_name + '_classes'
                        if failure is not None and report[loss] is None:
                            report[loss] = dict(t=t, stage=stage, **failure)
                        if feature_name != 'old':
                            joint_feature = lambda field, feature=feature: (M.old_record(field), feature(field))
                            failure = class_failure(view, keys, joint_feature,
                                                    lambda key: (int(key[0] == 1), key[2]))
                            loss = feature_name + '_joint'
                            if failure is not None and report[loss] is None:
                                report[loss] = dict(t=t, stage=stage, **failure)
        fields = next_fields
        if t == 110:
            references = {name: {key: feature(fields[key]) for key in CONTROLS}
                          for name, feature in (('local', local), ('sum', s6), ('old', M.old_record))}
            received_states = {name: compressed_state(fields, keys, stocks[name], t)
                               for name, keys in groups.items()}
            for name, keys in groups.items():
                for feature_name, feature in (('local', local), ('sum', s6), ('old', M.old_record)):
                    classifier = (lambda key: int(key[0] == 1)) if feature_name == 'old' else (lambda key: key[2])
                    failure = class_failure(fields, keys, feature, classifier)
                    if failure is not None:
                        reports[name][feature_name + '_classes'] = dict(t=t, stage='full', **failure)
                for feature_name, feature in (('local', local), ('sum', s6)):
                    failure = class_failure(fields, keys, lambda field, feature=feature:
                                            (M.old_record(field), feature(field)),
                                            lambda key: (int(key[0] == 1), key[2]))
                    if failure is not None:
                        reports[name][feature_name + '_joint'] = dict(t=t, stage='full', **failure)
    gates = {}
    for name, keys in groups.items():
        for key in keys:
            assert M.total_account(fields[key], *stocks[name][key]) == compound_accounts[name][key]
        r = reports[name]
        contacts = all(r[x] is None for x in ('first_contact', 'buffer_transfer', 'receiver_write', 'prefix_old'))
        gates[name] = dict(three_contacts=contacts)
        for feature_name in ('local', 'sum'):
            gates[name][feature_name] = contacts and all(r[x] is None for x in
                (feature_name + '_literal', feature_name + '_classes', feature_name + '_joint', 'old_classes'))
    initial_rad_h = M.H.ring_sum(M.H.h(z) for z in stock['rad'])
    incoming = dict(material_slots=12, radiation_slots=96,
                    Sm=M.H.ring_sum(stock['mat']), Sr=M.H.ring_sum(stock['rad']),
                    H=M.add(M.H.ring_sum(M.H.h(z) for z in stock['mat']), initial_rad_h),
                    Q=sum(M.q(z) for z in stock['mat'] + stock['rad']))
    result = dict(label=label, stock=incoming, v=v, b=b, dR=d,
                  common_compound={name: next(iter(ac.values())) for name, ac in compound_accounts.items()},
                  active_account_classes=sorted(set(active_accounts.values())),
                  initial=initial_states, received=received_states,
                  end={name: compressed_state(fields, keys, stocks[name], 142) for name, keys in groups.items()},
                  first_losses=reports, gates=gates,
                  first_events={name: sorted(c.items()) for name, c in first_events.items()},
                  successor_events={name: sorted(c.items()) for name, c in event_counts.items()},
                  receiver_values=[(d, M.neg(d)), (M.neg(w), w)],
                  receiver_sums=[M.sc(6, d), M.add(M.sc(6, d), M.mul(M.R, w))])
    emit('B_LABEL', result)
    return result


def main():
    print('NON-CANONICAL #2141 B; prepared full107 module; unchanged H3 afterward')
    data = M.prefix()
    M.print_prefix(data)
    assert len(LABELS) == 60
    results = [run_label(data, label) for label in LABELS]
    summary = {}
    for gate in ('three_contacts', 'local', 'sum'):
        passing = [r['label'] for r in results if all(r['gates'][name][gate] for name in ('ACTUAL', 'CONTROL'))]
        summary[gate] = dict(count=len(passing), labels=passing, first=passing[0] if passing else None)
    emit('B_CENSUS', summary)
    emit('B_AUDIT', sorted(M.AUDIT.items()))
    print('DONE candidate-C finite prepared link; no original-time-zero delivery or autonomous reset')


if __name__ == '__main__':
    main()
