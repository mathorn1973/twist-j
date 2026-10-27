#!/usr/bin/env python3
"""Exact fixed parity range-two source-energy test; standard library only.

This file must be publicly pinned with its preregistration before execution.
There is no parameter search, floating point, external input, or randomness.

Physical amplitudes equal G times the arithmetic amplitudes, where
G=diag(1,i,i,1) on the four object coins.  Thus the arithmetic seed
chi0=sqrt(2)*G^*chi is e2-e3.  This is a fixed change of coordinates,
not a change of the original occupation encoding or prepared source.
Every arithmetic amplitude lies in Z[zeta5], zeta5=exp(2*pi*i/5).

Let L=M2 C.  M2 fixes both contact ports, so M2 C=M2+(C-I).
After the fixed coin gauge, 5L is integral.  Also 5V is integral and
tokens see identity.  Consequently U25=25 G^* U G is integral.
Forward order: L5, V5 (token factor 5), object stream, then phases.
Adjoint order: conjugate phases, inverse stream, V5^T, then L5^T.

Receiver calibration is identity on chi and commutes with the frozen
position/type projection. Its conjugation factors out every memory/reference
input.  The uncalibrated fixed-label norm evaluated here is therefore the
full calibrated source-family certificate, not a memory postselection.

The fixed witness uses h=i*p4, C=(U+U*)/2, A=(U-U*)/(2i),
p4=A*sum_{j=0}^4 binom(2j,j)*C^(2j)/4^j. The common phase i has
no effect on its projected norm. The remainder norm is ||C^10 psi||.
Both polynomials multiply the unchanged source 1+/- (U^2-U^-2).
"""

from fractions import Fraction
from math import comb, gcd


PROBE = "P-SOURCE-PARITY-RANGE2-1"
RHO, ORDER, K = 2, 4, 12
SCALE = 25
POLYNOMIAL_DENOMINATOR = 65536
THRESHOLD = Fraction(1, 1800)
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
    """U25=25U or its exact adjoint in the fixed arithmetic coordinates."""
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


def polynomial_numerators():
    """Fixed integer numerators at common denominator 65536."""
    witness = {}
    for power, value in ((1, 39690), (3, 8820), (5, 2268), (7, 405), (9, 35)):
        witness[power] = value
        witness[-power] = -value
    # Independently expand i*A*sum_j binom(2j,j)*C^(2j)/4^j.
    expansion = {}
    for j in range(ORDER+1):
        factor = Fraction(POLYNOMIAL_DENOMINATOR*comb(2*j, j), 2*16**j)
        assert factor.denominator == 1
        for k in range(2*j+1):
            base_power = 2*j-2*k
            coefficient = factor.numerator*comb(2*j, k)
            for power, signed in ((base_power+1, coefficient), (base_power-1, -coefficient)):
                expansion[power] = expansion.get(power, 0) + signed
    expansion = {power: value for power, value in expansion.items() if value}
    assert expansion == witness
    remainder = {10-2*j: 64*comb(10, j) for j in range(11)}
    assert sum(remainder.values()) == POLYNOMIAL_DENOMINATOR
    return witness, remainder


def multiply_source(polynomial, setting):
    """Multiply by 1+setting*(z^2-z^-2), with no changed source."""
    result = {}
    for power, value in polynomial.items():
        for shift, coefficient in ((0, 1), (2, setting), (-2, -setting)):
            result[power+shift] = result.get(power+shift, 0) + coefficient*value
    return {power: value for power, value in result.items() if value}


class ForbiddenProjection:
    """Common opposite-parity mandatory-site projection for both settings.

    source_support is collected from exact NONZERO source amplitudes before
    the object coin is omitted. No coefficient signs or norm results select
    the projection. Source object positions are odd; target ones must be
    even. Their object occupation subbanks therefore differ at every site
    in the union of the two pairs of positions, independent of their coins.
    """

    def __init__(self, source_support):
        self.source_support = tuple(sorted(source_support))
        assert self.source_support
        self.geometry = tuple(sorted({
            (center-abs(relative), center+abs(relative), carrier, kind)
            for center, relative, carrier, kind in self.source_support
        }))
        self.cache = {}
        for center, relative, carrier, kind in self.source_support:
            assert (center+relative) % 2 == 1
            assert 95 <= carrier <= 99 and 0 <= kind < 3

    def __call__(self, key):
        center, relative, carrier, coin, kind = key
        del coin
        if (center+relative) % 2 != 0:
            return False
        separation = abs(relative)
        if separation >= 2:
            return True
        cache_key = (center, separation, carrier, kind)
        if cache_key in self.cache:
            return self.cache[cache_key]
        target_low, target_high = center-separation, center+separation
        for source_low, source_high, source_carrier, source_kind in self.geometry:
            low = min(target_low, source_low)
            high = max(target_high, source_high)
            if high-low > RHO:
                continue
            if (carrier, kind) != (source_carrier, source_kind):
                low = min(low, carrier, source_carrier)
                high = max(high, carrier, source_carrier)
            if high-low <= RHO:
                self.cache[cache_key] = False
                return False
        self.cache[cache_key] = True
        return True


