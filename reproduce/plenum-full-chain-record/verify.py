#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact, result-exposed replay of the prepared full-chain plenum certificate.

No packet transition catalogue drives the evolution. A sparse dictionary holds
every replacement of the fixed alternating background. Each matching visits
every pair meeting that support; all omitted background pairs refuse.
"""

from functools import lru_cache
import hashlib
import json
from pathlib import Path


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
BIGJ = (1, 0, 1, 0)
DELTA = (-1, -1, -1, -1)
POINTER = (0, 0, 0, 1)
MM = (-8, -2, -4, -6)
MP = (-6, -4, -2, -8)
CUT = 196608
BLOCK = 8192
FIXTURE_SHA256 = '80a21b34b74b8c0bc5bf9e1c92782f8a4fdc2bc41c289029184d2ce33be2182c'


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def mul(x, y):
    coefficients = [0] * 7
    for i in range(4):
        for k in range(4):
            coefficients[i + k] += x[i] * y[k]
    for i in range(6, 3, -1):
        for k in range(1, 5):
            coefficients[i - k] -= coefficients[i]
    return tuple(coefficients[:4])


def power(x, n):
    result = ONE
    for _ in range(n):
        result = mul(result, x)
    return result


def hermitian(x):
    a, b, c, d = x
    return mul(x, (a - b, -b, d - b, c - b))


def qaccount(x):
    numerator = 5 * sum(a * a for a in x) - sum(x) ** 2
    need(numerator % 2 == 0, 'nonintegral half trace')
    return numerator // 2


def beta(site):
    return DELTA if site & 1 else ZERO


def bounded(x):
    need(all(-1000000 <= a <= 1000000 for a in x), 'coefficient bound')


@lru_cache(maxsize=16384)
def contact(x, y):
    # Memoization is only of this literal pair arithmetic, never of a packet
    # trajectory, clock block, endpoint, translation or classification.
    bounded(x)
    bounded(y)
    difference = sub(x, y)
    if any(a & 1 for a in difference):
        return x, y
    a, b, c, d = (v // 2 for v in difference)
    change = (d - c - a, -c - b, a - 2 * c, b - c - d)
    left, right = add(x, change), sub(y, change)
    bounded(left)
    bounded(right)
    return left, right


def step(field, parity):
    # Matching pairs are disjoint. Collect all anchors before modifying output.
    anchors = {site - ((site - parity) & 1) for site in field}
    result = field.copy()
    for left in sorted(anchors):
        right = left + 1
        x, y = contact(field.get(left, beta(left)), field.get(right, beta(right)))
        if x == beta(left):
            result.pop(left, None)
        else:
            result[left] = x
        if y == beta(right):
            result.pop(right, None)
        else:
            result[right] = y
    need(len(result) <= 10000, 'finite support bound')
    need(all(sum(value) % 5 == site % 2 for site, value in result.items()),
         'fixed-site residue')
    return result


def accounts(field):
    total, herm = ZERO, ZERO
    half_trace = 0
    for site, value in field.items():
        bounded(value)
        background = beta(site)
        total = add(total, sub(value, background))
        herm = add(herm, sub(hermitian(value), hermitian(background)))
        half_trace += qaccount(value) - qaccount(background)
    need(4 * herm[0] - sum(herm[1:]) == 2 * half_trace, 'full H/Q agreement')
    return [list(total), list(herm)]


def letter(index):
    need(index > 0, 'positive clock index')
    valuation = (index & -index).bit_length() - 1
    return int(valuation % 2 == 0)


def tile(seed):
    word = [seed]
    for _ in range(13):
        word = [value for bit in word for value in (1, 1 - bit)]
    need(len(word) == BLOCK, 'block length')
    return word


def encode(field):
    return [[site, list(value)] for site, value in sorted(field.items())]


def normalize(field):
    need(bool(field), 'empty outgoing field')
    anchor = min(field) & ~1
    return anchor, {site - anchor: value for site, value in field.items()}


def state_key(field):
    return tuple(sorted(field.items()))


def xpacket(positive, k):
    return neg(mul(mul(ONE if positive else JROOT, BIGJ), add(ONE, power(RHO, k))))


def initial(branch):
    field = {-23: POINTER, 49: xpacket(False, 0), 562: MM}
    if branch != 'ABSENT':
        field[1 if branch == 'WRITE' else -131073] = xpacket(True, 0)
    need(all(value != beta(site) for site, value in field.items()), 'input support')
    return field


def certify(field, direction, boundary, words):
    anchor, start = normalize(field)
    pending = [start]
    seen = {state_key(start)}
    rows = []
    maximum_span = 0
    row_ticks = 0
    for start in pending:
        for seed in (0, 1):
            current = start
            low, high = min(current), max(current)
            need(high - low <= 1024, 'initial span bound')
            maximum_span = max(maximum_span, high - low)
            for bit in words[seed]:
                current = step(current, bit)
                need(bool(current), 'outgoing field vanished')
                first, last = min(current), max(current)
                need(last - first <= 1024, 'per-tick span bound')
                maximum_span = max(maximum_span, last - first)
                low, high = min(low, first), max(high, last)
                row_ticks += 1
            shift, end = normalize(current)
            need(shift % 2 == 0 and direction * shift > 0, 'outward even displacement')
            need(anchor + low >= boundary + 2 if direction > 0
                 else anchor + high <= boundary - 2, 'intermediate support gap')
            rows.append({'state': encode(start), 'end': encode(end),
                         'letter': seed, 'shift': shift, 'min': low, 'max': high})
            key = state_key(end)
            if key not in seen:
                seen.add(key)
                need(len(seen) <= 16, 'closure state bound')
                pending.append(end)
    need(len(rows) == 2 * len(seen), 'both seeds for every reached state')
    return {'anchor': anchor, 'direction': direction, 'boundary': boundary,
            'states': len(seen), 'rows': rows}, maximum_span, row_ticks


def main():
    raw = Path(__file__).with_name('certificate.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest() == FIXTURE_SHA256, 'fixture custody')
    expected = json.loads(raw)
    need(expected['schema'] == 1, 'fixture schema')
    need([r['branch'] for r in expected['runs']] == ['WRITE', 'FAR', 'ABSENT'],
         'reference inventory')
    need(sub(MP, MM) == add(mul(BIGJ, (1, -1, 0, 0)), mul(BIGJ, (1, -1, 0, 0))),
         'receiver sum change')
    need(hermitian(MP) == hermitian(MM) == (72, 0, 44, 44), 'receiver H')
    need(qaccount(MM) == qaccount(MP) == 100, 'receiver Q')
    need(accounts(initial('WRITE')) == accounts(initial('FAR')), 'equal S/H inputs')
    words = (tile(0), tile(1))
    # Finite indexing audit complements the written all-block valuation proof.
    for block_index in range(1, 5):
        need(words[letter(block_index)] ==
             [letter((block_index - 1) * BLOCK + k) for k in range(1, BLOCK + 1)],
             'aligned clock block')
    clock = [letter(k) for k in range(2, CUT + 1)]
    runs = []
    full_ticks = closure_ticks = row_count = stationary_checks = maximum_span = 0
    for reference in expected['runs']:
        branch = reference['branch']
        field = initial(branch)
        before = accounts(field)
        for bit in clock:
            field = step(field, bit)
            full_ticks += 1
        after = accounts(field)
        need(after == before, 'complete endpoint accounts')
        stationary = {-21 if branch == 'WRITE' else -23: POINTER,
                      560: MP if branch == 'WRITE' else MM}
        for parity in (0, 1):
            need(step(stationary, parity) == stationary, 'stationary component')
            stationary_checks += 1
        left = {site: value for site, value in field.items() if site < -23}
        right = {site: value for site, value in field.items() if site > 560}
        need({**left, **stationary, **right} == field, 'complete component decomposition')
        components = []
        if branch != 'ABSENT':
            components.append((left, -1, min(stationary)))
        else:
            need(not left, 'absent writer')
        components.append((right, 1, 560))
        certificates = []
        for component, direction, boundary in components:
            certificate, span, ticks = certify(component, direction, boundary, words)
            certificates.append(certificate)
            maximum_span = max(maximum_span, span)
            closure_ticks += ticks
            row_count += len(certificate['rows'])
        run = {'h': 0, 'branch': branch, 'n0': 1, 'cut': CUT,
               'field': encode(field), 'initial_accounts': before,
               'final_accounts': after, 'certificates': certificates}
        need(run == reference, 'full endpoint or complete certificate mismatch: ' + branch)
        runs.append(run)
    need((full_ticks, row_count, closure_ticks, stationary_checks, maximum_span) ==
         (589821, 34, 278528, 6, 1), 'frozen evaluation inventory')
    scientific_bytes = json.dumps(runs, sort_keys=True, separators=(',', ':')).encode('ascii')
    summary = {'result': 'PASS', 'reference_histories': len(runs),
               'full_ticks': full_ticks, 'closure_rows': row_count,
               'closure_ticks': closure_ticks, 'stationary_matchings': stationary_checks,
               'max_closure_span': maximum_span,
               'computed_reference_sha256': hashlib.sha256(scientific_bytes).hexdigest(),
               'fixture_sha256': FIXTURE_SHA256}
    print(json.dumps(summary, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
