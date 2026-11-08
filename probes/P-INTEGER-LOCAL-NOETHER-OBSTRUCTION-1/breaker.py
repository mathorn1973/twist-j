#!/usr/bin/env python3
"""Independent exact audit of the frozen local-Noether obstruction.

This implementation is derived from PREREG.md.  It reads no other probe,
imports no companion code, and assembles the action Hessian from its
quadratic summands.  First variations use rational dual arithmetic, and
the tail systems use full rational reduced row echelon form.
"""

from fractions import Fraction as F
from hashlib import sha256
from math import lcm
from pathlib import Path
import sys


ZERO = F(0)
ONE = F(1)
G = F(1, 324)
JUMP = F(29, 648)
ELL = (1, -1, 0, 0, 0)
SIGMA = (F(1, 2), F(1, 2), ZERO, ZERO, ZERO)
HORIZONS = (5, 7, 9, 13)
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
    """A completed exact check fired one frozen scientific falsifier."""


def require(condition, falsifier):
    if not condition:
        raise ScientificFailure(falsifier)


class Dual:
    """A rational value and its exact first directional coefficient."""

    __slots__ = ("value", "tangent")

    def __init__(self, value, tangent=ZERO):
        self.value = F(value)
        self.tangent = F(tangent)

    @staticmethod
    def lift(value):
        return value if isinstance(value, Dual) else Dual(value)

    def __add__(self, other):
        other = self.lift(other)
        return Dual(self.value + other.value, self.tangent + other.tangent)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.tangent)

    def __sub__(self, other):
        return self + -self.lift(other)

    def __rsub__(self, other):
        return self.lift(other) + -self

    def __mul__(self, other):
        other = self.lift(other)
        return Dual(self.value * other.value,
                    self.tangent * other.value + self.value * other.tangent)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        return Dual(self.value / other.value,
                    (self.tangent * other.value - self.value * other.tangent)
                    / (other.value * other.value))


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), ZERO)


def laplacian_integer(h):
    """The explicit frozen circulant, independent of the Hessian assembly."""
    return [188 * h[r] - 29 * (h[(r - 1) % 5] + h[(r + 1) % 5])
            - 65 * (h[(r - 2) % 5] + h[(r + 2) % 5]) for r in range(5)]


def build_history(T, k, coupling=G):
    history = [None] * (T + 1)
    history[k - 1] = [ONE, ZERO, -ONE, ZERO, ZERO, ZERO]
    history[k] = [ZERO] * 6

    def adjacent(center, known):
        lh = laplacian_integer(center[:5])
        h = [2 * center[r] - known[r] - lh[r] / 324
             + coupling * center[5] * ELL[r] for r in range(5)]
        chi = center[5] - known[5] + coupling * dot(ELL, center[:5])
        return h + [chi]

    for n in range(k, T):
        history[n + 1] = adjacent(history[n], history[n - 1])
    for n in range(k - 1, 0, -1):
        history[n - 1] = adjacent(history[n], history[n + 1])
    return history


def residuals(history):
    result = []
    for n in range(1, len(history) - 1):
        previous, center, following = history[n - 1:n + 2]
        lh = laplacian_integer(center[:5])
        result.append([
            following[r] - 2 * center[r] + previous[r] + lh[r] / 324
            - G * center[5] * ELL[r] for r in range(5)
        ] + [following[5] - center[5] + previous[5]
             - G * dot(ELL, center[:5])])
    return result


def assemble_action_hessian(T):
    """Expand A's kinetic squares, weighted edge squares and cross terms."""
    rows = [dict() for _ in range(6 * (T + 1))]

    def add(i, j, coefficient):
        rows[i][j] = rows[i].get(j, ZERO) + coefficient

    def square(i, j, coefficient):
        # Hessian of coefficient * (x_i-x_j)^2 / 2.
        add(i, i, coefficient)
        add(j, j, coefficient)
        add(i, j, -coefficient)
        add(j, i, -coefficient)

    for b in range(1, T + 1):
        for coordinate in range(6):
            square(6 * b + coordinate, 6 * (b - 1) + coordinate, ONE)
    for n in range(1, T):
        for tail, head, weight in EDGES:
            square(6 * n + head, 6 * n + tail, -weight)
        add(6 * n + 5, 6 * n + 5, -ONE)
        for r in range(5):
            add(6 * n + r, 6 * n + 5, G * ELL[r])
            add(6 * n + 5, 6 * n + r, G * ELL[r])
    return rows


