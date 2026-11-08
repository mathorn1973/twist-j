#!/usr/bin/env python3
"""Prospective exact audit; execute only after the public pin and receipt.

The primary implementation uses Fraction Taylor coefficients, triangular
coefficient recursion, binomial square roots, and adjugate inverses.  It
neither imports nor reads the independently authored breaker implementation.
"""

from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import subprocess
import sys


ORDER = 4
PROBE = "P-RELATIONAL-MASS-STABLE-BINDING-1"
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


class AuditFailure(Exception):
    """Only explicitly declared discrepancies use this exception."""


def require(condition, code):
    if not condition:
        raise AuditFailure(code)


def constant(value, n):
    return (F(value),) + (F(0),) * n


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def times_scalar(a, value):
    return tuple(x * value for x in a)


def times(a, b):
    out = [F(0)] * len(a)
    for i, x in enumerate(a):
        if x:
            for j in range(len(a) - i):
                if b[j]:
                    out[i + j] += x * b[j]
    return tuple(out)


def reciprocal(a, code="F02_GEOMETRY"):
    require(a[0] != 0, code)
    out = [1 / a[0]]
    for m in range(1, len(a)):
        out.append(-sum((a[j] * out[m - j] for j in range(1, m + 1)),
                        F(0)) / a[0])
    return tuple(out)


def square_root(a, root, code="F02_GEOMETRY"):
    """Finite binomial expansion at the explicitly checked positive root."""
    root = F(root)
    require(root > 0 and root * root == a[0], code)
    n = len(a) - 1
    one = constant(1, n)
    h = minus(times_scalar(a, 1 / a[0]), one)
    term = one
    total = one
    coefficient = F(1)
    for k in range(1, n + 1):
        term = times(term, h)
        coefficient *= (F(1, 2) - (k - 1)) / k
        total = plus(total, times_scalar(term, coefficient))
    return times_scalar(total, root)


def derivative(a):
    return tuple((i + 1) * a[i + 1] for i in range(len(a) - 1))


def matrix(values, n):
    return tuple(constant(v, n) for v in values)


def identity(n):
    return matrix((1, 0, 0, 1), n)


def transpose(a):
    return (a[0], a[2], a[1], a[3])


def matrix_plus(a, b):
    return tuple(plus(x, y) for x, y in zip(a, b))


def matrix_minus(a, b):
    return tuple(minus(x, y) for x, y in zip(a, b))


def matrix_scale(a, value):
    return tuple(times_scalar(x, value) for x in a)


def matrix_times(a, b):
    return tuple(plus(times(a[2 * i], b[j]),
                      times(a[2 * i + 1], b[2 + j]))
                 for i in range(2) for j in range(2))


def matrix_vector(a, v):
    return tuple(plus(times(a[2 * i], v[0]),
                      times(a[2 * i + 1], v[1])) for i in range(2))


def outer(a, b):
    return tuple(times(a[i], b[j]) for i in range(2) for j in range(2))


def dot(a, b):
    return plus(times(a[0], b[0]), times(a[1], b[1]))


def trace(a):
    return plus(a[0], a[3])


def determinant(a):
    return minus(times(a[0], a[3]), times(a[1], a[2]))


def matrix_inverse(a, code="F02_GEOMETRY"):
    invdet = reciprocal(determinant(a), code)
    adjugate = (a[3], times_scalar(a[1], -1),
                times_scalar(a[2], -1), a[0])
    return tuple(times(entry, invdet) for entry in adjugate)


def symmetric(a):
    return a[1] == a[2]


def zero_positive(a):
    return all(x == 0 for x in a[1:])


def trim_state(state, n):
    return tuple(tuple(p[:n + 1] for p in group) for group in state)


def initial_state(g, pi, r, rho, n=ORDER):
    return tuple(matrix(group, n) for group in (g, pi, r, rho))


