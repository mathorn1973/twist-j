#!/usr/bin/env python3
"""NON-CANONICAL exact audit of the frozen source-table classes.

Primary method: construct all reversible controls from independent orbit
permutations, and inspect all Cartesian products of reference permutations.
No repository verifier is imported. See PREREG.md for scope and ceilings.
"""

import hashlib
import itertools
import json
from collections import Counter, defaultdict


F = range(5)
S3 = tuple(itertools.permutations(range(3)))
S4 = tuple(itertools.permutations(range(4)))
J = (2, 3, 0, 1)


def require(condition, label, witness=None):
    if not condition:
        raise AssertionError((label, witness))


def inv(p):
    answer = [0] * len(p)
    for i, j in enumerate(p):
        answer[j] = i
    return tuple(answer)


def b(x):
    p1, p4, p1p, p4p, q, r = x
    return (-p1p % 5, -p4p % 5, -p1 % 5, -p4 % 5, -q % 5, -r % 5)


def d(x):
    return tuple((a - z) % 5 for a, z in zip((2, 1, 3, 4, 1, 1), x))


def e(x):
    return tuple((a - z) % 5 for a, z in zip((2, 1, 3, 4, 2, 1), x))


def det(p):
    return (p[0] * p[3] - p[1] * p[2]) % 5


def mixed(x, y):
    return (3 * (det(tuple((a + z) % 5 for a, z in zip(x, y)))
                 - det(x) - det(y))) % 5


def piston_b(p):
    return (-p[2] % 5, -p[3] % 5, -p[0] % 5, -p[1] % 5)


def source_audit():
    for cell in itertools.product(F, repeat=6):
        plus = cell[:4] + ((cell[4] + 1) % 5, cell[5])
        minus = cell[:4] + ((cell[4] - 1) % 5, cell[5])
        require(b(b(cell)) == d(d(cell)) == e(e(cell)) == cell,
                "native involutions", cell)
        require(e(d(cell)) == plus and d(e(cell)) == minus,
                "literal tau and inverse", cell)
        require(b(e(d(b(cell)))) == minus,
                "b tau b = tau inverse", cell)
    pistons = tuple(itertools.product(F, repeat=4))
    transformed = {p: piston_b(p) for p in pistons}
    for x in pistons:
        for y in pistons:
            require(mixed(transformed[x], transformed[y]) == -mixed(x, y) % 5,
                    "mixed source reading sign", (x, y))


def orbit_permutation(table, k):
    out = []
    for u, eta in itertools.product(range(2), repeat=2):
        h = (k if u == 0 else -k) % 5
        a, beta = divmod(table[2 * h + eta], 2)
        out.append(2 * (u ^ a) + beta)
    return tuple(out)


def all_controls():
    """Each zero-sheet map centralizes J; each other pair is an S4 map."""
    zero_options = []
    for beta in itertools.permutations(range(2)):
        for aa in itertools.product(range(2), repeat=2):
            zero_options.append(tuple(2 * aa[eta] + beta[eta] for eta in range(2)))
    for zero, p1, p2 in itertools.product(zero_options, S4, S4):
        table = list(zero) + [None] * 8
        for k, p in ((1, p1), (2, p2)):
            for u, eta in itertools.product(range(2), repeat=2):
                v, zeta = divmod(p[2 * u + eta], 2)
                h = (k if u == 0 else -k) % 5
                table[2 * h + eta] = 2 * (u ^ v) + zeta
        yield tuple(table)


def inverse_table(table):
    answer = [None] * 10
    for h, eta in itertools.product(F, range(2)):
        a, beta = divmod(table[2 * h + eta], 2)
        target_h = (-h if a else h) % 5
        target = 2 * target_h + beta
        require(answer[target] is None, "table inverse collision", table)
        answer[target] = 2 * a + eta
    require(None not in answer, "table inverse missing entry", table)
    return tuple(answer)


def shift_index(index, port, delta):
    pos, qq = divmod(index, 25)
    qx, qy = divmod(qq, 5)
    if port == 0:
        qx = (qx + delta) % 5
    else:
        qy = (qy + delta) % 5
    return 25 * pos + 5 * qx + qy


def lift_positions(p):
    """Full q lift forced by the parity of the literal I action."""
    result = []
    for pos in range(4):
        target = p[pos]
        sign = -1 if pos // 2 != target // 2 else 1
        for qx, qy in itertools.product(F, repeat=2):
            result.append(25 * target + 5 * (sign * qx % 5) + sign * qy % 5)
    return tuple(result)


