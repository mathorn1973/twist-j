"""Five-coefficient finite arithmetic audit for C-J-ZERO-ROOT-N.

The preregistration was the sole specification. This is a same-session
separate implementation, with no authority or external review claim.
"""

import json
from itertools import combinations, product
from math import comb


FIELD = range(5)
ZERO = (0, 0, 0, 0, 0)
BASIS = tuple(tuple(int(i == j) for i in FIELD) for j in FIELD)
ONE = BASIS[0]
ELL = (1, -1, 0, 0, 0)
J = (1, 0, 1, 0, 0)
RHO = BASIS[2]
DELTA = (0, 0, 1, -1, 0)
S = (-1, 0, -2, -2, 0)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(n, x):
    return tuple(n * a for a in x)


def multiply(x, y):
    """Convolve the coefficients in Z[X]/(X^5-1)."""
    result = [0] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            result[(i + j) % 5] += a * b
    return tuple(result)


def conjugate(x):
    return tuple(x[-i % 5] for i in FIELD)


def integral_class(x):
    """In O a common shift of all five coefficients represents zero."""
    return tuple(a - x[4] for a in x)


def residue(x):
    return tuple(a % 5 for a in integral_class(x))


def trace(x):
    embeddings = (tuple(x[i * unit % 5] for i in FIELD) for unit in range(1, 5))
    fixed = integral_class(tuple(sum(column) for column in zip(*embeddings)))
    assert fixed[1:] == ZERO[1:], x
    return fixed[0]


def reader(x):
    return tuple(2 * trace(multiply(BASIS[2 * k % 5], x)) for k in FIELD)


