"""Saved-file cross-check at the smallest registered volume."""
from decimal import Decimal, localcontext
import hashlib
from pathlib import Path
import sys

import numpy as np

from ordered_reader import read_measures
from reference_reader import load_state, read_amplitudes, read_query
from test_ordered_reader import state_bytes


def exact_value(record):
    with localcontext() as ctx:
        ctx.prec = 80
        root2, root5 = Decimal(2).sqrt(), Decimal(5).sqrt()
        a = (2 + root2).sqrt() / 2
        b = root2 / 2
        c = (2 - root2).sqrt() / 2
        short = [1, a, b, c, 0, -c, -b, -a, -1]
        cosines = short + short[-2:0:-1]
        assert record["root_order"] == 16
        return sum((x + y*root5)*z for (x, y), z in zip(record["coefficients"], cosines)) / record["denominator"]


def check(path):
    links = np.zeros((16,)*4+(4,), dtype=np.uint8)
    for point, value in {
        (0, 0, 0, 0, 0): 1, (0, 4, 0, 0, 0): 2,
        (15, 15, 1, 15, 0): 1, (15, 3, 1, 15, 0): 4,
        (1, 1, 0, 15, 2): 1, (1, 5, 0, 15, 2): 3,
    }.items():
        links[point] = value
    try:
        with path.open("xb") as file:
            file.write(data := state_bytes(links))
    except FileExistsError:
        raise RuntimeError("Use a new fixture path")
    try:
        digest = hashlib.sha256(data).hexdigest()
        raw = load_state(path, digest)
        computed = read_measures(path, digest, (4,), (4,))["observables"]
        amps = read_amplitudes(raw, 4)
        expected = {}
        for label in ("E", "M"):
            expected[f"A:{label}:4"] = amps[f"A_{label}"]["value"]
            expected[f"A0:{label}:4"] = amps[f"A_{label}"]["zero_mode"]
            for item in amps[f"C_{label}"]:
                if item["lag"] != 4:
                    expected[f"Acheck:{label}:4:{item['lag']}"] = item["value"]
        for label, index in (("pi/4", 2), ("pi/2", 4)):
            for orient in ((1, 2), (0, 1), (0, 2), (0, 3)):
                row = read_query(raw, 1, index, 2, orient, 4)
                key = f"D:4:{label}:{orient[0]}{orient[1]}:2"
                expected[key] = row["D"]
        assert set(expected) == set(computed), (set(expected)-set(computed), set(computed)-set(expected))
        for key, value in expected.items():
            lo, hi = map(Decimal, computed[key])
            assert lo <= exact_value(value) <= hi, key
        print(f"REGISTERED L16 FIXTURE PASS {len(expected)} observable intervals")
    finally:
        path.unlink()


if __name__ == "__main__":
    check(Path(sys.argv[1]))
