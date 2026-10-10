"""Supplementary exact L1 proof audit for the raw four-piston residue port.

Exploratory results were already exposed. This is not a formal probe or a
retrospective preregistration. Do not execute or import before the public
code-blob pin and readback. Written proofs carry the all-time conclusions.
No runtime source imports, external packages, randomness or file writes.
"""

from collections import Counter
from itertools import product


READ_AT_THREE = {(1, 0): 0, (2, 0): 1, (2, 1): 2, (3, 1): 3, (1, 2): 4}
FIRST_THREE = (
    ((0, 4), (0, 1), (1, 0)),
    ((1, 4), (0, 1), (2, 0)),
    ((1, 0), (4, 0), (2, 1)),
    ((2, 0), (3, 0), (3, 1)),
    ((0, 1), (1, 4), (1, 2)),
)
EXCEPTIONAL = {(0, 0), (3, 0), (3, 3), (1, 3)}


def native_step(n, state):
    """Literal six-coordinate native U, including its original selector."""
    p1, p4, p1p, p4p, q, r = state
    selected = (sum(state) + 2 * (n.bit_count() % 2)) % 5
    if selected == 0:
        out = (p4, p1, p4p, p1p, q, r)
    elif selected == 1:
        out = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif selected == 2:
        out = (2 - p1p, 1 - p4p + r, 2 - p1, 1 - p4 - r, 1 - q, -r)
    elif selected == 3:
        out = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    else:
        out = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    return tuple(value % 5 for value in out)


def triple_step(n, state):
    """Independent selected quotient table; no call to native_step."""
    bit = 0
    remaining = n
    while remaining:
        bit ^= remaining & 1
        remaining //= 2
    z, q, r = state
    if bit == 0:
        out = ((0, q, r), (4, -q, -r), (0, 1 - q, -r),
               (4, 1 - q, 1 - r), (4, 2 - q, 1 - r))[z]
    else:
        out = ((2, 1 - q, -r), (1, 1 - q, 1 - r), (1, 2 - q, 1 - r),
               (3, q, r), (1, -q, -r))[z]
    return tuple(value % 5 for value in out)


def context(n):
    """Sufficient evaluation context tau_n, defined here only for n >= 3."""
    if n < 3:
        raise ValueError("The compact reading context requires n >= 3.")
    m = (n - 1) // 2
    alternating_sum = 0
    sign = 1
    while m:
        alternating_sum += sign * m
        sign = -sign
        m //= 2
    sigma = 1 if n % 2 else -1
    z = (4 + 2 * ((n - 1).bit_count() % 2)) % 5
    return sigma, z, (alternating_sum - 1) % 5


def restore_at_three(tau, q, r):
    sigma, z, nu = tau
    return (1 + sigma * (q - z) + nu) % 5, (sigma * r - nu) % 5


def read_with_context(tau, q, r):
    """Ready-region readout; tau alone does not certify initial readiness."""
    restored = restore_at_three(tau, q, r)
    if restored in READ_AT_THREE:
        return "PRESENT", READ_AT_THREE[restored]
    return "BLANK", None


def read_residue(n, q, r):
    """Read the original sum from actual counter and receiver, with no history."""
    if n < 0:
        raise ValueError("The native counter must be nonnegative.")
    if n < 3:
        return "BLANK", None
    return read_with_context(context(n), q, r)


def support(s):
    sums = {s % 5, (s + 3) % 5, -s % 5, (2 - s) % 5}
    return {(q, r) for q, r in product(range(5), repeat=2) if (q + r) % 5 in sums}


def third_receiver(z, q, r):
    pair = ((q + 1, r + 1), (1 - q, 1 - r), (2 - q, 1 - r),
            (2 - q, 2 - r), (3 - q, 2 - r))[z]
    return tuple(value % 5 for value in pair)


def ring_product(left, right):
    """Exact multiplication in Z[j], Phi_5(j)=0, basis 1,j,j^2,j^3."""
    coefficients = [0] * 7
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            coefficients[i + j] += a * b
    for degree in range(6, 3, -1):
        top = coefficients[degree]
        for shift in range(1, 5):
            coefficients[degree - shift] -= top
        coefficients[degree] = 0
    return tuple(coefficients[:4])


