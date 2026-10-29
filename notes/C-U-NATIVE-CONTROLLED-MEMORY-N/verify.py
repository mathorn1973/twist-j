#!/usr/bin/env python3
"""Exact audit of the declared native controlled memory candidate.

Standard library only. No imported model, floating point, or sampled inputs.
This audits finite algebra; physical preparation and readout are not derived.
"""

from collections import Counter
from itertools import product


def mod(values):
    return tuple(v % 5 for v in values)


def theta(n):
    return bin(n).count("1") % 2


def native(x, bit):
    a, b, c, d, q, r = x
    index = (sum(x) + 2 * bit) % 5
    if index == 0:
        out = (b, a, d, c, q, r)
    elif index == 1:
        out = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        out = (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r)
    elif index == 3:
        out = (2-a, 1-b, 3-c, 4-d, 1-q, 1-r)
    else:
        out = (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)
    return mod(out), index


def evolve_three(x):
    for bit in (0, 1, 1):
        x, _ = native(x, bit)
    return x


def prepare(new, old, control):
    return mod((new, old, 4-new, 1-old, control, 0))


def source_read(port):
    a, c, q, r = port
    total, difference = (a+c) % 5, (a-c-2) % 5
    square = total * total % 5
    if square == 4:
        zhat = (2*total+q+r) % 5
        result = (0, (total*zhat*difference-1) % 5)
    elif square == 1:
        zhat = (q+r) % 5
        result = (1, (3+2*total*zhat*difference) % 5)
    else:
        return None
    return result if zhat in (1, 4) else None


def memory_read(port):
    b, d, q, r = port
    total, difference = (b+d) % 5, (b-d-1) % 5
    square = total * total % 5
    if square == 4:
        zhat = (2*total+q+r) % 5
        result = (0, total*zhat*difference % 5)
    elif square == 1:
        zhat = (q+r) % 5
        result = (1, (1+3*total*zhat*difference) % 5)
    else:
        return None
    return result if zhat in (1, 4) else None


def readings(x):
    a, b, c, d, q, r = x
    return source_read((a, c, q, r)), memory_read((b, d, q, r))


def logical(x):
    left, right = readings(x)
    if left is None or right is None:
        return None
    assert left[0] == right[0], ("control mismatch", x, left, right)
    return left[0], left[1], right[1]


def chart(x):
    a, b, c, d, _, _ = x
    return mod((a+c, b+d, a-c-2, b-d-1, sum(x)))


def sector(x):
    a_sum, b_sum, _, _, z = chart(x)
    if z not in (1, 4):
        return None
    if a_sum == b_sum and b_sum*b_sum % 5 == 4:
        return 0
    if (a_sum+b_sum) % 5 == 0 and b_sum*b_sum % 5 == 1:
        return 1
    return None


def pair_shift(x, pair, amount):
    y = list(x)
    first, second = pair
    y[first] = (y[first]+amount) % 5
    y[second] = (y[second]-amount) % 5
    return tuple(y)


def paired_port_shift(x, amount):
    return pair_shift(x, (5, 4), amount)


def emit(name, **counts):
    print("PASS " + name + " " + " ".join("%s=%s" % item for item in counts.items()))


