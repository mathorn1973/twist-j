#!/usr/bin/env python3
"""Independent exact five-cyclic-coordinate audit of CONSTRUCTIVE-3 output.

NON-CANONICAL / L1. No search module imports; no scientific run before pin.
Usage: python audit.py VERIFY_STDOUT_PATH
"""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

HEIGHTS = (-2, -1, 0, 1, 2)
ZERO = (0, 0, 0, 0, 0)


def normal(a):
    least = min(a)
    return tuple(x - least for x in a)


def add(a, b):
    return normal(tuple(x + y for x, y in zip(a, b)))


def minus(a, b):
    return normal(tuple(x - y for x, y in zip(a, b)))


def times(n, a):
    return normal(tuple(n * x for x in a))


def product(a, b):
    out = [0] * 5
    for i in range(5):
        for k in range(5):
            out[(i + k) % 5] += a[i] * b[k]
    return normal(out)


def rotate(a, exponent):
    out = [0] * 5
    for i, value in enumerate(a):
        out[(i + exponent) % 5] = value
    return tuple(out)


ONE = (1, 0, 0, 0, 0)
JROOT = (0, 1, 0, 0, 0)
RHO = (0, 0, 1, 0, 0)
U = minus(ONE, JROOT)
B = minus(ONE, RHO)
J = add(ONE, RHO)
X = normal((1, 1, 0, -2, 0))
TWO = times(2, ONE)


@lru_cache(maxsize=100000)
def value_account(a):
    numerator = 5 * sum(v * v for v in a) - sum(a) ** 2
    assert numerator % 2 == 0
    q = numerator // 2
    conjugate = tuple(a[(-i) % 5] for i in range(5))
    h = product(a, conjugate)
    assert h[1] == h[4] and h[2] == h[3]
    # h=A+B*phi, phi=-j^2-j^3, after subtracting h[1] times Phi_5.
    aa, bb = h[0] - h[1], h[1] - h[2]
    assert q == 2 * aa + bb
    return q, aa, bb, sum(a) % 5


