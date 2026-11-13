"""Exact bounded audit of the proposed common ENC4 normalization theorem."""
from copy import deepcopy
from fractions import Fraction
from itertools import product
import hashlib
from pathlib import Path
import sys

PINNED_SOURCES = {
    "auxiliary.py": "fd7ee07ee5f559e943d9ebb590f6c0fb154b248506ba004cb7fcd6f18dc7e3fe",
    "check.py": "5a8fb2aa9d6bfbe302719ce0871576539c1f5043ec96944aa153c44a768b9ccf",
    "common.py": "27a5bac2040105bd092edc4a279e5f7a5673362de2cfb32bf183520f5019c7ab",
    "generate.py": "b6e3169260944d4bff772d8c68d0b8e261cc4076b08d6e1e52dfca6c1c444de4",
    "polynomial.py": "f1f3dcb0857d6054beeffe6f7811949e28083540f1a8ea0f5fad5b2236932e60",
    "../../notes/canon/METRO-ENC4-CLOSURE-2026-11-13.md": "af1da9656d78ea2589b6b2a70476dd1b30b56a4dc5ed5f9d7a49f0ab586a0846",
}


def check_pinned_sources():
    directory = Path(__file__).resolve().parent
    for path, digest in PINNED_SOURCES.items():
        assert hashlib.sha256((directory / path).read_bytes()).hexdigest() == digest, path

check_pinned_sources()

from check import validate
from common import modulus
from generate import certificate
from polynomial import factor


CONVENTIONS = ("MSD-E0", "MSD-Z0", "LSD-E0", "LSD-Z0")
ID = [0, 1]
SWAP = [1, 0]


def case(convention, axis, weights, starts=(0,)):
    n = len(weights)
    return {
        "q": 2, "convention": convention, "starts": list(starts),
        "digits": [[list(row) for row in axis], [list(range(n)) for _ in range(2)]],
        "weights": [[str(x) for x in row] for row in weights],
    }


def decide(obj, raw=None, lit=None):
    cert = certificate(obj)
    s = validate(obj, cert)
    if raw is not None:
        assert cert["raw"]["status"] == raw
    if lit is not None:
        assert cert["lit"]["status"] == lit
    return s, cert


def rejects(obj, cert, reason):
    try:
        validate(obj, cert)
    except ValueError as error:
        assert str(error) == reason
    else:
        raise AssertionError("checker accepted a tampered record")


def semantic_controls():
    for convention in CONVENTIONS:
        _, cert = decide(case(convention, [[1, 1], [1, 1]], [(1,), (0,)]),
                         "RAW", "ZERO" if convention.endswith("Z0") else "REJECT")
        assert cert["raw"]["limit"] == ["0"]
        _, cert = decide(case(convention, [SWAP, SWAP], [(1, 0), (0, 1)]),
                         "REJECT", "REJECT")
        assert cert["lit"]["reason"] == "direction-split"
        obj = case(convention, [SWAP, SWAP], [(1, 1), (Fraction(7, 3), Fraction(7, 3))])
        s, cert = decide(obj, "REJECT", "PROB")
        assert cert["lit"]["limit"] == ["1/2", "1/2"]
        assert modulus(s, cert["axes"], cert["lit"], Fraction(1, 100)) == 25200
    print("SEMANTICS cases=12 exact")


def witness_controls():
    obj = case("LSD-E0", [[3, 2, 3, 2], [1, 0, 3, 2]],
               [(2, 2), (2, 2), (0, 0), (1, 1)])
    _, cert = decide(obj, "REJECT", "REJECT")
    assert cert["lit"]["reason"] == "tag-split"
    bad = deepcopy(cert)
    bad["lit"]["zero"] = {"start": 0, "words": [[1], [1]], "residues": [1, 0]}
    rejects(obj, bad, "claimed zero family contains positive mass")

    # The two axes act on different Cartesian factors. They commute
    # and both period-two residues contribute to the limit set.
    states = list(product(range(2), repeat=2))
    axis = [[states.index((1 - x, y)) for x, y in states]] * 2
    other = [[states.index((x, 1 - y)) for x, y in states]] * 2
    obj = case("LSD-Z0", axis, [(1, 0), (0, 1), (0, 1), (1, 0)])
    obj["digits"][1] = other
    _, cert = decide(obj, "REJECT", "REJECT")
    assert [x["h"] for x in cert["axes"]] == [2, 2]
    assert cert["lit"]["reason"] == "direction-split"

    jordan = case("LSD-Z0", [[0, 1, 2], [1, 2, 2]], [(0,), (1,), (0,)])
    _, cert = decide(jordan, "RAW", "REJECT")
    records = cert["auxiliary"]["axes"][0]["primary"]
    assert any(block["size"] == 2 for row in records for block in row["blocks"])
    cert["auxiliary"]["quotient_dimension"] = 0
    rejects(jordan, cert, "auxiliary module/spectral data mismatch")
    x2_plus_one = tuple(map(Fraction, (1, 0, 1)))
    assert factor(tuple(map(Fraction, (1, 0, 2, 0, 1)))) == [(x2_plus_one, 2)]
    print("WITNESSES cases=3 tampering=2 polynomial=1 exact")


def point(maps, n, msd, z0, start):
    digits = []
    while n:
        n, digit = divmod(n, 2)
        digits.append(digit)
    if not digits and z0:
        digits.append(0)
    for digit in reversed(digits) if msd else digits:
        start = maps[digit][start]
    return start


def exact_aligned_mean(maps, weights, c, k, start, msd, z0):
    interval = range(c * 2**k, (c + 1) * 2**k)
    return Fraction(sum(weights[point(maps, n, msd, z0, start)] for n in interval), 2**k)


def finite_surface():
    # Independent pointwise enumeration on all permutations of two
    # states. This surface has no transient or decaying sector.
    # Prefixes 1 and 2 represent both parities of canonical length
    # whenever both digit actions coincide. For different maps the
    # uniform variable block averages exactly after its first digit.
    counts = [0, 0, 0]
    for convention, digits, starts, weights in product(
        CONVENTIONS, product((ID, SWAP), repeat=2), ((0,), (1,), (0, 1)),
        product((0, 1), repeat=2),
    ):
        msd = convention.startswith("MSD")
        z0 = convention.endswith("Z0")
        obj = case(convention, digits, [(w,) for w in weights], starts)
        g = {exact_aligned_mean(digits, weights, c, k, start, msd, z0)
             for c, k, start in product((1, 2), (2, 3), starts)}
        positive = any(weights[point(digits, n, msd, z0, start)]
                       for n, start in product(range(8), starts))
        raw = "RAW" if len(g) == 1 else "REJECT"
        lit = "ZERO" if not positive else "REJECT" if 0 in g else "PROB"
        _, cert = decide(obj, raw, lit)
        if raw == "RAW":
            assert cert["raw"]["limit"] == [str(next(iter(g)))]
        if lit == "PROB":
            assert cert["lit"]["limit"] == ["1"]
            assert cert["lit"]["min_mass"] == str(min(g))
        counts[("ZERO", "PROB", "REJECT").index(lit)] += 1
    assert sum(counts) == 192
    print(f"SURFACE cases=192 ZERO={counts[0]} PROB={counts[1]} REJECT={counts[2]}")


def main():
    semantic_controls()
    witness_controls()
    finite_surface()
    print("PASS METRO ENC4 bounded exact audit")


if __name__ == "__main__":
    sys.stdout.reconfigure(newline="\n")
    main()
