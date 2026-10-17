#!/usr/bin/env python3
"""Exact audit for P-TM-CORR-ZEROS-1.

Proof-first, result-exposed, no-priority public probe.  Python 3.12 standard
library only.  Exact int and Fraction arithmetic; no float, file input,
network, clock, environment input, subprocess, or random module.

Exit 0: PROOF-SURVIVES
Exit 1: STOP-INTEGRITY
Exit 2: exact scientific FALSIFIED
"""

import hashlib
import sys
from fractions import Fraction


SCIENCE_FAILURES = []
INTEGRITY_STOPS = []
GATE_RESULTS = []
C_MAIN = None


def scientific(condition, code, detail):
    """Record an exact mathematical counterexample when condition is false."""
    if not condition:
        SCIENCE_FAILURES.append("%s %s" % (code, detail))


def integrity(condition, code, detail):
    """Record an integrity stop when condition is false."""
    if not condition:
        INTEGRITY_STOPS.append("%s %s" % (code, detail))


def run_gate(tag, function):
    science_before = len(SCIENCE_FAILURES)
    stop_before = len(INTEGRITY_STOPS)
    try:
        detail = function()
    except Exception as exc:  # deterministic type only; no host-dependent text
        INTEGRITY_STOPS.append(
            "%s unexpected-exception=%s" % (tag, type(exc).__name__)
        )
        detail = "unexpected exception"

    if len(INTEGRITY_STOPS) > stop_before:
        status = "STOP"
    elif len(SCIENCE_FAILURES) > science_before:
        status = "FALSIFIED"
    else:
        status = "PASS"
    GATE_RESULTS.append(status)
    print("%s %s  %s" % (tag, status, detail))


def oddpart(n):
    if n <= 0:
        raise ValueError("oddpart requires a positive integer")
    while n % 2 == 0:
        n //= 2
    return n


def tm_word(limit):
    """Return u_n=(-1)^s_2(n) for 0<=n<limit."""
    word = [1] * limit
    for n in range(1, limit):
        word[n] = -word[n >> 1] if n & 1 else word[n >> 1]
    return word


def is_power_of_two(n):
    return n > 0 and n & (n - 1) == 0


def build_c(limit):
    """Exact recurrence values c(0)..c(limit)."""
    values = [Fraction(0)] * (limit + 1)
    values[0] = Fraction(1)
    if limit >= 1:
        values[1] = Fraction(-1, 3)
    for k in range(2, limit + 1):
        if k & 1:
            m = k >> 1
            values[k] = -(values[m] + values[m + 1]) / 2
        else:
            values[k] = values[k >> 1]
    return values


def first_set_witness(left, right):
    extra = left - right
    missing = right - left
    if extra:
        return "extra=%d" % min(extra)
    if missing:
        return "missing=%d" % min(missing)
    return "none"


def gate_g1_dyadic_finite():
    m_max = 300
    n_max = 300
    lag_max = 2 * m_max + 1
    word = tm_word(2 * n_max + lag_max + 2)

    prefix = []
    for lag in range(lag_max + 1):
        row = [0] * (2 * n_max + 1)
        total = 0
        for n in range(2 * n_max):
            total += word[n] * word[n + lag]
            row[n + 1] = total
        prefix.append(row)

    witness = None
    for m in range(m_max + 1):
        for n in range(n_max + 1):
            if prefix[2 * m][2 * n] != 2 * prefix[m][n]:
                witness = "even m=%d N=%d" % (m, n)
                break
            if prefix[2 * m + 1][2 * n] != -(
                prefix[m][n] + prefix[m + 1][n]
            ):
                witness = "odd m=%d N=%d" % (m, n)
                break
        if witness is not None:
            break

    scientific(witness is None, "F1", witness or "none")
    return "both identities; 0<=m,N<=300; direct word"


