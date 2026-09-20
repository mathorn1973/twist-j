#!/usr/bin/env python3
"""Exact finite-premise audit; all-class/all-duration claims use the proofs.

Python standard library only.  Arithmetic on native points is in F5.
The admitted arithmetic circuit is not a physical implementation of U.
No gate is executed on import.
"""

from itertools import product


FIELD = range(5)
CODE_LABELS = (1, 2, 4, 3)
BLOCKS = 14


def sign(exponent):
    return 1 if exponent % 2 == 0 else -1


def trace(point):
    return sum(point) % 5


def source_sum(point):
    return sum(point[:4]) % 5


def mark(counter, point):
    return (sign(counter - 3) * source_sum(point)) % 5


def coarse(h):
    return (0, 1, 2, 2, 2)[h % 5]


def generator(index, point):
    a, b, c, d, q, r = point
    if index == 0:
        raw = (b, a, d, c, q, r)
    elif index == 1:
        raw = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        raw = (2 - c, 1 - d + r, 2 - a, 1 - b - r, 1 - q, -r)
    elif index == 3:
        raw = (2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r)
    elif index == 4:
        raw = (2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r)
    else:
        raise ValueError("generator index outside F5")
    return tuple(value % 5 for value in raw)


def quotient_generator(index, z, r):
    return (
        (z, r),
        (-z % 5, -r % 5),
        ((2 - z) % 5, -r % 5),
        ((2 - z) % 5, (1 - r) % 5),
        ((3 - z) % 5, (1 - r) % 5),
    )[index]


def step(point, bit):
    return generator((trace(point) + 2 * bit) % 5, point)


def translate(point, delta):
    return point[:4] + ((point[4] - delta) % 5, (point[5] + delta) % 5)


def follow(point, word):
    for bit in word:
        point = step(point, bit)
    return point


def theta(counter):
    return counter.bit_count() % 2


def code_point(counter, h):
    initial = (h, 0, 0, 0, (1 - h) % 5, 0)
    return follow(initial, (theta(j) for j in range(3, counter)))


def stable_points():
    for p in product(FIELD, repeat=4):
        s = sum(p)
        for z in (1, 4):
            for r in FIELD:
                yield p + ((z - s - r) % 5, r)


def polynomial(coefficients, h):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * h + coefficient) % 5
    return value


def audit_native_quotient():
    generator_cases = selector_cases = 0
    for point in product(FIELD, repeat=6):
        z, r = trace(point), point[5]
        for index in FIELD:
            result = generator(index, point)
            assert (trace(result), result[5]) == quotient_generator(index, z, r)
            assert generator(index, result) == point
            generator_cases += 1
        for bit in (0, 1):
            result = step(point, bit)
            assert (trace(result), result[5]) == quotient_generator(
                (z + 2 * bit) % 5, z, r
            )
            selector_cases += 1
    assert generator_cases == 78125 and selector_cases == 31250
    print("PASS A01 autonomous native quotient: 78125 generator / 31250 selector cases")


def audit_stable_transport():
    cases = 0
    table = {(1, 0): (1, 4), (1, 1): (3, 1),
             (4, 0): (4, 4), (4, 1): (1, 1)}
    for point in stable_points():
        z = trace(point)
        for bit in (0, 1):
            index, next_z = table[z, bit]
            after = step(point, bit)
            assert after == generator(index, point)
            assert trace(after) == next_z
            assert source_sum(after) == -source_sum(point) % 5
            for counter in (3, 4):
                assert mark(counter + 1, after) == mark(counter, point)
            for delta in FIELD:
                displaced = step(translate(point, delta), bit)
                assert displaced == translate(after, -delta)
                assert displaced[:4] == after[:4]
                assert trace(displaced) == trace(after)
                cases += 1
    assert cases == 62500
    print("PASS A02 stable label and paired-port transport: 62500 cases")


def audit_commanded_translation():
    cases = 0
    for point in product(FIELD, repeat=6):
        result = point
        for index in (1, 3, 1, 4):
            result = generator(index, result)
        assert result == translate(point, 2)
        cases += 1
    assert cases == 15625
    print("PASS A03 commanded word b,d,b,e equals T_2: 15625 points")


