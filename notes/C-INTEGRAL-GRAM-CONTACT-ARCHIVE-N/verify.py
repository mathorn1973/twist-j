#!/usr/bin/env python3
"""Frozen finite audit for C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N.

Author: A. M. Thorn <thorn@twistj.com>
SPDX-License-Identifier: Apache-2.0

NON-CANONICAL / L1. This audits only PREREG.md's seven inventories.
Universal claims require the separate written proof. No floats or sampling.
The raw map uses sum/difference coordinates. The record map separately
performs sparse left and right matrix multiplication, with exact division.
"""

from hashlib import sha256
from itertools import product
import sys


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
TWO = (2, 0, 0, 0)
THREE = (3, 0, 0, 0)
JROOT = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
RHO_INV = (0, 0, 0, 1)
JUNIT = (1, 0, 1, 0)
JUNIT_INV = (0, -1, -1, 0)

# Each data gate touches one edge of the supplied star with centre R=4.
# (kind, first slot, second slot, contact exponent)
PROGRAM = (
    ("swap", 4, 5, 0),
    ("swap", 4, 2, 0),
    ("contact", 0, 4, 1),
    ("swap", 4, 6, 0),
    ("swap", 4, 3, 0),
    ("contact", 1, 4, 1),
    ("identity", 0, 0, 0),
    ("identity", 0, 0, 0),
    ("contact", 1, 4, -1),
    ("swap", 4, 3, 0),
    ("swap", 4, 6, 0),
    ("contact", 0, 4, -1),
    ("swap", 4, 2, 0),
    ("swap", 4, 5, 0),
)


class AuditFailure(Exception):
    """An exact finite assertion failed; no tolerance or repair is applied."""


def require(condition, label):
    if not condition:
        raise AuditFailure(label)


def equal(actual, expected, label):
    if actual != expected:
        raise AuditFailure(f"{label}: actual={actual!r}; expected={expected!r}")


def add(a, b):
    return tuple(a[k] + b[k] for k in range(4))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return tuple(a[k] - b[k] for k in range(4))


def scale(n, a):
    return tuple(n * x for x in a)


def mul(a, b):
    """Multiply in Z[j]; reduce j^5=1 and j^4=-1-j-j^2-j^3."""
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    c4 = a1 * b3 + a2 * b2 + a3 * b1
    return (
        a0 * b0 + a2 * b3 + a3 * b2 - c4,
        a0 * b1 + a1 * b0 + a3 * b3 - c4,
        a0 * b2 + a1 * b1 + a2 * b0 - c4,
        a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0 - c4,
    )


def conjugate(a):
    a0, a1, a2, a3 = a
    return (a0 - a1, -a1, a3 - a1, a2 - a1)


def power(a, exponent):
    require(exponent >= 0, "power requires a nonnegative integer exponent")
    out = ONE
    base = a
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent //= 2
    return out


def mod2(a):
    return tuple(x % 2 for x in a)


def power_mod2(a, exponent):
    out = ONE
    base = mod2(a)
    while exponent:
        if exponent & 1:
            out = mod2(mul(out, base))
        base = mod2(mul(base, base))
        exponent //= 2
    return out


