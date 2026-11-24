#!/usr/bin/env python3
"""Exact zero stabilizer certificate and bounded constructive common-word search.

Scientific work starts only under main(). Limits constrain the optional
stabilizer-chain search; they never establish impossibility. Two arithmetic
representations independently check every audited contact.
"""

from pathlib import Path
from functools import lru_cache
from hashlib import sha256
from itertools import product
import heapq
import json
import sys


ZERO_CAP = 4096
ZERO_PATH_CAP = 4096
ZERO_POOL = 4096
H0_BANK = 256
H0_WORD_CAP = 256
COLLISION_POOL = 2048
H1_BANK = 128
H1_WORD_CAP = 4096
BRIDGE_POOL = 64
BRIDGE_ROOTS = 8
WALK_STEPS = 32768
WALK_DEPTH = 8
WORK_BUDGET = 100000000
FINAL_WORD_CAP = 100000
SEED_B = 0xD1B54A32D192ED03
SEED_C = 0x94D049BB133111EB
BANK_SHA256 = "d4270e03f851f0d2327e2eac7f23cc796b9bbffb1e54b2943f52a0c89fb83f07"
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


def normalize(word):
    blocks = []
    for edge in word:
        if blocks and blocks[-1][0] == edge:
            power = (blocks.pop()[1] + 1) % 5
            if power:
                blocks.append((edge, power))
        else:
            blocks.append((edge, 1))
    return tuple(edge for edge, power in blocks for _ in range(power))


def inverse_word(word):
    return normalize(edge for edge in reversed(word) for _ in range(4))


def format_word(word):
    return " ".join(f"{EDGES[e][0] + 1}{EDGES[e][1] + 1}" for e in word)


def word_hash(words):
    digest = sha256(b"STABILIZER-CHAIN/native-edge-words-v1\n")
    for word in sorted(words, key=lambda w: (len(w), w)):
        digest.update(len(word).to_bytes(4, "big"))
        digest.update(bytes(word))
    return digest.hexdigest()


class WorkLimit(Exception):
    pass


class Budget:
    def __init__(self):
        self.used = 0
        self.phase = "INITIAL"

    def take(self, count):
        if self.used + count > WORK_BUDGET:
            raise WorkLimit(self.phase)
        self.used += count


class Engine:
    """Exact value IDs and run-length programs; every new pair has dual audit."""
    def __init__(self):
        self.values, self.value_ids = [], {}
        self.words, self.blocks, self.word_ids = [], [], {}
        self.inverses = {}
        self.program(())

    def value(self, x):
        if x not in self.value_ids:
            self.value_ids[x] = len(self.values)
            self.values.append(x)
        return self.value_ids[x]

    def encode(self, state):
        return tuple(self.value(x) for x in state)

    def decode(self, state):
        return tuple(self.values[x] for x in state)

    def key(self, state):
        flat = tuple(a for x in self.decode(state) for a in x)
        assert len(flat) == 24 and all(-12 <= a <= 12 for a in flat)
        return bytes(a + 16 for a in flat)

    def program(self, word):
        word = normalize(word)
        if word not in self.word_ids:
            program = len(self.words)
            self.word_ids[word] = program
            self.words.append(word)
            blocks = []
            for edge in word:
                if blocks and blocks[-1][0] == edge:
                    blocks[-1] = (edge, blocks[-1][1] + 1)
                else:
                    blocks.append((edge, 1))
            assert all(1 <= power <= 4 for _, power in blocks)
            self.blocks.append(tuple(blocks))
        return self.word_ids[word]

    def inverse(self, program):
        if program not in self.inverses:
            other = self.program(inverse_word(self.words[program]))
            self.inverses[program] = other
            self.inverses[other] = program
        return self.inverses[program]

    @lru_cache(maxsize=100000)
    def cycle(self, a, b):
        x, y = self.values[a], self.values[b]
        audit_pair(x, y)
        result = [(a, b)]
        for _ in range(4):
            x, y = contact4(x, y)
            result.append((self.value(x), self.value(y)))
        return tuple(result)

    @lru_cache(maxsize=30000)
    def apply(self, state, program):
        out = list(state)
        for edge, power in self.blocks[program]:
            i, j = EDGES[edge]
            out[i], out[j] = self.cycle(out[i], out[j])[power]
        return tuple(out)

    def do(self, state, program, budget):
        budget.take(len(self.words[program]))
        return self.apply(state, program)

    def flatten(self, path):
        return normalize(edge for program in path for edge in self.words[program])


