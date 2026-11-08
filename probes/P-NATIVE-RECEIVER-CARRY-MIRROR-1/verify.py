#!/usr/bin/env python3
"""Exact native receiver / carry mirror audit. NON-CANONICAL / L1.

The exposed source package supplies the native rows and proposed circuit.
This verifier combines its contracts, independently cross-checks integral
arithmetic in the j and lambda bases, and invokes a hash-bound compiled audit.
Only actual receiver cells enter the routed circuit. Initial input labels
are used by assertions after evolution, never to choose its operations.
"""

from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import importlib.util
import json
import sys


FIELD = range(5)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
J = (1, 0, 1, 0)
J_INVERSE = (0, -1, -1, 0)
LAMBDA = (1, -1, 0, 0)
LAMBDA_J = (2, -2, 1, 0)
LAMBDA_J_INVERSE = (-2, 3, -1, 0)
SECTIONS = {"counting": (0, 1, 2, 3, 4), "balanced": (-2, -1, 0, 1, 2)}


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def char(value):
    return (0, 1, -1, -1, 1)[value % 5]


def native_tick(head, bit=0):
    """One declared native generator; bit zero is the original first tick."""
    require(len(head) == 6 and bit in (0, 1), "native dimensions")
    a, b, c, d, q, r = head
    selector = (sum(head) + 2 * bit) % 5
    if selector == 0:
        result = (b, a, d, c, q, r)
    elif selector == 1:
        result = (-c, -d, -a, -b, -q, -r)
    elif selector == 2:
        result = (2 - c, 1 - d + r, 2 - a, 1 - b - r, 1 - q, -r)
    elif selector == 3:
        result = (2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r)
    else:
        result = (2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r)
    return tuple(value % 5 for value in result)


def native_zero_tick(head):
    return native_tick(head, 0)


def forward_word(low, high):
    return 2 * low % 5, (3 * low + 2 * high) % 5


def inverse_word(low, high):
    return 3 * low % 5, (3 * low + 3 * high) % 5


def receiver_load(q, r):
    return (q + r + 2) % 5


def receiver_unload(low, r):
    return (low - r - 2) % 5


def circuit(q, r, high, archive):
    """Fixed four-cell bijection, with two literal boundary observations."""
    low = receiver_load(q, r)
    emitted, high = forward_word(low, high)
    high, archive = archive, high
    returned, high = inverse_word(emitted, high)
    return (receiver_unload(returned, r), r, high, archive), emitted, returned


def native_reader(q):
    require(q in (0, 1, 2), "reader outside the declared native family")
    return -1 if q == 1 else 1


def j_product(left, right):
    cyclic = [0] * 5
    for i, x in enumerate(left):
        for k, y in enumerate(right):
            cyclic[(i + k) % 5] += x * y
    return tuple(cyclic[i] - cyclic[4] for i in range(4))


def lambda_product(left, right):
    """Independent polynomial reduction by lambda^4-5lambda^3+10lambda^2-10lambda+5."""
    polynomial = [0] * 7
    for i, x in enumerate(left):
        for k, y in enumerate(right):
            polynomial[i + k] += x * y
    for degree in (6, 5, 4):
        leading = polynomial[degree]
        for offset, coefficient in enumerate((5, -10, 10, -5)):
            polynomial[degree - 4 + offset] -= leading * coefficient
        polynomial[degree] = 0
    return tuple(polynomial[:4])


def change_basis(value):
    """Substitution x -> 1-x converts either degree-three basis to the other."""
    return tuple(sum(value[i] * comb(i, k) * (-1) ** k for i in range(k, 4))
                 for k in range(4))


def j_residue(value):
    return sum(value) % 5


