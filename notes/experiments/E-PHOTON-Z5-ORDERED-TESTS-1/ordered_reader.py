"""Independent saved-link evaluator for the ordered Z5 diagnostics.

The chosen transform uses only explicit radix butterflies and dyadic-rounding
bounds. No error claim is made about a library FFT.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import re

import numpy as np


SCHEMA = b"TWISTJ_Z5_ORDERED_LINK_STATE_V1"
LEGACY_SCHEMA = b"TWISTJ_Z5_LINK_STATE_V1"
REAL = np.longdouble
COMPLEX = np.clongdouble
UNIT = Fraction(1, 1 << (np.finfo(REAL).nmant + 1))
TINY = Fraction(*np.finfo(REAL).tiny.as_integer_ratio())
PRECISION = Fraction(1, 1 << 30)
ORIENTATIONS = tuple((i, j) for i in range(4) for j in range(i + 1, 4))
PRIMARY = ((1, 2), (0, 1), (0, 2), (0, 3))
TRANSVERSE = (0, 2, 3)
Q_VALUES = (("pi/4", 1), ("pi/2", 2))
U_COEFFICIENT = np.array([0, 1, 2, -2, -1], dtype=np.int16)
V_COEFFICIENT = np.array([0, 0, 1, -1, 0], dtype=np.int16)


class IntegrityError(ValueError):
    """Malformed state, unsupported lattice or uncertified arithmetic."""


class PrecisionError(IntegrityError):
    """The arithmetic enclosure exceeds the protocol halfwidth."""


def _check_floating_environment():
    """Check the precision and tie rule assumed by the transform proof."""
    info = np.finfo(REAL)
    one = REAL(1)
    unit = info.eps / REAL(2)
    if (info.nmant < 52 or _fraction(unit) != UNIT or one + unit != one
            or one + REAL(3)*unit != one + REAL(4)*unit
            or -one - unit != -one):
        raise IntegrityError("explicit DFT requires binary round-to-nearest operations")


def _uint(raw, bound):
    if not re.fullmatch(rb"(0|[1-9][0-9]*)", raw) or len(raw) > len(str(bound)):
        raise IntegrityError("invalid canonical integer")
    value = int(raw)
    if value > bound:
        raise IntegrityError("integer out of range")
    return value


def parse_state(data, expected_sha256):
    if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
        raise IntegrityError("invalid state hash")
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        raise IntegrityError("state hash mismatch")
    lines = data.split(b"\n")
    if (len(lines) != 8 or lines[0] not in (SCHEMA, LEGACY_SCHEMA)
            or lines[6:] != [b"END", b""]):
        raise IntegrityError("invalid state framing")
    keys = (b"L=", b"CHAIN=", b"SAMPLE=", b"MACROCYCLE=", b"LINKS=")
    if any(not line.startswith(key) for line, key in zip(lines[1:6], keys)):
        raise IntegrityError("unexpected state field")
    raw_l, chain, sample, cycle, digits = (
        line[len(key):] for line, key in zip(lines[1:6], keys)
    )
    side = _uint(raw_l, 64 if lines[0] == SCHEMA else 32)
    if side < 2 or len(digits) != 4 * side**4:
        raise IntegrityError("invalid state size")
    if not re.fullmatch(rb"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}", chain):
        raise IntegrityError("invalid chain identifier")
    sample = _uint(sample, (1 << 64) - 1)
    cycle = _uint(cycle, (1 << 64) - 1)
    links = np.frombuffer(digits, dtype=np.uint8)
    if links.min() < ord("0") or links.max() > ord("4"):
        raise IntegrityError("invalid Z5 link digit")
    links = (links - ord("0")).reshape((side,) * 4 + (4,))
    return {"L": side, "chain": chain.decode("ascii"), "sample": sample,
            "macrocycle": cycle}, links


def curvature(links, orientation):
    i, j = orientation
    # The offset +10 keeps the uint8 additions and subtractions in range.
    ai = links[..., i]
    aj = links[..., j]
    return (10 + ai + np.roll(aj, -1, axis=i) - np.roll(ai, -1, axis=j) - aj) % 5


def _fraction(value):
    return Fraction(*value.as_integer_ratio())


def _atan_bounds(base, terms):
    value = sum((Fraction((-1)**i, (2*i+1) * base**(2*i+1))
                 for i in range(terms)), Fraction())
    remainder = Fraction((-1)**terms, (2*terms+1) * base**(2*terms+1))
    return min(value, value + remainder), max(value, value + remainder)


@lru_cache(maxsize=1)
def _pi_bounds():
    a, b = _atan_bounds(5, 56)
    c, d = _atan_bounds(239, 20)
    return 16*a - 4*d, 16*b - 4*c


def _convert(lo, hi):
    """Certificate by comparing the stored dyadic to the rational enclosure."""
    middle = (lo + hi) / 2
    scale = 10**70
    decimal = (middle.numerator * scale) // middle.denominator
    value = REAL(f"{decimal}e-70")
    exact = _fraction(value)
    if max(abs(exact-lo), abs(exact-hi)) > 2*UNIT:
        raise IntegrityError("constant conversion outside certified bound")
    return value


def _series(angle, sine):
    # Evaluate on [0,pi/2], then the first omitted alternating term bounds error.
    term = angle if sine else Fraction(1)
    value = term
    for i in range(1, 30):
        den = (2*i)*(2*i+1) if sine else (2*i-1)*(2*i)
        term *= -angle**2 / den
        value += term
    den = 60*61 if sine else 59*60
    tail = term * (-angle**2 / den)
    return min(value, value + tail), max(value, value + tail)


def _negative(bounds):
    return -bounds[1], -bounds[0]


def _dyadic_cover(lo, hi):
    scale = 1 << 144
    return (Fraction((lo.numerator*scale)//lo.denominator, scale),
            Fraction(-((-hi.numerator*scale)//hi.denominator), scale))


@lru_cache(maxsize=32)
def _root_intervals(side):
    low_pi, high_pi = _pi_bounds()
    result = []
    for k in range(side):
        # Choose nearest multiple of pi/2 and use a small signed residual.
        quadrant = (8*k + side) // (2*side)
        coefficient = Fraction(2*k, side) - Fraction(quadrant, 2)
        if coefficient:
            angle_low = abs(coefficient) * low_pi
            angle_span = abs(coefficient) * (high_pi - low_pi)
            c, d = _series(angle_low, False)
            e, f = _series(angle_low, True)
            real = _dyadic_cover(c - angle_span, d + angle_span)
            sine = _dyadic_cover(e - angle_span, f + angle_span)
            if coefficient < 0:
                sine = _negative(sine)
        else:
            real = Fraction(1), Fraction(1)
            sine = Fraction(0), Fraction(0)
        phase = ((real, _negative(sine)), (_negative(sine), _negative(real)),
                 (_negative(real), sine), (sine, real))
        result.append(phase[quadrant % 4])
    return tuple(result)


@lru_cache(maxsize=32)
def _roots(side):
    result = np.empty(side, dtype=COMPLEX)
    for k, (real, imag) in enumerate(_root_intervals(side)):
        result.real[k], result.imag[k] = _convert(*real), _convert(*imag)
    result.flags.writeable = False
    return result


def _sqrt_bounds(lo, hi):
    scale = 1 << 220
    def root(value):
        return math.isqrt((value.numerator * scale**2) // value.denominator)

    return Fraction(root(lo), scale), Fraction(root(hi) + 1, scale)


@lru_cache(maxsize=1)
def _score_intervals():
    low, high = _sqrt_bounds(Fraction(5), Fraction(5))
    one = _sqrt_bounds(5 - 2*high, 5 - 2*low)
    two = _sqrt_bounds(5 + 2*low, 5 + 2*high)
    return one, two


@lru_cache(maxsize=1)
def _score():
    one_bounds, two_bounds = _score_intervals()
    one, two = _convert(*one_bounds), _convert(*two_bounds)
    return np.array((0, one, two, -two, -one), dtype=REAL)


def _radix(n):
    for d in (2, 3, 5):
        if n % d == 0:
            return d
    # The frozen lattice schedule uses only 2, 3 and 5. A single direct
    # radix also provides fixture support at the other admitted sides.
    return n


def _depth_and_radix(n):
    depth, maximum = 0, 1
    while n > 1:
        d = _radix(n)
        maximum = max(maximum, d)
        depth += 1
        n //= d
    return depth, maximum


def _fft_last(values):
    """Normalized forward transform with the last axis as a single strided DFT."""
    n = values.shape[-1]
    if n == 1:
        return values
    radix = _radix(n)
    width = n // radix
    columns = values.reshape(values.shape[:-1] + (width, radix)).swapaxes(-1, -2)
    inner = _fft_last(columns)
    roots = _roots(n)
    k = np.arange(n).reshape(radix, width)
    factor = REAL(1) / REAL(radix)
    blocks = []
    for row in k:
        subtotal = inner[..., 0, :].copy()
        for offset in range(1, radix):
            subtotal += inner[..., offset, :] * roots[(offset * row) % n]
        blocks.append(subtotal * factor)
    return np.concatenate(blocks, axis=-1)


def _transform(values, axes):
    result = np.asarray(values, dtype=COMPLEX)
    for axis in axes:
        result = np.moveaxis(_fft_last(np.moveaxis(result, axis, -1)), -1, axis)
    return result


def _transform_error(side, axes, input_error):
    """Uniform Euclidean error, relative to the exactly normalized DFT.

    Root coordinate errors are <=2u. One complex product at input norm <=4
    incurs <=64u total, including its root error. The successive sum of up to
    r products and the final reciprocal scaling cost <=(32r+32)u after
    normalization. The enlarged (128+32r)u budget covers both. Each exact
    normalized butterfly is a contraction in the max Euclidean norm. Inputs
    have norm below 4 after accounting for this error at all used stages.
    """
    depth, maximum = _depth_and_radix(side)
    return input_error + axes * depth * (128 + 32*maximum) * UNIT


def _pairwise(values):
    values = np.ravel(values)
    if values.size == 0:
        return REAL(0)
    while values.size > 1:
        half = values.size // 2
        sums = values[:2*half:2] + values[1:2*half:2]
        if values.size % 2:
            sums = np.concatenate((sums, values[-1:]))
        values = sums
    return values[0]


def _amplitude_upper(values):
    # 2 max(|Re|,|Im|) is an exact, conservative Euclidean bound.
    maximum = max(np.max(np.abs(values.real)), np.max(np.abs(values.imag)))
    return 2 * _fraction(maximum)


def _product_error(error, amplitude, terms, mean_amplitude=None):
    depth = (max(1, terms) - 1).bit_length()
    mean_amplitude = amplitude if mean_amplitude is None else mean_amplitude
    return (2*error*mean_amplitude + error**2
            + (20+4*depth)*UNIT*amplitude*mean_amplitude
            + 64*(depth+1)*TINY)


def _interval(center, radius, key=""):
    lo, hi = center-radius, center+radius
    # Round outward in the units serialized for the analysis. Decimal parsing
    # of these strings stays outward, including for nonrepresentable dyadics.
    scale = 10**18
    lower = (lo.numerator * scale) // lo.denominator
    upper = -((-hi.numerator * scale) // hi.denominator)
    def decimal_string(numerator):
        prefix = "-" if numerator < 0 else ""
        whole, fraction = divmod(abs(numerator), scale)
        return f"{prefix}{whole}.{fraction:018d}"
    if Fraction(upper-lower, 2*scale) > PRECISION:
        width = decimal_string(upper-lower)
        raise PrecisionError(f"per-state enclosure exceeds 2^-30: {key} full_width={width}")
    return [decimal_string(lower), decimal_string(upper)]


def _axis_one_bins(flux, q_index):
    """Transform coordinate 1 only, using exact integer residue bins.

    The eight bins contain sums of integer score components. Before the
    arithmetic accumulation each coefficient has its exact count. The total
    absolute algebraic score per longitudinal line is <4L; the explicit
    eight-bin weighted sum is covered by 1024u uniformly for L<=64.
    """
    side = flux.shape[0]
    result = np.zeros((side,) * 3, dtype=COMPLEX)
    roots = _roots(8)
    score = _score()
    coefficient = score[2] - 2*score[1]
    for residue in range(8):
        block = flux[:, residue::8, :, :]
        u = np.sum(U_COEFFICIENT[block], axis=1, dtype=np.int16)
        v = np.sum(V_COEFFICIENT[block], axis=1, dtype=np.int16)
        term = u*score[1] + v*coefficient
        result += term * roots[(q_index*residue) % 8]
    return result * (REAL(1) / REAL(side))


def _power(values):
    return values.real*values.real + values.imag*values.imag


def _multiply_intervals(x, y):
    vertices = tuple(a*b for a in x for b in y)
    return min(vertices), max(vertices)


def _sum_intervals(x, y):
    return x[0]+y[0], x[1]+y[1]


def _square_interval(x):
    lo, hi = x
    ends = lo**2, hi**2
    return (Fraction() if lo <= 0 <= hi else min(ends), max(ends))


def _exact_power_reader(flux, q_index):
    """Rare-mode fallback with exact integer phase bins and rational roots."""
    side = flux.shape[0]
    roots = _root_intervals(side)
    coords = np.arange(side, dtype=np.int32)
    score1, score2 = _score_intervals()
    longitudinal_bins = None

    @lru_cache(maxsize=256)
    def power(momentum):
        nonlocal longitudinal_bins
        if longitudinal_bins is None:
            longitudinal_bins = []
            for residue in range(8):
                block = flux[:, residue::8, :, :]
                g = np.sum(U_COEFFICIENT[block], axis=1, dtype=np.int16)
                far = np.sum(V_COEFFICIENT[block], axis=1, dtype=np.int16)
                longitudinal_bins.append(((g-2*far).ravel(), far.ravel()))
        x, y, z = momentum
        phase = (x*coords[:, None, None] + y*coords[None, :, None]
                 + z*coords[None, None, :]).ravel() % side
        near_hist = np.zeros(side, dtype=np.int64)
        far_hist = np.zeros(side, dtype=np.int64)
        for residue, (near, far) in enumerate(longitudinal_bins):
            shift = q_index*(side//8)*residue
            # Each weighted count is an integer. The running absolute sum
            # is at most L^4 < 2^53, so bincount's binary64 adds are exact.
            near_hist += np.roll(np.bincount(phase, weights=near, minlength=side)
                                 .astype(np.int64), shift)
            far_hist += np.roll(np.bincount(phase, weights=far, minlength=side)
                                .astype(np.int64), shift)
        real = imag = Fraction(), Fraction()
        for near, far, (real_root, imag_root) in zip(near_hist, far_hist, roots):
            score = _sum_intervals(
                _multiply_intervals((int(near),)*2, score1),
                _multiply_intervals((int(far),)*2, score2),
            )
            real = _sum_intervals(real, _multiply_intervals(score, real_root))
            imag = _sum_intervals(imag, _multiply_intervals(score, imag_root))
        lo, hi = _sum_intervals(_square_interval(real), _square_interval(imag))
        return lo/side**4, hi/side**4

    return power


def _defect(spatial, side, radius, axis, orientation, offsets, key, exact_power):
    # Spatial array uses the original transverse axis order 0,2,3.
    width = (side + radius - 1) // radius
    j = np.arange(1-width, width)
    offset = list(offsets)
    index = TRANSVERSE.index(axis)
    band = [component % side for component in offset]
    band[index] = (offset[index] + j) % side
    selected = spatial[tuple(band)]
    powers = _power(selected)
    w = width - np.abs(j)
    sign = 1 if axis in orientation else -1
    center = sign * side**4 * (
        _fraction(_pairwise(w*powers)) / width**2 - _fraction(powers[width-1])
    )
    err = _transform_error(side, 3, 1024*UNIT)
    amplitude = _amplitude_upper(selected)
    radius_bound = 2 * side**4 * _product_error(err, amplitude, len(j))
    try:
        return _interval(center, radius_bound, key)
    except PrecisionError:
        bracket = Fraction(), Fraction()
        point = tuple(offsets[dim] % side for dim in range(3))
        for j_value, weight in zip(j, w):
            mode = list(point)
            mode[index] = (mode[index] + int(j_value)) % side
            exact = exact_power(tuple(mode))
            coefficient = Fraction(int(weight), width**2)
            bracket = _sum_intervals(bracket, _multiply_intervals(
                (coefficient, coefficient), exact
            ))
        bracket = _sum_intervals(bracket, _negative(exact_power(point)))
        if sign < 0:
            bracket = _negative(bracket)
        return _interval((bracket[0]+bracket[1])/2,
                         (bracket[1]-bracket[0])/2, key)


def _slice_band(flux, ratio):
    side = flux.shape[0]
    k = np.arange(1-ratio, ratio) % side
    score = _score()
    band = np.empty((side, len(k), len(k), len(k)), dtype=COMPLEX)
    slices = np.moveaxis(flux, 1, 0)
    for start in range(0, side, 4):
        fields = np.asarray(score[slices[start:start+4]], dtype=COMPLEX)
        for axis in (1, 2, 3):
            fields = np.take(_transform(fields, (axis,)), k, axis=axis)
        band[start:start+4] = fields
    return band


def _contact(flux, side):
    count = np.bincount(flux.ravel(), minlength=5)
    near = int(count[1] + count[4])
    far = int(count[2] + count[3])
    sqrt_lo, sqrt_hi = _sqrt_bounds(Fraction(5), Fraction(5))
    base = Fraction(side**4 + 5*(near+far), 2*side**4)
    coefficient = Fraction(far-near, side**4)
    lo, hi = sorted((base + coefficient*sqrt_lo, base + coefficient*sqrt_hi))
    return (lo+hi)/2, (hi-lo)/2


def _mean_amplitude_upper(values, weights, weight_sum):
    """Weighted average bound using computed positive Cartesian magnitudes."""
    depth = (max(1, values.size) - 1).bit_length()
    absolute = np.abs(values.real) + np.abs(values.imag)
    observed = _fraction(_pairwise(absolute*weights)) / weight_sum
    # At most two operations before each pairwise level. The compared
    # quantity is nonnegative, with integral nonzero weights at least one.
    return (observed + 16*(depth+4)*TINY) / (1 - 4*(depth+2)*UNIT)


def _amplitudes(wide_band, max_ratio, m, label, side, contact):
    ratio = side // m
    cut = slice(max_ratio-ratio, max_ratio+ratio-1)
    band = wide_band[:, cut, cut, cut]
    k = np.arange(1-ratio, ratio)
    ramp = ratio - np.abs(k)
    weights = ramp[:, None, None] * ramp[None, :, None] * ramp[None, None, :]
    sign = -1 if label == "E" else 1
    err = _transform_error(side, 3, 2*UNIT)
    amplitude = _amplitude_upper(band)
    mean_amp = _mean_amplitude_upper(band, weights, side*ratio**6)
    primary_radius = m*side**3*_product_error(err, amplitude, band.size, mean_amp)
    result = {}
    for lag in ([0, m, 2*m, 3*m] if side >= 6*m else [0, m]):
        tail = np.roll(band, -lag, axis=0)
        values = band.real*tail.real + band.imag*tail.imag
        raw = _fraction(_pairwise(values*weights))
        # Norm L^{-3/2} in F, time mean 1/L, packet denominator ratio^6.
        signed_scale = Fraction(sign * side**2, ratio**6)
        if lag == m:
            key = f"A:{label}:{m}"
            result[key] = _interval(m*signed_scale * raw, primary_radius, key)
            k0 = ratio - 1
            zero = _fraction(_pairwise(values[:, k0, k0, k0]))
            scale = m*signed_scale * ratio**3
            zero_band = band[:, k0, k0, k0]
            zm = _mean_amplitude_upper(zero_band, 1, side)
            radius_bound = Fraction(m*side**3, ratio**3)*_product_error(
                err, _amplitude_upper(zero_band), side, zm
            )
            key = f"A0:{label}:{m}"
            result[key] = _interval(scale*zero, radius_bound, key)
        else:
            center, radius_bound = signed_scale*raw, primary_radius / m
            if lag == 0 and label == "E":
                center += contact[0]
                radius_bound += contact[1]
            key = f"Acheck:{label}:{m}:{lag}"
            result[key] = _interval(center, radius_bound, key)
    return result


def measure_bytes(data, sha256, requested_m=(), requested_R=(), *, secondary=False):
    metadata, links = parse_state(data, sha256)
    _check_floating_environment()
    side = metadata["L"]
    requested_m = tuple(requested_m)
    requested_R = tuple(requested_R)
    if len(set(requested_m)) != len(requested_m) or len(set(requested_R)) != len(requested_R):
        raise IntegrityError("duplicate scale")
    if any(isinstance(m, bool) or not isinstance(m, int) or m < 1
           or side % m or 2*m > side for m in requested_m):
        raise IntegrityError("bad m for the declared state side")
    if requested_R and side % 8:
        raise IntegrityError("two fixed longitudinal modes must both be on grid")
    if any(isinstance(R, bool) or not isinstance(R, int) or not 2 <= R <= side//2
           for R in requested_R):
        raise IntegrityError("bad R for the declared state side")
    observables = {}
    for orientation in ORIENTATIONS:
        needed_a = orientation in ((0, 1), (0, 2)) and requested_m
        needed_b = requested_R and (secondary or orientation in PRIMARY)
        if not (needed_a or needed_b):
            continue
        flux = curvature(links, orientation)
        if needed_a:
            label = "E" if orientation == (0, 1) else "M"
            max_ratio = side // min(requested_m)
            wide_band = _slice_band(flux, max_ratio)
            contact = _contact(flux, side) if label == "E" else None
            for m in requested_m:
                observables.update(_amplitudes(wide_band, max_ratio, m, label, side, contact))
        if needed_b:
            orient_key = f"{orientation[0]}{orientation[1]}"
            for q_label, q_index in Q_VALUES:
                spatial = _transform(_axis_one_bins(flux, q_index), (0, 1, 2))
                exact_power = _exact_power_reader(flux, q_index)
                for R in requested_R:
                    if orientation in PRIMARY:
                        key = f"D:{R}:{q_label}:{orient_key}:2"
                        observables[key] = _defect(
                            spatial, side, R, 2, orientation, (0, 0, 0), key, exact_power
                        )
                    if secondary:
                        width = (side+R-1) // R
                        for axis in TRANSVERSE:
                            remaining = [a for a in TRANSVERSE if a != axis]
                            for a, b in product((-width, 0, width), repeat=2):
                                offsets = [0, 0, 0]
                                offsets[TRANSVERSE.index(remaining[0])] = a
                                offsets[TRANSVERSE.index(remaining[1])] = b
                                key = f"Dgrid:{R}:{q_label}:{orient_key}:{axis}:{a}:{b}"
                                observables[key] = _defect(
                                    spatial, side, R, axis, orientation, tuple(offsets), key,
                                    exact_power
                                )
    metadata["observables"] = observables
    return metadata


def read_measures(path, sha256, requested_m=(), requested_R=(), *, secondary=False):
    return measure_bytes(
        Path(path).read_bytes(), sha256, requested_m, requested_R, secondary=secondary
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--m", nargs="*", type=int, default=[])
    parser.add_argument("--radius", nargs="*", type=int, default=[])
    parser.add_argument("--secondary", action="store_true")
    args = parser.parse_args()
    try:
        record = read_measures(
            args.state, args.expected_sha256, args.m, args.radius, secondary=args.secondary
        )
    except IntegrityError as exc:
        parser.exit(2, f"STOP_INTEGRITY {exc}\n")
    print(json.dumps(record, sort_keys=True, separators=(",", ":"), allow_nan=False))


if __name__ == "__main__":
    main()