def audit_code_and_degree():
    code_cases = 0
    for counter in range(3, 21):
        points = [code_point(counter, h) for h in FIELD]
        direction = tuple((b - a) % 5 for a, b in zip(points[0], points[1]))
        assert len(set(points)) == 5
        assert len({(trace(p), p[5]) for p in points}) == 1
        for h, point in enumerate(points):
            assert point == tuple((a + h * d) % 5 for a, d in zip(points[0], direction))
            assert mark(counter, point) == h
            code_cases += 1
    quadratic_count = 0
    for coefficients in product(FIELD, repeat=3):
        assert any(polynomial(coefficients, h) != coarse(h) for h in CODE_LABELS)
        quadratic_count += 1
    extensions = {}
    for coefficients in product(FIELD, repeat=5):
        if all(polynomial(coefficients, h) == coarse(h) for h in CODE_LABELS):
            t = polynomial(coefficients, 0)
            assert t not in extensions
            assert coefficients == (t, 1, 1, 1, (3 - t) % 5)
            extensions[t] = coefficients
    assert code_cases == 90 and quadratic_count == 125
    assert set(extensions) == set(FIELD)
    assert all(polynomial(extensions[0], h) == coarse(h) for h in FIELD)
    print("PASS A04 affine code line: 90 points; 125 quadratics excluded; 5/3125 extensions")


def audit_two_port_target():
    cases = 0
    for counter in (3, 4):
        for z in (1, 4):
            images = set()
            for q, r in product(FIELD, repeat=2):
                s = (z - q - r) % 5
                point = (s, 0, 0, 0, q, r)
                delta = coarse(sign(counter - 3) * (z - q - r))
                result = ((q - delta) % 5, (r + delta) % 5)
                assert translate(point, coarse(mark(counter, point)))[4:] == result
                assert sum(result) % 5 == (q + r) % 5
                images.add(result)
                cases += 1
            assert len(images) == 25
    assert cases == 100
    print("PASS A05 known-sheet two-port reduction and bijection: 100 points")


def audit_two_port_family():
    permutations = set()
    points = tuple(product(FIELD, repeat=2))
    cases = 0
    for offsets in product(FIELD, repeat=5):
        images = []
        for s, r in points:
            result = (s, (r + offsets[s]) % 5)
            assert (result[0], (result[1] - offsets[result[0]]) % 5) == (s, r)
            assert (s, ((r + 1) + offsets[s]) % 5) == (result[0], (result[1] + 1) % 5)
            images.append(result)
            cases += 1
        assert len(set(images)) == 25
        permutations.add(tuple(images))
    assert len(permutations) == 3125 and cases == 78125
    # Mathematical admission alone selects neither coarse, fine nor no response.
    for offsets in ((0,) * 5, (1,) * 5, tuple(FIELD), (0, 1, 2, 2, 2)):
        assert tuple((s, (r + offsets[s]) % 5) for s, r in points) in permutations
    print("PASS A06 target-independent commuting two-port family: 3125 maps / 78125 points")