def j_split(value, section):
    lift = {digit % 5: digit for digit in section}
    output = lift[j_residue(value)]
    remainder = (value[0] - output, *value[1:])
    last, modulus = divmod(sum(remainder), 5)
    require(modulus == 0, "j-basis integral division")
    first = remainder[0] - last
    second = remainder[1] + first - last
    third = remainder[2] + second - last
    carry = (first, second, third, last)
    require(j_product(LAMBDA, carry) == remainder, "j-basis division certificate")
    return output, carry


def lambda_split(value, section):
    lift = {digit % 5: digit for digit in section}
    output = lift[value[0] % 5]
    require((value[0] - output) % 5 == 0, "lambda-basis integral division")
    last = -(value[0] - output) // 5
    carry = (value[1] - 10 * last, value[2] + 10 * last,
             value[3] - 5 * last, last)
    reconstructed = lambda_product((0, 1, 0, 0), carry)
    require((reconstructed[0] + output, *reconstructed[1:]) == value,
            "lambda-basis division certificate")
    return output, carry


def integral_edge(unit, lambda_unit, digit, section):
    j_value = j_product(unit, (digit, 0, 0, 0))
    lambda_value = lambda_product(lambda_unit, (digit, 0, 0, 0))
    require(change_basis(j_value) == lambda_value, "independent multiplication bases")
    output, carry = j_split(j_value, section)
    other_output, other_carry = lambda_split(lambda_value, section)
    require(output == other_output and change_basis(carry) == other_carry,
            "independent integral carries")
    require(change_basis(other_carry) == carry, "basis round trip")
    return output, carry


def carry_digits(carry, section):
    first, tail = j_split(carry, section)
    other_first, other_tail = lambda_split(change_basis(carry), section)
    require(first == other_first and change_basis(tail) == other_tail,
            "independent carry reader")
    return first % 5, j_residue(tail)


def integral_audit():
    require(j_product(J, J_INVERSE) == ONE, "integral unit inverse in j basis")
    require(lambda_product(LAMBDA_J, LAMBDA_J_INVERSE) == ONE,
            "integral unit inverse in lambda basis")
    require(change_basis(J) == LAMBDA_J and change_basis(J_INVERSE) == LAMBDA_J_INVERSE,
            "unit basis identities")
    rows = []
    reader_cases = quotient_cases = 0
    for section_name, section in SECTIONS.items():
        lift = {digit % 5: digit for digit in section}
        for low, high in product(FIELD, repeat=2):
            word = (lift[low], lift[high], 0, 0)
            for unit, expected in ((LAMBDA_J, forward_word(low, high)),
                                   (LAMBDA_J_INVERSE, inverse_word(low, high))):
                first, carry = lambda_split(lambda_product(unit, word), section)
                require((first % 5, carry[0] % 5) == expected,
                        "integral two-digit quotient map")
                quotient_cases += 1
        for digit in section:
            emitted, forward_carry = integral_edge(J, LAMBDA_J, digit, section)
            direct, direct_carry = integral_edge(J_INVERSE, LAMBDA_J_INVERSE, digit, section)
            returned, mirror_carry = integral_edge(J_INVERSE, LAMBDA_J_INVERSE, emitted, section)
            require(emitted % 5 == 2 * digit % 5 and direct % 5 == 3 * digit % 5,
                    "integral output residues")
            require(returned == digit, "exact representative return")
            conjugate_carry = tuple(-x for x in j_product(J_INVERSE, forward_carry))
            require(mirror_carry == conjugate_carry, "full integral mirror identity")
            require(j_residue(mirror_carry) == 2 * j_residue(forward_carry) % 5,
                    "paired residue multiplier")
            slopes = None
            for reader_section in SECTIONS.values():
                vf, uf = carry_digits(forward_carry, reader_section)
                vi, ui = carry_digits(direct_carry, reader_section)
                require(vf == vi == 3 * digit % 5, "same-input first-residue collision")
                require((uf, ui) == (digit % 5, -digit % 5), "second carry coefficients")
                require(char(vf) == char(vi) == -char(j_residue(mirror_carry)),
                        "same-input versus paired signs")
                if digit:
                    slopes = (uf * pow(vf, -1, 5) % 5, ui * pow(vi, -1, 5) % 5)
                    require(slopes == (2, 3), "fixed slope discriminator")
                else:
                    require((emitted, direct, returned) == (0, 0, 0), "zero letters")
                    require(forward_carry == direct_carry == mirror_carry == ZERO,
                            "zero has no directional reading")
                reader_cases += 1
            rows.append([section_name, digit, emitted, direct,
                         list(forward_carry), list(direct_carry), list(mirror_carry), slopes])
    require(quotient_cases == 100 and reader_cases == 20, "integral coverage")
    return {"section_letter_rows": len(rows), "carry_reader_cases": reader_cases,
            "quotient_section_direction_cases": quotient_cases,
            "fixed_input_slopes": [2, 3],
            "integral_rows_sha256": sha256(json.dumps(rows, separators=(",", ":")).encode("ascii")).hexdigest()}


