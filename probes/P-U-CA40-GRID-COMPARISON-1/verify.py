#!/usr/bin/env python3
"""Exact supporting fixtures for the local-window grid comparison.

NON-CANONICAL engineering support only; no candidate import or execution,
binary64 emulation, propagator validation, or numerical outcome prediction.
"""
from fractions import Fraction as Q
from math import isqrt
import json
import sys


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def occupied(labels):
    return [segment for segment in range(80)
            if any((label + segment // 16) % 5 == 0 for label in labels)]


def window_checks():
    dt = Q(1, 160000)
    windows = wrong_duration = reset_controls = 0
    for sign in (-1, 1):
        for labels in ((4, 3), (4, 4), (1, 1)):
            segments = occupied(labels)
            size = len(segments)
            require(size == (32 if labels == (4, 3) else 16), "occupied segment inventory")
            ordinals = (0, (size - 1) // 3, (2 * (size - 1)) // 3, size - 1)
            require(list(ordinals) == sorted(set(ordinals)), "distinct window ordinals")
            for ordinal, qc, qf in zip(ordinals, (0, 128, 128, 254), (0, 256, 256, 508)):
                segment = segments[ordinal]
                coarse = [dt * (segment + Q(qc + j, 256)) for j in range(3)]
                fine = [dt * (segment + Q(qf + j, 512)) for j in range(5)]
                require(coarse[0] == fine[0] and coarse[-1] == fine[-1], "same physical interval")
                require(coarse == fine[::2], "coarse boundaries match even fine boundaries")
                require(coarse[-1] - coarse[0] == Q(1, 20480000), "fixed physical duration")
                require(segment * dt <= coarse[0] < coarse[-1] <= (segment + 1) * dt,
                        "no amplitude switch inside window")
                require(fine[2] != coarse[-1], "two-fine-cell duration mutant")
                wrong_duration += 1
                require(coarse[0] != dt * Q(qc, 256), "discarded absolute-clock mutant")
                reset_controls += 1
                windows += 1
    return {"matched_windows": windows, "wrong_duration_controls": wrong_duration,
            "absolute_clock_controls": reset_controls}


def norm_squared(vector):
    return sum((x * x for x in vector), Q(0))


def square_interval(lo, hi):
    require(lo <= hi, "ordered input interval")
    return (Q(0) if lo <= 0 <= hi else min(lo * lo, hi * hi), max(lo * lo, hi * hi))


def sqrt_interval(value, bits=16):
    require(value >= 0, "nonnegative square root")
    scale = 1 << bits
    lower = Q(isqrt((value.numerator * scale * scale) // value.denominator), scale)
    upper = lower if lower * lower == value else lower + Q(1, scale)
    require(lower * lower <= value <= upper * upper, "rational square-root enclosure")
    return lower, upper


def classify(lower, upper, radius_sum_up):
    require(0 <= lower <= upper and radius_sum_up >= 0, "distance comparison domain")
    if lower > radius_sum_up:
        return "INCONSISTENT"
    if upper <= radius_sum_up:
        return "COMPATIBLE"
    return "UNRESOLVED"


def distance_checks():
    enclosure_cases = triangle_cases = 0
    for dimension in (2, 4, 8):
        for seed in range(5):
            truth = [Q(3, 5), Q(4, 5)] + [Q(0)] * (dimension - 2)
            da = [Q(i - seed, 64) for i in range(dimension)]
            db = [Q(seed + 2 * i + 1, 128) for i in range(dimension)]
            a = [t + e for t, e in zip(truth, da)]
            b = [t + e for t, e in zip(truth, db)]
            ea, eb = sum(map(abs, da), Q(0)), sum(map(abs, db), Q(0))
            require(norm_squared(truth) == 1, "shared normalized exact solution")
            require(norm_squared(da) <= ea * ea and norm_squared(db) <= eb * eb,
                    "valid separate error radii")
            delta = [x - y for x, y in zip(a, b)]
            exact_square = norm_squared(delta)
            require(exact_square <= (ea + eb) ** 2, "triangle consistency")
            triangle_cases += 1
            # Rational enclosing arithmetic, not a simulation of AVX rounding.
            intervals = [square_interval(x - Q(1, 1024), x + Q(1, 1024)) for x in delta]
            lower_square = sum((x[0] for x in intervals), Q(0))
            upper_square = sum((x[1] for x in intervals), Q(0))
            lower, upper = sqrt_interval(lower_square)[0], sqrt_interval(upper_square)[1]
            require(lower_square <= exact_square <= upper_square, "squared norm enclosure")
            require(lower * lower <= exact_square <= upper * upper, "L2 enclosure")
            require(classify(lower, upper, ea + eb + Q(1, 4096)) != "INCONSISTENT",
                    "valid radii cannot trigger inconsistency")
            enclosure_cases += 1
    require(square_interval(Q(-1, 8), Q(1, 4))[0] == 0,
            "zero-crossing square lower endpoint")
    require(min(Q(-1, 8) ** 2, Q(1, 4) ** 2) > 0,
            "naive positive lower square would exclude zero")
    cases = ((Q(0), Q(1, 2), Q(1, 2), "COMPATIBLE"),
             (Q(1, 2), Q(3, 4), Q(1, 4), "INCONSISTENT"),
             (Q(1, 4), Q(3, 4), Q(1, 2), "UNRESOLVED"),
             (Q(1, 2), Q(3, 4), Q(1, 2), "UNRESOLVED"))
    for lo, hi, radius, expected in cases:
        require(classify(lo, hi, radius) == expected, "three-way comparison/equality boundary")
    require(classify(Q(0), Q(1), Q(1, 2)) == "UNRESOLVED",
            "large upper endpoint is not a contradiction")
    require(classify(Q(1, 2), Q(1, 2), Q(1, 8)) == "INCONSISTENT",
            "underclaimed error-radius negative control")
    return {"triangle_cases": triangle_cases, "norm_enclosure_cases": enclosure_cases,
            "classification_cases": len(cases), "naive_square_controls": 1,
            "upper_only_failure_controls": 1, "underclaimed_radius_controls": 1}


def growth_checks():
    cases = ((Q(0), Q(0), True), (Q(1, 1024), Q(0), False),
             (Q(1, 16), Q(1, 32), True), (Q(65, 1024), Q(1, 32), False),
             (Q(1, 64), Q(1, 32), True))
    for coarse, fine, expected in cases:
        require((coarse <= 2 * fine) == expected, "exact zero-safe engineering screen")
    return {"growth_screen_cases": len(cases)}


def run_checks():
    counts = {}
    for check in (window_checks, distance_checks, growth_checks):
        counts.update(check())
    return {"status": "PASS", "probe": "P-U-CA40-GRID-COMPARISON-1",
            "scope": "exact_local_window_and_comparison_support_fixtures",
            "counts": counts, "arithmetic": "stdlib_Fraction",
            "kernel_executed": False, "IEEE_emulated": False,
            "grid_accuracy_established": False, "full_trajectory_certificate": False}


if __name__ == "__main__":
    sys.stdout.buffer.write((json.dumps(run_checks(), sort_keys=True,
                                       separators=(",", ":")) + "\n").encode("ascii"))
