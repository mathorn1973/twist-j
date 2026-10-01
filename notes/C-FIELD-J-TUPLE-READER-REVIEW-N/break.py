#!/usr/bin/env python3
"""Frozen independent tuple-storage and bounded scalar inverse audit."""

import argparse
import hashlib
import itertools
import pathlib
import types


C = ((0, 1, 0, 0), (0, 0, 1, -1),
     (1, -1, 0, -1), (0, 1, -2, 1))
AF = ((1, 0, 1, 0), (0, 1, 0, 1),
      (-2, 1, -1, 1), (1, -3, 1, -2))
BF = ((4, -2, 2, -1), (-2, 6, -1, 3),
      (2, -1, 2, 0), (-1, 3, 0, 2))
BOX = (range(-3, 4), range(-2, 3), range(-2, 3), range(-3, 4))
ZERO = (0, 0, 0, 0)
HOOK_EVENTS = []


def matrix_vector(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(4)) for row in matrix)


def field_energy(y):
    by = matrix_vector(BF, y)
    twice = sum(y[i] * by[i] for i in range(4))
    assert twice % 2 == 0
    return twice // 2


def coefficient_energies(a):
    p, q, r, s = a
    total = p*p + q*q + r*r + s*s
    return total-p*r-p*s-q*s, total-p*q-q*r-r*s


def normalize(value):
    if not issubclass(type(value), tuple) or tuple.__len__(value) != 3:
        return None
    e0 = tuple.__getitem__(value, 0)
    e1 = tuple.__getitem__(value, 1)
    residues = tuple.__getitem__(value, 2)
    if type(e0) is not int or type(e1) is not int:
        return None
    if not issubclass(type(residues), tuple) or tuple.__len__(residues) != 4:
        return None
    r0 = tuple.__getitem__(residues, 0)
    r1 = tuple.__getitem__(residues, 1)
    r2 = tuple.__getitem__(residues, 2)
    r3 = tuple.__getitem__(residues, 3)
    for entry in (r0, r1, r2, r3):
        if type(entry) is not int or not 0 <= entry < 5:
            return None
    return (e0, e1, (r0, r1, r2, r3))


def independent_reader(value):
    key = normalize(value)
    if key is None:
        return None
    e0, e1, residues = key
    if not 0 <= e0 <= 5 or not 0 <= e1 <= 13:
        return None
    if e0 == 0:
        return (ZERO, ZERO) if e1 == 0 and residues == ZERO else None
    norm = -e0*e0 + 3*e0*e1 - e1*e1
    if not 1 <= norm <= 31:
        return None
    lifts = tuple(tuple(a for a in interval if a % 5 == residue)
                  for interval, residue in zip(BOX, residues))
    answer = None
    for a in itertools.product(*lifts):
        if coefficient_energies(a) == (e0, e1):
            if answer is not None:
                return None
            answer = (a, matrix_vector(C, a))
    return answer


def forward_image():
    image = {}
    shells = [0] * 6
    largest_norm = 0
    count = 0
    for a in itertools.product(*BOX):
        count += 1
        y = matrix_vector(C, a)
        af2y = matrix_vector(AF, matrix_vector(AF, y))
        jy = tuple(y[i] + af2y[i] for i in range(4))
        energies = (field_energy(y), field_energy(jy))
        assert energies == coefficient_energies(a)
        assert energies[0] >= 0
        if energies[0] <= 5:
            e0, e1 = energies
            norm = -e0*e0 + 3*e0*e1 - e1*e1
            assert (a == ZERO and norm == 0) or 1 <= norm <= 31
            assert 0 <= e1 <= 13
            key = (e0, e1, tuple(x % 5 for x in a))
            assert key not in image
            image[key] = (a, y)
            shells[e0] += 1
            largest_norm = max(largest_norm, norm)
    assert count == 1225
    assert len(image) == 291
    assert tuple(shells) == (1, 20, 30, 60, 60, 120)
    assert largest_norm == 31
    return image


