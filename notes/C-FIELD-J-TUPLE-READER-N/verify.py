#!/usr/bin/env python3
"""NON-CANONICAL tuple-reader successor; run only after its public pin.

Standalone Python 3.10+ exact arithmetic. No predecessor imports or file I/O.
The complete input contract and immutable mathematical sources are in PREREG.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import json
import sys


BOX = ((-3, 3), (-2, 2), (-2, 2), (-3, 3))
ZERO = (0, 0, 0, 0)
C = ((0, 1, 0, 0), (0, 0, 1, -1), (1, -1, 0, -1), (0, 1, -2, 1))
AF = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
BF = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))


def normalize(value):
    """Read only genuine builtin tuple storage; never dispatch input hooks."""
    if not issubclass(type(value), tuple):
        return None
    if tuple.__len__(value) != 3:
        return None
    e0 = tuple.__getitem__(value, 0)
    e1 = tuple.__getitem__(value, 1)
    residue = tuple.__getitem__(value, 2)
    if type(e0) is not int or type(e1) is not int:
        return None
    if not issubclass(type(residue), tuple):
        return None
    if tuple.__len__(residue) != 4:
        return None
    slots = tuple(tuple.__getitem__(residue, i) for i in range(4))
    if any(type(x) is not int for x in slots):
        return None
    if any(x < 0 or x > 4 for x in slots):
        return None
    return e0, e1, slots


def coefficient_energies(a):
    x0, x1, x2, x3 = a
    squares = x0*x0 + x1*x1 + x2*x2 + x3*x3
    return (squares - x0*x2 - x0*x3 - x1*x3,
            squares - x0*x1 - x1*x2 - x2*x3)


def chart(a):
    a0, a1, a2, a3 = a
    return a1, a2-a3, a0-a1-a3, a1-2*a2+a3


def decode(value):
    datum = normalize(value)
    if datum is None:
        return None
    e0, e1, residue = datum
    if not (0 <= e0 <= 5 and 0 <= e1 <= 13):
        return None
    if e0 == 0:
        return (ZERO, ZERO) if e1 == 0 and residue == ZERO else None
    n = -e0*e0 + 3*e0*e1 - e1*e1
    if not 1 <= n <= 31:
        return None
    lifts = [tuple(x for x in range(lo, hi + 1) if x % 5 == r)
             for (lo, hi), r in zip(BOX, residue)]
    match = None
    for a in product(*lifts):
        if coefficient_energies(a) == (e0, e1):
            if match is not None:
                return None
            match = a
    return None if match is None else (match, chart(match))


def mv(matrix, vector):
    return tuple(sum(x*y for x, y in zip(row, vector)) for row in matrix)


def field_energy(y):
    doubled = sum(x*z for x, z in zip(y, mv(BF, y)))
    assert doubled % 2 == 0
    return doubled // 2


def reference_image():
    """Reference uses field matrices, not the reader's coefficient formulas."""
    image, shells, norms = {}, Counter(), []
    scanned = 0
    for a in product(*(range(lo, hi + 1) for lo, hi in BOX)):
        scanned += 1
        y = mv(C, a)
        af2y = mv(AF, mv(AF, y))
        jfy = tuple(x + z for x, z in zip(y, af2y))
        e0, e1 = field_energy(y), field_energy(jfy)
        assert e0 >= 0
        assert coefficient_energies(a) == (e0, e1)
        assert chart(a) == y
        if e0 > 5:
            continue
        key = e0, e1, tuple(x % 5 for x in a)
        assert key not in image
        image[key] = a, y
        shells[e0] += 1
        n = -e0*e0 + 3*e0*e1 - e1*e1
        assert 0 <= n <= 31 and 0 <= e1 <= 13
        norms.append(n)
    counts = [shells[i] for i in range(6)]
    assert scanned == 1225 and len(image) == 291
    assert counts == [1, 20, 30, 60, 60, 120] and max(norms) == 31
    return image, {"box_scanned": scanned, "states": len(image),
                   "shells": counts, "max_norm": max(norms)}


def tripwire(*args, **kwargs):
    raise AssertionError("An input override was invoked")


class PlainTuple(tuple):
    pass


