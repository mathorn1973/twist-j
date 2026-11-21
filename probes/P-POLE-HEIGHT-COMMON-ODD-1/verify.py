#!/usr/bin/env python3
"""Exact common-odd witness and bounded stabilizer-loop extension audit.

Scientific work starts only under main(). Limits constrain the optional
common-five search; they never establish impossibility. Two arithmetic
representations independently check every audited contact.
"""

from collections import Counter, OrderedDict, deque
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
import sys


ODD_DEPTH = 4
ODD_CAP = 2000
EXTRA_LOOPS = 20
BEAM_WIDTH = 128
BEAM_ROUNDS = 20
VISITED_CAP = 20000
BEAM_CONTACT_BUDGET = 20000000
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


def roots4():
    return tuple(tuple(int(i == k) for i in range(4)) for k in range(4)) + ((-1, -1, -1, -1),)


def histogram(values):
    return sorted(Counter(q4(a) for a in values).items())


def parity(value):
    return tuple(a % 2 for a in value)


def classifier_audit():
    roots = roots4()
    u = (1, -1, 0, 0)
    B = (1, 0, -1, 0)
    neutral = {sub4(a, b) for a in roots for b in roots}
    translated = {add4(u, a) for a in neutral}
    special = sub4(roots[2], roots[4])
    exceptions = {add4(u, special), sub4(u, special)}
    assert len(neutral) == 21 and {q4(a) for a in exceptions} == {10}
    traps = neutral | (translated - exceptions)
    allowed = {parity(ZERO4), parity(u)}
    allowed.update(parity(mul4(roots[2 * k % 5], B)) for k in range(5))
    assert len(allowed) == 7
    ball = set()
    for coordinates in product(range(-2, 3), repeat=5):
        if sum(coordinates) == 0 and sum(a * a for a in coordinates) <= 8:
            value = to4(coordinates)
            assert q4(value) == q5(canon5(coordinates))
            assert q4(value) == 5 * sum(a * a for a in coordinates) // 2
            assert sum(value) % 5 == 0 and value not in ball
            ball.add(value)
    assert len(ball) == 171
    assert histogram(ball) == [(0, 1), (5, 20), (10, 30), (15, 60), (20, 60)]
    isolated = {a for a in ball if parity(a) not in allowed}
    overlap = traps & isolated
    excluded = traps | isolated
    residual = ball - excluded
    assert traps <= ball
    assert (len(traps), len(isolated), len(overlap), len(excluded), len(residual)) == (32, 102, 14, 120, 51)
    assert histogram(traps) == [(0, 1), (5, 20), (10, 4), (15, 6), (20, 1)]
    assert histogram(isolated) == [(5, 8), (10, 30), (15, 24), (20, 40)]
    assert histogram(overlap) == [(5, 8), (10, 4), (15, 2)]
    assert histogram(excluded) == [(0, 1), (5, 20), (10, 30), (15, 28), (20, 41)]
    assert histogram(residual) == [(15, 32), (20, 19)]
    assert {a for a in residual if q4(a) == 20} == {
        scale4(2, a) for a in neutral if a != ZERO4 and a != u
    }
    closure_edges = 0
    for stock in sorted(isolated):
        for t in (-1, 1):
            start = initial(t, (stock, (2, 0, 0, 0)))
            state = start
            orbit = set()
            for _ in range(5):
                assert state not in orbit
                orbit.add(state)
                state = apply_ids_single(state, (0,))  # EDGES[0] is12.
            assert state == start and len(orbit) == 5
            for state in sorted(orbit):
                assert state[:4] != target(t, (stock, (2, 0, 0, 0)))[:4]
                assert state_totals(state) == state_totals(start)
                for edge_id in range(15):
                    assert apply_ids_single(state, (edge_id,)) in orbit
                    closure_edges += 1
    assert closure_edges == 15300
    emit("STOCK_CLASSIFIER", ball=len(ball), ball_Q=histogram(ball),
         arbitrary_helper_traps=len(traps), trap_Q=histogram(traps),
         parity_isolated=len(isolated), isolated_Q=histogram(isolated),
         overlap=len(overlap), overlap_Q=histogram(overlap),
         union=len(excluded), union_Q=histogram(excluded),
         residual=len(residual), residual_Q=histogram(residual),
         residual_reachability="NOT_CENSUSED", isolated_orbits=204,
         states_per_isolated_orbit=5, isolated_closure_edges=closure_edges)

    # Four further doubled-root stocks have disjoint data/helper five-cycles.
    differences = (sub4(roots[1], roots[3]), sub4(roots[2], roots[3]))
    extra_stocks = {scale4(sign * 2, d) for d in differences for sign in (-1, 1)}
    assert len(extra_stocks) == 4 and extra_stocks <= residual
    assert {q4(a) for a in extra_stocks} == {20}
    extra_edges = 0
    for stock in sorted(extra_stocks):
        for t in (-1, 1):
            start = initial(t, (stock, (2, 0, 0, 0)))
            orbit = {apply_ids_single(start, (0,) * a + (14,) * b)
                     for a in range(5) for b in range(5)}
            assert len(orbit) == 25
            helper_parities = set()
            for state in sorted(orbit):
                assert state[2] == u and state[3] == u
                assert parity(state[4]) == parity(state[5])
                helper_parities.add(parity(state[4]))
                assert state[:4] != target(t, (stock, (2, 0, 0, 0)))[:4]
                assert state_totals(state) == state_totals(start)
                for edge_id in range(15):
                    assert apply_ids_single(state, (edge_id,)) in orbit
                    extra_edges += 1
            assert len(helper_parities) == 5
            assert not (helper_parities & (allowed - {parity(ZERO4)}))
    assert extra_edges == 3000
    enlarged = excluded | extra_stocks
    remaining = ball - enlarged
    assert len(enlarged) == 124 and len(remaining) == 47
    assert histogram(remaining) == [(15, 32), (20, 15)]
    emit("HELPER_ISOLATION", stocks=sorted(extra_stocks), odd_inputs=2,
         orbits=8, states_per_orbit=25, closure_edges=extra_edges,
         excluded_union=len(enlarged), residual=len(remaining),
         residual_Q=histogram(remaining), residual_reachability="NOT_CENSUSED")


