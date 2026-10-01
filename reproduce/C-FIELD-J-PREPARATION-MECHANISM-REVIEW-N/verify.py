#!/usr/bin/env python3
"""Independent, exact and finite preparation-mechanism audit. Apache-2.0."""

from fractions import Fraction as F
from itertools import product


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    out = zero(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b, factor=F(1)):
    return [[x + factor * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, factor):
    return [[factor * x for x in row] for row in a]


def multiply(a, b):
    out = zero(len(a), len(b[0]))
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x * y
    return out


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def outer(a, b=None):
    if b is None:
        b = a
    return [[x * y for y in b] for x in a]


def assert_psd(a):
    """Exact symmetric Schur-complement certificate, including zero pivots."""
    assert a == transpose(a)
    work = [row[:] for row in a]
    n = len(a)
    for k in range(n):
        pivot = work[k][k]
        assert pivot >= 0
        if not pivot:
            assert all(work[k][j] == 0 for j in range(k, n))
            continue
        for i in range(k + 1, n):
            for j in range(i, n):
                value = work[i][j] - work[i][k] * work[k][j] / pivot
                work[i][j] = value
                work[j][i] = value


def rank(a):
    work = [row[:] for row in a]
    lead = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(lead, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[lead], work[pivot] = work[pivot], work[lead]
        value = work[lead][col]
        work[lead] = [x / value for x in work[lead]]
        for i in range(lead + 1, len(work)):
            value = work[i][col]
            if value:
                work[i] = [x - value * y for x, y in zip(work[i], work[lead])]
        lead += 1
        if lead == len(work):
            break
    return lead


def local(L, edge, full=False, sign=1):
    n = 2 * L if full else L
    a, b = edge, (edge + 1) % L
    if full:
        a, b = 2 * a, 2 * b
    d, s = [F(0)] * n, [F(0)] * n
    d[a], d[b] = F(1), F(-sign)
    s[a], s[b] = F(1), F(sign)
    p = scale(outer(d), F(1, 2))
    q = add(eye(n), p, -1)
    jump = scale(outer(s, d), F(1, 2))
    return p, q, jump


def forward(rho, q, jump):
    return add(multiply(multiply(q, rho), transpose(q)),
               multiply(multiply(jump, rho), transpose(jump)))


def adjoint(effect, q, jump):
    return add(multiply(multiply(transpose(q), effect), q),
               multiply(multiply(transpose(jump), effect), jump))


def ready(L, full=False):
    n = 2 * L if full else L
    out = zero(n)
    modes = range(0, n, 2) if full else range(n)
    for i in modes:
        for j in modes:
            out[i][j] = F(1, L)
    return out


def fidelity(rho):
    return sum((sum(row, F(0)) for row in rho), F(0)) / len(rho)


def put(out, key, value):
    if value:
        new = out.get(key, F(0)) + value
        if new:
            out[key] = new
        else:
            out.pop(key, None)


def sparse_add(a, b, factor=F(1)):
    out = dict(a)
    for key, value in b.items():
        put(out, key, factor * value)
    return out


def norm2(vector):
    return sum((x * x for x in vector.values()), F(0))


def reflection_column_data(L, edge):
    a, b = 4 * edge, 4 * ((edge + 1) % L)
    return {a: F(1), b: F(-1), a + 1: F(-1), b + 1: F(-1)}


def reflect(vector, z):
    overlap = sum((value * vector.get(key, F(0)) for key, value in z.items()), F(0))
    out = dict(vector)
    for key, value in z.items():
        put(out, key, -value * overlap / 2)
    return out


def dyadic(value):
    denominator = value.denominator
    return denominator > 0 and denominator & (denominator - 1) == 0


def matrix_dyadic(a):
    return all(dyadic(value) for row in a for value in row)


def local_audit():
    basis_cases = unit_cases = edges = 0
    for L in (3, 6, 8):
        dimension = 2 * L
        for edge in range(L):
            edges += 1
            z = reflection_column_data(L, edge)
            columns = [reflect({i: F(1)}, z) for i in range(4 * L)]
            u = zero(4 * L)
            for i, column in enumerate(columns):
                assert norm2(column) == 1
                assert reflect(column, z) == {i: F(1)}
                if (i // 2) % 2:
                    assert column == {i: F(1)}
                for k, value in column.items():
                    u[k][i] = value
                basis_cases += 1
            assert u == transpose(u)
            generator = scale(add(eye(4 * L), u, -1), F(1, 2))
            assert multiply(generator, generator) == generator
            assert trace(generator) == 1
            assert matrix_dyadic(u)
            p, q, jump = local(L, edge, full=True)
            assert matrix_dyadic(q) and matrix_dyadic(jump)
            assert add(multiply(transpose(q), q),
                       multiply(transpose(jump), jump)) == eye(dimension)
            qcols = transpose(q)
            jcols = transpose(jump)
            for a in range(dimension):
                for b in range(dimension):
                    reduced = zero(dimension)
                    for x, ket in columns[2 * a].items():
                        for y, bra in columns[2 * b].items():
                            if x % 2 == y % 2:
                                reduced[x // 2][y // 2] += ket * bra
                    expected = add(outer(qcols[a], qcols[b]),
                                   outer(jcols[a], jcols[b]))
                    assert reduced == expected
                    unit_cases += 1
            dirty = reflect({4 * j + 1: F(1) for j in range(L)}, z)
            actual = sum((sum((dirty.get(4 * j + bath, F(0))
                               for j in range(L)), F(0)) ** 2
                          for bath in range(2)), F(0)) / (L * L)
            assert actual == (1 - F(2, L)) ** 2
            assert norm2(dirty) == L
            # All touched pointer and bath levels have constant bare energy.
            flat_energy = scale(eye(4 * L), F(2))
            assert multiply(u, flat_energy) == multiply(flat_energy, u)
    assert (basis_cases, unit_cases) == (436, 3020)
    return edges, basis_cases, unit_cases


def contraction_audit():
    dimensions = certificates = 0
    for L in (3, 4, 6, 8, 11):
        identity, e = eye(L), ready(L)
        complement = add(identity, e, -1)
        prefix, loss, graph = identity, zero(L), zero(L)
        derivatives, differences, primitives = [], [], []
        for edge in range(L):
            p, q, jump = local(L, edge)
            primitives.append((q, jump))
            graph = add(graph, p)
            derivatives.append([prefix[edge][k] - prefix[(edge + 1) % L][k]
                                for k in range(L)])
            row = [F(0)] * L
            row[edge], row[(edge + 1) % L] = F(1), F(-1)
            differences.append(row)
            loss = add(loss, multiply(multiply(transpose(prefix), p), prefix))
            prefix = multiply(q, prefix)
        direct_loss = add(identity, multiply(transpose(prefix), prefix), -1)
        assert loss == direct_loss
        overlap = eye(L)
        for j in range(1, L - 1):
            overlap[j][j - 1] = F(-1, 2)
        overlap[L - 1][L - 2] = F(-1, 2)
        overlap[L - 1][0] = F(-1, 2)
        assert multiply(overlap, derivatives) == differences
        assert all(sum(abs(x) for x in row) <= 2 for row in overlap)
        assert all(sum(abs(x) for x in row) <= 2 for row in transpose(overlap))
        effect = e
        for q, jump in reversed(primitives):
            effect = adjoint(effect, q, jump)
        gain = add(effect, e, -1)
        for matrix in (
            add(graph, complement, -F(8, L * L)),
            add(scale(loss, F(4)), graph, -1),
            add(loss, complement, -F(2, L * L)),
            add(gain, loss, -F(2, L)),
            add(gain, complement, -F(4, L ** 3)),
        ):
            assert_psd(matrix)
            certificates += 1
        dimensions += 1
    return dimensions, certificates


def density_audit():
    snapshots = []
    states = boundaries = collisions = 0
    for L in (3, 4, 6, 8):
        e = ready(L)
        family = []
        for i in range(L):
            rho = zero(L)
            rho[i][i] = F(1)
            family.append(("basis", rho))
        p, q, jump = local(L, 0)
        family += [("diagonal", scale(eye(L), F(1, L))), ("E", e),
                   ("difference", p), ("sum", multiply(jump, transpose(jump)))]
        diagonal = scale(eye(L), F(1, L))
        expected = [row[:] for row in diagonal]
        expected[0][1] = expected[1][0] = F(1, L)
        assert forward(diagonal, q, jump) == expected
        assert trace(multiply(p, diagonal)) == F(1, L)
        r = 1 - F(4, L ** 3)
        for label, initial in family:
            states += 1
            rho = initial
            f0, marks = fidelity(rho), F(0)
            is_dyadic = matrix_dyadic(rho)
            for sweep in range(4):
                assert trace(rho) == 1
                assert_psd(rho)
                f = fidelity(rho)
                assert 1 - f <= r ** sweep * (1 - f0)
                assert marks == F(L, 2) * (f - f0)
                if label == "E":
                    assert rho == e and marks == 0
                snapshots.append((L, [row[:] for row in rho]))
                boundaries += 1
                if sweep == 3:
                    break
                for edge in range(L):
                    p, q, jump = local(L, edge)
                    mark = trace(multiply(p, rho))
                    assert mark >= 0
                    old = fidelity(rho)
                    rho = forward(rho, q, jump)
                    assert fidelity(rho) - old == F(2, L) * mark
                    marks += mark
                    if is_dyadic:
                        assert matrix_dyadic(rho)
                    collisions += 1
    assert (states, boundaries, collisions) == (37, 148, 627)
    return snapshots, (states, boundaries, collisions)


def retained_collision(vector, L, pointer, edge, bath_index):
    """Reflect four amplitudes within each retained spectator fiber."""
    out = {}
    neighbor = (edge + 1) % L
    for key, amplitude in vector.items():
        put(out, key, amplitude)
        position, bit = key[pointer], (key[3] >> bath_index) & 1
        if position not in (edge, neighbor):
            continue
        z_source = F(1 if position == edge and bit == 0 else -1)
        for target_position, target_bit, z_target in (
            (edge, 0, 1), (neighbor, 0, -1),
            (edge, 1, -1), (neighbor, 1, -1),
        ):
            changed = list(key)
            changed[pointer] = target_position
            changed[3] = (key[3] & ~(1 << bath_index)) | (target_bit << bath_index)
            put(out, tuple(changed), -amplitude * z_source * F(z_target, 2))
    return out


def reduced_vector(vector, keep, normalization):
    groups = {}
    for key, value in vector.items():
        retained = tuple(key[i] for i in keep)
        discarded = tuple(key[i] for i in range(len(key)) if i not in keep)
        group = groups.setdefault(discarded, {})
        put(group, retained, value)
    out = {}
    for group in groups.values():
        for a, x in group.items():
            for b, y in group.items():
                put(out, (a, b), x * y / normalization)
    return out


def project_ready(vector, L, pointers):
    groups = {}
    for key, amplitude in vector.items():
        spectator = tuple(key[i] for i in range(len(key)) if i not in pointers)
        put(groups, spectator, amplitude)
    out = {}
    for spectator, amplitude in groups.items():
        for modes in product(range(L), repeat=len(pointers)):
            mi, si = iter(modes), iter(spectator)
            key = tuple(next(mi) if i in pointers else next(si) for i in range(4))
            put(out, key, amplitude / (L ** len(pointers)))
    return out


def density_pointer_channel(rho, L, pointer, edge):
    _, q, jump = local(L, edge)
    out = {}
    for operation in (q, jump):
        for (ket, bra), value in rho.items():
            for a in range(L):
                left = operation[a][ket[pointer]]
                if not left:
                    continue
                for b in range(L):
                    right = operation[b][bra[pointer]]
                    if right:
                        changed_ket, changed_bra = list(ket), list(bra)
                        changed_ket[pointer], changed_bra[pointer] = a, b
                        put(out, (tuple(changed_ket), tuple(changed_bra)),
                            value * left * right)
    return out


def retained_audit():
    L = 3
    schedule = [(pointer, edge, pointer * L + edge)
                for pointer in range(2) for edge in range(L)]
    cases = 0
    for initial in (
        {(0, 0, 0, 0): F(1), (1, 1, 1, 0): F(1)},
        {(0, 1, 0, 0): F(1)},
    ):
        normalization = norm2(initial)
        rho = reduced_vector(initial, (0, 1, 2), normalization)
        vector = initial
        f0 = [norm2(project_ready(initial, L, (i,))) / normalization for i in range(2)]
        for pointer, edge, bath in schedule:
            vector = retained_collision(vector, L, pointer, edge, bath)
            rho = density_pointer_channel(rho, L, pointer, edge)
        assert norm2(vector) == normalization
        assert reduced_vector(vector, (0, 1, 2), normalization) == rho
        assert reduced_vector(vector, (2,), normalization) == reduced_vector(initial, (2,), normalization)
        backwards = vector
        for pointer, edge, bath in reversed(schedule):
            backwards = retained_collision(backwards, L, pointer, edge, bath)
        assert backwards == initial
        final_f = [norm2(project_ready(vector, L, (i,))) / normalization for i in range(2)]
        r = 1 - F(4, L ** 3)
        for old, new in zip(f0, final_f):
            assert 1 - new <= r * (1 - old)
        projected = project_ready(vector, L, (0, 1))
        residual = sparse_add(vector, projected, -1)
        probability = norm2(projected) / normalization
        assert 1 - probability <= sum((1 - x for x in final_f), F(0))
        assert norm2(projected) + norm2(residual) == normalization
        assert project_ready(residual, L, (0, 1)) == {}
        environment = reduced_vector(vector, (2, 3), normalization)
        tau = reduced_vector(projected, (2, 3), normalization)
        xi = reduced_vector(residual, (2, 3), normalization)
        assert environment == sparse_add(tau, xi)
        assert sum((value for (a, b), value in tau.items() if a == b), F(0)) == probability
        assert sum((value for (a, b), value in xi.items() if a == b), F(0)) == 1 - probability
        marks = sum((amplitude * amplitude * key[3].bit_count()
                     for key, amplitude in vector.items()), F(0)) / normalization
        assert marks == F(L, 2) * sum((new - old for new, old in zip(final_f, f0)), F(0))
        cases += 1
    return cases, len(schedule)


def phase_audit():
    patterns = consistent = fixed_edges = 0
    for L in (3, 5, 6):
        for signs in product((-1, 1), repeat=L):
            differences = zero(L)
            holonomy = 1
            for j, sign in enumerate(signs):
                differences[j][j] = F(1)
                differences[j][(j + 1) % L] = F(-sign)
                holonomy *= sign
            assert rank(differences) == (L - 1 if holonomy == 1 else L)
            if holonomy == 1:
                consistent += 1
                vector = [F(1)]
                for sign in signs[:-1]:
                    vector.append(vector[-1] * sign)
                dark = scale(outer(vector), F(1, L))
                assert multiply(differences, [[x] for x in vector]) == zero(L, 1)
                assert (dark == ready(L)) == all(sign == 1 for sign in signs)
                for j, sign in enumerate(signs):
                    _, q, jump = local(L, j, sign=sign)
                    assert forward(dark, q, jump) == dark
                    fixed_edges += 1
            patterns += 1
    assert not dyadic(F(1, 613))
    assert (patterns, consistent, fixed_edges) == (104, 52, 284)
    return patterns, consistent, fixed_edges


def shifted_block(rho, left_code, right_code):
    n = len(rho)
    out = zero(n)
    for i in range(n):
        for j in range(n):
            out[(i + left_code) % n][(j + right_code) % n] = rho[i][j]
    return out


def parity_block(rho, outcome):
    return [[value if i % 2 == outcome and j % 2 == outcome else F(0)
             for j, value in enumerate(row)] for i, row in enumerate(rho)]


def ceiling(value):
    return -((-value.numerator) // value.denominator)


def handoff_audit(snapshots):
    branches = schedules = budgets = 0
    codes = (0, 2, 1)
    for L, rho in snapshots:
        embedded = zero(2 * L)
        for i in range(L):
            for j in range(L):
                embedded[2 * i][2 * j] = rho[i][j]
        ideal = ready(L, full=True)
        difference = add(embedded, ideal, -1)
        for a, left_code in enumerate(codes):
            for b, right_code in enumerate(codes):
                actual_shift = shifted_block(embedded, left_code, right_code)
                ideal_shift = shifted_block(ideal, left_code, right_code)
                diff_shift = shifted_block(difference, left_code, right_code)
                summed = zero(2 * L)
                for outcome in range(2):
                    actual = parity_block(actual_shift, outcome)
                    target = parity_block(ideal_shift, outcome)
                    assert add(actual, target, -1) == parity_block(diff_shift, outcome)
                    assert parity_block(actual, outcome) == actual
                    assert parity_block(actual, 1 - outcome) == zero(2 * L)
                    coefficient = int(left_code % 2 == right_code % 2 == outcome)
                    assert trace(target) == coefficient
                    summed = add(summed, actual)
                    branches += 1
                # The source matrix unit contributes trace only when a=b.
                assert int(a == b) * trace(summed) == int(a == b) * trace(embedded)
    assert branches == 2664
    L = 613
    for K in (0, 2, 4):
        m = K + 1
        for seed in range(3):
            sweeps = [(i + seed) % 3 for i in range(m)]
            addresses = [(i, sweep, edge) for i in range(m)
                         for sweep in range(sweeps[i]) for edge in range(L)]
            assert len(addresses) == L * sum(sweeps)
            assert len(set(addresses)) == len(addresses)
            flags = tuple(i % 2 for i in range(K))
            def next_pulse(position):
                if position == len(addresses):
                    return "RESOURCE_EXHAUSTED", None, flags
                return "PULSE", addresses[position], flags
            for position, address in enumerate(addresses):
                status, actual_address, actual_flags = next_pulse(position)
                assert (status, actual_address, actual_flags) == ("PULSE", address, flags)
            assert next_pulse(len(addresses)) == ("RESOURCE_EXHAUSTED", None, flags)
            assert len(flags) == K and m == K + 1
            if K == 0:
                assert m == 1 and flags == ()
            schedules += 1
    a = F(4, L ** 3)
    for m in (1, 2, 5):
        for error in (F(1), F(1, 2), F(1, 10)):
            target = F(4, 9) * error ** 2
            for c in (F(m), m * (1 - F(1, L))):
                n = max(0, ceiling((c / target - 1) / a))
                assert c / (1 + n * a) <= target
                if n:
                    assert c / (1 + (n - 1) * a) > target
                bath_count = m * L * n
                assert isinstance(bath_count, int) and bath_count >= 0
                budgets += 1
    assert (schedules, budgets) == (9, 18)
    return branches, schedules, budgets


def main():
    edges, bases, units = local_audit()
    print(f"PASS local: edges={edges} full_basis={bases} pointer_units={units}")
    dimensions, certificates = contraction_audit()
    print(f"PASS contraction: dimensions={dimensions} exact_psd_certificates={certificates}")
    snapshots, (states, boundaries, collisions) = density_audit()
    print(f"PASS densities: states={states} boundaries={boundaries} collisions={collisions}")
    cases, baths = retained_audit()
    print(f"PASS retained: correlated_or_product_inputs={cases} distinct_baths_each={baths}")
    patterns, consistent, fixed_edges = phase_audit()
    print(f"PASS phase_exactness: sign_patterns={patterns} dark_lines={consistent} fixed_edges={fixed_edges}")
    branches, schedules, budgets = handoff_audit(snapshots)
    print(f"PASS handoff: branches={branches} schedules={schedules} rational_budgets={budgets}")
    print("SCOPE L=613; m=K+1; B=L sum n_i; approximate pointer preparation; occurrence NOT DERIVED")


if __name__ == "__main__":
    main()
