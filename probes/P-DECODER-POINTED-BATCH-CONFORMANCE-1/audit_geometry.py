"""Prospective exact geometry audit; no checks run at import.

The tesseract reference uses interval cells and their alternating boundary.
The torus reference uses oriented periodic cells in every degree. Neither
reference calls the implementation's boundary helpers. The wave reference
evaluates the Canon operator pointwise, independently of its scatter code.

Source scope: Public Canon v76, content
07910adb8418742bf52a0d204577b84b38009b18, MAXWELL-BIANCHI,
MAXWELL-AMPERE-CHAIN, MAXWELL-OBSTRUCTION-P, FCC-WEIGHTED-SHELL-SYMBOL,
PHOTON-SPATIAL-TEMPORAL-TRANSFER and PHOTON-TEMPORAL-CHARACTERISTIC.
Source injections are the candidate's disclosed CHOICES, not physical laws.
"""

from dataclasses import FrozenInstanceError
from fractions import Fraction
from itertools import permutations, product

import geometry


GATE_IDS = ("G04_TESSERACT", "G05_TORUS", "G06_WAVE")
GATE_DESCRIPTIONS = (
    ("G04_TESSERACT", "32 edge bases, independent coboundary and source injection"),
    ("G05_TORUS", "96 face bases, independent boundary, conservation and windings"),
    ("G06_WAVE", "exact shells, moments, two-slice seeds and pointwise recurrence"),
)
TEST_SOURCES = (
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (1, -2, 2, -1),
)
SOURCE_AXIS_PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2))


def _raises(expected, function, *args):
    try:
        function(*args)
    except expected:
        return
    raise AssertionError("required exception was not raised")


def _check_integer_tuple(values, size):
    assert type(values) is tuple and len(values) == size
    assert all(type(value) is int for value in values)


def _check_named_cells(cells, dimension):
    assert type(cells) is tuple
    for cell in cells:
        assert type(cell) is tuple and len(cell) == dimension + 1
        _check_integer_tuple(cell[0], 4)
        assert all(type(axis) is int for axis in cell[1:])


def _check_frozen(record):
    assert record.__dataclass_params__.frozen
    first_field = next(iter(record.__dataclass_fields__))
    _raises(FrozenInstanceError, setattr, record, first_field, None)


def _interval_cells(dimension):
    """-1 denotes the full oriented interval; 0 and 1 denote endpoints."""
    return tuple(
        cell for cell in product((-1, 0, 1), repeat=4)
        if cell.count(-1) == dimension
    )


def _interval_name(cell):
    base = tuple(0 if coordinate == -1 else coordinate for coordinate in cell)
    axes = tuple(axis for axis in range(4) if cell[axis] == -1)
    return (base, *axes)


def _interval_boundary(cell):
    result = []
    orientation = 1
    for axis in range(4):
        if cell[axis] != -1:
            continue
        for endpoint, endpoint_sign in ((1, 1), (0, -1)):
            facet = list(cell)
            facet[axis] = endpoint
            result.append((tuple(facet), orientation * endpoint_sign))
        orientation = -orientation
    return tuple(result)


def _interval_coboundary(cochain, target_dimension):
    return {
        cell: sum(sign * cochain[facet] for facet, sign in _interval_boundary(cell))
        for cell in _interval_cells(target_dimension)
    }


