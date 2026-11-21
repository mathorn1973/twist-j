#!/usr/bin/env python3
"""Exact bounded replay. Execute only after the public source pin."""

from hashlib import sha256
from json import dumps
from math import gcd


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 1, 0, 0)
POWERS = (ONE, RHO, (0, 0, 1, 0), (0, 0, 0, 1), (-1, -1, -1, -1))
CAP = 12
CORE = 16
COUNTS = {"native": 0, "enabled": 0, "refused": 0}
FINGERPRINT = sha256()


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, k):
    return tuple(k * x for x in a)


def mul(a, b):
    """Cyclic length-five convolution followed by Phi_5 reduction."""
    result = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[(i + j) % 5] += x * y
    return tuple(result[i] - result[4] for i in range(4))


def power(a, exponent):
    assert exponent >= 0
    result = ONE
    while exponent:
        if exponent % 2:
            result = mul(result, a)
        a = mul(a, a)
        exponent //= 2
    return result


def sigma(a, d):
    return tuple(sum(a[k] * POWERS[(k * d) % 5][i] for k in range(4))
                 for i in range(4))


def account(a):
    twice = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert twice >= 0 and twice % 2 == 0
    return twice // 2


def total(values):
    return tuple(sum(z[i] for z in values) for i in range(4))


def epsilon(a):
    return sum(a) % 5


def u(d):
    return sub(ONE, POWERS[d % 5])


def jcode(d):
    return add(ONE, POWERS[d % 5])