def flatten(history):
    return [coordinate for field in history for coordinate in field]


def hessian_apply(hessian, vector):
    return [sum((coefficient * vector[j] for j, coefficient in row.items()), ZERO)
            for row in hessian]


def transform(history, psi):
    T = len(history) - 1
    variation = [[ZERO] * 6 for _ in range(T + 1)]
    for n in range(1, T):
        q = [history[n + 1][r] - history[n - 1][r] for r in range(6)]
        variation[n] = [psi[n][r] * q[r] / 2 for r in range(5)] + [
            dot(SIGMA, psi[n]) * q[5] / 2
        ]
    return variation


def dual_history(history, variation):
    return [[Dual(x, dx) for x, dx in zip(field, delta)]
            for field, delta in zip(history, variation)]


def bond_density(previous, following):
    density = [(following[r] - previous[r]) * (following[r] - previous[r]) / 2
               for r in range(5)]
    for tail, head, weight in EDGES:
        term = weight * (following[head] - following[tail]) * (
            previous[head] - previous[tail]) / 4
        density[tail] += term
        density[head] += term
    chi_previous, chi_following = previous[5], following[5]
    chi_delta = chi_following - chi_previous
    for r in range(5):
        density[r] += SIGMA[r] * (chi_delta * chi_delta / 2
                                  + chi_following * chi_previous / 2)
        density[r] -= G * ELL[r] * (
            chi_previous * following[r] + chi_following * previous[r]) / 2
    return density


def currents(history, n):
    previous, center, following = history[n - 1:n + 2]
    q = [following[r] - previous[r] for r in range(6)]
    field_current = [weight * (center[head] - center[tail]) *
                     (q[tail] + q[head]) / 4 for tail, head, weight in EDGES]
    interaction = [-G * q[5] * (center[0] + center[1]) / 4] + [ZERO] * 9
    return field_current, interaction


def multipliers(T):
    return {"alpha": [ZERO] * (T + 1),
            "lambda": [[ZERO] * 5 for _ in range(T + 1)],
            "N": [[ZERO] * 10 for _ in range(T + 1)]}


def gamma(psi):
    T = len(psi) - 1
    result = multipliers(T)
    for b in range(1, T + 1):
        difference = [psi[b][r] - psi[b - 1][r] for r in range(5)]
        mean = sum(difference, ZERO) / 5
        result["alpha"][b] = mean
        result["lambda"][b] = [value - mean for value in difference]
    for n in range(1, T):
        result["N"][n] = [psi[n][head] - psi[n][tail]
                           for tail, head, _ in EDGES]
    return result


def derivative_interaction(history, multiplier, variation):
    """Evaluate the complete I in Q[epsilon]/(epsilon^2), at E_hom=0."""
    T = len(history) - 1
    x = dual_history(history, variation)
    value = Dual(ZERO)
    for b in range(1, T + 1):
        density = bond_density(x[b - 1], x[b])
        value -= multiplier["alpha"][b] * sum(density, ZERO)
        value -= dot(multiplier["lambda"][b], density)
    for n in range(1, T):
        field_current, interaction = currents(x, n)
        value += dot(multiplier["N"][n],
                     [a + b for a, b in zip(field_current, interaction)])
    return value.tangent


def prefix_action(history, multiplier, hessian):
    T = len(history) - 1
    theta = [[ZERO] * 5 for _ in range(T + 1)]
    for n in range(1, T):
        theta[n] = [theta[n - 1][r] + multiplier["alpha"][n]
                    + multiplier["lambda"][n][r] for r in range(5)]
    gamma_theta = gamma(theta)
    rho = multipliers(T)
    for b in range(1, T + 1):
        rho["alpha"][b] = multiplier["alpha"][b] - gamma_theta["alpha"][b]
        rho["lambda"][b] = [a - b for a, b in zip(
            multiplier["lambda"][b], gamma_theta["lambda"][b])]
    for n in range(1, T):
        rho["N"][n] = [a - b for a, b in zip(
            multiplier["N"][n], gamma_theta["N"][n])]
    variation = transform(history, theta)
    vector = flatten(variation)
    return -derivative_interaction(history, rho, variation) + dot(
        vector, hessian_apply(hessian, vector)) / 2