class HostileTuple(tuple):
    __len__ = tripwire
    __getitem__ = tripwire
    __iter__ = tripwire
    __getattribute__ = tripwire
    __eq__ = tripwire
    __ne__ = tripwire
    __hash__ = tripwire
    __bool__ = tripwire
    __str__ = tripwire
    __repr__ = tripwire
    __setattr__ = tripwire
    __delattr__ = tripwire


WRAPPERS = (tuple, PlainTuple, HostileTuple)


def wrap(key, outer, inner):
    e0, e1, residue = key
    stored_residue = tuple.__new__(inner, residue)
    return tuple.__new__(outer, (e0, e1, stored_residue))


def check_output(actual, expected):
    if expected is None:
        assert actual is None
        return
    assert type(actual) is tuple and len(actual) == 2
    assert all(type(part) is tuple and len(part) == 4 for part in actual)
    assert all(type(x) is int for part in actual for x in part)
    assert actual == expected


def complete_keys(image):
    residues = tuple(product(range(5), repeat=4))
    combinations = tuple(product(WRAPPERS, repeat=2))
    calls, accepted = 0, 0
    for e0, e1, residue in product(range(6), range(14), residues):
        key = e0, e1, residue
        expected = image.get(key)
        for outer, inner in combinations:
            value = wrap(key, outer, inner)
            assert normalize(value) == key
            result = decode(value)
            check_output(result, expected)
            calls += 1
            accepted += result is not None
    assert calls == 472500 and accepted == 9 * 291
    outside = 0
    for e0, e1, residue in product((-1, 6), (-1, 0, 1, 13, 14, 10000), residues):
        for outer, inner in combinations:
            assert decode(wrap((e0, e1, residue), outer, inner)) is None
            outside += 1
    for e0, e1, residue in product(range(6), (-1, 14, 10000), residues):
        for outer, inner in combinations:
            assert decode(wrap((e0, e1, residue), outer, inner)) is None
            outside += 1
    assert outside == 168750
    return {"keys": 52500, "wrapper_combinations": 9,
            "reader_calls": calls, "accepted_calls": accepted,
            "outside_keys": 18750, "outside_reader_calls": outside}


class IntSubclass(int):
    pass


class HostileInt(int):
    __eq__ = tripwire
    __lt__ = tripwire
    __gt__ = tripwire
    __int__ = tripwire
    __index__ = tripwire
    __getattribute__ = tripwire
    __bool__ = tripwire
    __repr__ = tripwire


class ForgedClass:
    @property
    def __class__(self):
        return tuple


class HostileClass:
    __getattribute__ = tripwire
    __len__ = tripwire
    __iter__ = tripwire
    __getitem__ = tripwire
    __eq__ = tripwire
    __bool__ = tripwire
    __repr__ = tripwire


class OuterFacade(tuple):
    def __len__(self):
        return 3

    def __getitem__(self, index):
        return (0, 0, ZERO)[index]

    def __iter__(self):
        return iter((0, 0, ZERO))


class ResidueFacade(tuple):
    def __len__(self):
        return 4

    def __getitem__(self, index):
        return ZERO[index]

    def __iter__(self):
        return iter(ZERO)


