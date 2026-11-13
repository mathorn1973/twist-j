"""Supplemental exact fixture audit for the common ENC4 proposal."""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import sys

if not __debug__:
    raise SystemExit("ENC4 review reproduction requires Python without optimization")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "probes" / "P-METRO-ENC4-CLOSURE-1"))

from check import canonical_maps, parse_axes, validate
from common import aligned, system
from generate import certificate


CONVENTIONS = ("MSD-E0", "MSD-Z0", "LSD-E0", "LSD-Z0")
ID = (0, 1)
SWAP = (1, 0)


def fixture(axes, weights, starts=(0,), conv="MSD-E0"):
    return {"q": len(axes[0]), "digits": [[list(d) for d in a] for a in axes],
            "starts": list(starts), "convention": conv,
            "weights": [[str(x) for x in row] for row in weights]}


def digits(n, q, conv):
    if not n:
        return [0] if conv.endswith("Z0") else []
    result = []
    while n:
        n, d = divmod(n, q)
        result.append(d)
    return result[::-1] if conv.startswith("MSD") else result


def point(obj, start, index):
    for axis, n in zip(obj["digits"], index):
        for d in digits(n, obj["q"], obj["convention"]):
            start = axis[d][start]
    return tuple(map(Q, obj["weights"][start]))


def average(rows):
    return tuple(sum(col) / len(rows) for col in zip(*rows))


def normalize(row):
    total = sum(row)
    return tuple(x / total for x in row) if total else None


def record(obj):
    cert = certificate(obj)
    validate(obj, cert)
    return cert


def complete_set(obj, cert):
    s = system(obj)
    tables, _ = parse_axes(s, cert["axes"])
    maps = tuple(canonical_maps(s, axis) for axis in s.digits)
    return {row for row, _ in aligned(s, tables, maps)}


def verdict(cert):
    return tuple((cert[key]["status"], cert[key].get("limit")) for key in ("raw", "lit"))


def whole_limit_surface():
    # Each letter is a permutation. If letters differ, one uniform
    # variable digit makes the state uniform. Otherwise exponents 2
    # and 3 exhaust both parities. Prefixes 1 and 2 exhaust possible
    # fixed maps under equal letters, and are immaterial under mixing.
    for conv, axis, starts, weights in product(
        CONVENTIONS, product((ID, SWAP), repeat=2), ((0,), (1,), (0, 1)),
        product((0, 1), repeat=2),
    ):
        obj = fixture((axis, (ID, ID)), [(x,) for x in weights], starts, conv)
        exact = {average([point(obj, s, (n, 1)) for n in range(c * 2**k, (c + 1) * 2**k)])
                 for s, c, k in product(starts, (1, 2), (2, 3))}
        assert complete_set(obj, record(obj)) == exact

    # Two nontrivial independent axes with two distinct residues each.
    states = list(product(range(2), repeat=2))
    first = tuple(states.index((1 - x, y)) for x, y in states)
    second = tuple(states.index((x, 1 - y)) for x, y in states)
    obj = fixture(((first, first), (second, second)), [(x, y) for x, y in states])
    assert complete_set(obj, record(obj)) == {tuple(map(Q, pair)) for pair in states}
    print("Full aligned-limit sets: 192 permutation cases and one active product")


def transport_equal(original, transported, starts, indices=lambda n: n):
    for start in original["starts"]:
        for index in product(range(16), repeat=2):
            assert point(original, start, index) == point(transported, starts[start], indices(index))
    old, new = record(original), record(transported)
    assert verdict(old) == verdict(new)
    assert complete_set(original, old) == complete_set(transported, new)


def quotient(obj, classes):
    representatives = [classes.index(i) for i in range(len(set(classes)))]
    axes = []
    for axis in obj["digits"]:
        maps = []
        for digit in axis:
            image = [classes[digit[s]] for s in representatives]
            assert all(image[classes[s]] == classes[digit[s]] for s in range(len(classes)))
            maps.append(image)
        axes.append(maps)
    assert all(obj["weights"][s] == obj["weights"][representatives[c]]
               for s, c in enumerate(classes))
    return fixture(axes, [obj["weights"][s] for s in representatives],
                   sorted({classes[s] for s in obj["starts"]}), obj["convention"])


def block(obj, initialized=False):
    assert obj["q"] == 2
    msd = obj["convention"].startswith("MSD")
    assert msd or not initialized
    states = list(product(range(len(obj["weights"])), range(4 if initialized else 1)))
    axes = []
    for i, axis in enumerate(obj["digits"]):
        maps = []
        for u in range(4):
            high, low = divmod(u, 2)
            word = [high, low] if msd else [low, high]
            image = []
            for state, flags in states:
                letters = word
                updated = flags
                if initialized and not flags & (1 << i):
                    letters = digits(u, 2, obj["convention"])
                    updated |= 1 << i
                for d in letters:
                    state = axis[d][state]
                image.append(states.index((state, updated)))
            maps.append(image)
        axes.append(maps)
    starts = {s: states.index((s, 0)) for s in obj["starts"]}
    result = fixture(axes, [obj["weights"][s] for s, _ in states],
                     starts.values(), obj["convention"])
    if not initialized:
        # For this fixture, zero-padding is identity before or after
        # the first nonzero digit, proving Pre_blk for every index.
        assert all(axis[0] == list(range(len(states))) for axis in obj["digits"])
    return result, starts


