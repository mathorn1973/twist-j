#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL, claim #2137 section A: earlier fixed-word response.

The bare preparation is reconstructed from base() in
notes/C-H3-INTEGRATED-SILENT-ARCHIVE-N/verify.py at
f96db81df668f138d7242ddfa2c7d946ea892833. Only the pinned native H3
source is imported. Rational perturbations never choose parity or B tags.
"""

from fractions import Fraction
from functools import cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import gcd, lcm
from pathlib import Path
import sys


SOURCE_SHA = "4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd"
SOURCE = Path(sys.argv[1] if len(sys.argv) > 1 else
              "reproduce/h3-referenced-record/verify.py")
assert sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA
SPEC = spec_from_file_location("h3_response_source", SOURCE)
H = module_from_spec(SPEC)
sys.modules[SPEC.name] = H
SPEC.loader.exec_module(H)
H.transport_pair = cache(H.transport_pair)
H.collision = cache(H.collision)
Z, O, R, J, JI, P = H.ZERO, H.ONE, H.RHO, H.J, H.J_INV, H.J_POWERS
add, sub, mul, sc = H.add, H.sub, cache(H.mul), H.scale
ETA = sub(O, R)
NY, FINAL = 2, 114
EVENTS = (89, 90)
SLOT_NAMES = tuple(product((0, 6), range(NY), (2, 3)))
SLOTS = tuple(H.index(NY, *s) for s in SLOT_NAMES)


def account(field):
    return (H.ring_sum(z for i, z in enumerate(field) if i % 4 < 2),
            H.ring_sum(z for i, z in enumerate(field) if i % 4 >= 2),
            H.ring_sum(H.h(z) for z in field))


def bare(p):
    m = sub(sc(2, O), R)
    gs = sc(2, mul(J, m))
    a = sc(-3, ETA)
    b = add(add(mul(m, R), mul(J, a)), sc(12, J))
    stock = (Z, Z, Z, b, b, b, add(mul(m, R), sc(2, a)))
    field = []
    for x, y in product(range(8), range(NY)):
        d = (P[p] if y == 0 else sc(3, P[1])) if x == 0 else JI if x == 6 else Z
        clk = gs if x == 0 else (6, -2, 12, 1) if x == 6 else Z
        corr = (Z if x == 0 else stock[x - 1]) if y == 0 else gs
        field.extend((d, sc(-1, d), clk, corr))
    return tuple(field)


def history(initial):
    ac = account(initial)
    full, post, tags = [initial], [None], [None]
    for t in range(1, FINAL + 1):
        bit = (t - 1) % 2
        mid = H.transport(full[-1], NY, bit)
        out, events = H.collide(mid, NY)
        assert account(mid) == account(out) == ac
        assert H.transport(mid, NY, bit, True) == full[-1]
        assert H.transport(H.transport(mid, NY, bit, True), NY, bit) == mid
        assert H.collide(out, NY)[0] == mid
        full.append(out)
        post.append(mid)
        tags.append(events)
    return full, post, tags, ac


def linear_pair(a, b, multiplier):
    center = sc(Fraction(1, 2), add(a, b))
    difference = sc(Fraction(1, 2), mul(multiplier, sub(a, b)))
    return add(center, difference), sub(center, difference)


def advance_response(field, tick, positive):
    out = list(field)
    bit = (tick - 1) % 2
    before = positive[0][tick - 1]
    for rail in (2, 3):
        size, breadth = (8, NY) if rail == 3 else (NY, 8)
        for p, other in product(range(bit, size, 2), range(breadth)):
            q = (p + 1) % size
            if rail == 3:
                i, k = (H.index(NY, x, other, rail) for x in (p, q))
            else:
                i, k = (H.index(NY, other, y, rail) for y in (p, q))
            if H.even(sub(before[i], before[k])):
                out[i], out[k] = linear_pair(field[i], field[k], R)
    for x, y, tag in positive[2][tick]:
        i, k = H.index(NY, x, y, 2), H.index(NY, x, y, 3)
        out[i], out[k] = linear_pair(out[i], out[k], JI if tag == 1 else J)
    return tuple(out)


def ring_dot(a, b):
    return H.ring_sum(mul(x, y) for x, y in zip(a, b))


def field_solve(columns, target):
    """Exact RREF with left row certificates, including rank-deficient cases."""
    m, n = len(target), len(columns)
    rows = [[columns[c][r] for c in range(n)] + [target[r]] for r in range(m)]
    left = [[O if i == k else Z for k in range(m)] for i in range(m)]
    pivots = []
    for c in range(n):
        k = next((i for i in range(len(pivots), m) if rows[i][c] != Z), None)
        if k is None:
            continue
        r = len(pivots)
        rows[r], rows[k] = rows[k], rows[r]
        left[r], left[k] = left[k], left[r]
        iv = H.inverse(rows[r][c])
        rows[r] = [mul(iv, x) for x in rows[r]]
        left[r] = [mul(iv, x) for x in left[r]]
        for i in range(m):
            if i == r or rows[i][c] == Z:
                continue
            factor = rows[i][c]
            rows[i] = [sub(x, mul(factor, y)) for x, y in zip(rows[i], rows[r])]
            left[i] = [sub(x, mul(factor, y)) for x, y in zip(left[i], left[r])]
        pivots.append(c)
    bad = next((i for i, row in enumerate(rows)
                if all(x == Z for x in row[:-1]) and row[-1] != Z), None)
    if bad is not None:
        certificate = tuple(left[bad])
        assert all(ring_dot(certificate, col) == Z for col in columns)
        residual = ring_dot(certificate, target)
        assert residual == rows[bad][-1] != Z
        return len(pivots), len(pivots) + 1, certificate, residual, None, None
    particular = [Z] * n
    for r, c in enumerate(pivots):
        particular[c] = rows[r][-1]
    kernel = []
    for f in range(n):
        if f in pivots:
            continue
        v = [Z] * n
        v[f] = O
        for r, c in enumerate(pivots):
            v[c] = sc(-1, rows[r][f])
        kernel.append(tuple(v))
    assert tuple(H.ring_sum(mul(particular[c], columns[c][r]) for c in range(n))
                 for r in range(m)) == target
    return len(pivots), len(pivots), None, None, tuple(particular), tuple(kernel)


def egcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def integer_solve(matrix, target, width):
    """Solve integer rows successively, retaining a complete Z kernel basis."""
    particular = [0] * width
    basis = [[int(i == k) for i in range(width)] for k in range(width)]
    for row, value in zip(matrix, target):
        residual = value - sum(a * x for a, x in zip(row, particular))
        coeff = [sum(a * x for a, x in zip(row, vec)) for vec in basis]
        if not any(coeff):
            if residual:
                return None, None
            continue
        k = next(i for i, x in enumerate(coeff) if x)
        coeff[0], coeff[k] = coeff[k], coeff[0]
        basis[0], basis[k] = basis[k], basis[0]
        for k in range(1, len(coeff)):
            a, b = coeff[0], coeff[k]
            if not b:
                continue
            g, s, t = egcd(a, b)
            first, other = basis[0], basis[k]
            basis[0] = [s * x + t * y for x, y in zip(first, other)]
            basis[k] = [(-b // g) * x + (a // g) * y for x, y in zip(first, other)]
            coeff[0], coeff[k] = g, 0
        if residual % coeff[0]:
            return None, None
        multiplier = residual // coeff[0]
        particular = [x + multiplier * y for x, y in zip(particular, basis[0])]
        basis = basis[1:]
    assert all(sum(a * x for a, x in zip(row, particular)) == y
               for row, y in zip(matrix, target))
    assert all(all(sum(a * x for a, x in zip(row, vec)) == 0 for row in matrix)
               for vec in basis)
    return particular, basis


def integral_amplitudes(columns, target):
    """Test eta*z in O, retaining all nonzero amplitudes where possible.

    For w=eta*z solve sum(response*w)=eta*target over integers. A grid
    {0,...,n} in each integer kernel parameter avoids the union of n
    proper amplitude-zero affine subspaces whenever avoidance is possible.
    """
    n = len(columns)
    basis4 = tuple(tuple(int(i == k) for i in range(4)) for k in range(4))
    matrix, rhs = [], []
    for r in range(len(target)):
        coefficients = [mul(columns[c][r], e) for c in range(n) for e in basis4]
        out = mul(ETA, target[r])
        for component in range(4):
            row = [Fraction(z[component]) for z in coefficients]
            value = Fraction(out[component])
            denominator = lcm(*(x.denominator for x in row), value.denominator)
            matrix.append([int(x * denominator) for x in row])
            rhs.append(int(value * denominator))
    p, ker = integer_solve(matrix, rhs, 4 * n)
    if p is None:
        return "NO_ETA_INTEGRAL_SOLUTION", None
    for c in range(n):
        if not any(p[4*c:4*c+4]) and all(not any(v[4*c:4*c+4]) for v in ker):
            return "FORCED_ZERO_AMPLITUDE", None
    for parameters in product(range(n + 1), repeat=len(ker)):
        w = [p[i] + sum(a * v[i] for a, v in zip(parameters, ker)) for i in range(4*n)]
        words = tuple(tuple(w[4*c:4*c+4]) for c in range(n))
        if not all(word != Z for word in words):
            continue
        amplitudes = tuple(mul(H.inverse(ETA), word) for word in words)
        assert tuple(H.ring_sum(mul(amplitudes[c], columns[c][r]) for c in range(n))
                     for r in range(len(target))) == target
        return "NONZERO_ETA_INTEGRAL", amplitudes
    raise AssertionError("finite affine nonzero grid bound")


def main():
    histories = [history(bare(p)) for p in range(5)]
    assert len({h[3] for h in histories}) == 1
    assert H.scalar_account(histories[0][3][2]) == 2630
    positive = histories[1]
    target = tuple(sub(positive[0][0][i], positive[0][FINAL][i]) for i in SLOTS)
    assert target != (Z,) * len(SLOTS)
    print("A SCOPE fixed-positive-native-branch Q(j), events (89,90), terminal114")
    print("A SOURCE_SHA256", SOURCE_SHA)
    print("A SLOT_ORDER", SLOT_NAMES)
    print("A TARGET", target)
    print("A BASELINE_ACCOUNTS", positive[3], "Q", H.scalar_account(positive[3][2]))
    for p, h in enumerate(histories):
        restored = tuple(h[0][FINAL][i] == h[0][0][i] for i in SLOTS)
        assert all(restored) == (p != 1)
        print("A BASELINE_RESTORED", p, restored)
    # Verify the fixed radiative operator against the actual reference word.
    radiation = tuple(z if i % 4 >= 2 else Z for i, z in enumerate(positive[0][0]))
    for t in range(1, FINAL + 1):
        radiation = advance_response(radiation, t, positive)
        assert radiation == tuple(z if i % 4 >= 2 else Z
                                  for i, z in enumerate(positive[0][t]))
    print("A FIXED_OPERATOR_BASELINE_MATCH", FINAL)
    responses = []
    for t in EVENTS:
        incoming = tuple(h[1][t][H.index(NY, 4, 0, 3)] for h in histories)
        assert len({incoming[p] for p in (0, 2, 3, 4)}) == 1
        assert incoming[1] != incoming[0]
        assert all(not any(x == 4 for x, y, tag in h[2][t]) for h in histories)
        field = [Z] * 64
        field[H.index(NY, 4, 0, 3)] = O
        field[H.index(NY, 4, 0, 2)] = sc(-1, O)
        field = tuple(field)
        for tick in range(t + 1, FINAL + 1):
            field = advance_response(field, tick, positive)
        response = tuple(field[i] for i in SLOTS)
        responses.append(response)
        print("A EVENT", t, "INCOMING", incoming, "RESPONSE", response)
    counts = {"single_tests": 2, "pair_tests": 1, "field_solutions": 0,
              "nonzero_eta_integral": 0}
    for indices in ((0,), (1,), (0, 1)):
        columns = tuple(responses[i] for i in indices)
        name = tuple(EVENTS[i] for i in indices)
        rank, aug, certificate, residual, particular, kernel = field_solve(columns, target)
        print("A SYSTEM", name, "RANK", rank, "AUGMENTED", aug)
        if certificate is not None:
            print("A NO_SOLUTION", name, "LEFT_NULL", certificate, "TARGET_RESIDUAL", residual)
            continue
        counts["field_solutions"] += 1
        print("A FIELD_FAMILY", name, "PARTICULAR", particular, "KERNEL", kernel)
        disposition, amplitudes = integral_amplitudes(columns, target)
        print("A INTEGRAL_TEST", name, disposition, "AMPLITUDES", amplitudes)
        if amplitudes is not None:
            counts["nonzero_eta_integral"] += 1
            print("A ETA_AMPLITUDES", name, tuple(mul(ETA, a) for a in amplitudes))
    print("A COUNTS", tuple(sorted(counts.items())))
    print("A LIMIT hypothetical fixed-word response; no native restoration claim")


if __name__ == "__main__":
    main()
