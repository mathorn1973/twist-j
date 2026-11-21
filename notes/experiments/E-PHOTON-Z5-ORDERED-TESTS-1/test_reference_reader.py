"""Synthetic integrity fixtures for the exact ordered Z5 reference reader."""

from fractions import Fraction
import hashlib
from itertools import product
import json
from contextlib import redirect_stdout
from io import BytesIO, StringIO
from unittest.mock import patch
import unittest

import reference_reader as reader


OLD = "TWISTJ_Z5_LINK_STATE_V1"
NEW = "TWISTJ_Z5_ORDERED_LINK_STATE_V1"


def site(side, point):
    x0, x1, x2, x3 = point
    return ((x0 * side + x1) * side + x2) * side + x3


def raw_state(side=4, values=None, schema=NEW):
    values = {} if values is None else values
    links = bytearray(b"0" * (4 * side**4))
    for (point, axis), residue in values.items():
        links[4 * site(side, point) + axis] = ord("0") + residue
    return (
        f"{schema}\nL={side}\nCHAIN=fixture-1\nSAMPLE=7\nMACROCYCLE=18\nLINKS=".encode("ascii")
        + links + b"\nEND\n"
    )


def parse(raw):
    return reader.parse_state(raw, hashlib.sha256(raw).hexdigest())


def specialize_l4(exact):
    """Evaluate at zeta_4=i independently of the reader."""
    if exact["root_order"] != 4:
        raise AssertionError("wrong fixture field")
    zero, one, two, three = exact["coefficients"]
    denominator = exact["denominator"]
    if one != three:
        raise AssertionError("expected a real fixture coefficient")
    return tuple(Fraction(a - b, denominator) for a, b in zip(zero, two))


def moved(values, side, shift):
    return {
        (tuple((x + y) % side for x, y in zip(point, shift)), axis): value
        for (point, axis), value in values.items()
    }


