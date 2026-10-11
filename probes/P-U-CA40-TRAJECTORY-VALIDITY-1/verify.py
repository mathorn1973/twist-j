#!/usr/bin/env python3
"""Exact finite audit of trajectory-comparison algebra, not trajectory data.

PUBLIC NON-CANONICAL. Conditional L1. Original code Apache-2.0.
Author: A. M. Thorn. This implementation is independent of the predecessor
waveform verifier; its pulse/carrier conventions are credited model reuse.

All arithmetic is integer or Fraction. Exponential objects are FORMAL jets,
never numerical approximations evaluated at lambda=1. The Taylor/Duhamel
analytic proof must be reviewed separately; fixtures do not prove global
analytic inequalities or the validity of a calcium approximation.

No imports execute checks. No files, network, subprocess, randomness,
floating point, transcendental functions or waveform predictions are used.
CLI has no arguments and writes exactly one ASCII JSON line plus LF.
"""

from fractions import Fraction as F
import itertools
import json
import sys


ORDER = 8
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))


class VerificationError(Exception):
    pass


def need(condition, label):
    if not condition:
        raise VerificationError(label)


def c(real=0, imag=0):
    return (F(real), F(imag))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])


def scale(a, r):
    return (a[0]*r, a[1]*r)


def conj(a):
    return (a[0], -a[1])


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def zeros():
    return [ZERO for _ in range(ORDER + 1)]


def jadd(a, b):
    return [add(x, y) for x, y in zip(a, b)]


def jscale(a, z):
    return [mul(x, z) for x in a]


def jconj(a):
    return [conj(x) for x in a]


def jmul(a, b):
    out = zeros()
    for n in range(ORDER + 1):
        for k in range(n + 1):
            out[n] = add(out[n], mul(a[k], b[n-k]))
    return out


def exp_jet(nu, time):
    return [scale(power(c(0, nu*time), n), F(1, factorial(n)))
            for n in range(ORDER + 1)]


def j_integral(nu, duration):
    out = zeros()
    for n in range(1, ORDER + 1):
        out[n] = scale(power(c(0, nu), n-1),
                       duration**n / factorial(n))
    return out


def k_integral(p, q, duration):
    if q:
        # [J(p)-J(p-q)]/(i*q), including p=q and p=0.
        return jscale(jadd(j_integral(p, duration),
                           jscale(j_integral(p-q, duration), c(-1))),
                      c(0, -F(1, q)))
    out = zeros()
    for n in range(2, ORDER + 1):
        out[n] = scale(power(c(0, p), n-2),
                       duration**n / (factorial(n-2)*n))
    return out


def segment_formula(freq, amps, start, duration, diagonal_only=False):
    """J/K segment formula as a formal lambda jet, through ORDER."""
    shifted = [jscale(exp_jet(nu, start), amp)
               for nu, amp in zip(freq, amps)]
    beta, area = zeros(), zeros()
    for p in range(2):
        beta = jadd(beta, jscale(jmul(shifted[p],
                       j_integral(freq[p], duration)), c(0, -1)))
        for q in range(2):
            if diagonal_only and p != q:
                continue
            term = jmul(jmul(shifted[p], jconj(shifted[q])),
                        k_integral(freq[p], freq[q], duration))
            area = jadd(area, [(z[1], F(0)) for z in term])
    return beta, area


def force_coefficients(freq, amps):
    out = zeros()
    for k in range(ORDER + 1):
        for nu, amp in zip(freq, amps):
            out[k] = add(out[k], scale(mul(amp, power(c(0, nu), k)),
                                      F(1, factorial(k))))
    return out


def monomial_integral(k, lo, hi):
    return (hi**(k+1) - lo**(k+1)) / (k+1)


def segment_triangle(freq, amps, start, duration):
    """Independent direct integration over the ordered time triangle."""
    coeff = force_coefficients(freq, amps)
    end = start + duration
    beta, area = zeros(), zeros()
    for k in range(ORDER):
        beta[k+1] = scale(mul(c(0, -1), coeff[k]),
                          monomial_integral(k, start, end))
        for ell in range(ORDER-k-1):
            triangle = (monomial_integral(k+ell+1, start, end)
                        - start**(ell+1)*monomial_integral(k, start, end))
            triangle /= ell+1
            n = k+ell+2
            area[n] = add(area[n], c(mul(coeff[k], conj(coeff[ell]))[1]
                                       * triangle))
    return beta, area


