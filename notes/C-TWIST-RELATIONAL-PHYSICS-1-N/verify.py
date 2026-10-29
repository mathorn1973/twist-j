#!/usr/bin/env python3
"""Exact finite certificates for C-TWIST-RELATIONAL-PHYSICS-1-N.

NON-CANONICAL. This module defines the proposed verifier; importing it does
not execute verification. Run it only after the parent freezes the public
preregistration. It uses Python integers and fractions only, with no floats,
random sampling, network, external packages, or dense apparatus matrices.

The operator/projector proof, arbitrary mixed/reference statements, Born
adoption, and physical preparation remain in PROOF.md. This script checks
their finite arithmetic certificates and explicitly scoped controls. It
does not enumerate a matrix of dimension 561**2 * 657072000 or independently
rederive the inherited 140-gate source apparatus.
"""

from fractions import Fraction
from math import comb, gcd, prod
import sys


CANDIDATE_ID = "C-TWIST-RELATIONAL-PHYSICS-1-N"
SOURCE_COMMIT = "a193e389fb1ddb0bdc89165b015c95a17eb1e425"
D_CLOCK = 561
K_CURSOR = 560
L_WORD = 140
DATA_DIMS = (15, 15, 15, 4, 3, 26, 26, 3, 2, 2, 2)
DATA_DIMENSION = 657072000
WINDOW_FIRST = 187
WINDOW_LAST = 374
WINDOW_COUNT = 188
JOINT_FLOOR = Fraction(47, 14025)
ROBUST_FLOOR = Fraction(1, 400)


class VerificationFailure(Exception):
    """One frozen finite arithmetic certificate failed."""


def require(condition, message):
    if not condition:
        raise VerificationFailure(message)


