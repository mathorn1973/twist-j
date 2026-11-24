"""Independent integer reference for ordered Z5 score observables.

An exact record represents a real number as
  sum_r (coefficients[r][0] + sqrt(5)*coefficients[r][1])*zeta_L**r
  / denominator.
The deliberately redundant group-ring basis makes every coefficient
comparison exact before specialization to a root of unity.
"""

import argparse
from dataclasses import dataclass
import hashlib
from itertools import product
import json
from pathlib import Path
import re


LIMITS = {
    "TWISTJ_Z5_LINK_STATE_V1": 32,
    "TWISTJ_Z5_ORDERED_LINK_STATE_V1": 64,
}
MAX_STATE_BYTES = 4 * 64**4 + 256
UINT64_MAX = 2**64 - 1
SCORE = ((0, 0), (1, 0), (2, 1), (-2, -1), (-1, 0))


class IntegrityError(ValueError):
    """A saved-state, metadata, or exact arithmetic contract failed."""


@dataclass(frozen=True)
class LinkState:
    schema: str
    side: int
    chain: str
    sample: int
    macrocycle: int
    links: bytes
    sha256: str
    byte_count: int


def canonical_decimal(raw, field):
    if not re.fullmatch(rb"(?:0|[1-9][0-9]{0,19})", raw):
        raise IntegrityError(f"invalid_{field}")
    value = int(raw)
    if value > UINT64_MAX:
        raise IntegrityError(f"overflow_{field}")
    return value


def parse_state(raw, expected_sha256):
    if not isinstance(expected_sha256, str) or not re.fullmatch(
        r"[0-9a-f]{64}", expected_sha256
    ):
        raise IntegrityError("invalid_external_sha256")
    if len(raw) > MAX_STATE_BYTES:
        raise IntegrityError("state_too_long")
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_sha256:
        raise IntegrityError("state_sha256_mismatch")

    lines = raw.split(b"\n")
    if len(lines) != 8 or lines[-2:] != [b"END", b""]:
        raise IntegrityError("invalid_state_line_count_or_terminator")
    try:
        schema = lines[0].decode("ascii")
    except UnicodeDecodeError as error:
        raise IntegrityError("invalid_state_schema") from error
    if schema not in LIMITS:
        raise IntegrityError("invalid_state_schema")

    names = (b"L=", b"CHAIN=", b"SAMPLE=", b"MACROCYCLE=", b"LINKS=")
    if not all(line.startswith(name) for line, name in zip(lines[1:6], names)):
        raise IntegrityError("unexpected_state_field")
    side_text, chain, sample_text, macrocycle_text, links = (
        line[len(name):] for line, name in zip(lines[1:6], names)
    )
    side = canonical_decimal(side_text, "L")
    if not 2 <= side <= LIMITS[schema]:
        raise IntegrityError("L_outside_schema_range")
    if not re.fullmatch(rb"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}", chain):
        raise IntegrityError("invalid_chain")
    sample = canonical_decimal(sample_text, "sample")
    macrocycle = canonical_decimal(macrocycle_text, "macrocycle")
    if len(links) != 4 * side**4 or links.strip(b"01234"):
        raise IntegrityError("invalid_links")
    header = (
        f"{schema}\nL={side}\nCHAIN={chain.decode('ascii')}\n"
        f"SAMPLE={sample}\nMACROCYCLE={macrocycle}\nLINKS="
    ).encode("ascii")
    if header + links + b"\nEND\n" != raw:
        raise IntegrityError("noncanonical_reserialization")
    return LinkState(schema, side, chain.decode("ascii"), sample, macrocycle,
                     links, digest, len(raw))


def load_state(path, expected_sha256):
    with Path(path).open("rb") as file:
        return parse_state(file.read(MAX_STATE_BYTES + 1), expected_sha256)