def gate_g2_limit_base_certificate():
    limit = 1 << 18
    word = tm_word(limit + 2)
    s1 = [0] * (limit + 1)
    total = 0
    for n in range(limit):
        total += word[n] * word[n + 1]
        s1[n + 1] = total

    def e(n):
        return Fraction(s1[n]) + Fraction(n, 3)

    recurrence_witness = None
    if e(0) != 0 or e(1) != Fraction(-2, 3):
        recurrence_witness = "base E(0)=%s E(1)=%s" % (e(0), e(1))

    if recurrence_witness is None:
        for n in range((limit // 2) + 1):
            if e(2 * n) != -e(n):
                recurrence_witness = "even N=%d" % n
                break
            if 2 * n + 1 <= limit and e(2 * n + 1) != -e(n) - Fraction(2, 3):
                recurrence_witness = "odd N=%d" % n
                break

    bound_witness = None
    for n in range(1, limit + 1):
        if abs(e(n)) > Fraction(2 * n.bit_length(), 3):
            bound_witness = "binary-length bound N=%d" % n
            break

    coefficient_certificate = (
        Fraction(2, 3) + Fraction(2, 3) == Fraction(4, 3)
        and Fraction(2, 3) >= 0
    )
    integrity(
        coefficient_certificate,
        "I2",
        "malformed binary-length coefficient certificate",
    )
    scientific(
        recurrence_witness is None,
        "F1",
        recurrence_witness or "none",
    )
    integrity(bound_witness is None, "I2", bound_witness or "none")
    return "E recurrences and base-limit certificate; 0<=N<=2^18"


def gate_g3_recurrence_ring():
    global C_MAIN
    limit = (1 << 18) + 2
    C_MAIN = build_c(limit)

    witness = None
    if C_MAIN[0] != 1 or C_MAIN[1] != Fraction(-1, 3):
        witness = "base"

    if witness is None:
        for k in range(2, limit + 1):
            if k & 1:
                m = k >> 1
                expected = -(C_MAIN[m] + C_MAIN[m + 1]) / 2
            else:
                expected = C_MAIN[k >> 1]
            if C_MAIN[k] != expected:
                witness = "recurrence k=%d" % k
                break

    if witness is None:
        for k, value in enumerate(C_MAIN):
            scaled = 3 * value
            if not is_power_of_two(scaled.denominator):
                witness = "ring k=%d denominator=%d" % (
                    k,
                    scaled.denominator,
                )
                break

    scientific(witness is None, "F2", witness or "none")

    alphabet_witness = None
    for k in range(1, limit + 1):
        if abs(C_MAIN[k]) > Fraction(1, 3):
            alphabet_witness = "alphabet bound k=%d" % k
            break
    integrity(
        alphabet_witness is None,
        "I2",
        alphabet_witness or "none",
    )
    return "recurrence, 3c(k) in Z[1/2], and |c(k)|<=1/3"


def gate_g4_parity_certificate():
    integrity(C_MAIN is not None, "I2", "G3 recurrence table unavailable")
    if C_MAIN is None:
        return "G3 prerequisite unavailable"

    limit = 1 << 18
    pairs = [None] * (limit + 1)
    witness = None

    for m in range(4, limit + 1):
        scale = 3 * (1 << (m.bit_length() - 3))
        aq = scale * C_MAIN[m]
        bq = scale * C_MAIN[m + 1]
        if aq.denominator != 1 or bq.denominator != 1:
            witness = "nonintegral m=%d" % m
            break
        pairs[m] = (aq.numerator, bq.numerator)

    expected_base = {
        4: (-1, 0),
        5: (0, 1),
        6: (1, 0),
        7: (0, -1),
    }
    if witness is None:
        for m in range(4, 8):
            if pairs[m] != expected_base[m]:
                witness = "base m=%d got=%s" % (m, pairs[m])
                break

    if witness is None:
        for m in range(4, (limit // 2) + 1):
            a, b = pairs[m]
            child0 = (2 * a, -(a + b))
            if pairs[2 * m] != child0:
                witness = "bit0 transfer m=%d" % m
                break
            if 2 * m + 1 <= limit:
                child1 = (-(a + b), 2 * b)
                if pairs[2 * m + 1] != child1:
                    witness = "bit1 transfer m=%d" % m
                    break

    parity_states = 0
    parity_closed = True
    for a in (0, 1):
        for b in (0, 1):
            if (a + b) & 1:
                parity_states += 1
                child0 = (2 * a, -(a + b))
                child1 = (-(a + b), 2 * b)
                for x, y in (child0, child1):
                    if not ((x + y) & 1) or not ((x - y) & 1):
                        parity_closed = False

    integrity(parity_states == 2, "I2", "odd-sum parity-state count")
    scientific(parity_closed, "F4", "mod-two transfer closure")

    if witness is None:
        for m in range(4, limit + 1):
            a, b = pairs[m]
            if not ((a + b) & 1) or not ((a - b) & 1):
                witness = "parity m=%d" % m
                break

    scientific(witness is None, "F4", witness or "none")
    return "four bases, two transfers, 2 parity states, 4<=m<=2^18"


def gate_g5_zero_neighbor():
    integrity(C_MAIN is not None, "I2", "G3 recurrence table unavailable")
    if C_MAIN is None:
        return "G3 prerequisite unavailable"

    limit = 200000
    zeros = {k for k in range(1, limit + 1) if C_MAIN[k] == 0}
    predicted = {
        k for k in range(1, limit + 1) if oddpart(k) in (5, 7)
    }
    scientific(
        zeros == predicted,
        "F3",
        first_set_witness(zeros, predicted),
    )

    neighbours = [
        m for m in range(1, limit + 1) if C_MAIN[m] == C_MAIN[m + 1]
    ]
    scientific(
        neighbours == [1],
        "F5",
        "neighbours=%s" % neighbours[:8],
    )
    return "zero set and neighbouring coincidence; range 1..200000"


def pair_matrix(m):
    """Independent pair route: return (c(m),c(m+1))."""
    x = Fraction(1)
    y = Fraction(-1, 3)
    for bit in bin(m)[2:]:
        if bit == "0":
            x, y = x, -(x + y) / 2
        else:
            x, y = -(x + y) / 2, y
    return x, y


def gate_g6_independent_matrix_deep():
    integrity(C_MAIN is not None, "I2", "G3 recurrence table unavailable")
    if C_MAIN is None:
        return "G3 prerequisite unavailable"

    route_witness = None
    for k in range(20001):
        if pair_matrix(k) != (C_MAIN[k], C_MAIN[k + 1]):
            route_witness = "overlap k=%d" % k
            break
    integrity(route_witness is None, "I3", route_witness or "none")

    theorem_witness = None
    deep_zero = [5 << 127, 7 << 193, 5 << 521, 7 << 607]
    deep_nonzero = [
        1 << 333,
        3 << 129,
        9 << 257,
        11 << 511,
        ((1 << 509) + (1 << 137) + 1) << 17,
    ]

    for k in deep_zero:
        if pair_matrix(k)[0] != 0:
            theorem_witness = "fixed expected-zero bits=%d" % k.bit_length()
            break
    if theorem_witness is None:
        for k in deep_nonzero:
            if pair_matrix(k)[0] == 0:
                theorem_witness = "fixed expected-nonzero bits=%d" % k.bit_length()
                break

    checked_q_shift = 0
    if theorem_witness is None:
        for q in range(1, 4002, 2):
            expected_zero = q in (5, 7)
            for a in range(65):
                k = q << a
                checked_q_shift += 1
                if (pair_matrix(k)[0] == 0) != expected_zero:
                    theorem_witness = "q=%d a=%d" % (q, a)
                    break
            if theorem_witness is not None:
                break

    seed = b"P-TM-CORR-ZEROS-1/G6/sha512/v1"
    checked_hash_cases = 0
    if theorem_witness is None:
        for i in range(256):
            digest = hashlib.sha512(seed + b"/" + str(i).encode("ascii")).digest()
            q = int.from_bytes(digest, "big") | (1 << 511) | 1
            k = q << (i % 65)
            checked_hash_cases += 1
            if pair_matrix(k)[0] == 0:
                theorem_witness = "hash-case=%d" % i
                break

    scientific(
        theorem_witness is None,
        "F3",
        theorem_witness or "none",
    )
    integrity(
        theorem_witness is not None or checked_q_shift == 2001 * 65,
        "I2",
        "q-shift count=%d" % checked_q_shift,
    )
    integrity(
        theorem_witness is not None or checked_hash_cases == 256,
        "I2",
        "hash-case count=%d" % checked_hash_cases,
    )
    return "matrix overlap, deep pins, 130065 q-shifts, 256 hash cases"


def gate_g7_convention_firewall():
    integrity(C_MAIN is not None, "I2", "G3 recurrence table unavailable")
    if C_MAIN is None:
        return "G3 prerequisite unavailable"

    k_max = 64
    n_max = 1024
    word = tm_word(n_max + k_max + 2)
    complemented = [-value for value in word]

    witness = None
    for k in range(k_max + 1):
        for n in range(n_max):
            if word[n] * word[n + k] != (
                complemented[n] * complemented[n + k]
            ):
                witness = "complement k=%d n=%d" % (k, n)
                break
        if witness is not None:
            break
    integrity(witness is None, "I2", witness or "none")

    if witness is None:
        for k in range(k_max + 1):
            for n in range(513):
                forward = sum(word[j] * word[j + k] for j in range(n))
                reverse = sum(
                    word[j] * word[j - k] for j in range(k, k + n)
                )
                if forward != reverse:
                    witness = "translated reversal k=%d N=%d" % (k, n)
                    break
            if witness is not None:
                break
    integrity(witness is None, "I2", witness or "none")

    lag_limit = 20000
    relabelled = {
        label
        for label in range(1, lag_limit + 1)
        if C_MAIN[label - 1] == 0
    }
    relabelled_expected = {
        label
        for label in range(1, lag_limit + 1)
        if label > 1 and oddpart(label - 1) in (5, 7)
    }
    scientific(
        relabelled == relabelled_expected,
        "F3",
        "lag relabelling " + first_set_witness(relabelled, relabelled_expected),
    )

    tword = [(1 - value) // 2 for value in word]
    algebra_witness = None
    for k in range(k_max + 1):
        sum_t_pair = 0
        sum_u = 0
        sum_u_shift = 0
        sum_u_pair = 0
        for n in range(1, 513):
            j = n - 1
            sum_t_pair += tword[j] * tword[j + k]
            sum_u += word[j]
            sum_u_shift += word[j + k]
            sum_u_pair += word[j] * word[j + k]
            if 4 * sum_t_pair != (
                n - sum_u - sum_u_shift + sum_u_pair
            ):
                algebra_witness = "alphabet k=%d N=%d" % (k, n)
                break
        if algebra_witness is not None:
            break
    integrity(algebra_witness is None, "I2", algebra_witness or "none")

    weighted_zero = None
    for k in range(1, 200001):
        d = (1 + C_MAIN[k]) / 4
        if d == 0:
            weighted_zero = k
            break
    integrity(
        weighted_zero is None,
        "I2",
        "weighted zero k=%s" % weighted_zero,
    )
    return (
        "complement k<=64 n<1024; reversal/alphabet N<=512; "
        "lag<=20000; weighted<=200000"
    )


def main():
    print("P-TM-CORR-ZEROS-1 verifier")
    print(
        "basis: Public Canon v71; lock base "
        "7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2; issue #694"
    )
    print("posture: proof-first; result-exposed; no priority claim")
    print("scope: L5 abstract drive word; no general discrepancy bound")
    print("arithmetic: int and Fraction only")
    print("")

    run_gate("G1 DYADIC-FINITE", gate_g1_dyadic_finite)
    run_gate("G2 LIMIT-BASE-CERTIFICATE", gate_g2_limit_base_certificate)
    run_gate("G3 RECURRENCE-RING", gate_g3_recurrence_ring)
    run_gate("G4 PARITY-CERTIFICATE", gate_g4_parity_certificate)
    run_gate("G5 ZERO-NEIGHBOR", gate_g5_zero_neighbor)
    run_gate("G6 INDEPENDENT-MATRIX-DEEP", gate_g6_independent_matrix_deep)
    run_gate("G7 CONVENTION-FIREWALL", gate_g7_convention_firewall)

    print("")
    if INTEGRITY_STOPS:
        print("SCIENTIFIC DECISION STOP-INTEGRITY")
        for item in sorted(set(INTEGRITY_STOPS)):
            print("STOP " + item)
        if SCIENCE_FAILURES:
            print("FALSIFIER WITHHELD BY STOP-PRECEDENCE")
        exit_code = 1
    elif SCIENCE_FAILURES:
        print("SCIENTIFIC DECISION FALSIFIED")
        for item in sorted(set(SCIENCE_FAILURES)):
            print("FALSIFIER " + item)
        exit_code = 2
    else:
        print("SCIENTIFIC DECISION PROOF-SURVIVES")
        exit_code = 0

    passed = sum(status == "PASS" for status in GATE_RESULTS)
    print("SUMMARY %d/%d PASS" % (passed, len(GATE_RESULTS)))
    return exit_code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # never emit a traceback or host-dependent detail
        print("SCIENTIFIC DECISION STOP-INTEGRITY")
        print("STOP unhandled-exception=%s" % type(exc).__name__)
        sys.exit(1)
