#!/usr/bin/env python3
"""Exact fixed weighted-dual range-two energy test; standard library only.

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
The predeclared successors are w_m=(F A^2 F)^m v, m=0,1,2,
v=F*p4*psi, with all a=0,...,10 reported for both settings. A common
phase i is retained on every dual vector and cancels in every overlap.
The published parity result is an exposed baseline, not a blind result.
"""

from fractions import Fraction
from math import comb, gcd


PROBE = "P-SOURCE-WEIGHTED-DUAL-RANGE2-1"
RHO, ORDER, K = 2, 4, 12
SCALE = 25
POLYNOMIAL_DENOMINATOR = 65536
THRESHOLD = Fraction(1, 1800)
SOURCE_Z_A, SOURCE_Z_B, SOURCE_Z_DEN = 39521, 154, 15625
FILTER_SCALE = 2500
COSINE_SCALE = 50
FROZEN_WITNESS_NORMS = {
    1: (
        2892801121271648300654391161185602239087291,
        61980366805893347586700769428701004257779,
        48805964406250000000000000000000000000000000,
    ),
    -1: (
        2055220798004531531033453148584521099007291,
        147254769192022813872660759545701541537779,
        48805964406250000000000000000000000000000000,
    ),
}
FROZEN_REMAINDER_10 = (
    356260215946584346290966425570284380144989,
    -3125887658726909070739880426477483149431,
    1489439831733703613281250000000000000000000,
)
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


def prepare_baseline():
    if not __debug__:
        raise RuntimeError("This verifier requires enabled assertions")
    assert (RHO, ORDER, K) == (2, 4, 12)
    assert POLYNOMIAL_DENOMINATOR == 2**16
    assert THRESHOLD == Fraction(1, 1800)
    ring_checks()
    matrix_checks()
    comparison_checks()

    witness_polynomial, remainder_polynomial = polynomial_numerators()
    source_polynomials = {
        j: {j-2*k: 2**(16-j)*comb(j, k) for k in range(j+1)}
        for j in range(11)
    }
    assert source_polynomials[10] == remainder_polynomial
    numerators = {"witness": {
        setting: multiply_source(witness_polynomial, setting) for setting in (1, -1)
    }}
    for j in range(11):
        numerators[j] = {
            setting: multiply_source(source_polynomials[j], setting) for setting in (1, -1)
        }
    for row in numerators["witness"].values():
        assert all(abs(power) <= 11 and power % 2 == 1 for power in row)
    for j in range(11):
        for row in numerators[j].values():
            assert all(abs(power) <= j+2 and power % 2 == j % 2 for power in row)
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
    names = ("witness",) + tuple(range(11))
    vectors = {name: {1: {}, -1: {}} for name in names}

    def collect(state, signed_power):
        for name in names:
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

    witness_norms = {}
    source_norms = {}
    for setting in (1, -1):
        assert all((key[0]+key[1]) % 2 == 0 and projection(key)
                   for key in vectors["witness"][setting])
        witness_norms[setting] = reduced_norm_squared(vectors["witness"][setting], denominator)
        assert witness_norms[setting] == FROZEN_WITNESS_NORMS[setting]
    for j in range(11):
        pair = []
        for setting in (1, -1):
            assert all((key[0]+key[1]) % 2 == (j+1) % 2 for key in vectors[j][setting])
            value = reduced_norm_squared(vectors[j][setting], denominator)
            assert quadratic_sign(value) >= 0
            pair.append(value)
        assert pair[0] == pair[1]
        source_norms[j] = pair[0]
        if j:
            assert quadratic_sign(quadratic_add(source_norms[j-1], pair[0], -1)) >= 0
        del vectors[j]
    assert source_norms[0] == (1, 0, 1)
    assert source_norms[10] == FROZEN_REMAINDER_10
    for setting in (1, -1):
        assert norm_gap_comparison(witness_norms[setting], source_norms[10])[4] == "LT"
    return (vectors["witness"], witness_norms, source_norms,
            projection, source_support, counts, denominator)


