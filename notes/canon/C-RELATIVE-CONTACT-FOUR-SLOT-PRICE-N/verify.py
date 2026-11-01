#!/usr/bin/env python3
"""One-architecture, notes-only exact replay of two supplied contact words.

NOT a public probe gate. Source: 2026-11-01 author note, pinned in PREREG.md.
Only the words transcribed below are reproduced. No lower-bound census is run.
"""
from collections import Counter
import re

Z = (0, 0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def jp(k):
    k %= 5
    return (-1, -1, -1, -1) if k == 4 else tuple(int(i == k) for i in range(4))


def mul(a, b):
    c = [0] * 4
    for i, ai in enumerate(a):
        for m, bm in enumerate(b):
            k = (i + m) % 5
            if k == 4:
                for u in range(4):
                    c[u] -= ai * bm
            else:
                c[k] += ai * bm
    return tuple(c)


def parse(s):
    s = s.replace(" ", "").replace("-", "+-")
    out = Z
    for item in s.split("+"):
        if not item:
            continue
        match = re.fullmatch(r"(-?\d*)(j(?:\^([0-4]))?)?", item)
        assert match is not None, (s, item)
        raw = match.group(1)
        coeff = int(raw) if raw not in ("", "-") else (-1 if raw == "-" else 1)
        power = int(match.group(3) or 1) if match.group(2) else 0
        out = add(out, tuple(coeff * n for n in jp(power)))
    return out


def parse_list(s):
    return [parse(x.strip()) for x in s.split("|")]


def halve(a):
    assert all(n % 2 == 0 for n in a), ("contact not admitted", a)
    return tuple(n // 2 for n in a)


def contact(k, a, b):
    half_sum = halve(add(a, b))
    half_diff = halve(sub(a, b))
    phase_diff = mul(jp(2 * k), half_diff)
    return add(half_sum, phase_diff), sub(half_sum, phase_diff)


def bar(a):
    value = Z
    for i, coeff in enumerate(a):
        value = add(value, tuple(coeff * n for n in jp(-i)))
    return value


def energy(a):
    return (5 * sum(t * t for t in a) - sum(a) ** 2) // 2


def residue(a):
    return sum(a) % 5


def total(state):
    out = Z
    for z, count in state.items():
        out = add(out, tuple(n * count for n in z))
    return out


def gram_sum(state):
    out = Z
    for z, count in state.items():
        n = mul(z, bar(z))
        out = add(out, tuple(v * count for v in n))
    return out


def account(state):
    return sum(energy(z) * count for z, count in state.items())


def histogram(state):
    out = [0] * 5
    for z, count in state.items():
        out[residue(z)] += count
    return tuple(out)


SIGNED = """
2|0|6
4|-3j-3j^2-3j^3|j+j^2+j^3
2|-j-3j^2-3j^3|-j-j^2-j^3
3|-j+j^2+j^3|6+3j+3j^2+3j^3
2|-j-j^2|2+3j+3j^2+2j^3
1|-2j-3j^2-2j^3|j^2+2j^3
1|-j-j^2|4-j+j^2+2j^3
2|2-2j+j^2|2+2j+j^2
4|j^2|4+j^2
4|-3j-3j^2-j^3|j+j^2+j^3
1|j^2+2j^3|2+j^2-2j^3
1|-j^2-2j^3|2-j^2+2j^3
3|-2j-3j^2-2j^3|2+j^2+2j^3
4|-1-2j^2|-1+2j^2
2|-1-2j-2j^2|1
"""

POSITIVE = """
3|0|6
2|-1-j|3-3j
3|-2-4j-2j^2-2j^3|0
4|-2j-2j^2-j^3|2+j^3
3|1-j|3+3j
1|0|2+2j+2j^2
3|2-2j^2|4+2j^2+2j^3
4|2+2j+j^2|4+j^2
1|j^2|2-j^2+2j^3
3|1-j-2j^2|3+j+2j^2+2j^3
3|1+2j^3|1+2j
1|2-2j^3|2+2j+2j^2+2j^3
3|-2j^2|4+2j+2j^2+2j^3
1|1+2j+2j^3|1+2j+2j^2
3|-1-j-2j^2|3+3j+2j^2+2j^3
4|2-j^2|2+j^2
"""

CASES = (
    ("signed", SIGNED,
     "-j-j^2-j^3|-j-j^2|-j-j^2|j+j^2+j^3",
     "3|3|3|-3",
     "-j-2j^2-j^3|-j+j^3", 12),
    ("positive", POSITIVE,
     "-1-j|1+2j|2+j^3|2+j^2",
     "3|3|3|3",
     "1|-1+j|-2-2j-j^3|2j+j^2+2j^3", 27),
)


def verify_case(name, word, source, target, sink, funded_energy):
    source, target, sink = parse_list(source), parse_list(target), parse_list(sink)
    initial = Counter([parse("6")] + [Z] * 21 + source)
    current = initial.copy()
    initial_sum = total(initial)
    initial_norm = gram_sum(initial)
    initial_account = account(initial)
    initial_hist = histogram(initial)
    assert sum(initial.values()) == 26
    assert sum(energy(x) for x in source) == funded_energy
    n = 0
    for line in word.strip().splitlines():
        k, x, y = line.split("|")
        k = int(k)
        x, y = parse(x), parse(y)
        assert 1 <= k <= 4
        assert current[x] > 0 and current[y] > (1 if x == y else 0), (
            name, n + 1, "absent input pair"
        )
        current.subtract((x, y))
        current += Counter()
        u, v = contact(k, x, y)
        current.update((u, v))
        n += 1
        assert sum(current.values()) == 26
        assert total(current) == initial_sum
        assert gram_sum(current) == initial_norm
        assert account(current) == initial_account
        assert histogram(current) == initial_hist
    expected = Counter(target + sink + [Z] * (26 - len(target) - len(sink)))
    assert current == expected, (name, "wrong final full multiset")
    assert histogram(Counter(source)) != histogram(Counter(sink + [Z] * (4 - len(sink))))
    print(f"PASS {name}: {n} power contacts, auxiliary account {funded_energy}")
    return n


def main():
    assert verify_case(*CASES[0]) == 15
    assert verify_case(*CASES[1]) == 16
    print("PASS auxiliary histogram changes: retained-output clean reset forbidden")


if __name__ == "__main__":
    main()
