"""Exact reduction; bounds require measured/qualified inputs, never defaults."""

from fractions import Fraction
from math import isqrt
from schema import keys, nonnegative, q, require

COMPONENTS = ("voltage", "current", "drift", "timing", "integration", "repeatability", "filter", "unresolved")


def expanded_uncertainty(model):
    """Conservative rational upper bound for k sqrt(1^T C 1), C in J^2.

    Contributions already include their signed sensitivities. Exact PSD LDL
    validates covariance; anticorrelation is retained. Effective degrees of
    freedom and coverage justification remain required external input bytes.
    """
    keys(model, ("components", "covariance_J2", "coverage_factor", "dof", "justification_sha256"))
    from schema import digest
    require(model["components"] == list(COMPONENTS), "all uncertainty components required")
    digest(model["justification_sha256"])
    require(nonnegative(model["dof"]) > 0, "effective degrees of freedom")
    k = nonnegative(model["coverage_factor"])
    require(k >= 1, "coverage factor")
    source = model["covariance_J2"]
    n = len(COMPONENTS)
    require(type(source) is list and len(source) == n and all(type(r) is list and len(r) == n for r in source), "covariance shape")
    matrix = [[q(x) for x in row] for row in source]
    require(all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n)), "covariance symmetry")
    residual = [row[:] for row in matrix]
    for i in range(n):
        pivot = residual[i][i]
        require(pivot >= 0, "covariance not positive semidefinite")
        if pivot == 0:
            require(all(residual[i][j] == 0 for j in range(i + 1, n)), "zero covariance pivot")
        else:
            for j in range(i + 1, n):
                for m in range(i + 1, n):
                    residual[j][m] -= residual[j][i] * residual[i][m] / pivot
    variance = sum(sum(row) for row in matrix)
    require(variance >= 0, "negative combined variance")
    scale = 10**12
    numerator = variance.numerator * scale * scale
    root = isqrt(numerator // variance.denominator)
    if root * root * variance.denominator < numerator:
        root += 1
    return k * Fraction(root, scale)


def integrate(series, start, end):
    """Signed/absolute VI over complete interval, including back-transfers.

    A segment stores simultaneous SI V,I on [t0,t1). Frozen reconstruction
    uncertainty must bound interpolation, tails, filter and unresolved ripple.
    No extrapolation across a gap; coverage failure returns None.
    """
    signed = absolute = Fraction(0)
    cursor = Fraction(start)
    end = Fraction(end)
    previous_end = None
    for item in series:
        t0, t1 = q(item["t0_s"]), q(item["t1_s"])
        require(previous_end is None or t0 >= previous_end, "overlapping/unordered V/I")
        previous_end = t1
        left, right = max(t0, start), min(t1, end)
        if left >= right:
            continue
        if left != cursor or item["V"] is None or item["I"] is None or any(f != "SYNTHETIC" for f in item["flags"]):
            return None
        energy = q(item["V"]) * q(item["I"]) * (right - left)
        signed += energy
        absolute += abs(energy)
        cursor = right
    return (signed, absolute) if cursor == end else None
