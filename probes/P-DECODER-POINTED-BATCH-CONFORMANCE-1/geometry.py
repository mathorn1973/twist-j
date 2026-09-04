"""Exact mathematical geometry for the pointed-batch decoder candidate.

CHOICES: the four source-to-edge, source-to-face and source-to-D3-site
injections below are explicitly selected decoder maps. They are not derived
physical source laws. The tesseract and periodic torus remain distinct tagged
integer carriers. The D3 wave has its own carrier and elapsed counter.

Sources: Public Canon v76, content
07910adb8418742bf52a0d204577b84b38009b18:
* canon/CANON.md, sections 2, 5 and 9;
* reproduce/maxwell/verify.py, oriented tesseract and 2^4 torus complexes;
* MAXWELL-BIANCHI, MAXWELL-AMPERE-CHAIN, MAXWELL-OBSTRUCTION-P;
* PHOTON-SPATIAL-TEMPORAL-TRANSFER and PHOTON-TEMPORAL-CHARACTERISTIC.

This module supplies no physical photon, source-current-detector bridge,
propagator theorem, occurrence law, SI scale or autonomous-update writeback.
Import defines only types, literal constants and functions: it constructs no
cells, shells, fields, trajectories, scientific checks or output records.
"""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product


Point3 = tuple[int, int, int]
Point4 = tuple[int, int, int, int]
Edge = tuple[Point4, int]
Face = tuple[Point4, int, int]
Cube = tuple[Point4, int, int, int]
Source = tuple[int, int, int, int]
WaveState = tuple[tuple[Point3, Fraction], ...]
WaveInput = Mapping[Point3, int | Fraction] | WaveState

SHELL_WEIGHTS = ((2, 6), (4, 1), (8, 15), (10, 1), (16, 1))
WAVE_SITES = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1))


@dataclass(frozen=True, slots=True)
class TesseractRecord:
    """Dense cochains in tesseract_edges()/tesseract_faces() order."""

    carrier_tag: str
    edge_A: tuple[int, ...]
    face_F: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class TorusRecord:
    """Dense integer chains in torus_faces()/torus_edges() order."""

    carrier_tag: str
    face_G: tuple[int, ...]
    current_j: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class GeometryRecord:
    """Two separately tagged carriers sharing only a declared source."""

    source: Source
    tesseract: TesseractRecord
    torus: TorusRecord


def _source(v: Source) -> Source:
    if not isinstance(v, tuple) or len(v) != 4:
        raise TypeError("source must be a tuple of four integers")
    if any(type(value) is not int for value in v):
        raise TypeError("source coefficients must be exact integers")
    return v


def _integer_values(values: Sequence[int], size: int) -> tuple[int, ...]:
    result = tuple(values)
    if len(result) != size:
        raise ValueError("integer chain/cochain has the wrong dimension")
    if any(type(value) is not int for value in result):
        raise TypeError("chain/cochain coefficients must be exact integers")
    return result


def _head(v: Point4, axis: int, periodic: bool) -> Point4:
    coordinates = list(v)
    coordinates[axis] = (coordinates[axis] + 1) % 2 if periodic else 1
    return tuple(coordinates)


def tesseract_vertices() -> tuple[Point4, ...]:
    return tuple(product((0, 1), repeat=4))


def tesseract_edges() -> tuple[Edge, ...]:
    """Lexicographic vertices, then increasing axes with v[axis] = 0."""
    return tuple(
        (v, axis)
        for v in tesseract_vertices()
        for axis in range(4)
        if v[axis] == 0
    )


def tesseract_faces() -> tuple[Face, ...]:
    return tuple(
        (v, i, j)
        for v in tesseract_vertices()
        for i, j in combinations(range(4), 2)
        if v[i] == 0 and v[j] == 0
    )


def tesseract_cubes() -> tuple[Cube, ...]:
    return tuple(
        (v, i, j, k)
        for v in tesseract_vertices()
        for i, j, k in combinations(range(4), 3)
        if v[i] == 0 and v[j] == 0 and v[k] == 0
    )


def tesseract_coboundary_1(edge_A: Sequence[int]) -> tuple[int, ...]:
    """F(v,i,j) = A(v+e_i,j)-A(v,j)-A(v+e_j,i)+A(v,i)."""
    edges = tesseract_edges()
    A = dict(zip(edges, _integer_values(edge_A, len(edges))))
    return tuple(
        A[(_head(v, i, False), j)] - A[(v, j)]
        - A[(_head(v, j, False), i)] + A[(v, i)]
        for v, i, j in tesseract_faces()
    )


