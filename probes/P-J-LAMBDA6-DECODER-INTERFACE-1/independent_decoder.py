#!/usr/bin/env python3
"""Independent exact API audit. Execute only after the coordinator's public pin.

No author implementation was read before this program's byte freeze.
Only the module named on the command line is imported, and only at execution.
The ideal oracle uses inverse-lattice signatures, not lambda digit division.
"""
import argparse
import dataclasses
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import sys

ONE = (1, 0, 0, 0)
ZERO = (0, 0, 0, 0)
LAM = (1, -1, 0, 0)
J = (1, 0, 1, 0)
JI = (0, -1, -1, 0)
CHECKS = 0


def require(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def mul(x, y):
    c = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            c[i + j] += a * b
    for degree in range(6, 3, -1):
        q = c[degree]
        for shift in range(1, 5):
            c[degree - shift] -= q
    return tuple(c[:4])


def power(x, n):
    if n < 0:
        raise ValueError("nonnegative power only")
    out = ONE
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n //= 2
    return out


def jpower(n):
    return power(J if n >= 0 else JI, abs(n))


def uv(x):
    a, b, c, d = x
    return (a*a-a*b+b*b-b*c+c*c-c*d+d*d,
            a*b-a*c-a*d+b*c-b*d+c*d)


def norm(x):
    u, v = uv(x)
    return u*u+u*v-v*v


def inverse(matrix):
    n = len(matrix)
    a = [[Fraction(v) for v in row] +
         [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        q = a[col][col]
        a[col] = [v / q for v in a[col]]
        for row in range(n):
            if row != col:
                q = a[row][col]
                a[row] = [v-q*w for v, w in zip(a[row], a[col])]
    return [row[n:] for row in a]


class Oracle:
    def __init__(self):
        self.powers = [power(LAM, n) for n in range(6)]
        lm6 = power(LAM, 6)
        columns = [mul(lm6, tuple(int(i == j) for i in range(4)))
                   for j in range(4)]
        matrix = [list(row) for row in zip(*columns)]
        inv = inverse(matrix)
        self.signature_matrix = []
        for row in inv:
            scaled = [v * 25 for v in row]
            require(all(v.denominator == 1 for v in scaled),
                    "ideal signature denominator divides25")
            self.signature_matrix.append([int(v) for v in scaled])
        for left, right in ((matrix, inv), (inv, matrix)):
            require(all(sum(left[i][k]*right[k][j] for k in range(4))
                        == int(i == j) for i in range(4) for j in range(4)),
                    "both inverse-matrix identities")
        self.by_signature = {}
        for digits in itertools.product(range(5), repeat=6):
            value = self.representative(digits)
            key = self.signature(value)
            require(key not in self.by_signature, "distinct canonical digit classes")
            self.by_signature[key] = digits
        require(len(self.by_signature) == 15625, "quotient cardinality")
        require(self.signature((25, 0, 0, 0)) == (0, 0, 0, 0),
                "quotient characteristic divides25")
        require(self.signature((5, 0, 0, 0)) != (0, 0, 0, 0),
                "quotient characteristic is not5")
        require(mul(J, JI) == ONE, "J unit inverse")
        self.strip = []
        self.lookup = {}
        for x in itertools.product(range(-8, 9), repeat=4):
            u, v = uv(x)
            n = u*u+u*v-v*v
            if 0 <= v < u and 1 <= n <= 941:
                key = (u, v, self.signature(x))
                require(key not in self.lookup, "independent strip key injection")
                self.lookup[key] = x
                self.strip.append(x)
        require(len(self.strip) == 3150, "inherited complete strip cardinality")

    def signature(self, x):
        return tuple(sum(a*b for a, b in zip(row, x)) % 25
                     for row in self.signature_matrix)

    def representative(self, digits):
        return tuple(sum(d*p[i] for d, p in zip(digits, self.powers))
                     for i in range(4))

    def digits(self, x):
        return self.by_signature[self.signature(x)]

    def encode(self, x):
        u, v = uv(x)
        return 2*u+v, 3*u-v, self.digits(x)

    def step(self, reading, reverse=False):
        s0, s1, digits = reading
        shifted = mul(JI if reverse else J, self.representative(digits))
        return ((3*s0-s1, s0, self.digits(shifted)) if reverse else
                (s1, 3*s1-s0, self.digits(shifted)))

    def decode(self, reading):
        s0, s1, digits = reading
        if (s0+s1) % 5 or (3*s0-2*s1) % 5:
            return None
        u, v = (s0+s1)//5, (3*s0-2*s1)//5
        n = u*u+u*v-v*v
        if not (s0 > 0 and 1 <= n <= 941):
            return None
        exponent = 0
        residue = self.representative(digits)
        while not 0 <= v < u:
            measure = 2*u+int(v >= u)
            if v < 0:
                u, v = u+v, u+2*v
                residue = mul(JI, residue)
                exponent += 1
            else:
                u, v = 2*u-v, v-u
                residue = mul(J, residue)
                exponent -= 1
            residue = self.representative(self.digits(residue))
            require(0 < 2*u+int(v >= u) < measure,
                    "positive integer normalization descent")
        beta = self.lookup.get((u, v, self.signature(residue)))
        if beta is None:
            return None
        alpha = mul(jpower(exponent), beta)
        require(self.encode(alpha) == reading, "oracle exact image reversal")
        return alpha, beta, exponent, n


def load_api(path):
    spec = importlib.util.spec_from_file_location("reviewed_decoder_api", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load requested API module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def expect_error(call, error, label):
    try:
        call()
    except error:
        return
    raise AssertionError(label)


def inspect_record(record, expected):
    fields = ("coefficients", "strip_coefficients", "unit_exponent", "norm")
    require(tuple(getattr(record, f) for f in fields) == expected,
            "all decoded fields")
    require(type(record.coefficients) is tuple and
            type(record.strip_coefficients) is tuple,
            "record tuple coordinates")
    require(type(record.unit_exponent) is int and type(record.norm) is int,
            "record exact integer fields")
    if dataclasses.is_dataclass(record):
        require(tuple(f.name for f in dataclasses.fields(record)) == fields,
                "exact record fields")
    elif hasattr(record, "_fields"):
        require(tuple(record._fields) == fields, "exact named record fields")


def api_reading(value, label):
    require(type(value) is tuple and len(value) == 3, label+" outer tuple")
    require(type(value[0]) is int and type(value[1]) is int,
            label+" exact traces")
    require(type(value[2]) is tuple and len(value[2]) == 6 and
            all(type(x) is int and 0 <= x < 5 for x in value[2]),
            label+" canonical tuple digits")
    return value


def audit(api, oracle):
    require(issubclass(api.InvalidReading, ValueError), "InvalidReading type")
    totals = {"valid_translates": 0, "large_translates": 0,
              "image_classifications": 0, "data_permutations": 0,
              "malformed_cases": 0}
    first_record = None
    for beta in oracle.strip:
        for exponent in (-12, -3, -1, 0, 1, 3, 12):
            alpha = mul(jpower(exponent), beta)
            reading = oracle.encode(alpha)
            require(api_reading(api.encode(alpha), "encode") == reading,
                    "exact encode on every translated strip point")
            expected = (alpha, beta, exponent, norm(beta))
            record = api.decode(*reading)
            inspect_record(record, expected)
            require(oracle.decode(reading) == expected, "independent inverse")
            require(api_reading(api.T6(*reading), "T6") == oracle.encode(mul(J, alpha)),
                    "data J intertwining")
            require(api_reading(api.T6_inverse(*reading), "T6 inverse") ==
                    oracle.encode(mul(JI, alpha)), "data J inverse intertwining")
            first_record = first_record or record
            totals["valid_translates"] += 1
    require(first_record is not None, "record example exists")
    try:
        first_record.norm = first_record.norm
    except (AttributeError, TypeError):
        pass
    else:
        raise AssertionError("Decoded record must be frozen")

    selected = sorted(set([oracle.strip[0], oracle.strip[-1], ONE] +
                          [x for x in oracle.strip if uv(x)[1] == 0][:3] +
                          [x for x in oracle.strip if norm(x) == 941][:2]))
    for beta in selected:
        for exponent in (-1000, -101, 101, 1000):
            alpha = mul(jpower(exponent), beta)
            reading = oracle.encode(alpha)
            require(api.encode(list(alpha)) == reading, "large list scalar encode")
            record = api.decode(reading[0], reading[1], list(reading[2]))
            inspect_record(record, (alpha, beta, exponent, norm(beta)))
            require(oracle.decode(reading) ==
                    (alpha, beta, exponent, norm(beta)), "large oracle inverse")
            totals["large_translates"] += 1

    trace_pairs = [(2*u+v, 3*u-v) for u, v in
                   ((1, 0), (1, 1), (2, 1), (13, 6), (27, 8))]
    trace_pairs += [(0, 0), (-2, -3), (1, 0), (80, 120)]
    for traces in trace_pairs:
        for digits in itertools.product(range(5), repeat=6):
            reading = (*traces, digits)
            expected = oracle.decode(reading)
            if expected is None:
                expect_error(lambda: api.decode(*reading), api.InvalidReading,
                             "nonimage reading accepted")
            else:
                record = api.decode(*reading)
                inspect_record(record, expected)
                require(api.encode(record.coefficients) == reading,
                        "accepted reading exact re-encode")
            totals["image_classifications"] += 1

    arbitrary_traces = ((0, 0), (1, -2), (-9, 17), (2, 3),
                        (10**30, -10**31))
    for traces in arbitrary_traces:
        for digits in itertools.product(range(5), repeat=6):
            reading = (*traces, digits)
            fwd = api_reading(api.T6(*reading), "all-reading T6")
            back = api_reading(api.T6_inverse(*reading), "all-reading inverse")
            require(fwd == oracle.step(reading), "all-reading forward formula")
            require(back == oracle.step(reading, True), "all-reading reverse formula")
            require(api.T6_inverse(*fwd) == reading and api.T6(*back) == reading,
                    "both all-reading inverse compositions")
            require((oracle.decode(reading) is None) ==
                    (oracle.decode(fwd) is None) ==
                    (oracle.decode(back) is None), "image membership preserved")
            totals["data_permutations"] += 1

    malformed_scalars = [None, True, 3, "1000", {}, (), (1, 0, 0),
                         (1, 0, 0, 0, 0), (True, 0, 0, 0),
                         (1.0, 0, 0, 0), ("1", 0, 0, 0),
                         iter((1, 0, 0, 0)), ZERO, (6, 0, 0, 0)]
    for value in malformed_scalars:
        expect_error(lambda: api.encode(value), ValueError,
                     "malformed/out-of-domain scalar accepted")
        totals["malformed_cases"] += 1
    good_digits = (1, 0, 0, 0, 0, 0)
    bad_readings = [(x, 3, good_digits) for x in (None, True, 2.0, "2")]
    bad_readings += [(2, x, good_digits) for x in (None, False, 3.0, "3")]
    bad_digits = [None, True, "100000", {}, (), (1,)*5, (1,)*7,
                  (True, 0, 0, 0, 0, 0), (1.0, 0, 0, 0, 0, 0),
                  ("1", 0, 0, 0, 0, 0), (-1, 0, 0, 0, 0, 0),
                  (5, 0, 0, 0, 0, 0), iter(good_digits)]
    bad_readings += [(2, 3, d) for d in bad_digits]
    for reading in bad_readings:
        for function in (api.decode, api.T6, api.T6_inverse):
            expect_error(lambda: function(*reading), api.InvalidReading,
                         "malformed reading accepted or wrong rejection class")
            totals["malformed_cases"] += 1
    return totals


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", type=Path,
                        default=Path(__file__).with_name("decoder.py"))
    parser.add_argument("--output-dir", "--out", dest="out", type=Path)
    args = parser.parse_args()
    api_bytes = args.api.read_bytes()
    api = load_api(args.api)
    oracle = Oracle()
    totals = audit(api, oracle)
    summary = {"status": "PASS", "checks": CHECKS, "coverage": totals,
               "api_sha256": hashlib.sha256(api_bytes).hexdigest(),
               "method": "polynomial ring and inverse-ideal-matrix oracle",
               "scope": "frozen lambda-six interface; one execution environment"}
    output = args.out
    if output is None and os.environ.get("TWISTJ_EVIDENCE_DIR"):
        output = Path(os.environ["TWISTJ_EVIDENCE_DIR"])/"independent"
    if output is not None:
        output.mkdir(parents=True, exist_ok=False)
        (output/"SUMMARY.json").write_text(json.dumps(summary, sort_keys=True,
                                                   indent=2)+"\n", encoding="utf-8")
    sys.stdout.buffer.write((json.dumps(summary, sort_keys=True,
                                       separators=(",", ":"))+"\n").encode("utf-8"))


if __name__ == "__main__":
    main()
