#!/usr/bin/env python3
"""Frozen primary: matrix powers, direct rational derivatives and convolutions.

Only standard-library exact arithmetic is used.  The companion is launched,
never imported or read.  Scientific evaluation occurs only inside main().
"""

from fractions import Fraction
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import subprocess
import sys


N = 4
Q = Fraction
IDENTIFIER = "P-INTEGER-FIXED-DURATION-BOUNDARY-1"
AUTHORITY = (
    ("canon/CANON.md", 1052518,
     "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("canon/CORE.md", 30714,
     "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("canon/FRONTIER.md", 27382,
     "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("canon/REGISTRY.tsv", 532811,
     "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("canon/CHANGELOG.md", 207770,
     "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class ScientificFailure(Exception):
    """A completed failure of one of the preregistered assertions."""


def require(condition, label):
    if not condition:
        raise ScientificFailure(label)


def zero(rows, cols):
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def identity(size):
    return [[Q(i == j) for j in range(size)] for i in range(size)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, value):
    return [[value * x for x in row] for row in a]


def multiply(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), Q(0))
             for col in bt] for row in a]


def matvec(a, x):
    return [sum((v * w for v, w in zip(row, x)), Q(0)) for row in a]


def vadd(a, b):
    return [x + y for x, y in zip(a, b)]


def vsub(a, b):
    return [x - y for x, y in zip(a, b)]


def vscale(a, value):
    return [value * x for x in a]


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def power(a, exponent):
    result = identity(len(a))
    for _ in range(exponent):
        result = multiply(result, a)
    return result


def inverse(a, label):
    size = len(a)
    work = [list(row) + list(unit)
            for row, unit in zip(a, identity(size))]
    for col in range(size):
        pivot = next((row for row in range(col, size)
                      if work[row][col] != 0), None)
        require(pivot is not None, label)
        work[col], work[pivot] = work[pivot], work[col]
        divisor = work[col][col]
        work[col] = [x / divisor for x in work[col]]
        for row in range(size):
            if row != col:
                multiplier = work[row][col]
                work[row] = [x - multiplier * y
                             for x, y in zip(work[row], work[col])]
    result = [row[size:] for row in work]
    require(multiply(a, result) == identity(size), label)
    require(multiply(result, a) == identity(size), label)
    return result


def ldl_pivots(a):
    size = len(a)
    lower = identity(size)
    pivots = []
    require(a == transpose(a), "F_GEOMETRY")
    for j in range(size):
        diagonal = a[j][j] - sum(
            (lower[j][i] ** 2 * pivots[i] for i in range(j)), Q(0))
        require(diagonal != 0, "F_GEOMETRY")
        pivots.append(diagonal)
        for k in range(j + 1, size):
            lower[k][j] = (a[k][j] - sum(
                (lower[k][i] * pivots[i] * lower[j][i]
                 for i in range(j)), Q(0))) / diagonal
    diagonal_matrix = zero(size, size)
    for i in range(size):
        diagonal_matrix[i][i] = pivots[i]
    require(multiply(multiply(lower, diagonal_matrix), transpose(lower)) == a,
            "F_GEOMETRY")
    return pivots


def block(a, row, col, size=6):
    return [line[col:col + size] for line in a[row:row + size]]


def block_matrix(a, b, c, d):
    return [ar + br for ar, br in zip(a, b)] + [
        cr + dr for cr, dr in zip(c, d)]


def flatten(a):
    return [x for row in a for x in row]


def csv(values):
    return ",".join(str(x) for x in values)


def matrix_series_product(a, b):
    result = []
    for degree in range(N + 1):
        coefficient = zero(len(a[0]), len(b[0][0]))
        for i in range(degree + 1):
            coefficient = add(coefficient, multiply(a[i], b[degree - i]))
        result.append(coefficient)
    return result


def matrix_vector_series(a, x):
    result = []
    for degree in range(N + 1):
        coefficient = [Q(0)] * len(a[0])
        for i in range(degree + 1):
            coefficient = vadd(coefficient, matvec(a[i], x[degree - i]))
        result.append(coefficient)
    return result


