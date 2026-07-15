#!/usr/bin/env python3
"""Focused checks for the NON-CANONICAL local lambda^5 model."""

from __future__ import annotations

import unittest
from collections import Counter

try:
    from .lambda5 import (
        J,
        LAMBDA,
        SIZE,
        CycleAction,
        Lambda5,
        arithmetic_centralizer_description,
        centralizer_description,
        centralizer_element,
        centralizer_orbits,
        commutes_with_j,
        elements,
        ideal_power_generators,
        iter_centralizer_generators,
        j_orbit_coordinates,
        j_orbit_spectrum,
        j_permutation,
        lambda_to_power,
        power_to_lambda,
        unit_multiplication_permutation,
        units,
        verify_arithmetic_centralizer,
        verify_unit_multiplication,
    )
except ImportError:  # Direct execution from this directory.
    from lambda5 import (  # type: ignore[no-redef]
        J,
        LAMBDA,
        SIZE,
        CycleAction,
        Lambda5,
        arithmetic_centralizer_description,
        centralizer_description,
        centralizer_element,
        centralizer_orbits,
        commutes_with_j,
        elements,
        ideal_power_generators,
        iter_centralizer_generators,
        j_orbit_coordinates,
        j_orbit_spectrum,
        j_permutation,
        lambda_to_power,
        power_to_lambda,
        unit_multiplication_permutation,
        units,
        verify_arithmetic_centralizer,
        verify_unit_multiplication,
    )


