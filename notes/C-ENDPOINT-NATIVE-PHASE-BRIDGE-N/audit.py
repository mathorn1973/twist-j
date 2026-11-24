#!/usr/bin/env python3
"""NON-CANONICAL frozen exact endpoint phase/native-reader audit.

No input files, floating point, numerical exponential or Hilbert truncation.
Q(zeta20) is used only for the supplied Schrodinger i and cyclotomic algebra.
The coherent norm, Hamiltonian and target time are not derived by this audit.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import sys


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def field(coefficients):
    out = [Fraction(x) for x in coefficients]
    out.extend([Fraction(0)] * max(0, 8-len(out)))
    # Phi20=x^8-x^6+x^4-x^2+1.
    for degree in range(len(out)-1, 7, -1):
        value = out[degree]
        out[degree] = Fraction(0)
        for offset, sign in ((2, 1), (4, -1), (6, 1), (8, -1)):
            out[degree-offset] += sign*value
    return tuple(out[:8])


ZERO = field([])
ONE = field([1])
T = field([0, 1])


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c*x for x in a)


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = [Fraction(0)]*15
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return field(out)


def power(a, n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


def conjugate(a):
    out = ZERO
    for k, x in enumerate(a):
        out = add(out, scale(power(T, (-k) % 20), x))
    return out


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def expectation(v, matrix):
    out = ZERO
    for row in range(2):
        for col in range(2):
            out = add(out, mul(conjugate(v[row]), mul(matrix[row][col], v[col])))
    return scale(out, Fraction(1, 2))  # norm squared is two


def serial(a):
    return [str(x) for x in a]


def phase_audit():
    zeta = power(T, 4)
    imag = power(T, 5)
    phi = add(add(ONE, zeta), conjugate(zeta))
    jseed = add(ONE, power(zeta, 2))
    require(power(T, 20) == ONE and power(T, 10) == scale(ONE, -1), "zeta20 order")
    require(mul(imag, imag) == scale(ONE, -1), "supplied i")
    require(power(zeta, 5) == ONE and zeta != ONE, "zeta5 order")
    require(mul(phi, phi) == add(phi, ONE), "golden relation")
    require(mul(phi, jseed) == zeta, "phi J=zeta5")
    require(mul(jseed, conjugate(jseed)) == sub(scale(ONE, 2), phi), "J norm")
    require(mul(zeta, conjugate(zeta)) == ONE, "unit phase norm")
    plus, minus = (ONE, zeta), (ONE, conjugate(zeta))
    for v in (plus, minus):
        norm2 = add(mul(conjugate(v[0]), v[0]), mul(conjugate(v[1]), v[1]))
        require(norm2 == scale(ONE, 2), "norm squared two")
    # Exact compression i[K,A]; the full f,g pair is not dynamically invariant.
    work = [[ZERO, scale(imag, Fraction(-1, 2))],
            [scale(imag, Fraction(1, 2)), ZERO]]
    current = [[scale(x, 2) for x in row] for row in work]
    wplus, wminus = expectation(plus, work), expectation(minus, work)
    require(wplus != ZERO and wminus == scale(wplus, -1), "opposite nonzero work")
    require(conjugate(wplus) == wplus, "real work mean")
    require(mul(wplus, wplus) == scale(add(phi, scale(ONE, 2)), Fraction(1, 16)),
            "square of work MEAN, not expectation of work square")
    require(expectation(plus, current) == scale(wplus, 2), "same current factor")
    # Eleven real symmetric compressions with the actual off-diagonal -1.
    for integer in range(-5, 6):
        diagonal_f = scale(ONE, integer)
        diagonal_g = add(scale(ONE, integer+1), phi)
        hmatrix = [[diagonal_f, scale(ONE, -1)], [scale(ONE, -1), diagonal_g]]
        require(expectation(plus, hmatrix) == expectation(minus, hmatrix),
                "conjugate equal Hamiltonian mean")
    dephased_work = scale(add(work[0][0], work[1][1]), Fraction(1, 2))
    require(dephased_work == ZERO and dephased_work != wplus, "phase erasure control")
    # Common J multiplication equals common zeta multiplication projectively.
    require(all(mul(phi, mul(jseed, a)) == mul(zeta, a) for a in plus),
            "common scalar normalized ray identity")
    c = [[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]]
    ident = [[int(i == j) for j in range(4)] for i in range(4)]
    c2, c3 = matmul(c, c), matmul(matmul(c, c), c)
    mphi = [[-c2[i][j]-c3[i][j] for j in range(4)] for i in range(4)]
    mj = [[ident[i][j]+c2[i][j] for j in range(4)] for i in range(4)]
    require(matmul(mphi, mj) == c, "integer phase matrix phi J")
    require(matmul(matmul(c3, c), c) == ident, "integer rotation order five")
    gram = [[5*int(i == j)-1 for j in range(4)] for i in range(4)]
    require(matmul(matmul(transpose(c), gram), c) == gram, "positive trace Gram preserved")
    require(gram == [[4, -1, -1, -1], [-1, 4, -1, -1],
                     [-1, -1, 4, -1], [-1, -1, -1, 4]], "trace metric fixture")
    return {"work_mean_plus_zeta20_coefficients": serial(wplus),
            "work_mean_minus_zeta20_coefficients": serial(wminus),
            "square_of_work_mean": "(phi+2)/16",
            "real_hamiltonian_diagonal_tests": 11,
            "dephased_work": "0",
            "integer_rotation_order": 5,
            "trace_gram_eigenvalues": [1, 5, 5, 5],
            "amplitude_encoding": "Z[zeta5]^2; supplied coherent norm/work rule",
            "native_preparation": "NOT DERIVED"}


def generator(index, x):
    a, b, c, d, q, r = x
    if index == 0:
        y = b, a, d, c, q, r
    elif index == 1:
        y = -c, -d, -a, -b, -q, -r
    elif index == 2:
        y = 2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r
    elif index == 3:
        y = 2-a, 1-b, 3-c, 4-d, 1-q, 1-r
    else:
        y = 2-a, 1-b, 3-c, 4-d, 2-q, 1-r
    return tuple(v % 5 for v in y)


def control(x, bit):
    return generator((sum(x)+2*bit) % 5, x)


def native_audit():
    heads = list(product(range(5), repeat=6))
    require(len(heads) == 15625, "complete native heads")
    controls = []
    sheet_maps = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
    for bit in (0, 1):
        counts = Counter(control(x, bit) for x in heads)
        histogram = Counter(counts.values())
        expected = {2: 3125, 3: 3125} if bit == 0 else {1: 6250, 3: 3125}
        require(dict(histogram) == expected, "native control fiber histogram")
        require(all(sum(control(x, bit)) % 5 == sheet_maps[bit][sum(x) % 5]
                    for x in heads), "native sheet map")
        controls.append({"bit": bit, "image_points": len(counts),
                         "fiber_histogram": dict(sorted(histogram.items()))})
    involutions = 0
    for x in heads:
        for index in range(5):
            require(generator(index, generator(index, x)) == x, "generator involution")
            involutions += 1
    x, y = (4, 1, 0, 0, 0, 0), (2, 1, 1, 2, 1, 0)
    collision = (1, 4, 0, 0, 0, 0)
    require(x != y and control(x, 0) == control(y, 0) == collision, "literal collision")
    final3 = [control(control(control(x, 0), 1), 1) for x in heads]
    fibers = Counter(final3)
    require(len(fibers) == 3125 and set(fibers.values()) == {5}, "E3 five-head fibers")
    require(all(sum(x) % 5 == 1 for x in final3), "origin synchronization sheet")
    pairs = {(end, sum(start) % 5) for start, end in zip(heads, final3)}
    require(len(pairs) == 15625, "retained-label/initial-phase product bijection")
    now = list(heads)
    image_sizes = []
    label_checks = 0
    for tick in range(32):
        bit = tick.bit_count() % 2
        now = [control(x, bit) for x in now]
        size = len(set(now))
        image_sizes.append(size)
        require(size == (6250 if tick < 2 else 3125), "fixed reachable image size")
        if tick >= 2:
            labels = {}
            for point, label in zip(now, final3):
                require(point not in labels or labels[point] == label,
                        "current checkpoint lost retained label")
                labels[point] = label
                label_checks += 1
            require(len(set(labels.values())) == 3125, "retained label bijection")
            require(len({sum(point) % 5 for point in now}) == 1, "selector phase synchronized")
    return {"complete_heads": len(heads), "controls": controls,
            "involution_cases": involutions,
            "literal_merger": {"head_a": x, "head_b": y, "output": collision},
            "E3_image_points": len(fibers), "E3_fiber_size": 5,
            "retained_label_phase_pairs": len(pairs),
            "continuation_ticks": 32, "image_sizes": image_sizes,
            "retained_label_checks": label_checks,
            "opposite_phase_encoding_on_merging_heads": "EXCLUDED by injective target theorem",
            "general_reader_class": "V^n G(ell_n), target V and G arbitrary",
            "native_hamiltonian_selection": "NOT DERIVED"}


def main():
    output = {"status": "NON-CANONICAL candidate-C finite audit only",
              "phase": phase_audit(), "native": native_audit(),
              "full_photon_phase": "NOT PROVED",
              "integer_to_hamiltonian_bridge": "NOT DERIVED",
              "verdict": "PASS frozen exact arithmetic and scoped native controls"}
    # Explicit LF bytes preserve the first-run artifact across platforms.
    sys.stdout.buffer.write((json.dumps(output, sort_keys=True, indent=2)+"\n").encode("utf-8"))


if __name__ == "__main__":
    main()
