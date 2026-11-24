#!/usr/bin/env python3
"""Frozen primary exact audit, tests 1--6 of PREREG.md.

PUBLIC / NON-CANONICAL. Original code: A. M. Thorn, Apache-2.0.
No phase inference. This program may run only after the public source pin.
The independent breaker is neither read nor imported.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json

from z7_exact import CubicLattice, G_SCORE, K7, R7, WEIGHTS, X7


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def integer_coefficients(value):
    require(all(c.denominator == 1 for c in value.coefficients), "Nonintegral comparison coefficient")
    return [c.numerator for c in value.coefficients]


def audit_local_words():
    rows = []
    for degree in range(7):
        counts = {"integer_zero": 0, "alias_5": 0, "alias_6": 0}
        total = 0
        for word in product((-1, 0, 1), repeat=degree):
            total += 1
            boundary = sum(word)
            for modulus in (7, 8, 13):
                require((boundary == 0) == (boundary % modulus == 0), "Local no-alias failure")
            counts["integer_zero"] += int(boundary == 0)
            for modulus in (5, 6):
                counts[f"alias_{modulus}"] += int(boundary != 0 and boundary % modulus == 0)
        require(total == 3**degree, "Incomplete local enumeration")
        require(counts["alias_5"] == (2 if degree == 5 else 12 if degree == 6 else 0), "Modulo-five control")
        require(counts["alias_6"] == (2 if degree == 6 else 0), "Modulo-six control")
        rows.append({"degree": degree, "words": total, **counts})
    return rows


def chain_boundary(lattice, chain):
    """Integer face-chain boundary, accepting a sparse face/value dictionary."""
    boundary = [0] * lattice.n_edges
    for face, value in chain.items():
        for edge, sign in lattice.boundary(face):
            boundary[edge] += value * sign
    return boundary


def vertex_boundary(lattice, current):
    boundary = [0] * lattice.volume
    for site in lattice.sites:
        for direction in range(lattice.dimension):
            value = current[lattice.edge(site, direction)]
            boundary[lattice.site_index[site]] -= value
            boundary[lattice.site_index[lattice.shift(site, direction)]] += value
    return boundary


def audit_alias_witnesses():
    rows = []
    for length in (4, 6):
        lattice = CubicLattice((length,) * 4)
        require(all(len(incident) == 6 for incident in lattice.edge_faces), "4D incidence degree")
        current = [0] * lattice.n_edges
        for site in lattice.sites:
            current[lattice.edge(site, 0)] = (-1) ** sum(site[1:])
        require(not any(vertex_boundary(lattice, current)), "Current not conserved")
        for modulus in range(2, 7):
            triple = next(a for a in product(range(3), repeat=3) if sum(a) == modulus)
            chain = {}
            for site in lattice.sites:
                parity = (-1) ** sum(site[1:])
                for direction, amount in enumerate(triple, start=1):
                    value = (0, (1 + parity) // 2, parity)[amount]
                    if value:
                        chain[lattice.face(site, 0, direction)] = value
            boundary = chain_boundary(lattice, chain)
            require(boundary == [modulus * value for value in current], "Wrong alias witness boundary")
            require(len(chain) == modulus * lattice.volume // 2, "Wrong alias witness support")
            require(all(value % modulus == 0 for value in boundary) and any(boundary), "Not a nonzero modular cycle")
            if modulus == 6:
                inserted = [value + charge for value, charge in zip(boundary, current)]
                require(inserted == [7 * value for value in current], "Inserted N7 witness")
                require(all(value % 7 == 0 for value in inserted) and any(inserted), "Inserted selection does not differ")
            rows.append({"L": length, "N": modulus, "triple": triple,
                         "vertices": lattice.volume, "edges": lattice.n_edges,
                         "support": len(chain), "current_support": sum(value != 0 for value in current)})
    return rows


def stack_pairings(lattice, chain, orientation):
    mu, nu = orientation
    result = {(a, b): 0 for a in range(lattice.lengths[mu]) for b in range(lattice.lengths[nu])}
    for site in lattice.sites:
        result[(site[mu], site[nu])] += chain.get(lattice.face(site, mu, nu), 0)
    return result


def cube_boundary(lattice, site, directions):
    result = defaultdict(int)
    for index, direction in enumerate(directions):
        mu, nu = tuple(d for d in directions if d != direction)
        sign = (-1) ** index
        result[lattice.face(lattice.shift(site, direction), mu, nu)] += sign
        result[lattice.face(site, mu, nu)] -= sign
    return {face: value for face, value in result.items() if value}


def audit_topology():
    lattice = CubicLattice((4,) * 4)
    sheets = []
    for orientation in lattice.orientations:
        transverse = [direction for direction in range(4) if direction not in orientation]
        sheet = {lattice.face(site, *orientation): 1 for site in lattice.sites
                 if all(site[direction] == 0 for direction in transverse)}
        require(not any(chain_boundary(lattice, sheet)), "Wrapping sheet not closed")
        for tested in lattice.orientations:
            expected = int(tested == orientation)
            pairings = stack_pairings(lattice, sheet, tested)
            require(set(pairings.values()) == {expected}, "Wrapping sheet stack mismatch")
            total = sum(sheet.get(lattice.face(site, *tested), 0) for site in lattice.sites)
            area = lattice.lengths[tested[0]] * lattice.lengths[tested[1]]
            require(total == area * expected, "Wrapping sheet uniform mismatch")
        sheets.append({"orientation": orientation, "support": len(sheet), "winding": 1})
    cubes = 0
    for site in lattice.sites:
        for directions in combinations(range(4), 3):
            chain = cube_boundary(lattice, site, directions)
            require(len(chain) == 6, "Cube has wrong face count")
            require(not any(chain_boundary(lattice, chain)), "Boundary squared is not zero")
            for orientation in lattice.orientations:
                require(not any(stack_pairings(lattice, chain, orientation).values()), "Local cube changes winding")
            cubes += 1
    return {"L": 4, "fundamental_sheets": sheets, "cube_boundaries": cubes}


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first,) + rest


def audit_field_and_conditionals():
    x, r = X7, R7
    require(x**3 + x**2 - 2*x - 1 == K7(), "Minimal polynomial")
    require((x - 1).sign() > 0 and (Fraction(3, 2) - x).sign() > 0, "Wrong real root")
    require(r.sign() > 0, "Negative square scale")
    require(sum(WEIGHTS) == K7(14), "Seven-weight normalization")
    require(sum(WEIGHTS[k] * G_SCORE[k] for k in range(7)) == K7(), "Odd weighted score")
    # Chebyshev recurrence for 2*cos(k*theta), including return at k=7.
    cosines = [K7(2), x]
    for _ in range(2, 8):
        cosines.append(x * cosines[-1] - cosines[-2])
    require(cosines[7] == K7(2), "Seventh-angle closure")
    require(all(value != K7(2) for value in cosines[1:7]), "Nonprimitive angle")
    for residue in range(7):
        weight, score = WEIGHTS[residue], G_SCORE[residue]
        require(weight == 2 + cosines[residue], "Weight/Chebyshev identity")
        require(weight.sign() > 0, "Nonpositive plaquette weight")
        require(weight == WEIGHTS[-residue % 7], "Weight parity")
        require(score == -G_SCORE[-residue % 7], "Score parity")
        require(weight * (1 + r * score**2) == K7(4), "Squared score identity")
        following = G_SCORE[(residue + 1) % 7]
        require(following * (1 - r * score) == score + 1, "Tangent addition identity")
        require(K7.from_json(weight.to_json()) == weight, "Field serialization")

    powers = [[weight**power for power in range(7)] for weight in WEIGHTS]
    digest = sha256()
    compositions = lines = 0
    previous = None
    for counts in weak_compositions(6, 7):
        require(previous is None or previous < counts, "Composition order")
        previous = counts
        masses = []
        for proposed in range(7):
            mass = K7(1)
            for residue, multiplicity in enumerate(counts):
                mass *= powers[(proposed + residue) % 7][multiplicity]
            require(mass.sign() > 0, "Nonpositive conditional mass")
            masses.append(mass)
            row = [list(counts), proposed, integer_coefficients(mass)]
            digest.update((json.dumps(row, separators=(",", ":")) + "\n").encode("ascii"))
            lines += 1
        total = sum(masses)
        inverse = total.inverse()
        probabilities = [mass * inverse for mass in masses]
        require(sum(probabilities) == K7(1), "Conditional normalization")
        require(all(probability.sign() > 0 for probability in probabilities), "Nonpositive probability")
        compositions += 1
    require(compositions == 924 and lines == 6468, "Conditional census incomplete")
    return {"weights": [integer_coefficients(weight) for weight in WEIGHTS],
            "compositions": compositions, "comparison_lines": lines,
            "conditional_mass_sha256": digest.hexdigest()}


def audit_2d():
    """Exhaustive plaquette assignments, grouped only to save exact arithmetic.

    Each visited assignment satisfies sum f=0 mod seven. Grouping by counts
    and the first face retains precisely the uniform and stack readers and
    the one-face shifted partition required by the frozen contract.
    """
    rows = []
    score_squares = tuple(score**2 for score in G_SCORE)
    stack_readers = tuple((1 - R7 * square) / 2 for square in score_squares)
    shift_ratios = tuple(WEIGHTS[(k + 1) % 7] / WEIGHTS[k] for k in range(7))
    for lengths in ((2, 2), (3, 2)):
        area = lengths[0] * lengths[1]
        grouped = Counter()
        states = 0
        for prefix in product(range(7), repeat=area - 1):
            flux = prefix + ((-sum(prefix)) % 7,)
            require(sum(flux) % 7 == 0, "Constrained plaquette enumeration")
            counts = tuple(flux.count(residue) for residue in range(7))
            grouped[(counts, flux[0])] += 1
            states += 1
        require(states == 7 ** (area - 1), "2D enumeration count")
        partition = uniform_numerator = stack_numerator = shifted_partition = K7()
        mass_cache = {}
        for (counts, first), multiplicity in sorted(grouped.items()):
            if counts not in mass_cache:
                mass = K7(1)
                score_sum = square_sum = K7()
                for residue, count in enumerate(counts):
                    mass *= WEIGHTS[residue] ** count
                    score_sum += count * G_SCORE[residue]
                    square_sum += count * score_squares[residue]
                uniform_reader = (Fraction(area, 2) + R7 * square_sum / 2
                                  - R7 * score_sum**2) / area**2
                mass_cache[counts] = (mass, uniform_reader)
            mass, uniform_reader = mass_cache[counts]
            contribution = multiplicity * mass
            partition += contribution
            uniform_numerator += contribution * uniform_reader
            stack_numerator += contribution * stack_readers[first]
            shifted_partition += contribution * shift_ratios[first]
        normalized_partition = partition / states
        expected_partition = 2**area + 2
        expected_mean = Fraction(2, expected_partition)
        uniform_mean = uniform_numerator / partition
        stack_mean = stack_numerator / partition
        normalized_shift = shifted_partition / states
        require(normalized_partition == K7(expected_partition), "2D partition control")
        require(uniform_mean == K7(expected_mean), "2D uniform Hessian control")
        require(stack_mean == K7(expected_mean), "2D stack Hessian control")
        require(normalized_shift == 2**area + X7, "2D discrete-source partition")
        require(shifted_partition / partition == (2**area + X7) / expected_partition, "2D source ratio")
        # In two dimensions all three constant ternary fields are cycles;
        # omitting winding sectors would incorrectly leave only 2**area.
        require(expected_partition != 2**area and expected_mean > 0, "Boundary-only control not detected")
        rows.append({"lengths": lengths, "assignments": states,
                     "partition": normalized_partition.to_json(),
                     "uniform_hessian": uniform_mean.to_json(),
                     "stack_hessian": stack_mean.to_json(),
                     "shifted_partition": normalized_shift.to_json(),
                     "source_ratio": (shifted_partition / partition).to_json(),
                     "boundary_only_partition": 2**area})
    return rows


def audit_small_complexes():
    lattice = CubicLattice((2, 2, 2))
    oriented = cube_boundary(lattice, (0, 0, 0), (0, 1, 2))
    faces = sorted(oriented)
    surviving = []
    partition = 0
    for word in product((-1, 0, 1), repeat=6):
        chain = dict(zip(faces, word))
        if not any(chain_boundary(lattice, chain)):
            surviving.append(word)
            partition += 2 ** word.count(0)
    expected = {tuple(0 for _ in faces), tuple(oriented[face] for face in faces),
                tuple(-oriented[face] for face in faces)}
    require(set(surviving) == expected, "Single-cube ternary kernel")
    require(partition == 66, "Single-cube partition")
    disk_partition = sum(2 if value == 0 else 1 for value in (-1, 0, 1)
                         if not any(chain_boundary(lattice, {faces[0]: value})))
    require(disk_partition == 2, "Single-disk partition")
    return {"cube_fields": 3**6, "cube_survivors": len(surviving),
            "cube_partition": partition, "disk_partition": disk_partition}


def main():
    result = {"candidate": "C-PHOTON-U1-FINITE-CENTER-N", "implementation": "primary",
              "status": "PASS", "phase_decision_weight": 0,
              "local_words": audit_local_words(),
              "alias_witnesses": audit_alias_witnesses(),
              "topology": audit_topology(),
              "field_and_conditionals": audit_field_and_conditionals(),
              "two_dimensional": audit_2d(),
              "small_complexes": audit_small_complexes()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