def field(state, kappa, root, code="F02_GEOMETRY",
          metric_binding=True, matter_binding=True):
    g, pi, r, rho = state
    inv = matrix_inverse(g, code)
    grho = matrix_vector(g, rho)
    energy = square_root(dot(rho, grho), root, code)
    invenergy = reciprocal(energy, code)
    ir = matrix_vector(inv, r)
    gdot = matrix_times(matrix_times(g, pi), g)
    pidot = matrix_scale(matrix_times(matrix_times(pi, g), pi), -1)
    pidot = matrix_minus(pidot,
                         tuple(times(x, times_scalar(invenergy, F(1, 2)))
                               for x in outer(rho, rho)))
    if metric_binding:
        pidot = matrix_plus(pidot, matrix_scale(outer(ir, ir), kappa))
    rdot = tuple(times(x, invenergy) for x in grho)
    rhodot = matrix_scale(ir, -2 * kappa) if matter_binding else matrix_scale(ir, 0)
    return (gdot, pidot, rdot, rhodot)


def solve(state0, kappa, root):
    """y_m = rhs_(m-1)/m; each right side sees only settled coefficients."""
    state = trim_state(state0, ORDER)
    for m in range(1, ORDER + 1):
        rhs = field(trim_state(state, m - 1), kappa, root)
        state = tuple(tuple(p[:m] + (q[m - 1] / m,) + p[m + 1:]
                            for p, q in zip(group, velocities))
                      for group, velocities in zip(state, rhs))
    return state


def invariants(state, kappa, root, code="F02_GEOMETRY"):
    g, pi, r, rho = state
    inv = matrix_inverse(g, code)
    gpi = matrix_times(g, pi)
    kinetic = times_scalar(trace(matrix_times(gpi, gpi)), F(1, 2))
    norm2 = dot(rho, matrix_vector(g, rho))
    energy = square_root(norm2, root, code)
    radius2 = dot(r, matrix_vector(inv, r))
    potential = times_scalar(radius2, kappa)
    charge = matrix_plus(matrix_scale(gpi, 2), outer(r, rho))
    charge_trace = trace(charge)
    delta = minus(determinant(charge),
                  times_scalar(times(charge_trace, charge_trace), F(1, 4)))
    return {
        "R": inv, "K": kinetic, "E": energy, "V": potential,
        "H": plus(plus(kinetic, energy), potential), "D": norm2,
        "d2": times_scalar(radius2, 4), "C": trace(gpi), "J": charge,
        "delta": delta, "gap": minus(times(norm2, potential),
                                       times_scalar(delta, 4 * kappa)),
        "z": dot(r, rho),
    }