def accumulate_polynomial(target, state, weight, projection=None):
    if not weight:
        return
    for key, value in state.items():
        if projection is None or projection(key):
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


def reduce_quadratic(a, b, denominator):
    assert denominator > 0
    divisor = gcd(gcd(abs(a), abs(b)), denominator)
    return (a//divisor, b//divisor, denominator//divisor)


def quadratic_add(x, y, multiplier=1):
    a, b, d = x
    c, e, f = y
    return reduce_quadratic(a*f+multiplier*c*d, b*f+multiplier*e*d, d*f)


def quadratic_multiply(x, y):
    a, b, d = x
    c, e, f = y
    return reduce_quadratic(a*c+5*b*e, a*e+b*c, d*f)


def quadratic_sign(x):
    a, b, denominator = x
    assert denominator > 0
    return sign_quadratic(a, b)


def quadratic_text(x):
    a, b, denominator = x
    return "(" + str(a) + "+(" + str(b) + ")*sqrt(5))/" + str(denominator)


def norm_gap_comparison(witness, remainder):
    """Exact sign of sqrt(W)-sqrt(R)-1/1800, without root evaluation."""
    assert quadratic_sign(witness) >= 0 and quadratic_sign(remainder) >= 0
    t_squared = (1, 0, 1800**2)
    delta = quadratic_add(quadratic_add(witness, remainder, -1), t_squared, -1)
    four_t_squared_r = quadratic_multiply((4, 0, 1800**2), remainder)
    squared_test = quadratic_add(quadratic_multiply(delta, delta), four_t_squared_r, -1)
    delta_sign = quadratic_sign(delta)
    squared_sign = quadratic_sign(squared_test)
    if delta_sign < 0:
        comparison = "LT"
    elif delta_sign == 0:
        comparison = "EQ" if quadratic_sign(remainder) == 0 else "LT"
    else:
        comparison = {1: "GT", 0: "EQ", -1: "LT"}[squared_sign]
    disposition = "CERTIFIED_OBSTRUCTION" if comparison == "GT" else "INCONCLUSIVE"
    assert (disposition == "CERTIFIED_OBSTRUCTION") == (delta_sign > 0 and squared_sign > 0)
    return delta, squared_test, delta_sign, squared_sign, comparison, disposition


def comparison_checks():
    zero = (0, 0, 1)
    assert norm_gap_comparison((1, 0, 1800**2), zero)[4] == "EQ"
    assert norm_gap_comparison((1, 0, 900**2), zero)[4] == "GT"
    assert norm_gap_comparison(zero, zero)[4] == "LT"
    assert norm_gap_comparison((1801**2, 0, 1800**2), (1, 0, 1))[4] == "EQ"
    assert norm_gap_comparison((1802**2, 0, 1800**2), (1, 0, 1))[4] == "GT"
    assert norm_gap_comparison((1, 0, 1), (1, 0, 1))[4] == "LT"


def checked_next(current, power, direction):
    following = step(current, adjoint=(direction == -1))
    assert_iterate(following, power)
    restored = step(following, adjoint=(direction == 1))
    assert_scaled_equal(restored, current, SCALE**2)
    if direction == 1 and power == 1:
        assert seed_overlap(following) == ZERO
    if direction == 1 and power == 2:
        assert seed_overlap(following) == (600, 0, 0, 0)
    if direction == 1 and power == 4:
        overlap = seed_overlap(following)
        real_twice = add_ring(overlap, conjugate(overlap))
        assert SCALE**4 % SOURCE_Z_DEN == 0
        factor = 4 * (SCALE**4 // SOURCE_Z_DEN)
        assert real_twice == quadratic_to_ring(factor*3677, -factor*77)
    return following


def exact_source_support(initial_chains):
    """Actual union for both sources, after exact coin-wise cancellation."""
    support = set()
    assert SCALE**4 % SOURCE_Z_DEN == 0
    factor = 4 * (SCALE**4 // SOURCE_Z_DEN)
    for setting in (1, -1):
        source = {}
        for key, value in SEED.items():
            accumulate(source, key, value, SCALE**2)
        for key, value in initial_chains[1][2].items():
            accumulate(source, key, value, setting)
        for key, value in initial_chains[-1][2].items():
            accumulate(source, key, value, -setting)
        assert state_norm_twice(source) == (factor*SOURCE_Z_A, factor*SOURCE_Z_B)
        for (center, relative, carrier, coin, kind), value in source.items():
            assert value != ZERO and 0 <= coin < 4
            assert 95 <= carrier <= 99 and (center+relative) % 2 == 1
            support.add((center, relative, carrier, kind))
    return support


def main():
    if not __debug__:
        raise RuntimeError("This verifier requires enabled assertions")
    assert (RHO, ORDER, K) == (2, 4, 12)
    assert POLYNOMIAL_DENOMINATOR == 2**16
    assert THRESHOLD == Fraction(1, 1800)
    ring_checks()
    matrix_checks()
    comparison_checks()

    witness_polynomial, remainder_polynomial = polynomial_numerators()
    numerators = {
        "witness": {setting: multiply_source(witness_polynomial, setting) for setting in (1, -1)},
        "remainder": {setting: multiply_source(remainder_polynomial, setting) for setting in (1, -1)},
    }
    for row in numerators["witness"].values():
        assert all(abs(power) <= 11 and power % 2 == 1 for power in row)
    for row in numerators["remainder"].values():
        assert all(abs(power) <= 12 and power % 2 == 0 for power in row)
        assert sum(row.values()) == POLYNOMIAL_DENOMINATOR
    denominator = POLYNOMIAL_DENOMINATOR * SCALE**K
    weights = {
        name: {
            setting: {power: value*SCALE**(K-abs(power)) for power, value in row.items()}
            for setting, row in by_setting.items()
        }
        for name, by_setting in numerators.items()
    }

    # The common projection is fixed from the actual sources BEFORE any
    # witness/remainder norm is inspected. Reuse these initial iterates.
    assert_iterate(SEED, 0)
    initial_chains = {}
    counts = {}
    for direction in (1, -1):
        chain = [SEED]
        for power in (1, 2):
            chain.append(checked_next(chain[-1], power, direction))
        initial_chains[direction] = chain
        counts[direction] = [len(state) for state in chain]
    source_support = exact_source_support(initial_chains)
    projection = ForbiddenProjection(source_support)
    vectors = {name: {1: {}, -1: {}} for name in ("witness", "remainder")}

    def collect(state, signed_power):
        for name in ("witness", "remainder"):
            selected_projection = projection if name == "witness" else None
            for setting in (1, -1):
                accumulate_polynomial(
                    vectors[name][setting], state,
                    weights[name][setting].get(signed_power, 0), selected_projection,
                )

    collect(SEED, 0)
    for direction in (1, -1):
        for power in (1, 2):
            collect(initial_chains[direction][power], direction*power)
        current = initial_chains[direction][2]
        for power in range(3, K+1):
            current = checked_next(current, power, direction)
            counts[direction].append(len(current))
            collect(current, direction*power)

    norms = {name: {} for name in ("witness", "remainder")}
    for setting in (1, -1):
        assert all((key[0]+key[1]) % 2 == 0 and projection(key)
                   for key in vectors["witness"][setting])
        assert all((key[0]+key[1]) % 2 == 1 for key in vectors["remainder"][setting])
        for name in ("witness", "remainder"):
            norms[name][setting] = reduced_norm_squared(vectors[name][setting], denominator)
            assert quadratic_sign(norms[name][setting]) >= 0
    # The complete equal spectral laws imply equality of the UNPROJECTED
    # C^10 remainder norms. The projected witness norms may differ.
    assert norms["remainder"][1] == norms["remainder"][-1]
    results = {
        setting: norm_gap_comparison(norms["witness"][setting], norms["remainder"][setting])
        for setting in (1, -1)
    }

    # Emit no partial success transcript before all exact checks pass.
    print("probe=" + PROBE)
    print("arithmetic=Z[zeta5]; fixed coin gauge G=diag(1,i,i,1)")
    print("parameters=rho:2,order:4,witness_degree:9,remainder_degree:10,seed_power:12")
    print("projection=common opposite-parity mandatory-site diameter>2")
    print("source_Z=(39521+154*sqrt(5))/15625")
    print("norm_gap_threshold=1/1800")
    print("energy_action_target=E0/1200")
    print("common_denominator=" + str(denominator))
    print("source_spatial_support=" + ";".join(
        ":".join(map(str, row)) for row in sorted(source_support)))
    print("positive_support_counts=" + ",".join(map(str, counts[1])))
    print("negative_support_counts=" + ",".join(map(str, counts[-1])))
    print("integrity=PASS")
    for setting, name in ((1, "plus"), (-1, "minus")):
        delta, squared_test, delta_sign, squared_sign, comparison, disposition = results[setting]
        print(name + "_witness_norm_squared=" + quadratic_text(norms["witness"][setting]))
        print(name + "_remainder_norm_squared=" + quadratic_text(norms["remainder"][setting]))
        print(name + "_gap_test_d=" + quadratic_text(delta))
        print(name + "_gap_test_d_sign=" + str(delta_sign))
        print(name + "_gap_test_e=" + quadratic_text(squared_test))
        print(name + "_gap_test_e_sign=" + str(squared_sign))
        print(name + "_gap_comparison=" + comparison)
        print(name + "_disposition=" + disposition)
    overall = "CERTIFIED_OBSTRUCTION" if any(
        row[5] == "CERTIFIED_OBSTRUCTION" for row in results.values()
    ) else "INCONCLUSIVE"
    print("overall_disposition=" + overall)


if __name__ == "__main__":
    main()
