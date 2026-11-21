#!/usr/bin/env python3
"""Independent exact audit of PREREG tests 1--6; Python standard library only.

Author: A. M. Thorn / independent breaker session, 2026-10-23.
Original work: Apache-2.0. NON-CANONICAL; no phase decision.

Arithmetic is independently implemented in Z[z]/Phi_7(z), not the primary
real cubic implementation. This source must be publicly pinned before use.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json


ZERO = (0, 0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(k, a):
    return tuple(k * x for x in a)


def sub(a, b):
    return add(a, scale(-1, b))


def mul(a, b):
    # First multiply modulo z^7-1, then remove the z^6 coefficient using
    # Phi_7=1+z+...+z^6. No floating point or real-root substitution.
    c = [0] * 7
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[(i + j) % 7] += x * y
    return tuple(c[i] - c[6] for i in range(6))


def power(a, n):
    result = ONE
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n //= 2
    return result


def zpow(k):
    k %= 7
    if k == 6:
        return (-1,) * 6
    return tuple(int(i == k) for i in range(6))


def automorphism(a, r):
    result = ZERO
    for i, coefficient in enumerate(a):
        result = add(result, scale(coefficient, zpow(r * i)))
    return result


X = add(zpow(1), zpow(-1))
X2 = mul(X, X)


def from_real(a, b, c):
    return add(scale(a, ONE), add(scale(b, X), scale(c, X2)))


def to_real(v):
    # Unique conversion from the canonical six cyclotomic coefficients.
    b = -v[3]
    c = v[2] + b
    a = v[0] + b - 2 * c
    assert from_real(a, b, c) == v
    assert automorphism(v, 6) == v
    return (a, b, c)


def poly_numerator(n, d):
    return n * n * n + n * n * d - 2 * n * d * d - d * d * d


def real_root_interval():
    # P(1)<0<P(3/2), and P'(x)>=3 on [1,3/2]. The contract's selected
    # real root is therefore uniquely isolated by these integer bisections.
    lo, hi, den = 2, 3, 2
    assert poly_numerator(lo, den) < 0 < poly_numerator(hi, den)
    for _ in range(96):
        mid = lo + hi
        new_den = 2 * den
        sign = poly_numerator(mid, new_den)
        assert sign != 0
        if sign < 0:
            lo, hi = mid, 2 * hi
        else:
            lo, hi = 2 * lo, mid
        den = new_den
    assert hi - lo == 1
    assert poly_numerator(lo, den) < 0 < poly_numerator(hi, den)
    return lo, hi, den


def positive_real(v, interval):
    a, b, c = to_real(v)
    lo, hi, den = interval
    # The midpoint error of q(x)=a+bx+cx^2 is at most
    # (|b|+3|c|)/(2*den), since 1<x<3/2.
    d = 2 * den
    n = lo + hi
    midpoint_numerator = a * d * d + b * n * d + c * n * n
    error_numerator = (abs(b) + 3 * abs(c)) * d
    assert midpoint_numerator > error_numerator


def compositions(total, length, prefix=()):
    if length == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from compositions(total - first, length - 1, prefix + (first,))


def audit_algebra():
    assert add(add(power(X, 3), X2), add(scale(-2, X), scale(-1, ONE))) == ZERO
    assert sum(zpow(k)[0] for k in range(7)) == 0
    assert power(zpow(1), 7) == ONE
    interval = real_root_interval()
    weights = tuple(add(scale(2, ONE), add(zpow(k), zpow(-k))) for k in range(7))
    expected_weights = (from_real(4, 0, 0), from_real(2, 1, 0),
                        from_real(0, 0, 1), from_real(3, -1, -1),
                        from_real(3, -1, -1), from_real(0, 0, 1),
                        from_real(2, 1, 0))
    assert weights == expected_weights
    # D=(z^k-z^-k)/w=(z^k-1)/(z^k+1). For odd order seven its exact
    # polynomial is z^k-z^(2k)+...-z^(6k), with integral coefficients.
    ds = []
    for k in range(7):
        d = ZERO
        for m in range(1, 7):
            d = add(d, scale(1 if m % 2 else -1, zpow(m * k)))
        assert mul(d, weights[k]) == sub(zpow(k), zpow(-k))
        assert automorphism(d, 6) == scale(-1, d)
        ds.append(d)
        positive_real(weights[k], interval)
    ds = tuple(ds)
    r = from_real(-1, -4, 4)
    assert mul(r, add(scale(2, ONE), X)) == sub(scale(2, ONE), X)
    assert mul(ds[1], ds[1]) == scale(-1, r)
    g2, g3 = from_real(-3, 2, 2), from_real(1, 4, 2)
    assert mul(g2, X) == add(scale(2, ONE), X)
    assert mul(g3, sub(X, ONE)) == add(ONE, X)
    gs = (ZERO, ONE, g2, g3, scale(-1, g3), scale(-1, g2), scale(-1, ONE))
    for k in range(7):
        assert ds[k] == mul(ds[1], gs[k])
    positive_real(r, interval)
    wpowers = tuple(tuple(power(w, p) for p in range(7)) for w in weights)

    def mass(counts, shift=0):
        value = ONE
        for k, count in enumerate(counts):
            if count:
                value = mul(value, wpowers[(shift + k) % 7][count])
        return value

    digest = sha256()
    count_vectors = 0
    rows = 0
    for counts in compositions(6, 7):
        count_vectors += 1
        masses = [mass(counts, a) for a in range(7)]
        total = ZERO
        for a, value in enumerate(masses):
            positive_real(value, interval)
            coefficients = to_real(value)
            payload = json.dumps([list(counts), a, list(coefficients)],
                                 separators=(",", ":"), ensure_ascii=True) + "\n"
            digest.update(payload.encode("ascii"))
            rows += 1
            total = add(total, value)
        positive_real(total, interval)
        # Normalize independently through the real-subfield norm, computed
        # by cyclotomic automorphisms. Every probability is represented as
        # its exact six integer numerators divided by the positive norm.
        adjugate = mul(automorphism(total, 2), automorphism(total, 3))
        norm = mul(total, adjugate)
        assert norm[0] > 0 and norm[1:] == (0, 0, 0, 0, 0)
        probability_numerators = [mul(value, adjugate) for value in masses]
        accumulated = ZERO
        for value in probability_numerators:
            accumulated = add(accumulated, value)
        assert accumulated == scale(norm[0], ONE)
    assert count_vectors == 924 and rows == 6468
    print("CONDITIONAL_MASSES compositions=924 rows=6468 sha256=" + digest.hexdigest())
    print("ALGEBRA weights=7 scores=7 positive=PASS normalization=PASS")
    return weights, ds, mass


def audit_incidence_words():
    total = 0
    rows = []
    for degree in range(7):
        aliases = {5: 0, 6: 0}
        for word in product((-1, 0, 1), repeat=degree):
            total += 1
            value = sum(word)
            for modulus in (7, 8, 13):
                assert (value == 0) == (value % modulus == 0)
            for modulus in aliases:
                aliases[modulus] += int(value != 0 and value % modulus == 0)
        rows.append([degree, 3 ** degree, aliases[5], aliases[6]])
    assert total == sum(3 ** degree for degree in range(7))
    print("INCIDENCE_WORDS " + json.dumps(rows, separators=(",", ":")))


def shifted(x, direction, sizes):
    y = list(x)
    y[direction] = (y[direction] + 1) % sizes[direction]
    return tuple(y)


def make_torus(sizes):
    dim = len(sizes)
    vertices = list(product(*(range(n) for n in sizes)))
    edges = [(x, mu) for x in vertices for mu in range(dim)]
    faces = [(x, mu, nu) for x in vertices for mu, nu in combinations(range(dim), 2)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    face_index = {face: i for i, face in enumerate(faces)}
    incidence = []
    for x, mu, nu in faces:
        column = Counter()
        for edge, sign in (((x, mu), 1), ((shifted(x, mu, sizes), nu), 1),
                           ((shifted(x, nu, sizes), mu), -1), ((x, nu), -1)):
            column[edge_index[edge]] += sign
        incidence.append({edge: value for edge, value in column.items() if value})
    return vertices, edges, faces, face_index, incidence


def boundary(face_values, incidence, edge_count):
    output = [0] * edge_count
    for p, value in face_values.items():
        for edge, sign in incidence[p].items():
            output[edge] += value * sign
    return output


def audit_four_tori():
    for side in (4, 6):
        sizes = (side,) * 4
        vertices, edges, faces, face_index, incidence = make_torus(sizes)
        volume = side ** 4
        row_degrees = [0] * len(edges)
        for column in incidence:
            for edge, sign in column.items():
                row_degrees[edge] += abs(sign)
        assert set(row_degrees) == {6}
        current = [((-1) ** sum(x[1:]) if mu == 0 else 0) for x, mu in edges]
        divergence = Counter()
        for (x, mu), value in zip(edges, current):
            divergence[x] -= value
            divergence[shifted(x, mu, sizes)] += value
        assert all(value == 0 for value in divergence.values())
        supports = []
        last_boundary = None
        for modulus in range(2, 7):
            coefficients = next(a for a in product(range(3), repeat=3) if sum(a) == modulus)
            state = {}
            for p, (x, mu, nu) in enumerate(faces):
                if mu != 0:
                    continue
                s = (-1) ** sum(x[1:])
                coefficient = coefficients[nu - 1]
                value = (0, (1 + s) // 2, s)[coefficient]
                if value:
                    state[p] = value
            b = boundary(state, incidence, len(edges))
            assert b == [modulus * value for value in current]
            assert any(b) and all(value % modulus == 0 for value in b)
            assert len(state) == modulus * volume // 2
            supports.append([modulus, len(state), sum(value != 0 for value in b)])
            last_boundary = b
        inserted = [b + j for b, j in zip(last_boundary, current)]
        assert inserted == [7 * value for value in current]
        assert any(inserted) and all(value % 7 == 0 for value in inserted)
        print("TORUS_WITNESSES L=" + str(side) + " " + json.dumps(supports, separators=(",", ":")))
        if side == 4:
            audit_wrapping(sizes, vertices, edges, faces, face_index, incidence)


def winding_values(state, faces, sizes, mu, nu):
    values = [[0 for _ in range(sizes[nu])] for _ in range(sizes[mu])]
    for p, coefficient in state.items():
        x, a, b = faces[p]
        if (a, b) == (mu, nu):
            values[x[mu]][x[nu]] += coefficient
    return tuple(value for row in values for value in row)


def audit_wrapping(sizes, vertices, edges, faces, face_index, incidence):
    sheet_count = 0
    for mu, nu in combinations(range(4), 2):
        sheet = {}
        for p, (x, a, b) in enumerate(faces):
            if (a, b) == (mu, nu) and all(x[r] == 0 for r in range(4) if r not in (mu, nu)):
                sheet[p] = 1
        assert len(sheet) == sizes[mu] * sizes[nu]
        assert not any(boundary(sheet, incidence, len(edges)))
        for a, b in combinations(range(4), 2):
            values = winding_values(sheet, faces, sizes, a, b)
            expected = int((a, b) == (mu, nu))
            assert set(values) == {expected}
            plane_sum = sum(v for p, v in sheet.items() if faces[p][1:] == (a, b))
            assert plane_sum == sizes[a] * sizes[b] * expected
        sheet_count += 1
    cube_count = 0
    for x in vertices:
        for a, b, c in combinations(range(4), 3):
            cube = {
                face_index[(shifted(x, a, sizes), b, c)]: 1,
                face_index[(x, b, c)]: -1,
                face_index[(shifted(x, b, sizes), a, c)]: -1,
                face_index[(x, a, c)]: 1,
                face_index[(shifted(x, c, sizes), a, b)]: 1,
                face_index[(x, a, b)]: -1,
            }
            assert len(cube) == 6
            assert not any(boundary(cube, incidence, len(edges)))
            for mu, nu in combinations(range(4), 2):
                assert set(winding_values(cube, faces, sizes, mu, nu)) == {0}
            cube_count += 1
    assert sheet_count == 6 and cube_count == 4 * 4 ** 4
    print("TOPOLOGY wrapping_sheets=6 cube_boundaries=1024 all_stacks=PASS")


def rank_mod_seven(matrix):
    a = [[entry % 7 for entry in row] for row in matrix]
    rank = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, 7)
        a[rank] = [(entry * inv) % 7 for entry in a[rank]]
        for row in range(len(a)):
            if row != rank and a[row][col]:
                factor = a[row][col]
                a[row] = [(v - factor * w) % 7 for v, w in zip(a[row], a[rank])]
        rank += 1
    return rank


def scalar(v):
    assert v[1:] == (0, 0, 0, 0, 0)
    return v[0]


def audit_two_tori(ds, mass):
    d2 = tuple(mul(d, d) for d in ds)
    for sizes in ((2, 2), (3, 2)):
        vertices, edges, faces, _, incidence = make_torus(sizes)
        area = sizes[0] * sizes[1]
        incidence_rows = [[column.get(e, 0) for column in incidence] for e in range(len(edges))]
        assert rank_mod_seven(incidence_rows) == area - 1
        assert not any(boundary(dict.fromkeys(range(area), 1), incidence, len(edges)))
        # Explicitly enumerate every constrained plaquette assignment. Only
        # its subsequent exact weighted summation is grouped by sufficient
        # statistics; no plaquette-independence approximation is made.
        multiplicities = Counter()
        for prefix in product(range(7), repeat=area - 1):
            f = prefix + ((-sum(prefix)) % 7,)
            counts = tuple(f.count(k) for k in range(7))
            multiplicities[(counts, f[0])] += 1
        assignments = sum(multiplicities.values())
        assert assignments == 7 ** (area - 1)
        total = uniform_numerator = stack_numerator = twisted = ZERO
        cached = {}
        for (counts, first), multiplicity in sorted(multiplicities.items()):
            if counts not in cached:
                m = mass(counts)
                sum_d = sum_d2 = ZERO
                for k, number in enumerate(counts):
                    sum_d = add(sum_d, scale(number, ds[k]))
                    sum_d2 = add(sum_d2, scale(number, d2[k]))
                doubled_uniform = add(sub(scale(area, ONE), sum_d2), scale(2, mul(sum_d, sum_d)))
                cached[counts] = (m, doubled_uniform)
            m, doubled_uniform = cached[counts]
            total = add(total, scale(multiplicity, m))
            uniform_numerator = add(uniform_numerator, scale(multiplicity, mul(m, doubled_uniform)))
            doubled_stack = add(ONE, d2[first])
            stack_numerator = add(stack_numerator, scale(multiplicity, mul(m, doubled_stack)))
            shifted_counts = list(counts)
            shifted_counts[first] -= 1
            shifted_counts[(first + 1) % 7] += 1
            twisted = add(twisted, scale(multiplicity, mass(tuple(shifted_counts))))
        gauge_factor = 7 ** (area - 1)
        partition = Fraction(scalar(total), gauge_factor)
        uniform_h = Fraction(scalar(uniform_numerator), 2 * area * area * scalar(total))
        stack_h = Fraction(scalar(stack_numerator), 2 * scalar(total))
        assert partition == 2 ** area + 2
        assert uniform_h == stack_h == Fraction(2, 2 ** area + 2)
        assert twisted == scale(gauge_factor, add(scale(2 ** area, ONE), X))
        # Independent dual enumeration retains the two winding sectors.
        closed = []
        for values in product((-1, 0, 1), repeat=area):
            state = {i: value for i, value in enumerate(values) if value}
            if not any(boundary(state, incidence, len(edges))):
                closed.append(values)
        assert closed == [(-1,) * area, (0,) * area, (1,) * area]
        dual_z = sum(2 ** (area - sum(value != 0 for value in row)) for row in closed)
        dual_m2 = sum(row[0] ** 2 * 2 ** (area - sum(value != 0 for value in row)) for row in closed)
        assert dual_z == partition and Fraction(dual_m2, dual_z) == uniform_h
        assert Fraction(0, 2 ** area) != uniform_h
        print("TWO_TORUS sizes=" + "x".join(map(str, sizes)) +
              " assignments=" + str(assignments) + " partition=" + str(partition) +
              " uniform_h=" + str(uniform_h) + " stack_h=" + str(stack_h) +
              " twist_coefficients=" + json.dumps([2 ** area, 1, 0], separators=(",", ":")) +
              " twist_denominator=" + str(2 ** area + 2) + " winding_states=3")


def audit_cube_and_disk():
    # Independently build the boundary of one unit three-cube without
    # periodic identifications. Positive coordinate edges orient the cell.
    points = list(product(range(2), repeat=3))
    edges = [(x, mu) for x in points for mu in range(3) if x[mu] == 0]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    faces = [(x, mu, nu) for x in points for mu, nu in combinations(range(3), 2)
             if x[mu] == 0 and x[nu] == 0]
    columns = []
    for x, mu, nu in faces:
        y, z = list(x), list(x)
        y[mu] += 1
        z[nu] += 1
        columns.append({edge_index[(x, mu)]: 1, edge_index[(tuple(y), nu)]: 1,
                        edge_index[(tuple(z), mu)]: -1, edge_index[(x, nu)]: -1})
    assert len(faces) == 6 and len(edges) == 12
    closed = []
    for values in product((-1, 0, 1), repeat=6):
        state = {i: value for i, value in enumerate(values) if value}
        if not any(boundary(state, columns, len(edges))):
            closed.append(values)
    assert len(closed) == 3
    assert sorted(sum(value != 0 for value in row) for row in closed) == [0, 6, 6]
    assert closed[0] == tuple(-value for value in closed[2])
    assert sum(2 ** (6 - sum(value != 0 for value in row)) for row in closed) == 66
    disk_column = ({0: 1, 1: 1, 2: -1, 3: -1},)
    disk = [value for value in (-1, 0, 1)
            if not any(boundary({0: value}, disk_column, 4))]
    assert disk == [0]
    disk_partition = sum(2 if value == 0 else 1 for value in disk)
    assert disk_partition == 2
    print("CUBE_DISK cube_states=3 cube_partition=66 disk_states=1 disk_partition=2")


def main():
    audit_incidence_words()
    audit_four_tori()
    _, ds, mass = audit_algebra()
    audit_two_tori(ds, mass)
    audit_cube_and_disk()
    print("BREAKER_RESULT PASS exact_tests=1-6 sampler_trajectory=NOT_RUN phase=NOT_ASSESSED")


if __name__ == "__main__":
    main()