class ReaderTest(unittest.TestCase):
    def test_zero_and_metadata_both_schemas(self):
        for schema in (OLD, NEW):
            state = parse(raw_state(schema=schema))
            result = reader.read_query(state, 0, 1, 1, (0, 1), 2)
            self.assertEqual(result["state"]["schema"], schema)
            self.assertEqual(result["state"]["chain"], "fixture-1")
            self.assertEqual(result["state"]["sample"], 7)
            self.assertEqual(result["state"]["macrocycle"], 18)
            self.assertEqual(specialize_l4(result["A"]), (0, 0))

    def test_single_link_electric_score(self):
        state = parse(raw_state(values={((0, 0, 0, 0), 0): 1}))
        result = reader.read_query(state, 2, 1, 1, (0, 1), 2)
        self.assertEqual(result["query"]["score_sign"], -1)
        self.assertEqual(
            specialize_l4(result["A"]), (Fraction(5, 256), Fraction(-2, 256))
        )
        modes = {row["transfer_index"]: specialize_l4(row["value"]) for row in result["Q"]}
        self.assertEqual(modes[0], (0, 0))
        self.assertEqual(modes[-1], (Fraction(10, 256), Fraction(-4, 256)))
        self.assertEqual(modes[1], modes[-1])

    def test_radical_score_and_periodic_seam(self):
        values = {((0, 0, 0, 0), 0): 2}
        result = reader.read_query(parse(raw_state(values=values)), 2, 1, 1, (0, 1), 2)
        seam_result = reader.read_query(
            parse(raw_state(values=moved(values, 4, (0, 3, 3, 0)))),
            2, 1, 1, (0, 1), 2,
        )
        self.assertEqual(
            specialize_l4(result["A"]), (Fraction(5, 256), Fraction(2, 256))
        )
        for key in ("A", "Q", "cyclic_covariance"):
            self.assertEqual(result[key], seam_result[key])

    def test_negative_sample_and_once_counted_midpoint(self):
        values = {((0, 0, 0, 0), 0): 1, ((0, 0, 2, 0), 0): 4}
        result = reader.read_query(parse(raw_state(values=values)), 1, 1, 2, (0, 1), 2)
        self.assertEqual(result["query"]["score_sign"], 1)
        self.assertEqual(
            specialize_l4(result["A"]), (Fraction(-5, 64), Fraction(2, 64))
        )
        self.assertEqual(
            specialize_l4(result["cyclic_covariance"][2]),
            (Fraction(-5, 64), Fraction(2, 64)),
        )

    def test_gauge_and_flat_holonomy_invariance(self):
        values = {((0, 0, 0, 0), 0): 2, ((0, 0, 2, 0), 0): 4}
        transformed = {}
        side = 4

        def gauge(point):
            return (point[0] * point[2] + point[1]) % 5

        for point in product(range(side), repeat=4):
            for axis in range(4):
                neighbour = tuple((x + (i == axis)) % side for i, x in enumerate(point))
                transformed[point, axis] = (
                    values.get((point, axis), 0)
                    + gauge(neighbour) - gauge(point) + (axis == 3)
                ) % 5
        arguments = (1, 1, 2, (0, 1), 2, (1, 1, 0, 0))
        original = reader.read_query(parse(raw_state(values=values)), *arguments)
        changed = reader.read_query(parse(raw_state(values=transformed)), *arguments)
        for key in ("A", "Q", "cyclic_covariance"):
            self.assertEqual(original[key], changed[key])

    def test_packet_electric_and_magnetic_signs(self):
        fixtures = (
            ("E", 1, (Fraction(-5, 64), Fraction(2, 64))),
            ("M", 0, (Fraction(5, 64), Fraction(-2, 64))),
        )
        for channel, link_axis, expected in fixtures:
            with self.subTest(channel=channel):
                values = {((0, 0, 0, 0), link_axis): 1, ((0, 2, 0, 0), link_axis): 1}
                result = reader.read_amplitudes(parse(raw_state(values=values)), 2)
                record = result[f"A_{channel}"]
                self.assertEqual(specialize_l4(record["value"]), expected)
                self.assertEqual(specialize_l4(record["zero_mode"]), (0, 0))
                lag_records = result[f"C_{channel}"]
                self.assertEqual([row["lag"] for row in lag_records], [0, 2])
                self.assertEqual(
                    specialize_l4(lag_records[1]["value"]), tuple(x / 2 for x in expected)
                )
                self.assertGreater(specialize_l4(lag_records[0]["value"])[0], 0)

    def test_electric_contact_is_onsite_minus_raw_score(self):
        vacuum = reader.read_amplitudes(parse(raw_state()), 1)
        self.assertEqual(specialize_l4(vacuum["C_E"][0]["value"]), (Fraction(1, 2), 0))
        self.assertEqual(specialize_l4(vacuum["C_M"][0]["value"]), (0, 0))

        values = {((0, 0, 0, 0), 1): 1}
        result = reader.read_amplitudes(parse(raw_state(values=values)), 1)
        electric = result["C_E"][0]
        self.assertEqual(
            specialize_l4(electric["value"]),
            (Fraction(1, 2) - Fraction(5, 256), Fraction(2, 256)),
        )
        self.assertEqual(
            specialize_l4(electric["zero_mode"]),
            ((Fraction(1, 2) + Fraction(5, 256)) / 64, Fraction(-2, 256 * 64)),
        )
        self.assertEqual(specialize_l4(result["C_M"][0]["value"]), (0, 0))

    def test_large_schema_boundary_and_bad_metadata(self):
        raw = raw_state()
        mutators = (
            lambda b: b.replace(b"L=4", b"L=04"),
            lambda b: b.replace(b"L=4", b"L=65"),
            lambda b: b.replace(b"SAMPLE=7", b"SAMPLE=18446744073709551616"),
            lambda b: b.replace(b"CHAIN=fixture-1", b"CHAIN=fixture/1"),
            lambda b: b.replace(b"LINKS=0", b"LINKS=5", 1),
            lambda b: b.replace(b"\n", b"\r\n"),
            lambda b: b[:-1],
            lambda b: b + b"\n",
        )
        for mutate in mutators:
            with self.subTest(mutate=mutate):
                with self.assertRaises(reader.IntegrityError):
                    parse(mutate(raw))
        with self.assertRaisesRegex(reader.IntegrityError, "L_outside_schema_range"):
            parse(raw.replace(NEW.encode(), OLD.encode()).replace(b"L=4", b"L=33"))
        with self.assertRaisesRegex(reader.IntegrityError, "invalid_links"):
            parse(raw.replace(b"L=4", b"L=33"))
        with self.assertRaisesRegex(reader.IntegrityError, "state_sha256_mismatch"):
            reader.parse_state(raw, "0" * 64)

    def test_cli_reads_external_hash_and_matches_direct(self):
        raw = raw_state(values={((0, 0, 0, 0), 0): 1})
        arguments = [
            "reference_reader.py", "--state", "fixture.state",
            "--expected-sha256", hashlib.sha256(raw).hexdigest(),
            "--longitudinal-axis", "2", "--longitudinal-index", "1",
            "--transfer-axis", "1", "--orientation", "0,1", "--radius", "2",
        ]
        stdout = StringIO()
        with patch("sys.argv", arguments), patch.object(reader.Path, "open", return_value=BytesIO(raw)):
            with redirect_stdout(stdout):
                reader.main()
        self.assertEqual(
            specialize_l4(json.loads(stdout.getvalue())["A"]),
            (Fraction(5, 256), Fraction(-2, 256)),
        )


if __name__ == "__main__":
    unittest.main()
