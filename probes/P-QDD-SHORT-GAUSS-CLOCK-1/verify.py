"""Exact, stdlib-only replay of a specified five-level control model."""

from collections import Counter
from fractions import Fraction as F
from itertools import product


LEVELS = range(5)
LINKS = 12
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
EMPTY = (ZERO,) * len(LEVELS)
CONTACT = (0, 1, -1, -1, -1)
ROUTES = {
    1: (("S", 0, 2), ("S", 1, 3)),
    2: (("S", 0, 2), ("S", 0, 3)),
    3: (("S", 0, 2),),
    4: (("S", 0, 2), ("S", 3, 4)),
}
CORE = (("C",), ("U",), ("U",), ("U",), ("S", 1, 4), ("U",), ("C",))
SIGN = ("Z", 2)
IDLE = ("I",)


# Coefficients a + b i/sqrt(5), represented by rational pairs.
def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(t, x):
    return t * x[0], t * x[1]


def conj(x):
    return x[0], -x[1]


def multiply(x, y):
    a, b = x
    c, d = y
    return a * c - b * d / 5, a * d + b * c


def norm_squared(x):
    return x[0] ** 2 + x[1] ** 2 / 5


def total(entries):
    result = ZERO
    for entry in entries:
        result = add(result, entry)
    return result


def vec_add(x, y):
    return tuple(add(a, b) for a, b in zip(x, y))


def vec_scale(t, x):
    return tuple(scale(t, a) for a in x)


def real_column(entries):
    return tuple((F(x), F(0)) for x in entries)


def basis(j):
    return tuple(ONE if i == j else ZERO for i in LEVELS)


def gamma(v):
    return tuple(
        total((v[(j - 1) % 5], v[(j + 1) % 5],
               scale(-1, v[(j - 2) % 5]), scale(-1, v[(j + 2) % 5])))
        for j in LEVELS
    )


def step(gate, v, adjoint=False):
    name, *addresses = gate
    if name == "I":
        return v
    if name == "U":
        mean = scale(F(1, 5), total(v))
        phase_sign = 1 if adjoint else -1
        return tuple(add(mean, scale(phase_sign, (-b / 5, a))) for a, b in gamma(v))
    if name == "C":
        dot = total(scale(s, x) for s, x in zip(CONTACT, v))
        return tuple(add(x, scale(F(-s, 2), dot)) for s, x in zip(CONTACT, v))
    out = list(v)
    if name == "S":
        i, j = addresses
        out[i], out[j] = out[j], out[i]
    elif name == "Z":
        i, = addresses
        out[i] = scale(-1, out[i])
    else:
        raise ValueError(f"Unknown gate {gate!r}")
    return tuple(out)


def apply(word, v):
    for gate in word:
        v = step(gate, v)
    return v


def schedule(k, reversed_sign=False):
    route = ROUTES[k]
    center = ((SIGN,) + CORE) if reversed_sign else (CORE + (SIGN,))
    return route + center + route[::-1]


def target(k, j, direction=1):
    out = list(basis(j))
    if k and j in (0, k):
        out[j] = F(4, 5), F(0)
        out[k if j == 0 else 0] = F(3 * direction if j == 0 else -3 * direction, 5), F(0)
    return tuple(out)


def channel_entry(columns, i, j, a, b):
    # Coefficient (a,b) in U |i><j| U†.
    return multiply(columns[i][a], conj(columns[j][b]))


def check_primitives():
    uniform = (ONE,) * len(LEVELS)
    assert gamma(uniform) == EMPTY
    for j in LEVELS:
        v = basis(j)
        assert gamma(gamma(v)) == vec_add(vec_scale(5, v), vec_scale(-1, uniform))
        assert apply((("U",),) * 4, v) == v
        assert apply((("U",),) * 3, v) == step(("U",), v, adjoint=True)
        assert step(("U",), step(("U",), v), adjoint=True) == v
        assert step(("C",), step(("C",), v)) == v
    difference = real_column((0, 1, 0, 0, -1))
    v = gamma(difference)
    assert v == real_column((0, 1, 2, -2, -1))
    assert step(("C",), v) == real_column((0, 0, 3, -1, 0))

    u = step(("U",), basis(0))
    u_adjoint = step(("U",), basis(0), adjoint=True)
    for col, orientation in ((u, 1), (u_adjoint, -1)):
        assert tuple(map(norm_squared, col)) == (F(1, 25),) + (F(6, 25),) * 4
        x, y = col[1:3]
        assert norm_squared(add(x, scale(-1, y))) / 2 == F(2, 5)
        assert norm_squared(add(x, y)) / 2 == F(2, 25)
        # Project onto (e1+i e2)/sqrt(2). Express the probability as
        # a+b sqrt(5), using Im(conj(x)y) = coefficient / sqrt(5).
        cross = multiply(conj(x), y)
        analyzer = (norm_squared(x) + norm_squared(y)) / 2, cross[1] / 5
        assert analyzer == (F(6, 25), F(2 * orientation, 25))
    print("PASS primitive identities and complex orientation analyzer with U-adjoint control")