def depth(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def primitive(state, left, right):
    """Literal native C, with a separate coordinate formula for rho*t."""
    COUNTS["native"] += 1
    a, b = state[left], state[right]
    difference = sub(a, b)
    if any(x % 2 for x in difference):
        COUNTS["refused"] += 1
        return False
    COUNTS["enabled"] += 1
    center = tuple((x + y) // 2 for x, y in zip(a, b))
    t = tuple(x // 2 for x in difference)
    rotated = (-t[3], t[0] - t[3], t[1] - t[3], t[2] - t[3])
    anew, bnew = add(center, rotated), sub(center, rotated)
    assert add(anew, bnew) == add(a, b)
    assert account(anew) + account(bnew) == account(a) + account(b)
    assert epsilon(anew) == epsilon(a) and epsilon(bnew) == epsilon(b)
    state[left], state[right] = anew, bnew
    return True


def macro(state, left, right, exponent):
    assert 1 <= exponent <= 4
    flags = [primitive(state, left, right) for _ in range(exponent)]
    assert all(flag == flags[0] for flag in flags)
    return flags[0]


def word(d):
    return [(0, 1, d), (0, 2, d)] + [
        (0, 2 + s, (pow(2, s, 5) * d) % 5) for s in range(1, CAP + 2)
    ]


def source(q, n, d):
    return [scale(u(d), n), scale(sub(scale(ONE, 4 * q), jcode(d)), n),
            scale(jcode(d), 2)]


def reader(state):
    """Uses only the present active port and the thirteen cascade ports."""
    targets = state[3:CORE]
    v = 0
    while v < len(targets) and targets[v] != ZERO:
        v += 1
    if v == len(targets):
        return None
    assert all(z == ZERO for z in targets[v:])
    m = gcd(*state[0])
    assert m > 0 and m % 2 == 1
    shape = tuple(x // m for x in state[0])
    choices = [d for d in range(1, 5) if shape == u(d)]
    assert len(choices) == 1
    return m, choices[0], v


def fingerprint(tag, q, n, d, state):
    payload = dumps([tag, q, n, d, state], separators=(",", ":"))
    FINGERPRINT.update(payload.encode("ascii") + b"\n")


def run_case(q, n, d, tag, archives=()):
    initial = source(q, n, d) + [ZERO] * (CAP + 1) + list(archives)
    state = initial.copy()
    old_account = sum(account(z) for z in archives)
    ready_account = (32 * q * q - 12 * q + 8) * n * n + 12
    assert sum(account(z) for z in initial) == ready_account + old_account
    assert total(initial[:3]) == add(
        scale(sub(scale(ONE, 2 * q), POWERS[d]), 2 * n), scale(jcode(d), 2))
    if q == 3:
        assert [epsilon(z) for z in initial[:3]] == [0, 0, 4]
    schedule = word(d)
    assert len(schedule) == 15
    before = COUNTS["native"]
    flags, boundaries = [], []
    for left, right, exponent in schedule:
        flags.append(macro(state, left, right, exponent))
        boundaries.append(tuple(state))
    assert COUNTS["native"] - before == (34, 38, 37, 41)[d - 1]
    assert flags[:2] == [True, True]

    x = q * n + 1
    v = depth(x)
    assert (v > CAP) == (tag == "depth-limit")
    accepted = min(v, CAP + 1)
    expected_b = scale(sub(scale(jcode(d), q), POWERS[d]), 2 * n)
    expected_c = add(scale(mul(u(d), u(d)), q * n),
                     mul(jcode(d), jcode(d)))
    assert boundaries[0][0] == scale(u(d), 2 * q * n)
    assert boundaries[0][1] == expected_b
    assert boundaries[1][:3] == (scale(u((2 * d) % 5), x),
                                 expected_b, expected_c)
    assert flags[2:] == [True] * accepted + [False] * (CAP + 1 - accepted)
    partial_m = x >> accepted
    actual_chart = (pow(2, accepted + 1, 5) * d) % 5
    expected = [scale(u(actual_chart), partial_m), expected_b, expected_c]
    for s in range(1, CAP + 2):
        e = (pow(2, s, 5) * d) % 5
        expected.append(scale(mul(u(e), u(e)), x >> s) if s <= accepted else ZERO)
    expected.extend(archives)
    assert state == expected
    assert state[CORE:] == list(archives)
    assert total(state) == total(initial)
    assert sum(account(z) for z in state) == ready_account + old_account
    assert [epsilon(z) for z in state] == [epsilon(z) for z in initial]
    read = reader(state)
    if v <= CAP:
        m = x >> v
        dp = (pow(2, v + 1, 5) * d) % 5
        assert read == (m, dp, v)
        assert ((m << v) - 1) // q == n and ((m << v) - 1) % q == 0
        assert (pow(pow(2, v + 1, 5), -1, 5) * dp) % 5 == d
        assert account(state[0]) == 5 * m * m
        records = state[3:CORE]
        record_account = sum(account(z) for z in records)
        assert record_account == 5 * (x * x - m * m)
        assert total(records) == sub(scale(u((2 * d) % 5), x),
                                    scale(u(dp), m))
        if q == 3 and n % 2 == 1:
            assert record_account >= 75
            assert (record_account == 75) == (n == m == 1)
        if q == 3 and n == 3:
            assert m == 5 and record_account == 375
            assert 260 * (m * m - n * n) + record_account == 4535
    else:
        assert read is None
        assert all(z != ZERO for z in state[3:CORE])
    fingerprint(tag, q, n, d, state)
    for left, right, exponent in reversed(schedule):
        macro(state, left, right, 5 - exponent)
    assert state == initial
    assert COUNTS["native"] - before == 75
    return boundaries


def covariance_family(q, n, tag, archives=()):
    base = None
    for d in range(1, 5):
        trace = run_case(q, n, d, tag, archives)
        assert all(boundary[CORE:] == archives for boundary in trace)
        if d == 1:
            base = trace
        else:
            assert base is not None
            assert [boundary[:CORE] for boundary in trace] == [
                tuple(sigma(z, d) for z in boundary[:CORE]) for boundary in base
            ]


def scalar_sequences():
    c = [2, 3]
    for _ in range(63):
        c.append(3 * c[-1] - c[-2])
    for r in range(65):
        assert c[r] == account(power(jcode(1), r))
    return c


def ring_and_resource_identities(c):
    for d in range(1, 5):
        ud, jd = u(d), jcode(d)
        assert account(ud) == 5 and account(jd) == 3
        assert account(mul(ud, ud)) == 15
        assert mul(ud, jd) == u((2 * d) % 5)
        product = ONE
        for r in range(4):
            product = mul(product, jcode((pow(2, r, 5) * d) % 5))
        assert product == ONE
    uu, jj = u(1), jcode(1)
    beta = mul(mul(uu, uu), jj)
    assert mul(beta, sigma(beta, 4)) == scale(ONE, 5)
    for v in range(13):
        for m in range(1, 32, 2):
            records = [scale(mul(mul(uu, uu), power(jj, s)),
                             (1 << (v - s)) * m) for s in range(1, v + 1)]
            assert sum(account(z) for z in records) == (
                5 * 4 ** v - c[v] - c[v + 1]) * m * m
            assert total(records) == scale(
                mul(mul(uu, jj), sub(scale(ONE, 1 << v), power(jj, v))), m)


def original_cases(c):
    uu, jj = u(1), jcode(1)
    schedule = [(0, 1, 1), (0, 2, 1)] + [
        (0, 2 + s, 1) for s in range(1, CAP + 2)
    ]
    for n in range(1, 4096, 2):
        initial = [scale(uu, 4 * n), scale(sub(scale(ONE, 2), RHO), 4 * n),
                   scale(jj, 2)] + [ZERO] * (CAP + 1)
        state = initial.copy()
        before = COUNTS["native"]
        for left, right, exponent in schedule:
            macro(state, left, right, exponent)
        x = 3 * n + 1
        v = depth(x)
        assert 1 <= v <= CAP
        m = x >> v
        assert state[0] == scale(mul(uu, power(jj, v + 1)), m)
        assert state[1] == scale(sub(scale(ONE, 3), RHO), 2 * n)
        assert state[2] == add(scale(mul(uu, uu), 3 * n), mul(jj, jj))
        for s in range(1, CAP + 2):
            want = scale(mul(mul(uu, uu), power(jj, s)), x >> s) if s <= v else ZERO
            assert state[2 + s] == want
        records = state[3:CORE]
        amount = sum(account(z) for z in records)
        assert amount == (5 * 4 ** v - c[v] - c[v + 1]) * m * m
        assert total(records) == sub(scale(mul(uu, jj), x), state[0])
        assert sum(account(z) for z in initial) == 272 * n * n + 12
        assert total(state) == total(initial)
        assert sum(account(z) for z in state) == sum(account(z) for z in initial)
        assert amount >= 55 and (amount == 55) == (n == m == 1)
        if n == 1:
            assert amount == 55 and account(total(records)) == 85
        if n == 3:
            assert m == 5 and amount == 250
            assert 272 * (m * m - n * n) + amount == 4602
        fingerprint("original", 3, n, 1, state)
        for left, right, exponent in reversed(schedule):
            macro(state, left, right, 5 - exponent)
        assert state == initial
        assert COUNTS["native"] - before == 75


def mersenne_prefixes():
    for k in range(2, 65):
        n = (1 << k) - 1
        for i in range(k - 1):
            assert n == 3 ** i * (1 << (k - i)) - 1
            numerator = 3 * n + 1
            divisions = 0
            while numerator % 2 == 0:
                numerator //= 2
                divisions += 1
            assert divisions == 1
            n = numerator
        assert n == 2 * 3 ** (k - 1) - 1


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled.")
    c = scalar_sequences()
    ring_and_resource_identities(c)
    for n in range(1, 4096, 2):
        covariance_family(3, n, "q3")
    for q in range(1, 10):
        for n in range(1, 128, 2):
            covariance_family(q, n, "supplied-gain")
    archives = (RHO, add(ONE, POWERS[3]))
    for n in range(1, 48, 2):
        covariance_family(3, n, "occupied", archives)
    for n, expected_depth in ((5461, 14), (13653, 13)):
        assert depth(3 * n + 1) == expected_depth
        covariance_family(3, n, "depth-limit")
    original_cases(c)
    mersenne_prefixes()
    assert COUNTS["native"] == 75 * (8192 + 2304 + 96 + 8 + 2048)
    assert COUNTS["native"] == COUNTS["enabled"] + COUNTS["refused"]
    print("CONTACT-FOUR-CHART-REPLAY v1")
    print("arithmetic: exact rho-basis integers; literal native C powers")
    print("q=3: 8192 complete four-chart cases; PASS")
    print("supplied gains q=1..9: 2304 complete cases; PASS")
    print("occupied archives: 96 complete cases, two literal old records; PASS")
    print("outside depth: 8 cases, depths 13 and 14; DEPTH_LIMIT as specified")
    print("Galois covariance: every corresponding powered-contact boundary; PASS")
    print("primitive word lengths d=1,2,3,4: 34,38,37,41")
    print("current reader: scalar gcd, four shapes and present depth prefix; PASS")
    print("original interface: 2048 actual complete cases; record accounts and sums; PASS")
    print("full native inverses: 12648; PASS")
    print("primitive calls:", COUNTS["native"], "enabled:", COUNTS["enabled"],
          "refused:", COUNTS["refused"])
    print("complete-output fingerprint SHA-256:", FINGERPRINT.hexdigest())
    print("3->5 necessary funding: original 4602; four-chart 4535")
    print("fixed-point record accounts: original 55; four-chart 75")
    print("unit trace recurrence: r=0..64; resource box: v=0..12,odd m<=31; PASS")
    print("Mersenne prefixes: k=2..64, all initial valuation-one steps; PASS")
    print("scope: no source reload or autonomous chart selector executed")
    print("scope: infinite resource obstructions are proof-only; no Collatz convergence claim")


if __name__ == "__main__":
    main()