def main():
    inputs = list(product(range(5), range(5), (0, 1)))
    assert len({prepare(*labels) for labels in inputs}) == 50
    prefixes = {}
    source_pair, memory_pair = (0, 2), (1, 3)
    for new, old, control in inputs:
        start = prepare(new, old, control)
        assert start[:4:2] == (new, (4-new) % 5)
        assert (start[1], start[3]) == (old, (1-old) % 5)
        assert start[4:] == (control, 0)
        if control == 0:
            expected = [start,
                mod((old, new, 1-old, 4-new, 0, 0)),
                mod((1+old, 2+new, 2-old, 1-new, 1, 0)),
                mod((1-old, 4-new, 1+old, 3+new, 1, 1))]
            word = (0, 2, 4)
            output = (0, old, new)
        else:
            expected = [start,
                mod((1+new, old-1, -new, -old, 4, 0)),
                start, mod((2-new, 1-old, 4+new, 3+old, 0, 1))]
            word = (1, 1, 3)
            output = (1, new, old)
        actual = [start]
        selected = []
        for n in range(3):
            after, which = native(actual[-1], theta(n))
            actual.append(after)
            selected.append(which)
        assert actual == expected, ("prefix", new, old, control, actual, expected)
        assert tuple(selected) == word
        for n, x in enumerate(actual):
            if control == 0 and n < 3:
                assert readings(x) == (None, None)
            else:
                assert logical(x) == output, ("readout", n, x, output, readings(x))
        prefixes[(new, old, control)] = actual
    emit("product_preparation_and_prefix", inputs=50, checkpoints=200)

    shell = set()
    for control in (0, 1):
        b_values = (2, 3) if control == 0 else (1, 4)
        for b_sum, z, cs, d, r in product(b_values, (1, 4), range(5), range(5), range(5)):
            a_sum = b_sum if control == 0 else -b_sum
            x = mod((3*(a_sum+cs+2), 3*(b_sum+d+1),
                     3*(a_sum-cs-2), 3*(b_sum-d-1), z-a_sum-b_sum-r, r))
            assert sector(x) == control
            assert x not in shell
            shell.add(x)
    direct = {x for x in product(range(5), repeat=6) if sector(x) is not None}
    assert shell == direct and len(shell) == 1000
    fibers = Counter(logical(x) for x in shell)
    assert len(fibers) == 50 and set(fibers.values()) == {20}
    assert {key[0] for key in fibers} == {0, 1}
    for states in prefixes.values():
        assert states[-1] in shell
    emit("complete_tail_carrier", states=1000, logical_outputs=50, states_per_output=20)

    transitions = 0
    for x in sorted(shell):
        a_sum, b_sum, cs, d, z = chart(x)
        invariants = mod((a_sum*a_sum, b_sum*b_sum, a_sum*z*cs, b_sum*z*d))
        for bit in (0, 1):
            y, which = native(x, bit)
            assert which in (1, 3, 4)
            assert y in shell and sector(y) == sector(x)
            assert logical(y) == logical(x)
            aa, bb, cc, dd, zz = chart(y)
            assert mod((aa*aa, bb*bb, aa*zz*cc, bb*zz*dd)) == invariants
            transitions += 1
    assert transitions == 2000
    emit("closed_tail_all_bits", transitions=transitions)

    response_cases = 0
    for new, old, control in inputs:
        x = prepare(new, old, control)
        y = evolve_three(x)
        for amount in range(5):
            for incoming, opposite in ((source_pair, memory_pair), (memory_pair, source_pair)):
                outgoing = opposite if control == 0 else incoming
                assert evolve_three(pair_shift(x, incoming, amount)) == pair_shift(y, outgoing, -amount)
                response_cases += 1
    assert response_cases == 500
    emit("raw_response_covariance", complete_state_equalities=response_cases)

    for x in sorted(shell):
        for amount in range(5):
            y = paired_port_shift(x, amount)
            assert y in shell and logical(y) == logical(x)
    emit("paired_port_record_blindness", comparisons=5000)

    image = Counter(evolve_three(x) for x in product(range(5), repeat=6))
    assert len(image) == 3125 and set(image.values()) == {5}
    assert all(sum(x) % 5 == 1 for x in image)
    emit("origin_zero_synchronization", input_heads=15625, image_heads=3125, fiber_size=5)

    dependencies = {}
    checked = 0
    blocks = ((0, 2), (1, 3), (4,), (5,))
    for x in product(range(5), repeat=6):
        z = sum(x) % 5
        if z not in (1, 4):
            continue
        for bit in (0, 1):
            y, which = native(x, bit)
            expected_index = {(1, 0): 1, (1, 1): 3, (4, 0): 4, (4, 1): 1}[(z, bit)]
            assert which == expected_index
            assert sum(y) % 5 == (1 if bit else 4)
            if which == 1:
                expected = mod((-x[2], -x[3], -x[0], -x[1], -x[4], -x[5]))
            else:
                offset = (2, 1, 3, 4, 1 if which == 3 else 2, 1)
                expected = mod(v-u for u, v in zip(x, offset))
            assert y == expected
            for block in blocks:
                key = (z, bit, block, tuple(x[i] for i in block))
                value = tuple(y[i] for i in block)
                if key in dependencies:
                    assert dependencies[key] == value
                else:
                    dependencies[key] = value
            checked += 1
    assert checked == 12500
    emit("synchronized_closed_block_law", point_bit_cases=checked, raw_blocks=4)

    # Audit the finite identities underlying the all-time affine argument.
    p = (2, 3, 0, 1, 4, 5)
    assert tuple(p[p[i]] for i in range(6)) == tuple(range(6))
    contexts = 0
    for start in range(3, 67):
        count_b = 0
        for end in range(start, start+17):
            if end > start:
                step = end-1
                count_b += int(theta(step) != theta(step-1))
            assert count_b % 2 == (theta(end-1) ^ theta(start-1))
            contexts += 1
        for k in range(1, 13):
            assert theta(2**k) == 1 and theta(2**k+1) == 0
            witness = 2**k + (1 if theta(start-1) else 2)
            assert theta(witness-1) == theta(start-1)
    emit("affine_boundary_finite_identity_audit", intervals=contexts, proof="BOUNDARY.md")

    # These mutations are explicitly rejected; they are not alternate models.
    changed_control = prepare(1, 2, 1)
    assert logical(evolve_three(changed_control))[1:] != (2, 1)
    changed_old = prepare(1, 3, 0)
    assert logical(evolve_three(changed_old)) != (0, 2, 1)
    zero = prepare(0, 2, 0)
    assert readings(zero) == (None, None)
    assert memory_read((evolve_three(zero)[1], evolve_three(zero)[3],
                        evolve_three(zero)[4], evolve_three(zero)[5])) == (0, 0)
    x = prepare(1, 2, 0)
    assert evolve_three(pair_shift(x, source_pair, 1)) != pair_shift(evolve_three(x), memory_pair, 1)
    emit("negative_controls", checks=4)
    print("PASS ALL exact_native_controlled_memory groups=9")


if __name__ == "__main__":
    main()