class WordPool:
    """A deterministic bounded set of shortest formal words, with lex ties."""
    def __init__(self, cap):
        self.cap, self.heap, self.members = cap, [], set()
        self.offers = 0

    def add(self, word):
        self.offers += 1
        if word in self.members:
            return
        item = (-len(word), tuple(-e for e in word), word)
        if len(self.heap) < self.cap:
            heapq.heappush(self.heap, item)
            self.members.add(word)
        elif (len(word), word) < (len(self.heap[0][2]), self.heap[0][2]):
            old = heapq.heapreplace(self.heap, item)
            self.members.remove(old[2])
            self.members.add(word)

    def ordered(self):
        return sorted(self.members, key=lambda word: (len(word), word))


class Rng:
    def __init__(self, seed):
        assert seed
        self.state = seed

    def next(self):
        mask = (1 << 64) - 1
        x = self.state
        x ^= x >> 12
        x ^= (x << 25) & mask
        x ^= x >> 27
        self.state = x & mask
        return (self.state * 2685821657736338717) & mask


def load_fixture(engine):
    raw = Path(__file__).with_name("BANK.json").read_bytes()
    assert sha256(raw).hexdigest() == BANK_SHA256
    rows = json.loads(raw)
    records = sorted((r for r in rows if r["kind"] == "MACRO"), key=lambda r: r["id"])
    assert [r["id"] for r in records] == list(range(64))
    bank = []
    for record in records:
        pairs = parse_word(record["word"])
        assert len(pairs) == record["contacts"]
        ids = tuple(EDGES.index(edge) for edge in pairs)
        assert normalize(ids) == ids
        bank.append(engine.program(ids))
    for record in records:
        assert engine.inverse(bank[record["id"]]) == bank[record["inverse_id"]]
    roots = [r for r in rows if r["kind"] == "EXTENSION_ROOTS"]
    assert len(roots) == 1
    convert = lambda state: tuple(tuple(x) for x in state)
    odd = tuple(convert(s) for s in roots[0]["odd_target"])
    source = tuple(convert(s) for s in roots[0]["even_source"])
    goal = tuple(convert(s) for s in roots[0]["even_target"])
    helpers = ((1, 1, 0, -2), (2, 0, 0, 0))
    assert odd == tuple(target(t, helpers) for t in (-1, 1))
    assert goal == tuple(target(t, helpers) for t in (-2, 0, 2))
    w38 = parse_word("12 12 12 12 35 36 13 13 13 13 16 26 26 26 16 16 23 23 23 23 26 26 26 16 13 13 13 13 36 34 45 45 45 45 46 46 12 12")
    assert len(w38) == 38
    for t in range(-2, 3):
        end, _, _ = replay(initial(t, helpers), w38)
        assert end == (odd[(-1, 1).index(t)] if t in (-1, 1) else source[(-2, 0, 2).index(t)])
    for program in bank:
        word = tuple(EDGES[e] for e in engine.words[program])
        for state in odd:
            end, _, _ = replay(state, word)
            assert end == state
    emit("FIXTURE", sha256=BANK_SHA256, macros=len(bank),
         W38_all_five_endpoints_verified=True, odd_fixing_verified=True,
         formal_inverse_pairs_verified=True)
    return (tuple(bank), tuple(engine.encode(s) for s in odd),
            tuple(engine.encode(s) for s in source), tuple(engine.encode(s) for s in goal),
            tuple(EDGES.index(e) for e in w38), helpers)


