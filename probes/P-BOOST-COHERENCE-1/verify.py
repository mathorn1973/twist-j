#!/usr/bin/env python3
"""Exact verifier for P-BOOST-COHERENCE-1.

The scientific checks in this file are preregistered by the adjacent
PREREG.md.  Do not execute this module before the common two-file public pin.
"""

from fractions import Fraction as F
import sys


class ScientificFailure(Exception):
    """A frozen scientific assertion failed."""


PASSED = []


def check(label, condition):
    if not condition:
        raise ScientificFailure(label)
    PASSED.append(label)


# Q(sqrt(5)): a pair (a, b) represents a + b*sqrt(5).
def q(a=0, b=0):
    return (F(a), F(b))


QZERO = q()
QONE = q(1)
QROOT5 = q(0, 1)


def qcoerce(value):
    if isinstance(value, tuple):
        return q(value[0], value[1])
    return q(value)


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qneg(x):
    return (-x[0], -x[1])


def qsub(x, y):
    return qadd(x, qneg(y))


def qmul(x, y):
    return (
        x[0] * y[0] + 5 * x[1] * y[1],
        x[0] * y[1] + x[1] * y[0],
    )


def qinv(x):
    norm = x[0] * x[0] - 5 * x[1] * x[1]
    if norm == 0:
        raise ZeroDivisionError("zero in Q(sqrt(5))")
    return (x[0] / norm, -x[1] / norm)


def qdiv(x, y):
    return qmul(x, qinv(y))


def qpow(x, exponent):
    if exponent < 0:
        return qpow(qinv(x), -exponent)
    result = QONE
    base = x
    power = exponent
    while power:
        if power & 1:
            result = qmul(result, base)
        base = qmul(base, base)
        power //= 2
    return result


# Laurent polynomials over Q(sqrt(5)), stored as sorted (power, coefficient)
# tuples.  Zero coefficients are removed at every operation.
def lp(terms=()):
    source = terms.items() if isinstance(terms, dict) else terms
    combined = {}
    for power, coefficient in source:
        coefficient = qcoerce(coefficient)
        combined[power] = qadd(combined.get(power, QZERO), coefficient)
    return tuple(
        (power, coefficient)
        for power, coefficient in sorted(combined.items())
        if coefficient != QZERO
    )


LPZERO = lp()
LPONE = lp({0: QONE})


def lpconst(value):
    return lp() if value == QZERO else lp({0: value})


def lpadd(x, y):
    return lp(tuple(x) + tuple(y))


def lpneg(x):
    return lp((power, qneg(coefficient)) for power, coefficient in x)


def lpsub(x, y):
    return lpadd(x, lpneg(y))


def lpmul(x, y):
    terms = []
    for power_x, coefficient_x in x:
        for power_y, coefficient_y in y:
            terms.append(
                (power_x + power_y, qmul(coefficient_x, coefficient_y))
            )
    return lp(terms)


def lpscale(value, polynomial):
    value = qcoerce(value)
    return lp((power, qmul(value, coefficient)) for power, coefficient in polynomial)


def lpconj(polynomial):
    return lp((-power, coefficient) for power, coefficient in polynomial)


def lpeval_one(polynomial):
    result = QZERO
    for _, coefficient in polynomial:
        result = qadd(result, coefficient)
    return result


# R = Q(sqrt(5))[z,z^-1,r]/(r^2-R2), represented by p0+p1*r.
R2 = lp(
    {
        -2: q(F(1, 20)),
        0: q(F(9, 10)),
        2: q(F(1, 20)),
    }
)


def ring(p0=LPZERO, p1=LPZERO):
    return (lp(p0), lp(p1))


RZERO = ring()
RONE = ring(LPONE)
RVAR = ring(LPZERO, LPONE)


def rconst(value):
    return ring(lpconst(value))


def rlaurent(polynomial):
    return ring(polynomial)


def radd(x, y):
    return ring(lpadd(x[0], y[0]), lpadd(x[1], y[1]))


def rneg(x):
    return ring(lpneg(x[0]), lpneg(x[1]))


def rsub(x, y):
    return radd(x, rneg(y))


def rmul(x, y):
    p0 = lpadd(lpmul(x[0], y[0]), lpmul(lpmul(x[1], y[1]), R2))
    p1 = lpadd(lpmul(x[0], y[1]), lpmul(x[1], y[0]))
    return ring(p0, p1)


def rscale(value, element):
    return ring(lpscale(value, element[0]), lpscale(value, element[1]))


