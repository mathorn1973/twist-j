#!/usr/bin/env python3
"""NON-CANONICAL / L1: prospective audit of one fixed 95-contact compiler.
All seven common-stock elements and every contact are fixed symbolically.
Primary scalar arithmetic is reused by text; no predecessor is imported.
"""
from collections import Counter
import hashlib
import json
import sys

HEIGHTS = (-2, -1, 0, 1, 2)


PAIRS = tuple((a, b) for a in range(8) for b in range(a + 1, 8))
ZERO = (0, 0, 0, 0)
U = (1, -1, 0, 0)
B = (1, 0, -1, 0)
J = (1, 0, 1, 0)
X = (1, 1, 0, -2)
TWO = (2, 0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def scale(n, a):
    return tuple(n * x for x in a)


def rho(a):
    a0, a1, a2, a3 = a
    return (a3 - a2, -a2, a0 - a2, a1 - a2)


def mul(a, b):
    c = [0] * 7
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            c[i + k] += x * y
    for k in range(6, 3, -1):
        v = c[k]
        for d in range(1, 5):
            c[k - d] -= v
        c[k] = 0
    return tuple(c[:4])


def conjugate(a):
    a0, a1, a2, a3 = a
    return (a0 - a1, -a1, a3 - a1, a2 - a1)


def q(a):
    n = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert n % 2 == 0
    return n // 2


def hermitian(a):
    h = mul(a, conjugate(a))
    assert h[1] == 0 and h[2] == h[3]
    return (h[0], -h[2])


def invariants(state):
    total = ZERO
    ha = hb = account = 0
    for a in state:
        total = add(total, a)
        ah, bh = hermitian(a)
        ha += ah
        hb += bh
        account += q(a)
    assert account == 2 * ha + hb
    return (total, (ha, hb), account,
            tuple(sum(a) % 5 for a in state))


def contact(a, b):
    difference = tuple(x - y for x, y in zip(a, b))
    if any(x % 2 for x in difference):
        return a, b, False
    middle = tuple((x + y) // 2 for x, y in zip(a, b))
    d = rho(tuple(x // 2 for x in difference))
    return add(middle, d), add(middle, neg(d)), True


def initial(t):
    return (add(U, scale(t, B)), add(U, scale(-t, B)),
            ZERO, ZERO, X, TWO, J, neg(J))


def target(t):
    value = J
    for _ in range((t + 2) % 5):
        value = rho(value)
    return (value, neg(value))


TARGETS = tuple(target(t) for t in HEIGHTS)


ONE = (1, 0, 0, 0)
J_INVERSE = (0, -1, -1, 0)
JB = mul(J, B)
SEPARATOR_REFS = (U, add(U, neg(JB)), add(U, neg(B)))
TRANSFORMED_X = (add(U, neg(JB)), add(U, neg(B)), U,
                 add(U, rho(B)), add(U, rho(JB)))
MARKER_HEIGHTS = (-1, 0, 1, 2)
MARKER_REFS = tuple(neg(mul(mul(B, TRANSFORMED_X[t + 2]), J_INVERSE))
                    for t in MARKER_HEIGHTS)
STOCK = SEPARATOR_REFS + MARKER_REFS
SEPARATORS = ((0, 8), (0, 9), (0, 10))


def inv_word(word):
    return tuple(edge for edge in reversed(word) for _ in range(4))


def writer(p, gate=5, plus=6, minus=7):
    return (((gate, minus),) + ((plus, minus),) * (5 - p)
            + ((gate, minus),) * 4 + ((plus, minus),) * p)


def compiler_word():
    word = list(SEPARATORS)
    for offset, t in enumerate(MARKER_HEIGHTS):
        marker_port = 11 + offset
        marker = ((0, marker_port), (5, marker_port))
        word.extend(marker + writer(t + 2) + inv_word(marker))
    word.extend(inv_word(SEPARATORS))
    return tuple(word)


WORD = compiler_word()


def pair_invariants(a, b):
    ah, bh = hermitian(a), hermitian(b)
    return (add(a, b), (ah[0] + bh[0], ah[1] + bh[1]), q(a) + q(b),
            sum(a) % 5, sum(b) % 5)


class Audit:
    def __init__(self):
        self.cuts = 0
        self.accepted = 0
        self.refused = 0

    def apply(self, initial_state, word):
        state = list(initial_state)
        admissions = []
        for a, b in word:
            before = pair_invariants(state[a], state[b])
            state[a], state[b], accepted = contact(state[a], state[b])
            assert pair_invariants(state[a], state[b]) == before
            self.cuts += 1
            self.accepted += int(accepted)
            self.refused += int(not accepted)
            admissions.append('A' if accepted else 'R')
        return tuple(state), ''.join(admissions)


def run():
    assert mul(J, J_INVERSE) == ONE
    assert len(STOCK) == 7 and len(WORD) == 95
    assert all(0 <= a < 15 and 0 <= b < 15 and a != b for a, b in WORD)
    expected_parities = ((1, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0),
                         (0, 0, 0, 1), (1, 0, 1, 0))
    assert tuple(tuple(c % 2 for c in x) for x in TRANSFORMED_X) == expected_parities
    assert len(set(expected_parities)) == 5 and ZERO not in expected_parities
    for t, ref in zip(MARKER_HEIGHTS, MARKER_REFS):
        assert add(mul(B, TRANSFORMED_X[t + 2]), mul(J, ref)) == ZERO
        assert tuple(c % 2 for c in ref) == expected_parities[t + 2]

    audit = Audit()
    prepared = {}
    for t in HEIGHTS:
        state = initial(t) + STOCK
        prepared[t], _ = audit.apply(state, SEPARATORS)
        assert prepared[t][0] == TRANSFORMED_X[t + 2]
        assert prepared[t][5:8] == (TWO, J, neg(J))

    marker_checks = []
    for offset, selected in enumerate(MARKER_HEIGHTS):
        port = 11 + offset
        marker = ((0, port), (5, port))
        for t in HEIGHTS:
            marked, admissions = audit.apply(prepared[t], marker)
            if t == selected:
                assert admissions == 'AA'
                assert marked[port] == B and marked[5] == J
            else:
                assert admissions == 'RR'
                assert marked == prepared[t]
            restored, _ = audit.apply(marked, inv_word(marker))
            assert restored == prepared[t]
            marker_checks.append([selected, t, admissions])

    writer_checks = []
    for p in range(1, 5):
        word = writer(p, 0, 1, 2)
        assert len(word) == 10
        for phase in range(5):
            clock = target(phase - 2)
            before = (TWO,) + clock
            after, trace = audit.apply(before, word)
            assert after == before
            restored, _ = audit.apply(after, inv_word(word))
            assert restored == before
            writer_checks.append(['inactive', p, phase, trace])
        before = (J, J, neg(J))
        after, trace = audit.apply(before, word)
        assert after == (J,) + target(p - 2)
        restored, _ = audit.apply(after, inv_word(word))
        assert restored == before
        writer_checks.append(['active', p, 0, trace])

    endpoints = {}
    traces = {}
    account = {}
    for t in HEIGHTS:
        before = initial(t) + STOCK
        endpoint, trace = audit.apply(before, WORD)
        expected = list(before)
        expected[6:8] = target(t)
        assert endpoint == tuple(expected)
        assert invariants(endpoint) == invariants(before)
        restored, _ = audit.apply(endpoint, inv_word(WORD))
        assert restored == before
        endpoints[str(t)] = endpoint
        traces[str(t)] = trace
        account[str(t)] = invariants(before)[2]
    assert len(marker_checks) == 20 and len(writer_checks) == 24
    assert audit.cuts == 3790
    stock_h = (sum(hermitian(x)[0] for x in STOCK),
               sum(hermitian(x)[1] for x in STOCK))
    stock_sum = ZERO
    for x in STOCK:
        stock_sum = add(stock_sum, x)
    result = {
        'status': 'PASS', 'scope': 'NON-CANONICAL / L1 / exact five-height compiler audit',
        'clock_target_rule': 't+2', 'heights': list(HEIGHTS),
        'slots': 15, 'extra_common_slots': 7, 'contacts': len(WORD),
        'word_one_based': [[a + 1, b + 1] for a, b in WORD],
        'stock_four_coefficients': STOCK,
        'separator_refs_four_coefficients': SEPARATOR_REFS,
        'marker_refs_four_coefficients': MARKER_REFS,
        'separator_z_four_coefficients': (ZERO, ZERO, ZERO),
        'transformed_x_four_coefficients': TRANSFORMED_X,
        'transformed_x_parities': expected_parities,
        'stock_q': sum(q(x) for x in STOCK),
        'stock_h_coefficients': stock_h, 'stock_sum_four_coefficients': stock_sum,
        'complete_initial_q': account,
        'complete_final_states': endpoints,
        'forward_admission_traces': traces,
        'marker_checks': marker_checks, 'writer_checks': writer_checks,
        'checked_primitive_cuts': audit.cuts,
        'accepted_contacts': audit.accepted, 'refused_contacts': audit.refused,
        'restored_original_g_and_stock': True,
        'complete_inverse_cases': 5,
    }
    encoded = json.dumps(result['word_one_based'], separators=(',', ':')).encode('ascii')
    result['word_json_sha256'] = hashlib.sha256(encoded).hexdigest()
    return result


if __name__ == '__main__':
    sys.stdout.buffer.write((json.dumps(run(), sort_keys=True,
                                       separators=(',', ':')) + '\n').encode('ascii'))