def append(alpha, phase, beta, area, cross_sign=1):
    cross = jmul(beta, jconj(alpha))
    return jadd(alpha, beta), jadd(jadd(phase, area),
                      [c(cross_sign*z[1]) for z in cross])


def polynomial_integral(poly, lo, hi):
    out = ZERO
    for k, value in enumerate(poly):
        out = add(out, scale(value, monomial_integral(k, lo, hi)))
    return out


def direct_ode(freq, segments):
    """Integrate alpha' and Im(alpha' conjugate(alpha)) as time polynomials.

    Unlike append(), this maintains the integral history inside each force
    interval. No J/K, triangle helper or chronological Weyl helper is used.
    """
    history, phase = zeros(), zeros()
    for start, duration, amps in segments:
        end = start + duration
        coeff = force_coefficients(freq, amps)
        # alpha_j(tau), with actual time t=lambda*tau.
        alpha_polys = [zeros() for _ in range(ORDER + 1)]
        for j in range(1, ORDER + 1):
            constant = sub(history[j-1], scale(coeff[j-1], start**j/j))
            alpha_polys[j][0] = mul(c(0, -1), constant)
            alpha_polys[j][j] = scale(mul(c(0, -1), coeff[j-1]), F(1, j))
        for k in range(ORDER):
            derivative = mul(c(0, -1), coeff[k])
            for j in range(1, ORDER-k):
                poly = zeros()
                for degree in range(ORDER-k+1):
                    poly[degree+k] = mul(derivative, conj(alpha_polys[j][degree]))
                value = polynomial_integral(poly, start, end)
                phase[k+j+1] = add(phase[k+j+1], c(value[1]))
        for k in range(ORDER):
            history[k] = add(history[k], scale(coeff[k],
                                monomial_integral(k, start, end)))
    alpha = zeros()
    for j in range(1, ORDER + 1):
        alpha[j] = mul(c(0, -1), history[j-1])
    return alpha, phase


def check_segments():
    frequencies = ((0, 0), (0, 1), (1, 0), (1, 1), (1, -1), (2, -3))
    amplitudes = ((ONE, I), (ONE, ONE), (c(1, 1), c(1, -2)), (ZERO, ONE))
    single_count, double_count = 0, 0
    start, duration = F(1, 3), F(1, 2)
    for freq, amps in itertools.product(frequencies, amplitudes):
        actual = segment_formula(freq, amps, start, duration)
        need(actual == segment_triangle(freq, amps, start, duration),
             "J/K versus ordered triangle")
        need(actual == direct_ode(freq, ((start, duration, amps),)),
             "J/K versus direct ODE")
        single_count += 1
        amps2 = (neg(amps[1]), add(amps[0], mul(I, amps[1])))
        second = (start+duration, F(2, 3), amps2)
        beta2, phase2 = segment_formula(freq, amps2, second[0], second[1])
        joined = append(actual[0], actual[1], beta2, phase2)
        need(joined == direct_ode(freq, ((start, duration, amps), second)),
             "chronological append versus piecewise ODE")
        double_count += 1

    full = segment_formula((0, 1), (ONE, I), start, duration)
    omitted = segment_formula((0, 1), (ONE, I), start, duration, True)
    need(full != omitted, "omitted two-frequency cross terms were not exposed")
    need(full != segment_formula((0, 1), (ONE, ZERO), start, duration),
         "dropped second frequency was not exposed")
    first, second = zeros(), zeros()
    first[1], second[1] = ONE, I
    correct = append(first, zeros(), second, zeros())
    need(correct[1][2] == ONE, "Weyl orientation")
    need(correct != append(first, zeros(), second, zeros(), -1), "wrong Weyl sign")
    need(correct != append(second, zeros(), first, zeros()), "wrong order")
    freq, amps = (1, -1), (c(1, 1), c(1, -2))
    absolute = segment_formula(freq, amps, start+duration, F(2, 3))
    reset = segment_formula(freq, amps, F(0), F(2, 3))
    need(absolute != reset, "absolute clock reset was not exposed")
    return {"formal_order": ORDER, "single_segments": single_count,
            "two_segment_histories": double_count,
            "numerical_transcendental_values_evaluated": False,
            "negative_controls": ["missing_frequency_cross", "dropped_frequency",
               "wrong_Weyl_sign", "wrong_order", "reset_absolute_clock"]}


def padd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def pscale(a, value):
    return {key: coefficient*value for key, coefficient in a.items()
            if coefficient*value}


def pmul(a, b):
    out = {}
    for (i, j), v in a.items():
        for (k, ell), w in b.items():
            key = (i+k, j+ell)
            out[key] = out.get(key, F(0)) + v*w
    return {key: value for key, value in out.items() if value}


