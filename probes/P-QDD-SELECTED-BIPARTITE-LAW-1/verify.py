#!/usr/bin/env python3
"""Exact audit of the selected bipartite QDD law; no physical data.

All arithmetic is rational.  Rational matrix units also span the complex
operator algebra, so the audited complex-linear identities are unrestricted
by the use of real fixtures.  Positivity and complete positivity follow from
the displayed Gram, pure-state, convex-mixture and Kraus constructions;
finite state fixtures are not substitutes for the written universal proof.
No imports of predecessor verifiers, runtime files, random draws or floats.
"""

from fractions import Fraction as F
from itertools import product


def matrix(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def zeros(n, m=None):
    return matrix([[0] * (n if m is None else m) for _ in range(n)])


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def add(a, b):
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    return tuple(tuple(x + y for x, y in zip(ar, br))
                 for ar, br in zip(a, b))


def scale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def sub(a, b):
    return add(a, scale(-1, b))


def total(items, n):
    out = zeros(n)
    for item in items:
        out = add(out, item)
    return out


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    assert len(a[0]) == len(b)
    out = [[F(0) for _ in b[0]] for _ in a]
    for i, ar in enumerate(a):
        for k, x in enumerate(ar):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x * y
    return tuple(tuple(row) for row in out)


def power(a, n):
    assert n >= 0 and len(a) == len(a[0])
    out = identity(len(a))
    for _ in range(n):
        out = mul(out, a)
    return out


def trace(a):
    assert len(a) == len(a[0])
    return sum((a[i][i] for i in range(len(a))), F(0))


def pairing(a, b):
    """tr(a b), independently contracted without constructing the product."""
    assert len(a) == len(b) and len(a[0]) == len(b[0]) == len(a)
    return sum((a[i][j] * b[j][i]
                for i in range(len(a)) for j in range(len(a))
                if a[i][j] and b[j][i]), F(0))


def rank(a):
    rows = [list(row) for row in a]
    pivot = 0
    for col in range(len(rows[0])):
        chosen = next((i for i in range(pivot, len(rows)) if rows[i][col]),
                      None)
        if chosen is None:
            continue
        rows[pivot], rows[chosen] = rows[chosen], rows[pivot]
        divisor = rows[pivot][col]
        rows[pivot] = [x / divisor for x in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [x - factor * y
                           for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def unit(n, i, j):
    return matrix([[int(a == i and b == j) for b in range(n)]
                   for a in range(n)])


def kron(a, b):
    return tuple(tuple(a[i][j] * b[k][l]
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def partial_a(x):
    """Trace out B, retaining A, in operator rather than covariance coordinates."""
    assert len(x) == len(x[0]) == 16
    return matrix([[sum(x[4 * i + k][4 * j + k] for k in range(4))
                    for j in range(4)] for i in range(4)])


def partial_b(x):
    """Trace out A, retaining B."""
    assert len(x) == len(x[0]) == 16
    return matrix([[sum(x[4 * k + i][4 * k + j] for k in range(4))
                    for j in range(4)] for i in range(4)])


def sharp(a, gram, gram_inv):
    return mul(mul(gram_inv, transpose(a)), gram)


def pure(v, gram):
    ket = matrix([[x] for x in v])
    bra = mul(transpose(ket), gram)
    norm = mul(bra, ket)[0][0]
    if norm == 0:
        assert all(x == 0 for x in v), "zero norm in a positive Gram space"
        return None
    assert norm > 0
    return scale(1 / norm, mul(ket, bra))


def normalized(rho):
    weight = trace(rho)
    assert weight >= 0
    if weight == 0:
        assert rho == zeros(len(rho)), "nonphysical zero-trace branch"
        return None
    return scale(1 / weight, rho)


def sandwich(p, x):
    return mul(mul(p, x), p)


def local_policy(which, history):
    assert which in (0, 1)
    if which == 0:
        return (len(history) + sum((i + 1) * bit
                                   for i, bit in enumerate(history))) % 5
    return (2 + 2 * len(history) + sum((i + 2) * bit
                                      for i, bit in enumerate(history))) % 5


def local_tree(which, effects, gram, gram_inv, depth):
    """Only own recorded history controls settings; no remote input exists."""
    unit4 = identity(4)
    chains = {(): unit4}
    branch_effects = {(): unit4}
    for d in range(depth):
        for history in product((0, 1), repeat=d):
            setting = local_policy(which, history)
            for outcome in (0, 1):
                child = history + (outcome,)
                k = mul(effects[setting][outcome], chains[history])
                chains[child] = k
                branch_effects[child] = mul(sharp(k, gram, gram_inv), k)
            assert add(branch_effects[history + (0,)],
                       branch_effects[history + (1,)]) == branch_effects[history]
    leaves = tuple(product((0, 1), repeat=depth))
    assert total((branch_effects[h] for h in leaves), 4) == unit4
    return chains, branch_effects


def main():
    i4, i16 = identity(4), identity(16)
    j4 = matrix([[1] * 4 for _ in range(4)])
    gram = sub(i4, scale(F(1, 5), j4))
    gram_inv = add(i4, j4)
    metric, metric_inv = kron(gram, gram), kron(gram_inv, gram_inv)
    r = matrix([[0, 0, 0, -1], [1, 0, 0, -1],
                [0, 1, 0, -1], [0, 0, 1, -1]])
    p0 = scale(F(1, 4), j4)
    ps = tuple(mul(mul(power(r, k), p0), power(r, (5 - k) % 5))
               for k in range(5))
    effects = tuple((p, sub(i4, p)) for p in ps)
    phi = tuple(gram_inv[i][j] / 2 for i in range(4) for j in range(4))
    rho = pure(phi, metric)
    mixture = scale(F(1, 16), i16)
    other_vector = tuple(F(int(i in (0, 5))) for i in range(16))
    fixtures = (rho, mixture, kron(ps[0], ps[1]), pure(other_vector, metric))

    # G1. Positive Gram decomposition and exact metric-normalized source.
    assert mul(gram, gram_inv) == i4
    assert mul(metric, metric_inv) == i16
    for n in range(1, 5):
        assert F(1) - F(n, 5) > 0  # eigenvalue of I_n-J_n/5 on ones
    assert power(r, 5) == i4 and sharp(r, gram, gram_inv) == power(r, 4)
    for x, pair in enumerate(effects):
        assert add(*pair) == i4
        for a, p in enumerate(pair):
            assert mul(p, p) == p and sharp(p, gram, gram_inv) == p
            assert rank(p) == (1 if a == 0 else 3)
        assert mul(*pair) == zeros(4)
        for y, q in enumerate(ps):
            assert pairing(pair[0], q) == (F(1) if x == y else F(1, 16))
    assert total(ps, 4) == scale(F(5, 4), i4)
    ket = matrix([[x] for x in phi])
    assert mul(mul(transpose(ket), metric), ket)[0][0] == 1
    assert mul(rho, rho) == rho and rank(rho) == 1
    assert partial_a(rho) == partial_b(rho) == scale(F(1, 4), i4)
    assert len(set(fixtures)) == 4
    for state in fixtures:
        assert trace(state) == 1 and sharp(state, metric, metric_inv) == state
    assert pure((0,) * 16, metric) is None
    print("G1 PASS: tensor Gram, five contexts, four sources and normalized Phi")

    # G2. The direct 16-dimensional branch agrees with independent scalar
    # trace contraction.  Commutation is checked before taking probabilities.
    branches, table = {}, {}
    for x, y in product(range(5), repeat=2):
        complete = zeros(16)
        for a, b in product((0, 1), repeat=2):
            left = kron(effects[x][a], i4)
            right = kron(i4, effects[y][b])
            k = kron(effects[x][a], effects[y][b])
            assert mul(left, right) == mul(right, left) == k
            assert sharp(k, metric, metric_inv) == k and mul(k, k) == k
            complete = add(complete, mul(k, k))
            out = sandwich(k, rho)
            probability = trace(out)
            assert probability == pairing(k, rho) and probability >= 0
            expected = ((F(1, 4), F(0), F(0), F(3, 4)) if x == y
                        else (F(1, 64), F(15, 64), F(15, 64), F(33, 64)))
            assert probability == expected[2 * a + b]
            if probability == 0:
                assert normalized(out) is None
            else:
                assert trace(normalized(out)) == 1
            branches[x, y, a, b], table[x, y, a, b] = k, probability
        assert complete == i16
        assert sum(table[x, y, a, b] for a, b in product((0, 1), repeat=2)) == 1
        assert sum(table[x, y, 0, b] for b in (0, 1)) == F(1, 4)
        assert sum(table[x, y, a, 0] for a in (0, 1)) == F(1, 4)
    assert len(table) == 100
    joint_record_law = {key: probability / 25 for key, probability in table.items()}
    assert sum(joint_record_law.values()) == 1
    for x, y in product(range(5), repeat=2):
        assert sum(joint_record_law[x, y, a, b]
                   for a, b in product((0, 1), repeat=2)) == F(1, 25)
    print("G2 PASS: 100 exact branches, joint table, commuting order and completeness")

    # G3. Factorized matrix units span all 16-by-16 matrices.  Compute the
    # remote channel and actual partial trace, not merely its trace-preserving
    # scalar formula.  This audits both directions at every remote setting.
    units4 = tuple(unit(4, i, j) for i in range(4) for j in range(4))
    unit_checks = 0
    for setting in range(5):
        images = tuple(total((sandwich(p, u) for p in effects[setting]), 4)
                       for u in units4)
        for ia, ib in product(range(16), repeat=2):
            original = kron(units4[ia], units4[ib])
            assert partial_a(kron(units4[ia], images[ib])) == partial_a(original)
            assert partial_b(kron(images[ia], units4[ib])) == partial_b(original)
            unit_checks += 1
    assert unit_checks == 1280
    for state in fixtures:
        ma, mb = partial_a(state), partial_b(state)
        for x, y in product(range(5), repeat=2):
            probabilities = {(a, b): pairing(branches[x, y, a, b], state)
                             for a, b in product((0, 1), repeat=2)}
            assert all(p >= 0 for p in probabilities.values())
            for a in (0, 1):
                assert sum(probabilities[a, b] for b in (0, 1)) == pairing(effects[x][a], ma)
            for b in (0, 1):
                assert sum(probabilities[a, b] for a in (0, 1)) == pairing(effects[y][b], mb)
    print("G3 PASS: both no-signalling identities on 256 units at five settings and four sources")

    # G4. Exhaustive deterministic local vertices; shared-random convex
    # combinations follow from linearity in the written proof.
    classical = []
    strategies = tuple(product((0, 1), repeat=5))
    for alice, bob in product(strategies, repeat=2):
        direct = (2 * sum(alice[x] * bob[x] for x in range(5))
                  - sum(alice[x] * bob[y] for x in range(5)
                        for y in range(5) if x != y))
        c = sum(alice[x] * bob[x] for x in range(5))
        assert direct == 3 * c - sum(alice) * sum(bob)
        classical.append(direct)
    assert len(classical) == 1024 and max(classical) == 2
    bell = (2 * sum(table[x, x, 0, 0] for x in range(5))
            - sum(table[x, y, 0, 0] for x in range(5)
                  for y in range(5) if x != y))
    assert bell == F(35, 16) > 2
    print("G4 PASS: 1024 deterministic local strategies bounded by 2; Phi gives 35/16")

    # G5. Rational spectral projectors certify the global maximum over all
    # complex density operators for these fixed effects, not for all settings.
    t = total((kron(p, p) for p in ps), 16)
    bop = total((scale(2 if x == y else -1, branches[x, y, 0, 0])
                 for x, y in product(range(5), repeat=2)), 16)
    assert bop == sub(scale(3, t), scale(F(25, 16), i16))
    top = scale(F(64, 25), mul(t, sub(t, scale(F(15, 16), i16))))
    middle = scale(F(-256, 75), mul(t, sub(t, scale(F(5, 4), i16))))
    bottom = sub(sub(i16, top), middle)
    spectral = ((top, F(35, 16), 1), (middle, F(5, 4), 4),
                (bottom, F(-25, 16), 11))
    for projection, value, multiplicity in spectral:
        assert mul(projection, projection) == projection
        assert sharp(projection, metric, metric_inv) == projection
        assert rank(projection) == trace(projection) == multiplicity
        assert mul(bop, projection) == scale(value, projection)
    for i, j in product(range(3), repeat=2):
        if i != j:
            assert mul(spectral[i][0], spectral[j][0]) == zeros(16)
    assert total((s[0] for s in spectral), 16) == i16
    assert total((scale(s[1], s[0]) for s in spectral), 16) == bop
    assert top == rho and pairing(bop, rho) == bell
    print("G5 PASS: fixed-operator spectrum 35/16 (1), 5/4 (4), -25/16 (11); unique top Phi")

    # G6. All ordered setting quadruples, repetitions included, and all
    # eight CHSH odd-sign forms.  CHSH nonviolation does not negate G4.
    correlations = {(x, y): sum((-1) ** (a + b) * table[x, y, a, b]
                               for a, b in product((0, 1), repeat=2))
                    for x, y in product(range(5), repeat=2)}
    assert all(e == (1 if x == y else F(1, 16))
               for (x, y), e in correlations.items())
    signs = tuple(s for s in product((-1, 1), repeat=4)
                  if s[0] * s[1] * s[2] * s[3] == -1)
    chsh_values = []
    for x0, x1, y0, y1 in product(range(5), repeat=4):
        entries = (correlations[x0, y0], correlations[x0, y1],
                   correlations[x1, y0], correlations[x1, y1])
        for s in signs:
            chsh_values.append(sum(sign * e for sign, e in zip(s, entries)))
    assert len(chsh_values) == 5000 and max(map(abs, chsh_values)) == 2
    print("G6 PASS: all 5000 CHSH forms have absolute value at most 2")

    # G7. A declared white-noise line, not a claim about every noise model.
    assert pairing(bop, mixture) == F(-5, 8)
    noise_values = {}
    for visibility in (F(0), F(9, 10), F(14, 15), F(19, 20), F(1)):
        state = add(scale(visibility, rho), scale(1 - visibility, mixture))
        for x, y in product(range(5), repeat=2):
            weights = []
            for a, b in product((0, 1), repeat=2):
                weight = pairing(branches[x, y, a, b], state)
                rank_product = (1 if a == 0 else 3) * (1 if b == 0 else 3)
                assert weight == (visibility * table[x, y, a, b]
                                  + (1 - visibility) * F(rank_product, 16))
                assert weight >= 0
                weights.append(weight)
            assert sum(weights) == 1
        value = pairing(bop, state)
        assert value == (45 * visibility - 10) / 16
        assert (value > 2) == (visibility > F(14, 15))
        noise_values[visibility] = value
    assert noise_values[F(14, 15)] == 2
    print("G7 PASS: white-noise Bell value (45v-10)/16 and threshold v > 14/15")

    # G8. Four local policy pairs, four sources, 64 joint leaves each.
    # Every prefix is checked too.  A remote policy can alter joint records
    # while its unconditioned sum leaves the other record law unchanged.
    trees = tuple(local_tree(which, effects, gram, gram_inv, 3)
                  for which in (0, 1))
    leaves = tuple(product((0, 1), repeat=3))
    leaf_count, node_count = 0, 0
    for state in fixtures:
        distributions = {}
        for wa, wb in product((0, 1), repeat=2):
            ea, eb = trees[wa][1], trees[wb][1]
            probabilities = {}
            for depth in range(4):
                words = tuple(product((0, 1), repeat=depth))
                for ha, hb in product(words, repeat=2):
                    value = pairing(kron(ea[ha], eb[hb]), state)
                    assert value >= 0
                    probabilities[ha, hb] = value
                    node_count += 1
                assert sum(probabilities[ha, hb]
                           for ha, hb in product(words, repeat=2)) == 1
            for depth in range(3):
                for ha, hb in product(tuple(product((0, 1), repeat=depth)), repeat=2):
                    assert sum(probabilities[ha + (a,), hb + (b,)]
                               for a, b in product((0, 1), repeat=2)) == probabilities[ha, hb]
            distributions[wa, wb] = probabilities
            for ha in leaves:
                assert sum(probabilities[ha, hb] for hb in leaves) == pairing(ea[ha], partial_a(state))
            for hb in leaves:
                assert sum(probabilities[ha, hb] for ha in leaves) == pairing(eb[hb], partial_b(state))
            leaf_count += len(leaves) ** 2
        for policy in (0, 1):
            for history in leaves:
                assert sum(distributions[policy, 0][history, h] for h in leaves) == sum(distributions[policy, 1][history, h] for h in leaves)
                assert sum(distributions[0, policy][h, history] for h in leaves) == sum(distributions[1, policy][h, history] for h in leaves)
    assert leaf_count == 1024 and node_count == 1360
    # Retained pair versus a full new pair.  Resetting a pointer leaves the
    # retained pair unchanged and therefore cannot realize the fresh law.
    retained, fresh = {}, {}
    for a, b, c, d in product((0, 1), repeat=4):
        first = sandwich(branches[0, 1, a, b], rho)
        old_second = sandwich(branches[0, 1, c, d], first)
        new_second = sandwich(branches[0, 1, c, d], scale(trace(first), rho))
        retained[a, b, c, d] = trace(old_second)
        fresh[a, b, c, d] = trace(new_second)
        assert trace(old_second) == (table[0, 1, a, b] if (a, b) == (c, d) else 0)
        assert trace(new_second) == table[0, 1, a, b] * table[0, 1, c, d]
    assert sum(retained.values()) == sum(fresh.values()) == 1
    assert retained[0, 0, 0, 1] == 0 < fresh[0, 0, 0, 1]
    print("G8 PASS: 1024 adaptive joint leaves, 1360 prefix pairs, both policy marginals and renewal")

    # G9. Selective steering changes conditioned states but not their mean.
    for y in range(5):
        average = zeros(4)
        for b in (0, 1):
            branch = sandwich(kron(i4, effects[y][b]), rho)
            reduced = partial_a(branch)
            expected = scale(F(1, 1 if b == 0 else 3), effects[y][b])
            assert normalized(reduced) == expected
            average = add(average, reduced)
        assert average == scale(F(1, 4), i4)
    # Setting-dependent separable preparations can duplicate this whole
    # probability table.  Each state is positive by this convex product form.
    # They fail the fixed, setting-independent source premise of the theorem.
    dependent_sources = {}
    for x, y in product(range(5), repeat=2):
        state = total((scale(table[x, y, a, b] / ((1 if a == 0 else 3) *
                                                  (1 if b == 0 else 3)),
                             branches[x, y, a, b])
                       for a, b in product((0, 1), repeat=2)), 16)
        assert trace(state) == 1 and sharp(state, metric, metric_inv) == state
        assert partial_a(state) == partial_b(state) == scale(F(1, 4), i4)
        for a, b in product((0, 1), repeat=2):
            assert pairing(branches[x, y, a, b], state) == table[x, y, a, b]
        dependent_sources[x, y] = state
    assert dependent_sources[0, 0] != dependent_sources[0, 1]
    print("G9 PASS: steering averages unchanged; 25 dependent separable sources expose independence premise")

    # G10. Actual communication is outside no-message control.  Bob sends
    # his outcome at setting 0; Alice uses setting 0 on LOW, 1 on HIGH.
    # This permitted communication genuinely changes Alice's total LOW law.
    communicated = F(0)
    fixed = F(0)
    for b in (0, 1):
        bob_branch = sandwich(kron(i4, effects[0][b]), rho)
        communicated += trace(sandwich(kron(effects[b][0], i4), bob_branch))
        fixed += trace(sandwich(kron(effects[0][0], i4), bob_branch))
    assert communicated == F(31, 64) and fixed == F(1, 4)
    assert communicated != fixed
    selective = tuple(normalized(partial_a(sandwich(kron(i4, p), rho)))
                      for p in effects[0])
    assert tuple(pairing(ps[0], state) for state in selective) == (1, 0)
    assert pairing(ps[0], partial_a(rho)) == F(1, 4)
    for y in (0, 1):
        selected_low = normalized(partial_a(sandwich(kron(i4, ps[y]), rho)))
        assert pairing(ps[0], selected_low) == (F(1) if y == 0 else F(1, 16))
        unselected = total((partial_a(sandwich(kron(i4, p), rho))
                            for p in effects[y]), 4)
        assert pairing(ps[0], unselected) == F(1, 4)
    # A second distinct boundary: Bob's message is encoded in Alice's
    # preparation itself.  Holding the source law fixed was then violated.
    message_sources = (ps[0], scale(F(1, 3), effects[0][1]))
    assert tuple(pairing(ps[0], state) for state in message_sources) == (1, 0)
    assert normalized(sandwich(branches[0, 0, 0, 1], rho)) is None
    print("G10 PASS: explicit message gives 31/64 versus 1/4; source messages give 1 versus 0; zero guarded")
    print("VERDICT: SELECTED-BIPARTITE-LAW; conditional theorem, tensor source and Born law adopted")


if __name__ == "__main__":
    main()
