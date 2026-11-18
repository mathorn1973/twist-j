# SPDX-License-Identifier: Apache-2.0
"""D3 differential static work under two independently specified clocks."""

from collections import defaultdict, deque
from fractions import Fraction

from shell import DEGREE, ORIGIN, SCALE, STENCIL, add, audit_field, fields, fraction_pair, grid, squared


BOXES = (10, 11)
HORIZON = 12
SAMPLES = {
    "axis_r2": (2, 0, 0),
    "axis_r4": (4, 0, 0),
    "face_1": (1, 1, 0),
    "face_2": (2, 2, 0),
    "face_3": (3, 3, 0),
    "r18_other": (4, 1, 1),
    "r26_first": (5, 1, 0),
    "r26_second": (4, 3, 1),
    "r50_first": (5, 5, 0),
    "r50_second": (5, 4, 3),
}
EQUAL_RADIUS = (("face_3", "r18_other"), ("r26_first", "r26_second"), ("r50_first", "r50_second"))


def double(point):
    return tuple(2 * coordinate for coordinate in point)


def first_hits(sites, destinations):
    """Read the first nonzero forced response independently of static work."""
    previous, current = {}, {ORIGIN: 1}
    seen = {}
    for tick in range(2, HORIZON + 1):
        denominator = SCALE ** (tick - 2)
        for point in destinations - seen.keys():
            if current.get(point, 0):
                seen[point] = tick, Fraction(current[point], denominator)
        if len(seen) == len(destinations):
            break
        following = defaultdict(int)
        following[ORIGIN] = denominator * SCALE
        for point, value in previous.items():
            following[point] -= SCALE ** 2 * value
        for point, value in current.items():
            following[point] += (2 * SCALE - DEGREE) * value
            for v, weight in STENCIL:
                other = add(point, v)
                if other in sites:
                    following[other] += weight * value
        previous, current = current, {point: value for point, value in following.items() if value}
    if seen.keys() != destinations:
        raise ValueError("frozen causal observation horizon exhausted")
    return seen


def shortest_walks(sites, destinations):
    """Independent shortest stencil support and positive leading coefficients."""
    depths, weights = {ORIGIN: 0}, {ORIGIN: 1}
    queue = deque([ORIGIN])
    while queue:
        point = queue.popleft()
        depth = depths[point]
        if destinations <= depths.keys() and depth >= max(depths[p] for p in destinations):
            break
        for v, weight in STENCIL:
            other = add(point, v)
            if other not in sites:
                continue
            if other not in depths:
                depths[other] = depth + 1
                weights[other] = 0
                queue.append(other)
            if depths[other] == depth + 1:
                weights[other] += weight * weights[point]
    return {
        point: (depths[point] + 2, Fraction(weights[point], SCALE ** depths[point]))
        for point in destinations
    }


def sample(field, denominator, hits, point):
    outer = double(point)
    radius2 = squared(point)
    potential_in = Fraction(field[point], denominator)
    potential_out = Fraction(field[outer], denominator)
    work = potential_in - potential_out
    inner_tick, inner_amplitude = hits[point]
    outer_tick, outer_amplitude = hits[outer]
    # Source activation at the origin is registered at tick two.
    causal_time = outer_tick - 2
    tangent_square = 4 * radius2 * work**2
    return {
        "points": (point, outer),
        "radius_squared": radius2,
        "potentials": [fraction_pair(value) for value in (potential_in, potential_out)],
        "unit_work": fraction_pair(work),
        "source_minus_one_work": fraction_pair(-work),
        "source_plus_two_work": fraction_pair(2 * work),
        "source_zero_work": (0, 1),
        "first_receipt_ticks": (inner_tick, outer_tick),
        "first_receipt_amplitudes": [fraction_pair(value) for value in (inner_amplitude, outer_amplitude)],
        "causal_time_outer_after_origin_hit": causal_time,
        "causal_action": fraction_pair(causal_time * work),
        "tangent_action_sqrt_radius2_coefficient": fraction_pair(2 * work),
        "tangent_action_squared": fraction_pair(tangent_square),
        "causal_over_tangent_time_squared": fraction_pair(Fraction(causal_time**2, 4 * radius2)),
    }


def box(size):
    sites = grid(size)
    destinations = {ORIGIN} | set(SAMPLES.values()) | {double(point) for point in SAMPLES.values()}
    if not destinations <= sites:
        raise ValueError("undeclared external D3 sample")
    hits = first_hits(sites, destinations)
    walked = shortest_walks(sites, destinations)
    all_fields, denominator, orbit_count = fields(size, sites)
    field = all_fields[0]
    halo = {other for point in sites for v, _ in STENCIL if (other := add(point, v)) not in sites}
    exterior = audit_field(field, halo, sites, denominator, 0)
    samples = {
        name: sample(field, denominator, hits, point)
        for name, point in SAMPLES.items()
    }
    return {
        "half_width": size,
        "grounded_interior_sites": len(sites),
        "orbits": orbit_count,
        "exterior_net_divergence": fraction_pair(exterior),
        "shortest_walk_agrees_with_first_receipt": walked == hits,
        "samples": samples,
    }


def run():
    rows = [box(size) for size in BOXES]
    small, large = (row["samples"] for row in rows)
    finite_size = {}
    for name in SAMPLES:
        first = Fraction(*small[name]["unit_work"])
        second = Fraction(*large[name]["unit_work"])
        finite_size[name] = {
            "work_large_minus_small": fraction_pair(second - first),
            "relative_to_large_work": fraction_pair((second - first) / second) if second else None,
            "same_first_receipt_ticks": small[name]["first_receipt_ticks"] == large[name]["first_receipt_ticks"],
        }
    return {
        "passed": all(row["shortest_walk_agrees_with_first_receipt"] for row in rows),
        "tangent_speed_squared": 1,
        "equal_radius_name_pairs": EQUAL_RADIUS,
        "first_receipt_origin_tick": 2,
        "boxes": rows,
        "finite_size": finite_size,
    }
