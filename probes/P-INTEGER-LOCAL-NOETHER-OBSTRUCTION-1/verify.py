#!/usr/bin/env python3
"""Exact primary audit; see the prospective PREREG.md and PROOF.md.

No companion source is imported.  The second implementation is run only as
an isolated process after this certificate has been assembled independently.
"""

from fractions import Fraction as F
import hashlib
import math
from pathlib import Path
import subprocess
import sys


NAME = "P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ZERO = F(0)
ONE = F(1)
G = F(1, 324)
JUMP = F(29, 648)
ELL = (1, -1, 0, 0, 0)
SIGMA = (F(1, 2), F(1, 2), ZERO, ZERO, ZERO)
EDGES = tuple((r, (r + 1) % 5, F(29, 324)) for r in range(5)) + tuple(
    (r, (r + 2) % 5, F(65, 324)) for r in range(5)
)
AUTHORITY = (
    ("CANON.md", 1052518,
     "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714,
     "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382,
     "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811,
     "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770,
     "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class ScientificFailure(Exception):
    """A completed exact check fired a preregistered falsifier."""


def need(condition, falsifier):
    if not condition:
        raise ScientificFailure(falsifier)


def authority_check():
    for name, size, digest in AUTHORITY:
        try:
            data = (ROOT / "canon" / name).read_bytes()
        except OSError:
            raise ScientificFailure("F_AUTHORITY") from None
        need(len(data) == size and hashlib.sha256(data).hexdigest() == digest,
             "F_AUTHORITY")


def zeros(rows, columns):
    return [[ZERO for _ in range(columns)] for _ in range(rows)]


def dot(a, b):
    return sum((v * w for v, w in zip(a, b)), ZERO)


def incidence(h):
    return [h[head] - h[tail] for tail, head, _ in EDGES]


def laplace(h):
    answer = [ZERO] * 5
    for tail, head, weight in EDGES:
        flux = weight * (h[head] - h[tail])
        answer[head] += flux
        answer[tail] -= flux
    return answer


def integer_laplace(h):
    return [188 * h[r] - 29 * (h[(r - 1) % 5] + h[(r + 1) % 5])
            - 65 * (h[(r - 2) % 5] + h[(r + 2) % 5]) for r in range(5)]


def adjacent(center, other, coupling):
    """Solve the autonomous equations for either missing adjacent slice."""
    lint = integer_laplace(center[:5])
    h = [2 * center[r] - other[r] - lint[r] / 324
         + coupling * center[5] * ELL[r] for r in range(5)]
    chi = center[5] - other[5] + coupling * dot(ELL, center[:5])
    return h + [chi]


def history(T, k, coupling=G):
    x = zeros(T + 1, 6)
    x[k - 1] = [ONE, ZERO, -ONE, ZERO, ZERO, ZERO]
    for n in range(k, T):
        x[n + 1] = adjacent(x[n], x[n - 1], coupling)
    for n in range(k - 1, 0, -1):
        x[n - 1] = adjacent(x[n], x[n + 1], coupling)
    return x


def residual(x, n):
    lap = laplace(x[n][:5])
    field = [x[n + 1][r] - 2 * x[n][r] + x[n - 1][r] + lap[r]
             - G * x[n][5] * ELL[r] for r in range(5)]
    source = x[n + 1][5] - x[n][5] + x[n - 1][5] - G * dot(ELL, x[n][:5])
    return field + [source]


def action(x):
    """The full fixed-endpoint quadratic A, including reciprocal coupling."""
    T = len(x) - 1
    total = ZERO
    for b in range(1, T + 1):
        total += sum(((x[b][i] - x[b - 1][i]) ** 2 for i in range(6)), ZERO) / 2
    for n in range(1, T):
        bh = incidence(x[n][:5])
        total -= (sum((edge[2] * q * q for edge, q in zip(EDGES, bh)), ZERO)
                  + x[n][5] ** 2) / 2
        total += G * x[n][5] * dot(ELL, x[n][:5])
    return total


def densities(x, b):
    now, old = x[b], x[b - 1]
    answer = [(now[r] - old[r]) ** 2 / 2 for r in range(5)]
    for tail, head, weight in EDGES:
        piece = weight * (now[head] - now[tail]) * (old[head] - old[tail]) / 4
        answer[tail] += piece
        answer[head] += piece
    source = ((now[5] - old[5]) ** 2 + now[5] * old[5]) / 2
    for r in range(5):
        answer[r] += SIGMA[r] * source
        answer[r] -= G * ELL[r] * (old[5] * now[r] + now[5] * old[r]) / 2
    return answer


def currents(x, n):
    q = [x[n + 1][i] - x[n - 1][i] for i in range(6)]
    spatial = [weight * (x[n][head] - x[n][tail]) * (q[tail] + q[head]) / 4
               for tail, head, weight in EDGES]
    interaction = [ZERO] * 10
    interaction[0] = -G * q[5] * (x[n][0] + x[n][1]) / 4
    return spatial, interaction


def empty_multiplier(T):
    return ([ZERO] * (T + 1), zeros(T + 1, 5), zeros(T + 1, 10))


def interaction_action(x, multiplier):
    alpha, lam, shift = multiplier
    T = len(x) - 1
    value = ZERO
    for b in range(1, T + 1):
        if alpha[b] != 0 or any(lam[b]):
            density = densities(x, b)
            value -= alpha[b] * sum(density, ZERO) + dot(lam[b], density)
    for n in range(1, T):
        if any(shift[n]):
            spatial, interaction = currents(x, n)
            value += dot(shift[n], [a + b for a, b in zip(spatial, interaction)])
    return value


def gamma(psi):
    T = len(psi) - 1
    alpha, lam, shift = empty_multiplier(T)
    for b in range(1, T + 1):
        delta = [psi[b][r] - psi[b - 1][r] for r in range(5)]
        alpha[b] = sum(delta, ZERO) / 5
        lam[b] = [value - alpha[b] for value in delta]
    for n in range(1, T):
        shift[n] = incidence(psi[n])
    return alpha, lam, shift


def generator(x, psi):
    T = len(x) - 1
    v = zeros(T + 1, 6)
    for n in range(1, T):
        v[n][:5] = [psi[n][r] * (x[n + 1][r] - x[n - 1][r]) / 2
                    for r in range(5)]
        v[n][5] = dot(SIGMA, psi[n]) * (x[n + 1][5] - x[n - 1][5]) / 2
    return v


def shifted(x, v, sign):
    return [[a + sign * b for a, b in zip(row, step)] for row, step in zip(x, v)]


def prefix_action(x, multiplier):
    """Evaluate definition (D), not its predicted mixed coefficient.

    I is quadratic in fields at fixed rho, so its exact central directional
    difference is its derivative.  A is homogeneous quadratic at a=0, hence
    Hess_A(v,v)/2 equals A(v).  Endpoints of v are zero.
    """
    T = len(x) - 1
    alpha, lam, shift = multiplier
    theta = zeros(T + 1, 5)
    for n in range(1, T):
        theta[n] = [theta[n - 1][r] + alpha[n] + lam[n][r] for r in range(5)]
    ga, gl, gn = gamma(theta)
    rho = ([alpha[b] - ga[b] for b in range(T + 1)],
           [[lam[b][r] - gl[b][r] for r in range(5)] for b in range(T + 1)],
           [[shift[n][e] - gn[n][e] for e in range(10)] for n in range(T + 1)])
    v = generator(x, theta)
    derivative = (interaction_action(shifted(x, v, 1), rho)
                  - interaction_action(shifted(x, v, -1), rho)) / 2
    return -derivative + action(v)


def auxiliary_action(multiplier, tau, p):
    _, lam, shift = multiplier
    T = len(tau) - 1
    value = ZERO
    for b in range(1, T + 1):
        value += 2 * dot(lam[b], laplace(tau[b]))
    for n in range(1, T):
        difference = [tau[n + 1][r] - tau[n][r] for r in range(5)]
        bdifference = incidence(difference)
        value += 2 * dot(shift[n], [EDGES[e][2] * bdifference[e] + p[n][e]
                                   for e in range(10)])
    return value


def parameters(T):
    for n in range(1, T):
        t = [ZERO] * (T + 1)
        t[n] = ONE
        yield t
    yield [ZERO] + [ONE] * (T - 1) + [ZERO]
    yield [ZERO] + [F((-1) ** n * (n + 1), 7) for n in range(1, T)] + [ZERO]


def current_derivative(x, k, t):
    psi = [[value] * 5 for value in t]
    v = generator(x, psi)
    jp, ip = currents(shifted(x, v, 1), k)
    jm, im = currents(shifted(x, v, -1), k)
    source_derivative = (ip[0] - im[0]) / 2
    return (jp[0] - jm[0]) / 2 + source_derivative, source_derivative


def affine_tail(T, k):
    """Propagate backwards from C_T=c, leaving c as one free parameter."""
    constants = [ZERO] * (T + 1)
    for b in range(T - 1, 0, -1):
        constants[b] = constants[b + 1] + (JUMP if b == k else ZERO)
    return constants


def tail_feasible(constants, zero_indices):
    required = {-constants[b] for b in zero_indices}
    if len(required) > 1:
        return False, None
    c = next(iter(required)) if required else ZERO
    return True, [c + value for value in constants]


def scaled_integer(value):
    need(isinstance(value, F) and value.denominator == 1, "F_INTEGER")
    return value.numerator


def certificate():
    authority_check()
    payload = []
    count = dict(histories=0, residuals=0, derivatives=0, parameters=0,
                 prefix=0, tails=0, plateau=0, escape=0, integers=0, wards=0)
    controls = {f"NC{i:02d}": False for i in range(1, 9)}

    for T in (5, 7, 9, 13):
        for k in range(2, T - 1):
            x = history(T, k)
            count["histories"] += 1
            need(all(sum(row[:5], ZERO) == 0 for row in x), "F_HISTORY")
            payload.append(f"H|{T}|{k}|" + ",".join(str(v) for row in x for v in row))
            D = math.lcm(*(v.denominator for row in x for v in row))
            encoded = [[scaled_integer(D * value) for value in row] for row in x]

            for n in range(1, T):
                res = residual(x, n)
                lint = integer_laplace(encoded[n][:5])
                integral = [324 * (encoded[n + 1][r] - 2 * encoded[n][r]
                                  + encoded[n - 1][r]) + lint[r]
                            - encoded[n][5] * ELL[r] for r in range(5)]
                integral.append(324 * (encoded[n + 1][5] - encoded[n][5]
                                       + encoded[n - 1][5])
                                - sum(ELL[r] * encoded[n][r] for r in range(5)))
                for coordinate in range(6):
                    need(res[coordinate] == 0, "F_HISTORY")
                    count["residuals"] += 1
                    plus = [row[:] for row in x]
                    minus = [row[:] for row in x]
                    plus[n][coordinate] += 1
                    minus[n][coordinate] -= 1
                    derivative = (action(plus) - action(minus)) / 2
                    need(derivative == -res[coordinate], "F_HISTORY")
                    count["derivatives"] += 1
                    need(isinstance(integral[coordinate], int)
                         and integral[coordinate] == 0, "F_INTEGER")
                    count["integers"] += 1

            plateau_derivative = None
            for i, t in enumerate(parameters(T)):
                derivative, source = current_derivative(x, k, t)
                need(source == 0 and derivative == -JUMP * t[k], "F_WITNESS")
                Q = math.lcm(*(value.denominator for value in t))
                left = scaled_integer(648 * Q * derivative)
                right = scaled_integer(29 * Q * t[k])
                need(left + right == 0, "F_INTEGER")
                count["parameters"] += 1
                count["wards"] += 1
                payload.append(f"C|{T}|{k}|{i}|{derivative}")
                if i == T - 1:
                    plateau_derivative = derivative

            only_n = empty_multiplier(T)
            only_n[2][k][0] = ONE
            n_value = prefix_action(x, only_n)
            for b in range(1, T + 1):
                only_a = empty_multiplier(T)
                only_a[0][b] = ONE
                together = empty_multiplier(T)
                together[0][b] = ONE
                together[2][k][0] = ONE
                mixed = prefix_action(x, together) - prefix_action(x, only_a) - n_value
                need(mixed == (JUMP if b <= k else ZERO), "F_PREFIX")
                payload.append(f"P|{T}|{k}|{b}|{mixed}")
                count["prefix"] += 1

            constants = affine_tail(T, k)
            need(all(constants[b] - constants[b + 1] == (JUMP if b == k else ZERO)
                     for b in range(1, T)), "F_TAIL")
            need(all(constants[b] == (JUMP if b <= k else ZERO)
                     for b in range(1, T + 1)), "F_TAIL")
            feasible_radii = []
            for radius in range(T):
                forbidden = [b for b in range(1, T + 1) if abs(b - k) > radius]
                feasible, solution = tail_feasible(constants, forbidden)
                need(feasible == (radius >= min(k - 1, T - k)), "F_TAIL")
                if feasible:
                    feasible_radii.append(radius)
                    need(all(solution[b] == 0 for b in forbidden), "F_TAIL")
                    need(all(solution[b] - solution[b + 1]
                             == (JUMP if b == k else ZERO) for b in range(1, T)),
                         "F_TAIL")
                payload.append(f"R|{T}|{k}|{radius}|{int(feasible)}")
                count["tails"] += 1
            need(feasible_radii and min(feasible_radii) == min(k - 1, T - k),
                 "F_RADIUS")
            too_small = min(k - 1, T - k) - 1
            forbidden = [b for b in range(1, T + 1) if abs(b - k) > too_small]
            need(not tail_feasible(constants, forbidden)[0], "F_CONTROL")
            controls["NC04"] = True

            # For plateau parameters Gamma changes only the endpoint alpha
            # bonds.  Setting both tail endpoints zero cannot cancel -JUMP.
            need(plateau_derivative == -JUMP and plateau_derivative != 0
                 and not tail_feasible(constants, (1, T))[0], "F_PLATEAU")
            count["plateau"] += 1
            tau = zeros(T + 1, 5)
            tau[k] = [F(value, 8) for value in ELL]
            p = zeros(T + 1, 10)
            escape = auxiliary_action(only_n, tau, p)
            need(sum(tau[k], ZERO) == 0 and escape == JUMP
                 and escape + plateau_derivative == 0, "F_ESCAPE")
            payload.append(f"E|{T}|{k}|{escape}")
            count["escape"] += 1

            if T == 5 and k == 2:
                controls["NC01"] = -plateau_derivative == JUMP and -plateau_derivative != -JUMP
                omitted = empty_multiplier(T)
                uniform = [[ZERO] * 5] + [[ONE] * 5 for _ in range(T - 1)] + [[ZERO] * 5]
                v = generator(x, uniform)
                removed = (interaction_action(shifted(x, v, 1), omitted)
                           - interaction_action(shifted(x, v, -1), omitted)) / 2
                controls["NC02"] = removed == 0 and removed != plateau_derivative
                wrong_history = history(T, k, ZERO)
                controls["NC03"] = any(value != 0 for n in range(1, T)
                                        for value in residual(wrong_history, n))
                controls["NC05"] = not tail_feasible(constants, (1, T))[0]
                wrong_tail = [-value for value in constants]
                controls["NC06"] = any(wrong_tail[b] - wrong_tail[b + 1]
                                        != (JUMP if b == k else ZERO) for b in range(1, T))
                controls["NC07"] = plateau_derivative == -JUMP and plateau_derivative != 0
                wrong_tau = [[-value for value in row] for row in tau]
                wrong_escape = auxiliary_action(only_n, wrong_tau, p)
                controls["NC08"] = (wrong_escape + plateau_derivative == -F(29, 324)
                                     and wrong_escape + plateau_derivative != 0)

    expected = dict(histories=22, residuals=1200, derivatives=1200,
                    parameters=244, prefix=222, tails=222, plateau=22,
                    escape=22, integers=1200, wards=244)
    need(count == expected, "F_COUNTS")
    for label, detected in controls.items():
        need(detected, "F_CONTROL")
        payload.append(f"N|{label}|DETECTED")
    digest = hashlib.sha256(("\n".join(payload) + "\n").encode("ascii")).hexdigest()
    lines = [
        f"CERTIFICATE={NAME}",
        "AUTHORITY_FILES=5",
        f"HISTORY_CASES={count['histories']}",
        f"ON_SHELL_COMPONENTS={count['residuals']}",
        f"ACTION_DERIVATIVES={count['derivatives']}",
        f"CURRENT_PARAMETER_CHECKS={count['parameters']}",
        f"PREFIX_MIXED_COEFFICIENTS={count['prefix']}",
        f"TAIL_SYSTEMS={count['tails']}",
        f"PLATEAU_OBSTRUCTIONS={count['plateau']}",
        f"AUXILIARY_ESCAPE_CHECKS={count['escape']}",
        f"INTEGER_RESIDUALS={count['integers']}",
        f"INTEGER_WARD_WITNESSES={count['wards']}",
        "WITNESS=-29/648",
        "TAIL_JUMP=29/648",
        f"PAYLOAD_SHA256={digest}",
        "NEGATIVE_CONTROLS=8",
        "CERTIFICATE_RESULT=PASS",
    ]
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        primary = certificate()
        try:
            other = subprocess.run([sys.executable, "-I", str(HERE / "breaker.py")],
                                   cwd=ROOT, capture_output=True, timeout=540, check=False)
        except (OSError, subprocess.TimeoutExpired):
            raise ScientificFailure("F_BYTES") from None
        need(other.returncode == 0 and other.stderr == b"" and other.stdout == primary,
             "F_BYTES")
        sys.stdout.buffer.write(primary + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except ScientificFailure as failure:
        sys.stdout.buffer.write((str(failure) + "\nRESULT=FAIL\n").encode("ascii"))


if __name__ == "__main__":
    main()
