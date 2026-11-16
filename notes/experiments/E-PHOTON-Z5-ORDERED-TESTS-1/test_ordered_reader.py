"""Deterministic fixtures for the certified ordered reader."""
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import unittest
from unittest.mock import patch

import numpy as np

import ordered_reader as fast
import reference_reader as direct


def state_bytes(links, schema=fast.SCHEMA):
    side = links.shape[0]
    digits = (links + ord("0")).astype(np.uint8).tobytes()
    fields = [schema, f"L={side}".encode(), b"CHAIN=fixture", b"SAMPLE=3",
              b"MACROCYCLE=5", b"LINKS="+digits, b"END", b""]
    return b"\n".join(fields)


def fixture(side=8):
    links = np.zeros((side,) * 4 + (4,), dtype=np.uint8)
    assignments = (
        ((0, 0, 0, 0, 0), 1), ((0, 2, 0, 0, 0), 2),
        ((7, 6, 1, 7, 0), 1), ((7, 0, 1, 7, 0), 4),
        ((0, 1, 0, 7, 2), 1), ((0, 3, 0, 7, 2), 1),
        ((3, 3, 5, 2, 1), 3), ((1, 4, 3, 4, 0), 2),
        ((0, 7, 0, 0, 3), 3),
    )
    for index, value in assignments:
        links[index] = value
    return links


def oracle_number(record):
    with localcontext() as ctx:
        ctx.prec = 80
        assert record["root_order"] == 8
        a = Decimal(2).sqrt() / 2
        cosines = (1, a, 0, -a, -1, -a, 0, a)
        sqrt5 = Decimal(5).sqrt()
        return sum((u + sqrt5*v)*c
                   for (u, v), c in zip(record["coefficients"], cosines)) / record["denominator"]


