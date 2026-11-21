#!/usr/bin/env python3
"""Exact fixed range-two source-energy test; standard library only.

This file must be publicly pinned with its preregistration before execution.
There is no parameter search, floating point, external input, or randomness.

Physical amplitudes equal G times the arithmetic amplitudes, where
G=diag(1,i,i,1) on the four object coins.  Thus the arithmetic seed
chi0=sqrt(2)*G^*chi is e2-e3.  This is a fixed change of coordinates,
not a change of the original occupation encoding or prepared source.
Every arithmetic amplitude lies in Z[zeta5], zeta5=exp(2*pi*i/5).

Let L=M2 C.  M2 fixes both contact ports, so M2 C=M2+(C-I).
After the fixed coin gauge, 5L is integral.  Also 5V is integral and
tokens see identity.  Consequently A=25 G^* U G is integral.
Forward order: L5, V5 (token factor 5), object stream, then phases.
Adjoint order: conjugate phases, inverse stream, V5^T, then L5^T.

Receiver calibration is identity on chi and commutes with the carrier
projection.  Its conjugation factors out every normalized memory/reference
input.  The uncalibrated fixed-label norm evaluated here is therefore the
full calibrated source-family certificate, not a memory postselection.
"""

from fractions import Fraction
from math import gcd, lcm


PROBE = "P-SOURCE-RANGE2-ENERGY-1"
RHO, ELL, N, K = 2, 2, 8, 12
SCALE = 25
TAIL = Fraction(1, 15840)
THRESHOLD = Fraction(1, 1200) + TAIL
SOURCE_Z_A, SOURCE_Z_B, SOURCE_Z_DEN = 39521, 154, 15625
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)

# State key: (R, r, carrier_position, object_coin, carrier_kind).
# Object coins 0,1,2,3 mean ++,+-,-+,--.
# Carrier kind 0 is token, 1 is pulse bank 1, 2 is pulse bank 2.
SEED = {
    (97, 0, 97, 1, 0): ONE,
    (97, 0, 97, 2, 0): (-1, 0, 0, 0),
}


def add_ring(x, y):
    return tuple(x[j] + y[j] for j in range(4))


def scale_ring(x, k):
    return (k*x[0], k*x[1], k*x[2], k*x[3])


def conjugate(x):
    a, b, c, d = x
    return (a-b, -b, d-b, c-b)


def multiply(x, y):
    """Product modulo zeta^4+zeta^3+zeta^2+zeta+1."""
    t = [0] * 7
    for j in range(4):
        for k in range(4):
            t[j+k] += x[j] * y[k]
    return (t[0]-t[4]+t[5], t[1]-t[4]+t[6],
            t[2]-t[4], t[3]-t[4])


def zeta_power(x, k):
    for _ in range(k % 5):
        a, b, c, d = x
        x = (-d, a-d, b-d, c-d)
    return x


def quadratic_to_ring(a, b):
    """a+b*sqrt(5), using sqrt(5)=-1-2*zeta^2-2*zeta^3."""
    return (a-b, 0, -2*b, -2*b)


def real_ring_twice(x):
    """Return A,B such that 2*x=A+B*sqrt(5); require real x."""
    a, b, c, d = x
    assert b == 0 and c == d
    return (2*a-c, -c)


def amplitude_norm_twice(x):
    """Return A,B with 2*|x|^2=A+B*sqrt(5), exactly."""
    a, b, c, d = x
    s = a*a + b*b + c*c + d*d
    near = a*b + b*c + c*d
    far = a*c + b*d + a*d
    return (2*s-near-far, near-far)


def state_norm_twice(state):
    a = b = 0
    for x in state.values():
        u, v = amplitude_norm_twice(x)
        a += u
        b += v
    return (a, b)


def sign_integer(x):
    return (x > 0) - (x < 0)


def sign_quadratic(a, b):
    """Exact sign of a+b*sqrt(5); no numerical root approximation."""
    if b == 0:
        return sign_integer(a)
    if a == 0:
        return sign_integer(b)
    sa, sb = sign_integer(a), sign_integer(b)
    if sa == sb:
        return sa
    discriminant = a*a - 5*b*b
    # Irrationality of sqrt(5) excludes zero here for nonzero integers.
    assert discriminant != 0
    return sa * sign_integer(discriminant)


def accumulate(state, key, value, coefficient=1):
    """Integer linear accumulation; remove exact zero amplitudes."""
    if coefficient == 0 or value == ZERO:
        return
    a, b, c, d = value
    previous = state.get(key, ZERO)
    result = (previous[0]+coefficient*a, previous[1]+coefficient*b,
              previous[2]+coefficient*c, previous[3]+coefficient*d)
    if result == ZERO:
        state.pop(key, None)
    else:
        state[key] = result