def audit():
    pistons = tuple(product(range(5), repeat=4))
    pairs = tuple(product(range(5), repeat=2))
    restore_checks = 0
    quotient_checks = 0
    histories = {}
    for source in pistons:
        kappa = sum(source) % 5
        state = source + (0, 1)
        triple = ((kappa + 1) % 5, 0, 1)
        history = []
        at_three = None
        for n in range(257):
            assert triple == (sum(state) % 5, state[4], state[5])
            quotient_checks += 1
            if 1 <= n <= 3:
                assert state[4:] == FIRST_THREE[kappa][n - 1]
            if n <= 3:
                history.append(state[4:])
            if n == 3:
                at_three = state[4:]
            if n >= 3:
                assert restore_at_three(context(n), *state[4:]) == at_three
                assert read_residue(n, *state[4:]) == ("PRESENT", kappa)
                restore_checks += 1
            if kappa == 0 and n == 7:
                assert state[4:] == FIRST_THREE[3][2] == (3, 1)
            if n < 256:
                state = native_step(n, state)
                triple = triple_step(n, triple)
        histories[source] = tuple(history)
    assert restore_checks == 158750
    assert quotient_checks == 160625
    assert len({row[0] for row in FIRST_THREE}) == 5
    assert FIRST_THREE[0][1] == FIRST_THREE[1][1]

    # Complete three-tick source census for every common receiver ready.
    # Prefix equivalence is promoted to all-time equivalence only by the proof.
    ready_classes = Counter()
    for q, r in pairs:
        prefix_fibres = Counter()
        tail_fibres = Counter()
        for source in pistons:
            z0 = (sum(source) + q + r) % 5
            state = source + (q, r)
            triple = (z0, q, r)
            prefix = [(q, r)]
            for n in range(3):
                state = native_step(n, state)
                triple = triple_step(n, triple)
                assert triple == (sum(state) % 5, state[4], state[5])
                prefix.append(state[4:])
            assert triple[0] == 1
            assert state[4:] == third_receiver(z0, q, r)
            prefix_fibres[tuple(prefix[:3])] += 1
            tail_fibres[state[4:]] += 1
        expected_prefix = [125, 125, 125, 250] if (q, r) == (3, 0) else [125] * 5
        expected_tail = [125, 125, 125, 250] if (q, r) in EXCEPTIONAL else [125] * 5
        assert sorted(prefix_fibres.values()) == expected_prefix
        assert sorted(tail_fibres.values()) == expected_tail
        ready_classes[(len(prefix_fibres), len(tail_fibres))] += 1

        w = (q + r) % 5
        sums = [sum(third_receiver(z, q, r)) % 5 for z in range(5)]
        assert sums == [(w + 2) % 5, (2 - w) % 5, (3 - w) % 5,
                        (4 - w) % 5, -w % 5]
        assert len(set(sums[1:])) == 4
        assert set(sums[1:]) & {3, 4}
        domains = [support(s) for s in sums]
        reached = {0}
        while True:
            enlarged = reached | {j for i in reached for j in range(5) if domains[i] & domains[j]}
            if enlarged == reached:
                break
            reached = enlarged
        assert reached == set(range(5))
    assert ready_classes == {(5, 5): 21, (5, 4): 3, (4, 4): 1}

    # A finite check of the projected support; infinite recurrence is proved
    # through the inherited actual-clock support theorem, not this loop.
    support_points = 0
    for q, r in pairs:
        state = ((1 - q - r) % 5, 0, 0, 0, q, r)
        triple = (1, q, r)
        seen = set()
        predicted = support((q + r) % 5)
        for n in range(3, 1025):
            assert triple == (sum(state) % 5, state[4], state[5])
            assert state[4:] in predicted
            seen.add(state[4:])
            support_points += 1
            if n < 1024:
                state = native_step(n, state)
                triple = triple_step(n, triple)
        assert seen == predicted
    assert support_points == 25550
    assert [len(support(s)) for s in range(5)] == [15, 10, 15, 20, 20]

    # Absence cannot differ from a present input with identical observation.
    source_fibres = Counter(sum(source) % 5 for source in pistons)
    assert source_fibres == {k: 125 for k in range(5)}
    assert sorted(Counter(histories.values()).values()) == [125] * 5
    for source in pistons:
        assert source_fibres[sum(source) % 5] - 1 == 124

    # All twenty stipulated contexts invert every receiver bijectively.
    contexts = tuple(product((-1, 1), (1, 4), range(5)))
    assert len(contexts) == 20
    for tau in contexts:
        assert {restore_at_three(tau, *pair) for pair in pairs} == set(pairs)
        readings = Counter(read_with_context(tau, *pair) for pair in pairs)
        assert readings[("BLANK", None)] == 20
        assert all(readings[("PRESENT", k)] == 1 for k in range(5))
    assert all(context(n) in contexts for n in range(3, 1025))
    assert context(4) == context(6) == (-1, 4, 0)
    assert context(5) == (1, 1, 0)
    assert context(7) == (1, 4, 1)
    assert context(5) != context(7)
    for n in range(3):
        assert all(read_residue(n, *pair) == ("BLANK", None) for pair in pairs)
    assert read_residue(3, 1, 0) == ("PRESENT", 0)
    assert read_residue(3, 0, 0) == ("BLANK", None)
    try:
        read_residue(-1, 0, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative native counter was accepted.")

    # Exact integral identities imply the unit argument for every modulus 5^m.
    one = (1, 0, 0, 0)
    J = (1, 0, 1, 0)
    J_inverse = (0, -1, -1, 0)
    J_squared = ring_product(J, J)
    J_squared_minus_one = tuple(a - b for a, b in zip(J_squared, one))
    assert ring_product(J_squared_minus_one, (-2, 1, 2, 6)) == (11, 0, 0, 0)
    assert ring_product(J, J_inverse) == one
    assert 11 % 5 != 0
    for source in pistons:
        assert sum(ring_product(J, source)) % 5 == 2 * sum(source) % 5
    collisions = 0
    for seed in product(range(5), repeat=6):
        states = [seed]
        for n in range(6):
            states.append(native_step(n, states[-1]))
        assert sum(states[3]) % 5 == 1
        assert states[4] == states[6]
        collisions += 1
    assert collisions == 15625

    print("u_raw_residue_port: supplementary exact L1 proof audit")
    print("raw ready (0,1): 625 sources, ticks 0..256, 160625 quotient agreements, 158750 restorations")
    print("all 25 readies: first-three formulas and source fibres; 21 good tails, 4 exceptional tails")
    print("receiver supports: 25 starts, ticks 3..1024, 25550 states; overlap graphs connected for all 25 readies")
    print("absence: 5 fibres of 125 sources; excluding one leaves 124 indistinguishable present sources")
    print("reader: 20 sufficient contexts, explicit non-autonomy witness, BLANK and PRESENT(0) distinguished")
    print("cyclotomic identities exact over Z[j]; psi4=psi6 for all 15625 origin-zero seeds")
    print("PASS; bounded audits do not prove infinite recurrence, context minimality or physical implementation")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without -O: this exact audit requires assertions.")
    audit()