def rpow(element, exponent):
    if exponent < 0:
        raise ValueError("negative ring powers are outside the carrier")
    result = RONE
    base = element
    power = exponent
    while power:
        if power & 1:
            result = rmul(result, base)
        base = rmul(base, base)
        power //= 2
    return result


def rconj(element):
    return ring(lpconj(element[0]), lpconj(element[1]))


def reval_one(element):
    # The frozen positive branch has r=1 at z=1.
    return qadd(lpeval_one(element[0]), lpeval_one(element[1]))


def matrix(a, b, c, d):
    return ((a, b), (c, d))


MZERO = matrix(RZERO, RZERO, RZERO, RZERO)
MIDENTITY = matrix(RONE, RZERO, RZERO, RONE)


def mfrom_q(a, b, c, d):
    return matrix(rconst(a), rconst(b), rconst(c), rconst(d))


def madd(x, y):
    return matrix(
        radd(x[0][0], y[0][0]),
        radd(x[0][1], y[0][1]),
        radd(x[1][0], y[1][0]),
        radd(x[1][1], y[1][1]),
    )


def mneg(x):
    return matrix(
        rneg(x[0][0]),
        rneg(x[0][1]),
        rneg(x[1][0]),
        rneg(x[1][1]),
    )


def msub(x, y):
    return madd(x, mneg(y))


def mmul(x, y):
    return matrix(
        radd(rmul(x[0][0], y[0][0]), rmul(x[0][1], y[1][0])),
        radd(rmul(x[0][0], y[0][1]), rmul(x[0][1], y[1][1])),
        radd(rmul(x[1][0], y[0][0]), rmul(x[1][1], y[1][0])),
        radd(rmul(x[1][0], y[0][1]), rmul(x[1][1], y[1][1])),
    )


def mscale(element, x):
    return matrix(
        rmul(element, x[0][0]),
        rmul(element, x[0][1]),
        rmul(element, x[1][0]),
        rmul(element, x[1][1]),
    )


def mtrace(x):
    return radd(x[0][0], x[1][1])


def mdet(x):
    return rsub(rmul(x[0][0], x[1][1]), rmul(x[0][1], x[1][0]))


def madjoint(x):
    return matrix(
        rconj(x[0][0]),
        rconj(x[1][0]),
        rconj(x[0][1]),
        rconj(x[1][1]),
    )


def meval_one(x):
    return (
        (reval_one(x[0][0]), reval_one(x[0][1])),
        (reval_one(x[1][0]), reval_one(x[1][1])),
    )


def qmatrix_scale(value, x):
    return (
        (qmul(value, x[0][0]), qmul(value, x[0][1])),
        (qmul(value, x[1][0]), qmul(value, x[1][1])),
    )


INV_ROOT5 = q(F(0), F(1, 5))
C1 = INV_ROOT5
S1 = q(F(0), F(2, 5))
C3 = q(F(0), F(2, 5))

A1 = mfrom_q(C1, S1, S1, qneg(C1))
SIGMA = mfrom_q(q(-1), QZERO, QZERO, QONE)
D = mmul(mmul(A1, SIGMA), A1)

Z = rlaurent(lp({1: QONE}))
ZINV = rlaurent(lp({-1: QONE}))
SHIFT = matrix(Z, RZERO, RZERO, ZINV)
W = mmul(SHIFT, A1)
T = mtrace(W)
H = rscale(F(1, 2), T)
LAMBDA_PLUS = radd(H, RVAR)
LAMBDA_MINUS = rsub(H, RVAR)
PPLUS = msub(W, mscale(LAMBDA_MINUS, MIDENTITY))
PMINUS = msub(W, mscale(LAMBDA_PLUS, MIDENTITY))
WINV = msub(W, mscale(T, MIDENTITY))

Z_PLUS_ZINV = lp({-1: QONE, 1: QONE})
CCOS = rlaurent(lpscale(INV_ROOT5, Z_PLUS_ZINV))
TWO_W_MINUS_T = msub(mscale(rconst(q(2)), W), mscale(T, MIDENTITY))
G = madd(mmul(mmul(PPLUS, D), PPLUS), mmul(mmul(PMINUS, D), PMINUS))
RHO = rneg(rpow(LAMBDA_MINUS, 2))
SIGMA_PHASE = rneg(rpow(LAMBDA_PLUS, 2))
XBLOCK = mmul(mmul(PPLUS, D), PMINUS)
YBLOCK = mmul(mmul(PMINUS, D), PPLUS)