class Q5:
    """An exact element a + b*sqrt(5), with rational coefficients."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Q5) else Q5(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Q5(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        return Q5(
            self.a * other.a + 5 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a * self.a - 5 * self.b * self.b
        require(norm != 0, "division by zero in Q(sqrt(5))")
        return Q5(self.a / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) * self.inverse()

    def __eq__(self, other):
        other = self.coerce(other)
        return self.a == other.a and self.b == other.b

    def sign(self):
        """Exact sign, using only rational signs and squared comparisons."""
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        square_difference = a * a - 5 * b * b
        # Opposite nonzero rational coefficients cannot have equal squares
        # here: 5 is not a rational square. Preserve the exact zero case
        # defensively without introducing a numerical tolerance.
        squared_sign = (square_difference > 0) - (square_difference < 0)
        return squared_sign if a > 0 else -squared_sign


def endpoint_delta():
    numerator = Q5(65536 * 48533, -65536 * 10985)
    denominator = Q5(5**9 * 39521, 5**9 * 154)
    require(denominator.sign() > 0, "endpoint denominator is not positive")
    return numerator / denominator


def tail_epsilon():
    return Fraction(3, 16) ** L_WORD


def exact_joint_lower_bound():
    # The analytic proof gives B_j > 1-epsilon on the entire clock window.
    return endpoint_delta() * Fraction(WINDOW_COUNT, D_CLOCK) * (1 - tail_epsilon())


def gate_01_constants_and_resources():
    d, k, length = D_CLOCK, K_CURSOR, L_WORD
    require((d, k, length) == (561, 560, 140), "frozen integer tuple changed")
    require(d == k + 1 and k == 4 * length, "cursor/padding relation failed")
    require(len(DATA_DIMS) == 11, "wrong data-register count")
    require(prod(DATA_DIMS) == DATA_DIMENSION, "wrong complete data dimension")
    require(12 * 8 + 17 + 2 + 3 * 8 + 1 == length, "inherited gate-count certificate failed")
    full_dims = (d, d) + DATA_DIMS
    require(len(full_dims) == 13, "the extra reference clock was not counted")
    require(prod(full_dims) == d * d * DATA_DIMENSION, "wrong complete physical carrier dimension")
    require(prod(full_dims) != d * DATA_DIMENSION, "two clocks collapsed into one")


def gate_02_positive_energy_and_complete_sector():
    d, k = D_CLOCK, K_CURSOR
    energy_star = Fraction(2 * k + 1, d)
    apparatus = tuple(Fraction(2 * s + 1, d) for s in range(d))
    clock = tuple(Fraction(2 * q, d) for q in range(d))
    require(energy_star == Fraction(1121, 561), "wrong fixed total energy")
    require(min(apparatus) == Fraction(1, d), "wrong positive apparatus floor")
    require(max(apparatus) == energy_star, "wrong apparatus ceiling")
    require(min(clock) == 0 and max(clock) == Fraction(2 * k, d), "wrong finite clock capacity")
    require(all(e > 0 for e in apparatus), "nonpositive apparatus energy")
    require(all(e >= 0 for e in clock), "negative clock energy")
    for s in range(d):
        q = k - s
        require(apparatus[s] + clock[q] == energy_star, "complementary energy matching failed")
    # This full finite census proves that VV* is the COMPLETE E_* sector,
    # conditional on the analytical complete-projector decomposition of H_A.
    matching_pairs = 0
    for q in range(d):
        for s in range(d):
            matches = 2 * q + 2 * s + 1 == 2 * k + 1
            require(matches == (q == k - s), "unexpected fixed-energy pair")
            matching_pairs += int(matches)
    require(matching_pairs == d, "wrong number of complementary energy pairs")


def gate_03_fourier_geometric_sum_certificate():
    d = D_CLOCK
    # A primitive d-th root zeta is part of the mathematical definition.
    # For a difference r!=0, the residues q*r consist of every multiple
    # of gcd(d,r), each gcd(d,r) times. Their sum evaluates to zero by
    # the exact geometric identity at a root of order d/gcd(d,r)>1.
    # This certifies all d**2 clock inner products through their differences.
    for r in range(d):
        counts = [0] * d
        for q in range(d):
            counts[(q * r) % d] += 1
        require(sum(counts) == d, "Fourier sum has the wrong term count")
        if r == 0:
            require(counts[0] == d and not any(counts[1:]), "diagonal Fourier norm failed")
            continue
        g = gcd(d, r)
        order = d // g
        require(order > 1 and (order * r) % d == 0, "wrong nontrivial root order")
        require(all((m * r) % d != 0 for m in range(1, order)), "root order is not minimal")
        require(
            all(counts[a] == (g if a % g == 0 else 0) for a in range(d)),
            "Fourier residue multiplicities failed",
        )
        # Polynomial certificate: (1-X^g) * sum_{m=0}^{order-1} X^(gm)
        # equals 1-X^d. Check its integer coefficients before evaluation.
        geometric = [0] * (d + 1)
        for m in range(order):
            geometric[g * m] += 1
            geometric[g * (m + 1)] -= 1
        require(geometric[0] == 1 and geometric[d] == -1, "geometric endpoints failed")
        require(not any(geometric[1:d]), "geometric polynomial did not telescope")


def gate_04_all_forward_phase_coefficients():
    d, k = D_CLOCK, K_CURSOR
    count = 0
    for j in range(d):
        for s in range(d):
            q = k - s
            # Exponents use w=exp(pi*i/d), of order 2d. The left is
            # <t_j|K-s>; the right is exp(+i E_* tau_j) exp(-i E_s tau_j).
            left = 2 * q * j
            right = ((2 * k + 1) - (2 * s + 1)) * j
            require(left == right, "clock-conditioned forward operator coefficient failed")
            require((left - right) % (2 * d) == 0, "phase residue equality failed")
            count += 1
    require(count == d * d, "phase certificate omitted a clock/energy pair")


def gate_05_clock_shift_and_density_period():
    d = D_CLOCK
    for q in range(d):
        for j in range(d):
            evolved = -2 * q * j - 2 * q
            shifted = -2 * q * ((j + 1) % d)
            require((evolved - shifted) % (2 * d) == 0, "clock-grid shift identity failed")
    for s in range(d):
        require((2 * s + 1) % 2 == 1, "apparatus recurrence is not the common minus sign")
    require(d > 1, "clock cannot distinguish the declared finite readings")
    # The spectrum makes U_A(d*tau_0)=-I; density period follows
    # analytically. No monotonically increasing cycle register is added.


def gate_06_exact_spectral_binomial_moments():
    d, k = D_CLOCK, K_CURSOR
    weights = tuple(comb(k, s) for s in range(d))
    total = 2**k
    require(sum(weights) == total, "spectral binomial weights are not normalized")
    require(sum(s * weights[s] for s in range(d)) == k * 2 ** (k - 1), "wrong binomial mean")
    centered = sum((2 * s - k) ** 2 * weights[s] for s in range(d))
    require(centered == k * total, "wrong exact binomial variance")
    mean_a = Fraction(sum((2 * s + 1) * weights[s] for s in range(d)), d * total)
    mean_c = Fraction(sum(2 * (k - s) * weights[s] for s in range(d)), d * total)
    var_a = Fraction(centered, d * d * total)
    var_c = Fraction(sum((k - 2 * s) ** 2 * weights[s] for s in range(d)), d * d * total)
    covariance = Fraction(sum((2 * s - k) * (k - 2 * s) * weights[s] for s in range(d)), d * d * total)
    require(mean_a == 1 and mean_c == Fraction(k, d), "wrong complete mean-energy account")
    require(var_a == Fraction(k, d * d) and var_c == var_a, "wrong component energy variance")
    require(covariance == -var_a, "energy anticorrelation failed")
    require(var_a + var_c + 2 * covariance == 0, "total energy has nonzero variance")
    require(mean_a + mean_c == Fraction(2 * k + 1, d), "mean total energy differs from E_*")
    # Independence from arbitrary data follows from W|0,psi>=|0,psi>
    # and the full-projector spin proof, not from enumeration of data states.


def gate_07_window_and_exact_angle_interval():
    d = D_CLOCK
    window = tuple(range(WINDOW_FIRST, WINDOW_LAST + 1))
    require(len(window) == WINDOW_COUNT, "wrong inclusive clock-window count")
    require(d - len(window) == 373, "wrong retained complementary clock-outcome count")
    require(window[0] * 3 == d and window[-1] * 3 == 2 * d, "window is not [T_h,2T_h]")
    require(all(d <= 3 * j <= 2 * d for j in window), "a clock angle left [pi/3,2pi/3]")
    require(Fraction(len(window), d) == Fraction(188, 561), "wrong window probability")
    # Analytic certificate, not a floating-point sine sample:
    # x in [pi/3,2pi/3] => sin(x)>=sqrt(3)/2 => sin(x)^2>=3/4.
    require(Fraction(3, 4) > Fraction(1, 2), "frozen binomial success floor changed")


def gate_08_exact_quadratic_endpoint_contrast():
    root5 = Q5(0, 1)
    require(root5 * root5 == Q5(5), "Q(sqrt(5)) multiplication failed")
    require(Q5(-2, 1).sign() > 0 and Q5(3, -1).sign() > 0, "wrong real embedding of sqrt(5)")
    denominator = Q5(39521, 154)
    require(denominator * denominator.inverse() == Q5(1), "quadratic inverse failed")
    delta = endpoint_delta()
    require((delta - Fraction(1, 50)).sign() > 0, "inherited endpoint contrast is not greater than 1/50")
    require((Q5(1) - delta).sign() > 0, "endpoint probability difference exceeds one")


def gate_09_uniform_tail_integer_certificate():
    k, length = K_CURSOR, L_WORD
    epsilon = tail_epsilon()
    require(k == 4 * length, "Markov exponent relation failed")
    require(epsilon == Fraction(3**length, 2**k), "Markov tail expressions differ")
    require(0 < epsilon < Fraction(1, 2**280) < Fraction(1, 2), "strict exact tail hierarchy failed")
    # At the least admitted p=3/4, E[3^-M]=(1-p+p/3)^K=2^-K.
    p_floor = Fraction(3, 4)
    require(1 - p_floor + p_floor / 3 == Fraction(1, 2), "Markov generating function failed")
    exact_boundary_tail = Fraction(sum(comb(k, m) * 3**m for m in range(length)), 4**k)
    require(0 < exact_boundary_tail < epsilon, "exact binomial boundary tail violates the analytic bound")
    # For every p>=3/4 the same generating function is <=1/2;
    # Markov's strict event M<L proves the all-window bound analytically.


def gate_10_complete_joint_contrast_bound():
    require(Fraction(WINDOW_COUNT, D_CLOCK) * Fraction(1, 100) == JOINT_FLOOR, "joint floor omitted the clock probability")
    lower = exact_joint_lower_bound()
    require((lower - JOINT_FLOOR).sign() > 0, "strict unconditional joint contrast bound failed")
    require((Q5(1) - lower).sign() > 0, "joint lower bound is not a probability contrast")


def gate_11_conditional_robustness_budget():
    epsilon_plus = Fraction(1, 10000)
    epsilon_minus = Fraction(1, 10000)
    eta_effect = Fraction(1, 10000)
    loss = epsilon_plus + epsilon_minus + 2 * eta_effect
    require(loss == Fraction(1, 2500), "wrong two-setting effect/preparation error coefficient")
    require(JOINT_FLOOR - loss > ROBUST_FLOOR, "frozen sufficient budget does not preserve contrast 1/400")
    require((exact_joint_lower_bound() - loss - ROBUST_FLOOR).sign() > 0, "strong exact robust contrast bound failed")
    # The trace-distance/effect-norm probability inequality is the
    # analytical premise. This gate checks its frozen rational budget;
    # it does not assert laboratory preparation or fabrication precision.


def gate_12_reject_wrong_energy_pairing():
    d, k = D_CLOCK, K_CURSOR
    # Wrong q=s matches only the middle energy s=K/2 and fails globally.
    bad_matches = [s for s in range(d) if 2 * s + 2 * s + 1 == 2 * k + 1]
    require(bad_matches == [k // 2], "wrong-pairing control did not have its exact single exception")
    require(len(bad_matches) != d, "wrong q=s energy pairing was accepted")
    require(1 != 2 * k + 1, "explicit s=0 wrong-pairing witness vanished")


def gate_13_reject_wrong_fourier_sign():
    d = D_CLOCK
    # Remove the common source-independent phase by comparing each s
    # with s=0. The wrong clock ket sign produces +2*s*j rather than
    # -2*s*j in exponents of exp(pi*i/d), i.e. backward evolution.
    failures = 0
    for j in range(d):
        for s in range(d):
            wrong_relative = 2 * s * j
            forward_relative = -2 * s * j
            failures += int((wrong_relative - forward_relative) % (2 * d) != 0)
    require(failures > 0, "wrong Fourier sign passed every forward coefficient")
    require((2 - (-2)) % (2 * d) != 0, "explicit j=s=1 wrong-sign witness vanished")


def matrix_scale(a, scalar):
    return tuple(tuple(scalar * entry for entry in row) for row in a)


def matrix_add(a, b):
    return tuple(tuple(x + y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def matrix_multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0])))
        for i in range(len(a))
    )


def matrix_trace(a):
    return sum(a[i][i] for i in range(len(a)))


def coherent_two_sector_data():
    half = Fraction(1, 2)
    coherent = ((half, half), (half, half))
    dephased = ((half, Fraction(0)), (Fraction(0), half))
    return coherent, dephased


def gate_14_dephasing_destroys_conditional_coherence():
    # Two nonzero apparatus spectral sectors s=0,1 are embedded in the
    # actual model. At j=0 all clock coefficients are exactly 1/sqrt(d).
    # Dephasing the paired sectors preserves their energy populations but
    # kills the off-diagonal entries of the conditional apparatus state.
    coherent, dephased = coherent_two_sector_data()
    effect_plus = coherent
    require(matrix_trace(coherent) == 1 and matrix_trace(dephased) == 1, "two-sector states are not normalized")
    require(matrix_multiply(coherent, coherent) == coherent, "coherent effect is not a rank-one projection")
    p_coherent = matrix_trace(matrix_multiply(effect_plus, coherent))
    p_dephased = matrix_trace(matrix_multiply(effect_plus, dephased))
    require(p_coherent == 1 and p_dephased == Fraction(1, 2), "dephasing did not destroy the declared conditional coherence")
    require(
        matrix_trace(matrix_scale(coherent, Fraction(1, D_CLOCK)))
        == matrix_trace(matrix_scale(dephased, Fraction(1, D_CLOCK)))
        == Fraction(1, D_CLOCK),
        "dephasing control changed the clock probability",
    )
    e0, e1 = Fraction(1, D_CLOCK), Fraction(3, D_CLOCK)
    energy = ((e0, Fraction(0)), (Fraction(0), e1))
    require(
        matrix_trace(matrix_multiply(energy, coherent))
        == matrix_trace(matrix_multiply(energy, dephased)),
        "dephasing control did not preserve the energy populations",
    )


def gate_15_compressed_effect_coefficient_and_nonprojectivity():
    d = D_CLOCK
    projection, _ = coherent_two_sector_data()
    identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    complement = matrix_add(identity, matrix_scale(projection, -1))
    e_plus = matrix_scale(projection, Fraction(1, d))
    e_minus = matrix_scale(complement, Fraction(1, d))
    require(matrix_multiply(e_plus, e_plus) == matrix_scale(e_plus, Fraction(1, d)), "wrong compressed effect-square coefficient")
    require(matrix_multiply(e_plus, e_plus) != e_plus, "compressed effect was incorrectly treated as projective")
    require(matrix_add(e_plus, e_minus) == matrix_scale(identity, Fraction(1, d)), "one clock slice does not sum to I/d")
    require(matrix_scale(matrix_add(e_plus, e_minus), d) == identity, "complete clock/pointer coefficient sum failed")
    # Positivity in this exact two-sector witness is certified by its
    # eigenvalues {0,1/d}; the general compression proof is analytical.
    determinant = e_plus[0][0] * e_plus[1][1] - e_plus[0][1] * e_plus[1][0]
    require(determinant == 0 and matrix_trace(e_plus) == Fraction(1, d), "wrong nonnegative compressed-effect eigenvalues")
    energy_star = Fraction(2 * K_CURSOR + 1, d)
    sector_energy = matrix_scale(identity, energy_star)
    require(
        matrix_multiply(sector_energy, e_plus) == matrix_multiply(e_plus, sector_energy),
        "compressed effect failed to commute on the fixed-energy sector",
    )
    # Orthogonal-block extension: two vectors in the actual physical
    # shell plus one vector outside it. E_out is essential for a POVM
    # on the full space; it must not disappear in imperfect trials.
    zero = Fraction(0)
    one = Fraction(1)
    q_star = ((one, zero, zero), (zero, one, zero), (zero, zero, zero))
    e_out = ((zero, zero, zero), (zero, zero, zero), (zero, zero, one))
    identity3 = ((one, zero, zero), (zero, one, zero), (zero, zero, one))
    shell_effect = (
        (e_plus[0][0], e_plus[0][1], zero),
        (e_plus[1][0], e_plus[1][1], zero),
        (zero, zero, zero),
    )
    h_total3 = (
        (energy_star, zero, zero),
        (zero, energy_star, zero),
        (zero, zero, Fraction(1, d)),
    )
    require(matrix_add(q_star, e_out) == identity3, "full-carrier E_out completeness failed")
    require(matrix_multiply(q_star, e_out) == matrix_scale(identity3, 0), "physical and outside blocks are not orthogonal")
    require(matrix_multiply(e_out, e_out) == e_out, "outside effect is not its stated projection")
    require(matrix_multiply(h_total3, shell_effect) == matrix_multiply(shell_effect, h_total3), "compressed full-block effect does not commute with total energy")
    require(matrix_multiply(h_total3, e_out) == matrix_multiply(e_out, h_total3), "outside effect does not commute with total energy")
    # Coarse clock effect is Q_*/d. Its mathematical square-root
    # instrument leaves the normalized joint physical state unchanged.
    # Its apparatus marginal is energy-dephased, whereas a local clock
    # conditioning gives the coherent state. They are NOT the same
    # instrument post-state. Physical implementation is not asserted.
    coherent, dephased = coherent_two_sector_data()
    require(coherent != dephased, "local conditional state was silently identified with the compressed-instrument marginal")
    require(matrix_scale(identity, Fraction(1, d)) == matrix_add(e_plus, e_minus), "coarse compressed clock effect differs from Q_*/d")


GATES = (
    ("G01 constants, complete carrier, two clocks", gate_01_constants_and_resources),
    ("G02 positive energies and complete fixed-energy sector", gate_02_positive_energy_and_complete_sector),
    ("G03 Fourier orthogonality: integer geometric certificates", gate_03_fourier_geometric_sum_certificate),
    ("G04 all 561^2 forward-phase coefficients", gate_04_all_forward_phase_coefficients),
    ("G05 cyclic clock shift and apparatus density return", gate_05_clock_shift_and_density_period),
    ("G06 exact spectral binomial normalization and energy moments", gate_06_exact_spectral_binomial_moments),
    ("G07 188 clock readings and exact sine-bound interval", gate_07_window_and_exact_angle_interval),
    ("G08 exact Q(sqrt(5)) endpoint contrast", gate_08_exact_quadratic_endpoint_contrast),
    ("G09 uniform Markov tail and exact binomial boundary", gate_09_uniform_tail_integer_certificate),
    ("G10 unconditional joint contrast above 47/14025", gate_10_complete_joint_contrast_bound),
    ("G11 conditional robustness budget above 1/400", gate_11_conditional_robustness_budget),
    ("G12 negative control: wrong energy pairing rejected", gate_12_reject_wrong_energy_pairing),
    ("G13 negative control: wrong Fourier sign rejected", gate_13_reject_wrong_fourier_sign),
    ("G14 negative control: paired dephasing loses coherence", gate_14_dephasing_destroys_conditional_coherence),
    ("G15 complete compressed POVM, E_out, and instrument distinction", gate_15_compressed_effect_coefficient_and_nonprojectivity),
)


def main():
    print(CANDIDATE_ID)
    print("SOURCE " + SOURCE_COMMIT)
    print("MODE exact integers, fractions, and Q(sqrt(5)); no floating point")
    try:
        for name, gate in GATES:
            gate()
            print(name + ": PASS")
    except VerificationFailure as error:
        print("RESULT FAIL: " + str(error))
        return 1
    print("RESULT PASS: 15 frozen finite certificates")
    print("SCOPE analytical operator proof and inherited source premises remain explicit")
    print("STATUS NON-CANONICAL; no physical realization, native derivation, or public promotion")
    return 0


if __name__ == "__main__":
    sys.exit(main())
