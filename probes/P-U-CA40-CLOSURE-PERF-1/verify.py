#!/usr/bin/env python3
"""Exact supporting fixtures for P-U-CA40-CLOSURE-PERF-1.

PUBLIC NON-CANONICAL conditional L1 engineering audit. This does not execute,
import, or certify the C++ kernels, floating-point endpoints, or performance.
"""
from fractions import Fraction as Q
from itertools import product
import json
import sys


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def basis(modes, cutoff):
    return sorted((n for n in product(range(cutoff + 1), repeat=modes)
                   if sum(n) <= cutoff), key=lambda n: (sum(n), n))


def triangular_matrix(states, support, mode, creation):
    """Generic nonzero rational complex rows with the kernel's support graph.

    These are memory/linear-algebra fixtures, not physical displacement tables.
    """
    matrix = []
    for n in states:
        row = []
        for p in states:
            same = all(n[j] == p[j] for j in range(len(n)) if j != mode)
            k = n[mode] - p[mode] if creation else p[mode] - n[mode]
            allowed = same and k >= 0 and (creation or sum(p) <= support)
            if not allowed:
                row.append((Q(0), Q(0)))
            elif k == 0:
                row.append((Q(1), Q(0)))
            else:
                row.append((Q((-1) ** k * (n[mode] + 1), 2 ** k * (k + 1)),
                            Q(k, 3 ** k)))
        matrix.append(row)
    return matrix


def row_value(matrix, source, row, dimension, lanes, lane):
    re = im = Q(0)
    for col, (ar, ai) in enumerate(matrix[row]):
        xr, xi = source[col * lanes + lane], source[(dimension + col) * lanes + lane]
        re += ar * xr - ai * xi
        im += ai * xr + ar * xi
    return re, im


def row_action(matrix, source, output, end, lanes, clear_complement):
    dimension = len(matrix)
    if clear_complement:
        output[end * lanes:dimension * lanes] = [Q(0)] * ((dimension - end) * lanes)
        output[(dimension + end) * lanes:] = [Q(0)] * ((dimension - end) * lanes)
    for row in range(end):
        for lane in range(lanes):
            re, im = row_value(matrix, source, row, dimension, lanes, lane)
            output[row * lanes + lane] = re
            output[(dimension + row) * lanes + lane] = im


def check_overwrite():
    checks = stale_controls = 0
    lanes = 2
    for modes in (1, 2, 3):
        for cutoff in (1, 2, 3):
            states = basis(modes, cutoff)
            dimension = len(states)
            for support in range(cutoff + 1):
                source = [Q((j % 11) - 5, 7) for j in range(2 * dimension * lanes)]
                end = sum(sum(n) <= support for n in states)
                for row in range(end, dimension):
                    for lane in range(lanes):
                        source[row * lanes + lane] = Q(0)
                        source[(dimension + row) * lanes + lane] = Q(0)
                for mode in range(modes):
                    for creation in (False, True):
                        matrix = triangular_matrix(states, support, mode, creation)
                        written = dimension if creation else end
                        expected = [Q(0)] * len(source)
                        row_action(matrix, source, expected, dimension, lanes, False)
                        actual = [Q(91)] * len(source)
                        row_action(matrix, source, actual, written, lanes, not creation)
                        require(actual == expected, "triangular overwrite/complement")
                        checks += 1
                        if not creation and end < dimension:
                            stale = [Q(91)] * len(source)
                            row_action(matrix, source, stale, written, lanes, False)
                            require(stale != expected, "stale guard negative control")
                            stale_controls += 1
    return {"triangular_layout_cases": checks, "stale_complement_controls": stale_controls}


def matrix_vector(matrix, source):
    return [sum((a * b for a, b in zip(row, source)), Q(0)) for row in matrix]


def guard_alias(source, output, term, temp):
    if (source is output or source is term or source is temp
            or output is term or output is temp):
        raise ValueError("alias")
    require(term is not temp, "distinct constructed workspace members")


def optimized_word(source, buffers, matrices):
    guard_alias(source, buffers["out"], buffers["term"], buffers["temp"])
    buffers["term"][:] = matrix_vector(matrices[0], source)
    for matrix in matrices[1:]:
        buffers["temp"][:] = matrix_vector(matrix, buffers["term"])
        buffers["term"], buffers["temp"] = buffers["temp"], buffers["term"]
    buffers["out"], buffers["term"] = buffers["term"], buffers["out"]
    return buffers["out"]


