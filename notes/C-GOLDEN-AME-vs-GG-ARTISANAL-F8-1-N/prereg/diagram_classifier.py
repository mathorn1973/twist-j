#!/usr/bin/env python3
"""Pure combinatorial census for the frozen closed n=4 F8 family.

This program has no tensor parser and accepts no tensor data.  It classifies
only four-coloured bipartite matching diagrams.  A normalized diagram fixes
sigma_0=id and is represented by (sigma_1,sigma_2,sigma_3) in S_4^3.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter


S4 = tuple(itertools.permutations(range(4)))
ID = (0, 1, 2, 3)

EXPECTED_REPRESENTATIVES = (
    ((1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)),
    ((1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1)),
    ((1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)),
    ((1, 2, 3, 0), (3, 0, 1, 2), (2, 3, 0, 1)),
)


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p after q."""

    return tuple(p[q[i]] for i in range(len(p)))


def conjugate(p: tuple[int, ...], g: tuple[int, ...]) -> tuple[int, ...]:
    return compose(compose(g, p), inverse(g))


def canonical_copy_class(triple: tuple[tuple[int, ...], ...]) -> tuple:
    """Canonicalize under simultaneous S4 conjugation of copy labels."""

    return min(tuple(conjugate(p, g) for p in triple) for g in S4)


def pair_multiplicities(triple: tuple[tuple[int, ...], ...]) -> Counter:
    counts: Counter = Counter()
    for p in (ID,) + triple:
        counts.update((r, p[r]) for r in range(4))
    return counts


def is_collision_free(triple: tuple[tuple[int, ...], ...]) -> bool:
    """True iff no T/bar-T vertex pair shares two coloured edges."""

    counts = pair_multiplicities(triple)
    return len(counts) == 16 and all(value == 1 for value in counts.values())


def normalize_first_matching(sequence: tuple[tuple[int, ...], ...]) -> tuple:
    """Set the first matching to id by relabelling all bar vertices.

    A matching maps a T-copy label to a bar-copy label.  Left composition by
    sequence[0]^{-1} therefore sends the first matching to the identity.
    """

    left = inverse(sequence[0])
    normalized = tuple(compose(left, p) for p in sequence)
    assert normalized[0] == ID
    return normalized[1:]


def party_action(
    rho: tuple[int, ...], representatives: tuple[tuple, ...]
) -> tuple[int, ...]:
    """Induced action of a party permutation on the four copy classes.

    Convention: new colour q receives old colour rho[q].
    """

    index = {rep: i for i, rep in enumerate(representatives)}
    image = []
    for triple in representatives:
        sequence = (ID,) + triple
        reordered = tuple(sequence[rho[q]] for q in range(4))
        normalized = normalize_first_matching(reordered)
        image.append(index[canonical_copy_class(normalized)])
    return tuple(image)


def serialize_triples(triples: tuple[tuple, ...]) -> bytes:
    lines = []
    for triple in triples:
        lines.append("/".join("".join(map(str, p)) for p in triple))
    return ("\n".join(lines) + "\n").encode("ascii")


