#!/usr/bin/env python3
"""Exact algebra supporting, but not replacing, a trajectory certificate.

PUBLIC NON-CANONICAL. Conditional L1. Apache-2.0, A. M. Thorn.
Fraction/Fock helpers adapt the public SINUS-COMPARISON-1 verifier.
New checks audit guard tails, defect reconstruction, Gauss norm identities
and error-budget semantics. No actual numerical trajectory is read here.
No execution on import, dependencies, filesystem, networking or subprocesses.
"""
from fractions import Fraction as F
import itertools
import json
from math import comb, factorial, isqrt
import sys


Z = (F(0), F(0))
O = (F(1), F(0))


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def c(a=0, b=0):
    return (F(a), F(b))


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[0], -a[1])


def conj(a):
    return (a[0], -a[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def scale(a, s):
    return (a[0]*s, a[1]*s)


def power(a, n):
    out = O
    for _ in range(n):
        out = mul(out, a)
    return out


def abs2(a):
    return a[0]*a[0]+a[1]*a[1]


def product(values):
    out = 1
    for value in values:
        out *= value
    return out


def compositions(total, modes):
    if modes == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for tail in compositions(total-first, modes-1):
                yield (first,)+tail


def basis(modes, cutoff):
    return tuple(n for j in range(cutoff+1) for n in compositions(j, modes))


def norm2(v):
    return sum((product(factorial(x) for x in n)*abs2(z)
                for n, z in v.items()), F(0))


def vadd(a, b):
    out = dict(a)
    for n, z in b.items():
        out[n] = add(out.get(n, Z), z)
    return {n: z for n, z in out.items() if z != Z}


def vscale(v, s):
    return {n: scale(z, s) for n, z in v.items() if scale(z, s) != Z}


def ladder(v, beta, raising, cutoff):
    out = {}
    for n, z in v.items():
        for mode, coefficient in enumerate(beta):
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
                out[target] = add(out.get(target, Z),
                                  scale(mul(coefficient, z), factor))
    return {n: z for n, z in out.items() if z != Z}


def exp_ladder(v, beta, raising, cutoff):
    out, term = dict(v), dict(v)
    for k in range(1, cutoff+1):
        term = vscale(ladder(term, beta, raising, cutoff), F(1, k))
        out = vadd(out, term)
    return out


def normal_action(v, beta, guard):
    lowered = exp_ladder(v, tuple(neg(conj(z)) for z in beta), False, guard)
    return exp_ladder(lowered, beta, True, guard)


def direct_coefficient(m, n, beta):
    out = Z
    for middle in itertools.product(*(range(min(a, b)+1) for a, b in zip(m, n))):
        term = O
        for a, b, j, z in zip(m, n, middle, beta):
            term = mul(term, scale(mul(power(z, a-j), power(neg(conj(z)), b-j)),
                                   F(comb(b, j), factorial(a-j))))
        out = add(out, term)
    return out


def upper_sqrt(x, bits=32):
    need(x >= 0 and bits >= 1, "sqrt domain")
    denominator = 1 << bits
    floor = isqrt((x.numerator*denominator*denominator)//x.denominator)
    if floor*floor*x.denominator != x.numerator*denominator*denominator:
        floor += 1
    out = F(floor, denominator)
    need(out*out >= x and (out == 0 or (out-F(1, denominator))**2 < x),
         "outward rational square root")
    return out


def check_guard():
    beta = (c(F(1, 7), F(1, 11)), c(F(-1, 13), F(1, 17)))
    columns = entries = 0
    for cutoff, guard in ((2, 4), (3, 5)):
        for initial in basis(2, cutoff):
            actual = normal_action({initial: O}, beta, guard)
            ambient = normal_action({initial: O}, beta, guard+2)
            need(actual == {n: z for n, z in ambient.items() if sum(n) <= guard},
                 "guard projection changed finite normal-order coefficient")
            for target in basis(2, guard):
                need(actual.get(target, Z) == direct_coefficient(target, initial, beta),
                     "guard normal order versus independent coefficients")
                entries += 1
            columns += 1
    shell_checks = 0
    b2 = sum((abs2(z) for z in beta), F(0))
    for j in range(5):
        shell = {n: c(F(k+1, 9), F(2-k, 19))
                 for k, n in enumerate(compositions(j, 2))}
        state = dict(shell)
        for k in range(1, 6):
            state = ladder(state, beta, True, j+k)
            bound_squared = b2**k*F(factorial(j+k), factorial(j))*norm2(shell)
            need(norm2(state) <= bound_squared, "shell creation bound")
            aligned = {(j, 0): O}
            for _ in range(k):
                aligned = ladder(aligned, (c(F(1, 4)), Z), True, j+k)
            need(norm2(aligned) == F(1, 16)**k*factorial(j+k),
                 "aligned one-mode shell saturates factorial bound")
            shell_checks += 1
    ratio_checks = 0
    for cutoff in range(3, 9):
        for extra in (2, 3, 4):
            guard = cutoff+extra
            for j in range(cutoff+1):
                first = guard-j+1
                b2 = F(1, 16)
                q2 = b2*F(j+first+1, (first+1)**2)
                q_upper = upper_sqrt(q2)
                need(q_upper < 1, "geometric denominator must be positive")
                term2 = b2**first*F(factorial(j+first),
                                     factorial(j)*factorial(first)**2)
                first_upper = upper_sqrt(term2)
                tail_upper = first_upper/(1-q_upper)
                need(tail_upper >= first_upper, "positive geometric tail")
                for k in range(first, first+8):
                    current = b2*F(j+k+1, (k+1)**2)
                    following = b2*F(j+k+2, (k+2)**2)
                    need(following <= current <= q_upper*q_upper,
                         "tail ratios must decrease")
                need(sum((q_upper**k for k in range(12)), F(0)) <= 1/(1-q_upper),
                     "finite geometric prefix bounded by infinite series")
                ratio_checks += 1
    need(F(1, 2) < 1 and 1/(1+F(1, 2)) < 1+F(1, 2),
         "wrong geometric denominator negative control")
    # A finite guard is never a proof that the creation tail vanishes.
    highest = ladder({(4,): O}, (c(F(1, 4)),), True, 5)
    need(norm2(highest) > 0, "omitted-shell negative control")
    return {"columns": columns, "matrix_entries": entries,
            "shell_power_fixtures": shell_checks, "ratio_fixtures": ratio_checks,
            "Gaussian_prefactor": "formal_not_numerically_evaluated",
            "actual_time_dependent_guard_tail_certified": False}


def padd(a, b):
    out = [F(0)]*max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def pmul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def peval(p, x):
    out = F(0)
    for coefficient in reversed(p):
        out = out*x+coefficient
    return out


def pderivative(p):
    return [i*p[i] for i in range(1, len(p))]


def check_defect():
    h = F(1, 8)
    y0 = F(7, 6)
    stages = (F(2, 3), F(-1, 7), F(3, 11), F(5, 13))
    dense_weights = ((0, 1, F(-3, 2), F(2, 3)),
                     (0, 0, 1, F(-2, 3)),
                     (0, 0, 1, F(-2, 3)),
                     (0, 0, F(-1, 2), F(2, 3)))
    polynomial = [y0]
    for stage, weight in zip(stages, dense_weights):
        polynomial = padd(polynomial, [h*stage*x for x in weight])
    endpoint = y0+h*(stages[0]+2*stages[1]+2*stages[2]+stages[3])/6
    need(peval(polynomial, F(0)) == y0 and peval(polynomial, F(1)) == endpoint,
         "RK dense reconstruction endpoints")
    jump = F(1, 1 << 30)
    recorded_endpoint = endpoint+jump
    corrected = padd(polynomial, [F(0), jump])
    need(peval(corrected, F(1)) == recorded_endpoint, "stored endpoint correction")
    derivative_delta = padd(pderivative(corrected), [-x for x in pderivative(polynomial)])
    need(derivative_delta[0]/h == jump/h and all(x == 0 for x in derivative_delta[1:]),
         "endpoint correction must enter time derivative")
    need(recorded_endpoint != endpoint, "dropping FP update jump negative control")
    # The current candidate uses quintic Hermite reconstruction. Its exact
    # construction identities do not assert accuracy of approximate slopes.
    y1, f0, f1, a0, a1 = F(9, 8), F(2, 5), F(-1, 3), F(4, 7), F(-2, 11)
    c0, c1, c2 = y0, h*f0, h*h*a0/2
    aa, bb, cc = y1-c0-c1-c2, h*f1-c1-2*c2, h*h*a1-2*c2
    quintic = [c0, c1, c2, 10*aa-4*bb+cc/2,
               -15*aa+7*bb-cc, 6*aa-3*bb+cc/2]
    first_derivative = pderivative(quintic)
    second_derivative = pderivative(first_derivative)
    need(peval(quintic, F(0)) == y0 and peval(quintic, F(1)) == y1,
         "quintic Hermite endpoint values")
    need(peval(first_derivative, F(0))/h == f0 and peval(first_derivative, F(1))/h == f1,
         "quintic Hermite endpoint slopes")
    need(peval(second_derivative, F(0))/(h*h) == a0
         and peval(second_derivative, F(1))/(h*h) == a1,
         "quintic Hermite endpoint second derivatives")
    # H=0: sampled defects at 0,1/2,1 vanish, yet endpoint error is nonzero.
    derivative = pmul(pmul([0, 0, 1], pmul([F(-1, 2), 1], [F(-1, 2), 1])),
                      pmul([-1, 1], [-1, 1]))
    need(all(peval(derivative, x) == 0 for x in (F(0), F(1, 2), F(1))),
         "sampling falsifier nodes")
    endpoint_error = sum((a/F(i+1) for i, a in enumerate(derivative)), F(0))
    need(endpoint_error == F(1, 840) > F(1, 1000), "sampling misses integrated defect")
    defect = (c(F(1, 7), F(2, 11)), c(F(-1, 5), F(1, 13)), c(F(3, 17)))
    total = sum((abs2(z) for z in defect), F(0))
    inside = sum((abs2(z) for z in defect[:2]), F(0))
    outside = abs2(defect[2])
    need(total == inside+outside and total > inside, "orthogonal guard defect decomposition")
    return {"dense_endpoint_correction": True, "quintic_Hermite_endpoint_identities": True,
            "orthogonal_defect_identity": True,
            "zero_sampled_defect_nonzero_endpoint_error": [1, 840],
            "continuous_defect_integral_certified": False}


# Exact real quadratic field Q(sqrt(15)); Gauss nodes are algebraic, not FP.
def qmul(a, b):
    return (a[0]*b[0]+15*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def qeval(p, x):
    out = Z
    for coefficient in reversed(p):
        out = add(qmul(out, x), c(coefficient))
    return out


def integral_average(p):
    return sum((coefficient/F(i+1) for i, coefficient in enumerate(p) if i % 2 == 0), F(0))


def check_gauss():
    nodes = (c(0, F(-1, 5)), Z, c(0, F(1, 5)))
    weights = (F(5, 18), F(4, 9), F(5, 18))
    need(all(w > 0 for w in weights) and sum(weights) == 1, "positive normalized weights")
    for degree in range(6):
        polynomial = [F(0)]*degree+[F(1)]
        quadrature = Z
        for x, w in zip(nodes, weights):
            quadrature = add(quadrature, scale(qeval(polynomial, x), w))
        need(quadrature == c(integral_average(polynomial)), "Gauss exact moment")
    vector_polynomials = ([F(2, 7), F(-1, 3), F(4, 11)],
                          [F(-1, 5), F(3, 13), F(2, 9)])
    norm_square = [F(0)]
    quadrature = Z
    for polynomial in vector_polynomials:
        norm_square = padd(norm_square, pmul(polynomial, polynomial))
        for x, w in zip(nodes, weights):
            value = qeval(polynomial, x)
            quadrature = add(quadrature, scale(qmul(value, value), w))
    need(quadrature == c(integral_average(norm_square)), "Gauss vector-polynomial L2 identity")
    # Any interpolation residual with node norm <= E obeys weighted L2 <= E.
    error_bound = F(3, 8)
    errors2 = (error_bound**2, error_bound**2/F(4), F(0))
    need(sum(w*x for w, x in zip(weights, errors2)) <= error_bound**2,
         "positive-weight interpolation stability")
    rho, majorant, degree = F(2), F(7, 3), 4
    chebyshev_error = 2*majorant*rho**(-degree)/(rho-1)
    need(2*chebyshev_error == 4*majorant*rho**(-degree)/(rho-1),
         "two interpolation errors in quadrature remainder")
    need(sum(w*x for w, x in zip((F(-1), F(3), F(-1)), (F(0), F(1), F(0)))) > 1,
         "negative-weight shortcut falsifier")
    need(F(1) != integral_average([0, 0, 1]), "endpoint trapezoid is not Gauss degree-two rule")
    return {"exact_algebraic_rule_nodes": 3, "exact_moments": 6,
            "vector_polynomial_L2_identity": True,
            "actual_certificate_nodes_weights_or_ellipse_bound_verified": False}


def decision(center, radius, threshold):
    need(radius >= 0, "nonnegative total radius")
    lo, hi = max(F(0), center-radius), min(F(1), center+radius)
    if hi <= threshold:
        return "WITHIN_TARGET"
    if lo > threshold:
        return "EXCEEDS_TARGET"
    return "UNRESOLVED"


def check_budget():
    ratio = F(1, 21)
    states = basis(7, 3)
    weights = [(1-ratio)**7*ratio**sum(n) for n in states]
    retained = sum(weights, F(0))
    grouped = (1-ratio)**7*sum((comb(j+6, 6)*ratio**j for j in range(4)), F(0))
    tail = 1-retained
    need(len(states) == 120 and retained == grouped, "exact retained thermal mass")
    need(tail == F(680046581, 794280046581), "thermal tail provenance")
    # Unnormalized endpoints: e_a+e_b alone is insufficient.
    approximate_a = approximate_b = F(6, 5)
    error_a = error_b = F(1, 5)
    gram_error = approximate_a*approximate_b-1
    safe = min(error_a+approximate_a*error_b, error_b+approximate_b*error_a)
    need(gram_error == safe == F(11, 25) and gram_error > error_a+error_b,
         "nonnormalized Gram-error falsifier")
    weighted_error = sum((w*safe for w in weights), F(0))
    need(weighted_error == retained*safe, "thermal weights have no rank multiplier")
    # These are budget toys, not predictions of the two physical angle cases.
    threshold = F(1, 1000)
    radius = tail/2+F(1, 10000)
    need(decision(F(1, 25), radius, threshold) == "EXCEEDS_TARGET", "positive-sign toy")
    need(decision(F(1, 40), radius, threshold) == "EXCEEDS_TARGET", "negative-sign toy")
    need(decision(F(0), radius, threshold) == "WITHIN_TARGET", "positive acceptance toy")
    need(decision(threshold, radius, threshold) == "UNRESOLVED", "interval straddles threshold")
    need(tail/2 != tail and decision(threshold, F(0), threshold) == "WITHIN_TARGET",
         "pair half-distance and equality conventions")
    return {"thermal_columns": 120, "omitted_mass": [tail.numerator, tail.denominator],
            "pair_thermal_radius": [tail.numerator, 2*tail.denominator],
            "nonnormalized_Gram_counterexample": [11, 25],
            "decision_fixtures_are_not_trajectory_predictions": True,
            "actual_pair_total_error_certified": False}


def run_checks():
    return {"status": "PASS", "scope": "exact_certificate_supporting_identities_only",
            "guard": check_guard(), "defect": check_defect(),
            "Gauss_L2": check_gauss(), "error_budget": check_budget(),
            "actual_interval_certificate_checked": False,
            "hardware_admission": False, "source_full_contact_obstruction_removed": False}


def main():
    need(len(sys.argv) == 1, "no CLI arguments accepted")
    payload = json.dumps(run_checks(), sort_keys=True, separators=(",", ":"))+"\n"
    sys.stdout.buffer.write(payload.encode("ascii"))


if __name__ == "__main__":
    main()