def bilinear_series(x, a, y):
    """Actual triple coefficient convolution of x(e)^T a(e) y(e)."""
    result = []
    for degree in range(N + 1):
        coefficient = Q(0)
        for i in range(degree + 1):
            for j in range(degree - i + 1):
                k = degree - i - j
                coefficient += dot(x[i], matvec(a[j], y[k]))
        result.append(coefficient)
    return result


def vector_dot_series(x, y):
    return [sum((dot(x[i], y[degree - i]) for i in range(degree + 1)), Q(0))
            for degree in range(N + 1)]


def substituted(a, parameter):
    return [scale(coefficient, parameter ** j)
            for j, coefficient in enumerate(a)]


def constant_vector_series(x):
    return [list(x)] + [[Q(0)] * len(x) for _ in range(N)]


def phase_parts(z):
    return [coefficient[:6] for coefficient in z], [
        coefficient[6:] for coefficient in z]


def generating_value(q, endpoint, a, e):
    return (dot(q, matvec(a, q)) + dot(endpoint, matvec(a, endpoint))) / 2 - \
        dot(q, matvec(e, endpoint))


def generating_momenta(q, endpoint, a, e):
    initial = vsub(matvec(e, endpoint), matvec(a, q))
    final = vsub(matvec(a, endpoint), matvec(e, q))
    return initial, final


def generating_series(q, endpoint, a, e):
    first = bilinear_series(q, a, q)
    last = bilinear_series(endpoint, a, endpoint)
    cross = bilinear_series(q, e, endpoint)
    return [(x + y) / 2 - z for x, y, z in zip(first, last, cross)]


def momentum_series(q, endpoint, a, e):
    eq = matrix_vector_series(e, q)
    e_endpoint = matrix_vector_series(e, endpoint)
    aq = matrix_vector_series(a, q)
    a_endpoint = matrix_vector_series(a, endpoint)
    initial = [vsub(x, y) for x, y in zip(e_endpoint, aq)]
    final = [vsub(x, y) for x, y in zip(a_endpoint, eq)]
    return initial, final


def energy(z, d):
    return (dot(z[6:], z[6:]) + dot(z[:6], matvec(d, z[:6]))) / 2


def phase_energy_series(z, d):
    q, p = phase_parts(z)
    dq = [matvec(d, coefficient) for coefficient in q]
    pp = vector_dot_series(p, p)
    qdq = vector_dot_series(q, dq)
    return [(x + y) / 2 for x, y in zip(pp, qdq)]


def authority_check():
    root = Path(__file__).resolve().parents[2]
    for relative, size, expected_hash in AUTHORITY:
        try:
            actual = (root / relative).read_bytes()
        except OSError:
            raise ScientificFailure("F_AUTHORITY") from None
        require(len(actual) == size and sha256(actual).hexdigest() == expected_hash,
                "F_AUTHORITY")
    return len(AUTHORITY)


