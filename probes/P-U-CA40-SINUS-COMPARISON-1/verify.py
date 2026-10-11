#!/usr/bin/env python3
"""Exact finite algebra for the conditional sinus-comparison probe.

PUBLIC NON-CANONICAL. L1. Original code Apache-2.0; A. M. Thorn.
Fraction-pair arithmetic follows the preceding trajectory audit's utility
pattern. The thermal, projected-displacement and restored-overlap fixtures
are new independent finite checks. They are not a floating solver oracle.

Unnormalized Fock vectors use |n>_u=(a^dagger)^n|0> and metric n!.
The universal Gaussian prefactor of D(beta) is kept formal, not evaluated.
No checks execute on import; no files, networking or subprocesses are used.
"""

from fractions import Fraction as F
import itertools
import json
from math import comb, factorial
import sys


Z = (F(0), F(0))
O = (F(1), F(0))
I = (F(0), F(1))


def need(ok, label):
    if not ok:
        raise RuntimeError(label)


def c(a=0, b=0):
    return (F(a), F(b))


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[0], -a[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def conj(a):
    return (a[0], -a[1])


def scale(a, value):
    return (a[0]*value, a[1]*value)


def power(a, n):
    value = O
    for _ in range(n):
        value = mul(value, a)
    return value


def abs2(a):
    return a[0]*a[0]+a[1]*a[1]


def product(items):
    value = 1
    for item in items:
        value *= item
    return value


def compositions(total, modes):
    if modes == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, modes-1):
                yield (first,)+rest


def basis(modes, cutoff):
    return tuple(n for total in range(cutoff+1) for n in compositions(total, modes))


def metric(n):
    return product(factorial(k) for k in n)


def vadd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = add(out.get(key, Z), value)
    return {key: value for key, value in out.items() if value != Z}


def vscale(a, value):
    return {key: scale(z, value) for key, z in a.items() if scale(z, value) != Z}


def inner(a, b):
    value = Z
    for n, z in a.items():
        value = add(value, scale(mul(conj(z), b.get(n, Z)), metric(n)))
    return value


def norm2(a):
    value = inner(a, a)
    need(value[1] == 0 and value[0] >= 0, "Fock metric positivity")
    return value[0]


def ladder(vector, coefficients, raising, cutoff):
    out = {}
    for n, value in vector.items():
        for mode, coefficient in enumerate(coefficients):
            target = list(n)
            if raising:
                target[mode] += 1
                factor = 1
            else:
                if n[mode] == 0:
                    continue
                target[mode] -= 1
                factor = n[mode]
            target = tuple(target)
            if sum(target) <= cutoff:
                increment = scale(mul(coefficient, value), factor)
                out[target] = add(out.get(target, Z), increment)
    return {n: z for n, z in out.items() if z != Z}


def nilpotent_exponential(vector, coefficients, raising, cutoff):
    out, term = dict(vector), dict(vector)
    for degree in range(1, cutoff+1):
        term = vscale(ladder(term, coefficients, raising, cutoff), F(1, degree))
        out = vadd(out, term)
    return out


def normal_order_action(vector, beta, cutoff):
    lower = tuple(neg(conj(z)) for z in beta)
    state = nilpotent_exponential(vector, lower, False, cutoff)
    return nilpotent_exponential(state, beta, True, cutoff)


def direct_coefficient(target, initial, beta):
    """Independent finite multinomial formula; Gaussian prefactor omitted."""
    total = Z
    for intermediate in itertools.product(*(range(min(m, n)+1) for m, n in zip(target, initial))):
        value = O
        for m, n, k, displacement in zip(target, initial, intermediate, beta):
            term = mul(power(neg(conj(displacement)), n-k), power(displacement, m-k))
            term = scale(term, F(comb(n, k), factorial(m-k)))
            value = mul(value, term)
        total = add(total, value)
    return total


