#!/usr/bin/env python3
"""Exact certificate audit for P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1.

The written proof in PREREG.md owns the universal real-variable and no-go
statements. This verifier audits the complete finite shell, reciprocal
two-torsion, Herm2 determinant, normalization, and massive-extension
certificates. It performs no sampling and uses no floating point, files,
network, subprocesses, clocks, randomness, or environment input.
"""

from fractions import Fraction
from itertools import product
from collections import Counter
import sys


PROBE_ID = "P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1"
NORMS = (2, 4, 8, 10, 16)
WEIGHTS = (6, 1, 15, 1, 1)
SIZES = (12, 6, 12, 24, 6)
SCALE = Fraction(1, 324)
SPATIAL_QUARTIC = Fraction(11, 27)
TEMPORAL_QUARTIC = Fraction(1, 12)
SYMBOL_MAX = Fraction(16, 9)
MASSIVE_SAFE_MU2 = Fraction(20, 9)

D3_BASIS = (
    (Fraction(1), Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(1)),
    (Fraction(0), Fraction(1), Fraction(1)),
)
RECIPROCAL_HALF_BASIS = (
    (Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2)),
    (Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2)),
    (Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2)),
)
IDENTITY3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)


class AuditFailure(Exception):
    pass


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


def transpose(matrix):
    return tuple(tuple(matrix[r][c] for r in range(len(matrix)))
                 for c in range(len(matrix[0])))


def matmul(left, right):
    return tuple(
        tuple(sum(left[r][m] * right[m][c] for m in range(len(right)))
              for c in range(len(right[0])))
        for r in range(len(left))
    )


def matvec(matrix, vector):
    return tuple(sum(matrix[r][c] * vector[c] for c in range(len(vector)))
                 for r in range(len(matrix)))


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def all_shells():
    buckets = {norm: [] for norm in NORMS}
    for vector in product(range(-4, 5), repeat=3):
        norm = sum(entry * entry for entry in vector)
        if norm in buckets:
            buckets[norm].append(vector)
    return tuple(tuple(buckets[norm]) for norm in NORMS)


def weighted_moment(shells, weights, powers):
    total = 0
    for shell, weight in zip(shells, weights):
        for vector in shell:
            monomial = 1
            for coordinate, power in zip(vector, powers):
                monomial *= coordinate ** power
            total += weight * monomial
    return Fraction(total)


def cos_quarter_turn(integer):
    return (1, 0, -1, 0)[integer % 4]


def two_torsion_symbol(shells, weights, label):
    # label m in F_2^3 represents k = pi B^{-T} m.
    k_over_pi = matvec(RECIPROCAL_HALF_BASIS, label)
    weighted = 0
    for shell, weight in zip(shells, weights):
        for vector in shell:
            twice_phase = 2 * sum(k_over_pi[i] * vector[i] for i in range(3))
            require(twice_phase.denominator == 1, "non-quarter-turn torsion phase")
            weighted += weight * (1 - cos_quarter_turn(twice_phase.numerator))
    return SCALE * weighted


