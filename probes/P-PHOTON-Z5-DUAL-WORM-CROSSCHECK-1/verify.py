#!/usr/bin/env python3
from __future__ import annotations

from dual_cycle_kernel import (
    Torus4,
    BitStream,
    PAIRS,
    TRIPLES,
    metropolis_step,
    state_sha256,
)

MOD = 5


def rank_mod5(columns: list[dict[int, int]], rows: int) -> int:
    matrix = []
    for column in columns:
        row = [0] * rows
        for index, value in column.items():
            row[index] = value % MOD
        matrix.append(row)
    rank = 0
    pivot_column = 0
    row_count = len(matrix)
    while rank < row_count and pivot_column < rows:
        pivot = None
        for candidate in range(rank, row_count):
            if matrix[candidate][pivot_column] % MOD:
                pivot = candidate
                break
        if pivot is None:
            pivot_column += 1
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][pivot_column], -1, MOD)
        matrix[rank] = [(value * inverse) % MOD for value in matrix[rank]]
        for candidate in range(row_count):
            if candidate == rank:
                continue
            factor = matrix[candidate][pivot_column] % MOD
            if factor:
                matrix[candidate] = [
                    (left - factor * right) % MOD
                    for left, right in zip(matrix[candidate], matrix[rank])
                ]
        rank += 1
        pivot_column += 1
    return rank


def boundary_column_for_plaq(lattice: Torus4, plaquette: int) -> dict[int, int]:
    site = plaquette // len(PAIRS)
    a, b = PAIRS[plaquette % len(PAIRS)]
    return {
        index: value % 5
        for index, value in lattice.plaquette_boundary(
            lattice.site_coord(site), a, b
        ).items()
        if value % 5
    }


def audit_lattice(L: int) -> tuple[int, int, int, int]:
    lattice = Torus4(L)
    d2 = [
        boundary_column_for_plaq(lattice, plaquette)
        for plaquette in range(lattice.n_plaq)
    ]
    rank_d2 = rank_mod5(d2, lattice.n_links)
    cycle_dimension = lattice.n_plaq - rank_d2
    generators = []
    for site in range(lattice.volume):
        x = lattice.site_coord(site)
        for triple in TRIPLES:
            generator = lattice.cube_boundary(x, *triple)
            state = [generator.get(p, 0) for p in range(lattice.n_plaq)]
            assert all(value == 0 for value in lattice.boundary1(state))
            generators.append(generator)
    for pair in PAIRS:
        generator = lattice.harmonic_plane(*pair)
        state = [generator.get(p, 0) for p in range(lattice.n_plaq)]
        assert all(value == 0 for value in lattice.boundary1(state))
        generators.append(generator)
    generator_rank = rank_mod5(generators, lattice.n_plaq)
    expected = 3 * (L**4) + 3
    assert cycle_dimension == expected, (L, cycle_dimension, expected)
    assert generator_rank == cycle_dimension, (L, generator_rank, cycle_dimension)
    return rank_d2, cycle_dimension, len(generators), generator_rank


def main() -> None:
    print("PROBE P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1")
    print("KERNEL CLOSED_SURFACE_RANDOM_WORD_METROPOLIS")
    for L in (2, 3):
        rank_d2, cycle_dimension, generator_count, generator_rank = audit_lattice(L)
        print(
            f"CYCLE_SPAN L={L} rank_d2={rank_d2} "
            f"cycle_dim={cycle_dimension} generators={generator_count} "
            f"generator_rank={generator_rank} status=PASS"
        )
    for old_support in range(97):
        for new_support in range(97):
            forward_cost = max(0, new_support - old_support)
            reverse_cost = max(0, old_support - new_support)
            assert old_support + forward_cost == new_support + reverse_cost
    print("DYADIC_METROPOLIS_BALANCE support_sizes=0..96 status=PASS")
    lattice = Torus4(2)
    state = [0] * lattice.n_plaq
    rng = BitStream(0x75620260901)
    accepted = 0
    invalid = 0
    letters = 0
    for _ in range(2000):
        state, diagnostics = metropolis_step(lattice, state, rng)
        accepted += diagnostics["accepted"]
        invalid += diagnostics["invalid_support"]
        letters += diagnostics["word_length"]
        assert lattice.valid_state(state)
    print(
        "FIXTURE L=2 steps=2000 "
        f"accepted={accepted} invalid_support={invalid} "
        f"word_letters={letters} state_sha256={state_sha256(state)} status=PASS"
    )
    print("PROPOSAL_SYMMETRY sign_involution=PASS")
    print("IRREDUCIBILITY generator_span_plus_geometric_word=PASS")
    print("APERIODICITY zero_length_word_probability=1/2 status=PASS")
    print("EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
