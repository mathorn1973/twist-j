# SPDX-License-Identifier: Apache-2.0
"""Exact grounded D3 fields and graph flux across finite cuts."""

from fractions import Fraction
from itertools import product
from math import lcm


WEIGHTS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
SCALE = 324
ORIGIN = (0, 0, 0)
BOXES = (7, 9)
SAMPLES = (
    ((4, 1, 1), (3, 3, 0)),
    ((7, 1, 0), (5, 5, 0)),
)
SOURCE_RING = frozenset(
    tuple(sign * 4 if i == axis else 0 for i in range(3))
    for axis, sign in product(range(3), (-1, 1))
)


def squared(point):
    return sum(x * x for x in point)


STENCIL = tuple(
    (v, WEIGHTS[squared(v)])
    for v in product(range(-4, 5), repeat=3)
    if squared(v) in WEIGHTS
)
DEGREE = sum(weight for _, weight in STENCIL)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def orbit(point):
    return tuple(sorted(map(abs, point), reverse=True))


def in_box(point, size):
    return max(map(abs, point)) <= size


def source(point):
    monopole = int(point == ORIGIN)
    neutral = 6 * monopole - int(point in SOURCE_RING)
    return monopole, neutral


def grid(size):
    return frozenset(
        point for point in product(range(-size, size + 1), repeat=3)
        if sum(point) % 2 == 0
    )


def bareiss(matrix, rhs_count):
    """Solve a fraction-free augmented system with exact divisibility checks."""
    count = len(matrix)
    previous = 1
    # The orbit quotient is similar to a positive-definite Dirichlet matrix.
    # Its leading principal minors are nonzero in this fixed ordering.
    for i in range(count - 1):
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("zero grounded-system pivot")
        for j in range(i + 1, count):
            row = matrix[j]
            factor = row[i]
            for k in range(i + 1, count + rhs_count):
                numerator = pivot * row[k] - factor * matrix[i][k]
                row[k], remainder = divmod(numerator, previous)
                if remainder:
                    raise ValueError("non-exact Bareiss division")
            row[i] = 0
        previous = pivot

    solved = []
    for rhs in range(rhs_count):
        values = [Fraction(0)] * count
        for i in range(count - 1, -1, -1):
            residual = matrix[i][count + rhs] - sum(
                matrix[i][j] * values[j] for j in range(i + 1, count)
            )
            values[i] = Fraction(residual) / matrix[i][i]
        solved.append(values)
    return solved