# 5 G^* M2 G.  Columns are input object coins.
M5 = (
    (1, -2, -2, -4),
    (2, 1, -4, 2),
    (2, -4, 1, 2),
    (-4, -2, -2, 1),
)


def coin_matrices():
    free = [[0] * 12 for _ in range(12)]
    for kind in range(3):
        for row in range(4):
            for column in range(4):
                free[4*kind+row][4*kind+column] = M5[row][column]
    contact = [row[:] for row in free]
    # Arithmetic contact ports are B_token and A_pulse-bank-1.
    token = ((1, 1), (2, -1))
    pulse = ((4, 1), (7, -1))
    for block in (token, pulse):
        for row, sr in block:
            for column, sc in block:
                contact[row][column] -= sr * sc
    for row, sr in pulse:
        for column, sc in token:
            contact[row][column] += 2 * sr * sc
            contact[column][row] -= 2 * sr * sc
    return tuple(tuple(row) for row in free), tuple(tuple(row) for row in contact)


FREE_MATRIX, CONTACT_MATRIX = coin_matrices()


def transitions(matrix, adjoint):
    return tuple(
        tuple((row, matrix[column][row] if adjoint else matrix[row][column])
              for row in range(12)
              if (matrix[column][row] if adjoint else matrix[row][column]))
        for column in range(12)
    )


COIN = {
    (False, False): transitions(FREE_MATRIX, False),
    (True, False): transitions(CONTACT_MATRIX, False),
    (False, True): transitions(FREE_MATRIX, True),
    (True, True): transitions(CONTACT_MATRIX, True),
}

# 5V with |x> mapped to exp(-ikx): exp(ik) moves c to c-1.
# Each entry is (output kind, carrier displacement, integer coefficient).
PULSE = (
    ((0, 0, 5),),
    ((1, 0, 1), (1, -1, -4), (2, 0, 2), (2, 1, 2)),
    ((1, 0, -2), (1, -1, -2), (2, 0, 1), (2, 1, -4)),
)


def reverse_pulse_edges():
    reverse = [[], [], []]
    for source_kind, edges in enumerate(PULSE):
        for target_kind, displacement, coefficient in edges:
            reverse[target_kind].append((source_kind, -displacement, coefficient))
    return tuple(tuple(sorted(edges)) for edges in reverse)


PULSE_ADJOINT = reverse_pulse_edges()
STREAM = ((-1, 0), (0, -1), (0, 1), (1, 0))


def apply_coin(state, adjoint):
    result = {}
    for (center, relative, carrier, coin, kind), value in state.items():
        at_contact = relative == 0 and center == carrier
        for output, coefficient in COIN[(at_contact, adjoint)][4*kind+coin]:
            out_kind, out_coin = divmod(output, 4)
            key = (center, relative, carrier, out_coin, out_kind)
            accumulate(result, key, value, coefficient)
    return result


def apply_pulse(state, adjoint):
    result = {}
    edges_by_kind = PULSE_ADJOINT if adjoint else PULSE
    for (center, relative, carrier, coin, kind), value in state.items():
        for out_kind, displacement, coefficient in edges_by_kind[kind]:
            key = (center, relative, carrier+displacement, coin, out_kind)
            accumulate(result, key, value, coefficient)
    return result


def apply_stream_phase(state, adjoint):
    result = {}
    for (center, relative, carrier, coin, kind), value in state.items():
        dc, dr = STREAM[coin]
        if adjoint:
            # Gamma* acts at the input r, before inverse streaming.
            value = zeta_power(value, 2 + (relative == 0))
            center -= dc
            relative -= dr
        else:
            center += dc
            relative += dr
            # Global exp(-i beta)=zeta^-2, Gamma=zeta^-1 at output r=0.
            value = zeta_power(value, -2 - (relative == 0))
        key = (center, relative, carrier, coin, kind)
        assert key not in result
        result[key] = value
    return result


def step(state, adjoint=False):
    """A=25U or its exact adjoint in the fixed arithmetic coordinates."""
    if adjoint:
        return apply_coin(apply_pulse(apply_stream_phase(state, True), True), True)
    return apply_stream_phase(apply_pulse(apply_coin(state, False), False), False)


def assert_scaled_equal(actual, expected, factor):
    assert len(actual) == len(expected)
    for key, value in expected.items():
        assert actual.get(key) == scale_ring(value, factor)


