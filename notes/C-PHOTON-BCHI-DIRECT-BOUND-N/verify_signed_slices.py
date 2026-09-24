#!/usr/bin/env python3
"""Exact signed-slice and insertion audit; NON-CANONICAL candidate-C.

Before execution, publicly pin this file and the unchanged imported
verify_connected_current.py. No full-measure or decay conclusion is tested.
"""

from collections import defaultdict, deque
from fractions import Fraction

from verify_connected_current import (
    add_chain, boundary, chain_boundary, cup_defect,
    oriented_components, shifted,
)


def signed_slices(chain, L):
    A = [0] * L
    for (x, axes), coefficient in chain.items():
        if axes == (0, 1):
            A[x[1] % L] += coefficient
    return A


def slice_current(current, L):
    B = [0] * L
    for (x, axes), coefficient in current.items():
        if axes == (0,):
            B[x[1] % L] += coefficient
    return B


def integer_primitive(B):
    assert sum(B) == 0
    H = [0]
    for value in B[1:]:
        H.append(H[-1] + value)
    assert all(H[r] - H[r - 1] == B[r] for r in range(len(B)))
    return H


def median_norm(H):
    median = sorted(H)[len(H) // 2]
    norm = sum(abs(value - median) for value in H)
    assert norm == min(sum(abs(value - candidate) for value in H)
                       for candidate in set(H))
    return norm, median


def audit_slice_identity(chain, current, L):
    A = signed_slices(chain, L)
    B = slice_current(current, L)
    assert all(A[r] - A[r - 1] == 5 * B[r] for r in range(L))
    H = integer_primitive(B)
    constant = A[0] - 5 * H[0]
    assert [A[r] - 5 * H[r] for r in range(L)] == [constant] * L
    assert len({value % 5 for value in A}) == 1
    norm, median = median_norm(H)
    A_norm, A_median = median_norm(A)
    assert A_norm == 5 * norm
    assert A_median == 5 * median + constant
    # The difference polynomial is a constant times 1+z+...+z^(L-1).
    # It vanishes at EVERY nonidentity L-th root, without float arithmetic.
    assert [A[r] - 5 * (H[r] - median) for r in range(L)] == [A_median] * L
    m01 = sum(abs(value) for (_, axes), value in chain.items()
              if axes == (0, 1))
    assert 5 * norm <= sum(abs(value) for value in A) <= m01
    # Exact nonzero-character audit at z=-1; the general character bound
    # is proved by the triangle inequality, not inferred from this sample.
    assert abs(sum(value * (-1) ** r for r, value in enumerate(A))) <= 5 * norm
    return A, B, H, norm, median


def current_component_sizes(current, L):
    vertex_edges = defaultdict(set)
    for edge in current:
        x, (direction,) = edge
        vertex_edges[x].add(edge)
        endpoint = tuple(t % L for t in shifted(x, direction))
        vertex_edges[endpoint].add(edge)
    unseen = set(current)
    sizes = []
    while unseen:
        seed = unseen.pop()
        component = {seed}
        queue = deque([seed])
        while queue:
            x, (direction,) = queue.popleft()
            endpoint = tuple(t % L for t in shifted(x, direction))
            for vertex in (x, endpoint):
                for edge in vertex_edges[vertex]:
                    if edge not in component:
                        component.add(edge)
                        unseen.remove(edge)
                        queue.append(edge)
        sizes.append(len(component))
    return sorted(sizes)


def audit_aligned_tube(D):
    assert D >= 3
    L = 2 * D + 4
    origin, other = (0, 0, 0, 0), (0, D + 1, 0, 0)
    first, second = cup_defect(origin, L), cup_defect(other, L)
    tube = {((0, k, 0, 0), (0, 1, 2)): 1 for k in range(1, D + 1)}
    chain = defaultdict(int)
    add_chain(chain, first)
    add_chain(chain, second)
    add_chain(chain, chain_boundary(tube, L), -1)
    chain = {cell: value for cell, value in chain.items() if value}
    assert len(chain) == 4 * D + 40
    assert set(chain.values()) <= {-1, 1}
    m01 = sum(axes == (0, 1) for _, axes in chain)
    assert m01 == 2 * D + 10
    expected_current = defaultdict(int)
    add_chain(expected_current, boundary((origin, (0, 1)), L), -1)
    add_chain(expected_current, boundary((other, (0, 1)), L), -1)
    expected_current = {edge: value for edge, value in expected_current.items() if value}
    assert chain_boundary(chain, L) == {
        edge: 5 * value for edge, value in expected_current.items()
    }
    assert current_component_sizes(expected_current, L) == [4, 4]
    incidences = defaultdict(list)
    for face in chain:
        for edge, sign in boundary(face, L).items():
            incidences[edge].append((face, sign))
    degrees, matchings = defaultdict(int), {}
    for edge, incident in incidences.items():
        degree = len(incident)
        assert degree in (2, 5)
        degrees[degree] += 1
        if degree == 2:
            matchings[edge] = ((incident[0][0], incident[1][0]),)
    assert dict(degrees) == {2: 8 * D + 60, 5: 8}
    components = oriented_components(sorted(chain), incidences, matchings)
    assert components is not None and len(components) == 1
    relative = components[0]
    anchor = min(relative)
    sign = chain[anchor] * relative[anchor]
    assert all(chain[face] == sign * relative[face] for face in chain)
    A, B, H, norm, median = audit_slice_identity(chain, expected_current, L)
    polynomial = {r: value for r, value in enumerate(A) if value}
    assert polynomial == {0: -5, D + 1: -5}
    canonical_primitive = {r: value - median for r, value in enumerate(H)
                           if value != median}
    assert canonical_primitive == {0: -1, D + 1: -1}
    assert norm == 2
    assert sum(abs(value) for value in A) == 10
    assert sum(value * value for value in A) == 50
    # Laurent polynomial |1+z^(D+1)|^2: no floating-point phases.
    autocorrelation = defaultdict(int)
    for r, value in canonical_primitive.items():
        for s, other_value in canonical_primitive.items():
            autocorrelation[r - s] += value * other_value
    assert dict(autocorrelation) == {0: 2, D + 1: 1, -(D + 1): 1}
    return L, chain, expected_current, norm


def audit_closed_slices():
    L = 8
    cube = boundary(((0, 0, 0, 0), (0, 1, 2)), L)
    assert not chain_boundary(cube, L)
    A, _, _, norm, _ = audit_slice_identity(cube, {}, L)
    assert A == [0] * L and norm == 0
    plane = {((x0, x1, 0, 0), (0, 1)): 1
             for x0 in range(L) for x1 in range(L)}
    assert not chain_boundary(plane, L)
    A, _, _, norm, _ = audit_slice_identity(plane, {}, L)
    assert A == [L] * L and norm == 0
    assert L % 5 != 0
    # Finite checks of the median quotient in nonzero residue classes.
    for residue in range(5):
        H = [-2, -1, 0, 0, 1, 3, 3, 4]
        A = [5 * value + residue for value in H]
        h_norm, h_median = median_norm(H)
        a_norm, a_median = median_norm(A)
        assert a_norm == 5 * h_norm
        assert a_median == 5 * h_median + residue
    return L


def swap_axes_one_two(chain):
    permutation = (0, 2, 1, 3)
    answer = {}
    for (x, axes), value in chain.items():
        y = [0] * 4
        for i in range(4):
            y[permutation[i]] = x[i]
        permuted_axes = [permutation[i] for i in axes]
        inversions = sum(permuted_axes[i] > permuted_axes[j]
                         for i in range(len(axes))
                         for j in range(i + 1, len(axes)))
        cell = (tuple(y), tuple(sorted(permuted_axes)))
        assert cell not in answer
        answer[cell] = (-1) ** inversions * value
    return answer


def audit_insertion(L, transverse):
    chain = cup_defect((0, 0, 0, 0), L)
    axes = (0, 1)
    if transverse:
        chain = swap_axes_one_two(chain)
        axes = (0, 2)
    assert len(chain) == 21
    assert set(chain.values()) <= {-1, 1}
    expected = boundary(((0, 0, 0, 0), axes), L)
    assert chain_boundary(chain, L) == {e: -5 * v for e, v in expected.items()}
    incidences = defaultdict(list)
    for face in chain:
        for edge, sign in boundary(face, L).items():
            incidences[edge].append((face, sign))
    degrees, matchings = defaultdict(int), {}
    neighborhood = set(chain)
    for edge, incident in incidences.items():
        degree = len(incident)
        assert degree in (2, 5)
        degrees[degree] += 1
        if degree == 2:
            matchings[edge] = ((incident[0][0], incident[1][0]),)
        x, (direction,) = edge
        for other in range(4):
            if other == direction:
                continue
            face_axes = tuple(sorted((direction, other)))
            for base in (x, tuple(v % L for v in shifted(x, other, -1))):
                face = (base, face_axes)
                assert edge in boundary(face, L)
                neighborhood.add(face)
    assert dict(degrees) == {2: 32, 5: 4}
    assert len(incidences) == 36
    assert len(neighborhood) <= 153
    assert len(neighborhood - set(chain)) <= sum(6 - len(v) for v in incidences.values()) == 132
    components = oriented_components(sorted(chain), incidences, matchings)
    assert components is not None and len(components) == 1
    relative = components[0]
    anchor = min(relative)
    sign = chain[anchor] * relative[anchor]
    assert all(chain[p] == sign * relative[p] for p in chain)
    coefficients = defaultdict(int)
    for (x, face_axes), value in chain.items():
        if face_axes == axes:
            coefficients[x[1]] += value
    coefficients = {r: v for r, v in coefficients.items() if v}
    target = {0: -3, 1: -1, L - 1: -1} if transverse else {0: -5}
    assert coefficients == target
    assert current_component_sizes({e: -v for e, v in expected.items()}, L) == [4]
    return len(neighborhood)


def main():
    print("Signed axial slices: NON-CANONICAL exact finite audit")
    for D in (3, 4, 8, 16, 32):
        L, chain, current, norm = audit_aligned_tube(D)
        print(f"D={D} L={L}: faces={len(chain)}, m01={2*D+10}, "
              f"charged_edges={len(current)}, signings=2, current_components=2, "
              f"signed_l1=10, signed_l2_squared=50, I1={norm}, bound=4")
    audit_closed_slices()
    print("Closed cube: slice=0; winding plane: constant slice=8; quotient=0")
    print("Integer residue, cyclic primitive, median quotient: PASS")
    for L in (8, 12):
        for transverse in (False, True):
            size = audit_insertion(L, transverse)
            orientation = "02" if transverse else "01"
            print(f"Insertion L={L} orientation={orientation}: faces=21, "
                  f"degrees=4x5+32x2, neighborhood={size}<=153, "
                  "one component, exact slice coefficients: PASS")
    rho = Fraction(1, 2 ** 173)
    b_floor = 25 * rho
    assert 0 < rho < b_floor < 1
    assert b_floor - 25 * rho == 0
    print("Exact floors: rho=2^-173; b_floor=25*rho; chi_floor=rho; difference=0")
    print("RESULT PASS; no uniform upper-chi estimate or positive P1 gap")


if __name__ == "__main__":
    main()