def relative(d):
    changes = tuple(value - d[0] for value in d)
    assert all(change % 5 == 0 for change in changes), changes
    return tuple(change // 5 for change in changes)


def raw_reading(d):
    assert all(value % 5 == 0 for value in d), d
    return tuple((value // 5) % 5 for value in d)


def inverse_r(r):
    vector = ZERO
    for k in range(1, 5):
        vector = add(vector, scale(r[k], BASIS[-2 * k % 5]))
    return residue(scale(3, vector))


def adjacent(word):
    return tuple((word[(k + 1) % 5] - word[k]) % 5 for k in FIELD)


def poly_word(coefficients):
    return tuple(
        sum(a * k**i for i, a in enumerate(coefficients)) % 5
        for k in FIELD
    )


def interpolation_degree(word):
    # The leading order of the initial differences gives the degree
    # because all factorials through 4! are units in F5.
    degree = -1
    for order in range(5):
        if word[0]:
            degree = order
        word = tuple((b - a) % 5 for a, b in zip(word, word[1:]))
    return degree


def minimum_nonzero_weight(words):
    return min(sum(value != 0 for value in word) for word in words if any(word))


def puncture(word, positions):
    return tuple(word[i] for i in positions)


def check_punctures(words, count):
    reconstructions = 0
    for positions in combinations(FIELD, count):
        decoder = {puncture(word, positions): word for word in words}
        assert len(decoder) == len(words), positions
        for word in words:
            assert decoder[puncture(word, positions)] == word, (positions, word)
            reconstructions += 1
    return reconstructions


def check_one_errors(words, *, raw):
    decoder = {}
    for word in words:
        for position in FIELD:
            for error in range(1, 5):
                changed = list(word)
                changed[position] = (changed[position] + error) % 5
                received = tuple(changed)
                assert received not in words, (word, received)
                assert received not in decoder, (word, received, decoder.get(received))
                decoder[received] = word

                if raw:
                    # One error in raw observations changes adjacent symbols
                    # together. A corrupted anchor changes all four r entries.
                    changed_q = adjacent(received)
                    original_q = adjacent(word)
                    changed_positions = {
                        k for k in FIELD if changed_q[k] != original_q[k]
                    }
                    assert changed_positions == {position, (position - 1) % 5}
                    if position == 0:
                        original_r = tuple((v - word[0]) % 5 for v in word)
                        changed_r = tuple((v - received[0]) % 5 for v in received)
                        assert changed_r[0] == original_r[0] == 0
                        assert all(changed_r[k] != original_r[k] for k in range(1, 5))
    return len(decoder)


def main():
    assert integral_class(add(J, scale(-1, conjugate(J)))) == DELTA
    assert integral_class(multiply(RHO, ELL)) == DELTA
    assert integral_class(conjugate(ELL)) == integral_class(
        scale(-1, multiply(BASIS[4], ELL))
    )
    assert integral_class(multiply(S, S)) == scale(5, ONE)
    ell_squared = multiply(ELL, ELL)
    ell_fourth = multiply(ell_squared, ell_squared)
    unit = (0, -1, 1, -1, 0)
    unit_inverse = (-1, -1, 0, 1, 0)
    assert integral_class(ell_fourth) == scale(5, unit)
    assert integral_class(multiply(unit, unit_inverse)) == ONE

    states = {coords + (0,) for coords in product(FIELD, repeat=4)}
    layers = [states]
    for _ in range(4):
        layers.append({residue(multiply(ELL, x)) for x in layers[-1]})
    ideal_sizes = [len(layer) for layer in layers]
    assert ideal_sizes == [5 ** (4 - order) for order in FIELD], ideal_sizes
    assert all(upper > lower for upper, lower in zip(layers, layers[1:]))
    assert layers[1] == {x for x in states if sum(x) % 5 == 0}
    square_zero = {x for x in states if residue(multiply(x, x)) == ZERO}
    assert square_zero == layers[2]

    relative_images = {}
    adjacent_images = {}
    raw_from_lifts = set()
    for x in states:
        d = reader(x)
        l = relative(d)
        r = tuple(value % 5 for value in l)
        relative_images[x] = r
        adjacent_images[x] = adjacent(r)

        assert reader(add(x, (1,) * 5)) == d, x
        ten_x, two_x = ZERO, ZERO
        for k in FIELD:
            phase = BASIS[-2 * k % 5]
            ten_x = add(ten_x, scale(d[k], phase))
            two_x = add(two_x, scale(l[k], phase))
            assert d[k] == 10 * x[-2 * k % 5] - 2 * sum(x), (x, k)
            assert l[k] == 2 * (x[-2 * k % 5] - x[0]), (x, k)

        assert integral_class(ten_x) == scale(10, x), x
        assert integral_class(two_x) == scale(2, x), x
        assert inverse_r(r) == x, x

        if x != ZERO:
            order = max(i for i, layer in enumerate(layers) if x in layer)
            assert interpolation_degree(r) == 4 - order, (x, order)

        for direction in BASIS[:4]:
            for multiplier in FIELD:
                lifted = add(x, scale(5 * multiplier, direction))
                lifted_d = reader(lifted)
                assert tuple(v % 5 for v in relative(lifted_d)) == r, (x, lifted)
                if x in square_zero:
                    lifted_f = raw_reading(lifted_d)
                    raw_from_lifts.add(lifted_f)
                    f = raw_reading(d)
                    offset = (-2 * multiplier) % 5
                    assert lifted_f == tuple((v + offset) % 5 for v in f), (x, lifted)

    assert len(set(relative_images.values())) == len(states)
    assert set(relative_images.values()) == {
        (0,) + coordinates for coordinates in product(FIELD, repeat=4)
    }

    anchored_distances, adjacent_distances = [], []
    for order, layer in enumerate(layers[:-1]):
        dimension = 4 - order
        coefficients = list(product(FIELD, repeat=dimension))
        anchored_words = {relative_images[x][1:] for x in layer}
        adjacent_words = {adjacent_images[x] for x in layer}
        assert anchored_words == {poly_word((0,) + coeff)[1:] for coeff in coefficients}
        assert adjacent_words == {poly_word(coeff) for coeff in coefficients}
        anchored_distances.append(minimum_nonzero_weight(anchored_words))
        adjacent_distances.append(minimum_nonzero_weight(adjacent_words))
    assert anchored_distances == [1, 2, 3, 4], anchored_distances
    assert adjacent_distances == [2, 3, 4, 5], adjacent_distances

    raw_words = set()
    nilpotent_parameters = set()
    for a, b in product(FIELD, repeat=2):
        representative = multiply(S, add(scale(a, ONE), scale(b, DELTA)))
        x = residue(representative)
        nilpotent_parameters.add(x)

        assert adjacent_images[x] == poly_word((3 * a + 2 * b, a)), (a, b)
        actual_f = raw_reading(reader(representative))
        assert actual_f == poly_word((actual_f[0], 2 * b, 3 * a)), (a, b)
        for c in FIELD:
            word = poly_word((c, 2 * b, 3 * a))
            raw_words.add(word)
            first = adjacent(word)
            second = adjacent(first)
            assert first == adjacent_images[x], (a, b, c)
            assert second == (a,) * 5, (a, b, c)
            assert adjacent(second) == ZERO, (a, b, c)

    assert nilpotent_parameters == square_zero
    assert raw_words == raw_from_lifts
    assert len(raw_words) == 5**3
    raw_distance = minimum_nonzero_weight(raw_words)
    assert raw_distance == 3
    nilpotent_adjacent = {adjacent_images[x] for x in square_zero}
    assert len(nilpotent_adjacent) == len(square_zero)
    raw_triples = check_punctures(raw_words, 3)
    adjacent_pairs = check_punctures(nilpotent_adjacent, 2)
    raw_errors = check_one_errors(raw_words, raw=True)
    adjacent_errors = check_one_errors(nilpotent_adjacent, raw=False)

    hermitian_kernel = set()
    for x in states:
        x_bar = conjugate(x)
        h0 = residue(add(x, x_bar))
        h1 = residue(add(multiply(J, x), multiply(conjugate(J), x_bar)))
        if h0 == h1 == ZERO:
            hermitian_kernel.add(x)
    assert hermitian_kernel == layers[3]
    witness = multiply(ELL, S)
    witness_difference = add(witness, scale(-1, conjugate(witness)))
    assert integral_class(multiply(DELTA, witness_difference)) == scale(5, ONE)

    time_reconstructions = 0
    for x in states:
        q = adjacent_images[x]
        shifted = q[1:] + q[:1]
        assert adjacent_images[residue(multiply(RHO, x))] == shifted, x
        assert adjacent_images[residue(multiply(J, x))] == tuple(
            (v + w) % 5 for v, w in zip(q, shifted)
        ), x

        values = []
        evolved = x
        for _ in range(4):
            values.append(adjacent_images[evolved][0])
            evolved = residue(multiply(J, evolved))

        partial_q = tuple(
            sum((-1) ** (n - i) * comb(n, i) * values[i] for i in range(n + 1)) % 5
            for n in range(4)
        )
        recovered_q = partial_q + (-sum(partial_q) % 5,)
        assert recovered_q == q, x
        recovered_r = tuple(sum(recovered_q[:k]) % 5 for k in FIELD)
        assert inverse_r(recovered_r) == x, x
        time_reconstructions += 1

        if x in square_zero:
            intercept = values[0]
            slope = values[1] - 2 * values[0]
            two_reading_q = poly_word((intercept, slope))
            assert two_reading_q == q, x
            two_reading_r = tuple(sum(two_reading_q[:k]) % 5 for k in FIELD)
            assert inverse_r(two_reading_r) == x, x

    summary = {
        "schema": "C-J-ZERO-ROOT-N/1",
        "states": len(states),
        "square_zero_states": len(square_zero),
        "relative_images": len(set(relative_images.values())),
        "ideal_sizes": ideal_sizes,
        "anchored_min_distance": anchored_distances,
        "adjacent_min_distance": adjacent_distances,
        "raw_nilpotent_words": len(raw_words),
        "raw_nilpotent_distance": raw_distance,
        "raw_single_errors": raw_errors,
        "adjacent_nilpotent_words": len(nilpotent_adjacent),
        "adjacent_single_errors": adjacent_errors,
        "raw_triple_reconstructions": raw_triples,
        "adjacent_pair_reconstructions": adjacent_pairs,
        "hermitian_kernel_size": len(hermitian_kernel),
        "j_time_reconstructions": time_reconstructions,
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
