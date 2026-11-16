#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact finite reproduction of the funded fixed-reference H3 record."""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
from itertools import combinations, product
import sys


NX = 8
HEIGHTS = (4, 6)
MODES = ("ABSENT_ROW0", "PLUS", "MINUS")
HORIZON = 14
HOLD = range(4, 14)

# Ordered basis (1, j, j^2, j^3) of Q[j]/(1+j+j^2+j^3+j^4).
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 0, 1, 0)
RHO_INV = (0, 0, 0, 1)
J = (1, 0, 1, 0)
J_INV = (0, -1, -1, 0)
REFERENCE = (0, 0, 0, 8)
GLOBAL = (ZERO, (0, 0, 0, 64), (13056, 0, -1280, -1280), 27392)
J_POWERS = (ONE, (0, 1, 0, 0), RHO, RHO_INV, (-1, -1, -1, -1))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(n, a):
    return tuple(n * x for x in a)


def ring_sum(values):
    total = ZERO
    for value in values:
        total = add(total, value)
    return total


def mul(a, b):
    if a == ZERO or b == ZERO:
        return ZERO
    coefficients = [0] * 7
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            coefficients[i + k] += x * y
    for i in range(6, 3, -1):
        for k in range(1, 5):
            coefficients[i - k] -= coefficients[i]
    return tuple(coefficients[:4])


def sigma(a, exponent):
    return ring_sum(scale(x, J_POWERS[i * exponent % 5])
                    for i, x in enumerate(a))


def conj(a):
    a0, a1, a2, a3 = a
    return (a0 - a1, -a1, a3 - a1, a2 - a1)


@cache
def inverse(a):
    numerator = mul(mul(sigma(a, 2), sigma(a, 3)), conj(a))
    norm = mul(a, numerator)
    require(norm[0] != 0 and norm[1:] == (0, 0, 0), "nonzero field inverse")
    return scale(Fraction(1, norm[0]), numerator)


@cache
def h(a):
    return mul(a, conj(a))


def scalar_account(real):
    return 2 * real[0] - real[2]


def even(a):
    return all(x % 2 == 0 for x in a)