def check_displacements():
    fixtures = (((c(F(1, 3), F(1, 4)),), 4),
                ((c(F(1, 3), F(1, 4)), c(F(-1, 5), F(1, 7))), 3),
                ((c(F(1, 3), F(1, 4)), c(F(-1, 5)), c(F(1, 7), F(-1, 8))), 3))
    columns, entries = 0, 0
    for beta, cutoff in fixtures:
        states = basis(len(beta), cutoff)
        negative = tuple(neg(z) for z in beta)
        for initial in states:
            actual = normal_order_action({initial: O}, beta, cutoff)
            ambient = normal_order_action({initial: O}, beta, 2*cutoff)
            ambient = {n: z for n, z in ambient.items() if sum(n) <= cutoff}
            need(actual == ambient, "Normal-order projection changed through larger carrier")
            for target in states:
                expected = direct_coefficient(target, initial, beta)
                need(actual.get(target, Z) == expected, "Projected displacement coefficient")
                reverse = direct_coefficient(initial, target, negative)
                need(scale(expected, metric(target)) == scale(conj(reverse), metric(initial)),
                     "Weighted adjoint D(beta)^dagger=D(-beta)")
                entries += 1
            columns += 1
        zero_beta = tuple(Z for _ in beta)
        need(normal_order_action({states[-1]: O}, zero_beta, cutoff) == {states[-1]: O},
             "Zero displacement")
    # At L=0, exp(i P X P)=I but P exp(i lambda X)P has nonzero lambda^2 term.
    beta = (c(F(1, 3)), c(0, F(1, 4)))
    full_vacuum_lambda2 = -sum((abs2(z) for z in beta), F(0))/2
    need(full_vacuum_lambda2 != 0, "Exponentiating projected X overclaim not exposed")
    return {"fixture_modes": [1, 2, 3], "columns": columns, "matrix_entries": entries,
            "Gaussian_prefactor": "formal_common_exp_minus_norm_beta_squared_over_two",
            "actual_transcendental_displacements_evaluated": False,
            "projected_exponential_overclaim_exposed": True}


def check_boundary():
    beta = (c(F(1, 3), F(1, 5)), c(F(-2, 7), F(1, 11)))
    count = 0
    for cutoff in (1, 2, 3):
        shell = {n: c(F(index+1, 7), F(1-index, 13))
                 for index, n in enumerate(compositions(cutoff, 2))}
        raising = ladder(shell, beta, True, cutoff+1)
        lowering = ladder(shell, tuple(conj(z) for z in beta), False, cutoff)
        vacuum_term = sum((abs2(z) for z in beta), F(0))*norm2(shell)
        need(norm2(raising) == vacuum_term+norm2(lowering), "QX shell norm identity")
        need(norm2(raising) != vacuum_term, "Boundary lowering term omission not exposed")
        general = vadd(shell, {(0, 0): c(F(2, 9))})
        full_x = vadd(ladder(general, beta, True, cutoff+1),
                      ladder(general, tuple(conj(z) for z in beta), False, cutoff+1))
        outside = {n: z for n, z in full_x.items() if sum(n) > cutoff}
        need(outside == raising, "Only highest shell contributes to QXP")
        count += 1
    # Generic finite unitary leakage identity, independently of oscillator exponentials.
    inside, outside = F(3, 5), F(4, 5)
    need(inside*inside+outside*outside == 1 and 1-inside*inside == outside*outside,
         "Unitary projected leakage norm")
    return {"boundary_shell_fixtures": count, "unitary_leakage_squared": [16, 25],
            "continuous_projection_residual_certified": False}


def check_thermal():
    ratio = F(1, 21)
    rows = []
    for cutoff in range(4):
        states = basis(7, cutoff)
        need(len(states) == comb(cutoff+7, 7), "Total-excitation dimension")
        enumerated = sum(((1-ratio)**7*ratio**sum(n) for n in states), F(0))
        grouped = (1-ratio)**7*sum((comb(j+6, 6)*ratio**j for j in range(cutoff+1)), F(0))
        need(enumerated == grouped, "Thermal degeneracy versus explicit occupations")
        tail = 1-grouped
        need(0 < tail < 1, "Thermal omitted mass")
        rows.append({"cutoff": cutoff, "columns": len(states),
                     "retained_mass": [grouped.numerator, grouped.denominator],
                     "omitted_mass": [tail.numerator, tail.denominator]})
    need(rows[3]["columns"] == 120, "Thermal reference count")
    tail3 = F(*rows[3]["omitted_mass"])
    need(tail3 < F(9, 10000), "K3 thermal tail bound")
    # The actual lane uses K3 only; smaller cutoffs audit exact combinatorics.
    retained = 1-tail3
    for tail_value in (O, neg(O), I, c(F(3, 5), F(4, 5))):
        full = add(c(retained), scale(tail_value, tail3))
        difference = add(full, c(-retained))
        need(abs2(difference) <= tail3*tail3, "Unnormalized omitted-tail complex disc")
    need(retained+tail3 == 1 and retained != 1, "Missing retained-mass restoration")
    # If all retained coherences equal 1, the identity tail gives D=0 and the
    # negative tail gives D=tail3. The center tail3/2 alone is not a witness.
    need(abs((retained+tail3)-1)/2 == 0, "Identity tail")
    need(abs((retained-tail3)-1)/2 == tail3, "Opposite tail")
    states = basis(7, 3)
    weighted_vacuum = (1-ratio)**7
    need(weighted_vacuum/retained != F(1, len(states)), "Uniform thermal-weight mutant")
    return {"reference_cutoffs": rows, "campaign_cutoff": 3,
            "unnormalized_weights_retained": True,
            "generic_two_channel_conditioning_allowance": [2*tail3.numerator, tail3.denominator],
            "pair_witness_thermal_radius": [tail3.numerator, 2*tail3.denominator],
            "negative_controls": ["uniform_weights", "missing_retained_mass", "tail_center_as_witness"]}