def receiver_audit():
    states = tuple(product(FIELD, repeat=4))
    images = tuple(circuit(*state)[0] for state in states)
    require(len(set(images)) == 625, "complete four-register bijection")
    for (q, r, high, archive), image in zip(states, images):
        loaded = receiver_load(q, r)
        require(image == (q, r, (loaded + 3 * archive) % 5, (3 * loaded + 2 * high) % 5),
                "occupied four-register closed affine formula")
    require(all(circuit(*image)[0] == state for state, image in zip(states, images)),
            "complete occupied four-register involution")
    for low, high in product(FIELD, repeat=2):
        require(inverse_word(*forward_word(low, high)) == (low, high), "two-digit inverse")
        require(forward_word(*inverse_word(low, high)) == (low, high), "two-digit reverse inverse")

    counts = [0] * 5
    table = {}
    phase_images = [[set() for _ in FIELD] for _ in (0, 1)]
    same_input = literal_inverse = wrong_offset = incidental_sign = 0
    for pistons in states:
        head = (*pistons, 0, 1)
        primary = native_zero_tick(head)
        q, r = primary[4:]
        endpoint, emitted, returned = circuit(q, r, 0, 0)
        # The secondary input is the actual emitted low, added to a fixed reference.
        secondary = [4, 0, 0, 0, 0, 1]
        secondary[0] = (secondary[0] + emitted) % 5
        secondary = native_zero_tick(tuple(secondary))
        final_q, final_r, mirrored_high, archived_high = endpoint
        require((final_q, final_r) == (q, r), "native receiver restoration")

        # Initial trace is consulted only here, as an audit reference after evolution.
        trace = sum(head) % 5
        counts[trace] += 1
        for bit in (0, 1):
            phase_images[bit][trace].add(sum(native_tick(head, bit)) % 5)
        loaded = receiver_load(q, r)
        if trace == 0:
            require((q, r, loaded) == (0, 1, 3), "unchanged zero-sheet control")
            continue
        require(loaded == returned == trace, "marked transfer and round trip")
        require((emitted, archived_high, mirrored_high) == (2 * trace % 5, 3 * trace % 5, trace),
                "actual low and carry residues")
        first_sign = native_reader(final_q)
        paired_sign = native_reader(secondary[4])
        require(first_sign == char(trace) == -char(archived_high), "primary sign")
        require(paired_sign == char(emitted) == -char(mirrored_high) == -first_sign,
                "paired native sign")
        for section in SECTIONS.values():
            digit = {value % 5: value for value in section}[loaded]
            letter, carry = integral_edge(J, LAMBDA_J, digit, section)
            back, mirror = integral_edge(J_INVERSE, LAMBDA_J_INVERSE, letter, section)
            require((letter % 5, back % 5, j_residue(carry), j_residue(mirror)) ==
                    (emitted, returned, archived_high, mirrored_high), "register/integral agreement")
        same_input += int(inverse_word(loaded, 0)[1] == archived_high)
        literal_inverse += int(inverse_word(*forward_word(loaded, 0)) == (loaded, 0))
        wrong_offset += int((q + r) % 5 != trace)
        incidental_sign += int(char(q + r) == char(trace))
        row = (q, r, loaded, emitted, archived_high, mirrored_high,
               first_sign, paired_sign, returned, secondary[4], secondary[5])
        require(row == table.setdefault(trace, row), "constant marked boundary class")

    require(counts == [125] * 5, "all native piston heads")
    require(same_input == literal_inverse == wrong_offset == 500, "negative-control coverage")
    require(incidental_sign == 125, "sign-only offset false positives retained")
    require(tuple(table[trace][:2] for trace in range(1, 5)) ==
            ((0, 4), (1, 4), (1, 0), (2, 0)), "four exact native receiver rows")
    affine_ports = [(a, b, c) for a, b, c in product(FIELD, repeat=3)
                    if all((a * row[0] + b * row[1] + c) % 5 == trace
                           for trace, row in table.items())]
    require(affine_ports == [(1, 1, 2)], "unique affine receiver port")
    require(all(len(image) == 1 for branch in phase_images for image in branch),
            "native phase maps independent of pistons on the ready family")
    maps = [tuple(next(iter(image)) for image in branch) for branch in phase_images]
    require(maps == [(0, 4, 0, 4, 4), (2, 1, 1, 3, 1)], "derived native phase maps")
    ranks = [len(set(mapping[1:])) for mapping in maps]
    require(ranks == [2, 2], "native trace-port rank obstruction")
    return {"native_heads": 625, "admitted_heads": 500, "off_domain_zero_heads": 125,
            "sheet_multiplicities": counts, "occupied_four_register_inverses": 625,
            "two_digit_inverse_words_both_orders": 25,
            "affine_port": list(affine_ports[0]),
            "same_input_inverse_controls": same_input, "full_word_inverse_controls": literal_inverse,
            "omitted_offset_wrong_digits": wrong_offset, "omitted_offset_incidental_signs": incidental_sign,
            "native_phase_maps": maps, "marked_phase_ranks": ranks,
            "marked_rows": [[trace, *row] for trace, row in sorted(table.items())]}