def current_variation(history, k, t):
    psi = [[value] * 5 for value in t]
    variation = transform(history, psi)
    field_current, interaction = currents(dual_history(history, variation), k)
    field_derivative = Dual.lift(field_current[0]).tangent
    interaction_derivative = Dual.lift(interaction[0]).tangent
    return field_derivative + interaction_derivative, interaction_derivative


def parameters(T):
    result = []
    for n in range(1, T):
        t = [ZERO] * (T + 1)
        t[n] = ONE
        result.append(t)
    result.append([ZERO] + [ONE] * (T - 1) + [ZERO])
    result.append([ZERO] + [F((-1) ** n * (n + 1), 7)
                            for n in range(1, T)] + [ZERO])
    return result


def tail_rows(T, k):
    rows = []
    for b in range(1, T):
        row = [ZERO] * (T + 1)
        row[b - 1], row[b] = ONE, -ONE
        row[T] = JUMP if b == k else ZERO
        rows.append(row)
    return rows


def zero_coordinate_row(T, b):
    row = [ZERO] * (T + 1)
    row[b - 1] = ONE
    return row


def rref(rows, variables):
    """Full exact Gauss-Jordan elimination, including all locality rows."""
    reduced = [[F(value) for value in row] for row in rows]
    pivots = []
    rank = 0
    for column in range(variables):
        candidate = next((r for r in range(rank, len(reduced))
                          if reduced[r][column] != 0), None)
        if candidate is None:
            continue
        reduced[rank], reduced[candidate] = reduced[candidate], reduced[rank]
        scale = reduced[rank][column]
        reduced[rank] = [entry / scale for entry in reduced[rank]]
        for r in range(len(reduced)):
            if r == rank or reduced[r][column] == 0:
                continue
            factor = reduced[r][column]
            reduced[r] = [entry - factor * pivot_entry for entry, pivot_entry
                          in zip(reduced[r], reduced[rank])]
        pivots.append(column)
        rank += 1
    feasible = all(any(row[:variables]) or row[variables] == 0 for row in reduced)
    return feasible, reduced, pivots


def local_system(T, k, radius):
    rows = tail_rows(T, k)
    rows.extend(zero_coordinate_row(T, b) for b in range(1, T + 1)
                if abs(b - k) > radius)
    return rref(rows, T)[0]


def auxiliary_variation(T, k, sign=ONE):
    """Differentiate B_aux in the explicitly supplied tau direction."""
    multiplier = multipliers(T)
    multiplier["N"][k][0] = ONE
    delta_tau = [[ZERO] * 5 for _ in range(T + 1)]
    delta_tau[k] = [sign * F(value, 8) for value in ELL]
    result = ZERO
    for b in range(1, T + 1):
        ldelta = [value / 324 for value in laplacian_integer(delta_tau[b])]
        result += 2 * dot(multiplier["lambda"][b], ldelta)
    for n in range(1, T):
        delta = [delta_tau[n + 1][r] - delta_tau[n][r] for r in range(5)]
        wb_delta = [weight * (delta[head] - delta[tail])
                    for tail, head, weight in EDGES]
        result += 2 * dot(multiplier["N"][n], wb_delta)
    return result


def authority_check():
    root = Path(__file__).resolve().parents[2]
    for name, size, expected_hash in AUTHORITY:
        try:
            data = (root / "canon" / name).read_bytes()
        except OSError:
            raise ScientificFailure("F_AUTHORITY") from None
        require(len(data) == size and sha256(data).hexdigest() == expected_hash,
                "F_AUTHORITY")