def audit(state, kappa, root, expected_initial=None, override=None):
    def check(value, code):
        require(value, override or code)

    geom = override or "F02_GEOMETRY"
    g, pi, r, rho = state
    n = len(g[0]) - 1
    values = invariants(state, kappa, root, geom)
    inv = values["R"]
    check(symmetric(g) and symmetric(pi) and symmetric(inv), "F02_GEOMETRY")
    check(g[0][0] > 0 and determinant(g)[0] > 0, "F02_GEOMETRY")
    check(matrix_times(g, inv) == identity(n)
          and matrix_times(inv, g) == identity(n), "F02_GEOMETRY")
    check(times(values["E"], values["E"]) == values["D"], "F02_GEOMETRY")
    if expected_initial is not None:
        check(trim_state(state, 0) == trim_state(expected_initial, 0),
              "F02_GEOMETRY")
    rhs = field(state, kappa, root, geom)
    for group, velocities in zip(state, rhs):
        for p, q in zip(group, velocities):
            check(derivative(p) == q[:n], "F03_FLOW")

    grho = matrix_vector(g, rho)
    invenergy = reciprocal(values["E"], geom)
    exchange_a = times(times_scalar(dot(grho, matrix_vector(pi, grho)),
                                    F(1, 2)), invenergy)
    exchange_b = times_scalar(dot(r, matrix_vector(pi, r)), kappa)
    exchange_w = times(times_scalar(values["z"], 2 * kappa), invenergy)
    balances = (
        ("E", minus(exchange_a, exchange_w)),
        ("V", minus(exchange_w, exchange_b)),
        ("K", minus(exchange_b, exchange_a)),
        ("C", minus(values["V"], times_scalar(values["E"], F(1, 2)))),
        ("z", minus(values["E"], times_scalar(values["V"], 2))),
    )
    for name, rate in balances:
        check(derivative(values[name]) == rate[:n], "F04_EXCHANGE")
    check(zero_positive(values["H"]), "F04_EXCHANGE")
    check(all(zero_positive(entry) for entry in values["J"])
          and zero_positive(values["delta"]), "F05_CHARGE")
    check(values["D"] == times(values["E"], values["E"]), "F05_CHARGE")
    check(values["d2"] == times_scalar(values["V"], 4 / kappa), "F05_CHARGE")
    check(trace(values["J"]) == plus(times_scalar(values["C"], 2), values["z"]),
          "F05_CHARGE")

    j = values["J"]
    q = trace(matrix_times(matrix_times(matrix_times(inv, j), g), transpose(j)))
    identity_rhs = times_scalar(
        minus(plus(plus(times(values["z"], values["z"]),
                        trace(matrix_times(j, j))), q), times(trace(j), trace(j))),
        kappa)
    check(values["gap"] == identity_rhs, "F06_BOUND")
    check(values["gap"][0] >= 0, "F06_BOUND")
    e0, h0 = values["E"][0], values["H"][0]
    delta0, d20 = values["delta"][0], values["d2"][0]
    if delta0 > 0:
        check(e0 > 0 and e0 * e0 * h0 >= 4 * kappa * delta0
              and d20 * h0 * h0 >= 16 * delta0
              and d20 <= 4 * h0 / kappa, "F06_BOUND")
    return values


def directional_gradients(state, kappa, root):
    """Differentiate actual perturbed Hamiltonians in ten independent directions."""
    base = trim_state(state, 0)
    rhs = field(base, kappa, root)
    directions = ((F(1), F(0), F(0), F(0)),
                  (F(0), F(0), F(0), F(1)),
                  (F(0), F(1), F(1), F(0)))
    vector_directions = ((F(1), F(0)), (F(0), F(1)))
    # Hamiltonian gradients: (-Pidot, Gdot, -rhodot, rdot).
    gradients = (matrix_scale(rhs[1], -1), rhs[0],
                 matrix_scale(rhs[3], -1), rhs[2])
    for group_index in range(4):
        for direction in directions if group_index < 2 else vector_directions:
            perturbed = []
            for j, group in enumerate(base):
                perturbed.append(tuple((entry[0], direction[i] if j == group_index
                                        else F(0)) for i, entry in enumerate(group)))
            actual = invariants(tuple(perturbed), kappa, root)["H"][1]
            predicted = sum((entry[0] * weight for entry, weight
                             in zip(gradients[group_index], direction)), F(0))
            require(actual == predicted, "F03_FLOW")


def transform(state, entries):
    n = len(state[0][0]) - 1
    a = matrix(entries, n)
    ainv = matrix_inverse(a, "F07_COVARIANCE")
    g, pi, r, rho = state
    return (matrix_times(matrix_times(a, g), transpose(a)),
            matrix_times(matrix_times(transpose(ainv), pi), ainv),
            matrix_vector(a, r), matrix_vector(transpose(ainv), rho))


def group_exponential(omega, sign, n):
    o = matrix(omega, 0)
    power = identity(0)
    coefficients = [[] for _ in range(4)]
    factorial = 1
    for m in range(n + 1):
        if m:
            power = matrix_times(power, o)
            factorial *= m
        for i in range(4):
            coefficients[i].append(power[i][0] * F(sign ** m, factorial))
    return tuple(tuple(p) for p in coefficients)


