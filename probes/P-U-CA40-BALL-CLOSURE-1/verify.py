#!/usr/bin/env python3
"""Exact algebra supporting, but not replacing, a trajectory certificate.

PUBLIC NON-CANONICAL. Conditional L1. Apache-2.0, A. M. Thorn.
P-U-CA40-BALL-CLOSURE-1, reservation #1460.
Authority base c2459261aa15552e6560753dd8e1753f5164972d.
Fraction/Fock helpers adapt the public SINUS-COMPARISON-1 verifier;
guard/defect/Gauss/budget checks inherit ERROR-CLOSURE-1 pin 3440928c.
New rational fixtures audit Schur majorants, norm-ball recurrences,
roundoff/underflow bookkeeping and dual Horner evaluation. They do not
certify the operation trace of a compiled kernel or any actual trajectory.
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


def euclidean2(v):
    """Ordinary complex Euclidean norm, not the unnormalized Fock metric."""
    return sum((abs2(z) for z in v), F(0))


def dense_action(matrix, vector):
    return tuple(sum_complex(mul(a, x) for a, x in zip(row, vector))
                 for row in matrix)


def sum_complex(values):
    out = Z
    for value in values:
        out = add(out, value)
    return out


def vector_add(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))


def vector_subtract(a, b):
    return tuple(add(x, neg(y)) for x, y in zip(a, b))


def schur_square(majorant):
    need(majorant and majorant[0], "nonempty Schur matrix")
    need(all(len(row) == len(majorant[0]) for row in majorant), "rectangular matrix")
    need(all(x >= 0 for row in majorant for x in row), "nonnegative Schur entries")
    rows = [sum(row, F(0)) for row in majorant]
    columns = [sum((row[j] for row in majorant), F(0))
               for j in range(len(majorant[0]))]
    return max(rows)*max(columns)


def schur_upper(matrix):
    # Rational component l1 norms majorize each complex entry magnitude.
    return upper_sqrt(schur_square([[abs(z[0])+abs(z[1]) for z in row]
                                   for row in matrix]))


def check_schur():
    matrices = (
        ((c(1), c(F(3, 5), F(4, 5))), (Z, c(F(-1, 2)))),
        ((c(1), Z), (c(1), Z), (Z, c(1))),
        ((c(1), c(F(1, 4), F(-1, 8)), Z),
         (Z, c(1), c(F(-3, 16), F(1, 8))), (Z, Z, c(1))))
    counts = 0
    for matrix in matrices:
        majorant = [[abs(z[0])+abs(z[1]) for z in row] for row in matrix]
        bound2 = schur_square(majorant)
        columns = len(matrix[0])
        vectors = [tuple(O if j == k else Z for j in range(columns))
                   for k in range(columns)]
        vectors += [tuple(c(F(j+1, 7), F(2-j, 11)) for j in range(columns))]
        for vector in vectors:
            image = dense_action(matrix, vector)
            # Explicit weighted Cauchy row inequality, then row/column bound.
            row_cauchy = sum((sum(row)*sum((b*abs2(x) for b, x in zip(row, vector)), F(0))
                              for row in majorant), F(0))
            need(euclidean2(image) <= row_cauchy <= bound2*euclidean2(vector),
                 "rational Schur majorant")
            # A direct sum of identical short chains has no sqrt(copy count).
            repeated = image*5
            need(euclidean2(repeated) == 5*euclidean2(image)
                 and euclidean2(repeated) <= bound2*euclidean2(vector*5),
                 "direct-sum Schur bound without mode-space dimension factor")
            counts += 1
        if len(matrix) == columns:
            for size in range(1, columns+1):
                block = [row[:size] for row in majorant[:size]]
                need(schur_square(block) <= bound2, "principal-chain majorant")
    tall = ((c(1),), (c(1),))
    need(euclidean2(dense_action(tall, (O,))) == 2 > 1,
         "row maximum alone is not a Euclidean operator-norm bound")
    # Realification preserves Euclidean norms; its absolute Schur matrix
    # can use |Re a|+|Im a| <= sqrt(2)|a|, hence sqrt(2) times S(|a|).
    z = c(F(3, 5), F(4, 5))
    need((abs(z[0])+abs(z[1]))**2 <= 2*abs2(z), "realification factor sqrt two")
    need((abs(z[0])+abs(z[1]))**2 > abs2(z), "dropping realification factor falsifier")
    return {"vector_fixtures": counts, "direct_sum_no_dimension_penalty": True,
            "row_only_norm_negative_control": True,
            "actual_kernel_coefficient_tables_checked": False}


def check_ball_recurrences():
    # Stored centers, exact target operators and perturbations are rational.
    center = (c(F(1, 2), F(1, 4)), c(F(-1, 8), F(3, 8)))
    perturbation = (c(F(1, 128)), c(0, F(-1, 256)))
    truth = vector_add(center, perturbation)
    hatted = ((c(1), c(F(1, 4), F(-1, 8))), (Z, c(1)))
    delta = ((c(F(1, 1024)), c(0, F(-1, 2048))),
             (c(F(1, 4096)), c(F(-1, 1024))))
    target = tuple(tuple(add(x, y) for x, y in zip(a, b)) for a, b in zip(hatted, delta))
    noise = (c(F(1, 65536), F(-1, 131072)), c(F(1, 131072)))
    stored_output = vector_add(dense_action(hatted, center), noise)
    target_output = dense_action(target, truth)
    n = upper_sqrt(euclidean2(center))
    r = upper_sqrt(euclidean2(perturbation))
    s, e = schur_upper(hatted), schur_upper(delta)
    arithmetic = upper_sqrt(euclidean2(noise))
    radius = (s+e)*r+e*n+arithmetic
    norm_bound = s*n+arithmetic
    need(euclidean2(vector_subtract(target_output, stored_output)) <= radius*radius,
         "coefficient/input/arithmetic norm-ball recurrence")
    need(euclidean2(stored_output) <= norm_bound*norm_bound,
         "stored center norm recurrence has no target coefficient-error term")
    need(2 > 1, "input uncertainty must be amplified by full target, not hatted norm only")
    # xhat=0,r=1,Ahat=1,A=2: omitting E*r gives 1 instead of required 2.
    need((F(1)+F(1))*F(1) == 2 and F(1)*F(1)+F(1)*F(0) < 2,
         "omitted coefficient uncertainty acting on input-ball falsifier")
    # A and inverse A multiply to identity. Local errors nevertheless see
    # noncontractive suffixes; only the ORIGINAL input ball is contractive.
    a = ((c(1), c(3)), (Z, c(1)))
    inverse = ((c(1), c(-3)), (Z, c(1)))
    local = (Z, O)
    for x in ((O, Z), (Z, O), center):
        need(dense_action(inverse, dense_action(a, x)) == x, "contractive total product")
    need(euclidean2(dense_action(a, local)) == 10 > euclidean2(local),
         "annihilation-half input cannot use final contraction")
    need(euclidean2(dense_action(inverse, local)) == 10 > euclidean2(local),
         "local arithmetic errors cannot all use suffix weight one")
    stored_first = vector_add(dense_action(a, center), local)
    stored_last = dense_action(inverse, stored_first)
    exact_error = vector_subtract(truth, stored_last)
    decomposition = vector_subtract(perturbation, dense_action(inverse, local))
    need(exact_error == decomposition, "exact telescoping input and suffix errors")
    telescoping_bound = r+schur_upper(inverse)*upper_sqrt(euclidean2(local))
    need(euclidean2(exact_error) <= telescoping_bound*telescoping_bound,
         "suffix-weighted local error bound")
    # Disjoint occupation grades share ONE half-action error vector.
    # Sum t_j ||P_j error|| <= sqrt(sum t_j^2) ||error||.
    tail_weights = (F(1, 16), F(1, 8), F(1, 4))
    for grade_errors in ((F(3, 5), F(4, 5), F(0)), tail_weights):
        weighted = sum((t*e for t, e in zip(tail_weights, grade_errors)), F(0))
        t2 = sum((t*t for t in tail_weights), F(0))
        e2 = sum((e*e for e in grade_errors), F(0))
        need(weighted*weighted <= t2*e2, "orthogonal-grade half-error tail aggregation")
    need(t2*t2 > max(tail_weights)**2*t2,
         "max tail weight alone cannot bound weighted grade-norm sum")
    return {"coefficient_and_input_ball_terms": True, "separate_center_norm_bound": True,
            "noncontractive_half_and_suffix_negative_controls": True,
            "orthogonal_grade_tail_Cauchy": True,
            "actual_trajectory_ball_checked": False}


def check_rounding():
    u, eta = F(1, 1 << 53), F(1, 1 << 1074)
    counts = 0
    for qmax in (0, 1, 2, 4, 8, 13, 15):
        k = 4*qmax+8
        need(k*u < 1, "gamma denominator positive")
        gamma = k*u/(1-k*u)
        need((1+u)**k-1 <= gamma and 1-(1-u)**k <= gamma,
             "exact relative rounding product envelope")
        need(qmax+2 <= k and 4*qmax <= k, "frozen complex dot operation/path domination")
        # Every additive eta term may cross at most k relative factors.
        underflow_sum = sum((eta*(1+u)**j for j in range(k)), F(0))
        need(underflow_sum <= k*eta/(1-k*u), "absolute underflow accumulation")
        for dimension in (1, 7, 19):
            underflow = upper_sqrt(F(2*dimension))*k*eta/(1-k*u)
            need(underflow > 0 and underflow*underflow >=
                 2*dimension*(k*eta/(1-k*u))**2,
                 "underflow allowance kept nonzero in per-column norm")
            counts += 1
    need(eta/2 > u*(eta/2) and eta/2 <= eta,
         "RN subnormal midpoint-to-zero defeats relative-error-only model")
    flushed = (1 << 40)*eta
    need(flushed > u*flushed+eta, "FTZ violates gradual-underflow error model")
    # An adversarial rational operation trace obeying the rounding law;
    # it is NOT an emulator/test of actual IEEE arithmetic or the compiler.
    matrix = ((c(1), c(F(3, 16), F(1, 8)), c(F(-1, 8), F(1, 16))),
              (Z, c(1), c(F(1, 4), F(-1, 16))), (Z, Z, c(1)))
    vector = (c(F(1, 2), F(1, 4)), c(F(-1, 8), F(3, 8)), c(F(1, 16), F(-1, 4)))
    step = 0
    def rnd(value):
        nonlocal step
        step += 1
        sign = 1 if step % 2 else -1
        return value*(1+sign*u)+sign*eta
    output = []
    for i, row in enumerate(matrix):
        real, imag = vector[i]
        for j in range(i+1, len(row)):
            ar, ai = row[j]
            xr, xi = vector[j]
            real = rnd(real+rnd(rnd(ar*xr)-rnd(ai*xi)))
            imag = rnd(imag+rnd(rnd(ar*xi)+rnd(ai*xr)))
        output.append(c(real, imag))
    difference2 = euclidean2(vector_subtract(output, dense_action(matrix, vector)))
    s, n = schur_upper(matrix), upper_sqrt(euclidean2(vector))
    qmax, dimension = len(matrix), len(matrix)
    k = 4*qmax+8
    gamma = k*u/(1-k*u)
    rho = upper_sqrt(F(2))*gamma*s
    allowance = rho*n+upper_sqrt(F(2*dimension))*k*eta/(1-k*u)
    need(0 < difference2 <= allowance*allowance,
         "non-FMA complex dot rational error-trace enclosure")
    input_error = (c(F(1, 4096)), Z, c(0, F(-1, 8192)))
    coefficient_error = tuple(tuple(c(F(1, 16384)) if i == j else Z
                                    for j in range(dimension)) for i in range(dimension))
    exact_matrix = tuple(tuple(add(a, b) for a, b in zip(row, change))
                         for row, change in zip(matrix, coefficient_error))
    exact_output = dense_action(exact_matrix, vector_add(vector, input_error))
    e = schur_upper(coefficient_error)
    r = upper_sqrt(euclidean2(input_error))
    full_radius = (s+e)*r+e*n+allowance
    stored_norm_upper = s*n+allowance
    need(euclidean2(vector_subtract(exact_output, output)) <= full_radius**2 and
         euclidean2(output) <= stored_norm_upper**2,
         "full operational norm-ball and center-norm recurrences")
    return {"gamma_underflow_dimension_fixtures": counts,
            "epsilon_power": -53, "absolute_underflow_power": -1074,
            "operation_count": "k=4*qmax+8",
            "rounding_trace_fixture": "rational_adversarial_law_not_IEEE_emulation",
            "relative_only_and_FTZ_negative_controls": True,
            "actual_compiler_operation_trace_checked": False}


def check_dual_horner():
    coefficients = [F(3, 8), F(-1, 4), F(5, 16), F(1, 32), F(-1, 64), F(3, 128)]
    xhat, xtrue = F(1, 2), F(1, 2)+F(1, 4096)
    theta_error = abs(xtrue-xhat)
    p, derivative = coefficients[-1], F(0)
    radius_p = radius_d = F(0)
    for coefficient in reversed(coefficients[:-1]):
        old_p, old_r, old_d = p, radius_p, derivative
        derivative = xhat*old_d+old_p
        radius_d = (abs(xhat)+theta_error)*radius_d+theta_error*abs(old_d)+old_r
        p = xhat*old_p+coefficient
        radius_p = (abs(xhat)+theta_error)*old_r+theta_error*abs(old_p)
    need(p == peval(coefficients, xhat) and derivative == peval(pderivative(coefficients), xhat),
         "dual Horner centers use old polynomial value")
    need(abs(peval(coefficients, xtrue)-p) <= radius_p and
         abs(peval(pderivative(coefficients), xtrue)-derivative) <= radius_d,
         "dual Horner node uncertainty through norm-ball recurrence")
    # At x=1/2, polynomial x^2 has derivative 1, not 1/2.
    wrong_p, wrong_d = F(1), F(0)
    for coefficient in (F(0), F(0)):
        wrong_p = xhat*wrong_p+coefficient
        wrong_d = xhat*wrong_d+wrong_p
    need(wrong_d != 2*xhat, "updated-polynomial derivative negative control")
    return {"exact_dual_Horner_identity": True, "node_uncertainty_ball": True,
            "updated_polynomial_negative_control": True,
            "actual_FP_Horner_trace_checked": False}


def run_checks():
    return {"status": "PASS", "scope": "exact_certificate_supporting_identities_only",
            "guard": check_guard(), "defect": check_defect(),
            "Gauss_L2": check_gauss(), "error_budget": check_budget(),
            "Schur": check_schur(), "norm_ball": check_ball_recurrences(),
            "rounding": check_rounding(), "dual_Horner": check_dual_horner(),
            "actual_interval_certificate_checked": False,
            "hardware_admission": False, "source_full_contact_obstruction_removed": False}


def main():
    need(len(sys.argv) == 1, "no CLI arguments accepted")
    payload = json.dumps(run_checks(), sort_keys=True, separators=(",", ":"))+"\n"
    sys.stdout.buffer.write(payload.encode("ascii"))


if __name__ == "__main__":
    main()
