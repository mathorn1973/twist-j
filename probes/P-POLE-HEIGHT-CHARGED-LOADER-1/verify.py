"""Bounded exact search. Do not execute before the public preregistration pin."""
from collections import OrderedDict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product

BIAS = 32
COEFFICIENT_BOUND = 10
WIDTH = 2000
LAYERS = 20
VISITED_LIMIT = 20000
PAIR_CACHE_LIMIT = 200000
EXPANSION_LIMIT = 4800000
TS = (-2, -1, 0, 1, 2)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ROOT = (0, 1, 0, 0)
P = (0, 0, 1, 0)
U = (1, -1, 0, 0)
B = (1, 0, -1, 0)
EDGES = tuple(combinations(range(6), 2))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(n, x):
    return tuple(n * a for a in x)


def mul(x, y):
    out = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i + j] += a * b
    for degree in range(6, 3, -1):
        leading = out[degree]
        for offset in range(1, 5):
            out[degree - offset] -= leading
        out[degree] = 0
    return tuple(out[:4])


def power(x, n):
    out = ONE
    for _ in range(n):
        out = mul(out, x)
    return out


def conjugate(x):
    out = ZERO
    for i, a in enumerate(x):
        out = add(out, scale(a, power(ROOT, (-i) % 5)))
    return out


def hermitian(x):
    return mul(x, conjugate(x))


def q(x):
    a, b, c, d = x
    numerator = 5 * (a*a + b*b + c*c + d*d) - (a+b+c+d)**2
    assert numerator % 2 == 0
    return numerator // 2


def admitted(pair):
    return all((a - b) % 2 == 0 for a, b in zip(*pair))