def periodic_checks(kappa, initial, root, omega):
    state = solve(initial, kappa, root)
    values = audit(state, kappa, root, initial, "F08_PERIODIC")
    a = group_exponential(omega, 1, ORDER)
    ai = group_exponential(omega, -1, ORDER)
    g0, pi0, r0, rho0 = initial
    exact = (matrix_times(matrix_times(a, g0), transpose(a)),
             matrix_times(matrix_times(transpose(ai), pi0), ai),
             matrix_vector(a, r0), matrix_vector(transpose(ai), rho0))
    require(state == exact, "F08_PERIODIC")
    o = matrix(omega, 0)
    require(matrix_times(o, o) == matrix_scale(identity(0), -2), "F08_PERIODIC")
    base = trim_state(initial, 0)
    g, pi, r, rho = base
    generator = (
        matrix_plus(matrix_times(o, g), matrix_times(g, transpose(o))),
        matrix_scale(matrix_plus(matrix_times(transpose(o), pi),
                                 matrix_times(pi, o)), -1),
        matrix_vector(o, r), matrix_scale(matrix_vector(transpose(o), rho), -1))
    require(field(base, kappa, root) == generator, "F08_PERIODIC")
    require(o == matrix_scale(tuple(p[:1] for p in values["J"]), F(-1, 2)),
            "F08_PERIODIC")
    for name, expected in (("K", 1), ("E", 6), ("V", 3), ("H", 10),
                           ("D", 36), ("d2", 4), ("C", 0), ("delta", 8)):
        require(values[name] == constant(expected, ORDER), "F08_PERIODIC")
    require(values["J"] == matrix((0, 4, -2, 0), ORDER), "F08_PERIODIC")
    return state, values


def minimum_checks(state, values, kappa):
    _, pi, r, rho = trim_state(state, 0)
    rv = tuple(p[0] for p in r)
    qv = tuple(p[0] for p in rho)
    a = abs(rv[0] * qv[1] - rv[1] * qv[0]) / 2
    b = F(1)
    u = b / a
    delta = values["delta"][0]
    require(a == 3 and b > 0 and b * b == a * a - delta and u == F(1, 3),
            "F09_MINIMUM")
    require(delta * delta * (1 - u) ** 4
            == 64 * kappa * u ** 3 * (1 + u) ** 2, "F09_MINIMUM")
    require((values["E"][0] + values["V"][0]) ** 3 == 27 * kappa * a * a,
            "F09_MINIMUM")
    require(values["z"][0] == 0 and dot(r, r)[0] == 1 and dot(rho, rho)[0] == 36,
            "F09_MINIMUM")
    j = tuple(p[:1] for p in values["J"])
    rq = outer(r, rho)
    require(matrix_plus(j, transpose(j))
            == matrix_scale(matrix_plus(rq, transpose(rq)), F(1, 3)),
            "F09_MINIMUM")
    require(trace(j)[0] == 0
            and values["K"][0] == (a - b) ** 2 / 4, "F09_MINIMUM")
    c = F(1)
    require(c ** 3 == kappa / a, "F09_MINIMUM")
    bprime = a / b
    bsecond = 1 / b - a * a / b ** 3
    fprime = 2 * c + (a - b) * (1 - bprime) / 2
    fsecond = -2 * c / (3 * a) + ((1 - bprime) ** 2 - (a - b) * bsecond) / 2
    require(fprime == 0 and fsecond == F(88, 9), "F09_MINIMUM")
    displaced = initial_state((1, 0, 0, 1), tuple(p[0] for p in pi),
                              (2, 0), (0, 3), 0)
    dv = invariants(displaced, kappa, F(3), "F09_MINIMUM")
    require(dv["J"] == j and dv["delta"][0] == delta
            and dv["H"][0] == 16 and dv["H"][0] > values["H"][0], "F09_MINIMUM")
    return a, b, u, fsecond, displaced, dv


