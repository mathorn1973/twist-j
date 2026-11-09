#!/usr/bin/env python3
"""Prospective literal S3/stopwatch/archive composition audit. NON-CANONICAL L1.
Primary arithmetic is shared with the new verify.py; audit.py independently
checks that compiler in the five-coefficient quotient representation.
No sealed predecessor executable is imported or executed.
"""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re
import sys
import verify as v

FIXTURE = Path("probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/WORD535.txt")
FIXTURE_SHA = "ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b"
CASES = tuple(((n, t),) for n in (0, 1) for t in v.HEIGHTS) + (
    ((0, -2), (1, 2)),
    ((1, -1), (0, 1)),
    ((0, 0), (1, 0)),
    ((0, -2), (1, 2), (0, 0)),
)
A_MAP = (31, 32, 33, 34, 35, 36, 3, 4, 37, 38, 39, 40, 41, 42, 43)
BANK_B = v.add(v.ONE, v.rho(v.rho(v.ONE)))

def source(n):
    return (v.ZERO, v.TWO, v.ZERO) if n == 0 else (v.B, v.J, v.ZERO)

def bank(label=None):
    result = [v.neg(BANK_B), BANK_B] * 5
    if label is not None:
        result[2 * label] = v.neg(v.rho(BANK_B))
        result[2 * label + 1] = v.rho(BANK_B)
    return result

def preparation(inputs):
    n, t = inputs[0]
    state = list(source(n)) + [v.J, v.neg(v.J)]
    state += [v.ZERO, v.B, v.ZERO, v.ZERO, v.J, v.ZERO]
    state += bank() + bank()
    state += list(v.initial(t)[:6]) + list(v.STOCK)
    for _ in inputs:
        state += bank() + bank()
    for n, t in inputs[1:]:
        state += list(source(n)) + list(v.initial(t)[:2])
    assert len(state) == 39 + 25 * len(inputs)
    return state

def inverse(word):
    return tuple((kind, a, b) for kind, a, b in reversed(word)
                 for _ in range(4 if kind == "C" else 1))

def contacts(edges):
    return tuple(("C", a, b) for a, b in edges)

def copier(a, d):
    local = ((0, 3),) * 2 + ((3, 4),) + ((0, 3),) * 3
    local += ((0, 5),) * 4 + ((0, 3), (0, 5))
    assert len(local) == 12
    result = []
    for p in range(5):
        q = (p + 1) % 5
        ports = (a + 2*p, a + 2*p + 1, a + 2*q, a + 2*q + 1,
                 d + 2*p, d + 2*p + 1)
        result.extend(("C", ports[x], ports[y]) for x, y in local)
    assert len(result) == 60
    return tuple(result)

@lru_cache(maxsize=131072)
def checked_pair(a, b):
    result_a, result_b, accepted = v.contact(a, b)
    assert v.pair_invariants(a, b) == v.pair_invariants(result_a, result_b)
    return result_a, result_b, accepted

class Runner:
    def __init__(self):
        self.contact_cuts = self.swaps = self.accepted = self.refused = 0
        self.boundary_checks = self.archive_guards = 0

    def apply(self, state, word, protected=frozenset()):
        for kind, a, b in word:
            assert a not in protected and b not in protected
            if protected:
                self.archive_guards += 1
            if kind == "C":
                x, y, accepted = checked_pair(state[a], state[b])
                state[a], state[b] = x, y
                self.contact_cuts += 1
                self.accepted += int(accepted)
                self.refused += int(not accepted)
            else:
                assert kind == "S"
                state[a], state[b] = state[b], state[a]
                self.swaps += 1

    def compare(self, state, expected, reference):
        assert state == expected
        # All fixed reload swaps in this declared family have equal residues.
        assert v.invariants(state) == reference
        self.boundary_checks += 1

