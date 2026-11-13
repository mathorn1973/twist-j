"""NON-CANONICAL seven-stock finite certificate auditor; no import-time run.

run() prints deterministic JSON certificates and returns a small summary.
Power-basis and normalized five-coefficient arithmetic are independently
implemented here. No earlier verifier or supplied review script is imported.
"""
from collections import deque
from itertools import combinations
import json

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
EDGES = tuple(combinations(range(6), 2))
ORBIT_CAP = 256
VALUE_CAP = 64
STOCK_FIVE = (
    (-2, 1, 0, 1, 0), (0, 1, 0, -2, 1), (-1, 0, -1, 2, 0),
    (-1, 2, 0, -1, 0), (1, 0, 1, -2, 0), (0, -1, 0, 2, -1),
)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(n, x):
    return tuple(n * a for a in x)


def times_j(x):
    a, b, c, d = x
    return (-d, a - d, b - d, c - d)


def root(k):
    x = ONE
    for _ in range(k % 5):
        x = times_j(x)
    return x


def q4(x):
    n = 5 * sum(a * a for a in x) - sum(x) ** 2
    assert n % 2 == 0
    return n // 2


def residue(x):
    return sum(x) % 5


def c4(x, y):
    delta = sub(x, y)
    if any(a % 2 for a in delta):
        return x, y
    center = tuple((a + b) // 2 for a, b in zip(x, y))
    half = tuple(a // 2 for a in delta)
    turn = times_j(times_j(half))
    return add(center, turn), sub(center, turn)


def norm5(x):
    return tuple(a - x[4] for a in x)


def q5(x):
    n = sum((x[i] - x[j]) ** 2 for i in range(5) for j in range(i + 1, 5))
    assert n % 2 == 0
    return n // 2


def c5(x, y):
    # This path works in Z[C5]/(1+j+...+j^4), not the power recurrence.
    x, y = norm5(x), norm5(y)
    delta = tuple(x[i] - y[i] for i in range(5))
    if any(a % 2 for a in delta):
        return x, y
    center = tuple((x[i] + y[i]) // 2 for i in range(5))
    half = tuple(a // 2 for a in delta)
    turn = tuple(half[(i - 2) % 5] for i in range(5))
    return (norm5(tuple(center[i] + turn[i] for i in range(5))),
            norm5(tuple(center[i] - turn[i] for i in range(5))))


def audit_pair(x, y):
    """Check both exact paths, accounts, labelled residues, and the full C^5 cycle."""
    first = c4(x, y)
    a, b = x, y
    aa, bb = x + (0,), y + (0,)
    for _ in range(5):
        a, b = c4(a, b)
        aa, bb = c5(aa, bb)
        assert aa == a + (0,) and bb == b + (0,), "dual contact"
        assert add(a, b) == add(x, y), "pair sum"
        assert q4(a) + q4(b) == q4(x) + q4(y), "pair Q"
        assert q4(a) == q5(aa) and q4(b) == q5(bb), "dual Q"
        assert (residue(a), residue(b)) == (residue(x), residue(y)), "slot residue"
    assert (a, b) == (x, y), "C fifth power"
    return first


def step(state, edge, checked=False):
    i, j = edge
    pair = audit_pair(state[i], state[j]) if checked else c4(state[i], state[j])
    out = list(state)
    out[i], out[j] = pair
    return tuple(out)


def swapped(state):
    return (state[1], state[0]) + state[2:]


def emit(kind, **fields):
    print(json.dumps(dict(kind=kind, **fields), sort_keys=True, separators=(",", ":")))


def orbit_certificate(stock, u, b, two):
    start = (b, scale(-1, b), u, u, stock, two)
    seen = {start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for edge in EDGES:
            out = step(state, edge)
            if out not in seen:
                seen.add(out)
                assert len(seen) <= ORBIT_CAP, "small-stock orbit resource cap"
                queue.append(out)
    assert len(seen) == 13, "exposed 13-state forecast"
    active = set()
    account = 28 + q4(stock)
    for sign, states in ((1, seen), (-1, {swapped(s) for s in seen})):
        assert len(states) == 13
        expected_start = start if sign == 1 else swapped(start)
        assert expected_start in states
        for state in sorted(states):
            assert state[2:4] == (u, u) and state[5] == two, "references and charge fixed"
            assert sum(q4(x) for x in state) == account
            assert tuple(residue(x) for x in state) == (0, 0, 0, 0, 0, 2)
            for edge in EDGES:
                out = step(state, edge, checked=True)
                assert out in states, "complete signed orbit edge closure"
                if out != state:
                    active.add(edge)
    assert active == {(0, 1), (0, 4), (1, 4)}, "three active data-stock edges"
    emit("SMALL_STOCK_ORBIT_CERTIFICATE", stock=stock, Q=q4(stock),
         states_plus=sorted(seen), states_minus="swap slots 1 and 2 in states_plus",
         complete=True, signed_edge_checks=2 * 13 * 15,
         active_edges=["%d%d" % (i + 1, j + 1) for i, j in sorted(active)],
         references_fixed=True, unrestricted_helper_target_absent=True)
    return 2 * 13 * 15


def value_certificate(stock, u, b, two):
    budget = 28 + q4(stock)
    assert budget == 48
    neutral = {b, scale(-1, b), u, stock}
    charged = {two}
    rounds = 0
    while True:
        new_n, new_r = set(neutral), set(charged)
        for x in sorted(neutral):
            for y in sorted(neutral):
                if q4(x) + q4(y) <= budget - 3:
                    new_n.update(c4(x, y))
            for r in sorted(charged):
                if q4(x) + q4(r) <= budget:
                    a, d = c4(x, r)
                    new_n.add(a)
                    new_r.add(d)
        assert len(new_n) <= VALUE_CAP and len(new_r) <= VALUE_CAP, "value closure resource cap"
        rounds += 1
        if new_n == neutral and new_r == charged:
            break
        neutral, charged = new_n, new_r
    assert (len(neutral), len(charged)) == (15, 5), "exposed 15/5 alphabet forecast"
    assert all(residue(x) == 0 for x in neutral)
    assert all(residue(r) == 2 and q4(r) >= 3 for r in charged)
    assert add(u, b) not in neutral, "required odd output excluded"
    eligible = ignored = checks = 0
    for x in sorted(neutral):
        for y in sorted(neutral):
            a, d = audit_pair(x, y)
            checks += 1
            if q4(x) + q4(y) <= budget - 3:
                eligible += 1
                assert a in neutral and d in neutral, "NN budget closure"
            else:
                ignored += 1
        for r in sorted(charged):
            for reverse in (False, True):
                pair = (r, x) if reverse else (x, r)
                a, d = audit_pair(*pair)
                checks += 1
                if q4(x) + q4(r) <= budget:
                    eligible += 1
                    assert ((a in charged and d in neutral) if reverse else
                            (a in neutral and d in charged)), "NR/RN budget closure"
                else:
                    ignored += 1
    assert checks == 375 and eligible + ignored == checks
    emit("SMALL_STOCK_VALUE_CERTIFICATE", stock=stock, Q=q4(stock), budget=budget,
         neutral=sorted(neutral), charged=sorted(charged), closure_rounds=rounds,
         ordered_pair_checks=checks, eligible_pairs=eligible, ignored_over_budget=ignored,
         required_value=add(u, b), required_value_absent=True,
         both_odd_signs=True, unrestricted_helper_target_absent=True)
    return checks


def prior_classes_exclude(stock, u, b):
    roots = [root(k) for k in range(5)]
    nset = {ZERO} | {sub(a, c) for a in roots for c in roots if a != c}
    un = {add(u, n) for n in nset}
    exception = sub(roots[2], roots[4])
    traps = (nset | un) - {add(u, exception), sub(u, exception)}
    parity = lambda x: tuple(a % 2 for a in x)
    allowed = {parity(ZERO), parity(u)}
    rotated = b
    for _ in range(5):
        allowed.add(parity(rotated))
        rotated = times_j(times_j(rotated))
    product_stocks = {scale(sg * 2, sub(roots[a], roots[3]))
                      for sg in (-1, 1) for a in (1, 2)}
    return stock in traps or parity(stock) not in allowed or stock in product_stocks


def run():
    """Execute only after the prospective source pin; return audited summary."""
    u, b, two = sub(ONE, root(1)), sub(ONE, root(2)), scale(2, ONE)
    stocks = tuple(norm5(s)[:4] for s in STOCK_FIVE)
    seventh = scale(2, sub(root(2), root(4)))
    assert len(set(stocks + (seventh,))) == 7
    assert all(q4(s) == 15 for s in stocks) and q4(seventh) == 20
    assert all(residue(s) == 0 for s in stocks + (seventh,))
    assert all(not prior_classes_exclude(s, u, b) for s in stocks + (seventh,)), "seven disjoint from prior 124"
    edge_checks = sum(orbit_certificate(s, u, b, two) for s in stocks)
    pair_checks = value_certificate(seventh, u, b, two)
    summary = dict(stocks=7, signed_orbit_edge_checks=edge_checks,
                   value_pair_checks=pair_checks, disjoint_from_prior_124=True,
                   total_exclusions_with_prior=131, independent_arithmetic_paths=2)
    emit("SMALL_STOCK_SUMMARY", **summary)
    return summary


if __name__ == "__main__":
    run()