def peval(poly, x, y):
    return sum((coefficient*x**i*y**j
                for (i, j), coefficient in poly.items()), F(0))


def check_moments():
    m, v = {(1, 0): F(1)}, {(0, 1): F(1)}
    moments = [{(0, 0): F(1)}, m]
    for j in range(1, 6):
        moments.append(padd(pmul(m, moments[-1]), pscale(pmul(v, moments[-2]), j)))
    for n in range(7):
        # Coefficient n! [t^n] exp(m*t) exp(v*t^2/2), independently formed.
        mgf = {(n-2*j, j): F(factorial(n), factorial(n-2*j)*factorial(j)*2**j)
               for j in range(n//2+1)}
        need(moments[n] == mgf, "Gaussian recurrence versus generating function")
    expected4 = {(4, 0): F(1), (2, 1): F(6), (0, 2): F(3)}
    expected6 = {(6, 0): F(1), (4, 1): F(15), (2, 2): F(45), (0, 3): F(15)}
    need(moments[4] == expected4 and moments[6] == expected6, "displayed moments")
    count = 0
    for mean, variance in itertools.product((F(-2), F(-1, 2), F(0), F(1, 3), F(3)),
                                            (F(0), F(1, 4), F(1), F(5, 2))):
        for n in (2, 4, 6):
            need(peval(moments[n], mean, variance) >= 0, "even moment nonnegative")
            need(peval(moments[n], mean, variance) == peval(moments[n], -mean, variance),
                 "even moment reflection")
        count += 1
    wrong6 = dict(expected6)
    wrong6[(2, 2)] = F(44)
    need(peval(wrong6, F(1), F(1)) != peval(expected6, F(1), F(1)), "wrong M6 coefficient")
    need(peval(expected4, F(0), F(1)) != peval(expected4, F(0), F(0)), "vacuum variance lost")
    need(peval(expected6, F(1), F(1)) != peval(expected6, F(0), F(1)), "displacement mean lost")
    return {"polynomial_orders": list(range(7)), "rational_mean_variance_fixtures": count,
            "negative_controls": ["wrong_M6_coefficient", "lost_vacuum_variance", "lost_mean"]}


def check_majorants():
    q4 = {(2, 0): F(1), (0, 2): F(3)}
    q6 = {(3, 0): F(1), (1, 2): F(8), (0, 3): F(4)}
    moment4 = {(4, 0): F(1), (2, 2): F(6), (0, 4): F(3)}
    moment6 = {(6, 0): F(1), (4, 2): F(15), (2, 4): F(45), (0, 6): F(15)}
    difference4 = padd(pmul(q4, q4), pscale(moment4, -1))
    difference6 = padd(pmul(q6, q6), pscale(moment6, -1))
    need(difference4 == {(0, 4): F(6)}, "quartic majorant")
    need(difference6 == {(4, 2): F(1), (3, 3): F(8), (2, 4): F(19),
                         (1, 5): F(64), (0, 6): F(1)}, "sixth majorant")
    need(all(value >= 0 for value in difference6.values()), "majorant coefficient sign")
    # chi=pi/2: cos(X)-1 has a nonzero quadratic coefficient. It is not O(X^3).
    cosine_minus_one_x2 = -F(1, factorial(2))
    need(cosine_minus_one_x2 != 0, "generic cubic-only remainder overclaim")
    # Endpoint samples are not a continuous-time envelope.
    bump = lambda t: t*t*(1-t)*(1-t)
    need(bump(F(0)) == bump(F(1)) == 0 and bump(F(1, 2)) == F(1, 16),
         "endpoint-only envelope overclaim")
    budget = F(1, 100)
    envelope_integrals = [sum((dt*bound for dt, bound in segments), F(0))
                          for segments in (((F(1, 2), F(1, 100)),),
                                           ((F(1, 2), F(1, 50)),),
                                           ((F(1, 2), F(3, 100)),))]
    need([value <= budget for value in envelope_integrals] == [True, True, False],
         "declared sufficient-budget comparison")
    return {"exact_polynomial_majorants": 2, "rational_LD_budget_fixture": [1, 100],
            "budget_fixture_outcomes": [True, True, False],
            "analytic_Duhamel_theorem_proved_by_fixtures": False,
            "negative_controls": ["generic_cubic_only_remainder", "endpoint_only_envelope"]}


def rotate(label, phase, other, quarter_turns):
    if label == 0:
        return other, (phase + quarter_turns - 1) % 4
    if label == other:
        return 0, (phase - quarter_turns - 1) % 4
    return label, phase


def cycle(label, phase=0):
    for other, angle in ((1, 1), (2, -1), (3, 1), (4, -1)):
        label, phase = rotate(label, phase, other, angle)
    return label, phase


def check_factorization():
    for label in range(6):
        need(cycle(label) == ((label+1) % 5 if label < 5 else 5, 0), "literal X5")
        value, phase = label, 0
        for _ in range(5):
            value, phase = cycle(value, phase)
        need((value, phase) == (label, 0), "X5 fifth power")
        value, phase = rotate(label, 0, 5, 1)
        need(rotate(value, phase, 5, -1) == (label, 0), "shelf adjoint all columns")
    for label in range(5):
        hidden, phase = rotate(label, 0, 5, 1)
        need(hidden != 0, "protected zero force response")
        need(rotate(hidden, phase, 5, -1) == (label, 0), "protected endpoint")
    count = 0
    for left, right in itertools.product(range(5), repeat=2):
        a, b, pa, pb, hits_a, hits_b, simultaneous = left, right, 0, 0, 0, 0, 0
        for _ in range(5):
            hits_a += int(a == 0)
            hits_b += int(b == 0)
            simultaneous += int(a == b == 0)
            a, pa = cycle(a, pa)
            b, pb = cycle(b, pb)
            count += 1
        need((a, b, pa, pb) == (left, right, 0, 0), "active pair endpoint")
        need(hits_a == hits_b == 1 and simultaneous == int(left == right),
             "active response incidence")
    hidden, phase = rotate(1, 0, 5, 1)
    exposed = 0
    for _ in range(5):
        exposed += int(hidden == 0)
        hidden, phase = cycle(hidden, phase)
    need(exposed == 1, "global spectator echo exposure")
    value, phase = 0, 0
    for _ in range(4):
        value, phase = cycle(value, phase)
    need((value, phase) != (0, 0), "missing cycle")
    value, phase = rotate(0, 0, 5, 1)
    need(rotate(value, phase, 5, 1) == (0, 2), "wrong unhide phase")
    perturbed_responses = [F(1, 10) if label == 2 else F(0) for label in range(5)]
    need(len(set(perturbed_responses)) > 1, "nonzero protected response breaks reduction")

    # Exactly periodic optical clock, not a floating assertion about exp(2*pi*i*n).
    need(F(1020000)*F(1, 10000) == 102, "integer optical periods per loop")
    phase_cases = 0
    for integral_left, integral_right in ((F(1, 7), F(-2, 9)), (F(3, 11), F(5, 13))):
        reference = -2*(integral_left + integral_right)
        for left, right in itertools.product(range(5), repeat=2):
            total = F(0)
            for loop in range(5):
                total -= 2*(int((left+loop) % 5 == 0)*integral_left
                            + int((right+loop) % 5 == 0)*integral_right)
            need(total == reference, "periodic uncompensated endpoint common phase")
            phase_cases += 1
    # A quarter-turn loop advance, with the same repeated envelope, breaks it.
    nonperiodic = {power(I, (-left) % 5)[1] + power(I, (-right) % 5)[1]
                   for left, right in itertools.product(range(5), repeat=2)}
    need(len(nonperiodic) > 1, "noninteger-period common-phase overclaim")
    return {"local_columns": 6, "fifth_power_columns": 6, "shelf_adjoint_columns": 6,
            "protected_code_columns": 5, "active_pairs": 25, "active_cycle_response_pairs": count,
            "optical_periods_per_loop": 102, "endpoint_common_phase_fixtures": phase_cases,
            "full_electronic_dimension_covered_by_conditional_factorization": 5**7,
            "protected_factorization_requires_zero_response_and_ideal_carriers": True,
            "negative_controls": ["global_echo", "missing_cycle", "wrong_unhide",
                                  "nonzero_protected_response", "noninteger_loop_period"]}


def run_checks():
    return {"status": "PASS", "scope": "finite_exact_trajectory_comparison_algebra_only",
            "two_frequency": check_segments(), "Gaussian_moments": check_moments(),
            "remainder_majorants": check_majorants(), "factorization": check_factorization(),
            "trajectory_numerics_verified": False, "continuous_time_certificate": False,
            "hardware_admission": False}


def main():
    need(len(sys.argv) == 1, "this exact verifier accepts no arguments")
    result = run_checks()
    sys.stdout.buffer.write((json.dumps(result, sort_keys=True, separators=(",", ":"))
                             + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
