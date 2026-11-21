#!/usr/bin/env python3
"""Exact full-Schreier streaming construction with kernel-preserving collision loops.

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
WORK_BUDGET = 300000000
FINAL_WORD_CAP = 100000
BRIDGE_ROOTS = 8
WALK_STEPS = 32768
WALK_DEPTH = 8
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


class Found(Exception):
    def __init__(self, root, continuation):
        self.root, self.continuation = root, continuation


class Budget:
    def __init__(self):
        self.used, self.phase = 0, "INITIAL"

    def take(self, count):
        if self.used + count > WORK_BUDGET:
            raise WorkLimit(self.phase)
        self.used += count


class Engine:
    """Shared exact program DAG, with independently audited integral contacts."""
    def __init__(self):
        self.values, self.value_ids = [], {}
        self.nodes, self.costs = [("i",)], [0]
        self.leaves, self.joins, self.inverses = {(): 0}, {}, {0: 0}

    def value(self, value):
        if value not in self.value_ids:
            self.value_ids[value] = len(self.values)
            self.values.append(value)
        return self.value_ids[value]

    def encode(self, state):
        return tuple(self.value(value) for value in state)

    def decode(self, state):
        return tuple(self.values[value] for value in state)

    def key(self, state):
        flat = tuple(a for value in self.decode(state) for a in value)
        assert len(flat) == 24 and all(-12 <= a <= 12 for a in flat)
        return bytes(a + 16 for a in flat)

    def program(self, word):
        word = normalize(word)
        if word not in self.leaves:
            blocks = []
            for edge in word:
                if blocks and blocks[-1][0] == edge:
                    blocks[-1] = (edge, blocks[-1][1] + 1)
                else:
                    blocks.append((edge, 1))
            assert all(1 <= power <= 4 for _, power in blocks)
            self.leaves[word] = len(self.nodes)
            self.nodes.append(("l", tuple(blocks), word))
            self.costs.append(len(word))
        return self.leaves[word]

    def join(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if self.inverses.get(a) == b or self.inverses.get(b) == a:
            return 0
        left, right = self.nodes[a], self.nodes[b]
        if left[0] == "j" and self.inverses.get(left[2]) == b:
            return left[1]
        if right[0] == "j" and self.inverses.get(a) == right[1]:
            return right[2]
        key = a, b
        if key not in self.joins:
            self.joins[key] = len(self.nodes)
            self.nodes.append(("j", a, b))
            self.costs.append(self.costs[a] + self.costs[b])
        return self.joins[key]

    def inverse(self, program):
        if program not in self.inverses:
            node = self.nodes[program]
            if node[0] == "l":
                result = self.program(inverse_word(node[2]))
            else:
                assert node[0] == "j"
                result = self.join(self.inverse(node[2]), self.inverse(node[1]))
            self.inverses[program] = result
            self.inverses.setdefault(result, program)
        return self.inverses[program]

    def expand(self, program):
        result, stack = [], [program]
        while stack:
            node = self.nodes[stack.pop()]
            if node[0] == "l":
                result.extend(node[2])
            elif node[0] == "j":
                stack.extend((node[2], node[1]))
        assert len(result) == self.costs[program]
        return tuple(result)

    @lru_cache(maxsize=100000)
    def cycle(self, a, b):
        x, y = self.values[a], self.values[b]
        audit_pair(x, y)
        result = [(a, b)]
        for _ in range(4):
            x, y = contact4(x, y)
            result.append((self.value(x), self.value(y)))
        return tuple(result)

    @lru_cache(maxsize=100000)
    def apply(self, state, program):
        node = self.nodes[program]
        if node[0] == "i":
            return state
        if node[0] == "j":
            return self.apply(self.apply(state, node[1]), node[2])
        out = list(state)
        for edge, power in node[1]:
            i, j = EDGES[edge]
            out[i], out[j] = self.cycle(out[i], out[j])[power]
        return tuple(out)

    def do(self, state, program, budget):
        budget.take(self.costs[program])
        return self.apply(state, program)

    @lru_cache(maxsize=None)
    def digest(self, program):
        node = self.nodes[program]
        if node[0] == "i":
            payload = b"IDENTITY"
        elif node[0] == "l":
            payload = b"LEAF" + len(node[2]).to_bytes(4, "big") + bytes(node[2])
        else:
            payload = b"JOIN" + self.digest(node[1]) + self.digest(node[2])
        return sha256(payload).digest()


class Rng:
    def __init__(self, seed):
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
        a, b = bank[record["id"]], bank[record["inverse_id"]]
        assert engine.expand(engine.inverse(a)) == engine.expand(b)
        engine.inverses[a] = b
    record = [r for r in rows if r["kind"] == "EXTENSION_ROOTS"]
    assert len(record) == 1
    convert = lambda state: tuple(tuple(x) for x in state)
    odd = tuple(convert(s) for s in record[0]["odd_target"])
    source = tuple(convert(s) for s in record[0]["even_source"])
    goal = tuple(convert(s) for s in record[0]["even_target"])
    helpers = ((1, 1, 0, -2), (2, 0, 0, 0))
    assert odd == tuple(target(t, helpers) for t in (-1, 1))
    assert goal == tuple(target(t, helpers) for t in (-2, 0, 2))
    w38 = parse_word("12 12 12 12 35 36 13 13 13 13 16 26 26 26 16 16 23 23 23 23 26 26 26 16 13 13 13 13 36 34 45 45 45 45 46 46 12 12")
    assert len(w38) == 38
    for t in range(-2, 3):
        end, _, _ = replay(initial(t, helpers), w38)
        expected = odd[(-1, 1).index(t)] if t in (-1, 1) else source[(-2, 0, 2).index(t)]
        assert end == expected
    for program in bank:
        word = tuple(EDGES[e] for e in engine.expand(program))
        for state in odd:
            end, _, _ = replay(state, word)
            assert end == state
    emit("FIXTURE", sha256=BANK_SHA256, macros=64, W38_endpoints_verified=True,
         odd_fixing_verified=True, formal_inverses_verified=True)
    return (tuple(bank), tuple(engine.encode(s) for s in odd),
            tuple(engine.encode(s) for s in source), tuple(engine.encode(s) for s in goal),
            engine.program(tuple(EDGES.index(e) for e in w38)), helpers)


def build_zero(engine, budget, bank, root, source):
    budget.phase = "ZERO_ORBIT"
    distances, parent, adjacency = {root: 0}, {}, {}
    queue = [(0, engine.key(root), root)]
    while queue:
        distance, _, state = heapq.heappop(queue)
        if distance != distances[state] or state in adjacency:
            continue
        row = []
        for program in bank:
            after = engine.do(state, program, budget)
            if after not in distances and len(distances) >= ZERO_CAP:
                emit("ZERO_ORBIT", complete=False, states=len(distances), status="LIMIT_STATES")
                raise WorkLimit("ZERO_STATE_CAP")
            cost = distance + engine.costs[program]
            if after not in distances or cost < distances[after]:
                distances[after] = cost
                parent[after] = state, program
                heapq.heappush(queue, (cost, engine.key(after), after))
            row.append(after)
        adjacency[state] = tuple(row)
    paths = {root: 0}
    for state in sorted(distances, key=lambda s: (distances[s], engine.key(s))):
        if state != root:
            before, program = parent[state]
            assert distances[state] == distances[before] + engine.costs[program]
            paths[state] = engine.join(paths[before], program)
        assert engine.costs[paths[state]] <= distances[state]
        for program, after in zip(bank, adjacency[state]):
            assert after in adjacency
            assert distances[after] <= distances[state] + engine.costs[program]
    digest = sha256(b"FULL-SCHREIER/zero-tree-edges-v1\n")
    descriptors = []
    for state in sorted(adjacency, key=engine.key):
        digest.update(engine.key(state))
        digest.update(engine.digest(paths[state]))
        for program, after in zip(bank, adjacency[state]):
            digest.update(engine.key(after))
            loop = engine.join(engine.join(paths[state], program), engine.inverse(paths[after]))
            descriptors.append(loop)
    emit("ZERO_ORBIT", complete=True, states=len(adjacency), edges=len(descriptors),
         source_in_orbit=source in adjacency, max_tree_cost=max(distances.values()),
         certificate_sha256=digest.hexdigest(), exposed_1556_match=len(adjacency) == 1556)
    if source not in adjacency:
        return None
    a = engine.inverse(paths[source])
    if engine.costs[a] > ZERO_PATH_CAP:
        raise WorkLimit("ZERO_BRIDGE_CAP")
    assert engine.do(source, a, budget) == root
    emit("FULL_SCHREIER", full_family=True, descriptor_count=len(descriptors),
         identity_descriptors=sum(p == 0 for p in descriptors),
         structural_programs=len(set(descriptors)),
         max_generator_cost=max(engine.costs[p] for p in descriptors),
         zero_bridge_cost=engine.costs[a], zero_bridge_word=format_word(engine.expand(a)),
         length_selection=False, fingerprint_selection=False)
    return a, descriptors


def audit_zero_prefix(engine, base, bridge, helpers):
    # Reserved certificate audit, outside the exploratory contact budget.
    ids = engine.expand(engine.join(base, bridge))
    pairs = tuple(EDGES[e] for e in ids)
    for t in (-1, 0, 1):
        endpoint, _, _ = replay(initial(t, helpers), pairs)
        assert endpoint == target(t, helpers)
    emit("ZERO_PREFIX_CERTIFICATE", inputs=[-1, 0, 1], contacts_per_input=len(ids),
         word=format_word(ids), native_word_sha256=word_hash([ids]),
         exact_full_endpoints=True, dual_arithmetic=True,
         inverse_contacts_per_input=4 * len(ids), inverse_recovery=True)


class Stream:
    def __init__(self, engine, budget, odd, goals, rminus, rplus, base, zero_bridge):
        self.e, self.budget = engine, budget
        self.odd, self.goals = odd, goals
        self.rminus, self.rplus = rminus, rplus
        self.base, self.a = base, zero_bridge
        self.minus_source, self.minus_target = {rminus: 0}, {goals[0]: 0}
        self.plus_source, self.plus_target = {}, {goals[2]: 0}
        self.bridges, self.roots, self.root_set = [], [], set()
        self.bridge_programs = set()
        self.collisions, self.collision_set = [], set()
        self.target_done = set()
        self.root_done = []
        self.descriptors_processed = self.unique_processed = 0
        self.direct_complete = False
        self.walk_steps = {"minus": [0, 0], "plus": [0, 0]}
        self.overlong = 0
        self.first_collision_representatives_fixed = True

    def initialize(self):
        if self.rminus == self.goals[0]:
            self.add_bridge(0, 0)

    def found(self, root, front, back):
        continuation = self.e.join(front, self.e.inverse(back))
        total = (self.e.costs[self.base] + self.e.costs[self.a] +
                 self.e.costs[self.bridges[root]] + self.e.costs[continuation])
        if total > FINAL_WORD_CAP:
            self.overlong += 1
            return
        raise Found(root, continuation)

    def plus_source_image(self, state, root, program):
        self.plus_source.setdefault(state, (root, program))
        if state in self.plus_target:
            self.found(root, program, self.plus_target[state])

    def plus_target_image(self, state, program):
        self.plus_target.setdefault(state, program)
        if state in self.plus_source:
            root, front = self.plus_source[state]
            self.found(root, front, program)

    def target_collision_image(self, program):
        if program not in self.target_done:
            state = self.e.do(self.goals[2], program, self.budget)
            self.target_done.add(program)
            self.plus_target_image(state, program)

    def root_collision_image(self, root, program):
        state = self.e.do(self.roots[root], program, self.budget)
        self.root_done[root] += 1
        self.plus_source_image(state, root, program)

    def add_bridge(self, front, back):
        if len(self.bridges) >= BRIDGE_ROOTS:
            return
        program = self.e.join(front, self.e.inverse(back))
        if program in self.bridge_programs:
            return
        self.bridge_programs.add(program)
        assert self.e.do(self.rminus, program, self.budget) == self.goals[0]
        assert self.e.do(self.goals[1], program, self.budget) == self.goals[1]
        root = self.e.do(self.rplus, program, self.budget)
        if root in self.root_set:
            return
        self.root_set.add(root)
        index = len(self.roots)
        self.roots.append(root)
        self.bridges.append(program)
        self.root_done.append(0)
        emit("MINUS_BRIDGE", index=index, contacts=self.e.costs[program],
             dag_sha256=self.e.digest(program).hex(), plus_source=self.e.decode(root))
        self.plus_source_image(root, index, 0)
        # A new root must see all previously retained collision directions.
        for collision in self.collisions:
            self.target_collision_image(collision)
            self.root_collision_image(index, collision)

    def add_collision(self, front, representative):
        loop = self.e.join(front, self.e.inverse(representative))
        if not loop:
            return
        for program in (loop, self.e.inverse(loop)):
            if not program or program in self.collision_set:
                continue
            self.collision_set.add(program)
            self.collisions.append(program)
            if self.roots:
                self.target_collision_image(program)
                for root in range(len(self.roots)):
                    self.root_collision_image(root, program)

    def minus_source_image(self, state, program):
        self.minus_source.setdefault(state, program)
        if state in self.minus_target:
            self.add_bridge(program, self.minus_target[state])

    def minus_target_image(self, state, program):
        if state in self.minus_source:
            self.add_bridge(self.minus_source[state], program)
        if state in self.minus_target:
            # Fixed first representative, including the root's identity word.
            self.add_collision(program, self.minus_target[state])
        else:
            self.minus_target[state] = program

    def summary(self, status):
        emit("STREAM", status=status, descriptor_offers=self.descriptors_processed,
             unique_direct_programs_started=self.unique_processed,
             direct_pass_complete=self.direct_complete,
             minus_images=[len(self.minus_source), len(self.minus_target)],
             bridges=len(self.bridges), collision_directions=len(self.collisions),
             plus_images=[len(self.plus_source), len(self.plus_target)],
             collision_target_images_completed=len(self.target_done),
             collision_images_completed_per_root=self.root_done,
             walks=self.walk_steps, overlong_meetings=self.overlong,
             logical_contacts=self.budget.used, program_nodes=len(self.e.nodes),
             collision_family_complete_stabilizer=False)


def inverse_closed(engine, programs):
    result, seen = [], set()
    for program in programs:
        for direction in (program, engine.inverse(program)):
            if direction and direction not in seen:
                seen.add(direction)
                result.append(direction)
    return tuple(result)


def walk(stream, programs, kind):
    engine, budget = stream.e, stream.budget
    budget.phase = "FALLBACK_" + kind.upper()
    bank = inverse_closed(engine, programs)
    if not bank:
        return
    rng = Rng(SEED_B if kind == "minus" else SEED_C)
    current = [None, None]
    for step in range(WALK_STEPS):
        for side in (0, 1):
            if step % WALK_DEPTH == 0:
                root = ((step // WALK_DEPTH) % len(stream.roots)) if kind == "plus" and side == 0 else 0
                if kind == "minus":
                    state = stream.rminus if side == 0 else stream.goals[0]
                else:
                    state = stream.roots[root] if side == 0 else stream.goals[2]
                current[side] = (state, 0, None, root)
            state, path, last, root = current[side]
            index = rng.next() % len(bank)
            if last is not None and bank[index] == engine.inverse(last):
                index = (index + 1) % len(bank)
            program = bank[index]
            after = engine.do(state, program, budget)
            path = engine.join(path, program)
            current[side] = (after, path, program, root)
            stream.walk_steps[kind][side] += 1
            if kind == "minus":
                if side == 0:
                    stream.minus_source_image(after, path)
                else:
                    stream.minus_target_image(after, path)
                if stream.roots:
                    return  # Continue on the final input with an actual bridge.
            elif side == 0:
                stream.plus_source_image(after, root, path)
            else:
                stream.plus_target_image(after, path)


def audit_success(stream, found, helpers):
    engine = stream.e
    b = stream.bridges[found.root]
    c = found.continuation
    # All following checks are reserved final certificate audits, not search.
    assert engine.apply(stream.rminus, b) == stream.goals[0]
    assert engine.apply(stream.goals[1], b) == stream.goals[1]
    assert engine.apply(stream.roots[found.root], c) == stream.goals[2]
    assert engine.apply(stream.goals[0], c) == stream.goals[0]
    assert engine.apply(stream.goals[1], c) == stream.goals[1]
    assert all(engine.apply(state, c) == state for state in stream.odd)
    full = engine.join(engine.join(engine.join(stream.base, stream.a), b), c)
    word_ids = engine.expand(full)
    assert len(word_ids) <= FINAL_WORD_CAP
    emit("COMMON_WORD", contacts=len(word_ids), word=format_word(word_ids),
         native_word_sha256=word_hash([word_ids]),
         bridge_lengths=[engine.costs[stream.a], engine.costs[b], engine.costs[c]],
         shortest_claim=False)
    pairs = tuple(EDGES[e] for e in word_ids)
    for t in range(-2, 3):
        endpoint, branches, changed = replay(initial(t, helpers), pairs)
        assert endpoint == target(t, helpers)
        emit("COMMON_WORD_INPUT", t=t, endpoint=endpoint, target_verified=True,
             helpers_returned=True, changed_steps=changed,
             admission_sha256=sha256(branches.encode("ascii")).hexdigest(),
             inverse_contacts=4 * len(word_ids), inverse_recovery=True)


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    emit("PROBE", name="P-POLE-HEIGHT-FULL-SCHREIER-1", arithmetic="EXACT_INTEGER",
         zero_cap=ZERO_CAP, zero_path_cap=ZERO_PATH_CAP, bridge_roots=BRIDGE_ROOTS,
         work_budget=WORK_BUDGET, final_word_cap=FINAL_WORD_CAP,
         fallback_steps_per_side=WALK_STEPS, fallback_restart_depth=WALK_DEPTH)
    engine = Engine()
    bank, odd, source, goal, base, helpers = load_fixture(engine)
    budget = Budget()
    stream = None
    status, verified = "INCONCLUSIVE", False
    try:
        zero = build_zero(engine, budget, bank, goal[1], source[1])
        if zero is None:
            status = "NO_WORD_IN_K0_ZERO_OBSTRUCTION"
        else:
            a, descriptors = zero
            audit_zero_prefix(engine, base, a, helpers)
            budget.phase = "AFTER_ZERO"
            rminus = engine.do(source[0], a, budget)
            rplus = engine.do(source[2], a, budget)
            stream = Stream(engine, budget, odd, goal, rminus, rplus, base, a)
            stream.initialize()
            budget.phase = "DIRECT_FULL_FAMILY"
            unique = []
            seen = {0}
            for program in descriptors:
                stream.descriptors_processed += 1
                if program in seen:
                    continue
                seen.add(program)
                unique.append(program)
                stream.unique_processed += 1
                image = engine.do(rminus, program, budget)
                stream.minus_source_image(image, program)
                image = engine.do(goal[0], program, budget)
                stream.minus_target_image(image, program)
            stream.direct_complete = True
            stream.summary("DIRECT_PASS_COMPLETE")
            if not stream.roots:
                walk(stream, unique, "minus")
            if stream.roots and stream.collisions:
                walk(stream, tuple(stream.collisions), "plus")
            status = "INCONCLUSIVE_COMPLETED_DECLARED_SEARCH"
    except Found as found:
        assert stream is not None
        audit_success(stream, found, helpers)
        status, verified = "FOUND", True
    except WorkLimit as exc:
        status = "INCONCLUSIVE_" + str(exc)
    if stream is not None:
        stream.summary(status)
    emit("RESULT", status=status, common_five_verified=verified,
         logical_search_contacts=budget.used, final_audit_budget="RESERVED_SEPARATELY",
         selected_family_length_cut=False, selected_family_fingerprint_cut=False,
         canon_promotion=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
