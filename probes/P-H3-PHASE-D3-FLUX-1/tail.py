# SPDX-License-Identifier: Apache-2.0
"""Exact coefficients of the first nonradial correction on two lattice rays."""

from fractions import Fraction
from shell import STENCIL, SCALE


def coefficient(h, b):
    terms = [Fraction(1)]
    for i in range(1, 7):
        rhs = {1:2*h, 2:b}.get(i, 0)
        terms.append((rhs - sum(terms[j]*terms[i-j] for j in range(1, i))) * Fraction(1,2))
    return terms[6]


def along(direction):
    n = [Fraction(x,3) for x in direction]
    moments = {2:Fraction(),4:Fraction()}
    total = Fraction()
    agrees = True
    for v, weight in STENCIL:
        h = sum(x*y for x, y in zip(n,v))
        b = sum(x*x for x in v)
        first = coefficient(h,b)
        polynomial = (b**3-15*h*h*b*b+35*h**4*b-21*h**6)/16
        agrees &= first == polynomial
        total += weight * first
        for order in moments:
            moments[order] += weight*h**order
    result = -total / (2*SCALE)
    return {"direction_times_three":direction,"relative_R_minus_four":[result.numerator,result.denominator],
            "independent_coefficients_agree":agrees,"low_moments_ok":moments=={2:648,4:3168}}


def run():
    rays = [along(n) for n in ((3,0,0),(2,2,1))]
    difference = Fraction(*rays[0]["relative_R_minus_four"])-Fraction(*rays[1]["relative_R_minus_four"])
    return {"rays":rays,"axis_minus_other":[difference.numerator,difference.denominator],
            "different_first_directional_terms":difference != 0}