def load_compiled_audit():
    """Verify all local executable dependencies before importing either helper."""
    directory = Path(__file__).resolve().parent
    manifest = json.loads((directory / "RUNTIME_SOURCES.json").read_text(encoding="utf-8"))
    names = {"compiled_audit.py", "arithmetic_compiler.py"}
    require(type(manifest) is dict and set(manifest) == names, "exact runtime source inventory")
    for name in sorted(names):
        entry = manifest[name]
        require(type(entry) is dict and set(entry) == {"sha256", "bytes"}, "runtime metadata schema")
        require(type(entry["bytes"]) is int and entry["bytes"] > 0, "runtime byte count type")
        digest = entry["sha256"]
        require(type(digest) is str and len(digest) == 64 and
                all(character in "0123456789abcdef" for character in digest), "runtime digest form")
        raw = (directory / name).read_bytes()
        require(len(raw) == entry["bytes"] and sha256(raw).hexdigest() == digest,
                "runtime source bytes: " + name)
    spec = importlib.util.spec_from_file_location("native_receiver_compiled_audit", directory / "compiled_audit.py")
    require(spec is not None and spec.loader is not None, "compiled audit import specification")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    if sys.flags.optimize or not __debug__:
        raise SystemExit("Integrity failure: optimization must remain disabled")
    sys.dont_write_bytecode = True
    result = {"scope": "NON-CANONICAL / L1 / candidate-C",
              "integral": integral_audit(), "receiver": receiver_audit()}
    compiled = load_compiled_audit()
    result["compiled"] = compiled.run(native_zero_tick)
    require(type(result["compiled"]) is dict, "compiled summary schema")
    result["status"] = "PASS"
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
