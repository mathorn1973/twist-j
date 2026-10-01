"""NON-CANONICAL: closed review schema for C96-06, no instrument driver."""

import json
import re
from fractions import Fraction
from hashlib import sha256

VERSION = "twist-j-c96-custody-1"
ROLES = ("B_2", "Z_2", "r_2")
FLAGS = ("MISSING", "SATURATION", "TIMING", "INVALID_POINTER", "SYNTHETIC")
OFFSETS = {"G": Fraction(2), "A": Fraction(9, 2), "B": Fraction(7), "F": Fraction(10)}


class Incident(ValueError):
    """Custody/schema violation; never silently sanitize evaluator input."""


def require(condition, message):
    if not condition:
        raise Incident(message)


def keys(value, names):
    require(type(value) is dict and set(value) == set(names), "closed schema fields")


def integer(value):
    require(type(value) is int, "integer required")
    return value


def q(value):
    """Canonical exact rational SI value; no whitespace, aliases, NaN or text."""
    require(type(value) is str and re.fullmatch(r"-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?", value), "rational required")
    result = Fraction(value)
    require(str(result) == value, "noncanonical rational")
    return result


def nonnegative(value):
    result = q(value)
    require(result >= 0, "negative uncertainty/bound")
    return result


def digest(value):
    require(type(value) is str and re.fullmatch("[0-9a-f]{64}", value), "SHA256 required")
    return value


def opaque(value):
    require(type(value) is str and re.fullmatch("[0-9a-f]{32}", value), "opaque random ID required")
    return value


