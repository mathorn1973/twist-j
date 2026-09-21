#!/usr/bin/env python3
"""Exact ideal-pulse audit, not an experimental ion-device measurement.

All nonzero amplitudes are powers of i, recorded by an exponent modulo four.
The five D levels are numbered 0,...,4; g=5 is an auxiliary internal level.
Three ions S,P,M share one oscillator.  The selected blue sideband couples
|D_k,1> and |g,0>; an occupied |g,1> on the addressed ion is OUT OF DOMAIN,
not a silently dark state.  Thus the oscillator cutoff is never used as a
physical boundary condition.  Proof of the domain is in PULSE-PROOF.md.

This file contains no fitted parameters, floating point, external dependency,
random input, or solver selecting the desired pulse sequence.
"""

import csv
from itertools import product
from pathlib import Path


G_LEVEL = 5
SOURCE, PORT, ARCHIVE = range(3)
NATIVE_LABELS = (1, 2, 3, 4)


class PulseDomainError(ValueError):
    """The selected exact doublet model does not cover this state."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def basis(s=0, p=0, m=0, bus=0):
    return ((s, p, m), bus, 0)


def pulse(kind, ion, level, area):
    """Area is an integer multiple of pi; the optical phase is zero."""
    if kind not in ("R", "B") or ion not in range(3):
        raise ValueError("invalid pulse address")
    if level not in range(5) or area not in (-2, -1, 1, 2):
        raise ValueError("invalid pulse level or area")
    return (kind, ion, level, area)


def apply_pulse(state, operation):
    levels, bus, phase = state
    if len(levels) != 3 or any(x not in range(6) for x in levels):
        raise PulseDomainError("invalid internal level")
    if bus not in (0, 1):
        raise PulseDomainError("oscillator occupation outside proved domain")
    kind, ion, selected, area = operation
    current = levels[ion]
    active = current in (selected, G_LEVEL)
    if kind == "B":
        if current == G_LEVEL and bus == 1:
            raise PulseDomainError("active |g,1> requires |D_k,2>")
        active = ((current == selected and bus == 1)
                  or (current == G_LEVEL and bus == 0))
    if not active:
        return state
    # exp(-i area*pi*sigma_x/2), exactly at these integer pulse areas.
    if abs(area) == 2:
        return (levels, bus, (phase + 2) % 4)
    changed = list(levels)
    changed[ion] = G_LEVEL if current == selected else selected
    if kind == "B":
        bus = 1 - bus
    return (tuple(changed), bus, (phase - area) % 4)


def run(sequence, state):
    for operation in sequence:
        state = apply_pulse(state, operation)
    return state


def inverse(sequence):
    return tuple((kind, ion, level, -area)
                 for kind, ion, level, area in reversed(sequence))


def R(ion, level, area):
    return pulse("R", ion, level, area)


def B(ion, level, area):
    return pulse("B", ion, level, area)


def local_q(ion, u, v):
    return (R(ion, v, -1), R(ion, u, 1), R(ion, v, 1))


def local_x2(ion):
    result = ()
    for u, v in ((0, 3), (3, 1), (1, 4), (4, 2)):
        result += local_q(ion, u, v)
    return result


def local_neg(ion):
    return ((R(ion, 1, 2), R(ion, 2, 2))
            + local_q(ion, 1, 4) + local_q(ion, 2, 3))


def controlled_minus(control, target, c):
    """Identity except for X^-1 on target when the control level is c."""
    require(control != target, "controlled operation needs distinct ions")
    encode = (R(control, c, 1), B(control, c, 1))
    move = ()
    for j in range(4):
        move += (B(target, j + 1, -1), B(target, j, 1),
                 B(target, j + 1, 1))
    return encode + move + inverse(encode)


def writer():
    # Physical source 0 is LOW; levels 1,2,3 are the three HIGH code levels.
    # The unused physical source level 4 is an explicit HIGH extension.
    return local_x2(PORT) + controlled_minus(SOURCE, PORT, 0)


def balanced(residue):
    residue %= 5
    return residue if residue <= 2 else residue - 5


def add(control, target, gain):
    require(gain in (-1, 1), "only the two preregistered SUM gains")
    result = ()
    for c in range(1, 5):
        repetitions = -balanced(gain * c)
        block = controlled_minus(control, target, c)
        if repetitions < 0:
            block = inverse(block)
        result += block * abs(repetitions)
    return result


def swap(x, y):
    return (add(x, y, 1) + add(y, x, -1) + add(x, y, 1)
            + local_neg(x))


def cycle(wait_ticks):
    require(wait_ticks >= 0, "negative wait")
    result = writer() + local_neg(PORT) * wait_ticks
    result += swap(PORT, ARCHIVE)
    if wait_ticks % 2:
        result += local_neg(PORT) + local_neg(ARCHIVE)
    return result


def counts(sequence):
    return (sum(kind == "B" for kind, _, _, _ in sequence),
            sum(kind == "R" for kind, _, _, _ in sequence))


def recorded_value(source):
    return 1 if source == 0 else 2


def expected_cycle(source, deviation, memory, wait_ticks):
    sign = -1 if wait_ticks % 2 else 1
    return basis(source, sign * memory % 5,
                 (deviation + recorded_value(source)) % 5)


def expect_domain_error(function, message):
    try:
        function()
    except PulseDomainError:
        return
    raise AssertionError(message)


def gate_pulse_inventory_and_domains():
    expected_fields = ("index", "kind", "register", "level", "area_pi",
                       "phase_pi", "calibration_key")
    with Path(__file__).with_name("PULSES.tsv").open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        require(tuple(reader.fieldnames) == expected_fields, "pulse TSV schema")
        rows = list(reader)
    require(len(rows) == 28, "frozen writer TSV length")
    decoded = []
    for index, row in enumerate(rows, 1):
        require(int(row["index"]) == index, "pulse TSV chronology")
        require(row["kind"] in ("carrier", "blue"), "pulse TSV kind")
        require(row["register"] in ("S", "P", "M"), "pulse TSV ion")
        level, area, phase = (int(row[field])
                              for field in ("level", "area_pi", "phase_pi"))
        require(area == 1 and phase in (0, 1), "positive pi pulse with fixed phase")
        require(row["calibration_key"]
                == ".".join((row["kind"], row["register"], str(level))),
                "pulse TSV calibration address")
        decoded.append(pulse("R" if row["kind"] == "carrier" else "B",
                             ("S", "P", "M").index(row["register"]),
                             level, -area if phase else area))
    require(tuple(decoded) == writer(), "fixed TSV and compiler differ")
    require(counts(tuple(decoded)) == (14, 14), "fixed writer pulse inventory")
    pairs = 0
    for ion, selected, area in product(range(3), range(5), (-2, -1, 1, 2)):
        carrier = R(ion, selected, area)
        sideband = B(ion, selected, area)
        for current, bus in product(range(6), (0, 1)):
            levels = [0, 0, 0]
            levels[ion] = current
            state = (tuple(levels), bus, 0)
            require(run((carrier,) + inverse((carrier,)), state) == state,
                    "carrier inverse including its phase")
            if current == G_LEVEL and bus == 1:
                expect_domain_error(lambda: apply_pulse(state, sideband),
                                    "a hot active doublet was truncated")
            else:
                require(run((sideband,) + inverse((sideband,)), state) == state,
                        "sideband inverse including its phase")
                pairs += 1
    require(pairs == 660, "pulse-domain audit inventory")
    require(apply_pulse(basis(), R(SOURCE, 0, 1))
            == ((G_LEVEL, 0, 0), 0, 3), "pi is minus i")
    require(apply_pulse(basis(), R(SOURCE, 0, -1))
            == ((G_LEVEL, 0, 0), 0, 1), "minus pi is plus i")
    require(apply_pulse(basis(), R(SOURCE, 0, 2))
            == ((0, 0, 0), 0, 2), "two pi has a minus sign")
    expect_domain_error(lambda: apply_pulse(basis(bus=2), B(SOURCE, 0, 1)),
                        "higher oscillator level was silently accepted")


def gate_local_blocks():
    for ion, u, v, x in product(range(3), range(5), range(5), range(5)):
        if u == v:
            continue
        inputs = [0, 0, 0]
        inputs[ion] = x
        outputs = list(inputs)
        outputs[ion] = v if x == u else u if x == v else x
        phase = 2 if x == u else 0
        require(run(local_q(ion, u, v), (tuple(inputs), 0, 0))
                == (tuple(outputs), 0, phase), "signed local exchange Q")
    for ion, x in product(range(3), range(5)):
        inputs = [0, 0, 0]
        inputs[ion] = x
        state = (tuple(inputs), 0, 0)
        outputs = list(inputs)
        outputs[ion] = (x + 2) % 5
        require(run(local_x2(ion), state) == (tuple(outputs), 0, 0), "local X squared")
        outputs[ion] = -x % 5
        require(run(local_neg(ion), state) == (tuple(outputs), 0, 0), "phase-correct NEG")
    require(counts(local_x2(PORT)) == (0, 12), "local X squared count")
    require(counts(local_neg(PORT)) == (0, 8), "local NEG count")


def gate_controlled_blocks():
    for control, target in ((SOURCE, PORT), (PORT, ARCHIVE), (ARCHIVE, PORT)):
        for c in range(5):
            mapping = {}
            sequence = controlled_minus(control, target, c)
            require(counts(sequence) == (14, 2), "controlled pulse count")
            for x, y in product(range(5), repeat=2):
                inputs = [0, 0, 0]
                inputs[control], inputs[target] = x, y
                state = (tuple(inputs), 0, 0)
                outputs = list(inputs)
                outputs[target] = (y - (x == c)) % 5
                output = run(sequence, state)
                require(output == (tuple(outputs), 0, 0), "controlled X inverse")
                require(run(inverse(sequence), output) == state, "controlled inverse")
                mapping[(x, y)] = output
            require(len(set(mapping.values())) == 25, "controlled support injectivity")
            for left, right in product(mapping, repeat=2):
                require((mapping[left][2] - mapping[right][2]) % 4 == 0,
                        "controlled matrix-unit relative phase")


def gate_writer():
    require(counts(writer()) == (14, 14), "writer pulse inventory")
    mapping = {}
    for source, deviation, memory in product(range(5), repeat=3):
        output = run(writer(), basis(source, deviation, memory))
        require(output == basis(source, (deviation + recorded_value(source)) % 5, memory),
                "writer including dirty port and unused source level")
        mapping[(source, deviation, memory)] = output
    require(len(set(mapping.values())) == 125, "writer support injectivity")
    code = tuple(product(range(4), range(5), range(5)))
    checked = 0
    for left, right in product(code, repeat=2):
        require((mapping[left][2] - mapping[right][2]) % 4 == 0,
                "writer matrix-unit relative phase")
        checked += 1
    require(checked == 10000, "complete writer matrix-unit inventory")


def gate_sum_swap():
    for gain, x, y in product((-1, 1), range(5), range(5)):
        sequence = add(PORT, ARCHIVE, gain)
        require(counts(sequence) == (84, 12), "SUM uses six controlled blocks")
        require(run(sequence, basis(0, x, y)) == basis(0, x, (y + gain * x) % 5),
                "SUM exact basis and phase")
    for x, y in product(range(5), repeat=2):
        require(run(swap(PORT, ARCHIVE), basis(0, x, y)) == basis(0, y, x),
                "SWAP exact basis and phase")
    require(counts(swap(PORT, ARCHIVE)) == (252, 44), "SWAP pulse inventory")


def gate_cycles():
    certificates = {}
    for k in range(4):
        sequence = cycle(k)
        require(counts(sequence) == (266, 58 + 8 * k + 16 * (k % 2)),
                "cycle pulse inventory")
        output_map = {}
        for source, deviation, memory in product(range(5), repeat=3):
            state = basis(source, deviation, memory)
            output = run(sequence, state)
            require(output == expected_cycle(source, deviation, memory, k),
                    "complete cycle with dirty port and dirty archive")
            output_map[(source, deviation, memory)] = output
        require(len(set(output_map.values())) == 125, "cycle is injective")
        certificates[k] = output_map
    return certificates


def gate_matrix_units(certificates):
    # This checks the exact matrix-unit action from the already computed
    # support/phase certificate, not by replaying pulses on every pair.
    code = tuple(product(range(4), range(5), range(5)))
    require(len(code) == 100, "code-domain dimension")
    checked = 0
    for k in range(4):
        mapping = certificates[k]
        for left, right in product(code, repeat=2):
            out_left, out_right = mapping[left], mapping[right]
            require(out_left[:2] == expected_cycle(*left, k)[:2], "left matrix support")
            require(out_right[:2] == expected_cycle(*right, k)[:2], "right matrix support")
            require((out_left[2] - out_right[2]) % 4 == 0,
                    "relative phase on a code matrix unit")
            checked += 1
    require(checked == 40000, "four complete code matrix-unit inventories")


def native_generator(index, x):
    a, b, c, d, q, r = x
    rows = (
        (b, a, d, c, q, r),
        (-c, -d, -a, -b, -q, -r),
        (2 - c, 1 - d + r, 2 - a, 1 - b - r, 1 - q, -r),
        (2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r),
        (2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r),
    )
    return tuple(value % 5 for value in rows[index])


def native_step(x, bit):
    require(bit in (0, 1), "binary native selector")
    return native_generator((sum(x) + 2 * bit) % 5, x)


def paired_shift(x, delta):
    return x[:4] + ((x[4] - delta) % 5, (x[5] + delta) % 5)


def transported_label(x, elapsed):
    return ((-1 if elapsed % 2 else 1) * sum(x[:4])) % 5


def gate_moving_native_chart():
    current = [(h, 0, 0, 0, (1 - h) % 5, 0) for h in NATIVE_LABELS]
    words = tuple(word for length in range(5)
                  for word in product((0, 1), repeat=length))
    checked = 0
    for n in range(3, 13):
        require(len({(sum(x) % 5, x[5]) for x in current}) == 1,
                "moving code has a common trace and reference port")
        require(len({paired_shift(x, delta)
                     for x, delta in product(current, range(5))}) == 20,
                "moving chart has twenty distinct native points")
        for physical_source, start in enumerate(current):
            h = NATIVE_LABELS[physical_source]
            require(transported_label(start, n - 3) == h, "moving source label")
            for delta, word in product(range(5), words):
                free = start
                changed = paired_shift(start, delta)
                for elapsed, bit in enumerate(word, 1):
                    free = native_step(free, bit)
                    changed = native_step(changed, bit)
                    sign = -1 if elapsed % 2 else 1
                    require(changed == paired_shift(free, sign * delta),
                            "native source trajectory and moving deviation")
                    require(sum(free) % 5 in (1, 4), "stable trace region")
                    require(transported_label(free, n - 3 + elapsed) == h,
                            "transported source label after arbitrary bit word")
                checked += 1
        bit = n.bit_count() % 2
        current = [native_step(x, bit) for x in current]
    require(len(words) == 31 and checked == 6200, "native chart audit inventory")


def gate_negative_controls():
    # Without V-dagger the selected source retains the oscillator marker.
    missing_uncompute = controlled_minus(SOURCE, PORT, 0)[:-2]
    require(run(missing_uncompute, basis()) != basis(0, 4, 0),
            "missing source uncompute was not detected")
    require(run(missing_uncompute, basis())[1] == 1,
            "uncomputed bus has no surviving record")
    # Without the odd-wait correction, the stored pointer has the wrong sign.
    uncorrected_odd = writer() + local_neg(PORT) + swap(PORT, ARCHIVE)
    require(run(uncorrected_odd, basis()) != expected_cycle(0, 0, 0, 1),
            "missing odd-wait sign correction was not detected")
    # Change exactly one minus-pi sideband in the first target transposition.
    wrong_sign = list(controlled_minus(SOURCE, PORT, 0))
    require(wrong_sign[2] == B(PORT, 1, -1), "negative-control pulse address")
    wrong_sign[2] = B(PORT, 1, 1)
    require(run(tuple(wrong_sign), basis(0, 1, 0)) != basis(0, 0, 0),
            "wrong target pulse sign was not detected")
    # Dropping the two 2pi phases preserves populations but destroys coherence.
    bare_neg = local_q(PORT, 1, 4) + local_q(PORT, 2, 3)
    outputs = [run(bare_neg, basis(0, x, 0)) for x in range(5)]
    require(all(output[:2] == basis(0, -x % 5, 0)[:2]
                for x, output in enumerate(outputs)), "bare NEG population witness")
    require(len({output[2] for output in outputs}) > 1,
            "bare NEG relative phase defect was not detected")
    # Starting with a hot bus is outside the proved implementation domain.
    # This rejection is not an assertion about the full physical hot-bus unitary.
    expect_domain_error(lambda: run(writer(), basis(bus=1)),
                        "hot bus was treated as a valid cold-bus implementation")


def main():
    gate_pulse_inventory_and_domains()
    print("G1 PASS: fixed 28-pulse TSV, exact phases and explicit doublet domains")
    gate_local_blocks()
    print("G2 PASS: signed local exchanges, X^2 and eight-carrier phase-correct NEG")
    gate_controlled_blocks()
    print("G3 PASS: five controlled X^-1 blocks, inverses and all pair matrix units")
    gate_writer()
    print("G4 PASS: writer on 125 triples and 10000 code matrix units; phases +1")
    gate_moving_native_chart()
    print("G5 PASS: 6200 moving-chart cases; n=3..12 and all bit words length<=4")
    gate_sum_swap()
    print("G6 PASS: SUM +/-1 and SWAP; helper levels and shared mode restored")
    certificates = gate_cycles()
    gate_matrix_units(certificates)
    print("G7 PASS: 500 cycles and 40000 code matrix units; 266 blue + (58+8k+16[k odd]) carrier")
    gate_negative_controls()
    print("G8 PASS: uncompute, parity, pulse-sign, coherence and hot-bus controls")
    print("VERDICT: IDEAL-ION-WRITER; conditional pulse theorem, no device measurement")


if __name__ == "__main__":
    main()