@lru_cache(maxsize=100000)
def contact(a, b):
    difference = minus(a, b)
    if any(value % 2 for value in difference):
        return a, b, False
    half = tuple(value // 2 for value in difference)
    delta = minus(rotate(half, 2), half)
    return add(a, delta), minus(b, delta), True


def full_account(state):
    total = ZERO
    q = ha = hb = 0
    residues = []
    for value in state:
        total = add(total, value)
        vq, va, vb, residue = value_account(value)
        q += vq
        ha += va
        hb += vb
        residues.append(residue)
    return total, q, ha, hb, tuple(residues)


def audited_step(state, pair):
    i, k = pair
    a, b = state[i], state[k]
    x, y, admitted = contact(a, b)
    aq, aa, ab, ar = value_account(a)
    bq, ba, bb, br = value_account(b)
    xq, xa, xb, xr = value_account(x)
    yq, ya, yb, yr = value_account(y)
    assert add(a, b) == add(x, y)
    assert aq + bq == xq + yq
    assert aa + ba == xa + ya and ab + bb == xb + yb
    assert (ar, br) == (xr, yr)
    state[i], state[k] = x, y
    return admitted



INV_J = normal((0, -1, -1, 0, 0))
JB = product(J, B)
SEPARATORS = (U, minus(U, JB), minus(U, B))
TRANSFORMED = (minus(U, JB), minus(U, B), U,
               add(U, product(RHO, B)), add(U, product(RHO, JB)))
MARKERS = tuple(times(-1, product(product(B, x), INV_J)) for x in TRANSFORMED[1:])
STOCK = SEPARATORS + MARKERS
P = [(0, 8), (0, 9), (0, 10)]


def local_writer(p, marker=5, plus=6, negative=7):
    assert p in (1, 2, 3, 4)
    a, t = (marker, negative), (plus, negative)
    return [a] + [t] * (5 - p) + [a] * 4 + [t] * p


def inverse(word):
    return [pair for pair in reversed(word) for _ in range(4)]


def complete_word():
    word = P[:]
    for p, marker in enumerate(range(11, 15), 1):
        m = [(0, marker), (5, marker)]
        word += m + local_writer(p) + inverse(m)
    return word + inverse(P)


def initial(t):
    return (add(U, times(t, B)), add(U, times(-t, B)),
            ZERO, ZERO, X, TWO, J, times(-1, J)) + STOCK


def target(t):
    value = rotate(J, 2 * ((t + 2) % 5))
    return value, times(-1, value)


def decode_four(raw):
    assert isinstance(raw, list) and len(raw) == 4
    assert all(type(v) is int for v in raw)
    return normal(tuple(raw) + (0,))


def parse_word(raw):
    assert isinstance(raw, list) and len(raw) == 95
    result = []
    for pair in raw:
        assert isinstance(pair, list) and len(pair) == 2
        assert all(type(value) is int for value in pair)
        assert 1 <= pair[0] < pair[1] <= 15
        result.append((pair[0] - 1, pair[1] - 1))
    return result


def parity(a):
    return tuple((a[k] - a[0]) % 2 for k in range(1, 5))


def audit_markers():
    reports = []
    checked = 0
    for index, selected in enumerate(HEIGHTS[1:]):
        marker = 11 + index
        m = [(0, marker), (5, marker)]
        for t in HEIGHTS:
            original = initial(t)
            state = list(original)
            reference = full_account(state)
            for pair in P:
                audited_step(state, pair)
                checked += 1
            assert state[0] == TRANSFORMED[HEIGHTS.index(t)]
            before = state[:]
            trace = [int(audited_step(state, pair)) for pair in m]
            checked += len(m)
            expected = before[:]
            if t == selected:
                expected[0] = times(2, product(product(RHO, before[0]), INV_J))
                expected[marker], expected[5] = B, J
            assert state == expected
            assert trace == ([1, 1] if t == selected else [0, 0])
            assert full_account(state) == reference
            for pair in inverse(P + m):
                audited_step(state, pair)
                checked += 1
            assert tuple(state) == original and full_account(state) == reference
            reports.append({"selected": selected, "height": t, "trace": trace})
    return {"status": "PASS", "cases": reports, "checked_primitive_cuts": checked}


def audit_writers():
    reports = []
    checked = 0
    for p in (1, 2, 3, 4):
        word = local_writer(p, 0, 1, 2)
        for active, q in [(True, 0)] + [(False, q) for q in range(5)]:
            phase = rotate(J, 2 * q)
            original = (J if active else TWO, phase, times(-1, phase))
            state = list(original)
            reference = full_account(state)
            for pair in word:
                audited_step(state, pair)
                checked += 1
            expected_phase = rotate(J, 2 * p) if active else phase
            assert tuple(state) == (original[0], expected_phase, times(-1, expected_phase))
            assert full_account(state) == reference
            for pair in inverse(word):
                audited_step(state, pair)
                checked += 1
            assert tuple(state) == original and full_account(state) == reference
            reports.append({"written_phase": p, "active": active, "input_phase": q})
    return {"status": "PASS", "cases": reports, "checked_primitive_cuts": checked}


def run(path):
    raw = Path(path).read_bytes()
    record = json.loads(raw)
    assert record["status"] in ("PASS", "FOUND")
    assert record["clock_target_rule"] == "t+2"
    assert record["separator_z_four_coefficients"] == [[0] * 4] * 3
    assert tuple(decode_four(v) for v in record["stock_four_coefficients"]) == STOCK
    assert tuple(decode_four(v) for v in record["separator_refs_four_coefficients"]) == SEPARATORS
    assert tuple(decode_four(v) for v in record["marker_refs_four_coefficients"]) == MARKERS
    assert tuple(decode_four(v) for v in record["transformed_x_four_coefficients"]) == TRANSFORMED
    word = parse_word(record["word_one_based"])
    assert word == complete_word()
    assert product(J, INV_J) == ONE
    labels = [parity(x) for x in TRANSFORMED]
    assert len(set(labels)) == 5 and (0, 0, 0, 0) not in labels
    marker_report = audit_markers()
    writer_report = audit_writers()
    checked = 0
    reports = []
    endpoints = []
    for t in HEIGHTS:
        original = initial(t)
        state = list(original)
        reference = full_account(state)
        trace = bytearray()
        for pair in word:
            trace.append(ord("A") if audited_step(state, pair) else ord("R"))
            checked += 1
        expected = list(original)
        expected[6], expected[7] = target(t)
        assert state == expected
        assert full_account(state) == reference
        assert tuple(decode_four(v) for v in record["complete_final_states"][str(t)]) == tuple(state)
        assert record["forward_admission_traces"][str(t)].encode("ascii") == bytes(trace)
        assert record["complete_initial_q"][str(t)] == reference[1]
        endpoints.append(state[:])
        for pair in inverse(word):
            audited_step(state, pair)
            checked += 1
        assert tuple(state) == original and full_account(state) == reference
        reports.append({"height": t, "target_phase": t + 2,
                        "forward_trace_sha256": hashlib.sha256(trace).hexdigest(),
                        "account": reference[1], "hermitian": list(reference[2:4])})
    endpoint_bytes = json.dumps(endpoints, separators=(",", ":")).encode("ascii")
    stock_account = full_account(STOCK)
    assert record["stock_q"] == stock_account[1]
    assert record["stock_h_coefficients"] == list(stock_account[2:4])
    assert decode_four(record["stock_sum_four_coefficients"]) == stock_account[0]
    return {
        "status": "PASS", "scope": "EXACT_95_CONTACT_COMPILER",
        "representation": "FIVE_CYCLIC_COEFFICIENTS_MOD_ALL_ONES",
        "verify_stdout_sha256": hashlib.sha256(raw).hexdigest(),
        "verify_source_sha256": hashlib.sha256(Path(__file__).with_name("verify.py").read_bytes()).hexdigest(),
        "audit_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "word_contacts": len(word), "literal_inverse_contacts": len(inverse(word)),
        "compiler_checked_primitive_cuts": checked,
        "all_checked_primitive_cuts": checked + marker_report["checked_primitive_cuts"]
            + writer_report["checked_primitive_cuts"],
        "compiler_cases": reports,
        "complete_forward_endpoints_sha256": hashlib.sha256(endpoint_bytes).hexdigest(),
        "stock_account": stock_account[1],
        "stock_hermitian": list(stock_account[2:4]),
        "stock_sum_five_coordinates": stock_account[0],
        "marker_audit": marker_report,
        "writer_audit": writer_report,
        "inverse": "EXACT_INITIAL_STATE_FOR_ALL_FIVE",
    }


if __name__ == "__main__":
    assert len(sys.argv) == 2, "expected VERIFY_STDOUT_PATH"
    result = run(sys.argv[1])
    sys.stdout.buffer.write(
        (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii"))