def format_ids(word):
    return " ".join(f"{EDGES[e][0] + 1}{EDGES[e][1] + 1}" for e in word)


def normalize_ids(word):
    """Free-product normal form using only the proved relation C_e^5=I."""
    blocks = []
    for edge in word:
        if blocks and blocks[-1][0] == edge:
            power = (blocks[-1][1] + 1) % 5
            blocks.pop()
            if power:
                blocks.append((edge, power))
        else:
            blocks.append((edge, 1))
    return tuple(edge for edge, power in blocks for _ in range(power))


def inverse_ids(word):
    return normalize_ids(edge for edge in reversed(word) for _ in range(4))


@lru_cache(maxsize=50000)
def apply_ids_single(state, word):
    for edge_id in word:
        edge = EDGES[edge_id]
        audit_pair(state[edge[0]], state[edge[1]])
        state = step4(state, edge)
    return state


def apply_joint(joint, word):
    return tuple(apply_ids_single(state, word) for state in joint)


def joint_error(joint, goal):
    return sum(q4(sub4(a, b)) for state, target_state in zip(joint, goal)
               for a, b in zip(state, target_state))


def joint_key(joint):
    # All inputs have total Q<=78, so each power coefficient has abs<=12.
    flat = tuple(a for state in joint for value in state for a in value)
    assert len(flat) in (48, 72) and all(-12 <= a <= 12 for a in flat)
    return bytes(a + 16 for a in flat)


def state_set_digest(states):
    keys = sorted(joint_key(state) for state in states)
    digest = sha256(b"P-POLE-HEIGHT-COMMON-ODD-1/joint-bias16-v1\n")
    digest.update(len(keys).to_bytes(8, "big"))
    for key in keys:
        digest.update(key)
    return digest.hexdigest()