def regressions():
    zero_result = ZERO, ZERO
    # The two preserved predecessor failures must now succeed independently.
    check_output(decode(tuple.__new__(PlainTuple, (0, 0, ZERO))), zero_result)
    check_output(decode((0, 0, tuple.__new__(PlainTuple, ZERO))), zero_result)
    bad_values = (
        None, [], {}, 0, (), (0,), (0, 0), (0, 0, ZERO, 0),
        ([0], 0, ZERO), (True, 0, ZERO), (0, False, ZERO),
        (Fraction(0), 0, ZERO), (0, "0", ZERO), (0, 0, [0, 0, 0, 0]),
        (0, 0, (0, 0, 0)), (0, 0, (0, 0, 0, 0, 0)),
        (0, 0, (False, 0, 0, 0)), (0, 0, (Fraction(0), 0, 0, 0)),
        (0, 0, (-1, 0, 0, 0)), (0, 0, (5, 0, 0, 0)),
        (IntSubclass(0), 0, ZERO), (0, IntSubclass(0), ZERO),
        (0, 0, (IntSubclass(0), 0, 0, 0)),
        (HostileInt(0), 0, ZERO), (0, HostileInt(0), ZERO),
        (0, 0, (HostileInt(0), 0, 0, 0)),
        ForgedClass(), HostileClass(), (0, 0, ForgedClass()),
        (0, 0, HostileClass()), (HostileClass(), 0, ZERO),
        (0, 0, (HostileClass(), 0, 0, 0)),
    )
    malformed_calls = 0
    for value in bad_values:
        assert normalize(value) is None and decode(value) is None
        malformed_calls += 1
        if type(value) is tuple:
            for outer in (PlainTuple, HostileTuple):
                wrapped = tuple.__new__(outer, value)
                assert normalize(wrapped) is None and decode(wrapped) is None
                malformed_calls += 1
    # Bad underlying residue slots must stay bad even behind hostile methods.
    for residue in ((), (0, 0, 0), (0, 0, 0, 0, 0), (False, 0, 0, 0),
                    (-1, 0, 0, 0), (5, 0, 0, 0), (HostileInt(0), 0, 0, 0)):
        for outer, inner in product(WRAPPERS, repeat=2):
            value = wrap((0, 0, residue), outer, inner)
            assert normalize(value) is None and decode(value) is None
            malformed_calls += 1
    # Public fake views neither erase valid underlying data nor create data.
    fake_outer_valid = tuple.__new__(OuterFacade, (1, 1, (1, 0, 0, 0)))
    fake_inner_valid = tuple.__new__(ResidueFacade, (1, 0, 0, 0))
    expected_one = (1, 0, 0, 0), (0, 0, 1, 0)
    check_output(decode(fake_outer_valid), expected_one)
    check_output(decode((1, 1, fake_inner_valid)), expected_one)
    assert decode(tuple.__new__(OuterFacade, ())) is None
    assert decode((0, 0, tuple.__new__(ResidueFacade, (0, 0, 0)))) is None
    assert decode(tuple.__new__(OuterFacade, (0, 0, (5, 0, 0, 0)))) is None
    # Mutable metadata exists but is not accessed, copied, changed or removed.
    inner = tuple.__new__(HostileTuple, ZERO)
    outer = tuple.__new__(HostileTuple, (0, 0, inner))
    outer_marker, inner_marker = {"values": [7]}, {"values": [11]}
    object.__setattr__(outer, "marker", outer_marker)
    object.__setattr__(inner, "marker", inner_marker)
    check_output(decode(outer), zero_result)
    outer_dict = object.__getattribute__(outer, "__dict__")
    inner_dict = object.__getattribute__(inner, "__dict__")
    assert set(outer_dict) == set(inner_dict) == {"marker"}
    assert outer_dict["marker"] is outer_marker and outer_marker == {"values": [7]}
    assert inner_dict["marker"] is inner_marker and inner_marker == {"values": [11]}
    huge = 10 ** 10000
    large_calls = 0
    for e0, e1 in ((huge, 0), (-huge, 0), (0, huge), (1, huge), (5, -huge)):
        for outer, inner in product(WRAPPERS, repeat=2):
            assert decode(wrap((e0, e1, ZERO), outer, inner)) is None
            large_calls += 1
    one, j = (1, 0, 0, 0), (0, 1, 0, 0)
    check_output(decode((1, 1, one)), (one, chart(one)))
    check_output(decode((1, 1, j)), (j, chart(j)))
    assert decode((1, 1, one)) != decode((1, 1, j))
    return {"original_counterexamples": 2, "malformed_calls": malformed_calls,
            "lying_view_cases": 5, "metadata_case": 1,
            "large_integer_calls": large_calls, "valid_substitution_cases": 2}


def main():
    if sys.flags.optimize:
        raise RuntimeError("Exact audit requires assertions enabled")
    image, sector = reference_image()
    finite = complete_keys(image)
    fixtures = regressions()
    result = {"candidate": "C-FIELD-J-TUPLE-READER-N", "layer": "L1",
              "status": "PASS", "sector": sector, "complete_keys": finite,
              "regressions": fixtures,
              "scope": "total_underlying_tuple_storage_reader_only"}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
