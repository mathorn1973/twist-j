#!/usr/bin/env python3
"""Exact, result-exposed neutral-stock and supplied-word audit.

Scientific work starts only under main(). Limits constrain the optional
single-input search; they never establish impossibility. Two arithmetic
representations independently check every audited contact.
"""

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
import sys


CAP = 100000
ZERO4 = (0, 0, 0, 0)
ONE4 = (1, 0, 0, 0)
ZERO5 = (0, 0, 0, 0, 0)
EDGES = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
         (1, 2), (1, 3), (1, 4), (1, 5), (2, 3),
         (2, 4), (2, 5), (3, 4), (3, 5), (4, 5))


def emit(kind, **fields):
    print(json.dumps(dict(kind=kind, **fields), sort_keys=True,
                     separators=(",", ":")), flush=True)


# Primary route: four power-basis coefficients, reduction by Phi_5.
def add4(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub4(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale4(n, x):
    return tuple(n * a for a in x)


def reduce4(coefficients):
    out = list(coefficients) + [0] * max(0, 4 - len(coefficients))
    for degree in range(len(out) - 1, 3, -1):
        value = out[degree]
        for shift in range(1, 5):
            out[degree - shift] -= value
        out[degree] = 0
    return tuple(out[:4])


def mul4(x, y):
    out = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i + j] += a * b
    return reduce4(out)


def rotate4(x):
    a, b, c, d = x
    return (-c + d, -c, a - c, b - c)


@lru_cache(maxsize=100000)
def q4(x):
    numerator = 5 * sum(a * a for a in x) - sum(x) ** 2
    assert numerator % 2 == 0
    return numerator // 2


@lru_cache(maxsize=100000)
def h4(x):
    conjugate = reduce4((x[0], 0, x[3], x[2], x[1]))
    return mul4(x, conjugate)


@lru_cache(maxsize=100000)
def contact4(x, y):
    difference = sub4(x, y)
    if any(a % 2 for a in difference):
        return x, y
    center_twice = add4(x, y)
    rotated = rotate4(difference)
    left_twice = add4(center_twice, rotated)
    right_twice = sub4(center_twice, rotated)
    assert all(a % 2 == 0 for a in left_twice + right_twice)
    return (tuple(a // 2 for a in left_twice),
            tuple(a // 2 for a in right_twice))


# Secondary route: Z^5 / Z(1,1,1,1,1), with minimum coefficient zero.
# It uses cyclic rotation and difference updates, not the primary matrix.
def canon5(x):
    floor = min(x)
    return tuple(a - floor for a in x)


def add5(x, y):
    return canon5(tuple(a + b for a, b in zip(x, y)))


def sub5(x, y):
    return canon5(tuple(a - b for a, b in zip(x, y)))


def scale5(n, x):
    return canon5(tuple(n * a for a in x))


def rotate5(x):
    return x[-2:] + x[:-2]


def mul5(x, y):
    out = [0] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[(i + j) % 5] += a * b
    return canon5(out)


@lru_cache(maxsize=100000)
def q5(x):
    numerator = sum((x[i] - x[j]) ** 2
                    for i in range(5) for j in range(i + 1, 5))
    assert numerator % 2 == 0
    return numerator // 2


@lru_cache(maxsize=100000)
def h5(x):
    return mul5(x, tuple(x[(-i) % 5] for i in range(5)))


@lru_cache(maxsize=100000)
def contact5(x, y):
    difference = tuple(a - b for a, b in zip(x, y))
    parity = difference[0] % 2
    if any(a % 2 != parity for a in difference):
        return x, y
    half = canon5(tuple((a - parity) // 2 for a in difference))
    delta = sub5(rotate5(half), half)
    return add5(x, delta), sub5(y, delta)


def to4(x):
    return tuple(x[i] - x[4] for i in range(4))


def to5(x):
    return canon5(x + (0,))


def replace_pair(state, edge, pair):
    i, j = edge
    return tuple(pair[0] if k == i else pair[1] if k == j else value
                 for k, value in enumerate(state))


def step4(state, edge):
    return replace_pair(state, edge, contact4(state[edge[0]], state[edge[1]]))


def step5(state, edge):
    return replace_pair(state, edge, contact5(state[edge[0]], state[edge[1]]))


@lru_cache(maxsize=100000)
def audit_pair(x, y):
    """Independent arithmetic, invariants and inverse for the entire C-cycle."""
    original = (x, y)
    current = original
    secondary = (to5(x), to5(y))
    expected_sum = add4(x, y)
    expected_h = add4(h4(x), h4(y))
    expected_q = q4(x) + q4(y)
    expected_residues = tuple(sum(a) % 5 for a in original)
    for _ in range(5):
        admitted = all(a % 2 == 0 for a in sub4(*current))
        differences = tuple(a - b for a, b in zip(*secondary))
        assert admitted == (len({a % 2 for a in differences}) == 1)
        current = contact4(*current)
        secondary = contact5(*secondary)
        assert current == tuple(to4(a) for a in secondary)
        assert add4(*current) == expected_sum
        assert add4(h4(current[0]), h4(current[1])) == expected_h
        assert sum(q4(a) for a in current) == expected_q
        assert tuple(sum(a) % 5 for a in current) == expected_residues
        assert to4(add5(*secondary)) == expected_sum
        assert to4(add5(h5(secondary[0]), h5(secondary[1]))) == expected_h
        assert sum(q5(a) for a in secondary) == expected_q
        assert tuple(sum(a) % 5 for a in secondary) == expected_residues
    assert current == original
    assert secondary == (to5(x), to5(y))
    return True


def state_totals(state):
    total_sum, total_h = ZERO4, ZERO4
    for value in state:
        total_sum = add4(total_sum, value)
        total_h = add4(total_h, h4(value))
    return total_sum, total_h, sum(q4(a) for a in state), tuple(sum(a) % 5 for a in state)


def parse_word(text):
    return tuple((int(token[0]) - 1, int(token[1]) - 1) for token in text.split())


def replay(start, word):
    """Audit forward and literal four-letter inverse, returning the endpoint."""
    baseline = state_totals(start)
    current = start
    secondary = tuple(to5(a) for a in start)
    branches = []
    changed = 0
    for edge in word:
        i, j = edge
        assert 0 <= i < j < len(start)
        pair = current[i], current[j]
        audit_pair(*pair)
        branches.append(int(all(a % 2 == 0 for a in sub4(*pair))))
        after = step4(current, edge)
        changed += int(after != current)
        current = after
        secondary = step5(secondary, edge)
        assert current == tuple(to4(a) for a in secondary)
        assert state_totals(current) == baseline
    endpoint = current
    for edge in reversed(word):
        for _ in range(4):
            audit_pair(current[edge[0]], current[edge[1]])
            current = step4(current, edge)
            secondary = step5(secondary, edge)
            assert current == tuple(to4(a) for a in secondary)
            assert state_totals(current) == baseline
    assert current == start and secondary == tuple(to5(a) for a in start)
    return endpoint, "".join(map(str, branches)), changed


def initial(t, helpers):
    u = (1, -1, 0, 0)
    data = (t, 0, -t, 0)
    return (data, scale4(-1, data), u, u) + helpers


def target(t, helpers):
    u = (1, -1, 0, 0)
    data = (t, 0, -t, 0)
    return (add4(u, data), sub4(u, data), ZERO4, ZERO4) + helpers


def audit_words():
    helpers = (ZERO4, (2, 0, 0, 0), (-2, 0, 0, 0))
    words = (
        ("W17", parse_word("57 27 27 23 23 23 47 47 47 67 67 67 17 17 37 37 37")),
        ("W20", parse_word("57 57 57 37 37 37 67 67 67 17 17 26 26 26 67 67 46 46 57 57")),
    )
    assert [len(word) for _, word in words] == [17, 20]
    for name, word in words:
        successes = []
        for t in range(-2, 3):
            start = initial(t, helpers)
            endpoint, branches, changed = replay(start, word)
            first_four = endpoint[:4] == target(t, helpers)[:4]
            returned = endpoint[4:] == helpers
            successes.append(first_four and returned)
            emit("SUPPLIED_WORD", name=name, t=t, forward_contacts=len(word),
                 inverse_contacts=4 * len(word), total_Q=sum(q4(a) for a in start),
                 target_first_four=first_four, helpers_returned=returned,
                 final_state=endpoint, admission_bits=branches, changed_steps=changed,
                 inverse_recovery=True)
            if t == 1:
                assert first_four
                if name == "W17":
                    assert endpoint[4:] == ((-1, 0, 1, 0), (1, 0, 1, 0), (0, 0, -2, 0))
                else:
                    assert returned
        emit("WORD_SCOPE", name=name, catalytic_all_five=all(successes))


def alphabet_and_stock_audit():
    roots = tuple(tuple(int(i == k) for i in range(4)) for k in range(4))
    roots += ((-1, -1, -1, -1),)
    roots5 = tuple(tuple(int(i == k) for i in range(5)) for k in range(5))
    assert tuple(to4(a) for a in roots5) == roots
    assert all(mul4(a, b) == roots[(i + j) % 5]
               for i, a in enumerate(roots) for j, b in enumerate(roots))
    neutral = {sub4(a, b) for a in roots for b in roots}
    charged = {add4(a, b) for a in roots for b in roots}
    assert neutral == {to4(sub5(a, b)) for a in roots5 for b in roots5}
    assert charged == {to4(add5(a, b)) for a in roots5 for b in roots5}
    assert (len(neutral), len(charged)) == (21, 15)
    u = (1, -1, 0, 0)
    for translation in (ZERO4, u):
        left_n = {add4(translation, a) for a in neutral}
        left_r = {add4(translation, a) for a in charged}
        counts = []
        for left, right in ((left_n, left_n), (left_n, left_r), (left_r, left_n)):
            count = 0
            for x, y in product(sorted(left), sorted(right)):
                audit_pair(x, y)
                current = (x, y)
                unshifted = tuple(sub4(a, translation) for a in current)
                for _ in range(5):
                    current = contact4(*current)
                    unshifted = contact4(*unshifted)
                    assert current == tuple(add4(a, translation) for a in unshifted)
                    assert current[0] in left and current[1] in right
                assert current == (x, y)
                count += 1
            counts.append(count)
        assert counts == [441, 315, 315]
        emit("ALPHABET", translation=translation, ordered_pairs=counts,
             powers_per_pair=5, closure="PASS")

    union = neutral | charged
    escapes = []
    for x, y in product(sorted(charged), repeat=2):
        audit_pair(x, y)
        after = contact4(x, y)
        if any(a not in union for a in after):
            escapes.append(((x, y), after))
    emit("R_R_ESCAPE", ordered_pairs=225, escapes=len(escapes),
         first_example=escapes[0] if escapes else None,
         exposed_escape_count=20, exposed_review_match=len(escapes) == 20)

    stocks = {add4(u, a) for a in neutral}
    stock_counts = Counter(q4(a) for a in stocks)
    assert dict(stock_counts) == {0: 1, 5: 7, 10: 6, 15: 6, 20: 1}
    for stock in stocks:
        for t in (-1, 1):
            preparation = initial(t, (stock, (2, 0, 0, 0)))
            endpoint = target(t, (stock, (2, 0, 0, 0)))
            shifted_in = tuple(sub4(a, u) for a in preparation)
            shifted_out = tuple(sub4(a, u) for a in endpoint)
            assert all(a in neutral for a in shifted_out[:5]) and shifted_out[5] in charged
            assert any(a not in neutral for a in shifted_in[:5])
            assert 15 in [q4(a) for a in shifted_in[:2]]
    emit("CATALYTIC_TRAP", translated_stocks=len(stocks),
         stock_Q_counts=sorted(stock_counts.items()), odd_inputs=2, endpoint_tests=42)

    # A neutral element has a unique integral five-coefficient lift with sum0.
    # Q<=20 then implies sum squares<=8, hence every coordinate lies in[-2,2].
    ball = set()
    candidates = 0
    for coordinates in product(range(-2, 3), repeat=5):
        candidates += 1
        if sum(coordinates) == 0 and sum(a * a for a in coordinates) <= 8:
            value = to4(coordinates)
            assert q4(value) == 5 * sum(a * a for a in coordinates) // 2
            assert sum(value) % 5 == 0 and q4(value) <= 20
            assert value not in ball
            ball.add(value)
    assert candidates == 3125 and len(ball) == 171 and stocks <= ball
    ball_counts = Counter(q4(a) for a in ball)
    assert dict(ball_counts) == {0: 1, 5: 20, 10: 30, 15: 60, 20: 60}
    assert {a for a in ball if q4(a) <= 5} == neutral
    emit("NEUTRAL_BALL", Q_max=20, coordinate_candidates=candidates,
         elements=len(ball), Q_counts=sorted(ball_counts.items()),
         translated_trap_elements=len(stocks))

    norm_two = {value for value in product(range(-2, 3), repeat=4) if q4(value) == 2}
    assert norm_two == set(roots) | {scale4(-1, a) for a in roots}
    assert all(h4(a) == ONE4 for a in norm_two)
    two_u = scale4(2, u)
    endpoints = []
    center = add4(ONE4, u)
    for k in range(5):
        phase = roots[2 * k % 5]
        helpers = sub4(center, phase), add4(center, phase)
        for t in (-1, 1):
            baseline = state_totals(initial(t, (two_u, (2, 0, 0, 0))))
            endpoint = target(t, helpers)
            assert state_totals(endpoint) == baseline
            shifted = tuple(sub4(a, u) for a in endpoint)
            assert all(a in neutral for a in shifted[:5]) and shifted[5] in charged
        endpoints.append(helpers)
    emit("TWO_U_ENDPOINTS", Q2_box_candidates=625, Q2_elements=len(norm_two),
         helper_phases=endpoints, odd_inputs=2, endpoint_tests=10,
         shifted_alphabet=True)
    return roots


def orientation_audit():
    u = (1, -1, 0, 0)
    B = (1, 0, -1, 0)
    A = (0, 1, 0, -1)
    J = (1, 0, 1, 0)
    X = (1, 1, 0, -2)
    D = (1, 0, 0, -1)
    assert mul4(J, A) == scale4(-1, u)
    assert X == add4(u, scale4(2, A)) and q4(X) == 15
    assert q4(sub4(X, u)) == 20
    audit_pair(u, X)
    assert contact4(u, X) == (scale4(2, D), ZERO4)
    assert contact5(to5(u), to5(X)) == (to5(scale4(2, D)), ZERO5)
    pair = (scale4(2, u), (2, 0, 0, 0))
    for _ in range(3):
        audit_pair(*pair)
        pair = contact4(*pair)
    assert pair == (add4(u, B), (2, -1, 1, 0))
    assert tuple(q4(a) for a in pair) == (15, 13)
    emit("ORIENTATION", X=X, X_Q=q4(X), X_minus_u_Q=q4(sub4(X, u)),
         contact_u_X=(scale4(2, D), ZERO4), contact3_two_u_two=pair,
         contact3_Q=[q4(a) for a in pair], status="PASS")
    return X


def search_step(state, edge, backward):
    pair = state[edge[0]], state[edge[1]]
    audit_pair(*pair)
    for _ in range(4 if backward else 1):
        pair = contact4(*pair)
    return replace_pair(state, edge, pair)


def state_key(state):
    # Search total Q=43; sum of all squared power coefficients is <=86.
    # Hence each integer coefficient has absolute value <=9.
    flat = tuple(a for value in state for a in value)
    assert len(flat) == 24 and all(-9 <= a <= 9 for a in flat)
    return bytes(a + 16 for a in flat)


def search_digest(distance):
    digest = sha256(b"P-POLE-HEIGHT-NEUTRAL-STOCK-1/power4-bias16-v1\n")
    digest.update(len(distance).to_bytes(8, "big"))
    for key in sorted(state_key(state) for state in distance):
        digest.update(key)
    return digest.hexdigest()


def recover_word(start, goal, meeting, predecessors):
    front, back = predecessors
    word = []
    current = meeting
    while current != start:
        before, edge = front[current]
        word.append(edge)
        current = before
    word.reverse()
    current = meeting
    while current != goal:
        after, edge = back[current]
        word.append(edge)
        current = after
    return tuple(word)


def bounded_search(X):
    """Directed BFS; reverse edges are C^4, each reversing ONE forward C."""
    helpers = (X, (2, 0, 0, 0))
    start, goal = initial(1, helpers), target(1, helpers)
    assert state_totals(start) == state_totals(goal)
    assert sum(q4(a) for a in start) == 43 and start != goal
    distances = [{start: 0}, {goal: 0}]
    predecessors = [{}, {}]
    frontiers = [[start], [goal]]
    radii = [0, 0]
    transitions = [0, 0]

    def finish(status, meeting=None, shortest=False, partial=False):
        word = None if meeting is None else recover_word(start, goal, meeting, predecessors)
        if word is not None:
            assert len(word) == distances[0][meeting] + distances[1][meeting]
        emit("X_SEARCH", status=status, source=start, target=goal, stored_states=[len(d) for d in distances],
             completed_radii=radii, attempted_edges=transitions,
             visited_sha256=[search_digest(d) for d in distances],
             partial_layer=partial, witness_found=word is not None,
             shortest_certified=shortest, word_length=None if word is None else len(word),
             exposed_27_match=None if word is None else len(word) == 27,
             state_cap_per_side=CAP, layers_per_side=20)
        return status, word, shortest

    for _ in range(20):
        for side in (0, 1):
            other = 1 - side
            assert frontiers[side]
            next_frontier = []
            best = None
            best_meeting = None
            for current in frontiers[side]:
                assert distances[side][current] == radii[side]
                for edge in EDGES:
                    after = search_step(current, edge, backward=bool(side))
                    transitions[side] += 1
                    if after not in distances[side]:
                        if len(distances[side]) >= CAP:
                            # A candidate already retained earlier in this partial
                            # layer remains a witness, but not a shortest certificate.
                            return finish("LIMIT_STATES", best_meeting, partial=True)
                        state_key(after)
                        distances[side][after] = radii[side] + 1
                        predecessors[side][after] = (current, edge)
                        next_frontier.append(after)
                    if after in distances[other]:
                        rank = (distances[side][after] + distances[other][after], state_key(after))
                        if best is None or rank < best:
                            best, best_meeting = rank, after
            frontiers[side] = next_frontier
            radii[side] += 1
            if best_meeting is not None:
                # Both discovered balls are complete through these radii.
                # Any shorter directed path would also intersect the two balls.
                return finish("FOUND", best_meeting, shortest=True)
            if not next_frontier:
                return finish("EXHAUSTED_NO_FIXED_ENDPOINT")
    return finish("LIMIT_DEPTH")


def audit_found_word(X, word, shortest):
    helpers = (X, (2, 0, 0, 0))
    emit("X_WORD", word=" ".join(f"{i + 1}{j + 1}" for i, j in word),
         forward_contacts=len(word), inverse_contacts=4 * len(word),
         shortest_for_t1_fixed_endpoint=shortest)
    successes = []
    for t in range(-2, 3):
        endpoint, branches, changed = replay(initial(t, helpers), word)
        first_four = endpoint[:4] == target(t, helpers)[:4]
        returned = endpoint[4:] == helpers
        successes.append(first_four and returned)
        emit("X_WORD_INPUT", t=t, target_first_four=first_four,
             helpers_returned=returned, final_state=endpoint,
             admission_bits=branches, changed_steps=changed, inverse_recovery=True)
        if t == 1:
            assert endpoint == target(t, helpers)
    emit("X_WORD_SCOPE", catalytic_all_five=all(successes))


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    emit("PROBE", name="P-POLE-HEIGHT-NEUTRAL-STOCK-1",
         arithmetic="EXACT_INTEGER", observation="RESULT_EXPOSED")
    audit_words()
    alphabet_and_stock_audit()
    X = orientation_audit()
    status, word, shortest = bounded_search(X)
    if word is not None:
        audit_found_word(X, word, shortest)
    emit("RESULT", fixed_audits="PASS", X_search=status,
         X_witness_verified=word is not None, canon_promotion=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
