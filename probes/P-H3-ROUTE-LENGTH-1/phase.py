# SPDX-License-Identifier: Apache-2.0
"""Exact chord phase in the embedding j = exp(2 pi i / 5)."""

from functools import cache


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def sign(n):
    return (n > 0) - (n < 0)


def radical_sign(value):
    """Sign of a + b sqrt(5), over integers."""
    a, b = value
    if not a or not b or sign(a) == sign(b):
        return sign(a or b)
    return sign(a) * sign(a * a - 5 * b * b)


def radical_product(left, right):
    a, b = left
    c, d = right
    return a * c + 5 * b * d, a * d + b * c


@cache
def coordinates(value):
    """Return 4 Re(z) and 2 Im(z)/sin(pi/5), as pairs in Q(sqrt(5))."""
    a, b, c, d = value
    return (4 * a - b - c - d, b - c - d), (b + 2 * c - 2 * d, b)


def determinant_sign(left, right):
    x0, y0 = coordinates(left)
    x1, y1 = coordinates(right)
    a, b = radical_product(x0, y1)
    c, d = radical_product(x1, y0)
    return radical_sign((a - c, b - d))


def divide_by_j(value):
    a, b, c, d = value
    return b - a, c - a, d - a, -a


@cache
def sector(value):
    """Index in 72-degree sectors, with the initial ray included."""
    if value == ZERO:
        return None
    rotated = value
    for index in range(5):
        following = divide_by_j(rotated)
        if radical_sign(coordinates(rotated)[1]) >= 0 > radical_sign(
            coordinates(following)[1]
        ):
            return index
        rotated = following
    raise ArithmeticError("nonzero endpoint has no sector")


def segment(left, right):
    """Return the signed positive-axis crossing, or None for an antipode."""
    x0, y0 = map(radical_sign, coordinates(left))
    x1, y1 = map(radical_sign, coordinates(right))
    if (y0 < 0 <= y1) or (y1 < 0 <= y0) or x0 * x1 < 0:
        direction = determinant_sign(left, right)
        if direction == 0 and (x0 * x1 < 0 or y0 * y1 < 0):
            return None
        if y0 < 0 <= y1 and direction > 0:
            return 1
        if y1 < 0 <= y0 and direction < 0:
            return -1
    return 0


def component(path, start, end, crossings):
    first, last = path[start], path[end]
    first_sector, last_sector = sector(first), sector(last)
    branch_order = sign(last_sector - first_sector)
    if branch_order == 0:
        branch_order = determinant_sign(first, last)
    # The lifted angle is 2*pi*crossings plus the branch endpoint angle
    # difference. Truncation is towards zero, including for negative turns.
    signed_turns = crossings
    if crossings * branch_order < 0:
        signed_turns -= sign(crossings)
    return {
        "start_index": start,
        "end_index": end,
        "initial_value": first,
        "final_value": last,
        "initial_sector": first_sector,
        "final_sector": last_sector,
        "ray_crossings": crossings,
        "signed_sector_displacement": last_sector - first_sector + 5 * crossings,
        "full_signed_turns": signed_turns,
    }


def summarize(path):
    """Measure contiguous nonzero components of the observed chord path.

    Index 0 is the initial cut. A singular zero is recorded at each zero
    sample. A singular interior crossing records its two nonzero endpoints.
    The signed sector displacement is the difference of lifted sector
    indices, including partial sectors; full signed turns truncate the
    actual lifted angular displacement towards zero.
    """
    path = tuple(map(tuple, path))
    if not path:
        raise ValueError("a phase path needs an initial cut")
    breaks, components = [], []
    start, crossings = None, 0
    for index, value in enumerate(path):
        if value == ZERO:
            if start is not None:
                components.append(component(path, start, index - 1, crossings))
                start, crossings = None, 0
            breaks.append({"kind": "zero", "index": index})
        elif start is None:
            start = index
        else:
            increment = segment(path[index - 1], value)
            if increment is None:
                components.append(component(path, start, index - 1, crossings))
                breaks.append({"kind": "antipodal", "from": index - 1, "to": index})
                start, crossings = index, 0
            else:
                crossings += increment
    if start is not None:
        components.append(component(path, start, len(path) - 1, crossings))

    continuous = not breaks
    result = {
        "initial_value": path[0],
        "final_value": path[-1],
        "initial_sector": sector(path[0]),
        "final_sector": sector(path[-1]),
        "continuous_complete": continuous,
        "singular_count": len(breaks),
        "singular_breaks": breaks,
        "component_count": len(components),
        "components": components,
    }
    for name in ("signed_sector_displacement", "ray_crossings", "full_signed_turns"):
        result[name] = components[0][name] if continuous else None
    return result


def self_test():
    roots = (ONE, (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (-1, -1, -1, -1))
    polygon = (*roots, ONE)
    for path, turns in ((polygon, 1), (reversed(polygon), -1)):
        result = summarize(path)
        assert result["continuous_complete"]
        assert result["ray_crossings"] == turns
        assert result["full_signed_turns"] == turns
        assert result["signed_sector_displacement"] == 5 * turns
    for path, turns in ((roots[4:] + (ONE,), 1), ((ONE, roots[4]), -1)):
        result = summarize(path)
        assert result["ray_crossings"] == turns
        assert result["full_signed_turns"] == 0
        assert result["signed_sector_displacement"] == turns
    result = summarize(roots[2:] + (ONE, roots[1]))
    assert result["ray_crossings"] == 1 and result["full_signed_turns"] == 0
    result = summarize((ONE, roots[1], ZERO, ONE, (-1, 0, 0, 0)))
    assert result["singular_count"] == 2 and result["component_count"] == 3
    assert [item["kind"] for item in result["singular_breaks"]] == ["zero", "antipodal"]
    assert result["initial_sector"] == 0 and result["final_sector"] == 2
    assert not result["continuous_complete"] and result["ray_crossings"] is None
    assert summarize((ZERO, ZERO))["component_count"] == 0
    result = summarize(roots[2 * index % 5] for index in range(6))
    assert result["full_signed_turns"] == 2
    assert result["signed_sector_displacement"] == 10


if __name__ == "__main__":
    self_test()
