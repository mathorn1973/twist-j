#!/usr/bin/env python3
"""Frozen, finite exact-integer audit. Not evidence for an all-L theorem.

Author: A. M. Thorn <thorn@twistj.com>
PUBLIC / NON-CANONICAL. Candidate-T ceiling applies to the accompanying
written proof; this finite audit neither promotes it nor estimates mixing.
Run only after the source and prospective specification have been pinned.
"""

from collections import deque
from itertools import product
import json


SIZES = (4, 6, 8, 10)
SOURCES = (1, 2)
COEFFICIENTS = (1, 2, 3, 4)
HEIGHT_GRAPHS = (
    ("edge2", 2, ((0, 1),)),
    ("path3", 3, ((0, 1), (1, 2))),
    ("cycle4", 4, ((0, 1), (1, 2), (2, 3), (3, 0))),
    ("star5", 5, ((0, 1), (0, 2), (0, 3), (0, 4))),
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def rep(value):
    return (value + 2) % 5 - 2


def local_wrap_audit():
    cases = 0
    downward_pairs = 0
    upward_pairs = 0
    for a, b, delta in product(range(5), repeat=3):
        aa, bb = (a + delta) % 5, (b - delta) % 5
        difference = aa + bb - a - b
        require(difference in (-5, 0, 5), "pair wrap exceeds one unit")
        require(aa - 2 == rep(a - 2 + delta), "head representative")
        require(bb - 2 == rep(b - 2 - delta), "tail representative")
        cases += 1
    for a, b in product(range(5), repeat=2):
        total = a + b
        if total >= 5:
            delta = (total - 5 - a) % 5
            aa, bb = (a + delta) % 5, (b - delta) % 5
            require((aa, bb) == (total - 5, 0), "downward pair move")
            require(aa + bb == total - 5, "downward total")
            downward_pairs += 1
        if total <= 3:
            delta = (4 - a) % 5
            aa, bb = (a + delta) % 5, (b - delta) % 5
            require((aa, bb) == (4, total + 1), "upward pair move")
            require(aa + bb == total + 5, "upward total")
            upward_pairs += 1
    return {"triples": cases, "downward_pairs": downward_pairs,
            "upward_pairs": upward_pairs}


def fixed_total_audit():
    result = []
    for name, order, edges in HEIGHT_GRAPHS:
        by_total = {}
        for state in product(range(5), repeat=order):
            by_total.setdefault(sum(state), set()).add(state)
        visited_total = 0
        traversed = 0
        for total, all_states in sorted(by_total.items()):
            first = min(all_states)
            visited = {first}
            queue = deque([first])
            while queue:
                state = queue.popleft()
                for u, v in edges:
                    for donor, receiver in ((u, v), (v, u)):
                        if state[donor] == 0 or state[receiver] == 4:
                            continue
                        updated = list(state)
                        updated[donor] -= 1
                        updated[receiver] += 1
                        target = tuple(updated)
                        require(sum(target) == total, "nonwrapping total")
                        require(target in all_states, "bounded transfer")
                        traversed += 1
                        if target not in visited:
                            visited.add(target)
                            queue.append(target)
            require(visited == all_states, "fixed-total disconnection: " + name)
            visited_total += len(visited)
        require(visited_total == 5 ** order, "height domain incomplete")
        result.append({"graph": name, "states": visited_total,
                       "totals": len(by_total), "directed_moves": traversed})
    return result


class Torus:
    """Actual 01-plaquette curl and its oriented periodic dual incidence.

    Site index is x0 + L*x1. Primal edge index is 2*site + mu.
    curl(x) = a0(x) + a1(x+e0) - a0(x+e1) - a1(x), modulo five.
    Each dual edge goes from the plaquette with coefficient -1 to +1.
    """

    def __init__(self, size):
        self.size = size
        self.order = size * size
        self.edges = []
        self.adj = [[] for _ in range(self.order)]
        for vertex in range(self.order):
            x, y = vertex % size, vertex // size
            candidates = (
                (self.index(x, y - 1), vertex, (0, 1)),
                (vertex, self.index(x - 1, y), (-1, 0)),
            )
            for tail, head, step in candidates:
                edge = len(self.edges)
                self.edges.append((tail, head, step))
                self.adj[tail].append((head, edge, 1))
                self.adj[head].append((tail, edge, -1))
        self.parent = [None] * self.order
        self.parent_edge = [None] * self.order
        self.parent[0] = 0
        self.ordering = [0]
        queue = deque([0])
        while queue:
            u = queue.popleft()
            for v, edge, sign in self.adj[u]:
                if self.parent[v] is None:
                    self.parent[v] = u
                    self.parent_edge[v] = edge
                    self.ordering.append(v)
                    queue.append(v)
        require(len(self.ordering) == self.order, "dual graph disconnected")
        self.tree = set(self.parent_edge[1:])
        require(len(self.tree) == self.order - 1, "tree size")
        self.chords = tuple(e for e in range(len(self.edges)) if e not in self.tree)

    def index(self, x, y):
        return (x % self.size) + self.size * (y % self.size)

    def curl(self, links):
        answer = []
        for vertex in range(self.order):
            x, y = vertex % self.size, vertex // self.size
            right = self.index(x + 1, y)
            above = self.index(x, y + 1)
            answer.append((links[2 * vertex] + links[2 * right + 1]
                           - links[2 * above] - links[2 * vertex + 1]) % 5)
        return answer

    def incidence_audit(self):
        for edge, (tail, head, _) in enumerate(self.edges):
            links = [0] * len(self.edges)
            links[edge] = 1
            expected = [0] * self.order
            expected[tail] = 4
            expected[head] = 1
            require(self.curl(links) == expected, "curl/incidence mismatch")

    def solve(self, target, source):
        residual = list(target)
        residual[0] = (residual[0] - source) % 5
        require(sum(residual) % 5 == 0, "source compatibility")
        links = [0] * len(self.edges)
        for vertex in reversed(self.ordering[1:]):
            parent = self.parent[vertex]
            edge = self.parent_edge[vertex]
            tail, head, _ = self.edges[edge]
            sign = 1 if head == vertex else -1
            require(vertex in (tail, head) and parent in (tail, head), "tree incidence")
            amount = residual[vertex] % 5
            links[edge] = (sign * amount) % 5
            residual[parent] = (residual[parent] + amount) % 5
        require(residual[0] % 5 == 0, "tree root residual")
        require(self.effective(links, source) == target, "tree lift source curl")
        return links

    def effective(self, links, source):
        flux = self.curl(links)
        flux[0] = (flux[0] + source) % 5
        return flux

    def cycle(self, chord):
        tail, head, _ = self.edges[chord]
        # The chord tail -> head, followed by the unique tree path head -> tail.
        previous = {head: None}
        queue = deque([head])
        while tail not in previous:
            require(bool(queue), "tree path absent")
            u = queue.popleft()
            for v, edge, sign in self.adj[u]:
                if edge in self.tree and v not in previous:
                    previous[v] = (u, edge, sign)
                    queue.append(v)
        path = []
        vertex = tail
        while vertex != head:
            prior, edge, sign = previous[vertex]
            path.append((edge, sign))
            vertex = prior
        path.reverse()
        result = [(chord, 1)] + path
        require(len({e for e, _ in result}) == len(result), "cycle repeats edge")
        require([e for e, _ in result if e not in self.tree] == [chord], "chord basis")
        current = tail
        vertices = {tail}
        dx = dy = 0
        for position, (edge, sign) in enumerate(result):
            a, b, step = self.edges[edge]
            start, finish = (a, b) if sign == 1 else (b, a)
            require(start == current, "cycle ordering")
            current = finish
            dx += sign * step[0]
            dy += sign * step[1]
            if position < len(result) - 1:
                require(current not in vertices, "cycle not simple")
                vertices.add(current)
        require(current == tail, "cycle not closed")
        require(dx % self.size == 0 and dy % self.size == 0, "cycle winding")
        return result, (dx // self.size, dy // self.size)


def extrema(order, source, sector):
    if sector == "minus":
        heights = [0] * order
        heights[0] = (2 * order + source) % 5
        winding = -((2 * order + source) // 5)
        require(winding <= -6, "minus slack")
    else:
        heights = [4] * order
        heights[0] -= (2 * order - source) % 5
        winding = (2 * order - source) // 5
        require(winding >= 6, "zero slack")
    flux = [(height - 2) % 5 for height in heights]
    require(sum(rep(f) for f in flux) == source + 5 * winding, "extreme winding")
    return flux, winding


def grid_audit():
    rows = []
    for size in SIZES:
        torus = Torus(size)
        torus.incidence_audit()
        cycles = [torus.cycle(chord) for chord in torus.chords]
        require(len(cycles) == torus.order + 1, "cycle-space dimension")
        windings = [winding for _, winding in cycles]
        require(any(a * d - b * c in (-1, 1)
                    for a, b in windings for c, d in windings),
                "noncontractible cycles do not span the torus")
        intermediates = 0
        completed = 0
        for source in SOURCES:
            for sector in ("minus", "zero"):
                target, extreme_w = extrema(torus.order, source, sector)
                base = torus.solve(target, source)
                for n in (1, torus.order):
                    # The other n-1 twisted slices remain at this same extreme.
                    for cycle, _ in cycles:
                        for coefficient in COEFFICIENTS:
                            links = list(base)
                            start = torus.edges[cycle[0][0]][0]
                            endpoint = start
                            for position, (edge, sign) in enumerate(cycle):
                                links[edge] = (links[edge] + sign * coefficient) % 5
                                tail, head, _ = torus.edges[edge]
                                endpoint = head if sign == 1 else tail
                                expected = list(target)
                                expected[start] = (expected[start] - coefficient) % 5
                                expected[endpoint] = (expected[endpoint] + coefficient) % 5
                                flux = torus.effective(links, source)
                                require(flux == expected, "intermediate endpoint flux")
                                numerator = sum(rep(f) for f in flux) - source
                                require(numerator % 5 == 0, "noninteger slice winding")
                                winding = numerator // 5
                                require(abs(winding - extreme_w) <= 1, "cycle slack exceeded")
                                total_w = (n - 1) * extreme_w + winding
                                allowed = 2 * total_w < -n if sector == "minus" else 2 * total_w >= -n
                                require(allowed, "intermediate exits frozen sector")
                                intermediates += 1
                            require(torus.effective(links, source) == target, "cycle fails to restore curl")
                            expected_links = list(base)
                            for edge, sign in cycle:
                                expected_links[edge] = (expected_links[edge] + sign * coefficient) % 5
                            require(links == expected_links and links != base, "nontrivial link-cycle lift")
                            completed += 1
        rows.append({"L": size, "plaquettes": torus.order,
                     "primal_links": len(torus.edges),
                     "fundamental_cycles": len(cycles),
                     "noncontractible_cycles": sum(w != (0, 0) for w in windings),
                     "completed_cycle_paths": completed,
                     "checked_intermediates": intermediates})
    return rows


def main():
    report = {"item": "C-PHOTON-RESTRICTED-REACHABILITY-N",
              "scope": "FINITE_INTEGER_AUDIT_ONLY",
              "local_wrap": local_wrap_audit(),
              "fixed_total": fixed_total_audit(),
              "periodic_grid": grid_audit(),
              "result": "PASS"}
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
