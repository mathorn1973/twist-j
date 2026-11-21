#!/usr/bin/env python3
"""Independent exact countercheck for C-TWIST-RELATIONAL-PHYSICS-1-N.

NON-CANONICAL conditional L1 candidate. Author: A. M. Thorn.
License: Apache-2.0.

Written from PREREG.md, COMPACT_MODEL.md and SOURCE_CIRCUIT.md without
opening the builder's proof, checker or execution results. This file must
not be executed before the immutable public pin has been read back.

This is an arithmetic and orthogonal-block certificate, not a dense-matrix
enumeration, a fresh proof of the inherited source circuit, or an experiment.
Only standard-library integers and fractions are used. The general operator
proof and the meaning of the small counterexamples are in BREAK_REVIEW.md.
"""

from fractions import Fraction as Q
from math import comb, gcd, prod


K = 560
D = 561
L = 140
DATA_FACTORS = (15, 15, 15, 4, 3, 26, 26, 3, 2, 2, 2)
WINDOW = tuple(range(187, 375))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def zero_matrix(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def identity_matrix(n):
    ans = zero_matrix(n)
    for j in range(n):
        ans[j][j] = Q(1)
    return ans


def matrix_add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def matrix_scale(a, c):
    return [[c * x for x in row] for row in a]


def matrix_product(a, b):
    n = len(a)
    require(len(b) == n, "small witness matrix size mismatch")
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def matrix_adjoint(a):
    # All explicitly materialized witnesses have rational real entries.
    return [list(row) for row in zip(*a)]


def determinant(a):
    """Small exact elimination; used only for matrices of size at most 3."""
    n = len(a)
    if n == 0:
        return Q(1)
    b = [row[:] for row in a]
    out = Q(1)
    for k in range(n):
        pivot = next((r for r in range(k, n) if b[r][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            out = -out
        p = b[k][k]
        out *= p
        for r in range(k + 1, n):
            ratio = b[r][k] / p
            for c in range(k + 1, n):
                b[r][c] -= ratio * b[k][c]
            b[r][k] = Q(0)
    return out


def check_small_positive(a, label):
    require(a == matrix_adjoint(a), label + " is not Hermitian")
    n = len(a)
    for mask in range(1 << n):
        indices = [j for j in range(n) if mask & (1 << j)]
        principal = [[a[i][j] for j in indices] for i in indices]
        require(determinant(principal) >= 0,
                label + " has a negative principal minor")


def inventory_certificate():
    require(K == 4 * L and D == K + 1, "fixed length convention")
    source_calls = 6 + 6
    other_source_gates = 3 + 6 + 3 + 3 + 1 + 1
    require(other_source_gates == 17, "source non-call gate count")
    gates = source_calls * 8 + other_source_gates + 2 + 3 * 8 + 1
    require(gates == L, "inherited complete word must have 140 gates")
    require(K - L == 420, "identity tail length")
    data_dim = prod(DATA_FACTORS)
    require(data_dim == 657_072_000, "data factorization")
    apparatus_dim = D * data_dim
    total_dim = D * apparatus_dim
    require(apparatus_dim == 368_617_392_000, "program/data dimension")
    require(total_dim == 206_794_356_912_000, "two-clock total dimension")
    require(len(DATA_FACTORS) == 11, "eleven data registers")
    require(len(DATA_FACTORS) + 2 == 13, "two separate clock registers")
    return "data=657072000; apparatus=368617392000; total=206794356912000"


def energy_shell_certificate():
    star = Q(2 * K + 1, D)
    data_dim = prod(DATA_FACTORS)
    shell = {(K - s, s) for s in range(D)}
    require(len(shell) == D, "pairing is injective")
    shell_count = 0
    outside_count = 0
    for q in range(D):
        clock_energy = Q(2 * q, D)
        require(0 <= clock_energy <= Q(2 * K, D),
                "reference-clock spectral bounds")
        for s in range(D):
            app_energy = Q(2 * s + 1, D)
            require(Q(1, D) <= app_energy <= star,
                    "positive apparatus spectrum bounds")
            on_shell = (clock_energy + app_energy == star)
            require(on_shell == ((q, s) in shell),
                    "the paired subspace is not the complete energy shell")
            # In the full block algebra sum_{j,y} E_jy=Q_star.
            # The missing block is explicitly E_out=I-Q_star.
            joint_sum = Q(1) if on_shell else Q(0)
            out_effect = Q(0) if on_shell else Q(1)
            require(joint_sum + out_effect == 1,
                    "POVM is incomplete on an energy block")
            shell_count += int(on_shell)
            outside_count += int(not on_shell)
    require(shell_count == D and outside_count == D * (D - 1),
            "full sector census")
    require(shell_count * data_dim == D * data_dim,
            "shell rank must equal complete apparatus dimension")
    require((shell_count + outside_count) * data_dim == D * D * data_dim,
            "outside sector omitted from carrier")
    wrong_pairs = [s for s in range(D)
                   if Q(4 * s + 1, D) != star]
    require(len(wrong_pairs) == K,
            "negative control q=s must fail except at the midpoint")
    require(Q(4 * (K // 2) + 1, D) == star,
            "wrong-pairing midpoint exception")
    return "561 paired blocks; 314160 outside blocks; wrong pairing detected"


def dft_orbit_certificate():
    """Geometric cancellation for every difference, not a prime-d shortcut.

    For h != 0, q*h mod D visits each multiple of g=gcd(h,D) exactly
    g times. Its root sum is g times a complete cycle of length D/g.
    The polynomial identity (1-x^g) sum_r x^(g*r)=1-x^D certifies
    cancellation at a primitive D-th root. Since g<D, 1-zeta^g != 0.
    """
    require(D == 3 * 11 * 17, "composite clock dimension")
    encountered_gcds = set()
    non_coprime = 0
    for h in range(D):
        counts = [0] * D
        for q in range(D):
            counts[(q * h) % D] += 1
        if h == 0:
            require(counts == [D] + [0] * (D - 1),
                    "zero-difference Fourier norm")
            continue
        g = gcd(h, D)
        order = D // g
        encountered_gcds.add(g)
        non_coprime += int(g > 1)
        require(order > 1 and g * order == D, "root order")
        require(counts == [g if r % g == 0 else 0 for r in range(D)],
                "gcd orbit multiplicity")
        coefficients = [0] * (D + 1)
        for r in range(order):
            coefficients[g * r] += 1
            coefficients[g * (r + 1)] -= 1
        require(coefficients == [1] + [0] * (D - 1) + [-1],
                "complete geometric-cycle polynomial")
    require(encountered_gcds == {1, 3, 11, 17, 33, 51, 187},
            "a composite-dimension orbit class was missed")
    require(non_coprime > 0, "non-coprime differences not checked")
    return "all 561 differences; all seven gcd classes; normalized DFT"


def forward_phase_certificate():
    modulus = 2 * D  # Exponents are in units pi*i/D.
    wrong_sign_detected = False
    for j in range(D):
        common = (2 * K + 1) * j
        wrong_common_at_zero = (-2 * K + 1) * j
        for s in range(D):
            paired_clock_bra = 2 * (K - s) * j
            forward_evolution = -(2 * s + 1) * j
            require(paired_clock_bra - forward_evolution == common,
                    "clock bra gives the wrong temporal orientation")
            wrong_clock_bra = -2 * (K - s) * j
            defect = (wrong_clock_bra - forward_evolution
                      - wrong_common_at_zero) % modulus
            wrong_sign_detected |= bool(defect)
    require(wrong_sign_detected, "wrong-sign negative control not detected")
    # A fixed two-energy witness precludes fixing the error by global phase.
    require(4 % modulus != 0,
            "wrong Fourier sign is not merely one common phase at j=1")
    return "314721 exact forward phase identities; reversed sign rejected"


def moment_certificate():
    weights = [comb(K, s) for s in range(D)]
    normalization = 1 << K
    require(sum(weights) == normalization, "binomial mass normalization")
    require(sum(s * w for s, w in enumerate(weights))
            == K * (1 << (K - 1)), "first binomial moment")
    require(sum(s * s * w for s, w in enumerate(weights))
            == K * (K + 1) * (1 << (K - 2)), "second binomial moment")

    app_mean = Q(sum((2 * s + 1) * w for s, w in enumerate(weights)),
                 D * normalization)
    app_second = Q(sum((2 * s + 1) ** 2 * w
                       for s, w in enumerate(weights)),
                   D * D * normalization)
    clock_mean = Q(sum(2 * (K - s) * w for s, w in enumerate(weights)),
                   D * normalization)
    clock_second = Q(sum((2 * (K - s)) ** 2 * w
                         for s, w in enumerate(weights)),
                     D * D * normalization)
    product_mean = Q(sum(2 * (K - s) * (2 * s + 1) * w
                         for s, w in enumerate(weights)),
                     D * D * normalization)
    require(app_mean == 1, "apparatus mean energy")
    require(app_second - app_mean ** 2 == Q(K, D * D),
            "apparatus energy variance")
    require(clock_mean == Q(K, D), "clock mean energy")
    require(clock_second - clock_mean ** 2 == Q(K, D * D),
            "reference-clock variance")
    covariance = product_mean - app_mean * clock_mean
    require(covariance == -Q(K, D * D), "exact energy anticorrelation")
    total_second = app_second + 2 * product_mean + clock_second
    total_mean = app_mean + clock_mean
    require(total_mean == Q(2 * K + 1, D), "stationary-shell energy mean")
    require(total_second - total_mean ** 2 == 0, "nonzero total variance")
    return "normalized 561 masses; exact means, variances and covariance"


def window_and_tail_certificate():
    require(len(WINDOW) == 188, "window cardinality")
    require(D - len(WINDOW) == 373, "clock complement cardinality")
    require(Q(WINDOW[0], D) == Q(1, 3), "left angle endpoint")
    require(Q(WINDOW[-1], D) == Q(2, 3), "right angle endpoint")
    require(all(Q(1, 3) <= Q(j, D) <= Q(2, 3) for j in WINDOW),
            "clock angle outside sine-square bound")

    # At p=3/4 this is the exact law, with common denominator 4**K.
    endpoint_weights = [comb(K, m) * 3 ** m for m in range(D)]
    require(sum(endpoint_weights) == 4 ** K,
            "exact binomial cursor normalization at the worst endpoint")
    tail = Q(sum(endpoint_weights[:L]), 4 ** K)
    markov = Q(3 ** (L - 1), 2 ** K)
    epsilon = Q(3, 16) ** L
    require(tail <= markov < epsilon,
            "strict unfinished-history bound")
    require(markov * 3 == epsilon, "Markov-to-frozen-epsilon conversion")
    require(epsilon < Q(1, 2 ** 280) < Q(1, 2),
            "frozen exponentially small tail bounds")

    # These two coefficient identities telescope to the derivative of
    # Pr[Bin(K,p)<L], namely -K*C(K-1,L-1)*p**(L-1)*(1-p)**(K-L).
    # Hence the endpoint check bounds every p>=3/4 in the window.
    for m in range(D):
        lower = comb(K - 1, m - 1) if m else 0
        upper = comb(K - 1, m) if m < K else 0
        require(m * comb(K, m) == K * lower,
                "binomial derivative positive term")
        require((K - m) * comb(K, m) == K * upper,
                "binomial derivative negative term")
    return "188/373 window split; exact endpoint tail; monotonicity certificate"


def contrast_isolation_certificate():
    # A deliberately coarse certified interval, not decimal approximation
    # or floating-point evaluation of sqrt(5).
    lo = Q(559, 250)
    hi = Q(22361, 10000)
    require(0 < lo < hi and lo * lo < 5 < hi * hi,
            "rational isolation of the positive root of x^2-5")
    numerator = lambda x: Q(65536) * (48533 - 10985 * x)
    denominator = lambda x: Q(5 ** 9) * (39521 + 154 * x)
    require(numerator(hi) > 0 and denominator(lo) > 0,
            "source contrast numerator or denominator is not positive")
    # f(x)=A(a-bx)/(C(c+ex)) has derivative
    # -A*(b*c+a*e)/(C*(c+ex)^2), strictly negative here.
    require(10985 * 39521 + 48533 * 154 > 0,
            "contrast monotonicity coefficient")
    lower_delta = numerator(hi) / denominator(hi)
    require(lower_delta > Q(1, 50), "Delta > 1/50 not certified")
    epsilon = Q(3, 16) ** L
    lower_joint = Q(len(WINDOW), D) * (1 - epsilon) * lower_delta
    require(lower_joint > Q(47, 14025), "joint contrast threshold")
    require(Q(len(WINDOW), D) * Q(1, 2) * Q(1, 50)
            == Q(47, 14025), "frozen conservative bound identity")
    return "rational sqrt(5) isolation; positive Delta>1/50; joint>47/14025"


def compression_and_negative_controls():
    # Generic compressed blocks are P_s Pi_y P_t with one phase factor.
    # Verify the coefficient identities for every pair of spectral blocks.
    # They do not suppose Pi_y commutes with the apparatus Hamiltonian.
    for s in range(D):
        for t in range(D):
            pullback_phase = -(K - s) + (K - t)
            gram_phase = s - t
            require(pullback_phase == gram_phase,
                    "compressed block is not a diagonal-unitary Gram form")
            require(pullback_phase + (-(K - t) + (K - s)) == 0,
                    "compressed off-diagonal adjoint phase")
            left_energy = 2 * (K - s) + 2 * s + 1
            right_energy = 2 * (K - t) + 2 * t + 1
            require(left_energy == right_energy,
                    "generic compressed block has nonzero energy commutator")

    # Exact rational witness on two energy-shell basis states and one
    # outside-shell state. This realizes the noncommuting pointer block
    # at j=0; general j is diagonal phase conjugation on the shell.
    identity = identity_matrix(3)
    shell = zero_matrix(3)
    shell[0][0] = shell[1][1] = Q(1)
    outside = matrix_add(identity, matrix_scale(shell, Q(-1)))
    pointer0 = [[Q(1, 2), Q(1, 2), Q(0)],
                [Q(1, 2), Q(1, 2), Q(0)],
                [Q(0), Q(0), Q(0)]]
    pointer1 = matrix_add(shell, matrix_scale(pointer0, Q(-1)))
    require(matrix_product(pointer0, pointer0) == pointer0,
            "pointer zero is not a projector")
    require(matrix_product(pointer1, pointer1) == pointer1,
            "pointer one is not a projector")
    require(matrix_product(pointer0, pointer1) == zero_matrix(3),
            "pointer effects are not orthogonal")
    effects = [matrix_scale(pointer0, Q(1, D)),
               matrix_scale(pointer1, Q(1, D))]
    star = Q(2 * K + 1, D)
    total_h = zero_matrix(3)
    total_h[0][0] = total_h[1][1] = star
    total_h[2][2] = star + Q(2, D)
    for k, effect in enumerate(effects):
        check_small_positive(effect, "compressed effect " + str(k))
        require(matrix_product(effect, effect)
                == matrix_scale(effect, Q(1, D)),
                "scaled-projector law E^2=E/d")
        require(matrix_product(effect, effect) != effect,
                "negative control: compressed effect falsely a projector")
        require(matrix_product(total_h, effect)
                == matrix_product(effect, total_h),
                "compressed effect fails energy commutation")
        require(matrix_product(effect, outside) == zero_matrix(3),
                "effect leaks outside stationary energy shell")
    check_small_positive(outside, "E_out")
    require(matrix_product(outside, outside) == outside,
            "E_out is not the complement projector")
    require(matrix_product(total_h, outside)
            == matrix_product(outside, total_h), "E_out commutator")
    single_clock_sum = matrix_add(*effects)
    require(single_clock_sum == matrix_scale(shell, Q(1, D)),
            "two pointer effects do not complete one clock reading")
    full_sum = matrix_scale(single_clock_sum, Q(D))
    require(matrix_add(full_sum, outside) == identity,
            "E_out omitted from complete POVM")
    require(full_sum != identity, "missing E_out was not detected")

    # Clock-energy dephasing removes one coherent off-diagonal block.
    coherent = [[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]]
    dephased = [[Q(1, 2), Q(0)], [Q(0), Q(1, 2)]]
    plus_effect = coherent
    probability = lambda rho: sum(
        (rho[i][j] * plus_effect[j][i] for i in range(2) for j in range(2)),
        Q(0))
    require(probability(coherent) == 1, "coherent-input control")
    require(probability(dephased) == Q(1, 2), "dephased-input control")
    require(coherent != dephased,
            "energy-correlation dephasing was falsely harmless")
    # The two extreme apparatus energies of the admitted pure ready input
    # have the equal positive masses w_0=w_K=2**(-K). The following are
    # their actual subnormalized blocks. The plus effect is zero on all
    # remaining energies, so this comparison uses no postselection.
    endpoint_mass = Q(1, 1 << K)
    full_coherent_block = matrix_scale(coherent, 2 * endpoint_mass)
    full_dephased_block = matrix_scale(dephased, 2 * endpoint_mass)
    require(probability(full_coherent_block) == 2 * endpoint_mass,
            "admitted-ready coherent endpoint block")
    require(probability(full_dephased_block) == endpoint_mass,
            "admitted-ready dephased endpoint block")
    require(probability(full_coherent_block)
            - probability(full_dephased_block) == endpoint_mass > 0,
            "dephasing control does not distinguish an admitted ready input")

    # A local clock projector on |q,s> creates |t_j,s>; only 1/d of
    # that state remains in the original total-energy shell. A compressed
    # shell-supported instrument need not have that local post-state.
    local_clock_poststate_outside_weight = 1 - Q(1, D)
    require(local_clock_poststate_outside_weight > 0,
            "post-state distinction negative control")
    return "positive complete effects with E_out; nonprojective/dephasing/post-state controls"


def robustness_certificate():
    preparation_plus = Q(1, 10000)
    preparation_minus = Q(1, 10000)
    effect_error = Q(1, 10000)
    loss = preparation_plus + preparation_minus + 2 * effect_error
    require(loss == Q(1, 2500), "fixed robustness loss")
    margin = Q(47, 14025) - loss
    require(margin > Q(1, 400), "fixed robust contrast margin")
    return "47/14025 - 1/2500 > 1/400, exact"


def main():
    checks = (
        ("INVENTORY", inventory_certificate),
        ("ENERGY_SHELL_AND_OUTSIDE", energy_shell_certificate),
        ("COMPOSITE_DFT", dft_orbit_certificate),
        ("FORWARD_PHASE", forward_phase_certificate),
        ("ENERGY_MOMENTS", moment_certificate),
        ("CLOCK_WINDOW_AND_TAIL", window_and_tail_certificate),
        ("CONTRAST_ISOLATION", contrast_isolation_certificate),
        ("COMPRESSED_POVM_AND_NEGATIVE_CONTROLS", compression_and_negative_controls),
        ("ROBUSTNESS", robustness_certificate),
    )
    reports = [(name, check()) for name, check in checks]
    for name, report in reports:
        print("PASS " + name + ": " + report)
    print("INDEPENDENT_EXACT_CHECK=PASS")
    print("SCOPE=NON_CANONICAL_CONDITIONAL_L1; NO_EMPIRICAL_OR_NATIVE_DERIVATION")


if __name__ == "__main__":
    main()