def reduced_contact(table):
    chi = {}
    involutive = True
    for k in (0, 1, 2):
        p = orbit_permutation(table, k)
        require(sorted(p) == list(range(4)), "orbit permutation", (table, k))
        involutive &= all(p[p[v]] == v for v in range(4))
        pp, jp, ip = lift_positions(p), lift_positions(J), lift_positions(inv(p))
        ee = tuple(pp[jp[ip[z]]] for z in range(100))
        require(all(ee[ee[z]] == z for z in range(100)),
                "complete reduced E involution", (table, k))
        responses = set()
        for z in range(100):
            for port in range(2):
                out = ee[shift_index(ee[shift_index(z, port, -1)], port, 1)]
                back = shift_index(ee[shift_index(ee[z], port, -1)], port, 1)
                if out == z:
                    active = 0
                elif out == shift_index(z, port, 3):
                    active = 1
                else:
                    raise AssertionError(("unanticipated full contact", table, k, z, port, out))
                require(back == shift_index(z, port, -3 * active),
                        "complete reduced inverse", (table, k, z, port))
                responses.add(active)
        require(len(responses) == 1, "sheet-independent contact", (table, k, responses))
        chi[k] = next(iter(responses))
    require(chi[0] == 1, "zero-sheet contact", table)
    return str(chi[1]) + str(chi[2]), bool(involutive)


def native_I(state):
    return b(state[:6]) + b(state[6:12]) + state[12:]


def native_W(state, table):
    h = mixed(state[:4], state[6:10])
    a, beta = divmod(table[2 * h + state[12]], 2)
    out = native_I(state) if a else state
    return out[:12] + (beta,)


def native_tau(state, port, direction):
    start = 6 * port
    cell = state[start:start + 6]
    cell = e(d(cell)) if direction == 1 else d(e(cell))
    return state[:start] + cell + state[start + 6:]


def native_E(state, table, inverse):
    return native_W(native_I(native_W(state, inverse)), table)


def native_K(state, port, table, inverse, backward=False):
    if backward:
        state = native_E(state, table, inverse)
        state = native_tau(state, port, -1)
        state = native_E(state, table, inverse)
        return native_tau(state, port, 1)
    state = native_tau(state, port, -1)
    state = native_E(state, table, inverse)
    state = native_tau(state, port, 1)
    return native_E(state, table, inverse)


def native_witness_audit(table, profile):
    inverse = inverse_table(table)
    for h, eta, port, qi in itertools.product(F, range(2), range(2), F):
        qx, qy = (qi, 2) if port == 0 else (2, qi)
        state = (1, 0, 0, 0, qx, 1, 0, 0, 0, 2 * h % 5, qy, 2, eta)
        require(mixed(state[:4], state[6:10]) == h, "faithful h witness", h)
        require(native_I(state)[:4] != state[:4], "faithful I witness", h)
        require(native_W(native_W(state, table), inverse) == state,
                "full native W inverse", (table, state))
        active = 1 if h == 0 else int(profile[0 if h in (1, 4) else 1])
        slot = 6 * port + 4
        expected = list(state)
        expected[slot] = (expected[slot] + 3 * active) % 5
        out = native_K(state, port, table, inverse)
        require(out == tuple(expected), "literal native K", (table, state, port, out))
        expected[slot] = (state[slot] - 3 * active) % 5
        back = native_K(state, port, table, inverse, backward=True)
        require(back == tuple(expected), "literal native inverse K", (table, state, port, back))


def control_census():
    seen = set()
    rows = []
    laws, involutive_laws = Counter(), Counter()
    for table in all_controls():
        require(table not in seen, "duplicate orbit construction", table)
        seen.add(table)
        profile, involutive = reduced_contact(table)
        native_witness_audit(table, profile)
        rows.append("".join(map(str, table)) + "\t" + profile + "\t" + str(int(involutive)) + "\n")
        laws[profile] += 1
        if involutive:
            involutive_laws[profile] += 1
    # Regression embedding only; this is not an admission filter.
    wb = (0, 1, 0, 2, 0, 2, 3, 1, 3, 1)
    require(wb in seen and reduced_contact(wb) == ("00", True), "old W_b embedding")
    polynomials = {}
    for profile in sorted(laws):
        c1, c2 = map(int, profile)
        coefficients = [1, 2 * (c2 - c1) % 5, (3 * (c1 + c2) - 1) % 5]
        for h in F:
            value = sum(c * pow(h, p, 5) for c, p in zip(coefficients, (0, 2, 4))) % 5
            intended = 1 if h == 0 else int(profile[0 if h in (1, 4) else 1])
            require(value == intended, "even interpolation", (profile, h))
        polynomials[profile] = coefficients
    return {
        "total": len(seen),
        "involutive": sum(involutive_laws.values()),
        "law_counts": dict(sorted(laws.items())),
        "involutive_law_counts": dict(sorted(involutive_laws.items())),
        "even_polynomials": polynomials,
        "census_sha256": hashlib.sha256("".join(sorted(rows)).encode("ascii")).hexdigest(),
    }


