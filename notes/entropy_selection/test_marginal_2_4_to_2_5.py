"""Exact marginal relation between the closed horizons 2..4 and 2..5.

NON-CANONICAL.  Both certificates already replay in their own test modules;
this module pins the RELATION between them, which grounds (and bounds) any
marginal-cost expectation for longer horizons:

- optimum(2..5) - optimum(2..4) = 1/4 exactly;
- the per-block marginal is UNIFORM: every one of the 625 blocks rises by
  exactly +30 in scale 24 (ordinary 40 -> 70, special 60 -> 90);
- the first transition distance 209/2500 is IDENTICAL in both optima;
- the terminal transition of the 2..5 optimum is exactly zero.

The horizon-6 preparation layer shows the uniform continuation already fails
for the special block at 2..6 (220, not 240; see ``horizon6_prep``), so this
module is the frozen record of where uniformity held, not a prediction that
it continues.
"""

from __future__ import annotations

import unittest
from collections import Counter
from fractions import Fraction

try:
    from .coupled_exact import build_exact_coupled_certificate
    from .coupled_horizon5 import build_exact_coupled_horizon5
except ImportError:  # Direct execution from this directory.
    from coupled_exact import build_exact_coupled_certificate  # type: ignore[no-redef]
    from coupled_horizon5 import build_exact_coupled_horizon5  # type: ignore[no-redef]


class MarginalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert4 = build_exact_coupled_certificate()
        cls.cert5 = build_exact_coupled_horizon5()

    def test_optima_and_quarter_marginal(self) -> None:
        self.assertEqual(self.cert4.optimum, Fraction(417, 1250))
        self.assertEqual(self.cert5.optimum, Fraction(1459, 2500))
        self.assertEqual(
            self.cert5.optimum - self.cert4.optimum, Fraction(1, 4)
        )

    def test_per_block_marginal_is_uniform_plus_30(self) -> None:
        blocks4 = self.cert4.witness.per_block_scaled_costs
        blocks5 = self.cert5.witness.per_block_scaled_costs
        self.assertEqual(len(blocks4), 625)
        self.assertEqual(len(blocks5), 625)
        self.assertEqual(Counter(blocks4), Counter({40: 624, 60: 1}))
        self.assertEqual(Counter(blocks5), Counter({70: 624, 90: 1}))
        self.assertTrue(
            all(b5 - b4 == 30 for b4, b5 in zip(blocks4, blocks5, strict=True))
        )
        self.assertEqual(sum(blocks5) - sum(blocks4), 625 * 30)
        self.assertEqual(sum(blocks5) - sum(blocks4), 43770 - 25020)

    def test_transition_structure(self) -> None:
        transitions5 = self.cert5.witness.transition_distances
        self.assertEqual(
            transitions5,
            (Fraction(209, 2500), Fraction(1, 2), Fraction(0)),
        )
        self.assertEqual(self.cert4.witness.first_transition, Fraction(209, 2500))
        self.assertEqual(self.cert4.witness.second_transition, Fraction(1, 4))
        # first transition identical across horizons; terminal transition of
        # the longer horizon exactly zero
        self.assertEqual(transitions5[0], self.cert4.witness.first_transition)
        self.assertEqual(transitions5[-1], Fraction(0))


if __name__ == "__main__":
    unittest.main()