def forbidden(*args, **kwargs):
    HOOK_EVENTS.append(1)
    raise RuntimeError("forbidden input hook invoked")


class PlainTuple(tuple):
    pass


class DeepTuple(PlainTuple):
    pass


class HostileTuple(tuple):
    __getattribute__ = forbidden
    __getattr__ = forbidden
    __len__ = forbidden
    __getitem__ = forbidden
    __iter__ = forbidden
    __eq__ = forbidden
    __ne__ = forbidden
    __lt__ = forbidden
    __le__ = forbidden
    __gt__ = forbidden
    __ge__ = forbidden
    __hash__ = forbidden
    __bool__ = forbidden
    __str__ = forbidden
    __repr__ = forbidden
    __format__ = forbidden
    __contains__ = forbidden
    __reversed__ = forbidden
    __int__ = forbidden
    __index__ = forbidden
    __float__ = forbidden
    __reduce__ = forbidden
    __reduce_ex__ = forbidden
    __getnewargs__ = forbidden
    __sizeof__ = forbidden
    count = forbidden
    index = forbidden


class HostileMeta(type):
    __getattribute__ = forbidden
    __eq__ = forbidden
    __ne__ = forbidden
    __hash__ = forbidden
    __instancecheck__ = forbidden
    __subclasscheck__ = forbidden
    __repr__ = forbidden
    __str__ = forbidden
    __mro__ = property(forbidden)
    __bases__ = property(forbidden)


class MetaTuple(HostileTuple, metaclass=HostileMeta):
    pass


class HostileObject:
    __getattribute__ = forbidden
    __len__ = forbidden
    __getitem__ = forbidden
    __iter__ = forbidden
    __eq__ = forbidden
    __hash__ = forbidden
    __bool__ = forbidden
    __int__ = forbidden
    __index__ = forbidden
    __repr__ = forbidden
    __str__ = forbidden


class MetaObject(HostileObject, metaclass=HostileMeta):
    pass


class ForgingMeta(type):
    @property
    def __mro__(cls):
        HOOK_EVENTS.append(1)
        return (tuple, object)

    @property
    def __bases__(cls):
        HOOK_EVENTS.append(1)
        return (tuple,)


class MroFacade(metaclass=ForgingMeta):
    pass


class ForgedTuple:
    @property
    def __class__(self):
        HOOK_EVENTS.append(1)
        return tuple

    __len__ = forbidden
    __getitem__ = forbidden
    __iter__ = forbidden


class ForgedHostileTuple:
    @property
    def __class__(self):
        HOOK_EVENTS.append(1)
        return MetaTuple


class ForgedInt:
    @property
    def __class__(self):
        HOOK_EVENTS.append(1)
        return int

    __int__ = forbidden
    __index__ = forbidden
    __eq__ = forbidden


class IntSubclass(int):
    __getattribute__ = forbidden
    __eq__ = forbidden
    __lt__ = forbidden
    __le__ = forbidden
    __int__ = forbidden
    __index__ = forbidden
    __hash__ = forbidden
    __bool__ = forbidden
    __repr__ = forbidden
    __add__ = forbidden
    __sub__ = forbidden
    __mul__ = forbidden
    __mod__ = forbidden
    __pow__ = forbidden
    __radd__ = forbidden
    __rsub__ = forbidden
    __rmul__ = forbidden
    __rmod__ = forbidden


class LyingTuple(tuple):
    def __len__(self):
        HOOK_EVENTS.append(1)
        return 3

    def __getitem__(self, index):
        HOOK_EVENTS.append(1)
        return (0, 0, ZERO)[index % 3]

    def __iter__(self):
        HOOK_EVENTS.append(1)
        return iter((0, 0, ZERO))

    @property
    def __class__(self):
        HOOK_EVENTS.append(1)
        return list


CLASSES = (tuple, PlainTuple, HostileTuple, MetaTuple)