def circuit(point, counter, boundary_words, defect=None):
    """Fourteen completed blocks; native ticks only at their 15 boundaries.

    Work storage is inert under native ticks. Multiplicative port blocks
    are implemented as their two allowed register updates with no tick
    between them. Intermediate comparison is at completed blocks/ticks.
    """
    assert len(boundary_words) == BLOCKS + 1
    assert trace(point) in (1, 4)
    launch = counter
    free = point
    h = mark(launch, point)
    w = v = u = 0
    inserted = 0
    for boundary in range(BLOCKS + 1):
        for bit in boundary_words[boundary]:
            point = step(point, bit)
            free = step(free, bit)
            counter += 1
            assert point == translate(free, sign(counter - launch) * inserted)
            assert mark(counter, point) == h
        if boundary == BLOCKS:
            break
        if boundary == 0:
            w = (w + mark(counter, point)) % 5
        elif boundary == 1:
            v = (v + w) % 5
        elif boundary == 2:
            if defect != "no_multiplication":
                u = (u + w * v) % 5
        elif boundary == 3:
            v = (v - w) % 5
        elif boundary == 4:
            v = (v + u) % 5
        elif boundary in (5, 6, 7, 8):
            amount = (w, u, w * u, 3 * u * v)[boundary - 5]
            if defect == "no_multiplication" and boundary >= 7:
                amount = 0
            beta = 1 if defect == "wrong_parity" else sign(counter - launch)
            increment = beta * amount % 5
            # Separate affine or multiply-add updates, with no U in between.
            coordinates = list(point)
            coordinates[4] = (coordinates[4] - increment) % 5
            coordinates[5] = (coordinates[5] + increment) % 5
            point = tuple(coordinates)
            inserted = (inserted + sign(counter - launch) * increment) % 5
        elif boundary == 9:
            v = (v - u) % 5
        elif boundary == 10:
            v = (v + w) % 5
        elif boundary == 11:
            if defect != "no_multiplication":
                u = (u - w * v) % 5
        elif boundary == 12:
            v = (v - w) % 5
        elif boundary == 13:
            cleanup = source_sum(point) if defect == "wrong_cleanup" else mark(counter, point)
            w = (w - cleanup) % 5
        assert point[:4] == free[:4]
        assert trace(point) == trace(free)
        assert point == translate(free, sign(counter - launch) * inserted)
    return point, (w, v, u), counter


def target(point, counter, boundary_words):
    word = tuple(bit for block in boundary_words for bit in block)
    return follow(translate(point, coarse(mark(counter, point))), word)


def audit_full_clean_circuit():
    empty = ((),) * (BLOCKS + 1)
    cases = 0
    for counter in (3, 4):
        for point in stable_points():
            after, work, end = circuit(point, counter, empty)
            assert after == target(point, counter, empty)
            assert work == (0, 0, 0) and end == counter
            cases += 1
    assert cases == 12500
    print("PASS A07 full stable-sheet clean construction: 12500 inputs")


def actual_schedule(counter, lengths):
    words = []
    for length in lengths:
        words.append(tuple(theta(j) for j in range(counter, counter + length)))
        counter += length
    return tuple(words)


def schedules():
    # Actual native driver, including both launch parities and all 15 cuts.
    lengths = [(0,) * 15, (1,) * 15, (2,) * 15, tuple(j % 3 for j in range(15))]
    for boundary in range(15):
        for gap in (1, 2):
            item = [0] * 15
            item[boundary] = gap
            lengths.append(tuple(item))
    for counter in range(3, 11):
        for item in lengths:
            yield counter, actual_schedule(counter, item)
    # Every binary word of length <= 5, placed at every cut and spread out.
    for counter in (3, 4):
        for length in range(6):
            for word in product((0, 1), repeat=length):
                for boundary in range(15):
                    gaps = [()] * 15
                    gaps[boundary] = word
                    yield counter, tuple(gaps)
                gaps = [[] for _ in range(15)]
                for index, bit in enumerate(word):
                    gaps[(3 * index + 1) % 15].append(bit)
                yield counter, tuple(tuple(gap) for gap in gaps)


def audit_waiting_and_coherence():
    schedule_count = point_count = units = 0
    high_off_diagonal = 0
    for counter, gaps in schedules():
        actual = []
        desired = []
        for h in CODE_LABELS:
            point = code_point(counter, h)
            after, work, end = circuit(point, counter, gaps)
            wanted = target(point, counter, gaps)
            assert after == wanted and work == (0, 0, 0)
            assert end == counter + sum(map(len, gaps))
            actual.append((after, work))
            desired.append((wanted, (0, 0, 0)))
            point_count += 1
        assert len(set(actual)) == 4
        # Each |i><j| carries reference |i><j| unchanged. This is an exact
        # sparse audit of all matrix units, not just four probabilities.
        for i, j in product(range(4), repeat=2):
            actual_joint = ((actual[i], i), (actual[j], j))
            desired_joint = ((desired[i], i), (desired[j], j))
            assert actual_joint == desired_joint
            assert actual[i][1] == actual[j][1] == (0, 0, 0)
            units += 1
            if i != j and i > 0 and j > 0:
                high_off_diagonal += 1
        schedule_count += 1
    assert schedule_count == 2288 and point_count == 9152
    assert units == 36608 and high_off_diagonal == 13728
    print("PASS A08 interleaved waiting: 2288 schedules / 9152 code inputs")
    print("PASS A09 coherent comparison: 36608 matrix units with untouched reference")