def validate_query(state, longitudinal_axis, longitudinal_index, transfer_axis,
                   orientation, radius, offsets=None):
    side = state.side
    if longitudinal_axis not in range(4) or transfer_axis not in range(4):
        raise IntegrityError("invalid_axis")
    if longitudinal_axis == transfer_axis or longitudinal_index % side == 0:
        raise IntegrityError("invalid_longitudinal_or_transfer_mode")
    if len(orientation) != 2 or not 0 <= orientation[0] < orientation[1] < 4:
        raise IntegrityError("invalid_orientation")
    if not 2 <= radius <= side:
        raise IntegrityError("invalid_radius")
    if offsets is None:
        wave = [0] * 4
        wave[longitudinal_axis] = longitudinal_index % side
    else:
        if len(offsets) != 4:
            raise IntegrityError("invalid_offsets")
        wave = [index % side for index in offsets]
        if wave[transfer_axis] != 0 or wave[longitudinal_axis] != longitudinal_index % side:
            raise IntegrityError("offsets_disagree_with_marked_axes")
    return tuple(wave)


def score_bins(state, orientation, transfer_axis, wave):
    side = state.side
    first_axis, second_axis = orientation
    strides = (side**3, side**2, side, 1)
    bins = [[[0, 0] for _ in range(side)] for _ in range(side)]
    raw = state.links
    for site, point in enumerate(product(range(side), repeat=4)):
        first_neighbour = site + strides[first_axis] * (
            1 if point[first_axis] + 1 < side else 1 - side
        )
        second_neighbour = site + strides[second_axis] * (
            1 if point[second_axis] + 1 < side else 1 - side
        )
        flux = (raw[4 * site + first_axis] + raw[4 * first_neighbour + second_axis]
                - raw[4 * second_neighbour + first_axis] - raw[4 * site + second_axis]) % 5
        if flux:
            residue = sum(index * coordinate for index, coordinate in zip(wave, point)) % side
            pair = bins[point[transfer_axis]][residue]
            score_real, score_radical = SCORE[flux]
            pair[0] += score_real
            pair[1] += score_radical
    return bins


def cyclic_correlation(left, right, target):
    """Add left(zeta) times right(zeta^-1), before multiplying by kappa^2."""
    side = len(left)
    right_terms = [(index, pair) for index, pair in enumerate(right) if any(pair)]
    for left_index, (a, b) in enumerate(left):
        if a or b:
            for right_index, (c, d) in right_terms:
                pair = target[(left_index - right_index) % side]
                pair[0] += a * c + 5 * b * d
                pair[1] += a * d + b * c


def multiply_kappa_squared(polynomial):
    return [[5 * a - 10 * b, -2 * a + 5 * b] for a, b in polynomial]


def mode_power(bins, index):
    side = len(bins)
    mode = [[0, 0] for _ in range(side)]
    for time, phase_row in enumerate(bins):
        for residue, (a, b) in enumerate(phase_row):
            pair = mode[(residue + time * index) % side]
            pair[0] += a
            pair[1] += b
    power = [[0, 0] for _ in range(side)]
    cyclic_correlation(mode, mode, power)
    return multiply_kappa_squared(power)


def direct_covariances(bins):
    """Return centered time-lag covariances before division by L^4."""
    side = len(bins)
    covariances = []
    for lag in range(side):
        numerator = [[0, 0] for _ in range(side)]
        for time, row in enumerate(bins):
            cyclic_correlation(bins[(time + lag) % side], row, numerator)
        covariances.append(multiply_kappa_squared(numerator))
    return covariances


def add_shifted(target, source, residue=0, multiplier=1):
    side = len(target)
    for index, (a, b) in enumerate(source):
        pair = target[(index + residue) % side]
        pair[0] += multiplier * a
        pair[1] += multiplier * b


def direct_fejer(covariances, width, sign):
    """The direct result's denominator is V*M^2, not V*M."""
    side = len(covariances)
    answer = [[0, 0] for _ in range(side)]
    for lag, polynomial in enumerate(covariances):
        add_shifted(answer, polynomial, multiplier=sign * width**2)
        for index in range(1 - width, width):
            add_shifted(answer, polynomial, lag * index,
                        -sign * (width - abs(index)))
    return answer


def exact_number(side, denominator, coefficients):
    return {"root_order": side, "denominator": denominator,
            "coefficients": coefficients}