def half(a):
    require(even(a), "nonintegral native half")
    return tuple(x // 2 for x in a)


T = h(J)


def transport_pair(a, b, backward):
    difference = sub(a, b)
    if not even(difference):
        return a, b
    center = add(a, b)
    rotated = mul(RHO_INV if backward else RHO, difference)
    return half(add(center, rotated)), half(sub(center, rotated))


def collision(cell):
    r0, r2, clk, corr = cell
    md, fd = sub(r0, r2), sub(clk, corr)
    if not even(md) or not even(fd):
        return cell, 0
    d, f = half(md), half(fd)
    if d != ZERO and h(f) == mul(T, h(d)):
        dn, fn, tag = mul(J, d), mul(J_INV, f), 1
    elif f != ZERO and h(d) == mul(T, h(f)):
        dn, fn, tag = mul(J_INV, d), mul(J, f), 2
    else:
        return cell, 0
    mc, fc = half(add(r0, r2)), half(add(clk, corr))
    return (add(mc, dn), sub(mc, dn), add(fc, fn), sub(fc, fn)), tag


def index(ny, x, y, rail):
    return 4 * (x * ny + y) + rail


def transport(field, ny, bit, backward=False):
    result = list(field)
    for rail in range(4):
        size, breadth = (NX, ny) if rail == 3 else (ny, NX)
        for p, orthogonal in product(range(bit, size, 2), range(breadth)):
            q = (p + 1) % size
            if rail == 3:
                i, k = (index(ny, x, orthogonal, rail) for x in (p, q))
            else:
                i, k = (index(ny, orthogonal, y, rail) for y in (p, q))
            result[i], result[k] = transport_pair(field[i], field[k], backward)
    return tuple(result)


def collide(field, ny):
    result, events = [], []
    for start in range(0, len(field), 4):
        cell, tag = collision(field[start:start + 4])
        result.extend(cell)
        if tag:
            events.append((*divmod(start // 4, ny), tag))
    return tuple(result), tuple(events)


def endpoints(ny):
    return index(ny, 2, ny - 1, 3), index(ny, 4, ny - 1, 3)


@dataclass(frozen=True)
class Cut:
    ny: int
    stage: str
    tick: int
    bit: int
    field: tuple


def prepare(ny, mode):
    field = [ZERO] * (4 * NX * ny)
    for y, value in ((0, scale(16, J)), (1, scale(16, J)),
                     (ny - 2, scale(24, mul(RHO, J_INV))),
                     (ny - 1, scale(24, mul(RHO, J_INV)))):
        field[index(ny, 0, y, 0)] = value
        field[index(ny, 0, y, 1)] = scale(-1, value)
    u, v = add(scale(2, ONE), RHO), add(scale(2, ONE), mul(RHO, RHO))
    absent = (u, scale(-1, u), v, scale(-1, v))
    for x in range(NX):
        field[index(ny, x, ny - 1, 3)] = REFERENCE
        wave = (scale(16, absent[x % 4]) if mode == "ABSENT_ROW0"
                else scale(32 * (1 if mode == "PLUS" else -1) * (-1)**(x // 2), ONE))
        field[index(ny, x, 0, 3)] = wave
    return Cut(ny, "full", 0, 0, tuple(field))


def advance(cut):
    if cut.stage == "full" and cut.tick < HORIZON:
        field = transport(cut.field, cut.ny, cut.bit)
        return Cut(cut.ny, "post-C", cut.tick + 1, cut.bit, field), ()
    require(cut.stage == "post-C", "forward step outside carrier")
    field, events = collide(cut.field, cut.ny)
    return Cut(cut.ny, "full", cut.tick, 1 - cut.bit, field), events


def retreat(cut):
    require(cut.tick > 0, "reverse step outside carrier")
    if cut.stage == "post-C":
        field = transport(cut.field, cut.ny, cut.bit, backward=True)
        return Cut(cut.ny, "full", cut.tick - 1, cut.bit, field)
    field, _ = collide(cut.field, cut.ny)
    return Cut(cut.ny, "post-C", cut.tick, 1 - cut.bit, field)


@dataclass(frozen=True)
class Factor:
    dimension: int
    ray: tuple | None
    scalar: tuple | None


def factor(vector):
    anchor = next((value for value in vector if value != ZERO), None)
    if anchor is None:
        return Factor(len(vector), None, None)
    reciprocal = inverse(anchor)
    return Factor(len(vector), tuple(mul(value, reciprocal) for value in vector), anchor)


def recompose(encoded):
    if encoded.ray is None:
        require(encoded.scalar is None, "zero factor with scalar")
        return (ZERO,) * encoded.dimension
    require(len(encoded.ray) == encoded.dimension, "ray dimension")
    require(encoded.scalar is not None and encoded.scalar != ZERO, "missing scalar")
    require(next((value for value in encoded.ray if value != ZERO), None) == ONE,
            "noncanonical first chart coordinate")
    return tuple(mul(encoded.scalar, value) for value in encoded.ray)


@dataclass(frozen=True)
class EncodedCut:
    ny: int
    stage: str
    tick: int
    bit: int
    factor: Factor


def encode(cut):
    return EncodedCut(cut.ny, cut.stage, cut.tick, cut.bit, factor(cut.field))


def decode(encoded):
    full = encoded.stage == "full"
    require(encoded.ny in HEIGHTS and encoded.stage in ("full", "post-C")
            and (0 if full else 1) <= encoded.tick <= HORIZON
            and encoded.bit == (encoded.tick - (0 if full else 1)) % 2,
            "native cut context")
    require(encoded.factor.dimension == 4 * NX * encoded.ny, "native field dimension")
    field = recompose(encoded.factor)
    require(all(Fraction(x).denominator == 1 for value in field for x in value),
            "reconstructed field outside the native ring")
    return Cut(encoded.ny, encoded.stage, encoded.tick, encoded.bit,
               tuple(tuple(int(x) for x in value) for value in field))


def lifted_advance(encoded):
    cut, events = advance(decode(encoded))
    return encode(cut), events


def lifted_retreat(encoded):
    return encode(retreat(decode(encoded)))


@dataclass(frozen=True)
class Account:
    count: int
    linear: tuple
    quadratic: tuple
    q: int


def partition(ny):
    def group(y_values, rails):
        return {index(ny, x, y, rail)
                for x, y, rail in product(range(NX), y_values, rails)}

    archive, reference = endpoints(ny)
    roles = {
        "working": {index(ny, 0, 0, rail) for rail in (0, 1)},
        "auxiliary_matter": {index(ny, 0, y, rail)
                             for y, rail in product((1, ny - 2, ny - 1), (0, 1))},
        "local_clock": {index(ny, 0, 0, 2)},
        "remote_clock": group(range(1, ny), (2,)),
        "archive": {archive},
        "reference": {reference},
        "wave_row": group((0,), (3,)),
        "remote_CORR": group(range(1, ny), (3,)) - {archive, reference},
    }
    coordinates = set(range(4 * NX * ny))
    roles["environment"] = coordinates - set().union(*roles.values())
    require(set().union(*roles.values()) == coordinates
            and sum(map(len, roles.values())) == len(coordinates), "role partition")
    return roles


def accounts(cut, roles):
    field, ny = cut.field, cut.ny
    squared = tuple(h(value) for value in field)

    def account(indices):
        quadratic = ring_sum(squared[i] for i in indices)
        return Account(len(indices), ring_sum(field[i] for i in indices),
                       quadratic, scalar_account(quadratic))

    def group(y_values, rails):
        return tuple(index(ny, x, y, rail)
                     for x, y, rail in product(range(NX), y_values, rails))

    rows = tuple(account(group((y,), range(4))) for y in range(ny))
    rails = tuple(account(group(range(ny), (rail,))) for rail in range(4))
    row_rails = tuple(account(group((y,), (rail,)))
                      for y, rail in product(range(ny), range(4)))
    by_role = {name: account(indices) for name, indices in roles.items()}
    matter = ring_sum(entry.linear for entry in rails[:2])
    radiation = ring_sum(entry.linear for entry in rails[2:])
    total = account(range(len(field)))
    require((matter, radiation, total.quadratic, total.q) == GLOBAL, "global accounts")
    for parts in (rows, rails, row_rails, by_role.values()):
        require(Account(sum(entry.count for entry in parts),
                        ring_sum(entry.linear for entry in parts),
                        ring_sum(entry.quadratic for entry in parts),
                        sum(entry.q for entry in parts)) == total, "account conservation")
    require(total.linear == add(matter, radiation), "linear matter/radiation split")
    require(by_role["reference"] == Account(1, REFERENCE, scale(64, ONE), 128),
            "single counted reference")
    archive = field[endpoints(ny)[0]]
    require(by_role["archive"] == Account(1, archive, h(archive), scalar_account(h(archive))),
            "archive account")
    return rows, rails, row_rails, by_role


def read_pair(a, b):
    weighted = mul(sub(RHO, mul(RHO, RHO)), sub(a, b))
    return Fraction(4 * weighted[0] - sum(weighted[1:]), 30), scalar_account(h(a))


def inspect_cut(cut, encoded, mode, roles, counts, archives):
    ny, tick = cut.ny, cut.tick
    decoded = decode(encoded)
    require(decoded == cut, "complete native cut reconstruction")
    counts[cut.stage] += 1
    direct_accounts = accounts(cut, roles)
    require(accounts(decoded, roles) == direct_accounts, "reconstructed account views")
    archive_index, reference_index = endpoints(ny)
    a, b = (decoded.field[i] for i in (archive_index, reference_index))
    require(b == REFERENCE, "native reference moved")
    pair = factor((a, b))
    require(recompose(pair) == (a, b), "pair round trip")
    for factored, anchor in ((pair, 1), (encoded.factor, reference_index)):
        require(mul(b, inverse(factored.ray[anchor])) == factored.scalar,
                "fixed reference recovers stored scalar")
    sign = dict(zip(MODES, (0, 1, -1)))[mode]
    rho2 = mul(RHO, RHO)
    delta = add(ONE, scale(sign, sub(rho2, mul(rho2, RHO))))
    first_factor = sub(ONE, RHO)
    expected_a = REFERENCE
    expected_reader = (Fraction(0), 128)
    if tick in HOLD:
        counts["hold"] += 1
        if sign:
            expected_a = add(REFERENCE, mul(mul(first_factor, first_factor), delta))
            expected_reader = (Fraction(sign), 313 if sign == 1 else 73)
    if tick == HORIZON:
        counts["boundary"] += 1
        if sign:
            expected_a = add(REFERENCE, mul(mul(first_factor, sub(ONE, rho2)), delta))
            expected_reader = (Fraction(1, 6) if sign == 1 else Fraction(-1, 2), 163)
    result = read_pair(*recompose(pair))
    require(a == expected_a and result == expected_reader,
            f"archive and reader at {ny}/{mode}/{cut.stage}/{tick}")
    archives.add(a)
    counts["reference"] += 1
    return direct_accounts, pair, result


def check_edges(full, post_c, mode):
    ny, bit, tick = full.ny, full.bit, post_c.tick

    def edge(x):
        left = x if x % 2 == bit else (x - 1) % NX
        endpoints = tuple(index(ny, p, ny - 1, 3)
                          for p in (left, (left + 1) % NX))
        before = tuple(full.field[i] for i in endpoints)
        after = tuple(post_c.field[i] for i in endpoints)
        return even(sub(*before)), before != after

    require(edge(4) == (True, False), "fixed reference transport")
    if mode == "ABSENT_ROW0":
        require(edge(2) == (True, False), "absent archive transport")
    elif tick in (4, HORIZON):
        require(edge(2) == (True, True), "signed archive writes and unlocks")
    elif tick in range(5, HORIZON):
        require(edge(2) == (False, False), "signed archive parity lock")


def check_native_write(post_c, full, mode):
    if mode == "ABSENT_ROW0":
        return
    sign = 1 if mode == "PLUS" else -1
    r0 = scale(16, ONE)
    corr = scale(16 * sign, add(scale(2, ONE), RHO))
    if full.tick == 1:
        require(full.field[:4] == (r0, scale(-1, r0), scale(-16 * sign, RHO), corr),
                "signed primary write")
    if full.tick == 2:
        start = index(full.ny, 0, full.ny - 1, 0)
        u, rho2 = add(scale(2, ONE), RHO), mul(RHO, RHO)
        matter = scale(4, u)
        clock = scale(8 * sign, sub(rho2, RHO))
        require(post_c.field[start:start + 4] == (matter, scale(-1, matter), clock, REFERENCE),
                "signed secondary input")
        delta = add(ONE, scale(sign, sub(rho2, mul(rho2, RHO))))
        require(full.field[start + 3] == add(REFERENCE, scale(4, delta)),
                "signed secondary write")


def history(ny, mode, counts, archives):
    roles = partition(ny)
    full = prepare(ny, mode)
    encoded = encode(full)
    cuts = [full]
    observed = {("full", 0): inspect_cut(full, encoded, mode, roles, counts, archives)}
    for tick in range(1, HORIZON + 1):
        post_c, _ = advance(full)
        next_full, events = advance(post_c)
        encoded_post_c, _ = lifted_advance(encoded)
        encoded_next, lifted_events = lifted_advance(encoded_post_c)
        require(lifted_events == events, "lifted native collision observations")
        expected_events = ()
        if mode != "ABSENT_ROW0" and tick in (1, 2):
            expected_events = ((0, 0 if tick == 1 else ny - 1, 2),)
        require(events == expected_events, "native collision event profile")
        check_edges(full, post_c, mode)
        check_native_write(post_c, next_full, mode)
        cuts.extend((post_c, next_full))
        for cut, state in ((post_c, encoded_post_c), (next_full, encoded_next)):
            observed[(cut.stage, tick)] = inspect_cut(cut, state, mode, roles, counts, archives)
        full, encoded = next_full, encoded_next
        counts["steps"] += 1
    for previous in reversed(cuts[:-1]):
        full = retreat(full)
        encoded = lifted_retreat(encoded)
        require(full == decode(encoded) == previous, "complete reverse history")
        counts["inverse substeps"] += 1
    counts["histories"] += 1
    return cuts[0], observed


def compare_preparations(histories, counts):
    starts, observations = zip(*histories)
    cold = [entry[("full", 0)] for entry in observations]
    require(cold[0] == cold[1] == cold[2] and len(set(starts)) == 3,
            "matched initial accounts and pair with distinct complete fields")
    counts["matched geometries"] += 1
    for stage in ("full", "post-C"):
        for tick in (*HOLD, HORIZON):
            pairs = [entry[(stage, tick)][1] for entry in observations]
            require(len({pair.ray for pair in pairs}) == 3, "distinct anchored rays")
            one_coordinate = [factor((recompose(pair)[0],)).ray for pair in pairs]
            require(set(one_coordinate) == {(ONE,)}, "archive-only ray collapse")
            if tick == HORIZON:
                (_, q_plus), (_, q_minus) = [entry[(stage, tick)][2]
                                            for entry in observations[1:]]
                require(q_plus == q_minus == 163
                        and observations[1][stage, tick][2] != observations[2][stage, tick][2],
                        "archive ray and q do not determine signed boundary reader")
            counts["in-class comparisons"] += 1


def nonnegative(real):
    # At j = exp(2 pi i/5), phi = -(j^2+j^3) = (1+sqrt(5))/2.
    a, zero, c, match = real
    require(zero == 0 and c == match, "expected real quadratic coefficient form")
    rational = a - Fraction(c, 2)
    radical = -Fraction(c, 2)
    if rational >= 0 and radical >= 0:
        return True
    if rational < 0 and radical <= 0:
        return False
    if radical < 0:
        return rational * rational >= 5 * radical * radical
    return 5 * radical * radical >= rational * rational


def projector_audit(archives, counts):
    for exponent in (1, 2):
        beta = sigma(REFERENCE, exponent)
        reference_norm = h(beta)
        require(reference_norm == scale(64, ONE), "reference in ordered embedding")
        cases = []
        for archive in sorted(archives):
            z = sigma(archive, exponent)
            archive_norm = h(z)
            mass = add(archive_norm, reference_norm)
            reciprocal = inverse(mass)
            pair = (z, beta)
            matrix = tuple(mul(mul(pair[i], conj(pair[k])), reciprocal)
                           for i, k in product(range(2), repeat=2))
            p12, p22 = matrix[1], matrix[3]
            require(p22 == scale(64, reciprocal)
                    and mul(mul(beta, p12), inverse(p22)) == z, "anchored projector inverse")
            require(nonnegative(sub(p22, scale(Fraction(1, 429), ONE)))
                    and nonnegative(sub(p22, scale(Fraction(1, 427), ONE))),
                    "budget-controlled projector chart bounds")
            cases.append((z, mass, matrix))
            counts["projectors"] += 1
        for (z, mass, matrix), (w, other_mass, other) in combinations(cases, 2):
            observed = ring_sum(h(sub(a, b)) for a, b in zip(matrix, other))
            displacement = h(sub(z, w))
            predicted = scale(128, mul(displacement, inverse(mul(mass, other_mass))))
            require(observed == predicted, "projector Frobenius identity")
            lower = scale(Fraction(128, 27456**2), displacement)
            upper = scale(Fraction(1, 32), displacement)
            require(nonnegative(sub(observed, lower)) and nonnegative(sub(upper, observed)),
                    "projector distance bounds")
            counts["projector comparisons"] += 1


def main():
    counts, archives, final = Counter(), set(), {}
    require(recompose(factor((ZERO, ZERO))) == (ZERO, ZERO), "zero chart representation")
    for ny in HEIGHTS:
        runs = [history(ny, mode, counts, archives) for mode in MODES]
        compare_preparations(runs, counts)
        for mode, (_, observations) in zip(MODES, runs):
            readings = (observations["full", HOLD.start][2], observations["full", HORIZON][2])
            if mode in final:
                require(final[mode] == readings, "geometry-independent finite readers")
            final[mode] = readings
    require(len(archives) == 5, "five distinct archive values")
    projector_audit(archives, counts)

    sys.stdout.reconfigure(newline="\n")
    print("H3 fixed-reference record")
    print("geometry: 8 x 4, 8 x 6")
    print(f"histories={counts['histories']} full={counts['full']} post-C={counts['post-C']} "
          f"steps={counts['steps']} inverse-substeps={counts['inverse substeps']}")
    print(f"reference-cuts={counts['reference']} hold-cuts={counts['hold']} "
          f"boundary-cuts={counts['boundary']} matched-geometries={counts['matched geometries']} "
          f"in-class-comparisons={counts['in-class comparisons']}")
    print(f"Q={GLOBAL[3]} reference-q={scalar_account(h(REFERENCE))}")
    for mode, ((held, hold_q), (boundary, boundary_q)) in final.items():
        print(f"{mode} hold-R={held} hold-q={hold_q} cut14-R={boundary} cut14-q={boundary_q}")
    print(f"projectors={counts['projectors']} comparisons={counts['projector comparisons']} "
          "P22>=1/427 (also >=1/429)")
    print("PASS")


if __name__ == "__main__":
    main()