def geometry(records):
    spatial = zero(5, 5)
    for tail in range(5):
        for step, weight in ((1, Q(29, 324)), (2, Q(65, 324))):
            head = (tail + step) % 5
            incidence = [Q(0)] * 5
            incidence[tail] = Q(-1)
            incidence[head] = Q(1)
            for i in range(5):
                for j in range(5):
                    spatial[i][j] += weight * incidence[i] * incidence[j]
    circulant = [[Q(188 if i == j else
                      -29 if (j - i) % 5 in (1, 4) else -65, 324)
                  for j in range(5)] for i in range(5)]
    require(spatial == circulant, "F_GEOMETRY")
    ell = [Q(1), Q(-1), Q(0), Q(0), Q(0)]
    coupling = Q(1, 324)
    potential = zero(6, 6)
    for i in range(5):
        for j in range(5):
            potential[i][j] = spatial[i][j]
        potential[i][5] = potential[5][i] = -coupling * ell[i]
    potential[5][5] = Q(1)
    unit = identity(6)
    c = subtract(unit, scale(potential, Q(1, 2)))
    d = subtract(unit, multiply(c, c))
    null = zero(6, 6)
    k = block_matrix(null, unit, scale(d, Q(-1)), null)
    m = block_matrix(c, unit, scale(d, Q(-1)), c)
    metric = block_matrix(d, null, null, unit)
    uniform = [Q(1)] * 5 + [Q(0)]
    require(matvec(d, uniform) == [Q(0)] * 6, "F_GEOMETRY")
    require(add(multiply(c, c), d) == unit, "F_GEOMETRY")
    require(all(a == transpose(a) for a in (spatial, potential, c, d)),
            "F_GEOMETRY")
    require(multiply(c, d) == multiply(d, c), "F_GEOMETRY")
    require(multiply(multiply(transpose(m), metric), m) == metric,
            "F_GEOMETRY")
    require(multiply(m, k) == multiply(k, m), "F_GEOMETRY")
    positive_spatial = subtract(identity(5), spatial)
    positive_full = subtract(scale(unit, Q(3)), potential)
    spatial_pivots = ldl_pivots(positive_spatial)
    full_pivots = ldl_pivots(positive_full)
    require(all(x > 0 for x in spatial_pivots + full_pivots), "F_GEOMETRY")
    spatial_inverse = inverse(positive_spatial, "F_GEOMETRY")
    schur = -(coupling ** 2) * dot(ell, matvec(spatial_inverse, ell))
    require(schur < 0, "F_GEOMETRY")
    composite = power(m, 3)
    u3, b3 = block(composite, 0, 0), block(composite, 0, 6)
    require(u3 == subtract(power(c, 3), scale(multiply(c, d), Q(3))),
            "F_GEOMETRY")
    require(b3 == subtract(scale(power(c, 2), Q(4)), unit), "F_GEOMETRY")
    require(b3 == multiply(subtract(unit, potential), positive_full),
            "F_GEOMETRY")
    require(block(composite, 6, 0) == scale(multiply(d, b3), Q(-1)) and
            block(composite, 6, 6) == u3, "F_GEOMETRY")
    b3_pivots = ldl_pivots(b3)
    require(sum(x > 0 for x in b3_pivots) == 5 and
            sum(x < 0 for x in b3_pivots) == 1, "F_GEOMETRY")
    e3 = inverse(b3, "F_GEOMETRY")
    records.append("P|" + csv(spatial_pivots) + "|" + csv(full_pivots) +
                   "|" + str(schur))
    records.append("B|" + csv(flatten(u3)) + "|" + csv(flatten(b3)) +
                   "|" + csv(flatten(e3)))
    return c, d, k, m, uniform, u3, b3, e3


def formal_series(k, m, c, records, counts):
    rotations = [scale(power(k, j), Q(1, factorial(j))) for j in range(N + 1)]
    for j in range(N):
        require(scale(rotations[j + 1], Q(j + 1)) == multiply(k, rotations[j]),
                "F_SERIES")
    for i in range(N + 1):
        for j in range(N + 1 - i):
            require(multiply(rotations[i], rotations[j]) ==
                    scale(rotations[i + j], Q(comb(i + j, i))), "F_SERIES")
            counts["COMPOSITION_PAIRS"] += 1
    transfers = [multiply(m, coefficient) for coefficient in rotations]
    u = [block(coefficient, 0, 0) for coefficient in transfers]
    b = [block(coefficient, 0, 6) for coefficient in transfers]
    e = [inverse(b[0], "F_SERIES")]
    for degree in range(1, N + 1):
        remainder = zero(6, 6)
        for j in range(1, degree + 1):
            remainder = add(remainder, multiply(b[j], e[degree - j]))
        e.append(scale(multiply(e[0], remainder), Q(-1)))
    a = matrix_series_product(e, u)
    identity_series = [identity(6)] + [zero(6, 6) for _ in range(N)]
    require(matrix_series_product(b, e) == identity_series and
            matrix_series_product(e, b) == identity_series, "F_SERIES")
    require(a[0] == c and e[0] == identity(6), "F_SERIES")
    require(a[1] == scale(identity(6), Q(-1)) and e[1] == scale(c, Q(-1)),
            "F_SERIES")
    require(all(coefficient == transpose(coefficient) for coefficient in a + e),
            "F_SERIES")
    for j, coefficient in enumerate(rotations):
        records.append("R|" + str(j) + "|" + csv(flatten(coefficient)))
    return rotations, transfers, a, e