def word_set_digest(words):
    digest = sha256(b"P-POLE-HEIGHT-COMMON-ODD-1/edge-word-set-v1\n")
    digest.update(len(words).to_bytes(8, "big"))
    for word in sorted(words):
        digest.update(len(word).to_bytes(4, "big"))
        digest.update(bytes(word))
    return digest.hexdigest()


def audit_w38(helpers):
    text = ("12 12 12 12 35 36 13 13 13 13 16 26 26 26 16 16 "
            "23 23 23 23 26 26 26 16 13 13 13 13 36 34 45 45 45 45 "
            "46 46 12 12")
    word = parse_word(text)
    assert len(word) == 38
    ids = tuple(EDGES.index(edge) for edge in word)
    endpoints = {}
    for t in range(-2, 3):
        endpoint, branches, changed = replay(initial(t, helpers), word)
        endpoints[t] = endpoint
        first_four = endpoint[:4] == target(t, helpers)[:4]
        returned = endpoint[4:] == helpers
        emit("W38_INPUT", t=t, final_state=endpoint,
             target_first_four=first_four, helpers_returned=returned,
             admission_bits=branches, changed_steps=changed,
             forward_contacts=38, inverse_contacts=152, inverse_recovery=True)
        if t in (-1, 1):
            assert endpoint == target(t, helpers)
    emit("W38_SCOPE", odd_pair_verified=True,
         common_five=all(endpoints[t] == target(t, helpers) for t in range(-2, 3)),
         minimum_38="NOT_AUDITED")
    return ids, endpoints


def odd_loop_candidates(root):
    tree = {root: ()}
    queue = deque([root])
    truncated = False
    tree_edges = 0
    while queue:
        state = queue.popleft()
        path = tree[state]
        if len(path) >= ODD_DEPTH:
            continue
        for edge in range(15):
            after = apply_joint(state, (edge,))
            tree_edges += 1
            if after not in tree:
                if len(tree) >= ODD_CAP:
                    truncated = True
                    continue
                tree[after] = path + (edge,)
                queue.append(after)
    # A second pass includes all boundary self-loops and edges to states
    # discovered later in the breadth-first traversal.
    candidates = set()
    internal = 0
    external = 0
    for state in sorted(tree, key=joint_key):
        path = tree[state]
        assert apply_joint(root, path) == state
        for edge in range(15):
            after = apply_joint(state, (edge,))
            if after not in tree:
                external += 1
                continue
            internal += 1
            loop = normalize_ids(path + (edge,) + inverse_ids(tree[after]))
            if not loop:
                continue
            inverse = inverse_ids(loop)
            assert len(loop) <= 21 and len(inverse) <= 24
            representative = min(loop, inverse)
            candidates.add(representative)
    assert internal + external == 15 * len(tree)
    primitives = tuple((edge,) for edge in range(15)
                       if apply_joint(root, (edge,)) == root)
    assert len(primitives) == 12 and set(primitives) <= candidates
    emit("ODD_TREE", depth_limit=ODD_DEPTH, state_cap=ODD_CAP,
         stored_states=len(tree), tree_edge_offers=tree_edges,
         internal_edges=internal, external_edges=external,
         capped=truncated, tree_sha256=state_set_digest(tree),
         formal_undirected_loops=len(candidates),
         loop_sha256=word_set_digest(candidates), reserved_primitives=len(primitives))
    return candidates, primitives