def sharp_remainders(source_norms):
    """Positive Taylor envelope; LINEAR combinations of source norms."""
    error_coefficients = {
        n: Fraction(315*comb(2*(n-5), n-5), 256*n*4**(n-5))
        for n in range(5, 15)
    }
    squared_coefficients = {
        n: sum((error_coefficients[j]*error_coefficients[n-j]
                for j in range(5, n-4)), Fraction(0))
        for n in range(10, 20)
    }
    assert error_coefficients[5] == Fraction(63, 256)
    assert squared_coefficients[10] == Fraction(3969, 65536)
    assert squared_coefficients[11] == Fraction(6615, 131072)
    assert squared_coefficients[12] == Fraction(45045, 1048576)
    assert all(value > 0 for value in squared_coefficients.values())
    result = {}
    for a in range(11):
        total = Fraction(0)
        value = (0, 0, 1)
        for n in range(10, a+10):
            coefficient = squared_coefficients[n]
            total += coefficient
            term = quadratic_multiply(
                (coefficient.numerator, 0, coefficient.denominator), source_norms[n-a],
            )
            value = quadratic_add(value, term)
        assert 0 <= total < 1
        tail = 1-total
        value = quadratic_add(value, quadratic_multiply(
            (tail.numerator, 0, tail.denominator), source_norms[10],
        ))
        assert quadratic_sign(value) >= 0
        assert quadratic_sign(quadratic_add(source_norms[10-a], value, -1)) >= 0
        if a:
            assert quadratic_sign(quadratic_add(value, result[a-1], -1)) >= 0
        result[a] = value
    assert result[0] == source_norms[10]
    return result


def assert_general_support(state, radius):
    """Support/parity check without imposing a unitary-vector norm."""
    for (center, relative, carrier, coin, kind), value in state.items():
        assert abs(center-97)+abs(relative) <= radius
        assert abs(carrier-97) <= radius
        assert (center-97+relative-radius) % 2 == 0
        assert 0 <= coin < 4 and 0 <= kind < 3
        assert value != ZERO and all(type(x) is int for x in value)


def cosine_numerator(state):
    """50*C times the input numerator. Never reapply F here."""
    result = step(state, False)
    reverse = step(state, True)
    for key, value in reverse.items():
        accumulate(result, key, value)
    return result


def filtered_numerator(state, projection):
    """2500*F*A^2*F on an already F-supported numerator."""
    assert all(projection(key) for key in state)
    result = {}
    for key, value in state.items():
        accumulate(result, key, value, 1250)
    for adjoint in (False, True):
        first = step(state, adjoint)
        second = step(first, adjoint)
        del first
        for key, value in second.items():
            if projection(key):
                accumulate(result, key, value, -1)
        del second
    return result


def normalized_overlap(state, reference, state_denominator, reference_denominator):
    """Re<state,reference> after their respective sqrt(2Z) normalizations."""
    overlap = ZERO
    for key, right in reference.items():
        left = state.get(key)
        if left is not None:
            overlap = add_ring(overlap, multiply(conjugate(left), right))
    # The filter F*A^2*F is positive, so its powers have real overlaps.
    assert overlap == conjugate(overlap)
    four_real = real_ring_twice(add_ring(overlap, conjugate(overlap)))
    a, b = four_real
    za, zb, zd = SOURCE_Z_A, SOURCE_Z_B, SOURCE_Z_DEN
    numerator_a = zd*(za*a-5*zb*b)
    numerator_b = zd*(za*b-zb*a)
    denominator = 8*state_denominator*reference_denominator*(za*za-5*zb*zb)
    return reduce_quadratic(numerator_a, numerator_b, denominator)


def weighted_comparison(overlap, dual_norm, moment, remainder):
    """Compare X-sqrt(B*R) with (1/1800)*sqrt(N), exactly."""
    assert all(quadratic_sign(x) >= 0 for x in (overlap, dual_norm, moment, remainder))
    product = quadratic_multiply(moment, remainder)
    t_squared_n = quadratic_multiply((1, 0, 1800**2), dual_norm)
    delta = quadratic_add(quadratic_add(
        quadratic_multiply(overlap, overlap), product, -1), t_squared_n, -1)
    squared_test = quadratic_add(quadratic_multiply(delta, delta),
                                 quadratic_multiply((4, 0, 1),
                                                    quadratic_multiply(t_squared_n, product)), -1)
    delta_sign, squared_sign = quadratic_sign(delta), quadratic_sign(squared_test)
    guards = quadratic_sign(overlap) > 0 and quadratic_sign(dual_norm) > 0
    if not guards:
        comparison = "ZERO_DUAL"
    elif delta_sign < 0:
        comparison = "LT"
    elif delta_sign == 0:
        comparison = "EQ" if quadratic_sign(product) == 0 else "LT"
    else:
        comparison = {1: "GT", 0: "EQ", -1: "LT"}[squared_sign]
    disposition = "CERTIFIED_OBSTRUCTION" if comparison == "GT" else "INCONCLUSIVE"
    assert (disposition == "CERTIFIED_OBSTRUCTION") == (guards and delta_sign > 0 and squared_sign > 0)
    return delta_sign, squared_sign, comparison, disposition