def regular_cases(c, d, m, u3, b3, e3, rotations, transfers, a, e,
                  records, counts, controls):
    directions = ([Q(1), Q(-1), Q(0)], [Q(0), Q(1), Q(-1)],
                  [Q(1), Q(-2), Q(1)])
    a3 = multiply(e3, u3)
    u3_prime = scale(multiply(d, b3), Q(-1))
    b3_prime = u3
    e3_prime = scale(multiply(multiply(e3, b3_prime), e3), Q(-1))
    a3_prime = add(multiply(e3_prime, u3), multiply(e3, u3_prime))
    require(all(matrix == transpose(matrix)
                for matrix in (e3, a3, e3_prime, a3_prime)), "F_BOUNDARY")
    for r in range(1, 7):
        initial = [Q(((r + 1) * (j + 2) + j * j) % 19 - 9, r + 2)
                   for j in range(12)]
        phases = [matvec(power(m, n), initial) for n in range(4)]
        h = energy(initial, d)
        require(h > 0 and all(energy(z, d) == h for z in phases), "F_VARIATION")
        for n, z in enumerate(phases):
            records.append("Z|" + str(r) + "|" + str(n) + "|" + csv(z))
        records.append("H|" + str(r) + "|" + str(h))
        bond_values, parameter_derivatives = [], []
        incoming, outgoing = [], []
        for b in range(1, 4):
            q, endpoint = phases[b - 1][:6], phases[b][:6]
            bond_values.append(generating_value(q, endpoint, a[0], e[0]))
            start_p, end_p = generating_momenta(q, endpoint, a[0], e[0])
            outgoing.append(start_p)
            incoming.append(end_p)
            require(start_p == phases[b - 1][6:] and end_p == phases[b][6:],
                    "F_VARIATION")
            derivative = generating_value(q, endpoint, a[1], e[1])
            parameter_derivatives.append(derivative)
            require(derivative == -h, "F_VARIATION")
        require(all(incoming[n - 1] == outgoing[n] for n in (1, 2)),
                "F_VARIATION")
        constrained = [dot(direction, parameter_derivatives) for direction in directions]
        require(all(work == 0 for work in constrained), "F_VARIATION")
        counts["CONSTRAINED_VARIATIONS"] += len(constrained)
        free = dot([Q(1), Q(0), Q(0)], parameter_derivatives)
        require(free == -h and free != 0, "F_VARIATION")
        counts["FREE_LAPSE_WITNESSES"] += 1
        fixed = h + 1
        shifted_derivatives = [derivative + fixed for derivative in parameter_derivatives]
        added_works = [dot(direction, shifted_derivatives) for direction in directions]
        require(all(work == 0 for work in added_works) and h - fixed == -1,
                "F_VARIATION")
        controls["NC01"].append(h > 0 and all(work == 0 for work in constrained))
        controls["NC02"].append(all(work == 0 for work in added_works) and h - fixed == -1)
        records.append("W|" + str(r) + "|" + csv(constrained) + "|" + str(free) +
                       "|" + csv(added_works))

        q, endpoint = phases[0][:6], phases[3][:6]
        recovered = matvec(e3, vsub(endpoint, matvec(u3, q)))
        require(recovered == initial[6:], "F_BOUNDARY")
        total_zero = sum(bond_values, Q(0))
        total_boundary = generating_value(q, endpoint, a3, e3)
        require(total_zero == total_boundary, "F_BOUNDARY")
        boundary_derivative = generating_value(q, endpoint, a3_prime, e3_prime)
        require(boundary_derivative == -h, "F_BOUNDARY")
        boundary_initial, boundary_final = generating_momenta(q, endpoint, a3, e3)
        require(boundary_initial == phases[0][6:] and
                boundary_final == phases[3][6:], "F_BOUNDARY")
        recovered_h = energy(q + recovered, d)
        require(recovered_h == h and recovered_h - fixed == -1, "F_BOUNDARY")
        controls["NC06"].append(recovered_h - fixed == -1)
        controls["NC08"].append(boundary_derivative != h)
        records.append("A|" + str(r) + "|" + str(total_zero) + "|" +
                       str(total_boundary) + "|" + str(boundary_derivative))
        counts["REGULAR_BOUNDARY_CASES"] += 1

        theta = [Q(0), Q(r - 3, r + 1), Q(2 * r - 5, r + 2), Q(0)]
        eta = [Q(0), Q(r + 2, r + 3), -Q(r + 1, r + 4), Q(0)]
        alpha = [theta[b] - theta[b - 1] for b in range(1, 4)]
        require(sum(alpha, Q(0)) == 0, "F_GAUGE")
        transformed = [[vscale(matvec(rotations[j], phases[n]), theta[n] ** j)
                        for j in range(N + 1)] for n in range(4)]
        require(transformed[0] == constant_vector_series(phases[0]) and
                transformed[3] == constant_vector_series(phases[3]), "F_GAUGE")
        for n in range(4):
            dressed = matrix_vector_series(substituted(rotations, -theta[n]),
                                           transformed[n])
            require(dressed == constant_vector_series(phases[n]), "F_GAUGE")
            require(phase_energy_series(transformed[n], d) == [h] + [Q(0)] * N,
                    "F_GAUGE")
            composed = matrix_vector_series(substituted(rotations, eta[n]),
                                            transformed[n])
            direct_composition = [vscale(matvec(rotations[j], phases[n]),
                                         (theta[n] + eta[n]) ** j)
                                  for j in range(N + 1)]
            require(composed == direct_composition, "F_GAUGE")
            for j in range(N + 1):
                records.append("G|" + str(r) + "|" + str(n) + "|" + str(j) +
                               "|" + csv(transformed[n][j]))
            counts["GAUGE_PHASE_SERIES"] += 1
        actual_action = [Q(0)] * (N + 1)
        for b in range(1, 4):
            transferred = matrix_vector_series(substituted(transfers, alpha[b - 1]),
                                                transformed[b - 1])
            require(transferred == transformed[b], "F_GAUGE")
            q_series, p_series = phase_parts(transformed[b - 1])
            endpoint_series, final_p_series = phase_parts(transformed[b])
            a_sub = substituted(a, alpha[b - 1])
            e_sub = substituted(e, alpha[b - 1])
            actual_start, actual_final = momentum_series(q_series, endpoint_series,
                                                         a_sub, e_sub)
            require(actual_start == p_series and actual_final == final_p_series,
                    "F_GAUGE")
            action = generating_series(q_series, endpoint_series, a_sub, e_sub)
            actual_action = [x + y for x, y in zip(actual_action, action)]
            counts["GAUGE_BOND_SERIES"] += 1
        require(actual_action == [total_zero] + [Q(0)] * N, "F_GAUGE")
        records.append("S|" + str(r) + "|" + csv(actual_action))
        counts["GAUGE_ACTION_SERIES"] += 1

        if r == 1:
            omitted_phase_residuals = []
            wrong_dressing_residuals = []
            for b in range(1, 4):
                changed_transfer = matrix_vector_series(
                    substituted(transfers, alpha[b - 1]),
                    constant_vector_series(phases[b - 1]))
                omitted_phase_residuals.extend(vsub(
                    changed_transfer[1], constant_vector_series(phases[b])[1]))
            for n in range(4):
                wrong_dressed = matrix_vector_series(substituted(rotations, theta[n]),
                                                     transformed[n])
                wrong_dressing_residuals.extend(vsub(
                    wrong_dressed[1], constant_vector_series(phases[n])[1]))
            controls["NC03"].append(any(x != 0 for x in omitted_phase_residuals))
            controls["NC04"].append(any(x != 0 for x in wrong_dressing_residuals))


