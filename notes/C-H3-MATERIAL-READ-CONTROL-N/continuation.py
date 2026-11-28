#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL #2139 A: unchanged continuation and funded causal controls.

The two full-column material donors are diagnostic boundary preparations.
They are not inserted into the A1 trajectories. All time labels are relative
to the source exchange at absolute full tick 114 unless explicitly marked.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib


MODEL = Path(__file__).with_name('model.py')
MODEL_SHA256 = '7b2f12553efe075e97a3814e68b6402690d1f66c389e1a6c45694aeccd91365d'
assert hashlib.sha256(MODEL.read_bytes()).hexdigest() == MODEL_SHA256
assert hashlib.sha256(Path(__file__).with_name('PREREG.md').read_bytes()).hexdigest() == (
    'dafa06568fe1a38f21c806ebeea694e5e635b151667045c5e6761498c7879981')
import model as M


START, END, OFFSET = 121, 1024, 114
PREFIX_DIGEST = 'fde15d156a9879098a6a93b3a3fe75b25b11f6c13f637eeb1f568e918a602060'
KEYS = tuple(M.KEYS)
INPUTS = tuple(product(range(5), repeat=2))
CONTROL_KEYS = tuple((old, fresh, a) for old, fresh in KEYS for a in range(2))
BANK_MATERIAL = frozenset(M.ix(4, y, r) for y in range(6) for r in (0, 1))


def field_key(p, fresh):
    return int(p == 1), fresh


def cell(f, y):
    return tuple(f[M.ix(4, y, r)] for r in range(4))


def radiation(f, y):
    return tuple(f[M.ix(4, y, r)] for r in (2, 3))


def exterior(f):
    """Every coordinate except the twelve bank material slots."""
    return tuple(z for i, z in enumerate(f) if i not in BANK_MATERIAL)


def event_map(events):
    result = {(x, y): tag for x, y, tag in events}
    assert len(result) == len(events)
    assert all(tag in (1, 2) for tag in result.values())
    return result


def tag_vector(events):
    e = event_map(events)
    return tuple(e.get((4, y), 0) for y in range(6))


def class_values(fields, feature, bit):
    values = [set(), set()]
    for k, f in fields.items():
        values[bit(k)].add(feature(f))
    return tuple(values)


def class_summary(fields, feature, bit):
    values = class_values(fields, feature, bit)
    return (len(values[0]), len(values[1]), len(values[0] & values[1]))


def clean_two(fields, feature, bit):
    return class_summary(fields, feature, bit) == (1, 1, 0)


def first_literal_difference(fields, feature, references):
    for key, f in fields.items():
        actual, expected = feature(f), references[key]
        if actual != expected:
            different = next(i for i, (a, b) in enumerate(zip(actual, expected)) if a != b)
            return key, different, expected[different], actual[different]
    return None


def freeze_losses(losses, t, stage, fields, sum_refs, old_refs, fresh_bit):
    for label, feature, refs in (
        ('literal_S0', M.sum0, sum_refs),
        ('literal_old', M.old_record, old_refs),
    ):
        if losses[label] is None:
            difference = first_literal_difference(fields, feature, refs)
            if difference is not None:
                losses[label] = (t, stage, difference)
    for label, feature, bit in (
        ('fresh_classes', M.sum0, fresh_bit),
        ('old_classes', M.old_record, lambda k: k[0]),
    ):
        if losses[label] is None:
            summary = class_summary(fields, feature, bit)
            if summary != (1, 1, 0):
                losses[label] = (t, stage, summary)