def tangent_invariants(initial, tangent, kappa, root):
    state = tuple(tuple((p[0], v[0]) for p, v in zip(group, velocity))
                  for group, velocity in zip(initial, tangent))
    return invariants(state, kappa, root, "F10_NEGATIVE_CONTROL")


def negative_controls(first_base, first_values, periodic_values,
                      displaced_values, pi_binding):
    detected = []

    def detected_if(number, condition):
        require(condition, "F10_NEGATIVE_CONTROL")
        detected.append("NC%02d" % number)

    s1 = initial_state((1, 0, 0, 1), (0, 0, 0, 0), (1, 0), (3, 4), 0)
    wrong = field(s1, F(1), F(5), metric_binding=False, matter_binding=False)
    wrong_values = tangent_invariants(s1, wrong, F(1), F(5))
    detected_if(1, wrong_values["H"][1] == F(6, 5)
                and wrong_values["H"][1] != 0)

    rho = matrix((0, 2), 0)
    plus_p = matrix_scale(rho, F(1, 2))
    minus_p = matrix_scale(rho, F(-1, 2))
    pair = square_root(dot(rho, rho), F(2), "F10_NEGATIVE_CONTROL")[0]
    eplus = square_root(dot(plus_p, plus_p), F(1), "F10_NEGATIVE_CONTROL")[0]
    eminus = square_root(dot(minus_p, minus_p), F(1), "F10_NEGATIVE_CONTROL")[0]
    detected_if(2, eplus + eminus == pair == 2 and eplus == 1 and eplus != pair)

    scaled = transform(first_base, (2, 0, 0, 2))
    sv = invariants(scaled, F(1), F(2), "F10_NEGATIVE_CONTROL")
    coord = times_scalar(dot(first_base[2], first_base[2]), 4)
    scaled_coord = times_scalar(dot(scaled[2], scaled[2]), 4)
    detected_if(3, sv["d2"] == first_values["d2"]
                and sv["H"] == first_values["H"]
                and scaled_coord == times_scalar(coord, 4)
                and scaled_coord[0] != coord[0])

    s4 = initial_state((1, 0, 0, 1), (0, 0, 0, 0), (1, 0), (0, 2), 0)
    v4 = invariants(s4, F(1), F(2), "F10_NEGATIVE_CONTROL")
    sb = initial_state((1, 0, 0, 1), pi_binding, (1, 0), (0, 2), 0)
    vb = invariants(sb, F(1), F(2), "F10_NEGATIVE_CONTROL")
    detected_if(4, v4["delta"][0] == 0 and vb["delta"][0] == 1)

    s5 = initial_state((1, 0, 0, 1), (1, 0, 0, 1), (1, 0), (0, 2), 0)
    v5 = invariants(s5, F(1), F(2), "F10_NEGATIVE_CONTROL")
    detj = determinant(v5["J"])[0]
    detected_if(5, v5["delta"][0] == 0 and detj == 4
                and v5["D"][0] * v5["V"][0] < 4 * detj)

    omitted = field(s5, F(1), F(2), metric_binding=False)
    omitted_values = tangent_invariants(s5, omitted, F(1), F(2))
    detected_if(6, omitted_values["H"][1] == -1 and omitted_values["H"][1] != 0)

    correct = field(s1, F(1), F(5))
    correct_values = tangent_invariants(s1, correct, F(1), F(5))
    detected_if(7, correct_values["E"][1] == F(-6, 5)
                and correct_values["V"][1] == F(6, 5)
                and correct_values["K"][1] == 0 and correct_values["E"][1] != 0)
    detected_if(8, periodic_values["delta"][0] == displaced_values["delta"][0] == 8
                and periodic_values["H"][0] == 10 and displaced_values["H"][0] == 16
                and periodic_values["H"][0] != displaced_values["H"][0])
    return detected


def scalar_text(value):
    return str(F(value))


def array_text(values):
    return ",".join(scalar_text(value) for value in values)