def select_loops(root, start, goal, candidates, primitives):
    primitive_set = set(primitives)
    ranked = []
    evaluations = 0
    evaluation_contacts = 0
    odd_return_contacts = 0
    for word in sorted(candidates):
        inverse = inverse_ids(word)
        assert apply_joint(root, word) == root
        assert apply_joint(root, inverse) == root
        odd_return_contacts += 2 * (len(word) + len(inverse))
    for word in sorted(candidates - primitive_set):
        inverse = inverse_ids(word)
        forward_error = joint_error(apply_joint(start, word), goal)
        reverse_error = joint_error(apply_joint(goal, inverse), start)
        evaluations += 1
        evaluation_contacts += 3 * (len(word) + len(inverse))
        rank = (min(forward_error, reverse_error), forward_error + reverse_error,
                len(word) + len(inverse), word)
        ranked.append((rank, word, forward_error, reverse_error))
    ranked.sort()
    chosen = [(word, None, None, True) for word in primitives]
    chosen.extend((word, f, r, False) for _, word, f, r in ranked[:EXTRA_LOOPS])
    moves = []
    reserved_flags = []
    for word, _, _, reserved in chosen:
        for directed in (word, inverse_ids(word)):
            assert directed not in moves
            assert apply_joint(root, directed) == root
            moves.append(directed)
            reserved_flags.append(reserved)
    assert len(moves) <= 64
    inverse_indices = tuple(moves.index(inverse_ids(word)) for word in moves)
    assert all(inverse_indices[inverse_indices[i]] == i for i in range(len(moves)))
    emit("LOOP_SELECTION", candidate_evaluations=evaluations, candidate_odd_return_checks=2 * len(candidates), logical_odd_case_contacts=odd_return_contacts,
         logical_even_case_contacts=evaluation_contacts,
         undirected_selected=len(chosen), directed_selected=len(moves),
         reserved_undirected=len(primitives),
         best_ranked_scores=[(f, r) for _, _, f, r in ranked[:EXTRA_LOOPS]],
         directed_word_sha256=word_set_digest(moves))
    for i, word in enumerate(moves):
        emit("MACRO", id=i, inverse_id=inverse_indices[i], contacts=len(word),
             word=format_ids(word), reserved_primitive=reserved_flags[i])
    return tuple(moves), inverse_indices


def beam_extension(start, goal, moves, inverse_indices):
    # A frontier record is(state, macro-ID path, elementary length, Q error).
    roots = (start, goal)
    frontiers = [[(state, (), 0, joint_error(state, roots[1 - side]))]
                 for side, state in enumerate(roots)]
    visited = [OrderedDict([(state, ((), 0))]) for state in roots]
    used_contacts = 0
    offered = [0, 0]
    applied = [0, 0]
    complete_layers = [0, 0]
    best_errors = [frontiers[0][0][3], frontiers[1][0][3]]

    def combine(side, path, other_path):
        front_path, back_path = (path, other_path) if side == 0 else (other_path, path)
        return front_path + tuple(inverse_indices[i] for i in reversed(back_path))

    def finish(status, path=None, partial=False):
        emit("EVEN_SEARCH", status=status, witness_found=path is not None,
             completed_layers=complete_layers, offered_macros=offered,
             applied_macros=applied, logical_even_case_contacts=used_contacts,
             contact_budget=BEAM_CONTACT_BUDGET,
             retained_visited=[len(v) for v in visited],
             visited_sha256=[state_set_digest(v) for v in visited],
             best_Q_errors=best_errors, partial_layer=partial,
             shortest_claim=False)
        return status, path

    if start == goal:
        return finish("BASE_ALREADY_SOLVES_ALL", ())
    for _ in range(BEAM_ROUNDS):
        for side in (0, 1):
            other = 1 - side
            candidates = {}
            for state, path, length, _ in frontiers[side]:
                for move_id, word in enumerate(moves):
                    offered[side] += 1
                    cost = 3 * len(word)
                    if used_contacts + cost > BEAM_CONTACT_BUDGET:
                        return finish("LIMIT_CONTACT_BUDGET", partial=True)
                    used_contacts += cost
                    applied[side] += 1
                    after = apply_joint(state, word)
                    next_path = path + (move_id,)
                    next_length = length + len(word)
                    if after in visited[other]:
                        other_path, _ = visited[other][after]
                        # The complete candidate path is retained locally even
                        # before this candidate is selected for the next beam.
                        return finish("FOUND", combine(side, next_path, other_path), partial=True)
                    if after in visited[side]:
                        continue
                    previous = candidates.get(after)
                    if previous is not None and (previous[0], previous[1]) <= (next_length, next_path):
                        continue
                    error = joint_error(after, roots[other])
                    best_errors[side] = min(best_errors[side], error)
                    candidates[after] = (next_length, next_path, error)
            assert len(candidates) <= BEAM_WIDTH * len(moves)
            ordered = sorted(candidates.items(), key=lambda item: (
                item[1][2], item[1][0], joint_key(item[0]), item[1][1]))[:BEAM_WIDTH]
            frontiers[side] = [(state, path, length, error)
                               for state, (length, path, error) in ordered]
            for state, path, length, _ in frontiers[side]:
                assert state not in visited[side]
                visited[side][state] = (path, length)
                while len(visited[side]) > VISITED_CAP:
                    visited[side].popitem(last=False)
            complete_layers[side] += 1
            emit("BEAM_LAYER", side=side, layer=complete_layers[side],
                 candidate_states=len(candidates), retained=len(frontiers[side]),
                 visited=len(visited[side]),
                 best_retained_Q=None if not frontiers[side] else frontiers[side][0][3],
                 best_seen_Q=best_errors[side], logical_even_case_contacts=used_contacts)
            if not frontiers[side]:
                return finish("LIMIT_EMPTY_HEURISTIC_FRONTIER")
    return finish("LIMIT_LAYER_BUDGET")