def tesseract_coboundary_2(face_F: Sequence[int]) -> tuple[int, ...]:
    """Alternating forward face differences on the eight oriented cubes."""
    faces = tesseract_faces()
    F = dict(zip(faces, _integer_values(face_F, len(faces))))
    return tuple(
        F[(_head(v, i, False), j, k)] - F[(v, j, k)]
        - F[(_head(v, j, False), i, k)] + F[(v, i, k)]
        + F[(_head(v, k, False), i, j)] - F[(v, i, j)]
        for v, i, j, k in tesseract_cubes()
    )


def torus_vertices() -> tuple[Point4, ...]:
    return tuple(product((0, 1), repeat=4))


def torus_edges() -> tuple[Edge, ...]:
    """All 64 positively oriented edges, retaining both edges per 2-cycle."""
    return tuple((v, axis) for v in torus_vertices() for axis in range(4))


def torus_faces() -> tuple[Face, ...]:
    return tuple(
        (v, i, j)
        for v in torus_vertices()
        for i, j in combinations(range(4), 2)
    )


def torus_boundary_2(face_G: Sequence[int]) -> tuple[int, ...]:
    """Oriented face boundary on the periodic 2^4 integer complex."""
    faces = torus_faces()
    values = _integer_values(face_G, len(faces))
    edges = torus_edges()
    index = {edge: position for position, edge in enumerate(edges)}
    current = [0] * len(edges)
    for (v, i, j), value in zip(faces, values):
        current[index[(_head(v, i, True), j)]] += value
        current[index[(v, j)]] -= value
        current[index[(_head(v, j, True), i)]] -= value
        current[index[(v, i)]] += value
    return tuple(current)


def torus_boundary_1(current_j: Sequence[int]) -> tuple[int, ...]:
    """Head minus tail, including distinct parallel edges on the 2-torus."""
    edges = torus_edges()
    values = _integer_values(current_j, len(edges))
    vertices = torus_vertices()
    index = {v: position for position, v in enumerate(vertices)}
    divergence = [0] * len(vertices)
    for (v, axis), value in zip(edges, values):
        divergence[index[v]] -= value
        divergence[index[_head(v, axis, True)]] += value
    return tuple(divergence)


def torus_windings(current_j: Sequence[int]) -> tuple[int, int, int, int]:
    """Canonical cut sums f_mu(v,axis) = [axis=mu and v[mu]=1]."""
    edges = torus_edges()
    values = _integer_values(current_j, len(edges))
    return tuple(
        sum(
            value
            for (v, axis), value in zip(edges, values)
            if axis == mu and v[mu] == 1
        )
        for mu in range(4)
    )


def geometry_seed(v: Source) -> GeometryRecord:
    """Apply the two declared integer source injections.

    CHOICE T: A(e1,0)=v0, A(e2,0)=v1, A(e3,0)=v2, A(e2,1)=v3;
    every other tesseract edge is zero. Consequently the four base faces
    (01,02,03,12) read (-v0,-v1,-v2,-v3). F=dA is not identically zero
    as a source map, and its zero fibre is exactly the zero source.

    CHOICE P: on the distinct periodic torus, G(0,01/02/03/12)=v0/v1/v2/v3
    and all other faces are zero. Set j=boundary(G). Each coefficient has
    its own edge (e_i,j), so this current map also has only the zero source
    in its zero fibre. Conservation and zero windings follow from being a
    face boundary. No tesseract/torus or physical-field equality is asserted.
    """
    source = _source(v)
    selected_edges = (
        ((0, 1, 0, 0), 0),
        ((0, 0, 1, 0), 0),
        ((0, 0, 0, 1), 0),
        ((0, 0, 1, 0), 1),
    )
    injection_A = dict(zip(selected_edges, source))
    edge_A = tuple(injection_A.get(edge, 0) for edge in tesseract_edges())
    zero = (0, 0, 0, 0)
    selected_faces = (
        (zero, 0, 1), (zero, 0, 2), (zero, 0, 3), (zero, 1, 2),
    )
    injection_G = dict(zip(selected_faces, source))
    face_G = tuple(injection_G.get(face, 0) for face in torus_faces())
    return GeometryRecord(
        source=source,
        tesseract=TesseractRecord(
            carrier_tag="TESSERACT_3_PLUS_1_INTEGER",
            edge_A=edge_A,
            face_F=tesseract_coboundary_1(edge_A),
        ),
        torus=TorusRecord(
            carrier_tag="PERIODIC_TORUS_2_POWER_4_INTEGER",
            face_G=face_G,
            current_j=torus_boundary_2(face_G),
        ),
    )