def assert_iterate(state, power):
    assert state_norm_twice(state) == (4 * SCALE**(2*power), 0)
    for (center, relative, carrier, coin, kind), value in state.items():
        assert 0 <= coin < 4 and 0 <= kind < 3
        assert abs(center-97) + abs(relative) <= power
        assert abs(carrier-97) <= power
        assert (center-97+relative-power) % 2 == 0
        assert value != ZERO and all(type(a) is int for a in value)


def seed_overlap(state):
    first = state.get((97, 0, 97, 1, 0), ZERO)
    second = state.get((97, 0, 97, 2, 0), ZERO)
    return add_ring(first, scale_ring(second, -1))


def coefficients(setting):
    """Coefficients of i*v before projection and source normalization.

    T10 gives v=-(3i/2) sum_{n=5}^{10}(U^n-U^-n)psi/D_n.
    Multiplication by the common phase i preserves its norm.  Both signs
    of psi are expanded exactly; the source chi0 has norm sqrt(2).
    """
    result = {}
    for n in range(RHO+ELL+1, N+ELL+1):
        denominator = 1
        for j in range(-ELL, ELL+1):
            denominator *= n+j
        q = Fraction(3, 2*denominator)
        terms = ((n, 1), (-n, -1),
                 (n+2, setting), (n-2, -setting),
                 (-n+2, -setting), (-n-2, setting))
        for power, multiplier in terms:
            result[power] = result.get(power, Fraction(0)) + multiplier*q
    return {power: value for power, value in result.items() if value}


def accumulate_projected(target, state, weight):
    for key, value in state.items():
        carrier = key[2]
        if carrier <= 90 or carrier >= 104:
            accumulate(target, key, value, weight)


def ring_checks():
    assert zeta_power(ONE, 5) == ONE
    total = ZERO
    for k in range(5):
        total = add_ring(total, zeta_power(ONE, k))
    assert total == ZERO
    assert conjugate(ZETA) == zeta_power(ONE, 4)
    root_five = quadratic_to_ring(0, 1)
    assert multiply(root_five, root_five) == (5, 0, 0, 0)
    tests = (ONE, ZETA, (1, 2, -3, 4), (-5, 0, 7, -2))
    for x in tests:
        assert conjugate(conjugate(x)) == x
        assert real_ring_twice(multiply(x, conjugate(x))) == amplitude_norm_twice(x)
        for y in tests:
            assert conjugate(multiply(x, y)) == multiply(conjugate(x), conjugate(y))
    assert sign_quadratic(0, 0) == 0
    assert sign_quadratic(-2, 1) == 1
    assert sign_quadratic(2, -1) == -1
    assert sign_quadratic(3, -1) == 1
    assert sign_quadratic(-3, 1) == -1


def matrix_checks():
    for matrix in (FREE_MATRIX, CONTACT_MATRIX):
        for row in range(12):
            for column in range(12):
                value = sum(matrix[k][row]*matrix[k][column] for k in range(12))
                assert value == (25 if row == column else 0)
    for kind in range(3):
        test = {(97, 0, 97, 0, kind): ONE}
        restored = apply_pulse(apply_pulse(test, False), True)
        assert_scaled_equal(restored, test, 25)