def reductions():
    ident = list(range(5))
    swap = [1, 0, 3, 2, 4]
    for conv in CONVENTIONS:
        obj = fixture(((ident, swap), (ident, ident)), [(2,), (4,), (2,), (4,), (9,)],
                      (0, 2), conv)
        # Both allowed-start components are closed, and state 4 is unreachable.
        reduced = fixture([[d[:4] for d in axis] for axis in obj["digits"]],
                          obj["weights"][:4], obj["starts"], conv)
        transport_equal(obj, reduced, {0: 0, 2: 2})
        perm = [3, 0, 4, 1, 2]
        transport_equal(obj, quotient(obj, perm), dict(enumerate(perm)))
        classes = [0, 1, 0, 1, 2]
        transport_equal(obj, quotient(obj, classes), dict(enumerate(classes)))
        swapped = deepcopy(obj)
        swapped["digits"].reverse()
        transport_equal(obj, swapped, {0: 0, 2: 2}, lambda n: n[::-1])
        blocked, starts = block(obj)
        transport_equal(obj, blocked, starts)
        if conv.startswith("MSD"):
            # Zero acts by a swap. Initialized flags matter for
            # the high base-four digit of an odd-length word.
            src = fixture(((SWAP, SWAP), (ID, ID)), [(1, 0), (0, 1)], conv=conv)
            blocked, starts = block(src, initialized=True)
            assert point(src, 0, (1, 0)) != point(src, 0, (3, 0))
            transport_equal(src, blocked, starts)
    print("Reduction fixtures: 22 exact transports with stream and certificate comparisons")


def normalization_and_zero():
    obj = fixture(((ID, SWAP), (ID, ID)), [(3, 0), (0, 1)])
    rows = [point(obj, 0, (x, y)) for x, y in product(range(2, 4), range(2))]
    assert normalize(average(rows)) == (Q(3, 4), Q(1, 4))
    assert average([normalize(row) for row in rows]) == (Q(1, 2), Q(1, 2))
    assert record(obj)["lit"]["limit"] == ["3/4", "1/4"]

    obj = fixture((((1, 1), ID), (ID, ID)), [(1,), (0,)])
    cert = record(obj)
    assert verdict(cert) == (("RAW", ["0"]), ("REJECT", None))
    assert cert["lit"]["reason"] == "tag-split"
    # Prefix 1 retains the unique all-ones path of positive mass.
    # Prefix 2 ("10") puts all paths in absorbing zero before padding.
    for k in range(7):
        assert average([point(obj, 0, (n, 1)) for n in range(2**k, 2**(k+1))]) == (Q(1, 2**k),)
        assert all(point(obj, 0, (n, 1)) == (0,) for n in range(2 * 2**k, 3 * 2**k))
    bad = deepcopy(cert)
    bad["lit"]["zero"] = {"start": 0, "words": [[1], [1]], "residues": [0, 0]}
    try:
        validate(obj, bad)
    except ValueError as error:
        assert str(error) == "claimed zero family contains positive mass"
    else:
        raise AssertionError("positive MSD tail accepted as a zero family")
    print("Normalization order and MSD transient zero family: exact")


def spectral():
    # An unreachable output component adds a kernel dimension.
    # In the two reachable coordinates, the two letter averages
    # are projection onto (1,1) and identity respectively.
    obj = fixture((((0, 1, 2), (1, 0, 2)), ((0, 1, 2), (0, 1, 2))),
                  [(1, 0), (0, 1), (0, 2)])
    # Separate the unreachable direction from the constant reachable
    # direction using an extra output coordinate.
    for i, row in enumerate(obj["weights"]):
        row.append(str(int(i == 2)))
    cert = record(obj)
    aux = cert["auxiliary"]
    assert (aux["module_dimension"], aux["kernel_dimension"], aux["quotient_dimension"]) == (3, 1, 2)
    assert aux["axes"][0]["average"]["data"] == [["1/2", "1/2"], ["1/2", "1/2"]]
    assert aux["axes"][1]["average"]["data"] == [["1", "0"], ["0", "1"]]

    # On the reachable two-dimensional span, P = (1/2)I + N,
    # with N nonzero and N^2=0. No factorization oracle is needed.
    obj = fixture((((0, 1, 2), (1, 2, 2)), ((0, 1, 2), (0, 1, 2))),
                  [(0,), (1,), (0,)])
    aux = record(obj)["auxiliary"]
    assert aux["quotient_dimension"] == 2
    matrix = [[Q(x) for x in row] for row in aux["axes"][0]["average"]["data"]]
    nilpotent = [[x - Q(i == j, 2) for j, x in enumerate(row)] for i, row in enumerate(matrix)]
    assert any(x for row in nilpotent for x in row)
    assert all(sum(nilpotent[i][k] * nilpotent[k][j] for k in range(2)) == 0
               for i, j in product(range(2), repeat=2))
    primary, = aux["axes"][0]["primary"]
    assert primary["nullities"] == [0, 1, 2]
    assert primary["blocks"] == [{"size": 2, "count_per_root": 1}]
    print("Independent quotient dimensions, averaging entries, and Jordan size: exact")


if __name__ == "__main__":
    sys.stdout.reconfigure(newline="\n")
    whole_limit_surface()
    reductions()
    normalization_and_zero()
    spectral()
    print("PASS ENC4 supplemental review reproduction")