def shell_vectors(norm_squared: int) -> tuple[Point3, ...]:
    """The complete lexicographic D3 shell for one registered squared norm."""
    if type(norm_squared) is not int:
        raise TypeError("shell squared norm must be an exact integer")
    if norm_squared not in (2, 4, 8, 10, 16):
        raise ValueError("shell is outside the registered five-shell carrier")
    return tuple(
        point
        for point in product(range(-4, 5), repeat=3)
        if sum(coordinate * coordinate for coordinate in point) == norm_squared
        and sum(point) % 2 == 0
    )


def _wave_mapping(state: WaveInput) -> dict[Point3, Fraction]:
    if isinstance(state, Mapping):
        entries = state.items()
    elif isinstance(state, tuple):
        entries = state
    else:
        raise TypeError("wave state must be a mapping or an immutable tuple")
    result = {}
    seen = set()
    for entry in entries:
        if not isinstance(entry, tuple) or len(entry) != 2:
            raise TypeError("wave entries must be (point, coefficient) tuples")
        point, value = entry
        if not isinstance(point, tuple) or len(point) != 3:
            raise TypeError("wave points must be integer triples")
        if any(type(coordinate) is not int for coordinate in point):
            raise TypeError("wave coordinates must be exact integers")
        if sum(point) % 2:
            raise ValueError("wave point is outside D3")
        if point in seen:
            raise ValueError("duplicate point in immutable wave state")
        seen.add(point)
        if type(value) is not int and not isinstance(value, Fraction):
            raise TypeError("wave coefficients must be integers or Fractions")
        coefficient = Fraction(value)
        if coefficient:
            result[point] = coefficient
    return result


def _freeze_wave(state: Mapping[Point3, Fraction]) -> WaveState:
    return tuple((point, value) for point, value in sorted(state.items()) if value)


def wave_initial(v: Source) -> tuple[WaveState, WaveState]:
    """CHOICE W: psi0=psi1=sum_j v_j delta_yj at the four WAVE_SITES.

    The first snapshot is psi0 at elapsed cut zero, the second is psi1 at
    elapsed cut one. This selected source map and two-slice initialization
    introduce no physical wave source, vacuum, photon or time calibration.
    """
    source = _source(v)
    state = _freeze_wave(
        {point: Fraction(value) for point, value in zip(WAVE_SITES, source)}
    )
    return state, state


def wave_step(previous: WaveInput, current: WaveInput) -> WaveState:
    """Return 2*current-previous-A_F0(current), exactly and without mutation.

    A_F0 f(x) = (1/324) sum_(n,v in S_n) w_n*(f(x)-f(x+v)),
    with all five registered shells, weights SHELL_WEIGHTS and flat flux one.
    Input may be a finite mapping or WaveState; output is a lexicographic
    immutable tuple of nonzero Fraction coefficients. No floating-point,
    Fourier truncation, finite periodic quotient or physical propagator
    interpretation enters. Every call advances the elapsed wave counter once.
    """
    old = _wave_mapping(previous)
    now = _wave_mapping(current)
    result = {point: -value for point, value in old.items()}
    for point, value in now.items():
        result[point] = result.get(point, Fraction(0)) + 2 * value
    stencil = tuple(
        (shift, Fraction(weight, 324))
        for norm_squared, weight in SHELL_WEIGHTS
        for shift in shell_vectors(norm_squared)
    )
    diagonal_weight = sum((weight for _, weight in stencil), Fraction(0))
    for point, value in now.items():
        result[point] = result.get(point, Fraction(0)) - diagonal_weight * value
        for shift, weight in stencil:
            target = tuple(point[axis] - shift[axis] for axis in range(3))
            result[target] = result.get(target, Fraction(0)) + weight * value
    return _freeze_wave(result)
