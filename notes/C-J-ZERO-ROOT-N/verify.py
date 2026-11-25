#!/usr/bin/env python3
"""Exact four-coordinate arithmetic audit for C-J-ZERO-ROOT-N (non-canonical)."""

import json
from itertools import combinations, product
from math import comb


P = 5
PHASES = range(P)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JOT = (0, 1, 0, 0)
BASIS = tuple(tuple(int(i == k) for i in range(4)) for k in range(4))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(c, x):
    return tuple(c * a for a in x)


def subtract(x, y):
    return add(x, scale(-1, y))


def residue(x):
    return tuple(a % P for a in x)


def multiply(x, y):
    """Integer multiplication modulo 1+j+j^2+j^3+j^4."""
    coeff = [0] * 7
    for i, a in enumerate(x):
        for k, b in enumerate(y):
            coeff[i + k] += a * b
    for i in range(6, 3, -1):
        for k in range(i - 4, i):
            coeff[k] -= coeff[i]
    return tuple(coeff[:4])


def powers(x, count):
    values = [ONE]
    for _ in range(1, count):
        values.append(multiply(values[-1], x))
    return values


def linear_combination(weights, vectors):
    acc = ZERO
    for w, v in zip(weights, vectors):
        acc = add(acc, scale(w, v))
    return acc


def field_trace(x):
    """Trace of the integer multiplication matrix in the power basis."""
    return sum(multiply(x, e)[i] for i, e in enumerate(BASIS))


ROOTS = powers(JOT, 5)
RHO = ROOTS[2]
J = add(ONE, RHO)
ELL = subtract(ONE, JOT)
DELTA = subtract(ROOTS[2], ROOTS[3])
SQRT5 = subtract(scale(-1, ONE), scale(2, add(ROOTS[2], ROOTS[3])))
ROTATIONS = powers(RHO, 5)
INVERSE_ROTATIONS = tuple(ROTATIONS[-k % P] for k in PHASES)
TRACE_ROWS = tuple(tuple(2 * field_trace(multiply(z, e)) for e in BASIS)
                   for z in ROTATIONS)


def conjugate(x):
    return linear_combination(x, tuple(ROOTS[-i % P] for i in range(4)))


def readings(x):
    return tuple(sum(a * b for a, b in zip(row, x)) for row in TRACE_ROWS)