# Sparse Gaussian-rational polynomials in (Omega,x,y,z,mu).
# Coefficients are pairs (real, imaginary).
ZERO_G = (Fraction(0), Fraction(0))
ONE_G = (Fraction(1), Fraction(0))
I_G = (Fraction(0), Fraction(1))


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gneg(a):
    return (-a[0], -a[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def pclean(poly):
    return {exp: coeff for exp, coeff in poly.items() if coeff != ZERO_G}


def padd(left, right):
    out = dict(left)
    for exp, coeff in right.items():
        out[exp] = gadd(out.get(exp, ZERO_G), coeff)
    return pclean(out)


def pneg(poly):
    return pclean({exp: gneg(coeff) for exp, coeff in poly.items()})


def pmul(left, right):
    out = {}
    for ea, ca in left.items():
        for eb, cb in right.items():
            exp = tuple(a + b for a, b in zip(ea, eb))
            out[exp] = gadd(out.get(exp, ZERO_G), gmul(ca, cb))
    return pclean(out)


def pvar(index):
    exp = [0] * 5
    exp[index] = 1
    return {tuple(exp): ONE_G}


def pscale(poly, scalar):
    scalar_g = (Fraction(scalar), Fraction(0))
    return pclean({exp: gmul(coeff, scalar_g) for exp, coeff in poly.items()})


def herm2_determinant_certificate():
    omega, x, y, z, mu = (pvar(i) for i in range(5))
    iy = {exp: gmul(coeff, I_G) for exp, coeff in y.items()}
    a = padd(omega, z)
    d = padd(omega, pneg(z))
    b = padd(x, pneg(iy))
    c = padd(x, iy)
    determinant = padd(pmul(a, d), pneg(pmul(b, c)))

    expected = {}
    for variable, sign in ((omega, 1), (x, -1), (y, -1), (z, -1)):
        expected = padd(expected, pscale(pmul(variable, variable), sign))

    massive = padd(determinant, pneg(pmul(mu, mu)))
    expected_massive = padd(expected, pneg(pmul(mu, mu)))

    # Negative control: use the same off-diagonal sign twice.
    bad_determinant = padd(pmul(a, d), pneg(pmul(c, c)))
    return determinant == expected, massive == expected_massive, bad_determinant != expected


def main():
    shells = all_shells()
    require(tuple(len(shell) for shell in shells) == SIZES, "shell census")
    require(all(sum(v) % 2 == 0 for shell in shells for v in shell), "D3 support")
    require(determinant3(D3_BASIS) == -2, "D3 index")
    require(matmul(transpose(D3_BASIS), RECIPROCAL_HALF_BASIS) == IDENTITY3,
            "reciprocal half basis")

    # Exact inherited moments and normalization.
    m200 = weighted_moment(shells, WEIGHTS, (2, 0, 0))
    m110 = weighted_moment(shells, WEIGHTS, (1, 1, 0))
    m400 = weighted_moment(shells, WEIGHTS, (4, 0, 0))
    m220 = weighted_moment(shells, WEIGHTS, (2, 2, 0))
    require(m200 == 648 and m110 == 0, "quadratic moment")
    require(m400 == 3168 and m220 == 1056, "quartic moment")
    require(SCALE * m200 / 2 == 1, "quadratic normalization")
    require(SCALE * m400 / 24 == SPATIAL_QUARTIC, "spatial quartic coefficient")
    require(2 * Fraction(1, 24) == TEMPORAL_QUARTIC, "temporal quartic coefficient")

    labels = tuple(product((0, 1), repeat=3))
    values = tuple(two_torsion_symbol(shells, WEIGHTS, label) for label in labels)
    counts = Counter(values)
    expected_counts = Counter({
        Fraction(0): 1,
        Fraction(1, 3): 4,
        Fraction(32, 81): 3,
    })
    require(counts == expected_counts, "two-torsion symbol multiset")
    require(values[0] == 0, "zero torsion class")
    require(all(value > 0 for label, value in zip(labels, values) if label != (0, 0, 0)),
            "nonzero torsion positivity")

    # Each F_2^3 label is a distinct class because B^T(k/pi)=m modulo 2.
    recovered = tuple(matvec(transpose(D3_BASIS),
                             matvec(RECIPROCAL_HALF_BASIS, label))
                      for label in labels)
    require(recovered == labels and len(set(recovered)) == 8, "torsion class completeness")

    h_det, massive_det, bad_det_rejected = herm2_determinant_certificate()
    require(h_det, "Herm2 determinant")
    require(massive_det, "massive determinant")
    require(bad_det_rejected, "Herm2 sign negative control")

    # A natural separated inversion-equivariant vector square root would
    # vanish at all two-torsion classes, contradicting the seven positive
    # values above. The universal implication is proved in PREREG.md.
    require(sum(1 for value in values if value > 0) == 7, "global obstruction count")

    # Massive scalar extension: s+mu^2 stays in the real two-branch interval
    # for every momentum whenever mu^2 <= 4-max(s).
    require(Fraction(4) - SYMBOL_MAX == MASSIVE_SAFE_MU2, "massive safe interval")
    require(SYMBOL_MAX + MASSIVE_SAFE_MU2 == 4, "massive endpoint")

    # Independent finite negative controls.
    bad_weights = (5, 1, 15, 1, 1)
    bad_counts = Counter(two_torsion_symbol(shells, bad_weights, label)
                         for label in labels)
    require(bad_counts != expected_counts, "weight negative control")
    require(Fraction(1, 325) * m200 / 2 != 1, "scale negative control")
    bad_reciprocal = tuple(tuple(value + (Fraction(1) if r == 0 and c == 0 else 0)
                                    for c, value in enumerate(row))
                           for r, row in enumerate(RECIPROCAL_HALF_BASIS))
    require(matmul(transpose(D3_BASIS), bad_reciprocal) != IDENTITY3,
            "reciprocal negative control")

    lines = (
        f"PROBE {PROBE_ID}",
        "EXPOSURE RESULT_EXPOSED_PROOF_AUDIT",
        "SHELL_SIZES 12,6,12,24,6",
        "D3_INDEX 2",
        "RECIPROCAL_TWO_TORSION 8",
        "TWO_TORSION_SYMBOL_VALUES 0:1,1/3:4,32/81:3",
        "GLOBAL_SEPARATED_EQUIVARIANT_VECTOR_LIFT EMPTY",
        "HERM2_DETERMINANT Omega^2-x^2-y^2-z^2",
        "SPATIAL_QUARTIC_REMAINDER 11/27",
        "TEMPORAL_QUARTIC_REMAINDER 1/12",
        "TANGENT_HERM2_GERM AGREE",
        "MASSIVE_SCALAR_GERM AGREE",
        "MASSIVE_REAL_BRANCH_SAFE_MU2_BOUND 20/9",
        "FALSIFIERS NONE",
        "RESULT PASS",
    )
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.stderr.write(f"{PROBE_ID} STOP\n")
        raise SystemExit(1)