def check_output(reader, value, expected, label):
    before = len(HOOK_EVENTS)
    result = reader(value)
    assert len(HOOK_EVENTS) == before, (label, "input hook")
    if result is not None:
        assert type(result) is tuple and len(result) == 2, (label, "outer output")
        for vector in result:
            assert type(vector) is tuple and len(vector) == 4, (label, "vector output")
            assert all(type(x) is int for x in vector), (label, "integer output")
    assert result == expected, (label, "reader result")


def wrapped_key(key, outer, inner):
    residue = tuple.__new__(inner, key[2])
    return tuple.__new__(outer, (key[0], key[1], residue))


def semantic_keys():
    for e0 in range(6):
        for e1 in range(14):
            for residues in itertools.product(range(5), repeat=4):
                yield (e0, e1, residues)
    for e0 in (-1, 6):
        for e1 in (-1, 0, 1, 13, 14, 10000):
            for residues in itertools.product(range(5), repeat=4):
                yield (e0, e1, residues)
    for e0 in range(6):
        for e1 in (-1, 14, 10000):
            for residues in itertools.product(range(5), repeat=4):
                yield (e0, e1, residues)


def fixed_fixtures(image):
    fixtures = []

    def add(value, expected=None):
        fixtures.append((value, expected))

    hostile = HostileObject()
    forged_tuple = ForgedTuple()
    forged_int = ForgedInt()
    invalid_values = (None, False, True, 0, 1, 1.0, 0j, "", b"", bytearray(),
                      [], {}, set(), frozenset(), range(4), object(), hostile,
                      forged_tuple, forged_int, int.__new__(IntSubclass, 0),
                      MetaObject(), MroFacade(), ForgedHostileTuple())
    for value in invalid_values:
        add(value)
        for outer in CLASSES:
            add(tuple.__new__(outer, (0, 0, value)))

    # Underlying arities and contents, including poisoned would-be slots.
    for outer in CLASSES + (LyingTuple, DeepTuple):
        for stored in ((), (0,), (0, 0), (0, 0, ZERO, 0),
                       (hostile,), (hostile, hostile, hostile, hostile)):
            add(tuple.__new__(outer, stored))
        for inner in CLASSES + (LyingTuple, DeepTuple):
            for stored in ((), (0,), (0, 0, 0), (0, 0, 0, 0, 0),
                           (hostile,), (hostile, hostile, hostile, hostile)):
                add(tuple.__new__(outer, (0, 0, tuple.__new__(inner, stored))))

    bad_numbers = (False, True, 0.0, 1.0, 0j, "0", None, [], {}, hostile,
                   forged_int, int.__new__(IntSubclass, 0),
                   int.__new__(IntSubclass, 1))
    for value in bad_numbers:
        for outer in CLASSES:
            add(tuple.__new__(outer, (value, 0, ZERO)))
            add(tuple.__new__(outer, (0, value, ZERO)))
            for inner in CLASSES:
                for slot in range(4):
                    residues = [0, 0, 0, 0]
                    residues[slot] = value
                    add(tuple.__new__(outer, (0, 0, tuple.__new__(inner, residues))))

    huge = 1 << 100000
    for outer in CLASSES:
        for inner in CLASSES:
            for bad in (-huge, -1, 5, huge):
                for slot in range(4):
                    residues = [0, 0, 0, 0]
                    residues[slot] = bad
                    add(tuple.__new__(outer, (0, 0, tuple.__new__(inner, residues))))
            for e0, e1 in ((huge, huge), (-huge, 0), (0, huge),
                           (1, huge), (5, -huge), (0, -huge)):
                add(wrapped_key((e0, e1, ZERO), outer, inner))

    valid_keys = ((0, 0, ZERO), (1, 1, (1, 0, 0, 0)),
                  (1, 1, (0, 1, 0, 0)))
    # Include both predecessor false rejections verbatim in semantic content.
    add(tuple.__new__(PlainTuple, (0, 0, ZERO)), (ZERO, ZERO))
    add((0, 0, tuple.__new__(PlainTuple, ZERO)), (ZERO, ZERO))
    for outer in CLASSES + (LyingTuple, DeepTuple):
        for inner in CLASSES + (LyingTuple, DeepTuple):
            for key in valid_keys:
                add(wrapped_key(key, outer, inner), image[key])
            add(wrapped_key((0, 1, ZERO), outer, inner))
            add(wrapped_key((1, 1, ZERO), outer, inner))
    assert not HOOK_EVENTS
    return fixtures