def reduced_norm_squared(state, denominator):
    """Norm of state/(denominator*sqrt(2Z)), as (a+b*sqrt5)/d."""
    a, b = state_norm_twice(state)
    assert sign_quadratic(a, b) >= 0
    za, zb, zd = SOURCE_Z_A, SOURCE_Z_B, SOURCE_Z_DEN
    numerator_a = zd * (za*a - 5*zb*b)
    numerator_b = zd * (za*b - zb*a)
    output_denominator = 4 * denominator**2 * (za*za - 5*zb*zb)
    assert output_denominator > 0
    divisor = gcd(gcd(abs(numerator_a), abs(numerator_b)), output_denominator)
    return (numerator_a//divisor, numerator_b//divisor, output_denominator//divisor)


def main():
    if not __debug__:
        raise RuntimeError("This verifier requires enabled assertions")
    assert (RHO, ELL, N, K) == (2, 2, 8, 12)
    assert K == N + ELL + 2
    assert THRESHOLD == Fraction(71, 79200)
    assert THRESHOLD**2 == Fraction(5041, 6272640000)
    assert TAIL == Fraction(3, 4*9*10*11*12)
    ring_checks()
    matrix_checks()

    q = {1: coefficients(1), -1: coefficients(-1)}
    assert all(abs(power) <= K for row in q.values() for power in row)
    coefficient_denominator = 1
    for row in q.values():
        for value in row.values():
            coefficient_denominator = lcm(coefficient_denominator, value.denominator)
    denominator = coefficient_denominator * SCALE**K
    weights = {
        setting: {
            power: int(value*coefficient_denominator) * SCALE**(K-abs(power))
            for power, value in row.items()
        }
        for setting, row in q.items()
    }
    for setting, row in q.items():
        for power, value in row.items():
            assert Fraction(weights[setting][power], denominator) == value/SCALE**abs(power)

    projected = {1: {}, -1: {}}
    saved_two = {}
    counts = {}
    assert_iterate(SEED, 0)
    for direction in (1, -1):
        current = SEED
        support_counts = [len(SEED)]
        for setting in (1, -1):
            if direction == 1 and 0 in weights[setting]:
                accumulate_projected(projected[setting], current, weights[setting][0])
        for power in range(1, K+1):
            following = step(current, adjoint=(direction == -1))
            assert_iterate(following, power)
            # Every computed nonzero power is checked by the opposite step.
            restored = step(following, adjoint=(direction == 1))
            assert_scaled_equal(restored, current, SCALE**2)
            del restored
            current = following
            support_counts.append(len(current))
            if power == 2:
                saved_two[direction] = current
                if direction == 1:
                    assert seed_overlap(current) == (600, 0, 0, 0)
            if direction == 1 and power == 4:
                overlap = seed_overlap(current)
                real_twice = add_ring(overlap, conjugate(overlap))
                factor = 4 * (SCALE**4 // SOURCE_Z_DEN)
                assert SCALE**4 % SOURCE_Z_DEN == 0
                assert real_twice == quadratic_to_ring(factor*3677, -factor*77)
            for setting in (1, -1):
                weight = weights[setting].get(direction*power, 0)
                if weight:
                    accumulate_projected(projected[setting], current, weight)
        counts[direction] = tuple(support_counts)

    # chi0 ± (U²-U^-²)chi0 has squared norm 2Z, for BOTH settings.
    source_expected_factor = 4 * (SCALE**4 // SOURCE_Z_DEN)
    for setting in (1, -1):
        source = {}
        for key, value in SEED.items():
            accumulate(source, key, value, SCALE**2)
        for key, value in saved_two[1].items():
            accumulate(source, key, value, setting)
        for key, value in saved_two[-1].items():
            accumulate(source, key, value, -setting)
        assert state_norm_twice(source) == (
            source_expected_factor*SOURCE_Z_A,
            source_expected_factor*SOURCE_Z_B,
        )
        assert all(95 <= key[2] <= 99 for key in source)

    results = {}
    threshold_squared = THRESHOLD**2
    for setting in (1, -1):
        assert all(key[2] <= 90 or key[2] >= 104 for key in projected[setting])
        a, b, d = reduced_norm_squared(projected[setting], denominator)
        assert sign_quadratic(a, b) >= 0
        sign = sign_quadratic(
            threshold_squared.denominator*a - threshold_squared.numerator*d,
            threshold_squared.denominator*b,
        )
        comparison = {1: "GT", 0: "EQ", -1: "LT"}[sign]
        disposition = "CERTIFIED_OBSTRUCTION" if sign > 0 else "INCONCLUSIVE"
        results[setting] = (a, b, d, comparison, disposition)

    # No partial success transcript is emitted before all integrity checks pass.
    print("probe=" + PROBE)
    print("arithmetic=Z[zeta5]; fixed coin gauge G=diag(1,i,i,1)")
    print("parameters=rho:2,ell:2,N:8,seed_power:12")
    print("carrier_projection=c<=90 or c>=104")
    print("source_Z=(39521+154*sqrt(5))/15625")
    print("remainder=1/15840")
    print("norm_threshold=71/79200")
    print("squared_threshold=5041/6272640000")
    print("common_denominator=" + str(denominator))
    print("positive_support_counts=" + ",".join(map(str, counts[1])))
    print("negative_support_counts=" + ",".join(map(str, counts[-1])))
    print("integrity=PASS")
    for setting, name in ((1, "plus"), (-1, "minus")):
        a, b, d, comparison, disposition = results[setting]
        print(name + "_norm_squared=(" + str(a) + "+(" + str(b)
              + ")*sqrt(5))/" + str(d))
        print(name + "_comparison=" + comparison)
        print(name + "_disposition=" + disposition)
    overall = "CERTIFIED_OBSTRUCTION" if any(
        row[4] == "CERTIFIED_OBSTRUCTION" for row in results.values()
    ) else "INCONCLUSIVE"
    print("overall_disposition=" + overall)


if __name__ == "__main__":
    main()