def uniform_shear(z, parameter):
    return vadd(z[:6], vscale(z[6:], parameter)) + list(z[6:])


def caustic_cases(d, uniform, records, counts, controls):
    directions = ([Q(1), Q(-1), Q(0)], [Q(0), Q(1), Q(-1)],
                  [Q(1), Q(-2), Q(1)])
    representatives = {}
    initial_phases = set()
    for sign in (-1, 1):
        base_lapses = None
        base_accumulated = None
        base_phases = None
        for distinguished in range(3):
            lapses = [Q(-3 if b == distinguished else 0) for b in range(3)]
            accumulated = [Q(0)]
            for lapse in lapses:
                accumulated.append(accumulated[-1] + lapse)
            signed_uniform = vscale(uniform, Q(sign))
            phases = [vscale(signed_uniform, Q(n) + accumulated[n]) +
                      list(signed_uniform) for n in range(4)]
            require(phases[0][:6] == [Q(0)] * 6 and
                    phases[3][:6] == [Q(0)] * 6, "F_CAUSTIC")
            require(sum(lapses, Q(0)) == -3, "F_CAUSTIC")
            h = energy(phases[0], d)
            require(h == Q(5, 2) and all(energy(z, d) == h for z in phases),
                    "F_CAUSTIC")
            require(all(matvec(d, z[:6]) == [Q(0)] * 6 and
                        matvec(d, z[6:]) == [Q(0)] * 6 for z in phases),
                    "F_CAUSTIC")
            actions, derivatives, initial_momenta, final_momenta = [], [], [], []
            for b in range(3):
                q, endpoint = phases[b][:6], phases[b + 1][:6]
                denominator = 1 + lapses[b]
                require(denominator != 0, "F_CAUSTIC")
                delta = vsub(endpoint, q)
                norm = dot(delta, delta)
                action = norm / (2 * denominator)
                gradient_initial = vscale(delta, -Q(1) / denominator)
                gradient_final = vscale(delta, Q(1) / denominator)
                initial_p = vscale(gradient_initial, Q(-1))
                final_p = gradient_final
                require(initial_p == phases[b][6:] and
                        final_p == phases[b + 1][6:], "F_CAUSTIC")
                require(phases[b + 1] == uniform_shear(phases[b], denominator),
                        "F_CAUSTIC")
                derivative = -norm / (2 * denominator ** 2)
                require(derivative == -h, "F_CAUSTIC")
                actions.append(action)
                derivatives.append(derivative)
                initial_momenta.append(initial_p)
                final_momenta.append(final_p)
            require(all(final_momenta[n - 1] == initial_momenta[n] for n in (1, 2)),
                    "F_CAUSTIC")
            total_action = sum(actions, Q(0))
            works = [dot(direction, derivatives) for direction in directions]
            require(total_action == 0 and all(work == 0 for work in works),
                    "F_CAUSTIC")
            if distinguished == 0:
                base_lapses = lapses
                base_accumulated = accumulated
                base_phases = phases
                representatives[sign] = phases[0]
            else:
                theta = [x - y for x, y in zip(accumulated, base_accumulated)]
                require(theta[0] == 0 and theta[3] == 0, "F_CAUSTIC")
                shifted_lapses = [base_lapses[b] + theta[b + 1] - theta[b]
                                  for b in range(3)]
                require(shifted_lapses == lapses, "F_CAUSTIC")
                transformed = [uniform_shear(base_phases[n], theta[n])
                               for n in range(4)]
                require(transformed == phases, "F_CAUSTIC")
            initial_phases.add(tuple(phases[0]))

            forbidden_theta = [Q(0), Q(0), Q(0), Q(1)]
            forbidden_lapses = [lapses[b] + forbidden_theta[b + 1] - forbidden_theta[b]
                                 for b in range(3)]
            forbidden_phases = [uniform_shear(phases[n], forbidden_theta[n])
                                for n in range(4)]
            lapse_change = sum(forbidden_lapses, Q(0)) - sum(lapses, Q(0))
            endpoint_change = vsub(forbidden_phases[3][:6], phases[3][:6])
            require(lapse_change == 1 and endpoint_change == signed_uniform and
                    endpoint_change != [Q(0)] * 6, "F_CAUSTIC")
            controls["NC07"].append(lapse_change != 0 and endpoint_change != [Q(0)] * 6)
            records.append("C|" + str(sign) + "|" + str(distinguished) + "|" +
                           csv(flatten(phases)) + "|" + str(h) + "|" +
                           str(total_action) + "|" + csv(works))
            counts["CAUSTIC_HISTORIES"] += 1
    counts["CAUSTIC_ORBITS"] = len(initial_phases)
    require(counts["CAUSTIC_ORBITS"] == 2 and
            representatives[-1][6:] != representatives[1][6:], "F_CAUSTIC")
    controls["NC05"].append(representatives[-1][6:] != representatives[1][6:])


