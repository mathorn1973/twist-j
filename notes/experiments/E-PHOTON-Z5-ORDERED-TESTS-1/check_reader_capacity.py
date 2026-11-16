"""Deterministic nonsampler construction and reader resource check."""
import argparse
from decimal import Decimal
import hashlib
import json
import platform
import resource
import time

import numpy as np

from ordered_reader import IntegrityError, SCHEMA, measure_bytes


A_ROWS = {16:(4,), 24:(4,6), 32:(4,8), 36:(6,), 40:(), 48:(6,8), 64:(8,)}
B_ROWS = {16:(4,), 24:(4,6), 32:(4,8), 36:(), 40:(6,), 48:(6,8), 64:(8,)}


def constructed_state(side, pattern):
    count = 4*side**4
    digits = np.full(count, ord("0"), dtype=np.uint8)
    if pattern == "dense":
        for start in range(0, count, 1 << 20):
            stop = min(start + (1 << 20), count)
            word = np.arange(start, stop, dtype=np.uint32)
            word ^= word >> 16
            word *= np.uint32(0x7feb352d)
            word ^= word >> 15
            word *= np.uint32(0x846ca68b)
            word ^= word >> 16
            digits[start:stop] = (word % 5).astype(np.uint8) + ord("0")
    else:
        cells = digits.reshape((side,)*4 + (4,))
        profile = np.array([0, 1, 3, 4, 3, 1, 0, 4], dtype=np.uint8)
        cells[..., 0] = profile[np.arange(side) % 8][None, :, None, None] + ord("0")
    return b"\n".join((SCHEMA, f"L={side}".encode(), b"CHAIN=capacity-fixture",
                       b"SAMPLE=0", b"MACROCYCLE=0", b"LINKS="+digits.tobytes(),
                       b"END", b""))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--side", type=int, choices=tuple(A_ROWS), required=True)
    parser.add_argument("--pattern", choices=("dense", "coherent"), default="dense")
    parser.add_argument("--secondary", action="store_true")
    args = parser.parse_args()
    data = constructed_state(args.side, args.pattern)
    sha256 = hashlib.sha256(data).hexdigest()
    start = time.perf_counter()
    result = {
        "numpy": np.__version__,
        "architecture": platform.machine(),
        "longdouble_mantissa_bits": np.finfo(np.longdouble).nmant + 1,
        "side": args.side, "pattern": args.pattern, "secondary": args.secondary,
        "state_bytes": len(data),
    }
    try:
        record = measure_bytes(data, sha256, A_ROWS[args.side], B_ROWS[args.side],
                               secondary=args.secondary)
    except IntegrityError as exc:
        result["integrity_stop"] = str(exc)
    else:
        intervals = record["observables"]
        result["keys"] = len(intervals)
        result["json_bytes"] = len(json.dumps(record, separators=(",", ":")))
        result["max_halfwidth"] = str(max((Decimal(hi)-Decimal(lo))/2
                                         for lo, hi in intervals.values()))
        result["nonzero_intervals"] = sum(
            not Decimal(lo) <= 0 <= Decimal(hi) for lo, hi in intervals.values()
        )
    result["reader_seconds"] = round(time.perf_counter()-start, 3)
    result["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
