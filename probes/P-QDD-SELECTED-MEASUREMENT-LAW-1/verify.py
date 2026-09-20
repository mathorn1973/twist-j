#!/usr/bin/env python3
"""Exact certificates for a selected measurement law; no laboratory claim.

All entries are rational.  Matrix units span the complex operator algebra too,
so equality of these complex-linear maps is checked without floating complex
arithmetic.  Positivity and complete positivity use the displayed Gram/Kraus
factorizations and the written proof, not a finite sample of density matrices.
This file has no runtime dependency on authority files or external data.
"""

from fractions import Fraction as F
from itertools import permutations, product


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


def flatten(a):
    return tuple(x for row in a for x in row)


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


def inverse(a):
    n = len(a)
    assert n == len(a[0])
    unit = identity(n)
    rows = [list(a[i] + unit[i]) for i in range(n)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if rows[i][col]), None)
        assert pivot is not None, "singular inverse"
        rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [x / divisor for x in rows[col]]
        for i in range(n):
            if i != col:
                factor = rows[i][col]
                rows[i] = [x - factor * y
                           for x, y in zip(rows[i], rows[col])]
    return tuple(tuple(row[n:]) for row in rows)


def column(v):
    return matrix([[x] for x in v])


def sharp(a, gram):
    return mul(mul(inverse(gram), transpose(a)), gram)


def pure(v, gram):
    ket = column(v)
    bra = mul(transpose(ket), gram)
    norm = mul(bra, ket)[0][0]
    if norm == 0:
        assert all(x == 0 for x in v), "zero norm in positive Gram space"
        return None  # ZERO_SUPPORT; no division and no outcome draw.
    assert norm > 0
    return scale(1 / norm, mul(ket, bra))


def normalized(rho):
    weight = trace(rho)
    assert weight >= 0
    if weight == 0:
        assert rho == zeros(len(rho)), "nonphysical zero-trace branch"
        return None
    return scale(1 / weight, rho)


def unit(n, i, j):
    return matrix([[int(a == i and b == j) for b in range(n)]
                   for a in range(n)])


def units(n):
    return tuple(unit(n, i, j) for i in range(n) for j in range(n))