def audit_negative_controls():
    empty = ((),) * 15
    gaps = list(empty)
    gaps[1] = (0,)
    point = code_point(3, 1)
    after, work, _ = circuit(point, 3, tuple(gaps), "wrong_cleanup")
    assert after == target(point, 3, tuple(gaps)) and work != (0, 0, 0)
    gaps = list(empty)
    gaps[5] = (0,)
    after, work, _ = circuit(point, 3, tuple(gaps), "wrong_parity")
    assert after != target(point, 3, tuple(gaps)) and work == (0, 0, 0)
    point = code_point(3, 3)
    after, work, _ = circuit(point, 3, empty, "no_multiplication")
    assert after != target(point, 3, empty) and work == (0, 0, 0)
    # Inserting U between q and r updates destroys the balanced-block claim.
    point = code_point(3, 1)
    q_half = point[:4] + ((point[4] - 1) % 5, point[5])
    middle = step(q_half, 0)
    unbalanced = middle[:5] + ((middle[5] + 1) % 5,)
    balanced = step(translate(point, 1), 0)
    assert unbalanced != balanced and unbalanced[:4] != balanced[:4]
    print("PASS A10 negative controls: cleanup, parity, nonlinearity, split-port timing")


def entrance_affine_a(point):
    return point[:4] + ((point[4] + source_sum(point) + 2) % 5, point[5])


def entrance_affine_a_inverse(point):
    return point[:4] + ((point[4] - source_sum(point) - 2) % 5, point[5])


def entrance_affine_b(point):
    a, b, c, d, q, r = point
    return tuple(value % 5 for value in (
        a + b + 3 * c + r + 3,
        3 * a + 3 * c + 3 * r,
        4 * a + 2 * r + 3,
        4 * a + 2 * c + d + r,
        q + 4 * c,
        3 * a + 3 * c + 4 * r + 3,
    ))


def entrance_affine_b_inverse(point):
    aa, bb, cc, dd, qq, rr = point
    r = (rr - bb - 3) % 5
    a = 4 * (cc - 3 - 2 * r) % 5
    c = (2 * bb - a - r) % 5
    b = (aa - 3 - a - 3 * c - r) % 5
    d = (dd - 4 * a - 2 * c - r) % 5
    q = (qq - 4 * c) % 5
    return a, b, c, d, q, r


def audit_native_routed_entrance():
    permutation_cases = 0
    for point in product(FIELD, repeat=6):
        assert entrance_affine_a_inverse(entrance_affine_a(point)) == point
        assert entrance_affine_a(entrance_affine_a_inverse(point)) == point
        assert entrance_affine_b_inverse(entrance_affine_b(point)) == point
        assert entrance_affine_b(entrance_affine_b_inverse(point)) == point
        permutation_cases += 1
    assert theta(3) == 0 and theta(4) == 1
    paths = []
    targets = []
    for h in CODE_LABELS:
        point = code_point(3, h)
        path = [point]
        path.append(entrance_affine_a(path[-1]))
        path.append(step(path[-1], theta(3)))
        path.append(entrance_affine_b(path[-1]))
        path.append(step(path[-1], theta(4)))
        wanted = translate(point, coarse(h))
        assert follow(point, (theta(3), theta(4))) == point
        assert follow(wanted, (theta(3), theta(4))) == wanted
        assert path[-1] == wanted
        paths.append(path)
        targets.append(wanted)
    # Global U need not be injective. Each actually used four-point prefix is.
    for stage in range(5):
        assert len({path[stage] for path in paths}) == 4
    units = 0
    for i, j in product(range(4), repeat=2):
        # Basis pushforwards have coefficient +1; no auxiliary/environment
        # register is discarded in this explicitly mathematical comparison.
        actual = ((paths[i][-1], i), (paths[j][-1], j), 1)
        desired = ((targets[i], i), (targets[j], j), 1)
        assert actual == desired
        units += 1
    assert permutation_cases == 15625 and units == 16
    print("PASS A11 affine routing with two actual U ticks: 15625 inverse / 16 coherent cases")


