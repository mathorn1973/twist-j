# SPDX-License-Identifier: Apache-2.0
"""Audit the slipped Canon normalization and two identical-flux scalar comparators."""

from fractions import Fraction
from hashlib import sha256
import importlib.util
from math import comb, isqrt
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[2] / "reproduce/alpha-value/verify.py"
if sha256(SOURCE.read_bytes()).hexdigest() != "e967e5df82fa06bcf68bcd6c914f6ae25fe79e1a971ede8faf7ccfffe0c6cc17":
    raise ValueError("alpha arithmetic pin")
spec = importlib.util.spec_from_file_location("canonical_interval", SOURCE)
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)


def pair(x):
    return x.numerator, x.denominator


def normalization():
    sc = iv.SC
    one = (sc, sc)
    pi2 = iv.ipow(iv.pi_interval(), 2)
    root5floor = isqrt(5 * sc * sc)
    phi = ((sc + root5floor)//2, (sc + root5floor + 1)//2 + 1)
    b = iv.idiv(one, iv.imul((160*sc,160*sc), iv.ipow(phi,4)))
    slip = iv.idiv(one, iv.ipow(iv.iadd(one, iv.idiv(b,pi2)), 5))
    delta = iv.isub(one,slip)
    ppm = (10**6 * delta[0] // sc, -(-10**6 * delta[1] // sc))
    coeffs = [comb(5, k) for k in range(6)]
    # At the symbolic denominator root t=-b, numerator t^4/b^4 is +1.
    return {"relative_bare_to_committed_correction_ppm_outward":ppm,
            "reciprocal_binomial":coeffs,
            "numerator_at_minus_b_over_b4":(-1)**4,
            "positive_correction_below_one_per_mille":0 < delta[0] <= delta[1] < sc//1000}


def run(shell_result):
    comparisons = []
    for box in shell_result["boxes"]:
        difference = Fraction(*box["monopole_G_200_minus_G_400"])
        trials = []
        for z in (1, 2):
            potential = difference / z
            trials.append({"Z":z, "work_difference_for_unit_probe":pair(potential),
                           "four_time_units_work":pair(4*potential),
                           "weighted_current_difference_multiplier":pair(Fraction(z,z))})
        comparisons.append({"half_width":box["half_width"], "trials":trials,
                            "nonzero":difference != 0,
                            "same_flux_different_work":difference != difference/2})
    return {"finite_boxes":comparisons,"adopted_formula":normalization()}