def check_words():
    for k in range(1, 5):
        word = schedule(k)
        counts = Counter(gate[0] for gate in word)
        assert len(word) == (12, 12, 10, 12)[k - 1]
        assert counts == {"U": 4, "C": 2, "Z": 1, "S": len(word) - 7}
        actual = tuple(apply(word, basis(j)) for j in LEVELS)
        expected = tuple(target(k, j) for j in LEVELS)
        assert actual == expected
        wrong = tuple(apply(schedule(k, reversed_sign=True), basis(j)) for j in LEVELS)
        assert wrong == tuple(target(k, j, direction=-1) for j in LEVELS)
        assert wrong != actual
        for i, j, a, b in product(LEVELS, repeat=4):
            assert channel_entry(actual, i, j, a, b) == channel_entry(expected, i, j, a, b)
        assert norm_squared(actual[0][k]) == norm_squared(wrong[0][k]) == F(9, 25)
        for j, sign, expected_right, expected_wrong in (
            (0, 1, F(49, 50), F(1, 50)),
            (0, -1, F(1, 50), F(49, 50)),
            (k, 1, F(1, 50), F(49, 50)),
        ):
            for cols, probability in ((actual, expected_right), (wrong, expected_wrong)):
                assert norm_squared(add(cols[j][0], scale(sign, cols[j][k]))) / 2 == probability
    print("PASS 20 signed columns, 100 matrix units and direction-sensitive probabilities")


def weighted_adjacency(word, state):
    # Work in the unnormalized symmetric basis sqrt(binomial(m,q)) |q>.
    # A normalized forward weight sqrt((q+1)(m-q)) is q+1 here.
    # The reverse hop from q is m-q+1 and applies the adjoint data gate.
    out = [EMPTY] * (LINKS + 1)
    for q, v in enumerate(state):
        if v == EMPTY:
            continue
        if q < LINKS:
            moved = vec_scale(q + 1, step(word[q], v))
            out[q + 1] = vec_add(out[q + 1], moved)
        if q > 0:
            moved = vec_scale(LINKS - q + 1, step(word[q - 1], v, adjoint=True))
            out[q - 1] = vec_add(out[q - 1], moved)
    return out


def endpoint(word, initial):
    # Link unitarity makes the spectrum of A equal to m-2l (l=0,...,m).
    # For lambda*T=pi/2 and m divisible by four, exp(-i*pi*A/2)=(-1)^l.
    # Newton interpolation uses sum_n (-2)^n binomial(l,n), with
    # l=(m-A)/2. Apply each factor to the full clock/data vector.
    assert len(word) == LINKS and LINKS % 4 == 0
    term = [initial] + [EMPTY] * LINKS
    result = term.copy()
    for n in range(1, LINKS + 1):
        applied = weighted_adjacency(word, term)
        term = [
            vec_scale(F(1, n), vec_add(a, vec_scale(2 * n - 2 - LINKS, b)))
            for a, b in zip(applied, term)
        ]
        result = [vec_add(a, b) for a, b in zip(result, term)]
    return result


def check_clock():
    assert max((q + 1) * (LINKS - q) for q in range(LINKS)) == 42
    for k in LEVELS:
        word = schedule(k) if k else ()
        padded = word + (IDLE,) * (LINKS - len(word))
        for j in LEVELS:
            end = endpoint(padded, basis(j))
            assert end == [EMPTY] * LINKS + [target(k, j)]
    # A single substituted link still transfers the clock but changes data.
    word = schedule(1)
    modified = (IDLE,) + word[1:]
    end = endpoint(modified, basis(0))
    assert end == [EMPTY] * LINKS + [basis(2)]
    assert end[-1] != target(1, 0)
    print("PASS 25 initialized clock/data columns and altered-link control")


def check_timing_bound():
    # Sequential cost in units of pi/omega, as rational part plus
    # a coefficient of 1/sqrt(5). Read the resource counts from the words.
    for k in range(1, 5):
        counts = Counter(gate[0] for gate in schedule(k))
        rational_cost = F(counts["S"], 2) + F(counts["C"], 4) + counts["Z"]
        assert rational_cost <= 4 and F(counts["U"], 2) == 2
    # With all modeled link couplings available and lambda=supported headroom
    # divided by sqrt(42), T=pi sqrt(42)/(2 g_head).

    print('PASS conditional sequential timing and clock coupling bounds')


def main():
    if not __debug__:
        raise SystemExit("Run without -O.")
    check_primitives()
    check_words()
    check_clock()
    check_timing_bound()


if __name__ == "__main__":
    main()
