#!/usr/bin/env python3
"""Post-run comparison of the independent review build with PR1879 digests.

NON-CANONICAL / L1. Written only after review.py had completed its full run.
The JSON serialization below (compact separators, ["C"|"SWAP",i,j] program
entries, [parameters, endpoint] per ordered triple in itertools.product order)
was read from the target verify.py solely to make the published digests
comparable. No target code is imported or executed; every word and endpoint
here comes from review.py's own construction and its own literal execution.

Usage:  python3 -I compare_after_run.py
"""

import hashlib
import itertools
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review as R  # noqa: E402  (own review module, same directory)

TARGET = {
    "complete_program_sha256":
        "a0e78fe4f4b430c76d4753fcbe7aed96cbfe43e340353cad2f4d1b8b56eeaeb6",
    "complete_inverse_program_sha256":
        "ccc21b191f368b4a2ae450cc6c5fd422f2edeb85f957a08d88348e43a000ed12",
    "complete_endpoint_sha256":
        "5fa52c61f2af6731eefcf9827cda7491e8fe9b2f54e420aa439c157a312755c1",
    "decoded_history_sha256":
        "bff60f741c325dc5c3a27bc737c389c37466d93bb267f16ef2f9198b6e42e46c",
}


def compact(value):
    return json.dumps(value, separators=(",", ":")).encode("ascii")


def main():
    segs, n = R.program(3)
    R.need(n == 101, "k=3 carrier")
    flat = []
    for _, _, wd in segs:
        flat += wd
    inv = R.literal_inverse(flat)
    ser = lambda word: [["SWAP" if kind else "C", i, k] for kind, i, k in word]
    got = {
        "complete_program_sha256": hashlib.sha256(compact(ser(flat))).hexdigest(),
        "complete_inverse_program_sha256": hashlib.sha256(compact(ser(inv))).hexdigest(),
    }
    arch, _, _ = R.layout(3)
    ends, hist = hashlib.sha256(), hashlib.sha256()
    for tup in itertools.product(R.INPUTS, repeat=3):
        st = R.ids(R.initial(3, tup))
        for _, _, wd in segs:
            R.run(st, wd)
        endpoint = [list(R.VALS[x]) for x in st]
        ends.update(compact([[list(p) for p in tup], endpoint]))
        labels = []
        for a, d in arch:
            labels += [R.decode_bank(endpoint_slice(endpoint, a)),
                       R.decode_bank(endpoint_slice(endpoint, d))]
        decoded = []
        for pa, pb in zip(labels[::2], labels[1::2]):
            dd = (pa - pb) % 5
            decoded.append([0 if dd == 1 else 1, (-pa) % 5])
        R.need(decoded == [list(p) for p in tup], "decoded")
        hist.update(compact([[list(p) for p in tup], labels, decoded]))
    got["complete_endpoint_sha256"] = ends.hexdigest()
    got["decoded_history_sha256"] = hist.hexdigest()
    for key in sorted(TARGET):
        status = "MATCH" if got[key] == TARGET[key] else "DIFFER"
        print("%s %s %s" % (status, key, got[key]))
    if any(got[k] != TARGET[k] for k in TARGET):
        raise SystemExit("FAIL: digest difference")
    print("ALL FOUR PR1879 DIGESTS REPRODUCED FROM THE INDEPENDENT BUILD")


def endpoint_slice(endpoint, base):
    return [tuple(v) for v in endpoint[base:base + 10]]


if __name__ == "__main__":
    main()