def read_query(state, longitudinal_axis, longitudinal_index, transfer_axis,
               orientation, radius, offsets=None, *, direct=True):
    wave = validate_query(state, longitudinal_axis, longitudinal_index,
                          transfer_axis, orientation, radius, offsets)
    side = state.side
    volume = side**4
    width = (side + radius - 1) // radius
    sign = -1 if transfer_axis in orientation else 1
    bins = score_bins(state, orientation, transfer_axis, wave)
    powers = {index: mode_power(bins, index) for index in range(1 - width, width)}
    numerator = [[0, 0] for _ in range(side)]
    add_shifted(numerator, powers[0], multiplier=sign * width**2)
    for index, power in powers.items():
        add_shifted(numerator, power, multiplier=-sign * (width - abs(index)))

    result = {
        "schema": "TWISTJ_Z5_ORDERED_REFERENCE_V1",
        "state": {
            "schema": state.schema, "L": side, "chain": state.chain,
            "sample": state.sample, "macrocycle": state.macrocycle,
            "bytes": state.byte_count, "sha256": state.sha256,
        },
        "query": {
            "longitudinal_axis": longitudinal_axis,
            "longitudinal_index": wave[longitudinal_axis],
            "transfer_axis": transfer_axis, "orientation": list(orientation),
            "wave": list(wave), "radius": radius, "width": width, "score_sign": sign,
        },
        "Q": [
            {"transfer_index": index, "value": exact_number(side, volume, power)}
            for index, power in powers.items()
        ],
        "A": exact_number(side, volume * width**2, numerator),
        "D": exact_number(side, volume * width**2, numerator),
    }
    if direct:
        covariances = direct_covariances(bins)
        if direct_fejer(covariances, width, sign) != numerator:
            raise IntegrityError("direct_and_frequency_fejer_disagree")
        for index, power in powers.items():
            restored = [[0, 0] for _ in range(side)]
            for lag, polynomial in enumerate(covariances):
                add_shifted(restored, polynomial, lag * index)
            if restored != power:
                raise IntegrityError("direct_and_frequency_power_disagree")
        result["cyclic_covariance"] = [
            exact_number(side, volume, polynomial) for polynomial in covariances
        ]
    return result


def read_ordered(state, expected_sha256, queries):
    parsed = load_state(state, expected_sha256)
    return [read_query(parsed, **query) for query in queries]


def packet_kernel(side, ratio):
    kernel = []
    for displacement in range(side):
        coefficients = [0] * side
        for index in range(1 - ratio, ratio):
            coefficients[(index * displacement) % side] += ratio - abs(index)
        kernel.append(coefficients)
    return kernel


def multiply_integer_roots(left, right):
    side = len(left)
    answer = [0] * side
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b:
                    answer[(i + j) % side] += a * b
    return answer


def cube_score_rows(state, orientation):
    """Direct chart triples for Test A, independent of score_bins."""
    side = state.side
    axis_a, axis_b = orientation
    rows = [[] for _ in range(side)]

    def edge(point, axis, displacement=None):
        x = list(point)
        if displacement is not None:
            x[displacement] = (x[displacement] + 1) % side
        p, q, r, s = x
        site = ((p * side + q) * side + r) * side + s
        return state.links[4 * site + axis] - 48

    for point in product(range(side), repeat=4):
        value = (edge(point, axis_a) + edge(point, axis_b, axis_a)
                 - edge(point, axis_a, axis_b) - edge(point, axis_b)) % 5
        if value:
            rows[point[1]].append(((point[0], point[2], point[3]), SCORE[value]))
    return rows


def score_distance_counts(rows, lag):
    side = len(rows)
    distances = {}
    for time, row in enumerate(rows):
        for point, (a, b) in rows[(time + lag) % side]:
            for other, (c, d) in row:
                difference = tuple((x - y) % side for x, y in zip(point, other))
                count = distances.setdefault(difference, [0, 0])
                count[0] += a * c + 5 * b * d
                count[1] += a * d + b * c
    return distances


def packet_record(rows, lag, ratio, sign, lag_factor, kernel, triples):
    side = len(rows)
    numerator = [[0, 0] for _ in range(side)]
    origin = [0, 0]
    for difference, (a, b) in score_distance_counts(rows, lag).items():
        if a == b == 0:
            continue
        origin[0] += a
        origin[1] += b
        sorted_difference = tuple(sorted(difference))
        if sorted_difference not in triples:
            x, y, z = sorted_difference
            triples[sorted_difference] = multiply_integer_roots(
                multiply_integer_roots(kernel[x], kernel[y]), kernel[z]
            )
        for residue, coefficient in enumerate(triples[sorted_difference]):
            numerator[residue][0] += coefficient * a
            numerator[residue][1] += coefficient * b

    prefactor = lag_factor * sign
    for pair in numerator:
        pair[0] *= prefactor
        pair[1] *= prefactor
    zero_mode = [[prefactor * value for value in origin]] + [[0, 0] for _ in range(side - 1)]
    return {
        "lag": lag,
        "value": exact_number(side, side**4 * ratio**6, multiply_kappa_squared(numerator)),
        "zero_mode": exact_number(side, side**4 * ratio**3, multiply_kappa_squared(zero_mode)),
    }