def matmul(a, b):
    return [[sum_complex(mul(a[i][k], b[k][j]) for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def sum_complex(values):
    out = Z
    for value in values:
        out = add(out, value)
    return out


def adjoint(a):
    return [[conj(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]


def check_frames():
    identity = [[O, Z], [Z, O]]
    ua = identity
    ub = [[c(F(3, 5)), c(F(4, 5))], [c(F(-4, 5)), c(F(3, 5))]]
    need(matmul(adjoint(ub), ub) == identity, "Rational frame unitarity")
    wa = [[I, Z], [Z, neg(I)]]
    wb = [[Z, O], [O, Z]]
    physical = matmul(adjoint(matmul(ub, wb)), matmul(ua, wa))
    restored = matmul(matmul(adjoint(wb), matmul(adjoint(ub), ua)), wa)
    need(physical == restored, "Restored U_L frame overlap identity")
    raw = matmul(adjoint(wb), wa)
    need(raw != restored, "Raw moving-frame overlap mutant")
    # With W_a=W_b=I, nonlinear and linear are the SAME physical evolution.
    linear = matmul(adjoint(ub), ua)
    need(linear[0][0] == c(F(3, 5)) and identity[0][0] != linear[0][0],
         "False difference caused by dropping relative U_L")
    phase_ua = [[I, Z], [Z, I]]
    phase_wa = [[neg(I), Z], [Z, neg(I)]]
    need(matmul(phase_ua, phase_wa) == identity, "Branch-frame rephasing cancellation")
    return {"restored_overlap_identity": True, "branch_frame_gauge_identity": True,
            "raw_W_overlap_overclaim_exposed": True,
            "purified_overlap_is_Uhlmann_fidelity": False}


def check_source_factor():
    # A finite IP tensor V fixture; dark electronic responses are an explicit premise.
    def joint(state):
        p, a, b = state
        return p, a, b ^ a

    checked = 0
    for state in itertools.product(range(5), range(2), range(2)):
        for shift, phase_power in itertools.product(range(5), repeat=2):
            p, a, b = state
            shifted = ((p+shift) % 5, a, b)
            left = joint(shifted)
            jp, ja, jb = joint(state)
            right = ((jp+shift) % 5, ja, jb)
            need(left == right and phase_power*p % 5 == phase_power*jp % 5,
                 "Full source Weyl algebra commutation")
            checked += 1
    return {"Weyl_commutation_columns": checked,
            "physical_spectator_darkness_verified": False,
            "factorization_is_conditional_on_zero_electronic_response": True}


def run_checks():
    return {"status": "PASS", "scope": "finite_exact_truncation_and_frame_algebra_only",
            "thermal": check_thermal(), "projected_displacement": check_displacements(),
            "boundary": check_boundary(), "frame_overlap": check_frames(),
            "protected_source": check_source_factor(), "trajectory_numerics_verified": False,
            "dynamic_cutoff_certificate": False, "time_integration_certificate": False,
            "hardware_admission": False}


def main():
    need(len(sys.argv) == 1, "No verifier arguments accepted")
    sys.stdout.buffer.write((json.dumps(run_checks(), sort_keys=True, separators=(",", ":"))
                             + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