def classify() -> dict:
    normalized = tuple(itertools.product(S4, repeat=3))
    collision_free = tuple(t for t in normalized if is_collision_free(t))
    representatives = tuple(sorted({canonical_copy_class(t) for t in collision_free}))
    orbit_sizes = tuple(
        sum(canonical_copy_class(t) == rep for t in collision_free)
        for rep in representatives
    )

    if representatives != EXPECTED_REPRESENTATIVES:
        raise AssertionError((representatives, EXPECTED_REPRESENTATIVES))
    if len(normalized) != 13_824 or len(collision_free) != 24:
        raise AssertionError("unexpected normalized/collision-free census")
    if orbit_sizes != (6, 6, 6, 6):
        raise AssertionError(orbit_sizes)

    actions_by_party = tuple((rho, party_action(rho, representatives)) for rho in S4)
    action_image = tuple(sorted({action for _, action in actions_by_party}))
    expected_image = tuple(
        sorted((0,) + tail for tail in itertools.permutations((1, 2, 3)))
    )
    if action_image != expected_image:
        raise AssertionError((action_image, expected_image))
    kernel = tuple(rho for rho, action in actions_by_party if action == (0, 1, 2, 3))
    expected_kernel = (
        (0, 1, 2, 3),
        (1, 0, 3, 2),
        (2, 3, 0, 1),
        (3, 2, 1, 0),
    )
    if kernel != expected_kernel:
        raise AssertionError((kernel, expected_kernel))

    lower_degree = {}
    for n in (1, 2, 3):
        sn = tuple(itertools.permutations(range(n)))
        ident = tuple(range(n))
        count = 0
        for triple in itertools.product(sn, repeat=3):
            multiplicities = Counter()
            for p in (ident,) + triple:
                multiplicities.update((r, p[r]) for r in range(n))
            if len(multiplicities) == 4 * n and all(v == 1 for v in multiplicities.values()):
                count += 1
        if count:
            raise AssertionError((n, count))
        lower_degree[str(n)] = count

    representative_bytes = serialize_triples(representatives)
    labeled_bytes = serialize_triples(tuple(sorted(collision_free)))
    return {
        "schema": "artisan-f8-diagram-census-v1",
        "input_data": "none",
        "n": 4,
        "normalization": "sigma0=id",
        "normalized_diagrams": len(normalized),
        "double_edge_reducible_diagrams": len(normalized) - len(collision_free),
        "collision_free_labeled_diagrams": len(collision_free),
        "collision_free_copy_classes": len(representatives),
        "copy_class_orbit_sizes": orbit_sizes,
        "representatives": representatives,
        "representatives_sha256": hashlib.sha256(representative_bytes).hexdigest(),
        "collision_free_labeled_sha256": hashlib.sha256(labeled_bytes).hexdigest(),
        "lower_degree_collision_free_counts": lower_degree,
        "party_action_convention": "new_colour_q=old_colour_rho[q]",
        "party_action_image": action_image,
        "party_action_image_order": len(action_image),
        "party_actions": tuple(
            {"rho": rho, "class_action": action} for rho, action in actions_by_party
        ),
        "party_action_kernel": kernel,
        "party_action_kernel_order": len(kernel),
        "party_action_summary": "D0 fixed; D1,D2,D3 carry the full S3 action",
    }


def human_output(result: dict) -> str:
    lines = [
        "ARTISAN_F8_DIAGRAM_CLASSIFIER_V1",
        f"INPUT_DATA={result['input_data']}",
        f"NORMALIZED_DIAGRAMS={result['normalized_diagrams']}",
        f"DOUBLE_EDGE_REDUCIBLE={result['double_edge_reducible_diagrams']}",
        f"COLLISION_FREE_LABELED={result['collision_free_labeled_diagrams']}",
        f"COPY_CLASSES={result['collision_free_copy_classes']}",
        "ORBIT_SIZES=" + ",".join(map(str, result["copy_class_orbit_sizes"])),
    ]
    for i, triple in enumerate(result["representatives"]):
        text = "/".join("".join(map(str, p)) for p in triple)
        lines.append(f"D{i}={text}")
    lines.extend(
        [
            f"REPRESENTATIVES_SHA256={result['representatives_sha256']}",
            f"LABELED_SHA256={result['collision_free_labeled_sha256']}",
            f"PARTY_IMAGE_ORDER={result['party_action_image_order']}",
            f"PARTY_KERNEL_ORDER={result['party_action_kernel_order']}",
            "PARTY_ACTION=D0_FIXED_D1_D2_D3_FULL_S3",
            "LOWER_N_COLLISION_FREE=n1:0,n2:0,n3:0",
            "STATUS=PASS",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit canonical JSON")
    args = parser.parse_args()
    result = classify()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(human_output(result), end="")


if __name__ == "__main__":
    main()