class Lambda5ModelTests(unittest.TestCase):
    def test_change_of_basis_is_involutive(self) -> None:
        samples = ((1, 0, 0, 0), (3, -7, 11, 5), (-2, 9, 0, -4))
        for vector in samples:
            self.assertEqual(power_to_lambda(lambda_to_power(vector)), vector)

    def test_all_digit_and_additive_normal_forms_are_unique(self) -> None:
        representatives = list(elements())
        self.assertEqual(len(representatives), SIZE)
        self.assertEqual(len({x.digits for x in representatives}), SIZE)
        self.assertEqual(len({x.lambda_coeffs for x in representatives}), SIZE)
        self.assertEqual(
            {x.lambda_coeffs[0] for x in representatives}, set(range(25))
        )
        for x in representatives:
            self.assertEqual(Lambda5.from_digits(x.digits), x)
            self.assertEqual(Lambda5.from_lambda_coeffs(x.lambda_coeffs), x)
            self.assertEqual(Lambda5.from_power_coeffs(x.power_coeffs), x)

    def test_lambda5_ideal_generators_reduce_to_zero(self) -> None:
        generators = ideal_power_generators()
        self.assertEqual(len(generators), 4)
        for generator in generators:
            self.assertEqual(Lambda5.from_power_coeffs(generator), Lambda5.zero())
        for x in elements():
            for generator in generators:
                shifted = tuple(a + b for a, b in zip(x.power_coeffs, generator))
                self.assertEqual(Lambda5.from_power_coeffs(shifted), x)

    def test_lambda_digits_and_valuation(self) -> None:
        counts = Counter(x.valuation() for x in elements())
        self.assertEqual(counts, {0: 2500, 1: 500, 2: 100, 3: 20, 4: 4, 5: 1})
        self.assertEqual(LAMBDA.valuation(), 1)
        self.assertEqual((LAMBDA * LAMBDA).valuation(), 2)
        self.assertEqual((5 * Lambda5.one()).valuation(), 4)
        self.assertEqual((LAMBDA * (5 * Lambda5.one())), Lambda5.zero())

    def test_addition_and_multiplication(self) -> None:
        points = tuple(elements())
        zero = Lambda5.zero()
        one = Lambda5.one()
        for index in range(0, SIZE, 37):
            x = points[index]
            y = points[(17 * index + 23) % SIZE]
            z = points[(31 * index + 7) % SIZE]
            self.assertEqual(x + zero, x)
            self.assertEqual(x + (-x), zero)
            self.assertEqual(x * one, x)
            self.assertEqual(x * y, y * x)
            self.assertEqual((x + y) + z, x + (y + z))
            self.assertEqual((x * y) * z, x * (y * z))
            self.assertEqual(x * (y + z), x * y + x * z)

    def test_public_j_matrix_equals_ring_multiplication(self) -> None:
        self.assertEqual(J, Lambda5.from_digits((2, -2, 1, 0, 0)))
        for x in elements():
            self.assertEqual(x.mul_by_j(), J * x)

    def test_all_ring_units_and_exact_inverses(self) -> None:
        unit_list = tuple(units())
        self.assertEqual(len(unit_list), 2500)
        self.assertEqual(len(set(unit_list)), 2500)
        self.assertTrue(all(unit.valuation() == 0 for unit in unit_list))
        self.assertTrue(verify_arithmetic_centralizer())
        for unit in unit_list:
            inverse = unit.inverse()
            self.assertEqual(unit * inverse, Lambda5.one())
            self.assertEqual(inverse * unit, Lambda5.one())
        for nonunit in (Lambda5.zero(), LAMBDA, 5 * Lambda5.one()):
            self.assertFalse(nonunit.is_unit())
            with self.assertRaises(ValueError):
                nonunit.inverse()
            with self.assertRaises(ValueError):
                unit_multiplication_permutation(nonunit)

    def test_arithmetic_centralizer_permutations(self) -> None:
        description = arithmetic_centralizer_description()
        full = centralizer_description()
        self.assertEqual(description.name, "(O/lambda^5)^x by multiplication")
        self.assertEqual(description.order, 2500)
        self.assertEqual(description.factorization, ((2, 2), (5, 4)))
        self.assertEqual(description.full_centralizer_order, full.order)
        self.assertEqual(description.index_in_full_centralizer, full.order // 2500)
        self.assertTrue(description.faithful)

        # Cover every residue digit and several principal-unit depths with
        # explicit 3125-point permutations; all 2500 units receive the exact
        # inverse/commutator gate in verify_arithmetic_centralizer above.
        samples = (
            Lambda5.from_digits((1, 0, 0, 0, 0)),
            Lambda5.from_digits((2, 0, 0, 0, 0)),
            Lambda5.from_digits((3, 1, 0, 0, 0)),
            Lambda5.from_digits((4, 0, 1, 2, 3)),
            J,
        )
        for unit in samples:
            mapping = unit_multiplication_permutation(unit)
            self.assertEqual(mapping[Lambda5.one().index], unit.index)
            self.assertTrue(verify_unit_multiplication(unit, full_carrier=True))

    def test_j_permutation_and_orbit_spectrum(self) -> None:
        permutation = j_permutation()
        self.assertEqual(set(permutation), set(range(SIZE)))
        self.assertEqual(j_orbit_spectrum(), {1: 1, 4: 1, 20: 156})
        coordinates = j_orbit_coordinates()
        self.assertEqual(len(coordinates), SIZE)
        for point, (length, cycle_number, position) in enumerate(coordinates):
            next_length, next_cycle, next_position = coordinates[permutation[point]]
            self.assertEqual((next_length, next_cycle), (length, cycle_number))
            self.assertEqual(next_position, (position + 1) % length)

    def test_full_centralizer_description_and_generators(self) -> None:
        description = centralizer_description()
        self.assertEqual(description.cycle_counts, ((1, 1), (4, 1), (20, 156)))
        self.assertEqual(
            description.abstract_factors, ("C_4", "C_20 wr S_156")
        )
        self.assertEqual(description.order, 4 * (20**156) * __import__("math").factorial(156))
        self.assertEqual(description.canonical_generator_count, 312)

        generators = list(iter_centralizer_generators())
        self.assertEqual(len(generators), 312)
        self.assertEqual(len({name for name, _ in generators}), 312)
        for _, generator in generators:
            self.assertTrue(commutes_with_j(generator))

        blocks = centralizer_orbits()
        self.assertEqual(tuple(map(len, blocks)), (1, 4, 3120))
        self.assertEqual(set().union(*map(set, blocks)), set(range(SIZE)))

    def test_parameterized_centralizer_element(self) -> None:
        sigma = list(range(156))
        sigma[0], sigma[-1] = sigma[-1], sigma[0]
        shifts = [0] * 156
        shifts[0] = 7
        shifts[-1] = -3
        action = CycleAction(20, tuple(sigma), tuple(shifts))
        mapping = centralizer_element((action,))
        self.assertTrue(commutes_with_j(mapping))


if __name__ == "__main__":
    unittest.main(verbosity=2)