def _check_tesseract():
    edge_cells = _interval_cells(1)
    face_cells = _interval_cells(2)
    cube_cells = _interval_cells(3)
    edge_names = tuple(sorted(_interval_name(cell) for cell in edge_cells))
    face_names = tuple(sorted(_interval_name(cell) for cell in face_cells))
    cube_names = tuple(sorted(_interval_name(cell) for cell in cube_cells))
    assert geometry.tesseract_vertices() == tuple(product((0, 1), repeat=4))
    assert geometry.tesseract_edges() == edge_names and len(edge_names) == 32
    assert geometry.tesseract_faces() == face_names and len(face_names) == 24
    assert geometry.tesseract_cubes() == cube_names and len(cube_names) == 8
    for vertex in geometry.tesseract_vertices():
        _check_integer_tuple(vertex, 4)
    _check_named_cells(geometry.tesseract_edges(), 1)
    _check_named_cells(geometry.tesseract_faces(), 2)
    _check_named_cells(geometry.tesseract_cubes(), 3)
    edge_index = {name: i for i, name in enumerate(edge_names)}
    face_index = {name: i for i, name in enumerate(face_names)}

    for source_index in range(32):
        basis = tuple(int(i == source_index) for i in range(32))
        reference_A = {
            cell: basis[edge_index[_interval_name(cell)]] for cell in edge_cells
        }
        reference_F = _interval_coboundary(reference_A, 2)
        expected_F = {
            _interval_name(cell): value for cell, value in reference_F.items()
        }
        actual_F = geometry.tesseract_coboundary_1(basis)
        _check_integer_tuple(actual_F, 24)
        assert actual_F == tuple(expected_F[name] for name in face_names)
        assert all(value == 0 for value in _interval_coboundary(reference_F, 3).values())
        actual_dF = geometry.tesseract_coboundary_2(actual_F)
        _check_integer_tuple(actual_dF, 8)
        assert actual_dF == (0,) * 8

    # Test d:C^2->C^3 independently on its entire domain basis as well.
    for source_index in range(24):
        basis = tuple(int(i == source_index) for i in range(24))
        reference_F = {
            cell: basis[face_index[_interval_name(cell)]] for cell in face_cells
        }
        expected = {
            _interval_name(cell): value
            for cell, value in _interval_coboundary(reference_F, 3).items()
        }
        actual_dF = geometry.tesseract_coboundary_2(basis)
        _check_integer_tuple(actual_dF, 8)
        assert actual_dF == tuple(
            expected[name] for name in cube_names
        )

    selected_edges = (
        ((0, 1, 0, 0), 0), ((0, 0, 1, 0), 0),
        ((0, 0, 0, 1), 0), ((0, 0, 1, 0), 1),
    )
    zero = (0, 0, 0, 0)
    for source in TEST_SOURCES:
        record = geometry.geometry_seed(source)
        assert record.source == source
        _check_integer_tuple(record.source, 4)
        _check_frozen(record)
        _check_frozen(record.tesseract)
        assert record.tesseract.carrier_tag == "TESSERACT_3_PLUS_1_INTEGER"
        A, F = record.tesseract.edge_A, record.tesseract.face_F
        _check_integer_tuple(A, 32)
        _check_integer_tuple(F, 24)
        source_edges = dict(zip(selected_edges, source))
        assert A == tuple(source_edges.get(name, 0) for name in edge_names)
        reference_A = {
            cell: A[edge_index[_interval_name(cell)]] for cell in edge_cells
        }
        expected = {
            _interval_name(cell): value
            for cell, value in _interval_coboundary(reference_A, 2).items()
        }
        assert F == tuple(expected[name] for name in face_names)
        assert tuple(F[face_index[(zero, i, j)]] for i, j in SOURCE_AXIS_PAIRS) == tuple(
            -value for value in source
        )
        assert any(F) == any(source)
        assert geometry.tesseract_coboundary_2(F) == (0,) * 8
    _raises(TypeError, geometry.geometry_seed, (0, 0, 0, 0.5))
    _raises(TypeError, geometry.tesseract_coboundary_1, (0.0,) * 32)


def _periodic_cells(dimension):
    """Independent cells (base, axes), with axes encoded by a four-bit mask."""
    return tuple(
        (base, tuple(axis for axis in range(4) if mask & (1 << axis)))
        for base in product(range(2), repeat=4)
        for mask in range(16)
        if mask.bit_count() == dimension
    )


def _periodic_name(cell):
    base, axes = cell
    return (base, *axes)


def _periodic_boundary(cell):
    base, axes = cell
    result = []
    for position, axis in enumerate(axes):
        remaining = axes[:position] + axes[position + 1:]
        upper = tuple((value + int(k == axis)) % 2 for k, value in enumerate(base))
        sign = 1 if position % 2 == 0 else -1
        result.append(((upper, remaining), sign))
        result.append(((base, remaining), -sign))
    return tuple(result)


def _periodic_chain_boundary(chain):
    result = {}
    for cell, coefficient in chain.items():
        for facet, incidence in _periodic_boundary(cell):
            result[facet] = result.get(facet, 0) + coefficient * incidence
    return result


def _reference_windings(current):
    return tuple(
        sum(
            coefficient for (base, axes), coefficient in current.items()
            if axes == (mu,) and base[mu] == 1
        )
        for mu in range(4)
    )