def run():
    authority_check()
    counts = {key: 0 for key in (
        "HISTORY_CASES", "ON_SHELL_COMPONENTS", "ACTION_DERIVATIVES",
        "CURRENT_PARAMETER_CHECKS", "PREFIX_MIXED_COEFFICIENTS", "TAIL_SYSTEMS",
        "PLATEAU_OBSTRUCTIONS", "AUXILIARY_ESCAPE_CHECKS", "INTEGER_RESIDUALS",
        "INTEGER_WARD_WITNESSES")}
    payload = []
    all_undersized_detected = True
    for T in HORIZONS:
        hessian = assemble_action_hessian(T)
        for k in range(2, T - 1):
            history = build_history(T, k)
            counts["HISTORY_CASES"] += 1
            payload.append("H|{}|{}|{}\n".format(T, k, ",".join(map(str, flatten(history)))))
            residual = residuals(history)
            gradient = hessian_apply(hessian, flatten(history))
            for field in history:
                require(sum(field[:5], ZERO) == 0, "F_HISTORY")
            for n in range(1, T):
                for coordinate in range(6):
                    require(residual[n - 1][coordinate] == 0, "F_HISTORY")
                    counts["ON_SHELL_COMPONENTS"] += 1
                    require(gradient[6 * n + coordinate] == -residual[n - 1][coordinate],
                            "F_HISTORY")
                    counts["ACTION_DERIVATIVES"] += 1

            denominator = lcm(*(value.denominator for value in flatten(history)))
            require(denominator > 0, "F_INTEGER")
            encoded = [[denominator * value for value in field] for field in history]
            require(all(value.denominator == 1 for value in flatten(encoded)), "F_INTEGER")
            for n in range(1, T):
                lh = laplacian_integer(encoded[n][:5])
                integer_residual = [
                    324 * (encoded[n + 1][r] - 2 * encoded[n][r] + encoded[n - 1][r])
                    + lh[r] - encoded[n][5] * ELL[r] for r in range(5)
                ] + [324 * (encoded[n + 1][5] - encoded[n][5] + encoded[n - 1][5])
                     - dot(ELL, encoded[n][:5])]
                for value in integer_residual:
                    require(value.denominator == 1 and value == 0, "F_INTEGER")
                    counts["INTEGER_RESIDUALS"] += 1

            parameter_list = parameters(T)
            for index, t in enumerate(parameter_list):
                derivative, interaction = current_variation(history, k, t)
                require(derivative == -JUMP * t[k] and interaction == 0, "F_WITNESS")
                counts["CURRENT_PARAMETER_CHECKS"] += 1
                parameter_denominator = lcm(*(value.denominator for value in t))
                ward_left = 648 * parameter_denominator * derivative
                ward_right = 29 * parameter_denominator * t[k]
                require(ward_left.denominator == 1 and ward_right.denominator == 1
                        and ward_left + ward_right == 0, "F_INTEGER")
                counts["INTEGER_WARD_WITNESSES"] += 1
                payload.append(f"C|{T}|{k}|{index}|{derivative}\n")

            for b in range(1, T + 1):
                alpha = multipliers(T)
                alpha["alpha"][b] = ONE
                current = multipliers(T)
                current["N"][k][0] = ONE
                combined = multipliers(T)
                combined["alpha"][b] = ONE
                combined["N"][k][0] = ONE
                mixed = (prefix_action(history, combined, hessian)
                         - prefix_action(history, alpha, hessian)
                         - prefix_action(history, current, hessian))
                require(mixed == (JUMP if b <= k else ZERO), "F_PREFIX")
                counts["PREFIX_MIXED_COEFFICIENTS"] += 1
                payload.append(f"P|{T}|{k}|{b}|{mixed}\n")

            feasible, reduced, pivots = rref(tail_rows(T, k), T)
            require(feasible and pivots == list(range(T - 1)), "F_TAIL")
            # RREF must exhibit exactly C_b-C_T=JUMP*1_(b<=k).
            for b, row in enumerate(reduced, 1):
                expected = [ZERO] * (T + 1)
                expected[b - 1], expected[T - 1] = ONE, -ONE
                expected[T] = JUMP if b <= k else ZERO
                require(row == expected, "F_TAIL")
            minimum = min(k - 1, T - k)
            feasible_radii = []
            for radius in range(T):
                feasible = local_system(T, k, radius)
                require(feasible == (radius >= minimum), "F_TAIL")
                if feasible:
                    feasible_radii.append(radius)
                counts["TAIL_SYSTEMS"] += 1
                payload.append(f"R|{T}|{k}|{radius}|{int(feasible)}\n")
            require(feasible_radii and min(feasible_radii) == minimum, "F_RADIUS")
            undersized = not local_system(T, k, minimum - 1)
            all_undersized_detected = all_undersized_detected and undersized
            require(undersized, "F_PLATEAU")
            both_tails = tail_rows(T, k) + [zero_coordinate_row(T, 1),
                                            zero_coordinate_row(T, T)]
            plateau = parameter_list[T - 1]
            plateau_derivative, interaction = current_variation(history, k, plateau)
            plateau_gamma = gamma([[value] * 5 for value in plateau])
            require(plateau_gamma["alpha"] == [ZERO, ONE] + [ZERO] * (T - 2) + [-ONE]
                    and all(value == 0 for row in plateau_gamma["lambda"] for value in row)
                    and all(value == 0 for row in plateau_gamma["N"] for value in row)
                    and not rref(both_tails, T)[0] and plateau_derivative == -JUMP
                    and interaction == 0, "F_PLATEAU")
            counts["PLATEAU_OBSTRUCTIONS"] += 1
            escape = auxiliary_variation(T, k)
            require(escape == JUMP and plateau_derivative + escape == 0, "F_ESCAPE")
            counts["AUXILIARY_ESCAPE_CHECKS"] += 1
            payload.append(f"E|{T}|{k}|{escape}\n")

    T, k = 5, 2
    control_history = build_history(T, k)
    plateau = parameters(T)[T - 1]
    derivative, interaction = current_variation(control_history, k, plateau)
    controls = []
    # Reverse only the tested field-current sign, keeping the interaction term.
    reversed_derivative = -(derivative - interaction) + interaction
    controls.append(reversed_derivative == JUMP and reversed_derivative != -JUMP)
    omitted = multipliers(T)
    omitted_derivative = derivative_interaction(
        control_history, omitted,
        transform(control_history, [[value] * 5 for value in plateau]))
    controls.append(omitted_derivative == 0 and omitted_derivative != -JUMP)
    uncoupled = build_history(T, k, coupling=ZERO)
    controls.append(any(value != 0 for row in residuals(uncoupled) for value in row))
    controls.append(all_undersized_detected and not local_system(T, k, min(k - 1, T - k) - 1))
    both_tails = tail_rows(T, k) + [zero_coordinate_row(T, 1), zero_coordinate_row(T, T)]
    controls.append(not rref(both_tails, T)[0])
    wrong_tail = [-JUMP if b <= k else ZERO for b in range(1, T + 1)]
    controls.append(any(dot(row[:T], wrong_tail) != row[T] for row in tail_rows(T, k)))
    gradient = hessian_apply(assemble_action_hessian(T), flatten(control_history))
    controls.append(all(gradient[6 * n + r] == 0 for n in range(1, T) for r in range(6))
                    and derivative == -JUMP and derivative != 0)
    wrong_escape = auxiliary_variation(T, k, sign=-ONE)
    controls.append(derivative + wrong_escape == F(-29, 324)
                    and derivative + auxiliary_variation(T, k) == 0)
    require(len(controls) == 8 and all(controls), "F_CONTROL")
    payload.extend(f"N|NC{index:02d}|DETECTED\n" for index in range(1, 9))

    expected_counts = {
        "HISTORY_CASES": 22,
        "ON_SHELL_COMPONENTS": 1200,
        "ACTION_DERIVATIVES": 1200,
        "CURRENT_PARAMETER_CHECKS": 244,
        "PREFIX_MIXED_COEFFICIENTS": 222,
        "TAIL_SYSTEMS": 222,
        "PLATEAU_OBSTRUCTIONS": 22,
        "AUXILIARY_ESCAPE_CHECKS": 22,
        "INTEGER_RESIDUALS": 1200,
        "INTEGER_WARD_WITNESSES": 244,
    }
    require(counts == expected_counts, "F_COUNTS")
    digest = sha256("".join(payload).encode("ascii")).hexdigest()
    lines = ["CERTIFICATE=P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1", "AUTHORITY_FILES=5"]
    lines.extend(f"{key}={value}" for key, value in counts.items())
    lines.extend(("WITNESS=-29/648", "TAIL_JUMP=29/648", f"PAYLOAD_SHA256={digest}",
                  "NEGATIVE_CONTROLS=8", "CERTIFICATE_RESULT=PASS"))
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))


if __name__ == "__main__":
    try:
        run()
    except ScientificFailure as failure:
        sys.stdout.buffer.write((str(failure) + "\nRESULT=FAIL\n").encode("ascii"))
