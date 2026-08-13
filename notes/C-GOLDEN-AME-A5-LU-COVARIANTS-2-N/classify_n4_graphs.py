#!/usr/bin/env python3
"""Purely combinatorial n=4 balanced-diagram quotient.

No tensor data is read.  Fixed open leg q is normalized to color 0.
Its partial matching is id on closed vertices 1,2,3.  A diagram is then an
ordered triple of S4 permutations for the other three colors, modulo
simultaneous conjugation by S3 fixing open-copy label 0.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import argparse
from collections import Counter, defaultdict, deque
from pathlib import Path


S4 = tuple(itertools.permutations(range(4)))
S3_FIX0 = tuple((0,) + p for p in itertools.permutations((1, 2, 3)))
IDENTITY = (0, 1, 2, 3)


def inv(p):
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def conjugate(p, g):
    return compose(compose(g, p), inv(g))


def canonical(triple):
    return min(tuple(conjugate(p, g) for p in triple) for g in S3_FIX0)


def edge_multiplicities(triple):
    # color 0 is the open-leg partial identity matching on closed vertices.
    counts = Counter((r, r) for r in (1, 2, 3))
    for p in triple:
        counts.update((r, p[r]) for r in range(4))
    return counts


def double_edges(triple):
    return tuple(sorted((r, s, m) for (r, s), m in edge_multiplicities(triple).items() if m >= 2))


def one_step_double_edge_reduction(triple):
    """Pure graph rewrite induced by one 2-unitarity identity.

    It returns only structural data; no tensor coefficient is evaluated.
    """
    matchings = [{1: 1, 2: 2, 3: 3}] + [dict(enumerate(p)) for p in triple]
    open_a = [0, None, None, None]
    open_b = [0, None, None, None]
    pairs = double_edges(triple)
    if not pairs:
        return None
    r, s, multiplicity = pairs[0]
    shared_colors = tuple(c for c, matching in enumerate(matchings) if matching.get(r) == s)
    contracted = set(shared_colors[:2])
    loops = 0
    external_delta = False
    for color, matching in enumerate(matchings):
        if color in contracted:
            if matching.pop(r, None) != s:
                raise RuntimeError("contracted color is not a shared edge")
            continue

        # A remaining shared edge closes into a dimension loop after the
        # two-index unitary contraction.
        if matching.get(r) == s:
            del matching[r]
            loops += 1
            continue

        if r in matching:
            b_neighbor = matching.pop(r)
            a_side = ("edge", b_neighbor)
        else:
            if open_a[color] != r:
                raise RuntimeError("missing A incidence is not open")
            a_side = ("open", None)
            open_a[color] = None

        pred = next((u for u, v in matching.items() if v == s), None)
        if pred is not None:
            del matching[pred]
            b_side = ("edge", pred)
        else:
            if open_b[color] != s:
                raise RuntimeError("missing B incidence is not open")
            b_side = ("open", None)
            open_b[color] = None

        if a_side[0] == "edge" and b_side[0] == "edge":
            matching[b_side[1]] = a_side[1]
        elif a_side[0] == "open" and b_side[0] == "edge":
            open_a[color] = b_side[1]
        elif a_side[0] == "edge" and b_side[0] == "open":
            open_b[color] = a_side[1]
        else:
            external_delta = True

    remaining_a = tuple(x for x in range(4) if x != r)
    remaining_b = tuple(x for x in range(4) if x != s)
    for color, matching in enumerate(matchings):
        if set(mapping_value for mapping_value in matching.values()) - set(remaining_b):
            raise RuntimeError("removed B vertex remains")
        if set(matching) - set(remaining_a):
            raise RuntimeError("removed A vertex remains")
        if color == 0 and not external_delta:
            if len(matching) != 2 or open_a[color] not in remaining_a or open_b[color] not in remaining_b:
                raise RuntimeError("reduction is not an n=3 one-leg diagram")
        elif color == 0 and external_delta:
            if len(matching) != 3 or open_a[color] is not None or open_b[color] is not None:
                raise RuntimeError("external-delta remainder is not closed")
        elif len(matching) != 3:
            raise RuntimeError("non-open color is not a size-three perfect matching")
    return {
        "pair": (r, s),
        "original_multiplicity": multiplicity,
        "shared_colors": shared_colors,
        "contracted_colors": tuple(sorted(contracted)),
        "dimension_loops": loops,
        "target_type": "scalar_identity_times_closed_n3" if external_delta else "one_leg_n3",
    }


def graph_components(triple):
    # vertices A0..A3 are 0..3, B0..B3 are 4..7. Open half-edges do not join.
    adjacency = {i: set() for i in range(8)}
    for r in (1, 2, 3):
        adjacency[r].add(4 + r)
        adjacency[4 + r].add(r)
    for p in triple:
        for r in range(4):
            s = p[r]
            adjacency[r].add(4 + s)
            adjacency[4 + s].add(r)
    unseen = set(range(8))
    comps = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        comp = {root}
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in sorted(adjacency[v]):
                if w in unseen:
                    unseen.remove(w)
                    comp.add(w)
                    queue.append(w)
        comps.append(tuple(sorted(comp)))
    return tuple(comps)


def cycle_type(p):
    seen = set()
    sizes = []
    for x in range(4):
        if x in seen:
            continue
        y, n = x, 0
        while y not in seen:
            seen.add(y)
            n += 1
            y = p[y]
        sizes.append(n)
    return tuple(sorted(sizes, reverse=True))


def automorphism_order(triple):
    return sum(tuple(conjugate(p, g) for p in triple) == triple for g in S3_FIX0)


def main(output_path: Path):
    reps = {}
    labeled_irreducible = 0
    labeled_connected_irreducible = 0
    labeled_reduction_histogram = Counter()
    for triple in itertools.product(S4, repeat=3):
        key = canonical(triple)
        if key not in reps:
            reps[key] = None
        if not double_edges(triple):
            labeled_irreducible += 1
            if len(graph_components(triple)) == 1:
                labeled_connected_irreducible += 1
        else:
            reduction = one_step_double_edge_reduction(triple)
            labeled_reduction_histogram[(reduction["target_type"], reduction["original_multiplicity"], reduction["dimension_loops"])] += 1

    rows = []
    reduction_histogram = Counter()
    for rep in sorted(reps):
        doubles = double_edges(rep)
        comps = graph_components(rep)
        aut = automorphism_order(rep)
        orbit = 6 // aut
        row = {
            "permutations": rep,
            "cycle_types": [cycle_type(p) for p in rep],
            "double_edges": doubles,
            "irreducible_no_double_edge": not doubles,
            "components": comps,
            "connected": len(comps) == 1,
            "automorphism_order_in_S3": aut,
            "labeled_orbit_size": orbit,
            "star_inverse_canonical": canonical(tuple(inv(p) for p in rep)),
        }
        if doubles:
            reduction = one_step_double_edge_reduction(rep)
            row["lex_first_reduction"] = reduction
            reduction_histogram[(reduction["target_type"], reduction["original_multiplicity"], reduction["dimension_loops"])] += 1
        rows.append(row)

    hist = Counter()
    for row in rows:
        hist[(row["irreducible_no_double_edge"], row["connected"], row["automorphism_order_in_S3"])] += 1
    raw_text = "".join(
        "/".join("".join(map(str, p)) for p in row["permutations"]) + "\n"
        for row in rows
    )
    irreducible_rows = [r for r in rows if r["irreducible_no_double_edge"]]
    irreducible_text = "".join(
        "/".join("".join(map(str, p)) for p in row["permutations"]) + "\n"
        for row in irreducible_rows
    )
    connected_rows = [r for r in irreducible_rows if r["connected"]]
    if any(r["star_inverse_canonical"] != r["permutations"] for r in connected_rows):
        raise RuntimeError("an irreducible representative is not self-star in its S3 orbit")
    connected_text = "".join(
        "/".join("".join(map(str, p)) for p in row["permutations"]) + "\n"
        for row in connected_rows
    )

    burnside = (24**3 + 3 * 4**3 + 2 * 3**3) // 6
    result = {
        "model": "ordered triples S4^3 modulo simultaneous conjugation by S3 fixing 0",
        "raw_per_leg": 6 * 24**3,
        "normalized_labeled_per_leg": 24**3,
        "burnside_orbits_per_leg": burnside,
        "enumerated_orbits_per_leg": len(rows),
        "labeled_no_double_edge_after_q_normalization": labeled_irreducible,
        "orbits_no_double_edge_per_leg": len(irreducible_rows),
        "labeled_connected_no_double_edge_after_q_normalization": labeled_connected_irreducible,
        "orbits_connected_no_double_edge_per_leg": len(connected_rows),
        "irreducible_orbits_self_star": sum(
            r["star_inverse_canonical"] == r["permutations"] for r in irreducible_rows
        ),
        "orbits_double_edge_per_leg": len(rows) - len(irreducible_rows),
        "histogram_irreducible_connected_aut_order": {
            f"irreducible={k[0]},connected={k[1]},aut={k[2]}": v for k, v in sorted(hist.items())
        },
        "orbit_reduction_histogram_target_multiplicity_loops": {
            f"target={k[0]},multiplicity={k[1]},loops={k[2]}": v
            for k, v in sorted(reduction_histogram.items())
        },
        "labeled_reduction_histogram_target_multiplicity_loops": {
            f"target={k[0]},multiplicity={k[1]},loops={k[2]}": v
            for k, v in sorted(labeled_reduction_histogram.items())
        },
        "all_representatives_sha256": hashlib.sha256(raw_text.encode()).hexdigest(),
        "no_double_edge_representatives_sha256": hashlib.sha256(irreducible_text.encode()).hexdigest(),
        "connected_no_double_edge_representatives_sha256": hashlib.sha256(connected_text.encode()).hexdigest(),
        "representatives": rows,
    }
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    summary = {k: v for k, v in result.items() if k != "representatives"}
    summary["result_sha256"] = hashlib.sha256(output_path.read_bytes()).hexdigest()
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("GRAPH_CLASSIFICATION.json"))
    args = parser.parse_args()
    main(args.output)