def canonical(value):
    return json.dumps(value, ensure_ascii=True, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("ascii")


def hash_object(value):
    return sha256(canonical(value)).hexdigest()


def load(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result
    with open(path, encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=unique,
                         parse_constant=lambda _: (_ for _ in ()).throw(Incident("nonfinite JSON")))


def flags(value):
    require(type(value) is list and value == sorted(set(value)) and all(v in FLAGS for v in value), "closed quality vocabulary")


def coordinates(value, length):
    require(type(value) is list and len(value) == length, "coordinate count")
    for item in value:
        if item is not None:
            integer(item)


def bank(value):
    keys(value, ("energy_J", "U_J", "voltage_V"))
    for name in value:
        if value[name] is not None:
            (nonnegative if name == "U_J" else q)(value[name])


def reading(value):
    keys(value, ("t_s", "coordinates", "p", "optical", "angle_deg", "banks", "temperature_C", "flags"))
    q(value["t_s"])
    coordinates(value["coordinates"], 31)
    if value["p"] is not None:
        integer(value["p"])
    if value["optical"] is not None:
        require(type(value["optical"]) is int and 0 <= value["optical"] < 8, "raw three-bit code")
    for name in ("angle_deg", "temperature_C"):
        if value[name] is not None:
            q(value[name])
    keys(value["banks"], ROLES)
    for item in value["banks"].values():
        bank(item)
    flags(value["flags"])


def segment(value):
    keys(value, ("t0_s", "t1_s", "V", "I", "flags"))
    require(q(value["t1_s"]) > q(value["t0_s"]), "nonpositive sample interval")
    for name in ("V", "I"):
        if value[name] is not None:
            q(value[name])
    flags(value["flags"])


def packet(value):
    keys(value, ("schema", "id", "frames", "ports", "uncertainty", "flags"))
    require(value["schema"] == VERSION, "schema version")
    opaque(value["id"])
    require(type(value["frames"]) is list, "frames list")
    for frame in value["frames"]:
        keys(frame, ("step", "layer", "readings"))
        integer(frame["step"])
        require(frame["layer"] in ("INIT", "G", "A", "B", "F"), "closed layer")
        require(type(frame["readings"]) is list, "readings list")
        for item in frame["readings"]:
            reading(item)
    keys(value["ports"], ROLES)
    for series in value["ports"].values():
        require(type(series) is list, "series list")
        for item in series:
            segment(item)
    keys(value["uncertainty"], ("time_s", "first_work_J", "whole_abs_J", "slot_abs_J"))
    for name in ("time_s", "first_work_J", "whole_abs_J"):
        if value["uncertainty"][name] is not None:
            nonnegative(value["uncertainty"][name])
    slots = value["uncertainty"]["slot_abs_J"]
    require(type(slots) is list and len(slots) == 10, "ten slot uncertainties")
    for item in slots:
        if item is not None:
            nonnegative(item)
    flags(value["flags"])
    return value


def packet_flags(value):
    """Complete validated packet provenance/quality, including nested records.

    A missing frame never erases a marker on a retained record. Only the
    closed schema's flags fields are read; arbitrary metadata is not admitted.
    """
    packet(value)
    found = set(value["flags"])
    for frame in value["frames"]:
        for item in frame["readings"]:
            found.update(item["flags"])
    for series in value["ports"].values():
        for item in series:
            found.update(item["flags"])
    return found


def frame_keys():
    return [(0, "INIT")] + [(step, layer) for step in range(1, 11) for layer in "GABF"]


def table(value):
    """Expected tables are predictions, never accepted as observations."""
    require(type(value) is list and len(value) == 41, "41 expected frames")
    for item, (step, layer) in zip(value, frame_keys()):
        keys(item, ("step", "layer", "coordinates", "p", "counts"))
        require(item["step"] == step and item["layer"] == layer, "expected frame order")
        coordinates(item["coordinates"], 31)
        require(None not in item["coordinates"], "incomplete prediction")
        require(type(item["p"]) is int and 0 <= item["p"] < 5, "expected pointer")
        keys(item["counts"], ROLES)
        for count in item["counts"].values():
            require(type(count) is int and 0 <= count <= 41, "bank count")


def contract(value):
    keys(value, ("schema", "kind", "positive_tables", "null_table", "read_grid_s", "optical_codes"))
    require(value["schema"] == VERSION and value["kind"] == "PUBLIC_PREDICTIONS", "prediction type")
    require(type(value["positive_tables"]) is list and len(value["positive_tables"]) > 0, "positive prediction family required")
    for item in value["positive_tables"] + [value["null_table"]]:
        table(item)
    null = value["null_table"]
    require(all(row["coordinates"] == null[0]["coordinates"] and row["counts"] == null[0]["counts"]
                and row["p"] == 0 for row in null), "null predicate must remain prepared and blank")
    for candidate in value["positive_tables"]:
        require(candidate[0]["p"] == 0, "positive initial blank")
        require(all(row["p"] == 0 for row in candidate if row["step"] < 3), "no premature write")
        require(all(row["p"] != 0 for row in candidate if row["step"] >= 3), "HIT through boundary ten")
        by_key = {(row["step"], row["layer"]): row for row in candidate}
        require(by_key[(2, "F")]["counts"]["r_2"] == 2, "positive resource arrival at two")
        require(by_key[(3, "G")]["counts"]["B_2"] - candidate[0]["counts"]["B_2"] == 2,
                "first receiving one-joule logical work")
        reset = by_key[(4, "F")]
        require(reset["coordinates"] == candidate[0]["coordinates"] and reset["counts"] == candidate[0]["counts"],
                "old receiver reset at four")
    require(type(value["read_grid_s"]) is list and len(value["read_grid_s"]) == 41, "read grid")
    for times, (step, layer) in zip(value["read_grid_s"], frame_keys()):
        require(type(times) is list and times, "read grid empty")
        values = [q(v) for v in times]
        require(values == sorted(set(values)), "read grid order")
        end = 0 if layer == "INIT" else 10 * (step - 1) + OFFSETS[layer]
        start = end if layer == "INIT" else end - Fraction(1, 10)
        require(values[0] == start and values[-1] == end, "entire fixed read window required")
        require(all(start <= x <= end for x in values), "read grid outside fixed window")
    codes = value["optical_codes"]
    require(type(codes) is list and len(codes) == 5 and len(set(codes)) == 5, "five optical codes")
    require(all(type(v) is int and 0 <= v < 8 for v in codes), "three optical bits")
    return value