def elementary(pair):
    x, y = pair
    if not admitted(pair):
        return pair
    sums = add(x, y)
    differences = sub(x, y)
    assert all(a % 2 == 0 for a in sums + differences)
    center = tuple(a // 2 for a in sums)
    half_difference = tuple(a // 2 for a in differences)
    rotated = mul(P, half_difference)
    return add(center, rotated), sub(center, rotated)


def repeated_pair(pair, count):
    for _ in range(count):
        pair = elementary(pair)
    return pair


def encode(cases):
    values = [a for case in cases for slot in case for a in slot]
    assert len(values) == 120
    assert all(abs(a) <= COEFFICIENT_BOUND for a in values)
    return bytes(a + BIAS for a in values)


def decode(state):
    assert len(state) == 120
    values = tuple(a - BIAS for a in state)
    return tuple(
        tuple(tuple(values[24*t + 4*i:24*t + 4*i + 4]) for i in range(6))
        for t in range(5)
    )


def pack_pair(pair):
    return bytes(a + BIAS for slot in pair for a in slot)


def unpack_pair(data):
    return tuple(tuple(a - BIAS for a in data[4*i:4*i+4]) for i in range(2))


@lru_cache(maxsize=PAIR_CACHE_LIMIT)
def pair_variants(data):
    """Four exact powers, computed by integer multiplication by j squared."""
    x, y = unpack_pair(data)
    if x == y or not admitted((x, y)):
        return None
    center = tuple((a + b) // 2 for a, b in zip(x, y))
    d = tuple((a - b) // 2 for a, b in zip(x, y))
    result = []
    old_q = q(x) + q(y)
    for _ in range(4):
        a, b, c, e = d
        d = (-c + e, -c, a - c, b - c)
        left, right = add(center, d), sub(center, d)
        assert all(abs(a) <= COEFFICIENT_BOUND for a in left + right)
        assert q(left) + q(right) == old_q
        result.append(pack_pair((left, right)))
    return tuple(result)


def error_slot(state, target, offset):
    return q(tuple(state[offset+i] - target[offset+i] for i in range(4)))


def scores(state, reference, forward):
    data = helpers = 0
    for t in range(5):
        for slot in range(6):
            value = error_slot(state, reference, 24*t + 4*slot)
            if slot < 4:
                data += value
            else:
                helpers += value
    return (data, helpers) if forward else (data + helpers, 0)


def prepared_cases(family="B"):
    base = B if family == "B" else sub(ROOT, power(ROOT, 3))
    return tuple(
        (scale(t, base), scale(-t, base), U, U, ZERO, scale(2, ONE))
        for t in TS
    )


def targets(family="B"):
    base = B if family == "B" else sub(ROOT, power(ROOT, 3))
    return tuple(
        (add(U, scale(t, base)), sub(U, scale(t, base)), ZERO, ZERO)
        for t in TS
    )


def helper_phases():
    return tuple((sub(ONE, power(P, k)), add(ONE, power(P, k))) for k in range(5))


def is_goal(state, target):
    return all(state[24*t:24*t+16] == target[24*t:24*t+16] for t in range(5))


def invert_word(word):
    return tuple(4*(action // 4) + 3 - action % 4 for action in reversed(word))


def normalized_word(word):
    out = []
    for action in word:
        edge, exponent = action // 4, action % 4 + 1
        if out and out[-1] // 4 == edge:
            exponent = (out.pop() % 4 + 1 + exponent) % 5
        if exponent:
            out.append(4*edge + exponent - 1)
    return tuple(out)


def node(state, word, reference, forward):
    first, second = scores(state, reference, forward)
    return ((first, second, state, word), state, word)


class BoundedBeam:
    """Indexed maximum heap: at most WIDTH distinct states, no stale entries."""
    def __init__(self):
        self.heap = []
        self.positions = {}

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.positions[self.heap[i][1]] = i
        self.positions[self.heap[j][1]] = j

    def up(self, i):
        while i:
            parent = (i - 1) // 2
            if self.heap[parent][0] >= self.heap[i][0]:
                break
            self.swap(parent, i)
            i = parent

    def down(self, i):
        size = len(self.heap)
        while 2*i + 1 < size:
            child = 2*i + 1
            if child + 1 < size and self.heap[child+1][0] > self.heap[child][0]:
                child += 1
            if self.heap[i][0] >= self.heap[child][0]:
                break
            self.swap(i, child)
            i = child

    def offer(self, item):
        state = item[1]
        if state in self.positions:
            i = self.positions[state]
            if item[0] >= self.heap[i][0]:
                return
            self.heap[i] = item
            self.down(i)
            return
        if len(self.heap) < WIDTH:
            self.positions[state] = len(self.heap)
            self.heap.append(item)
            self.up(len(self.heap)-1)
        elif item[0] < self.heap[0][0]:
            del self.positions[self.heap[0][1]]
            self.heap[0] = item
            self.positions[state] = 0
            self.down(0)
        assert len(self.heap) == len(self.positions) <= WIDTH

    def ordered(self):
        return sorted(self.heap, key=lambda item: item[0])


def remember(visited, frontier):
    for _, state, word in frontier:
        if state not in visited:
            visited[state] = word
            if len(visited) > VISITED_LIMIT:
                visited.popitem(last=False)
    assert len(visited) <= VISITED_LIMIT


def frontier_digest(frontier):
    digest = sha256()
    for rank, state, word in frontier:
        digest.update(rank[0].to_bytes(4, "big"))
        digest.update(rank[1].to_bytes(4, "big"))
        digest.update(state)
        digest.update(bytes((len(word),)))
        digest.update(bytes(word))
    return digest.hexdigest()


def weights_for(reference):
    result = []
    for i, j in EDGES:
        edge_weights = []
        for t in range(5):
            oi, oj = 24*t+4*i, 24*t+4*j
            difference = [reference[oi+k]-reference[oj+k] for k in range(4)]
            total = sum(difference)
            edge_weights.append(tuple(5*a-total for a in difference))
        result.append(tuple(edge_weights))
    return tuple(result)


def expand(frontier, visited, opposite, forward, depth, initial, goal,
           reference, weights, counter):
    beam = BoundedBeam()
    parents = attempts = nonidentity = 0
    for rank, state, word in frontier:
        parents += 1
        last_edge = word[-1] // 4 if word else -1
        for edge, (i, j) in enumerate(EDGES):
            if edge == last_edge:
                continue
            pairs = []
            variants = []
            for t in range(5):
                oi, oj = 24*t+4*i, 24*t+4*j
                pair = state[oi:oi+4] + state[oj:oj+4]
                pairs.append(pair)
                variants.append(pair_variants(pair))
            attempts += 4
            counter[0] += 4
            assert counter[0] <= EXPANSION_LIMIT
            if all(value is None for value in variants):
                continue
            old_data_error = 0
            if forward and i < 4 <= j:
                old_data_error = sum(
                    error_slot(state, reference, 24*t+4*i) for t in range(5)
                )
            for exponent in range(1, 5):
                out = bytearray(state)
                total_delta = new_data_error = 0
                for t in range(5):
                    updated = variants[t][exponent-1] if variants[t] is not None else pairs[t]
                    oi, oj = 24*t+4*i, 24*t+4*j
                    out[oi:oi+4] = updated[:4]
                    out[oj:oj+4] = updated[4:]
                    total_delta -= sum(
                        (updated[k]-pairs[t][k])*weights[edge][t][k] for k in range(4)
                    )
                    if forward and i < 4 <= j:
                        new_data_error += q(tuple(
                            updated[k]-reference[oi+k] for k in range(4)
                        ))
                successor = bytes(out)
                assert successor != state
                nonidentity += 1
                next_word = word + (4*edge + exponent-1,)
                # Check endpoints and the other retained history before any pruning.
                if forward and is_goal(successor, goal):
                    return normalized_word(next_word), None, (parents, attempts, nonidentity)
                if not forward and successor == initial:
                    return normalized_word(invert_word(next_word)), None, (parents, attempts, nonidentity)
                if successor in opposite:
                    if forward:
                        found = next_word + invert_word(opposite[successor])
                    else:
                        found = opposite[successor] + invert_word(next_word)
                    found = normalized_word(found)
                    assert len(found) <= 2*LAYERS
                    return found, None, (parents, attempts, nonidentity)
                if successor in visited:
                    continue
                if not forward:
                    primary, secondary = rank[0] + total_delta, 0
                elif j < 4:
                    primary, secondary = rank[0] + total_delta, rank[1]
                elif i >= 4:
                    primary, secondary = rank[0], rank[1] + total_delta
                else:
                    delta = new_data_error - old_data_error
                    primary, secondary = rank[0] + delta, rank[1] + total_delta - delta
                assert 0 <= primary and 0 <= secondary and primary + secondary <= 760
                key = (primary, secondary, successor, next_word)
                beam.offer((key, successor, next_word))
    selected = beam.ordered()
    for rank, state, word in selected:
        assert scores(state, reference, forward) == rank[:2]
        assert len(word) == depth
    remember(visited, selected)
    return None, selected, (parents, attempts, nonidentity)


def search(initial, goal, phases):
    forward_reference = goal
    forward = [node(initial, (), forward_reference, True)]
    reverse = []
    root_manifest = sha256()
    for phase_tuple in product(range(5), repeat=5):
        cases = tuple(targets()[t] + phases[k] for t, k in enumerate(phase_tuple))
        state = encode(cases)
        root_manifest.update(bytes(phase_tuple))
        root_manifest.update(state)
        reverse.append(node(state, (), initial, False))
    assert len(reverse) == 3125
    # The initial reverse expansion follows lexicographic phase order.
    f_seen, r_seen = OrderedDict(), OrderedDict()
    remember(f_seen, forward)
    remember(r_seen, reverse)
    f_weights, r_weights = weights_for(forward_reference), weights_for(initial)
    print("ROOTS forward=1 reverse=3125 sha256=" + root_manifest.hexdigest())
    counter = [0]
    for depth in range(1, LAYERS+1):
        for direction in ("F", "R"):
            is_forward = direction == "F"
            frontier = forward if is_forward else reverse
            visited = f_seen if is_forward else r_seen
            opposite = r_seen if is_forward else f_seen
            reference = forward_reference if is_forward else initial
            weights = f_weights if is_forward else r_weights
            found, selected, stats = expand(
                frontier, visited, opposite, is_forward, depth, initial, goal,
                reference, weights, counter
            )
            if found is not None:
                print("LAYER %s %d parents=%d attempts=%d nonidentity=%d MEET" %
                      ((direction, depth) + stats))
                return found, counter[0]
            print("LAYER %s %d parents=%d attempts=%d nonidentity=%d retained=%d visited=%d sha256=%s" %
                  ((direction, depth) + stats + (len(selected), len(visited), frontier_digest(selected))))
            if is_forward:
                forward = selected
            else:
                reverse = selected
    assert counter[0] <= 4443560
    return None, counter[0]


def totals(case):
    total_sum = total_h = ZERO
    total_q = 0
    for value in case:
        total_sum = add(total_sum, value)
        total_h = add(total_h, hermitian(value))
        total_q += q(value)
    return total_sum, total_h, total_q


def residues(case):
    return tuple(sum(value) % 5 for value in case)


def pair_audit(before, after):
    assert elementary(before) == after
    assert add(*before) == add(*after)
    assert add(hermitian(before[0]), hermitian(before[1])) == add(
        hermitian(after[0]), hermitian(after[1])
    )
    assert q(before[0])+q(before[1]) == q(after[0])+q(after[1])
    assert residues(before) == residues(after)
    assert repeated_pair(before, 5) == before
    assert repeated_pair(after, 4) == before
    assert elementary(repeated_pair(before, 4)) == before


def raw_step(case, edge, inverse=False):
    i, j = EDGES[edge]
    before = (case[i], case[j])
    after = before
    for _ in range(4 if inverse else 1):
        following = elementary(after)
        pair_audit(after, following)
        after = following
    if inverse:
        assert elementary(after) == before
    out = list(case)
    out[i], out[j] = after
    out = tuple(out)
    assert totals(out) == totals(case)
    assert residues(out) == residues(case)
    return out


def expanded_edges(word):
    return tuple(edge for action in word
                 for edge in [action // 4]*(action % 4+1))


def replay(case, word):
    history = [case]
    pattern = []
    charged_counts = [0]*5
    for edge in expanded_edges(word):
        i, j = EDGES[edge]
        accepted = admitted((case[i], case[j]))
        pattern.append("1" if accepted else "0")
        if j == 5 and accepted:
            charged_counts[i] += 1
        case = raw_step(case, edge)
        history.append(case)
    return history, "".join(pattern), tuple(charged_counts)


def undo(final, edges):
    state = final
    for edge in reversed(edges):
        state = raw_step(state, edge, inverse=True)
    return state


def fast_apply(state, word):
    for action in word:
        i, j = EDGES[action // 4]
        out = bytearray(state)
        for t in range(5):
            oi, oj = 24*t+4*i, 24*t+4*j
            data = state[oi:oi+4]+state[oj:oj+4]
            variants = pair_variants(data)
            updated = data if variants is None else variants[action % 4]
            out[oi:oi+4], out[oj:oj+4] = updated[:4], updated[4:]
        state = bytes(out)
    return state


def interaction(case):
    return q(sub(case[1], case[2]))


def controls():
    assert power(ROOT, 5) == ONE
    assert power(P, 3) == ROOT
    assert q(U) == q(B) == 5 and q(scale(2, ONE)) == 8
    phases = helper_phases()
    assert len(set(phases)) == 5
    for left, right in phases:
        assert add(left, right) == scale(2, ONE)
        assert q(left)+q(right) == 8
        assert residues((left, right)) == (0, 2)
    source = prepared_cases()
    goal = tuple(targets()[i]+phases[0] for i in range(5))
    for t, case, target in zip(TS, source, goal):
        assert totals(case) == totals(target)
        assert totals(case)[2] == 10*t*t + 18 <= 58
        assert residues(case) == residues(target) == (0, 0, 0, 0, 0, 2)
        assert interaction(case) == 5+5*t*t+5*t
        assert interaction(target) == 5+5*t*t-5*t
        for i, j in EDGES:
            pair = (case[i], case[j])
            variants = pair_variants(pack_pair(pair))
            for exponent in range(1, 5):
                expected = repeated_pair(pair, exponent)
                actual = pair if variants is None else unpack_pair(variants[exponent-1])
                assert actual == expected
                assert repeated_pair(expected, 5-exponent) == pair
    # Exposed known-reference control; no unknown input is claimed here.
    catalyst = (ZERO, U, scale(2, ONE), ZERO, ZERO, ZERO)
    edge13, edge23 = EDGES.index((0, 2)), EDGES.index((1, 2))
    control_word = (4*edge13+2, 4*edge23+1)
    history, _, _ = replay(catalyst, control_word)
    assert history[-1] == (U, ZERO, scale(2, ONE), ZERO, ZERO, ZERO)
    assert undo(history[-1], expanded_edges(control_word)) == catalyst
    assert totals(catalyst)[2] == 13
    assert invert_word((0, 1, 2, 3)) == (0, 1, 2, 3)
    assert normalized_word((0, 3)) == ()
    return encode(source), encode(goal), phases


def audit_found(word, initial, goal, phases):
    assert 0 < len(word) <= 40
    edges = expanded_edges(word)
    histories, patterns, endpoints = [], [], []
    fast_final = fast_apply(initial, word)
    assert is_goal(fast_final, goal)
    for t, case, fast_case in zip(TS, prepared_cases(), decode(fast_final)):
        history, pattern, counts = replay(case, word)
        final = history[-1]
        assert final == fast_case
        assert final[:4] == targets()[TS.index(t)]
        phase = phases.index(final[4:])
        assert undo(final, edges) == case
        if t % 2:
            assert tuple(value % 5 for value in counts[:4]) == (3, 3, 2, 2)
            assert counts[4] % 5 == phase
            lower = 15 if phase == 0 else 10+phase
            assert len(edges) >= sum(counts) >= lower
        histories.append(history)
        patterns.append(pattern)
        endpoints.append(phase)
    assert len(set(patterns)) >= 2
    # A_t=jB_t: fixed pre/post wrapper, independently replayed and reversed.
    edge12 = EDGES.index((0, 1))
    a_word = (4*edge12+1,) + word + (4*edge12+2,)
    for index, case in enumerate(prepared_cases("A")):
        history, _, _ = replay(case, a_word)
        assert history[-1][:4] == targets("A")[index]
        assert history[-1][4:] == phases[endpoints[index]]
        assert undo(history[-1], expanded_edges(a_word)) == case
    stock = max(
        [0] + [interaction(case)-interaction(history[0])
               for history in histories for case in history]
    )
    assert 20 <= stock <= 101
    bank_rows = []
    for t, history, phase in zip(TS, histories, endpoints):
        initial_i = interaction(history[0])
        initial_total = totals(history[0])[2] + initial_i + stock + 10
        loader_bank, reader_bank = stock, 10
        for before, after in zip(history, history[1:]):
            loader_bank += interaction(before)-interaction(after)
            assert loader_bank >= 0 and reader_bank == 10
            assert totals(after)[2]+interaction(after)+loader_bank+reader_bank == initial_total
        loaded = history[-1]
        assert loader_bank == stock+10*t
        read_state = raw_step(loaded, edge12)
        reader_bank += interaction(loaded)-interaction(read_state)
        assert reader_bank == 10-5*t >= 0
        assert totals(read_state)[2]+interaction(read_state)+loader_bank+reader_bank == initial_total
        bank_rows.append((t, phase, loader_bank, reader_bank))
        # Funded inverse-contact boundaries; C^4 separately verifies the site map.
        restored = raw_step(read_state, edge12, inverse=True)
        reader_bank += interaction(read_state)-interaction(restored)
        assert restored == loaded and reader_bank == 10
        state = restored
        for edge, previous in zip(reversed(edges), reversed(history[:-1])):
            predecessor = raw_step(state, edge, inverse=True)
            loader_bank += interaction(state)-interaction(predecessor)
            assert predecessor == previous and loader_bank >= 0
            assert totals(predecessor)[2]+interaction(predecessor)+loader_bank+reader_bank == initial_total
            state = predecessor
        assert state == history[0] and (loader_bank, reader_bank) == (stock, 10)
    print("WORD " + " ".join("%d-%d^%d" %
          (EDGES[a//4][0]+1, EDGES[a//4][1]+1, a%4+1) for a in word))
    print("LENGTH macros=%d elementary=%d A_wrapper_elementary=%d" %
          (len(word), len(edges), len(edges)+5))
    print("FUNDING B_load=%d reader_initial=10 inverse_contact_boundaries" % stock)
    for row, pattern in zip(bank_rows, patterns):
        t, phase, loader_bank, reader_bank = row
        helpers = phases[phase]
        print("B t=%d phase_p=%d loader_bank=%d reader_bank=%d helpers=%s pattern=%s" %
              (t, phase, loader_bank, reader_bank, repr(helpers), pattern))
    print("AUDIT B=5 A_wrapped=5 inverse=10 distinct_branch_patterns=%d" % len(set(patterns)))


def main():
    initial, goal, phases = controls()
    print("P-POLE-HEIGHT-CHARGED-LOADER-1")
    print("CONTROLS PASS pair_powers=300 known_catalyst=1")
    print("SEARCH width=2000 layers_per_direction=20 visited_per_direction=20000 cache=200000")
    word, attempts = search(initial, goal, phases)
    assert attempts < EXPANSION_LIMIT
    if word is None:
        print("SEARCH_NOT_FOUND attempts=%d bounded_heuristic_only" % attempts)
    else:
        print("SEARCH_FOUND attempts=%d" % attempts)
        audit_found(word, initial, goal, phases)
    info = pair_variants.cache_info()
    assert info.currsize <= PAIR_CACHE_LIMIT
    print("CACHE hits=%d misses=%d size=%d" % (info.hits, info.misses, info.currsize))
    print("RESULT PASS")


if __name__ == "__main__":
    main()