def _check_torus():
    edge_cells = _periodic_cells(1)
    face_cells = _periodic_cells(2)
    edge_names = tuple(sorted(_periodic_name(cell) for cell in edge_cells))
    face_names = tuple(sorted(_periodic_name(cell) for cell in face_cells))
    assert geometry.torus_vertices() == tuple(product(range(2), repeat=4))
    assert geometry.torus_edges() == edge_names and len(edge_names) == 64
    assert geometry.torus_faces() == face_names and len(face_names) == 96
    for vertex in geometry.torus_vertices():
        _check_integer_tuple(vertex, 4)
    _check_named_cells(geometry.torus_edges(), 1)
    _check_named_cells(geometry.torus_faces(), 2)
    edge_index = {name: i for i, name in enumerate(edge_names)}
    face_index = {name: i for i, name in enumerate(face_names)}
    face_by_name = {_periodic_name(cell): cell for cell in face_cells}

    for source_index, face_name in enumerate(face_names):
        basis = tuple(int(i == source_index) for i in range(96))
        reference = _periodic_chain_boundary({face_by_name[face_name]: 1})
        expected_j = {
            _periodic_name(cell): value for cell, value in reference.items()
        }
        actual_j = geometry.torus_boundary_2(basis)
        _check_integer_tuple(actual_j, 64)
        assert actual_j == tuple(expected_j.get(name, 0) for name in edge_names)
        assert all(value == 0 for value in _periodic_chain_boundary(reference).values())
        assert _reference_windings(reference) == (0, 0, 0, 0)
        divergence = geometry.torus_boundary_1(actual_j)
        windings = geometry.torus_windings(actual_j)
        _check_integer_tuple(divergence, 16)
        _check_integer_tuple(windings, 4)
        assert divergence == (0,) * 16
        assert windings == (0, 0, 0, 0)

    # Independent full-basis checks prevent constant-zero divergence/winding
    # helpers from passing merely because every selected current is a boundary.
    vertices = tuple(product(range(2), repeat=4))
    for source_index, edge in enumerate(edge_names):
        basis = tuple(int(i == source_index) for i in range(64))
        reference = {(edge[0], (edge[1],)): 1}
        divergence = _periodic_chain_boundary(reference)
        actual_divergence = geometry.torus_boundary_1(basis)
        actual_windings = geometry.torus_windings(basis)
        _check_integer_tuple(actual_divergence, 16)
        _check_integer_tuple(actual_windings, 4)
        assert actual_divergence == tuple(
            divergence.get((vertex, ()), 0) for vertex in vertices
        )
        assert actual_windings == _reference_windings(reference)

    zero = (0, 0, 0, 0)
    for source in TEST_SOURCES:
        record = geometry.geometry_seed(source)
        _check_frozen(record.torus)
        assert record.torus.carrier_tag == "PERIODIC_TORUS_2_POWER_4_INTEGER"
        G, j = record.torus.face_G, record.torus.current_j
        _check_integer_tuple(G, 96)
        _check_integer_tuple(j, 64)
        selected = {(zero, i, k): value for (i, k), value in zip(SOURCE_AXIS_PAIRS, source)}
        assert G == tuple(selected.get(name, 0) for name in face_names)
        reference_G = {
            cell: G[face_index[_periodic_name(cell)]] for cell in face_cells
        }
        expected = {
            _periodic_name(cell): value
            for cell, value in _periodic_chain_boundary(reference_G).items()
        }
        assert j == tuple(expected.get(name, 0) for name in edge_names)
        recovered = []
        for first_axis, second_axis in SOURCE_AXIS_PAIRS:
            head = tuple(int(axis == first_axis) for axis in range(4))
            recovered.append(j[edge_index[(head, second_axis)]])
        assert tuple(recovered) == source
        assert any(j) == any(source)
        assert geometry.torus_boundary_1(j) == (0,) * 16
        assert geometry.torus_windings(j) == (0, 0, 0, 0)
    _raises(TypeError, geometry.torus_boundary_2, (0.0,) * 96)


def _reference_shells():
    # These are all three-square partitions of the five frozen squared norms.
    patterns = ((2, 6, (1, 1, 0)), (4, 1, (2, 0, 0)), (8, 15, (2, 2, 0)),
                (10, 1, (3, 1, 0)), (16, 1, (4, 0, 0)))
    return tuple(
        (norm, weight, tuple(sorted({
            tuple(sign * coordinate for sign, coordinate in zip(signs, permutation))
            for permutation in permutations(pattern)
            for signs in product((-1, 1), repeat=3)
        })))
        for norm, weight, pattern in patterns
    )