def main():
    data = FIXTURE.read_bytes()
    assert hashlib.sha256(data).hexdigest() == FIXTURE_SHA
    old = tuple((int(a)-1, int(b)-1)
                for a, b in re.findall(rb"C\((\d+),(\d+)\)", data))
    assert len(old) == 535 and all(0 <= a < 31 and 0 <= b < 31 for a, b in old)
    W = contacts(old * 10)
    Winv = inverse(W)
    A = contacts(tuple((A_MAP[a], A_MAP[b]) for a, b in v.WORD))
    Ainv = inverse(A)
    assert len(A) == 95 and len(Ainv) == 380
    assert sum(v.q(x) for x in v.STOCK) == 80
    assert (sum(v.hermitian(x)[0] for x in v.STOCK),
            sum(v.hermitian(x)[1] for x in v.STOCK)) == (33, 14)
    audit = Runner()
    rows = []
    for inputs in CASES:
        k = len(inputs)
        state = preparation(inputs)
        initial = state[:]
        expected = state[:]
        reference = v.invariants(state)
        sum_t2 = sum(t*t for _, t in inputs)
        assert reference[0] == (1 + 4*k, -9 - 2*k, -6, -12)
        assert reference[2] == 177 + 78*k + 10*sum_t2
        assert reference[1] == (70 + 30*k + 4*sum_t2, 37 + 18*k + 2*sum_t2)
        protected = set()
        whole_word = []
        current_word_count = 0
        for stage, (n, t) in enumerate(inputs):
            r = t + 2
            target = 44 + 20*stage
            copy_word = copier(11, target) + copier(21, target + 10)
            U = W + copy_word + Winv
            assert len(U) == 26870
            cycle = A + U + Ainv
            assert len(cycle) == 27345
            audit.apply(state, A, protected)
            translated = expected[:]
            translated[3:5] = v.target(t)
            audit.compare(state, translated, reference)

            audit.apply(state, W, protected)
            after_run = translated[:]
            # Y_(n+10) is the result of one F step beyond Y_n.
            advanced = list(source(n))
            for edge in ((0, 1), (1, 2)):
                a, b = edge
                advanced[a], advanced[b], _ = checked_pair(advanced[a], advanced[b])
            after_run[:3] = advanced
            p_a = (-r) % 5
            p_b = (-(r + (1 if n == 0 else 8))) % 5
            after_run[11:21] = bank(p_a)
            after_run[21:31] = bank(p_b)
            audit.compare(state, after_run, reference)

            audit.apply(state, copy_word[:60], protected)
            protected.update(range(target, target+10))
            audit.apply(state, copy_word[60:], protected)
            protected.update(range(target+10, target+20))
            copied = after_run[:]
            copied[target:target+10] = bank(p_a)
            copied[target+10:target+20] = bank(p_b)
            audit.compare(state, copied, reference)

            audit.apply(state, Winv, protected)
            restored_core = translated[:]
            restored_core[target:target+20] = bank(p_a) + bank(p_b)
            audit.compare(state, restored_core, reference)

            audit.apply(state, Ainv, protected)
            expected[target:target+20] = bank(p_a) + bank(p_b)
            audit.compare(state, expected, reference)
            protected.update(range(target, target+20))
            whole_word.extend(cycle)
            current_word_count += len(cycle)
            if stage < k - 1:
                cartridge = 44 + 20*k + 5*stage
                swaps = tuple(("S", a, cartridge+i)
                              for i, a in enumerate((0, 1, 2, 31, 32)))
                audit.apply(state, swaps, protected)
                for _, a, b in swaps:
                    expected[a], expected[b] = expected[b], expected[a]
                audit.compare(state, expected, reference)
                whole_word.extend(swaps)
        assert current_word_count == 27345*k
        # Archives alone recover all source phases and heights.
        decoded = []
        for stage in range(k):
            start = 44 + 20*stage
            labels = []
            for start_bank in (start, start+10):
                matches = [p for p in range(5) if state[start_bank:start_bank+10] == bank(p)]
                assert len(matches) == 1
                labels.append(matches[0])
            delta = (labels[0] - labels[1]) % 5
            assert delta in (1, 3)
            decoded.append((0 if delta == 1 else 1, (-labels[0]) % 5 - 2))
        assert tuple(decoded) == inputs
        endpoint_digest = hashlib.sha256(json.dumps(state,separators=(",",":")).encode()).hexdigest()
        audit.apply(state, inverse(whole_word))
        audit.compare(state, initial, reference)
        rows.append(dict(inputs=inputs, slots=len(state), Q=reference[2], H=reference[1],
                         contacts_forward=27345*k, swaps_forward=5*(k-1),
                         final_state_sha256=endpoint_digest))
    assert len(CASES) == 14 and sum(map(len, CASES)) == 19
    assert audit.contact_cuts == 2597775 and audit.swaps == 50
    result = dict(status="PASS",scope="NON-CANONICAL / L1 literal finite composition audit",
                  source_word_sha256=FIXTURE_SHA, cases=rows, cycles=19,
                  contact_cuts=audit.contact_cuts, swap_cuts=audit.swaps,
                  accepted=audit.accepted,refused=audit.refused,
                  boundary_checks=audit.boundary_checks,archive_address_guards=audit.archive_guards)
    sys.stdout.buffer.write((json.dumps(result,sort_keys=True,separators=(",",":"))+"\n").encode("ascii"))

if __name__ == "__main__":
    main()