def reference_value(p, r):
    return p[r] if r < 3 else r


def table_shift(table, t):
    return tuple(table[(q + t) % 5] for q in F)


def left_relabel(table, ell):
    return tuple(tuple(ell[r] for r in p) for p in table)


def endpoint(table):
    inverse = tuple(inv(p) for p in table)
    return tuple(tuple(inverse[(q + 3) % 5][table[q][r]] for r in range(3)) for q in F)


def orbit_count(items, action):
    remaining = set(items)
    count = 0
    while remaining:
        item = min(remaining)
        orbit = set(action(item))
        require(orbit <= set(items), "action leaves admitted set", item)
        remaining.difference_update(orbit)
        count += 1
    return count


def reader_census(law_profiles):
    admitted = set()
    involutive = set()
    fibres = defaultdict(set)
    rows = []
    for table in itertools.product(S3, repeat=5):
        inverse = tuple(inv(p) for p in table)
        if any(inverse[(q + 3) % 5][table[q][0]] != 1 for q in F):
            continue
        admitted.add(table)
        is_involution = table == inverse
        if is_involution:
            involutive.add(table)
        signature = endpoint(table)
        fibres[signature].add(table)
        flat = "".join(str(r) for p in table for r in p)
        sig = "".join(str(r) for p in signature for r in p)
        rows.append(flat + "\t" + sig + "\t" + str(int(is_involution)) + "\n")
        for profile, h, q, r in itertools.product(law_profiles, F, F, F):
            active = 1 if h == 0 else int(profile[0 if h in (1, 4) else 1])
            q1 = (q + 3 * active) % 5
            r1 = reference_value(inverse[q1], reference_value(table[q], r))
            recovered = reference_value(inverse[q], reference_value(table[q1], r1))
            require(recovered == r, "complete occupied reader inverse", (table, profile, h, q, r))
            require((q1 - 3 * active) % 5 == q, "occupied reader q inverse")
            if r == 0:
                require(r1 == active, "prepared contact readout", (table, profile, h, q))
            if active == 0:
                require(r1 == r, "identity experiment on all references", (table, q, r))
            if r >= 3:
                require(r1 == r, "inactive reference labels", (table, q, r))
    known = ((0, 2, 1), (0, 1, 2), (2, 1, 0), (1, 0, 2), (1, 0, 2))
    require(known in involutive, "old reference-table embedding")
    require(all(table_shift(known, t) in involutive for t in F), "old q translates")
    for table in admitted:
        ept = endpoint(table)
        internal = {left_relabel(table, ell) for ell in S3}
        require(internal == fibres[ept], "exact endpoint fibre equals internal orbit", table)
        require(len(internal) == len(S3), "free internal action", table)
        q_orbit = {table_shift(table, t) for t in F}
        require(len(q_orbit) == 5, "free q-translation action", table)
        joint = {left_relabel(table_shift(table, t), ell) for t in F for ell in S3}
        require(len(joint) == 5 * len(S3), "free joint action", table)
        for t in F:
            require(endpoint(table_shift(table, t)) == table_shift(ept, t),
                    "endpoint q conjugacy", (table, t))
    for ept in fibres:
        require(len({table_shift(ept, t) for t in F}) == 5,
                "free endpoint q action", ept)
    return {
        "total": len(admitted),
        "involutive": len(involutive),
        "table_q_orbits": orbit_count(admitted, lambda p: (table_shift(p, t) for t in F)),
        "endpoint_maps": len(fibres),
        "endpoint_q_orbits": orbit_count(fibres, lambda p: (table_shift(p, t) for t in F)),
        "involutive_q_orbits": orbit_count(involutive, lambda p: (table_shift(p, t) for t in F)),
        "internal_orbits": orbit_count(admitted, lambda p: (left_relabel(p, ell) for ell in S3)),
        "joint_orbits": orbit_count(admitted, lambda p: (left_relabel(table_shift(p, t), ell)
                                                       for t in F for ell in S3)),
        "census_sha256": hashlib.sha256("".join(sorted(rows)).encode("ascii")).hexdigest(),
    }


def main():
    source_audit()
    controls = control_census()
    readers = reader_census(tuple(controls["law_counts"]))
    print(json.dumps({"status": "PASS", "controls": controls, "readers": readers},
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
