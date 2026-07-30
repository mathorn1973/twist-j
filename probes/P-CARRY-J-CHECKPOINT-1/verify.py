#!/usr/bin/env python3
"""Exact audit for P-CARRY-J-CHECKPOINT-1.

The proof in PREREG.md is symbolic. This verifier independently exhausts the
finite checkpoint carrier, audits the five generator trace laws, and checks
the frozen checkpoint collision and ramified phase separation.
"""

from itertools import product


P = 5
CHECKPOINT_COUNT = P**6
checks = []


def check(name, condition):
    checks.append((name, bool(condition)))


def mod5(values):
    return tuple(value % P for value in values)


def generator_a(state):
    p1, p4, p1p, p4p, q, r = state
    return (p4, p1, p4p, p1p, q, r)


def generator_b(state):
    p1, p4, p1p, p4p, q, r = state
    return mod5((-p1p, -p4p, -p1, -p4, -q, -r))


def generator_c(state):
    p1, p4, p1p, p4p, q, r = state
    return mod5(
        (
            -p1p + 2,
            -p4p + 1 + r,
            -p1 + 2,
            -p4 + 1 - r,
            1 - q,
            -r,
        )
    )


def generator_d(state):
    center = (2, 1, 3, 4, 1, 1)
    return mod5(c - x for c, x in zip(center, state))


def generator_e(state):
    shifted_center = (2, 1, 3, 4, 2, 1)
    return mod5(c - x for c, x in zip(shifted_center, state))


GENERATORS = (
    generator_a,
    generator_b,
    generator_c,
    generator_d,
    generator_e,
)

# z(g_i psi) = alpha_i z(psi) + beta_i modulo five.
TRACE_AFFINE = ((1, 0), (-1, 0), (-1, 2), (-1, 2), (-1, 3))


def trace6(state):
    return sum(state) % P


def thue_morse(n):
    return n.bit_count() & 1


def theta(n):
    return pow(2, n.bit_count(), P)


def trace_skeleton(initial_trace):
    traces = [initial_trace]
    selectors = []
    z = initial_trace
    for n in range(6):
        selector = (z + 2 * thue_morse(n)) % P
        selectors.append(selector)
        alpha, beta = TRACE_AFFINE[selector]
        z = (alpha * z + beta) % P
        traces.append(z)
    return traces, selectors


# Gate 01: independently audit every declared generator relation used by the
# proof on the full finite checkpoint carrier.
involutions_hold = True
trace_laws_hold = True
checkpoint_count = 0
for checkpoint in product(range(P), repeat=6):
    checkpoint_count += 1
    z = trace6(checkpoint)
    for index, generator in enumerate(GENERATORS):
        image = generator(checkpoint)
        alpha, beta = TRACE_AFFINE[index]
        involutions_hold &= generator(image) == checkpoint
        trace_laws_hold &= trace6(image) == (alpha * z + beta) % P

check(
    "01 generator algebra: five involutions and five z6 laws on 15625 checkpoints",
    checkpoint_count == CHECKPOINT_COUNT
    and involutions_hold
    and trace_laws_hold,
)


# Gate 02: use only the affine trace table and the exact Thue-Morse prefix.
expected_paths = {
    0: ([0, 0, 2, 1, 4, 1, 4], [0, 2, 4, 1, 1, 1]),
    1: ([1, 4, 1, 1, 4, 1, 4], [1, 1, 3, 1, 1, 1]),
    2: ([2, 0, 2, 1, 4, 1, 4], [2, 2, 4, 1, 1, 1]),
    3: ([3, 4, 1, 1, 4, 1, 4], [3, 1, 3, 1, 1, 1]),
    4: ([4, 4, 1, 1, 4, 1, 4], [4, 1, 3, 1, 1, 1]),
}
observed_paths = {z: trace_skeleton(z) for z in range(P)}
check(
    "02 trace skeleton: all five z0 classes force z3=1 and selectors i3=i4=i5=1",
    [thue_morse(n) for n in range(6)] == [0, 1, 1, 0, 1, 0]
    and observed_paths == expected_paths,
)


# Gates 03 and 05: evolve every seed through the full six-coordinate update,
# independently of the trace-only skeleton. Build the attempted h constraints
# at n=4 and n=6 and retain every contradictory checkpoint key.
collision_count = 0
forced_selector_count = 0
assignments = {}
conflicting_keys = set()

for seed in product(range(P), repeat=6):
    states = [seed]
    selectors = []
    state = seed
    for n in range(6):
        selector = (trace6(state) + 2 * thue_morse(n)) % P
        selectors.append(selector)
        state = GENERATORS[selector](state)
        states.append(state)

    collision_count += states[4] == states[6]
    forced_selector_count += (
        trace6(states[3]) == 1 and selectors[3:6] == [1, 1, 1]
    )

    for checkpoint, phase in ((states[4], theta(4)), (states[6], theta(6))):
        previous = assignments.setdefault(checkpoint, phase)
        if previous != phase:
            conflicting_keys.add(checkpoint)

check(
    "03 universal checkpoint collision: psi4=psi6 for all 15625 seeds",
    collision_count == CHECKPOINT_COUNT
    and forced_selector_count == CHECKPOINT_COUNT,
)


# Gate 04: the inherited ramified lift separates the colliding times.
check(
    "04 ramified phase separation: Theta4=2 and Theta6=4 in F5*",
    theta(4) == 2 and theta(6) == 4 and theta(4) != theta(6),
)


check(
    "05 factorization no-go: every visited collision key receives both phases",
    len(assignments) > 0 and conflicting_keys == set(assignments),
)


passed = sum(result for _, result in checks)
for name, result in checks:
    print(("PASS " if result else "FAIL ") + name)
if passed == len(checks):
    print(f"RESULT {passed}/{len(checks)} ALL PASS")
else:
    print(f"RESULT {passed}/{len(checks)}")
raise SystemExit(0 if passed == len(checks) else 1)
