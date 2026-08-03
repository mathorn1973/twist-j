"""Standalone exact verification of a candidate kappa witness JSON.

This non-formal checker uses explicit failures rather than ``assert`` so
``python -O`` cannot disable a scientific gate.  It checks:

1. the JSON schema and absence of duplicate support entries;
2. a nonzero ternary, closed current with connected support and an explicit
   closed Eulerian traversal using every support edge once;
3. a ternary face chain satisfying partial n = 5j coefficientwise; and
4. the declared support counts and 2^F <= 7^L in exact integer arithmetic.
"""

import json
import sys

from kappa_lib import chain_d, edge_d, check_connected_edge_simple


EXPECTED_KEYS = {"P", "m", "C", "D", "L", "F", "j", "n"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def is_int(value):
    return type(value) is int


def parse_vertex(raw, label):
    require(isinstance(raw, list) and len(raw) == 4,
            "%s vertex must be a four-integer list" % label)
    require(all(is_int(x) for x in raw),
            "%s vertex contains a non-integer coordinate" % label)
    return tuple(raw)


def parse_current(raw):
    require(isinstance(raw, list), "j must be a list")
    current = {}
    for index, item in enumerate(raw):
        label = "j[%d]" % index
        require(isinstance(item, list) and len(item) == 3,
                "%s must have [vertex, direction, coefficient]" % label)
        vertex = parse_vertex(item[0], label)
        direction, coefficient = item[1], item[2]
        require(is_int(direction) and 0 <= direction < 4,
                "%s has an invalid direction" % label)
        require(is_int(coefficient) and coefficient in (-1, 1),
                "%s has a non-ternary support coefficient" % label)
        edge = (vertex, direction)
        require(edge not in current, "%s duplicates an earlier edge" % label)
        current[edge] = coefficient
    require(current, "j is empty")
    return current


def parse_faces(raw):
    require(isinstance(raw, list), "n must be a list")
    faces = {}
    for index, item in enumerate(raw):
        label = "n[%d]" % index
        require(isinstance(item, list) and len(item) == 4,
                "%s must have [vertex, a, b, coefficient]" % label)
        vertex = parse_vertex(item[0], label)
        a, b, coefficient = item[1], item[2], item[3]
        require(is_int(a) and is_int(b) and 0 <= a < b < 4,
                "%s has invalid face directions" % label)
        require(is_int(coefficient) and coefficient in (-1, 1),
                "%s has a non-ternary support coefficient" % label)
        face = (vertex, a, b)
        require(face not in faces, "%s duplicates an earlier face" % label)
        faces[face] = coefficient
    return faces


def verify(path):
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    require(isinstance(data, dict), "top-level JSON value must be an object")
    require(set(data) == EXPECTED_KEYS,
            "top-level keys differ from the frozen candidate schema")
    for field in ("P", "m", "C", "D", "L", "F"):
        require(is_int(data[field]), "%s must be an integer" % field)
    for field in ("P", "m", "C", "D", "L"):
        require(data[field] > 0, "%s must be positive" % field)
    require(data["F"] >= 0, "F must be nonnegative")

    current = parse_current(data["j"])
    faces = parse_faces(data["n"])
    require(not edge_d(current), "partial j is nonzero")
    length, walk = check_connected_edge_simple(current)
    area = len(faces)
    require(data["L"] == length, "declared L disagrees with |supp j|")
    require(data["F"] == area, "declared F disagrees with |supp n|")

    target = {edge: 5 * coefficient for edge, coefficient in current.items()}
    require(chain_d(faces) == target, "partial n != 5j")

    lhs = 2 ** area
    rhs = 7 ** length
    require(lhs <= rhs, "2^F > 7^L")
    return length, area, len(walk), lhs, rhs


def main(argv):
    if len(argv) != 2:
        print("usage: verify_witness.py WITNESS.json", file=sys.stderr)
        return 2
    try:
        length, area, walk_steps, lhs, rhs = verify(argv[1])
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("KAPPA-WITNESS FAIL: %s" % exc, file=sys.stderr)
        return 1

    print("KAPPA-WITNESS PASS")
    print("L = %d   F = %d   F/L = %d/%d" %
          (length, area, area, length))
    print("2^F <= 7^L verified as exact integers "
          "(%d-digit vs %d-digit)" % (len(str(lhs)), len(str(rhs))))
    print("closed edge-simple worldline: Eulerian walk of %d steps "
          "over connected support" % walk_steps)
    print("candidate consequence (NON-CANONICAL, no probe run): if issue "
          "#200 admits this current, the exact pair excludes every K2 "
          "coefficient; the formal outcome predicate remains to be frozen")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