def metadata_audit(reader):
    outer = tuple.__new__(PlainTuple, (0, 0, tuple.__new__(PlainTuple, ZERO)))
    inner = tuple.__getitem__(outer, 2)
    outer_state = {"items": [17, 23], "token": object()}
    inner_state = {"items": [31, 47], "token": object()}
    object.__setattr__(outer, "metadata", outer_state)
    object.__setattr__(inner, "metadata", inner_state)
    outer_dict = object.__getattribute__(outer, "__dict__")
    inner_dict = object.__getattribute__(inner, "__dict__")
    outer_token, inner_token = outer_state["token"], inner_state["token"]
    check_output(reader, outer, (ZERO, ZERO), "metadata")
    assert tuple(outer_dict) == ("metadata",) and outer_dict["metadata"] is outer_state
    assert tuple(inner_dict) == ("metadata",) and inner_dict["metadata"] is inner_state
    assert outer_state["items"] == [17, 23] and outer_state["token"] is outer_token
    assert inner_state["items"] == [31, 47] and inner_state["token"] is inner_token
    assert tuple(outer_state) == ("items", "token")
    assert tuple(inner_state) == ("items", "token")


def audit_reader(reader, image, fixtures):
    keys = calls = 0
    for key in semantic_keys():
        expected = image.get(key)
        for outer in CLASSES:
            for inner in CLASSES:
                check_output(reader, wrapped_key(key, outer, inner), expected,
                             (keys, calls % 16))
                calls += 1
        keys += 1
    assert keys == 71250 and calls == 1140000
    for index, (value, expected) in enumerate(fixtures):
        check_output(reader, value, expected, ("fixture", index))
    metadata_audit(reader)
    assert not HOOK_EVENTS
    return keys, calls, len(fixtures)


def load_candidate(path, expected_hash, reader_name):
    source = pathlib.Path(path).read_bytes()
    actual_hash = hashlib.sha256(source).hexdigest()
    if actual_hash != expected_hash:
        raise RuntimeError("candidate SHA-256 differs from public pin")
    module = types.ModuleType("independently_frozen_candidate_comparison")
    module.__file__ = str(path)
    exec(compile(source, str(path), "exec"), module.__dict__)
    reader = module.__dict__[reader_name]
    if not callable(reader):
        raise RuntimeError("candidate reader is not callable")
    return reader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate")
    parser.add_argument("--sha256")
    parser.add_argument("--reader")
    args = parser.parse_args()
    if bool(args.candidate) != bool(args.sha256) or bool(args.candidate) != bool(args.reader):
        parser.error("candidate, sha256 and reader must be supplied together")
    image = forward_image()
    fixtures = fixed_fixtures(image)
    keys, calls, fixed = audit_reader(independent_reader, image, fixtures)
    print("box 1225; image 291; shells 1 20 30 60 60 120; maximum norm 31")
    print("independent keys %d; wrapped calls %d; fixed fixtures %d; metadata 1" %
          (keys, calls, fixed))
    if args.candidate:
        candidate = load_candidate(args.candidate, args.sha256, args.reader)
        keys, calls, fixed = audit_reader(candidate, image, fixtures)
        print("candidate keys %d; wrapped calls %d; fixed fixtures %d; metadata 1" %
              (keys, calls, fixed))
    print("hook calls 0; PASS")


if __name__ == "__main__":
    main()
