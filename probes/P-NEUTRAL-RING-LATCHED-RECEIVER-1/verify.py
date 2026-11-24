"""Exact L1 audit; first execution requires the public preregistration pin."""
from itertools import product

Z = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def sub(x, y):
    return add(x, neg(y))


def scale(n, x):
    return tuple(n * a for a in x)


def mul(x, y):
    out = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i + j] += a * b
    for degree in range(6, 3, -1):
        coefficient = out[degree]
        for offset in range(1, 5):
            out[degree - offset] -= coefficient
        out[degree] = 0
    return tuple(out[:4])


def power(x, n):
    out = ONE
    for _ in range(n):
        out = mul(out, x)
    return out


def conjugate(x):
    out = Z
    for i, coefficient in enumerate(x):
        out = add(out, scale(coefficient, power(JROOT, (-i) % 5)))
    return out


def norm(x):
    return mul(x, conjugate(x))


def q(x):
    numerator = 5 * sum(a * a for a in x) - sum(x) ** 2
    assert numerator % 2 == 0
    return numerator // 2


def admitted(x, y):
    return all(a % 2 == 0 for a in sub(x, y))


P = power(JROOT, 2)
A = sub(ONE, JROOT)


def contact(x, y):
    if not admitted(x, y):
        return x, y
    s = tuple(a // 2 for a in add(x, y))
    d = tuple(a // 2 for a in sub(x, y))
    pd = mul(P, d)
    return add(s, pd), sub(s, pd)


def repeated(pair, count):
    for _ in range(count):
        pair = contact(*pair)
    return pair


def conserved(before, after):
    assert add(*before) == add(*after)
    assert add(norm(before[0]), norm(before[1])) == add(norm(after[0]), norm(after[1]))
    assert sum(map(q, before)) == sum(map(q, after))
    assert repeated(after, 4) == before
    assert repeated(before, 5) == before



def initial_ring(length, flaw, bit):
    phases = [0] * length
    phases[2] = flaw
    if bit:
        phases[-1] = phases[0] = 1
    ring = [scale((-1) ** i, mul(A, power(P, k))) for i, k in enumerate(phases)]
    return tuple(ring + [scale(3, A), scale(-3, A)]), 0


def totals(state):
    total_sum = total_norm = Z
    total_q = 0
    for value in state:
        total_sum = add(total_sum, value)
        total_norm = add(total_norm, norm(value))
        total_q += q(value)
    return total_sum, total_norm, total_q


def normal_layer(state, parity, inverse=False):
    length = len(state) - 2
    old_parity = parity ^ 1 if inverse else parity
    edges = [(i, (i + 1) % length) for i in range(old_parity, length, 2)]
    edges.append((length, length + 1))
    if inverse:
        edges.reverse()
    updated = list(state)
    for i, j in edges:
        pair = (updated[i], updated[j])
        updated[i], updated[j] = repeated(pair, 4) if inverse else contact(*pair)
    return tuple(updated), parity ^ 1


def read_contact(state, receiver, inverse=False):
    arm = len(state) - 2
    updated = list(state)
    pair = (updated[receiver], updated[arm])
    updated[receiver], updated[arm] = repeated(pair, 4) if inverse else contact(*pair)
    return tuple(updated)


def composition_case(length, flaw, receiver, expected_time, expected_pointers):
    experiments = [initial_ring(length, flaw, bit) for bit in (0, 1)]
    conserved_totals = [totals(state) for state, _ in experiments]
    assert conserved_totals[0] == conserved_totals[1]
    assert conserved_totals[0][2] == 5 * length + 90
    horizon = 16 * length + 80
    for time in range(horizon + 1):
        probes = []
        for bit, (state, parity) in enumerate(experiments):
            assert parity == time % 2
            assert totals(state) == conserved_totals[bit]
            assert all(q(value) == 5 for value in state[:length])
            reference = scale(3, mul(A, power(P, time % 5)))
            assert state[-2:] == (reference, neg(reference))
            sampled = read_contact(state, receiver)
            assert totals(sampled) == conserved_totals[bit]
            assert q(sampled[-2]) in (25, 45)
            probes.append(sampled)
        pointers = tuple(q(state[-2]) for state in probes)
        if pointers[0] != pointers[1]:
            assert time == expected_time, (length, flaw, receiver, time, expected_time)
            assert pointers == expected_pointers, (length, flaw, pointers)
            for bit, sampled in enumerate(probes):
                # M occupies its own layer and leaves ring parity unchanged.
                original, parity = experiments[bit]
                actual = sampled
                for step in range(21):
                    assert totals(actual) == conserved_totals[bit]
                    assert q(actual[-2]) == pointers[bit]
                    if step < 20:
                        actual, parity = normal_layer(actual, parity)
                for _ in range(20):
                    actual, parity = normal_layer(actual, parity, inverse=True)
                assert actual == sampled
                actual = read_contact(actual, receiver, inverse=True)
                assert (actual, parity) == experiments[bit]
            return (length, flaw, receiver, time, time + 1, *pointers)
        if time < horizon:
            experiments = [normal_layer(state, parity) for state, parity in experiments]
    raise AssertionError(("no pointer contrast", length, flaw, receiver, horizon))


def integration_audit():
    rows = []
    for receiver in (4, 8, 12, 16, 20, 24):
        rows.append(composition_case(64, 0, receiver, receiver, (25, 45)))
    delay = {0: 2, 2: 0, 4: 1, 6: 3, 8: 0}
    for length in (20, 22, 24, 26, 28):
        for flaw in (1, 2, 3, 4):
            expected_time = 4 * length - 57 + delay[length % 10]
            pointers = (45, 25) if length % 10 == 2 else (25, 45)
            rows.append(composition_case(length, flaw, 8, expected_time, pointers))
    print("L,h,D,snapshot,read_completion,pointer_bit0,pointer_bit1")
    for row in rows:
        print(",".join(map(str, row)))
    print("Whole-ring paired experiments:", len(rows))
    print("Complete invasive-read continuations and reversals:", 2 * len(rows))


def main():
    assert power(JROOT, 5) == ONE
    assert q(A) == 5
    assert mul(norm(A), norm(sub(ONE, P))) == scale(5, ONE)
    ring_count = 0
    for sign, k, ell in product((-1, 1), range(5), range(5)):
        x = scale(sign, mul(A, power(P, k)))
        y = scale(-sign, mul(A, power(P, ell)))
        out = contact(x, y)
        assert admitted(x, y) == (k == ell)
        assert out == ((mul(P, x), mul(P, y)) if k == ell else (x, y))
        assert tuple(map(q, out)) == (5, 5)
        conserved((x, y), out)
        ring_count += 1

    detector_count = principal_count = retained_snapshots = 0
    zero_transfer_count = 0
    for sign, c, k, r in product((-1, 1), (-5, -3, -1, 1, 3, 5), range(5), range(5)):
        u = mul(A, power(P, r))
        x = scale(sign, mul(A, power(P, k)))
        y = scale(c, u)
        unused = neg(y)
        assert repeated((scale(c, A), scale(-c, A)), r) == (y, unused)
        assert contact(y, unused) == (mul(P, y), mul(P, unused))
        source, pointer = contact(x, y)
        conserved((x, y), (source, pointer))
        matched = k == r
        assert admitted(x, y) == matched
        before_total = 5 + 10 * c * c
        assert q(source) + q(pointer) + q(unused) == before_total
        if matched:
            predicted = 5 * (c * c + 1) // 2
            assert (q(source), q(pointer)) == (predicted, predicted)
            delta_norm = 5 * (c * c - 1) // 4
            assert sub(norm(source), norm(x)) == scale(delta_norm, ONE)
        else:
            assert (source, pointer) == (x, y)

        clock = (pointer, unused)
        latched = matched and c % 4 == (-sign) % 4
        assert (not admitted(*clock)) == latched
        if latched:
            assert contact(*clock) == clock
        else:
            assert contact(*clock) != clock
            assert repeated(clock, 5) == clock

        if sign == 1 and c == 3:
            principal_count += 1
            expected_pointer = 25 if matched else 45
            assert q(pointer) == expected_pointer
            for step in range(21):
                assert q(clock[0]) == expected_pointer
                if matched:
                    assert clock == (pointer, unused)
                retained_snapshots += 1
                if step < 20:
                    clock = contact(*clock)

        if sign == 1 and c == -1:
            assert (q(source), q(pointer), q(unused)) == (5, 5, 5)
            assert latched == matched
            zero_transfer_count += 1
        detector_count += 1

    # Expected adversarial control: a negative source is not the principal latch.
    source, pointer = contact(neg(A), scale(3, A))
    clock_next = contact(pointer, scale(-3, A))
    assert tuple(map(q, clock_next)) == (60, 10)
    assert clock_next[0] == (-3, 0, 2, -4)

    # Odd common amplitude scaling preserves admission, not a universal record quantum.
    for k, r in product(range(5), range(5)):
        x = mul(A, power(P, k))
        y = scale(3, mul(A, power(P, r)))
        before = contact(x, y)
        after = contact(scale(3, x), scale(3, y))
        assert after == tuple(scale(3, z) for z in before)
        assert q(after[0]) - q(scale(3, x)) == (180 if k == r else 0)

    print("Exact phase-ring cases:", ring_count)
    print("Exact signed odd-reference detector cases:", detector_count)
    print("Principal positive-source c=3 cases:", principal_count)
    print("Principal retained pointer snapshots:", retained_snapshots)
    print("Zero-transfer c=-1 controls:", zero_transfer_count)
    print("Negative-source unlatched control: Q=(60,10)")
    print("Odd-scale b=3 control: transferred Q=180 or 0")
    integration_audit()
    print("PASS: specified L1 identities and finite composition; no physical-energy or occurrence claim")


if __name__ == "__main__":
    main()