def predicate_tag(mids, outs, events, y, bit, old_refs):
    """A lesser tag classifier, with its unassumed readiness reported."""
    tags = [set(), set()]
    for key in outs:
        tags[bit(key)].add(event_map(events[key]).get((4, y), 0))
    if tags[0] != {0} or len(tags[1]) != 1 or 0 in tags[1]:
        return None
    incoming = {radiation(f, y) for f in mids.values()}
    outgoing = class_values(outs, lambda f: radiation(f, y), bit)
    common_old = all(M.old_record(f) == old_refs[k] for k, f in outs.items())
    strict_radiation = (len(outgoing[0]), len(outgoing[1]),
                        len(outgoing[0] & outgoing[1])) == (1, 1, 0)
    return dict(row=y, tag=next(iter(tags[1])), incoming_count=len(incoming),
                outgoing_class_counts=(len(outgoing[0]), len(outgoing[1])),
                outgoing_overlap=len(outgoing[0] & outgoing[1]),
                literal_old_at_full=common_old,
                strict_at_full=len(incoming) == 1 and strict_radiation and common_old,
                incoming=next(iter(incoming)) if len(incoming) == 1 else None,
                outgoing=tuple(next(iter(v)) for v in outgoing)
                if strict_radiation else None)


def find_readers(t, mids, outs, events, bit, old_refs, lesser, strict,
                 require_old_prefix=True):
    for y in range(6):
        witness = predicate_tag(mids, outs, events, y, bit, old_refs)
        if witness is None:
            continue
        witness = dict(relative=t, absolute=t + OFFSET, **witness)
        if lesser is None:
            lesser = witness
        if strict is None and witness['strict_at_full'] and require_old_prefix:
            strict = witness
    return lesser, strict


def advance_all(fields, t, accounts):
    mids, outs, events = {}, {}, {}
    for key, f in fields.items():
        mids[key], outs[key], events[key] = M.advance(f, t, accounts[key])
    return mids, outs, events


def a1(prefix, endpoints):
    audit_before = M.AUDIT.copy()
    fields = dict(endpoints)
    accounts = {k: M.account(f) for k, f in fields.items()}
    sum_refs = {k: M.sum0(f) for k, f in fields.items()}
    old_refs = {k: M.old_record(f) for k, f in fields.items()}
    fresh_bit = lambda k: int(k[1] == 1)
    assert clean_two(fields, M.sum0, fresh_bit)
    assert clean_two(fields, M.old_record, lambda k: k[0])
    losses = dict.fromkeys(('literal_S0', 'fresh_classes', 'literal_old', 'old_classes'))
    counts = {k: Counter() for k in KEYS}
    first_b = dict.fromkeys(KEYS)
    lesser = strict = None
    initial_compound = {}
    for p, fresh in INPUTS:
        k = field_key(p, fresh)
        stock = prefix['source_reserves'][p, fresh]
        initial_compound[p, fresh] = M.total_account(fields[k], matstock=stock)
    assert len(set(initial_compound.values())) == 1
    print('A1_COMMON_COMPOUND_ACCOUNT', next(iter(initial_compound.values())))
    for t in range(START + 1, END + 1):
        mids, fields, events = advance_all(fields, t, accounts)
        for stage, cut in (('post-C', mids), ('full', fields)):
            freeze_losses(losses, t, stage, cut, sum_refs, old_refs, fresh_bit)
        for k in KEYS:
            bank = tuple(e for e in events[k] if e[0] == 4)
            counts[k].update((y, tag) for _, y, tag in bank)
            if bank and first_b[k] is None:
                first_b[k] = (t, bank)
        lesser, strict = find_readers(t, mids, fields, events, fresh_bit,
                                     old_refs, lesser, strict)
    compound = []
    for p, fresh in INPUTS:
        k = field_key(p, fresh)
        stock = prefix['source_reserves'][p, fresh]
        assert M.total_account(fields[k], matstock=stock) == initial_compound[p, fresh]
        compound.append((fields[k], END % 2, stock))
    print('A1_LOSSES', losses)
    print('A1_FIRST_TAG_CLASSIFIER', lesser)
    print('A1_STRICT_NATURAL_READER', strict)
    for k in KEYS:
        print('A1_BANK', k, 'FIRST', first_b[k], 'COUNT', sum(counts[k].values()),
              'BY_ROW_TAG', tuple(sorted(counts[k].items())), 'END_SHA256', M.digest(fields[k]))
    weighted = sum(sum(counts[k].values()) * (1 if k[0] else 4) for k in KEYS)
    ticks = len(KEYS) * (END - START)
    audit = M.AUDIT - audit_before
    assert audit == Counter(ticks=ticks, checked_cuts=2 * ticks, two_sided_inverses=ticks)
    print('A1_COMPLETE', 'INPUTS', len(INPUTS), 'FIELD_REPRESENTATIVES', len(KEYS),
          'END_DISTINCT_FIELDS', len(set(fields.values())),
          'COMPOUND_STATES', len(set(compound)), 'BANK_B_INPUT_WEIGHTED', weighted,
          'CHECKED_NATIVE_TICKS', ticks, 'CHECKED_POST_C_CUTS', ticks,
          'CHECKED_FULL_CUTS', ticks, 'EXACT_NATIVE_INVERSE_TICKS', ticks,
          'END_FIELD_SHA256', M.digest([fields[k] for k in KEYS]),
          'END_COMPOUND_SHA256', M.digest(compound))
    print('A1_AUDIT', tuple(sorted(audit.items())),
          'INERT_SOURCE_RESERVES_EXACTLY_RETAINED', True)