class TestOrderedReader(unittest.TestCase):
    def measure(self, links, m=(2,), R=(2,), *, secondary=False):
        data = state_bytes(links)
        digest = hashlib.sha256(data).hexdigest()
        return fast.measure_bytes(data, digest, m, R, secondary=secondary)

    def assert_contains(self, enclosure, exact):
        lower, upper = map(Decimal, enclosure)
        self.assertLessEqual(lower, exact)
        self.assertLessEqual(exact, upper)
        self.assertLessEqual((Fraction(upper)-Fraction(lower))/2, fast.PRECISION)

    def test_zero_and_electric_contact(self):
        values = self.measure(np.zeros((8,)*4+(4,), dtype=np.uint8))["observables"]
        for key, interval in values.items():
            expected = Decimal("0.5") if key == "Acheck:E:2:0" else Decimal(0)
            with self.subTest(key=key):
                self.assert_contains(interval, expected)

    def test_signed_wrapped_state_against_exact_reference(self):
        links = fixture()
        data = state_bytes(links)
        digest = hashlib.sha256(data).hexdigest()
        original = direct.parse_state(data, digest)
        observables = self.measure(links, (2,), (3,), secondary=True)["observables"]
        A = direct.read_amplitudes(original, 2)
        estimates = []
        for label in ("E", "M"):
            key = f"A:{label}:2"
            exact = oracle_number(A[f"A_{label}"]["value"])
            estimates.append(exact)
            self.assert_contains(observables[key], exact)
            self.assert_contains(observables[f"A0:{label}:2"],
                                 oracle_number(A[f"A_{label}"]["zero_mode"]))
            self.assert_contains(observables[f"Acheck:{label}:2:0"],
                                 oracle_number(A[f"C_{label}"][0]["value"]))
        self.assertTrue(all(x != 0 for x in estimates))

        for q_name, k in fast.Q_VALUES:
            for orientation in fast.PRIMARY:
                orientation_name = str(orientation[0]) + str(orientation[1])
                estimate = direct.read_query(original, 1, k, 2, orientation, 3)["D"]
                self.assert_contains(observables[f"D:3:{q_name}:{orientation_name}:2"],
                                     oracle_number(estimate))

        width = 3
        for axis, orient, coords in ((0, (0, 1), (2, 3)), (3, (2, 3), (0, 2))):
            offsets = [0] * 4
            offsets[1] = 2
            offsets[coords[0]], offsets[coords[1]] = width, -width
            estimate = direct.read_query(original, 1, 2, axis, orient, 3, tuple(offsets))["D"]
            name = str(orient[0]) + str(orient[1])
            key = f"Dgrid:3:pi/2:{name}:{axis}:{width}:{-width}"
            self.assert_contains(observables[key], oracle_number(estimate))

    def test_gauge_and_charge_invariance(self):
        links = fixture()
        base = self.measure(links)["observables"]
        x = np.indices((8,) * 4, dtype=np.int16)
        gauge = (x[0] + x[1]*x[2] + x[3]**2) % 5
        shifted = links.copy()
        for i in range(4):
            shifted[..., i] = (links[..., i] + np.roll(gauge, -1, axis=i) - gauge) % 5
        self.assertEqual(self.measure(shifted)["observables"], base)
        self.assertEqual(self.measure((5-links) % 5)["observables"], base)

    def test_exact_mode_fallback_against_direct_reader(self):
        links = fixture()
        data = state_bytes(links)
        original = direct.parse_state(data, hashlib.sha256(data).hexdigest())
        # Force the conservative fast interval to fail while preserving the
        # actual acceptance threshold and exact phase-bin fallback.
        with patch.object(fast, "_transform_error", return_value=Fraction(1, 32)):
            result = self.measure(links, (), (3,), secondary=True)["observables"]
        for orient, q_index, q_name in (((0, 1), 1, "pi/4"), ((1, 2), 2, "pi/2")):
            name = str(orient[0]) + str(orient[1])
            expected = oracle_number(direct.read_query(original, 1, q_index, 2, orient, 3)["D"])
            interval = result[f"D:3:{q_name}:{name}:2"]
            self.assert_contains(interval, expected)
            self.assertLessEqual(Decimal(interval[1])-Decimal(interval[0]), Decimal("2e-18"))

    def test_normalized_transform_and_mixed_radices(self):
        for n in (2, 3, 5, 8, 12):
            with self.subTest(n=n):
                values = np.zeros(n, dtype=fast.COMPLEX)
                values[n-1] = 1
                result = fast._transform(values, (0,))
                expected = fast._roots(n)[(np.arange(n)*(n-1)) % n]/n
                self.assertLess(float(np.max(np.abs(result-expected))), 1e-13)
                constant = fast._transform(np.ones(n, dtype=fast.REAL), (0,))
                self.assertLess(abs(complex(constant[0])-1), 1e-14)
                self.assertLess(float(np.max(np.abs(constant[1:]))), 1e-13)

    def test_parse_rejects_bad_custody_and_schema(self):
        data = state_bytes(fixture())
        with self.assertRaises(fast.IntegrityError):
            fast.parse_state(data, "0"*64)
        for malformed in (data[:-1], data.replace(b"L=8", b"L=08"),
                          data.replace(b"CHAIN=fixture", b"CHAIN=bad!"),
                          data.replace(b"\n", b"\r\n")):
            with self.subTest(malformed=malformed[:80]), self.assertRaises(fast.IntegrityError):
                fast.parse_state(malformed, hashlib.sha256(malformed).hexdigest())
        legacy = state_bytes(fixture(), fast.LEGACY_SCHEMA)
        self.assertEqual(fast.parse_state(legacy, hashlib.sha256(legacy).hexdigest())[0]["L"], 8)

    def test_outward_rounding_and_precision_fail(self):
        self.assert_contains(fast._interval(Fraction(-1, 3), Fraction()),
                             Decimal("-0.33333333333333333333333333333333333"))
        with self.assertRaises(fast.PrecisionError):
            fast._interval(Fraction(), fast.PRECISION*2)


if __name__ == "__main__":
    unittest.main()