def kron(a, b):
    return tuple(tuple(a[i][j] * b[k][l]
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def partial_left(a, left, right):
    assert len(a) == left * right and len(a[0]) == left * right
    return matrix([[sum(a[i * right + k][i * right + l]
                        for i in range(left))
                    for l in range(right)] for k in range(right)])


def partial_right(a, left, right):
    assert len(a) == left * right and len(a[0]) == left * right
    return matrix([[sum(a[i * right + k][j * right + k]
                        for k in range(right))
                    for j in range(left)] for i in range(left)])


def sandwich(p, x):
    return mul(mul(p, x), p)


def channel(kraus, x, gram):
    out = zeros(len(x))
    for k in kraus:
        out = add(out, mul(mul(k, x), sharp(k, gram)))
    return out


def main():
    i4 = identity(4)
    j4 = matrix([[1] * 4 for _ in range(4)])
    gram = sub(i4, scale(F(1, 5), j4))
    gram_inv = add(i4, j4)
    r = matrix([[0, 0, 0, -1], [1, 0, 0, -1],
                [0, 1, 0, -1], [0, 0, 1, -1]])
    p0 = scale(F(1, 4), j4)
    ps = tuple(mul(mul(power(r, k), p0), power(r, (5 - k) % 5))
               for k in range(5))
    qs = tuple(sub(i4, p) for p in ps)
    effects = tuple((p, q) for p, q in zip(ps, qs))

    # G1: Gram positivity is explicit: eigenvalues 1/5 on ones and
    # 1 on its sum-zero complement.  The same decomposition also certifies
    # each leading principal block I_n-J_n/5 for n <= 4.
    assert mul(gram, gram_inv) == i4 and inverse(gram) == gram_inv
    for n in range(1, 5):
        leading = matrix([row[:n] for row in gram[:n]])
        # I_n - J_n/5 is positive for n <= 4 by the displayed decomposition.
        assert sub(identity(n), scale(F(1, 5), matrix([[1] * n] * n))) == leading
        assert F(1) - F(n, 5) > 0
    assert power(r, 5) == i4 and sharp(r, gram) == power(r, 4)
    assert mul(mul(transpose(r), gram), r) == gram
    total = zeros(4)
    for k, (p, q) in enumerate(effects):
        assert mul(p, p) == p and mul(q, q) == q
        assert sharp(p, gram) == p and sharp(q, gram) == q
        assert mul(p, q) == zeros(4) and mul(q, p) == zeros(4)
        assert rank(p) == 1 and rank(q) == 3 and add(p, q) == i4
        assert mul(mul(r, p), power(r, 4)) == ps[(k + 1) % 5]
        total = add(total, p)
        for l, other in enumerate(ps):
            assert trace(mul(p, other)) == (F(1) if k == l else F(1, 16))
    assert total == scale(F(5, 4), i4)
    print("G1 PASS: positive Gram, order-five isometry and five simplex contexts")

    # G2: each branch is given by one exact Kraus map, with K^sharp=K.
    # The Kraus-square identity certifies CP and trace preservation in every
    # ancillary dimension; finite matrix-unit checks audit the linear identities.
    for p, q in effects:
        assert add(mul(sharp(p, gram), p), mul(sharp(q, gram), q)) == i4
        for x in units(4):
            low, high = sandwich(p, x), sandwich(q, x)
            assert trace(add(low, high)) == trace(x)
            assert sandwich(p, low) == low and sandwich(q, high) == high
            assert sandwich(p, high) == zeros(4)
            assert sandwich(q, low) == zeros(4)
            assert trace(low) == trace(mul(p, x))
            assert trace(high) == trace(mul(q, x))
    print("G2 PASS: Kraus completeness and branch identities on all 16 matrix units")

    # G3: source times three-state blank/LOW/HIGH pointer.  The two swaps
    # need not commute: orthogonal source controls make their sum unitary.
    swap_l = matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    swap_h = matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    ready = unit(3, 0, 0)
    gram12 = kron(gram, identity(3))
    for p, q in effects:
        writer = add(kron(p, swap_l), kron(q, swap_h))
        writer_sharp = sharp(writer, gram12)
        assert writer_sharp == writer
        assert mul(writer_sharp, writer) == identity(12)
        for x in units(4):
            written = mul(mul(writer, kron(x, ready)), writer_sharp)
            assert trace(written) == trace(x)
            assert partial_right(written, 4, 3) == add(sandwich(p, x), sandwich(q, x))
            for label, effect in ((1, p), (2, q)):
                block = matrix([[written[3 * i + label][3 * j + label]
                                 for j in range(4)] for i in range(4)])
                assert block == sandwich(effect, x)
            assert all(written[3 * i][3 * j] == 0
                       for i in range(4) for j in range(4))
            assert matrix([[written[3 * i + 1][3 * j + 2]
                            for j in range(4)] for i in range(4)]) == mul(mul(p, x), q)
    print("G3 PASS: five exact 12-dimensional writers and coherent pointer blocks")

    # G4: the inherited three-pass criterion is audited in its own HIGH
    # support basis.  It is not inferred by finite sampling of channels.
    h = matrix([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
    a = matrix([[-1, -1, F(-3, 4)], [0, 0, F(1, 4)], [1, 0, F(1, 4)]])
    ash = sharp(a, h)
    bs = tuple(mul(power(ash, n), power(a, n)) for n in range(4))
    ds = ((-1, -1, 3), (11, -5, -1), (-9, -25, -5))
    projectors = tuple(pure(d, h) for d in ds)
    expected_weights = (F(15, 16), F(215, 256), F(2815, 4096))
    assert sub(h, mul(mul(transpose(a), h), a)) == matrix([[0, 0, 0], [0, 0, 0], [0, 0, F(5, 4)]])
    assert mul(ash, column(ds[0])) == scale(F(1, 4), column(ds[1]))
    assert mul(ash, column(ds[1])) == scale(F(1, 4), column(ds[2]))
    assert rank(transpose(matrix(ds))) == 3
    assert mul(mul(transpose(column(ds[0])), h), column(ds[1]))[0][0] == -4
    assert mul(mul(transpose(column(ds[0])), h), column(ds[2]))[0][0] == -20
    for n in range(3):
        difference = sub(bs[n], bs[n + 1])
        assert difference == scale(expected_weights[n], projectors[n])
        assert rank(difference) == 1 and trace(difference) == expected_weights[n]
    comm_columns = [tuple(y for p in projectors
                          for y in flatten(sub(mul(x, p), mul(p, x))))
                    for x in units(3)]
    assert rank(transpose(tuple(comm_columns))) == 8
    span = transpose(matrix(ds[:2]))
    rs = mul(mul(mul(span, inverse(mul(mul(transpose(span), h), span))), transpose(span)), h)
    complement = sub(identity(3), rs)
    assert sharp(rs, h) == rs and mul(rs, rs) == rs and rank(rs) == 2
    two_pass = lambda x: add(sandwich(rs, x), sandwich(complement, x))
    assert two_pass(bs[1]) == bs[1] and two_pass(bs[2]) == bs[2]
    assert two_pass(bs[3]) != bs[3]
    # Explicit rational depolarizing Kraus witness: 24 S4 matrices, each
    # weighted by 1/6, 1/12, 1/12.  No irrational square root is introduced.
    basis = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]])
    # This embeds the inherited A into each HIGH support.  It does not
    # identify A with the compression of the chosen context shift R.
    for context in range(5):
        transported_basis = mul(power(r, context), basis)
        assert mul(mul(transpose(transported_basis), gram), transported_basis) == h
        assert mul(qs[context], transported_basis) == transported_basis
        assert rank(transported_basis) == 3
    kraus = []
    for perm in permutations(range(4)):
        perm4 = matrix([[int(i == perm[j]) for j in range(4)] for i in range(4)])
        ambient = mul(perm4, basis)
        restricted = ambient[:3]
        assert mul(basis, restricted) == ambient
        assert mul(mul(transpose(restricted), h), restricted) == h
        kraus.extend(scale(weight, restricted) for weight in (F(1, 6), F(1, 12), F(1, 12)))
    assert len(kraus) == 72
    completeness = zeros(3)
    for k in kraus:
        completeness = add(completeness, mul(sharp(k, h), k))
    assert completeness == identity(3)
    for x in units(3):
        assert channel(kraus, x, h) == scale(trace(x) / 3, identity(3))
    dep_pure = channel(kraus, projectors[0], h)
    assert dep_pure != projectors[0] and trace(mul(dep_pure, dep_pure)) == F(1, 3)
    print("G4 PASS: three-pass rank-eight certificate and two-pass/depolarizing witnesses")

    states = (ps[0], ps[2], scale(F(1, 4), i4),
              pure((1, 0, 0, 0), gram), pure((1, -1, 0, 0), gram),
              pure((1, 1, 0, 0), gram))
    assert len(states) == 6 and len(set(states)) == 6
    for rho in states:
        assert trace(rho) == 1 and sharp(rho, gram) == rho

    def branch(x, context, outcome):
        return sandwich(effects[context][outcome], x)

    def history(x, contexts, outcomes):
        assert len(contexts) == len(outcomes)
        for context, outcome in zip(contexts, outcomes):
            x = branch(x, context, outcome)
        return x

    # G5: unnormalized branches carry joint probabilities; no division is
    # used during composition.  Every prefix is checked before extending it.
    history_count = 0
    for contexts in product(range(5), repeat=3):
        for rho in states:
            level = {(): rho}
            for context in contexts:
                extended = {}
                for word, source in level.items():
                    children = [branch(source, context, o) for o in range(2)]
                    assert sum(trace(child) for child in children) == trace(source)
                    for outcome, child in enumerate(children):
                        assert trace(child) >= 0
                        normalized(child)  # Includes the zero-weight guard.
                        extended[word + (outcome,)] = child
                level = extended
            assert sum(trace(x) for x in level.values()) == 1
            for word, child in level.items():
                assert child == history(rho, contexts, word)
                history_count += 1
    assert history_count == 6000
    adaptive_count = 0
    for rho in states:
        level = {(): rho}
        for _ in range(4):
            extended = {}
            for word, source in level.items():
                context = (len(word) + sum((i + 1) * bit for i, bit in enumerate(word))) % 5
                children = [branch(source, context, outcome) for outcome in range(2)]
                assert sum(trace(x) for x in children) == trace(source)
                for outcome, child in enumerate(children):
                    assert trace(child) >= 0
                    extended[word + (outcome,)] = child
            level = extended
            assert sum(trace(x) for x in level.values()) == 1
        adaptive_count += len(level)
    assert adaptive_count == 96
    print("G5 PASS: 6000 ordered histories, 96 adaptive leaves and exact prefix marginals")

    # G6: fixed-context reuse and genuinely fresh source replacement differ.
    # Replacement is defined on source-reference joints, not only marginals.
    for context in range(5):
        for rho in states:
            for length in range(1, 6):
                for word in product(range(2), repeat=length):
                    result = history(rho, (context,) * length, word)
                    expected = (branch(rho, context, word[0])
                                if len(set(word)) == 1 else zeros(4))
                    assert result == expected
    fresh_count = 0
    for rho in states:
        for contexts in product(range(5), repeat=3):
            total_probability = F(0)
            for word in product(range(2), repeat=3):
                current = rho
                expected_probability = F(1)
                for context, outcome in zip(contexts, word):
                    expected_probability *= trace(branch(rho, context, outcome))
                    selected = branch(current, context, outcome)
                    # Unnormalized replacement: R_rho(X)=tr(X) rho.
                    current = scale(trace(selected), rho)
                assert trace(current) == expected_probability
                total_probability += trace(current)
                fresh_count += 1
            assert total_probability == 1
    assert fresh_count == 6000
    mixed = states[2]
    assert trace(history(mixed, (0, 0), (0, 0))) == F(1, 4)
    assert trace(branch(mixed, 0, 0)) ** 2 == F(1, 16)
    # Source-reference vector v0|0>+v1|1> has unequal Schmidt weights;
    # a correct replacement preserves the complete reference marginal.
    v0, v1 = (1, -1, 0, 0), (1, 1, -2, 0)
    entangled = pure(tuple(x for pair in zip(v0, v1) for x in pair),
                     kron(gram, identity(2)))
    ref_before = partial_left(entangled, 4, 2)
    assert ref_before == matrix([[F(1, 4), 0], [0, F(3, 4)]])
    replaced = kron(ps[0], ref_before)
    assert partial_left(replaced, 4, 2) == ref_before
    assert partial_right(replaced, 4, 2) == ps[0]
    assert replaced != entangled
    print("G6 PASS: repeated records, 6000 fresh-source histories and joint reset witness")

    # G7: the intervening noncommuting measurement changes a later marginal.
    low_low = trace(history(ps[0], (1, 0), (0, 0)))
    high_low = trace(history(ps[0], (1, 0), (1, 0)))
    assert low_low == F(1, 256) and high_low == F(225, 256)
    assert low_low + high_low == F(113, 128)
    assert trace(branch(ps[0], 0, 0)) == 1
    zero_branch = branch(ps[0], 0, 1)
    assert zero_branch == zeros(4) and normalized(zero_branch) is None
    assert pure((0, 0, 0, 0), gram) is None
    print("G7 PASS: ordered interference 1/256 + 225/256 = 113/128; ZERO_SUPPORT guarded")

    # G8: deliberately wrong constructions must violate the frozen identity.
    assert trace(branch(mixed, 0, 0)) != trace(mixed)  # Missing HIGH branch.
    bad_context = mul(mul(r, p0), r)  # Wrong inverse on the right.
    assert bad_context != ps[1] and trace(bad_context) == F(-1, 4)
    high_basis = ((1, -1, 0, 0), (1, 1, -2, 0), (1, 1, 1, -3))
    fine = tuple(pure(v, gram) for v in high_basis)
    assert add(add(fine[0], fine[1]), fine[2]) == qs[0]
    coherent_high = pure((2, 0, -2, 0), gram)
    assert sandwich(qs[0], coherent_high) == coherent_high
    fine_read = zeros(4)
    for effect in fine:
        fine_read = add(fine_read, sandwich(effect, coherent_high))
    assert fine_read != coherent_high
    assert trace(mul(fine_read, fine_read)) < 1
    # Resetting a separate port cannot remove an existing source-reference
    # correlation.  Its source-reference marginal is still entangled above.
    port_reset_only = kron(entangled, ready)
    joint_source_reset = kron(replaced, ready)
    assert partial_right(port_reset_only, 8, 3) == entangled
    assert partial_right(joint_source_reset, 8, 3) == replaced
    assert port_reset_only != joint_source_reset
    print("G8 PASS: missing outcome, wrong inverse, fine HIGH record and port-only reset rejected")
    print("VERDICT: SELECTED-MEASUREMENT-LAW; conditional theorem, physical adoption not derived")


if __name__ == "__main__":
    main()