def coefficient_fields(state, values, m):
    fields = [array_text(p[m] for p in group) for group in state]
    fields.extend(scalar_text(values[name][m]) for name in ("K", "E", "V", "D", "d2", "C"))
    fields.append(array_text(p[m] for p in values["J"]))
    fields.extend(scalar_text(values[name][m]) for name in ("delta", "gap"))
    require(len(fields) == 13, "F11_PAYLOAD")
    return fields


def authority_check():
    root = Path(__file__).resolve().parents[2]
    count = 0
    for relative, size, digest in AUTHORITY:
        path = root / relative
        require(path.is_file(), "F01_AUTHORITY")
        content = path.read_bytes()
        require(len(content) == size and sha256(content).hexdigest() == digest,
                "F01_AUTHORITY")
        count += 1
    require(count == 5, "F01_AUTHORITY")
    return count


def certificate(authority_count):
    kappas = (F(1, 2), F(1), F(2))
    positions = ((F(1), F(0)), (F(2), F(0)))
    momenta = ((F(0), F(1)), (F(0), F(2)), (F(0), F(-2)),
               (F(3), F(4)), (F(3), F(-4)))
    roots = (F(1), F(2), F(2), F(5), F(5))
    half = F(1, 2)
    pis = ((F(0), F(0), F(0), F(0)),
           (F(0), -half, -half, F(0)),
           (F(0), half, half, F(0)),
           (half, -half, -half, F(0)),
           (F(0), -half, -half, -half),
           (half, F(-1), F(-1), -half),
           (-half, F(1), F(1), half))
    g0 = (F(1), F(0), F(0), F(1))
    records = []

    def emit(*fields):
        records.append("|".join(str(x) for x in fields))

    emit("G", array_text(g0))
    for bi, pi in enumerate(pis):
        emit("B", bi, array_text(pi))
    for qi, (rho, root) in enumerate(zip(momenta, roots)):
        emit("Q", qi, array_text(rho), scalar_text(root))
    for ri, r in enumerate(positions):
        emit("R", ri, array_text(r))
    for ki, kappa in enumerate(kappas):
        emit("K", ki, scalar_text(kappa))
    require(len(records) == 18, "F11_PAYLOAD")

    cases = {}
    signs = {"POS": 0, "ZERO": 0, "NEG": 0}
    rows = 0
    for ki, kappa in enumerate(kappas):
        for ri, r in enumerate(positions):
            for qi, (rho, root) in enumerate(zip(momenta, roots)):
                for bi, pi in enumerate(pis):
                    initial = initial_state(g0, pi, r, rho)
                    state = solve(initial, kappa, root)
                    values = audit(state, kappa, root, initial)
                    directional_gradients(initial, kappa, root)
                    delta0 = values["delta"][0]
                    sign = "POS" if delta0 > 0 else "NEG" if delta0 < 0 else "ZERO"
                    signs[sign] += 1
                    indices = (ki, ri, qi, bi)
                    cases[indices] = (state, values)
                    emit("C", *indices, scalar_text(kappa), scalar_text(delta0), sign)
                    for m in range(ORDER + 1):
                        emit("S", *indices, m, *coefficient_fields(state, values, m))
                        rows += 1
    require(len(cases) == 210 and sum(signs.values()) == len(cases)
            and all(count > 0 for count in signs.values()) and rows == 1050,
            "F11_PAYLOAD")

    base_indices = ((1, 0, 1, 1), (2, 1, 2, 6))
    changes = ((1, 1, 0, 1), (0, 1, 1, 0), (2, 0, 0, 1))
    covariance_count = 0
    for indices in base_indices:
        ki, _, qi, _ = indices
        original, original_values = cases[indices]
        for change in changes:
            moved = transform(original, change)
            moved_values = audit(moved, kappas[ki], roots[qi], override="F07_COVARIANCE")
            for name in ("K", "E", "V", "D", "d2", "C", "delta", "gap"):
                require(moved_values[name] == original_values[name], "F07_COVARIANCE")
            a = matrix(change, ORDER)
            jprime = matrix_times(matrix_times(a, original_values["J"]),
                                  matrix_inverse(a, "F07_COVARIANCE"))
            require(moved_values["J"] == jprime, "F07_COVARIANCE")
            emit("A", covariance_count, ",".join(str(i) for i in indices), array_text(change))
            for m in range(ORDER + 1):
                emit("Y", covariance_count, m, *coefficient_fields(moved, moved_values, m))
            covariance_count += 1
    require(covariance_count == 6, "F11_PAYLOAD")

    kstar = F(3)
    omega = (F(0), F(-2), F(1), F(0))
    periodic_initial = initial_state(g0, (0, -1, -1, 0), (1, 0), (0, 6))
    periodic, pv = periodic_checks(kstar, periodic_initial, F(6), omega)
    a, b, u, second, displaced, dv = minimum_checks(periodic, pv, kstar)
    emit("W", scalar_text(kstar), array_text(omega), scalar_text(a), scalar_text(b),
         scalar_text(u), scalar_text(second))
    periodic_count = 0
    for m in range(ORDER + 1):
        emit("T", m, *coefficient_fields(periodic, pv, m))
    periodic_count += 1
    emit("F", "RADIAL_DISPLACEMENT", *coefficient_fields(displaced, dv, 0))
    first_state, first_values = cases[base_indices[0]]
    controls = negative_controls(first_state, first_values, pv, dv, pis[1])
    for control in controls:
        emit("N", control, "DETECTED")
    require(periodic_count == 1 and len(controls) == 8 and len(set(controls)) == 8,
            "F11_PAYLOAD")
    require(len(records) == 1329 and all("\n" not in row and "\r" not in row
                                       for row in records), "F11_PAYLOAD")
    payload = ("\n".join(records) + "\n").encode("ascii")
    require(payload.count(b"\n") == len(records), "F11_PAYLOAD")
    lines = (
        "CERTIFICATE=" + PROBE,
        "AUTHORITY_FILES=" + str(authority_count),
        "COUPLINGS=" + str(len(kappas)),
        "SEPARATIONS=" + str(len(positions)),
        "MOMENTA=" + str(len(momenta)),
        "METRIC_MOMENTA=" + str(len(pis)),
        "TRAJECTORY_CASES=" + str(len(cases)),
        "ELLIPTIC_CASES=" + str(signs["POS"]),
        "PARABOLIC_CASES=" + str(signs["ZERO"]),
        "HYPERBOLIC_CASES=" + str(signs["NEG"]),
        "FORMAL_ORDER=" + str(ORDER),
        "COEFFICIENT_ROWS=" + str(rows),
        "COVARIANCE_CASES=" + str(covariance_count),
        "PERIODIC_CASES=" + str(periodic_count),
        "NEGATIVE_CONTROLS=" + str(len(controls)),
        "PAYLOAD_RECORDS=" + str(len(records)),
        "PAYLOAD_SHA256=" + sha256(payload).hexdigest(),
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 18, "F11_PAYLOAD")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        authority_count = authority_check()
        common = certificate(authority_count)
        try:
            result = subprocess.run(
                [sys.executable, "-I", str(Path(__file__).resolve().with_name("breaker.py"))],
                shell=False, stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                cwd=Path(__file__).resolve().parents[2],
                env={"LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1",
                     "PYTHONHASHSEED": "0", "TZ": "UTC"},
                timeout=540, check=False)
        except subprocess.TimeoutExpired:
            raise AuditFailure("F12_BREAKER") from None
        require(result.returncode == 0 and result.stderr == b""
                and result.stdout == common, "F12_BREAKER")
    except AuditFailure as failure:
        sys.stdout.buffer.write(("FALSIFIER=" + str(failure) + "\nRESULT=FAIL\n").encode("ascii"))
        return
    sys.stdout.buffer.write(common + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")


if __name__ == "__main__":
    main()
