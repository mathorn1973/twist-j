#!/usr/bin/env python3
"""Independent matrix/chart audit for P-U-TWO-TRACE-PORT-CONTACTS-1.

Author: A. M. Thorn. License: Apache-2.0.
No primary or predecessor scientific program is imported.
Frozen before primary-code exposure and before scientific execution.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys


CHECKS = 0
RHO = (0, 0, 0, 0, 1, 0)
READY6 = (2, 1, 3, 4, 0, 4)
HOMOGENEOUS = (0, 0, 0, 0, 0, 0, 1)

# Coordinate order p1,p4,p1p,p4p,q,r,1. Each generator is a full
# homogeneous affine matrix, not a reduced table of target predicates.
GENERATORS = (
    (
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
        HOMOGENEOUS,
    ),
    (
        (0, 0, -1, 0, 0, 0, 0),
        (0, 0, 0, -1, 0, 0, 0),
        (-1, 0, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0, -1, 0),
        HOMOGENEOUS,
    ),
    (
        (0, 0, -1, 0, 0, 0, 2),
        (0, 0, 0, -1, 0, 1, 1),
        (-1, 0, 0, 0, 0, 0, 2),
        (0, -1, 0, 0, 0, -1, 1),
        (0, 0, 0, 0, -1, 0, 1),
        (0, 0, 0, 0, 0, -1, 0),
        HOMOGENEOUS,
    ),
    (
        (-1, 0, 0, 0, 0, 0, 2),
        (0, -1, 0, 0, 0, 0, 1),
        (0, 0, -1, 0, 0, 0, 3),
        (0, 0, 0, -1, 0, 0, 4),
        (0, 0, 0, 0, -1, 0, 1),
        (0, 0, 0, 0, 0, -1, 1),
        HOMOGENEOUS,
    ),
    (
        (-1, 0, 0, 0, 0, 0, 2),
        (0, -1, 0, 0, 0, 0, 1),
        (0, 0, -1, 0, 0, 0, 3),
        (0, 0, 0, -1, 0, 0, 4),
        (0, 0, 0, 0, -1, 0, 2),
        (0, 0, 0, 0, 0, -1, 1),
        HOMOGENEOUS,
    ),
)


def require(condition, reason):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(reason)


def apply(matrix, checkpoint):
    column = tuple(checkpoint) + (1,)
    result = tuple(sum(a*b for a, b in zip(row, column)) % 5
                   for row in matrix)
    require(result[-1] == 1, 'homogeneous coordinate')
    return result[:-1]


def theta(counter):
    return format(counter, 'b').count('1') % 2


def trace(checkpoint):
    return sum(checkpoint) % 5


def native(checkpoint, counter):
    index = (trace(checkpoint) + 2*theta(counter)) % 5
    return apply(GENERATORS[index], checkpoint), index


def to_chart(source, checkpoint):
    return (source, trace(checkpoint), *checkpoint[:4], checkpoint[5])


def from_chart(chart):
    source, z, p1, p4, p1p, p4p, r = chart
    piston = (p1, p4, p1p, p4p)
    return source, piston + ((z-sum(piston)-r) % 5, r)


def exchange(source, checkpoint):
    chart = to_chart(source, checkpoint)
    return from_chart((chart[1], chart[0], *chart[2:]))


def pointer(checkpoint):
    return ((checkpoint[0] + checkpoint[2]) % 5)**2 % 5


def encoded_rows(rows):
    return (json.dumps(rows, separators=(',', ':')) + '\n').encode('utf-8')


def digest(rows):
    return hashlib.sha256(encoded_rows(rows)).hexdigest()


def simulate(a1, a2, contacts_enabled):
    sources = [(a1+1) % 5, (a2+1) % 5]
    receivers = [RHO, RHO]
    history, contacts, selectors = [], [], []
    for counter in range(10):
        history.append([a1, a2, counter, *sources,
                        *receivers[0], *receivers[1]])
        if counter == 9:
            break
        if contacts_enabled and counter in (0, 6):
            address = 0 if counter == 0 else 1
            old_source, old_receiver = sources[address], receivers[address]
            sources[address], receivers[address] = exchange(
                old_source, old_receiver)
            contacts.append([a1, a2, counter, old_source, sources[address],
                             *old_receiver, *receivers[address]])
        indices = []
        for address in (0, 1):
            receivers[address], index = native(receivers[address], counter)
            indices.append(index)
        selectors.append([a1, a2, counter, *indices])
    return history, contacts, selectors


def main():
    primitive_states = 0
    retention_cases = 0
    for checkpoint in itertools.product(range(5), repeat=6):
        for source in range(5):
            chart = to_chart(source, checkpoint)
            require(from_chart(chart) == (source, checkpoint), 'chart inverse')
            outgoing, changed = exchange(source, checkpoint)
            require(exchange(outgoing, changed) == (source, checkpoint),
                    'full primitive involution')
            require(outgoing == trace(checkpoint) and trace(changed) == source,
                    'source and native trace exchanged')
            require(changed[:4] == checkpoint[:4] and changed[5] == checkpoint[5],
                    'unchanged piston and r')
            require(all(0 <= x < 5 for x in (outgoing, *changed)),
                    'canonical primitive output')
            primitive_states += 1
        if trace(checkpoint) in (1, 4):
            for bit in (0, 1):
                index = (trace(checkpoint) + 2*bit) % 5
                changed = apply(GENERATORS[index], checkpoint)
                require(index in (1, 3, 4), 'stable native generator class')
                require(trace(changed) == (4 if bit == 0 else 1),
                        'stable trace closure')
                require((changed[0]+changed[2]) % 5 ==
                        -(checkpoint[0]+checkpoint[2]) % 5, 'A negation')
                require(pointer(changed) == pointer(checkpoint), 'W retained')
                retention_cases += 1
    require(primitive_states == 78125, 'complete primitive domain')
    require(retention_cases == 12500, 'complete X14 times two controls')
    require([theta(n) for n in range(3)] == [0, 1, 1], 'first clock block')
    require([theta(n) for n in range(6, 9)] == [0, 1, 1], 'second clock block')

    histories, contacts, selectors, control_histories = [], [], [], []
    by_input = {}
    failed_control_pairs = 0
    for a1, a2 in itertools.product(range(5), repeat=2):
        h, c, j = simulate(a1, a2, True)
        by_input[(a1, a2)] = h
        histories.extend(h)
        contacts.extend(c)
        selectors.extend(j)
        require(len(c) == 2 and len(j) == 9, 'fixed operation counts')
        require(len(h) == 10 and all(len(row) == 17 for row in h),
                'complete boundary state')
        require(all(len(row) == 17 for row in c), 'complete exchange state')
        for row in h:
            n, s1, s2 = row[2:5]
            r1, r2 = tuple(row[5:11]), tuple(row[11:17])
            require(all(0 <= x < 5 for x in row[3:]), 'canonical protocol state')
            require(s1 == ((a1+1) % 5 if n == 0 else 1), 'first source account')
            require(s2 == ((a2+1) % 5 if n <= 6 else 4), 'second source account')
            if n >= 3:
                require(pointer(r1) == int(a1 == 4), 'first record retained')
                require(trace(r1) in (1, 4), 'first record in protected sheet')
            if n == 6:
                require(r2 == READY6, 'complete freely evolved second readiness')
            if n >= 9:
                require(pointer(r2) == int(a2 == 4), 'second record complete')
                require(trace(r2) in (1, 4), 'second record in protected sheet')
        no, empty, unused = simulate(a1, a2, False)
        control_histories.extend(no)
        require(not empty and len(unused) == 9, 'control has no contact')
        for row in no:
            require(row[3:5] == [(a1+1) % 5, (a2+1) % 5],
                    'control keeps both source ports')
            require(pointer(row[5:11]) == pointer(row[11:17]) == 0,
                    'control never writes either pointer')
        failed_control_pairs += ((pointer(no[-1][5:11]), pointer(no[-1][11:17]))
                                 != (int(a1 == 4), int(a2 == 4)))
    require(failed_control_pairs == 9, 'control fails all pairs containing four')
    for a1, a2 in itertools.product(range(5), repeat=2):
        for n in range(10):
            row = by_input[(a1, a2)][n]
            require(row[5:11] == by_input[(a1, 0)][n][5:11],
                    'first entire receiver independent of source two')
            require(row[11:17] == by_input[(0, a2)][n][11:17],
                    'second entire receiver independent of source one')
            if n <= 6:
                require(row[11:17] == by_input[(0, 0)][n][11:17],
                        'second receiver independent of both sources before contact')
    for n in (3, 9):
        require(by_input[(0, 0)][n][2:] == by_input[(1, 0)][n][2:],
                'known collision of complete enlarged states retained')
    require(len(histories) == 250 and len(contacts) == 50 and len(selectors) == 225,
            'shared complete history counts')
    result = dict(status='PASS', input_pairs=25, history_rows=len(histories),
                  contact_rows=len(contacts), history_sha256=digest(histories),
                  contact_sha256=digest(contacts), primitive_states=primitive_states,
                  retention_cases=retention_cases, selector_rows=len(selectors),
                  selector_sha256=digest(selectors), native_cell_steps=450,
                  control_failed_pairs=failed_control_pairs,
                  control_history_sha256=digest(control_histories), assertions=CHECKS)
    evidence = os.environ.get('TWISTJ_EVIDENCE_DIR')
    if evidence:
        destination = Path(evidence) / 'independent'
        destination.mkdir(parents=True, exist_ok=False)
        artifacts = {'HISTORIES.json': histories, 'CONTACTS.json': contacts,
                     'SELECTORS.json': selectors, 'CONTROL-HISTORIES.json': control_histories,
                     'SUMMARY.json': result}
        for name, rows in artifacts.items():
            data = encoded_rows(rows)
            if len(data) >= 5*1024*1024:
                raise AssertionError('evidence bound')
            (destination/name).write_bytes(data)
    sys.stdout.buffer.write(encoded_rows(result))


if __name__ == '__main__':
    main()