def _reference_wave_step(previous, current, shells):
    # Only the candidate support is collected here. Every coefficient below
    # is evaluated by direct pointwise lookup of f(x+v), not by scattering.
    candidates = set(previous) | set(current)
    for point in current:
        for _, _, shell in shells:
            for shift in shell:
                candidates.add(tuple(point[axis] - shift[axis] for axis in range(3)))
    result = {}
    for point in sorted(candidates):
        center = current.get(point, Fraction(0))
        laplacian = Fraction(0)
        for _, weight, shell in shells:
            neighbors = sum(
                (current.get(
                    tuple(point[axis] + shift[axis] for axis in range(3)), Fraction(0)
                ) for shift in shell),
                Fraction(0),
            )
            laplacian += weight * (len(shell) * center - neighbors)
        value = 2 * center - previous.get(point, Fraction(0)) - laplacian / 324
        if value:
            result[point] = value
    return tuple(result.items())


def _check_wave_state(state):
    assert type(state) is tuple
    points = []
    for entry in state:
        assert type(entry) is tuple and len(entry) == 2
        point, value = entry
        assert type(point) is tuple and len(point) == 3
        assert all(type(coordinate) is int for coordinate in point)
        assert sum(point) % 2 == 0
        assert type(value) is Fraction and value != 0
        points.append(point)
    assert points == sorted(set(points))


def _check_wave():
    shells = _reference_shells()
    assert geometry.SHELL_WEIGHTS == ((2, 6), (4, 1), (8, 15), (10, 1), (16, 1))
    assert type(geometry.SHELL_WEIGHTS) is tuple
    for pair in geometry.SHELL_WEIGHTS:
        _check_integer_tuple(pair, 2)
    assert tuple(len(shell) for _, _, shell in shells) == (12, 6, 12, 24, 6)
    for norm, _, shell in shells:
        actual_shell = geometry.shell_vectors(norm)
        assert type(actual_shell) is tuple and actual_shell == shell
        for point in actual_shell:
            _check_integer_tuple(point, 3)
    weighted = tuple((point, weight) for _, weight, shell in shells for point in shell)
    assert sum(weight for _, weight in weighted) == 288
    for i in range(3):
        for j in range(3):
            assert sum(weight * point[i] * point[j] for point, weight in weighted) == (
                648 if i == j else 0
            )
        assert sum(weight * point[i] ** 4 for point, weight in weighted) == 3168
        assert sum(weight * point[i] ** 6 for point, weight in weighted) == 21888
        for j in range(3):
            if i != j:
                assert sum(
                    weight * point[i] ** 2 * point[j] ** 2 for point, weight in weighted
                ) == 1056
                assert sum(
                    weight * point[i] ** 4 * point[j] ** 2 for point, weight in weighted
                ) == 4224
    assert sum(
        weight * point[0] ** 2 * point[1] ** 2 * point[2] ** 2
        for point, weight in weighted
    ) == 0

    sites = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1))
    assert geometry.WAVE_SITES == sites
    for source in TEST_SOURCES:
        psi0, psi1 = geometry.wave_initial(source)
        expected_initial = tuple(sorted(
            (point, Fraction(value)) for point, value in zip(sites, source) if value
        ))
        assert psi0 == psi1 == expected_initial
        _check_wave_state(psi0)
        _check_wave_state(psi1)
        previous, current = dict(psi0), dict(psi1)
        previous_copy, current_copy = previous.copy(), current.copy()
        psi2 = geometry.wave_step(previous, current)
        assert previous == previous_copy and current == current_copy
        _check_wave_state(psi2)
        assert psi2 == _reference_wave_step(previous, current, shells)
        if source == (1, -2, 2, -1):
            psi3 = geometry.wave_step(psi1, psi2)
            _check_wave_state(psi3)
            assert psi3 == _reference_wave_step(dict(psi1), dict(psi2), shells)
    _raises(TypeError, geometry.wave_initial, (0, 0, 0, 0.5))
    _raises(TypeError, geometry.wave_step, {}, {(0, 0, 0): 0.5})
    _raises(ValueError, geometry.wave_step, {}, {(1, 0, 0): Fraction(1)})


def run_checks() -> list[tuple[str, bool]]:
    """Run the three frozen gates; only scientific AssertionError maps to False."""
    if not __debug__:
        raise RuntimeError("geometry assertion audit requires non-optimized Python")
    results = []
    for gate_id, check in (
        ("G04_TESSERACT", _check_tesseract),
        ("G05_TORUS", _check_torus),
        ("G06_WAVE", _check_wave),
    ):
        try:
            check()
        except AssertionError:
            passed = False
        else:
            passed = True
        results.append((gate_id, passed))
    return results