def alternating_source(point):
    a, b, c, d = point[:4]
    return (-a + b - c + d) % 5


def audit_one_tick_obstruction():
    # Trace is affine along every affinely encoded input line. Nonconstant
    # trace has alpha != 0 and one of 40 bit/alpha/beta itineraries.
    expected_survivors = {
        (0, 2, 0): (4, 1, 3),
        (0, 3, 2): (3, 1, 4),
        (1, 2, 3): (4, 1, 3),
        (1, 3, 0): (3, 1, 4),
        (1, 2, 4): (0, 2, 4),
        (1, 3, 1): (4, 2, 0),
    }
    survivors = {}
    itineraries = 0
    r_slope = (1, -1, -1, -1, -1)
    r_constant = (0, 0, 0, 1, 1)
    ell_constant = (0, 0, 3, 0, 0)
    for bit in (0, 1):
        for alpha in (1, 2, 3, 4):
            for beta in FIELD:
                z_values = [(alpha * h + beta) % 5 for h in (2, 3, 4)]
                selected = tuple((z + 2 * bit) % 5 for z in z_values)
                traces = [quotient_generator(g, z, 0)[0]
                          for g, z in zip(selected, z_values)]
                trace_second_difference = (traces[0] - 2 * traces[1] + traces[2]) % 5
                if trace_second_difference == 0:
                    survivors[bit, alpha, beta] = selected
                    if selected in ((4, 1, 3), (3, 1, 4)):
                        assert tuple(r_slope[g] for g in selected) == (-1, -1, -1)
                        constants = [r_constant[g] for g in selected]
                        assert (constants[0] - 2 * constants[1] + constants[2]) % 5 == 2
                    else:
                        assert selected in ((0, 2, 4), (4, 2, 0))
                        constants = [ell_constant[g] for g in selected]
                        assert (constants[0] - 2 * constants[1] + constants[2]) % 5 == 4
                itineraries += 1
    assert survivors == expected_survivors and itineraries == 40
    premise_cases = 0
    for p in product(FIELD, repeat=4):
        for r in FIELD:
            point = p + (0, r)
            for index in FIELD:
                after = generator(index, point)
                assert after[5] == (r_slope[index] * r + r_constant[index]) % 5
                assert alternating_source(after) == (
                    -alternating_source(point) + ell_constant[index]
                ) % 5
                premise_cases += 1
    # Constant trace selects one affine generator, so every second
    # difference vanishes. The desired four outputs do not form a line.
    wanted = [translate(code_point(3, h), coarse(h)) for h in (1, 2, 3, 4)]
    high_difference = tuple((a - 2 * b + c) % 5
                            for a, b, c in zip(wanted[1], wanted[2], wanted[3]))
    low_difference = tuple((a - 2 * b + c) % 5
                           for a, b, c in zip(wanted[0], wanted[1], wanted[2]))
    assert high_difference == (0,) * 6 and low_difference != (0,) * 6
    assert premise_cases == 15625
    print("PASS A12 one-U obstruction premises: 40 itineraries / 15625 coordinate checks")


def main():
    print("P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1")
    audit_native_quotient()
    audit_stable_transport()
    audit_commanded_translation()
    audit_code_and_degree()
    audit_two_port_target()
    audit_two_port_family()
    audit_full_clean_circuit()
    audit_waiting_and_coherence()
    audit_negative_controls()
    audit_native_routed_entrance()
    audit_one_tick_obstruction()
    print("PASS finite-premise audit: 12/12")
    print("SCOPE full classes/durations: written proofs; affine controls or arithmetic are admitted")
    print("PHYSICAL entrance primitive, timing, preparation and environment: OPEN")


if __name__ == "__main__":
    main()