def fibonacci_lucas(limit):
    fibonacci = [0, 1]
    lucas = [2, 1]
    while len(fibonacci) <= limit:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        lucas.append(lucas[-1] + lucas[-2])
    return fibonacci, lucas


def interval_count(x, width, closed):
    lower = x - width
    upper = x + width
    start = lower.numerator // lower.denominator - 2
    stop = upper.numerator // upper.denominator + 3
    if closed:
        return sum(1 for center in range(start, stop) if lower <= center <= upper)
    return sum(1 for center in range(start, stop) if lower < center < upper)


def group_integer_coins():
    positive_pairs = [
        (a, b)
        for a in range(1, 6)
        for b in range(1, 6)
        if a * a + b * b == 5
    ]
    check("F1-positive-integer-solutions", positive_pairs == [(1, 2), (2, 1)])

    fibonacci, lucas = fibonacci_lucas(101)
    odd_hits = []
    for n in range(1, 102, 2):
        check(
            "F1-odd-fibonacci-lucas-identity-n{}".format(n),
            lucas[n] * lucas[n] - 5 * fibonacci[n] * fibonacci[n] == -4,
        )
        if lucas[n] % fibonacci[n] == 0:
            odd_hits.append(n)
    check("F1-odd-rung-audit", odd_hits == [1, 3])
    check(
        "F1-rung-normalizations",
        [
            (lucas[n] // fibonacci[n], 2 // fibonacci[n])
            for n in odd_hits
        ]
        == [(1, 2), (2, 1)],
    )
    beta_1 = q(F(0), F(lucas[1], 5 * fibonacci[1]))
    beta_3 = q(F(0), F(lucas[3], 5 * fibonacci[3]))
    check("F1-beta-1", beta_1 == C1)
    check("F1-beta-3", beta_3 == C3)


def group_cover_and_half_rung():
    half = F(1, 2)
    for center in range(-8, 9):
        for numerator in range(14):
            x = F(center) + F(numerator, 14)
            check(
                "F2-half-closed-cover-{}-{}".format(center, numerator),
                interval_count(x, half, True) >= 1,
            )
    check("F2-subhalf-gap", interval_count(half, F(2, 5), True) == 0)

    for center in range(-8, 9):
        generic = F(center) + F(1, 7)
        rung = F(center)
        for width in (1, 3):
            check(
                "F2-generic-open-w{}-n{}".format(width, center),
                interval_count(generic, F(width), False) == 2 * width,
            )
            check(
                "F2-rung-open-w{}-n{}".format(width, center),
                interval_count(rung, F(width), False) == 2 * width - 1,
            )

        nonseam = F(center) + F(1, 3)
        seam = F(center) + half
        check(
            "F2-half-generic-open-n{}".format(center),
            interval_count(nonseam, half, False) == 1,
        )
        check(
            "F2-half-seam-open-n{}".format(center),
            interval_count(seam, half, False) == 0,
        )
        check(
            "F2-half-seam-closed-n{}".format(center),
            interval_count(seam, half, True) == 2,
        )

    phi = q(F(1, 2), F(1, 2))
    half_rung = qdiv(qsub(phi, QONE), qadd(phi, QONE))
    check("F2-half-rung-sqrt5-minus-2", half_rung == q(-2, 1))
    check("F2-half-rung-phi-minus-3", half_rung == qpow(phi, -3))
    check("F2-half-rung-not-admissible", half_rung not in (C1, C3))


def group_t1_velocity_operator():
    expected_d = mfrom_q(q(F(3, 5)), q(F(-4, 5)), q(F(-4, 5)), q(F(-3, 5)))
    check("F3-D-3-4-5", D == expected_d)
    check("F3-D-involution", mmul(D, D) == MIDENTITY)
    check("F3-D-trace", mtrace(D) == RZERO)
    check("F3-D-determinant", mdet(D) == rconst(q(-1)))


def group_t2_spectral_skeleton():
    check(
        "F4-Cayley-Hamilton",
        mmul(W, W) == madd(mscale(T, W), MIDENTITY),
    )
    check("F4-right-inverse", mmul(W, WINV) == MIDENTITY)
    check("F4-left-inverse", mmul(WINV, W) == MIDENTITY)
    check(
        "F4-eigenvalue-product",
        rmul(LAMBDA_PLUS, LAMBDA_MINUS) == rconst(q(-1)),
    )
    check(
        "F4-dispersion-root",
        rsub(rpow(RVAR, 2), rpow(H, 2)) == RONE,
    )
    two_r = rscale(F(2), RVAR)
    check(
        "F4-pplus-square",
        mmul(PPLUS, PPLUS) == mscale(two_r, PPLUS),
    )
    check(
        "F4-pminus-square",
        mmul(PMINUS, PMINUS) == mscale(rneg(two_r), PMINUS),
    )
    check("F4-pplus-pminus", mmul(PPLUS, PMINUS) == MZERO)
    check("F4-pminus-pplus", mmul(PMINUS, PPLUS) == MZERO)
    check(
        "F4-projector-resolution",
        msub(PPLUS, PMINUS) == mscale(two_r, MIDENTITY),
    )
    check(
        "F4-W-pplus",
        mmul(W, PPLUS) == mscale(LAMBDA_PLUS, PPLUS),
    )
    check(
        "F4-W-pminus",
        mmul(W, PMINUS) == mscale(LAMBDA_MINUS, PMINUS),
    )
    check(
        "F4-lambda-plus-unit",
        rmul(LAMBDA_PLUS, rconj(LAMBDA_PLUS)) == RONE,
    )
    check(
        "F4-lambda-minus-unit",
        rmul(LAMBDA_MINUS, rconj(LAMBDA_MINUS)) == RONE,
    )


def group_t2_gap():
    check(
        "F4-rho-ratio",
        rmul(RHO, LAMBDA_PLUS) == LAMBDA_MINUS,
    )
    one_minus_rho = rsub(RONE, RHO)
    check(
        "F4-gap",
        rmul(one_minus_rho, rconj(one_minus_rho))
        == rscale(F(4), rpow(RVAR, 2)),
    )
    cosine_squared = lpscale(
        q(F(1, 4)),
        lpmul(Z_PLUS_ZINV, Z_PLUS_ZINV),
    )
    check(
        "F4-gap-floor-polynomial",
        rsub(rpow(RVAR, 2), rconst(q(F(4, 5))))
        == rlaurent(lpscale(q(F(1, 5)), cosine_squared)),
    )


def group_t3_drift():
    check("F5-tr-WD", mtrace(mmul(W, D)) == rneg(CCOS))
    check(
        "F5-HF-plus",
        mmul(mmul(PPLUS, D), PPLUS) == mscale(rneg(CCOS), PPLUS),
    )
    check(
        "F5-HF-minus",
        mmul(mmul(PMINUS, D), PMINUS) == mscale(rneg(CCOS), PMINUS),
    )
    check(
        "F5-G-closed-form",
        G == mscale(rneg(CCOS), TWO_W_MINUS_T),
    )
    check(
        "F5-two-W-minus-t-square",
        mmul(TWO_W_MINUS_T, TWO_W_MINUS_T)
        == mscale(rscale(F(4), rpow(RVAR, 2)), MIDENTITY),
    )
    check(
        "F5-G-square",
        mmul(G, G)
        == mscale(
            rmul(rpow(CCOS, 2), rscale(F(4), rpow(RVAR, 2))),
            MIDENTITY,
        ),
    )
    cosine_squared = lpscale(
        q(F(1, 4)),
        lpmul(Z_PLUS_ZINV, Z_PLUS_ZINV),
    )
    c1_squared = F(1, 5)
    check(
        "F5-drift-numerator",
        rpow(CCOS, 2)
        == rlaurent(lpscale(q(4 * c1_squared), cosine_squared)),
    )
    check(
        "F5-drift-denominator",
        rpow(RVAR, 2)
        == radd(
            rconst(q(1 - c1_squared)),
            rlaurent(lpscale(q(c1_squared), cosine_squared)),
        ),
    )

    a1_at_one = meval_one(A1)
    expected_v_zero = qmatrix_scale(qneg(C1), a1_at_one)
    actual_v_zero = qmatrix_scale(q(F(1, 4)), meval_one(G))
    check("F5-zero-mode", actual_v_zero == expected_v_zero)

    for c_squared in (F(1, 5), F(4, 5)):
        # The coefficient of u=sin^2(k) in
        # c^2(1-c^2 u)-c^2(1-u) is c^2(1-c^2).
        width_coefficient = c_squared * (1 - c_squared)
        check(
            "F5-coherent-width-c2-{}".format(c_squared),
            width_coefficient > 0,
        )


def group_t4_uniform_read_kernel():
    four_r_squared = rscale(F(4), rpow(RVAR, 2))
    check(
        "F6-base-decomposition",
        mscale(four_r_squared, D) == msub(msub(G, XBLOCK), YBLOCK),
    )
    check("F6-G-fixed", mmul(mmul(WINV, G), W) == G)
    check(
        "F6-X-phase",
        mmul(mmul(WINV, XBLOCK), W) == mscale(RHO, XBLOCK),
    )
    check(
        "F6-conjugate-phase",
        SIGMA_PHASE == rconj(RHO),
    )
    check(
        "F6-Y-phase",
        mmul(mmul(WINV, YBLOCK), W) == mscale(rconj(RHO), YBLOCK),
    )
    check("F6-off-band-adjoints", madjoint(XBLOCK) == YBLOCK)

    r_min_squared = F(4, 5)
    uniform_constant_squared = 1 / r_min_squared
    check("F6-r-min-positive", r_min_squared > 0)
    check("F6-uniform-constant-squared", uniform_constant_squared == F(5, 4))
    check(
        "F6-uniform-constant",
        q(F(0), F(1, 2)) == qdiv(QONE, q(F(0), F(2, 5))),
    )


def group_t5_selectors():
    coins = (
        {
            "name": "beta_1",
            "width": 1,
            "multiplicity": 2,
            "c": C1,
            "c_squared": F(1, 5),
            "r_min": q(F(0), F(2, 5)),
            "r_min_squared": F(4, 5),
            "uniform_constant": q(F(0), F(1, 2)),
            "uniform_squared": F(5, 4),
            "gap_squared": F(16, 5),
        },
        {
            "name": "beta_3",
            "width": 3,
            "multiplicity": 6,
            "c": C3,
            "c_squared": F(4, 5),
            "r_min": INV_ROOT5,
            "r_min_squared": F(1, 5),
            "uniform_constant": QROOT5,
            "uniform_squared": F(5),
            "gap_squared": F(4, 5),
        },
    )

    for coin in coins:
        check(
            "F7-c-squared-{}".format(coin["name"]),
            qpow(coin["c"], 2) == q(coin["c_squared"]),
        )
        check(
            "F7-cover-multiplicity-{}".format(coin["name"]),
            coin["multiplicity"] == 2 * coin["width"],
        )
        check(
            "F7-r-min-{}".format(coin["name"]),
            coin["r_min_squared"] == 1 - coin["c_squared"],
        )
        check(
            "F7-r-min-square-{}".format(coin["name"]),
            qpow(coin["r_min"], 2) == q(coin["r_min_squared"]),
        )
        check(
            "F7-uniform-squared-{}".format(coin["name"]),
            coin["uniform_squared"] == 1 / coin["r_min_squared"],
        )
        check(
            "F7-uniform-constant-square-{}".format(coin["name"]),
            qpow(coin["uniform_constant"], 2) == q(coin["uniform_squared"]),
        )
        check(
            "F7-uniform-reciprocal-{}".format(coin["name"]),
            qmul(coin["r_min"], coin["uniform_constant"]) == QONE,
        )
        check(
            "F7-gap-squared-{}".format(coin["name"]),
            coin["gap_squared"] == 4 * coin["r_min_squared"],
        )

    minimum_multiplicity = min(coin["multiplicity"] for coin in coins)
    minimum_uniform = min(coin["uniform_squared"] for coin in coins)
    maximum_width = max(coin["width"] for coin in coins)
    s1 = [coin["name"] for coin in coins if coin["multiplicity"] == minimum_multiplicity]
    s2 = [coin["name"] for coin in coins if coin["uniform_squared"] == minimum_uniform]
    s3 = [coin["name"] for coin in coins if coin["width"] == maximum_width]
    check("F8-S1-unique-beta1", s1 == ["beta_1"])
    check("F8-S2-unique-beta1", s2 == ["beta_1"])
    check("F8-S3-unique-beta3", s3 == ["beta_3"])


GROUPS = (
    ("integer coins", group_integer_coins),
    ("cover and half-rung", group_cover_and_half_rung),
    ("T1 velocity operator", group_t1_velocity_operator),
    ("T2 spectral skeleton", group_t2_spectral_skeleton),
    ("T2 spectral gap", group_t2_gap),
    ("T3 drift", group_t3_drift),
    ("T4 uniform read kernel", group_t4_uniform_read_kernel),
    ("T5 selector ranking", group_t5_selectors),
)


def main():
    for group_name, group in GROUPS:
        before = len(PASSED)
        group()
        print(
            "PASS {} ({} checks)".format(
                group_name,
                len(PASSED) - before,
            )
        )
    print("SUMMARY PASS groups={} checks={}".format(len(GROUPS), len(PASSED)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ScientificFailure as error:
        print("FIRE {}".format(error), file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(
            "STOP code defect: {}: {}".format(type(error).__name__, error),
            file=sys.stderr,
        )
        sys.exit(2)
