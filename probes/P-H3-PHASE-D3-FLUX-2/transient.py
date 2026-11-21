# SPDX-License-Identifier: Apache-2.0
"""Exact D3 scalar source turn-on and character-phase tests."""

from fractions import Fraction
from itertools import product

from shell import DEGREE, ORIGIN, SCALE, STENCIL, squared


TIMES = (0, 1, 2, 4, 6)
RADII = (1, 2, 3, 4)


def words(value):
    return [value.numerator, value.denominator]


def evolve():
    # X_t = SCALE**(t-1) * u_t at t>=1. X_0 is zero.
    fields = [{}, {ORIGIN: 1}]
    for t in range(1, max(TIMES) + 1):
        previous, current = fields[t - 1 : t + 1]
        nxt = {key: -SCALE**2 * value for key, value in previous.items()}
        for (x, y, z), value in current.items():
            center = (x, y, z)
            nxt[center] = nxt.get(center, 0) + (2 * SCALE - DEGREE) * value
            for (dx, dy, dz), w in STENCIL:
                key = (x + dx, y + dy, z + dz)
                nxt[key] = nxt.get(key, 0) + w * value
        nxt[ORIGIN] = nxt.get(ORIGIN, 0) + SCALE**t
        fields.append({key: value for key, value in nxt.items() if value != 0})
    return fields


def ball(radius):
    return {
        p for p in product(range(-radius, radius + 1), repeat=3)
        if sum(p) % 2 == 0 and squared(p) <= radius**2
    }


def boundary_numerator(field, inside):
    result = 0
    for x, y, z in inside:
        u = field.get((x, y, z), 0)
        for (dx, dy, dz), w in STENCIL:
            outside = (x + dx, y + dy, z + dz)
            if outside not in inside:
                result += w * (u - field.get(outside, 0))
    return result


def enclosed_acceleration(fields, t, inside):
    # Independent time difference from three actual field cuts.
    if t == 0:
        return sum(fields[1].get(p, 0) for p in inside)
    return sum(
        fields[t + 1].get(p, 0) - 2 * SCALE * fields[t].get(p, 0)
        + SCALE**2 * fields[t - 1].get(p, 0)
        for p in inside
    )


def turn_on():
    fields = evolve()
    balls = {r: ball(r) for r in RADII}
    rows = []
    first_expected = {1: Fraction(8, 9), 2: Fraction(35, 54), 3: Fraction(5, 54), 4: Fraction(0)}
    for t in TIMES:
        for r, inside in balls.items():
            denom = SCALE**t
            flux = Fraction(boundary_numerator(fields[t], inside), denom)
            acceleration = Fraction(enclosed_acceleration(fields, t, inside), denom)
            rows.append({
                "t": t, "r": r, "flux": words(flux), "enclosed_acceleration": words(acceleration),
                "sum_is_unit_source": flux + acceleration == 1,
                "first_cut_check": flux == first_expected[r] if t == 1 else None,
                "equals_static_unit_flux": flux == 1,
            })
    return rows


def character_symbol(cosines):
    s = Fraction(sum(w * (1 - cosines[v[0] % len(cosines)]) for v, w in STENCIL), SCALE)
    trace = 2 - s
    discriminant = trace**2 - 4
    return s, trace, discriminant


def squarefree_kernel(n):
    result = 1
    factor = 2
    while factor * factor <= n:
        odd = False
        while n % factor == 0:
            odd = not odd
            n //= factor
        if odd:
            result *= factor
        factor += 1
    return result * n


def pure_modes():
    modes = []
    characters = (
        ("pi/2", (1, 0, -1, 0), Fraction(77, 81)),
        ("pi", (1, -1), Fraction(32, 81)),
    )
    for k, cosines, expected_s in characters:
        s, trace, discriminant = character_symbol(cosines)
        root_unit_obstruction = trace.denominator != 1
        # Multiplying a rational discriminant by its squared trace denominator
        # keeps the same quadratic field and yields an integer.
        int_discriminant = trace.numerator**2 - 4 * trace.denominator**2
        assert int_discriminant == discriminant * trace.denominator**2
        root_field = -squarefree_kernel(-int_discriminant) if int_discriminant < 0 else None
        modes.append({
            "k_x": k, "symbol_s": words(s), "lambda_plus_inverse_and_transfer_trace": words(trace),
            "expected_symbol_matches": s == expected_s,
            "discriminant": words(discriminant), "unit_eigenvalues_with_distinct_roots": 0 < s < 4,
            "root_of_unity_obstruction": root_unit_obstruction,
            "imaginary_quadratic_field_radicand": root_field,
        })
    fields = {mode["imaginary_quadratic_field_radicand"] for mode in modes}
    distinct_fields = len(fields) == 2 and None not in fields
    return {
        "modes": modes, "distinct_imaginary_quadratic_fields": distinct_fields,
        "common_phase_integer_step_obstructed": distinct_fields and all(
            mode["unit_eigenvalues_with_distinct_roots"] and mode["root_of_unity_obstruction"]
            for mode in modes
        ),
    }


def run():
    return {"turn_on": turn_on(), "pure_modes": pure_modes()}