def half(a, label):
    require(all(x % 2 == 0 for x in a), f"nonintegral half at {label}: {a!r}")
    return tuple(x // 2 for x in a)


def trace(a):
    return 4 * a[0] - a[1] - a[2] - a[3]


def account(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    require(numerator % 2 == 0, "account numerator is not even")
    return numerator // 2


def sum_ring(elements):
    out = ZERO
    for a in elements:
        out = add(out, a)
    return out


def full_invariants(z):
    total = sum_ring(z)
    hermitian = sum_ring(mul(a, conjugate(a)) for a in z)
    energy = sum(account(a) for a in z)
    equal(trace(hermitian), 2 * energy, "full Hermitian trace/account identity")
    return (total, hermitian, energy)


def gram(z):
    barred = tuple(conjugate(a) for a in z)
    return tuple(tuple(mul(a, b) for b in barred) for a in z)


def raw_admission(x, y):
    return all(t % 2 == 0 for t in sub(x, y))


def raw_contact(z, i, j, exponent=1):
    require(i != j, "contact slots must differ")
    require(exponent in (-1, 1), "contact exponent must be +1 or -1")
    if not raw_admission(z[i], z[j]):
        return z
    centre = half(add(z[i], z[j]), "raw centre")
    relative = half(sub(z[i], z[j]), "raw relative coordinate")
    phase = RHO if exponent == 1 else RHO_INV
    turned = mul(phase, relative)
    out = list(z)
    out[i] = add(centre, turned)
    out[j] = sub(centre, turned)
    return tuple(out)


def gram_difference(g, i, j):
    return sub(add(g[i][i], g[j][j]), add(g[i][j], g[j][i]))


def record_admission(g, i, j):
    # Full O_F-valued norm, not its scalar trace or trace parity.
    return all(t % 2 == 0 for t in gram_difference(g, i, j))


def record_contact(g, i, j, exponent=1):
    """Independent A G A^dagger, integral only on the frozen Gram image."""
    require(i != j, "record contact slots must differ")
    require(exponent in (-1, 1), "record exponent must be +1 or -1")
    if not record_admission(g, i, j):
        return g
    phase = RHO if exponent == 1 else RHO_INV
    diagonal = add(ONE, phase)
    off_diagonal = sub(ONE, phase)
    n = len(g)

    # Sparse left multiplication. Rows i,j come from the same original G.
    work = [list(row) for row in g]
    for k in range(n):
        work[i][k] = half(
            add(mul(diagonal, g[i][k]), mul(off_diagonal, g[j][k])),
            "A G row i",
        )
        work[j][k] = half(
            add(mul(off_diagonal, g[i][k]), mul(diagonal, g[j][k])),
            "A G row j",
        )
    left = tuple(tuple(row) for row in work)

    # Sparse right multiplication by A^dagger, from the whole left product.
    diagonal_bar = conjugate(diagonal)
    off_diagonal_bar = conjugate(off_diagonal)
    work = [list(row) for row in left]
    for k in range(n):
        work[k][i] = half(
            add(mul(left[k][i], diagonal_bar), mul(left[k][j], off_diagonal_bar)),
            "A G A^dagger column i",
        )
        work[k][j] = half(
            add(mul(left[k][i], off_diagonal_bar), mul(left[k][j], diagonal_bar)),
            "A G A^dagger column j",
        )
    return tuple(tuple(row) for row in work)


def raw_swap(z, i, j):
    out = list(z)
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def record_swap(g, i, j):
    order = list(range(len(g)))
    order[i], order[j] = order[j], order[i]
    return tuple(tuple(g[r][s] for s in order) for r in order)


def raw_gate(z, gate, inverse=False):
    kind, i, j, exponent = gate
    if kind == "contact":
        return raw_contact(z, i, j, -exponent if inverse else exponent)
    if kind == "swap":
        return raw_swap(z, i, j)
    equal(kind, "identity", "unknown raw program gate")
    return z


def record_gate(g, gate, inverse=False):
    kind, i, j, exponent = gate
    if kind == "contact":
        return record_contact(g, i, j, -exponent if inverse else exponent)
    if kind == "swap":
        return record_swap(g, i, j)
    equal(kind, "identity", "unknown record program gate")
    return g


def raw_step(c, z):
    return ((c + 1) % 14, raw_gate(z, PROGRAM[c]))


def raw_inverse(c, z):
    previous = (c - 1) % 14
    return (previous, raw_gate(z, PROGRAM[previous], inverse=True))


def record_step(c, g):
    return ((c + 1) % 14, record_gate(g, PROGRAM[c]))


def record_inverse(c, g):
    previous = (c - 1) % 14
    return (previous, record_gate(g, PROGRAM[previous], inverse=True))


def read_final(c, g):
    """Read only (c,G); a zero record in the window is still VALID."""
    if c not in (6, 7, 8):
        return ("NOT_IN_WINDOW", None)
    slots = (5, 6, 4)  # A0, A1, R in this exact order.
    return ("VALID", tuple(tuple(g[r][s] for s in slots) for r in slots))


def integer_line(values):
    require(all(type(value) is int for value in values), "certificate noninteger")
    return (",".join(str(value) for value in values) + "\n").encode("utf-8")


def feed_program_certificate(digest, prefix, case_index, n, c, z, energy):
    values = [case_index, n, c]
    for a in z:
        values.extend(a)
    values.append(energy)
    equal(len(values), 32, "program certificate field count")
    digest.update(prefix.encode("utf-8") + b"|" + integer_line(values))


def audit_f1(context):
    zero_norms = 0
    nonzero_scalar_zeros = 0
    residues = tuple(product((0, 1), repeat=4))
    for a in residues:
        barred = mod2(conjugate(a))
        equal(barred, power_mod2(a, 4), "F1 conjugation/Frobenius4")
        norm = mod2(mul(a, conjugate(a)))
        equal(norm, power_mod2(a, 5), "F1 relative norm/fifth power")
        equal(mod2(conjugate(norm)), norm, "F1 conjugation-fixed norm")
        equal(norm == ZERO, a == ZERO, "F1 norm-zero locus")
        zero_norms += int(norm == ZERO)
        # The scalar trace here is Tr_F4/F2(norm), or q(a) modulo 2.
        # It is not Tr_K/Q(a*bar(a)) modulo 2, which would always vanish.
        scalar_trace = mod2(add(norm, power_mod2(norm, 2)))
        equal(scalar_trace, (account(a) % 2, 0, 0, 0), "F1 binary trace formula")
        nonzero_scalar_zeros += int(a != ZERO and scalar_trace == ZERO)
    equal(len(residues), 16, "F1 residue count")
    equal(zero_norms, 1, "F1 zero-norm count")
    equal(nonzero_scalar_zeros, 5, "F1 nonzero scalar-trace zeros")
    equal(mul(JUNIT, JUNIT_INV), ONE, "F1 J inverse")
    equal(mul(RHO, RHO_INV), ONE, "F1 rho inverse")
    equal(power(RHO, 5), ONE, "F1 rho fifth power")
    for exponent in range(1, 5):
        require(power(RHO, exponent) != ONE, "F1 rho order is less than five")
    return "residues=16 zero_norms=1 nonzero_scalar_trace_zeros=5"


def audit_f2(context):
    box = tuple(product((-1, 0, 1), repeat=4))
    digest = sha256()
    pairs = 0
    admitted_count = 0
    for x, y in product(box, repeat=2):
        z = (x, y)
        g = gram(z)
        admitted = raw_admission(x, y)
        equal(record_admission(g, 0, 1), admitted, "F2 raw/Gram admission")
        difference_norm = mul(sub(x, y), conjugate(sub(x, y)))
        equal(gram_difference(g, 0, 1), difference_norm, "F2 full difference norm")
        equal(
            all(t % 4 == 0 for t in difference_norm),
            admitted,
            "F2 four-divisibility equivalence",
        )
        out = raw_contact(z, 0, 1)
        out_g = record_contact(g, 0, 1)
        equal(out_g, gram(out), "F2 forward Gram continuation")
        equal(raw_contact(out, 0, 1, -1), z, "F2 raw inverse after forward")
        equal(record_contact(out_g, 0, 1, -1), g, "F2 record inverse after forward")
        inverse_out = raw_contact(z, 0, 1, -1)
        inverse_g = record_contact(g, 0, 1, -1)
        equal(inverse_g, gram(inverse_out), "F2 backward Gram continuation")
        equal(raw_contact(inverse_out, 0, 1), z, "F2 raw forward after inverse")
        equal(record_contact(inverse_g, 0, 1), g, "F2 record forward after inverse")
        invariants = full_invariants(z)
        equal(full_invariants(out), invariants, "F2 forward S/h/E")
        equal(full_invariants(inverse_out), invariants, "F2 backward S/h/E")
        fifth_z, fifth_g = z, g
        for _ in range(5):
            fifth_z = raw_contact(fifth_z, 0, 1)
            fifth_g = record_contact(fifth_g, 0, 1)
            equal(fifth_g, gram(fifth_z), "F2 power Gram continuation")
        equal(fifth_z, z, "F2 raw fifth power")
        equal(fifth_g, g, "F2 record fifth power")
        if not admitted:
            equal(out, z, "F2 whole-state refusal identity")
        fields = (*x, *y, *out[0], *out[1], int(admitted), invariants[2])
        equal(len(fields), 18, "F2 certificate field count")
        digest.update(integer_line(fields))
        admitted_count += int(admitted)
        pairs += 1
    equal(pairs, 6561, "F2 ordered pair count")
    context["pair_sha256"] = digest.hexdigest()
    return f"pairs={pairs} admitted={admitted_count}"


def control_trace_loss():
    equal(account(ONE), 2, "F3.1 scalar account")
    equal(account(ONE) % 2, 0, "F3.1 scalar trace is even")
    require(not raw_admission(ONE, ZERO), "F3.1 raw contact must be refused")
    require(not record_admission(gram((ONE, ZERO)), 0, 1), "F3.1 full norm refuses")
    equal(raw_contact((ONE, ZERO), 0, 1), (ONE, ZERO), "F3.1 refusal")


def control_normalization_loss():
    low, high = (ONE, ZERO), (TWO, ZERO)
    g_low, g_high = gram(low), gram(high)
    equal(g_high, tuple(tuple(scale(4, a) for a in row) for row in g_low),
          "F3.2 equal normalized Gram records")
    equal(full_invariants(high)[2], 4 * full_invariants(low)[2],
          "F3.2 normalization account scale")
    equal(account(raw_contact(low, 0, 1)[1]), 0, "F3.2 small receiver")
    equal(account(raw_contact(high, 0, 1)[1]), 5, "F3.2 large receiver")


def control_phase_sensitivity():
    plus = (TWO, scale(2, RHO))
    minus = (TWO, scale(2, RHO_INV))
    for z in (plus, minus):
        g = gram(z)
        equal((g[0][0], g[1][1]), (scale(4, ONE), scale(4, ONE)),
              "F3.3 identical diagonal entries")
        equal(full_invariants(z)[2], 16, "F3.3 input total E")
    out_plus, out_minus = raw_contact(plus, 0, 1), raw_contact(minus, 0, 1)
    equal(tuple(account(a) for a in out_plus), (13, 3), "F3.3 plus accounts")
    equal(tuple(account(a) for a in out_minus), (3, 13), "F3.3 minus accounts")
    equal(full_invariants(out_plus)[2], 16, "F3.3 plus total E")
    equal(full_invariants(out_minus)[2], 16, "F3.3 minus total E")


def control_outside_map():
    first, second = (ONE, ONE), (JROOT, JROOT)
    equal(gram(first), gram(second), "F3.4 original equal Grams")
    out_first = (first[1], conjugate(first[0]))
    out_second = (second[1], conjugate(second[0]))
    equal(gram(out_first)[0][1], ONE, "F3.4 first off-diagonal")
    equal(gram(out_second)[0][1], RHO, "F3.4 second off-diagonal")
    require(gram(out_first) != gram(out_second), "F3.4 outside map must not descend")


def control_reference_extension():
    equal(gram((TWO,)), gram((scale(2, RHO),)), "F3.5 old single-slot Gram")
    equal(gram((TWO,))[0][0], scale(4, ONE), "F3.5 single-slot norm")
    first = raw_contact((TWO, TWO), 0, 1)
    second = raw_contact((scale(2, RHO), TWO), 0, 1)
    equal(account(first[1]), 8, "F3.5 first receiver")
    equal(account(second[1]), 13, "F3.5 reference-sensitive receiver")


def audit_f3(context):
    # Run every frozen negative control, even if another control fails.
    controls = (
        control_trace_loss,
        control_normalization_loss,
        control_phase_sensitivity,
        control_outside_map,
        control_reference_extension,
    )
    failures = []
    for index, control in enumerate(controls, start=1):
        try:
            control()
        except Exception as exc:
            failures.append(f"control={index} {type(exc).__name__}: {exc}")
    if failures:
        raise AuditFailure(" | ".join(failures))
    return "controls=5 exact_values=PASS"


def evaluate_mod11(a):
    return sum(a[k] * (-2) ** k for k in range(4)) % 11


def audit_f4(context):
    a = (2, 1, 0, 0)
    a_bar = conjugate(a)
    equal(sum((-2) ** k for k in range(5)), 11, "F4 residue root relation")
    equal(evaluate_mod11(a), 0, "F4 a vanishes at j=-2 modulo11")
    require(evaluate_mod11(a_bar) != 0, "F4 nonintegral phase-ratio witness")
    words = (
        (ONE, TWO, THREE, JROOT, (1, 1, 0, 0), ZERO, RHO),
        (ZERO, ONE, TWO, ZERO, JROOT, (1, -1, 0, 0), RHO_INV),
        (ONE, ONE, ONE, ONE, ONE, ONE, ONE),
    )
    comparisons = 0
    for word in words:
        for start_clock in range(14):
            z = tuple(mul(a, w) for w in word)
            z_prime = tuple(mul(a_bar, w) for w in word)
            c = start_clock
            record = gram(z)
            for n in range(15):
                equal(gram(z), gram(z_prime), "F4 full Gram fibre")
                equal(record, gram(z), "F4 representative-free record recurrence")
                comparisons += 1
                if n < 14:
                    next_c, next_z = raw_step(c, z)
                    prime_c, next_prime = raw_step(c, z_prime)
                    record_c, next_record = record_step(c, record)
                    equal((prime_c, record_c), (next_c, next_c), "F4 clock agreement")
                    c, z, z_prime, record = next_c, next_z, next_prime, next_record
    equal(comparisons, 630, "F4 paired boundary count")
    return "fibres=3 initial_clocks=14 paired_boundaries=630"


def prepared_outputs(u, v):
    a = add(mul(add(ONE, RHO), u), mul(sub(ONE, RHO), v))
    b = add(mul(sub(ONE, RHO), u), mul(add(ONE, RHO), v))
    return a, b


def audit_f5(context):
    u_values = (ZERO, ONE, neg(ONE), JROOT)
    v_values = (ZERO, ONE, RHO, RHO_INV)
    old_values = (ZERO, ONE, JROOT, (1, 1, 0, 0), (2, -1, 0, 0))
    cases = 0
    boundaries = 0
    valid_zero_records = 0
    for case_index, (u1, u2, v1, v2, old) in enumerate(
            product(u_values, u_values, v_values, v_values, old_values)):
        initial = (scale(2, u1), scale(2, u2), scale(2, v1), scale(2, v2),
                   old, ZERO, ZERO)
        a1, b1 = prepared_outputs(u1, v1)
        a2, b2 = prepared_outputs(u2, v2)
        expected_endpoint = (a1, a2, ZERO, ZERO, b2, old, b1)
        expected_read = gram((old, b1, b2))
        invariants = full_invariants(initial)
        equal(invariants[2],
              4 * sum(account(t) for t in (u1, u2, v1, v2)) + account(old),
              "F5 prepared energy formula")
        c, z = 0, initial
        record = gram(z)
        for n in range(15):
            equal(c, n % 14, "F5 clock")
            equal(full_invariants(z), invariants, "F5 full S/h/E conservation")
            equal(record, gram(z), "F5 exact Gram continuation")
            status, readout = read_final(c, record)
            if c in (6, 7, 8):
                equal(status, "VALID", "F5 valid reader status")
                equal(z, expected_endpoint, "F5 prepared complete endpoint")
                equal(readout, expected_read, "F5 ordered archive readout")
                if all(entry == ZERO for row in readout for entry in row):
                    valid_zero_records += 1
            else:
                equal((status, readout), ("NOT_IN_WINDOW", None), "F5 outside window")
            if n == 3:
                equal(z[4], b1, "F5 first output in continuing receiver")
            if 4 <= n <= 8:
                equal(z[6], b1, "F5 directly retained first output")
            if 1 <= n <= 8:
                equal(z[5], old, "F5 old occupied receiver content")
            feed_program_certificate(context["program_hash"], "P", case_index,
                                     n, c, z, invariants[2])
            boundaries += 1
            if n < 14:
                previous_c, previous_z, previous_record = c, z, record
                c, z = raw_step(previous_c, previous_z)
                record_c, record = record_step(previous_c, previous_record)
                equal(record_c, c, "F5 record clock")
        equal((c, z), (0, initial), "F5 complete fourteen-tick return")
        equal(record, gram(initial), "F5 record fourteen-tick return")
        cases += 1
    equal(cases, 1280, "F5 prepared case count")
    equal(boundaries, 19200, "F5 boundary count")
    context["f5_complete"] = True
    return f"cases={cases} boundaries={boundaries} zero_VALID_records={valid_zero_records}"


def audit_f6(context):
    alphabets = ((ONE, (1, 2, 0, 0)), (ONE, scale(2, RHO)))
    cases = 0
    boundaries = 0
    for alphabet in alphabets:
        for initial in product(alphabet, repeat=7):
            require(all(a != ZERO for a in initial), "F6 all seven slots occupied")
            invariants = full_invariants(initial)
            c, z = 0, initial
            record = gram(z)
            for n in range(15):
                equal(c, n % 14, "F6 clock")
                equal(full_invariants(z), invariants, "F6 occupied S/h/E")
                equal(record, gram(z), "F6 occupied Gram continuation")
                status, readout = read_final(c, record)
                if c in (6, 7, 8):
                    equal(status, "VALID", "F6 reader window")
                    equal(readout, gram((z[5], z[6], z[4])), "F6 actual ordered subrecord")
                else:
                    equal((status, readout), ("NOT_IN_WINDOW", None), "F6 outside window")
                feed_program_certificate(context["program_hash"], "O", cases,
                                         n, c, z, invariants[2])
                boundaries += 1
                if n < 14:
                    previous_c, previous_z, previous_record = c, z, record
                    c, z = raw_step(previous_c, previous_z)
                    record_c, record = record_step(previous_c, previous_record)
                    equal(record_c, c, "F6 record clock")
            equal((c, z), (0, initial), "F6 dirty complete-state return")
            equal(record, gram(initial), "F6 dirty record return")
            cases += 1
    equal(cases, 256, "F6 occupied input count")
    equal(boundaries, 3840, "F6 occupied boundary count")
    context["f6_complete"] = True
    return f"cases={cases} boundaries={boundaries}"


def audit_f7(context):
    initial = tuple(add(ONE, scale(2, power(JROOT, k))) for k in range(7))
    initial_g = gram(initial)
    invariants = full_invariants(initial)
    steps = 0
    for start_clock in range(14):
        c, z, record = start_clock, initial, initial_g
        for _ in range(14):
            equal(record, gram(z), "F7 boundary Gram")
            equal(full_invariants(z), invariants, "F7 S/h/E")
            previous_raw = raw_inverse(c, z)
            equal(raw_step(*previous_raw), (c, z), "F7 raw forward after inverse")
            previous_record = record_inverse(c, record)
            equal(record_step(*previous_record), (c, record), "F7 record forward after inverse")
            next_c, next_z = raw_step(c, z)
            record_c, next_record = record_step(c, record)
            equal(record_c, next_c, "F7 clock agreement")
            equal(raw_inverse(next_c, next_z), (c, z), "F7 raw inverse after forward")
            equal(record_inverse(record_c, next_record), (c, record),
                  "F7 record inverse after forward")
            equal(next_record, gram(next_z), "F7 forward Gram recurrence")
            c, z, record = next_c, next_z, next_record
            steps += 1
        equal((c, z), (start_clock, initial), "F7 arbitrary-clock complete cycle")
        equal(record, initial_g, "F7 arbitrary-clock record cycle")
    equal(steps, 196, "F7 inverse step count")
    return "initial_clocks=14 complete_cycles=14 bidirectional_steps=196"


def main():
    context = {"program_hash": sha256()}
    groups = (audit_f1, audit_f2, audit_f3, audit_f4, audit_f5, audit_f6, audit_f7)
    failures = []
    print("C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N exact finite audit")
    print("STATUS=NON-CANONICAL/L1/candidate-C; universal proof separate")
    for index, group in enumerate(groups, start=1):
        try:
            summary = group(context)
        except Exception as exc:
            failures.append(index)
            print(f"F{index} FAIL {type(exc).__name__}: {exc}")
        else:
            print(f"F{index} PASS {summary}")
    print("PAIR_SHA256=" + context.get("pair_sha256", "INCOMPLETE"))
    if context.get("f5_complete") and context.get("f6_complete"):
        print("PROGRAM_SHA256=" + context["program_hash"].hexdigest())
    else:
        print("PROGRAM_SHA256=INCOMPLETE")
    if failures:
        print("RESULT=FAIL failed_groups=" + ",".join(map(str, failures)))
        return 1
    print("RESULT=PASS groups=7; no physical or public-status promotion")
    return 0


if __name__ == "__main__":
    sys.exit(main())