def zero_orbit(engine, budget, bank, root, source):
    budget.phase = "ZERO_ORBIT"
    distances = {root: 0}
    parent = {}
    adjacency = {}
    queue = [(0, engine.key(root), root)]
    while queue:
        distance, _, state = heapq.heappop(queue)
        if distance != distances[state] or state in adjacency:
            continue
        row = []
        for program in bank:
            after = engine.do(state, program, budget)
            if after not in distances and len(distances) >= ZERO_CAP:
                emit("ZERO_ORBIT", status="LIMIT_STATES", states=len(distances),
                     closed=False, exposed_1556_match=None)
                raise WorkLimit("ZERO_STATE_CAP")
            new_distance = distance + len(engine.words[program])
            if after not in distances or new_distance < distances[after]:
                distances[after] = new_distance
                parent[after] = (state, program)
                heapq.heappush(queue, (new_distance, engine.key(after), after))
            row.append(after)
        adjacency[state] = tuple(row)
    assert len(adjacency) == len(distances)
    paths = {root: ()}
    for state in sorted(distances, key=lambda s: (distances[s], engine.key(s))):
        if state != root:
            before, program = parent[state]
            assert before in paths
            assert distances[state] == distances[before] + len(engine.words[program])
            paths[state] = normalize(paths[before] + engine.words[program])
        assert len(paths[state]) <= distances[state]
        for program, after in zip(bank, adjacency[state]):
            assert after in adjacency
            assert distances[after] <= distances[state] + len(engine.words[program])
    digest = sha256(b"STABILIZER-CHAIN/zero-tree-and-edges-v1\n")
    for state in sorted(adjacency, key=engine.key):
        digest.update(engine.key(state))
        digest.update(len(paths[state]).to_bytes(4, "big"))
        digest.update(bytes(paths[state]))
        for after in adjacency[state]:
            digest.update(engine.key(after))
    emit("ZERO_ORBIT", status="COMPLETE", states=len(adjacency), closed=True,
         edges=64 * len(adjacency), source_in_orbit=source in adjacency,
         max_tree_native_cost=max(distances.values()), certificate_sha256=digest.hexdigest(),
         exposed_1556_match=len(adjacency) == 1556)
    if source not in adjacency:
        return None
    bridge_word = inverse_word(paths[source])
    if len(bridge_word) > ZERO_PATH_CAP:
        raise WorkLimit("ZERO_BRIDGE_WORD_CAP")
    bridge = engine.program(bridge_word)
    assert engine.do(source, bridge, budget) == root
    pool = WordPool(ZERO_POOL)
    eligible = 0
    for state in sorted(adjacency, key=engine.key):
        for program, after in zip(bank, adjacency[state]):
            word = normalize(paths[state] + engine.words[program] + inverse_word(paths[after]))
            if not word:
                continue
            inverse = inverse_word(word)
            if max(len(word), len(inverse)) <= H0_WORD_CAP:
                eligible += 1
                pool.add(min(word, inverse))
    emit("ZERO_SCHREIER", full_family_edges=64 * len(adjacency),
         full_family_representation="COMPLETE_TREE_PLUS_ALL_EDGES",
         eligible_word_offers=eligible, retained_formal_pool=len(pool.members),
         pool_cap=ZERO_POOL, word_cap=H0_WORD_CAP, pool_sha256=word_hash(pool.members),
         kernel_words_not_quotiented=True, bridge_contacts=len(bridge_word),
         bridge_word=format_word(bridge_word))
    return bridge, pool


def select_bank(engine, budget, pool, limit, fixed, future, label):
    budget.phase = label + "_SELECTION"
    signatures = set()
    selected = []
    scored = 0
    for word in pool.ordered():
        program = engine.program(word)
        signature = tuple(engine.do(state, program, budget) for state in future)
        scored += 1
        if signature in signatures:
            continue  # Heuristic diversity selection, never a group quotient.
        signatures.add(signature)
        inverse = engine.inverse(program)
        for directed in (program, inverse):
            for state in fixed:
                assert engine.do(state, directed, budget) == state
            selected.append(directed)
        if len(selected) // 2 >= limit:
            break
    assert len(selected) == len(set(selected))
    assert all(engine.inverse(program) in selected for program in selected)
    emit("SELECTED_BANK", label=label, pool=len(pool.members), scored=scored,
         undirected=len(selected) // 2, directed=len(selected),
         word_lengths=[len(engine.words[p]) for p in selected],
         native_words_sha256=word_hash(engine.words[p] for p in selected),
         reduction="EXPLICIT_HEURISTIC_SUBGROUP_SELECTION",
         logical_contacts=budget.used)
    return tuple(selected)