def audit_extension(base_word, extension_path, moves, helpers):
    odd_root = tuple(target(t, helpers) for t in (-1, 1))
    odd_state = odd_root
    extension_word = ()
    for move_id in extension_path:
        word = moves[move_id]
        odd_state = apply_joint(odd_state, word)
        assert odd_state == odd_root
        extension_word += word
    complete = base_word + extension_word
    pairs = tuple(EDGES[i] for i in complete)
    emit("COMMON_WORD", macro_ids=extension_path, macro_boundaries=len(extension_path),
         extension_contacts=len(extension_word), total_contacts=len(complete),
         word=format_ids(complete), odd_boundary_retention=True, shortest_claim=False)
    for t in range(-2, 3):
        endpoint, branches, changed = replay(initial(t, helpers), pairs)
        assert endpoint == target(t, helpers)
        emit("COMMON_WORD_INPUT", t=t, target_verified=True, helpers_returned=True,
             final_state=endpoint, admission_bits=branches, changed_steps=changed,
             inverse_contacts=4 * len(complete), inverse_recovery=True)


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    emit("PROBE", name="P-POLE-HEIGHT-COMMON-ODD-1", arithmetic="EXACT_INTEGER",
         observation="RESULT_EXPOSED", odd_depth=ODD_DEPTH, odd_state_cap=ODD_CAP,
         extra_undirected_loops=EXTRA_LOOPS, beam_width=BEAM_WIDTH,
         rounds_per_direction=BEAM_ROUNDS, visited_cap_per_direction=VISITED_CAP,
         logical_beam_contact_budget=BEAM_CONTACT_BUDGET)
    helpers = ((1, 1, 0, -2), (2, 0, 0, 0))
    base_word, endpoints = audit_w38(helpers)
    classifier_audit()
    odd_root = tuple(target(t, helpers) for t in (-1, 1))
    even_start = tuple(endpoints[t] for t in (-2, 0, 2))
    even_goal = tuple(target(t, helpers) for t in (-2, 0, 2))
    assert all(state_totals(a) == state_totals(b) for a, b in zip(even_start, even_goal))
    emit("EXTENSION_ROOTS", odd_target=odd_root, even_source=even_start, even_target=even_goal,
         initial_Q_error=joint_error(even_start, even_goal))
    candidates, primitives = odd_loop_candidates(odd_root)
    moves, inverse_indices = select_loops(odd_root, even_start, even_goal, candidates, primitives)
    status, extension_path = beam_extension(even_start, even_goal, moves, inverse_indices)
    if extension_path is not None:
        audit_extension(base_word, extension_path, moves, helpers)
    emit("RESULT", supplied_odd_word="VERIFIED", finite_classifier="PASS",
         common_five_search=status, common_five_verified=extension_path is not None,
         minimum_38="NOT_AUDITED", canon_promotion=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