def fields(size, sites):
    representatives = sorted({orbit(point) for point in sites})
    index = {point: i for i, point in enumerate(representatives)}
    count = len(representatives)
    matrix = []
    for point in representatives:
        row = [0] * count + [SCALE * load for load in source(point)]
        row[index[point]] += DEGREE
        for v, weight in STENCIL:
            other = add(point, v)
            if in_box(other, size):
                row[index[orbit(other)]] -= weight
        matrix.append(row)
    solved = bareiss(matrix, 2)
    denominator = lcm(*(value.denominator for values in solved for value in values))
    maps = []
    for values in solved:
        maps.append({
            point: values[index[orbit(point)]].numerator
            * (denominator // values[index[orbit(point)]].denominator)
            for point in sites
        })
    return maps, denominator, count


def divergence(field, point):
    here = field.get(point, 0)
    return sum(weight * (here - field.get(add(point, v), 0)) for v, weight in STENCIL)


def audit_field(field, halo, sites, denominator, component):
    for point in sites:
        if divergence(field, point) != SCALE * denominator * source(point)[component]:
            raise ValueError("sitewise D3 equation failed")
    sink = sum(divergence(field, point) for point in sorted(halo))
    expected_sink = -SCALE * denominator * sum(source(point)[component] for point in sites)
    if sink != expected_sink:
        raise ValueError("whole grounded exterior current")
    return Fraction(sink, SCALE * denominator)


def fraction_pair(value):
    return value.numerator, value.denominator


def crossing_edges(cut):
    for point in sorted(cut):
        for v, weight in STENCIL:
            other = add(point, v)
            if other not in cut:
                yield point, other, squared(v), weight


def cut_record(cut, fields_pair, denominator, radius_squared=None):
    counts = {shell: 0 for shell in WEIGHTS}
    by_shell = [{shell: 0 for shell in WEIGHTS} for _ in fields_pair]
    for point, other, shell, weight in crossing_edges(cut):
        counts[shell] += 1
        for field, shell_totals in zip(fields_pair, by_shell):
            shell_totals[shell] += weight * (field[point] - field.get(other, 0))
    fluxes = tuple(Fraction(sum(totals.values()), SCALE * denominator) for totals in by_shell)
    loads = tuple(sum(source(point)[i] for point in cut) for i in range(2))
    if fluxes != loads:
        raise ValueError("Gauss cut closure")
    monopole, neutral = fluxes
    record = {
        "sites": len(cut),
        "outgoing_edges_by_squared_length": counts,
        "weighted_edge_count": sum(counts[shell] * WEIGHTS[shell] for shell in WEIGHTS),
        "charges_monopole_neutral": loads,
        "flux_monopole_neutral": [fraction_pair(current) for current in fluxes],
        "flux_two_monopoles": fraction_pair(2 * monopole),
        "flux_negative_monopole": fraction_pair(-monopole),
        "flux_monopole_plus_neutral": fraction_pair(monopole + neutral),
        "monopole_flux_by_squared_length": {
            shell: fraction_pair(Fraction(by_shell[0][shell], SCALE * denominator))
            for shell in WEIGHTS
        },
        "mean_flux_per_counted_edge": fraction_pair(monopole / sum(counts.values())),
        # This is pi times the nominal continuum area-normalized mean.
        "pi_times_nominal_spherical_mean": (
            fraction_pair(monopole / (4 * radius_squared)) if radius_squared else None
        ),
    }
    return record


def radial_current_moment(field, point):
    """First edge-current moment contracted with x, with scale applied by caller."""
    return sum(
        weight * (field[point] - field.get(add(point, v), 0))
        * sum(x * delta for x, delta in zip(point, v))
        for v, weight in STENCIL
    )


def direction_record(field_pair, denominator, pair):
    first, second = pair
    field, neutral = field_pair
    return {
        "squared_radius": squared(first),
        "points": pair,
        "potential": [fraction_pair(Fraction(field[p], denominator)) for p in pair],
        "neutral_perturbation": [fraction_pair(Fraction(neutral[p], denominator)) for p in pair],
        "radial_current_moment_times_radius": [
            fraction_pair(Fraction(radial_current_moment(field, p), SCALE * denominator))
            for p in pair
        ],
        "unequal_potential": field[first] != field[second],
        "unequal_radial_current_moment": (
            radial_current_moment(field, first) != radial_current_moment(field, second)
        ),
    }


def box(size):
    sites = grid(size)
    potential, denominator, orbit_count = fields(size, sites)
    halo = {add(point, v) for point in sites for v, _ in STENCIL if not in_box(add(point, v), size)}
    sinks = [audit_field(field, halo, sites, denominator, i) for i, field in enumerate(potential)]
    spheres = {}
    for radius in range(1, 6):
        sphere = {point for point in sites if squared(point) <= radius ** 2}
        spheres[radius] = cut_record(sphere, potential, denominator, radius ** 2)
    cube = {point for point in sites if in_box(point, 2)}
    cuts = {
        "spheres": spheres,
        "inner_cube": cut_record(cube, potential, denominator),
        "punctured_inner_cube": cut_record(cube - {ORIGIN}, potential, denominator),
        "grounded_box": cut_record(sites, potential, denominator),
    }
    directions = [direction_record(potential, denominator, pair) for pair in SAMPLES]
    anisotropy = any(row["unequal_potential"] for row in directions)
    changed_outer_field = any(
        value != (0, 1) for row in directions for value in row["neutral_perturbation"]
    )
    return {
        "half_width": size,
        "site_count": len(sites),
        "orbit_count": orbit_count,
        "grounded_exterior_sites": len(halo),
        "exterior_divergence_monopole_neutral": [fraction_pair(val) for val in sinks],
        "cuts": cuts,
        "monopole_G_200_minus_G_400": fraction_pair(
            Fraction(potential[0][(2, 0, 0)] - potential[0][(4, 0, 0)], denominator)
        ),
        "equal_radius_directions": directions,
        "unequal_potential_at_equal_radius": anisotropy,
        "same_enclosed_source_changed_outer_field": changed_outer_field,
        "passed": anisotropy and changed_outer_field,
    }


def run():
    multiplicities = {
        shell: sum(squared(v) == shell for v, _ in STENCIL) for shell in WEIGHTS
    }
    # Half the weighted second moment in any one axis is the symbol's
    # leading coefficient. Mixed moments vanish by signed symmetry.
    leading_coefficient = tuple(
        Fraction(sum(weight * v[i] ** 2 for v, weight in STENCIL), 2 * SCALE)
        for i in range(3)
    )
    if multiplicities != {2: 12, 4: 6, 8: 12, 10: 24, 16: 6} or leading_coefficient != (1,) * 3:
        raise ValueError("canonical D3 stencil or scale")
    # Equal Euclidean length three, inequivalent under cubic symmetries.
    directions = ((3, 0, 0), (2, 2, 1))
    sixth_moments = [
        sum(weight * sum(a * b for a, b in zip(k, v)) ** 6 for v, weight in STENCIL)
        for k in directions
    ]
    sixth_symbol_difference = Fraction(sixth_moments[0] - sixth_moments[1], SCALE * 720)
    rows = [box(size) for size in BOXES]
    return {
        "passed": sixth_symbol_difference == Fraction(32, 3) and all(row["passed"] for row in rows),
        "scale": SCALE,
        "shell_multiplicities": multiplicities,
        "stencil_weighted_degree": DEGREE,
        "leading_diagonal_coefficients": [fraction_pair(c) for c in leading_coefficient],
        "sixth_symbol_directions": directions,
        "weighted_sixth_moments": sixth_moments,
        "sixth_symbol_coefficient_difference": fraction_pair(sixth_symbol_difference),
        "boxes": rows,
    }