def compute_certificate():
    authority_files = authority_check()
    count_order = (
        ("COMPOSITION_PAIRS", 15),
        ("REGULAR_BOUNDARY_CASES", 6),
        ("CONSTRAINED_VARIATIONS", 18),
        ("FREE_LAPSE_WITNESSES", 6),
        ("GAUGE_PHASE_SERIES", 24),
        ("GAUGE_BOND_SERIES", 18),
        ("GAUGE_ACTION_SERIES", 6),
        ("CAUSTIC_HISTORIES", 6),
        ("CAUSTIC_ORBITS", 2),
    )
    counts = {name: 0 for name, _ in count_order}
    controls = {"NC" + str(i).zfill(2): [] for i in range(1, 9)}
    records = []
    c, d, k, m, uniform, u3, b3, e3 = geometry(records)
    rotations, transfers, a, e = formal_series(k, m, c, records, counts)
    regular_cases(c, d, m, u3, b3, e3, rotations, transfers, a, e,
                  records, counts, controls)
    caustic_cases(d, uniform, records, counts, controls)
    expected_observations = {"NC01": 6, "NC02": 6, "NC03": 1, "NC04": 1,
                             "NC05": 1, "NC06": 6, "NC07": 6, "NC08": 6}
    for name, observations in controls.items():
        require(len(observations) == expected_observations[name], "F_COUNTS")
        require(all(observations), "F_CONTROL")
        records.append("N|" + name + "|DETECTED")
    require(authority_files == 5 and len(controls) == 8 and N == 4, "F_COUNTS")
    require(all(counts[name] == expected for name, expected in count_order), "F_COUNTS")
    payload = ("\n".join(records) + "\n").encode("ascii")
    lines = ["CERTIFICATE=" + IDENTIFIER, "AUTHORITY_FILES=" + str(authority_files),
             "SERIES_ORDER=" + str(N)]
    lines.extend(name + "=" + str(counts[name]) for name, _ in count_order)
    lines.extend(["CAUSTIC_ENERGY=5/2", "PAYLOAD_SHA256=" + sha256(payload).hexdigest(),
                  "NEGATIVE_CONTROLS=" + str(len(controls)), "CERTIFICATE_RESULT=PASS"])
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        certificate = compute_certificate()
        try:
            result = subprocess.run(
                [sys.executable, "-I", str(Path(__file__).resolve().with_name("breaker.py"))],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=540,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            raise ScientificFailure("F_BYTES") from None
        require(result.returncode == 0 and result.stderr == b"" and
                result.stdout == certificate, "F_BYTES")
    except ScientificFailure as failure:
        sys.stdout.buffer.write((str(failure) + "\nRESULT=FAIL\n").encode("ascii"))
        return 0
    sys.stdout.buffer.write(certificate + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