def electric_contact(record, rows, ratio):
    """Replace the raw score contact by the dual electric contact."""
    side = len(rows)
    score_squared = [[0, 0] for _ in range(side)]
    for row in rows:
        for _, (a, b) in row:
            score_squared[0][0] += a * a + 5 * b * b
            score_squared[0][1] += 2 * a * b
    onsite = multiply_kappa_squared(score_squared)
    onsite[0][0] += side**4
    result = {"lag": 0}
    for name, packet_factor in (("value", ratio**6), ("zero_mode", 1)):
        raw = record[name]
        coefficients = [[-2 * a, -2 * b] for a, b in raw["coefficients"]]
        add_shifted(coefficients, onsite, multiplier=packet_factor)
        result[name] = exact_number(side, 2 * raw["denominator"], coefficients)
    return result


def read_amplitudes(state, m):
    """Direct, sparse pair-distance oracle intended for fixture-sized states."""
    side = state.side
    if m < 1 or side % m or side < 2 * m:
        raise IntegrityError("invalid_packet_width_or_lag")
    ratio = side // m
    kernel = packet_kernel(side, ratio)
    if sum(kernel[0]) != ratio**2:
        raise IntegrityError("packet_weights_not_normalized")
    triples = {}
    output = {
        "schema": "TWISTJ_Z5_ORDERED_REFERENCE_V1",
        "state": {
            "schema": state.schema, "L": side, "chain": state.chain,
            "sample": state.sample, "macrocycle": state.macrocycle,
            "bytes": state.byte_count, "sha256": state.sha256,
        },
        "m": m, "r": ratio,
    }
    for channel, orientation, sign in (("E", (0, 1), -1), ("M", (0, 2), 1)):
        rows = cube_score_rows(state, orientation)
        output[f"A_{channel}"] = packet_record(rows, m, ratio, sign, m, kernel, triples)
        lags = (0, m, 2 * m, 3 * m) if side >= 6 * m else (0, m)
        output[f"C_{channel}"] = [
            packet_record(rows, lag, ratio, 1 if lag == 0 else sign, 1,
                          kernel, triples)
            for lag in lags
        ]
        if channel == "E":
            contact = output["C_E"][0]
            output["C_E"][0] = electric_contact(contact, rows, ratio)
    return output


def parse_coordinates(value):
    try:
        return tuple(map(int, value.split(",")))
    except ValueError as error:
        raise argparse.ArgumentTypeError("expected comma-separated integers") from error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--longitudinal-axis", type=int)
    parser.add_argument("--longitudinal-index", type=int)
    parser.add_argument("--transfer-axis", type=int)
    parser.add_argument("--orientation", type=parse_coordinates)
    parser.add_argument("--radius", type=int)
    parser.add_argument("--offsets", type=parse_coordinates)
    parser.add_argument("--m", type=int)
    parser.add_argument("--frequency-only", action="store_true")
    args = parser.parse_args()
    try:
        state = load_state(args.state, args.expected_sha256)
        query = (args.longitudinal_axis, args.longitudinal_index,
                 args.transfer_axis, args.orientation, args.radius)
        if args.m is not None:
            if any(value is not None for value in query) or args.offsets or args.frequency_only:
                raise IntegrityError("packet_and_tail_options_are_mutually_exclusive")
            result = read_amplitudes(state, args.m)
        else:
            if any(value is None for value in query):
                raise IntegrityError("missing_tail_query_options")
            result = read_query(state, *query, args.offsets, direct=not args.frequency_only)
    except OSError:
        parser.exit(2, "STOP_INTEGRITY state_io_error\n")
    except IntegrityError as error:
        parser.exit(2, f"STOP_INTEGRITY {error}\n")
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