def relative_integral(d):
    assert all((v - d[0]) % P == 0 for v in d)
    return tuple((v - d[0]) // P for v in d)


def relative(x):
    return residue(relative_integral(readings(x)))


def difference(word):
    return tuple((word[(k + 1) % P] - word[k]) % P for k in PHASES)


def adjacent(x):
    return difference(relative(x))


def from_adjacent(word):
    assert sum(word) % P == 0
    anchored = [0]
    for value in word[:4]:
        anchored.append((anchored[-1] + value) % P)
    return residue(scale(pow(2, -1, P), linear_combination(anchored, INVERSE_ROTATIONS)))


def evaluate(coeff):
    return tuple(sum(a * k**i for i, a in enumerate(coeff)) % P for k in PHASES)


def interpolate(indices, word):
    """Lagrange coefficients in ascending power order over F5."""
    result = [0] * len(indices)
    for k in indices:
        numerator = [1]
        denominator = 1
        for u in indices:
            if u == k:
                continue
            extended = [0] * (len(numerator) + 1)
            for i, a in enumerate(numerator):
                extended[i] -= u * a
                extended[i + 1] += a
            numerator = extended
            denominator *= k - u
        w = word[k] * pow(denominator, -1, P)
        for i, a in enumerate(numerator):
            result[i] = (result[i] + w * a) % P
    return tuple(result)


def exact_checks(x, d, integral):
    assert linear_combination(d, INVERSE_ROTATIONS) == scale(10, x)
    assert linear_combination(integral[1:], INVERSE_ROTATIONS[1:]) == scale(2, x)
    # Unused rho^2 coefficient is fixed at zero in this basis conversion.
    coeff = (x[0], x[2], 0, x[1], x[3])
    assert linear_combination(coeff, ROTATIONS) == x
    for k in PHASES:
        assert d[k] == 10 * coeff[-k % P] - 2 * sum(coeff)
        assert integral[k] == 2 * (coeff[-k % P] - coeff[0])


def lift_checks(x, d, anchored):
    for e in BASIS:
        for t in PHASES:
            y = scale(t, e)
            lifted = readings(add(x, scale(P, y)))
            assert relative_integral(lifted) == add(relative_integral(d),
                                                    scale(P, relative_integral(readings(y))))
            assert residue(relative_integral(lifted)) == anchored
            shifts = []
            for old, new in zip(d, lifted):
                assert (new - old) % P == 0
                shifts.append((new - old) // P % P)
                if old % P == 0:
                    assert (new // P - old // P) % P == shifts[-1]
            assert set(shifts) == {(-2 * sum(y)) % P}


def time_checks(x, q, in_root_layer):
    assert adjacent(multiply(RHO, x)) == q[1:] + q[:1]
    assert adjacent(multiply(J, x)) == tuple((q[k] + q[(k + 1) % P]) % P for k in PHASES)
    clock = tuple(adjacent(multiply(t, x))[0] for t in powers(J, 4))
    recovered = []
    for n, value in enumerate(clock):
        previous = sum(comb(n, i) * recovered[i] for i in range(n))
        recovered.append((value - previous) % P)
    recovered.append(-sum(recovered) % P)
    assert tuple(recovered) == q and from_adjacent(tuple(recovered)) == x
    if in_root_layer:
        first, second = clock[:2]
        linear = evaluate((first, second - 2 * first))
        assert linear == q and from_adjacent(linear) == x


def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))


def single_substitutions(words):
    """Every radius-one received word must have its unique correct nearest word."""
    count = 0
    for source in words:
        for i in PHASES:
            for error in range(1, P):
                damaged = list(source)
                damaged[i] = (damaged[i] + error) % P
                candidates = [w for w in words if hamming(w, damaged) <= 1]
                assert candidates == [source]
                count += 1
    return count


def reconstruct_subsets(words, dimension):
    count = 0
    for word in words:
        for indices in combinations(PHASES, dimension):
            coeff = interpolate(indices, word)
            assert evaluate(coeff) == word
            count += 1
    return count


def min_weight(words):
    return min(sum(value != 0 for value in word) for word in words if any(word))


def nilpotent_checks(root_layer):
    parameter_states = set()
    raw_words = set()
    adjacent_words = set()
    for a, b in product(PHASES, repeat=2):
        lift = multiply(SQRT5, add(scale(a, ONE), scale(b, DELTA)))
        parameter_states.add(residue(lift))
        raw_base = readings(lift)
        assert raw_base[0] == 0
        q = adjacent(lift)
        assert q == evaluate((3 * a + 2 * b, a))
        adjacent_words.add(q)
        for t in PHASES:
            d = readings(add(lift, scale(P * t, ONE)))
            assert all(v % P == 0 for v in d)
            f = tuple(v // P % P for v in d)
            c = f[0]
            assert c == 3 * t % P
            assert f == evaluate((c, 2 * b, 3 * a))
            assert difference(f) == q
            assert difference(q) == (a,) * P
            assert difference(difference(q)) == (0,) * P
            raw_words.add(f)
            for error in range(1, P):
                bad_anchor = (f[0] + error) % P
                corrupted = (bad_anchor,) + f[1:]
                good_relative = tuple((v - f[0]) % P for v in f[1:])
                bad_relative = tuple((v - bad_anchor) % P for v in corrupted[1:])
                assert hamming(good_relative, bad_relative) == 4
                assert hamming(q, difference(corrupted)) == 2
    assert parameter_states == root_layer
    assert raw_words == {evaluate(c) for c in product(PHASES, repeat=3)}
    assert adjacent_words == {evaluate(c) for c in product(PHASES, repeat=2)}
    return {
        "raw_nilpotent_words": len(raw_words),
        "raw_nilpotent_distance": min_weight(raw_words),
        "raw_single_errors": single_substitutions(raw_words),
        "adjacent_nilpotent_words": len(adjacent_words),
        "adjacent_single_errors": single_substitutions(adjacent_words),
        "raw_triple_reconstructions": reconstruct_subsets(raw_words, 3),
        "adjacent_pair_reconstructions": reconstruct_subsets(adjacent_words, 2),
    }


def main():
    if not __debug__:
        raise RuntimeError("run without Python optimization so that checks execute")
    assert multiply(SQRT5, SQRT5) == scale(P, ONE)
    assert subtract(J, conjugate(J)) == DELTA == multiply(RHO, ELL)
    witness = multiply(ELL, SQRT5)
    assert multiply(DELTA, subtract(witness, conjugate(witness))) == scale(P, ONE)

    states = tuple(product(PHASES, repeat=4))
    layers = [{residue(multiply(g, x)) for x in states} for g in powers(ELL, 5)]
    square_zero = {x for x in states if residue(multiply(x, x)) == ZERO}
    assert square_zero == layers[2]
    hermitian_kernel = set()
    anchored_layers = [set() for _ in layers]
    adjacent_layers = [set() for _ in layers]
    time_reconstructions = 0

    for x in states:
        d = readings(x)
        integral = relative_integral(d)
        exact_checks(x, d, integral)
        anchored = residue(integral)
        assert anchored[0] == 0
        q = difference(anchored)
        lift_checks(x, d, anchored)
        assert from_adjacent(q) == x
        assert all(v % P == (-2 * sum(x)) % P for v in d)
        assert all(v % P == 0 for v in d) == (x in layers[1])
        assert difference(difference(difference(q))) == (2 * sum(x) % P,) * P
        coeff = interpolate(PHASES, anchored)
        assert coeff[0] == 0 and evaluate(coeff) == anchored
        if x != ZERO:
            order = max(i for i, ideal in enumerate(layers) if x in ideal)
            degree = max(i for i, a in enumerate(coeff) if a != 0)
            assert degree == 4 - order
        for i, ideal in enumerate(layers):
            if x in ideal:
                anchored_layers[i].add(anchored[1:])
                adjacent_layers[i].add(q)
        jx = multiply(J, x)
        if residue(add(x, conjugate(x))) == ZERO and residue(add(jx, conjugate(jx))) == ZERO:
            hermitian_kernel.add(x)
        time_checks(x, q, x in layers[2])
        time_reconstructions += 1

    assert hermitian_kernel == layers[3]
    assert anchored_layers[4] == {(0,) * 4} and adjacent_layers[4] == {(0,) * 5}
    for i in range(4):
        coefficients = tuple(product(PHASES, repeat=4 - i))
        assert anchored_layers[i] == {evaluate((0,) + c)[1:] for c in coefficients}
        assert adjacent_layers[i] == {evaluate(c) for c in coefficients}
    audit = {
        "schema": "C-J-ZERO-ROOT-N/1",
        "states": len(states),
        "square_zero_states": len(square_zero),
        "relative_images": len(anchored_layers[0]),
        "ideal_sizes": [len(layer) for layer in layers],
        "anchored_min_distance": [min_weight(words) for words in anchored_layers[:4]],
        "adjacent_min_distance": [min_weight(words) for words in adjacent_layers[:4]],
        "hermitian_kernel_size": len(hermitian_kernel),
        "j_time_reconstructions": time_reconstructions,
    }
    audit.update(nilpotent_checks(square_zero))
    assert audit["ideal_sizes"] == [P**(4 - i) for i in range(5)]
    assert audit["relative_images"] == len(states)
    assert audit["anchored_min_distance"] == [1, 2, 3, 4]
    assert audit["adjacent_min_distance"] == [2, 3, 4, 5]
    assert audit["raw_nilpotent_distance"] == 3
    print(json.dumps(audit, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