def walk_search(engine, budget, sources, target_state, bank, seed, collect, label):
    """Sources carry external bridge indices; all target paths have one root."""
    budget.phase = label
    rng = Rng(seed)
    seen = [{state: (i, (), 0) for i, state in enumerate(sources)}, {target_state: (0, (), 0)}]
    current = [None, None]
    bridges = WordPool(BRIDGE_POOL)
    collisions = WordPool(COLLISION_POOL)
    steps = [0, 0]
    meetings = 0
    limited = False
    found = None
    for i, state in enumerate(sources):
        if state == target_state:
            if not collect:
                found = (i, ())
            else:
                bridges.add(())
    if not bank:
        return bridges, collisions, found, True
    for step in range(WALK_STEPS):
        if found is not None and not collect:
            break
        for side in (0, 1):
            if step % WALK_DEPTH == 0:
                base = (step // WALK_DEPTH) % len(sources) if side == 0 else 0
                root = sources[base] if side == 0 else target_state
                current[side] = (root, base, (), 0)
            state, base, path, cost = current[side]
            index = rng.next() % len(bank)
            if path and bank[index] == engine.inverse(path[-1]):
                index = (index + 1) % len(bank)
            program = bank[index]
            try:
                after = engine.do(state, program, budget)
            except WorkLimit:
                limited = True
                break
            steps[side] += 1
            new_path = path + (program,)
            new_cost = cost + len(engine.words[program])
            record = (base, new_path, new_cost)
            current[side] = (after, base, new_path, new_cost)
            opposite = seen[1 - side].get(after)
            if opposite is not None:
                meetings += 1
                front, back = (record, opposite) if side == 0 else (opposite, record)
                word = normalize(engine.flatten(front[1]) + inverse_word(engine.flatten(back[1])))
                if collect:
                    assert front[0] == 0
                    bridges.add(word)
                else:
                    found = (front[0], word)
                    break
            previous = seen[side].get(after)
            if collect and side == 1 and previous is not None:
                word = normalize(engine.flatten(new_path) + inverse_word(engine.flatten(previous[1])))
                if word:
                    inverse = inverse_word(word)
                    assert max(len(word), len(inverse)) <= H1_WORD_CAP
                    collisions.add(min(word, inverse))
            if previous is None or (new_cost, base, new_path) < (previous[2], previous[0], previous[1]):
                seen[side][after] = record
        if limited or (found is not None and not collect):
            break
    emit("WALK", label=label, seed=seed, steps=steps, restart_depth=WALK_DEPTH,
         source_roots=len(sources), seen_states=[len(s) for s in seen],
         meetings=meetings, bridge_words=len(bridges.members),
         bridge_pool_sha256=word_hash(bridges.members),
         collision_offers=collisions.offers, collision_words=len(collisions.members),
         collision_sha256=word_hash(collisions.members),
         limit_reached=limited, final_witness=found is not None,
         logical_contacts=budget.used)
    return bridges, collisions, found, limited


def final_audit(engine, base, a, b, c, helpers):
    # Audits are reserved outside the exploratory budget.
    full = normalize(base + engine.words[a] + engine.words[b] + c)
    if len(full) > FINAL_WORD_CAP:
        emit("FINAL_WORD", status="INCONCLUSIVE_WORD_CAP", contacts=len(full), cap=FINAL_WORD_CAP)
        return False
    word = tuple(EDGES[e] for e in full)
    emit("COMMON_WORD", contacts=len(full), word=format_word(full),
         native_word_sha256=word_hash([full]), shortest_claim=False,
         zero_bridge_contacts=len(engine.words[a]), minus_bridge_contacts=len(engine.words[b]),
         plus_bridge_contacts=len(c))
    for t in range(-2, 3):
        endpoint, branches, changed = replay(initial(t, helpers), word)
        assert endpoint == target(t, helpers)
        emit("COMMON_WORD_INPUT", t=t, endpoint=endpoint, target_verified=True,
             helpers_returned=True, changed_steps=changed,
             admission_sha256=sha256(branches.encode("ascii")).hexdigest(),
             inverse_contacts=4 * len(full), inverse_recovery=True)
    return True


def search(engine, budget, bank, odd, source, goal, base, helpers):
    zero = zero_orbit(engine, budget, bank, goal[1], source[1])
    if zero is None:
        return "NO_WORD_IN_K0_ZERO_OBSTRUCTION", False
    a, pool = zero
    budget.phase = "AFTER_ZERO"
    rminus = engine.do(source[0], a, budget)
    rplus = engine.do(source[2], a, budget)
    fixed0 = odd + (goal[1],)
    h0 = select_bank(engine, budget, pool, H0_BANK, fixed0,
                     (rminus, goal[0], rplus, goal[2]), "H0")
    if not h0:
        return "INCONCLUSIVE_EMPTY_H0_BANK", False
    bridges, collisions, _, limited = walk_search(engine, budget, (rminus,), goal[0],
                                                  h0, SEED_B, True, "MINUS_TRANSPORT")
    if limited:
        return "INCONCLUSIVE_WORK_BUDGET", False
    if not bridges.members:
        return "INCONCLUSIVE_MINUS_TRANSPORT", False
    budget.phase = "BRIDGE_ROOT_SELECTION"
    chosen, roots, distinct = [], [], set()
    for word in bridges.ordered():
        b = engine.program(word)
        assert engine.do(rminus, b, budget) == goal[0]
        assert engine.do(goal[1], b, budget) == goal[1]
        root = engine.do(rplus, b, budget)
        if root in distinct:
            continue
        distinct.add(root)
        chosen.append(b)
        roots.append(root)
        if len(chosen) >= BRIDGE_ROOTS:
            break
    emit("MINUS_BRIDGES", selected=len(chosen),
         native_lengths=[len(engine.words[b]) for b in chosen],
         native_words=[format_word(engine.words[b]) for b in chosen],
         plus_sources=[engine.decode(s) for s in roots])
    for index, root in enumerate(roots):
        if root == goal[2]:
            verified = final_audit(engine, base, a, chosen[index], (), helpers)
            return "FOUND" if verified else "INCONCLUSIVE_WORD_CAP", verified
    if not collisions.members:
        return "INCONCLUSIVE_EMPTY_COLLISION_POOL", False
    h1 = select_bank(engine, budget, collisions, H1_BANK, fixed0 + (goal[0],),
                     (roots[0], goal[2]), "H1")
    if not h1:
        return "INCONCLUSIVE_EMPTY_H1_BANK", False
    _, _, found, limited = walk_search(engine, budget, tuple(roots), goal[2],
                                       h1, SEED_C, False, "PLUS_TRANSPORT")
    if found is None:
        return "INCONCLUSIVE_WORK_BUDGET" if limited else "INCONCLUSIVE_PLUS_TRANSPORT", False
    index, c = found
    c_program = engine.program(c)
    assert engine.apply(goal[1], c_program) == goal[1]
    assert engine.apply(goal[0], c_program) == goal[0]
    assert all(engine.apply(s, c_program) == s for s in odd)
    assert engine.apply(roots[index], c_program) == goal[2]
    verified = final_audit(engine, base, a, chosen[index], c, helpers)
    return "FOUND" if verified else "INCONCLUSIVE_WORD_CAP", verified


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    emit("PROBE", name="P-POLE-HEIGHT-STABILIZER-CHAIN-1", arithmetic="EXACT_INTEGER",
         zero_cap=ZERO_CAP, zero_pool=ZERO_POOL, H0_undirected=H0_BANK,
         H0_word_cap=H0_WORD_CAP, collision_pool=COLLISION_POOL,
         H1_undirected=H1_BANK, H1_word_cap=H1_WORD_CAP,
         steps_per_side=WALK_STEPS, restart_depth=WALK_DEPTH,
         bridge_pool=BRIDGE_POOL, bridge_roots=BRIDGE_ROOTS,
         work_budget=WORK_BUDGET, final_word_cap=FINAL_WORD_CAP)
    import smallstock
    smallstock.run()
    engine = Engine()
    bank, odd, source, goal, base, helpers = load_fixture(engine)
    budget = Budget()
    try:
        status, verified = search(engine, budget, bank, odd, source, goal, base, helpers)
    except WorkLimit as exc:
        status, verified = "INCONCLUSIVE_" + str(exc), False
    emit("RESULT", status=status, common_five_verified=verified,
         logical_search_contacts=budget.used, final_audit_budget="RESERVED_SEPARATELY",
         selected_banks_complete_stabilizers=False, canon_promotion=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