def a2(prefix, endpoints):
    audit_before = M.AUDIT.copy()
    m0, m1 = M.material(endpoints[0, 0]), M.material(endpoints[0, 1])
    donors = (m0, m1)
    assert m0 != m1
    assert all(M.material(f) == donors[int(k[1] == 1)] for k, f in endpoints.items())
    fields, reserves, initial_compound = {}, {}, {}
    old_refs = {}
    boundary_count = 0
    for p, fresh in INPUTS:
        base_key = field_key(p, fresh)
        original = endpoints[base_key]
        source_stock = prefix['source_reserves'][p, fresh]
        before = M.total_account(original, matstock=source_stock + m0 + m1)
        for a in range(2):
            f, after_donors = M.swap_material(original, donors, a)
            assert M.swap_material(f, after_donors, a) == (original, donors)
            after_stock = source_stock + after_donors[0] + after_donors[1]
            assert M.total_account(f, matstock=after_stock) == before
            full_key, key = (p, fresh, a), base_key + (a,)
            if key in fields:
                assert fields[key] == f
            else:
                fields[key] = f
            reserves[full_key] = (source_stock, after_donors)
            initial_compound[full_key] = before
            old_refs[key] = M.old_record(original)
            assert M.old_record(f) == old_refs[key]
            boundary_count += 1
    assert set(fields) == set(CONTROL_KEYS)
    fields = {k: fields[k] for k in CONTROL_KEYS}
    accounts = {k: M.account(f) for k, f in fields.items()}
    assert len(set(initial_compound.values())) == 1
    print('A2_MATERIAL_DONORS', donors)
    print('A2_COMMON_COMPOUND_ACCOUNT', next(iter(initial_compound.values())))
    first_difference = dict.fromkeys(KEYS)
    first_old_loss = None
    lesser = strict = None
    paired_equal_full = paired_equal_mid = 0
    for base_key in KEYS:
        assert exterior(fields[base_key + (0,)]) == exterior(fields[base_key + (1,)])
    for t in range(START + 1, END + 1):
        mids, fields, events = advance_all(fields, t, accounts)
        for base_key in KEYS:
            if first_difference[base_key] is not None:
                continue
            k0, k1 = base_key + (0,), base_key + (1,)
            assert exterior(mids[k0]) == exterior(mids[k1])
            paired_equal_mid += 1
            tags0, tags1 = tag_vector(events[k0]), tag_vector(events[k1])
            if tags0 == tags1:
                assert exterior(fields[k0]) == exterior(fields[k1])
                paired_equal_full += 1
                continue
            rows = []
            for y in range(6):
                if tags0[y] == tags1[y]:
                    continue
                incoming = radiation(mids[k0], y)
                assert incoming == radiation(mids[k1], y)
                rows.append(dict(row=y, incoming=incoming, tags=(tags0[y], tags1[y]),
                                 outputs=(cell(fields[k0], y), cell(fields[k1], y)),
                                 radiation_differs=radiation(fields[k0], y) != radiation(fields[k1], y)))
            first_difference[base_key] = dict(relative=t, absolute=t + OFFSET,
                                              tag_vectors=(tags0, tags1), rows=tuple(rows))
        for stage, cut in (('post-C', mids), ('full', fields)):
            if first_old_loss is None:
                loss = first_literal_difference(cut, M.old_record, old_refs)
                if loss is not None:
                    first_old_loss = (t, stage, loss)
        lesser, strict = find_readers(t, mids, fields, events, lambda k: k[2],
                                     old_refs, lesser, strict,
                                     require_old_prefix=first_old_loss is None)
    compound = []
    for p, fresh in INPUTS:
        for a in range(2):
            key = field_key(p, fresh) + (a,)
            source_stock, after_donors = reserves[p, fresh, a]
            stock = source_stock + after_donors[0] + after_donors[1]
            assert M.total_account(fields[key], matstock=stock) == initial_compound[p, fresh, a]
            compound.append((fields[key], END % 2, source_stock, after_donors))
    for key in KEYS:
        print('A2_FIRST_TAG_DIFFERENCE', key, first_difference[key])
    print('A2_FIRST_LITERAL_OLD_LOSS', first_old_loss)
    print('A2_FIRST_TAG_CLASSIFIER', lesser)
    print('A2_STRICT_COMMON_CONTROL_READER', strict)
    for key in CONTROL_KEYS:
        print('A2_END_FIELD', key, M.digest(fields[key]))
    ticks = len(CONTROL_KEYS) * (END - START)
    audit = M.AUDIT - audit_before
    assert audit == Counter(ticks=ticks, checked_cuts=2 * ticks,
                            two_sided_inverses=ticks, material_swaps=2 * boundary_count)
    print('A2_COMPLETE', 'INPUT_DONOR_ARMS', len(compound),
          'FIELD_REPRESENTATIVES', len(CONTROL_KEYS),
          'END_DISTINCT_FIELDS', len(set(fields.values())),
          'COMPOUND_STATES', len(set(compound)),
          'SWAP_ACCOUNT_AND_INVERSE_CHECKS', boundary_count,
          'PAIRED_EQUAL_POST_C_CHECKS', paired_equal_mid,
          'PAIRED_EQUAL_FULL_CHECKS', paired_equal_full,
          'CHECKED_NATIVE_TICKS', ticks, 'CHECKED_POST_C_CUTS', ticks,
          'CHECKED_FULL_CUTS', ticks, 'EXACT_NATIVE_INVERSE_TICKS', ticks,
          'END_FIELD_SHA256', M.digest([fields[k] for k in CONTROL_KEYS]),
          'END_COMPOUND_SHA256', M.digest(compound))
    print('A2_AUDIT', tuple(sorted(audit.items())),
          'INERT_SOURCE_AND_DONOR_RESERVES_EXACTLY_RETAINED', True)


def main():
    prefix = M.prefix()
    M.print_prefix(prefix)
    endpoints = {k: prefix['second'][k][0][START] for k in KEYS}
    assert M.digest([endpoints[k] for k in KEYS]) == PREFIX_DIGEST
    assert len(prefix['source_reserves']) == len(INPUTS)
    print('A_PREFIX', 'PUBLIC_PREREG', '0fabe9ffdb8b387614344aa484589e3898bdb784',
          'ENDPOINT_SHA256', PREFIX_DIGEST, 'RELATIVE_START', START,
          'ABSOLUTE_START', OFFSET + START, 'RELATIVE_END', END,
          'ABSOLUTE_END', OFFSET + END)
    a1(prefix, endpoints)
    a2(prefix, endpoints)
    print('DONE NON-CANONICAL finite A continuation and funded material controls; no B verdict')


if __name__ == '__main__':
    main()
