#!/usr/bin/env python3
"""Independent exact breaker, written only from PREREG.md.

Internal basis is (1,rho,rho**2,rho**3), rho=j**2.  No author verifier is
imported or read.  Scientific execution is forbidden before the public pin.
"""

import argparse
import hashlib
import json
import platform
import sys


ZERO = (0, 0, 0, 0)
TOKEN = (1, -1, 0, 0)
HELPER = (1, 1, 0, 0)
DOMAIN = (1, 3, 5, 7, 9, 11, 13, 15, 17, 23)
STARTS = (1, 3, 5, 7, 9, 11, 13, 15)
X0, Y0, A0, B0, SCRATCH0, HELP = 0, 12, 24, 30, 36, 48
SELECTORS = (45, 46, 47)
NSLOTS = 49


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def plus(a, b):
    return tuple(a[i] + b[i] for i in range(4))


def times_rho(z):
    a, b, c, d = z
    return (-d, a - d, b - d, c - d)


def primitive(a, b):
    """Literal C, independently in the rho basis."""
    delta = tuple(a[i] - b[i] for i in range(4))
    if any(x & 1 for x in delta):
        return (a, b)
    center = tuple((a[i] + b[i]) // 2 for i in range(4))
    half_delta = tuple(x // 2 for x in delta)
    rotated = times_rho(half_delta)
    return (
        tuple(center[i] + rotated[i] for i in range(4)),
        tuple(center[i] - rotated[i] for i in range(4)),
    )


def q(z):
    numerator = 5 * sum(x * x for x in z) - sum(z) ** 2
    require(numerator % 2 == 0, "Q ceased to be integral")
    return numerator // 2


def to_j_basis(z):
    """rho=j**2, rho**2=j**4, rho**3=j."""
    a, b, c, d = z
    return [a - c, d - c, b - c, -c]


def collatz(n):
    require(n > 0 and n & 1, "nonpositive or even arithmetic input")
    numerator = 3 * n + 1
    depth = 0
    while numerator % 2 == 0:
        numerator //= 2
        depth += 1
    return numerator, depth


def inverse_arithmetic(m, depth):
    numerator = (1 << depth) * m - 1
    require(depth > 0 and numerator % 3 == 0, "inadmissible inverse pair")
    n = numerator // 3
    require(n > 0 and n & 1, "inverse did not restore a positive odd")
    require(collatz(n) == (m, depth), "inverse depth was not exact")
    return n


def rails(base, width, value):
    require(0 <= value < (1 << width), "binary chart overflow")
    return tuple(base + 2 * bit + ((value >> bit) & 1) for bit in range(width))


def set_bits(state, base, width, value, token=TOKEN, zero=ZERO):
    require(0 <= value < (1 << width), "binary initialization overflow")
    for bit in range(width):
        one = (value >> bit) & 1
        state[base + 2 * bit] = zero if one else token
        state[base + 2 * bit + 1] = token if one else zero


def get_bits(state, base, width):
    result = 0
    for bit in range(width):
        pair = tuple(state[base + 2 * bit : base + 2 * bit + 2])
        require(pair in ((TOKEN, ZERO), (ZERO, TOKEN)), "dirty bit chart")
        if pair[1] == TOKEN:
            result |= 1 << bit
    return result


def initial_state(n, selector=45, old_a=0, old_b=0, buffer=0):
    state = [ZERO] * NSLOTS
    for base, width, value in ((X0, 6, n), (Y0, 6, buffer),
                               (A0, 3, old_a), (B0, 3, old_b)):
        set_bits(state, base, width, value)
    state[selector] = TOKEN
    state[HELP] = HELPER
    return state


def build_word():
    """Compile independently as a macro tape, then lower it to edges."""
    macros = []
    module_lengths = []

    def controlled_xors(controls, targets):
        # Borrow successive control tokens into freshly blank scratch slots.
        require(1 <= len(controls) <= 10, "scratch/control bound exceeded")
        borrowed = []
        previous = controls[0]
        for offset, source in enumerate(controls[1:]):
            destination = SCRATCH0 + offset
            gate = ("V", previous, source, destination)
            macros.append(gate)
            borrowed.append(gate)
            previous = destination
        for left, right in targets:
            macros.append(("V", previous, left, right))
        macros.extend(reversed(borrowed))

    def output_pairs(base, width, value):
        return [(base + 2 * bit, base + 2 * bit + 1)
                for bit in range(width) if (value >> bit) & 1]

    for selector, archive in ((45, A0), (46, B0)):
        begin = len(macros)
        for n in DOMAIN:
            m, depth = collatz(n)
            controls = (selector,) + rails(X0, 6, n)
            targets = output_pairs(Y0, 6, m) + output_pairs(archive, 3, depth)
            controlled_xors(controls, targets)
        for n in DOMAIN:
            m, depth = collatz(n)
            controls = (selector,) + rails(Y0, 6, m) + rails(archive, 3, depth)
            controlled_xors(controls, output_pairs(X0, 6, n))
        for bit in range(6):
            controlled_xors((selector, Y0 + 2 * bit + 1),
                            [(X0 + 2 * bit, X0 + 2 * bit + 1)])
            controlled_xors((selector, X0 + 2 * bit + 1),
                            [(Y0 + 2 * bit, Y0 + 2 * bit + 1)])
        module_lengths.append(len(macros) - begin)
    macros.append(("D", 46, 47))
    macros.append(("D", 45, 46))

    def d_edges(c, d):
        return ([(HELP, c)] * 3 + [(HELP, d)] * 3
                + [(HELP, c), (HELP, d), (HELP, c)])

    edges = []
    for gate in macros:
        if gate[0] == "D":
            edges.extend(d_edges(gate[1], gate[2]))
        else:
            _, g, c, d = gate
            edges.append((g, HELP))
            edges.extend(d_edges(c, d))
            edges.extend([(g, HELP)] * 4)
            edges.extend(d_edges(c, d))
    require(all(0 <= i < NSLOTS and 0 <= j < NSLOTS and i != j
                for i, j in edges), "invalid literal edge")
    return macros, tuple(edges), tuple(module_lengths)


class ExactLane:
    def __init__(self):
        self.cache = {}
        self.primitive_applications = 0

    def contact(self, state, i, j):
        key = (state[i], state[j])
        result = self.cache.get(key)
        if result is None:
            result = primitive(*key)
            require(plus(*key) == plus(*result), "primitive broke sum")
            require(q(key[0]) + q(key[1]) == q(result[0]) + q(result[1]),
                    "primitive broke Q")
            require(sum(key[0]) % 5 == sum(result[0]) % 5,
                    "primitive broke first labelled residue")
            require(sum(key[1]) % 5 == sum(result[1]) % 5,
                    "primitive broke second labelled residue")
            cycle = key
            for _ in range(5):
                cycle = primitive(*cycle)
            require(cycle == key, "primitive fifth power failed")
            inverse = result
            for _ in range(4):
                inverse = primitive(*inverse)
            require(inverse == key, "primitive exact inverse failed")
            self.cache[key] = result
        state[i], state[j] = result
        self.primitive_applications += 1

    def apply(self, state, edges):
        for i, j in edges:
            self.contact(state, i, j)

    def invert(self, state, edges):
        for i, j in reversed(edges):
            for _ in range(4):
                self.contact(state, i, j)


def audit_boundary(state):
    require(len(state) == NSLOTS, "state length changed")
    total = tuple(sum(z[i] for z in state) for i in range(4))
    require(total == plus(tuple(19 * x for x in TOKEN), HELPER), "boundary sum")
    require(sum(q(z) for z in state) == 98, "boundary Q")
    require(all(sum(z) % 5 == (2 if i == HELP else 0)
                for i, z in enumerate(state)), "boundary labelled residue")
    require(get_bits(state, Y0, 6) == 0, "buffer not blank")
    require(all(z == ZERO for z in state[SCRATCH0:45]), "scratch not blank")
    require(state[HELP] == HELPER, "helper not restored")
    selector = [i for i in SELECTORS if state[i] == TOKEN]
    require(len(selector) == 1 and all(state[i] in (ZERO, TOKEN)
                                    for i in SELECTORS), "dirty selector")
    return [get_bits(state, X0, 6), get_bits(state, A0, 3),
            get_bits(state, B0, 3), selector[0]]


def test_local_macros(lane):
    h, g, c, d = HELP, 0, 1, 2
    d_word = ([(h, c)] * 3 + [(h, d)] * 3
              + [(h, c), (h, d), (h, c)])
    v_word = [(g, h)] + d_word + [(g, h)] * 4 + d_word
    require(len(v_word) == 23 and len(d_word) == 9, "local word length")
    targets = ((ZERO, ZERO), (TOKEN, ZERO), (ZERO, TOKEN))
    rows = []
    for control in (ZERO, TOKEN):
        for left, right in targets:
            before = [ZERO] * NSLOTS
            before[g], before[h], before[c], before[d] = control, HELPER, left, right
            actual = before.copy()
            lane.apply(actual, v_word)
            expected = before.copy()
            if control == TOKEN:
                expected[c], expected[d] = right, left
            require(actual == expected, "one of six exact V rows failed")
            lane.invert(actual, v_word)
            require(actual == before, "local V native inverse failed")
            rows.append([int(control == TOKEN), int(left == TOKEN), int(right == TOKEN)])
    for left, right in targets:
        before = [ZERO] * NSLOTS
        before[h], before[c], before[d] = HELPER, left, right
        actual = before.copy()
        lane.apply(actual, d_word)
        expected = before.copy()
        expected[c], expected[d] = right, left
        require(actual == expected, "unconditional D row failed")
        lane.invert(actual, d_word)
        require(actual == before, "local D native inverse failed")
    return rows


def abstract_skip_audit(macros):
    count = 0
    for current in range(64):
        for old_a in range(8):
            for old_b in range(8):
                state = [0] * NSLOTS
                for base, width, value in ((X0, 6, current), (Y0, 6, 0),
                                           (A0, 3, old_a), (B0, 3, old_b)):
                    set_bits(state, base, width, value, token=1, zero=0)
                state[47], state[HELP] = 1, 2
                expected = state.copy()
                expected[45], expected[47] = 1, 0
                for gate in macros:
                    if gate[0] == "D":
                        c, d = gate[1:]
                        state[c], state[d] = state[d], state[c]
                    else:
                        _, g, c, d = gate
                        require(state[g] in (0, 1), "abstract control outside chart")
                        require(state[c] + state[d] <= 1,
                                "abstract target outside proved V contract")
                        if state[g]:
                            state[c], state[d] = state[d], state[c]
                require(state == expected, "abstract skip changed a nonselector slot")
                count += 1
    require(count == 4096, "abstract skip count")
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--boundaries-out", help="optional full canonical boundary JSON")
    args = parser.parse_args()
    macros, edges, module_lengths = build_word()
    edge_bytes = "".join(f"{i},{j}\n" for i, j in edges).encode("ascii")
    edge_digest = hashlib.sha256(edge_bytes).hexdigest()
    lane = ExactLane()
    v_rows = test_local_macros(lane)
    boundaries = []
    readings = []
    inverse_count = 0
    first_groups = {}

    for n in STARTS:
        initial = initial_state(n)
        state = initial.copy()
        audit_boundary(state)
        n1, depth1 = collatz(n)
        require(n in DOMAIN and n1 in DOMAIN, "active arithmetic input left D")
        n2, depth2 = collatz(n1)
        expected_rows = ([n1, depth1, 0, 46], [n2, depth1, depth2, 47],
                         [n2, depth1, depth2, 45])
        full_rows, chart_rows = [], []
        for expected in expected_rows:
            lane.apply(state, edges)
            chart = audit_boundary(state)
            require(chart == expected, "three-word trajectory boundary mismatch")
            chart_rows.append(chart)
            full_rows.append([to_j_basis(z) for z in state])
        restored = inverse_arithmetic(inverse_arithmetic(n2, depth2), depth1)
        require(restored == n, "ordered archive failed initial-input restoration")
        for _ in range(3):
            lane.invert(state, edges)
        require(state == initial, "three-word full native inverse failed")
        inverse_count += 1
        boundaries.append([n] + full_rows)
        readings.append([n] + chart_rows)
        first_groups.setdefault(n1, []).append([n, depth1])

    occupied = []
    for n in DOMAIN:
        m, depth = collatz(n)
        for old_a in range(8):
            initial = initial_state(n, selector=46, old_a=old_a)
            state = initial.copy()
            audit_boundary(state)
            lane.apply(state, edges)
            chart = audit_boundary(state)
            require(chart == [m, old_a, depth, 47], "occupied archive continuation")
            require(inverse_arithmetic(m, depth) == n, "occupied inverse arithmetic")
            lane.invert(state, edges)
            require(state == initial, "occupied full native inverse failed")
            inverse_count += 1
            occupied.append([n, old_a] + chart)
    require(len(occupied) == 80 and inverse_count == 88, "full replay case count")

    skip_count = abstract_skip_audit(macros)
    collisions = [[m, entries] for m, entries in sorted(first_groups.items())
                  if len({entry[1] for entry in entries}) > 1]
    require(collisions, "missing identical outputs with distinct depths")
    boundary_bytes = json.dumps(boundaries, separators=(",", ":")).encode("ascii")
    if args.boundaries_out:
        with open(args.boundaries_out, "wb") as handle:
            handle.write(boundary_bytes)

    result = {
        "status": "PASS",
        "scope": "NON-CANONICAL / L1 / candidate-C; independent x86_64 breaker",
        "basis": "internal rho; boundary j",
        "python": sys.version.split()[0],
        "machine": platform.machine(),
        "edge_count": len(edges),
        "edge_sha256": edge_digest,
        "edge_bytes": len(edge_bytes),
        "macro_count": len(macros),
        "module_macro_counts": list(module_lengths),
        "boundary_sha256": hashlib.sha256(boundary_bytes).hexdigest(),
        "boundary_bytes": len(boundary_bytes),
        "boundary_payload": "[[initial_n,state_after_W,state_after_W2,state_after_W3],...]",
        "v_rows": v_rows,
        "d_rows": 3,
        "three_word_cases": 8,
        "occupied_cases": len(occupied),
        "native_inverse_cases": inverse_count,
        "abstract_skip_cases": skip_count,
        "abstract_skip_scope": "proved V/D swap semantics; no primitive replay for 4096 skip cases",
        "primitive_applications": lane.primitive_applications,
        "distinct_ordered_primitive_pairs": len(lane.cache),
        "trajectory_readings": readings,
        "occupied_readings": occupied,
        "same_output_different_depth": collisions,
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