def check_ownership():
    checks = 0
    for dimension in (2, 3, 5):
        lower = [[Q(i + j + 1, 7) if j <= i else Q(0)
                  for j in range(dimension)] for i in range(dimension)]
        upper = [list(row) for row in zip(*lower)]
        for length in (2, 3, 14):
            matrices = [lower if j % 2 else upper for j in range(length)]
            buffers = {name: [Q(37)] * dimension for name in ("out", "term", "temp")}
            for repetition in range(3):
                source = [Q(j + repetition + 1, 3) for j in range(dimension)]
                original = source.copy()
                expected = source.copy()
                for matrix in matrices:
                    expected = matrix_vector(matrix, expected)
                require(optimized_word(source, buffers, matrices) == expected,
                        "copy versus ownership exchange")
                require(source == original, "source preserved")
                require(len({id(v) for v in buffers.values()}) == 3,
                        "distinct buffers after repeated exchange")
                checks += 1
    objects = [[], [], [], []]
    negatives = 0
    for a, b in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3)):
        args = objects.copy()
        args[b] = args[a]
        try:
            guard_alias(*args)
        except ValueError:
            negatives += 1
        else:
            raise AssertionError("missing alias rejection")
    matrix = [[Q(int(j <= i)) for j in range(3)] for i in range(3)]
    original = [Q(1), Q(2), Q(3)]
    corrupt = original.copy()
    for i, row in enumerate(matrix):
        corrupt[i] = sum((a * b for a, b in zip(row, corrupt)), Q(0))
    require(corrupt != matrix_vector(matrix, original), "unguarded in-place counterexample")
    return {"ownership_reuse_cases": checks, "alias_rejections": negatives,
            "in_place_corruption_controls": 1}


def embed(vector, guard_dimension):
    return vector + [Q(0)] * (guard_dimension - len(vector))


def dual_horner(coefficients, theta):
    value = [Q(0)] * len(coefficients[0])
    derivative = value.copy()
    for coefficient in reversed(coefficients):
        derivative = [theta * d + p for d, p in zip(derivative, value)]
        value = [theta * p + a for p, a in zip(value, coefficient)]
    return value, derivative


def check_horner():
    checks = underflow_checks = 0
    u, eta = Q(1, 2 ** 53), Q(1, 2 ** 1074)
    for dimension in (1, 2, 4):
        for guard_dimension in (dimension, dimension + 1, dimension + 3):
            for degree in range(6):
                coefficients = [[Q((j + 2) * (i + 1) * (-1) ** (j + i), 13)
                                 for i in range(dimension)] for j in range(degree + 1)]
                extended = [embed(a, guard_dimension) for a in coefficients]
                for theta in (Q(-1, 3), Q(0), Q(1, 2), Q(1), Q(4, 3)):
                    value, derivative = dual_horner(coefficients, theta)
                    big_value, big_derivative = dual_horner(extended, theta)
                    direct = [sum((coefficients[j][i] * theta ** j
                                   for j in range(degree + 1)), Q(0))
                              for i in range(dimension)]
                    direct_derivative = [sum((j * coefficients[j][i] * theta ** (j - 1)
                                              for j in range(1, degree + 1)), Q(0))
                                         for i in range(dimension)]
                    require(value == direct and derivative == direct_derivative,
                            "dual Horner monomial identity")
                    require(big_value == embed(value, guard_dimension)
                            and big_derivative == embed(derivative, guard_dimension),
                            "Horner commutes with exact zero extension")
                    require(sum(p * p for p in value) == sum(p * p for p in big_value),
                            "zero extension isometry")
                    checks += 1
            for operations in (1, 2, 12):
                factor = operations * eta / (1 - operations * u)
                small_U_squared = 2 * dimension * factor ** 2
                old_U_squared = 2 * guard_dimension * factor ** 2
                require(small_U_squared <= old_U_squared, "retained U_G conservative")
                underflow_checks += 1
    # Updating p before d silently changes dual Horner; make that mutant fire.
    value = derivative = Q(0)
    for coefficient in (Q(3), Q(2), Q(1)):
        value = value / 2 + coefficient
        derivative = derivative / 2 + value
    require(derivative != Q(5), "old-value derivative negative control")
    return {"horner_embedding_cases": checks, "underflow_dimension_cases": underflow_checks,
            "new_value_derivative_controls": 1}


def run_checks():
    counts = {}
    for check in (check_overwrite, check_ownership, check_horner):
        counts.update(check())
    return {"status": "PASS", "probe": "P-U-CA40-CLOSURE-PERF-1",
            "scope": "exact_rational_supporting_optimization_fixtures",
            "arithmetic": "stdlib_Fraction", "counts": counts,
            "kernel_executed": False, "floating_equivalence_established": False,
            "performance_established": False, "full_trajectory_certificate": False}


if __name__ == "__main__":
    sys.stdout.buffer.write((json.dumps(run_checks(), sort_keys=True,
                                       separators=(",", ":")) + "\n").encode("ascii"))
