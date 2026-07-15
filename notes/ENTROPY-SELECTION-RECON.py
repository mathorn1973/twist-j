#!/usr/bin/env python3
"""NON-CANONICAL local recon for the entropy selection problem.

This diagnostic compares finite dyadic Thue--Morse approximants of the
living-kernel skew action with multiplication by J on O/lambda^5.  It is not
a public verifier, carries no frozen target, and must not be cited as probe
evidence.
"""

from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BRIDGE4 = REPO / "probes" / "P-ENTROPY-BRIDGE-4" / "verify.py"


def load_bridge4():
    spec = spec_from_file_location("public_entropy_bridge4", BRIDGE4)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the public Bridge-4 definitions")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cycle_type(mapping, points):
    remaining = set(points)
    cycles = Counter()
    while remaining:
        start = min(remaining)
        state = start
        length = 0
        while state in remaining:
            remaining.remove(state)
            state = mapping[state]
            length += 1
        if state != start:
            raise RuntimeError("mapping is not a permutation of the carrier")
        cycles[length] += 1
    return cycles


def source_monodromy_type(period):
    """Cycle type of J^period from the public O/lambda^5 J-spectrum."""
    j_orbits = {1: 1, 4: 1, 20: 156}
    result = Counter()
    for orbit_length, orbit_count in j_orbits.items():
        split = gcd(period, orbit_length)
        result[orbit_length // split] += orbit_count * split
    return result


def compose_word(F, word, points):
    mapping = {}
    for point in points:
        state = point
        for letter in word:
            state = F[letter][state]
        mapping[point] = state
    return mapping


def signature(counter):
    return tuple(sorted(counter.items()))


def main():
    public = load_bridge4()
    F = public.build_kernel()
    tm = tuple(bin(n).count("1") & 1 for n in range(1 << 10))
    support, components = public.census(F, tm)
    halves = (
        frozenset(F[0][state] for state in support),
        frozenset(F[1][state] for state in support),
    )

    print("ENTROPY-SELECTION local recon")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print("comparison: J^L on O/lambda^5 versus one repeated dyadic")
    print("Thue--Morse supertile on the living carrier")
    print()

    for level in range(2, 11):
        period = 1 << level
        word = tm[:period]
        source_half = halves[word[-1]]
        target_map = compose_word(F, word, source_half)
        target_type = cycle_type(target_map, source_half)
        source_type = source_monodromy_type(period)

        component_types = Counter()
        singlet_type = None
        for component in components:
            points = component & source_half
            local_type = cycle_type(target_map, points)
            if len(component) == 10:
                singlet_type = signature(local_type)
            else:
                component_types[signature(local_type)] += 1

        print(
            "level=%02d L=%04d source=%s target=%s match=%s"
            % (
                level,
                period,
                dict(sorted(source_type.items())),
                dict(sorted(target_type.items())),
                source_type == target_type,
            )
        )
        print("  singlet=%s" % (dict(singlet_type or ()),))
        print(
            "  size20=%s"
            % ({str(dict(key)): count for key, count in component_types.items()},)
        )

    print()
    print("Interpretation guard:")
    print("A mismatch is not a no-go for a measurable selector because the")
    print("Thue--Morse subshift has no periodic points. It is evidence that a")
    print("selector cannot be obtained by naively matching repeated finite")
    print("supertiles; any viable construction must use the aperiodic carry")
    print("structure and must be tested separately for regularity and measure.")


if __name__ == "__main__":
    main()
