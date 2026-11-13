"""Exact input and linear algebra for the ENC4 certificate."""
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from fractions import Fraction
from itertools import product

# Python's configurable decimal conversion guard is not a mathematical cap.
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def fields(obj, *keys):
    require(type(obj) is dict and obj.keys() == set(keys), "invalid object fields")


def sequence(obj, length=None):
    require(type(obj) is list and (length is None or len(obj) == length), "invalid array")
    return obj


def integer(value, minimum=0, maximum=None):
    require(type(value) is int and value >= minimum and
            (maximum is None or value <= maximum), "integer out of range")
    return value


def rat(value):
    require(type(value) is str and re.fullmatch(r"-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?", value),
            "invalid rational")
    answer = Fraction(value)
    require(str(answer) == value, "noncanonical rational")
    return answer


def strict_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON field")
        result[key] = value
    return result


def read(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=strict_pairs)


def dump(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(obj):
    return hashlib.sha256(dump(obj).encode("ascii")).hexdigest()


@dataclass(frozen=True)
class System:
    q: int
    digits: tuple
    starts: tuple
    weights: tuple
    convention: str

    @property
    def n(self):
        return len(self.weights)

    @property
    def a(self):
        return len(self.digits)

    @property
    def r(self):
        return len(self.weights[0])

    @property
    def msd(self):
        return self.convention.startswith("MSD")


def system(obj):
    fields(obj, "q", "convention", "starts", "digits", "weights")
    q = integer(obj["q"], 2)
    convention = obj["convention"]
    require(convention in ("MSD-E0", "MSD-Z0", "LSD-E0", "LSD-Z0"), "unknown convention")
    weights = sequence(obj["weights"])
    n = len(weights)
    require(n > 0, "empty carrier")
    r = len(sequence(weights[0]))
    require(r > 0, "empty output")
    weights = tuple(tuple(map(rat, sequence(row, r))) for row in weights)
    require(all(x >= 0 for row in weights for x in row), "negative weight")
    starts = tuple(integer(s, 0, n - 1) for s in sequence(obj["starts"]))
    require(starts and len(set(starts)) == len(starts), "starts must be distinct and nonempty")
    digits = tuple(
        tuple(tuple(integer(s, 0, n - 1) for s in sequence(row, n))
              for row in sequence(axis, q))
        for axis in sequence(obj["digits"])
    )
    require(len(digits) >= 2, "rank below two")
    for i, axis in enumerate(digits):
        for earlier in digits[:i]:
            require(all(f[g[s]] == g[f[s]] for f in axis for g in earlier
                        for s in range(n)), "noncommuting coordinates")
    return System(q, digits, starts, weights, convention)


def identity(n):
    return tuple(tuple(Fraction(i == j) for j in range(n)) for i in range(n))


def mul(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in zip(*b))
                 for row in a)


def sub(a, b):
    return tuple(tuple(x - y for x, y in zip(row, other)) for row, other in zip(a, b))


def power(a, exponent):
    result = identity(len(a))
    while exponent:
        if exponent & 1:
            result = mul(result, a)
        exponent >>= 1
        if exponent:
            a = mul(a, a)
    return result


def transition(axis):
    n = len(axis[0])
    return tuple(tuple(Fraction(sum(f[s] == t for f in axis), len(axis))
                       for t in range(n)) for s in range(n))


def pullback(mapping):
    return tuple(tuple(Fraction(t == j) for j in range(len(mapping))) for t in mapping)


def norm(a):
    return max(sum(abs(x) for x in row) for row in a)


def follows(axis, word):
    mapping = tuple(range(len(axis[0])))
    for digit in word:
        mapping = tuple(axis[digit][state] for state in mapping)
    return mapping


def maps(axis, msd):
    """Enumerate canonical positive transformation maps with word witnesses."""
    q = len(axis)
    if msd:
        pending = [(axis[d], (d,)) for d in range(1, q)]
    else:
        pending = [(tuple(range(len(axis[0]))), ())]
    seen = set()
    positive = {}
    cursor = 0
    while cursor < len(pending):
        mapping, word = pending[cursor]
        cursor += 1
        if mapping in seen:
            continue
        seen.add(mapping)
        if msd:
            positive.setdefault(mapping, word)
        for d, letter in enumerate(axis):
            nxt = tuple(letter[s] for s in mapping)
            if not msd and d:
                positive.setdefault(nxt, word + (d,))
            if nxt not in seen:
                pending.append((nxt, word + (d,)))
    return positive


def value(s, words, start):
    for axis, word in zip(s.digits, words):
        start = follows(axis, word)[start]
    return s.weights[start]


def boundary(s):
    return tuple(maps(axis, s.msd) for axis in s.digits)


def nonzero_point(s, positive):
    options = [tuple(words.values()) + (((),) if s.convention.endswith("E0") else ((0,),))
               for words in positive]
    for start in s.starts:
        for words in product(*options):
            if any(value(s, words, start)):
                return {"start": start, "words": [list(w) for w in words]}
    return None


def align_value(s, limit, start, words, residues):
    result = s.weights
    for i in reversed(range(s.a)):
        fixed = pullback(follows(s.digits[i], words[i]))
        block = limit[i][residues[i]]
        result = mul(mul(fixed, block) if s.msd else mul(block, fixed), result)
    return result[start]


def aligned(s, limits, positive):
    """Yield finite limit rows and one legal representative of each entry."""
    for start in s.starts:
        for words in product(*(m.values() for m in positive)):
            for residues in product(*(range(len(axis)) for axis in limits)):
                value_ = align_value(s, limits, start, words, residues)
                yield value_, {"start": start, "words": [list(w) for w in words],
                               "residues": list(residues)}


def limit_tables(transitions, projections, periods):
    tables = []
    for p, e, h in zip(transitions, projections, periods):
        values = [e]
        for _ in range(1, h):
            values.append(mul(p, values[-1]))
        tables.append(values)
    return tables


def direction(row):
    total = sum(row)
    return tuple(x / total for x in row) if total else None


def encoded(row):
    return [str(x) for x in row]


def modulus(s, axes, claim, eps):
    require(eps > 0 and claim["status"] != "REJECT", "modulus requires acceptance and eps > 0")
    if claim["status"] == "ZERO":
        return 1
    eta = eps
    if claim["status"] == "PROB":
        mu = rat(claim["min_mass"])
        eta = min(mu / (2 * s.r), eps * mu / (2 * (s.r + 1)))
    w = max(x for row in s.weights for x in row)
    k = max(axis["K"] for axis in axes)
    while w * sum(rat(axis["theta"]) ** (k // axis["K"]) for axis in axes) > eta / 2:
        k *= 2
    return max(1, math.ceil(2 * w * s.a * (1 + 2 * s.q ** k) / eta))
