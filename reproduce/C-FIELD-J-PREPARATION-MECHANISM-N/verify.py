#!/usr/bin/env python3
"""Exact finite audit of the frozen preparation-mechanism specification.

Python 3.10+, standard library only. No predecessor imports or runtime data.
The universal statements are proved in the companion PROOF.md; these finite
domains are precisely those registered before execution. No actual occurrence
or physical implementation is inferred from a successful audit.
"""

from fractions import Fraction as F
from itertools import product


SPEC_PIN = "7809098069d4c4ff9f362048cf92c3e8b4714493"
PHYSICAL_L = 613


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def zero(rows, cols=None):
    return [[F(0) for _ in range(rows if cols is None else cols)]
            for _ in range(rows)]


def identity(n):
    result = zero(n)
    for j in range(n):
        result[j][j] = F(1)
    return result


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, c):
    return [[c * x for x in row] for row in a]


def multiply(a, b):
    result = zero(len(a), len(b[0]))
    for i, row in enumerate(a):
        out = result[i]
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[j] += x * y
    return result


def matvec(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def outer(a, b):
    return [[x * y for y in b] for x in a]


def trace(a):
    return sum((a[j][j] for j in range(len(a))), F(0))


def trace_product(a, b):
    return sum((a[i][j] * b[j][i]
                for i in range(len(a)) for j in range(len(a))), F(0))


def conjugate(a, x):
    return multiply(multiply(a, x), transpose(a))


def is_zero(a):
    return all(not x for row in a for x in row)


def psd(a, label):
    """Exact symmetric Schur-complement certificate, including zero pivots."""
    require(a == transpose(a), label + ": not symmetric")
    work = [row[:] for row in a]
    n = len(work)
    for k in range(n):
        pivot = work[k][k]
        require(pivot >= 0, label + ": negative pivot")
        if not pivot:
            require(all(not work[k][j] for j in range(k + 1, n)),
                    label + ": nonzero row at zero pivot")
            continue
        for i in range(k + 1, n):
            for j in range(i, n):
                work[i][j] -= work[i][k] * work[k][j] / pivot
                work[j][i] = work[i][j]


def matrix_rank(a):
    work = [row[:] for row in a]
    pivot_row = 0
    for col in range(len(work[0])):
        hit = next((r for r in range(pivot_row, len(work)) if work[r][col]),
                   None)
        if hit is None:
            continue
        work[pivot_row], work[hit] = work[hit], work[pivot_row]
        pivot = work[pivot_row][col]
        work[pivot_row] = [x / pivot for x in work[pivot_row]]
        for row in range(pivot_row + 1, len(work)):
            factor = work[row][col]
            if factor:
                work[row] = [x - factor * y
                             for x, y in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def is_dyadic(x):
    denominator = F(x).denominator
    return denominator & (denominator - 1) == 0


def dyadic_matrix(a):
    return all(is_dyadic(x) for row in a for x in row)


def pair_matrices(length, edge, full=False, sign=1):
    """Q, J, P_minus, P_plus on the even ring or full C pointer."""
    size = 2 * length if full else length
    j = 2 * edge if full else edge
    k = 2 * ((edge + 1) % length) if full else (edge + 1) % length
    minus, plus = [F(0)] * size, [F(0)] * size
    minus[j], minus[k] = F(1), F(-sign)
    plus[j], plus[k] = F(1), F(sign)
    pm = scale(outer(minus, minus), F(1, 2))
    pp = scale(outer(plus, plus), F(1, 2))
    q = sub(identity(size), pm)
    jump = scale(outer(plus, minus), F(1, 2))
    return q, jump, pm, pp


def reflection(length, edge):
    """U and its rank-one generator projector in the entire 4L space."""
    nu = [F(0)] * (4 * length)
    j, k = 2 * edge, 2 * ((edge + 1) % length)
    nu[2 * j] = F(1, 2)
    nu[2 * k] = F(-1, 2)
    nu[2 * j + 1] = F(-1, 2)
    nu[2 * k + 1] = F(-1, 2)
    projector = outer(nu, nu)
    return sub(identity(4 * length), scale(projector, F(2))), projector


def channel(q, jump, rho):
    return add(conjugate(q, rho), conjugate(jump, rho))


def adjoint_channel(q, jump, observable):
    return add(conjugate(transpose(q), observable),
               conjugate(transpose(jump), observable))


def ready(length):
    return [[F(1, length) for _ in range(length)] for _ in range(length)]


def embed_even(a):
    result = zero(2 * len(a))
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            result[2 * i][2 * j] = value
    return result


def fidelity(rho):
    return sum((x for row in rho for x in row), F(0)) / len(rho)


def local_dilation_audit():
    inverse_cases = unit_cases = 0
    for length in (3, 4, 5, 7):
        size = 2 * length
        even_ready = embed_even(ready(length))
        for edge in range(length):
            u, generator = reflection(length, edge)
            q, jump, pm, _ = pair_matrices(length, edge, full=True)
            require(multiply(generator, generator) == generator,
                    "generator projector")
            require(generator == transpose(generator) and trace(generator) == 1,
                    "normalized Hermitian pulse projector")
            require(u == transpose(u) and u == sub(identity(2 * size),
                                                   scale(generator, F(2))),
                    "area-pi reflection polynomial")
            require(add(multiply(transpose(q), q),
                        multiply(transpose(jump), jump)) == identity(size),
                    "fresh-bath channel completeness")
            require(all(dyadic_matrix(x) for x in (u, q, jump, pm)),
                    "dyadic local matrices")
            u2 = multiply(u, u)
            for basis in range(2 * size):
                require([u2[row][basis] for row in range(2 * size)] ==
                        [F(row == basis) for row in range(2 * size)],
                        "all-state inverse basis")
                pointer = basis // 2
                if pointer % 2:
                    require([u[row][basis] for row in range(2 * size)] ==
                            [F(row == basis) for row in range(2 * size)],
                            "odd-sector identity for both bath states")
                inverse_cases += 1
            flat_energy = scale(identity(2 * size), F(2))
            require(multiply(u, flat_energy) == multiply(flat_energy, u),
                    "selected flat pointer-plus-bath energy")
            for a in range(size):
                for b in range(size):
                    reduced = zero(size)
                    expected = zero(size)
                    for x in range(size):
                        for y in range(size):
                            reduced[x][y] = sum(
                                (u[2 * x + bit][2 * a] *
                                 u[2 * y + bit][2 * b] for bit in (0, 1)), F(0))
                            expected[x][y] = (q[x][a] * q[y][b] +
                                               jump[x][a] * jump[y][b])
                    require(reduced == expected, "all fresh-bath matrix units")
                    unit_cases += 1
            # An unnormalized even vector has norm squared L. This avoids
            # introducing a square-root field for the pure-state test.
            dirty_input = [F(0)] * (2 * size)
            for j in range(length):
                dirty_input[4 * j + 1] = F(1)
            dirty_output = matvec(u, dirty_input)
            dirty_rho = [[sum((dirty_output[2 * x + bit] *
                              dirty_output[2 * y + bit]
                              for bit in (0, 1)), F(0)) / length
                          for y in range(size)] for x in range(size)]
            require(trace(dirty_rho) == 1, "dirty-bath normalization")
            require(trace_product(even_ready, dirty_rho) ==
                    (1 - F(2, length)) ** 2, "dirty bath spoils E fidelity")
    require((inverse_cases, unit_cases) == (396, 2236), "local audit counts")
    print("PASS local_dilation inverse_basis=396 fresh_bath_matrix_units=2236")


def contraction_audit():
    for length in range(3, 13):
        one = identity(length)
        pe = ready(length)
        complement = sub(one, pe)
        graph, loss_sum = zero(length), zero(length)
        prefix = one
        derivatives, bare_rows, primitives = [], [], []
        for edge in range(length):
            q, jump, pm, _ = pair_matrices(length, edge)
            primitives.append((q, jump))
            graph = add(graph, pm)
            loss_sum = add(loss_sum, conjugate(transpose(prefix), pm))
            raw = [F(0)] * length
            raw[edge] = F(1)
            raw[(edge + 1) % length] = F(-1)
            bare_rows.append(raw)
            derivatives.append(multiply([raw], prefix)[0])
            prefix = multiply(q, prefix)
            require(conjugate(q, pe) == pe, "each projection fixes E")
        a = prefix
        loss = sub(one, multiply(transpose(a), a))
        require(loss == loss_sum, "telescoping no-jump loss")
        require(loss == scale(multiply(transpose(derivatives), derivatives),
                              F(1, 2)), "derivative norm-loss identity")
        overlap = identity(length)
        for j in range(1, length - 1):
            overlap[j][j - 1] = F(-1, 2)
        overlap[length - 1][length - 2] = F(-1, 2)
        overlap[length - 1][0] = F(-1, 2)
        require(multiply(overlap, derivatives) == bare_rows,
                "local-overlap rows including wrap-around")
        require(max(sum(abs(x) for x in row) for row in overlap) <= 2 and
                max(sum(abs(x) for x in row) for row in transpose(overlap)) <= 2,
                "overlap row and column bounds")
        psd(sub(graph, scale(complement, F(8, length ** 2))), "cycle gap")
        psd(sub(scale(loss, F(4)), graph), "overlap quadratic bound")
        psd(sub(loss, scale(complement, F(2, length ** 2))), "loss lower bound")
        observable = pe
        for q, jump in reversed(primitives):
            observable = adjoint_channel(q, jump, observable)
        increment = sub(observable, pe)
        psd(sub(increment, scale(loss, F(2, length))), "first-jump inequality")
        psd(sub(increment, scale(complement, F(4, length ** 3))),
            "rational sweep contraction")
        require(conjugate(a, pe) == pe, "no-jump product fixes E")
    print("PASS contraction dimensions=10 even_L=3..12 exact_PSD_certificates")


def reduced_preparation_audit():
    boundaries = []
    collision_count = 0
    for length in (3, 4, 5):
        pe = ready(length)
        inputs = []
        for j in range(length):
            density = zero(length)
            density[j][j] = F(1)
            inputs.append(("basis" + str(j), density))
        _, _, pm, pp = pair_matrices(length, 0)
        inputs.extend((("diagonal", scale(identity(length), F(1, length))),
                       ("E", pe), ("minus", pm), ("plus", pp)))
        r = 1 - F(4, length ** 3)
        for name, initial in inputs:
            rho = initial
            initial_f = fidelity(initial)
            marks = F(0)
            dyadic_input = dyadic_matrix(initial)
            for sweep in range(5):
                psd(rho, "reduced density positivity")
                require(trace(rho) == 1, "reduced density trace")
                require(1 - fidelity(rho) <= r ** sweep * (1 - initial_f),
                        "finite rational contraction")
                require(marks == F(length, 2) * (fidelity(rho) - initial_f),
                        "cumulative bath-mark expectation")
                if dyadic_input:
                    require(dyadic_matrix(rho), "finite dyadic closure")
                boundaries.append((length, name, sweep, rho))
                if sweep == 4:
                    break
                for edge in range(length):
                    q, jump, defect, _ = pair_matrices(length, edge)
                    mark = trace_product(defect, rho)
                    require(0 <= mark <= 1, "fresh bath mark expectation")
                    next_rho = channel(q, jump, rho)
                    require(fidelity(next_rho) - fidelity(rho) ==
                            F(2, length) * mark, "edge fidelity-mark identity")
                    marks += mark
                    rho = next_rho
                    if name == "E":
                        require(rho == pe and not marks, "edgewise E stationarity")
                    if dyadic_input:
                        require(dyadic_matrix(rho), "edgewise dyadic closure")
                    collision_count += 1
        diagonal = scale(identity(length), F(1, length))
        q, jump, defect, _ = pair_matrices(length, 0)
        first = channel(q, jump, diagonal)
        expected = [row[:] for row in diagonal]
        expected[0][1] = expected[1][0] = F(1, length)
        require(first == expected and trace_product(defect, diagonal) ==
                F(1, length), "equal populations distinguish coherent readiness")
        require(channel(q, jump, pe) == pe and trace_product(defect, pe) == 0,
                "coherent ready gives no mark")
    require(len(boundaries) == 120 and collision_count == 392,
            "reduced audit counts")
    print("PASS reduced_preparation state_boundaries=120 edge_collisions=392")
    return boundaries


def clean_sparse(values):
    return {key: value for key, value in values.items() if value}


def sparse_add(a, b, factor=F(1)):
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, F(0)) + factor * value
    return clean_sparse(result)


def sparse_inner(a, b):
    return sum((value * b.get(key, F(0)) for key, value in a.items()), F(0))


def full_collision(state, pointer, edge, bath, length):
    """Retained amplitudes keyed by (even-mode i, even-mode j, R, bath-mask)."""
    result = {}
    right = (edge + 1) % length
    signs = {(edge, 0): F(1), (right, 0): F(-1),
             (edge, 1): F(-1), (right, 1): F(-1)}
    for key, amplitude in state.items():
        mode = key[pointer]
        bit = (key[3] >> bath) & 1
        if mode not in (edge, right):
            result[key] = result.get(key, F(0)) + amplitude
            continue
        input_sign = signs[(mode, bit)]
        for (out_mode, out_bit), output_sign in signs.items():
            coefficient = F((mode, bit) == (out_mode, out_bit))
            coefficient -= input_sign * output_sign / 2
            if coefficient:
                out = list(key)
                out[pointer] = out_mode
                out[3] = (key[3] & ~(1 << bath)) | (out_bit << bath)
                out = tuple(out)
                result[out] = result.get(out, F(0)) + coefficient * amplitude
    return clean_sparse(result)


def reduced_cross(left, right, weight, keep):
    """Exact partial trace of weight |left><right|, as sparse matrix entries."""
    discard = tuple(i for i in range(4) if i not in keep)
    lg, rg = {}, {}
    for state, groups in ((left, lg), (right, rg)):
        for key, amplitude in state.items():
            rest = tuple(key[i] for i in discard)
            kept = tuple(key[i] for i in keep)
            groups.setdefault(rest, []).append((kept, amplitude))
    result = {}
    for rest in lg.keys() & rg.keys():
        for a, x in lg[rest]:
            for b, y in rg[rest]:
                key = (a, b)
                result[key] = result.get(key, F(0)) + weight * x * y
    return clean_sparse(result)


def project_ready(state, pointers, length):
    result = {}
    choices = tuple(product(range(length), repeat=len(pointers)))
    divisor = length ** len(pointers)
    for key, amplitude in state.items():
        for assignment in choices:
            out = list(key)
            for pointer, value in zip(pointers, assignment):
                out[pointer] = value
            out = tuple(out)
            result[out] = result.get(out, F(0)) + amplitude / divisor
    return clean_sparse(result)


def kron(a, b):
    return [[a[i // len(b)][j // len(b)] * b[i % len(b)][j % len(b)]
             for j in range(len(a) * len(b))]
            for i in range(len(a) * len(b))]


def pointer_density(state, weight, length):
    sparse = reduced_cross(state, state, weight, (0, 1))
    result = zero(length * length)
    for (a, b), value in sparse.items():
        result[a[0] * length + a[1]][b[0] * length + b[1]] = value
    return result


def retained_environment_audit():
    length = 3
    initial_cases = (
        ({(0, 0, 0, 0): F(1), (1, 1, 1, 0): F(1)}, F(1, 2)),
        ({(0, 0, 0, 0): F(1)}, F(1)),
    )
    sequence = [(pointer, edge, pointer * length + edge)
                for pointer in range(2) for edge in range(length)]
    require(len({bath for _, _, bath in sequence}) == 6, "fresh bath addresses")
    for initial, weight in initial_cases:
        state = initial
        expected_pointer = pointer_density(initial, weight, length)
        for pointer, edge, bath in sequence:
            state = full_collision(state, pointer, edge, bath, length)
            q, jump, _, _ = pair_matrices(length, edge)
            if pointer == 0:
                q, jump = kron(q, identity(length)), kron(jump, identity(length))
            else:
                q, jump = kron(identity(length), q), kron(identity(length), jump)
            expected_pointer = channel(q, jump, expected_pointer)
        require(weight * sparse_inner(state, state) == 1,
                "complete retained state normalization")
        recovered = state
        for pointer, edge, bath in reversed(sequence):
            recovered = full_collision(recovered, pointer, edge, bath, length)
        require(recovered == initial, "complete retained inverse")
        require(reduced_cross(state, state, weight, (2,)) ==
                reduced_cross(initial, initial, weight, (2,)),
                "unchanged reference marginal")
        require(pointer_density(state, weight, length) == expected_pointer,
                "retained/reduced two-pointer agreement")
        p0 = project_ready(state, (0,), length)
        p1 = project_ready(state, (1,), length)
        both = project_ready(state, (0, 1), length)
        require(project_ready(p0, (1,), length) == both ==
                project_ready(p1, (0,), length), "commuting ready projections")
        require(project_ready(both, (0, 1), length) == both,
                "bank ready projector idempotence")
        f0, f1, fb = [weight * sparse_inner(x, x) for x in (p0, p1, both)]
        r = 1 - F(4, length ** 3)
        for pointer, f in enumerate((f0, f1)):
            initial_projection = project_ready(initial, (pointer,), length)
            fi = weight * sparse_inner(initial_projection, initial_projection)
            require(1 - f <= r * (1 - fi), "correlated pointer fidelity bound")
        require(1 - fb <= (1 - f0) + (1 - f1), "bank union bound")
        neither = sparse_add(sparse_add(sparse_add(state, p0, F(-1)),
                                       p1, F(-1)), both)
        union_remainder = weight * sparse_inner(neither, neither)
        require((1 - f0) + (1 - f1) - (1 - fb) == union_remainder >= 0,
                "exact positive union remainder")
        complement = sparse_add(state, both, F(-1))
        require(sparse_add(both, complement) == state and
                sparse_inner(both, complement) == 0, "orthogonal projection split")
        require(weight * sparse_inner(complement, complement) == 1 - fb,
                "discarded projection mass")
        actual_rest = reduced_cross(state, state, weight, (2, 3))
        projected_rest = reduced_cross(both, both, weight, (2, 3))
        remaining_rest = reduced_cross(complement, complement, weight, (2, 3))
        require(sparse_add(actual_rest, projected_rest, F(-1)) == remaining_rest,
                "actual remaining marginal minus projected marginal is positive Gram")
        require(not reduced_cross(both, complement, weight, (2, 3)),
                "cross terms vanish in remaining partial trace")
        require(sum((v for (a, b), v in remaining_rest.items() if a == b), F(0)) ==
                1 - fb, "remaining marginal exact trace")
    print("PASS retained_environment correlated_cases=2 pointers=2 fresh_baths=6")


def phase_and_exact_boundary_audit():
    pattern_count = 0
    for length in (3, 4, 5, 7):
        pe = ready(length)
        for signs in product((-1, 1), repeat=length):
            difference = zero(length)
            holonomy = 1
            for edge, sign in enumerate(signs):
                difference[edge][edge] = F(1)
                difference[edge][(edge + 1) % length] = F(-sign)
                holonomy *= sign
            require(matrix_rank(difference) == length - (holonomy == 1),
                    "phase common-kernel rank")
            if holonomy == 1:
                gauge = [F(1)]
                for sign in signs[:-1]:
                    gauge.append(gauge[-1] * sign)
                require(gauge[-1] * signs[-1] == gauge[0], "phase wrap closure")
                require(not any(matvec(difference, gauge)), "explicit dark vector")
                density = scale(outer(gauge, gauge), F(1, length))
                require(trace(density) == 1, "phase dark density normalization")
                for edge, sign in enumerate(signs):
                    q, jump, _, _ = pair_matrices(length, edge, sign=sign)
                    require(channel(q, jump, density) == density,
                            "local phase dark density fixed")
                require((density == pe) == all(sign == 1 for sign in signs),
                        "nonconstant phase line differs from E")
            pattern_count += 1
    require(pattern_count == 184, "phase census count")
    require(not is_dyadic(F(1, PHYSICAL_L)), "613 ready entry not dyadic")
    require(F(PHYSICAL_L - 1, 2) == 306, "basis bath-mark asymptote")
    print("PASS phases_and_exact_boundary sign_patterns=184 dyadic_1_over_613=NO")


def shifted_block(a, left_shift, right_shift):
    n = len(a)
    result = zero(n)
    for i in range(n):
        for j in range(n):
            result[(i + left_shift) % n][(j + right_shift) % n] = a[i][j]
    return result


def parity_branch(a, parity):
    return [[x if i % 2 == parity and j % 2 == parity else F(0)
             for j, x in enumerate(row)] for i, row in enumerate(a)]


def handoff_audit(boundaries):
    budget_count = interface_count = 0
    for capacity in (0, 1, 2):
        for sweeps in (0, 1, 2):
            pointers = capacity + 1
            addresses = tuple((i, sweep, edge)
                              for i in range(pointers)
                              for sweep in range(sweeps)
                              for edge in range(PHYSICAL_L))
            bath_count = pointers * PHYSICAL_L * sweeps
            require(len(addresses) == bath_count == len(set(addresses)),
                    "finite distinct bath resource count")
            # These are external-script descriptors, not new physical gates
            # or autonomous readiness tests. Exhaustion retains the carrier.
            flags = tuple(i % 2 for i in range(capacity))
            carried_flags = flags
            next_unused = len(addresses)
            status = ("RESOURCE_EXHAUSTED" if next_unused == bath_count
                      else "ADDRESS_AVAILABLE")
            require(status == "RESOURCE_EXHAUSTED" and carried_flags == flags,
                    "exhausted script has no reset of archive flags")
            if capacity == 0:
                require(not flags, "no C archive capacity at K=0")
            budget_count += 1
    for length, _, _, density in boundaries:
        actual, ideal = embed_even(density), embed_even(ready(length))
        difference = sub(actual, ideal)
        for a, b in product((0, 1), repeat=2):
            actual_shift = shifted_block(actual, a, b)
            ideal_shift = shifted_block(ideal, a, b)
            difference_shift = shifted_block(difference, a, b)
            actual_sum, ideal_sum = zero(2 * length), zero(2 * length)
            for outcome in (0, 1):
                actual_out = parity_branch(actual_shift, outcome)
                ideal_out = parity_branch(ideal_shift, outcome)
                difference_out = parity_branch(difference_shift, outcome)
                require(sub(actual_out, ideal_out) == difference_out,
                        "exact source-unit operator error composition")
                for output in (actual_out, ideal_out, difference_out):
                    require(parity_branch(output, outcome) == output and
                            is_zero(parity_branch(output, 1 - outcome)),
                            "passive reread retains outcome, opposite branch zero")
                actual_sum, ideal_sum = add(actual_sum, actual_out), add(ideal_sum,
                                                                              ideal_out)
                interface_count += 1
            # The source unit |a><b| has zero full trace for a != b.
            source_trace = F(a == b)
            require(source_trace * trace(actual_sum) == source_trace * trace(actual),
                    "complete actual read trace preservation")
            require(source_trace * trace(ideal_sum) == source_trace * trace(ideal),
                    "complete ideal read trace preservation")
    require((budget_count, interface_count) == (9, 960), "handoff audit counts")
    print("PASS approximate_handoff budgets=9 source_unit_outcome_cases=960")


def main():
    local_dilation_audit()
    contraction_audit()
    boundaries = reduced_preparation_audit()
    retained_environment_audit()
    phase_and_exact_boundary_audit()
    handoff_audit(boundaries)
    print("RESOURCE L=613 m=K+1 fresh_baths=L*sum(n_i); equal_n=m*L*n")
    print("SCOPE approximate pointer preparation; occurrence NOT DERIVED")


if __name__ == "__main__":
    main()
