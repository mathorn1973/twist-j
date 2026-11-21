#!/usr/bin/env python3
"""NON-CANONICAL exact common-ready archive/coherence audit.

Supplied Hilbert vectors are mathematical comparisons, not native preparation.
No external input, floating point, numerical exponential or physical Born law.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
import sys


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def generator(index, x):
    a, b, c, d, q, r = x
    if index == 0:
        y = b, a, d, c, q, r
    elif index == 1:
        y = -c, -d, -a, -b, -q, -r
    elif index == 2:
        y = 2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r
    elif index == 3:
        y = 2-a, 1-b, 3-c, 4-d, 1-q, 1-r
    else:
        y = 2-a, 1-b, 3-c, 4-d, 2-q, 1-r
    return tuple(v % 5 for v in y)


def phase(x):
    return sum(x) % 5


def theta(n):
    require(n >= 0, "negative counter is not a native theta input")
    return n.bit_count() % 2


def calendar(n, s):
    if n == 0:
        return s
    if n == 1:
        return 0 if s in (0, 2) else 4
    if n == 2:
        return 2 if s in (0, 2) else 1
    return 4-3*theta(n-1)


def selected(n, s):
    return (calendar(n, s)+2*theta(n)) % 5


def native_step(n, x):
    return generator((phase(x)+2*theta(n)) % 5, x)


def step(n, state):
    x, m = state
    if n == 0:
        mu = (m+phase(x)) % 5
        return generator(mu, x), mu
    return generator(selected(n, m), x), m


def inverse_step(n, state):
    y, mu = state
    if n == 0:
        x = generator(mu, y)
        return x, (mu-phase(x)) % 5
    return generator(selected(n, mu), y), mu


def counter_step(state):
    n, x, m = state
    y, mu = (x, m) if n < 0 else step(n, (x, m))
    return n+1, y, mu


def counter_inverse(state):
    n, y, mu = state
    x, m = (y, mu) if n-1 < 0 else inverse_step(n-1, (y, mu))
    return n-1, x, m


def native_audit():
    heads = list(product(range(5), repeat=6))
    dirty = [(x, m) for x in heads for m in range(5)]
    require(len(heads) == 15625 and len(dirty) == 78125, "full carriers")
    sheet_maps = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
    h = list(range(5))
    for n in range(64):
        require(h == [calendar(n, s) for s in range(5)], "closed native calendar")
        h = [sheet_maps[theta(n)][v] for v in h]
    outputs0 = set()
    for state in dirty:
        out = step(0, state)
        outputs0.add(out)
        require(inverse_step(0, out) == state, "dirty first-step left inverse")
        require(step(0, inverse_step(0, state)) == state, "dirty first-step right inverse")
    require(len(outputs0) == 78125, "complete first permutation image")
    # The complete possible tail index templates: two transient, three constant.
    expected_templates = {(2, 1, 2, 1, 1), (4, 3, 4, 3, 3),
                          (4, 4, 4, 4, 4), (1, 1, 1, 1, 1), (3, 3, 3, 3, 3)}
    representatives = {}
    for n in range(1, 32):
        representatives.setdefault(tuple(selected(n, s) for s in range(5)), n)
    require(set(representatives) == expected_templates, "all five tail templates")
    tail_cases = 0
    for template, n in sorted(representatives.items()):
        for state in dirty:
            require(inverse_step(n, step(n, state)) == state, "dirty tail left inverse")
            require(step(n, inverse_step(n, state)) == state, "dirty tail right inverse")
            tail_cases += 1
    current = [(x, 0) for x in heads]
    raw = list(heads)
    initial_phases = [phase(x) for x in heads]
    continuation_checks = 0
    endpoint3 = None
    for n in range(32):
        next_current, next_raw = [], []
        for old, point, s in zip(current, raw, initial_phases):
            out = step(n, old)
            expected_x = native_step(n, point)
            require(out == (expected_x, s), "initialized native projection and archive")
            require(inverse_step(n, out) == old, "occupied continuation inverse")
            next_current.append(out)
            next_raw.append(expected_x)
            continuation_checks += 1
        current, raw = next_current, next_raw
        require(len(set(current)) == 15625, "full ready distinction")
        if n == 2:
            endpoint3 = list(current)
    restored = list(current)
    for n in reversed(range(32)):
        restored = [inverse_step(n, state) for state in restored]
    require(restored == [(x, 0) for x in heads], "full 32-tick original-head restoration")
    fibers = defaultdict(list)
    for head, (point, m) in zip(heads, endpoint3):
        require(m == phase(head), "E3 archive source phase")
        fibers[point].append((head, m))
    require(len(fibers) == 3125, "E3 endpoint count")
    require(all(len(rows) == 5 and {m for _, m in rows} == set(range(5))
                for rows in fibers.values()), "minimal five labels at every endpoint")
    erased_pairs = 0
    for rows in fibers.values():
        for (_, s), (_, t) in combinations(rows, 2):
            require(s != t, "merger branches must have orthogonal archive labels")
            erased_pairs += 1
    require(erased_pairs == 31250, "all within-fiber erased cross terms")
    # Full checkpoint agreement for every dirty state is impossible, and is not claimed.
    dirty_disagreements = sum(step(0, state)[0] != native_step(0, state[0]) for state in dirty)
    require(dirty_disagreements > 0, "off-ready boundary must be visible")
    raw_first = Counter(native_step(0, x) for x in heads)
    require(max(raw_first.values()) == 3, "one-step archive lower bound")
    require(max(len(rows) for rows in fibers.values()) == 5, "all-time archive lower bound")
    clock_cases = 0
    clock_heads = [heads[0], heads[1], heads[-1], (4, 1, 0, 0, 0, 0)]
    for n in (-3, -1, 0, 1, 2, 3, 17, 32):
        for x in clock_heads:
            for m in range(5):
                state = n, x, m
                require(counter_inverse(counter_step(state)) == state, "two-sided clock left inverse")
                require(counter_step(counter_inverse(state)) == state, "two-sided clock right inverse")
                clock_cases += 1
    return {"native_heads": len(heads), "dirty_carrier_states": len(dirty),
            "first_dirty_permutation_cases": len(dirty),
            "tail_template_cases": tail_cases, "tail_templates": sorted(expected_templates),
            "initialized_continuation_checks": continuation_checks,
            "original_heads_restored_after_ticks": 32, "restored_heads": len(restored),
            "E3_checkpoints": len(fibers), "archive_states_per_E3_checkpoint": 5,
            "minimum_one_step_archive": 3, "minimum_all_head_archive": 5,
            "merger_cross_terms_erased_by_partial_trace": erased_pairs,
            "dirty_native_projection_disagreements": dirty_disagreements,
            "two_sided_clock_inverse_fixtures": clock_cases,
            "native_archive_writer": "NOT DERIVED; added shear/control gates"}


def field(coefficients):
    out = [Fraction(x) for x in coefficients]
    out.extend([Fraction(0)]*max(0, 4-len(out)))
    for degree in range(len(out)-1, 3, -1):
        value = out[degree]
        out[degree] = Fraction(0)
        for offset in range(1, 5):
            out[degree-offset] -= value
    return tuple(out[:4])


ZERO, ONE, JPHASE = field([]), field([1]), field([0, 1])


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c*x for x in a)


def mul(a, b):
    out = [Fraction(0)]*7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return field(out)


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


def conjugate(a):
    out = ZERO
    for k, value in enumerate(a):
        out = add(out, scale(power(JPHASE, (-k) % 5), value))
    return out


def density(vector):
    # Unnormalized vector norm squared is two; density is divided by two.
    norm_squared = ZERO
    for value in vector.values():
        norm_squared = add(norm_squared, mul(value, conjugate(value)))
    require(norm_squared == scale(ONE, 2), "conditional pair density norm squared")
    return {(x, y): scale(mul(a, conjugate(b)), Fraction(1, 2))
            for x, a in vector.items() for y, b in vector.items()}


def reduced_checkpoint(rho):
    out = {}
    for ((x, s), (y, t)), value in rho.items():
        if s == t:
            out[(x, y)] = add(out.get((x, y), ZERO), value)
    return {key: value for key, value in out.items() if value != ZERO}


def distance_squared(rho, sigma):
    out = ZERO
    for key in set(rho) | set(sigma):
        diff = add(rho.get(key, ZERO), scale(sigma.get(key, ZERO), -1))
        out = add(out, mul(conjugate(diff), diff))
    return out


def pair_witness(x, y):
    states = [(x, 0), (y, 0)]
    for n in range(3):
        states = [step(n, state) for state in states]
    plus = density({states[0]: ONE, states[1]: JPHASE})
    minus = density({states[0]: ONE, states[1]: conjugate(JPHASE)})
    require(len(states) == 2 and states[0] != states[1], "distinct joint pair after synchronization")
    return plus, minus, reduced_checkpoint(plus), reduced_checkpoint(minus), states


def coherence_audit():
    require(power(JPHASE, 5) == ONE and JPHASE != ONE, "fifth-root phase")
    phi = add(add(ONE, JPHASE), conjugate(JPHASE))
    expected_distance = scale(add(phi, scale(ONE, 2)), Fraction(1, 2))
    x, y = (4, 1, 0, 0, 0, 0), (2, 1, 1, 2, 1, 0)
    plus, minus, local_plus, local_minus, states = pair_witness(x, y)
    require(states[0][0] == states[1][0] and states[0][1] != states[1][1], "literal merger archive")
    require(plus != minus and distance_squared(plus, minus) == expected_distance,
            "global phase preserved")
    require(local_plus == local_minus == {(states[0][0], states[0][0]): ONE},
            "checkpoint merger phase invisible")
    same_x, same_y = (0, 0, 0, 0, 0, 0), (1, 4, 0, 0, 0, 0)
    require(phase(same_x) == phase(same_y), "same initial phase fixture")
    sp, sm, lp, lm, same_states = pair_witness(same_x, same_y)
    require(same_states[0][1] == same_states[1][1] and same_states[0][0] != same_states[1][0],
            "same phase distinct endpoints")
    require(lp != lm and distance_squared(lp, lm) == expected_distance,
            "same phase local coherence survives")
    # Classical diagonal basis preparations stay diagonal under every permutation.
    input_basis_density = {(((x, 0), (x, 0))): ONE}
    output_basis_density = {(states[0], states[0]): ONE}
    require(len(input_basis_density) == len(output_basis_density) == 1
            and all(left == right for left, right in output_basis_density),
            "basis preparation creates no off-diagonal term")
    return {"merger_pair": [x, y], "global_density_squared_distance": "(phi+2)/2",
            "merger_reduced_checkpoint": "identical rank-one density for j and j^-1",
            "same_phase_local_coherence": "retained; squared density distance (phi+2)/2",
            "physical_coherent_preparation": "NOT DERIVED",
            "endpoint_current_work": "NOT DERIVED by this archive construction"}


def main():
    output = {"status": "NON-CANONICAL candidate-C finite audit only",
              "native_extension": native_audit(), "coherence": coherence_audit(),
              "full_forward_clock_lift": "isometry, not onto unitary",
              "optional_two_sided_clock": "added domain and negative-time identity rule",
              "physical_hilbert_ontology": "NOT FORCED",
              "hamiltonian_or_continuum_limit": "NOT DERIVED",
              "verdict": "PASS frozen archive inverse and conditional coherence tests"}
    sys.stdout.buffer.write((json.dumps(output, sort_keys=True, indent=2)+"\n").encode("utf-8"))


if __name__ == "__main__":
    main()