def main():
    assert FILTER_SCALE == 2500 and COSINE_SCALE == 50
    (initial_witnesses, witness_norms, source_norms, projection,
     source_support, counts, denominator) = prepare_baseline()
    remainder_bounds = sharp_remainders(source_norms)
    family_values = {}
    cases = {}
    for setting in (1, -1):
        reference = initial_witnesses[setting]
        current_dual = reference
        dual_denominator = denominator
        previous_overlap = previous_norm = None
        for m in range(3):
            assert_general_support(current_dual, 11+2*m)
            assert all(projection(key) for key in current_dual)
            norm = reduced_norm_squared(current_dual, dual_denominator)
            overlap = normalized_overlap(current_dual, reference, dual_denominator, denominator)
            assert quadratic_sign(norm) >= 0
            assert quadratic_sign(quadratic_add(overlap, norm, -1)) >= 0
            assert quadratic_sign(quadratic_add(witness_norms[setting], overlap, -1)) >= 0
            assert quadratic_sign(quadratic_add(
                quadratic_multiply(norm, witness_norms[setting]),
                quadratic_multiply(overlap, overlap), -1,
            )) >= 0
            if m == 0:
                assert norm == overlap == witness_norms[setting]
            else:
                assert quadratic_sign(quadratic_add(previous_overlap, overlap, -1)) >= 0
                assert quadratic_sign(quadratic_add(previous_norm, norm, -1)) >= 0
            if m == 2:
                assert overlap == family_values[(setting, 1)][1]
            family_values[(setting, m)] = (overlap, norm)

            cosine_current = current_dual
            cosine_denominator = dual_denominator
            previous_moment = None
            for a in range(11):
                assert_general_support(cosine_current, 11+2*m+a)
                moment = norm if a == 0 else reduced_norm_squared(cosine_current, cosine_denominator)
                assert quadratic_sign(moment) >= 0
                if a:
                    assert quadratic_sign(quadratic_add(previous_moment, moment, -1)) >= 0
                else:
                    assert moment == norm
                result = weighted_comparison(overlap, norm, moment, remainder_bounds[a])
                if m == 0 and a == 0:
                    assert result[2] == "LT"
                cases[(setting, m, a)] = (moment,) + result
                previous_moment = moment
                if a < 10:
                    cosine_current = cosine_numerator(cosine_current)
                    cosine_denominator *= COSINE_SCALE
            del cosine_current
            previous_overlap, previous_norm = overlap, norm
            if m < 2:
                current_dual = filtered_numerator(current_dual, projection)
                dual_denominator *= FILTER_SCALE

    assert len(cases) == 66
    # No partial scientific transcript before every case and invariant passes.
    print("probe=" + PROBE)
    print("arithmetic=Z[zeta5]; fixed coin gauge G=diag(1,i,i,1)")
    print("parameters=rho:2,order:4,m:0..2,a:0..10,settings:plus/minus,cases:66")
    print("radii=source:12,dual:25")
    print("projection=common opposite-parity mandatory-site diameter>2")
    print("source_Z=(39521+154*sqrt(5))/15625")
    print("dual_gap_threshold=1/1800")
    print("energy_action_target=E0/1200")
    print("common_denominator=" + str(denominator))
    print("exposed_baseline=parity2 witness norms and R10 reproduced; m0_a0 LT both")
    print("source_spatial_support=" + ";".join(
        ":".join(map(str, row)) for row in sorted(source_support)))
    print("positive_support_counts=" + ",".join(map(str, counts[1])))
    print("negative_support_counts=" + ",".join(map(str, counts[-1])))
    print("integrity=PASS")
    for j in range(11):
        print("source_R" + str(j).zfill(2) + "=" + quadratic_text(source_norms[j]))
    for a in range(11):
        print("sharp_R_a" + str(a).zfill(2) + "=" + quadratic_text(remainder_bounds[a]))
    sign_dispositions = []
    for setting, name in ((1, "plus"), (-1, "minus")):
        for m in range(3):
            prefix = name + "_m" + str(m)
            overlap, norm = family_values[(setting, m)]
            print(prefix + "_X=" + quadratic_text(overlap))
            print(prefix + "_N=" + quadratic_text(norm))
            for a in range(11):
                key = prefix + "_a" + str(a).zfill(2)
                moment, delta_sign, squared_sign, comparison, disposition = cases[(setting, m, a)]
                print(key + "_B=" + quadratic_text(moment))
                print(key + "_d_sign=" + str(delta_sign))
                print(key + "_e_sign=" + str(squared_sign))
                print(key + "_comparison=" + comparison)
                print(key + "_disposition=" + disposition)
        sign_result = "CERTIFIED_OBSTRUCTION" if any(
            cases[(setting, m, a)][4] == "CERTIFIED_OBSTRUCTION"
            for m in range(3) for a in range(11)
        ) else "INCONCLUSIVE"
        sign_dispositions.append(sign_result)
        print(name + "_disposition=" + sign_result)
    overall = "CERTIFIED_OBSTRUCTION" if "CERTIFIED_OBSTRUCTION" in sign_dispositions else "INCONCLUSIVE"
    print("overall_disposition=" + overall)


if __name__ == "__main__":
    main()
